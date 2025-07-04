from __future__ import annotations

from typing import Any
from typing import Optional

import itertools
import logging
import os
import shutil
from dataclasses import dataclass
from pathlib import Path

import setuptools.build_meta as _orig

logging.basicConfig(level="INFO", format="%(levelname)s: %(message)s")
log = logging.getLogger()

PACKAGE_DIR = Path("src/gi-stubs")
GI_REPOSITORY_DIR = PACKAGE_DIR / "repository"


@dataclass
class LibVersion:
    name: str
    version: str

    @classmethod
    def from_str(cls, string: str) -> LibVersion:
        name = string[:-1]
        version = string[-1]
        return cls(name=name, version=version)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, LibVersion):
            return False
        return obj.name == self.name

    def __str__(self) -> str:
        return f"{self.name}{self.version}"


DEFAULT_STUB_CONFIG = [
    LibVersion("Gdk", "4"),
    LibVersion("GdkWin32", "4"),
    LibVersion("GIRepository", "3"),
    LibVersion("Gtk", "4"),
    LibVersion("GtkSource", "5"),
    LibVersion("JavaScriptCore", "6"),
    LibVersion("Soup", "3"),
    LibVersion("WebKit", "6"),
]


def _get_settings_stub_config(
    config_settings: Optional[dict[str, str]],
) -> list[LibVersion]:
    libs = []
    if config_settings is None:
        return libs

    config = config_settings.get("config")
    if config is None:
        return libs

    libs = [lib.strip() for lib in config.split(",")]
    log.info("Settings stub config: %s", libs)
    return list(map(LibVersion.from_str, libs))


def _get_env_stub_config() -> list[LibVersion]:
    libs = []
    env_var = os.environ.get("PYGOBJECT_STUB_CONFIG")
    if env_var is not None:
        libs = [lib.strip() for lib in env_var.split(",")]
    log.info("Env stub config: %s", libs)
    return list(map(LibVersion.from_str, libs))


def _check_config(stub_config: list[LibVersion]) -> None:
    for lib in stub_config:
        stub_path = GI_REPOSITORY_DIR / f"_{lib}.pyi"
        if not stub_path.exists():
            raise ValueError(f"Unknown library {lib}")


def _install_stubs(stub_config: list[LibVersion]) -> None:
    for lib in stub_config:
        if lib in DEFAULT_STUB_CONFIG:
            DEFAULT_STUB_CONFIG.remove(lib)

    for lib in itertools.chain(stub_config, DEFAULT_STUB_CONFIG):
        stub_path = GI_REPOSITORY_DIR / f"_{lib}.pyi"
        new_stub_path = GI_REPOSITORY_DIR / f"{lib.name}.pyi"
        log.info("Install %s", lib)
        shutil.copy(stub_path, new_stub_path)


def get_requires_for_build_sdist(*args: Any, **kwargs: Any) -> str:
    return _orig.get_requires_for_build_sdist(*args, **kwargs)


def build_sdist(*args: Any, **kwargs: Any) -> str:
    return _orig.build_sdist(*args, **kwargs)


def get_requires_for_build_wheel(*args: Any, **kwargs: Any) -> str:
    return _orig.get_requires_for_build_wheel(*args, **kwargs)


def prepare_metadata_for_build_wheel(*args: Any, **kwargs: Any) -> str:
    return _orig.prepare_metadata_for_build_wheel(*args, **kwargs)


def build_wheel(
    wheel_directory: str,
    config_settings: Optional[dict[str, str]] = None,
    metadata_directory: Optional[str] = None,
) -> str:
    stub_config = _get_settings_stub_config(config_settings)
    if not stub_config:
        stub_config = _get_env_stub_config()

    _check_config(stub_config)
    _install_stubs(stub_config)

    basename = _orig.build_wheel(
        wheel_directory,
        config_settings=config_settings,
        metadata_directory=metadata_directory,
    )

    return basename
