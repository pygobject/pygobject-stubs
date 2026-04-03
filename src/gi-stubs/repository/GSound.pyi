from typing import Any
from typing import Final
from typing import TypeVar

from collections.abc import Callable
from enum import IntEnum

from gi.repository import Gio
from gi.repository import GObject

T = TypeVar("T")

ATTR_APPLICATION_ICON: Final = "application.icon"
ATTR_APPLICATION_ICON_NAME: Final = "application.icon_name"
ATTR_APPLICATION_ID: Final = "application.id"
ATTR_APPLICATION_LANGUAGE: Final = "application.language"
ATTR_APPLICATION_NAME: Final = "application.name"
ATTR_APPLICATION_PROCESS_BINARY: Final = "application.process.binary"
ATTR_APPLICATION_PROCESS_HOST: Final = "application.process.host"
ATTR_APPLICATION_PROCESS_ID: Final = "application.process.id"
ATTR_APPLICATION_PROCESS_USER: Final = "application.process.user"
ATTR_APPLICATION_VERSION: Final = "application.version"
ATTR_CANBERRA_CACHE_CONTROL: Final = "canberra.cache-control"
ATTR_CANBERRA_ENABLE: Final = "canberra.enable"
ATTR_CANBERRA_FORCE_CHANNEL: Final = "canberra.force_channel"
ATTR_CANBERRA_VOLUME: Final = "canberra.volume"
ATTR_CANBERRA_XDG_THEME_NAME: Final = "canberra.xdg-theme.name"
ATTR_CANBERRA_XDG_THEME_OUTPUT_PROFILE: Final = "canberra.xdg-theme.output-profile"
ATTR_EVENT_DESCRIPTION: Final = "event.description"
ATTR_EVENT_ID: Final = "event.id"
ATTR_EVENT_MOUSE_BUTTON: Final = "event.mouse.button"
ATTR_EVENT_MOUSE_HPOS: Final = "event.mouse.hpos"
ATTR_EVENT_MOUSE_VPOS: Final = "event.mouse.vpos"
ATTR_EVENT_MOUSE_X: Final = "event.mouse.x"
ATTR_EVENT_MOUSE_Y: Final = "event.mouse.y"
ATTR_MEDIA_ARTIST: Final = "media.artist"
ATTR_MEDIA_FILENAME: Final = "media.filename"
ATTR_MEDIA_ICON: Final = "media.icon"
ATTR_MEDIA_ICON_NAME: Final = "media.icon_name"
ATTR_MEDIA_LANGUAGE: Final = "media.language"
ATTR_MEDIA_NAME: Final = "media.name"
ATTR_MEDIA_ROLE: Final = "media.role"
ATTR_MEDIA_TITLE: Final = "media.title"
ATTR_WINDOW_DESKTOP: Final = "window.desktop"
ATTR_WINDOW_HEIGHT: Final = "window.height"
ATTR_WINDOW_HPOS: Final = "window.hpos"
ATTR_WINDOW_ICON: Final = "window.icon"
ATTR_WINDOW_ICON_NAME: Final = "window.icon_name"
ATTR_WINDOW_ID: Final = "window.id"
ATTR_WINDOW_NAME: Final = "window.name"
ATTR_WINDOW_VPOS: Final = "window.vpos"
ATTR_WINDOW_WIDTH: Final = "window.width"
ATTR_WINDOW_X: Final = "window.x"
ATTR_WINDOW_X11_DISPLAY: Final = "window.x11.display"
ATTR_WINDOW_X11_MONITOR: Final = "window.x11.monitor"
ATTR_WINDOW_X11_SCREEN: Final = "window.x11.screen"
ATTR_WINDOW_X11_XID: Final = "window.x11.xid"
ATTR_WINDOW_Y: Final = "window.y"

def error_quark() -> int: ...

class Context(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Context(**properties)
        new(cancellable:Gio.Cancellable=None) -> GSound.Context

    Object GSoundContext

    Signals from GObject:
      notify (GParam)
    """
    def cache(self, attrs: dict[str, str]) -> bool: ...
    @classmethod
    def new(cls, cancellable: Gio.Cancellable | None = None) -> Context: ...
    def open(self) -> bool: ...
    def play_full(
        self,
        attrs: dict[str, str],
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def play_full_finish(self, result: Gio.AsyncResult) -> bool: ...
    def play_simple(
        self,
        attrs: dict[str, str],
        cancellable: Gio.Cancellable | None = None,
    ) -> bool: ...
    def set_attributes(self, attrs: dict[str, str]) -> bool: ...
    def set_driver(self, driver: str) -> bool: ...

class ContextClass(GObject.GPointer): ...

class Error(IntEnum):
    ACCESS = -13
    CANCELED = -11
    CORRUPT = -7
    DESTROYED = -10
    DISABLED = -16
    DISCONNECTED = -18
    FORKED = -17
    INTERNAL = -15
    INVALID = -2
    IO = -14
    NODRIVER = -5
    NOTAVAILABLE = -12
    NOTFOUND = -9
    NOTSUPPORTED = -1
    OOM = -4
    STATE = -3
    SYSTEM = -6
    TOOBIG = -8
