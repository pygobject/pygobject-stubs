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

from gi.repository import Atk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk

_lock = ...  # FIXME Constant
_namespace: str = "Gspell"
_version: str = "1"

def checker_error_quark() -> int: ...
def language_get_available() -> list[Language]: ...
def language_get_default() -> Optional[Language]: ...
def language_lookup(language_code: str) -> Optional[Language]: ...

class Checker(GObject.Object):
    """
    :Constructors:

    ::

        Checker(**properties)
        new(language:Gspell.Language=None) -> Gspell.Checker

    Object GspellChecker

    Signals from GspellChecker:
      word-added-to-personal (gchararray)
      word-added-to-session (gchararray)
      session-cleared ()

    Properties from GspellChecker:
      language -> GspellLanguage: Language


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        language: Optional[Language]
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(self, language: Optional[Language] = ...): ...
    def add_word_to_personal(self, word: str, word_length: int) -> None: ...
    def add_word_to_session(self, word: str, word_length: int) -> None: ...
    def check_word(self, word: str, word_length: int) -> bool: ...
    def clear_session(self) -> None: ...
    def do_session_cleared(self) -> None: ...
    def do_word_added_to_personal(self, word: str) -> None: ...
    def do_word_added_to_session(self, word: str) -> None: ...
    def get_language(self) -> Optional[Language]: ...
    def get_suggestions(self, word: str, word_length: int) -> list[str]: ...
    @classmethod
    def new(cls, language: Optional[Language] = None) -> Checker: ...
    def set_correction(
        self, word: str, word_length: int, replacement: str, replacement_length: int
    ) -> None: ...
    def set_language(self, language: Optional[Language] = None) -> None: ...

class CheckerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CheckerClass()
    """

    parent_class: GObject.ObjectClass = ...
    word_added_to_personal: Callable[[Checker, str], None] = ...
    word_added_to_session: Callable[[Checker, str], None] = ...
    session_cleared: Callable[[Checker], None] = ...
    padding: list[None] = ...

class CheckerDialog(Gtk.Dialog, Atk.ImplementorIface, Gtk.Buildable):
    """
    :Constructors:

    ::

        CheckerDialog(**properties)
        new(parent:Gtk.Window, navigator:Gspell.Navigator) -> Gtk.Widget

    Object GspellCheckerDialog

    Properties from GspellCheckerDialog:
      spell-navigator -> GspellNavigator: Spell Navigator


    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximisation
        If this window's titlebar should be hidden when the window is maximised
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialogue
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximised
        Whether the window is maximised

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

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
        spell_navigator: Navigator
        use_header_bar: int
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
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
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Dialog = ...
    def __init__(
        self,
        spell_navigator: Navigator = ...,
        use_header_bar: int = ...,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
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
    ): ...
    def get_spell_navigator(self) -> Navigator: ...
    @classmethod
    def new(cls, parent: Gtk.Window, navigator: Navigator) -> CheckerDialog: ...

class CheckerDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CheckerDialogClass()
    """

    parent_class: Gtk.DialogClass = ...
    padding: list[None] = ...

