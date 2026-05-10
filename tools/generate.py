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
from typing_extensions import get_overloads
from typing_extensions import Self

import argparse
import importlib
import inspect
import itertools
import pprint
import re
import subprocess
import sys
import textwrap
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Iterator
from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
from dataclasses import replace
from enum import IntEnum
from enum import IntFlag
from pathlib import Path
from types import GenericAlias
from types import ModuleType

import gi
import gi._gi as GI
from parse import FromImport
from parse import Import
from parse import Imports
from parse import Overrides
from parse import parse
from parse import TypeVarInfo
from parse import TypeVars
from parse import TypeVarTupleInfo

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
    r"\bgi\.(?:repository|overrides)\.(?P<namespace>\w+)\.(?P<name>(?:\w+)(?:\.\w+)*)\b"
)
_import_re: Final = re.compile(
    r"\b(?P<module>(?:[A-Za-z_]\w+\.)*[A-Za-z_]\w+)\.(?P<name>[A-Za-z_]\w+)\b"
)
_type_vars_re: Final = re.compile(r"(?<!\w)[~+-](?P<name>[A-Za-z_]\w*)\b")
_strip_boolean_result_re: Final = re.compile(r"\bstrip_boolean_result\b")

RESERVED_KEYWORDS = {"async"}
ALLOWED_FUNCTIONS = {
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

GI_IMPORT_ALIASES: Final = {
    "gi.Boxed": ("GObject", "GBoxed"),
    "gobject.GInterface": ("GObject", "GInterface"),
}

EXCLUDED_VARARGS_CALLBACKS: Final = {
    ("GLib", "DestroyNotify"),
}

MODULE_NORMALIZATION: Final[dict[tuple[str, str | None], str]] = {
    ("typing", "Self"): "typing_extensions",  # 3.11+
    ("typing", "TypeVar"): "typing_extensions",  # default= 3.13+, infer_variance= 3.12+
    ("typing", "Unpack"): "typing_extensions",  # 3.11+
    ("typing", "TypeVarTuple"): "typing_extensions",  # 3.11+
}


def _normalize_module_name(module: str, name: str | None, /) -> str:
    return MODULE_NORMALIZATION.get((module, name), module)


def _fix_argument_name(name: str | None, /) -> str:
    if name is None:
        raise ValueError("Argument name cannot be None")

    if name in RESERVED_KEYWORDS:
        name = f"_{name}"
    return name.replace("-", "_")


def _get_return_type(return_args: list[str], /) -> str:
    return (
        "None"
        if not return_args
        else return_args[0]
        if len(return_args) == 1
        else f"tuple[{', '.join(return_args)}]"
    )


def _make_nullable(py_type: str) -> str:
    if not py_type.endswith(" | None") and py_type != "None":
        return f"{py_type} | None"

    return py_type


_FROM_PYTHON: Final = frozenset({GI.Direction.IN, GI.Direction.INOUT})
_TO_PYTHON: Final = frozenset({GI.Direction.OUT, GI.Direction.INOUT})


@dataclass(slots=True, frozen=True)
class _VisibleArgument:
    info: GI.ArgInfo
    c_index: int
    direction: GI.Direction
    required: bool
    nullable: bool
    is_closure_target: bool
    is_varargs_slot: bool
    is_varargs_callback: bool


@dataclass(slots=True, frozen=True)
class _CallableArguments:
    args: tuple[GI.ArgInfo, ...]
    can_have_defaults: bool
    hidden: frozenset[int]
    closure_targets: frozenset[int]
    varargs_index: int | None

    @property
    def varargs_info(self) -> GI.ArgInfo | None:
        return self.args[self.varargs_index] if self.varargs_index is not None else None

    def __iter__(self) -> Iterator[_VisibleArgument]:
        for index, gi_arg in enumerate(self.args):
            if index in self.hidden:
                continue

            direction = gi_arg.get_direction()
            nullable = gi_arg.may_be_null()
            closure_index = gi_arg.get_closure_index()

            yield _VisibleArgument(
                info=gi_arg,
                c_index=index,
                direction=direction,
                # An arg is "required" (no `= ...` default) iff PyGObject's
                # runtime would reject omitting it. The runtime accepts
                # omission iff pygi_arg_cache_allow_none() is true, which
                # boils down to may_be_null OR is_optional.
                required=not (nullable or gi_arg.is_optional()),
                nullable=nullable,
                is_closure_target=index in self.closure_targets,
                is_varargs_slot=index == self.varargs_index,
                is_varargs_callback=closure_index == self.varargs_index,
            )

    @classmethod
    def for_callable(
        cls, info: GI.CallableInfo, /, *, allow_varargs: bool = True
    ) -> Self:
        gi_args = info.get_arguments()

        hidden_indexes: set[int] = set()
        closure_indexes: set[int] = set()
        from_python_indexes: set[int] = set()

        if (
            return_array_length_index := info.get_return_type().get_array_length_index()
        ) > -1:
            hidden_indexes.add(return_array_length_index)

        is_callback = isinstance(info, GI.CallbackInfo)

        if is_callback:
            # Callback arguments that are used for closure have a closure index
            # that matches their argument index, so we can just check for that
            # instead of checking the type and direction
            for arg_index, arg in enumerate(gi_args):
                if arg.get_closure_index() == arg_index:
                    closure_indexes.add(arg_index)

                from_python_indexes.add(arg_index)

            # Apply PyGObject's user_data heuristic when no explicit closure
            # annotation is present. This mirrors the auto-detection in
            # pygi_closure_cache_new (pygi-cache.c lines 1092-1111), which
            # picks the first IN-direction void-pointer arg and treats it
            # as the user_data slot for the callback.
            if not closure_indexes:
                for arg_index, arg in enumerate(gi_args):
                    if arg.get_direction() != GI.Direction.IN:
                        continue
                    type_info = arg.get_type_info()
                    if (
                        type_info.get_tag() == GI.TypeTag.VOID
                        and type_info.is_pointer()
                    ):
                        closure_indexes.add(arg_index)
                        break
        else:
            for arg_index, arg in enumerate(gi_args):
                type_info = arg.get_type_info()
                tag = type_info.get_tag()
                is_from_python = arg.get_direction() in _FROM_PYTHON

                # Hide array length args
                if (
                    tag == GI.TypeTag.ARRAY
                    and (array_length_index := type_info.get_array_length_index()) > -1
                ):
                    hidden_indexes.add(array_length_index)

                # Hide destroy and closure args for callbacks
                if (
                    tag == GI.TypeTag.INTERFACE
                    and isinstance(type_info.get_interface(), GI.CallbackInfo)
                    and arg_index not in hidden_indexes
                    and arg_index not in closure_indexes
                ):
                    if (
                        closure_index := arg.get_closure_index()
                    ) > -1 and is_from_python:
                        closure_indexes.add(closure_index)

                    if (destroy_index := arg.get_destroy_index()) > -1:
                        hidden_indexes.add(destroy_index)

                if is_from_python:
                    from_python_indexes.add(arg_index)

        # Find the last closure argument whether it comes before or after the callback.
        last_visible_from_python = max(from_python_indexes - hidden_indexes, default=-1)

        # Treat a user_data slot as the *varargs argument iff it is the
        # trailing FROM_PYTHON arg in C-arg order (i.e. no other visible
        # FROM_PYTHON arg has a higher C-arg index). This mirrors
        # PyGObject's runtime varargs detection in the reverse loop of
        # _callable_cache_generate_args_cache_real, which picks the last
        # FROM_PYTHON arg and only treats it as varargs when it is a
        # CHILD_WITH_PYARG (i.e. a user_data slot).
        varargs_index = (
            last_visible_from_python
            if allow_varargs and last_visible_from_python in closure_indexes
            else None
        )

        return cls(
            args=gi_args,
            can_have_defaults=isinstance(info, GI.FunctionInfo),
            hidden=frozenset(hidden_indexes),
            closure_targets=frozenset(closure_indexes),
            varargs_index=varargs_index,
        )


def _get_callable_arguments(
    stub: Stub, info: GI.CallableInfo, /, *, allow_varargs: bool = True
) -> tuple[dict[str, str], list[str]]:
    arguments = _CallableArguments.for_callable(info, allow_varargs=allow_varargs)

    py_args: list[_VisibleArgument] = []
    return_args: list[str] = []
    required_indexes: set[int] = set()

    for arg in arguments:
        if arg.direction in _FROM_PYTHON and not arg.is_varargs_slot:
            py_args.append(arg)

            if arg.required:
                required_indexes.add(arg.c_index)

        if arg.direction in _TO_PYTHON:
            return_args.append(
                _type_info_to_python(
                    stub, arg.info.get_type_info(), out=True, nullable=arg.nullable
                )
            )

    last_required = max(required_indexes, default=-1)
    args: dict[str, str] = {}

    for py_arg in py_args:
        arg_type = _type_info_to_python(
            stub,
            py_arg.info.get_type_info(),
            nullable=py_arg.nullable,
            varargs_callback=py_arg.is_varargs_callback,
            closure_argument=py_arg.is_closure_target,
        )

        if arguments.can_have_defaults and py_arg.c_index > last_required:
            arg_type = f"{arg_type} = {'None' if py_arg.nullable else '...'}"

        args[_fix_argument_name(py_arg.info.get_name())] = arg_type

    if (varargs_info := arguments.varargs_info) is not None:
        args[f"*{_fix_argument_name(varargs_info.get_name())}"] = (
            f"{stub.get_import('typing', 'Unpack')}[{stub.get_callback_typevar_tuple()}]"
        )

    return_type = info.get_return_type()
    if not info.skip_return() and (
        return_type.get_tag() != GI.TypeTag.VOID or return_type.is_pointer()
    ):
        return_args = [
            _type_info_to_python(
                stub, return_type, out=True, nullable=info.may_return_null()
            ),
            *return_args,
        ]

    return args, return_args


def _type_info_to_python(
    stub: Stub,
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

            value_type = _type_info_to_python(stub, value_info, out=out)

            if tag == GI.TypeTag.ARRAY:
                if out:
                    # As output argument array of type uint8 are returned as bytes
                    if value_info.get_tag() == GI.TypeTag.UINT8:
                        py_type = f"bytes"
                    else:
                        py_type = f"list[{value_type}]"
                else:
                    # As input arguments array can be generated by any sequence
                    py_type = f"{stub.get_import('collections.abc', 'Sequence')}[{value_type}]"
            else:
                py_type = f"list[{value_type}]"

            # All return/out/inout arrays/lists get marshalled as a list, regardless of nullable
            nullable = nullable and not out
        case GI.TypeTag.GHASH:
            key_info = info.get_param_type(0)
            value_info = info.get_param_type(1)

            if TYPE_CHECKING:
                assert key_info is not None
                assert value_info is not None

            key_type = _type_info_to_python(stub, key_info, out=out)
            value_type = _type_info_to_python(stub, value_info, out=out)
            collection_type = (
                "dict" if out else stub.get_import("collections.abc", "Mapping")
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
                #     py_type = stub.get_namespace_member(
                #         interface_info.get_namespace(), callback_name
                #     )

                #     if (
                #         varargs_callback
                #         and (interface_info.get_namespace(), interface_info.get_name())
                #         not in EXCLUDED_VARARGS_CALLBACKS
                #     ):
                #         py_type = f"{py_type}[{stub.get_import('typing', 'Unpack')}[{stub.get_callback_typevar_tuple()}]]"
                # else:
                #    # Generate the `Callable[]` annotation for anonymous callbacks
                #    (callback_args, callback_return_args) = _get_callable_arguments(
                #        stub, interface_info, allow_varargs=varargs_callback
                #    )
                #    callback_return_type = _get_return_type(callback_return_args)

                #    py_type = f"{stub.get_import('collections.abc', 'Callable')}[[{', '.join(callback_args.values())}], {callback_return_type}]"
                (callback_args, callback_return_args) = _get_callable_arguments(
                    stub, interface_info, allow_varargs=varargs_callback
                )
                callback_return_type = _get_return_type(callback_return_args)

                py_type = f"{stub.get_import('collections.abc', 'Callable')}[[{', '.join(callback_args.values())}], {callback_return_type}]"
            elif interface_info is not None:
                interface_namespace = interface_info.get_namespace()
                interface_name = interface_info.get_name()

                if interface_namespace == "GObject" and interface_name == "Value":
                    py_type = stub.get_import("typing", "Any")

                elif interface_namespace == "GObject" and interface_name == "Closure":
                    py_type = f"{stub.get_import('collections.abc', 'Callable')}[..., {stub.get_import('typing', 'Any')}]"

                elif (
                    interface_namespace == "cairo"
                    and interface_name == "Context"
                    and not out
                ):
                    some_surface = stub.get_typevar(
                        "_SomeSurface",
                        bound=f"{stub.get_namespace_member('cairo', 'Surface')}",
                    )
                    py_type = f"{stub.get_namespace_member('cairo', 'Context')}[{some_surface}]"
                else:
                    py_type = stub.get_namespace_member(
                        interface_namespace, f"{interface_name}"
                    )
        case GI.TypeTag.VOID:
            if info.is_pointer():
                if closure_argument:
                    # Arguments passed to callbacks are specially handled by the PyGObject marshalling code,
                    # so they can be anything
                    py_type = f"{stub.get_import('typing', 'Any')} | None"
                else:
                    # Pointers can be int | CapsuleType | None, but we don't have CapsuleType until 3.13
                    # This is what typeshed did until 3.13
                    py_type = (
                        "int"
                        if out
                        else f"int | {stub.get_import('typing', 'Any')} | None"
                    )

                # All return/out/inout pointers get marshalled as int, regardless of nullable
                nullable = nullable and not out
            else:
                py_type = "None"
        case GI.TypeTag.GTYPE:
            py_type = f"type[{stub.get_import('typing', 'Any')}]"
        case GI.TypeTag.ERROR:
            py_type = stub.get_namespace_member("GLib", "Error")

    if py_type is None:
        raise ValueError(f"Unsupported GI type tag: {tag}")

    if nullable:
        py_type = _make_nullable(py_type)

    return py_type


def _generate_full_name(prefix: str, name: str) -> str:
    return f"{prefix}.{name}" if prefix else name


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

    if function_flags & GI.FunctionInfoFlags.IS_CONSTRUCTOR:
        constructor = True

    if function_flags & GI.FunctionInfoFlags.IS_METHOD:
        method = True

    if in_class and not method and not constructor:
        static = True

    # Arguments
    args, return_args = _get_callable_arguments(stub, function)
    args_types = [f"{_fix_argument_name(name)}: {arg}" for name, arg in args.items()]

    return_type = (
        return_signature if return_signature else _get_return_type(return_args)
    )

    # Generate string
    prepend = ""
    if constructor:
        if name == "__init__":
            # We pass the "new" constructor with the name __init__ because type checkers
            # do better with __init__ signatures, so we have to change the signature a bit
            args_types.insert(0, "self")
            return_type = "None"
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

    _, return_args = _get_callable_arguments(stub, real_function)
    return_args = return_args[1:]  # Strip first return value

    return_signature = _get_return_type(return_args)

    if fail_ret is None:
        return_signature = _make_nullable(f"{return_signature}")
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
    *,
    is_overload: bool = False,
) -> str:
    if name.startswith("_") and name not in ALLOWED_FUNCTIONS:
        return ""

    if hasattr(function, "__wrapped__") and _strip_boolean_result_re.search(
        str(function)
    ):
        return _wrapped_strip_boolean_result(stub, name, function, in_class)

    if isinstance(function, GI.FunctionInfo) or isinstance(function, GI.VFuncInfo):
        if in_class is None and function.get_namespace() != stub.namespace:
            # Set up a constant for functions that are aliases
            return f"{name}: {stub.get_final()} = {stub.get_namespace_member(function.get_namespace(), f'{function.get_name()}')}\n"

        return _build_function_info(stub, name, function, in_class)

    if in_class is None and (alias := stub.get_alias(name, function)) is not None:
        # Set up a constant for functions that are aliases
        return f"{name}: {stub.get_final()} = {alias}\n"

    signature_string: str
    missing_annotation = False

    if not is_overload and (overloads := get_overloads(function)):
        lines = [
            f"@{stub.get_import('typing', 'overload')}\n{_build_function(stub, name, overload, in_class, is_overload=True)}"
            for overload in overloads
        ]
        return "\n".join(lines)

    try:
        signature = inspect.signature(function)

        if name == "__init__" and signature.parameters:
            # Since we pass in __new__ with the name __init__, we need to replace the
            # `cls` parameter with `self` and set the return annotation to `None`
            parameters = list(signature.parameters.values())
            parameters[0] = parameters[0].replace(
                name="self", annotation=inspect.Parameter.empty
            )
            signature = signature.replace(parameters=parameters, return_annotation=None)
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
class PropertyInfo:
    stub: Stub
    gi_info: GI.PropertyInfo

    # Needed for get_getter() and get_setter() because GI.PropertyInfo doesn't have them
    gir_info: GIRepository.PropertyInfo

    gobject_name: str = field(init=False)
    name: str = field(init=False)

    _init_type: str | None = field(init=False, default=None)
    _prop_type: str | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.gobject_name = f"{self.gi_info.get_name()}"
        self.name = _fix_argument_name(self.gobject_name)

    @property
    def readable(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.READABLE)

    @property
    def writable(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.WRITABLE)

    @property
    def construct(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.CONSTRUCT)

    @property
    def construct_only(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.CONSTRUCT_ONLY)

    @property
    def prop_type(self) -> str:
        if self._prop_type is not None:
            return self._prop_type

        py_type = _type_info_to_python(
            self.stub, self.gi_info.get_type_info(), out=True
        )
        getter = self.gir_info.get_getter()
        setter = self.gir_info.get_setter()

        if (getter and getter.may_return_null()) or (
            # If it is wratable only prop, check if setter can accept NULL
            setter and setter.get_arg(0).may_be_null()
        ):
            py_type = _make_nullable(py_type)

        self._prop_type = py_type

        return py_type

    @property
    def init_type(self) -> str:
        if self._init_type is not None:
            return self._init_type

        setter = self.gir_info.get_setter()
        py_type = _type_info_to_python(
            self.stub,
            self.gi_info.get_type_info(),
            nullable=bool(setter and setter.get_arg(0).may_be_null()),
        )

        self._init_type = py_type

        return py_type


PropertyInfoDict: TypeAlias = dict[str, PropertyInfo]
_MISSING = object()


@dataclass(slots=True)
class ClassInfo:
    stub: Stub
    cls: type[Any]
    name: str
    prefix: str
    in_class: Any | None
    full_name: str = field(init=False)

    _bases: tuple[type[Any], ...] | None = field(init=False, default=None)
    _gi_info: GI.RegisteredTypeInfo | None = field(
        init=False, default=cast(Any, _MISSING)
    )
    _class_properties: PropertyInfoDict | None = field(init=False, default=None)
    _init_properties: PropertyInfoDict | None = field(init=False, default=None)
    _class_content: str | None = field(init=False, default=None)
    _fields: list[GI.FieldInfo] | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.full_name = _generate_full_name(self.prefix, self.name)

    @property
    def is_interface(self) -> bool:
        return isinstance(self.gi_info, GI.InterfaceInfo)

    @property
    def is_object(self) -> bool:
        return isinstance(self.gi_info, GI.ObjectInfo)

    @property
    def bases(self) -> tuple[type[Any], ...]:
        if self._bases is not None:
            return self._bases

        self._bases, self._gi_info = self.__get_bases_and_gi_info()

        return self._bases

    @property
    def gi_info(self) -> GI.RegisteredTypeInfo | None:
        if self._gi_info is not _MISSING:
            return self._gi_info

        self._bases, self._gi_info = self.__get_bases_and_gi_info()

        return self._gi_info

    @property
    def properties(self) -> PropertyInfoDict:
        if self._class_properties is not None:
            return self._class_properties

        self._class_properties, self._init_properties = self.__get_properties()

        return self._class_properties

    @property
    def init_properties(self) -> PropertyInfoDict:
        if self._init_properties is not None:
            return self._init_properties

        self._class_properties, self._init_properties = self.__get_properties()

        return self._init_properties

    @property
    def contents(self) -> str:
        if self._class_content is not None:
            return self._class_content

        self._class_content, self._fields = self.__get_contents_and_fields()

        return self._class_content

    @property
    def fields(self) -> list[GI.FieldInfo]:
        if self._fields is not None:
            return self._fields

        self._class_content, self._fields = self.__get_contents_and_fields()

        return self._fields

    def __get_bases_and_gi_info(
        self,
    ) -> tuple[tuple[type[Any], ...], GI.RegisteredTypeInfo | None]:
        full_module_name = f"{self.cls.__module__}.{self.cls.__qualname__}"
        object_info: GI.RegisteredTypeInfo | None = self.cls.__dict__.get("__info__")
        bases = list(get_original_bases(self.cls))

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
        if full_module_name.startswith("gi.overrides.") and any(
            base.__module__.startswith("gi.repository.") for base in bases
        ):
            bases: list[Any] = []
            gi_repo_full_name = full_module_name.replace(
                "gi.overrides.", "gi.repository.", 1
            )

            for base in get_original_bases(self.cls):
                if f"{base.__module__}.{base.__qualname__}" == gi_repo_full_name:
                    bases.extend(get_original_bases(base))

                    if object_info is None:
                        object_info = base.__dict__.get("__info__")
                elif base is not object and base not in bases:
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

    def __find_repo_property(
        self, prop_info: GI.PropertyInfo, /
    ) -> GIRepository.PropertyInfo | None:
        class_info = self.stub.repo.find_by_name(
            prop_info.get_namespace(), f"{prop_info.get_container().get_name()}"
        )
        prop_name = prop_info.get_name()

        if isinstance(
            class_info, (GIRepository.ObjectInfo, GIRepository.InterfaceInfo)
        ):
            for i in range(class_info.get_n_properties()):
                property = class_info.get_property(i)
                if property.get_name() == prop_name:
                    return property

        return None

    def __iterate_class_properties(
        self,
        gi_info: GI.ObjectInfo | GI.InterfaceInfo,
        *,
        include_interfaces: bool = False,
    ) -> Iterator[PropertyInfo]:
        interface_properties: Iterable[tuple[GI.PropertyInfo, ...]] = (
            (iface.get_properties() for iface in gi_info.get_interfaces())
            if isinstance(gi_info, GI.ObjectInfo) and include_interfaces
            else []
        )

        yield from (
            PropertyInfo(self.stub, prop, prop_info)
            for prop in itertools.chain(gi_info.get_properties(), *interface_properties)
            if (prop_info := self.__find_repo_property(prop)) is not None
        )

    def __iterate_parents(self) -> Iterator[GI.ObjectInfo]:
        if not isinstance(self.gi_info, GI.ObjectInfo):
            return

        current = self.gi_info.get_parent()
        while current is not None:
            yield current
            current = current.get_parent()

    def __iterate_parent_class_properties(self) -> Iterator[PropertyInfo]:
        for parent in self.__iterate_parents():
            yield from self.__iterate_class_properties(parent)

    def __get_properties(self) -> tuple[PropertyInfoDict, PropertyInfoDict]:
        if not isinstance(self.gi_info, (GI.ObjectInfo, GI.InterfaceInfo)):
            return {}, {}

        names: set[str] = set()
        class_props: PropertyInfoDict = {}
        init_props: PropertyInfoDict = {}

        for prop_info in self.__iterate_class_properties(
            self.gi_info, include_interfaces=True
        ):
            if (name := prop_info.name) in names:
                continue

            names.add(name)

            if prop_info.readable or (
                prop_info.writable and not prop_info.construct_only
            ):
                class_props[name] = prop_info

            if prop_info.writable or prop_info.construct or prop_info.construct_only:
                init_props[name] = prop_info

        for prop_info in self.__iterate_parent_class_properties():
            if (name := prop_info.name) in names:
                continue

            names.add(name)

            if prop_info.writable or prop_info.construct or prop_info.construct_only:
                init_props[name] = prop_info

        return class_props, init_props

    def __get_contents_and_fields(self) -> tuple[str, list[GI.FieldInfo]]:
        return _gi_build_stub_parts(
            self.stub, self.cls, _find_attributes(self.cls), self.cls, self.full_name
        )

    def __build_docstring(self) -> str | None:
        # extracting docs
        docs = (
            f"{(getattr(self.cls, '__doc__', '') or '').strip()}\n\n{
                getattr(self.cls, '__gdoc__', '') or ''
            }"
        ).strip()

        if docs:
            docs = '"""\n' + docs.strip() + '\n"""'
            return docs

        return None

    def __build_props_class(self) -> str | None:
        if override := self.stub.check_override(self.full_name, "Props"):
            return override

        if (
            not isinstance(self.gi_info, (GI.ObjectInfo, GI.InterfaceInfo))
            or not self.properties
        ):
            return None

        lines: list[str] = []

        for name, prop_info in self.properties.items():
            py_type = prop_info.prop_type

            if prop_info.readable and (
                not prop_info.writable or prop_info.construct_only
            ):
                lines.append(self.stub.get_property(name, py_type))
            else:
                lines.append(f"{name}: {py_type}")

        props_string = "\n".join(lines) or "..."

        parents_string = ""
        if isinstance(self.gi_info, GI.ObjectInfo) and (
            parent := self.gi_info.get_parent()
        ):
            parent_name = f"{parent.get_name()}"
            parents_string = f"({self.stub.get_namespace_member(parent.get_namespace(), parent_name)}.Props)"

        return f"""@{self.stub.get_import("typing", "type_check_only")}
class Props{parents_string}:
{textwrap.indent(props_string, "    ")}"""

    def __build_props_property(self, props_class: str | None) -> str | None:
        if override := self.stub.check_override(self.full_name, "props"):
            return override

        if isinstance(self.gi_info, GI.ObjectInfo) and props_class is not None:
            return self.stub.get_property("props", "Props")

        return None

    def __build_props(self) -> str | None:
        lines: list[str] = []

        if (props_class := self.__build_props_class()) is not None:
            lines.append(props_class)

        if (props_property := self.__build_props_property(props_class)) is not None:
            lines.append(props_property)

        return "\n".join(lines) if lines else None

    def __build_fields(self) -> str:
        lines: list[str] = []

        for field in self.fields:
            name = f"{field.get_name()}"

            if override := self.stub.check_override(self.full_name, name):
                lines.append(override)
            else:
                py_type = _type_info_to_python(
                    self.stub, field.get_type_info(), out=True
                )
                flags = field.get_flags()
                if not (flags & GI.FieldInfoFlags.IS_WRITABLE):
                    lines.append(self.stub.get_property(name, py_type))
                else:
                    lines.append(f"{name}: {py_type}")

        return "\n".join(lines)

    def __build_init(self) -> str | None:
        if override := self.stub.check_override(self.full_name, "__init__"):
            return override

        # Structs and Boxed use __new__ as constructor with a dummy __init__, but
        # overrides can introduce either __new__ or __init__. The priority below is:
        # 1. __new__ is the same as the "new" method from __info__
        # 2. __new__ exists on this class
        # 3. __init__ exists on this class
        if issubclass(self.cls, (GI.Boxed, GI.Struct)):
            if isinstance(self.cls.__new__, GI.BaseInfo) and isinstance(
                self.gi_info, (GI.StructInfo, GI.UnionInfo)
            ):
                for method_info in self.gi_info.get_methods():
                    if method_info.equal(self.cls.__new__):
                        return _build_function(
                            self.stub, "__init__", method_info, self.cls
                        )

            if "__new__" in self.cls.__dict__:
                return _build_function(
                    self.stub, "__init__", self.cls.__new__, self.cls
                )

            if "__init__" in self.cls.__dict__:
                return _build_function(
                    self.stub, "__init__", self.cls.__init__, self.cls
                )

        if not isinstance(self.gi_info, GI.ObjectInfo):
            return None

        if not self.init_properties:
            # Pango.Layout and Pango.FontDescription override __new__
            if "__new__" in self.cls.__dict__:
                return _build_function(
                    self.stub, "__init__", self.cls.__new__, self.cls
                )

            return None

        args: list[str] = []

        for name, init_prop in self.init_properties.items():
            args.append(f"{name}: {init_prop.init_type} = ...")

        return f"def __init__(self, *, {', '.join(args)}) -> None: ..."

    def build(self) -> str:
        if override := self.stub.check_override(self.prefix, self.name):
            return override

        if (
            not self.in_class
            and (alias := self.stub.get_alias(self.name, self.cls)) is not None
        ):
            # Set up a constant for classes that are aliases
            # NOTE: this should not use `Final` because doing so turns the alias into
            # a variable rather than a class
            return f"{self.name} = {alias}"

        string_parents = ""
        if self.bases:
            bases_strings = [
                self.stub.get_class_import(base)
                for base in self.bases
                if base is not object
            ]

            string_parents = f"({', '.join(bases_strings)})"

        lines = [f"class {self.name}{string_parents}:"]

        if docs := self.__build_docstring():
            lines.append(textwrap.indent(docs, "    "))

        if self.is_object and (props := self.__build_props()) is not None:
            lines.append(textwrap.indent(props, "    "))

        if class_fields := self.__build_fields():
            lines.append(textwrap.indent(class_fields, "    "))

        if class_constructor := self.__build_init():
            lines.append(textwrap.indent(class_constructor.strip(), "    "))

        lines.append(textwrap.indent(self.contents, "    "))

        class_string = "\n".join(lines).strip()

        if class_string.endswith(":"):
            class_string += " ..."

        return class_string


@dataclass(slots=True)
class Stub:
    repo: GIRepository.Repository
    parent: ObjectT
    namespace: str
    overrides: Overrides
    imports: InitVar[Imports]
    typevars: InitVar[TypeVars]
    needed_imports: dict[tuple[str, str | None], FromImport | Import] = field(
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
                if isinstance(_import, FromImport)
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
        full_name = _generate_full_name(prefix, name)
        if full_name in self.overrides:
            return "# override\n" + self.__fix_annotations(self.overrides[full_name])
        return None

    def __get_import(
        self, module: str, /, name: str | None = None
    ) -> FromImport | Import | None:
        module = _normalize_module_name(module, name)
        return self.needed_imports.get((module, name))

    def __add_import(
        self,
        module: str,
        /,
        name: str | None = None,
        import_as: str | None = None,
    ) -> Import | FromImport:
        module = _normalize_module_name(module, name)

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
        # Since mypy doesn't support infer_variance, we'll disable this for now and enable
        # it when/if it's supported (or when 3.11 is dropped)
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
        return self.get_typevar_tuple("_DataTs", default=f"tuple[()]")

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
        return f"{indent}@{property_symbol}\n{indent}def {name}(self) -> {return_annotation}: ..."

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
            ("gi.repository.", "gi.overrides.", "_gi.")
        ) or module.startswith(self.known_namespaces_prefixes):
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
        self, annotation: Any, /, *, fix_imports: bool = False
    ) -> str:
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

        return self.__fix_annotations(formatted, fix_imports=fix_imports)

    def format_signature(self, signature: inspect.Signature) -> str:
        try:
            # This requires Python 3.14
            formatted = signature.format(quote_annotation_strings=False)  # pyright: ignore[reportAttributeAccessIssue]
        except:
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

    def build(self) -> str:
        ret = _gi_build_stub_parts(self, self.parent, dir(self.parent), None, "")[0]

        extras: list[str] = []

        if self.namespace == "GObject":
            # TODO: find a better way to keep things (like protocols) that aren't in the actual module
            # but are needed for the stubs
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
    classes: dict[str, ClassInfo] = {}
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
                classes[name] = ClassInfo(stub, obj, name, prefix_name, in_class)
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
    if (in_class and issubclass(in_class, (GI.Boxed, GI.Struct, GObject.Object))) or (
        stub.check_override(prefix_name, "__init__")
    ):
        # __new__ and __init__ are handled during class construction as __init__
        functions.pop("__new__", None)
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
    for name, class_info in sorted(classes.items()):
        if class_string := class_info.build():
            ret += f"{class_string}\n"

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
    module: str,
    version: str,
    init: str | None,
    overrides: Overrides,
    imports: Imports,
    typevars: TypeVars,
) -> str:
    repo = GIRepository.Repository()
    repo.require(module, version, 0)  # type: ignore

    gi.require_version(module, version)
    m = importlib.import_module(f".{module}", "gi.repository")

    if init:
        exec(init)
    stub = Stub(repo, m, module, overrides, imports, typevars)
    return stub.build()


