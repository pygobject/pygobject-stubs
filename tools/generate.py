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


def callable_get_arguments(type: GIRepository.CallbackInfo,
                           current_namespace: str) -> Tuple[set[str], list[str], list[str], list[str]]:
    needed_namespaces: set[str] = set()
    function_args = type.get_arguments()
    accept_optional_args = False
    names: list[str] = []
    args: list[str] = []
    return_args: list[str] = []
    skip: list[int] = []
    for (i, arg) in enumerate(function_args):
        (ns, t) = type_to_python(arg.get_type(),
                                 current_namespace,
                                 needed_namespaces)
        needed_namespaces.update(ns)

        if i in skip:
            continue

        if arg.get_closure() >= 0:
            accept_optional_args = True
            skip.append(arg.get_closure())
            skip.append(arg.get_destroy())

        if arg.get_closure() != i and arg.get_destroy() != i:
            direction = arg.get_direction()
            if direction == GIRepository.Direction.OUT or direction == GIRepository.Direction.INOUT:
                return_args.append(t)
            elif direction == GIRepository.Direction.IN or direction == GIRepository.Direction.INOUT:
                if arg.may_be_null() and t != "None":
                    args.append(f"Optional[{t}]")
                else:
                    args.append(t)
                names.append(arg.get_name())

    if accept_optional_args:
        args.append("*args")

    (ns, return_type) = type_to_python(type.get_return_type(),
                                       current_namespace,
                                       needed_namespaces)
    needed_namespaces.update(ns)
    if type.may_return_null() and return_type != "None":
        return_type = f"Optional[{return_type}]"

    if return_type != "None" or len(return_args) == 0:
        return_args.insert(0, return_type)

    return (needed_namespaces, names, args, return_args);


def type_to_python(type: GIRepository.GTypeInfo,
                   current_namespace: str,
                   needed_namespaces: set[str]) -> Tuple[set[str], str]:
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
        if current_namespace == "GObject":
            return (needed_namespaces, "GType")
        else:
            needed_namespaces.add("GObject")
            return (needed_namespaces, "GObject.GType")

    if tag in (tags.INT8,
               tags.INT16,
               tags.INT32,
               tags.INT64,
               tags.UINT8,
               tags.UINT16,
               tags.UINT32,
               tags.UINT64):
        return (needed_namespaces, "int")

    if tag == tags.INTERFACE:
        interface = type.get_interface()
        if isinstance(interface, GIRepository.CallbackInfo):
            (ns, _, args, return_args) = callable_get_arguments(interface, current_namespace)
            needed_namespaces.update(ns)

            return_type = ""
            if len(return_args) == 1:
                return_type = return_args[0]
            else:
                return_type = f"Tuple[{', '.join(return_args)}]"

            # FIXME, how to express Callable with variable arguments?
            if len(args) > 0 and args[-1] == "*args":
                return (needed_namespaces, f"Callable[..., {return_type}]")
            else:
                return (needed_namespaces, f"Callable[[{', '.join(args)}], {return_type}]")
        else:
            namespace = interface.get_namespace()
            if current_namespace == namespace:
                return (needed_namespaces, f"{interface.get_name()}")
            else:
                needed_namespaces.add(namespace)
                return (needed_namespaces, f"{namespace}.{interface.get_name()}")

    if tag == tags.VOID:
        return (needed_namespaces, "None")

    raise ValueError("TODO")


def build(parent: ObjectT, namespace: str) -> str:
    (ret, ns) = _gi_build_stub(parent, namespace, dir(parent))

    typings = "from typing import Callable, Optional, Tuple"
    imports = [f"from gi.repository import {n}" for n in sorted(ns)]

    return typings + "\n\n" + "\n".join(imports) + "\n\n\n" + ret


def _gi_build_stub(parent: ObjectT,
                   current_namespace: str,
                   children: list[str],
                   needed_namespaces: set[str] = set(),
                   in_class: bool = False) -> Tuple[str, set[str]]:
    """
    Inspect the passed module recursively and build stubs for functions,
    classes, etc.
    """
    classes: dict[str, Type[Any]] = {}
    functions: dict[str, Callable[..., Any]] = {}
    constants: dict[str, Any] = {}
    methods: dict[str, Callable[..., Any]] = {}
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
            methods[name] = obj
        elif (
            str(obj).startswith("<flags")
            or str(obj).startswith("<enum ")
            or str(obj).startswith("<GType ")
            or inspect.isdatadescriptor(obj)
        ):
            constants[name] = 0
        elif isinstance(obj, (int, str, float)):
            constants[name] = obj
        elif callable(obj):
            # Fall back to a function for anything callable
            functions[name] = obj
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
        if hasattr(function, "get_arguments"):
            constructor: bool = False
            method: bool = False
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
            (ns, names, args, return_args) = callable_get_arguments(function, current_namespace);
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
            elif method:
                args_types.insert(0, "self")
            elif static:
                prepend = "@staticmethod\n"

            ret += f"{prepend}def {name}({', '.join(str(a) for a in args_types)}) -> {return_type}: ...\n"
        else:
            ret += f"# TODO\ndef {name}(*args, **kwargs): ...\n"

    if ret and functions:
        ret += "\n"

    for name in sorted(methods):
        if name.startswith("_"):
            continue
        ret += f"def {name}(self, *args, **kwargs): ...\n"

    if ret and methods:
        ret += "\n"

    for name, obj in sorted(classes.items()):
        (classret, needed_namespaces) = _gi_build_stub(obj,
                                                       current_namespace,
                                                       find_methods(obj),
                                                       needed_namespaces,
                                                       True)

        parents: list[str] = []
        if hasattr(obj, "__info__"):
            object_info = obj.__info__ # type: ignore

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

        if not classret:
            ret += f"class {name}{string_parents}: ...\n"
        else:
            ret += f"class {name}{string_parents}:\n"

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
    for obj in mro[1:]:
        name = get_gname(obj)
        if name == main_name:
            continue
        other_attrs.update(dir(obj))

    obj_attrs = all_attrs - other_attrs
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
