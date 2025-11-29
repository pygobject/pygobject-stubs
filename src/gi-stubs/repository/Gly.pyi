import typing

import enum

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "Gly"
_version: str = "2"

def loader_error_quark() -> int: ...
def memory_format_has_alpha(memory_format: MemoryFormat) -> bool: ...
def memory_format_is_premultiplied(memory_format: MemoryFormat) -> bool: ...

class Cicp(GObject.GBoxed):
    """
    :Constructors:

    ::

        Cicp()
    """

    color_primaries: int = ...
    transfer_characteristics: int = ...
    matrix_coefficients: int = ...
    video_full_range_flag: int = ...
    def copy(self) -> Cicp: ...
    def free(self) -> None: ...

class Creator(GObject.Object):
    """
    :Constructors:

    ::

        Creator(**properties)
        new(mime_type:str) -> Gly.Creator

    Object GlyCreator

    Properties from GlyCreator:
      sandbox-selector -> GlySandboxSelector: sandbox-selector
      mime-type -> gchararray: mime-type

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        mime_type: str
        sandbox_selector: SandboxSelector

    props: Props = ...
    def __init__(
        self, mime_type: str = ..., sandbox_selector: SandboxSelector = ...
    ) -> None: ...
    def add_frame(
        self, width: int, height: int, memory_format: MemoryFormat, texture: GLib.Bytes
    ) -> NewFrame: ...
    def add_frame_with_stride(
        self,
        width: int,
        height: int,
        stride: int,
        memory_format: MemoryFormat,
        texture: GLib.Bytes,
    ) -> NewFrame: ...
    def add_metadata_key_value(self, key: str, value: str) -> bool: ...
    def create(self) -> typing.Optional[EncodedImage]: ...
    def create_async(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def create_finish(self, result: Gio.AsyncResult) -> EncodedImage: ...
    @classmethod
    def new(cls, mime_type: str) -> Creator: ...
    def set_encoding_compression(self, compression: int) -> bool: ...
    def set_encoding_quality(self, quality: int) -> bool: ...
    def set_sandbox_selector(self, sandbox_selector: SandboxSelector) -> bool: ...

class CreatorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CreatorClass()
    """

    parent_class: GObject.ObjectClass = ...

class EncodedImage(GObject.Object):
    """
    :Constructors:

    ::

        EncodedImage(**properties)

    Object GlyEncodedImage

    Properties from GlyEncodedImage:
      data -> GBytes: data

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        data: GLib.Bytes

    props: Props = ...
    def get_data(self) -> GLib.Bytes: ...

class EncodedImageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EncodedImageClass()
    """

    parent_class: GObject.ObjectClass = ...

class Frame(GObject.Object):
    """
    :Constructors:

    ::

        Frame(**properties)

    Object GlyFrame

    Signals from GObject:
      notify (GParam)
    """
    def get_buf_bytes(self) -> GLib.Bytes: ...
    def get_color_cicp(self) -> typing.Optional[Cicp]: ...
    def get_delay(self) -> int: ...
    def get_height(self) -> int: ...
    def get_memory_format(self) -> MemoryFormat: ...
    def get_stride(self) -> int: ...
    def get_width(self) -> int: ...

class FrameClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameClass()
    """

    parent_class: GObject.ObjectClass = ...

class FrameRequest(GObject.Object):
    """
    :Constructors:

    ::

        FrameRequest(**properties)
        new() -> Gly.FrameRequest

    Object GlyFrameRequest

    Properties from GlyFrameRequest:
      scale-width -> guint: scale-width
      scale-height -> guint: scale-height
      loop-animation -> gboolean: loop-animation

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        loop_animation: bool
        scale_height: int
        scale_width: int

    props: Props = ...
    def __init__(self, loop_animation: bool = ...) -> None: ...
    @classmethod
    def new(cls) -> FrameRequest: ...
    def set_loop_animation(self, loop_animation: bool) -> None: ...
    def set_scale(self, width: int, height: int) -> None: ...

class FrameRequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FrameRequestClass()
    """

    parent_class: GObject.ObjectClass = ...

class Image(GObject.Object):
    """
    :Constructors:

    ::

        Image(**properties)

    Object GlyImage

    Signals from GObject:
      notify (GParam)
    """
    def get_height(self) -> int: ...
    def get_metadata_key_value(self, key: str) -> typing.Optional[str]: ...
    def get_metadata_keys(self) -> list[str]: ...
    def get_mime_type(self) -> str: ...
    def get_specific_frame(self, frame_request: FrameRequest) -> Frame: ...
    def get_specific_frame_async(
        self,
        frame_request: FrameRequest,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_specific_frame_finish(self, result: Gio.AsyncResult) -> Frame: ...
    def get_transformation_orientation(self) -> int: ...
    def get_width(self) -> int: ...
    def next_frame(self) -> Frame: ...
    def next_frame_async(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def next_frame_finish(self, result: Gio.AsyncResult) -> Frame: ...

class ImageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ImageClass()
    """

    parent_class: GObject.ObjectClass = ...

