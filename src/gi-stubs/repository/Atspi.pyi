from typing import Any
from typing import Final
from typing import Literal
from typing import Protocol
from typing import type_check_only
from typing import TypeAlias
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

from collections.abc import Callable
from collections.abc import Mapping
from collections.abc import Sequence

from gi import _gi
from gi.repository import DBus
from gi.repository import GLib
from gi.repository import GObject

_DataTs = TypeVarTuple("_DataTs", default=Unpack[tuple[()]])

ACCESSIBLE_VERSION: Final[int]
ACTION_VERSION: Final[int]
APPLICATION_VERSION: Final[int]
CACHE_VERSION: Final[int]
COLLECTION_VERSION: Final[int]
COMPONENTLAYER_COUNT: Final[int]
COMPONENT_VERSION: Final[int]
COORD_TYPE_COUNT: Final[int]
DBUS_INTERFACE_ACCESSIBLE: Final = "org.a11y.atspi.Accessible"
DBUS_INTERFACE_ACTION: Final = "org.a11y.atspi.Action"
DBUS_INTERFACE_APPLICATION: Final = "org.a11y.atspi.Application"
DBUS_INTERFACE_CACHE: Final = "org.a11y.atspi.Cache"
DBUS_INTERFACE_COLLECTION: Final = "org.a11y.atspi.Collection"
DBUS_INTERFACE_COMPONENT: Final = "org.a11y.atspi.Component"
DBUS_INTERFACE_DEC: Final = "org.a11y.atspi.DeviceEventController"
DBUS_INTERFACE_DEVICE_EVENT_LISTENER: Final = "org.a11y.atspi.DeviceEventListener"
DBUS_INTERFACE_DOCUMENT: Final = "org.a11y.atspi.Document"
DBUS_INTERFACE_EDITABLE_TEXT: Final = "org.a11y.atspi.EditableText"
DBUS_INTERFACE_EVENT_KEYBOARD: Final = "org.a11y.atspi.Event.Keyboard"
DBUS_INTERFACE_EVENT_MOUSE: Final = "org.a11y.atspi.Event.Mouse"
DBUS_INTERFACE_EVENT_OBJECT: Final = "org.a11y.atspi.Event.Object"
DBUS_INTERFACE_EVENT_SCREEN_READER: Final = "org.a11y.atspi.Event.ScreenReader"
DBUS_INTERFACE_HYPERLINK: Final = "org.a11y.atspi.Hyperlink"
DBUS_INTERFACE_HYPERTEXT: Final = "org.a11y.atspi.Hypertext"
DBUS_INTERFACE_IMAGE: Final = "org.a11y.atspi.Image"
DBUS_INTERFACE_KEYBOARD_MONITOR: Final = "org.freedesktop.a11y.KeyboardMonitor"
DBUS_INTERFACE_POINTER_LOCATOR: Final = "org.freedesktop.a11y.PointerLocator"
DBUS_INTERFACE_REGISTRY: Final = "org.a11y.atspi.Registry"
DBUS_INTERFACE_SELECTION: Final = "org.a11y.atspi.Selection"
DBUS_INTERFACE_SOCKET: Final = "org.a11y.atspi.Socket"
DBUS_INTERFACE_TABLE: Final = "org.a11y.atspi.Table"
DBUS_INTERFACE_TABLE_CELL: Final = "org.a11y.atspi.TableCell"
DBUS_INTERFACE_TEXT: Final = "org.a11y.atspi.Text"
DBUS_INTERFACE_VALUE: Final = "org.a11y.atspi.Value"
DBUS_NAME_A11Y_MANAGER: Final = "org.freedesktop.a11y.Manager"
DBUS_NAME_REGISTRY: Final = "org.a11y.atspi.Registry"
DBUS_PATH_A11Y_MANAGER: Final = "/org/freedesktop/a11y/Manager"
DBUS_PATH_DEC: Final = "/org/a11y/atspi/registry/deviceeventcontroller"
DBUS_PATH_NULL: Final = "/org/a11y/atspi/null"
DBUS_PATH_REGISTRY: Final = "/org/a11y/atspi/registry"
DBUS_PATH_ROOT: Final = "/org/a11y/atspi/accessible/root"
DBUS_PATH_SCREEN_READER: Final = "/org/a11y/atspi/screenreader"
DEVICE_A11Y_MANAGER_VIRTUAL_MOD_END: Final[int]
DEVICE_A11Y_MANAGER_VIRTUAL_MOD_START: Final[int]
DEVICE_EVENT_CONTROLLER_VERSION: Final[int]
DEVICE_EVENT_LISTENER_VERSION: Final[int]
DOCUMENT_VERSION: Final[int]
EDITABLE_TEXT_VERSION: Final[int]
EVENTTYPE_COUNT: Final[int]
EVENT_VERSION: Final[int]
HYPERLINK_VERSION: Final[int]
HYPERTEXT_VERSION: Final[int]
IMAGE_VERSION: Final[int]
KEYEVENTTYPE_COUNT: Final[int]
KEYSYNTHTYPE_COUNT: Final[int]
LOCALE_TYPE_COUNT: Final[int]
MATCHTYPES_COUNT: Final[int]
MAX_CHILDREN: Final[int]
MODIFIERTYPE_COUNT: Final[int]
REGISTRY_VERSION: Final[int]
RELATIONTYPE_COUNT: Final[int]
ROLE_COUNT: Final[int]
SCROLLTYPE_COUNT: Final[int]
SELECTION_VERSION: Final[int]
SOCKET_VERSION: Final[int]
SORTORDER_COUNT: Final[int]
STATETYPE_COUNT: Final[int]
TABLE_CELL_VERSION: Final[int]
TABLE_VERSION: Final[int]
TEXT_BOUNDARY_TYPE_COUNT: Final[int]
TEXT_CLIP_TYPE_COUNT: Final[int]
TEXT_VERSION: Final[int]
TREETRAVERSALTYPE_COUNT: Final[int]
VALUE_VERSION: Final[int]

def deregister_device_event_listener(
    listener: DeviceListener, filter: int | Any | None = None
) -> bool: ...
def deregister_keystroke_listener(
    listener: DeviceListener,
    key_set: Sequence[KeyDefinition] | None,
    modmask: int,
    event_types: int,
) -> bool: ...
def event_main() -> None: ...
def event_quit() -> None: ...
def exit() -> int: ...
def generate_keyboard_event(
    keyval: int, keystring: str | None, synth_type: _KeySynthTypeValueType
) -> bool: ...
def generate_mouse_event(x: int, y: int, name: str) -> bool: ...
def generate_mouse_event_async(
    x: int,
    y: int,
    name: str,
    callback: Callable[[Unpack[_DataTs]], None],
    *callback_data: Unpack[_DataTs],
) -> None: ...
def get_desktop(i: int) -> Accessible: ...
def get_desktop_count() -> int: ...
def get_desktop_list() -> list[Accessible]: ...
def get_version() -> tuple[int, int, int]: ...
def init() -> int: ...
def is_initialized() -> bool: ...
def register_device_event_listener(
    listener: DeviceListener, event_types: int, filter: int | Any | None = None
) -> bool: ...
def register_keystroke_listener(
    listener: DeviceListener,
    key_set: Sequence[KeyDefinition] | None,
    modmask: int,
    event_types: int,
    sync_type: _KeyListenerSyncTypeValueType,
) -> bool: ...
def role_get_localized_name(role: _RoleValueType) -> str: ...
def role_get_name(role: _RoleValueType) -> str: ...
def set_g_main_loop_reentrancy(enabled: bool) -> None: ...
def set_main_context(cnx: GLib.MainContext) -> None: ...
def set_reference_window(accessible: Accessible) -> None: ...
def set_timeout(val: int, startup_time: int) -> None: ...

