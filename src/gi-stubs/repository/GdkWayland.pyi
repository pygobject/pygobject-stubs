from typing import Any
from typing import TypeVar

from collections.abc import Callable

from gi.repository import _Gdk4
from gi.repository import GObject
from gi.repository import Pango

T = TypeVar("T")

class WaylandDevice(_Gdk4.Device):
    """
    :Constructors:

    ::

        WaylandDevice(**properties)

    Object GdkWaylandDevice

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
        display: _Gdk4.Display = ...,
        has_cursor: bool = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: _Gdk4.Seat = ...,
        source: _Gdk4.InputSource = ...,
        vendor_id: str = ...,
    ) -> None: ...
    def get_node_path(self) -> str | None: ...
    def get_xkb_keymap(self) -> None: ...

class WaylandDeviceClass(GObject.GPointer): ...

class WaylandDisplay(_Gdk4.Display):
    """
    :Constructors:

    ::

        WaylandDisplay(**properties)

    Object GdkWaylandDisplay

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
    def get_egl_display(self) -> None: ...
    def get_startup_notification_id(self) -> str | None: ...
    def query_registry(self, global_: str) -> bool: ...
    def set_cursor_theme(self, name: str, size: int) -> None: ...
    def set_startup_notification_id(self, startup_id: str) -> None: ...

class WaylandDisplayClass(GObject.GPointer): ...

class WaylandGLContext(_Gdk4.GLContext):
    """
    :Constructors:

    ::

        WaylandGLContext(**properties)

    Object GdkWaylandGLContext

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

class WaylandGLContextClass(GObject.GPointer): ...

class WaylandMonitor(_Gdk4.Monitor):
    """
    :Constructors:

    ::

        WaylandMonitor(**properties)

    Object GdkWaylandMonitor

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

class WaylandMonitorClass(GObject.GPointer): ...

class WaylandPopup(WaylandSurface, _Gdk4.Popup):
    """
    :Constructors:

    ::

        WaylandPopup(**properties)

    Object GdkWaylandPopup

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
    class Props(WaylandSurface.Props):
        cursor: _Gdk4.Cursor | None
        display: _Gdk4.Display
        frame_clock: _Gdk4.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int
        autohide: bool
        parent: _Gdk4.Surface | None

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display = ...,
        frame_clock: _Gdk4.FrameClock = ...,
        autohide: bool = ...,
        parent: _Gdk4.Surface = ...,
    ) -> None: ...

class WaylandSeat(_Gdk4.Seat):
    """
    :Constructors:

    ::

        WaylandSeat(**properties)

    Object GdkWaylandSeat

    Signals from GdkSeat:
      device-added (GdkDevice)
      device-removed (GdkDevice)
      tool-added (GdkDeviceTool)
      tool-removed (GdkDeviceTool)

    Properties from GdkSeat:
      display -> GdkDisplay: display

    Signals from GObject:
      notify (GParam)
    """
    class Props(_Gdk4.Seat.Props):
        display: _Gdk4.Display

    @property
    def props(self) -> Props: ...
    def __init__(self, display: _Gdk4.Display = ...) -> None: ...

class WaylandSeatClass(GObject.GPointer): ...

class WaylandSurface(_Gdk4.Surface):
    """
    :Constructors:

    ::

        WaylandSurface(**properties)

    Object GdkWaylandSurface

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
    def force_next_commit(self) -> None: ...

class WaylandToplevel(WaylandSurface, _Gdk4.Toplevel):
    """
    :Constructors:

    ::

        WaylandToplevel(**properties)

    Object GdkWaylandToplevel

    Signals from GdkToplevel:
      compute-size (GdkToplevelSize)

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
    class Props(WaylandSurface.Props):
        cursor: _Gdk4.Cursor | None
        display: _Gdk4.Display
        frame_clock: _Gdk4.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int
        capabilities: _Gdk4.ToplevelCapabilities
        decorated: bool
        deletable: bool
        fullscreen_mode: _Gdk4.FullscreenMode
        gravity: _Gdk4.Gravity
        icon_list: None
        modal: bool
        shortcuts_inhibited: bool
        startup_id: str
        state: _Gdk4.ToplevelState
        title: str
        transient_for: _Gdk4.Surface

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display = ...,
        frame_clock: _Gdk4.FrameClock = ...,
        decorated: bool = ...,
        deletable: bool = ...,
        fullscreen_mode: _Gdk4.FullscreenMode = ...,
        gravity: _Gdk4.Gravity = ...,
        icon_list: None = ...,
        modal: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: _Gdk4.Surface = ...,
    ) -> None: ...
    def drop_exported_handle(self, handle: str) -> None: ...
    def export_handle(self, callback: Callable[..., None], *user_data: Any) -> bool: ...
    def set_application_id(self, application_id: str) -> None: ...
    def set_transient_for_exported(self, parent_handle_str: str) -> bool: ...
    def unexport_handle(self) -> None: ...
