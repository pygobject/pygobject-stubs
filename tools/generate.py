#!/usr/bin/env python3

# Based on https://github.com/PyCQA/astroid/blob/main/astroid/brain/brain_gi.py
# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE

from __future__ import annotations

import typing

import argparse
import importlib
import inspect
import itertools
import pprint
import re
import textwrap
from types import ModuleType

import gi
import gi._gi as GI
import parse

gi.require_version("GIRepository", "3.0")
from gi.repository import GIRepository
from gi.repository import GObject

_identifier_re = r"^[A-Za-z_]\w*$"

ObjectT = typing.Union[ModuleType, typing.Type[typing.Any]]

RESERVED_KEYWORDS = {"async"}
ALLOWED_FUNCTIONS = {
    "__enter__",
    "__exit__",
    "__iter__",
    "__getitem__",
    "__setitem__",
    "__len__",
    "__int__",
    "__float__",
    "__bool__",
}


def fix_argument_name(name: str) -> str:
    if name in RESERVED_KEYWORDS:
        name = f"_{name}"
    return name.replace("-", "_")


def _object_get_props(
    repo: GIRepository.Repository,
    obj: GI.ObjectInfo,
) -> typing.Tuple[list[GIRepository.BaseInfo], list[GIRepository.BaseInfo]]:
    parents: list[GI.ObjectInfo] = []
    parent: typing.Optional[GI.ObjectInfo] = obj.get_parent()
    while parent:
        parents.append(parent)
        parent = parent.get_parent()

    interfaces: list[GI.InterfaceInfo] = list(obj.get_interfaces())

    subclasses: list[GI.ObjectInfo | GI.InterfaceInfo] = parents + interfaces

    props: list[GI.PropertyInfo] = list(obj.get_properties())
    for s in subclasses:
        props.extend(s.get_properties())

    readable_props: list[GIRepository.BaseInfo] = []
    writable_props: list[GIRepository.BaseInfo] = []

    for prop in props:
        namespace = prop.get_namespace()
        container = prop.get_container()
        class_info = repo.find_by_name(namespace, container.get_name())
        if class_info is None:
            raise Exception(f"Unable to find {namespace}.{container}")

        if isinstance(class_info, GIRepository.ObjectInfo):
            n_props = GIRepository.ObjectInfo.get_n_properties(class_info)
            for i in range(n_props):
                p: GIRepository.BaseInfo = GIRepository.ObjectInfo.get_property(
                    class_info, i
                )
                if p.get_name() == prop.get_name():
                    flags = GIRepository.PropertyInfo.get_flags(p)
                    if flags & GObject.ParamFlags.READABLE:
                        readable_props.append(p)
                    if flags & GObject.ParamFlags.WRITABLE:
                        writable_props.append(p)

        if isinstance(class_info, GIRepository.InterfaceInfo):
            n_props = GIRepository.InterfaceInfo.get_n_properties(class_info)
            for i in range(n_props):
                p: GIRepository.BaseInfo = GIRepository.InterfaceInfo.get_property(
                    class_info, i
                )
                if p.get_name() == prop.get_name():
                    flags = GIRepository.PropertyInfo.get_flags(p)
                    if flags & GObject.ParamFlags.READABLE:
                        readable_props.append(p)
                    if flags & GObject.ParamFlags.WRITABLE:
                        writable_props.append(p)

    return (readable_props, writable_props)


def _callable_get_arguments(
    type: GI.CallbackInfo,
    current_namespace: str,
    needed_namespaces: set[str],
    can_default: bool = False,
) -> typing.Tuple[list[str], list[str], list[str]]:
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
                t = _type_to_python(
                    arg.get_type_info(), current_namespace, needed_namespaces, True
                )

                dict_return_args[i] = t
            elif direction == GI.Direction.IN or direction == GI.Direction.INOUT:
                dict_names[i] = arg.get_name()
                dict_args[i] = arg

    # Traverse args in reverse to check for optional args
    args = list(dict_args.values())
    for a in reversed(args):
        t = _type_to_python(
            a.get_type_info(),
            current_namespace,
            needed_namespaces,
            False,
            a.get_closure_index() >= 0,  # True if function admits variable arguments
        )

        if a.may_be_null() and t != "None":
            if can_default:
                str_args.append(f"typing.Optional[{t}] = None")
            else:
                str_args.append(f"typing.Optional[{t}]")
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
        str_args.append("typing.Any")

    return_type = _type_to_python(
        type.get_return_type(), current_namespace, needed_namespaces, True
    )
    if type.may_return_null() and return_type != "None" and not is_async_res:
        return_type = f"typing.Optional[{return_type}]"

    return_args = list(dict_return_args.values())
    if return_type != "None" or len(return_args) == 0:
        return_args.insert(0, return_type)

    return (names, str_args, return_args)


