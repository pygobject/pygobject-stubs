from typing import List

import os
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py


def _get_lib_config() -> List[str]:
    libs = []
    env_var = os.environ.get("PYGOBJECT_STUB_CONFIG")
    if env_var is not None:
        libs = [lib.strip() for lib in env_var.split(",")]
    return libs


class build(build_py):
    def _copy_multi_version_stubs(self) -> None:
        package_dir = Path(self.build_lib) / "gi-stubs"
        src_dir = package_dir / "__multi_version_stubs"
        dst_dir = package_dir / "repository"

        for lib in _get_lib_config():
            lib_wo_version = lib[:-1]
            src = src_dir / f"{lib}.pyi"
            dst = dst_dir / f"{lib_wo_version}.pyi"
            if dst.exists():
                dst.unlink()
            self.copy_file(str(src), str(dst))

    def run(self) -> None:
        build_py.run(self)
        self._copy_multi_version_stubs()


setup(
    cmdclass={
        "build_py": build,
    },
)
