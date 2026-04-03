from typing import TypeVar

from gi.repository import _Gdk4
from gi.repository import Gly

T = TypeVar("T")

def frame_get_texture(frame: Gly.Frame) -> _Gdk4.Texture: ...
