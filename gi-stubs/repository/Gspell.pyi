from typing import Optional

from gi.repository import GObject
from gi.repository import Gtk

_namespace: str = ...
_version: str = ...

def checker_error_quark() -> int: ...
def language_get_available() -> list[Language]: ...
def language_get_default() -> Optional[Language]: ...
def language_lookup(language_code: str) -> Optional[Language]: ...

class Checker(GObject.Object):
    parent_instance = ...

    def add_word_to_personal(self, word: str, word_length: int) -> None: ...
    def add_word_to_session(self, word: str, word_length: int) -> None: ...
    def check_word(self, word: str, word_length: int) -> bool: ...
    def clear_session(self) -> None: ...
    def get_language(self) -> Optional[Language]: ...
    def get_suggestions(self, word: str, word_length: int) -> list[str]: ...
    @classmethod
    def new(cls, language: Optional[Language]) -> Checker: ...
    def set_correction(
        self, word: str, word_length: int, replacement: str, replacement_length: int
    ) -> None: ...
    def set_language(self, language: Optional[Language]) -> None: ...
    def do_session_cleared(self) -> None: ...
    def do_word_added_to_personal(self, word: str) -> None: ...
    def do_word_added_to_session(self, word: str) -> None: ...

class CheckerDialog(Gtk.Dialog):
    def get_spell_navigator(self) -> Navigator: ...

class Entry(GObject.Object):
    def basic_setup(self) -> None: ...
    def get_entry(self) -> Gtk.Entry: ...
    @classmethod
    def get_from_gtk_entry(cls, gtk_entry: Gtk.Entry) -> Entry: ...
    def get_inline_spell_checking(self) -> bool: ...
    def set_inline_spell_checking(self, enable: bool) -> None: ...

class EntryBuffer(GObject.Object):
    def get_buffer(self) -> EntryBuffer: ...
    @classmethod
    def get_from_gtk_entry_buffer(cls, gtk_buffer: Gtk.EntryBuffer) -> EntryBuffer: ...
    def get_spell_checker(self) -> Checker: ...
    def set_spell_checker(self, spell_checker: Optional[Checker]) -> None: ...

class Language:
    def compare(self, language_b: Language) -> int: ...
    def free(self) -> None: ...
    def get_available(cls) -> list[Language]: ...
    def get_code(self) -> str: ...
    @classmethod
    def get_default(cls) -> Language: ...
    def get_name(self) -> str: ...
    @classmethod
    def lookup(cls, language_code: str) -> Optional[Language]: ...

class LanguageChooser(GObject.GInterface):
    def get_language(self) -> Optional[Language]: ...
    def get_language_code(self) -> str: ...
    def set_language(self, language: Optional[Language]) -> None: ...
    def set_language_code(self, language_code: Optional[str]) -> None: ...

class LanguageChooserButton(Gtk.Button): ...
class LanguageChooserDialog(Gtk.Dialog, LanguageChooser): ...

class LanguageChooserInterface:
    get_language_full: object = ...
    parent_interface: GObject.TypeInterface = ...
    set_language: object = ...

class Navigator(GObject.GInterface):
    def change(self, word: str, change_to: str) -> None: ...
    def change_all(self, word: str, change_to: str) -> None: ...
    def goto_next(self) -> tuple[bool, str, Checker]: ...

class NavigatorInterface:
    change: object = ...
    change_all: object = ...
    goto_next: object = ...
    parent_interface: GObject.TypeInterface = ...

class NavigatorTextView(GObject.Object, Navigator):
    parent_instance = ...

    def get_view(self) -> Gtk.TextView: ...
    @classmethod
    def new(cls, view: Gtk.TextView) -> Navigator: ...

class TextBuffer(GObject.Object):
    def get_buffer(self) -> Gtk.TextBuffer: ...
    @classmethod
    def get_from_gtk_text_buffer(cls, gtk_buffer: Gtk.TextBuffer) -> TextBuffer: ...
    def get_spell_checker(self) -> Optional[Checker]: ...
    def set_spell_checker(self, spell_checker: Optional[Checker]) -> None: ...

class TextView(GObject.Object):
    parent_instance = ...

    def basic_setup(self) -> None: ...
    def get_enable_language_menu(self) -> bool: ...
    @classmethod
    def get_from_gtk_text_view(cls, gtk_view: Gtk.TextView) -> TextView: ...
    def get_inline_spell_checking(self) -> bool: ...
    def get_view(self) -> Gtk.TextView: ...
    def set_enable_language_menu(self, enable_language_menu: bool) -> None: ...
    def set_inline_spell_checking(self, enable: bool) -> None: ...

class CheckerError(GObject.GEnum):
    DICTIONARY: int = ...
    NO_LANGUAGE_SET: int = ...
    quark: int = ...
