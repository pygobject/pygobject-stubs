from typing import TypeVar

from enum import IntEnum

from gi.repository import _Gdk4
from gi.repository import GObject
from gi.repository import Pango
from gi.repository import xlib

T = TypeVar("T")

def x11_device_get_id(device: X11DeviceXI2) -> int: ...
def x11_device_manager_lookup(
    device_manager: X11DeviceManagerXI2, device_id: int
) -> X11DeviceXI2 | None: ...
def x11_free_compound_text(ctext: int) -> None: ...
def x11_free_text_list(list: str) -> None: ...
def x11_get_server_time(surface: X11Surface) -> int: ...
def x11_get_xatom_by_name_for_display(display: X11Display, atom_name: str) -> int: ...
def x11_get_xatom_name_for_display(display: X11Display, xatom: int) -> str: ...
def x11_lookup_xdisplay(xdisplay: xlib.Display) -> X11Display: ...
def x11_set_sm_client_id(sm_client_id: str | None = None) -> None: ...

class X11AppLaunchContext(_Gdk4.AppLaunchContext):
    """
    :Constructors:

    ::

        X11AppLaunchContext(**properties)

    Object GdkX11AppLaunchContext

    Properties from GdkAppLaunchContext:
      display -> GdkDisplay: display

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gdk4.AppLaunchContext.Props):
        display: _Gdk4.Display

    @property
    def props(self) -> Props: ...
    def __init__(self, display: _Gdk4.Display = ...) -> None: ...

class X11AppLaunchContextClass(GObject.GPointer): ...

class X11DeviceManagerXI2(GObject.Object):
    """
    :Constructors:

    ::

        X11DeviceManagerXI2(**properties)

    Object GdkX11DeviceManagerXI2

    Properties from GdkX11DeviceManagerXI2:
      display -> GdkDisplay: display
      opcode -> gint: opcode
      major -> gint: major
      minor -> gint: minor

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        display: _Gdk4.Display
        major: int
        minor: int
        opcode: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        display: _Gdk4.Display = ...,
        major: int = ...,
        minor: int = ...,
        opcode: int = ...,
    ) -> None: ...

class X11DeviceManagerXI2Class(GObject.GPointer): ...

