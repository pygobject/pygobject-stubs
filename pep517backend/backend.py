from __future__ import annotations

from typing import Any, Optional

import itertools
import logging
import os
import shutil
from pathlib import Path

import setuptools.build_meta as _orig


logging.basicConfig(level="INFO", format="%(levelname)s: %(message)s")
log = logging.getLogger()

PACKAGE_DIR = Path("src/gi-stubs")
GI_REPOSITORY_DIR = PACKAGE_DIR / "repository"
DEFAULT_STUB_CONFIG = ["Gdk4", "Gtk4", "Soup3"]


def _get_settings_stub_config(config_settings: Optional[dict[str, str]]) -> list[str]:
    libs = []
    if config_settings is None:
        return libs

    config = config_settings.get("config")
    if config is None:
        return libs

    libs = [lib.strip() for lib in config.split(",")]
    log.info("Settings stub config: %s", libs)
    return libs


def _get_env_stub_config() -> list[str]:
    libs = []
    env_var = os.environ.get("PYGOBJECT_STUB_CONFIG")
    if env_var is not None:
        libs = [lib.strip() for lib in env_var.split(",")]
    log.info("Env stub config: %s", libs)
    return libs


def _check_config(stub_config: list[str]) -> None:
    for lib in stub_config:
        stub_path = GI_REPOSITORY_DIR / f"_{lib}.pyi"
        if not stub_path.exists():
            raise ValueError(f"Unknown library {lib}")


def _install_stubs(stub_config: list[str]) -> None:
    for lib in itertools.chain(stub_config, DEFAULT_STUB_CONFIG):
        stub_path = GI_REPOSITORY_DIR / f"_{lib}.pyi"
        new_stub_path = GI_REPOSITORY_DIR / f"{lib[:-1]}.pyi"
        if not new_stub_path.exists():
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
