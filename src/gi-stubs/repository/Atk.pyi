from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

try:
    from warnings import deprecated
except ImportError:
    from typing_extensions import deprecated

from gi.repository import GLib
from gi.repository import GObject

BINARY_AGE: int = 25010
INTERFACE_AGE: int = 1
MAJOR_VERSION: int = 2
MICRO_VERSION: int = 0
MINOR_VERSION: int = 50
VERSION_MIN_REQUIRED: int = 2
_lock = ...  # FIXME Constant
_namespace: str = "Atk"
_version: str = "1.0"

def attribute_set_free(attrib_set: list[None]) -> None: ...
@deprecated(
    "Focus tracking has been dropped as a feature to be implemented by ATK itself. As #AtkObject::focus-event was deprecated in favor of a #AtkObject::state-change signal, in order to notify a focus change on your implementation, you can use atk_object_notify_state_change() instead."
)
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
@deprecated(
    'Focus tracking has been dropped as a feature to be implemented by ATK itself. If you need focus tracking on your implementation, subscribe to the #AtkObject::state-change "focused" signal.'
)
def remove_focus_tracker(tracker_id: int) -> None: ...
def remove_global_event_listener(listener_id: int) -> None: ...
def remove_key_event_listener(listener_id: int) -> None: ...
def role_for_name(name: str) -> Role: ...
def role_get_localized_name(role: Role) -> str: ...
def role_get_name(role: Role) -> str: ...
@deprecated(
    "Since 2.12. If your application/toolkit doesn't find a suitable role for a specific object defined at #AtkRole, please submit a bug in order to add a new role to the specification."
)
def role_register(name: str) -> Role: ...
def state_type_for_name(name: str) -> StateType: ...
def state_type_get_name(type: StateType) -> str: ...
def state_type_register(name: str) -> StateType: ...
def text_attribute_for_name(name: str) -> TextAttribute: ...
def text_attribute_get_name(attr: TextAttribute) -> str: ...
def text_attribute_get_value(attr: TextAttribute, index_: int) -> Optional[str]: ...
def text_attribute_register(name: str) -> TextAttribute: ...
def text_free_ranges(ranges: Sequence[TextRange]) -> None: ...
def value_type_get_localized_name(value_type: ValueType) -> str: ...
def value_type_get_name(value_type: ValueType) -> str: ...

class Action(GObject.GInterface):
    """
    Interface AtkAction
    """

    def do_action(self, i: int) -> bool: ...
    def get_description(self, i: int) -> Optional[str]: ...
    def get_keybinding(self, i: int) -> Optional[str]: ...
    def get_localized_name(self, i: int) -> Optional[str]: ...
    def get_n_actions(self) -> int: ...
    def get_name(self, i: int) -> Optional[str]: ...
    def set_description(self, i: int, desc: str) -> bool: ...

class ActionIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionIface()
    """

    parent: GObject.TypeInterface = ...
    do_action: Callable[[Action, int], bool] = ...
    get_n_actions: Callable[[Action], int] = ...
    get_description: Callable[[Action, int], Optional[str]] = ...
    get_name: Callable[[Action, int], Optional[str]] = ...
    get_keybinding: Callable[[Action, int], Optional[str]] = ...
    set_description: Callable[[Action, int, str], bool] = ...
    get_localized_name: Callable[[Action, int], Optional[str]] = ...

class Attribute(GObject.GPointer):
    """
    :Constructors:

    ::

        Attribute()
    """

    name: str = ...
    value: str = ...
    @staticmethod
    def set_free(attrib_set: list[None]) -> None: ...

class Component(GObject.GInterface):
    """
    Interface AtkComponent
    """

    def contains(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def get_alpha(self) -> float: ...
    def get_extents(self, coord_type: CoordType) -> Tuple[int, int, int, int]: ...
    def get_layer(self) -> Layer: ...
    def get_mdi_zorder(self) -> int: ...
    @deprecated("Since 2.12. Use atk_component_get_extents() instead.")
    def get_position(self, coord_type: CoordType) -> Tuple[int, int]: ...
    @deprecated("Since 2.12. Use atk_component_get_extents() instead.")
    def get_size(self) -> Tuple[int, int]: ...
    def grab_focus(self) -> bool: ...
    def ref_accessible_at_point(
        self, x: int, y: int, coord_type: CoordType
    ) -> Optional[Object]: ...
    @deprecated(
        'If you need to track when an object gains or lose the focus, use the #AtkObject::state-change "focused" notification instead.'
    )
    def remove_focus_handler(self, handler_id: int) -> None: ...
    def scroll_to(self, type: ScrollType) -> bool: ...
    def scroll_to_point(self, coords: CoordType, x: int, y: int) -> bool: ...
    def set_extents(
        self, x: int, y: int, width: int, height: int, coord_type: CoordType
    ) -> bool: ...
    def set_position(self, x: int, y: int, coord_type: CoordType) -> bool: ...
    def set_size(self, width: int, height: int) -> bool: ...

class ComponentIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ComponentIface()
    """

    parent: GObject.TypeInterface = ...
    add_focus_handler: None = ...
    contains: Callable[[Component, int, int, CoordType], bool] = ...
    ref_accessible_at_point: Callable[
        [Component, int, int, CoordType], Optional[Object]
    ] = ...
    get_extents: Callable[[Component, CoordType], Tuple[int, int, int, int]] = ...
    get_position: Callable[[Component, CoordType], Tuple[int, int]] = ...
    get_size: Callable[[Component], Tuple[int, int]] = ...
    grab_focus: Callable[[Component], bool] = ...
    remove_focus_handler: Callable[[Component, int], None] = ...
    set_extents: Callable[[Component, int, int, int, int, CoordType], bool] = ...
    set_position: Callable[[Component, int, int, CoordType], bool] = ...
    set_size: Callable[[Component, int, int], bool] = ...
    get_layer: Callable[[Component], Layer] = ...
    get_mdi_zorder: Callable[[Component], int] = ...
    bounds_changed: Callable[[Component, Rectangle], None] = ...
    get_alpha: Callable[[Component], float] = ...
    scroll_to: Callable[[Component, ScrollType], bool] = ...
    scroll_to_point: Callable[[Component, CoordType, int, int], bool] = ...

class Document(GObject.GInterface):
    """
    Interface AtkDocument
    """

    def get_attribute_value(self, attribute_name: str) -> Optional[str]: ...
    def get_attributes(self) -> list[None]: ...
    def get_current_page_number(self) -> int: ...
    @deprecated(
        "Since 2.12. @document is already a representation of the document. Use it directly, or one of its children, as an instance of the DOM."
    )
    def get_document(self) -> None: ...
    @deprecated(
        "Since 2.12. Please use atk_document_get_attributes() to ask for the document type if it applies."
    )
    def get_document_type(self) -> str: ...
    @deprecated("Please use atk_object_get_object_locale() instead.")
    def get_locale(self) -> str: ...
    def get_page_count(self) -> int: ...
    def set_attribute_value(
        self, attribute_name: str, attribute_value: str
    ) -> bool: ...

class DocumentIface(GObject.GPointer):
    """
    :Constructors:

    ::

        DocumentIface()
    """

    parent: GObject.TypeInterface = ...
    get_document_type: Callable[[Document], str] = ...
    get_document: Callable[[Document], None] = ...
    get_document_locale: Callable[[Document], str] = ...
    get_document_attributes: Callable[[Document], list[None]] = ...
    get_document_attribute_value: Callable[[Document, str], Optional[str]] = ...
    set_document_attribute: Callable[[Document, str, str], bool] = ...
    get_current_page_number: Callable[[Document], int] = ...
    get_page_count: Callable[[Document], int] = ...

class EditableText(GObject.GInterface):
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

class EditableTextIface(GObject.GPointer):
    """
    :Constructors:

    ::

        EditableTextIface()
    """

    parent_interface: GObject.TypeInterface = ...
    set_run_attributes: Callable[[EditableText, list[None], int, int], bool] = ...
    set_text_contents: Callable[[EditableText, str], None] = ...
    insert_text: Callable[[EditableText, str, int, int], None] = ...
    copy_text: Callable[[EditableText, int, int], None] = ...
    cut_text: Callable[[EditableText, int, int], None] = ...
    delete_text: Callable[[EditableText, int, int], None] = ...
    paste_text: Callable[[EditableText, int], None] = ...

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

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_hypertext_nlinks: int
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
    props: Props = ...
    parent: Object = ...
    def __init__(
        self,
        accessible_description: str = ...,
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
    ): ...
    @staticmethod
    def for_object(obj: GObject.Object) -> Object: ...
    def get_object(self) -> GObject.Object: ...

class GObjectAccessibleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GObjectAccessibleClass()
    """

    parent_class: ObjectClass = ...
    pad1: Callable[..., bool] = ...
    pad2: Callable[..., bool] = ...

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

    class Props:
        end_index: int
        number_of_anchors: int
        selected_link: bool
        start_index: int
    props: Props = ...
    parent: GObject.Object = ...
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
    @deprecated(
        "Please use ATK_STATE_FOCUSABLE for all links, and ATK_STATE_FOCUSED for focused links."
    )
    def is_selected_link(self) -> bool: ...
    def is_valid(self) -> bool: ...

class HyperlinkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HyperlinkClass()
    """

    parent: GObject.ObjectClass = ...
    get_uri: Callable[[Hyperlink, int], str] = ...
    get_object: Callable[[Hyperlink, int], Object] = ...
    get_end_index: Callable[[Hyperlink], int] = ...
    get_start_index: Callable[[Hyperlink], int] = ...
    is_valid: Callable[[Hyperlink], bool] = ...
    get_n_anchors: Callable[[Hyperlink], int] = ...
    link_state: Callable[[Hyperlink], int] = ...
    is_selected_link: Callable[[Hyperlink], bool] = ...
    link_activated: Callable[[Hyperlink], None] = ...
    pad1: Callable[..., bool] = ...

class HyperlinkImpl(GObject.GInterface):
    """
    Interface AtkHyperlinkImpl
    """

    def get_hyperlink(self) -> Hyperlink: ...

class HyperlinkImplIface(GObject.GPointer):
    """
    :Constructors:

    ::

        HyperlinkImplIface()
    """

    parent: GObject.TypeInterface = ...
    get_hyperlink: Callable[[HyperlinkImpl], Hyperlink] = ...

class Hypertext(GObject.GInterface):
    """
    Interface AtkHypertext
    """

    def get_link(self, link_index: int) -> Hyperlink: ...
    def get_link_index(self, char_index: int) -> int: ...
    def get_n_links(self) -> int: ...

class HypertextIface(GObject.GPointer):
    """
    :Constructors:

    ::

        HypertextIface()
    """

    parent: GObject.TypeInterface = ...
    get_link: Callable[[Hypertext, int], Hyperlink] = ...
    get_n_links: Callable[[Hypertext], int] = ...
    get_link_index: Callable[[Hypertext, int], int] = ...
    link_selected: Callable[[Hypertext, int], None] = ...

class Image(GObject.GInterface):
    """
    Interface AtkImage
    """

    def get_image_description(self) -> str: ...
    def get_image_locale(self) -> Optional[str]: ...
    def get_image_position(self, coord_type: CoordType) -> Tuple[int, int]: ...
    def get_image_size(self) -> Tuple[int, int]: ...
    def set_image_description(self, description: str) -> bool: ...

class ImageIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ImageIface()
    """

    parent: GObject.TypeInterface = ...
    get_image_position: Callable[[Image, CoordType], Tuple[int, int]] = ...
    get_image_description: Callable[[Image], str] = ...
    get_image_size: Callable[[Image], Tuple[int, int]] = ...
    set_image_description: Callable[[Image, str], bool] = ...
    get_image_locale: Callable[[Image], Optional[str]] = ...

class Implementor(GObject.GPointer):
    def ref_accessible(self) -> Object: ...

class ImplementorIface(GObject.GInterface): ...

class KeyEventStruct(GObject.GPointer):
    """
    :Constructors:

    ::

        KeyEventStruct()
    """

    type: int = ...
    state: int = ...
    keyval: int = ...
    length: int = ...
    string: str = ...
    keycode: int = ...
    timestamp: int = ...

class Misc(GObject.Object):
    """
    :Constructors:

    ::

        Misc(**properties)

    Object AtkMisc

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    def do_threads_enter(self) -> None: ...
    def do_threads_leave(self) -> None: ...
    @deprecated("Since 2.12.")
    @staticmethod
    def get_instance() -> Misc: ...
    @deprecated("Since 2.12.")
    def threads_enter(self) -> None: ...
    @deprecated("Since 2.12.")
    def threads_leave(self) -> None: ...

class MiscClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MiscClass()
    """

    parent: GObject.ObjectClass = ...
    threads_enter: Callable[[Misc], None] = ...
    threads_leave: Callable[[Misc], None] = ...
    vfuncs: list[None] = ...

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

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_hypertext_nlinks: int
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
    props: Props = ...
    parent: Object = ...
    def __init__(
        self,
        accessible_description: str = ...,
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
    ): ...
    @classmethod
    def new(cls, obj: GObject.Object) -> NoOpObject: ...

class NoOpObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NoOpObjectClass()
    """

    parent_class: ObjectClass = ...

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

    parent: ObjectFactory = ...
    @classmethod
    def new(cls) -> NoOpObjectFactory: ...

class NoOpObjectFactoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NoOpObjectFactoryClass()
    """

    parent_class: ObjectFactoryClass = ...

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

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_hypertext_nlinks: int
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
    props: Props = ...
    parent: GObject.Object = ...
    description: str = ...
    name: str = ...
    accessible_parent: Object = ...
    role: Role = ...
    relation_set: RelationSet = ...
    layer: Layer = ...
    def __init__(
        self,
        accessible_description: str = ...,
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
    ): ...
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
    def get_index_in_parent(self) -> int: ...
    @deprecated("Use atk_component_get_layer instead.")
    def get_layer(self) -> Layer: ...
    @deprecated("Use atk_component_get_mdi_zorder instead.")
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
    @deprecated("See atk_object_connect_property_change_handler()")
    def remove_property_change_handler(self, handler_id: int) -> None: ...
    def remove_relationship(
        self, relationship: RelationType, target: Object
    ) -> bool: ...
    def set_accessible_id(self, name: str) -> None: ...
    def set_description(self, description: str) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_parent(self, parent: Object) -> None: ...
    def set_role(self, role: Role) -> None: ...

class ObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """

    parent: GObject.ObjectClass = ...
    get_name: Callable[[Object], str] = ...
    get_description: Callable[[Object], str] = ...
    get_parent: Callable[[Object], Object] = ...
    get_n_children: Callable[[Object], int] = ...
    ref_child: None = ...
    get_index_in_parent: Callable[[Object], int] = ...
    ref_relation_set: Callable[[Object], RelationSet] = ...
    get_role: Callable[[Object], Role] = ...
    get_layer: Callable[[Object], Layer] = ...
    get_mdi_zorder: Callable[[Object], int] = ...
    ref_state_set: Callable[[Object], StateSet] = ...
    set_name: Callable[[Object, str], None] = ...
    set_description: Callable[[Object, str], None] = ...
    set_parent: Callable[[Object, Object], None] = ...
    set_role: Callable[[Object, Role], None] = ...
    connect_property_change_handler: None = ...
    remove_property_change_handler: Callable[[Object, int], None] = ...
    initialize: Callable[[Object, None], None] = ...
    children_changed: Callable[[Object, int, None], None] = ...
    focus_event: Callable[[Object, bool], None] = ...
    property_change: Callable[[Object, PropertyValues], None] = ...
    state_change: Callable[[Object, str, bool], None] = ...
    visible_data_changed: Callable[[Object], None] = ...
    active_descendant_changed: Callable[[Object, None], None] = ...
    get_attributes: Callable[[Object], list[None]] = ...
    get_object_locale: Callable[[Object], str] = ...
    pad1: Callable[..., bool] = ...

class ObjectFactory(GObject.Object):
    """
    :Constructors:

    ::

        ObjectFactory(**properties)

    Object AtkObjectFactory

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    def create_accessible(self, obj: GObject.Object) -> Object: ...
    def do_invalidate(self) -> None: ...
    def get_accessible_type(self) -> Type: ...
    def invalidate(self) -> None: ...

class ObjectFactoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectFactoryClass()
    """

    parent_class: GObject.ObjectClass = ...
    create_accessible: None = ...
    invalidate: Callable[[ObjectFactory], None] = ...
    get_accessible_type: Callable[[], Type] = ...
    pad1: Callable[..., bool] = ...
    pad2: Callable[..., bool] = ...

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

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_hypertext_nlinks: int
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
    props: Props = ...
    parent: Object = ...
    def __init__(
        self,
        accessible_description: str = ...,
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
    ): ...
    def do_get_object_id(self) -> str: ...
    def get_id(self) -> str: ...
    @classmethod
    def new(cls) -> Plug: ...
    def set_child(self, child: Object) -> None: ...

class PlugClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PlugClass()
    """

    parent_class: ObjectClass = ...
    get_object_id: Callable[[Plug], str] = ...

class PropertyValues(GObject.GPointer):
    """
    :Constructors:

    ::

        PropertyValues()
    """

    property_name: str = ...
    old_value: Any = ...
    new_value: Any = ...

class Range(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(lower_limit:float, upper_limit:float, description:str) -> Atk.Range
    """

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

    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...

class Registry(GObject.Object):
    """
    :Constructors:

    ::

        Registry(**properties)

    Object AtkRegistry

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    factory_type_registry: dict[None, None] = ...
    factory_singleton_cache: dict[None, None] = ...
    def get_factory(self, type: Type) -> ObjectFactory: ...
    def get_factory_type(self, type: Type) -> Type: ...
    def set_factory_type(self, type: Type, factory_type: Type) -> None: ...

class RegistryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RegistryClass()
    """

    parent_class: GObject.ObjectClass = ...

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

    class Props:
        relation_type: RelationType
        target: GObject.ValueArray
    props: Props = ...
    parent: GObject.Object = ...
    target: list[None] = ...
    relationship: RelationType = ...
    def __init__(
        self, relation_type: RelationType = ..., target: GObject.ValueArray = ...
    ): ...
    def add_target(self, target: Object) -> None: ...
    def get_relation_type(self) -> RelationType: ...
    def get_target(self) -> list[Object]: ...
    @classmethod
    def new(cls, targets: Sequence[Object], relationship: RelationType) -> Relation: ...
    def remove_target(self, target: Object) -> bool: ...

class RelationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RelationClass()
    """

    parent: GObject.ObjectClass = ...

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

    parent: GObject.Object = ...
    relations: list[None] = ...
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

class RelationSetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RelationSetClass()
    """

    parent: GObject.ObjectClass = ...
    pad1: Callable[..., bool] = ...
    pad2: Callable[..., bool] = ...

class Selection(GObject.GInterface):
    """
    Interface AtkSelection
    """

    def add_selection(self, i: int) -> bool: ...
    def clear_selection(self) -> bool: ...
    def get_selection_count(self) -> int: ...
    def is_child_selected(self, i: int) -> bool: ...
    def ref_selection(self, i: int) -> Optional[Object]: ...
    def remove_selection(self, i: int) -> bool: ...
    def select_all_selection(self) -> bool: ...

class SelectionIface(GObject.GPointer):
    """
    :Constructors:

    ::

        SelectionIface()
    """

    parent: GObject.TypeInterface = ...
    add_selection: Callable[[Selection, int], bool] = ...
    clear_selection: Callable[[Selection], bool] = ...
    ref_selection: Callable[[Selection, int], Optional[Object]] = ...
    get_selection_count: Callable[[Selection], int] = ...
    is_child_selected: Callable[[Selection, int], bool] = ...
    remove_selection: Callable[[Selection, int], bool] = ...
    select_all_selection: Callable[[Selection], bool] = ...
    selection_changed: Callable[[Selection], None] = ...

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

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accessible_component_layer: int
        accessible_component_mdi_zorder: int
        accessible_description: str
        accessible_hypertext_nlinks: int
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
    props: Props = ...
    parent: Object = ...
    embedded_plug_id: str = ...
    def __init__(
        self,
        accessible_description: str = ...,
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
    ): ...
    def do_embed(self, plug_id: str) -> None: ...
    def embed(self, plug_id: str) -> None: ...
    def is_occupied(self) -> bool: ...
    @classmethod
    def new(cls) -> Socket: ...

class SocketClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketClass()
    """

    parent_class: ObjectClass = ...
    embed: Callable[[Socket, str], None] = ...

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

    parent: GObject.Object = ...
    def add_state(self, type: StateType) -> bool: ...
    def add_states(self, types: Sequence[StateType]) -> None: ...
    def and_sets(self, compare_set: StateSet) -> StateSet: ...
    def clear_states(self) -> None: ...
    def contains_state(self, type: StateType) -> bool: ...
    def contains_states(self, types: Sequence[StateType]) -> bool: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new(cls) -> StateSet: ...
    def or_sets(self, compare_set: StateSet) -> Optional[StateSet]: ...
    def remove_state(self, type: StateType) -> bool: ...
    def xor_sets(self, compare_set: StateSet) -> StateSet: ...

class StateSetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StateSetClass()
    """

    parent: GObject.ObjectClass = ...

class StreamableContent(GObject.GInterface):
    """
    Interface AtkStreamableContent
    """

    def get_mime_type(self, i: int) -> str: ...
    def get_n_mime_types(self) -> int: ...
    def get_stream(self, mime_type: str) -> GLib.IOChannel: ...
    def get_uri(self, mime_type: str) -> Optional[str]: ...

class StreamableContentIface(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamableContentIface()
    """

    parent: GObject.TypeInterface = ...
    get_n_mime_types: Callable[[StreamableContent], int] = ...
    get_mime_type: Callable[[StreamableContent, int], str] = ...
    get_stream: Callable[[StreamableContent, str], GLib.IOChannel] = ...
    get_uri: Callable[[StreamableContent, str], Optional[str]] = ...
    pad1: Callable[..., bool] = ...
    pad2: Callable[..., bool] = ...
    pad3: Callable[..., bool] = ...

class Table(GObject.GInterface):
    """
    Interface AtkTable
    """

    def add_column_selection(self, column: int) -> bool: ...
    def add_row_selection(self, row: int) -> bool: ...
    def get_caption(self) -> Optional[Object]: ...
    @deprecated("Since 2.12.")
    def get_column_at_index(self, index_: int) -> int: ...
    def get_column_description(self, column: int) -> str: ...
    def get_column_extent_at(self, row: int, column: int) -> int: ...
    def get_column_header(self, column: int) -> Optional[Object]: ...
    @deprecated(
        "Since 2.12. Use atk_table_ref_at() in order to get the accessible that represents the cell at (@row, @column)"
    )
    def get_index_at(self, row: int, column: int) -> int: ...
    def get_n_columns(self) -> int: ...
    def get_n_rows(self) -> int: ...
    @deprecated("since 2.12.")
    def get_row_at_index(self, index_: int) -> int: ...
    def get_row_description(self, row: int) -> Optional[str]: ...
    def get_row_extent_at(self, row: int, column: int) -> int: ...
    def get_row_header(self, row: int) -> Optional[Object]: ...
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

class TableCell(GObject.GInterface):
    """
    Interface AtkTableCell

    Signals from GObject:
      notify (GParam)
    """

    def get_column_header_cells(self) -> list[Object]: ...
    def get_column_span(self) -> int: ...
    def get_position(self) -> Tuple[bool, int, int]: ...
    def get_row_column_span(self) -> Tuple[bool, int, int, int, int]: ...
    def get_row_header_cells(self) -> list[Object]: ...
    def get_row_span(self) -> int: ...
    def get_table(self) -> Object: ...

class TableCellIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TableCellIface()
    """

    parent: GObject.TypeInterface = ...
    get_column_span: Callable[[TableCell], int] = ...
    get_column_header_cells: Callable[[TableCell], list[Object]] = ...
    get_position: Callable[[TableCell], Tuple[bool, int, int]] = ...
    get_row_span: Callable[[TableCell], int] = ...
    get_row_header_cells: Callable[[TableCell], list[Object]] = ...
    get_row_column_span: Callable[[TableCell], Tuple[bool, int, int, int, int]] = ...
    get_table: Callable[[TableCell], Object] = ...

class TableIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TableIface()
    """

    parent: GObject.TypeInterface = ...
    ref_at: Callable[[Table, int, int], Object] = ...
    get_index_at: Callable[[Table, int, int], int] = ...
    get_column_at_index: Callable[[Table, int], int] = ...
    get_row_at_index: Callable[[Table, int], int] = ...
    get_n_columns: Callable[[Table], int] = ...
    get_n_rows: Callable[[Table], int] = ...
    get_column_extent_at: Callable[[Table, int, int], int] = ...
    get_row_extent_at: Callable[[Table, int, int], int] = ...
    get_caption: Callable[[Table], Optional[Object]] = ...
    get_column_description: Callable[[Table, int], str] = ...
    get_column_header: Callable[[Table, int], Optional[Object]] = ...
    get_row_description: Callable[[Table, int], Optional[str]] = ...
    get_row_header: Callable[[Table, int], Optional[Object]] = ...
    get_summary: Callable[[Table], Object] = ...
    set_caption: Callable[[Table, Object], None] = ...
    set_column_description: Callable[[Table, int, str], None] = ...
    set_column_header: Callable[[Table, int, Object], None] = ...
    set_row_description: Callable[[Table, int, str], None] = ...
    set_row_header: Callable[[Table, int, Object], None] = ...
    set_summary: Callable[[Table, Object], None] = ...
    get_selected_columns: Callable[[Table, int], int] = ...
    get_selected_rows: Callable[[Table, int], int] = ...
    is_column_selected: Callable[[Table, int], bool] = ...
    is_row_selected: Callable[[Table, int], bool] = ...
    is_selected: Callable[[Table, int, int], bool] = ...
    add_row_selection: Callable[[Table, int], bool] = ...
    remove_row_selection: Callable[[Table, int], bool] = ...
    add_column_selection: Callable[[Table, int], bool] = ...
    remove_column_selection: Callable[[Table, int], bool] = ...
    row_inserted: Callable[[Table, int, int], None] = ...
    column_inserted: Callable[[Table, int, int], None] = ...
    row_deleted: Callable[[Table, int, int], None] = ...
    column_deleted: Callable[[Table, int, int], None] = ...
    row_reordered: Callable[[Table], None] = ...
    column_reordered: Callable[[Table], None] = ...
    model_changed: Callable[[Table], None] = ...

class Text(GObject.GInterface):
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
    ) -> Tuple[int, int, int, int]: ...
    def get_default_attributes(self) -> list[None]: ...
    def get_n_selections(self) -> int: ...
    def get_offset_at_point(self, x: int, y: int, coords: CoordType) -> int: ...
    def get_range_extents(
        self, start_offset: int, end_offset: int, coord_type: CoordType
    ) -> TextRectangle: ...
    def get_run_attributes(self, offset: int) -> Tuple[list[None], int, int]: ...
    def get_selection(self, selection_num: int) -> Tuple[str, int, int]: ...
    def get_string_at_offset(
        self, offset: int, granularity: TextGranularity
    ) -> Tuple[Optional[str], int, int]: ...
    def get_text(self, start_offset: int, end_offset: int) -> str: ...
    @deprecated("Please use atk_text_get_string_at_offset() instead.")
    def get_text_after_offset(
        self, offset: int, boundary_type: TextBoundary
    ) -> Tuple[str, int, int]: ...
    @deprecated(
        "This method is deprecated since ATK version 2.9.4. Please use atk_text_get_string_at_offset() instead."
    )
    def get_text_at_offset(
        self, offset: int, boundary_type: TextBoundary
    ) -> Tuple[str, int, int]: ...
    @deprecated("Please use atk_text_get_string_at_offset() instead.")
    def get_text_before_offset(
        self, offset: int, boundary_type: TextBoundary
    ) -> Tuple[str, int, int]: ...
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

class TextIface(GObject.GPointer):
    """
    :Constructors:

    ::

        TextIface()
    """

    parent: GObject.TypeInterface = ...
    get_text: Callable[[Text, int, int], str] = ...
    get_text_after_offset: Callable[
        [Text, int, TextBoundary], Tuple[str, int, int]
    ] = ...
    get_text_at_offset: Callable[[Text, int, TextBoundary], Tuple[str, int, int]] = ...
    get_character_at_offset: Callable[[Text, int], str] = ...
    get_text_before_offset: Callable[
        [Text, int, TextBoundary], Tuple[str, int, int]
    ] = ...
    get_caret_offset: Callable[[Text], int] = ...
    get_run_attributes: Callable[[Text, int], Tuple[list[None], int, int]] = ...
    get_default_attributes: Callable[[Text], list[None]] = ...
    get_character_extents: Callable[
        [Text, int, CoordType], Tuple[int, int, int, int]
    ] = ...
    get_character_count: Callable[[Text], int] = ...
    get_offset_at_point: Callable[[Text, int, int, CoordType], int] = ...
    get_n_selections: Callable[[Text], int] = ...
    get_selection: Callable[[Text, int], Tuple[str, int, int]] = ...
    add_selection: Callable[[Text, int, int], bool] = ...
    remove_selection: Callable[[Text, int], bool] = ...
    set_selection: Callable[[Text, int, int, int], bool] = ...
    set_caret_offset: Callable[[Text, int], bool] = ...
    text_changed: Callable[[Text, int, int], None] = ...
    text_caret_moved: Callable[[Text, int], None] = ...
    text_selection_changed: Callable[[Text], None] = ...
    text_attributes_changed: Callable[[Text], None] = ...
    get_range_extents: Callable[[Text, int, int, CoordType], TextRectangle] = ...
    get_bounded_ranges: Callable[
        [Text, TextRectangle, CoordType, TextClipType, TextClipType], list[TextRange]
    ] = ...
    get_string_at_offset: Callable[
        [Text, int, TextGranularity], Tuple[Optional[str], int, int]
    ] = ...
    scroll_substring_to: Callable[[Text, int, int, ScrollType], bool] = ...
    scroll_substring_to_point: Callable[
        [Text, int, int, CoordType, int, int], bool
    ] = ...

class TextRange(GObject.GBoxed):
    """
    :Constructors:

    ::

        TextRange()
    """

    bounds: TextRectangle = ...
    start_offset: int = ...
    end_offset: int = ...
    content: str = ...

class TextRectangle(GObject.GPointer):
    """
    :Constructors:

    ::

        TextRectangle()
    """

    x: int = ...
    y: int = ...
    width: int = ...
    height: int = ...

class Util(GObject.Object):
    """
    :Constructors:

    ::

        Util(**properties)

    Object AtkUtil

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...

class UtilClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UtilClass()
    """

    parent: GObject.ObjectClass = ...
    add_global_event_listener: None = ...
    remove_global_event_listener: Callable[[int], None] = ...
    add_key_event_listener: None = ...
    remove_key_event_listener: Callable[[int], None] = ...
    get_root: None = ...
    get_toolkit_name: Callable[[], str] = ...
    get_toolkit_version: Callable[[], str] = ...

class Value(GObject.GInterface):
    """
    Interface AtkValue
    """

    @deprecated("Since 2.12. Use atk_value_get_value_and_text() instead.")
    def get_current_value(self) -> Any: ...
    def get_increment(self) -> float: ...
    @deprecated("Since 2.12. Use atk_value_get_range() instead.")
    def get_maximum_value(self) -> Any: ...
    @deprecated("Since 2.12. Use atk_value_get_increment() instead.")
    def get_minimum_increment(self) -> Any: ...
    @deprecated("Since 2.12. Use atk_value_get_range() instead.")
    def get_minimum_value(self) -> Any: ...
    def get_range(self) -> Optional[Range]: ...
    def get_sub_ranges(self) -> list[Range]: ...
    def get_value_and_text(self) -> Tuple[float, str]: ...
    @deprecated("Since 2.12. Use atk_value_set_value() instead.")
    def set_current_value(self, value: Any) -> bool: ...
    def set_value(self, new_value: float) -> None: ...

class ValueIface(GObject.GPointer):
    """
    :Constructors:

    ::

        ValueIface()
    """

    parent: GObject.TypeInterface = ...
    get_current_value: Callable[[Value], Any] = ...
    get_maximum_value: Callable[[Value], Any] = ...
    get_minimum_value: Callable[[Value], Any] = ...
    set_current_value: Callable[[Value, Any], bool] = ...
    get_minimum_increment: Callable[[Value], Any] = ...
    get_value_and_text: Callable[[Value], Tuple[float, str]] = ...
    get_range: Callable[[Value], Optional[Range]] = ...
    get_increment: Callable[[Value], float] = ...
    get_sub_ranges: Callable[[Value], list[Range]] = ...
    set_value: Callable[[Value, float], None] = ...

class Window(GObject.GInterface): ...

class WindowIface(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowIface()
    """

    parent: GObject.TypeInterface = ...

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
    LAST_DEFINED = 128
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
    def get_value(attr: TextAttribute, index_: int) -> Optional[str]: ...
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
