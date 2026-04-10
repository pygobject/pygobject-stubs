from typing import TypeVar

from gi.repository import _Gtk4
from gi.repository import Xdp

T = TypeVar("T")

def parent_new_gtk(window: _Gtk4.Window) -> Xdp.Parent: ...
