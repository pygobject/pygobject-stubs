import typing

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

T = typing.TypeVar("T")

COOKIE_MAX_AGE_ONE_DAY: int = 0
COOKIE_MAX_AGE_ONE_HOUR: int = 3600
COOKIE_MAX_AGE_ONE_WEEK: int = 0
COOKIE_MAX_AGE_ONE_YEAR: int = 0
FORM_MIME_TYPE_MULTIPART: str = "multipart/form-data"
FORM_MIME_TYPE_URLENCODED: str = "application/x-www-form-urlencoded"
HSTS_POLICY_MAX_AGE_PAST: int = 0
HTTP_URI_FLAGS: int = 482
MAJOR_VERSION: int = 3
MICRO_VERSION: int = 5
MINOR_VERSION: int = 6
VERSION_MIN_REQUIRED: int = 2
_lock = ...  # FIXME Constant
_namespace: str = "Soup"
_version: str = "3.0"

def check_version(major: int, minor: int, micro: int) -> bool: ...
def cookie_parse(
    header: str, origin: typing.Optional[GLib.Uri] = None
) -> typing.Optional[Cookie]: ...
def cookies_from_request(msg: Message) -> list[Cookie]: ...
def cookies_from_response(msg: Message) -> list[Cookie]: ...
def cookies_to_cookie_header(cookies: list[Cookie]) -> str: ...
def cookies_to_request(cookies: list[Cookie], msg: Message) -> None: ...
def cookies_to_response(cookies: list[Cookie], msg: Message) -> None: ...
def date_time_new_from_http_string(
    date_string: str,
) -> typing.Optional[GLib.DateTime]: ...
def date_time_to_string(date: GLib.DateTime, format: DateFormat) -> str: ...
def form_decode(encoded_form: str) -> dict[str, str]: ...
def form_decode_multipart(
    multipart: Multipart, file_control_name: typing.Optional[str] = None
) -> typing.Tuple[typing.Optional[dict[str, str]], str, str, GLib.Bytes]: ...
def form_encode_datalist(form_data_set: GLib.Data) -> str: ...
def form_encode_hash(form_data_set: dict[str, str]) -> str: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def header_contains(header: str, token: str) -> bool: ...
def header_free_param_list(param_list: dict[str, str]) -> None: ...
def header_g_string_append_param(
    string: GLib.String, name: str, value: typing.Optional[str] = None
) -> None: ...
def header_g_string_append_param_quoted(
    string: GLib.String, name: str, value: str
) -> None: ...
def header_parse_list(header: str) -> list[str]: ...
def header_parse_param_list(header: str) -> dict[str, str]: ...
def header_parse_param_list_strict(header: str) -> typing.Optional[dict[str, str]]: ...
def header_parse_quality_list(header: str) -> typing.Tuple[list[str], list[str]]: ...
def header_parse_semi_param_list(header: str) -> dict[str, str]: ...
def header_parse_semi_param_list_strict(
    header: str,
) -> typing.Optional[dict[str, str]]: ...
def headers_parse(str: str, len: int, dest: MessageHeaders) -> bool: ...
def headers_parse_request(
    str: str, len: int, req_headers: MessageHeaders
) -> typing.Tuple[int, str, str, HTTPVersion]: ...
def headers_parse_response(
    str: str, len: int, headers: MessageHeaders
) -> typing.Tuple[bool, HTTPVersion, int, str]: ...
def headers_parse_status_line(
    status_line: str,
) -> typing.Tuple[bool, HTTPVersion, int, str]: ...
def message_headers_iter_init(hdrs: MessageHeaders) -> MessageHeadersIter: ...
def message_headers_iter_next() -> typing.Tuple[bool, MessageHeadersIter, str, str]: ...
def session_error_quark() -> int: ...
def status_get_phrase(status_code: int) -> str: ...
def tld_domain_is_public_suffix(domain: str) -> bool: ...
def tld_error_quark() -> int: ...
def tld_get_base_domain(hostname: str) -> str: ...

# override
def uri_decode_data_uri(
    uri: str,
) -> typing.Tuple[typing.Optional[GLib.Bytes], typing.Optional[str]]: ...
def uri_equal(uri1: GLib.Uri, uri2: GLib.Uri) -> bool: ...
def websocket_client_prepare_handshake(
    msg: Message,
    origin: typing.Optional[str] = None,
    protocols: typing.Optional[typing.Sequence[str]] = None,
    supported_extensions: typing.Optional[typing.Sequence[GObject.TypeClass]] = None,
) -> None: ...
def websocket_client_verify_handshake(
    msg: Message,
    supported_extensions: typing.Optional[typing.Sequence[GObject.TypeClass]] = None,
) -> typing.Tuple[bool, list[WebsocketExtension]]: ...
def websocket_error_quark() -> int: ...
def websocket_server_check_handshake(
    msg: ServerMessage,
    origin: typing.Optional[str] = None,
    protocols: typing.Optional[typing.Sequence[str]] = None,
    supported_extensions: typing.Optional[typing.Sequence[GObject.TypeClass]] = None,
) -> bool: ...
def websocket_server_process_handshake(
    msg: ServerMessage,
    expected_origin: typing.Optional[str] = None,
    protocols: typing.Optional[typing.Sequence[str]] = None,
    supported_extensions: typing.Optional[typing.Sequence[GObject.TypeClass]] = None,
) -> typing.Tuple[bool, list[WebsocketExtension]]: ...

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
      authority -> gchararray: Authority
        Authentication authority
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated
      is-cancelled -> gboolean: Cancelled
        Whether or not the auth is cancelled

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        authority: str
        is_authenticated: bool
        is_cancelled: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self, authority: str = ..., is_for_proxy: bool = ..., realm: str = ...
    ) -> None: ...
    def authenticate(self, username: str, password: str) -> None: ...
    def can_authenticate(self) -> bool: ...
    def cancel(self) -> None: ...
    def do_authenticate(self, username: str, password: str) -> None: ...
    def do_can_authenticate(self) -> bool: ...
    def do_get_authorization(self, msg: Message) -> str: ...
    def do_get_protection_space(self, source_uri: GLib.Uri) -> list[str]: ...
    def do_is_authenticated(self) -> bool: ...
    def do_is_ready(self, msg: Message) -> bool: ...
    def do_update(self, msg: Message, auth_header: dict[None, None]) -> bool: ...
    def get_authority(self) -> str: ...
    def get_authorization(self, msg: Message) -> str: ...
    def get_info(self) -> str: ...
    def get_protection_space(self, source_uri: GLib.Uri) -> list[str]: ...
    def get_realm(self) -> str: ...
    def get_scheme_name(self) -> str: ...
    def is_authenticated(self) -> bool: ...
    def is_cancelled(self) -> bool: ...
    def is_for_proxy(self) -> bool: ...
    def is_ready(self, msg: Message) -> bool: ...
    @classmethod
    def new(
        cls, type: typing.Type[typing.Any], msg: Message, auth_header: str
    ) -> typing.Optional[Auth]: ...
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
      authority -> gchararray: Authority
        Authentication authority
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated
      is-cancelled -> gboolean: Cancelled
        Whether or not the auth is cancelled

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        authority: str
        is_authenticated: bool
        is_cancelled: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str

    props: Props = ...
    def __init__(
        self, authority: str = ..., is_for_proxy: bool = ..., realm: str = ...
    ) -> None: ...

class AuthClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthClass()
    """

    parent_class: GObject.ObjectClass = ...
    scheme_name: str = ...
    strength: int = ...
    update: typing.Callable[[Auth, Message, dict[None, None]], bool] = ...
    get_protection_space: typing.Callable[[Auth, GLib.Uri], list[str]] = ...
    authenticate: typing.Callable[[Auth, str, str], None] = ...
    is_authenticated: typing.Callable[[Auth], bool] = ...
    get_authorization: typing.Callable[[Auth, Message], str] = ...
    is_ready: typing.Callable[[Auth, Message], bool] = ...
    can_authenticate: typing.Callable[[Auth], bool] = ...
    padding: list[None] = ...

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
      authority -> gchararray: Authority
        Authentication authority
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated
      is-cancelled -> gboolean: Cancelled
        Whether or not the auth is cancelled

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        authority: str
        is_authenticated: bool
        is_cancelled: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str

    props: Props = ...
    def __init__(
        self, authority: str = ..., is_for_proxy: bool = ..., realm: str = ...
    ) -> None: ...

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

    # override
    class Props:
        filter: typing.Callable[..., bool]
        filter_data: None
        generic_auth_callback: typing.Callable[..., bool]
        generic_auth_data: None
        proxy: bool
        realm: str

    # override
    props: Props = ...
    parent_instance: GObject.Object = ...
    # override
    def __init__(
        self,
        filter: typing.Callable[..., bool] = ...,
        filter_data: None = ...,
        generic_auth_callback: typing.Callable[..., bool] = ...,
        generic_auth_data: None = ...,
        proxy: bool = ...,
        realm: str = ...,
    ) -> None: ...
    def accepts(self, msg: ServerMessage) -> typing.Optional[str]: ...
    def add_path(self, path: str) -> None: ...
    def challenge(self, msg: ServerMessage) -> None: ...
    def check_password(
        self, msg: ServerMessage, username: str, password: str
    ) -> bool: ...
    def covers(self, msg: ServerMessage) -> bool: ...
    def do_accepts(self, msg: ServerMessage, header: str) -> str: ...
    def do_challenge(self, msg: ServerMessage) -> str: ...
    def do_check_password(
        self, msg: ServerMessage, username: str, password: str
    ) -> bool: ...
    def get_realm(self) -> str: ...
    def remove_path(self, path: str) -> None: ...
    def set_filter(
        self, filter: typing.Callable[..., bool], *filter_data: typing.Any
    ) -> None: ...
    def set_generic_auth_callback(
        self, auth_callback: typing.Callable[..., bool], *auth_data: typing.Any
    ) -> None: ...

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

    # override
    class Props:
        auth_callback: typing.Callable[..., bool]
        auth_data: None
        filter: typing.Callable[..., bool]
        filter_data: None
        generic_auth_callback: typing.Callable[..., bool]
        generic_auth_data: None
        proxy: bool
        realm: str

    # override
    props: Props = ...
    # override
    def __init__(
        self,
        auth_callback: typing.Callable[..., bool] = ...,
        auth_data: None = ...,
        filter: typing.Callable[..., bool] = ...,
        filter_data: None = ...,
        generic_auth_callback: typing.Callable[..., bool] = ...,
        generic_auth_data: None = ...,
        proxy: bool = ...,
        realm: str = ...,
    ) -> None: ...
    def set_auth_callback(
        self, callback: typing.Callable[..., bool], *user_data: typing.Any
    ) -> None: ...

class AuthDomainBasicClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthDomainBasicClass()
    """

    parent_class: AuthDomainClass = ...

class AuthDomainClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthDomainClass()
    """

    parent_class: GObject.ObjectClass = ...
    accepts: typing.Callable[[AuthDomain, ServerMessage, str], str] = ...
    challenge: typing.Callable[[AuthDomain, ServerMessage], str] = ...
    check_password: typing.Callable[[AuthDomain, ServerMessage, str, str], bool] = ...
    padding: list[None] = ...

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

    # override
    class Props:
        auth_callback: typing.Callable[..., typing.Optional[str]]
        auth_data: None
        filter: typing.Callable[..., bool]
        filter_data: None
        generic_auth_callback: typing.Callable[..., bool]
        generic_auth_data: None
        proxy: bool
        realm: str

    # override
    props: Props = ...
    # override
    def __init__(
        self,
        auth_callback: typing.Callable[..., typing.Optional[str]] = ...,
        auth_data: None = ...,
        filter: typing.Callable[..., bool] = ...,
        filter_data: None = ...,
        generic_auth_callback: typing.Callable[..., bool] = ...,
        generic_auth_data: None = ...,
        proxy: bool = ...,
        realm: str = ...,
    ) -> None: ...
    @staticmethod
    def encode_password(username: str, realm: str, password: str) -> str: ...
    def set_auth_callback(
        self,
        callback: typing.Callable[..., typing.Optional[str]],
        *user_data: typing.Any,
    ) -> None: ...

class AuthDomainDigestClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthDomainDigestClass()
    """

    parent_class: AuthDomainClass = ...

