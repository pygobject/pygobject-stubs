from typing import Any

from collections.abc import Callable

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

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
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_start(self) -> Callable[[Client, Gio.DBusMethodInvocation], bool]: ...
    @property
    def handle_stop(self) -> Callable[[Client, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_active(self) -> Callable[[Client], bool]: ...
    @property
    def get_desktop_id(self) -> Callable[[Client], str | None]: ...
    @property
    def get_distance_threshold(self) -> Callable[[Client], int]: ...
    @property
    def get_location(self) -> Callable[[Client], str | None]: ...
    @property
    def get_requested_accuracy_level(self) -> Callable[[Client], int]: ...
    @property
    def get_time_threshold(self) -> Callable[[Client], int]: ...
    @property
    def location_updated(self) -> Callable[[Client, str, str], None]: ...

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
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> ClientProxyPrivate: ...
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
    ) -> None: ...
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
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

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
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ClientSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        active: bool = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        location: str = ...,
        requested_accuracy_level: int = ...,
        time_threshold: int = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> ClientSkeleton: ...

class ClientSkeletonClass(GObject.GPointer):
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class ClientSkeletonPrivate(GObject.GPointer): ...

class Location(GObject.GInterface):
    @staticmethod
    def interface_info() -> Gio.DBusInterfaceInfo: ...
    @staticmethod
    def override_properties(
        klass: GObject.ObjectClass, property_id_begin: int
    ) -> int: ...

class LocationIface(GObject.GPointer):
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_accuracy(self) -> Callable[[Location], float]: ...
    @property
    def get_altitude(self) -> Callable[[Location], float]: ...
    @property
    def get_description(self) -> Callable[[Location], str | None]: ...
    @property
    def get_heading(self) -> Callable[[Location], float]: ...
    @property
    def get_latitude(self) -> Callable[[Location], float]: ...
    @property
    def get_longitude(self) -> Callable[[Location], float]: ...
    @property
    def get_speed(self) -> Callable[[Location], float]: ...
    @property
    def get_timestamp(self) -> Callable[[Location], GLib.Variant | None]: ...

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
    @property
    def parent_instance(self) -> Gio.DBusProxy: ...
    @property
    def priv(self) -> LocationProxyPrivate: ...
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
    ) -> None: ...
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
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

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
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> LocationSkeletonPrivate: ...
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
    ) -> None: ...
    @classmethod
    def new(cls) -> LocationSkeleton: ...

class LocationSkeletonClass(GObject.GPointer):
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

class LocationSkeletonPrivate(GObject.GPointer): ...

class Manager(GObject.GInterface):
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
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def handle_add_agent(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation, str], bool]: ...
    @property
    def handle_create_client(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation], bool]: ...
    @property
    def handle_delete_client(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation, str], bool]: ...
    @property
    def handle_get_client(
        self,
    ) -> Callable[[Manager, Gio.DBusMethodInvocation], bool]: ...
    @property
    def get_available_accuracy_level(self) -> Callable[[Manager], int]: ...
    @property
    def get_in_use(self) -> Callable[[Manager], bool]: ...

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
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ) -> None: ...
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
    @property
    def parent_class(self) -> Gio.DBusProxyClass: ...

class ManagerProxyPrivate(GObject.GPointer): ...

class ManagerSkeleton(Gio.DBusInterfaceSkeleton, Manager, Gio.DBusInterface):
    class Props(Gio.DBusInterfaceSkeleton.Props):
        g_flags: Gio.DBusInterfaceSkeletonFlags
        available_accuracy_level: int
        in_use: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> Gio.DBusInterfaceSkeleton: ...
    @property
    def priv(self) -> ManagerSkeletonPrivate: ...
    def __init__(
        self,
        g_flags: Gio.DBusInterfaceSkeletonFlags = ...,
        available_accuracy_level: int = ...,
        in_use: bool = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> ManagerSkeleton: ...

class ManagerSkeletonClass(GObject.GPointer):
    @property
    def parent_class(self) -> Gio.DBusInterfaceSkeletonClass: ...

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
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def priv(self) -> SimplePrivate: ...
    def __init__(
        self,
        accuracy_level: AccuracyLevel = ...,
        desktop_id: str = ...,
        distance_threshold: int = ...,
        time_threshold: int = ...,
    ) -> None: ...
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
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

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
