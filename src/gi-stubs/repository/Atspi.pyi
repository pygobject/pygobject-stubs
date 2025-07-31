import typing

from gi.repository import DBus
from gi.repository import GLib
from gi.repository import GObject

T = typing.TypeVar("T")

COMPONENTLAYER_COUNT: int = 9
COORD_TYPE_COUNT: int = 3
DBUS_INTERFACE_ACCESSIBLE: str = "org.a11y.atspi.Accessible"
DBUS_INTERFACE_ACTION: str = "org.a11y.atspi.Action"
DBUS_INTERFACE_APPLICATION: str = "org.a11y.atspi.Application"
DBUS_INTERFACE_CACHE: str = "org.a11y.atspi.Cache"
DBUS_INTERFACE_COLLECTION: str = "org.a11y.atspi.Collection"
DBUS_INTERFACE_COMPONENT: str = "org.a11y.atspi.Component"
DBUS_INTERFACE_DEC: str = "org.a11y.atspi.DeviceEventController"
DBUS_INTERFACE_DEVICE_EVENT_LISTENER: str = "org.a11y.atspi.DeviceEventListener"
DBUS_INTERFACE_DOCUMENT: str = "org.a11y.atspi.Document"
DBUS_INTERFACE_EDITABLE_TEXT: str = "org.a11y.atspi.EditableText"
DBUS_INTERFACE_EVENT_KEYBOARD: str = "org.a11y.atspi.Event.Keyboard"
DBUS_INTERFACE_EVENT_MOUSE: str = "org.a11y.atspi.Event.Mouse"
DBUS_INTERFACE_EVENT_OBJECT: str = "org.a11y.atspi.Event.Object"
DBUS_INTERFACE_EVENT_SCREEN_READER: str = "org.a11y.atspi.Event.ScreenReader"
DBUS_INTERFACE_HYPERLINK: str = "org.a11y.atspi.Hyperlink"
DBUS_INTERFACE_HYPERTEXT: str = "org.a11y.atspi.Hypertext"
DBUS_INTERFACE_IMAGE: str = "org.a11y.atspi.Image"
DBUS_INTERFACE_REGISTRY: str = "org.a11y.atspi.Registry"
DBUS_INTERFACE_SELECTION: str = "org.a11y.atspi.Selection"
DBUS_INTERFACE_SOCKET: str = "org.a11y.atspi.Socket"
DBUS_INTERFACE_TABLE: str = "org.a11y.atspi.Table"
DBUS_INTERFACE_TABLE_CELL: str = "org.a11y.atspi.TableCell"
DBUS_INTERFACE_TEXT: str = "org.a11y.atspi.Text"
DBUS_INTERFACE_VALUE: str = "org.a11y.atspi.Value"
DBUS_NAME_REGISTRY: str = "org.a11y.atspi.Registry"
DBUS_PATH_DEC: str = "/org/a11y/atspi/registry/deviceeventcontroller"
DBUS_PATH_NULL: str = "/org/a11y/atspi/null"
DBUS_PATH_REGISTRY: str = "/org/a11y/atspi/registry"
DBUS_PATH_ROOT: str = "/org/a11y/atspi/accessible/root"
DBUS_PATH_SCREEN_READER: str = "/org/a11y/atspi/screenreader"
EVENTTYPE_COUNT: int = 4
KEYEVENTTYPE_COUNT: int = 2
KEYSYNTHTYPE_COUNT: int = 5
LOCALE_TYPE_COUNT: int = 6
MATCHTYPES_COUNT: int = 6
MODIFIERTYPE_COUNT: int = 8
RELATIONTYPE_COUNT: int = 24
ROLE_COUNT: int = 131
SCROLLTYPE_COUNT: int = 7
SORTORDER_COUNT: int = 8
STATETYPE_COUNT: int = 42
TEXT_BOUNDARY_TYPE_COUNT: int = 7
TEXT_CLIP_TYPE_COUNT: int = 4
TREETRAVERSALTYPE_COUNT: int = 4
_lock = ...  # FIXME Constant
_namespace: str = "Atspi"
_version: str = "2.0"

