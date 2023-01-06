# Based on https://github.com/PyCQA/astroid/blob/main/astroid/brain/brain_gi.py
# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE

from __future__ import annotations

from typing import Any
from typing import Callable
from typing import Optional
from typing import Type
from typing import Union

import argparse
import importlib
import inspect
import re
from types import ModuleType

import gi
from gi.repository import GObject

_identifier_re = r"^[A-Za-z_]\w*$"

ObjectT = Union[ModuleType, Type[Any]]


def build(parent: ObjectT) -> str:
    return _gi_build_stub(parent, dir(parent))


def _gi_build_stub(parent: ObjectT, children: list[str]) -> str:
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
        ret += f"def {name}(*args, **kwargs): ...\n"

    if ret and functions:
        ret += "\n"

    for name in sorted(methods):
        if name.startswith("_"):
            continue
        ret += f"def {name}(self, *args, **kwargs): ...\n"

    if ret and methods:
        ret += "\n"

    for name, obj in sorted(classes.items()):
        classret = _gi_build_stub(obj, find_methods(obj))
        if not classret:
            ret += f"class {name}: ...\n"
        else:
            ret += f"class {name}:\n"

        for line in classret.splitlines():
            ret += "    " + line + "\n"
        ret += "\n"

    for name, obj in sorted(flags.items()):
        base = "GObject.GFlags"
        ret += f"class {name}({base}):\n"
        for key in sorted(vars(obj)):
            if not key.startswith("__"):
                ret += f"    {key} = ...\n"
        ret += "\n"

    for name, obj in sorted(enums.items()):
        base = "GObject.GEnum"
        ret += f"class {name}({base}):\n"
        for key in sorted(vars(obj)):
            if not key.startswith("__"):
                ret += f"    {key} = ...\n"
        ret += "\n"
    return ret


def is_valid_class(name: str) -> bool:
    if "Accessible" in name:
        return False
    if name.endswith("Private"):
        return False
    if name.endswith("Class"):
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
print(build(module))
