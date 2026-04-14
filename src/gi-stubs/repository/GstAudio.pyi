from typing import Any
from typing import Final
from typing import Protocol
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable
from collections.abc import Sequence
from enum import IntEnum

from gi import _gi
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase

T = TypeVar("T")

AUDIO_CHANNELS_RANGE: Final = "(int) [ 1, max ]"
AUDIO_CONVERTER_OPT_DITHER_METHOD: Final = "GstAudioConverter.dither-method"
AUDIO_CONVERTER_OPT_DITHER_THRESHOLD: Final = "GstAudioConverter.dither-threshold"
AUDIO_CONVERTER_OPT_MIX_MATRIX: Final = "GstAudioConverter.mix-matrix"
AUDIO_CONVERTER_OPT_NOISE_SHAPING_METHOD: Final = (
    "GstAudioConverter.noise-shaping-method"
)
AUDIO_CONVERTER_OPT_QUANTIZATION: Final = "GstAudioConverter.quantization"
AUDIO_CONVERTER_OPT_RESAMPLER_METHOD: Final = "GstAudioConverter.resampler-method"
AUDIO_DECODER_MAX_ERRORS: Final[int]
AUDIO_DECODER_SINK_NAME: Final = "sink"
AUDIO_DECODER_SRC_NAME: Final = "src"
AUDIO_DEF_CHANNELS: Final[int]
AUDIO_DEF_FORMAT: Final = "S16LE"
AUDIO_DEF_RATE: Final[int]
AUDIO_ENCODER_SINK_NAME: Final = "sink"
AUDIO_ENCODER_SRC_NAME: Final = "src"
AUDIO_FORMATS_ALL: Final[str]
AUDIO_FORMAT_LAST: Final[int]
AUDIO_RATE_RANGE: Final = "(int) [ 1, max ]"
AUDIO_RESAMPLER_OPT_CUBIC_B: Final = "GstAudioResampler.cubic-b"
AUDIO_RESAMPLER_OPT_CUBIC_C: Final = "GstAudioResampler.cubic-c"
AUDIO_RESAMPLER_OPT_CUTOFF: Final = "GstAudioResampler.cutoff"
AUDIO_RESAMPLER_OPT_FILTER_INTERPOLATION: Final = (
    "GstAudioResampler.filter-interpolation"
)
AUDIO_RESAMPLER_OPT_FILTER_MODE: Final = "GstAudioResampler.filter-mode"
AUDIO_RESAMPLER_OPT_FILTER_MODE_THRESHOLD: Final = (
    "GstAudioResampler.filter-mode-threshold"
)
AUDIO_RESAMPLER_OPT_FILTER_OVERSAMPLE: Final = "GstAudioResampler.filter-oversample"
AUDIO_RESAMPLER_OPT_MAX_PHASE_ERROR: Final = "GstAudioResampler.max-phase-error"
AUDIO_RESAMPLER_OPT_N_TAPS: Final = "GstAudioResampler.n-taps"
AUDIO_RESAMPLER_OPT_STOP_ATTENUATION: Final = "GstAudioResampler.stop-attenutation"
AUDIO_RESAMPLER_OPT_TRANSITION_BANDWIDTH: Final = (
    "GstAudioResampler.transition-bandwidth"
)
AUDIO_RESAMPLER_QUALITY_DEFAULT: Final[int]
AUDIO_RESAMPLER_QUALITY_MAX: Final[int]
AUDIO_RESAMPLER_QUALITY_MIN: Final[int]
DSD_FORMATS_ALL: Final = "{ DSDU32BE, DSDU16BE, DSDU8, DSDU32LE, DSDU16LE }"
DSD_MEDIA_TYPE: Final = "audio/x-dsd"
DSD_SILENCE_PATTERN_BYTE: Final[int]
META_TAG_AUDIO_CHANNELS_STR: Final = "channels"
META_TAG_AUDIO_RATE_STR: Final = "rate"
META_TAG_AUDIO_STR: Final = "audio"
META_TAG_DSD_PLANE_OFFSETS_STR: Final = "dsdplaneoffsets"

def audio_buffer_clip(
    buffer: Gst.Buffer, segment: Gst.Segment, rate: int, bpf: int
) -> Gst.Buffer | None: ...
def audio_buffer_map(
    info: AudioInfo, gstbuffer: Gst.Buffer, flags: Gst.MapFlags
) -> tuple[bool, AudioBuffer]: ...
def audio_buffer_reorder_channels(
    buffer: Gst.Buffer,
    format: AudioFormat,
    from_: Sequence[AudioChannelPosition],
    to: Sequence[AudioChannelPosition],
) -> bool: ...
def audio_buffer_truncate(
    buffer: Gst.Buffer, bpf: int, trim: int, samples: int
) -> Gst.Buffer: ...
def audio_channel_get_fallback_mask(channels: int) -> int: ...
def audio_channel_positions_from_mask(
    channel_mask: int, position: Sequence[AudioChannelPosition]
) -> bool: ...
def audio_channel_positions_to_mask(
    position: Sequence[AudioChannelPosition], force_order: bool
) -> tuple[bool, int]: ...
def audio_channel_positions_to_string(
    position: Sequence[AudioChannelPosition],
) -> str: ...
def audio_channel_positions_to_valid_order(
    position: Sequence[AudioChannelPosition],
) -> bool: ...
def audio_check_valid_channel_positions(
    position: Sequence[AudioChannelPosition], force_order: bool
) -> bool: ...
def audio_clipping_meta_api_get_type() -> type[Any]: ...
def audio_clipping_meta_get_info() -> Gst.MetaInfo: ...
def audio_downmix_meta_api_get_type() -> type[Any]: ...
def audio_downmix_meta_get_info() -> Gst.MetaInfo: ...
def audio_format_build_integer(
    sign: bool, endianness: int, width: int, depth: int
) -> AudioFormat: ...
def audio_format_fill_silence(info: AudioFormatInfo, dest: Sequence[int]) -> None: ...
def audio_format_from_string(format: str) -> AudioFormat: ...
def audio_format_get_info(format: AudioFormat) -> AudioFormatInfo: ...
def audio_format_to_string(format: AudioFormat) -> str: ...
def audio_formats_raw() -> list[AudioFormat]: ...
def audio_get_channel_reorder_map(
    from_: Sequence[AudioChannelPosition],
    to: Sequence[AudioChannelPosition],
    reorder_map: Sequence[int],
) -> bool: ...
def audio_iec61937_frame_size(spec: AudioRingBufferSpec) -> int: ...
def audio_iec61937_payload(
    src: Sequence[int], dst: Sequence[int], spec: AudioRingBufferSpec, endianness: int
) -> bool: ...
def audio_info_from_caps(caps: Gst.Caps) -> tuple[bool, AudioInfo]: ...
def audio_info_init() -> AudioInfo: ...
def audio_level_meta_api_get_type() -> type[Any]: ...
def audio_level_meta_get_info() -> Gst.MetaInfo: ...
def audio_make_raw_caps(
    formats: Sequence[AudioFormat] | None, layout: AudioLayout
) -> Gst.Caps: ...
def audio_meta_api_get_type() -> type[Any]: ...
def audio_meta_get_info() -> Gst.MetaInfo: ...
def audio_reorder_channels(
    data: Sequence[int],
    format: AudioFormat,
    from_: Sequence[AudioChannelPosition],
    to: Sequence[AudioChannelPosition],
) -> bool: ...
def audio_reorder_channels_with_reorder_map(
    data: Sequence[int], bps: int, reorder_map: Sequence[int]
) -> None: ...
def audio_resampler_new(
    method: AudioResamplerMethod,
    flags: AudioResamplerFlags,
    format: AudioFormat,
    channels: int,
    in_rate: int,
    out_rate: int,
    options: Gst.Structure,
) -> AudioResampler: ...
def audio_resampler_options_set_quality(
    method: AudioResamplerMethod,
    quality: int,
    in_rate: int,
    out_rate: int,
    options: Gst.Structure,
) -> None: ...
def buffer_add_audio_clipping_meta(
    buffer: Gst.Buffer, format: Gst.Format, start: int, end: int
) -> AudioClippingMeta: ...
def buffer_add_audio_downmix_meta(
    buffer: Gst.Buffer,
    from_position: Sequence[AudioChannelPosition],
    to_position: Sequence[AudioChannelPosition],
    matrix: float,
) -> AudioDownmixMeta: ...
def buffer_add_audio_level_meta(
    buffer: Gst.Buffer, level: int, voice_activity: bool
) -> AudioLevelMeta | None: ...
def buffer_add_audio_meta(
    buffer: Gst.Buffer, info: AudioInfo, samples: int, offsets: int | None = None
) -> AudioMeta: ...
def buffer_add_dsd_plane_offset_meta(
    buffer: Gst.Buffer,
    num_channels: int,
    num_bytes_per_channel: int,
    offsets: int | None = None,
) -> DsdPlaneOffsetMeta: ...
def buffer_get_audio_downmix_meta_for_channels(
    buffer: Gst.Buffer, to_position: Sequence[AudioChannelPosition]
) -> AudioDownmixMeta: ...
def buffer_get_audio_level_meta(buffer: Gst.Buffer) -> AudioLevelMeta | None: ...
def dsd_convert(
    input_data: int,
    output_data: int,
    input_format: DsdFormat,
    output_format: DsdFormat,
    input_layout: AudioLayout,
    output_layout: AudioLayout,
    input_plane_offsets: int,
    output_plane_offsets: int,
    num_dsd_bytes: int,
    num_channels: int,
    reverse_byte_bits: bool,
) -> None: ...
def dsd_format_from_string(str: str) -> DsdFormat: ...
def dsd_format_get_width(format: DsdFormat) -> int: ...
def dsd_format_to_string(format: DsdFormat) -> str: ...
def dsd_info_from_caps(caps: Gst.Caps) -> tuple[bool, DsdInfo]: ...
def dsd_info_init() -> DsdInfo: ...
def dsd_plane_offset_meta_api_get_type() -> type[Any]: ...
def dsd_plane_offset_meta_get_info() -> Gst.MetaInfo: ...
def stream_volume_convert_volume(
    from_: StreamVolumeFormat, to: StreamVolumeFormat, val: float
) -> float: ...

