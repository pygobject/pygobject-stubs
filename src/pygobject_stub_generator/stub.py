from __future__ import annotations

from typing import Any
from typing import cast
from typing import Final
from typing import get_args
from typing import get_origin
from typing import TYPE_CHECKING
from typing import TypeAlias
from typing_extensions import get_overloads

import inspect
import re
import textwrap
from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
from dataclasses import replace
from enum import IntEnum
from enum import IntFlag
from types import ModuleType

import gi
import gi._gi as GI

from .arguments import Arguments
from .arguments import VisibleArgument
from .class_info import ClassInfo
from .import_info import FromImportInfo
from .import_info import ImportInfo
from .type_var_info import TypeVarInfo
from .type_var_info import TypeVarTupleInfo
from .utils import generate_full_name
from .utils import get_return_type
from .utils import make_nullable

gi.require_version("GIRepository", "3.0")

from gi.repository import GObject  # noqa: E402

if TYPE_CHECKING:
    from collections.abc import Callable

    from gi.repository import _GIRepository3 as GIRepository

    from .parse import Imports
    from .parse import Overrides
    from .parse import TypeVars
else:
    from gi.repository import GIRepository

_Object: TypeAlias = ModuleType | type[Any]

_identifier_re: Final = re.compile(r"^[A-Za-z_]\w*$")
_typing_re: Final = re.compile(r"(?:typing\.)(?P<name>\w+)\b")
_free_typing_re: Final = re.compile(r"\b(?P<name>Any|Self)\b")
_gi_repository_re: Final = re.compile(
    r"\bgi\.(?:repository|overrides)\.(?P<namespace>\w+)\.(?P<name>(?:\w+)(?:\.\w+)*)\b"
)
_import_re: Final = re.compile(
    r"\b(?P<module>(?:[A-Za-z_]\w+\.)*[A-Za-z_]\w+)\.(?P<name>[A-Za-z_]\w+)\b"
)
_type_vars_re: Final = re.compile(r"(?<!\w)[~+-](?P<name>[A-Za-z_]\w*)\b")
_strip_boolean_result_re: Final = re.compile(r"\bstrip_boolean_result\b")

_RESERVED_KEYWORDS: Final = {"async"}
_ALLOWED_FUNCTIONS: Final = {
    "__new__",
    "__init__",
    "__enter__",
    "__exit__",
    "__iter__",
    "__next__",
    "__getitem__",
    "__setitem__",
    "__delitem__",
    "__len__",
    "__int__",
    "__float__",
    "__bool__",
    "__contains__",
}

_GI_IMPORT_ALIASES: Final = {
    "gi.Boxed": ("GObject", "GBoxed"),
    "gobject.GInterface": ("GObject", "GInterface"),
}

_EXCLUDED_VARARGS_CALLBACKS: Final = {
    ("GLib", "DestroyNotify"),
}

_MODULE_NORMALIZATION: Final[dict[tuple[str, str | None], str]] = {
    ("typing", "Self"): "typing_extensions",  # 3.11+
    ("typing", "TypeVar"): "typing_extensions",  # default= 3.13+, infer_variance= 3.12+
    ("typing", "Unpack"): "typing_extensions",  # 3.11+
    ("typing", "TypeVarTuple"): "typing_extensions",  # 3.11+
}


def _normalize_module_name(module: str, name: str | None, /) -> str:
    return _MODULE_NORMALIZATION.get((module, name), module)


def _replace_optional(formatted: str) -> str:
    for prefix in ("typing.Optional[", "Optional["):
        while (idx := formatted.find(prefix)) != -1:
            depth = 0
            for i in range(idx + len(prefix) - 1, len(formatted)):
                if formatted[i] == "[":
                    depth += 1
                elif formatted[i] == "]":
                    depth -= 1
                    if depth == 0:
                        inner = formatted[idx + len(prefix) : i]
                        formatted = (
                            formatted[:idx] + inner + " | None" + formatted[i + 1 :]
                        )
                        break
    return formatted


def _replace_union(formatted: str) -> str:
    for prefix in ("typing.Union[", "Union["):
        while (start := formatted.find(prefix)) != -1:
            bracket_depth = 0
            for end in range(start + len(prefix) - 1, len(formatted)):
                if formatted[end] == "[":
                    bracket_depth += 1
                elif formatted[end] == "]":
                    bracket_depth -= 1
                    if bracket_depth == 0:
                        inner = formatted[start + len(prefix) : end]
                        # Split by top-level commas only
                        parts: list[str] = []
                        part_start = 0
                        nesting_depth = 0
                        for pos, char in enumerate(inner):
                            if char == "[":
                                nesting_depth += 1
                            elif char == "]":
                                nesting_depth -= 1
                            elif char == "," and nesting_depth == 0:
                                parts.append(inner[part_start:pos].strip())
                                part_start = pos + 1
                        parts.append(inner[part_start:].strip())
                        formatted = (
                            formatted[:start] + " | ".join(parts) + formatted[end + 1 :]
                        )
                        break
    return formatted


