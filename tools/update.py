#!/usr/bin/env python3

from __future__ import annotations

from typing import Final
from typing import TYPE_CHECKING

import argparse
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

if TYPE_CHECKING:
    from collections.abc import Collection
    from collections.abc import Container
    from collections.abc import Iterator
    from collections.abc import Sequence


@dataclass(slots=True, frozen=True)
class TypeLib:
    name: str
    version: str
    output: str | None = None
    init: str | None = None
    collections: list[str] = field(default_factory=list, hash=False)

    @property
    def filename(self) -> str:
        return f"{self.output or self.name}.pyi"


_GST_INIT: Final = (
    'gi.require_version("Gst", "1.0"); from gi.repository import Gst; Gst.init(None)'
)


_TYPELIBS: Final = [
    TypeLib("Adw", "1"),
    TypeLib("AppIndicator3", "0.1"),
    TypeLib("AppStream", "1.0"),
    TypeLib("Aravis", "0.8"),
    TypeLib("Atk", "1.0"),
    TypeLib("Atspi", "2.0"),
    TypeLib("AyatanaAppIndicator3", "0.1"),
    TypeLib("DBus", "1.0", collections=["dbus"]),
    TypeLib("DBusGLib", "1.0", collections=["dbus"]),
    TypeLib("ECal", "2.0"),
    TypeLib("EDataServer", "1.2"),
    TypeLib("Farstream", "0.2"),
    TypeLib("Flatpak", "1.0"),
    TypeLib("Gdk", "3.0", output="_Gdk3", collections=["gdk"]),
    TypeLib("Gdk", "4.0", output="_Gdk4", collections=["gdk"]),
    TypeLib("GdkPixbuf", "2.0", collections=["gdk"]),
    TypeLib("GdkMacos", "4.0", output="_GdkMacos4", collections=["gdk"]),
    TypeLib("GdkWin32", "3.0", output="_GdkWin323", collections=["gdk"]),
    TypeLib("GdkWin32", "4.0", output="_GdkWin324", collections=["gdk"]),
    TypeLib("GdkWayland", "4.0", collections=["gdk"]),
    TypeLib("GdkX11", "4.0", collections=["gdk"]),
    TypeLib("Geoclue", "2.0"),
    TypeLib("GExiv2", "0.10"),
    TypeLib("Ggit", "1.0"),
    TypeLib("Gio", "2.0", collections=["gio"]),
    TypeLib("GioUnix", "2.0", collections=["gio"]),
    TypeLib("GioWin32", "2.0", collections=["gio"]),
    # This only works for either version at a time, so not added to the glib collection
    TypeLib("GIRepository", "2.0", output="_GIRepository2"),
    TypeLib(
        "GIRepository",
        "3.0",
        output="_GIRepository3",
        collections=["glib"],
    ),
    TypeLib("GLib", "2.0", collections=["glib"]),
    TypeLib("GLibUnix", "2.0", collections=["glib"]),
    TypeLib("GLibWin32", "2.0", collections=["glib"]),
    TypeLib("Gly", "2"),
    TypeLib("GlyGtk4", "2"),
    TypeLib("GModule", "2.0", collections=["glib"]),
    TypeLib("Goa", "1.0"),
    TypeLib("GObject", "2.0", collections=["glib"]),
    TypeLib("Graphene", "1.0", collections=["gtk"]),
    TypeLib("Gsk", "4.0", collections=["gtk"]),
    TypeLib("GSound", "1.0"),
    TypeLib("Gspell", "1"),
    TypeLib("Gst", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstApp", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstAudio", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstBase", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstPbutils", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstRtsp", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstRtp", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstRtspServer", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstSdp", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstVideo", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("GstWebRTC", "1.0", init=_GST_INIT, collections=["gstreamer"]),
    TypeLib("Gtk", "3.0", output="_Gtk3", collections=["gtk"]),
    TypeLib("Gtk", "4.0", output="_Gtk4", collections=["gtk"]),
    TypeLib("GtkSource", "4", output="_GtkSource4"),
    TypeLib("GtkSource", "5", output="_GtkSource5"),
    TypeLib("Handy", "1"),
    TypeLib("IBus", "1.0"),
    TypeLib("ICalGLib", "3.0"),
    TypeLib("JavaScriptCore", "6.0", output="_JavaScriptCore6", collections=["webkit"]),
    TypeLib("Manette", "0.2"),
    TypeLib("Notify", "0.7"),
    TypeLib("OSTree", "1.0"),
    TypeLib("Panel", "1"),
    TypeLib("Pango", "1.0", collections=["pango"]),
    TypeLib("PangoCairo", "1.0", collections=["pango"]),
    TypeLib("Poppler", "0.18"),
    TypeLib("Rsvg", "2.0"),
    TypeLib("Secret", "1"),
    TypeLib("Shumate", "1.0"),
    TypeLib("Soup", "2.4", output="_Soup2"),
    TypeLib("Soup", "3.0", output="_Soup3"),
    TypeLib("Spelling", "1"),
    TypeLib("Vte", "2.91"),
    TypeLib("WebKit", "6.0", output="_WebKit6", collections=["webkit"]),
    TypeLib("win32", "1.0", collections=["glib"]),
    TypeLib("XApp", "1.0"),
    TypeLib("Xdp", "1.0"),
    TypeLib("XdpGtk4", "1.0"),
]

_SUPER_COLLECTIONS: Final = {
    "gio-all": [
        "gio",
        "glib",
    ],
    "gdk-all": [
        "gdk",
        "pango",
        "gio-all",
    ],
    "gtk-all": [
        "gtk",
        "Rsvg",
        "gdk-all",
    ],
}


def _list_typelibs() -> None:
    for typelib in sorted(_TYPELIBS, key=lambda t: (t.name.lower(), t.version)):
        print(f"{typelib.name} {typelib.version}")


def _list_collections() -> None:
    for collection, typelibs in sorted(_build_collection_mapping().items()):
        print(f"{collection}:")
        for typelib in sorted(typelibs, key=lambda t: (t.name.lower(), t.version)):
            print(f"  - {typelib.name} {typelib.version}")


def _build_collection_mapping() -> dict[str, list[TypeLib]]:
    collections: dict[str, list[TypeLib]] = defaultdict(list)

    for typelib in _TYPELIBS:
        if typelib.collections:
            for collection in typelib.collections:
                collections[collection].append(typelib)

    for super_collection, sub_collections in _SUPER_COLLECTIONS.items():
        for sub_collection in sub_collections:
            if sub_collection in collections:
                collections[super_collection].extend(collections[sub_collection])
            else:
                collections[super_collection].extend(
                    typelib for typelib in _TYPELIBS if sub_collection == typelib.name
                )

    return collections


def _get_typelibs(
    typelib_names: Sequence[str],
    collection_names: Sequence[str],
    exclusions: Container[str],
    collection_exclusions: Collection[str],
    /,
) -> Iterator[TypeLib]:
    typelibs_to_update: set[TypeLib] = {
        typelib
        for typelib in _TYPELIBS
        if typelib.name in typelib_names
        or f"{typelib.name}-{typelib.version}" in typelib_names
    }

    collections: dict[str, list[TypeLib]] = (
        _build_collection_mapping() if collection_names or collection_exclusions else {}
    )

    for collection_name in collection_names:
        if collection_name not in collections:
            print(f"Unknown collection: {collection_name}")
            continue

        typelibs_to_update.update(collections[collection_name])

    if not typelibs_to_update and not typelib_names and not collection_names:
        typelibs_to_update = set(_TYPELIBS)

    for collection_exclusion in collection_exclusions:
        if collection_exclusion not in collections:
            print(f"Unknown collection exclusion: {collection_exclusion}")
            continue

        typelibs_to_update = typelibs_to_update - set(collections[collection_exclusion])

    for typelib in sorted(typelibs_to_update, key=lambda t: (t.name, t.version)):
        if (
            typelib.name not in exclusions
            and f"{typelib.name}-{typelib.version}" not in exclusions
        ):
            yield typelib


def main() -> None:
    parser = argparse.ArgumentParser(description="Update stubs")
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Update all stubs.",
    )
    parser.add_argument(
        "-l",
        "--list-typelibs",
        action="store_true",
        help="List all available typelibs.",
    )
    parser.add_argument(
        "-L",
        "--list-collections",
        action="store_true",
        help="List all available collections and the typelibs they include.",
    )
    parser.add_argument(
        "-t",
        "--typelib",
        type=str,
        action="append",
        default=[],
        help="Update only modules with the given typelib name and optional version, "
        "e.g. Gdk or Gdk-3.0. Can be specified multiple times.",
    )
    parser.add_argument(
        "-x",
        "--exclude",
        type=str,
        action="append",
        default=[],
        help="Exclude modules with the given typelib name and optional version, "
        "e.g. Gdk or Gdk-3.0. Can be specified multiple times.",
    )
    parser.add_argument(
        "-c",
        "--collection",
        type=str,
        action="append",
        default=[],
        help="Update all modules in the given collection, e.g. gdk or gtk-all. Can be "
        "specified multiple times.",
    )
    parser.add_argument(
        "-e",
        "--exclude-collection",
        type=str,
        action="append",
        default=[],
        help="Exclude all modules in the given collection, e.g. gdk or gtk-all. Can be "
        "specified multiple times.",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    if args.list_typelibs:
        _list_typelibs()
        return

    if args.list_collections:
        _list_collections()
        return

    repo_path = Path(__file__).parent.parent / "src/gi-stubs/repository"
    failed_generations: list[Path] = []
    failed_formatting: list[Path] = []

    if args.all:
        args.typelib = [f"{typelib.name}-{typelib.version}" for typelib in _TYPELIBS]
        args.collection = []

    for typelib in _get_typelibs(
        args.typelib, args.collection, set(args.exclude), set(args.exclude_collection)
    ):
        print(f"Updating {typelib.name} {typelib.version}")

        output_path = repo_path / typelib.filename
        cmd: list[str | Path] = [
            "python3",
            "-m",
            "pygobject_stub_generator",
            typelib.name,
            typelib.version,
            "-u",
            output_path,
            "--format",
            "ruff check --select=I001 --select=F401 --stdin-filename %FILENAME% --fix -",  # noqa: E501
            "--format",
            "ruff format --stdin-filename %FILENAME% -",
        ]
        if typelib.init:
            cmd += ["--init", typelib.init]

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as error:
            if error.returncode == 2:
                print(f"Formatting failed for {output_path}", file=sys.stderr)
                failed_formatting.append(output_path)
            else:
                print(f"Failed to generate {output_path}", file=sys.stderr)
                failed_generations.append(output_path)

    if failed_generations:
        print("Generating the following stubs failed:", file=sys.stderr)
        print(
            "\n".join(f"  - {path}" for path in failed_generations),
            file=sys.stderr,
        )

    if failed_formatting:
        print("Formatting the following stubs failed:", file=sys.stderr)
        print(
            "\n".join(f"  - {path}" for path in failed_formatting),
            file=sys.stderr,
        )

    if failed_generations:
        sys.exit(1)
    elif failed_formatting:
        sys.exit(2)


if __name__ == "__main__":
    main()
