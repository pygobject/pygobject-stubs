import typing

from gi.repository import Gio
from gi.repository import GObject

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "GioWin32"
_version: str = "2.0"

def registry_settings_backend_new(
    registry_key: typing.Optional[str] = None,
) -> Gio.SettingsBackend: ...

class InputStream(Gio.InputStream):
    """
    :Constructors:

    ::

        InputStream(**properties)
        new(handle=None, close_handle:bool) -> Gio.InputStream

    Object GWin32InputStream

    Properties from GWin32InputStream:
      handle -> gpointer: handle
      close-handle -> gboolean: close-handle

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: Gio.InputStream = ...
    priv: InputStreamPrivate = ...
    @staticmethod
    def get_close_handle(stream: InputStream) -> bool: ...
    @staticmethod
    def get_handle(stream: InputStream) -> None: ...
    def new(
        handle: typing.Any, close_handle: bool
    ) -> InputStream: ...  # FIXME Function
    @staticmethod
    def set_close_handle(stream: InputStream, close_handle: bool) -> None: ...

class InputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputStreamClass()
    """

    parent_class: Gio.InputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class InputStreamPrivate(GObject.GPointer): ...

class NetworkMonitor(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkMonitor()
    """

    parent_instance: None = ...
    priv: NetworkMonitorPrivate = ...

class NetworkMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkMonitorClass()
    """

    parent_class: None = ...

class NetworkMonitorPrivate(GObject.GPointer): ...

class OutputStream(Gio.OutputStream):
    """
    :Constructors:

    ::

        OutputStream(**properties)
        new(handle=None, close_handle:bool) -> Gio.OutputStream

    Object GWin32OutputStream

    Properties from GWin32OutputStream:
      handle -> gpointer: handle
      close-handle -> gboolean: close-handle

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: Gio.OutputStream = ...
    priv: OutputStreamPrivate = ...
    @staticmethod
    def get_close_handle(stream: OutputStream) -> bool: ...
    @staticmethod
    def get_handle(stream: OutputStream) -> None: ...
    def new(
        handle: typing.Any, close_handle: bool
    ) -> OutputStream: ...  # FIXME Function
    @staticmethod
    def set_close_handle(stream: OutputStream, close_handle: bool) -> None: ...

class OutputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OutputStreamClass()
    """

    parent_class: Gio.OutputStreamClass = ...
    _g_reserved1: None = ...
    _g_reserved2: None = ...
    _g_reserved3: None = ...
    _g_reserved4: None = ...
    _g_reserved5: None = ...

class OutputStreamPrivate(GObject.GPointer): ...
