from typing import Any
from typing import Final
from typing import Literal
from typing import Protocol
from typing import TypeAlias
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

from collections.abc import Callable
from collections.abc import Sequence

from gi import _gi
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstSdp

_DataTs = TypeVarTuple("_DataTs", default=Unpack[tuple[()]])

RTSP_DEFAULT_PORT: Final[int]

def rtsp_auth_credentials_free(credentials: RTSPAuthCredential) -> None: ...
def rtsp_connection_accept(
    socket: Gio.Socket, cancellable: Gio.Cancellable | None = None
) -> tuple[RTSPResult, RTSPConnection | None]: ...
def rtsp_connection_create(url: RTSPUrl) -> tuple[RTSPResult, RTSPConnection]: ...
def rtsp_connection_create_from_socket(
    socket: Gio.Socket, ip: str, port: int, initial_buffer: str
) -> tuple[RTSPResult, RTSPConnection | None]: ...
def rtsp_find_header_field(header: str) -> RTSPHeaderField: ...
def rtsp_find_method(method: str) -> RTSPMethod: ...
def rtsp_generate_digest_auth_response(
    algorithm: str | None,
    method: str,
    realm: str,
    username: str,
    password: str,
    uri: str,
    nonce: str,
) -> str | None: ...
def rtsp_generate_digest_auth_response_from_md5(
    algorithm: str | None, method: str, md5: str, uri: str, nonce: str
) -> str | None: ...
def rtsp_header_allow_multiple(field: _RTSPHeaderFieldValueType) -> bool: ...
def rtsp_header_as_text(field: _RTSPHeaderFieldValueType) -> str | None: ...
def rtsp_message_new() -> tuple[RTSPResult, RTSPMessage]: ...
def rtsp_message_new_data(channel: int) -> tuple[RTSPResult, RTSPMessage]: ...
def rtsp_message_new_request(
    method: _RTSPMethodValueType, uri: str
) -> tuple[RTSPResult, RTSPMessage]: ...
def rtsp_message_new_response(
    code: _RTSPStatusCodeValueType,
    reason: str | None = None,
    request: RTSPMessage | None = None,
) -> tuple[RTSPResult, RTSPMessage]: ...
def rtsp_method_as_text(method: _RTSPMethodValueType) -> str | None: ...
def rtsp_options_as_text(options: _RTSPMethodValueType) -> str: ...
def rtsp_options_from_text(options: str) -> RTSPMethod: ...
def rtsp_range_convert_units(
    range: RTSPTimeRange, unit: _RTSPRangeUnitValueType
) -> bool: ...
def rtsp_range_free(range: RTSPTimeRange) -> None: ...
def rtsp_range_get_times(range: RTSPTimeRange) -> tuple[bool, int, int]: ...
def rtsp_range_parse(rangestr: str) -> tuple[RTSPResult, RTSPTimeRange]: ...
def rtsp_range_to_string(range: RTSPTimeRange) -> str: ...
def rtsp_status_as_text(code: _RTSPStatusCodeValueType) -> str: ...
def rtsp_strresult(result: _RTSPResultValueType) -> str: ...
def rtsp_transport_get_manager(
    trans: _RTSPTransModeValueType, option: int
) -> tuple[RTSPResult, str | None]: ...
def rtsp_transport_get_mime(
    trans: _RTSPTransModeValueType,
) -> tuple[RTSPResult, str]: ...
def rtsp_transport_init() -> tuple[RTSPResult, RTSPTransport]: ...
def rtsp_transport_new() -> tuple[RTSPResult, RTSPTransport]: ...
def rtsp_transport_parse(str: str) -> tuple[RTSPResult, RTSPTransport]: ...
def rtsp_url_parse(urlstr: str) -> tuple[RTSPResult, RTSPUrl | None]: ...
def rtsp_version_as_text(version: _RTSPVersionValueType) -> str: ...

