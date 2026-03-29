from typing import Any

from collections.abc import Callable

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

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

class Client(GObject.Object):
    def call_start(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_start_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_start_sync(self, cancellable: Gio.Cancellable | None = None) -> bool: ...
    def call_stop(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_stop_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_stop_sync(self, cancellable: Gio.Cancellable | None = None) -> bool: ...
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
    parent_iface: GObject.TypeInterface = ...
    handle_start: Callable[[Client, Gio.DBusMethodInvocation], bool] = ...
    handle_stop: Callable[[Client, Gio.DBusMethodInvocation], bool] = ...
    get_active: Callable[[Client], bool] = ...
    get_desktop_id: Callable[[Client], str | None] = ...
    get_distance_threshold: Callable[[Client], int] = ...
    get_location: Callable[[Client], str | None] = ...
    get_requested_accuracy_level: Callable[[Client], int] = ...
    get_time_threshold: Callable[[Client], int] = ...
    location_updated: Callable[[Client, str, str], None] = ...

class ClientProxy(
    Gio.DBusProxy, Client, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    class Props(Gio.DBusProxy.Props):
        g_bus_type: Gio.BusType
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

    @property
    def props(self) -> Props: ...
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
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ClientProxyPrivate: ...
    @staticmethod
    def create(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_finish(result: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def create_full(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        flags: ClientProxyCreateFlags,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def create_full_finish(result: Gio.AsyncResult) -> ClientProxy: ...
    @staticmethod
    def create_full_sync(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        flags: ClientProxyCreateFlags,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...
    @staticmethod
    def create_sync(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> ClientProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> ClientProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> ClientProxy: ...

class ClientProxyClass(GObject.GPointer):
    parent_class: Gio.DBusProxyClass = ...

class ClientProxyPrivate(GObject.GPointer): ...

class ClientSkeleton(Gio.DBusInterfaceSkeleton, Client, Gio.DBusInterface):
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        active: bool
        desktop_id: str
        distance_threshold: int
        location: str
        requested_accuracy_level: int
        time_threshold: int

    @property
    def props(self) -> Props: ...
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
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ClientSkeletonPrivate: ...
    @classmethod
    def new(cls) -> ClientSkeleton: ...

class ClientSkeletonClass(GObject.GPointer):
    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ClientSkeletonPrivate(GObject.GPointer): ...

class Location(GObject.Object):
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class LocationIface(GObject.GPointer):
    parent_iface: GObject.TypeInterface = ...
    get_accuracy: Callable[[Location], float] = ...
    get_altitude: Callable[[Location], float] = ...
    get_description: Callable[[Location], str | None] = ...
    get_heading: Callable[[Location], float] = ...
    get_latitude: Callable[[Location], float] = ...
    get_longitude: Callable[[Location], float] = ...
    get_speed: Callable[[Location], float] = ...
    get_timestamp: Callable[[Location], GLib.Variant | None] = ...

class LocationProxy(
    Gio.DBusProxy, Location, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable
):
    class Props(Gio.DBusProxy.Props):
        g_bus_type: Gio.BusType
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

    @property
    def props(self) -> Props: ...
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
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> LocationProxyPrivate: ...
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
    def new_finish(cls, res: Gio.AsyncResult) -> LocationProxy: ...
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
    def new_for_bus_finish(cls, res: Gio.AsyncResult) -> LocationProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: Gio.BusType,
        flags: Gio.DBusProxyFlags,
        name: str,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> LocationProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: Gio.DBusConnection,
        flags: Gio.DBusProxyFlags,
        name: str | None,
        object_path: str,
        cancellable: Gio.Cancellable | None = None,
    ) -> LocationProxy: ...

class LocationProxyClass(GObject.GPointer):
    parent_class: Gio.DBusProxyClass = ...

class LocationProxyPrivate(GObject.GPointer): ...

class LocationSkeleton(Gio.DBusInterfaceSkeleton, Location, Gio.DBusInterface):
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        accuracy: float
        altitude: float
        description: str
        heading: float
        latitude: float
        longitude: float
        speed: float
        timestamp: GLib.Variant

    @property
    def props(self) -> Props: ...
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
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> LocationSkeletonPrivate: ...
    @classmethod
    def new(cls) -> LocationSkeleton: ...

class LocationSkeletonClass(GObject.GPointer):
    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class LocationSkeletonPrivate(GObject.GPointer): ...

class Manager(GObject.Object):
    def call_add_agent(
        self,
        arg_id: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_add_agent_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_add_agent_sync(
        self, arg_id: str, cancellable: Gio.Cancellable | None = None
    ) -> bool: ...
    def call_create_client(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_create_client_finish(self, res: Gio.AsyncResult) -> tuple[bool, str]: ...
    def call_create_client_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str]: ...
    def call_delete_client(
        self,
        arg_client: str,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_delete_client_finish(self, res: Gio.AsyncResult) -> bool: ...
    def call_delete_client_sync(
        self, arg_client: str, cancellable: Gio.Cancellable | None = None
    ) -> bool: ...
    def call_get_client(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def call_get_client_finish(self, res: Gio.AsyncResult) -> tuple[bool, str]: ...
    def call_get_client_sync(
        self, cancellable: Gio.Cancellable | None = None
    ) -> tuple[bool, str]: ...
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
    class Props(Gio.DBusProxy.Props):
        g_bus_type: Gio.BusType
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

    @property
    def props(self) -> Props: ...
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
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ManagerProxyPrivate: ...
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
    parent_class: Gio.DBusProxyClass = ...

class ManagerProxyPrivate(GObject.GPointer): ...

class ManagerSkeleton(Gio.DBusInterfaceSkeleton, Manager, Gio.DBusInterface):
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        available_accuracy_level: int
        in_use: bool

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ): ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ManagerSkeletonPrivate: ...
    @classmethod
    def new(cls) -> ManagerSkeleton: ...

class ManagerSkeletonClass(GObject.GPointer):
    parent_class: Gio.DBusInterfaceSkeletonClass = ...

class ManagerSkeletonPrivate(GObject.GPointer): ...

class Simple(GObject.Object, Gio.AsyncInitable):
    class Props(GObject.Object.Props):
        accuracy_level: AccuracyLevel
        client: ClientProxy
        desktop_id: str
        distance_threshold: int
        location: LocationProxy
        time_threshold: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        accuracy_level: AccuracyLevel = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        time_threshold: int = ...,
    ): ...
    parent: GObject.Object = ...
    @property
    def priv(self) -> SimplePrivate: ...
    # override
    def get_client(self) -> ClientProxy | None: ...
    def get_location(self) -> Location: ...
    @staticmethod
    def new(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, result: Gio.AsyncResult) -> Simple: ...
    @classmethod
    def new_sync(
        cls,
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        cancellable: Gio.Cancellable | None = None,
    ) -> Simple: ...
    @staticmethod
    def new_with_thresholds(
        desktop_id: str,
        accuracy_level: AccuracyLevel,
        time_threshold: int,
        distance_threshold: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
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
        cancellable: Gio.Cancellable | None = None,
    ) -> Simple: ...

class SimpleClass(GObject.GPointer):
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
