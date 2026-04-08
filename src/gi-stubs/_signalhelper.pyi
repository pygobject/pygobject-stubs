from typing import Any
from typing import Literal
from typing import overload
from typing_extensions import Self

from collections.abc import Callable
from collections.abc import Sequence

from . import _gi

class Signal(str):
    class BoundSignal(str):
        def __init__(self, signal: Signal, gobj: _gi.GObject): ...
        def __call__(self, *args: object, **kargs: object) -> Any: ...
        def connect(
            self, callback: Callable[..., Any], *args: object, **kargs: object
        ) -> int: ...
        def connect_detailed(
            self,
            callback: Callable[..., Any],
            detail: str,
            *args: object,
            **kargs: object,
        ) -> int: ...
        def disconnect(self, handler_id: int) -> None: ...
        def emit(self, *args: object, **kargs: object) -> Any: ...

    def __init__(
        self,
        name: Callable[..., Any] | str = "",
        func: Callable[..., Any] | None = None,
        flags: int = _gi.SIGNAL_RUN_FIRST,
        return_type: type[Any] | None = None,
        arg_types: Sequence[type[Any]] | None = None,
        doc: str = "",
        accumulator: Callable[..., Any] | None = None,
        accu_data: object | None = None,
    ): ...
    @overload
    def __get__(self, instance: None, owner: Any = ...) -> Self: ...
    @overload
    def __get__(self, instance: object, owner: Any = ...) -> BoundSignal: ...
    def __call__(self, obj: object, *args: object, **kargs: object) -> Any: ...
    def copy(self, newName: str | None = None) -> Self: ...
    def get_signal_args(
        self,
    ) -> tuple[
        int, type[Any], Sequence[type[Any]], Callable[..., Any] | None, object | None
    ]: ...

class SignalOverride(Signal):
    def get_signal_args(self) -> Literal["override"]: ...
