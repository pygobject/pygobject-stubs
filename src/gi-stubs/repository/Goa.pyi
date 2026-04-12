from typing import Any
from typing import Final
from typing import Protocol
from typing import TypeVar

from collections.abc import Callable

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = TypeVar("T")

ERROR_NUM_ENTRIES: Final[int]
MAJOR_VERSION: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]

def account_interface_info() -> Gio.DBusInterfaceInfo: ...
def account_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def calendar_interface_info() -> Gio.DBusInterfaceInfo: ...
def calendar_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def chat_interface_info() -> Gio.DBusInterfaceInfo: ...
def chat_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def check_version(
    required_major: int, required_minor: int, required_micro: int
) -> str: ...
def contacts_interface_info() -> Gio.DBusInterfaceInfo: ...
def contacts_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def documents_interface_info() -> Gio.DBusInterfaceInfo: ...
def documents_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def error_quark() -> int: ...
def exchange_interface_info() -> Gio.DBusInterfaceInfo: ...
def exchange_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def files_interface_info() -> Gio.DBusInterfaceInfo: ...
def files_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def mail_interface_info() -> Gio.DBusInterfaceInfo: ...
def mail_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def manager_interface_info() -> Gio.DBusInterfaceInfo: ...
def manager_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def maps_interface_info() -> Gio.DBusInterfaceInfo: ...
def maps_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def media_server_interface_info() -> Gio.DBusInterfaceInfo: ...
def media_server_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def music_interface_info() -> Gio.DBusInterfaceInfo: ...
def music_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def oauth2_based_interface_info() -> Gio.DBusInterfaceInfo: ...
def oauth2_based_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def oauth_based_interface_info() -> Gio.DBusInterfaceInfo: ...
def oauth_based_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def password_based_interface_info() -> Gio.DBusInterfaceInfo: ...
def password_based_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def photos_interface_info() -> Gio.DBusInterfaceInfo: ...
def photos_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def printers_interface_info() -> Gio.DBusInterfaceInfo: ...
def printers_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def read_later_interface_info() -> Gio.DBusInterfaceInfo: ...
def read_later_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def ticketing_interface_info() -> Gio.DBusInterfaceInfo: ...
def ticketing_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def todo_interface_info() -> Gio.DBusInterfaceInfo: ...
def todo_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...