class Accessible(
    Object,
    Action,
    Collection,
    Component,
    Document,
    EditableText,
    Hypertext,
    Image,
    Selection,
    Table,
    TableCell,
    Text,
    Value,
):
    """
    :Constructors:

    ::

        Accessible(**properties)

    Object AtspiAccessible

    Signals from AtspiAccessible:
      region-changed (gint, gint)
      mode-changed (gint, gchararray)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> Object: ...
    @property
    def accessible_parent(self) -> Accessible: ...
    @property
    def children(self) -> list[int]: ...
    @property
    def role(self) -> Role: ...
    @property
    def interfaces(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def states(self) -> StateSet: ...
    @property
    def attributes(self) -> dict[int, int]: ...
    @property
    def cached_properties(self) -> int: ...
    @property
    def priv(self) -> AccessiblePrivate: ...
    # override
    def __bool__(self) -> bool: ...  # FIXME: Override is missing typing annotation
    # override
    def __getitem__(
        self, i: int
    ) -> Any: ...  # FIXME: Override is missing typing annotation
    # override
    def __len__(self) -> int: ...  # FIXME: Override is missing typing annotation
    # override
    def __nonzero__(self) -> bool: ...  # FIXME: Override is missing typing annotation
    def clear_cache(self) -> None: ...
    def clear_cache_single(self) -> None: ...
    def do_mode_changed(self, enabled: bool, /) -> None: ...
    def do_region_changed(self, current_offset: int, last_offset: int, /) -> None: ...
    def get_accessible_id(self) -> str: ...
    def get_action(self) -> Action: ...
    def get_action_iface(self) -> Action: ...
    def get_application(self) -> Accessible: ...
    def get_atspi_version(self) -> str: ...
    def get_attributes(self) -> dict[str, str]: ...
    def get_attributes_as_array(self) -> list[str]: ...
    def get_child_at_index(self, child_index: int) -> Accessible: ...
    def get_child_count(self) -> int: ...
    def get_collection(self) -> Collection: ...
    def get_collection_iface(self) -> Collection: ...
    def get_component(self) -> Component: ...
    def get_component_iface(self) -> Component: ...
    def get_description(self) -> str: ...
    def get_document(self) -> Document: ...
    def get_document_iface(self) -> Document: ...
    def get_editable_text(self) -> EditableText: ...
    def get_editable_text_iface(self) -> EditableText: ...
    def get_help_text(self) -> str: ...
    def get_hyperlink(self) -> Hyperlink: ...
    def get_hypertext(self) -> Hypertext: ...
    def get_hypertext_iface(self) -> Hypertext: ...
    def get_id(self) -> int: ...
    def get_image(self) -> Image: ...
    def get_image_iface(self) -> Image: ...
    def get_index_in_parent(self) -> int: ...
    def get_interfaces(self) -> list[str]: ...
    def get_localized_role_name(self) -> str: ...
    def get_name(self) -> str: ...
    def get_object_locale(self) -> str: ...
    def get_parent(self) -> Accessible | None: ...
    def get_process_id(self) -> int: ...
    def get_relation_set(self) -> list[Relation]: ...
    def get_role(self) -> Role: ...
    def get_role_name(self) -> str: ...
    def get_selection(self) -> Selection: ...
    def get_selection_iface(self) -> Selection: ...
    def get_state_set(self) -> StateSet: ...
    def get_table(self) -> Table: ...
    def get_table_cell(self) -> TableCell: ...
    def get_table_iface(self) -> Table: ...
    def get_text(self) -> Text: ...
    def get_text_iface(self) -> Text: ...
    def get_toolkit_name(self) -> str: ...
    def get_toolkit_version(self) -> str: ...
    def get_value(self) -> Value: ...
    def get_value_iface(self) -> Value: ...
    def is_action(self) -> bool: ...
    def is_application(self) -> bool: ...
    def is_collection(self) -> bool: ...
    def is_component(self) -> bool: ...
    def is_document(self) -> bool: ...
    def is_editable_text(self) -> bool: ...
    def is_hyperlink(self) -> bool: ...
    def is_hypertext(self) -> bool: ...
    def is_image(self) -> bool: ...
    def is_selection(self) -> bool: ...
    def is_table(self) -> bool: ...
    def is_table_cell(self) -> bool: ...
    def is_text(self) -> bool: ...
    def is_value(self) -> bool: ...
    def set_cache_mask(self, mask: _CacheValueType) -> None: ...

class AccessibleClass(_gi.Struct):
    """
    :Constructors:

    ::

        AccessibleClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...
    @property
    def region_changed(self) -> Callable[[Accessible, int, int], None]: ...
    @property
    def mode_changed(self) -> Callable[[Accessible, bool], None]: ...

class AccessiblePrivate(_gi.Struct): ...

class Action(GObject.GInterface, Protocol):
    """
    Interface AtspiAction
    """
    def do_action(self, i: int) -> bool: ...
    def get_action_description(self, i: int) -> str: ...
    def get_action_name(self, i: int) -> str: ...
    def get_key_binding(self, i: int) -> str: ...
    def get_localized_name(self, i: int) -> str: ...
    def get_n_actions(self) -> int: ...

class Application(GObject.Object):
    """
    :Constructors:

    ::

        Application(**properties)

    Object AtspiApplication

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def hash(self) -> dict[int, int]: ...
    @property
    def bus_name(self) -> str: ...
    @property
    def bus(self) -> DBus.Connection: ...
    @property
    def root(self) -> int: ...
    @property
    def cache(self) -> Cache: ...
    @property
    def toolkit_name(self) -> str: ...
    @property
    def toolkit_version(self) -> str: ...
    @property
    def atspi_version(self) -> str: ...
    @property
    def time_added(self) -> int: ...
    @property
    def pid(self) -> int: ...
    @property
    def get_items_pending(self) -> DBus.PendingCall: ...
    @property
    def get_items_finished(self) -> bool: ...

class ApplicationClass(_gi.Struct):
    """
    :Constructors:

    ::

        ApplicationClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Collection(GObject.GInterface, Protocol):
    """
    Interface AtspiCollection
    """
    def get_active_descendant(self) -> Accessible: ...
    def get_matches(
        self,
        rule: MatchRule,
        sortby: _CollectionSortOrderValueType,
        count: int,
        traverse: bool,
    ) -> list[Accessible]: ...
    def get_matches_from(
        self,
        current_object: Accessible,
        rule: MatchRule,
        sortby: _CollectionSortOrderValueType,
        tree: _CollectionTreeTraversalTypeValueType,
        count: int,
        traverse: bool,
    ) -> list[Accessible]: ...
    def get_matches_to(
        self,
        current_object: Accessible,
        rule: MatchRule,
        sortby: _CollectionSortOrderValueType,
        tree: _CollectionTreeTraversalTypeValueType,
        limit_scope: bool,
        count: int,
        traverse: bool,
    ) -> list[Accessible]: ...
    def is_ancestor_of(self, test: Accessible) -> bool: ...

