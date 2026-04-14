from typing import Any
from typing import Final
from typing import Protocol
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable
from collections.abc import Sequence

from gi import _gi
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase

T = TypeVar("T")

BUFFER_POOL_OPTION_VIDEO_AFFINE_TRANSFORMATION_META: Final = (
    "GstBufferPoolOptionVideoAffineTransformation"
)
BUFFER_POOL_OPTION_VIDEO_ALIGNMENT: Final = "GstBufferPoolOptionVideoAlignment"
BUFFER_POOL_OPTION_VIDEO_GL_TEXTURE_UPLOAD_META: Final = (
    "GstBufferPoolOptionVideoGLTextureUploadMeta"
)
BUFFER_POOL_OPTION_VIDEO_META: Final = "GstBufferPoolOptionVideoMeta"
CAPS_FEATURE_FORMAT_INTERLACED: Final = "format:Interlaced"
CAPS_FEATURE_META_GST_VIDEO_AFFINE_TRANSFORMATION_META: Final = (
    "meta:GstVideoAffineTransformation"
)
CAPS_FEATURE_META_GST_VIDEO_GL_TEXTURE_UPLOAD_META: Final = (
    "meta:GstVideoGLTextureUploadMeta"
)
CAPS_FEATURE_META_GST_VIDEO_META: Final = "meta:GstVideoMeta"
CAPS_FEATURE_META_GST_VIDEO_OVERLAY_COMPOSITION: Final = (
    "meta:GstVideoOverlayComposition"
)
META_TAG_VIDEO_COLORSPACE_STR: Final = "colorspace"
META_TAG_VIDEO_ORIENTATION_STR: Final = "orientation"
META_TAG_VIDEO_SIZE_STR: Final = "size"
META_TAG_VIDEO_STR: Final = "video"
VIDEO_COLORIMETRY_BT2020: Final = "bt2020"
VIDEO_COLORIMETRY_BT2020_10: Final = "bt2020-10"
VIDEO_COLORIMETRY_BT2100_HLG: Final = "bt2100-hlg"
VIDEO_COLORIMETRY_BT2100_PQ: Final = "bt2100-pq"
VIDEO_COLORIMETRY_BT601: Final = "bt601"
VIDEO_COLORIMETRY_BT709: Final = "bt709"
VIDEO_COLORIMETRY_SMPTE240M: Final = "smpte240m"
VIDEO_COLORIMETRY_SRGB: Final = "sRGB"
VIDEO_COMP_A: Final[int]
VIDEO_COMP_B: Final[int]
VIDEO_COMP_G: Final[int]
VIDEO_COMP_INDEX: Final[int]
VIDEO_COMP_PALETTE: Final[int]
VIDEO_COMP_R: Final[int]
VIDEO_COMP_U: Final[int]
VIDEO_COMP_V: Final[int]
VIDEO_COMP_Y: Final[int]
VIDEO_CONVERTER_OPT_ALPHA_MODE: Final = "GstVideoConverter.alpha-mode"
VIDEO_CONVERTER_OPT_ALPHA_VALUE: Final = "GstVideoConverter.alpha-value"
VIDEO_CONVERTER_OPT_ASYNC_TASKS: Final = "GstVideoConverter.async-tasks"
VIDEO_CONVERTER_OPT_BORDER_ARGB: Final = "GstVideoConverter.border-argb"
VIDEO_CONVERTER_OPT_CHROMA_MODE: Final = "GstVideoConverter.chroma-mode"
VIDEO_CONVERTER_OPT_CHROMA_RESAMPLER_METHOD: Final = (
    "GstVideoConverter.chroma-resampler-method"
)
VIDEO_CONVERTER_OPT_DEST_HEIGHT: Final = "GstVideoConverter.dest-height"
VIDEO_CONVERTER_OPT_DEST_WIDTH: Final = "GstVideoConverter.dest-width"
VIDEO_CONVERTER_OPT_DEST_X: Final = "GstVideoConverter.dest-x"
VIDEO_CONVERTER_OPT_DEST_Y: Final = "GstVideoConverter.dest-y"
VIDEO_CONVERTER_OPT_DITHER_METHOD: Final = "GstVideoConverter.dither-method"
VIDEO_CONVERTER_OPT_DITHER_QUANTIZATION: Final = "GstVideoConverter.dither-quantization"
VIDEO_CONVERTER_OPT_FILL_BORDER: Final = "GstVideoConverter.fill-border"
VIDEO_CONVERTER_OPT_GAMMA_MODE: Final = "GstVideoConverter.gamma-mode"
VIDEO_CONVERTER_OPT_MATRIX_MODE: Final = "GstVideoConverter.matrix-mode"
VIDEO_CONVERTER_OPT_PRIMARIES_MODE: Final = "GstVideoConverter.primaries-mode"
VIDEO_CONVERTER_OPT_RESAMPLER_METHOD: Final = "GstVideoConverter.resampler-method"
VIDEO_CONVERTER_OPT_RESAMPLER_TAPS: Final = "GstVideoConverter.resampler-taps"
VIDEO_CONVERTER_OPT_SRC_HEIGHT: Final = "GstVideoConverter.src-height"
VIDEO_CONVERTER_OPT_SRC_WIDTH: Final = "GstVideoConverter.src-width"
VIDEO_CONVERTER_OPT_SRC_X: Final = "GstVideoConverter.src-x"
VIDEO_CONVERTER_OPT_SRC_Y: Final = "GstVideoConverter.src-y"
VIDEO_CONVERTER_OPT_THREADS: Final = "GstVideoConverter.threads"
VIDEO_DECODER_MAX_ERRORS: Final[int]
VIDEO_DECODER_SINK_NAME: Final = "sink"
VIDEO_DECODER_SRC_NAME: Final = "src"
VIDEO_DMA_DRM_CAPS_MAKE: Final[str]
VIDEO_ENCODER_SINK_NAME: Final = "sink"
VIDEO_ENCODER_SRC_NAME: Final = "src"
VIDEO_FORMATS_ALL: Final = "{ "
VIDEO_FORMATS_ALL_STR: Final[str]
VIDEO_FORMATS_ANY: Final = "{ "
VIDEO_FORMATS_ANY_STR: Final = "DMA_DRM, "
VIDEO_FORMAT_LAST: Final[int]
VIDEO_FPS_RANGE: Final = "(fraction) [ 0, max ]"
VIDEO_MAX_COMPONENTS: Final[int]
VIDEO_MAX_PLANES: Final[int]
VIDEO_RESAMPLER_OPT_CUBIC_B: Final = "GstVideoResampler.cubic-b"
VIDEO_RESAMPLER_OPT_CUBIC_C: Final = "GstVideoResampler.cubic-c"
VIDEO_RESAMPLER_OPT_ENVELOPE: Final = "GstVideoResampler.envelope"
VIDEO_RESAMPLER_OPT_MAX_TAPS: Final = "GstVideoResampler.max-taps"
VIDEO_RESAMPLER_OPT_SHARPEN: Final = "GstVideoResampler.sharpen"
VIDEO_RESAMPLER_OPT_SHARPNESS: Final = "GstVideoResampler.sharpness"
VIDEO_SCALER_OPT_DITHER_METHOD: Final = "GstVideoScaler.dither-method"
VIDEO_SIZE_RANGE: Final = "(int) [ 1, max ]"
VIDEO_TILE_TYPE_MASK: Final[int]
VIDEO_TILE_TYPE_SHIFT: Final[int]
VIDEO_TILE_X_TILES_MASK: Final[int]
VIDEO_TILE_Y_TILES_SHIFT: Final[int]

