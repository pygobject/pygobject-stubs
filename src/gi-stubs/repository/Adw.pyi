import typing

from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango
from typing_extensions import Self

T = typing.TypeVar("T")

DURATION_INFINITE: int = 4294967295
MAJOR_VERSION: int = 1
MICRO_VERSION: int = 7
MINOR_VERSION: int = 7
VERSION_S: str = "1.7.7"
_lock = ...  # FIXME Constant
_namespace: str = "Adw"
_version: str = "1"

def accent_color_to_rgba(self: AccentColor) -> Gdk.RGBA: ...
def accent_color_to_standalone_rgba(self: AccentColor, dark: bool) -> Gdk.RGBA: ...
def breakpoint_condition_parse(str: str) -> BreakpointCondition: ...
def easing_ease(self: Easing, value: float) -> float: ...
def get_enable_animations(widget: Gtk.Widget) -> bool: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def init() -> None: ...
def is_initialized() -> bool: ...
def length_unit_from_px(
    unit: LengthUnit, value: float, settings: typing.Optional[Gtk.Settings] = None
) -> float: ...
def length_unit_to_px(
    unit: LengthUnit, value: float, settings: typing.Optional[Gtk.Settings] = None
) -> float: ...
def lerp(a: float, b: float, t: float) -> float: ...
def rgba_to_standalone(rgba: Gdk.RGBA, dark: bool) -> Gdk.RGBA: ...

class AboutDialog(
    Dialog, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.ShortcutManager
):
    """
    :Constructors:

    ::

        AboutDialog(**properties)
        new() -> Adw.Dialog
        new_from_appdata(resource_path:str, release_notes_version:str=None) -> Adw.Dialog

    Object AdwAboutDialog

    Signals from AdwAboutDialog:
      activate-link (gchararray) -> gboolean

    Properties from AdwAboutDialog:
      application-icon -> gchararray: application-icon
      application-name -> gchararray: application-name
      developer-name -> gchararray: developer-name
      version -> gchararray: version
      release-notes-version -> gchararray: release-notes-version
      release-notes -> gchararray: release-notes
      comments -> gchararray: comments
      website -> gchararray: website
      support-url -> gchararray: support-url
      issue-url -> gchararray: issue-url
      debug-info -> gchararray: debug-info
      debug-info-filename -> gchararray: debug-info-filename
      developers -> GStrv: developers
      designers -> GStrv: designers
      artists -> GStrv: artists
      documenters -> GStrv: documenters
      translator-credits -> gchararray: translator-credits
      copyright -> gchararray: copyright
      license-type -> GtkLicense: license-type
      license -> gchararray: license

    Signals from AdwDialog:
      closed ()
      close-attempt ()

    Properties from AdwDialog:
      child -> GtkWidget: child
      title -> gchararray: title
      can-close -> gboolean: can-close
      content-width -> gint: content-width
      content-height -> gint: content-height
      follows-content-size -> gboolean: follows-content-size
      presentation-mode -> AdwDialogPresentationMode: presentation-mode
      focus-widget -> GtkWidget: focus-widget
      default-widget -> GtkWidget: default-widget
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Dialog.Props):
        application_icon: str
        application_name: str
        artists: typing.Optional[list[str]]
        comments: str
        copyright: str
        debug_info: str
        debug_info_filename: str
        designers: typing.Optional[list[str]]
        developer_name: str
        developers: typing.Optional[list[str]]
        documenters: typing.Optional[list[str]]
        issue_url: str
        license: str
        license_type: Gtk.License
        release_notes: str
        release_notes_version: str
        support_url: str
        translator_credits: str
        version: str
        website: str
        can_close: bool
        child: typing.Optional[Gtk.Widget]
        content_height: int
        content_width: int
        current_breakpoint: typing.Optional[Breakpoint]
        default_widget: typing.Optional[Gtk.Widget]
        focus_widget: typing.Optional[Gtk.Widget]
        follows_content_size: bool
        presentation_mode: DialogPresentationMode
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        application_icon: str = ...,
        application_name: str = ...,
        artists: typing.Optional[typing.Sequence[str]] = ...,
        comments: str = ...,
        copyright: str = ...,
        debug_info: str = ...,
        debug_info_filename: str = ...,
        designers: typing.Optional[typing.Sequence[str]] = ...,
        developer_name: str = ...,
        developers: typing.Optional[typing.Sequence[str]] = ...,
        documenters: typing.Optional[typing.Sequence[str]] = ...,
        issue_url: str = ...,
        license: str = ...,
        license_type: Gtk.License = ...,
        release_notes: str = ...,
        release_notes_version: str = ...,
        support_url: str = ...,
        translator_credits: str = ...,
        version: str = ...,
        website: str = ...,
        can_close: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        content_height: int = ...,
        content_width: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        follows_content_size: bool = ...,
        presentation_mode: DialogPresentationMode = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_acknowledgement_section(
        self, name: typing.Optional[str], people: typing.Sequence[str]
    ) -> None: ...
    def add_credit_section(
        self, name: typing.Optional[str], people: typing.Sequence[str]
    ) -> None: ...
    def add_legal_section(
        self,
        title: str,
        copyright: typing.Optional[str],
        license_type: Gtk.License,
        license: typing.Optional[str] = None,
    ) -> None: ...
    def add_link(self, title: str, url: str) -> None: ...
    def add_other_app(self, appid: str, name: str, summary: str) -> None: ...
    def get_application_icon(self) -> str: ...
    def get_application_name(self) -> str: ...
    def get_artists(self) -> typing.Optional[list[str]]: ...
    def get_comments(self) -> str: ...
    def get_copyright(self) -> str: ...
    def get_debug_info(self) -> str: ...
    def get_debug_info_filename(self) -> str: ...
    def get_designers(self) -> typing.Optional[list[str]]: ...
    def get_developer_name(self) -> str: ...
    def get_developers(self) -> typing.Optional[list[str]]: ...
    def get_documenters(self) -> typing.Optional[list[str]]: ...
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
    def new(cls) -> AboutDialog: ...
    @classmethod
    def new_from_appdata(
        cls, resource_path: str, release_notes_version: typing.Optional[str] = None
    ) -> AboutDialog: ...
    def set_application_icon(self, application_icon: str) -> None: ...
    def set_application_name(self, application_name: str) -> None: ...
    def set_artists(
        self, artists: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_comments(self, comments: str) -> None: ...
    def set_copyright(self, copyright: str) -> None: ...
    def set_debug_info(self, debug_info: str) -> None: ...
    def set_debug_info_filename(self, filename: str) -> None: ...
    def set_designers(
        self, designers: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_developer_name(self, developer_name: str) -> None: ...
    def set_developers(
        self, developers: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_documenters(
        self, documenters: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_issue_url(self, issue_url: str) -> None: ...
    def set_license(self, license: str) -> None: ...
    def set_license_type(self, license_type: Gtk.License) -> None: ...
    def set_release_notes(self, release_notes: str) -> None: ...
    def set_release_notes_version(self, version: str) -> None: ...
    def set_support_url(self, support_url: str) -> None: ...
    def set_translator_credits(self, translator_credits: str) -> None: ...
    def set_version(self, version: str) -> None: ...
    def set_website(self, website: str) -> None: ...

class AboutDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AboutDialogClass()
    """

    parent_class: DialogClass = ...

class AboutWindow(
    Window,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Native,
    Gtk.Root,
    Gtk.ShortcutManager,
):
    """
    :Constructors:

    ::

        AboutWindow(**properties)
        new() -> Gtk.Widget
        new_from_appdata(resource_path:str, release_notes_version:str=None) -> Gtk.Widget

    Object AdwAboutWindow

    Signals from AdwAboutWindow:
      activate-link (gchararray) -> gboolean

    Properties from AdwAboutWindow:
      application-icon -> gchararray: application-icon
      application-name -> gchararray: application-name
      developer-name -> gchararray: developer-name
      version -> gchararray: version
      release-notes-version -> gchararray: release-notes-version
      release-notes -> gchararray: release-notes
      comments -> gchararray: comments
      website -> gchararray: website
      support-url -> gchararray: support-url
      issue-url -> gchararray: issue-url
      debug-info -> gchararray: debug-info
      debug-info-filename -> gchararray: debug-info-filename
      developers -> GStrv: developers
      designers -> GStrv: designers
      artists -> GStrv: artists
      documenters -> GStrv: documenters
      translator-credits -> gchararray: translator-credits
      copyright -> gchararray: copyright
      license-type -> GtkLicense: license-type
      license -> gchararray: license

    Properties from AdwWindow:
      content -> GtkWidget: content
      current-breakpoint -> AdwBreakpoint: current-breakpoint
      dialogs -> GListModel: dialogs
      visible-dialog -> AdwDialog: visible-dialog
      adaptive-preview -> gboolean: adaptive-preview

    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Window.Props):
        application_icon: str
        application_name: str
        artists: typing.Optional[list[str]]
        comments: str
        copyright: str
        debug_info: str
        debug_info_filename: str
        designers: typing.Optional[list[str]]
        developer_name: str
        developers: typing.Optional[list[str]]
        documenters: typing.Optional[list[str]]
        issue_url: str
        license: str
        license_type: Gtk.License
        release_notes: str
        release_notes_version: str
        support_url: str
        translator_credits: str
        version: str
        website: str
        adaptive_preview: bool
        content: typing.Optional[Gtk.Widget]
        current_breakpoint: typing.Optional[Breakpoint]
        dialogs: Gio.ListModel
        visible_dialog: typing.Optional[Dialog]
        application: typing.Optional[Gtk.Application]
        child: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: typing.Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: typing.Optional[Gtk.Widget]
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: typing.Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: typing.Optional[str]
        titlebar: typing.Optional[Gtk.Widget]
        transient_for: typing.Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        artists: typing.Optional[typing.Sequence[str]] = ...,
        comments: str = ...,
        copyright: str = ...,
        debug_info: str = ...,
        debug_info_filename: str = ...,
        designers: typing.Optional[typing.Sequence[str]] = ...,
        developer_name: str = ...,
        developers: typing.Optional[typing.Sequence[str]] = ...,
        documenters: typing.Optional[typing.Sequence[str]] = ...,
        issue_url: str = ...,
        license: str = ...,
        license_type: Gtk.License = ...,
        release_notes: str = ...,
        release_notes_version: str = ...,
        support_url: str = ...,
        translator_credits: str = ...,
        version: str = ...,
        website: str = ...,
        adaptive_preview: bool = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        application: typing.Optional[Gtk.Application] = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: typing.Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: typing.Optional[str] = ...,
        titlebar: typing.Optional[Gtk.Widget] = ...,
        transient_for: typing.Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_acknowledgement_section(
        self, name: typing.Optional[str], people: typing.Sequence[str]
    ) -> None: ...
    def add_credit_section(
        self, name: typing.Optional[str], people: typing.Sequence[str]
    ) -> None: ...
    def add_legal_section(
        self,
        title: str,
        copyright: typing.Optional[str],
        license_type: Gtk.License,
        license: typing.Optional[str] = None,
    ) -> None: ...
    def add_link(self, title: str, url: str) -> None: ...
    def get_application_icon(self) -> str: ...
    def get_application_name(self) -> str: ...
    def get_artists(self) -> typing.Optional[list[str]]: ...
    def get_comments(self) -> str: ...
    def get_copyright(self) -> str: ...
    def get_debug_info(self) -> str: ...
    def get_debug_info_filename(self) -> str: ...
    def get_designers(self) -> typing.Optional[list[str]]: ...
    def get_developer_name(self) -> str: ...
    def get_developers(self) -> typing.Optional[list[str]]: ...
    def get_documenters(self) -> typing.Optional[list[str]]: ...
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
    @classmethod
    def new_from_appdata(
        cls, resource_path: str, release_notes_version: typing.Optional[str] = None
    ) -> AboutWindow: ...
    def set_application_icon(self, application_icon: str) -> None: ...
    def set_application_name(self, application_name: str) -> None: ...
    def set_artists(
        self, artists: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_comments(self, comments: str) -> None: ...
    def set_copyright(self, copyright: str) -> None: ...
    def set_debug_info(self, debug_info: str) -> None: ...
    def set_debug_info_filename(self, filename: str) -> None: ...
    def set_designers(
        self, designers: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_developer_name(self, developer_name: str) -> None: ...
    def set_developers(
        self, developers: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
    def set_documenters(
        self, documenters: typing.Optional[typing.Sequence[str]] = None
    ) -> None: ...
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
    """
    :Constructors:

    ::

        AboutWindowClass()
    """

    parent_class: WindowClass = ...

class ActionRow(
    PreferencesRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        ActionRow(**properties)
        new() -> Gtk.Widget

    Object AdwActionRow

    Signals from AdwActionRow:
      activated ()

    Properties from AdwActionRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      activatable-widget -> GtkWidget: activatable-widget
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines
      subtitle-selectable -> gboolean: subtitle-selectable

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(PreferencesRow.Props):
        activatable_widget: typing.Optional[Gtk.Widget]
        icon_name: typing.Optional[str]
        subtitle: typing.Optional[str]
        subtitle_lines: int
        subtitle_selectable: bool
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        activatable_widget: typing.Optional[Gtk.Widget] = ...,
        icon_name: typing.Optional[str] = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        subtitle_selectable: bool = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def activate(self) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, widget: Gtk.Widget) -> None: ...
    def get_activatable_widget(self) -> typing.Optional[Gtk.Widget]: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_subtitle(self) -> typing.Optional[str]: ...
    def get_subtitle_lines(self) -> int: ...
    def get_subtitle_selectable(self) -> bool: ...
    def get_title_lines(self) -> int: ...
    @classmethod
    def new(cls) -> ActionRow: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_activatable_widget(
        self, widget: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_subtitle_lines(self, subtitle_lines: int) -> None: ...
    def set_subtitle_selectable(self, subtitle_selectable: bool) -> None: ...
    def set_title_lines(self, title_lines: int) -> None: ...

class ActionRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ActionRowClass()
    """

    parent_class: PreferencesRowClass = ...
    activate: typing.Callable[[ActionRow], None] = ...
    padding: list[None] = ...

class AlertDialog(
    Dialog, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.ShortcutManager
):
    """
    :Constructors:

    ::

        AlertDialog(**properties)
        new(heading:str=None, body:str=None) -> Adw.Dialog

    Object AdwAlertDialog

    Signals from AdwAlertDialog:
      response (gchararray)

    Properties from AdwAlertDialog:
      heading -> gchararray: heading
      heading-use-markup -> gboolean: heading-use-markup
      body -> gchararray: body
      body-use-markup -> gboolean: body-use-markup
      extra-child -> GtkWidget: extra-child
      prefer-wide-layout -> gboolean: prefer-wide-layout
      default-response -> gchararray: default-response
      close-response -> gchararray: close-response

    Signals from AdwDialog:
      closed ()
      close-attempt ()

    Properties from AdwDialog:
      child -> GtkWidget: child
      title -> gchararray: title
      can-close -> gboolean: can-close
      content-width -> gint: content-width
      content-height -> gint: content-height
      follows-content-size -> gboolean: follows-content-size
      presentation-mode -> AdwDialogPresentationMode: presentation-mode
      focus-widget -> GtkWidget: focus-widget
      default-widget -> GtkWidget: default-widget
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Dialog.Props):
        body: str
        body_use_markup: bool
        close_response: str
        default_response: typing.Optional[str]
        extra_child: typing.Optional[Gtk.Widget]
        heading: typing.Optional[str]
        heading_use_markup: bool
        prefer_wide_layout: bool
        can_close: bool
        child: typing.Optional[Gtk.Widget]
        content_height: int
        content_width: int
        current_breakpoint: typing.Optional[Breakpoint]
        default_widget: typing.Optional[Gtk.Widget]
        focus_widget: typing.Optional[Gtk.Widget]
        follows_content_size: bool
        presentation_mode: DialogPresentationMode
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    parent_instance: Dialog = ...
    def __init__(
        self,
        body: str = ...,
        body_use_markup: bool = ...,
        close_response: str = ...,
        default_response: typing.Optional[str] = ...,
        extra_child: typing.Optional[Gtk.Widget] = ...,
        heading: typing.Optional[str] = ...,
        heading_use_markup: bool = ...,
        prefer_wide_layout: bool = ...,
        can_close: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        content_height: int = ...,
        content_width: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        follows_content_size: bool = ...,
        presentation_mode: DialogPresentationMode = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_response(self, id: str, label: str) -> None: ...
    def choose(
        self,
        parent: typing.Optional[Gtk.Widget] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def choose_finish(self, result: Gio.AsyncResult) -> str: ...
    def do_response(self, response: str) -> None: ...
    def get_body(self) -> str: ...
    def get_body_use_markup(self) -> bool: ...
    def get_close_response(self) -> str: ...
    def get_default_response(self) -> typing.Optional[str]: ...
    def get_extra_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_heading(self) -> typing.Optional[str]: ...
    def get_heading_use_markup(self) -> bool: ...
    def get_prefer_wide_layout(self) -> bool: ...
    def get_response_appearance(self, response: str) -> ResponseAppearance: ...
    def get_response_enabled(self, response: str) -> bool: ...
    def get_response_label(self, response: str) -> str: ...
    def has_response(self, response: str) -> bool: ...
    @classmethod
    def new(
        cls, heading: typing.Optional[str] = None, body: typing.Optional[str] = None
    ) -> AlertDialog: ...
    def remove_response(self, id: str) -> None: ...
    def set_body(self, body: str) -> None: ...
    def set_body_use_markup(self, use_markup: bool) -> None: ...
    def set_close_response(self, response: str) -> None: ...
    def set_default_response(self, response: typing.Optional[str] = None) -> None: ...
    def set_extra_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_heading(self, heading: typing.Optional[str] = None) -> None: ...
    def set_heading_use_markup(self, use_markup: bool) -> None: ...
    def set_prefer_wide_layout(self, prefer_wide_layout: bool) -> None: ...
    def set_response_appearance(
        self, response: str, appearance: ResponseAppearance
    ) -> None: ...
    def set_response_enabled(self, response: str, enabled: bool) -> None: ...
    def set_response_label(self, response: str, label: str) -> None: ...

class AlertDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AlertDialogClass()
    """

    parent_class: DialogClass = ...
    response: typing.Callable[[AlertDialog, str], None] = ...
    padding: list[None] = ...