class AudioAggregator(GstBase.Aggregator):
    """
    :Constructors:

    ::

        AudioAggregator(**properties)

    Object GstAudioAggregator

    Properties from GstAudioAggregator:
      output-buffer-duration -> guint64: Output Buffer Duration
        Output block size in nanoseconds
      alignment-threshold -> guint64: Alignment Threshold
        Timestamp alignment threshold in nanoseconds
      discont-wait -> guint64: Discont Wait
        Window of time in nanoseconds to wait before creating a discontinuity
      output-buffer-duration-fraction -> GstFraction: Output buffer duration fraction
        Output block size in nanoseconds, expressed as a fraction
      ignore-inactive-pads -> gboolean: Ignore inactive pads
        Avoid timing out waiting for inactive pads
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
        alignment_threshold: int
        discont_wait: int
        force_live: bool
        ignore_inactive_pads: bool
        output_buffer_duration: int
        output_buffer_duration_fraction: Gst.Fraction
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
    def parent(self) -> GstBase.Aggregator: ...
    @property
    def current_caps(self) -> Gst.Caps: ...
    @property
    def priv(self) -> AudioAggregatorPrivate: ...
    def __init__(
        self,
        *,
        alignment_threshold: int = ...,
        discont_wait: int = ...,
        force_live: bool = ...,
        ignore_inactive_pads: bool = ...,
        output_buffer_duration: int = ...,
        output_buffer_duration_fraction: Gst.Fraction = ...,
        emit_signals: bool = ...,
        latency: int = ...,
        min_upstream_latency: int = ...,
        start_time: int = ...,
        start_time_selection: GstBase.AggregatorStartTimeSelection = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_aggregate_one_buffer(
        self,
        pad: AudioAggregatorPad,
        inbuf: Gst.Buffer,
        in_offset: int,
        outbuf: Gst.Buffer,
        out_offset: int,
        num_frames: int,
    ) -> bool: ...
    def do_create_output_buffer(self, num_frames: int) -> Gst.Buffer: ...
    def set_sink_caps(self, pad: AudioAggregatorPad, caps: Gst.Caps) -> None: ...

class AudioAggregatorClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioAggregatorClass()
    """
    @property
    def parent_class(self) -> GstBase.AggregatorClass: ...
    @property
    def create_output_buffer(self) -> Callable[[AudioAggregator, int], Gst.Buffer]: ...
    @property
    def aggregate_one_buffer(
        self,
    ) -> Callable[
        [AudioAggregator, AudioAggregatorPad, Gst.Buffer, int, Gst.Buffer, int, int],
        bool,
    ]: ...

class AudioAggregatorConvertPad(AudioAggregatorPad):
    """
    :Constructors:

    ::

        AudioAggregatorConvertPad(**properties)

    Object GstAudioAggregatorConvertPad

    Properties from GstAudioAggregatorConvertPad:
      converter-config -> GstStructure: Converter configuration
        A GstStructure describing the configuration that should be used when converting this pad's audio buffers

    Properties from GstAudioAggregatorPad:
      qos-messages -> gboolean: Quality of Service Messages
        Emit QoS messages when dropping buffers

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
    class Props(AudioAggregatorPad.Props):
        converter_config: Gst.Structure
        qos_messages: bool
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
    def parent(self) -> AudioAggregatorPad: ...
    @property
    def priv(self) -> AudioAggregatorConvertPadPrivate: ...
    def __init__(
        self,
        *,
        converter_config: Gst.Structure = ...,
        qos_messages: bool = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...

class AudioAggregatorConvertPadClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioAggregatorConvertPadClass()
    """
    @property
    def parent_class(self) -> AudioAggregatorPadClass: ...

class AudioAggregatorConvertPadPrivate(_gi.Struct): ...

class AudioAggregatorPad(GstBase.AggregatorPad):
    """
    :Constructors:

    ::

        AudioAggregatorPad(**properties)

    Object GstAudioAggregatorPad

    Properties from GstAudioAggregatorPad:
      qos-messages -> gboolean: Quality of Service Messages
        Emit QoS messages when dropping buffers

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
        qos_messages: bool
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
    def info(self) -> AudioInfo: ...
    @property
    def priv(self) -> AudioAggregatorPadPrivate: ...
    def __init__(
        self,
        *,
        qos_messages: bool = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_convert_buffer(
        self, in_info: AudioInfo, out_info: AudioInfo, buffer: Gst.Buffer
    ) -> Gst.Buffer: ...
    def do_update_conversion_info(self) -> None: ...

class AudioAggregatorPadClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioAggregatorPadClass()
    """
    @property
    def parent_class(self) -> GstBase.AggregatorPadClass: ...
    @property
    def convert_buffer(
        self,
    ) -> Callable[
        [AudioAggregatorPad, AudioInfo, AudioInfo, Gst.Buffer], Gst.Buffer
    ]: ...
    @property
    def update_conversion_info(self) -> Callable[[AudioAggregatorPad], None]: ...

class AudioAggregatorPadPrivate(_gi.Struct): ...
class AudioAggregatorPrivate(_gi.Struct): ...

class AudioBaseSink(GstBase.BaseSink):
    """
    :Constructors:

    ::

        AudioBaseSink(**properties)

    Object GstAudioBaseSink

    Properties from GstAudioBaseSink:
      buffer-time -> gint64: Buffer Time
        Size of audio buffer in microseconds, this is the minimum latency that the sink reports
      latency-time -> gint64: Latency Time
        The minimum amount of data to write in each iteration in microseconds
      provide-clock -> gboolean: Provide Clock
        Provide a clock to be used as the global pipeline clock
      slave-method -> GstAudioBaseSinkSlaveMethod: Slave Method
        Algorithm used to match the rate of the masterclock
      can-activate-pull -> gboolean: Allow Pull Scheduling
        Allow pull-based scheduling
      alignment-threshold -> guint64: Alignment Threshold
        Timestamp alignment threshold in nanoseconds
      drift-tolerance -> gint64: Drift Tolerance
        Tolerance for clock drift in microseconds
      discont-wait -> guint64: Discont Wait
        Window of time in nanoseconds to wait before creating a discontinuity

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
        alignment_threshold: int
        buffer_time: int
        can_activate_pull: bool
        discont_wait: int
        drift_tolerance: int
        latency_time: int
        provide_clock: bool
        slave_method: AudioBaseSinkSlaveMethod
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
    def ringbuffer(self) -> AudioRingBuffer: ...
    @property
    def buffer_time(self) -> int: ...
    @property
    def latency_time(self) -> int: ...
    @property
    def next_sample(self) -> int: ...
    @property
    def provided_clock(self) -> Gst.Clock: ...
    @property
    def eos_rendering(self) -> bool: ...
    @property
    def priv(self) -> AudioBaseSinkPrivate: ...
    def __init__(
        self,
        *,
        alignment_threshold: int = ...,
        buffer_time: int = ...,
        can_activate_pull: bool = ...,
        discont_wait: int = ...,
        drift_tolerance: int = ...,
        latency_time: int = ...,
        provide_clock: bool = ...,
        slave_method: AudioBaseSinkSlaveMethod = ...,
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
    def create_ringbuffer(self) -> AudioRingBuffer | None: ...
    def do_create_ringbuffer(self) -> AudioRingBuffer | None: ...
    def do_payload(self, buffer: Gst.Buffer) -> Gst.Buffer: ...
    def get_alignment_threshold(self) -> int: ...
    def get_discont_wait(self) -> int: ...
    def get_drift_tolerance(self) -> int: ...
    def get_provide_clock(self) -> bool: ...
    def get_slave_method(self) -> AudioBaseSinkSlaveMethod: ...
    def report_device_failure(self) -> None: ...
    def set_alignment_threshold(self, alignment_threshold: int) -> None: ...
    def set_custom_slaving_callback(
        self, callback: Callable[..., None], *user_data: Any
    ) -> None: ...
    def set_discont_wait(self, discont_wait: int) -> None: ...
    def set_drift_tolerance(self, drift_tolerance: int) -> None: ...
    def set_provide_clock(self, provide: bool) -> None: ...
    def set_slave_method(self, method: AudioBaseSinkSlaveMethod) -> None: ...

class AudioBaseSinkClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioBaseSinkClass()
    """
    @property
    def parent_class(self) -> GstBase.BaseSinkClass: ...
    @property
    def create_ringbuffer(
        self,
    ) -> Callable[[AudioBaseSink], AudioRingBuffer | None]: ...
    @property
    def payload(self) -> Callable[[AudioBaseSink, Gst.Buffer], Gst.Buffer]: ...

