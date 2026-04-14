#!/usr/bin/env python3

# Based on https://github.com/PyCQA/astroid/blob/main/astroid/brain/brain_gi.py
# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE

from __future__ import annotations

from typing import Any
from typing import cast
from typing import Final
from typing import Generic
from typing import get_args
from typing import get_origin
from typing import Protocol
from typing import TYPE_CHECKING
from typing import TypeAlias
from typing_extensions import get_original_bases

import argparse
import importlib
import inspect
import itertools
import pprint
import re
import textwrap
from collections.abc import Callable
from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
from enum import IntEnum
from enum import IntFlag
from types import GenericAlias
from types import ModuleType

import gi
import gi._gi as GI
from parse import FromImport
from parse import Import
from parse import Imports
from parse import Overrides
from parse import parse

gi.require_version("GIRepository", "3.0")

if TYPE_CHECKING:
    from gi.repository import _GIRepository3 as GIRepository
else:
    from gi.repository import GIRepository

from gi.repository import GObject

ObjectT: TypeAlias = ModuleType | type[Any]

_identifier_re: Final = re.compile(r"^[A-Za-z_]\w*$")
_typing_re: Final = re.compile(r"(?:typing\.)(?P<name>\w+)\b")
_free_typing_re: Final = re.compile(r"\b(?P<name>Any|Self)\b")
_gi_repository_re: Final = re.compile(
    r"\bgi\.repository\.(?P<namespace>\w+)\.(?P<name>.*)\b"
)
_type_vars_re: Final = re.compile(r"[~+-](?P<name>\w+)\b")

# GLib 2.86 added a new flag which changed the naming of WRITABLE to IS_WRITABLE
_IS_FIELD_WRITABLE: Final[GIRepository.FieldInfoFlags] = getattr(
    GIRepository.FieldInfoFlags, "IS_WRITABLE", None
) or getattr(GIRepository.FieldInfoFlags, "WRITABLE")

RESERVED_KEYWORDS = {"async"}
ALLOWED_FUNCTIONS = {
    "__new__",
    "__init__",
    "__enter__",
    "__exit__",
    "__iter__",
    "__getitem__",
    "__setitem__",
    "__len__",
    "__int__",
    "__float__",
    "__bool__",
    "__contains__",
}

GI_IMPORT_ALIASES: Final = {
    "gi.Boxed": ("GObject", "GBoxed"),
    "gobject.GInterface": ("GObject", "GInterface"),
}


def fix_argument_name(name: str) -> str:
    if name in RESERVED_KEYWORDS:
        name = f"_{name}"
    return name.replace("-", "_")


def _object_get_props(
    repo: GIRepository.Repository,
    obj: GI.ObjectInfo,
) -> tuple[list[GIRepository.PropertyInfo], list[GIRepository.PropertyInfo]]:
    parents: list[GI.ObjectInfo] = []
    parent: GI.ObjectInfo | None = obj.get_parent()
    while parent:
        parents.append(parent)
        parent = parent.get_parent()

    interfaces = list(obj.get_interfaces())

    subclasses = parents + interfaces

    props = list(obj.get_properties())
    for s in subclasses:
        props.extend(s.get_properties())

    readable_props: list[GIRepository.PropertyInfo] = []
    writable_props: list[GIRepository.PropertyInfo] = []

    for prop in props:
        namespace = prop.get_namespace()
        container = prop.get_container()

        class_info = repo.find_by_name(namespace, container.get_name())
        if class_info is None:
            raise Exception(f"Unable to find {namespace}.{container}")

        if isinstance(class_info, GIRepository.ObjectInfo):
            for i in range(class_info.get_n_properties()):
                p = class_info.get_property(i)
                if p.get_name() == prop.get_name():
                    flags = p.get_flags()
                    if flags & GObject.ParamFlags.READABLE:
                        readable_props.append(p)
                    if flags & GObject.ParamFlags.WRITABLE:
                        writable_props.append(p)

        if isinstance(class_info, GIRepository.InterfaceInfo):
            for i in range(class_info.get_n_properties()):
                p = class_info.get_property(i)
                if p.get_name() == prop.get_name():
                    flags = p.get_flags()
                    if flags & GObject.ParamFlags.READABLE:
                        readable_props.append(p)
                    if flags & GObject.ParamFlags.WRITABLE:
                        writable_props.append(p)

    return (readable_props, writable_props)


