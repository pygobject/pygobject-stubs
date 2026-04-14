from typing import Any
from typing import Final
from typing import TypeVar

from collections.abc import Callable
from collections.abc import Sequence
from enum import IntEnum

import cairo
from gi import _gi
from gi.repository import Gio
from gi.repository import GObject

T = TypeVar("T")
_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

HAVE_CSS: Final = True
HAVE_PIXBUF: Final[int]
HAVE_SVGZ: Final = True
MAJOR_VERSION: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]
VERSION: Final = "2.61.0"

def cleanup() -> None: ...
def error_quark() -> int: ...
def init() -> None: ...
def set_default_dpi(dpi: float) -> None: ...
def set_default_dpi_x_y(dpi_x: float, dpi_y: float) -> None: ...
def term() -> None: ...

class DimensionData(_gi.Struct):
    """
    :Constructors:

    ::

        DimensionData()
    """

    width: int
    height: int
    em: float
    ex: float

class Handle(GObject.Object):
    """
    :Constructors:

    ::

        Handle(**properties)
        new() -> Rsvg.Handle
        new_from_data(data:list) -> Rsvg.Handle or None
        new_from_file(filename:str) -> Rsvg.Handle or None
        new_from_gfile_sync(file:Gio.File, flags:Rsvg.HandleFlags, cancellable:Gio.Cancellable=None) -> Rsvg.Handle or None
        new_from_stream_sync(input_stream:Gio.InputStream, base_file:Gio.File=None, flags:Rsvg.HandleFlags, cancellable:Gio.Cancellable=None) -> Rsvg.Handle or None
        new_with_flags(flags:Rsvg.HandleFlags) -> Rsvg.Handle

    Object RsvgHandle

    Properties from RsvgHandle:
      dpi-x -> gdouble: dpi-x
      dpi-y -> gdouble: dpi-y
      flags -> RsvgHandleFlags: flags
      base-uri -> gchararray: base-uri
      width -> gint: width
      height -> gint: height
      em -> gdouble: em
      ex -> gdouble: ex
      title -> gchararray: title
      desc -> gchararray: desc
      metadata -> gchararray: metadata

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        base_uri: str
        desc: str | None
        dpi_x: float
        dpi_y: float
        em: float
        ex: float
        flags: HandleFlags
        height: int
        metadata: str | None
        title: str | None
        width: int

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    def __init__(
        self,
        *,
        base_uri: str = ...,
        dpi_x: float = ...,
        dpi_y: float = ...,
        flags: HandleFlags = ...,
    ) -> None: ...
    def close(self) -> bool: ...
    def free(self) -> None: ...
    def get_base_uri(self) -> str: ...
    def get_desc(self) -> str | None: ...
    def get_dimensions(self) -> DimensionData: ...
    def get_dimensions_sub(
        self, id: str | None = None
    ) -> tuple[bool, DimensionData]: ...
    def get_geometry_for_element(
        self, id: str | None = None
    ) -> tuple[bool, Rectangle, Rectangle]: ...
    def get_geometry_for_layer(
        self, id: str | None, viewport: Rectangle
    ) -> tuple[bool, Rectangle, Rectangle]: ...
    def get_intrinsic_dimensions(
        self,
    ) -> tuple[bool, Length, bool, Length, bool, Rectangle]: ...
    def get_intrinsic_size_in_pixels(self) -> tuple[bool, float, float]: ...
    def get_metadata(self) -> str | None: ...
    def get_position_sub(self, id: str | None = None) -> tuple[bool, PositionData]: ...
    def get_title(self) -> str | None: ...
    def has_sub(self, id: str) -> bool: ...
    def internal_set_testing(self, testing: bool) -> None: ...
    @classmethod
    def new(cls) -> Handle: ...
    @classmethod
    def new_from_data(cls, data: Sequence[int]) -> Handle | None: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Handle | None: ...
    @classmethod
    def new_from_gfile_sync(
        cls,
        file: Gio.File,
        flags: HandleFlags,
        cancellable: Gio.Cancellable | None = None,
    ) -> Handle | None: ...
    @classmethod
    def new_from_stream_sync(
        cls,
        input_stream: Gio.InputStream,
        base_file: Gio.File | None,
        flags: HandleFlags,
        cancellable: Gio.Cancellable | None = None,
    ) -> Handle | None: ...
    @classmethod
    def new_with_flags(cls, flags: HandleFlags) -> Handle: ...
    def read_stream_sync(
        self, stream: Gio.InputStream, cancellable: Gio.Cancellable | None = None
    ) -> bool: ...
    def render_cairo(self, cr: cairo.Context[_SomeSurface]) -> bool: ...
    def render_cairo_sub(
        self, cr: cairo.Context[_SomeSurface], id: str | None = None
    ) -> bool: ...
    def render_document(
        self, cr: cairo.Context[_SomeSurface], viewport: Rectangle
    ) -> bool: ...
    def render_element(
        self,
        cr: cairo.Context[_SomeSurface],
        id: str | None,
        element_viewport: Rectangle,
    ) -> bool: ...
    def render_layer(
        self, cr: cairo.Context[_SomeSurface], id: str | None, viewport: Rectangle
    ) -> bool: ...
    def set_base_gfile(self, base_file: Gio.File) -> None: ...
    def set_base_uri(self, base_uri: str) -> None: ...
    def set_cancellable_for_rendering(
        self, cancellable: Gio.Cancellable | None = None
    ) -> None: ...
    def set_dpi(self, dpi: float) -> None: ...
    def set_dpi_x_y(self, dpi_x: float, dpi_y: float) -> None: ...
    def set_size_callback(
        self, size_func: Callable[..., tuple[int, int]] | None = None, *user_data: Any
    ) -> None: ...
    def set_stylesheet(self, css: Sequence[int]) -> bool: ...
    def write(self, buf: Sequence[int]) -> bool: ...

class HandleClass(_gi.Struct):
    """
    :Constructors:

    ::

        HandleClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...

class Length(_gi.Struct):
    """
    :Constructors:

    ::

        Length()
    """

    length: float
    unit: Unit

class PositionData(_gi.Struct):
    """
    :Constructors:

    ::

        PositionData()
    """

    x: int
    y: int

class Rectangle(_gi.Struct):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: float
    y: float
    width: float
    height: float

class HandleFlags(GObject.GFlags):
    FLAGS_NONE = 0
    FLAG_KEEP_IMAGE_DATA = 2
    FLAG_UNLIMITED = 1

class Error(GObject.GEnum):
    FAILED = 0
    @staticmethod
    def quark() -> int: ...

class Unit(IntEnum):
    CH = 9
    CM = 5
    EM = 2
    EX = 3
    IN = 4
    MM = 6
    PC = 8
    PERCENT = 0
    PT = 7
    PX = 1
