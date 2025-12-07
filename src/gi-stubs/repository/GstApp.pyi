import typing

from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase
from typing_extensions import Self

T = typing.TypeVar("T")

class AppSink(GstBase.BaseSink, Gst.URIHandler):
    """
    :Constructors:

    ::

        AppSink(**properties)

    Object GstAppSink

    Signals from GstAppSink:
      eos ()
      new-preroll () -> GstFlowReturn
      new-sample () -> GstFlowReturn
      propose-allocation (GstQuery) -> gboolean
      new-serialized-event () -> gboolean
      pull-preroll () -> GstSample
      pull-sample () -> GstSample
      try-pull-preroll (guint64) -> GstSample
      try-pull-sample (guint64) -> GstSample
      try-pull-object (guint64) -> GstMiniObject

    Properties from GstAppSink:
      caps -> GstCaps: Caps
        The allowed caps for the sink pad
      eos -> gboolean: EOS
        Check if the sink is EOS or not started
      emit-signals -> gboolean: Emit signals
        Emit new-preroll and new-sample signals
      max-buffers -> guint: Max Buffers
        The maximum number of buffers to queue internally (0 = unlimited)
      drop -> gboolean: Drop
        Drop old buffers when the buffer queue is filled
      wait-on-eos -> gboolean: Wait on EOS
        Wait for all buffers to be processed after receiving an EOS
      buffer-list -> gboolean: Buffer List
        Use buffer lists
      max-time -> guint64: Max time
        The maximum total duration to queue internally (in ns, 0 = unlimited)
      max-bytes -> guint64: Max bytes
        The maximum amount of bytes to queue internally (0 = unlimited)

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
        buffer_list: bool
        caps: typing.Optional[Gst.Caps]
        drop: bool
        emit_signals: bool
        eos: bool
        max_buffers: int
        max_bytes: int
        max_time: int
        wait_on_eos: bool
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
    basesink: GstBase.BaseSink = ...
    priv: AppSinkPrivate = ...
    def __init__(
        self,
        buffer_list: bool = ...,
        caps: typing.Optional[Gst.Caps] = ...,
        drop: bool = ...,
        emit_signals: bool = ...,
        max_buffers: int = ...,
        max_bytes: int = ...,
        max_time: int = ...,
        wait_on_eos: bool = ...,
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
    def do_eos(self) -> None: ...
    def do_new_preroll(self) -> Gst.FlowReturn: ...
    def do_new_sample(self) -> Gst.FlowReturn: ...
    def do_pull_preroll(self) -> typing.Optional[Gst.Sample]: ...
    def do_pull_sample(self) -> typing.Optional[Gst.Sample]: ...
    def do_try_pull_object(self, timeout: int) -> typing.Optional[Gst.MiniObject]: ...
    def do_try_pull_preroll(self, timeout: int) -> typing.Optional[Gst.Sample]: ...
    def do_try_pull_sample(self, timeout: int) -> typing.Optional[Gst.Sample]: ...
    def get_buffer_list_support(self) -> bool: ...
    def get_caps(self) -> typing.Optional[Gst.Caps]: ...
    def get_drop(self) -> bool: ...
    def get_emit_signals(self) -> bool: ...
    def get_max_buffers(self) -> int: ...
    def get_max_bytes(self) -> int: ...
    def get_max_time(self) -> int: ...
    def get_wait_on_eos(self) -> bool: ...
    def is_eos(self) -> bool: ...
    def pull_object(self) -> gi.repository.Gst.MiniObject: ...
    def pull_preroll(self) -> typing.Optional[Gst.Sample]: ...
    def pull_sample(self) -> typing.Optional[Gst.Sample]: ...
    def set_buffer_list_support(self, enable_lists: bool) -> None: ...
    def set_caps(self, caps: typing.Optional[Gst.Caps] = None) -> None: ...
    def set_drop(self, drop: bool) -> None: ...
    def set_emit_signals(self, emit: bool) -> None: ...
    def set_max_buffers(self, max: int) -> None: ...
    def set_max_bytes(self, max: int) -> None: ...
    def set_max_time(self, max: int) -> None: ...
    def set_wait_on_eos(self, wait: bool) -> None: ...
    def try_pull_object(
        self, timeout: int
    ) -> Optional[gi.repository.Gst.MiniObject]: ...
    def try_pull_preroll(self, timeout: int) -> typing.Optional[Gst.Sample]: ...
    def try_pull_sample(self, timeout: int) -> typing.Optional[Gst.Sample]: ...

class AppSinkClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AppSinkClass()
    """

    basesink_class: GstBase.BaseSinkClass = ...
    eos: typing.Callable[[AppSink], None] = ...
    new_preroll: typing.Callable[[AppSink], Gst.FlowReturn] = ...
    new_sample: typing.Callable[[AppSink], Gst.FlowReturn] = ...
    pull_preroll: typing.Callable[[AppSink], typing.Optional[Gst.Sample]] = ...
    pull_sample: typing.Callable[[AppSink], typing.Optional[Gst.Sample]] = ...
    try_pull_preroll: typing.Callable[[AppSink, int], typing.Optional[Gst.Sample]] = ...
    try_pull_sample: typing.Callable[[AppSink, int], typing.Optional[Gst.Sample]] = ...
    try_pull_object: typing.Callable[
        [AppSink, int], typing.Optional[Gst.MiniObject]
    ] = ...

