from typing import cast

import os
import re
import sys
import xml.etree.ElementTree as ET

import gi
from gi.repository import GLib

NS = {
    "core": "http://www.gtk.org/introspection/core/1.0",
    "c": "http://www.gtk.org/introspection/c/1.0",
    "glib": "http://www.gtk.org/introspection/glib/1.0",
}


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


def _docs(
    root: ET.Element,
    parent_map: dict[ET.Element, ET.Element],
    tag: str,
    remove_newlines=False,
) -> dict[str, str]:
    docs: dict[str, str] = {}

    for child in root.iterfind(f".//core:{tag}", NS):
        parents: list[str] = []
        parent = parent_map[child]
        while parent:
            try:
                if "virtual-method" in parent.tag:
                    parents.insert(0, "do_" + parent.attrib["name"])
                else:
                    parents.insert(0, parent.attrib["name"])
                if "signal" in parent.tag:
                    parents.insert(0, "$signal")
                if "property" in parent.tag:
                    parents.insert(0, "$property")
            except KeyError:
                if "return-value" in parent.tag:
                    parents.insert(0, "$return-value")
            parent = parent_map.get(parent, None)
        text = cast(str, child.text).replace('"', '\\"')
        if remove_newlines:
            text = text.replace("\n", " ")
        text = re.sub(" +", " ", text)
        text = re.sub("\n ", "\n", text)
        docs[".".join(parents[1:])] = text
    return docs


def load_gir(module: str, version: str) -> tuple[dict[str, str], dict[str, str]]:
    gir_tree = ET.parse(_get_gir_path(f"{module}-{version}.gir"))
    gir_root = gir_tree.getroot()
    gir_parent_map = {c: p for p in gir_tree.iter() for c in p}

    return _docs(gir_root, gir_parent_map, "doc"), _docs(
        gir_root, gir_parent_map, "doc-deprecated", True
    )