def _callable_get_arguments(
    stub: Stub,
    type: GI.CallableInfo,
    can_default: bool = False,
) -> tuple[list[str], list[str], list[str]]:
    function_args = type.get_arguments()
    accept_optional_args = False
    optional_args_name = ""
    dict_names: dict[int, str] = {}
    dict_args: dict[int, GI.ArgInfo] = {}
    str_args: list[str] = []
    dict_return_args: dict[int, str] = {}
    skip: list[int] = []

    # Filter out array length arguments for return type
    ret_type = type.get_return_type()
    if ret_type.get_array_length_index() >= 0:
        skip.append(ret_type.get_array_length_index())

    for i, arg in enumerate(function_args):
        if i in skip:
            continue

        def skip_arg(index: int) -> None:
            if index < 0:
                return
            if index < i:
                dict_names.pop(index, None)
                dict_args.pop(index, None)
                dict_return_args.pop(index, None)
            elif index > i:
                skip.append(index)

        if arg.get_closure_index() >= 0:
            accept_optional_args = True
            optional_args_name = function_args[arg.get_closure_index()].get_name()
            skip_arg(arg.get_closure_index())
            skip_arg(arg.get_destroy_index())

        # Filter out array length args
        arg_type = arg.get_type_info()
        len_arg: int = arg_type.get_array_length_index()
        skip_arg(len_arg)

        # Need to check because user_data can be the first arg
        if arg.get_closure_index() != i and arg.get_destroy_index() != i:
            direction = arg.get_direction()
            if direction == GI.Direction.OUT or direction == GI.Direction.INOUT:
                t = _type_to_python(stub, arg.get_type_info(), True)

                dict_return_args[i] = t
            elif direction == GI.Direction.IN or direction == GI.Direction.INOUT:
                dict_names[i] = arg.get_name()
                dict_args[i] = arg

    # Traverse args in reverse to check for optional args
    args = list(dict_args.values())
    for a in reversed(args):
        t = _type_to_python(
            stub,
            a.get_type_info(),
            False,
            a.get_closure_index() >= 0,  # True if function admits variable arguments
        )

        if a.may_be_null() and t != "None":
            if can_default:
                str_args.append(f"{t} | None = None")
            else:
                str_args.append(f"{t} | None")
        else:
            can_default = False
            str_args.append(t)

    str_args = list(reversed(str_args))
    names = list(dict_names.values())

    # We need this info to filter out None as return arg for methods
    # that process Gio.AsyncResult. In python this method raises always.
    is_async_res = "Gio.AsyncResult" in str_args

    if accept_optional_args:
        names.append(f"*{optional_args_name}")
        str_args.append(stub.get_import("typing", "Any"))

    return_type = _type_to_python(stub, type.get_return_type(), True)
    if type.may_return_null() and return_type != "None" and not is_async_res:
        return_type = f"{return_type} | None"

    return_args = list(dict_return_args.values())
    if return_type != "None" or len(return_args) == 0:
        return_args.insert(0, return_type)

    return (names, str_args, return_args)


