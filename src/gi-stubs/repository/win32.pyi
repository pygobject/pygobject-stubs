import typing

from gi.repository import GObject

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "win32"
_version: str = "1.0"

class MSG(GObject.GPointer): ...
