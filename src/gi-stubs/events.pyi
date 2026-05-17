from typing_extensions import Self
from typing_extensions import TypeVar
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

import asyncio
import sys
from collections.abc import Callable
from collections.abc import Generator
from contextlib import contextmanager
from types import TracebackType

from gi.repository import GLib

if sys.version_info >= (3, 14):
    from asyncio.events import _AbstractEventLoopPolicy
else:
    from asyncio.events import AbstractEventLoopPolicy as _AbstractEventLoopPolicy

_T_co = TypeVar("_T_co", covariant=True)
_Ts = TypeVarTuple("_Ts")

class GLibTask(asyncio.Task[_T_co]):
    def set_priority(self, priority: int) -> None: ...
    def get_priority(self) -> int: ...

class _GLibEventLoopMixin:
    def __init__(self, main_context: GLib.MainContext | None) -> None: ...
    @contextmanager
    def paused(self) -> Generator[None]: ...
    @contextmanager
    def running(self, quit_func: Callable[[], object]) -> Generator[None]: ...
    def stop(self) -> None: ...
    def time(self) -> float: ...

class _GLibEventLoopRunMixin:
    def run_forever(self) -> None: ...

if sys.platform == "win32":
    class GLibEventLoop(
        _GLibEventLoopMixin, _GLibEventLoopRunMixin, asyncio.ProactorEventLoop
    ):
        def __init__(self, main_context: GLib.MainContext | None = None) -> None: ...

else:
    class GLibEventLoop(
        _GLibEventLoopMixin, _GLibEventLoopRunMixin, asyncio.SelectorEventLoop
    ):
        def __init__(self, main_context: GLib.MainContext | None = None) -> None: ...
        def add_signal_handler(
            self,
            sig: int,
            callback: Callable[[Unpack[_Ts]], object],
            *args: Unpack[_Ts],
        ) -> None: ...
        def remove_signal_handler(self, sig: int) -> bool: ...
        def close(self) -> None: ...

class GLibEventLoopPolicy(_AbstractEventLoopPolicy):
    def __init__(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def get_event_loop(self) -> GLibEventLoop: ...
    def get_event_loop_for_context(self, ctx: GLib.MainContext) -> GLibEventLoop: ...
    def set_event_loop(self, loop: asyncio.AbstractEventLoop | None) -> None: ...
    def new_event_loop(self) -> GLibEventLoop: ...

    if sys.platform != "win32" and sys.version_info < (3, 12):
        def get_child_watcher(self) -> asyncio.AbstractChildWatcher: ...
