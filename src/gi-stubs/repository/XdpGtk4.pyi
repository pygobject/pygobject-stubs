from typing import TypeVar

from gi.repository import Gtk
from gi.repository import Xdp

T = TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "XdpGtk4"
_version: str = "1.0"

def parent_new_gtk(window: Gtk.Window) -> Xdp.Parent: ...
