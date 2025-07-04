#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


class Lib:
    name: str
    version: str
    output: str

    def __init__(self, name: str, version: str, *, output: str | None = None) -> None:
        self.name = name
        self.version = version
        self.output = output or name


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
    Lib("GioWin32", "2.0"),
    Lib("GLib", "2.0"),
    Lib("GLibWin32", "2.0"),
    Lib("GModule", "2.0"),
    Lib("Goa", "1.0"),
    Lib("GObject", "2.0"),
    Lib("Graphene", "1.0"),
    Lib("Gsk", "4.0"),
    Lib("GSound", "1.0"),
    Lib("Gspell", "1"),
    Lib("Gst", "1.0"),
    Lib("GstBase", "1.0"),
    Lib("GstRtsp", "1.0"),
    Lib("GstRtp", "1.0"),
    Lib("GstRtspServer", "1.0"),
    Lib("GstPbutils", "1.0"),
    Lib("GstSdp", "1.0"),
    Lib("GstWebRTC", "1.0"),
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
]

if __name__ == "__main__":
    repo_path = Path("src/gi-stubs/repository")
    failed_generations = []

    for lib in libraries:
        output_path = repo_path / f"{lib.output}.pyi"

        print(f"Generating {output_path}", file=sys.stderr)
        gen_process = subprocess.run(
            ["tools/generate.py", lib.name, lib.version, "-u", output_path],
        )

        if gen_process.returncode == 0:
            print(f"Formatting {output_path}", file=sys.stderr)
            subprocess.run(["black", output_path])
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