@dataclass(slots=True)
class Stub:
    repo: GIRepository.Repository
    parent: _Object
    namespace: str
    overrides: Overrides
    imports: InitVar[Imports]
    typevars: InitVar[TypeVars]
    needed_imports: dict[tuple[str, str | None], FromImportInfo | ImportInfo] = field(
        init=False
    )
    needed_typevars: list[TypeVarInfo | TypeVarTupleInfo] = field(
        init=False, default_factory=list
    )
    known_namespaces: set[str] = field(init=False, default_factory=set)
    known_namespaces_prefixes: tuple[str, ...] = field(
        init=False, default_factory=tuple
    )

    def __post_init__(self, imports: Imports, typevars: TypeVars) -> None:
        self.needed_imports = {}

        for _import in imports:
            name = (
                (
                    _import.import_as or _import.name
                    if _import.module == "gi.repository"
                    else _import.name
                )
                if isinstance(_import, FromImportInfo)
                else None
            )
            module = _normalize_module_name(_import.module, name)

            self.needed_imports[(module, name)] = replace(_import, module=module)

        self.known_namespaces = {
            dependency.rsplit("-", 1)[0]
            for dependency in self.repo.get_dependencies(self.namespace)
        } | {self.namespace}
        self.known_namespaces_prefixes = tuple(
            f"{namespace}." for namespace in self.known_namespaces
        )

        self.needed_typevars = list(typevars)

        if self.namespace == "Gtk":
            self.get_import("os")

    def check_override(self, prefix: str, name: str) -> str | None:
        full_name = generate_full_name(prefix, name)
        if full_name in self.overrides:
            return "# override\n" + self.__fix_annotations(self.overrides[full_name])
        return None

    def __get_import(
        self, module: str, /, name: str | None = None
    ) -> FromImportInfo | ImportInfo | None:
        module = _normalize_module_name(module, name)
        return self.needed_imports.get((module, name))

    def __add_import(
        self,
        module: str,
        /,
        name: str | None = None,
        import_as: str | None = None,
    ) -> ImportInfo | FromImportInfo:
        module = _normalize_module_name(module, name)

        import_object = (
            ImportInfo(module, import_as)
            if name is None
            else FromImportInfo(module, name, import_as)
        )

        self.needed_imports[(module, name)] = import_object

        return import_object

    def get_import(self, module: str, name: str | None = None) -> str:
        if (_import := self.__get_import(module, name)) is not None:
            return _import.symbol

        if name is None:
            self.__add_import(module)
            return module

        if module == "builtins":
            return name

        symbols = [_import.symbol for _import in self.needed_imports.values()]
        import_as = name
        while import_as in symbols:
            import_as = f"_{import_as}"

        self.__add_import(module, name, None if import_as == name else import_as)
        return import_as

    def get_namespace_member(
        self,
        namespace: str,
        name: str,
        /,
    ) -> str:
        if namespace == self.namespace:
            return name

        if namespace in ("_gi", "_gtktemplate"):
            if (_import := self.__get_import("gi", namespace)) is None:
                _import = self.__add_import("gi", namespace)
        elif namespace == "_gi_gst":
            if (_import := self.__get_import("gi.overrides", "_gi_gst")) is None:
                _import = self.__add_import("gi.overrides", "_gi_gst")
        elif namespace == "cairo":
            if (_import := self.__get_import(namespace)) is None:
                _import = self.__add_import(namespace)
        elif (_import := self.__get_import("gi.repository", namespace)) is None:
            _import = self.__add_import("gi.repository", namespace)

        return f"{_import.symbol}.{name}"

    def get_typevar(
        self,
        name: str,
        /,
        *constraints: str,
        default: str | None = None,
        bound: str | None = None,
        covariant: bool = False,
        contravariant: bool = False,
        # TODO: https://github.com/python/mypy/issues/17811
        # Since mypy doesn't support infer_variance, we'll disable this for now and
        # enable it when/if it's supported (or when 3.11 is dropped)
        # infer_variance: bool = False,
    ) -> str:
        if covariant and not contravariant:
            name = f"{name}_co"

        if contravariant and not covariant:
            name = f"{name}_contra"

        typevar = TypeVarInfo(
            name,
            default,
            constraints if constraints else None,
            bound,
            contravariant=contravariant,
            covariant=covariant,
            # infer_variance=infer_variance,
        )

        if typevar not in self.needed_typevars:
            self.needed_typevars.append(typevar)

        return name

    def get_typevar_tuple(self, name: str, /, *, default: str | None = None) -> str:
        if default is not None:
            unpack_symbol = self.get_import("typing", "Unpack")
            default = f"{unpack_symbol}[{default}]"

        typevar_tuple = TypeVarTupleInfo(name, default)

        if typevar_tuple not in self.needed_typevars:
            self.needed_typevars.append(typevar_tuple)

        return name

    def get_callback_typevar_tuple(self) -> str:
        return self.get_typevar_tuple("_DataTs", default="tuple[()]")

    def get_final(self, annotation: str | None = None) -> str:
        final_symbol = self.get_import("typing", "Final")

        if annotation is None:
            return final_symbol

        return (
            annotation
            if f"{final_symbol}[" in annotation
            else f"{final_symbol}[{annotation}]"
        )

    def get_alias(self, name: str, obj: object, /) -> str | None:
        if obj.__module__.startswith(("gi.overrides.", "gi.repository.")):
            namespace = obj.__module__.rsplit(".", 1)[1]
        elif obj.__module__ == "gobject" or obj.__module__ == "gi._gi":
            namespace = "_gi"
        elif obj.__module__ == "gi._gtktemplate":
            return self.get_namespace_member("_gtktemplate", obj.__qualname__)  # type: ignore[attr-defined]
        else:
            return None

        if namespace != self.namespace or name != obj.__qualname__:  # type: ignore[attr-defined]
            return self.get_namespace_member(namespace, obj.__qualname__)  # type: ignore[attr-defined]

        return None

    def get_property(
        self, name: str, return_annotation: str, /, *, indent: str = ""
    ) -> str:
        property_symbol = self.get_import("builtins", "property")
        return f"{indent}@{property_symbol}\n{indent}def {name}(self) -> {
            return_annotation
        }: ..."

    def get_class_import(self, cls: type[Any], /) -> str:
        # Things like Generic and Protocol show up in the MRO as `Generic` rather than
        # `Generic[T]`, so we need to get the original class to get the type arguments
        # to recreate them in the stubs
        origin_cls = get_origin(cls) or cls

        # TODO: track generics and properly create them in the stub
        arg_names = [arg.__name__ for arg in get_args(cls)]
        args = f"[{', '.join(arg_names)}]" if arg_names else ""

        full_name = f"{origin_cls.__module__}.{origin_cls.__qualname__}"

        ns: str | None = None
        name = ""

        if alias := _GI_IMPORT_ALIASES.get(full_name):
            ns, name = alias
        elif full_name.startswith(("gi.overrides.", "gi.repository.")):
            _, _, ns, name = full_name.split(".", 3)
        elif full_name.startswith(("gi.", "_gi.", "GI.", "_GI.", "gobject.")):
            ns, name = full_name.split(".", 1)
            ns = "_gi"
        elif full_name.startswith("cairo."):
            ns, name = full_name.split(".", 1)

        if ns is not None:
            return f"{self.get_namespace_member(ns, name)}{args}"

        module, name = full_name.rsplit(".", 1)
        return f"{self.get_import(module, name)}{args}"

    def fix_argument_name(self, name: str | None, /) -> str:
        if name is None:
            raise ValueError("Argument name cannot be None")

        if name in _RESERVED_KEYWORDS:
            name = f"_{name}"
        return name.replace("-", "_")

    def get_callable_arguments(
        self, info: GI.CallableInfo, /, *, allow_varargs: bool = True
    ) -> tuple[dict[str, str], list[str]]:
        arguments = Arguments.for_callable(info, allow_varargs=allow_varargs)

        py_args: list[VisibleArgument] = []
        return_args: list[str] = []
        required_indexes: set[int] = set()

        for arg in arguments:
            if arg.from_python and not arg.is_varargs_slot:
                py_args.append(arg)

                if arg.required:
                    required_indexes.add(arg.c_index)

            if arg.to_python:
                return_args.append(
                    self.type_info_to_python(
                        arg.info.get_type_info(), out=True, nullable=arg.nullable
                    )
                )

        last_required = max(required_indexes, default=-1)
        args: dict[str, str] = {}

        for py_arg in py_args:
            arg_type = self.type_info_to_python(
                py_arg.info.get_type_info(),
                nullable=py_arg.nullable,
                varargs_callback=py_arg.is_varargs_callback,
                closure_argument=py_arg.is_closure_target,
            )

            if arguments.can_have_defaults and py_arg.c_index > last_required:
                arg_type = f"{arg_type} = {'None' if py_arg.nullable else '...'}"

            args[self.fix_argument_name(py_arg.info.get_name())] = arg_type

        if (varargs_info := arguments.varargs_info) is not None:
            args[f"*{self.fix_argument_name(varargs_info.get_name())}"] = f"{
                self.get_import('typing', 'Unpack')
            }[{self.get_callback_typevar_tuple()}]"

        return_type = info.get_return_type()
        if not info.skip_return() and (
            return_type.get_tag() != GI.TypeTag.VOID or return_type.is_pointer()
        ):
            return_args = [
                self.type_info_to_python(
                    return_type, out=True, nullable=info.may_return_null()
                ),
                *return_args,
            ]

        return args, return_args

    def type_info_to_python(
        self,
        info: GI.TypeInfo,
        /,
        *,
        out: bool = False,
        nullable: bool = False,
        varargs_callback: bool = False,
        closure_argument: bool = False,
    ) -> str:
        tag = info.get_tag()

        py_type: str | None = None

        match tag:
            case GI.TypeTag.BOOLEAN:
                py_type = "bool"
            case (
                GI.TypeTag.INT8
                | GI.TypeTag.INT16
                | GI.TypeTag.INT32
                | GI.TypeTag.INT64
                | GI.TypeTag.UINT8
                | GI.TypeTag.UINT16
                | GI.TypeTag.UINT32
                | GI.TypeTag.UINT64
            ):
                py_type = "int"
            case GI.TypeTag.DOUBLE | GI.TypeTag.FLOAT:
                py_type = "float"
            case GI.TypeTag.UTF8 | GI.TypeTag.FILENAME | GI.TypeTag.UNICHAR:
                py_type = "str"
            case GI.TypeTag.ARRAY | GI.TypeTag.GLIST | GI.TypeTag.GSLIST:
                value_info = info.get_param_type(0)

                if TYPE_CHECKING:
                    assert value_info is not None

                value_type = self.type_info_to_python(value_info, out=out)

                if tag == GI.TypeTag.ARRAY:
                    if out:
                        # As output argument array of type uint8 are returned as bytes
                        if value_info.get_tag() == GI.TypeTag.UINT8:
                            py_type = "bytes"
                        else:
                            py_type = f"list[{value_type}]"
                    else:
                        # As input arguments array can be generated by any sequence
                        py_type = f"{self.get_import('collections.abc', 'Sequence')}[{
                            value_type
                        }]"
                else:
                    py_type = f"list[{value_type}]"

                # All return/out/inout arrays/lists get marshalled as a list, regardless
                # of nullable
                nullable = nullable and not out
            case GI.TypeTag.GHASH:
                key_info = info.get_param_type(0)
                value_info = info.get_param_type(1)

                if TYPE_CHECKING:
                    assert key_info is not None
                    assert value_info is not None

                key_type = self.type_info_to_python(key_info, out=out)
                value_type = self.type_info_to_python(value_info, out=out)
                collection_type = (
                    "dict" if out else self.get_import("collections.abc", "Mapping")
                )

                py_type = f"{collection_type}[{key_type}, {value_type}]"
            case GI.TypeTag.INTERFACE:
                interface_info = info.get_interface()

                if isinstance(interface_info, GI.CallbackInfo):
                    # TODO: enable this when PyGObject exposes CallbackInfos
                    # if (
                    #     callback_name := interface_info.get_name()
                    # ) and not interface_info.get_container():
                    #     # Reference named callbacks directly
                    #     py_type = self.get_namespace_member(
                    #         interface_info.get_namespace(), callback_name
                    #     )
                    #
                    #     if (
                    #         varargs_callback
                    #         and (
                    #             interface_info.get_namespace(),
                    #             interface_info.get_name(),
                    #         )
                    #         not in _EXCLUDED_VARARGS_CALLBACKS
                    #     ):
                    #         py_type = f"{py_type}[{
                    #             self.get_import('typing', 'Unpack')
                    #         }[{self.get_callback_typevar_tuple()}]]"
                    # else:
                    #     # Generate the `Callable[]` annotation for anonymous callbacks
                    #     (callback_args, callback_return_args) = (
                    #         self.get_callable_arguments(
                    #            interface_info, allow_varargs=varargs_callback
                    #         )
                    #     )
                    #     callback_return_type = get_return_type(callback_return_args)
                    #
                    #     py_type = f"{
                    #         self.get_import('collections.abc', 'Callable')
                    #     }[[{
                    #         ', '.join(callback_args.values())
                    #     }], {callback_return_type}]"
                    (callback_args, callback_return_args) = self.get_callable_arguments(
                        interface_info, allow_varargs=varargs_callback
                    )
                    callback_return_type = get_return_type(callback_return_args)

                    py_type = f"{self.get_import('collections.abc', 'Callable')}[[{
                        ', '.join(callback_args.values())
                    }], {callback_return_type}]"
                elif interface_info is not None:
                    interface_namespace = interface_info.get_namespace()
                    interface_name = interface_info.get_name()

                    if interface_namespace == "GObject" and interface_name == "Value":
                        py_type = self.get_import("typing", "Any")

                    elif (
                        interface_namespace == "GObject" and interface_name == "Closure"
                    ):
                        py_type = f"{
                            self.get_import('collections.abc', 'Callable')
                        }[..., {self.get_import('typing', 'Any')}]"

                    elif (
                        interface_namespace == "cairo"
                        and interface_name == "Context"
                        and not out
                    ):
                        some_surface = self.get_typevar(
                            "_SomeSurface",
                            bound=f"{self.get_namespace_member('cairo', 'Surface')}",
                        )
                        py_type = f"{self.get_namespace_member('cairo', 'Context')}[{
                            some_surface
                        }]"
                    else:
                        py_type = self.get_namespace_member(
                            interface_namespace, f"{interface_name}"
                        )
            case GI.TypeTag.VOID:
                if info.is_pointer():
                    if closure_argument:
                        # Arguments passed to callbacks are specially handled by the
                        # PyGObject marshalling code, so they can be anything
                        py_type = f"{self.get_import('typing', 'Any')} | None"
                    else:
                        # Pointers can be int | CapsuleType | None, but we don't have
                        # CapsuleType until 3.13 This is what typeshed did until 3.13
                        py_type = (
                            "int"
                            if out
                            else f"int | {self.get_import('typing', 'Any')} | None"
                        )

                    # All return/out/inout pointers get marshalled as int, regardless of
                    # nullable
                    nullable = nullable and not out
                else:
                    py_type = "None"
            case GI.TypeTag.GTYPE:
                py_type = f"type[{self.get_import('typing', 'Any')}]"
            case GI.TypeTag.ERROR:
                py_type = self.get_namespace_member("GLib", "Error")

        if py_type is None:
            raise ValueError(f"Unsupported GI type tag: {tag}")

        if nullable:
            py_type = make_nullable(py_type)

        return py_type

    def __replace_typing(self, match: re.Match[str]) -> str:
        match match.group("name"):
            case ("Callable" | "Sequence" | "Iterable" | "Iterator") as name:
                symbol = self.get_import("collections.abc", name)
            case "ContextManager" as name:
                symbol = self.get_import("contextlib", f"Abstract{name}")
            case "Type" | "Tuple" | "List" | "Dict" | "Set" | "FrozenSet" as name:
                symbol = name.lower()
            case _ as name:
                symbol = self.get_import("typing", name)

        return symbol

    def __replace_free_typing(self, match: re.Match[str]) -> str:
        name = match.group("name")
        return self.get_import("typing", name)

    def __replace_import(self, match: re.Match[str]) -> str:
        module = match.group("module")
        name = match.group("name")

        if module.startswith(
            ("gi.repository.", "gi.overrides.", "_gi.", *self.known_namespaces_prefixes)
        ):
            if module.startswith(f"{self.namespace}."):
                return f"{module.split('.', 1)[1]}.{name}"
            return f"{module}.{name}"

        if module in self.known_namespaces:
            if module == self.namespace:
                return name
            return f"{module}.{name}"

        if module in {"gi", "gobject"}:
            if name == "Struct":
                return self.get_namespace_member("_gi", "Struct")
            return f"gi.repository.GObject.{name}"

        return self.get_import(module, name)

    def __replace_gi_repository(self, match: re.Match[str]) -> str:
        namespace = match.group("namespace")
        symbol = self.get_namespace_member(namespace, match.group("name"))
        return f"{symbol}"

    def __fix_annotations(self, formatted: str, /, *, fix_imports: bool = False) -> str:
        formatted = _replace_optional(formatted)
        formatted = _replace_union(formatted)
        formatted = _typing_re.sub(self.__replace_typing, formatted)
        formatted = _free_typing_re.sub(self.__replace_free_typing, formatted)
        formatted = re.sub(
            rf"\b{self.get_import('typing', 'Generator')}\[(.*?), None, None\]",
            rf"{self.get_import('collections.abc', 'Iterator')}[\1]",
            formatted,
        )
        if fix_imports:
            formatted = _import_re.sub(self.__replace_import, formatted)
        formatted = _gi_repository_re.sub(self.__replace_gi_repository, formatted)
        formatted = _type_vars_re.sub(r"\g<name>", formatted)
        return re.sub(rf"\b{self.namespace}\.", r"", formatted)

    def format_annotation(
        self, annotation: object, /, *, fix_imports: bool = False
    ) -> str:
        try:
            # This requires Python 3.14
            formatted = inspect.formatannotation(
                annotation,
                quote_annotation_strings=False,  # pyright: ignore[reportCallIssue]
            )
        except Exception:
            # This should be a good enough fallback for older Pythons
            formatted = (
                inspect.formatannotation(annotation).replace('"', "").replace("'", "")
            )

        return self.__fix_annotations(formatted, fix_imports=fix_imports)

    def format_signature(self, signature: inspect.Signature) -> str:
        try:
            # This requires Python 3.14
            formatted = signature.format(quote_annotation_strings=False)  # pyright: ignore[reportAttributeAccessIssue]
        except Exception:
            # This should be a good enough fallback for older Pythons
            formatted = str(signature).replace('"', "").replace("'", "")

        return self.__fix_annotations(formatted, fix_imports=True)

    # TODO: enable this when PyGObject exposes CallbackInfos
    # def __build_callback_type(self, callback_info: GI.CallbackInfo) -> str:
    #     name = f"{callback_info.get_name()}"
    #
    #     if override := self.check_override("", name):
    #         return override
    #
    #     # NOTE: Use `type X =` when 3.11 is dropped
    #     type_alias = self.get_import("typing", "TypeAlias")
    #     signature = callback_info.__signature__
    #
    #     callback_data_arg_name = next(
    #         (
    #             arg.get_name()
    #             for arg in callback_info.get_arguments()
    #             if arg.get_closure_index() > -1
    #         ),
    #         None,
    #     )
    #
    #     annotation = self.format_annotation(
    #         Callable[
    #             [
    #                 self.get_callback_typevar_tuple()
    #                 if param.name == callback_data_arg_name
    #                 else param.annotation
    #                 for param in signature.parameters.values()
    #             ],
    #             signature.return_annotation,
    #         ],
    #         fix_imports=True,
    #     )
    #
    #     if callback_data_arg_name is not None:
    #         unpack_symbol = self.get_import("typing", "Unpack")
    #         annotation = re.sub(
    #             r"""['"]_DataTs['"]""",
    #             f"{unpack_symbol}[_DataTs]",
    #             annotation,
    #         )
    #
    #     return f"""{name}: {type_alias} = {annotation}"""
    #
    # def __build_callback_types(self) -> str:
    #     lines: list[str] = []
    #
    #     gi_repo = gi.Repository.get_default()
    #     for callback_info in gi_repo.get_infos(self.namespace):
    #         if not isinstance(callback_info, GI.CallbackInfo):
    #             continue
    #
    #         lines.append(self.__build_callback_type(callback_info))
    #
    #     return "\n".join(lines)

    def __build_function(
        self,
        name: str,
        function: GI.FunctionInfo | GI.VFuncInfo,
        in_class: type[Any] | None,
        return_signature: str | None = None,
        comment: str | None = None,
    ) -> str:
        constructor: bool = False
        method: bool = isinstance(function, GI.VFuncInfo)
        static: bool = False

        # Flags
        function_flags = function.get_flags()

        if function_flags & GI.FunctionInfoFlags.IS_CONSTRUCTOR:
            constructor = True

        if function_flags & GI.FunctionInfoFlags.IS_METHOD:
            method = True

        if in_class and not method and not constructor:
            static = True

        # Arguments
        args, return_args = self.get_callable_arguments(function)
        args_types = [
            f"{self.fix_argument_name(name)}: {arg}" for name, arg in args.items()
        ]

        return_type = (
            return_signature if return_signature else get_return_type(return_args)
        )

        # Generate string
        prepend = ""
        if constructor:
            if name == "__init__":
                # We pass the "new" constructor with the name __init__ because type
                # checkers do better with __init__ signatures, so we have to change the
                # signature a bit
                args_types.insert(0, "self")
                return_type = "None"
            else:
                prepend = "@classmethod\n"
                args_types.insert(0, "cls")
                # Override return value, for example Gtk.Button.new returns a Gtk.Widget
                # instead of Gtk.Button
                rt = function.get_container().get_name()
                if rt is not None and return_type != f"{rt} | None":
                    return_type = rt
        elif method:
            args_types.insert(0, "self")
        elif static:
            prepend = "@staticmethod\n"

        if comment:
            return f"{prepend}def {name}({', '.join(str(a) for a in args_types)}) -> {
                return_type
            }: ... # {comment}\n"

        return f"{prepend}def {name}({', '.join(str(a) for a in args_types)}) -> {
            return_type
        }: ...\n"

    def __wrapped_strip_boolean_result(
        self,
        name: str,
        function: Callable[..., Any],
        in_class: type[Any] | None,
    ) -> str:
        real_function = cast("GI.FunctionInfo", cast("Any", function).__wrapped__)
        fail_ret = inspect.getclosurevars(function).nonlocals.get("fail_ret")

        _, return_args = self.get_callable_arguments(real_function)
        return_args = return_args[1:]  # Strip first return value

        return_signature = get_return_type(return_args)

        if fail_ret is None:
            return_signature = make_nullable(f"{return_signature}")
        else:
            if type(fail_ret) is tuple:
                if len(fail_ret) > 0:
                    return_signature = f"({return_signature} | tuple{
                        str(fail_ret).replace('(', '[').replace(')', ']')
                    })"
                else:
                    return_signature = f"({return_signature} | tuple[()])"
            else:
                return_signature = f"({return_signature} | {
                    self.get_import('typing', 'Literal')
                }[{fail_ret}])"

        return self.__build_function(
            name,
            real_function,
            in_class,
            return_signature,
            "CHECK Wrapped function",
        )

    def build_function(
        self,
        name: str,
        function: Callable[..., Any],
        in_class: type[Any] | None,
        *,
        is_overload: bool = False,
    ) -> str:
        if name.startswith("_") and name not in _ALLOWED_FUNCTIONS:
            return ""

        if hasattr(function, "__wrapped__") and _strip_boolean_result_re.search(
            str(function)
        ):
            return self.__wrapped_strip_boolean_result(name, function, in_class)

        if isinstance(function, (GI.FunctionInfo, GI.VFuncInfo)):
            if in_class is None and function.get_namespace() != self.namespace:
                # Set up a constant for functions that are aliases
                return f"{name}: {self.get_final()} = {
                    self.get_namespace_member(
                        function.get_namespace(), f'{function.get_name()}'
                    )
                }\n"

            return self.__build_function(name, function, in_class)

        if in_class is None and (alias := self.get_alias(name, function)) is not None:
            # Set up a constant for functions that are aliases
            return f"{name}: {self.get_final()} = {alias}\n"

        signature_string: str
        missing_annotation = False

        if not is_overload and (overloads := get_overloads(function)):
            lines = [
                f"@{self.get_import('typing', 'overload')}\n{
                    self.build_function(name, overload, in_class, is_overload=True)
                }"
                for overload in overloads
            ]
            return "\n".join(lines)

        try:
            signature = inspect.signature(function)

            if name == "__init__" and signature.parameters:
                # Since we pass in __new__ with the name __init__, we need to replace
                # the `cls` parameter with `self` and set the return annotation to
                # `None`
                parameters = list(signature.parameters.values())
                parameters[0] = parameters[0].replace(
                    name="self", annotation=inspect.Parameter.empty
                )
                signature = signature.replace(
                    parameters=parameters, return_annotation=None
                )
            for param in signature.parameters.values():
                if param.name != "self" and param.annotation is inspect.Parameter.empty:
                    missing_annotation = True
            if signature.return_annotation is inspect.Signature.empty:
                missing_annotation = True

            signature_string = self.format_signature(signature)
        except Exception:
            missing_annotation = True
            if in_class:
                signature_string = "(self, *args, **kwargs)"
            else:
                signature_string = "(*args, **kwargs)"

        definition = ""
        if in_class:
            if hasattr(function, "name"):
                function_name: str = cast("Any", function).name
            else:
                function_name = function.__name__

            static_function = inspect.getattr_static(in_class, function_name, None)
            if (
                static_function
                and isinstance(static_function, staticmethod)
                and name != "__init__"
            ):
                definition += "@staticmethod\n"
        definition += f"def {name}{signature_string}:"
        docstring = (function.__doc__ or "").strip()
        if docstring:
            docstring = f'"""\n{docstring}\n"""'
            docstring = textwrap.indent(docstring, "    ")
            definition += f"\n{docstring}"
        else:
            definition += " ..."

        if missing_annotation:
            definition += "  # FIXME: Override is missing typing annotation"
        definition += "\n"

        return definition

    def build_contents_and_fields(
        self,
        parent: _Object,
        children: list[str],
        in_class: type[Any] | None,
        prefix_name: str,
    ) -> tuple[str, list[GI.FieldInfo]]:
        """
        Inspect the passed module recursively and build stubs for functions,
        classes, etc.
        """
        classes: dict[str, ClassInfo] = {}
        functions: dict[str, Callable[..., Any]] = {}
        constants: dict[str, Any] = {}
        flags: dict[str, type[Any]] = {}
        enums: dict[str, type[Any]] = {}

        ret = ""

        for name in children:
            if name.startswith("__") and name not in _ALLOWED_FUNCTIONS:
                continue

            # Check if this is a valid name in python
            if not _identifier_re.match(name):
                continue

            try:
                obj = getattr(parent, name)
            except AttributeError:
                continue

            if inspect.isclass(obj):
                if issubclass(obj, IntFlag):
                    flags[name] = obj
                elif issubclass(obj, IntEnum):
                    enums[name] = obj
                else:
                    classes[name] = ClassInfo(self, obj, name, prefix_name, in_class)
            elif (
                inspect.isfunction(obj)
                or inspect.isbuiltin(obj)
                or inspect.ismethoddescriptor(obj)
            ):
                functions[name] = obj
            elif inspect.ismethod(obj):
                # bound methods
                functions[name] = obj.__func__
            elif callable(obj):
                # Fall back to a function for anything callable
                functions[name] = obj
            else:
                # Assume everything else is some manner of constant
                constants[name] = obj

        # Filter out private constants
        constants = {k: v for k, v in constants.items() if not k.startswith("_")}

        # Those are type hints overrides can have for instance attributes
        annotations = {
            k: v
            for k, v in getattr(parent, "__annotations__", {}).items()
            if not k.startswith("_") and k not in constants
        }

        # Remove fields from constants to preserve output order
        fields: list[GI.FieldInfo] = []
        if in_class:
            obj_info = getattr(in_class, "__info__", None)
            if isinstance(obj_info, (GI.StructInfo, GI.ObjectInfo)):
                for f in obj_info.get_fields():
                    field_name = f.get_name()
                    if field_name in constants:
                        del constants[field_name]
                        fields.append(f)

        # annotations
        for name in sorted(annotations):
            ret += f"{name}: {self.format_annotation(annotations[name])}\n"

        # Constants
        for name in sorted(constants):
            if name[0].isdigit():
                # GDK has some busted constant names like
                # Gdk.EventType.2BUTTON_PRESS
                continue

            override = self.check_override(prefix_name, name)
            if override:
                ret += override + "\n"
                continue

            val = constants[name]

            if str(val.__class__).startswith(("<flag", "<enum")):
                val = val.real

            annotation = getattr(parent, "__annotations__", {}).get(name)
            if annotation:
                annotation_string = self.format_annotation(annotation)
            else:
                annotation_string = val.__class__.__name__

            if (isinstance(val, str) and len(val) <= 50) or isinstance(val, bool):
                ret += f"{name}: {self.get_final()} = {val!r}\n"
            elif (
                isinstance(val, (str, float, int))
                or annotation is not None
                or not in_class
            ):
                ret += f"{name}: {self.get_final(annotation_string)}\n"
            else:
                constant_annotation = "" if in_class else f": {self.get_final()}"
                ret += f"{name}{
                    constant_annotation
                } = ...  # FIXME: Constant is missing typing annotation\n"

        if ret and functions:
            ret += "\n"

        # Functions
        if (
            in_class and issubclass(in_class, (GI.Boxed, GI.Struct, GObject.Object))
        ) or (self.check_override(prefix_name, "__init__")):
            # __new__ and __init__ are handled during class construction as __init__
            functions.pop("__new__", None)
            functions.pop("__init__", None)

        for name, func in sorted(functions.items()):
            override = self.check_override(prefix_name, name)
            if override:
                ret += override + "\n"
                continue

            ret += self.build_function(name, func, in_class)

        if ret and classes:
            ret += "\n"

        # Classes
        for _, class_info in sorted(classes.items()):
            if class_string := class_info.build():
                ret += f"{class_string}\n"

        if ret and flags:
            ret += "\n"

        # Flags
        for name, obj in sorted(flags.items()):
            override = self.check_override(prefix_name, name)
            if override:
                ret += override + "\n\n"
                continue

            if in_class is None and (alias := self.get_alias(name, obj)) is not None:
                ret += f"{name} = {alias}\n"
                continue

            full_name = generate_full_name(prefix_name, name)
            flag_base = (
                self.get_namespace_member("GObject", "GFlags")
                if issubclass(obj, GObject.GFlags)
                else self.get_import("enum", "IntFlag")
            )

            ret += f"class {name}({flag_base}):\n"
            for key in sorted(vars(obj)):
                if key.startswith(("__", "_")) or key[0].isdigit():
                    continue

                override = self.check_override(full_name, key)
                if override:
                    for line in override.splitlines():
                        ret += "    " + line + "\n"
                    continue

                o = getattr(obj, key)
                if isinstance(o, GI.FunctionInfo):
                    function_ret = self.build_function(key, o, obj)
                    for line in function_ret.splitlines():
                        ret += "    " + line + "\n"
                elif hasattr(o, "real"):
                    value = o.real
                    ret += f"    {key} = {value}\n"
                else:
                    ret += f"    {key} = ... # FIXME Flags\n"
            ret += "\n"

        if ret and enums:
            ret += "\n"

        # Enums
        for name, obj in sorted(enums.items()):
            override = self.check_override(prefix_name, name)
            if override:
                ret += override + "\n\n"
                continue

            if in_class is None and (alias := self.get_alias(name, obj)) is not None:
                ret += f"{name} = {alias}\n"
                continue

            full_name = generate_full_name(prefix_name, name)
            enum_base = (
                self.get_namespace_member("GObject", "GEnum")
                if issubclass(obj, GObject.GEnum)
                else self.get_import("enum", "IntEnum")
            )

            # Some Enums can be empty in the end
            ret += f"class {name}({enum_base}):\n"
            length_before = len(ret)
            for key in sorted(vars(obj)):
                if key.startswith(("__", "_")) or key[0].isdigit():
                    continue

                override = self.check_override(full_name, key)
                if override:
                    for line in override.splitlines():
                        ret += "    " + line + "\n"
                    continue

                o = getattr(obj, key)
                if isinstance(o, GI.FunctionInfo):
                    function_ret = self.build_function(key, o, obj)
                    for line in function_ret.splitlines():
                        ret += "    " + line + "\n"
                elif hasattr(o, "real"):
                    value = o.real
                    ret += f"    {key} = {value}\n"
                else:
                    ret += f"    {key} = ... # FIXME Enum\n"

            if len(ret) == length_before:
                # No attributes were found
                ret += "    ...\n"

            ret += "\n"

        return ret, fields

    def build(self) -> str:
        ret = self.build_contents_and_fields(self.parent, dir(self.parent), None, "")[0]

        extras: list[str] = []

        if self.namespace == "GObject":
            # TODO: find a better way to keep things (like protocols) that aren't in the
            # actual module but are needed for the stubs
            object_protocol = self.check_override("", "ObjectProtocol")

            if object_protocol is not None:
                extras.append(object_protocol)

        # TODO: enable this when PyGObject exposes CallbackInfos
        # This must be called before generating the imports
        # callbacks = self.__build_callback_types()

        imports = [f"{_import}" for _import in self.needed_imports.values()]
        extras_str = "\n".join(extras)

        # Only keep the typevars that are actually used in the generated stubs
        used_typevars: list[str] = []
        for typevar in self.needed_typevars:
            typevar_re = re.compile(rf"\b{typevar.name}\b")

            if (
                typevar_re.search(extras_str) is not None
                or typevar_re.search(ret) is not None
            ):
                used_typevars.append(typevar.build(self))

        return (
            "\n".join(imports)
            + "\n"
            + "\n".join(used_typevars)
            + "\n\n"
            + extras_str
            # TODO: enable this when PyGObject exposes CallbackInfos
            # + "\n\n"
            # + callbacks
            + "\n\n"
            + ret
        )
