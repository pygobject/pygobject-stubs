import typing

from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import win32

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "GdkWin32"
_version: str = "4.0"

def win32_handle_table_lookup(handle: int) -> None: ...

class Win32Display(Gdk.Display):
    """
    :Constructors:

    ::

        Win32Display(**properties)

    Object GdkWin32Display

    Signals from GdkDisplay:
      opened ()
      closed (gboolean)
      seat-added (GdkSeat)
      seat-removed (GdkSeat)
      setting-changed (gchararray)

    Properties from GdkDisplay:
      composited -> gboolean: composited
      rgba -> gboolean: rgba
      shadow-width -> gboolean: shadow-width
      input-shapes -> gboolean: input-shapes
      dmabuf-formats -> GdkDmabufFormats: dmabuf-formats

    Signals from GObject:
      notify (GParam)
    """

    def add_filter(
        self,
        function: typing.Callable[..., Win32MessageFilterReturn],
        *data: typing.Any,
    ) -> None: ...
    def get_egl_display(self) -> None: ...
    @staticmethod
    def get_wgl_version(display: Gdk.Display) -> typing.Tuple[bool, int, int]: ...
    def remove_filter(
        self,
        function: typing.Callable[..., Win32MessageFilterReturn],
        *data: typing.Any,
    ) -> None: ...
    def set_cursor_theme(self, name: typing.Optional[str], size: int) -> None: ...

class Win32DisplayClass(GObject.GPointer): ...
class Win32DisplayManager(Gdk.DisplayManager): ...
class Win32DisplayManagerClass(GObject.GPointer): ...
class Win32Drag(Gdk.Drag): ...
class Win32DragClass(GObject.GPointer): ...
class Win32GLContext(Gdk.GLContext): ...
class Win32GLContextClass(GObject.GPointer): ...

class Win32HCursor(GObject.Object):
    """
    :Constructors:

    ::

        Win32HCursor(**properties)
        new(display:GdkWin32.Win32Display, handle:int, destroyable:bool) -> GdkWin32.Win32HCursor

    Object GdkWin32HCursor

    Properties from GdkWin32HCursor:
      display -> GdkDisplay: display
      handle -> gpointer: handle
      destroyable -> gboolean: destroyable

    Signals from GObject:
      notify (GParam)
    """

    def new(
        display: Win32Display, handle: int, destroyable: bool
    ) -> Win32HCursor: ...  # FIXME Function

class Win32HCursorClass(GObject.GPointer): ...

class Win32MessageFilterReturn:
    CONTINUE: Win32MessageFilterReturn = 0
    REMOVE: Win32MessageFilterReturn = 1
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class Win32Monitor(Gdk.Monitor):
    """
    :Constructors:

    ::

        Win32Monitor(**properties)

    Object GdkWin32Monitor

    Signals from GdkMonitor:
      invalidate ()

    Properties from GdkMonitor:
      description -> gchararray: description
      display -> GdkDisplay: display
      manufacturer -> gchararray: manufacturer
      model -> gchararray: model
      connector -> gchararray: connector
      scale-factor -> gint: scale-factor
      scale -> gdouble: scale
      geometry -> GdkRectangle: geometry
      width-mm -> gint: width-mm
      height-mm -> gint: height-mm
      refresh-rate -> gint: refresh-rate
      subpixel-layout -> GdkSubpixelLayout: subpixel-layout
      valid -> gboolean: valid

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get_workarea(monitor: Gdk.Monitor) -> Gdk.Rectangle: ...

class Win32MonitorClass(GObject.GPointer): ...
class Win32Screen(GObject.Object): ...
class Win32ScreenClass(GObject.GPointer): ...

class Win32Surface(Gdk.Surface):
    """
    :Constructors:

    ::

        Win32Surface(**properties)

    Object GdkWin32Surface

    Signals from GdkSurface:
      layout (gint, gint)
      render (CairoRegion) -> gboolean
      event (gpointer) -> gboolean
      enter-monitor (GdkMonitor)
      leave-monitor (GdkMonitor)

    Properties from GdkSurface:
      cursor -> GdkCursor: cursor
      display -> GdkDisplay: display
      frame-clock -> GdkFrameClock: frame-clock
      mapped -> gboolean: mapped
      width -> gint: width
      height -> gint: height
      scale-factor -> gint: scale-factor
      scale -> gdouble: scale

    Signals from GObject:
      notify (GParam)
    """

    def get_handle(self) -> int: ...
    @staticmethod
    def get_impl_hwnd(surface: Gdk.Surface) -> int: ...
    @staticmethod
    def is_win32(surface: Gdk.Surface) -> bool: ...
    def set_urgency_hint(self, urgent: bool) -> None: ...

class Win32SurfaceClass(GObject.GPointer): ...

class _Win32HCursorFake(GObject.GPointer):
    """
    :Constructors:

    ::

        _Win32HCursorFake()
    """

    parent_instance: GObject.Object = ...
    readonly_handle: int = ...
