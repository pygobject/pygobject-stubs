from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TypeVar

try:
    from warnings import deprecated
except ImportError:
    from typing_extensions import deprecated

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

ADDRESS_ANY_PORT: int = 0
ADDRESS_FAMILY: str = "family"
ADDRESS_NAME: str = "name"
ADDRESS_PHYSICAL: str = "physical"
ADDRESS_PORT: str = "port"
ADDRESS_PROTOCOL: str = "protocol"
ADDRESS_SOCKADDR: str = "sockaddr"
AUTH_DOMAIN_ADD_PATH: str = "add-path"
AUTH_DOMAIN_BASIC_AUTH_CALLBACK: str = "auth-callback"
AUTH_DOMAIN_BASIC_AUTH_DATA: str = "auth-data"
AUTH_DOMAIN_DIGEST_AUTH_CALLBACK: str = "auth-callback"
AUTH_DOMAIN_DIGEST_AUTH_DATA: str = "auth-data"
AUTH_DOMAIN_FILTER: str = "filter"
AUTH_DOMAIN_FILTER_DATA: str = "filter-data"
AUTH_DOMAIN_GENERIC_AUTH_CALLBACK: str = "generic-auth-callback"
AUTH_DOMAIN_GENERIC_AUTH_DATA: str = "generic-auth-data"
AUTH_DOMAIN_PROXY: str = "proxy"
AUTH_DOMAIN_REALM: str = "realm"
AUTH_DOMAIN_REMOVE_PATH: str = "remove-path"
AUTH_HOST: str = "host"
AUTH_IS_AUTHENTICATED: str = "is-authenticated"
AUTH_IS_FOR_PROXY: str = "is-for-proxy"
AUTH_REALM: str = "realm"
AUTH_SCHEME_NAME: str = "scheme-name"
CHAR_HTTP_CTL: int = 16
CHAR_HTTP_SEPARATOR: int = 8
CHAR_URI_GEN_DELIMS: int = 2
CHAR_URI_PERCENT_ENCODED: int = 1
CHAR_URI_SUB_DELIMS: int = 4
COOKIE_JAR_ACCEPT_POLICY: str = "accept-policy"
COOKIE_JAR_DB_FILENAME: str = "filename"
COOKIE_JAR_READ_ONLY: str = "read-only"
COOKIE_JAR_TEXT_FILENAME: str = "filename"
COOKIE_MAX_AGE_ONE_DAY: int = 0
COOKIE_MAX_AGE_ONE_HOUR: int = 3600
COOKIE_MAX_AGE_ONE_WEEK: int = 0
COOKIE_MAX_AGE_ONE_YEAR: int = 0
FORM_MIME_TYPE_MULTIPART: str = "multipart/form-data"
FORM_MIME_TYPE_URLENCODED: str = "application/x-www-form-urlencoded"
HSTS_ENFORCER_DB_FILENAME: str = "filename"
HSTS_POLICY_MAX_AGE_PAST: int = 0
LOGGER_LEVEL: str = "level"
LOGGER_MAX_BODY_SIZE: str = "max-body-size"
MAJOR_VERSION: int = 2
MESSAGE_FIRST_PARTY: str = "first-party"
MESSAGE_FLAGS: str = "flags"
MESSAGE_HTTP_VERSION: str = "http-version"
MESSAGE_IS_TOP_LEVEL_NAVIGATION: str = "is-top-level-navigation"
MESSAGE_METHOD: str = "method"
MESSAGE_PRIORITY: str = "priority"
MESSAGE_REASON_PHRASE: str = "reason-phrase"
MESSAGE_REQUEST_BODY: str = "request-body"
MESSAGE_REQUEST_BODY_DATA: str = "request-body-data"
MESSAGE_REQUEST_HEADERS: str = "request-headers"
MESSAGE_RESPONSE_BODY: str = "response-body"
MESSAGE_RESPONSE_BODY_DATA: str = "response-body-data"
MESSAGE_RESPONSE_HEADERS: str = "response-headers"
MESSAGE_SERVER_SIDE: str = "server-side"
MESSAGE_SITE_FOR_COOKIES: str = "site-for-cookies"
MESSAGE_STATUS_CODE: str = "status-code"
MESSAGE_TLS_CERTIFICATE: str = "tls-certificate"
MESSAGE_TLS_ERRORS: str = "tls-errors"
MESSAGE_URI: str = "uri"
MICRO_VERSION: int = 3
MINOR_VERSION: int = 74
REQUEST_SESSION: str = "session"
REQUEST_URI: str = "uri"
SERVER_ASYNC_CONTEXT: str = "async-context"
SERVER_HTTPS_ALIASES: str = "https-aliases"
SERVER_HTTP_ALIASES: str = "http-aliases"
SERVER_INTERFACE: str = "interface"
SERVER_PORT: str = "port"
SERVER_RAW_PATHS: str = "raw-paths"
SERVER_SERVER_HEADER: str = "server-header"
SERVER_SSL_CERT_FILE: str = "ssl-cert-file"
SERVER_SSL_KEY_FILE: str = "ssl-key-file"
SERVER_TLS_CERTIFICATE: str = "tls-certificate"
SESSION_ACCEPT_LANGUAGE: str = "accept-language"
SESSION_ACCEPT_LANGUAGE_AUTO: str = "accept-language-auto"
SESSION_ASYNC_CONTEXT: str = "async-context"
SESSION_HTTPS_ALIASES: str = "https-aliases"
SESSION_HTTP_ALIASES: str = "http-aliases"
SESSION_IDLE_TIMEOUT: str = "idle-timeout"
SESSION_LOCAL_ADDRESS: str = "local-address"
SESSION_MAX_CONNS: str = "max-conns"
SESSION_MAX_CONNS_PER_HOST: str = "max-conns-per-host"
SESSION_PROXY_RESOLVER: str = "proxy-resolver"
SESSION_PROXY_URI: str = "proxy-uri"
SESSION_SSL_CA_FILE: str = "ssl-ca-file"
SESSION_SSL_STRICT: str = "ssl-strict"
SESSION_SSL_USE_SYSTEM_CA_FILE: str = "ssl-use-system-ca-file"
SESSION_TIMEOUT: str = "timeout"
SESSION_TLS_DATABASE: str = "tls-database"
SESSION_TLS_INTERACTION: str = "tls-interaction"
SESSION_USER_AGENT: str = "user-agent"
SESSION_USE_NTLM: str = "use-ntlm"
SESSION_USE_THREAD_CONTEXT: str = "use-thread-context"
SOCKET_ASYNC_CONTEXT: str = "async-context"
SOCKET_FLAG_NONBLOCKING: str = "non-blocking"
SOCKET_IS_SERVER: str = "is-server"
SOCKET_LOCAL_ADDRESS: str = "local-address"
SOCKET_REMOTE_ADDRESS: str = "remote-address"
SOCKET_SSL_CREDENTIALS: str = "ssl-creds"
SOCKET_SSL_FALLBACK: str = "ssl-fallback"
SOCKET_SSL_STRICT: str = "ssl-strict"
SOCKET_TIMEOUT: str = "timeout"
SOCKET_TLS_CERTIFICATE: str = "tls-certificate"
SOCKET_TLS_ERRORS: str = "tls-errors"
SOCKET_TRUSTED_CERTIFICATE: str = "trusted-certificate"
SOCKET_USE_THREAD_CONTEXT: str = "use-thread-context"
VERSION_MIN_REQUIRED: int = 2
_lock = ...  # FIXME Constant
_namespace: str = "Soup"
_version: str = "2.4"

def check_version(major: int, minor: int, micro: int) -> bool: ...
def cookie_parse(header: str, origin: URI) -> Optional[Cookie]: ...
def cookies_from_request(msg: Message) -> list[Cookie]: ...
def cookies_from_response(msg: Message) -> list[Cookie]: ...
def cookies_to_cookie_header(cookies: list[Cookie]) -> str: ...
def cookies_to_request(cookies: list[Cookie], msg: Message) -> None: ...
def cookies_to_response(cookies: list[Cookie], msg: Message) -> None: ...
def form_decode(encoded_form: str) -> dict[str, str]: ...
def form_decode_multipart(
    msg: Message, file_control_name: Optional[str] = None
) -> Tuple[Optional[dict[str, str]], str, str, Buffer]: ...
def form_encode_datalist(form_data_set: GLib.Data) -> str: ...
def form_encode_hash(form_data_set: dict[str, str]) -> str: ...
def form_request_new_from_datalist(
    method: str, uri: str, form_data_set: GLib.Data
) -> Message: ...
def form_request_new_from_hash(
    method: str, uri: str, form_data_set: dict[str, str]
) -> Message: ...
def form_request_new_from_multipart(uri: str, multipart: Multipart) -> Message: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def get_resource() -> Gio.Resource: ...
def header_contains(header: str, token: str) -> bool: ...
def header_free_param_list(param_list: dict[str, str]) -> None: ...
def header_g_string_append_param(
    string: GLib.String, name: str, value: str
) -> None: ...
def header_g_string_append_param_quoted(
    string: GLib.String, name: str, value: str
) -> None: ...
def header_parse_list(header: str) -> list[str]: ...
def header_parse_param_list(header: str) -> dict[str, str]: ...
def header_parse_param_list_strict(header: str) -> Optional[dict[str, str]]: ...
def header_parse_quality_list(header: str) -> Tuple[list[str], list[str]]: ...
def header_parse_semi_param_list(header: str) -> dict[str, str]: ...
def header_parse_semi_param_list_strict(header: str) -> Optional[dict[str, str]]: ...
def headers_parse(str: str, len: int, dest: MessageHeaders) -> bool: ...
def headers_parse_request(
    str: str, len: int, req_headers: MessageHeaders
) -> Tuple[int, str, str, HTTPVersion]: ...
def headers_parse_response(
    str: str, len: int, headers: MessageHeaders
) -> Tuple[bool, HTTPVersion, int, str]: ...
def headers_parse_status_line(
    status_line: str,
) -> Tuple[bool, HTTPVersion, int, str]: ...
def http_error_quark() -> int: ...
def message_headers_iter_init(hdrs: MessageHeaders) -> MessageHeadersIter: ...
def request_error_quark() -> int: ...
def requester_error_quark() -> int: ...
def status_get_phrase(status_code: int) -> str: ...
def status_proxify(status_code: int) -> int: ...
def str_case_equal(v1: None, v2: None) -> bool: ...
def str_case_hash(key: None) -> int: ...
def tld_domain_is_public_suffix(domain: str) -> bool: ...
def tld_error_quark() -> int: ...
def tld_get_base_domain(hostname: str) -> str: ...
def uri_decode(part: str) -> str: ...
def uri_encode(part: str, escape_extra: Optional[str] = None) -> str: ...
def uri_normalize(part: str, unescape_extra: Optional[str] = None) -> str: ...
@deprecated("Use #GVariant API instead.")
def value_array_new() -> GObject.ValueArray: ...
@deprecated("Use #GVariant API instead.")
def value_hash_insert_value(hash: dict[str, Any], key: str, value: Any) -> None: ...
@deprecated("Use #GVariant API instead.")
def value_hash_new() -> dict[str, Any]: ...
def websocket_client_prepare_handshake(
    msg: Message,
    origin: Optional[str] = None,
    protocols: Optional[Sequence[str]] = None,
) -> None: ...
def websocket_client_prepare_handshake_with_extensions(
    msg: Message,
    origin: Optional[str] = None,
    protocols: Optional[Sequence[str]] = None,
    supported_extensions: Optional[Sequence[GObject.TypeClass]] = None,
) -> None: ...
def websocket_client_verify_handshake(msg: Message) -> bool: ...
def websocket_client_verify_handshake_with_extensions(
    msg: Message, supported_extensions: Optional[Sequence[GObject.TypeClass]] = None
) -> Tuple[bool, list[WebsocketExtension]]: ...
def websocket_error_get_quark() -> int: ...
def websocket_server_check_handshake(
    msg: Message,
    origin: Optional[str] = None,
    protocols: Optional[Sequence[str]] = None,
) -> bool: ...
def websocket_server_check_handshake_with_extensions(
    msg: Message,
    origin: Optional[str] = None,
    protocols: Optional[Sequence[str]] = None,
    supported_extensions: Optional[Sequence[GObject.TypeClass]] = None,
) -> bool: ...
def websocket_server_process_handshake(
    msg: Message,
    expected_origin: Optional[str] = None,
    protocols: Optional[Sequence[str]] = None,
) -> bool: ...
def websocket_server_process_handshake_with_extensions(
    msg: Message,
    expected_origin: Optional[str] = None,
    protocols: Optional[Sequence[str]] = None,
    supported_extensions: Optional[Sequence[GObject.TypeClass]] = None,
) -> Tuple[bool, list[WebsocketExtension]]: ...
@deprecated("Use soup_xmlrpc_build_request() instead.")
def xmlrpc_build_method_call(
    method_name: str, params: Sequence[Any]
) -> Optional[str]: ...
@deprecated("Use soup_xmlrpc_build_response() instead.")
def xmlrpc_build_method_response(value: Any) -> Optional[str]: ...
def xmlrpc_build_request(method_name: str, params: GLib.Variant) -> str: ...
def xmlrpc_build_response(value: GLib.Variant) -> str: ...
def xmlrpc_error_quark() -> int: ...
def xmlrpc_fault_quark() -> int: ...
def xmlrpc_message_new(uri: str, method_name: str, params: GLib.Variant) -> Message: ...
def xmlrpc_message_set_response(msg: Message, value: GLib.Variant) -> bool: ...
@deprecated("Use soup_xmlrpc_parse_request_full() instead.")
def xmlrpc_parse_method_call(
    method_call: str, length: int
) -> Tuple[bool, str, GObject.ValueArray]: ...
@deprecated("Use soup_xmlrpc_parse_response() instead.")
def xmlrpc_parse_method_response(
    method_response: str, length: int
) -> Tuple[bool, Any]: ...
def xmlrpc_parse_request(method_call: str, length: int) -> Tuple[str, XMLRPCParams]: ...
def xmlrpc_parse_response(
    method_response: str, length: int, signature: Optional[str] = None
) -> GLib.Variant: ...
def xmlrpc_variant_get_datetime(variant: GLib.Variant) -> Date: ...
def xmlrpc_variant_new_datetime(date: Date) -> GLib.Variant: ...