class AudioBaseSinkPrivate(_gi.Struct): ...

class AudioBaseSrc(GstBase.PushSrc):
    """
    :Constructors:

    ::

        AudioBaseSrc(**properties)

    Object GstAudioBaseSrc

    Properties from GstAudioBaseSrc:
      buffer-time -> gint64: Buffer Time
        Size of audio buffer in microseconds. This is the maximum amount of data that is buffered in the device and the maximum latency that the source reports. This value might be ignored by the element if necessary; see "actual-buffer-time"
      latency-time -> gint64: Latency Time
        The minimum amount of data to read in each iteration in microseconds. This is the minimum latency that the source reports. This value might be ignored by the element if necessary; see "actual-latency-time"
      actual-buffer-time -> gint64: Actual Buffer Time
        Actual configured size of audio buffer in microseconds
      actual-latency-time -> gint64: Actual Latency Time
        Actual configured audio latency in microseconds
      provide-clock -> gboolean: Provide Clock
        Provide a clock to be used as the global pipeline clock
      slave-method -> GstAudioBaseSrcSlaveMethod: Slave Method
        Algorithm used to match the rate of the masterclock

    Properties from GstBaseSrc:
      blocksize -> guint: Block size
        Size in bytes to read per buffer (-1 = default)
      num-buffers -> gint: num-buffers
        Number of buffers to output before sending EOS (-1 = unlimited)
      typefind -> gboolean: Typefind
        Run typefind before negotiating (deprecated, non-functional)
      do-timestamp -> gboolean: Do timestamp
        Apply current stream time to buffers
      automatic-eos -> gboolean: Automatic EOS
        Automatically EOS when the segment is done

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
    class Props(GstBase.PushSrc.Props):
        actual_buffer_time: int
        actual_latency_time: int
        buffer_time: int
        latency_time: int
        provide_clock: bool
        slave_method: AudioBaseSrcSlaveMethod
        automatic_eos: bool
        blocksize: int
        do_timestamp: bool
        num_buffers: int
        typefind: bool
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def element(self) -> GstBase.PushSrc: ...
    @property
    def ringbuffer(self) -> AudioRingBuffer: ...
    @property
    def buffer_time(self) -> int: ...
    @property
    def latency_time(self) -> int: ...
    @property
    def next_sample(self) -> int: ...
    @property
    def clock(self) -> Gst.Clock: ...
    @property
    def priv(self) -> AudioBaseSrcPrivate: ...
    def __init__(
        self,
        *,
        buffer_time: int = ...,
        latency_time: int = ...,
        provide_clock: bool = ...,
        slave_method: AudioBaseSrcSlaveMethod = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def create_ringbuffer(self) -> AudioRingBuffer | None: ...
    def do_create_ringbuffer(self) -> AudioRingBuffer | None: ...
    def get_provide_clock(self) -> bool: ...
    def get_slave_method(self) -> AudioBaseSrcSlaveMethod: ...
    def set_provide_clock(self, provide: bool) -> None: ...
    def set_slave_method(self, method: AudioBaseSrcSlaveMethod) -> None: ...

class AudioBaseSrcClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioBaseSrcClass()
    """
    @property
    def parent_class(self) -> GstBase.PushSrcClass: ...
    @property
    def create_ringbuffer(self) -> Callable[[AudioBaseSrc], AudioRingBuffer | None]: ...

class AudioBaseSrcPrivate(_gi.Struct): ...

class AudioBuffer(_gi.Struct):
    """
    :Constructors:

    ::

        AudioBuffer()
    """

    info: AudioInfo
    n_samples: int
    n_planes: int
    planes: None
    buffer: Gst.Buffer
    @property
    def map_infos(self) -> Gst.MapInfo: ...
    @property
    def priv_planes_arr(self) -> list[None]: ...
    @property
    def priv_map_infos_arr(self) -> list[Gst.MapInfo]: ...
    @staticmethod
    def clip(
        buffer: Gst.Buffer, segment: Gst.Segment, rate: int, bpf: int
    ) -> Gst.Buffer | None: ...
    @staticmethod
    def map(
        info: AudioInfo, gstbuffer: Gst.Buffer, flags: Gst.MapFlags
    ) -> tuple[bool, AudioBuffer]: ...
    @staticmethod
    def reorder_channels(
        buffer: Gst.Buffer,
        format: AudioFormat,
        from_: Sequence[AudioChannelPosition],
        to: Sequence[AudioChannelPosition],
    ) -> bool: ...
    @staticmethod
    def truncate(
        buffer: Gst.Buffer, bpf: int, trim: int, samples: int
    ) -> Gst.Buffer: ...
    def unmap(self) -> None: ...

class AudioCdSrc(GstBase.PushSrc, Gst.URIHandler):
    """
    :Constructors:

    ::

        AudioCdSrc(**properties)

    Object GstAudioCdSrc

    Properties from GstAudioCdSrc:
      mode -> GstAudioCdSrcMode: Mode
        Mode
      device -> gchararray: Device
        CD device location
      track -> guint: Track
        Track

    Properties from GstBaseSrc:
      blocksize -> guint: Block size
        Size in bytes to read per buffer (-1 = default)
      num-buffers -> gint: num-buffers
        Number of buffers to output before sending EOS (-1 = unlimited)
      typefind -> gboolean: Typefind
        Run typefind before negotiating (deprecated, non-functional)
      do-timestamp -> gboolean: Do timestamp
        Apply current stream time to buffers
      automatic-eos -> gboolean: Automatic EOS
        Automatically EOS when the segment is done

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
    class Props(GstBase.PushSrc.Props):
        device: str
        mode: AudioCdSrcMode
        track: int
        automatic_eos: bool
        blocksize: int
        do_timestamp: bool
        num_buffers: int
        typefind: bool
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def pushsrc(self) -> GstBase.PushSrc: ...
    @property
    def tags(self) -> Gst.TagList: ...
    @property
    def priv(self) -> AudioCdSrcPrivate: ...
    def __init__(
        self,
        *,
        device: str = ...,
        mode: AudioCdSrcMode = ...,
        track: int = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def add_track(self, track: AudioCdSrcTrack) -> bool: ...
    def do_close(self) -> None: ...
    def do_open(self, device: str) -> bool: ...
    def do_read_sector(self, sector: int) -> Gst.Buffer: ...

class AudioCdSrcClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioCdSrcClass()
    """
    @property
    def pushsrc_class(self) -> GstBase.PushSrcClass: ...
    @property
    def open(self) -> Callable[[AudioCdSrc, str], bool]: ...
    @property
    def close(self) -> Callable[[AudioCdSrc], None]: ...
    @property
    def read_sector(self) -> Callable[[AudioCdSrc, int], Gst.Buffer]: ...

class AudioCdSrcPrivate(_gi.Struct): ...

class AudioCdSrcTrack(_gi.Struct):
    """
    :Constructors:

    ::

        AudioCdSrcTrack()
    """

    is_audio: bool
    num: int
    start: int
    end: int
    tags: Gst.TagList

