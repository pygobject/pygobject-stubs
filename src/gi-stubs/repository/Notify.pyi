from typing import Any
from typing import Final

from collections.abc import Callable
from collections.abc import Sequence

from gi.repository import GdkPixbuf
from gi.repository import GLib
from gi.repository import GObject

EXPIRES_DEFAULT: Final[int]
EXPIRES_NEVER: Final[int]
VERSION_MAJOR: Final[int]
VERSION_MICRO: Final[int]
VERSION_MINOR: Final[int]

def get_app_name() -> str: ...
def get_server_caps() -> list[str]: ...
def get_server_info() -> tuple[bool, str, str, str, str]: ...
def init(app_name: str | None = None) -> bool: ...
def is_initted() -> bool: ...
def set_app_name(app_name: str) -> None: ...
def uninit() -> None: ...

class Notification(GObject.Object):
    """
    :Constructors:

    ::

        Notification(**properties)
        new(summary:str, body:str=None, icon:str=None) -> Notify.Notification

    Object NotifyNotification

    Signals from NotifyNotification:
      closed ()

    Properties from NotifyNotification:
      id -> gint: ID
        The notification ID
      app-name -> gchararray: Application name
        The application name to use for this notification
      summary -> gchararray: Summary
        The summary text
      body -> gchararray: Message Body
        The message body text
      icon-name -> gchararray: Icon Name
        The icon filename or icon theme-compliant name
      closed-reason -> gint: Closed Reason
        The reason code for why the notification was closed

    Signals from GObject:
      notify (GParam)
    """

    class Props(GObject.Object.Props):
        app_name: str | None
        body: str
        closed_reason: int
        icon_name: str
        id: int
        summary: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> NotificationPrivate: ...
    def __init__(
        self,
        app_name: str | None = ...,
        body: str = ...,
        icon_name: str = ...,
        id: int = ...,
        summary: str = ...,
    ) -> None: ...
    def add_action(
        self, action: str, label: str, callback: Callable[..., None], *user_data: Any
    ) -> None: ...
    def clear_actions(self) -> None: ...
    def clear_hints(self) -> None: ...
    def close(self) -> bool: ...
    def do_closed(self) -> None: ...
    def get_activation_token(self) -> str | None: ...
    def get_closed_reason(self) -> int: ...
    @classmethod
    def new(
        cls, summary: str, body: str | None = None, icon: str | None = None
    ) -> Notification: ...
    def set_app_name(self, app_name: str | None = None) -> None: ...
    def set_category(self, category: str) -> None: ...
    def set_hint(self, key: str, value: GLib.Variant | None = None) -> None: ...
    def set_hint_byte(self, key: str, value: int) -> None: ...
    def set_hint_byte_array(self, key: str, value: Sequence[int]) -> None: ...
    def set_hint_double(self, key: str, value: float) -> None: ...
    def set_hint_int32(self, key: str, value: int) -> None: ...
    def set_hint_string(self, key: str, value: str) -> None: ...
    def set_hint_uint32(self, key: str, value: int) -> None: ...
    def set_icon_from_pixbuf(self, icon: GdkPixbuf.Pixbuf) -> None: ...
    def set_image_from_pixbuf(self, pixbuf: GdkPixbuf.Pixbuf) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_urgency(self, urgency: Urgency) -> None: ...
    def show(self) -> bool: ...
    def update(
        self, summary: str, body: str | None = None, icon: str | None = None
    ) -> bool: ...

class NotificationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NotificationClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def closed(self) -> Callable[[Notification], None]: ...

class NotificationPrivate(GObject.GPointer): ...

class ClosedReason(GObject.GEnum):
    API_REQUEST = 3
    DISMISSED = 2
    EXPIRED = 1
    UNDEFIEND = 4
    UNSET = -1

class Urgency(GObject.GEnum):
    CRITICAL = 2
    LOW = 0
    NORMAL = 1