class AuthManager(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        AuthManager(**properties)

    Object SoupAuthManager

    Signals from GObject:
      notify (GParam)
    """

    def clear_cached_credentials(self) -> None: ...
    def use_auth(self, uri: GLib.Uri, auth: Auth) -> None: ...

class AuthManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AuthManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

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
      authority -> gchararray: Authority
        Authentication authority
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated
      is-cancelled -> gboolean: Cancelled
        Whether or not the auth is cancelled

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        authority: str
        is_authenticated: bool
        is_cancelled: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str

    props: Props = ...
    def __init__(
        self, authority: str = ..., is_for_proxy: bool = ..., realm: str = ...
    ) -> None: ...

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
      authority -> gchararray: Authority
        Authentication authority
      is-for-proxy -> gboolean: For Proxy
        Whether or not the auth is for a proxy server
      is-authenticated -> gboolean: Authenticated
        Whether or not the auth is authenticated
      is-cancelled -> gboolean: Cancelled
        Whether or not the auth is cancelled

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        authority: str
        is_authenticated: bool
        is_cancelled: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str

    props: Props = ...
    def __init__(
        self, authority: str = ..., is_for_proxy: bool = ..., realm: str = ...
    ) -> None: ...
    @staticmethod
    def supported() -> bool: ...

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
    def __init__(self, cache_dir: str = ..., cache_type: CacheType = ...) -> None: ...
    def clear(self) -> None: ...
    def do_get_cacheability(self, msg: Message) -> Cacheability: ...
    def dump(self) -> None: ...
    def flush(self) -> None: ...
    def get_max_size(self) -> int: ...
    def load(self) -> None: ...
    @classmethod
    def new(cls, cache_dir: typing.Optional[str], cache_type: CacheType) -> Cache: ...
    def set_max_size(self, max_size: int) -> None: ...

class CacheClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CacheClass()
    """

    parent_class: GObject.ObjectClass = ...
    get_cacheability: typing.Callable[[Cache, Message], Cacheability] = ...
    padding: list[None] = ...

class ContentDecoder(GObject.Object, SessionFeature): ...

class ContentDecoderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentDecoderClass()
    """

    parent_class: GObject.ObjectClass = ...

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

    @classmethod
    def new(cls) -> ContentSniffer: ...
    def sniff(
        self, msg: Message, buffer: GLib.Bytes
    ) -> typing.Tuple[str, dict[str, str]]: ...

class ContentSnifferClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentSnifferClass()
    """

    parent_class: GObject.ObjectClass = ...

class Cookie(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(name:str, value:str, domain:str, path:str, max_age:int) -> Soup.Cookie
    """

    def applies_to_uri(self, uri: GLib.Uri) -> bool: ...
    def copy(self) -> Cookie: ...
    def domain_matches(self, host: str) -> bool: ...
    def equal(self, cookie2: Cookie) -> bool: ...
    def free(self) -> None: ...
    def get_domain(self) -> str: ...
    def get_expires(self) -> typing.Optional[GLib.DateTime]: ...
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
    def parse(
        header: str, origin: typing.Optional[GLib.Uri] = None
    ) -> typing.Optional[Cookie]: ...
    def set_domain(self, domain: str) -> None: ...
    def set_expires(self, expires: GLib.DateTime) -> None: ...
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
    parent_instance: GObject.Object = ...
    def __init__(
        self, accept_policy: CookieJarAcceptPolicy = ..., read_only: bool = ...
    ) -> None: ...
    def add_cookie(self, cookie: Cookie) -> None: ...
    def add_cookie_full(
        self,
        cookie: Cookie,
        uri: typing.Optional[GLib.Uri] = None,
        first_party: typing.Optional[GLib.Uri] = None,
    ) -> None: ...
    def add_cookie_with_first_party(
        self, first_party: GLib.Uri, cookie: Cookie
    ) -> None: ...
    def all_cookies(self) -> list[Cookie]: ...
    def delete_cookie(self, cookie: Cookie) -> None: ...
    def do_changed(self, old_cookie: Cookie, new_cookie: Cookie) -> None: ...
    def do_is_persistent(self) -> bool: ...
    def do_save(self) -> None: ...
    def get_accept_policy(self) -> CookieJarAcceptPolicy: ...
    def get_cookie_list(self, uri: GLib.Uri, for_http: bool) -> list[Cookie]: ...
    def get_cookie_list_with_same_site_info(
        self,
        uri: GLib.Uri,
        top_level: typing.Optional[GLib.Uri],
        site_for_cookies: typing.Optional[GLib.Uri],
        for_http: bool,
        is_safe_method: bool,
        is_top_level_navigation: bool,
    ) -> list[Cookie]: ...
    def get_cookies(self, uri: GLib.Uri, for_http: bool) -> typing.Optional[str]: ...
    def is_persistent(self) -> bool: ...
    @classmethod
    def new(cls) -> CookieJar: ...
    def set_accept_policy(self, policy: CookieJarAcceptPolicy) -> None: ...
    def set_cookie(self, uri: GLib.Uri, cookie: str) -> None: ...
    def set_cookie_with_first_party(
        self, uri: GLib.Uri, first_party: GLib.Uri, cookie: str
    ) -> None: ...

class CookieJarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieJarClass()
    """

    parent_class: GObject.ObjectClass = ...
    save: typing.Callable[[CookieJar], None] = ...
    is_persistent: typing.Callable[[CookieJar], bool] = ...
    changed: typing.Callable[[CookieJar, Cookie, Cookie], None] = ...
    padding: list[None] = ...

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
    def __init__(
        self,
        filename: str = ...,
        accept_policy: CookieJarAcceptPolicy = ...,
        read_only: bool = ...,
    ) -> None: ...
    @classmethod
    def new(cls, filename: str, read_only: bool) -> CookieJarDB: ...

class CookieJarDBClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieJarDBClass()
    """

    parent_class: CookieJarClass = ...

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
    def __init__(
        self,
        filename: str = ...,
        accept_policy: CookieJarAcceptPolicy = ...,
        read_only: bool = ...,
    ) -> None: ...
    @classmethod
    def new(cls, filename: str, read_only: bool) -> CookieJarText: ...

class CookieJarTextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        CookieJarTextClass()
    """

    parent_class: CookieJarClass = ...

class HSTSEnforcer(GObject.Object, SessionFeature):
    """
    :Constructors:

    ::

        HSTSEnforcer(**properties)
        new() -> Soup.HSTSEnforcer

    Object SoupHSTSEnforcer

    Signals from SoupHSTSEnforcer:
      changed (SoupHSTSPolicy, SoupHSTSPolicy)

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def do_changed(self, old_policy: HSTSPolicy, new_policy: HSTSPolicy) -> None: ...
    def do_has_valid_policy(self, domain: str) -> bool: ...
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
    is_persistent: typing.Callable[[HSTSEnforcer], bool] = ...
    has_valid_policy: typing.Callable[[HSTSEnforcer, str], bool] = ...
    changed: typing.Callable[[HSTSEnforcer, HSTSPolicy, HSTSPolicy], None] = ...
    padding: list[None] = ...

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

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        filename: str

    props: Props = ...
    def __init__(self, filename: str = ...) -> None: ...
    @classmethod
    def new(cls, filename: str) -> HSTSEnforcerDB: ...

class HSTSEnforcerDBClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HSTSEnforcerDBClass()
    """

    parent_class: HSTSEnforcerClass = ...

class HSTSPolicy(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(domain:str, max_age:int, include_subdomains:bool) -> Soup.HSTSPolicy
        new_from_response(msg:Soup.Message) -> Soup.HSTSPolicy or None
        new_full(domain:str, max_age:int, expires:GLib.DateTime, include_subdomains:bool) -> Soup.HSTSPolicy
        new_session_policy(domain:str, include_subdomains:bool) -> Soup.HSTSPolicy
    """

    def copy(self) -> HSTSPolicy: ...
    def equal(self, policy2: HSTSPolicy) -> bool: ...
    def free(self) -> None: ...
    def get_domain(self) -> str: ...
    def get_expires(self) -> GLib.DateTime: ...
    def get_max_age(self) -> int: ...
    def includes_subdomains(self) -> bool: ...
    def is_expired(self) -> bool: ...
    def is_session_policy(self) -> bool: ...
    @classmethod
    def new(cls, domain: str, max_age: int, include_subdomains: bool) -> HSTSPolicy: ...
    @classmethod
    def new_from_response(cls, msg: Message) -> typing.Optional[HSTSPolicy]: ...
    @classmethod
    def new_full(
        cls, domain: str, max_age: int, expires: GLib.DateTime, include_subdomains: bool
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
        new(level:Soup.LoggerLogLevel) -> Soup.Logger

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
    def __init__(
        self, level: LoggerLogLevel = ..., max_body_size: int = ...
    ) -> None: ...
    def get_max_body_size(self) -> int: ...
    @classmethod
    def new(cls, level: LoggerLogLevel) -> Logger: ...
    def set_max_body_size(self, max_body_size: int) -> None: ...
    def set_printer(
        self, printer: typing.Callable[..., None], *printer_data: typing.Any
    ) -> None: ...
    def set_request_filter(
        self,
        request_filter: typing.Callable[..., LoggerLogLevel],
        *filter_data: typing.Any,
    ) -> None: ...
    def set_response_filter(
        self,
        response_filter: typing.Callable[..., LoggerLogLevel],
        *filter_data: typing.Any,
    ) -> None: ...

class LoggerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LoggerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Message(GObject.Object):
    """
    :Constructors:

    ::

        Message(**properties)
        new(method:str, uri_string:str) -> Soup.Message or None
        new_from_encoded_form(method:str, uri_string:str, encoded_form:str) -> Soup.Message or None
        new_from_multipart(uri_string:str, multipart:Soup.Multipart) -> Soup.Message or None
        new_from_uri(method:str, uri:GLib.Uri) -> Soup.Message
        new_options_ping(base_uri:GLib.Uri) -> Soup.Message

    Object SoupMessage

    Signals from SoupMessage:
      wrote-headers ()
      wrote-body-data (guint)
      wrote-body ()
      got-informational ()
      got-headers ()
      got-body-data (guint)
      got-body ()
      content-sniffed (gchararray, GHashTable)
      starting ()
      restarted ()
      finished ()
      authenticate (SoupAuth, gboolean) -> gboolean
      network-event (GSocketClientEvent, GIOStream)
      accept-certificate (GTlsCertificate, GTlsCertificateFlags) -> gboolean
      request-certificate (GTlsClientConnection) -> gboolean
      request-certificate-password (GTlsPassword) -> gboolean
      hsts-enforced ()

    Properties from SoupMessage:
      method -> gchararray: Method
        The message's HTTP method
      uri -> GUri: URI
        The message's Request-URI
      http-version -> SoupHTTPVersion: HTTP Version
        The HTTP protocol version to use
      flags -> SoupMessageFlags: Flags
        Various message options
      status-code -> guint: Status code
        The HTTP response status code
      reason-phrase -> gchararray: Reason phrase
        The HTTP response reason phrase
      first-party -> GUri: First party
        The URI loaded in the application when the message was requested.
      request-headers -> SoupMessageHeaders: Request Headers
        The HTTP request headers
      response-headers -> SoupMessageHeaders: Response Headers
        The HTTP response headers
      tls-peer-certificate -> GTlsCertificate: TLS Peer Certificate
        The TLS peer certificate associated with the message
      tls-peer-certificate-errors -> GTlsCertificateFlags: TLS Peer Certificate Errors
        The verification errors on the message's TLS peer certificate
      tls-protocol-version -> GTlsProtocolVersion: TLS Protocol Version
        TLS protocol version negotiated for this connection
      tls-ciphersuite-name -> gchararray: TLS Ciphersuite Name
        Name of TLS ciphersuite negotiated for this connection
      remote-address -> GSocketAddress: Remote Address
        The remote address of the connection associated with the message
      priority -> SoupMessagePriority: Priority
        The priority of the message
      site-for-cookies -> GUri: Site for cookies
        The URI for the site to compare cookies against
      is-top-level-navigation -> gboolean: Is top-level navigation
        If the current messsage is navigating between top-levels
      is-options-ping -> gboolean: Is Options Ping
        The message is an OPTIONS ping

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        first_party: GLib.Uri
        flags: MessageFlags
        http_version: HTTPVersion
        is_options_ping: bool
        is_top_level_navigation: bool
        method: str
        priority: MessagePriority
        reason_phrase: typing.Optional[str]
        remote_address: typing.Optional[Gio.SocketAddress]
        request_headers: MessageHeaders
        response_headers: MessageHeaders
        site_for_cookies: GLib.Uri
        status_code: int
        tls_ciphersuite_name: str
        tls_peer_certificate: typing.Optional[Gio.TlsCertificate]
        tls_peer_certificate_errors: Gio.TlsCertificateFlags
        tls_protocol_version: Gio.TlsProtocolVersion
        uri: GLib.Uri

    props: Props = ...
    def __init__(
        self,
        first_party: GLib.Uri = ...,
        flags: MessageFlags = ...,
        is_options_ping: bool = ...,
        is_top_level_navigation: bool = ...,
        method: str = ...,
        priority: MessagePriority = ...,
        site_for_cookies: typing.Optional[GLib.Uri] = ...,
        uri: GLib.Uri = ...,
    ) -> None: ...
    def add_flags(self, flags: MessageFlags) -> None: ...
    def disable_feature(self, feature_type: typing.Type[typing.Any]) -> None: ...
    def get_connection_id(self) -> int: ...
    def get_first_party(self) -> GLib.Uri: ...
    def get_flags(self) -> MessageFlags: ...
    def get_force_http1(self) -> bool: ...
    def get_http_version(self) -> HTTPVersion: ...
    def get_is_options_ping(self) -> bool: ...
    def get_is_top_level_navigation(self) -> bool: ...
    def get_method(self) -> str: ...
    def get_metrics(self) -> typing.Optional[MessageMetrics]: ...
    def get_priority(self) -> MessagePriority: ...
    def get_reason_phrase(self) -> typing.Optional[str]: ...
    def get_remote_address(self) -> typing.Optional[Gio.SocketAddress]: ...
    def get_request_headers(self) -> MessageHeaders: ...
    def get_response_headers(self) -> MessageHeaders: ...
    def get_site_for_cookies(self) -> GLib.Uri: ...
    def get_status(self) -> Status: ...
    def get_tls_ciphersuite_name(self) -> str: ...
    def get_tls_peer_certificate(self) -> typing.Optional[Gio.TlsCertificate]: ...
    def get_tls_peer_certificate_errors(self) -> Gio.TlsCertificateFlags: ...
    def get_tls_protocol_version(self) -> Gio.TlsProtocolVersion: ...
    def get_uri(self) -> GLib.Uri: ...
    def is_feature_disabled(self, feature_type: typing.Type[typing.Any]) -> bool: ...
    def is_keepalive(self) -> bool: ...
    @classmethod
    def new(cls, method: str, uri_string: str) -> typing.Optional[Message]: ...
    @classmethod
    def new_from_encoded_form(
        cls, method: str, uri_string: str, encoded_form: str
    ) -> typing.Optional[Message]: ...
    @classmethod
    def new_from_multipart(
        cls, uri_string: str, multipart: Multipart
    ) -> typing.Optional[Message]: ...
    @classmethod
    def new_from_uri(cls, method: str, uri: GLib.Uri) -> Message: ...
    @classmethod
    def new_options_ping(cls, base_uri: GLib.Uri) -> Message: ...
    def query_flags(self, flags: MessageFlags) -> bool: ...
    def remove_flags(self, flags: MessageFlags) -> None: ...
    def set_first_party(self, first_party: GLib.Uri) -> None: ...
    def set_flags(self, flags: MessageFlags) -> None: ...
    def set_force_http1(self, value: bool) -> None: ...
    def set_is_options_ping(self, is_options_ping: bool) -> None: ...
    def set_is_top_level_navigation(self, is_top_level_navigation: bool) -> None: ...
    def set_method(self, method: str) -> None: ...
    def set_priority(self, priority: MessagePriority) -> None: ...
    def set_request_body(
        self,
        content_type: typing.Optional[str],
        stream: typing.Optional[Gio.InputStream],
        content_length: int,
    ) -> None: ...
    def set_request_body_from_bytes(
        self,
        content_type: typing.Optional[str] = None,
        bytes: typing.Optional[GLib.Bytes] = None,
    ) -> None: ...
    def set_site_for_cookies(
        self, site_for_cookies: typing.Optional[GLib.Uri] = None
    ) -> None: ...
    def set_tls_client_certificate(
        self, certificate: typing.Optional[Gio.TlsCertificate] = None
    ) -> None: ...
    def set_uri(self, uri: GLib.Uri) -> None: ...
    def tls_client_certificate_password_request_complete(self) -> None: ...

class MessageBody(GObject.GBoxed):
    """
    :Constructors:

    ::

        MessageBody()
        new() -> Soup.MessageBody
    """

    data: bytes = ...
    length: int = ...
    def append(self, data: typing.Sequence[int]) -> None: ...
    def append_bytes(self, buffer: GLib.Bytes) -> None: ...
    def complete(self) -> None: ...
    def flatten(self) -> GLib.Bytes: ...
    def get_accumulate(self) -> bool: ...
    def get_chunk(self, offset: int) -> typing.Optional[GLib.Bytes]: ...
    def got_chunk(self, chunk: GLib.Bytes) -> None: ...
    @classmethod
    def new(cls) -> MessageBody: ...
    def ref(self) -> MessageBody: ...
    def set_accumulate(self, accumulate: bool) -> None: ...
    def truncate(self) -> None: ...
    def unref(self) -> None: ...
    def wrote_chunk(self, chunk: GLib.Bytes) -> None: ...

class MessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MessageClass()
    """

    parent_class: GObject.ObjectClass = ...

class MessageHeaders(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(type:Soup.MessageHeadersType) -> Soup.MessageHeaders
    """

    def append(self, name: str, value: str) -> None: ...
    def clean_connection_headers(self) -> None: ...
    def clear(self) -> None: ...
    def foreach(
        self, func: typing.Callable[..., None], *user_data: typing.Any
    ) -> None: ...
    def free_ranges(self, ranges: Range) -> None: ...
    def get_content_disposition(self) -> typing.Tuple[bool, str, dict[str, str]]: ...
    def get_content_length(self) -> int: ...
    def get_content_range(self) -> typing.Tuple[bool, int, int, int]: ...
    def get_content_type(
        self,
    ) -> typing.Tuple[typing.Optional[str], dict[str, str]]: ...
    def get_encoding(self) -> Encoding: ...
    def get_expectations(self) -> Expectation: ...
    def get_headers_type(self) -> MessageHeadersType: ...
    def get_list(self, name: str) -> typing.Optional[str]: ...
    def get_one(self, name: str) -> typing.Optional[str]: ...
    def get_ranges(self, total_length: int) -> typing.Tuple[bool, list[Range]]: ...
    def header_contains(self, name: str, token: str) -> bool: ...
    def header_equals(self, name: str, value: str) -> bool: ...
    @classmethod
    def new(cls, type: MessageHeadersType) -> MessageHeaders: ...
    def ref(self) -> MessageHeaders: ...
    def remove(self, name: str) -> None: ...
    def replace(self, name: str, value: str) -> None: ...
    def set_content_disposition(
        self, disposition: str, params: typing.Optional[dict[str, str]] = None
    ) -> None: ...
    def set_content_length(self, content_length: int) -> None: ...
    def set_content_range(self, start: int, end: int, total_length: int) -> None: ...
    def set_content_type(
        self, content_type: str, params: typing.Optional[dict[str, str]] = None
    ) -> None: ...
    def set_encoding(self, encoding: Encoding) -> None: ...
    def set_expectations(self, expectations: Expectation) -> None: ...
    def set_range(self, start: int, end: int) -> None: ...
    def set_ranges(self, ranges: Range, length: int) -> None: ...
    def unref(self) -> None: ...

class MessageHeadersIter(GObject.GPointer):
    """
    :Constructors:

    ::

        MessageHeadersIter()
    """

    dummy: list[None] = ...
    @staticmethod
    def init(hdrs: MessageHeaders) -> MessageHeadersIter: ...
    @staticmethod
    def next() -> typing.Tuple[bool, MessageHeadersIter, str, str]: ...

class MessageMetrics(GObject.GBoxed):
    def copy(self) -> MessageMetrics: ...
    def free(self) -> None: ...
    def get_connect_end(self) -> int: ...
    def get_connect_start(self) -> int: ...
    def get_dns_end(self) -> int: ...
    def get_dns_start(self) -> int: ...
    def get_fetch_start(self) -> int: ...
    def get_request_body_bytes_sent(self) -> int: ...
    def get_request_body_size(self) -> int: ...
    def get_request_header_bytes_sent(self) -> int: ...
    def get_request_start(self) -> int: ...
    def get_response_body_bytes_received(self) -> int: ...
    def get_response_body_size(self) -> int: ...
    def get_response_end(self) -> int: ...
    def get_response_header_bytes_received(self) -> int: ...
    def get_response_start(self) -> int: ...
    def get_tls_start(self) -> int: ...

class Multipart(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(mime_type:str) -> Soup.Multipart
        new_from_message(headers:Soup.MessageHeaders, body:GLib.Bytes) -> Soup.Multipart or None
    """

    def append_form_file(
        self,
        control_name: str,
        filename: typing.Optional[str],
        content_type: typing.Optional[str],
        body: GLib.Bytes,
    ) -> None: ...
    def append_form_string(self, control_name: str, data: str) -> None: ...
    def append_part(self, headers: MessageHeaders, body: GLib.Bytes) -> None: ...
    def free(self) -> None: ...
    def get_length(self) -> int: ...
    def get_part(self, part: int) -> typing.Tuple[bool, MessageHeaders, GLib.Bytes]: ...
    @classmethod
    def new(cls, mime_type: str) -> Multipart: ...
    @classmethod
    def new_from_message(
        cls, headers: MessageHeaders, body: GLib.Bytes
    ) -> typing.Optional[Multipart]: ...
    def to_message(self, dest_headers: MessageHeaders) -> GLib.Bytes: ...

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
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        message: Message
        base_stream: Gio.InputStream
        close_base_stream: bool

    props: Props = ...
    def __init__(
        self,
        message: Message = ...,
        base_stream: Gio.InputStream = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_headers(self) -> typing.Optional[MessageHeaders]: ...
    @classmethod
    def new(
        cls, msg: Message, base_stream: Gio.InputStream
    ) -> MultipartInputStream: ...
    def next_part(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Optional[Gio.InputStream]: ...
    def next_part_async(
        self,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *data: typing.Any,
    ) -> None: ...
    def next_part_finish(self, result: Gio.AsyncResult) -> Gio.InputStream: ...

class MultipartInputStreamClass(GObject.GPointer):
    """
    :Constructors:

    ::

        MultipartInputStreamClass()
    """

    parent_class: Gio.FilterInputStreamClass = ...

class Range(GObject.GPointer):
    """
    :Constructors:

    ::

        Range()
    """

    start: int = ...
    end: int = ...

class Server(GObject.Object):
    """
    :Constructors:

    ::

        Server(**properties)

    Object SoupServer

    Signals from SoupServer:
      request-started (SoupServerMessage)
      request-read (SoupServerMessage)
      request-finished (SoupServerMessage)
      request-aborted (SoupServerMessage)

    Properties from SoupServer:
      tls-certificate -> GTlsCertificate: TLS certificate
        GTlsCertificate to use for https
      tls-database -> GTlsDatabase: TLS database
        GTlsDatabase to use for validating SSL/TLS client certificates
      tls-auth-mode -> GTlsAuthenticationMode: TLS Authentication Mode
        GTlsAuthenticationMode to use for SSL/TLS client authentication
      raw-paths -> gboolean: Raw paths
        If %TRUE, percent-encoding in the Request-URI path will not be automatically decoded.
      server-header -> gchararray: Server header
        Server header

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        raw_paths: bool
        server_header: str
        tls_auth_mode: Gio.TlsAuthenticationMode
        tls_certificate: typing.Optional[Gio.TlsCertificate]
        tls_database: typing.Optional[Gio.TlsDatabase]

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        raw_paths: bool = ...,
        server_header: str = ...,
        tls_auth_mode: Gio.TlsAuthenticationMode = ...,
        tls_certificate: Gio.TlsCertificate = ...,
        tls_database: Gio.TlsDatabase = ...,
    ) -> None: ...
    def accept_iostream(
        self,
        stream: Gio.IOStream,
        local_addr: typing.Optional[Gio.SocketAddress] = None,
        remote_addr: typing.Optional[Gio.SocketAddress] = None,
    ) -> bool: ...
    def add_auth_domain(self, auth_domain: AuthDomain) -> None: ...
    def add_early_handler(
        self,
        path: typing.Optional[str],
        callback: typing.Callable[..., None],
        *user_data: typing.Any,
    ) -> None: ...
    def add_handler(
        self,
        path: typing.Optional[str],
        callback: typing.Callable[..., None],
        *user_data: typing.Any,
    ) -> None: ...
    def add_websocket_extension(
        self, extension_type: typing.Type[typing.Any]
    ) -> None: ...
    def add_websocket_handler(
        self,
        path: typing.Optional[str],
        origin: typing.Optional[str],
        protocols: typing.Optional[typing.Sequence[str]],
        callback: typing.Callable[..., None],
        *user_data: typing.Any,
    ) -> None: ...
    def disconnect(self) -> None: ...
    def do_request_aborted(self, msg: ServerMessage) -> None: ...
    def do_request_finished(self, msg: ServerMessage) -> None: ...
    def do_request_read(self, msg: ServerMessage) -> None: ...
    def do_request_started(self, msg: ServerMessage) -> None: ...
    def get_listeners(self) -> list[Gio.Socket]: ...
    def get_tls_auth_mode(self) -> Gio.TlsAuthenticationMode: ...
    def get_tls_certificate(self) -> typing.Optional[Gio.TlsCertificate]: ...
    def get_tls_database(self) -> typing.Optional[Gio.TlsDatabase]: ...
    def get_uris(self) -> list[GLib.Uri]: ...
    def is_https(self) -> bool: ...
    def listen(
        self, address: Gio.SocketAddress, options: ServerListenOptions
    ) -> bool: ...
    def listen_all(self, port: int, options: ServerListenOptions) -> bool: ...
    def listen_local(self, port: int, options: ServerListenOptions) -> bool: ...
    def listen_socket(
        self, socket: Gio.Socket, options: ServerListenOptions
    ) -> bool: ...
    def pause_message(self, msg: ServerMessage) -> None: ...
    def remove_auth_domain(self, auth_domain: AuthDomain) -> None: ...
    def remove_handler(self, path: str) -> None: ...
    def remove_websocket_extension(
        self, extension_type: typing.Type[typing.Any]
    ) -> None: ...
    def set_tls_auth_mode(self, mode: Gio.TlsAuthenticationMode) -> None: ...
    def set_tls_certificate(self, certificate: Gio.TlsCertificate) -> None: ...
    def set_tls_database(self, tls_database: Gio.TlsDatabase) -> None: ...
    def unpause_message(self, msg: ServerMessage) -> None: ...

class ServerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ServerClass()
    """

    parent_class: GObject.ObjectClass = ...
    request_started: typing.Callable[[Server, ServerMessage], None] = ...
    request_read: typing.Callable[[Server, ServerMessage], None] = ...
    request_finished: typing.Callable[[Server, ServerMessage], None] = ...
    request_aborted: typing.Callable[[Server, ServerMessage], None] = ...
    padding: list[None] = ...

class ServerMessage(GObject.Object):
    """
    :Constructors:

    ::

        ServerMessage(**properties)

    Object SoupServerMessage

    Signals from SoupServerMessage:
      wrote-headers ()
      wrote-body-data (guint)
      wrote-body ()
      got-headers ()
      got-body ()
      finished ()
      accept-certificate (GTlsCertificate, GTlsCertificateFlags) -> gboolean
      wrote-informational ()
      wrote-chunk ()
      got-chunk (GBytes)
      connected ()
      disconnected ()

    Properties from SoupServerMessage:
      tls-peer-certificate -> GTlsCertificate: TLS Peer Certificate
        The TLS peer certificate associated with the message
      tls-peer-certificate-errors -> GTlsCertificateFlags: TLS Peer Certificate Errors
        The verification errors on the message's TLS peer certificate

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        tls_peer_certificate: typing.Optional[Gio.TlsCertificate]
        tls_peer_certificate_errors: Gio.TlsCertificateFlags

    props: Props = ...
    def get_http_version(self) -> HTTPVersion: ...
    def get_local_address(self) -> typing.Optional[Gio.SocketAddress]: ...
    def get_method(self) -> str: ...
    def get_reason_phrase(self) -> typing.Optional[str]: ...
    def get_remote_address(self) -> typing.Optional[Gio.SocketAddress]: ...
    def get_remote_host(self) -> typing.Optional[str]: ...
    def get_request_body(self) -> MessageBody: ...
    def get_request_headers(self) -> MessageHeaders: ...
    def get_response_body(self) -> MessageBody: ...
    def get_response_headers(self) -> MessageHeaders: ...
    def get_socket(self) -> typing.Optional[Gio.Socket]: ...
    def get_status(self) -> int: ...
    def get_tls_peer_certificate(self) -> typing.Optional[Gio.TlsCertificate]: ...
    def get_tls_peer_certificate_errors(self) -> Gio.TlsCertificateFlags: ...
    def get_uri(self) -> GLib.Uri: ...
    def is_options_ping(self) -> bool: ...
    def pause(self) -> None: ...
    def set_http_version(self, version: HTTPVersion) -> None: ...
    def set_redirect(self, status_code: int, redirect_uri: str) -> None: ...
    def set_response(
        self,
        content_type: typing.Optional[str],
        resp_use: MemoryUse,
        resp_body: typing.Optional[typing.Sequence[int]] = None,
    ) -> None: ...
    def set_status(
        self, status_code: int, reason_phrase: typing.Optional[str] = None
    ) -> None: ...
    def steal_connection(self) -> Gio.IOStream: ...
    def unpause(self) -> None: ...

class ServerMessageClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ServerMessageClass()
    """

    parent_class: GObject.ObjectClass = ...

class Session(GObject.Object):
    """
    :Constructors:

    ::

        Session(**properties)
        new() -> Soup.Session

    Object SoupSession

    Signals from SoupSession:
      request-queued (SoupMessage)
      request-unqueued (SoupMessage)

    Properties from SoupSession:
      proxy-resolver -> GProxyResolver: Proxy Resolver
        The GProxyResolver to use for this session
      max-conns -> gint: Max Connection Count
        The maximum number of connections that the session can open at once
      max-conns-per-host -> gint: Max Per-Host Connection Count
        The maximum number of connections that the session can open at once to a given host
      tls-database -> GTlsDatabase: TLS Database
        TLS database to use
      timeout -> guint: Timeout value
        Value in seconds to timeout a blocking I/O
      user-agent -> gchararray: User-Agent string
        User-Agent string
      accept-language -> gchararray: Accept-Language string
        Accept-Language string
      accept-language-auto -> gboolean: Accept-Language automatic mode
        Accept-Language automatic mode
      remote-connectable -> GSocketConnectable: Remote Connectable
        Socket to connect to make outgoing connections on
      idle-timeout -> guint: Idle Timeout
        Connection lifetime when idle
      local-address -> GInetSocketAddress: Local address
        Address of local end of socket
      tls-interaction -> GTlsInteraction: TLS Interaction
        TLS interaction to use

    Signals from GObject:
      notify (GParam)
    """

    class Props:
        accept_language: typing.Optional[str]
        accept_language_auto: bool
        idle_timeout: int
        local_address: typing.Optional[Gio.InetSocketAddress]
        max_conns: int
        max_conns_per_host: int
        proxy_resolver: typing.Optional[Gio.ProxyResolver]
        remote_connectable: typing.Optional[Gio.SocketConnectable]
        timeout: int
        tls_database: typing.Optional[Gio.TlsDatabase]
        tls_interaction: typing.Optional[Gio.TlsInteraction]
        user_agent: typing.Optional[str]

    props: Props = ...
    parent_instance: GObject.Object = ...
    def __init__(
        self,
        accept_language: str = ...,
        accept_language_auto: bool = ...,
        idle_timeout: int = ...,
        local_address: Gio.InetSocketAddress = ...,
        max_conns: int = ...,
        max_conns_per_host: int = ...,
        proxy_resolver: typing.Optional[Gio.ProxyResolver] = ...,
        remote_connectable: Gio.SocketConnectable = ...,
        timeout: int = ...,
        tls_database: typing.Optional[Gio.TlsDatabase] = ...,
        tls_interaction: typing.Optional[Gio.TlsInteraction] = ...,
        user_agent: str = ...,
    ) -> None: ...
    def abort(self) -> None: ...
    def add_feature(self, feature: SessionFeature) -> None: ...
    def add_feature_by_type(self, feature_type: typing.Type[typing.Any]) -> None: ...
    def do_request_queued(self, msg: Message) -> None: ...
    def do_request_unqueued(self, msg: Message) -> None: ...
    def get_accept_language(self) -> typing.Optional[str]: ...
    def get_accept_language_auto(self) -> bool: ...
    def get_async_result_message(self, result: Gio.AsyncResult) -> Message: ...
    def get_feature(
        self, feature_type: typing.Type[typing.Any]
    ) -> typing.Optional[SessionFeature]: ...
    def get_feature_for_message(
        self, feature_type: typing.Type[typing.Any], msg: Message
    ) -> typing.Optional[SessionFeature]: ...
    def get_idle_timeout(self) -> int: ...
    def get_local_address(self) -> typing.Optional[Gio.InetSocketAddress]: ...
    def get_max_conns(self) -> int: ...
    def get_max_conns_per_host(self) -> int: ...
    def get_proxy_resolver(self) -> typing.Optional[Gio.ProxyResolver]: ...
    def get_remote_connectable(self) -> typing.Optional[Gio.SocketConnectable]: ...
    def get_timeout(self) -> int: ...
    def get_tls_database(self) -> typing.Optional[Gio.TlsDatabase]: ...
    def get_tls_interaction(self) -> typing.Optional[Gio.TlsInteraction]: ...
    def get_user_agent(self) -> typing.Optional[str]: ...
    def has_feature(self, feature_type: typing.Type[typing.Any]) -> bool: ...
    @classmethod
    def new(cls) -> Session: ...
    def preconnect_async(
        self,
        msg: Message,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def preconnect_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remove_feature(self, feature: SessionFeature) -> None: ...
    def remove_feature_by_type(self, feature_type: typing.Type[typing.Any]) -> None: ...
    def send(
        self, msg: Message, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> Gio.InputStream: ...
    def send_and_read(
        self, msg: Message, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> GLib.Bytes: ...
    def send_and_read_async(
        self,
        msg: Message,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def send_and_read_finish(self, result: Gio.AsyncResult) -> GLib.Bytes: ...
    def send_and_splice(
        self,
        msg: Message,
        out_stream: Gio.OutputStream,
        flags: Gio.OutputStreamSpliceFlags,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> int: ...
    def send_and_splice_async(
        self,
        msg: Message,
        out_stream: Gio.OutputStream,
        flags: Gio.OutputStreamSpliceFlags,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def send_and_splice_finish(self, result: Gio.AsyncResult) -> int: ...
    def send_async(
        self,
        msg: Message,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def send_finish(self, result: Gio.AsyncResult) -> Gio.InputStream: ...
    def set_accept_language(self, accept_language: str) -> None: ...
    def set_accept_language_auto(self, accept_language_auto: bool) -> None: ...
    def set_idle_timeout(self, timeout: int) -> None: ...
    def set_proxy_resolver(
        self, proxy_resolver: typing.Optional[Gio.ProxyResolver] = None
    ) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_tls_database(
        self, tls_database: typing.Optional[Gio.TlsDatabase] = None
    ) -> None: ...
    def set_tls_interaction(
        self, tls_interaction: typing.Optional[Gio.TlsInteraction] = None
    ) -> None: ...
    def set_user_agent(self, user_agent: str) -> None: ...
    def websocket_connect_async(
        self,
        msg: Message,
        origin: typing.Optional[str],
        protocols: typing.Optional[typing.Sequence[str]],
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def websocket_connect_finish(
        self, result: Gio.AsyncResult
    ) -> WebsocketConnection: ...

class SessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SessionClass()
    """

    parent_class: GObject.ObjectClass = ...
    request_queued: typing.Callable[[Session, Message], None] = ...
    request_unqueued: typing.Callable[[Session, Message], None] = ...
    _soup_reserved1: None = ...
    _soup_reserved2: None = ...
    _soup_reserved3: None = ...
    _soup_reserved4: None = ...
    _soup_reserved5: None = ...
    _soup_reserved6: None = ...
    _soup_reserved7: None = ...
    _soup_reserved8: None = ...

class SessionFeature(GObject.GInterface): ...
class SessionFeatureInterface(GObject.GPointer): ...

class WebsocketConnection(GObject.Object):
    """
    :Constructors:

    ::

        WebsocketConnection(**properties)
        new(stream:Gio.IOStream, uri:GLib.Uri, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None, extensions:list) -> Soup.WebsocketConnection

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
      uri -> GUri: URI
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
      keepalive-pong-timeout -> guint: Keepalive pong timeout
        Keepalive pong timeout
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
        keepalive_pong_timeout: int
        max_incoming_payload_size: int
        origin: typing.Optional[str]
        protocol: typing.Optional[str]
        state: WebsocketState
        uri: GLib.Uri

    props: Props = ...
    def __init__(
        self,
        connection_type: WebsocketConnectionType = ...,
        extensions: None = ...,
        io_stream: Gio.IOStream = ...,
        keepalive_interval: int = ...,
        keepalive_pong_timeout: int = ...,
        max_incoming_payload_size: int = ...,
        origin: str = ...,
        protocol: str = ...,
        uri: GLib.Uri = ...,
    ) -> None: ...
    def close(self, code: int, data: typing.Optional[str] = None) -> None: ...
    def get_close_code(self) -> int: ...
    def get_close_data(self) -> str: ...
    def get_connection_type(self) -> WebsocketConnectionType: ...
    def get_extensions(self) -> list[WebsocketExtension]: ...
    def get_io_stream(self) -> Gio.IOStream: ...
    def get_keepalive_interval(self) -> int: ...
    def get_keepalive_pong_timeout(self) -> int: ...
    def get_max_incoming_payload_size(self) -> int: ...
    def get_origin(self) -> typing.Optional[str]: ...
    def get_protocol(self) -> typing.Optional[str]: ...
    def get_state(self) -> WebsocketState: ...
    def get_uri(self) -> GLib.Uri: ...
    @classmethod
    def new(
        cls,
        stream: Gio.IOStream,
        uri: GLib.Uri,
        type: WebsocketConnectionType,
        origin: typing.Optional[str],
        protocol: typing.Optional[str],
        extensions: list[WebsocketExtension],
    ) -> WebsocketConnection: ...
    def send_binary(
        self, data: typing.Optional[typing.Sequence[int]] = None
    ) -> None: ...
    def send_message(self, type: WebsocketDataType, message: GLib.Bytes) -> None: ...
    def send_text(self, text: str) -> None: ...
    def set_keepalive_interval(self, interval: int) -> None: ...
    def set_keepalive_pong_timeout(self, pong_timeout: int) -> None: ...
    def set_max_incoming_payload_size(self, max_incoming_payload_size: int) -> None: ...

class WebsocketConnectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketConnectionClass()
    """

    parent_class: GObject.ObjectClass = ...

class WebsocketExtension(GObject.Object):
    """
    :Constructors:

    ::

        WebsocketExtension(**properties)

    Object SoupWebsocketExtension

    Signals from GObject:
      notify (GParam)
    """

    parent_instance: GObject.Object = ...
    def configure(
        self,
        connection_type: WebsocketConnectionType,
        params: typing.Optional[dict[None, None]] = None,
    ) -> bool: ...
    def do_configure(
        self,
        connection_type: WebsocketConnectionType,
        params: typing.Optional[dict[None, None]] = None,
    ) -> bool: ...
    def do_get_request_params(self) -> typing.Optional[str]: ...
    def do_get_response_params(self) -> typing.Optional[str]: ...
    def do_process_incoming_message(
        self, payload: GLib.Bytes
    ) -> typing.Tuple[GLib.Bytes, int]: ...
    def do_process_outgoing_message(
        self, payload: GLib.Bytes
    ) -> typing.Tuple[GLib.Bytes, int]: ...
    def get_request_params(self) -> typing.Optional[str]: ...
    def get_response_params(self) -> typing.Optional[str]: ...
    def process_incoming_message(
        self, payload: GLib.Bytes
    ) -> typing.Tuple[GLib.Bytes, int]: ...
    def process_outgoing_message(
        self, payload: GLib.Bytes
    ) -> typing.Tuple[GLib.Bytes, int]: ...

class WebsocketExtensionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketExtensionClass()
    """

    parent_class: GObject.ObjectClass = ...
    name: str = ...
    configure: typing.Callable[
        [
            WebsocketExtension,
            WebsocketConnectionType,
            typing.Optional[dict[None, None]],
        ],
        bool,
    ] = ...
    get_request_params: typing.Callable[
        [WebsocketExtension], typing.Optional[str]
    ] = ...
    get_response_params: typing.Callable[
        [WebsocketExtension], typing.Optional[str]
    ] = ...
    process_outgoing_message: typing.Callable[
        [WebsocketExtension, GLib.Bytes], typing.Tuple[GLib.Bytes, int]
    ] = ...
    process_incoming_message: typing.Callable[
        [WebsocketExtension, GLib.Bytes], typing.Tuple[GLib.Bytes, int]
    ] = ...
    padding: list[None] = ...

class WebsocketExtensionDeflate(WebsocketExtension): ...

class WebsocketExtensionDeflateClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketExtensionDeflateClass()
    """

    parent_class: WebsocketExtensionClass = ...

class WebsocketExtensionManager(GObject.Object, SessionFeature): ...

class WebsocketExtensionManagerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebsocketExtensionManagerClass()
    """

    parent_class: GObject.ObjectClass = ...

class Cacheability(GObject.GFlags):
    CACHEABLE = 1
    INVALIDATES = 4
    UNCACHEABLE = 2
    VALIDATES = 8

class Expectation(GObject.GFlags):
    CONTINUE = 2
    UNRECOGNIZED = 1

class MessageFlags(GObject.GFlags):
    COLLECT_METRICS = 32
    DO_NOT_USE_AUTH_CACHE = 16
    IDEMPOTENT = 8
    NEW_CONNECTION = 4
    NO_REDIRECT = 2

class ServerListenOptions(GObject.GFlags):
    HTTPS = 1
    IPV4_ONLY = 2
    IPV6_ONLY = 4

class CacheType(GObject.GEnum):
    SHARED = 1
    SINGLE_USER = 0

class CookieJarAcceptPolicy(GObject.GEnum):
    ALWAYS = 0
    GRANDFATHERED_THIRD_PARTY = 3
    NEVER = 1
    NO_THIRD_PARTY = 2

class DateFormat(GObject.GEnum):
    COOKIE = 2
    HTTP = 1

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
    HTTP_2_0 = 2

class LoggerLogLevel(GObject.GEnum):
    BODY = 3
    HEADERS = 2
    MINIMAL = 1
    NONE = 0

class MemoryUse(GObject.GEnum):
    COPY = 2
    STATIC = 0
    TAKE = 1

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

class SameSitePolicy(GObject.GEnum):
    LAX = 1
    NONE = 0
    STRICT = 2

class SessionError(GObject.GEnum):
    ENCODING = 1
    MESSAGE_ALREADY_IN_QUEUE = 6
    PARSING = 0
    REDIRECT_BAD_URI = 5
    REDIRECT_NO_LOCATION = 4
    TOO_MANY_REDIRECTS = 2
    TOO_MANY_RESTARTS = 3
    @staticmethod
    def quark() -> int: ...

class Status(GObject.GEnum):
    ACCEPTED = 202
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
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
    LENGTH_REQUIRED = 411
    LOCKED = 423
    METHOD_NOT_ALLOWED = 405
    MISDIRECTED_REQUEST = 421
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
    SWITCHING_PROTOCOLS = 101
    TEMPORARY_REDIRECT = 307
    UNAUTHORIZED = 401
    UNPROCESSABLE_ENTITY = 422
    UNSUPPORTED_MEDIA_TYPE = 415
    USE_PROXY = 305
    @staticmethod
    def get_phrase(status_code: int) -> str: ...

class TLDError(GObject.GEnum):
    INVALID_HOSTNAME = 0
    IS_IP_ADDRESS = 1
    NOT_ENOUGH_DOMAINS = 2
    NO_BASE_DOMAIN = 3
    NO_PSL_DATA = 4
    @staticmethod
    def quark() -> int: ...

class URIComponent(GObject.GEnum):
    AUTH_PARAMS = 4
    FRAGMENT = 9
    HOST = 5
    NONE = 0
    PASSWORD = 3
    PATH = 7
    PORT = 6
    QUERY = 8
    SCHEME = 1
    USER = 2

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
    def quark() -> int: ...

class WebsocketState(GObject.GEnum):
    CLOSED = 3
    CLOSING = 2
    OPEN = 1