class Entry(GObject.Object):
    """
    :Constructors:

    ::

        Entry(**properties)

    Object GspellEntry

    Properties from GspellEntry:
      entry -> GtkEntry: Entry

      inline-spell-checking -> gboolean: Inline Spell Checking


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        entry: Gtk.Entry
        inline_spell_checking: bool
    props: Props = ...
    def __init__(self, entry: Gtk.Entry = ..., inline_spell_checking: bool = ...): ...
    def basic_setup(self) -> None: ...
    def get_entry(self) -> Gtk.Entry: ...
    @staticmethod
    def get_from_gtk_entry(gtk_entry: Gtk.Entry) -> Entry: ...
    def get_inline_spell_checking(self) -> bool: ...
    def set_inline_spell_checking(self, enable: bool) -> None: ...

class EntryBuffer(GObject.Object):
    """
    :Constructors:

    ::

        EntryBuffer(**properties)

    Object GspellEntryBuffer

    Properties from GspellEntryBuffer:
      buffer -> GtkEntryBuffer: Buffer

      spell-checker -> GspellChecker: Spell Checker


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Gtk.EntryBuffer
        spell_checker: Optional[Checker]
    props: Props = ...
    def __init__(
        self, buffer: Gtk.EntryBuffer = ..., spell_checker: Optional[Checker] = ...
    ): ...
    def get_buffer(self) -> Gtk.EntryBuffer: ...
    @staticmethod
    def get_from_gtk_entry_buffer(gtk_buffer: Gtk.EntryBuffer) -> EntryBuffer: ...
    def get_spell_checker(self) -> Optional[Checker]: ...
    def set_spell_checker(self, spell_checker: Optional[Checker] = None) -> None: ...

class EntryBufferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EntryBufferClass()
    """

    parent_class: GObject.ObjectClass = ...

class EntryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EntryClass()
    """

    parent_class: GObject.ObjectClass = ...

class Language(GObject.GBoxed):
    def compare(self, language_b: Language) -> int: ...
    def copy(self) -> Language: ...
    def free(self) -> None: ...
    @staticmethod
    def get_available() -> list[Language]: ...
    def get_code(self) -> str: ...
    @staticmethod
    def get_default() -> Optional[Language]: ...
    def get_name(self) -> str: ...
    @staticmethod
    def lookup(language_code: str) -> Optional[Language]: ...

class LanguageChooser(GObject.GInterface):
    """
    Interface GspellLanguageChooser

    Signals from GObject:
      notify (GParam)
    """

    def get_language(self) -> Optional[Language]: ...
    def get_language_code(self) -> str: ...
    def set_language(self, language: Optional[Language] = None) -> None: ...
    def set_language_code(self, language_code: Optional[str] = None) -> None: ...

class LanguageChooserButton(
    Gtk.Button,
    Atk.ImplementorIface,
    LanguageChooser,
    Gtk.Actionable,
    Gtk.Activatable,
    Gtk.Buildable,
):
    """
    :Constructors:

    ::

        LanguageChooserButton(**properties)
        new(current_language:Gspell.Language=None) -> Gtk.Widget

    Object GspellLanguageChooserButton

    Signals from GtkButton:
      activate ()
      pressed ()
      released ()
      clicked ()
      enter ()
      leave ()

    Properties from GtkButton:
      label -> gchararray: Label
        Text of the label widget inside the button, if the button contains a label widget
      image -> GtkWidget: Image widget
        Child widget to appear next to the button text
      relief -> GtkReliefStyle: Border relief
        The border relief style
      use-underline -> gboolean: Use underline
        If set, an underline in the text indicates the next character should be used for the mnemonic accelerator key
      use-stock -> gboolean: Use stock
        If set, the label is used to pick a stock item instead of being displayed
      xalign -> gfloat: Horizontal alignment for child
        Horizontal position of child in available space. 0.0 is left aligned, 1.0 is right aligned
      yalign -> gfloat: Vertical alignment for child
        Vertical position of child in available space. 0.0 is top aligned, 1.0 is bottom aligned
      image-position -> GtkPositionType: Image position
        The position of the image relative to the text
      always-show-image -> gboolean: Always show image
        Whether the image will always be shown

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

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
        always_show_image: bool
        image: Optional[Gtk.Widget]
        image_position: Gtk.PositionType
        label: str
        relief: Gtk.ReliefStyle
        use_stock: bool
        use_underline: bool
        xalign: float
        yalign: float
        border_width: int
        resize_mode: Gtk.ResizeMode
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
        language: Optional[Language]
        language_code: str
        action_name: Optional[str]
        action_target: GLib.Variant
        related_action: Gtk.Action
        use_action_appearance: bool
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Button = ...
    def __init__(
        self,
        always_show_image: bool = ...,
        image: Optional[Gtk.Widget] = ...,
        image_position: Gtk.PositionType = ...,
        label: str = ...,
        relief: Gtk.ReliefStyle = ...,
        use_stock: bool = ...,
        use_underline: bool = ...,
        xalign: float = ...,
        yalign: float = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
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
        language: Optional[Language] = ...,
        language_code: Optional[str] = ...,
        action_name: Optional[str] = ...,
        action_target: GLib.Variant = ...,
        related_action: Gtk.Action = ...,
        use_action_appearance: bool = ...,
    ): ...
    @classmethod
    def new(
        cls, current_language: Optional[Language] = None
    ) -> LanguageChooserButton: ...

class LanguageChooserButtonClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageChooserButtonClass()
    """

    parent_class: Gtk.ButtonClass = ...
    padding: list[None] = ...

