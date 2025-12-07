import typing

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase
from typing_extensions import Self

T = typing.TypeVar("T")

AUDIO_CHANNELS_RANGE: str = "(int) [ 1, max ]"
AUDIO_CONVERTER_OPT_DITHER_METHOD: str = "GstAudioConverter.dither-method"
AUDIO_CONVERTER_OPT_DITHER_THRESHOLD: str = "GstAudioConverter.dither-threshold"
AUDIO_CONVERTER_OPT_MIX_MATRIX: str = "GstAudioConverter.mix-matrix"
AUDIO_CONVERTER_OPT_NOISE_SHAPING_METHOD: str = "GstAudioConverter.noise-shaping-method"
AUDIO_CONVERTER_OPT_QUANTIZATION: str = "GstAudioConverter.quantization"
AUDIO_CONVERTER_OPT_RESAMPLER_METHOD: str = "GstAudioConverter.resampler-method"
AUDIO_DECODER_MAX_ERRORS: int = -1
AUDIO_DECODER_SINK_NAME: str = "sink"
AUDIO_DECODER_SRC_NAME: str = "src"
AUDIO_DEF_CHANNELS: int = 2
AUDIO_DEF_FORMAT: str = "S16LE"
AUDIO_DEF_RATE: int = 44100
AUDIO_ENCODER_SINK_NAME: str = "sink"
AUDIO_ENCODER_SRC_NAME: str = "src"
AUDIO_FORMATS_ALL: str = ...
AUDIO_FORMAT_LAST: int = 32
AUDIO_RATE_RANGE: str = "(int) [ 1, max ]"
AUDIO_RESAMPLER_OPT_CUBIC_B: str = "GstAudioResampler.cubic-b"
AUDIO_RESAMPLER_OPT_CUBIC_C: str = "GstAudioResampler.cubic-c"
AUDIO_RESAMPLER_OPT_CUTOFF: str = "GstAudioResampler.cutoff"
AUDIO_RESAMPLER_OPT_FILTER_INTERPOLATION: str = "GstAudioResampler.filter-interpolation"
AUDIO_RESAMPLER_OPT_FILTER_MODE: str = "GstAudioResampler.filter-mode"
AUDIO_RESAMPLER_OPT_FILTER_MODE_THRESHOLD: str = (
    "GstAudioResampler.filter-mode-threshold"
)
AUDIO_RESAMPLER_OPT_FILTER_OVERSAMPLE: str = "GstAudioResampler.filter-oversample"
AUDIO_RESAMPLER_OPT_MAX_PHASE_ERROR: str = "GstAudioResampler.max-phase-error"
AUDIO_RESAMPLER_OPT_N_TAPS: str = "GstAudioResampler.n-taps"
AUDIO_RESAMPLER_OPT_STOP_ATTENUATION: str = "GstAudioResampler.stop-attenutation"
AUDIO_RESAMPLER_OPT_TRANSITION_BANDWIDTH: str = "GstAudioResampler.transition-bandwidth"
AUDIO_RESAMPLER_QUALITY_DEFAULT: int = 4
AUDIO_RESAMPLER_QUALITY_MAX: int = 10
AUDIO_RESAMPLER_QUALITY_MIN: int = 0
DSD_FORMATS_ALL: str = "{ DSDU32BE, DSDU16BE, DSDU8, DSDU32LE, DSDU16LE }"
DSD_MEDIA_TYPE: str = "audio/x-dsd"
DSD_SILENCE_PATTERN_BYTE: int = 105
META_TAG_AUDIO_CHANNELS_STR: str = "channels"
META_TAG_AUDIO_RATE_STR: str = "rate"
META_TAG_AUDIO_STR: str = "audio"
META_TAG_DSD_PLANE_OFFSETS_STR: str = "dsdplaneoffsets"

