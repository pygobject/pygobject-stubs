# Based on https://github.com/PyCQA/astroid/blob/main/astroid/brain/brain_gi.py
# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE

from __future__ import annotations

from typing import Any
from typing import Callable
from typing import Optional
from typing import Type
from typing import Tuple
from typing import Union

import argparse
import importlib
import inspect
import re
from types import ModuleType

import gi
import gi._gi as GIRepository
from gi.repository import GObject

_identifier_re = r"^[A-Za-z_]\w*$"

ObjectT = Union[ModuleType, Type[Any]]


def object_get_props(
    obj: GIRepository.ObjectInfo, all: bool = False
) -> list[GIRepository.PropertyInfo]:
    props: list[GIRepository.PropertyInfo] = []
    for p in obj.get_properties():
        f = p.get_flags()
        if (
            all
            or f & GObject.ParamFlags.CONSTRUCT
            or f & GObject.ParamFlags.CONSTRUCT_ONLY
            or f & GObject.ParamFlags.WRITABLE
        ):
            props.append(p)

    parent = obj.get_parent()
    if parent and isinstance(parent, GIRepository.ObjectInfo):
        props.extend(object_get_props(obj.get_parent(), all))

    return props


def callable_get_arguments(
    type: GIRepository.CallbackInfo, current_namespace: str
) -> Tuple[set[str], list[str], list[str], list[str]]:
    needed_namespaces: set[str] = set()
    function_args = type.get_arguments()
    accept_optional_args = False
    names: list[str] = []
    args: list[str] = []
    return_args: list[str] = []
    skip: list[int] = []
    for (i, arg) in enumerate(function_args):
        (ns, t) = type_to_python(arg.get_type(), current_namespace, needed_namespaces)
        needed_namespaces.update(ns)

        if i in skip:
            continue

        if arg.get_closure() >= 0:
            accept_optional_args = True
            skip.append(arg.get_closure())
            skip.append(arg.get_destroy())

        if arg.get_closure() != i and arg.get_destroy() != i:
            direction = arg.get_direction()
            if (
                direction == GIRepository.Direction.OUT
                or direction == GIRepository.Direction.INOUT
            ):
                return_args.append(t)
            elif (
                direction == GIRepository.Direction.IN
                or direction == GIRepository.Direction.INOUT
            ):
                if arg.may_be_null() and t != "None":
                    args.append(f"Optional[{t}]")
                else:
                    args.append(t)
                names.append(arg.get_name())

    if accept_optional_args:
        names.append("*args")
        args.append("Any")

    (ns, return_type) = type_to_python(
        type.get_return_type(), current_namespace, needed_namespaces
    )
    needed_namespaces.update(ns)
    if type.may_return_null() and return_type != "None":
        return_type = f"Optional[{return_type}]"

    if return_type != "None" or len(return_args) == 0:
        return_args.insert(0, return_type)

    return (needed_namespaces, names, args, return_args)


