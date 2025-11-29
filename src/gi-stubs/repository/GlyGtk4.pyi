import typing

from gi.repository import Gdk
from gi.repository import Gly

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "GlyGtk4"
_version: str = "2"

def frame_get_texture(frame: Gly.Frame) -> Gdk.Texture: ...
