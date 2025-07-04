import typing

from gi.repository import Gdk
from gi.repository import GObject

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "GdkWin32"
_version: str = "3.0"

def win32_selection_add_targets(
    owner: Gdk.Window, selection: Gdk.Atom, n_targets: int, targets: Gdk.Atom
) -> None: ...
def win32_selection_clear_targets_libgtk_only(
    display: Gdk.Display, selection: Gdk.Atom
) -> None: ...

class Win32Cursor(Gdk.Cursor): ...
class Win32CursorClass(GObject.GPointer): ...

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
      monitor-added (GdkMonitor)
      monitor-removed (GdkMonitor)

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def get_wgl_version(display: Gdk.Display) -> typing.Tuple[bool, int, int]: ...
    def set_cursor_theme(self, name: typing.Optional[str], size: int) -> None: ...

class Win32DisplayClass(GObject.GPointer): ...
class Win32DisplayManager(Gdk.DisplayManager): ...
class Win32DisplayManagerClass(GObject.GPointer): ...
class Win32DragContext(Gdk.DragContext): ...
class Win32DragContextClass(GObject.GPointer): ...
class Win32GLContext(Gdk.GLContext): ...
class Win32GLContextClass(GObject.GPointer): ...

class Win32Keymap(Gdk.Keymap):
    """
    :Constructors:

    ::

        Win32Keymap(**properties)

    Object GdkWin32Keymap

    Signals from GdkKeymap:
      direction-changed ()
      keys-changed ()
      state-changed ()

    Signals from GObject:
      notify (GParam)
    """

    def check_compose(
        self, compose_buffer: int, compose_buffer_len: int, output: int, output_len: int
    ) -> Win32KeymapMatch: ...

class Win32KeymapClass(GObject.GPointer): ...

class Win32KeymapMatch:
    EXACT: Win32KeymapMatch = 3
    INCOMPLETE: Win32KeymapMatch = 1
    NONE: Win32KeymapMatch = 0
    PARTIAL: Win32KeymapMatch = 2
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

class Win32Monitor(Gdk.Monitor): ...
class Win32MonitorClass(GObject.GPointer): ...
class Win32Screen(Gdk.Screen): ...
class Win32ScreenClass(GObject.GPointer): ...

class Win32Window(Gdk.Window):
    """
    :Constructors:

    ::

        Win32Window(**properties)

    Object GdkWin32Window

    Signals from GdkWindow:
      pick-embedded-child (gdouble, gdouble) -> GdkWindow
      to-embedder (gdouble, gdouble, gpointer, gpointer)
      from-embedder (gdouble, gdouble, gpointer, gpointer)
      create-surface (gint, gint) -> CairoSurface
      moved-to-rect (gpointer, gpointer, gboolean, gboolean)

    Properties from GdkWindow:
      cursor -> GdkCursor: Cursor
        Cursor

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def is_win32(window: Gdk.Window) -> bool: ...

class Win32WindowClass(GObject.GPointer): ...
