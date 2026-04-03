from typing import TypeVar

from gi.repository import GObject

T = TypeVar("T")

class MSG(GObject.GPointer): ...
