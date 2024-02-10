from typing import cast

import os
import re
import sys
import xml.etree.ElementTree as ET

import gi
from gi.repository import GLib


def _get_gir_path(girname: str) -> str:
    searchdirs: list[str] = []

    from_env = os.getenv("GI_GIR_PATH", "")
    if from_env:
        searchdirs.extend(from_env.split(os.pathsep))

    user_data_dir = GLib.get_user_data_dir()
    if user_data_dir is not None:
        searchdirs.append(os.path.join(user_data_dir, "gir-1.0"))

    for path in GLib.get_system_data_dirs():
        searchdirs.append(os.path.join(path, "gir-1.0"))

    if os.name != "nt":
        # For backwards compatibility, was always unconditionally added to the list.
        searchdirs.append("/usr/share/gir-1.0")

    for d in searchdirs:
        path = os.path.join(d, girname)
        if os.path.exists(path):
            return path

    sys.stderr.write(f"Couldn't find '{girname}' (search path: '{searchdirs}')\n")
    sys.exit(1)


def load_gir(module: str, version: str) -> dict[str, str]:
    deprecation_docs: dict[str, str] = {}
    ns = {
        "core": "http://www.gtk.org/introspection/core/1.0",
        "c": "http://www.gtk.org/introspection/c/1.0",
        "glib": "http://www.gtk.org/introspection/glib/1.0",
    }
    gir_tree = ET.parse(_get_gir_path(f"{module}-{version}.gir"))
    gir_root = gir_tree.getroot()
    gir_parent_map = {c: p for p in gir_tree.iter() for c in p}

    for child in gir_root.iterfind(".//core:doc-deprecated", ns):
        parents: list[str] = []
        parent = gir_parent_map[child]
        while True:
            try:
                parents.insert(0, parent.attrib["name"])
            except KeyError:
                break
            parent = gir_parent_map[parent]
        deprecation_docs[".".join(parents[1:])] = re.sub(
            " +", " ", cast(str, child.text).replace("\n", " ").replace('"', '\\"')
        )

    return deprecation_docs