class TypeInfo:
    # This struct tries to emulate gi.TypeInfo

    def __init__(
        self,
        obj: typing.Any,
        get_tag: typing.Callable[[TypeInfo], int],
        get_param_type: typing.Callable[[TypeInfo, int], TypeInfo],
        get_interface: typing.Callable[[TypeInfo], TypeInfo],
    ):
        self.obj = obj
        self._get_tag = get_tag
        self._get_param_type = get_param_type
        self._get_interface = get_interface

    def get_tag(self) -> int:
        return self._get_tag(self.obj)

    def get_param_type(self, n: int) -> TypeInfo:
        type = self._get_param_type(self.obj, n)
        return TypeInfo(type, self._get_tag, self._get_param_type, self._get_interface)

    def get_interface(self) -> TypeInfo:
        type = self._get_interface(self.obj)
        return TypeInfo(type, self._get_tag, self._get_param_type, self._get_interface)

    def get_name(self) -> str:
        return self.obj.get_name()

    def get_namespace(self) -> str:
        return self.obj.get_namespace()

    def get_type_info(self) -> GI.InfoType:
        return self.obj.get_type_info()


def _build_type(type: GIRepository.BaseInfo) -> TypeInfo:
    return TypeInfo(
        type,
        GIRepository.TypeInfo.get_tag,
        GIRepository.TypeInfo.get_param_type,
        GIRepository.TypeInfo.get_interface,
    )


def _type_to_python(
    type: TypeInfo,
    current_namespace: str,
    needed_namespaces: set[str],
    out_arg: bool = False,
    varargs: bool = False,
) -> str:
    tag = type.get_tag()
    tags = GI.TypeTag

    if tag == tags.ARRAY:
        array_type = type.get_param_type(0)
        t = _type_to_python(array_type, current_namespace, needed_namespaces)
        if out_arg:
            # As output argument array of type uint8 are returned as bytes
            if array_type.get_tag() == GI.TypeTag.UINT8:
                return f"bytes"
            return f"list[{t}]"

        # As input arguments array can be generated by any sequence
        return f"typing.Sequence[{t}]"

    if tag in (tags.GLIST, tags.GSLIST):
        array_type = type.get_param_type(0)
        t = _type_to_python(array_type, current_namespace, needed_namespaces)
        return f"list[{t}]"

    if tag == tags.BOOLEAN:
        return "bool"

    if tag in (tags.DOUBLE, tags.FLOAT):
        return "float"

    if tag == tags.ERROR:
        if current_namespace == "GLib":
            return "Error"
        else:
            needed_namespaces.add("GLib")
            return "GLib.Error"

    if tag == tags.GHASH:
        key_type = type.get_param_type(0)
        value_type = type.get_param_type(1)
        kt = _type_to_python(key_type, current_namespace, needed_namespaces)
        vt = _type_to_python(value_type, current_namespace, needed_namespaces)
        return f"dict[{kt}, {vt}]"

    if tag in (tags.FILENAME, tags.UTF8, tags.UNICHAR):
        return "str"

    if tag == tags.GTYPE:
        return "typing.Type[typing.Any]"

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
            (names, args, return_args) = _callable_get_arguments(
                interface, current_namespace, needed_namespaces
            )

            return_type = ""
            if len(return_args) == 1:
                return_type = return_args[0]
            else:
                return_type = f"typing.Tuple[{', '.join(return_args)}]"

            # FIXME, how to express Callable with variable arguments?
            if (len(names) > 0 and names[-1].startswith("*")) or varargs:
                return f"typing.Callable[..., {return_type}]"
            else:
                return f"typing.Callable[[{', '.join(args)}], {return_type}]"
        else:
            namespace = interface.get_namespace()
            name = interface.get_name()

            if not re.match(_identifier_re, name):
                # Convert Flags and Enums with invalid name to int
                # Example NM 1.0 library
                if interface.get_type() in (
                    GIRepository.InfoType.FLAGS,
                    GIRepository.InfoType.ENUM,
                ):
                    return "int"

            if namespace == "GObject" and name == "Value":
                return "typing.Any"

            if namespace == "GObject" and name == "Closure":
                return "typing.Callable[..., typing.Any]"

            if namespace == "cairo" and name == "Context" and not out_arg:
                return "cairo.Context[_SomeSurface]"

            if current_namespace == namespace:
                return f"{name}"
            else:
                needed_namespaces.add(namespace)
                return f"{namespace}.{name}"

    if tag == tags.VOID:
        return "None"

    raise ValueError("TODO")