def type_to_python(
    type: GIRepository.GTypeInfo, current_namespace: str, needed_namespaces: set[str]
) -> Tuple[set[str], str]:
    tag = type.get_tag()
    tags = GIRepository.TypeTag

    if tag == tags.ARRAY:
        array_type = type.get_param_type(0)
        (ns, t) = type_to_python(array_type, current_namespace, needed_namespaces)
        needed_namespaces.update(ns)
        return (needed_namespaces, f"list[{t}]")

    if tag == tags.BOOLEAN:
        return (needed_namespaces, "bool")

    if tag in (tags.DOUBLE, tags.FLOAT):
        return (needed_namespaces, "float")

    if tag == tags.ERROR:
        if current_namespace == "GLib":
            return (needed_namespaces, "Error")
        else:
            needed_namespaces.add("GLib")
            return (needed_namespaces, "GLib.Error")

    if tag in (tags.FILENAME, tags.GHASH, tags.UTF8, tags.UNICHAR):
        return (needed_namespaces, "str")

    if tag in (tags.GLIST, tags.GSLIST):
        # FIXME
        return (needed_namespaces, "list")

    if tag == tags.GTYPE:
        return (needed_namespaces, "Type")

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
        return (needed_namespaces, "int")

    if tag == tags.INTERFACE:
        interface = type.get_interface()
        if isinstance(interface, GIRepository.CallbackInfo):
            (ns, names, args, return_args) = callable_get_arguments(
                interface, current_namespace
            )
            needed_namespaces.update(ns)

            return_type = ""
            if len(return_args) == 1:
                return_type = return_args[0]
            else:
                return_type = f"Tuple[{', '.join(return_args)}]"

            # FIXME, how to express Callable with variable arguments?
            if len(names) > 0 and names[-1] == "*args":
                return (needed_namespaces, f"Callable[..., {return_type}]")
            else:
                return (
                    needed_namespaces,
                    f"Callable[[{', '.join(args)}], {return_type}]",
                )
        else:
            namespace = interface.get_namespace()
            name = interface.get_name()

            if namespace == "GObject" and name == "Value":
                return (needed_namespaces, "Any")

            if current_namespace == namespace:
                return (needed_namespaces, f"{name}")
            else:
                needed_namespaces.add(namespace)
                return (needed_namespaces, f"{namespace}.{name}")

    if tag == tags.VOID:
        return (needed_namespaces, "None")

    raise ValueError("TODO")


def build(parent: ObjectT, namespace: str) -> str:
    (ret, ns) = _gi_build_stub(parent, namespace, dir(parent))

    typings = "from typing import Any, Callable, Optional, Tuple, Type"
    imports = [f"from gi.repository import {n}" for n in sorted(ns)]

    return typings + "\n\n" + "\n".join(imports) + "\n\n\n" + ret