class X11DeviceXI2(_Gdk4.Device):
    """
    :Constructors:

    ::

        X11DeviceXI2(**properties)

    Object GdkX11DeviceXI2

    Properties from GdkX11DeviceXI2:
      device-id -> gint: device-id

    Signals from GdkDevice:
      changed ()
      tool-changed (GdkDeviceTool)

    Properties from GdkDevice:
      display -> GdkDisplay: display
      name -> gchararray: name
      source -> GdkInputSource: source
      has-cursor -> gboolean: has-cursor
      n-axes -> guint: n-axes
      vendor-id -> gchararray: vendor-id
      product-id -> gchararray: product-id
      seat -> GdkSeat: seat
      num-touches -> guint: num-touches
      tool -> GdkDeviceTool: tool
      direction -> PangoDirection: direction
      has-bidi-layouts -> gboolean: has-bidi-layouts
      caps-lock-state -> gboolean: caps-lock-state
      num-lock-state -> gboolean: num-lock-state
      scroll-lock-state -> gboolean: scroll-lock-state
      modifier-state -> GdkModifierType: modifier-state
      layout-names -> GStrv: layout-names
      active-layout-index -> gint: active-layout-index

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gdk4.Device.Props):
        device_id: int
        active_layout_index: int
        caps_lock_state: bool
        direction: Pango.Direction
        display: _Gdk4.Display
        has_bidi_layouts: bool
        has_cursor: bool
        layout_names: list[str] | None
        modifier_state: _Gdk4.ModifierType
        n_axes: int
        name: str
        num_lock_state: bool
        num_touches: int
        product_id: str | None
        scroll_lock_state: bool
        seat: _Gdk4.Seat
        source: _Gdk4.InputSource
        tool: _Gdk4.DeviceTool | None
        vendor_id: str | None

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        device_id: int = ...,
        display: _Gdk4.Display = ...,
        has_cursor: bool = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: _Gdk4.Seat = ...,
        source: _Gdk4.InputSource = ...,
        vendor_id: str = ...,
    ) -> None: ...

class X11DeviceXI2Class(GObject.GPointer): ...

class X11Display(_Gdk4.Display):
    """
    :Constructors:

    ::

        X11Display(**properties)

    Object GdkX11Display

    Signals from GdkX11Display:
      xevent (gpointer) -> gboolean

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
    class Props(_Gdk4.Display.Props):
        composited: bool
        dmabuf_formats: _Gdk4.DmabufFormats
        input_shapes: bool
        rgba: bool
        shadow_width: bool

    @property
    def props(self) -> Props: ...
    def error_trap_pop(self) -> int: ...
    def error_trap_pop_ignored(self) -> None: ...
    def error_trap_push(self) -> None: ...
    def get_default_group(self) -> _Gdk4.Surface: ...
    def get_egl_display(self) -> None: ...
    def get_egl_version(self) -> tuple[bool, int, int]: ...
    def get_glx_version(self) -> tuple[bool, int, int]: ...
    def get_primary_monitor(self) -> _Gdk4.Monitor: ...
    def get_screen(self) -> X11Screen: ...
    def get_startup_notification_id(self) -> str: ...
    def get_user_time(self) -> int: ...
    def get_xcursor(self, cursor: _Gdk4.Cursor) -> int: ...
    def get_xdisplay(self) -> xlib.Display: ...
    def get_xrootwindow(self) -> int: ...
    def get_xscreen(self) -> xlib.Screen: ...
    def grab(self) -> None: ...
    @staticmethod
    def open(
        display_name: str | None = None,
    ) -> _Gdk4.Display | None: ...
    def set_cursor_theme(self, theme: str | None, size: int) -> None: ...
    @staticmethod
    def set_program_class(display: _Gdk4.Display, program_class: str) -> None: ...
    def set_startup_notification_id(self, startup_id: str) -> None: ...
    def set_surface_scale(self, scale: int) -> None: ...
    def string_to_compound_text(self, str: str) -> tuple[int, str, int, bytes]: ...
    def text_property_to_text_list(
        self, encoding: str, format: int, text: int, length: int, list: str
    ) -> int: ...
    def ungrab(self) -> None: ...
    def utf8_to_compound_text(self, str: str) -> tuple[bool, str, int, bytes]: ...

class X11DisplayClass(GObject.GPointer): ...

class X11Drag(_Gdk4.Drag):
    """
    :Constructors:

    ::

        X11Drag(**properties)

    Object GdkX11Drag

    Signals from GdkDrag:
      cancel (GdkDragCancelReason)
      drop-performed ()
      dnd-finished ()

    Properties from GdkDrag:
      content -> GdkContentProvider: content
      device -> GdkDevice: device
      display -> GdkDisplay: display
      formats -> GdkContentFormats: formats
      selected-action -> GdkDragAction: selected-action
      actions -> GdkDragAction: actions
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gdk4.Drag.Props):
        actions: _Gdk4.DragAction
        content: _Gdk4.ContentProvider
        device: _Gdk4.Device
        display: _Gdk4.Display
        formats: _Gdk4.ContentFormats
        selected_action: _Gdk4.DragAction
        surface: _Gdk4.Surface

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        actions: _Gdk4.DragAction = ...,
        content: _Gdk4.ContentProvider = ...,
        device: _Gdk4.Device = ...,
        formats: _Gdk4.ContentFormats = ...,
        selected_action: _Gdk4.DragAction = ...,
        surface: _Gdk4.Surface = ...,
    ) -> None: ...

class X11DragClass(GObject.GPointer): ...

class X11GLContext(_Gdk4.GLContext):
    """
    :Constructors:

    ::

        X11GLContext(**properties)

    Object GdkX11GLContext

    Properties from GdkGLContext:
      allowed-apis -> GdkGLAPI: allowed-apis
      api -> GdkGLAPI: api
      shared-context -> GdkGLContext: shared-context

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gdk4.GLContext.Props):
        allowed_apis: _Gdk4.GLAPI
        api: _Gdk4.GLAPI
        shared_context: _Gdk4.GLContext | None
        display: _Gdk4.Display | None
        surface: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        allowed_apis: _Gdk4.GLAPI = ...,
        shared_context: _Gdk4.GLContext = ...,
        display: _Gdk4.Display = ...,
        surface: _Gdk4.Surface = ...,
    ) -> None: ...

