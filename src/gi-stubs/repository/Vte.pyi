from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

import cairo
from gi.repository import Atk
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

MAJOR_VERSION: int = 0
MICRO_VERSION: int = 2
MINOR_VERSION: int = 74
REGEX_FLAGS_DEFAULT: int = 1075314688
SPAWN_NO_PARENT_ENVV: int = 33554432
SPAWN_NO_SYSTEMD_SCOPE: int = 67108864
SPAWN_REQUIRE_SYSTEMD_SCOPE: int = 134217728
TEST_FLAGS_ALL: int = 18446744073709551615
TEST_FLAGS_NONE: int = 0
_lock = ...  # FIXME Constant
_namespace: str = "Vte"
_version: str = "2.91"

def get_encoding_supported(encoding: str) -> bool: ...
def get_encodings(include_aliases: bool) -> list[str]: ...
def get_feature_flags() -> FeatureFlags: ...
def get_features() -> str: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def get_user_shell() -> str: ...
def pty_error_quark() -> int: ...
def regex_error_quark() -> int: ...

class CharAttributes(GObject.GPointer):
    """
    :Constructors:

    ::

        CharAttributes()
    """

    row: int = ...
    column: int = ...
    fore: Pango.Color = ...
    back: Pango.Color = ...
    underline: int = ...
    strikethrough: int = ...
    columns: int = ...

