from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import Gio
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import GtkSource

T = TypeVar("T")

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

    class Props:
        language: Optional[str]
        provider: Provider

    props: Props = ...
    def __init__(self, language: str = ..., provider: Provider = ...) -> None: ...
    def add_word(self, word: str) -> None: ...
    def check_word(self, word: str, word_len: int) -> bool: ...
    @staticmethod
    def get_default() -> Checker: ...
    def get_extra_word_chars(self) -> str: ...
    def get_language(self) -> Optional[str]: ...
    def get_provider(self) -> Provider: ...
    def ignore_word(self, word: str) -> None: ...
    def list_corrections(self, word: str) -> Optional[list[str]]: ...
    @classmethod
    def new(
        cls,
        provider: Optional[Provider] = None,
        language: Optional[str] = None,
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

    class Props:
        code: Optional[str]

    props: Props = ...
    def __init__(self, code: str = ...) -> None: ...
    def add_word(self, word: str) -> None: ...
    def contains_word(self, word: str, word_len: int) -> bool: ...
    def get_code(self) -> Optional[str]: ...
    def get_extra_word_chars(self) -> str: ...
    def ignore_word(self, word: str) -> None: ...
    def list_corrections(self, word: str, word_len: int) -> Optional[list[str]]: ...

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

    class Props:
        code: Optional[str]
        group: Optional[str]
        name: Optional[str]

    props: Props = ...
    def __init__(self, code: str = ..., group: str = ..., name: str = ...) -> None: ...
    def get_code(self) -> Optional[str]: ...
    def get_group(self) -> Optional[str]: ...
    def get_name(self) -> Optional[str]: ...

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

    class Props:
        display_name: Optional[str]

    props: Props = ...
    def __init__(self, display_name: str = ...) -> None: ...
    @staticmethod
    def get_default() -> Provider: ...
    def get_default_code(self) -> Optional[str]: ...
    def get_display_name(self) -> Optional[str]: ...
    def list_languages(self) -> Gio.ListModel: ...
    def load_dictionary(self, language: str) -> Optional[Dictionary]: ...
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

    class Props:
        buffer: Optional[GtkSource.Buffer]
        checker: Optional[Checker]
        enabled: bool
        language: Optional[str]

    props: Props = ...
    def __init__(
        self,
        buffer: GtkSource.Buffer = ...,
        checker: Checker = ...,
        enabled: bool = ...,
        language: str = ...,
    ) -> None: ...
    def get_buffer(self) -> Optional[GtkSource.Buffer]: ...
    def get_checker(self) -> Optional[Checker]: ...
    def get_enabled(self) -> bool: ...
    def get_language(self) -> Optional[str]: ...
    def get_menu_model(self) -> Gio.MenuModel: ...
    def get_tag(self) -> Optional[Gtk.TextTag]: ...
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