class AudioChannelMixer(_gi.Struct):
    def free(self) -> None: ...
    def is_passthrough(self) -> bool: ...
    def samples(self, in_: None, out: None, samples: int) -> None: ...

class AudioClippingMeta(_gi.Struct):
    """
    :Constructors:

    ::

        AudioClippingMeta()
    """

    meta: Gst.Meta
    format: Gst.Format
    start: int
    end: int
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class AudioClock(Gst.SystemClock):
    """
    :Constructors:

    ::

        AudioClock(**properties)
        new(name:str, func:GstAudio.AudioClockGetTimeFunc, user_data=None) -> Gst.Clock

    Object GstAudioClock

    Properties from GstSystemClock:
      clock-type -> GstClockType: Clock type
        The type of underlying clock implementation used

    Signals from GstClock:
      synced (gboolean)

    Properties from GstClock:
      window-size -> gint: Window size
        The size of the window used to calculate rate and offset
      window-threshold -> gint: Window threshold
        The threshold to start calculating rate and offset
      timeout -> guint64: Timeout
        The amount of time, in nanoseconds, to sample master and slave clocks

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
    class Props(Gst.SystemClock.Props):
        clock_type: Gst.ClockType
        timeout: int
        window_size: int
        window_threshold: int
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def clock(self) -> Gst.SystemClock: ...
    @property
    def func(self) -> Callable[..., int]: ...
    @property
    def user_data(self) -> None: ...
    @property
    def destroy_notify(self) -> Callable[[None], None]: ...
    @property
    def last_time(self) -> int: ...
    @property
    def time_offset(self) -> int: ...
    def __init__(
        self,
        *,
        clock_type: Gst.ClockType = ...,
        timeout: int = ...,
        window_size: int = ...,
        window_threshold: int = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def adjust(self, time: int) -> int: ...
    def get_time(self) -> int: ...
    def invalidate(self) -> None: ...
    @classmethod
    def new(
        cls, name: str, func: Callable[..., int], *user_data: Any
    ) -> AudioClock: ...
    def reset(self, time: int) -> None: ...

class AudioClockClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioClockClass()
    """
    @property
    def parent_class(self) -> Gst.SystemClockClass: ...