def _build(
    repo: GIRepository.Repository,
    parent: ObjectT,
    namespace: str,
    overrides: dict[str, str],
) -> str:
    ns: set[str] = set()
    ret = _gi_build_stub(repo, parent, namespace, dir(parent), ns, overrides, None, "")

    imports: list[str] = []
    typevars: list[str] = [
        'T = typing.TypeVar("T")',
    ]

    if namespace == "Gtk":
        imports.append("import os")
        typevars.append(
            """CellRendererT = typing.TypeVar(
    "CellRendererT",
    CellRendererCombo,
    CellRendererPixbuf,
    CellRendererProgress,
    CellRendererSpin,
    CellRendererSpinner,
    CellRendererText,
    CellRendererToggle,
)
WidgetT = typing.TypeVar("WidgetT", bound=Widget)
"""
        )
    elif namespace == "GObject":
        imports.append("import enum")

    if "cairo" in ns:
        imports.append("import cairo")
        typevars.append(
            '_SomeSurface = typing.TypeVar("_SomeSurface", bound=cairo.Surface)'
        )
        ns.remove("cairo")

    imports += [f"from gi.repository import {n}" for n in sorted(ns)]

    return (
        "import typing\n"
        + "from typing_extensions import Self\n"
        + "\n"
        + "\n".join(imports)
        + "\n"
        + "\n".join(typevars)
        + "\n\n"
        + ret
    )


def _generate_full_name(prefix: str, name: str) -> str:
    full_name = name
    if len(prefix) > 0:
        full_name = f"{prefix}.{name}"
    return full_name


def _build_function_info(
    current_namespace: str,
    name: str,
    function: GI.FunctionInfo | GI.VFuncInfo,
    in_class: typing.Optional[typing.Any],
    needed_namespaces: set[str],
    return_signature: typing.Optional[str] = None,
    comment: typing.Optional[str] = None,
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
    (names, args, return_args) = _callable_get_arguments(
        function, current_namespace, needed_namespaces, True
    )
    args_types = [
        f"{fix_argument_name(name)}: {args[i]}" for (i, name) in enumerate(names)
    ]

    # Return type
    if return_signature:
        return_type = return_signature
    elif len(return_args) > 1:
        return_type = f"typing.Tuple[{', '.join(return_args)}]"
    else:
        return_type = f"{return_args[0]}"

    # Generate string
    prepend = ""
    if constructor:
        args_types.insert(0, "cls")
        prepend = "@classmethod\n"
        # Override return value, for example Gtk.Button.new returns a Gtk.Widget instead of Gtk.Button
        rt = function.get_container().get_name()
        if return_type != f"typing.Optional[{rt}]":
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
    current_namespace: str,
    name: str,
    function: typing.Any,
    in_class: typing.Optional[typing.Any],
    needed_namespaces: set[str],
) -> str:
    real_function = function.__wrapped__
    fail_ret = inspect.getclosurevars(function).nonlocals.get("fail_ret")

    (_, _, return_args) = _callable_get_arguments(
        real_function, current_namespace, needed_namespaces
    )
    return_args = return_args[1:]  # Strip first return value

    if len(return_args) > 1:
        return_signature = f"typing.Tuple[{', '.join(return_args)}]"
    else:
        return_signature = f"{return_args[0]}"

    if fail_ret is None:
        return_signature = f"typing.Optional[{return_signature}]"
    else:
        if type(fail_ret) is tuple:
            if len(fail_ret) > 0:
                return_signature = f"({return_signature} | typing.Tuple{str(fail_ret).replace('(', '[').replace(')', ']')})"
            else:
                return_signature = f"({return_signature} | typing.Tuple[()])"
        else:
            return_signature = f"({return_signature} | typing.Literal[{fail_ret}])"

    return _build_function_info(
        current_namespace,
        name,
        real_function,
        in_class,
        needed_namespaces,
        return_signature,
        "CHECK Wrapped function",
    )