class Animation(GObject.Object):
    """
    :Constructors:

    ::

        Animation(**properties)

    Object AdwAnimation

    Signals from AdwAnimation:
      done ()

    Properties from AdwAnimation:
      widget -> GtkWidget: widget
      target -> AdwAnimationTarget: target
      value -> gdouble: value
      state -> AdwAnimationState: state
      follow-enable-animations-setting -> gboolean: follow-enable-animations-setting

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        follow_enable_animations_setting: bool
        state: AnimationState
        target: AnimationTarget
        value: float
        widget: Gtk.Widget

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        follow_enable_animations_setting: bool = ...,
        target: AnimationTarget = ...,
        widget: Gtk.Widget = ...,
    ) -> None: ...
    def get_follow_enable_animations_setting(self) -> bool: ...
    def get_state(self) -> AnimationState: ...
    def get_target(self) -> AnimationTarget: ...
    def get_value(self) -> float: ...
    def get_widget(self) -> Gtk.Widget: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    def reset(self) -> None: ...
    def resume(self) -> None: ...
    def set_follow_enable_animations_setting(self, setting: bool) -> None: ...
    def set_target(self, target: AnimationTarget) -> None: ...
    def skip(self) -> None: ...

class AnimationClass(GObject.GPointer): ...
class AnimationTarget(GObject.Object): ...
class AnimationTargetClass(GObject.GPointer): ...

class Application(Gtk.Application, Gio.ActionGroup, Gio.ActionMap):
    """
    :Constructors:

    ::

        Application(**properties)
        new(application_id:str=None, flags:Gio.ApplicationFlags) -> Adw.Application

    Object AdwApplication

    Properties from AdwApplication:
      style-manager -> AdwStyleManager: style-manager

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkApplication:
      window-added (GtkWindow)
      window-removed (GtkWindow)
      query-end ()

    Properties from GtkApplication:
      register-session -> gboolean: register-session
      screensaver-active -> gboolean: screensaver-active
      menubar -> GMenuModel: menubar
      active-window -> GtkWindow: active-window

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GApplication:
      activate ()
      startup ()
      shutdown ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean

    Properties from GApplication:
      application-id -> gchararray: application-id
      version -> gchararray: version
      flags -> GApplicationFlags: flags
      resource-base-path -> gchararray: resource-base-path
      is-registered -> gboolean: is-registered
      is-remote -> gboolean: is-remote
      inactivity-timeout -> guint: inactivity-timeout
      action-group -> GActionGroup: action-group
      is-busy -> gboolean: is-busy

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Application.Props):
        style_manager: StyleManager
        active_window: typing.Optional[Gtk.Window]
        menubar: typing.Optional[Gio.MenuModel]
        register_session: bool
        screensaver_active: bool
        application_id: typing.Optional[str]
        flags: Gio.ApplicationFlags
        inactivity_timeout: int
        is_busy: bool
        is_registered: bool
        is_remote: bool
        resource_base_path: typing.Optional[str]
        version: typing.Optional[str]
        action_group: typing.Optional[Gio.ActionGroup]

    props: Props = ...
    parent_instance: Gtk.Application = ...
    def __init__(
        self,
        menubar: typing.Optional[Gio.MenuModel] = ...,
        register_session: bool = ...,
        action_group: typing.Optional[Gio.ActionGroup] = ...,
        application_id: typing.Optional[str] = ...,
        flags: Gio.ApplicationFlags = ...,
        inactivity_timeout: int = ...,
        resource_base_path: typing.Optional[str] = ...,
        version: str = ...,
    ) -> None: ...
    def get_style_manager(self) -> StyleManager: ...
    @classmethod
    def new(
        cls, application_id: typing.Optional[str], flags: Gio.ApplicationFlags
    ) -> Application: ...

class ApplicationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationClass()
    """

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
    """
    :Constructors:

    ::

        ApplicationWindow(**properties)
        new(app:Gtk.Application) -> Gtk.Widget

    Object AdwApplicationWindow

    Properties from AdwApplicationWindow:
      content -> GtkWidget: content
      current-breakpoint -> AdwBreakpoint: current-breakpoint
      dialogs -> GListModel: dialogs
      visible-dialog -> AdwDialog: visible-dialog
      adaptive-preview -> gboolean: adaptive-preview

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Properties from GtkApplicationWindow:
      show-menubar -> gboolean: show-menubar

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.ApplicationWindow.Props):
        adaptive_preview: bool
        content: typing.Optional[Gtk.Widget]
        current_breakpoint: typing.Optional[Breakpoint]
        dialogs: Gio.ListModel
        visible_dialog: typing.Optional[Dialog]
        show_menubar: bool
        application: typing.Optional[Gtk.Application]
        child: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: typing.Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: typing.Optional[Gtk.Widget]
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: typing.Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: typing.Optional[str]
        titlebar: typing.Optional[Gtk.Widget]
        transient_for: typing.Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        adaptive_preview: bool = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        show_menubar: bool = ...,
        application: typing.Optional[Gtk.Application] = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: typing.Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: typing.Optional[str] = ...,
        titlebar: typing.Optional[Gtk.Widget] = ...,
        transient_for: typing.Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_breakpoint(self, breakpoint: Breakpoint) -> None: ...
    def get_adaptive_preview(self) -> bool: ...
    def get_content(self) -> typing.Optional[Gtk.Widget]: ...
    def get_current_breakpoint(self) -> typing.Optional[Breakpoint]: ...
    def get_dialogs(self) -> Gio.ListModel: ...
    def get_visible_dialog(self) -> typing.Optional[Dialog]: ...
    @classmethod
    def new(cls, app: Gtk.Application) -> ApplicationWindow: ...
    def set_adaptive_preview(self, adaptive_preview: bool) -> None: ...
    def set_content(self, content: typing.Optional[Gtk.Widget] = None) -> None: ...

class ApplicationWindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ApplicationWindowClass()
    """

    parent_class: Gtk.ApplicationWindowClass = ...
    padding: list[None] = ...

class Avatar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Avatar(**properties)
        new(size:int, text:str=None, show_initials:bool) -> Gtk.Widget

    Object AdwAvatar

    Properties from AdwAvatar:
      icon-name -> gchararray: icon-name
      text -> gchararray: text
      show-initials -> gboolean: show-initials
      custom-image -> GdkPaintable: custom-image
      size -> gint: size

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        custom_image: typing.Optional[Gdk.Paintable]
        icon_name: typing.Optional[str]
        show_initials: bool
        size: int
        text: typing.Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        custom_image: typing.Optional[Gdk.Paintable] = ...,
        icon_name: typing.Optional[str] = ...,
        show_initials: bool = ...,
        size: int = ...,
        text: typing.Optional[str] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def draw_to_texture(self, scale_factor: int) -> Gdk.Texture: ...
    def get_custom_image(self) -> typing.Optional[Gdk.Paintable]: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_show_initials(self) -> bool: ...
    def get_size(self) -> int: ...
    def get_text(self) -> typing.Optional[str]: ...
    @classmethod
    def new(
        cls, size: int, text: typing.Optional[str], show_initials: bool
    ) -> Avatar: ...
    def set_custom_image(
        self, custom_image: typing.Optional[Gdk.Paintable] = None
    ) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_show_initials(self, show_initials: bool) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_text(self, text: typing.Optional[str] = None) -> None: ...

class AvatarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AvatarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Banner(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        Banner(**properties)
        new(title:str) -> Gtk.Widget

    Object AdwBanner

    Signals from AdwBanner:
      button-clicked ()

    Properties from AdwBanner:
      title -> gchararray: title
      button-label -> gchararray: button-label
      revealed -> gboolean: revealed
      use-markup -> gboolean: use-markup
      button-style -> AdwBannerButtonStyle: button-style

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        button_label: typing.Optional[str]
        button_style: BannerButtonStyle
        revealed: bool
        title: str
        use_markup: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    def __init__(
        self,
        button_label: typing.Optional[str] = ...,
        button_style: BannerButtonStyle = ...,
        revealed: bool = ...,
        title: str = ...,
        use_markup: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def get_button_label(self) -> typing.Optional[str]: ...
    def get_button_style(self) -> BannerButtonStyle: ...
    def get_revealed(self) -> bool: ...
    def get_title(self) -> str: ...
    def get_use_markup(self) -> bool: ...
    @classmethod
    def new(cls, title: str) -> Banner: ...
    def set_button_label(self, label: typing.Optional[str] = None) -> None: ...
    def set_button_style(self, style: BannerButtonStyle) -> None: ...
    def set_revealed(self, revealed: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_markup(self, use_markup: bool) -> None: ...

class BannerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BannerClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Bin(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Bin(**properties)
        new() -> Gtk.Widget

    Object AdwBin

    Properties from AdwBin:
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        child: typing.Optional[Gtk.Widget] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> Bin: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...

class BinClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BinClass()
    """

    parent_class: Gtk.WidgetClass = ...

