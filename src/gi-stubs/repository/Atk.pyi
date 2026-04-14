from typing import Any
from typing import Final
from typing import Protocol
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable
from collections.abc import Sequence

from gi import _gi
from gi.repository import GLib
from gi.repository import GObject

T = TypeVar("T")

BINARY_AGE: Final[int]
INTERFACE_AGE: Final[int]
MAJOR_VERSION: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]
VERSION_MIN_REQUIRED: Final[int]

def attribute_set_free(attrib_set: list[None]) -> None: ...
def focus_tracker_notify(object: Object) -> None: ...
def get_binary_age() -> int: ...
def get_default_registry() -> Registry: ...
def get_focus_object() -> Object: ...
def get_interface_age() -> int: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def get_root() -> Object: ...
def get_toolkit_name() -> str: ...
def get_toolkit_version() -> str: ...
def get_version() -> str: ...
def relation_type_for_name(name: str) -> RelationType: ...
def relation_type_get_name(type: RelationType) -> str: ...
def relation_type_register(name: str) -> RelationType: ...
def remove_focus_tracker(tracker_id: int) -> None: ...
def remove_global_event_listener(listener_id: int) -> None: ...
def remove_key_event_listener(listener_id: int) -> None: ...
def role_for_name(name: str) -> Role: ...
def role_get_localized_name(role: Role) -> str: ...
def role_get_name(role: Role) -> str: ...
def role_register(name: str) -> Role: ...
def state_type_for_name(name: str) -> StateType: ...
def state_type_get_name(type: StateType) -> str: ...
def state_type_register(name: str) -> StateType: ...
def text_attribute_for_name(name: str) -> TextAttribute: ...
def text_attribute_get_name(attr: TextAttribute) -> str: ...
def text_attribute_get_value(attr: TextAttribute, index_: int) -> str | None: ...
def text_attribute_register(name: str) -> TextAttribute: ...
def text_free_ranges(ranges: Sequence[TextRange]) -> None: ...
def value_type_get_localized_name(value_type: ValueType) -> str: ...
def value_type_get_name(value_type: ValueType) -> str: ...

class Action(GObject.GInterface, Protocol):
    """
    Interface AtkAction
    """
    def do_action(self, i: int) -> bool: ...
    def get_description(self, i: int) -> str | None: ...
    def get_keybinding(self, i: int) -> str | None: ...
    def get_localized_name(self, i: int) -> str | None: ...
    def get_n_actions(self) -> int: ...
    def get_name(self, i: int) -> str | None: ...
    def set_description(self, i: int, desc: str) -> bool: ...

class ActionIface(_gi.Struct):
    """
    :Constructors:

    ::

        ActionIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def do_action(self) -> Callable[[Action, int], bool]: ...
    @property
    def get_n_actions(self) -> Callable[[Action], int]: ...
    @property
    def get_description(self) -> Callable[[Action, int], str | None]: ...
    @property
    def get_name(self) -> Callable[[Action, int], str | None]: ...
    @property
    def get_keybinding(self) -> Callable[[Action, int], str | None]: ...
    @property
    def set_description(self) -> Callable[[Action, int, str], bool]: ...
    @property
    def get_localized_name(self) -> Callable[[Action, int], str | None]: ...

class Attribute(_gi.Struct):
    """
    :Constructors:

    ::

        Attribute()
    """

    name: str
    value: str
    @staticmethod
    def set_free(attrib_set: list[None]) -> None: ...

class Component(GObject.GInterface, Protocol):
    """
    Interface AtkComponent
    """
    def contains(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def get_alpha(self) -> float: ...
    def get_extents(self, coord_type: CoordType) -> tuple[int, int, int, int]: ...
    def get_layer(self) -> Layer: ...
    def get_mdi_zorder(self) -> int: ...
    def get_position(self, coord_type: CoordType) -> tuple[int, int]: ...
    def get_size(self) -> tuple[int, int]: ...
    def grab_focus(self) -> bool: ...
    def ref_accessible_at_point(
        self, x: int, y: int, coord_type: CoordType
    ) -> Object | None: ...
    def remove_focus_handler(self, handler_id: int) -> None: ...
    def scroll_to(self, type: ScrollType) -> bool: ...
    def scroll_to_point(self, coords: CoordType, x: int, y: int) -> bool: ...
    def set_extents(
        self, x: int, y: int, width: int, height: int, coord_type: CoordType
    ) -> bool: ...
    def set_position(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def set_size(self, width: int, height: int) -> bool: ...

class ComponentIface(_gi.Struct):
    """
    :Constructors:

    ::

        ComponentIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def add_focus_handler(self) -> None: ...
    @property
    def contains(self) -> Callable[[Component, int, int, CoordType], bool]: ...
    @property
    def ref_accessible_at_point(
        self,
    ) -> Callable[[Component, int, int, CoordType], Object | None]: ...
    @property
    def get_extents(
        self,
    ) -> Callable[[Component, CoordType], tuple[int, int, int, int]]: ...
    @property
    def get_position(self) -> Callable[[Component, CoordType], tuple[int, int]]: ...
    @property
    def get_size(self) -> Callable[[Component], tuple[int, int]]: ...
    @property
    def grab_focus(self) -> Callable[[Component], bool]: ...
    @property
    def remove_focus_handler(self) -> Callable[[Component, int], None]: ...
    @property
    def set_extents(
        self,
    ) -> Callable[[Component, int, int, int, int, CoordType], bool]: ...
    @property
    def set_position(self) -> Callable[[Component, int, int, CoordType], bool]: ...
    @property
    def set_size(self) -> Callable[[Component, int, int], bool]: ...
    @property
    def get_layer(self) -> Callable[[Component], Layer]: ...
    @property
    def get_mdi_zorder(self) -> Callable[[Component], int]: ...
    @property
    def bounds_changed(self) -> Callable[[Component, Rectangle], None]: ...
    @property
    def get_alpha(self) -> Callable[[Component], float]: ...
    @property
    def scroll_to(self) -> Callable[[Component, ScrollType], bool]: ...
    @property
    def scroll_to_point(self) -> Callable[[Component, CoordType, int, int], bool]: ...

class Document(GObject.GInterface, Protocol):
    """
    Interface AtkDocument
    """
    def get_attribute_value(self, attribute_name: str) -> str | None: ...
    def get_attributes(self) -> list[None]: ...
    def get_current_page_number(self) -> int: ...
    def get_document(self) -> None: ...
    def get_document_type(self) -> str: ...
    def get_locale(self) -> str: ...
    def get_page_count(self) -> int: ...
    def get_text_selections(self) -> list[TextSelection]: ...
    def set_attribute_value(
        self, attribute_name: str, attribute_value: str
    ) -> bool: ...
    def set_text_selections(self, selections: Sequence[TextSelection]) -> bool: ...