def _build_function(
    current_namespace: str,
    name: str,
    function: typing.Any,
    in_class: typing.Optional[typing.Any],
    needed_namespaces: set[str],
) -> str:
    if name.startswith("_") and name not in ALLOWED_FUNCTIONS:
        return ""

    if hasattr(function, "__wrapped__"):
        if "strip_boolean_result" in str(function):
            return _wrapped_strip_boolean_result(
                current_namespace, name, function, in_class, needed_namespaces
            )

    if isinstance(function, GI.FunctionInfo) or isinstance(function, GI.VFuncInfo):
        return _build_function_info(
            current_namespace, name, function, in_class, needed_namespaces
        )

    signature_string: str
    missing_annotation = False
    try:
        signature = inspect.signature(function)
        for param in signature.parameters.values():
            if param.name != "self" and param.annotation is inspect.Parameter.empty:
                missing_annotation = True
        if signature.return_annotation is inspect.Signature.empty:
            missing_annotation = True
        try:
            # This requires Python 3.14
            signature_string = signature.format(quote_annotation_strings=False)
        except:
            # This should be a good enough fallback for older Pythons
            signature_string = str(signature).replace('"', "").replace("'", "")
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


def _check_override(
    prefix: str, name: str, overrides: dict[str, str]
) -> typing.Optional[str]:
    full_name = _generate_full_name(prefix, name)
    if full_name in overrides:
        return "# override\n" + overrides[full_name]
    return None


def _format_annotation(annotation: typing.Any) -> str:
    try:
        # This requires Python 3.14
        return inspect.formatannotation(annotation, quote_annotation_strings=False)
    except:
        # This should be a good enough fallback for older Pythons
        return inspect.formatannotation(annotation).replace('"', "").replace("'", "")


def _gi_build_stub(
    repo: GIRepository.Repository,
    parent: ObjectT,
    current_namespace: str,
    children: list[str],
    needed_namespaces: set[str],
    overrides: dict[str, str],
    in_class: typing.Optional[typing.Any],
    prefix_name: str,
) -> str:
    return _gi_build_stub_parts(
        repo,
        parent,
        current_namespace,
        children,
        needed_namespaces,
        overrides,
        in_class,
        prefix_name,
    )[0]