def deregister_device_event_listener(
    listener: DeviceListener, filter: None
) -> bool: ...
def deregister_keystroke_listener(
    listener: DeviceListener,
    key_set: typing.Optional[typing.Sequence[KeyDefinition]],
    modmask: int,
    event_types: int,
) -> bool: ...
def event_main() -> None: ...
def event_quit() -> None: ...
def exit() -> int: ...
def generate_keyboard_event(
    keyval: int, keystring: typing.Optional[str], synth_type: KeySynthType
) -> bool: ...
def generate_mouse_event(x: int, y: int, name: str) -> bool: ...
def generate_mouse_event_async(
    x: int,
    y: int,
    name: str,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *callback_data: typing.Any,
) -> None: ...
def get_desktop(i: int) -> Accessible: ...
def get_desktop_count() -> int: ...
def get_desktop_list() -> list[Accessible]: ...
def get_version() -> typing.Tuple[int, int, int]: ...
def init() -> int: ...
def is_initialized() -> bool: ...
def register_device_event_listener(
    listener: DeviceListener, event_types: int, filter: None
) -> bool: ...
def register_keystroke_listener(
    listener: DeviceListener,
    key_set: typing.Optional[typing.Sequence[KeyDefinition]],
    modmask: int,
    event_types: int,
    sync_type: KeyListenerSyncType,
) -> bool: ...
def role_get_localized_name(role: Role) -> str: ...
def role_get_name(role: Role) -> str: ...
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

    parent: Object = ...
    accessible_parent: Accessible = ...
    children: list[None] = ...
    role: Role = ...
    interfaces: int = ...
    name: str = ...
    description: str = ...
    states: StateSet = ...
    attributes: dict[None, None] = ...
    cached_properties: int = ...
    priv: AccessiblePrivate = ...
    def clear_cache(self) -> None: ...
    def clear_cache_single(self) -> None: ...
    def do_mode_changed(self, enabled: bool) -> None: ...
    def do_region_changed(self, current_offset: int, last_offset: int) -> None: ...
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
    def get_parent(self) -> typing.Optional[Accessible]: ...
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
    def set_cache_mask(self, mask: Cache) -> None: ...

class AccessibleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AccessibleClass()
    """

    parent_class: ObjectClass = ...
    region_changed: typing.Callable[[Accessible, int, int], None] = ...
    mode_changed: typing.Callable[[Accessible, bool], None] = ...

class AccessiblePrivate(GObject.GPointer): ...

class Action(GObject.GInterface):
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

    parent: GObject.Object = ...
    hash: dict[None, None] = ...
    bus_name: str = ...
    bus: DBus.Connection = ...
    root: None = ...
    cache: Cache = ...
    toolkit_name: str = ...
    toolkit_version: str = ...
    atspi_version: str = ...
    time_added: None = ...

class ApplicationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationClass()
    """

    parent_class: GObject.ObjectClass = ...

class Collection(GObject.GInterface):
    """
    Interface AtspiCollection
    """

    def get_active_descendant(self) -> Accessible: ...
    def get_matches(
        self, rule: MatchRule, sortby: CollectionSortOrder, count: int, traverse: bool
    ) -> list[Accessible]: ...
    def get_matches_from(
        self,
        current_object: Accessible,
        rule: MatchRule,
        sortby: CollectionSortOrder,
        tree: CollectionTreeTraversalType,
        count: int,
        traverse: bool,
    ) -> list[Accessible]: ...
    def get_matches_to(
        self,
        current_object: Accessible,
        rule: MatchRule,
        sortby: CollectionSortOrder,
        tree: CollectionTreeTraversalType,
        limit_scope: bool,
        count: int,
        traverse: bool,
    ) -> list[Accessible]: ...
    def is_ancestor_of(self, test: Accessible) -> bool: ...

