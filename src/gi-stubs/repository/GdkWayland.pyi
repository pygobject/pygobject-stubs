from typing import Any
from typing import type_check_only
from typing_extensions import Unpack

from collections.abc import Callable

from gi import _gi
from gi.repository import _Gdk4

_DataTs = TypeVarTuple("_DataTs", default=Unpack[tuple[()]])

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
    def __init__(
        self,
        *,
        display: _Gdk4.Display | None = ...,
        has_cursor: bool = ...,
        name: str | None = ...,
        num_touches: int = ...,
        product_id: str | None = ...,
        seat: _Gdk4.Seat | None = ...,
        source: _Gdk4._InputSourceValueType = ...,
        vendor_id: str | None = ...,
    ) -> None: ...
    def get_node_path(self) -> str | None: ...
    def get_xkb_keymap(self) -> int: ...

class WaylandDeviceClass(_gi.Struct): ...

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
    def get_egl_display(self) -> int: ...
    def get_startup_notification_id(self) -> str | None: ...
    def query_registry(self, global_: str) -> bool: ...
    def set_cursor_theme(self, name: str, size: int) -> None: ...
    def set_startup_notification_id(self, startup_id: str) -> None: ...

class WaylandDisplayClass(_gi.Struct): ...

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
    def __init__(
        self,
        *,
        allowed_apis: _Gdk4._GLAPIValueType = ...,
        shared_context: _Gdk4.GLContext | None = ...,
        display: _Gdk4.Display | None = ...,
        surface: _Gdk4.Surface | None = ...,
    ) -> None: ...

class WaylandGLContextClass(_gi.Struct): ...

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
    def __init__(self, *, display: _Gdk4.Display | None = ...) -> None: ...

class WaylandMonitorClass(_gi.Struct): ...

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
    @type_check_only
    class Props(WaylandSurface.Props):
        @property
        def autohide(self) -> bool: ...
        @property
        def parent(self) -> _Gdk4.Surface | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        autohide: bool = ...,
        parent: _Gdk4.Surface | None = ...,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display | None = ...,
        frame_clock: _Gdk4.FrameClock | None = ...,
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
    def __init__(self, *, display: _Gdk4.Display | None = ...) -> None: ...

class WaylandSeatClass(_gi.Struct): ...

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
    def __init__(
        self,
        *,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display | None = ...,
        frame_clock: _Gdk4.FrameClock | None = ...,
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
    @type_check_only
    class Props(WaylandSurface.Props):
        @property
        def capabilities(self) -> _Gdk4.ToplevelCapabilities: ...
        decorated: bool
        deletable: bool
        @property
        def fullscreen_mode(self) -> _Gdk4.FullscreenMode: ...
        @fullscreen_mode.setter
        def fullscreen_mode(self, value: _Gdk4._FullscreenModeValueType) -> None: ...
        @property
        def gravity(self) -> _Gdk4.Gravity: ...
        @gravity.setter
        def gravity(self, value: _Gdk4._GravityValueType) -> None: ...
        @property
        def icon_list(self) -> int: ...
        @icon_list.setter
        def icon_list(self, value: int | Any | None) -> None: ...
        modal: bool
        @property
        def shortcuts_inhibited(self) -> bool: ...
        @property
        def startup_id(self) -> str | None: ...
        @startup_id.setter
        def startup_id(self, value: str) -> None: ...
        @property
        def state(self) -> _Gdk4.ToplevelState: ...
        @property
        def title(self) -> str | None: ...
        @title.setter
        def title(self, value: str) -> None: ...
        @property
        def transient_for(self) -> _Gdk4.Surface | None: ...
        @transient_for.setter
        def transient_for(self, value: _Gdk4.Surface) -> None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        decorated: bool = ...,
        deletable: bool = ...,
        fullscreen_mode: _Gdk4._FullscreenModeValueType = ...,
        gravity: _Gdk4._GravityValueType = ...,
        icon_list: int | Any | None = ...,
        modal: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: _Gdk4.Surface = ...,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display | None = ...,
        frame_clock: _Gdk4.FrameClock | None = ...,
    ) -> None: ...
    def drop_exported_handle(self, handle: str) -> None: ...
    def export_handle(
        self,
        callback: Callable[[WaylandToplevel, str, Unpack[_DataTs]], None],
        *user_data: Unpack[_DataTs],
    ) -> bool: ...
    def set_application_id(self, application_id: str) -> None: ...
    def set_transient_for_exported(self, parent_handle_str: str) -> bool: ...
    def unexport_handle(self) -> None: ...
