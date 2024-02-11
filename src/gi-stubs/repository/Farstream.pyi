from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst

CODEC_FORMAT: str = "%d: %s %s clock:%d channels:%d params:%p"
CODEC_ID_ANY: int = -1
CODEC_ID_DISABLE: int = -2
RTP_HEADER_EXTENSION_FORMAT: str = "%d: (%s) %s"
_lock = ...  # FIXME Constant
_namespace: str = "Farstream"
_version: str = "0.2"

def candidate_list_copy(candidate_list: list[Codec]) -> list[Codec]: ...
def codec_list_are_equal(
    list1: Optional[list[Codec]] = None, list2: Optional[list[Codec]] = None
) -> bool: ...
def codec_list_copy(codec_list: list[Codec]) -> list[Codec]: ...
def codec_list_from_keyfile(filename: str) -> list[Codec]: ...
def error_quark() -> int: ...
def media_type_to_string(media_type: MediaType) -> str: ...
def parse_error(
    object: GObject.Object, message: Gst.Message
) -> Tuple[bool, Error, str]: ...
def rtp_header_extension_list_copy(
    extensions: list[RtpHeaderExtension],
) -> list[RtpHeaderExtension]: ...
def rtp_header_extension_list_from_keyfile(
    filename: str, media_type: MediaType
) -> list[RtpHeaderExtension]: ...
def utils_get_default_codec_preferences(element: Gst.Element) -> list[Codec]: ...
def utils_get_default_rtp_header_extension_preferences(
    element: Gst.Element, media_type: MediaType
) -> list[Codec]: ...
def utils_set_bitrate(element: Gst.Element, bitrate: int) -> None: ...
def value_set_candidate_list(
    value: Any, candidates: Optional[list[Candidate]] = None
) -> None: ...

class Candidate(GObject.GBoxed):
    """
    :Constructors:

    ::

        Candidate()
        new(foundation:str, component_id:int, type:Farstream.CandidateType, proto:Farstream.NetworkProtocol, ip:str=None, port:int) -> Farstream.Candidate
        new_full(foundation:str, component_id:int, ip:str=None, port:int, base_ip:str=None, base_port:int, proto:Farstream.NetworkProtocol, priority:int, type:Farstream.CandidateType, username:str=None, password:str=None, ttl:int) -> Farstream.Candidate
    """

    foundation: str = ...
    component_id: int = ...
    ip: str = ...
    port: int = ...
    base_ip: str = ...
    base_port: int = ...
    proto: NetworkProtocol = ...
    priority: int = ...
    type: CandidateType = ...
    username: str = ...
    password: str = ...
    ttl: int = ...
    def copy(self) -> Candidate: ...
    @classmethod
    def new(
        cls,
        foundation: str,
        component_id: int,
        type: CandidateType,
        proto: NetworkProtocol,
        ip: Optional[str],
        port: int,
    ) -> Candidate: ...
    @classmethod
    def new_full(
        cls,
        foundation: str,
        component_id: int,
        ip: Optional[str],
        port: int,
        base_ip: Optional[str],
        base_port: int,
        proto: NetworkProtocol,
        priority: int,
        type: CandidateType,
        username: Optional[str],
        password: Optional[str],
        ttl: int,
    ) -> Candidate: ...

class CandidateList(GObject.GBoxed):
    @staticmethod
    def copy(candidate_list: list[Codec]) -> list[Codec]: ...

class Codec(GObject.GBoxed):
    """
    :Constructors:

    ::

        Codec()
        new(id:int, encoding_name:str, media_type:Farstream.MediaType, clock_rate:int) -> Farstream.Codec
    """

    id: int = ...
    encoding_name: str = ...
    media_type: MediaType = ...
    clock_rate: int = ...
    channels: int = ...
    minimum_reporting_interval: int = ...
    optional_params: list[CodecParameter] = ...
    feedback_params: list[FeedbackParameter] = ...
    def add_feedback_parameter(
        self, type: str, subtype: str, extra_params: str
    ) -> None: ...
    def add_optional_parameter(self, name: str, value: str) -> None: ...
    def are_equal(self, codec2: Codec) -> bool: ...
    def copy(self) -> Codec: ...
    def get_feedback_parameter(
        self,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        extra_params: Optional[str] = None,
    ) -> FeedbackParameter: ...
    def get_optional_parameter(
        self, name: str, value: Optional[str] = None
    ) -> CodecParameter: ...
    @classmethod
    def new(
        cls, id: int, encoding_name: str, media_type: MediaType, clock_rate: int
    ) -> Codec: ...
    def remove_feedback_parameter(self, item: list[FeedbackParameter]) -> None: ...
    def remove_optional_parameter(self, param: CodecParameter) -> None: ...
    def to_string(self) -> str: ...