class DocumentIface(_gi.Struct):
    """
    :Constructors:

    ::

        DocumentIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_document_type(self) -> Callable[[Document], str]: ...
    @property
    def get_document(self) -> Callable[[Document], None]: ...
    @property
    def get_document_locale(self) -> Callable[[Document], str]: ...
    @property
    def get_document_attributes(self) -> Callable[[Document], list[None]]: ...
    @property
    def get_document_attribute_value(self) -> Callable[[Document, str], str | None]: ...
    @property
    def set_document_attribute(self) -> Callable[[Document, str, str], bool]: ...
    @property
    def get_current_page_number(self) -> Callable[[Document], int]: ...
    @property
    def get_page_count(self) -> Callable[[Document], int]: ...
    @property
    def get_text_selections(self) -> Callable[[Document], list[TextSelection]]: ...
    @property
    def set_text_selections(
        self,
    ) -> Callable[[Document, Sequence[TextSelection]], bool]: ...

class EditableText(GObject.GInterface, Protocol):
    """
    Interface AtkEditableText
    """
    def copy_text(self, start_pos: int, end_pos: int) -> None: ...
    def cut_text(self, start_pos: int, end_pos: int) -> None: ...
    def delete_text(self, start_pos: int, end_pos: int) -> None: ...
    def insert_text(self, string: str, length: int, position: int) -> None: ...
    def paste_text(self, position: int) -> None: ...
    def set_run_attributes(
        self, attrib_set: list[None], start_offset: int, end_offset: int
    ) -> bool: ...
    def set_text_contents(self, string: str) -> None: ...

class EditableTextIface(_gi.Struct):
    """
    :Constructors:

    ::

        EditableTextIface()
    """
    @property
    def parent_interface(self) -> GObject.TypeInterface: ...
    @property
    def set_run_attributes(
        self,
    ) -> Callable[[EditableText, list[None], int, int], bool]: ...
    @property
    def set_text_contents(self) -> Callable[[EditableText, str], None]: ...
    @property
    def insert_text(self) -> Callable[[EditableText, str, int, int], None]: ...
    @property
    def copy_text(self) -> Callable[[EditableText, int, int], None]: ...
    @property
    def cut_text(self) -> Callable[[EditableText, int, int], None]: ...
    @property
    def delete_text(self) -> Callable[[EditableText, int, int], None]: ...
    @property
    def paste_text(self) -> Callable[[EditableText, int], None]: ...

class GObjectAccessible(Object):
    """
    :Constructors:

    ::

        GObjectAccessible(**properties)

    Object AtkGObjectAccessible

    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
      announcement (gchararray)
      notification (gchararray, gint)
      attribute-changed (gchararray, gchararray)

    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance’s name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Parent of the current accessible as returned by atk_object_get_parent()
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> AtkRole: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
      accessible-id -> gchararray: Accessible ID
        ID for the accessible; useful for automated testing
      accessible-help-text -> gchararray: Help text
        Help text associated with the accessible

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_help_text: str
        accessible_hypertext_nlinks: int
        accessible_id: str
        accessible_name: str
        accessible_parent: Object
        accessible_role: Role
        accessible_table_caption: str
        accessible_table_caption_object: Object
        accessible_table_column_description: str
        accessible_table_column_header: Object
        accessible_table_row_description: str
        accessible_table_row_header: Object
        accessible_table_summary: Object
        accessible_value: float

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> Object: ...
    def __init__(
        self,
        *,
        accessible_description: str = ...,
        accessible_help_text: str = ...,
        accessible_id: str = ...,
        accessible_name: str = ...,
        accessible_parent: Object = ...,
        accessible_role: Role = ...,
        accessible_table_caption: str = ...,
        accessible_table_caption_object: Object = ...,
        accessible_table_column_description: str = ...,
        accessible_table_column_header: Object = ...,
        accessible_table_row_description: str = ...,
        accessible_table_row_header: Object = ...,
        accessible_table_summary: Object = ...,
        accessible_value: float = ...,
    ) -> None: ...
    @staticmethod
    def for_object(obj: GObject.Object) -> Object: ...
    def get_object(self) -> GObject.Object: ...

class GObjectAccessibleClass(_gi.Struct):
    """
    :Constructors:

    ::

        GObjectAccessibleClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...
    @property
    def pad1(self) -> Callable[..., bool]: ...
    @property
    def pad2(self) -> Callable[..., bool]: ...

class Hyperlink(GObject.Object, Action):
    """
    :Constructors:

    ::

        Hyperlink(**properties)

    Object AtkHyperlink

    Signals from AtkHyperlink:
      link-activated ()

    Properties from AtkHyperlink:
      selected-link -> gboolean: Selected Link
        Specifies whether the AtkHyperlink object is selected
      number-of-anchors -> gint: Number of Anchors
        The number of anchors associated with the AtkHyperlink object
      end-index -> gint: End index
        The end index of the AtkHyperlink object
      start-index -> gint: Start index
        The start index of the AtkHyperlink object

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        end_index: int
        number_of_anchors: int
        selected_link: bool
        start_index: int

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    def do_get_end_index(self) -> int: ...
    def do_get_n_anchors(self) -> int: ...
    def do_get_object(self, i: int) -> Object: ...
    def do_get_start_index(self) -> int: ...
    def do_get_uri(self, i: int) -> str: ...
    def do_is_selected_link(self) -> bool: ...
    def do_is_valid(self) -> bool: ...
    def do_link_activated(self) -> None: ...
    def do_link_state(self) -> int: ...
    def get_end_index(self) -> int: ...
    def get_n_anchors(self) -> int: ...
    def get_object(self, i: int) -> Object: ...
    def get_start_index(self) -> int: ...
    def get_uri(self, i: int) -> str: ...
    def is_inline(self) -> bool: ...
    def is_selected_link(self) -> bool: ...
    def is_valid(self) -> bool: ...

class HyperlinkClass(_gi.Struct):
    """
    :Constructors:

    ::

        HyperlinkClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...
    @property
    def get_uri(self) -> Callable[[Hyperlink, int], str]: ...
    @property
    def get_object(self) -> Callable[[Hyperlink, int], Object]: ...
    @property
    def get_end_index(self) -> Callable[[Hyperlink], int]: ...
    @property
    def get_start_index(self) -> Callable[[Hyperlink], int]: ...
    @property
    def is_valid(self) -> Callable[[Hyperlink], bool]: ...
    @property
    def get_n_anchors(self) -> Callable[[Hyperlink], int]: ...
    @property
    def link_state(self) -> Callable[[Hyperlink], int]: ...
    @property
    def is_selected_link(self) -> Callable[[Hyperlink], bool]: ...
    @property
    def link_activated(self) -> Callable[[Hyperlink], None]: ...
    @property
    def pad1(self) -> Callable[..., bool]: ...

class HyperlinkImpl(GObject.GInterface, Protocol):
    """
    Interface AtkHyperlinkImpl
    """
    def get_hyperlink(self) -> Hyperlink: ...

class HyperlinkImplIface(_gi.Struct):
    """
    :Constructors:

    ::

        HyperlinkImplIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_hyperlink(self) -> Callable[[HyperlinkImpl], Hyperlink]: ...

class Hypertext(GObject.GInterface, Protocol):
    """
    Interface AtkHypertext
    """
    def get_link(self, link_index: int) -> Hyperlink: ...
    def get_link_index(self, char_index: int) -> int: ...
    def get_n_links(self) -> int: ...

class HypertextIface(_gi.Struct):
    """
    :Constructors:

    ::

        HypertextIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_link(self) -> Callable[[Hypertext, int], Hyperlink]: ...
    @property
    def get_n_links(self) -> Callable[[Hypertext], int]: ...
    @property
    def get_link_index(self) -> Callable[[Hypertext, int], int]: ...
    @property
    def link_selected(self) -> Callable[[Hypertext, int], None]: ...

class Image(GObject.GInterface, Protocol):
    """
    Interface AtkImage
    """
    def get_image_description(self) -> str: ...
    def get_image_locale(self) -> str | None: ...
    def get_image_position(self, coord_type: CoordType) -> tuple[int, int]: ...
    def get_image_size(self) -> tuple[int, int]: ...
    def set_image_description(self, description: str) -> bool: ...

class ImageIface(_gi.Struct):
    """
    :Constructors:

    ::

        ImageIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_image_position(self) -> Callable[[Image, CoordType], tuple[int, int]]: ...
    @property
    def get_image_description(self) -> Callable[[Image], str]: ...
    @property
    def get_image_size(self) -> Callable[[Image], tuple[int, int]]: ...
    @property
    def set_image_description(self) -> Callable[[Image, str], bool]: ...
    @property
    def get_image_locale(self) -> Callable[[Image], str | None]: ...

class Implementor(_gi.Struct):
    def ref_accessible(self) -> Object: ...

class ImplementorIface(GObject.GInterface, Protocol): ...

class KeyEventStruct(_gi.Struct):
    """
    :Constructors:

    ::

        KeyEventStruct()
    """

    type: int
    state: int
    keyval: int
    length: int
    string: str
    keycode: int
    timestamp: int

