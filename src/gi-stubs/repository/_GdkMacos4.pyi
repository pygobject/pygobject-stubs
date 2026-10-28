from typing import type_check_only

from gi import _gi
from gi.repository import _Gdk4
from gi.repository import GObject

class MacosDevice(_Gdk4.Device):
    """
    :Constructors:

    ::

        MacosDevice(**properties)

    Object GdkMacosDevice

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

class MacosDeviceClass(_gi.Struct): ...

class MacosDisplay(_Gdk4.Display):
    """
    :Constructors:

    ::

        MacosDisplay(**properties)

    Object GdkMacosDisplay

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

class MacosDisplayClass(_gi.Struct): ...

class MacosGLContext(_Gdk4.GLContext):
    """
    :Constructors:

    ::

        MacosGLContext(**properties)

    Object GdkMacosGLContext

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

class MacosGLContextClass(_gi.Struct): ...

class MacosKeymap(GObject.Object):
    """
    :Constructors:

    ::

        MacosKeymap(**properties)

    Object GdkMacosKeymap

    Signals from GdkKeymap:
      direction-changed ()
      keys-changed ()
      state-changed ()

    Properties from GdkKeymap:
      display -> GdkDisplay: display

    Signals from GObject:
      notify (GParam)
    """

class MacosKeymapClass(_gi.Struct): ...

class MacosMonitor(_Gdk4.Monitor):
    """
    :Constructors:

    ::

        MacosMonitor(**properties)

    Object GdkMacosMonitor

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
    @staticmethod
    def get_workarea(monitor: _Gdk4.Monitor) -> _Gdk4.Rectangle: ...

class MacosMonitorClass(_gi.Struct): ...

class MacosSeat(_Gdk4.Seat):
    """
    :Constructors:

    ::

        MacosSeat(**properties)

    Object GdkMacosSeat

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

class MacosSeatClass(_gi.Struct): ...

class MacosSurface(_Gdk4.Surface):
    """
    :Constructors:

    ::

        MacosSurface(**properties)

    Object GdkMacosSurface

    Properties from GdkMacosSurface:
      native -> gpointer: native

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
    class Props(_Gdk4.Surface.Props):
        @property
        def native(self) -> int: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        cursor: _Gdk4.Cursor | None = ...,
        display: _Gdk4.Display | None = ...,
        frame_clock: _Gdk4.FrameClock | None = ...,
    ) -> None: ...
    def get_native_window(self) -> int: ...

class MacosSurfaceClass(_gi.Struct): ...