def _type_to_python(
    stub: Stub,
    type: GI.TypeInfo | GIRepository.TypeInfo,
    out_arg: bool = False,
    varargs: bool = False,
) -> str:
    tag = type.get_tag()
    tags = GI.TypeTag

    if tag == tags.ARRAY:
        array_type = type.get_param_type(0)

        if TYPE_CHECKING:
            assert array_type is not None

        t = _type_to_python(stub, array_type)
        if out_arg:
            # As output argument array of type uint8 are returned as bytes
            if array_type.get_tag() == GI.TypeTag.UINT8:
                return f"bytes"
            return f"list[{t}]"

        # As input arguments array can be generated by any sequence
        return f"{stub.get_import('collections.abc', 'Sequence')}[{t}]"

    if tag in (tags.GLIST, tags.GSLIST):
        array_type = type.get_param_type(0)

        if TYPE_CHECKING:
            assert array_type is not None

        t = _type_to_python(stub, array_type)
        return f"list[{t}]"

    if tag == tags.BOOLEAN:
        return "bool"

    if tag in (tags.DOUBLE, tags.FLOAT):
        return "float"

    if tag == tags.ERROR:
        return stub.get_namespace_member("GLib", "Error")

    if tag == tags.GHASH:
        key_type = type.get_param_type(0)
        value_type = type.get_param_type(1)

        if TYPE_CHECKING:
            assert key_type is not None
            assert value_type is not None

        kt = _type_to_python(stub, key_type)
        vt = _type_to_python(stub, value_type)
        return f"dict[{kt}, {vt}]"

    if tag in (tags.FILENAME, tags.UTF8, tags.UNICHAR):
        return "str"

    if tag == tags.GTYPE:
        return f"type[{stub.get_import('typing', 'Any')}]"

    if tag in (
        tags.INT8,
        tags.INT16,
        tags.INT32,
        tags.INT64,
        tags.UINT8,
        tags.UINT16,
        tags.UINT32,
        tags.UINT64,
    ):
        return "int"

    if tag == tags.INTERFACE:
        interface = type.get_interface()
        if isinstance(interface, GI.CallbackInfo):
            (names, args, return_args) = _callable_get_arguments(stub, interface)

            return_type = ""
            if len(return_args) == 1:
                return_type = return_args[0]
            else:
                return_type = f"tuple[{', '.join(return_args)}]"

            # FIXME, how to express Callable with variable arguments?
            if (len(names) > 0 and names[-1].startswith("*")) or varargs:
                return f"{stub.get_import('collections.abc', 'Callable')}[..., {return_type}]"
            else:
                return f"{stub.get_import('collections.abc', 'Callable')}[[{', '.join(args)}], {return_type}]"
        elif interface is not None:
            namespace = interface.get_namespace()
            name = interface.get_name()

            if name is not None and not _identifier_re.match(name):
                # Convert Flags and Enums with invalid name to int
                # Example NM 1.0 library
                if interface.get_type() in (
                    GIRepository.InfoType.FLAGS,
                    GIRepository.InfoType.ENUM,
                ):
                    return "int"

            if namespace == "GObject" and name == "Value":
                return stub.get_import("typing", "Any")

            if namespace == "GObject" and name == "Closure":
                return f"{stub.get_import('collections.abc', 'Callable')}[..., {stub.get_import('typing', 'Any')}]"

            if namespace == "cairo" and name == "Context" and not out_arg:
                return f"{stub.get_namespace_member('cairo', 'Context')}[_SomeSurface]"

            return stub.get_namespace_member(namespace, name)

    if tag == tags.VOID:
        return "None"

    raise ValueError("TODO")


def _generate_full_name(prefix: str, name: str) -> str:
    full_name = name
    if len(prefix) > 0:
        full_name = f"{prefix}.{name}"
    return full_name


def _build_function_info(
    stub: Stub,
    name: str,
    function: GI.FunctionInfo | GI.VFuncInfo,
    in_class: Any | None,
    return_signature: str | None = None,
    comment: str | None = None,
) -> str:
    constructor: bool = False
    method: bool = isinstance(function, GI.VFuncInfo)
    static: bool = False

    # Flags
    function_flags = function.get_flags()

    if function_flags & GIRepository.FunctionInfoFlags.IS_CONSTRUCTOR:
        constructor = True

    if function_flags & GIRepository.FunctionInfoFlags.IS_METHOD:
        method = True

    if in_class and not method and not constructor:
        static = True

    # Arguments
    (names, args, return_args) = _callable_get_arguments(stub, function, True)
    args_types = [
        f"{fix_argument_name(name)}: {args[i]}" for (i, name) in enumerate(names)
    ]

    # Return type
    if return_signature:
        return_type = return_signature
    elif len(return_args) > 1:
        return_type = f"tuple[{', '.join(return_args)}]"
    else:
        return_type = f"{return_args[0]}"

    # Generate string
    prepend = ""
    if constructor:
        if name == "__new__":
            prepend = "@staticmethod\n"
            self_symbol = stub.get_import("typing_extensions", "Self")
            args_types.insert(0, f"cls: type[{self_symbol}]")
            return_type = self_symbol
        else:
            prepend = "@classmethod\n"
            args_types.insert(0, "cls")
            # Override return value, for example Gtk.Button.new returns a Gtk.Widget instead of Gtk.Button
            rt = function.get_container().get_name()
            if return_type != f"{rt} | None":
                return_type = rt
    elif method:
        args_types.insert(0, "self")
    elif static:
        prepend = "@staticmethod\n"

    if comment:
        return f"{prepend}def {name}({', '.join(str(a) for a in args_types)}) -> {return_type}: ... # {comment}\n"
    else:
        return f"{prepend}def {name}({', '.join(str(a) for a in args_types)}) -> {return_type}: ...\n"