class RTSPAuthCredential(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPAuthCredential()
    """

    scheme: RTSPAuthMethod
    params: RTSPAuthParam
    authorization: str

class RTSPAuthParam(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPAuthParam()
    """

    name: str
    value: str
    def copy(self) -> RTSPAuthParam: ...
    def free(self) -> None: ...

class RTSPConnection(_gi.Struct):
    @staticmethod
    def accept(
        socket: Gio.Socket, cancellable: Gio.Cancellable | None = None
    ) -> tuple[RTSPResult, RTSPConnection | None]: ...
    def add_extra_http_request_header(self, key: str, value: str) -> None: ...
    def clear_auth_params(self) -> None: ...
    def close(self) -> RTSPResult: ...
    def connect(self, timeout: GLib.TimeVal) -> RTSPResult: ...
    def connect_usec(self, timeout: int) -> RTSPResult: ...
    def connect_with_response(
        self, timeout: GLib.TimeVal, response: RTSPMessage
    ) -> RTSPResult: ...
    def connect_with_response_usec(
        self, timeout: int, response: RTSPMessage
    ) -> RTSPResult: ...
    @staticmethod
    def create(url: RTSPUrl) -> tuple[RTSPResult, RTSPConnection]: ...
    @staticmethod
    def create_from_socket(
        socket: Gio.Socket, ip: str, port: int, initial_buffer: str
    ) -> tuple[RTSPResult, RTSPConnection | None]: ...
    def do_tunnel(self, conn2: RTSPConnection | None = None) -> RTSPResult: ...
    def flush(self, flush: bool) -> RTSPResult: ...
    def free(self) -> RTSPResult: ...
    def get_ignore_x_server_reply(self) -> bool: ...
    def get_ip(self) -> str | None: ...
    def get_read_socket(self) -> Gio.Socket | None: ...
    def get_remember_session_id(self) -> bool: ...
    def get_tls(self) -> Gio.TlsConnection: ...
    def get_tls_database(self) -> Gio.TlsDatabase | None: ...
    def get_tls_interaction(self) -> Gio.TlsInteraction | None: ...
    def get_tls_validation_flags(self) -> Gio.TlsCertificateFlags: ...
    def get_tunnelid(self) -> str | None: ...
    def get_url(self) -> RTSPUrl: ...
    def get_write_socket(self) -> Gio.Socket | None: ...
    def is_tunneled(self) -> bool: ...
    def next_timeout(self, timeout: GLib.TimeVal) -> RTSPResult: ...
    def next_timeout_usec(self) -> int: ...
    def poll(
        self, events: _RTSPEventValueType, timeout: GLib.TimeVal
    ) -> tuple[RTSPResult, RTSPEvent]: ...
    def poll_usec(
        self, events: _RTSPEventValueType, timeout: int
    ) -> tuple[RTSPResult, RTSPEvent]: ...
    def read(self, data: Sequence[int], timeout: GLib.TimeVal) -> RTSPResult: ...
    def read_usec(self, data: Sequence[int], timeout: int) -> RTSPResult: ...
    def receive(self, message: RTSPMessage, timeout: GLib.TimeVal) -> RTSPResult: ...
    def receive_usec(self, message: RTSPMessage, timeout: int) -> RTSPResult: ...
    def reset_timeout(self) -> RTSPResult: ...
    def send(self, message: RTSPMessage, timeout: GLib.TimeVal) -> RTSPResult: ...
    def send_messages(
        self, messages: Sequence[RTSPMessage], timeout: GLib.TimeVal
    ) -> RTSPResult: ...
    def send_messages_usec(
        self, messages: Sequence[RTSPMessage], timeout: int
    ) -> RTSPResult: ...
    def send_usec(self, message: RTSPMessage, timeout: int) -> RTSPResult: ...
    def set_accept_certificate_func(
        self,
        func: Callable[
            [
                Gio.TlsConnection,
                Gio.TlsCertificate,
                Gio._TlsCertificateFlagsValueType,
                Unpack[_DataTs],
            ],
            bool,
        ],
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    def set_auth(
        self, method: _RTSPAuthMethodValueType, user: str, pass_: str
    ) -> RTSPResult: ...
    def set_auth_param(self, param: str, value: str) -> None: ...
    def set_content_length_limit(self, limit: int) -> None: ...
    def set_http_mode(self, enable: bool) -> None: ...
    def set_ignore_x_server_reply(self, ignore: bool) -> None: ...
    def set_ip(self, ip: str) -> None: ...
    def set_proxy(self, host: str, port: int) -> RTSPResult: ...
    def set_qos_dscp(self, qos_dscp: int) -> RTSPResult: ...
    def set_remember_session_id(self, remember: bool) -> None: ...
    def set_tls_database(self, database: Gio.TlsDatabase | None = None) -> None: ...
    def set_tls_interaction(
        self, interaction: Gio.TlsInteraction | None = None
    ) -> None: ...
    def set_tls_validation_flags(
        self, flags: Gio._TlsCertificateFlagsValueType
    ) -> bool: ...
    def set_tunneled(self, tunneled: bool) -> None: ...
    def write(self, data: Sequence[int], timeout: GLib.TimeVal) -> RTSPResult: ...
    def write_usec(self, data: Sequence[int], timeout: int) -> RTSPResult: ...

class RTSPExtension(GObject.GInterface, Protocol):
    """
    Interface GstRTSPExtension
    """
    def after_send(self, req: RTSPMessage, resp: RTSPMessage) -> RTSPResult: ...
    def before_send(self, req: RTSPMessage) -> RTSPResult: ...
    def configure_stream(self, caps: Gst.Caps) -> bool: ...
    def detect_server(self, resp: RTSPMessage) -> bool: ...
    def get_transports(
        self, protocols: _RTSPLowerTransValueType, transport: str
    ) -> RTSPResult: ...
    def parse_sdp(self, sdp: GstSdp.SDPMessage, s: Gst.Structure) -> RTSPResult: ...
    def receive_request(self, req: RTSPMessage) -> RTSPResult: ...
    def send(self, req: RTSPMessage, resp: RTSPMessage) -> RTSPResult: ...
    def setup_media(self, media: GstSdp.SDPMedia) -> RTSPResult: ...
    def stream_select(self, url: RTSPUrl) -> RTSPResult: ...

class RTSPExtensionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPExtensionInterface()
    """
    @property
    def parent(self) -> GObject.TypeInterface: ...
    @property
    def detect_server(self) -> Callable[[RTSPExtension, RTSPMessage], bool]: ...
    @property
    def before_send(self) -> Callable[[RTSPExtension, RTSPMessage], RTSPResult]: ...
    @property
    def after_send(
        self,
    ) -> Callable[[RTSPExtension, RTSPMessage, RTSPMessage], RTSPResult]: ...
    @property
    def parse_sdp(
        self,
    ) -> Callable[[RTSPExtension, GstSdp.SDPMessage, Gst.Structure], RTSPResult]: ...
    @property
    def setup_media(self) -> Callable[[RTSPExtension, GstSdp.SDPMedia], RTSPResult]: ...
    @property
    def configure_stream(self) -> Callable[[RTSPExtension, Gst.Caps], bool]: ...
    @property
    def get_transports(
        self,
    ) -> Callable[[RTSPExtension, _RTSPLowerTransValueType, str], RTSPResult]: ...
    @property
    def stream_select(self) -> Callable[[RTSPExtension, RTSPUrl], RTSPResult]: ...
    @property
    def send(
        self,
    ) -> Callable[[RTSPExtension, RTSPMessage, RTSPMessage], RTSPResult]: ...
    @property
    def receive_request(self) -> Callable[[RTSPExtension, RTSPMessage], RTSPResult]: ...

class RTSPMessage(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPMessage()
    """

    type: RTSPMsgType
    @property
    def hdr_fields(self) -> list[int]: ...
    @property
    def body(self) -> int: ...
    @property
    def body_size(self) -> int: ...
    @property
    def body_buffer(self) -> Gst.Buffer: ...
    def add_header(
        self, field: _RTSPHeaderFieldValueType, value: str
    ) -> RTSPResult: ...
    def add_header_by_name(self, header: str, value: str) -> RTSPResult: ...
    def append_headers(self, str: GLib.String) -> RTSPResult: ...
    def copy(self) -> tuple[RTSPResult, RTSPMessage | None]: ...
    def dump(self) -> RTSPResult: ...
    def free(self) -> RTSPResult: ...
    def get_body(self) -> tuple[RTSPResult, bytes]: ...
    def get_body_buffer(self) -> tuple[RTSPResult, Gst.Buffer]: ...
    def get_header(
        self, field: _RTSPHeaderFieldValueType, indx: int
    ) -> tuple[RTSPResult, str | None]: ...
    def get_header_by_name(
        self, header: str, index: int
    ) -> tuple[RTSPResult, str | None]: ...
    def get_type(self) -> RTSPMsgType: ...
    def has_body_buffer(self) -> bool: ...
    def init(self) -> RTSPResult: ...
    def init_data(self, channel: int) -> RTSPResult: ...
    def init_request(self, method: _RTSPMethodValueType, uri: str) -> RTSPResult: ...
    def init_response(
        self,
        code: _RTSPStatusCodeValueType,
        reason: str | None = None,
        request: RTSPMessage | None = None,
    ) -> RTSPResult: ...
    def parse_auth_credentials(
        self, field: _RTSPHeaderFieldValueType
    ) -> list[RTSPAuthCredential]: ...
    def parse_data(self) -> tuple[RTSPResult, int]: ...
    def parse_request(self) -> tuple[RTSPResult, RTSPMethod, str, RTSPVersion]: ...
    def parse_response(self) -> tuple[RTSPResult, RTSPStatusCode, str, RTSPVersion]: ...
    def remove_header(
        self, field: _RTSPHeaderFieldValueType, indx: int
    ) -> RTSPResult: ...
    def remove_header_by_name(self, header: str, index: int) -> RTSPResult: ...
    def set_body(self, data: Sequence[int]) -> RTSPResult: ...
    def set_body_buffer(self, buffer: Gst.Buffer) -> RTSPResult: ...
    def steal_body(self) -> tuple[RTSPResult, bytes]: ...
    def steal_body_buffer(self) -> tuple[RTSPResult, Gst.Buffer]: ...
    def take_body(self, data: Sequence[int]) -> RTSPResult: ...
    def take_body_buffer(self, buffer: Gst.Buffer) -> RTSPResult: ...
    def take_header(
        self, field: _RTSPHeaderFieldValueType, value: str
    ) -> RTSPResult: ...
    def take_header_by_name(self, header: str, value: str) -> RTSPResult: ...
    def unset(self) -> RTSPResult: ...

class RTSPRange(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPRange()
    """

    min: int
    max: int
    @staticmethod
    def convert_units(range: RTSPTimeRange, unit: _RTSPRangeUnitValueType) -> bool: ...
    @staticmethod
    def free(range: RTSPTimeRange) -> None: ...
    @staticmethod
    def get_times(range: RTSPTimeRange) -> tuple[bool, int, int]: ...
    @staticmethod
    def parse(rangestr: str) -> tuple[RTSPResult, RTSPTimeRange]: ...
    @staticmethod
    def to_string(range: RTSPTimeRange) -> str: ...

class RTSPTime(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPTime()
    """

    type: RTSPTimeType
    seconds: float

class RTSPTime2(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPTime2()
    """

    frames: float
    year: int
    month: int
    day: int

class RTSPTimeRange(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPTimeRange()
    """

    unit: RTSPRangeUnit
    min: RTSPTime
    max: RTSPTime
    min2: RTSPTime2
    max2: RTSPTime2

class RTSPTransport(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPTransport()
    """

    trans: RTSPTransMode
    profile: RTSPProfile
    lower_transport: RTSPLowerTrans
    destination: str
    source: str
    layers: int
    mode_play: bool
    mode_record: bool
    append: bool
    interleaved: RTSPRange
    ttl: int
    port: RTSPRange
    client_port: RTSPRange
    server_port: RTSPRange
    ssrc: int
    def as_text(self) -> str | None: ...
    def free(self) -> RTSPResult: ...
    @staticmethod
    def get_manager(
        trans: _RTSPTransModeValueType, option: int
    ) -> tuple[RTSPResult, str | None]: ...
    def get_media_type(self) -> tuple[RTSPResult, str]: ...
    @staticmethod
    def get_mime(trans: _RTSPTransModeValueType) -> tuple[RTSPResult, str]: ...
    @staticmethod
    def init() -> tuple[RTSPResult, RTSPTransport]: ...
    @staticmethod
    def new() -> tuple[RTSPResult, RTSPTransport]: ...
    @staticmethod
    def parse(str: str) -> tuple[RTSPResult, RTSPTransport]: ...

class RTSPUrl(GObject.GBoxed):
    """
    :Constructors:

    ::

        RTSPUrl()
    """

    transports: RTSPLowerTrans
    family: RTSPFamily
    user: str
    passwd: str
    host: str
    port: int
    abspath: str
    query: str
    def copy(self) -> RTSPUrl: ...
    def decode_path_components(self) -> list[str]: ...
    def free(self) -> None: ...
    def get_port(self) -> tuple[RTSPResult, int]: ...
    def get_request_uri(self) -> str: ...
    def get_request_uri_with_control(self, control_path: str) -> str: ...
    @staticmethod
    def parse(urlstr: str) -> tuple[RTSPResult, RTSPUrl | None]: ...
    def set_port(self, port: int) -> RTSPResult: ...

class RTSPWatch(_gi.Struct):
    def attach(self, context: GLib.MainContext | None = None) -> int: ...
    def get_send_backlog(self) -> tuple[int, int]: ...
    def reset(self) -> None: ...
    def send_message(self, message: RTSPMessage) -> tuple[RTSPResult, int]: ...
    def send_messages(
        self, messages: Sequence[RTSPMessage]
    ) -> tuple[RTSPResult, int]: ...
    def set_flushing(self, flushing: bool) -> None: ...
    def set_send_backlog(self, bytes: int, messages: int) -> None: ...
    def unref(self) -> None: ...
    def wait_backlog(self, timeout: GLib.TimeVal) -> RTSPResult: ...
    def wait_backlog_usec(self, timeout: int) -> RTSPResult: ...
    def write_data(self, data: Sequence[int]) -> tuple[RTSPResult, int]: ...

class RTSPWatchFuncs(_gi.Struct):
    """
    :Constructors:

    ::

        RTSPWatchFuncs()
    """
    @property
    def message_received(
        self,
    ) -> Callable[[RTSPWatch, RTSPMessage, Any | None], RTSPResult]: ...
    @property
    def message_sent(self) -> Callable[[RTSPWatch, int, Any | None], RTSPResult]: ...
    @property
    def closed(self) -> Callable[[RTSPWatch, Any | None], RTSPResult]: ...
    @property
    def error(
        self,
    ) -> Callable[[RTSPWatch, _RTSPResultValueType, Any | None], RTSPResult]: ...
    @property
    def tunnel_start(self) -> Callable[[RTSPWatch, Any | None], RTSPStatusCode]: ...
    @property
    def tunnel_complete(self) -> Callable[[RTSPWatch, Any | None], RTSPResult]: ...
    @property
    def error_full(
        self,
    ) -> Callable[
        [RTSPWatch, _RTSPResultValueType, RTSPMessage, int, Any | None], RTSPResult
    ]: ...
    @property
    def tunnel_lost(self) -> Callable[[RTSPWatch, Any | None], RTSPResult]: ...
    @property
    def tunnel_http_response(
        self,
    ) -> Callable[[RTSPWatch, RTSPMessage, RTSPMessage, Any | None], RTSPResult]: ...

class RTSPEvent(GObject.GFlags):
    READ = 1
    WRITE = 2

_RTSPEventLiteralType: TypeAlias = Literal[
    "GST_RTSP_EV_READ", "GST_RTSP_EV_WRITE", "read", "write"
]
_RTSPEventValueType: TypeAlias = (
    RTSPEvent | _RTSPEventLiteralType | tuple[_RTSPEventLiteralType, ...]
)

class RTSPLowerTrans(GObject.GFlags):
    HTTP = 16
    TCP = 4
    TLS = 32
    UDP = 1
    UDP_MCAST = 2
    UNKNOWN = 0

_RTSPLowerTransLiteralType: TypeAlias = Literal[
    "GST_RTSP_LOWER_TRANS_HTTP",
    "GST_RTSP_LOWER_TRANS_TCP",
    "GST_RTSP_LOWER_TRANS_TLS",
    "GST_RTSP_LOWER_TRANS_UDP",
    "GST_RTSP_LOWER_TRANS_UDP_MCAST",
    "GST_RTSP_LOWER_TRANS_UNKNOWN",
    "http",
    "tcp",
    "tls",
    "udp",
    "udp-mcast",
    "unknown",
]
_RTSPLowerTransValueType: TypeAlias = (
    RTSPLowerTrans | _RTSPLowerTransLiteralType | tuple[_RTSPLowerTransLiteralType, ...]
)

class RTSPMethod(GObject.GFlags):
    ANNOUNCE = 2
    DESCRIBE = 1
    GET = 2048
    GET_PARAMETER = 4
    INVALID = 0
    OPTIONS = 8
    PAUSE = 16
    PLAY = 32
    POST = 4096
    RECORD = 64
    REDIRECT = 128
    SETUP = 256
    SET_PARAMETER = 512
    TEARDOWN = 1024
    @staticmethod
    def as_text(method: _RTSPMethodValueType) -> str | None: ...

_RTSPMethodLiteralType: TypeAlias = Literal[
    "GST_RTSP_ANNOUNCE",
    "GST_RTSP_DESCRIBE",
    "GST_RTSP_GET",
    "GST_RTSP_GET_PARAMETER",
    "GST_RTSP_INVALID",
    "GST_RTSP_OPTIONS",
    "GST_RTSP_PAUSE",
    "GST_RTSP_PLAY",
    "GST_RTSP_POST",
    "GST_RTSP_RECORD",
    "GST_RTSP_REDIRECT",
    "GST_RTSP_SETUP",
    "GST_RTSP_SET_PARAMETER",
    "GST_RTSP_TEARDOWN",
    "announce",
    "describe",
    "get",
    "get-parameter",
    "invalid",
    "options",
    "pause",
    "play",
    "post",
    "record",
    "redirect",
    "set-parameter",
    "setup",
    "teardown",
]
_RTSPMethodValueType: TypeAlias = (
    RTSPMethod | _RTSPMethodLiteralType | tuple[_RTSPMethodLiteralType, ...]
)

class RTSPProfile(GObject.GFlags):
    AVP = 1
    AVPF = 4
    SAVP = 2
    SAVPF = 8
    UNKNOWN = 0

_RTSPProfileLiteralType: TypeAlias = Literal[
    "GST_RTSP_PROFILE_AVP",
    "GST_RTSP_PROFILE_AVPF",
    "GST_RTSP_PROFILE_SAVP",
    "GST_RTSP_PROFILE_SAVPF",
    "GST_RTSP_PROFILE_UNKNOWN",
    "avp",
    "avpf",
    "savp",
    "savpf",
    "unknown",
]
_RTSPProfileValueType: TypeAlias = (
    RTSPProfile | _RTSPProfileLiteralType | tuple[_RTSPProfileLiteralType, ...]
)

class RTSPTransMode(GObject.GFlags):
    RDT = 2
    RTP = 1
    UNKNOWN = 0

_RTSPTransModeLiteralType: TypeAlias = Literal[
    "GST_RTSP_TRANS_RDT",
    "GST_RTSP_TRANS_RTP",
    "GST_RTSP_TRANS_UNKNOWN",
    "rdt",
    "rtp",
    "unknown",
]
_RTSPTransModeValueType: TypeAlias = (
    RTSPTransMode | _RTSPTransModeLiteralType | tuple[_RTSPTransModeLiteralType, ...]
)

class RTSPAuthMethod(GObject.GEnum):
    BASIC = 1
    DIGEST = 2
    NONE = 0

_RTSPAuthMethodLiteralType: TypeAlias = Literal[
    "GST_RTSP_AUTH_BASIC",
    "GST_RTSP_AUTH_DIGEST",
    "GST_RTSP_AUTH_NONE",
    "basic",
    "digest",
    "none",
]
_RTSPAuthMethodValueType: TypeAlias = RTSPAuthMethod | _RTSPAuthMethodLiteralType

class RTSPFamily(GObject.GEnum):
    INET = 1
    INET6 = 2
    NONE = 0

_RTSPFamilyLiteralType: TypeAlias = Literal[
    "GST_RTSP_FAM_INET",
    "GST_RTSP_FAM_INET6",
    "GST_RTSP_FAM_NONE",
    "inet",
    "inet6",
    "none",
]
_RTSPFamilyValueType: TypeAlias = RTSPFamily | _RTSPFamilyLiteralType

class RTSPHeaderField(GObject.GEnum):
    ACCEPT = 1
    ACCEPT_CHARSET = 56
    ACCEPT_ENCODING = 2
    ACCEPT_LANGUAGE = 3
    ACCEPT_RANGES = 86
    ALERT = 45
    ALLOW = 4
    AUTHENTICATION_INFO = 76
    AUTHORIZATION = 5
    BANDWIDTH = 6
    BLOCKSIZE = 7
    CACHE_CONTROL = 8
    CLIENT_CHALLENGE = 40
    CLIENT_ID = 46
    COMPANY_ID = 47
    CONFERENCE = 9
    CONNECTION = 10
    CONTENT_BASE = 11
    CONTENT_ENCODING = 12
    CONTENT_LANGUAGE = 13
    CONTENT_LENGTH = 14
    CONTENT_LOCATION = 15
    CONTENT_TYPE = 16
    CSEQ = 17
    DATE = 18
    ETAG = 54
    EXPIRES = 19
    FRAMES = 87
    FROM = 20
    GUID = 48
    HOST = 77
    IF_MATCH = 55
    IF_MODIFIED_SINCE = 21
    INVALID = 0
    KEYMGMT = 82
    LANGUAGE = 51
    LAST = 89
    LAST_MODIFIED = 22
    LOCATION = 53
    MAX_ASM_WIDTH = 50
    MEDIA_PROPERTIES = 84
    PIPELINED_REQUESTS = 83
    PLAYER_START_TIME = 52
    PRAGMA = 78
    PROXY_AUTHENTICATE = 23
    PROXY_REQUIRE = 24
    PUBLIC = 25
    RANGE = 26
    RATE_CONTROL = 88
    REAL_CHALLENGE1 = 41
    REAL_CHALLENGE2 = 42
    REAL_CHALLENGE3 = 43
    REFERER = 27
    REGION_DATA = 49
    REQUIRE = 28
    RETRY_AFTER = 29
    RTCP_INTERVAL = 81
    RTP_INFO = 30
    SCALE = 31
    SEEK_STYLE = 85
    SERVER = 33
    SESSION = 32
    SPEED = 34
    SUBSCRIBE = 44
    SUPPORTED = 57
    TIMESTAMP = 75
    TRANSPORT = 35
    UNSUPPORTED = 36
    USER_AGENT = 37
    VARY = 58
    VIA = 38
    WWW_AUTHENTICATE = 39
    X_ACCELERATE_STREAMING = 59
    X_ACCEPT_AUTHENT = 60
    X_ACCEPT_PROXY_AUTHENT = 61
    X_BROADCAST_ID = 62
    X_BURST_STREAMING = 63
    X_NOTICE = 64
    X_PLAYER_LAG_TIME = 65
    X_PLAYLIST = 66
    X_PLAYLIST_CHANGE_NOTICE = 67
    X_PLAYLIST_GEN_ID = 68
    X_PLAYLIST_SEEK_ID = 69
    X_PROXY_CLIENT_AGENT = 70
    X_PROXY_CLIENT_VERB = 71
    X_RECEDING_PLAYLISTCHANGE = 72
    X_RTP_INFO = 73
    X_SERVER_IP_ADDRESS = 79
    X_SESSIONCOOKIE = 80
    X_STARTUPPROFILE = 74

_RTSPHeaderFieldLiteralType: TypeAlias = Literal[
    "GST_RTSP_HDR_ACCEPT",
    "GST_RTSP_HDR_ACCEPT_CHARSET",
    "GST_RTSP_HDR_ACCEPT_ENCODING",
    "GST_RTSP_HDR_ACCEPT_LANGUAGE",
    "GST_RTSP_HDR_ACCEPT_RANGES",
    "GST_RTSP_HDR_ALERT",
    "GST_RTSP_HDR_ALLOW",
    "GST_RTSP_HDR_AUTHENTICATION_INFO",
    "GST_RTSP_HDR_AUTHORIZATION",
    "GST_RTSP_HDR_BANDWIDTH",
    "GST_RTSP_HDR_BLOCKSIZE",
    "GST_RTSP_HDR_CACHE_CONTROL",
    "GST_RTSP_HDR_CLIENT_CHALLENGE",
    "GST_RTSP_HDR_CLIENT_ID",
    "GST_RTSP_HDR_COMPANY_ID",
    "GST_RTSP_HDR_CONFERENCE",
    "GST_RTSP_HDR_CONNECTION",
    "GST_RTSP_HDR_CONTENT_BASE",
    "GST_RTSP_HDR_CONTENT_ENCODING",
    "GST_RTSP_HDR_CONTENT_LANGUAGE",
    "GST_RTSP_HDR_CONTENT_LENGTH",
    "GST_RTSP_HDR_CONTENT_LOCATION",
    "GST_RTSP_HDR_CONTENT_TYPE",
    "GST_RTSP_HDR_CSEQ",
    "GST_RTSP_HDR_DATE",
    "GST_RTSP_HDR_ETAG",
    "GST_RTSP_HDR_EXPIRES",
    "GST_RTSP_HDR_FRAMES",
    "GST_RTSP_HDR_FROM",
    "GST_RTSP_HDR_GUID",
    "GST_RTSP_HDR_HOST",
    "GST_RTSP_HDR_IF_MATCH",
    "GST_RTSP_HDR_IF_MODIFIED_SINCE",
    "GST_RTSP_HDR_INVALID",
    "GST_RTSP_HDR_KEYMGMT",
    "GST_RTSP_HDR_LANGUAGE",
    "GST_RTSP_HDR_LAST",
    "GST_RTSP_HDR_LAST_MODIFIED",
    "GST_RTSP_HDR_LOCATION",
    "GST_RTSP_HDR_MAX_ASM_WIDTH",
    "GST_RTSP_HDR_MEDIA_PROPERTIES",
    "GST_RTSP_HDR_PIPELINED_REQUESTS",
    "GST_RTSP_HDR_PLAYER_START_TIME",
    "GST_RTSP_HDR_PRAGMA",
    "GST_RTSP_HDR_PROXY_AUTHENTICATE",
    "GST_RTSP_HDR_PROXY_REQUIRE",
    "GST_RTSP_HDR_PUBLIC",
    "GST_RTSP_HDR_RANGE",
    "GST_RTSP_HDR_RATE_CONTROL",
    "GST_RTSP_HDR_REAL_CHALLENGE1",
    "GST_RTSP_HDR_REAL_CHALLENGE2",
    "GST_RTSP_HDR_REAL_CHALLENGE3",
    "GST_RTSP_HDR_REFERER",
    "GST_RTSP_HDR_REGION_DATA",
    "GST_RTSP_HDR_REQUIRE",
    "GST_RTSP_HDR_RETRY_AFTER",
    "GST_RTSP_HDR_RTCP_INTERVAL",
    "GST_RTSP_HDR_RTP_INFO",
    "GST_RTSP_HDR_SCALE",
    "GST_RTSP_HDR_SEEK_STYLE",
    "GST_RTSP_HDR_SERVER",
    "GST_RTSP_HDR_SESSION",
    "GST_RTSP_HDR_SPEED",
    "GST_RTSP_HDR_SUBSCRIBE",
    "GST_RTSP_HDR_SUPPORTED",
    "GST_RTSP_HDR_TIMESTAMP",
    "GST_RTSP_HDR_TRANSPORT",
    "GST_RTSP_HDR_UNSUPPORTED",
    "GST_RTSP_HDR_USER_AGENT",
    "GST_RTSP_HDR_VARY",
    "GST_RTSP_HDR_VIA",
    "GST_RTSP_HDR_WWW_AUTHENTICATE",
    "GST_RTSP_HDR_X_ACCELERATE_STREAMING",
    "GST_RTSP_HDR_X_ACCEPT_AUTHENT",
    "GST_RTSP_HDR_X_ACCEPT_PROXY_AUTHENT",
    "GST_RTSP_HDR_X_BROADCAST_ID",
    "GST_RTSP_HDR_X_BURST_STREAMING",
    "GST_RTSP_HDR_X_NOTICE",
    "GST_RTSP_HDR_X_PLAYER_LAG_TIME",
    "GST_RTSP_HDR_X_PLAYLIST",
    "GST_RTSP_HDR_X_PLAYLIST_CHANGE_NOTICE",
    "GST_RTSP_HDR_X_PLAYLIST_GEN_ID",
    "GST_RTSP_HDR_X_PLAYLIST_SEEK_ID",
    "GST_RTSP_HDR_X_PROXY_CLIENT_AGENT",
    "GST_RTSP_HDR_X_PROXY_CLIENT_VERB",
    "GST_RTSP_HDR_X_RECEDING_PLAYLISTCHANGE",
    "GST_RTSP_HDR_X_RTP_INFO",
    "GST_RTSP_HDR_X_SERVER_IP_ADDRESS",
    "GST_RTSP_HDR_X_SESSIONCOOKIE",
    "GST_RTSP_HDR_X_STARTUPPROFILE",
    "accept",
    "accept-charset",
    "accept-encoding",
    "accept-language",
    "accept-ranges",
    "alert",
    "allow",
    "authentication-info",
    "authorization",
    "bandwidth",
    "blocksize",
    "cache-control",
    "client-challenge",
    "client-id",
    "company-id",
    "conference",
    "connection",
    "content-base",
    "content-encoding",
    "content-language",
    "content-length",
    "content-location",
    "content-type",
    "cseq",
    "date",
    "etag",
    "expires",
    "frames",
    "from",
    "guid",
    "host",
    "if-match",
    "if-modified-since",
    "invalid",
    "keymgmt",
    "language",
    "last",
    "last-modified",
    "location",
    "max-asm-width",
    "media-properties",
    "pipelined-requests",
    "player-start-time",
    "pragma",
    "proxy-authenticate",
    "proxy-require",
    "public",
    "range",
    "rate-control",
    "real-challenge1",
    "real-challenge2",
    "real-challenge3",
    "referer",
    "region-data",
    "require",
    "retry-after",
    "rtcp-interval",
    "rtp-info",
    "scale",
    "seek-style",
    "server",
    "session",
    "speed",
    "subscribe",
    "supported",
    "timestamp",
    "transport",
    "unsupported",
    "user-agent",
    "vary",
    "via",
    "www-authenticate",
    "x-accelerate-streaming",
    "x-accept-authent",
    "x-accept-proxy-authent",
    "x-broadcast-id",
    "x-burst-streaming",
    "x-notice",
    "x-player-lag-time",
    "x-playlist",
    "x-playlist-change-notice",
    "x-playlist-gen-id",
    "x-playlist-seek-id",
    "x-proxy-client-agent",
    "x-proxy-client-verb",
    "x-receding-playlistchange",
    "x-rtp-info",
    "x-server-ip-address",
    "x-sessioncookie",
    "x-startupprofile",
]
_RTSPHeaderFieldValueType: TypeAlias = RTSPHeaderField | _RTSPHeaderFieldLiteralType

class RTSPMsgType(GObject.GEnum):
    DATA = 5
    HTTP_REQUEST = 3
    HTTP_RESPONSE = 4
    INVALID = 0
    REQUEST = 1
    RESPONSE = 2

_RTSPMsgTypeLiteralType: TypeAlias = Literal[
    "GST_RTSP_MESSAGE_DATA",
    "GST_RTSP_MESSAGE_HTTP_REQUEST",
    "GST_RTSP_MESSAGE_HTTP_RESPONSE",
    "GST_RTSP_MESSAGE_INVALID",
    "GST_RTSP_MESSAGE_REQUEST",
    "GST_RTSP_MESSAGE_RESPONSE",
    "data",
    "http-request",
    "http-response",
    "invalid",
    "request",
    "response",
]
_RTSPMsgTypeValueType: TypeAlias = RTSPMsgType | _RTSPMsgTypeLiteralType

class RTSPRangeUnit(GObject.GEnum):
    CLOCK = 4
    NPT = 3
    SMPTE = 0
    SMPTE_25 = 2
    SMPTE_30_DROP = 1

_RTSPRangeUnitLiteralType: TypeAlias = Literal[
    "GST_RTSP_RANGE_CLOCK",
    "GST_RTSP_RANGE_NPT",
    "GST_RTSP_RANGE_SMPTE",
    "GST_RTSP_RANGE_SMPTE_25",
    "GST_RTSP_RANGE_SMPTE_30_DROP",
    "clock",
    "npt",
    "smpte",
    "smpte-25",
    "smpte-30-drop",
]
_RTSPRangeUnitValueType: TypeAlias = RTSPRangeUnit | _RTSPRangeUnitLiteralType

class RTSPResult(GObject.GEnum):
    EEOF = -11
    EINTR = -3
    EINVAL = -2
    ELAST = -17
    ENET = -12
    ENOMEM = -4
    ENOTIMPL = -6
    ENOTIP = -13
    EPARSE = -8
    ERESOLV = -5
    ERROR = -1
    ESYS = -7
    ETGET = -15
    ETIMEOUT = -14
    ETPOST = -16
    EWSASTART = -9
    EWSAVERSION = -10
    OK = 0
    OK_REDIRECT = 1

_RTSPResultLiteralType: TypeAlias = Literal[
    "GST_RTSP_EEOF",
    "GST_RTSP_EINTR",
    "GST_RTSP_EINVAL",
    "GST_RTSP_ELAST",
    "GST_RTSP_ENET",
    "GST_RTSP_ENOMEM",
    "GST_RTSP_ENOTIMPL",
    "GST_RTSP_ENOTIP",
    "GST_RTSP_EPARSE",
    "GST_RTSP_ERESOLV",
    "GST_RTSP_ERROR",
    "GST_RTSP_ESYS",
    "GST_RTSP_ETGET",
    "GST_RTSP_ETIMEOUT",
    "GST_RTSP_ETPOST",
    "GST_RTSP_EWSASTART",
    "GST_RTSP_EWSAVERSION",
    "GST_RTSP_OK",
    "GST_RTSP_OK_REDIRECT",
    "eeof",
    "eintr",
    "einval",
    "elast",
    "enet",
    "enomem",
    "enotimpl",
    "enotip",
    "eparse",
    "eresolv",
    "error",
    "esys",
    "etget",
    "etimeout",
    "etpost",
    "ewsastart",
    "ewsaversion",
    "ok",
    "ok-redirect",
]
_RTSPResultValueType: TypeAlias = RTSPResult | _RTSPResultLiteralType

class RTSPState(GObject.GEnum):
    INIT = 1
    INVALID = 0
    PLAYING = 4
    READY = 2
    RECORDING = 5
    SEEKING = 3

_RTSPStateLiteralType: TypeAlias = Literal[
    "GST_RTSP_STATE_INIT",
    "GST_RTSP_STATE_INVALID",
    "GST_RTSP_STATE_PLAYING",
    "GST_RTSP_STATE_READY",
    "GST_RTSP_STATE_RECORDING",
    "GST_RTSP_STATE_SEEKING",
    "init",
    "invalid",
    "playing",
    "ready",
    "recording",
    "seeking",
]
_RTSPStateValueType: TypeAlias = RTSPState | _RTSPStateLiteralType

class RTSPStatusCode(GObject.GEnum):
    AGGREGATE_OPERATION_NOT_ALLOWED = 459
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
    CONFERENCE_NOT_FOUND = 452
    CONTINUE = 100
    CREATED = 201
    DESTINATION_UNREACHABLE = 462
    FORBIDDEN = 403
    GATEWAY_TIMEOUT = 504
    GONE = 410
    HEADER_FIELD_NOT_VALID_FOR_RESOURCE = 456
    INTERNAL_SERVER_ERROR = 500
    INVALID = 0
    INVALID_RANGE = 457
    KEY_MANAGEMENT_FAILURE = 463
    LENGTH_REQUIRED = 411
    LOW_ON_STORAGE = 250
    METHOD_NOT_ALLOWED = 405
    METHOD_NOT_VALID_IN_THIS_STATE = 455
    MOVED_PERMANENTLY = 301
    MOVE_TEMPORARILY = 302
    MULTIPLE_CHOICES = 300
    NOT_ACCEPTABLE = 406
    NOT_ENOUGH_BANDWIDTH = 453
    NOT_FOUND = 404
    NOT_IMPLEMENTED = 501
    NOT_MODIFIED = 304
    OK = 200
    ONLY_AGGREGATE_OPERATION_ALLOWED = 460
    OPTION_NOT_SUPPORTED = 551
    PARAMETER_IS_READONLY = 458
    PARAMETER_NOT_UNDERSTOOD = 451
    PAYMENT_REQUIRED = 402
    PRECONDITION_FAILED = 412
    PROXY_AUTH_REQUIRED = 407
    REDIRECT_PERMANENTLY = 308
    REDIRECT_TEMPORARILY = 307
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_TIMEOUT = 408
    REQUEST_URI_TOO_LARGE = 414
    RTSP_VERSION_NOT_SUPPORTED = 505
    SEE_OTHER = 303
    SERVICE_UNAVAILABLE = 503
    SESSION_NOT_FOUND = 454
    UNAUTHORIZED = 401
    UNSUPPORTED_MEDIA_TYPE = 415
    UNSUPPORTED_TRANSPORT = 461
    USE_PROXY = 305

_RTSPStatusCodeLiteralType: TypeAlias = Literal[
    "GST_RTSP_STS_AGGREGATE_OPERATION_NOT_ALLOWED",
    "GST_RTSP_STS_BAD_GATEWAY",
    "GST_RTSP_STS_BAD_REQUEST",
    "GST_RTSP_STS_CONFERENCE_NOT_FOUND",
    "GST_RTSP_STS_CONTINUE",
    "GST_RTSP_STS_CREATED",
    "GST_RTSP_STS_DESTINATION_UNREACHABLE",
    "GST_RTSP_STS_FORBIDDEN",
    "GST_RTSP_STS_GATEWAY_TIMEOUT",
    "GST_RTSP_STS_GONE",
    "GST_RTSP_STS_HEADER_FIELD_NOT_VALID_FOR_RESOURCE",
    "GST_RTSP_STS_INTERNAL_SERVER_ERROR",
    "GST_RTSP_STS_INVALID",
    "GST_RTSP_STS_INVALID_RANGE",
    "GST_RTSP_STS_KEY_MANAGEMENT_FAILURE",
    "GST_RTSP_STS_LENGTH_REQUIRED",
    "GST_RTSP_STS_LOW_ON_STORAGE",
    "GST_RTSP_STS_METHOD_NOT_ALLOWED",
    "GST_RTSP_STS_METHOD_NOT_VALID_IN_THIS_STATE",
    "GST_RTSP_STS_MOVED_PERMANENTLY",
    "GST_RTSP_STS_MOVE_TEMPORARILY",
    "GST_RTSP_STS_MULTIPLE_CHOICES",
    "GST_RTSP_STS_NOT_ACCEPTABLE",
    "GST_RTSP_STS_NOT_ENOUGH_BANDWIDTH",
    "GST_RTSP_STS_NOT_FOUND",
    "GST_RTSP_STS_NOT_IMPLEMENTED",
    "GST_RTSP_STS_NOT_MODIFIED",
    "GST_RTSP_STS_OK",
    "GST_RTSP_STS_ONLY_AGGREGATE_OPERATION_ALLOWED",
    "GST_RTSP_STS_OPTION_NOT_SUPPORTED",
    "GST_RTSP_STS_PARAMETER_IS_READONLY",
    "GST_RTSP_STS_PARAMETER_NOT_UNDERSTOOD",
    "GST_RTSP_STS_PAYMENT_REQUIRED",
    "GST_RTSP_STS_PRECONDITION_FAILED",
    "GST_RTSP_STS_PROXY_AUTH_REQUIRED",
    "GST_RTSP_STS_REDIRECT_PERMANENTLY",
    "GST_RTSP_STS_REDIRECT_TEMPORARILY",
    "GST_RTSP_STS_REQUEST_ENTITY_TOO_LARGE",
    "GST_RTSP_STS_REQUEST_TIMEOUT",
    "GST_RTSP_STS_REQUEST_URI_TOO_LARGE",
    "GST_RTSP_STS_RTSP_VERSION_NOT_SUPPORTED",
    "GST_RTSP_STS_SEE_OTHER",
    "GST_RTSP_STS_SERVICE_UNAVAILABLE",
    "GST_RTSP_STS_SESSION_NOT_FOUND",
    "GST_RTSP_STS_UNAUTHORIZED",
    "GST_RTSP_STS_UNSUPPORTED_MEDIA_TYPE",
    "GST_RTSP_STS_UNSUPPORTED_TRANSPORT",
    "GST_RTSP_STS_USE_PROXY",
    "aggregate-operation-not-allowed",
    "bad-gateway",
    "bad-request",
    "conference-not-found",
    "continue",
    "created",
    "destination-unreachable",
    "forbidden",
    "gateway-timeout",
    "gone",
    "header-field-not-valid-for-resource",
    "internal-server-error",
    "invalid",
    "invalid-range",
    "key-management-failure",
    "length-required",
    "low-on-storage",
    "method-not-allowed",
    "method-not-valid-in-this-state",
    "move-temporarily",
    "moved-permanently",
    "multiple-choices",
    "not-acceptable",
    "not-enough-bandwidth",
    "not-found",
    "not-implemented",
    "not-modified",
    "ok",
    "only-aggregate-operation-allowed",
    "option-not-supported",
    "parameter-is-readonly",
    "parameter-not-understood",
    "payment-required",
    "precondition-failed",
    "proxy-auth-required",
    "redirect-permanently",
    "redirect-temporarily",
    "request-entity-too-large",
    "request-timeout",
    "request-uri-too-large",
    "rtsp-version-not-supported",
    "see-other",
    "service-unavailable",
    "session-not-found",
    "unauthorized",
    "unsupported-media-type",
    "unsupported-transport",
    "use-proxy",
]
_RTSPStatusCodeValueType: TypeAlias = RTSPStatusCode | _RTSPStatusCodeLiteralType

class RTSPTimeType(GObject.GEnum):
    END = 2
    FRAMES = 3
    NOW = 1
    SECONDS = 0
    UTC = 4

_RTSPTimeTypeLiteralType: TypeAlias = Literal[
    "GST_RTSP_TIME_END",
    "GST_RTSP_TIME_FRAMES",
    "GST_RTSP_TIME_NOW",
    "GST_RTSP_TIME_SECONDS",
    "GST_RTSP_TIME_UTC",
    "end",
    "frames",
    "now",
    "seconds",
    "utc",
]
_RTSPTimeTypeValueType: TypeAlias = RTSPTimeType | _RTSPTimeTypeLiteralType

class RTSPVersion(GObject.GEnum):
    INVALID = 0
    @staticmethod
    def as_text(version: _RTSPVersionValueType) -> str: ...

_RTSPVersionLiteralType: TypeAlias = Literal["GST_RTSP_VERSION_INVALID", "invalid"]
_RTSPVersionValueType: TypeAlias = RTSPVersion | _RTSPVersionLiteralType