def _format(output: str, formatters: list[str], /, *, file: Path | None = None) -> str:
    for formatter in formatters:
        if file is not None:
            formatter = formatter.replace("%FILENAME%", str(file))

        try:
            proc = subprocess.run(
                [formatter],
                input=output,
                capture_output=True,
                shell=True,
                text=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(
                f"Formatter '{formatter}' failed with exit code {e.returncode}",
                file=sys.stderr,
            )
            print(e.stderr, file=sys.stderr)
            exit(2)

        output = proc.stdout

    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate module stubs")
    parser.add_argument("module", type=str, help="Gdk, Gtk, ...")
    parser.add_argument("version", type=str, help="3.0, 4.0, ...")
    parser.add_argument(
        "-u", dest="update", type=Path, help="Stub file to update e.g. -u Gdk.pyi"
    )
    parser.add_argument(
        "--init",
        type=str,
        help='Initialization code that must be evaluated first e.g. \'gi.require_version("Gst", "1.0"); from gi.repository import Gst; Gst.init(None)\'',
    )
    parser.add_argument(
        "--format",
        type=str,
        action="append",
        default=[],
        help='Formatter to run on generated stub (e.g. --format "black -q -")',
    )

    args = parser.parse_args()
    update_file: Path | None = args.update

    if update_file is not None:
        overrides: Overrides = {}
        imports: Imports = []
        typevars: TypeVars = []

        if update_file.exists():
            overrides, imports, typevars = parse(update_file.read_text())

        output = start(
            args.module, args.version, args.init, overrides, imports, typevars
        )

        print("Running with these overrides:")
        pprint.pprint(overrides)

        output = _format(output, args.format, file=update_file)
        update_file.write_text(output)
    else:
        print(
            _format(
                start(args.module, args.version, args.init, {}, [], []), args.format
            )
        )


if __name__ == "__main__":
    main()
