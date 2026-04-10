from typing import Final
from typing import TypeVar

from enum import IntEnum
from enum import IntFlag

from gi.repository import GObject

T = TypeVar("T")

MODULE_IMPL_AR: Final[int]
MODULE_IMPL_DL: Final[int]
MODULE_IMPL_NONE: Final[int]
MODULE_IMPL_WIN32: Final[int]

def module_build_path(directory: str | None, module_name: str) -> str: ...
def module_error() -> str: ...
def module_error_quark() -> int: ...
def module_supported() -> bool: ...

class Module(GObject.GPointer):
    @staticmethod
    def build_path(directory: str | None, module_name: str) -> str: ...
    def close(self) -> bool: ...
    @staticmethod
    def error() -> str: ...
    @staticmethod
    def error_quark() -> int: ...
    def make_resident(self) -> None: ...
    def name(self) -> str: ...
    @staticmethod
    def supported() -> bool: ...
    def symbol(self, symbol_name: str) -> tuple[bool, None]: ...

class ModuleFlags(IntFlag):
    LAZY = 1
    LOCAL = 2
    MASK = 3

class ModuleError(IntEnum):
    CHECK_FAILED = 1
    FAILED = 0
