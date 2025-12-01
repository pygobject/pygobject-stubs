import typing

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstSdp
from typing_extensions import Self

T = typing.TypeVar("T")

def webrtc_error_quark() -> int: ...
def webrtc_sdp_type_to_string(type: WebRTCSDPType) -> str: ...

class WebRTCDTLSTransport(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCDTLSTransport(**properties)

    Object GstWebRTCDTLSTransport

    Properties from GstWebRTCDTLSTransport:
      session-id -> guint: Session ID
        Unique session ID
      transport -> GstWebRTCICETransport: ICE transport
        ICE transport used by this dtls transport
      state -> GstWebRTCDTLSTransportState: DTLS state
        State of the DTLS transport
      client -> gboolean: DTLS client
        Are we the client in the DTLS handshake?
      certificate -> gchararray: DTLS certificate
        DTLS certificate
      remote-certificate -> gchararray: Remote DTLS certificate
        Remote DTLS certificate

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
        certificate: str
        client: bool
        remote_certificate: str
        session_id: int
        state: WebRTCDTLSTransportState
        transport: WebRTCICETransport
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    def __init__(
        self,
        certificate: str = ...,
        client: bool = ...,
        session_id: int = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...

class WebRTCDTLSTransportClass(GObject.GPointer): ...

class WebRTCDataChannel(GObject.Object):
    """
    :Constructors:

    ::

        WebRTCDataChannel(**properties)

    Object GstWebRTCDataChannel

    Signals from GstWebRTCDataChannel:
      on-open ()
      on-close ()
      on-error (GError)
      on-message-data (GBytes)
      on-message-string (gchararray)
      on-buffered-amount-low ()
      send-data (GBytes)
      send-string (gchararray)
      close ()

    Properties from GstWebRTCDataChannel:
      label -> gchararray: Label
        Data channel label
      ordered -> gboolean: Ordered
        Using ordered transmission mode
      max-packet-lifetime -> gint: Maximum Packet Lifetime
        Maximum number of milliseconds that transmissions and retransmissions may occur in unreliable mode (-1 = unset)
      max-retransmits -> gint: Maximum Retransmits
        Maximum number of retransmissions attempted in unreliable mode
      protocol -> gchararray: Protocol
        Data channel protocol
      negotiated -> gboolean: Negotiated
        Whether this data channel was negotiated by the application
      id -> gint: ID
        ID negotiated by this data channel (-1 = unset)
      priority -> GstWebRTCPriorityType: Priority
        The priority of data sent using this data channel
      ready-state -> GstWebRTCDataChannelState: Ready State
        The Ready state of this data channel
      buffered-amount -> guint64: Buffered Amount
        The amount of data in bytes currently buffered
      buffered-amount-low-threshold -> guint64: Buffered Amount Low Threshold
        The threshold at which the buffered amount is considered low and the buffered-amount-low signal is emitted

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        buffered_amount: int
        buffered_amount_low_threshold: int
        id: int
        label: str
        max_packet_lifetime: int
        max_retransmits: int
        negotiated: bool
        ordered: bool
        priority: WebRTCPriorityType
        protocol: str
        ready_state: WebRTCDataChannelState

    props: Props = ...
    def __init__(
        self,
        buffered_amount_low_threshold: int = ...,
        id: int = ...,
        label: str = ...,
        max_packet_lifetime: int = ...,
        max_retransmits: int = ...,
        negotiated: bool = ...,
        ordered: bool = ...,
        priority: WebRTCPriorityType = ...,
        protocol: str = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def send_data(self, data: typing.Optional[GLib.Bytes] = None) -> None: ...
    def send_data_full(self, data: typing.Optional[GLib.Bytes] = None) -> bool: ...
    def send_string(self, str: typing.Optional[str] = None) -> None: ...
    def send_string_full(self, str: typing.Optional[str] = None) -> bool: ...

class WebRTCDataChannelClass(GObject.GPointer): ...

class WebRTCICE(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCICE(**properties)

    Object GstWebRTCICE

    Signals from GstWebRTCICE:
      add-local-ip-address (gchararray) -> gboolean

    Properties from GstWebRTCICE:
      min-rtp-port -> guint: ICE RTP candidate min port
        Minimum port for local rtp port range. min-rtp-port must be <= max-rtp-port
      max-rtp-port -> guint: ICE RTP candidate max port
        Maximum port for local rtp port range. max-rtp-port must be >= min-rtp-port

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
        max_rtp_port: int
        min_rtp_port: int
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    parent: Gst.Object = ...
    ice_gathering_state: WebRTCICEGatheringState = ...
    ice_connection_state: WebRTCICEConnectionState = ...
    min_rtp_port: int = ...
    max_rtp_port: int = ...
    def __init__(
        self,
        max_rtp_port: int = ...,
        min_rtp_port: int = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def add_candidate(
        self,
        stream: WebRTCICEStream,
        candidate: str,
        promise: typing.Optional[Gst.Promise] = None,
    ) -> None: ...
    def add_stream(self, session_id: int) -> typing.Optional[WebRTCICEStream]: ...
    def add_turn_server(self, uri: str) -> bool: ...
    def do_add_candidate(
        self,
        stream: WebRTCICEStream,
        candidate: str,
        promise: typing.Optional[Gst.Promise] = None,
    ) -> None: ...
    def do_add_stream(self, session_id: int) -> typing.Optional[WebRTCICEStream]: ...
    def do_add_turn_server(self, uri: str) -> bool: ...
    def do_find_transport(
        self, stream: WebRTCICEStream, component: WebRTCICEComponent
    ) -> typing.Optional[WebRTCICETransport]: ...
    def do_gather_candidates(self, stream: WebRTCICEStream) -> bool: ...
    def do_get_http_proxy(self) -> str: ...
    def do_get_is_controller(self) -> bool: ...
    def do_get_local_candidates(
        self, stream: WebRTCICEStream
    ) -> WebRTCICECandidateStats: ...
    def do_get_remote_candidates(
        self, stream: WebRTCICEStream
    ) -> WebRTCICECandidateStats: ...
    def do_get_selected_pair(
        self, stream: WebRTCICEStream
    ) -> typing.Tuple[bool, WebRTCICECandidateStats, WebRTCICECandidateStats]: ...
    def do_get_stun_server(self) -> typing.Optional[str]: ...
    def do_get_turn_server(self) -> typing.Optional[str]: ...
    def do_set_force_relay(self, force_relay: bool) -> None: ...
    def do_set_http_proxy(self, uri: str) -> None: ...
    def do_set_is_controller(self, controller: bool) -> None: ...
    def do_set_local_credentials(
        self, stream: WebRTCICEStream, ufrag: str, pwd: str
    ) -> bool: ...
    def do_set_on_ice_candidate(
        self, func: typing.Callable[..., None], *user_data: typing.Any
    ) -> None: ...
    def do_set_remote_credentials(
        self, stream: WebRTCICEStream, ufrag: str, pwd: str
    ) -> bool: ...
    def do_set_stun_server(self, uri: typing.Optional[str] = None) -> None: ...
    def do_set_tos(self, stream: WebRTCICEStream, tos: int) -> None: ...
    def do_set_turn_server(self, uri: typing.Optional[str] = None) -> None: ...
    def find_transport(
        self, stream: WebRTCICEStream, component: WebRTCICEComponent
    ) -> typing.Optional[WebRTCICETransport]: ...
    def gather_candidates(self, stream: WebRTCICEStream) -> bool: ...
    def get_http_proxy(self) -> str: ...
    def get_is_controller(self) -> bool: ...
    def get_local_candidates(
        self, stream: WebRTCICEStream
    ) -> list[WebRTCICECandidateStats]: ...
    def get_remote_candidates(
        self, stream: WebRTCICEStream
    ) -> list[WebRTCICECandidateStats]: ...
    def get_selected_pair(
        self, stream: WebRTCICEStream
    ) -> typing.Tuple[bool, WebRTCICECandidateStats, WebRTCICECandidateStats]: ...
    def get_stun_server(self) -> typing.Optional[str]: ...
    def get_turn_server(self) -> typing.Optional[str]: ...
    def set_force_relay(self, force_relay: bool) -> None: ...
    def set_http_proxy(self, uri: str) -> None: ...
    def set_is_controller(self, controller: bool) -> None: ...
    def set_local_credentials(
        self, stream: WebRTCICEStream, ufrag: str, pwd: str
    ) -> bool: ...
    def set_on_ice_candidate(
        self, func: typing.Callable[..., None], *user_data: typing.Any
    ) -> None: ...
    def set_remote_credentials(
        self, stream: WebRTCICEStream, ufrag: str, pwd: str
    ) -> bool: ...
    def set_stun_server(self, uri: typing.Optional[str] = None) -> None: ...
    def set_tos(self, stream: WebRTCICEStream, tos: int) -> None: ...
    def set_turn_server(self, uri: typing.Optional[str] = None) -> None: ...

class WebRTCICECandidateStats(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebRTCICECandidateStats()
    """

    ipaddr: str = ...
    port: int = ...
    stream_id: int = ...
    type: str = ...
    proto: str = ...
    relay_proto: str = ...
    prio: int = ...
    url: str = ...
    def copy(self) -> WebRTCICECandidateStats: ...
    def free(self) -> None: ...

class WebRTCICEClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebRTCICEClass()
    """

    parent_class: Gst.ObjectClass = ...
    add_stream: typing.Callable[
        [WebRTCICE, int], typing.Optional[WebRTCICEStream]
    ] = ...
    find_transport: typing.Callable[
        [WebRTCICE, WebRTCICEStream, WebRTCICEComponent],
        typing.Optional[WebRTCICETransport],
    ] = ...
    gather_candidates: typing.Callable[[WebRTCICE, WebRTCICEStream], bool] = ...
    add_candidate: typing.Callable[
        [WebRTCICE, WebRTCICEStream, str, typing.Optional[Gst.Promise]], None
    ] = ...
    set_local_credentials: typing.Callable[
        [WebRTCICE, WebRTCICEStream, str, str], bool
    ] = ...
    set_remote_credentials: typing.Callable[
        [WebRTCICE, WebRTCICEStream, str, str], bool
    ] = ...
    add_turn_server: typing.Callable[[WebRTCICE, str], bool] = ...
    set_is_controller: typing.Callable[[WebRTCICE, bool], None] = ...
    get_is_controller: typing.Callable[[WebRTCICE], bool] = ...
    set_force_relay: typing.Callable[[WebRTCICE, bool], None] = ...
    set_stun_server: typing.Callable[[WebRTCICE, typing.Optional[str]], None] = ...
    get_stun_server: typing.Callable[[WebRTCICE], typing.Optional[str]] = ...
    set_turn_server: typing.Callable[[WebRTCICE, typing.Optional[str]], None] = ...
    get_turn_server: typing.Callable[[WebRTCICE], typing.Optional[str]] = ...
    set_http_proxy: typing.Callable[[WebRTCICE, str], None] = ...
    get_http_proxy: typing.Callable[[WebRTCICE], str] = ...
    set_tos: typing.Callable[[WebRTCICE, WebRTCICEStream, int], None] = ...
    set_on_ice_candidate: typing.Callable[..., None] = ...
    get_local_candidates: typing.Callable[
        [WebRTCICE, WebRTCICEStream], WebRTCICECandidateStats
    ] = ...
    get_remote_candidates: typing.Callable[
        [WebRTCICE, WebRTCICEStream], WebRTCICECandidateStats
    ] = ...
    get_selected_pair: typing.Callable[
        [WebRTCICE, WebRTCICEStream],
        typing.Tuple[bool, WebRTCICECandidateStats, WebRTCICECandidateStats],
    ] = ...

class WebRTCICEStream(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCICEStream(**properties)

    Object GstWebRTCICEStream

    Properties from GstWebRTCICEStream:
      stream-id -> guint: ICE stream id
        ICE stream id associated with this stream

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
        stream_id: int
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    parent: Gst.Object = ...
    stream_id: int = ...
    def __init__(
        self,
        stream_id: int = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def do_find_transport(
        self, component: WebRTCICEComponent
    ) -> typing.Optional[WebRTCICETransport]: ...
    def do_gather_candidates(self) -> bool: ...
    def find_transport(
        self, component: WebRTCICEComponent
    ) -> typing.Optional[WebRTCICETransport]: ...
    def gather_candidates(self) -> bool: ...

class WebRTCICEStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebRTCICEStreamClass()
    """

    parent_class: Gst.ObjectClass = ...
    find_transport: typing.Callable[
        [WebRTCICEStream, WebRTCICEComponent], typing.Optional[WebRTCICETransport]
    ] = ...
    gather_candidates: typing.Callable[[WebRTCICEStream], bool] = ...

class WebRTCICETransport(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCICETransport(**properties)

    Object GstWebRTCICETransport

    Signals from GstWebRTCICETransport:
      on-selected-candidate-pair-change ()
      on-new-candidate (gchararray)

    Properties from GstWebRTCICETransport:
      component -> GstWebRTCICEComponent: ICE component
        The ICE component of this transport
      state -> GstWebRTCICEConnectionState: ICE connection state
        The ICE connection state of this transport
      gathering-state -> GstWebRTCICEGatheringState: ICE gathering state
        The ICE gathering state of this transport

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
        component: WebRTCICEComponent
        gathering_state: WebRTCICEGatheringState
        state: WebRTCICEConnectionState
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    parent: Gst.Object = ...
    role: WebRTCICERole = ...
    component: WebRTCICEComponent = ...
    state: WebRTCICEConnectionState = ...
    gathering_state: WebRTCICEGatheringState = ...
    src: Gst.Element = ...
    sink: Gst.Element = ...
    def __init__(
        self,
        component: WebRTCICEComponent = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def connection_state_change(self, new_state: WebRTCICEConnectionState) -> None: ...
    def do_gather_candidates(self) -> bool: ...
    def gathering_state_change(self, new_state: WebRTCICEGatheringState) -> None: ...
    def new_candidate(
        self, stream_id: int, component: WebRTCICEComponent, attr: str
    ) -> None: ...
    def selected_pair_change(self) -> None: ...

class WebRTCICETransportClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebRTCICETransportClass()
    """

    parent_class: Gst.ObjectClass = ...
    gather_candidates: typing.Callable[[WebRTCICETransport], bool] = ...

class WebRTCRTPReceiver(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCRTPReceiver(**properties)

    Object GstWebRTCRTPReceiver

    Properties from GstWebRTCRTPReceiver:
      transport -> GstWebRTCDTLSTransport: Transport
        The DTLS transport for this receiver

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
        transport: WebRTCDTLSTransport
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    def __init__(
        self, name: typing.Optional[str] = ..., parent: Gst.Object = ...
    ) -> None: ...

class WebRTCRTPReceiverClass(GObject.GPointer): ...

class WebRTCRTPSender(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCRTPSender(**properties)

    Object GstWebRTCRTPSender

    Properties from GstWebRTCRTPSender:
      priority -> GstWebRTCPriorityType: Priority
        The priority from which to set the DSCP field on packets
      transport -> GstWebRTCDTLSTransport: Transport
        The DTLS transport for this sender

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
        priority: WebRTCPriorityType
        transport: WebRTCDTLSTransport
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    def __init__(
        self,
        priority: WebRTCPriorityType = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...
    def set_priority(self, priority: WebRTCPriorityType) -> None: ...

class WebRTCRTPSenderClass(GObject.GPointer): ...

class WebRTCRTPTransceiver(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCRTPTransceiver(**properties)

    Object GstWebRTCRTPTransceiver

    Properties from GstWebRTCRTPTransceiver:
      sender -> GstWebRTCRTPSender: Sender
        The RTP sender for this transceiver
      receiver -> GstWebRTCRTPReceiver: Receiver
        The RTP receiver for this transceiver
      direction -> GstWebRTCRTPTransceiverDirection: Direction
        Transceiver direction
      mlineindex -> guint: Media Line Index
        Index in the SDP of the Media
      mid -> gchararray: Media ID
        The media ID of the m-line associated with this transceiver. This  association is established, when possible, whenever either a local or remote description is applied. This field is null if neither a local or remote description has been applied, or if its associated m-line is rejected by either a remote offer or any answer.
      current-direction -> GstWebRTCRTPTransceiverDirection: Current Direction
        Transceiver current direction
      kind -> GstWebRTCKind: Media Kind
        Kind of media this transceiver transports
      codec-preferences -> GstCaps: Codec Preferences
        Caps representing the codec preferences.

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
        codec_preferences: Gst.Caps
        current_direction: WebRTCRTPTransceiverDirection
        direction: WebRTCRTPTransceiverDirection
        kind: WebRTCKind
        mid: str
        mlineindex: int
        receiver: WebRTCRTPReceiver
        sender: WebRTCRTPSender
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    def __init__(
        self,
        codec_preferences: Gst.Caps = ...,
        direction: WebRTCRTPTransceiverDirection = ...,
        mlineindex: int = ...,
        receiver: WebRTCRTPReceiver = ...,
        sender: WebRTCRTPSender = ...,
        name: typing.Optional[str] = ...,
        parent: Gst.Object = ...,
    ) -> None: ...

class WebRTCRTPTransceiverClass(GObject.GPointer): ...

class WebRTCSCTPTransport(Gst.Object):
    """
    :Constructors:

    ::

        WebRTCSCTPTransport(**properties)

    Object GstWebRTCSCTPTransport

    Properties from GstWebRTCSCTPTransport:
      transport -> GstWebRTCDTLSTransport: WebRTC DTLS Transport
        DTLS transport used for this SCTP transport
      state -> GstWebRTCSCTPTransportState: WebRTC SCTP Transport state
        WebRTC SCTP Transport state
      max-message-size -> guint64: Maximum message size
        Maximum message size as reported by the transport
      max-channels -> guint: Maximum number of channels
        Maximum number of channels

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
        max_channels: int
        max_message_size: int
        state: WebRTCSCTPTransportState
        transport: WebRTCDTLSTransport
        name: typing.Optional[str]
        parent: typing.Optional[Gst.Object]

    props: Props = ...
    def __init__(
        self, name: typing.Optional[str] = ..., parent: Gst.Object = ...
    ) -> None: ...

class WebRTCSCTPTransportClass(GObject.GPointer): ...

class WebRTCSessionDescription(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebRTCSessionDescription()
        new(type:GstWebRTC.WebRTCSDPType, sdp:GstSdp.SDPMessage) -> GstWebRTC.WebRTCSessionDescription
    """

    type: WebRTCSDPType = ...
    sdp: GstSdp.SDPMessage = ...
    def copy(self) -> WebRTCSessionDescription: ...
    def free(self) -> None: ...
    @classmethod
    def new(
        cls, type: WebRTCSDPType, sdp: GstSdp.SDPMessage
    ) -> WebRTCSessionDescription: ...

class WebRTCBundlePolicy(GObject.GEnum):
    BALANCED = 1
    MAX_BUNDLE = 3
    MAX_COMPAT = 2
    NONE = 0

class WebRTCDTLSSetup(GObject.GEnum):
    ACTIVE = 2
    ACTPASS = 1
    NONE = 0
    PASSIVE = 3

class WebRTCDTLSTransportState(GObject.GEnum):
    CLOSED = 1
    CONNECTED = 4
    CONNECTING = 3
    FAILED = 2
    NEW = 0

class WebRTCDataChannelState(GObject.GEnum):
    CLOSED = 4
    CLOSING = 3
    CONNECTING = 1
    OPEN = 2

class WebRTCError(GObject.GEnum):
    DATA_CHANNEL_FAILURE = 0
    DTLS_FAILURE = 1
    ENCODER_ERROR = 6
    FINGERPRINT_FAILURE = 2
    HARDWARE_ENCODER_NOT_AVAILABLE = 5
    INTERNAL_FAILURE = 8
    INVALID_MODIFICATION = 9
    INVALID_STATE = 7
    SCTP_FAILURE = 3
    SDP_SYNTAX_ERROR = 4
    TYPE_ERROR = 10
    @staticmethod
    def quark() -> int: ...

class WebRTCFECType(GObject.GEnum):
    NONE = 0
    ULP_RED = 1

class WebRTCICEComponent(GObject.GEnum):
    RTCP = 1
    RTP = 0

class WebRTCICEConnectionState(GObject.GEnum):
    CHECKING = 1
    CLOSED = 6
    COMPLETED = 3
    CONNECTED = 2
    DISCONNECTED = 5
    FAILED = 4
    NEW = 0

class WebRTCICEGatheringState(GObject.GEnum):
    COMPLETE = 2
    GATHERING = 1
    NEW = 0

class WebRTCICERole(GObject.GEnum):
    CONTROLLED = 0
    CONTROLLING = 1

class WebRTCICETransportPolicy(GObject.GEnum):
    ALL = 0
    RELAY = 1

class WebRTCKind(GObject.GEnum):
    AUDIO = 1
    UNKNOWN = 0
    VIDEO = 2

class WebRTCPeerConnectionState(GObject.GEnum):
    CLOSED = 5
    CONNECTED = 2
    CONNECTING = 1
    DISCONNECTED = 3
    FAILED = 4
    NEW = 0

class WebRTCPriorityType(GObject.GEnum):
    HIGH = 4
    LOW = 2
    MEDIUM = 3
    VERY_LOW = 1

class WebRTCRTPTransceiverDirection(GObject.GEnum):
    INACTIVE = 1
    NONE = 0
    RECVONLY = 3
    SENDONLY = 2
    SENDRECV = 4

class WebRTCSCTPTransportState(GObject.GEnum):
    CLOSED = 3
    CONNECTED = 2
    CONNECTING = 1
    NEW = 0

class WebRTCSDPType(GObject.GEnum):
    ANSWER = 3
    OFFER = 1
    PRANSWER = 2
    ROLLBACK = 4
    @staticmethod
    def to_string(type: WebRTCSDPType) -> str: ...

class WebRTCSignalingState(GObject.GEnum):
    CLOSED = 1
    HAVE_LOCAL_OFFER = 2
    HAVE_LOCAL_PRANSWER = 4
    HAVE_REMOTE_OFFER = 3
    HAVE_REMOTE_PRANSWER = 5
    STABLE = 0

class WebRTCStatsType(GObject.GEnum):
    CANDIDATE_PAIR = 11
    CERTIFICATE = 14
    CODEC = 1
    CSRC = 6
    DATA_CHANNEL = 8
    INBOUND_RTP = 2
    LOCAL_CANDIDATE = 12
    OUTBOUND_RTP = 3
    PEER_CONNECTION = 7
    REMOTE_CANDIDATE = 13
    REMOTE_INBOUND_RTP = 4
    REMOTE_OUTBOUND_RTP = 5
    STREAM = 9
    TRANSPORT = 10