class Component(GObject.GInterface):
    """
    Interface AtspiComponent
    """

    def contains(self, x: int, y: int, ctype: CoordType) -> bool: ...
    def get_accessible_at_point(
        self, x: int, y: int, ctype: CoordType
    ) -> typing.Optional[Accessible]: ...
    def get_alpha(self) -> float: ...
    def get_extents(self, ctype: CoordType) -> Rect: ...
    def get_layer(self) -> ComponentLayer: ...
    def get_mdi_z_order(self) -> int: ...
    def get_position(self, ctype: CoordType) -> Point: ...
    def get_size(self) -> Point: ...
    def grab_focus(self) -> bool: ...
    def scroll_to(self, type: ScrollType) -> bool: ...
    def scroll_to_point(self, coords: CoordType, x: int, y: int) -> bool: ...
    def set_extents(
        self, x: int, y: int, width: int, height: int, ctype: CoordType
    ) -> bool: ...
    def set_position(self, x: int, y: int, ctype: CoordType) -> bool: ...
    def set_size(self, width: int, height: int) -> bool: ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)
        new() -> Atspi.Device

    Object AtspiDevice

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    def add_key_grab(
        self,
        kd: KeyDefinition,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> int: ...
    def add_key_watcher(
        self,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_add_key_grab(self, kd: KeyDefinition) -> bool: ...
    def do_generate_mouse_event(
        self, obj: Accessible, x: int, y: int, name: str
    ) -> None: ...
    def do_get_locked_modifiers(self) -> int: ...
    def do_get_modifier(self, keycode: int) -> int: ...
    def do_grab_keyboard(self) -> bool: ...
    def do_map_modifier(self, keycode: int) -> int: ...
    def do_remove_key_grab(self, id: int) -> None: ...
    def do_ungrab_keyboard(self) -> None: ...
    def do_unmap_modifier(self, keycode: int) -> None: ...
    def generate_mouse_event(
        self, obj: Accessible, x: int, y: int, name: str
    ) -> None: ...
    def get_grab_by_id(self, id: int) -> KeyDefinition: ...
    def get_locked_modifiers(self) -> int: ...
    def get_modifier(self, keycode: int) -> int: ...
    def grab_keyboard(self) -> bool: ...
    def map_modifier(self, keycode: int) -> int: ...
    @classmethod
    def new(cls) -> Device: ...
    def notify_key(
        self, pressed: bool, keycode: int, keysym: int, state: int, text: str
    ) -> bool: ...
    def remove_key_grab(self, id: int) -> None: ...
    def ungrab_keyboard(self) -> None: ...
    def unmap_modifier(self, keycode: int) -> None: ...

class DeviceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceClass()
    """

    parent_class: GObject.ObjectClass = ...
    add_key_grab: typing.Callable[[Device, KeyDefinition], bool] = ...
    remove_key_grab: typing.Callable[[Device, int], None] = ...
    map_modifier: typing.Callable[[Device, int], int] = ...
    unmap_modifier: typing.Callable[[Device, int], None] = ...
    get_modifier: typing.Callable[[Device, int], int] = ...
    grab_keyboard: typing.Callable[[Device], bool] = ...
    ungrab_keyboard: typing.Callable[[Device], None] = ...
    get_locked_modifiers: typing.Callable[[Device], int] = ...
    generate_mouse_event: typing.Callable[
        [Device, Accessible, int, int, str], None
    ] = ...

class DeviceEvent(GObject.GBoxed):
    """
    :Constructors:

    ::

        DeviceEvent()
    """

    type: EventType = ...
    id: int = ...
    hw_code: int = ...
    modifiers: int = ...
    timestamp: int = ...
    event_string: str = ...
    is_text: bool = ...

class DeviceLegacy(Device):
    """
    :Constructors:

    ::

        DeviceLegacy(**properties)
        new() -> Atspi.DeviceLegacy

    Object AtspiDeviceLegacy

    Signals from GObject:
      notify (GParam)
    """

    parent: Device = ...
    @classmethod
    def new(cls) -> DeviceLegacy: ...

class DeviceLegacyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceLegacyClass()
    """

    parent_class: DeviceClass = ...

class DeviceListener(GObject.Object):
    """
    :Constructors:

    ::

        DeviceListener(**properties)
        new(callback:Atspi.DeviceListenerCB, user_data=None) -> Atspi.DeviceListener

    Object AtspiDeviceListener

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    id: int = ...
    callbacks: list[None] = ...
    def add_callback(
        self, callback: typing.Callable[..., bool], *user_data: typing.Any
    ) -> None: ...
    def do_device_event(self, event: DeviceEvent) -> bool: ...
    @classmethod
    def new(
        cls, callback: typing.Callable[..., bool], *user_data: typing.Any
    ) -> DeviceListener: ...
    def remove_callback(self, callback: typing.Callable[..., bool]) -> None: ...

class DeviceListenerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceListenerClass()
    """

    parent_class: GObject.ObjectClass = ...
    device_event: typing.Callable[[DeviceListener, DeviceEvent], bool] = ...

class DeviceX11(Device):
    """
    :Constructors:

    ::

        DeviceX11(**properties)
        new() -> Atspi.DeviceX11

    Object AtspiDeviceX11

    Signals from GObject:
      notify (GParam)
    """

    parent: Device = ...
    @classmethod
    def new(cls) -> DeviceX11: ...

class DeviceX11Class(GObject.GPointer):
    """
    :Constructors:

    ::

        DeviceX11Class()
    """

    parent_class: DeviceClass = ...

class Document(GObject.GInterface):
    """
    Interface AtspiDocument
    """

    def get_current_page_number(self) -> int: ...
    def get_document_attribute_value(self, attribute: str) -> str: ...
    def get_document_attributes(self) -> dict[str, str]: ...
    def get_locale(self) -> str: ...
    def get_page_count(self) -> int: ...
    def get_text_selections(self) -> list[TextSelection]: ...
    def set_text_selections(
        self, selections: typing.Sequence[TextSelection]
    ) -> bool: ...

class EditableText(GObject.GInterface):
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

    type: str = ...
    source: Accessible = ...
    detail1: int = ...
    detail2: int = ...
    any_data: typing.Any = ...
    sender: Accessible = ...
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

    parent: GObject.Object = ...
    callback: typing.Callable[..., None] = ...
    user_data: None = ...
    cb_destroyed: typing.Callable[[None], None] = ...
    def deregister(self, event_type: str) -> bool: ...
    @staticmethod
    def deregister_from_callback(
        callback: typing.Callable[..., None], event_type: str, *user_data: typing.Any
    ) -> bool: ...
    @classmethod
    def new(
        cls, callback: typing.Callable[..., None], *user_data: typing.Any
    ) -> EventListener: ...
    def register(self, event_type: str) -> bool: ...
    @staticmethod
    def register_from_callback(
        callback: typing.Callable[..., None], event_type: str, *user_data: typing.Any
    ) -> bool: ...
    @staticmethod
    def register_from_callback_full(
        callback: typing.Optional[typing.Callable[..., None]],
        event_type: str,
        properties: typing.Sequence[str],
        *user_data: typing.Any,
    ) -> bool: ...
    @staticmethod
    def register_from_callback_with_app(
        callback: typing.Optional[typing.Callable[..., None]],
        event_type: str,
        properties: typing.Sequence[str],
        app: typing.Optional[Accessible] = None,
        *user_data: typing.Any,
    ) -> bool: ...
    def register_full(
        self, event_type: str, properties: typing.Optional[typing.Sequence[str]] = None
    ) -> bool: ...
    def register_with_app(
        self,
        event_type: str,
        properties: typing.Optional[typing.Sequence[str]] = None,
        app: typing.Optional[Accessible] = None,
    ) -> bool: ...

class EventListenerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EventListenerClass()
    """

    parent_class: GObject.ObjectClass = ...

class EventListenerMode(GObject.GPointer):
    """
    :Constructors:

    ::

        EventListenerMode()
    """

    synchronous: bool = ...
    preemptive: bool = ...
    global_: bool = ...

class Hyperlink(Object):
    """
    :Constructors:

    ::

        Hyperlink(**properties)

    Object AtspiHyperlink

    Signals from GObject:
      notify (GParam)
    """

    parent: Object = ...
    def get_end_index(self) -> int: ...
    def get_index_range(self) -> Range: ...
    def get_n_anchors(self) -> int: ...
    def get_object(self, i: int) -> Accessible: ...
    def get_start_index(self) -> int: ...
    def get_uri(self, i: int) -> str: ...
    def is_valid(self) -> bool: ...

class HyperlinkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HyperlinkClass()
    """

    parent_class: ObjectClass = ...

class Hypertext(GObject.GInterface):
    """
    Interface AtspiHypertext
    """

    def get_link(self, link_index: int) -> typing.Optional[Hyperlink]: ...
    def get_link_index(self, character_offset: int) -> int: ...
    def get_n_links(self) -> int: ...

class Image(GObject.GInterface):
    """
    Interface AtspiImage
    """

    def get_image_description(self) -> str: ...
    def get_image_extents(self, ctype: CoordType) -> Rect: ...
    def get_image_locale(self) -> str: ...
    def get_image_position(self, ctype: CoordType) -> Point: ...
    def get_image_size(self) -> Point: ...

class KeyDefinition(GObject.GBoxed):
    """
    :Constructors:

    ::

        KeyDefinition()
    """

    keycode: int = ...
    keysym: int = ...
    keystring: str = ...
    modifiers: int = ...

class KeySet(GObject.GPointer):
    """
    :Constructors:

    ::

        KeySet()
    """

    keysyms: int = ...
    keycodes: int = ...
    keystrings: str = ...
    len: int = ...

class MatchRule(GObject.Object):
    """
    :Constructors:

    ::

        MatchRule(**properties)
        new(states:Atspi.StateSet, statematchtype:Atspi.CollectionMatchType, attributes:dict, attributematchtype:Atspi.CollectionMatchType, roles:list, rolematchtype:Atspi.CollectionMatchType, interfaces:list, interfacematchtype:Atspi.CollectionMatchType, invert:bool) -> Atspi.MatchRule

    Object AtspiMatchRule

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    states: StateSet = ...
    statematchtype: CollectionMatchType = ...
    attributes: dict[None, None] = ...
    attributematchtype: CollectionMatchType = ...
    interfaces: list[None] = ...
    interfacematchtype: CollectionMatchType = ...
    roles: list[int] = ...
    rolematchtype: CollectionMatchType = ...
    invert: bool = ...
    @classmethod
    def new(
        cls,
        states: StateSet,
        statematchtype: CollectionMatchType,
        attributes: dict[str, str],
        attributematchtype: CollectionMatchType,
        roles: typing.Sequence[Role],
        rolematchtype: CollectionMatchType,
        interfaces: typing.Sequence[str],
        interfacematchtype: CollectionMatchType,
        invert: bool,
    ) -> MatchRule: ...

class MatchRuleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MatchRuleClass()
    """

    parent_class: GObject.ObjectClass = ...

class Object(GObject.Object):
    """
    :Constructors:

    ::

        Object(**properties)

    Object AtspiObject

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    app: Application = ...
    path: str = ...

class ObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """

    parent_class: GObject.ObjectClass = ...

class Point(GObject.GBoxed):
    """
    :Constructors:

    ::

        Point()
    """

    x: int = ...
    y: int = ...
    def copy(self) -> Point: ...

class Range(GObject.GBoxed):
    """
    :Constructors:

    ::

        Range()
    """

    start_offset: int = ...
    end_offset: int = ...
    def copy(self) -> Range: ...

class Rect(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rect()
    """

    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...
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

    parent: GObject.Object = ...
    relation_type: RelationType = ...
    targets: list[None] = ...
    def get_n_targets(self) -> int: ...
    def get_relation_type(self) -> RelationType: ...
    def get_target(self, i: int) -> Accessible: ...

class RelationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RelationClass()
    """

    parent_class: GObject.ObjectClass = ...

class Selection(GObject.GInterface):
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

    parent: GObject.Object = ...
    accessible: None = ...
    states: int = ...
    def add(self, state: StateType) -> None: ...
    def compare(self, set2: StateSet) -> StateSet: ...
    def contains(self, state: StateType) -> bool: ...
    def equals(self, set2: StateSet) -> bool: ...
    def get_states(self) -> list[StateType]: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls, states: typing.Sequence[StateType]) -> StateSet: ...
    def remove(self, state: StateType) -> None: ...
    def set_by_name(self, name: str, enabled: bool) -> None: ...

class StateSetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StateSetClass()
    """

    parent_class: GObject.ObjectClass = ...

class Table(GObject.GInterface):
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
    ) -> typing.Tuple[bool, int, int, int, int, bool]: ...
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

class TableCell(GObject.GInterface):
    """
    Interface AtspiTableCell
    """

    def get_column_header_cells(self) -> list[Accessible]: ...
    def get_column_index(self) -> int: ...
    def get_column_span(self) -> int: ...
    def get_position(self) -> typing.Tuple[int, int, int]: ...
    def get_row_column_span(self) -> typing.Tuple[int, int, int, int]: ...
    def get_row_header_cells(self) -> list[Accessible]: ...
    def get_row_span(self) -> int: ...
    def get_table(self) -> Accessible: ...

class Text(GObject.GInterface):
    """
    Interface AtspiText
    """

    def add_selection(self, start_offset: int, end_offset: int) -> bool: ...
    def get_attribute_run(
        self, offset: int, include_defaults: bool
    ) -> typing.Tuple[dict[str, str], int, int]: ...
    def get_bounded_ranges(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        type: CoordType,
        clipTypeX: TextClipType,
        clipTypeY: TextClipType,
    ) -> list[TextRange]: ...
    def get_caret_offset(self) -> int: ...
    def get_character_at_offset(self, offset: int) -> int: ...
    def get_character_count(self) -> int: ...
    def get_character_extents(self, offset: int, type: CoordType) -> Rect: ...
    def get_default_attributes(self) -> dict[str, str]: ...
    def get_n_selections(self) -> int: ...
    def get_offset_at_point(self, x: int, y: int, type: CoordType) -> int: ...
    def get_range_extents(
        self, start_offset: int, end_offset: int, type: CoordType
    ) -> Rect: ...
    def get_selection(self, selection_num: int) -> Range: ...
    def get_string_at_offset(
        self, offset: int, granularity: TextGranularity
    ) -> TextRange: ...
    def get_text(self, start_offset: int, end_offset: int) -> str: ...
    def get_text_after_offset(
        self, offset: int, type: TextBoundaryType
    ) -> TextRange: ...
    def get_text_at_offset(self, offset: int, type: TextBoundaryType) -> TextRange: ...
    def get_text_attribute_value(
        self, offset: int, attribute_name: str
    ) -> typing.Optional[str]: ...
    def get_text_attributes(
        self, offset: int
    ) -> typing.Tuple[dict[str, str], int, int]: ...
    def get_text_before_offset(
        self, offset: int, type: TextBoundaryType
    ) -> TextRange: ...
    def remove_selection(self, selection_num: int) -> bool: ...
    def scroll_substring_to(
        self, start_offset: int, end_offset: int, type: ScrollType
    ) -> bool: ...
    def scroll_substring_to_point(
        self, start_offset: int, end_offset: int, coords: CoordType, x: int, y: int
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

    start_offset: int = ...
    end_offset: int = ...
    content: str = ...

class TextSelection(GObject.GPointer):
    """
    :Constructors:

    ::

        TextSelection()
    """

    start_object: Accessible = ...
    start_offset: int = ...
    end_object: Accessible = ...
    end_offset: int = ...
    start_is_active: bool = ...

class Value(GObject.GInterface):
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

class KeyListenerSyncType(GObject.GFlags):
    ALL_WINDOWS = 4
    CANCONSUME = 2
    NOSYNC = 0
    SYNCHRONOUS = 1

class CollectionMatchType(GObject.GEnum):
    ALL = 1
    ANY = 2
    EMPTY = 4
    INVALID = 0
    LAST_DEFINED = 5
    NONE = 3

class CollectionSortOrder(GObject.GEnum):
    CANONICAL = 1
    FLOW = 2
    INVALID = 0
    LAST_DEFINED = 7
    REVERSE_CANONICAL = 4
    REVERSE_FLOW = 5
    REVERSE_TAB = 6
    TAB = 3

class CollectionTreeTraversalType(GObject.GEnum):
    INORDER = 2
    LAST_DEFINED = 3
    RESTRICT_CHILDREN = 0
    RESTRICT_SIBLING = 1

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

class CoordType(GObject.GEnum):
    PARENT = 2
    SCREEN = 0
    WINDOW = 1

class EventType(GObject.GEnum):
    BUTTON_PRESSED_EVENT = 2
    BUTTON_RELEASED_EVENT = 3
    KEY_PRESSED_EVENT = 0
    KEY_RELEASED_EVENT = 1

class KeyEventType(GObject.GEnum):
    PRESSED = 0
    RELEASED = 1

class KeySynthType(GObject.GEnum):
    LOCKMODIFIERS = 5
    PRESS = 0
    PRESSRELEASE = 2
    RELEASE = 1
    STRING = 4
    SYM = 3
    UNLOCKMODIFIERS = 6

class Live(GObject.GEnum):
    ASSERTIVE = 2
    NONE = 0
    POLITE = 1

class LocaleType(GObject.GEnum):
    COLLATE = 1
    CTYPE = 2
    MESSAGES = 0
    MONETARY = 3
    NUMERIC = 4
    TIME = 5

class ModifierType(GObject.GEnum):
    ALT = 3
    CONTROL = 2
    META = 4
    META2 = 5
    META3 = 6
    NUMLOCK = 14
    SHIFT = 0
    SHIFTLOCK = 1

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
    LAST_DEFINED = 130
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
    def get_localized_name(role: Role) -> str: ...
    @staticmethod
    def get_name(role: Role) -> str: ...

class ScrollType(GObject.GEnum):
    ANYWHERE = 6
    BOTTOM_EDGE = 3
    BOTTOM_RIGHT = 1
    LEFT_EDGE = 4
    RIGHT_EDGE = 5
    TOP_EDGE = 2
    TOP_LEFT = 0

class StateType(GObject.GEnum):
    ACTIVE = 1
    ANIMATED = 35
    ARMED = 2
    BUSY = 3
    CHECKABLE = 41
    CHECKED = 4
    COLLAPSED = 5
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

class TextBoundaryType(GObject.GEnum):
    CHAR = 0
    LINE_END = 6
    LINE_START = 5
    SENTENCE_END = 4
    SENTENCE_START = 3
    WORD_END = 2
    WORD_START = 1

class TextClipType(GObject.GEnum):
    BOTH = 3
    MAX = 2
    MIN = 1
    NONE = 0

class TextGranularity(GObject.GEnum):
    CHAR = 0
    LINE = 3
    PARAGRAPH = 4
    SENTENCE = 2
    WORD = 1
