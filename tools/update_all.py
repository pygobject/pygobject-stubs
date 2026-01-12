#!/usr/bin/env python3

import typing

import argparse
import subprocess
import sys
from pathlib import Path


class Lib:
    name: str
    version: str
    output: str
    init: str

    def __init__(
        self, name: str, version: str, *, output: str | None = None, init: str = ""
    ) -> None:
        self.name = name
        self.version = version
        self.output = output or name
        self.init = init


GST_INIT = (
    'gi.require_version("Gst", "1.0"); from gi.repository import Gst; Gst.init(None)'
)


# Add libraries below. When multiple versions are available, specify the output argument.
libraries = [
    Lib("Adw", "1"),
    Lib("AppIndicator3", "0.1"),
    Lib("AppStream", "1.0"),
    Lib("Atk", "1.0"),
    Lib("AyatanaAppIndicator3", "0.1"),
    Lib("Farstream", "0.2"),
    Lib("Flatpak", "1.0"),
    Lib("Gdk", "3.0", output="_Gdk3"),
    Lib("Gdk", "4.0", output="_Gdk4"),
    Lib("GdkPixbuf", "2.0"),
    Lib("GdkWin32", "3.0", output="_GdkWin323"),
    Lib("GdkWin32", "4.0", output="_GdkWin324"),
    Lib("GdkX11", "4.0"),
    Lib("Geoclue", "2.0"),
    Lib("GExiv2", "0.10"),
    Lib("Ggit", "1.0"),
    Lib("Gio", "2.0"),
    # This only works for either version at a time
    # Lib("GIRepository", "2.0", output="_GIRepository2"),
    Lib("GIRepository", "3.0", output="_GIRepository3"),
    Lib("GioWin32", "2.0"),
    Lib("GLib", "2.0"),
    Lib("GLibWin32", "2.0"),
    Lib("Gly", "2"),
    Lib("GlyGtk4", "2"),
    Lib("GModule", "2.0"),
    Lib("Goa", "1.0"),
    Lib("GObject", "2.0"),
    Lib("Graphene", "1.0"),
    Lib("Gsk", "4.0"),
    Lib("GSound", "1.0"),
    Lib("Gspell", "1"),
    Lib("Gst", "1.0", init=GST_INIT),
    Lib("GstBase", "1.0", init=GST_INIT),
    Lib("GstRtsp", "1.0", init=GST_INIT),
    Lib("GstRtp", "1.0", init=GST_INIT),
    Lib("GstRtspServer", "1.0", init=GST_INIT),
    Lib("GstPbutils", "1.0", init=GST_INIT),
    Lib("GstSdp", "1.0", init=GST_INIT),
    Lib("GstWebRTC", "1.0", init=GST_INIT),
    Lib("GstAudio", "1.0", init=GST_INIT),
    Lib("GstVideo", "1.0", init=GST_INIT),
    Lib("GstApp", "1.0", init=GST_INIT),
    Lib("Gtk", "3.0", output="_Gtk3"),
    Lib("Gtk", "4.0", output="_Gtk4"),
    Lib("GtkSource", "4", output="_GtkSource4"),
    Lib("GtkSource", "5", output="_GtkSource5"),
    Lib("Handy", "1"),
    Lib("JavaScriptCore", "6.0", output="_JavaScriptCore6"),
    Lib("Manette", "0.2"),
    Lib("Notify", "0.7"),
    Lib("OSTree", "1.0"),
    Lib("Panel", "1"),
    Lib("Pango", "1.0"),
    Lib("PangoCairo", "1.0"),
    Lib("Poppler", "0.18"),
    Lib("Rsvg", "2.0"),
    Lib("Secret", "1"),
    Lib("Shumate", "1.0"),
    Lib("Soup", "2.4", output="_Soup2"),
    Lib("Soup", "3.0", output="_Soup3"),
    Lib("Spelling", "1"),
    Lib("Vte", "2.91"),
    Lib("WebKit", "6.0", output="_WebKit6"),
    Lib("XApp", "1.0"),
    Lib("Xdp", "1.0"),
    Lib("win32", "1.0"),
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update stubs")
    parser.add_argument(
        "--only",
        type=str,
        help="Update only modules with the given name prefixes, comma-separated",
    )

    args = parser.parse_args()

    repo_path = Path("src/gi-stubs/repository")
    failed_generations = []

    only = args.only.split(",") if args.only else []
    only = [prefix.strip() for prefix in only]

    for lib in libraries:
        if only and not any(lib.name.startswith(prefix) for prefix in only):
            continue

        output_path = repo_path / f"{lib.output}.pyi"

        print(f"Generating {output_path}", file=sys.stderr)
        cmd: typing.List[str | Path] = [
            "tools/generate.py",
            lib.name,
            lib.version,
            "-u",
            output_path,
        ]
        if lib.init:
            cmd += ["--init", lib.init]
        gen_process = subprocess.run(cmd)

        if gen_process.returncode == 0:
            print(f"Formatting {output_path}", file=sys.stderr)
            subprocess.run(["ruff", "format", output_path])
            print(f"Sorting imports in {output_path}", file=sys.stderr)
            subprocess.run(["isort", output_path])
        else:
            print(f"Failed to generate {output_path}", file=sys.stderr)
            failed_generations.append(output_path)

    if failed_generations:
        print("Generating the following stubs failed:", file=sys.stderr)
        print(
            "\n".join(f"  - {path}" for path in failed_generations),
            file=sys.stderr,
        )
        sys.exit(1)