class Component(GObject.GInterface, Protocol):
    """
    Interface AtspiComponent
    """
    def contains(self, x: int, y: int, ctype: _CoordTypeValueType) -> bool: ...
    def get_accessible_at_point(
        self, x: int, y: int, ctype: _CoordTypeValueType
    ) -> Accessible | None: ...
    def get_alpha(self) -> float: ...
    def get_extents(self, ctype: _CoordTypeValueType) -> Rect: ...
    def get_layer(self) -> ComponentLayer: ...
    def get_mdi_z_order(self) -> int: ...
    def get_position(self, ctype: _CoordTypeValueType) -> Point: ...
    def get_size(self) -> Point: ...
    def grab_focus(self) -> bool: ...
    def scroll_to(self, type: _ScrollTypeValueType) -> bool: ...
    def scroll_to_point(self, coords: _CoordTypeValueType, x: int, y: int) -> bool: ...
    def set_extents(
        self, x: int, y: int, width: int, height: int, ctype: _CoordTypeValueType
    ) -> bool: ...
    def set_position(self, x: int, y: int, ctype: _CoordTypeValueType) -> bool: ...
    def set_size(self, width: int, height: int) -> bool: ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)
        new() -> Atspi.Device
        new_full(app_id:str=None) -> Atspi.Device

    Object AtspiDevice

    Signals from AtspiDevice:
      key-pressed (guint, guint, AtspiModifierType, gchararray)
      key-released (guint, guint, AtspiModifierType, gchararray)
      pointer-moved (AtspiAccessible, guint, guint)

    Properties from AtspiDevice:
      app-id -> gchararray: Application ID
        The application ID of the application that created this device

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def app_id(self) -> str: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(self, *, app_id: str | None = ...) -> None: ...
    def add_key_grab(
        self,
        kd: KeyDefinition,
        callback: Callable[[Device, bool, int, int, int, str, Unpack[_DataTs]], None]
        | None = None,
        *user_data: Unpack[_DataTs],
    ) -> int: ...
    def add_key_watcher(
        self,
        callback: Callable[[Device, bool, int, int, int, str, Unpack[_DataTs]], None],
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    def clear_key_grabs(self) -> None: ...
    def do_add_key_grab(self, kd: KeyDefinition, /) -> bool: ...
    def do_generate_mouse_event(
        self, obj: Accessible, x: int, y: int, name: str, /
    ) -> None: ...
    def do_get_capabilities(self) -> DeviceCapability: ...
    def do_get_keysym_modifier(self, keysym: int, /) -> int: ...
    def do_get_locked_modifiers(self) -> int: ...
    def do_get_modifier(self, keycode: int, /) -> int: ...
    def do_grab_keyboard(self) -> bool: ...
    def do_map_keysym_modifier(self, keysym: int, /) -> int: ...
    def do_map_modifier(self, keycode: int, /) -> int: ...
    def do_remove_key_grab(self, id: int, /) -> None: ...
    def do_set_capabilities(
        self, capabilities: _DeviceCapabilityValueType, /
    ) -> DeviceCapability: ...
    def do_ungrab_keyboard(self) -> None: ...
    def do_unmap_keysym_modifier(self, keysym: int, /) -> None: ...
    def do_unmap_modifier(self, keycode: int, /) -> None: ...
    def generate_mouse_event(
        self, obj: Accessible, x: int, y: int, name: str
    ) -> None: ...
    def get_app_id(self) -> str: ...
    def get_capabilities(self) -> DeviceCapability: ...
    def get_grab_by_id(self, id: int) -> KeyDefinition: ...
    def get_keysym_modifier(self, keysym: int) -> int: ...
    def get_locked_modifiers(self) -> int: ...
    def get_modifier(self, keycode: int) -> int: ...
    def grab_keyboard(self) -> bool: ...
    def map_keysym_modifier(self, keysym: int) -> int: ...
    def map_modifier(self, keycode: int) -> int: ...
    @classmethod
    def new(cls) -> Device: ...
    @classmethod
    def new_full(cls, app_id: str | None = None) -> Device: ...
    def notify_key(
        self, pressed: bool, keycode: int, keysym: int, state: int, text: str
    ) -> bool: ...
    def remove_key_grab(self, id: int) -> None: ...
    def set_app_id(self, app_id: str) -> None: ...
    def set_capabilities(
        self, capabilities: _DeviceCapabilityValueType
    ) -> DeviceCapability: ...
    def ungrab_keyboard(self) -> None: ...
    def unmap_keysym_modifier(self, keysym: int) -> None: ...
    def unmap_modifier(self, keycode: int) -> None: ...

class DeviceA11yManager(Device):
    """
    :Constructors:

    ::

        DeviceA11yManager(**properties)
        try_new() -> Atspi.DeviceA11yManager
        try_new_full(app_id:str=None) -> Atspi.DeviceA11yManager

    Object AtspiDeviceA11yManager

    Properties from AtspiDeviceA11yManager:
      session-bus -> GDBusConnection: Session Bus
        The session bus
      keyboard-monitor -> GDBusProxy: Keyboard Monitor
        The keyboard monitor proxy
      pointer-locator -> GDBusProxy: Pointer Locator
        The pointer locator proxy

    Signals from AtspiDevice:
      key-pressed (guint, guint, AtspiModifierType, gchararray)
      key-released (guint, guint, AtspiModifierType, gchararray)
      pointer-moved (AtspiAccessible, guint, guint)

    Properties from AtspiDevice:
      app-id -> gchararray: Application ID
        The application ID of the application that created this device

    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *, app_id: str | None = ...) -> None: ...
    @classmethod
    def try_new(cls) -> DeviceA11yManager: ...
    @classmethod
    def try_new_full(cls, app_id: str | None = None) -> DeviceA11yManager: ...

class DeviceA11yManagerClass(_gi.Struct):
    """
    :Constructors:

    ::

        DeviceA11yManagerClass()
    """
    @property
    def parent_class(self) -> DeviceClass: ...

class DeviceClass(_gi.Struct):
    """
    :Constructors:

    ::

        DeviceClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def add_key_grab(self) -> Callable[[Device, KeyDefinition], bool]: ...
    @property
    def remove_key_grab(self) -> Callable[[Device, int], None]: ...
    @property
    def map_modifier(self) -> Callable[[Device, int], int]: ...
    @property
    def unmap_modifier(self) -> Callable[[Device, int], None]: ...
    @property
    def get_modifier(self) -> Callable[[Device, int], int]: ...
    @property
    def grab_keyboard(self) -> Callable[[Device], bool]: ...
    @property
    def ungrab_keyboard(self) -> Callable[[Device], None]: ...
    @property
    def get_locked_modifiers(self) -> Callable[[Device], int]: ...
    @property
    def generate_mouse_event(
        self,
    ) -> Callable[[Device, Accessible, int, int, str], None]: ...
    @property
    def map_keysym_modifier(self) -> Callable[[Device, int], int]: ...
    @property
    def unmap_keysym_modifier(self) -> Callable[[Device, int], None]: ...
    @property
    def get_keysym_modifier(self) -> Callable[[Device, int], int]: ...
    @property
    def get_capabilities(self) -> Callable[[Device], DeviceCapability]: ...
    @property
    def set_capabilities(
        self,
    ) -> Callable[[Device, _DeviceCapabilityValueType], DeviceCapability]: ...

class DeviceEvent(GObject.GBoxed):
    """
    :Constructors:

    ::

        DeviceEvent()
    """

    type: EventType
    id: int
    hw_code: int
    modifiers: int
    timestamp: int
    event_string: str
    is_text: bool

class DeviceLegacy(Device):
    """
    :Constructors:

    ::

        DeviceLegacy(**properties)
        new() -> Atspi.DeviceLegacy
        new_full(app_id:str=None) -> Atspi.DeviceLegacy

    Object AtspiDeviceLegacy

    Signals from AtspiDevice:
      key-pressed (guint, guint, AtspiModifierType, gchararray)
      key-released (guint, guint, AtspiModifierType, gchararray)
      pointer-moved (AtspiAccessible, guint, guint)

    Properties from AtspiDevice:
      app-id -> gchararray: Application ID
        The application ID of the application that created this device

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> Device: ...
    def __init__(self, *, app_id: str | None = ...) -> None: ...
    @classmethod
    def new(cls) -> DeviceLegacy: ...
    @classmethod
    def new_full(cls, app_id: str | None = None) -> DeviceLegacy: ...

class DeviceLegacyClass(_gi.Struct):
    """
    :Constructors:

    ::

        DeviceLegacyClass()
    """
    @property
    def parent_class(self) -> DeviceClass: ...

class DeviceListener(GObject.Object):
    """
    :Constructors:

    ::

        DeviceListener(**properties)
        new(callback:Atspi.DeviceListenerCB=None, user_data=None) -> Atspi.DeviceListener

    Object AtspiDeviceListener

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def id(self) -> int: ...
    @property
    def callbacks(self) -> list[int]: ...
    def add_callback(
        self,
        callback: Callable[[DeviceEvent, Unpack[_DataTs]], bool],
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    def do_device_event(self, event: DeviceEvent, /) -> bool: ...
    @classmethod
    def new(
        cls,
        callback: Callable[[DeviceEvent, Unpack[_DataTs]], bool] | None = None,
        *user_data: Unpack[_DataTs],
    ) -> DeviceListener: ...
    def remove_callback(
        self, callback: Callable[[DeviceEvent, Any | None], bool]
    ) -> None: ...

class DeviceListenerClass(_gi.Struct):
    """
    :Constructors:

    ::

        DeviceListenerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def device_event(self) -> Callable[[DeviceListener, DeviceEvent], bool]: ...

class DeviceX11(Device):
    """
    :Constructors:

    ::

        DeviceX11(**properties)
        new() -> Atspi.DeviceX11
        new_full(app_id:str=None) -> Atspi.DeviceX11

    Object AtspiDeviceX11

    Signals from AtspiDevice:
      key-pressed (guint, guint, AtspiModifierType, gchararray)
      key-released (guint, guint, AtspiModifierType, gchararray)
      pointer-moved (AtspiAccessible, guint, guint)

    Properties from AtspiDevice:
      app-id -> gchararray: Application ID
        The application ID of the application that created this device

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> Device: ...
    def __init__(self, *, app_id: str | None = ...) -> None: ...
    @classmethod
    def new(cls) -> DeviceX11: ...
    @classmethod
    def new_full(cls, app_id: str | None = None) -> DeviceX11: ...

class DeviceX11Class(_gi.Struct):
    """
    :Constructors:

    ::

        DeviceX11Class()
    """
    @property
    def parent_class(self) -> DeviceClass: ...

class Document(GObject.GInterface, Protocol):
    """
    Interface AtspiDocument
    """
    def get_current_page_number(self) -> int: ...
    def get_document_attribute_value(self, attribute: str) -> str: ...
    def get_document_attributes(self) -> dict[str, str]: ...
    def get_locale(self) -> str: ...
    def get_page_count(self) -> int: ...
    def get_text_selections(self) -> list[TextSelection]: ...
    def set_text_selections(self, selections: Sequence[TextSelection]) -> bool: ...

class EditableText(GObject.GInterface, Protocol):
    """
    Interface AtspiEditableText
    """
    def copy_text(self, start_pos: int, end_pos: int) -> bool: ...
    def cut_text(self, start_pos: int, end_pos: int) -> bool: ...
    def delete_text(self, start_pos: int, end_pos: int) -> bool: ...
    def insert_text(self, position: int, text: str, length: int) -> bool: ...
    def paste_text(self, position: int) -> bool: ...
    def set_text_contents(self, new_contents: str) -> bool: ...

class Event(GObject.GBoxed):
    """
    :Constructors:

    ::

        Event()
    """

    type: str
    source: Accessible
    detail1: int
    detail2: int
    any_data: Any
    sender: Accessible
    @staticmethod
    def main() -> None: ...
    @staticmethod
    def quit() -> None: ...

class EventListener(GObject.Object):
    """
    :Constructors:

    ::

        EventListener(**properties)
        new(callback:Atspi.EventListenerCB, user_data=None) -> Atspi.EventListener

    Object AtspiEventListener

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def callback(self) -> Callable[[Event, Any | None], None]: ...
    @property
    def user_data(self) -> int: ...
    @property
    def cb_destroyed(self) -> Callable[[Any | None], None]: ...
    def deregister(self, event_type: str) -> bool: ...
    @staticmethod
    def deregister_from_callback(
        callback: Callable[[Event, Any | None], None],
        user_data: Any | None,
        event_type: str,
    ) -> bool: ...
    @classmethod
    def new(
        cls,
        callback: Callable[[Event, Unpack[_DataTs]], None],
        *user_data: Unpack[_DataTs],
    ) -> EventListener: ...
    def register(self, event_type: str) -> bool: ...
    @staticmethod
    def register_from_callback(
        callback: Callable[[Event, Any | None], None],
        user_data: Any | None,
        event_type: str,
    ) -> bool: ...
    @staticmethod
    def register_from_callback_full(
        callback: Callable[[Event, Any | None], None],
        user_data: Any | None,
        event_type: str,
        properties: Sequence[str],
    ) -> bool: ...
    @staticmethod
    def register_from_callback_with_app(
        callback: Callable[[Event, Any | None], None],
        user_data: Any | None,
        event_type: str,
        properties: Sequence[str],
        app: Accessible | None = None,
    ) -> bool: ...
    def register_full(
        self, event_type: str, properties: Sequence[str] | None = None
    ) -> bool: ...
    def register_with_app(
        self,
        event_type: str,
        properties: Sequence[str] | None = None,
        app: Accessible | None = None,
    ) -> bool: ...

class EventListenerClass(_gi.Struct):
    """
    :Constructors:

    ::

        EventListenerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class EventListenerMode(_gi.Struct):
    """
    :Constructors:

    ::

        EventListenerMode()
    """

    synchronous: bool
    preemptive: bool
    global_: bool

class Hyperlink(Object):
    """
    :Constructors:

    ::

        Hyperlink(**properties)

    Object AtspiHyperlink

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> Object: ...
    def get_end_index(self) -> int: ...
    def get_index_range(self) -> Range: ...
    def get_n_anchors(self) -> int: ...
    def get_object(self, i: int) -> Accessible: ...
    def get_start_index(self) -> int: ...
    def get_uri(self, i: int) -> str: ...
    def is_valid(self) -> bool: ...

class HyperlinkClass(_gi.Struct):
    """
    :Constructors:

    ::

        HyperlinkClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...

class Hypertext(GObject.GInterface, Protocol):
    """
    Interface AtspiHypertext
    """
    def get_link(self, link_index: int) -> Hyperlink | None: ...
    def get_link_index(self, character_offset: int) -> int: ...
    def get_n_links(self) -> int: ...

class Image(GObject.GInterface, Protocol):
    """
    Interface AtspiImage
    """
    def get_image_description(self) -> str: ...
    def get_image_extents(self, ctype: _CoordTypeValueType) -> Rect: ...
    def get_image_locale(self) -> str: ...
    def get_image_position(self, ctype: _CoordTypeValueType) -> Point: ...
    def get_image_size(self) -> Point: ...

class KeyDefinition(GObject.GBoxed):
    """
    :Constructors:

    ::

        KeyDefinition()
    """

    keycode: int
    keysym: int
    keystring: str
    modifiers: int

class KeySet(_gi.Struct):
    """
    :Constructors:

    ::

        KeySet()
    """

    keysyms: int
    keycodes: int
    keystrings: str
    len: int

class MatchRule(GObject.Object):
    """
    :Constructors:

    ::

        MatchRule(**properties)
        new(states:Atspi.StateSet=None, statematchtype:Atspi.CollectionMatchType, attributes:dict=None, attributematchtype:Atspi.CollectionMatchType, roles:list=None, rolematchtype:Atspi.CollectionMatchType, interfaces:list=None, interfacematchtype:Atspi.CollectionMatchType, invert:bool) -> Atspi.MatchRule

    Object AtspiMatchRule

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def states(self) -> StateSet: ...
    @property
    def statematchtype(self) -> CollectionMatchType: ...
    @property
    def attributes(self) -> dict[int, int]: ...
    @property
    def attributematchtype(self) -> CollectionMatchType: ...
    @property
    def interfaces(self) -> list[int]: ...
    @property
    def interfacematchtype(self) -> CollectionMatchType: ...
    @property
    def roles(self) -> list[int]: ...
    @property
    def rolematchtype(self) -> CollectionMatchType: ...
    @property
    def invert(self) -> bool: ...
    @classmethod
    def new(
        cls,
        states: StateSet | None,
        statematchtype: _CollectionMatchTypeValueType,
        attributes: Mapping[str, str] | None,
        attributematchtype: _CollectionMatchTypeValueType,
        roles: Sequence[_RoleValueType] | None,
        rolematchtype: _CollectionMatchTypeValueType,
        interfaces: Sequence[str] | None,
        interfacematchtype: _CollectionMatchTypeValueType,
        invert: bool,
    ) -> MatchRule: ...

class MatchRuleClass(_gi.Struct):
    """
    :Constructors:

    ::

        MatchRuleClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Object(GObject.Object):
    """
    :Constructors:

    ::

        Object(**properties)

    Object AtspiObject

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def app(self) -> Application: ...
    @property
    def path(self) -> str: ...

class ObjectClass(_gi.Struct):
    """
    :Constructors:

    ::

        ObjectClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Point(GObject.GBoxed):
    """
    :Constructors:

    ::

        Point()
    """

    x: int
    y: int
    def copy(self) -> Point: ...

class Range(GObject.GBoxed):
    """
    :Constructors:

    ::

        Range()
    """

    start_offset: int
    end_offset: int
    def copy(self) -> Range: ...

class Rect(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rect()
    """

    x: int
    y: int
    width: int
    height: int
    def copy(self) -> Rect: ...

class Relation(GObject.Object):
    """
    :Constructors:

    ::

        Relation(**properties)

    Object AtspiRelation

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def relation_type(self) -> RelationType: ...
    @property
    def targets(self) -> list[int]: ...
    def get_n_targets(self) -> int: ...
    def get_relation_type(self) -> RelationType: ...
    def get_target(self, i: int) -> Accessible: ...

class RelationClass(_gi.Struct):
    """
    :Constructors:

    ::

        RelationClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Selection(GObject.GInterface, Protocol):
    """
    Interface AtspiSelection
    """
    def clear_selection(self) -> bool: ...
    def deselect_child(self, child_index: int) -> bool: ...
    def deselect_selected_child(self, selected_child_index: int) -> bool: ...
    def get_n_selected_children(self) -> int: ...
    def get_selected_child(self, selected_child_index: int) -> Accessible: ...
    def is_child_selected(self, child_index: int) -> bool: ...
    def select_all(self) -> bool: ...
    def select_child(self, child_index: int) -> bool: ...

class StateSet(GObject.Object):
    """
    :Constructors:

    ::

        StateSet(**properties)
        new(states:list) -> Atspi.StateSet

    Object AtspiStateSet

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def accessible(self) -> int: ...
    @property
    def states(self) -> int: ...
    def add(self, state: _StateTypeValueType) -> None: ...
    def compare(self, set2: StateSet) -> StateSet: ...
    def contains(self, state: _StateTypeValueType) -> bool: ...
    def equals(self, set2: StateSet) -> bool: ...
    def get_states(self) -> list[StateType]: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls, states: Sequence[_StateTypeValueType]) -> StateSet: ...
    def remove(self, state: _StateTypeValueType) -> None: ...
    def set_by_name(self, name: str, enabled: bool) -> None: ...

class StateSetClass(_gi.Struct):
    """
    :Constructors:

    ::

        StateSetClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Table(GObject.GInterface, Protocol):
    """
    Interface AtspiTable
    """
    def add_column_selection(self, column: int) -> bool: ...
    def add_row_selection(self, row: int) -> bool: ...
    def get_accessible_at(self, row: int, column: int) -> Accessible: ...
    def get_caption(self) -> Accessible: ...
    def get_column_at_index(self, index: int) -> int: ...
    def get_column_description(self, column: int) -> str: ...
    def get_column_extent_at(self, row: int, column: int) -> int: ...
    def get_column_header(self, column: int) -> Accessible: ...
    def get_index_at(self, row: int, column: int) -> int: ...
    def get_n_columns(self) -> int: ...
    def get_n_rows(self) -> int: ...
    def get_n_selected_columns(self) -> int: ...
    def get_n_selected_rows(self) -> int: ...
    def get_row_at_index(self, index: int) -> int: ...
    def get_row_column_extents_at_index(
        self, index: int
    ) -> tuple[bool, int, int, int, int, bool]: ...
    def get_row_description(self, row: int) -> str: ...
    def get_row_extent_at(self, row: int, column: int) -> int: ...
    def get_row_header(self, row: int) -> Accessible: ...
    def get_selected_columns(self) -> list[int]: ...
    def get_selected_rows(self) -> list[int]: ...
    def get_summary(self) -> Accessible: ...
    def is_column_selected(self, column: int) -> bool: ...
    def is_row_selected(self, row: int) -> bool: ...
    def is_selected(self, row: int, column: int) -> bool: ...
    def remove_column_selection(self, column: int) -> bool: ...
    def remove_row_selection(self, row: int) -> bool: ...

class TableCell(GObject.GInterface, Protocol):
    """
    Interface AtspiTableCell
    """
    def get_column_header_cells(self) -> list[Accessible]: ...
    def get_column_index(self) -> int: ...
    def get_column_span(self) -> int: ...
    def get_position(self) -> tuple[int, int, int]: ...
    def get_row_column_span(self) -> tuple[int, int, int, int]: ...
    def get_row_header_cells(self) -> list[Accessible]: ...
    def get_row_span(self) -> int: ...
    def get_table(self) -> Accessible: ...

class Text(GObject.GInterface, Protocol):
    """
    Interface AtspiText
    """
    def add_selection(self, start_offset: int, end_offset: int) -> bool: ...
    def get_attribute_run(
        self, offset: int, include_defaults: bool
    ) -> tuple[dict[str, str], int, int]: ...
    def get_bounded_ranges(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        type: _CoordTypeValueType,
        clipTypeX: _TextClipTypeValueType,
        clipTypeY: _TextClipTypeValueType,
    ) -> list[TextRange]: ...
    def get_caret_offset(self) -> int: ...
    def get_character_at_offset(self, offset: int) -> int: ...
    def get_character_count(self) -> int: ...
    def get_character_extents(self, offset: int, type: _CoordTypeValueType) -> Rect: ...
    def get_default_attributes(self) -> dict[str, str]: ...
    def get_n_selections(self) -> int: ...
    def get_offset_at_point(self, x: int, y: int, type: _CoordTypeValueType) -> int: ...
    def get_range_extents(
        self, start_offset: int, end_offset: int, type: _CoordTypeValueType
    ) -> Rect: ...
    def get_selection(self, selection_num: int) -> Range: ...
    def get_string_at_offset(
        self, offset: int, granularity: _TextGranularityValueType
    ) -> TextRange: ...
    def get_text(self, start_offset: int, end_offset: int) -> str: ...
    def get_text_after_offset(
        self, offset: int, type: _TextBoundaryTypeValueType
    ) -> TextRange: ...
    def get_text_at_offset(
        self, offset: int, type: _TextBoundaryTypeValueType
    ) -> TextRange: ...
    def get_text_attribute_value(
        self, offset: int, attribute_name: str
    ) -> str | None: ...
    def get_text_attributes(self, offset: int) -> tuple[dict[str, str], int, int]: ...
    def get_text_before_offset(
        self, offset: int, type: _TextBoundaryTypeValueType
    ) -> TextRange: ...
    def remove_selection(self, selection_num: int) -> bool: ...
    def scroll_substring_to(
        self, start_offset: int, end_offset: int, type: _ScrollTypeValueType
    ) -> bool: ...
    def scroll_substring_to_point(
        self,
        start_offset: int,
        end_offset: int,
        coords: _CoordTypeValueType,
        x: int,
        y: int,
    ) -> bool: ...
    def set_caret_offset(self, new_offset: int) -> bool: ...
    def set_selection(
        self, selection_num: int, start_offset: int, end_offset: int
    ) -> bool: ...

class TextRange(GObject.GBoxed):
    """
    :Constructors:

    ::

        TextRange()
    """

    start_offset: int
    end_offset: int
    content: str

class TextSelection(GObject.GBoxed):
    """
    :Constructors:

    ::

        TextSelection()
    """

    start_object: Accessible
    start_offset: int
    end_object: Accessible
    end_offset: int
    start_is_active: bool

class Value(GObject.GInterface, Protocol):
    """
    Interface AtspiValue
    """
    def get_current_value(self) -> float: ...
    def get_maximum_value(self) -> float: ...
    def get_minimum_increment(self) -> float: ...
    def get_minimum_value(self) -> float: ...
    def get_text(self) -> str: ...
    def set_current_value(self, new_value: float) -> bool: ...

class Cache(GObject.GFlags):
    ALL = 1073741823
    ATTRIBUTES = 128
    CHILDREN = 2
    DEFAULT = 127
    DESCRIPTION = 8
    INTERFACES = 64
    NAME = 4
    NONE = 0
    PARENT = 1
    ROLE = 32
    STATES = 16
    UNDEFINED = 1073741824

_CacheLiteralType: TypeAlias = Literal[
    "ATSPI_CACHE_ALL",
    "ATSPI_CACHE_ATTRIBUTES",
    "ATSPI_CACHE_CHILDREN",
    "ATSPI_CACHE_DEFAULT",
    "ATSPI_CACHE_DESCRIPTION",
    "ATSPI_CACHE_INTERFACES",
    "ATSPI_CACHE_NAME",
    "ATSPI_CACHE_NONE",
    "ATSPI_CACHE_PARENT",
    "ATSPI_CACHE_ROLE",
    "ATSPI_CACHE_STATES",
    "ATSPI_CACHE_UNDEFINED",
    "all",
    "attributes",
    "children",
    "default",
    "description",
    "interfaces",
    "name",
    "none",
    "parent",
    "role",
    "states",
    "undefined",
]
_CacheValueType: TypeAlias = Cache | _CacheLiteralType | tuple[_CacheLiteralType, ...]

class DeviceCapability(GObject.GFlags):
    KEYBOARD_GRAB = 4
    KEYBOARD_MONITOR = 1
    KEYBOARD_SYNTH = 2
    POINTER_MONITOR = 8
    POINTER_SYNTH = 16
    TOUCH_MONITOR = 32
    TOUCH_SYNTH = 64

_DeviceCapabilityLiteralType: TypeAlias = Literal[
    "ATSPI_DEVICE_CAP_KEYBOARD_GRAB",
    "ATSPI_DEVICE_CAP_KEYBOARD_MONITOR",
    "ATSPI_DEVICE_CAP_KEYBOARD_SYNTH",
    "ATSPI_DEVICE_CAP_POINTER_MONITOR",
    "ATSPI_DEVICE_CAP_POINTER_SYNTH",
    "ATSPI_DEVICE_CAP_TOUCH_MONITOR",
    "ATSPI_DEVICE_CAP_TOUCH_SYNTH",
    "keyboard-grab",
    "keyboard-monitor",
    "keyboard-synth",
    "pointer-monitor",
    "pointer-synth",
    "touch-monitor",
    "touch-synth",
]
_DeviceCapabilityValueType: TypeAlias = (
    DeviceCapability
    | _DeviceCapabilityLiteralType
    | tuple[_DeviceCapabilityLiteralType, ...]
)

class KeyListenerSyncType(GObject.GFlags):
    ALL_WINDOWS = 4
    CANCONSUME = 2
    NOSYNC = 0
    SYNCHRONOUS = 1

_KeyListenerSyncTypeLiteralType: TypeAlias = Literal[
    "ATSPI_KEYLISTENER_ALL_WINDOWS",
    "ATSPI_KEYLISTENER_CANCONSUME",
    "ATSPI_KEYLISTENER_NOSYNC",
    "ATSPI_KEYLISTENER_SYNCHRONOUS",
    "all-windows",
    "canconsume",
    "nosync",
    "synchronous",
]
_KeyListenerSyncTypeValueType: TypeAlias = (
    KeyListenerSyncType
    | _KeyListenerSyncTypeLiteralType
    | tuple[_KeyListenerSyncTypeLiteralType, ...]
)

class CollectionMatchType(GObject.GEnum):
    ALL = 1
    ANY = 2
    EMPTY = 4
    INVALID = 0
    LAST_DEFINED = 5
    NONE = 3

_CollectionMatchTypeLiteralType: TypeAlias = Literal[
    "ATSPI_Collection_MATCH_ALL",
    "ATSPI_Collection_MATCH_ANY",
    "ATSPI_Collection_MATCH_EMPTY",
    "ATSPI_Collection_MATCH_INVALID",
    "ATSPI_Collection_MATCH_LAST_DEFINED",
    "ATSPI_Collection_MATCH_NONE",
    "all",
    "any",
    "empty",
    "invalid",
    "last-defined",
    "none",
]
_CollectionMatchTypeValueType: TypeAlias = (
    CollectionMatchType | _CollectionMatchTypeLiteralType
)

class CollectionSortOrder(GObject.GEnum):
    CANONICAL = 1
    FLOW = 2
    INVALID = 0
    LAST_DEFINED = 7
    REVERSE_CANONICAL = 4
    REVERSE_FLOW = 5
    REVERSE_TAB = 6
    TAB = 3

_CollectionSortOrderLiteralType: TypeAlias = Literal[
    "ATSPI_Collection_SORT_ORDER_CANONICAL",
    "ATSPI_Collection_SORT_ORDER_FLOW",
    "ATSPI_Collection_SORT_ORDER_INVALID",
    "ATSPI_Collection_SORT_ORDER_LAST_DEFINED",
    "ATSPI_Collection_SORT_ORDER_REVERSE_CANONICAL",
    "ATSPI_Collection_SORT_ORDER_REVERSE_FLOW",
    "ATSPI_Collection_SORT_ORDER_REVERSE_TAB",
    "ATSPI_Collection_SORT_ORDER_TAB",
    "canonical",
    "flow",
    "invalid",
    "last-defined",
    "reverse-canonical",
    "reverse-flow",
    "reverse-tab",
    "tab",
]
_CollectionSortOrderValueType: TypeAlias = (
    CollectionSortOrder | _CollectionSortOrderLiteralType
)

class CollectionTreeTraversalType(GObject.GEnum):
    INORDER = 2
    LAST_DEFINED = 3
    RESTRICT_CHILDREN = 0
    RESTRICT_SIBLING = 1

_CollectionTreeTraversalTypeLiteralType: TypeAlias = Literal[
    "ATSPI_Collection_TREE_INORDER",
    "ATSPI_Collection_TREE_LAST_DEFINED",
    "ATSPI_Collection_TREE_RESTRICT_CHILDREN",
    "ATSPI_Collection_TREE_RESTRICT_SIBLING",
    "inorder",
    "last-defined",
    "restrict-children",
    "restrict-sibling",
]
_CollectionTreeTraversalTypeValueType: TypeAlias = (
    CollectionTreeTraversalType | _CollectionTreeTraversalTypeLiteralType
)

class ComponentLayer(GObject.GEnum):
    BACKGROUND = 1
    CANVAS = 2
    INVALID = 0
    LAST_DEFINED = 8
    MDI = 4
    OVERLAY = 6
    POPUP = 5
    WIDGET = 3
    WINDOW = 7

_ComponentLayerLiteralType: TypeAlias = Literal[
    "ATSPI_LAYER_BACKGROUND",
    "ATSPI_LAYER_CANVAS",
    "ATSPI_LAYER_INVALID",
    "ATSPI_LAYER_LAST_DEFINED",
    "ATSPI_LAYER_MDI",
    "ATSPI_LAYER_OVERLAY",
    "ATSPI_LAYER_POPUP",
    "ATSPI_LAYER_WIDGET",
    "ATSPI_LAYER_WINDOW",
    "background",
    "canvas",
    "invalid",
    "last-defined",
    "mdi",
    "overlay",
    "popup",
    "widget",
    "window",
]
_ComponentLayerValueType: TypeAlias = ComponentLayer | _ComponentLayerLiteralType

class CoordType(GObject.GEnum):
    LAST_DEFINED = 3
    PARENT = 2
    SCREEN = 0
    WINDOW = 1

_CoordTypeLiteralType: TypeAlias = Literal[
    "ATSPI_COORD_TYPE_LAST_DEFINED",
    "ATSPI_COORD_TYPE_PARENT",
    "ATSPI_COORD_TYPE_SCREEN",
    "ATSPI_COORD_TYPE_WINDOW",
    "last-defined",
    "parent",
    "screen",
    "window",
]
_CoordTypeValueType: TypeAlias = CoordType | _CoordTypeLiteralType

class EventType(GObject.GEnum):
    BUTTON_PRESSED_EVENT = 2
    BUTTON_RELEASED_EVENT = 3
    EVENT_LAST_DEFINED = 4
    KEY_PRESSED_EVENT = 0
    KEY_RELEASED_EVENT = 1

_EventTypeLiteralType: TypeAlias = Literal[
    "ATSPI_BUTTON_PRESSED_EVENT",
    "ATSPI_BUTTON_RELEASED_EVENT",
    "ATSPI_EVENT_LAST_DEFINED",
    "ATSPI_KEY_PRESSED_EVENT",
    "ATSPI_KEY_RELEASED_EVENT",
    "button-pressed-event",
    "button-released-event",
    "event-last-defined",
    "key-pressed-event",
    "key-released-event",
]
_EventTypeValueType: TypeAlias = EventType | _EventTypeLiteralType

class KeyEventType(GObject.GEnum):
    EVENT_LAST_DEFINED = 2
    PRESSED = 0
    RELEASED = 1

_KeyEventTypeLiteralType: TypeAlias = Literal[
    "ATSPI_KEY_EVENT_LAST_DEFINED",
    "ATSPI_KEY_PRESSED",
    "ATSPI_KEY_RELEASED",
    "event-last-defined",
    "pressed",
    "released",
]
_KeyEventTypeValueType: TypeAlias = KeyEventType | _KeyEventTypeLiteralType

class KeySynthType(GObject.GEnum):
    LOCKMODIFIERS = 5
    PRESS = 0
    PRESSRELEASE = 2
    RELEASE = 1
    STRING = 4
    SYM = 3
    SYNTH_LAST_DEFINED = 7
    UNLOCKMODIFIERS = 6

_KeySynthTypeLiteralType: TypeAlias = Literal[
    "ATSPI_KEY_LOCKMODIFIERS",
    "ATSPI_KEY_PRESS",
    "ATSPI_KEY_PRESSRELEASE",
    "ATSPI_KEY_RELEASE",
    "ATSPI_KEY_STRING",
    "ATSPI_KEY_SYM",
    "ATSPI_KEY_SYNTH_LAST_DEFINED",
    "ATSPI_KEY_UNLOCKMODIFIERS",
    "lockmodifiers",
    "press",
    "pressrelease",
    "release",
    "string",
    "sym",
    "synth-last-defined",
    "unlockmodifiers",
]
_KeySynthTypeValueType: TypeAlias = KeySynthType | _KeySynthTypeLiteralType

class Live(GObject.GEnum):
    ASSERTIVE = 2
    NONE = 0
    POLITE = 1

_LiveLiteralType: TypeAlias = Literal[
    "ATSPI_LIVE_ASSERTIVE",
    "ATSPI_LIVE_NONE",
    "ATSPI_LIVE_POLITE",
    "assertive",
    "none",
    "polite",
]
_LiveValueType: TypeAlias = Live | _LiveLiteralType

class LocaleType(GObject.GEnum):
    COLLATE = 1
    CTYPE = 2
    LAST_DEFINED = 6
    MESSAGES = 0
    MONETARY = 3
    NUMERIC = 4
    TIME = 5

_LocaleTypeLiteralType: TypeAlias = Literal[
    "ATSPI_LOCALE_TYPE_COLLATE",
    "ATSPI_LOCALE_TYPE_CTYPE",
    "ATSPI_LOCALE_TYPE_LAST_DEFINED",
    "ATSPI_LOCALE_TYPE_MESSAGES",
    "ATSPI_LOCALE_TYPE_MONETARY",
    "ATSPI_LOCALE_TYPE_NUMERIC",
    "ATSPI_LOCALE_TYPE_TIME",
    "collate",
    "ctype",
    "last-defined",
    "messages",
    "monetary",
    "numeric",
    "time",
]
_LocaleTypeValueType: TypeAlias = LocaleType | _LocaleTypeLiteralType

class ModifierType(GObject.GEnum):
    ALT = 3
    CONTROL = 2
    META = 4
    META2 = 5
    META3 = 6
    NUMLOCK = 14
    SHIFT = 0
    SHIFTLOCK = 1
    SUPER = 6

_ModifierTypeLiteralType: TypeAlias = Literal[
    "ATSPI_MODIFIER_ALT",
    "ATSPI_MODIFIER_CONTROL",
    "ATSPI_MODIFIER_META",
    "ATSPI_MODIFIER_META2",
    "ATSPI_MODIFIER_META3",
    "ATSPI_MODIFIER_NUMLOCK",
    "ATSPI_MODIFIER_SHIFT",
    "ATSPI_MODIFIER_SHIFTLOCK",
    "alt",
    "control",
    "meta",
    "meta2",
    "meta3",
    "numlock",
    "shift",
    "shiftlock",
]
_ModifierTypeValueType: TypeAlias = ModifierType | _ModifierTypeLiteralType

class RelationType(GObject.GEnum):
    CONTROLLED_BY = 4
    CONTROLLER_FOR = 3
    DESCRIBED_BY = 18
    DESCRIPTION_FOR = 17
    DETAILS = 19
    DETAILS_FOR = 20
    EMBEDDED_BY = 14
    EMBEDS = 13
    ERROR_FOR = 22
    ERROR_MESSAGE = 21
    EXTENDED = 9
    FLOWS_FROM = 11
    FLOWS_TO = 10
    LABELLED_BY = 2
    LABEL_FOR = 1
    LAST_DEFINED = 23
    MEMBER_OF = 5
    NODE_CHILD_OF = 7
    NODE_PARENT_OF = 8
    NULL = 0
    PARENT_WINDOW_OF = 16
    POPUP_FOR = 15
    SUBWINDOW_OF = 12
    TOOLTIP_FOR = 6

_RelationTypeLiteralType: TypeAlias = Literal[
    "ATSPI_RELATION_CONTROLLED_BY",
    "ATSPI_RELATION_CONTROLLER_FOR",
    "ATSPI_RELATION_DESCRIBED_BY",
    "ATSPI_RELATION_DESCRIPTION_FOR",
    "ATSPI_RELATION_DETAILS",
    "ATSPI_RELATION_DETAILS_FOR",
    "ATSPI_RELATION_EMBEDDED_BY",
    "ATSPI_RELATION_EMBEDS",
    "ATSPI_RELATION_ERROR_FOR",
    "ATSPI_RELATION_ERROR_MESSAGE",
    "ATSPI_RELATION_EXTENDED",
    "ATSPI_RELATION_FLOWS_FROM",
    "ATSPI_RELATION_FLOWS_TO",
    "ATSPI_RELATION_LABELLED_BY",
    "ATSPI_RELATION_LABEL_FOR",
    "ATSPI_RELATION_LAST_DEFINED",
    "ATSPI_RELATION_MEMBER_OF",
    "ATSPI_RELATION_NODE_CHILD_OF",
    "ATSPI_RELATION_NODE_PARENT_OF",
    "ATSPI_RELATION_NULL",
    "ATSPI_RELATION_PARENT_WINDOW_OF",
    "ATSPI_RELATION_POPUP_FOR",
    "ATSPI_RELATION_SUBWINDOW_OF",
    "ATSPI_RELATION_TOOLTIP_FOR",
    "controlled-by",
    "controller-for",
    "described-by",
    "description-for",
    "details",
    "details-for",
    "embedded-by",
    "embeds",
    "error-for",
    "error-message",
    "extended",
    "flows-from",
    "flows-to",
    "label-for",
    "labelled-by",
    "last-defined",
    "member-of",
    "node-child-of",
    "node-parent-of",
    "null",
    "parent-window-of",
    "popup-for",
    "subwindow-of",
    "tooltip-for",
]
_RelationTypeValueType: TypeAlias = RelationType | _RelationTypeLiteralType

class Role(GObject.GEnum):
    ACCELERATOR_LABEL = 1
    ALERT = 2
    ANIMATION = 3
    APPLICATION = 75
    ARROW = 4
    ARTICLE = 109
    AUDIO = 106
    AUTOCOMPLETE = 76
    BLOCK_QUOTE = 105
    BUTTON = 43
    CALENDAR = 5
    CANVAS = 6
    CAPTION = 81
    CHART = 80
    CHECK_BOX = 7
    CHECK_MENU_ITEM = 8
    COLOR_CHOOSER = 9
    COLUMN_HEADER = 10
    COMBO_BOX = 11
    COMMENT = 97
    CONTENT_DELETION = 125
    CONTENT_INSERTION = 126
    DATE_EDITOR = 12
    DEFINITION = 108
    DESCRIPTION_LIST = 121
    DESCRIPTION_TERM = 122
    DESCRIPTION_VALUE = 123
    DESKTOP_FRAME = 14
    DESKTOP_ICON = 13
    DIAL = 15
    DIALOG = 16
    DIRECTORY_PANE = 17
    DOCUMENT_EMAIL = 96
    DOCUMENT_FRAME = 82
    DOCUMENT_PRESENTATION = 93
    DOCUMENT_SPREADSHEET = 92
    DOCUMENT_TEXT = 94
    DOCUMENT_WEB = 95
    DRAWING_AREA = 18
    EDITBAR = 77
    EMBEDDED = 78
    ENTRY = 79
    EXTENDED = 70
    FILE_CHOOSER = 19
    FILLER = 20
    FOCUS_TRAVERSABLE = 21
    FONT_CHOOSER = 22
    FOOTER = 72
    FOOTNOTE = 124
    FORM = 87
    FRAME = 23
    GLASS_PANE = 24
    GROUPING = 99
    HEADER = 71
    HEADING = 83
    HTML_CONTAINER = 25
    ICON = 26
    IMAGE = 27
    IMAGE_MAP = 100
    INFO_BAR = 102
    INPUT_METHOD_WINDOW = 89
    INTERNAL_FRAME = 28
    INVALID = 0
    LABEL = 29
    LANDMARK = 110
    LAST_DEFINED = 131
    LAYERED_PANE = 30
    LEVEL_BAR = 103
    LINK = 88
    LIST = 31
    LIST_BOX = 98
    LIST_ITEM = 32
    LOG = 111
    MARK = 127
    MARQUEE = 112
    MATH = 113
    MATH_FRACTION = 117
    MATH_ROOT = 118
    MENU = 33
    MENU_BAR = 34
    MENU_ITEM = 35
    NOTIFICATION = 101
    OPTION_PANE = 36
    PAGE = 84
    PAGE_TAB = 37
    PAGE_TAB_LIST = 38
    PANEL = 39
    PARAGRAPH = 73
    PASSWORD_TEXT = 40
    POPUP_MENU = 41
    PROGRESS_BAR = 42
    PUSH_BUTTON = 43
    PUSH_BUTTON_MENU = 129
    RADIO_BUTTON = 44
    RADIO_MENU_ITEM = 45
    RATING = 114
    REDUNDANT_OBJECT = 86
    ROOT_PANE = 46
    ROW_HEADER = 47
    RULER = 74
    SCROLL_BAR = 48
    SCROLL_PANE = 49
    SECTION = 85
    SEPARATOR = 50
    SLIDER = 51
    SPIN_BUTTON = 52
    SPLIT_PANE = 53
    STATIC = 116
    STATUS_BAR = 54
    SUBSCRIPT = 119
    SUGGESTION = 128
    SUPERSCRIPT = 120
    SWITCH = 130
    TABLE = 55
    TABLE_CELL = 56
    TABLE_COLUMN_HEADER = 57
    TABLE_ROW = 90
    TABLE_ROW_HEADER = 58
    TEAROFF_MENU_ITEM = 59
    TERMINAL = 60
    TEXT = 61
    TIMER = 115
    TITLE_BAR = 104
    TOGGLE_BUTTON = 62
    TOOL_BAR = 63
    TOOL_TIP = 64
    TREE = 65
    TREE_ITEM = 91
    TREE_TABLE = 66
    UNKNOWN = 67
    VIDEO = 107
    VIEWPORT = 68
    WINDOW = 69
    @staticmethod
    def get_localized_name(role: _RoleValueType) -> str: ...
    @staticmethod
    def get_name(role: _RoleValueType) -> str: ...

_RoleLiteralType: TypeAlias = Literal[
    "ATSPI_ROLE_ACCELERATOR_LABEL",
    "ATSPI_ROLE_ALERT",
    "ATSPI_ROLE_ANIMATION",
    "ATSPI_ROLE_APPLICATION",
    "ATSPI_ROLE_ARROW",
    "ATSPI_ROLE_ARTICLE",
    "ATSPI_ROLE_AUDIO",
    "ATSPI_ROLE_AUTOCOMPLETE",
    "ATSPI_ROLE_BLOCK_QUOTE",
    "ATSPI_ROLE_BUTTON",
    "ATSPI_ROLE_CALENDAR",
    "ATSPI_ROLE_CANVAS",
    "ATSPI_ROLE_CAPTION",
    "ATSPI_ROLE_CHART",
    "ATSPI_ROLE_CHECK_BOX",
    "ATSPI_ROLE_CHECK_MENU_ITEM",
    "ATSPI_ROLE_COLOR_CHOOSER",
    "ATSPI_ROLE_COLUMN_HEADER",
    "ATSPI_ROLE_COMBO_BOX",
    "ATSPI_ROLE_COMMENT",
    "ATSPI_ROLE_CONTENT_DELETION",
    "ATSPI_ROLE_CONTENT_INSERTION",
    "ATSPI_ROLE_DATE_EDITOR",
    "ATSPI_ROLE_DEFINITION",
    "ATSPI_ROLE_DESCRIPTION_LIST",
    "ATSPI_ROLE_DESCRIPTION_TERM",
    "ATSPI_ROLE_DESCRIPTION_VALUE",
    "ATSPI_ROLE_DESKTOP_FRAME",
    "ATSPI_ROLE_DESKTOP_ICON",
    "ATSPI_ROLE_DIAL",
    "ATSPI_ROLE_DIALOG",
    "ATSPI_ROLE_DIRECTORY_PANE",
    "ATSPI_ROLE_DOCUMENT_EMAIL",
    "ATSPI_ROLE_DOCUMENT_FRAME",
    "ATSPI_ROLE_DOCUMENT_PRESENTATION",
    "ATSPI_ROLE_DOCUMENT_SPREADSHEET",
    "ATSPI_ROLE_DOCUMENT_TEXT",
    "ATSPI_ROLE_DOCUMENT_WEB",
    "ATSPI_ROLE_DRAWING_AREA",
    "ATSPI_ROLE_EDITBAR",
    "ATSPI_ROLE_EMBEDDED",
    "ATSPI_ROLE_ENTRY",
    "ATSPI_ROLE_EXTENDED",
    "ATSPI_ROLE_FILE_CHOOSER",
    "ATSPI_ROLE_FILLER",
    "ATSPI_ROLE_FOCUS_TRAVERSABLE",
    "ATSPI_ROLE_FONT_CHOOSER",
    "ATSPI_ROLE_FOOTER",
    "ATSPI_ROLE_FOOTNOTE",
    "ATSPI_ROLE_FORM",
    "ATSPI_ROLE_FRAME",
    "ATSPI_ROLE_GLASS_PANE",
    "ATSPI_ROLE_GROUPING",
    "ATSPI_ROLE_HEADER",
    "ATSPI_ROLE_HEADING",
    "ATSPI_ROLE_HTML_CONTAINER",
    "ATSPI_ROLE_ICON",
    "ATSPI_ROLE_IMAGE",
    "ATSPI_ROLE_IMAGE_MAP",
    "ATSPI_ROLE_INFO_BAR",
    "ATSPI_ROLE_INPUT_METHOD_WINDOW",
    "ATSPI_ROLE_INTERNAL_FRAME",
    "ATSPI_ROLE_INVALID",
    "ATSPI_ROLE_LABEL",
    "ATSPI_ROLE_LANDMARK",
    "ATSPI_ROLE_LAST_DEFINED",
    "ATSPI_ROLE_LAYERED_PANE",
    "ATSPI_ROLE_LEVEL_BAR",
    "ATSPI_ROLE_LINK",
    "ATSPI_ROLE_LIST",
    "ATSPI_ROLE_LIST_BOX",
    "ATSPI_ROLE_LIST_ITEM",
    "ATSPI_ROLE_LOG",
    "ATSPI_ROLE_MARK",
    "ATSPI_ROLE_MARQUEE",
    "ATSPI_ROLE_MATH",
    "ATSPI_ROLE_MATH_FRACTION",
    "ATSPI_ROLE_MATH_ROOT",
    "ATSPI_ROLE_MENU",
    "ATSPI_ROLE_MENU_BAR",
    "ATSPI_ROLE_MENU_ITEM",
    "ATSPI_ROLE_NOTIFICATION",
    "ATSPI_ROLE_OPTION_PANE",
    "ATSPI_ROLE_PAGE",
    "ATSPI_ROLE_PAGE_TAB",
    "ATSPI_ROLE_PAGE_TAB_LIST",
    "ATSPI_ROLE_PANEL",
    "ATSPI_ROLE_PARAGRAPH",
    "ATSPI_ROLE_PASSWORD_TEXT",
    "ATSPI_ROLE_POPUP_MENU",
    "ATSPI_ROLE_PROGRESS_BAR",
    "ATSPI_ROLE_PUSH_BUTTON_MENU",
    "ATSPI_ROLE_RADIO_BUTTON",
    "ATSPI_ROLE_RADIO_MENU_ITEM",
    "ATSPI_ROLE_RATING",
    "ATSPI_ROLE_REDUNDANT_OBJECT",
    "ATSPI_ROLE_ROOT_PANE",
    "ATSPI_ROLE_ROW_HEADER",
    "ATSPI_ROLE_RULER",
    "ATSPI_ROLE_SCROLL_BAR",
    "ATSPI_ROLE_SCROLL_PANE",
    "ATSPI_ROLE_SECTION",
    "ATSPI_ROLE_SEPARATOR",
    "ATSPI_ROLE_SLIDER",
    "ATSPI_ROLE_SPIN_BUTTON",
    "ATSPI_ROLE_SPLIT_PANE",
    "ATSPI_ROLE_STATIC",
    "ATSPI_ROLE_STATUS_BAR",
    "ATSPI_ROLE_SUBSCRIPT",
    "ATSPI_ROLE_SUGGESTION",
    "ATSPI_ROLE_SUPERSCRIPT",
    "ATSPI_ROLE_SWITCH",
    "ATSPI_ROLE_TABLE",
    "ATSPI_ROLE_TABLE_CELL",
    "ATSPI_ROLE_TABLE_COLUMN_HEADER",
    "ATSPI_ROLE_TABLE_ROW",
    "ATSPI_ROLE_TABLE_ROW_HEADER",
    "ATSPI_ROLE_TEAROFF_MENU_ITEM",
    "ATSPI_ROLE_TERMINAL",
    "ATSPI_ROLE_TEXT",
    "ATSPI_ROLE_TIMER",
    "ATSPI_ROLE_TITLE_BAR",
    "ATSPI_ROLE_TOGGLE_BUTTON",
    "ATSPI_ROLE_TOOL_BAR",
    "ATSPI_ROLE_TOOL_TIP",
    "ATSPI_ROLE_TREE",
    "ATSPI_ROLE_TREE_ITEM",
    "ATSPI_ROLE_TREE_TABLE",
    "ATSPI_ROLE_UNKNOWN",
    "ATSPI_ROLE_VIDEO",
    "ATSPI_ROLE_VIEWPORT",
    "ATSPI_ROLE_WINDOW",
    "accelerator-label",
    "alert",
    "animation",
    "application",
    "arrow",
    "article",
    "audio",
    "autocomplete",
    "block-quote",
    "button",
    "calendar",
    "canvas",
    "caption",
    "chart",
    "check-box",
    "check-menu-item",
    "color-chooser",
    "column-header",
    "combo-box",
    "comment",
    "content-deletion",
    "content-insertion",
    "date-editor",
    "definition",
    "description-list",
    "description-term",
    "description-value",
    "desktop-frame",
    "desktop-icon",
    "dial",
    "dialog",
    "directory-pane",
    "document-email",
    "document-frame",
    "document-presentation",
    "document-spreadsheet",
    "document-text",
    "document-web",
    "drawing-area",
    "editbar",
    "embedded",
    "entry",
    "extended",
    "file-chooser",
    "filler",
    "focus-traversable",
    "font-chooser",
    "footer",
    "footnote",
    "form",
    "frame",
    "glass-pane",
    "grouping",
    "header",
    "heading",
    "html-container",
    "icon",
    "image",
    "image-map",
    "info-bar",
    "input-method-window",
    "internal-frame",
    "invalid",
    "label",
    "landmark",
    "last-defined",
    "layered-pane",
    "level-bar",
    "link",
    "list",
    "list-box",
    "list-item",
    "log",
    "mark",
    "marquee",
    "math",
    "math-fraction",
    "math-root",
    "menu",
    "menu-bar",
    "menu-item",
    "notification",
    "option-pane",
    "page",
    "page-tab",
    "page-tab-list",
    "panel",
    "paragraph",
    "password-text",
    "popup-menu",
    "progress-bar",
    "push-button-menu",
    "radio-button",
    "radio-menu-item",
    "rating",
    "redundant-object",
    "root-pane",
    "row-header",
    "ruler",
    "scroll-bar",
    "scroll-pane",
    "section",
    "separator",
    "slider",
    "spin-button",
    "split-pane",
    "static",
    "status-bar",
    "subscript",
    "suggestion",
    "superscript",
    "switch",
    "table",
    "table-cell",
    "table-column-header",
    "table-row",
    "table-row-header",
    "tearoff-menu-item",
    "terminal",
    "text",
    "timer",
    "title-bar",
    "toggle-button",
    "tool-bar",
    "tool-tip",
    "tree",
    "tree-item",
    "tree-table",
    "unknown",
    "video",
    "viewport",
    "window",
]
_RoleValueType: TypeAlias = Role | _RoleLiteralType

class ScrollType(GObject.GEnum):
    ANYWHERE = 6
    BOTTOM_EDGE = 3
    BOTTOM_RIGHT = 1
    LAST_DEFINED = 7
    LEFT_EDGE = 4
    RIGHT_EDGE = 5
    TOP_EDGE = 2
    TOP_LEFT = 0

_ScrollTypeLiteralType: TypeAlias = Literal[
    "ATSPI_SCROLL_ANYWHERE",
    "ATSPI_SCROLL_BOTTOM_EDGE",
    "ATSPI_SCROLL_BOTTOM_RIGHT",
    "ATSPI_SCROLL_LAST_DEFINED",
    "ATSPI_SCROLL_LEFT_EDGE",
    "ATSPI_SCROLL_RIGHT_EDGE",
    "ATSPI_SCROLL_TOP_EDGE",
    "ATSPI_SCROLL_TOP_LEFT",
    "anywhere",
    "bottom-edge",
    "bottom-right",
    "last-defined",
    "left-edge",
    "right-edge",
    "top-edge",
    "top-left",
]
_ScrollTypeValueType: TypeAlias = ScrollType | _ScrollTypeLiteralType

class StateType(GObject.GEnum):
    ACTIVE = 1
    ANIMATED = 35
    ARMED = 2
    BUSY = 3
    CHECKABLE = 41
    CHECKED = 4
    COLLAPSED = 5
    DEFAULT = 39
    DEFUNCT = 6
    EDITABLE = 7
    ENABLED = 8
    EXPANDABLE = 9
    EXPANDED = 10
    FOCUSABLE = 11
    FOCUSED = 12
    HAS_POPUP = 42
    HAS_TOOLTIP = 13
    HORIZONTAL = 14
    ICONIFIED = 15
    INDETERMINATE = 32
    INVALID = 0
    INVALID_ENTRY = 36
    IS_DEFAULT = 39
    LAST_DEFINED = 44
    MANAGES_DESCENDANTS = 31
    MODAL = 16
    MULTISELECTABLE = 18
    MULTI_LINE = 17
    OPAQUE = 19
    PRESSED = 20
    READ_ONLY = 43
    REQUIRED = 33
    RESIZABLE = 21
    SELECTABLE = 22
    SELECTABLE_TEXT = 38
    SELECTED = 23
    SENSITIVE = 24
    SHOWING = 25
    SINGLE_LINE = 26
    STALE = 27
    SUPPORTS_AUTOCOMPLETION = 37
    TRANSIENT = 28
    TRUNCATED = 34
    VERTICAL = 29
    VISIBLE = 30
    VISITED = 40

_StateTypeLiteralType: TypeAlias = Literal[
    "ATSPI_STATE_ACTIVE",
    "ATSPI_STATE_ANIMATED",
    "ATSPI_STATE_ARMED",
    "ATSPI_STATE_BUSY",
    "ATSPI_STATE_CHECKABLE",
    "ATSPI_STATE_CHECKED",
    "ATSPI_STATE_COLLAPSED",
    "ATSPI_STATE_DEFUNCT",
    "ATSPI_STATE_EDITABLE",
    "ATSPI_STATE_ENABLED",
    "ATSPI_STATE_EXPANDABLE",
    "ATSPI_STATE_EXPANDED",
    "ATSPI_STATE_FOCUSABLE",
    "ATSPI_STATE_FOCUSED",
    "ATSPI_STATE_HAS_POPUP",
    "ATSPI_STATE_HAS_TOOLTIP",
    "ATSPI_STATE_HORIZONTAL",
    "ATSPI_STATE_ICONIFIED",
    "ATSPI_STATE_INDETERMINATE",
    "ATSPI_STATE_INVALID",
    "ATSPI_STATE_INVALID_ENTRY",
    "ATSPI_STATE_IS_DEFAULT",
    "ATSPI_STATE_LAST_DEFINED",
    "ATSPI_STATE_MANAGES_DESCENDANTS",
    "ATSPI_STATE_MODAL",
    "ATSPI_STATE_MULTISELECTABLE",
    "ATSPI_STATE_MULTI_LINE",
    "ATSPI_STATE_OPAQUE",
    "ATSPI_STATE_PRESSED",
    "ATSPI_STATE_READ_ONLY",
    "ATSPI_STATE_REQUIRED",
    "ATSPI_STATE_RESIZABLE",
    "ATSPI_STATE_SELECTABLE",
    "ATSPI_STATE_SELECTABLE_TEXT",
    "ATSPI_STATE_SELECTED",
    "ATSPI_STATE_SENSITIVE",
    "ATSPI_STATE_SHOWING",
    "ATSPI_STATE_SINGLE_LINE",
    "ATSPI_STATE_STALE",
    "ATSPI_STATE_SUPPORTS_AUTOCOMPLETION",
    "ATSPI_STATE_TRANSIENT",
    "ATSPI_STATE_TRUNCATED",
    "ATSPI_STATE_VERTICAL",
    "ATSPI_STATE_VISIBLE",
    "ATSPI_STATE_VISITED",
    "active",
    "animated",
    "armed",
    "busy",
    "checkable",
    "checked",
    "collapsed",
    "defunct",
    "editable",
    "enabled",
    "expandable",
    "expanded",
    "focusable",
    "focused",
    "has-popup",
    "has-tooltip",
    "horizontal",
    "iconified",
    "indeterminate",
    "invalid",
    "invalid-entry",
    "is-default",
    "last-defined",
    "manages-descendants",
    "modal",
    "multi-line",
    "multiselectable",
    "opaque",
    "pressed",
    "read-only",
    "required",
    "resizable",
    "selectable",
    "selectable-text",
    "selected",
    "sensitive",
    "showing",
    "single-line",
    "stale",
    "supports-autocompletion",
    "transient",
    "truncated",
    "vertical",
    "visible",
    "visited",
]
_StateTypeValueType: TypeAlias = StateType | _StateTypeLiteralType

class TextBoundaryType(GObject.GEnum):
    CHAR = 0
    LAST_DEFINED = 7
    LINE_END = 6
    LINE_START = 5
    SENTENCE_END = 4
    SENTENCE_START = 3
    WORD_END = 2
    WORD_START = 1

_TextBoundaryTypeLiteralType: TypeAlias = Literal[
    "ATSPI_TEXT_BOUNDARY_CHAR",
    "ATSPI_TEXT_BOUNDARY_LAST_DEFINED",
    "ATSPI_TEXT_BOUNDARY_LINE_END",
    "ATSPI_TEXT_BOUNDARY_LINE_START",
    "ATSPI_TEXT_BOUNDARY_SENTENCE_END",
    "ATSPI_TEXT_BOUNDARY_SENTENCE_START",
    "ATSPI_TEXT_BOUNDARY_WORD_END",
    "ATSPI_TEXT_BOUNDARY_WORD_START",
    "char",
    "last-defined",
    "line-end",
    "line-start",
    "sentence-end",
    "sentence-start",
    "word-end",
    "word-start",
]
_TextBoundaryTypeValueType: TypeAlias = TextBoundaryType | _TextBoundaryTypeLiteralType

class TextClipType(GObject.GEnum):
    BOTH = 3
    LAST_DEFINED = 4
    MAX = 2
    MIN = 1
    NONE = 0

_TextClipTypeLiteralType: TypeAlias = Literal[
    "ATSPI_TEXT_CLIP_BOTH",
    "ATSPI_TEXT_CLIP_LAST_DEFINED",
    "ATSPI_TEXT_CLIP_MAX",
    "ATSPI_TEXT_CLIP_MIN",
    "ATSPI_TEXT_CLIP_NONE",
    "both",
    "last-defined",
    "max",
    "min",
    "none",
]
_TextClipTypeValueType: TypeAlias = TextClipType | _TextClipTypeLiteralType

class TextGranularity(GObject.GEnum):
    CHAR = 0
    LINE = 3
    PARAGRAPH = 4
    SENTENCE = 2
    WORD = 1

_TextGranularityLiteralType: TypeAlias = Literal[
    "ATSPI_TEXT_GRANULARITY_CHAR",
    "ATSPI_TEXT_GRANULARITY_LINE",
    "ATSPI_TEXT_GRANULARITY_PARAGRAPH",
    "ATSPI_TEXT_GRANULARITY_SENTENCE",
    "ATSPI_TEXT_GRANULARITY_WORD",
    "char",
    "line",
    "paragraph",
    "sentence",
    "word",
]
_TextGranularityValueType: TypeAlias = TextGranularity | _TextGranularityLiteralType