class BottomSheet(
    Gtk.Widget, Swipeable, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        BottomSheet(**properties)
        new() -> Gtk.Widget

    Object AdwBottomSheet

    Signals from AdwBottomSheet:
      close-attempt ()

    Properties from AdwBottomSheet:
      content -> GtkWidget: content
      sheet -> GtkWidget: sheet
      bottom-bar -> GtkWidget: bottom-bar
      open -> gboolean: open
      align -> gfloat: align
      full-width -> gboolean: full-width
      show-drag-handle -> gboolean: show-drag-handle
      modal -> gboolean: modal
      can-open -> gboolean: can-open
      can-close -> gboolean: can-close
      sheet-height -> gint: sheet-height
      bottom-bar-height -> gint: bottom-bar-height
      reveal-bottom-bar -> gboolean: reveal-bottom-bar

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        align: float
        bottom_bar: typing.Optional[Gtk.Widget]
        bottom_bar_height: int
        can_close: bool
        can_open: bool
        content: typing.Optional[Gtk.Widget]
        full_width: bool
        modal: bool
        open: bool
        reveal_bottom_bar: bool
        sheet: typing.Optional[Gtk.Widget]
        sheet_height: int
        show_drag_handle: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        align: float = ...,
        bottom_bar: typing.Optional[Gtk.Widget] = ...,
        can_close: bool = ...,
        can_open: bool = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        full_width: bool = ...,
        modal: bool = ...,
        open: bool = ...,
        reveal_bottom_bar: bool = ...,
        sheet: typing.Optional[Gtk.Widget] = ...,
        show_drag_handle: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_align(self) -> float: ...
    def get_bottom_bar(self) -> typing.Optional[Gtk.Widget]: ...
    def get_bottom_bar_height(self) -> int: ...
    def get_can_close(self) -> bool: ...
    def get_can_open(self) -> bool: ...
    def get_content(self) -> typing.Optional[Gtk.Widget]: ...
    def get_full_width(self) -> bool: ...
    def get_modal(self) -> bool: ...
    def get_open(self) -> bool: ...
    def get_reveal_bottom_bar(self) -> bool: ...
    def get_sheet(self) -> typing.Optional[Gtk.Widget]: ...
    def get_sheet_height(self) -> int: ...
    def get_show_drag_handle(self) -> bool: ...
    @classmethod
    def new(cls) -> BottomSheet: ...
    def set_align(self, align: float) -> None: ...
    def set_bottom_bar(
        self, bottom_bar: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_can_close(self, can_close: bool) -> None: ...
    def set_can_open(self, can_open: bool) -> None: ...
    def set_content(self, content: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_full_width(self, full_width: bool) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_open(self, open: bool) -> None: ...
    def set_reveal_bottom_bar(self, reveal: bool) -> None: ...
    def set_sheet(self, sheet: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_show_drag_handle(self, show_drag_handle: bool) -> None: ...

class BottomSheetClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BottomSheetClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Breakpoint(GObject.Object, Gtk.Buildable):
    """
    :Constructors:

    ::

        Breakpoint(**properties)
        new(condition:Adw.BreakpointCondition) -> Adw.Breakpoint

    Object AdwBreakpoint

    Signals from AdwBreakpoint:
      apply ()
      unapply ()

    Properties from AdwBreakpoint:
      condition -> AdwBreakpointCondition: condition

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        condition: typing.Optional[BreakpointCondition]

    props: Props = ...
    def __init__(
        self, condition: typing.Optional[BreakpointCondition] = ...
    ) -> None: ...
    def add_setter(
        self,
        object: GObject.Object,
        property: str,
        value: typing.Optional[typing.Any] = None,
    ) -> None: ...
    def add_setters(
        self,
        objects: typing.Sequence[GObject.Object],
        names: typing.Sequence[str],
        values: typing.Sequence[typing.Any],
    ) -> None: ...
    def get_condition(self) -> typing.Optional[BreakpointCondition]: ...
    @classmethod
    def new(cls, condition: BreakpointCondition) -> Breakpoint: ...
    def set_condition(
        self, condition: typing.Optional[BreakpointCondition] = None
    ) -> None: ...

class BreakpointBin(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        BreakpointBin(**properties)
        new() -> Gtk.Widget

    Object AdwBreakpointBin

    Properties from AdwBreakpointBin:
      child -> GtkWidget: child
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        current_breakpoint: typing.Optional[Breakpoint]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        child: typing.Optional[Gtk.Widget] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_breakpoint(self, breakpoint: Breakpoint) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_current_breakpoint(self) -> typing.Optional[Breakpoint]: ...
    @classmethod
    def new(cls) -> BreakpointBin: ...
    def remove_breakpoint(self, breakpoint: Breakpoint) -> None: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...

class BreakpointBinClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BreakpointBinClass()
    """

    parent_class: Gtk.WidgetClass = ...
    padding: list[None] = ...

class BreakpointClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BreakpointClass()
    """

    parent_class: GObject.ObjectClass = ...

class BreakpointCondition(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_and(condition_1:Adw.BreakpointCondition, condition_2:Adw.BreakpointCondition) -> Adw.BreakpointCondition
        new_length(type:Adw.BreakpointConditionLengthType, value:float, unit:Adw.LengthUnit) -> Adw.BreakpointCondition
        new_or(condition_1:Adw.BreakpointCondition, condition_2:Adw.BreakpointCondition) -> Adw.BreakpointCondition
        new_ratio(type:Adw.BreakpointConditionRatioType, width:int, height:int) -> Adw.BreakpointCondition
    """
    def copy(self) -> BreakpointCondition: ...
    def free(self) -> None: ...
    @classmethod
    def new_and(
        cls, condition_1: BreakpointCondition, condition_2: BreakpointCondition
    ) -> BreakpointCondition: ...
    @classmethod
    def new_length(
        cls, type: BreakpointConditionLengthType, value: float, unit: LengthUnit
    ) -> BreakpointCondition: ...
    @classmethod
    def new_or(
        cls, condition_1: BreakpointCondition, condition_2: BreakpointCondition
    ) -> BreakpointCondition: ...
    @classmethod
    def new_ratio(
        cls, type: BreakpointConditionRatioType, width: int, height: int
    ) -> BreakpointCondition: ...
    @staticmethod
    def parse(str: str) -> BreakpointCondition: ...
    def to_string(self) -> str: ...

class ButtonContent(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ButtonContent(**properties)
        new() -> Gtk.Widget

    Object AdwButtonContent

    Properties from AdwButtonContent:
      icon-name -> gchararray: icon-name
      label -> gchararray: label
      use-underline -> gboolean: use-underline
      can-shrink -> gboolean: can-shrink

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        can_shrink: bool
        icon_name: str
        label: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        can_shrink: bool = ...,
        icon_name: str = ...,
        label: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_can_shrink(self) -> bool: ...
    def get_icon_name(self) -> str: ...
    def get_label(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> ButtonContent: ...
    def set_can_shrink(self, can_shrink: bool) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class ButtonContentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ButtonContentClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ButtonRow(
    PreferencesRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        ButtonRow(**properties)
        new() -> Gtk.Widget

    Object AdwButtonRow

    Signals from AdwButtonRow:
      activated ()

    Properties from AdwButtonRow:
      start-icon-name -> gchararray: start-icon-name
      end-icon-name -> gchararray: end-icon-name

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(PreferencesRow.Props):
        end_icon_name: typing.Optional[str]
        start_icon_name: typing.Optional[str]
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    def __init__(
        self,
        end_icon_name: typing.Optional[str] = ...,
        start_icon_name: typing.Optional[str] = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def get_end_icon_name(self) -> typing.Optional[str]: ...
    def get_start_icon_name(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> ButtonRow: ...
    def set_end_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_start_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...

class ButtonRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ButtonRowClass()
    """

    parent_class: PreferencesRowClass = ...

class CallbackAnimationTarget(AnimationTarget):
    """
    :Constructors:

    ::

        CallbackAnimationTarget(**properties)
        new(callback:Adw.AnimationTargetFunc) -> Adw.AnimationTarget

    Object AdwCallbackAnimationTarget

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(
        cls, callback: typing.Callable[..., None], *user_data: typing.Any
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
    """
    :Constructors:

    ::

        Carousel(**properties)
        new() -> Gtk.Widget

    Object AdwCarousel

    Signals from AdwCarousel:
      page-changed (guint)

    Properties from AdwCarousel:
      n-pages -> guint: n-pages
      position -> gdouble: position
      interactive -> gboolean: interactive
      spacing -> guint: spacing
      scroll-params -> AdwSpringParams: scroll-params
      allow-mouse-drag -> gboolean: allow-mouse-drag
      allow-scroll-wheel -> gboolean: allow-scroll-wheel
      allow-long-swipes -> gboolean: allow-long-swipes
      reveal-duration -> guint: reveal-duration

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
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
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
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
    """
    :Constructors:

    ::

        CarouselClass()
    """

    parent_class: Gtk.WidgetClass = ...

class CarouselIndicatorDots(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        CarouselIndicatorDots(**properties)
        new() -> Gtk.Widget

    Object AdwCarouselIndicatorDots

    Properties from AdwCarouselIndicatorDots:
      carousel -> AdwCarousel: carousel

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        carousel: typing.Optional[Carousel]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        carousel: typing.Optional[Carousel] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_carousel(self) -> typing.Optional[Carousel]: ...
    @classmethod
    def new(cls) -> CarouselIndicatorDots: ...
    def set_carousel(self, carousel: typing.Optional[Carousel] = None) -> None: ...

class CarouselIndicatorDotsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CarouselIndicatorDotsClass()
    """

    parent_class: Gtk.WidgetClass = ...

class CarouselIndicatorLines(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        CarouselIndicatorLines(**properties)
        new() -> Gtk.Widget

    Object AdwCarouselIndicatorLines

    Properties from AdwCarouselIndicatorLines:
      carousel -> AdwCarousel: carousel

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        carousel: typing.Optional[Carousel]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        carousel: typing.Optional[Carousel] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_carousel(self) -> typing.Optional[Carousel]: ...
    @classmethod
    def new(cls) -> CarouselIndicatorLines: ...
    def set_carousel(self, carousel: typing.Optional[Carousel] = None) -> None: ...

class CarouselIndicatorLinesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CarouselIndicatorLinesClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Clamp(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        Clamp(**properties)
        new() -> Gtk.Widget

    Object AdwClamp

    Properties from AdwClamp:
      child -> GtkWidget: child
      maximum-size -> gint: maximum-size
      tightening-threshold -> gint: tightening-threshold
      unit -> AdwLengthUnit: unit

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        maximum_size: int
        tightening_threshold: int
        unit: LengthUnit
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        child: typing.Optional[Gtk.Widget] = ...,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        unit: LengthUnit = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    def get_unit(self) -> LengthUnit: ...
    @classmethod
    def new(cls) -> Clamp: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...
    def set_unit(self, unit: LengthUnit) -> None: ...

class ClampClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClampClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ClampLayout(Gtk.LayoutManager, Gtk.Orientable):
    """
    :Constructors:

    ::

        ClampLayout(**properties)
        new() -> Gtk.LayoutManager

    Object AdwClampLayout

    Properties from AdwClampLayout:
      maximum-size -> gint: maximum-size
      tightening-threshold -> gint: tightening-threshold
      unit -> AdwLengthUnit: unit

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.LayoutManager.Props):
        maximum_size: int
        tightening_threshold: int
        unit: LengthUnit
        orientation: Gtk.Orientation

    props: Props = ...
    def __init__(
        self,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        unit: LengthUnit = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    def get_unit(self) -> LengthUnit: ...
    @classmethod
    def new(cls) -> ClampLayout: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...
    def set_unit(self, unit: LengthUnit) -> None: ...

class ClampLayoutClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClampLayoutClass()
    """

    parent_class: Gtk.LayoutManagerClass = ...

class ClampScrollable(
    Gtk.Widget,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
    Gtk.Scrollable,
):
    """
    :Constructors:

    ::

        ClampScrollable(**properties)
        new() -> Gtk.Widget

    Object AdwClampScrollable

    Properties from AdwClampScrollable:
      child -> GtkWidget: child
      maximum-size -> gint: maximum-size
      tightening-threshold -> gint: tightening-threshold
      unit -> AdwLengthUnit: unit

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        maximum_size: int
        tightening_threshold: int
        unit: LengthUnit
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        orientation: Gtk.Orientation
        hadjustment: typing.Optional[Gtk.Adjustment]
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: typing.Optional[Gtk.Adjustment]
        vscroll_policy: Gtk.ScrollablePolicy

    props: Props = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        maximum_size: int = ...,
        tightening_threshold: int = ...,
        unit: LengthUnit = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
        hadjustment: typing.Optional[Gtk.Adjustment] = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: typing.Optional[Gtk.Adjustment] = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    def get_unit(self) -> LengthUnit: ...
    @classmethod
    def new(cls) -> ClampScrollable: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...
    def set_unit(self, unit: LengthUnit) -> None: ...

class ClampScrollableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClampScrollableClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ComboRow(
    ActionRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        ComboRow(**properties)
        new() -> Gtk.Widget

    Object AdwComboRow

    Properties from AdwComboRow:
      selected -> guint: selected
      selected-item -> GObject: selected-item
      model -> GListModel: model
      factory -> GtkListItemFactory: factory
      header-factory -> GtkListItemFactory: header-factory
      list-factory -> GtkListItemFactory: list-factory
      expression -> GtkExpression: Expression
        Expression to determine strings to search for
      use-subtitle -> gboolean: use-subtitle
      enable-search -> gboolean: enable-search
      search-match-mode -> GtkStringFilterMatchMode: search-match-mode

    Signals from AdwActionRow:
      activated ()

    Properties from AdwActionRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      activatable-widget -> GtkWidget: activatable-widget
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines
      subtitle-selectable -> gboolean: subtitle-selectable

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(ActionRow.Props):
        enable_search: bool
        expression: typing.Optional[Gtk.Expression]
        factory: typing.Optional[Gtk.ListItemFactory]
        header_factory: typing.Optional[Gtk.ListItemFactory]
        list_factory: typing.Optional[Gtk.ListItemFactory]
        model: typing.Optional[Gio.ListModel]
        search_match_mode: Gtk.StringFilterMatchMode
        selected: int
        selected_item: typing.Optional[GObject.Object]
        use_subtitle: bool
        activatable_widget: typing.Optional[Gtk.Widget]
        icon_name: typing.Optional[str]
        subtitle: typing.Optional[str]
        subtitle_lines: int
        subtitle_selectable: bool
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    parent_instance: ActionRow = ...
    def __init__(
        self,
        enable_search: bool = ...,
        expression: typing.Optional[Gtk.Expression] = ...,
        factory: typing.Optional[Gtk.ListItemFactory] = ...,
        header_factory: typing.Optional[Gtk.ListItemFactory] = ...,
        list_factory: typing.Optional[Gtk.ListItemFactory] = ...,
        model: typing.Optional[Gio.ListModel] = ...,
        search_match_mode: Gtk.StringFilterMatchMode = ...,
        selected: int = ...,
        use_subtitle: bool = ...,
        activatable_widget: typing.Optional[Gtk.Widget] = ...,
        icon_name: typing.Optional[str] = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        subtitle_selectable: bool = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def get_enable_search(self) -> bool: ...
    def get_expression(self) -> typing.Optional[Gtk.Expression]: ...
    def get_factory(self) -> typing.Optional[Gtk.ListItemFactory]: ...
    def get_header_factory(self) -> typing.Optional[Gtk.ListItemFactory]: ...
    def get_list_factory(self) -> typing.Optional[Gtk.ListItemFactory]: ...
    def get_model(self) -> typing.Optional[Gio.ListModel]: ...
    def get_search_match_mode(self) -> Gtk.StringFilterMatchMode: ...
    def get_selected(self) -> int: ...
    def get_selected_item(self) -> typing.Optional[GObject.Object]: ...
    def get_use_subtitle(self) -> bool: ...
    @classmethod
    def new(cls) -> ComboRow: ...
    def set_enable_search(self, enable_search: bool) -> None: ...
    def set_expression(
        self, expression: typing.Optional[Gtk.Expression] = None
    ) -> None: ...
    def set_factory(
        self, factory: typing.Optional[Gtk.ListItemFactory] = None
    ) -> None: ...
    def set_header_factory(
        self, factory: typing.Optional[Gtk.ListItemFactory] = None
    ) -> None: ...
    def set_list_factory(
        self, factory: typing.Optional[Gtk.ListItemFactory] = None
    ) -> None: ...
    def set_model(self, model: typing.Optional[Gio.ListModel] = None) -> None: ...
    def set_search_match_mode(
        self, search_match_mode: Gtk.StringFilterMatchMode
    ) -> None: ...
    def set_selected(self, position: int) -> None: ...
    def set_use_subtitle(self, use_subtitle: bool) -> None: ...

class ComboRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ComboRowClass()
    """

    parent_class: ActionRowClass = ...
    padding: list[None] = ...

class Dialog(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.ShortcutManager
):
    """
    :Constructors:

    ::

        Dialog(**properties)
        new() -> Adw.Dialog

    Object AdwDialog

    Signals from AdwDialog:
      closed ()
      close-attempt ()

    Properties from AdwDialog:
      child -> GtkWidget: child
      title -> gchararray: title
      can-close -> gboolean: can-close
      content-width -> gint: content-width
      content-height -> gint: content-height
      follows-content-size -> gboolean: follows-content-size
      presentation-mode -> AdwDialogPresentationMode: presentation-mode
      focus-widget -> GtkWidget: focus-widget
      default-widget -> GtkWidget: default-widget
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        can_close: bool
        child: typing.Optional[Gtk.Widget]
        content_height: int
        content_width: int
        current_breakpoint: typing.Optional[Breakpoint]
        default_widget: typing.Optional[Gtk.Widget]
        focus_widget: typing.Optional[Gtk.Widget]
        follows_content_size: bool
        presentation_mode: DialogPresentationMode
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        can_close: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        content_height: int = ...,
        content_width: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        follows_content_size: bool = ...,
        presentation_mode: DialogPresentationMode = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_breakpoint(self, breakpoint: Breakpoint) -> None: ...
    def close(self) -> bool: ...
    def do_close_attempt(self) -> None: ...
    def do_closed(self) -> None: ...
    def force_close(self) -> None: ...
    def get_can_close(self) -> bool: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_content_height(self) -> int: ...
    def get_content_width(self) -> int: ...
    def get_current_breakpoint(self) -> typing.Optional[Breakpoint]: ...
    def get_default_widget(self) -> typing.Optional[Gtk.Widget]: ...
    def get_focus(self) -> typing.Optional[Gtk.Widget]: ...
    def get_follows_content_size(self) -> bool: ...
    def get_presentation_mode(self) -> DialogPresentationMode: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls) -> Dialog: ...
    def present(self, parent: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_can_close(self, can_close: bool) -> None: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_content_height(self, content_height: int) -> None: ...
    def set_content_width(self, content_width: int) -> None: ...
    def set_default_widget(
        self, default_widget: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_focus(self, focus: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_follows_content_size(self, follows_content_size: bool) -> None: ...
    def set_presentation_mode(
        self, presentation_mode: DialogPresentationMode
    ) -> None: ...
    def set_title(self, title: str) -> None: ...

class DialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        DialogClass()
    """

    parent_class: Gtk.WidgetClass = ...
    close_attempt: typing.Callable[[Dialog], None] = ...
    closed: typing.Callable[[Dialog], None] = ...
    padding: list[None] = ...

class EntryRow(
    PreferencesRow,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Editable,
):
    """
    :Constructors:

    ::

        EntryRow(**properties)
        new() -> Gtk.Widget

    Object AdwEntryRow

    Signals from AdwEntryRow:
      apply ()
      entry-activated ()

    Properties from AdwEntryRow:
      show-apply-button -> gboolean: show-apply-button
      input-hints -> GtkInputHints: input-hints
      input-purpose -> GtkInputPurpose: input-purpose
      attributes -> PangoAttrList: attributes
      enable-emoji-completion -> gboolean: enable-emoji-completion
      activates-default -> gboolean: activates-default
      text-length -> guint: text-length
      max-length -> gint: max-length

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(PreferencesRow.Props):
        activates_default: bool
        attributes: typing.Optional[Pango.AttrList]
        enable_emoji_completion: bool
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        max_length: int
        show_apply_button: bool
        text_length: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
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
        attributes: typing.Optional[Pango.AttrList] = ...,
        enable_emoji_completion: bool = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        max_length: int = ...,
        show_apply_button: bool = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, widget: Gtk.Widget) -> None: ...
    def get_activates_default(self) -> bool: ...
    def get_attributes(self) -> typing.Optional[Pango.AttrList]: ...
    def get_enable_emoji_completion(self) -> bool: ...
    def get_input_hints(self) -> Gtk.InputHints: ...
    def get_input_purpose(self) -> Gtk.InputPurpose: ...
    def get_max_length(self) -> int: ...
    def get_show_apply_button(self) -> bool: ...
    def get_text_length(self) -> int: ...
    def grab_focus_without_selecting(self) -> bool: ...
    @classmethod
    def new(cls) -> EntryRow: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_activates_default(self, activates: bool) -> None: ...
    def set_attributes(
        self, attributes: typing.Optional[Pango.AttrList] = None
    ) -> None: ...
    def set_enable_emoji_completion(self, enable_emoji_completion: bool) -> None: ...
    def set_input_hints(self, hints: Gtk.InputHints) -> None: ...
    def set_input_purpose(self, purpose: Gtk.InputPurpose) -> None: ...
    def set_max_length(self, max_length: int) -> None: ...
    def set_show_apply_button(self, show_apply_button: bool) -> None: ...

class EntryRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EntryRowClass()
    """

    parent_class: PreferencesRowClass = ...

class EnumListItem(GObject.Object):
    """
    :Constructors:

    ::

        EnumListItem(**properties)

    Object AdwEnumListItem

    Properties from AdwEnumListItem:
      value -> gint: value
      name -> gchararray: name
      nick -> gchararray: nick

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        name: str
        nick: str
        value: int

    props: Props = ...
    def get_name(self) -> str: ...
    def get_nick(self) -> str: ...
    def get_value(self) -> int: ...

class EnumListItemClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EnumListItemClass()
    """

    parent_class: GObject.ObjectClass = ...

class EnumListModel(GObject.Object, Gio.ListModel):
    """
    :Constructors:

    ::

        EnumListModel(**properties)
        new(enum_type:GType) -> Adw.EnumListModel

    Object AdwEnumListModel

    Properties from AdwEnumListModel:
      enum-type -> GType: enum-type

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        enum_type: typing.Type[typing.Any]

    props: Props = ...
    def __init__(self, enum_type: typing.Type[typing.Any] = ...) -> None: ...
    def find_position(self, value: int) -> int: ...
    def get_enum_type(self) -> typing.Type[typing.Any]: ...
    @classmethod
    def new(cls, enum_type: typing.Type[typing.Any]) -> EnumListModel: ...

class EnumListModelClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EnumListModelClass()
    """

    parent_class: GObject.ObjectClass = ...

class ExpanderRow(
    PreferencesRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        ExpanderRow(**properties)
        new() -> Gtk.Widget

    Object AdwExpanderRow

    Properties from AdwExpanderRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      expanded -> gboolean: expanded
      enable-expansion -> gboolean: enable-expansion
      show-enable-switch -> gboolean: show-enable-switch
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(PreferencesRow.Props):
        enable_expansion: bool
        expanded: bool
        icon_name: typing.Optional[str]
        show_enable_switch: bool
        subtitle: str
        subtitle_lines: int
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    parent_instance: PreferencesRow = ...
    def __init__(
        self,
        enable_expansion: bool = ...,
        expanded: bool = ...,
        icon_name: typing.Optional[str] = ...,
        show_enable_switch: bool = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def add_action(self, widget: Gtk.Widget) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_row(self, child: Gtk.Widget) -> None: ...
    def add_suffix(self, widget: Gtk.Widget) -> None: ...
    def get_enable_expansion(self) -> bool: ...
    def get_expanded(self) -> bool: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_show_enable_switch(self) -> bool: ...
    def get_subtitle(self) -> str: ...
    def get_subtitle_lines(self) -> int: ...
    def get_title_lines(self) -> int: ...
    @classmethod
    def new(cls) -> ExpanderRow: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_enable_expansion(self, enable_expansion: bool) -> None: ...
    def set_expanded(self, expanded: bool) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_show_enable_switch(self, show_enable_switch: bool) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_subtitle_lines(self, subtitle_lines: int) -> None: ...
    def set_title_lines(self, title_lines: int) -> None: ...

class ExpanderRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExpanderRowClass()
    """

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
    """
    :Constructors:

    ::

        Flap(**properties)
        new() -> Gtk.Widget

    Object AdwFlap

    Properties from AdwFlap:
      content -> GtkWidget: content
      flap -> GtkWidget: flap
      separator -> GtkWidget: separator
      flap-position -> GtkPackType: flap-position
      reveal-flap -> gboolean: reveal-flap
      reveal-params -> AdwSpringParams: reveal-params
      reveal-progress -> gdouble: reveal-progress
      fold-policy -> AdwFlapFoldPolicy: fold-policy
      fold-threshold-policy -> AdwFoldThresholdPolicy: fold-threshold-policy
      fold-duration -> guint: fold-duration
      folded -> gboolean: folded
      locked -> gboolean: locked
      transition-type -> AdwFlapTransitionType: transition-type
      modal -> gboolean: modal
      swipe-to-open -> gboolean: swipe-to-open
      swipe-to-close -> gboolean: swipe-to-close

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        content: typing.Optional[Gtk.Widget]
        flap: typing.Optional[Gtk.Widget]
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
        separator: typing.Optional[Gtk.Widget]
        swipe_to_close: bool
        swipe_to_open: bool
        transition_type: FlapTransitionType
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        content: typing.Optional[Gtk.Widget] = ...,
        flap: typing.Optional[Gtk.Widget] = ...,
        flap_position: Gtk.PackType = ...,
        fold_duration: int = ...,
        fold_policy: FlapFoldPolicy = ...,
        fold_threshold_policy: FoldThresholdPolicy = ...,
        locked: bool = ...,
        modal: bool = ...,
        reveal_flap: bool = ...,
        reveal_params: SpringParams = ...,
        separator: typing.Optional[Gtk.Widget] = ...,
        swipe_to_close: bool = ...,
        swipe_to_open: bool = ...,
        transition_type: FlapTransitionType = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_content(self) -> typing.Optional[Gtk.Widget]: ...
    def get_flap(self) -> typing.Optional[Gtk.Widget]: ...
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
    def get_separator(self) -> typing.Optional[Gtk.Widget]: ...
    def get_swipe_to_close(self) -> bool: ...
    def get_swipe_to_open(self) -> bool: ...
    def get_transition_type(self) -> FlapTransitionType: ...
    @classmethod
    def new(cls) -> Flap: ...
    def set_content(self, content: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_flap(self, flap: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_flap_position(self, position: Gtk.PackType) -> None: ...
    def set_fold_duration(self, duration: int) -> None: ...
    def set_fold_policy(self, policy: FlapFoldPolicy) -> None: ...
    def set_fold_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_locked(self, locked: bool) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_reveal_flap(self, reveal_flap: bool) -> None: ...
    def set_reveal_params(self, params: SpringParams) -> None: ...
    def set_separator(self, separator: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_swipe_to_close(self, swipe_to_close: bool) -> None: ...
    def set_swipe_to_open(self, swipe_to_open: bool) -> None: ...
    def set_transition_type(self, transition_type: FlapTransitionType) -> None: ...

class FlapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FlapClass()
    """

    parent_class: Gtk.WidgetClass = ...

class HeaderBar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        HeaderBar(**properties)
        new() -> Gtk.Widget

    Object AdwHeaderBar

    Properties from AdwHeaderBar:
      title-widget -> GtkWidget: title-widget
      show-start-title-buttons -> gboolean: show-start-title-buttons
      show-end-title-buttons -> gboolean: show-end-title-buttons
      show-back-button -> gboolean: show-back-button
      decoration-layout -> gchararray: decoration-layout
      centering-policy -> AdwCenteringPolicy: centering-policy
      show-title -> gboolean: show-title

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        centering_policy: CenteringPolicy
        decoration_layout: typing.Optional[str]
        show_back_button: bool
        show_end_title_buttons: bool
        show_start_title_buttons: bool
        show_title: bool
        title_widget: typing.Optional[Gtk.Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        decoration_layout: typing.Optional[str] = ...,
        show_back_button: bool = ...,
        show_end_title_buttons: bool = ...,
        show_start_title_buttons: bool = ...,
        show_title: bool = ...,
        title_widget: typing.Optional[Gtk.Widget] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_centering_policy(self) -> CenteringPolicy: ...
    def get_decoration_layout(self) -> typing.Optional[str]: ...
    def get_show_back_button(self) -> bool: ...
    def get_show_end_title_buttons(self) -> bool: ...
    def get_show_start_title_buttons(self) -> bool: ...
    def get_show_title(self) -> bool: ...
    def get_title_widget(self) -> typing.Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> HeaderBar: ...
    def pack_end(self, child: Gtk.Widget) -> None: ...
    def pack_start(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_centering_policy(self, centering_policy: CenteringPolicy) -> None: ...
    def set_decoration_layout(self, layout: typing.Optional[str] = None) -> None: ...
    def set_show_back_button(self, show_back_button: bool) -> None: ...
    def set_show_end_title_buttons(self, setting: bool) -> None: ...
    def set_show_start_title_buttons(self, setting: bool) -> None: ...
    def set_show_title(self, show_title: bool) -> None: ...
    def set_title_widget(
        self, title_widget: typing.Optional[Gtk.Widget] = None
    ) -> None: ...

class HeaderBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HeaderBarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class InlineViewSwitcher(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        InlineViewSwitcher(**properties)
        new() -> Gtk.Widget

    Object AdwInlineViewSwitcher

    Properties from AdwInlineViewSwitcher:
      stack -> AdwViewStack: stack
      display-mode -> AdwInlineViewSwitcherDisplayMode: display-mode
      homogeneous -> gboolean: homogeneous
      can-shrink -> gboolean: can-shrink

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        can_shrink: bool
        display_mode: InlineViewSwitcherDisplayMode
        homogeneous: bool
        stack: typing.Optional[ViewStack]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        can_shrink: bool = ...,
        display_mode: InlineViewSwitcherDisplayMode = ...,
        homogeneous: bool = ...,
        stack: typing.Optional[ViewStack] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_can_shrink(self) -> bool: ...
    def get_display_mode(self) -> InlineViewSwitcherDisplayMode: ...
    def get_homogeneous(self) -> bool: ...
    def get_stack(self) -> typing.Optional[ViewStack]: ...
    @classmethod
    def new(cls) -> InlineViewSwitcher: ...
    def set_can_shrink(self, can_shrink: bool) -> None: ...
    def set_display_mode(self, mode: InlineViewSwitcherDisplayMode) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_stack(self, stack: typing.Optional[ViewStack] = None) -> None: ...

class InlineViewSwitcherClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InlineViewSwitcherClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Layout(GObject.Object, Gtk.Buildable):
    """
    :Constructors:

    ::

        Layout(**properties)
        new(content:Gtk.Widget) -> Adw.Layout

    Object AdwLayout

    Properties from AdwLayout:
      content -> GtkWidget: content
      name -> gchararray: name

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        content: Gtk.Widget
        name: typing.Optional[str]

    props: Props = ...
    def __init__(
        self, content: Gtk.Widget = ..., name: typing.Optional[str] = ...
    ) -> None: ...
    def get_content(self) -> Gtk.Widget: ...
    def get_name(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls, content: Gtk.Widget) -> Layout: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...

class LayoutClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LayoutClass()
    """

    parent_class: GObject.ObjectClass = ...

class LayoutSlot(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        LayoutSlot(**properties)
        new(id:str) -> Gtk.Widget

    Object AdwLayoutSlot

    Properties from AdwLayoutSlot:
      id -> gchararray: id

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        id: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        id: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_slot_id(self) -> str: ...
    @classmethod
    def new(cls, id: str) -> LayoutSlot: ...

class LayoutSlotClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LayoutSlotClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Leaflet(
    Gtk.Widget,
    Swipeable,
    Gtk.Accessible,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Orientable,
):
    """
    :Constructors:

    ::

        Leaflet(**properties)
        new() -> Gtk.Widget

    Object AdwLeaflet

    Properties from AdwLeaflet:
      can-unfold -> gboolean: can-unfold
      folded -> gboolean: folded
      fold-threshold-policy -> AdwFoldThresholdPolicy: fold-threshold-policy
      homogeneous -> gboolean: homogeneous
      visible-child -> GtkWidget: visible-child
      visible-child-name -> gchararray: visible-child-name
      transition-type -> AdwLeafletTransitionType: transition-type
      mode-transition-duration -> guint: mode-transition-duration
      child-transition-params -> AdwSpringParams: child-transition-params
      child-transition-running -> gboolean: child-transition-running
      can-navigate-back -> gboolean: can-navigate-back
      can-navigate-forward -> gboolean: can-navigate-forward
      pages -> GtkSelectionModel: pages

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
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
        visible_child: typing.Optional[Gtk.Widget]
        visible_child_name: typing.Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def append(self, child: Gtk.Widget) -> LeafletPage: ...
    def get_adjacent_child(
        self, direction: NavigationDirection
    ) -> typing.Optional[Gtk.Widget]: ...
    def get_can_navigate_back(self) -> bool: ...
    def get_can_navigate_forward(self) -> bool: ...
    def get_can_unfold(self) -> bool: ...
    def get_child_by_name(self, name: str) -> typing.Optional[Gtk.Widget]: ...
    def get_child_transition_params(self) -> SpringParams: ...
    def get_child_transition_running(self) -> bool: ...
    def get_fold_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_folded(self) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_mode_transition_duration(self) -> int: ...
    def get_page(self, child: Gtk.Widget) -> LeafletPage: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_transition_type(self) -> LeafletTransitionType: ...
    def get_visible_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_visible_child_name(self) -> typing.Optional[str]: ...
    def insert_child_after(
        self, child: Gtk.Widget, sibling: typing.Optional[Gtk.Widget] = None
    ) -> LeafletPage: ...
    def navigate(self, direction: NavigationDirection) -> bool: ...
    @classmethod
    def new(cls) -> Leaflet: ...
    def prepend(self, child: Gtk.Widget) -> LeafletPage: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def reorder_child_after(
        self, child: Gtk.Widget, sibling: typing.Optional[Gtk.Widget] = None
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
    """
    :Constructors:

    ::

        LeafletClass()
    """

    parent_class: Gtk.WidgetClass = ...

class LeafletPage(GObject.Object):
    """
    :Constructors:

    ::

        LeafletPage(**properties)

    Object AdwLeafletPage

    Properties from AdwLeafletPage:
      child -> GtkWidget: child
      name -> gchararray: name
      navigatable -> gboolean: navigatable

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        child: Gtk.Widget
        name: typing.Optional[str]
        navigatable: bool

    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        name: typing.Optional[str] = ...,
        navigatable: bool = ...,
    ) -> None: ...
    def get_child(self) -> Gtk.Widget: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_navigatable(self) -> bool: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_navigatable(self, navigatable: bool) -> None: ...

class LeafletPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LeafletPageClass()
    """

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
    """
    :Constructors:

    ::

        MessageDialog(**properties)
        new(parent:Gtk.Window=None, heading:str=None, body:str=None) -> Gtk.Widget

    Object AdwMessageDialog

    Signals from AdwMessageDialog:
      response (gchararray)

    Properties from AdwMessageDialog:
      heading -> gchararray: heading
      heading-use-markup -> gboolean: heading-use-markup
      body -> gchararray: body
      body-use-markup -> gboolean: body-use-markup
      extra-child -> GtkWidget: extra-child
      default-response -> gchararray: default-response
      close-response -> gchararray: close-response

    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Window.Props):
        body: str
        body_use_markup: bool
        close_response: str
        default_response: typing.Optional[str]
        extra_child: typing.Optional[Gtk.Widget]
        heading: typing.Optional[str]
        heading_use_markup: bool
        application: typing.Optional[Gtk.Application]
        child: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: typing.Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: typing.Optional[Gtk.Widget]
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: typing.Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: typing.Optional[str]
        titlebar: typing.Optional[Gtk.Widget]
        transient_for: typing.Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        default_response: typing.Optional[str] = ...,
        extra_child: typing.Optional[Gtk.Widget] = ...,
        heading: typing.Optional[str] = ...,
        heading_use_markup: bool = ...,
        application: typing.Optional[Gtk.Application] = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: typing.Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: typing.Optional[str] = ...,
        titlebar: typing.Optional[Gtk.Widget] = ...,
        transient_for: typing.Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_response(self, id: str, label: str) -> None: ...
    def choose(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def choose_finish(self, result: Gio.AsyncResult) -> str: ...
    def do_response(self, response: str) -> None: ...
    def get_body(self) -> str: ...
    def get_body_use_markup(self) -> bool: ...
    def get_close_response(self) -> str: ...
    def get_default_response(self) -> typing.Optional[str]: ...
    def get_extra_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_heading(self) -> typing.Optional[str]: ...
    def get_heading_use_markup(self) -> bool: ...
    def get_response_appearance(self, response: str) -> ResponseAppearance: ...
    def get_response_enabled(self, response: str) -> bool: ...
    def get_response_label(self, response: str) -> str: ...
    def has_response(self, response: str) -> bool: ...
    @classmethod
    def new(
        cls,
        parent: typing.Optional[Gtk.Window] = None,
        heading: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
    ) -> MessageDialog: ...
    def remove_response(self, id: str) -> None: ...
    def response(self, response: str) -> None: ...
    def set_body(self, body: str) -> None: ...
    def set_body_use_markup(self, use_markup: bool) -> None: ...
    def set_close_response(self, response: str) -> None: ...
    def set_default_response(self, response: typing.Optional[str] = None) -> None: ...
    def set_extra_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_heading(self, heading: typing.Optional[str] = None) -> None: ...
    def set_heading_use_markup(self, use_markup: bool) -> None: ...
    def set_response_appearance(
        self, response: str, appearance: ResponseAppearance
    ) -> None: ...
    def set_response_enabled(self, response: str, enabled: bool) -> None: ...
    def set_response_label(self, response: str, label: str) -> None: ...

class MessageDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MessageDialogClass()
    """

    parent_class: Gtk.WindowClass = ...
    response: typing.Callable[[MessageDialog, str], None] = ...
    padding: list[None] = ...

class MultiLayoutView(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        MultiLayoutView(**properties)
        new() -> Gtk.Widget

    Object AdwMultiLayoutView

    Properties from AdwMultiLayoutView:
      layout -> AdwLayout: layout
      layout-name -> gchararray: layout-name

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        layout: typing.Optional[Layout]
        layout_name: typing.Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        layout: Layout = ...,
        layout_name: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_layout(self, layout: Layout) -> None: ...
    def get_child(self, id: str) -> typing.Optional[Gtk.Widget]: ...
    def get_layout(self) -> typing.Optional[Layout]: ...
    def get_layout_by_name(self, name: str) -> typing.Optional[Layout]: ...
    def get_layout_name(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> MultiLayoutView: ...
    def remove_layout(self, layout: Layout) -> None: ...
    def set_child(self, id: str, child: Gtk.Widget) -> None: ...
    def set_layout(self, layout: Layout) -> None: ...
    def set_layout_name(self, name: str) -> None: ...

class MultiLayoutViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MultiLayoutViewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class NavigationPage(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        NavigationPage(**properties)
        new(child:Gtk.Widget, title:str) -> Adw.NavigationPage
        new_with_tag(child:Gtk.Widget, title:str, tag:str) -> Adw.NavigationPage

    Object AdwNavigationPage

    Signals from AdwNavigationPage:
      showing ()
      shown ()
      hiding ()
      hidden ()

    Properties from AdwNavigationPage:
      child -> GtkWidget: child
      tag -> gchararray: tag
      title -> gchararray: title
      can-pop -> gboolean: can-pop

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        can_pop: bool
        child: typing.Optional[Gtk.Widget]
        tag: typing.Optional[str]
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        can_pop: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        tag: typing.Optional[str] = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def do_hidden(self) -> None: ...
    def do_hiding(self) -> None: ...
    def do_showing(self) -> None: ...
    def do_shown(self) -> None: ...
    def get_can_pop(self) -> bool: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_tag(self) -> typing.Optional[str]: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls, child: Gtk.Widget, title: str) -> NavigationPage: ...
    @classmethod
    def new_with_tag(
        cls, child: Gtk.Widget, title: str, tag: str
    ) -> NavigationPage: ...
    def set_can_pop(self, can_pop: bool) -> None: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_tag(self, tag: typing.Optional[str] = None) -> None: ...
    def set_title(self, title: str) -> None: ...

class NavigationPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NavigationPageClass()
    """

    parent_class: Gtk.WidgetClass = ...
    showing: typing.Callable[[NavigationPage], None] = ...
    shown: typing.Callable[[NavigationPage], None] = ...
    hiding: typing.Callable[[NavigationPage], None] = ...
    hidden: typing.Callable[[NavigationPage], None] = ...
    padding: list[None] = ...

class NavigationSplitView(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        NavigationSplitView(**properties)
        new() -> Gtk.Widget

    Object AdwNavigationSplitView

    Properties from AdwNavigationSplitView:
      sidebar -> AdwNavigationPage: sidebar
      content -> AdwNavigationPage: content
      sidebar-position -> GtkPackType: sidebar-position
      collapsed -> gboolean: collapsed
      show-content -> gboolean: show-content
      min-sidebar-width -> gdouble: min-sidebar-width
      max-sidebar-width -> gdouble: max-sidebar-width
      sidebar-width-fraction -> gdouble: sidebar-width-fraction
      sidebar-width-unit -> AdwLengthUnit: sidebar-width-unit

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        collapsed: bool
        content: typing.Optional[NavigationPage]
        max_sidebar_width: float
        min_sidebar_width: float
        show_content: bool
        sidebar: typing.Optional[NavigationPage]
        sidebar_position: Gtk.PackType
        sidebar_width_fraction: float
        sidebar_width_unit: LengthUnit
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        collapsed: bool = ...,
        content: typing.Optional[NavigationPage] = ...,
        max_sidebar_width: float = ...,
        min_sidebar_width: float = ...,
        show_content: bool = ...,
        sidebar: typing.Optional[NavigationPage] = ...,
        sidebar_position: Gtk.PackType = ...,
        sidebar_width_fraction: float = ...,
        sidebar_width_unit: LengthUnit = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_collapsed(self) -> bool: ...
    def get_content(self) -> typing.Optional[NavigationPage]: ...
    def get_max_sidebar_width(self) -> float: ...
    def get_min_sidebar_width(self) -> float: ...
    def get_show_content(self) -> bool: ...
    def get_sidebar(self) -> typing.Optional[NavigationPage]: ...
    def get_sidebar_position(self) -> Gtk.PackType: ...
    def get_sidebar_width_fraction(self) -> float: ...
    def get_sidebar_width_unit(self) -> LengthUnit: ...
    @classmethod
    def new(cls) -> NavigationSplitView: ...
    def set_collapsed(self, collapsed: bool) -> None: ...
    def set_content(self, content: typing.Optional[NavigationPage] = None) -> None: ...
    def set_max_sidebar_width(self, width: float) -> None: ...
    def set_min_sidebar_width(self, width: float) -> None: ...
    def set_show_content(self, show_content: bool) -> None: ...
    def set_sidebar(self, sidebar: typing.Optional[NavigationPage] = None) -> None: ...
    def set_sidebar_position(self, position: Gtk.PackType) -> None: ...
    def set_sidebar_width_fraction(self, fraction: float) -> None: ...
    def set_sidebar_width_unit(self, unit: LengthUnit) -> None: ...

class NavigationSplitViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NavigationSplitViewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class NavigationView(
    Gtk.Widget, Swipeable, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        NavigationView(**properties)
        new() -> Gtk.Widget

    Object AdwNavigationView

    Signals from AdwNavigationView:
      pushed ()
      popped (AdwNavigationPage)
      replaced ()
      get-next-page () -> AdwNavigationPage

    Properties from AdwNavigationView:
      visible-page -> AdwNavigationPage: visible-page
      visible-page-tag -> gchararray: visible-page-tag
      hhomogeneous -> gboolean: hhomogeneous
      vhomogeneous -> gboolean: vhomogeneous
      animate-transitions -> gboolean: animate-transitions
      pop-on-escape -> gboolean: pop-on-escape
      navigation-stack -> GListModel: navigation-stack

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        animate_transitions: bool
        hhomogeneous: bool
        navigation_stack: Gio.ListModel
        pop_on_escape: bool
        vhomogeneous: bool
        visible_page: typing.Optional[NavigationPage]
        visible_page_tag: typing.Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        animate_transitions: bool = ...,
        hhomogeneous: bool = ...,
        pop_on_escape: bool = ...,
        vhomogeneous: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add(self, page: NavigationPage) -> None: ...
    def find_page(self, tag: str) -> typing.Optional[NavigationPage]: ...
    def get_animate_transitions(self) -> bool: ...
    def get_hhomogeneous(self) -> bool: ...
    def get_navigation_stack(self) -> Gio.ListModel: ...
    def get_pop_on_escape(self) -> bool: ...
    def get_previous_page(
        self, page: NavigationPage
    ) -> typing.Optional[NavigationPage]: ...
    def get_vhomogeneous(self) -> bool: ...
    def get_visible_page(self) -> typing.Optional[NavigationPage]: ...
    def get_visible_page_tag(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> NavigationView: ...
    def pop(self) -> bool: ...
    def pop_to_page(self, page: NavigationPage) -> bool: ...
    def pop_to_tag(self, tag: str) -> bool: ...
    def push(self, page: NavigationPage) -> None: ...
    def push_by_tag(self, tag: str) -> None: ...
    def remove(self, page: NavigationPage) -> None: ...
    def replace(self, pages: typing.Sequence[NavigationPage]) -> None: ...
    def replace_with_tags(self, tags: typing.Sequence[str]) -> None: ...
    def set_animate_transitions(self, animate_transitions: bool) -> None: ...
    def set_hhomogeneous(self, hhomogeneous: bool) -> None: ...
    def set_pop_on_escape(self, pop_on_escape: bool) -> None: ...
    def set_vhomogeneous(self, vhomogeneous: bool) -> None: ...

class NavigationViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NavigationViewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class OverlaySplitView(
    Gtk.Widget, Swipeable, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        OverlaySplitView(**properties)
        new() -> Gtk.Widget

    Object AdwOverlaySplitView

    Properties from AdwOverlaySplitView:
      content -> GtkWidget: content
      sidebar -> GtkWidget: sidebar
      sidebar-position -> GtkPackType: sidebar-position
      show-sidebar -> gboolean: show-sidebar
      collapsed -> gboolean: collapsed
      pin-sidebar -> gboolean: pin-sidebar
      enable-show-gesture -> gboolean: enable-show-gesture
      enable-hide-gesture -> gboolean: enable-hide-gesture
      min-sidebar-width -> gdouble: min-sidebar-width
      max-sidebar-width -> gdouble: max-sidebar-width
      sidebar-width-fraction -> gdouble: sidebar-width-fraction
      sidebar-width-unit -> AdwLengthUnit: sidebar-width-unit

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        collapsed: bool
        content: typing.Optional[Gtk.Widget]
        enable_hide_gesture: bool
        enable_show_gesture: bool
        max_sidebar_width: float
        min_sidebar_width: float
        pin_sidebar: bool
        show_sidebar: bool
        sidebar: typing.Optional[Gtk.Widget]
        sidebar_position: Gtk.PackType
        sidebar_width_fraction: float
        sidebar_width_unit: LengthUnit
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        collapsed: bool = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        enable_hide_gesture: bool = ...,
        enable_show_gesture: bool = ...,
        max_sidebar_width: float = ...,
        min_sidebar_width: float = ...,
        pin_sidebar: bool = ...,
        show_sidebar: bool = ...,
        sidebar: typing.Optional[Gtk.Widget] = ...,
        sidebar_position: Gtk.PackType = ...,
        sidebar_width_fraction: float = ...,
        sidebar_width_unit: LengthUnit = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_collapsed(self) -> bool: ...
    def get_content(self) -> typing.Optional[Gtk.Widget]: ...
    def get_enable_hide_gesture(self) -> bool: ...
    def get_enable_show_gesture(self) -> bool: ...
    def get_max_sidebar_width(self) -> float: ...
    def get_min_sidebar_width(self) -> float: ...
    def get_pin_sidebar(self) -> bool: ...
    def get_show_sidebar(self) -> bool: ...
    def get_sidebar(self) -> typing.Optional[Gtk.Widget]: ...
    def get_sidebar_position(self) -> Gtk.PackType: ...
    def get_sidebar_width_fraction(self) -> float: ...
    def get_sidebar_width_unit(self) -> LengthUnit: ...
    @classmethod
    def new(cls) -> OverlaySplitView: ...
    def set_collapsed(self, collapsed: bool) -> None: ...
    def set_content(self, content: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_enable_hide_gesture(self, enable_hide_gesture: bool) -> None: ...
    def set_enable_show_gesture(self, enable_show_gesture: bool) -> None: ...
    def set_max_sidebar_width(self, width: float) -> None: ...
    def set_min_sidebar_width(self, width: float) -> None: ...
    def set_pin_sidebar(self, pin_sidebar: bool) -> None: ...
    def set_show_sidebar(self, show_sidebar: bool) -> None: ...
    def set_sidebar(self, sidebar: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_sidebar_position(self, position: Gtk.PackType) -> None: ...
    def set_sidebar_width_fraction(self, fraction: float) -> None: ...
    def set_sidebar_width_unit(self, unit: LengthUnit) -> None: ...

class OverlaySplitViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OverlaySplitViewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class PasswordEntryRow(
    EntryRow,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Editable,
):
    """
    :Constructors:

    ::

        PasswordEntryRow(**properties)
        new() -> Gtk.Widget

    Object AdwPasswordEntryRow

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from AdwEntryRow:
      apply ()
      entry-activated ()

    Properties from AdwEntryRow:
      show-apply-button -> gboolean: show-apply-button
      input-hints -> GtkInputHints: input-hints
      input-purpose -> GtkInputPurpose: input-purpose
      attributes -> PangoAttrList: attributes
      enable-emoji-completion -> gboolean: enable-emoji-completion
      activates-default -> gboolean: activates-default
      text-length -> guint: text-length
      max-length -> gint: max-length

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(EntryRow.Props):
        activates_default: bool
        attributes: typing.Optional[Pango.AttrList]
        enable_emoji_completion: bool
        input_hints: Gtk.InputHints
        input_purpose: Gtk.InputPurpose
        max_length: int
        show_apply_button: bool
        text_length: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
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
        attributes: typing.Optional[Pango.AttrList] = ...,
        enable_emoji_completion: bool = ...,
        input_hints: Gtk.InputHints = ...,
        input_purpose: Gtk.InputPurpose = ...,
        max_length: int = ...,
        show_apply_button: bool = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> PasswordEntryRow: ...

class PasswordEntryRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordEntryRowClass()
    """

    parent_class: EntryRowClass = ...

class PreferencesDialog(
    Dialog, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.ShortcutManager
):
    """
    :Constructors:

    ::

        PreferencesDialog(**properties)
        new() -> Adw.Dialog

    Object AdwPreferencesDialog

    Properties from AdwPreferencesDialog:
      visible-page -> GtkWidget: visible-page
      visible-page-name -> gchararray: visible-page-name
      search-enabled -> gboolean: search-enabled

    Signals from AdwDialog:
      closed ()
      close-attempt ()

    Properties from AdwDialog:
      child -> GtkWidget: child
      title -> gchararray: title
      can-close -> gboolean: can-close
      content-width -> gint: content-width
      content-height -> gint: content-height
      follows-content-size -> gboolean: follows-content-size
      presentation-mode -> AdwDialogPresentationMode: presentation-mode
      focus-widget -> GtkWidget: focus-widget
      default-widget -> GtkWidget: default-widget
      current-breakpoint -> AdwBreakpoint: current-breakpoint

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Dialog.Props):
        search_enabled: bool
        visible_page: typing.Optional[Gtk.Widget]
        visible_page_name: typing.Optional[str]
        can_close: bool
        child: typing.Optional[Gtk.Widget]
        content_height: int
        content_width: int
        current_breakpoint: typing.Optional[Breakpoint]
        default_widget: typing.Optional[Gtk.Widget]
        focus_widget: typing.Optional[Gtk.Widget]
        follows_content_size: bool
        presentation_mode: DialogPresentationMode
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    parent_instance: Dialog = ...
    def __init__(
        self,
        search_enabled: bool = ...,
        visible_page: Gtk.Widget = ...,
        visible_page_name: str = ...,
        can_close: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        content_height: int = ...,
        content_width: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        follows_content_size: bool = ...,
        presentation_mode: DialogPresentationMode = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add(self, page: PreferencesPage) -> None: ...
    def add_toast(self, toast: Toast) -> None: ...
    def get_search_enabled(self) -> bool: ...
    def get_visible_page(self) -> typing.Optional[PreferencesPage]: ...
    def get_visible_page_name(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> PreferencesDialog: ...
    def pop_subpage(self) -> bool: ...
    def push_subpage(self, page: NavigationPage) -> None: ...
    def remove(self, page: PreferencesPage) -> None: ...
    def set_search_enabled(self, search_enabled: bool) -> None: ...
    def set_visible_page(self, page: PreferencesPage) -> None: ...
    def set_visible_page_name(self, name: str) -> None: ...

class PreferencesDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesDialogClass()
    """

    parent_class: DialogClass = ...
    padding: list[None] = ...

class PreferencesGroup(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        PreferencesGroup(**properties)
        new() -> Gtk.Widget

    Object AdwPreferencesGroup

    Properties from AdwPreferencesGroup:
      title -> gchararray: title
      description -> gchararray: description
      header-suffix -> GtkWidget: header-suffix
      separate-rows -> gboolean: separate-rows

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        description: typing.Optional[str]
        header_suffix: typing.Optional[Gtk.Widget]
        separate_rows: bool
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        description: typing.Optional[str] = ...,
        header_suffix: typing.Optional[Gtk.Widget] = ...,
        separate_rows: bool = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add(self, child: Gtk.Widget) -> None: ...
    def get_description(self) -> typing.Optional[str]: ...
    def get_header_suffix(self) -> typing.Optional[Gtk.Widget]: ...
    def get_separate_rows(self) -> bool: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls) -> PreferencesGroup: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_description(self, description: typing.Optional[str] = None) -> None: ...
    def set_header_suffix(self, suffix: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_separate_rows(self, separate_rows: bool) -> None: ...
    def set_title(self, title: str) -> None: ...

class PreferencesGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesGroupClass()
    """

    parent_class: Gtk.WidgetClass = ...
    padding: list[None] = ...

class PreferencesPage(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        PreferencesPage(**properties)
        new() -> Gtk.Widget

    Object AdwPreferencesPage

    Properties from AdwPreferencesPage:
      icon-name -> gchararray: icon-name
      title -> gchararray: title
      description -> gchararray: description
      name -> gchararray: name
      use-underline -> gboolean: use-underline
      description-centered -> gboolean: description-centered
      banner -> AdwBanner: banner

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        banner: typing.Optional[Banner]
        description: str
        description_centered: bool
        icon_name: typing.Optional[str]
        name: typing.Optional[str]
        title: str
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        banner: typing.Optional[Banner] = ...,
        description: str = ...,
        description_centered: bool = ...,
        icon_name: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        title: str = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add(self, group: PreferencesGroup) -> None: ...
    def get_banner(self) -> typing.Optional[Banner]: ...
    def get_description(self) -> str: ...
    def get_description_centered(self) -> bool: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_title(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> PreferencesPage: ...
    def remove(self, group: PreferencesGroup) -> None: ...
    def scroll_to_top(self) -> None: ...
    def set_banner(self, banner: typing.Optional[Banner] = None) -> None: ...
    def set_description(self, description: str) -> None: ...
    def set_description_centered(self, centered: bool) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class PreferencesPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesPageClass()
    """

    parent_class: Gtk.WidgetClass = ...
    padding: list[None] = ...

class PreferencesRow(
    Gtk.ListBoxRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        PreferencesRow(**properties)
        new() -> Gtk.Widget

    Object AdwPreferencesRow

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.ListBoxRow.Props):
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
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
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
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
    """
    :Constructors:

    ::

        PreferencesRowClass()
    """

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
    """
    :Constructors:

    ::

        PreferencesWindow(**properties)
        new() -> Gtk.Widget

    Object AdwPreferencesWindow

    Properties from AdwPreferencesWindow:
      visible-page -> GtkWidget: visible-page
      visible-page-name -> gchararray: visible-page-name
      search-enabled -> gboolean: search-enabled
      can-navigate-back -> gboolean: can-navigate-back

    Properties from AdwWindow:
      content -> GtkWidget: content
      current-breakpoint -> AdwBreakpoint: current-breakpoint
      dialogs -> GListModel: dialogs
      visible-dialog -> AdwDialog: visible-dialog
      adaptive-preview -> gboolean: adaptive-preview

    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Window.Props):
        can_navigate_back: bool
        search_enabled: bool
        visible_page: typing.Optional[Gtk.Widget]
        visible_page_name: typing.Optional[str]
        adaptive_preview: bool
        content: typing.Optional[Gtk.Widget]
        current_breakpoint: typing.Optional[Breakpoint]
        dialogs: Gio.ListModel
        visible_dialog: typing.Optional[Dialog]
        application: typing.Optional[Gtk.Application]
        child: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: typing.Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: typing.Optional[Gtk.Widget]
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: typing.Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: typing.Optional[str]
        titlebar: typing.Optional[Gtk.Widget]
        transient_for: typing.Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        adaptive_preview: bool = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        application: typing.Optional[Gtk.Application] = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: typing.Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: typing.Optional[str] = ...,
        titlebar: typing.Optional[Gtk.Widget] = ...,
        transient_for: typing.Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add(self, page: PreferencesPage) -> None: ...
    def add_toast(self, toast: Toast) -> None: ...
    def close_subpage(self) -> None: ...
    def get_can_navigate_back(self) -> bool: ...
    def get_search_enabled(self) -> bool: ...
    def get_visible_page(self) -> typing.Optional[PreferencesPage]: ...
    def get_visible_page_name(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> PreferencesWindow: ...
    def pop_subpage(self) -> bool: ...
    def present_subpage(self, subpage: Gtk.Widget) -> None: ...
    def push_subpage(self, page: NavigationPage) -> None: ...
    def remove(self, page: PreferencesPage) -> None: ...
    def set_can_navigate_back(self, can_navigate_back: bool) -> None: ...
    def set_search_enabled(self, search_enabled: bool) -> None: ...
    def set_visible_page(self, page: PreferencesPage) -> None: ...
    def set_visible_page_name(self, name: str) -> None: ...

class PreferencesWindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PreferencesWindowClass()
    """

    parent_class: WindowClass = ...
    padding: list[None] = ...

class PropertyAnimationTarget(AnimationTarget):
    """
    :Constructors:

    ::

        PropertyAnimationTarget(**properties)
        new(object:GObject.Object, property_name:str) -> Adw.AnimationTarget
        new_for_pspec(object:GObject.Object, pspec:GObject.ParamSpec) -> Adw.AnimationTarget

    Object AdwPropertyAnimationTarget

    Properties from AdwPropertyAnimationTarget:
      object -> GObject: object
      pspec -> GParam: pspec

    Signals from GObject:
      notify (GParam)
    """
    class Props(AnimationTarget.Props):
        object: GObject.Object
        pspec: GObject.ParamSpec

    props: Props = ...
    def __init__(
        self, object: GObject.Object = ..., pspec: GObject.ParamSpec = ...
    ) -> None: ...
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

class SpinRow(
    ActionRow,
    Gtk.Accessible,
    Gtk.Actionable,
    Gtk.Buildable,
    Gtk.ConstraintTarget,
    Gtk.Editable,
):
    """
    :Constructors:

    ::

        SpinRow(**properties)
        new(adjustment:Gtk.Adjustment=None, climb_rate:float, digits:int) -> Gtk.Widget
        new_with_range(min:float, max:float, step:float) -> Gtk.Widget

    Object AdwSpinRow

    Signals from AdwSpinRow:
      input (gpointer) -> gint
      output () -> gboolean
      wrapped ()

    Properties from AdwSpinRow:
      adjustment -> GtkAdjustment: adjustment
      climb-rate -> gdouble: climb-rate
      digits -> guint: digits
      numeric -> gboolean: numeric
      snap-to-ticks -> gboolean: snap-to-ticks
      update-policy -> GtkSpinButtonUpdatePolicy: update-policy
      value -> gdouble: value
      wrap -> gboolean: wrap

    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)

    Signals from AdwActionRow:
      activated ()

    Properties from AdwActionRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      activatable-widget -> GtkWidget: activatable-widget
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines
      subtitle-selectable -> gboolean: subtitle-selectable

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(ActionRow.Props):
        adjustment: Gtk.Adjustment
        climb_rate: float
        digits: int
        numeric: bool
        snap_to_ticks: bool
        update_policy: Gtk.SpinButtonUpdatePolicy
        value: float
        wrap: bool
        activatable_widget: typing.Optional[Gtk.Widget]
        icon_name: typing.Optional[str]
        subtitle: typing.Optional[str]
        subtitle_lines: int
        subtitle_selectable: bool
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
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
        adjustment: typing.Optional[Gtk.Adjustment] = ...,
        climb_rate: float = ...,
        digits: int = ...,
        numeric: bool = ...,
        snap_to_ticks: bool = ...,
        update_policy: Gtk.SpinButtonUpdatePolicy = ...,
        value: float = ...,
        wrap: bool = ...,
        activatable_widget: typing.Optional[Gtk.Widget] = ...,
        icon_name: typing.Optional[str] = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        subtitle_selectable: bool = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
        editable: bool = ...,
        enable_undo: bool = ...,
        max_width_chars: int = ...,
        text: str = ...,
        width_chars: int = ...,
        xalign: float = ...,
    ) -> None: ...
    def configure(
        self,
        adjustment: typing.Optional[Gtk.Adjustment],
        climb_rate: float,
        digits: int,
    ) -> None: ...
    def get_adjustment(self) -> Gtk.Adjustment: ...
    def get_climb_rate(self) -> float: ...
    def get_digits(self) -> int: ...
    def get_numeric(self) -> bool: ...
    def get_snap_to_ticks(self) -> bool: ...
    def get_update_policy(self) -> Gtk.SpinButtonUpdatePolicy: ...
    def get_value(self) -> float: ...
    def get_wrap(self) -> bool: ...
    @classmethod
    def new(
        cls, adjustment: typing.Optional[Gtk.Adjustment], climb_rate: float, digits: int
    ) -> SpinRow: ...
    @classmethod
    def new_with_range(cls, min: float, max: float, step: float) -> SpinRow: ...
    def set_adjustment(
        self, adjustment: typing.Optional[Gtk.Adjustment] = None
    ) -> None: ...
    def set_climb_rate(self, climb_rate: float) -> None: ...
    def set_digits(self, digits: int) -> None: ...
    def set_numeric(self, numeric: bool) -> None: ...
    def set_range(self, min: float, max: float) -> None: ...
    def set_snap_to_ticks(self, snap_to_ticks: bool) -> None: ...
    def set_update_policy(self, policy: Gtk.SpinButtonUpdatePolicy) -> None: ...
    def set_value(self, value: float) -> None: ...
    def set_wrap(self, wrap: bool) -> None: ...
    def update(self) -> None: ...

class SpinRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpinRowClass()
    """

    parent_class: ActionRowClass = ...

class Spinner(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        Spinner(**properties)
        new() -> Gtk.Widget

    Object AdwSpinner

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    @classmethod
    def new(cls) -> Spinner: ...

class SpinnerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpinnerClass()
    """

    parent_class: Gtk.WidgetClass = ...

class SpinnerPaintable(GObject.Object, Gdk.Paintable, Gtk.SymbolicPaintable):
    """
    :Constructors:

    ::

        SpinnerPaintable(**properties)
        new(widget:Gtk.Widget=None) -> Adw.SpinnerPaintable

    Object AdwSpinnerPaintable

    Properties from AdwSpinnerPaintable:
      widget -> GtkWidget: widget

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        widget: typing.Optional[Gtk.Widget]

    props: Props = ...
    def __init__(self, widget: typing.Optional[Gtk.Widget] = ...) -> None: ...
    def get_widget(self) -> typing.Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls, widget: typing.Optional[Gtk.Widget] = None) -> SpinnerPaintable: ...
    def set_widget(self, widget: typing.Optional[Gtk.Widget] = None) -> None: ...

class SpinnerPaintableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SpinnerPaintableClass()
    """

    parent_class: GObject.ObjectClass = ...

class SplitButton(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        SplitButton(**properties)
        new() -> Gtk.Widget

    Object AdwSplitButton

    Signals from AdwSplitButton:
      activate ()
      clicked ()

    Properties from AdwSplitButton:
      label -> gchararray: label
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
      can-shrink -> gboolean: can-shrink
      menu-model -> GMenuModel: menu-model
      popover -> GtkPopover: popover
      direction -> GtkArrowType: direction
      dropdown-tooltip -> gchararray: dropdown-tooltip

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        can_shrink: bool
        child: typing.Optional[Gtk.Widget]
        direction: Gtk.ArrowType
        dropdown_tooltip: str
        icon_name: typing.Optional[str]
        label: typing.Optional[str]
        menu_model: typing.Optional[Gio.MenuModel]
        popover: typing.Optional[Gtk.Popover]
        use_underline: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    def __init__(
        self,
        can_shrink: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        direction: Gtk.ArrowType = ...,
        dropdown_tooltip: str = ...,
        icon_name: str = ...,
        label: str = ...,
        menu_model: typing.Optional[Gio.MenuModel] = ...,
        popover: typing.Optional[Gtk.Popover] = ...,
        use_underline: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def get_can_shrink(self) -> bool: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_direction(self) -> Gtk.ArrowType: ...
    def get_dropdown_tooltip(self) -> str: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_label(self) -> typing.Optional[str]: ...
    def get_menu_model(self) -> typing.Optional[Gio.MenuModel]: ...
    def get_popover(self) -> typing.Optional[Gtk.Popover]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> SplitButton: ...
    def popdown(self) -> None: ...
    def popup(self) -> None: ...
    def set_can_shrink(self, can_shrink: bool) -> None: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_direction(self, direction: Gtk.ArrowType) -> None: ...
    def set_dropdown_tooltip(self, tooltip: str) -> None: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_menu_model(
        self, menu_model: typing.Optional[Gio.MenuModel] = None
    ) -> None: ...
    def set_popover(self, popover: typing.Optional[Gtk.Popover] = None) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class SplitButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SplitButtonClass()
    """

    parent_class: Gtk.WidgetClass = ...

class SpringAnimation(Animation):
    """
    :Constructors:

    ::

        SpringAnimation(**properties)
        new(widget:Gtk.Widget, from_:float, to:float, spring_params:Adw.SpringParams, target:Adw.AnimationTarget) -> Adw.Animation

    Object AdwSpringAnimation

    Properties from AdwSpringAnimation:
      value-from -> gdouble: value-from
      value-to -> gdouble: value-to
      spring-params -> AdwSpringParams: spring-params
      initial-velocity -> gdouble: initial-velocity
      epsilon -> gdouble: epsilon
      clamp -> gboolean: clamp
      estimated-duration -> guint: estimated-duration
      velocity -> gdouble: velocity

    Signals from AdwAnimation:
      done ()

    Properties from AdwAnimation:
      widget -> GtkWidget: widget
      target -> AdwAnimationTarget: target
      value -> gdouble: value
      state -> AdwAnimationState: state
      follow-enable-animations-setting -> gboolean: follow-enable-animations-setting

    Signals from GObject:
      notify (GParam)
    """
    class Props(Animation.Props):
        clamp: bool
        epsilon: float
        estimated_duration: int
        initial_velocity: float
        spring_params: SpringParams
        value_from: float
        value_to: float
        velocity: float
        follow_enable_animations_setting: bool
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
        follow_enable_animations_setting: bool = ...,
        target: AnimationTarget = ...,
        widget: Gtk.Widget = ...,
    ) -> None: ...
    def calculate_value(self, time: int) -> float: ...
    def calculate_velocity(self, time: int) -> float: ...
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
    """
    :Constructors:

    ::

        new(damping_ratio:float, mass:float, stiffness:float) -> Adw.SpringParams
        new_full(damping:float, mass:float, stiffness:float) -> Adw.SpringParams
    """
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
    """
    :Constructors:

    ::

        Squeezer(**properties)
        new() -> Gtk.Widget

    Object AdwSqueezer

    Properties from AdwSqueezer:
      visible-child -> GtkWidget: visible-child
      homogeneous -> gboolean: homogeneous
      switch-threshold-policy -> AdwFoldThresholdPolicy: switch-threshold-policy
      allow-none -> gboolean: allow-none
      transition-duration -> guint: transition-duration
      transition-type -> AdwSqueezerTransitionType: transition-type
      transition-running -> gboolean: transition-running
      interpolate-size -> gboolean: interpolate-size
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      pages -> GtkSelectionModel: pages

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        allow_none: bool
        homogeneous: bool
        interpolate_size: bool
        pages: Gtk.SelectionModel
        switch_threshold_policy: FoldThresholdPolicy
        transition_duration: int
        transition_running: bool
        transition_type: SqueezerTransitionType
        visible_child: typing.Optional[Gtk.Widget]
        xalign: float
        yalign: float
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
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
    def get_visible_child(self) -> typing.Optional[Gtk.Widget]: ...
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
    """
    :Constructors:

    ::

        SqueezerClass()
    """

    parent_class: Gtk.WidgetClass = ...

class SqueezerPage(GObject.Object):
    """
    :Constructors:

    ::

        SqueezerPage(**properties)

    Object AdwSqueezerPage

    Properties from AdwSqueezerPage:
      child -> GtkWidget: child
      enabled -> gboolean: enabled

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        child: Gtk.Widget
        enabled: bool

    props: Props = ...
    def __init__(self, child: Gtk.Widget = ..., enabled: bool = ...) -> None: ...
    def get_child(self) -> Gtk.Widget: ...
    def get_enabled(self) -> bool: ...
    def set_enabled(self, enabled: bool) -> None: ...

class SqueezerPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SqueezerPageClass()
    """

    parent_class: GObject.ObjectClass = ...

class StatusPage(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        StatusPage(**properties)
        new() -> Gtk.Widget

    Object AdwStatusPage

    Properties from AdwStatusPage:
      icon-name -> gchararray: icon-name
      paintable -> GdkPaintable: paintable
      title -> gchararray: title
      description -> gchararray: description
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        description: typing.Optional[str]
        icon_name: typing.Optional[str]
        paintable: typing.Optional[Gdk.Paintable]
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        description: typing.Optional[str] = ...,
        icon_name: typing.Optional[str] = ...,
        paintable: typing.Optional[Gdk.Paintable] = ...,
        title: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_description(self) -> typing.Optional[str]: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_paintable(self) -> typing.Optional[Gdk.Paintable]: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls) -> StatusPage: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_description(self, description: typing.Optional[str] = None) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_paintable(
        self, paintable: typing.Optional[Gdk.Paintable] = None
    ) -> None: ...
    def set_title(self, title: str) -> None: ...

class StatusPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StatusPageClass()
    """

    parent_class: Gtk.WidgetClass = ...

class StyleManager(GObject.Object):
    """
    :Constructors:

    ::

        StyleManager(**properties)

    Object AdwStyleManager

    Properties from AdwStyleManager:
      display -> GdkDisplay: display
      color-scheme -> AdwColorScheme: color-scheme
      system-supports-color-schemes -> gboolean: system-supports-color-schemes
      dark -> gboolean: dark
      high-contrast -> gboolean: high-contrast
      system-supports-accent-colors -> gboolean: system-supports-accent-colors
      accent-color -> AdwAccentColor: accent-color
      accent-color-rgba -> GdkRGBA: accent-color-rgba
      document-font-name -> gchararray: document-font-name
      monospace-font-name -> gchararray: monospace-font-name

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        accent_color: AccentColor
        accent_color_rgba: Gdk.RGBA
        color_scheme: ColorScheme
        dark: bool
        display: typing.Optional[Gdk.Display]
        document_font_name: str
        high_contrast: bool
        monospace_font_name: str
        system_supports_accent_colors: bool
        system_supports_color_schemes: bool

    props: Props = ...
    def __init__(
        self, color_scheme: ColorScheme = ..., display: Gdk.Display = ...
    ) -> None: ...
    def get_accent_color(self) -> AccentColor: ...
    def get_accent_color_rgba(self) -> Gdk.RGBA: ...
    def get_color_scheme(self) -> ColorScheme: ...
    def get_dark(self) -> bool: ...
    @staticmethod
    def get_default() -> StyleManager: ...
    def get_display(self) -> typing.Optional[Gdk.Display]: ...
    def get_document_font_name(self) -> str: ...
    @staticmethod
    def get_for_display(display: Gdk.Display) -> StyleManager: ...
    def get_high_contrast(self) -> bool: ...
    def get_monospace_font_name(self) -> str: ...
    def get_system_supports_accent_colors(self) -> bool: ...
    def get_system_supports_color_schemes(self) -> bool: ...
    def set_color_scheme(self, color_scheme: ColorScheme) -> None: ...

class StyleManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StyleManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class SwipeTracker(GObject.Object, Gtk.Orientable):
    """
    :Constructors:

    ::

        SwipeTracker(**properties)
        new(swipeable:Adw.Swipeable) -> Adw.SwipeTracker

    Object AdwSwipeTracker

    Signals from AdwSwipeTracker:
      prepare (AdwNavigationDirection)
      begin-swipe ()
      update-swipe (gdouble)
      end-swipe (gdouble, gdouble)

    Properties from AdwSwipeTracker:
      swipeable -> AdwSwipeable: swipeable
      enabled -> gboolean: enabled
      reversed -> gboolean: reversed
      allow-mouse-drag -> gboolean: allow-mouse-drag
      allow-long-swipes -> gboolean: allow-long-swipes
      lower-overshoot -> gboolean: lower-overshoot
      upper-overshoot -> gboolean: upper-overshoot
      allow-window-handle -> gboolean: allow-window-handle

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        allow_long_swipes: bool
        allow_mouse_drag: bool
        allow_window_handle: bool
        enabled: bool
        lower_overshoot: bool
        reversed: bool
        swipeable: Swipeable
        upper_overshoot: bool
        orientation: Gtk.Orientation

    props: Props = ...
    def __init__(
        self,
        allow_long_swipes: bool = ...,
        allow_mouse_drag: bool = ...,
        allow_window_handle: bool = ...,
        enabled: bool = ...,
        lower_overshoot: bool = ...,
        reversed: bool = ...,
        swipeable: Swipeable = ...,
        upper_overshoot: bool = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_allow_window_handle(self) -> bool: ...
    def get_enabled(self) -> bool: ...
    def get_lower_overshoot(self) -> bool: ...
    def get_reversed(self) -> bool: ...
    def get_swipeable(self) -> Swipeable: ...
    def get_upper_overshoot(self) -> bool: ...
    @classmethod
    def new(cls, swipeable: Swipeable) -> SwipeTracker: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_allow_window_handle(self, allow_window_handle: bool) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_lower_overshoot(self, overshoot: bool) -> None: ...
    def set_reversed(self, reversed: bool) -> None: ...
    def set_upper_overshoot(self, overshoot: bool) -> None: ...
    def shift_position(self, delta: float) -> None: ...

class SwipeTrackerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SwipeTrackerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Swipeable(GObject.GInterface):
    """
    Interface AdwSwipeable

    Signals from GObject:
      notify (GParam)
    """
    def get_cancel_progress(self) -> float: ...
    def get_distance(self) -> float: ...
    def get_progress(self) -> float: ...
    def get_snap_points(self) -> list[float]: ...
    def get_swipe_area(
        self, navigation_direction: NavigationDirection, is_drag: bool
    ) -> Gdk.Rectangle: ...

class SwipeableInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        SwipeableInterface()
    """

    parent: GObject.TypeInterface = ...
    get_distance: typing.Callable[[Swipeable], float] = ...
    get_snap_points: typing.Callable[[Swipeable], list[float]] = ...
    get_progress: typing.Callable[[Swipeable], float] = ...
    get_cancel_progress: typing.Callable[[Swipeable], float] = ...
    get_swipe_area: typing.Callable[
        [Swipeable, NavigationDirection, bool], Gdk.Rectangle
    ] = ...
    padding: list[None] = ...

class SwitchRow(
    ActionRow, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        SwitchRow(**properties)
        new() -> Gtk.Widget

    Object AdwSwitchRow

    Properties from AdwSwitchRow:
      active -> gboolean: active

    Signals from AdwActionRow:
      activated ()

    Properties from AdwActionRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      activatable-widget -> GtkWidget: activatable-widget
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines
      subtitle-selectable -> gboolean: subtitle-selectable

    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup

    Signals from GtkListBoxRow:
      activate ()

    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(ActionRow.Props):
        active: bool
        activatable_widget: typing.Optional[Gtk.Widget]
        icon_name: typing.Optional[str]
        subtitle: typing.Optional[str]
        subtitle_lines: int
        subtitle_selectable: bool
        title_lines: int
        title: str
        title_selectable: bool
        use_markup: bool
        use_underline: bool
        activatable: bool
        child: typing.Optional[Gtk.Widget]
        selectable: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    def __init__(
        self,
        active: bool = ...,
        activatable_widget: typing.Optional[Gtk.Widget] = ...,
        icon_name: typing.Optional[str] = ...,
        subtitle: str = ...,
        subtitle_lines: int = ...,
        subtitle_selectable: bool = ...,
        title_lines: int = ...,
        title: str = ...,
        title_selectable: bool = ...,
        use_markup: bool = ...,
        use_underline: bool = ...,
        activatable: bool = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        selectable: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def get_active(self) -> bool: ...
    @classmethod
    def new(cls) -> SwitchRow: ...
    def set_active(self, is_active: bool) -> None: ...

class SwitchRowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SwitchRowClass()
    """

    parent_class: ActionRowClass = ...

class TabBar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        TabBar(**properties)
        new() -> Adw.TabBar

    Object AdwTabBar

    Signals from AdwTabBar:
      extra-drag-drop (AdwTabPage, GValue) -> gboolean
      extra-drag-value (AdwTabPage, GValue) -> GdkDragAction

    Properties from AdwTabBar:
      view -> AdwTabView: view
      start-action-widget -> GtkWidget: start-action-widget
      end-action-widget -> GtkWidget: end-action-widget
      autohide -> gboolean: autohide
      tabs-revealed -> gboolean: tabs-revealed
      expand-tabs -> gboolean: expand-tabs
      inverted -> gboolean: inverted
      is-overflowing -> gboolean: is-overflowing
      extra-drag-preload -> gboolean: extra-drag-preload
      extra-drag-preferred-action -> GdkDragAction: extra-drag-preferred-action

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        autohide: bool
        end_action_widget: typing.Optional[Gtk.Widget]
        expand_tabs: bool
        extra_drag_preferred_action: Gdk.DragAction
        extra_drag_preload: bool
        inverted: bool
        is_overflowing: bool
        start_action_widget: typing.Optional[Gtk.Widget]
        tabs_revealed: bool
        view: typing.Optional[TabView]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        end_action_widget: typing.Optional[Gtk.Widget] = ...,
        expand_tabs: bool = ...,
        extra_drag_preload: bool = ...,
        inverted: bool = ...,
        start_action_widget: typing.Optional[Gtk.Widget] = ...,
        view: typing.Optional[TabView] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_autohide(self) -> bool: ...
    def get_end_action_widget(self) -> typing.Optional[Gtk.Widget]: ...
    def get_expand_tabs(self) -> bool: ...
    def get_extra_drag_preferred_action(self) -> Gdk.DragAction: ...
    def get_extra_drag_preload(self) -> bool: ...
    def get_inverted(self) -> bool: ...
    def get_is_overflowing(self) -> bool: ...
    def get_start_action_widget(self) -> typing.Optional[Gtk.Widget]: ...
    def get_tabs_revealed(self) -> bool: ...
    def get_view(self) -> typing.Optional[TabView]: ...
    @classmethod
    def new(cls) -> TabBar: ...
    def set_autohide(self, autohide: bool) -> None: ...
    def set_end_action_widget(
        self, widget: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_expand_tabs(self, expand_tabs: bool) -> None: ...
    def set_extra_drag_preload(self, preload: bool) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_start_action_widget(
        self, widget: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_view(self, view: typing.Optional[TabView] = None) -> None: ...
    def setup_extra_drop_target(
        self,
        actions: Gdk.DragAction,
        types: typing.Optional[typing.Sequence[typing.Type[typing.Any]]] = None,
    ) -> None: ...

class TabBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabBarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class TabButton(
    Gtk.Widget, Gtk.Accessible, Gtk.Actionable, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        TabButton(**properties)
        new() -> Gtk.Widget

    Object AdwTabButton

    Signals from AdwTabButton:
      activate ()
      clicked ()

    Properties from AdwTabButton:
      view -> AdwTabView: view

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        view: typing.Optional[TabView]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole
        action_name: typing.Optional[str]
        action_target: GLib.Variant

    props: Props = ...
    def __init__(
        self,
        view: typing.Optional[TabView] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        action_name: typing.Optional[str] = ...,
        action_target: GLib.Variant = ...,
    ) -> None: ...
    def get_view(self) -> typing.Optional[TabView]: ...
    @classmethod
    def new(cls) -> TabButton: ...
    def set_view(self, view: typing.Optional[TabView] = None) -> None: ...

class TabButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabButtonClass()
    """

    parent_class: Gtk.WidgetClass = ...

class TabOverview(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        TabOverview(**properties)
        new() -> Gtk.Widget

    Object AdwTabOverview

    Signals from AdwTabOverview:
      extra-drag-drop (AdwTabPage, GValue) -> gboolean
      extra-drag-value (AdwTabPage, GValue) -> GdkDragAction
      create-tab () -> AdwTabPage

    Properties from AdwTabOverview:
      view -> AdwTabView: view
      child -> GtkWidget: child
      open -> gboolean: open
      inverted -> gboolean: inverted
      enable-search -> gboolean: enable-search
      search-active -> gboolean: search-active
      enable-new-tab -> gboolean: enable-new-tab
      secondary-menu -> GMenuModel: secondary-menu
      show-start-title-buttons -> gboolean: show-start-title-buttons
      show-end-title-buttons -> gboolean: show-end-title-buttons
      extra-drag-preferred-action -> GdkDragAction: extra-drag-preferred-action
      extra-drag-preload -> gboolean: extra-drag-preload

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        enable_new_tab: bool
        enable_search: bool
        extra_drag_preferred_action: Gdk.DragAction
        extra_drag_preload: bool
        inverted: bool
        open: bool
        search_active: bool
        secondary_menu: typing.Optional[Gio.MenuModel]
        show_end_title_buttons: bool
        show_start_title_buttons: bool
        view: typing.Optional[TabView]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        enable_new_tab: bool = ...,
        enable_search: bool = ...,
        extra_drag_preload: bool = ...,
        inverted: bool = ...,
        open: bool = ...,
        secondary_menu: typing.Optional[Gio.MenuModel] = ...,
        show_end_title_buttons: bool = ...,
        show_start_title_buttons: bool = ...,
        view: typing.Optional[TabView] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_enable_new_tab(self) -> bool: ...
    def get_enable_search(self) -> bool: ...
    def get_extra_drag_preferred_action(self) -> Gdk.DragAction: ...
    def get_extra_drag_preload(self) -> bool: ...
    def get_inverted(self) -> bool: ...
    def get_open(self) -> bool: ...
    def get_search_active(self) -> bool: ...
    def get_secondary_menu(self) -> typing.Optional[Gio.MenuModel]: ...
    def get_show_end_title_buttons(self) -> bool: ...
    def get_show_start_title_buttons(self) -> bool: ...
    def get_view(self) -> typing.Optional[TabView]: ...
    @classmethod
    def new(cls) -> TabOverview: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_enable_new_tab(self, enable_new_tab: bool) -> None: ...
    def set_enable_search(self, enable_search: bool) -> None: ...
    def set_extra_drag_preload(self, preload: bool) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_open(self, open: bool) -> None: ...
    def set_secondary_menu(
        self, secondary_menu: typing.Optional[Gio.MenuModel] = None
    ) -> None: ...
    def set_show_end_title_buttons(self, show_end_title_buttons: bool) -> None: ...
    def set_show_start_title_buttons(self, show_start_title_buttons: bool) -> None: ...
    def set_view(self, view: typing.Optional[TabView] = None) -> None: ...
    def setup_extra_drop_target(
        self,
        actions: Gdk.DragAction,
        types: typing.Optional[typing.Sequence[typing.Type[typing.Any]]] = None,
    ) -> None: ...

class TabOverviewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabOverviewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class TabPage(GObject.Object, Gtk.Accessible):
    """
    :Constructors:

    ::

        TabPage(**properties)

    Object AdwTabPage

    Properties from AdwTabPage:
      child -> GtkWidget: child
      parent -> AdwTabPage: parent
      selected -> gboolean: selected
      pinned -> gboolean: pinned
      title -> gchararray: title
      tooltip -> gchararray: tooltip
      icon -> GIcon: icon
      loading -> gboolean: loading
      indicator-icon -> GIcon: indicator-icon
      indicator-tooltip -> gchararray: indicator-tooltip
      indicator-activatable -> gboolean: indicator-activatable
      needs-attention -> gboolean: needs-attention
      keyword -> gchararray: keyword
      thumbnail-xalign -> gfloat: thumbnail-xalign
      thumbnail-yalign -> gfloat: thumbnail-yalign
      live-thumbnail -> gboolean: live-thumbnail

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        child: Gtk.Widget
        icon: typing.Optional[Gio.Icon]
        indicator_activatable: bool
        indicator_icon: typing.Optional[Gio.Icon]
        indicator_tooltip: str
        keyword: typing.Optional[str]
        live_thumbnail: bool
        loading: bool
        needs_attention: bool
        parent: typing.Optional[TabPage]
        pinned: bool
        selected: bool
        thumbnail_xalign: float
        thumbnail_yalign: float
        title: str
        tooltip: typing.Optional[str]
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        child: Gtk.Widget = ...,
        icon: typing.Optional[Gio.Icon] = ...,
        indicator_activatable: bool = ...,
        indicator_icon: typing.Optional[Gio.Icon] = ...,
        indicator_tooltip: str = ...,
        keyword: str = ...,
        live_thumbnail: bool = ...,
        loading: bool = ...,
        needs_attention: bool = ...,
        parent: TabPage = ...,
        thumbnail_xalign: float = ...,
        thumbnail_yalign: float = ...,
        title: str = ...,
        tooltip: str = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_child(self) -> Gtk.Widget: ...
    def get_icon(self) -> typing.Optional[Gio.Icon]: ...
    def get_indicator_activatable(self) -> bool: ...
    def get_indicator_icon(self) -> typing.Optional[Gio.Icon]: ...
    def get_indicator_tooltip(self) -> str: ...
    def get_keyword(self) -> typing.Optional[str]: ...
    def get_live_thumbnail(self) -> bool: ...
    def get_loading(self) -> bool: ...
    def get_needs_attention(self) -> bool: ...
    def get_parent(self) -> typing.Optional[TabPage]: ...
    def get_pinned(self) -> bool: ...
    def get_selected(self) -> bool: ...
    def get_thumbnail_xalign(self) -> float: ...
    def get_thumbnail_yalign(self) -> float: ...
    def get_title(self) -> str: ...
    def get_tooltip(self) -> typing.Optional[str]: ...
    def invalidate_thumbnail(self) -> None: ...
    def set_icon(self, icon: typing.Optional[Gio.Icon] = None) -> None: ...
    def set_indicator_activatable(self, activatable: bool) -> None: ...
    def set_indicator_icon(
        self, indicator_icon: typing.Optional[Gio.Icon] = None
    ) -> None: ...
    def set_indicator_tooltip(self, tooltip: str) -> None: ...
    def set_keyword(self, keyword: str) -> None: ...
    def set_live_thumbnail(self, live_thumbnail: bool) -> None: ...
    def set_loading(self, loading: bool) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_thumbnail_xalign(self, xalign: float) -> None: ...
    def set_thumbnail_yalign(self, yalign: float) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_tooltip(self, tooltip: str) -> None: ...

class TabPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabPageClass()
    """

    parent_class: GObject.ObjectClass = ...

class TabView(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        TabView(**properties)
        new() -> Adw.TabView

    Object AdwTabView

    Signals from AdwTabView:
      page-attached (AdwTabPage, gint)
      page-detached (AdwTabPage, gint)
      page-reordered (AdwTabPage, gint)
      close-page (AdwTabPage) -> gboolean
      setup-menu (AdwTabPage)
      create-window () -> AdwTabView
      indicator-activated (AdwTabPage)

    Properties from AdwTabView:
      n-pages -> gint: n-pages
      n-pinned-pages -> gint: n-pinned-pages
      is-transferring-page -> gboolean: is-transferring-page
      selected-page -> AdwTabPage: selected-page
      default-icon -> GIcon: default-icon
      menu-model -> GMenuModel: menu-model
      shortcuts -> AdwTabViewShortcuts: shortcuts
      pages -> GtkSelectionModel: pages

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        default_icon: Gio.Icon
        is_transferring_page: bool
        menu_model: typing.Optional[Gio.MenuModel]
        n_pages: int
        n_pinned_pages: int
        pages: Gtk.SelectionModel
        selected_page: typing.Optional[TabPage]
        shortcuts: TabViewShortcuts
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        menu_model: typing.Optional[Gio.MenuModel] = ...,
        selected_page: TabPage = ...,
        shortcuts: TabViewShortcuts = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_page(
        self, child: Gtk.Widget, parent: typing.Optional[TabPage] = None
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
    def get_menu_model(self) -> typing.Optional[Gio.MenuModel]: ...
    def get_n_pages(self) -> int: ...
    def get_n_pinned_pages(self) -> int: ...
    def get_nth_page(self, position: int) -> TabPage: ...
    def get_page(self, child: Gtk.Widget) -> TabPage: ...
    def get_page_position(self, page: TabPage) -> int: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_selected_page(self) -> typing.Optional[TabPage]: ...
    def get_shortcuts(self) -> TabViewShortcuts: ...
    def insert(self, child: Gtk.Widget, position: int) -> TabPage: ...
    def insert_pinned(self, child: Gtk.Widget, position: int) -> TabPage: ...
    def invalidate_thumbnails(self) -> None: ...
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
    def set_menu_model(
        self, menu_model: typing.Optional[Gio.MenuModel] = None
    ) -> None: ...
    def set_page_pinned(self, page: TabPage, pinned: bool) -> None: ...
    def set_selected_page(self, selected_page: TabPage) -> None: ...
    def set_shortcuts(self, shortcuts: TabViewShortcuts) -> None: ...
    def transfer_page(
        self, page: TabPage, other_view: TabView, position: int
    ) -> None: ...

class TabViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TabViewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class TimedAnimation(Animation):
    """
    :Constructors:

    ::

        TimedAnimation(**properties)
        new(widget:Gtk.Widget, from_:float, to:float, duration:int, target:Adw.AnimationTarget) -> Adw.Animation

    Object AdwTimedAnimation

    Properties from AdwTimedAnimation:
      value-from -> gdouble: value-from
      value-to -> gdouble: value-to
      duration -> guint: duration
      easing -> AdwEasing: easing
      repeat-count -> guint: repeat-count
      reverse -> gboolean: reverse
      alternate -> gboolean: alternate

    Signals from AdwAnimation:
      done ()

    Properties from AdwAnimation:
      widget -> GtkWidget: widget
      target -> AdwAnimationTarget: target
      value -> gdouble: value
      state -> AdwAnimationState: state
      follow-enable-animations-setting -> gboolean: follow-enable-animations-setting

    Signals from GObject:
      notify (GParam)
    """
    class Props(Animation.Props):
        alternate: bool
        duration: int
        easing: Easing
        repeat_count: int
        reverse: bool
        value_from: float
        value_to: float
        follow_enable_animations_setting: bool
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
        follow_enable_animations_setting: bool = ...,
        target: AnimationTarget = ...,
        widget: Gtk.Widget = ...,
    ) -> None: ...
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
    """
    :Constructors:

    ::

        Toast(**properties)
        new(title:str) -> Adw.Toast

    Object AdwToast

    Signals from AdwToast:
      button-clicked ()
      dismissed ()

    Properties from AdwToast:
      title -> gchararray: title
      button-label -> gchararray: button-label
      action-name -> gchararray: action-name
      action-target -> GVariant: action-target
      priority -> AdwToastPriority: priority
      timeout -> guint: timeout
      custom-title -> GtkWidget: custom-title
      use-markup -> gboolean: use-markup

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        action_name: typing.Optional[str]
        action_target: typing.Optional[GLib.Variant]
        button_label: typing.Optional[str]
        custom_title: typing.Optional[Gtk.Widget]
        priority: ToastPriority
        timeout: int
        title: typing.Optional[str]
        use_markup: bool

    props: Props = ...
    def __init__(
        self,
        action_name: typing.Optional[str] = ...,
        action_target: typing.Optional[GLib.Variant] = ...,
        button_label: typing.Optional[str] = ...,
        custom_title: typing.Optional[Gtk.Widget] = ...,
        priority: ToastPriority = ...,
        timeout: int = ...,
        title: str = ...,
        use_markup: bool = ...,
    ) -> None: ...
    def dismiss(self) -> None: ...
    def get_action_name(self) -> typing.Optional[str]: ...
    def get_action_target_value(self) -> typing.Optional[GLib.Variant]: ...
    def get_button_label(self) -> typing.Optional[str]: ...
    def get_custom_title(self) -> typing.Optional[Gtk.Widget]: ...
    def get_priority(self) -> ToastPriority: ...
    def get_timeout(self) -> int: ...
    def get_title(self) -> typing.Optional[str]: ...
    def get_use_markup(self) -> bool: ...
    @classmethod
    def new(cls, title: str) -> Toast: ...
    def set_action_name(self, action_name: typing.Optional[str] = None) -> None: ...
    def set_action_target_value(
        self, action_target: typing.Optional[GLib.Variant] = None
    ) -> None: ...
    def set_button_label(self, button_label: typing.Optional[str] = None) -> None: ...
    def set_custom_title(self, widget: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_detailed_action_name(
        self, detailed_action_name: typing.Optional[str] = None
    ) -> None: ...
    def set_priority(self, priority: ToastPriority) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_markup(self, use_markup: bool) -> None: ...

class ToastClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ToastClass()
    """

    parent_class: GObject.ObjectClass = ...

class ToastOverlay(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ToastOverlay(**properties)
        new() -> Gtk.Widget

    Object AdwToastOverlay

    Properties from AdwToastOverlay:
      child -> GtkWidget: child

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        child: typing.Optional[Gtk.Widget]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_toast(self, toast: Toast) -> None: ...
    def dismiss_all(self) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    @classmethod
    def new(cls) -> ToastOverlay: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...

class ToastOverlayClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ToastOverlayClass()
    """

    parent_class: Gtk.WidgetClass = ...

class Toggle(GObject.Object):
    """
    :Constructors:

    ::

        Toggle(**properties)
        new() -> Adw.Toggle

    Object AdwToggle

    Properties from AdwToggle:
      name -> gchararray: name
      label -> gchararray: label
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      tooltip -> gchararray: tooltip
      child -> GtkWidget: child
      enabled -> gboolean: enabled

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        child: typing.Optional[Gtk.Widget]
        enabled: bool
        icon_name: typing.Optional[str]
        label: typing.Optional[str]
        name: str
        tooltip: str
        use_underline: bool

    props: Props = ...
    def __init__(
        self,
        child: typing.Optional[Gtk.Widget] = ...,
        enabled: bool = ...,
        icon_name: typing.Optional[str] = ...,
        label: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        tooltip: str = ...,
        use_underline: bool = ...,
    ) -> None: ...
    def get_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_enabled(self) -> bool: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_index(self) -> int: ...
    def get_label(self) -> typing.Optional[str]: ...
    def get_name(self) -> str: ...
    def get_tooltip(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new(cls) -> Toggle: ...
    def set_child(self, child: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_label(self, label: typing.Optional[str] = None) -> None: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_tooltip(self, tooltip: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class ToggleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ToggleClass()
    """

    parent_class: GObject.ObjectClass = ...

class ToggleGroup(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        ToggleGroup(**properties)
        new() -> Gtk.Widget

    Object AdwToggleGroup

    Properties from AdwToggleGroup:
      n-toggles -> guint: n-toggles
      active -> guint: active
      active-name -> gchararray: active-name
      homogeneous -> gboolean: homogeneous
      can-shrink -> gboolean: can-shrink
      toggles -> GtkSelectionModel: toggles

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        active: int
        active_name: typing.Optional[str]
        can_shrink: bool
        homogeneous: bool
        n_toggles: int
        toggles: Gtk.SelectionModel
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        active: int = ...,
        active_name: typing.Optional[str] = ...,
        can_shrink: bool = ...,
        homogeneous: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def add(self, toggle: Toggle) -> None: ...
    def get_active(self) -> int: ...
    def get_active_name(self) -> typing.Optional[str]: ...
    def get_can_shrink(self) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_n_toggles(self) -> int: ...
    def get_toggle(self, index: int) -> typing.Optional[Toggle]: ...
    def get_toggle_by_name(self, name: str) -> typing.Optional[Toggle]: ...
    def get_toggles(self) -> Gtk.SelectionModel: ...
    @classmethod
    def new(cls) -> ToggleGroup: ...
    def remove(self, toggle: Toggle) -> None: ...
    def remove_all(self) -> None: ...
    def set_active(self, active: int) -> None: ...
    def set_active_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_can_shrink(self, can_shrink: bool) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...

class ToggleGroupClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ToggleGroupClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ToolbarView(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ToolbarView(**properties)
        new() -> Gtk.Widget

    Object AdwToolbarView

    Properties from AdwToolbarView:
      content -> GtkWidget: content
      top-bar-style -> AdwToolbarStyle: top-bar-style
      bottom-bar-style -> AdwToolbarStyle: bottom-bar-style
      reveal-top-bars -> gboolean: reveal-top-bars
      reveal-bottom-bars -> gboolean: reveal-bottom-bars
      extend-content-to-top-edge -> gboolean: extend-content-to-top-edge
      extend-content-to-bottom-edge -> gboolean: extend-content-to-bottom-edge
      top-bar-height -> gint: top-bar-height
      bottom-bar-height -> gint: bottom-bar-height

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        bottom_bar_height: int
        bottom_bar_style: ToolbarStyle
        content: typing.Optional[Gtk.Widget]
        extend_content_to_bottom_edge: bool
        extend_content_to_top_edge: bool
        reveal_bottom_bars: bool
        reveal_top_bars: bool
        top_bar_height: int
        top_bar_style: ToolbarStyle
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        bottom_bar_style: ToolbarStyle = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        extend_content_to_bottom_edge: bool = ...,
        extend_content_to_top_edge: bool = ...,
        reveal_bottom_bars: bool = ...,
        reveal_top_bars: bool = ...,
        top_bar_style: ToolbarStyle = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_bottom_bar(self, widget: Gtk.Widget) -> None: ...
    def add_top_bar(self, widget: Gtk.Widget) -> None: ...
    def get_bottom_bar_height(self) -> int: ...
    def get_bottom_bar_style(self) -> ToolbarStyle: ...
    def get_content(self) -> typing.Optional[Gtk.Widget]: ...
    def get_extend_content_to_bottom_edge(self) -> bool: ...
    def get_extend_content_to_top_edge(self) -> bool: ...
    def get_reveal_bottom_bars(self) -> bool: ...
    def get_reveal_top_bars(self) -> bool: ...
    def get_top_bar_height(self) -> int: ...
    def get_top_bar_style(self) -> ToolbarStyle: ...
    @classmethod
    def new(cls) -> ToolbarView: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_bottom_bar_style(self, style: ToolbarStyle) -> None: ...
    def set_content(self, content: typing.Optional[Gtk.Widget] = None) -> None: ...
    def set_extend_content_to_bottom_edge(self, extend: bool) -> None: ...
    def set_extend_content_to_top_edge(self, extend: bool) -> None: ...
    def set_reveal_bottom_bars(self, reveal: bool) -> None: ...
    def set_reveal_top_bars(self, reveal: bool) -> None: ...
    def set_top_bar_style(self, style: ToolbarStyle) -> None: ...

class ToolbarViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ToolbarViewClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ViewStack(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ViewStack(**properties)
        new() -> Gtk.Widget

    Object AdwViewStack

    Properties from AdwViewStack:
      hhomogeneous -> gboolean: hhomogeneous
      vhomogeneous -> gboolean: vhomogeneous
      visible-child -> GtkWidget: visible-child
      visible-child-name -> gchararray: visible-child-name
      enable-transitions -> gboolean: enable-transitions
      transition-duration -> guint: transition-duration
      transition-running -> gboolean: transition-running
      pages -> GtkSelectionModel: pages

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        enable_transitions: bool
        hhomogeneous: bool
        pages: Gtk.SelectionModel
        transition_duration: int
        transition_running: bool
        vhomogeneous: bool
        visible_child: typing.Optional[Gtk.Widget]
        visible_child_name: typing.Optional[str]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        enable_transitions: bool = ...,
        hhomogeneous: bool = ...,
        transition_duration: int = ...,
        vhomogeneous: bool = ...,
        visible_child: Gtk.Widget = ...,
        visible_child_name: str = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add(self, child: Gtk.Widget) -> ViewStackPage: ...
    def add_named(
        self, child: Gtk.Widget, name: typing.Optional[str] = None
    ) -> ViewStackPage: ...
    def add_titled(
        self, child: Gtk.Widget, name: typing.Optional[str], title: str
    ) -> ViewStackPage: ...
    def add_titled_with_icon(
        self, child: Gtk.Widget, name: typing.Optional[str], title: str, icon_name: str
    ) -> ViewStackPage: ...
    def get_child_by_name(self, name: str) -> typing.Optional[Gtk.Widget]: ...
    def get_enable_transitions(self) -> bool: ...
    def get_hhomogeneous(self) -> bool: ...
    def get_page(self, child: Gtk.Widget) -> ViewStackPage: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    def get_vhomogeneous(self) -> bool: ...
    def get_visible_child(self) -> typing.Optional[Gtk.Widget]: ...
    def get_visible_child_name(self) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> ViewStack: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_enable_transitions(self, enable_transitions: bool) -> None: ...
    def set_hhomogeneous(self, hhomogeneous: bool) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_vhomogeneous(self, vhomogeneous: bool) -> None: ...
    def set_visible_child(self, child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class ViewStackClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewStackClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ViewStackPage(GObject.Object, Gtk.Accessible):
    """
    :Constructors:

    ::

        ViewStackPage(**properties)

    Object AdwViewStackPage

    Properties from AdwViewStackPage:
      child -> GtkWidget: child
      name -> gchararray: name
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      needs-attention -> gboolean: needs-attention
      badge-number -> guint: badge-number
      visible -> gboolean: visible

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        badge_number: int
        child: Gtk.Widget
        icon_name: typing.Optional[str]
        name: typing.Optional[str]
        needs_attention: bool
        title: typing.Optional[str]
        use_underline: bool
        visible: bool
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        badge_number: int = ...,
        child: Gtk.Widget = ...,
        icon_name: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        needs_attention: bool = ...,
        title: typing.Optional[str] = ...,
        use_underline: bool = ...,
        visible: bool = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_badge_number(self) -> int: ...
    def get_child(self) -> Gtk.Widget: ...
    def get_icon_name(self) -> typing.Optional[str]: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_needs_attention(self) -> bool: ...
    def get_title(self) -> typing.Optional[str]: ...
    def get_use_underline(self) -> bool: ...
    def get_visible(self) -> bool: ...
    def set_badge_number(self, badge_number: int) -> None: ...
    def set_icon_name(self, icon_name: typing.Optional[str] = None) -> None: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_title(self, title: typing.Optional[str] = None) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class ViewStackPageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewStackPageClass()
    """

    parent_class: GObject.ObjectClass = ...

class ViewStackPages(GObject.Object, Gio.ListModel, Gtk.SelectionModel):
    """
    :Constructors:

    ::

        ViewStackPages(**properties)

    Object AdwViewStackPages

    Properties from AdwViewStackPages:
      selected-page -> AdwViewStackPage: selected-page

    Signals from GListModel:
      items-changed (guint, guint, guint)

    Signals from GtkSelectionModel:
      selection-changed (guint, guint)

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        selected_page: typing.Optional[ViewStackPage]

    props: Props = ...
    def __init__(self, selected_page: ViewStackPage = ...) -> None: ...
    def get_selected_page(self) -> typing.Optional[ViewStackPage]: ...
    def set_selected_page(self, page: ViewStackPage) -> None: ...

class ViewStackPagesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewStackPagesClass()
    """

    parent_class: GObject.ObjectClass = ...

class ViewSwitcher(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ViewSwitcher(**properties)
        new() -> Gtk.Widget

    Object AdwViewSwitcher

    Properties from AdwViewSwitcher:
      policy -> AdwViewSwitcherPolicy: policy
      stack -> AdwViewStack: stack

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        policy: ViewSwitcherPolicy
        stack: typing.Optional[ViewStack]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        stack: typing.Optional[ViewStack] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_policy(self) -> ViewSwitcherPolicy: ...
    def get_stack(self) -> typing.Optional[ViewStack]: ...
    @classmethod
    def new(cls) -> ViewSwitcher: ...
    def set_policy(self, policy: ViewSwitcherPolicy) -> None: ...
    def set_stack(self, stack: typing.Optional[ViewStack] = None) -> None: ...

class ViewSwitcherBar(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        ViewSwitcherBar(**properties)
        new() -> Gtk.Widget

    Object AdwViewSwitcherBar

    Properties from AdwViewSwitcherBar:
      stack -> AdwViewStack: stack
      reveal -> gboolean: reveal

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        reveal: bool
        stack: typing.Optional[ViewStack]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        stack: typing.Optional[ViewStack] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_reveal(self) -> bool: ...
    def get_stack(self) -> typing.Optional[ViewStack]: ...
    @classmethod
    def new(cls) -> ViewSwitcherBar: ...
    def set_reveal(self, reveal: bool) -> None: ...
    def set_stack(self, stack: typing.Optional[ViewStack] = None) -> None: ...

class ViewSwitcherBarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewSwitcherBarClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ViewSwitcherClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewSwitcherClass()
    """

    parent_class: Gtk.WidgetClass = ...

class ViewSwitcherTitle(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget
):
    """
    :Constructors:

    ::

        ViewSwitcherTitle(**properties)
        new() -> Gtk.Widget

    Object AdwViewSwitcherTitle

    Properties from AdwViewSwitcherTitle:
      stack -> AdwViewStack: stack
      title -> gchararray: title
      subtitle -> gchararray: subtitle
      view-switcher-enabled -> gboolean: view-switcher-enabled
      title-visible -> gboolean: title-visible

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        stack: typing.Optional[ViewStack]
        subtitle: str
        title: str
        title_visible: bool
        view_switcher_enabled: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        accessible_role: Gtk.AccessibleRole

    props: Props = ...
    def __init__(
        self,
        stack: typing.Optional[ViewStack] = ...,
        subtitle: str = ...,
        title: str = ...,
        view_switcher_enabled: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_stack(self) -> typing.Optional[ViewStack]: ...
    def get_subtitle(self) -> str: ...
    def get_title(self) -> str: ...
    def get_title_visible(self) -> bool: ...
    def get_view_switcher_enabled(self) -> bool: ...
    @classmethod
    def new(cls) -> ViewSwitcherTitle: ...
    def set_stack(self, stack: typing.Optional[ViewStack] = None) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_view_switcher_enabled(self, enabled: bool) -> None: ...

class ViewSwitcherTitleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ViewSwitcherTitleClass()
    """

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
    """
    :Constructors:

    ::

        Window(**properties)
        new() -> Gtk.Widget

    Object AdwWindow

    Properties from AdwWindow:
      content -> GtkWidget: content
      current-breakpoint -> AdwBreakpoint: current-breakpoint
      dialogs -> GListModel: dialogs
      visible-dialog -> AdwDialog: visible-dialog
      adaptive-preview -> gboolean: adaptive-preview

    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean

    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      suspended -> gboolean: suspended
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Window.Props):
        adaptive_preview: bool
        content: typing.Optional[Gtk.Widget]
        current_breakpoint: typing.Optional[Breakpoint]
        dialogs: Gio.ListModel
        visible_dialog: typing.Optional[Dialog]
        application: typing.Optional[Gtk.Application]
        child: typing.Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_widget: typing.Optional[Gtk.Widget]
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        display: Gdk.Display
        focus_visible: bool
        focus_widget: typing.Optional[Gtk.Widget]
        fullscreened: bool
        handle_menubar_accel: bool
        hide_on_close: bool
        icon_name: typing.Optional[str]
        is_active: bool
        maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        suspended: bool
        title: typing.Optional[str]
        titlebar: typing.Optional[Gtk.Widget]
        transient_for: typing.Optional[Gtk.Window]
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        adaptive_preview: bool = ...,
        content: typing.Optional[Gtk.Widget] = ...,
        application: typing.Optional[Gtk.Application] = ...,
        child: typing.Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_widget: typing.Optional[Gtk.Widget] = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        display: Gdk.Display = ...,
        focus_visible: bool = ...,
        focus_widget: typing.Optional[Gtk.Widget] = ...,
        fullscreened: bool = ...,
        handle_menubar_accel: bool = ...,
        hide_on_close: bool = ...,
        icon_name: typing.Optional[str] = ...,
        maximized: bool = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        startup_id: str = ...,
        title: typing.Optional[str] = ...,
        titlebar: typing.Optional[Gtk.Widget] = ...,
        transient_for: typing.Optional[Gtk.Window] = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def add_breakpoint(self, breakpoint: Breakpoint) -> None: ...
    def get_adaptive_preview(self) -> bool: ...
    def get_content(self) -> typing.Optional[Gtk.Widget]: ...
    def get_current_breakpoint(self) -> typing.Optional[Breakpoint]: ...
    def get_dialogs(self) -> Gio.ListModel: ...
    def get_visible_dialog(self) -> typing.Optional[Dialog]: ...
    @classmethod
    def new(cls) -> Window: ...
    def set_adaptive_preview(self, adaptive_preview: bool) -> None: ...
    def set_content(self, content: typing.Optional[Gtk.Widget] = None) -> None: ...

class WindowClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowClass()
    """

    parent_class: Gtk.WindowClass = ...
    padding: list[None] = ...

class WindowTitle(Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget):
    """
    :Constructors:

    ::

        WindowTitle(**properties)
        new(title:str, subtitle:str) -> Gtk.Widget

    Object AdwWindowTitle

    Properties from AdwWindowTitle:
      title -> gchararray: title
      subtitle -> gchararray: subtitle

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        subtitle: str
        title: str
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
    ) -> None: ...
    def get_subtitle(self) -> str: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(cls, title: str, subtitle: str) -> WindowTitle: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_title(self, title: str) -> None: ...

class WindowTitleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WindowTitleClass()
    """

    parent_class: Gtk.WidgetClass = ...

class WrapBox(
    Gtk.Widget, Gtk.Accessible, Gtk.Buildable, Gtk.ConstraintTarget, Gtk.Orientable
):
    """
    :Constructors:

    ::

        WrapBox(**properties)
        new() -> Gtk.Widget

    Object AdwWrapBox

    Properties from AdwWrapBox:
      child-spacing -> gint: child-spacing
      child-spacing-unit -> AdwLengthUnit: child-spacing-unit
      pack-direction -> AdwPackDirection: pack-direction
      align -> gfloat: align
      justify -> AdwJustifyMode: justify
      justify-last-line -> gboolean: justify-last-line
      line-spacing -> gint: line-spacing
      line-spacing-unit -> AdwLengthUnit: line-spacing-unit
      line-homogeneous -> gboolean: line-homogeneous
      natural-line-length -> gint: natural-line-length
      natural-line-length-unit -> AdwLengthUnit: natural-line-length-unit
      wrap-reverse -> gboolean: wrap-reverse
      wrap-policy -> AdwWrapPolicy: wrap-policy

    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
      limit-events -> gboolean: limit-events

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.Widget.Props):
        align: float
        child_spacing: int
        child_spacing_unit: LengthUnit
        justify: JustifyMode
        justify_last_line: bool
        line_homogeneous: bool
        line_spacing: int
        line_spacing_unit: LengthUnit
        natural_line_length: int
        natural_line_length_unit: LengthUnit
        pack_direction: PackDirection
        wrap_policy: WrapPolicy
        wrap_reverse: bool
        can_focus: bool
        can_target: bool
        css_classes: list[str]
        css_name: str
        cursor: typing.Optional[Gdk.Cursor]
        focus_on_click: bool
        focusable: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        layout_manager: typing.Optional[Gtk.LayoutManager]
        limit_events: bool
        margin_bottom: int
        margin_end: int
        margin_start: int
        margin_top: int
        name: str
        opacity: float
        overflow: Gtk.Overflow
        parent: typing.Optional[Gtk.Widget]
        receives_default: bool
        root: typing.Optional[Gtk.Root]
        scale_factor: int
        sensitive: bool
        tooltip_markup: typing.Optional[str]
        tooltip_text: typing.Optional[str]
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
        align: float = ...,
        child_spacing: int = ...,
        child_spacing_unit: LengthUnit = ...,
        justify: JustifyMode = ...,
        justify_last_line: bool = ...,
        line_homogeneous: bool = ...,
        line_spacing: int = ...,
        line_spacing_unit: LengthUnit = ...,
        natural_line_length: int = ...,
        natural_line_length_unit: LengthUnit = ...,
        pack_direction: PackDirection = ...,
        wrap_policy: WrapPolicy = ...,
        wrap_reverse: bool = ...,
        can_focus: bool = ...,
        can_target: bool = ...,
        css_classes: typing.Sequence[str] = ...,
        css_name: str = ...,
        cursor: typing.Optional[Gdk.Cursor] = ...,
        focus_on_click: bool = ...,
        focusable: bool = ...,
        halign: Gtk.Align = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        layout_manager: typing.Optional[Gtk.LayoutManager] = ...,
        limit_events: bool = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        opacity: float = ...,
        overflow: Gtk.Overflow = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        tooltip_markup: typing.Optional[str] = ...,
        tooltip_text: typing.Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        accessible_role: Gtk.AccessibleRole = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def append(self, child: Gtk.Widget) -> None: ...
    def get_align(self) -> float: ...
    def get_child_spacing(self) -> int: ...
    def get_child_spacing_unit(self) -> LengthUnit: ...
    def get_justify(self) -> JustifyMode: ...
    def get_justify_last_line(self) -> bool: ...
    def get_line_homogeneous(self) -> bool: ...
    def get_line_spacing(self) -> int: ...
    def get_line_spacing_unit(self) -> LengthUnit: ...
    def get_natural_line_length(self) -> int: ...
    def get_natural_line_length_unit(self) -> LengthUnit: ...
    def get_pack_direction(self) -> PackDirection: ...
    def get_wrap_policy(self) -> WrapPolicy: ...
    def get_wrap_reverse(self) -> bool: ...
    def insert_child_after(
        self, child: Gtk.Widget, sibling: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    @classmethod
    def new(cls) -> WrapBox: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def reorder_child_after(
        self, child: Gtk.Widget, sibling: typing.Optional[Gtk.Widget] = None
    ) -> None: ...
    def set_align(self, align: float) -> None: ...
    def set_child_spacing(self, child_spacing: int) -> None: ...
    def set_child_spacing_unit(self, unit: LengthUnit) -> None: ...
    def set_justify(self, justify: JustifyMode) -> None: ...
    def set_justify_last_line(self, justify_last_line: bool) -> None: ...
    def set_line_homogeneous(self, homogeneous: bool) -> None: ...
    def set_line_spacing(self, line_spacing: int) -> None: ...
    def set_line_spacing_unit(self, unit: LengthUnit) -> None: ...
    def set_natural_line_length(self, natural_line_length: int) -> None: ...
    def set_natural_line_length_unit(self, unit: LengthUnit) -> None: ...
    def set_pack_direction(self, pack_direction: PackDirection) -> None: ...
    def set_wrap_policy(self, wrap_policy: WrapPolicy) -> None: ...
    def set_wrap_reverse(self, wrap_reverse: bool) -> None: ...

class WrapBoxClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WrapBoxClass()
    """

    parent_class: Gtk.WidgetClass = ...

class WrapLayout(Gtk.LayoutManager, Gtk.Orientable):
    """
    :Constructors:

    ::

        WrapLayout(**properties)
        new() -> Gtk.LayoutManager

    Object AdwWrapLayout

    Properties from AdwWrapLayout:
      child-spacing -> gint: child-spacing
      child-spacing-unit -> AdwLengthUnit: child-spacing-unit
      pack-direction -> AdwPackDirection: pack-direction
      align -> gfloat: align
      justify -> AdwJustifyMode: justify
      justify-last-line -> gboolean: justify-last-line
      line-spacing -> gint: line-spacing
      line-spacing-unit -> AdwLengthUnit: line-spacing-unit
      line-homogeneous -> gboolean: line-homogeneous
      natural-line-length -> gint: natural-line-length
      natural-line-length-unit -> AdwLengthUnit: natural-line-length-unit
      wrap-reverse -> gboolean: wrap-reverse
      wrap-policy -> AdwWrapPolicy: wrap-policy

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gtk.LayoutManager.Props):
        align: float
        child_spacing: int
        child_spacing_unit: LengthUnit
        justify: JustifyMode
        justify_last_line: bool
        line_homogeneous: bool
        line_spacing: int
        line_spacing_unit: LengthUnit
        natural_line_length: int
        natural_line_length_unit: LengthUnit
        pack_direction: PackDirection
        wrap_policy: WrapPolicy
        wrap_reverse: bool
        orientation: Gtk.Orientation

    props: Props = ...
    def __init__(
        self,
        align: float = ...,
        child_spacing: int = ...,
        child_spacing_unit: LengthUnit = ...,
        justify: JustifyMode = ...,
        justify_last_line: bool = ...,
        line_homogeneous: bool = ...,
        line_spacing: int = ...,
        line_spacing_unit: LengthUnit = ...,
        natural_line_length: int = ...,
        natural_line_length_unit: LengthUnit = ...,
        pack_direction: PackDirection = ...,
        wrap_policy: WrapPolicy = ...,
        wrap_reverse: bool = ...,
        orientation: Gtk.Orientation = ...,
    ) -> None: ...
    def get_align(self) -> float: ...
    def get_child_spacing(self) -> int: ...
    def get_child_spacing_unit(self) -> LengthUnit: ...
    def get_justify(self) -> JustifyMode: ...
    def get_justify_last_line(self) -> bool: ...
    def get_line_homogeneous(self) -> bool: ...
    def get_line_spacing(self) -> int: ...
    def get_line_spacing_unit(self) -> LengthUnit: ...
    def get_natural_line_length(self) -> int: ...
    def get_natural_line_length_unit(self) -> LengthUnit: ...
    def get_pack_direction(self) -> PackDirection: ...
    def get_wrap_policy(self) -> WrapPolicy: ...
    def get_wrap_reverse(self) -> bool: ...
    @classmethod
    def new(cls) -> WrapLayout: ...
    def set_align(self, align: float) -> None: ...
    def set_child_spacing(self, child_spacing: int) -> None: ...
    def set_child_spacing_unit(self, unit: LengthUnit) -> None: ...
    def set_justify(self, justify: JustifyMode) -> None: ...
    def set_justify_last_line(self, justify_last_line: bool) -> None: ...
    def set_line_homogeneous(self, homogeneous: bool) -> None: ...
    def set_line_spacing(self, line_spacing: int) -> None: ...
    def set_line_spacing_unit(self, unit: LengthUnit) -> None: ...
    def set_natural_line_length(self, natural_line_length: int) -> None: ...
    def set_natural_line_length_unit(self, unit: LengthUnit) -> None: ...
    def set_pack_direction(self, pack_direction: PackDirection) -> None: ...
    def set_wrap_policy(self, wrap_policy: WrapPolicy) -> None: ...
    def set_wrap_reverse(self, wrap_reverse: bool) -> None: ...

class WrapLayoutClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WrapLayoutClass()
    """

    parent_class: Gtk.LayoutManagerClass = ...

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

class AccentColor(GObject.GEnum):
    BLUE = 0
    GREEN = 2
    MAIA = 108
    ORANGE = 4
    PINK = 6
    PURPLE = 7
    RED = 5
    SLATE = 8
    TEAL = 1
    YELLOW = 3
    @staticmethod
    def to_rgba(self: AccentColor) -> Gdk.RGBA: ...
    @staticmethod
    def to_standalone_rgba(self: AccentColor, dark: bool) -> Gdk.RGBA: ...

class AnimationState(GObject.GEnum):
    FINISHED = 3
    IDLE = 0
    PAUSED = 1
    PLAYING = 2

class BannerButtonStyle(GObject.GEnum):
    DEFAULT = 0
    SUGGESTED = 1

class BreakpointConditionLengthType(GObject.GEnum):
    MAX_HEIGHT = 3
    MAX_WIDTH = 1
    MIN_HEIGHT = 2
    MIN_WIDTH = 0

class BreakpointConditionRatioType(GObject.GEnum):
    MAX_ASPECT_RATIO = 1
    MIN_ASPECT_RATIO = 0

class CenteringPolicy(GObject.GEnum):
    LOOSE = 0
    STRICT = 1

class ColorScheme(GObject.GEnum):
    DEFAULT = 0
    FORCE_DARK = 4
    FORCE_LIGHT = 1
    PREFER_DARK = 3
    PREFER_LIGHT = 2

class DialogPresentationMode(GObject.GEnum):
    AUTO = 0
    BOTTOM_SHEET = 2
    FLOATING = 1

class Easing(GObject.GEnum):
    EASE = 31
    EASE_IN = 32
    EASE_IN_BACK = 25
    EASE_IN_BOUNCE = 28
    EASE_IN_CIRC = 19
    EASE_IN_CUBIC = 4
    EASE_IN_ELASTIC = 22
    EASE_IN_EXPO = 16
    EASE_IN_OUT = 34
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
    EASE_OUT = 33
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

class InlineViewSwitcherDisplayMode(GObject.GEnum):
    BOTH = 2
    ICONS = 1
    LABELS = 0

class JustifyMode(GObject.GEnum):
    FILL = 1
    NONE = 0
    SPREAD = 2

class LeafletTransitionType(GObject.GEnum):
    OVER = 0
    SLIDE = 2
    UNDER = 1

class LengthUnit(GObject.GEnum):
    PT = 1
    PX = 0
    SP = 2
    @staticmethod
    def from_px(
        unit: LengthUnit, value: float, settings: typing.Optional[Gtk.Settings] = None
    ) -> float: ...
    @staticmethod
    def to_px(
        unit: LengthUnit, value: float, settings: typing.Optional[Gtk.Settings] = None
    ) -> float: ...

class NavigationDirection(GObject.GEnum):
    BACK = 0
    FORWARD = 1

class PackDirection(GObject.GEnum):
    END_TO_START = 1
    START_TO_END = 0

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

class ToolbarStyle(GObject.GEnum):
    FLAT = 0
    RAISED = 1
    RAISED_BORDER = 2

class ViewSwitcherPolicy(GObject.GEnum):
    NARROW = 0
    WIDE = 1

class WrapPolicy(GObject.GEnum):
    MINIMUM = 0
    NATURAL = 1