class Misc(GObject.Object):
    """
    :Constructors:

    ::

        Misc(**properties)

    Object AtkMisc

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    def do_threads_enter(self) -> None: ...
    def do_threads_leave(self) -> None: ...
    @staticmethod
    def get_instance() -> Misc: ...
    def threads_enter(self) -> None: ...
    def threads_leave(self) -> None: ...

class MiscClass(_gi.Struct):
    """
    :Constructors:

    ::

        MiscClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...
    @property
    def threads_enter(self) -> Callable[[Misc], None]: ...
    @property
    def threads_leave(self) -> Callable[[Misc], None]: ...
    @property
    def vfuncs(self) -> list[None]: ...

class NoOpObject(
    Object,
    Action,
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
    Window,
):
    """
    :Constructors:

    ::

        NoOpObject(**properties)
        new(obj:GObject.Object) -> Atk.Object

    Object AtkNoOpObject

    Signals from AtkComponent:
      bounds-changed (AtkRectangle)

    Signals from AtkSelection:
      selection-changed ()

    Signals from AtkTable:
      row-inserted (gint, gint)
      column-inserted (gint, gint)
      row-deleted (gint, gint)
      column-deleted (gint, gint)
      row-reordered ()
      column-reordered ()
      model-changed ()

    Signals from AtkText:
      text-changed (gint, gint)
      text-insert (gint, gint, gchararray)
      text-remove (gint, gint, gchararray)
      text-caret-moved (gint)
      text-selection-changed ()
      text-attributes-changed ()

    Signals from AtkHypertext:
      link-selected (gint)

    Signals from AtkValue:
      value-changed (gdouble, gchararray)

    Signals from AtkDocument:
      load-complete ()
      reload ()
      load-stopped ()
      page-changed (gint)
      document-attribute-changed (gchararray, gchararray)

    Signals from AtkWindow:
      activate ()
      create ()
      deactivate ()
      destroy ()
      maximize ()
      minimize ()
      move ()
      resize ()
      restore ()

    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
      announcement (gchararray)
      notification (gchararray, gint)
      attribute-changed (gchararray, gchararray)

    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance’s name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Parent of the current accessible as returned by atk_object_get_parent()
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> AtkRole: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
      accessible-id -> gchararray: Accessible ID
        ID for the accessible; useful for automated testing
      accessible-help-text -> gchararray: Help text
        Help text associated with the accessible

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_help_text: str
        accessible_hypertext_nlinks: int
        accessible_id: str
        accessible_name: str
        accessible_parent: Object
        accessible_role: Role
        accessible_table_caption: str
        accessible_table_caption_object: Object
        accessible_table_column_description: str
        accessible_table_column_header: Object
        accessible_table_row_description: str
        accessible_table_row_header: Object
        accessible_table_summary: Object
        accessible_value: float

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> Object: ...
    def __init__(
        self,
        *,
        accessible_description: str = ...,
        accessible_help_text: str = ...,
        accessible_id: str = ...,
        accessible_name: str = ...,
        accessible_parent: Object = ...,
        accessible_role: Role = ...,
        accessible_table_caption: str = ...,
        accessible_table_caption_object: Object = ...,
        accessible_table_column_description: str = ...,
        accessible_table_column_header: Object = ...,
        accessible_table_row_description: str = ...,
        accessible_table_row_header: Object = ...,
        accessible_table_summary: Object = ...,
        accessible_value: float = ...,
    ) -> None: ...
    @classmethod
    def new(cls, obj: GObject.Object) -> NoOpObject: ...

class NoOpObjectClass(_gi.Struct):
    """
    :Constructors:

    ::

        NoOpObjectClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...

