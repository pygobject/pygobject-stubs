from typing import Any
from typing import Callable
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type

from gi.repository import cairo
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Graphene
from gi.repository import Gsk
from gi.repository import Pango

ACCESSIBLE_VALUE_UNDEFINED: int = -1
BINARY_AGE: int = 803
IM_MODULE_EXTENSION_POINT_NAME: str = "gtk-im-module"
INPUT_ERROR: int = -1
INTERFACE_AGE: int = 3
INVALID_LIST_POSITION: int = 4294967295
LEVEL_BAR_OFFSET_FULL: str = "full"
LEVEL_BAR_OFFSET_HIGH: str = "high"
LEVEL_BAR_OFFSET_LOW: str = "low"
MAJOR_VERSION: int = 4
MAX_COMPOSE_LEN: int = 7
MEDIA_FILE_EXTENSION_POINT_NAME: str = "gtk-media-file"
MICRO_VERSION: int = 3
MINOR_VERSION: int = 8
PAPER_NAME_A3: str = "iso_a3"
PAPER_NAME_A4: str = "iso_a4"
PAPER_NAME_A5: str = "iso_a5"
PAPER_NAME_B5: str = "iso_b5"
PAPER_NAME_EXECUTIVE: str = "na_executive"
PAPER_NAME_LEGAL: str = "na_legal"
PAPER_NAME_LETTER: str = "na_letter"
PRINT_SETTINGS_COLLATE: str = "collate"
PRINT_SETTINGS_DEFAULT_SOURCE: str = "default-source"
PRINT_SETTINGS_DITHER: str = "dither"
PRINT_SETTINGS_DUPLEX: str = "duplex"
PRINT_SETTINGS_FINISHINGS: str = "finishings"
PRINT_SETTINGS_MEDIA_TYPE: str = "media-type"
PRINT_SETTINGS_NUMBER_UP: str = "number-up"
PRINT_SETTINGS_NUMBER_UP_LAYOUT: str = "number-up-layout"
PRINT_SETTINGS_N_COPIES: str = "n-copies"
PRINT_SETTINGS_ORIENTATION: str = "orientation"
PRINT_SETTINGS_OUTPUT_BASENAME: str = "output-basename"
PRINT_SETTINGS_OUTPUT_BIN: str = "output-bin"
PRINT_SETTINGS_OUTPUT_DIR: str = "output-dir"
PRINT_SETTINGS_OUTPUT_FILE_FORMAT: str = "output-file-format"
PRINT_SETTINGS_OUTPUT_URI: str = "output-uri"
PRINT_SETTINGS_PAGE_RANGES: str = "page-ranges"
PRINT_SETTINGS_PAGE_SET: str = "page-set"
PRINT_SETTINGS_PAPER_FORMAT: str = "paper-format"
PRINT_SETTINGS_PAPER_HEIGHT: str = "paper-height"
PRINT_SETTINGS_PAPER_WIDTH: str = "paper-width"
PRINT_SETTINGS_PRINTER: str = "printer"
PRINT_SETTINGS_PRINTER_LPI: str = "printer-lpi"
PRINT_SETTINGS_PRINT_PAGES: str = "print-pages"
PRINT_SETTINGS_QUALITY: str = "quality"
PRINT_SETTINGS_RESOLUTION: str = "resolution"
PRINT_SETTINGS_RESOLUTION_X: str = "resolution-x"
PRINT_SETTINGS_RESOLUTION_Y: str = "resolution-y"
PRINT_SETTINGS_REVERSE: str = "reverse"
PRINT_SETTINGS_SCALE: str = "scale"
PRINT_SETTINGS_USE_COLOR: str = "use-color"
PRINT_SETTINGS_WIN32_DRIVER_EXTRA: str = "win32-driver-extra"
PRINT_SETTINGS_WIN32_DRIVER_VERSION: str = "win32-driver-version"
PRIORITY_RESIZE: int = 110
STYLE_PROVIDER_PRIORITY_APPLICATION: int = 600
STYLE_PROVIDER_PRIORITY_FALLBACK: int = 1
STYLE_PROVIDER_PRIORITY_SETTINGS: int = 400
STYLE_PROVIDER_PRIORITY_THEME: int = 200
STYLE_PROVIDER_PRIORITY_USER: int = 800
TEXT_VIEW_PRIORITY_VALIDATE: int = 125
TREE_SORTABLE_DEFAULT_SORT_COLUMN_ID: int = -1
TREE_SORTABLE_UNSORTED_SORT_COLUMN_ID: int = -2
_introspection_module = ...  # FIXME Constant
_lock = ...  # FIXME Constant
_namespace: str = "Gtk"
_overrides_module = ...  # FIXME Constant
_version: str = "4.0"

def accelerator_get_default_mod_mask() -> Gdk.ModifierType: ...
def accelerator_get_label(
    accelerator_key: int, accelerator_mods: Gdk.ModifierType
) -> str: ...
def accelerator_get_label_with_keycode(
    display: Optional[Gdk.Display],
    accelerator_key: int,
    keycode: int,
    accelerator_mods: Gdk.ModifierType,
) -> str: ...
def accelerator_name(
    accelerator_key: int, accelerator_mods: Gdk.ModifierType
) -> str: ...
def accelerator_name_with_keycode(
    display: Optional[Gdk.Display],
    accelerator_key: int,
    keycode: int,
    accelerator_mods: Gdk.ModifierType,
) -> str: ...
def accelerator_parse(accelerator: str) -> Tuple[bool, int, Gdk.ModifierType]: ...
def accelerator_parse_with_keycode(
    accelerator: str, display: Optional[Gdk.Display] = None
) -> Tuple[bool, int, list[int], Gdk.ModifierType]: ...
def accelerator_valid(keyval: int, modifiers: Gdk.ModifierType) -> bool: ...
def accessible_property_init_value(
    property: AccessibleProperty, value: Any
) -> None: ...
def accessible_relation_init_value(
    relation: AccessibleRelation, value: Any
) -> None: ...
def accessible_state_init_value(state: AccessibleState, value: Any) -> None: ...
def bitset_iter_init_at(set: Bitset, target: int) -> Tuple[bool, BitsetIter, int]: ...
def bitset_iter_init_first(set: Bitset) -> Tuple[bool, BitsetIter, int]: ...
def bitset_iter_init_last(set: Bitset) -> Tuple[bool, BitsetIter, int]: ...
def builder_error_quark() -> int: ...
def check_version(
    required_major: int, required_minor: int, required_micro: int
) -> Optional[str]: ...
def constraint_vfl_parser_error_quark() -> int: ...
def css_parser_error_quark() -> int: ...
def css_parser_warning_quark() -> int: ...
def disable_setlocale() -> None: ...
def distribute_natural_allocation(
    extra_space: int, n_requested_sizes: int, sizes: Sequence[RequestedSize]
) -> int: ...
def editable_delegate_get_property(
    object: GObject.Object, prop_id: int, value: Any, pspec: GObject.ParamSpec
) -> bool: ...
def editable_delegate_set_property(
    object: GObject.Object, prop_id: int, value: Any, pspec: GObject.ParamSpec
) -> bool: ...
def editable_install_properties(
    object_class: GObject.ObjectClass, first_prop: int
) -> int: ...
def enumerate_printers(func: Callable[..., bool], wait: bool, *data: Any) -> None: ...
def file_chooser_error_quark() -> int: ...
def get_binary_age() -> int: ...
def get_debug_flags() -> DebugFlags: ...
def get_default_language() -> Pango.Language: ...
def get_interface_age() -> int: ...
def get_locale_direction() -> TextDirection: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def hsv_to_rgb(h: float, s: float, v: float) -> Tuple[float, float, float]: ...
def icon_theme_error_quark() -> int: ...
def init() -> None: ...
def init_check() -> bool: ...
def is_initialized() -> bool: ...
def native_get_for_surface(surface: Gdk.Surface) -> Optional[Native]: ...
def ordering_from_cmpfunc(cmpfunc_result: int) -> Ordering: ...
def paper_size_get_default() -> str: ...
def paper_size_get_paper_sizes(include_custom: bool) -> list[PaperSize]: ...
def param_spec_expression(
    name: str, nick: str, blurb: str, flags: GObject.ParamFlags
) -> GObject.ParamSpec: ...
def print_error_quark() -> int: ...
def print_run_page_setup_dialog(
    parent: Optional[Window], page_setup: Optional[PageSetup], settings: PrintSettings
) -> PageSetup: ...
def print_run_page_setup_dialog_async(
    parent: Optional[Window],
    page_setup: Optional[PageSetup],
    settings: PrintSettings,
    done_cb: Callable[..., None],
    *data: Any,
) -> None: ...
def recent_manager_error_quark() -> int: ...
def render_activity(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_arrow(
    context: StyleContext,
    cr: cairo.Context,
    angle: float,
    x: float,
    y: float,
    size: float,
) -> None: ...
def render_background(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_check(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_expander(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_focus(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_frame(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_handle(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def render_icon(
    context: StyleContext, cr: cairo.Context, texture: Gdk.Texture, x: float, y: float
) -> None: ...
def render_layout(
    context: StyleContext, cr: cairo.Context, x: float, y: float, layout: Pango.Layout
) -> None: ...
def render_line(
    context: StyleContext, cr: cairo.Context, x0: float, y0: float, x1: float, y1: float
) -> None: ...
def render_option(
    context: StyleContext,
    cr: cairo.Context,
    x: float,
    y: float,
    width: float,
    height: float,
) -> None: ...
def rgb_to_hsv(r: float, g: float, b: float) -> Tuple[float, float, float]: ...
def set_debug_flags(flags: DebugFlags) -> None: ...
def show_uri(parent: Optional[Window], uri: str, timestamp: int) -> None: ...
def show_uri_full(
    parent: Optional[Window],
    uri: str,
    timestamp: int,
    cancellable: Optional[Gio.Cancellable] = None,
    callback: Optional[Callable[..., None]] = None,
    *user_data: Any,
) -> None: ...
def show_uri_full_finish(parent: Window, result: Gio.AsyncResult) -> bool: ...
def test_accessible_assertion_message_role(
    domain: str,
    file: str,
    line: int,
    func: str,
    expr: str,
    accessible: Accessible,
    expected_role: AccessibleRole,
    actual_role: AccessibleRole,
) -> None: ...
def test_accessible_has_property(
    accessible: Accessible, property: AccessibleProperty
) -> bool: ...
def test_accessible_has_relation(
    accessible: Accessible, relation: AccessibleRelation
) -> bool: ...
def test_accessible_has_role(accessible: Accessible, role: AccessibleRole) -> bool: ...
def test_accessible_has_state(
    accessible: Accessible, state: AccessibleState
) -> bool: ...
def test_list_all_types() -> list[Type]: ...
def test_register_all_types() -> None: ...
def test_widget_wait_for_draw(widget: Widget) -> None: ...
def tree_create_row_drag_content(
    tree_model: TreeModel, path: TreePath
) -> Gdk.ContentProvider: ...
def tree_get_row_drag_data(value: Any) -> Tuple[bool, TreeModel, TreePath]: ...
def tree_row_reference_deleted(proxy: GObject.Object, path: TreePath) -> None: ...
def tree_row_reference_inserted(proxy: GObject.Object, path: TreePath) -> None: ...
def value_dup_expression(value: Any) -> Optional[Expression]: ...
def value_get_expression(value: Any) -> Optional[Expression]: ...
def value_set_expression(value: Any, expression: Expression) -> None: ...
def value_take_expression(
    value: Any, expression: Optional[Expression] = None
) -> None: ...

class ATContext(GObject.Object):
    class Props:
        accessible: Accessible
        accessible_role: AccessibleRole
        display: Gdk.Display
    props: Props = ...
    def __init__(
        self,
        accessible: Accessible = ...,
        accessible_role: AccessibleRole = ...,
        display: Gdk.Display = ...,
    ): ...
    @classmethod
    def create(
        cls,
        accessible_role: AccessibleRole,
        accessible: Accessible,
        display: Gdk.Display,
    ) -> Optional[ATContext]: ...
    def get_accessible(self) -> Accessible: ...
    def get_accessible_role(self) -> AccessibleRole: ...

class ATContextClass(GObject.GPointer): ...

class AboutDialog(
    Window, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        artists: list[str]
        authors: list[str]
        comments: str
        copyright: str
        documenters: list[str]
        license: str
        license_type: License
        logo: Gdk.Paintable
        logo_icon_name: str
        program_name: str
        system_information: str
        translator_credits: str
        version: str
        website: str
        website_label: str
        wrap_license: bool
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        artists: Sequence[str] = ...,
        authors: Sequence[str] = ...,
        comments: str = ...,
        copyright: str = ...,
        documenters: Sequence[str] = ...,
        license: str = ...,
        license_type: License = ...,
        logo: Gdk.Paintable = ...,
        logo_icon_name: str = ...,
        program_name: str = ...,
        system_information: str = ...,
        translator_credits: str = ...,
        version: str = ...,
        website: str = ...,
        website_label: str = ...,
        wrap_license: bool = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_credit_section(self, section_name: str, people: Sequence[str]) -> None: ...
    def get_artists(self) -> list[str]: ...
    def get_authors(self) -> list[str]: ...
    def get_comments(self) -> Optional[str]: ...
    def get_copyright(self) -> Optional[str]: ...
    def get_documenters(self) -> list[str]: ...
    def get_license(self) -> Optional[str]: ...
    def get_license_type(self) -> License: ...
    def get_logo(self) -> Optional[Gdk.Paintable]: ...
    def get_logo_icon_name(self) -> Optional[str]: ...
    def get_program_name(self) -> Optional[str]: ...
    def get_system_information(self) -> Optional[str]: ...
    def get_translator_credits(self) -> Optional[str]: ...
    def get_version(self) -> Optional[str]: ...
    def get_website(self) -> Optional[str]: ...
    def get_website_label(self) -> Optional[str]: ...
    def get_wrap_license(self) -> bool: ...
    @classmethod
    def new(cls) -> AboutDialog: ...
    def set_artists(self, artists: Sequence[str]) -> None: ...
    def set_authors(self, authors: Sequence[str]) -> None: ...
    def set_comments(self, comments: Optional[str] = None) -> None: ...
    def set_copyright(self, copyright: Optional[str] = None) -> None: ...
    def set_documenters(self, documenters: Sequence[str]) -> None: ...
    def set_license(self, license: Optional[str] = None) -> None: ...
    def set_license_type(self, license_type: License) -> None: ...
    def set_logo(self, logo: Optional[Gdk.Paintable] = None) -> None: ...
    def set_logo_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_program_name(self, name: Optional[str] = None) -> None: ...
    def set_system_information(
        self, system_information: Optional[str] = None
    ) -> None: ...
    def set_translator_credits(
        self, translator_credits: Optional[str] = None
    ) -> None: ...
    def set_version(self, version: Optional[str] = None) -> None: ...
    def set_website(self, website: Optional[str] = None) -> None: ...
    def set_website_label(self, website_label: str) -> None: ...
    def set_wrap_license(self, wrap_license: bool) -> None: ...

class Accessible(GObject.Object):
    def get_accessible_role(self) -> AccessibleRole: ...
    def reset_property(self, property: AccessibleProperty) -> None: ...
    def reset_relation(self, relation: AccessibleRelation) -> None: ...
    def reset_state(self, state: AccessibleState) -> None: ...
    def update_property(
        self,
        n_properties: int,
        properties: Sequence[AccessibleProperty],
        values: Sequence[Any],
    ) -> None: ...
    def update_relation(
        self,
        n_relations: int,
        relations: Sequence[AccessibleRelation],
        values: Sequence[Any],
    ) -> None: ...
    def update_state(
        self, n_states: int, states: Sequence[AccessibleState], values: Sequence[Any]
    ) -> None: ...

class AccessibleInterface(GObject.GPointer): ...

class ActionBar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        revealed: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        revealed: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_center_widget(self) -> Optional[Widget]: ...
    def get_revealed(self) -> bool: ...
    @classmethod
    def new(cls) -> ActionBar: ...
    def pack_end(self, child: Widget) -> None: ...
    def pack_start(self, child: Widget) -> None: ...
    def remove(self, child: Widget) -> None: ...
    def set_center_widget(self, center_widget: Optional[Widget] = None) -> None: ...
    def set_revealed(self, revealed: bool) -> None: ...

class Actionable(GObject.Object):
    def get_action_name(self) -> Optional[str]: ...
    def get_action_target_value(self) -> Optional[GLib.Variant]: ...
    def set_action_name(self, action_name: Optional[str] = None) -> None: ...
    def set_action_target_value(
        self, target_value: Optional[GLib.Variant] = None
    ) -> None: ...
    def set_detailed_action_name(self, detailed_action_name: str) -> None: ...

class ActionableInterface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    get_action_name: Callable[[Actionable], Optional[str]] = ...
    set_action_name: Callable[[Actionable, Optional[str]], None] = ...
    get_action_target_value: Callable[[Actionable], Optional[GLib.Variant]] = ...
    set_action_target_value: Callable[[Actionable, Optional[GLib.Variant]], None] = ...

class ActivateAction(ShortcutAction):
    @staticmethod
    def get() -> ActivateAction: ...

class ActivateActionClass(GObject.GPointer): ...

class Adjustment(GObject.InitiallyUnowned):
    class Props:
        lower: float
        page_increment: float
        page_size: float
        step_increment: float
        upper: float
        value: float
    props: Props = ...
    def __init__(
        self,
        lower: float = ...,
        page_increment: float = ...,
        page_size: float = ...,
        step_increment: float = ...,
        upper: float = ...,
        value: float = ...,
    ): ...
    parent_instance: GObject.InitiallyUnowned = ...
    def clamp_page(self, lower: float, upper: float) -> None: ...
    def configure(
        self,
        value: float,
        lower: float,
        upper: float,
        step_increment: float,
        page_increment: float,
        page_size: float,
    ) -> None: ...
    def do_changed(self) -> None: ...
    def do_value_changed(self) -> None: ...
    def get_lower(self) -> float: ...
    def get_minimum_increment(self) -> float: ...
    def get_page_increment(self) -> float: ...
    def get_page_size(self) -> float: ...
    def get_step_increment(self) -> float: ...
    def get_upper(self) -> float: ...
    def get_value(self) -> float: ...
    @classmethod
    def new(
        cls,
        value: float,
        lower: float,
        upper: float,
        step_increment: float,
        page_increment: float,
        page_size: float,
    ) -> Adjustment: ...
    def set_lower(self, lower: float) -> None: ...
    def set_page_increment(self, page_increment: float) -> None: ...
    def set_page_size(self, page_size: float) -> None: ...
    def set_step_increment(self, step_increment: float) -> None: ...
    def set_upper(self, upper: float) -> None: ...
    def set_value(self, value: float) -> None: ...

class AdjustmentClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...
    changed: Callable[[Adjustment], None] = ...
    value_changed: Callable[[Adjustment], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class AlternativeTrigger(ShortcutTrigger):
    class Props:
        first: ShortcutTrigger
        second: ShortcutTrigger
    props: Props = ...
    def __init__(self, first: ShortcutTrigger = ..., second: ShortcutTrigger = ...): ...
    def get_first(self) -> ShortcutTrigger: ...
    def get_second(self) -> ShortcutTrigger: ...
    @classmethod
    def new(
        cls, first: ShortcutTrigger, second: ShortcutTrigger
    ) -> AlternativeTrigger: ...

class AlternativeTriggerClass(GObject.GPointer): ...

class AnyFilter(MultiFilter, Gio.ListModel, Buildable):
    class Props:
        item_type: Type
        n_items: int
    props: Props = ...
    @classmethod
    def new(cls) -> AnyFilter: ...

class AnyFilterClass(GObject.GPointer): ...

class AppChooser(GObject.Object):
    def get_app_info(self) -> Optional[Gio.AppInfo]: ...
    def get_content_type(self) -> str: ...
    def refresh(self) -> None: ...

class AppChooserButton(Widget, Accessible, AppChooser, Buildable, ConstraintTarget):
    class Props:
        heading: str
        modal: bool
        show_default_item: bool
        show_dialog_item: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        content_type: str
    props: Props = ...
    def __init__(
        self,
        heading: str = ...,
        modal: bool = ...,
        show_default_item: bool = ...,
        show_dialog_item: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        content_type: str = ...,
    ): ...
    def append_custom_item(self, name: str, label: str, icon: Gio.Icon) -> None: ...
    def append_separator(self) -> None: ...
    def get_heading(self) -> Optional[str]: ...
    def get_modal(self) -> bool: ...
    def get_show_default_item(self) -> bool: ...
    def get_show_dialog_item(self) -> bool: ...
    @classmethod
    def new(cls, content_type: str) -> AppChooserButton: ...
    def set_active_custom_item(self, name: str) -> None: ...
    def set_heading(self, heading: str) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_show_default_item(self, setting: bool) -> None: ...
    def set_show_dialog_item(self, setting: bool) -> None: ...

class AppChooserDialog(
    Dialog,
    Accessible,
    AppChooser,
    Buildable,
    ConstraintTarget,
    Native,
    Root,
    ShortcutManager,
):
    class Props:
        gfile: Gio.File
        heading: str
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        content_type: str
    props: Props = ...
    def __init__(
        self,
        gfile: Gio.File = ...,
        heading: str = ...,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        content_type: str = ...,
    ): ...
    def get_heading(self) -> Optional[str]: ...
    def get_widget(self) -> Widget: ...
    @classmethod
    def new(
        cls, parent: Optional[Window], flags: DialogFlags, file: Gio.File
    ) -> AppChooserDialog: ...
    @classmethod
    def new_for_content_type(
        cls, parent: Optional[Window], flags: DialogFlags, content_type: str
    ) -> AppChooserDialog: ...
    def set_heading(self, heading: str) -> None: ...

class AppChooserWidget(Widget, Accessible, AppChooser, Buildable, ConstraintTarget):
    class Props:
        default_text: str
        show_all: bool
        show_default: bool
        show_fallback: bool
        show_other: bool
        show_recommended: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        content_type: str
    props: Props = ...
    def __init__(
        self,
        default_text: str = ...,
        show_all: bool = ...,
        show_default: bool = ...,
        show_fallback: bool = ...,
        show_other: bool = ...,
        show_recommended: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        content_type: str = ...,
    ): ...
    def get_default_text(self) -> Optional[str]: ...
    def get_show_all(self) -> bool: ...
    def get_show_default(self) -> bool: ...
    def get_show_fallback(self) -> bool: ...
    def get_show_other(self) -> bool: ...
    def get_show_recommended(self) -> bool: ...
    @classmethod
    def new(cls, content_type: str) -> AppChooserWidget: ...
    def set_default_text(self, text: str) -> None: ...
    def set_show_all(self, setting: bool) -> None: ...
    def set_show_default(self, setting: bool) -> None: ...
    def set_show_fallback(self, setting: bool) -> None: ...
    def set_show_other(self, setting: bool) -> None: ...
    def set_show_recommended(self, setting: bool) -> None: ...

class Application(Gio.Application, Gio.ActionGroup, Gio.ActionMap):
    class Props:
        active_window: Window
        menubar: Gio.MenuModel
        register_session: bool
        screensaver_active: bool
        action_group: Gio.ActionGroup
        application_id: str
        flags: Gio.ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: str
    props: Props = ...
    def __init__(
        self,
        menubar: Gio.MenuModel = ...,
        register_session: bool = ...,
        action_group: Gio.ActionGroup = ...,
        application_id: str = ...,
        flags: Gio.ApplicationFlags = ...,
        inactivity_timeout: int = ...,
        resource_base_path: str = ...,
    ): ...
    parent_instance: Gio.Application = ...
    def add_window(self, window: Window) -> None: ...
    def do_window_added(self, window: Window) -> None: ...
    def do_window_removed(self, window: Window) -> None: ...
    def get_accels_for_action(self, detailed_action_name: str) -> list[str]: ...
    def get_actions_for_accel(self, accel: str) -> list[str]: ...
    def get_active_window(self) -> Optional[Window]: ...
    def get_menu_by_id(self, id: str) -> Optional[Gio.Menu]: ...
    def get_menubar(self) -> Optional[Gio.MenuModel]: ...
    def get_window_by_id(self, id: int) -> Optional[Window]: ...
    def get_windows(self) -> list[Window]: ...
    def inhibit(
        self,
        window: Optional[Window],
        flags: ApplicationInhibitFlags,
        reason: Optional[str] = None,
    ) -> int: ...
    def list_action_descriptions(self) -> list[str]: ...
    @classmethod
    def new(
        cls, application_id: Optional[str], flags: Gio.ApplicationFlags
    ) -> Application: ...
    def remove_window(self, window: Window) -> None: ...
    def set_accels_for_action(
        self, detailed_action_name: str, accels: Sequence[str]
    ) -> None: ...
    def set_menubar(self, menubar: Optional[Gio.MenuModel] = None) -> None: ...
    def uninhibit(self, cookie: int) -> None: ...

class ApplicationClass(GObject.GPointer):
    parent_class: Gio.ApplicationClass = ...
    window_added: Callable[[Application, Window], None] = ...
    window_removed: Callable[[Application, Window], None] = ...
    padding: list[None] = ...

class ApplicationWindow(
    Window,
    Gio.ActionGroup,
    Gio.ActionMap,
    Accessible,
    Buildable,
    ConstraintTarget,
    Native,
    Root,
    ShortcutManager,
):
    class Props:
        show_menubar: bool
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        show_menubar: bool = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Window = ...
    def get_help_overlay(self) -> Optional[ShortcutsWindow]: ...
    def get_id(self) -> int: ...
    def get_show_menubar(self) -> bool: ...
    @classmethod
    def new(cls, application: Application) -> ApplicationWindow: ...
    def set_help_overlay(
        self, help_overlay: Optional[ShortcutsWindow] = None
    ) -> None: ...
    def set_show_menubar(self, show_menubar: bool) -> None: ...

class ApplicationWindowClass(GObject.GPointer):
    parent_class: WindowClass = ...
    padding: list[None] = ...

class AspectFrame(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        obey_child: bool
        ratio: float
        xalign: float
        yalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        obey_child: bool = ...,
        ratio: float = ...,
        xalign: float = ...,
        yalign: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    def get_obey_child(self) -> bool: ...
    def get_ratio(self) -> float: ...
    def get_xalign(self) -> float: ...
    def get_yalign(self) -> float: ...
    @classmethod
    def new(
        cls, xalign: float, yalign: float, ratio: float, obey_child: bool
    ) -> AspectFrame: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_obey_child(self, obey_child: bool) -> None: ...
    def set_ratio(self, ratio: float) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...

class Assistant(
    Window, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        pages: Gio.ListModel
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_action_widget(self, child: Widget) -> None: ...
    def append_page(self, page: Widget) -> int: ...
    def commit(self) -> None: ...
    def get_current_page(self) -> int: ...
    def get_n_pages(self) -> int: ...
    def get_nth_page(self, page_num: int) -> Optional[Widget]: ...
    def get_page(self, child: Widget) -> AssistantPage: ...
    def get_page_complete(self, page: Widget) -> bool: ...
    def get_page_title(self, page: Widget) -> str: ...
    def get_page_type(self, page: Widget) -> AssistantPageType: ...
    def get_pages(self) -> Gio.ListModel: ...
    def insert_page(self, page: Widget, position: int) -> int: ...
    @classmethod
    def new(cls) -> Assistant: ...
    def next_page(self) -> None: ...
    def prepend_page(self, page: Widget) -> int: ...
    def previous_page(self) -> None: ...
    def remove_action_widget(self, child: Widget) -> None: ...
    def remove_page(self, page_num: int) -> None: ...
    def set_current_page(self, page_num: int) -> None: ...
    def set_forward_page_func(
        self, page_func: Optional[Callable[..., int]] = None, *data: Any
    ) -> None: ...
    def set_page_complete(self, page: Widget, complete: bool) -> None: ...
    def set_page_title(self, page: Widget, title: str) -> None: ...
    def set_page_type(self, page: Widget, type: AssistantPageType) -> None: ...
    def update_buttons_state(self) -> None: ...

class AssistantPage(GObject.Object):
    class Props:
        child: Widget
        complete: bool
        page_type: AssistantPageType
        title: str
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        complete: bool = ...,
        page_type: AssistantPageType = ...,
        title: str = ...,
    ): ...
    def get_child(self) -> Widget: ...

class BinLayout(LayoutManager):
    @classmethod
    def new(cls) -> BinLayout: ...

class BinLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class Bitset(GObject.GBoxed):
    def add(self, value: int) -> bool: ...
    def add_range(self, start: int, n_items: int) -> None: ...
    def add_range_closed(self, first: int, last: int) -> None: ...
    def add_rectangle(
        self, start: int, width: int, height: int, stride: int
    ) -> None: ...
    def contains(self, value: int) -> bool: ...
    def copy(self) -> Bitset: ...
    def difference(self, other: Bitset) -> None: ...
    def equals(self, other: Bitset) -> bool: ...
    def get_maximum(self) -> int: ...
    def get_minimum(self) -> int: ...
    def get_nth(self, nth: int) -> int: ...
    def get_size(self) -> int: ...
    def get_size_in_range(self, first: int, last: int) -> int: ...
    def intersect(self, other: Bitset) -> None: ...
    def is_empty(self) -> bool: ...
    @classmethod
    def new_empty(cls) -> Bitset: ...
    @classmethod
    def new_range(cls, start: int, n_items: int) -> Bitset: ...
    def ref(self) -> Bitset: ...
    def remove(self, value: int) -> bool: ...
    def remove_all(self) -> None: ...
    def remove_range(self, start: int, n_items: int) -> None: ...
    def remove_range_closed(self, first: int, last: int) -> None: ...
    def remove_rectangle(
        self, start: int, width: int, height: int, stride: int
    ) -> None: ...
    def shift_left(self, amount: int) -> None: ...
    def shift_right(self, amount: int) -> None: ...
    def splice(self, position: int, removed: int, added: int) -> None: ...
    def subtract(self, other: Bitset) -> None: ...
    def union(self, other: Bitset) -> None: ...
    def unref(self) -> None: ...

class BitsetIter(GObject.GBoxed):
    private_data: list[None] = ...
    def get_value(self) -> int: ...
    @staticmethod
    def init_at(set: Bitset, target: int) -> Tuple[bool, BitsetIter, int]: ...
    @staticmethod
    def init_first(set: Bitset) -> Tuple[bool, BitsetIter, int]: ...
    @staticmethod
    def init_last(set: Bitset) -> Tuple[bool, BitsetIter, int]: ...
    def is_valid(self) -> bool: ...
    def next(self) -> Tuple[bool, int]: ...
    def previous(self) -> Tuple[bool, int]: ...

class BookmarkList(GObject.Object, Gio.ListModel):
    class Props:
        attributes: str
        filename: str
        io_priority: int
        item_type: Type
        loading: bool
        n_items: int
    props: Props = ...
    def __init__(
        self, attributes: str = ..., filename: str = ..., io_priority: int = ...
    ): ...
    def get_attributes(self) -> Optional[str]: ...
    def get_filename(self) -> str: ...
    def get_io_priority(self) -> int: ...
    def is_loading(self) -> bool: ...
    @classmethod
    def new(
        cls, filename: Optional[str] = None, attributes: Optional[str] = None
    ) -> BookmarkList: ...
    def set_attributes(self, attributes: Optional[str] = None) -> None: ...
    def set_io_priority(self, io_priority: int) -> None: ...

class BookmarkListClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class BoolFilter(Filter):
    class Props:
        expression: Expression
        invert: bool
    props: Props = ...
    def __init__(self, expression: Expression = ..., invert: bool = ...): ...
    def get_expression(self) -> Optional[Expression]: ...
    def get_invert(self) -> bool: ...
    @classmethod
    def new(cls, expression: Optional[Expression] = None) -> BoolFilter: ...
    def set_expression(self, expression: Optional[Expression] = None) -> None: ...
    def set_invert(self, invert: bool) -> None: ...

class BoolFilterClass(GObject.GPointer):
    parent_class: FilterClass = ...

class Border(GObject.GBoxed):
    left: int = ...
    right: int = ...
    top: int = ...
    bottom: int = ...
    def copy(self) -> Border: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> Border: ...

class Box(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        baseline_position: BaselinePosition
        homogeneous: bool
        spacing: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        baseline_position: BaselinePosition = ...,
        homogeneous: bool = ...,
        spacing: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    parent_instance: Widget = ...
    def append(self, child: Widget) -> None: ...
    def get_baseline_position(self) -> BaselinePosition: ...
    def get_homogeneous(self) -> bool: ...
    def get_spacing(self) -> int: ...
    def insert_child_after(
        self, child: Widget, sibling: Optional[Widget] = None
    ) -> None: ...
    @classmethod
    def new(cls, orientation: Orientation, spacing: int) -> Box: ...
    def prepend(self, child: Widget) -> None: ...
    def remove(self, child: Widget) -> None: ...
    def reorder_child_after(
        self, child: Widget, sibling: Optional[Widget] = None
    ) -> None: ...
    def set_baseline_position(self, position: BaselinePosition) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class BoxClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    padding: list[None] = ...

class BoxLayout(LayoutManager, Orientable):
    class Props:
        baseline_position: BaselinePosition
        homogeneous: bool
        spacing: int
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        baseline_position: BaselinePosition = ...,
        homogeneous: bool = ...,
        spacing: int = ...,
        orientation: Orientation = ...,
    ): ...
    def get_baseline_position(self) -> BaselinePosition: ...
    def get_homogeneous(self) -> bool: ...
    def get_spacing(self) -> int: ...
    @classmethod
    def new(cls, orientation: Orientation) -> BoxLayout: ...
    def set_baseline_position(self, position: BaselinePosition) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class BoxLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class Buildable(GObject.Object):
    def get_buildable_id(self) -> Optional[str]: ...

class BuildableIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    set_id: Callable[[Buildable, str], None] = ...
    get_id: Callable[[Buildable], str] = ...
    add_child: Callable[[Buildable, Builder, GObject.Object, Optional[str]], None] = ...
    set_buildable_property: Callable[[Buildable, Builder, str, Any], None] = ...
    construct_child: None = ...
    custom_tag_start: Callable[
        [Buildable, Builder, Optional[GObject.Object], str],
        Tuple[bool, BuildableParser, None],
    ] = ...
    custom_tag_end: Callable[
        [Buildable, Builder, Optional[GObject.Object], str, None], None
    ] = ...
    custom_finished: Callable[
        [Buildable, Builder, Optional[GObject.Object], str, None], None
    ] = ...
    parser_finished: Callable[[Buildable, Builder], None] = ...
    get_internal_child: Callable[[Buildable, Builder, str], GObject.Object] = ...

class BuildableParseContext(GObject.GPointer):
    def get_element(self) -> Optional[str]: ...
    def get_element_stack(self) -> list[str]: ...
    def get_position(self) -> Tuple[int, int]: ...
    def pop(self) -> None: ...
    def push(self, parser: BuildableParser, user_data: None) -> None: ...

class BuildableParser(GObject.GPointer):
    start_element: Callable[..., None] = ...
    end_element: Callable[..., None] = ...
    text: Callable[..., None] = ...
    error: Callable[..., None] = ...
    padding: list[None] = ...

class Builder(GObject.Object):
    class Props:
        current_object: GObject.Object
        scope: BuilderScope
        translation_domain: str
    props: Props = ...
    def __init__(
        self,
        current_object: GObject.Object = ...,
        scope: BuilderScope = ...,
        translation_domain: str = ...,
    ): ...
    def add_from_file(self, filename: str) -> bool: ...
    def add_from_resource(self, resource_path: str) -> bool: ...
    def add_from_string(self, *args, **kwargs): ...  # FIXME Method
    def add_objects_from_file(
        self, filename: str, object_ids: Sequence[str]
    ) -> bool: ...
    def add_objects_from_resource(
        self, resource_path: str, object_ids: Sequence[str]
    ) -> bool: ...
    def add_objects_from_string(self, *args, **kwargs): ...  # FIXME Method
    def create_closure(
        self,
        function_name: str,
        flags: BuilderClosureFlags,
        object: Optional[GObject.Object] = None,
    ) -> Optional[Callable[..., Any]]: ...
    def define_builder_scope(self, *args, **kwargs): ...  # FIXME Method
    def expose_object(self, name: str, object: GObject.Object) -> None: ...
    def extend_with_template(
        self, object: GObject.Object, template_type: Type, buffer: str, length: int
    ) -> bool: ...
    def get_current_object(self) -> Optional[GObject.Object]: ...
    def get_object(self, name: str) -> Optional[GObject.Object]: ...
    def get_objects(self) -> list[GObject.Object]: ...
    def get_scope(self) -> BuilderScope: ...
    def get_translation_domain(self) -> Optional[str]: ...
    def get_type_from_name(self, type_name: str) -> Type: ...
    @classmethod
    def new(cls) -> Builder: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Builder: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> Builder: ...
    @classmethod
    def new_from_string(cls, string: str, length: int) -> Builder: ...
    def set_current_object(
        self, current_object: Optional[GObject.Object] = None
    ) -> None: ...
    def set_scope(self, scope: Optional[BuilderScope] = None) -> None: ...
    def set_translation_domain(self, domain: Optional[str] = None) -> None: ...
    def value_from_string(
        self, pspec: GObject.ParamSpec, string: str
    ) -> Tuple[bool, Any]: ...
    def value_from_string_type(self, type: Type, string: str) -> Tuple[bool, Any]: ...

    class BuilderScope:
        g_type_instance: GObject.TypeInstance = ...
        ref_count: int = ...
        qdata: GLib.Data = ...
        def bind_property(self, *args, **kwargs): ...  # FIXME Method
        def bind_property_full(self, *args, **kwargs): ...  # FIXME Method
        def compat_control(self, *args, **kwargs): ...  # FIXME Method
        def do_create_closure(self, *args, **kwargs): ...  # FIXME Method
        def force_floating(self, *args, **kwargs): ...  # FIXME Method
        def freeze_notify(self, *args, **kwargs): ...  # FIXME Method
        def get_data(self, *args, **kwargs): ...  # FIXME Method
        def get_property(self, *args, **kwargs): ...  # FIXME Method
        def get_qdata(self, *args, **kwargs): ...  # FIXME Method
        def getv(
            self, n_properties: int, names: Sequence[str], values: Sequence[Any]
        ) -> None: ...
        def interface_find_property(self, *args, **kwargs): ...  # FIXME Method
        def interface_install_property(self, *args, **kwargs): ...  # FIXME Method
        def interface_list_properties(self, *args, **kwargs): ...  # FIXME Method
        def is_floating(self) -> bool: ...
        @classmethod
        def newv(
            cls,
            object_type: Type,
            n_parameters: int,
            parameters: Sequence[GObject.Parameter],
        ) -> Object: ...
        def notify(self, property_name: str) -> None: ...
        def notify_by_pspec(self, *args, **kwargs): ...  # FIXME Method
        def ref(self, *args, **kwargs): ...  # FIXME Method
        def ref_sink(self, *args, **kwargs): ...  # FIXME Method
        def run_dispose(self) -> None: ...
        def set_data(self, *args, **kwargs): ...  # FIXME Method
        def set_property(self, *args, **kwargs): ...  # FIXME Method
        def steal_data(self, *args, **kwargs): ...  # FIXME Method
        def steal_qdata(self, *args, **kwargs): ...  # FIXME Method
        def thaw_notify(self) -> None: ...
        def unref(self, *args, **kwargs): ...  # FIXME Method
        def watch_closure(self, *args, **kwargs): ...  # FIXME Method

class BuilderCScope(GObject.Object, BuilderScope):
    parent_instance: GObject.Object = ...
    def add_callback_symbol(
        self, callback_name: str, callback_symbol: Callable[[], None]
    ) -> None: ...
    @classmethod
    def new(cls) -> BuilderCScope: ...

class BuilderCScopeClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class BuilderClass(GObject.GPointer): ...

class BuilderListItemFactory(ListItemFactory):
    class Props:
        bytes: GLib.Bytes
        resource: str
        scope: BuilderScope
    props: Props = ...
    def __init__(
        self, bytes: GLib.Bytes = ..., resource: str = ..., scope: BuilderScope = ...
    ): ...
    def get_bytes(self) -> GLib.Bytes: ...
    def get_resource(self) -> Optional[str]: ...
    def get_scope(self) -> Optional[BuilderScope]: ...
    @classmethod
    def new_from_bytes(
        cls, scope: Optional[BuilderScope], bytes: GLib.Bytes
    ) -> BuilderListItemFactory: ...
    @classmethod
    def new_from_resource(
        cls, scope: Optional[BuilderScope], resource_path: str
    ) -> BuilderListItemFactory: ...

class BuilderListItemFactoryClass(GObject.GPointer): ...
class BuilderScope(GObject.Object): ...

class BuilderScopeInterface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    get_type_from_name: Callable[[BuilderScope, Builder, str], Type] = ...
    get_type_from_function: Callable[[BuilderScope, Builder, str], Type] = ...
    create_closure: Callable[
        [BuilderScope, Builder, str, BuilderClosureFlags, GObject.Object],
        Callable[..., Any],
    ] = ...

class Button(Widget, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        has_frame: bool
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    parent_instance: Widget = ...
    def do_activate(self) -> None: ...
    def do_clicked(self) -> None: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_has_frame(self) -> bool: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_label(self) -> Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> Button: ...
    @classmethod
    def new_from_icon_name(cls, icon_name: Optional[str] = None) -> Button: ...
    @classmethod
    def new_with_label(cls, label: str) -> Button: ...
    @classmethod
    def new_with_mnemonic(cls, label: str) -> Button: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_has_frame(self, has_frame: bool) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class ButtonClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    clicked: Callable[[Button], None] = ...
    activate: Callable[[Button], None] = ...
    padding: list[None] = ...

class ButtonPrivate(GObject.GPointer): ...

class CClosureExpression(Expression):
    @classmethod
    def new(
        cls,
        value_type: Type,
        marshal: Optional[Callable[..., None]],
        n_params: int,
        params: Sequence[Expression],
        callback_func: Callable[[], None],
        *user_data: Any,
    ) -> CClosureExpression: ...

class Calendar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        day: int
        month: int
        show_day_names: bool
        show_heading: bool
        show_week_numbers: bool
        year: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        day: int = ...,
        month: int = ...,
        show_day_names: bool = ...,
        show_heading: bool = ...,
        show_week_numbers: bool = ...,
        year: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def clear_marks(self) -> None: ...
    def get_date(self) -> GLib.DateTime: ...
    def get_day_is_marked(self, day: int) -> bool: ...
    def get_show_day_names(self) -> bool: ...
    def get_show_heading(self) -> bool: ...
    def get_show_week_numbers(self) -> bool: ...
    def mark_day(self, day: int) -> None: ...
    @classmethod
    def new(cls) -> Calendar: ...
    def select_day(self, date: GLib.DateTime) -> None: ...
    def set_show_day_names(self, value: bool) -> None: ...
    def set_show_heading(self, value: bool) -> None: ...
    def set_show_week_numbers(self, value: bool) -> None: ...
    def unmark_day(self, day: int) -> None: ...

class CallbackAction(ShortcutAction):
    @classmethod
    def new(
        cls, callback: Optional[Callable[..., bool]] = None, *data: Any
    ) -> CallbackAction: ...

class CallbackActionClass(GObject.GPointer): ...

class CellArea(GObject.InitiallyUnowned, Buildable, CellLayout):
    class Props:
        edit_widget: CellEditable
        edited_cell: CellRenderer
        focus_cell: CellRenderer
    props: Props = ...
    def __init__(self, focus_cell: CellRenderer = ...): ...
    parent_instance: GObject.InitiallyUnowned = ...
    def activate(
        self,
        context: CellAreaContext,
        widget: Widget,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
        edit_only: bool,
    ) -> bool: ...
    def activate_cell(
        self,
        widget: Widget,
        renderer: CellRenderer,
        event: Gdk.Event,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> bool: ...
    def add(self, renderer: CellRenderer) -> None: ...
    def add_focus_sibling(
        self, renderer: CellRenderer, sibling: CellRenderer
    ) -> None: ...
    def apply_attributes(
        self,
        tree_model: TreeModel,
        iter: TreeIter,
        is_expander: bool,
        is_expanded: bool,
    ) -> None: ...
    def attribute_connect(
        self, renderer: CellRenderer, attribute: str, column: int
    ) -> None: ...
    def attribute_disconnect(self, renderer: CellRenderer, attribute: str) -> None: ...
    def attribute_get_column(self, renderer: CellRenderer, attribute: str) -> int: ...
    def cell_get_property(
        self, renderer: CellRenderer, property_name: str, value: Any
    ) -> None: ...
    def cell_set_property(
        self, renderer: CellRenderer, property_name: str, value: Any
    ) -> None: ...
    def copy_context(self, context: CellAreaContext) -> CellAreaContext: ...
    def create_context(self) -> CellAreaContext: ...
    def do_activate(
        self,
        context: CellAreaContext,
        widget: Widget,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
        edit_only: bool,
    ) -> bool: ...
    def do_add(self, renderer: CellRenderer) -> None: ...
    def do_apply_attributes(
        self,
        tree_model: TreeModel,
        iter: TreeIter,
        is_expander: bool,
        is_expanded: bool,
    ) -> None: ...
    def do_copy_context(self, context: CellAreaContext) -> CellAreaContext: ...
    def do_create_context(self) -> CellAreaContext: ...
    def do_event(
        self,
        context: CellAreaContext,
        widget: Widget,
        event: Gdk.Event,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> int: ...
    def do_focus(self, direction: DirectionType) -> bool: ...
    def do_foreach(
        self, callback: Callable[..., bool], *callback_data: Any
    ) -> None: ...
    def do_foreach_alloc(
        self,
        context: CellAreaContext,
        widget: Widget,
        cell_area: Gdk.Rectangle,
        background_area: Gdk.Rectangle,
        callback: Callable[..., bool],
        *callback_data: Any,
    ) -> None: ...
    def do_get_cell_property(
        self,
        renderer: CellRenderer,
        property_id: int,
        value: Any,
        pspec: GObject.ParamSpec,
    ) -> None: ...
    def do_get_preferred_height(
        self, context: CellAreaContext, widget: Widget
    ) -> Tuple[int, int]: ...
    def do_get_preferred_height_for_width(
        self, context: CellAreaContext, widget: Widget, width: int
    ) -> Tuple[int, int]: ...
    def do_get_preferred_width(
        self, context: CellAreaContext, widget: Widget
    ) -> Tuple[int, int]: ...
    def do_get_preferred_width_for_height(
        self, context: CellAreaContext, widget: Widget, height: int
    ) -> Tuple[int, int]: ...
    def do_get_request_mode(self) -> SizeRequestMode: ...
    def do_is_activatable(self) -> bool: ...
    def do_remove(self, renderer: CellRenderer) -> None: ...
    def do_set_cell_property(
        self,
        renderer: CellRenderer,
        property_id: int,
        value: Any,
        pspec: GObject.ParamSpec,
    ) -> None: ...
    def do_snapshot(
        self,
        context: CellAreaContext,
        widget: Widget,
        snapshot: Snapshot,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
        paint_focus: bool,
    ) -> None: ...
    def event(
        self,
        context: CellAreaContext,
        widget: Widget,
        event: Gdk.Event,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> int: ...
    def find_cell_property(self, property_name: str) -> GObject.ParamSpec: ...
    def focus(self, direction: DirectionType) -> bool: ...
    def foreach(self, callback: Callable[..., bool], *callback_data: Any) -> None: ...
    def foreach_alloc(
        self,
        context: CellAreaContext,
        widget: Widget,
        cell_area: Gdk.Rectangle,
        background_area: Gdk.Rectangle,
        callback: Callable[..., bool],
        *callback_data: Any,
    ) -> None: ...
    def get_cell_allocation(
        self,
        context: CellAreaContext,
        widget: Widget,
        renderer: CellRenderer,
        cell_area: Gdk.Rectangle,
    ) -> Gdk.Rectangle: ...
    def get_cell_at_position(
        self,
        context: CellAreaContext,
        widget: Widget,
        cell_area: Gdk.Rectangle,
        x: int,
        y: int,
    ) -> Tuple[CellRenderer, Gdk.Rectangle]: ...
    def get_current_path_string(self) -> str: ...
    def get_edit_widget(self) -> Optional[CellEditable]: ...
    def get_edited_cell(self) -> Optional[CellRenderer]: ...
    def get_focus_cell(self) -> Optional[CellRenderer]: ...
    def get_focus_from_sibling(
        self, renderer: CellRenderer
    ) -> Optional[CellRenderer]: ...
    def get_focus_siblings(self, renderer: CellRenderer) -> list[CellRenderer]: ...
    def get_preferred_height(
        self, context: CellAreaContext, widget: Widget
    ) -> Tuple[int, int]: ...
    def get_preferred_height_for_width(
        self, context: CellAreaContext, widget: Widget, width: int
    ) -> Tuple[int, int]: ...
    def get_preferred_width(
        self, context: CellAreaContext, widget: Widget
    ) -> Tuple[int, int]: ...
    def get_preferred_width_for_height(
        self, context: CellAreaContext, widget: Widget, height: int
    ) -> Tuple[int, int]: ...
    def get_request_mode(self) -> SizeRequestMode: ...
    def has_renderer(self, renderer: CellRenderer) -> bool: ...
    def inner_cell_area(
        self, widget: Widget, cell_area: Gdk.Rectangle
    ) -> Gdk.Rectangle: ...
    def install_cell_property(
        self, property_id: int, pspec: GObject.ParamSpec
    ) -> None: ...
    def is_activatable(self) -> bool: ...
    def is_focus_sibling(
        self, renderer: CellRenderer, sibling: CellRenderer
    ) -> bool: ...
    def list_cell_properties(self) -> list[GObject.ParamSpec]: ...
    def remove(self, renderer: CellRenderer) -> None: ...
    def remove_focus_sibling(
        self, renderer: CellRenderer, sibling: CellRenderer
    ) -> None: ...
    def request_renderer(
        self,
        renderer: CellRenderer,
        orientation: Orientation,
        widget: Widget,
        for_size: int,
    ) -> Tuple[int, int]: ...
    def set_focus_cell(self, renderer: Optional[CellRenderer] = None) -> None: ...
    def snapshot(
        self,
        context: CellAreaContext,
        widget: Widget,
        snapshot: Snapshot,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
        paint_focus: bool,
    ) -> None: ...
    def stop_editing(self, canceled: bool) -> None: ...

class CellAreaBox(CellArea, Buildable, CellLayout, Orientable):
    class Props:
        spacing: int
        edit_widget: CellEditable
        edited_cell: CellRenderer
        focus_cell: CellRenderer
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        spacing: int = ...,
        focus_cell: CellRenderer = ...,
        orientation: Orientation = ...,
    ): ...
    def get_spacing(self) -> int: ...
    @classmethod
    def new(cls) -> CellAreaBox: ...
    def pack_end(
        self, renderer: CellRenderer, expand: bool, align: bool, fixed: bool
    ) -> None: ...
    def pack_start(
        self, renderer: CellRenderer, expand: bool, align: bool, fixed: bool
    ) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class CellAreaClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...
    add: Callable[[CellArea, CellRenderer], None] = ...
    remove: Callable[[CellArea, CellRenderer], None] = ...
    foreach: Callable[..., None] = ...
    foreach_alloc: Callable[..., None] = ...
    event: Callable[
        [
            CellArea,
            CellAreaContext,
            Widget,
            Gdk.Event,
            Gdk.Rectangle,
            CellRendererState,
        ],
        int,
    ] = ...
    snapshot: Callable[
        [
            CellArea,
            CellAreaContext,
            Widget,
            Snapshot,
            Gdk.Rectangle,
            Gdk.Rectangle,
            CellRendererState,
            bool,
        ],
        None,
    ] = ...
    apply_attributes: Callable[[CellArea, TreeModel, TreeIter, bool, bool], None] = ...
    create_context: Callable[[CellArea], CellAreaContext] = ...
    copy_context: Callable[[CellArea, CellAreaContext], CellAreaContext] = ...
    get_request_mode: Callable[[CellArea], SizeRequestMode] = ...
    get_preferred_width: Callable[
        [CellArea, CellAreaContext, Widget], Tuple[int, int]
    ] = ...
    get_preferred_height_for_width: Callable[
        [CellArea, CellAreaContext, Widget, int], Tuple[int, int]
    ] = ...
    get_preferred_height: Callable[
        [CellArea, CellAreaContext, Widget], Tuple[int, int]
    ] = ...
    get_preferred_width_for_height: Callable[
        [CellArea, CellAreaContext, Widget, int], Tuple[int, int]
    ] = ...
    set_cell_property: Callable[
        [CellArea, CellRenderer, int, Any, GObject.ParamSpec], None
    ] = ...
    get_cell_property: Callable[
        [CellArea, CellRenderer, int, Any, GObject.ParamSpec], None
    ] = ...
    focus: Callable[[CellArea, DirectionType], bool] = ...
    is_activatable: Callable[[CellArea], bool] = ...
    activate: Callable[
        [CellArea, CellAreaContext, Widget, Gdk.Rectangle, CellRendererState, bool],
        bool,
    ] = ...
    padding: list[None] = ...
    def find_cell_property(self, property_name: str) -> GObject.ParamSpec: ...
    def install_cell_property(
        self, property_id: int, pspec: GObject.ParamSpec
    ) -> None: ...
    def list_cell_properties(self) -> list[GObject.ParamSpec]: ...

class CellAreaContext(GObject.Object):
    class Props:
        area: CellArea
        minimum_height: int
        minimum_width: int
        natural_height: int
        natural_width: int
    props: Props = ...
    def __init__(self, area: CellArea = ...): ...
    parent_instance: GObject.Object = ...
    def allocate(self, width: int, height: int) -> None: ...
    def do_allocate(self, width: int, height: int) -> None: ...
    def do_get_preferred_height_for_width(self, width: int) -> Tuple[int, int]: ...
    def do_get_preferred_width_for_height(self, height: int) -> Tuple[int, int]: ...
    def do_reset(self) -> None: ...
    def get_allocation(self) -> Tuple[int, int]: ...
    def get_area(self) -> CellArea: ...
    def get_preferred_height(self) -> Tuple[int, int]: ...
    def get_preferred_height_for_width(self, width: int) -> Tuple[int, int]: ...
    def get_preferred_width(self) -> Tuple[int, int]: ...
    def get_preferred_width_for_height(self, height: int) -> Tuple[int, int]: ...
    def push_preferred_height(
        self, minimum_height: int, natural_height: int
    ) -> None: ...
    def push_preferred_width(self, minimum_width: int, natural_width: int) -> None: ...
    def reset(self) -> None: ...

class CellAreaContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    allocate: Callable[[CellAreaContext, int, int], None] = ...
    reset: Callable[[CellAreaContext], None] = ...
    get_preferred_height_for_width: Callable[
        [CellAreaContext, int], Tuple[int, int]
    ] = ...
    get_preferred_width_for_height: Callable[
        [CellAreaContext, int], Tuple[int, int]
    ] = ...
    padding: list[None] = ...

class CellAreaContextPrivate(GObject.GPointer): ...

class CellEditable(GObject.Object):
    def editing_done(self) -> None: ...
    def remove_widget(self) -> None: ...
    def start_editing(self, event: Optional[Gdk.Event] = None) -> None: ...

class CellEditableIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    editing_done: Callable[[CellEditable], None] = ...
    remove_widget: Callable[[CellEditable], None] = ...
    start_editing: Callable[[CellEditable, Optional[Gdk.Event]], None] = ...

class CellLayout(GObject.Object):
    def add_attribute(
        self, cell: CellRenderer, attribute: str, column: int
    ) -> None: ...
    def clear(self) -> None: ...
    def clear_attributes(self, cell: CellRenderer) -> None: ...
    def get_area(self) -> Optional[CellArea]: ...
    def get_cells(self) -> list[CellRenderer]: ...
    def pack_end(self, cell: CellRenderer, expand: bool) -> None: ...
    def pack_start(self, cell: CellRenderer, expand: bool) -> None: ...
    def reorder(self, cell: CellRenderer, position: int) -> None: ...
    def set_cell_data_func(
        self,
        cell: CellRenderer,
        func: Optional[Callable[..., None]] = None,
        *func_data: Any,
    ) -> None: ...

class CellLayoutIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    pack_start: Callable[[CellLayout, CellRenderer, bool], None] = ...
    pack_end: Callable[[CellLayout, CellRenderer, bool], None] = ...
    clear: Callable[[CellLayout], None] = ...
    add_attribute: Callable[[CellLayout, CellRenderer, str, int], None] = ...
    set_cell_data_func: Callable[..., None] = ...
    clear_attributes: Callable[[CellLayout, CellRenderer], None] = ...
    reorder: Callable[[CellLayout, CellRenderer, int], None] = ...
    get_cells: Callable[[CellLayout], list[CellRenderer]] = ...
    get_area: Callable[[CellLayout], Optional[CellArea]] = ...

class CellRenderer(GObject.InitiallyUnowned):
    class Props:
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    parent_instance: GObject.InitiallyUnowned = ...
    priv: CellRendererPrivate = ...
    def activate(
        self,
        event: Gdk.Event,
        widget: Widget,
        path: str,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> bool: ...
    def do_activate(
        self,
        event: Gdk.Event,
        widget: Widget,
        path: str,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> bool: ...
    def do_editing_canceled(self) -> None: ...
    def do_editing_started(self, editable: CellEditable, path: str) -> None: ...
    def do_get_aligned_area(
        self, widget: Widget, flags: CellRendererState, cell_area: Gdk.Rectangle
    ) -> Gdk.Rectangle: ...
    def do_get_preferred_height(self, widget: Widget) -> Tuple[int, int]: ...
    def do_get_preferred_height_for_width(
        self, widget: Widget, width: int
    ) -> Tuple[int, int]: ...
    def do_get_preferred_width(self, widget: Widget) -> Tuple[int, int]: ...
    def do_get_preferred_width_for_height(
        self, widget: Widget, height: int
    ) -> Tuple[int, int]: ...
    def do_get_request_mode(self) -> SizeRequestMode: ...
    def do_snapshot(
        self,
        snapshot: Snapshot,
        widget: Widget,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> None: ...
    def do_start_editing(
        self,
        event: Optional[Gdk.Event],
        widget: Widget,
        path: str,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> Optional[CellEditable]: ...
    def get_aligned_area(
        self, widget: Widget, flags: CellRendererState, cell_area: Gdk.Rectangle
    ) -> Gdk.Rectangle: ...
    def get_alignment(self) -> Tuple[float, float]: ...
    def get_fixed_size(self) -> Tuple[int, int]: ...
    def get_is_expanded(self) -> bool: ...
    def get_is_expander(self) -> bool: ...
    def get_padding(self) -> Tuple[int, int]: ...
    def get_preferred_height(self, widget: Widget) -> Tuple[int, int]: ...
    def get_preferred_height_for_width(
        self, widget: Widget, width: int
    ) -> Tuple[int, int]: ...
    def get_preferred_size(self, widget: Widget) -> Tuple[Requisition, Requisition]: ...
    def get_preferred_width(self, widget: Widget) -> Tuple[int, int]: ...
    def get_preferred_width_for_height(
        self, widget: Widget, height: int
    ) -> Tuple[int, int]: ...
    def get_request_mode(self) -> SizeRequestMode: ...
    def get_sensitive(self) -> bool: ...
    def get_state(
        self, widget: Optional[Widget], cell_state: CellRendererState
    ) -> StateFlags: ...
    def get_visible(self) -> bool: ...
    def is_activatable(self) -> bool: ...
    def set_alignment(self, xalign: float, yalign: float) -> None: ...
    def set_fixed_size(self, width: int, height: int) -> None: ...
    def set_is_expanded(self, is_expanded: bool) -> None: ...
    def set_is_expander(self, is_expander: bool) -> None: ...
    def set_padding(self, xpad: int, ypad: int) -> None: ...
    def set_sensitive(self, sensitive: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def snapshot(
        self,
        snapshot: Snapshot,
        widget: Widget,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> None: ...
    def start_editing(
        self,
        event: Optional[Gdk.Event],
        widget: Widget,
        path: str,
        background_area: Gdk.Rectangle,
        cell_area: Gdk.Rectangle,
        flags: CellRendererState,
    ) -> Optional[CellEditable]: ...
    def stop_editing(self, canceled: bool) -> None: ...

class CellRendererAccel(CellRendererText):
    class Props:
        accel_key: int
        accel_mode: CellRendererAccelMode
        accel_mods: Gdk.ModifierType
        keycode: int
        align_set: bool
        alignment: Pango.Alignment
        attributes: Pango.AttrList
        background: str
        background_rgba: Gdk.RGBA
        background_set: bool
        editable: bool
        editable_set: bool
        ellipsize: Pango.EllipsizeMode
        ellipsize_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        foreground: str
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        language: str
        language_set: bool
        markup: str
        max_width_chars: int
        placeholder_text: str
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        single_paragraph_mode: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        text: str
        underline: Pango.Underline
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        width_chars: int
        wrap_mode: Pango.WrapMode
        wrap_width: int
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        accel_key: int = ...,
        accel_mode: CellRendererAccelMode = ...,
        accel_mods: Gdk.ModifierType = ...,
        keycode: int = ...,
        align_set: bool = ...,
        alignment: Pango.Alignment = ...,
        attributes: Pango.AttrList = ...,
        background: str = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        ellipsize: Pango.EllipsizeMode = ...,
        ellipsize_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        foreground: str = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        markup: str = ...,
        max_width_chars: int = ...,
        placeholder_text: str = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        single_paragraph_mode: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        text: str = ...,
        underline: Pango.Underline = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        width_chars: int = ...,
        wrap_mode: Pango.WrapMode = ...,
        wrap_width: int = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    @classmethod
    def new(cls) -> CellRendererAccel: ...

class CellRendererClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...
    get_request_mode: Callable[[CellRenderer], SizeRequestMode] = ...
    get_preferred_width: Callable[[CellRenderer, Widget], Tuple[int, int]] = ...
    get_preferred_height_for_width: Callable[
        [CellRenderer, Widget, int], Tuple[int, int]
    ] = ...
    get_preferred_height: Callable[[CellRenderer, Widget], Tuple[int, int]] = ...
    get_preferred_width_for_height: Callable[
        [CellRenderer, Widget, int], Tuple[int, int]
    ] = ...
    get_aligned_area: Callable[
        [CellRenderer, Widget, CellRendererState, Gdk.Rectangle], Gdk.Rectangle
    ] = ...
    snapshot: Callable[
        [
            CellRenderer,
            Snapshot,
            Widget,
            Gdk.Rectangle,
            Gdk.Rectangle,
            CellRendererState,
        ],
        None,
    ] = ...
    activate: Callable[
        [
            CellRenderer,
            Gdk.Event,
            Widget,
            str,
            Gdk.Rectangle,
            Gdk.Rectangle,
            CellRendererState,
        ],
        bool,
    ] = ...
    start_editing: Callable[
        [
            CellRenderer,
            Optional[Gdk.Event],
            Widget,
            str,
            Gdk.Rectangle,
            Gdk.Rectangle,
            CellRendererState,
        ],
        Optional[CellEditable],
    ] = ...
    editing_canceled: Callable[[CellRenderer], None] = ...
    editing_started: Callable[[CellRenderer, CellEditable, str], None] = ...
    padding: list[None] = ...

class CellRendererClassPrivate(GObject.GPointer): ...

class CellRendererCombo(CellRendererText):
    class Props:
        has_entry: bool
        model: TreeModel
        text_column: int
        align_set: bool
        alignment: Pango.Alignment
        attributes: Pango.AttrList
        background: str
        background_rgba: Gdk.RGBA
        background_set: bool
        editable: bool
        editable_set: bool
        ellipsize: Pango.EllipsizeMode
        ellipsize_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        foreground: str
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        language: str
        language_set: bool
        markup: str
        max_width_chars: int
        placeholder_text: str
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        single_paragraph_mode: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        text: str
        underline: Pango.Underline
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        width_chars: int
        wrap_mode: Pango.WrapMode
        wrap_width: int
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        has_entry: bool = ...,
        model: TreeModel = ...,
        text_column: int = ...,
        align_set: bool = ...,
        alignment: Pango.Alignment = ...,
        attributes: Pango.AttrList = ...,
        background: str = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        ellipsize: Pango.EllipsizeMode = ...,
        ellipsize_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        foreground: str = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        markup: str = ...,
        max_width_chars: int = ...,
        placeholder_text: str = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        single_paragraph_mode: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        text: str = ...,
        underline: Pango.Underline = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        width_chars: int = ...,
        wrap_mode: Pango.WrapMode = ...,
        wrap_width: int = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    @classmethod
    def new(cls) -> CellRendererCombo: ...

class CellRendererPixbuf(CellRenderer):
    class Props:
        gicon: Gio.Icon
        icon_name: str
        icon_size: IconSize
        pixbuf: GdkPixbuf.Pixbuf
        pixbuf_expander_closed: GdkPixbuf.Pixbuf
        pixbuf_expander_open: GdkPixbuf.Pixbuf
        texture: Gdk.Texture
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        icon_size: IconSize = ...,
        pixbuf: GdkPixbuf.Pixbuf = ...,
        pixbuf_expander_closed: GdkPixbuf.Pixbuf = ...,
        pixbuf_expander_open: GdkPixbuf.Pixbuf = ...,
        texture: Gdk.Texture = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    @classmethod
    def new(cls) -> CellRendererPixbuf: ...

class CellRendererPrivate(GObject.GPointer): ...

class CellRendererProgress(CellRenderer, Orientable):
    class Props:
        inverted: bool
        pulse: int
        text: str
        text_xalign: float
        text_yalign: float
        value: int
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        inverted: bool = ...,
        pulse: int = ...,
        text: str = ...,
        text_xalign: float = ...,
        text_yalign: float = ...,
        value: int = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
        orientation: Orientation = ...,
    ): ...
    @classmethod
    def new(cls) -> CellRendererProgress: ...

class CellRendererSpin(CellRendererText):
    class Props:
        adjustment: Adjustment
        climb_rate: float
        digits: int
        align_set: bool
        alignment: Pango.Alignment
        attributes: Pango.AttrList
        background: str
        background_rgba: Gdk.RGBA
        background_set: bool
        editable: bool
        editable_set: bool
        ellipsize: Pango.EllipsizeMode
        ellipsize_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        foreground: str
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        language: str
        language_set: bool
        markup: str
        max_width_chars: int
        placeholder_text: str
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        single_paragraph_mode: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        text: str
        underline: Pango.Underline
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        width_chars: int
        wrap_mode: Pango.WrapMode
        wrap_width: int
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        adjustment: Adjustment = ...,
        climb_rate: float = ...,
        digits: int = ...,
        align_set: bool = ...,
        alignment: Pango.Alignment = ...,
        attributes: Pango.AttrList = ...,
        background: str = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        ellipsize: Pango.EllipsizeMode = ...,
        ellipsize_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        foreground: str = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        markup: str = ...,
        max_width_chars: int = ...,
        placeholder_text: str = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        single_paragraph_mode: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        text: str = ...,
        underline: Pango.Underline = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        width_chars: int = ...,
        wrap_mode: Pango.WrapMode = ...,
        wrap_width: int = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    @classmethod
    def new(cls) -> CellRendererSpin: ...

class CellRendererSpinner(CellRenderer):
    class Props:
        active: bool
        pulse: int
        size: IconSize
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        active: bool = ...,
        pulse: int = ...,
        size: IconSize = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    @classmethod
    def new(cls) -> CellRendererSpinner: ...

class CellRendererText(CellRenderer):
    class Props:
        align_set: bool
        alignment: Pango.Alignment
        attributes: Pango.AttrList
        background: str
        background_rgba: Gdk.RGBA
        background_set: bool
        editable: bool
        editable_set: bool
        ellipsize: Pango.EllipsizeMode
        ellipsize_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        foreground: str
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        language: str
        language_set: bool
        markup: str
        max_width_chars: int
        placeholder_text: str
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        single_paragraph_mode: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        text: str
        underline: Pango.Underline
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        width_chars: int
        wrap_mode: Pango.WrapMode
        wrap_width: int
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        align_set: bool = ...,
        alignment: Pango.Alignment = ...,
        attributes: Pango.AttrList = ...,
        background: str = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        ellipsize: Pango.EllipsizeMode = ...,
        ellipsize_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        foreground: str = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        markup: str = ...,
        max_width_chars: int = ...,
        placeholder_text: str = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        single_paragraph_mode: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        text: str = ...,
        underline: Pango.Underline = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        width_chars: int = ...,
        wrap_mode: Pango.WrapMode = ...,
        wrap_width: int = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    parent: CellRenderer = ...
    def do_edited(self, path: str, new_text: str) -> None: ...
    @classmethod
    def new(cls) -> CellRendererText: ...
    def set_fixed_height_from_font(self, number_of_rows: int) -> None: ...

class CellRendererTextClass(GObject.GPointer):
    parent_class: CellRendererClass = ...
    edited: Callable[[CellRendererText, str, str], None] = ...
    padding: list[None] = ...

class CellRendererToggle(CellRenderer):
    class Props:
        activatable: bool
        active: bool
        inconsistent: bool
        radio: bool
        cell_background: str
        cell_background_rgba: Gdk.RGBA
        cell_background_set: bool
        editing: bool
        height: int
        is_expanded: bool
        is_expander: bool
        mode: CellRendererMode
        sensitive: bool
        visible: bool
        width: int
        xalign: float
        xpad: int
        yalign: float
        ypad: int
    props: Props = ...
    def __init__(
        self,
        activatable: bool = ...,
        active: bool = ...,
        inconsistent: bool = ...,
        radio: bool = ...,
        cell_background: str = ...,
        cell_background_rgba: Gdk.RGBA = ...,
        cell_background_set: bool = ...,
        height: int = ...,
        is_expanded: bool = ...,
        is_expander: bool = ...,
        mode: CellRendererMode = ...,
        sensitive: bool = ...,
        visible: bool = ...,
        width: int = ...,
        xalign: float = ...,
        xpad: int = ...,
        yalign: float = ...,
        ypad: int = ...,
    ): ...
    def get_activatable(self) -> bool: ...
    def get_active(self) -> bool: ...
    def get_radio(self) -> bool: ...
    @classmethod
    def new(cls) -> CellRendererToggle: ...
    def set_activatable(self, setting: bool) -> None: ...
    def set_active(self, setting: bool) -> None: ...
    def set_radio(self, radio: bool) -> None: ...

class CellView(Widget, Accessible, Buildable, CellLayout, ConstraintTarget, Orientable):
    class Props:
        cell_area: CellArea
        cell_area_context: CellAreaContext
        draw_sensitive: bool
        fit_model: bool
        model: TreeModel
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        cell_area: CellArea = ...,
        cell_area_context: CellAreaContext = ...,
        draw_sensitive: bool = ...,
        fit_model: bool = ...,
        model: TreeModel = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def get_displayed_row(self) -> Optional[TreePath]: ...
    def get_draw_sensitive(self) -> bool: ...
    def get_fit_model(self) -> bool: ...
    def get_model(self) -> Optional[TreeModel]: ...
    @classmethod
    def new(cls) -> CellView: ...
    @classmethod
    def new_with_context(cls, area: CellArea, context: CellAreaContext) -> CellView: ...
    @classmethod
    def new_with_markup(cls, markup: str) -> CellView: ...
    @classmethod
    def new_with_text(cls, text: str) -> CellView: ...
    @classmethod
    def new_with_texture(cls, texture: Gdk.Texture) -> CellView: ...
    def set_displayed_row(self, path: Optional[TreePath] = None) -> None: ...
    def set_draw_sensitive(self, draw_sensitive: bool) -> None: ...
    def set_fit_model(self, fit_model: bool) -> None: ...
    def set_model(self, model: Optional[TreeModel] = None) -> None: ...

class CenterBox(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        baseline_position: BaselinePosition
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        baseline_position: BaselinePosition = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def get_baseline_position(self) -> BaselinePosition: ...
    def get_center_widget(self) -> Optional[Widget]: ...
    def get_end_widget(self) -> Optional[Widget]: ...
    def get_start_widget(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls) -> CenterBox: ...
    def set_baseline_position(self, position: BaselinePosition) -> None: ...
    def set_center_widget(self, child: Optional[Widget] = None) -> None: ...
    def set_end_widget(self, child: Optional[Widget] = None) -> None: ...
    def set_start_widget(self, child: Optional[Widget] = None) -> None: ...

class CenterBoxClass(GObject.GPointer): ...

class CenterLayout(LayoutManager):
    def get_baseline_position(self) -> BaselinePosition: ...
    def get_center_widget(self) -> Optional[Widget]: ...
    def get_end_widget(self) -> Optional[Widget]: ...
    def get_orientation(self) -> Orientation: ...
    def get_start_widget(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls) -> CenterLayout: ...
    def set_baseline_position(self, baseline_position: BaselinePosition) -> None: ...
    def set_center_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_end_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_orientation(self, orientation: Orientation) -> None: ...
    def set_start_widget(self, widget: Optional[Widget] = None) -> None: ...

class CenterLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class CheckButton(Widget, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        active: bool
        child: Widget
        group: CheckButton
        inconsistent: bool
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        active: bool = ...,
        child: Widget = ...,
        group: CheckButton = ...,
        inconsistent: bool = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    parent_instance: Widget = ...
    def do_activate(self) -> None: ...
    def do_toggled(self) -> None: ...
    def get_active(self) -> bool: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_inconsistent(self) -> bool: ...
    def get_label(self) -> Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> CheckButton: ...
    @classmethod
    def new_with_label(cls, label: Optional[str] = None) -> CheckButton: ...
    @classmethod
    def new_with_mnemonic(cls, label: Optional[str] = None) -> CheckButton: ...
    def set_active(self, setting: bool) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_group(self, group: Optional[CheckButton] = None) -> None: ...
    def set_inconsistent(self, inconsistent: bool) -> None: ...
    def set_label(self, label: Optional[str] = None) -> None: ...
    def set_use_underline(self, setting: bool) -> None: ...

class CheckButtonClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    toggled: Callable[[CheckButton], None] = ...
    activate: Callable[[CheckButton], None] = ...
    padding: list[None] = ...

class ClosureExpression(Expression):
    @classmethod
    def new(
        cls,
        value_type: Type,
        closure: Callable[..., Any],
        n_params: int,
        params: Optional[Sequence[Expression]] = None,
    ) -> ClosureExpression: ...

class ColorButton(Widget, Accessible, Buildable, ColorChooser, ConstraintTarget):
    class Props:
        modal: bool
        show_editor: bool
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        rgba: Gdk.RGBA
        use_alpha: bool
    props: Props = ...
    def __init__(
        self,
        modal: bool = ...,
        show_editor: bool = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        rgba: Gdk.RGBA = ...,
        use_alpha: bool = ...,
    ): ...
    def get_modal(self) -> bool: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls) -> ColorButton: ...
    @classmethod
    def new_with_rgba(cls, rgba: Gdk.RGBA) -> ColorButton: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_title(self, title: str) -> None: ...

class ColorChooser(GObject.Object):
    def add_palette(
        self,
        orientation: Orientation,
        colors_per_line: int,
        n_colors: int,
        colors: Optional[Sequence[Gdk.RGBA]] = None,
    ) -> None: ...
    def get_rgba(self) -> Gdk.RGBA: ...
    def get_use_alpha(self) -> bool: ...
    def set_rgba(self, color: Gdk.RGBA) -> None: ...
    def set_use_alpha(self, use_alpha: bool) -> None: ...

class ColorChooserDialog(
    Dialog,
    Accessible,
    Buildable,
    ColorChooser,
    ConstraintTarget,
    Native,
    Root,
    ShortcutManager,
):
    class Props:
        show_editor: bool
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        rgba: Gdk.RGBA
        use_alpha: bool
    props: Props = ...
    def __init__(
        self,
        show_editor: bool = ...,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        rgba: Gdk.RGBA = ...,
        use_alpha: bool = ...,
    ): ...
    @classmethod
    def new(
        cls, title: Optional[str] = None, parent: Optional[Window] = None
    ) -> ColorChooserDialog: ...

class ColorChooserInterface(GObject.GPointer):
    base_interface: GObject.TypeInterface = ...
    get_rgba: Callable[[ColorChooser], Gdk.RGBA] = ...
    set_rgba: Callable[[ColorChooser, Gdk.RGBA], None] = ...
    add_palette: Callable[
        [ColorChooser, Orientation, int, int, Optional[Sequence[Gdk.RGBA]]], None
    ] = ...
    color_activated: Callable[[ColorChooser, Gdk.RGBA], None] = ...
    padding: list[None] = ...

class ColorChooserWidget(Widget, Accessible, Buildable, ColorChooser, ConstraintTarget):
    class Props:
        show_editor: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        rgba: Gdk.RGBA
        use_alpha: bool
    props: Props = ...
    def __init__(
        self,
        show_editor: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        rgba: Gdk.RGBA = ...,
        use_alpha: bool = ...,
    ): ...
    @classmethod
    def new(cls) -> ColorChooserWidget: ...

class ColumnView(Widget, Accessible, Buildable, ConstraintTarget, Scrollable):
    class Props:
        columns: Gio.ListModel
        enable_rubberband: bool
        model: SelectionModel
        reorderable: bool
        show_column_separators: bool
        show_row_separators: bool
        single_click_activate: bool
        sorter: Sorter
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        enable_rubberband: bool = ...,
        model: SelectionModel = ...,
        reorderable: bool = ...,
        show_column_separators: bool = ...,
        show_row_separators: bool = ...,
        single_click_activate: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    def append_column(self, column: ColumnViewColumn) -> None: ...
    def get_columns(self) -> Gio.ListModel: ...
    def get_enable_rubberband(self) -> bool: ...
    def get_model(self) -> Optional[SelectionModel]: ...
    def get_reorderable(self) -> bool: ...
    def get_show_column_separators(self) -> bool: ...
    def get_show_row_separators(self) -> bool: ...
    def get_single_click_activate(self) -> bool: ...
    def get_sorter(self) -> Optional[Sorter]: ...
    def insert_column(self, position: int, column: ColumnViewColumn) -> None: ...
    @classmethod
    def new(cls, model: Optional[SelectionModel] = None) -> ColumnView: ...
    def remove_column(self, column: ColumnViewColumn) -> None: ...
    def set_enable_rubberband(self, enable_rubberband: bool) -> None: ...
    def set_model(self, model: Optional[SelectionModel] = None) -> None: ...
    def set_reorderable(self, reorderable: bool) -> None: ...
    def set_show_column_separators(self, show_column_separators: bool) -> None: ...
    def set_show_row_separators(self, show_row_separators: bool) -> None: ...
    def set_single_click_activate(self, single_click_activate: bool) -> None: ...
    def sort_by_column(
        self, column: Optional[ColumnViewColumn], direction: SortType
    ) -> None: ...

class ColumnViewClass(GObject.GPointer): ...

class ColumnViewColumn(GObject.Object):
    class Props:
        column_view: ColumnView
        expand: bool
        factory: ListItemFactory
        fixed_width: int
        header_menu: Gio.MenuModel
        resizable: bool
        sorter: Sorter
        title: str
        visible: bool
    props: Props = ...
    def __init__(
        self,
        expand: bool = ...,
        factory: ListItemFactory = ...,
        fixed_width: int = ...,
        header_menu: Gio.MenuModel = ...,
        resizable: bool = ...,
        sorter: Sorter = ...,
        title: str = ...,
        visible: bool = ...,
    ): ...
    def get_column_view(self) -> Optional[ColumnView]: ...
    def get_expand(self) -> bool: ...
    def get_factory(self) -> Optional[ListItemFactory]: ...
    def get_fixed_width(self) -> int: ...
    def get_header_menu(self) -> Optional[Gio.MenuModel]: ...
    def get_resizable(self) -> bool: ...
    def get_sorter(self) -> Optional[Sorter]: ...
    def get_title(self) -> Optional[str]: ...
    def get_visible(self) -> bool: ...
    @classmethod
    def new(
        cls, title: Optional[str] = None, factory: Optional[ListItemFactory] = None
    ) -> ColumnViewColumn: ...
    def set_expand(self, expand: bool) -> None: ...
    def set_factory(self, factory: Optional[ListItemFactory] = None) -> None: ...
    def set_fixed_width(self, fixed_width: int) -> None: ...
    def set_header_menu(self, menu: Optional[Gio.MenuModel] = None) -> None: ...
    def set_resizable(self, resizable: bool) -> None: ...
    def set_sorter(self, sorter: Optional[Sorter] = None) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class ColumnViewColumnClass(GObject.GPointer): ...

class ComboBox(
    Widget, Accessible, Buildable, CellEditable, CellLayout, ConstraintTarget
):
    class Props:
        active: int
        active_id: str
        button_sensitivity: SensitivityType
        child: Widget
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        editing_canceled: bool
    props: Props = ...
    def __init__(
        self,
        active: int = ...,
        active_id: str = ...,
        button_sensitivity: SensitivityType = ...,
        child: Widget = ...,
        entry_text_column: int = ...,
        has_entry: bool = ...,
        has_frame: bool = ...,
        id_column: int = ...,
        model: TreeModel = ...,
        popup_fixed_width: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editing_canceled: bool = ...,
    ): ...
    parent_instance: Widget = ...
    def do_activate(self) -> None: ...
    def do_changed(self) -> None: ...
    def do_format_entry_text(self, path: str) -> str: ...
    def get_active(self) -> int: ...
    def get_active_id(self) -> Optional[str]: ...
    def get_active_iter(self, *args, **kwargs): ...  # FIXME Method
    def get_button_sensitivity(self) -> SensitivityType: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_entry_text_column(self) -> int: ...
    def get_has_entry(self) -> bool: ...
    def get_id_column(self) -> int: ...
    def get_model(self) -> Optional[TreeModel]: ...
    def get_popup_fixed_width(self) -> bool: ...
    @classmethod
    def new(cls) -> ComboBox: ...
    @classmethod
    def new_with_entry(cls) -> ComboBox: ...
    @classmethod
    def new_with_model(cls, model: TreeModel) -> ComboBox: ...
    @classmethod
    def new_with_model_and_entry(cls, model: TreeModel) -> ComboBox: ...
    def popdown(self) -> None: ...
    def popup(self) -> None: ...
    def popup_for_device(self, device: Gdk.Device) -> None: ...
    def set_active(self, index_: int) -> None: ...
    def set_active_id(self, active_id: Optional[str] = None) -> bool: ...
    def set_active_iter(self, iter: Optional[TreeIter] = None) -> None: ...
    def set_button_sensitivity(self, sensitivity: SensitivityType) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_entry_text_column(self, text_column: int) -> None: ...
    def set_id_column(self, id_column: int) -> None: ...
    def set_model(self, model: Optional[TreeModel] = None) -> None: ...
    def set_popup_fixed_width(self, fixed: bool) -> None: ...
    def set_row_separator_func(
        self, func: Optional[Callable[..., bool]] = None, *data: Any
    ) -> None: ...

class ComboBoxClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    changed: Callable[[ComboBox], None] = ...
    format_entry_text: Callable[[ComboBox, str], str] = ...
    activate: Callable[[ComboBox], None] = ...
    padding: list[None] = ...

class ComboBoxText(
    ComboBox, Accessible, Buildable, CellEditable, CellLayout, ConstraintTarget
):
    class Props:
        active: int
        active_id: str
        button_sensitivity: SensitivityType
        child: Widget
        entry_text_column: int
        has_entry: bool
        has_frame: bool
        id_column: int
        model: TreeModel
        popup_fixed_width: bool
        popup_shown: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        editing_canceled: bool
    props: Props = ...
    def __init__(
        self,
        active: int = ...,
        active_id: str = ...,
        button_sensitivity: SensitivityType = ...,
        child: Widget = ...,
        entry_text_column: int = ...,
        has_entry: bool = ...,
        has_frame: bool = ...,
        id_column: int = ...,
        model: TreeModel = ...,
        popup_fixed_width: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editing_canceled: bool = ...,
    ): ...
    def append(self, id: Optional[str], text: str) -> None: ...
    def append_text(self, text: str) -> None: ...
    def get_active_text(self) -> Optional[str]: ...
    def insert(self, position: int, id: Optional[str], text: str) -> None: ...
    def insert_text(self, position: int, text: str) -> None: ...
    @classmethod
    def new(cls) -> ComboBoxText: ...
    @classmethod
    def new_with_entry(cls) -> ComboBoxText: ...
    def prepend(self, id: Optional[str], text: str) -> None: ...
    def prepend_text(self, text: str) -> None: ...
    def remove(self, position: int) -> None: ...
    def remove_all(self) -> None: ...

class ConstantExpression(Expression):
    def get_value(self) -> Any: ...
    @classmethod
    def new_for_value(cls, value: Any) -> ConstantExpression: ...

class Constraint(GObject.Object):
    class Props:
        constant: float
        multiplier: float
        relation: ConstraintRelation
        source: ConstraintTarget
        source_attribute: ConstraintAttribute
        strength: int
        target: ConstraintTarget
        target_attribute: ConstraintAttribute
    props: Props = ...
    def __init__(
        self,
        constant: float = ...,
        multiplier: float = ...,
        relation: ConstraintRelation = ...,
        source: ConstraintTarget = ...,
        source_attribute: ConstraintAttribute = ...,
        strength: int = ...,
        target: ConstraintTarget = ...,
        target_attribute: ConstraintAttribute = ...,
    ): ...
    def get_constant(self) -> float: ...
    def get_multiplier(self) -> float: ...
    def get_relation(self) -> ConstraintRelation: ...
    def get_source(self) -> Optional[ConstraintTarget]: ...
    def get_source_attribute(self) -> ConstraintAttribute: ...
    def get_strength(self) -> int: ...
    def get_target(self) -> Optional[ConstraintTarget]: ...
    def get_target_attribute(self) -> ConstraintAttribute: ...
    def is_attached(self) -> bool: ...
    def is_constant(self) -> bool: ...
    def is_required(self) -> bool: ...
    @classmethod
    def new(
        cls,
        target: Optional[ConstraintTarget],
        target_attribute: ConstraintAttribute,
        relation: ConstraintRelation,
        source: Optional[ConstraintTarget],
        source_attribute: ConstraintAttribute,
        multiplier: float,
        constant: float,
        strength: int,
    ) -> Constraint: ...
    @classmethod
    def new_constant(
        cls,
        target: Optional[ConstraintTarget],
        target_attribute: ConstraintAttribute,
        relation: ConstraintRelation,
        constant: float,
        strength: int,
    ) -> Constraint: ...

class ConstraintClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class ConstraintGuide(GObject.Object, ConstraintTarget):
    class Props:
        max_height: int
        max_width: int
        min_height: int
        min_width: int
        name: str
        nat_height: int
        nat_width: int
        strength: ConstraintStrength
    props: Props = ...
    def __init__(
        self,
        max_height: int = ...,
        max_width: int = ...,
        min_height: int = ...,
        min_width: int = ...,
        name: str = ...,
        nat_height: int = ...,
        nat_width: int = ...,
        strength: ConstraintStrength = ...,
    ): ...
    def get_max_size(self) -> Tuple[int, int]: ...
    def get_min_size(self) -> Tuple[int, int]: ...
    def get_name(self) -> Optional[str]: ...
    def get_nat_size(self) -> Tuple[int, int]: ...
    def get_strength(self) -> ConstraintStrength: ...
    @classmethod
    def new(cls) -> ConstraintGuide: ...
    def set_max_size(self, width: int, height: int) -> None: ...
    def set_min_size(self, width: int, height: int) -> None: ...
    def set_name(self, name: Optional[str] = None) -> None: ...
    def set_nat_size(self, width: int, height: int) -> None: ...
    def set_strength(self, strength: ConstraintStrength) -> None: ...

class ConstraintGuideClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class ConstraintLayout(LayoutManager, Buildable):
    def add_constraint(self, constraint: Constraint) -> None: ...
    def add_constraints_from_description(
        self, lines: Sequence[str], hspacing: int, vspacing: int, views: str
    ) -> list[Constraint]: ...
    def add_guide(self, guide: ConstraintGuide) -> None: ...
    @classmethod
    def new(cls) -> ConstraintLayout: ...
    def observe_constraints(self) -> Gio.ListModel: ...
    def observe_guides(self) -> Gio.ListModel: ...
    def remove_all_constraints(self) -> None: ...
    def remove_constraint(self, constraint: Constraint) -> None: ...
    def remove_guide(self, guide: ConstraintGuide) -> None: ...

class ConstraintLayoutChild(LayoutChild):
    class Props:
        child_widget: Widget
        layout_manager: LayoutManager
    props: Props = ...
    def __init__(
        self, child_widget: Widget = ..., layout_manager: LayoutManager = ...
    ): ...

class ConstraintLayoutChildClass(GObject.GPointer):
    parent_class: LayoutChildClass = ...

class ConstraintLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class ConstraintTarget(GObject.Object): ...
class ConstraintTargetInterface(GObject.GPointer): ...

class CssLocation(GObject.GPointer):
    bytes: int = ...
    chars: int = ...
    lines: int = ...
    line_bytes: int = ...
    line_chars: int = ...

class CssProvider(GObject.Object, StyleProvider):
    parent_instance: GObject.Object = ...
    def load_from_data(self, data: Sequence[int]) -> None: ...
    def load_from_file(self, file: Gio.File) -> None: ...
    def load_from_path(self, path: str) -> None: ...
    def load_from_resource(self, resource_path: str) -> None: ...
    def load_named(self, name: str, variant: Optional[str] = None) -> None: ...
    @classmethod
    def new(cls) -> CssProvider: ...
    def to_string(self) -> str: ...

class CssProviderClass(GObject.GPointer): ...
class CssProviderPrivate(GObject.GPointer): ...

class CssSection(GObject.GBoxed):
    def get_end_location(self) -> CssLocation: ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_parent(self) -> Optional[CssSection]: ...
    def get_start_location(self) -> CssLocation: ...
    @classmethod
    def new(
        cls, file: Optional[Gio.File], start: CssLocation, end: CssLocation
    ) -> CssSection: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> CssSection: ...
    def to_string(self) -> str: ...
    def unref(self) -> None: ...

class CssStyleChange(GObject.GPointer): ...

class CustomFilter(Filter):
    @classmethod
    def new(
        cls, match_func: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> CustomFilter: ...
    def set_filter_func(
        self, match_func: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> None: ...

class CustomFilterClass(GObject.GPointer):
    parent_class: FilterClass = ...

class CustomLayout(LayoutManager):
    @classmethod
    def new(
        cls,
        request_mode: Optional[Callable[[Widget], SizeRequestMode]],
        measure: Callable[[Widget, Orientation, int], Tuple[int, int, int, int]],
        allocate: Callable[[Widget, int, int, int], None],
    ) -> CustomLayout: ...

class CustomLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class CustomSorter(Sorter):
    def new(self, *args, **kwargs): ...  # FIXME Method
    def set_sort_func(self, *args, **kwargs): ...  # FIXME Method

class CustomSorterClass(GObject.GPointer):
    parent_class: SorterClass = ...

class Dialog(
    Window, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Window = ...
    def add_action_widget(self, child: Widget, response_id: int) -> None: ...
    def add_button(self, button_text: str, response_id: int) -> Widget: ...
    def add_buttons(self, *args, **kwargs): ...  # FIXME Method
    def do_close(self) -> None: ...
    def do_response(self, response_id: int) -> None: ...
    def get_content_area(self) -> Box: ...
    def get_header_bar(self) -> HeaderBar: ...
    def get_response_for_widget(self, widget: Widget) -> int: ...
    def get_widget_for_response(self, response_id: int) -> Optional[Widget]: ...
    @classmethod
    def new(cls) -> Dialog: ...
    def response(self, response_id: int) -> None: ...
    def set_default_response(self, response_id: int) -> None: ...
    def set_response_sensitive(self, response_id: int, setting: bool) -> None: ...

class DialogClass(GObject.GPointer):
    parent_class: WindowClass = ...
    response: Callable[[Dialog, int], None] = ...
    close: Callable[[Dialog], None] = ...
    padding: list[None] = ...

class DirectoryList(GObject.Object, Gio.ListModel):
    class Props:
        attributes: str
        error: GLib.Error
        file: Gio.File
        io_priority: int
        item_type: Type
        loading: bool
        monitored: bool
        n_items: int
    props: Props = ...
    def __init__(
        self,
        attributes: str = ...,
        file: Gio.File = ...,
        io_priority: int = ...,
        monitored: bool = ...,
    ): ...
    def get_attributes(self) -> Optional[str]: ...
    def get_error(self) -> Optional[GLib.Error]: ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_io_priority(self) -> int: ...
    def get_monitored(self) -> bool: ...
    def is_loading(self) -> bool: ...
    @classmethod
    def new(
        cls, attributes: Optional[str] = None, file: Optional[Gio.File] = None
    ) -> DirectoryList: ...
    def set_attributes(self, attributes: Optional[str] = None) -> None: ...
    def set_file(self, file: Optional[Gio.File] = None) -> None: ...
    def set_io_priority(self, io_priority: int) -> None: ...
    def set_monitored(self, monitored: bool) -> None: ...

class DirectoryListClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class DragIcon(Widget, Accessible, Buildable, ConstraintTarget, Native, Root):
    class Props:
        child: Widget
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    @staticmethod
    def create_widget_for_value(value: Any) -> Optional[Widget]: ...
    def get_child(self) -> Optional[Widget]: ...
    @staticmethod
    def get_for_drag(drag: Gdk.Drag) -> Widget: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    @staticmethod
    def set_from_paintable(
        drag: Gdk.Drag, paintable: Gdk.Paintable, hot_x: int, hot_y: int
    ) -> None: ...

class DragIconClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class DragSource(GestureSingle):
    class Props:
        actions: Gdk.DragAction
        content: Gdk.ContentProvider
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        actions: Gdk.DragAction = ...,
        content: Gdk.ContentProvider = ...,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def drag_cancel(self) -> None: ...
    def get_actions(self) -> Gdk.DragAction: ...
    def get_content(self) -> Optional[Gdk.ContentProvider]: ...
    def get_drag(self) -> Optional[Gdk.Drag]: ...
    @classmethod
    def new(cls) -> DragSource: ...
    def set_actions(self, actions: Gdk.DragAction) -> None: ...
    def set_content(self, content: Optional[Gdk.ContentProvider] = None) -> None: ...
    def set_icon(
        self, paintable: Optional[Gdk.Paintable], hot_x: int, hot_y: int
    ) -> None: ...

class DragSourceClass(GObject.GPointer): ...

class DrawingArea(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        content_height: int
        content_width: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        content_height: int = ...,
        content_width: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    widget: Widget = ...
    def do_resize(self, width: int, height: int) -> None: ...
    def get_content_height(self) -> int: ...
    def get_content_width(self) -> int: ...
    @classmethod
    def new(cls) -> DrawingArea: ...
    def set_content_height(self, height: int) -> None: ...
    def set_content_width(self, width: int) -> None: ...
    def set_draw_func(
        self, draw_func: Optional[Callable[..., None]] = None, *user_data: Any
    ) -> None: ...

class DrawingAreaClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    resize: Callable[[DrawingArea, int, int], None] = ...
    padding: list[None] = ...

class DropControllerMotion(EventController):
    class Props:
        contains_pointer: bool
        drop: Gdk.Drop
        is_pointer: bool
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def contains_pointer(self) -> bool: ...
    def get_drop(self) -> Optional[Gdk.Drop]: ...
    def is_pointer(self) -> bool: ...
    @classmethod
    def new(cls) -> DropControllerMotion: ...

class DropControllerMotionClass(GObject.GPointer): ...

class DropDown(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        enable_search: bool
        expression: Expression
        factory: ListItemFactory
        list_factory: ListItemFactory
        model: Gio.ListModel
        selected: int
        selected_item: GObject.Object
        show_arrow: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        enable_search: bool = ...,
        expression: Expression = ...,
        factory: ListItemFactory = ...,
        list_factory: ListItemFactory = ...,
        model: Gio.ListModel = ...,
        selected: int = ...,
        show_arrow: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_enable_search(self) -> bool: ...
    def get_expression(self) -> Optional[Expression]: ...
    def get_factory(self) -> Optional[ListItemFactory]: ...
    def get_list_factory(self) -> Optional[ListItemFactory]: ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_selected(self) -> int: ...
    def get_selected_item(self) -> Optional[GObject.Object]: ...
    def get_show_arrow(self) -> bool: ...
    @classmethod
    def new(
        cls,
        model: Optional[Gio.ListModel] = None,
        expression: Optional[Expression] = None,
    ) -> DropDown: ...
    @classmethod
    def new_from_strings(cls, strings: Sequence[str]) -> DropDown: ...
    def set_enable_search(self, enable_search: bool) -> None: ...
    def set_expression(self, expression: Optional[Expression] = None) -> None: ...
    def set_factory(self, factory: Optional[ListItemFactory] = None) -> None: ...
    def set_list_factory(self, factory: Optional[ListItemFactory] = None) -> None: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...
    def set_selected(self, position: int) -> None: ...
    def set_show_arrow(self, show_arrow: bool) -> None: ...

class DropDownClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class DropTarget(EventController):
    class Props:
        actions: Gdk.DragAction
        current_drop: Gdk.Drop
        formats: Gdk.ContentFormats
        preload: bool
        value: Any
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        actions: Gdk.DragAction = ...,
        formats: Gdk.ContentFormats = ...,
        preload: bool = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_actions(self) -> Gdk.DragAction: ...
    def get_current_drop(self) -> Optional[Gdk.Drop]: ...
    def get_drop(self) -> Optional[Gdk.Drop]: ...
    def get_formats(self) -> Optional[Gdk.ContentFormats]: ...
    def get_gtypes(self) -> Optional[list[Type]]: ...
    def get_preload(self) -> bool: ...
    def get_value(self) -> Optional[Any]: ...
    @classmethod
    def new(cls, type: Type, actions: Gdk.DragAction) -> DropTarget: ...
    def reject(self) -> None: ...
    def set_actions(self, actions: Gdk.DragAction) -> None: ...
    def set_gtypes(self, types: Optional[Sequence[Type]] = None) -> None: ...
    def set_preload(self, preload: bool) -> None: ...

class DropTargetAsync(EventController):
    class Props:
        actions: Gdk.DragAction
        formats: Gdk.ContentFormats
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        actions: Gdk.DragAction = ...,
        formats: Gdk.ContentFormats = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_actions(self) -> Gdk.DragAction: ...
    def get_formats(self) -> Optional[Gdk.ContentFormats]: ...
    @classmethod
    def new(
        cls, formats: Optional[Gdk.ContentFormats], actions: Gdk.DragAction
    ) -> DropTargetAsync: ...
    def reject_drop(self, drop: Gdk.Drop) -> None: ...
    def set_actions(self, actions: Gdk.DragAction) -> None: ...
    def set_formats(self, formats: Optional[Gdk.ContentFormats] = None) -> None: ...

class DropTargetAsyncClass(GObject.GPointer): ...
class DropTargetClass(GObject.GPointer): ...

class Editable(GObject.Object):
    @staticmethod
    def delegate_get_property(
        object: GObject.Object, prop_id: int, value: Any, pspec: GObject.ParamSpec
    ) -> bool: ...
    @staticmethod
    def delegate_set_property(
        object: GObject.Object, prop_id: int, value: Any, pspec: GObject.ParamSpec
    ) -> bool: ...
    def delete_selection(self) -> None: ...
    def delete_text(self, start_pos: int, end_pos: int) -> None: ...
    def finish_delegate(self) -> None: ...
    def get_alignment(self) -> float: ...
    def get_chars(self, start_pos: int, end_pos: int) -> str: ...
    def get_delegate(self) -> Optional[Editable]: ...
    def get_editable(self) -> bool: ...
    def get_enable_undo(self) -> bool: ...
    def get_max_width_chars(self) -> int: ...
    def get_position(self) -> int: ...
    def get_selection_bounds(self, *args, **kwargs): ...  # FIXME Method
    def get_text(self) -> str: ...
    def get_width_chars(self) -> int: ...
    def init_delegate(self) -> None: ...
    def insert_text(self, *args, **kwargs): ...  # FIXME Method
    @staticmethod
    def install_properties(
        object_class: GObject.ObjectClass, first_prop: int
    ) -> int: ...
    def select_region(self, start_pos: int, end_pos: int) -> None: ...
    def set_alignment(self, xalign: float) -> None: ...
    def set_editable(self, is_editable: bool) -> None: ...
    def set_enable_undo(self, enable_undo: bool) -> None: ...
    def set_max_width_chars(self, n_chars: int) -> None: ...
    def set_position(self, position: int) -> None: ...
    def set_text(self, text: str) -> None: ...
    def set_width_chars(self, n_chars: int) -> None: ...

class EditableInterface(GObject.GPointer):
    base_iface: GObject.TypeInterface = ...
    insert_text: Callable[[Editable, str, int], int] = ...
    delete_text: Callable[[Editable, int, int], None] = ...
    changed: Callable[[Editable], None] = ...
    get_text: Callable[[Editable], str] = ...
    do_insert_text: Callable[[Editable, str, int], int] = ...
    do_delete_text: Callable[[Editable, int, int], None] = ...
    get_selection_bounds: Callable[[Editable], Tuple[bool, int, int]] = ...
    set_selection_bounds: Callable[[Editable, int, int], None] = ...
    get_delegate: Callable[[Editable], Optional[Editable]] = ...

class EditableLabel(Widget, Accessible, Buildable, ConstraintTarget, Editable):
    class Props:
        editing: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
    props: Props = ...
    def __init__(
        self,
        editing: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    def get_editing(self) -> bool: ...
    @classmethod
    def new(cls, str: str) -> EditableLabel: ...
    def start_editing(self) -> None: ...
    def stop_editing(self, commit: bool) -> None: ...

class EditableLabelClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class EmojiChooser(
    Popover, Accessible, Buildable, ConstraintTarget, Native, ShortcutManager
):
    class Props:
        autohide: bool
        cascade_popdown: bool
        child: Widget
        default_widget: Widget
        has_arrow: bool
        mnemonics_visible: bool
        pointing_to: Gdk.Rectangle
        position: PositionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        autohide: bool = ...,
        cascade_popdown: bool = ...,
        child: Widget = ...,
        default_widget: Widget = ...,
        has_arrow: bool = ...,
        mnemonics_visible: bool = ...,
        pointing_to: Gdk.Rectangle = ...,
        position: PositionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    @classmethod
    def new(cls) -> EmojiChooser: ...

class EmojiChooserClass(GObject.GPointer): ...

class Entry(Widget, Accessible, Buildable, CellEditable, ConstraintTarget, Editable):
    class Props:
        activates_default: bool
        attributes: Pango.AttrList
        buffer: EntryBuffer
        completion: EntryCompletion
        enable_emoji_completion: bool
        extra_menu: Gio.MenuModel
        has_frame: bool
        im_module: str
        input_hints: InputHints
        input_purpose: InputPurpose
        invisible_char: int
        invisible_char_set: bool
        max_length: int
        overwrite_mode: bool
        placeholder_text: str
        primary_icon_activatable: bool
        primary_icon_gicon: Gio.Icon
        primary_icon_name: str
        primary_icon_paintable: Gdk.Paintable
        primary_icon_sensitive: bool
        primary_icon_storage_type: ImageType
        primary_icon_tooltip_markup: str
        primary_icon_tooltip_text: str
        progress_fraction: float
        progress_pulse_step: float
        scroll_offset: int
        secondary_icon_activatable: bool
        secondary_icon_gicon: Gio.Icon
        secondary_icon_name: str
        secondary_icon_paintable: Gdk.Paintable
        secondary_icon_sensitive: bool
        secondary_icon_storage_type: ImageType
        secondary_icon_tooltip_markup: str
        secondary_icon_tooltip_text: str
        show_emoji_icon: bool
        tabs: Pango.TabArray
        text_length: int
        truncate_multiline: bool
        visibility: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        editing_canceled: bool
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
    props: Props = ...
    def __init__(
        self,
        activates_default: bool = ...,
        attributes: Pango.AttrList = ...,
        buffer: EntryBuffer = ...,
        completion: EntryCompletion = ...,
        enable_emoji_completion: bool = ...,
        extra_menu: Gio.MenuModel = ...,
        has_frame: bool = ...,
        im_module: str = ...,
        input_hints: InputHints = ...,
        input_purpose: InputPurpose = ...,
        invisible_char: int = ...,
        invisible_char_set: bool = ...,
        max_length: int = ...,
        overwrite_mode: bool = ...,
        placeholder_text: str = ...,
        primary_icon_activatable: bool = ...,
        primary_icon_gicon: Gio.Icon = ...,
        primary_icon_name: str = ...,
        primary_icon_paintable: Gdk.Paintable = ...,
        primary_icon_sensitive: bool = ...,
        primary_icon_tooltip_markup: str = ...,
        primary_icon_tooltip_text: str = ...,
        progress_fraction: float = ...,
        progress_pulse_step: float = ...,
        secondary_icon_activatable: bool = ...,
        secondary_icon_gicon: Gio.Icon = ...,
        secondary_icon_name: str = ...,
        secondary_icon_paintable: Gdk.Paintable = ...,
        secondary_icon_sensitive: bool = ...,
        secondary_icon_tooltip_markup: str = ...,
        secondary_icon_tooltip_text: str = ...,
        show_emoji_icon: bool = ...,
        tabs: Pango.TabArray = ...,
        truncate_multiline: bool = ...,
        visibility: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editing_canceled: bool = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    parent_instance: Widget = ...
    def do_activate(self) -> None: ...
    def get_activates_default(self) -> bool: ...
    def get_alignment(self) -> float: ...
    def get_attributes(self) -> Optional[Pango.AttrList]: ...
    def get_buffer(self) -> EntryBuffer: ...
    def get_completion(self) -> Optional[EntryCompletion]: ...
    def get_current_icon_drag_source(self) -> int: ...
    def get_extra_menu(self) -> Optional[Gio.MenuModel]: ...
    def get_has_frame(self) -> bool: ...
    def get_icon_activatable(self, icon_pos: EntryIconPosition) -> bool: ...
    def get_icon_area(self, icon_pos: EntryIconPosition) -> Gdk.Rectangle: ...
    def get_icon_at_pos(self, x: int, y: int) -> int: ...
    def get_icon_gicon(self, icon_pos: EntryIconPosition) -> Optional[Gio.Icon]: ...
    def get_icon_name(self, icon_pos: EntryIconPosition) -> Optional[str]: ...
    def get_icon_paintable(
        self, icon_pos: EntryIconPosition
    ) -> Optional[Gdk.Paintable]: ...
    def get_icon_sensitive(self, icon_pos: EntryIconPosition) -> bool: ...
    def get_icon_storage_type(self, icon_pos: EntryIconPosition) -> ImageType: ...
    def get_icon_tooltip_markup(self, icon_pos: EntryIconPosition) -> Optional[str]: ...
    def get_icon_tooltip_text(self, icon_pos: EntryIconPosition) -> Optional[str]: ...
    def get_input_hints(self) -> InputHints: ...
    def get_input_purpose(self) -> InputPurpose: ...
    def get_invisible_char(self) -> str: ...
    def get_max_length(self) -> int: ...
    def get_overwrite_mode(self) -> bool: ...
    def get_placeholder_text(self) -> Optional[str]: ...
    def get_progress_fraction(self) -> float: ...
    def get_progress_pulse_step(self) -> float: ...
    def get_tabs(self) -> Optional[Pango.TabArray]: ...
    def get_text_length(self) -> int: ...
    def get_visibility(self) -> bool: ...
    def grab_focus_without_selecting(self) -> bool: ...
    @classmethod
    def new(cls) -> Entry: ...
    @classmethod
    def new_with_buffer(cls, buffer: EntryBuffer) -> Entry: ...
    def progress_pulse(self) -> None: ...
    def reset_im_context(self) -> None: ...
    def set_activates_default(self, setting: bool) -> None: ...
    def set_alignment(self, xalign: float) -> None: ...
    def set_attributes(self, attrs: Pango.AttrList) -> None: ...
    def set_buffer(self, buffer: EntryBuffer) -> None: ...
    def set_completion(self, completion: Optional[EntryCompletion] = None) -> None: ...
    def set_extra_menu(self, model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_has_frame(self, setting: bool) -> None: ...
    def set_icon_activatable(
        self, icon_pos: EntryIconPosition, activatable: bool
    ) -> None: ...
    def set_icon_drag_source(
        self,
        icon_pos: EntryIconPosition,
        provider: Gdk.ContentProvider,
        actions: Gdk.DragAction,
    ) -> None: ...
    def set_icon_from_gicon(
        self, icon_pos: EntryIconPosition, icon: Optional[Gio.Icon] = None
    ) -> None: ...
    def set_icon_from_icon_name(
        self, icon_pos: EntryIconPosition, icon_name: Optional[str] = None
    ) -> None: ...
    def set_icon_from_paintable(
        self, icon_pos: EntryIconPosition, paintable: Optional[Gdk.Paintable] = None
    ) -> None: ...
    def set_icon_sensitive(
        self, icon_pos: EntryIconPosition, sensitive: bool
    ) -> None: ...
    def set_icon_tooltip_markup(
        self, icon_pos: EntryIconPosition, tooltip: Optional[str] = None
    ) -> None: ...
    def set_icon_tooltip_text(
        self, icon_pos: EntryIconPosition, tooltip: Optional[str] = None
    ) -> None: ...
    def set_input_hints(self, hints: InputHints) -> None: ...
    def set_input_purpose(self, purpose: InputPurpose) -> None: ...
    def set_invisible_char(self, ch: str) -> None: ...
    def set_max_length(self, max: int) -> None: ...
    def set_overwrite_mode(self, overwrite: bool) -> None: ...
    def set_placeholder_text(self, text: Optional[str] = None) -> None: ...
    def set_progress_fraction(self, fraction: float) -> None: ...
    def set_progress_pulse_step(self, fraction: float) -> None: ...
    def set_tabs(self, tabs: Optional[Pango.TabArray] = None) -> None: ...
    def set_visibility(self, visible: bool) -> None: ...
    def unset_invisible_char(self) -> None: ...

class EntryBuffer(GObject.Object):
    class Props:
        length: int
        max_length: int
        text: str
    props: Props = ...
    def __init__(self, max_length: int = ..., text: str = ...): ...
    parent_instance: GObject.Object = ...
    def delete_text(self, position: int, n_chars: int) -> int: ...
    def do_delete_text(self, position: int, n_chars: int) -> int: ...
    def do_deleted_text(self, position: int, n_chars: int) -> None: ...
    def do_get_length(self) -> int: ...
    def do_get_text(self, n_bytes: int) -> str: ...
    def do_insert_text(self, position: int, chars: str, n_chars: int) -> int: ...
    def do_inserted_text(self, position: int, chars: str, n_chars: int) -> None: ...
    def emit_deleted_text(self, position: int, n_chars: int) -> None: ...
    def emit_inserted_text(self, position: int, chars: str, n_chars: int) -> None: ...
    def get_bytes(self) -> int: ...
    def get_length(self) -> int: ...
    def get_max_length(self) -> int: ...
    def get_text(self) -> str: ...
    def insert_text(self, position: int, chars: str, n_chars: int) -> int: ...
    @classmethod
    def new(cls, initial_chars: Optional[str], n_initial_chars: int) -> EntryBuffer: ...
    def set_max_length(self, max_length: int) -> None: ...
    def set_text(self, chars: str, n_chars: int) -> None: ...

class EntryBufferClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    inserted_text: Callable[[EntryBuffer, int, str, int], None] = ...
    deleted_text: Callable[[EntryBuffer, int, int], None] = ...
    get_text: Callable[[EntryBuffer, int], str] = ...
    get_length: Callable[[EntryBuffer], int] = ...
    insert_text: Callable[[EntryBuffer, int, str, int], int] = ...
    delete_text: Callable[[EntryBuffer, int, int], int] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...
    _gtk_reserved5: None = ...
    _gtk_reserved6: None = ...
    _gtk_reserved7: None = ...
    _gtk_reserved8: None = ...

class EntryClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    activate: Callable[[Entry], None] = ...
    padding: list[None] = ...

class EntryCompletion(GObject.Object, Buildable, CellLayout):
    class Props:
        cell_area: CellArea
        inline_completion: bool
        inline_selection: bool
        minimum_key_length: int
        model: TreeModel
        popup_completion: bool
        popup_set_width: bool
        popup_single_match: bool
        text_column: int
    props: Props = ...
    def __init__(
        self,
        cell_area: CellArea = ...,
        inline_completion: bool = ...,
        inline_selection: bool = ...,
        minimum_key_length: int = ...,
        model: TreeModel = ...,
        popup_completion: bool = ...,
        popup_set_width: bool = ...,
        popup_single_match: bool = ...,
        text_column: int = ...,
    ): ...
    def complete(self) -> None: ...
    def compute_prefix(self, key: str) -> Optional[str]: ...
    def get_completion_prefix(self) -> Optional[str]: ...
    def get_entry(self) -> Widget: ...
    def get_inline_completion(self) -> bool: ...
    def get_inline_selection(self) -> bool: ...
    def get_minimum_key_length(self) -> int: ...
    def get_model(self) -> Optional[TreeModel]: ...
    def get_popup_completion(self) -> bool: ...
    def get_popup_set_width(self) -> bool: ...
    def get_popup_single_match(self) -> bool: ...
    def get_text_column(self) -> int: ...
    def insert_prefix(self) -> None: ...
    @classmethod
    def new(cls) -> EntryCompletion: ...
    @classmethod
    def new_with_area(cls, area: CellArea) -> EntryCompletion: ...
    def set_inline_completion(self, inline_completion: bool) -> None: ...
    def set_inline_selection(self, inline_selection: bool) -> None: ...
    def set_match_func(self, func: Callable[..., bool], *func_data: Any) -> None: ...
    def set_minimum_key_length(self, length: int) -> None: ...
    def set_model(self, model: Optional[TreeModel] = None) -> None: ...
    def set_popup_completion(self, popup_completion: bool) -> None: ...
    def set_popup_set_width(self, popup_set_width: bool) -> None: ...
    def set_popup_single_match(self, popup_single_match: bool) -> None: ...
    def set_text_column(self, column: int) -> None: ...

class EventController(GObject.Object):
    class Props:
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_current_event(self) -> Optional[Gdk.Event]: ...
    def get_current_event_device(self) -> Optional[Gdk.Device]: ...
    def get_current_event_state(self) -> Gdk.ModifierType: ...
    def get_current_event_time(self) -> int: ...
    def get_name(self) -> Optional[str]: ...
    def get_propagation_limit(self) -> PropagationLimit: ...
    def get_propagation_phase(self) -> PropagationPhase: ...
    def get_widget(self) -> Widget: ...
    def reset(self) -> None: ...
    def set_name(self, name: Optional[str] = None) -> None: ...
    def set_propagation_limit(self, limit: PropagationLimit) -> None: ...
    def set_propagation_phase(self, phase: PropagationPhase) -> None: ...
    def set_static_name(self, name: Optional[str] = None) -> None: ...

class EventControllerClass(GObject.GPointer): ...

class EventControllerFocus(EventController):
    class Props:
        contains_focus: bool
        is_focus: bool
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def contains_focus(self) -> bool: ...
    def is_focus(self) -> bool: ...
    @classmethod
    def new(cls) -> EventControllerFocus: ...

class EventControllerFocusClass(GObject.GPointer): ...

class EventControllerKey(EventController):
    class Props:
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def forward(self, widget: Widget) -> bool: ...
    def get_group(self) -> int: ...
    def get_im_context(self) -> Optional[IMContext]: ...
    @classmethod
    def new(cls) -> EventControllerKey: ...
    def set_im_context(self, im_context: Optional[IMContext] = None) -> None: ...

class EventControllerKeyClass(GObject.GPointer): ...

class EventControllerLegacy(EventController):
    class Props:
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    @classmethod
    def new(cls) -> EventControllerLegacy: ...

class EventControllerLegacyClass(GObject.GPointer): ...

class EventControllerMotion(EventController):
    class Props:
        contains_pointer: bool
        is_pointer: bool
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def contains_pointer(self) -> bool: ...
    def is_pointer(self) -> bool: ...
    @classmethod
    def new(cls) -> EventControllerMotion: ...

class EventControllerMotionClass(GObject.GPointer): ...

class EventControllerScroll(EventController):
    class Props:
        flags: EventControllerScrollFlags
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        flags: EventControllerScrollFlags = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_flags(self) -> EventControllerScrollFlags: ...
    def get_unit(self) -> Gdk.ScrollUnit: ...
    @classmethod
    def new(cls, flags: EventControllerScrollFlags) -> EventControllerScroll: ...
    def set_flags(self, flags: EventControllerScrollFlags) -> None: ...

class EventControllerScrollClass(GObject.GPointer): ...

class EveryFilter(MultiFilter, Gio.ListModel, Buildable):
    class Props:
        item_type: Type
        n_items: int
    props: Props = ...
    @classmethod
    def new(cls) -> EveryFilter: ...

class EveryFilterClass(GObject.GPointer): ...

class Expander(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        expanded: bool
        label: str
        label_widget: Widget
        resize_toplevel: bool
        use_markup: bool
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        expanded: bool = ...,
        label: str = ...,
        label_widget: Widget = ...,
        resize_toplevel: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    def get_expanded(self) -> bool: ...
    def get_label(self) -> Optional[str]: ...
    def get_label_widget(self) -> Optional[Widget]: ...
    def get_resize_toplevel(self) -> bool: ...
    def get_use_markup(self) -> bool: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls, label: Optional[str] = None) -> Expander: ...
    @classmethod
    def new_with_mnemonic(cls, label: Optional[str] = None) -> Expander: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_expanded(self, expanded: bool) -> None: ...
    def set_label(self, label: Optional[str] = None) -> None: ...
    def set_label_widget(self, label_widget: Optional[Widget] = None) -> None: ...
    def set_resize_toplevel(self, resize_toplevel: bool) -> None: ...
    def set_use_markup(self, use_markup: bool) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class Expression:
    def bind(
        self,
        target: GObject.Object,
        property: str,
        this_: Optional[GObject.Object] = None,
    ) -> ExpressionWatch: ...
    def evaluate(self, this_: Optional[GObject.Object], value: Any) -> bool: ...
    def get_value_type(self) -> Type: ...
    def is_static(self) -> bool: ...
    def ref(self) -> Expression: ...
    def unref(self) -> None: ...
    def watch(
        self,
        this_: Optional[GObject.Object],
        notify: Callable[..., None],
        *user_data: Any,
    ) -> ExpressionWatch: ...

class ExpressionWatch(GObject.GBoxed):
    def evaluate(self, value: Any) -> bool: ...
    def ref(self) -> ExpressionWatch: ...
    def unref(self) -> None: ...
    def unwatch(self) -> None: ...

class FileChooser(GObject.Object):
    def add_choice(
        self,
        id: str,
        label: str,
        options: Optional[Sequence[str]] = None,
        option_labels: Optional[Sequence[str]] = None,
    ) -> None: ...
    def add_filter(self, filter: FileFilter) -> None: ...
    def add_shortcut_folder(self, folder: Gio.File) -> bool: ...
    def get_action(self) -> FileChooserAction: ...
    def get_choice(self, id: str) -> Optional[str]: ...
    def get_create_folders(self) -> bool: ...
    def get_current_folder(self) -> Optional[Gio.File]: ...
    def get_current_name(self) -> Optional[str]: ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_files(self) -> Gio.ListModel: ...
    def get_filter(self) -> Optional[FileFilter]: ...
    def get_filters(self) -> Gio.ListModel: ...
    def get_select_multiple(self) -> bool: ...
    def get_shortcut_folders(self) -> Gio.ListModel: ...
    def remove_choice(self, id: str) -> None: ...
    def remove_filter(self, filter: FileFilter) -> None: ...
    def remove_shortcut_folder(self, folder: Gio.File) -> bool: ...
    def set_action(self, action: FileChooserAction) -> None: ...
    def set_choice(self, id: str, option: str) -> None: ...
    def set_create_folders(self, create_folders: bool) -> None: ...
    def set_current_folder(self, file: Optional[Gio.File] = None) -> bool: ...
    def set_current_name(self, name: str) -> None: ...
    def set_file(self, file: Gio.File) -> bool: ...
    def set_filter(self, filter: FileFilter) -> None: ...
    def set_select_multiple(self, select_multiple: bool) -> None: ...

class FileChooserDialog(
    Dialog,
    Accessible,
    Buildable,
    ConstraintTarget,
    FileChooser,
    Native,
    Root,
    ShortcutManager,
):
    class Props:
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action: FileChooserAction
        create_folders: bool
        filter: FileFilter
        filters: Gio.ListModel
        select_multiple: bool
        shortcut_folders: Gio.ListModel
    props: Props = ...
    def __init__(
        self,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action: FileChooserAction = ...,
        create_folders: bool = ...,
        filter: FileFilter = ...,
        select_multiple: bool = ...,
    ): ...

class FileChooserNative(NativeDialog, FileChooser):
    class Props:
        accept_label: str
        cancel_label: str
        modal: bool
        title: str
        transient_for: Window
        visible: bool
        action: FileChooserAction
        create_folders: bool
        filter: FileFilter
        filters: Gio.ListModel
        select_multiple: bool
        shortcut_folders: Gio.ListModel
    props: Props = ...
    def __init__(
        self,
        accept_label: str = ...,
        cancel_label: str = ...,
        modal: bool = ...,
        title: str = ...,
        transient_for: Window = ...,
        visible: bool = ...,
        action: FileChooserAction = ...,
        create_folders: bool = ...,
        filter: FileFilter = ...,
        select_multiple: bool = ...,
    ): ...
    def get_accept_label(self) -> Optional[str]: ...
    def get_cancel_label(self) -> Optional[str]: ...
    @classmethod
    def new(
        cls,
        title: Optional[str],
        parent: Optional[Window],
        action: FileChooserAction,
        accept_label: Optional[str] = None,
        cancel_label: Optional[str] = None,
    ) -> FileChooserNative: ...
    def set_accept_label(self, accept_label: Optional[str] = None) -> None: ...
    def set_cancel_label(self, cancel_label: Optional[str] = None) -> None: ...

class FileChooserNativeClass(GObject.GPointer):
    parent_class: NativeDialogClass = ...

class FileChooserWidget(Widget, Accessible, Buildable, ConstraintTarget, FileChooser):
    class Props:
        search_mode: bool
        subtitle: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action: FileChooserAction
        create_folders: bool
        filter: FileFilter
        filters: Gio.ListModel
        select_multiple: bool
        shortcut_folders: Gio.ListModel
    props: Props = ...
    def __init__(
        self,
        search_mode: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action: FileChooserAction = ...,
        create_folders: bool = ...,
        filter: FileFilter = ...,
        select_multiple: bool = ...,
    ): ...
    @classmethod
    def new(cls, action: FileChooserAction) -> FileChooserWidget: ...

class FileFilter(Filter, Buildable):
    class Props:
        name: str
    props: Props = ...
    def __init__(self, name: str = ...): ...
    def add_mime_type(self, mime_type: str) -> None: ...
    def add_pattern(self, pattern: str) -> None: ...
    def add_pixbuf_formats(self) -> None: ...
    def add_suffix(self, suffix: str) -> None: ...
    def get_attributes(self) -> list[str]: ...
    def get_name(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> FileFilter: ...
    @classmethod
    def new_from_gvariant(cls, variant: GLib.Variant) -> FileFilter: ...
    def set_name(self, name: Optional[str] = None) -> None: ...
    def to_gvariant(self) -> GLib.Variant: ...

class Filter(GObject.Object):
    parent_instance: GObject.Object = ...
    def changed(self, change: FilterChange) -> None: ...
    def do_get_strictness(self) -> FilterMatch: ...
    def do_match(self, item: Optional[GObject.Object] = None) -> bool: ...
    def get_strictness(self) -> FilterMatch: ...
    def match(self, item: GObject.Object) -> bool: ...

class FilterClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    match: Callable[[Filter, Optional[GObject.Object]], bool] = ...
    get_strictness: Callable[[Filter], FilterMatch] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...
    _gtk_reserved5: None = ...
    _gtk_reserved6: None = ...
    _gtk_reserved7: None = ...
    _gtk_reserved8: None = ...

class FilterListModel(GObject.Object, Gio.ListModel):
    class Props:
        filter: Filter
        incremental: bool
        item_type: Type
        model: Gio.ListModel
        n_items: int
        pending: int
    props: Props = ...
    def __init__(
        self, filter: Filter = ..., incremental: bool = ..., model: Gio.ListModel = ...
    ): ...
    def get_filter(self) -> Optional[Filter]: ...
    def get_incremental(self) -> bool: ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_pending(self) -> int: ...
    @classmethod
    def new(
        cls, model: Optional[Gio.ListModel] = None, filter: Optional[Filter] = None
    ) -> FilterListModel: ...
    def set_filter(self, filter: Optional[Filter] = None) -> None: ...
    def set_incremental(self, incremental: bool) -> None: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...

class FilterListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class Fixed(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Widget = ...
    def get_child_position(self, widget: Widget) -> Tuple[float, float]: ...
    def get_child_transform(self, widget: Widget) -> Optional[Gsk.Transform]: ...
    def move(self, widget: Widget, x: float, y: float) -> None: ...
    @classmethod
    def new(cls) -> Fixed: ...
    def put(self, widget: Widget, x: float, y: float) -> None: ...
    def remove(self, widget: Widget) -> None: ...
    def set_child_transform(
        self, widget: Widget, transform: Optional[Gsk.Transform] = None
    ) -> None: ...

class FixedClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    padding: list[None] = ...

class FixedLayout(LayoutManager):
    @classmethod
    def new(cls) -> FixedLayout: ...

class FixedLayoutChild(LayoutChild):
    class Props:
        transform: Gsk.Transform
        child_widget: Widget
        layout_manager: LayoutManager
    props: Props = ...
    def __init__(
        self,
        transform: Gsk.Transform = ...,
        child_widget: Widget = ...,
        layout_manager: LayoutManager = ...,
    ): ...
    def get_transform(self) -> Optional[Gsk.Transform]: ...
    def set_transform(self, transform: Gsk.Transform) -> None: ...

class FixedLayoutChildClass(GObject.GPointer):
    parent_class: LayoutChildClass = ...

class FixedLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class FlattenListModel(GObject.Object, Gio.ListModel):
    class Props:
        item_type: Type
        model: Gio.ListModel
        n_items: int
    props: Props = ...
    def __init__(self, model: Gio.ListModel = ...): ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_model_for_item(self, position: int) -> Optional[Gio.ListModel]: ...
    @classmethod
    def new(cls, model: Optional[Gio.ListModel] = None) -> FlattenListModel: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...

class FlattenListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class FlowBox(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        accept_unpaired_release: bool
        activate_on_single_click: bool
        column_spacing: int
        homogeneous: bool
        max_children_per_line: int
        min_children_per_line: int
        row_spacing: int
        selection_mode: SelectionMode
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        accept_unpaired_release: bool = ...,
        activate_on_single_click: bool = ...,
        column_spacing: int = ...,
        homogeneous: bool = ...,
        max_children_per_line: int = ...,
        min_children_per_line: int = ...,
        row_spacing: int = ...,
        selection_mode: SelectionMode = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def append(self, child: Widget) -> None: ...
    def bind_model(
        self,
        model: Optional[Gio.ListModel],
        create_widget_func: Callable[..., Widget],
        *user_data: Any,
    ) -> None: ...
    def get_activate_on_single_click(self) -> bool: ...
    def get_child_at_index(self, idx: int) -> Optional[FlowBoxChild]: ...
    def get_child_at_pos(self, x: int, y: int) -> Optional[FlowBoxChild]: ...
    def get_column_spacing(self) -> int: ...
    def get_homogeneous(self) -> bool: ...
    def get_max_children_per_line(self) -> int: ...
    def get_min_children_per_line(self) -> int: ...
    def get_row_spacing(self) -> int: ...
    def get_selected_children(self) -> list[FlowBoxChild]: ...
    def get_selection_mode(self) -> SelectionMode: ...
    def insert(self, widget: Widget, position: int) -> None: ...
    def invalidate_filter(self) -> None: ...
    def invalidate_sort(self) -> None: ...
    @classmethod
    def new(cls) -> FlowBox: ...
    def prepend(self, child: Widget) -> None: ...
    def remove(self, widget: Widget) -> None: ...
    def select_all(self) -> None: ...
    def select_child(self, child: FlowBoxChild) -> None: ...
    def selected_foreach(self, func: Callable[..., None], *data: Any) -> None: ...
    def set_activate_on_single_click(self, single: bool) -> None: ...
    def set_column_spacing(self, spacing: int) -> None: ...
    def set_filter_func(
        self, filter_func: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> None: ...
    def set_hadjustment(self, adjustment: Adjustment) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_max_children_per_line(self, n_children: int) -> None: ...
    def set_min_children_per_line(self, n_children: int) -> None: ...
    def set_row_spacing(self, spacing: int) -> None: ...
    def set_selection_mode(self, mode: SelectionMode) -> None: ...
    def set_sort_func(
        self, sort_func: Optional[Callable[..., int]] = None, *user_data: Any
    ) -> None: ...
    def set_vadjustment(self, adjustment: Adjustment) -> None: ...
    def unselect_all(self) -> None: ...
    def unselect_child(self, child: FlowBoxChild) -> None: ...

class FlowBoxChild(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Widget = ...
    def changed(self) -> None: ...
    def do_activate(self) -> None: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_index(self) -> int: ...
    def is_selected(self) -> bool: ...
    @classmethod
    def new(cls) -> FlowBoxChild: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...

class FlowBoxChildClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    activate: Callable[[FlowBoxChild], None] = ...
    padding: list[None] = ...

class FontButton(Widget, Accessible, Buildable, ConstraintTarget, FontChooser):
    class Props:
        modal: bool
        title: str
        use_font: bool
        use_size: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        language: str
        level: FontChooserLevel
        preview_text: str
        show_preview_entry: bool
    props: Props = ...
    def __init__(
        self,
        modal: bool = ...,
        title: str = ...,
        use_font: bool = ...,
        use_size: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        language: str = ...,
        level: FontChooserLevel = ...,
        preview_text: str = ...,
        show_preview_entry: bool = ...,
    ): ...
    def get_modal(self) -> bool: ...
    def get_title(self) -> str: ...
    def get_use_font(self) -> bool: ...
    def get_use_size(self) -> bool: ...
    @classmethod
    def new(cls) -> FontButton: ...
    @classmethod
    def new_with_font(cls, fontname: str) -> FontButton: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_font(self, use_font: bool) -> None: ...
    def set_use_size(self, use_size: bool) -> None: ...

class FontChooser(GObject.Object):
    def get_font(self) -> Optional[str]: ...
    def get_font_desc(self) -> Optional[Pango.FontDescription]: ...
    def get_font_face(self) -> Optional[Pango.FontFace]: ...
    def get_font_family(self) -> Optional[Pango.FontFamily]: ...
    def get_font_features(self) -> str: ...
    def get_font_map(self) -> Optional[Pango.FontMap]: ...
    def get_font_size(self) -> int: ...
    def get_language(self) -> str: ...
    def get_level(self) -> FontChooserLevel: ...
    def get_preview_text(self) -> str: ...
    def get_show_preview_entry(self) -> bool: ...
    def set_filter_func(
        self, filter: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> None: ...
    def set_font(self, fontname: str) -> None: ...
    def set_font_desc(self, font_desc: Pango.FontDescription) -> None: ...
    def set_font_map(self, fontmap: Optional[Pango.FontMap] = None) -> None: ...
    def set_language(self, language: str) -> None: ...
    def set_level(self, level: FontChooserLevel) -> None: ...
    def set_preview_text(self, text: str) -> None: ...
    def set_show_preview_entry(self, show_preview_entry: bool) -> None: ...

class FontChooserDialog(
    Dialog,
    Accessible,
    Buildable,
    ConstraintTarget,
    FontChooser,
    Native,
    Root,
    ShortcutManager,
):
    class Props:
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        language: str
        level: FontChooserLevel
        preview_text: str
        show_preview_entry: bool
    props: Props = ...
    def __init__(
        self,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        language: str = ...,
        level: FontChooserLevel = ...,
        preview_text: str = ...,
        show_preview_entry: bool = ...,
    ): ...
    @classmethod
    def new(
        cls, title: Optional[str] = None, parent: Optional[Window] = None
    ) -> FontChooserDialog: ...

class FontChooserIface(GObject.GPointer):
    base_iface: GObject.TypeInterface = ...
    get_font_family: Callable[[FontChooser], Optional[Pango.FontFamily]] = ...
    get_font_face: Callable[[FontChooser], Optional[Pango.FontFace]] = ...
    get_font_size: Callable[[FontChooser], int] = ...
    set_filter_func: Callable[..., None] = ...
    font_activated: Callable[[FontChooser, str], None] = ...
    set_font_map: Callable[[FontChooser, Optional[Pango.FontMap]], None] = ...
    get_font_map: Callable[[FontChooser], Optional[Pango.FontMap]] = ...
    padding: list[None] = ...

class FontChooserWidget(Widget, Accessible, Buildable, ConstraintTarget, FontChooser):
    class Props:
        tweak_action: Gio.Action
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        language: str
        level: FontChooserLevel
        preview_text: str
        show_preview_entry: bool
    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        language: str = ...,
        level: FontChooserLevel = ...,
        preview_text: str = ...,
        show_preview_entry: bool = ...,
    ): ...
    @classmethod
    def new(cls) -> FontChooserWidget: ...

class Frame(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        label: str
        label_widget: Widget
        label_xalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        label: str = ...,
        label_widget: Widget = ...,
        label_xalign: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Widget = ...
    def do_compute_child_allocation(self, allocation: Gdk.Rectangle) -> None: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_label(self) -> Optional[str]: ...
    def get_label_align(self) -> float: ...
    def get_label_widget(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls, label: Optional[str] = None) -> Frame: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_label(self, label: Optional[str] = None) -> None: ...
    def set_label_align(self, xalign: float) -> None: ...
    def set_label_widget(self, label_widget: Optional[Widget] = None) -> None: ...

class FrameClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    compute_child_allocation: Callable[[Frame, Gdk.Rectangle], None] = ...
    padding: list[None] = ...

class GLArea(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        auto_render: bool
        context: Gdk.GLContext
        has_depth_buffer: bool
        has_stencil_buffer: bool
        use_es: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        auto_render: bool = ...,
        has_depth_buffer: bool = ...,
        has_stencil_buffer: bool = ...,
        use_es: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Widget = ...
    def attach_buffers(self) -> None: ...
    def do_render(self, context: Gdk.GLContext) -> bool: ...
    def do_resize(self, width: int, height: int) -> None: ...
    def get_auto_render(self) -> bool: ...
    def get_context(self) -> Optional[Gdk.GLContext]: ...
    def get_error(self) -> Optional[GLib.Error]: ...
    def get_has_depth_buffer(self) -> bool: ...
    def get_has_stencil_buffer(self) -> bool: ...
    def get_required_version(self) -> Tuple[int, int]: ...
    def get_use_es(self) -> bool: ...
    def make_current(self) -> None: ...
    @classmethod
    def new(cls) -> GLArea: ...
    def queue_render(self) -> None: ...
    def set_auto_render(self, auto_render: bool) -> None: ...
    def set_error(self, error: Optional[GLib.Error] = None) -> None: ...
    def set_has_depth_buffer(self, has_depth_buffer: bool) -> None: ...
    def set_has_stencil_buffer(self, has_stencil_buffer: bool) -> None: ...
    def set_required_version(self, major: int, minor: int) -> None: ...
    def set_use_es(self, use_es: bool) -> None: ...

class GLAreaClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    render: Callable[[GLArea, Gdk.GLContext], bool] = ...
    resize: Callable[[GLArea, int, int], None] = ...
    create_context: None = ...
    _padding: list[None] = ...

class Gesture(EventController):
    class Props:
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_bounding_box(self) -> Tuple[bool, Gdk.Rectangle]: ...
    def get_bounding_box_center(self) -> Tuple[bool, float, float]: ...
    def get_device(self) -> Optional[Gdk.Device]: ...
    def get_group(self) -> list[Gesture]: ...
    def get_last_event(
        self, sequence: Optional[Gdk.EventSequence] = None
    ) -> Optional[Gdk.Event]: ...
    def get_last_updated_sequence(self) -> Optional[Gdk.EventSequence]: ...
    def get_point(
        self, sequence: Optional[Gdk.EventSequence] = None
    ) -> Tuple[bool, float, float]: ...
    def get_sequence_state(self, sequence: Gdk.EventSequence) -> EventSequenceState: ...
    def get_sequences(self) -> list[Gdk.EventSequence]: ...
    def group(self, gesture: Gesture) -> None: ...
    def handles_sequence(
        self, sequence: Optional[Gdk.EventSequence] = None
    ) -> bool: ...
    def is_active(self) -> bool: ...
    def is_grouped_with(self, other: Gesture) -> bool: ...
    def is_recognized(self) -> bool: ...
    def set_sequence_state(
        self, sequence: Gdk.EventSequence, state: EventSequenceState
    ) -> bool: ...
    def set_state(self, state: EventSequenceState) -> bool: ...
    def ungroup(self) -> None: ...

class GestureClass(GObject.GPointer): ...

class GestureClick(GestureSingle):
    class Props:
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    @classmethod
    def new(cls) -> GestureClick: ...

class GestureClickClass(GObject.GPointer): ...

class GestureDrag(GestureSingle):
    class Props:
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_offset(self) -> Tuple[bool, float, float]: ...
    def get_start_point(self) -> Tuple[bool, float, float]: ...
    @classmethod
    def new(cls) -> GestureDrag: ...

class GestureDragClass(GObject.GPointer): ...

class GestureLongPress(GestureSingle):
    class Props:
        delay_factor: float
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        delay_factor: float = ...,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_delay_factor(self) -> float: ...
    @classmethod
    def new(cls) -> GestureLongPress: ...
    def set_delay_factor(self, delay_factor: float) -> None: ...

class GestureLongPressClass(GObject.GPointer): ...

class GesturePan(GestureDrag):
    class Props:
        orientation: Orientation
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        orientation: Orientation = ...,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_orientation(self) -> Orientation: ...
    @classmethod
    def new(cls, orientation: Orientation) -> GesturePan: ...
    def set_orientation(self, orientation: Orientation) -> None: ...

class GesturePanClass(GObject.GPointer): ...

class GestureRotate(Gesture):
    class Props:
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_angle_delta(self) -> float: ...
    @classmethod
    def new(cls) -> GestureRotate: ...

class GestureRotateClass(GObject.GPointer): ...

class GestureSingle(Gesture):
    class Props:
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_button(self) -> int: ...
    def get_current_button(self) -> int: ...
    def get_current_sequence(self) -> Optional[Gdk.EventSequence]: ...
    def get_exclusive(self) -> bool: ...
    def get_touch_only(self) -> bool: ...
    def set_button(self, button: int) -> None: ...
    def set_exclusive(self, exclusive: bool) -> None: ...
    def set_touch_only(self, touch_only: bool) -> None: ...

class GestureSingleClass(GObject.GPointer): ...

class GestureStylus(GestureSingle):
    class Props:
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_axes(self, axes: Sequence[Gdk.AxisUse]) -> Tuple[bool, list[float]]: ...
    def get_axis(self, axis: Gdk.AxisUse) -> Tuple[bool, float]: ...
    def get_backlog(self) -> Tuple[bool, list[Gdk.TimeCoord]]: ...
    def get_device_tool(self) -> Optional[Gdk.DeviceTool]: ...
    @classmethod
    def new(cls) -> GestureStylus: ...

class GestureStylusClass(GObject.GPointer): ...

class GestureSwipe(GestureSingle):
    class Props:
        button: int
        exclusive: bool
        touch_only: bool
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        button: int = ...,
        exclusive: bool = ...,
        touch_only: bool = ...,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_velocity(self) -> Tuple[bool, float, float]: ...
    @classmethod
    def new(cls) -> GestureSwipe: ...

class GestureSwipeClass(GObject.GPointer): ...

class GestureZoom(Gesture):
    class Props:
        n_points: int
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        n_points: int = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def get_scale_delta(self) -> float: ...
    @classmethod
    def new(cls) -> GestureZoom: ...

class GestureZoomClass(GObject.GPointer): ...

class Grid(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        baseline_row: int = ...,
        column_homogeneous: bool = ...,
        column_spacing: int = ...,
        row_homogeneous: bool = ...,
        row_spacing: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    parent_instance: Widget = ...
    def attach(
        self, child: Widget, column: int, row: int, width: int, height: int
    ) -> None: ...
    def attach_next_to(
        self,
        child: Widget,
        sibling: Optional[Widget],
        side: PositionType,
        width: int,
        height: int,
    ) -> None: ...
    def get_baseline_row(self) -> int: ...
    def get_child_at(self, column: int, row: int) -> Optional[Widget]: ...
    def get_column_homogeneous(self) -> bool: ...
    def get_column_spacing(self) -> int: ...
    def get_row_baseline_position(self, row: int) -> BaselinePosition: ...
    def get_row_homogeneous(self) -> bool: ...
    def get_row_spacing(self) -> int: ...
    def insert_column(self, position: int) -> None: ...
    def insert_next_to(self, sibling: Widget, side: PositionType) -> None: ...
    def insert_row(self, position: int) -> None: ...
    @classmethod
    def new(cls) -> Grid: ...
    def query_child(self, child: Widget) -> Tuple[int, int, int, int]: ...
    def remove(self, child: Widget) -> None: ...
    def remove_column(self, position: int) -> None: ...
    def remove_row(self, position: int) -> None: ...
    def set_baseline_row(self, row: int) -> None: ...
    def set_column_homogeneous(self, homogeneous: bool) -> None: ...
    def set_column_spacing(self, spacing: int) -> None: ...
    def set_row_baseline_position(self, row: int, pos: BaselinePosition) -> None: ...
    def set_row_homogeneous(self, homogeneous: bool) -> None: ...
    def set_row_spacing(self, spacing: int) -> None: ...

class GridClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    padding: list[None] = ...

class GridLayout(LayoutManager):
    class Props:
        baseline_row: int
        column_homogeneous: bool
        column_spacing: int
        row_homogeneous: bool
        row_spacing: int
    props: Props = ...
    def __init__(
        self,
        baseline_row: int = ...,
        column_homogeneous: bool = ...,
        column_spacing: int = ...,
        row_homogeneous: bool = ...,
        row_spacing: int = ...,
    ): ...
    def get_baseline_row(self) -> int: ...
    def get_column_homogeneous(self) -> bool: ...
    def get_column_spacing(self) -> int: ...
    def get_row_baseline_position(self, row: int) -> BaselinePosition: ...
    def get_row_homogeneous(self) -> bool: ...
    def get_row_spacing(self) -> int: ...
    @classmethod
    def new(cls) -> GridLayout: ...
    def set_baseline_row(self, row: int) -> None: ...
    def set_column_homogeneous(self, homogeneous: bool) -> None: ...
    def set_column_spacing(self, spacing: int) -> None: ...
    def set_row_baseline_position(self, row: int, pos: BaselinePosition) -> None: ...
    def set_row_homogeneous(self, homogeneous: bool) -> None: ...
    def set_row_spacing(self, spacing: int) -> None: ...

class GridLayoutChild(LayoutChild):
    class Props:
        column: int
        column_span: int
        row: int
        row_span: int
        child_widget: Widget
        layout_manager: LayoutManager
    props: Props = ...
    def __init__(
        self,
        column: int = ...,
        column_span: int = ...,
        row: int = ...,
        row_span: int = ...,
        child_widget: Widget = ...,
        layout_manager: LayoutManager = ...,
    ): ...
    def get_column(self) -> int: ...
    def get_column_span(self) -> int: ...
    def get_row(self) -> int: ...
    def get_row_span(self) -> int: ...
    def set_column(self, column: int) -> None: ...
    def set_column_span(self, span: int) -> None: ...
    def set_row(self, row: int) -> None: ...
    def set_row_span(self, span: int) -> None: ...

class GridLayoutChildClass(GObject.GPointer):
    parent_class: LayoutChildClass = ...

class GridLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class GridView(
    ListBase, Accessible, Buildable, ConstraintTarget, Orientable, Scrollable
):
    class Props:
        enable_rubberband: bool
        factory: ListItemFactory
        max_columns: int
        min_columns: int
        model: SelectionModel
        single_click_activate: bool
        orientation: Orientation
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        enable_rubberband: bool = ...,
        factory: ListItemFactory = ...,
        max_columns: int = ...,
        min_columns: int = ...,
        model: SelectionModel = ...,
        single_click_activate: bool = ...,
        orientation: Orientation = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    def get_enable_rubberband(self) -> bool: ...
    def get_factory(self) -> Optional[ListItemFactory]: ...
    def get_max_columns(self) -> int: ...
    def get_min_columns(self) -> int: ...
    def get_model(self) -> Optional[SelectionModel]: ...
    def get_single_click_activate(self) -> bool: ...
    @classmethod
    def new(
        cls,
        model: Optional[SelectionModel] = None,
        factory: Optional[ListItemFactory] = None,
    ) -> GridView: ...
    def set_enable_rubberband(self, enable_rubberband: bool) -> None: ...
    def set_factory(self, factory: Optional[ListItemFactory] = None) -> None: ...
    def set_max_columns(self, max_columns: int) -> None: ...
    def set_min_columns(self, min_columns: int) -> None: ...
    def set_model(self, model: Optional[SelectionModel] = None) -> None: ...
    def set_single_click_activate(self, single_click_activate: bool) -> None: ...

class GridViewClass(GObject.GPointer): ...

class HeaderBar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        decoration_layout: str
        show_title_buttons: bool
        title_widget: Widget
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        decoration_layout: str = ...,
        show_title_buttons: bool = ...,
        title_widget: Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_decoration_layout(self) -> Optional[str]: ...
    def get_show_title_buttons(self) -> bool: ...
    def get_title_widget(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls) -> HeaderBar: ...
    def pack_end(self, child: Widget) -> None: ...
    def pack_start(self, child: Widget) -> None: ...
    def remove(self, child: Widget) -> None: ...
    def set_decoration_layout(self, layout: Optional[str] = None) -> None: ...
    def set_show_title_buttons(self, setting: bool) -> None: ...
    def set_title_widget(self, title_widget: Optional[Widget] = None) -> None: ...

class IMContext(GObject.Object):
    class Props:
        input_hints: InputHints
        input_purpose: InputPurpose
    props: Props = ...
    def __init__(
        self, input_hints: InputHints = ..., input_purpose: InputPurpose = ...
    ): ...
    parent_instance: GObject.Object = ...
    def delete_surrounding(self, offset: int, n_chars: int) -> bool: ...
    def do_commit(self, str: str) -> None: ...
    def do_delete_surrounding(self, offset: int, n_chars: int) -> bool: ...
    def do_filter_keypress(self, event: Gdk.Event) -> bool: ...
    def do_focus_in(self) -> None: ...
    def do_focus_out(self) -> None: ...
    def do_get_preedit_string(self) -> Tuple[str, Pango.AttrList, int]: ...
    def do_get_surrounding(self) -> Tuple[bool, str, int]: ...
    def do_get_surrounding_with_selection(self) -> Tuple[bool, str, int, int]: ...
    def do_preedit_changed(self) -> None: ...
    def do_preedit_end(self) -> None: ...
    def do_preedit_start(self) -> None: ...
    def do_reset(self) -> None: ...
    def do_retrieve_surrounding(self) -> bool: ...
    def do_set_client_widget(self, widget: Optional[Widget] = None) -> None: ...
    def do_set_cursor_location(self, area: Gdk.Rectangle) -> None: ...
    def do_set_surrounding(self, text: str, len: int, cursor_index: int) -> None: ...
    def do_set_surrounding_with_selection(
        self, text: str, len: int, cursor_index: int, anchor_index: int
    ) -> None: ...
    def do_set_use_preedit(self, use_preedit: bool) -> None: ...
    def filter_key(
        self,
        press: bool,
        surface: Gdk.Surface,
        device: Gdk.Device,
        time: int,
        keycode: int,
        state: Gdk.ModifierType,
        group: int,
    ) -> bool: ...
    def filter_keypress(self, event: Gdk.Event) -> bool: ...
    def focus_in(self) -> None: ...
    def focus_out(self) -> None: ...
    def get_preedit_string(self) -> Tuple[str, Pango.AttrList, int]: ...
    def get_surrounding(self, *args, **kwargs): ...  # FIXME Method
    def get_surrounding_with_selection(self) -> Tuple[bool, str, int, int]: ...
    def reset(self) -> None: ...
    def set_client_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_cursor_location(self, area: Gdk.Rectangle) -> None: ...
    def set_surrounding(self, text: str, len: int, cursor_index: int) -> None: ...
    def set_surrounding_with_selection(
        self, text: str, len: int, cursor_index: int, anchor_index: int
    ) -> None: ...
    def set_use_preedit(self, use_preedit: bool) -> None: ...

class IMContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    preedit_start: Callable[[IMContext], None] = ...
    preedit_end: Callable[[IMContext], None] = ...
    preedit_changed: Callable[[IMContext], None] = ...
    commit: Callable[[IMContext, str], None] = ...
    retrieve_surrounding: Callable[[IMContext], bool] = ...
    delete_surrounding: Callable[[IMContext, int, int], bool] = ...
    set_client_widget: Callable[[IMContext, Optional[Widget]], None] = ...
    get_preedit_string: Callable[[IMContext], Tuple[str, Pango.AttrList, int]] = ...
    filter_keypress: Callable[[IMContext, Gdk.Event], bool] = ...
    focus_in: Callable[[IMContext], None] = ...
    focus_out: Callable[[IMContext], None] = ...
    reset: Callable[[IMContext], None] = ...
    set_cursor_location: Callable[[IMContext, Gdk.Rectangle], None] = ...
    set_use_preedit: Callable[[IMContext, bool], None] = ...
    set_surrounding: Callable[[IMContext, str, int, int], None] = ...
    get_surrounding: Callable[[IMContext], Tuple[bool, str, int]] = ...
    set_surrounding_with_selection: Callable[
        [IMContext, str, int, int, int], None
    ] = ...
    get_surrounding_with_selection: Callable[
        [IMContext], Tuple[bool, str, int, int]
    ] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...
    _gtk_reserved5: None = ...

class IMContextSimple(IMContext):
    class Props:
        input_hints: InputHints
        input_purpose: InputPurpose
    props: Props = ...
    def __init__(
        self, input_hints: InputHints = ..., input_purpose: InputPurpose = ...
    ): ...
    object: IMContext = ...
    priv: IMContextSimplePrivate = ...
    def add_compose_file(self, compose_file: str) -> None: ...
    @classmethod
    def new(cls) -> IMContextSimple: ...

class IMContextSimpleClass(GObject.GPointer):
    parent_class: IMContextClass = ...

class IMContextSimplePrivate(GObject.GPointer): ...

class IMMulticontext(IMContext):
    class Props:
        input_hints: InputHints
        input_purpose: InputPurpose
    props: Props = ...
    def __init__(
        self, input_hints: InputHints = ..., input_purpose: InputPurpose = ...
    ): ...
    object: IMContext = ...
    priv: IMMulticontextPrivate = ...
    def get_context_id(self) -> str: ...
    @classmethod
    def new(cls) -> IMMulticontext: ...
    def set_context_id(self, context_id: Optional[str] = None) -> None: ...

class IMMulticontextClass(GObject.GPointer):
    parent_class: IMContextClass = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class IMMulticontextPrivate(GObject.GPointer): ...

class IconPaintable(GObject.Object, Gdk.Paintable, SymbolicPaintable):
    class Props:
        file: Gio.File
        icon_name: str
        is_symbolic: bool
    props: Props = ...
    def __init__(
        self, file: Gio.File = ..., icon_name: str = ..., is_symbolic: bool = ...
    ): ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def is_symbolic(self) -> bool: ...
    @classmethod
    def new_for_file(cls, file: Gio.File, size: int, scale: int) -> IconPaintable: ...

class IconTheme(GObject.Object):
    class Props:
        display: Gdk.Display
        icon_names: list[str]
        resource_path: list[str]
        search_path: list[str]
        theme_name: str
    props: Props = ...
    def __init__(
        self,
        display: Gdk.Display = ...,
        resource_path: Sequence[str] = ...,
        search_path: Sequence[str] = ...,
        theme_name: str = ...,
    ): ...
    def add_resource_path(self, path: str) -> None: ...
    def add_search_path(self, path: str) -> None: ...
    def get_display(self) -> Optional[Gdk.Display]: ...
    @staticmethod
    def get_for_display(display: Gdk.Display) -> IconTheme: ...
    def get_icon_names(self) -> list[str]: ...
    def get_icon_sizes(self, icon_name: str) -> list[int]: ...
    def get_resource_path(self) -> Optional[list[str]]: ...
    def get_search_path(self) -> Optional[list[str]]: ...
    def get_theme_name(self) -> str: ...
    def has_gicon(self, gicon: Gio.Icon) -> bool: ...
    def has_icon(self, icon_name: str) -> bool: ...
    def lookup_by_gicon(
        self,
        icon: Gio.Icon,
        size: int,
        scale: int,
        direction: TextDirection,
        flags: IconLookupFlags,
    ) -> IconPaintable: ...
    def lookup_icon(
        self,
        icon_name: str,
        fallbacks: Optional[Sequence[str]],
        size: int,
        scale: int,
        direction: TextDirection,
        flags: IconLookupFlags,
    ) -> IconPaintable: ...
    @classmethod
    def new(cls) -> IconTheme: ...
    def set_resource_path(self, path: Optional[Sequence[str]] = None) -> None: ...
    def set_search_path(self, path: Optional[Sequence[str]] = None) -> None: ...
    def set_theme_name(self, theme_name: Optional[str] = None) -> None: ...

class IconView(Widget, Accessible, Buildable, CellLayout, ConstraintTarget, Scrollable):
    class Props:
        activate_on_single_click: bool
        cell_area: CellArea
        column_spacing: int
        columns: int
        item_orientation: Orientation
        item_padding: int
        item_width: int
        margin: int
        markup_column: int
        model: TreeModel
        pixbuf_column: int
        reorderable: bool
        row_spacing: int
        selection_mode: SelectionMode
        spacing: int
        text_column: int
        tooltip_column: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        activate_on_single_click: bool = ...,
        cell_area: CellArea = ...,
        column_spacing: int = ...,
        columns: int = ...,
        item_orientation: Orientation = ...,
        item_padding: int = ...,
        item_width: int = ...,
        margin: int = ...,
        markup_column: int = ...,
        model: TreeModel = ...,
        pixbuf_column: int = ...,
        reorderable: bool = ...,
        row_spacing: int = ...,
        selection_mode: SelectionMode = ...,
        spacing: int = ...,
        text_column: int = ...,
        tooltip_column: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    def create_drag_icon(self, path: TreePath) -> Optional[Gdk.Paintable]: ...
    def enable_model_drag_dest(
        self, formats: Gdk.ContentFormats, actions: Gdk.DragAction
    ) -> None: ...
    def enable_model_drag_source(
        self,
        start_button_mask: Gdk.ModifierType,
        formats: Gdk.ContentFormats,
        actions: Gdk.DragAction,
    ) -> None: ...
    def get_activate_on_single_click(self) -> bool: ...
    def get_cell_rect(
        self, path: TreePath, cell: Optional[CellRenderer] = None
    ) -> Tuple[bool, Gdk.Rectangle]: ...
    def get_column_spacing(self) -> int: ...
    def get_columns(self) -> int: ...
    def get_cursor(self) -> Tuple[bool, TreePath, CellRenderer]: ...
    def get_dest_item_at_pos(self, *args, **kwargs): ...  # FIXME Method
    def get_drag_dest_item(self) -> Tuple[TreePath, IconViewDropPosition]: ...
    def get_item_at_pos(self, *args, **kwargs): ...  # FIXME Method
    def get_item_column(self, path: TreePath) -> int: ...
    def get_item_orientation(self) -> Orientation: ...
    def get_item_padding(self) -> int: ...
    def get_item_row(self, path: TreePath) -> int: ...
    def get_item_width(self) -> int: ...
    def get_margin(self) -> int: ...
    def get_markup_column(self) -> int: ...
    def get_model(self) -> Optional[TreeModel]: ...
    def get_path_at_pos(self, x: int, y: int) -> Optional[TreePath]: ...
    def get_pixbuf_column(self) -> int: ...
    def get_reorderable(self) -> bool: ...
    def get_row_spacing(self) -> int: ...
    def get_selected_items(self) -> list[TreePath]: ...
    def get_selection_mode(self) -> SelectionMode: ...
    def get_spacing(self) -> int: ...
    def get_text_column(self) -> int: ...
    def get_tooltip_column(self) -> int: ...
    def get_tooltip_context(
        self, x: int, y: int, keyboard_tip: bool
    ) -> Tuple[bool, TreeModel, TreePath, TreeIter]: ...
    def get_visible_range(self, *args, **kwargs): ...  # FIXME Method
    def item_activated(self, path: TreePath) -> None: ...
    @classmethod
    def new(cls) -> IconView: ...
    @classmethod
    def new_with_area(cls, area: CellArea) -> IconView: ...
    @classmethod
    def new_with_model(cls, model: TreeModel) -> IconView: ...
    def path_is_selected(self, path: TreePath) -> bool: ...
    def scroll_to_path(
        self, path: TreePath, use_align: bool, row_align: float, col_align: float
    ) -> None: ...
    def select_all(self) -> None: ...
    def select_path(self, path: TreePath) -> None: ...
    def selected_foreach(self, func: Callable[..., None], *data: Any) -> None: ...
    def set_activate_on_single_click(self, single: bool) -> None: ...
    def set_column_spacing(self, column_spacing: int) -> None: ...
    def set_columns(self, columns: int) -> None: ...
    def set_cursor(
        self, path: TreePath, cell: Optional[CellRenderer], start_editing: bool
    ) -> None: ...
    def set_drag_dest_item(
        self, path: Optional[TreePath], pos: IconViewDropPosition
    ) -> None: ...
    def set_item_orientation(self, orientation: Orientation) -> None: ...
    def set_item_padding(self, item_padding: int) -> None: ...
    def set_item_width(self, item_width: int) -> None: ...
    def set_margin(self, margin: int) -> None: ...
    def set_markup_column(self, column: int) -> None: ...
    def set_model(self, model: Optional[TreeModel] = None) -> None: ...
    def set_pixbuf_column(self, column: int) -> None: ...
    def set_reorderable(self, reorderable: bool) -> None: ...
    def set_row_spacing(self, row_spacing: int) -> None: ...
    def set_selection_mode(self, mode: SelectionMode) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...
    def set_text_column(self, column: int) -> None: ...
    def set_tooltip_cell(
        self, tooltip: Tooltip, path: TreePath, cell: Optional[CellRenderer] = None
    ) -> None: ...
    def set_tooltip_column(self, column: int) -> None: ...
    def set_tooltip_item(self, tooltip: Tooltip, path: TreePath) -> None: ...
    def unselect_all(self) -> None: ...
    def unselect_path(self, path: TreePath) -> None: ...
    def unset_model_drag_dest(self) -> None: ...
    def unset_model_drag_source(self) -> None: ...

class Image(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        file: str
        gicon: Gio.Icon
        icon_name: str
        icon_size: IconSize
        paintable: Gdk.Paintable
        pixel_size: int
        resource: str
        storage_type: ImageType
        use_fallback: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        file: str = ...,
        gicon: Gio.Icon = ...,
        icon_name: str = ...,
        icon_size: IconSize = ...,
        paintable: Gdk.Paintable = ...,
        pixel_size: int = ...,
        resource: str = ...,
        use_fallback: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def clear(self) -> None: ...
    def get_gicon(self) -> Optional[Gio.Icon]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_icon_size(self) -> IconSize: ...
    def get_paintable(self) -> Optional[Gdk.Paintable]: ...
    def get_pixel_size(self) -> int: ...
    def get_storage_type(self) -> ImageType: ...
    @classmethod
    def new(cls) -> Image: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Image: ...
    @classmethod
    def new_from_gicon(cls, icon: Gio.Icon) -> Image: ...
    @classmethod
    def new_from_icon_name(cls, icon_name: Optional[str] = None) -> Image: ...
    @classmethod
    def new_from_paintable(cls, paintable: Optional[Gdk.Paintable] = None) -> Image: ...
    @classmethod
    def new_from_pixbuf(cls, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> Image: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> Image: ...
    def set_from_file(self, filename: Optional[str] = None) -> None: ...
    def set_from_gicon(self, icon: Gio.Icon) -> None: ...
    def set_from_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_from_paintable(self, paintable: Optional[Gdk.Paintable] = None) -> None: ...
    def set_from_pixbuf(self, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> None: ...
    def set_from_resource(self, resource_path: Optional[str] = None) -> None: ...
    def set_icon_size(self, icon_size: IconSize) -> None: ...
    def set_pixel_size(self, pixel_size: int) -> None: ...

class InfoBar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        message_type: MessageType
        revealed: bool
        show_close_button: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        message_type: MessageType = ...,
        revealed: bool = ...,
        show_close_button: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_action_widget(self, child: Widget, response_id: int) -> None: ...
    def add_button(self, button_text: str, response_id: int) -> Button: ...
    def add_child(self, widget: Widget) -> None: ...
    def get_message_type(self) -> MessageType: ...
    def get_revealed(self) -> bool: ...
    def get_show_close_button(self) -> bool: ...
    @classmethod
    def new(cls) -> InfoBar: ...
    def remove_action_widget(self, widget: Widget) -> None: ...
    def remove_child(self, widget: Widget) -> None: ...
    def response(self, response_id: int) -> None: ...
    def set_default_response(self, response_id: int) -> None: ...
    def set_message_type(self, message_type: MessageType) -> None: ...
    def set_response_sensitive(self, response_id: int, setting: bool) -> None: ...
    def set_revealed(self, revealed: bool) -> None: ...
    def set_show_close_button(self, setting: bool) -> None: ...

class Inscription(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        attributes: Pango.AttrList
        markup: str
        min_chars: int
        min_lines: int
        nat_chars: int
        nat_lines: int
        text: str
        text_overflow: InscriptionOverflow
        wrap_mode: Pango.WrapMode
        xalign: float
        yalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        attributes: Pango.AttrList = ...,
        markup: str = ...,
        min_chars: int = ...,
        min_lines: int = ...,
        nat_chars: int = ...,
        nat_lines: int = ...,
        text: str = ...,
        text_overflow: InscriptionOverflow = ...,
        wrap_mode: Pango.WrapMode = ...,
        xalign: float = ...,
        yalign: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_attributes(self) -> Optional[Pango.AttrList]: ...
    def get_min_chars(self) -> int: ...
    def get_min_lines(self) -> int: ...
    def get_nat_chars(self) -> int: ...
    def get_nat_lines(self) -> int: ...
    def get_text(self) -> Optional[str]: ...
    def get_text_overflow(self) -> InscriptionOverflow: ...
    def get_wrap_mode(self) -> Pango.WrapMode: ...
    def get_xalign(self) -> float: ...
    def get_yalign(self) -> float: ...
    @classmethod
    def new(cls, text: Optional[str] = None) -> Inscription: ...
    def set_attributes(self, attrs: Optional[Pango.AttrList] = None) -> None: ...
    def set_markup(self, markup: Optional[str] = None) -> None: ...
    def set_min_chars(self, min_chars: int) -> None: ...
    def set_min_lines(self, min_lines: int) -> None: ...
    def set_nat_chars(self, nat_chars: int) -> None: ...
    def set_nat_lines(self, nat_lines: int) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...
    def set_text_overflow(self, overflow: InscriptionOverflow) -> None: ...
    def set_wrap_mode(self, wrap_mode: Pango.WrapMode) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...

class InscriptionClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class KeyvalTrigger(ShortcutTrigger):
    class Props:
        keyval: int
        modifiers: Gdk.ModifierType
    props: Props = ...
    def __init__(self, keyval: int = ..., modifiers: Gdk.ModifierType = ...): ...
    def get_keyval(self) -> int: ...
    def get_modifiers(self) -> Gdk.ModifierType: ...
    @classmethod
    def new(cls, keyval: int, modifiers: Gdk.ModifierType) -> KeyvalTrigger: ...

class KeyvalTriggerClass(GObject.GPointer): ...

class Label(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        attributes: Pango.AttrList
        ellipsize: Pango.EllipsizeMode
        extra_menu: Gio.MenuModel
        justify: Justification
        label: str
        lines: int
        max_width_chars: int
        mnemonic_keyval: int
        mnemonic_widget: Widget
        natural_wrap_mode: NaturalWrapMode
        selectable: bool
        single_line_mode: bool
        tabs: Pango.TabArray
        use_markup: bool
        use_underline: bool
        width_chars: int
        wrap: bool
        wrap_mode: Pango.WrapMode
        xalign: float
        yalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        attributes: Pango.AttrList = ...,
        ellipsize: Pango.EllipsizeMode = ...,
        extra_menu: Gio.MenuModel = ...,
        justify: Justification = ...,
        label: str = ...,
        lines: int = ...,
        max_width_chars: int = ...,
        mnemonic_widget: Widget = ...,
        natural_wrap_mode: NaturalWrapMode = ...,
        selectable: bool = ...,
        single_line_mode: bool = ...,
        tabs: Pango.TabArray = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        width_chars: int = ...,
        wrap: bool = ...,
        wrap_mode: Pango.WrapMode = ...,
        xalign: float = ...,
        yalign: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_attributes(self) -> Optional[Pango.AttrList]: ...
    def get_current_uri(self) -> Optional[str]: ...
    def get_ellipsize(self) -> Pango.EllipsizeMode: ...
    def get_extra_menu(self) -> Optional[Gio.MenuModel]: ...
    def get_justify(self) -> Justification: ...
    def get_label(self) -> str: ...
    def get_layout(self) -> Pango.Layout: ...
    def get_layout_offsets(self) -> Tuple[int, int]: ...
    def get_lines(self) -> int: ...
    def get_max_width_chars(self) -> int: ...
    def get_mnemonic_keyval(self) -> int: ...
    def get_mnemonic_widget(self) -> Optional[Widget]: ...
    def get_natural_wrap_mode(self) -> NaturalWrapMode: ...
    def get_selectable(self) -> bool: ...
    def get_selection_bounds(self) -> Tuple[bool, int, int]: ...
    def get_single_line_mode(self) -> bool: ...
    def get_tabs(self) -> Optional[Pango.TabArray]: ...
    def get_text(self) -> str: ...
    def get_use_markup(self) -> bool: ...
    def get_use_underline(self) -> bool: ...
    def get_width_chars(self) -> int: ...
    def get_wrap(self) -> bool: ...
    def get_wrap_mode(self) -> Pango.WrapMode: ...
    def get_xalign(self) -> float: ...
    def get_yalign(self) -> float: ...
    @classmethod
    def new(cls, str: Optional[str] = None) -> Label: ...
    @classmethod
    def new_with_mnemonic(cls, str: Optional[str] = None) -> Label: ...
    def select_region(self, start_offset: int, end_offset: int) -> None: ...
    def set_attributes(self, attrs: Optional[Pango.AttrList] = None) -> None: ...
    def set_ellipsize(self, mode: Pango.EllipsizeMode) -> None: ...
    def set_extra_menu(self, model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_justify(self, jtype: Justification) -> None: ...
    def set_label(self, str: str) -> None: ...
    def set_lines(self, lines: int) -> None: ...
    def set_markup(self, str: str) -> None: ...
    def set_markup_with_mnemonic(self, str: str) -> None: ...
    def set_max_width_chars(self, n_chars: int) -> None: ...
    def set_mnemonic_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_natural_wrap_mode(self, wrap_mode: NaturalWrapMode) -> None: ...
    def set_selectable(self, setting: bool) -> None: ...
    def set_single_line_mode(self, single_line_mode: bool) -> None: ...
    def set_tabs(self, tabs: Optional[Pango.TabArray] = None) -> None: ...
    def set_text(self, str: str) -> None: ...
    def set_text_with_mnemonic(self, str: str) -> None: ...
    def set_use_markup(self, setting: bool) -> None: ...
    def set_use_underline(self, setting: bool) -> None: ...
    def set_width_chars(self, n_chars: int) -> None: ...
    def set_wrap(self, wrap: bool) -> None: ...
    def set_wrap_mode(self, wrap_mode: Pango.WrapMode) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...

class LayoutChild(GObject.Object):
    class Props:
        child_widget: Widget
        layout_manager: LayoutManager
    props: Props = ...
    def __init__(
        self, child_widget: Widget = ..., layout_manager: LayoutManager = ...
    ): ...
    parent_instance: GObject.Object = ...
    def get_child_widget(self) -> Widget: ...
    def get_layout_manager(self) -> LayoutManager: ...

class LayoutChildClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class LayoutManager(GObject.Object):
    parent_instance: GObject.Object = ...
    def allocate(
        self, widget: Widget, width: int, height: int, baseline: int
    ) -> None: ...
    def do_allocate(
        self, widget: Widget, width: int, height: int, baseline: int
    ) -> None: ...
    def do_create_layout_child(
        self, widget: Widget, for_child: Widget
    ) -> LayoutChild: ...
    def do_get_request_mode(self, widget: Widget) -> SizeRequestMode: ...
    def do_measure(
        self, widget: Widget, orientation: Orientation, for_size: int
    ) -> Tuple[int, int, int, int]: ...
    def do_root(self) -> None: ...
    def do_unroot(self) -> None: ...
    def get_layout_child(self, child: Widget) -> LayoutChild: ...
    def get_request_mode(self) -> SizeRequestMode: ...
    def get_widget(self) -> Optional[Widget]: ...
    def layout_changed(self) -> None: ...
    def measure(
        self, widget: Widget, orientation: Orientation, for_size: int
    ) -> Tuple[int, int, int, int]: ...

class LayoutManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    get_request_mode: Callable[[LayoutManager, Widget], SizeRequestMode] = ...
    measure: Callable[
        [LayoutManager, Widget, Orientation, int], Tuple[int, int, int, int]
    ] = ...
    allocate: Callable[[LayoutManager, Widget, int, int, int], None] = ...
    layout_child_type: Type = ...
    create_layout_child: Callable[[LayoutManager, Widget, Widget], LayoutChild] = ...
    root: Callable[[LayoutManager], None] = ...
    unroot: Callable[[LayoutManager], None] = ...
    _padding: list[None] = ...

class LevelBar(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        inverted: bool
        max_value: float
        min_value: float
        mode: LevelBarMode
        value: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        inverted: bool = ...,
        max_value: float = ...,
        min_value: float = ...,
        mode: LevelBarMode = ...,
        value: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def add_offset_value(self, name: str, value: float) -> None: ...
    def get_inverted(self) -> bool: ...
    def get_max_value(self) -> float: ...
    def get_min_value(self) -> float: ...
    def get_mode(self) -> LevelBarMode: ...
    def get_offset_value(self, name: Optional[str] = None) -> Tuple[bool, float]: ...
    def get_value(self) -> float: ...
    @classmethod
    def new(cls) -> LevelBar: ...
    @classmethod
    def new_for_interval(cls, min_value: float, max_value: float) -> LevelBar: ...
    def remove_offset_value(self, name: Optional[str] = None) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_max_value(self, value: float) -> None: ...
    def set_min_value(self, value: float) -> None: ...
    def set_mode(self, mode: LevelBarMode) -> None: ...
    def set_value(self, value: float) -> None: ...

class LinkButton(Button, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        uri: str
        visited: bool
        child: Widget
        has_frame: bool
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        uri: str = ...,
        visited: bool = ...,
        child: Widget = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_uri(self) -> str: ...
    def get_visited(self) -> bool: ...
    @classmethod
    def new(cls, uri: str) -> LinkButton: ...
    @classmethod
    def new_with_label(cls, uri: str, label: Optional[str] = None) -> LinkButton: ...
    def set_uri(self, uri: str) -> None: ...
    def set_visited(self, visited: bool) -> None: ...

class ListBase(Widget, Accessible, Buildable, ConstraintTarget, Orientable, Scrollable):
    class Props:
        orientation: Orientation
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        orientation: Orientation = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...

class ListBaseClass(GObject.GPointer): ...

class ListBox(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        accept_unpaired_release: bool
        activate_on_single_click: bool
        selection_mode: SelectionMode
        show_separators: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        accept_unpaired_release: bool = ...,
        activate_on_single_click: bool = ...,
        selection_mode: SelectionMode = ...,
        show_separators: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def append(self, child: Widget) -> None: ...
    def bind_model(
        self,
        model: Optional[Gio.ListModel] = None,
        create_widget_func: Optional[Callable[..., Widget]] = None,
        *user_data: Any,
    ) -> None: ...
    def drag_highlight_row(self, row: ListBoxRow) -> None: ...
    def drag_unhighlight_row(self) -> None: ...
    def get_activate_on_single_click(self) -> bool: ...
    def get_adjustment(self) -> Optional[Adjustment]: ...
    def get_row_at_index(self, index_: int) -> Optional[ListBoxRow]: ...
    def get_row_at_y(self, y: int) -> Optional[ListBoxRow]: ...
    def get_selected_row(self) -> Optional[ListBoxRow]: ...
    def get_selected_rows(self) -> list[ListBoxRow]: ...
    def get_selection_mode(self) -> SelectionMode: ...
    def get_show_separators(self) -> bool: ...
    def insert(self, child: Widget, position: int) -> None: ...
    def invalidate_filter(self) -> None: ...
    def invalidate_headers(self) -> None: ...
    def invalidate_sort(self) -> None: ...
    @classmethod
    def new(cls) -> ListBox: ...
    def prepend(self, child: Widget) -> None: ...
    def remove(self, child: Widget) -> None: ...
    def select_all(self) -> None: ...
    def select_row(self, row: Optional[ListBoxRow] = None) -> None: ...
    def selected_foreach(self, func: Callable[..., None], *data: Any) -> None: ...
    def set_activate_on_single_click(self, single: bool) -> None: ...
    def set_adjustment(self, adjustment: Optional[Adjustment] = None) -> None: ...
    def set_filter_func(
        self, filter_func: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> None: ...
    def set_header_func(
        self, update_header: Optional[Callable[..., None]] = None, *user_data: Any
    ) -> None: ...
    def set_placeholder(self, placeholder: Optional[Widget] = None) -> None: ...
    def set_selection_mode(self, mode: SelectionMode) -> None: ...
    def set_show_separators(self, show_separators: bool) -> None: ...
    def set_sort_func(
        self, sort_func: Optional[Callable[..., int]] = None, *user_data: Any
    ) -> None: ...
    def unselect_all(self) -> None: ...
    def unselect_row(self, row: ListBoxRow) -> None: ...

class ListBoxRow(Widget, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        activatable: bool
        child: Widget
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        activatable: bool = ...,
        child: Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    parent_instance: Widget = ...
    def changed(self) -> None: ...
    def do_activate(self) -> None: ...
    def get_activatable(self) -> bool: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_header(self) -> Optional[Widget]: ...
    def get_index(self) -> int: ...
    def get_selectable(self) -> bool: ...
    def is_selected(self) -> bool: ...
    @classmethod
    def new(cls) -> ListBoxRow: ...
    def set_activatable(self, activatable: bool) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_header(self, header: Optional[Widget] = None) -> None: ...
    def set_selectable(self, selectable: bool) -> None: ...

class ListBoxRowClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    activate: Callable[[ListBoxRow], None] = ...
    padding: list[None] = ...

class ListItem(GObject.Object):
    class Props:
        activatable: bool
        child: Widget
        item: GObject.Object
        position: int
        selectable: bool
        selected: bool
    props: Props = ...
    def __init__(
        self, activatable: bool = ..., child: Widget = ..., selectable: bool = ...
    ): ...
    def get_activatable(self) -> bool: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_item(self) -> Optional[GObject.Object]: ...
    def get_position(self) -> int: ...
    def get_selectable(self) -> bool: ...
    def get_selected(self) -> bool: ...
    def set_activatable(self, activatable: bool) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_selectable(self, selectable: bool) -> None: ...

class ListItemClass(GObject.GPointer): ...
class ListItemFactory(GObject.Object): ...
class ListItemFactoryClass(GObject.GPointer): ...

class ListStore(
    GObject.Object, Buildable, TreeDragDest, TreeDragSource, TreeModel, TreeSortable
):
    parent: GObject.Object = ...
    priv: ListStorePrivate = ...
    def append(self, *args, **kwargs): ...  # FIXME Method
    def clear(self) -> None: ...
    def insert(self, *args, **kwargs): ...  # FIXME Method
    def insert_after(self, *args, **kwargs): ...  # FIXME Method
    def insert_before(self, *args, **kwargs): ...  # FIXME Method
    def insert_with_values(
        self, position: int, columns: Sequence[int], values: Sequence[Any]
    ) -> TreeIter: ...
    def insert_with_valuesv(
        self, position: int, columns: Sequence[int], values: Sequence[Any]
    ) -> TreeIter: ...
    def iter_is_valid(self, iter: TreeIter) -> bool: ...
    def move_after(
        self, iter: TreeIter, position: Optional[TreeIter] = None
    ) -> None: ...
    def move_before(
        self, iter: TreeIter, position: Optional[TreeIter] = None
    ) -> None: ...
    @classmethod
    def new(cls, n_columns: int, types: Sequence[Type]) -> ListStore: ...
    def prepend(self, *args, **kwargs): ...  # FIXME Method
    def remove(self, iter: TreeIter) -> bool: ...
    def reorder(self, new_order: Sequence[int]) -> None: ...
    def set(self, *args, **kwargs): ...  # FIXME Method
    def set_column_types(self, n_columns: int, types: Sequence[Type]) -> None: ...
    def set_value(self, *args, **kwargs): ...  # FIXME Method
    def swap(self, a: TreeIter, b: TreeIter) -> None: ...

class ListStoreClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class ListStorePrivate(GObject.GPointer): ...

class ListView(
    ListBase, Accessible, Buildable, ConstraintTarget, Orientable, Scrollable
):
    class Props:
        enable_rubberband: bool
        factory: ListItemFactory
        model: SelectionModel
        show_separators: bool
        single_click_activate: bool
        orientation: Orientation
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        enable_rubberband: bool = ...,
        factory: ListItemFactory = ...,
        model: SelectionModel = ...,
        show_separators: bool = ...,
        single_click_activate: bool = ...,
        orientation: Orientation = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    def get_enable_rubberband(self) -> bool: ...
    def get_factory(self) -> Optional[ListItemFactory]: ...
    def get_model(self) -> Optional[SelectionModel]: ...
    def get_show_separators(self) -> bool: ...
    def get_single_click_activate(self) -> bool: ...
    @classmethod
    def new(
        cls,
        model: Optional[SelectionModel] = None,
        factory: Optional[ListItemFactory] = None,
    ) -> ListView: ...
    def set_enable_rubberband(self, enable_rubberband: bool) -> None: ...
    def set_factory(self, factory: Optional[ListItemFactory] = None) -> None: ...
    def set_model(self, model: Optional[SelectionModel] = None) -> None: ...
    def set_show_separators(self, show_separators: bool) -> None: ...
    def set_single_click_activate(self, single_click_activate: bool) -> None: ...

class ListViewClass(GObject.GPointer): ...

class LockButton(Button, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        permission: Gio.Permission
        text_lock: str
        text_unlock: str
        tooltip_lock: str
        tooltip_not_authorized: str
        tooltip_unlock: str
        child: Widget
        has_frame: bool
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        permission: Gio.Permission = ...,
        text_lock: str = ...,
        text_unlock: str = ...,
        tooltip_lock: str = ...,
        tooltip_not_authorized: str = ...,
        tooltip_unlock: str = ...,
        child: Widget = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_permission(self) -> Optional[Gio.Permission]: ...
    @classmethod
    def new(cls, permission: Optional[Gio.Permission] = None) -> LockButton: ...
    def set_permission(self, permission: Optional[Gio.Permission] = None) -> None: ...

class MapListModel(GObject.Object, Gio.ListModel):
    class Props:
        has_map: bool
        item_type: Type
        model: Gio.ListModel
        n_items: int
    props: Props = ...
    def __init__(self, model: Gio.ListModel = ...): ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def has_map(self) -> bool: ...
    @classmethod
    def new(
        cls,
        model: Optional[Gio.ListModel] = None,
        map_func: Optional[Callable[..., GObject.Object]] = None,
        *user_data: Any,
    ) -> MapListModel: ...
    def set_map_func(
        self, map_func: Optional[Callable[..., GObject.Object]] = None, *user_data: Any
    ) -> None: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...

class MapListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class MediaControls(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        media_stream: MediaStream
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        media_stream: MediaStream = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_media_stream(self) -> Optional[MediaStream]: ...
    @classmethod
    def new(cls, stream: Optional[MediaStream] = None) -> MediaControls: ...
    def set_media_stream(self, stream: Optional[MediaStream] = None) -> None: ...

class MediaControlsClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class MediaFile(MediaStream, Gdk.Paintable):
    class Props:
        file: Gio.File
        input_stream: Gio.InputStream
        duration: int
        ended: bool
        error: GLib.Error
        has_audio: bool
        has_video: bool
        loop: bool
        muted: bool
        playing: bool
        prepared: bool
        seekable: bool
        seeking: bool
        timestamp: int
        volume: float
    props: Props = ...
    def __init__(
        self,
        file: Gio.File = ...,
        input_stream: Gio.InputStream = ...,
        loop: bool = ...,
        muted: bool = ...,
        playing: bool = ...,
        prepared: bool = ...,
        volume: float = ...,
    ): ...
    parent_instance: MediaStream = ...
    def clear(self) -> None: ...
    def do_close(self) -> None: ...
    def do_open(self) -> None: ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_input_stream(self) -> Optional[Gio.InputStream]: ...
    @classmethod
    def new(cls) -> MediaFile: ...
    @classmethod
    def new_for_file(cls, file: Gio.File) -> MediaFile: ...
    @classmethod
    def new_for_filename(cls, filename: str) -> MediaFile: ...
    @classmethod
    def new_for_input_stream(cls, stream: Gio.InputStream) -> MediaFile: ...
    @classmethod
    def new_for_resource(cls, resource_path: str) -> MediaFile: ...
    def set_file(self, file: Optional[Gio.File] = None) -> None: ...
    def set_filename(self, filename: Optional[str] = None) -> None: ...
    def set_input_stream(self, stream: Optional[Gio.InputStream] = None) -> None: ...
    def set_resource(self, resource_path: Optional[str] = None) -> None: ...

class MediaFileClass(GObject.GPointer):
    parent_class: MediaStreamClass = ...
    open: Callable[[MediaFile], None] = ...
    close: Callable[[MediaFile], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class MediaStream(GObject.Object, Gdk.Paintable):
    class Props:
        duration: int
        ended: bool
        error: GLib.Error
        has_audio: bool
        has_video: bool
        loop: bool
        muted: bool
        playing: bool
        prepared: bool
        seekable: bool
        seeking: bool
        timestamp: int
        volume: float
    props: Props = ...
    def __init__(
        self,
        loop: bool = ...,
        muted: bool = ...,
        playing: bool = ...,
        prepared: bool = ...,
        volume: float = ...,
    ): ...
    parent_instance: GObject.Object = ...
    def do_pause(self) -> None: ...
    def do_play(self) -> bool: ...
    def do_realize(self, surface: Gdk.Surface) -> None: ...
    def do_seek(self, timestamp: int) -> None: ...
    def do_unrealize(self, surface: Gdk.Surface) -> None: ...
    def do_update_audio(self, muted: bool, volume: float) -> None: ...
    def gerror(self, error: GLib.Error) -> None: ...
    def get_duration(self) -> int: ...
    def get_ended(self) -> bool: ...
    def get_error(self) -> Optional[GLib.Error]: ...
    def get_loop(self) -> bool: ...
    def get_muted(self) -> bool: ...
    def get_playing(self) -> bool: ...
    def get_timestamp(self) -> int: ...
    def get_volume(self) -> float: ...
    def has_audio(self) -> bool: ...
    def has_video(self) -> bool: ...
    def is_prepared(self) -> bool: ...
    def is_seekable(self) -> bool: ...
    def is_seeking(self) -> bool: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    def realize(self, surface: Gdk.Surface) -> None: ...
    def seek(self, timestamp: int) -> None: ...
    def seek_failed(self) -> None: ...
    def seek_success(self) -> None: ...
    def set_loop(self, loop: bool) -> None: ...
    def set_muted(self, muted: bool) -> None: ...
    def set_playing(self, playing: bool) -> None: ...
    def set_volume(self, volume: float) -> None: ...
    def stream_ended(self) -> None: ...
    def stream_prepared(
        self, has_audio: bool, has_video: bool, seekable: bool, duration: int
    ) -> None: ...
    def stream_unprepared(self) -> None: ...
    def unrealize(self, surface: Gdk.Surface) -> None: ...
    def update(self, timestamp: int) -> None: ...

class MediaStreamClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    play: Callable[[MediaStream], bool] = ...
    pause: Callable[[MediaStream], None] = ...
    seek: Callable[[MediaStream, int], None] = ...
    update_audio: Callable[[MediaStream, bool, float], None] = ...
    realize: Callable[[MediaStream, Gdk.Surface], None] = ...
    unrealize: Callable[[MediaStream, Gdk.Surface], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...
    _gtk_reserved5: None = ...
    _gtk_reserved6: None = ...
    _gtk_reserved7: None = ...
    _gtk_reserved8: None = ...

class MenuButton(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        always_show_arrow: bool
        child: Widget
        direction: ArrowType
        has_frame: bool
        icon_name: str
        label: str
        menu_model: Gio.MenuModel
        popover: Popover
        primary: bool
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        always_show_arrow: bool = ...,
        child: Widget = ...,
        direction: ArrowType = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        menu_model: Gio.MenuModel = ...,
        popover: Popover = ...,
        primary: bool = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_always_show_arrow(self) -> bool: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_direction(self) -> ArrowType: ...
    def get_has_frame(self) -> bool: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_label(self) -> Optional[str]: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    def get_popover(self) -> Optional[Popover]: ...
    def get_primary(self) -> bool: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> MenuButton: ...
    def popdown(self) -> None: ...
    def popup(self) -> None: ...
    def set_always_show_arrow(self, always_show_arrow: bool) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_create_popup_func(
        self, func: Optional[Callable[..., None]] = None, *user_data: Any
    ) -> None: ...
    def set_direction(self, direction: ArrowType) -> None: ...
    def set_has_frame(self, has_frame: bool) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_menu_model(self, menu_model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_popover(self, popover: Optional[Widget] = None) -> None: ...
    def set_primary(self, primary: bool) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class MessageDialog(
    Dialog, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        buttons: ButtonsType
        message_area: Widget
        message_type: MessageType
        secondary_text: str
        secondary_use_markup: bool
        text: str
        use_markup: bool
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        buttons: ButtonsType = ...,
        message_type: MessageType = ...,
        secondary_text: str = ...,
        secondary_use_markup: bool = ...,
        text: str = ...,
        use_markup: bool = ...,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Dialog = ...
    def get_message_area(self) -> Widget: ...
    def set_markup(self, str: str) -> None: ...

class MessageDialogClass(GObject.GPointer): ...

class MnemonicAction(ShortcutAction):
    @staticmethod
    def get() -> MnemonicAction: ...

class MnemonicActionClass(GObject.GPointer): ...

class MnemonicTrigger(ShortcutTrigger):
    class Props:
        keyval: int
    props: Props = ...
    def __init__(self, keyval: int = ...): ...
    def get_keyval(self) -> int: ...
    @classmethod
    def new(cls, keyval: int) -> MnemonicTrigger: ...

class MnemonicTriggerClass(GObject.GPointer): ...

class MountOperation(Gio.MountOperation):
    class Props:
        display: Gdk.Display
        is_showing: bool
        parent: Window
        anonymous: bool
        choice: int
        domain: str
        is_tcrypt_hidden_volume: bool
        is_tcrypt_system_volume: bool
        password: str
        password_save: Gio.PasswordSave
        pim: int
        username: str
    props: Props = ...
    def __init__(
        self,
        display: Gdk.Display = ...,
        parent: Window = ...,
        anonymous: bool = ...,
        choice: int = ...,
        domain: str = ...,
        is_tcrypt_hidden_volume: bool = ...,
        is_tcrypt_system_volume: bool = ...,
        password: str = ...,
        password_save: Gio.PasswordSave = ...,
        pim: int = ...,
        username: str = ...,
    ): ...
    parent_instance: Gio.MountOperation = ...
    priv: MountOperationPrivate = ...
    def get_display(self) -> Gdk.Display: ...
    def get_parent(self) -> Optional[Window]: ...
    def is_showing(self) -> bool: ...
    @classmethod
    def new(cls, parent: Optional[Window] = None) -> MountOperation: ...
    def set_display(self, display: Gdk.Display) -> None: ...
    def set_parent(self, parent: Optional[Window] = None) -> None: ...

class MountOperationClass(GObject.GPointer):
    parent_class: Gio.MountOperationClass = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class MountOperationPrivate(GObject.GPointer): ...

class MultiFilter(Filter, Gio.ListModel, Buildable):
    class Props:
        item_type: Type
        n_items: int
    props: Props = ...
    def append(self, filter: Filter) -> None: ...
    def remove(self, position: int) -> None: ...

class MultiFilterClass(GObject.GPointer): ...

class MultiSelection(GObject.Object, Gio.ListModel, SelectionModel):
    class Props:
        item_type: Type
        model: Gio.ListModel
        n_items: int
    props: Props = ...
    def __init__(self, model: Gio.ListModel = ...): ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    @classmethod
    def new(cls, model: Optional[Gio.ListModel] = None) -> MultiSelection: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...

class MultiSelectionClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class MultiSorter(Sorter, Gio.ListModel, Buildable):
    class Props:
        item_type: Type
        n_items: int
    props: Props = ...
    def append(self, sorter: Sorter) -> None: ...
    @classmethod
    def new(cls) -> MultiSorter: ...
    def remove(self, position: int) -> None: ...

class MultiSorterClass(GObject.GPointer):
    parent_class: SorterClass = ...

class NamedAction(ShortcutAction):
    class Props:
        action_name: str
    props: Props = ...
    def __init__(self, action_name: str = ...): ...
    def get_action_name(self) -> str: ...
    @classmethod
    def new(cls, name: str) -> NamedAction: ...

class NamedActionClass(GObject.GPointer): ...

class Native(GObject.Object):
    @staticmethod
    def get_for_surface(surface: Gdk.Surface) -> Optional[Native]: ...
    def get_renderer(self) -> Gsk.Renderer: ...
    def get_surface(self) -> Gdk.Surface: ...
    def get_surface_transform(self) -> Tuple[float, float]: ...
    def realize(self) -> None: ...
    def unrealize(self) -> None: ...

class NativeDialog(GObject.Object):
    class Props:
        modal: bool
        title: str
        transient_for: Window
        visible: bool
    props: Props = ...
    def __init__(
        self,
        modal: bool = ...,
        title: str = ...,
        transient_for: Window = ...,
        visible: bool = ...,
    ): ...
    parent_instance: GObject.Object = ...
    def destroy(self) -> None: ...
    def do_hide(self) -> None: ...
    def do_response(self, response_id: int) -> None: ...
    def do_show(self) -> None: ...
    def get_modal(self) -> bool: ...
    def get_title(self) -> Optional[str]: ...
    def get_transient_for(self) -> Optional[Window]: ...
    def get_visible(self) -> bool: ...
    def hide(self) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_transient_for(self, parent: Optional[Window] = None) -> None: ...
    def show(self) -> None: ...

class NativeDialogClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    response: Callable[[NativeDialog, int], None] = ...
    show: Callable[[NativeDialog], None] = ...
    hide: Callable[[NativeDialog], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class NativeInterface(GObject.GPointer): ...

class NeverTrigger(ShortcutTrigger):
    @staticmethod
    def get() -> NeverTrigger: ...

class NeverTriggerClass(GObject.GPointer): ...

class NoSelection(GObject.Object, Gio.ListModel, SelectionModel):
    class Props:
        item_type: Type
        model: Gio.ListModel
        n_items: int
    props: Props = ...
    def __init__(self, model: Gio.ListModel = ...): ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    @classmethod
    def new(cls, model: Optional[Gio.ListModel] = None) -> NoSelection: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...

class NoSelectionClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class Notebook(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        enable_popup: bool
        group_name: str
        page: int
        pages: Gio.ListModel
        scrollable: bool
        show_border: bool
        show_tabs: bool
        tab_pos: PositionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        enable_popup: bool = ...,
        group_name: str = ...,
        page: int = ...,
        scrollable: bool = ...,
        show_border: bool = ...,
        show_tabs: bool = ...,
        tab_pos: PositionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def append_page(self, child: Widget, tab_label: Optional[Widget] = None) -> int: ...
    def append_page_menu(
        self,
        child: Widget,
        tab_label: Optional[Widget] = None,
        menu_label: Optional[Widget] = None,
    ) -> int: ...
    def detach_tab(self, child: Widget) -> None: ...
    def get_action_widget(self, pack_type: PackType) -> Optional[Widget]: ...
    def get_current_page(self) -> int: ...
    def get_group_name(self) -> Optional[str]: ...
    def get_menu_label(self, child: Widget) -> Optional[Widget]: ...
    def get_menu_label_text(self, child: Widget) -> Optional[str]: ...
    def get_n_pages(self) -> int: ...
    def get_nth_page(self, page_num: int) -> Optional[Widget]: ...
    def get_page(self, child: Widget) -> NotebookPage: ...
    def get_pages(self) -> Gio.ListModel: ...
    def get_scrollable(self) -> bool: ...
    def get_show_border(self) -> bool: ...
    def get_show_tabs(self) -> bool: ...
    def get_tab_detachable(self, child: Widget) -> bool: ...
    def get_tab_label(self, child: Widget) -> Optional[Widget]: ...
    def get_tab_label_text(self, child: Widget) -> Optional[str]: ...
    def get_tab_pos(self) -> PositionType: ...
    def get_tab_reorderable(self, child: Widget) -> bool: ...
    def insert_page(
        self, child: Widget, tab_label: Optional[Widget], position: int
    ) -> int: ...
    def insert_page_menu(
        self,
        child: Widget,
        tab_label: Optional[Widget],
        menu_label: Optional[Widget],
        position: int,
    ) -> int: ...
    @classmethod
    def new(cls) -> Notebook: ...
    def next_page(self) -> None: ...
    def page_num(self, child: Widget) -> int: ...
    def popup_disable(self) -> None: ...
    def popup_enable(self) -> None: ...
    def prepend_page(
        self, child: Widget, tab_label: Optional[Widget] = None
    ) -> int: ...
    def prepend_page_menu(
        self,
        child: Widget,
        tab_label: Optional[Widget] = None,
        menu_label: Optional[Widget] = None,
    ) -> int: ...
    def prev_page(self) -> None: ...
    def remove_page(self, page_num: int) -> None: ...
    def reorder_child(self, child: Widget, position: int) -> None: ...
    def set_action_widget(self, widget: Widget, pack_type: PackType) -> None: ...
    def set_current_page(self, page_num: int) -> None: ...
    def set_group_name(self, group_name: Optional[str] = None) -> None: ...
    def set_menu_label(
        self, child: Widget, menu_label: Optional[Widget] = None
    ) -> None: ...
    def set_menu_label_text(self, child: Widget, menu_text: str) -> None: ...
    def set_scrollable(self, scrollable: bool) -> None: ...
    def set_show_border(self, show_border: bool) -> None: ...
    def set_show_tabs(self, show_tabs: bool) -> None: ...
    def set_tab_detachable(self, child: Widget, detachable: bool) -> None: ...
    def set_tab_label(
        self, child: Widget, tab_label: Optional[Widget] = None
    ) -> None: ...
    def set_tab_label_text(self, child: Widget, tab_text: str) -> None: ...
    def set_tab_pos(self, pos: PositionType) -> None: ...
    def set_tab_reorderable(self, child: Widget, reorderable: bool) -> None: ...

class NotebookPage(GObject.Object):
    class Props:
        child: Widget
        detachable: bool
        menu: Widget
        menu_label: str
        position: int
        reorderable: bool
        tab: Widget
        tab_expand: bool
        tab_fill: bool
        tab_label: str
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        detachable: bool = ...,
        menu: Widget = ...,
        menu_label: str = ...,
        position: int = ...,
        reorderable: bool = ...,
        tab: Widget = ...,
        tab_expand: bool = ...,
        tab_fill: bool = ...,
        tab_label: str = ...,
    ): ...
    def get_child(self) -> Widget: ...

class NothingAction(ShortcutAction):
    @staticmethod
    def get() -> NothingAction: ...

class NothingActionClass(GObject.GPointer): ...

class NumericSorter(Sorter):
    class Props:
        expression: Expression
        sort_order: SortType
    props: Props = ...
    def __init__(self, expression: Expression = ..., sort_order: SortType = ...): ...
    def get_expression(self) -> Optional[Expression]: ...
    def get_sort_order(self) -> SortType: ...
    @classmethod
    def new(cls, expression: Optional[Expression] = None) -> NumericSorter: ...
    def set_expression(self, expression: Optional[Expression] = None) -> None: ...
    def set_sort_order(self, sort_order: SortType) -> None: ...

class NumericSorterClass(GObject.GPointer):
    parent_class: SorterClass = ...

class ObjectExpression(Expression):
    def get_object(self) -> Optional[GObject.Object]: ...
    @classmethod
    def new(cls, object: GObject.Object) -> ObjectExpression: ...

class Orientable(GObject.Object):
    def get_orientation(self) -> Orientation: ...
    def set_orientation(self, orientation: Orientation) -> None: ...

class OrientableIface(GObject.GPointer):
    base_iface: GObject.TypeInterface = ...

class Overlay(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_overlay(self, widget: Widget) -> None: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_clip_overlay(self, widget: Widget) -> bool: ...
    def get_measure_overlay(self, widget: Widget) -> bool: ...
    @classmethod
    def new(cls) -> Overlay: ...
    def remove_overlay(self, widget: Widget) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_clip_overlay(self, widget: Widget, clip_overlay: bool) -> None: ...
    def set_measure_overlay(self, widget: Widget, measure: bool) -> None: ...

class OverlayLayout(LayoutManager):
    @classmethod
    def new(cls) -> OverlayLayout: ...

class OverlayLayoutChild(LayoutChild):
    class Props:
        clip_overlay: bool
        measure: bool
        child_widget: Widget
        layout_manager: LayoutManager
    props: Props = ...
    def __init__(
        self,
        clip_overlay: bool = ...,
        measure: bool = ...,
        child_widget: Widget = ...,
        layout_manager: LayoutManager = ...,
    ): ...
    def get_clip_overlay(self) -> bool: ...
    def get_measure(self) -> bool: ...
    def set_clip_overlay(self, clip_overlay: bool) -> None: ...
    def set_measure(self, measure: bool) -> None: ...

class OverlayLayoutChildClass(GObject.GPointer):
    parent_class: LayoutChildClass = ...

class OverlayLayoutClass(GObject.GPointer):
    parent_class: LayoutManagerClass = ...

class PadActionEntry(GObject.GPointer):
    type: PadActionType = ...
    index: int = ...
    mode: int = ...
    label: str = ...
    action_name: str = ...

class PadController(EventController):
    class Props:
        action_group: Gio.ActionGroup
        pad: Gdk.Device
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        action_group: Gio.ActionGroup = ...,
        pad: Gdk.Device = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    @classmethod
    def new(
        cls, group: Gio.ActionGroup, pad: Optional[Gdk.Device] = None
    ) -> PadController: ...
    def set_action(
        self, type: PadActionType, index: int, mode: int, label: str, action_name: str
    ) -> None: ...
    def set_action_entries(self, entries: Sequence[PadActionEntry]) -> None: ...

class PadControllerClass(GObject.GPointer): ...

class PageRange(GObject.GPointer):
    start: int = ...
    end: int = ...

class PageSetup(GObject.Object):
    def copy(self) -> PageSetup: ...
    def get_bottom_margin(self, unit: Unit) -> float: ...
    def get_left_margin(self, unit: Unit) -> float: ...
    def get_orientation(self) -> PageOrientation: ...
    def get_page_height(self, unit: Unit) -> float: ...
    def get_page_width(self, unit: Unit) -> float: ...
    def get_paper_height(self, unit: Unit) -> float: ...
    def get_paper_size(self) -> PaperSize: ...
    def get_paper_width(self, unit: Unit) -> float: ...
    def get_right_margin(self, unit: Unit) -> float: ...
    def get_top_margin(self, unit: Unit) -> float: ...
    def load_file(self, file_name: str) -> bool: ...
    def load_key_file(
        self, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> bool: ...
    @classmethod
    def new(cls) -> PageSetup: ...
    @classmethod
    def new_from_file(cls, file_name: str) -> PageSetup: ...
    @classmethod
    def new_from_gvariant(cls, variant: GLib.Variant) -> PageSetup: ...
    @classmethod
    def new_from_key_file(
        cls, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> PageSetup: ...
    def set_bottom_margin(self, margin: float, unit: Unit) -> None: ...
    def set_left_margin(self, margin: float, unit: Unit) -> None: ...
    def set_orientation(self, orientation: PageOrientation) -> None: ...
    def set_paper_size(self, size: PaperSize) -> None: ...
    def set_paper_size_and_default_margins(self, size: PaperSize) -> None: ...
    def set_right_margin(self, margin: float, unit: Unit) -> None: ...
    def set_top_margin(self, margin: float, unit: Unit) -> None: ...
    def to_file(self, file_name: str) -> bool: ...
    def to_gvariant(self) -> GLib.Variant: ...
    def to_key_file(
        self, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> None: ...

class PageSetupUnixDialog(
    Dialog, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_page_setup(self) -> PageSetup: ...
    def get_print_settings(self) -> Optional[PrintSettings]: ...
    @classmethod
    def new(
        cls, title: Optional[str] = None, parent: Optional[Window] = None
    ) -> PageSetupUnixDialog: ...
    def set_page_setup(self, page_setup: PageSetup) -> None: ...
    def set_print_settings(
        self, print_settings: Optional[PrintSettings] = None
    ) -> None: ...

class Paned(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        end_child: Widget
        max_position: int
        min_position: int
        position: int
        position_set: bool
        resize_end_child: bool
        resize_start_child: bool
        shrink_end_child: bool
        shrink_start_child: bool
        start_child: Widget
        wide_handle: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        end_child: Widget = ...,
        position: int = ...,
        position_set: bool = ...,
        resize_end_child: bool = ...,
        resize_start_child: bool = ...,
        shrink_end_child: bool = ...,
        shrink_start_child: bool = ...,
        start_child: Widget = ...,
        wide_handle: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def get_end_child(self) -> Optional[Widget]: ...
    def get_position(self) -> int: ...
    def get_resize_end_child(self) -> bool: ...
    def get_resize_start_child(self) -> bool: ...
    def get_shrink_end_child(self) -> bool: ...
    def get_shrink_start_child(self) -> bool: ...
    def get_start_child(self) -> Optional[Widget]: ...
    def get_wide_handle(self) -> bool: ...
    @classmethod
    def new(cls, orientation: Orientation) -> Paned: ...
    def set_end_child(self, child: Optional[Widget] = None) -> None: ...
    def set_position(self, position: int) -> None: ...
    def set_resize_end_child(self, resize: bool) -> None: ...
    def set_resize_start_child(self, resize: bool) -> None: ...
    def set_shrink_end_child(self, resize: bool) -> None: ...
    def set_shrink_start_child(self, resize: bool) -> None: ...
    def set_start_child(self, child: Optional[Widget] = None) -> None: ...
    def set_wide_handle(self, wide: bool) -> None: ...

class PaperSize(GObject.GBoxed):
    def copy(self) -> PaperSize: ...
    def free(self) -> None: ...
    @staticmethod
    def get_default() -> str: ...
    def get_default_bottom_margin(self, unit: Unit) -> float: ...
    def get_default_left_margin(self, unit: Unit) -> float: ...
    def get_default_right_margin(self, unit: Unit) -> float: ...
    def get_default_top_margin(self, unit: Unit) -> float: ...
    def get_display_name(self) -> str: ...
    def get_height(self, unit: Unit) -> float: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_paper_sizes(include_custom: bool) -> list[PaperSize]: ...
    def get_ppd_name(self) -> str: ...
    def get_width(self, unit: Unit) -> float: ...
    def is_custom(self) -> bool: ...
    def is_equal(self, size2: PaperSize) -> bool: ...
    def is_ipp(self) -> bool: ...
    @classmethod
    def new(cls, name: Optional[str] = None) -> PaperSize: ...
    @classmethod
    def new_custom(
        cls, name: str, display_name: str, width: float, height: float, unit: Unit
    ) -> PaperSize: ...
    @classmethod
    def new_from_gvariant(cls, variant: GLib.Variant) -> PaperSize: ...
    @classmethod
    def new_from_ipp(cls, ipp_name: str, width: float, height: float) -> PaperSize: ...
    @classmethod
    def new_from_key_file(
        cls, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> PaperSize: ...
    @classmethod
    def new_from_ppd(
        cls, ppd_name: str, ppd_display_name: str, width: float, height: float
    ) -> PaperSize: ...
    def set_size(self, width: float, height: float, unit: Unit) -> None: ...
    def to_gvariant(self) -> GLib.Variant: ...
    def to_key_file(self, key_file: GLib.KeyFile, group_name: str) -> None: ...

class ParamSpecExpression(GObject.ParamSpec):
    parent_instance: GObject.ParamSpec = ...

class PasswordEntry(Widget, Accessible, Buildable, ConstraintTarget, Editable):
    class Props:
        activates_default: bool
        extra_menu: Gio.MenuModel
        placeholder_text: str
        show_peek_icon: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
    props: Props = ...
    def __init__(
        self,
        activates_default: bool = ...,
        extra_menu: Gio.MenuModel = ...,
        placeholder_text: str = ...,
        show_peek_icon: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    def get_extra_menu(self) -> Optional[Gio.MenuModel]: ...
    def get_show_peek_icon(self) -> bool: ...
    @classmethod
    def new(cls) -> PasswordEntry: ...
    def set_extra_menu(self, model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_show_peek_icon(self, show_peek_icon: bool) -> None: ...

class PasswordEntryBuffer(EntryBuffer):
    class Props:
        length: int
        max_length: int
        text: str
    props: Props = ...
    def __init__(self, max_length: int = ..., text: str = ...): ...
    @classmethod
    def new(cls) -> PasswordEntryBuffer: ...

class PasswordEntryBufferClass(GObject.GPointer):
    parent_class: EntryBufferClass = ...

class PasswordEntryClass(GObject.GPointer): ...

class Picture(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        alternative_text: str
        can_shrink: bool
        content_fit: ContentFit
        file: Gio.File
        keep_aspect_ratio: bool
        paintable: Gdk.Paintable
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        alternative_text: str = ...,
        can_shrink: bool = ...,
        content_fit: ContentFit = ...,
        file: Gio.File = ...,
        keep_aspect_ratio: bool = ...,
        paintable: Gdk.Paintable = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_alternative_text(self) -> Optional[str]: ...
    def get_can_shrink(self) -> bool: ...
    def get_content_fit(self) -> ContentFit: ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_keep_aspect_ratio(self) -> bool: ...
    def get_paintable(self) -> Optional[Gdk.Paintable]: ...
    @classmethod
    def new(cls) -> Picture: ...
    @classmethod
    def new_for_file(cls, file: Optional[Gio.File] = None) -> Picture: ...
    @classmethod
    def new_for_filename(cls, filename: Optional[str] = None) -> Picture: ...
    @classmethod
    def new_for_paintable(
        cls, paintable: Optional[Gdk.Paintable] = None
    ) -> Picture: ...
    @classmethod
    def new_for_pixbuf(cls, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> Picture: ...
    @classmethod
    def new_for_resource(cls, resource_path: Optional[str] = None) -> Picture: ...
    def set_alternative_text(self, alternative_text: Optional[str] = None) -> None: ...
    def set_can_shrink(self, can_shrink: bool) -> None: ...
    def set_content_fit(self, content_fit: ContentFit) -> None: ...
    def set_file(self, file: Optional[Gio.File] = None) -> None: ...
    def set_filename(self, filename: Optional[str] = None) -> None: ...
    def set_keep_aspect_ratio(self, keep_aspect_ratio: bool) -> None: ...
    def set_paintable(self, paintable: Optional[Gdk.Paintable] = None) -> None: ...
    def set_pixbuf(self, pixbuf: Optional[GdkPixbuf.Pixbuf] = None) -> None: ...
    def set_resource(self, resource_path: Optional[str] = None) -> None: ...

class PictureClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class Popover(Widget, Accessible, Buildable, ConstraintTarget, Native, ShortcutManager):
    class Props:
        autohide: bool
        cascade_popdown: bool
        child: Widget
        default_widget: Widget
        has_arrow: bool
        mnemonics_visible: bool
        pointing_to: Gdk.Rectangle
        position: PositionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        autohide: bool = ...,
        cascade_popdown: bool = ...,
        child: Widget = ...,
        default_widget: Widget = ...,
        has_arrow: bool = ...,
        mnemonics_visible: bool = ...,
        pointing_to: Gdk.Rectangle = ...,
        position: PositionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent: Widget = ...
    def do_activate_default(self) -> None: ...
    def do_closed(self) -> None: ...
    def get_autohide(self) -> bool: ...
    def get_cascade_popdown(self) -> bool: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_has_arrow(self) -> bool: ...
    def get_mnemonics_visible(self) -> bool: ...
    def get_offset(self) -> Tuple[int, int]: ...
    def get_pointing_to(self) -> Tuple[bool, Gdk.Rectangle]: ...
    def get_position(self) -> PositionType: ...
    @classmethod
    def new(cls) -> Popover: ...
    def popdown(self) -> None: ...
    def popup(self) -> None: ...
    def present(self) -> None: ...
    def set_autohide(self, autohide: bool) -> None: ...
    def set_cascade_popdown(self, cascade_popdown: bool) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_default_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_has_arrow(self, has_arrow: bool) -> None: ...
    def set_mnemonics_visible(self, mnemonics_visible: bool) -> None: ...
    def set_offset(self, x_offset: int, y_offset: int) -> None: ...
    def set_pointing_to(self, rect: Optional[Gdk.Rectangle] = None) -> None: ...
    def set_position(self, position: PositionType) -> None: ...

class PopoverClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    closed: Callable[[Popover], None] = ...
    activate_default: Callable[[Popover], None] = ...
    reserved: list[None] = ...

class PopoverMenu(
    Popover, Accessible, Buildable, ConstraintTarget, Native, ShortcutManager
):
    class Props:
        menu_model: Gio.MenuModel
        visible_submenu: str
        autohide: bool
        cascade_popdown: bool
        child: Widget
        default_widget: Widget
        has_arrow: bool
        mnemonics_visible: bool
        pointing_to: Gdk.Rectangle
        position: PositionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        menu_model: Gio.MenuModel = ...,
        visible_submenu: str = ...,
        autohide: bool = ...,
        cascade_popdown: bool = ...,
        child: Widget = ...,
        default_widget: Widget = ...,
        has_arrow: bool = ...,
        mnemonics_visible: bool = ...,
        pointing_to: Gdk.Rectangle = ...,
        position: PositionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_child(self, child: Widget, id: str) -> bool: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    @classmethod
    def new_from_model(cls, model: Optional[Gio.MenuModel] = None) -> PopoverMenu: ...
    @classmethod
    def new_from_model_full(
        cls, model: Gio.MenuModel, flags: PopoverMenuFlags
    ) -> PopoverMenu: ...
    def remove_child(self, child: Widget) -> bool: ...
    def set_menu_model(self, model: Optional[Gio.MenuModel] = None) -> None: ...

class PopoverMenuBar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        menu_model: Gio.MenuModel
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        menu_model: Gio.MenuModel = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_child(self, child: Widget, id: str) -> bool: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    @classmethod
    def new_from_model(
        cls, model: Optional[Gio.MenuModel] = None
    ) -> PopoverMenuBar: ...
    def remove_child(self, child: Widget) -> bool: ...
    def set_menu_model(self, model: Optional[Gio.MenuModel] = None) -> None: ...

class PrintBackend(GObject.GPointer): ...

class PrintContext(GObject.Object):
    def create_pango_context(self) -> Pango.Context: ...
    def create_pango_layout(self) -> Pango.Layout: ...
    def get_cairo_context(self) -> cairo.Context: ...
    def get_dpi_x(self) -> float: ...
    def get_dpi_y(self) -> float: ...
    def get_hard_margins(self) -> Tuple[bool, float, float, float, float]: ...
    def get_height(self) -> float: ...
    def get_page_setup(self) -> PageSetup: ...
    def get_pango_fontmap(self) -> Pango.FontMap: ...
    def get_width(self) -> float: ...
    def set_cairo_context(
        self, cr: cairo.Context, dpi_x: float, dpi_y: float
    ) -> None: ...

class PrintJob(GObject.Object):
    class Props:
        page_setup: PageSetup
        printer: Printer
        settings: PrintSettings
        title: str
        track_print_status: bool
    props: Props = ...
    def __init__(
        self,
        page_setup: PageSetup = ...,
        printer: Printer = ...,
        settings: PrintSettings = ...,
        title: str = ...,
        track_print_status: bool = ...,
    ): ...
    def get_collate(self) -> bool: ...
    def get_n_up(self) -> int: ...
    def get_n_up_layout(self) -> NumberUpLayout: ...
    def get_num_copies(self) -> int: ...
    def get_page_ranges(self) -> list[PageRange]: ...
    def get_page_set(self) -> PageSet: ...
    def get_pages(self) -> PrintPages: ...
    def get_printer(self) -> Printer: ...
    def get_reverse(self) -> bool: ...
    def get_rotate(self) -> bool: ...
    def get_scale(self) -> float: ...
    def get_settings(self) -> PrintSettings: ...
    def get_status(self) -> PrintStatus: ...
    def get_surface(self) -> cairo.Surface: ...
    def get_title(self) -> str: ...
    def get_track_print_status(self) -> bool: ...
    @classmethod
    def new(
        cls,
        title: str,
        printer: Printer,
        settings: PrintSettings,
        page_setup: PageSetup,
    ) -> PrintJob: ...
    def send(self, callback: Callable[..., None], *user_data: Any) -> None: ...
    def set_collate(self, collate: bool) -> None: ...
    def set_n_up(self, n_up: int) -> None: ...
    def set_n_up_layout(self, layout: NumberUpLayout) -> None: ...
    def set_num_copies(self, num_copies: int) -> None: ...
    def set_page_ranges(self, ranges: Sequence[PageRange]) -> None: ...
    def set_page_set(self, page_set: PageSet) -> None: ...
    def set_pages(self, pages: PrintPages) -> None: ...
    def set_reverse(self, reverse: bool) -> None: ...
    def set_rotate(self, rotate: bool) -> None: ...
    def set_scale(self, scale: float) -> None: ...
    def set_source_fd(self, fd: int) -> bool: ...
    def set_source_file(self, filename: str) -> bool: ...
    def set_track_print_status(self, track_status: bool) -> None: ...

class PrintOperation(GObject.Object, PrintOperationPreview):
    class Props:
        allow_async: bool
        current_page: int
        custom_tab_label: str
        default_page_setup: PageSetup
        embed_page_setup: bool
        export_filename: str
        has_selection: bool
        job_name: str
        n_pages: int
        n_pages_to_print: int
        print_settings: PrintSettings
        show_progress: bool
        status: PrintStatus
        status_string: str
        support_selection: bool
        track_print_status: bool
        unit: Unit
        use_full_page: bool
    props: Props = ...
    def __init__(
        self,
        allow_async: bool = ...,
        current_page: int = ...,
        custom_tab_label: str = ...,
        default_page_setup: PageSetup = ...,
        embed_page_setup: bool = ...,
        export_filename: str = ...,
        has_selection: bool = ...,
        job_name: str = ...,
        n_pages: int = ...,
        print_settings: PrintSettings = ...,
        show_progress: bool = ...,
        support_selection: bool = ...,
        track_print_status: bool = ...,
        unit: Unit = ...,
        use_full_page: bool = ...,
    ): ...
    parent_instance: GObject.Object = ...
    priv: PrintOperationPrivate = ...
    def cancel(self) -> None: ...
    def do_begin_print(self, context: PrintContext) -> None: ...
    def do_custom_widget_apply(self, widget: Widget) -> None: ...
    def do_done(self, result: PrintOperationResult) -> None: ...
    def do_draw_page(self, context: PrintContext, page_nr: int) -> None: ...
    def do_end_print(self, context: PrintContext) -> None: ...
    def do_paginate(self, context: PrintContext) -> bool: ...
    def do_preview(
        self, preview: PrintOperationPreview, context: PrintContext, parent: Window
    ) -> bool: ...
    def do_request_page_setup(
        self, context: PrintContext, page_nr: int, setup: PageSetup
    ) -> None: ...
    def do_status_changed(self) -> None: ...
    def do_update_custom_widget(
        self, widget: Widget, setup: PageSetup, settings: PrintSettings
    ) -> None: ...
    def draw_page_finish(self) -> None: ...
    def get_default_page_setup(self) -> PageSetup: ...
    def get_embed_page_setup(self) -> bool: ...
    def get_error(self) -> None: ...
    def get_has_selection(self) -> bool: ...
    def get_n_pages_to_print(self) -> int: ...
    def get_print_settings(self) -> Optional[PrintSettings]: ...
    def get_status(self) -> PrintStatus: ...
    def get_status_string(self) -> str: ...
    def get_support_selection(self) -> bool: ...
    def is_finished(self) -> bool: ...
    @classmethod
    def new(cls) -> PrintOperation: ...
    def run(
        self, action: PrintOperationAction, parent: Optional[Window] = None
    ) -> PrintOperationResult: ...
    def set_allow_async(self, allow_async: bool) -> None: ...
    def set_current_page(self, current_page: int) -> None: ...
    def set_custom_tab_label(self, label: Optional[str] = None) -> None: ...
    def set_default_page_setup(
        self, default_page_setup: Optional[PageSetup] = None
    ) -> None: ...
    def set_defer_drawing(self) -> None: ...
    def set_embed_page_setup(self, embed: bool) -> None: ...
    def set_export_filename(self, filename: str) -> None: ...
    def set_has_selection(self, has_selection: bool) -> None: ...
    def set_job_name(self, job_name: str) -> None: ...
    def set_n_pages(self, n_pages: int) -> None: ...
    def set_print_settings(
        self, print_settings: Optional[PrintSettings] = None
    ) -> None: ...
    def set_show_progress(self, show_progress: bool) -> None: ...
    def set_support_selection(self, support_selection: bool) -> None: ...
    def set_track_print_status(self, track_status: bool) -> None: ...
    def set_unit(self, unit: Unit) -> None: ...
    def set_use_full_page(self, full_page: bool) -> None: ...

class PrintOperationClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    done: Callable[[PrintOperation, PrintOperationResult], None] = ...
    begin_print: Callable[[PrintOperation, PrintContext], None] = ...
    paginate: Callable[[PrintOperation, PrintContext], bool] = ...
    request_page_setup: Callable[
        [PrintOperation, PrintContext, int, PageSetup], None
    ] = ...
    draw_page: Callable[[PrintOperation, PrintContext, int], None] = ...
    end_print: Callable[[PrintOperation, PrintContext], None] = ...
    status_changed: Callable[[PrintOperation], None] = ...
    create_custom_widget: None = ...
    custom_widget_apply: Callable[[PrintOperation, Widget], None] = ...
    preview: Callable[
        [PrintOperation, PrintOperationPreview, PrintContext, Window], bool
    ] = ...
    update_custom_widget: Callable[
        [PrintOperation, Widget, PageSetup, PrintSettings], None
    ] = ...
    padding: list[None] = ...

class PrintOperationPreview(GObject.Object):
    def end_preview(self) -> None: ...
    def is_selected(self, page_nr: int) -> bool: ...
    def render_page(self, page_nr: int) -> None: ...

class PrintOperationPreviewIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    ready: Callable[[PrintOperationPreview, PrintContext], None] = ...
    got_page_size: Callable[
        [PrintOperationPreview, PrintContext, PageSetup], None
    ] = ...
    render_page: Callable[[PrintOperationPreview, int], None] = ...
    is_selected: Callable[[PrintOperationPreview, int], bool] = ...
    end_preview: Callable[[PrintOperationPreview], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...
    _gtk_reserved5: None = ...
    _gtk_reserved6: None = ...
    _gtk_reserved7: None = ...
    _gtk_reserved8: None = ...

class PrintOperationPrivate(GObject.GPointer): ...

class PrintSettings(GObject.Object):
    def copy(self) -> PrintSettings: ...
    def foreach(self, func: Callable[..., None], *user_data: Any) -> None: ...
    def get(self, key: str) -> Optional[str]: ...
    def get_bool(self, key: str) -> bool: ...
    def get_collate(self) -> bool: ...
    def get_default_source(self) -> Optional[str]: ...
    def get_dither(self) -> Optional[str]: ...
    def get_double(self, key: str) -> float: ...
    def get_double_with_default(self, key: str, def_: float) -> float: ...
    def get_duplex(self) -> PrintDuplex: ...
    def get_finishings(self) -> Optional[str]: ...
    def get_int(self, key: str) -> int: ...
    def get_int_with_default(self, key: str, def_: int) -> int: ...
    def get_length(self, key: str, unit: Unit) -> float: ...
    def get_media_type(self) -> Optional[str]: ...
    def get_n_copies(self) -> int: ...
    def get_number_up(self) -> int: ...
    def get_number_up_layout(self) -> NumberUpLayout: ...
    def get_orientation(self) -> PageOrientation: ...
    def get_output_bin(self) -> Optional[str]: ...
    def get_page_ranges(self) -> list[PageRange]: ...
    def get_page_set(self) -> PageSet: ...
    def get_paper_height(self, unit: Unit) -> float: ...
    def get_paper_size(self) -> Optional[PaperSize]: ...
    def get_paper_width(self, unit: Unit) -> float: ...
    def get_print_pages(self) -> PrintPages: ...
    def get_printer(self) -> Optional[str]: ...
    def get_printer_lpi(self) -> float: ...
    def get_quality(self) -> PrintQuality: ...
    def get_resolution(self) -> int: ...
    def get_resolution_x(self) -> int: ...
    def get_resolution_y(self) -> int: ...
    def get_reverse(self) -> bool: ...
    def get_scale(self) -> float: ...
    def get_use_color(self) -> bool: ...
    def has_key(self, key: str) -> bool: ...
    def load_file(self, file_name: str) -> bool: ...
    def load_key_file(
        self, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> bool: ...
    @classmethod
    def new(cls) -> PrintSettings: ...
    @classmethod
    def new_from_file(cls, file_name: str) -> PrintSettings: ...
    @classmethod
    def new_from_gvariant(cls, variant: GLib.Variant) -> PrintSettings: ...
    @classmethod
    def new_from_key_file(
        cls, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> PrintSettings: ...
    def set(self, key: str, value: Optional[str] = None) -> None: ...
    def set_bool(self, key: str, value: bool) -> None: ...
    def set_collate(self, collate: bool) -> None: ...
    def set_default_source(self, default_source: str) -> None: ...
    def set_dither(self, dither: str) -> None: ...
    def set_double(self, key: str, value: float) -> None: ...
    def set_duplex(self, duplex: PrintDuplex) -> None: ...
    def set_finishings(self, finishings: str) -> None: ...
    def set_int(self, key: str, value: int) -> None: ...
    def set_length(self, key: str, value: float, unit: Unit) -> None: ...
    def set_media_type(self, media_type: str) -> None: ...
    def set_n_copies(self, num_copies: int) -> None: ...
    def set_number_up(self, number_up: int) -> None: ...
    def set_number_up_layout(self, number_up_layout: NumberUpLayout) -> None: ...
    def set_orientation(self, orientation: PageOrientation) -> None: ...
    def set_output_bin(self, output_bin: str) -> None: ...
    def set_page_ranges(self, page_ranges: Sequence[PageRange]) -> None: ...
    def set_page_set(self, page_set: PageSet) -> None: ...
    def set_paper_height(self, height: float, unit: Unit) -> None: ...
    def set_paper_size(self, paper_size: PaperSize) -> None: ...
    def set_paper_width(self, width: float, unit: Unit) -> None: ...
    def set_print_pages(self, pages: PrintPages) -> None: ...
    def set_printer(self, printer: str) -> None: ...
    def set_printer_lpi(self, lpi: float) -> None: ...
    def set_quality(self, quality: PrintQuality) -> None: ...
    def set_resolution(self, resolution: int) -> None: ...
    def set_resolution_xy(self, resolution_x: int, resolution_y: int) -> None: ...
    def set_reverse(self, reverse: bool) -> None: ...
    def set_scale(self, scale: float) -> None: ...
    def set_use_color(self, use_color: bool) -> None: ...
    def to_file(self, file_name: str) -> bool: ...
    def to_gvariant(self) -> GLib.Variant: ...
    def to_key_file(
        self, key_file: GLib.KeyFile, group_name: Optional[str] = None
    ) -> None: ...
    def unset(self, key: str) -> None: ...

class PrintUnixDialog(
    Dialog, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        current_page: int
        embed_page_setup: bool
        has_selection: bool
        manual_capabilities: PrintCapabilities
        page_setup: PageSetup
        print_settings: PrintSettings
        selected_printer: Printer
        support_selection: bool
        use_header_bar: int
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        current_page: int = ...,
        embed_page_setup: bool = ...,
        has_selection: bool = ...,
        manual_capabilities: PrintCapabilities = ...,
        page_setup: PageSetup = ...,
        print_settings: PrintSettings = ...,
        support_selection: bool = ...,
        use_header_bar: int = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_custom_tab(self, child: Widget, tab_label: Widget) -> None: ...
    def get_current_page(self) -> int: ...
    def get_embed_page_setup(self) -> bool: ...
    def get_has_selection(self) -> bool: ...
    def get_manual_capabilities(self) -> PrintCapabilities: ...
    def get_page_setup(self) -> PageSetup: ...
    def get_page_setup_set(self) -> bool: ...
    def get_selected_printer(self) -> Optional[Printer]: ...
    def get_settings(self) -> PrintSettings: ...
    def get_support_selection(self) -> bool: ...
    @classmethod
    def new(
        cls, title: Optional[str] = None, parent: Optional[Window] = None
    ) -> PrintUnixDialog: ...
    def set_current_page(self, current_page: int) -> None: ...
    def set_embed_page_setup(self, embed: bool) -> None: ...
    def set_has_selection(self, has_selection: bool) -> None: ...
    def set_manual_capabilities(self, capabilities: PrintCapabilities) -> None: ...
    def set_page_setup(self, page_setup: PageSetup) -> None: ...
    def set_settings(self, settings: Optional[PrintSettings] = None) -> None: ...
    def set_support_selection(self, support_selection: bool) -> None: ...

class Printer(GObject.Object):
    class Props:
        accepting_jobs: bool
        accepts_pdf: bool
        accepts_ps: bool
        icon_name: str
        is_virtual: bool
        job_count: int
        location: str
        name: str
        paused: bool
        state_message: str
    props: Props = ...
    def __init__(
        self,
        accepts_pdf: bool = ...,
        accepts_ps: bool = ...,
        is_virtual: bool = ...,
        name: str = ...,
    ): ...
    def accepts_pdf(self) -> bool: ...
    def accepts_ps(self) -> bool: ...
    def compare(self, b: Printer) -> int: ...
    def get_backend(self) -> PrintBackend: ...
    def get_capabilities(self) -> PrintCapabilities: ...
    def get_default_page_size(self) -> PageSetup: ...
    def get_description(self) -> str: ...
    def get_hard_margins(self) -> Tuple[bool, float, float, float, float]: ...
    def get_hard_margins_for_paper_size(
        self, paper_size: PaperSize
    ) -> Tuple[bool, float, float, float, float]: ...
    def get_icon_name(self) -> str: ...
    def get_job_count(self) -> int: ...
    def get_location(self) -> str: ...
    def get_name(self) -> str: ...
    def get_state_message(self) -> str: ...
    def has_details(self) -> bool: ...
    def is_accepting_jobs(self) -> bool: ...
    def is_active(self) -> bool: ...
    def is_default(self) -> bool: ...
    def is_paused(self) -> bool: ...
    def is_virtual(self) -> bool: ...
    def list_papers(self) -> list[PageSetup]: ...
    @classmethod
    def new(cls, name: str, backend: PrintBackend, virtual_: bool) -> Printer: ...
    def request_details(self) -> None: ...

class ProgressBar(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        ellipsize: Pango.EllipsizeMode
        fraction: float
        inverted: bool
        pulse_step: float
        show_text: bool
        text: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        ellipsize: Pango.EllipsizeMode = ...,
        fraction: float = ...,
        inverted: bool = ...,
        pulse_step: float = ...,
        show_text: bool = ...,
        text: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def get_ellipsize(self) -> Pango.EllipsizeMode: ...
    def get_fraction(self) -> float: ...
    def get_inverted(self) -> bool: ...
    def get_pulse_step(self) -> float: ...
    def get_show_text(self) -> bool: ...
    def get_text(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> ProgressBar: ...
    def pulse(self) -> None: ...
    def set_ellipsize(self, mode: Pango.EllipsizeMode) -> None: ...
    def set_fraction(self, fraction: float) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_pulse_step(self, fraction: float) -> None: ...
    def set_show_text(self, show_text: bool) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...

class PropertyExpression(Expression):
    def get_expression(self) -> Optional[Expression]: ...
    def get_pspec(self) -> GObject.ParamSpec: ...
    @classmethod
    def new(
        cls, this_type: Type, expression: Optional[Expression], property_name: str
    ) -> PropertyExpression: ...
    @classmethod
    def new_for_pspec(
        cls, expression: Optional[Expression], pspec: GObject.ParamSpec
    ) -> PropertyExpression: ...

class PyGTKDeprecationWarning:
    args = ...  # FIXME Constant

    def add_note(self, *args, **kwargs): ...  # FIXME Method
    def with_traceback(self, *args, **kwargs): ...  # FIXME Method

class Range(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        adjustment: Adjustment
        fill_level: float
        inverted: bool
        restrict_to_fill_level: bool
        round_digits: int
        show_fill_level: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        adjustment: Adjustment = ...,
        fill_level: float = ...,
        inverted: bool = ...,
        restrict_to_fill_level: bool = ...,
        round_digits: int = ...,
        show_fill_level: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    parent_instance: Widget = ...
    def do_adjust_bounds(self, new_value: float) -> None: ...
    def do_change_value(self, scroll: ScrollType, new_value: float) -> bool: ...
    def do_get_range_border(self, border_: Border) -> None: ...
    def do_move_slider(self, scroll: ScrollType) -> None: ...
    def do_value_changed(self) -> None: ...
    def get_adjustment(self) -> Adjustment: ...
    def get_fill_level(self) -> float: ...
    def get_flippable(self) -> bool: ...
    def get_inverted(self) -> bool: ...
    def get_range_rect(self) -> Gdk.Rectangle: ...
    def get_restrict_to_fill_level(self) -> bool: ...
    def get_round_digits(self) -> int: ...
    def get_show_fill_level(self) -> bool: ...
    def get_slider_range(self) -> Tuple[int, int]: ...
    def get_slider_size_fixed(self) -> bool: ...
    def get_value(self) -> float: ...
    def set_adjustment(self, adjustment: Adjustment) -> None: ...
    def set_fill_level(self, fill_level: float) -> None: ...
    def set_flippable(self, flippable: bool) -> None: ...
    def set_increments(self, step: float, page: float) -> None: ...
    def set_inverted(self, setting: bool) -> None: ...
    def set_range(self, min: float, max: float) -> None: ...
    def set_restrict_to_fill_level(self, restrict_to_fill_level: bool) -> None: ...
    def set_round_digits(self, round_digits: int) -> None: ...
    def set_show_fill_level(self, show_fill_level: bool) -> None: ...
    def set_slider_size_fixed(self, size_fixed: bool) -> None: ...
    def set_value(self, value: float) -> None: ...

class RangeClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    value_changed: Callable[[Range], None] = ...
    adjust_bounds: Callable[[Range, float], None] = ...
    move_slider: Callable[[Range, ScrollType], None] = ...
    get_range_border: Callable[[Range, Border], None] = ...
    change_value: Callable[[Range, ScrollType, float], bool] = ...
    padding: list[None] = ...

class RecentData(GObject.GPointer):
    display_name: str = ...
    description: str = ...
    mime_type: str = ...
    app_name: str = ...
    app_exec: str = ...
    groups: list[str] = ...
    is_private: bool = ...

class RecentInfo(GObject.GBoxed):
    def create_app_info(
        self, app_name: Optional[str] = None
    ) -> Optional[Gio.AppInfo]: ...
    def exists(self) -> bool: ...
    def get_added(self) -> GLib.DateTime: ...
    def get_age(self) -> int: ...
    def get_application_info(self, *args, **kwargs): ...  # FIXME Method
    def get_applications(self) -> list[str]: ...
    def get_description(self) -> str: ...
    def get_display_name(self) -> str: ...
    def get_gicon(self) -> Optional[Gio.Icon]: ...
    def get_groups(self) -> list[str]: ...
    def get_mime_type(self) -> str: ...
    def get_modified(self) -> GLib.DateTime: ...
    def get_private_hint(self) -> bool: ...
    def get_short_name(self) -> str: ...
    def get_uri(self) -> str: ...
    def get_uri_display(self) -> Optional[str]: ...
    def get_visited(self) -> GLib.DateTime: ...
    def has_application(self, app_name: str) -> bool: ...
    def has_group(self, group_name: str) -> bool: ...
    def is_local(self) -> bool: ...
    def last_application(self) -> str: ...
    def match(self, info_b: RecentInfo) -> bool: ...
    def ref(self) -> RecentInfo: ...
    def unref(self) -> None: ...

class RecentManager(GObject.Object):
    class Props:
        filename: str
        size: int
    props: Props = ...
    def __init__(self, filename: str = ...): ...
    parent_instance: GObject.Object = ...
    priv: RecentManagerPrivate = ...
    def add_full(self, uri: str, recent_data: RecentData) -> bool: ...
    def add_item(self, uri: str) -> bool: ...
    def do_changed(self) -> None: ...
    @staticmethod
    def get_default() -> RecentManager: ...
    def get_items(self) -> list[RecentInfo]: ...
    def has_item(self, uri: str) -> bool: ...
    def lookup_item(self, uri: str) -> Optional[RecentInfo]: ...
    def move_item(self, uri: str, new_uri: Optional[str] = None) -> bool: ...
    @classmethod
    def new(cls) -> RecentManager: ...
    def purge_items(self) -> int: ...
    def remove_item(self, uri: str) -> bool: ...

class RecentManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    changed: Callable[[RecentManager], None] = ...
    _gtk_recent1: None = ...
    _gtk_recent2: None = ...
    _gtk_recent3: None = ...
    _gtk_recent4: None = ...

class RecentManagerPrivate(GObject.GPointer): ...

class RequestedSize(GObject.GPointer):
    data: None = ...
    minimum_size: int = ...
    natural_size: int = ...

class Requisition(GObject.GBoxed):
    width: int = ...
    height: int = ...
    def copy(self) -> Requisition: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls) -> Requisition: ...

class Revealer(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        child_revealed: bool
        reveal_child: bool
        transition_duration: int
        transition_type: RevealerTransitionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        reveal_child: bool = ...,
        transition_duration: int = ...,
        transition_type: RevealerTransitionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    def get_child_revealed(self) -> bool: ...
    def get_reveal_child(self) -> bool: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_type(self) -> RevealerTransitionType: ...
    @classmethod
    def new(cls) -> Revealer: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_reveal_child(self, reveal_child: bool) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: RevealerTransitionType) -> None: ...

class Root(GObject.Object):
    def get_display(self) -> Gdk.Display: ...
    def get_focus(self) -> Optional[Widget]: ...
    def set_focus(self, focus: Optional[Widget] = None) -> None: ...

class RootInterface(GObject.GPointer): ...

class Scale(Range, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        digits: int
        draw_value: bool
        has_origin: bool
        value_pos: PositionType
        adjustment: Adjustment
        fill_level: float
        inverted: bool
        restrict_to_fill_level: bool
        round_digits: int
        show_fill_level: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        digits: int = ...,
        draw_value: bool = ...,
        has_origin: bool = ...,
        value_pos: PositionType = ...,
        adjustment: Adjustment = ...,
        fill_level: float = ...,
        inverted: bool = ...,
        restrict_to_fill_level: bool = ...,
        round_digits: int = ...,
        show_fill_level: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    parent_instance: Range = ...
    def add_mark(
        self, value: float, position: PositionType, markup: Optional[str] = None
    ) -> None: ...
    def clear_marks(self) -> None: ...
    def do_get_layout_offsets(self) -> Tuple[int, int]: ...
    def get_digits(self) -> int: ...
    def get_draw_value(self) -> bool: ...
    def get_has_origin(self) -> bool: ...
    def get_layout(self) -> Optional[Pango.Layout]: ...
    def get_layout_offsets(self) -> Tuple[int, int]: ...
    def get_value_pos(self) -> PositionType: ...
    @classmethod
    def new(
        cls, orientation: Orientation, adjustment: Optional[Adjustment] = None
    ) -> Scale: ...
    @classmethod
    def new_with_range(
        cls, orientation: Orientation, min: float, max: float, step: float
    ) -> Scale: ...
    def set_digits(self, digits: int) -> None: ...
    def set_draw_value(self, draw_value: bool) -> None: ...
    def set_format_value_func(
        self, func: Optional[Callable[..., str]] = None, *user_data: Any
    ) -> None: ...
    def set_has_origin(self, has_origin: bool) -> None: ...
    def set_value_pos(self, pos: PositionType) -> None: ...

class ScaleButton(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        adjustment: Adjustment
        icons: list[str]
        value: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        adjustment: Adjustment = ...,
        icons: Sequence[str] = ...,
        value: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    parent_instance: Widget = ...
    def do_value_changed(self, value: float) -> None: ...
    def get_adjustment(self) -> Adjustment: ...
    def get_minus_button(self) -> Button: ...
    def get_plus_button(self) -> Button: ...
    def get_popup(self) -> Widget: ...
    def get_value(self) -> float: ...
    @classmethod
    def new(
        cls, min: float, max: float, step: float, icons: Optional[Sequence[str]] = None
    ) -> ScaleButton: ...
    def set_adjustment(self, adjustment: Adjustment) -> None: ...
    def set_icons(self, icons: Sequence[str]) -> None: ...
    def set_value(self, value: float) -> None: ...

class ScaleButtonClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    value_changed: Callable[[ScaleButton, float], None] = ...
    padding: list[None] = ...

class ScaleClass(GObject.GPointer):
    parent_class: RangeClass = ...
    get_layout_offsets: Callable[[Scale], Tuple[int, int]] = ...
    padding: list[None] = ...

class Scrollable(GObject.Object):
    def get_border(self) -> Tuple[bool, Border]: ...
    def get_hadjustment(self) -> Optional[Adjustment]: ...
    def get_hscroll_policy(self) -> ScrollablePolicy: ...
    def get_vadjustment(self) -> Optional[Adjustment]: ...
    def get_vscroll_policy(self) -> ScrollablePolicy: ...
    def set_hadjustment(self, hadjustment: Optional[Adjustment] = None) -> None: ...
    def set_hscroll_policy(self, policy: ScrollablePolicy) -> None: ...
    def set_vadjustment(self, vadjustment: Optional[Adjustment] = None) -> None: ...
    def set_vscroll_policy(self, policy: ScrollablePolicy) -> None: ...

class ScrollableInterface(GObject.GPointer):
    base_iface: GObject.TypeInterface = ...
    get_border: Callable[[Scrollable], Tuple[bool, Border]] = ...

class Scrollbar(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        adjustment: Adjustment
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        adjustment: Adjustment = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def get_adjustment(self) -> Adjustment: ...
    @classmethod
    def new(
        cls, orientation: Orientation, adjustment: Optional[Adjustment] = None
    ) -> Scrollbar: ...
    def set_adjustment(self, adjustment: Optional[Adjustment] = None) -> None: ...

class ScrolledWindow(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        hadjustment: Adjustment
        has_frame: bool
        hscrollbar_policy: PolicyType
        kinetic_scrolling: bool
        max_content_height: int
        max_content_width: int
        min_content_height: int
        min_content_width: int
        overlay_scrolling: bool
        propagate_natural_height: bool
        propagate_natural_width: bool
        vadjustment: Adjustment
        vscrollbar_policy: PolicyType
        window_placement: CornerType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        hadjustment: Adjustment = ...,
        has_frame: bool = ...,
        hscrollbar_policy: PolicyType = ...,
        kinetic_scrolling: bool = ...,
        max_content_height: int = ...,
        max_content_width: int = ...,
        min_content_height: int = ...,
        min_content_width: int = ...,
        overlay_scrolling: bool = ...,
        propagate_natural_height: bool = ...,
        propagate_natural_width: bool = ...,
        vadjustment: Adjustment = ...,
        vscrollbar_policy: PolicyType = ...,
        window_placement: CornerType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    def get_hadjustment(self) -> Adjustment: ...
    def get_has_frame(self) -> bool: ...
    def get_hscrollbar(self) -> Widget: ...
    def get_kinetic_scrolling(self) -> bool: ...
    def get_max_content_height(self) -> int: ...
    def get_max_content_width(self) -> int: ...
    def get_min_content_height(self) -> int: ...
    def get_min_content_width(self) -> int: ...
    def get_overlay_scrolling(self) -> bool: ...
    def get_placement(self) -> CornerType: ...
    def get_policy(self) -> Tuple[PolicyType, PolicyType]: ...
    def get_propagate_natural_height(self) -> bool: ...
    def get_propagate_natural_width(self) -> bool: ...
    def get_vadjustment(self) -> Adjustment: ...
    def get_vscrollbar(self) -> Widget: ...
    @classmethod
    def new(cls) -> ScrolledWindow: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_hadjustment(self, hadjustment: Optional[Adjustment] = None) -> None: ...
    def set_has_frame(self, has_frame: bool) -> None: ...
    def set_kinetic_scrolling(self, kinetic_scrolling: bool) -> None: ...
    def set_max_content_height(self, height: int) -> None: ...
    def set_max_content_width(self, width: int) -> None: ...
    def set_min_content_height(self, height: int) -> None: ...
    def set_min_content_width(self, width: int) -> None: ...
    def set_overlay_scrolling(self, overlay_scrolling: bool) -> None: ...
    def set_placement(self, window_placement: CornerType) -> None: ...
    def set_policy(
        self, hscrollbar_policy: PolicyType, vscrollbar_policy: PolicyType
    ) -> None: ...
    def set_propagate_natural_height(self, propagate: bool) -> None: ...
    def set_propagate_natural_width(self, propagate: bool) -> None: ...
    def set_vadjustment(self, vadjustment: Optional[Adjustment] = None) -> None: ...
    def unset_placement(self) -> None: ...

class SearchBar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        key_capture_widget: Widget
        search_mode_enabled: bool
        show_close_button: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        key_capture_widget: Widget = ...,
        search_mode_enabled: bool = ...,
        show_close_button: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def connect_entry(self, entry: Editable) -> None: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_key_capture_widget(self) -> Optional[Widget]: ...
    def get_search_mode(self) -> bool: ...
    def get_show_close_button(self) -> bool: ...
    @classmethod
    def new(cls) -> SearchBar: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_key_capture_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_search_mode(self, search_mode: bool) -> None: ...
    def set_show_close_button(self, visible: bool) -> None: ...

class SearchEntry(Widget, Accessible, Buildable, ConstraintTarget, Editable):
    class Props:
        activates_default: bool
        placeholder_text: str
        search_delay: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
    props: Props = ...
    def __init__(
        self,
        activates_default: bool = ...,
        placeholder_text: str = ...,
        search_delay: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    def get_key_capture_widget(self) -> Optional[Widget]: ...
    def get_search_delay(self) -> int: ...
    @classmethod
    def new(cls) -> SearchEntry: ...
    def set_key_capture_widget(self, widget: Optional[Widget] = None) -> None: ...
    def set_search_delay(self, delay: int) -> None: ...

class SelectionFilterModel(GObject.Object, Gio.ListModel):
    class Props:
        item_type: Type
        model: SelectionModel
        n_items: int
    props: Props = ...
    def __init__(self, model: SelectionModel = ...): ...
    def get_model(self) -> Optional[SelectionModel]: ...
    @classmethod
    def new(cls, model: Optional[SelectionModel] = None) -> SelectionFilterModel: ...
    def set_model(self, model: Optional[SelectionModel] = None) -> None: ...

class SelectionFilterModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class SelectionModel(GObject.Object):
    def get_selection(self) -> Bitset: ...
    def get_selection_in_range(self, position: int, n_items: int) -> Bitset: ...
    def is_selected(self, position: int) -> bool: ...
    def select_all(self) -> bool: ...
    def select_item(self, position: int, unselect_rest: bool) -> bool: ...
    def select_range(
        self, position: int, n_items: int, unselect_rest: bool
    ) -> bool: ...
    def selection_changed(self, position: int, n_items: int) -> None: ...
    def set_selection(self, selected: Bitset, mask: Bitset) -> bool: ...
    def unselect_all(self) -> bool: ...
    def unselect_item(self, position: int) -> bool: ...
    def unselect_range(self, position: int, n_items: int) -> bool: ...

class SelectionModelInterface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    is_selected: Callable[[SelectionModel, int], bool] = ...
    get_selection_in_range: Callable[[SelectionModel, int, int], Bitset] = ...
    select_item: Callable[[SelectionModel, int, bool], bool] = ...
    unselect_item: Callable[[SelectionModel, int], bool] = ...
    select_range: Callable[[SelectionModel, int, int, bool], bool] = ...
    unselect_range: Callable[[SelectionModel, int, int], bool] = ...
    select_all: Callable[[SelectionModel], bool] = ...
    unselect_all: Callable[[SelectionModel], bool] = ...
    set_selection: Callable[[SelectionModel, Bitset, Bitset], bool] = ...

class Separator(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    @classmethod
    def new(cls, orientation: Orientation) -> Separator: ...

class Settings(GObject.Object, StyleProvider):
    class Props:
        gtk_alternative_button_order: bool
        gtk_alternative_sort_arrows: bool
        gtk_application_prefer_dark_theme: bool
        gtk_cursor_aspect_ratio: float
        gtk_cursor_blink: bool
        gtk_cursor_blink_time: int
        gtk_cursor_blink_timeout: int
        gtk_cursor_theme_name: str
        gtk_cursor_theme_size: int
        gtk_decoration_layout: str
        gtk_dialogs_use_header: bool
        gtk_dnd_drag_threshold: int
        gtk_double_click_distance: int
        gtk_double_click_time: int
        gtk_enable_accels: bool
        gtk_enable_animations: bool
        gtk_enable_event_sounds: bool
        gtk_enable_input_feedback_sounds: bool
        gtk_enable_primary_paste: bool
        gtk_entry_password_hint_timeout: int
        gtk_entry_select_on_focus: bool
        gtk_error_bell: bool
        gtk_font_name: str
        gtk_fontconfig_timestamp: int
        gtk_hint_font_metrics: bool
        gtk_icon_theme_name: str
        gtk_im_module: str
        gtk_keynav_use_caret: bool
        gtk_label_select_on_focus: bool
        gtk_long_press_time: int
        gtk_overlay_scrolling: bool
        gtk_primary_button_warps_slider: bool
        gtk_print_backends: str
        gtk_print_preview_command: str
        gtk_recent_files_enabled: bool
        gtk_recent_files_max_age: int
        gtk_shell_shows_app_menu: bool
        gtk_shell_shows_desktop: bool
        gtk_shell_shows_menubar: bool
        gtk_sound_theme_name: str
        gtk_split_cursor: bool
        gtk_theme_name: str
        gtk_titlebar_double_click: str
        gtk_titlebar_middle_click: str
        gtk_titlebar_right_click: str
        gtk_xft_antialias: int
        gtk_xft_dpi: int
        gtk_xft_hinting: int
        gtk_xft_hintstyle: str
        gtk_xft_rgba: str
    props: Props = ...
    def __init__(
        self,
        gtk_alternative_button_order: bool = ...,
        gtk_alternative_sort_arrows: bool = ...,
        gtk_application_prefer_dark_theme: bool = ...,
        gtk_cursor_aspect_ratio: float = ...,
        gtk_cursor_blink: bool = ...,
        gtk_cursor_blink_time: int = ...,
        gtk_cursor_blink_timeout: int = ...,
        gtk_cursor_theme_name: str = ...,
        gtk_cursor_theme_size: int = ...,
        gtk_decoration_layout: str = ...,
        gtk_dialogs_use_header: bool = ...,
        gtk_dnd_drag_threshold: int = ...,
        gtk_double_click_distance: int = ...,
        gtk_double_click_time: int = ...,
        gtk_enable_accels: bool = ...,
        gtk_enable_animations: bool = ...,
        gtk_enable_event_sounds: bool = ...,
        gtk_enable_input_feedback_sounds: bool = ...,
        gtk_enable_primary_paste: bool = ...,
        gtk_entry_password_hint_timeout: int = ...,
        gtk_entry_select_on_focus: bool = ...,
        gtk_error_bell: bool = ...,
        gtk_font_name: str = ...,
        gtk_fontconfig_timestamp: int = ...,
        gtk_hint_font_metrics: bool = ...,
        gtk_icon_theme_name: str = ...,
        gtk_im_module: str = ...,
        gtk_keynav_use_caret: bool = ...,
        gtk_label_select_on_focus: bool = ...,
        gtk_long_press_time: int = ...,
        gtk_overlay_scrolling: bool = ...,
        gtk_primary_button_warps_slider: bool = ...,
        gtk_print_backends: str = ...,
        gtk_print_preview_command: str = ...,
        gtk_recent_files_enabled: bool = ...,
        gtk_recent_files_max_age: int = ...,
        gtk_shell_shows_app_menu: bool = ...,
        gtk_shell_shows_desktop: bool = ...,
        gtk_shell_shows_menubar: bool = ...,
        gtk_sound_theme_name: str = ...,
        gtk_split_cursor: bool = ...,
        gtk_theme_name: str = ...,
        gtk_titlebar_double_click: str = ...,
        gtk_titlebar_middle_click: str = ...,
        gtk_titlebar_right_click: str = ...,
        gtk_xft_antialias: int = ...,
        gtk_xft_dpi: int = ...,
        gtk_xft_hinting: int = ...,
        gtk_xft_hintstyle: str = ...,
        gtk_xft_rgba: str = ...,
    ): ...
    @staticmethod
    def get_default() -> Optional[Settings]: ...
    @staticmethod
    def get_for_display(display: Gdk.Display) -> Settings: ...
    def reset_property(self, name: str) -> None: ...

class Shortcut(GObject.Object):
    class Props:
        action: ShortcutAction
        arguments: GLib.Variant
        trigger: ShortcutTrigger
    props: Props = ...
    def __init__(
        self,
        action: ShortcutAction = ...,
        arguments: GLib.Variant = ...,
        trigger: ShortcutTrigger = ...,
    ): ...
    def get_action(self) -> Optional[ShortcutAction]: ...
    def get_arguments(self) -> Optional[GLib.Variant]: ...
    def get_trigger(self) -> Optional[ShortcutTrigger]: ...
    @classmethod
    def new(
        cls,
        trigger: Optional[ShortcutTrigger] = None,
        action: Optional[ShortcutAction] = None,
    ) -> Shortcut: ...
    def set_action(self, action: Optional[ShortcutAction] = None) -> None: ...
    def set_arguments(self, args: Optional[GLib.Variant] = None) -> None: ...
    def set_trigger(self, trigger: Optional[ShortcutTrigger] = None) -> None: ...

class ShortcutAction(GObject.Object):
    def activate(
        self,
        flags: ShortcutActionFlags,
        widget: Widget,
        args: Optional[GLib.Variant] = None,
    ) -> bool: ...
    @classmethod
    def parse_string(cls, string: str) -> Optional[ShortcutAction]: ...
    def print_(self, string: GLib.String) -> None: ...
    def to_string(self) -> str: ...

class ShortcutActionClass(GObject.GPointer): ...

class ShortcutClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class ShortcutController(EventController, Gio.ListModel, Buildable):
    class Props:
        item_type: Type
        mnemonic_modifiers: Gdk.ModifierType
        model: Gio.ListModel
        n_items: int
        scope: ShortcutScope
        name: str
        propagation_limit: PropagationLimit
        propagation_phase: PropagationPhase
        widget: Widget
    props: Props = ...
    def __init__(
        self,
        mnemonic_modifiers: Gdk.ModifierType = ...,
        model: Gio.ListModel = ...,
        scope: ShortcutScope = ...,
        name: str = ...,
        propagation_limit: PropagationLimit = ...,
        propagation_phase: PropagationPhase = ...,
    ): ...
    def add_shortcut(self, shortcut: Shortcut) -> None: ...
    def get_mnemonics_modifiers(self) -> Gdk.ModifierType: ...
    def get_scope(self) -> ShortcutScope: ...
    @classmethod
    def new(cls) -> ShortcutController: ...
    @classmethod
    def new_for_model(cls, model: Gio.ListModel) -> ShortcutController: ...
    def remove_shortcut(self, shortcut: Shortcut) -> None: ...
    def set_mnemonics_modifiers(self, modifiers: Gdk.ModifierType) -> None: ...
    def set_scope(self, scope: ShortcutScope) -> None: ...

class ShortcutControllerClass(GObject.GPointer): ...

class ShortcutLabel(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        accelerator: str
        disabled_text: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        accelerator: str = ...,
        disabled_text: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_accelerator(self) -> Optional[str]: ...
    def get_disabled_text(self) -> Optional[str]: ...
    @classmethod
    def new(cls, accelerator: str) -> ShortcutLabel: ...
    def set_accelerator(self, accelerator: str) -> None: ...
    def set_disabled_text(self, disabled_text: str) -> None: ...

class ShortcutLabelClass(GObject.GPointer): ...
class ShortcutManager(GObject.Object): ...

class ShortcutManagerInterface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    add_controller: Callable[[ShortcutManager, ShortcutController], None] = ...
    remove_controller: Callable[[ShortcutManager, ShortcutController], None] = ...

class ShortcutTrigger(GObject.Object):
    def compare(self, trigger2: ShortcutTrigger) -> int: ...
    def equal(self, trigger2: ShortcutTrigger) -> bool: ...
    def hash(self) -> int: ...
    @classmethod
    def parse_string(cls, string: str) -> Optional[ShortcutTrigger]: ...
    def print_(self, string: GLib.String) -> None: ...
    def print_label(self, display: Gdk.Display, string: GLib.String) -> bool: ...
    def to_label(self, display: Gdk.Display) -> str: ...
    def to_string(self) -> str: ...
    def trigger(self, event: Gdk.Event, enable_mnemonics: bool) -> Gdk.KeyMatch: ...

class ShortcutTriggerClass(GObject.GPointer): ...

class ShortcutsGroup(Box, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        accel_size_group: SizeGroup
        height: int
        title: str
        title_size_group: SizeGroup
        view: str
        baseline_position: BaselinePosition
        homogeneous: bool
        spacing: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        accel_size_group: SizeGroup = ...,
        title: str = ...,
        title_size_group: SizeGroup = ...,
        view: str = ...,
        baseline_position: BaselinePosition = ...,
        homogeneous: bool = ...,
        spacing: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...

class ShortcutsGroupClass(GObject.GPointer): ...

class ShortcutsSection(Box, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        max_height: int
        section_name: str
        title: str
        view_name: str
        baseline_position: BaselinePosition
        homogeneous: bool
        spacing: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        max_height: int = ...,
        section_name: str = ...,
        title: str = ...,
        view_name: str = ...,
        baseline_position: BaselinePosition = ...,
        homogeneous: bool = ...,
        spacing: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...

class ShortcutsSectionClass(GObject.GPointer): ...

class ShortcutsShortcut(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        accel_size_group: SizeGroup
        accelerator: str
        action_name: str
        direction: TextDirection
        icon: Gio.Icon
        icon_set: bool
        shortcut_type: ShortcutType
        subtitle: str
        subtitle_set: bool
        title: str
        title_size_group: SizeGroup
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        accel_size_group: SizeGroup = ...,
        accelerator: str = ...,
        action_name: str = ...,
        direction: TextDirection = ...,
        icon: Gio.Icon = ...,
        icon_set: bool = ...,
        shortcut_type: ShortcutType = ...,
        subtitle: str = ...,
        subtitle_set: bool = ...,
        title: str = ...,
        title_size_group: SizeGroup = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...

class ShortcutsShortcutClass(GObject.GPointer): ...

class ShortcutsWindow(
    Window, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        section_name: str
        view_name: str
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        section_name: str = ...,
        view_name: str = ...,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...

class SignalAction(ShortcutAction):
    class Props:
        signal_name: str
    props: Props = ...
    def __init__(self, signal_name: str = ...): ...
    def get_signal_name(self) -> str: ...
    @classmethod
    def new(cls, signal_name: str) -> SignalAction: ...

class SignalActionClass(GObject.GPointer): ...

class SignalListItemFactory(ListItemFactory):
    @classmethod
    def new(cls) -> SignalListItemFactory: ...

class SignalListItemFactoryClass(GObject.GPointer): ...

class SingleSelection(GObject.Object, Gio.ListModel, SelectionModel):
    class Props:
        autoselect: bool
        can_unselect: bool
        item_type: Type
        model: Gio.ListModel
        n_items: int
        selected: int
        selected_item: GObject.Object
    props: Props = ...
    def __init__(
        self,
        autoselect: bool = ...,
        can_unselect: bool = ...,
        model: Gio.ListModel = ...,
        selected: int = ...,
    ): ...
    def get_autoselect(self) -> bool: ...
    def get_can_unselect(self) -> bool: ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_selected(self) -> int: ...
    def get_selected_item(self) -> Optional[GObject.Object]: ...
    @classmethod
    def new(cls, model: Optional[Gio.ListModel] = None) -> SingleSelection: ...
    def set_autoselect(self, autoselect: bool) -> None: ...
    def set_can_unselect(self, can_unselect: bool) -> None: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...
    def set_selected(self, position: int) -> None: ...

class SingleSelectionClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class SizeGroup(GObject.Object, Buildable):
    class Props:
        mode: SizeGroupMode
    props: Props = ...
    def __init__(self, mode: SizeGroupMode = ...): ...
    parent_instance: GObject.Object = ...
    def add_widget(self, widget: Widget) -> None: ...
    def get_mode(self) -> SizeGroupMode: ...
    def get_widgets(self) -> list[Widget]: ...
    @classmethod
    def new(cls, mode: SizeGroupMode) -> SizeGroup: ...
    def remove_widget(self, widget: Widget) -> None: ...
    def set_mode(self, mode: SizeGroupMode) -> None: ...

class SliceListModel(GObject.Object, Gio.ListModel):
    class Props:
        item_type: Type
        model: Gio.ListModel
        n_items: int
        offset: int
        size: int
    props: Props = ...
    def __init__(
        self, model: Gio.ListModel = ..., offset: int = ..., size: int = ...
    ): ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_offset(self) -> int: ...
    def get_size(self) -> int: ...
    @classmethod
    def new(
        cls, model: Optional[Gio.ListModel], offset: int, size: int
    ) -> SliceListModel: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...
    def set_offset(self, offset: int) -> None: ...
    def set_size(self, size: int) -> None: ...

class SliceListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class Snapshot(Gdk.Snapshot):
    def append_border(
        self,
        outline: Gsk.RoundedRect,
        border_width: Sequence[float],
        border_color: Sequence[Gdk.RGBA],
    ) -> None: ...
    def append_cairo(self, bounds: Graphene.Rect) -> cairo.Context: ...
    def append_color(self, color: Gdk.RGBA, bounds: Graphene.Rect) -> None: ...
    def append_conic_gradient(
        self,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        rotation: float,
        stops: Sequence[Gsk.ColorStop],
    ) -> None: ...
    def append_inset_shadow(
        self,
        outline: Gsk.RoundedRect,
        color: Gdk.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> None: ...
    def append_layout(self, layout: Pango.Layout, color: Gdk.RGBA) -> None: ...
    def append_linear_gradient(
        self,
        bounds: Graphene.Rect,
        start_point: Graphene.Point,
        end_point: Graphene.Point,
        stops: Sequence[Gsk.ColorStop],
    ) -> None: ...
    def append_node(self, node: Gsk.RenderNode) -> None: ...
    def append_outset_shadow(
        self,
        outline: Gsk.RoundedRect,
        color: Gdk.RGBA,
        dx: float,
        dy: float,
        spread: float,
        blur_radius: float,
    ) -> None: ...
    def append_radial_gradient(
        self,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        hradius: float,
        vradius: float,
        start: float,
        end: float,
        stops: Sequence[Gsk.ColorStop],
    ) -> None: ...
    def append_repeating_linear_gradient(
        self,
        bounds: Graphene.Rect,
        start_point: Graphene.Point,
        end_point: Graphene.Point,
        stops: Sequence[Gsk.ColorStop],
    ) -> None: ...
    def append_repeating_radial_gradient(
        self,
        bounds: Graphene.Rect,
        center: Graphene.Point,
        hradius: float,
        vradius: float,
        start: float,
        end: float,
        stops: Sequence[Gsk.ColorStop],
    ) -> None: ...
    def append_texture(self, texture: Gdk.Texture, bounds: Graphene.Rect) -> None: ...
    def gl_shader_pop_texture(self) -> None: ...
    @classmethod
    def new(cls) -> Snapshot: ...
    def perspective(self, depth: float) -> None: ...
    def pop(self) -> None: ...
    def push_blend(self, blend_mode: Gsk.BlendMode) -> None: ...
    def push_blur(self, radius: float) -> None: ...
    def push_clip(self, bounds: Graphene.Rect) -> None: ...
    def push_color_matrix(
        self, color_matrix: Graphene.Matrix, color_offset: Graphene.Vec4
    ) -> None: ...
    def push_cross_fade(self, progress: float) -> None: ...
    def push_gl_shader(
        self, shader: Gsk.GLShader, bounds: Graphene.Rect, take_args: GLib.Bytes
    ) -> None: ...
    def push_opacity(self, opacity: float) -> None: ...
    def push_repeat(
        self, bounds: Graphene.Rect, child_bounds: Optional[Graphene.Rect] = None
    ) -> None: ...
    def push_rounded_clip(self, bounds: Gsk.RoundedRect) -> None: ...
    def push_shadow(self, shadow: Sequence[Gsk.Shadow]) -> None: ...
    def render_background(
        self, context: StyleContext, x: float, y: float, width: float, height: float
    ) -> None: ...
    def render_focus(
        self, context: StyleContext, x: float, y: float, width: float, height: float
    ) -> None: ...
    def render_frame(
        self, context: StyleContext, x: float, y: float, width: float, height: float
    ) -> None: ...
    def render_insertion_cursor(
        self,
        context: StyleContext,
        x: float,
        y: float,
        layout: Pango.Layout,
        index: int,
        direction: Pango.Direction,
    ) -> None: ...
    def render_layout(
        self, context: StyleContext, x: float, y: float, layout: Pango.Layout
    ) -> None: ...
    def restore(self) -> None: ...
    def rotate(self, angle: float) -> None: ...
    def rotate_3d(self, angle: float, axis: Graphene.Vec3) -> None: ...
    def save(self) -> None: ...
    def scale(self, factor_x: float, factor_y: float) -> None: ...
    def scale_3d(self, factor_x: float, factor_y: float, factor_z: float) -> None: ...
    def to_node(self) -> Optional[Gsk.RenderNode]: ...
    def to_paintable(
        self, size: Optional[Graphene.Size] = None
    ) -> Optional[Gdk.Paintable]: ...
    def transform(self, transform: Optional[Gsk.Transform] = None) -> None: ...
    def transform_matrix(self, matrix: Graphene.Matrix) -> None: ...
    def translate(self, point: Graphene.Point) -> None: ...
    def translate_3d(self, point: Graphene.Point3D) -> None: ...

class SnapshotClass(GObject.GPointer): ...

class SortListModel(GObject.Object, Gio.ListModel):
    class Props:
        incremental: bool
        item_type: Type
        model: Gio.ListModel
        n_items: int
        pending: int
        sorter: Sorter
    props: Props = ...
    def __init__(
        self, incremental: bool = ..., model: Gio.ListModel = ..., sorter: Sorter = ...
    ): ...
    def get_incremental(self) -> bool: ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_pending(self) -> int: ...
    def get_sorter(self) -> Optional[Sorter]: ...
    @classmethod
    def new(
        cls, model: Optional[Gio.ListModel] = None, sorter: Optional[Sorter] = None
    ) -> SortListModel: ...
    def set_incremental(self, incremental: bool) -> None: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...
    def set_sorter(self, sorter: Optional[Sorter] = None) -> None: ...

class SortListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class Sorter(GObject.Object):
    parent_instance: GObject.Object = ...
    def changed(self, change: SorterChange) -> None: ...
    def compare(self, item1: GObject.Object, item2: GObject.Object) -> Ordering: ...
    def do_compare(
        self,
        item1: Optional[GObject.Object] = None,
        item2: Optional[GObject.Object] = None,
    ) -> Ordering: ...
    def do_get_order(self) -> SorterOrder: ...
    def get_order(self) -> SorterOrder: ...

class SorterClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    compare: Callable[
        [Sorter, Optional[GObject.Object], Optional[GObject.Object]], Ordering
    ] = ...
    get_order: Callable[[Sorter], SorterOrder] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...
    _gtk_reserved5: None = ...
    _gtk_reserved6: None = ...
    _gtk_reserved7: None = ...
    _gtk_reserved8: None = ...

class SpinButton(
    Widget, Accessible, Buildable, CellEditable, ConstraintTarget, Editable, Orientable
):
    class Props:
        adjustment: Adjustment
        climb_rate: float
        digits: int
        numeric: bool
        snap_to_ticks: bool
        update_policy: SpinButtonUpdatePolicy
        value: float
        wrap: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        editing_canceled: bool
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        adjustment: Adjustment = ...,
        climb_rate: float = ...,
        digits: int = ...,
        numeric: bool = ...,
        snap_to_ticks: bool = ...,
        update_policy: SpinButtonUpdatePolicy = ...,
        value: float = ...,
        wrap: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editing_canceled: bool = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
        orientation: Orientation = ...,
    ): ...
    def configure(
        self, adjustment: Optional[Adjustment], climb_rate: float, digits: int
    ) -> None: ...
    def get_adjustment(self) -> Adjustment: ...
    def get_climb_rate(self) -> float: ...
    def get_digits(self) -> int: ...
    def get_increments(self) -> Tuple[float, float]: ...
    def get_numeric(self) -> bool: ...
    def get_range(self) -> Tuple[float, float]: ...
    def get_snap_to_ticks(self) -> bool: ...
    def get_update_policy(self) -> SpinButtonUpdatePolicy: ...
    def get_value(self) -> float: ...
    def get_value_as_int(self) -> int: ...
    def get_wrap(self) -> bool: ...
    @classmethod
    def new(
        cls, adjustment: Optional[Adjustment], climb_rate: float, digits: int
    ) -> SpinButton: ...
    @classmethod
    def new_with_range(cls, min: float, max: float, step: float) -> SpinButton: ...
    def set_adjustment(self, adjustment: Adjustment) -> None: ...
    def set_climb_rate(self, climb_rate: float) -> None: ...
    def set_digits(self, digits: int) -> None: ...
    def set_increments(self, step: float, page: float) -> None: ...
    def set_numeric(self, numeric: bool) -> None: ...
    def set_range(self, min: float, max: float) -> None: ...
    def set_snap_to_ticks(self, snap_to_ticks: bool) -> None: ...
    def set_update_policy(self, policy: SpinButtonUpdatePolicy) -> None: ...
    def set_value(self, value: float) -> None: ...
    def set_wrap(self, wrap: bool) -> None: ...
    def spin(self, direction: SpinType, increment: float) -> None: ...
    def update(self) -> None: ...

class Spinner(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        spinning: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        spinning: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_spinning(self) -> bool: ...
    @classmethod
    def new(cls) -> Spinner: ...
    def set_spinning(self, spinning: bool) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class Stack(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        hhomogeneous: bool
        interpolate_size: bool
        pages: SelectionModel
        transition_duration: int
        transition_running: bool
        transition_type: StackTransitionType
        vhomogeneous: bool
        visible_child: Widget
        visible_child_name: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        hhomogeneous: bool = ...,
        interpolate_size: bool = ...,
        transition_duration: int = ...,
        transition_type: StackTransitionType = ...,
        vhomogeneous: bool = ...,
        visible_child: Widget = ...,
        visible_child_name: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def add_child(self, child: Widget) -> StackPage: ...
    def add_named(self, child: Widget, name: Optional[str] = None) -> StackPage: ...
    def add_titled(
        self, child: Widget, name: Optional[str], title: str
    ) -> StackPage: ...
    def get_child_by_name(self, name: str) -> Optional[Widget]: ...
    def get_hhomogeneous(self) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_page(self, child: Widget) -> StackPage: ...
    def get_pages(self) -> SelectionModel: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    def get_transition_type(self) -> StackTransitionType: ...
    def get_vhomogeneous(self) -> bool: ...
    def get_visible_child(self) -> Optional[Widget]: ...
    def get_visible_child_name(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> Stack: ...
    def remove(self, child: Widget) -> None: ...
    def set_hhomogeneous(self, hhomogeneous: bool) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: StackTransitionType) -> None: ...
    def set_vhomogeneous(self, vhomogeneous: bool) -> None: ...
    def set_visible_child(self, child: Widget) -> None: ...
    def set_visible_child_full(
        self, name: str, transition: StackTransitionType
    ) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class StackPage(GObject.Object, Accessible):
    class Props:
        child: Widget
        icon_name: str
        name: str
        needs_attention: bool
        title: str
        use_underline: bool
        visible: bool
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        icon_name: str = ...,
        name: str = ...,
        needs_attention: bool = ...,
        title: str = ...,
        use_underline: bool = ...,
        visible: bool = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Widget: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_name(self) -> Optional[str]: ...
    def get_needs_attention(self) -> bool: ...
    def get_title(self) -> Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    def get_visible(self) -> bool: ...
    def set_icon_name(self, setting: str) -> None: ...
    def set_name(self, setting: str) -> None: ...
    def set_needs_attention(self, setting: bool) -> None: ...
    def set_title(self, setting: str) -> None: ...
    def set_use_underline(self, setting: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class StackSidebar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        stack: Stack
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        stack: Stack = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_stack(self) -> Optional[Stack]: ...
    @classmethod
    def new(cls) -> StackSidebar: ...
    def set_stack(self, stack: Stack) -> None: ...

class StackSwitcher(Widget, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        stack: Stack
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        stack: Stack = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    def get_stack(self) -> Optional[Stack]: ...
    @classmethod
    def new(cls) -> StackSwitcher: ...
    def set_stack(self, stack: Optional[Stack] = None) -> None: ...

class Statusbar(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_context_id(self, context_description: str) -> int: ...
    @classmethod
    def new(cls) -> Statusbar: ...
    def pop(self, context_id: int) -> None: ...
    def push(self, context_id: int, text: str) -> int: ...
    def remove(self, context_id: int, message_id: int) -> None: ...
    def remove_all(self, context_id: int) -> None: ...

class StringFilter(Filter):
    class Props:
        expression: Expression
        ignore_case: bool
        match_mode: StringFilterMatchMode
        search: str
    props: Props = ...
    def __init__(
        self,
        expression: Expression = ...,
        ignore_case: bool = ...,
        match_mode: StringFilterMatchMode = ...,
        search: str = ...,
    ): ...
    def get_expression(self) -> Optional[Expression]: ...
    def get_ignore_case(self) -> bool: ...
    def get_match_mode(self) -> StringFilterMatchMode: ...
    def get_search(self) -> Optional[str]: ...
    @classmethod
    def new(cls, expression: Optional[Expression] = None) -> StringFilter: ...
    def set_expression(self, expression: Optional[Expression] = None) -> None: ...
    def set_ignore_case(self, ignore_case: bool) -> None: ...
    def set_match_mode(self, mode: StringFilterMatchMode) -> None: ...
    def set_search(self, search: Optional[str] = None) -> None: ...

class StringFilterClass(GObject.GPointer):
    parent_class: FilterClass = ...

class StringList(GObject.Object, Gio.ListModel, Buildable):
    def append(self, string: str) -> None: ...
    def get_string(self, position: int) -> Optional[str]: ...
    @classmethod
    def new(cls, strings: Optional[Sequence[str]] = None) -> StringList: ...
    def remove(self, position: int) -> None: ...
    def splice(
        self, position: int, n_removals: int, additions: Optional[Sequence[str]] = None
    ) -> None: ...
    def take(self, string: str) -> None: ...

class StringListClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class StringObject(GObject.Object):
    class Props:
        string: str
    props: Props = ...
    def get_string(self) -> str: ...
    @classmethod
    def new(cls, string: str) -> StringObject: ...

class StringObjectClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class StringSorter(Sorter):
    class Props:
        expression: Expression
        ignore_case: bool
    props: Props = ...
    def __init__(self, expression: Expression = ..., ignore_case: bool = ...): ...
    def get_expression(self) -> Optional[Expression]: ...
    def get_ignore_case(self) -> bool: ...
    @classmethod
    def new(cls, expression: Optional[Expression] = None) -> StringSorter: ...
    def set_expression(self, expression: Optional[Expression] = None) -> None: ...
    def set_ignore_case(self, ignore_case: bool) -> None: ...

class StringSorterClass(GObject.GPointer):
    parent_class: SorterClass = ...

class StyleContext(GObject.Object):
    class Props:
        display: Gdk.Display
    props: Props = ...
    def __init__(self, display: Gdk.Display = ...): ...
    parent_object: GObject.Object = ...
    def add_class(self, class_name: str) -> None: ...
    def add_provider(self, provider: StyleProvider, priority: int) -> None: ...
    @staticmethod
    def add_provider_for_display(
        display: Gdk.Display, provider: StyleProvider, priority: int
    ) -> None: ...
    def do_changed(self) -> None: ...
    def get_border(self) -> Border: ...
    def get_color(self) -> Gdk.RGBA: ...
    def get_display(self) -> Gdk.Display: ...
    def get_margin(self) -> Border: ...
    def get_padding(self) -> Border: ...
    def get_scale(self) -> int: ...
    def get_state(self) -> StateFlags: ...
    def has_class(self, class_name: str) -> bool: ...
    def lookup_color(self, color_name: str) -> Tuple[bool, Gdk.RGBA]: ...
    def remove_class(self, class_name: str) -> None: ...
    def remove_provider(self, provider: StyleProvider) -> None: ...
    @staticmethod
    def remove_provider_for_display(
        display: Gdk.Display, provider: StyleProvider
    ) -> None: ...
    def restore(self) -> None: ...
    def save(self) -> None: ...
    def set_display(self, display: Gdk.Display) -> None: ...
    def set_scale(self, scale: int) -> None: ...
    def set_state(self, flags: StateFlags) -> None: ...
    def to_string(self, flags: StyleContextPrintFlags) -> str: ...

class StyleContextClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    changed: Callable[[StyleContext], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class StyleProvider(GObject.Object): ...

class Switch(Widget, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        active: bool
        state: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        active: bool = ...,
        state: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_active(self) -> bool: ...
    def get_state(self) -> bool: ...
    @classmethod
    def new(cls) -> Switch: ...
    def set_active(self, is_active: bool) -> None: ...
    def set_state(self, state: bool) -> None: ...

class SymbolicPaintable(GObject.Object):
    def snapshot_symbolic(
        self,
        snapshot: Gdk.Snapshot,
        width: float,
        height: float,
        colors: Sequence[Gdk.RGBA],
    ) -> None: ...

class SymbolicPaintableInterface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    snapshot_symbolic: Callable[
        [SymbolicPaintable, Gdk.Snapshot, float, float, Sequence[Gdk.RGBA]], None
    ] = ...

# override
class Template:
    def __init__(
        self, filename: str = ..., resource_path: str = ..., string: str = ...
    ) -> None: ...
    @classmethod
    def from_file(cls, filename: str): ...
    @classmethod
    def from_resource(cls, resource_path: str): ...
    @classmethod
    def from_string(cls, string: str): ...
    def __call__(self, cls): ...

    class Callback: ...
    class Child: ...

class Text(Widget, Accessible, Buildable, ConstraintTarget, Editable):
    class Props:
        activates_default: bool
        attributes: Pango.AttrList
        buffer: EntryBuffer
        enable_emoji_completion: bool
        extra_menu: Gio.MenuModel
        im_module: str
        input_hints: InputHints
        input_purpose: InputPurpose
        invisible_char: int
        invisible_char_set: bool
        max_length: int
        overwrite_mode: bool
        placeholder_text: str
        propagate_text_width: bool
        scroll_offset: int
        tabs: Pango.TabArray
        truncate_multiline: bool
        visibility: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
    props: Props = ...
    def __init__(
        self,
        activates_default: bool = ...,
        attributes: Pango.AttrList = ...,
        buffer: EntryBuffer = ...,
        enable_emoji_completion: bool = ...,
        extra_menu: Gio.MenuModel = ...,
        im_module: str = ...,
        input_hints: InputHints = ...,
        input_purpose: InputPurpose = ...,
        invisible_char: int = ...,
        invisible_char_set: bool = ...,
        max_length: int = ...,
        overwrite_mode: bool = ...,
        placeholder_text: str = ...,
        propagate_text_width: bool = ...,
        tabs: Pango.TabArray = ...,
        truncate_multiline: bool = ...,
        visibility: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    parent_instance: Widget = ...
    def compute_cursor_extents(
        self, position: int
    ) -> Tuple[Graphene.Rect, Graphene.Rect]: ...
    def get_activates_default(self) -> bool: ...
    def get_attributes(self) -> Optional[Pango.AttrList]: ...
    def get_buffer(self) -> EntryBuffer: ...
    def get_enable_emoji_completion(self) -> bool: ...
    def get_extra_menu(self) -> Optional[Gio.MenuModel]: ...
    def get_input_hints(self) -> InputHints: ...
    def get_input_purpose(self) -> InputPurpose: ...
    def get_invisible_char(self) -> str: ...
    def get_max_length(self) -> int: ...
    def get_overwrite_mode(self) -> bool: ...
    def get_placeholder_text(self) -> Optional[str]: ...
    def get_propagate_text_width(self) -> bool: ...
    def get_tabs(self) -> Optional[Pango.TabArray]: ...
    def get_text_length(self) -> int: ...
    def get_truncate_multiline(self) -> bool: ...
    def get_visibility(self) -> bool: ...
    def grab_focus_without_selecting(self) -> bool: ...
    @classmethod
    def new(cls) -> Text: ...
    @classmethod
    def new_with_buffer(cls, buffer: EntryBuffer) -> Text: ...
    def set_activates_default(self, activates: bool) -> None: ...
    def set_attributes(self, attrs: Optional[Pango.AttrList] = None) -> None: ...
    def set_buffer(self, buffer: EntryBuffer) -> None: ...
    def set_enable_emoji_completion(self, enable_emoji_completion: bool) -> None: ...
    def set_extra_menu(self, model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_input_hints(self, hints: InputHints) -> None: ...
    def set_input_purpose(self, purpose: InputPurpose) -> None: ...
    def set_invisible_char(self, ch: str) -> None: ...
    def set_max_length(self, length: int) -> None: ...
    def set_overwrite_mode(self, overwrite: bool) -> None: ...
    def set_placeholder_text(self, text: Optional[str] = None) -> None: ...
    def set_propagate_text_width(self, propagate_text_width: bool) -> None: ...
    def set_tabs(self, tabs: Optional[Pango.TabArray] = None) -> None: ...
    def set_truncate_multiline(self, truncate_multiline: bool) -> None: ...
    def set_visibility(self, visible: bool) -> None: ...
    def unset_invisible_char(self) -> None: ...

class TextBuffer(GObject.Object):
    class Props:
        can_redo: bool
        can_undo: bool
        cursor_position: int
        enable_undo: bool
        has_selection: bool
        tag_table: TextTagTable
        text: str
    props: Props = ...
    def __init__(
        self, enable_undo: bool = ..., tag_table: TextTagTable = ..., text: str = ...
    ): ...
    parent_instance: GObject.Object = ...
    priv: TextBufferPrivate = ...
    def add_mark(self, mark: TextMark, where: TextIter) -> None: ...
    def add_selection_clipboard(self, clipboard: Gdk.Clipboard) -> None: ...
    def apply_tag(self, tag: TextTag, start: TextIter, end: TextIter) -> None: ...
    def apply_tag_by_name(self, name: str, start: TextIter, end: TextIter) -> None: ...
    def backspace(
        self, iter: TextIter, interactive: bool, default_editable: bool
    ) -> bool: ...
    def begin_irreversible_action(self) -> None: ...
    def begin_user_action(self) -> None: ...
    def copy_clipboard(self, clipboard: Gdk.Clipboard) -> None: ...
    def create_child_anchor(self, iter: TextIter) -> TextChildAnchor: ...
    def create_mark(self, *args, **kwargs): ...  # FIXME Method
    # override
    def create_tag(self, tag_name: str, **properties) -> None: ...
    def cut_clipboard(
        self, clipboard: Gdk.Clipboard, default_editable: bool
    ) -> None: ...
    def delete(self, start: TextIter, end: TextIter) -> None: ...
    def delete_interactive(
        self, start_iter: TextIter, end_iter: TextIter, default_editable: bool
    ) -> bool: ...
    def delete_mark(self, mark: TextMark) -> None: ...
    def delete_mark_by_name(self, name: str) -> None: ...
    def delete_selection(self, interactive: bool, default_editable: bool) -> bool: ...
    def do_apply_tag(self, tag: TextTag, start: TextIter, end: TextIter) -> None: ...
    def do_begin_user_action(self) -> None: ...
    def do_changed(self) -> None: ...
    def do_delete_range(self, start: TextIter, end: TextIter) -> None: ...
    def do_end_user_action(self) -> None: ...
    def do_insert_child_anchor(
        self, iter: TextIter, anchor: TextChildAnchor
    ) -> None: ...
    def do_insert_paintable(self, iter: TextIter, paintable: Gdk.Paintable) -> None: ...
    def do_insert_text(
        self, pos: TextIter, new_text: str, new_text_length: int
    ) -> None: ...
    def do_mark_deleted(self, mark: TextMark) -> None: ...
    def do_mark_set(self, location: TextIter, mark: TextMark) -> None: ...
    def do_modified_changed(self) -> None: ...
    def do_paste_done(self, clipboard: Gdk.Clipboard) -> None: ...
    def do_redo(self) -> None: ...
    def do_remove_tag(self, tag: TextTag, start: TextIter, end: TextIter) -> None: ...
    def do_undo(self) -> None: ...
    def end_irreversible_action(self) -> None: ...
    def end_user_action(self) -> None: ...
    def get_bounds(self) -> Tuple[TextIter, TextIter]: ...
    def get_can_redo(self) -> bool: ...
    def get_can_undo(self) -> bool: ...
    def get_char_count(self) -> int: ...
    def get_enable_undo(self) -> bool: ...
    def get_end_iter(self) -> TextIter: ...
    def get_has_selection(self) -> bool: ...
    def get_insert(self) -> TextMark: ...
    def get_iter_at_child_anchor(self, anchor: TextChildAnchor) -> TextIter: ...
    def get_iter_at_line(self, line_number: int) -> Tuple[bool, TextIter]: ...
    def get_iter_at_line_index(
        self, line_number: int, byte_index: int
    ) -> Tuple[bool, TextIter]: ...
    def get_iter_at_line_offset(
        self, line_number: int, char_offset: int
    ) -> Tuple[bool, TextIter]: ...
    def get_iter_at_mark(self, mark: TextMark) -> TextIter: ...
    def get_iter_at_offset(self, char_offset: int) -> TextIter: ...
    def get_line_count(self) -> int: ...
    def get_mark(self, name: str) -> Optional[TextMark]: ...
    def get_max_undo_levels(self) -> int: ...
    def get_modified(self) -> bool: ...
    def get_selection_bound(self) -> TextMark: ...
    def get_selection_bounds(self, *args, **kwargs): ...  # FIXME Method
    def get_selection_content(self) -> Gdk.ContentProvider: ...
    def get_slice(
        self, start: TextIter, end: TextIter, include_hidden_chars: bool
    ) -> str: ...
    def get_start_iter(self) -> TextIter: ...
    def get_tag_table(self) -> TextTagTable: ...
    def get_text(
        self, start: TextIter, end: TextIter, include_hidden_chars: bool
    ) -> str: ...
    def insert(self, *args, **kwargs): ...  # FIXME Method
    def insert_at_cursor(self, *args, **kwargs): ...  # FIXME Method
    def insert_child_anchor(self, iter: TextIter, anchor: TextChildAnchor) -> None: ...
    def insert_interactive(
        self, iter: TextIter, text: str, len: int, default_editable: bool
    ) -> bool: ...
    def insert_interactive_at_cursor(
        self, text: str, len: int, default_editable: bool
    ) -> bool: ...
    def insert_markup(self, iter: TextIter, markup: str, len: int) -> None: ...
    def insert_paintable(self, iter: TextIter, paintable: Gdk.Paintable) -> None: ...
    def insert_range(self, iter: TextIter, start: TextIter, end: TextIter) -> None: ...
    def insert_range_interactive(
        self, iter: TextIter, start: TextIter, end: TextIter, default_editable: bool
    ) -> bool: ...
    def insert_with_tags(self, *args, **kwargs): ...  # FIXME Method
    # override
    def insert_with_tags_by_name(
        self, iter: TextIter, text: str, *tags: Any
    ) -> None: ...
    def move_mark(self, mark: TextMark, where: TextIter) -> None: ...
    def move_mark_by_name(self, name: str, where: TextIter) -> None: ...
    @classmethod
    def new(cls, table: Optional[TextTagTable] = None) -> TextBuffer: ...
    def paste_clipboard(
        self,
        clipboard: Gdk.Clipboard,
        override_location: Optional[TextIter],
        default_editable: bool,
    ) -> None: ...
    def place_cursor(self, where: TextIter) -> None: ...
    def redo(self) -> None: ...
    def remove_all_tags(self, start: TextIter, end: TextIter) -> None: ...
    def remove_selection_clipboard(self, clipboard: Gdk.Clipboard) -> None: ...
    def remove_tag(self, tag: TextTag, start: TextIter, end: TextIter) -> None: ...
    def remove_tag_by_name(self, name: str, start: TextIter, end: TextIter) -> None: ...
    def select_range(self, ins: TextIter, bound: TextIter) -> None: ...
    def set_enable_undo(self, enable_undo: bool) -> None: ...
    def set_max_undo_levels(self, max_undo_levels: int) -> None: ...
    def set_modified(self, setting: bool) -> None: ...
    # override
    def set_text(self, text: str, len: int = -1) -> None: ...
    def undo(self) -> None: ...

class TextBufferClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    insert_text: Callable[[TextBuffer, TextIter, str, int], None] = ...
    insert_paintable: Callable[[TextBuffer, TextIter, Gdk.Paintable], None] = ...
    insert_child_anchor: Callable[[TextBuffer, TextIter, TextChildAnchor], None] = ...
    delete_range: Callable[[TextBuffer, TextIter, TextIter], None] = ...
    changed: Callable[[TextBuffer], None] = ...
    modified_changed: Callable[[TextBuffer], None] = ...
    mark_set: Callable[[TextBuffer, TextIter, TextMark], None] = ...
    mark_deleted: Callable[[TextBuffer, TextMark], None] = ...
    apply_tag: Callable[[TextBuffer, TextTag, TextIter, TextIter], None] = ...
    remove_tag: Callable[[TextBuffer, TextTag, TextIter, TextIter], None] = ...
    begin_user_action: Callable[[TextBuffer], None] = ...
    end_user_action: Callable[[TextBuffer], None] = ...
    paste_done: Callable[[TextBuffer, Gdk.Clipboard], None] = ...
    undo: Callable[[TextBuffer], None] = ...
    redo: Callable[[TextBuffer], None] = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class TextBufferPrivate(GObject.GPointer): ...

class TextChildAnchor(GObject.Object):
    parent_instance: GObject.Object = ...
    segment: None = ...
    def get_deleted(self) -> bool: ...
    def get_widgets(self) -> list[Widget]: ...
    @classmethod
    def new(cls) -> TextChildAnchor: ...
    @classmethod
    def new_with_replacement(cls, character: str) -> TextChildAnchor: ...

class TextChildAnchorClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class TextIter(GObject.GBoxed):
    dummy1: None = ...
    dummy2: None = ...
    dummy3: int = ...
    dummy4: int = ...
    dummy5: int = ...
    dummy6: int = ...
    dummy7: int = ...
    dummy8: int = ...
    dummy9: None = ...
    dummy10: None = ...
    dummy11: int = ...
    dummy12: int = ...
    dummy13: int = ...
    dummy14: None = ...
    def assign(self, other: TextIter) -> None: ...
    def backward_char(self) -> bool: ...
    def backward_chars(self, count: int) -> bool: ...
    def backward_cursor_position(self) -> bool: ...
    def backward_cursor_positions(self, count: int) -> bool: ...
    def backward_find_char(
        self,
        pred: Callable[..., bool],
        limit: Optional[TextIter] = None,
        *user_data: Any,
    ) -> bool: ...
    def backward_line(self) -> bool: ...
    def backward_lines(self, count: int) -> bool: ...
    def backward_search(self, *args, **kwargs): ...  # FIXME Method
    def backward_sentence_start(self) -> bool: ...
    def backward_sentence_starts(self, count: int) -> bool: ...
    def backward_to_tag_toggle(self, tag: Optional[TextTag] = None) -> bool: ...
    def backward_visible_cursor_position(self) -> bool: ...
    def backward_visible_cursor_positions(self, count: int) -> bool: ...
    def backward_visible_line(self) -> bool: ...
    def backward_visible_lines(self, count: int) -> bool: ...
    def backward_visible_word_start(self) -> bool: ...
    def backward_visible_word_starts(self, count: int) -> bool: ...
    def backward_word_start(self) -> bool: ...
    def backward_word_starts(self, count: int) -> bool: ...
    def can_insert(self, default_editability: bool) -> bool: ...
    def compare(self, rhs: TextIter) -> int: ...
    def copy(self) -> TextIter: ...
    def editable(self, default_setting: bool) -> bool: ...
    def ends_line(self) -> bool: ...
    def ends_sentence(self) -> bool: ...
    def ends_tag(self, tag: Optional[TextTag] = None) -> bool: ...
    def ends_word(self) -> bool: ...
    def equal(self, rhs: TextIter) -> bool: ...
    def forward_char(self) -> bool: ...
    def forward_chars(self, count: int) -> bool: ...
    def forward_cursor_position(self) -> bool: ...
    def forward_cursor_positions(self, count: int) -> bool: ...
    def forward_find_char(
        self,
        pred: Callable[..., bool],
        limit: Optional[TextIter] = None,
        *user_data: Any,
    ) -> bool: ...
    def forward_line(self) -> bool: ...
    def forward_lines(self, count: int) -> bool: ...
    def forward_search(self, *args, **kwargs): ...  # FIXME Method
    def forward_sentence_end(self) -> bool: ...
    def forward_sentence_ends(self, count: int) -> bool: ...
    def forward_to_end(self) -> None: ...
    def forward_to_line_end(self) -> bool: ...
    def forward_to_tag_toggle(self, tag: Optional[TextTag] = None) -> bool: ...
    def forward_visible_cursor_position(self) -> bool: ...
    def forward_visible_cursor_positions(self, count: int) -> bool: ...
    def forward_visible_line(self) -> bool: ...
    def forward_visible_lines(self, count: int) -> bool: ...
    def forward_visible_word_end(self) -> bool: ...
    def forward_visible_word_ends(self, count: int) -> bool: ...
    def forward_word_end(self) -> bool: ...
    def forward_word_ends(self, count: int) -> bool: ...
    def free(self) -> None: ...
    def get_buffer(self) -> TextBuffer: ...
    def get_bytes_in_line(self) -> int: ...
    def get_char(self) -> str: ...
    def get_chars_in_line(self) -> int: ...
    def get_child_anchor(self) -> Optional[TextChildAnchor]: ...
    def get_language(self) -> Pango.Language: ...
    def get_line(self) -> int: ...
    def get_line_index(self) -> int: ...
    def get_line_offset(self) -> int: ...
    def get_marks(self) -> list[TextMark]: ...
    def get_offset(self) -> int: ...
    def get_paintable(self) -> Optional[Gdk.Paintable]: ...
    def get_slice(self, end: TextIter) -> str: ...
    def get_tags(self) -> list[TextTag]: ...
    def get_text(self, end: TextIter) -> str: ...
    def get_toggled_tags(self, toggled_on: bool) -> list[TextTag]: ...
    def get_visible_line_index(self) -> int: ...
    def get_visible_line_offset(self) -> int: ...
    def get_visible_slice(self, end: TextIter) -> str: ...
    def get_visible_text(self, end: TextIter) -> str: ...
    def has_tag(self, tag: TextTag) -> bool: ...
    def in_range(self, start: TextIter, end: TextIter) -> bool: ...
    def inside_sentence(self) -> bool: ...
    def inside_word(self) -> bool: ...
    def is_cursor_position(self) -> bool: ...
    def is_end(self) -> bool: ...
    def is_start(self) -> bool: ...
    def order(self, second: TextIter) -> None: ...
    def set_line(self, line_number: int) -> None: ...
    def set_line_index(self, byte_on_line: int) -> None: ...
    def set_line_offset(self, char_on_line: int) -> None: ...
    def set_offset(self, char_offset: int) -> None: ...
    def set_visible_line_index(self, byte_on_line: int) -> None: ...
    def set_visible_line_offset(self, char_on_line: int) -> None: ...
    def starts_line(self) -> bool: ...
    def starts_sentence(self) -> bool: ...
    def starts_tag(self, tag: Optional[TextTag] = None) -> bool: ...
    def starts_word(self) -> bool: ...
    def toggles_tag(self, tag: Optional[TextTag] = None) -> bool: ...

class TextMark(GObject.Object):
    class Props:
        left_gravity: bool
        name: str
    props: Props = ...
    def __init__(self, left_gravity: bool = ..., name: str = ...): ...
    parent_instance: GObject.Object = ...
    segment: None = ...
    def get_buffer(self) -> Optional[TextBuffer]: ...
    def get_deleted(self) -> bool: ...
    def get_left_gravity(self) -> bool: ...
    def get_name(self) -> Optional[str]: ...
    def get_visible(self) -> bool: ...
    @classmethod
    def new(cls, name: Optional[str], left_gravity: bool) -> TextMark: ...
    def set_visible(self, setting: bool) -> None: ...

class TextMarkClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class TextTag(GObject.Object):
    class Props:
        accumulative_margin: bool
        allow_breaks: bool
        allow_breaks_set: bool
        background: str
        background_full_height: bool
        background_full_height_set: bool
        background_rgba: Gdk.RGBA
        background_set: bool
        direction: TextDirection
        editable: bool
        editable_set: bool
        fallback: bool
        fallback_set: bool
        family: str
        family_set: bool
        font: str
        font_desc: Pango.FontDescription
        font_features: str
        font_features_set: bool
        foreground: str
        foreground_rgba: Gdk.RGBA
        foreground_set: bool
        indent: int
        indent_set: bool
        insert_hyphens: bool
        insert_hyphens_set: bool
        invisible: bool
        invisible_set: bool
        justification: Justification
        justification_set: bool
        language: str
        language_set: bool
        left_margin: int
        left_margin_set: bool
        letter_spacing: int
        letter_spacing_set: bool
        line_height: float
        line_height_set: bool
        name: str
        overline: Pango.Overline
        overline_rgba: Gdk.RGBA
        overline_rgba_set: bool
        overline_set: bool
        paragraph_background: str
        paragraph_background_rgba: Gdk.RGBA
        paragraph_background_set: bool
        pixels_above_lines: int
        pixels_above_lines_set: bool
        pixels_below_lines: int
        pixels_below_lines_set: bool
        pixels_inside_wrap: int
        pixels_inside_wrap_set: bool
        right_margin: int
        right_margin_set: bool
        rise: int
        rise_set: bool
        scale: float
        scale_set: bool
        sentence: bool
        sentence_set: bool
        show_spaces: Pango.ShowFlags
        show_spaces_set: bool
        size: int
        size_points: float
        size_set: bool
        stretch: Pango.Stretch
        stretch_set: bool
        strikethrough: bool
        strikethrough_rgba: Gdk.RGBA
        strikethrough_rgba_set: bool
        strikethrough_set: bool
        style: Pango.Style
        style_set: bool
        tabs: Pango.TabArray
        tabs_set: bool
        text_transform: Pango.TextTransform
        text_transform_set: bool
        underline: Pango.Underline
        underline_rgba: Gdk.RGBA
        underline_rgba_set: bool
        underline_set: bool
        variant: Pango.Variant
        variant_set: bool
        weight: int
        weight_set: bool
        word: bool
        word_set: bool
        wrap_mode: WrapMode
        wrap_mode_set: bool
    props: Props = ...
    def __init__(
        self,
        accumulative_margin: bool = ...,
        allow_breaks: bool = ...,
        allow_breaks_set: bool = ...,
        background: str = ...,
        background_full_height: bool = ...,
        background_full_height_set: bool = ...,
        background_rgba: Gdk.RGBA = ...,
        background_set: bool = ...,
        direction: TextDirection = ...,
        editable: bool = ...,
        editable_set: bool = ...,
        fallback: bool = ...,
        fallback_set: bool = ...,
        family: str = ...,
        family_set: bool = ...,
        font: str = ...,
        font_desc: Pango.FontDescription = ...,
        font_features: str = ...,
        font_features_set: bool = ...,
        foreground: str = ...,
        foreground_rgba: Gdk.RGBA = ...,
        foreground_set: bool = ...,
        indent: int = ...,
        indent_set: bool = ...,
        insert_hyphens: bool = ...,
        insert_hyphens_set: bool = ...,
        invisible: bool = ...,
        invisible_set: bool = ...,
        justification: Justification = ...,
        justification_set: bool = ...,
        language: str = ...,
        language_set: bool = ...,
        left_margin: int = ...,
        left_margin_set: bool = ...,
        letter_spacing: int = ...,
        letter_spacing_set: bool = ...,
        line_height: float = ...,
        line_height_set: bool = ...,
        name: str = ...,
        overline: Pango.Overline = ...,
        overline_rgba: Gdk.RGBA = ...,
        overline_rgba_set: bool = ...,
        overline_set: bool = ...,
        paragraph_background: str = ...,
        paragraph_background_rgba: Gdk.RGBA = ...,
        paragraph_background_set: bool = ...,
        pixels_above_lines: int = ...,
        pixels_above_lines_set: bool = ...,
        pixels_below_lines: int = ...,
        pixels_below_lines_set: bool = ...,
        pixels_inside_wrap: int = ...,
        pixels_inside_wrap_set: bool = ...,
        right_margin: int = ...,
        right_margin_set: bool = ...,
        rise: int = ...,
        rise_set: bool = ...,
        scale: float = ...,
        scale_set: bool = ...,
        sentence: bool = ...,
        sentence_set: bool = ...,
        show_spaces: Pango.ShowFlags = ...,
        show_spaces_set: bool = ...,
        size: int = ...,
        size_points: float = ...,
        size_set: bool = ...,
        stretch: Pango.Stretch = ...,
        stretch_set: bool = ...,
        strikethrough: bool = ...,
        strikethrough_rgba: Gdk.RGBA = ...,
        strikethrough_rgba_set: bool = ...,
        strikethrough_set: bool = ...,
        style: Pango.Style = ...,
        style_set: bool = ...,
        tabs: Pango.TabArray = ...,
        tabs_set: bool = ...,
        text_transform: Pango.TextTransform = ...,
        text_transform_set: bool = ...,
        underline: Pango.Underline = ...,
        underline_rgba: Gdk.RGBA = ...,
        underline_rgba_set: bool = ...,
        underline_set: bool = ...,
        variant: Pango.Variant = ...,
        variant_set: bool = ...,
        weight: int = ...,
        weight_set: bool = ...,
        word: bool = ...,
        word_set: bool = ...,
        wrap_mode: WrapMode = ...,
        wrap_mode_set: bool = ...,
    ): ...
    parent_instance: GObject.Object = ...
    priv: TextTagPrivate = ...
    def changed(self, size_changed: bool) -> None: ...
    def get_priority(self) -> int: ...
    @classmethod
    def new(cls, name: Optional[str] = None) -> TextTag: ...
    def set_priority(self, priority: int) -> None: ...

class TextTagClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class TextTagPrivate(GObject.GPointer): ...

class TextTagTable(GObject.Object, Buildable):
    def add(self, tag: TextTag) -> bool: ...
    def foreach(self, func: Callable[..., None], *data: Any) -> None: ...
    def get_size(self) -> int: ...
    def lookup(self, name: str) -> Optional[TextTag]: ...
    @classmethod
    def new(cls) -> TextTagTable: ...
    def remove(self, tag: TextTag) -> None: ...

class TextView(Widget, Accessible, Buildable, ConstraintTarget, Scrollable):
    class Props:
        accepts_tab: bool
        bottom_margin: int
        buffer: TextBuffer
        cursor_visible: bool
        editable: bool
        extra_menu: Gio.MenuModel
        im_module: str
        indent: int
        input_hints: InputHints
        input_purpose: InputPurpose
        justification: Justification
        left_margin: int
        monospace: bool
        overwrite: bool
        pixels_above_lines: int
        pixels_below_lines: int
        pixels_inside_wrap: int
        right_margin: int
        tabs: Pango.TabArray
        top_margin: int
        wrap_mode: WrapMode
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        accepts_tab: bool = ...,
        bottom_margin: int = ...,
        buffer: TextBuffer = ...,
        cursor_visible: bool = ...,
        editable: bool = ...,
        extra_menu: Gio.MenuModel = ...,
        im_module: str = ...,
        indent: int = ...,
        input_hints: InputHints = ...,
        input_purpose: InputPurpose = ...,
        justification: Justification = ...,
        left_margin: int = ...,
        monospace: bool = ...,
        overwrite: bool = ...,
        pixels_above_lines: int = ...,
        pixels_below_lines: int = ...,
        pixels_inside_wrap: int = ...,
        right_margin: int = ...,
        tabs: Pango.TabArray = ...,
        top_margin: int = ...,
        wrap_mode: WrapMode = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    parent_instance: Widget = ...
    priv: TextViewPrivate = ...
    def add_child_at_anchor(self, child: Widget, anchor: TextChildAnchor) -> None: ...
    def add_overlay(self, child: Widget, xpos: int, ypos: int) -> None: ...
    def backward_display_line(self, iter: TextIter) -> bool: ...
    def backward_display_line_start(self, iter: TextIter) -> bool: ...
    def buffer_to_window_coords(
        self, win: TextWindowType, buffer_x: int, buffer_y: int
    ) -> Tuple[int, int]: ...
    def do_backspace(self) -> None: ...
    def do_copy_clipboard(self) -> None: ...
    def do_cut_clipboard(self) -> None: ...
    def do_delete_from_cursor(self, type: DeleteType, count: int) -> None: ...
    def do_extend_selection(
        self,
        granularity: TextExtendSelection,
        location: TextIter,
        start: TextIter,
        end: TextIter,
    ) -> bool: ...
    def do_insert_at_cursor(self, str: str) -> None: ...
    def do_insert_emoji(self) -> None: ...
    def do_move_cursor(
        self, step: MovementStep, count: int, extend_selection: bool
    ) -> None: ...
    def do_paste_clipboard(self) -> None: ...
    def do_set_anchor(self) -> None: ...
    def do_snapshot_layer(self, layer: TextViewLayer, snapshot: Snapshot) -> None: ...
    def do_toggle_overwrite(self) -> None: ...
    def forward_display_line(self, iter: TextIter) -> bool: ...
    def forward_display_line_end(self, iter: TextIter) -> bool: ...
    def get_accepts_tab(self) -> bool: ...
    def get_bottom_margin(self) -> int: ...
    def get_buffer(self) -> TextBuffer: ...
    def get_cursor_locations(
        self, iter: Optional[TextIter] = None
    ) -> Tuple[Gdk.Rectangle, Gdk.Rectangle]: ...
    def get_cursor_visible(self) -> bool: ...
    def get_editable(self) -> bool: ...
    def get_extra_menu(self) -> Gio.MenuModel: ...
    def get_gutter(self, win: TextWindowType) -> Optional[Widget]: ...
    def get_indent(self) -> int: ...
    def get_input_hints(self) -> InputHints: ...
    def get_input_purpose(self) -> InputPurpose: ...
    def get_iter_at_location(self, x: int, y: int) -> Tuple[bool, TextIter]: ...
    def get_iter_at_position(self, x: int, y: int) -> Tuple[bool, TextIter, int]: ...
    def get_iter_location(self, iter: TextIter) -> Gdk.Rectangle: ...
    def get_justification(self) -> Justification: ...
    def get_left_margin(self) -> int: ...
    def get_line_at_y(self, y: int) -> Tuple[TextIter, int]: ...
    def get_line_yrange(self, iter: TextIter) -> Tuple[int, int]: ...
    def get_ltr_context(self) -> Pango.Context: ...
    def get_monospace(self) -> bool: ...
    def get_overwrite(self) -> bool: ...
    def get_pixels_above_lines(self) -> int: ...
    def get_pixels_below_lines(self) -> int: ...
    def get_pixels_inside_wrap(self) -> int: ...
    def get_right_margin(self) -> int: ...
    def get_rtl_context(self) -> Pango.Context: ...
    def get_tabs(self) -> Optional[Pango.TabArray]: ...
    def get_top_margin(self) -> int: ...
    def get_visible_rect(self) -> Gdk.Rectangle: ...
    def get_wrap_mode(self) -> WrapMode: ...
    def im_context_filter_keypress(self, event: Gdk.Event) -> bool: ...
    def move_mark_onscreen(self, mark: TextMark) -> bool: ...
    def move_overlay(self, child: Widget, xpos: int, ypos: int) -> None: ...
    def move_visually(self, iter: TextIter, count: int) -> bool: ...
    @classmethod
    def new(cls) -> TextView: ...
    @classmethod
    def new_with_buffer(cls, buffer: TextBuffer) -> TextView: ...
    def place_cursor_onscreen(self) -> bool: ...
    def remove(self, child: Widget) -> None: ...
    def reset_cursor_blink(self) -> None: ...
    def reset_im_context(self) -> None: ...
    def scroll_mark_onscreen(self, mark: TextMark) -> None: ...
    def scroll_to_iter(
        self,
        iter: TextIter,
        within_margin: float,
        use_align: bool,
        xalign: float,
        yalign: float,
    ) -> bool: ...
    def scroll_to_mark(
        self,
        mark: TextMark,
        within_margin: float,
        use_align: bool,
        xalign: float,
        yalign: float,
    ) -> None: ...
    def set_accepts_tab(self, accepts_tab: bool) -> None: ...
    def set_bottom_margin(self, bottom_margin: int) -> None: ...
    def set_buffer(self, buffer: Optional[TextBuffer] = None) -> None: ...
    def set_cursor_visible(self, setting: bool) -> None: ...
    def set_editable(self, setting: bool) -> None: ...
    def set_extra_menu(self, model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_gutter(
        self, win: TextWindowType, widget: Optional[Widget] = None
    ) -> None: ...
    def set_indent(self, indent: int) -> None: ...
    def set_input_hints(self, hints: InputHints) -> None: ...
    def set_input_purpose(self, purpose: InputPurpose) -> None: ...
    def set_justification(self, justification: Justification) -> None: ...
    def set_left_margin(self, left_margin: int) -> None: ...
    def set_monospace(self, monospace: bool) -> None: ...
    def set_overwrite(self, overwrite: bool) -> None: ...
    def set_pixels_above_lines(self, pixels_above_lines: int) -> None: ...
    def set_pixels_below_lines(self, pixels_below_lines: int) -> None: ...
    def set_pixels_inside_wrap(self, pixels_inside_wrap: int) -> None: ...
    def set_right_margin(self, right_margin: int) -> None: ...
    def set_tabs(self, tabs: Pango.TabArray) -> None: ...
    def set_top_margin(self, top_margin: int) -> None: ...
    def set_wrap_mode(self, wrap_mode: WrapMode) -> None: ...
    def starts_display_line(self, iter: TextIter) -> bool: ...
    def window_to_buffer_coords(
        self, win: TextWindowType, window_x: int, window_y: int
    ) -> Tuple[int, int]: ...

class TextViewClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    move_cursor: Callable[[TextView, MovementStep, int, bool], None] = ...
    set_anchor: Callable[[TextView], None] = ...
    insert_at_cursor: Callable[[TextView, str], None] = ...
    delete_from_cursor: Callable[[TextView, DeleteType, int], None] = ...
    backspace: Callable[[TextView], None] = ...
    cut_clipboard: Callable[[TextView], None] = ...
    copy_clipboard: Callable[[TextView], None] = ...
    paste_clipboard: Callable[[TextView], None] = ...
    toggle_overwrite: Callable[[TextView], None] = ...
    create_buffer: None = ...
    snapshot_layer: Callable[[TextView, TextViewLayer, Snapshot], None] = ...
    extend_selection: Callable[
        [TextView, TextExtendSelection, TextIter, TextIter, TextIter], bool
    ] = ...
    insert_emoji: Callable[[TextView], None] = ...
    padding: list[None] = ...

class TextViewPrivate(GObject.GPointer): ...

class ToggleButton(Button, Accessible, Actionable, Buildable, ConstraintTarget):
    class Props:
        active: bool
        group: ToggleButton
        child: Widget
        has_frame: bool
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        action_name: str
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        active: bool = ...,
        group: ToggleButton = ...,
        child: Widget = ...,
        has_frame: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    button: Button = ...
    def do_toggled(self) -> None: ...
    def get_active(self) -> bool: ...
    @classmethod
    def new(cls) -> ToggleButton: ...
    @classmethod
    def new_with_label(cls, label: str) -> ToggleButton: ...
    @classmethod
    def new_with_mnemonic(cls, label: str) -> ToggleButton: ...
    def set_active(self, is_active: bool) -> None: ...
    def set_group(self, group: Optional[ToggleButton] = None) -> None: ...
    def toggled(self) -> None: ...

class ToggleButtonClass(GObject.GPointer):
    parent_class: ButtonClass = ...
    toggled: Callable[[ToggleButton], None] = ...
    padding: list[None] = ...

class Tooltip(GObject.Object):
    def set_custom(self, custom_widget: Optional[Widget] = None) -> None: ...
    def set_icon(self, paintable: Optional[Gdk.Paintable] = None) -> None: ...
    def set_icon_from_gicon(self, gicon: Optional[Gio.Icon] = None) -> None: ...
    def set_icon_from_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_markup(self, markup: Optional[str] = None) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...
    def set_tip_area(self, rect: Gdk.Rectangle) -> None: ...

class TreeDragDest(GObject.Object):
    def drag_data_received(self, dest: TreePath, value: Any) -> bool: ...
    def row_drop_possible(self, dest_path: TreePath, value: Any) -> bool: ...

class TreeDragDestIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    drag_data_received: Callable[[TreeDragDest, TreePath, Any], bool] = ...
    row_drop_possible: Callable[[TreeDragDest, TreePath, Any], bool] = ...

class TreeDragSource(GObject.Object):
    def drag_data_delete(self, path: TreePath) -> bool: ...
    def drag_data_get(self, path: TreePath) -> Optional[Gdk.ContentProvider]: ...
    def row_draggable(self, path: TreePath) -> bool: ...

class TreeDragSourceIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    row_draggable: Callable[[TreeDragSource, TreePath], bool] = ...
    drag_data_get: Callable[
        [TreeDragSource, TreePath], Optional[Gdk.ContentProvider]
    ] = ...
    drag_data_delete: Callable[[TreeDragSource, TreePath], bool] = ...

class TreeExpander(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        indent_for_icon: bool
        item: GObject.Object
        list_row: TreeListRow
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        indent_for_icon: bool = ...,
        list_row: TreeListRow = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    def get_indent_for_icon(self) -> bool: ...
    def get_item(self) -> Optional[GObject.Object]: ...
    def get_list_row(self) -> Optional[TreeListRow]: ...
    @classmethod
    def new(cls) -> TreeExpander: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_indent_for_icon(self, indent_for_icon: bool) -> None: ...
    def set_list_row(self, list_row: Optional[TreeListRow] = None) -> None: ...

class TreeExpanderClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class TreeIter(GObject.GBoxed):
    stamp: int = ...
    user_data: None = ...
    user_data2: None = ...
    user_data3: None = ...
    def copy(self) -> TreeIter: ...
    def free(self) -> None: ...

class TreeListModel(GObject.Object, Gio.ListModel):
    class Props:
        autoexpand: bool
        item_type: Type
        model: Gio.ListModel
        n_items: int
        passthrough: bool
    props: Props = ...
    def __init__(self, autoexpand: bool = ..., passthrough: bool = ...): ...
    def get_autoexpand(self) -> bool: ...
    def get_child_row(self, position: int) -> Optional[TreeListRow]: ...
    def get_model(self) -> Gio.ListModel: ...
    def get_passthrough(self) -> bool: ...
    def get_row(self, position: int) -> Optional[TreeListRow]: ...
    @classmethod
    def new(
        cls,
        root: Gio.ListModel,
        passthrough: bool,
        autoexpand: bool,
        create_func: Callable[..., Optional[Gio.ListModel]],
        *user_data: Any,
    ) -> TreeListModel: ...
    def set_autoexpand(self, autoexpand: bool) -> None: ...

class TreeListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class TreeListRow(GObject.Object):
    class Props:
        children: Gio.ListModel
        depth: int
        expandable: bool
        expanded: bool
        item: GObject.Object
    props: Props = ...
    def __init__(self, expanded: bool = ...): ...
    def get_child_row(self, position: int) -> Optional[TreeListRow]: ...
    def get_children(self) -> Optional[Gio.ListModel]: ...
    def get_depth(self) -> int: ...
    def get_expanded(self) -> bool: ...
    def get_item(self) -> Optional[GObject.Object]: ...
    def get_parent(self) -> Optional[TreeListRow]: ...
    def get_position(self) -> int: ...
    def is_expandable(self) -> bool: ...
    def set_expanded(self, expanded: bool) -> None: ...

class TreeListRowClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class TreeListRowSorter(Sorter):
    class Props:
        sorter: Sorter
    props: Props = ...
    def __init__(self, sorter: Sorter = ...): ...
    def get_sorter(self) -> Optional[Sorter]: ...
    @classmethod
    def new(cls, sorter: Optional[Sorter] = None) -> TreeListRowSorter: ...
    def set_sorter(self, sorter: Optional[Sorter] = None) -> None: ...

class TreeListRowSorterClass(GObject.GPointer):
    parent_class: SorterClass = ...

class TreeModel(GObject.Object):
    def filter_new(self, root: Optional[TreePath] = None) -> TreeModel: ...
    def foreach(self, func: Callable[..., bool], *user_data: Any) -> None: ...
    def get(self, *args, **kwargs): ...  # FIXME Method
    def get_column_type(self, index_: int) -> Type: ...
    def get_flags(self) -> TreeModelFlags: ...
    def get_iter(self, *args, **kwargs): ...  # FIXME Method
    def get_iter_first(self, *args, **kwargs): ...  # FIXME Method
    def get_iter_from_string(self, *args, **kwargs): ...  # FIXME Method
    def get_n_columns(self) -> int: ...
    def get_path(self, iter: TreeIter) -> TreePath: ...
    def get_string_from_iter(self, iter: TreeIter) -> Optional[str]: ...
    def get_value(self, iter: TreeIter, column: int) -> Any: ...
    def iter_children(self, *args, **kwargs): ...  # FIXME Method
    def iter_has_child(self, iter: TreeIter) -> bool: ...
    def iter_n_children(self, iter: Optional[TreeIter] = None) -> int: ...
    def iter_next(self, *args, **kwargs): ...  # FIXME Method
    def iter_nth_child(self, *args, **kwargs): ...  # FIXME Method
    def iter_parent(self, *args, **kwargs): ...  # FIXME Method
    def iter_previous(self, *args, **kwargs): ...  # FIXME Method
    def ref_node(self, iter: TreeIter) -> None: ...
    def row_changed(self, *args, **kwargs): ...  # FIXME Method
    def row_deleted(self, *args, **kwargs): ...  # FIXME Method
    def row_has_child_toggled(self, *args, **kwargs): ...  # FIXME Method
    def row_inserted(self, *args, **kwargs): ...  # FIXME Method
    def rows_reordered(self, *args, **kwargs): ...  # FIXME Method
    def set_row(self, *args, **kwargs): ...  # FIXME Method
    def sort_new_with_model(self, *args, **kwargs): ...  # FIXME Method
    def unref_node(self, iter: TreeIter) -> None: ...

class TreeModelFilter(GObject.Object, TreeDragSource, TreeModel):
    class Props:
        child_model: TreeModel
        virtual_root: TreePath
    props: Props = ...
    def __init__(self, child_model: TreeModel = ..., virtual_root: TreePath = ...): ...
    parent: GObject.Object = ...
    priv: TreeModelFilterPrivate = ...
    def clear_cache(self) -> None: ...
    def convert_child_iter_to_iter(
        self, child_iter: TreeIter
    ) -> Tuple[bool, TreeIter]: ...
    def convert_child_path_to_path(
        self, child_path: TreePath
    ) -> Optional[TreePath]: ...
    def convert_iter_to_child_iter(self, filter_iter: TreeIter) -> TreeIter: ...
    def convert_path_to_child_path(
        self, filter_path: TreePath
    ) -> Optional[TreePath]: ...
    def do_modify(
        self, child_model: TreeModel, iter: TreeIter, value: Any, column: int
    ) -> None: ...
    def do_visible(self, child_model: TreeModel, iter: TreeIter) -> bool: ...
    def get_model(self) -> TreeModel: ...
    def refilter(self) -> None: ...
    def set_modify_func(
        self,
        n_columns: int,
        types: Sequence[Type],
        func: Callable[..., Any],
        *data: Any,
    ) -> None: ...
    def set_value(self, *args, **kwargs): ...  # FIXME Method
    def set_visible_column(self, column: int) -> None: ...
    def set_visible_func(self, *args, **kwargs): ...  # FIXME Method

class TreeModelFilterClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    visible: Callable[[TreeModelFilter, TreeModel, TreeIter], bool] = ...
    modify: Callable[[TreeModelFilter, TreeModel, TreeIter, Any, int], None] = ...
    padding: list[None] = ...

class TreeModelFilterPrivate(GObject.GPointer): ...

class TreeModelIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    row_changed: Callable[[TreeModel, TreePath, TreeIter], None] = ...
    row_inserted: Callable[[TreeModel, TreePath, TreeIter], None] = ...
    row_has_child_toggled: Callable[[TreeModel, TreePath, TreeIter], None] = ...
    row_deleted: Callable[[TreeModel, TreePath], None] = ...
    rows_reordered: Callable[[TreeModel, TreePath, TreeIter, int], None] = ...
    get_flags: Callable[[TreeModel], TreeModelFlags] = ...
    get_n_columns: Callable[[TreeModel], int] = ...
    get_column_type: Callable[[TreeModel, int], Type] = ...
    get_iter: Callable[[TreeModel, TreePath], Tuple[bool, TreeIter]] = ...
    get_path: Callable[[TreeModel, TreeIter], TreePath] = ...
    get_value: Callable[[TreeModel, TreeIter, int], Any] = ...
    iter_next: Callable[[TreeModel, TreeIter], bool] = ...
    iter_previous: Callable[[TreeModel, TreeIter], bool] = ...
    iter_children: Callable[
        [TreeModel, Optional[TreeIter]], Tuple[bool, TreeIter]
    ] = ...
    iter_has_child: Callable[[TreeModel, TreeIter], bool] = ...
    iter_n_children: Callable[[TreeModel, Optional[TreeIter]], int] = ...
    iter_nth_child: Callable[
        [TreeModel, Optional[TreeIter], int], Tuple[bool, TreeIter]
    ] = ...
    iter_parent: Callable[[TreeModel, TreeIter], Tuple[bool, TreeIter]] = ...
    ref_node: Callable[[TreeModel, TreeIter], None] = ...
    unref_node: Callable[[TreeModel, TreeIter], None] = ...

class TreeModelRow:
    next = ...  # FIXME Constant
    parent = ...  # FIXME Constant
    path = ...  # FIXME Constant
    previous = ...  # FIXME Constant

    def get_next(self, *args, **kwargs): ...  # FIXME Method
    def get_parent(self, *args, **kwargs): ...  # FIXME Method
    def get_previous(self, *args, **kwargs): ...  # FIXME Method
    def iterchildren(self, *args, **kwargs): ...  # FIXME Method

class TreeModelRowIter: ...

class TreeModelSort(GObject.Object, TreeDragSource, TreeModel, TreeSortable):
    class Props:
        model: TreeModel
    props: Props = ...
    def __init__(self, model: TreeModel = ...): ...
    parent: GObject.Object = ...
    priv: TreeModelSortPrivate = ...
    def clear_cache(self) -> None: ...
    def convert_child_iter_to_iter(
        self, child_iter: TreeIter
    ) -> Tuple[bool, TreeIter]: ...
    def convert_child_path_to_path(
        self, child_path: TreePath
    ) -> Optional[TreePath]: ...
    def convert_iter_to_child_iter(self, sorted_iter: TreeIter) -> TreeIter: ...
    def convert_path_to_child_path(
        self, sorted_path: TreePath
    ) -> Optional[TreePath]: ...
    def get_model(self) -> TreeModel: ...
    def iter_is_valid(self, iter: TreeIter) -> bool: ...
    @classmethod
    def new_with_model(cls, child_model: TreeModel) -> TreeModelSort: ...
    def reset_default_sort_func(self) -> None: ...

class TreeModelSortClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class TreeModelSortPrivate(GObject.GPointer): ...

class TreePath(GObject.GBoxed):
    def append_index(self, index_: int) -> None: ...
    def compare(self, b: TreePath) -> int: ...
    def copy(self) -> TreePath: ...
    def down(self) -> None: ...
    def free(self) -> None: ...
    def get_depth(self) -> int: ...
    def get_indices(self) -> Optional[list[int]]: ...
    def is_ancestor(self, descendant: TreePath) -> bool: ...
    def is_descendant(self, ancestor: TreePath) -> bool: ...
    @classmethod
    def new(cls) -> TreePath: ...
    @classmethod
    def new_first(cls) -> TreePath: ...
    @classmethod
    def new_from_indices(cls, indices: Sequence[int]) -> TreePath: ...
    @classmethod
    def new_from_string(cls, path: str) -> Optional[TreePath]: ...
    def next(self) -> None: ...
    def prepend_index(self, index_: int) -> None: ...
    def prev(self) -> bool: ...
    def to_string(self) -> Optional[str]: ...
    def up(self) -> bool: ...

class TreeRowData(GObject.GBoxed): ...

class TreeRowReference(GObject.GBoxed):
    def copy(self) -> TreeRowReference: ...
    @staticmethod
    def deleted(proxy: GObject.Object, path: TreePath) -> None: ...
    def free(self) -> None: ...
    def get_model(self) -> TreeModel: ...
    def get_path(self) -> Optional[TreePath]: ...
    @staticmethod
    def inserted(proxy: GObject.Object, path: TreePath) -> None: ...
    @classmethod
    def new(cls, model: TreeModel, path: TreePath) -> Optional[TreeRowReference]: ...
    @classmethod
    def new_proxy(
        cls, proxy: GObject.Object, model: TreeModel, path: TreePath
    ) -> Optional[TreeRowReference]: ...
    def valid(self) -> bool: ...

class TreeSelection(GObject.Object):
    class Props:
        mode: SelectionMode
    props: Props = ...
    def __init__(self, mode: SelectionMode = ...): ...
    def count_selected_rows(self) -> int: ...
    def get_mode(self) -> SelectionMode: ...
    def get_selected(self, *args, **kwargs): ...  # FIXME Method
    def get_selected_rows(self, *args, **kwargs): ...  # FIXME Method
    def get_tree_view(self) -> TreeView: ...
    def iter_is_selected(self, iter: TreeIter) -> bool: ...
    def path_is_selected(self, path: TreePath) -> bool: ...
    def select_all(self) -> None: ...
    def select_iter(self, iter: TreeIter) -> None: ...
    def select_path(self, *args, **kwargs): ...  # FIXME Method
    def select_range(self, start_path: TreePath, end_path: TreePath) -> None: ...
    def selected_foreach(self, func: Callable[..., None], *data: Any) -> None: ...
    def set_mode(self, type: SelectionMode) -> None: ...
    def set_select_function(
        self, func: Optional[Callable[..., bool]] = None, *data: Any
    ) -> None: ...
    def unselect_all(self) -> None: ...
    def unselect_iter(self, iter: TreeIter) -> None: ...
    def unselect_path(self, path: TreePath) -> None: ...
    def unselect_range(self, start_path: TreePath, end_path: TreePath) -> None: ...

class TreeSortable(GObject.Object):
    def get_sort_column_id(self, *args, **kwargs): ...  # FIXME Method
    def has_default_sort_func(self) -> bool: ...
    def set_default_sort_func(self, *args, **kwargs): ...  # FIXME Method
    def set_sort_column_id(self, sort_column_id: int, order: SortType) -> None: ...
    def set_sort_func(self, *args, **kwargs): ...  # FIXME Method
    def sort_column_changed(self) -> None: ...

class TreeSortableIface(GObject.GPointer):
    g_iface: GObject.TypeInterface = ...
    sort_column_changed: Callable[[TreeSortable], None] = ...
    get_sort_column_id: Callable[[TreeSortable], Tuple[bool, int, SortType]] = ...
    set_sort_column_id: Callable[[TreeSortable, int, SortType], None] = ...
    set_sort_func: Callable[..., None] = ...
    set_default_sort_func: Callable[..., None] = ...
    has_default_sort_func: Callable[[TreeSortable], bool] = ...

class TreeStore(
    GObject.Object, Buildable, TreeDragDest, TreeDragSource, TreeModel, TreeSortable
):
    parent: GObject.Object = ...
    priv: TreeStorePrivate = ...
    def append(self, *args, **kwargs): ...  # FIXME Method
    def clear(self) -> None: ...
    def insert(self, *args, **kwargs): ...  # FIXME Method
    def insert_after(self, *args, **kwargs): ...  # FIXME Method
    def insert_before(self, *args, **kwargs): ...  # FIXME Method
    def insert_with_values(
        self,
        parent: Optional[TreeIter],
        position: int,
        columns: Sequence[int],
        values: Sequence[Any],
    ) -> TreeIter: ...
    def is_ancestor(self, iter: TreeIter, descendant: TreeIter) -> bool: ...
    def iter_depth(self, iter: TreeIter) -> int: ...
    def iter_is_valid(self, iter: TreeIter) -> bool: ...
    def move_after(
        self, iter: TreeIter, position: Optional[TreeIter] = None
    ) -> None: ...
    def move_before(
        self, iter: TreeIter, position: Optional[TreeIter] = None
    ) -> None: ...
    @classmethod
    def new(cls, n_columns: int, types: Sequence[Type]) -> TreeStore: ...
    def prepend(self, *args, **kwargs): ...  # FIXME Method
    def remove(self, iter: TreeIter) -> bool: ...
    def set(self, *args, **kwargs): ...  # FIXME Method
    def set_column_types(self, n_columns: int, types: Sequence[Type]) -> None: ...
    def set_value(self, *args, **kwargs): ...  # FIXME Method
    def swap(self, a: TreeIter, b: TreeIter) -> None: ...

class TreeStoreClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class TreeStorePrivate(GObject.GPointer): ...

class TreeView(Widget, Accessible, Buildable, ConstraintTarget, Scrollable):
    class Props:
        activate_on_single_click: bool
        enable_grid_lines: TreeViewGridLines
        enable_search: bool
        enable_tree_lines: bool
        expander_column: TreeViewColumn
        fixed_height_mode: bool
        headers_clickable: bool
        headers_visible: bool
        hover_expand: bool
        hover_selection: bool
        level_indentation: int
        model: TreeModel
        reorderable: bool
        rubber_banding: bool
        search_column: int
        show_expanders: bool
        tooltip_column: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        activate_on_single_click: bool = ...,
        enable_grid_lines: TreeViewGridLines = ...,
        enable_search: bool = ...,
        enable_tree_lines: bool = ...,
        expander_column: TreeViewColumn = ...,
        fixed_height_mode: bool = ...,
        headers_clickable: bool = ...,
        headers_visible: bool = ...,
        hover_expand: bool = ...,
        hover_selection: bool = ...,
        level_indentation: int = ...,
        model: TreeModel = ...,
        reorderable: bool = ...,
        rubber_banding: bool = ...,
        search_column: int = ...,
        show_expanders: bool = ...,
        tooltip_column: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    parent_instance: Widget = ...
    def append_column(self, column: TreeViewColumn) -> int: ...
    def collapse_all(self) -> None: ...
    def collapse_row(self, path: TreePath) -> bool: ...
    def columns_autosize(self) -> None: ...
    def convert_bin_window_to_tree_coords(
        self, bx: int, by: int
    ) -> Tuple[int, int]: ...
    def convert_bin_window_to_widget_coords(
        self, bx: int, by: int
    ) -> Tuple[int, int]: ...
    def convert_tree_to_bin_window_coords(
        self, tx: int, ty: int
    ) -> Tuple[int, int]: ...
    def convert_tree_to_widget_coords(self, tx: int, ty: int) -> Tuple[int, int]: ...
    def convert_widget_to_bin_window_coords(
        self, wx: int, wy: int
    ) -> Tuple[int, int]: ...
    def convert_widget_to_tree_coords(self, wx: int, wy: int) -> Tuple[int, int]: ...
    def create_row_drag_icon(self, path: TreePath) -> Optional[Gdk.Paintable]: ...
    def do_columns_changed(self) -> None: ...
    def do_cursor_changed(self) -> None: ...
    def do_expand_collapse_cursor_row(
        self, logical: bool, expand: bool, open_all: bool
    ) -> bool: ...
    def do_move_cursor(
        self, step: MovementStep, count: int, extend: bool, modify: bool
    ) -> bool: ...
    def do_row_activated(
        self, path: TreePath, column: Optional[TreeViewColumn] = None
    ) -> None: ...
    def do_row_collapsed(self, iter: TreeIter, path: TreePath) -> None: ...
    def do_row_expanded(self, iter: TreeIter, path: TreePath) -> None: ...
    def do_select_all(self) -> bool: ...
    def do_select_cursor_parent(self) -> bool: ...
    def do_select_cursor_row(self, start_editing: bool) -> bool: ...
    def do_start_interactive_search(self) -> bool: ...
    def do_test_collapse_row(self, iter: TreeIter, path: TreePath) -> bool: ...
    def do_test_expand_row(self, iter: TreeIter, path: TreePath) -> bool: ...
    def do_toggle_cursor_row(self) -> bool: ...
    def do_unselect_all(self) -> bool: ...
    def enable_model_drag_dest(
        self, formats: Gdk.ContentFormats, actions: Gdk.DragAction
    ) -> None: ...
    def enable_model_drag_source(
        self,
        start_button_mask: Gdk.ModifierType,
        formats: Gdk.ContentFormats,
        actions: Gdk.DragAction,
    ) -> None: ...
    def expand_all(self) -> None: ...
    def expand_row(self, path: TreePath, open_all: bool) -> bool: ...
    def expand_to_path(self, path: TreePath) -> None: ...
    def get_activate_on_single_click(self) -> bool: ...
    def get_background_area(
        self, path: Optional[TreePath] = None, column: Optional[TreeViewColumn] = None
    ) -> Gdk.Rectangle: ...
    def get_cell_area(self, *args, **kwargs): ...  # FIXME Method
    def get_column(self, n: int) -> Optional[TreeViewColumn]: ...
    def get_columns(self) -> list[TreeViewColumn]: ...
    def get_cursor(self) -> Tuple[TreePath, TreeViewColumn]: ...
    def get_dest_row_at_pos(self, *args, **kwargs): ...  # FIXME Method
    def get_drag_dest_row(self) -> Tuple[TreePath, TreeViewDropPosition]: ...
    def get_enable_search(self) -> bool: ...
    def get_enable_tree_lines(self) -> bool: ...
    def get_expander_column(self) -> Optional[TreeViewColumn]: ...
    def get_fixed_height_mode(self) -> bool: ...
    def get_grid_lines(self) -> TreeViewGridLines: ...
    def get_headers_clickable(self) -> bool: ...
    def get_headers_visible(self) -> bool: ...
    def get_hover_expand(self) -> bool: ...
    def get_hover_selection(self) -> bool: ...
    def get_level_indentation(self) -> int: ...
    def get_model(self) -> Optional[TreeModel]: ...
    def get_n_columns(self) -> int: ...
    def get_path_at_pos(self, *args, **kwargs): ...  # FIXME Method
    def get_reorderable(self) -> bool: ...
    def get_rubber_banding(self) -> bool: ...
    def get_search_column(self) -> int: ...
    def get_search_entry(self) -> Optional[Editable]: ...
    def get_selection(self) -> TreeSelection: ...
    def get_show_expanders(self) -> bool: ...
    def get_tooltip_column(self) -> int: ...
    def get_tooltip_context(
        self, x: int, y: int, keyboard_tip: bool
    ) -> Tuple[bool, TreeModel, TreePath, TreeIter]: ...
    def get_visible_range(self, *args, **kwargs): ...  # FIXME Method
    def get_visible_rect(self) -> Gdk.Rectangle: ...
    def insert_column(self, column: TreeViewColumn, position: int) -> int: ...
    def insert_column_with_attributes(self, *args, **kwargs): ...  # FIXME Method
    def insert_column_with_data_func(
        self,
        position: int,
        title: str,
        cell: CellRenderer,
        func: Callable[..., None],
        *data: Any,
    ) -> int: ...
    def is_blank_at_pos(
        self, x: int, y: int
    ) -> Tuple[bool, TreePath, TreeViewColumn, int, int]: ...
    def is_rubber_banding_active(self) -> bool: ...
    def map_expanded_rows(self, func: Callable[..., None], *data: Any) -> None: ...
    def move_column_after(
        self, column: TreeViewColumn, base_column: Optional[TreeViewColumn] = None
    ) -> None: ...
    @classmethod
    def new(cls) -> TreeView: ...
    @classmethod
    def new_with_model(cls, model: TreeModel) -> TreeView: ...
    def remove_column(self, column: TreeViewColumn) -> int: ...
    def row_activated(
        self, path: TreePath, column: Optional[TreeViewColumn] = None
    ) -> None: ...
    def row_expanded(self, path: TreePath) -> bool: ...
    def scroll_to_cell(self, *args, **kwargs): ...  # FIXME Method
    def scroll_to_point(self, tree_x: int, tree_y: int) -> None: ...
    def set_activate_on_single_click(self, single: bool) -> None: ...
    def set_column_drag_function(
        self, func: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> None: ...
    def set_cursor(self, *args, **kwargs): ...  # FIXME Method
    def set_cursor_on_cell(
        self,
        path: TreePath,
        focus_column: Optional[TreeViewColumn],
        focus_cell: Optional[CellRenderer],
        start_editing: bool,
    ) -> None: ...
    def set_drag_dest_row(
        self, path: Optional[TreePath], pos: TreeViewDropPosition
    ) -> None: ...
    def set_enable_search(self, enable_search: bool) -> None: ...
    def set_enable_tree_lines(self, enabled: bool) -> None: ...
    def set_expander_column(self, column: Optional[TreeViewColumn] = None) -> None: ...
    def set_fixed_height_mode(self, enable: bool) -> None: ...
    def set_grid_lines(self, grid_lines: TreeViewGridLines) -> None: ...
    def set_headers_clickable(self, setting: bool) -> None: ...
    def set_headers_visible(self, headers_visible: bool) -> None: ...
    def set_hover_expand(self, expand: bool) -> None: ...
    def set_hover_selection(self, hover: bool) -> None: ...
    def set_level_indentation(self, indentation: int) -> None: ...
    def set_model(self, model: Optional[TreeModel] = None) -> None: ...
    def set_reorderable(self, reorderable: bool) -> None: ...
    def set_row_separator_func(
        self, func: Optional[Callable[..., bool]] = None, *data: Any
    ) -> None: ...
    def set_rubber_banding(self, enable: bool) -> None: ...
    def set_search_column(self, column: int) -> None: ...
    def set_search_entry(self, entry: Optional[Editable] = None) -> None: ...
    def set_search_equal_func(
        self, search_equal_func: Callable[..., bool], *search_user_data: Any
    ) -> None: ...
    def set_show_expanders(self, enabled: bool) -> None: ...
    def set_tooltip_cell(
        self,
        tooltip: Tooltip,
        path: Optional[TreePath] = None,
        column: Optional[TreeViewColumn] = None,
        cell: Optional[CellRenderer] = None,
    ) -> None: ...
    def set_tooltip_column(self, column: int) -> None: ...
    def set_tooltip_row(self, tooltip: Tooltip, path: TreePath) -> None: ...
    def unset_rows_drag_dest(self) -> None: ...
    def unset_rows_drag_source(self) -> None: ...

class TreeViewClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    row_activated: Callable[[TreeView, TreePath, Optional[TreeViewColumn]], None] = ...
    test_expand_row: Callable[[TreeView, TreeIter, TreePath], bool] = ...
    test_collapse_row: Callable[[TreeView, TreeIter, TreePath], bool] = ...
    row_expanded: Callable[[TreeView, TreeIter, TreePath], None] = ...
    row_collapsed: Callable[[TreeView, TreeIter, TreePath], None] = ...
    columns_changed: Callable[[TreeView], None] = ...
    cursor_changed: Callable[[TreeView], None] = ...
    move_cursor: Callable[[TreeView, MovementStep, int, bool, bool], bool] = ...
    select_all: Callable[[TreeView], bool] = ...
    unselect_all: Callable[[TreeView], bool] = ...
    select_cursor_row: Callable[[TreeView, bool], bool] = ...
    toggle_cursor_row: Callable[[TreeView], bool] = ...
    expand_collapse_cursor_row: Callable[[TreeView, bool, bool, bool], bool] = ...
    select_cursor_parent: Callable[[TreeView], bool] = ...
    start_interactive_search: Callable[[TreeView], bool] = ...
    _reserved: list[None] = ...

class TreeViewColumn(GObject.InitiallyUnowned, Buildable, CellLayout):
    class Props:
        alignment: float
        cell_area: CellArea
        clickable: bool
        expand: bool
        fixed_width: int
        max_width: int
        min_width: int
        reorderable: bool
        resizable: bool
        sizing: TreeViewColumnSizing
        sort_column_id: int
        sort_indicator: bool
        sort_order: SortType
        spacing: int
        title: str
        visible: bool
        widget: Widget
        width: int
        x_offset: int
    props: Props = ...
    def __init__(
        self,
        alignment: float = ...,
        cell_area: CellArea = ...,
        clickable: bool = ...,
        expand: bool = ...,
        fixed_width: int = ...,
        max_width: int = ...,
        min_width: int = ...,
        reorderable: bool = ...,
        resizable: bool = ...,
        sizing: TreeViewColumnSizing = ...,
        sort_column_id: int = ...,
        sort_indicator: bool = ...,
        sort_order: SortType = ...,
        spacing: int = ...,
        title: str = ...,
        visible: bool = ...,
        widget: Widget = ...,
    ): ...
    def add_attribute(
        self, cell_renderer: CellRenderer, attribute: str, column: int
    ) -> None: ...
    def cell_get_position(self, *args, **kwargs): ...  # FIXME Method
    def cell_get_size(self) -> Tuple[int, int, int, int]: ...
    def cell_is_visible(self) -> bool: ...
    def cell_set_cell_data(
        self,
        tree_model: TreeModel,
        iter: TreeIter,
        is_expander: bool,
        is_expanded: bool,
    ) -> None: ...
    def clear(self) -> None: ...
    def clear_attributes(self, cell_renderer: CellRenderer) -> None: ...
    def clicked(self) -> None: ...
    def focus_cell(self, cell: CellRenderer) -> None: ...
    def get_alignment(self) -> float: ...
    def get_button(self) -> Widget: ...
    def get_clickable(self) -> bool: ...
    def get_expand(self) -> bool: ...
    def get_fixed_width(self) -> int: ...
    def get_max_width(self) -> int: ...
    def get_min_width(self) -> int: ...
    def get_reorderable(self) -> bool: ...
    def get_resizable(self) -> bool: ...
    def get_sizing(self) -> TreeViewColumnSizing: ...
    def get_sort_column_id(self) -> int: ...
    def get_sort_indicator(self) -> bool: ...
    def get_sort_order(self) -> SortType: ...
    def get_spacing(self) -> int: ...
    def get_title(self) -> str: ...
    def get_tree_view(self) -> Optional[Widget]: ...
    def get_visible(self) -> bool: ...
    def get_widget(self) -> Optional[Widget]: ...
    def get_width(self) -> int: ...
    def get_x_offset(self) -> int: ...
    @classmethod
    def new(cls) -> TreeViewColumn: ...
    @classmethod
    def new_with_area(cls, area: CellArea) -> TreeViewColumn: ...
    def pack_end(self, cell: CellRenderer, expand: bool) -> None: ...
    def pack_start(self, cell: CellRenderer, expand: bool) -> None: ...
    def queue_resize(self) -> None: ...
    def set_alignment(self, xalign: float) -> None: ...
    def set_attributes(self, *args, **kwargs): ...  # FIXME Method
    def set_cell_data_func(self, *args, **kwargs): ...  # FIXME Method
    def set_clickable(self, clickable: bool) -> None: ...
    def set_expand(self, expand: bool) -> None: ...
    def set_fixed_width(self, fixed_width: int) -> None: ...
    def set_max_width(self, max_width: int) -> None: ...
    def set_min_width(self, min_width: int) -> None: ...
    def set_reorderable(self, reorderable: bool) -> None: ...
    def set_resizable(self, resizable: bool) -> None: ...
    def set_sizing(self, type: TreeViewColumnSizing) -> None: ...
    def set_sort_column_id(self, sort_column_id: int) -> None: ...
    def set_sort_indicator(self, setting: bool) -> None: ...
    def set_sort_order(self, order: SortType) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def set_widget(self, widget: Optional[Widget] = None) -> None: ...

class Video(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        autoplay: bool
        file: Gio.File
        loop: bool
        media_stream: MediaStream
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        autoplay: bool = ...,
        file: Gio.File = ...,
        loop: bool = ...,
        media_stream: MediaStream = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_autoplay(self) -> bool: ...
    def get_file(self) -> Optional[Gio.File]: ...
    def get_loop(self) -> bool: ...
    def get_media_stream(self) -> Optional[MediaStream]: ...
    @classmethod
    def new(cls) -> Video: ...
    @classmethod
    def new_for_file(cls, file: Optional[Gio.File] = None) -> Video: ...
    @classmethod
    def new_for_filename(cls, filename: Optional[str] = None) -> Video: ...
    @classmethod
    def new_for_media_stream(cls, stream: Optional[MediaStream] = None) -> Video: ...
    @classmethod
    def new_for_resource(cls, resource_path: Optional[str] = None) -> Video: ...
    def set_autoplay(self, autoplay: bool) -> None: ...
    def set_file(self, file: Optional[Gio.File] = None) -> None: ...
    def set_filename(self, filename: Optional[str] = None) -> None: ...
    def set_loop(self, loop: bool) -> None: ...
    def set_media_stream(self, stream: Optional[MediaStream] = None) -> None: ...
    def set_resource(self, resource_path: Optional[str] = None) -> None: ...

class VideoClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class Viewport(Widget, Accessible, Buildable, ConstraintTarget, Scrollable):
    class Props:
        child: Widget
        scroll_to_focus: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        hadjustment: Adjustment
        hscroll_policy: ScrollablePolicy
        vadjustment: Adjustment
        vscroll_policy: ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        scroll_to_focus: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        hadjustment: Adjustment = ...,
        hscroll_policy: ScrollablePolicy = ...,
        vadjustment: Adjustment = ...,
        vscroll_policy: ScrollablePolicy = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    def get_scroll_to_focus(self) -> bool: ...
    @classmethod
    def new(
        cls,
        hadjustment: Optional[Adjustment] = None,
        vadjustment: Optional[Adjustment] = None,
    ) -> Viewport: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_scroll_to_focus(self, scroll_to_focus: bool) -> None: ...

class VolumeButton(ScaleButton, Accessible, Buildable, ConstraintTarget, Orientable):
    class Props:
        use_symbolic: bool
        adjustment: Adjustment
        icons: list[str]
        value: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
        orientation: Orientation
    props: Props = ...
    def __init__(
        self,
        use_symbolic: bool = ...,
        adjustment: Adjustment = ...,
        icons: Sequence[str] = ...,
        value: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
        orientation: Orientation = ...,
    ): ...
    parent: ScaleButton = ...
    @classmethod
    def new(cls) -> VolumeButton: ...

class Widget(GObject.InitiallyUnowned, Accessible, Buildable, ConstraintTarget):
    class Props:
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: GObject.InitiallyUnowned = ...
    priv: WidgetPrivate = ...
    def action_set_enabled(self, action_name: str, enabled: bool) -> None: ...
    def activate(self) -> bool: ...
    def activate_action(
        self, name: str, args: Optional[GLib.Variant] = None
    ) -> bool: ...
    def activate_default(self) -> None: ...
    def add_controller(self, controller: EventController) -> None: ...
    def add_css_class(self, css_class: str) -> None: ...
    def add_mnemonic_label(self, label: Widget) -> None: ...
    def add_shortcut(self, shortcut: Shortcut) -> None: ...
    def add_tick_callback(
        self, callback: Callable[..., bool], *user_data: Any
    ) -> int: ...
    def allocate(
        self,
        width: int,
        height: int,
        baseline: int,
        transform: Optional[Gsk.Transform] = None,
    ) -> None: ...
    def bind_template_callback_full(
        self, callback_name: str, callback_symbol: Callable[[], None]
    ) -> None: ...
    def bind_template_child_full(
        self, name: str, internal_child: bool, struct_offset: int
    ) -> None: ...
    def child_focus(self, direction: DirectionType) -> bool: ...
    def compute_bounds(self, target: Widget) -> Tuple[bool, Graphene.Rect]: ...
    def compute_expand(self, orientation: Orientation) -> bool: ...
    def compute_point(
        self, target: Widget, point: Graphene.Point
    ) -> Tuple[bool, Graphene.Point]: ...
    def compute_transform(self, target: Widget) -> Tuple[bool, Graphene.Matrix]: ...
    def contains(self, x: float, y: float) -> bool: ...
    def create_pango_context(self) -> Pango.Context: ...
    def create_pango_layout(self, text: Optional[str] = None) -> Pango.Layout: ...
    def dispose_template(self, widget_type: Type) -> None: ...
    def do_compute_expand(self, hexpand_p: bool, vexpand_p: bool) -> None: ...
    def do_contains(self, x: float, y: float) -> bool: ...
    def do_css_changed(self, change: CssStyleChange) -> None: ...
    def do_direction_changed(self, previous_direction: TextDirection) -> None: ...
    def do_focus(self, direction: DirectionType) -> bool: ...
    def do_get_request_mode(self) -> SizeRequestMode: ...
    def do_grab_focus(self) -> bool: ...
    def do_hide(self) -> None: ...
    def do_keynav_failed(self, direction: DirectionType) -> bool: ...
    def do_map(self) -> None: ...
    def do_measure(
        self, orientation: Orientation, for_size: int
    ) -> Tuple[int, int, int, int]: ...
    def do_mnemonic_activate(self, group_cycling: bool) -> bool: ...
    def do_move_focus(self, direction: DirectionType) -> None: ...
    def do_query_tooltip(
        self, x: int, y: int, keyboard_tooltip: bool, tooltip: Tooltip
    ) -> bool: ...
    def do_realize(self) -> None: ...
    def do_root(self) -> None: ...
    def do_set_focus_child(self, child: Optional[Widget] = None) -> None: ...
    def do_show(self) -> None: ...
    def do_size_allocate(self, width: int, height: int, baseline: int) -> None: ...
    def do_snapshot(self, snapshot: Snapshot) -> None: ...
    def do_state_flags_changed(self, previous_state_flags: StateFlags) -> None: ...
    def do_system_setting_changed(self, settings: SystemSetting) -> None: ...
    def do_unmap(self) -> None: ...
    def do_unrealize(self) -> None: ...
    def do_unroot(self) -> None: ...
    def drag_check_threshold(
        self, start_x: int, start_y: int, current_x: int, current_y: int
    ) -> bool: ...
    def error_bell(self) -> None: ...
    def get_activate_signal(self) -> int: ...
    def get_allocated_baseline(self) -> int: ...
    def get_allocated_height(self) -> int: ...
    def get_allocated_width(self) -> int: ...
    def get_allocation(self) -> Gdk.Rectangle: ...
    def get_ancestor(self, widget_type: Type) -> Optional[Widget]: ...
    def get_can_focus(self) -> bool: ...
    def get_can_target(self) -> bool: ...
    def get_child_visible(self) -> bool: ...
    def get_clipboard(self) -> Gdk.Clipboard: ...
    def get_css_classes(self) -> list[str]: ...
    def get_css_name(self) -> str: ...
    def get_cursor(self) -> Optional[Gdk.Cursor]: ...
    @staticmethod
    def get_default_direction() -> TextDirection: ...
    def get_direction(self) -> TextDirection: ...
    def get_display(self) -> Gdk.Display: ...
    def get_first_child(self) -> Optional[Widget]: ...
    def get_focus_child(self) -> Optional[Widget]: ...
    def get_focus_on_click(self) -> bool: ...
    def get_focusable(self) -> bool: ...
    def get_font_map(self) -> Optional[Pango.FontMap]: ...
    def get_font_options(self) -> Optional[cairo.FontOptions]: ...
    def get_frame_clock(self) -> Optional[Gdk.FrameClock]: ...
    def get_halign(self) -> Align: ...
    def get_has_tooltip(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_hexpand(self) -> bool: ...
    def get_hexpand_set(self) -> bool: ...
    def get_last_child(self) -> Optional[Widget]: ...
    def get_layout_manager(self) -> Optional[LayoutManager]: ...
    def get_layout_manager_type(self) -> Type: ...
    def get_mapped(self) -> bool: ...
    def get_margin_bottom(self) -> int: ...
    def get_margin_end(self) -> int: ...
    def get_margin_start(self) -> int: ...
    def get_margin_top(self) -> int: ...
    def get_name(self) -> str: ...
    def get_native(self) -> Optional[Native]: ...
    def get_next_sibling(self) -> Optional[Widget]: ...
    def get_opacity(self) -> float: ...
    def get_overflow(self) -> Overflow: ...
    def get_pango_context(self) -> Pango.Context: ...
    def get_parent(self) -> Optional[Widget]: ...
    def get_preferred_size(self) -> Tuple[Requisition, Requisition]: ...
    def get_prev_sibling(self) -> Optional[Widget]: ...
    def get_primary_clipboard(self) -> Gdk.Clipboard: ...
    def get_realized(self) -> bool: ...
    def get_receives_default(self) -> bool: ...
    def get_request_mode(self) -> SizeRequestMode: ...
    def get_root(self) -> Optional[Root]: ...
    def get_scale_factor(self) -> int: ...
    def get_sensitive(self) -> bool: ...
    def get_settings(self) -> Settings: ...
    def get_size(self, orientation: Orientation) -> int: ...
    def get_size_request(self) -> Tuple[int, int]: ...
    def get_state_flags(self) -> StateFlags: ...
    def get_style_context(self) -> StyleContext: ...
    def get_template_child(self, widget_type: Type, name: str) -> GObject.Object: ...
    def get_tooltip_markup(self) -> Optional[str]: ...
    def get_tooltip_text(self) -> Optional[str]: ...
    def get_valign(self) -> Align: ...
    def get_vexpand(self) -> bool: ...
    def get_vexpand_set(self) -> bool: ...
    def get_visible(self) -> bool: ...
    def get_width(self) -> int: ...
    def grab_focus(self) -> bool: ...
    def has_css_class(self, css_class: str) -> bool: ...
    def has_default(self) -> bool: ...
    def has_focus(self) -> bool: ...
    def has_visible_focus(self) -> bool: ...
    def hide(self) -> None: ...
    def in_destruction(self) -> bool: ...
    def init_template(self) -> None: ...
    def insert_action_group(
        self, name: str, group: Optional[Gio.ActionGroup] = None
    ) -> None: ...
    def insert_after(
        self, parent: Widget, previous_sibling: Optional[Widget] = None
    ) -> None: ...
    def insert_before(
        self, parent: Widget, next_sibling: Optional[Widget] = None
    ) -> None: ...
    def install_action(
        self,
        action_name: str,
        parameter_type: Optional[str],
        activate: Callable[[Widget, str, GLib.Variant], None],
    ) -> None: ...
    def install_property_action(self, action_name: str, property_name: str) -> None: ...
    def is_ancestor(self, ancestor: Widget) -> bool: ...
    def is_drawable(self) -> bool: ...
    def is_focus(self) -> bool: ...
    def is_sensitive(self) -> bool: ...
    def is_visible(self) -> bool: ...
    def keynav_failed(self, direction: DirectionType) -> bool: ...
    def list_mnemonic_labels(self) -> list[Widget]: ...
    def map(self) -> None: ...
    def measure(
        self, orientation: Orientation, for_size: int
    ) -> Tuple[int, int, int, int]: ...
    def mnemonic_activate(self, group_cycling: bool) -> bool: ...
    def observe_children(self) -> Gio.ListModel: ...
    def observe_controllers(self) -> Gio.ListModel: ...
    def pick(self, x: float, y: float, flags: PickFlags) -> Optional[Widget]: ...
    def query_action(
        self, index_: int
    ) -> Tuple[bool, Type, str, GLib.VariantType, str]: ...
    def queue_allocate(self) -> None: ...
    def queue_draw(self) -> None: ...
    def queue_resize(self) -> None: ...
    def realize(self) -> None: ...
    def remove_controller(self, controller: EventController) -> None: ...
    def remove_css_class(self, css_class: str) -> None: ...
    def remove_mnemonic_label(self, label: Widget) -> None: ...
    def remove_tick_callback(self, id: int) -> None: ...
    def set_accessible_role(self, accessible_role: AccessibleRole) -> None: ...
    def set_activate_signal(self, signal_id: int) -> None: ...
    def set_activate_signal_from_name(self, signal_name: str) -> None: ...
    def set_can_focus(self, can_focus: bool) -> None: ...
    def set_can_target(self, can_target: bool) -> None: ...
    def set_child_visible(self, child_visible: bool) -> None: ...
    def set_css_classes(self, classes: Sequence[str]) -> None: ...
    def set_css_name(self, name: str) -> None: ...
    def set_cursor(self, cursor: Optional[Gdk.Cursor] = None) -> None: ...
    def set_cursor_from_name(self, name: Optional[str] = None) -> None: ...
    @staticmethod
    def set_default_direction(dir: TextDirection) -> None: ...
    def set_direction(self, dir: TextDirection) -> None: ...
    def set_focus_child(self, child: Optional[Widget] = None) -> None: ...
    def set_focus_on_click(self, focus_on_click: bool) -> None: ...
    def set_focusable(self, focusable: bool) -> None: ...
    def set_font_map(self, font_map: Optional[Pango.FontMap] = None) -> None: ...
    def set_font_options(self, options: Optional[cairo.FontOptions] = None) -> None: ...
    def set_halign(self, align: Align) -> None: ...
    def set_has_tooltip(self, has_tooltip: bool) -> None: ...
    def set_hexpand(self, expand: bool) -> None: ...
    def set_hexpand_set(self, set: bool) -> None: ...
    def set_layout_manager(
        self, layout_manager: Optional[LayoutManager] = None
    ) -> None: ...
    def set_layout_manager_type(self, type: Type) -> None: ...
    def set_margin_bottom(self, margin: int) -> None: ...
    def set_margin_end(self, margin: int) -> None: ...
    def set_margin_start(self, margin: int) -> None: ...
    def set_margin_top(self, margin: int) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_opacity(self, opacity: float) -> None: ...
    def set_overflow(self, overflow: Overflow) -> None: ...
    def set_parent(self, parent: Widget) -> None: ...
    def set_receives_default(self, receives_default: bool) -> None: ...
    def set_sensitive(self, sensitive: bool) -> None: ...
    def set_size_request(self, width: int, height: int) -> None: ...
    def set_state_flags(self, flags: StateFlags, clear: bool) -> None: ...
    def set_template(self, template_bytes: GLib.Bytes) -> None: ...
    def set_template_from_resource(self, resource_name: str) -> None: ...
    def set_template_scope(self, scope: BuilderScope) -> None: ...
    def set_tooltip_markup(self, markup: Optional[str] = None) -> None: ...
    def set_tooltip_text(self, text: Optional[str] = None) -> None: ...
    def set_valign(self, align: Align) -> None: ...
    def set_vexpand(self, expand: bool) -> None: ...
    def set_vexpand_set(self, set: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def should_layout(self) -> bool: ...
    def show(self) -> None: ...
    def size_allocate(self, allocation: Gdk.Rectangle, baseline: int) -> None: ...
    def snapshot_child(self, child: Widget, snapshot: Snapshot) -> None: ...
    def translate_coordinates(self, *args, **kwargs): ...  # FIXME Method
    def trigger_tooltip_query(self) -> None: ...
    def unmap(self) -> None: ...
    def unparent(self) -> None: ...
    def unrealize(self) -> None: ...
    def unset_state_flags(self, flags: StateFlags) -> None: ...

class WidgetClass(GObject.GPointer):
    parent_class: GObject.InitiallyUnownedClass = ...
    show: Callable[[Widget], None] = ...
    hide: Callable[[Widget], None] = ...
    map: Callable[[Widget], None] = ...
    unmap: Callable[[Widget], None] = ...
    realize: Callable[[Widget], None] = ...
    unrealize: Callable[[Widget], None] = ...
    root: Callable[[Widget], None] = ...
    unroot: Callable[[Widget], None] = ...
    size_allocate: Callable[[Widget, int, int, int], None] = ...
    state_flags_changed: Callable[[Widget, StateFlags], None] = ...
    direction_changed: Callable[[Widget, TextDirection], None] = ...
    get_request_mode: Callable[[Widget], SizeRequestMode] = ...
    measure: Callable[[Widget, Orientation, int], Tuple[int, int, int, int]] = ...
    mnemonic_activate: Callable[[Widget, bool], bool] = ...
    grab_focus: Callable[[Widget], bool] = ...
    focus: Callable[[Widget, DirectionType], bool] = ...
    set_focus_child: Callable[[Widget, Optional[Widget]], None] = ...
    move_focus: Callable[[Widget, DirectionType], None] = ...
    keynav_failed: Callable[[Widget, DirectionType], bool] = ...
    query_tooltip: Callable[[Widget, int, int, bool, Tooltip], bool] = ...
    compute_expand: Callable[[Widget, bool, bool], None] = ...
    css_changed: Callable[[Widget, CssStyleChange], None] = ...
    system_setting_changed: Callable[[Widget, SystemSetting], None] = ...
    snapshot: Callable[[Widget, Snapshot], None] = ...
    contains: Callable[[Widget, float, float], bool] = ...
    priv: WidgetClassPrivate = ...
    padding: list[None] = ...
    def add_shortcut(self, shortcut: Shortcut) -> None: ...
    def bind_template_callback_full(
        self, callback_name: str, callback_symbol: Callable[[], None]
    ) -> None: ...
    def bind_template_child_full(
        self, name: str, internal_child: bool, struct_offset: int
    ) -> None: ...
    def get_accessible_role(self) -> AccessibleRole: ...
    def get_activate_signal(self) -> int: ...
    def get_css_name(self) -> str: ...
    def get_layout_manager_type(self) -> Type: ...
    def install_action(
        self,
        action_name: str,
        parameter_type: Optional[str],
        activate: Callable[[Widget, str, GLib.Variant], None],
    ) -> None: ...
    def install_property_action(self, action_name: str, property_name: str) -> None: ...
    def query_action(
        self, index_: int
    ) -> Tuple[bool, Type, str, GLib.VariantType, str]: ...
    def set_accessible_role(self, accessible_role: AccessibleRole) -> None: ...
    def set_activate_signal(self, signal_id: int) -> None: ...
    def set_activate_signal_from_name(self, signal_name: str) -> None: ...
    def set_css_name(self, name: str) -> None: ...
    def set_layout_manager_type(self, type: Type) -> None: ...
    def set_template(self, template_bytes: GLib.Bytes) -> None: ...
    def set_template_from_resource(self, resource_name: str) -> None: ...
    def set_template_scope(self, scope: BuilderScope) -> None: ...

class WidgetClassPrivate(GObject.GPointer): ...

class WidgetPaintable(GObject.Object, Gdk.Paintable):
    class Props:
        widget: Widget
    props: Props = ...
    def __init__(self, widget: Widget = ...): ...
    def get_widget(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls, widget: Optional[Widget] = None) -> WidgetPaintable: ...
    def set_widget(self, widget: Optional[Widget] = None) -> None: ...

class WidgetPaintableClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class WidgetPrivate(GObject.GPointer): ...

class Window(
    Widget, Accessible, Buildable, ConstraintTarget, Native, Root, ShortcutManager
):
    class Props:
        application: Application
        child: Widget
        decorated: bool
        default_height: int
        default_widget: Widget
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: str
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        startup_id: str
        title: str
        titlebar: Widget
        transient_for: Window
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        application: Application = ...,
        child: Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Widget = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: str = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        titlebar: Widget = ...,
        transient_for: Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    parent_instance: Widget = ...
    def close(self) -> None: ...
    def destroy(self) -> None: ...
    def do_activate_default(self) -> None: ...
    def do_activate_focus(self) -> None: ...
    def do_close_request(self) -> bool: ...
    def do_enable_debugging(self, toggle: bool) -> bool: ...
    def do_keys_changed(self) -> None: ...
    def fullscreen(self) -> None: ...
    def fullscreen_on_monitor(self, monitor: Gdk.Monitor) -> None: ...
    def get_application(self) -> Optional[Application]: ...
    def get_child(self) -> Optional[Widget]: ...
    def get_decorated(self) -> bool: ...
    @staticmethod
    def get_default_icon_name() -> Optional[str]: ...
    def get_default_size(self) -> Tuple[int, int]: ...
    def get_default_widget(self) -> Optional[Widget]: ...
    def get_deletable(self) -> bool: ...
    def get_destroy_with_parent(self) -> bool: ...
    def get_focus(self) -> Optional[Widget]: ...
    def get_focus_visible(self) -> bool: ...
    def get_group(self) -> WindowGroup: ...
    def get_handle_menubar_accel(self) -> bool: ...
    def get_hide_on_close(self) -> bool: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_mnemonics_visible(self) -> bool: ...
    def get_modal(self) -> bool: ...
    def get_resizable(self) -> bool: ...
    def get_title(self) -> Optional[str]: ...
    def get_titlebar(self) -> Optional[Widget]: ...
    @staticmethod
    def get_toplevels() -> Gio.ListModel: ...
    def get_transient_for(self) -> Optional[Window]: ...
    def has_group(self) -> bool: ...
    def is_active(self) -> bool: ...
    def is_fullscreen(self) -> bool: ...
    def is_maximized(self) -> bool: ...
    @staticmethod
    def list_toplevels() -> list[Widget]: ...
    def maximize(self) -> None: ...
    def minimize(self) -> None: ...
    @classmethod
    def new(cls) -> Window: ...
    def present(self) -> None: ...
    def present_with_time(self, timestamp: int) -> None: ...
    def set_application(self, application: Optional[Application] = None) -> None: ...
    @staticmethod
    def set_auto_startup_notification(setting: bool) -> None: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...
    def set_decorated(self, setting: bool) -> None: ...
    @staticmethod
    def set_default_icon_name(name: str) -> None: ...
    def set_default_size(self, width: int, height: int) -> None: ...
    def set_default_widget(self, default_widget: Optional[Widget] = None) -> None: ...
    def set_deletable(self, setting: bool) -> None: ...
    def set_destroy_with_parent(self, setting: bool) -> None: ...
    def set_display(self, display: Gdk.Display) -> None: ...
    def set_focus(self, focus: Optional[Widget] = None) -> None: ...
    def set_focus_visible(self, setting: bool) -> None: ...
    def set_handle_menubar_accel(self, handle_menubar_accel: bool) -> None: ...
    def set_hide_on_close(self, setting: bool) -> None: ...
    def set_icon_name(self, name: Optional[str] = None) -> None: ...
    @staticmethod
    def set_interactive_debugging(enable: bool) -> None: ...
    def set_mnemonics_visible(self, setting: bool) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_resizable(self, resizable: bool) -> None: ...
    def set_startup_id(self, startup_id: str) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_titlebar(self, titlebar: Optional[Widget] = None) -> None: ...
    def set_transient_for(self, parent: Optional[Window] = None) -> None: ...
    def unfullscreen(self) -> None: ...
    def unmaximize(self) -> None: ...
    def unminimize(self) -> None: ...

class WindowClass(GObject.GPointer):
    parent_class: WidgetClass = ...
    activate_focus: Callable[[Window], None] = ...
    activate_default: Callable[[Window], None] = ...
    keys_changed: Callable[[Window], None] = ...
    enable_debugging: Callable[[Window, bool], bool] = ...
    close_request: Callable[[Window], bool] = ...
    padding: list[None] = ...

class WindowControls(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        decoration_layout: str
        empty: bool
        side: PackType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        decoration_layout: str = ...,
        side: PackType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_decoration_layout(self) -> Optional[str]: ...
    def get_empty(self) -> bool: ...
    def get_side(self) -> PackType: ...
    @classmethod
    def new(cls, side: PackType) -> WindowControls: ...
    def set_decoration_layout(self, layout: Optional[str] = None) -> None: ...
    def set_side(self, side: PackType) -> None: ...

class WindowControlsClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class WindowGroup(GObject.Object):
    parent_instance: GObject.Object = ...
    priv: WindowGroupPrivate = ...
    def add_window(self, window: Window) -> None: ...
    def list_windows(self) -> list[Window]: ...
    @classmethod
    def new(cls) -> WindowGroup: ...
    def remove_window(self, window: Window) -> None: ...

class WindowGroupClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...
    _gtk_reserved1: None = ...
    _gtk_reserved2: None = ...
    _gtk_reserved3: None = ...
    _gtk_reserved4: None = ...

class WindowGroupPrivate(GObject.GPointer): ...

class WindowHandle(Widget, Accessible, Buildable, ConstraintTarget):
    class Props:
        child: Widget
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Gdk.Cursor
        focus_on_click: bool
        focusable: bool
        halign: Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: LayoutManager
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Overflow
        parent: Widget
        receives_default: bool
        root: Root
        scale_factor: int
        sensitive: bool
        tooltip_markup: str
        tooltip_text: str
        valign: Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Widget]: ...
    @classmethod
    def new(cls) -> WindowHandle: ...
    def set_child(self, child: Optional[Widget] = None) -> None: ...

class WindowHandleClass(GObject.GPointer):
    parent_class: WidgetClass = ...

class ApplicationInhibitFlags(GObject.GFlags):
    IDLE = 8
    LOGOUT = 1
    SUSPEND = 4
    SWITCH = 2

class BuilderClosureFlags(GObject.GFlags):
    SWAPPED = 1

class CellRendererState(GObject.GFlags):
    EXPANDABLE = 32
    EXPANDED = 64
    FOCUSED = 16
    INSENSITIVE = 4
    PRELIT = 2
    SELECTED = 1
    SORTED = 8

class DebugFlags(GObject.GFlags):
    A11Y = 131072
    ACTIONS = 4096
    BUILDER = 128
    BUILDER_OBJECTS = 65536
    CONSTRAINTS = 32768
    GEOMETRY = 16
    ICONFALLBACK = 262144
    ICONTHEME = 32
    INTERACTIVE = 1024
    INVERT_TEXT_DIR = 524288
    KEYBINDINGS = 4
    LAYOUT = 8192
    MODULES = 8
    NO_CSS_CACHE = 512
    PRINTING = 64
    SIZE_REQUEST = 256
    SNAPSHOT = 16384
    TEXT = 1
    TOUCHSCREEN = 2048
    TREE = 2

class DialogFlags(GObject.GFlags):
    DESTROY_WITH_PARENT = 2
    MODAL = 1
    USE_HEADER_BAR = 4

class EventControllerScrollFlags(GObject.GFlags):
    BOTH_AXES = 3
    DISCRETE = 4
    HORIZONTAL = 2
    KINETIC = 8
    NONE = 0
    VERTICAL = 1

class FontChooserLevel(GObject.GFlags):
    FAMILY = 0
    FEATURES = 8
    SIZE = 2
    STYLE = 1
    VARIATIONS = 4

class IconLookupFlags(GObject.GFlags):
    FORCE_REGULAR = 1
    FORCE_SYMBOLIC = 2
    PRELOAD = 4

class InputHints(GObject.GFlags):
    EMOJI = 512
    INHIBIT_OSK = 128
    LOWERCASE = 8
    NONE = 0
    NO_EMOJI = 1024
    NO_SPELLCHECK = 2
    PRIVATE = 2048
    SPELLCHECK = 1
    UPPERCASE_CHARS = 16
    UPPERCASE_SENTENCES = 64
    UPPERCASE_WORDS = 32
    VERTICAL_WRITING = 256
    WORD_COMPLETION = 4

class PickFlags(GObject.GFlags):
    DEFAULT = 0
    INSENSITIVE = 1
    NON_TARGETABLE = 2

class PopoverMenuFlags(GObject.GFlags):
    NESTED = 1

class PrintCapabilities(GObject.GFlags):
    COLLATE = 4
    COPIES = 2
    GENERATE_PDF = 32
    GENERATE_PS = 64
    NUMBER_UP = 256
    NUMBER_UP_LAYOUT = 512
    PAGE_SET = 1
    PREVIEW = 128
    REVERSE = 8
    SCALE = 16

class ShortcutActionFlags(GObject.GFlags):
    EXCLUSIVE = 1

class StateFlags(GObject.GFlags):
    ACTIVE = 1
    BACKDROP = 64
    CHECKED = 2048
    DIR_LTR = 128
    DIR_RTL = 256
    DROP_ACTIVE = 4096
    FOCUSED = 32
    FOCUS_VISIBLE = 8192
    FOCUS_WITHIN = 16384
    INCONSISTENT = 16
    INSENSITIVE = 8
    LINK = 512
    NORMAL = 0
    PRELIGHT = 2
    SELECTED = 4
    VISITED = 1024

class StyleContextPrintFlags(GObject.GFlags):
    NONE = 0
    RECURSE = 1
    SHOW_CHANGE = 4
    SHOW_STYLE = 2

class TextSearchFlags(GObject.GFlags):
    CASE_INSENSITIVE = 4
    TEXT_ONLY = 2
    VISIBLE_ONLY = 1

class TreeModelFlags(GObject.GFlags):
    ITERS_PERSIST = 1
    LIST_ONLY = 2

class AccessibleAutocomplete(GObject.GEnum):
    BOTH = 3
    INLINE = 1
    LIST = 2
    NONE = 0

class AccessibleInvalidState(GObject.GEnum):
    FALSE = 0
    GRAMMAR = 2
    SPELLING = 3
    TRUE = 1

class AccessibleProperty(GObject.GEnum):
    AUTOCOMPLETE = 0
    DESCRIPTION = 1
    HAS_POPUP = 2
    KEY_SHORTCUTS = 3
    LABEL = 4
    LEVEL = 5
    MODAL = 6
    MULTI_LINE = 7
    MULTI_SELECTABLE = 8
    ORIENTATION = 9
    PLACEHOLDER = 10
    READ_ONLY = 11
    REQUIRED = 12
    ROLE_DESCRIPTION = 13
    SORT = 14
    VALUE_MAX = 15
    VALUE_MIN = 16
    VALUE_NOW = 17
    VALUE_TEXT = 18
    @staticmethod
    def init_value(property: AccessibleProperty, value: Any) -> None: ...

class AccessibleRelation(GObject.GEnum):
    ACTIVE_DESCENDANT = 0
    COL_COUNT = 1
    COL_INDEX = 2
    COL_INDEX_TEXT = 3
    COL_SPAN = 4
    CONTROLS = 5
    DESCRIBED_BY = 6
    DETAILS = 7
    ERROR_MESSAGE = 8
    FLOW_TO = 9
    LABELLED_BY = 10
    OWNS = 11
    POS_IN_SET = 12
    ROW_COUNT = 13
    ROW_INDEX = 14
    ROW_INDEX_TEXT = 15
    ROW_SPAN = 16
    SET_SIZE = 17
    @staticmethod
    def init_value(relation: AccessibleRelation, value: Any) -> None: ...

class AccessibleRole(GObject.GEnum):
    ALERT = 0
    ALERT_DIALOG = 1
    BANNER = 2
    BUTTON = 3
    CAPTION = 4
    CELL = 5
    CHECKBOX = 6
    COLUMN_HEADER = 7
    COMBO_BOX = 8
    COMMAND = 9
    COMPOSITE = 10
    DIALOG = 11
    DOCUMENT = 12
    FEED = 13
    FORM = 14
    GENERIC = 15
    GRID = 16
    GRID_CELL = 17
    GROUP = 18
    HEADING = 19
    IMG = 20
    INPUT = 21
    LABEL = 22
    LANDMARK = 23
    LEGEND = 24
    LINK = 25
    LIST = 26
    LIST_BOX = 27
    LIST_ITEM = 28
    LOG = 29
    MAIN = 30
    MARQUEE = 31
    MATH = 32
    MENU = 34
    MENU_BAR = 35
    MENU_ITEM = 36
    MENU_ITEM_CHECKBOX = 37
    MENU_ITEM_RADIO = 38
    METER = 33
    NAVIGATION = 39
    NONE = 40
    NOTE = 41
    OPTION = 42
    PRESENTATION = 43
    PROGRESS_BAR = 44
    RADIO = 45
    RADIO_GROUP = 46
    RANGE = 47
    REGION = 48
    ROW = 49
    ROW_GROUP = 50
    ROW_HEADER = 51
    SCROLLBAR = 52
    SEARCH = 53
    SEARCH_BOX = 54
    SECTION = 55
    SECTION_HEAD = 56
    SELECT = 57
    SEPARATOR = 58
    SLIDER = 59
    SPIN_BUTTON = 60
    STATUS = 61
    STRUCTURE = 62
    SWITCH = 63
    TAB = 64
    TABLE = 65
    TAB_LIST = 66
    TAB_PANEL = 67
    TEXT_BOX = 68
    TIME = 69
    TIMER = 70
    TOOLBAR = 71
    TOOLTIP = 72
    TREE = 73
    TREE_GRID = 74
    TREE_ITEM = 75
    WIDGET = 76
    WINDOW = 77

class AccessibleSort(GObject.GEnum):
    ASCENDING = 1
    DESCENDING = 2
    NONE = 0
    OTHER = 3

class AccessibleState(GObject.GEnum):
    BUSY = 0
    CHECKED = 1
    DISABLED = 2
    EXPANDED = 3
    HIDDEN = 4
    INVALID = 5
    PRESSED = 6
    SELECTED = 7
    @staticmethod
    def init_value(state: AccessibleState, value: Any) -> None: ...

class AccessibleTristate(GObject.GEnum):
    FALSE = 0
    MIXED = 2
    TRUE = 1

class Align(GObject.GEnum):
    BASELINE = 4
    CENTER = 3
    END = 2
    FILL = 0
    START = 1

class ArrowType(GObject.GEnum):
    DOWN = 1
    LEFT = 2
    NONE = 4
    RIGHT = 3
    UP = 0

class AssistantPageType(GObject.GEnum):
    CONFIRM = 2
    CONTENT = 0
    CUSTOM = 5
    INTRO = 1
    PROGRESS = 4
    SUMMARY = 3

class BaselinePosition(GObject.GEnum):
    BOTTOM = 2
    CENTER = 1
    TOP = 0

class BorderStyle(GObject.GEnum):
    DASHED = 6
    DOTTED = 5
    DOUBLE = 7
    GROOVE = 8
    HIDDEN = 1
    INSET = 3
    NONE = 0
    OUTSET = 4
    RIDGE = 9
    SOLID = 2

class BuilderError(GObject.GEnum):
    DUPLICATE_ID = 8
    INVALID_ATTRIBUTE = 3
    INVALID_FUNCTION = 14
    INVALID_ID = 13
    INVALID_PROPERTY = 11
    INVALID_SIGNAL = 12
    INVALID_TAG = 4
    INVALID_TYPE_FUNCTION = 0
    INVALID_VALUE = 6
    MISSING_ATTRIBUTE = 2
    MISSING_PROPERTY_VALUE = 5
    OBJECT_TYPE_REFUSED = 9
    TEMPLATE_MISMATCH = 10
    UNHANDLED_TAG = 1
    VERSION_MISMATCH = 7
    @staticmethod
    def quark() -> int: ...

class ButtonsType(GObject.GEnum):
    CANCEL = 3
    CLOSE = 2
    NONE = 0
    OK = 1
    OK_CANCEL = 5
    YES_NO = 4

class CellRendererAccelMode(GObject.GEnum):
    GTK = 0
    OTHER = 1

class CellRendererMode(GObject.GEnum):
    ACTIVATABLE = 1
    EDITABLE = 2
    INERT = 0

class ConstraintAttribute(GObject.GEnum):
    BASELINE = 11
    BOTTOM = 4
    CENTER_X = 9
    CENTER_Y = 10
    END = 6
    HEIGHT = 8
    LEFT = 1
    NONE = 0
    RIGHT = 2
    START = 5
    TOP = 3
    WIDTH = 7

class ConstraintRelation(GObject.GEnum):
    EQ = 0
    GE = 1
    LE = -1

class ConstraintStrength(GObject.GEnum):
    MEDIUM = 1000
    REQUIRED = 1001001000
    STRONG = 1000000000
    WEAK = 1

class ConstraintVflParserError(GObject.GEnum):
    ATTRIBUTE = 1
    METRIC = 3
    PRIORITY = 4
    RELATION = 5
    SYMBOL = 0
    VIEW = 2
    @staticmethod
    def quark() -> int: ...

class ContentFit(GObject.GEnum):
    CONTAIN = 1
    COVER = 2
    FILL = 0
    SCALE_DOWN = 3

class CornerType(GObject.GEnum):
    BOTTOM_LEFT = 1
    BOTTOM_RIGHT = 3
    TOP_LEFT = 0
    TOP_RIGHT = 2

class CssParserError(GObject.GEnum):
    FAILED = 0
    IMPORT = 2
    NAME = 3
    SYNTAX = 1
    UNKNOWN_VALUE = 4

class CssParserWarning(GObject.GEnum):
    DEPRECATED = 0
    SYNTAX = 1
    UNIMPLEMENTED = 2

class DeleteType(GObject.GEnum):
    CHARS = 0
    DISPLAY_LINES = 3
    DISPLAY_LINE_ENDS = 4
    PARAGRAPHS = 6
    PARAGRAPH_ENDS = 5
    WHITESPACE = 7
    WORDS = 2
    WORD_ENDS = 1

class DirectionType(GObject.GEnum):
    DOWN = 3
    LEFT = 4
    RIGHT = 5
    TAB_BACKWARD = 1
    TAB_FORWARD = 0
    UP = 2

class EditableProperties(GObject.GEnum):
    NUM_PROPERTIES = 8
    PROP_CURSOR_POSITION = 1
    PROP_EDITABLE = 3
    PROP_ENABLE_UNDO = 7
    PROP_MAX_WIDTH_CHARS = 5
    PROP_SELECTION_BOUND = 2
    PROP_TEXT = 0
    PROP_WIDTH_CHARS = 4
    PROP_XALIGN = 6

class EntryIconPosition(GObject.GEnum):
    PRIMARY = 0
    SECONDARY = 1

class EventSequenceState(GObject.GEnum):
    CLAIMED = 1
    DENIED = 2
    NONE = 0

class FileChooserAction(GObject.GEnum):
    OPEN = 0
    SAVE = 1
    SELECT_FOLDER = 2

class FileChooserError(GObject.GEnum):
    ALREADY_EXISTS = 2
    BAD_FILENAME = 1
    INCOMPLETE_HOSTNAME = 3
    NONEXISTENT = 0
    @staticmethod
    def quark() -> int: ...

class FilterChange(GObject.GEnum):
    DIFFERENT = 0
    LESS_STRICT = 1
    MORE_STRICT = 2

class FilterMatch(GObject.GEnum):
    ALL = 2
    NONE = 1
    SOME = 0

class IconSize(GObject.GEnum):
    INHERIT = 0
    LARGE = 2
    NORMAL = 1

class IconThemeError(GObject.GEnum):
    FAILED = 1
    NOT_FOUND = 0
    @staticmethod
    def quark() -> int: ...

class IconViewDropPosition(GObject.GEnum):
    DROP_ABOVE = 4
    DROP_BELOW = 5
    DROP_INTO = 1
    DROP_LEFT = 2
    DROP_RIGHT = 3
    NO_DROP = 0

class ImageType(GObject.GEnum):
    EMPTY = 0
    GICON = 2
    ICON_NAME = 1
    PAINTABLE = 3

class InputPurpose(GObject.GEnum):
    ALPHA = 1
    DIGITS = 2
    EMAIL = 6
    FREE_FORM = 0
    NAME = 7
    NUMBER = 3
    PASSWORD = 8
    PHONE = 4
    PIN = 9
    TERMINAL = 10
    URL = 5

class InscriptionOverflow(GObject.GEnum):
    CLIP = 0
    ELLIPSIZE_END = 3
    ELLIPSIZE_MIDDLE = 2
    ELLIPSIZE_START = 1

class Justification(GObject.GEnum):
    CENTER = 2
    FILL = 3
    LEFT = 0
    RIGHT = 1

class LevelBarMode(GObject.GEnum):
    CONTINUOUS = 0
    DISCRETE = 1

class License(GObject.GEnum):
    AGPL_3_0 = 13
    AGPL_3_0_ONLY = 14
    APACHE_2_0 = 16
    ARTISTIC = 8
    BSD = 6
    BSD_3 = 15
    CUSTOM = 1
    GPL_2_0 = 2
    GPL_2_0_ONLY = 9
    GPL_3_0 = 3
    GPL_3_0_ONLY = 10
    LGPL_2_1 = 4
    LGPL_2_1_ONLY = 11
    LGPL_3_0 = 5
    LGPL_3_0_ONLY = 12
    MIT_X11 = 7
    MPL_2_0 = 17
    UNKNOWN = 0

class MessageType(GObject.GEnum):
    ERROR = 3
    INFO = 0
    OTHER = 4
    QUESTION = 2
    WARNING = 1

class MovementStep(GObject.GEnum):
    BUFFER_ENDS = 8
    DISPLAY_LINES = 3
    DISPLAY_LINE_ENDS = 4
    HORIZONTAL_PAGES = 9
    LOGICAL_POSITIONS = 0
    PAGES = 7
    PARAGRAPHS = 5
    PARAGRAPH_ENDS = 6
    VISUAL_POSITIONS = 1
    WORDS = 2

class NaturalWrapMode(GObject.GEnum):
    INHERIT = 0
    NONE = 1
    WORD = 2

class NotebookTab(GObject.GEnum):
    FIRST = 0
    LAST = 1

class NumberUpLayout(GObject.GEnum):
    BTLR = 6
    BTRL = 7
    LRBT = 1
    LRTB = 0
    RLBT = 3
    RLTB = 2
    TBLR = 4
    TBRL = 5

class Ordering(GObject.GEnum):
    EQUAL = 0
    LARGER = 1
    SMALLER = -1
    @staticmethod
    def from_cmpfunc(cmpfunc_result: int) -> Ordering: ...

class Orientation(GObject.GEnum):
    HORIZONTAL = 0
    VERTICAL = 1

class Overflow(GObject.GEnum):
    HIDDEN = 1
    VISIBLE = 0

class PackType(GObject.GEnum):
    END = 1
    START = 0

class PadActionType(GObject.GEnum):
    BUTTON = 0
    RING = 1
    STRIP = 2

class PageOrientation(GObject.GEnum):
    LANDSCAPE = 1
    PORTRAIT = 0
    REVERSE_LANDSCAPE = 3
    REVERSE_PORTRAIT = 2

class PageSet(GObject.GEnum):
    ALL = 0
    EVEN = 1
    ODD = 2

class PanDirection(GObject.GEnum):
    DOWN = 3
    LEFT = 0
    RIGHT = 1
    UP = 2

class PolicyType(GObject.GEnum):
    ALWAYS = 0
    AUTOMATIC = 1
    EXTERNAL = 3
    NEVER = 2

class PositionType(GObject.GEnum):
    BOTTOM = 3
    LEFT = 0
    RIGHT = 1
    TOP = 2

class PrintDuplex(GObject.GEnum):
    HORIZONTAL = 1
    SIMPLEX = 0
    VERTICAL = 2

class PrintError(GObject.GEnum):
    GENERAL = 0
    INTERNAL_ERROR = 1
    INVALID_FILE = 3
    NOMEM = 2
    @staticmethod
    def quark() -> int: ...

class PrintOperationAction(GObject.GEnum):
    EXPORT = 3
    PREVIEW = 2
    PRINT = 1
    PRINT_DIALOG = 0

class PrintOperationResult(GObject.GEnum):
    APPLY = 1
    CANCEL = 2
    ERROR = 0
    IN_PROGRESS = 3

class PrintPages(GObject.GEnum):
    ALL = 0
    CURRENT = 1
    RANGES = 2
    SELECTION = 3

class PrintQuality(GObject.GEnum):
    DRAFT = 3
    HIGH = 2
    LOW = 0
    NORMAL = 1

class PrintStatus(GObject.GEnum):
    FINISHED = 7
    FINISHED_ABORTED = 8
    GENERATING_DATA = 2
    INITIAL = 0
    PENDING = 4
    PENDING_ISSUE = 5
    PREPARING = 1
    PRINTING = 6
    SENDING_DATA = 3

class PropagationLimit(GObject.GEnum):
    NONE = 0
    SAME_NATIVE = 1

class PropagationPhase(GObject.GEnum):
    BUBBLE = 2
    CAPTURE = 1
    NONE = 0
    TARGET = 3

class RecentManagerError(GObject.GEnum):
    INVALID_ENCODING = 2
    INVALID_URI = 1
    NOT_FOUND = 0
    NOT_REGISTERED = 3
    READ = 4
    UNKNOWN = 6
    WRITE = 5
    @staticmethod
    def quark() -> int: ...

class ResponseType(GObject.GEnum):
    ACCEPT = -3
    APPLY = -10
    CANCEL = -6
    CLOSE = -7
    DELETE_EVENT = -4
    HELP = -11
    NO = -9
    NONE = -1
    OK = -5
    REJECT = -2
    YES = -8

class RevealerTransitionType(GObject.GEnum):
    CROSSFADE = 1
    NONE = 0
    SLIDE_DOWN = 5
    SLIDE_LEFT = 3
    SLIDE_RIGHT = 2
    SLIDE_UP = 4
    SWING_DOWN = 9
    SWING_LEFT = 7
    SWING_RIGHT = 6
    SWING_UP = 8

class ScrollStep(GObject.GEnum):
    ENDS = 2
    HORIZONTAL_ENDS = 5
    HORIZONTAL_PAGES = 4
    HORIZONTAL_STEPS = 3
    PAGES = 1
    STEPS = 0

class ScrollType(GObject.GEnum):
    END = 15
    JUMP = 1
    NONE = 0
    PAGE_BACKWARD = 4
    PAGE_DOWN = 9
    PAGE_FORWARD = 5
    PAGE_LEFT = 12
    PAGE_RIGHT = 13
    PAGE_UP = 8
    START = 14
    STEP_BACKWARD = 2
    STEP_DOWN = 7
    STEP_FORWARD = 3
    STEP_LEFT = 10
    STEP_RIGHT = 11
    STEP_UP = 6

class ScrollablePolicy(GObject.GEnum):
    MINIMUM = 0
    NATURAL = 1

class SelectionMode(GObject.GEnum):
    BROWSE = 2
    MULTIPLE = 3
    NONE = 0
    SINGLE = 1

class SensitivityType(GObject.GEnum):
    AUTO = 0
    OFF = 2
    ON = 1

class ShortcutScope(GObject.GEnum):
    GLOBAL = 2
    LOCAL = 0
    MANAGED = 1

class ShortcutType(GObject.GEnum):
    ACCELERATOR = 0
    GESTURE = 7
    GESTURE_PINCH = 1
    GESTURE_ROTATE_CLOCKWISE = 3
    GESTURE_ROTATE_COUNTERCLOCKWISE = 4
    GESTURE_STRETCH = 2
    GESTURE_SWIPE_LEFT = 8
    GESTURE_SWIPE_RIGHT = 9
    GESTURE_TWO_FINGER_SWIPE_LEFT = 5
    GESTURE_TWO_FINGER_SWIPE_RIGHT = 6

class SizeGroupMode(GObject.GEnum):
    BOTH = 3
    HORIZONTAL = 1
    NONE = 0
    VERTICAL = 2

class SizeRequestMode(GObject.GEnum):
    CONSTANT_SIZE = 2
    HEIGHT_FOR_WIDTH = 0
    WIDTH_FOR_HEIGHT = 1

class SortType(GObject.GEnum):
    ASCENDING = 0
    DESCENDING = 1

class SorterChange(GObject.GEnum):
    DIFFERENT = 0
    INVERTED = 1
    LESS_STRICT = 2
    MORE_STRICT = 3

class SorterOrder(GObject.GEnum):
    NONE = 1
    PARTIAL = 0
    TOTAL = 2

class SpinButtonUpdatePolicy(GObject.GEnum):
    ALWAYS = 0
    IF_VALID = 1

class SpinType(GObject.GEnum):
    END = 5
    HOME = 4
    PAGE_BACKWARD = 3
    PAGE_FORWARD = 2
    STEP_BACKWARD = 1
    STEP_FORWARD = 0
    USER_DEFINED = 6

class StackTransitionType(GObject.GEnum):
    CROSSFADE = 1
    NONE = 0
    OVER_DOWN = 9
    OVER_DOWN_UP = 17
    OVER_LEFT = 10
    OVER_LEFT_RIGHT = 18
    OVER_RIGHT = 11
    OVER_RIGHT_LEFT = 19
    OVER_UP = 8
    OVER_UP_DOWN = 16
    ROTATE_LEFT = 20
    ROTATE_LEFT_RIGHT = 22
    ROTATE_RIGHT = 21
    SLIDE_DOWN = 5
    SLIDE_LEFT = 3
    SLIDE_LEFT_RIGHT = 6
    SLIDE_RIGHT = 2
    SLIDE_UP = 4
    SLIDE_UP_DOWN = 7
    UNDER_DOWN = 13
    UNDER_LEFT = 14
    UNDER_RIGHT = 15
    UNDER_UP = 12

class StringFilterMatchMode(GObject.GEnum):
    EXACT = 0
    PREFIX = 2
    SUBSTRING = 1

class SymbolicColor(GObject.GEnum):
    ERROR = 1
    FOREGROUND = 0
    SUCCESS = 3
    WARNING = 2

class SystemSetting(GObject.GEnum):
    DISPLAY = 3
    DPI = 0
    FONT_CONFIG = 2
    FONT_NAME = 1
    ICON_THEME = 4

class TextDirection(GObject.GEnum):
    LTR = 1
    NONE = 0
    RTL = 2

class TextExtendSelection(GObject.GEnum):
    LINE = 1
    WORD = 0

class TextViewLayer(GObject.GEnum):
    ABOVE_TEXT = 1
    BELOW_TEXT = 0

class TextWindowType(GObject.GEnum):
    BOTTOM = 6
    LEFT = 3
    RIGHT = 4
    TEXT = 2
    TOP = 5
    WIDGET = 1

class TreeViewColumnSizing(GObject.GEnum):
    AUTOSIZE = 1
    FIXED = 2
    GROW_ONLY = 0

class TreeViewDropPosition(GObject.GEnum):
    AFTER = 1
    BEFORE = 0
    INTO_OR_AFTER = 3
    INTO_OR_BEFORE = 2

class TreeViewGridLines(GObject.GEnum):
    BOTH = 3
    HORIZONTAL = 1
    NONE = 0
    VERTICAL = 2

class Unit(GObject.GEnum):
    INCH = 2
    MM = 3
    NONE = 0
    POINTS = 1

class WrapMode(GObject.GEnum):
    CHAR = 1
    NONE = 0
    WORD = 2
    WORD_CHAR = 3
