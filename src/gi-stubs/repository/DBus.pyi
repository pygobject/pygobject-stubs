import typing

from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

class Connection(GObject.GPointer): ...
class Error(GObject.GPointer): ...
class Message(GObject.GPointer): ...
class MessageIter(GObject.GPointer): ...
class PendingCall(GObject.GPointer): ...

class BusType(GObject.GEnum):
    SESSION = 0
    STARTER = 2
    SYSTEM = 1
