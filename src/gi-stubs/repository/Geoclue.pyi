from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

_lock = ...  # FIXME Constant
_namespace: str = "Geoclue"
_version: str = "2.0"

def client_interface_info() -> Gio.DBusInterfaceInfo: ...
def client_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def location_interface_info() -> Gio.DBusInterfaceInfo: ...
def location_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...
def manager_interface_info() -> Gio.DBusInterfaceInfo: ...
def manager_override_properties(
    klass: GObject.ObjectClass, property_id_begin: int
) -> int: ...

class Client(GObject.GInterface):
    """
    Interface GClueClient

    Signals from GObject:
      notify (GParam)
    """

    def call_start(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_start_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_start_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def call_stop(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_stop_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_stop_sync(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def complete_start(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_stop(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def emit_location_updated(self, arg_old: str, arg_new: str) -> None: ...
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class ClientIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientIface()
    """

    parent_iface: GObject.TypeInterface = ...
    handle_start: Callable[[Client, Gio.DBusMethodInvocation], bool] = ...
    handle_stop: Callable[[Client, Gio.DBusMethodInvocation], bool] = ...
    get_active: Callable[[Client], bool] = ...
    get_desktop_id: Callable[[Client], Optional[str]] = ...
    get_distance_threshold: Callable[[Client], int] = ...
    get_location: Callable[[Client], Optional[str]] = ...
    get_requested_accuracy_level: Callable[[Client], int] = ...
    get_time_threshold: Callable[[Client], int] = ...
    location_updated: Callable[[Client, str, str], None] = ...

class ClientProxy(
    Gio.DBusProxy, Client, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    """
    :Constructors:

    ::

        ClientProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Geoclue.ClientProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Geoclue.ClientProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ClientProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ClientProxy

    Object GClueClientProxy

    Signals from GClueClient:
      handle-start (GDBusMethodInvocation) -> gboolean
      handle-stop (GDBusMethodInvocation) -> gboolean
      location-updated (gchararray, gchararray)

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

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        active: bool
        desktop_id: str
        distance_threshold: int
        location: str
        requested_accuracy_level: int
        time_threshold: int
        g_bus_type: Gio.BusType
    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ClientProxyPrivate = ...
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
        active: bool = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        location: str = ...,
        requested_accuracy_level: int = ...,
        time_threshold: int = ...,
    ): ...
    @staticmethod
    def create(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_finish(result: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def create_full(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        flags: ClientProxyCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_full_finish(result: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def create_full_sync(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        flags: ClientProxyCreateFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ClientProxy: ...
    @staticmethod
    def create_sync(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ClientProxy: ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ClientProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ClientProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ClientProxy: ...

class ClientProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ClientProxyPrivate(GObject.GPointer): ...

class ClientSkeleton(Gio.DBusInterfaceSkeleton, Client, Gio.DBusInterface):
    """
    :Constructors:

    ::

        ClientSkeleton(**properties)
        new() -> Geoclue.ClientSkeleton

    Object GClueClientSkeleton

    Signals from GClueClient:
      handle-start (GDBusMethodInvocation) -> gboolean
      handle-stop (GDBusMethodInvocation) -> gboolean
      location-updated (gchararray, gchararray)

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_flags: Gio.DBusInterfaceSkeletonFlags
        active: bool
        desktop_id: str
        distance_threshold: int
        location: str
        requested_accuracy_level: int
        time_threshold: int
    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ClientSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        active: bool = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        location: str = ...,
        requested_accuracy_level: int = ...,
        time_threshold: int = ...,
    ): ...
    @classmethod
    def new(cls) -> ClientSkeleton: ...

class ClientSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ClientSkeletonPrivate(GObject.GPointer): ...

class Location(GObject.GInterface):
    """
    Interface GClueLocation

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class LocationIface(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationIface()
    """

    parent_iface: GObject.TypeInterface = ...
    get_accuracy: Callable[[Location], float] = ...
    get_altitude: Callable[[Location], float] = ...
    get_description: Callable[[Location], Optional[str]] = ...
    get_heading: Callable[[Location], float] = ...
    get_latitude: Callable[[Location], float] = ...
    get_longitude: Callable[[Location], float] = ...
    get_speed: Callable[[Location], float] = ...
    get_timestamp: Callable[[Location], Optional[GLib.Variant]] = ...

class LocationProxy(
    Gio.DBusProxy, Location, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    """
    :Constructors:

    ::

        LocationProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Geoclue.LocationProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Geoclue.LocationProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.LocationProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.LocationProxy

    Object GClueLocationProxy

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

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        accuracy: float
        altitude: float
        description: str
        heading: float
        latitude: float
        longitude: float
        speed: float
        timestamp: GLib.Variant
        g_bus_type: Gio.BusType
    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: LocationProxyPrivate = ...
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
        accuracy: float = ...,
        altitude: float = ...,
        description: str = ...,
        heading: float = ...,
        latitude: float = ...,
        longitude: float = ...,
        speed: float = ...,
        timestamp: GLib.Variant = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: Gio.AsyncResult) -> LocationProxy: ...
    @staticmethod
    def new_for_bus(
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> LocationProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> LocationProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> LocationProxy: ...

class LocationProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class LocationProxyPrivate(GObject.GPointer): ...

class LocationSkeleton(Gio.DBusInterfaceSkeleton, Location, Gio.DBusInterface):
    """
    :Constructors:

    ::

        LocationSkeleton(**properties)
        new() -> Geoclue.LocationSkeleton

    Object GClueLocationSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accuracy: float
        altitude: float
        description: str
        heading: float
        latitude: float
        longitude: float
        speed: float
        timestamp: GLib.Variant
    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: LocationSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        accuracy: float = ...,
        altitude: float = ...,
        description: str = ...,
        heading: float = ...,
        latitude: float = ...,
        longitude: float = ...,
        speed: float = ...,
        timestamp: GLib.Variant = ...,
    ): ...
    @classmethod
    def new(cls) -> LocationSkeleton: ...

class LocationSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LocationSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class LocationSkeletonPrivate(GObject.GPointer): ...

class Manager(GObject.GInterface):
    """
    Interface GClueManager

    Signals from GObject:
      notify (GParam)
    """

    def call_add_agent(
        self,
        arg_id: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_add_agent_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_add_agent_sync(
        self, arg_id: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def call_create_client(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_create_client_finish(self, res: Gio.AsyncResult) -> Tuple[bool, str]: ...
    def call_create_client_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, str]: ...
    def call_delete_client(
        self,
        arg_client: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_delete_client_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_delete_client_sync(
        self, arg_client: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def call_get_client(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_client_finish(self, res: Gio.AsyncResult) -> Tuple[bool, str]: ...
    def call_get_client_sync(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[bool, str]: ...
    def complete_add_agent(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_create_client(
        self, invocation: Gio.DBusMethodInvocation, client: str
    ) -> None: ...
    def complete_delete_client(self, invocation: Gio.DBusMethodInvocation) -> None: ...
    def complete_get_client(
        self, invocation: Gio.DBusMethodInvocation, client: str
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

    parent_iface: GObject.TypeInterface = ...
    handle_add_agent: Callable[[Manager, Gio.DBusMethodInvocation, str], bool] = ...
    handle_create_client: Callable[[Manager, Gio.DBusMethodInvocation], bool] = ...
    handle_delete_client: Callable[[Manager, Gio.DBusMethodInvocation, str], bool] = ...
    handle_get_client: Callable[[Manager, Gio.DBusMethodInvocation], bool] = ...
    get_available_accuracy_level: Callable[[Manager], int] = ...
    get_in_use: Callable[[Manager], bool] = ...

class ManagerProxy(
    Gio.DBusProxy, Manager, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    """
    :Constructors:

    ::

        ManagerProxy(**properties)
        new_finish(res:Gio.AsyncResult) -> Geoclue.ManagerProxy
        new_for_bus_finish(res:Gio.AsyncResult) -> Geoclue.ManagerProxy
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ManagerProxy
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> Geoclue.ManagerProxy

    Object GClueManagerProxy

    Signals from GClueManager:
      handle-get-client (GDBusMethodInvocation) -> gboolean
      handle-create-client (GDBusMethodInvocation) -> gboolean
      handle-delete-client (GDBusMethodInvocation, gchararray) -> gboolean
      handle-add-agent (GDBusMethodInvocation, gchararray) -> gboolean

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

    class Props:
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        available_accuracy_level: int
        in_use: bool
        g_bus_type: Gio.BusType
    props: Props = ...
    parent_instance: Gio.DBusProxy = ...
    priv: ManagerProxyPrivate = ...
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
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ): ...
    @staticmethod
    def new(
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
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
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
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
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ManagerProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: Optional[str],
        object_path: str,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> ManagerProxy: ...

class ManagerProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerProxyClass()
    """

    parent_class: Gio.DBusProxyClass = ...

class ManagerProxyPrivate(GObject.GPointer): ...

class ManagerSkeleton(Gio.DBusInterfaceSkeleton, Manager, Gio.DBusInterface):
    """
    :Constructors:

    ::

        ManagerSkeleton(**properties)
        new() -> Geoclue.ManagerSkeleton

    Object GClueManagerSkeleton

    Signals from GClueManager:
      handle-get-client (GDBusMethodInvocation) -> gboolean
      handle-create-client (GDBusMethodInvocation) -> gboolean
      handle-delete-client (GDBusMethodInvocation, gchararray) -> gboolean
      handle-add-agent (GDBusMethodInvocation, gchararray) -> gboolean

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags
        Flags for the interface skeleton

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        g_flags: Gio.DBusInterfaceSkeletonFlags
        available_accuracy_level: int
        in_use: bool
    props: Props = ...
    parent_instance: Gio.DBusInterfaceSkeleton = ...
    priv: ManagerSkeletonPrivate = ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ): ...
    @classmethod
    def new(cls) -> ManagerSkeleton: ...

class ManagerSkeletonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ManagerSkeletonClass()
    """

    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ManagerSkeletonPrivate(GObject.GPointer): ...

class Simple(GObject.Object, Gio.AsyncInitable):
    """
    :Constructors:

    ::

        Simple(**properties)
        new_finish(result:Gio.AsyncResult) -> Geoclue.Simple
        new_sync(desktop_id:str, accuracy_level:Geoclue.AccuracyLevel, cancellable:Gio.Cancellable=None) -> Geoclue.Simple
        new_with_thresholds_finish(result:Gio.AsyncResult) -> Geoclue.Simple
        new_with_thresholds_sync(desktop_id:str, accuracy_level:Geoclue.AccuracyLevel, time_threshold:int, distance_threshold:int, cancellable:Gio.Cancellable=None) -> Geoclue.Simple

    Object GClueSimple

    Properties from GClueSimple:
      desktop-id -> gchararray: DesktopID
        Desktop ID
      accuracy-level -> GClueAccuracyLevel: AccuracyLevel
        Requested accuracy level
      client -> GClueClientProxy: Client
        Client proxy
      location -> GClueLocationProxy: Location
        Location proxy
      distance-threshold -> guint: DistanceThreshold
        DistanceThreshold
      time-threshold -> guint: TimeThreshold
        TimeThreshold

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        client: ClientProxy
        distance_threshold: int
        location: LocationProxy
        time_threshold: int
        accuracy_level: AccuracyLevel
        desktop_id: str
    props: Props = ...
    parent: GObject.Object = ...
    priv: SimplePrivate = ...
    def __init__(
        self,
        accuracy_level: AccuracyLevel = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        time_threshold: int = ...,
    ): ...
    # override
    def get_client(self) -> Optional[ClientProxy]: ...
    def get_location(self) -> Location: ...
    @staticmethod
    def new(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, result: Gio.AsyncResult) -> Simple: ...
    @classmethod
    def new_sync(
        cls,
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Simple: ...
    @staticmethod
    def new_with_thresholds(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        time_threshold: int,
        distance_threshold: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_with_thresholds_finish(cls, result: Gio.AsyncResult) -> Simple: ...
    @classmethod
    def new_with_thresholds_sync(
        cls,
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        time_threshold: int,
        distance_threshold: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Simple: ...

class SimpleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SimpleClass()
    """

    parent_class: GObject.ObjectClass = ...

class SimplePrivate(GObject.GPointer): ...

class ClientProxyCreateFlags(GObject.GFlags):
    AUTO_DELETE = 1
    NONE = 0

class AccuracyLevel(GObject.GEnum):
    CITY = 4
    COUNTRY = 1
    EXACT = 8
    NEIGHBORHOOD = 5
    NONE = 0
    STREET = 6
