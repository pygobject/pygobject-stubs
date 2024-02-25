from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

try:
    from warnings import deprecated
except ImportError:
    from typing_extensions import deprecated

from gi.repository import GObject

_lock = ...  # FIXME Constant
_namespace: str = "GModule"
_version: str = "2.0"

@deprecated(
    "Use g_module_open() instead with @module_name as the basename of the file_name argument. See %G_MODULE_SUFFIX for why."
)
def module_build_path(directory: Optional[str], module_name: str) -> str: ...
def module_error() -> str: ...
def module_error_quark() -> int: ...
def module_supported() -> bool: ...

class Module(GObject.GPointer):
    @deprecated(
        "Use g_module_open() instead with @module_name as the basename of the file_name argument. See %G_MODULE_SUFFIX for why."
    )
    @staticmethod
    def build_path(directory: Optional[str], module_name: str) -> str: ...
    def close(self) -> bool: ...
    @staticmethod
    def error() -> str: ...
    @staticmethod
    def error_quark() -> int: ...
    def make_resident(self) -> None: ...
    def name(self) -> str: ...
    @staticmethod
    def supported() -> bool: ...
    def symbol(self, symbol_name: str) -> Tuple[bool, None]: ...

class ModuleFlags(GObject.GFlags):
    LAZY = 1
    LOCAL = 2
    MASK = 3

class ModuleError(GObject.GEnum):
    CHECK_FAILED = 1
    FAILED = 0