class AppSinkPrivate(GObject.GPointer): ...

class AppSrc(GstBase.BaseSrc, Gst.URIHandler):
    """
    :Constructors:

    ::

        AppSrc(**properties)

    Object GstAppSrc

    Signals from GstAppSrc:
      need-data (guint)
      enough-data ()
      seek-data (guint64) -> gboolean
      push-buffer (GstBuffer) -> GstFlowReturn
      push-buffer-list (GstBufferList) -> GstFlowReturn
      push-sample (GstSample) -> GstFlowReturn
      end-of-stream () -> GstFlowReturn

    Properties from GstAppSrc:
      caps -> GstCaps: Caps
        The allowed caps for the src pad
      size -> gint64: Size
        The size of the data stream in bytes (-1 if unknown)
      stream-type -> GstAppStreamType: Stream Type
        the type of the stream
      max-bytes -> guint64: Max bytes
        The maximum number of bytes to queue internally (0 = unlimited)
      max-buffers -> guint64: Max buffers
        The maximum number of buffers to queue internally (0 = unlimited)
      max-time -> guint64: Max time
        The maximum amount of time to queue internally (0 = unlimited)
      format -> GstFormat: Format
        The format of the segment events and seek
      block -> gboolean: Block
        Block push-buffer when max-bytes are queued
      is-live -> gboolean: Is Live
        Whether to act as a live source
      min-latency -> gint64: Min Latency
        The minimum latency (-1 = default)
      max-latency -> gint64: Max Latency
        The maximum latency (-1 = unlimited)
      emit-signals -> gboolean: Emit signals
        Emit need-data, enough-data and seek-data signals
      min-percent -> guint: Min Percent
        Emit need-data when queued bytes drops below this percent of max-bytes
      current-level-bytes -> guint64: Current Level Bytes
        The number of currently queued bytes
      current-level-buffers -> guint64: Current Level Buffers
        The number of currently queued buffers
      current-level-time -> guint64: Current Level Time
        The amount of currently queued time
      duration -> guint64: Duration
        The duration of the data stream in nanoseconds (GST_CLOCK_TIME_NONE if unknown)
      handle-segment-change -> gboolean: Handle Segment Change
        Whether to detect and handle changed time format GstSegment in GstSample. User should set valid GstSegment in GstSample. Must set format property as "time" to enable this property
      leaky-type -> GstAppLeakyType: Leaky Type
        Whether to drop buffers once the internal queue is full

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
    class Props(GstBase.BaseSrc.Props):
        block: bool
        caps: typing.Optional[Gst.Caps]
        current_level_buffers: int
        current_level_bytes: int
        current_level_time: int
        duration: int
        emit_signals: bool
        format: Gst.Format
        handle_segment_change: bool
        is_live: bool
        leaky_type: AppLeakyType
        max_buffers: int
        max_bytes: int
        max_latency: int
        max_time: int
        min_latency: int
        min_percent: int
        size: int
        stream_type: AppStreamType
        automatic_eos: bool
        blocksize: int
        do_timestamp: bool
        num_buffers: int
        typefind: bool
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    basesrc: GstBase.BaseSrc = ...
    priv: AppSrcPrivate = ...
    def __init__(
        self,
        block: bool = ...,
        caps: typing.Optional[Gst.Caps] = ...,
        duration: int = ...,
        emit_signals: bool = ...,
        format: Gst.Format = ...,
        handle_segment_change: bool = ...,
        is_live: bool = ...,
        leaky_type: AppLeakyType = ...,
        max_buffers: int = ...,
        max_bytes: int = ...,
        max_latency: int = ...,
        max_time: int = ...,
        min_latency: int = ...,
        min_percent: int = ...,
        size: int = ...,
        stream_type: AppStreamType = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_end_of_stream(self) -> Gst.FlowReturn: ...
    def do_enough_data(self) -> None: ...
    def do_need_data(self, length: int) -> None: ...
    def do_push_buffer(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def do_push_buffer_list(self, buffer_list: Gst.BufferList) -> Gst.FlowReturn: ...
    def do_push_sample(self, sample: Gst.Sample) -> Gst.FlowReturn: ...
    def do_seek_data(self, offset: int) -> bool: ...
    def end_of_stream(self) -> Gst.FlowReturn: ...
    def get_caps(self) -> typing.Optional[Gst.Caps]: ...
    def get_current_level_buffers(self) -> int: ...
    def get_current_level_bytes(self) -> int: ...
    def get_current_level_time(self) -> int: ...
    def get_duration(self) -> int: ...
    def get_emit_signals(self) -> bool: ...
    def get_latency(self) -> typing.Tuple[int, int]: ...
    def get_leaky_type(self) -> AppLeakyType: ...
    def get_max_buffers(self) -> int: ...
    def get_max_bytes(self) -> int: ...
    def get_max_time(self) -> int: ...
    def get_size(self) -> int: ...
    def get_stream_type(self) -> AppStreamType: ...
    def push_buffer(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def push_buffer_list(self, buffer_list: Gst.BufferList) -> Gst.FlowReturn: ...
    def push_sample(self, sample: Gst.Sample) -> Gst.FlowReturn: ...
    def set_caps(self, caps: typing.Optional[Gst.Caps] = None) -> None: ...
    def set_duration(self, duration: int) -> None: ...
    def set_emit_signals(self, emit: bool) -> None: ...
    def set_latency(self, min: int, max: int) -> None: ...
    def set_leaky_type(self, leaky: AppLeakyType) -> None: ...
    def set_max_buffers(self, max: int) -> None: ...
    def set_max_bytes(self, max: int) -> None: ...
    def set_max_time(self, max: int) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_stream_type(self, type: AppStreamType) -> None: ...

class AppSrcClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AppSrcClass()
    """

    basesrc_class: GstBase.BaseSrcClass = ...
    need_data: typing.Callable[[AppSrc, int], None] = ...
    enough_data: typing.Callable[[AppSrc], None] = ...
    seek_data: typing.Callable[[AppSrc, int], bool] = ...
    push_buffer: typing.Callable[[AppSrc, Gst.Buffer], Gst.FlowReturn] = ...
    end_of_stream: typing.Callable[[AppSrc], Gst.FlowReturn] = ...
    push_sample: typing.Callable[[AppSrc, Gst.Sample], Gst.FlowReturn] = ...
    push_buffer_list: typing.Callable[[AppSrc, Gst.BufferList], Gst.FlowReturn] = ...

class AppSrcPrivate(GObject.GPointer): ...

class AppLeakyType(GObject.GEnum):
    DOWNSTREAM = 2
    NONE = 0
    UPSTREAM = 1

class AppStreamType(GObject.GEnum):
    RANDOM_ACCESS = 2
    SEEKABLE = 1
    STREAM = 0