def ancillary_meta_api_get_type() -> type[Any]: ...
def ancillary_meta_get_info() -> Gst.MetaInfo: ...
def buffer_add_ancillary_meta(buffer: Gst.Buffer) -> AncillaryMeta: ...
def buffer_add_video_afd_meta(
    buffer: Gst.Buffer, field: int, spec: VideoAFDSpec, afd: VideoAFDValue
) -> VideoAFDMeta: ...
def buffer_add_video_affine_transformation_meta(
    buffer: Gst.Buffer,
) -> VideoAffineTransformationMeta: ...
def buffer_add_video_bar_meta(
    buffer: Gst.Buffer, field: int, is_letterbox: bool, bar_data1: int, bar_data2: int
) -> VideoBarMeta: ...
def buffer_add_video_caption_meta(
    buffer: Gst.Buffer, caption_type: VideoCaptionType, data: Sequence[int]
) -> VideoCaptionMeta: ...
def buffer_add_video_codec_alpha_meta(
    buffer: Gst.Buffer, alpha_buffer: Gst.Buffer
) -> VideoCodecAlphaMeta: ...
def buffer_add_video_gl_texture_upload_meta(
    buffer: Gst.Buffer,
    texture_orientation: VideoGLTextureOrientation,
    n_textures: int,
    texture_type: VideoGLTextureType,
    upload: Callable[..., bool],
    user_data_copy: Callable[[None], None],
    user_data_free: Callable[[None], None],
    *user_data: Any,
) -> VideoGLTextureUploadMeta: ...
def buffer_add_video_meta(
    buffer: Gst.Buffer,
    flags: VideoFrameFlags,
    format: VideoFormat,
    width: int,
    height: int,
) -> VideoMeta: ...
def buffer_add_video_meta_full(
    buffer: Gst.Buffer,
    flags: VideoFrameFlags,
    format: VideoFormat,
    width: int,
    height: int,
    n_planes: int,
    offset: Sequence[int],
    stride: Sequence[int],
) -> VideoMeta: ...
def buffer_add_video_overlay_composition_meta(
    buf: Gst.Buffer, comp: VideoOverlayComposition | None = None
) -> VideoOverlayCompositionMeta: ...
def buffer_add_video_region_of_interest_meta(
    buffer: Gst.Buffer, roi_type: str, x: int, y: int, w: int, h: int
) -> VideoRegionOfInterestMeta: ...
def buffer_add_video_region_of_interest_meta_id(
    buffer: Gst.Buffer, roi_type: int, x: int, y: int, w: int, h: int
) -> VideoRegionOfInterestMeta: ...
def buffer_add_video_sei_user_data_unregistered_meta(
    buffer: Gst.Buffer, uuid: int, data: int | None, size: int
) -> VideoSEIUserDataUnregisteredMeta: ...
def buffer_add_video_time_code_meta(
    buffer: Gst.Buffer, tc: VideoTimeCode
) -> VideoTimeCodeMeta | None: ...
def buffer_add_video_time_code_meta_full(
    buffer: Gst.Buffer,
    fps_n: int,
    fps_d: int,
    latest_daily_jam: GLib.DateTime,
    flags: VideoTimeCodeFlags,
    hours: int,
    minutes: int,
    seconds: int,
    frames: int,
    field_count: int,
) -> VideoTimeCodeMeta | None: ...
def buffer_get_video_meta(buffer: Gst.Buffer) -> VideoMeta | None: ...
def buffer_get_video_meta_id(buffer: Gst.Buffer, id: int) -> VideoMeta | None: ...
def buffer_get_video_region_of_interest_meta_id(
    buffer: Gst.Buffer, id: int
) -> VideoRegionOfInterestMeta | None: ...
def buffer_pool_config_get_video_alignment(
    config: Gst.Structure, align: VideoAlignment
) -> bool: ...
def buffer_pool_config_set_video_alignment(
    config: Gst.Structure, align: VideoAlignment
) -> None: ...
def is_video_overlay_prepare_window_handle_message(msg: Gst.Message) -> bool: ...
def navigation_event_get_coordinates(event: Gst.Event) -> tuple[bool, float, float]: ...
def navigation_event_get_type(event: Gst.Event) -> NavigationEventType: ...
def navigation_event_new_command(command: NavigationCommand) -> Gst.Event: ...
def navigation_event_new_key_press(
    key: str, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_key_release(
    key: str, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_mouse_button_press(
    button: int, x: float, y: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_mouse_button_release(
    button: int, x: float, y: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_mouse_double_click(
    button: int, x: float, y: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_mouse_move(
    x: float, y: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_mouse_scroll(
    x: float, y: float, delta_x: float, delta_y: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_touch_cancel(state: NavigationModifierType) -> Gst.Event: ...
def navigation_event_new_touch_down(
    identifier: int, x: float, y: float, pressure: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_touch_frame(state: NavigationModifierType) -> Gst.Event: ...
def navigation_event_new_touch_motion(
    identifier: int, x: float, y: float, pressure: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_new_touch_up(
    identifier: int, x: float, y: float, state: NavigationModifierType
) -> Gst.Event: ...
def navigation_event_parse_command(
    event: Gst.Event,
) -> tuple[bool, NavigationCommand]: ...
def navigation_event_parse_key_event(event: Gst.Event) -> tuple[bool, str]: ...
def navigation_event_parse_modifier_state(
    event: Gst.Event, state: NavigationModifierType
) -> bool: ...
def navigation_event_parse_mouse_button_event(
    event: Gst.Event,
) -> tuple[bool, int, float, float]: ...
def navigation_event_parse_mouse_move_event(
    event: Gst.Event,
) -> tuple[bool, float, float]: ...
def navigation_event_parse_mouse_scroll_event(
    event: Gst.Event,
) -> tuple[bool, float, float, float, float]: ...
def navigation_event_parse_touch_event(
    event: Gst.Event,
) -> tuple[bool, int, float, float, float]: ...
def navigation_event_parse_touch_up_event(
    event: Gst.Event,
) -> tuple[bool, int, float, float]: ...
def navigation_event_set_coordinates(event: Gst.Event, x: float, y: float) -> bool: ...
def navigation_message_get_type(message: Gst.Message) -> NavigationMessageType: ...
def navigation_message_new_angles_changed(
    src: Gst.Object, cur_angle: int, n_angles: int
) -> Gst.Message: ...
def navigation_message_new_commands_changed(src: Gst.Object) -> Gst.Message: ...
def navigation_message_new_event(src: Gst.Object, event: Gst.Event) -> Gst.Message: ...
def navigation_message_new_mouse_over(src: Gst.Object, active: bool) -> Gst.Message: ...
def navigation_message_parse_angles_changed(
    message: Gst.Message,
) -> tuple[bool, int, int]: ...
def navigation_message_parse_event(message: Gst.Message) -> tuple[bool, Gst.Event]: ...
def navigation_message_parse_mouse_over(message: Gst.Message) -> tuple[bool, bool]: ...
def navigation_query_get_type(query: Gst.Query) -> NavigationQueryType: ...
def navigation_query_new_angles() -> Gst.Query: ...
def navigation_query_new_commands() -> Gst.Query: ...
def navigation_query_parse_angles(query: Gst.Query) -> tuple[bool, int, int]: ...
def navigation_query_parse_commands_length(query: Gst.Query) -> tuple[bool, int]: ...
def navigation_query_parse_commands_nth(
    query: Gst.Query, nth: int
) -> tuple[bool, NavigationCommand]: ...
def navigation_query_set_angles(
    query: Gst.Query, cur_angle: int, n_angles: int
) -> None: ...
def navigation_query_set_commandsv(
    query: Gst.Query, cmds: Sequence[NavigationCommand]
) -> None: ...
def video_afd_meta_api_get_type() -> type[Any]: ...
def video_afd_meta_get_info() -> Gst.MetaInfo: ...
def video_affine_transformation_meta_api_get_type() -> type[Any]: ...
def video_affine_transformation_meta_get_info() -> Gst.MetaInfo: ...
def video_bar_meta_api_get_type() -> type[Any]: ...
def video_bar_meta_get_info() -> Gst.MetaInfo: ...
def video_blend(
    dest: VideoFrame, src: VideoFrame, x: int, y: int, global_alpha: float
) -> bool: ...
def video_blend_scale_linear_RGBA(
    src: VideoInfo, src_buffer: Gst.Buffer, dest_height: int, dest_width: int
) -> tuple[VideoInfo, Gst.Buffer]: ...
def video_calculate_display_ratio(
    video_width: int,
    video_height: int,
    video_par_n: int,
    video_par_d: int,
    display_par_n: int,
    display_par_d: int,
) -> tuple[bool, int, int]: ...
def video_caption_meta_api_get_type() -> type[Any]: ...
def video_caption_meta_get_info() -> Gst.MetaInfo: ...
def video_caption_type_from_caps(caps: Gst.Caps) -> VideoCaptionType: ...
def video_caption_type_to_caps(type: VideoCaptionType) -> Gst.Caps: ...
def video_center_rect(
    src: VideoRectangle, dst: VideoRectangle, scaling: bool
) -> VideoRectangle: ...
def video_chroma_from_string(s: str) -> VideoChromaSite: ...
def video_chroma_resample(
    resample: VideoChromaResample, lines: None, width: int
) -> None: ...
def video_chroma_site_from_string(s: str) -> VideoChromaSite: ...
def video_chroma_site_to_string(site: VideoChromaSite) -> str | None: ...
def video_chroma_to_string(site: VideoChromaSite) -> str: ...
def video_codec_alpha_meta_api_get_type() -> type[Any]: ...
def video_codec_alpha_meta_get_info() -> Gst.MetaInfo: ...
def video_color_matrix_from_iso(value: int) -> VideoColorMatrix: ...
def video_color_matrix_get_Kr_Kb(
    matrix: VideoColorMatrix,
) -> tuple[bool, float, float]: ...
def video_color_matrix_to_iso(matrix: VideoColorMatrix) -> int: ...
def video_color_primaries_from_iso(value: int) -> VideoColorPrimaries: ...
def video_color_primaries_get_info(
    primaries: VideoColorPrimaries,
) -> VideoColorPrimariesInfo: ...
def video_color_primaries_is_equivalent(
    primaries: VideoColorPrimaries, other: VideoColorPrimaries
) -> bool: ...
def video_color_primaries_to_iso(primaries: VideoColorPrimaries) -> int: ...
def video_color_range_offsets(
    range: VideoColorRange, info: VideoFormatInfo
) -> tuple[list[int], list[int]]: ...
def video_color_transfer_decode(func: VideoTransferFunction, val: float) -> float: ...
def video_color_transfer_encode(func: VideoTransferFunction, val: float) -> float: ...
def video_convert_sample(
    sample: Gst.Sample, to_caps: Gst.Caps, timeout: int
) -> Gst.Sample | None: ...
def video_convert_sample_async(
    sample: Gst.Sample,
    to_caps: Gst.Caps,
    timeout: int,
    callback: Callable[..., None],
    *user_data: Any,
) -> None: ...
def video_crop_meta_api_get_type() -> type[Any]: ...
def video_crop_meta_get_info() -> Gst.MetaInfo: ...
def video_dma_drm_format_from_gst_format(
    format: VideoFormat, modifier: int | None = None
) -> int: ...
def video_dma_drm_format_to_gst_format(fourcc: int, modifier: int) -> VideoFormat: ...
def video_dma_drm_fourcc_from_format(format: VideoFormat) -> int: ...
def video_dma_drm_fourcc_from_string(format_str: str) -> tuple[int, int]: ...
def video_dma_drm_fourcc_to_format(fourcc: int) -> VideoFormat: ...
def video_dma_drm_fourcc_to_string(fourcc: int, modifier: int) -> str | None: ...
def video_event_is_force_key_unit(event: Gst.Event) -> bool: ...
def video_event_new_downstream_force_key_unit(
    timestamp: int, stream_time: int, running_time: int, all_headers: bool, count: int
) -> Gst.Event: ...
def video_event_new_still_frame(in_still: bool) -> Gst.Event: ...
def video_event_new_upstream_force_key_unit(
    running_time: int, all_headers: bool, count: int
) -> Gst.Event: ...
def video_event_parse_downstream_force_key_unit(
    event: Gst.Event,
) -> tuple[bool, int, int, int, bool, int]: ...
def video_event_parse_still_frame(event: Gst.Event) -> tuple[bool, bool]: ...
def video_event_parse_upstream_force_key_unit(
    event: Gst.Event,
) -> tuple[bool, int, bool, int]: ...
def video_field_order_from_string(order: str) -> VideoFieldOrder: ...
def video_field_order_to_string(order: VideoFieldOrder) -> str: ...
def video_format_from_fourcc(fourcc: int) -> VideoFormat: ...
def video_format_from_masks(
    depth: int,
    bpp: int,
    endianness: int,
    red_mask: int,
    green_mask: int,
    blue_mask: int,
    alpha_mask: int,
) -> VideoFormat: ...
def video_format_from_string(format: str) -> VideoFormat: ...
def video_format_get_info(format: VideoFormat) -> VideoFormatInfo: ...
def video_format_get_palette(format: VideoFormat) -> int: ...
def video_format_to_fourcc(format: VideoFormat) -> int: ...
def video_format_to_string(format: VideoFormat) -> str: ...
def video_formats_any() -> list[VideoFormat]: ...
def video_formats_raw() -> list[VideoFormat]: ...
def video_frame_map(
    info: VideoInfo, buffer: Gst.Buffer, flags: Gst.MapFlags
) -> tuple[bool, VideoFrame]: ...
def video_frame_map_id(
    info: VideoInfo, buffer: Gst.Buffer, id: int, flags: Gst.MapFlags
) -> tuple[bool, VideoFrame]: ...
def video_gl_texture_upload_meta_api_get_type() -> type[Any]: ...
def video_gl_texture_upload_meta_get_info() -> Gst.MetaInfo: ...
def video_guess_framerate(duration: int) -> tuple[bool, int, int]: ...
def video_info_dma_drm_from_caps(caps: Gst.Caps) -> tuple[bool, VideoInfoDmaDrm]: ...
def video_info_dma_drm_from_video_info(
    info: VideoInfo, modifier: int
) -> tuple[bool, VideoInfoDmaDrm]: ...
def video_info_dma_drm_init() -> VideoInfoDmaDrm: ...
def video_info_from_caps(caps: Gst.Caps) -> tuple[bool, VideoInfo]: ...
def video_info_init() -> VideoInfo: ...
def video_interlace_mode_from_string(mode: str) -> VideoInterlaceMode: ...
def video_interlace_mode_to_string(mode: VideoInterlaceMode) -> str: ...
def video_is_common_aspect_ratio(
    width: int, height: int, par_n: int, par_d: int
) -> bool: ...
def video_is_dma_drm_caps(caps: Gst.Caps) -> bool: ...
def video_make_raw_caps(formats: Sequence[VideoFormat] | None = None) -> Gst.Caps: ...
def video_make_raw_caps_with_features(
    formats: Sequence[VideoFormat] | None = None,
    features: Gst.CapsFeatures | None = None,
) -> Gst.Caps: ...
def video_mastering_display_info_from_string(
    mastering: str,
) -> tuple[bool, VideoMasteringDisplayInfo]: ...
def video_meta_api_get_type() -> type[Any]: ...
def video_meta_get_info() -> Gst.MetaInfo: ...
def video_meta_transform_scale_get_quark() -> int: ...
def video_multiview_get_doubled_height_modes() -> Any: ...
def video_multiview_get_doubled_size_modes() -> Any: ...
def video_multiview_get_doubled_width_modes() -> Any: ...
def video_multiview_get_mono_modes() -> Any: ...
def video_multiview_get_unpacked_modes() -> Any: ...
def video_multiview_guess_half_aspect(
    mv_mode: VideoMultiviewMode, width: int, height: int, par_n: int, par_d: int
) -> bool: ...
def video_multiview_mode_from_caps_string(
    caps_mview_mode: str,
) -> VideoMultiviewMode: ...
def video_multiview_mode_to_caps_string(
    mview_mode: VideoMultiviewMode,
) -> str | None: ...
def video_multiview_video_info_change_mode(
    info: VideoInfo,
    out_mview_mode: VideoMultiviewMode,
    out_mview_flags: VideoMultiviewFlags,
) -> None: ...
def video_orientation_from_tag(
    taglist: Gst.TagList,
) -> tuple[bool, VideoOrientationMethod]: ...
def video_overlay_composition_meta_api_get_type() -> type[Any]: ...
def video_overlay_composition_meta_get_info() -> Gst.MetaInfo: ...
def video_overlay_install_properties(
    oclass: GObject.ObjectClass, last_prop_id: int
) -> None: ...
def video_overlay_set_property(
    object: GObject.Object, last_prop_id: int, property_id: int, value: Any
) -> bool: ...
def video_region_of_interest_meta_api_get_type() -> type[Any]: ...
def video_region_of_interest_meta_get_info() -> Gst.MetaInfo: ...
def video_sei_user_data_unregistered_meta_api_get_type() -> type[Any]: ...
def video_sei_user_data_unregistered_meta_get_info() -> Gst.MetaInfo: ...
def video_sei_user_data_unregistered_parse_precision_time_stamp(
    user_data: VideoSEIUserDataUnregisteredMeta,
) -> tuple[bool, int, int]: ...
def video_tile_get_index(
    mode: VideoTileMode, x: int, y: int, x_tiles: int, y_tiles: int
) -> int: ...
def video_time_code_meta_api_get_type() -> type[Any]: ...
def video_time_code_meta_get_info() -> Gst.MetaInfo: ...
def video_transfer_function_decode(
    func: VideoTransferFunction, val: float
) -> float: ...
def video_transfer_function_encode(
    func: VideoTransferFunction, val: float
) -> float: ...
def video_transfer_function_from_iso(value: int) -> VideoTransferFunction: ...
def video_transfer_function_is_equivalent(
    from_func: VideoTransferFunction,
    from_bpp: int,
    to_func: VideoTransferFunction,
    to_bpp: int,
) -> bool: ...
def video_transfer_function_to_iso(func: VideoTransferFunction) -> int: ...

class AncillaryMeta(_gi.Struct):
    """
    :Constructors:

    ::

        AncillaryMeta()
    """

    meta: Gst.Meta
    field: AncillaryMetaField
    c_not_y_channel: bool
    line: int
    offset: int
    DID: int
    SDID_block_number: int
    data_count: int
    data: int
    checksum: int
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class ColorBalance(GObject.GInterface, Protocol):
    """
    Interface GstColorBalance
    """
    def get_balance_type(self) -> ColorBalanceType: ...
    def get_value(self, channel: ColorBalanceChannel) -> int: ...
    def list_channels(self) -> list[ColorBalanceChannel]: ...
    def set_value(self, channel: ColorBalanceChannel, value: int) -> None: ...
    def value_changed(self, channel: ColorBalanceChannel, value: int) -> None: ...

class ColorBalanceChannel(GObject.Object):
    """
    :Constructors:

    ::

        ColorBalanceChannel(**properties)

    Object GstColorBalanceChannel

    Signals from GstColorBalanceChannel:
      value-changed (gint)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent(self) -> GObject.Object: ...
    @property
    def label(self) -> str: ...
    @property
    def min_value(self) -> int: ...
    @property
    def max_value(self) -> int: ...
    def do_value_changed(self, value: int) -> None: ...

class ColorBalanceChannelClass(_gi.Struct):
    """
    :Constructors:

    ::

        ColorBalanceChannelClass()
    """
    @property
    def parent(self) -> GObject.ObjectClass: ...
    @property
    def value_changed(self) -> Callable[[ColorBalanceChannel, int], None]: ...

class ColorBalanceInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ColorBalanceInterface()
    """
    @property
    def iface(self) -> GObject.TypeInterface: ...
    @property
    def list_channels(self) -> Callable[[ColorBalance], list[ColorBalanceChannel]]: ...
    @property
    def set_value(self) -> Callable[[ColorBalance, ColorBalanceChannel, int], None]: ...
    @property
    def get_value(self) -> Callable[[ColorBalance, ColorBalanceChannel], int]: ...
    @property
    def get_balance_type(self) -> Callable[[ColorBalance], ColorBalanceType]: ...
    @property
    def value_changed(
        self,
    ) -> Callable[[ColorBalance, ColorBalanceChannel, int], None]: ...

class Navigation(GObject.GInterface, Protocol):
    """
    Interface GstNavigation
    """
    @staticmethod
    def event_get_coordinates(event: Gst.Event) -> tuple[bool, float, float]: ...
    @staticmethod
    def event_get_type(event: Gst.Event) -> NavigationEventType: ...
    @staticmethod
    def event_new_command(command: NavigationCommand) -> Gst.Event: ...
    @staticmethod
    def event_new_key_press(key: str, state: NavigationModifierType) -> Gst.Event: ...
    @staticmethod
    def event_new_key_release(key: str, state: NavigationModifierType) -> Gst.Event: ...
    @staticmethod
    def event_new_mouse_button_press(
        button: int, x: float, y: float, state: NavigationModifierType
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_mouse_button_release(
        button: int, x: float, y: float, state: NavigationModifierType
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_mouse_double_click(
        button: int, x: float, y: float, state: NavigationModifierType
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_mouse_move(
        x: float, y: float, state: NavigationModifierType
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_mouse_scroll(
        x: float,
        y: float,
        delta_x: float,
        delta_y: float,
        state: NavigationModifierType,
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_touch_cancel(state: NavigationModifierType) -> Gst.Event: ...
    @staticmethod
    def event_new_touch_down(
        identifier: int,
        x: float,
        y: float,
        pressure: float,
        state: NavigationModifierType,
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_touch_frame(state: NavigationModifierType) -> Gst.Event: ...
    @staticmethod
    def event_new_touch_motion(
        identifier: int,
        x: float,
        y: float,
        pressure: float,
        state: NavigationModifierType,
    ) -> Gst.Event: ...
    @staticmethod
    def event_new_touch_up(
        identifier: int, x: float, y: float, state: NavigationModifierType
    ) -> Gst.Event: ...
    @staticmethod
    def event_parse_command(event: Gst.Event) -> tuple[bool, NavigationCommand]: ...
    @staticmethod
    def event_parse_key_event(event: Gst.Event) -> tuple[bool, str]: ...
    @staticmethod
    def event_parse_modifier_state(
        event: Gst.Event, state: NavigationModifierType
    ) -> bool: ...
    @staticmethod
    def event_parse_mouse_button_event(
        event: Gst.Event,
    ) -> tuple[bool, int, float, float]: ...
    @staticmethod
    def event_parse_mouse_move_event(event: Gst.Event) -> tuple[bool, float, float]: ...
    @staticmethod
    def event_parse_mouse_scroll_event(
        event: Gst.Event,
    ) -> tuple[bool, float, float, float, float]: ...
    @staticmethod
    def event_parse_touch_event(
        event: Gst.Event,
    ) -> tuple[bool, int, float, float, float]: ...
    @staticmethod
    def event_parse_touch_up_event(
        event: Gst.Event,
    ) -> tuple[bool, int, float, float]: ...
    @staticmethod
    def event_set_coordinates(event: Gst.Event, x: float, y: float) -> bool: ...
    @staticmethod
    def message_get_type(message: Gst.Message) -> NavigationMessageType: ...
    @staticmethod
    def message_new_angles_changed(
        src: Gst.Object, cur_angle: int, n_angles: int
    ) -> Gst.Message: ...
    @staticmethod
    def message_new_commands_changed(src: Gst.Object) -> Gst.Message: ...
    @staticmethod
    def message_new_event(src: Gst.Object, event: Gst.Event) -> Gst.Message: ...
    @staticmethod
    def message_new_mouse_over(src: Gst.Object, active: bool) -> Gst.Message: ...
    @staticmethod
    def message_parse_angles_changed(message: Gst.Message) -> tuple[bool, int, int]: ...
    @staticmethod
    def message_parse_event(message: Gst.Message) -> tuple[bool, Gst.Event]: ...
    @staticmethod
    def message_parse_mouse_over(message: Gst.Message) -> tuple[bool, bool]: ...
    @staticmethod
    def query_get_type(query: Gst.Query) -> NavigationQueryType: ...
    @staticmethod
    def query_new_angles() -> Gst.Query: ...
    @staticmethod
    def query_new_commands() -> Gst.Query: ...
    @staticmethod
    def query_parse_angles(query: Gst.Query) -> tuple[bool, int, int]: ...
    @staticmethod
    def query_parse_commands_length(query: Gst.Query) -> tuple[bool, int]: ...
    @staticmethod
    def query_parse_commands_nth(
        query: Gst.Query, nth: int
    ) -> tuple[bool, NavigationCommand]: ...
    @staticmethod
    def query_set_angles(query: Gst.Query, cur_angle: int, n_angles: int) -> None: ...
    @staticmethod
    def query_set_commandsv(
        query: Gst.Query, cmds: Sequence[NavigationCommand]
    ) -> None: ...
    def send_command(self, command: NavigationCommand) -> None: ...
    def send_event(self, structure: Gst.Structure) -> None: ...
    def send_event_simple(self, event: Gst.Event) -> None: ...
    def send_key_event(self, event: str, key: str) -> None: ...
    def send_mouse_event(self, event: str, button: int, x: float, y: float) -> None: ...
    def send_mouse_scroll_event(
        self, x: float, y: float, delta_x: float, delta_y: float
    ) -> None: ...

class NavigationInterface(_gi.Struct):
    """
    :Constructors:

    ::

        NavigationInterface()
    """
    @property
    def iface(self) -> GObject.TypeInterface: ...
    @property
    def send_event(self) -> Callable[[Navigation, Gst.Structure], None]: ...
    @property
    def send_event_simple(self) -> Callable[[Navigation, Gst.Event], None]: ...

class VideoAFDMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAFDMeta()
    """

    meta: Gst.Meta
    field: int
    spec: VideoAFDSpec
    afd: VideoAFDValue
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoAffineTransformationMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAffineTransformationMeta()
    """

    meta: Gst.Meta
    matrix: list[float]
    def apply_matrix(self, matrix: Sequence[float]) -> None: ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoAggregator(GstBase.Aggregator):
    """
    :Constructors:

    ::

        VideoAggregator(**properties)

    Object GstVideoAggregator

    Properties from GstVideoAggregator:
      force-live -> gboolean: Force live
        Always operate in live mode and aggregate on timeout regardless of whether any live sources are linked upstream

    Signals from GstAggregator:
      samples-selected (GstSegment, guint64, guint64, guint64, GstStructure)

    Properties from GstAggregator:
      latency -> guint64: Buffer latency
        Additional latency in live mode to allow upstream to take longer to produce buffers for the current position (in nanoseconds)
      min-upstream-latency -> guint64: Buffer latency
        When sources with a higher latency are expected to be plugged in dynamically after the aggregator has started playing, this allows overriding the minimum latency reported by the initial source(s). This is only taken into account when larger than the actually reported minimum latency. (nanoseconds)
      start-time-selection -> GstAggregatorStartTimeSelection: Start Time Selection
        Decides which start time is output
      start-time -> guint64: Start Time
        Start time to use if start-time-selection=set
      emit-signals -> gboolean: Emit signals
        Send signals

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(GstBase.Aggregator.Props):
        force_live: bool
        emit_signals: bool
        latency: int
        min_upstream_latency: int
        start_time: int
        start_time_selection: GstBase.AggregatorStartTimeSelection
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def aggregator(self) -> GstBase.Aggregator: ...
    @property
    def info(self) -> VideoInfo: ...
    @property
    def priv(self) -> VideoAggregatorPrivate: ...
    def __init__(
        self,
        *,
        force_live: bool = ...,
        emit_signals: bool = ...,
        latency: int = ...,
        min_upstream_latency: int = ...,
        start_time: int = ...,
        start_time_selection: GstBase.AggregatorStartTimeSelection = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_aggregate_frames(self, outbuffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_create_output_buffer(self, outbuffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_find_best_format(
        self, downstream_caps: Gst.Caps, best_info: VideoInfo
    ) -> bool: ...
    def do_update_caps(self, caps: Gst.Caps) -> Gst.Caps: ...
    def get_execution_task_pool(self) -> Gst.TaskPool: ...

class VideoAggregatorClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAggregatorClass()
    """
    @property
    def parent_class(self) -> GstBase.AggregatorClass: ...
    @property
    def update_caps(self) -> Callable[[VideoAggregator, Gst.Caps], Gst.Caps]: ...
    @property
    def aggregate_frames(
        self,
    ) -> Callable[[VideoAggregator, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def create_output_buffer(
        self,
    ) -> Callable[[VideoAggregator, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def find_best_format(
        self,
    ) -> Callable[[VideoAggregator, Gst.Caps, VideoInfo], bool]: ...

class VideoAggregatorConvertPad(VideoAggregatorPad):
    """
    :Constructors:

    ::

        VideoAggregatorConvertPad(**properties)

    Object GstVideoAggregatorConvertPad

    Properties from GstVideoAggregatorConvertPad:
      converter-config -> GstStructure: Converter configuration
        A GstStructure describing the configuration that should be used when scaling and converting this pad's video frames

    Properties from GstVideoAggregatorPad:
      zorder -> guint: Z-Order
        Z Order of the picture
      repeat-after-eos -> gboolean: Repeat After EOS
        Repeat the last frame after EOS until all pads are EOS
      max-last-buffer-repeat -> guint64: Max Last Buffer Repeat
        Repeat last buffer for time (in ns, -1=until EOS), behaviour on EOS is not affected

    Signals from GstAggregatorPad:
      buffer-consumed (GstBuffer)

    Properties from GstAggregatorPad:
      emit-signals -> gboolean: Emit signals
        Send signals to signal data consumption

    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)

    Properties from GstPad:
      caps -> GstCaps: Caps
        The capabilities of the pad
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
      offset -> gint64: Offset
        The running time offset of the pad

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(VideoAggregatorPad.Props):
        converter_config: Gst.Structure
        max_last_buffer_repeat: int
        repeat_after_eos: bool
        zorder: int
        emit_signals: bool
        caps: Gst.Caps
        direction: Gst.PadDirection
        offset: int
        template: Gst.PadTemplate
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> VideoAggregatorPad: ...
    @property
    def priv(self) -> VideoAggregatorConvertPadPrivate: ...
    def __init__(
        self,
        *,
        converter_config: Gst.Structure = ...,
        max_last_buffer_repeat: int = ...,
        repeat_after_eos: bool = ...,
        zorder: int = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_create_conversion_info(
        self, agg: VideoAggregator, conversion_info: VideoInfo
    ) -> None: ...
    def update_conversion_info(self) -> None: ...

class VideoAggregatorConvertPadClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAggregatorConvertPadClass()
    """
    @property
    def parent_class(self) -> VideoAggregatorPadClass: ...
    @property
    def create_conversion_info(
        self,
    ) -> Callable[[VideoAggregatorConvertPad, VideoAggregator, VideoInfo], None]: ...

class VideoAggregatorConvertPadPrivate(_gi.Struct): ...

class VideoAggregatorPad(GstBase.AggregatorPad):
    """
    :Constructors:

    ::

        VideoAggregatorPad(**properties)

    Object GstVideoAggregatorPad

    Properties from GstVideoAggregatorPad:
      zorder -> guint: Z-Order
        Z Order of the picture
      repeat-after-eos -> gboolean: Repeat After EOS
        Repeat the last frame after EOS until all pads are EOS
      max-last-buffer-repeat -> guint64: Max Last Buffer Repeat
        Repeat last buffer for time (in ns, -1=until EOS), behaviour on EOS is not affected

    Signals from GstAggregatorPad:
      buffer-consumed (GstBuffer)

    Properties from GstAggregatorPad:
      emit-signals -> gboolean: Emit signals
        Send signals to signal data consumption

    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)

    Properties from GstPad:
      caps -> GstCaps: Caps
        The capabilities of the pad
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
      offset -> gint64: Offset
        The running time offset of the pad

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(GstBase.AggregatorPad.Props):
        max_last_buffer_repeat: int
        repeat_after_eos: bool
        zorder: int
        emit_signals: bool
        caps: Gst.Caps
        direction: Gst.PadDirection
        offset: int
        template: Gst.PadTemplate
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GstBase.AggregatorPad: ...
    @property
    def info(self) -> VideoInfo: ...
    @property
    def priv(self) -> VideoAggregatorPadPrivate: ...
    def __init__(
        self,
        *,
        max_last_buffer_repeat: int = ...,
        repeat_after_eos: bool = ...,
        zorder: int = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_clean_frame(
        self, videoaggregator: VideoAggregator, prepared_frame: VideoFrame
    ) -> None: ...
    def do_prepare_frame(
        self,
        videoaggregator: VideoAggregator,
        buffer: Gst.Buffer,
        prepared_frame: VideoFrame,
    ) -> bool: ...
    def do_prepare_frame_finish(
        self, videoaggregator: VideoAggregator, prepared_frame: VideoFrame
    ) -> None: ...
    def do_prepare_frame_start(
        self,
        videoaggregator: VideoAggregator,
        buffer: Gst.Buffer,
        prepared_frame: VideoFrame,
    ) -> None: ...
    def do_update_conversion_info(self) -> None: ...
    def get_current_buffer(self) -> Gst.Buffer: ...
    def get_prepared_frame(self) -> VideoFrame: ...
    def has_current_buffer(self) -> bool: ...
    def set_needs_alpha(self, needs_alpha: bool) -> None: ...

class VideoAggregatorPadClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAggregatorPadClass()
    """
    @property
    def parent_class(self) -> GstBase.AggregatorPadClass: ...
    @property
    def update_conversion_info(self) -> Callable[[VideoAggregatorPad], None]: ...
    @property
    def prepare_frame(
        self,
    ) -> Callable[
        [VideoAggregatorPad, VideoAggregator, Gst.Buffer, VideoFrame], bool
    ]: ...
    @property
    def clean_frame(
        self,
    ) -> Callable[[VideoAggregatorPad, VideoAggregator, VideoFrame], None]: ...
    @property
    def prepare_frame_start(
        self,
    ) -> Callable[
        [VideoAggregatorPad, VideoAggregator, Gst.Buffer, VideoFrame], None
    ]: ...
    @property
    def prepare_frame_finish(
        self,
    ) -> Callable[[VideoAggregatorPad, VideoAggregator, VideoFrame], None]: ...

class VideoAggregatorPadPrivate(_gi.Struct): ...

class VideoAggregatorParallelConvertPad(VideoAggregatorConvertPad):
    """
    :Constructors:

    ::

        VideoAggregatorParallelConvertPad(**properties)

    Object GstVideoAggregatorParallelConvertPad

    Properties from GstVideoAggregatorConvertPad:
      converter-config -> GstStructure: Converter configuration
        A GstStructure describing the configuration that should be used when scaling and converting this pad's video frames

    Properties from GstVideoAggregatorPad:
      zorder -> guint: Z-Order
        Z Order of the picture
      repeat-after-eos -> gboolean: Repeat After EOS
        Repeat the last frame after EOS until all pads are EOS
      max-last-buffer-repeat -> guint64: Max Last Buffer Repeat
        Repeat last buffer for time (in ns, -1=until EOS), behaviour on EOS is not affected

    Signals from GstAggregatorPad:
      buffer-consumed (GstBuffer)

    Properties from GstAggregatorPad:
      emit-signals -> gboolean: Emit signals
        Send signals to signal data consumption

    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)

    Properties from GstPad:
      caps -> GstCaps: Caps
        The capabilities of the pad
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
      offset -> gint64: Offset
        The running time offset of the pad

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(VideoAggregatorConvertPad.Props):
        converter_config: Gst.Structure
        max_last_buffer_repeat: int
        repeat_after_eos: bool
        zorder: int
        emit_signals: bool
        caps: Gst.Caps
        direction: Gst.PadDirection
        offset: int
        template: Gst.PadTemplate
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> VideoAggregatorConvertPad: ...
    def __init__(
        self,
        *,
        converter_config: Gst.Structure = ...,
        max_last_buffer_repeat: int = ...,
        repeat_after_eos: bool = ...,
        zorder: int = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...

class VideoAggregatorParallelConvertPadClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAggregatorParallelConvertPadClass()
    """
    @property
    def parent_class(self) -> VideoAggregatorConvertPadClass: ...

class VideoAggregatorPrivate(_gi.Struct): ...

class VideoAlignment(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAlignment()
    """

    padding_top: int
    padding_bottom: int
    padding_left: int
    padding_right: int
    stride_align: list[int]
    def reset(self) -> None: ...

class VideoAncillary(_gi.Struct):
    """
    :Constructors:

    ::

        VideoAncillary()
    """

    DID: int
    SDID_block_number: int
    data_count: int
    data: bytes

class VideoBarMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoBarMeta()
    """

    meta: Gst.Meta
    field: int
    is_letterbox: bool
    bar_data1: int
    bar_data2: int
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoBufferPool(Gst.BufferPool):
    """
    :Constructors:

    ::

        VideoBufferPool(**properties)
        new() -> Gst.BufferPool

    Object GstVideoBufferPool

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gst.BufferPool.Props):
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def bufferpool(self) -> Gst.BufferPool: ...
    @property
    def priv(self) -> VideoBufferPoolPrivate: ...
    def __init__(self, *, name: str | None = ..., parent: Gst.Object = ...) -> None: ...
    @classmethod
    def new(cls) -> VideoBufferPool: ...

class VideoBufferPoolClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoBufferPoolClass()
    """
    @property
    def parent_class(self) -> Gst.BufferPoolClass: ...

class VideoBufferPoolPrivate(_gi.Struct): ...

class VideoCaptionMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoCaptionMeta()
    """

    meta: Gst.Meta
    caption_type: VideoCaptionType
    data: bytes
    size: int
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoChromaResample(_gi.Struct):
    def free(self) -> None: ...
    def get_info(self) -> tuple[int, int]: ...

class VideoCodecAlphaMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoCodecAlphaMeta()
    """

    meta: Gst.Meta
    buffer: Gst.Buffer
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoCodecFrame(GObject.GBoxed):
    """
    :Constructors:

    ::

        VideoCodecFrame()
    """
    @property
    def ref_count(self) -> int: ...
    @property
    def flags(self) -> int: ...
    system_frame_number: int
    @property
    def decode_frame_number(self) -> int: ...
    @property
    def presentation_frame_number(self) -> int: ...
    dts: int
    pts: int
    duration: int
    distance_from_sync: int
    input_buffer: Gst.Buffer
    output_buffer: Gst.Buffer
    deadline: int
    @property
    def events(self) -> list[None]: ...
    @property
    def user_data(self) -> None: ...
    @property
    def user_data_destroy_notify(self) -> Callable[[None], None]: ...
    def get_user_data(self) -> None: ...
    def ref(self) -> VideoCodecFrame: ...
    # override
    def set_user_data(self, user_data: Any, notify: Callable[..., None]) -> None: ...
    def unref(self) -> None: ...

class VideoCodecState(GObject.GBoxed):
    """
    :Constructors:

    ::

        VideoCodecState()
    """
    @property
    def ref_count(self) -> int: ...
    info: VideoInfo
    caps: Gst.Caps
    codec_data: Gst.Buffer
    allocation_caps: Gst.Caps
    mastering_display_info: VideoMasteringDisplayInfo
    content_light_level: VideoContentLightLevel
    @property
    def padding(self) -> list[None]: ...
    def ref(self) -> VideoCodecState: ...
    def unref(self) -> None: ...

class VideoColorPrimariesInfo(_gi.Struct):
    """
    :Constructors:

    ::

        VideoColorPrimariesInfo()
    """

    primaries: VideoColorPrimaries
    Wx: float
    Wy: float
    Rx: float
    Ry: float
    Gx: float
    Gy: float
    Bx: float
    By: float

class VideoColorimetry(_gi.Struct):
    """
    :Constructors:

    ::

        VideoColorimetry()
    """

    range: VideoColorRange
    matrix: VideoColorMatrix
    transfer: VideoTransferFunction
    primaries: VideoColorPrimaries
    def from_string(self, color: str) -> bool: ...
    def is_equal(self, other: VideoColorimetry) -> bool: ...
    def is_equivalent(
        self, bitdepth: int, other: VideoColorimetry, other_bitdepth: int
    ) -> bool: ...
    def matches(self, color: str) -> bool: ...
    def to_string(self) -> str | None: ...

class VideoContentLightLevel(_gi.Struct):
    """
    :Constructors:

    ::

        VideoContentLightLevel()
    """

    max_content_light_level: int
    max_frame_average_light_level: int
    def add_to_caps(self, caps: Gst.Caps) -> bool: ...
    def from_caps(self, caps: Gst.Caps) -> bool: ...
    def from_string(self, level: str) -> bool: ...
    def init(self) -> None: ...
    def is_equal(self, other: VideoContentLightLevel) -> bool: ...
    def to_string(self) -> str: ...

class VideoConverter(_gi.Struct):
    def frame(self, src: VideoFrame, dest: VideoFrame) -> None: ...
    def frame_finish(self) -> None: ...
    def free(self) -> None: ...
    def get_config(self) -> Gst.Structure: ...
    def get_in_info(self) -> VideoInfo: ...
    def get_out_info(self) -> VideoInfo: ...
    def set_config(self, config: Gst.Structure) -> bool: ...

class VideoCropMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoCropMeta()
    """

    meta: Gst.Meta
    x: int
    y: int
    width: int
    height: int
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoDecoder(Gst.Element):
    """
    :Constructors:

    ::

        VideoDecoder(**properties)

    Object GstVideoDecoder

    Properties from GstVideoDecoder:
      qos -> gboolean: Quality of Service
        Handle Quality-of-Service events from downstream
      max-errors -> gint: Max errors
        Max consecutive decoder errors before returning flow error
      min-force-key-unit-interval -> guint64: Minimum Force Keyunit Interval
        Minimum interval between force-keyunit requests in nanoseconds
      discard-corrupted-frames -> gboolean: Discard Corrupted Frames
        Discard frames marked as corrupted instead of outputting them
      automatic-request-sync-points -> gboolean: Automatic Request Sync Points
        Automatically request sync points when it would be useful
      automatic-request-sync-point-flags -> GstVideoDecoderRequestSyncPointFlags: Automatic Request Sync Point Flags
        Flags to use when automatically requesting sync points

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gst.Element.Props):
        automatic_request_sync_point_flags: VideoDecoderRequestSyncPointFlags
        automatic_request_sync_points: bool
        discard_corrupted_frames: bool
        max_errors: int
        min_force_key_unit_interval: int
        qos: bool
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def element(self) -> Gst.Element: ...
    @property
    def sinkpad(self) -> Gst.Pad: ...
    @property
    def srcpad(self) -> Gst.Pad: ...
    @property
    def stream_lock(self) -> GLib.RecMutex: ...
    @property
    def input_segment(self) -> Gst.Segment: ...
    @property
    def output_segment(self) -> Gst.Segment: ...
    @property
    def priv(self) -> VideoDecoderPrivate: ...
    @property
    def padding(self) -> list[None]: ...
    def __init__(
        self,
        *,
        automatic_request_sync_point_flags: VideoDecoderRequestSyncPointFlags = ...,
        automatic_request_sync_points: bool = ...,
        discard_corrupted_frames: bool = ...,
        max_errors: int = ...,
        min_force_key_unit_interval: int = ...,
        qos: bool = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def add_to_frame(self, n_bytes: int) -> None: ...
    def allocate_output_buffer(self) -> Gst.Buffer | None: ...
    def allocate_output_frame(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def allocate_output_frame_with_params(
        self, frame: VideoCodecFrame, params: Gst.BufferPoolAcquireParams
    ) -> Gst.FlowReturn: ...
    def do_close(self) -> bool: ...
    def do_decide_allocation(self, query: Gst.Query) -> bool: ...
    def do_drain(self) -> Gst.FlowReturn: ...
    def do_finish(self) -> Gst.FlowReturn: ...
    def do_flush(self) -> bool: ...
    def do_getcaps(self, filter: Gst.Caps) -> Gst.Caps: ...
    def do_handle_frame(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def do_handle_missing_data(self, timestamp: int, duration: int) -> bool: ...
    def do_negotiate(self) -> bool: ...
    def do_open(self) -> bool: ...
    def do_parse(
        self, frame: VideoCodecFrame, adapter: GstBase.Adapter, at_eos: bool
    ) -> Gst.FlowReturn: ...
    def do_propose_allocation(self, query: Gst.Query) -> bool: ...
    def do_reset(self, hard: bool) -> bool: ...
    def do_set_format(self, state: VideoCodecState) -> bool: ...
    def do_sink_event(self, event: Gst.Event) -> bool: ...
    def do_sink_query(self, query: Gst.Query) -> bool: ...
    def do_src_event(self, event: Gst.Event) -> bool: ...
    def do_src_query(self, query: Gst.Query) -> bool: ...
    def do_start(self) -> bool: ...
    def do_stop(self) -> bool: ...
    def do_transform_meta(self, frame: VideoCodecFrame, meta: Gst.Meta) -> bool: ...
    def drop_frame(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def drop_subframe(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def finish_frame(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def finish_subframe(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def get_allocator(self) -> tuple[Gst.Allocator, Gst.AllocationParams]: ...
    def get_buffer_pool(self) -> Gst.BufferPool | None: ...
    def get_estimate_rate(self) -> int: ...
    def get_frame(self, frame_number: int) -> VideoCodecFrame | None: ...
    def get_frames(self) -> list[VideoCodecFrame]: ...
    def get_input_subframe_index(self, frame: VideoCodecFrame) -> int: ...
    def get_latency(self) -> tuple[int, int]: ...
    def get_max_decode_time(self, frame: VideoCodecFrame) -> int: ...
    def get_max_errors(self) -> int: ...
    def get_needs_format(self) -> bool: ...
    def get_needs_sync_point(self) -> bool: ...
    def get_oldest_frame(self) -> VideoCodecFrame | None: ...
    def get_output_state(self) -> VideoCodecState | None: ...
    def get_packetized(self) -> bool: ...
    def get_pending_frame_size(self) -> int: ...
    def get_processed_subframe_index(self, frame: VideoCodecFrame) -> int: ...
    def get_qos_proportion(self) -> float: ...
    def get_subframe_mode(self) -> bool: ...
    def have_frame(self) -> Gst.FlowReturn: ...
    def have_last_subframe(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def merge_tags(self, tags: Gst.TagList | None, mode: Gst.TagMergeMode) -> None: ...
    def negotiate(self) -> bool: ...
    def proxy_getcaps(
        self, caps: Gst.Caps | None = None, filter: Gst.Caps | None = None
    ) -> Gst.Caps: ...
    def release_frame(self, frame: VideoCodecFrame) -> None: ...
    def request_sync_point(
        self, frame: VideoCodecFrame, flags: VideoDecoderRequestSyncPointFlags
    ) -> None: ...
    def set_estimate_rate(self, enabled: bool) -> None: ...
    def set_interlaced_output_state(
        self,
        fmt: VideoFormat,
        interlace_mode: VideoInterlaceMode,
        width: int,
        height: int,
        reference: VideoCodecState | None = None,
    ) -> VideoCodecState | None: ...
    def set_latency(self, min_latency: int, max_latency: int) -> None: ...
    def set_max_errors(self, num: int) -> None: ...
    def set_needs_format(self, enabled: bool) -> None: ...
    def set_needs_sync_point(self, enabled: bool) -> None: ...
    def set_output_state(
        self,
        fmt: VideoFormat,
        width: int,
        height: int,
        reference: VideoCodecState | None = None,
    ) -> VideoCodecState | None: ...
    def set_packetized(self, packetized: bool) -> None: ...
    def set_subframe_mode(self, subframe_mode: bool) -> None: ...
    def set_use_default_pad_acceptcaps(self, use: bool) -> None: ...

class VideoDecoderClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoDecoderClass()
    """
    @property
    def element_class(self) -> Gst.ElementClass: ...
    @property
    def open(self) -> Callable[[VideoDecoder], bool]: ...
    @property
    def close(self) -> Callable[[VideoDecoder], bool]: ...
    @property
    def start(self) -> Callable[[VideoDecoder], bool]: ...
    @property
    def stop(self) -> Callable[[VideoDecoder], bool]: ...
    @property
    def parse(
        self,
    ) -> Callable[
        [VideoDecoder, VideoCodecFrame, GstBase.Adapter, bool], Gst.FlowReturn
    ]: ...
    @property
    def set_format(self) -> Callable[[VideoDecoder, VideoCodecState], bool]: ...
    @property
    def reset(self) -> Callable[[VideoDecoder, bool], bool]: ...
    @property
    def finish(self) -> Callable[[VideoDecoder], Gst.FlowReturn]: ...
    @property
    def handle_frame(
        self,
    ) -> Callable[[VideoDecoder, VideoCodecFrame], Gst.FlowReturn]: ...
    @property
    def sink_event(self) -> Callable[[VideoDecoder, Gst.Event], bool]: ...
    @property
    def src_event(self) -> Callable[[VideoDecoder, Gst.Event], bool]: ...
    @property
    def negotiate(self) -> Callable[[VideoDecoder], bool]: ...
    @property
    def decide_allocation(self) -> Callable[[VideoDecoder, Gst.Query], bool]: ...
    @property
    def propose_allocation(self) -> Callable[[VideoDecoder, Gst.Query], bool]: ...
    @property
    def flush(self) -> Callable[[VideoDecoder], bool]: ...
    @property
    def sink_query(self) -> Callable[[VideoDecoder, Gst.Query], bool]: ...
    @property
    def src_query(self) -> Callable[[VideoDecoder, Gst.Query], bool]: ...
    @property
    def getcaps(self) -> Callable[[VideoDecoder, Gst.Caps], Gst.Caps]: ...
    @property
    def drain(self) -> Callable[[VideoDecoder], Gst.FlowReturn]: ...
    @property
    def transform_meta(
        self,
    ) -> Callable[[VideoDecoder, VideoCodecFrame, Gst.Meta], bool]: ...
    @property
    def handle_missing_data(self) -> Callable[[VideoDecoder, int, int], bool]: ...
    @property
    def padding(self) -> list[None]: ...

class VideoDecoderPrivate(_gi.Struct): ...
class VideoDirection(GObject.GInterface, Protocol): ...

class VideoDirectionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        VideoDirectionInterface()
    """
    @property
    def iface(self) -> GObject.TypeInterface: ...

class VideoDither(_gi.Struct):
    def free(self) -> None: ...
    def line(self, line: None, x: int, y: int, width: int) -> None: ...

class VideoEncoder(Gst.Element, Gst.Preset):
    """
    :Constructors:

    ::

        VideoEncoder(**properties)

    Object GstVideoEncoder

    Properties from GstVideoEncoder:
      qos -> gboolean: Qos
        Handle Quality-of-Service events from downstream
      min-force-key-unit-interval -> guint64: Minimum Force Keyunit Interval
        Minimum interval between force-keyunit requests in nanoseconds

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gst.Element.Props):
        min_force_key_unit_interval: int
        qos: bool
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def element(self) -> Gst.Element: ...
    @property
    def sinkpad(self) -> Gst.Pad: ...
    @property
    def srcpad(self) -> Gst.Pad: ...
    @property
    def stream_lock(self) -> GLib.RecMutex: ...
    @property
    def input_segment(self) -> Gst.Segment: ...
    @property
    def output_segment(self) -> Gst.Segment: ...
    @property
    def priv(self) -> VideoEncoderPrivate: ...
    @property
    def padding(self) -> list[None]: ...
    def __init__(
        self,
        *,
        min_force_key_unit_interval: int = ...,
        qos: bool = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def allocate_output_buffer(self, size: int) -> Gst.Buffer: ...
    def allocate_output_frame(
        self, frame: VideoCodecFrame, size: int
    ) -> Gst.FlowReturn: ...
    def do_close(self) -> bool: ...
    def do_decide_allocation(self, query: Gst.Query) -> bool: ...
    def do_finish(self) -> Gst.FlowReturn: ...
    def do_flush(self) -> bool: ...
    def do_getcaps(self, filter: Gst.Caps) -> Gst.Caps: ...
    def do_handle_frame(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def do_negotiate(self) -> bool: ...
    def do_open(self) -> bool: ...
    def do_pre_push(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def do_propose_allocation(self, query: Gst.Query) -> bool: ...
    def do_reset(self, hard: bool) -> bool: ...
    def do_set_format(self, state: VideoCodecState) -> bool: ...
    def do_sink_event(self, event: Gst.Event) -> bool: ...
    def do_sink_query(self, query: Gst.Query) -> bool: ...
    def do_src_event(self, event: Gst.Event) -> bool: ...
    def do_src_query(self, query: Gst.Query) -> bool: ...
    def do_start(self) -> bool: ...
    def do_stop(self) -> bool: ...
    def do_transform_meta(self, frame: VideoCodecFrame, meta: Gst.Meta) -> bool: ...
    def drop_frame(self, frame: VideoCodecFrame) -> None: ...
    def finish_frame(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def finish_subframe(self, frame: VideoCodecFrame) -> Gst.FlowReturn: ...
    def get_allocator(self) -> tuple[Gst.Allocator, Gst.AllocationParams]: ...
    def get_frame(self, frame_number: int) -> VideoCodecFrame | None: ...
    def get_frames(self) -> list[VideoCodecFrame]: ...
    def get_latency(self) -> tuple[int, int]: ...
    def get_max_encode_time(self, frame: VideoCodecFrame) -> int: ...
    def get_min_force_key_unit_interval(self) -> int: ...
    def get_oldest_frame(self) -> VideoCodecFrame | None: ...
    def get_output_state(self) -> VideoCodecState | None: ...
    def is_qos_enabled(self) -> bool: ...
    def merge_tags(self, tags: Gst.TagList | None, mode: Gst.TagMergeMode) -> None: ...
    def negotiate(self) -> bool: ...
    def proxy_getcaps(
        self, caps: Gst.Caps | None = None, filter: Gst.Caps | None = None
    ) -> Gst.Caps: ...
    def release_frame(self, frame: VideoCodecFrame) -> None: ...
    def set_headers(self, headers: list[Gst.Buffer]) -> None: ...
    def set_latency(self, min_latency: int, max_latency: int) -> None: ...
    def set_min_force_key_unit_interval(self, interval: int) -> None: ...
    def set_min_pts(self, min_pts: int) -> None: ...
    def set_output_state(
        self, caps: Gst.Caps, reference: VideoCodecState | None = None
    ) -> VideoCodecState | None: ...
    def set_qos_enabled(self, enabled: bool) -> None: ...

class VideoEncoderClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoEncoderClass()
    """
    @property
    def element_class(self) -> Gst.ElementClass: ...
    @property
    def open(self) -> Callable[[VideoEncoder], bool]: ...
    @property
    def close(self) -> Callable[[VideoEncoder], bool]: ...
    @property
    def start(self) -> Callable[[VideoEncoder], bool]: ...
    @property
    def stop(self) -> Callable[[VideoEncoder], bool]: ...
    @property
    def set_format(self) -> Callable[[VideoEncoder, VideoCodecState], bool]: ...
    @property
    def handle_frame(
        self,
    ) -> Callable[[VideoEncoder, VideoCodecFrame], Gst.FlowReturn]: ...
    @property
    def reset(self) -> Callable[[VideoEncoder, bool], bool]: ...
    @property
    def finish(self) -> Callable[[VideoEncoder], Gst.FlowReturn]: ...
    @property
    def pre_push(self) -> Callable[[VideoEncoder, VideoCodecFrame], Gst.FlowReturn]: ...
    @property
    def getcaps(self) -> Callable[[VideoEncoder, Gst.Caps], Gst.Caps]: ...
    @property
    def sink_event(self) -> Callable[[VideoEncoder, Gst.Event], bool]: ...
    @property
    def src_event(self) -> Callable[[VideoEncoder, Gst.Event], bool]: ...
    @property
    def negotiate(self) -> Callable[[VideoEncoder], bool]: ...
    @property
    def decide_allocation(self) -> Callable[[VideoEncoder, Gst.Query], bool]: ...
    @property
    def propose_allocation(self) -> Callable[[VideoEncoder, Gst.Query], bool]: ...
    @property
    def flush(self) -> Callable[[VideoEncoder], bool]: ...
    @property
    def sink_query(self) -> Callable[[VideoEncoder, Gst.Query], bool]: ...
    @property
    def src_query(self) -> Callable[[VideoEncoder, Gst.Query], bool]: ...
    @property
    def transform_meta(
        self,
    ) -> Callable[[VideoEncoder, VideoCodecFrame, Gst.Meta], bool]: ...

class VideoEncoderPrivate(_gi.Struct): ...

class VideoFilter(GstBase.BaseTransform):
    """
    :Constructors:

    ::

        VideoFilter(**properties)

    Object GstVideoFilter

    Properties from GstBaseTransform:
      qos -> gboolean: QoS
        Handle Quality-of-Service events

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(GstBase.BaseTransform.Props):
        qos: bool
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def element(self) -> GstBase.BaseTransform: ...
    @property
    def negotiated(self) -> bool: ...
    @property
    def in_info(self) -> VideoInfo: ...
    @property
    def out_info(self) -> VideoInfo: ...
    def __init__(
        self, *, qos: bool = ..., name: str | None = ..., parent: Gst.Object = ...
    ) -> None: ...
    def do_set_info(
        self,
        incaps: Gst.Caps,
        in_info: VideoInfo,
        outcaps: Gst.Caps,
        out_info: VideoInfo,
    ) -> bool: ...
    def do_transform_frame(
        self, inframe: VideoFrame, outframe: VideoFrame
    ) -> Gst.FlowReturn: ...
    def do_transform_frame_ip(self, frame: VideoFrame) -> Gst.FlowReturn: ...

class VideoFilterClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoFilterClass()
    """
    @property
    def parent_class(self) -> GstBase.BaseTransformClass: ...
    @property
    def set_info(
        self,
    ) -> Callable[[VideoFilter, Gst.Caps, VideoInfo, Gst.Caps, VideoInfo], bool]: ...
    @property
    def transform_frame(
        self,
    ) -> Callable[[VideoFilter, VideoFrame, VideoFrame], Gst.FlowReturn]: ...
    @property
    def transform_frame_ip(
        self,
    ) -> Callable[[VideoFilter, VideoFrame], Gst.FlowReturn]: ...

class VideoFormatInfo(_gi.Struct):
    """
    :Constructors:

    ::

        VideoFormatInfo()
    """

    format: VideoFormat
    name: str
    description: str
    flags: VideoFormatFlags
    bits: int
    n_components: int
    shift: list[int]
    depth: list[int]
    pixel_stride: list[int]
    n_planes: int
    plane: list[int]
    poffset: list[int]
    w_sub: list[int]
    h_sub: list[int]
    unpack_format: VideoFormat
    unpack_func: Callable[
        [VideoFormatInfo, VideoPackFlags, None, None, int, int, int, int], None
    ]
    pack_lines: int
    pack_func: Callable[
        [
            VideoFormatInfo,
            VideoPackFlags,
            None,
            int,
            None,
            int,
            VideoChromaSite,
            int,
            int,
        ],
        None,
    ]
    tile_mode: VideoTileMode
    tile_ws: int
    tile_hs: int
    tile_info: list[VideoTileInfo]
    def component(self, plane: int) -> int: ...
    def extrapolate_stride(self, plane: int, stride: int) -> int: ...

class VideoFrame(_gi.Struct):
    """
    :Constructors:

    ::

        VideoFrame()
    """

    info: VideoInfo
    flags: VideoFrameFlags
    buffer: Gst.Buffer
    meta: None
    id: int
    data: list[None]
    def copy(self, src: VideoFrame) -> bool: ...
    def copy_plane(self, src: VideoFrame, plane: int) -> bool: ...
    @staticmethod
    def map(
        info: VideoInfo, buffer: Gst.Buffer, flags: Gst.MapFlags
    ) -> tuple[bool, VideoFrame]: ...
    @staticmethod
    def map_id(
        info: VideoInfo, buffer: Gst.Buffer, id: int, flags: Gst.MapFlags
    ) -> tuple[bool, VideoFrame]: ...
    def unmap(self) -> None: ...

class VideoGLTextureUploadMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoGLTextureUploadMeta()
    """

    meta: Gst.Meta
    texture_orientation: VideoGLTextureOrientation
    n_textures: int
    texture_type: list[VideoGLTextureType]
    @property
    def buffer(self) -> Gst.Buffer: ...
    @property
    def user_data(self) -> None: ...
    @property
    def user_data_copy(self) -> Callable[[None], None]: ...
    @property
    def user_data_free(self) -> Callable[[None], None]: ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...
    def upload(self, texture_id: int) -> bool: ...

class VideoInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        VideoInfo()
        new() -> GstVideo.VideoInfo
        new_from_caps(caps:Gst.Caps) -> GstVideo.VideoInfo or None
    """

    finfo: VideoFormatInfo
    interlace_mode: VideoInterlaceMode
    flags: VideoFlags
    width: int
    height: int
    size: int
    views: int
    chroma_site: VideoChromaSite
    colorimetry: VideoColorimetry
    par_n: int
    par_d: int
    fps_n: int
    fps_d: int
    offset: list[int]
    stride: list[int]
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def align(self, align: VideoAlignment) -> bool: ...
    def align_full(self, align: VideoAlignment) -> tuple[bool, int]: ...
    def convert(
        self, src_format: Gst.Format, src_value: int, dest_format: Gst.Format
    ) -> tuple[bool, int]: ...
    def copy(self) -> VideoInfo: ...
    def free(self) -> None: ...
    def from_caps(*args): ...  # FIXME: Override is missing typing annotation
    @staticmethod
    def init() -> VideoInfo: ...
    def is_equal(self, other: VideoInfo) -> bool: ...
    @classmethod
    def new(cls) -> VideoInfo: ...
    @classmethod
    def new_from_caps(cls, caps: Gst.Caps) -> VideoInfo | None: ...
    def set_format(self, format: VideoFormat, width: int, height: int) -> bool: ...
    def set_interlaced_format(
        self, format: VideoFormat, mode: VideoInterlaceMode, width: int, height: int
    ) -> bool: ...
    def to_caps(self) -> Gst.Caps: ...

class VideoInfoDmaDrm(GObject.GBoxed):
    """
    :Constructors:

    ::

        VideoInfoDmaDrm()
        new() -> GstVideo.VideoInfoDmaDrm
        new_from_caps(caps:Gst.Caps) -> GstVideo.VideoInfoDmaDrm or None
    """

    vinfo: VideoInfo
    drm_fourcc: int
    drm_modifier: int
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def free(self) -> None: ...
    @staticmethod
    def from_caps(caps: Gst.Caps) -> tuple[bool, VideoInfoDmaDrm]: ...
    @staticmethod
    def from_video_info(
        info: VideoInfo, modifier: int
    ) -> tuple[bool, VideoInfoDmaDrm]: ...
    @staticmethod
    def init() -> VideoInfoDmaDrm: ...
    @classmethod
    def new(cls) -> VideoInfoDmaDrm: ...
    @classmethod
    def new_from_caps(cls, caps: Gst.Caps) -> VideoInfoDmaDrm | None: ...
    def to_caps(self) -> Gst.Caps | None: ...
    def to_video_info(self) -> tuple[bool, VideoInfo]: ...

class VideoMasteringDisplayInfo(_gi.Struct):
    """
    :Constructors:

    ::

        VideoMasteringDisplayInfo()
    """

    display_primaries: list[VideoMasteringDisplayInfoCoordinates]
    white_point: VideoMasteringDisplayInfoCoordinates
    max_display_mastering_luminance: int
    min_display_mastering_luminance: int
    def add_to_caps(self, caps: Gst.Caps) -> bool: ...
    def from_caps(self, caps: Gst.Caps) -> bool: ...
    @staticmethod
    def from_string(mastering: str) -> tuple[bool, VideoMasteringDisplayInfo]: ...
    def init(self) -> None: ...
    def is_equal(self, other: VideoMasteringDisplayInfo) -> bool: ...
    def to_string(self) -> str: ...

class VideoMasteringDisplayInfoCoordinates(_gi.Struct):
    """
    :Constructors:

    ::

        VideoMasteringDisplayInfoCoordinates()
    """

    x: int
    y: int

class VideoMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoMeta()
    """

    meta: Gst.Meta
    buffer: Gst.Buffer
    flags: VideoFrameFlags
    format: VideoFormat
    id: int
    width: int
    height: int
    n_planes: int
    offset: list[int]
    stride: list[int]
    alignment: VideoAlignment
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...
    def get_plane_height(self) -> tuple[bool, list[int]]: ...
    def get_plane_size(self) -> tuple[bool, list[int]]: ...
    def map(
        self, plane: int, info: Gst.MapInfo, flags: Gst.MapFlags
    ) -> tuple[bool, None, int]: ...
    def set_alignment(self, alignment: VideoAlignment) -> bool: ...
    def unmap(self, plane: int, info: Gst.MapInfo) -> bool: ...

class VideoMetaTransform(_gi.Struct):
    """
    :Constructors:

    ::

        VideoMetaTransform()
    """

    in_info: VideoInfo
    out_info: VideoInfo
    @staticmethod
    def scale_get_quark() -> int: ...

class VideoMultiviewFlagsSet(Gst.FlagSet): ...

class VideoOrientation(GObject.GInterface, Protocol):
    """
    Interface GstVideoOrientation
    """
    @staticmethod
    def from_tag(taglist: Gst.TagList) -> tuple[bool, VideoOrientationMethod]: ...
    def get_hcenter(self) -> tuple[bool, int]: ...
    def get_hflip(self) -> tuple[bool, bool]: ...
    def get_vcenter(self) -> tuple[bool, int]: ...
    def get_vflip(self) -> tuple[bool, bool]: ...
    def set_hcenter(self, center: int) -> bool: ...
    def set_hflip(self, flip: bool) -> bool: ...
    def set_vcenter(self, center: int) -> bool: ...
    def set_vflip(self, flip: bool) -> bool: ...

class VideoOrientationInterface(_gi.Struct):
    """
    :Constructors:

    ::

        VideoOrientationInterface()
    """
    @property
    def iface(self) -> GObject.TypeInterface: ...
    @property
    def get_hflip(self) -> Callable[[VideoOrientation], tuple[bool, bool]]: ...
    @property
    def get_vflip(self) -> Callable[[VideoOrientation], tuple[bool, bool]]: ...
    @property
    def get_hcenter(self) -> Callable[[VideoOrientation], tuple[bool, int]]: ...
    @property
    def get_vcenter(self) -> Callable[[VideoOrientation], tuple[bool, int]]: ...
    @property
    def set_hflip(self) -> Callable[[VideoOrientation, bool], bool]: ...
    @property
    def set_vflip(self) -> Callable[[VideoOrientation, bool], bool]: ...
    @property
    def set_hcenter(self) -> Callable[[VideoOrientation, int], bool]: ...
    @property
    def set_vcenter(self) -> Callable[[VideoOrientation, int], bool]: ...

class VideoOverlay(GObject.GInterface, Protocol):
    """
    Interface GstVideoOverlay
    """
    def expose(self) -> None: ...
    def got_window_handle(self, handle: int) -> None: ...
    def handle_events(self, handle_events: bool) -> None: ...
    @staticmethod
    def install_properties(oclass: GObject.ObjectClass, last_prop_id: int) -> None: ...
    def prepare_window_handle(self) -> None: ...
    @staticmethod
    def set_property(
        object: GObject.Object, last_prop_id: int, property_id: int, value: Any
    ) -> bool: ...
    def set_render_rectangle(self, x: int, y: int, width: int, height: int) -> bool: ...
    def set_window_handle(self, handle: int) -> None: ...

class VideoOverlayComposition(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(rectangle:GstVideo.VideoOverlayRectangle=None) -> GstVideo.VideoOverlayComposition
    """
    @staticmethod
    def __new__(
        cls: type[Self], rectangle: VideoOverlayRectangle | None = None
    ) -> Self: ...
    def add_rectangle(self, rectangle: VideoOverlayRectangle) -> None: ...
    def blend(self, video_buf: VideoFrame) -> bool: ...
    def copy(self) -> VideoOverlayComposition: ...
    def get_rectangle(self, n: int) -> VideoOverlayRectangle | None: ...
    def get_seqnum(self) -> int: ...
    def make_writable(self) -> VideoOverlayComposition: ...
    def n_rectangles(self) -> int: ...
    @classmethod
    def new(
        cls, rectangle: VideoOverlayRectangle | None = None
    ) -> VideoOverlayComposition: ...

class VideoOverlayCompositionMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoOverlayCompositionMeta()
    """

    meta: Gst.Meta
    overlay: VideoOverlayComposition
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoOverlayInterface(_gi.Struct):
    """
    :Constructors:

    ::

        VideoOverlayInterface()
    """
    @property
    def iface(self) -> GObject.TypeInterface: ...
    @property
    def expose(self) -> Callable[[VideoOverlay], None]: ...
    @property
    def handle_events(self) -> Callable[[VideoOverlay, bool], None]: ...
    @property
    def set_render_rectangle(
        self,
    ) -> Callable[[VideoOverlay, int, int, int, int], None]: ...
    @property
    def set_window_handle(self) -> Callable[[VideoOverlay, int], None]: ...

class VideoOverlayRectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_raw(pixels:Gst.Buffer, render_x:int, render_y:int, render_width:int, render_height:int, flags:GstVideo.VideoOverlayFormatFlags) -> GstVideo.VideoOverlayRectangle
    """
    def copy(self) -> VideoOverlayRectangle: ...
    def get_flags(self) -> VideoOverlayFormatFlags: ...
    def get_global_alpha(self) -> float: ...
    def get_pixels_argb(self, flags: VideoOverlayFormatFlags) -> Gst.Buffer: ...
    def get_pixels_ayuv(self, flags: VideoOverlayFormatFlags) -> Gst.Buffer: ...
    def get_pixels_raw(self, flags: VideoOverlayFormatFlags) -> Gst.Buffer: ...
    def get_pixels_unscaled_argb(
        self, flags: VideoOverlayFormatFlags
    ) -> Gst.Buffer: ...
    def get_pixels_unscaled_ayuv(
        self, flags: VideoOverlayFormatFlags
    ) -> Gst.Buffer: ...
    def get_pixels_unscaled_raw(self, flags: VideoOverlayFormatFlags) -> Gst.Buffer: ...
    def get_render_rectangle(self) -> tuple[bool, int, int, int, int]: ...
    def get_seqnum(self) -> int: ...
    @classmethod
    def new_raw(
        cls,
        pixels: Gst.Buffer,
        render_x: int,
        render_y: int,
        render_width: int,
        render_height: int,
        flags: VideoOverlayFormatFlags,
    ) -> VideoOverlayRectangle: ...
    def set_global_alpha(self, global_alpha: float) -> None: ...
    def set_render_rectangle(
        self, render_x: int, render_y: int, render_width: int, render_height: int
    ) -> None: ...

class VideoRectangle(_gi.Struct):
    """
    :Constructors:

    ::

        VideoRectangle()
    """

    x: int
    y: int
    w: int
    h: int

class VideoRegionOfInterestMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoRegionOfInterestMeta()
    """

    meta: Gst.Meta
    roi_type: int
    id: int
    parent_id: int
    x: int
    y: int
    w: int
    h: int
    params: list[None]
    def add_param(self, s: Gst.Structure) -> None: ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...
    def get_param(self, name: str) -> Gst.Structure | None: ...

class VideoResampler(_gi.Struct):
    """
    :Constructors:

    ::

        VideoResampler()
    """

    in_size: int
    out_size: int
    max_taps: int
    n_phases: int
    offset: int
    phase: int
    n_taps: int
    taps: float
    def clear(self) -> None: ...
    def init(
        self,
        method: VideoResamplerMethod,
        flags: VideoResamplerFlags,
        n_phases: int,
        n_taps: int,
        shift: float,
        in_size: int,
        out_size: int,
        options: Gst.Structure,
    ) -> bool: ...

class VideoSEIUserDataUnregisteredMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoSEIUserDataUnregisteredMeta()
    """

    meta: Gst.Meta
    uuid: bytes
    data: int
    size: int
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoScaler(_gi.Struct):
    def free(self) -> None: ...
    def get_coeff(self, out_offset: int) -> tuple[float, int, int]: ...
    def get_max_taps(self) -> int: ...
    def horizontal(
        self, format: VideoFormat, src: None, dest: None, dest_offset: int, width: int
    ) -> None: ...
    def vertical(
        self,
        format: VideoFormat,
        src_lines: None,
        dest: None,
        dest_offset: int,
        width: int,
    ) -> None: ...

class VideoSink(GstBase.BaseSink):
    """
    :Constructors:

    ::

        VideoSink(**properties)

    Object GstVideoSink

    Properties from GstVideoSink:
      show-preroll-frame -> gboolean: Show preroll frame
        Whether to render video frames during preroll

    Properties from GstBaseSink:
      sync -> gboolean: Sync
        Sync on the clock
      max-lateness -> gint64: Max Lateness
        Maximum number of nanoseconds that a buffer can be late before it is dropped (-1 unlimited)
      qos -> gboolean: Qos
        Generate Quality-of-Service events upstream
      async -> gboolean: Async
        Go asynchronously to PAUSED
      ts-offset -> gint64: TS Offset
        Timestamp offset in nanoseconds
      enable-last-sample -> gboolean: Enable Last Buffer
        Enable the last-sample property
      last-sample -> GstSample: Last Sample
        The last sample received in the sink
      blocksize -> guint: Block size
        Size in bytes to pull per buffer (0 = default)
      render-delay -> guint64: Render Delay
        Additional render delay of the sink in nanoseconds
      throttle-time -> guint64: Throttle time
        The time to keep between rendered buffers (0 = disabled)
      max-bitrate -> guint64: Max Bitrate
        The maximum bits per second to render (0 = disabled)
      processing-deadline -> guint64: Processing deadline
        Maximum processing time for a buffer in nanoseconds
      stats -> GstStructure: Statistics
        Sink Statistics

    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()

    Signals from GstObject:
      deep-notify (GstObject, GParam)

    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
      parent -> GstObject: Parent
        The parent of the object

    Signals from GObject:
      notify (GParam)
    """
    class Props(GstBase.BaseSink.Props):
        show_preroll_frame: bool
        blocksize: int
        enable_last_sample: bool
        last_sample: Gst.Sample | None
        max_bitrate: int
        max_lateness: int
        processing_deadline: int
        qos: bool
        render_delay: int
        stats: Gst.Structure
        sync: bool
        throttle_time: int
        ts_offset: int
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def element(self) -> GstBase.BaseSink: ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def priv(self) -> VideoSinkPrivate: ...
    def __init__(
        self,
        *,
        show_preroll_frame: bool = ...,
        blocksize: int = ...,
        enable_last_sample: bool = ...,
        max_bitrate: int = ...,
        max_lateness: int = ...,
        processing_deadline: int = ...,
        qos: bool = ...,
        render_delay: int = ...,
        sync: bool = ...,
        throttle_time: int = ...,
        ts_offset: int = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    @staticmethod
    def center_rect(
        src: VideoRectangle, dst: VideoRectangle, scaling: bool
    ) -> VideoRectangle: ...
    def do_set_info(self, caps: Gst.Caps, info: VideoInfo) -> bool: ...
    def do_show_frame(self, buf: Gst.Buffer) -> Gst.FlowReturn: ...

class VideoSinkClass(_gi.Struct):
    """
    :Constructors:

    ::

        VideoSinkClass()
    """
    @property
    def parent_class(self) -> GstBase.BaseSinkClass: ...
    @property
    def show_frame(self) -> Callable[[VideoSink, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def set_info(self) -> Callable[[VideoSink, Gst.Caps, VideoInfo], bool]: ...

class VideoSinkPrivate(_gi.Struct): ...

class VideoTileInfo(_gi.Struct):
    """
    :Constructors:

    ::

        VideoTileInfo()
    """

    width: int
    height: int
    stride: int
    size: int
    @property
    def padding(self) -> list[int]: ...

class VideoTimeCode(GObject.GBoxed):
    """
    :Constructors:

    ::

        VideoTimeCode()
        new(fps_n:int, fps_d:int, latest_daily_jam:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, hours:int, minutes:int, seconds:int, frames:int, field_count:int) -> GstVideo.VideoTimeCode
        new_empty() -> GstVideo.VideoTimeCode
        new_from_date_time(fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> GstVideo.VideoTimeCode
        new_from_date_time_full(fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> GstVideo.VideoTimeCode or None
        new_from_string(tc_str:str) -> GstVideo.VideoTimeCode or None
    """

    config: VideoTimeCodeConfig
    hours: int
    minutes: int
    seconds: int
    frames: int
    field_count: int
    def add_frames(self, frames: int) -> None: ...
    def add_interval(self, tc_inter: VideoTimeCodeInterval) -> VideoTimeCode | None: ...
    def clear(self) -> None: ...
    def compare(self, tc2: VideoTimeCode) -> int: ...
    def copy(self) -> VideoTimeCode: ...
    def frames_since_daily_jam(self) -> int: ...
    def free(self) -> None: ...
    def increment_frame(self) -> None: ...
    def init(
        self,
        fps_n: int,
        fps_d: int,
        latest_daily_jam: GLib.DateTime | None,
        flags: VideoTimeCodeFlags,
        hours: int,
        minutes: int,
        seconds: int,
        frames: int,
        field_count: int,
    ) -> None: ...
    def init_from_date_time(
        self,
        fps_n: int,
        fps_d: int,
        dt: GLib.DateTime,
        flags: VideoTimeCodeFlags,
        field_count: int,
    ) -> None: ...
    def init_from_date_time_full(
        self,
        fps_n: int,
        fps_d: int,
        dt: GLib.DateTime,
        flags: VideoTimeCodeFlags,
        field_count: int,
    ) -> bool: ...
    def is_valid(self) -> bool: ...
    @classmethod
    def new(
        cls,
        fps_n: int,
        fps_d: int,
        latest_daily_jam: GLib.DateTime,
        flags: VideoTimeCodeFlags,
        hours: int,
        minutes: int,
        seconds: int,
        frames: int,
        field_count: int,
    ) -> VideoTimeCode: ...
    @classmethod
    def new_empty(cls) -> VideoTimeCode: ...
    @classmethod
    def new_from_date_time(
        cls,
        fps_n: int,
        fps_d: int,
        dt: GLib.DateTime,
        flags: VideoTimeCodeFlags,
        field_count: int,
    ) -> VideoTimeCode: ...
    @classmethod
    def new_from_date_time_full(
        cls,
        fps_n: int,
        fps_d: int,
        dt: GLib.DateTime,
        flags: VideoTimeCodeFlags,
        field_count: int,
    ) -> VideoTimeCode | None: ...
    @classmethod
    def new_from_string(cls, tc_str: str) -> VideoTimeCode | None: ...
    def nsec_since_daily_jam(self) -> int: ...
    def to_date_time(self) -> GLib.DateTime | None: ...
    def to_string(self) -> str: ...

class VideoTimeCodeConfig(_gi.Struct):
    """
    :Constructors:

    ::

        VideoTimeCodeConfig()
    """

    fps_n: int
    fps_d: int
    flags: VideoTimeCodeFlags
    latest_daily_jam: GLib.DateTime

class VideoTimeCodeInterval(GObject.GBoxed):
    """
    :Constructors:

    ::

        VideoTimeCodeInterval()
        new(hours:int, minutes:int, seconds:int, frames:int) -> GstVideo.VideoTimeCodeInterval
        new_from_string(tc_inter_str:str) -> GstVideo.VideoTimeCodeInterval or None
    """

    hours: int
    minutes: int
    seconds: int
    frames: int
    def clear(self) -> None: ...
    def copy(self) -> VideoTimeCodeInterval: ...
    def free(self) -> None: ...
    def init(self, hours: int, minutes: int, seconds: int, frames: int) -> None: ...
    @classmethod
    def new(
        cls, hours: int, minutes: int, seconds: int, frames: int
    ) -> VideoTimeCodeInterval: ...
    @classmethod
    def new_from_string(cls, tc_inter_str: str) -> VideoTimeCodeInterval | None: ...

class VideoTimeCodeMeta(_gi.Struct):
    """
    :Constructors:

    ::

        VideoTimeCodeMeta()
    """

    meta: Gst.Meta
    tc: VideoTimeCode
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class VideoVBIEncoder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(format:GstVideo.VideoFormat, pixel_width:int) -> GstVideo.VideoVBIEncoder or None
    """
    @staticmethod
    def __new__(cls: type[Self], format: VideoFormat, pixel_width: int) -> Self: ...
    def add_ancillary(
        self, composite: bool, DID: int, SDID_block_number: int, data: Sequence[int]
    ) -> bool: ...
    def copy(self) -> VideoVBIEncoder: ...
    def free(self) -> None: ...
    @classmethod
    def new(cls, format: VideoFormat, pixel_width: int) -> VideoVBIEncoder | None: ...
    def write_line(self, data: int) -> None: ...

class VideoVBIParser(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(format:GstVideo.VideoFormat, pixel_width:int) -> GstVideo.VideoVBIParser or None
    """
    @staticmethod
    def __new__(cls: type[Self], format: VideoFormat, pixel_width: int) -> Self: ...
    def add_line(self, data: Sequence[int]) -> None: ...
    def copy(self) -> VideoVBIParser: ...
    def free(self) -> None: ...
    def get_ancillary(self) -> tuple[VideoVBIParserResult, VideoAncillary]: ...
    @classmethod
    def new(cls, format: VideoFormat, pixel_width: int) -> VideoVBIParser | None: ...

class NavigationModifierType(GObject.GFlags):
    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    HYPER_MASK = 134217728
    LOCK_MASK = 2
    MASK = 469770239
    META_MASK = 268435456
    MOD1_MASK = 8
    MOD2_MASK = 16
    MOD3_MASK = 32
    MOD4_MASK = 64
    MOD5_MASK = 128
    NONE = 0
    SHIFT_MASK = 1
    SUPER_MASK = 67108864

class VideoBufferFlags(GObject.GFlags):
    BOTTOM_FIELD = 8388608
    FIRST_IN_BUNDLE = 33554432
    INTERLACED = 1048576
    LAST = 268435456
    MARKER = 512
    MULTIPLE_VIEW = 16777216
    ONEFIELD = 8388608
    RFF = 4194304
    TFF = 2097152
    TOP_FIELD = 10485760

class VideoChromaFlags(GObject.GFlags):
    INTERLACED = 1
    NONE = 0

class VideoChromaSite(GObject.GFlags):
    ALT_LINE = 8
    COSITED = 6
    DV = 14
    H_COSITED = 2
    JPEG = 1
    MPEG2 = 2
    NONE = 1
    UNKNOWN = 0
    V_COSITED = 4
    @staticmethod
    def from_string(s: str) -> VideoChromaSite: ...
    @staticmethod
    def to_string(site: VideoChromaSite) -> str | None: ...

class VideoCodecFrameFlags(GObject.GFlags):
    CORRUPTED = 16
    DECODE_ONLY = 1
    FORCE_KEYFRAME = 4
    FORCE_KEYFRAME_HEADERS = 8
    SYNC_POINT = 2

class VideoDecoderRequestSyncPointFlags(GObject.GFlags):
    CORRUPT_OUTPUT = 2
    DISCARD_INPUT = 1

class VideoDitherFlags(GObject.GFlags):
    INTERLACED = 1
    NONE = 0
    QUANTIZE = 2

class VideoFlags(GObject.GFlags):
    NONE = 0
    PREMULTIPLIED_ALPHA = 2
    VARIABLE_FPS = 1

class VideoFormatFlags(GObject.GFlags):
    ALPHA = 8
    COMPLEX = 64
    GRAY = 4
    LE = 16
    PALETTE = 32
    RGB = 2
    SUBTILES = 512
    TILED = 256
    UNPACK = 128
    YUV = 1

class VideoFrameFlags(GObject.GFlags):
    BOTTOM_FIELD = 8
    FIRST_IN_BUNDLE = 32
    INTERLACED = 1
    MULTIPLE_VIEW = 16
    NONE = 0
    ONEFIELD = 8
    RFF = 4
    TFF = 2
    TOP_FIELD = 10

class VideoFrameMapFlags(GObject.GFlags):
    LAST = 16777216
    NO_REF = 65536

class VideoMultiviewFlags(GObject.GFlags):
    HALF_ASPECT = 16384
    LEFT_FLIPPED = 2
    LEFT_FLOPPED = 4
    MIXED_MONO = 32768
    NONE = 0
    RIGHT_FLIPPED = 8
    RIGHT_FLOPPED = 16
    RIGHT_VIEW_FIRST = 1

class VideoOverlayFormatFlags(GObject.GFlags):
    GLOBAL_ALPHA = 2
    NONE = 0
    PREMULTIPLIED_ALPHA = 1

class VideoPackFlags(GObject.GFlags):
    INTERLACED = 2
    NONE = 0
    TRUNCATE_RANGE = 1

class VideoResamplerFlags(GObject.GFlags):
    HALF_TAPS = 1
    NONE = 0

class VideoScalerFlags(GObject.GFlags):
    INTERLACED = 1
    NONE = 0

class VideoTimeCodeFlags(GObject.GFlags):
    DROP_FRAME = 1
    INTERLACED = 2
    NONE = 0

class AncillaryMetaField(GObject.GEnum):
    INTERLACED_FIRST = 16
    INTERLACED_SECOND = 17
    PROGRESSIVE = 0

class ColorBalanceType(GObject.GEnum):
    HARDWARE = 0
    SOFTWARE = 1

class NavigationCommand(GObject.GEnum):
    ACTIVATE = 24
    DOWN = 23
    INVALID = 0
    LEFT = 20
    MENU1 = 1
    MENU2 = 2
    MENU3 = 3
    MENU4 = 4
    MENU5 = 5
    MENU6 = 6
    MENU7 = 7
    NEXT_ANGLE = 31
    PREV_ANGLE = 30
    RIGHT = 21
    UP = 22

class NavigationEventType(GObject.GEnum):
    COMMAND = 6
    INVALID = 0
    KEY_PRESS = 1
    KEY_RELEASE = 2
    MOUSE_BUTTON_PRESS = 3
    MOUSE_BUTTON_RELEASE = 4
    MOUSE_DOUBLE_CLICK = 13
    MOUSE_MOVE = 5
    MOUSE_SCROLL = 7
    TOUCH_CANCEL = 12
    TOUCH_DOWN = 8
    TOUCH_FRAME = 11
    TOUCH_MOTION = 9
    TOUCH_UP = 10

class NavigationMessageType(GObject.GEnum):
    ANGLES_CHANGED = 3
    COMMANDS_CHANGED = 2
    EVENT = 4
    INVALID = 0
    MOUSE_OVER = 1

class NavigationQueryType(GObject.GEnum):
    ANGLES = 2
    COMMANDS = 1
    INVALID = 0

class VideoAFDSpec(GObject.GEnum):
    ATSC_A53 = 1
    DVB_ETSI = 0
    SMPTE_ST2016_1 = 2

class VideoAFDValue(GObject.GEnum):
    GREATER_THAN_16_9 = 4
    UNAVAILABLE = 0

class VideoAlphaMode(GObject.GEnum):
    COPY = 0
    MULT = 2
    SET = 1

class VideoAncillaryDID(GObject.GEnum):
    CAMERA_POSITION = 240
    DELETION = 128
    HANC_3G_AUDIO_DATA_FIRST = 160
    HANC_3G_AUDIO_DATA_LAST = 167
    HANC_ERROR_DETECTION = 244
    HANC_HDTV_AUDIO_DATA_FIRST = 224
    HANC_HDTV_AUDIO_DATA_LAST = 231
    HANC_SDTV_AUDIO_DATA_1_FIRST = 236
    HANC_SDTV_AUDIO_DATA_1_LAST = 239
    HANC_SDTV_AUDIO_DATA_2_FIRST = 248
    HANC_SDTV_AUDIO_DATA_2_LAST = 255
    UNDEFINED = 0

class VideoAncillaryDID16(GObject.GEnum):
    S2016_3_AFD_BAR = 16645
    S334_EIA_608 = 24834
    S334_EIA_708 = 24833

class VideoCaptionType(GObject.GEnum):
    CEA608_RAW = 1
    CEA608_S334_1A = 2
    CEA708_CDP = 4
    CEA708_RAW = 3
    UNKNOWN = 0
    @staticmethod
    def from_caps(caps: Gst.Caps) -> VideoCaptionType: ...
    @staticmethod
    def to_caps(type: VideoCaptionType) -> Gst.Caps: ...

class VideoChromaMethod(GObject.GEnum):
    LINEAR = 1
    NEAREST = 0

class VideoChromaMode(GObject.GEnum):
    DOWNSAMPLE_ONLY = 2
    FULL = 0
    NONE = 3
    UPSAMPLE_ONLY = 1

class VideoColorMatrix(GObject.GEnum):
    BT2020 = 6
    BT601 = 4
    BT709 = 3
    FCC = 2
    RGB = 1
    SMPTE240M = 5
    UNKNOWN = 0
    @staticmethod
    def from_iso(value: int) -> VideoColorMatrix: ...
    @staticmethod
    def get_Kr_Kb(matrix: VideoColorMatrix) -> tuple[bool, float, float]: ...
    @staticmethod
    def to_iso(matrix: VideoColorMatrix) -> int: ...

class VideoColorPrimaries(GObject.GEnum):
    ADOBERGB = 8
    BT2020 = 7
    BT470BG = 3
    BT470M = 2
    BT709 = 1
    EBU3213 = 12
    FILM = 6
    SMPTE170M = 4
    SMPTE240M = 5
    SMPTEEG432 = 11
    SMPTERP431 = 10
    SMPTEST428 = 9
    UNKNOWN = 0
    @staticmethod
    def from_iso(value: int) -> VideoColorPrimaries: ...
    @staticmethod
    def get_info(primaries: VideoColorPrimaries) -> VideoColorPrimariesInfo: ...
    @staticmethod
    def is_equivalent(
        primaries: VideoColorPrimaries, other: VideoColorPrimaries
    ) -> bool: ...
    @staticmethod
    def to_iso(primaries: VideoColorPrimaries) -> int: ...

class VideoColorRange(GObject.GEnum):
    UNKNOWN = 0
    @staticmethod
    def offsets(
        range: VideoColorRange, info: VideoFormatInfo
    ) -> tuple[list[int], list[int]]: ...

class VideoDitherMethod(GObject.GEnum):
    BAYER = 4
    FLOYD_STEINBERG = 2
    NONE = 0
    SIERRA_LITE = 3
    VERTERR = 1

class VideoFieldOrder(GObject.GEnum):
    BOTTOM_FIELD_FIRST = 2
    TOP_FIELD_FIRST = 1
    UNKNOWN = 0
    @staticmethod
    def from_string(order: str) -> VideoFieldOrder: ...
    @staticmethod
    def to_string(order: VideoFieldOrder) -> str: ...

class VideoFormat(GObject.GEnum):
    A420 = 34
    A420_10BE = 54
    A420_10LE = 55
    A420_12BE = 124
    A420_12LE = 123
    A420_16BE = 130
    A420_16LE = 129
    A422 = 117
    A422_10BE = 56
    A422_10LE = 57
    A422_12BE = 122
    A422_12LE = 121
    A422_16BE = 128
    A422_16LE = 127
    A444 = 118
    A444_10BE = 58
    A444_10LE = 59
    A444_12BE = 120
    A444_12LE = 119
    A444_16BE = 126
    A444_16LE = 125
    ABGR = 14
    ABGR64_BE = 109
    ABGR64_LE = 108
    ARGB = 13
    ARGB64 = 39
    ARGB64_BE = 103
    ARGB64_LE = 102
    AV12 = 101
    AYUV = 6
    AYUV64 = 40
    BGR = 16
    BGR10A2_LE = 85
    BGR15 = 32
    BGR16 = 30
    BGRA = 12
    BGRA64_BE = 107
    BGRA64_LE = 106
    BGRP = 100
    BGRX = 8
    DMA_DRM = 114
    ENCODED = 1
    GBR = 48
    GBRA = 65
    GBRA_10BE = 66
    GBRA_10LE = 67
    GBRA_12BE = 70
    GBRA_12LE = 71
    GBR_10BE = 49
    GBR_10LE = 50
    GBR_12BE = 68
    GBR_12LE = 69
    GBR_16BE = 132
    GBR_16LE = 131
    GRAY10_LE16 = 138
    GRAY10_LE32 = 78
    GRAY16_BE = 26
    GRAY16_LE = 27
    GRAY8 = 25
    I420 = 2
    I420_10BE = 42
    I420_10LE = 43
    I420_12BE = 72
    I420_12LE = 73
    I422_10BE = 44
    I422_10LE = 45
    I422_12BE = 74
    I422_12LE = 75
    IYU1 = 38
    IYU2 = 63
    MT2110R = 116
    MT2110T = 115
    NV12 = 23
    NV12_10BE_8L128 = 112
    NV12_10LE32 = 79
    NV12_10LE40 = 81
    NV12_10LE40_4L4 = 113
    NV12_16L32S = 110
    NV12_32L32 = 98
    NV12_4L4 = 97
    NV12_64Z32 = 53
    NV12_8L128 = 111
    NV16 = 51
    NV16_10LE32 = 80
    NV21 = 24
    NV24 = 52
    NV61 = 60
    P010_10BE = 61
    P010_10LE = 62
    P012_BE = 91
    P012_LE = 92
    P016_BE = 89
    P016_LE = 90
    R210 = 41
    RBGA = 133
    RGB = 15
    RGB10A2_LE = 86
    RGB15 = 31
    RGB16 = 29
    RGB8P = 35
    RGBA = 11
    RGBA64_BE = 105
    RGBA64_LE = 104
    RGBP = 99
    RGBX = 7
    UNKNOWN = 0
    UYVP = 33
    UYVY = 5
    V210 = 21
    V216 = 22
    V308 = 28
    VUYA = 84
    VYUY = 64
    XBGR = 10
    XRGB = 9
    Y210 = 82
    Y212_BE = 93
    Y212_LE = 94
    Y216_BE = 135
    Y216_LE = 134
    Y410 = 83
    Y412_BE = 95
    Y412_LE = 96
    Y416_BE = 137
    Y416_LE = 136
    Y41B = 17
    Y42B = 18
    Y444 = 20
    Y444_10BE = 46
    Y444_10LE = 47
    Y444_12BE = 76
    Y444_12LE = 77
    Y444_16BE = 87
    Y444_16LE = 88
    YUV9 = 36
    YUY2 = 4
    YV12 = 3
    YVU9 = 37
    YVYU = 19
    @staticmethod
    def from_fourcc(fourcc: int) -> VideoFormat: ...
    @staticmethod
    def from_masks(
        depth: int,
        bpp: int,
        endianness: int,
        red_mask: int,
        green_mask: int,
        blue_mask: int,
        alpha_mask: int,
    ) -> VideoFormat: ...
    @staticmethod
    def from_string(format: str) -> VideoFormat: ...
    @staticmethod
    def get_info(format: VideoFormat) -> VideoFormatInfo: ...
    @staticmethod
    def get_palette(format: VideoFormat) -> int: ...
    @staticmethod
    def to_fourcc(format: VideoFormat) -> int: ...
    @staticmethod
    def to_string(format: VideoFormat) -> str: ...

class VideoGLTextureOrientation(GObject.GEnum):
    FLIP_Y_FLIP = 3
    FLIP_Y_NORMAL = 2
    NORMAL_Y_FLIP = 1
    NORMAL_Y_NORMAL = 0

class VideoGLTextureType(GObject.GEnum):
    LUMINANCE = 0
    LUMINANCE_ALPHA = 1
    R = 5
    RG = 6
    RGB = 3
    RGB16 = 2
    RGBA = 4

class VideoGammaMode(GObject.GEnum):
    NONE = 0
    REMAP = 1

class VideoInterlaceMode(GObject.GEnum):
    ALTERNATE = 4
    FIELDS = 3
    INTERLEAVED = 1
    MIXED = 2
    PROGRESSIVE = 0
    @staticmethod
    def from_string(mode: str) -> VideoInterlaceMode: ...
    @staticmethod
    def to_string(mode: VideoInterlaceMode) -> str: ...

class VideoMatrixMode(GObject.GEnum):
    FULL = 0
    INPUT_ONLY = 1
    NONE = 3
    OUTPUT_ONLY = 2

class VideoMultiviewFramePacking(GObject.GEnum):
    CHECKERBOARD = 8
    COLUMN_INTERLEAVED = 5
    LEFT = 1
    MONO = 0
    NONE = -1
    RIGHT = 2
    ROW_INTERLEAVED = 6
    SIDE_BY_SIDE = 3
    SIDE_BY_SIDE_QUINCUNX = 4
    TOP_BOTTOM = 7

class VideoMultiviewMode(GObject.GEnum):
    CHECKERBOARD = 8
    COLUMN_INTERLEAVED = 5
    FRAME_BY_FRAME = 32
    LEFT = 1
    MONO = 0
    MULTIVIEW_FRAME_BY_FRAME = 33
    NONE = -1
    RIGHT = 2
    ROW_INTERLEAVED = 6
    SEPARATED = 34
    SIDE_BY_SIDE = 3
    SIDE_BY_SIDE_QUINCUNX = 4
    TOP_BOTTOM = 7
    @staticmethod
    def from_caps_string(caps_mview_mode: str) -> VideoMultiviewMode: ...
    @staticmethod
    def to_caps_string(mview_mode: VideoMultiviewMode) -> str | None: ...

class VideoOrientationMethod(GObject.GEnum):
    AUTO = 8
    CUSTOM = 9
    HORIZ = 4
    IDENTITY = 0
    UL_LR = 6
    UR_LL = 7
    VERT = 5

class VideoPrimariesMode(GObject.GEnum):
    FAST = 2
    MERGE_ONLY = 1
    NONE = 0

class VideoResamplerMethod(GObject.GEnum):
    CUBIC = 2
    LANCZOS = 4
    LINEAR = 1
    NEAREST = 0
    SINC = 3

class VideoTileMode(GObject.GEnum):
    LINEAR = 131072
    UNKNOWN = 0
    ZFLIPZ_2X2 = 65536

class VideoTileType(GObject.GEnum):
    INDEXED = 0

class VideoTransferFunction(GObject.GEnum):
    ADOBERGB = 12
    ARIB_STD_B67 = 15
    BT2020_10 = 13
    BT2020_12 = 11
    BT601 = 16
    BT709 = 5
    GAMMA10 = 1
    GAMMA18 = 2
    GAMMA20 = 3
    GAMMA22 = 4
    GAMMA28 = 8
    LOG100 = 9
    LOG316 = 10
    SMPTE2084 = 14
    SMPTE240M = 6
    SRGB = 7
    UNKNOWN = 0
    @staticmethod
    def decode(func: VideoTransferFunction, val: float) -> float: ...
    @staticmethod
    def encode(func: VideoTransferFunction, val: float) -> float: ...
    @staticmethod
    def from_iso(value: int) -> VideoTransferFunction: ...
    @staticmethod
    def is_equivalent(
        from_func: VideoTransferFunction,
        from_bpp: int,
        to_func: VideoTransferFunction,
        to_bpp: int,
    ) -> bool: ...
    @staticmethod
    def to_iso(func: VideoTransferFunction) -> int: ...

class VideoVBIParserResult(GObject.GEnum):
    DONE = 0
    ERROR = 2
    OK = 1
