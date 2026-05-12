from typing_extensions import Unpack

from collections.abc import Callable
from enum import IntEnum

from gi import _gi
from gi.repository import GLib

_DataTs = TypeVarTuple("_DataTs", default=Unpack[tuple[()]])

def closefrom(lowfd: int) -> int: ...
def error_quark() -> int: ...
def fd_add_full(
    priority: int,
    fd: int,
    condition: GLib._IOConditionValueType,
    function: Callable[[int, GLib._IOConditionValueType, Unpack[_DataTs]], bool],
    *user_data: Unpack[_DataTs],
) -> int: ...
def fd_source_new(fd: int, condition: GLib._IOConditionValueType) -> GLib.Source: ...
def fdwalk_set_cloexec(lowfd: int) -> int: ...
def get_passwd_entry(user_name: str) -> int: ...
def open_pipe(fds: int, flags: int) -> bool: ...
def set_fd_nonblocking(fd: int, nonblock: bool) -> bool: ...
def signal_add_full(
    priority: int,
    signum: int,
    handler: Callable[[Unpack[_DataTs]], bool],
    *user_data: Unpack[_DataTs],
) -> int: ...
def signal_source_new(signum: int) -> GLib.Source: ...

class Pipe(_gi.Struct):
    """
    :Constructors:

    ::

        Pipe()
    """

    fds: list[int]

class PipeEnd(IntEnum):
    READ = 0
    WRITE = 1