def audio_buffer_clip(
    buffer: Gst.Buffer, segment: Gst.Segment, rate: int, bpf: int
) -> typing.Optional[Gst.Buffer]: ...
def audio_buffer_map(
    info: AudioInfo, gstbuffer: Gst.Buffer, flags: Gst.MapFlags
) -> typing.Tuple[bool, AudioBuffer]: ...
def audio_buffer_reorder_channels(
    buffer: Gst.Buffer,
    format: AudioFormat,
    from_: typing.Sequence[AudioChannelPosition],
    to: typing.Sequence[AudioChannelPosition],
) -> bool: ...
def audio_buffer_truncate(
    buffer: Gst.Buffer, bpf: int, trim: int, samples: int
) -> Gst.Buffer: ...
def audio_channel_get_fallback_mask(channels: int) -> int: ...
def audio_channel_positions_from_mask(
    channel_mask: int, position: typing.Sequence[AudioChannelPosition]
) -> bool: ...
def audio_channel_positions_to_mask(
    position: typing.Sequence[AudioChannelPosition], force_order: bool
) -> typing.Tuple[bool, int]: ...
def audio_channel_positions_to_string(
    position: typing.Sequence[AudioChannelPosition],
) -> str: ...
def audio_channel_positions_to_valid_order(
    position: typing.Sequence[AudioChannelPosition],
) -> bool: ...
def audio_check_valid_channel_positions(
    position: typing.Sequence[AudioChannelPosition], force_order: bool
) -> bool: ...
def audio_clipping_meta_api_get_type() -> typing.Type[typing.Any]: ...
def audio_clipping_meta_get_info() -> Gst.MetaInfo: ...
def audio_downmix_meta_api_get_type() -> typing.Type[typing.Any]: ...
def audio_downmix_meta_get_info() -> Gst.MetaInfo: ...
def audio_format_build_integer(
    sign: bool, endianness: int, width: int, depth: int
) -> AudioFormat: ...
def audio_format_fill_silence(
    info: AudioFormatInfo, dest: typing.Sequence[int]
) -> None: ...
def audio_format_from_string(format: str) -> AudioFormat: ...
def audio_format_get_info(format: AudioFormat) -> AudioFormatInfo: ...
def audio_format_to_string(format: AudioFormat) -> str: ...
def audio_formats_raw() -> list[AudioFormat]: ...
def audio_get_channel_reorder_map(
    from_: typing.Sequence[AudioChannelPosition],
    to: typing.Sequence[AudioChannelPosition],
    reorder_map: typing.Sequence[int],
) -> bool: ...
def audio_iec61937_frame_size(spec: AudioRingBufferSpec) -> int: ...
def audio_iec61937_payload(
    src: typing.Sequence[int],
    dst: typing.Sequence[int],
    spec: AudioRingBufferSpec,
    endianness: int,
) -> bool: ...
def audio_info_from_caps(caps: Gst.Caps) -> typing.Tuple[bool, AudioInfo]: ...
def audio_info_init() -> AudioInfo: ...
def audio_level_meta_api_get_type() -> typing.Type[typing.Any]: ...
def audio_level_meta_get_info() -> Gst.MetaInfo: ...
def audio_make_raw_caps(
    formats: typing.Optional[typing.Sequence[AudioFormat]], layout: AudioLayout
) -> Gst.Caps: ...
def audio_meta_api_get_type() -> typing.Type[typing.Any]: ...
def audio_meta_get_info() -> Gst.MetaInfo: ...
def audio_reorder_channels(
    data: typing.Sequence[int],
    format: AudioFormat,
    from_: typing.Sequence[AudioChannelPosition],
    to: typing.Sequence[AudioChannelPosition],
) -> bool: ...
def audio_reorder_channels_with_reorder_map(
    data: typing.Sequence[int], bps: int, reorder_map: typing.Sequence[int]
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
    from_position: typing.Sequence[AudioChannelPosition],
    to_position: typing.Sequence[AudioChannelPosition],
    matrix: float,
) -> AudioDownmixMeta: ...
def buffer_add_audio_level_meta(
    buffer: Gst.Buffer, level: int, voice_activity: bool
) -> typing.Optional[AudioLevelMeta]: ...
def buffer_add_audio_meta(
    buffer: Gst.Buffer,
    info: AudioInfo,
    samples: int,
    offsets: typing.Optional[int] = None,
) -> AudioMeta: ...
def buffer_add_dsd_plane_offset_meta(
    buffer: Gst.Buffer,
    num_channels: int,
    num_bytes_per_channel: int,
    offsets: typing.Optional[int] = None,
) -> DsdPlaneOffsetMeta: ...
def buffer_get_audio_downmix_meta_for_channels(
    buffer: Gst.Buffer, to_position: typing.Sequence[AudioChannelPosition]
) -> AudioDownmixMeta: ...
def buffer_get_audio_level_meta(
    buffer: Gst.Buffer,
) -> typing.Optional[AudioLevelMeta]: ...
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
def dsd_info_from_caps(caps: Gst.Caps) -> typing.Tuple[bool, DsdInfo]: ...
def dsd_info_init() -> DsdInfo: ...
def dsd_plane_offset_meta_api_get_type() -> typing.Type[typing.Any]: ...
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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    parent: GstBase.Aggregator = ...
    current_caps: Gst.Caps = ...
    priv: AudioAggregatorPrivate = ...
    def __init__(
        self,
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
        name: typing.Optional[str] = ...,
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

class AudioAggregatorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioAggregatorClass()
    """

    parent_class: GstBase.AggregatorClass = ...
    create_output_buffer: typing.Callable[[AudioAggregator, int], Gst.Buffer] = ...
    aggregate_one_buffer: typing.Callable[
        [AudioAggregator, AudioAggregatorPad, Gst.Buffer, int, Gst.Buffer, int, int],
        bool,
    ] = ...

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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    parent: AudioAggregatorPad = ...
    priv: AudioAggregatorConvertPadPrivate = ...
    def __init__(
        self,
        converter_config: Gst.Structure = ...,
        qos_messages: bool = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...

class AudioAggregatorConvertPadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioAggregatorConvertPadClass()
    """

    parent_class: AudioAggregatorPadClass = ...

class AudioAggregatorConvertPadPrivate(GObject.GPointer): ...

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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    parent: GstBase.AggregatorPad = ...
    info: AudioInfo = ...
    priv: AudioAggregatorPadPrivate = ...
    def __init__(
        self,
        qos_messages: bool = ...,
        emit_signals: bool = ...,
        direction: Gst.PadDirection = ...,
        offset: int = ...,
        template: Gst.PadTemplate = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_convert_buffer(
        self, in_info: AudioInfo, out_info: AudioInfo, buffer: Gst.Buffer
    ) -> Gst.Buffer: ...
    def do_update_conversion_info(self) -> None: ...

class AudioAggregatorPadClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioAggregatorPadClass()
    """

    parent_class: GstBase.AggregatorPadClass = ...
    convert_buffer: typing.Callable[
        [AudioAggregatorPad, AudioInfo, AudioInfo, Gst.Buffer], Gst.Buffer
    ] = ...
    update_conversion_info: typing.Callable[[AudioAggregatorPad], None] = ...

class AudioAggregatorPadPrivate(GObject.GPointer): ...
class AudioAggregatorPrivate(GObject.GPointer): ...

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
        last_sample: typing.Optional[Gst.Sample]
        max_bitrate: int
        max_lateness: int
        processing_deadline: int
        qos: bool
        render_delay: int
        stats: Gst.Structure
        sync: bool
        throttle_time: int
        ts_offset: int
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    element: GstBase.BaseSink = ...
    ringbuffer: AudioRingBuffer = ...
    buffer_time: int = ...
    latency_time: int = ...
    next_sample: int = ...
    provided_clock: Gst.Clock = ...
    eos_rendering: bool = ...
    priv: AudioBaseSinkPrivate = ...
    def __init__(
        self,
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
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def create_ringbuffer(self) -> typing.Optional[AudioRingBuffer]: ...
    def do_create_ringbuffer(self) -> typing.Optional[AudioRingBuffer]: ...
    def do_payload(self, buffer: Gst.Buffer) -> Gst.Buffer: ...
    def get_alignment_threshold(self) -> int: ...
    def get_discont_wait(self) -> int: ...
    def get_drift_tolerance(self) -> int: ...
    def get_provide_clock(self) -> bool: ...
    def get_slave_method(self) -> AudioBaseSinkSlaveMethod: ...
    def report_device_failure(self) -> None: ...
    def set_alignment_threshold(self, alignment_threshold: int) -> None: ...
    def set_custom_slaving_callback(
        self, callback: typing.Callable[..., None], *user_data: typing.Any
    ) -> None: ...
    def set_discont_wait(self, discont_wait: int) -> None: ...
    def set_drift_tolerance(self, drift_tolerance: int) -> None: ...
    def set_provide_clock(self, provide: bool) -> None: ...
    def set_slave_method(self, method: AudioBaseSinkSlaveMethod) -> None: ...

class AudioBaseSinkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioBaseSinkClass()
    """

    parent_class: GstBase.BaseSinkClass = ...
    create_ringbuffer: typing.Callable[
        [AudioBaseSink], typing.Optional[AudioRingBuffer]
    ] = ...
    payload: typing.Callable[[AudioBaseSink, Gst.Buffer], Gst.Buffer] = ...

class AudioBaseSinkPrivate(GObject.GPointer): ...

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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    element: GstBase.PushSrc = ...
    ringbuffer: AudioRingBuffer = ...
    buffer_time: int = ...
    latency_time: int = ...
    next_sample: int = ...
    clock: Gst.Clock = ...
    priv: AudioBaseSrcPrivate = ...
    def __init__(
        self,
        buffer_time: int = ...,
        latency_time: int = ...,
        provide_clock: bool = ...,
        slave_method: AudioBaseSrcSlaveMethod = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def create_ringbuffer(self) -> typing.Optional[AudioRingBuffer]: ...
    def do_create_ringbuffer(self) -> typing.Optional[AudioRingBuffer]: ...
    def get_provide_clock(self) -> bool: ...
    def get_slave_method(self) -> AudioBaseSrcSlaveMethod: ...
    def set_provide_clock(self, provide: bool) -> None: ...
    def set_slave_method(self, method: AudioBaseSrcSlaveMethod) -> None: ...

class AudioBaseSrcClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioBaseSrcClass()
    """

    parent_class: GstBase.PushSrcClass = ...
    create_ringbuffer: typing.Callable[
        [AudioBaseSrc], typing.Optional[AudioRingBuffer]
    ] = ...

class AudioBaseSrcPrivate(GObject.GPointer): ...

class AudioBuffer(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioBuffer()
    """

    info: AudioInfo = ...
    n_samples: int = ...
    n_planes: int = ...
    planes: None = ...
    buffer: Gst.Buffer = ...
    map_infos: Gst.MapInfo = ...
    priv_planes_arr: list[None] = ...
    priv_map_infos_arr: list[Gst.MapInfo] = ...
    @staticmethod
    def clip(
        buffer: Gst.Buffer, segment: Gst.Segment, rate: int, bpf: int
    ) -> typing.Optional[Gst.Buffer]: ...
    @staticmethod
    def map(
        info: AudioInfo, gstbuffer: Gst.Buffer, flags: Gst.MapFlags
    ) -> typing.Tuple[bool, AudioBuffer]: ...
    @staticmethod
    def reorder_channels(
        buffer: Gst.Buffer,
        format: AudioFormat,
        from_: typing.Sequence[AudioChannelPosition],
        to: typing.Sequence[AudioChannelPosition],
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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    pushsrc: GstBase.PushSrc = ...
    tags: Gst.TagList = ...
    priv: AudioCdSrcPrivate = ...
    def __init__(
        self,
        device: str = ...,
        mode: AudioCdSrcMode = ...,
        track: int = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def add_track(self, track: AudioCdSrcTrack) -> bool: ...
    def do_close(self) -> None: ...
    def do_open(self, device: str) -> bool: ...
    def do_read_sector(self, sector: int) -> Gst.Buffer: ...

class AudioCdSrcClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioCdSrcClass()
    """

    pushsrc_class: GstBase.PushSrcClass = ...
    open: typing.Callable[[AudioCdSrc, str], bool] = ...
    close: typing.Callable[[AudioCdSrc], None] = ...
    read_sector: typing.Callable[[AudioCdSrc, int], Gst.Buffer] = ...

class AudioCdSrcPrivate(GObject.GPointer): ...

class AudioCdSrcTrack(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioCdSrcTrack()
    """

    is_audio: bool = ...
    num: int = ...
    start: int = ...
    end: int = ...
    tags: Gst.TagList = ...

class AudioChannelMixer(GObject.GPointer):
    def free(self) -> None: ...
    def is_passthrough(self) -> bool: ...
    def samples(self, in_: None, out: None, samples: int) -> None: ...

class AudioClippingMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioClippingMeta()
    """

    meta: Gst.Meta = ...
    format: Gst.Format = ...
    start: int = ...
    end: int = ...
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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    clock: Gst.SystemClock = ...
    func: typing.Callable[..., int] = ...
    user_data: None = ...
    destroy_notify: typing.Callable[[None], None] = ...
    last_time: int = ...
    time_offset: int = ...
    def __init__(
        self,
        clock_type: Gst.ClockType = ...,
        timeout: int = ...,
        window_size: int = ...,
        window_threshold: int = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def adjust(self, time: int) -> int: ...
    def get_time(self) -> int: ...
    def invalidate(self) -> None: ...
    @classmethod
    def new(
        cls, name: str, func: typing.Callable[..., int], *user_data: typing.Any
    ) -> AudioClock: ...
    def reset(self, time: int) -> None: ...

class AudioClockClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioClockClass()
    """

    parent_class: Gst.SystemClockClass = ...

class AudioConverter(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(flags:GstAudio.AudioConverterFlags, in_info:GstAudio.AudioInfo, out_info:GstAudio.AudioInfo, config:Gst.Structure=None) -> GstAudio.AudioConverter or None
    """
    def convert(
        self, flags: AudioConverterFlags, in_: typing.Sequence[int]
    ) -> typing.Tuple[bool, bytes]: ...
    def free(self) -> None: ...
    def get_config(self) -> typing.Tuple[Gst.Structure, int, int]: ...
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
        config: typing.Optional[Gst.Structure] = None,
    ) -> typing.Optional[AudioConverter]: ...
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
        self, in_rate: int, out_rate: int, config: typing.Optional[Gst.Structure] = None
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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    element: Gst.Element = ...
    sinkpad: Gst.Pad = ...
    srcpad: Gst.Pad = ...
    stream_lock: GLib.RecMutex = ...
    input_segment: Gst.Segment = ...
    output_segment: Gst.Segment = ...
    priv: AudioDecoderPrivate = ...
    def __init__(
        self,
        max_errors: int = ...,
        min_latency: int = ...,
        plc: bool = ...,
        tolerance: int = ...,
        name: typing.Optional[str] = ...,
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
    def do_parse(
        self, adapter: GstBase.Adapter
    ) -> typing.Tuple[Gst.FlowReturn, int, int]: ...
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
    def finish_frame(
        self, buf: typing.Optional[Gst.Buffer], frames: int
    ) -> Gst.FlowReturn: ...
    def finish_subframe(
        self, buf: typing.Optional[Gst.Buffer] = None
    ) -> Gst.FlowReturn: ...
    def get_allocator(self) -> typing.Tuple[Gst.Allocator, Gst.AllocationParams]: ...
    def get_audio_info(self) -> AudioInfo: ...
    def get_delay(self) -> int: ...
    def get_drainable(self) -> bool: ...
    def get_estimate_rate(self) -> int: ...
    def get_latency(self) -> typing.Tuple[int, int]: ...
    def get_max_errors(self) -> int: ...
    def get_min_latency(self) -> int: ...
    def get_needs_format(self) -> bool: ...
    def get_parse_state(self) -> typing.Tuple[bool, bool]: ...
    def get_plc(self) -> bool: ...
    def get_plc_aware(self) -> int: ...
    def get_tolerance(self) -> int: ...
    def merge_tags(
        self, tags: typing.Optional[Gst.TagList], mode: Gst.TagMergeMode
    ) -> None: ...
    def negotiate(self) -> bool: ...
    def proxy_getcaps(
        self,
        caps: typing.Optional[Gst.Caps] = None,
        filter: typing.Optional[Gst.Caps] = None,
    ) -> Gst.Caps: ...
    def set_allocation_caps(
        self, allocation_caps: typing.Optional[Gst.Caps] = None
    ) -> None: ...
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

class AudioDecoderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioDecoderClass()
    """

    element_class: Gst.ElementClass = ...
    start: typing.Callable[[AudioDecoder], bool] = ...
    stop: typing.Callable[[AudioDecoder], bool] = ...
    set_format: typing.Callable[[AudioDecoder, Gst.Caps], bool] = ...
    parse: typing.Callable[
        [AudioDecoder, GstBase.Adapter], typing.Tuple[Gst.FlowReturn, int, int]
    ] = ...
    handle_frame: typing.Callable[[AudioDecoder, Gst.Buffer], Gst.FlowReturn] = ...
    flush: typing.Callable[[AudioDecoder, bool], None] = ...
    pre_push: typing.Callable[[AudioDecoder, Gst.Buffer], Gst.FlowReturn] = ...
    sink_event: typing.Callable[[AudioDecoder, Gst.Event], bool] = ...
    src_event: typing.Callable[[AudioDecoder, Gst.Event], bool] = ...
    open: typing.Callable[[AudioDecoder], bool] = ...
    close: typing.Callable[[AudioDecoder], bool] = ...
    negotiate: typing.Callable[[AudioDecoder], bool] = ...
    decide_allocation: typing.Callable[[AudioDecoder, Gst.Query], bool] = ...
    propose_allocation: typing.Callable[[AudioDecoder, Gst.Query], bool] = ...
    sink_query: typing.Callable[[AudioDecoder, Gst.Query], bool] = ...
    src_query: typing.Callable[[AudioDecoder, Gst.Query], bool] = ...
    getcaps: typing.Callable[[AudioDecoder, Gst.Caps], Gst.Caps] = ...
    transform_meta: typing.Callable[
        [AudioDecoder, Gst.Buffer, Gst.Meta, Gst.Buffer], bool
    ] = ...

class AudioDecoderPrivate(GObject.GPointer): ...

class AudioDownmixMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioDownmixMeta()
    """

    meta: Gst.Meta = ...
    from_position: AudioChannelPosition = ...
    to_position: AudioChannelPosition = ...
    from_channels: int = ...
    to_channels: int = ...
    matrix: float = ...
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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    element: Gst.Element = ...
    sinkpad: Gst.Pad = ...
    srcpad: Gst.Pad = ...
    stream_lock: GLib.RecMutex = ...
    input_segment: Gst.Segment = ...
    output_segment: Gst.Segment = ...
    priv: AudioEncoderPrivate = ...
    def __init__(
        self,
        hard_resync: bool = ...,
        perfect_timestamp: bool = ...,
        tolerance: int = ...,
        name: typing.Optional[str] = ...,
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
        self, buffer: typing.Optional[Gst.Buffer], samples: int
    ) -> Gst.FlowReturn: ...
    def get_allocator(self) -> typing.Tuple[Gst.Allocator, Gst.AllocationParams]: ...
    def get_audio_info(self) -> AudioInfo: ...
    def get_drainable(self) -> bool: ...
    def get_frame_max(self) -> int: ...
    def get_frame_samples_max(self) -> int: ...
    def get_frame_samples_min(self) -> int: ...
    def get_hard_min(self) -> bool: ...
    def get_hard_resync(self) -> bool: ...
    def get_latency(self) -> typing.Tuple[int, int]: ...
    def get_lookahead(self) -> int: ...
    def get_mark_granule(self) -> bool: ...
    def get_perfect_timestamp(self) -> bool: ...
    def get_tolerance(self) -> int: ...
    def merge_tags(
        self, tags: typing.Optional[Gst.TagList], mode: Gst.TagMergeMode
    ) -> None: ...
    def negotiate(self) -> bool: ...
    def proxy_getcaps(
        self,
        caps: typing.Optional[Gst.Caps] = None,
        filter: typing.Optional[Gst.Caps] = None,
    ) -> Gst.Caps: ...
    def set_allocation_caps(
        self, allocation_caps: typing.Optional[Gst.Caps] = None
    ) -> None: ...
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

class AudioEncoderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioEncoderClass()
    """

    element_class: Gst.ElementClass = ...
    start: typing.Callable[[AudioEncoder], bool] = ...
    stop: typing.Callable[[AudioEncoder], bool] = ...
    set_format: typing.Callable[[AudioEncoder, AudioInfo], bool] = ...
    handle_frame: typing.Callable[[AudioEncoder, Gst.Buffer], Gst.FlowReturn] = ...
    flush: typing.Callable[[AudioEncoder], None] = ...
    pre_push: typing.Callable[[AudioEncoder, Gst.Buffer], Gst.FlowReturn] = ...
    sink_event: typing.Callable[[AudioEncoder, Gst.Event], bool] = ...
    src_event: typing.Callable[[AudioEncoder, Gst.Event], bool] = ...
    getcaps: typing.Callable[[AudioEncoder, Gst.Caps], Gst.Caps] = ...
    open: typing.Callable[[AudioEncoder], bool] = ...
    close: typing.Callable[[AudioEncoder], bool] = ...
    negotiate: typing.Callable[[AudioEncoder], bool] = ...
    decide_allocation: typing.Callable[[AudioEncoder, Gst.Query], bool] = ...
    propose_allocation: typing.Callable[[AudioEncoder, Gst.Query], bool] = ...
    transform_meta: typing.Callable[
        [AudioEncoder, Gst.Buffer, Gst.Meta, Gst.Buffer], bool
    ] = ...
    sink_query: typing.Callable[[AudioEncoder, Gst.Query], bool] = ...
    src_query: typing.Callable[[AudioEncoder, Gst.Query], bool] = ...

class AudioEncoderPrivate(GObject.GPointer): ...

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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    basetransform: GstBase.BaseTransform = ...
    info: AudioInfo = ...
    def __init__(
        self,
        qos: bool = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def add_pad_templates(self, allowed_caps: Gst.Caps) -> None: ...
    def do_setup(self, info: AudioInfo) -> bool: ...

class AudioFilterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioFilterClass()
    """

    basetransformclass: GstBase.BaseTransformClass = ...
    setup: typing.Callable[[AudioFilter, AudioInfo], bool] = ...
    def add_pad_templates(self, allowed_caps: Gst.Caps) -> None: ...

class AudioFormatInfo(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioFormatInfo()
    """

    format: AudioFormat = ...
    name: str = ...
    description: str = ...
    flags: AudioFormatFlags = ...
    endianness: int = ...
    width: int = ...
    depth: int = ...
    silence: bytes = ...
    unpack_format: AudioFormat = ...
    unpack_func: typing.Callable[
        [
            AudioFormatInfo,
            AudioPackFlags,
            typing.Sequence[int],
            typing.Sequence[int],
            int,
        ],
        None,
    ] = ...
    pack_func: typing.Callable[
        [
            AudioFormatInfo,
            AudioPackFlags,
            typing.Sequence[int],
            typing.Sequence[int],
            int,
        ],
        None,
    ] = ...
    def fill_silence(self, dest: typing.Sequence[int]) -> None: ...

class AudioInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        AudioInfo()
        new() -> GstAudio.AudioInfo
        new_from_caps(caps:Gst.Caps) -> GstAudio.AudioInfo or None
    """

    finfo: AudioFormatInfo = ...
    flags: AudioFlags = ...
    layout: AudioLayout = ...
    rate: int = ...
    channels: int = ...
    bpf: int = ...
    position: list[AudioChannelPosition] = ...
    def convert(
        self, src_fmt: Gst.Format, src_val: int, dest_fmt: Gst.Format
    ) -> typing.Tuple[bool, int]: ...
    def copy(self) -> AudioInfo: ...
    def free(self) -> None: ...
    def from_caps(*args): ...  # FIXME: Override is missing typing annotation
    @staticmethod
    def init() -> AudioInfo: ...
    def is_equal(self, other: AudioInfo) -> bool: ...
    @classmethod
    def new(cls) -> AudioInfo: ...
    @classmethod
    def new_from_caps(cls, caps: Gst.Caps) -> typing.Optional[AudioInfo]: ...
    def set_format(
        self,
        format: AudioFormat,
        rate: int,
        channels: int,
        position: typing.Optional[typing.Sequence[AudioChannelPosition]] = None,
    ) -> None: ...
    def to_caps(self) -> Gst.Caps: ...

class AudioLevelMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioLevelMeta()
    """

    meta: Gst.Meta = ...
    level: int = ...
    voice_activity: bool = ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class AudioMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioMeta()
    """

    meta: Gst.Meta = ...
    info: AudioInfo = ...
    samples: int = ...
    offsets: int = ...
    priv_offsets_arr: list[int] = ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class AudioQuantize(GObject.GPointer):
    def free(self) -> None: ...
    def reset(self) -> None: ...
    def samples(self, in_: None, out: None, samples: int) -> None: ...

class AudioResampler(GObject.GPointer):
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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    object: Gst.Object = ...
    cond: GLib.Cond = ...
    open: bool = ...
    acquired: bool = ...
    memory: int = ...
    size: int = ...
    timestamps: int = ...
    spec: AudioRingBufferSpec = ...
    samples_per_seg: int = ...
    empty_seg: int = ...
    state: int = ...
    segdone: int = ...
    segbase: int = ...
    waiting: int = ...
    callback: typing.Callable[..., None] = ...
    cb_data: None = ...
    need_reorder: bool = ...
    channel_reorder_map: list[int] = ...
    flushing: bool = ...
    may_start: int = ...
    active: bool = ...
    cb_data_notify: typing.Callable[[None], None] = ...
    priv: AudioRingBufferPrivate = ...
    def __init__(
        self, name: typing.Optional[str] = ..., parent: Gst.Object = ...
    ) -> None: ...
    def acquire(self, spec: AudioRingBufferSpec) -> bool: ...
    def activate(self, active: bool) -> bool: ...
    def advance(self, advance: int) -> None: ...
    def clear(self, segment: int) -> None: ...
    def clear_all(self) -> None: ...
    def close_device(self) -> bool: ...
    def commit(
        self, data: typing.Sequence[int], out_samples: int
    ) -> typing.Tuple[int, int, int]: ...
    def convert(
        self, src_fmt: Gst.Format, src_val: int, dest_fmt: Gst.Format
    ) -> typing.Tuple[bool, int]: ...
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
        self, data: typing.Sequence[int], out_samples: int
    ) -> typing.Tuple[int, int, int]: ...
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
    def prepare_read(self) -> typing.Tuple[bool, int, bytes]: ...
    def read(
        self, sample: int, data: typing.Sequence[int]
    ) -> typing.Tuple[int, int]: ...
    def release(self) -> bool: ...
    def samples_done(self) -> int: ...
    def set_callback(
        self,
        cb: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_channel_positions(
        self, position: typing.Sequence[AudioChannelPosition]
    ) -> None: ...
    def set_errored(self) -> None: ...
    def set_flushing(self, flushing: bool) -> None: ...
    def set_sample(self, sample: int) -> None: ...
    def set_segdone(self, segdone: int) -> None: ...
    def set_timestamp(self, readseg: int, timestamp: int) -> None: ...
    def start(self) -> bool: ...
    def stop(self) -> bool: ...

class AudioRingBufferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioRingBufferClass()
    """

    parent_class: Gst.ObjectClass = ...
    open_device: typing.Callable[[AudioRingBuffer], bool] = ...
    acquire: typing.Callable[[AudioRingBuffer, AudioRingBufferSpec], bool] = ...
    release: typing.Callable[[AudioRingBuffer], bool] = ...
    close_device: typing.Callable[[AudioRingBuffer], bool] = ...
    start: typing.Callable[[AudioRingBuffer], bool] = ...
    pause: typing.Callable[[AudioRingBuffer], bool] = ...
    resume: typing.Callable[[AudioRingBuffer], bool] = ...
    stop: typing.Callable[[AudioRingBuffer], bool] = ...
    delay: typing.Callable[[AudioRingBuffer], int] = ...
    activate: typing.Callable[[AudioRingBuffer, bool], bool] = ...
    commit: typing.Callable[
        [AudioRingBuffer, typing.Sequence[int], int], typing.Tuple[int, int, int]
    ] = ...
    clear_all: typing.Callable[[AudioRingBuffer], None] = ...

class AudioRingBufferPrivate(GObject.GPointer): ...

class AudioRingBufferSpec(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioRingBufferSpec()
    """

    caps: Gst.Caps = ...
    type: AudioRingBufferFormatType = ...
    info: AudioInfo = ...
    latency_time: int = ...
    buffer_time: int = ...
    segsize: int = ...
    segtotal: int = ...
    seglatency: int = ...

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
        last_sample: typing.Optional[Gst.Sample]
        max_bitrate: int
        max_lateness: int
        processing_deadline: int
        qos: bool
        render_delay: int
        stats: Gst.Structure
        sync: bool
        throttle_time: int
        ts_offset: int
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    element: AudioBaseSink = ...
    thread: GLib.Thread = ...
    def __init__(
        self,
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
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_close(self) -> bool: ...
    def do_delay(self) -> int: ...
    def do_open(self) -> bool: ...
    def do_pause(self) -> None: ...
    def do_reset(self) -> None: ...
    def do_resume(self) -> None: ...
    def do_unprepare(self) -> bool: ...
    def do_write(self, data: typing.Sequence[int]) -> int: ...

class AudioSinkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioSinkClass()
    """

    parent_class: AudioBaseSinkClass = ...
    open: typing.Callable[[AudioSink], bool] = ...
    prepare: typing.Callable[[AudioSink, AudioRingBufferSpec], bool] = ...
    unprepare: typing.Callable[[AudioSink], bool] = ...
    close: typing.Callable[[AudioSink], bool] = ...
    write: typing.Callable[[AudioSink, typing.Sequence[int]], int] = ...
    delay: typing.Callable[[AudioSink], int] = ...
    reset: typing.Callable[[AudioSink], None] = ...
    pause: typing.Callable[[AudioSink], None] = ...
    resume: typing.Callable[[AudioSink], None] = ...
    stop: typing.Callable[[AudioSink], None] = ...
    extension: AudioSinkClassExtension = ...

class AudioSinkClassExtension(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioSinkClassExtension()
    """

    clear_all: typing.Callable[[AudioSink], None] = ...

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
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    element: AudioBaseSrc = ...
    thread: GLib.Thread = ...
    def __init__(
        self,
        buffer_time: int = ...,
        latency_time: int = ...,
        provide_clock: bool = ...,
        slave_method: AudioBaseSrcSlaveMethod = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_close(self) -> bool: ...
    def do_delay(self) -> int: ...
    def do_open(self) -> bool: ...
    def do_prepare(self, spec: AudioRingBufferSpec) -> bool: ...
    def do_read(self, data: typing.Sequence[int]) -> typing.Tuple[int, int]: ...
    def do_reset(self) -> None: ...
    def do_unprepare(self) -> bool: ...

class AudioSrcClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AudioSrcClass()
    """

    parent_class: AudioBaseSrcClass = ...
    open: typing.Callable[[AudioSrc], bool] = ...
    prepare: typing.Callable[[AudioSrc, AudioRingBufferSpec], bool] = ...
    unprepare: typing.Callable[[AudioSrc], bool] = ...
    close: typing.Callable[[AudioSrc], bool] = ...
    read: typing.Callable[
        [AudioSrc, typing.Sequence[int]], typing.Tuple[int, int]
    ] = ...
    delay: typing.Callable[[AudioSrc], int] = ...
    reset: typing.Callable[[AudioSrc], None] = ...

class AudioStreamAlign(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(rate:int, alignment_threshold:int, discont_wait:int) -> GstAudio.AudioStreamAlign
    """
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
    ) -> typing.Tuple[bool, int, int, int]: ...
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

    format: DsdFormat = ...
    rate: int = ...
    channels: int = ...
    layout: AudioLayout = ...
    reversed_bytes: bool = ...
    positions: list[AudioChannelPosition] = ...
    flags: AudioFlags = ...
    def copy(self) -> DsdInfo: ...
    def free(self) -> None: ...
    @staticmethod
    def from_caps(caps: Gst.Caps) -> typing.Tuple[bool, DsdInfo]: ...
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
        positions: typing.Optional[typing.Sequence[AudioChannelPosition]] = None,
    ) -> None: ...
    def to_caps(self) -> Gst.Caps: ...

class DsdPlaneOffsetMeta(GObject.GPointer):
    """
    :Constructors:

    ::

        DsdPlaneOffsetMeta()
    """

    meta: Gst.Meta = ...
    num_channels: int = ...
    num_bytes_per_channel: int = ...
    offsets: int = ...
    priv_offsets_arr: list[int] = ...
    @staticmethod
    def get_info() -> Gst.MetaInfo: ...

class StreamVolume(GObject.GInterface):
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

class StreamVolumeInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamVolumeInterface()
    """

    iface: GObject.TypeInterface = ...

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
    def fill_silence(info: AudioFormatInfo, dest: typing.Sequence[int]) -> None: ...
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

class StreamVolumeFormat(GObject.GEnum):
    CUBIC = 1
    DB = 2
    LINEAR = 0
