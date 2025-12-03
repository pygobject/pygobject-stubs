import typing

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GModule
from gi.repository import GObject
from typing_extensions import Self

T = typing.TypeVar("T")

PIXBUF_MAJOR: int = 2
PIXBUF_MICRO: int = 12
PIXBUF_MINOR: int = 42
PIXBUF_VERSION: str = "2.42.12"
_lock = ...  # FIXME Constant
_namespace: str = "GdkPixbuf"
_overrides_module = ...  # FIXME Constant
_version: str = "2.0"

def pixbuf_error_quark() -> int: ...

class Pixbuf(GObject.Object, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        Pixbuf(**properties)
        new(colorspace:GdkPixbuf.Colorspace, has_alpha:bool, bits_per_sample:int, width:int, height:int) -> GdkPixbuf.Pixbuf or None
        new_from_bytes(data:GLib.Bytes, colorspace:GdkPixbuf.Colorspace, has_alpha:bool, bits_per_sample:int, width:int, height:int, rowstride:int) -> GdkPixbuf.Pixbuf
        new_from_data(data:list, colorspace:GdkPixbuf.Colorspace, has_alpha:bool, bits_per_sample:int, width:int, height:int, rowstride:int, destroy_fn:GdkPixbuf.PixbufDestroyNotify=None, destroy_fn_data=None) -> GdkPixbuf.Pixbuf
        new_from_file(filename:str) -> GdkPixbuf.Pixbuf or None
        new_from_file_at_scale(filename:str, width:int, height:int, preserve_aspect_ratio:bool) -> GdkPixbuf.Pixbuf or None
        new_from_file_at_size(filename:str, width:int, height:int) -> GdkPixbuf.Pixbuf or None
        new_from_inline(data:list, copy_pixels:bool) -> GdkPixbuf.Pixbuf
        new_from_resource(resource_path:str) -> GdkPixbuf.Pixbuf or None
        new_from_resource_at_scale(resource_path:str, width:int, height:int, preserve_aspect_ratio:bool) -> GdkPixbuf.Pixbuf or None
        new_from_stream(stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> GdkPixbuf.Pixbuf or None
        new_from_stream_at_scale(stream:Gio.InputStream, width:int, height:int, preserve_aspect_ratio:bool, cancellable:Gio.Cancellable=None) -> GdkPixbuf.Pixbuf or None
        new_from_stream_finish(async_result:Gio.AsyncResult) -> GdkPixbuf.Pixbuf or None
        new_from_xpm_data(data:list) -> GdkPixbuf.Pixbuf or None

    Object GdkPixbuf

    Properties from GdkPixbuf:
      colorspace -> GdkColorspace: Colorspace
        The colorspace in which the samples are interpreted
      n-channels -> gint: Number of Channels
        The number of samples per pixel
      has-alpha -> gboolean: Has Alpha
        Whether the pixbuf has an alpha channel
      bits-per-sample -> gint: Bits per Sample
        The number of bits per sample
      width -> gint: Width
        The number of columns of the pixbuf
      height -> gint: Height
        The number of rows of the pixbuf
      rowstride -> gint: Rowstride
        The number of bytes between the start of a row and the start of the next row
      pixels -> gpointer: Pixels
        A pointer to the pixel data of the pixbuf
      pixel-bytes -> GBytes: Pixel Bytes
        Readonly pixel data

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        bits_per_sample: int
        colorspace: Colorspace
        has_alpha: bool
        height: int
        n_channels: int
        pixel_bytes: GLib.Bytes
        pixels: None
        rowstride: int
        width: int

    props: Props = ...
    def __init__(
        self,
        bits_per_sample: int = ...,
        colorspace: Colorspace = ...,
        has_alpha: bool = ...,
        height: int = ...,
        n_channels: int = ...,
        pixel_bytes: GLib.Bytes = ...,
        pixels: None = ...,
        rowstride: int = ...,
        width: int = ...,
    ) -> None: ...
    def add_alpha(
        self, substitute_color: bool, r: int, g: int, b: int
    ) -> typing.Optional[Pixbuf]: ...
    def apply_embedded_orientation(self) -> typing.Optional[Pixbuf]: ...
    @staticmethod
    def calculate_rowstride(
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
    ) -> int: ...
    def composite(
        self,
        dest: Pixbuf,
        dest_x: int,
        dest_y: int,
        dest_width: int,
        dest_height: int,
        offset_x: float,
        offset_y: float,
        scale_x: float,
        scale_y: float,
        interp_type: InterpType,
        overall_alpha: int,
    ) -> None: ...
    def composite_color(
        self,
        dest: Pixbuf,
        dest_x: int,
        dest_y: int,
        dest_width: int,
        dest_height: int,
        offset_x: float,
        offset_y: float,
        scale_x: float,
        scale_y: float,
        interp_type: InterpType,
        overall_alpha: int,
        check_x: int,
        check_y: int,
        check_size: int,
        color1: int,
        color2: int,
    ) -> None: ...
    def composite_color_simple(
        self,
        dest_width: int,
        dest_height: int,
        interp_type: InterpType,
        overall_alpha: int,
        check_size: int,
        color1: int,
        color2: int,
    ) -> typing.Optional[Pixbuf]: ...
    def copy(self) -> typing.Optional[Pixbuf]: ...
    def copy_area(
        self,
        src_x: int,
        src_y: int,
        width: int,
        height: int,
        dest_pixbuf: Pixbuf,
        dest_x: int,
        dest_y: int,
    ) -> None: ...
    def copy_options(self, dest_pixbuf: Pixbuf) -> bool: ...
    def fill(self, pixel: int) -> None: ...
    def flip(self, horizontal: bool) -> typing.Optional[Pixbuf]: ...
    def get_bits_per_sample(self) -> int: ...
    def get_byte_length(self) -> int: ...
    def get_colorspace(self) -> Colorspace: ...
    @staticmethod
    def get_file_info(
        filename: str,
    ) -> typing.Tuple[typing.Optional[PixbufFormat], int, int]: ...
    @staticmethod
    def get_file_info_async(
        filename: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @staticmethod
    def get_file_info_finish(
        async_result: Gio.AsyncResult,
    ) -> typing.Tuple[PixbufFormat, int, int]: ...
    @staticmethod
    def get_formats() -> list[PixbufFormat]: ...
    def get_has_alpha(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_n_channels(self) -> int: ...
    def get_option(self, key: str) -> typing.Optional[str]: ...
    def get_options(self) -> dict[str, str]: ...
    def get_pixels(self) -> bytes: ...
    def get_rowstride(self) -> int: ...
    def get_width(self) -> int: ...
    @staticmethod
    def init_modules(path: str) -> bool: ...
    @classmethod
    def new(
        cls,
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
    ) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new_from_bytes(
        cls,
        data: GLib.Bytes,
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
        rowstride: int,
    ) -> Pixbuf: ...
    # override
    @classmethod
    def new_from_data(
        cls,
        data: GLib.Bytes,
        colorspace: Colorspace,
        has_alpha: bool,
        bits_per_sample: int,
        width: int,
        height: int,
        rowstride: int,
        destroy_fn: typing.Any,
        *destroy_fn_data: typing.Any,
    ) -> Pixbuf: ...
    @classmethod
    def new_from_file(cls, filename: str) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new_from_file_at_scale(
        cls, filename: str, width: int, height: int, preserve_aspect_ratio: bool
    ) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new_from_file_at_size(
        cls, filename: str, width: int, height: int
    ) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new_from_inline(
        cls, data: typing.Sequence[int], copy_pixels: bool
    ) -> Pixbuf: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new_from_resource_at_scale(
        cls, resource_path: str, width: int, height: int, preserve_aspect_ratio: bool
    ) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new_from_stream(
        cls,
        stream: Gio.InputStream,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Optional[Pixbuf]: ...
    @staticmethod
    def new_from_stream_async(
        stream: Gio.InputStream,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_from_stream_at_scale(
        cls,
        stream: Gio.InputStream,
        width: int,
        height: int,
        preserve_aspect_ratio: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Optional[Pixbuf]: ...
    @staticmethod
    def new_from_stream_at_scale_async(
        stream: Gio.InputStream,
        width: int,
        height: int,
        preserve_aspect_ratio: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_from_stream_finish(cls, async_result: Gio.AsyncResult) -> Pixbuf: ...
    @classmethod
    def new_from_xpm_data(
        cls, data: typing.Sequence[str]
    ) -> typing.Optional[Pixbuf]: ...
    def new_subpixbuf(
        self, src_x: int, src_y: int, width: int, height: int
    ) -> Pixbuf: ...
    def read_pixel_bytes(self) -> GLib.Bytes: ...
    def read_pixels(self) -> int: ...
    def remove_option(self, key: str) -> bool: ...
    def rotate_simple(self, angle: PixbufRotation) -> typing.Optional[Pixbuf]: ...
    def saturate_and_pixelate(
        self, dest: Pixbuf, saturation: float, pixelate: bool
    ) -> None: ...
    def save_to_bufferv(
        self,
        type: str,
        option_keys: typing.Optional[typing.Sequence[str]] = None,
        option_values: typing.Optional[typing.Sequence[str]] = None,
    ) -> typing.Tuple[bool, bytes]: ...
    def save_to_callbackv(
        self,
        save_func: typing.Callable[..., typing.Tuple[bool, GLib.Error]],
        type: str,
        option_keys: typing.Optional[typing.Sequence[str]] = None,
        option_values: typing.Optional[typing.Sequence[str]] = None,
        *user_data: typing.Any,
    ) -> bool: ...
    @staticmethod
    def save_to_stream_finish(async_result: Gio.AsyncResult) -> bool: ...
    def save_to_streamv(
        self,
        stream: Gio.OutputStream,
        type: str,
        option_keys: typing.Optional[typing.Sequence[str]] = None,
        option_values: typing.Optional[typing.Sequence[str]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def save_to_streamv_async(
        self,
        stream: Gio.OutputStream,
        type: str,
        option_keys: typing.Optional[typing.Sequence[str]] = None,
        option_values: typing.Optional[typing.Sequence[str]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def savev(
        self,
        filename: str,
        type: str,
        option_keys: typing.Optional[typing.Sequence[str]] = None,
        option_values: typing.Optional[typing.Sequence[str]] = None,
    ) -> bool: ...
    def scale(
        self,
        dest: Pixbuf,
        dest_x: int,
        dest_y: int,
        dest_width: int,
        dest_height: int,
        offset_x: float,
        offset_y: float,
        scale_x: float,
        scale_y: float,
        interp_type: InterpType,
    ) -> None: ...
    def scale_simple(
        self, dest_width: int, dest_height: int, interp_type: InterpType
    ) -> typing.Optional[Pixbuf]: ...
    def set_option(self, key: str, value: str) -> bool: ...

class PixbufAnimation(GObject.Object):
    """
    :Constructors:

    ::

        PixbufAnimation(**properties)
        new_from_file(filename:str) -> GdkPixbuf.PixbufAnimation or None
        new_from_resource(resource_path:str) -> GdkPixbuf.PixbufAnimation or None
        new_from_stream(stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> GdkPixbuf.PixbufAnimation or None
        new_from_stream_finish(async_result:Gio.AsyncResult) -> GdkPixbuf.PixbufAnimation or None

    Object GdkPixbufAnimation

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_get_iter(
        self, start_time: typing.Optional[GLib.TimeVal] = None
    ) -> PixbufAnimationIter: ...
    def do_get_size(self, width: int, height: int) -> None: ...
    def do_get_static_image(self) -> Pixbuf: ...
    def do_is_static_image(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_iter(
        self, start_time: typing.Optional[GLib.TimeVal] = None
    ) -> PixbufAnimationIter: ...
    def get_static_image(self) -> Pixbuf: ...
    def get_width(self) -> int: ...
    def is_static_image(self) -> bool: ...
    @classmethod
    def new_from_file(cls, filename: str) -> typing.Optional[PixbufAnimation]: ...
    @classmethod
    def new_from_resource(
        cls, resource_path: str
    ) -> typing.Optional[PixbufAnimation]: ...
    @classmethod
    def new_from_stream(
        cls,
        stream: Gio.InputStream,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Optional[PixbufAnimation]: ...
    @staticmethod
    def new_from_stream_async(
        stream: Gio.InputStream,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_from_stream_finish(
        cls, async_result: Gio.AsyncResult
    ) -> PixbufAnimation: ...

class PixbufAnimationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufAnimationClass()
    """

    parent_class: GObject.ObjectClass = ...
    is_static_image: typing.Callable[[PixbufAnimation], bool] = ...
    get_static_image: typing.Callable[[PixbufAnimation], Pixbuf] = ...
    get_size: typing.Callable[[PixbufAnimation, int, int], None] = ...
    get_iter: typing.Callable[
        [PixbufAnimation, typing.Optional[GLib.TimeVal]], PixbufAnimationIter
    ] = ...

class PixbufAnimationIter(GObject.Object):
    """
    :Constructors:

    ::

        PixbufAnimationIter(**properties)

    Object GdkPixbufAnimationIter

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def advance(self, current_time: typing.Optional[GLib.TimeVal] = None) -> bool: ...
    def do_advance(
        self, current_time: typing.Optional[GLib.TimeVal] = None
    ) -> bool: ...
    def do_get_delay_time(self) -> int: ...
    def do_get_pixbuf(self) -> Pixbuf: ...
    def do_on_currently_loading_frame(self) -> bool: ...
    def get_delay_time(self) -> int: ...
    def get_pixbuf(self) -> Pixbuf: ...
    def on_currently_loading_frame(self) -> bool: ...

class PixbufAnimationIterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufAnimationIterClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_delay_time: typing.Callable[[PixbufAnimationIter], int] = ...
    get_pixbuf: typing.Callable[[PixbufAnimationIter], Pixbuf] = ...
    on_currently_loading_frame: typing.Callable[[PixbufAnimationIter], bool] = ...
    advance: typing.Callable[
        [PixbufAnimationIter, typing.Optional[GLib.TimeVal]], bool
    ] = ...

class PixbufFormat(GObject.GBoxed):
    """
    :Constructors:

    ::

        PixbufFormat()
    """

    name: str = ...
    signature: PixbufModulePattern = ...
    domain: str = ...
    description: str = ...
    mime_types: list[str] = ...
    extensions: list[str] = ...
    flags: int = ...
    disabled: bool = ...
    license: str = ...
    def copy(self) -> typing.Optional[PixbufFormat]: ...
    def free(self) -> None: ...
    def get_description(self) -> typing.Optional[str]: ...
    def get_extensions(self) -> typing.Optional[list[str]]: ...
    def get_license(self) -> typing.Optional[str]: ...
    def get_mime_types(self) -> typing.Optional[list[str]]: ...
    def get_name(self) -> typing.Optional[str]: ...
    def is_disabled(self) -> bool: ...
    def is_save_option_supported(self, option_key: str) -> bool: ...
    def is_scalable(self) -> bool: ...
    def is_writable(self) -> bool: ...
    def set_disabled(self, disabled: bool) -> None: ...

class PixbufLoader(GObject.Object):
    """
    :Constructors:

    ::

        PixbufLoader(**properties)
        new() -> GdkPixbuf.PixbufLoader
        new_with_mime_type(mime_type:str) -> GdkPixbuf.PixbufLoader
        new_with_type(image_type:str) -> GdkPixbuf.PixbufLoader

    Object GdkPixbufLoader

    Signals from GdkPixbufLoader:
      size-prepared (gint, gint)
      area-prepared ()
      area-updated (gint, gint, gint, gint)
      closed ()

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    priv: None = ...
    def close(self) -> bool: ...
    def do_area_prepared(self) -> None: ...
    def do_area_updated(self, x: int, y: int, width: int, height: int) -> None: ...
    def do_closed(self) -> None: ...
    def do_size_prepared(self, width: int, height: int) -> None: ...
    def get_animation(self) -> typing.Optional[PixbufAnimation]: ...
    def get_format(self) -> typing.Optional[PixbufFormat]: ...
    def get_pixbuf(self) -> typing.Optional[Pixbuf]: ...
    @classmethod
    def new(cls) -> PixbufLoader: ...
    @classmethod
    def new_with_mime_type(cls, mime_type: str) -> PixbufLoader: ...
    @classmethod
    def new_with_type(cls, image_type: str) -> PixbufLoader: ...
    def set_size(self, width: int, height: int) -> None: ...
    def write(self, buf: typing.Sequence[int]) -> bool: ...
    def write_bytes(self, buffer: GLib.Bytes) -> bool: ...

class PixbufLoaderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufLoaderClass()
    """

    parent_class: GObject.ObjectClass = ...
    size_prepared: typing.Callable[[PixbufLoader, int, int], None] = ...
    area_prepared: typing.Callable[[PixbufLoader], None] = ...
    area_updated: typing.Callable[[PixbufLoader, int, int, int, int], None] = ...
    closed: typing.Callable[[PixbufLoader], None] = ...

class PixbufModule(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufModule()
    """

    module_name: str = ...
    module_path: str = ...
    module: GModule.Module = ...
    info: PixbufFormat = ...
    load: typing.Callable[[None], Pixbuf] = ...
    load_xpm_data: typing.Callable[[typing.Sequence[str]], Pixbuf] = ...
    begin_load: None = ...
    stop_load: typing.Callable[[None], bool] = ...
    load_increment: typing.Callable[[None, typing.Sequence[int]], bool] = ...
    load_animation: typing.Callable[[None], PixbufAnimation] = ...
    save: typing.Callable[
        [
            None,
            Pixbuf,
            typing.Optional[typing.Sequence[str]],
            typing.Optional[typing.Sequence[str]],
        ],
        bool,
    ] = ...
    save_to_callback: None = ...
    is_save_option_supported: typing.Callable[[str], bool] = ...
    _reserved1: None = ...
    _reserved2: None = ...
    _reserved3: None = ...
    _reserved4: None = ...

class PixbufModulePattern(GObject.GPointer):
    """
    :Constructors:

    ::

        PixbufModulePattern()
    """

    prefix: str = ...
    mask: str = ...
    relevance: int = ...

class PixbufNonAnim(PixbufAnimation):
    """
    :Constructors:

    ::

        PixbufNonAnim(**properties)
        new(pixbuf:GdkPixbuf.Pixbuf) -> GdkPixbuf.PixbufAnimation

    Object GdkPixbufNonAnim

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls, pixbuf: Pixbuf) -> PixbufNonAnim: ...

class PixbufSimpleAnim(PixbufAnimation):
    """
    :Constructors:

    ::

        PixbufSimpleAnim(**properties)
        new(width:int, height:int, rate:float) -> GdkPixbuf.PixbufSimpleAnim

    Object GdkPixbufSimpleAnim

    Properties from GdkPixbufSimpleAnim:
      loop -> gboolean: Loop
        Whether the animation should loop when it reaches the end

    Signals from GObject:
      notify (GParam)
    """
    class Props(PixbufAnimation.Props):
        loop: bool

    props: Props = ...
    def __init__(self, loop: bool = ...) -> None: ...
    def add_frame(self, pixbuf: Pixbuf) -> None: ...
    def get_loop(self) -> bool: ...
    @classmethod
    def new(cls, width: int, height: int, rate: float) -> PixbufSimpleAnim: ...
    def set_loop(self, loop: bool) -> None: ...

class PixbufSimpleAnimClass(GObject.GPointer): ...
class PixbufSimpleAnimIter(PixbufAnimationIter): ...

class PixbufFormatFlags(GObject.GFlags):
    SCALABLE = 2
    THREADSAFE = 4
    WRITABLE = 1

class Colorspace(GObject.GEnum):
    RGB = 0

class InterpType(GObject.GEnum):
    BILINEAR = 2
    HYPER = 3
    NEAREST = 0
    TILES = 1

class PixbufAlphaMode(GObject.GEnum):
    BILEVEL = 0
    FULL = 1

class PixbufError(GObject.GEnum):
    BAD_OPTION = 2
    CORRUPT_IMAGE = 0
    FAILED = 5
    INCOMPLETE_ANIMATION = 6
    INSUFFICIENT_MEMORY = 1
    UNKNOWN_TYPE = 3
    UNSUPPORTED_OPERATION = 4
    @staticmethod
    def quark() -> int: ...

class PixbufRotation(GObject.GEnum):
    CLOCKWISE = 270
    COUNTERCLOCKWISE = 90
    NONE = 0
    UPSIDEDOWN = 180
