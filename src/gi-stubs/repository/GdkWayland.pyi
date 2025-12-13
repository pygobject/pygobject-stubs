import typing

from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import Pango
from typing_extensions import Self

T = typing.TypeVar("T")

class WaylandDevice(Gdk.Device):
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
    class Props(Gdk.Device.Props):
        active_layout_index: int
        caps_lock_state: bool
        direction: Pango.Direction
        display: Gdk.Display
        has_bidi_layouts: bool
        has_cursor: bool
        layout_names: typing.Optional[list[str]]
        modifier_state: Gdk.ModifierType
        n_axes: int
        name: str
        num_lock_state: bool
        num_touches: int
        product_id: typing.Optional[str]
        scroll_lock_state: bool
        seat: Gdk.Seat
        source: Gdk.InputSource
        tool: typing.Optional[Gdk.DeviceTool]
        vendor_id: typing.Optional[str]

    props: Props = ...
    def __init__(
        self,
        display: Gdk.Display = ...,
        has_cursor: bool = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: Gdk.Seat = ...,
        source: Gdk.InputSource = ...,
        vendor_id: str = ...,
    ) -> None: ...
    def get_node_path(self) -> typing.Optional[str]: ...
    def get_xkb_keymap(self) -> None: ...

class WaylandDeviceClass(GObject.GPointer): ...

class WaylandDisplay(Gdk.Display):
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
    class Props(Gdk.Display.Props):
        composited: bool
        dmabuf_formats: Gdk.DmabufFormats
        input_shapes: bool
        rgba: bool
        shadow_width: bool

    props: Props = ...
    def get_egl_display(self) -> None: ...
    def get_startup_notification_id(self) -> typing.Optional[str]: ...
    def query_registry(self, global_: str) -> bool: ...
    def set_cursor_theme(self, name: str, size: int) -> None: ...
    def set_startup_notification_id(self, startup_id: str) -> None: ...

class WaylandDisplayClass(GObject.GPointer): ...

class WaylandGLContext(Gdk.GLContext):
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
    class Props(Gdk.GLContext.Props):
        allowed_apis: Gdk.GLAPI
        api: Gdk.GLAPI
        shared_context: typing.Optional[Gdk.GLContext]
        display: typing.Optional[Gdk.Display]
        surface: typing.Optional[Gdk.Surface]

    props: Props = ...
    def __init__(
        self,
        allowed_apis: Gdk.GLAPI = ...,
        shared_context: Gdk.GLContext = ...,
        display: Gdk.Display = ...,
        surface: Gdk.Surface = ...,
    ) -> None: ...

class WaylandGLContextClass(GObject.GPointer): ...

class WaylandMonitor(Gdk.Monitor):
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
    class Props(Gdk.Monitor.Props):
        connector: typing.Optional[str]
        description: typing.Optional[str]
        display: Gdk.Display
        geometry: Gdk.Rectangle
        height_mm: int
        manufacturer: typing.Optional[str]
        model: typing.Optional[str]
        refresh_rate: int
        scale: float
        scale_factor: int
        subpixel_layout: Gdk.SubpixelLayout
        valid: bool
        width_mm: int

    props: Props = ...
    def __init__(self, display: Gdk.Display = ...) -> None: ...

class WaylandMonitorClass(GObject.GPointer): ...

class WaylandPopup(WaylandSurface, Gdk.Popup):
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
        cursor: typing.Optional[Gdk.Cursor]
        display: Gdk.Display
        frame_clock: Gdk.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int
        autohide: bool
        parent: typing.Optional[Gdk.Surface]

    props: Props = ...
    def __init__(
        self,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        display: Gdk.Display = ...,
        frame_clock: Gdk.FrameClock = ...,
        autohide: bool = ...,
        parent: Gdk.Surface = ...,
    ) -> None: ...

class WaylandSeat(Gdk.Seat):
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
    class Props(Gdk.Seat.Props):
        display: Gdk.Display

    props: Props = ...
    def __init__(self, display: Gdk.Display = ...) -> None: ...

class WaylandSeatClass(GObject.GPointer): ...

class WaylandSurface(Gdk.Surface):
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
    class Props(Gdk.Surface.Props):
        cursor: typing.Optional[Gdk.Cursor]
        display: Gdk.Display
        frame_clock: Gdk.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int

    props: Props = ...
    def __init__(
        self,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        display: Gdk.Display = ...,
        frame_clock: Gdk.FrameClock = ...,
    ) -> None: ...
    def force_next_commit(self) -> None: ...

class WaylandToplevel(WaylandSurface, Gdk.Toplevel):
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
        cursor: typing.Optional[Gdk.Cursor]
        display: Gdk.Display
        frame_clock: Gdk.FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int
        capabilities: Gdk.ToplevelCapabilities
        decorated: bool
        deletable: bool
        fullscreen_mode: Gdk.FullscreenMode
        gravity: Gdk.Gravity
        icon_list: None
        modal: bool
        shortcuts_inhibited: bool
        startup_id: str
        state: Gdk.ToplevelState
        title: str
        transient_for: Gdk.Surface

    props: Props = ...
    def __init__(
        self,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        display: Gdk.Display = ...,
        frame_clock: Gdk.FrameClock = ...,
        decorated: bool = ...,
        deletable: bool = ...,
        fullscreen_mode: Gdk.FullscreenMode = ...,
        gravity: Gdk.Gravity = ...,
        icon_list: None = ...,
        modal: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Gdk.Surface = ...,
    ) -> None: ...
    def drop_exported_handle(self, handle: str) -> None: ...
    def export_handle(
        self, callback: typing.Callable[..., None], *user_data: typing.Any
    ) -> bool: ...
    def set_application_id(self, application_id: str) -> None: ...
    def set_transient_for_exported(self, parent_handle_str: str) -> bool: ...
    def unexport_handle(self) -> None: ...