def _gi_build_stub(
    parent: ObjectT,
    current_namespace: str,
    children: list[str],
    needed_namespaces: set[str] = set(),
    in_class: Optional[Any] = None,
) -> Tuple[str, set[str]]:
    """
    Inspect the passed module recursively and build stubs for functions,
    classes, etc.
    """
    classes: dict[str, Type[Any]] = {}
    functions: dict[str, Callable[..., Any]] = {}
    constants: dict[str, Any] = {}
    flags: dict[str, Type[Any]] = {}
    enums: dict[str, Type[Any]] = {}

    for name in children:
        if name.startswith("__"):
            continue

        # Check if this is a valid name in python
        if not re.match(_identifier_re, name):
            continue

        try:
            obj = getattr(parent, name)
        except AttributeError:
            continue

        if inspect.isclass(obj):
            if not is_valid_class(name):
                continue
            if GObject.GFlags in obj.__mro__:
                flags[name] = obj
            elif GObject.GEnum in obj.__mro__:
                enums[name] = obj
            else:
                classes[name] = obj
        elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
            functions[name] = obj
        elif inspect.ismethod(obj) or inspect.ismethoddescriptor(obj):
            functions[name] = obj
        elif callable(obj):
            # Fall back to a function for anything callable
            functions[name] = obj
        elif in_class:
            # Check if obj was already processed
            if hasattr(in_class, "__info__"):
                obj_info = in_class.__info__
                if isinstance(
                    obj_info, (GIRepository.StructInfo, GIRepository.ObjectInfo)
                ):
                    if not (name in [f.get_name() for f in obj_info.get_fields()]):
                        constants[name] = 0
                else:
                    constants[name] = 0
            else:
                constants[name] = 0
        elif (
            str(obj).startswith("<flags")
            or str(obj).startswith("<enum ")
            or str(obj).startswith("<GType ")
            or inspect.isdatadescriptor(obj)
        ):
            constants[name] = 0
        elif isinstance(obj, (int, str, float)):
            constants[name] = obj
        else:
            # Assume everything else is some manner of constant
            constants[name] = 0

    ret = ""

    for name in sorted(constants):
        if name[0].isdigit():
            # GDK has some busted constant names like
            # Gdk.EventType.2BUTTON_PRESS
            continue

        val = constants[name]
        if val == 0:
            ret += f"{name} = ...\n"
        elif isinstance(val, (int, str, float)):
            ret += f"{name}: {val.__class__.__name__} = ...\n"
        else:
            raise ValueError
    if ret and constants:
        ret += "\n"

    for name in sorted(functions):
        if name.startswith("_"):
            continue

        function = functions[name]
        if isinstance(function, GIRepository.FunctionInfo) or isinstance(
            function, GIRepository.VFuncInfo
        ):
            constructor: bool = False
            method: bool = isinstance(function, GIRepository.VFuncInfo)
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
            (ns, names, args, return_args) = callable_get_arguments(
                function, current_namespace
            )
            needed_namespaces.update(ns)
            args_types = [f"{name}: {args[i]}" for (i, name) in enumerate(names)]

            # Return type
            if len(return_args) > 1:
                return_type = f"Tuple[{', '.join(return_args)}]"
            else:
                return_type = f"{', '.join(return_args)}"

            # Generate string
            prepend = ""
            if constructor:
                args_types.insert(0, "cls")
                prepend = "@classmethod\n"
                # Override return value, for example Gtk.Button.new returns a Gtk.Widget instead of Gtk.Button
                rt = function.get_container().get_name()
                if return_type != f"Optional[{rt}]":
                    return_type = rt
            elif method:
                args_types.insert(0, "self")
            elif static:
                prepend = "@staticmethod\n"

            ret += f"{prepend}def {name}({', '.join(str(a) for a in args_types)}) -> {return_type}: ...\n"
        else:
            ret += f"# TODO\ndef {name}(*args, **kwargs): ...\n"

    if ret and functions:
        ret += "\n"

    for name, obj in sorted(classes.items()):
        (classret, needed_namespaces) = _gi_build_stub(
            obj, current_namespace, find_methods(obj), needed_namespaces, obj
        )

        writable_props: list[GIRepository.PropertyInfo] = []
        all_props: list[GIRepository.ProperyInfo] = []
        parents: list[str] = []
        fields: list[str] = []
        if hasattr(obj, "__info__"):
            object_info = obj.__info__  # type: ignore

            if isinstance(object_info, GIRepository.StructInfo):
                for f in object_info.get_fields():
                    (ns, t) = type_to_python(
                        f.get_type(), current_namespace, needed_namespaces
                    )
                    needed_namespaces.update(ns)
                    n = f.get_name()
                    if n in dir(obj):
                        fields.append(f"{n}: {t}")

            if isinstance(object_info, GIRepository.ObjectInfo):
                p = object_info.get_parent()
                if p:
                    if current_namespace == p.get_namespace():
                        parents.append(f"{p.get_name()}")
                    else:
                        parents.append(f"{p.get_namespace()}.{p.get_name()}")
                        needed_namespaces.add(p.get_namespace())

                ifaces = object_info.get_interfaces()
                for i in ifaces:
                    if current_namespace == i.get_namespace():
                        parents.append(f"{i.get_name()}")
                    else:
                        parents.append(f"{i.get_namespace()}.{i.get_name()}")
                        needed_namespaces.add(i.get_namespace())

                for f in object_info.get_fields():
                    (ns, t) = type_to_python(
                        f.get_type(), current_namespace, needed_namespaces
                    )
                    needed_namespaces.update(ns)
                    n = f.get_name()
                    if n in dir(obj):
                        fields.append(f"{n}: {t}")

                # Properties
                writable_props = object_get_props(object_info, False)
                all_props = object_get_props(object_info, True)

            if issubclass(obj, GObject.GBoxed):
                if current_namespace == "GObject":
                    parents.append(f"GBoxed")
                else:
                    parents.append(f"GObject.GBoxed")
                    needed_namespaces.add("GObject")

            if issubclass(obj, GObject.GPointer):
                if current_namespace == "GObject":
                    parents.append(f"GPointer")
                else:
                    parents.append(f"GObject.GPointer")
                    needed_namespaces.add("GObject")

        string_parents = ""
        if len(parents) > 0:
            string_parents = f"({', '.join(parents)})"

        if (
            not classret
            and len(fields) == 0
            and len(writable_props) == 0
            and len(all_props) == 0
        ):
            ret += f"class {name}{string_parents}: ...\n"
        else:
            ret += f"class {name}{string_parents}:\n"

        if len(all_props) > 0:
            names: list[str] = []
            s: list[str] = []
            for p in all_props:
                n = p.get_name().replace("-", "_")
                if n in names:
                    # Avoid duplicates
                    continue
                names.append(n)
                (ns, t) = type_to_python(
                    p.get_type(), current_namespace, needed_namespaces
                )
                needed_namespaces.update(ns)
                s.append(f"{n}: {t} = ...")

            separator = "\n        "
            ret += f"    class {name}__Props:\n        {separator.join(s)}\n"
            ret += f"    props: {name}__Props = ...\n"

        if len(writable_props) > 0:
            names: list[str] = []
            s: list[str] = []
            for p in writable_props:
                n = p.get_name().replace("-", "_")
                if n in names:
                    # Avoid duplicates
                    continue
                names.append(n)
                (ns, t) = type_to_python(
                    p.get_type(), current_namespace, needed_namespaces
                )
                needed_namespaces.update(ns)
                s.append(f"{n}: {t} = ...")

            ret += f"    def __init__(self, {', '.join(s)}): ...\n"

        for field in fields:
            ret += f"    {field} = ...\n"

        for line in classret.splitlines():
            ret += "    " + line + "\n"

        ret += "\n"

    for name, obj in sorted(flags.items()):
        if current_namespace == "GObject":
            if name != "GFlags":
                base = "GFlags"
            else:
                base = ""
        else:
            needed_namespaces.add("GObject")
            base = "GObject.GFlags"

        ret += f"class {name}({base}):\n"
        for key in sorted(vars(obj)):
            if not key.startswith("__"):
                ret += f"    {key} = ...\n"
        ret += "\n"

    for name, obj in sorted(enums.items()):
        if current_namespace == "GObject":
            if name != "GEnum":
                base = "GEnum"
            else:
                base = ""
        else:
            needed_namespaces.add("GObject")
            base = "GObject.GEnum"

        ret += f"class {name}({base}):\n"
        for key in sorted(vars(obj)):
            if not key.startswith("__"):
                ret += f"    {key} = ...\n"
        ret += "\n"

    return (ret, needed_namespaces)