class NoOpObjectFactory(ObjectFactory):
    """
    :Constructors:

    ::

        NoOpObjectFactory(**properties)
        new() -> Atk.ObjectFactory

    Object AtkNoOpObjectFactory

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> ObjectFactory: ...
    @classmethod
    def new(cls) -> NoOpObjectFactory: ...

class NoOpObjectFactoryClass(_gi.Struct):
    """
    :Constructors:

    ::

        NoOpObjectFactoryClass()
    """
    @property
    def parent_class(self) -> ObjectFactoryClass: ...

class Object(GObject.Object):
    """
    :Constructors:

    ::

        Object(**properties)

    Object AtkObject

    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
      announcement (gchararray)
      notification (gchararray, gint)
      attribute-changed (gchararray, gchararray)

    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance’s name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Parent of the current accessible as returned by atk_object_get_parent()
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> AtkRole: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
      accessible-id -> gchararray: Accessible ID
        ID for the accessible; useful for automated testing
      accessible-help-text -> gchararray: Help text
        Help text associated with the accessible

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_help_text: str
        accessible_hypertext_nlinks: int
        accessible_id: str
        accessible_name: str
        accessible_parent: Object
        accessible_role: Role
        accessible_table_caption: str
        accessible_table_caption_object: Object
        accessible_table_column_description: str
        accessible_table_column_header: Object
        accessible_table_row_description: str
        accessible_table_row_header: Object
        accessible_table_summary: Object
        accessible_value: float

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def description(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def accessible_parent(self) -> Object: ...
    @property
    def role(self) -> Role: ...
    @property
    def relation_set(self) -> RelationSet: ...
    @property
    def layer(self) -> Layer: ...
    def __init__(
        self,
        *,
        accessible_description: str = ...,
        accessible_help_text: str = ...,
        accessible_id: str = ...,
        accessible_name: str = ...,
        accessible_parent: Object = ...,
        accessible_role: Role = ...,
        accessible_table_caption: str = ...,
        accessible_table_caption_object: Object = ...,
        accessible_table_column_description: str = ...,
        accessible_table_column_header: Object = ...,
        accessible_table_row_description: str = ...,
        accessible_table_row_header: Object = ...,
        accessible_table_summary: Object = ...,
        accessible_value: float = ...,
    ) -> None: ...
    def add_relationship(self, relationship: RelationType, target: Object) -> bool: ...
    def do_active_descendant_changed(self, child: None) -> None: ...
    def do_children_changed(self, change_index: int, changed_child: None) -> None: ...
    def do_focus_event(self, focus_in: bool) -> None: ...
    def do_get_attributes(self) -> list[None]: ...
    def do_get_description(self) -> str: ...
    def do_get_index_in_parent(self) -> int: ...
    def do_get_layer(self) -> Layer: ...
    def do_get_mdi_zorder(self) -> int: ...
    def do_get_n_children(self) -> int: ...
    def do_get_name(self) -> str: ...
    def do_get_object_locale(self) -> str: ...
    def do_get_parent(self) -> Object: ...
    def do_get_role(self) -> Role: ...
    def do_initialize(self, data: None) -> None: ...
    def do_property_change(self, values: PropertyValues) -> None: ...
    def do_ref_relation_set(self) -> RelationSet: ...
    def do_ref_state_set(self) -> StateSet: ...
    def do_remove_property_change_handler(self, handler_id: int) -> None: ...
    def do_set_description(self, description: str) -> None: ...
    def do_set_name(self, name: str) -> None: ...
    def do_set_parent(self, parent: Object) -> None: ...
    def do_set_role(self, role: Role) -> None: ...
    def do_state_change(self, name: str, state_set: bool) -> None: ...
    def do_visible_data_changed(self) -> None: ...
    def get_accessible_id(self) -> str: ...
    def get_attributes(self) -> list[None]: ...
    def get_description(self) -> str: ...
    def get_help_text(self) -> str: ...
    def get_index_in_parent(self) -> int: ...
    def get_layer(self) -> Layer: ...
    def get_mdi_zorder(self) -> int: ...
    def get_n_accessible_children(self) -> int: ...
    def get_name(self) -> str: ...
    def get_object_locale(self) -> str: ...
    def get_parent(self) -> Object: ...
    def get_role(self) -> Role: ...
    def initialize(self, data: None) -> None: ...
    def notify_state_change(self, state: int, value: bool) -> None: ...
    def peek_parent(self) -> Object: ...
    def ref_accessible_child(self, i: int) -> Object: ...
    def ref_relation_set(self) -> RelationSet: ...
    def ref_state_set(self) -> StateSet: ...
    def remove_property_change_handler(self, handler_id: int) -> None: ...
    def remove_relationship(
        self, relationship: RelationType, target: Object
    ) -> bool: ...
    def set_accessible_id(self, id: str) -> None: ...
    def set_description(self, description: str) -> None: ...
    def set_help_text(self, help_text: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_parent(self, parent: Object) -> None: ...
    def set_role(self, role: Role) -> None: ...

class ObjectClass(_gi.Struct):
    """
    :Constructors:

    ::

        ObjectClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...
    @property
    def get_name(self) -> Callable[[Object], str]: ...
    @property
    def get_description(self) -> Callable[[Object], str]: ...
    @property
    def get_parent(self) -> Callable[[Object], Object]: ...
    @property
    def get_n_children(self) -> Callable[[Object], int]: ...
    @property
    def ref_child(self) -> None: ...
    @property
    def get_index_in_parent(self) -> Callable[[Object], int]: ...
    @property
    def ref_relation_set(self) -> Callable[[Object], RelationSet]: ...
    @property
    def get_role(self) -> Callable[[Object], Role]: ...
    @property
    def get_layer(self) -> Callable[[Object], Layer]: ...
    @property
    def get_mdi_zorder(self) -> Callable[[Object], int]: ...
    @property
    def ref_state_set(self) -> Callable[[Object], StateSet]: ...
    @property
    def set_name(self) -> Callable[[Object, str], None]: ...
    @property
    def set_description(self) -> Callable[[Object, str], None]: ...
    @property
    def set_parent(self) -> Callable[[Object, Object], None]: ...
    @property
    def set_role(self) -> Callable[[Object, Role], None]: ...
    @property
    def connect_property_change_handler(self) -> None: ...
    @property
    def remove_property_change_handler(self) -> Callable[[Object, int], None]: ...
    @property
    def initialize(self) -> Callable[[Object, None], None]: ...
    @property
    def children_changed(self) -> Callable[[Object, int, None], None]: ...
    @property
    def focus_event(self) -> Callable[[Object, bool], None]: ...
    @property
    def property_change(self) -> Callable[[Object, PropertyValues], None]: ...
    @property
    def state_change(self) -> Callable[[Object, str, bool], None]: ...
    @property
    def visible_data_changed(self) -> Callable[[Object], None]: ...
    @property
    def active_descendant_changed(self) -> Callable[[Object, None], None]: ...
    @property
    def get_attributes(self) -> Callable[[Object], list[None]]: ...
    @property
    def get_object_locale(self) -> Callable[[Object], str]: ...
    @property
    def pad1(self) -> Callable[..., bool]: ...

class ObjectFactory(GObject.Object):
    """
    :Constructors:

    ::

        ObjectFactory(**properties)

    Object AtkObjectFactory

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    def create_accessible(self, obj: GObject.Object) -> Object: ...
    def do_invalidate(self) -> None: ...
    def get_accessible_type(self) -> type[Any]: ...
    def invalidate(self) -> None: ...

class ObjectFactoryClass(_gi.Struct):
    """
    :Constructors:

    ::

        ObjectFactoryClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def create_accessible(self) -> None: ...
    @property
    def invalidate(self) -> Callable[[ObjectFactory], None]: ...
    @property
    def get_accessible_type(self) -> Callable[[], type[Any]]: ...
    @property
    def pad1(self) -> Callable[..., bool]: ...
    @property
    def pad2(self) -> Callable[..., bool]: ...

class Plug(Object, Component):
    """
    :Constructors:

    ::

        Plug(**properties)
        new() -> Atk.Object

    Object AtkPlug

    Signals from AtkComponent:
      bounds-changed (AtkRectangle)

    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
      announcement (gchararray)
      notification (gchararray, gint)
      attribute-changed (gchararray, gchararray)

    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance’s name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Parent of the current accessible as returned by atk_object_get_parent()
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> AtkRole: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
      accessible-id -> gchararray: Accessible ID
        ID for the accessible; useful for automated testing
      accessible-help-text -> gchararray: Help text
        Help text associated with the accessible

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_help_text: str
        accessible_hypertext_nlinks: int
        accessible_id: str
        accessible_name: str
        accessible_parent: Object
        accessible_role: Role
        accessible_table_caption: str
        accessible_table_caption_object: Object
        accessible_table_column_description: str
        accessible_table_column_header: Object
        accessible_table_row_description: str
        accessible_table_row_header: Object
        accessible_table_summary: Object
        accessible_value: float

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> Object: ...
    def __init__(
        self,
        *,
        accessible_description: str = ...,
        accessible_help_text: str = ...,
        accessible_id: str = ...,
        accessible_name: str = ...,
        accessible_parent: Object = ...,
        accessible_role: Role = ...,
        accessible_table_caption: str = ...,
        accessible_table_caption_object: Object = ...,
        accessible_table_column_description: str = ...,
        accessible_table_column_header: Object = ...,
        accessible_table_row_description: str = ...,
        accessible_table_row_header: Object = ...,
        accessible_table_summary: Object = ...,
        accessible_value: float = ...,
    ) -> None: ...
    def do_get_object_id(self) -> str: ...
    def get_id(self) -> str: ...
    @classmethod
    def new(cls) -> Plug: ...
    def set_child(self, child: Object) -> None: ...

class PlugClass(_gi.Struct):
    """
    :Constructors:

    ::

        PlugClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...
    @property
    def get_object_id(self) -> Callable[[Plug], str]: ...

class PropertyValues(_gi.Struct):
    """
    :Constructors:

    ::

        PropertyValues()
    """

    property_name: str
    old_value: Any
    new_value: Any

class Range(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(lower_limit:float, upper_limit:float, description:str) -> Atk.Range
    """
    @staticmethod
    def __new__(
        cls: type[Self], lower_limit: float, upper_limit: float, description: str
    ) -> Self: ...
    def copy(self) -> Range: ...
    def free(self) -> None: ...
    def get_description(self) -> str: ...
    def get_lower_limit(self) -> float: ...
    def get_upper_limit(self) -> float: ...
    @classmethod
    def new(cls, lower_limit: float, upper_limit: float, description: str) -> Range: ...

class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: int
    y: int
    width: int
    height: int

class Registry(GObject.Object):
    """
    :Constructors:

    ::

        Registry(**properties)

    Object AtkRegistry

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def factory_type_registry(self) -> dict[None, None]: ...
    @property
    def factory_singleton_cache(self) -> dict[None, None]: ...
    def get_factory(self, type: type[Any]) -> ObjectFactory: ...
    def get_factory_type(self, type: type[Any]) -> type[Any]: ...
    def set_factory_type(self, type: type[Any], factory_type: type[Any]) -> None: ...

class RegistryClass(_gi.Struct):
    """
    :Constructors:

    ::

        RegistryClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Relation(GObject.Object):
    """
    :Constructors:

    ::

        Relation(**properties)
        new(targets:list, relationship:Atk.RelationType) -> Atk.Relation

    Object AtkRelation

    Properties from AtkRelation:
      relation-type -> AtkRelationType: Relation Type
        The type of the relation
      target -> GValueArray: Target
        An array of the targets for the relation

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        relation_type: RelationType
        target: GObject.ValueArray

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def target(self) -> list[None]: ...
    @property
    def relationship(self) -> RelationType: ...
    def __init__(
        self, *, relation_type: RelationType = ..., target: GObject.ValueArray = ...
    ) -> None: ...
    def add_target(self, target: Object) -> None: ...
    def get_relation_type(self) -> RelationType: ...
    def get_target(self) -> list[Object]: ...
    @classmethod
    def new(cls, targets: Sequence[Object], relationship: RelationType) -> Relation: ...
    def remove_target(self, target: Object) -> bool: ...

class RelationClass(_gi.Struct):
    """
    :Constructors:

    ::

        RelationClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...

class RelationSet(GObject.Object):
    """
    :Constructors:

    ::

        RelationSet(**properties)
        new() -> Atk.RelationSet

    Object AtkRelationSet

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def relations(self) -> list[None]: ...
    def add(self, relation: Relation) -> None: ...
    def add_relation_by_type(
        self, relationship: RelationType, target: Object
    ) -> None: ...
    def contains(self, relationship: RelationType) -> bool: ...
    def contains_target(self, relationship: RelationType, target: Object) -> bool: ...
    def get_n_relations(self) -> int: ...
    def get_relation(self, i: int) -> Relation: ...
    def get_relation_by_type(self, relationship: RelationType) -> Relation: ...
    @classmethod
    def new(cls) -> RelationSet: ...
    def remove(self, relation: Relation) -> None: ...

class RelationSetClass(_gi.Struct):
    """
    :Constructors:

    ::

        RelationSetClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...
    @property
    def pad1(self) -> Callable[..., bool]: ...
    @property
    def pad2(self) -> Callable[..., bool]: ...

class Selection(GObject.GInterface, Protocol):
    """
    Interface AtkSelection
    """
    def add_selection(self, i: int) -> bool: ...
    def clear_selection(self) -> bool: ...
    def get_selection_count(self) -> int: ...
    def is_child_selected(self, i: int) -> bool: ...
    def ref_selection(self, i: int) -> Object | None: ...
    def remove_selection(self, i: int) -> bool: ...
    def select_all_selection(self) -> bool: ...

class SelectionIface(_gi.Struct):
    """
    :Constructors:

    ::

        SelectionIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def add_selection(self) -> Callable[[Selection, int], bool]: ...
    @property
    def clear_selection(self) -> Callable[[Selection], bool]: ...
    @property
    def ref_selection(self) -> Callable[[Selection, int], Object | None]: ...
    @property
    def get_selection_count(self) -> Callable[[Selection], int]: ...
    @property
    def is_child_selected(self) -> Callable[[Selection, int], bool]: ...
    @property
    def remove_selection(self) -> Callable[[Selection, int], bool]: ...
    @property
    def select_all_selection(self) -> Callable[[Selection], bool]: ...
    @property
    def selection_changed(self) -> Callable[[Selection], None]: ...

class Socket(Object, Component):
    """
    :Constructors:

    ::

        Socket(**properties)
        new() -> Atk.Object

    Object AtkSocket

    Signals from AtkComponent:
      bounds-changed (AtkRectangle)

    Signals from AtkObject:
      children-changed (guint, gpointer)
      focus-event (gboolean)
      property-change (gpointer)
      state-change (gchararray, gboolean)
      visible-data-changed ()
      active-descendant-changed (gpointer)
      announcement (gchararray)
      notification (gchararray, gint)
      attribute-changed (gchararray, gchararray)

    Properties from AtkObject:
      accessible-name -> gchararray: Accessible Name
        Object instance’s name formatted for assistive technology access
      accessible-description -> gchararray: Accessible Description
        Description of an object, formatted for assistive technology access
      accessible-parent -> AtkObject: Accessible Parent
        Parent of the current accessible as returned by atk_object_get_parent()
      accessible-value -> gdouble: Accessible Value
        Is used to notify that the value has changed
      accessible-role -> AtkRole: Accessible Role
        The accessible role of this object
      accessible-component-layer -> gint: Accessible Layer
        The accessible layer of this object
      accessible-component-mdi-zorder -> gint: Accessible MDI Value
        The accessible MDI value of this object
      accessible-table-caption -> gchararray: Accessible Table Caption
        Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead
      accessible-table-column-description -> gchararray: Accessible Table Column Description
        Is used to notify that the table column description has changed
      accessible-table-column-header -> AtkObject: Accessible Table Column Header
        Is used to notify that the table column header has changed
      accessible-table-row-description -> gchararray: Accessible Table Row Description
        Is used to notify that the table row description has changed
      accessible-table-row-header -> AtkObject: Accessible Table Row Header
        Is used to notify that the table row header has changed
      accessible-table-summary -> AtkObject: Accessible Table Summary
        Is used to notify that the table summary has changed
      accessible-table-caption-object -> AtkObject: Accessible Table Caption Object
        Is used to notify that the table caption has changed
      accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links
        The number of links which the current AtkHypertext has
      accessible-id -> gchararray: Accessible ID
        ID for the accessible; useful for automated testing
      accessible-help-text -> gchararray: Help text
        Help text associated with the accessible

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_help_text: str
        accessible_hypertext_nlinks: int
        accessible_id: str
        accessible_name: str
        accessible_parent: Object
        accessible_role: Role
        accessible_table_caption: str
        accessible_table_caption_object: Object
        accessible_table_column_description: str
        accessible_table_column_header: Object
        accessible_table_row_description: str
        accessible_table_row_header: Object
        accessible_table_summary: Object
        accessible_value: float

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> Object: ...
    @property
    def embedded_plug_id(self) -> str: ...
    def __init__(
        self,
        *,
        accessible_description: str = ...,
        accessible_help_text: str = ...,
        accessible_id: str = ...,
        accessible_name: str = ...,
        accessible_parent: Object = ...,
        accessible_role: Role = ...,
        accessible_table_caption: str = ...,
        accessible_table_caption_object: Object = ...,
        accessible_table_column_description: str = ...,
        accessible_table_column_header: Object = ...,
        accessible_table_row_description: str = ...,
        accessible_table_row_header: Object = ...,
        accessible_table_summary: Object = ...,
        accessible_value: float = ...,
    ) -> None: ...
    def do_embed(self, plug_id: str) -> None: ...
    def embed(self, plug_id: str) -> None: ...
    def is_occupied(self) -> bool: ...
    @classmethod
    def new(cls) -> Socket: ...

class SocketClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketClass()
    """
    @property
    def parent_class(self) -> ObjectClass: ...
    @property
    def embed(self) -> Callable[[Socket, str], None]: ...

class StateSet(GObject.Object):
    """
    :Constructors:

    ::

        StateSet(**properties)
        new() -> Atk.StateSet

    Object AtkStateSet

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    def add_state(self, type: StateType) -> bool: ...
    def add_states(self, types: Sequence[StateType]) -> None: ...
    def and_sets(self, compare_set: StateSet) -> StateSet: ...
    def clear_states(self) -> None: ...
    def contains_state(self, type: StateType) -> bool: ...
    def contains_states(self, types: Sequence[StateType]) -> bool: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls) -> StateSet: ...
    def or_sets(self, compare_set: StateSet) -> StateSet | None: ...
    def remove_state(self, type: StateType) -> bool: ...
    def xor_sets(self, compare_set: StateSet) -> StateSet: ...

class StateSetClass(_gi.Struct):
    """
    :Constructors:

    ::

        StateSetClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...

class StreamableContent(GObject.GInterface, Protocol):
    """
    Interface AtkStreamableContent
    """
    def get_mime_type(self, i: int) -> str: ...
    def get_n_mime_types(self) -> int: ...
    def get_stream(self, mime_type: str) -> GLib.IOChannel: ...
    def get_uri(self, mime_type: str) -> str | None: ...

class StreamableContentIface(_gi.Struct):
    """
    :Constructors:

    ::

        StreamableContentIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_n_mime_types(self) -> Callable[[StreamableContent], int]: ...
    @property
    def get_mime_type(self) -> Callable[[StreamableContent, int], str]: ...
    @property
    def get_stream(self) -> Callable[[StreamableContent, str], GLib.IOChannel]: ...
    @property
    def get_uri(self) -> Callable[[StreamableContent, str], str | None]: ...
    @property
    def pad1(self) -> Callable[..., bool]: ...
    @property
    def pad2(self) -> Callable[..., bool]: ...
    @property
    def pad3(self) -> Callable[..., bool]: ...

class Table(GObject.GInterface, Protocol):
    """
    Interface AtkTable
    """
    def add_column_selection(self, column: int) -> bool: ...
    def add_row_selection(self, row: int) -> bool: ...
    def get_caption(self) -> Object | None: ...
    def get_column_at_index(self, index_: int) -> int: ...
    def get_column_description(self, column: int) -> str: ...
    def get_column_extent_at(self, row: int, column: int) -> int: ...
    def get_column_header(self, column: int) -> Object | None: ...
    def get_index_at(self, row: int, column: int) -> int: ...
    def get_n_columns(self) -> int: ...
    def get_n_rows(self) -> int: ...
    def get_row_at_index(self, index_: int) -> int: ...
    def get_row_description(self, row: int) -> str | None: ...
    def get_row_extent_at(self, row: int, column: int) -> int: ...
    def get_row_header(self, row: int) -> Object | None: ...
    def get_selected_columns(self, selected: int) -> int: ...
    def get_selected_rows(self, selected: int) -> int: ...
    def get_summary(self) -> Object: ...
    def is_column_selected(self, column: int) -> bool: ...
    def is_row_selected(self, row: int) -> bool: ...
    def is_selected(self, row: int, column: int) -> bool: ...
    def ref_at(self, row: int, column: int) -> Object: ...
    def remove_column_selection(self, column: int) -> bool: ...
    def remove_row_selection(self, row: int) -> bool: ...
    def set_caption(self, caption: Object) -> None: ...
    def set_column_description(self, column: int, description: str) -> None: ...
    def set_column_header(self, column: int, header: Object) -> None: ...
    def set_row_description(self, row: int, description: str) -> None: ...
    def set_row_header(self, row: int, header: Object) -> None: ...
    def set_summary(self, accessible: Object) -> None: ...

class TableCell(GObject.GInterface, Protocol):
    """
    Interface AtkTableCell

    Signals from GObject:
      notify (GParam)
    """
    def get_column_header_cells(self) -> list[Object]: ...
    def get_column_span(self) -> int: ...
    def get_position(self) -> tuple[bool, int, int]: ...
    def get_row_column_span(self) -> tuple[bool, int, int, int, int]: ...
    def get_row_header_cells(self) -> list[Object]: ...
    def get_row_span(self) -> int: ...
    def get_table(self) -> Object: ...

class TableCellIface(_gi.Struct):
    """
    :Constructors:

    ::

        TableCellIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_column_span(self) -> Callable[[TableCell], int]: ...
    @property
    def get_column_header_cells(self) -> Callable[[TableCell], list[Object]]: ...
    @property
    def get_position(self) -> Callable[[TableCell], tuple[bool, int, int]]: ...
    @property
    def get_row_span(self) -> Callable[[TableCell], int]: ...
    @property
    def get_row_header_cells(self) -> Callable[[TableCell], list[Object]]: ...
    @property
    def get_row_column_span(
        self,
    ) -> Callable[[TableCell], tuple[bool, int, int, int, int]]: ...
    @property
    def get_table(self) -> Callable[[TableCell], Object]: ...

class TableIface(_gi.Struct):
    """
    :Constructors:

    ::

        TableIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def ref_at(self) -> Callable[[Table, int, int], Object]: ...
    @property
    def get_index_at(self) -> Callable[[Table, int, int], int]: ...
    @property
    def get_column_at_index(self) -> Callable[[Table, int], int]: ...
    @property
    def get_row_at_index(self) -> Callable[[Table, int], int]: ...
    @property
    def get_n_columns(self) -> Callable[[Table], int]: ...
    @property
    def get_n_rows(self) -> Callable[[Table], int]: ...
    @property
    def get_column_extent_at(self) -> Callable[[Table, int, int], int]: ...
    @property
    def get_row_extent_at(self) -> Callable[[Table, int, int], int]: ...
    @property
    def get_caption(self) -> Callable[[Table], Object | None]: ...
    @property
    def get_column_description(self) -> Callable[[Table, int], str]: ...
    @property
    def get_column_header(self) -> Callable[[Table, int], Object | None]: ...
    @property
    def get_row_description(self) -> Callable[[Table, int], str | None]: ...
    @property
    def get_row_header(self) -> Callable[[Table, int], Object | None]: ...
    @property
    def get_summary(self) -> Callable[[Table], Object]: ...
    @property
    def set_caption(self) -> Callable[[Table, Object], None]: ...
    @property
    def set_column_description(self) -> Callable[[Table, int, str], None]: ...
    @property
    def set_column_header(self) -> Callable[[Table, int, Object], None]: ...
    @property
    def set_row_description(self) -> Callable[[Table, int, str], None]: ...
    @property
    def set_row_header(self) -> Callable[[Table, int, Object], None]: ...
    @property
    def set_summary(self) -> Callable[[Table, Object], None]: ...
    @property
    def get_selected_columns(self) -> Callable[[Table, int], int]: ...
    @property
    def get_selected_rows(self) -> Callable[[Table, int], int]: ...
    @property
    def is_column_selected(self) -> Callable[[Table, int], bool]: ...
    @property
    def is_row_selected(self) -> Callable[[Table, int], bool]: ...
    @property
    def is_selected(self) -> Callable[[Table, int, int], bool]: ...
    @property
    def add_row_selection(self) -> Callable[[Table, int], bool]: ...
    @property
    def remove_row_selection(self) -> Callable[[Table, int], bool]: ...
    @property
    def add_column_selection(self) -> Callable[[Table, int], bool]: ...
    @property
    def remove_column_selection(self) -> Callable[[Table, int], bool]: ...
    @property
    def row_inserted(self) -> Callable[[Table, int, int], None]: ...
    @property
    def column_inserted(self) -> Callable[[Table, int, int], None]: ...
    @property
    def row_deleted(self) -> Callable[[Table, int, int], None]: ...
    @property
    def column_deleted(self) -> Callable[[Table, int, int], None]: ...
    @property
    def row_reordered(self) -> Callable[[Table], None]: ...
    @property
    def column_reordered(self) -> Callable[[Table], None]: ...
    @property
    def model_changed(self) -> Callable[[Table], None]: ...

class Text(GObject.GInterface, Protocol):
    """
    Interface AtkText
    """
    def add_selection(self, start_offset: int, end_offset: int) -> bool: ...
    @staticmethod
    def free_ranges(ranges: Sequence[TextRange]) -> None: ...
    def get_bounded_ranges(
        self,
        rect: TextRectangle,
        coord_type: CoordType,
        x_clip_type: TextClipType,
        y_clip_type: TextClipType,
    ) -> list[TextRange]: ...
    def get_caret_offset(self) -> int: ...
    def get_character_at_offset(self, offset: int) -> str: ...
    def get_character_count(self) -> int: ...
    def get_character_extents(
        self, offset: int, coords: CoordType
    ) -> tuple[int, int, int, int]: ...
    def get_default_attributes(self) -> list[None]: ...
    def get_n_selections(self) -> int: ...
    def get_offset_at_point(self, x: int, y: int, coords: CoordType) -> int: ...
    def get_range_extents(
        self, start_offset: int, end_offset: int, coord_type: CoordType
    ) -> TextRectangle: ...
    def get_run_attributes(self, offset: int) -> tuple[list[None], int, int]: ...
    def get_selection(self, selection_num: int) -> tuple[str, int, int]: ...
    def get_string_at_offset(
        self, offset: int, granularity: TextGranularity
    ) -> tuple[str | None, int, int]: ...
    def get_text(self, start_offset: int, end_offset: int) -> str: ...
    def get_text_after_offset(
        self, offset: int, boundary_type: TextBoundary
    ) -> tuple[str, int, int]: ...
    def get_text_at_offset(
        self, offset: int, boundary_type: TextBoundary
    ) -> tuple[str, int, int]: ...
    def get_text_before_offset(
        self, offset: int, boundary_type: TextBoundary
    ) -> tuple[str, int, int]: ...
    def remove_selection(self, selection_num: int) -> bool: ...
    def scroll_substring_to(
        self, start_offset: int, end_offset: int, type: ScrollType
    ) -> bool: ...
    def scroll_substring_to_point(
        self, start_offset: int, end_offset: int, coords: CoordType, x: int, y: int
    ) -> bool: ...
    def set_caret_offset(self, offset: int) -> bool: ...
    def set_selection(
        self, selection_num: int, start_offset: int, end_offset: int
    ) -> bool: ...

class TextIface(_gi.Struct):
    """
    :Constructors:

    ::

        TextIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_text(self) -> Callable[[Text, int, int], str]: ...
    @property
    def get_text_after_offset(
        self,
    ) -> Callable[[Text, int, TextBoundary], tuple[str, int, int]]: ...
    @property
    def get_text_at_offset(
        self,
    ) -> Callable[[Text, int, TextBoundary], tuple[str, int, int]]: ...
    @property
    def get_character_at_offset(self) -> Callable[[Text, int], str]: ...
    @property
    def get_text_before_offset(
        self,
    ) -> Callable[[Text, int, TextBoundary], tuple[str, int, int]]: ...
    @property
    def get_caret_offset(self) -> Callable[[Text], int]: ...
    @property
    def get_run_attributes(
        self,
    ) -> Callable[[Text, int], tuple[list[None], int, int]]: ...
    @property
    def get_default_attributes(self) -> Callable[[Text], list[None]]: ...
    @property
    def get_character_extents(
        self,
    ) -> Callable[[Text, int, CoordType], tuple[int, int, int, int]]: ...
    @property
    def get_character_count(self) -> Callable[[Text], int]: ...
    @property
    def get_offset_at_point(self) -> Callable[[Text, int, int, CoordType], int]: ...
    @property
    def get_n_selections(self) -> Callable[[Text], int]: ...
    @property
    def get_selection(self) -> Callable[[Text, int], tuple[str, int, int]]: ...
    @property
    def add_selection(self) -> Callable[[Text, int, int], bool]: ...
    @property
    def remove_selection(self) -> Callable[[Text, int], bool]: ...
    @property
    def set_selection(self) -> Callable[[Text, int, int, int], bool]: ...
    @property
    def set_caret_offset(self) -> Callable[[Text, int], bool]: ...
    @property
    def text_changed(self) -> Callable[[Text, int, int], None]: ...
    @property
    def text_caret_moved(self) -> Callable[[Text, int], None]: ...
    @property
    def text_selection_changed(self) -> Callable[[Text], None]: ...
    @property
    def text_attributes_changed(self) -> Callable[[Text], None]: ...
    @property
    def get_range_extents(
        self,
    ) -> Callable[[Text, int, int, CoordType], TextRectangle]: ...
    @property
    def get_bounded_ranges(
        self,
    ) -> Callable[
        [Text, TextRectangle, CoordType, TextClipType, TextClipType], list[TextRange]
    ]: ...
    @property
    def get_string_at_offset(
        self,
    ) -> Callable[[Text, int, TextGranularity], tuple[str | None, int, int]]: ...
    @property
    def scroll_substring_to(self) -> Callable[[Text, int, int, ScrollType], bool]: ...
    @property
    def scroll_substring_to_point(
        self,
    ) -> Callable[[Text, int, int, CoordType, int, int], bool]: ...

class TextRange(GObject.GBoxed):
    """
    :Constructors:

    ::

        TextRange()
    """

    bounds: TextRectangle
    start_offset: int
    end_offset: int
    content: str

class TextRectangle(_gi.Struct):
    """
    :Constructors:

    ::

        TextRectangle()
    """

    x: int
    y: int
    width: int
    height: int

class TextSelection(_gi.Struct):
    """
    :Constructors:

    ::

        TextSelection()
    """

    start_object: Object
    start_offset: int
    end_object: Object
    end_offset: int
    start_is_active: bool

class Util(GObject.Object):
    """
    :Constructors:

    ::

        Util(**properties)

    Object AtkUtil

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...

class UtilClass(_gi.Struct):
    """
    :Constructors:

    ::

        UtilClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...
    @property
    def add_global_event_listener(self) -> None: ...
    @property
    def remove_global_event_listener(self) -> Callable[[int], None]: ...
    @property
    def add_key_event_listener(self) -> None: ...
    @property
    def remove_key_event_listener(self) -> Callable[[int], None]: ...
    @property
    def get_root(self) -> None: ...
    @property
    def get_toolkit_name(self) -> Callable[[], str]: ...
    @property
    def get_toolkit_version(self) -> Callable[[], str]: ...

class Value(GObject.GInterface, Protocol):
    """
    Interface AtkValue
    """
    def get_current_value(self) -> Any: ...
    def get_increment(self) -> float: ...
    def get_maximum_value(self) -> Any: ...
    def get_minimum_increment(self) -> Any: ...
    def get_minimum_value(self) -> Any: ...
    def get_range(self) -> Range | None: ...
    def get_sub_ranges(self) -> list[Range]: ...
    def get_value_and_text(self) -> tuple[float, str]: ...
    def set_current_value(self, value: Any) -> bool: ...
    def set_value(self, new_value: float) -> None: ...

class ValueIface(_gi.Struct):
    """
    :Constructors:

    ::

        ValueIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def get_current_value(self) -> Callable[[Value], Any]: ...
    @property
    def get_maximum_value(self) -> Callable[[Value], Any]: ...
    @property
    def get_minimum_value(self) -> Callable[[Value], Any]: ...
    @property
    def set_current_value(self) -> Callable[[Value, Any], bool]: ...
    @property
    def get_minimum_increment(self) -> Callable[[Value], Any]: ...
    @property
    def get_value_and_text(self) -> Callable[[Value], tuple[float, str]]: ...
    @property
    def get_range(self) -> Callable[[Value], Range | None]: ...
    @property
    def get_increment(self) -> Callable[[Value], float]: ...
    @property
    def get_sub_ranges(self) -> Callable[[Value], list[Range]]: ...
    @property
    def set_value(self) -> Callable[[Value, float], None]: ...

class Window(GObject.GInterface, Protocol): ...

class WindowIface(_gi.Struct):
    """
    :Constructors:

    ::

        WindowIface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...

class HyperlinkStateFlags(GObject.GFlags):
    INLINE = 1

class CoordType(GObject.GEnum):
    PARENT = 2
    SCREEN = 0
    WINDOW = 1

class KeyEventType(GObject.GEnum):
    LAST_DEFINED = 2
    PRESS = 0
    RELEASE = 1

class Layer(GObject.GEnum):
    BACKGROUND = 1
    CANVAS = 2
    INVALID = 0
    MDI = 4
    OVERLAY = 6
    POPUP = 5
    WIDGET = 3
    WINDOW = 7

class Live(GObject.GEnum):
    ASSERTIVE = 2
    NONE = 0
    POLITE = 1

class RelationType(GObject.GEnum):
    CONTROLLED_BY = 1
    CONTROLLER_FOR = 2
    DESCRIBED_BY = 14
    DESCRIPTION_FOR = 15
    DETAILS = 17
    DETAILS_FOR = 18
    EMBEDDED_BY = 11
    EMBEDS = 10
    ERROR_FOR = 20
    ERROR_MESSAGE = 19
    FLOWS_FROM = 8
    FLOWS_TO = 7
    LABELLED_BY = 4
    LABEL_FOR = 3
    LAST_DEFINED = 21
    MEMBER_OF = 5
    NODE_CHILD_OF = 6
    NODE_PARENT_OF = 16
    NULL = 0
    PARENT_WINDOW_OF = 13
    POPUP_FOR = 12
    SUBWINDOW_OF = 9
    @staticmethod
    def for_name(name: str) -> RelationType: ...
    @staticmethod
    def get_name(type: RelationType) -> str: ...
    @staticmethod
    def register(name: str) -> RelationType: ...

class Role(GObject.GEnum):
    ACCELERATOR_LABEL = 1
    ALERT = 2
    ANIMATION = 3
    APPLICATION = 73
    ARROW = 4
    ARTICLE = 107
    AUDIO = 104
    AUTOCOMPLETE = 74
    BLOCK_QUOTE = 103
    BUTTON = 42
    CALENDAR = 5
    CANVAS = 6
    CAPTION = 79
    CHART = 78
    CHECK_BOX = 7
    CHECK_MENU_ITEM = 8
    COLOR_CHOOSER = 9
    COLUMN_HEADER = 10
    COMBO_BOX = 11
    COMMENT = 95
    CONTENT_DELETION = 123
    CONTENT_INSERTION = 124
    DATE_EDITOR = 12
    DEFINITION = 106
    DESCRIPTION_LIST = 114
    DESCRIPTION_TERM = 115
    DESCRIPTION_VALUE = 116
    DESKTOP_FRAME = 14
    DESKTOP_ICON = 13
    DIAL = 15
    DIALOG = 16
    DIRECTORY_PANE = 17
    DOCUMENT_EMAIL = 94
    DOCUMENT_FRAME = 80
    DOCUMENT_PRESENTATION = 91
    DOCUMENT_SPREADSHEET = 90
    DOCUMENT_TEXT = 92
    DOCUMENT_WEB = 93
    DRAWING_AREA = 18
    EDIT_BAR = 75
    EMBEDDED = 76
    ENTRY = 77
    FILE_CHOOSER = 19
    FILLER = 20
    FONT_CHOOSER = 21
    FOOTER = 70
    FOOTNOTE = 122
    FORM = 85
    FRAME = 22
    GLASS_PANE = 23
    GROUPING = 97
    HEADER = 69
    HEADING = 81
    HTML_CONTAINER = 24
    ICON = 25
    IMAGE = 26
    IMAGE_MAP = 98
    INFO_BAR = 100
    INPUT_METHOD_WINDOW = 87
    INTERNAL_FRAME = 27
    INVALID = 0
    LABEL = 28
    LANDMARK = 108
    LAST_DEFINED = 129
    LAYERED_PANE = 29
    LEVEL_BAR = 101
    LINK = 86
    LIST = 30
    LIST_BOX = 96
    LIST_ITEM = 31
    LOG = 109
    MARK = 125
    MARQUEE = 110
    MATH = 111
    MATH_FRACTION = 118
    MATH_ROOT = 119
    MENU = 32
    MENU_BAR = 33
    MENU_ITEM = 34
    NOTIFICATION = 99
    OPTION_PANE = 35
    PAGE = 82
    PAGE_TAB = 36
    PAGE_TAB_LIST = 37
    PANEL = 38
    PARAGRAPH = 71
    PASSWORD_TEXT = 39
    POPUP_MENU = 40
    PROGRESS_BAR = 41
    PUSH_BUTTON = 42
    PUSH_BUTTON_MENU = 127
    RADIO_BUTTON = 43
    RADIO_MENU_ITEM = 44
    RATING = 112
    REDUNDANT_OBJECT = 84
    ROOT_PANE = 45
    ROW_HEADER = 46
    RULER = 72
    SCROLL_BAR = 47
    SCROLL_PANE = 48
    SECTION = 83
    SEPARATOR = 49
    SLIDER = 50
    SPIN_BUTTON = 52
    SPLIT_PANE = 51
    STATIC = 117
    STATUSBAR = 53
    SUBSCRIPT = 120
    SUGGESTION = 126
    SUPERSCRIPT = 121
    SWITCH = 128
    TABLE = 54
    TABLE_CELL = 55
    TABLE_COLUMN_HEADER = 56
    TABLE_ROW = 88
    TABLE_ROW_HEADER = 57
    TEAR_OFF_MENU_ITEM = 58
    TERMINAL = 59
    TEXT = 60
    TIMER = 113
    TITLE_BAR = 102
    TOGGLE_BUTTON = 61
    TOOL_BAR = 62
    TOOL_TIP = 63
    TREE = 64
    TREE_ITEM = 89
    TREE_TABLE = 65
    UNKNOWN = 66
    VIDEO = 105
    VIEWPORT = 67
    WINDOW = 68
    @staticmethod
    def for_name(name: str) -> Role: ...
    @staticmethod
    def get_localized_name(role: Role) -> str: ...
    @staticmethod
    def get_name(role: Role) -> str: ...
    @staticmethod
    def register(name: str) -> Role: ...

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
    ANIMATED = 37
    ARMED = 2
    BUSY = 3
    CHECKABLE = 39
    CHECKED = 4
    COLLAPSED = 43
    DEFAULT = 36
    DEFUNCT = 5
    EDITABLE = 6
    ENABLED = 7
    EXPANDABLE = 8
    EXPANDED = 9
    FOCUSABLE = 10
    FOCUSED = 11
    HAS_POPUP = 40
    HAS_TOOLTIP = 41
    HORIZONTAL = 12
    ICONIFIED = 13
    INDETERMINATE = 30
    INVALID = 0
    INVALID_ENTRY = 33
    LAST_DEFINED = 44
    MANAGES_DESCENDANTS = 29
    MODAL = 14
    MULTISELECTABLE = 16
    MULTI_LINE = 15
    OPAQUE = 17
    PRESSED = 18
    READ_ONLY = 42
    REQUIRED = 32
    RESIZABLE = 19
    SELECTABLE = 20
    SELECTABLE_TEXT = 35
    SELECTED = 21
    SENSITIVE = 22
    SHOWING = 23
    SINGLE_LINE = 24
    STALE = 25
    SUPPORTS_AUTOCOMPLETION = 34
    TRANSIENT = 26
    TRUNCATED = 31
    VERTICAL = 27
    VISIBLE = 28
    VISITED = 38
    @staticmethod
    def for_name(name: str) -> StateType: ...
    @staticmethod
    def get_name(type: StateType) -> str: ...
    @staticmethod
    def register(name: str) -> StateType: ...

class TextAttribute(GObject.GEnum):
    BG_COLOR = 18
    BG_FULL_HEIGHT = 9
    BG_STIPPLE = 20
    DIRECTION = 23
    EDITABLE = 5
    FAMILY_NAME = 17
    FG_COLOR = 19
    FG_STIPPLE = 21
    INDENT = 3
    INVALID = 0
    INVISIBLE = 4
    JUSTIFICATION = 24
    LANGUAGE = 16
    LAST_DEFINED = 29
    LEFT_MARGIN = 1
    PIXELS_ABOVE_LINES = 6
    PIXELS_BELOW_LINES = 7
    PIXELS_INSIDE_WRAP = 8
    RIGHT_MARGIN = 2
    RISE = 10
    SCALE = 14
    SIZE = 13
    STRETCH = 25
    STRIKETHROUGH = 12
    STYLE = 27
    TEXT_POSITION = 28
    UNDERLINE = 11
    VARIANT = 26
    WEIGHT = 15
    WRAP_MODE = 22
    @staticmethod
    def for_name(name: str) -> TextAttribute: ...
    @staticmethod
    def get_name(attr: TextAttribute) -> str: ...
    @staticmethod
    def get_value(attr: TextAttribute, index_: int) -> str | None: ...
    @staticmethod
    def register(name: str) -> TextAttribute: ...

class TextBoundary(GObject.GEnum):
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

class ValueType(GObject.GEnum):
    ACCEPTABLE = 2
    BAD = 11
    BEST = 14
    GOOD = 12
    HIGH = 8
    LAST_DEFINED = 15
    LOW = 6
    MEDIUM = 7
    STRONG = 3
    VERY_BAD = 10
    VERY_GOOD = 13
    VERY_HIGH = 9
    VERY_LOW = 5
    VERY_STRONG = 4
    VERY_WEAK = 0
    WEAK = 1
    @staticmethod
    def get_localized_name(value_type: ValueType) -> str: ...
    @staticmethod
    def get_name(value_type: ValueType) -> str: ...