class Account(GObject.GInterface, Protocol):
    """
    Interface GoaAccount

    Signals from GObject:
      notify (GParam)
    """

    def call_ensure_credentials(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_ensure_credentials_finish(
        self, res: Gio.AsyncResult
    ) -> tuple[bool, int]: ...
    def call_ensure_credentials_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, int]: ...
    def call_remove(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_remove_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_remove_sync(self, cancellable: Gio.Cancellable | None = None) -> bool: ...
    def complete_ensure_credentials(
        self, invocation: Gio.DBusMethodInvocation, expires_in: int
    ) -> None: ...
    def complete_remove(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class AccountIface(GObject.GPointer):
    """
    :Constructors:

    ::

        AccountIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_ensure_credentials(
        self,
    ) -> Callable[[Account, Gio.DBusMethodInvocation], bool]: ...
    @property
    def handle_remove(self) -> Callable[[Account, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_attention_needed(self) -> Callable[[Account], bool]: ...
    @property
    def get_calendar_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_chat_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_contacts_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_documents_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_files_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_id(self) -> Callable[[Account], str | None]: ...
    @property
    def get_identity(self) -> Callable[[Account], str | None]: ...
    @property
    def get_is_locked(self) -> Callable[[Account], bool]: ...
    @property
    def get_is_temporary(self) -> Callable[[Account], bool]: ...
    @property
    def get_mail_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_maps_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_music_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_photos_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_presentation_identity(self) -> Callable[[Account], str | None]: ...
    @property
    def get_printers_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_provider_icon(self) -> Callable[[Account], str | None]: ...
    @property
    def get_provider_name(self) -> Callable[[Account], str | None]: ...
    @property
    def get_provider_type(self) -> Callable[[Account], str | None]: ...
    @property
    def get_read_later_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_ticketing_disabled(self) -> Callable[[Account], bool]: ...
    @property
    def get_todo_disabled(self) -> Callable[[Account], bool]: ...

class AccountProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Account
):
    """
    :Constructors:

    ::

        AccountProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.AccountProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.AccountProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.AccountProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.AccountProxy

    Object GoaAccountProxy

    Signals from GoaAccount:
      handle-remove (GDBusMethodInvocation) -> gboolean
      handle-ensure-credentials (GDBusMethodInvocation) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        attention_needed: bool
        calendar_disabled: bool
        chat_disabled: bool
        contacts_disabled: bool
        documents_disabled: bool
        files_disabled: bool
        id: str
        identity: str
        is_locked: bool
        is_temporary: bool
        mail_disabled: bool
        maps_disabled: bool
        music_disabled: bool
        photos_disabled: bool
        presentation_identity: str
        printers_disabled: bool
        provider_icon: str
        provider_name: str
        provider_type: str
        read_later_disabled: bool
        ticketing_disabled: bool
        todo_disabled: bool
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> AccountProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        attention_needed: bool = ...,
        calendar_disabled: bool = ...,
        chat_disabled: bool = ...,
        contacts_disabled: bool = ...,
        documents_disabled: bool = ...,
        files_disabled: bool = ...,
        id: str = ...,
        identity: str = ...,
        is_locked: bool = ...,
        is_temporary: bool = ...,
        mail_disabled: bool = ...,
        maps_disabled: bool = ...,
        music_disabled: bool = ...,
        photos_disabled: bool = ...,
        presentation_identity: str = ...,
        printers_disabled: bool = ...,
        provider_icon: str = ...,
        provider_name: str = ...,
        provider_type: str = ...,
        read_later_disabled: bool = ...,
        ticketing_disabled: bool = ...,
        todo_disabled: bool = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> AccountProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> AccountProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> AccountProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> AccountProxy: ...

class AccountProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AccountProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class AccountProxyPrivate(GObject.GPointer): ...

class AccountSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Account):
    """
    :Constructors:

    ::

        AccountSkeleton(**properties)
        new() -> Goa.AccountSkeleton

    Object GoaAccountSkeleton

    Signals from GoaAccount:
      handle-remove (GDBusMethodInvocation) -> gboolean
      handle-ensure-credentials (GDBusMethodInvocation) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        attention_needed: bool
        calendar_disabled: bool
        chat_disabled: bool
        contacts_disabled: bool
        documents_disabled: bool
        files_disabled: bool
        id: str
        identity: str
        is_locked: bool
        is_temporary: bool
        mail_disabled: bool
        maps_disabled: bool
        music_disabled: bool
        photos_disabled: bool
        presentation_identity: str
        printers_disabled: bool
        provider_icon: str
        provider_name: str
        provider_type: str
        read_later_disabled: bool
        ticketing_disabled: bool
        todo_disabled: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> AccountSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        attention_needed: bool = ...,
        calendar_disabled: bool = ...,
        chat_disabled: bool = ...,
        contacts_disabled: bool = ...,
        documents_disabled: bool = ...,
        files_disabled: bool = ...,
        id: str = ...,
        identity: str = ...,
        is_locked: bool = ...,
        is_temporary: bool = ...,
        mail_disabled: bool = ...,
        maps_disabled: bool = ...,
        music_disabled: bool = ...,
        photos_disabled: bool = ...,
        presentation_identity: str = ...,
        printers_disabled: bool = ...,
        provider_icon: str = ...,
        provider_name: str = ...,
        provider_type: str = ...,
        read_later_disabled: bool = ...,
        ticketing_disabled: bool = ...,
        todo_disabled: bool = ...,
    ): ...
    @classmethod
    def new(cls) -> AccountSkeleton: ...

class AccountSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AccountSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class AccountSkeletonPrivate(GObject.GPointer): ...

class Calendar(GObject.GInterface, Protocol):
    """
    Interface GoaCalendar

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class CalendarIface(GObject.GPointer):
    """
    :Constructors:

    ::

        CalendarIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_accept_ssl_errors(self) -> Callable[[Calendar], bool]: ...
    @property
    def get_uri(self) -> Callable[[Calendar], str | None]: ...

class CalendarProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Calendar
):
    """
    :Constructors:

    ::

        CalendarProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.CalendarProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.CalendarProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.CalendarProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.CalendarProxy

    Object GoaCalendarProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        accept_ssl_errors: bool
        uri: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> CalendarProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> CalendarProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> CalendarProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> CalendarProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> CalendarProxy: ...

class CalendarProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CalendarProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class CalendarProxyPrivate(GObject.GPointer): ...

class CalendarSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Calendar):
    """
    :Constructors:

    ::

        CalendarSkeleton(**properties)
        new() -> Goa.CalendarSkeleton

    Object GoaCalendarSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accept_ssl_errors: bool
        uri: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> CalendarSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @classmethod
    def new(cls) -> CalendarSkeleton: ...

class CalendarSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CalendarSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class CalendarSkeletonPrivate(GObject.GPointer): ...

class Chat(GObject.GInterface, Protocol):
    """
    Interface GoaChat

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ChatIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ChatIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class ChatProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Chat
):
    """
    :Constructors:

    ::

        ChatProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ChatProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ChatProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ChatProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ChatProxy

    Object GoaChatProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ChatProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ChatProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ChatProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ChatProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ChatProxy: ...

class ChatProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ChatProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ChatProxyPrivate(GObject.GPointer): ...

class ChatSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Chat):
    """
    :Constructors:

    ::

        ChatSkeleton(**properties)
        new() -> Goa.ChatSkeleton

    Object GoaChatSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ChatSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> ChatSkeleton: ...

class ChatSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ChatSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ChatSkeletonPrivate(GObject.GPointer): ...

class Client(GObject.Object, Gio.AsyncInitable, Gio.Initable):
    """
    :Constructors:

    ::

        Client(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.Client
        new_sync(cancellable:Gio.Cancellable=None) -> Goa.Client

    Object GoaClient

    Signals from GoaClient:
      account-added (GoaObject)
      account-removed (GoaObject)
      account-changed (GoaObject)

    Properties from GoaClient:
      object-manager -> GDBusObjectManager: object manager
        The GDBusObjectManager used by the GoaClient

    Signals from GObject:
      notify (GParam)
    """

    class Props(GObject.Object.Props):
        object_manager: Gio.DBusObjectManager

    @property
    def props(self) -> Props: ...
    def get_accounts(self) -> list[Object]: ...
    def get_manager(self) -> Manager | None: ...
    def get_object_manager(self) -> Gio.DBusObjectManager: ...
    def lookup_by_id(self, id: str) -> Object: ...
    @staticmethod
    def new(
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> Client: ...
    @classmethod
    def new_sync(cls, cancellable: Gio.Cancellable | None = None) -> Client: ...

class ClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Contacts(GObject.GInterface, Protocol):
    """
    Interface GoaContacts

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ContactsIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ContactsIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_accept_ssl_errors(self) -> Callable[[Contacts], bool]: ...
    @property
    def get_uri(self) -> Callable[[Contacts], str | None]: ...

class ContactsProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Contacts
):
    """
    :Constructors:

    ::

        ContactsProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ContactsProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ContactsProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ContactsProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ContactsProxy

    Object GoaContactsProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        accept_ssl_errors: bool
        uri: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ContactsProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ContactsProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ContactsProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ContactsProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ContactsProxy: ...

class ContactsProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContactsProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ContactsProxyPrivate(GObject.GPointer): ...

class ContactsSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Contacts):
    """
    :Constructors:

    ::

        ContactsSkeleton(**properties)
        new() -> Goa.ContactsSkeleton

    Object GoaContactsSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accept_ssl_errors: bool
        uri: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ContactsSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @classmethod
    def new(cls) -> ContactsSkeleton: ...

class ContactsSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContactsSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ContactsSkeletonPrivate(GObject.GPointer): ...

class Documents(GObject.GInterface, Protocol):
    """
    Interface GoaDocuments

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class DocumentsIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentsIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class DocumentsProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Documents
):
    """
    :Constructors:

    ::

        DocumentsProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.DocumentsProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.DocumentsProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.DocumentsProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.DocumentsProxy

    Object GoaDocumentsProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> DocumentsProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> DocumentsProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> DocumentsProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> DocumentsProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> DocumentsProxy: ...

class DocumentsProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentsProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class DocumentsProxyPrivate(GObject.GPointer): ...

class DocumentsSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Documents):
    """
    :Constructors:

    ::

        DocumentsSkeleton(**properties)
        new() -> Goa.DocumentsSkeleton

    Object GoaDocumentsSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> DocumentsSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> DocumentsSkeleton: ...

class DocumentsSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentsSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class DocumentsSkeletonPrivate(GObject.GPointer): ...

class Exchange(GObject.GInterface, Protocol):
    """
    Interface GoaExchange

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ExchangeIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ExchangeIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_accept_ssl_errors(self) -> Callable[[Exchange], bool]: ...
    @property
    def get_host(self) -> Callable[[Exchange], str | None]: ...

class ExchangeProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Exchange
):
    """
    :Constructors:

    ::

        ExchangeProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ExchangeProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ExchangeProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ExchangeProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ExchangeProxy

    Object GoaExchangeProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        accept_ssl_errors: bool
        host: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ExchangeProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        accept_ssl_errors: bool = ...,
        host: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ExchangeProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ExchangeProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ExchangeProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ExchangeProxy: ...

class ExchangeProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExchangeProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ExchangeProxyPrivate(GObject.GPointer): ...

class ExchangeSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Exchange):
    """
    :Constructors:

    ::

        ExchangeSkeleton(**properties)
        new() -> Goa.ExchangeSkeleton

    Object GoaExchangeSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accept_ssl_errors: bool
        host: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ExchangeSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        host: str = ...,
    ): ...
    @classmethod
    def new(cls) -> ExchangeSkeleton: ...

class ExchangeSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExchangeSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ExchangeSkeletonPrivate(GObject.GPointer): ...

class Files(GObject.GInterface, Protocol):
    """
    Interface GoaFiles

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class FilesIface(GObject.GPointer):
    """
    :Constructors:

    ::

        FilesIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_accept_ssl_errors(self) -> Callable[[Files], bool]: ...
    @property
    def get_uri(self) -> Callable[[Files], str | None]: ...

class FilesProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Files
):
    """
    :Constructors:

    ::

        FilesProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.FilesProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.FilesProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.FilesProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.FilesProxy

    Object GoaFilesProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        accept_ssl_errors: bool
        uri: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> FilesProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> FilesProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> FilesProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> FilesProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> FilesProxy: ...

class FilesProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilesProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class FilesProxyPrivate(GObject.GPointer): ...

class FilesSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Files):
    """
    :Constructors:

    ::

        FilesSkeleton(**properties)
        new() -> Goa.FilesSkeleton

    Object GoaFilesSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accept_ssl_errors: bool
        uri: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> FilesSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accept_ssl_errors: bool = ...,
        uri: str = ...,
    ): ...
    @classmethod
    def new(cls) -> FilesSkeleton: ...

class FilesSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FilesSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class FilesSkeletonPrivate(GObject.GPointer): ...

class Mail(GObject.GInterface, Protocol):
    """
    Interface GoaMail

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MailIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MailIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_email_address(self) -> Callable[[Mail], str | None]: ...
    @property
    def get_imap_accept_ssl_errors(self) -> Callable[[Mail], bool]: ...
    @property
    def get_imap_host(self) -> Callable[[Mail], str | None]: ...
    @property
    def get_imap_supported(self) -> Callable[[Mail], bool]: ...
    @property
    def get_imap_use_ssl(self) -> Callable[[Mail], bool]: ...
    @property
    def get_imap_use_tls(self) -> Callable[[Mail], bool]: ...
    @property
    def get_imap_user_name(self) -> Callable[[Mail], str | None]: ...
    @property
    def get_name(self) -> Callable[[Mail], str | None]: ...
    @property
    def get_smtp_accept_ssl_errors(self) -> Callable[[Mail], bool]: ...
    @property
    def get_smtp_auth_login(self) -> Callable[[Mail], bool]: ...
    @property
    def get_smtp_auth_plain(self) -> Callable[[Mail], bool]: ...
    @property
    def get_smtp_auth_xoauth2(self) -> Callable[[Mail], bool]: ...

class MailProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Mail
):
    """
    :Constructors:

    ::

        MailProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MailProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MailProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MailProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MailProxy

    Object GoaMailProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        email_address: str
        imap_accept_ssl_errors: bool
        imap_host: str
        imap_supported: bool
        imap_use_ssl: bool
        imap_use_tls: bool
        imap_user_name: str
        name: str
        smtp_accept_ssl_errors: bool
        smtp_auth_login: bool
        smtp_auth_plain: bool
        smtp_auth_xoauth2: bool
        smtp_host: str
        smtp_supported: bool
        smtp_use_auth: bool
        smtp_use_ssl: bool
        smtp_use_tls: bool
        smtp_user_name: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> MailProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        email_address: str = ...,
        imap_accept_ssl_errors: bool = ...,
        imap_host: str = ...,
        imap_supported: bool = ...,
        imap_use_ssl: bool = ...,
        imap_use_tls: bool = ...,
        imap_user_name: str = ...,
        name: str = ...,
        smtp_accept_ssl_errors: bool = ...,
        smtp_auth_login: bool = ...,
        smtp_auth_plain: bool = ...,
        smtp_auth_xoauth2: bool = ...,
        smtp_host: str = ...,
        smtp_supported: bool = ...,
        smtp_use_auth: bool = ...,
        smtp_use_ssl: bool = ...,
        smtp_use_tls: bool = ...,
        smtp_user_name: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> MailProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MailProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MailProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MailProxy: ...

class MailProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MailProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class MailProxyPrivate(GObject.GPointer): ...

class MailSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Mail):
    """
    :Constructors:

    ::

        MailSkeleton(**properties)
        new() -> Goa.MailSkeleton

    Object GoaMailSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        email_address: str
        imap_accept_ssl_errors: bool
        imap_host: str
        imap_supported: bool
        imap_use_ssl: bool
        imap_use_tls: bool
        imap_user_name: str
        name: str
        smtp_accept_ssl_errors: bool
        smtp_auth_login: bool
        smtp_auth_plain: bool
        smtp_auth_xoauth2: bool
        smtp_host: str
        smtp_supported: bool
        smtp_use_auth: bool
        smtp_use_ssl: bool
        smtp_use_tls: bool
        smtp_user_name: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> MailSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        email_address: str = ...,
        imap_accept_ssl_errors: bool = ...,
        imap_host: str = ...,
        imap_supported: bool = ...,
        imap_use_ssl: bool = ...,
        imap_use_tls: bool = ...,
        imap_user_name: str = ...,
        name: str = ...,
        smtp_accept_ssl_errors: bool = ...,
        smtp_auth_login: bool = ...,
        smtp_auth_plain: bool = ...,
        smtp_auth_xoauth2: bool = ...,
        smtp_host: str = ...,
        smtp_supported: bool = ...,
        smtp_use_auth: bool = ...,
        smtp_use_ssl: bool = ...,
        smtp_use_tls: bool = ...,
        smtp_user_name: str = ...,
    ): ...
    @classmethod
    def new(cls) -> MailSkeleton: ...

class MailSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MailSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class MailSkeletonPrivate(GObject.GPointer): ...

class Manager(GObject.GInterface, Protocol):
    """
    Interface GoaManager

    Signals from GObject:
      notify (GParam)
    """

    def call_add_account(
        self,
        arg_provider: str,
        arg_identity: str,
        arg_presentation_identity: str,
        arg_credentials: GLib.Variant,
        arg_details: GLib.Variant,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_add_account_finish(self, res: Gio.AsyncResult) -> tuple[bool, str]: ...
    def call_add_account_sync(
        self,
        arg_provider: str,
        arg_identity: str,
        arg_presentation_identity: str,
        arg_credentials: GLib.Variant,
        arg_details: GLib.Variant,
        cancellable: Gio.Cancellable | None = None,
    ) -> tuple[bool, str]: ...
    def call_is_supported_provider(
        self,
        arg_provider_type: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_is_supported_provider_finish(
        self, res: Gio.AsyncResult
    ) -> tuple[bool, bool]: ...
    def call_is_supported_provider_sync(
        self, arg_provider_type: str, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, bool]: ...
    def complete_add_account(
        self, invocation: Gio.DBusMethodInvocation, account_object_path: str
    ) -> None: ...
    def complete_is_supported_provider(
        self, invocation: Gio.DBusMethodInvocation, is_supported: bool
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ManagerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_add_account(
        self,
    ) -> Callable[
        [Manager, Gio.DBusMethodInvocation, str, str, str, GLib.Variant, GLib.Variant],
        bool,
    ]: ...
    @property
    def handle_is_supported_provider(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation, str], bool]: ...

class ManagerProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Manager
):
    """
    :Constructors:

    ::

        ManagerProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ManagerProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ManagerProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ManagerProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ManagerProxy

    Object GoaManagerProxy

    Signals from GoaManager:
      handle-add-account (GDBusMethodInvocation, gchararray, gchararray, gchararray, GVariant, GVariant) -> gboolean
      handle-is-supported-provider (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ManagerProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ManagerProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ManagerProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ManagerProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ManagerProxy: ...

class ManagerProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ManagerProxyPrivate(GObject.GPointer): ...

class ManagerSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Manager):
    """
    :Constructors:

    ::

        ManagerSkeleton(**properties)
        new() -> Goa.ManagerSkeleton

    Object GoaManagerSkeleton

    Signals from GoaManager:
      handle-add-account (GDBusMethodInvocation, gchararray, gchararray, gchararray, GVariant, GVariant) -> gboolean
      handle-is-supported-provider (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ManagerSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> ManagerSkeleton: ...

class ManagerSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ManagerSkeletonPrivate(GObject.GPointer): ...

class Maps(GObject.GInterface, Protocol):
    """
    Interface GoaMaps

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MapsIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MapsIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class MapsProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Maps
):
    """
    :Constructors:

    ::

        MapsProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MapsProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MapsProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MapsProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MapsProxy

    Object GoaMapsProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> MapsProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> MapsProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MapsProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MapsProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MapsProxy: ...

class MapsProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapsProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class MapsProxyPrivate(GObject.GPointer): ...

class MapsSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Maps):
    """
    :Constructors:

    ::

        MapsSkeleton(**properties)
        new() -> Goa.MapsSkeleton

    Object GoaMapsSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> MapsSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> MapsSkeleton: ...

class MapsSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MapsSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class MapsSkeletonPrivate(GObject.GPointer): ...

class MediaServer(GObject.GInterface, Protocol):
    """
    Interface GoaMediaServer

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MediaServerIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaServerIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_dlna_supported(self) -> Callable[[MediaServer], bool]: ...
    @property
    def get_udn(self) -> Callable[[MediaServer], str | None]: ...

class MediaServerProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, MediaServer
):
    """
    :Constructors:

    ::

        MediaServerProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MediaServerProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MediaServerProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MediaServerProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MediaServerProxy

    Object GoaMediaServerProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        dlna_supported: bool
        udn: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> MediaServerProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        dlna_supported: bool = ...,
        udn: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> MediaServerProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MediaServerProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MediaServerProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MediaServerProxy: ...

class MediaServerProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaServerProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class MediaServerProxyPrivate(GObject.GPointer): ...

class MediaServerSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, MediaServer):
    """
    :Constructors:

    ::

        MediaServerSkeleton(**properties)
        new() -> Goa.MediaServerSkeleton

    Object GoaMediaServerSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        dlna_supported: bool
        udn: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> MediaServerSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        dlna_supported: bool = ...,
        udn: str = ...,
    ): ...
    @classmethod
    def new(cls) -> MediaServerSkeleton: ...

class MediaServerSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MediaServerSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class MediaServerSkeletonPrivate(GObject.GPointer): ...

class Music(GObject.GInterface, Protocol):
    """
    Interface GoaMusic

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class MusicIface(GObject.GPointer):
    """
    :Constructors:

    ::

        MusicIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class MusicProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Music
):
    """
    :Constructors:

    ::

        MusicProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.MusicProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.MusicProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MusicProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.MusicProxy

    Object GoaMusicProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> MusicProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> MusicProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> MusicProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MusicProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> MusicProxy: ...

class MusicProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MusicProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class MusicProxyPrivate(GObject.GPointer): ...

class MusicSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Music):
    """
    :Constructors:

    ::

        MusicSkeleton(**properties)
        new() -> Goa.MusicSkeleton

    Object GoaMusicSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> MusicSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> MusicSkeleton: ...

class MusicSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MusicSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class MusicSkeletonPrivate(GObject.GPointer): ...

class OAuth2Based(GObject.GInterface, Protocol):
    """
    Interface GoaOAuth2Based

    Signals from GObject:
      notify (GParam)
    """

    def call_get_access_token(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_access_token_finish(
        self, res: Gio.AsyncResult
    ) -> tuple[bool, str, int]: ...
    def call_get_access_token_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str, int]: ...
    def complete_get_access_token(
        self, invocation: Gio.DBusMethodInvocation, access_token: str, expires_in: int
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class OAuth2BasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2BasedIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_get_access_token(
        self,
    ) -> Callable[[OAuth2Based, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_client_id(self) -> Callable[[OAuth2Based], str | None]: ...
    @property
    def get_client_secret(self) -> Callable[[OAuth2Based], str | None]: ...

class OAuth2BasedProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, OAuth2Based
):
    """
    :Constructors:

    ::

        OAuth2BasedProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.OAuth2BasedProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.OAuth2BasedProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuth2BasedProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuth2BasedProxy

    Object GoaOAuth2BasedProxy

    Signals from GoaOAuth2Based:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        client_id: str
        client_secret: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> OAuth2BasedProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        client_id: str = ...,
        client_secret: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> OAuth2BasedProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> OAuth2BasedProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> OAuth2BasedProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> OAuth2BasedProxy: ...

class OAuth2BasedProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2BasedProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class OAuth2BasedProxyPrivate(GObject.GPointer): ...

class OAuth2BasedSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, OAuth2Based):
    """
    :Constructors:

    ::

        OAuth2BasedSkeleton(**properties)
        new() -> Goa.OAuth2BasedSkeleton

    Object GoaOAuth2BasedSkeleton

    Signals from GoaOAuth2Based:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        client_id: str
        client_secret: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> OAuth2BasedSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        client_id: str = ...,
        client_secret: str = ...,
    ): ...
    @classmethod
    def new(cls) -> OAuth2BasedSkeleton: ...

class OAuth2BasedSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2BasedSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class OAuth2BasedSkeletonPrivate(GObject.GPointer): ...

class OAuthBased(GObject.GInterface, Protocol):
    """
    Interface GoaOAuthBased

    Signals from GObject:
      notify (GParam)
    """

    def call_get_access_token(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_access_token_finish(
        self, res: Gio.AsyncResult
    ) -> tuple[bool, str, str, int]: ...
    def call_get_access_token_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str, str, int]: ...
    def complete_get_access_token(
        self,
        invocation: Gio.DBusMethodInvocation,
        access_token: str,
        access_token_secret: str,
        expires_in: int,
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class OAuthBasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuthBasedIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_get_access_token(
        self,
    ) -> Callable[[OAuthBased, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_consumer_key(self) -> Callable[[OAuthBased], str | None]: ...
    @property
    def get_consumer_secret(self) -> Callable[[OAuthBased], str | None]: ...

class OAuthBasedProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, OAuthBased
):
    """
    :Constructors:

    ::

        OAuthBasedProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.OAuthBasedProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.OAuthBasedProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuthBasedProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.OAuthBasedProxy

    Object GoaOAuthBasedProxy

    Signals from GoaOAuthBased:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        consumer_key: str
        consumer_secret: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> OAuthBasedProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        consumer_key: str = ...,
        consumer_secret: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> OAuthBasedProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> OAuthBasedProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> OAuthBasedProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> OAuthBasedProxy: ...

class OAuthBasedProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuthBasedProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class OAuthBasedProxyPrivate(GObject.GPointer): ...

class OAuthBasedSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, OAuthBased):
    """
    :Constructors:

    ::

        OAuthBasedSkeleton(**properties)
        new() -> Goa.OAuthBasedSkeleton

    Object GoaOAuthBasedSkeleton

    Signals from GoaOAuthBased:
      handle-get-access-token (GDBusMethodInvocation) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        consumer_key: str
        consumer_secret: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> OAuthBasedSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        consumer_key: str = ...,
        consumer_secret: str = ...,
    ): ...
    @classmethod
    def new(cls) -> OAuthBasedSkeleton: ...

class OAuthBasedSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuthBasedSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class OAuthBasedSkeletonPrivate(GObject.GPointer): ...

class Object(GObject.GInterface, Protocol):
    """
    Interface GoaObject

    Signals from GObject:
      notify (GParam)
    """

    def get_account(self) -> Account | None: ...
    def get_calendar(self) -> Calendar | None: ...
    def get_chat(self) -> Chat | None: ...
    def get_contacts(self) -> Contacts | None: ...
    def get_documents(self) -> Documents | None: ...
    def get_exchange(self) -> Exchange | None: ...
    def get_files(self) -> Files | None: ...
    def get_mail(self) -> Mail | None: ...
    def get_manager(self) -> Manager | None: ...
    def get_maps(self) -> Maps | None: ...
    def get_media_server(self) -> MediaServer | None: ...
    def get_music(self) -> Music | None: ...
    def get_oauth2_based(self) -> OAuth2Based | None: ...
    def get_oauth_based(self) -> OAuthBased | None: ...
    def get_password_based(self) -> PasswordBased | None: ...
    def get_photos(self) -> Photos | None: ...
    def get_printers(self) -> Printers | None: ...
    def get_read_later(self) -> ReadLater | None: ...
    def get_ticketing(self) -> Ticketing | None: ...
    def get_todo(self) -> Todo | None: ...

class ObjectIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class ObjectManagerClient(
    Gio.DBusObjectManagerClient, Gio.AsyncInitable, Gio.DBusObjectManager, Gio.Initable
):
    """
    :Constructors:

    ::

        ObjectManagerClient(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ObjectManagerClient
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ObjectManagerClient
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ObjectManagerClient
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ObjectManagerClient

    Object GoaObjectManagerClient

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GDBusObjectManagerClient:
      interface-proxy-signal (GDBusObjectProxy, GDBusProxy, gchararray, gchararray, GVariant)
      interface-proxy-properties-changed (GDBusObjectProxy, GDBusProxy, GVariant, GStrv)

    Properties from GDBusObjectManagerClient:
      bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      connection -> GDBusConnection: Connection
        The connection to use
      flags -> GDBusObjectManagerClientFlags: Flags
        Flags for the proxy manager
      object-path -> gchararray: Object Path
        The object path of the control object
      name -> gchararray: Name
        Name that the manager is for
      name-owner -> gchararray: Name Owner
        The owner of the name we are watching
      get-proxy-type-func -> gpointer: GDBusProxyTypeFunc Function Pointer
        The GDBusProxyTypeFunc pointer to use
      get-proxy-type-user-data -> gpointer: GDBusProxyTypeFunc User Data
        The GDBusProxyTypeFunc user_data
      get-proxy-type-destroy-notify -> gpointer: GDBusProxyTypeFunc user data free function
        The GDBusProxyTypeFunc user data free function

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.DBusObjectManagerClient.Props):
        connection: Gio.DBusConnection
        flags: Gio.DBusObjectManagerClientFlags
        get_proxy_type_destroy_notify: None
        get_proxy_type_func: None
        get_proxy_type_user_data: None
        name: str
        name_owner: str | None
        object_path: str
        bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusObjectManagerClient: ...
    @property
    def priv(self) -> ObjectManagerClientPrivate: ...
    def __init__(
        self,
        bus_type: Gio.BusType = ...,
        connection: Gio.DBusConnection = ...,
        flags: Gio.DBusObjectManagerClientFlags = ...,
        get_proxy_type_destroy_notify: None = ...,
        get_proxy_type_func: None = ...,
        get_proxy_type_user_data: None = ...,
        name: str = ...,
        object_path: str = ...,
    ): ...
    @staticmethod
    def get_proxy_type(
        manager: Gio.DBusObjectManagerClient,
        object_path: str,
        interface_name: str | None,
        user_data: None,
    ) -> type: ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusObjectManagerClientFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ObjectManagerClient: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ObjectManagerClient: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusObjectManagerClientFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ObjectManagerClient: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusObjectManagerClientFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ObjectManagerClient: ...

class ObjectManagerClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectManagerClientClass()
    """
    @property
    def parent_class(self) -> Gio.DBusObjectManagerClientClass: ...

class ObjectManagerClientPrivate(GObject.GPointer): ...

class ObjectProxy(Gio.DBusObjectProxy, Gio.DBusObject, Object):
    """
    :Constructors:

    ::

        ObjectProxy(**properties)
        new(connection:Gio.DBusConnection, object_path:str) -> Goa.ObjectProxy

    Object GoaObjectProxy

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Properties from GDBusObjectProxy:
      g-object-path -> gchararray: Object Path
        The object path of the proxy
      g-connection -> GDBusConnection: Connection
        The connection of the proxy

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusObjectProxy.Props):
        g_connection: Gio.DBusConnection
        g_object_path: str
        account: Account | None
        calendar: Calendar | None
        chat: Chat | None
        contacts: Contacts | None
        documents: Documents | None
        exchange: Exchange | None
        files: Files | None
        mail: Mail | None
        manager: Manager | None
        maps: Maps | None
        media_server: MediaServer | None
        music: Music | None
        oauth_based: OAuthBased | None
        oauth2_based: OAuth2Based | None
        password_based: PasswordBased | None
        photos: Photos | None
        printers: Printers | None
        read_later: ReadLater | None
        ticketing: Ticketing | None
        todo: Todo | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusObjectProxy: ...
    @property
    def priv(self) -> ObjectProxyPrivate: ...
    def __init__(
        self,
        g_connection: Gio.DBusConnection = ...,
        g_object_path: str = ...,
        account: Account = ...,
        calendar: Calendar = ...,
        chat: Chat = ...,
        contacts: Contacts = ...,
        documents: Documents = ...,
        exchange: Exchange = ...,
        files: Files = ...,
        mail: Mail = ...,
        manager: Manager = ...,
        maps: Maps = ...,
        media_server: MediaServer = ...,
        music: Music = ...,
        oauth_based: OAuthBased = ...,
        oauth2_based: OAuth2Based = ...,
        password_based: PasswordBased = ...,
        photos: Photos = ...,
        printers: Printers = ...,
        read_later: ReadLater = ...,
        ticketing: Ticketing = ...,
        todo: Todo = ...,
    ): ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection, object_path: str) -> ObjectProxy: ...

class ObjectProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusObjectProxyClass: ...

class ObjectProxyPrivate(GObject.GPointer): ...

class ObjectSkeleton(Gio.DBusObjectSkeleton, Gio.DBusObject, Object):
    """
    :Constructors:

    ::

        ObjectSkeleton(**properties)
        new(object_path:str) -> Goa.ObjectSkeleton

    Object GoaObjectSkeleton

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GDBusObjectSkeleton:
      authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean

    Properties from GDBusObjectSkeleton:
      g-object-path -> gchararray: Object Path
        The object path where the object is exported

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusObjectSkeleton.Props):
        g_object_path: str
        account: Account | None
        calendar: Calendar | None
        chat: Chat | None
        contacts: Contacts | None
        documents: Documents | None
        exchange: Exchange | None
        files: Files | None
        mail: Mail | None
        manager: Manager | None
        maps: Maps | None
        media_server: MediaServer | None
        music: Music | None
        oauth_based: OAuthBased | None
        oauth2_based: OAuth2Based | None
        password_based: PasswordBased | None
        photos: Photos | None
        printers: Printers | None
        read_later: ReadLater | None
        ticketing: Ticketing | None
        todo: Todo | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusObjectSkeleton: ...
    @property
    def priv(self) -> ObjectSkeletonPrivate: ...
    def __init__(
        self,
        g_object_path: str = ...,
        account: Account = ...,
        calendar: Calendar = ...,
        chat: Chat = ...,
        contacts: Contacts = ...,
        documents: Documents = ...,
        exchange: Exchange = ...,
        files: Files = ...,
        mail: Mail = ...,
        manager: Manager = ...,
        maps: Maps = ...,
        media_server: MediaServer = ...,
        music: Music = ...,
        oauth_based: OAuthBased = ...,
        oauth2_based: OAuth2Based = ...,
        password_based: PasswordBased = ...,
        photos: Photos = ...,
        printers: Printers = ...,
        read_later: ReadLater = ...,
        ticketing: Ticketing = ...,
        todo: Todo = ...,
    ): ...
    @classmethod
    def new(cls, object_path: str) -> ObjectSkeleton: ...
    def set_account(self, interface_: Account | None = None) -> None: ...
    def set_calendar(self, interface_: Calendar | None = None) -> None: ...
    def set_chat(self, interface_: Chat | None = None) -> None: ...
    def set_contacts(self, interface_: Contacts | None = None) -> None: ...
    def set_documents(self, interface_: Documents | None = None) -> None: ...
    def set_exchange(self, interface_: Exchange | None = None) -> None: ...
    def set_files(self, interface_: Files | None = None) -> None: ...
    def set_mail(self, interface_: Mail | None = None) -> None: ...
    def set_manager(self, interface_: Manager | None = None) -> None: ...
    def set_maps(self, interface_: Maps | None = None) -> None: ...
    def set_media_server(self, interface_: MediaServer | None = None) -> None: ...
    def set_music(self, interface_: Music | None = None) -> None: ...
    def set_oauth2_based(self, interface_: OAuth2Based | None = None) -> None: ...
    def set_oauth_based(self, interface_: OAuthBased | None = None) -> None: ...
    def set_password_based(self, interface_: PasswordBased | None = None) -> None: ...
    def set_photos(self, interface_: Photos | None = None) -> None: ...
    def set_printers(self, interface_: Printers | None = None) -> None: ...
    def set_read_later(self, interface_: ReadLater | None = None) -> None: ...
    def set_ticketing(self, interface_: Ticketing | None = None) -> None: ...
    def set_todo(self, interface_: Todo | None = None) -> None: ...

class ObjectSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusObjectSkeletonClass: ...

class ObjectSkeletonPrivate(GObject.GPointer): ...

class PasswordBased(GObject.GInterface, Protocol):
    """
    Interface GoaPasswordBased

    Signals from GObject:
      notify (GParam)
    """

    def call_get_password(
        self,
        arg_id: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_password_finish(self, res: Gio.AsyncResult) -> tuple[bool, str]: ...
    def call_get_password_sync(
        self, arg_id: str, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str]: ...
    def complete_get_password(
        self, invocation: Gio.DBusMethodInvocation, password: str
    ) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class PasswordBasedIface(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordBasedIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_get_password(
        self,
    ) -> Callable[[PasswordBased, Gio.DBusMethodInvocation, str], bool]: ...

class PasswordBasedProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, PasswordBased
):
    """
    :Constructors:

    ::

        PasswordBasedProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.PasswordBasedProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.PasswordBasedProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PasswordBasedProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PasswordBasedProxy

    Object GoaPasswordBasedProxy

    Signals from GoaPasswordBased:
      handle-get-password (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> PasswordBasedProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> PasswordBasedProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> PasswordBasedProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> PasswordBasedProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> PasswordBasedProxy: ...

class PasswordBasedProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordBasedProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class PasswordBasedProxyPrivate(GObject.GPointer): ...

class PasswordBasedSkeleton(
    Gio.DBusInterfaceSkeleton, Gio.DBusInterface, PasswordBased
):
    """
    :Constructors:

    ::

        PasswordBasedSkeleton(**properties)
        new() -> Goa.PasswordBasedSkeleton

    Object GoaPasswordBasedSkeleton

    Signals from GoaPasswordBased:
      handle-get-password (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> PasswordBasedSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> PasswordBasedSkeleton: ...

class PasswordBasedSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordBasedSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class PasswordBasedSkeletonPrivate(GObject.GPointer): ...

class Photos(GObject.GInterface, Protocol):
    """
    Interface GoaPhotos

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class PhotosIface(GObject.GPointer):
    """
    :Constructors:

    ::

        PhotosIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class PhotosProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Photos
):
    """
    :Constructors:

    ::

        PhotosProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.PhotosProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.PhotosProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PhotosProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PhotosProxy

    Object GoaPhotosProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> PhotosProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> PhotosProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> PhotosProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> PhotosProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> PhotosProxy: ...

class PhotosProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PhotosProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class PhotosProxyPrivate(GObject.GPointer): ...

class PhotosSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Photos):
    """
    :Constructors:

    ::

        PhotosSkeleton(**properties)
        new() -> Goa.PhotosSkeleton

    Object GoaPhotosSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> PhotosSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> PhotosSkeleton: ...

class PhotosSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PhotosSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class PhotosSkeletonPrivate(GObject.GPointer): ...

class Printers(GObject.GInterface, Protocol):
    """
    Interface GoaPrinters

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class PrintersIface(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintersIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class PrintersProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Printers
):
    """
    :Constructors:

    ::

        PrintersProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.PrintersProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.PrintersProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PrintersProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.PrintersProxy

    Object GoaPrintersProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> PrintersProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> PrintersProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> PrintersProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> PrintersProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> PrintersProxy: ...

class PrintersProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintersProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class PrintersProxyPrivate(GObject.GPointer): ...

class PrintersSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Printers):
    """
    :Constructors:

    ::

        PrintersSkeleton(**properties)
        new() -> Goa.PrintersSkeleton

    Object GoaPrintersSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> PrintersSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> PrintersSkeleton: ...

class PrintersSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PrintersSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class PrintersSkeletonPrivate(GObject.GPointer): ...

class ReadLater(GObject.GInterface, Protocol):
    """
    Interface GoaReadLater

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ReadLaterIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ReadLaterIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class ReadLaterProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, ReadLater
):
    """
    :Constructors:

    ::

        ReadLaterProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.ReadLaterProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.ReadLaterProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ReadLaterProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.ReadLaterProxy

    Object GoaReadLaterProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ReadLaterProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ReadLaterProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ReadLaterProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ReadLaterProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ReadLaterProxy: ...

class ReadLaterProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ReadLaterProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ReadLaterProxyPrivate(GObject.GPointer): ...

class ReadLaterSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, ReadLater):
    """
    :Constructors:

    ::

        ReadLaterSkeleton(**properties)
        new() -> Goa.ReadLaterSkeleton

    Object GoaReadLaterSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ReadLaterSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> ReadLaterSkeleton: ...

class ReadLaterSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ReadLaterSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ReadLaterSkeletonPrivate(GObject.GPointer): ...

class Ticketing(GObject.GInterface, Protocol):
    """
    Interface GoaTicketing

    Signals from GObject:
      notify (GParam)
    """

    def call_get_ticket(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_ticket_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_get_ticket_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> bool: ...
    def complete_get_ticket(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class TicketingIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TicketingIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_get_ticket(
        self,
    ) -> Callable[[Ticketing, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_details(self) -> Callable[[Ticketing], GLib.Variant | None]: ...

class TicketingProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Ticketing
):
    """
    :Constructors:

    ::

        TicketingProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.TicketingProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.TicketingProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TicketingProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TicketingProxy

    Object GoaTicketingProxy

    Signals from GoaTicketing:
      handle-get-ticket (GDBusMethodInvocation) -> gboolean

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        details: GLib.Variant
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> TicketingProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
        details: GLib.Variant = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> TicketingProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> TicketingProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> TicketingProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> TicketingProxy: ...

class TicketingProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TicketingProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class TicketingProxyPrivate(GObject.GPointer): ...

class TicketingSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Ticketing):
    """
    :Constructors:

    ::

        TicketingSkeleton(**properties)
        new() -> Goa.TicketingSkeleton

    Object GoaTicketingSkeleton

    Signals from GoaTicketing:
      handle-get-ticket (GDBusMethodInvocation) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        details: GLib.Variant

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> TicketingSkeletonPrivate: ...
    def __init__(
        self, g_flags: Gio.DBusInterfaceSkeletonFlags = ..., details: GLib.Variant = ...
    ): ...
    @classmethod
    def new(cls) -> TicketingSkeleton: ...

class TicketingSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TicketingSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class TicketingSkeletonPrivate(GObject.GPointer): ...

class Todo(GObject.GInterface, Protocol):
    """
    Interface GoaTodo

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class TodoIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TodoIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...

class TodoProxy(
    Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable, Todo
):
    """
    :Constructors:

    ::

        TodoProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Goa.TodoProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Goa.TodoProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TodoProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Goa.TodoProxy

    Object GoaTodoProxy

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
        The connection the proxy is for
      g-bus-type -> GBusType: Bus Type
        The bus to connect to, if any
      g-name -> gchararray: g-name
        The well-known or unique name that the proxy is for
      g-name-owner -> gchararray: g-name-owner
        The unique name for the owner
      g-flags -> GDBusProxyFlags: g-flags
        Flags for the proxy
      g-object-path -> gchararray: g-object-path
        The object path the proxy is for
      g-interface-name -> gchararray: g-interface-name
        The D-Bus interface name the proxy is for
      g-default-timeout -> gint: Default Timeout
        Timeout for remote method invocation
      g-interface-info -> GDBusInterfaceInfo: Interface Information
        Interface Information

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> TodoProxyPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> TodoProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> TodoProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> TodoProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> TodoProxy: ...

class TodoProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TodoProxyClass()
    """
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class TodoProxyPrivate(GObject.GPointer): ...

class TodoSkeleton(Gio.DBusInterfaceSkeleton, Gio.DBusInterface, Todo):
    """
    :Constructors:

    ::

        TodoSkeleton(**properties)
        new() -> Goa.TodoSkeleton

    Object GoaTodoSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> TodoSkeletonPrivate: ...
    def __init__(self, g_flags: Gio.DBusInterfaceSkeletonFlags = ...): ...
    @classmethod
    def new(cls) -> TodoSkeleton: ...

class TodoSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TodoSkeletonClass()
    """
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class TodoSkeletonPrivate(GObject.GPointer): ...

class Error(GObject.GEnum):
    ACCOUNT_EXISTS = 3
    DIALOG_DISMISSED = 2
    FAILED = 0
    NOT_AUTHORIZED = 4
    NOT_SUPPORTED = 1
    SSL = 5
    @staticmethod
    def quark() -> int: ...