class LanguageChooserDialog(
    Gtk.Dialog, Atk.ImplementorIface, LanguageChooser, Gtk.Buildable
):
    """
    :Constructors:

    ::

        LanguageChooserDialog(**properties)
        new(parent:Gtk.Window, current_language:Gspell.Language=None, flags:Gtk.DialogFlags) -> Gtk.Widget

    Object GspellLanguageChooserDialog

    Signals from GtkDialog:
      response (gint)
      close ()

    Properties from GtkDialog:
      use-header-bar -> gint: Use Header Bar
        Use Header Bar for actions.

    Signals from GtkWindow:
      keys-changed ()
      set-focus (GtkWidget)
      activate-focus ()
      activate-default ()
      enable-debugging (gboolean) -> gboolean

    Properties from GtkWindow:
      type -> GtkWindowType: Window Type
        The type of the window
      title -> gchararray: Window Title
        The title of the window
      role -> gchararray: Window Role
        Unique identifier for the window to be used when restoring a session
      resizable -> gboolean: Resizable
        If TRUE, users can resize the window
      modal -> gboolean: Modal
        If TRUE, the window is modal (other windows are not usable while this one is up)
      window-position -> GtkWindowPosition: Window Position
        The initial position of the window
      default-width -> gint: Default Width
        The default width of the window, used when initially showing the window
      default-height -> gint: Default Height
        The default height of the window, used when initially showing the window
      destroy-with-parent -> gboolean: Destroy with Parent
        If this window should be destroyed when the parent is destroyed
      hide-titlebar-when-maximized -> gboolean: Hide the titlebar during maximisation
        If this window's titlebar should be hidden when the window is maximised
      icon -> GdkPixbuf: Icon
        Icon for this window
      icon-name -> gchararray: Icon Name
        Name of the themed icon for this window
      screen -> GdkScreen: Screen
        The screen where this window will be displayed
      type-hint -> GdkWindowTypeHint: Type hint
        Hint to help the desktop environment understand what kind of window this is and how to treat it.
      skip-taskbar-hint -> gboolean: Skip taskbar
        TRUE if the window should not be in the task bar.
      skip-pager-hint -> gboolean: Skip pager
        TRUE if the window should not be in the pager.
      urgency-hint -> gboolean: Urgent
        TRUE if the window should be brought to the user's attention.
      accept-focus -> gboolean: Accept focus
        TRUE if the window should receive the input focus.
      focus-on-map -> gboolean: Focus on map
        TRUE if the window should receive the input focus when mapped.
      decorated -> gboolean: Decorated
        Whether the window should be decorated by the window manager
      deletable -> gboolean: Deletable
        Whether the window frame should have a close button
      gravity -> GdkGravity: Gravity
        The window gravity of the window
      transient-for -> GtkWindow: Transient for Window
        The transient parent of the dialogue
      attached-to -> GtkWidget: Attached to Widget
        The widget where the window is attached
      has-resize-grip -> gboolean: Resize grip
        Specifies whether the window should have a resize grip
      resize-grip-visible -> gboolean: Resize grip is visible
        Specifies whether the window's resize grip is visible.
      application -> GtkApplication: GtkApplication
        The GtkApplication for the window
      is-active -> gboolean: Is Active
        Whether the toplevel is the current active window
      has-toplevel-focus -> gboolean: Focus in Toplevel
        Whether the input focus is within this GtkWindow
      startup-id -> gchararray: Startup ID
        Unique startup identifier for the window used by startup-notification
      mnemonics-visible -> gboolean: Mnemonics Visible
        Whether mnemonics are currently visible in this window
      focus-visible -> gboolean: Focus Visible
        Whether focus rectangles are currently visible in this window
      is-maximized -> gboolean: Is maximised
        Whether the window is maximised

    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)

    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container

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
        use_header_bar: int
        accept_focus: bool
        application: Optional[Gtk.Application]
        attached_to: Optional[Gtk.Widget]
        decorated: bool
        default_height: int
        default_width: int
        deletable: bool
        destroy_with_parent: bool
        focus_on_map: bool
        focus_visible: bool
        gravity: Gdk.Gravity
        has_resize_grip: bool
        has_toplevel_focus: bool
        hide_titlebar_when_maximized: bool
        icon: Optional[GdkPixbuf.Pixbuf]
        icon_name: Optional[str]
        is_active: bool
        is_maximized: bool
        mnemonics_visible: bool
        modal: bool
        resizable: bool
        resize_grip_visible: bool
        role: Optional[str]
        screen: Gdk.Screen
        skip_pager_hint: bool
        skip_taskbar_hint: bool
        title: Optional[str]
        transient_for: Optional[Gtk.Window]
        type: Gtk.WindowType
        type_hint: Gdk.WindowTypeHint
        urgency_hint: bool
        window_position: Gtk.WindowPosition
        border_width: int
        resize_mode: Gtk.ResizeMode
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
        language: Optional[Language]
        language_code: str
        startup_id: str
        child: Gtk.Widget
    props: Props = ...
    parent_instance: Gtk.Dialog = ...
    def __init__(
        self,
        use_header_bar: int = ...,
        accept_focus: bool = ...,
        application: Optional[Gtk.Application] = ...,
        attached_to: Optional[Gtk.Widget] = ...,
        decorated: bool = ...,
        default_height: int = ...,
        default_width: int = ...,
        deletable: bool = ...,
        destroy_with_parent: bool = ...,
        focus_on_map: bool = ...,
        focus_visible: bool = ...,
        gravity: Gdk.Gravity = ...,
        has_resize_grip: bool = ...,
        hide_titlebar_when_maximized: bool = ...,
        icon: Optional[GdkPixbuf.Pixbuf] = ...,
        icon_name: Optional[str] = ...,
        mnemonics_visible: bool = ...,
        modal: bool = ...,
        resizable: bool = ...,
        role: str = ...,
        screen: Gdk.Screen = ...,
        skip_pager_hint: bool = ...,
        skip_taskbar_hint: bool = ...,
        startup_id: str = ...,
        title: str = ...,
        transient_for: Optional[Gtk.Window] = ...,
        type: Gtk.WindowType = ...,
        type_hint: Gdk.WindowTypeHint = ...,
        urgency_hint: bool = ...,
        window_position: Gtk.WindowPosition = ...,
        border_width: int = ...,
        child: Gtk.Widget = ...,
        resize_mode: Gtk.ResizeMode = ...,
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
        language: Optional[Language] = ...,
        language_code: Optional[str] = ...,
    ): ...
    @classmethod
    def new(
        cls,
        parent: Gtk.Window,
        current_language: Optional[Language],
        flags: Gtk.DialogFlags,
    ) -> LanguageChooserDialog: ...

class LanguageChooserDialogClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageChooserDialogClass()
    """

    parent_class: Gtk.DialogClass = ...
    padding: list[None] = ...

class LanguageChooserInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageChooserInterface()
    """

    parent_interface: GObject.TypeInterface = ...
    get_language_full: Callable[[LanguageChooser, bool], Language] = ...
    set_language: Callable[[LanguageChooser, Optional[Language]], None] = ...

class Navigator(GObject.GInterface):
    """
    Interface GspellNavigator

    Signals from GObject:
      notify (GParam)
    """

    def change(self, word: str, change_to: str) -> None: ...
    def change_all(self, word: str, change_to: str) -> None: ...
    def goto_next(self) -> Tuple[bool, str, Checker]: ...

class NavigatorInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        NavigatorInterface()
    """

    parent_interface: GObject.TypeInterface = ...
    goto_next: Callable[[Navigator], Tuple[bool, str, Checker]] = ...
    change: Callable[[Navigator, str, str], None] = ...
    change_all: Callable[[Navigator, str, str], None] = ...

class NavigatorTextView(GObject.InitiallyUnowned, Navigator):
    """
    :Constructors:

    ::

        NavigatorTextView(**properties)

    Object GspellNavigatorTextView

    Properties from GspellNavigatorTextView:
      view -> GtkTextView: View


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        view: Gtk.TextView
    props: Props = ...
    parent_instance: GObject.InitiallyUnowned = ...
    def __init__(self, view: Gtk.TextView = ...): ...
    def get_view(self) -> Gtk.TextView: ...
    @staticmethod
    def new(view: Gtk.TextView) -> Navigator: ...

class NavigatorTextViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NavigatorTextViewClass()
    """

    parent_class: GObject.InitiallyUnownedClass = ...
    padding: list[None] = ...

