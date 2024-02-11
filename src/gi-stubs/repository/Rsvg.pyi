from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GObject

MAJOR_VERSION: int = 2
MICRO_VERSION: int = 1
MINOR_VERSION: int = 57
VERSION: str = "2.57.1"
_lock = ...  # FIXME Constant
_namespace: str = "Rsvg"
_version: str = "2.0"

def cleanup() -> None: ...
def error_quark() -> int: ...
def init() -> None: ...
def pixbuf_from_file(filename: str) -> Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_max_size(
    filename: str, max_width: int, max_height: int
) -> Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_size(
    filename: str, width: int, height: int
) -> Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_zoom(
    filename: str, x_zoom: float, y_zoom: float
) -> Optional[GdkPixbuf.Pixbuf]: ...
def pixbuf_from_file_at_zoom_with_max(
    filename: str, x_zoom: float, y_zoom: float, max_width: int, max_height: int
) -> Optional[GdkPixbuf.Pixbuf]: ...
def set_default_dpi(dpi: float) -> None: ...
def set_default_dpi_x_y(dpi_x: float, dpi_y: float) -> None: ...
def term() -> None: ...

class DimensionData(GObject.GPointer):
    """
    :Constructors:

    ::

        DimensionData()
    """

    width: int = ...
    height: int = ...
    em: float = ...
    ex: float = ...

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
      flags -> RsvgHandleFlags: flags
      dpi-x -> gdouble: dpi-x
      dpi-y -> gdouble: dpi-y
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

    class Props:
        base_uri: str
        desc: Optional[str]
        dpi_x: float
        dpi_y: float
        em: float
        ex: float
        flags: HandleFlags
        height: int
        metadata: Optional[str]
        title: Optional[str]
        width: int
    props: Props = ...
    parent: GObject.Object = ...
    _abi_padding: list[None] = ...
    def __init__(
        self,
        base_uri: str = ...,
        dpi_x: float = ...,
        dpi_y: float = ...,
        flags: HandleFlags = ...,
    ): ...
    def close(self) -> bool: ...
    def free(self) -> None: ...
    def get_base_uri(self) -> str: ...
    def get_desc(self) -> Optional[str]: ...
    def get_dimensions(self) -> DimensionData: ...
    def get_dimensions_sub(
        self, id: Optional[str] = None
    ) -> Tuple[bool, DimensionData]: ...
    def get_geometry_for_element(
        self, id: Optional[str] = None
    ) -> Tuple[bool, Rectangle, Rectangle]: ...
    def get_geometry_for_layer(
        self, id: Optional[str], viewport: Rectangle
    ) -> Tuple[bool, Rectangle, Rectangle]: ...
    def get_intrinsic_dimensions(
        self,
    ) -> Tuple[bool, Length, bool, Length, bool, Rectangle]: ...
    def get_intrinsic_size_in_pixels(self) -> Tuple[bool, float, float]: ...
    def get_metadata(self) -> Optional[str]: ...
    def get_pixbuf(self) -> Optional[GdkPixbuf.Pixbuf]: ...
    def get_pixbuf_sub(
        self, id: Optional[str] = None
    ) -> Optional[GdkPixbuf.Pixbuf]: ...
    def get_position_sub(
        self, id: Optional[str] = None
    ) -> Tuple[bool, PositionData]: ...
    def get_title(self) -> Optional[str]: ...
    def has_sub(self, id: str) -> bool: ...
    def internal_set_testing(self, testing: bool) -> None: ...
    @classmethod
    def new(cls) -> Handle: ...
    @classmethod
    def new_from_data(cls, data: Sequence[int]) -> Optional[Handle]: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Optional[Handle]: ...
    @classmethod
    def new_from_gfile_sync(
        cls,
        file: Gio.File,
        flags: HandleFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Optional[Handle]: ...
    @classmethod
    def new_from_stream_sync(
        cls,
        input_stream: Gio.InputStream,
        base_file: Optional[Gio.File],
        flags: HandleFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Optional[Handle]: ...
    @classmethod
    def new_with_flags(cls, flags: HandleFlags) -> Handle: ...
    def read_stream_sync(
        self, stream: Gio.InputStream, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def render_cairo(self, cr: cairo.Context[_SomeSurface]) -> bool: ...
    def render_cairo_sub(
        self, cr: cairo.Context[_SomeSurface], id: Optional[str] = None
    ) -> bool: ...
    def render_document(
        self, cr: cairo.Context[_SomeSurface], viewport: Rectangle
    ) -> bool: ...
    def render_element(
        self,
        cr: cairo.Context[_SomeSurface],
        id: Optional[str],
        element_viewport: Rectangle,
    ) -> bool: ...
    def render_layer(
        self, cr: cairo.Context[_SomeSurface], id: Optional[str], viewport: Rectangle
    ) -> bool: ...
    def set_base_gfile(self, base_file: Gio.File) -> None: ...
    def set_base_uri(self, base_uri: str) -> None: ...
    def set_dpi(self, dpi: float) -> None: ...
    def set_dpi_x_y(self, dpi_x: float, dpi_y: float) -> None: ...
    def set_size_callback(
        self,
        size_func: Optional[Callable[..., Tuple[int, int]]] = None,
        *user_data: Any,
    ) -> None: ...
    def set_stylesheet(self, css: Sequence[int]) -> bool: ...
    def write(self, buf: Sequence[int]) -> bool: ...

class HandleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HandleClass()
    """

    parent: GObject.ObjectClass = ...
    _abi_padding: list[None] = ...

class Length(GObject.GPointer):
    """
    :Constructors:

    ::

        Length()
    """

    length: float = ...
    unit: Unit = ...

class PositionData(GObject.GPointer):
    """
    :Constructors:

    ::

        PositionData()
    """

    x: int = ...
    y: int = ...

class Rectangle(GObject.GPointer):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: float = ...
    y: float = ...
    width: float = ...
    height: float = ...

class HandleFlags(GObject.GFlags):
    FLAGS_NONE = 0
    FLAG_KEEP_IMAGE_DATA = 2
    FLAG_UNLIMITED = 1

class Error(GObject.GEnum):
    FAILED = 0
    @staticmethod
    def quark() -> int: ...

class Unit(GObject.GEnum):
    CM = 5
    EM = 2
    EX = 3
    IN = 4
    MM = 6
    PC = 8
    PERCENT = 0
    PT = 7
    PX = 1