def _gi_build_stub_parts(
    repo: GIRepository.Repository,
    parent: ObjectT,
    current_namespace: str,
    children: list[str],
    needed_namespaces: set[str],
    overrides: dict[str, str],
    in_class: typing.Optional[typing.Any],
    prefix_name: str,
) -> tuple[str, list[GI.FieldInfo]]:
    """
    Inspect the passed module recursively and build stubs for functions,
    classes, etc.
    """
    classes: dict[str, typing.Type[typing.Any]] = {}
    functions: dict[str, typing.Callable[..., typing.Any]] = {}
    constants: dict[str, typing.Any] = {}
    flags: dict[str, typing.Type[typing.Any]] = {}
    enums: dict[str, typing.Type[typing.Any]] = {}

    ret = ""

    for name in children:
        if name.startswith("__") and name not in ALLOWED_FUNCTIONS:
            continue

        # Check if this is a valid name in python
        if not re.match(_identifier_re, name):
            continue

        try:
            obj = getattr(parent, name)
        except AttributeError:
            continue

        if inspect.isclass(obj):
            if GObject.GFlags in obj.__mro__ or str(obj).startswith("<flag"):
                flags[name] = obj
            elif GObject.GEnum in obj.__mro__ or str(obj).startswith("<enum"):
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
        ret += f"{name}: {_format_annotation(annotations[name])}\n"

    # Constants
    for name in sorted(constants):
        if name[0].isdigit():
            # GDK has some busted constant names like
            # Gdk.EventType.2BUTTON_PRESS
            continue

        override = _check_override(prefix_name, name, overrides)
        if override:
            ret += override + "\n"
            continue

        val = constants[name]

        if str(val.__class__).startswith(("<flag", "<enum")):
            val = val.real

        annotation = getattr(parent, "__annotations__", {}).get(name)
        if annotation:
            annotation_string = _format_annotation(annotation)
        else:
            annotation_string = val.__class__.__name__

        if isinstance(val, str):
            if len(val) > 50:
                ret += f"{name}: {annotation_string} = ...\n"
            else:
                ret += f'{name}: {annotation_string} = "{val}"\n'
        elif isinstance(val, (bool, float, int)):
            ret += f"{name}: {annotation_string} = {val}\n"
        elif val.__class__.__name__ == "Atom":
            ret += f"{name}: {annotation_string} = ...\n"
        elif annotation is not None:
            ret += f"{name}: {annotation_string} = ...\n"
        else:
            ret += f"{name} = ...  # FIXME: Constant is missing typing annotation\n"

    if ret and functions:
        ret += "\n"

    # Functions
    for name in sorted(functions):
        override = _check_override(prefix_name, name, overrides)
        if override:
            ret += override + "\n"
            continue

        ret += _build_function(
            current_namespace, name, functions[name], in_class, needed_namespaces
        )

    if ret and classes:
        ret += "\n"

    # Classes
    for name, obj in sorted(classes.items()):
        override = _check_override(prefix_name, name, overrides)
        if override:
            ret += override + "\n\n"
            continue

        full_name = _generate_full_name(prefix_name, name)

        classret, fields = _gi_build_stub_parts(
            repo,
            obj,
            current_namespace,
            _find_attributes(obj),
            needed_namespaces,
            overrides,
            obj,
            full_name,
        )

        readable_props: list[GIRepository.BaseInfo] = []
        writable_props: list[GIRepository.BaseInfo] = []
        parents: list[str] = []
        props_parents: list[str] = []
        object_info = obj.__dict__.get("__info__")
        bases = [obj] if object_info else obj.__bases__
        for b in bases:
            object_info = b.__dict__.get("__info__")
            gtype = b.__dict__.get("__gtype__")

            if isinstance(object_info, GI.ObjectInfo):
                p = object_info.get_parent()
                if p:
                    if current_namespace == p.get_namespace():
                        parents.append(f"{p.get_name()}")
                    else:
                        parents.append(f"{p.get_namespace()}.{p.get_name()}")
                        needed_namespaces.add(p.get_namespace())
                    props_parents.append(f"{parents[-1]}.Props")

                ifaces = object_info.get_interfaces()
                for i in ifaces:
                    if current_namespace == i.get_namespace():
                        parents.append(f"{i.get_name()}")
                    else:
                        parents.append(f"{i.get_namespace()}.{i.get_name()}")
                        needed_namespaces.add(i.get_namespace())

                # Properties
                (rp, wp) = _object_get_props(repo, object_info)
                readable_props.extend(rp)
                writable_props.extend(wp)

            elif isinstance(object_info, GI.InterfaceInfo):
                if current_namespace == "GObject":
                    parents.append("Object")
                else:
                    parents.append("GObject.GInterface")
                    needed_namespaces.add("GObject")

            elif gtype and issubclass(b, GObject.GBoxed):
                if current_namespace == "GObject":
                    parents.append(f"GBoxed")
                else:
                    parents.append(f"GObject.GBoxed")
                    needed_namespaces.add("GObject")

            elif gtype and issubclass(b, GObject.GPointer):
                if current_namespace == "GObject":
                    parents.append(f"GPointer")
                else:
                    parents.append(f"GObject.GPointer")
                    needed_namespaces.add("GObject")

            else:
                # Add non-GI base classes. Overrides could define new classes, such as:
                # class FooError(Exception):
                #    pass
                type_fullname = f"{b.__module__}.{b.__qualname__}"
                if type_fullname.startswith("gi.overrides."):
                    type_fullname = type_fullname[len("gi.overrides.") :]
                ns, type_name = type_fullname.split(".", 1)
                if ns == current_namespace:
                    parents.append(type_name)
                elif ns == "builtins":
                    if type_name != "object":
                        parents.append(type_name)
                else:
                    parents.append(type_fullname)
                    needed_namespaces.add(ns)

        string_parents = ""
        if len(parents) > 0:
            string_parents = f"({', '.join(parents)})"

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

        props_override = _check_override(full_name, "Props", overrides)
        if props_override:
            for line in props_override.splitlines():
                ret += "    " + line + "\n"
        elif len(readable_props) > 0 or len(writable_props) > 0:
            names: list[str] = []
            s: list[str] = []
            for p in itertools.chain(readable_props, writable_props):
                n = fix_argument_name(p.get_name())
                if n in names:
                    # Avoid duplicates
                    continue
                names.append(n)
                type = _build_type(GIRepository.PropertyInfo.get_type_info(p))
                t = _type_to_python(type, current_namespace, needed_namespaces, True)

                # Check getter/setter
                getter = GIRepository.PropertyInfo.get_getter(p)
                setter = GIRepository.PropertyInfo.get_setter(p)
                if getter and GIRepository.CallableInfo.may_return_null(getter):
                    s.append(f"{n}: typing.Optional[{t}]")
                elif setter and not getter:
                    # If is writable only prop check if setter can accept NULL
                    arg_info = GIRepository.CallableInfo.get_arg(setter, 0)
                    if GIRepository.ArgInfo.may_be_null(arg_info):
                        s.append(f"{n}: typing.Optional[{t}]")
                    else:
                        s.append(f"{n}: {t}")
                else:
                    s.append(f"{n}: {t}")

            props_string_parents = ""
            if len(props_parents) > 0:
                props_string_parents = f"({', '.join(props_parents)})"

            separator = "\n        "
            ret += (
                f"    class Props{props_string_parents}:\n        {separator.join(s)}\n"
            )
            ret += f"    props: Props = ...\n"

        for f in fields:
            t = _type_to_python(
                f.get_type_info(), current_namespace, needed_namespaces, True
            )
            n = f.get_name()
            override = _check_override(full_name, n, overrides)
            if override:
                ret += f"    {override} = ...\n"
            else:
                ret += f"    {n}: {t} = ...\n"

        class_constructor_override = _check_override(full_name, "__init__", overrides)
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
                type = _build_type(GIRepository.PropertyInfo.get_type_info(p))
                t = _type_to_python(type, current_namespace, needed_namespaces)
                setter = GIRepository.PropertyInfo.get_setter(p)
                if setter:
                    arg_info = GIRepository.CallableInfo.get_arg(setter, 0)
                    if GIRepository.ArgInfo.may_be_null(arg_info):
                        s.append(f"{n}: typing.Optional[{t}] = ...")
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
        override = _check_override(prefix_name, name, overrides)
        if override:
            ret += override + "\n\n"
            continue

        full_name = _generate_full_name(prefix_name, name)

        if current_namespace == "GObject":
            if name != "GFlags":
                base = "GFlags"
            else:
                base = "enum.IntFlag"
        else:
            needed_namespaces.add("GObject")
            base = "GObject.GFlags"

        ret += f"class {name}({base}):\n"
        for key in sorted(vars(obj)):
            if key.startswith(("__", "_")) or key[0].isdigit():
                continue

            override = _check_override(full_name, key, overrides)
            if override:
                for line in override.splitlines():
                    ret += "    " + line + "\n"
                continue

            o = getattr(obj, key)
            if isinstance(o, GI.FunctionInfo):
                function_ret = _build_function(
                    current_namespace, key, o, obj, needed_namespaces
                )
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
        override = _check_override(prefix_name, name, overrides)
        if override:
            ret += override + "\n\n"
            continue

        full_name = _generate_full_name(prefix_name, name)

        if current_namespace == "GObject":
            if name != "GEnum":
                base = "GEnum"
            else:
                base = "enum.IntEnum"
        else:
            needed_namespaces.add("GObject")
            base = "GObject.GEnum"

        # Some Enums can be empty in the end
        ret += f"class {name}({base}):\n"
        length_before = len(ret)
        for key in sorted(vars(obj)):
            if key.startswith(("__", "_")) or key[0].isdigit():
                continue

            override = _check_override(full_name, key, overrides)
            if override:
                for line in override.splitlines():
                    ret += "    " + line + "\n"
                continue

            o = getattr(obj, key)
            if isinstance(o, GI.FunctionInfo):
                function_ret = _build_function(
                    current_namespace, key, o, obj, needed_namespaces
                )
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


def _find_attributes(obj: typing.Type[typing.Any]) -> list[str]:
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
    module: str, version: str, init: str | None, overrides: dict[str, str]
) -> str:
    repo = GIRepository.Repository()
    repo.require(module, version, 0)  # type: ignore
    m = importlib.import_module(f".{module}", "gi.repository")
    if init:
        exec(init)
    return _build(repo, m, module, overrides)


if __name__ == "__main__":
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
        overrides: dict[str, str] = {}
        try:
            with open(args.update, "r") as file:
                overrides = parse.parse(file.read())
        except FileNotFoundError:
            pass
        output = start(args.module, args.version, args.init, overrides)
        print("Running with these overrides:")
        pprint.pprint(overrides)
        with open(args.update, "w+") as file:
            file.write(output)
    else:
        print(start(args.module, args.version, args.init, {}))