class TextBuffer(GObject.Object):
    """
    :Constructors:

    ::

        TextBuffer(**properties)

    Object GspellTextBuffer

    Properties from GspellTextBuffer:
      buffer -> GtkTextBuffer: Buffer

      spell-checker -> GspellChecker: Spell Checker


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        buffer: Gtk.TextBuffer
        spell_checker: Optional[Checker]
    props: Props = ...
    def __init__(
        self, buffer: Gtk.TextBuffer = ..., spell_checker: Optional[Checker] = ...
    ): ...
    def get_buffer(self) -> Gtk.TextBuffer: ...
    @staticmethod
    def get_from_gtk_text_buffer(gtk_buffer: Gtk.TextBuffer) -> TextBuffer: ...
    def get_spell_checker(self) -> Optional[Checker]: ...
    def set_spell_checker(self, spell_checker: Optional[Checker] = None) -> None: ...

class TextBufferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TextBufferClass()
    """

    parent_class: GObject.ObjectClass = ...

class TextView(GObject.Object):
    """
    :Constructors:

    ::

        TextView(**properties)

    Object GspellTextView

    Properties from GspellTextView:
      view -> GtkTextView: View

      inline-spell-checking -> gboolean: Inline Spell Checking

      enable-language-menu -> gboolean: Enable Language Menu


    Signals from GObject:
      notify (GParam)
    """

    class Props:
        enable_language_menu: bool
        inline_spell_checking: bool
        view: Gtk.TextView
    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        enable_language_menu: bool = ...,
        inline_spell_checking: bool = ...,
        view: Gtk.TextView = ...,
    ): ...
    def basic_setup(self) -> None: ...
    def get_enable_language_menu(self) -> bool: ...
    @staticmethod
    def get_from_gtk_text_view(gtk_view: Gtk.TextView) -> TextView: ...
    def get_inline_spell_checking(self) -> bool: ...
    def get_view(self) -> Gtk.TextView: ...
    def set_enable_language_menu(self, enable_language_menu: bool) -> None: ...
    def set_inline_spell_checking(self, enable: bool) -> None: ...

class TextViewClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TextViewClass()
    """

    parent_class: GObject.ObjectClass = ...
    padding: list[None] = ...

class CheckerError(GObject.GEnum):
    DICTIONARY = 0
    NO_LANGUAGE_SET = 1
    @staticmethod
    def quark() -> int: ...