class CodecGList(GObject.GBoxed):
    @staticmethod
    def are_equal(
        list1: Optional[list[Codec]] = None, list2: Optional[list[Codec]] = None
    ) -> bool: ...
    @staticmethod
    def copy(codec_list: list[Codec]) -> list[Codec]: ...
    @staticmethod
    def from_keyfile(filename: str) -> list[Codec]: ...

class CodecParameter(GObject.GBoxed):
    """
    :Constructors:

    ::

        CodecParameter()
    """

    name: str = ...
    value: str = ...
    def copy(self) -> CodecParameter: ...
    def free(self) -> None: ...

class Conference(Gst.Bin, Gst.ChildProxy):
    """
    :Constructors:

    ::

        Conference(**properties)

    Object FsConference

    Signals from GstChildProxy:
      child-added (GObject, gchararray)
      child-removed (GObject, gchararray)

    Signals from GstBin:
      element-added (GstElement)
      element-removed (GstElement)
      deep-element-added (GstBin, GstElement)
      deep-element-removed (GstBin, GstElement)
      do-latency () -> gboolean

    Properties from GstBin:
      async-handling -> gboolean: Async Handling
        The bin will handle Asynchronous state changes
      message-forward -> gboolean: Message Forward
        Forwards all children messages

    Signals from GstChildProxy:
      child-added (GObject, gchararray)
      child-removed (GObject, gchararray)

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

    class Props:
        async_handling: bool
        message_forward: bool
        name: Optional[str]
        parent: Optional[Gst.Object]
    props: Props = ...
    parent: Gst.Bin = ...
    _padding: list[None] = ...
    def __init__(
        self,
        async_handling: bool = ...,
        message_forward: bool = ...,
        name: Optional[str] = ...,
        parent: Gst.Object = ...,
    ): ...
    def do_new_participant(self) -> Participant: ...
    def do_new_session(self, media_type: MediaType) -> Session: ...
    def new_participant(self) -> Participant: ...
    def new_session(self, media_type: MediaType) -> Session: ...

class ConferenceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConferenceClass()
    """

    parent: Gst.BinClass = ...
    new_session: Callable[[Conference, MediaType], Session] = ...
    new_participant: Callable[[Conference], Participant] = ...
    _gst_reserved: list[None] = ...

class ElementAddedNotifier(GObject.Object):
    """
    :Constructors:

    ::

        ElementAddedNotifier(**properties)
        new() -> Farstream.ElementAddedNotifier

    Object FsElementAddedNotifier

    Signals from FsElementAddedNotifier:
      element-added (GstBin, GstElement)

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: ElementAddedNotifierPrivate = ...
    def add(self, bin: Gst.Bin) -> None: ...
    @classmethod
    def new(cls) -> ElementAddedNotifier: ...
    def remove(self, bin: Gst.Bin) -> bool: ...
    def set_default_properties(self, element: Gst.Element) -> int: ...
    def set_properties_from_file(self, filename: str) -> bool: ...
    def set_properties_from_keyfile(self, keyfile: GLib.KeyFile) -> int: ...

class ElementAddedNotifierClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ElementAddedNotifierClass()
    """

    parent_class: GObject.ObjectClass = ...

class ElementAddedNotifierPrivate(GObject.GPointer): ...

class FeedbackParameter(GObject.GBoxed):
    """
    :Constructors:

    ::

        FeedbackParameter()
    """

    type: str = ...
    subtype: str = ...
    extra_params: str = ...
    def copy(self) -> FeedbackParameter: ...
    def free(self) -> None: ...

class Participant(GObject.Object):
    """
    :Constructors:

    ::

        Participant(**properties)

    Object FsParticipant

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    mutex: GLib.Mutex = ...
    priv: ParticipantPrivate = ...
    _padding: list[None] = ...

class ParticipantClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ParticipantClass()
    """

    parent_class: GObject.ObjectClass = ...
    priv: ParticipantPrivate = ...
    _padding: list[None] = ...

class ParticipantPrivate(GObject.GPointer): ...