class AudioConverter(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(flags:GstAudio.AudioConverterFlags, in_info:GstAudio.AudioInfo, out_info:GstAudio.AudioInfo, config:Gst.Structure=None) -> GstAudio.AudioConverter or None
    """
    @staticmethod
    def __new__(
        cls: type[Self],
        flags: AudioConverterFlags,
        in_info: AudioInfo,
        out_info: AudioInfo,
        config: Gst.Structure | None = None,
    ) -> Self: ...
    def convert(
        self, flags: AudioConverterFlags, in_: Sequence[int]
    ) -> tuple[bool, bytes]: ...
    def free(self) -> None: ...
    def get_config(self) -> tuple[Gst.Structure, int, int]: ...
    def get_in_frames(self, out_frames: int) -> int: ...
    def get_max_latency(self) -> int: ...
    def get_out_frames(self, in_frames: int) -> int: ...
    def is_passthrough(self) -> bool: ...
    @classmethod
    def new(
        cls,
        flags: AudioConverterFlags,
        in_info: AudioInfo,
        out_info: AudioInfo,
        config: Gst.Structure | None = None,
    ) -> AudioConverter | None: ...
    def reset(self) -> None: ...
    def samples(
        self,
        flags: AudioConverterFlags,
        in_: None,
        in_frames: int,
        out: None,
        out_frames: int,
    ) -> bool: ...
    def supports_inplace(self) -> bool: ...
    def update_config(
        self, in_rate: int, out_rate: int, config: Gst.Structure | None = None
    ) -> bool: ...

class AudioDecoder(Gst.Element):
    """
    :Constructors:

    ::

        AudioDecoder(**properties)

    Object GstAudioDecoder

    Properties from GstAudioDecoder:
      min-latency -> gint64: Minimum Latency
        Aggregate output data to a minimum of latency time (ns)
      tolerance -> gint64: Tolerance
        Perfect ts while timestamp jitter/imperfection within tolerance (ns)
      plc -> gboolean: Packet Loss Concealment
        Perform packet loss concealment (if supported)
      max-errors -> gint: Max errors
        Max consecutive decoder errors before returning flow error

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
        max_errors: int
        min_latency: int
        plc: bool
        tolerance: int
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
    def priv(self) -> AudioDecoderPrivate: ...
    def __init__(
        self,
        *,
        max_errors: int = ...,
        min_latency: int = ...,
        plc: bool = ...,
        tolerance: int = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def allocate_output_buffer(self, size: int) -> Gst.Buffer: ...
    def do_close(self) -> bool: ...
    def do_decide_allocation(self, query: Gst.Query) -> bool: ...
    def do_flush(self, hard: bool) -> None: ...
    def do_getcaps(self, filter: Gst.Caps) -> Gst.Caps: ...
    def do_handle_frame(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_negotiate(self) -> bool: ...
    def do_open(self) -> bool: ...
    def do_parse(self, adapter: GstBase.Adapter) -> tuple[Gst.FlowReturn, int, int]: ...
    def do_pre_push(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_propose_allocation(self, query: Gst.Query) -> bool: ...
    def do_set_format(self, caps: Gst.Caps) -> bool: ...
    def do_sink_event(self, event: Gst.Event) -> bool: ...
    def do_sink_query(self, query: Gst.Query) -> bool: ...
    def do_src_event(self, event: Gst.Event) -> bool: ...
    def do_src_query(self, query: Gst.Query) -> bool: ...
    def do_start(self) -> bool: ...
    def do_stop(self) -> bool: ...
    def do_transform_meta(
        self, outbuf: Gst.Buffer, meta: Gst.Meta, inbuf: Gst.Buffer
    ) -> bool: ...
    def finish_frame(self, buf: Gst.Buffer | None, frames: int) -> Gst.FlowReturn: ...
    def finish_subframe(self, buf: Gst.Buffer | None = None) -> Gst.FlowReturn: ...
    def get_allocator(self) -> tuple[Gst.Allocator, Gst.AllocationParams]: ...
    def get_audio_info(self) -> AudioInfo: ...
    def get_delay(self) -> int: ...
    def get_drainable(self) -> bool: ...
    def get_estimate_rate(self) -> int: ...
    def get_latency(self) -> tuple[int, int]: ...
    def get_max_errors(self) -> int: ...
    def get_min_latency(self) -> int: ...
    def get_needs_format(self) -> bool: ...
    def get_parse_state(self) -> tuple[bool, bool]: ...
    def get_plc(self) -> bool: ...
    def get_plc_aware(self) -> int: ...
    def get_tolerance(self) -> int: ...
    def merge_tags(self, tags: Gst.TagList | None, mode: Gst.TagMergeMode) -> None: ...
    def negotiate(self) -> bool: ...
    def proxy_getcaps(
        self, caps: Gst.Caps | None = None, filter: Gst.Caps | None = None
    ) -> Gst.Caps: ...
    def set_allocation_caps(self, allocation_caps: Gst.Caps | None = None) -> None: ...
    def set_drainable(self, enabled: bool) -> None: ...
    def set_estimate_rate(self, enabled: bool) -> None: ...
    def set_latency(self, min: int, max: int) -> None: ...
    def set_max_errors(self, num: int) -> None: ...
    def set_min_latency(self, num: int) -> None: ...
    def set_needs_format(self, enabled: bool) -> None: ...
    def set_output_caps(self, caps: Gst.Caps) -> bool: ...
    def set_output_format(self, info: AudioInfo) -> bool: ...
    def set_plc(self, enabled: bool) -> None: ...
    def set_plc_aware(self, plc: bool) -> None: ...
    def set_tolerance(self, tolerance: int) -> None: ...
    def set_use_default_pad_acceptcaps(self, use: bool) -> None: ...

class AudioDecoderClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioDecoderClass()
    """
    @property
    def element_class(self) -> Gst.ElementClass: ...
    @property
    def start(self) -> Callable[[AudioDecoder], bool]: ...
    @property
    def stop(self) -> Callable[[AudioDecoder], bool]: ...
    @property
    def set_format(self) -> Callable[[AudioDecoder, Gst.Caps], bool]: ...
    @property
    def parse(
        self,
    ) -> Callable[[AudioDecoder, GstBase.Adapter], tuple[Gst.FlowReturn, int, int]]: ...
    @property
    def handle_frame(self) -> Callable[[AudioDecoder, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def flush(self) -> Callable[[AudioDecoder, bool], None]: ...
    @property
    def pre_push(self) -> Callable[[AudioDecoder, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def sink_event(self) -> Callable[[AudioDecoder, Gst.Event], bool]: ...
    @property
    def src_event(self) -> Callable[[AudioDecoder, Gst.Event], bool]: ...
    @property
    def open(self) -> Callable[[AudioDecoder], bool]: ...
    @property
    def close(self) -> Callable[[AudioDecoder], bool]: ...
    @property
    def negotiate(self) -> Callable[[AudioDecoder], bool]: ...
    @property
    def decide_allocation(self) -> Callable[[AudioDecoder, Gst.Query], bool]: ...
    @property
    def propose_allocation(self) -> Callable[[AudioDecoder, Gst.Query], bool]: ...
    @property
    def sink_query(self) -> Callable[[AudioDecoder, Gst.Query], bool]: ...
    @property
    def src_query(self) -> Callable[[AudioDecoder, Gst.Query], bool]: ...
    @property
    def getcaps(self) -> Callable[[AudioDecoder, Gst.Caps], Gst.Caps]: ...
    @property
    def transform_meta(
        self,
    ) -> Callable[[AudioDecoder, Gst.Buffer, Gst.Meta, Gst.Buffer], bool]: ...

class AudioDecoderPrivate(_gi.Struct): ...

class AudioDownmixMeta(_gi.Struct):
    """
    :Constructors:

    ::

        AudioDownmixMeta()
    """

    meta: Gst.Meta
    from_position: AudioChannelPosition
    to_position: AudioChannelPosition
    from_channels: int
    to_channels: int
    matrix: float
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class AudioEncoder(Gst.Element, Gst.Preset):
    """
    :Constructors:

    ::

        AudioEncoder(**properties)

    Object GstAudioEncoder

    Properties from GstAudioEncoder:
      perfect-timestamp -> gboolean: Perfect Timestamps
        Favour perfect timestamps over tracking upstream timestamps
      mark-granule -> gboolean: Granule Marking
        Apply granule semantics to buffer metadata (implies perfect-timestamp)
      hard-resync -> gboolean: Hard Resync
        Perform clipping and sample flushing upon discontinuity
      tolerance -> gint64: Tolerance
        Consider discontinuity if timestamp jitter/imperfection exceeds tolerance (ns)

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
        hard_resync: bool
        mark_granule: bool
        perfect_timestamp: bool
        tolerance: int
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
    def priv(self) -> AudioEncoderPrivate: ...
    def __init__(
        self,
        *,
        hard_resync: bool = ...,
        perfect_timestamp: bool = ...,
        tolerance: int = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def allocate_output_buffer(self, size: int) -> Gst.Buffer: ...
    def do_close(self) -> bool: ...
    def do_decide_allocation(self, query: Gst.Query) -> bool: ...
    def do_flush(self) -> None: ...
    def do_getcaps(self, filter: Gst.Caps) -> Gst.Caps: ...
    def do_handle_frame(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_negotiate(self) -> bool: ...
    def do_open(self) -> bool: ...
    def do_pre_push(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_propose_allocation(self, query: Gst.Query) -> bool: ...
    def do_set_format(self, info: AudioInfo) -> bool: ...
    def do_sink_event(self, event: Gst.Event) -> bool: ...
    def do_sink_query(self, query: Gst.Query) -> bool: ...
    def do_src_event(self, event: Gst.Event) -> bool: ...
    def do_src_query(self, query: Gst.Query) -> bool: ...
    def do_start(self) -> bool: ...
    def do_stop(self) -> bool: ...
    def do_transform_meta(
        self, outbuf: Gst.Buffer, meta: Gst.Meta, inbuf: Gst.Buffer
    ) -> bool: ...
    def finish_frame(
        self, buffer: Gst.Buffer | None, samples: int
    ) -> Gst.FlowReturn: ...
    def get_allocator(self) -> tuple[Gst.Allocator, Gst.AllocationParams]: ...
    def get_audio_info(self) -> AudioInfo: ...
    def get_drainable(self) -> bool: ...
    def get_frame_max(self) -> int: ...
    def get_frame_samples_max(self) -> int: ...
    def get_frame_samples_min(self) -> int: ...
    def get_hard_min(self) -> bool: ...
    def get_hard_resync(self) -> bool: ...
    def get_latency(self) -> tuple[int, int]: ...
    def get_lookahead(self) -> int: ...
    def get_mark_granule(self) -> bool: ...
    def get_perfect_timestamp(self) -> bool: ...
    def get_tolerance(self) -> int: ...
    def merge_tags(self, tags: Gst.TagList | None, mode: Gst.TagMergeMode) -> None: ...
    def negotiate(self) -> bool: ...
    def proxy_getcaps(
        self, caps: Gst.Caps | None = None, filter: Gst.Caps | None = None
    ) -> Gst.Caps: ...
    def set_allocation_caps(self, allocation_caps: Gst.Caps | None = None) -> None: ...
    def set_drainable(self, enabled: bool) -> None: ...
    def set_frame_max(self, num: int) -> None: ...
    def set_frame_samples_max(self, num: int) -> None: ...
    def set_frame_samples_min(self, num: int) -> None: ...
    def set_hard_min(self, enabled: bool) -> None: ...
    def set_hard_resync(self, enabled: bool) -> None: ...
    def set_headers(self, headers: list[Gst.Buffer]) -> None: ...
    def set_latency(self, min: int, max: int) -> None: ...
    def set_lookahead(self, num: int) -> None: ...
    def set_mark_granule(self, enabled: bool) -> None: ...
    def set_output_format(self, caps: Gst.Caps) -> bool: ...
    def set_perfect_timestamp(self, enabled: bool) -> None: ...
    def set_tolerance(self, tolerance: int) -> None: ...

class AudioEncoderClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioEncoderClass()
    """
    @property
    def element_class(self) -> Gst.ElementClass: ...
    @property
    def start(self) -> Callable[[AudioEncoder], bool]: ...
    @property
    def stop(self) -> Callable[[AudioEncoder], bool]: ...
    @property
    def set_format(self) -> Callable[[AudioEncoder, AudioInfo], bool]: ...
    @property
    def handle_frame(self) -> Callable[[AudioEncoder, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def flush(self) -> Callable[[AudioEncoder], None]: ...
    @property
    def pre_push(self) -> Callable[[AudioEncoder, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def sink_event(self) -> Callable[[AudioEncoder, Gst.Event], bool]: ...
    @property
    def src_event(self) -> Callable[[AudioEncoder, Gst.Event], bool]: ...
    @property
    def getcaps(self) -> Callable[[AudioEncoder, Gst.Caps], Gst.Caps]: ...
    @property
    def open(self) -> Callable[[AudioEncoder], bool]: ...
    @property
    def close(self) -> Callable[[AudioEncoder], bool]: ...
    @property
    def negotiate(self) -> Callable[[AudioEncoder], bool]: ...
    @property
    def decide_allocation(self) -> Callable[[AudioEncoder, Gst.Query], bool]: ...
    @property
    def propose_allocation(self) -> Callable[[AudioEncoder, Gst.Query], bool]: ...
    @property
    def transform_meta(
        self,
    ) -> Callable[[AudioEncoder, Gst.Buffer, Gst.Meta, Gst.Buffer], bool]: ...
    @property
    def sink_query(self) -> Callable[[AudioEncoder, Gst.Query], bool]: ...
    @property
    def src_query(self) -> Callable[[AudioEncoder, Gst.Query], bool]: ...

class AudioEncoderPrivate(_gi.Struct): ...

class AudioFilter(GstBase.BaseTransform):
    """
    :Constructors:

    ::

        AudioFilter(**properties)

    Object GstAudioFilter

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
    def basetransform(self) -> GstBase.BaseTransform: ...
    @property
    def info(self) -> AudioInfo: ...
    def __init__(
        self, *, qos: bool = ..., name: str | None = ..., parent: Gst.Object = ...
    ) -> None: ...
    def add_pad_templates(self, allowed_caps: Gst.Caps) -> None: ...
    def do_setup(self, info: AudioInfo) -> bool: ...

class AudioFilterClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioFilterClass()
    """
    @property
    def basetransformclass(self) -> GstBase.BaseTransformClass: ...
    @property
    def setup(self) -> Callable[[AudioFilter, AudioInfo], bool]: ...
    def add_pad_templates(self, allowed_caps: Gst.Caps) -> None: ...

class AudioFormatInfo(_gi.Struct):
    """
    :Constructors:

    ::

        AudioFormatInfo()
    """

    format: AudioFormat
    name: str
    description: str
    flags: AudioFormatFlags
    endianness: int
    width: int
    depth: int
    silence: bytes
    unpack_format: AudioFormat
    unpack_func: Callable[
        [AudioFormatInfo, AudioPackFlags, Sequence[int], Sequence[int], int], None
    ]
    pack_func: Callable[
        [AudioFormatInfo, AudioPackFlags, Sequence[int], Sequence[int], int], None
    ]
    def fill_silence(self, dest: Sequence[int]) -> None: ...

class AudioInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        AudioInfo()
        new() -> GstAudio.AudioInfo
        new_from_caps(caps:Gst.Caps) -> GstAudio.AudioInfo or None
    """

    finfo: AudioFormatInfo
    flags: AudioFlags
    layout: AudioLayout
    rate: int
    channels: int
    bpf: int
    position: list[AudioChannelPosition]
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def convert(
        self, src_fmt: Gst.Format, src_val: int, dest_fmt: Gst.Format
    ) -> tuple[bool, int]: ...
    def copy(self) -> AudioInfo: ...
    def free(self) -> None: ...
    def from_caps(*args): ...  # FIXME: Override is missing typing annotation
    @staticmethod
    def init() -> AudioInfo: ...
    def is_equal(self, other: AudioInfo) -> bool: ...
    @classmethod
    def new(cls) -> AudioInfo: ...
    @classmethod
    def new_from_caps(cls, caps: Gst.Caps) -> AudioInfo | None: ...
    def set_format(
        self,
        format: AudioFormat,
        rate: int,
        channels: int,
        position: Sequence[AudioChannelPosition] | None = None,
    ) -> None: ...
    def to_caps(self) -> Gst.Caps: ...

class AudioLevelMeta(_gi.Struct):
    """
    :Constructors:

    ::

        AudioLevelMeta()
    """

    meta: Gst.Meta
    level: int
    voice_activity: bool
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class AudioMeta(_gi.Struct):
    """
    :Constructors:

    ::

        AudioMeta()
    """

    meta: Gst.Meta
    info: AudioInfo
    samples: int
    offsets: int
    @property
    def priv_offsets_arr(self) -> list[int]: ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class AudioQuantize(_gi.Struct):
    def free(self) -> None: ...
    def reset(self) -> None: ...
    def samples(self, in_: None, out: None, samples: int) -> None: ...

class AudioResampler(_gi.Struct):
    def free(self) -> None: ...
    def get_in_frames(self, out_frames: int) -> int: ...
    def get_max_latency(self) -> int: ...
    def get_out_frames(self, in_frames: int) -> int: ...
    @staticmethod
    def new(
        method: AudioResamplerMethod,
        flags: AudioResamplerFlags,
        format: AudioFormat,
        channels: int,
        in_rate: int,
        out_rate: int,
        options: Gst.Structure,
    ) -> AudioResampler: ...
    @staticmethod
    def options_set_quality(
        method: AudioResamplerMethod,
        quality: int,
        in_rate: int,
        out_rate: int,
        options: Gst.Structure,
    ) -> None: ...
    def resample(
        self, in_: None, in_frames: int, out: None, out_frames: int
    ) -> None: ...
    def reset(self) -> None: ...
    def update(self, in_rate: int, out_rate: int, options: Gst.Structure) -> bool: ...

class AudioRingBuffer(Gst.Object):
    """
    :Constructors:

    ::

        AudioRingBuffer(**properties)

    Object GstAudioRingBuffer

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
    class Props(Gst.Object.Props):
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def object(self) -> Gst.Object: ...
    @property
    def cond(self) -> GLib.Cond: ...
    @property
    def open(self) -> bool: ...
    @property
    def acquired(self) -> bool: ...
    @property
    def memory(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def timestamps(self) -> int: ...
    @property
    def spec(self) -> AudioRingBufferSpec: ...
    @property
    def samples_per_seg(self) -> int: ...
    @property
    def empty_seg(self) -> int: ...
    @property
    def state(self) -> int: ...
    @property
    def segdone(self) -> int: ...
    @property
    def segbase(self) -> int: ...
    @property
    def waiting(self) -> int: ...
    @property
    def callback(self) -> Callable[..., None]: ...
    @property
    def cb_data(self) -> None: ...
    @property
    def need_reorder(self) -> bool: ...
    @property
    def channel_reorder_map(self) -> list[int]: ...
    @property
    def flushing(self) -> bool: ...
    @property
    def may_start(self) -> int: ...
    @property
    def active(self) -> bool: ...
    @property
    def cb_data_notify(self) -> Callable[[None], None]: ...
    @property
    def priv(self) -> AudioRingBufferPrivate: ...
    def __init__(self, *, name: str | None = ..., parent: Gst.Object = ...) -> None: ...
    def acquire(self, spec: AudioRingBufferSpec) -> bool: ...
    def activate(self, active: bool) -> bool: ...
    def advance(self, advance: int) -> None: ...
    def clear(self, segment: int) -> None: ...
    def clear_all(self) -> None: ...
    def close_device(self) -> bool: ...
    def commit(self, data: Sequence[int], out_samples: int) -> tuple[int, int, int]: ...
    def convert(
        self, src_fmt: Gst.Format, src_val: int, dest_fmt: Gst.Format
    ) -> tuple[bool, int]: ...
    @staticmethod
    def debug_spec_buff(spec: AudioRingBufferSpec) -> None: ...
    @staticmethod
    def debug_spec_caps(spec: AudioRingBufferSpec) -> None: ...
    def delay(self) -> int: ...
    def device_is_open(self) -> bool: ...
    def do_acquire(self, spec: AudioRingBufferSpec) -> bool: ...
    def do_activate(self, active: bool) -> bool: ...
    def do_clear_all(self) -> None: ...
    def do_close_device(self) -> bool: ...
    def do_commit(
        self, data: Sequence[int], out_samples: int
    ) -> tuple[int, int, int]: ...
    def do_delay(self) -> int: ...
    def do_open_device(self) -> bool: ...
    def do_pause(self) -> bool: ...
    def do_release(self) -> bool: ...
    def do_resume(self) -> bool: ...
    def do_start(self) -> bool: ...
    def do_stop(self) -> bool: ...
    def get_segbase(self) -> int: ...
    def get_segdone(self) -> int: ...
    def is_acquired(self) -> bool: ...
    def is_active(self) -> bool: ...
    def is_flushing(self) -> bool: ...
    def open_device(self) -> bool: ...
    @staticmethod
    def parse_caps(spec: AudioRingBufferSpec, caps: Gst.Caps) -> bool: ...
    def pause(self) -> bool: ...
    def prepare_read(self) -> tuple[bool, int, bytes]: ...
    def read(self, sample: int, data: Sequence[int]) -> tuple[int, int]: ...
    def release(self) -> bool: ...
    def samples_done(self) -> int: ...
    def set_callback(
        self, cb: Callable[..., None] | None = None, *user_data: Any
    ) -> None: ...
    def set_channel_positions(
        self, position: Sequence[AudioChannelPosition]
    ) -> None: ...
    def set_errored(self) -> None: ...
    def set_flushing(self, flushing: bool) -> None: ...
    def set_sample(self, sample: int) -> None: ...
    def set_segdone(self, segdone: int) -> None: ...
    def set_timestamp(self, readseg: int, timestamp: int) -> None: ...
    def start(self) -> bool: ...
    def stop(self) -> bool: ...

class AudioRingBufferClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioRingBufferClass()
    """
    @property
    def parent_class(self) -> Gst.ObjectClass: ...
    @property
    def open_device(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def acquire(self) -> Callable[[AudioRingBuffer, AudioRingBufferSpec], bool]: ...
    @property
    def release(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def close_device(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def start(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def pause(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def resume(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def stop(self) -> Callable[[AudioRingBuffer], bool]: ...
    @property
    def delay(self) -> Callable[[AudioRingBuffer], int]: ...
    @property
    def activate(self) -> Callable[[AudioRingBuffer, bool], bool]: ...
    @property
    def commit(
        self,
    ) -> Callable[[AudioRingBuffer, Sequence[int], int], tuple[int, int, int]]: ...
    @property
    def clear_all(self) -> Callable[[AudioRingBuffer], None]: ...

class AudioRingBufferPrivate(_gi.Struct): ...

class AudioRingBufferSpec(_gi.Struct):
    """
    :Constructors:

    ::

        AudioRingBufferSpec()
    """

    caps: Gst.Caps
    type: AudioRingBufferFormatType
    info: AudioInfo
    latency_time: int
    buffer_time: int
    segsize: int
    segtotal: int
    seglatency: int

class AudioSink(AudioBaseSink):
    """
    :Constructors:

    ::

        AudioSink(**properties)

    Object GstAudioSink

    Properties from GstAudioBaseSink:
      buffer-time -> gint64: Buffer Time
        Size of audio buffer in microseconds, this is the minimum latency that the sink reports
      latency-time -> gint64: Latency Time
        The minimum amount of data to write in each iteration in microseconds
      provide-clock -> gboolean: Provide Clock
        Provide a clock to be used as the global pipeline clock
      slave-method -> GstAudioBaseSinkSlaveMethod: Slave Method
        Algorithm used to match the rate of the masterclock
      can-activate-pull -> gboolean: Allow Pull Scheduling
        Allow pull-based scheduling
      alignment-threshold -> guint64: Alignment Threshold
        Timestamp alignment threshold in nanoseconds
      drift-tolerance -> gint64: Drift Tolerance
        Tolerance for clock drift in microseconds
      discont-wait -> guint64: Discont Wait
        Window of time in nanoseconds to wait before creating a discontinuity

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
    class Props(AudioBaseSink.Props):
        alignment_threshold: int
        buffer_time: int
        can_activate_pull: bool
        discont_wait: int
        drift_tolerance: int
        latency_time: int
        provide_clock: bool
        slave_method: AudioBaseSinkSlaveMethod
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
    def element(self) -> AudioBaseSink: ...
    @property
    def thread(self) -> GLib.Thread: ...
    def __init__(
        self,
        *,
        alignment_threshold: int = ...,
        buffer_time: int = ...,
        can_activate_pull: bool = ...,
        discont_wait: int = ...,
        drift_tolerance: int = ...,
        latency_time: int = ...,
        provide_clock: bool = ...,
        slave_method: AudioBaseSinkSlaveMethod = ...,
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
    def do_close(self) -> bool: ...
    def do_delay(self) -> int: ...
    def do_open(self) -> bool: ...
    def do_pause(self) -> None: ...
    def do_prepare(self, spec: AudioRingBufferSpec) -> bool: ...
    def do_reset(self) -> None: ...
    def do_resume(self) -> None: ...
    def do_stop(self) -> None: ...
    def do_unprepare(self) -> bool: ...
    def do_write(self, data: Sequence[int]) -> int: ...

class AudioSinkClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioSinkClass()
    """
    @property
    def parent_class(self) -> AudioBaseSinkClass: ...
    @property
    def open(self) -> Callable[[AudioSink], bool]: ...
    @property
    def prepare(self) -> Callable[[AudioSink, AudioRingBufferSpec], bool]: ...
    @property
    def unprepare(self) -> Callable[[AudioSink], bool]: ...
    @property
    def close(self) -> Callable[[AudioSink], bool]: ...
    @property
    def write(self) -> Callable[[AudioSink, Sequence[int]], int]: ...
    @property
    def delay(self) -> Callable[[AudioSink], int]: ...
    @property
    def reset(self) -> Callable[[AudioSink], None]: ...
    @property
    def pause(self) -> Callable[[AudioSink], None]: ...
    @property
    def resume(self) -> Callable[[AudioSink], None]: ...
    @property
    def stop(self) -> Callable[[AudioSink], None]: ...
    @property
    def extension(self) -> AudioSinkClassExtension: ...

class AudioSinkClassExtension(_gi.Struct):
    """
    :Constructors:

    ::

        AudioSinkClassExtension()
    """
    @property
    def clear_all(self) -> Callable[[AudioSink], None]: ...

class AudioSrc(AudioBaseSrc):
    """
    :Constructors:

    ::

        AudioSrc(**properties)

    Object GstAudioSrc

    Properties from GstAudioBaseSrc:
      buffer-time -> gint64: Buffer Time
        Size of audio buffer in microseconds. This is the maximum amount of data that is buffered in the device and the maximum latency that the source reports. This value might be ignored by the element if necessary; see "actual-buffer-time"
      latency-time -> gint64: Latency Time
        The minimum amount of data to read in each iteration in microseconds. This is the minimum latency that the source reports. This value might be ignored by the element if necessary; see "actual-latency-time"
      actual-buffer-time -> gint64: Actual Buffer Time
        Actual configured size of audio buffer in microseconds
      actual-latency-time -> gint64: Actual Latency Time
        Actual configured audio latency in microseconds
      provide-clock -> gboolean: Provide Clock
        Provide a clock to be used as the global pipeline clock
      slave-method -> GstAudioBaseSrcSlaveMethod: Slave Method
        Algorithm used to match the rate of the masterclock

    Properties from GstBaseSrc:
      blocksize -> guint: Block size
        Size in bytes to read per buffer (-1 = default)
      num-buffers -> gint: num-buffers
        Number of buffers to output before sending EOS (-1 = unlimited)
      typefind -> gboolean: Typefind
        Run typefind before negotiating (deprecated, non-functional)
      do-timestamp -> gboolean: Do timestamp
        Apply current stream time to buffers
      automatic-eos -> gboolean: Automatic EOS
        Automatically EOS when the segment is done

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
    class Props(AudioBaseSrc.Props):
        actual_buffer_time: int
        actual_latency_time: int
        buffer_time: int
        latency_time: int
        provide_clock: bool
        slave_method: AudioBaseSrcSlaveMethod
        automatic_eos: bool
        blocksize: int
        do_timestamp: bool
        num_buffers: int
        typefind: bool
        name: str | None
        parent: Gst.Object | None

    @property
    def props(self) -> Props: ...
    @property
    def element(self) -> AudioBaseSrc: ...
    @property
    def thread(self) -> GLib.Thread: ...
    def __init__(
        self,
        *,
        buffer_time: int = ...,
        latency_time: int = ...,
        provide_clock: bool = ...,
        slave_method: AudioBaseSrcSlaveMethod = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_close(self) -> bool: ...
    def do_delay(self) -> int: ...
    def do_open(self) -> bool: ...
    def do_prepare(self, spec: AudioRingBufferSpec) -> bool: ...
    def do_read(self, data: Sequence[int]) -> tuple[int, int]: ...
    def do_reset(self) -> None: ...
    def do_unprepare(self) -> bool: ...

class AudioSrcClass(_gi.Struct):
    """
    :Constructors:

    ::

        AudioSrcClass()
    """
    @property
    def parent_class(self) -> AudioBaseSrcClass: ...
    @property
    def open(self) -> Callable[[AudioSrc], bool]: ...
    @property
    def prepare(self) -> Callable[[AudioSrc, AudioRingBufferSpec], bool]: ...
    @property
    def unprepare(self) -> Callable[[AudioSrc], bool]: ...
    @property
    def close(self) -> Callable[[AudioSrc], bool]: ...
    @property
    def read(self) -> Callable[[AudioSrc, Sequence[int]], tuple[int, int]]: ...
    @property
    def delay(self) -> Callable[[AudioSrc], int]: ...
    @property
    def reset(self) -> Callable[[AudioSrc], None]: ...

class AudioStreamAlign(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(rate:int, alignment_threshold:int, discont_wait:int) -> GstAudio.AudioStreamAlign
    """
    @staticmethod
    def __new__(
        cls: type[Self], rate: int, alignment_threshold: int, discont_wait: int
    ) -> Self: ...
    def copy(self) -> AudioStreamAlign: ...
    def free(self) -> None: ...
    def get_alignment_threshold(self) -> int: ...
    def get_discont_wait(self) -> int: ...
    def get_rate(self) -> int: ...
    def get_samples_since_discont(self) -> int: ...
    def get_timestamp_at_discont(self) -> int: ...
    def mark_discont(self) -> None: ...
    @classmethod
    def new(
        cls, rate: int, alignment_threshold: int, discont_wait: int
    ) -> AudioStreamAlign: ...
    def process(
        self, discont: bool, timestamp: int, n_samples: int
    ) -> tuple[bool, int, int, int]: ...
    def set_alignment_threshold(self, alignment_threshold: int) -> None: ...
    def set_discont_wait(self, discont_wait: int) -> None: ...
    def set_rate(self, rate: int) -> None: ...

class DsdInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DsdInfo()
        new() -> GstAudio.DsdInfo
        new_from_caps(caps:Gst.Caps) -> GstAudio.DsdInfo
    """

    format: DsdFormat
    rate: int
    channels: int
    layout: AudioLayout
    reversed_bytes: bool
    positions: list[AudioChannelPosition]
    flags: AudioFlags
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def copy(self) -> DsdInfo: ...
    def free(self) -> None: ...
    @staticmethod
    def from_caps(caps: Gst.Caps) -> tuple[bool, DsdInfo]: ...
    @staticmethod
    def init() -> DsdInfo: ...
    def is_equal(self, other: DsdInfo) -> bool: ...
    @classmethod
    def new(cls) -> DsdInfo: ...
    @classmethod
    def new_from_caps(cls, caps: Gst.Caps) -> DsdInfo: ...
    def set_format(
        self,
        format: DsdFormat,
        rate: int,
        channels: int,
        positions: Sequence[AudioChannelPosition] | None = None,
    ) -> None: ...
    def to_caps(self) -> Gst.Caps: ...

class DsdPlaneOffsetMeta(_gi.Struct):
    """
    :Constructors:

    ::

        DsdPlaneOffsetMeta()
    """

    meta: Gst.Meta
    num_channels: int
    num_bytes_per_channel: int
    offsets: int
    @property
    def priv_offsets_arr(self) -> list[int]: ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class StreamVolume(GObject.GInterface, Protocol):
    """
    Interface GstStreamVolume

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def convert_volume(
        from_: StreamVolumeFormat, to: StreamVolumeFormat, val: float
    ) -> float: ...
    def get_mute(self) -> bool: ...
    def get_volume(self, format: StreamVolumeFormat) -> float: ...
    def set_mute(self, mute: bool) -> None: ...
    def set_volume(self, format: StreamVolumeFormat, val: float) -> None: ...

class StreamVolumeInterface(_gi.Struct):
    """
    :Constructors:

    ::

        StreamVolumeInterface()
    """
    @property
    def iface(self) -> GObject.TypeInterface: ...

class AudioChannelMixerFlags(GObject.GFlags):
    NONE = 0
    NON_INTERLEAVED_IN = 1
    NON_INTERLEAVED_OUT = 2
    UNPOSITIONED_IN = 4
    UNPOSITIONED_OUT = 8

class AudioConverterFlags(GObject.GFlags):
    IN_WRITABLE = 1
    NONE = 0
    VARIABLE_RATE = 2

class AudioFlags(GObject.GFlags):
    NONE = 0
    UNPOSITIONED = 1

class AudioFormatFlags(GObject.GFlags):
    COMPLEX = 16
    FLOAT = 2
    INTEGER = 1
    SIGNED = 4
    UNPACK = 32

class AudioPackFlags(GObject.GFlags):
    NONE = 0
    TRUNCATE_RANGE = 1

class AudioQuantizeFlags(GObject.GFlags):
    NONE = 0
    NON_INTERLEAVED = 1

class AudioResamplerFlags(GObject.GFlags):
    NONE = 0
    NON_INTERLEAVED_IN = 1
    NON_INTERLEAVED_OUT = 2
    VARIABLE_RATE = 4

class AudioBaseSinkDiscontReason(GObject.GEnum):
    ALIGNMENT = 4
    DEVICE_FAILURE = 5
    FLUSH = 2
    NEW_CAPS = 1
    NO_DISCONT = 0
    SYNC_LATENCY = 3

class AudioBaseSinkSlaveMethod(GObject.GEnum):
    CUSTOM = 3
    NONE = 2
    RESAMPLE = 0
    SKEW = 1

class AudioBaseSrcSlaveMethod(GObject.GEnum):
    NONE = 3
    RESAMPLE = 0
    RE_TIMESTAMP = 1
    SKEW = 2

class AudioCdSrcMode(GObject.GEnum):
    CONTINUOUS = 1
    NORMAL = 0

class AudioChannelPosition(GObject.GEnum):
    BOTTOM_FRONT_CENTER = 21
    BOTTOM_FRONT_LEFT = 22
    BOTTOM_FRONT_RIGHT = 23
    FRONT_CENTER = 2
    FRONT_LEFT = 0
    FRONT_LEFT_OF_CENTER = 6
    FRONT_RIGHT = 1
    FRONT_RIGHT_OF_CENTER = 7
    INVALID = -1
    LFE1 = 3
    LFE2 = 9
    MONO = -2
    NONE = -3
    REAR_CENTER = 8
    REAR_LEFT = 4
    REAR_RIGHT = 5
    SIDE_LEFT = 10
    SIDE_RIGHT = 11
    SURROUND_LEFT = 26
    SURROUND_RIGHT = 27
    TOP_CENTER = 15
    TOP_FRONT_CENTER = 14
    TOP_FRONT_LEFT = 12
    TOP_FRONT_RIGHT = 13
    TOP_REAR_CENTER = 20
    TOP_REAR_LEFT = 16
    TOP_REAR_RIGHT = 17
    TOP_SIDE_LEFT = 18
    TOP_SIDE_RIGHT = 19
    TOP_SURROUND_LEFT = 28
    TOP_SURROUND_RIGHT = 29
    WIDE_LEFT = 24
    WIDE_RIGHT = 25

class AudioDitherMethod(GObject.GEnum):
    NONE = 0
    RPDF = 1
    TPDF = 2
    TPDF_HF = 3

class AudioFormat(GObject.GEnum):
    ENCODED = 1
    F32 = 28
    F32BE = 29
    F32LE = 28
    F64 = 30
    F64BE = 31
    F64LE = 30
    S16 = 4
    S16BE = 5
    S16LE = 4
    S18 = 24
    S18BE = 25
    S18LE = 24
    S20 = 20
    S20BE = 21
    S20LE = 20
    S24 = 16
    S24BE = 17
    S24LE = 16
    S24_32 = 8
    S24_32BE = 9
    S24_32LE = 8
    S32 = 12
    S32BE = 13
    S32LE = 12
    S8 = 2
    U16 = 6
    U16BE = 7
    U16LE = 6
    U18 = 26
    U18BE = 27
    U18LE = 26
    U20 = 22
    U20BE = 23
    U20LE = 22
    U24 = 18
    U24BE = 19
    U24LE = 18
    U24_32 = 10
    U24_32BE = 11
    U24_32LE = 10
    U32 = 14
    U32BE = 15
    U32LE = 14
    U8 = 3
    UNKNOWN = 0
    @staticmethod
    def build_integer(
        sign: bool, endianness: int, width: int, depth: int
    ) -> AudioFormat: ...
    @staticmethod
    def fill_silence(info: AudioFormatInfo, dest: Sequence[int]) -> None: ...
    @staticmethod
    def from_string(format: str) -> AudioFormat: ...
    @staticmethod
    def get_info(format: AudioFormat) -> AudioFormatInfo: ...
    @staticmethod
    def to_string(format: AudioFormat) -> str: ...

class AudioLayout(GObject.GEnum):
    INTERLEAVED = 0
    NON_INTERLEAVED = 1

class AudioNoiseShapingMethod(GObject.GEnum):
    ERROR_FEEDBACK = 1
    HIGH = 4
    MEDIUM = 3
    NONE = 0
    SIMPLE = 2

class AudioResamplerFilterInterpolation(GObject.GEnum):
    CUBIC = 2
    LINEAR = 1
    NONE = 0

class AudioResamplerFilterMode(GObject.GEnum):
    AUTO = 2
    FULL = 1
    INTERPOLATED = 0

class AudioResamplerMethod(GObject.GEnum):
    BLACKMAN_NUTTALL = 3
    CUBIC = 2
    KAISER = 4
    LINEAR = 1
    NEAREST = 0

class AudioRingBufferFormatType(GObject.GEnum):
    AC3 = 7
    A_LAW = 2
    DSD = 15
    DTS = 9
    EAC3 = 8
    FLAC = 14
    GSM = 5
    IEC958 = 6
    IMA_ADPCM = 3
    MPEG = 4
    MPEG2_AAC = 10
    MPEG2_AAC_RAW = 12
    MPEG4_AAC = 11
    MPEG4_AAC_RAW = 13
    MU_LAW = 1
    RAW = 0

class AudioRingBufferState(GObject.GEnum):
    ERROR = 3
    PAUSED = 1
    STARTED = 2
    STOPPED = 0

class DsdFormat(GObject.GEnum):
    DSD_FORMAT_U16 = 2
    DSD_FORMAT_U16BE = 3
    DSD_FORMAT_U16LE = 2
    DSD_FORMAT_U32 = 4
    DSD_FORMAT_U32BE = 5
    DSD_FORMAT_U32LE = 4
    DSD_FORMAT_U8 = 1
    DSD_FORMAT_UNKNOWN = 0
    NUM_DSD_FORMATS = 6
    @staticmethod
    def from_string(str: str) -> DsdFormat: ...
    @staticmethod
    def get_width(format: DsdFormat) -> int: ...
    @staticmethod
    def to_string(format: DsdFormat) -> str: ...

class StreamVolumeFormat(IntEnum):
    CUBIC = 1
    DB = 2
    LINEAR = 0
