from typing import Any
from typing import overload
from typing import Self
from typing import TypeVar

import os
from collections.abc import Callable

from gi.repository import _Gtk4
from gi.repository import GObject

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])

class _BuilderScope(GObject.GObject, _Gtk4.BuilderScope):
    """
    Object gi+_gtktemplate+BuilderScope

    Signals from GObject:
        notify (GParam)
    """
    def do_create_closure(
        self,
        builder: _Gtk4.Builder,
        func_name: str,
        flags: _Gtk4.BuilderClosureFlags,
        obj: object,
    ) -> GObject.Closure: ...

class Template:
    @overload
    def __init__(
        self,
        *,
        filename: str | os.PathLike[str],
        resource_path: str = ...,
        string: str | bytes = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        filename: str | os.PathLike[str] = ...,
        resource_path: str,
        string: str | bytes = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *,
        filename: str | os.PathLike[str] = ...,
        resource_path: str = ...,
        string: str | bytes,
    ) -> None: ...
    @classmethod
    def from_file(cls, filename: str | os.PathLike[str]) -> Self: ...
    @classmethod
    def from_resource(cls, resource_path: str) -> Self: ...
    @classmethod
    def from_string(cls, string: str | bytes) -> Self: ...
    def __call__(self, cls: _T) -> _T: ...

    class Callback:
        def __init__(self, name: str | None = ...) -> None: ...
        def __call__(self, func: _F) -> _F: ...

    @classmethod
    def Child(cls: Any, name: str | None = ...) -> Any: ...