class Plugin(GObject.TypeModule, GObject.TypePlugin):
    """
    :Constructors:

    ::

        Plugin(**properties)

    Object FsPlugin

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.TypeModule = ...
    type: Type = ...
    name: str = ...
    priv: PluginPrivate = ...
    unused: list[None] = ...
    @staticmethod
    def list_available(type_suffix: str) -> list[str]: ...
    @staticmethod
    def register_static(name: str, type_suffix: str, type: Type) -> None: ...

class PluginClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PluginClass()
    """

    parent_class: GObject.TypeModuleClass = ...
    unused: list[None] = ...

class PluginPrivate(GObject.GPointer): ...

class RtpHeaderExtension(GObject.GBoxed):
    """
    :Constructors:

    ::

        RtpHeaderExtension()
        new(id:int, direction:Farstream.StreamDirection, uri:str) -> Farstream.RtpHeaderExtension
    """

    id: int = ...
    direction: StreamDirection = ...
    uri: str = ...
    def are_equal(self, extension2: RtpHeaderExtension) -> bool: ...
    @classmethod
    def new(
        cls, id: int, direction: StreamDirection, uri: str
    ) -> RtpHeaderExtension: ...

class RtpHeaderExtensionGList(GObject.GBoxed):
    @staticmethod
    def copy(extensions: list[RtpHeaderExtension]) -> list[RtpHeaderExtension]: ...
    @staticmethod
    def from_keyfile(
        filename: str, media_type: MediaType
    ) -> list[RtpHeaderExtension]: ...

class Session(GObject.Object):
    """
    :Constructors:

    ::

        Session(**properties)

    Object FsSession

    Signals from FsSession:
      error (GObject, FsError, gchararray)

    Properties from FsSession:
      conference -> FsConference: The FsConference
        The Conference this stream refers to
      media-type -> FsMediaType: The media type of the session
        An enum that specifies the media type of the session
      id -> guint: The ID of the session
        This ID is used on pad related to this session
      sink-pad -> GstPad: A gstreamer sink pad for this session
        A pad used for sending data on this session
      codec-preferences -> FsCodecGList: List of user preferences for the codecs
        A GList of FsCodecs that allows user to set his codec options and priorities
      codecs -> FsCodecGList: List of codecs
        A GList of FsCodecs indicating the codecs for this session
      codecs-without-config -> FsCodecGList: List of codecs without the configuration data
        A GList of FsCodecs indicating the codecs for this session without any configuration data
      current-send-codec -> FsCodec: Current active send codec
        An FsCodec indicating the currently active send codec
      tos -> guint: IP Type of Service
        The IP Type of Service to set on sent packets

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        allowed_sink_caps: Gst.Caps
        allowed_src_caps: Gst.Caps
        codec_preferences: list[Codec]
        codecs: list[Codec]
        codecs_without_config: list[Codec]
        conference: Conference
        current_send_codec: Codec
        encryption_parameters: Gst.Structure
        id: int
        media_type: MediaType
        sink_pad: Gst.Pad
        tos: int
    props: Props = ...
    parent: GObject.Object = ...
    priv: SessionPrivate = ...
    _padding: list[None] = ...
    def __init__(
        self,
        conference: Conference = ...,
        id: int = ...,
        media_type: MediaType = ...,
        tos: int = ...,
    ): ...
    def codecs_need_resend(
        self,
        old_codecs: Optional[list[Codec]] = None,
        new_codecs: Optional[list[Codec]] = None,
    ) -> list[Codec]: ...
    def destroy(self) -> None: ...
    def do_codecs_need_resend(
        self,
        old_codecs: Optional[list[Codec]] = None,
        new_codecs: Optional[list[Codec]] = None,
    ) -> list[Codec]: ...
    def do_get_stream_transmitter_type(self, transmitter: str) -> Type: ...
    def do_list_transmitters(self) -> list[str]: ...
    def do_new_stream(
        self, participant: Participant, direction: StreamDirection
    ) -> Stream: ...
    def do_set_allowed_caps(
        self, sink_caps: Optional[Gst.Caps] = None, src_caps: Optional[Gst.Caps] = None
    ) -> bool: ...
    def do_set_codec_preferences(
        self, codec_preferences: Optional[list[Codec]] = None
    ) -> bool: ...
    def do_set_encryption_parameters(
        self, parameters: Optional[Gst.Structure] = None
    ) -> bool: ...
    def do_set_send_codec(self, send_codec: Codec) -> bool: ...
    def do_start_telephony_event(self, event: int, volume: int) -> bool: ...
    def do_stop_telephony_event(self) -> bool: ...
    def emit_error(self, error_no: int, error_msg: str) -> None: ...
    def get_stream_transmitter_type(self, transmitter: str) -> Type: ...
    def list_transmitters(self) -> list[str]: ...
    def new_stream(
        self, participant: Participant, direction: StreamDirection
    ) -> Stream: ...
    def parse_codecs_changed(self, message: Gst.Message) -> bool: ...
    def parse_send_codec_changed(
        self, message: Gst.Message
    ) -> Tuple[bool, Codec, list[Codec]]: ...
    def parse_telephony_event_started(
        self, message: Gst.Message
    ) -> Tuple[bool, DTMFMethod, DTMFEvent, int]: ...
    def parse_telephony_event_stopped(
        self, message: Gst.Message
    ) -> Tuple[bool, DTMFMethod]: ...
    def set_allowed_caps(
        self, sink_caps: Optional[Gst.Caps] = None, src_caps: Optional[Gst.Caps] = None
    ) -> bool: ...
    def set_codec_preferences(
        self, codec_preferences: Optional[list[Codec]] = None
    ) -> bool: ...
    def set_encryption_parameters(
        self, parameters: Optional[Gst.Structure] = None
    ) -> bool: ...
    def set_send_codec(self, send_codec: Codec) -> bool: ...
    def start_telephony_event(self, event: int, volume: int) -> bool: ...
    def stop_telephony_event(self) -> bool: ...

class SessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionClass()
    """

    parent_class: GObject.ObjectClass = ...
    new_stream: Callable[[Session, Participant, StreamDirection], Stream] = ...
    start_telephony_event: Callable[[Session, int, int], bool] = ...
    stop_telephony_event: Callable[[Session], bool] = ...
    set_send_codec: Callable[[Session, Codec], bool] = ...
    set_codec_preferences: Callable[[Session, Optional[list[Codec]]], bool] = ...
    list_transmitters: Callable[[Session], list[str]] = ...
    get_stream_transmitter_type: Callable[[Session, str], Type] = ...
    codecs_need_resend: Callable[
        [Session, Optional[list[Codec]], Optional[list[Codec]]], list[Codec]
    ] = ...
    set_allowed_caps: Callable[
        [Session, Optional[Gst.Caps], Optional[Gst.Caps]], bool
    ] = ...
    set_encryption_parameters: Callable[[Session, Optional[Gst.Structure]], bool] = ...
    _padding: list[None] = ...