class X11GLContextClass(GObject.GPointer): ...

class X11Monitor(_Gdk4.Monitor):
    """
    :Constructors:

    ::

        X11Monitor(**properties)

    Object GdkX11Monitor

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
    class Props(_Gdk4.Monitor.Props):
        connector: str | None
        description: str | None
        display: _Gdk4.Display
        geometry: _Gdk4.Rectangle
        height_mm: int
        manufacturer: str | None
        model: str | None
        refresh_rate: int
        scale: float
        scale_factor: int
        subpixel_layout: _Gdk4.SubpixelLayout
        valid: bool
        width_mm: int

    @property
    def props(self) -> Props: ...
    def __init__(self, display: _Gdk4.Display = ...) -> None: ...
    def get_output(self) -> int: ...
    def get_workarea(self) -> _Gdk4.Rectangle: ...

class X11MonitorClass(GObject.GPointer): ...

class X11Screen(GObject.Object):
    """
    :Constructors:

    ::

        X11Screen(**properties)

    Object GdkX11Screen

    Signals from GdkX11Screen:
      window-manager-changed ()

    Signals from GObject:
      notify (GParam)
    """
    def get_current_desktop(self) -> int: ...
    def get_monitor_output(self, monitor_num: int) -> int: ...
    def get_number_of_desktops(self) -> int: ...
    def get_screen_number(self) -> int: ...
    def get_window_manager_name(self) -> str: ...
    def get_xscreen(self) -> xlib.Screen: ...
    def supports_net_wm_hint(self, property_name: str) -> bool: ...

class X11ScreenClass(GObject.GPointer): ...

class X11Surface(_Gdk4.Surface):
    """
    :Constructors:

    ::

        X11Surface(**properties)

    Object GdkX11Surface

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
    class Props(_Gdk4.Surface.Props):
        cursor: _Gdk4.Cursor | None
        display: _Gdk4.Display
        frame_clock: _Gdk4.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display = ...,
        frame_clock: _Gdk4.FrameClock = ...,
    ) -> None: ...
    def get_desktop(self) -> int: ...
    def get_group(self) -> _Gdk4.Surface | None: ...
    def get_xid(self) -> int: ...
    @staticmethod
    def lookup_for_display(display: X11Display, window: int) -> X11Surface: ...
    def move_to_current_desktop(self) -> None: ...
    def move_to_desktop(self, desktop: int) -> None: ...
    def set_frame_sync_enabled(self, frame_sync_enabled: bool) -> None: ...
    def set_group(self, leader: _Gdk4.Surface) -> None: ...
    def set_skip_pager_hint(self, skips_pager: bool) -> None: ...
    def set_skip_taskbar_hint(self, skips_taskbar: bool) -> None: ...
    def set_theme_variant(self, variant: str) -> None: ...
    def set_urgency_hint(self, urgent: bool) -> None: ...
    def set_user_time(self, timestamp: int) -> None: ...
    def set_utf8_property(self, name: str, value: str | None = None) -> None: ...

class X11SurfaceClass(GObject.GPointer): ...

class X11DeviceType(IntEnum):
    FLOATING = 2
    LOGICAL = 0
    PHYSICAL = 1
