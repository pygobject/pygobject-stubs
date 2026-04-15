from typing import Any
from typing import type_check_only
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable

from gi import _gi
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase

T = TypeVar("T")

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
      current-level-bytes -> guint64: Current Level Bytes
        The number of currently queued bytes
      current-level-buffers -> guint64: Current Level Buffers
        The number of currently queued buffers
      current-level-time -> guint64: Current Level Time
        The amount of currently queued time
      leaky-type -> GstAppLeakyType: Leaky Type
        Whether to drop buffers once the internal queue is full
      in -> guint64: In
        Number of input buffers
      out -> guint64: Out
        Number of output buffers
      dropped -> guint64: Dropped
        Number of dropped buffers
      silent -> gboolean: silent
        Don't emit notify for dropped buffers

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
    @type_check_only
    class Props(GstBase.BaseSink.Props):
        buffer_list: bool
        caps: Gst.Caps | None
        @property
        def current_level_buffers(self) -> int: ...
        @property
        def current_level_bytes(self) -> int: ...
        @property
        def current_level_time(self) -> int: ...
        drop: bool
        @property
        def dropped(self) -> int: ...
        emit_signals: bool
        @property
        def eos(self) -> bool: ...
        leaky_type: AppLeakyType
        max_buffers: int
        max_bytes: int
        max_time: int
        @property
        def out(self) -> int: ...
        silent: bool
        wait_on_eos: bool

    @property
    def props(self) -> Props: ...
    @property
    def basesink(self) -> GstBase.BaseSink: ...
    @property
    def priv(self) -> AppSinkPrivate: ...
    def __init__(
        self,
        *,
        buffer_list: bool = ...,
        caps: Gst.Caps | None = ...,
        drop: bool = ...,
        emit_signals: bool = ...,
        leaky_type: AppLeakyType = ...,
        max_buffers: int = ...,
        max_bytes: int = ...,
        max_time: int = ...,
        silent: bool = ...,
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
        name: str | None = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_eos(self) -> None: ...
    def do_new_preroll(self) -> Gst.FlowReturn: ...
    def do_new_sample(self) -> Gst.FlowReturn: ...
    def do_pull_preroll(self) -> Gst.Sample | None: ...
    def do_pull_sample(self) -> Gst.Sample | None: ...
    def do_try_pull_object(self, timeout: int) -> Gst.MiniObject | None: ...
    def do_try_pull_preroll(self, timeout: int) -> Gst.Sample | None: ...
    def do_try_pull_sample(self, timeout: int) -> Gst.Sample | None: ...
    def get_buffer_list_support(self) -> bool: ...
    def get_caps(self) -> Gst.Caps | None: ...
    def get_current_level_buffers(self) -> int: ...
    def get_current_level_bytes(self) -> int: ...
    def get_current_level_time(self) -> int: ...
    def get_drop(self) -> bool: ...
    def get_emit_signals(self) -> bool: ...
    def get_leaky_type(self) -> AppLeakyType: ...
    def get_max_buffers(self) -> int: ...
    def get_max_bytes(self) -> int: ...
    def get_max_time(self) -> int: ...
    def get_wait_on_eos(self) -> bool: ...
    def is_eos(self) -> bool: ...
    def pull_object(self) -> Gst.MiniObject: ...
    def pull_preroll(self) -> Gst.Sample | None: ...
    def pull_sample(self) -> Gst.Sample | None: ...
    def set_buffer_list_support(self, enable_lists: bool) -> None: ...
    def set_caps(self, caps: Gst.Caps | None = None) -> None: ...
    def set_drop(self, drop: bool) -> None: ...
    def set_emit_signals(self, emit: bool) -> None: ...
    def set_leaky_type(self, leaky: AppLeakyType) -> None: ...
    def set_max_buffers(self, max: int) -> None: ...
    def set_max_bytes(self, max: int) -> None: ...
    def set_max_time(self, max: int) -> None: ...
    def set_simple_callbacks(
        self, cb: AppSinkSimpleCallbacks | None = None
    ) -> None: ...
    def set_wait_on_eos(self, wait: bool) -> None: ...
    def try_pull_object(self, timeout: int) -> Gst.MiniObject | None: ...
    def try_pull_preroll(self, timeout: int) -> Gst.Sample | None: ...
    def try_pull_sample(self, timeout: int) -> Gst.Sample | None: ...

class AppSinkClass(_gi.Struct):
    """
    :Constructors:

    ::

        AppSinkClass()
    """
    @property
    def basesink_class(self) -> GstBase.BaseSinkClass: ...
    @property
    def eos(self) -> Callable[[AppSink], None]: ...
    @property
    def new_preroll(self) -> Callable[[AppSink], Gst.FlowReturn]: ...
    @property
    def new_sample(self) -> Callable[[AppSink], Gst.FlowReturn]: ...
    @property
    def pull_preroll(self) -> Callable[[AppSink], Gst.Sample | None]: ...
    @property
    def pull_sample(self) -> Callable[[AppSink], Gst.Sample | None]: ...
    @property
    def try_pull_preroll(self) -> Callable[[AppSink, int], Gst.Sample | None]: ...
    @property
    def try_pull_sample(self) -> Callable[[AppSink, int], Gst.Sample | None]: ...
    @property
    def try_pull_object(self) -> Callable[[AppSink, int], Gst.MiniObject | None]: ...

class AppSinkPrivate(_gi.Struct): ...

class AppSinkSimpleCallbacks(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> GstApp.AppSinkSimpleCallbacks
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    @classmethod
    def new(cls) -> AppSinkSimpleCallbacks: ...
    def ref(self) -> AppSinkSimpleCallbacks: ...
    def set_eos(self, eos_cb: Callable[..., None], *user_data: Any) -> None: ...
    def set_new_event(
        self, new_event_cb: Callable[..., bool], *user_data: Any
    ) -> None: ...
    def set_new_preroll(
        self, new_preroll_cb: Callable[..., Gst.FlowReturn], *user_data: Any
    ) -> None: ...
    def set_new_sample(
        self, new_sample_cb: Callable[..., Gst.FlowReturn], *user_data: Any
    ) -> None: ...
    def set_propose_allocation(
        self, propose_allocation_cb: Callable[..., bool], *user_data: Any
    ) -> None: ...
    def unref(self) -> None: ...

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
      in -> guint64: In
        Number of input buffers
      out -> guint64: Out
        Number of output buffers
      dropped -> guint64: Dropped
        Number of dropped buffers
      silent -> gboolean: silent
        Don't emit notify for dropped buffers

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
    @type_check_only
    class Props(GstBase.BaseSrc.Props):
        block: bool
        caps: Gst.Caps | None
        @property
        def current_level_buffers(self) -> int: ...
        @property
        def current_level_bytes(self) -> int: ...
        @property
        def current_level_time(self) -> int: ...
        @property
        def dropped(self) -> int: ...
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
        @property
        def out(self) -> int: ...
        silent: bool
        size: int
        stream_type: AppStreamType

    @property
    def props(self) -> Props: ...
    @property
    def basesrc(self) -> GstBase.BaseSrc: ...
    @property
    def priv(self) -> AppSrcPrivate: ...
    def __init__(
        self,
        *,
        block: bool = ...,
        caps: Gst.Caps | None = ...,
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
        silent: bool = ...,
        size: int = ...,
        stream_type: AppStreamType = ...,
        automatic_eos: bool = ...,
        blocksize: int = ...,
        do_timestamp: bool = ...,
        num_buffers: int = ...,
        typefind: bool = ...,
        name: str | None = ...,
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
    def get_caps(self) -> Gst.Caps | None: ...
    def get_current_level_buffers(self) -> int: ...
    def get_current_level_bytes(self) -> int: ...
    def get_current_level_time(self) -> int: ...
    def get_duration(self) -> int: ...
    def get_emit_signals(self) -> bool: ...
    def get_latency(self) -> tuple[int, int]: ...
    def get_leaky_type(self) -> AppLeakyType: ...
    def get_max_buffers(self) -> int: ...
    def get_max_bytes(self) -> int: ...
    def get_max_time(self) -> int: ...
    def get_size(self) -> int: ...
    def get_stream_type(self) -> AppStreamType: ...
    def push_buffer(self, buffer: Gst.Buffer) -> Gst.FlowReturn: ...
    def push_buffer_list(self, buffer_list: Gst.BufferList) -> Gst.FlowReturn: ...
    def push_sample(self, sample: Gst.Sample) -> Gst.FlowReturn: ...
    def set_caps(self, caps: Gst.Caps | None = None) -> None: ...
    def set_duration(self, duration: int) -> None: ...
    def set_emit_signals(self, emit: bool) -> None: ...
    def set_latency(self, min: int, max: int) -> None: ...
    def set_leaky_type(self, leaky: AppLeakyType) -> None: ...
    def set_max_buffers(self, max: int) -> None: ...
    def set_max_bytes(self, max: int) -> None: ...
    def set_max_time(self, max: int) -> None: ...
    def set_simple_callbacks(self, cb: AppSrcSimpleCallbacks | None = None) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_stream_type(self, type: AppStreamType) -> None: ...

class AppSrcClass(_gi.Struct):
    """
    :Constructors:

    ::

        AppSrcClass()
    """
    @property
    def basesrc_class(self) -> GstBase.BaseSrcClass: ...
    @property
    def need_data(self) -> Callable[[AppSrc, int], None]: ...
    @property
    def enough_data(self) -> Callable[[AppSrc], None]: ...
    @property
    def seek_data(self) -> Callable[[AppSrc, int], bool]: ...
    @property
    def push_buffer(self) -> Callable[[AppSrc, Gst.Buffer], Gst.FlowReturn]: ...
    @property
    def end_of_stream(self) -> Callable[[AppSrc], Gst.FlowReturn]: ...
    @property
    def push_sample(self) -> Callable[[AppSrc, Gst.Sample], Gst.FlowReturn]: ...
    @property
    def push_buffer_list(
        self,
    ) -> Callable[[AppSrc, Gst.BufferList], Gst.FlowReturn]: ...

class AppSrcPrivate(_gi.Struct): ...

class AppSrcSimpleCallbacks(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> GstApp.AppSrcSimpleCallbacks
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    @classmethod
    def new(cls) -> AppSrcSimpleCallbacks: ...
    def ref(self) -> AppSrcSimpleCallbacks: ...
    def set_enough_data(
        self, enough_data_cb: Callable[..., None], *user_data: Any
    ) -> None: ...
    def set_need_data(
        self, need_data_cb: Callable[..., None], *user_data: Any
    ) -> None: ...
    def set_seek_data(
        self, seek_data_cb: Callable[..., bool], *user_data: Any
    ) -> None: ...
    def unref(self) -> None: ...

class AppLeakyType(GObject.GEnum):
    DOWNSTREAM = 2
    NONE = 0
    UPSTREAM = 1

class AppStreamType(GObject.GEnum):
    RANDOM_ACCESS = 2
    SEEKABLE = 1
    STREAM = 0