class SessionPrivate(GObject.GPointer): ...

class Stream(GObject.Object):
    """
    :Constructors:

    ::

        Stream(**properties)

    Object FsStream

    Signals from FsStream:
      error (FsError, gchararray)
      src-pad-added (GstPad, FsCodec)

    Properties from FsStream:
      remote-codecs -> FsCodecGList: List of remote codecs
        A GList of FsCodecs of the remote codecs
      negotiated-codecs -> FsCodecGList: List of remote codecs
        A GList of FsCodecs of the negotiated codecs for this stream
      current-recv-codecs -> FsCodecGList: The codecs currently being received
        A GList of FsCodec representing the codecs that have been received
      direction -> FsStreamDirection: The direction of the stream
        An enum to set and get the direction of the stream
      participant -> FsParticipant: The participant of the stream
        An FsParticipant represented by the stream
      session -> FsSession: The session of the stream
        An FsSession represented by the stream
      require-encryption -> gboolean: Require Encryption
        If TRUE, only encrypted content will be accepted

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        current_recv_codecs: list[Codec]
        decryption_parameters: Gst.Structure
        direction: StreamDirection
        negotiated_codecs: list[Codec]
        participant: Participant
        remote_codecs: list[Codec]
        require_encryption: bool
        session: Session
    props: Props = ...
    parent: GObject.Object = ...
    priv: StreamPrivate = ...
    _padding: list[None] = ...
    def __init__(
        self,
        direction: StreamDirection = ...,
        participant: Participant = ...,
        require_encryption: bool = ...,
        session: Session = ...,
    ): ...
    def add_id(self, id: int) -> None: ...
    def add_remote_candidates(self, candidates: list[Candidate]) -> bool: ...
    def destroy(self) -> None: ...
    def do_add_id(self, id: int) -> None: ...
    def do_add_remote_candidates(self, candidates: list[Candidate]) -> bool: ...
    def do_force_remote_candidates(
        self, remote_candidates: list[Candidate]
    ) -> bool: ...
    def do_set_decryption_parameters(self, parameters: Gst.Structure) -> bool: ...
    def do_set_remote_codecs(self, remote_codecs: list[Codec]) -> bool: ...
    def do_set_transmitter(
        self,
        transmitter: str,
        stream_transmitter_parameters: Optional[Sequence[GObject.Parameter]] = None,
    ) -> bool: ...
    def emit_error(self, error_no: int, error_msg: str) -> None: ...
    def emit_src_pad_added(self, pad: Gst.Pad, codec: Codec) -> None: ...
    def force_remote_candidates(self, remote_candidates: list[Candidate]) -> bool: ...
    def iterate_src_pads(self) -> Gst.Iterator: ...
    def parse_component_state_changed(
        self, message: Gst.Message
    ) -> Tuple[bool, int, StreamState]: ...
    def parse_local_candidates_prepared(self, message: Gst.Message) -> bool: ...
    def parse_new_active_candidate_pair(
        self, message: Gst.Message
    ) -> Tuple[bool, Candidate, Candidate]: ...
    def parse_new_local_candidate(
        self, message: Gst.Message
    ) -> Tuple[bool, Candidate]: ...
    def parse_recv_codecs_changed(
        self, message: Gst.Message
    ) -> Tuple[bool, list[Codec]]: ...
    def set_decryption_parameters(self, parameters: Gst.Structure) -> bool: ...
    def set_remote_codecs(self, remote_codecs: list[Codec]) -> bool: ...
    def set_transmitter(
        self,
        transmitter: str,
        stream_transmitter_parameters: Optional[Sequence[GObject.Parameter]] = None,
    ) -> bool: ...
    def set_transmitter_ht(
        self,
        transmitter: str,
        stream_transmitter_parameters: Optional[dict[str, Any]] = None,
    ) -> bool: ...

class StreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamClass()
    """

    parent_class: GObject.ObjectClass = ...
    add_remote_candidates: Callable[[Stream, list[Candidate]], bool] = ...
    force_remote_candidates: Callable[[Stream, list[Candidate]], bool] = ...
    set_remote_codecs: Callable[[Stream, list[Codec]], bool] = ...
    add_id: Callable[[Stream, int], None] = ...
    set_transmitter: Callable[
        [Stream, str, Optional[Sequence[GObject.Parameter]]], bool
    ] = ...
    set_decryption_parameters: Callable[[Stream, Gst.Structure], bool] = ...
    _padding: list[None] = ...

