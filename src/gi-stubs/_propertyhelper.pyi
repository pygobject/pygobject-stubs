from typing import Any
from typing import Final

from collections.abc import Callable

from . import _gi

G_MAXFLOAT: Final[float]
G_MAXDOUBLE: Final[float]
G_MININT: Final[int]
G_MAXINT: Final[int]
G_MAXUINT: Final[int]
G_MINLONG: Final[int]
G_MAXLONG: Final[int]
G_MAXULONG: Final[int]

class Property:
    def __init__(
        self,
        getter: Callable[[Any], Any] | None = None,
        setter: Callable[[Any, Any], None] | None = None,
        type: type[Any] | None = None,
        default: Any = None,
        nick: str = "",
        blurb: str = "",
        flags: int = _gi.PARAM_READWRITE,
        minimum: float | None = None,
        maximum: float | None = None,
    ) -> None: ...
    def __call__(self, fget: Callable[[Any], Any]) -> Property: ...
    def __get__(self, instance: Any, klass: Any) -> Any: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def get_pspec_args(self) -> tuple[Any, ...]: ...
    def getter(self, fget: Callable[[Any], Any]) -> Property: ...
    def setter(self, fset: Callable[[Any, Any], None]) -> Property: ...

def install_properties(cls: type[Any]) -> None: ...