def is_valid_class(name: str) -> bool:
    if name.endswith("Private"):
        return False
    if name.endswith("Iface"):
        return False
    return True


def find_methods(obj: Type[Any]) -> list[str]:
    mro = inspect.getmro(obj)
    main_name = get_gname(mro[0])

    all_attrs = set(dir(obj))
    other_attrs: set[str] = set()
    for o in mro[1:]:
        name = get_gname(o)
        if name == main_name:
            continue
        other_attrs.update(dir(o))

    obj_attrs = all_attrs - other_attrs

    # Search for overridden methods
    if hasattr(obj, "__info__"):
        obj_info = obj.__info__  # type: ignore
        if isinstance(obj_info, (GIRepository.ObjectInfo, GIRepository.StructInfo)):
            methods = obj_info.get_methods()
            for m in methods:
                name = m.get_name()
                if name in dir(obj) and not name in obj_attrs:
                    obj_attrs.add(name)

    return sorted(list(obj_attrs))


def get_gname(obj: Type[Any]) -> Optional[str]:
    if not hasattr(obj, "__gtype__"):
        return None
    return obj.__gtype__.name  # type: ignore


description = "Generate module stubs\n\nUsage: generate.py Gdk 3.0 > Gdk.py"

parser = argparse.ArgumentParser(description=description)
parser.add_argument("module", type=str, help="Gdk, Gtk, ...")
parser.add_argument("version", type=str, help="3.0, 4.0, ...")

args = parser.parse_args()

gi.require_version(args.module, args.version)
module = importlib.import_module(f".{args.module}", "gi.repository")
print(build(module, args.module))
