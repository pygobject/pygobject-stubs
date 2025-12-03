import typing

from gi.repository import Gio
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import GtkSource
from typing_extensions import Self

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "Spelling"
_version: str = "1"

def init() -> None: ...

class Checker(GObject.Object):
    """
    :Constructors:

    ::

        Checker(**properties)
        new(provider:Spelling.Provider=None, language:str=None) -> Spelling.Checker

    Object SpellingChecker

    Properties from SpellingChecker:
      language -> gchararray: language
      provider -> SpellingProvider: provider

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        language: typing.Optional[str]
        provider: Provider

    props: Props = ...
    def __init__(self, language: str = ..., provider: Provider = ...) -> None: ...
    def add_word(self, word: str) -> None: ...
    def check_word(self, word: str, word_len: int) -> bool: ...
    @staticmethod
    def get_default() -> Checker: ...
    def get_extra_word_chars(self) -> str: ...
    def get_language(self) -> typing.Optional[str]: ...
    def get_provider(self) -> Provider: ...
    def ignore_word(self, word: str) -> None: ...
    def list_corrections(self, word: str) -> typing.Optional[list[str]]: ...
    @classmethod
    def new(
        cls,
        provider: typing.Optional[Provider] = None,
        language: typing.Optional[str] = None,
    ) -> Checker: ...
    def set_language(self, language: str) -> None: ...

class CheckerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CheckerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Dictionary(GObject.Object):
    """
    :Constructors:

    ::

        Dictionary(**properties)

    Object SpellingDictionary

    Properties from SpellingDictionary:
      code -> gchararray: code

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        code: typing.Optional[str]

    props: Props = ...
    def __init__(self, code: str = ...) -> None: ...
    def add_word(self, word: str) -> None: ...
    def contains_word(self, word: str, word_len: int) -> bool: ...
    def get_code(self) -> typing.Optional[str]: ...
    def get_extra_word_chars(self) -> str: ...
    def ignore_word(self, word: str) -> None: ...
    def list_corrections(
        self, word: str, word_len: int
    ) -> typing.Optional[list[str]]: ...

class DictionaryClass(GObject.GPointer): ...

class Language(GObject.Object):
    """
    :Constructors:

    ::

        Language(**properties)

    Object SpellingLanguage

    Properties from SpellingLanguage:
      code -> gchararray: code
      group -> gchararray: group
      name -> gchararray: name

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        code: typing.Optional[str]
        group: typing.Optional[str]
        name: typing.Optional[str]

    props: Props = ...
    def __init__(self, code: str = ..., group: str = ..., name: str = ...) -> None: ...
    def get_code(self) -> typing.Optional[str]: ...
    def get_group(self) -> typing.Optional[str]: ...
    def get_name(self) -> typing.Optional[str]: ...

class LanguageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LanguageClass()
    """

    parent_class: GObject.ObjectClass = ...

class Provider(GObject.Object):
    """
    :Constructors:

    ::

        Provider(**properties)

    Object SpellingProvider

    Properties from SpellingProvider:
      display-name -> gchararray: Display Name
        Display Name

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        display_name: typing.Optional[str]

    props: Props = ...
    def __init__(self, display_name: str = ...) -> None: ...
    @staticmethod
    def get_default() -> Provider: ...
    def get_default_code(self) -> typing.Optional[str]: ...
    def get_display_name(self) -> typing.Optional[str]: ...
    def list_languages(self) -> Gio.ListModel: ...
    def load_dictionary(self, language: str) -> typing.Optional[Dictionary]: ...
    def supports_language(self, language: str) -> bool: ...

class ProviderClass(GObject.GPointer): ...

class TextBufferAdapter(GObject.Object, Gio.ActionGroup):
    """
    :Constructors:

    ::

        TextBufferAdapter(**properties)
        new(buffer:GtkSource.Buffer, checker:Spelling.Checker) -> Spelling.TextBufferAdapter

    Object SpellingTextBufferAdapter

    Properties from SpellingTextBufferAdapter:
      buffer -> GtkSourceBuffer: buffer
      checker -> SpellingChecker: checker
      enabled -> gboolean: enabled
      language -> gchararray: language

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        buffer: typing.Optional[GtkSource.Buffer]
        checker: typing.Optional[Checker]
        enabled: bool
        language: typing.Optional[str]

    props: Props = ...
    def __init__(
        self,
        buffer: GtkSource.Buffer = ...,
        checker: Checker = ...,
        enabled: bool = ...,
        language: str = ...,
    ) -> None: ...
    def get_buffer(self) -> typing.Optional[GtkSource.Buffer]: ...
    def get_checker(self) -> typing.Optional[Checker]: ...
    def get_enabled(self) -> bool: ...
    def get_language(self) -> typing.Optional[str]: ...
    def get_menu_model(self) -> Gio.MenuModel: ...
    def get_tag(self) -> typing.Optional[Gtk.TextTag]: ...
    def invalidate_all(self) -> None: ...
    @classmethod
    def new(cls, buffer: GtkSource.Buffer, checker: Checker) -> TextBufferAdapter: ...
    def set_checker(self, checker: Checker) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_language(self, language: str) -> None: ...
    def update_corrections(self) -> None: ...

class TextBufferAdapterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TextBufferAdapterClass()
    """

    parent_class: GObject.ObjectClass = ...