class Loader(GObject.Object):
    """
    :Constructors:

    ::

        Loader(**properties)
        new(file:Gio.File) -> Gly.Loader
        new_for_bytes(bytes:GLib.Bytes) -> Gly.Loader
        new_for_stream(stream:Gio.InputStream) -> Gly.Loader

    Object GlyLoader

    Properties from GlyLoader:
      file -> GFile: file
      stream -> GInputStream: stream
      bytes -> GBytes: bytes
      cancellable -> GCancellable: cancellable
      sandbox-selector -> GlySandboxSelector: sandbox-selector
      memory-format-selection -> GlyMemoryFormatSelection: memory-format-selection
      apply-transformation -> gboolean: apply-transformation

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        apply_transformation: bool
        bytes: GLib.Bytes
        cancellable: Gio.Cancellable
        file: Gio.File
        memory_format_selection: MemoryFormatSelection
        sandbox_selector: SandboxSelector
        stream: Gio.InputStream

    props: Props = ...
    def __init__(
        self,
        apply_transformation: bool = ...,
        bytes: GLib.Bytes = ...,
        cancellable: Gio.Cancellable = ...,
        file: Gio.File = ...,
        memory_format_selection: MemoryFormatSelection = ...,
        sandbox_selector: SandboxSelector = ...,
        stream: Gio.InputStream = ...,
    ) -> None: ...
    @staticmethod
    def get_mime_types() -> list[str]: ...
    @staticmethod
    def get_mime_types_async(
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def get_mime_types_finish(result: Gio.AsyncResult) -> list[str]: ...
    def load(self) -> Image: ...
    def load_async(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def load_finish(self, result: Gio.AsyncResult) -> Image: ...
    @classmethod
    def new(cls, file: Gio.File) -> Loader: ...
    @classmethod
    def new_for_bytes(cls, bytes: GLib.Bytes) -> Loader: ...
    @classmethod
    def new_for_stream(cls, stream: Gio.InputStream) -> Loader: ...
    def set_accepted_memory_formats(
        self, memory_format_selection: MemoryFormatSelection
    ) -> None: ...
    def set_apply_transformations(self, apply_transformations: bool) -> None: ...
    def set_sandbox_selector(self, sandbox_selector: SandboxSelector) -> None: ...

class LoaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LoaderClass()
    """

    parent_class: GObject.ObjectClass = ...

class NewFrame(GObject.Object):
    """
    :Constructors:

    ::

        NewFrame(**properties)

    Object GlyNewFrame

    Signals from GObject:
      notify (GParam)
    """
    def set_color_icc_profile(self, icc_profile: GLib.Bytes) -> bool: ...

class NewFrameClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NewFrameClass()
    """

    parent_class: GObject.ObjectClass = ...

class MemoryFormatSelection(enum.IntFlag):
    A8B8G8R8 = 64
    A8R8G8B8 = 16
    A8R8G8B8_PREMULTIPLIED = 2
    B8G8R8 = 256
    B8G8R8A8 = 8
    B8G8R8A8_PREMULTIPLIED = 1
    G16 = 4194304
    G16A16 = 2097152
    G16A16_PREMULTIPLIED = 1048576
    G8 = 524288
    G8A8 = 262144
    G8A8_PREMULTIPLIED = 131072
    R16G16B16 = 512
    R16G16B16A16 = 2048
    R16G16B16A16_FLOAT = 8192
    R16G16B16A16_PREMULTIPLIED = 1024
    R16G16B16_FLOAT = 4096
    R32G32B32A32_FLOAT = 65536
    R32G32B32A32_FLOAT_PREMULTIPLIED = 32768
    R32G32B32_FLOAT = 16384
    R8G8B8 = 128
    R8G8B8A8 = 32
    R8G8B8A8_PREMULTIPLIED = 4

class LoaderError(enum.IntEnum):
    FAILED = 0
    NO_MORE_FRAMES = 2
    UNKNOWN_IMAGE_FORMAT = 1
    @staticmethod
    def quark() -> int: ...

class MemoryFormat(enum.IntEnum):
    A8B8G8R8 = 6
    A8R8G8B8 = 4
    A8R8G8B8_PREMULTIPLIED = 1
    B8G8R8 = 8
    B8G8R8A8 = 3
    B8G8R8A8_PREMULTIPLIED = 0
    G16 = 22
    G16A16 = 21
    G16A16_PREMULTIPLIED = 20
    G8 = 19
    G8A8 = 18
    G8A8_PREMULTIPLIED = 17
    R16G16B16 = 9
    R16G16B16A16 = 11
    R16G16B16A16_FLOAT = 13
    R16G16B16A16_PREMULTIPLIED = 10
    R16G16B16_FLOAT = 12
    R32G32B32A32_FLOAT = 16
    R32G32B32A32_FLOAT_PREMULTIPLIED = 15
    R32G32B32_FLOAT = 14
    R8G8B8 = 7
    R8G8B8A8 = 5
    R8G8B8A8_PREMULTIPLIED = 2
    @staticmethod
    def has_alpha(memory_format: MemoryFormat) -> bool: ...
    @staticmethod
    def is_premultiplied(memory_format: MemoryFormat) -> bool: ...

class SandboxSelector(enum.IntEnum):
    AUTO = 0
    BWRAP = 1
    FLATPAK_SPAWN = 2
    NOT_SANDBOXED = 3
