from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

DURATION_INFINITE: int = 4294967295
MAJOR_VERSION: int = 1
MICRO_VERSION: int = 3
MINOR_VERSION: int = 2
VERSION_S: str = "1.2.3"
_lock = ...  # FIXME Constant
_namespace: str = "Adw"
_version: str = "1"

def easing_ease(self: Easing, value: float) -> float: ...
def get_enable_animations(widget: Gtk.Widget) -> bool: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def init() -> None: ...
def is_initialized() -> bool: ...
def lerp(a: float, b: float, t: float) -> float: ...

class AboutWindow(
    Window,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    class Props:
        application_icon: str
        application_name: str
        artists: Optional[list[str]]
        comments: str
        copyright: str
        debug_info: str
        debug_info_filename: str
        designers: Optional[list[str]]
        developer_name: str
        developers: Optional[list[str]]
        documenters: Optional[list[str]]
        issue_url: str
        license: str
        license_type: Gtk.License
        release_notes: str
        release_notes_version: str
        support_url: str
        translator_credits: str
        version: str
        website: str
        content: Optional[Gtk.Widget]
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    def __init__(
        self,
        application_icon: str = ...,
        application_name: str = ...,
        artists: Sequence[str] = ...,
        comments: str = ...,
        copyright: str = ...,
        debug_info: str = ...,
        debug_info_filename: str = ...,
        designers: Sequence[str] = ...,
        developer_name: str = ...,
        developers: Sequence[str] = ...,
        documenters: Sequence[str] = ...,
        issue_url: str = ...,
        license: str = ...,
        license_type: Gtk.License = ...,
        release_notes: str = ...,
        release_notes_version: str = ...,
        support_url: str = ...,
        translator_credits: str = ...,
        version: str = ...,
        website: str = ...,
        content: Gtk.Widget = ...,
        application: Gtk.Application = ...,
        child: Gtk.Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Gtk.Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
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
        titlebar: Gtk.Widget = ...,
        transient_for: Gtk.Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_acknowledgement_section(
        self, name: Optional[str], people: Sequence[str]
    ) -> None: ...
    def add_credit_section(
        self, name: Optional[str], people: Sequence[str]
    ) -> None: ...
    def add_legal_section(
        self,
        title: str,
        copyright: Optional[str],
        license_type: Gtk.License,
        license: Optional[str] = None,
    ) -> None: ...
    def add_link(self, title: str, url: str) -> None: ...
    def get_application_icon(self) -> str: ...
    def get_application_name(self) -> str: ...
    def get_artists(self) -> Optional[list[str]]: ...
    def get_comments(self) -> str: ...
    def get_copyright(self) -> str: ...
    def get_debug_info(self) -> str: ...
    def get_debug_info_filename(self) -> str: ...
    def get_designers(self) -> Optional[list[str]]: ...
    def get_developer_name(self) -> str: ...
    def get_developers(self) -> Optional[list[str]]: ...
    def get_documenters(self) -> Optional[list[str]]: ...
    def get_issue_url(self) -> str: ...
    def get_license(self) -> str: ...
    def get_license_type(self) -> Gtk.License: ...
    def get_release_notes(self) -> str: ...
    def get_release_notes_version(self) -> str: ...
    def get_support_url(self) -> str: ...
    def get_translator_credits(self) -> str: ...
    def get_version(self) -> str: ...
    def get_website(self) -> str: ...
    @classmethod
    def new(cls) -> AboutWindow: ...
    def set_application_icon(self, application_icon: str) -> None: ...
    def set_application_name(self, application_name: str) -> None: ...
    def set_artists(self, artists: Optional[Sequence[str]] = None) -> None: ...
    def set_comments(self, comments: str) -> None: ...
    def set_copyright(self, copyright: str) -> None: ...
    def set_debug_info(self, debug_info: str) -> None: ...
    def set_debug_info_filename(self, filename: str) -> None: ...
    def set_designers(self, designers: Optional[Sequence[str]] = None) -> None: ...
    def set_developer_name(self, developer_name: str) -> None: ...
    def set_developers(self, developers: Optional[Sequence[str]] = None) -> None: ...
    def set_documenters(self, documenters: Optional[Sequence[str]] = None) -> None: ...
    def set_issue_url(self, issue_url: str) -> None: ...
    def set_license(self, license: str) -> None: ...
    def set_license_type(self, license_type: Gtk.License) -> None: ...
    def set_release_notes(self, release_notes: str) -> None: ...
    def set_release_notes_version(self, version: str) -> None: ...
    def set_support_url(self, support_url: str) -> None: ...
    def set_translator_credits(self, translator_credits: str) -> None: ...
    def set_version(self, version: str) -> None: ...
    def set_website(self, website: str) -> None: ...

class AboutWindowClass(GObject.GPointer):
    parent_class: WindowClass = ...

class ActionRow(
    PreferencesRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        activatable_widget: Optional[Gtk.Widget]
        icon_name: Optional[str]
        subtitle: Optional[str]
        subtitle_lines: int
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        activatable_widget: Gtk.Widget = ...,
        icon_name: str = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: Gtk.Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def activate(self) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, widget: Gtk.Widget) -> None: ...
    def get_activatable_widget(self) -> Optional[Gtk.Widget]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_subtitle(self) -> Optional[str]: ...
    def get_subtitle_lines(self) -> int: ...
    def get_title_lines(self) -> int: ...
    @classmethod
    def new(cls) -> ActionRow: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_activatable_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_subtitle_lines(self, subtitle_lines: int) -> None: ...
    def set_title_lines(self, title_lines: int) -> None: ...

class ActionRowClass(GObject.GPointer):
    parent_class: PreferencesRowClass = ...
    activate: Callable[[ActionRow], None] = ...
    padding: list[None] = ...

class Animation(GObject.Object):
    class Props:
        state: AnimationState
        target: AnimationTarget
        value: float
        widget: Gtk.Widget
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, target: AnimationTarget = ..., widget: Gtk.Widget = ...): ...
    def get_state(self) -> AnimationState: ...
    def get_target(self) -> AnimationTarget: ...
    def get_value(self) -> float: ...
    def get_widget(self) -> Gtk.Widget: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    def reset(self) -> None: ...
    def resume(self) -> None: ...
    def set_target(self, target: AnimationTarget) -> None: ...
    def skip(self) -> None: ...

class AnimationClass(GObject.GPointer): ...
class AnimationTarget(GObject.Object): ...
class AnimationTargetClass(GObject.GPointer): ...

class Application(Gtk.Application, Gio.ActionGroup, Gio.ActionMap):
    class Props:
        style_manager: StyleManager
        active_window: Optional[Gtk.Window]
        menubar: Optional[Gio.MenuModel]
        register_session: bool
        screensaver_active: bool
        application_id: Optional[str]
        flags: Gio.ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: Optional[str]
        action_group: Optional[Gio.ActionGroup]
    props: Props = ...
    parent_instance: Gtk.Application = ...
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
    def get_style_manager(self) -> StyleManager: ...
    @classmethod
    def new(
        cls, application_id: Optional[str], flags: Gio.ApplicationFlags
    ) -> Application: ...

class ApplicationClass(GObject.GPointer):
    parent_class: Gtk.ApplicationClass = ...
    padding: list[None] = ...

class ApplicationWindow(
    Gtk.ApplicationWindow,
    Gio.ActionGroup,
    Gio.ActionMap,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    class Props:
        content: Optional[Gtk.Widget]
        show_menubar: bool
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    parent_instance: Gtk.ApplicationWindow = ...
    def __init__(
        self,
        content: Gtk.Widget = ...,
        show_menubar: bool = ...,
        application: Gtk.Application = ...,
        child: Gtk.Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Gtk.Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
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
        titlebar: Gtk.Widget = ...,
        transient_for: Gtk.Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_content(self) -> Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls, app: Gtk.Application) -> ApplicationWindow: ...
    def set_content(self, content: Optional[Gtk.Widget] = None) -> None: ...

class ApplicationWindowClass(GObject.GPointer):
    parent_class: Gtk.ApplicationWindowClass = ...
    padding: list[None] = ...

class Avatar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        custom_image: Optional[Gdk.Paintable]
        icon_name: Optional[str]
        show_initials: bool
        size: int
        text: Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        custom_image: Gdk.Paintable = ...,
        icon_name: str = ...,
        show_initials: bool = ...,
        size: int = ...,
        text: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def draw_to_texture(self, scale_factor: int) -> Gdk.Texture: ...
    def get_custom_image(self) -> Optional[Gdk.Paintable]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_show_initials(self) -> bool: ...
    def get_size(self) -> int: ...
    def get_text(self) -> Optional[str]: ...
    @classmethod
    def new(cls, size: int, text: Optional[str], show_initials: bool) -> Avatar: ...
    def set_custom_image(
        self, custom_image: Optional[Gdk.Paintable] = None
    ) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_show_initials(self, show_initials: bool) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_text(self, text: Optional[str] = None) -> None: ...

class AvatarClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class Bin(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        child: Optional[Gtk.Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> Bin: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...

class BinClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ButtonContent(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
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
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_icon_name(self) -> str: ...
    def get_label(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> ButtonContent: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class ButtonContentClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class CallbackAnimationTarget(AnimationTarget):
    @classmethod
    def new(
        cls, callback: Callable[..., None], *user_data: Any
    ) -> CallbackAnimationTarget: ...

class CallbackAnimationTargetClass(GObject.GPointer): ...

class Carousel(
    Gtk.Widget,
    Swipeable,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
):
    class Props:
        allow_long_swipes: bool
        allow_mouse_drag: bool
        allow_scroll_wheel: bool
        interactive: bool
        n_pages: int
        position: float
        reveal_duration: int
        scroll_params: SpringParams
        spacing: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        allow_long_swipes: bool = ...,
        allow_mouse_drag: bool = ...,
        allow_scroll_wheel: bool = ...,
        interactive: bool = ...,
        reveal_duration: int = ...,
        scroll_params: SpringParams = ...,
        spacing: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def append(self, child: Gtk.Widget) -> None: ...
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_allow_scroll_wheel(self) -> bool: ...
    def get_interactive(self) -> bool: ...
    def get_n_pages(self) -> int: ...
    def get_nth_page(self, n: int) -> Gtk.Widget: ...
    def get_position(self) -> float: ...
    def get_reveal_duration(self) -> int: ...
    def get_scroll_params(self) -> SpringParams: ...
    def get_spacing(self) -> int: ...
    def insert(self, child: Gtk.Widget, position: int) -> None: ...
    @classmethod
    def new(cls) -> Carousel: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def reorder(self, child: Gtk.Widget, position: int) -> None: ...
    def scroll_to(self, widget: Gtk.Widget, animate: bool) -> None: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_allow_scroll_wheel(self, allow_scroll_wheel: bool) -> None: ...
    def set_interactive(self, interactive: bool) -> None: ...
    def set_reveal_duration(self, reveal_duration: int) -> None: ...
    def set_scroll_params(self, params: SpringParams) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class CarouselClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class CarouselIndicatorDots(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    class Props:
        carousel: Optional[Carousel]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        carousel: Carousel = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_carousel(self) -> Optional[Carousel]: ...
    @classmethod
    def new(cls) -> CarouselIndicatorDots: ...
    def set_carousel(self, carousel: Optional[Carousel] = None) -> None: ...

class CarouselIndicatorDotsClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class CarouselIndicatorLines(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    class Props:
        carousel: Optional[Carousel]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        carousel: Carousel = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_carousel(self) -> Optional[Carousel]: ...
    @classmethod
    def new(cls) -> CarouselIndicatorLines: ...
    def set_carousel(self, carousel: Optional[Carousel] = None) -> None: ...

class CarouselIndicatorLinesClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class Clamp(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    class Props:
        child: Optional[Gtk.Widget]
        maximum_size: int
        tightening_threshold: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new(cls) -> Clamp: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ClampClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ClampLayout(Gtk.LayoutManager, Gtk.Orientable):
    class Props:
        maximum_size: int
        tightening_threshold: int
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new(cls) -> ClampLayout: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ClampLayoutClass(GObject.GPointer):
    parent_class: Gtk.LayoutManagerClass = ...

class ClampScrollable(
    Gtk.Widget,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
    Gtk.Scrollable,
):
    class Props:
        child: Optional[Gtk.Widget]
        maximum_size: int
        tightening_threshold: int
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
        hadjustment: Optional[Gtk.Adjustment]
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Optional[Gtk.Adjustment]
        vscroll_policy: Gtk.ScrollablePolicy
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
        hadjustment: Gtk.Adjustment = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Gtk.Adjustment = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new(cls) -> ClampScrollable: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ClampScrollableClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ComboRow(
    ActionRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        expression: Optional[Gtk.Expression]
        factory: Optional[Gtk.ListItemFactory]
        list_factory: Optional[Gtk.ListItemFactory]
        model: Optional[Gio.ListModel]
        selected: int
        selected_item: Optional[GObject.Object]
        use_subtitle: bool
        activatable_widget: Optional[Gtk.Widget]
        icon_name: Optional[str]
        subtitle: Optional[str]
        subtitle_lines: int
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
    props: Props = ...
    parent_instance: ActionRow = ...
    def __init__(
        self,
        expression: Gtk.Expression = ...,
        factory: Gtk.ListItemFactory = ...,
        list_factory: Gtk.ListItemFactory = ...,
        model: Gio.ListModel = ...,
        selected: int = ...,
        use_subtitle: bool = ...,
        activatable_widget: Gtk.Widget = ...,
        icon_name: str = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: Gtk.Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_expression(self) -> Optional[Gtk.Expression]: ...
    def get_factory(self) -> Optional[Gtk.ListItemFactory]: ...
    def get_list_factory(self) -> Optional[Gtk.ListItemFactory]: ...
    def get_model(self) -> Optional[Gio.ListModel]: ...
    def get_selected(self) -> int: ...
    def get_selected_item(self) -> Optional[GObject.Object]: ...
    def get_use_subtitle(self) -> bool: ...
    @classmethod
    def new(cls) -> ComboRow: ...
    def set_expression(self, expression: Optional[Gtk.Expression] = None) -> None: ...
    def set_factory(self, factory: Optional[Gtk.ListItemFactory] = None) -> None: ...
    def set_list_factory(
        self, factory: Optional[Gtk.ListItemFactory] = None
    ) -> None: ...
    def set_model(self, model: Optional[Gio.ListModel] = None) -> None: ...
    def set_selected(self, position: int) -> None: ...
    def set_use_subtitle(self, use_subtitle: bool) -> None: ...

class ComboRowClass(GObject.GPointer):
    parent_class: ActionRowClass = ...
    padding: list[None] = ...

class EntryRow(
    PreferencesRow,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Editable,
):
    class Props:
        activates_default: bool
        attributes: Optional[Pango.AttrList]
        enable_emoji_completion: bool
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        show_apply_button: bool
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
        cursor_position: int
        editable: bool
        enable_undo: bool
        max_width_chars: int
        selection_bound: int
        text: str
        width_chars: int
        xalign: float
    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        activates_default: bool = ...,
        attributes: Pango.AttrList = ...,
        enable_emoji_completion: bool = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        show_apply_button: bool = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: Gtk.Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, widget: Gtk.Widget) -> None: ...
    def get_activates_default(self) -> bool: ...
    def get_attributes(self) -> Optional[Pango.AttrList]: ...
    def get_enable_emoji_completion(self) -> bool: ...
    def get_input_hints(self) -> Gtk.InputHints: ...
    def get_input_purpose(self) -> Gtk.InputPurpose: ...
    def get_show_apply_button(self) -> bool: ...
    @classmethod
    def new(cls) -> EntryRow: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_activates_default(self, activates: bool) -> None: ...
    def set_attributes(self, attributes: Optional[Pango.AttrList] = None) -> None: ...
    def set_enable_emoji_completion(self, enable_emoji_completion: bool) -> None: ...
    def set_input_hints(self, hints: Gtk.InputHints) -> None: ...
    def set_input_purpose(self, purpose: Gtk.InputPurpose) -> None: ...
    def set_show_apply_button(self, show_apply_button: bool) -> None: ...

class EntryRowClass(GObject.GPointer):
    parent_class: PreferencesRowClass = ...

class EnumListItem(GObject.Object):
    class Props:
        name: str
        nick: str
        value: int
    props: Props = ...
    def get_name(self) -> str: ...
    def get_nick(self) -> str: ...
    def get_value(self) -> int: ...

class EnumListItemClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class EnumListModel(GObject.Object, Gio.ListModel):
    class Props:
        enum_type: Type
    props: Props = ...
    def __init__(self, enum_type: Type = ...): ...
    def find_position(self, value: int) -> int: ...
    def get_enum_type(self) -> Type: ...
    @classmethod
    def new(cls, enum_type: Type) -> EnumListModel: ...

class EnumListModelClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class ExpanderRow(
    PreferencesRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        enable_expansion: bool
        expanded: bool
        icon_name: Optional[str]
        show_enable_switch: bool
        subtitle: str
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        enable_expansion: bool = ...,
        expanded: bool = ...,
        icon_name: str = ...,
        show_enable_switch: bool = ...,
        subtitle: str = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: Gtk.Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def add_action(self, widget: Gtk.Widget) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_row(self, child: Gtk.Widget) -> None: ...
    def get_enable_expansion(self) -> bool: ...
    def get_expanded(self) -> bool: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_show_enable_switch(self) -> bool: ...
    def get_subtitle(self) -> str: ...
    @classmethod
    def new(cls) -> ExpanderRow: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_enable_expansion(self, enable_expansion: bool) -> None: ...
    def set_expanded(self, expanded: bool) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_show_enable_switch(self, show_enable_switch: bool) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...

class ExpanderRowClass(GObject.GPointer):
    parent_class: PreferencesRowClass = ...
    padding: list[None] = ...

class Flap(
    Gtk.Widget,
    Swipeable,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
):
    class Props:
        content: Optional[Gtk.Widget]
        flap: Optional[Gtk.Widget]
        flap_position: Gtk.PackType
        fold_duration: int
        fold_policy: FlapFoldPolicy
        fold_threshold_policy: FoldThresholdPolicy
        folded: bool
        locked: bool
        modal: bool
        reveal_flap: bool
        reveal_params: SpringParams
        reveal_progress: float
        separator: Optional[Gtk.Widget]
        swipe_to_close: bool
        swipe_to_open: bool
        transition_type: FlapTransitionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        content: Gtk.Widget = ...,
        flap: Gtk.Widget = ...,
        flap_position: Gtk.PackType = ...,
        fold_duration: int = ...,
        fold_policy: FlapFoldPolicy = ...,
        fold_threshold_policy: FoldThresholdPolicy = ...,
        locked: bool = ...,
        modal: bool = ...,
        reveal_flap: bool = ...,
        reveal_params: SpringParams = ...,
        separator: Gtk.Widget = ...,
        swipe_to_close: bool = ...,
        swipe_to_open: bool = ...,
        transition_type: FlapTransitionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_content(self) -> Optional[Gtk.Widget]: ...
    def get_flap(self) -> Optional[Gtk.Widget]: ...
    def get_flap_position(self) -> Gtk.PackType: ...
    def get_fold_duration(self) -> int: ...
    def get_fold_policy(self) -> FlapFoldPolicy: ...
    def get_fold_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_folded(self) -> bool: ...
    def get_locked(self) -> bool: ...
    def get_modal(self) -> bool: ...
    def get_reveal_flap(self) -> bool: ...
    def get_reveal_params(self) -> SpringParams: ...
    def get_reveal_progress(self) -> float: ...
    def get_separator(self) -> Optional[Gtk.Widget]: ...
    def get_swipe_to_close(self) -> bool: ...
    def get_swipe_to_open(self) -> bool: ...
    def get_transition_type(self) -> FlapTransitionType: ...
    @classmethod
    def new(cls) -> Flap: ...
    def set_content(self, content: Optional[Gtk.Widget] = None) -> None: ...
    def set_flap(self, flap: Optional[Gtk.Widget] = None) -> None: ...
    def set_flap_position(self, position: Gtk.PackType) -> None: ...
    def set_fold_duration(self, duration: int) -> None: ...
    def set_fold_policy(self, policy: FlapFoldPolicy) -> None: ...
    def set_fold_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_locked(self, locked: bool) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_reveal_flap(self, reveal_flap: bool) -> None: ...
    def set_reveal_params(self, params: SpringParams) -> None: ...
    def set_separator(self, separator: Optional[Gtk.Widget] = None) -> None: ...
    def set_swipe_to_close(self, swipe_to_close: bool) -> None: ...
    def set_swipe_to_open(self, swipe_to_open: bool) -> None: ...
    def set_transition_type(self, transition_type: FlapTransitionType) -> None: ...

class FlapClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class HeaderBar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        centering_policy: CenteringPolicy
        decoration_layout: Optional[str]
        show_end_title_buttons: bool
        show_start_title_buttons: bool
        title_widget: Optional[Gtk.Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        centering_policy: CenteringPolicy = ...,
        decoration_layout: str = ...,
        show_end_title_buttons: bool = ...,
        show_start_title_buttons: bool = ...,
        title_widget: Gtk.Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_centering_policy(self) -> CenteringPolicy: ...
    def get_decoration_layout(self) -> Optional[str]: ...
    def get_show_end_title_buttons(self) -> bool: ...
    def get_show_start_title_buttons(self) -> bool: ...
    def get_title_widget(self) -> Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> HeaderBar: ...
    def pack_end(self, child: Gtk.Widget) -> None: ...
    def pack_start(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_centering_policy(self, centering_policy: CenteringPolicy) -> None: ...
    def set_decoration_layout(self, layout: Optional[str] = None) -> None: ...
    def set_show_end_title_buttons(self, setting: bool) -> None: ...
    def set_show_start_title_buttons(self, setting: bool) -> None: ...
    def set_title_widget(self, title_widget: Optional[Gtk.Widget] = None) -> None: ...

class HeaderBarClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class Leaflet(
    Gtk.Widget,
    Swipeable,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
):
    class Props:
        can_navigate_back: bool
        can_navigate_forward: bool
        can_unfold: bool
        child_transition_params: SpringParams
        child_transition_running: bool
        fold_threshold_policy: FoldThresholdPolicy
        folded: bool
        homogeneous: bool
        mode_transition_duration: int
        pages: Gtk.SelectionModel
        transition_type: LeafletTransitionType
        visible_child: Optional[Gtk.Widget]
        visible_child_name: Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        can_navigate_back: bool = ...,
        can_navigate_forward: bool = ...,
        can_unfold: bool = ...,
        child_transition_params: SpringParams = ...,
        fold_threshold_policy: FoldThresholdPolicy = ...,
        homogeneous: bool = ...,
        mode_transition_duration: int = ...,
        transition_type: LeafletTransitionType = ...,
        visible_child: Gtk.Widget = ...,
        visible_child_name: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def append(self, child: Gtk.Widget) -> LeafletPage: ...
    def get_adjacent_child(
        self, direction: NavigationDirection
    ) -> Optional[Gtk.Widget]: ...
    def get_can_navigate_back(self) -> bool: ...
    def get_can_navigate_forward(self) -> bool: ...
    def get_can_unfold(self) -> bool: ...
    def get_child_by_name(self, name: str) -> Optional[Gtk.Widget]: ...
    def get_child_transition_params(self) -> SpringParams: ...
    def get_child_transition_running(self) -> bool: ...
    def get_fold_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_folded(self) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_mode_transition_duration(self) -> int: ...
    def get_page(self, child: Gtk.Widget) -> LeafletPage: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_transition_type(self) -> LeafletTransitionType: ...
    def get_visible_child(self) -> Optional[Gtk.Widget]: ...
    def get_visible_child_name(self) -> Optional[str]: ...
    def insert_child_after(
        self, child: Gtk.Widget, sibling: Optional[Gtk.Widget] = None
    ) -> LeafletPage: ...
    def navigate(self, direction: NavigationDirection) -> bool: ...
    @classmethod
    def new(cls) -> Leaflet: ...
    def prepend(self, child: Gtk.Widget) -> LeafletPage: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def reorder_child_after(
        self, child: Gtk.Widget, sibling: Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_can_navigate_back(self, can_navigate_back: bool) -> None: ...
    def set_can_navigate_forward(self, can_navigate_forward: bool) -> None: ...
    def set_can_unfold(self, can_unfold: bool) -> None: ...
    def set_child_transition_params(self, params: SpringParams) -> None: ...
    def set_fold_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_mode_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: LeafletTransitionType) -> None: ...
    def set_visible_child(self, visible_child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class LeafletClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class LeafletPage(GObject.Object):
    class Props:
        child: Gtk.Widget
        name: Optional[str]
        navigatable: bool
    props: Props = ...
    def __init__(
        self, child: Gtk.Widget = ..., name: str = ..., navigatable: bool = ...
    ): ...
    def get_child(self) -> Gtk.Widget: ...
    def get_name(self) -> Optional[str]: ...
    def get_navigatable(self) -> bool: ...
    def set_name(self, name: Optional[str] = None) -> None: ...
    def set_navigatable(self, navigatable: bool) -> None: ...

class LeafletPageClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class MessageDialog(
    Gtk.Window,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    class Props:
        body: str
        body_use_markup: bool
        close_response: str
        default_response: Optional[str]
        extra_child: Optional[Gtk.Widget]
        heading: Optional[str]
        heading_use_markup: bool
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    parent_instance: Gtk.Window = ...
    def __init__(
        self,
        body: str = ...,
        body_use_markup: bool = ...,
        close_response: str = ...,
        default_response: str = ...,
        extra_child: Gtk.Widget = ...,
        heading: str = ...,
        heading_use_markup: bool = ...,
        application: Gtk.Application = ...,
        child: Gtk.Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Gtk.Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
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
        titlebar: Gtk.Widget = ...,
        transient_for: Gtk.Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_response(self, id: str, label: str) -> None: ...
    def do_response(self, response: str) -> None: ...
    def get_body(self) -> str: ...
    def get_body_use_markup(self) -> bool: ...
    def get_close_response(self) -> str: ...
    def get_default_response(self) -> Optional[str]: ...
    def get_extra_child(self) -> Optional[Gtk.Widget]: ...
    def get_heading(self) -> Optional[str]: ...
    def get_heading_use_markup(self) -> bool: ...
    def get_response_appearance(self, response: str) -> ResponseAppearance: ...
    def get_response_enabled(self, response: str) -> bool: ...
    def get_response_label(self, response: str) -> str: ...
    def has_response(self, response: str) -> bool: ...
    @classmethod
    def new(
        cls,
        parent: Optional[Gtk.Window] = None,
        heading: Optional[str] = None,
        body: Optional[str] = None,
    ) -> MessageDialog: ...
    def response(self, response: str) -> None: ...
    def set_body(self, body: str) -> None: ...
    def set_body_use_markup(self, use_markup: bool) -> None: ...
    def set_close_response(self, response: str) -> None: ...
    def set_default_response(self, response: Optional[str] = None) -> None: ...
    def set_extra_child(self, child: Optional[Gtk.Widget] = None) -> None: ...
    def set_heading(self, heading: Optional[str] = None) -> None: ...
    def set_heading_use_markup(self, use_markup: bool) -> None: ...
    def set_response_appearance(
        self, response: str, appearance: ResponseAppearance
    ) -> None: ...
    def set_response_enabled(self, response: str, enabled: bool) -> None: ...
    def set_response_label(self, response: str, label: str) -> None: ...

class MessageDialogClass(GObject.GPointer):
    parent_class: Gtk.WindowClass = ...
    response: Callable[[MessageDialog, str], None] = ...
    padding: list[None] = ...

class PasswordEntryRow(
    EntryRow,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Editable,
):
    class Props:
        activates_default: bool
        attributes: Optional[Pango.AttrList]
        enable_emoji_completion: bool
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        show_apply_button: bool
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
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
        enable_emoji_completion: bool = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        show_apply_button: bool = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: Gtk.Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ): ...
    @classmethod
    def new(cls) -> PasswordEntryRow: ...

class PasswordEntryRowClass(GObject.GPointer):
    parent_class: EntryRowClass = ...

class PreferencesGroup(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        description: Optional[str]
        header_suffix: Optional[Gtk.Widget]
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        description: str = ...,
        header_suffix: Gtk.Widget = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add(self, child: Gtk.Widget) -> None: ...
    def get_description(self) -> Optional[str]: ...
    def get_header_suffix(self) -> Optional[Gtk.Widget]: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls) -> PreferencesGroup: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_description(self, description: Optional[str] = None) -> None: ...
    def set_header_suffix(self, suffix: Optional[Gtk.Widget] = None) -> None: ...
    def set_title(self, title: str) -> None: ...

class PreferencesGroupClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...
    padding: list[None] = ...

class PreferencesPage(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        icon_name: Optional[str]
        name: Optional[str]
        title: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    parent_instance: Gtk.Widget = ...
    def __init__(
        self,
        icon_name: str = ...,
        name: str = ...,
        title: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add(self, group: PreferencesGroup) -> None: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_name(self) -> Optional[str]: ...
    def get_title(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> PreferencesPage: ...
    def remove(self, group: PreferencesGroup) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_name(self, name: Optional[str] = None) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class PreferencesPageClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...
    padding: list[None] = ...

class PreferencesRow(
    Gtk.ListBoxRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
    props: Props = ...
    parent_instance: Gtk.ListBoxRow = ...
    def __init__(
        self,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: Gtk.Widget = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_title(self) -> str: ...
    def get_title_selectable(self) -> bool: ...
    def get_use_markup(self) -> bool: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> PreferencesRow: ...
    def set_title(self, title: str) -> None: ...
    def set_title_selectable(self, title_selectable: bool) -> None: ...
    def set_use_markup(self, use_markup: bool) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class PreferencesRowClass(GObject.GPointer):
    parent_class: Gtk.ListBoxRowClass = ...
    padding: list[None] = ...

class PreferencesWindow(
    Window,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    class Props:
        can_navigate_back: bool
        search_enabled: bool
        visible_page: Optional[Gtk.Widget]
        visible_page_name: Optional[str]
        content: Optional[Gtk.Widget]
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    parent_instance: Window = ...
    def __init__(
        self,
        can_navigate_back: bool = ...,
        search_enabled: bool = ...,
        visible_page: Gtk.Widget = ...,
        visible_page_name: str = ...,
        content: Gtk.Widget = ...,
        application: Gtk.Application = ...,
        child: Gtk.Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Gtk.Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
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
        titlebar: Gtk.Widget = ...,
        transient_for: Gtk.Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add(self, page: PreferencesPage) -> None: ...
    def add_toast(self, toast: Toast) -> None: ...
    def close_subpage(self) -> None: ...
    def get_can_navigate_back(self) -> bool: ...
    def get_search_enabled(self) -> bool: ...
    def get_visible_page(self) -> Optional[PreferencesPage]: ...
    def get_visible_page_name(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> PreferencesWindow: ...
    def present_subpage(self, subpage: Gtk.Widget) -> None: ...
    def remove(self, page: PreferencesPage) -> None: ...
    def set_can_navigate_back(self, can_navigate_back: bool) -> None: ...
    def set_search_enabled(self, search_enabled: bool) -> None: ...
    def set_visible_page(self, page: PreferencesPage) -> None: ...
    def set_visible_page_name(self, name: str) -> None: ...

class PreferencesWindowClass(GObject.GPointer):
    parent_class: WindowClass = ...
    padding: list[None] = ...

class PropertyAnimationTarget(AnimationTarget):
    class Props:
        object: GObject.Object
        pspec: GObject.ParamSpec
    props: Props = ...
    def __init__(
        self, object: GObject.Object = ..., pspec: GObject.ParamSpec = ...
    ): ...
    def get_object(self) -> GObject.Object: ...
    def get_pspec(self) -> GObject.ParamSpec: ...
    @classmethod
    def new(
        cls, object: GObject.Object, property_name: str
    ) -> PropertyAnimationTarget: ...
    @classmethod
    def new_for_pspec(
        cls, object: GObject.Object, pspec: GObject.ParamSpec
    ) -> PropertyAnimationTarget: ...

class PropertyAnimationTargetClass(GObject.GPointer): ...

class SplitButton(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        child: Optional[Gtk.Widget]
        direction: Gtk.ArrowType
        dropdown_tooltip: str
        icon_name: Optional[str]
        label: Optional[str]
        menu_model: Optional[Gio.MenuModel]
        popover: Optional[Gtk.Popover]
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: Optional[str]
        action_target: GLib.Variant
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        direction: Gtk.ArrowType = ...,
        dropdown_tooltip: str = ...,
        icon_name: str = ...,
        label: str = ...,
        menu_model: Gio.MenuModel = ...,
        popover: Gtk.Popover = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
    ): ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    def get_direction(self) -> Gtk.ArrowType: ...
    def get_dropdown_tooltip(self) -> str: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_label(self) -> Optional[str]: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    def get_popover(self) -> Optional[Gtk.Popover]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> SplitButton: ...
    def popdown(self) -> None: ...
    def popup(self) -> None: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...
    def set_direction(self, direction: Gtk.ArrowType) -> None: ...
    def set_dropdown_tooltip(self, tooltip: str) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_menu_model(self, menu_model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_popover(self, popover: Optional[Gtk.Popover] = None) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class SplitButtonClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class SpringAnimation(Animation):
    class Props:
        clamp: bool
        epsilon: float
        estimated_duration: int
        initial_velocity: float
        spring_params: SpringParams
        value_from: float
        value_to: float
        velocity: float
        state: AnimationState
        target: AnimationTarget
        value: float
        widget: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        clamp: bool = ...,
        epsilon: float = ...,
        initial_velocity: float = ...,
        spring_params: SpringParams = ...,
        value_from: float = ...,
        value_to: float = ...,
        target: AnimationTarget = ...,
        widget: Gtk.Widget = ...,
    ): ...
    def get_clamp(self) -> bool: ...
    def get_epsilon(self) -> float: ...
    def get_estimated_duration(self) -> int: ...
    def get_initial_velocity(self) -> float: ...
    def get_spring_params(self) -> SpringParams: ...
    def get_value_from(self) -> float: ...
    def get_value_to(self) -> float: ...
    def get_velocity(self) -> float: ...
    @classmethod
    def new(
        cls,
        widget: Gtk.Widget,
        from_: float,
        to: float,
        spring_params: SpringParams,
        target: AnimationTarget,
    ) -> SpringAnimation: ...
    def set_clamp(self, clamp: bool) -> None: ...
    def set_epsilon(self, epsilon: float) -> None: ...
    def set_initial_velocity(self, velocity: float) -> None: ...
    def set_spring_params(self, spring_params: SpringParams) -> None: ...
    def set_value_from(self, value: float) -> None: ...
    def set_value_to(self, value: float) -> None: ...

class SpringAnimationClass(GObject.GPointer): ...

class SpringParams(GObject.GBoxed):
    def get_damping(self) -> float: ...
    def get_damping_ratio(self) -> float: ...
    def get_mass(self) -> float: ...
    def get_stiffness(self) -> float: ...
    @classmethod
    def new(
        cls, damping_ratio: float, mass: float, stiffness: float
    ) -> SpringParams: ...
    @classmethod
    def new_full(
        cls, damping: float, mass: float, stiffness: float
    ) -> SpringParams: ...
    def ref(self) -> SpringParams: ...
    def unref(self) -> None: ...

class Squeezer(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    class Props:
        allow_none: bool
        homogeneous: bool
        interpolate_size: bool
        pages: Gtk.SelectionModel
        switch_threshold_policy: FoldThresholdPolicy
        transition_duration: int
        transition_running: bool
        transition_type: SqueezerTransitionType
        visible_child: Optional[Gtk.Widget]
        xalign: float
        yalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        allow_none: bool = ...,
        homogeneous: bool = ...,
        interpolate_size: bool = ...,
        switch_threshold_policy: FoldThresholdPolicy = ...,
        transition_duration: int = ...,
        transition_type: SqueezerTransitionType = ...,
        xalign: float = ...,
        yalign: float = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def add(self, child: Gtk.Widget) -> SqueezerPage: ...
    def get_allow_none(self) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_page(self, child: Gtk.Widget) -> SqueezerPage: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_switch_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    def get_transition_type(self) -> SqueezerTransitionType: ...
    def get_visible_child(self) -> Optional[Gtk.Widget]: ...
    def get_xalign(self) -> float: ...
    def get_yalign(self) -> float: ...
    @classmethod
    def new(cls) -> Squeezer: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_allow_none(self, allow_none: bool) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_switch_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: SqueezerTransitionType) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...

class SqueezerClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class SqueezerPage(GObject.Object):
    class Props:
        child: Gtk.Widget
        enabled: bool
    props: Props = ...
    def __init__(self, child: Gtk.Widget = ..., enabled: bool = ...): ...
    def get_child(self) -> Gtk.Widget: ...
    def get_enabled(self) -> bool: ...
    def set_enabled(self, enabled: bool) -> None: ...

class SqueezerPageClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class StatusPage(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        child: Optional[Gtk.Widget]
        description: Optional[str]
        icon_name: Optional[str]
        paintable: Optional[Gdk.Paintable]
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        description: str = ...,
        icon_name: str = ...,
        paintable: Gdk.Paintable = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    def get_description(self) -> Optional[str]: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_paintable(self) -> Optional[Gdk.Paintable]: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls) -> StatusPage: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...
    def set_description(self, description: Optional[str] = None) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_paintable(self, paintable: Optional[Gdk.Paintable] = None) -> None: ...
    def set_title(self, title: str) -> None: ...

class StatusPageClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class StyleManager(GObject.Object):
    class Props:
        color_scheme: ColorScheme
        dark: bool
        display: Gdk.Display
        high_contrast: bool
        system_supports_color_schemes: bool
    props: Props = ...
    def __init__(self, color_scheme: ColorScheme = ..., display: Gdk.Display = ...): ...
    def get_color_scheme(self) -> ColorScheme: ...
    def get_dark(self) -> bool: ...
    @staticmethod
    def get_default() -> StyleManager: ...
    def get_display(self) -> Gdk.Display: ...
    @staticmethod
    def get_for_display(display: Gdk.Display) -> StyleManager: ...
    def get_high_contrast(self) -> bool: ...
    def get_system_supports_color_schemes(self) -> bool: ...
    def set_color_scheme(self, color_scheme: ColorScheme) -> None: ...

class StyleManagerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class SwipeTracker(GObject.Object, Gtk.Orientable):
    class Props:
        allow_long_swipes: bool
        allow_mouse_drag: bool
        enabled: bool
        reversed: bool
        swipeable: Swipeable
        orientation: Gtk.Orientation
    props: Props = ...
    def __init__(
        self,
        allow_long_swipes: bool = ...,
        allow_mouse_drag: bool = ...,
        enabled: bool = ...,
        reversed: bool = ...,
        swipeable: Swipeable = ...,
        orientation: Gtk.Orientation = ...,
    ): ...
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_enabled(self) -> bool: ...
    def get_reversed(self) -> bool: ...
    def get_swipeable(self) -> Swipeable: ...
    @classmethod
    def new(cls, swipeable: Swipeable) -> SwipeTracker: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_reversed(self, reversed: bool) -> None: ...
    def shift_position(self, delta: float) -> None: ...

class SwipeTrackerClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class Swipeable(GObject.GInterface):
    def get_cancel_progress(self) -> float: ...
    def get_distance(self) -> float: ...
    def get_progress(self) -> float: ...
    def get_snap_points(self) -> list[float]: ...
    def get_swipe_area(
        self, navigation_direction: NavigationDirection, is_drag: bool
    ) -> Gdk.Rectangle: ...

class SwipeableInterface(GObject.GPointer):
    parent: GObject.TypeInterface = ...
    get_distance: Callable[[Swipeable], float] = ...
    get_snap_points: Callable[[Swipeable], list[float]] = ...
    get_progress: Callable[[Swipeable], float] = ...
    get_cancel_progress: Callable[[Swipeable], float] = ...
    get_swipe_area: Callable[
        [Swipeable, NavigationDirection, bool], Gdk.Rectangle
    ] = ...
    padding: list[None] = ...

class TabBar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        autohide: bool
        end_action_widget: Optional[Gtk.Widget]
        expand_tabs: bool
        inverted: bool
        is_overflowing: bool
        start_action_widget: Optional[Gtk.Widget]
        tabs_revealed: bool
        view: Optional[TabView]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        autohide: bool = ...,
        end_action_widget: Gtk.Widget = ...,
        expand_tabs: bool = ...,
        inverted: bool = ...,
        start_action_widget: Gtk.Widget = ...,
        view: TabView = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_autohide(self) -> bool: ...
    def get_end_action_widget(self) -> Optional[Gtk.Widget]: ...
    def get_expand_tabs(self) -> bool: ...
    def get_inverted(self) -> bool: ...
    def get_is_overflowing(self) -> bool: ...
    def get_start_action_widget(self) -> Optional[Gtk.Widget]: ...
    def get_tabs_revealed(self) -> bool: ...
    def get_view(self) -> Optional[TabView]: ...
    @classmethod
    def new(cls) -> TabBar: ...
    def set_autohide(self, autohide: bool) -> None: ...
    def set_end_action_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_expand_tabs(self, expand_tabs: bool) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_start_action_widget(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_view(self, view: Optional[TabView] = None) -> None: ...
    def setup_extra_drop_target(
        self, actions: Gdk.DragAction, types: Optional[Sequence[Type]] = None
    ) -> None: ...

class TabBarClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class TabPage(GObject.Object):
    class Props:
        child: Gtk.Widget
        icon: Optional[Gio.Icon]
        indicator_activatable: bool
        indicator_icon: Optional[Gio.Icon]
        indicator_tooltip: str
        loading: bool
        needs_attention: bool
        parent: Optional[TabPage]
        pinned: bool
        selected: bool
        title: str
        tooltip: Optional[str]
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        icon: Gio.Icon = ...,
        indicator_activatable: bool = ...,
        indicator_icon: Gio.Icon = ...,
        indicator_tooltip: str = ...,
        loading: bool = ...,
        needs_attention: bool = ...,
        parent: TabPage = ...,
        title: str = ...,
        tooltip: str = ...,
    ): ...
    def get_child(self) -> Gtk.Widget: ...
    def get_icon(self) -> Optional[Gio.Icon]: ...
    def get_indicator_activatable(self) -> bool: ...
    def get_indicator_icon(self) -> Optional[Gio.Icon]: ...
    def get_indicator_tooltip(self) -> str: ...
    def get_loading(self) -> bool: ...
    def get_needs_attention(self) -> bool: ...
    def get_parent(self) -> Optional[TabPage]: ...
    def get_pinned(self) -> bool: ...
    def get_selected(self) -> bool: ...
    def get_title(self) -> str: ...
    def get_tooltip(self) -> Optional[str]: ...
    def set_icon(self, icon: Optional[Gio.Icon] = None) -> None: ...
    def set_indicator_activatable(self, activatable: bool) -> None: ...
    def set_indicator_icon(self, indicator_icon: Optional[Gio.Icon] = None) -> None: ...
    def set_indicator_tooltip(self, tooltip: str) -> None: ...
    def set_loading(self, loading: bool) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_tooltip(self, tooltip: str) -> None: ...

class TabPageClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class TabView(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        default_icon: Gio.Icon
        is_transferring_page: bool
        menu_model: Optional[Gio.MenuModel]
        n_pages: int
        n_pinned_pages: int
        pages: Gtk.SelectionModel
        selected_page: Optional[TabPage]
        shortcuts: TabViewShortcuts
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        default_icon: Gio.Icon = ...,
        menu_model: Gio.MenuModel = ...,
        selected_page: TabPage = ...,
        shortcuts: TabViewShortcuts = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_page(
        self, child: Gtk.Widget, parent: Optional[TabPage] = None
    ) -> TabPage: ...
    def add_shortcuts(self, shortcuts: TabViewShortcuts) -> None: ...
    def append(self, child: Gtk.Widget) -> TabPage: ...
    def append_pinned(self, child: Gtk.Widget) -> TabPage: ...
    def close_other_pages(self, page: TabPage) -> None: ...
    def close_page(self, page: TabPage) -> None: ...
    def close_page_finish(self, page: TabPage, confirm: bool) -> None: ...
    def close_pages_after(self, page: TabPage) -> None: ...
    def close_pages_before(self, page: TabPage) -> None: ...
    def get_default_icon(self) -> Gio.Icon: ...
    def get_is_transferring_page(self) -> bool: ...
    def get_menu_model(self) -> Optional[Gio.MenuModel]: ...
    def get_n_pages(self) -> int: ...
    def get_n_pinned_pages(self) -> int: ...
    def get_nth_page(self, position: int) -> TabPage: ...
    def get_page(self, child: Gtk.Widget) -> TabPage: ...
    def get_page_position(self, page: TabPage) -> int: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_selected_page(self) -> Optional[TabPage]: ...
    def get_shortcuts(self) -> TabViewShortcuts: ...
    def insert(self, child: Gtk.Widget, position: int) -> TabPage: ...
    def insert_pinned(self, child: Gtk.Widget, position: int) -> TabPage: ...
    @classmethod
    def new(cls) -> TabView: ...
    def prepend(self, child: Gtk.Widget) -> TabPage: ...
    def prepend_pinned(self, child: Gtk.Widget) -> TabPage: ...
    def remove_shortcuts(self, shortcuts: TabViewShortcuts) -> None: ...
    def reorder_backward(self, page: TabPage) -> bool: ...
    def reorder_first(self, page: TabPage) -> bool: ...
    def reorder_forward(self, page: TabPage) -> bool: ...
    def reorder_last(self, page: TabPage) -> bool: ...
    def reorder_page(self, page: TabPage, position: int) -> bool: ...
    def select_next_page(self) -> bool: ...
    def select_previous_page(self) -> bool: ...
    def set_default_icon(self, default_icon: Gio.Icon) -> None: ...
    def set_menu_model(self, menu_model: Optional[Gio.MenuModel] = None) -> None: ...
    def set_page_pinned(self, page: TabPage, pinned: bool) -> None: ...
    def set_selected_page(self, selected_page: TabPage) -> None: ...
    def set_shortcuts(self, shortcuts: TabViewShortcuts) -> None: ...
    def transfer_page(
        self, page: TabPage, other_view: TabView, position: int
    ) -> None: ...

class TabViewClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class TimedAnimation(Animation):
    class Props:
        alternate: bool
        duration: int
        easing: Easing
        repeat_count: int
        reverse: bool
        value_from: float
        value_to: float
        state: AnimationState
        target: AnimationTarget
        value: float
        widget: Gtk.Widget
    props: Props = ...
    def __init__(
        self,
        alternate: bool = ...,
        duration: int = ...,
        easing: Easing = ...,
        repeat_count: int = ...,
        reverse: bool = ...,
        value_from: float = ...,
        value_to: float = ...,
        target: AnimationTarget = ...,
        widget: Gtk.Widget = ...,
    ): ...
    def get_alternate(self) -> bool: ...
    def get_duration(self) -> int: ...
    def get_easing(self) -> Easing: ...
    def get_repeat_count(self) -> int: ...
    def get_reverse(self) -> bool: ...
    def get_value_from(self) -> float: ...
    def get_value_to(self) -> float: ...
    @classmethod
    def new(
        cls,
        widget: Gtk.Widget,
        from_: float,
        to: float,
        duration: int,
        target: AnimationTarget,
    ) -> TimedAnimation: ...
    def set_alternate(self, alternate: bool) -> None: ...
    def set_duration(self, duration: int) -> None: ...
    def set_easing(self, easing: Easing) -> None: ...
    def set_repeat_count(self, repeat_count: int) -> None: ...
    def set_reverse(self, reverse: bool) -> None: ...
    def set_value_from(self, value: float) -> None: ...
    def set_value_to(self, value: float) -> None: ...

class TimedAnimationClass(GObject.GPointer): ...

class Toast(GObject.Object):
    class Props:
        action_name: Optional[str]
        action_target: GLib.Variant
        button_label: Optional[str]
        custom_title: Optional[Gtk.Widget]
        priority: ToastPriority
        timeout: int
        title: Optional[str]
    props: Props = ...
    def __init__(
        self,
        action_name: str = ...,
        action_target: GLib.Variant = ...,
        button_label: str = ...,
        custom_title: Gtk.Widget = ...,
        priority: ToastPriority = ...,
        timeout: int = ...,
        title: str = ...,
    ): ...
    def dismiss(self) -> None: ...
    def get_action_name(self) -> Optional[str]: ...
    def get_action_target_value(self) -> Optional[GLib.Variant]: ...
    def get_button_label(self) -> Optional[str]: ...
    def get_custom_title(self) -> Optional[Gtk.Widget]: ...
    def get_priority(self) -> ToastPriority: ...
    def get_timeout(self) -> int: ...
    def get_title(self) -> Optional[str]: ...
    @classmethod
    def new(cls, title: str) -> Toast: ...
    def set_action_name(self, action_name: Optional[str] = None) -> None: ...
    def set_action_target_value(
        self, action_target: Optional[GLib.Variant] = None
    ) -> None: ...
    def set_button_label(self, button_label: Optional[str] = None) -> None: ...
    def set_custom_title(self, widget: Optional[Gtk.Widget] = None) -> None: ...
    def set_detailed_action_name(
        self, detailed_action_name: Optional[str] = None
    ) -> None: ...
    def set_priority(self, priority: ToastPriority) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_title(self, title: str) -> None: ...

class ToastClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class ToastOverlay(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        child: Optional[Gtk.Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add_toast(self, toast: Toast) -> None: ...
    def get_child(self) -> Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> ToastOverlay: ...
    def set_child(self, child: Optional[Gtk.Widget] = None) -> None: ...

class ToastOverlayClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ViewStack(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        hhomogeneous: bool
        pages: Gtk.SelectionModel
        vhomogeneous: bool
        visible_child: Optional[Gtk.Widget]
        visible_child_name: Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        hhomogeneous: bool = ...,
        vhomogeneous: bool = ...,
        visible_child: Gtk.Widget = ...,
        visible_child_name: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def add(self, child: Gtk.Widget) -> ViewStackPage: ...
    def add_named(
        self, child: Gtk.Widget, name: Optional[str] = None
    ) -> ViewStackPage: ...
    def add_titled(
        self, child: Gtk.Widget, name: Optional[str], title: str
    ) -> ViewStackPage: ...
    def add_titled_with_icon(
        self, child: Gtk.Widget, name: Optional[str], title: str, icon_name: str
    ) -> ViewStackPage: ...
    def get_child_by_name(self, name: str) -> Optional[Gtk.Widget]: ...
    def get_hhomogeneous(self) -> bool: ...
    def get_page(self, child: Gtk.Widget) -> ViewStackPage: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_vhomogeneous(self) -> bool: ...
    def get_visible_child(self) -> Optional[Gtk.Widget]: ...
    def get_visible_child_name(self) -> Optional[str]: ...
    @classmethod
    def new(cls) -> ViewStack: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_hhomogeneous(self, hhomogeneous: bool) -> None: ...
    def set_vhomogeneous(self, vhomogeneous: bool) -> None: ...
    def set_visible_child(self, child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class ViewStackClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ViewStackPage(GObject.Object):
    class Props:
        badge_number: int
        child: Gtk.Widget
        icon_name: Optional[str]
        name: Optional[str]
        needs_attention: bool
        title: Optional[str]
        use_underline: bool
        visible: bool
    props: Props = ...
    def __init__(
        self,
        badge_number: int = ...,
        child: Gtk.Widget = ...,
        icon_name: str = ...,
        name: str = ...,
        needs_attention: bool = ...,
        title: str = ...,
        use_underline: bool = ...,
        visible: bool = ...,
    ): ...
    def get_badge_number(self) -> int: ...
    def get_child(self) -> Gtk.Widget: ...
    def get_icon_name(self) -> Optional[str]: ...
    def get_name(self) -> Optional[str]: ...
    def get_needs_attention(self) -> bool: ...
    def get_title(self) -> Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    def get_visible(self) -> bool: ...
    def set_badge_number(self, badge_number: int) -> None: ...
    def set_icon_name(self, icon_name: Optional[str] = None) -> None: ...
    def set_name(self, name: Optional[str] = None) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_title(self, title: Optional[str] = None) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class ViewStackPageClass(GObject.GPointer):
    parent_class: GObject.ObjectClass = ...

class ViewSwitcher(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        policy: ViewSwitcherPolicy
        stack: Optional[ViewStack]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        policy: ViewSwitcherPolicy = ...,
        stack: ViewStack = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_policy(self) -> ViewSwitcherPolicy: ...
    def get_stack(self) -> Optional[ViewStack]: ...
    @classmethod
    def new(cls) -> ViewSwitcher: ...
    def set_policy(self, policy: ViewSwitcherPolicy) -> None: ...
    def set_stack(self, stack: Optional[ViewStack] = None) -> None: ...

class ViewSwitcherBar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        reveal: bool
        stack: Optional[ViewStack]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        reveal: bool = ...,
        stack: ViewStack = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_reveal(self) -> bool: ...
    def get_stack(self) -> Optional[ViewStack]: ...
    @classmethod
    def new(cls) -> ViewSwitcherBar: ...
    def set_reveal(self, reveal: bool) -> None: ...
    def set_stack(self, stack: Optional[ViewStack] = None) -> None: ...

class ViewSwitcherBarClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ViewSwitcherClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class ViewSwitcherTitle(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    class Props:
        stack: Optional[ViewStack]
        subtitle: str
        title: str
        title_visible: bool
        view_switcher_enabled: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        stack: ViewStack = ...,
        subtitle: str = ...,
        title: str = ...,
        view_switcher_enabled: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_stack(self) -> Optional[ViewStack]: ...
    def get_subtitle(self) -> str: ...
    def get_title(self) -> str: ...
    def get_title_visible(self) -> bool: ...
    def get_view_switcher_enabled(self) -> bool: ...
    @classmethod
    def new(cls) -> ViewSwitcherTitle: ...
    def set_stack(self, stack: Optional[ViewStack] = None) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_view_switcher_enabled(self, enabled: bool) -> None: ...

class ViewSwitcherTitleClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class Window(
    Gtk.Window,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    class Props:
        content: Optional[Gtk.Widget]
        application: Optional[Gtk.Application]
        child: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: Gtk.Widget
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        title: Optional[str]
        titlebar: Optional[Gtk.Widget]
        transient_for: Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        startup_id: str
    props: Props = ...
    parent_instance: Gtk.Window = ...
    def __init__(
        self,
        content: Gtk.Widget = ...,
        application: Gtk.Application = ...,
        child: Gtk.Widget = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: Gtk.Widget = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: Gtk.Widget = ...,
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
        titlebar: Gtk.Widget = ...,
        transient_for: Gtk.Window = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_content(self) -> Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> Window: ...
    def set_content(self, content: Optional[Gtk.Widget] = None) -> None: ...

class WindowClass(GObject.GPointer):
    parent_class: Gtk.WindowClass = ...
    padding: list[None] = ...

class WindowTitle(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    class Props:
        subtitle: str
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: Optional[Gtk.LayoutManager]
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: Optional[Gtk.Widget]
        receives_default: bool
        root: Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
    props: Props = ...
    def __init__(
        self,
        subtitle: str = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: Sequence[str] = ...,
        css_name: str = ...,
        cursor: Gdk.Cursor = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: Gtk.LayoutManager = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: str = ...,
        tooltip_text: str = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ): ...
    def get_subtitle(self) -> str: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls, title: str, subtitle: str) -> WindowTitle: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_title(self, title: str) -> None: ...

class WindowTitleClass(GObject.GPointer):
    parent_class: Gtk.WidgetClass = ...

class TabViewShortcuts(GObject.GFlags):
    ALL_SHORTCUTS = 4095
    ALT_DIGITS = 1024
    ALT_ZERO = 2048
    CONTROL_END = 32
    CONTROL_HOME = 16
    CONTROL_PAGE_DOWN = 8
    CONTROL_PAGE_UP = 4
    CONTROL_SHIFT_END = 512
    CONTROL_SHIFT_HOME = 256
    CONTROL_SHIFT_PAGE_DOWN = 128
    CONTROL_SHIFT_PAGE_UP = 64
    CONTROL_SHIFT_TAB = 2
    CONTROL_TAB = 1
    NONE = 0

class AnimationState(GObject.GEnum):
    FINISHED = 3
    IDLE = 0
    PAUSED = 1
    PLAYING = 2

class CenteringPolicy(GObject.GEnum):
    LOOSE = 0
    STRICT = 1

class ColorScheme(GObject.GEnum):
    DEFAULT = 0
    FORCE_DARK = 4
    FORCE_LIGHT = 1
    PREFER_DARK = 3
    PREFER_LIGHT = 2

class Easing(GObject.GEnum):
    EASE_IN_BACK = 25
    EASE_IN_BOUNCE = 28
    EASE_IN_CIRC = 19
    EASE_IN_CUBIC = 4
    EASE_IN_ELASTIC = 22
    EASE_IN_EXPO = 16
    EASE_IN_OUT_BACK = 27
    EASE_IN_OUT_BOUNCE = 30
    EASE_IN_OUT_CIRC = 21
    EASE_IN_OUT_CUBIC = 6
    EASE_IN_OUT_ELASTIC = 24
    EASE_IN_OUT_EXPO = 18
    EASE_IN_OUT_QUAD = 3
    EASE_IN_OUT_QUART = 9
    EASE_IN_OUT_QUINT = 12
    EASE_IN_OUT_SINE = 15
    EASE_IN_QUAD = 1
    EASE_IN_QUART = 7
    EASE_IN_QUINT = 10
    EASE_IN_SINE = 13
    EASE_OUT_BACK = 26
    EASE_OUT_BOUNCE = 29
    EASE_OUT_CIRC = 20
    EASE_OUT_CUBIC = 5
    EASE_OUT_ELASTIC = 23
    EASE_OUT_EXPO = 17
    EASE_OUT_QUAD = 2
    EASE_OUT_QUART = 8
    EASE_OUT_QUINT = 11
    EASE_OUT_SINE = 14
    LINEAR = 0
    @staticmethod
    def ease(self: Easing, value: float) -> float: ...

class FlapFoldPolicy(GObject.GEnum):
    ALWAYS = 1
    AUTO = 2
    NEVER = 0

class FlapTransitionType(GObject.GEnum):
    OVER = 0
    SLIDE = 2
    UNDER = 1

class FoldThresholdPolicy(GObject.GEnum):
    MINIMUM = 0
    NATURAL = 1

class LeafletTransitionType(GObject.GEnum):
    OVER = 0
    SLIDE = 2
    UNDER = 1

class NavigationDirection(GObject.GEnum):
    BACK = 0
    FORWARD = 1

class ResponseAppearance(GObject.GEnum):
    DEFAULT = 0
    DESTRUCTIVE = 2
    SUGGESTED = 1

class SqueezerTransitionType(GObject.GEnum):
    CROSSFADE = 1
    NONE = 0

class ToastPriority(GObject.GEnum):
    HIGH = 1
    NORMAL = 0

class ViewSwitcherPolicy(GObject.GEnum):
    NARROW = 0
    WIDE = 1