class StreamPrivate(GObject.GPointer): ...

class StreamTransmitter(GObject.Object):
    """
    :Constructors:

    ::

        StreamTransmitter(**properties)

    Object FsStreamTransmitter

    Signals from FsStreamTransmitter:
      error (FsError, gchararray)
      new-active-candidate-pair (FsCandidate, FsCandidate)
      new-local-candidate (FsCandidate)
      local-candidates-prepared ()
      known-source-packet-received (guint, gpointer)
      state-changed (guint, FsStreamState)

    Properties from FsStreamTransmitter:
      sending -> gboolean: Whether to send from this transmitter
        If set to FALSE, the transmitter will stop sending to this person
      preferred-local-candidates -> FsCandidateList: The preferred candidates
        A GList of FsCandidates
      associate-on-source -> gboolean: Associate incoming data based on the source address
        Whether to associate incoming data stream based on the source address

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        associate_on_source: bool
        preferred_local_candidates: CandidateList
        sending: bool
    props: Props = ...
    parent: GObject.Object = ...
    priv: StreamTransmitterPrivate = ...
    _padding: list[None] = ...
    def __init__(
        self,
        associate_on_source: bool = ...,
        preferred_local_candidates: CandidateList = ...,
        sending: bool = ...,
    ): ...
    def add_remote_candidates(self, candidates: list[Candidate]) -> bool: ...
    def do_add_remote_candidates(self, candidates: list[Candidate]) -> bool: ...
    def do_force_remote_candidates(
        self, remote_candidates: list[Candidate]
    ) -> bool: ...
    def do_gather_local_candidates(self) -> bool: ...
    def do_stop(self) -> None: ...
    def emit_error(self, error_no: int, error_msg: str) -> None: ...
    def force_remote_candidates(self, remote_candidates: list[Candidate]) -> bool: ...
    def gather_local_candidates(self) -> bool: ...
    def stop(self) -> None: ...

class StreamTransmitterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        StreamTransmitterClass()
    """

    parent_class: GObject.ObjectClass = ...
    add_remote_candidates: Callable[[StreamTransmitter, list[Candidate]], bool] = ...
    force_remote_candidates: Callable[[StreamTransmitter, list[Candidate]], bool] = ...
    gather_local_candidates: Callable[[StreamTransmitter], bool] = ...
    stop: Callable[[StreamTransmitter], None] = ...
    _padding: list[None] = ...

