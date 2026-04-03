from typing import Any
from typing import TypeVar

from collections.abc import Callable
from collections.abc import Sequence
from enum import IntEnum

from gi.repository import GLib
from gi.repository import GObject

T = TypeVar("T")

def closefrom(lowfd: int) -> int: ...
def error_quark() -> int: ...
def fd_add_full(
    priority: int,
    fd: int,
    condition: GLib.IOCondition,
    function: Callable[..., bool],
    *user_data: Any,
) -> int: ...
def fd_query_path(fd: int) -> str: ...
def fd_source_new(fd: int, condition: GLib.IOCondition) -> GLib.Source: ...
def fdwalk_set_cloexec(lowfd: int) -> int: ...
def get_passwd_entry(user_name: str) -> None: ...
def open_pipe(fds: Sequence[int], flags: int) -> bool: ...
def set_fd_nonblocking(fd: int, nonblock: bool) -> bool: ...
def signal_add(
    priority: int, signum: int, handler: Callable[..., bool], *user_data: Any
) -> int: ...
def signal_add_full(
    priority: int, signum: int, handler: Callable[..., bool], *user_data: Any
) -> int: ...
def signal_source_new(signum: int) -> GLib.Source: ...

class Pipe(GObject.GPointer):
    """
    :Constructors:

    ::

        Pipe()
    """

    fds: list[int]

class PipeEnd(IntEnum):
    READ = 0
    WRITE = 1