class Address(GObject.Object, Gio.SocketConnectable):
    """
    :Constructors:

    ::

        Address(**properties)
        new(name:str, port:int) -> Soup.Address
        new_any(family:Soup.AddressFamily, port:int) -> Soup.Address or None
        new_from_sockaddr(sa=None, len:int) -> Soup.Address or None

    Object SoupAddress

    Properties from SoupAddress:
      name -> gchararray: Name
        Hostname for this address
      family -> SoupAddressFamily: Family
        Address family for this address
      port -> gint: Port
        Port for this address
      protocol -> gchararray: Protocol
        URI scheme for this address
      physical -> gchararray: Physical address
        IP address for this address
      sockaddr -> gpointer: sockaddr
        struct sockaddr for this address

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        family: AddressFamily
        name: Optional[str]
        physical: Optional[str]
        port: int
        protocol: str
        sockaddr: Optional[None]
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        family: AddressFamily = ...,
        name: str = ...,
        port: int = ...,
        protocol: str = ...,
        sockaddr: None = ...,
    ): ...
    def equal_by_ip(self, addr2: Address) -> bool: ...
    def equal_by_name(self, addr2: Address) -> bool: ...
    def get_gsockaddr(self) -> Gio.SocketAddress: ...
    def get_name(self) -> Optional[str]: ...
    def get_physical(self) -> Optional[str]: ...
    def get_port(self) -> int: ...
    def get_sockaddr(self) -> int: ...
    def hash_by_ip(self) -> int: ...
    def hash_by_name(self) -> int: ...
    def is_resolved(self) -> bool: ...
    @classmethod
    def new(cls, name: str, port: int) -> Address: ...
    @classmethod
    def new_any(cls, family: AddressFamily, port: int) -> Optional[Address]: ...
    @classmethod
    def new_from_sockaddr(cls, sa: None, len: int) -> Optional[Address]: ...
    def resolve_async(
        self,
        async_context: Optional[GLib.MainContext],
        cancellable: Optional[Gio.Cancellable],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    def resolve_sync(self, cancellable: Optional[Gio.Cancellable] = None) -> int: ...

class AddressClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AddressClass()
    """

    parent_class: GObject.ObjectClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class Auth(GObject.Object):
    """
    :Constructors:

    ::

        Auth(**properties)
        new(type:GType, msg:Soup.Message, auth_header:str) -> Soup.Auth or None

    Object SoupAuth

    Properties from SoupAuth:
      scheme-name -> gchararray: Scheme name
        Authentication scheme name
      realm -> gchararray: Realm
        Authentication realm
      host -> gchararray: Host
        Authentication host
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        host: str
        is_authenticated: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str
    props: Props = ...
    parent: GObject.Object = ...
    realm: str = ...
    def __init__(self, host: str = ..., is_for_proxy: bool = ..., realm: str = ...): ...
    def authenticate(self, username: str, password: str) -> None: ...
    def can_authenticate(self) -> bool: ...
    def do_authenticate(self, username: str, password: str) -> None: ...
    def do_can_authenticate(self) -> bool: ...
    def do_get_authorization(self, msg: Message) -> str: ...
    def do_get_protection_space(self, source_uri: URI) -> list[str]: ...
    def do_is_authenticated(self) -> bool: ...
    def do_is_ready(self, msg: Message) -> bool: ...
    def do_update(self, msg: Message, auth_header: dict[None, None]) -> bool: ...
    def get_authorization(self, msg: Message) -> str: ...
    def get_host(self) -> str: ...
    def get_info(self) -> str: ...
    def get_protection_space(self, source_uri: URI) -> list[str]: ...
    def get_realm(self) -> str: ...
    def get_saved_password(self, user: str) -> str: ...
    def get_saved_users(self) -> list[str]: ...
    def get_scheme_name(self) -> str: ...
    def has_saved_password(self, username: str, password: str) -> None: ...
    def is_authenticated(self) -> bool: ...
    def is_for_proxy(self) -> bool: ...
    def is_ready(self, msg: Message) -> bool: ...
    @classmethod
    def new(cls, type: Type, msg: Message, auth_header: str) -> Optional[Auth]: ...
    def save_password(self, username: str, password: str) -> None: ...
    def update(self, msg: Message, auth_header: str) -> bool: ...

class AuthBasic(Auth):
    """
    :Constructors:

    ::

        AuthBasic(**properties)

    Object SoupAuthBasic

    Properties from SoupAuth:
      scheme-name -> gchararray: Scheme name
        Authentication scheme name
      realm -> gchararray: Realm
        Authentication realm
      host -> gchararray: Host
        Authentication host
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        host: str
        is_authenticated: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str
    props: Props = ...
    def __init__(self, host: str = ..., is_for_proxy: bool = ..., realm: str = ...): ...

class AuthClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthClass()
    """

    parent_class: GObject.ObjectClass = ...
    scheme_name: str = ...
    strength: int = ...
    update: Callable[[Auth, Message, dict[None, None]], bool] = ...
    get_protection_space: Callable[[Auth, URI], list[str]] = ...
    authenticate: Callable[[Auth, str, str], None] = ...
    is_authenticated: Callable[[Auth], bool] = ...
    get_authorization: Callable[[Auth, Message], str] = ...
    is_ready: Callable[[Auth, Message], bool] = ...
    can_authenticate: Callable[[Auth], bool] = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class AuthDigest(Auth):
    """
    :Constructors:

    ::

        AuthDigest(**properties)

    Object SoupAuthDigest

    Properties from SoupAuth:
      scheme-name -> gchararray: Scheme name
        Authentication scheme name
      realm -> gchararray: Realm
        Authentication realm
      host -> gchararray: Host
        Authentication host
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        host: str
        is_authenticated: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str
    props: Props = ...
    def __init__(self, host: str = ..., is_for_proxy: bool = ..., realm: str = ...): ...

class AuthDomain(GObject.Object):
    """
    :Constructors:

    ::

        AuthDomain(**properties)

    Object SoupAuthDomain

    Properties from SoupAuthDomain:
      realm -> gchararray: Realm
        The realm of this auth domain
      proxy -> gboolean: Proxy
        Whether or not this is a proxy auth domain
      add-path -> gchararray: Add a path
        Add a path covered by this auth domain
      remove-path -> gchararray: Remove a path
        Remove a path covered by this auth domain
      filter -> gpointer: Filter
        A filter for deciding whether or not to require authentication
      filter-data -> gpointer: Filter data
        Data to pass to filter
      generic-auth-callback -> gpointer: Generic authentication callback
        An authentication callback that can be used with any SoupAuthDomain subclass
      generic-auth-data -> gpointer: Authentication callback data
        Data to pass to auth callback

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filter: AuthDomainFilter
        filter_data: None
        generic_auth_callback: AuthDomainGenericAuthCallback
        generic_auth_data: None
        proxy: bool
        realm: str
        add_path: str
        remove_path: str
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        add_path: str = ...,
        filter: AuthDomainFilter = ...,
        filter_data: None = ...,
        generic_auth_callback: AuthDomainGenericAuthCallback = ...,
        generic_auth_data: None = ...,
        proxy: bool = ...,
        realm: str = ...,
        remove_path: str = ...,
    ): ...
    def accepts(self, msg: Message) -> Optional[str]: ...
    def add_path(self, path: str) -> None: ...
    def challenge(self, msg: Message) -> None: ...
    def check_password(self, msg: Message, username: str, password: str) -> bool: ...
    def covers(self, msg: Message) -> bool: ...
    def do_accepts(self, msg: Message, header: str) -> str: ...
    def do_challenge(self, msg: Message) -> str: ...
    def do_check_password(self, msg: Message, username: str, password: str) -> bool: ...
    def get_realm(self) -> str: ...
    def remove_path(self, path: str) -> None: ...
    def set_filter(self, filter: Callable[..., bool], *filter_data: Any) -> None: ...
    def set_generic_auth_callback(
        self, auth_callback: Callable[..., bool], *auth_data: Any
    ) -> None: ...
    def try_generic_auth_callback(self, msg: Message, username: str) -> bool: ...

class AuthDomainBasic(AuthDomain):
    """
    :Constructors:

    ::

        AuthDomainBasic(**properties)

    Object SoupAuthDomainBasic

    Properties from SoupAuthDomainBasic:
      auth-callback -> gpointer: Authentication callback
        Password-checking callback
      auth-data -> gpointer: Authentication callback data
        Data to pass to authentication callback

    Properties from SoupAuthDomain:
      realm -> gchararray: Realm
        The realm of this auth domain
      proxy -> gboolean: Proxy
        Whether or not this is a proxy auth domain
      add-path -> gchararray: Add a path
        Add a path covered by this auth domain
      remove-path -> gchararray: Remove a path
        Remove a path covered by this auth domain
      filter -> gpointer: Filter
        A filter for deciding whether or not to require authentication
      filter-data -> gpointer: Filter data
        Data to pass to filter
      generic-auth-callback -> gpointer: Generic authentication callback
        An authentication callback that can be used with any SoupAuthDomain subclass
      generic-auth-data -> gpointer: Authentication callback data
        Data to pass to auth callback

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        auth_callback: AuthDomainBasicAuthCallback
        auth_data: None
        filter: AuthDomainFilter
        filter_data: None
        generic_auth_callback: AuthDomainGenericAuthCallback
        generic_auth_data: None
        proxy: bool
        realm: str
        add_path: str
        remove_path: str
    props: Props = ...
    parent: AuthDomain = ...
    def __init__(
        self,
        auth_callback: AuthDomainBasicAuthCallback = ...,
        auth_data: None = ...,
        add_path: str = ...,
        filter: AuthDomainFilter = ...,
        filter_data: None = ...,
        generic_auth_callback: AuthDomainGenericAuthCallback = ...,
        generic_auth_data: None = ...,
        proxy: bool = ...,
        realm: str = ...,
        remove_path: str = ...,
    ): ...
    def set_auth_callback(
        self, callback: Callable[..., bool], *user_data: Any
    ) -> None: ...

class AuthDomainBasicClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthDomainBasicClass()
    """

    parent_class: AuthDomainClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class AuthDomainClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthDomainClass()
    """

    parent_class: GObject.ObjectClass = ...
    accepts: Callable[[AuthDomain, Message, str], str] = ...
    challenge: Callable[[AuthDomain, Message], str] = ...
    check_password: Callable[[AuthDomain, Message, str, str], bool] = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class AuthDomainDigest(AuthDomain):
    """
    :Constructors:

    ::

        AuthDomainDigest(**properties)

    Object SoupAuthDomainDigest

    Properties from SoupAuthDomainDigest:
      auth-callback -> gpointer: Authentication callback
        Password-finding callback
      auth-data -> gpointer: Authentication callback data
        Data to pass to authentication callback

    Properties from SoupAuthDomain:
      realm -> gchararray: Realm
        The realm of this auth domain
      proxy -> gboolean: Proxy
        Whether or not this is a proxy auth domain
      add-path -> gchararray: Add a path
        Add a path covered by this auth domain
      remove-path -> gchararray: Remove a path
        Remove a path covered by this auth domain
      filter -> gpointer: Filter
        A filter for deciding whether or not to require authentication
      filter-data -> gpointer: Filter data
        Data to pass to filter
      generic-auth-callback -> gpointer: Generic authentication callback
        An authentication callback that can be used with any SoupAuthDomain subclass
      generic-auth-data -> gpointer: Authentication callback data
        Data to pass to auth callback

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        auth_callback: AuthDomainDigestAuthCallback
        auth_data: None
        filter: AuthDomainFilter
        filter_data: None
        generic_auth_callback: AuthDomainGenericAuthCallback
        generic_auth_data: None
        proxy: bool
        realm: str
        add_path: str
        remove_path: str
    props: Props = ...
    parent: AuthDomain = ...
    def __init__(
        self,
        auth_callback: AuthDomainDigestAuthCallback = ...,
        auth_data: None = ...,
        add_path: str = ...,
        filter: AuthDomainFilter = ...,
        filter_data: None = ...,
        generic_auth_callback: AuthDomainGenericAuthCallback = ...,
        generic_auth_data: None = ...,
        proxy: bool = ...,
        realm: str = ...,
        remove_path: str = ...,
    ): ...
    @staticmethod
    def encode_password(username: str, realm: str, password: str) -> str: ...
    def set_auth_callback(
        self, callback: Callable[..., Optional[str]], *user_data: Any
    ) -> None: ...

class AuthDomainDigestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthDomainDigestClass()
    """

    parent_class: AuthDomainClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class AuthManager(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        AuthManager(**properties)

    Object SoupAuthManager

    Signals from SoupAuthManager:
      authenticate (SoupMessage, SoupAuth, gboolean)

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: AuthManagerPrivate = ...
    def clear_cached_credentials(self) -> None: ...
    def do_authenticate(self, msg: Message, auth: Auth, retrying: bool) -> None: ...
    def use_auth(self, uri: URI, auth: Auth) -> None: ...

class AuthManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthManagerClass()
    """

    parent_class: GObject.ObjectClass = ...
    authenticate: Callable[[AuthManager, Message, Auth, bool], None] = ...

class AuthManagerPrivate(GObject.GPointer): ...

class AuthNTLM(Auth):
    """
    :Constructors:

    ::

        AuthNTLM(**properties)

    Object SoupAuthNTLM

    Properties from SoupAuth:
      scheme-name -> gchararray: Scheme name
        Authentication scheme name
      realm -> gchararray: Realm
        Authentication realm
      host -> gchararray: Host
        Authentication host
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        host: str
        is_authenticated: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str
    props: Props = ...
    def __init__(self, host: str = ..., is_for_proxy: bool = ..., realm: str = ...): ...

class AuthNegotiate(Auth):
    """
    :Constructors:

    ::

        AuthNegotiate(**properties)

    Object SoupAuthNegotiate

    Properties from SoupAuth:
      scheme-name -> gchararray: Scheme name
        Authentication scheme name
      realm -> gchararray: Realm
        Authentication realm
      host -> gchararray: Host
        Authentication host
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        host: str
        is_authenticated: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str
    props: Props = ...
    def __init__(self, host: str = ..., is_for_proxy: bool = ..., realm: str = ...): ...
    @staticmethod
    def supported() -> bool: ...

class Buffer(GObject.GBoxed):
    """
    :Constructors:

    ::

        Buffer()
        new(data:list) -> Soup.Buffer
        new_with_owner(data:list, owner=None, owner_dnotify:GLib.DestroyNotify=None) -> Soup.Buffer
    """

    data: None = ...
    length: int = ...
    def copy(self) -> Buffer: ...
    def free(self) -> None: ...
    def get_as_bytes(self) -> GLib.Bytes: ...
    def get_data(self) -> bytes: ...
    def get_owner(self) -> None: ...
    @classmethod
    def new(cls, data: Sequence[int]) -> Buffer: ...
    def new_subbuffer(self, offset: int, length: int) -> Buffer: ...
    @classmethod
    def new_with_owner(
        cls,
        data: Sequence[int],
        owner: None,
        owner_dnotify: Optional[Callable[[None], None]] = None,
    ) -> Buffer: ...

class ByteArray(GObject.GBoxed): ...

class Cache(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        Cache(**properties)
        new(cache_dir:str=None, cache_type:Soup.CacheType) -> Soup.Cache

    Object SoupCache

    Properties from SoupCache:
      cache-dir -> gchararray: Cache directory
        The directory to store the cache files
      cache-type -> SoupCacheType: Cache type
        Whether the cache is private or shared

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        cache_dir: str
        cache_type: CacheType
    props: Props = ...
    parent_instance: GObject.Object = ...
    priv: CachePrivate = ...
    def __init__(self, cache_dir: str = ..., cache_type: CacheType = ...): ...
    def clear(self) -> None: ...
    def do_get_cacheability(self, msg: Message) -> Cacheability: ...
    def dump(self) -> None: ...
    def flush(self) -> None: ...
    def get_max_size(self) -> int: ...
    def load(self) -> None: ...
    @classmethod
    def new(cls, cache_dir: Optional[str], cache_type: CacheType) -> Cache: ...
    def set_max_size(self, max_size: int) -> None: ...

class CacheClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CacheClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_cacheability: Callable[[Cache, Message], Cacheability] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...

class CachePrivate(GObject.GPointer): ...

class ClientContext(GObject.GBoxed):
    @deprecated(
        "Use soup_client_context_get_remote_address(), which returns a #GSocketAddress."
    )
    def get_address(self) -> Optional[Address]: ...
    def get_auth_domain(self) -> Optional[AuthDomain]: ...
    def get_auth_user(self) -> Optional[str]: ...
    def get_gsocket(self) -> Optional[Gio.Socket]: ...
    def get_host(self) -> Optional[str]: ...
    def get_local_address(self) -> Optional[Gio.SocketAddress]: ...
    def get_remote_address(self) -> Optional[Gio.SocketAddress]: ...
    @deprecated("use soup_client_context_get_gsocket(), which returns a #GSocket.")
    def get_socket(self) -> Socket: ...
    def steal_connection(self) -> Gio.IOStream: ...

class Connection(GObject.GPointer): ...

class ContentDecoder(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        ContentDecoder(**properties)

    Object SoupContentDecoder

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: ContentDecoderPrivate = ...

class ContentDecoderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentDecoderClass()
    """

    parent_class: GObject.ObjectClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...
    _libsoup_reserved5: None = ...

class ContentDecoderPrivate(GObject.GPointer): ...

class ContentSniffer(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        ContentSniffer(**properties)
        new() -> Soup.ContentSniffer

    Object SoupContentSniffer

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: ContentSnifferPrivate = ...
    def do_get_buffer_size(self) -> int: ...
    def do_sniff(self, msg: Message, buffer: Buffer) -> Tuple[str, dict[str, str]]: ...
    def get_buffer_size(self) -> int: ...
    @classmethod
    def new(cls) -> ContentSniffer: ...
    def sniff(self, msg: Message, buffer: Buffer) -> Tuple[str, dict[str, str]]: ...

class ContentSnifferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentSnifferClass()
    """

    parent_class: GObject.ObjectClass = ...
    sniff: Callable[[ContentSniffer, Message, Buffer], Tuple[str, dict[str, str]]] = ...
    get_buffer_size: Callable[[ContentSniffer], int] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...
    _libsoup_reserved5: None = ...

class ContentSnifferPrivate(GObject.GPointer): ...

class Cookie(GObject.GBoxed):
    """
    :Constructors:

    ::

        Cookie()
        new(name:str, value:str, domain:str, path:str, max_age:int) -> Soup.Cookie
    """

    name: str = ...
    value: str = ...
    domain: str = ...
    path: str = ...
    expires: Date = ...
    secure: bool = ...
    http_only: bool = ...
    def applies_to_uri(self, uri: URI) -> bool: ...
    def copy(self) -> Cookie: ...
    def domain_matches(self, host: str) -> bool: ...
    def equal(self, cookie2: Cookie) -> bool: ...
    def free(self) -> None: ...
    def get_domain(self) -> str: ...
    def get_expires(self) -> Optional[Date]: ...
    def get_http_only(self) -> bool: ...
    def get_name(self) -> str: ...
    def get_path(self) -> str: ...
    def get_same_site_policy(self) -> SameSitePolicy: ...
    def get_secure(self) -> bool: ...
    def get_value(self) -> str: ...
    @classmethod
    def new(
        cls, name: str, value: str, domain: str, path: str, max_age: int
    ) -> Cookie: ...
    @staticmethod
    def parse(header: str, origin: URI) -> Optional[Cookie]: ...
    def set_domain(self, domain: str) -> None: ...
    def set_expires(self, expires: Date) -> None: ...
    def set_http_only(self, http_only: bool) -> None: ...
    def set_max_age(self, max_age: int) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_path(self, path: str) -> None: ...
    def set_same_site_policy(self, policy: SameSitePolicy) -> None: ...
    def set_secure(self, secure: bool) -> None: ...
    def set_value(self, value: str) -> None: ...
    def to_cookie_header(self) -> str: ...
    def to_set_cookie_header(self) -> str: ...

class CookieJar(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        CookieJar(**properties)
        new() -> Soup.CookieJar

    Object SoupCookieJar

    Signals from SoupCookieJar:
      changed (SoupCookie, SoupCookie)

    Properties from SoupCookieJar:
      read-only -> gboolean: Read-only
        Whether or not the cookie jar is read-only
      accept-policy -> SoupCookieJarAcceptPolicy: Accept-policy
        The policy the jar should follow to accept or reject cookies

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_policy: CookieJarAcceptPolicy
        read_only: bool
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self, accept_policy: CookieJarAcceptPolicy = ..., read_only: bool = ...
    ): ...
    def add_cookie(self, cookie: Cookie) -> None: ...
    def add_cookie_full(
        self,
        cookie: Cookie,
        uri: Optional[URI] = None,
        first_party: Optional[URI] = None,
    ) -> None: ...
    def add_cookie_with_first_party(self, first_party: URI, cookie: Cookie) -> None: ...
    def all_cookies(self) -> list[Cookie]: ...
    def delete_cookie(self, cookie: Cookie) -> None: ...
    def do_changed(self, old_cookie: Cookie, new_cookie: Cookie) -> None: ...
    def do_is_persistent(self) -> bool: ...
    def do_save(self) -> None: ...
    def get_accept_policy(self) -> CookieJarAcceptPolicy: ...
    def get_cookie_list(self, uri: URI, for_http: bool) -> list[Cookie]: ...
    def get_cookie_list_with_same_site_info(
        self,
        uri: URI,
        top_level: Optional[URI],
        site_for_cookies: Optional[URI],
        for_http: bool,
        is_safe_method: bool,
        is_top_level_navigation: bool,
    ) -> list[Cookie]: ...
    def get_cookies(self, uri: URI, for_http: bool) -> Optional[str]: ...
    def is_persistent(self) -> bool: ...
    @classmethod
    def new(cls) -> CookieJar: ...
    @deprecated("This is a no-op.")
    def save(self) -> None: ...
    def set_accept_policy(self, policy: CookieJarAcceptPolicy) -> None: ...
    def set_cookie(self, uri: URI, cookie: str) -> None: ...
    def set_cookie_with_first_party(
        self, uri: URI, first_party: URI, cookie: str
    ) -> None: ...

class CookieJarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieJarClass()
    """

    parent_class: GObject.ObjectClass = ...
    save: Callable[[CookieJar], None] = ...
    is_persistent: Callable[[CookieJar], bool] = ...
    changed: Callable[[CookieJar, Cookie, Cookie], None] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...

class CookieJarDB(CookieJar, SessionFeature):
    """
    :Constructors:

    ::

        CookieJarDB(**properties)
        new(filename:str, read_only:bool) -> Soup.CookieJar

    Object SoupCookieJarDB

    Properties from SoupCookieJarDB:
      filename -> gchararray: Filename
        Cookie-storage filename

    Signals from SoupCookieJar:
      changed (SoupCookie, SoupCookie)

    Properties from SoupCookieJar:
      read-only -> gboolean: Read-only
        Whether or not the cookie jar is read-only
      accept-policy -> SoupCookieJarAcceptPolicy: Accept-policy
        The policy the jar should follow to accept or reject cookies

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filename: str
        accept_policy: CookieJarAcceptPolicy
        read_only: bool
    props: Props = ...
    parent: CookieJar = ...
    def __init__(
        self,
        filename: str = ...,
        accept_policy: CookieJarAcceptPolicy = ...,
        read_only: bool = ...,
    ): ...
    @classmethod
    def new(cls, filename: str, read_only: bool) -> CookieJarDB: ...

class CookieJarDBClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieJarDBClass()
    """

    parent_class: CookieJarClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class CookieJarText(CookieJar, SessionFeature):
    """
    :Constructors:

    ::

        CookieJarText(**properties)
        new(filename:str, read_only:bool) -> Soup.CookieJar

    Object SoupCookieJarText

    Properties from SoupCookieJarText:
      filename -> gchararray: Filename
        Cookie-storage filename

    Signals from SoupCookieJar:
      changed (SoupCookie, SoupCookie)

    Properties from SoupCookieJar:
      read-only -> gboolean: Read-only
        Whether or not the cookie jar is read-only
      accept-policy -> SoupCookieJarAcceptPolicy: Accept-policy
        The policy the jar should follow to accept or reject cookies

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filename: str
        accept_policy: CookieJarAcceptPolicy
        read_only: bool
    props: Props = ...
    parent: CookieJar = ...
    def __init__(
        self,
        filename: str = ...,
        accept_policy: CookieJarAcceptPolicy = ...,
        read_only: bool = ...,
    ): ...
    @classmethod
    def new(cls, filename: str, read_only: bool) -> CookieJarText: ...

class CookieJarTextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieJarTextClass()
    """

    parent_class: CookieJarClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class Date(GObject.GBoxed):
    """
    :Constructors:

    ::

        Date()
        new(year:int, month:int, day:int, hour:int, minute:int, second:int) -> Soup.Date
        new_from_now(offset_seconds:int) -> Soup.Date
        new_from_string(date_string:str) -> Soup.Date or None
        new_from_time_t(when:int) -> Soup.Date
    """

    year: int = ...
    month: int = ...
    day: int = ...
    hour: int = ...
    minute: int = ...
    second: int = ...
    utc: bool = ...
    offset: int = ...
    def copy(self) -> Date: ...
    def free(self) -> None: ...
    def get_day(self) -> int: ...
    def get_hour(self) -> int: ...
    def get_minute(self) -> int: ...
    def get_month(self) -> int: ...
    def get_offset(self) -> int: ...
    def get_second(self) -> int: ...
    def get_utc(self) -> int: ...
    def get_year(self) -> int: ...
    def is_past(self) -> bool: ...
    @classmethod
    def new(
        cls, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> Date: ...
    @classmethod
    def new_from_now(cls, offset_seconds: int) -> Date: ...
    @classmethod
    def new_from_string(cls, date_string: str) -> Optional[Date]: ...
    @classmethod
    def new_from_time_t(cls, when: int) -> Date: ...
    def to_string(self, format: DateFormat) -> str: ...
    def to_time_t(self) -> int: ...
    @deprecated("Do not use #GTimeVal, as it's not Y2038-safe.")
    def to_timeval(self) -> GLib.TimeVal: ...

class HSTSEnforcer(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        HSTSEnforcer(**properties)
        new() -> Soup.HSTSEnforcer

    Object SoupHSTSEnforcer

    Signals from SoupHSTSEnforcer:
      changed (SoupHSTSPolicy, SoupHSTSPolicy)
      hsts-enforced (SoupMessage)

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: HSTSEnforcerPrivate = ...
    def do_changed(self, old_policy: HSTSPolicy, new_policy: HSTSPolicy) -> None: ...
    def do_has_valid_policy(self, domain: str) -> bool: ...
    def do_hsts_enforced(self, message: Message) -> None: ...
    def do_is_persistent(self) -> bool: ...
    def get_domains(self, session_policies: bool) -> list[str]: ...
    def get_policies(self, session_policies: bool) -> list[HSTSPolicy]: ...
    def has_valid_policy(self, domain: str) -> bool: ...
    def is_persistent(self) -> bool: ...
    @classmethod
    def new(cls) -> HSTSEnforcer: ...
    def set_policy(self, policy: HSTSPolicy) -> None: ...
    def set_session_policy(self, domain: str, include_subdomains: bool) -> None: ...

class HSTSEnforcerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HSTSEnforcerClass()
    """

    parent_class: GObject.ObjectClass = ...
    is_persistent: Callable[[HSTSEnforcer], bool] = ...
    has_valid_policy: Callable[[HSTSEnforcer, str], bool] = ...
    changed: Callable[[HSTSEnforcer, HSTSPolicy, HSTSPolicy], None] = ...
    hsts_enforced: Callable[[HSTSEnforcer, Message], None] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class HSTSEnforcerDB(HSTSEnforcer, SessionFeature):
    """
    :Constructors:

    ::

        HSTSEnforcerDB(**properties)
        new(filename:str) -> Soup.HSTSEnforcer

    Object SoupHSTSEnforcerDB

    Properties from SoupHSTSEnforcerDB:
      filename -> gchararray: Filename
        HSTS policy storage filename

    Signals from SoupHSTSEnforcer:
      changed (SoupHSTSPolicy, SoupHSTSPolicy)
      hsts-enforced (SoupMessage)

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filename: str
    props: Props = ...
    parent: HSTSEnforcer = ...
    priv: HSTSEnforcerDBPrivate = ...
    def __init__(self, filename: str = ...): ...
    @classmethod
    def new(cls, filename: str) -> HSTSEnforcerDB: ...

class HSTSEnforcerDBClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HSTSEnforcerDBClass()
    """

    parent_class: HSTSEnforcerClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class HSTSEnforcerDBPrivate(GObject.GPointer): ...
class HSTSEnforcerPrivate(GObject.GPointer): ...

class HSTSPolicy(GObject.GBoxed):
    """
    :Constructors:

    ::

        HSTSPolicy()
        new(domain:str, max_age:int, include_subdomains:bool) -> Soup.HSTSPolicy
        new_from_response(msg:Soup.Message) -> Soup.HSTSPolicy or None
        new_full(domain:str, max_age:int, expires:Soup.Date, include_subdomains:bool) -> Soup.HSTSPolicy
        new_session_policy(domain:str, include_subdomains:bool) -> Soup.HSTSPolicy
    """

    domain: str = ...
    max_age: int = ...
    expires: Date = ...
    include_subdomains: bool = ...
    def copy(self) -> HSTSPolicy: ...
    def equal(self, policy2: HSTSPolicy) -> bool: ...
    def free(self) -> None: ...
    def get_domain(self) -> str: ...
    def includes_subdomains(self) -> bool: ...
    def is_expired(self) -> bool: ...
    def is_session_policy(self) -> bool: ...
    @classmethod
    def new(cls, domain: str, max_age: int, include_subdomains: bool) -> HSTSPolicy: ...
    @classmethod
    def new_from_response(cls, msg: Message) -> Optional[HSTSPolicy]: ...
    @classmethod
    def new_full(
        cls, domain: str, max_age: int, expires: Date, include_subdomains: bool
    ) -> HSTSPolicy: ...
    @classmethod
    def new_session_policy(
        cls, domain: str, include_subdomains: bool
    ) -> HSTSPolicy: ...

class Logger(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        Logger(**properties)
        new(level:Soup.LoggerLogLevel, max_body_size:int) -> Soup.Logger

    Object SoupLogger

    Properties from SoupLogger:
      level -> SoupLoggerLogLevel: Level
        The level of logging output
      max-body-size -> gint: Max Body Size
        The maximum body size to output

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        level: LoggerLogLevel
        max_body_size: int
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(self, level: LoggerLogLevel = ..., max_body_size: int = ...): ...
    @deprecated("Use soup_session_add_feature() instead.")
    def attach(self, session: Session) -> None: ...
    @deprecated("Use soup_session_remove_feature() instead.")
    def detach(self, session: Session) -> None: ...
    @classmethod
    def new(cls, level: LoggerLogLevel, max_body_size: int) -> Logger: ...
    def set_printer(self, printer: Callable[..., None], *printer_data: Any) -> None: ...
    def set_request_filter(
        self, request_filter: Callable[..., LoggerLogLevel], *filter_data: Any
    ) -> None: ...
    def set_response_filter(
        self, response_filter: Callable[..., LoggerLogLevel], *filter_data: Any
    ) -> None: ...

class LoggerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LoggerClass()
    """

    parent_class: GObject.ObjectClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class Message(GObject.Object):
    """
    :Constructors:

    ::

        Message(**properties)
        new(method:str, uri_string:str) -> Soup.Message or None
        new_from_uri(method:str, uri:Soup.URI) -> Soup.Message

    Object SoupMessage

    Signals from SoupMessage:
      wrote-informational ()
      wrote-headers ()
      wrote-chunk ()
      wrote-body-data (SoupBuffer)
      wrote-body ()
      got-informational ()
      got-headers ()
      got-chunk (SoupBuffer)
      got-body ()
      content-sniffed (gchararray, GHashTable)
      starting ()
      restarted ()
      finished ()
      network-event (GSocketClientEvent, GIOStream)

    Properties from SoupMessage:
      method -> gchararray: Method
        The message's HTTP method
      uri -> SoupURI: URI
        The message's Request-URI
      http-version -> SoupHTTPVersion: HTTP Version
        The HTTP protocol version to use
      flags -> SoupMessageFlags: Flags
        Various message options
      server-side -> gboolean: Server-side
        Whether or not the message is server-side rather than client-side
      status-code -> guint: Status code
        The HTTP response status code
      reason-phrase -> gchararray: Reason phrase
        The HTTP response reason phrase
      first-party -> SoupURI: First party
        The URI loaded in the application when the message was requested.
      request-body -> SoupMessageBody: Request Body
        The HTTP request content
      request-body-data -> GBytes: Request Body Data
        The HTTP request body
      request-headers -> SoupMessageHeaders: Request Headers
        The HTTP request headers
      response-body -> SoupMessageBody: Response Body
        The HTTP response content
      response-body-data -> GBytes: Response Body Data
        The HTTP response body
      response-headers -> SoupMessageHeaders: Response Headers
        The HTTP response headers
      tls-certificate -> GTlsCertificate: TLS Certificate
        The TLS certificate associated with the message
      tls-errors -> GTlsCertificateFlags: TLS Errors
        The verification errors on the message's TLS certificate
      priority -> SoupMessagePriority: Priority
        The priority of the message
      site-for-cookies -> SoupURI: Site for cookies
        The URI for the site to compare cookies against
      is-top-level-navigation -> gboolean: Is top-level navigation
        If the current messsage is navigating between top-levels

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        first_party: URI
        flags: MessageFlags
        http_version: HTTPVersion
        is_top_level_navigation: bool
        method: str
        priority: MessagePriority
        reason_phrase: str
        request_body: MessageBody
        request_body_data: GLib.Bytes
        request_headers: MessageHeaders
        response_body: MessageBody
        response_body_data: GLib.Bytes
        response_headers: MessageHeaders
        server_side: bool
        site_for_cookies: URI
        status_code: int
        tls_certificate: Gio.TlsCertificate
        tls_errors: Gio.TlsCertificateFlags
        uri: URI
    props: Props = ...
    parent: GObject.Object = ...
    method: str = ...
    status_code: int = ...
    reason_phrase: str = ...
    request_body: MessageBody = ...
    request_headers: MessageHeaders = ...
    response_body: MessageBody = ...
    response_headers: MessageHeaders = ...
    def __init__(
        self,
        first_party: URI = ...,
        flags: MessageFlags = ...,
        http_version: HTTPVersion = ...,
        is_top_level_navigation: bool = ...,
        method: str = ...,
        priority: MessagePriority = ...,
        reason_phrase: str = ...,
        server_side: bool = ...,
        site_for_cookies: Optional[URI] = ...,
        status_code: int = ...,
        tls_certificate: Gio.TlsCertificate = ...,
        tls_errors: Gio.TlsCertificateFlags = ...,
        uri: URI = ...,
    ): ...
    def content_sniffed(self, content_type: str, params: dict[None, None]) -> None: ...
    def disable_feature(self, feature_type: Type) -> None: ...
    def do_finished(self) -> None: ...
    def do_got_body(self) -> None: ...
    def do_got_chunk(self, chunk: Buffer) -> None: ...
    def do_got_headers(self) -> None: ...
    def do_got_informational(self) -> None: ...
    def do_restarted(self) -> None: ...
    def do_starting(self) -> None: ...
    def do_wrote_body(self) -> None: ...
    def do_wrote_chunk(self) -> None: ...
    def do_wrote_headers(self) -> None: ...
    def do_wrote_informational(self) -> None: ...
    def finished(self) -> None: ...
    def get_address(self) -> Address: ...
    def get_first_party(self) -> URI: ...
    def get_flags(self) -> MessageFlags: ...
    def get_http_version(self) -> HTTPVersion: ...
    def get_https_status(
        self,
    ) -> Tuple[bool, Gio.TlsCertificate, Gio.TlsCertificateFlags]: ...
    def get_is_top_level_navigation(self) -> bool: ...
    def get_priority(self) -> MessagePriority: ...
    def get_site_for_cookies(self) -> URI: ...
    def get_soup_request(self) -> Request: ...
    def get_uri(self) -> URI: ...
    def got_body(self) -> None: ...
    def got_chunk(self, chunk: Buffer) -> None: ...
    def got_headers(self) -> None: ...
    def got_informational(self) -> None: ...
    def is_feature_disabled(self, feature_type: Type) -> bool: ...
    def is_keepalive(self) -> bool: ...
    @classmethod
    def new(cls, method: str, uri_string: str) -> Optional[Message]: ...
    @classmethod
    def new_from_uri(cls, method: str, uri: URI) -> Message: ...
    def restarted(self) -> None: ...
    @deprecated(
        "#SoupRequest provides a much simpler API that lets you read the response directly into your own buffers without needing to mess with callbacks, pausing/unpausing, etc."
    )
    def set_chunk_allocator(
        self, allocator: Callable[..., Optional[Buffer]], *user_data: Any
    ) -> None: ...
    def set_first_party(self, first_party: URI) -> None: ...
    def set_flags(self, flags: MessageFlags) -> None: ...
    def set_http_version(self, version: HTTPVersion) -> None: ...
    def set_is_top_level_navigation(self, is_top_level_navigation: bool) -> None: ...
    def set_priority(self, priority: MessagePriority) -> None: ...
    def set_redirect(self, status_code: int, redirect_uri: str) -> None: ...
    def set_request(
        self,
        content_type: Optional[str],
        req_use: MemoryUse,
        req_body: Optional[Sequence[int]] = None,
    ) -> None: ...
    def set_response(
        self,
        content_type: Optional[str],
        resp_use: MemoryUse,
        resp_body: Optional[Sequence[int]] = None,
    ) -> None: ...
    def set_site_for_cookies(self, site_for_cookies: Optional[URI] = None) -> None: ...
    def set_status(self, status_code: int) -> None: ...
    def set_status_full(self, status_code: int, reason_phrase: str) -> None: ...
    def set_uri(self, uri: URI) -> None: ...
    def starting(self) -> None: ...
    def wrote_body(self) -> None: ...
    def wrote_body_data(self, chunk: Buffer) -> None: ...
    def wrote_chunk(self) -> None: ...
    def wrote_headers(self) -> None: ...
    def wrote_informational(self) -> None: ...

class MessageBody(GObject.GBoxed):
    """
    :Constructors:

    ::

        MessageBody()
        new() -> Soup.MessageBody
    """

    data: str = ...
    length: int = ...
    def append(self, data: Sequence[int]) -> None: ...
    def append_buffer(self, buffer: Buffer) -> None: ...
    def complete(self) -> None: ...
    def flatten(self) -> Buffer: ...
    def free(self) -> None: ...
    def get_accumulate(self) -> bool: ...
    def get_chunk(self, offset: int) -> Optional[Buffer]: ...
    def got_chunk(self, chunk: Buffer) -> None: ...
    @classmethod
    def new(cls) -> MessageBody: ...
    def set_accumulate(self, accumulate: bool) -> None: ...
    def truncate(self) -> None: ...
    def wrote_chunk(self, chunk: Buffer) -> None: ...

class MessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MessageClass()
    """

    parent_class: GObject.ObjectClass = ...
    wrote_informational: Callable[[Message], None] = ...
    wrote_headers: Callable[[Message], None] = ...
    wrote_chunk: Callable[[Message], None] = ...
    wrote_body: Callable[[Message], None] = ...
    got_informational: Callable[[Message], None] = ...
    got_headers: Callable[[Message], None] = ...
    got_chunk: Callable[[Message, Buffer], None] = ...
    got_body: Callable[[Message], None] = ...
    restarted: Callable[[Message], None] = ...
    finished: Callable[[Message], None] = ...
    starting: Callable[[Message], None] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...

class MessageHeaders(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(type:Soup.MessageHeadersType) -> Soup.MessageHeaders
    """

    def append(self, name: str, value: str) -> None: ...
    def clean_connection_headers(self) -> None: ...
    def clear(self) -> None: ...
    def foreach(self, func: Callable[..., None], *user_data: Any) -> None: ...
    def free(self) -> None: ...
    def free_ranges(self, ranges: Range) -> None: ...
    @deprecated(
        "Use soup_message_headers_get_one() or soup_message_headers_get_list() instead."
    )
    def get(self, name: str) -> Optional[str]: ...
    def get_content_disposition(self) -> Tuple[bool, str, dict[str, str]]: ...
    def get_content_length(self) -> int: ...
    def get_content_range(self) -> Tuple[bool, int, int, int]: ...
    def get_content_type(self) -> Tuple[Optional[str], dict[str, str]]: ...
    def get_encoding(self) -> Encoding: ...
    def get_expectations(self) -> Expectation: ...
    def get_headers_type(self) -> MessageHeadersType: ...
    def get_list(self, name: str) -> Optional[str]: ...
    def get_one(self, name: str) -> Optional[str]: ...
    def get_ranges(self, total_length: int) -> Tuple[bool, list[Range]]: ...
    def header_contains(self, name: str, token: str) -> bool: ...
    def header_equals(self, name: str, value: str) -> bool: ...
    @classmethod
    def new(cls, type: MessageHeadersType) -> MessageHeaders: ...
    def remove(self, name: str) -> None: ...
    def replace(self, name: str, value: str) -> None: ...
    def set_content_disposition(
        self, disposition: str, params: Optional[dict[str, str]] = None
    ) -> None: ...
    def set_content_length(self, content_length: int) -> None: ...
    def set_content_range(self, start: int, end: int, total_length: int) -> None: ...
    def set_content_type(
        self, content_type: str, params: Optional[dict[str, str]] = None
    ) -> None: ...
    def set_encoding(self, encoding: Encoding) -> None: ...
    def set_expectations(self, expectations: Expectation) -> None: ...
    def set_range(self, start: int, end: int) -> None: ...
    def set_ranges(self, ranges: Range, length: int) -> None: ...

class MessageHeadersIter(GObject.GPointer):
    """
    :Constructors:

    ::

        MessageHeadersIter()
    """

    dummy: list[None] = ...
    @staticmethod
    def init(hdrs: MessageHeaders) -> MessageHeadersIter: ...
    def next(self) -> Tuple[bool, str, str]: ...

class MessageQueue(GObject.GPointer): ...
class MessageQueueItem(GObject.GPointer): ...

class Multipart(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(mime_type:str) -> Soup.Multipart
        new_from_message(headers:Soup.MessageHeaders, body:Soup.MessageBody) -> Soup.Multipart or None
    """

    def append_form_file(
        self, control_name: str, filename: str, content_type: str, body: Buffer
    ) -> None: ...
    def append_form_string(self, control_name: str, data: str) -> None: ...
    def append_part(self, headers: MessageHeaders, body: Buffer) -> None: ...
    def free(self) -> None: ...
    def get_length(self) -> int: ...
    def get_part(self, part: int) -> Tuple[bool, MessageHeaders, Buffer]: ...
    @classmethod
    def new(cls, mime_type: str) -> Multipart: ...
    @classmethod
    def new_from_message(
        cls, headers: MessageHeaders, body: MessageBody
    ) -> Optional[Multipart]: ...
    def to_message(
        self, dest_headers: MessageHeaders, dest_body: MessageBody
    ) -> None: ...

class MultipartInputStream(Gio.FilterInputStream, Gio.PollableInputStream):
    """
    :Constructors:

    ::

        MultipartInputStream(**properties)
        new(msg:Soup.Message, base_stream:Gio.InputStream) -> Soup.MultipartInputStream

    Object SoupMultipartInputStream

    Properties from SoupMultipartInputStream:
      message -> SoupMessage: Message
        The SoupMessage

    Properties from GFilterInputStream:
      base-stream -> GInputStream: The Filter Base Stream
        The underlying base stream on which the io ops will be done.
      close-base-stream -> gboolean: Close Base Stream
        If the base stream should be closed when the filter stream is closed.

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        message: Message
        base_stream: Gio.InputStream
        close_base_stream: bool
    props: Props = ...
    parent_instance: Gio.FilterInputStream = ...
    priv: MultipartInputStreamPrivate = ...
    def __init__(
        self,
        message: Message = ...,
        base_stream: Gio.InputStream = ...,
        close_base_stream: bool = ...,
    ): ...
    def get_headers(self) -> Optional[MessageHeaders]: ...
    @classmethod
    def new(
        cls, msg: Message, base_stream: Gio.InputStream
    ) -> MultipartInputStream: ...
    def next_part(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Optional[Gio.InputStream]: ...
    def next_part_async(
        self,
        io_priority: int,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *data: Any,
    ) -> None: ...
    def next_part_finish(
        self, result: Gio.AsyncResult
    ) -> Optional[Gio.InputStream]: ...

class MultipartInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MultipartInputStreamClass()
    """

    parent_class: Gio.FilterInputStreamClass = ...

class MultipartInputStreamPrivate(GObject.GPointer): ...

class PasswordManager(GObject.GInterface):
    """
    Interface SoupPasswordManager

    Signals from GObject:
      notify (GParam)
    """

    def get_passwords_async(
        self,
        msg: Message,
        auth: Auth,
        retrying: bool,
        async_context: GLib.MainContext,
        cancellable: Optional[Gio.Cancellable],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    def get_passwords_sync(
        self, msg: Message, auth: Auth, cancellable: Optional[Gio.Cancellable] = None
    ) -> None: ...

class PasswordManagerInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PasswordManagerInterface()
    """

    base: GObject.TypeInterface = ...
    get_passwords_async: Callable[..., None] = ...
    get_passwords_sync: Callable[
        [PasswordManager, Message, Auth, Optional[Gio.Cancellable]], None
    ] = ...

class ProxyResolver(GObject.GInterface):
    """
    Interface SoupProxyResolver

    Signals from GObject:
      notify (GParam)
    """

    @deprecated("Use SoupProxyURIResolver.get_proxy_uri_async instead")
    def get_proxy_async(
        self,
        msg: Message,
        async_context: GLib.MainContext,
        cancellable: Optional[Gio.Cancellable],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    @deprecated("Use SoupProxyURIResolver.get_proxy_uri_sync() instead")
    def get_proxy_sync(
        self, msg: Message, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[int, Address]: ...

class ProxyResolverDefault(GObject.Object, ProxyURIResolver, SessionFeature):
    """
    :Constructors:

    ::

        ProxyResolverDefault(**properties)

    Object SoupProxyResolverDefault

    Properties from SoupProxyResolverDefault:
      gproxy-resolver -> GProxyResolver: GProxyResolver
        The underlying GProxyResolver

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        gproxy_resolver: Gio.ProxyResolver
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(self, gproxy_resolver: Gio.ProxyResolver = ...): ...

class ProxyResolverDefaultClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyResolverDefaultClass()
    """

    parent_class: GObject.ObjectClass = ...

class ProxyResolverInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyResolverInterface()
    """

    base: GObject.TypeInterface = ...
    get_proxy_async: Callable[..., None] = ...
    get_proxy_sync: Callable[
        [ProxyResolver, Message, Optional[Gio.Cancellable]], Tuple[int, Address]
    ] = ...

class ProxyURIResolver(GObject.GInterface):
    """
    Interface SoupProxyURIResolver

    Signals from GObject:
      notify (GParam)
    """

    @deprecated("#SoupProxyURIResolver is deprecated in favor of #GProxyResolver")
    def get_proxy_uri_async(
        self,
        uri: URI,
        async_context: Optional[GLib.MainContext],
        cancellable: Optional[Gio.Cancellable],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    @deprecated("#SoupProxyURIResolver is deprecated in favor of #GProxyResolver")
    def get_proxy_uri_sync(
        self, uri: URI, cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[int, URI]: ...

class ProxyURIResolverInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyURIResolverInterface()
    """

    base: GObject.TypeInterface = ...
    get_proxy_uri_async: Callable[..., None] = ...
    get_proxy_uri_sync: Callable[
        [ProxyURIResolver, URI, Optional[Gio.Cancellable]], Tuple[int, URI]
    ] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class Range(GObject.GPointer):
    """
    :Constructors:

    ::

        Range()
    """

    start: int = ...
    end: int = ...

class Request(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Request(**properties)

    Object SoupRequest

    Properties from SoupRequest:
      uri -> SoupURI: URI
        The request URI
      session -> SoupSession: Session
        The request's session

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        session: Session
        uri: URI
    props: Props = ...
    parent: GObject.Object = ...
    priv: RequestPrivate = ...
    def __init__(self, session: Session = ..., uri: URI = ...): ...
    def do_check_uri(self, uri: URI) -> bool: ...
    def do_get_content_length(self) -> int: ...
    def do_get_content_type(self) -> Optional[str]: ...
    def do_send(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Gio.InputStream: ...
    def do_send_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def do_send_finish(self, result: Gio.AsyncResult) -> Gio.InputStream: ...
    def get_content_length(self) -> int: ...
    def get_content_type(self) -> Optional[str]: ...
    def get_session(self) -> Session: ...
    def get_uri(self) -> URI: ...
    def send(
        self, cancellable: Optional[Gio.Cancellable] = None
    ) -> Gio.InputStream: ...
    def send_async(
        self,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def send_finish(self, result: Gio.AsyncResult) -> Gio.InputStream: ...

class RequestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RequestClass()
    """

    parent: GObject.ObjectClass = ...
    schemes: str = ...
    check_uri: Callable[[Request, URI], bool] = ...
    send: Callable[[Request, Optional[Gio.Cancellable]], Gio.InputStream] = ...
    send_async: Callable[..., None] = ...
    send_finish: Callable[[Request, Gio.AsyncResult], Gio.InputStream] = ...
    get_content_length: Callable[[Request], int] = ...
    get_content_type: Callable[[Request], Optional[str]] = ...

class RequestData(Request, Gio.Initable):
    """
    :Constructors:

    ::

        RequestData(**properties)

    Object SoupRequestData

    Properties from SoupRequest:
      uri -> SoupURI: URI
        The request URI
      session -> SoupSession: Session
        The request's session

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        session: Session
        uri: URI
    props: Props = ...
    parent: Request = ...
    priv: RequestDataPrivate = ...
    def __init__(self, session: Session = ..., uri: URI = ...): ...

class RequestDataClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RequestDataClass()
    """

    parent: RequestClass = ...

class RequestDataPrivate(GObject.GPointer): ...

class RequestFile(Request, Gio.Initable):
    """
    :Constructors:

    ::

        RequestFile(**properties)

    Object SoupRequestFile

    Properties from SoupRequest:
      uri -> SoupURI: URI
        The request URI
      session -> SoupSession: Session
        The request's session

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        session: Session
        uri: URI
    props: Props = ...
    parent: Request = ...
    priv: RequestFilePrivate = ...
    def __init__(self, session: Session = ..., uri: URI = ...): ...
    def get_file(self) -> Gio.File: ...

class RequestFileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RequestFileClass()
    """

    parent: RequestClass = ...

class RequestFilePrivate(GObject.GPointer): ...

class RequestHTTP(Request, Gio.Initable):
    """
    :Constructors:

    ::

        RequestHTTP(**properties)

    Object SoupRequestHTTP

    Properties from SoupRequest:
      uri -> SoupURI: URI
        The request URI
      session -> SoupSession: Session
        The request's session

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        session: Session
        uri: URI
    props: Props = ...
    parent: Request = ...
    priv: RequestHTTPPrivate = ...
    def __init__(self, session: Session = ..., uri: URI = ...): ...
    def get_message(self) -> Message: ...

class RequestHTTPClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RequestHTTPClass()
    """

    parent: RequestClass = ...

class RequestHTTPPrivate(GObject.GPointer): ...
class RequestPrivate(GObject.GPointer): ...

class Requester(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        Requester(**properties)
        new() -> Soup.Requester

    Object SoupRequester

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: RequesterPrivate = ...
    @classmethod
    def new(cls) -> Requester: ...
    def request(self, uri_string: str) -> Request: ...
    def request_uri(self, uri: URI) -> Request: ...

class RequesterClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RequesterClass()
    """

    parent_class: GObject.ObjectClass = ...

class RequesterPrivate(GObject.GPointer): ...

class Server(GObject.Object):
    """
    :Constructors:

    ::

        Server(**properties)

    Object SoupServer

    Signals from SoupServer:
      request-started (SoupMessage, SoupClientContext)
      request-read (SoupMessage, SoupClientContext)
      request-finished (SoupMessage, SoupClientContext)
      request-aborted (SoupMessage, SoupClientContext)

    Properties from SoupServer:
      port -> guint: Port
        Port to listen on (Deprecated)
      interface -> SoupAddress: Interface
        Address of interface to listen on (Deprecated)
      ssl-cert-file -> gchararray: TLS (aka SSL) certificate file
        File containing server TLS (aka SSL) certificate
      ssl-key-file -> gchararray: TLS (aka SSL) key file
        File containing server TLS (aka SSL) key
      tls-certificate -> GTlsCertificate: TLS certificate
        GTlsCertificate to use for https
      async-context -> gpointer: Async GMainContext
        The GMainContext to dispatch async I/O in
      raw-paths -> gboolean: Raw paths
        If %TRUE, percent-encoding in the Request-URI path will not be automatically decoded.
      server-header -> gchararray: Server header
        Server header
      http-aliases -> GStrv: http aliases
        URI schemes that are considered aliases for 'http'
      https-aliases -> GStrv: https aliases
        URI schemes that are considered aliases for 'https'
      add-websocket-extension -> GType: Add support for a WebSocket extension
        Add support for a WebSocket extension of the given type
      remove-websocket-extension -> GType: Remove support for a WebSocket extension
        Remove support for a WebSocket extension of the given type

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        async_context: Optional[None]
        http_aliases: list[str]
        https_aliases: list[str]
        interface: Address
        port: int
        raw_paths: bool
        server_header: str
        ssl_cert_file: str
        ssl_key_file: str
        tls_certificate: Gio.TlsCertificate
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        async_context: None = ...,
        http_aliases: Sequence[str] = ...,
        https_aliases: Sequence[str] = ...,
        interface: Address = ...,
        port: int = ...,
        raw_paths: bool = ...,
        server_header: str = ...,
        ssl_cert_file: str = ...,
        ssl_key_file: str = ...,
        tls_certificate: Gio.TlsCertificate = ...,
    ): ...
    def accept_iostream(
        self,
        stream: Gio.IOStream,
        local_addr: Optional[Gio.SocketAddress] = None,
        remote_addr: Optional[Gio.SocketAddress] = None,
    ) -> bool: ...
    def add_auth_domain(self, auth_domain: AuthDomain) -> None: ...
    def add_early_handler(
        self, path: Optional[str], callback: Callable[..., None], *user_data: Any
    ) -> None: ...
    def add_handler(
        self, path: Optional[str], callback: Callable[..., None], *user_data: Any
    ) -> None: ...
    def add_websocket_extension(self, extension_type: Type) -> None: ...
    def add_websocket_handler(
        self,
        path: Optional[str],
        origin: Optional[str],
        protocols: Optional[Sequence[str]],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    def disconnect(self) -> None: ...
    def do_request_aborted(self, msg: Message, client: ClientContext) -> None: ...
    def do_request_finished(self, msg: Message, client: ClientContext) -> None: ...
    def do_request_read(self, msg: Message, client: ClientContext) -> None: ...
    def do_request_started(self, msg: Message, client: ClientContext) -> None: ...
    @deprecated(
        "If you are using soup_server_listen(), etc, then the server listens on the thread-default #GMainContext, and this property is ignored."
    )
    def get_async_context(self) -> Optional[GLib.MainContext]: ...
    @deprecated(
        "If you are using soup_server_listen(), etc, then use soup_server_get_listeners() to get a list of all listening sockets, but note that that function returns #GSockets, not #SoupSockets."
    )
    def get_listener(self) -> Socket: ...
    def get_listeners(self) -> list[Gio.Socket]: ...
    @deprecated(
        "If you are using soup_server_listen(), etc, then use soup_server_get_uris() to get a list of all listening addresses."
    )
    def get_port(self) -> int: ...
    def get_uris(self) -> list[URI]: ...
    def is_https(self) -> bool: ...
    def listen(
        self, address: Gio.SocketAddress, options: ServerListenOptions
    ) -> bool: ...
    def listen_all(self, port: int, options: ServerListenOptions) -> bool: ...
    def listen_fd(self, fd: int, options: ServerListenOptions) -> bool: ...
    def listen_local(self, port: int, options: ServerListenOptions) -> bool: ...
    def listen_socket(
        self, socket: Gio.Socket, options: ServerListenOptions
    ) -> bool: ...
    def pause_message(self, msg: Message) -> None: ...
    @deprecated(
        "When using soup_server_listen(), etc, the server will always listen for connections, and will process them whenever the thread-default #GMainContext is running."
    )
    def quit(self) -> None: ...
    def remove_auth_domain(self, auth_domain: AuthDomain) -> None: ...
    def remove_handler(self, path: str) -> None: ...
    def remove_websocket_extension(self, extension_type: Type) -> None: ...
    @deprecated(
        "When using soup_server_listen(), etc, the server will always listen for connections, and will process them whenever the thread-default #GMainContext is running."
    )
    def run(self) -> None: ...
    @deprecated(
        "When using soup_server_listen(), etc, the server will always listen for connections, and will process them whenever the thread-default #GMainContext is running."
    )
    def run_async(self) -> None: ...
    def set_ssl_cert_file(self, ssl_cert_file: str, ssl_key_file: str) -> bool: ...
    def unpause_message(self, msg: Message) -> None: ...

class ServerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ServerClass()
    """

    parent_class: GObject.ObjectClass = ...
    request_started: Callable[[Server, Message, ClientContext], None] = ...
    request_read: Callable[[Server, Message, ClientContext], None] = ...
    request_finished: Callable[[Server, Message, ClientContext], None] = ...
    request_aborted: Callable[[Server, Message, ClientContext], None] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class Session(GObject.Object):
    """
    :Constructors:

    ::

        Session(**properties)
        new() -> Soup.Session

    Object SoupSession

    Signals from SoupSession:
      authenticate (SoupMessage, SoupAuth, gboolean)
      request-started (SoupMessage, SoupSocket)
      request-queued (SoupMessage)
      request-unqueued (SoupMessage)
      connection-created (GObject)
      tunneling (GObject)

    Properties from SoupSession:
      proxy-uri -> SoupURI: Proxy URI
        The HTTP Proxy to use for this session
      proxy-resolver -> GProxyResolver: Proxy Resolver
        The GProxyResolver to use for this session
      max-conns -> gint: Max Connection Count
        The maximum number of connections that the session can open at once
      max-conns-per-host -> gint: Max Per-Host Connection Count
        The maximum number of connections that the session can open at once to a given host
      use-ntlm -> gboolean: Use NTLM
        Whether or not to use NTLM authentication
      ssl-ca-file -> gchararray: SSL CA file
        File containing SSL CA certificates
      ssl-use-system-ca-file -> gboolean: Use system CA file
        Use the system certificate database
      tls-database -> GTlsDatabase: TLS Database
        TLS database to use
      ssl-strict -> gboolean: Strictly validate SSL certificates
        Whether certificate errors should be considered a connection error
      async-context -> gpointer: Async GMainContext
        The GMainContext to dispatch async I/O in
      use-thread-context -> gboolean: Use thread-default GMainContext
        Whether to use thread-default main contexts
      timeout -> guint: Timeout value
        Value in seconds to timeout a blocking I/O
      user-agent -> gchararray: User-Agent string
        User-Agent string
      accept-language -> gchararray: Accept-Language string
        Accept-Language string
      accept-language-auto -> gboolean: Accept-Language automatic mode
        Accept-Language automatic mode
      idle-timeout -> guint: Idle Timeout
        Connection lifetime when idle
      add-feature -> SoupSessionFeature: Add Feature
        Add a feature object to the session
      add-feature-by-type -> GType: Add Feature By Type
        Add a feature object of the given type to the session
      remove-feature-by-type -> GType: Remove Feature By Type
        Remove features of the given type from the session
      http-aliases -> GStrv: http aliases
        URI schemes that are considered aliases for 'http'
      https-aliases -> GStrv: https aliases
        URI schemes that are considered aliases for 'https'
      local-address -> SoupAddress: Local address
        Address of local end of socket
      tls-interaction -> GTlsInteraction: TLS Interaction
        TLS interaction to use

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_language: str
        accept_language_auto: bool
        async_context: Optional[None]
        http_aliases: list[str]
        https_aliases: list[str]
        idle_timeout: int
        local_address: Address
        max_conns: int
        max_conns_per_host: int
        proxy_resolver: Gio.ProxyResolver
        proxy_uri: URI
        ssl_ca_file: str
        ssl_strict: bool
        ssl_use_system_ca_file: bool
        timeout: int
        tls_database: Gio.TlsDatabase
        tls_interaction: Gio.TlsInteraction
        use_ntlm: bool
        use_thread_context: bool
        user_agent: str
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        accept_language: str = ...,
        accept_language_auto: bool = ...,
        async_context: None = ...,
        http_aliases: Sequence[str] = ...,
        https_aliases: Sequence[str] = ...,
        idle_timeout: int = ...,
        local_address: Address = ...,
        max_conns: int = ...,
        max_conns_per_host: int = ...,
        proxy_resolver: Gio.ProxyResolver = ...,
        proxy_uri: URI = ...,
        ssl_ca_file: str = ...,
        ssl_strict: bool = ...,
        ssl_use_system_ca_file: bool = ...,
        timeout: int = ...,
        tls_database: Gio.TlsDatabase = ...,
        tls_interaction: Gio.TlsInteraction = ...,
        use_ntlm: bool = ...,
        use_thread_context: bool = ...,
        user_agent: str = ...,
    ): ...
    def abort(self) -> None: ...
    def add_feature(self, feature: SessionFeature) -> None: ...
    def add_feature_by_type(self, feature_type: Type) -> None: ...
    def cancel_message(self, msg: Message, status_code: int) -> None: ...
    def connect_async(
        self,
        uri: URI,
        cancellable: Optional[Gio.Cancellable] = None,
        progress_callback: Optional[Callable[..., None]] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def connect_finish(self, result: Gio.AsyncResult) -> Gio.IOStream: ...
    def do_auth_required(self, msg: Message, auth: Auth, retrying: bool) -> None: ...
    def do_authenticate(self, msg: Message, auth: Auth, retrying: bool) -> None: ...
    def do_cancel_message(self, msg: Message, status_code: int) -> None: ...
    def do_flush_queue(self) -> None: ...
    def do_kick(self) -> None: ...
    def do_queue_message(
        self,
        msg: Message,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def do_request_started(self, msg: Message, socket: Socket) -> None: ...
    def do_requeue_message(self, msg: Message) -> None: ...
    def do_send_message(self, msg: Message) -> int: ...
    def get_async_context(self) -> Optional[GLib.MainContext]: ...
    def get_feature(self, feature_type: Type) -> Optional[SessionFeature]: ...
    def get_feature_for_message(
        self, feature_type: Type, msg: Message
    ) -> Optional[SessionFeature]: ...
    def get_features(self, feature_type: Type) -> list[SessionFeature]: ...
    def has_feature(self, feature_type: Type) -> bool: ...
    @classmethod
    def new(cls) -> Session: ...
    def pause_message(self, msg: Message) -> None: ...
    def prefetch_dns(
        self,
        hostname: str,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    @deprecated("use soup_session_prefetch_dns() instead")
    def prepare_for_uri(self, uri: URI) -> None: ...
    def queue_message(
        self,
        msg: Message,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def redirect_message(self, msg: Message) -> bool: ...
    def remove_feature(self, feature: SessionFeature) -> None: ...
    def remove_feature_by_type(self, feature_type: Type) -> None: ...
    def request(self, uri_string: str) -> Request: ...
    def request_http(self, method: str, uri_string: str) -> RequestHTTP: ...
    def request_http_uri(self, method: str, uri: URI) -> RequestHTTP: ...
    def request_uri(self, uri: URI) -> Request: ...
    def requeue_message(self, msg: Message) -> None: ...
    def send(
        self, msg: Message, cancellable: Optional[Gio.Cancellable] = None
    ) -> Gio.InputStream: ...
    def send_async(
        self,
        msg: Message,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def send_finish(self, result: Gio.AsyncResult) -> Gio.InputStream: ...
    def send_message(self, msg: Message) -> int: ...
    def steal_connection(self, msg: Message) -> Gio.IOStream: ...
    def unpause_message(self, msg: Message) -> None: ...
    def websocket_connect_async(
        self,
        msg: Message,
        origin: Optional[str] = None,
        protocols: Optional[Sequence[str]] = None,
        cancellable: Optional[Gio.Cancellable] = None,
        callback: Optional[Callable[..., None]] = None,
        *user_data: Any,
    ) -> None: ...
    def websocket_connect_finish(
        self, result: Gio.AsyncResult
    ) -> WebsocketConnection: ...
    def would_redirect(self, msg: Message) -> bool: ...

class SessionAsync(Session):
    """
    :Constructors:

    ::

        SessionAsync(**properties)
        new() -> Soup.Session

    Object SoupSessionAsync

    Signals from SoupSession:
      authenticate (SoupMessage, SoupAuth, gboolean)
      request-started (SoupMessage, SoupSocket)
      request-queued (SoupMessage)
      request-unqueued (SoupMessage)
      connection-created (GObject)
      tunneling (GObject)

    Properties from SoupSession:
      proxy-uri -> SoupURI: Proxy URI
        The HTTP Proxy to use for this session
      proxy-resolver -> GProxyResolver: Proxy Resolver
        The GProxyResolver to use for this session
      max-conns -> gint: Max Connection Count
        The maximum number of connections that the session can open at once
      max-conns-per-host -> gint: Max Per-Host Connection Count
        The maximum number of connections that the session can open at once to a given host
      use-ntlm -> gboolean: Use NTLM
        Whether or not to use NTLM authentication
      ssl-ca-file -> gchararray: SSL CA file
        File containing SSL CA certificates
      ssl-use-system-ca-file -> gboolean: Use system CA file
        Use the system certificate database
      tls-database -> GTlsDatabase: TLS Database
        TLS database to use
      ssl-strict -> gboolean: Strictly validate SSL certificates
        Whether certificate errors should be considered a connection error
      async-context -> gpointer: Async GMainContext
        The GMainContext to dispatch async I/O in
      use-thread-context -> gboolean: Use thread-default GMainContext
        Whether to use thread-default main contexts
      timeout -> guint: Timeout value
        Value in seconds to timeout a blocking I/O
      user-agent -> gchararray: User-Agent string
        User-Agent string
      accept-language -> gchararray: Accept-Language string
        Accept-Language string
      accept-language-auto -> gboolean: Accept-Language automatic mode
        Accept-Language automatic mode
      idle-timeout -> guint: Idle Timeout
        Connection lifetime when idle
      add-feature -> SoupSessionFeature: Add Feature
        Add a feature object to the session
      add-feature-by-type -> GType: Add Feature By Type
        Add a feature object of the given type to the session
      remove-feature-by-type -> GType: Remove Feature By Type
        Remove features of the given type from the session
      http-aliases -> GStrv: http aliases
        URI schemes that are considered aliases for 'http'
      https-aliases -> GStrv: https aliases
        URI schemes that are considered aliases for 'https'
      local-address -> SoupAddress: Local address
        Address of local end of socket
      tls-interaction -> GTlsInteraction: TLS Interaction
        TLS interaction to use

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_language: str
        accept_language_auto: bool
        async_context: Optional[None]
        http_aliases: list[str]
        https_aliases: list[str]
        idle_timeout: int
        local_address: Address
        max_conns: int
        max_conns_per_host: int
        proxy_resolver: Gio.ProxyResolver
        proxy_uri: URI
        ssl_ca_file: str
        ssl_strict: bool
        ssl_use_system_ca_file: bool
        timeout: int
        tls_database: Gio.TlsDatabase
        tls_interaction: Gio.TlsInteraction
        use_ntlm: bool
        use_thread_context: bool
        user_agent: str
    props: Props = ...
    parent: Session = ...
    def __init__(
        self,
        accept_language: str = ...,
        accept_language_auto: bool = ...,
        async_context: None = ...,
        http_aliases: Sequence[str] = ...,
        https_aliases: Sequence[str] = ...,
        idle_timeout: int = ...,
        local_address: Address = ...,
        max_conns: int = ...,
        max_conns_per_host: int = ...,
        proxy_resolver: Gio.ProxyResolver = ...,
        proxy_uri: URI = ...,
        ssl_ca_file: str = ...,
        ssl_strict: bool = ...,
        ssl_use_system_ca_file: bool = ...,
        timeout: int = ...,
        tls_database: Gio.TlsDatabase = ...,
        tls_interaction: Gio.TlsInteraction = ...,
        use_ntlm: bool = ...,
        use_thread_context: bool = ...,
        user_agent: str = ...,
    ): ...
    @deprecated(
        '#SoupSessionAsync is deprecated; use a plain #SoupSession, created with soup_session_new(). See the <link linkend="libsoup-session-porting">porting guide</link>.'
    )
    @classmethod
    def new(cls) -> SessionAsync: ...

class SessionAsyncClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionAsyncClass()
    """

    parent_class: SessionClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class SessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionClass()
    """

    parent_class: GObject.ObjectClass = ...
    request_started: Callable[[Session, Message, Socket], None] = ...
    authenticate: Callable[[Session, Message, Auth, bool], None] = ...
    queue_message: Callable[..., None] = ...
    requeue_message: Callable[[Session, Message], None] = ...
    send_message: Callable[[Session, Message], int] = ...
    cancel_message: Callable[[Session, Message, int], None] = ...
    auth_required: Callable[[Session, Message, Auth, bool], None] = ...
    flush_queue: Callable[[Session], None] = ...
    kick: Callable[[Session], None] = ...
    _libsoup_reserved4: None = ...

class SessionFeature(GObject.GInterface):
    """
    Interface SoupSessionFeature

    Signals from GObject:
      notify (GParam)
    """

    def add_feature(self, type: Type) -> bool: ...
    def attach(self, session: Session) -> None: ...
    def detach(self, session: Session) -> None: ...
    def has_feature(self, type: Type) -> bool: ...
    def remove_feature(self, type: Type) -> bool: ...

class SessionFeatureInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionFeatureInterface()
    """

    parent: GObject.TypeInterface = ...
    attach: Callable[[SessionFeature, Session], None] = ...
    detach: Callable[[SessionFeature, Session], None] = ...
    request_queued: Callable[[SessionFeature, Session, Message], None] = ...
    request_started: Callable[[SessionFeature, Session, Message, Socket], None] = ...
    request_unqueued: Callable[[SessionFeature, Session, Message], None] = ...
    add_feature: Callable[[SessionFeature, Type], bool] = ...
    remove_feature: Callable[[SessionFeature, Type], bool] = ...
    has_feature: Callable[[SessionFeature, Type], bool] = ...

class SessionSync(Session):
    """
    :Constructors:

    ::

        SessionSync(**properties)
        new() -> Soup.Session

    Object SoupSessionSync

    Signals from SoupSession:
      authenticate (SoupMessage, SoupAuth, gboolean)
      request-started (SoupMessage, SoupSocket)
      request-queued (SoupMessage)
      request-unqueued (SoupMessage)
      connection-created (GObject)
      tunneling (GObject)

    Properties from SoupSession:
      proxy-uri -> SoupURI: Proxy URI
        The HTTP Proxy to use for this session
      proxy-resolver -> GProxyResolver: Proxy Resolver
        The GProxyResolver to use for this session
      max-conns -> gint: Max Connection Count
        The maximum number of connections that the session can open at once
      max-conns-per-host -> gint: Max Per-Host Connection Count
        The maximum number of connections that the session can open at once to a given host
      use-ntlm -> gboolean: Use NTLM
        Whether or not to use NTLM authentication
      ssl-ca-file -> gchararray: SSL CA file
        File containing SSL CA certificates
      ssl-use-system-ca-file -> gboolean: Use system CA file
        Use the system certificate database
      tls-database -> GTlsDatabase: TLS Database
        TLS database to use
      ssl-strict -> gboolean: Strictly validate SSL certificates
        Whether certificate errors should be considered a connection error
      async-context -> gpointer: Async GMainContext
        The GMainContext to dispatch async I/O in
      use-thread-context -> gboolean: Use thread-default GMainContext
        Whether to use thread-default main contexts
      timeout -> guint: Timeout value
        Value in seconds to timeout a blocking I/O
      user-agent -> gchararray: User-Agent string
        User-Agent string
      accept-language -> gchararray: Accept-Language string
        Accept-Language string
      accept-language-auto -> gboolean: Accept-Language automatic mode
        Accept-Language automatic mode
      idle-timeout -> guint: Idle Timeout
        Connection lifetime when idle
      add-feature -> SoupSessionFeature: Add Feature
        Add a feature object to the session
      add-feature-by-type -> GType: Add Feature By Type
        Add a feature object of the given type to the session
      remove-feature-by-type -> GType: Remove Feature By Type
        Remove features of the given type from the session
      http-aliases -> GStrv: http aliases
        URI schemes that are considered aliases for 'http'
      https-aliases -> GStrv: https aliases
        URI schemes that are considered aliases for 'https'
      local-address -> SoupAddress: Local address
        Address of local end of socket
      tls-interaction -> GTlsInteraction: TLS Interaction
        TLS interaction to use

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_language: str
        accept_language_auto: bool
        async_context: Optional[None]
        http_aliases: list[str]
        https_aliases: list[str]
        idle_timeout: int
        local_address: Address
        max_conns: int
        max_conns_per_host: int
        proxy_resolver: Gio.ProxyResolver
        proxy_uri: URI
        ssl_ca_file: str
        ssl_strict: bool
        ssl_use_system_ca_file: bool
        timeout: int
        tls_database: Gio.TlsDatabase
        tls_interaction: Gio.TlsInteraction
        use_ntlm: bool
        use_thread_context: bool
        user_agent: str
    props: Props = ...
    parent: Session = ...
    def __init__(
        self,
        accept_language: str = ...,
        accept_language_auto: bool = ...,
        async_context: None = ...,
        http_aliases: Sequence[str] = ...,
        https_aliases: Sequence[str] = ...,
        idle_timeout: int = ...,
        local_address: Address = ...,
        max_conns: int = ...,
        max_conns_per_host: int = ...,
        proxy_resolver: Gio.ProxyResolver = ...,
        proxy_uri: URI = ...,
        ssl_ca_file: str = ...,
        ssl_strict: bool = ...,
        ssl_use_system_ca_file: bool = ...,
        timeout: int = ...,
        tls_database: Gio.TlsDatabase = ...,
        tls_interaction: Gio.TlsInteraction = ...,
        use_ntlm: bool = ...,
        use_thread_context: bool = ...,
        user_agent: str = ...,
    ): ...
    @deprecated(
        '#SoupSessionSync is deprecated; use a plain #SoupSession, created with soup_session_new(). See the <link linkend="libsoup-session-porting">porting guide</link>.'
    )
    @classmethod
    def new(cls) -> SessionSync: ...

class SessionSyncClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionSyncClass()
    """

    parent_class: SessionClass = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class Socket(GObject.Object, Gio.Initable):
    """
    :Constructors:

    ::

        Socket(**properties)

    Object SoupSocket

    Signals from SoupSocket:
      readable ()
      writable ()
      disconnected ()
      new-connection (SoupSocket)
      event (GSocketClientEvent, GIOStream)

    Properties from SoupSocket:
      fd -> gint: FD
        The socket's file descriptor
      gsocket -> GSocket: GSocket
        The socket's underlying GSocket
      iostream -> GIOStream: GIOStream
        The socket's underlying GIOStream
      local-address -> SoupAddress: Local address
        Address of local end of socket
      remote-address -> SoupAddress: Remote address
        Address of remote end of socket
      non-blocking -> gboolean: Non-blocking
        Whether or not the socket uses non-blocking I/O
      ipv6-only -> gboolean: IPv6 only
        IPv6 only
      is-server -> gboolean: Server
        Whether or not the socket is a server socket
      ssl-creds -> gpointer: SSL credentials
        SSL credential information, passed from the session to the SSL implementation
      ssl-strict -> gboolean: Strictly validate SSL certificates
        Whether certificate errors should be considered a connection error
      ssl-fallback -> gboolean: SSLv3 fallback
        Use SSLv3 instead of TLS (client-side only)
      async-context -> gpointer: Async GMainContext
        The GMainContext to dispatch this socket's async I/O in
      use-thread-context -> gboolean: Use thread context
        Use g_main_context_get_thread_default
      timeout -> guint: Timeout value
        Value in seconds to timeout a blocking I/O
      trusted-certificate -> gboolean: Trusted Certificate
        Whether the server certificate is trusted, if this is an SSL socket
      tls-certificate -> GTlsCertificate: TLS certificate
        The peer's TLS certificate
      tls-errors -> GTlsCertificateFlags: TLS errors
        Errors with the peer's TLS certificate
      socket-properties -> SoupSocketProperties: Socket properties
        Socket properties

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        async_context: None
        fd: int
        ipv6_only: bool
        is_server: bool
        local_address: Address
        non_blocking: bool
        remote_address: Address
        ssl_creds: None
        ssl_fallback: bool
        ssl_strict: bool
        timeout: int
        tls_certificate: Gio.TlsCertificate
        tls_errors: Gio.TlsCertificateFlags
        trusted_certificate: bool
        use_thread_context: bool
        gsocket: Gio.Socket
        iostream: Gio.IOStream
    props: Props = ...
    parent: GObject.Object = ...
    def __init__(
        self,
        async_context: None = ...,
        fd: int = ...,
        gsocket: Gio.Socket = ...,
        iostream: Gio.IOStream = ...,
        ipv6_only: bool = ...,
        local_address: Address = ...,
        non_blocking: bool = ...,
        remote_address: Address = ...,
        ssl_creds: None = ...,
        ssl_fallback: bool = ...,
        ssl_strict: bool = ...,
        timeout: int = ...,
        use_thread_context: bool = ...,
    ): ...
    def connect_async(
        self,
        cancellable: Optional[Gio.Cancellable],
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    def connect_sync(self, cancellable: Optional[Gio.Cancellable] = None) -> int: ...
    def disconnect(self) -> None: ...
    def do_disconnected(self) -> None: ...
    def do_new_connection(self, new_sock: Socket) -> None: ...
    def do_readable(self) -> None: ...
    def do_writable(self) -> None: ...
    def get_fd(self) -> int: ...
    def get_local_address(self) -> Address: ...
    def get_remote_address(self) -> Address: ...
    def is_connected(self) -> bool: ...
    def is_ssl(self) -> bool: ...
    def listen(self) -> bool: ...
    def read(
        self, buffer: Sequence[int], cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[SocketIOStatus, int]: ...
    def read_until(
        self,
        buffer: Sequence[int],
        boundary: None,
        boundary_len: int,
        cancellable: Optional[Gio.Cancellable] = None,
    ) -> Tuple[SocketIOStatus, int, bool]: ...
    def start_proxy_ssl(
        self, ssl_host: str, cancellable: Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def start_ssl(self, cancellable: Optional[Gio.Cancellable] = None) -> bool: ...
    def write(
        self, buffer: Sequence[int], cancellable: Optional[Gio.Cancellable] = None
    ) -> Tuple[SocketIOStatus, int]: ...

class SocketClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SocketClass()
    """

    parent_class: GObject.ObjectClass = ...
    readable: Callable[[Socket], None] = ...
    writable: Callable[[Socket], None] = ...
    disconnected: Callable[[Socket], None] = ...
    new_connection: Callable[[Socket, Socket], None] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class URI(GObject.GBoxed):
    """
    :Constructors:

    ::

        URI()
        new(uri_string:str=None) -> Soup.URI or None
        new_with_base(base:Soup.URI, uri_string:str) -> Soup.URI
    """

    scheme: str = ...
    user: str = ...
    password: str = ...
    host: str = ...
    port: int = ...
    path: str = ...
    query: str = ...
    fragment: str = ...
    def copy(self) -> URI: ...
    def copy_host(self) -> URI: ...
    @staticmethod
    def decode(part: str) -> str: ...
    @staticmethod
    def encode(part: str, escape_extra: Optional[str] = None) -> str: ...
    def equal(self, uri2: URI) -> bool: ...
    def free(self) -> None: ...
    def get_fragment(self) -> str: ...
    def get_host(self) -> str: ...
    def get_password(self) -> str: ...
    def get_path(self) -> str: ...
    def get_port(self) -> int: ...
    def get_query(self) -> str: ...
    def get_scheme(self) -> str: ...
    def get_user(self) -> str: ...
    def host_equal(self, v2: URI) -> bool: ...
    def host_hash(self) -> int: ...
    @classmethod
    def new(cls, uri_string: Optional[str] = None) -> Optional[URI]: ...
    @classmethod
    def new_with_base(cls, base: URI, uri_string: str) -> URI: ...
    @staticmethod
    def normalize(part: str, unescape_extra: Optional[str] = None) -> str: ...
    def set_fragment(self, fragment: Optional[str] = None) -> None: ...
    def set_host(self, host: Optional[str] = None) -> None: ...
    def set_password(self, password: Optional[str] = None) -> None: ...
    def set_path(self, path: str) -> None: ...
    def set_port(self, port: int) -> None: ...
    def set_query(self, query: Optional[str] = None) -> None: ...
    def set_query_from_form(self, form: dict[str, str]) -> None: ...
    def set_scheme(self, scheme: str) -> None: ...
    def set_user(self, user: Optional[str] = None) -> None: ...
    def to_string(self, just_path_and_query: bool) -> str: ...
    def uses_default_port(self) -> bool: ...

class WebsocketConnection(GObject.Object):
    """
    :Constructors:

    ::

        WebsocketConnection(**properties)
        new(stream:Gio.IOStream, uri:Soup.URI, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None) -> Soup.WebsocketConnection
        new_with_extensions(stream:Gio.IOStream, uri:Soup.URI, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None, extensions:list) -> Soup.WebsocketConnection

    Object SoupWebsocketConnection

    Signals from SoupWebsocketConnection:
      message (gint, GBytes)
      error (GError)
      closing ()
      closed ()
      pong (GBytes)

    Properties from SoupWebsocketConnection:
      io-stream -> GIOStream: I/O Stream
        Underlying I/O stream
      connection-type -> SoupWebsocketConnectionType: Connection type
        Connection type (client/server)
      uri -> SoupURI: URI
        The WebSocket URI
      origin -> gchararray: Origin
        The WebSocket origin
      protocol -> gchararray: Protocol
        The chosen WebSocket protocol
      state -> SoupWebsocketState: State
        State
      max-incoming-payload-size -> guint64: Max incoming payload size
        Max incoming payload size
      keepalive-interval -> guint: Keepalive interval
        Keepalive interval
      extensions -> gpointer: Active extensions
        The list of active extensions

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        connection_type: WebsocketConnectionType
        extensions: None
        io_stream: Gio.IOStream
        keepalive_interval: int
        max_incoming_payload_size: int
        origin: Optional[str]
        protocol: Optional[str]
        state: WebsocketState
        uri: URI
    props: Props = ...
    parent: GObject.Object = ...
    pv: WebsocketConnectionPrivate = ...
    def __init__(
        self,
        connection_type: WebsocketConnectionType = ...,
        extensions: None = ...,
        io_stream: Gio.IOStream = ...,
        keepalive_interval: int = ...,
        max_incoming_payload_size: int = ...,
        origin: str = ...,
        protocol: str = ...,
        uri: URI = ...,
    ): ...
    def close(self, code: int, data: Optional[str] = None) -> None: ...
    def do_closed(self) -> None: ...
    def do_closing(self) -> None: ...
    def do_error(self, error: GLib.Error) -> None: ...
    def do_message(self, type: WebsocketDataType, message: GLib.Bytes) -> None: ...
    def do_pong(self, message: GLib.Bytes) -> None: ...
    def get_close_code(self) -> int: ...
    def get_close_data(self) -> str: ...
    def get_connection_type(self) -> WebsocketConnectionType: ...
    def get_extensions(self) -> list[WebsocketExtension]: ...
    def get_io_stream(self) -> Gio.IOStream: ...
    def get_keepalive_interval(self) -> int: ...
    def get_max_incoming_payload_size(self) -> int: ...
    def get_origin(self) -> Optional[str]: ...
    def get_protocol(self) -> Optional[str]: ...
    def get_state(self) -> WebsocketState: ...
    def get_uri(self) -> URI: ...
    @classmethod
    def new(
        cls,
        stream: Gio.IOStream,
        uri: URI,
        type: WebsocketConnectionType,
        origin: Optional[str] = None,
        protocol: Optional[str] = None,
    ) -> WebsocketConnection: ...
    @classmethod
    def new_with_extensions(
        cls,
        stream: Gio.IOStream,
        uri: URI,
        type: WebsocketConnectionType,
        origin: Optional[str],
        protocol: Optional[str],
        extensions: list[WebsocketExtension],
    ) -> WebsocketConnection: ...
    def send_binary(self, data: Optional[Sequence[int]] = None) -> None: ...
    def send_message(self, type: WebsocketDataType, message: GLib.Bytes) -> None: ...
    def send_text(self, text: str) -> None: ...
    def set_keepalive_interval(self, interval: int) -> None: ...
    def set_max_incoming_payload_size(self, max_incoming_payload_size: int) -> None: ...

class WebsocketConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketConnectionClass()
    """

    parent: GObject.ObjectClass = ...
    message: Callable[[WebsocketConnection, WebsocketDataType, GLib.Bytes], None] = ...
    error: Callable[[WebsocketConnection, GLib.Error], None] = ...
    closing: Callable[[WebsocketConnection], None] = ...
    closed: Callable[[WebsocketConnection], None] = ...
    pong: Callable[[WebsocketConnection, GLib.Bytes], None] = ...

class WebsocketConnectionPrivate(GObject.GPointer): ...

class WebsocketExtension(GObject.Object):
    """
    :Constructors:

    ::

        WebsocketExtension(**properties)

    Object SoupWebsocketExtension

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    def configure(
        self,
        connection_type: WebsocketConnectionType,
        params: Optional[dict[None, None]] = None,
    ) -> bool: ...
    def do_configure(
        self,
        connection_type: WebsocketConnectionType,
        params: Optional[dict[None, None]] = None,
    ) -> bool: ...
    def do_get_request_params(self) -> Optional[str]: ...
    def do_get_response_params(self) -> Optional[str]: ...
    def do_process_incoming_message(
        self, payload: GLib.Bytes
    ) -> Tuple[GLib.Bytes, int]: ...
    def do_process_outgoing_message(
        self, payload: GLib.Bytes
    ) -> Tuple[GLib.Bytes, int]: ...
    def get_request_params(self) -> Optional[str]: ...
    def get_response_params(self) -> Optional[str]: ...
    def process_incoming_message(
        self, payload: GLib.Bytes
    ) -> Tuple[GLib.Bytes, int]: ...
    def process_outgoing_message(
        self, payload: GLib.Bytes
    ) -> Tuple[GLib.Bytes, int]: ...

class WebsocketExtensionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketExtensionClass()
    """

    parent_class: GObject.ObjectClass = ...
    name: str = ...
    configure: Callable[
        [WebsocketExtension, WebsocketConnectionType, Optional[dict[None, None]]], bool
    ] = ...
    get_request_params: Callable[[WebsocketExtension], Optional[str]] = ...
    get_response_params: Callable[[WebsocketExtension], Optional[str]] = ...
    process_outgoing_message: Callable[
        [WebsocketExtension, GLib.Bytes], Tuple[GLib.Bytes, int]
    ] = ...
    process_incoming_message: Callable[
        [WebsocketExtension, GLib.Bytes], Tuple[GLib.Bytes, int]
    ] = ...
    _libsoup_reserved1: None = ...
    _libsoup_reserved2: None = ...
    _libsoup_reserved3: None = ...
    _libsoup_reserved4: None = ...

class WebsocketExtensionDeflate(WebsocketExtension):
    """
    :Constructors:

    ::

        WebsocketExtensionDeflate(**properties)

    Object SoupWebsocketExtensionDeflate

    Signals from GObject:
      notify (GParam)
    """

    parent: WebsocketExtension = ...

class WebsocketExtensionDeflateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketExtensionDeflateClass()
    """

    parent_class: WebsocketExtensionClass = ...

class WebsocketExtensionManager(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        WebsocketExtensionManager(**properties)

    Object SoupWebsocketExtensionManager

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...

class WebsocketExtensionManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketExtensionManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class XMLRPCParams(GObject.GPointer):
    def free(self) -> None: ...
    def parse(self, signature: Optional[str] = None) -> GLib.Variant: ...

class Cacheability(GObject.GFlags):
    CACHEABLE = 1
    INVALIDATES = 4
    UNCACHEABLE = 2
    VALIDATES = 8

class Expectation(GObject.GFlags):
    CONTINUE = 2
    UNRECOGNIZED = 1

class MessageFlags(GObject.GFlags):
    CAN_REBUILD = 4
    CERTIFICATE_TRUSTED = 32
    CONTENT_DECODED = 16
    DO_NOT_USE_AUTH_CACHE = 512
    IDEMPOTENT = 128
    IGNORE_CONNECTION_LIMITS = 256
    NEW_CONNECTION = 64
    NO_REDIRECT = 2
    OVERWRITE_CHUNKS = 8

class ServerListenOptions(GObject.GFlags):
    HTTPS = 1
    IPV4_ONLY = 2
    IPV6_ONLY = 4

class AddressFamily(GObject.GEnum):
    INVALID = -1
    IPV4 = 2
    IPV6 = 10

class CacheResponse(GObject.GEnum):
    FRESH = 0
    NEEDS_VALIDATION = 1
    STALE = 2

class CacheType(GObject.GEnum):
    SHARED = 1
    SINGLE_USER = 0

class ConnectionState(GObject.GEnum):
    CONNECTING = 1
    DISCONNECTED = 5
    IDLE = 2
    IN_USE = 3
    NEW = 0
    REMOTE_DISCONNECTED = 4

class CookieJarAcceptPolicy(GObject.GEnum):
    ALWAYS = 0
    GRANDFATHERED_THIRD_PARTY = 3
    NEVER = 1
    NO_THIRD_PARTY = 2

class DateFormat(GObject.GEnum):
    COOKIE = 2
    HTTP = 1
    ISO8601 = 5
    ISO8601_COMPACT = 4
    ISO8601_FULL = 5
    ISO8601_XMLRPC = 6
    RFC2822 = 3

class Encoding(GObject.GEnum):
    BYTERANGES = 5
    CHUNKED = 4
    CONTENT_LENGTH = 2
    EOF = 3
    NONE = 1
    UNRECOGNIZED = 0

class HTTPVersion(GObject.GEnum):
    HTTP_1_0 = 0
    HTTP_1_1 = 1

class KnownStatusCode(GObject.GEnum):
    ACCEPTED = 202
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
    CANCELLED = 1
    CANT_CONNECT = 4
    CANT_CONNECT_PROXY = 5
    CANT_RESOLVE = 2
    CANT_RESOLVE_PROXY = 3
    CONFLICT = 409
    CONTINUE = 100
    CREATED = 201
    EXPECTATION_FAILED = 417
    FAILED_DEPENDENCY = 424
    FORBIDDEN = 403
    FOUND = 302
    GATEWAY_TIMEOUT = 504
    GONE = 410
    HTTP_VERSION_NOT_SUPPORTED = 505
    INSUFFICIENT_STORAGE = 507
    INTERNAL_SERVER_ERROR = 500
    INVALID_RANGE = 416
    IO_ERROR = 7
    LENGTH_REQUIRED = 411
    LOCKED = 423
    MALFORMED = 8
    METHOD_NOT_ALLOWED = 405
    MOVED_PERMANENTLY = 301
    MOVED_TEMPORARILY = 302
    MULTIPLE_CHOICES = 300
    MULTI_STATUS = 207
    NONE = 0
    NON_AUTHORITATIVE = 203
    NOT_ACCEPTABLE = 406
    NOT_APPEARING_IN_THIS_PROTOCOL = 306
    NOT_EXTENDED = 510
    NOT_FOUND = 404
    NOT_IMPLEMENTED = 501
    NOT_MODIFIED = 304
    NO_CONTENT = 204
    OK = 200
    PARTIAL_CONTENT = 206
    PAYMENT_REQUIRED = 402
    PRECONDITION_FAILED = 412
    PROCESSING = 102
    PROXY_AUTHENTICATION_REQUIRED = 407
    PROXY_UNAUTHORIZED = 407
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_TIMEOUT = 408
    REQUEST_URI_TOO_LONG = 414
    RESET_CONTENT = 205
    SEE_OTHER = 303
    SERVICE_UNAVAILABLE = 503
    SSL_FAILED = 6
    SWITCHING_PROTOCOLS = 101
    TEMPORARY_REDIRECT = 307
    TLS_FAILED = 11
    TOO_MANY_REDIRECTS = 10
    TRY_AGAIN = 9
    UNAUTHORIZED = 401
    UNPROCESSABLE_ENTITY = 422
    UNSUPPORTED_MEDIA_TYPE = 415
    USE_PROXY = 305

class LoggerLogLevel(GObject.GEnum):
    BODY = 3
    HEADERS = 2
    MINIMAL = 1
    NONE = 0

class MemoryUse(GObject.GEnum):
    COPY = 2
    STATIC = 0
    TAKE = 1
    TEMPORARY = 3

class MessageHeadersType(GObject.GEnum):
    MULTIPART = 2
    REQUEST = 0
    RESPONSE = 1

class MessagePriority(GObject.GEnum):
    HIGH = 3
    LOW = 1
    NORMAL = 2
    VERY_HIGH = 4
    VERY_LOW = 0

class RequestError(GObject.GEnum):
    BAD_URI = 0
    ENCODING = 3
    PARSING = 2
    UNSUPPORTED_URI_SCHEME = 1
    @staticmethod
    def quark() -> int: ...

class RequesterError(GObject.GEnum):
    BAD_URI = 0
    UNSUPPORTED_URI_SCHEME = 1
    @staticmethod
    def quark() -> int: ...

class SameSitePolicy(GObject.GEnum):
    LAX = 1
    NONE = 0
    STRICT = 2

class SocketIOStatus(GObject.GEnum):
    EOF = 2
    ERROR = 3
    OK = 0
    WOULD_BLOCK = 1

class Status(GObject.GEnum):
    ACCEPTED = 202
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
    CANCELLED = 1
    CANT_CONNECT = 4
    CANT_CONNECT_PROXY = 5
    CANT_RESOLVE = 2
    CANT_RESOLVE_PROXY = 3
    CONFLICT = 409
    CONTINUE = 100
    CREATED = 201
    EXPECTATION_FAILED = 417
    FAILED_DEPENDENCY = 424
    FORBIDDEN = 403
    FOUND = 302
    GATEWAY_TIMEOUT = 504
    GONE = 410
    HTTP_VERSION_NOT_SUPPORTED = 505
    INSUFFICIENT_STORAGE = 507
    INTERNAL_SERVER_ERROR = 500
    INVALID_RANGE = 416
    IO_ERROR = 7
    LENGTH_REQUIRED = 411
    LOCKED = 423
    MALFORMED = 8
    METHOD_NOT_ALLOWED = 405
    MOVED_PERMANENTLY = 301
    MOVED_TEMPORARILY = 302
    MULTIPLE_CHOICES = 300
    MULTI_STATUS = 207
    NONE = 0
    NON_AUTHORITATIVE = 203
    NOT_ACCEPTABLE = 406
    NOT_APPEARING_IN_THIS_PROTOCOL = 306
    NOT_EXTENDED = 510
    NOT_FOUND = 404
    NOT_IMPLEMENTED = 501
    NOT_MODIFIED = 304
    NO_CONTENT = 204
    OK = 200
    PARTIAL_CONTENT = 206
    PAYMENT_REQUIRED = 402
    PERMANENT_REDIRECT = 308
    PRECONDITION_FAILED = 412
    PROCESSING = 102
    PROXY_AUTHENTICATION_REQUIRED = 407
    PROXY_UNAUTHORIZED = 407
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_TIMEOUT = 408
    REQUEST_URI_TOO_LONG = 414
    RESET_CONTENT = 205
    SEE_OTHER = 303
    SERVICE_UNAVAILABLE = 503
    SSL_FAILED = 6
    SWITCHING_PROTOCOLS = 101
    TEMPORARY_REDIRECT = 307
    TLS_FAILED = 11
    TOO_MANY_REDIRECTS = 10
    TRY_AGAIN = 9
    UNAUTHORIZED = 401
    UNPROCESSABLE_ENTITY = 422
    UNSUPPORTED_MEDIA_TYPE = 415
    USE_PROXY = 305
    @staticmethod
    def get_phrase(status_code: int) -> str: ...
    @staticmethod
    def proxify(status_code: int) -> int: ...

class TLDError(GObject.GEnum):
    INVALID_HOSTNAME = 0
    IS_IP_ADDRESS = 1
    NOT_ENOUGH_DOMAINS = 2
    NO_BASE_DOMAIN = 3
    NO_PSL_DATA = 4
    @staticmethod
    def quark() -> int: ...

class WebsocketCloseCode(GObject.GEnum):
    ABNORMAL = 1006
    BAD_DATA = 1007
    GOING_AWAY = 1001
    NORMAL = 1000
    NO_EXTENSION = 1010
    NO_STATUS = 1005
    POLICY_VIOLATION = 1008
    PROTOCOL_ERROR = 1002
    SERVER_ERROR = 1011
    TLS_HANDSHAKE = 1015
    TOO_BIG = 1009
    UNSUPPORTED_DATA = 1003

class WebsocketConnectionType(GObject.GEnum):
    CLIENT = 1
    SERVER = 2
    UNKNOWN = 0

class WebsocketDataType(GObject.GEnum):
    BINARY = 2
    TEXT = 1

class WebsocketError(GObject.GEnum):
    BAD_HANDSHAKE = 2
    BAD_ORIGIN = 3
    FAILED = 0
    NOT_WEBSOCKET = 1
    @staticmethod
    def get_quark() -> int: ...

class WebsocketState(GObject.GEnum):
    CLOSED = 3
    CLOSING = 2
    OPEN = 1

class XMLRPCError(GObject.GEnum):
    ARGUMENTS = 0
    RETVAL = 1
    @staticmethod
    def quark() -> int: ...

class XMLRPCFault(GObject.GEnum):
    APPLICATION_ERROR = -32500
    PARSE_ERROR_INVALID_CHARACTER_FOR_ENCODING = -32702
    PARSE_ERROR_NOT_WELL_FORMED = -32700
    PARSE_ERROR_UNSUPPORTED_ENCODING = -32701
    SERVER_ERROR_INTERNAL_XML_RPC_ERROR = -32603
    SERVER_ERROR_INVALID_METHOD_PARAMETERS = -32602
    SERVER_ERROR_INVALID_XML_RPC = -32600
    SERVER_ERROR_REQUESTED_METHOD_NOT_FOUND = -32601
    SYSTEM_ERROR = -32400
    TRANSPORT_ERROR = -32300
    @staticmethod
    def quark() -> int: ...
