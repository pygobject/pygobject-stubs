from __future__ import annotations

from typing import TYPE_CHECKING

import argparse
import importlib
import pprint
import subprocess
import sys
from pathlib import Path

import gi

from .parse import Imports
from .parse import Overrides
from .parse import parse
from .parse import TypeVars
from .stub import Stub

gi.require_version("GIRepository", "3.0")

if TYPE_CHECKING:
    from gi.repository import _GIRepository3 as GIRepository
else:
    from gi.repository import GIRepository


def _build(
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
    parser = argparse.ArgumentParser(
        prog="pygobject_stub_generator", description="Generate module stubs"
    )
    parser.add_argument("module", type=str, help="Gdk, Gtk, ...")
    parser.add_argument("version", type=str, help="3.0, 4.0, ...")
    parser.add_argument(
        "-u", dest="update", type=Path, help="Stub file to update e.g. -u Gdk.pyi"
    )
    parser.add_argument(
        "--init",
        type=str,
        help="Initialization code that must be evaluated first e.g. "
        '\'gi.require_version("Gst", "1.0"); from gi.repository import Gst; '
        "Gst.init(None)'",
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

        output = _build(
            args.module, args.version, args.init, overrides, imports, typevars
        )

        print("Running with these overrides:")
        pprint.pprint(overrides)

        output = _format(output, args.format, file=update_file)
        update_file.write_text(output)
    else:
        print(
            _format(
                _build(args.module, args.version, args.init, {}, [], []), args.format
            )
        )