class StreamTransmitterPrivate(GObject.GPointer): ...

class Transmitter(GObject.Object):
    """
    :Constructors:

    ::

        Transmitter(**properties)
        new(type:str, components:int, tos:int) -> Farstream.Transmitter

    Object FsTransmitter

    Signals from FsTransmitter:
      error (FsError, gchararray)

    Properties from FsTransmitter:
      gst-sink -> GstElement: The network source
        A source GstElement to be used by a FsSession
      gst-src -> GstElement: The network source
        A source GstElement to be used by a FsSession
      components -> guint: Number of componnets
        The number of components to create
      tos -> guint: IP Type of Service
        The IP Type of Service to set on sent packets
      do-timestamp -> gboolean: Do Timestamp
        Apply current stream time to buffers

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        components: int
        do_timestamp: bool
        gst_sink: Gst.Element
        gst_src: Gst.Element
        tos: int
    props: Props = ...
    parent: GObject.Object = ...
    priv: TransmitterPrivate = ...
    construction_error: GLib.Error = ...
    _padding: list[None] = ...
    def __init__(
        self, components: int = ..., do_timestamp: bool = ..., tos: int = ...
    ): ...
    def do_get_stream_transmitter_type(self) -> Type: ...
    def do_new_stream_transmitter(
        self, participant: Participant, n_parameters: int, parameters: GObject.Parameter
    ) -> StreamTransmitter: ...
    def emit_error(self, error_no: int, error_msg: str) -> None: ...
    def get_stream_transmitter_type(self) -> Type: ...
    @staticmethod
    def list_available() -> list[str]: ...
    @classmethod
    def new(cls, type: str, components: int, tos: int) -> Transmitter: ...
    def new_stream_transmitter(
        self, participant: Participant, n_parameters: int, parameters: GObject.Parameter
    ) -> StreamTransmitter: ...

class TransmitterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TransmitterClass()
    """

    parent_class: GObject.ObjectClass = ...
    new_stream_transmitter: Callable[
        [Transmitter, Participant, int, GObject.Parameter], StreamTransmitter
    ] = ...
    get_stream_transmitter_type: Callable[[Transmitter], Type] = ...
    _padding: list[None] = ...

class TransmitterPrivate(GObject.GPointer): ...

class StreamDirection(GObject.GFlags):
    BOTH = 3
    NONE = 0
    RECV = 2
    SEND = 1

class CandidateType(GObject.GEnum):
    HOST = 0
    MULTICAST = 4
    PRFLX = 2
    RELAY = 3
    SRFLX = 1

class ComponentType(GObject.GEnum):
    NONE = 0
    RTCP = 2
    RTP = 1

class DTMFEvent(GObject.GEnum):
    A = 12
    B = 13
    C = 14
    D = 15
    POUND = 11
    STAR = 10

class DTMFMethod(GObject.GEnum):
    RTP_RFC4733 = 1
    SOUND = 2

class Error(GObject.GEnum):
    ALREADY_EXISTS = 109
    CONNECTION_FAILED = 107
    CONSTRUCTION = 1
    DISPOSED = 108
    INTERNAL = 2
    INVALID_ARGUMENTS = 100
    NEGOTIATION_FAILED = 103
    NETWORK = 101
    NOT_IMPLEMENTED = 102
    NO_CODECS = 105
    NO_CODECS_LEFT = 106
    UNKNOWN_CODEC = 104
    @staticmethod
    def quark() -> int: ...

class MediaType(GObject.GEnum):
    APPLICATION = 2
    AUDIO = 0
    LAST = 2
    VIDEO = 1
    @staticmethod
    def to_string(media_type: MediaType) -> str: ...

class NetworkProtocol(GObject.GEnum):
    TCP = 1
    TCP_ACTIVE = 2
    TCP_PASSIVE = 1
    TCP_SO = 3
    UDP = 0

class StreamState(GObject.GEnum):
    CONNECTED = 4
    CONNECTING = 3
    DISCONNECTED = 1
    FAILED = 0
    GATHERING = 2
    READY = 5