class Pty(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Pty(**properties)
        new_foreign_sync(fd:int, cancellable:Gio.Cancellable=None) -> Vte.Pty
        new_sync(flags:Vte.PtyFlags, cancellable:Gio.Cancellable=None) -> Vte.Pty

    Object VtePty

    Properties from VtePty:
      flags -> VtePtyFlags: flags
      fd -> gint: fd

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        fd: int
        flags: PtyFlags
    props: Props = ...
    def __init__(self, fd: int = ..., flags: PtyFlags = ...): ...
    def child_setup(self) -> None: ...
    def close(self) -> None: ...
    def get_fd(self) -> int: ...
    def get_size(self) -> Tuple[bool, int, int]: ...
    @classmethod
    def new_foreign_sync(
        cls, fd: int, cancellable: Optional[Gio.Cancellable] = None
    ) -> Pty: ...
    @classmethod
    def new_sync(
        cls, flags: PtyFlags, cancellable: Optional[Gio.Cancellable] = None
    ) -> Pty: ...
    def set_size(self, rows: int, columns: int) -> bool: ...
    def set_utf8(self, utf8: bool) -> bool: ...
    def spawn_async(
        self,
        working_directory: Optional[str],
        argv: Sequence[str],
        envv: Optional[Sequence[str]],
        spawn_flags: GLib.SpawnFlags,
        child_setup: Optional[Callable[..., None]],
        timeout: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def spawn_finish(self, result: Gio.AsyncResult) -> Tuple[bool, int]: ...
    def spawn_with_fds_async(
        self,
        working_directory: Optional[str],
        argv: Sequence[str],
        envv: Optional[Sequence[str]],
        fds: Optional[Sequence[int]],
        map_fds: Optional[Sequence[int]],
        spawn_flags: GLib.SpawnFlags,
        child_setup: Optional[Callable[..., None]],
        timeout: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...

class PtyClass(GObject.GPointer): ...

class Regex(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_for_match(pattern:str, pattern_length:int, flags:int) -> Vte.Regex
        new_for_search(pattern:str, pattern_length:int, flags:int) -> Vte.Regex
    """

    def jit(self, flags: int) -> bool: ...
    @classmethod
    def new_for_match(cls, pattern: str, pattern_length: int, flags: int) -> Regex: ...
    @classmethod
    def new_for_search(cls, pattern: str, pattern_length: int, flags: int) -> Regex: ...
    def ref(self) -> Regex: ...
    def substitute(self, subject: str, replacement: str, flags: int) -> str: ...
    def unref(self) -> Regex: ...

class Terminal(Gtk.Widget, Atk.ImplementorIface, Gtk.Buildable, Gtk.Scrollable):
    """
    :Constructors:

    ::

        Terminal(**properties)
        new() -> Vte.Terminal

    Object VteTerminal

    Signals from VteTerminal:
      eof ()
      child-exited (gint)
      window-title-changed ()
      icon-title-changed ()
      current-directory-uri-changed ()
      current-file-uri-changed ()
      hyperlink-hover-uri-changed (gchararray, GdkRectangle)
      encoding-changed ()
      commit (gchararray, guint)
      char-size-changed (guint, guint)
      selection-changed ()
      contents-changed ()
      cursor-moved ()
      deiconify-window ()
      iconify-window ()
      raise-window ()
      lower-window ()
      refresh-window ()
      restore-window ()
      maximize-window ()
      resize-window (guint, guint)
      move-window (guint, guint)
      increase-font-size ()
      decrease-font-size ()
      text-modified ()
      text-inserted ()
      text-deleted ()
      text-scrolled (gint)
      copy-clipboard ()
      paste-clipboard ()
      bell ()

    Properties from VteTerminal:
      allow-bold -> gboolean: allow-bold
      allow-hyperlink -> gboolean: allow-hyperlink
      audible-bell -> gboolean: audible-bell
      backspace-binding -> VteEraseBinding: backspace-binding
      bold-is-bright -> gboolean: bold-is-bright
      cell-height-scale -> gdouble: cell-height-scale
      cell-width-scale -> gdouble: cell-width-scale
      cjk-ambiguous-width -> gint: cjk-ambiguous-width
      cursor-blink-mode -> VteCursorBlinkMode: cursor-blink-mode
      cursor-shape -> VteCursorShape: cursor-shape
      current-directory-uri -> gchararray: current-directory-uri
      current-file-uri -> gchararray: current-file-uri
      delete-binding -> VteEraseBinding: delete-binding
      enable-bidi -> gboolean: enable-bidi
      enable-fallback-scrolling -> gboolean: enable-fallback-scrolling
      enable-shaping -> gboolean: enable-shaping
      enable-sixel -> gboolean: enable-sixel
      encoding -> gchararray: encoding
      font-desc -> PangoFontDescription: font-desc
      font-options -> CairoFontOptions: font-options
      font-scale -> gdouble: font-scale
      hyperlink-hover-uri -> gchararray: hyperlink-hover-uri
      icon-title -> gchararray: icon-title
      input-enabled -> gboolean: input-enabled
      pointer-autohide -> gboolean: pointer-autohide
      pty -> VtePty: pty
      rewrap-on-resize -> gboolean: rewrap-on-resize
      scrollback-lines -> guint: scrollback-lines
      scroll-on-keystroke -> gboolean: scroll-on-keystroke
      scroll-on-output -> gboolean: scroll-on-output
      scroll-unit-is-pixels -> gboolean: scroll-unit-is-pixels
      text-blink-mode -> VteTextBlinkMode: text-blink-mode
      window-title -> gchararray: window-title
      word-char-exceptions -> gchararray: word-char-exceptions

    Signals from GtkWidget:
      composited-changed ()
      event (GdkEvent) -> gboolean
      direction-changed (GtkTextDirection)
      state-changed (GtkStateType)
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-allocate (GdkRectangle)
      state-flags-changed (GtkStateFlags)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      style-updated ()
      grab-notify (gboolean)
      child-notify (GParam)
      draw (CairoContext) -> gboolean
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      touch-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean

    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      focus-on-click -> gboolean: Focus on click
        Whether the widget should grab focus when it is clicked with the mouse
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colours etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realised
      opacity -> gdouble: Opacity for Widget
        The opacity of the widget, from 0 to 1
      double-buffered -> gboolean: Double Buffered
        Whether the widget is double buffered
      halign -> GtkAlign: Horizontal Alignment
        How to position in extra horizontal space
      valign -> GtkAlign: Vertical Alignment
        How to position in extra vertical space
      margin-left -> gint: Margin on Left
        Pixels of extra space on the left side
      margin-right -> gint: Margin on Right
        Pixels of extra space on the right side
      margin-start -> gint: Margin on Start
        Pixels of extra space on the start
      margin-end -> gint: Margin on End
        Pixels of extra space on the end
      margin-top -> gint: Margin on Top
        Pixels of extra space on the top side
      margin-bottom -> gint: Margin on Bottom
        Pixels of extra space on the bottom side
      margin -> gint: All Margins
        Pixels of extra space on all four sides
      hexpand -> gboolean: Horizontal Expand
        Whether widget wants more horizontal space
      vexpand -> gboolean: Vertical Expand
        Whether widget wants more vertical space
      hexpand-set -> gboolean: Horizontal Expand Set
        Whether to use the hexpand property
      vexpand-set -> gboolean: Vertical Expand Set
        Whether to use the vexpand property
      expand -> gboolean: Expand Both
        Whether widget wants to expand in both directions
      scale-factor -> gint: Scale factor
        The scaling factor of the window

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allow_bold: bool
        allow_hyperlink: bool
        audible_bell: bool
        backspace_binding: EraseBinding
        bold_is_bright: bool
        cell_height_scale: float
        cell_width_scale: float
        cjk_ambiguous_width: int
        current_directory_uri: Optional[str]
        current_file_uri: Optional[str]
        cursor_blink_mode: CursorBlinkMode
        cursor_shape: CursorShape
        delete_binding: EraseBinding
        enable_bidi: bool
        enable_fallback_scrolling: bool
        enable_shaping: bool
        enable_sixel: bool
        encoding: Optional[str]
        font_desc: Pango.FontDescription
        font_options: Optional[cairo.FontOptions]
        font_scale: float
        hyperlink_hover_uri: str
        icon_title: Optional[str]
        input_enabled: bool
        pointer_autohide: bool
        pty: Pty
        rewrap_on_resize: bool
        scroll_on_keystroke: bool
        scroll_on_output: bool
        scroll_unit_is_pixels: bool
        scrollback_lines: int
        text_blink_mode: TextBlinkMode
        window_title: Optional[str]
        word_char_exceptions: Optional[str]
        app_paintable: bool
        can_default: bool
        can_focus: bool
        composite_child: bool
        double_buffered: bool
        events: Gdk.EventMask
        expand: bool
        focus_on_click: bool
        halign: Gtk.Align
        has_default: bool
        has_focus: bool
        has_tooltip: bool
        height_request: int
        hexpand: bool
        hexpand_set: bool
        is_focus: bool
        margin: int
        margin_bottom: int
        margin_end: int
        margin_left: int
        margin_right: int
        margin_start: int
        margin_top: int
        name: str
        no_show_all: bool
        opacity: float
        parent: Optional[Gtk.Container]
        receives_default: bool
        scale_factor: int
        sensitive: bool
        style: Gtk.Style
        tooltip_markup: Optional[str]
        tooltip_text: Optional[str]
        valign: Gtk.Align
        vexpand: bool
        vexpand_set: bool
        visible: bool
        width_request: int
        window: Optional[Gdk.Window]
        hadjustment: Gtk.Adjustment
        hscroll_policy: Gtk.ScrollablePolicy
        vadjustment: Gtk.Adjustment
        vscroll_policy: Gtk.ScrollablePolicy
    props: Props = ...
    widget: Gtk.Widget = ...
    _unused_padding: list[None] = ...
    def __init__(
        self,
        allow_bold: bool = ...,
        allow_hyperlink: bool = ...,
        audible_bell: bool = ...,
        backspace_binding: EraseBinding = ...,
        bold_is_bright: bool = ...,
        cell_height_scale: float = ...,
        cell_width_scale: float = ...,
        cjk_ambiguous_width: int = ...,
        cursor_blink_mode: CursorBlinkMode = ...,
        cursor_shape: CursorShape = ...,
        delete_binding: EraseBinding = ...,
        enable_bidi: bool = ...,
        enable_fallback_scrolling: bool = ...,
        enable_shaping: bool = ...,
        enable_sixel: bool = ...,
        encoding: Optional[str] = ...,
        font_desc: Pango.FontDescription = ...,
        font_options: Optional[cairo.FontOptions] = ...,
        font_scale: float = ...,
        input_enabled: bool = ...,
        pointer_autohide: bool = ...,
        pty: Optional[Pty] = ...,
        rewrap_on_resize: bool = ...,
        scroll_on_keystroke: bool = ...,
        scroll_on_output: bool = ...,
        scroll_unit_is_pixels: bool = ...,
        scrollback_lines: int = ...,
        text_blink_mode: TextBlinkMode = ...,
        app_paintable: bool = ...,
        can_default: bool = ...,
        can_focus: bool = ...,
        double_buffered: bool = ...,
        events: Gdk.EventMask = ...,
        expand: bool = ...,
        focus_on_click: bool = ...,
        halign: Gtk.Align = ...,
        has_default: bool = ...,
        has_focus: bool = ...,
        has_tooltip: bool = ...,
        height_request: int = ...,
        hexpand: bool = ...,
        hexpand_set: bool = ...,
        is_focus: bool = ...,
        margin: int = ...,
        margin_bottom: int = ...,
        margin_end: int = ...,
        margin_left: int = ...,
        margin_right: int = ...,
        margin_start: int = ...,
        margin_top: int = ...,
        name: str = ...,
        no_show_all: bool = ...,
        opacity: float = ...,
        parent: Gtk.Container = ...,
        receives_default: bool = ...,
        sensitive: bool = ...,
        style: Optional[Gtk.Style] = ...,
        tooltip_markup: Optional[str] = ...,
        tooltip_text: Optional[str] = ...,
        valign: Gtk.Align = ...,
        vexpand: bool = ...,
        vexpand_set: bool = ...,
        visible: bool = ...,
        width_request: int = ...,
        hadjustment: Optional[Gtk.Adjustment] = ...,
        hscroll_policy: Gtk.ScrollablePolicy = ...,
        vadjustment: Optional[Gtk.Adjustment] = ...,
        vscroll_policy: Gtk.ScrollablePolicy = ...,
    ): ...
    def copy_clipboard(self) -> None: ...
    def copy_clipboard_format(self, format: Format) -> None: ...
    def copy_primary(self) -> None: ...
    def do_bell(self) -> None: ...
    def do_char_size_changed(self, char_width: int, char_height: int) -> None: ...
    def do_child_exited(self, status: int) -> None: ...
    def do_commit(self, text: str, size: int) -> None: ...
    def do_contents_changed(self) -> None: ...
    def do_copy_clipboard(self) -> None: ...
    def do_cursor_moved(self) -> None: ...
    def do_decrease_font_size(self) -> None: ...
    def do_deiconify_window(self) -> None: ...
    def do_encoding_changed(self) -> None: ...
    def do_eof(self) -> None: ...
    def do_icon_title_changed(self) -> None: ...
    def do_iconify_window(self) -> None: ...
    def do_increase_font_size(self) -> None: ...
    def do_lower_window(self) -> None: ...
    def do_maximize_window(self) -> None: ...
    def do_move_window(self, x: int, y: int) -> None: ...
    def do_paste_clipboard(self) -> None: ...
    def do_raise_window(self) -> None: ...
    def do_refresh_window(self) -> None: ...
    def do_resize_window(self, width: int, height: int) -> None: ...
    def do_restore_window(self) -> None: ...
    def do_selection_changed(self) -> None: ...
    def do_text_deleted(self) -> None: ...
    def do_text_inserted(self) -> None: ...
    def do_text_modified(self) -> None: ...
    def do_text_scrolled(self, delta: int) -> None: ...
    def do_window_title_changed(self) -> None: ...
    def event_check_gregex_simple(
        self,
        event: Gdk.Event,
        regexes: Sequence[GLib.Regex],
        match_flags: GLib.RegexMatchFlags,
    ) -> Tuple[bool, list[str]]: ...
    def event_check_regex_simple(
        self, event: Gdk.Event, regexes: Sequence[Regex], match_flags: int
    ) -> Optional[list[str]]: ...
    def feed(self, data: Optional[Sequence[int]] = None) -> None: ...
    def feed_child(self, text: Optional[Sequence[int]] = None) -> None: ...
    def feed_child_binary(self, data: Optional[Sequence[int]] = None) -> None: ...
    def get_allow_bold(self) -> bool: ...
    def get_allow_hyperlink(self) -> bool: ...
    def get_audible_bell(self) -> bool: ...
    def get_bold_is_bright(self) -> bool: ...
    def get_cell_height_scale(self) -> float: ...
    def get_cell_width_scale(self) -> float: ...
    def get_char_height(self) -> int: ...
    def get_char_width(self) -> int: ...
    def get_cjk_ambiguous_width(self) -> int: ...
    def get_color_background_for_draw(self) -> Gdk.RGBA: ...
    def get_column_count(self) -> int: ...
    def get_current_directory_uri(self) -> Optional[str]: ...
    def get_current_file_uri(self) -> Optional[str]: ...
    def get_cursor_blink_mode(self) -> CursorBlinkMode: ...
    def get_cursor_position(self) -> Tuple[int, int]: ...
    def get_cursor_shape(self) -> CursorShape: ...
    def get_enable_bidi(self) -> bool: ...
    def get_enable_fallback_scrolling(self) -> bool: ...
    def get_enable_shaping(self) -> bool: ...
    def get_enable_sixel(self) -> bool: ...
    def get_encoding(self) -> Optional[str]: ...
    def get_font(self) -> Pango.FontDescription: ...
    def get_font_options(self) -> Optional[cairo.FontOptions]: ...
    def get_font_scale(self) -> float: ...
    def get_geometry_hints(self, min_rows: int, min_columns: int) -> Gdk.Geometry: ...
    def get_has_selection(self) -> bool: ...
    def get_icon_title(self) -> Optional[str]: ...
    def get_input_enabled(self) -> bool: ...
    def get_mouse_autohide(self) -> bool: ...
    def get_pty(self) -> Pty: ...
    def get_rewrap_on_resize(self) -> bool: ...
    def get_row_count(self) -> int: ...
    def get_scroll_on_keystroke(self) -> bool: ...
    def get_scroll_on_output(self) -> bool: ...
    def get_scroll_unit_is_pixels(self) -> bool: ...
    def get_scrollback_lines(self) -> int: ...
    def get_text(
        self, is_selected: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> Tuple[Optional[str], list[CharAttributes]]: ...
    def get_text_blink_mode(self) -> TextBlinkMode: ...
    def get_text_include_trailing_spaces(
        self, is_selected: Optional[Callable[..., bool]] = None, *user_data: Any
    ) -> Tuple[str, list[CharAttributes]]: ...
    def get_text_range(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int,
        is_selected: Optional[Callable[..., bool]] = None,
        *user_data: Any,
    ) -> Tuple[Optional[str], list[CharAttributes]]: ...
    def get_text_range_format(
        self, format: Format, start_row: int, start_col: int, end_row: int, end_col: int
    ) -> Tuple[Optional[str], int]: ...
    def get_text_selected(self, format: Format) -> Optional[str]: ...
    def get_text_selected_full(self, format: Format) -> Tuple[Optional[str], int]: ...
    def get_window_title(self) -> Optional[str]: ...
    def get_word_char_exceptions(self) -> Optional[str]: ...
    def hyperlink_check_event(self, event: Gdk.Event) -> Optional[str]: ...
    def match_add_gregex(
        self, gregex: GLib.Regex, gflags: GLib.RegexMatchFlags
    ) -> int: ...
    def match_add_regex(self, regex: Regex, flags: int) -> int: ...
    def match_check(self, column: int, row: int) -> Tuple[Optional[str], int]: ...
    def match_check_event(self, event: Gdk.Event) -> Tuple[Optional[str], int]: ...
    def match_remove(self, tag: int) -> None: ...
    def match_remove_all(self) -> None: ...
    def match_set_cursor(
        self, tag: int, cursor: Optional[Gdk.Cursor] = None
    ) -> None: ...
    def match_set_cursor_name(self, tag: int, cursor_name: str) -> None: ...
    def match_set_cursor_type(self, tag: int, cursor_type: Gdk.CursorType) -> None: ...
    @classmethod
    def new(cls) -> Terminal: ...
    def paste_clipboard(self) -> None: ...
    def paste_primary(self) -> None: ...
    def paste_text(self, text: str) -> None: ...
    def pty_new_sync(
        self, flags: PtyFlags, cancellable: Optional[Gio.Cancellable] = None
    ) -> Pty: ...
    def reset(self, clear_tabstops: bool, clear_history: bool) -> None: ...
    def search_find_next(self) -> bool: ...
    def search_find_previous(self) -> bool: ...
    def search_get_gregex(self) -> GLib.Regex: ...
    def search_get_regex(self) -> Regex: ...
    def search_get_wrap_around(self) -> bool: ...
    def search_set_gregex(
        self, gregex: Optional[GLib.Regex], gflags: GLib.RegexMatchFlags
    ) -> None: ...
    def search_set_regex(self, regex: Optional[Regex], flags: int) -> None: ...
    def search_set_wrap_around(self, wrap_around: bool) -> None: ...
    def select_all(self) -> None: ...
    def set_allow_bold(self, allow_bold: bool) -> None: ...
    def set_allow_hyperlink(self, allow_hyperlink: bool) -> None: ...
    def set_audible_bell(self, is_audible: bool) -> None: ...
    def set_backspace_binding(self, binding: EraseBinding) -> None: ...
    def set_bold_is_bright(self, bold_is_bright: bool) -> None: ...
    def set_cell_height_scale(self, scale: float) -> None: ...
    def set_cell_width_scale(self, scale: float) -> None: ...
    def set_cjk_ambiguous_width(self, width: int) -> None: ...
    def set_clear_background(self, setting: bool) -> None: ...
    def set_color_background(self, background: Gdk.RGBA) -> None: ...
    def set_color_bold(self, bold: Optional[Gdk.RGBA] = None) -> None: ...
    def set_color_cursor(
        self, cursor_background: Optional[Gdk.RGBA] = None
    ) -> None: ...
    def set_color_cursor_foreground(
        self, cursor_foreground: Optional[Gdk.RGBA] = None
    ) -> None: ...
    def set_color_foreground(self, foreground: Gdk.RGBA) -> None: ...
    def set_color_highlight(
        self, highlight_background: Optional[Gdk.RGBA] = None
    ) -> None: ...
    def set_color_highlight_foreground(
        self, highlight_foreground: Optional[Gdk.RGBA] = None
    ) -> None: ...
    def set_colors(
        self,
        foreground: Optional[Gdk.RGBA] = None,
        background: Optional[Gdk.RGBA] = None,
        palette: Optional[Sequence[Gdk.RGBA]] = None,
    ) -> None: ...
    def set_cursor_blink_mode(self, mode: CursorBlinkMode) -> None: ...
    def set_cursor_shape(self, shape: CursorShape) -> None: ...
    def set_default_colors(self) -> None: ...
    def set_delete_binding(self, binding: EraseBinding) -> None: ...
    def set_enable_bidi(self, enable_bidi: bool) -> None: ...
    def set_enable_fallback_scrolling(self, enable: bool) -> None: ...
    def set_enable_shaping(self, enable_shaping: bool) -> None: ...
    def set_enable_sixel(self, enabled: bool) -> None: ...
    def set_encoding(self, codeset: Optional[str] = None) -> bool: ...
    def set_font(self, font_desc: Optional[Pango.FontDescription] = None) -> None: ...
    def set_font_options(
        self, font_options: Optional[cairo.FontOptions] = None
    ) -> None: ...
    def set_font_scale(self, scale: float) -> None: ...
    def set_geometry_hints_for_window(self, window: Gtk.Window) -> None: ...
    def set_input_enabled(self, enabled: bool) -> None: ...
    def set_mouse_autohide(self, setting: bool) -> None: ...
    def set_pty(self, pty: Optional[Pty] = None) -> None: ...
    def set_rewrap_on_resize(self, rewrap: bool) -> None: ...
    def set_scroll_on_keystroke(self, scroll: bool) -> None: ...
    def set_scroll_on_output(self, scroll: bool) -> None: ...
    def set_scroll_unit_is_pixels(self, enable: bool) -> None: ...
    def set_scrollback_lines(self, lines: int) -> None: ...
    def set_size(self, columns: int, rows: int) -> None: ...
    def set_text_blink_mode(self, text_blink_mode: TextBlinkMode) -> None: ...
    def set_word_char_exceptions(self, exceptions: str) -> None: ...
    def spawn_async(
        self,
        pty_flags: PtyFlags,
        working_directory: Optional[str],
        argv: Sequence[str],
        envv: Optional[Sequence[str]],
        spawn_flags: GLib.SpawnFlags,
        child_setup: Optional[Callable[..., None]],
        timeout: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def spawn_sync(
        self,
        pty_flags: PtyFlags,
        working_directory: Optional[str],
        argv: Sequence[str],
        envv: Optional[Sequence[str]],
        spawn_flags: GLib.SpawnFlags,
        child_setup: Optional[Callable[..., None]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        *child_setup_data: Any,
    ) -> Tuple[bool, int]: ...
    def spawn_with_fds_async(
        self,
        pty_flags: PtyFlags,
        working_directory: Optional[str],
        argv: Sequence[str],
        envv: Optional[Sequence[str]],
        fds: Optional[Sequence[int]],
        map_fds: Optional[Sequence[int]],
        spawn_flags: GLib.SpawnFlags,
        child_setup: Optional[Callable[..., None]],
        timeout: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def unselect_all(self) -> None: ...
    def watch_child(self, child_pid: int) -> None: ...
    def write_contents_sync(
        self,
        stream: Gio.OutputStream,
        flags: WriteFlags,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> bool: ...

class TerminalClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TerminalClass()
    """

    parent_class: Gtk.WidgetClass = ...
    eof: Callable[[Terminal], None] = ...
    child_exited: Callable[[Terminal, int], None] = ...
    encoding_changed: Callable[[Terminal], None] = ...
    char_size_changed: Callable[[Terminal, int, int], None] = ...
    window_title_changed: Callable[[Terminal], None] = ...
    icon_title_changed: Callable[[Terminal], None] = ...
    selection_changed: Callable[[Terminal], None] = ...
    contents_changed: Callable[[Terminal], None] = ...
    cursor_moved: Callable[[Terminal], None] = ...
    commit: Callable[[Terminal, str, int], None] = ...
    deiconify_window: Callable[[Terminal], None] = ...
    iconify_window: Callable[[Terminal], None] = ...
    raise_window: Callable[[Terminal], None] = ...
    lower_window: Callable[[Terminal], None] = ...
    refresh_window: Callable[[Terminal], None] = ...
    restore_window: Callable[[Terminal], None] = ...
    maximize_window: Callable[[Terminal], None] = ...
    resize_window: Callable[[Terminal, int, int], None] = ...
    move_window: Callable[[Terminal, int, int], None] = ...
    increase_font_size: Callable[[Terminal], None] = ...
    decrease_font_size: Callable[[Terminal], None] = ...
    text_modified: Callable[[Terminal], None] = ...
    text_inserted: Callable[[Terminal], None] = ...
    text_deleted: Callable[[Terminal], None] = ...
    text_scrolled: Callable[[Terminal, int], None] = ...
    copy_clipboard: Callable[[Terminal], None] = ...
    paste_clipboard: Callable[[Terminal], None] = ...
    bell: Callable[[Terminal], None] = ...
    _extra_padding: list[None] = ...
    _padding: list[None] = ...
    priv: TerminalClassPrivate = ...

class TerminalClassPrivate(GObject.GPointer): ...

class FeatureFlags(GObject.GFlags):
    FLAGS_MASK = 18446744073709551615
    FLAG_BIDI = 1
    FLAG_ICU = 2
    FLAG_SIXEL = 8
    FLAG_SYSTEMD = 4

class PtyFlags(GObject.GFlags):
    DEFAULT = 0
    NO_CTTY = 64
    NO_FALLBACK = 16
    NO_HELPER = 8
    NO_LASTLOG = 1
    NO_SESSION = 32
    NO_UTMP = 2
    NO_WTMP = 4

class Align(GObject.GEnum):
    CENTER = 1
    END = 3
    START = 0

class CursorBlinkMode(GObject.GEnum):
    OFF = 2
    ON = 1
    SYSTEM = 0

class CursorShape(GObject.GEnum):
    BLOCK = 0
    IBEAM = 1
    UNDERLINE = 2

class EraseBinding(GObject.GEnum):
    ASCII_BACKSPACE = 1
    ASCII_DELETE = 2
    AUTO = 0
    DELETE_SEQUENCE = 3
    TTY = 4

class Format(GObject.GEnum):
    HTML = 2
    TEXT = 1

class PtyError(GObject.GEnum):
    PTY98_FAILED = 1
    PTY_HELPER_FAILED = 0
    @staticmethod
    def quark() -> int: ...

class RegexError(GObject.GEnum):
    INCOMPATIBLE = 2147483646
    NOT_SUPPORTED = 2147483647
    @staticmethod
    def quark() -> int: ...

class TextBlinkMode(GObject.GEnum):
    ALWAYS = 3
    FOCUSED = 1
    NEVER = 0
    UNFOCUSED = 2

class WriteFlags(GObject.GEnum):
    DEFAULT = 0