def _wrapped_strip_boolean_result(
    stub: Stub,
    name: str,
    function: Any,
    in_class: Any | None,
) -> str:
    real_function = function.__wrapped__
    fail_ret = inspect.getclosurevars(function).nonlocals.get("fail_ret")

    (_, _, return_args) = _callable_get_arguments(stub, real_function)
    return_args = return_args[1:]  # Strip first return value

    if len(return_args) > 1:
        return_signature = f"tuple[{', '.join(return_args)}]"
    else:
        return_signature = f"{return_args[0]}"

    if fail_ret is None:
        return_signature = f"{return_signature} | None"
    else:
        if type(fail_ret) is tuple:
            if len(fail_ret) > 0:
                return_signature = f"({return_signature} | tuple{str(fail_ret).replace('(', '[').replace(')', ']')})"
            else:
                return_signature = f"({return_signature} | tuple[()])"
        else:
            return_signature = f"({return_signature} | {stub.get_import('typing', 'Literal')}[{fail_ret}])"

    return _build_function_info(
        stub,
        name,
        real_function,
        in_class,
        return_signature,
        "CHECK Wrapped function",
    )


def _build_function(
    stub: Stub,
    name: str,
    function: Any,
    in_class: Any | None,
) -> str:
    if name.startswith("_") and name not in ALLOWED_FUNCTIONS:
        return ""

    if hasattr(function, "__wrapped__"):
        if "strip_boolean_result" in str(function):
            return _wrapped_strip_boolean_result(stub, name, function, in_class)

    if isinstance(function, GI.FunctionInfo) or isinstance(function, GI.VFuncInfo):
        if in_class is None and function.get_namespace() != stub.namespace:
            # Set up a constant for functions that are aliases
            return f"{name}: {stub.get_final()} = {stub.get_namespace_member(function.get_namespace(), function.get_name())}\n"

        return _build_function_info(stub, name, function, in_class)

    if in_class is None and (alias := stub.get_alias(name, function)) is not None:
        # Set up a constant for functions that are aliases
        return f"{name}: {stub.get_final()} = {alias}\n"

    signature_string: str
    missing_annotation = False
    try:
        # TODO: handle @overload with get_overloads()
        signature = inspect.signature(function)
        for param in signature.parameters.values():
            if param.name != "self" and param.annotation is inspect.Parameter.empty:
                missing_annotation = True
        if signature.return_annotation is inspect.Signature.empty:
            missing_annotation = True

        signature_string = stub.format_signature(signature)
    except:
        missing_annotation = True
        if in_class:
            signature_string = "(self, *args, **kwargs)"
        else:
            signature_string = "(*args, **kwargs)"

    definition = ""
    if in_class:
        if hasattr(function, "name"):
            function_name = function.name
        else:
            function_name = function.__name__

        static_function = inspect.getattr_static(in_class, function_name, None)
        if static_function and isinstance(static_function, staticmethod):
            definition += "@staticmethod\n"
    definition += f"def {name}{signature_string}:"
    docstring = (function.__doc__ or "").strip()
    if docstring:
        docstring = f'"""\n{docstring}\n"""'
        docstring = textwrap.indent(docstring, "    ")
        definition += f"\n{docstring}"
    else:
        definition += f" ..."

    if missing_annotation:
        definition += "  # FIXME: Override is missing typing annotation"
    definition += "\n"

    return definition


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
    parent: ObjectT
    namespace: str
    overrides: Overrides
    imports: InitVar[Imports]
    needed_imports: dict[tuple[str, str | None], FromImport | Import] = field(
        init=False
    )

    def __post_init__(self, imports: Imports) -> None:
        self.needed_imports = {
            (
                _import.module,
                (
                    _import.import_as or _import.name
                    if _import.module == "gi.repository"
                    else _import.name
                )
                if isinstance(_import, FromImport)
                else None,
            ): _import
            for _import in imports
        }

    def check_override(self, prefix: str, name: str) -> str | None:
        full_name = _generate_full_name(prefix, name)
        if full_name in self.overrides:
            return "# override\n" + self.__fix_annotations(self.overrides[full_name])
        return None

    def __get_import(
        self, module: str, /, name: str | None = None
    ) -> FromImport | Import | None:
        return self.needed_imports.get((module, name))

    def __add_import(
        self,
        module: str,
        /,
        name: str | None = None,
        import_as: str | None = None,
    ) -> Import | FromImport:
        import_object = (
            Import(module, import_as)
            if name is None
            else FromImport(module, name, import_as)
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
            return self.get_namespace_member("_gtktemplate", obj.__qualname__)
        else:
            return None

        if namespace != self.namespace or name != obj.__qualname__:
            return self.get_namespace_member(namespace, obj.__qualname__)

        return None

    def get_property(
        self, name: str, return_annotation: str, /, *, indent: str = ""
    ) -> str:
        property_symbol = self.get_import("builtins", "property")
        return f"{indent}@{property_symbol}\n{indent}def {name}(self) -> {return_annotation}: ...\n"

    def get_class_import(self, cls: Any, /) -> str:
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

        if alias := GI_IMPORT_ALIASES.get(full_name):
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

    def get_class_info(
        self, cls: type[Any], /
    ) -> tuple[tuple[type[Any], ...], GI.RegisteredTypeInfo | None]:
        full_name = f"{cls.__module__}.{cls.__qualname__}"
        object_info: GI.RegisteredTypeInfo | None = cls.__dict__.get("__info__")
        bases = list(get_original_bases(cls))

        # Because we're generating types for gi.repository, we have to generate stubs for
        # override classes that come from gi.repository and inherit from gi.repository classes.
        # Effectively, we want to write the stubs as if the override class and repository class
        # are one class in the MRO. What this means is that the following transformations need to
        # happen:
        # 1. For the following:
        #    gi.repository.X.One(<One repository bases>)
        #    gi.overrides.X.One(<One prefix override bases>, gi.repository.X.One, <One suffix override bases>) ->
        #        gi.repository.X.One(<One prefix override bases>, <One repository bases>, <One override bases>)
        # 2. gi.overrides.X.Two(float) -> gi.repository.X.Two(float)
        # 3. gi.overrides.X.Three(gi.overrides.X.Four, ...) -> gi.repository.X.Three(gi.repository.X.Four, ...)
        if full_name.startswith("gi.overrides.") and any(
            base.__module__.startswith("gi.repository.") for base in bases
        ):
            bases: list[Any] = []
            gi_repo_full_name = full_name.replace("gi.overrides.", "gi.repository.", 1)

            for base in get_original_bases(cls):
                if f"{base.__module__}.{base.__qualname__}" == gi_repo_full_name:
                    bases.extend(get_original_bases(base))

                    if object_info is None:
                        object_info = base.__dict__.get("__info__")
                elif base is not object:
                    bases.append(base)

        if GI.GInterface in bases and not any(
            get_origin(base) is Protocol for base in bases
        ):
            # Most overrides use Generic instead of Protocol for interfaces
            index = next(
                (
                    i
                    for i, base in enumerate(bases)
                    if get_origin(base) is Generic and get_args(base)
                ),
                None,
            )
            if index is None:
                bases.append(Protocol)
            else:
                args = get_args(bases[index])
                bases[index] = GenericAlias(cast(Any, Protocol), args)

        return tuple(bases), object_info

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
        return self.get_import("typing" if name == "Any" else "typing_extensions", name)

    def __replace_gi_repository(self, match: re.Match[str]) -> str:
        namespace = match.group("namespace")
        symbol = self.get_namespace_member(namespace, match.group("name"))
        return f"{symbol}"

    def __fix_annotations(self, formatted: str) -> str:
        formatted = _replace_optional(formatted)
        formatted = _replace_union(formatted)
        formatted = _typing_re.sub(self.__replace_typing, formatted)
        formatted = _free_typing_re.sub(self.__replace_free_typing, formatted)
        formatted = _gi_repository_re.sub(self.__replace_gi_repository, formatted)
        formatted = _type_vars_re.sub(r"\g<name>", formatted)
        return re.sub(rf"\b{self.namespace}\.", r"", formatted)

    def format_annotation(self, annotation: Any) -> str:
        try:
            # This requires Python 3.14
            formatted = inspect.formatannotation(
                annotation,
                quote_annotation_strings=False,  # pyright: ignore[reportCallIssue]
            )
        except:
            # This should be a good enough fallback for older Pythons
            formatted = (
                inspect.formatannotation(annotation).replace('"', "").replace("'", "")
            )

        return self.__fix_annotations(formatted)

    def format_signature(self, signature: inspect.Signature) -> str:
        try:
            # This requires Python 3.14
            formatted = signature.format(quote_annotation_strings=False)  # pyright: ignore[reportAttributeAccessIssue]
        except:
            # This should be a good enough fallback for older Pythons
            formatted = str(signature).replace('"', "").replace("'", "")

        return self.__fix_annotations(formatted)

    def build(self) -> str:
        ret = _gi_build_stub_parts(self, self.parent, dir(self.parent), None, "")[0]

        _TypeVar = self.get_import("typing", "TypeVar")

        typevars: list[str] = [
            f'T = {_TypeVar}("T")',
        ]

        if self.namespace == "GObject":
            # TODO: find a better way to keep things (like protocols) that aren't in the actual module
            # but are needed for the stubs
            object_protocol = self.check_override("", "ObjectProtocol")

            if object_protocol is not None:
                typevars.append(object_protocol)
        elif self.namespace == "Gtk":
            self.get_import("os")
            typevars.append(
                f"""CellRendererT = {_TypeVar}(
    "CellRendererT",
    CellRendererCombo,
    CellRendererPixbuf,
    CellRendererProgress,
    CellRendererSpin,
    CellRendererSpinner,
    CellRendererText,
    CellRendererToggle,
)
WidgetT = {_TypeVar}("WidgetT", bound=Widget)"""
            )
        elif self.namespace == "Gio":
            any_symbol = self.get_import("typing", "Any")
            typevars.extend(
                [
                    f'ObjectItemType = {_TypeVar}("ObjectItemType", bound=GObject.Object, default={any_symbol})',
                    f'ObjectPropsItemType = {_TypeVar}("ObjectPropsItemType", bound=GObject.Object, default={any_symbol})',
                ]
            )

        if ("cairo", None) in self.needed_imports:
            typevars.append(
                f'_SomeSurface = {_TypeVar}("_SomeSurface", bound=cairo.Surface)'
            )

        imports = [f"{_import}" for _import in self.needed_imports.values()]

        return "\n".join(imports) + "\n" + "\n".join(typevars) + "\n\n" + ret


def _gi_build_stub_parts(
    stub: Stub,
    parent: ObjectT,
    children: list[str],
    in_class: Any | None,
    prefix_name: str,
) -> tuple[str, list[GI.FieldInfo]]:
    """
    Inspect the passed module recursively and build stubs for functions,
    classes, etc.
    """
    classes: dict[str, type[Any]] = {}
    functions: dict[str, Callable[..., Any]] = {}
    constants: dict[str, Any] = {}
    flags: dict[str, type[Any]] = {}
    enums: dict[str, type[Any]] = {}

    ret = ""

    for name in children:
        if name.startswith("__") and name not in ALLOWED_FUNCTIONS:
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
                classes[name] = obj
        elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
            functions[name] = obj
        elif inspect.ismethoddescriptor(obj):
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
        ret += f"{name}: {stub.format_annotation(annotations[name])}\n"

    # Constants
    for name in sorted(constants):
        if name[0].isdigit():
            # GDK has some busted constant names like
            # Gdk.EventType.2BUTTON_PRESS
            continue

        override = stub.check_override(prefix_name, name)
        if override:
            ret += override + "\n"
            continue

        val = constants[name]

        if str(val.__class__).startswith(("<flag", "<enum")):
            val = val.real

        annotation = getattr(parent, "__annotations__", {}).get(name)
        if annotation:
            annotation_string = stub.format_annotation(annotation)
        else:
            annotation_string = val.__class__.__name__

        if (isinstance(val, str) and len(val) <= 50) or isinstance(val, bool):
            ret += f"{name}: {stub.get_final()} = {val!r}\n"
        elif (
            isinstance(val, (str, float, int)) or annotation is not None or not in_class
        ):
            ret += f"{name}: {stub.get_final(annotation_string)}\n"
        else:
            constant_annotation = "" if in_class else f": {stub.get_final()}"
            ret += f"{name}{constant_annotation} = ...  # FIXME: Constant is missing typing annotation\n"

    if ret and functions:
        ret += "\n"

    # Functions
    if (
        "__new__" in functions
        or (in_class and issubclass(in_class, GObject.GObject))
        or stub.check_override(prefix_name, "__init__")
    ):
        functions.pop("__init__", None)

    for name, func in sorted(functions.items()):
        override = stub.check_override(prefix_name, name)
        if override:
            ret += override + "\n"
            continue

        ret += _build_function(stub, name, func, in_class)

    if ret and classes:
        ret += "\n"

    # Classes
    for name, obj in sorted(classes.items()):
        override = stub.check_override(prefix_name, name)
        if override:
            ret += override + "\n\n"
            continue

        if in_class is None and (alias := stub.get_alias(name, obj)) is not None:
            # Set up a constant for classes that are aliases
            # NOTE: this should not use `Final` because doing so turns the alias into
            # a variable rather than a class
            ret += f"{name} = {alias}\n"
            continue

        full_name = _generate_full_name(prefix_name, name)

        classret, fields = _gi_build_stub_parts(
            stub,
            obj,
            _find_attributes(obj),
            obj,
            full_name,
        )

        readable_props: list[GIRepository.PropertyInfo] = []
        writable_props: list[GIRepository.PropertyInfo] = []
        props_parents: list[str] = []
        class_bases, class_object_info = stub.get_class_info(obj)

        if class_object_info is not None:
            if isinstance(class_object_info, GI.ObjectInfo):
                p = class_object_info.get_parent()
                if p:
                    props_parents.append(
                        f"{stub.get_namespace_member(p.get_namespace(), p.get_name())}.Props"
                    )

                # Properties
                (rp, wp) = _object_get_props(stub.repo, class_object_info)
                readable_props.extend(rp)
                writable_props.extend(wp)

        string_parents = ""
        if class_bases:
            bases_strings = [
                stub.get_class_import(base)
                for base in class_bases
                if base is not object
            ]

            string_parents = f"({', '.join(bases_strings)})"

        if (
            not classret
            and len(fields) == 0
            and len(readable_props) == 0
            and len(writable_props) == 0
        ):
            ret += f"class {name}{string_parents}: ...\n"
        else:
            ret += f"class {name}{string_parents}:\n"

            # extracting docs
            doc = getattr(obj, "__doc__", "") or ""
            gdoc = getattr(obj, "__gdoc__", "") or ""

            txt = doc.strip() + "\n\n" + gdoc.strip()
            if not txt.isspace():
                txt = '"""\n' + txt.strip() + '\n"""' + "\n"
                txt = textwrap.indent(txt, "    ")
                ret += txt

        props_class_override = stub.check_override(full_name, "Props")
        if props_class_override:
            for line in props_class_override.splitlines():
                ret += "    " + line + "\n"
        elif readable_props or writable_props:
            names: list[str] = []
            s: list[str] = []
            for p in itertools.chain(readable_props, writable_props):
                n = fix_argument_name(p.get_name())
                if n in names:
                    # Avoid duplicates
                    continue
                names.append(n)
                t = _type_to_python(stub, p.get_type_info(), True)

                # Check getter/setter
                getter = p.get_getter()
                setter = p.get_setter()
                if getter and getter.may_return_null():
                    s.append(f"{n}: {t} | None")
                elif setter and not getter:
                    # If is writable only prop check if setter can accept NULL
                    arg_info = setter.get_arg(0)
                    if arg_info.may_be_null():
                        s.append(f"{n}: {t} | None")
                    else:
                        s.append(f"{n}: {t}")
                else:
                    s.append(f"{n}: {t}")

            props_string_parents = (
                f"({', '.join(props_parents)})" if props_parents else ""
            )

            separator = "\n        "
            ret += f"    class Props{props_string_parents}:{separator}"
            ret += separator.join(s)
            ret += "\n"

        props_override = stub.check_override(full_name, "props")
        if props_override:
            for line in props_override.splitlines():
                ret += "    " + line + "\n"
        elif props_class_override or readable_props or writable_props:
            ret += stub.get_property("props", "Props", indent="    ")

        for f in fields:
            t = _type_to_python(stub, f.get_type_info(), True)
            n = f.get_name()
            override = stub.check_override(full_name, n)
            if override:
                ret += f"    {override}\n"
            else:
                field_flags = f.get_flags()
                if not (field_flags & _IS_FIELD_WRITABLE):
                    ret += stub.get_property(n, t, indent="    ")
                else:
                    ret += f"    {n}: {t}\n"

        class_constructor_override = stub.check_override(full_name, "__init__")
        if class_constructor_override:
            for line in class_constructor_override.splitlines():
                ret += "    " + line + "\n"
        elif len(writable_props) > 0:
            names: list[str] = []
            s: list[str] = []
            for p in writable_props:
                n = fix_argument_name(p.get_name())
                if n in names:
                    # Avoid duplicates
                    continue
                names.append(n)
                t = _type_to_python(stub, p.get_type_info())
                setter = p.get_setter()
                if setter:
                    arg_info = setter.get_arg(0)
                    if arg_info.may_be_null():
                        s.append(f"{n}: {t} | None = ...")
                    else:
                        s.append(f"{n}: {t} = ...")
                else:
                    s.append(f"{n}: {t} = ...")

            separator = ",\n                 "
            ret += f"    def __init__(self, *, {separator.join(s)}) -> None: ...\n"

        for line in classret.splitlines():
            ret += "    " + line + "\n"

        ret += "\n"

    if ret and flags:
        ret += "\n"

    # Flags
    for name, obj in sorted(flags.items()):
        override = stub.check_override(prefix_name, name)
        if override:
            ret += override + "\n\n"
            continue

        if in_class is None and (alias := stub.get_alias(name, obj)) is not None:
            ret += f"{name} = {alias}\n"
            continue

        full_name = _generate_full_name(prefix_name, name)
        flag_base = (
            stub.get_namespace_member("GObject", "GFlags")
            if issubclass(obj, GObject.GFlags)
            else stub.get_import("enum", "IntFlag")
        )

        ret += f"class {name}({flag_base}):\n"
        for key in sorted(vars(obj)):
            if key.startswith(("__", "_")) or key[0].isdigit():
                continue

            override = stub.check_override(full_name, key)
            if override:
                for line in override.splitlines():
                    ret += "    " + line + "\n"
                continue

            o = getattr(obj, key)
            if isinstance(o, GI.FunctionInfo):
                function_ret = _build_function(stub, key, o, obj)
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
        override = stub.check_override(prefix_name, name)
        if override:
            ret += override + "\n\n"
            continue

        if in_class is None and (alias := stub.get_alias(name, obj)) is not None:
            ret += f"{name} = {alias}\n"
            continue

        full_name = _generate_full_name(prefix_name, name)
        enum_base = (
            stub.get_namespace_member("GObject", "GEnum")
            if issubclass(obj, GObject.GEnum)
            else stub.get_import("enum", "IntEnum")
        )

        # Some Enums can be empty in the end
        ret += f"class {name}({enum_base}):\n"
        length_before = len(ret)
        for key in sorted(vars(obj)):
            if key.startswith(("__", "_")) or key[0].isdigit():
                continue

            override = stub.check_override(full_name, key)
            if override:
                for line in override.splitlines():
                    ret += "    " + line + "\n"
                continue

            o = getattr(obj, key)
            if isinstance(o, GI.FunctionInfo):
                function_ret = _build_function(stub, key, o, obj)
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


def _find_attributes(obj: type[Any]) -> list[str]:
    # Get all attributes resolved in this class, excluding inherited ones.
    # This includes overridden attributes that could have a different signature
    # in parent classes.
    obj_attrs = set(obj.__dict__.keys())

    # Add inherited GI attributes if we are a direct override of a GI class.
    if "__info__" not in obj.__dict__:
        for base in obj.__bases__:
            if "__info__" in base.__dict__:
                obj_attrs.update(base.__dict__.keys())

    return sorted(list(obj_attrs))


def start(
    module: str, version: str, init: str | None, overrides: Overrides, imports: Imports
) -> str:
    repo = GIRepository.Repository()
    repo.require(module, version, 0)  # type: ignore

    gi.require_version(module, version)
    m = importlib.import_module(f".{module}", "gi.repository")

    if init:
        exec(init)
    stub = Stub(repo, m, module, overrides, imports)
    return stub.build()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate module stubs")
    parser.add_argument("module", type=str, help="Gdk, Gtk, ...")
    parser.add_argument("version", type=str, help="3.0, 4.0, ...")
    parser.add_argument(
        "-u", dest="update", type=str, help="Stub file to update e.g. -u Gdk.pyi"
    )
    parser.add_argument(
        "--init",
        type=str,
        help='Initialization code that must be evaluated first e.g. \'gi.require_version("Gst", "1.0"); from gi.repository import Gst; Gst.init(None)\'',
    )

    args = parser.parse_args()

    if args.update:
        overrides: Overrides = {}
        imports: Imports = []
        try:
            with open(args.update) as file:
                overrides, imports = parse(file.read())
        except FileNotFoundError:
            pass
        output = start(args.module, args.version, args.init, overrides, imports)
        print("Running with these overrides:")
        pprint.pprint(overrides)
        with open(args.update, "w+") as file:
            file.write(output)
    else:
        print(start(args.module, args.version, args.init, {}, []))


if __name__ == "__main__":
    main()
