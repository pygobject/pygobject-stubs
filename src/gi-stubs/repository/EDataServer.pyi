import typing

from gi.repository import Camel
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Json
from gi.repository import libxml2
from gi.repository import Soup
from typing_extensions import Self

T = typing.TypeVar("T")

CLIENT_BACKEND_PROPERTY_CACHE_DIR: str = "cache-dir"
CLIENT_BACKEND_PROPERTY_CAPABILITIES: str = "capabilities"
CLIENT_BACKEND_PROPERTY_ONLINE: str = "online"
CLIENT_BACKEND_PROPERTY_OPENED: str = "opened"
CLIENT_BACKEND_PROPERTY_OPENING: str = "opening"
CLIENT_BACKEND_PROPERTY_READONLY: str = "readonly"
CLIENT_BACKEND_PROPERTY_REVISION: str = "revision"
DEBUG_LOG_DOMAIN_CAL_QUERIES: str = "CalQueries"
DEBUG_LOG_DOMAIN_GLOG: str = "GLog"
DEBUG_LOG_DOMAIN_USER: str = "USER"
EDS_MAJOR_VERSION: int = 3
EDS_MICRO_VERSION: int = 3
EDS_MINOR_VERSION: int = 52
NETWORK_MONITOR_ALWAYS_ONLINE_NAME: str = '"always-online"'
OAUTH2_SECRET_ACCESS_TOKEN: str = "access_token"
OAUTH2_SECRET_EXPIRES_AFTER: str = "expires_after"
OAUTH2_SECRET_REFRESH_TOKEN: str = "refresh_token"
SOURCE_CREDENTIAL_PASSWORD: str = "password"
SOURCE_CREDENTIAL_SSL_TRUST: str = "ssl-trust"
SOURCE_CREDENTIAL_USERNAME: str = "username"
SOURCE_EXTENSION_ADDRESS_BOOK: str = "Address Book"
SOURCE_EXTENSION_ALARMS: str = "Alarms"
SOURCE_EXTENSION_AUTHENTICATION: str = "Authentication"
SOURCE_EXTENSION_AUTOCOMPLETE: str = "Autocomplete"
SOURCE_EXTENSION_AUTOCONFIG: str = "Autoconfig"
SOURCE_EXTENSION_CALENDAR: str = "Calendar"
SOURCE_EXTENSION_COLLECTION: str = "Collection"
SOURCE_EXTENSION_CONTACTS_BACKEND: str = "Contacts Backend"
SOURCE_EXTENSION_GOA: str = "GNOME Online Accounts"
SOURCE_EXTENSION_LDAP_BACKEND: str = "LDAP Backend"
SOURCE_EXTENSION_LOCAL_BACKEND: str = "Local Backend"
SOURCE_EXTENSION_MAIL_ACCOUNT: str = "Mail Account"
SOURCE_EXTENSION_MAIL_COMPOSITION: str = "Mail Composition"
SOURCE_EXTENSION_MAIL_IDENTITY: str = "Mail Identity"
SOURCE_EXTENSION_MAIL_SIGNATURE: str = "Mail Signature"
SOURCE_EXTENSION_MAIL_SUBMISSION: str = "Mail Submission"
SOURCE_EXTENSION_MAIL_TRANSPORT: str = "Mail Transport"
SOURCE_EXTENSION_MDN: str = "Message Disposition Notifications"
SOURCE_EXTENSION_MEMO_LIST: str = "Memo List"
SOURCE_EXTENSION_OFFLINE: str = "Offline"
SOURCE_EXTENSION_OPENPGP: str = "Pretty Good Privacy (OpenPGP)"
SOURCE_EXTENSION_PROXY: str = "Proxy"
SOURCE_EXTENSION_REFRESH: str = "Refresh"
SOURCE_EXTENSION_RESOURCE: str = "Resource"
SOURCE_EXTENSION_REVISION_GUARDS: str = "Revision Guards"
SOURCE_EXTENSION_SECURITY: str = "Security"
SOURCE_EXTENSION_SMIME: str = "Secure MIME (S/MIME)"
SOURCE_EXTENSION_TASK_LIST: str = "Task List"
SOURCE_EXTENSION_UOA: str = "Ubuntu Online Accounts"
SOURCE_EXTENSION_WEATHER_BACKEND: str = "Weather Backend"
SOURCE_EXTENSION_WEBDAV_BACKEND: str = "WebDAV Backend"
SOURCE_EXTENSION_WEBDAV_NOTES: str = "WebDAV Notes"
SOURCE_PARAM_SETTING: int = 1
WEBDAV_CAPABILITY_ACCESS_CONTROL: str = "access-control"
WEBDAV_CAPABILITY_ADDRESSBOOK: str = "addressbook"
WEBDAV_CAPABILITY_BIND: str = "bind"
WEBDAV_CAPABILITY_CALENDAR_ACCESS: str = "calendar-access"
WEBDAV_CAPABILITY_CALENDAR_AUTO_SCHEDULE: str = "calendar-auto-schedule"
WEBDAV_CAPABILITY_CALENDAR_PROXY: str = "calendar-proxy"
WEBDAV_CAPABILITY_CALENDAR_SCHEDULE: str = "calendar-schedule"
WEBDAV_CAPABILITY_CLASS_1: str = "1"
WEBDAV_CAPABILITY_CLASS_2: str = "2"
WEBDAV_CAPABILITY_CLASS_3: str = "3"
WEBDAV_CAPABILITY_EXTENDED_MKCOL: str = "extended-mkcol"
WEBDAV_COLLATION_ASCII_CASEMAP: str = "i;"
WEBDAV_COLLATION_ASCII_CASEMAP_SUFFIX: str = "ascii-casemap"
WEBDAV_COLLATION_ASCII_NUMERIC: str = "i;"
WEBDAV_COLLATION_ASCII_NUMERIC_SUFFIX: str = "ascii-numeric"
WEBDAV_COLLATION_OCTET: str = "i;"
WEBDAV_COLLATION_OCTET_SUFFIX: str = "octet"
WEBDAV_COLLATION_UNICODE_CASEMAP: str = "i;"
WEBDAV_COLLATION_UNICODE_CASEMAP_SUFFIX: str = "unicode-casemap"
WEBDAV_CONTENT_TYPE_CALENDAR: str = 'text/calendar; charset="utf-8"'
WEBDAV_CONTENT_TYPE_VCARD: str = 'text/vcard; charset="utf-8"'
WEBDAV_CONTENT_TYPE_XML: str = 'application/xml; charset="utf-8"'
WEBDAV_DEPTH_INFINITY: str = "infinity"
WEBDAV_DEPTH_THIS: str = "0"
WEBDAV_DEPTH_THIS_AND_CHILDREN: str = "1"
WEBDAV_NS_CALDAV: str = "urn:ietf:params:xml:ns:caldav"
WEBDAV_NS_CALENDARSERVER: str = "http://calendarserver.org/ns/"
WEBDAV_NS_CARDDAV: str = "urn:ietf:params:xml:ns:carddav"
WEBDAV_NS_DAV: str = "DAV:"
WEBDAV_NS_ICAL: str = "http://apple.com/ns/ical/"

def binding_bind_property(
    source: GObject.Object,
    source_property: str,
    target: GObject.Object,
    target_property: str,
    flags: GObject.BindingFlags,
) -> GObject.Binding: ...
def binding_bind_property_full(
    source: GObject.Object,
    source_property: str,
    target: GObject.Object,
    target_property: str,
    flags: GObject.BindingFlags,
    transform_to: typing.Optional[typing.Callable[..., typing.Any]] = None,
    transform_from: typing.Optional[typing.Callable[..., typing.Any]] = None,
) -> GObject.Binding: ...
def binding_transform_enum_nick_to_value(
    binding: GObject.Binding,
    source_value: typing.Any,
    target_value: typing.Any,
    not_used: None,
) -> bool: ...
def binding_transform_enum_value_to_nick(
    binding: GObject.Binding,
    source_value: typing.Any,
    target_value: typing.Any,
    not_used: None,
) -> bool: ...
def categories_add(
    category: str, unused: str, icon_file: str, searchable: bool
) -> None: ...
def categories_dup_icon_file_for(category: str) -> str: ...
def categories_dup_list() -> list[str]: ...
def categories_exist(category: str) -> bool: ...
def categories_get_icon_file_for(category: str) -> str: ...
def categories_get_list() -> list[str]: ...
def categories_is_searchable(category: str) -> bool: ...
def categories_register_change_listener(
    listener: typing.Callable[..., None], *user_data: typing.Any
) -> None: ...
def categories_remove(category: str) -> None: ...
def categories_set_icon_file_for(category: str, icon_file: str) -> None: ...
def categories_unregister_change_listener(
    listener: typing.Callable[..., None], *user_data: typing.Any
) -> None: ...
def collator_error_quark() -> int: ...
def data_server_util_get_dbus_call_timeout() -> int: ...
def data_server_util_set_dbus_call_timeout(timeout_msec: int) -> None: ...
def debug_log_clear() -> None: ...
def debug_log_disable_domains(domains: typing.Sequence[str]) -> None: ...
def debug_log_dump(filename: str) -> bool: ...
def debug_log_dump_to_dated_file() -> bool: ...
def debug_log_enable_domains(domains: typing.Sequence[str]) -> None: ...
def debug_log_get_max_lines() -> int: ...
def debug_log_is_domain_enabled(domain: str) -> bool: ...
def debug_log_load_configuration(filename: str) -> bool: ...
def debug_log_set_max_lines(num_lines: int) -> None: ...
def eds_check_version(
    required_major: int, required_minor: int, required_micro: int
) -> typing.Optional[str]: ...
def enum_from_string(
    enum_type: typing.Type[typing.Any], string: str, enum_value: int
) -> bool: ...
def enum_to_string(enum_type: typing.Type[typing.Any], enum_value: int) -> str: ...
def file_recursive_delete(
    file: Gio.File,
    io_priority: int,
    cancellable: typing.Optional[Gio.Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def file_recursive_delete_finish(file: Gio.File, result: Gio.AsyncResult) -> bool: ...
def file_recursive_delete_sync(
    file: Gio.File, cancellable: typing.Optional[Gio.Cancellable] = None
) -> bool: ...
def filename_make_safe(string: str) -> None: ...
def filename_mkdir_encoded(
    basepath: str, fileprefix: str, filename: typing.Optional[str], fileindex: int
) -> typing.Optional[str]: ...
def free_form_exp_to_sexp(
    free_form_exp: str, symbols: FreeFormExpSymbol
) -> typing.Optional[str]: ...
def gdata_task_add_completed(builder: Json.Builder, value: int) -> None: ...
def gdata_task_add_due(builder: Json.Builder, value: int) -> None: ...
def gdata_task_add_id(builder: Json.Builder, value: str) -> None: ...
def gdata_task_add_notes(
    builder: Json.Builder, value: typing.Optional[str] = None
) -> None: ...
def gdata_task_add_status(builder: Json.Builder, value: GDataTaskStatus) -> None: ...
def gdata_task_add_title(builder: Json.Builder, value: str) -> None: ...
def gdata_task_get_completed(task: Json.Object) -> int: ...
def gdata_task_get_deleted(task: Json.Object) -> bool: ...
def gdata_task_get_due(task: Json.Object) -> int: ...
def gdata_task_get_etag(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_hidden(task: Json.Object) -> bool: ...
def gdata_task_get_id(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_notes(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_parent(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_position(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_self_link(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_status(task: Json.Object) -> GDataTaskStatus: ...
def gdata_task_get_title(task: Json.Object) -> typing.Optional[str]: ...
def gdata_task_get_updated(task: Json.Object) -> int: ...
def gdata_tasklist_add_id(builder: Json.Builder, value: str) -> None: ...
def gdata_tasklist_add_title(builder: Json.Builder, value: str) -> None: ...
def gdata_tasklist_get_etag(tasklist: Json.Object) -> typing.Optional[str]: ...
def gdata_tasklist_get_id(tasklist: Json.Object) -> typing.Optional[str]: ...
def gdata_tasklist_get_self_link(tasklist: Json.Object) -> typing.Optional[str]: ...
def gdata_tasklist_get_title(tasklist: Json.Object) -> typing.Optional[str]: ...
def gdata_tasklist_get_updated(tasklist: Json.Object) -> int: ...
def get_user_cache_dir() -> str: ...
def get_user_config_dir() -> str: ...
def get_user_data_dir() -> str: ...
def localtime_with_offset(tt: int, tm: None, offset: int) -> None: ...
def mktime_utc(tm: None) -> int: ...
def oauth2_service_util_compile_value(
    compile_value: str, out_glob_buff_size: int
) -> typing.Tuple[str, str]: ...
def oauth2_service_util_extract_from_uri(
    in_uri: str,
) -> typing.Tuple[bool, str, str, str]: ...
def oauth2_service_util_set_to_form(
    form: dict[str, str], name: str, value: typing.Optional[str] = None
) -> None: ...
def oauth2_service_util_take_to_form(
    form: dict[str, str], name: str, value: typing.Optional[str] = None
) -> None: ...
def queue_transfer(src_queue: GLib.Queue, dst_queue: GLib.Queue) -> None: ...
def secret_store_delete_sync(
    uid: str, cancellable: typing.Optional[Gio.Cancellable] = None
) -> bool: ...
def secret_store_lookup_sync(
    uid: str, cancellable: typing.Optional[Gio.Cancellable] = None
) -> typing.Tuple[bool, str]: ...
def secret_store_store_sync(
    uid: str,
    secret: str,
    label: str,
    permanently: bool,
    cancellable: typing.Optional[Gio.Cancellable] = None,
) -> bool: ...
def soup_ssl_trust_connect(soup_message: Soup.Message, source: Source) -> None: ...
def strftime(string: str, max: int, fmt: str, tm: None) -> int: ...
def time_format_date_and_time(
    date_tm: None,
    use_24_hour_format: bool,
    show_midnight: bool,
    show_zero_seconds: bool,
    buffer: str,
    buffer_size: int,
) -> None: ...
def time_format_time(
    date_tm: None,
    use_24_hour_format: bool,
    show_zero_seconds: bool,
    buffer: str,
    buffer_size: int,
) -> None: ...
def time_get_d_fmt_with_4digit_year() -> str: ...
def time_parse_date(value: str, result: None) -> TimeParseStatus: ...
def time_parse_date_and_time(value: str, result: None) -> TimeParseStatus: ...
def time_parse_date_and_time_ex(
    value: str, result: None, two_digit_year: bool
) -> TimeParseStatus: ...
def time_parse_date_ex(
    value: str, result: None, two_digit_year: bool
) -> TimeParseStatus: ...
def time_parse_date_format(
    value: str, format: str
) -> typing.Tuple[TimeParseStatus, None, bool]: ...
def time_parse_time(value: str, result: None) -> TimeParseStatus: ...
def timeout_add_seconds_with_name(
    priority: int,
    interval: int,
    name: typing.Optional[str],
    function: typing.Callable[..., bool],
    *data: typing.Any,
) -> int: ...
def timeout_add_with_name(
    priority: int,
    interval: int,
    name: typing.Optional[str],
    function: typing.Callable[..., bool],
    *data: typing.Any,
) -> int: ...
def type_traverse(
    parent_type: typing.Type[typing.Any],
    func: typing.Callable[..., None],
    *user_data: typing.Any,
) -> None: ...
def uid_new() -> str: ...
def utf8_strftime(string: str, max: int, fmt: str, tm: None) -> int: ...
def util_can_use_collection_as_credential_source(
    collection_source: None, child_source: None
) -> bool: ...
def util_change_uri_component(
    component: Soup.URIComponent, value: typing.Optional[str] = None
) -> GLib.Uri: ...
def util_change_uri_port(port: int) -> GLib.Uri: ...
def util_copy_object_slist(
    copy_to: typing.Optional[list[GObject.Object]], objects: list[GObject.Object]
) -> list[GObject.Object]: ...
def util_copy_string_slist(
    copy_to: typing.Optional[list[str]], strings: list[str]
) -> list[str]: ...
def util_ensure_gdbus_string(str: typing.Optional[str], gdbus_str: str) -> str: ...
def util_free_nullable_object_slist(objects: list[GObject.Object]) -> None: ...
def util_free_object_slist(objects: list[GObject.Object]) -> None: ...
def util_free_string_slist(strings: list[str]) -> None: ...
def util_generate_uid() -> str: ...
def util_get_directory_variants(
    main_path: str, replace_prefix: str, with_modules_dir: bool
) -> list[str]: ...
def util_get_source_full_name(registry: None, source: None) -> str: ...
def util_gthread_id(thread: GLib.Thread) -> int: ...
def util_guess_source_is_readonly(source: None) -> bool: ...
def util_identity_can_send(registry: None, identity_source: None) -> bool: ...
def util_safe_free_string(str: str) -> None: ...
def util_slist_to_strv(strings: list[str]) -> list[str]: ...
def util_source_compare_for_sort(source_a: None, source_b: None) -> int: ...
def util_strcmp0(
    str1: typing.Optional[str] = None, str2: typing.Optional[str] = None
) -> int: ...
def util_strdup_strip(string: typing.Optional[str] = None) -> typing.Optional[str]: ...
def util_strstrcase(haystack: str, needle: str) -> typing.Optional[str]: ...
def util_strv_equal(v1: typing.Sequence[str], v2: typing.Sequence[str]) -> bool: ...
def util_strv_to_slist(strv: str) -> list[str]: ...
def util_unicode_get_utf8(text: str, out: str) -> typing.Optional[str]: ...
def util_unref_in_thread(object: None) -> None: ...
def util_utf8_data_make_valid(data: typing.Optional[str], data_bytes: int) -> str: ...
def util_utf8_decompose(text: str) -> str: ...
def util_utf8_make_valid(str: typing.Optional[str] = None) -> str: ...
def util_utf8_normalize(str: typing.Optional[str] = None) -> typing.Optional[str]: ...
def util_utf8_remove_accents(
    str: typing.Optional[str] = None,
) -> typing.Optional[str]: ...
def util_utf8_strcasecmp(s1: str, s2: str) -> int: ...
def util_utf8_strstrcase(
    haystack: typing.Optional[str] = None, needle: typing.Optional[str] = None
) -> typing.Optional[str]: ...
def util_utf8_strstrcasedecomp(haystack: str, needle: str) -> typing.Optional[str]: ...
def webdav_access_control_entry_free(ptr: None) -> None: ...
def webdav_discover_free_discovered_sources(
    discovered_sources: list[WebDAVDiscoveredSource],
) -> None: ...
def webdav_discover_sources(
    source: Source,
    url_use_path: typing.Optional[str],
    only_supports: int,
    credentials: typing.Optional[NamedParameters] = None,
    cancellable: typing.Optional[Gio.Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def webdav_discover_sources_finish(
    source: Source, result: Gio.AsyncResult
) -> typing.Tuple[
    bool, str, Gio.TlsCertificateFlags, list[WebDAVDiscoveredSource], list[str]
]: ...
def webdav_discover_sources_full(
    source: Source,
    url_use_path: typing.Optional[str],
    only_supports: int,
    credentials: typing.Optional[NamedParameters] = None,
    ref_source_func: typing.Optional[
        typing.Callable[..., typing.Optional[Source]]
    ] = None,
    cancellable: typing.Optional[Gio.Cancellable] = None,
    callback: typing.Optional[typing.Callable[..., None]] = None,
    *user_data: typing.Any,
) -> None: ...
def webdav_discover_sources_full_sync(
    source: Source,
    url_use_path: typing.Optional[str],
    only_supports: int,
    credentials: typing.Optional[NamedParameters] = None,
    ref_source_func: typing.Optional[
        typing.Callable[..., typing.Optional[Source]]
    ] = None,
    cancellable: typing.Optional[Gio.Cancellable] = None,
    *ref_source_func_user_data: typing.Any,
) -> typing.Tuple[
    bool, str, Gio.TlsCertificateFlags, list[WebDAVDiscoveredSource], list[str]
]: ...
def webdav_discover_sources_sync(
    source: Source,
    url_use_path: typing.Optional[str],
    only_supports: int,
    credentials: typing.Optional[NamedParameters] = None,
    cancellable: typing.Optional[Gio.Cancellable] = None,
) -> typing.Tuple[
    bool, str, Gio.TlsCertificateFlags, list[WebDAVDiscoveredSource], list[str]
]: ...
def webdav_privilege_free(ptr: None) -> None: ...
def webdav_property_change_free(ptr: None) -> None: ...
def webdav_resource_free(ptr: None) -> None: ...
def xml_destroy_hash(hash: dict[str, str]) -> None: ...
def xml_save_file(filename: str, doc: libxml2.Doc) -> int: ...
def xml_to_hash(doc: libxml2.Doc, type: XmlHashType) -> dict[str, str]: ...
def xmlhash_add(hash: XmlHash, key: str, data: str) -> None: ...
def xmlhash_compare(hash: XmlHash, key: str, compare_data: str) -> XmlHashStatus: ...
def xmlhash_destroy(hash: XmlHash) -> None: ...
def xmlhash_foreach_key(
    hash: XmlHash, func: typing.Callable[..., None], *user_data: typing.Any
) -> None: ...
def xmlhash_foreach_key_remove(
    hash: XmlHash, func: typing.Callable[..., bool], *user_data: typing.Any
) -> None: ...
def xmlhash_remove(hash: XmlHash, key: str) -> None: ...
def xmlhash_write(hash: XmlHash) -> None: ...

class AsyncClosure(GObject.GPointer): ...

class Client(GObject.Object):
    """
    :Constructors:

    ::

        Client(**properties)

    Object EClient

    Signals from EClient:
      opened (GError)
      backend-error (gchararray)
      backend-died ()
      backend-property-changed (gchararray, gchararray)

    Properties from EClient:
      capabilities -> gpointer: Capabilities
        The capabilities of this client
      main-context -> GMainContext: Main Context
        The main loop context on which to attach event sources
      online -> gboolean: Online
        Whether this client is online
      opened -> gboolean: Opened
        Whether this client is open and ready to use
      readonly -> gboolean: Read only
        Whether this client's backing data is readonly
      source -> ESource: Source
        The ESource for which this client was created

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        capabilities: None
        main_context: GLib.MainContext
        online: bool
        opened: bool
        readonly: bool
        source: Source

    props: Props = ...
    parent: GObject.Object = ...
    priv: ClientPrivate = ...
    def __init__(self, online: bool = ..., source: Source = ...) -> None: ...
    def cancel_all(self) -> None: ...
    def check_capability(self, capability: str) -> bool: ...
    def check_refresh_supported(self) -> bool: ...
    def do_backend_died(self) -> None: ...
    def do_backend_error(self, error_msg: str) -> None: ...
    def do_backend_property_changed(self, prop_name: str, prop_value: str) -> None: ...
    def do_get_backend_property(
        self,
        prop_name: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_get_backend_property_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str]: ...
    def do_get_backend_property_sync(
        self, prop_name: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str]: ...
    def do_open(
        self,
        only_if_exists: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_open_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_open_sync(
        self, only_if_exists: bool, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_opened(self, error: GLib.Error) -> None: ...
    def do_refresh(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_refresh_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_refresh_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_remove(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_remove_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_remove_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_retrieve_capabilities(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_retrieve_capabilities_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str]: ...
    def do_retrieve_capabilities_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str]: ...
    def do_retrieve_properties_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_set_backend_property(
        self,
        prop_name: str,
        prop_value: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_set_backend_property_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_set_backend_property_sync(
        self,
        prop_name: str,
        prop_value: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def do_unwrap_dbus_error(self, dbus_error: GLib.Error) -> None: ...
    def dup_bus_name(self) -> str: ...
    @staticmethod
    def error_create(
        code: ClientError, custom_msg: typing.Optional[str] = None
    ) -> GLib.Error: ...
    @staticmethod
    def error_quark() -> int: ...
    @staticmethod
    def error_to_string(code: ClientError) -> str: ...
    def get_backend_property(
        self,
        prop_name: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_backend_property_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str]: ...
    def get_backend_property_sync(
        self, prop_name: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str]: ...
    def get_capabilities(self) -> list[str]: ...
    def get_source(self) -> Source: ...
    def is_online(self) -> bool: ...
    def is_opened(self) -> bool: ...
    def is_readonly(self) -> bool: ...
    def open(
        self,
        only_if_exists: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def open_finish(self, result: Gio.AsyncResult) -> bool: ...
    def open_sync(
        self, only_if_exists: bool, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def ref_main_context(self) -> GLib.MainContext: ...
    def refresh(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def refresh_finish(self, result: Gio.AsyncResult) -> bool: ...
    def refresh_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def remove(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def remove_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remove_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def retrieve_capabilities(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def retrieve_capabilities_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str]: ...
    def retrieve_capabilities_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str]: ...
    def retrieve_properties(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def retrieve_properties_finish(self, result: Gio.AsyncResult) -> bool: ...
    def retrieve_properties_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_backend_property(
        self,
        prop_name: str,
        prop_value: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def set_backend_property_finish(self, result: Gio.AsyncResult) -> bool: ...
    def set_backend_property_sync(
        self,
        prop_name: str,
        prop_value: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def set_bus_name(self, bus_name: str) -> None: ...
    def unwrap_dbus_error(self, dbus_error: GLib.Error) -> None: ...
    @staticmethod
    def util_copy_object_slist(
        copy_to: typing.Optional[list[GObject.Object]], objects: list[GObject.Object]
    ) -> list[GObject.Object]: ...
    @staticmethod
    def util_copy_string_slist(
        copy_to: typing.Optional[list[str]], strings: list[str]
    ) -> list[str]: ...
    @staticmethod
    def util_free_object_slist(objects: list[GObject.Object]) -> None: ...
    @staticmethod
    def util_free_string_slist(strings: list[str]) -> None: ...
    @staticmethod
    def util_parse_comma_strings(strings: str) -> list[str]: ...
    @staticmethod
    def util_slist_to_strv(strings: list[str]) -> list[str]: ...
    @staticmethod
    def util_strv_to_slist(strv: str) -> list[str]: ...
    @staticmethod
    def util_unwrap_dbus_error(
        dbus_error: GLib.Error,
        known_errors: ClientErrorsList,
        known_errors_count: int,
        known_errors_domain: int,
        fail_when_none_matched: bool,
    ) -> typing.Tuple[bool, GLib.Error]: ...
    def wait_for_connected(
        self,
        timeout_seconds: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def wait_for_connected_finish(self, result: Gio.AsyncResult) -> bool: ...
    def wait_for_connected_sync(
        self, timeout_seconds: int, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...

class ClientClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientClass()
    """

    parent: GObject.ObjectClass = ...
    get_dbus_proxy: None = ...
    unwrap_dbus_error: typing.Callable[[Client, GLib.Error], None] = ...
    retrieve_capabilities: typing.Callable[..., None] = ...
    retrieve_capabilities_finish: typing.Callable[
        [Client, Gio.AsyncResult], typing.Tuple[bool, str]
    ] = ...
    retrieve_capabilities_sync: typing.Callable[
        [Client, typing.Optional[Gio.Cancellable]], typing.Tuple[bool, str]
    ] = ...
    get_backend_property: typing.Callable[..., None] = ...
    get_backend_property_finish: typing.Callable[
        [Client, Gio.AsyncResult], typing.Tuple[bool, str]
    ] = ...
    get_backend_property_sync: typing.Callable[
        [Client, str, typing.Optional[Gio.Cancellable]], typing.Tuple[bool, str]
    ] = ...
    set_backend_property: typing.Callable[..., None] = ...
    set_backend_property_finish: typing.Callable[[Client, Gio.AsyncResult], bool] = ...
    set_backend_property_sync: typing.Callable[
        [Client, str, str, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    open: typing.Callable[..., None] = ...
    open_finish: typing.Callable[[Client, Gio.AsyncResult], bool] = ...
    open_sync: typing.Callable[
        [Client, bool, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    remove: typing.Callable[..., None] = ...
    remove_finish: typing.Callable[[Client, Gio.AsyncResult], bool] = ...
    remove_sync: typing.Callable[[Client, typing.Optional[Gio.Cancellable]], bool] = ...
    refresh: typing.Callable[..., None] = ...
    refresh_finish: typing.Callable[[Client, Gio.AsyncResult], bool] = ...
    refresh_sync: typing.Callable[
        [Client, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    retrieve_properties_sync: typing.Callable[
        [Client, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    opened: typing.Callable[[Client, GLib.Error], None] = ...
    backend_error: typing.Callable[[Client, str], None] = ...
    backend_died: typing.Callable[[Client], None] = ...
    backend_property_changed: typing.Callable[[Client, str, str], None] = ...

class ClientErrorsList(GObject.GPointer):
    """
    :Constructors:

    ::

        ClientErrorsList()
    """

    name: str = ...
    err_code: int = ...

class ClientPrivate(GObject.GPointer): ...

class Collator(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(locale:str) -> EDataServer.Collator
        new_interpret_country(locale:str) -> EDataServer.Collator, country_code:str
    """
    def collate(
        self, str_a: typing.Optional[str] = None, str_b: typing.Optional[str] = None
    ) -> typing.Tuple[bool, int]: ...
    @staticmethod
    def error_quark() -> int: ...
    def generate_key(self, str: str) -> str: ...
    def generate_key_for_index(self, index: int) -> str: ...
    def get_index(self, str: str) -> int: ...
    def get_index_labels(self) -> typing.Tuple[list[str], int, int, int, int]: ...
    @classmethod
    def new(cls, locale: str) -> Collator: ...
    @classmethod
    def new_interpret_country(cls, locale: str) -> Collator: ...
    def ref(self) -> Collator: ...
    def unref(self) -> None: ...

class Extensible(GObject.GInterface):
    """
    Interface EExtensible

    Signals from GObject:
      notify (GParam)
    """
    def list_extensions(
        self, extension_type: typing.Type[typing.Any]
    ) -> list[Extension]: ...
    def load_extensions(self) -> None: ...
    def reload_extensions(self) -> None: ...

class ExtensibleInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        ExtensibleInterface()
    """

    parent_interface: GObject.TypeInterface = ...

class Extension(GObject.Object):
    """
    :Constructors:

    ::

        Extension(**properties)

    Object EExtension

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        extensible: Extensible

    props: Props = ...
    parent: GObject.Object = ...
    priv: ExtensionPrivate = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...
    def get_extensible(self) -> Extensible: ...

class ExtensionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExtensionClass()
    """

    parent_class: GObject.ObjectClass = ...
    extensible_type: typing.Type[typing.Any] = ...

class ExtensionPrivate(GObject.GPointer): ...
class Flag(GObject.GPointer): ...

class FreeFormExpSymbol(GObject.GPointer):
    """
    :Constructors:

    ::

        FreeFormExpSymbol()
    """

    names: str = ...
    hint: str = ...
    build_sexp: typing.Callable[[str, str, str], str] = ...

class GDataQuery(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> EDataServer.GDataQuery
    """
    def get_completed_max(self) -> typing.Tuple[int, bool]: ...
    def get_completed_min(self) -> typing.Tuple[int, bool]: ...
    def get_due_max(self) -> typing.Tuple[int, bool]: ...
    def get_due_min(self) -> typing.Tuple[int, bool]: ...
    def get_max_results(self) -> typing.Tuple[int, bool]: ...
    def get_show_completed(self) -> typing.Tuple[bool, bool]: ...
    def get_show_deleted(self) -> typing.Tuple[bool, bool]: ...
    def get_show_hidden(self) -> typing.Tuple[bool, bool]: ...
    def get_updated_min(self) -> typing.Tuple[int, bool]: ...
    @classmethod
    def new(cls) -> GDataQuery: ...
    def ref(self) -> GDataQuery: ...
    def set_completed_max(self, value: int) -> None: ...
    def set_completed_min(self, value: int) -> None: ...
    def set_due_max(self, value: int) -> None: ...
    def set_due_min(self, value: int) -> None: ...
    def set_max_results(self, value: int) -> None: ...
    def set_show_completed(self, value: bool) -> None: ...
    def set_show_deleted(self, value: bool) -> None: ...
    def set_show_hidden(self, value: bool) -> None: ...
    def set_updated_min(self, value: int) -> None: ...
    def to_string(self) -> typing.Optional[str]: ...
    def unref(self) -> None: ...

class GDataSession(SoupSession):
    """
    :Constructors:

    ::

        GDataSession(**properties)
        new(source:EDataServer.Source) -> EDataServer.GDataSession

    Object EGDataSession

    Properties from ESoupSession:
      source -> ESource: Source
      credentials -> ENamedParameters: Credentials
      force-http1 -> gboolean: Force HTTP/1

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
    class Props(SoupSession.Props):
        credentials: typing.Optional[NamedParameters]
        force_http1: bool
        source: typing.Optional[Source]
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
    parent: SoupSession = ...
    priv: GDataSessionPrivate = ...
    def __init__(
        self,
        credentials: typing.Optional[NamedParameters] = ...,
        force_http1: bool = ...,
        source: Source = ...,
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
    @classmethod
    def new(cls, source: Source) -> GDataSession: ...
    def tasklists_delete_sync(
        self, tasklist_id: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def tasklists_get_sync(
        self, tasklist_id: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasklists_insert_sync(
        self, title: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasklists_list_sync(
        self,
        query: typing.Optional[GDataQuery] = None,
        cb: typing.Optional[typing.Callable[..., bool]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *user_data: typing.Any,
    ) -> bool: ...
    def tasklists_patch_sync(
        self,
        tasklist_id: str,
        tasklist_properties: Json.Builder,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasklists_update_sync(
        self,
        tasklist_id: str,
        tasklist: Json.Builder,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasks_clear_sync(
        self, tasklist_id: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def tasks_delete_sync(
        self,
        tasklist_id: str,
        task_id: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def tasks_get_sync(
        self,
        tasklist_id: str,
        task_id: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasks_insert_sync(
        self,
        tasklist_id: str,
        task: Json.Builder,
        parent_task_id: typing.Optional[str] = None,
        previous_task_id: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasks_list_sync(
        self,
        tasklist_id: str,
        query: typing.Optional[GDataQuery] = None,
        cb: typing.Optional[typing.Callable[..., bool]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *user_data: typing.Any,
    ) -> bool: ...
    def tasks_move_sync(
        self,
        tasklist_id: str,
        task_id: str,
        parent_task_id: typing.Optional[str] = None,
        previous_task_id: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def tasks_patch_sync(
        self,
        tasklist_id: str,
        task_id: str,
        task_properties: Json.Builder,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, Json.Object]: ...
    def tasks_update_sync(
        self,
        tasklist_id: str,
        task_id: str,
        task: Json.Builder,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, Json.Object]: ...

class GDataSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        GDataSessionClass()
    """

    parent_class: SoupSessionClass = ...
    reserved: list[None] = ...

class GDataSessionPrivate(GObject.GPointer): ...
class MemChunk(GObject.GPointer): ...

class Module(GObject.TypeModule, GObject.TypePlugin):
    """
    :Constructors:

    ::

        Module(**properties)
        new(filename:str) -> EDataServer.Module

    Object EModule

    Properties from EModule:
      filename -> gchararray: Filename
        The filename of the module

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.TypeModule.Props):
        filename: str

    props: Props = ...
    parent: GObject.TypeModule = ...
    priv: ModulePrivate = ...
    def __init__(self, filename: str = ...) -> None: ...
    def get_filename(self) -> str: ...
    @staticmethod
    def load_all_in_directory(dirname: str) -> list[Module]: ...
    @staticmethod
    def load_all_in_directory_and_prefixes(
        dirname: str, dirprefix: typing.Optional[str] = None
    ) -> list[Module]: ...
    @staticmethod
    def load_file(filename: str) -> Module: ...
    @classmethod
    def new(cls, filename: str) -> Module: ...

class ModuleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ModuleClass()
    """

    parent_class: GObject.TypeModuleClass = ...

class ModulePrivate(GObject.GPointer): ...

class NamedParameters(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> EDataServer.NamedParameters
        new_string(str:str) -> EDataServer.NamedParameters
        new_strv(strv:str) -> EDataServer.NamedParameters
    """
    def assign(self, from_: typing.Optional[NamedParameters] = None) -> None: ...
    def clear(self) -> None: ...
    def count(self) -> int: ...
    def equal(self, parameters2: NamedParameters) -> bool: ...
    def exists(self, name: str) -> bool: ...
    def free(self) -> None: ...
    def get(self, name: str) -> typing.Optional[str]: ...
    def get_name(self, index: int) -> typing.Optional[str]: ...
    @classmethod
    def new(cls) -> NamedParameters: ...
    def new_clone(self) -> NamedParameters: ...
    @classmethod
    def new_string(cls, str: str) -> NamedParameters: ...
    @classmethod
    def new_strv(cls, strv: str) -> NamedParameters: ...
    def set(self, name: str, value: typing.Optional[str] = None) -> None: ...
    def test(self, name: str, value: str, case_sensitively: bool) -> bool: ...
    def to_string(self) -> typing.Optional[str]: ...
    def to_strv(self) -> list[str]: ...

class NetworkMonitor(GObject.Object, Gio.Initable, Gio.NetworkMonitor):
    """
    :Constructors:

    ::

        NetworkMonitor(**properties)

    Object ENetworkMonitor

    Properties from ENetworkMonitor:
      gio-name -> gchararray: GIO name

    Signals from GNetworkMonitor:
      network-changed (gboolean)

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        gio_name: typing.Optional[str]
        connectivity: Gio.NetworkConnectivity
        network_available: bool
        network_metered: bool

    props: Props = ...
    parent: GObject.Object = ...
    priv: NetworkMonitorPrivate = ...
    def __init__(self, gio_name: typing.Optional[str] = ...) -> None: ...
    def dup_gio_name(self) -> str: ...
    @staticmethod
    def get_default() -> Gio.NetworkMonitor: ...
    def list_gio_names(self) -> list[str]: ...
    def set_gio_name(self, gio_name: typing.Optional[str] = None) -> None: ...

class NetworkMonitorClass(GObject.GPointer):
    """
    :Constructors:

    ::

        NetworkMonitorClass()
    """

    parent_class: GObject.ObjectClass = ...

class NetworkMonitorPrivate(GObject.GPointer): ...

class OAuth2Service(GObject.GInterface):
    """
    Interface EOAuth2Service

    Signals from GObject:
      notify (GParam)
    """
    def can_process(self, source: Source) -> bool: ...
    def delete_token_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def extract_authorization_code(
        self,
        source: Source,
        page_title: str,
        page_uri: str,
        page_content: typing.Optional[str] = None,
    ) -> typing.Tuple[bool, str]: ...
    def extract_error_message(
        self,
        source: Source,
        page_title: str,
        page_uri: str,
        page_content: typing.Optional[str] = None,
    ) -> typing.Tuple[bool, str]: ...
    def get_access_token_sync(
        self,
        source: Source,
        ref_source: typing.Callable[..., typing.Optional[Source]],
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *ref_source_user_data: typing.Any,
    ) -> typing.Tuple[bool, str, int]: ...
    def get_authentication_policy(
        self, source: Source, uri: str
    ) -> OAuth2ServiceNavigationPolicy: ...
    def get_authentication_uri(self, source: Source) -> str: ...
    def get_client_id(self, source: Source) -> str: ...
    def get_client_secret(self, source: Source) -> typing.Optional[str]: ...
    def get_display_name(self) -> str: ...
    def get_flags(self) -> int: ...
    def get_name(self) -> str: ...
    def get_redirect_uri(self, source: Source) -> typing.Optional[str]: ...
    def get_refresh_uri(self, source: Source) -> str: ...
    def guess_can_process(
        self,
        protocol: typing.Optional[str] = None,
        hostname: typing.Optional[str] = None,
    ) -> bool: ...
    def prepare_authentication_uri_query(
        self, source: Source, uri_query: dict[str, str]
    ) -> None: ...
    def prepare_get_token_form(
        self, source: Source, authorization_code: str, form: dict[str, str]
    ) -> None: ...
    def prepare_get_token_message(
        self, source: Source, message: Soup.Message
    ) -> None: ...
    def prepare_refresh_token_form(
        self, source: Source, refresh_token: str, form: dict[str, str]
    ) -> None: ...
    def prepare_refresh_token_message(
        self, source: Source, message: Soup.Message
    ) -> None: ...
    def receive_and_store_token_sync(
        self,
        source: Source,
        authorization_code: str,
        ref_source: typing.Callable[..., typing.Optional[Source]],
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *ref_source_user_data: typing.Any,
    ) -> bool: ...
    def refresh_and_store_token_sync(
        self,
        source: Source,
        refresh_token: str,
        ref_source: typing.Callable[..., typing.Optional[Source]],
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *ref_source_user_data: typing.Any,
    ) -> bool: ...
    @staticmethod
    def util_compile_value(
        compile_value: str, out_glob_buff_size: int
    ) -> typing.Tuple[str, str]: ...
    @staticmethod
    def util_extract_from_uri(in_uri: str) -> typing.Tuple[bool, str, str, str]: ...
    @staticmethod
    def util_set_to_form(
        form: dict[str, str], name: str, value: typing.Optional[str] = None
    ) -> None: ...
    @staticmethod
    def util_take_to_form(
        form: dict[str, str], name: str, value: typing.Optional[str] = None
    ) -> None: ...

class OAuth2ServiceBase(Extension):
    """
    :Constructors:

    ::

        OAuth2ServiceBase(**properties)

    Object EOAuth2ServiceBase

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(Extension.Props):
        extensible: Extensible

    props: Props = ...
    parent: Extension = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...

class OAuth2ServiceBaseClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2ServiceBaseClass()
    """

    parent_class: ExtensionClass = ...

class OAuth2ServiceGoogle(OAuth2ServiceBase, OAuth2Service):
    """
    :Constructors:

    ::

        OAuth2ServiceGoogle(**properties)

    Object EOAuth2ServiceGoogle

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(OAuth2ServiceBase.Props):
        extensible: Extensible

    props: Props = ...
    parent: OAuth2ServiceBase = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...

class OAuth2ServiceGoogleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2ServiceGoogleClass()
    """

    parent_class: OAuth2ServiceBaseClass = ...

class OAuth2ServiceInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2ServiceInterface()
    """

    parent_interface: GObject.TypeInterface = ...
    can_process: typing.Callable[[OAuth2Service, Source], bool] = ...
    guess_can_process: typing.Callable[
        [OAuth2Service, typing.Optional[str], typing.Optional[str]], bool
    ] = ...
    get_flags: typing.Callable[[OAuth2Service], int] = ...
    get_name: typing.Callable[[OAuth2Service], str] = ...
    get_display_name: typing.Callable[[OAuth2Service], str] = ...
    get_client_id: typing.Callable[[OAuth2Service, Source], str] = ...
    get_client_secret: typing.Callable[
        [OAuth2Service, Source], typing.Optional[str]
    ] = ...
    get_authentication_uri: typing.Callable[[OAuth2Service, Source], str] = ...
    get_refresh_uri: typing.Callable[[OAuth2Service, Source], str] = ...
    get_redirect_uri: typing.Callable[
        [OAuth2Service, Source], typing.Optional[str]
    ] = ...
    prepare_authentication_uri_query: typing.Callable[
        [OAuth2Service, Source, dict[str, str]], None
    ] = ...
    get_authentication_policy: typing.Callable[
        [OAuth2Service, Source, str], OAuth2ServiceNavigationPolicy
    ] = ...
    extract_authorization_code: typing.Callable[
        [OAuth2Service, Source, str, str, typing.Optional[str]], typing.Tuple[bool, str]
    ] = ...
    prepare_get_token_form: typing.Callable[
        [OAuth2Service, Source, str, dict[str, str]], None
    ] = ...
    prepare_get_token_message: typing.Callable[
        [OAuth2Service, Source, Soup.Message], None
    ] = ...
    prepare_refresh_token_form: typing.Callable[
        [OAuth2Service, Source, str, dict[str, str]], None
    ] = ...
    prepare_refresh_token_message: typing.Callable[
        [OAuth2Service, Source, Soup.Message], None
    ] = ...
    extract_error_message: typing.Callable[
        [OAuth2Service, Source, str, str, typing.Optional[str]], typing.Tuple[bool, str]
    ] = ...
    reserved: list[None] = ...

class OAuth2ServiceOutlook(OAuth2ServiceBase, OAuth2Service):
    """
    :Constructors:

    ::

        OAuth2ServiceOutlook(**properties)

    Object EOAuth2ServiceOutlook

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(OAuth2ServiceBase.Props):
        extensible: Extensible

    props: Props = ...
    parent: OAuth2ServiceBase = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...

class OAuth2ServiceOutlookClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2ServiceOutlookClass()
    """

    parent_class: OAuth2ServiceBaseClass = ...

class OAuth2ServiceYahoo(OAuth2ServiceBase, OAuth2Service):
    """
    :Constructors:

    ::

        OAuth2ServiceYahoo(**properties)

    Object EOAuth2ServiceYahoo

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(OAuth2ServiceBase.Props):
        extensible: Extensible

    props: Props = ...
    parent: OAuth2ServiceBase = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...

class OAuth2ServiceYahooClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2ServiceYahooClass()
    """

    parent_class: OAuth2ServiceBaseClass = ...

class OAuth2Services(GObject.Object, Extensible):
    """
    :Constructors:

    ::

        OAuth2Services(**properties)
        new() -> EDataServer.OAuth2Services

    Object EOAuth2Services

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: OAuth2ServicesPrivate = ...
    def add(self, service: OAuth2Service) -> None: ...
    def find(self, source: Source) -> typing.Optional[OAuth2Service]: ...
    def guess(
        self,
        protocol: typing.Optional[str] = None,
        hostname: typing.Optional[str] = None,
    ) -> typing.Optional[OAuth2Service]: ...
    def is_oauth2_alias(self, auth_method: typing.Optional[str] = None) -> bool: ...
    @staticmethod
    def is_oauth2_alias_static(auth_method: typing.Optional[str] = None) -> bool: ...
    @staticmethod
    def is_supported() -> bool: ...
    def list(self) -> list[OAuth2Service]: ...
    @classmethod
    def new(cls) -> OAuth2Services: ...
    def remove(self, service: OAuth2Service) -> None: ...

class OAuth2ServicesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        OAuth2ServicesClass()
    """

    parent_class: GObject.ObjectClass = ...
    reserved: list[None] = ...

class OAuth2ServicesPrivate(GObject.GPointer): ...

class OperationPool(GObject.GPointer):
    def free(self) -> None: ...
    def push(self, opdata: None) -> None: ...
    def release_opid(self, opid: int) -> None: ...
    def reserve_opid(self) -> int: ...

class SoupAuthBearer(Soup.Auth):
    """
    :Constructors:

    ::

        SoupAuthBearer(**properties)

    Object ESoupAuthBearer

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
    class Props(Soup.Auth.Props):
        authority: str
        is_authenticated: bool
        is_cancelled: bool
        is_for_proxy: bool
        realm: str
        scheme_name: str

    props: Props = ...
    parent: Soup.Auth = ...
    priv: SoupAuthBearerPrivate = ...
    def __init__(
        self, authority: str = ..., is_for_proxy: bool = ..., realm: str = ...
    ) -> None: ...
    def is_expired(self) -> bool: ...
    def set_access_token(self, access_token: str, expires_in_seconds: int) -> None: ...

class SoupAuthBearerClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SoupAuthBearerClass()
    """

    parent_class: Soup.AuthClass = ...

class SoupAuthBearerPrivate(GObject.GPointer): ...

class SoupSession(Soup.Session):
    """
    :Constructors:

    ::

        SoupSession(**properties)
        new(source:EDataServer.Source) -> EDataServer.SoupSession

    Object ESoupSession

    Properties from ESoupSession:
      source -> ESource: Source
      credentials -> ENamedParameters: Credentials
      force-http1 -> gboolean: Force HTTP/1

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
    class Props(Soup.Session.Props):
        credentials: typing.Optional[NamedParameters]
        force_http1: bool
        source: typing.Optional[Source]
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
    parent: Soup.Session = ...
    priv: SoupSessionPrivate = ...
    def __init__(
        self,
        credentials: typing.Optional[NamedParameters] = ...,
        force_http1: bool = ...,
        source: Source = ...,
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
    def check_result(
        self, message: Soup.Message, read_bytes: None, bytes_length: int
    ) -> bool: ...
    def dup_credentials(self) -> typing.Optional[NamedParameters]: ...
    @staticmethod
    def error_quark() -> int: ...
    def get_authentication_requires_credentials(self) -> bool: ...
    def get_force_http1(self) -> bool: ...
    def get_log_level(self) -> Soup.LoggerLogLevel: ...
    def get_source(self) -> typing.Optional[Source]: ...
    def get_ssl_error_details(
        self,
    ) -> typing.Tuple[bool, str, Gio.TlsCertificateFlags]: ...
    def handle_authentication_failure(
        self, credentials: typing.Optional[NamedParameters], op_error: GLib.Error
    ) -> typing.Tuple[SourceAuthenticationResult, str, Gio.TlsCertificateFlags]: ...
    @classmethod
    def new(cls, source: Source) -> SoupSession: ...
    def new_message(self, method: str, uri_string: str) -> Soup.Message: ...
    def new_message_from_uri(self, method: str, uri: GLib.Uri) -> Soup.Message: ...
    def prepare_message_send_sync(
        self,
        message: Soup.Message,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> None: ...
    def send_message(
        self,
        message: Soup.Message,
        io_priority: int,
        prepare_data: None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def send_message_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[Gio.InputStream, str, Gio.TlsCertificateFlags]: ...
    def send_message_simple_sync(
        self,
        message: Soup.Message,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bytes: ...
    def send_message_sync(
        self,
        message: Soup.Message,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> Gio.InputStream: ...
    def set_credentials(
        self, credentials: typing.Optional[NamedParameters] = None
    ) -> None: ...
    def set_force_http1(self, force_http1: bool) -> None: ...
    def setup_logging(self, logging_level: typing.Optional[str] = None) -> None: ...
    @staticmethod
    def util_get_force_http1_supported() -> bool: ...
    @staticmethod
    def util_get_message_bytes(message: Soup.Message) -> typing.Optional[bytes]: ...
    @staticmethod
    def util_normalize_uri_path(uri: GLib.Uri) -> typing.Optional[GLib.Uri]: ...
    @staticmethod
    def util_ref_message_request_body(
        message: Soup.Message,
    ) -> typing.Tuple[typing.Optional[Gio.InputStream], int]: ...
    @staticmethod
    def util_set_message_request_body(
        message: Soup.Message,
        content_type: typing.Optional[str],
        input_stream: Gio.InputStream,
        length: int,
    ) -> None: ...
    @staticmethod
    def util_set_message_request_body_from_data(
        message: Soup.Message,
        create_copy: bool,
        content_type: typing.Optional[str],
        data: None,
        length: int,
        free_func: typing.Optional[typing.Callable[[None], None]] = None,
    ) -> None: ...
    @staticmethod
    def util_status_to_string(
        status_code: int, reason_phrase: typing.Optional[str] = None
    ) -> str: ...

class SoupSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SoupSessionClass()
    """

    parent_class: Soup.SessionClass = ...
    reserved: list[None] = ...

class SoupSessionPrivate(GObject.GPointer): ...

class Source(GObject.Object, Gio.Initable, Gio.ProxyResolver):
    """
    :Constructors:

    ::

        Source(**properties)
        new(dbus_object:Gio.DBusObject=None, main_context:GLib.MainContext=None) -> EDataServer.Source
        new_with_uid(uid:str, main_context:GLib.MainContext=None) -> EDataServer.Source

    Object ESource

    Signals from ESource:
      changed ()
      credentials-required (ESourceCredentialsReason, gchararray, GTlsCertificateFlags, GError)
      authenticate (ENamedParameters)

    Properties from ESource:
      dbus-object -> EDBusObject: D-Bus Object
        The D-Bus object for the data source
      display-name -> gchararray: Display Name
        The human-readable name of the data source
      enabled -> gboolean: Enabled
        Whether the data source is enabled
      main-context -> GMainContext: Main Context
        The main loop context on which to attach event sources
      parent -> gchararray: Parent
        The unique identity of the parent data source
      remote-creatable -> gboolean: Remote Creatable
        Whether the data source can create remote resources
      remote-deletable -> gboolean: Remote Deletable
        Whether the data source can delete remote resources
      removable -> gboolean: Removable
        Whether the data source is removable
      uid -> gchararray: UID
        The unique identity of the data source
      writable -> gboolean: Writable
        Whether the data source is writable
      connection-status -> ESourceConnectionStatus: Connection Status
        Connection status of the source

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        connection_status: SourceConnectionStatus
        display_name: str
        enabled: bool
        main_context: GLib.MainContext
        parent: typing.Optional[str]
        remote_creatable: bool
        remote_deletable: bool
        removable: bool
        uid: str
        writable: bool

    props: Props = ...
    parent: GObject.Object = ...
    priv: SourcePrivate = ...
    def __init__(
        self,
        display_name: str = ...,
        enabled: bool = ...,
        main_context: GLib.MainContext = ...,
        parent: typing.Optional[str] = ...,
        uid: str = ...,
    ) -> None: ...
    def camel_configure_service(self, service: Camel.Service) -> None: ...
    def changed(self) -> None: ...
    def compare_by_display_name(self, source2: Source) -> int: ...
    def delete_password(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def delete_password_finish(self, result: Gio.AsyncResult) -> bool: ...
    def delete_password_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_authenticate(self, credentials: NamedParameters) -> None: ...
    def do_changed(self) -> None: ...
    def do_credentials_required(
        self,
        reason: SourceCredentialsReason,
        certificate_pem: str,
        certificate_errors: Gio.TlsCertificateFlags,
        op_error: GLib.Error,
    ) -> None: ...
    def do_get_oauth2_access_token(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_get_oauth2_access_token_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str, int]: ...
    def do_get_oauth2_access_token_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str, int]: ...
    def do_invoke_authenticate_impl(
        self,
        dbus_source: None,
        arg_credentials: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def do_invoke_credentials_required_impl(
        self,
        dbus_source: None,
        arg_reason: str,
        arg_certificate_pem: str,
        arg_certificate_errors: str,
        arg_dbus_error_name: str,
        arg_dbus_error_message: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def do_remote_create(
        self,
        scratch_source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_remote_create_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_remote_create_sync(
        self,
        scratch_source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def do_remote_delete(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_remote_delete_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_remote_delete_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_remove(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_remove_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_remove_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_unset_last_credentials_required_arguments_impl(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_write(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def do_write_finish(self, result: Gio.AsyncResult) -> bool: ...
    def do_write_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def dup_display_name(self) -> str: ...
    def dup_parent(self) -> typing.Optional[str]: ...
    def dup_secret_label(self) -> str: ...
    def dup_uid(self) -> str: ...
    def emit_credentials_required(
        self,
        reason: SourceCredentialsReason,
        certificate_pem: str,
        certificate_errors: Gio.TlsCertificateFlags,
        op_error: typing.Optional[GLib.Error] = None,
    ) -> None: ...
    def equal(self, source2: Source) -> bool: ...
    def get_connection_status(self) -> SourceConnectionStatus: ...
    def get_display_name(self) -> str: ...
    def get_enabled(self) -> bool: ...
    def get_extension(self, extension_name: str) -> SourceExtension: ...
    def get_last_credentials_required_arguments(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_last_credentials_required_arguments_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[
        bool, SourceCredentialsReason, str, Gio.TlsCertificateFlags, GLib.Error
    ]: ...
    def get_last_credentials_required_arguments_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[
        bool, SourceCredentialsReason, str, Gio.TlsCertificateFlags, GLib.Error
    ]: ...
    def get_oauth2_access_token(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def get_oauth2_access_token_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str, int]: ...
    def get_oauth2_access_token_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str, int]: ...
    def get_parent(self) -> typing.Optional[str]: ...
    def get_remote_creatable(self) -> bool: ...
    def get_remote_deletable(self) -> bool: ...
    def get_removable(self) -> bool: ...
    def get_uid(self) -> str: ...
    def get_writable(self) -> bool: ...
    def has_extension(self, extension_name: str) -> bool: ...
    def hash(self) -> int: ...
    def invoke_authenticate(
        self,
        credentials: typing.Optional[NamedParameters] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def invoke_authenticate_finish(self, result: Gio.AsyncResult) -> bool: ...
    def invoke_authenticate_sync(
        self,
        credentials: typing.Optional[NamedParameters] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def invoke_credentials_required(
        self,
        reason: SourceCredentialsReason,
        certificate_pem: str,
        certificate_errors: Gio.TlsCertificateFlags,
        op_error: typing.Optional[GLib.Error] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def invoke_credentials_required_finish(self, result: Gio.AsyncResult) -> bool: ...
    def invoke_credentials_required_sync(
        self,
        reason: SourceCredentialsReason,
        certificate_pem: str,
        certificate_errors: Gio.TlsCertificateFlags,
        op_error: typing.Optional[GLib.Error] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def lookup_password(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_password_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str]: ...
    def lookup_password_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str]: ...
    def mail_signature_load(
        self,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def mail_signature_load_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, str, int]: ...
    def mail_signature_load_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str, int]: ...
    def mail_signature_replace(
        self,
        contents: str,
        length: int,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def mail_signature_replace_finish(self, result: Gio.AsyncResult) -> bool: ...
    def mail_signature_replace_sync(
        self,
        contents: str,
        length: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def mail_signature_symlink(
        self,
        symlink_target: str,
        io_priority: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def mail_signature_symlink_finish(self, result: Gio.AsyncResult) -> bool: ...
    def mail_signature_symlink_sync(
        self, symlink_target: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    @classmethod
    def new(
        cls,
        dbus_object: typing.Optional[Gio.DBusObject] = None,
        main_context: typing.Optional[GLib.MainContext] = None,
    ) -> Source: ...
    @classmethod
    def new_with_uid(
        cls, uid: str, main_context: typing.Optional[GLib.MainContext] = None
    ) -> Source: ...
    @staticmethod
    def parameter_to_key(param_name: str) -> str: ...
    def proxy_lookup(
        self,
        uri: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def proxy_lookup_finish(self, result: Gio.AsyncResult) -> list[str]: ...
    def proxy_lookup_sync(
        self, uri: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Optional[list[str]]: ...
    def ref_dbus_object(self) -> typing.Optional[Gio.DBusObject]: ...
    def ref_main_context(self) -> GLib.MainContext: ...
    def refresh_add_timeout(
        self,
        context: typing.Optional[GLib.MainContext],
        callback: typing.Callable[..., None],
        *user_data: typing.Any,
    ) -> int: ...
    def refresh_force_timeout(self) -> None: ...
    def refresh_remove_timeout(self, refresh_timeout_id: int) -> bool: ...
    def refresh_remove_timeouts_by_data(self, user_data: None) -> int: ...
    def remote_create(
        self,
        scratch_source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def remote_create_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remote_create_sync(
        self,
        scratch_source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def remote_delete(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def remote_delete_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remote_delete_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def remove(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def remove_finish(self, result: Gio.AsyncResult) -> bool: ...
    def remove_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_connection_status(
        self, connection_status: SourceConnectionStatus
    ) -> None: ...
    def set_display_name(self, display_name: str) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_parent(self, parent: typing.Optional[str] = None) -> None: ...
    def store_password(
        self,
        password: str,
        permanently: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def store_password_finish(self, result: Gio.AsyncResult) -> bool: ...
    def store_password_sync(
        self,
        password: str,
        permanently: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def to_string(self) -> typing.Tuple[str, int]: ...
    def unset_last_credentials_required_arguments(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def unset_last_credentials_required_arguments_finish(
        self, result: Gio.AsyncResult
    ) -> bool: ...
    def unset_last_credentials_required_arguments_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def write(
        self,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def write_finish(self, result: Gio.AsyncResult) -> bool: ...
    def write_sync(
        self, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...

class SourceAddressBook(SourceBackend):
    """
    :Constructors:

    ::

        SourceAddressBook(**properties)

    Object ESourceAddressBook

    Properties from ESourceAddressBook:
      order -> guint: Order
        A sorting order of the source

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceBackend.Props):
        order: int
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceBackend = ...
    priv: SourceAddressBookPrivate = ...
    def __init__(
        self,
        order: int = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def get_order(self) -> int: ...
    def set_order(self, order: int) -> None: ...

class SourceAddressBookClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceAddressBookClass()
    """

    parent_class: SourceBackendClass = ...

class SourceAddressBookPrivate(GObject.GPointer): ...

class SourceAlarms(SourceExtension):
    """
    :Constructors:

    ::

        SourceAlarms(**properties)

    Object ESourceAlarms

    Properties from ESourceAlarms:
      include-me -> gboolean: IncludeMe
        Include this source in alarm notifications
      last-notified -> gchararray: LastNotified
        Last alarm notification (in ISO 8601 format)
      for-every-event -> gboolean: ForEveryEvent
        Show a notification before every event in this source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        for_every_event: bool
        include_me: bool
        last_notified: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceAlarmsPrivate = ...
    def __init__(
        self,
        for_every_event: bool = ...,
        include_me: bool = ...,
        last_notified: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_last_notified(self) -> typing.Optional[str]: ...
    def get_for_every_event(self) -> bool: ...
    def get_include_me(self) -> bool: ...
    def get_last_notified(self) -> typing.Optional[str]: ...
    def set_for_every_event(self, for_every_event: bool) -> None: ...
    def set_include_me(self, include_me: bool) -> None: ...
    def set_last_notified(self, last_notified: typing.Optional[str] = None) -> None: ...

class SourceAlarmsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceAlarmsClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceAlarmsPrivate(GObject.GPointer): ...

class SourceAuthentication(SourceExtension):
    """
    :Constructors:

    ::

        SourceAuthentication(**properties)

    Object ESourceAuthentication

    Properties from ESourceAuthentication:
      connectable -> GSocketConnectable: Connectable
        A GSocketConnectable constructed from the host and port properties
      host -> gchararray: Host
        Host name for the remote account
      method -> gchararray: Method
        Authentication method
      port -> guint: Port
        Port number for the remote account
      proxy-uid -> gchararray: Proxy UID
        ESource UID of a proxy profile
      remember-password -> gboolean: Remember Password
        Whether to offer to remember the password by default when prompted
      user -> gchararray: User
        User name for the remote account
      credential-name -> gchararray: Credential Name
        What name to use for the authentication method in credentials for authentication
      is-external -> gboolean: Is External
        Whether the authentication is done by another authentication manager (like any Single Sign On daemon)

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        connectable: Gio.SocketConnectable
        credential_name: typing.Optional[str]
        host: typing.Optional[str]
        is_external: bool
        method: typing.Optional[str]
        port: int
        proxy_uid: str
        remember_password: bool
        user: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceAuthenticationPrivate = ...
    def __init__(
        self,
        credential_name: typing.Optional[str] = ...,
        host: typing.Optional[str] = ...,
        is_external: bool = ...,
        method: typing.Optional[str] = ...,
        port: int = ...,
        proxy_uid: str = ...,
        remember_password: bool = ...,
        user: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_credential_name(self) -> typing.Optional[str]: ...
    def dup_host(self) -> typing.Optional[str]: ...
    def dup_method(self) -> typing.Optional[str]: ...
    def dup_proxy_uid(self) -> str: ...
    def dup_user(self) -> typing.Optional[str]: ...
    def get_credential_name(self) -> typing.Optional[str]: ...
    def get_host(self) -> typing.Optional[str]: ...
    def get_is_external(self) -> bool: ...
    def get_method(self) -> typing.Optional[str]: ...
    def get_port(self) -> int: ...
    def get_proxy_uid(self) -> str: ...
    def get_remember_password(self) -> bool: ...
    def get_user(self) -> typing.Optional[str]: ...
    def ref_connectable(self) -> typing.Optional[Gio.SocketConnectable]: ...
    def required(self) -> bool: ...
    def set_credential_name(
        self, credential_name: typing.Optional[str] = None
    ) -> None: ...
    def set_host(self, host: typing.Optional[str] = None) -> None: ...
    def set_is_external(self, is_external: bool) -> None: ...
    def set_method(self, method: typing.Optional[str] = None) -> None: ...
    def set_port(self, port: int) -> None: ...
    def set_proxy_uid(self, proxy_uid: str) -> None: ...
    def set_remember_password(self, remember_password: bool) -> None: ...
    def set_user(self, user: typing.Optional[str] = None) -> None: ...

class SourceAuthenticationClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceAuthenticationClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceAuthenticationPrivate(GObject.GPointer): ...

class SourceAutocomplete(SourceExtension):
    """
    :Constructors:

    ::

        SourceAutocomplete(**properties)

    Object ESourceAutocomplete

    Properties from ESourceAutocomplete:
      include-me -> gboolean: IncludeMe
        Include this source when autocompleting

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        include_me: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceAutocompletePrivate = ...
    def __init__(self, include_me: bool = ..., source: Source = ...) -> None: ...
    def get_include_me(self) -> bool: ...
    def set_include_me(self, include_me: bool) -> None: ...

class SourceAutocompleteClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceAutocompleteClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceAutocompletePrivate(GObject.GPointer): ...

class SourceAutoconfig(SourceExtension):
    """
    :Constructors:

    ::

        SourceAutoconfig(**properties)

    Object ESourceAutoconfig

    Properties from ESourceAutoconfig:
      revision -> gchararray: Revision
        Identifier to map a particular version of a system-wide source to a user-specific source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        revision: str
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceAutoconfigPrivate = ...
    def __init__(self, revision: str = ..., source: Source = ...) -> None: ...
    def dup_revision(self) -> str: ...
    def get_revision(self) -> str: ...
    def set_revision(self, revision: str) -> None: ...

class SourceAutoconfigClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceAutoconfigClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceAutoconfigPrivate(GObject.GPointer): ...

class SourceBackend(SourceExtension):
    """
    :Constructors:

    ::

        SourceBackend(**properties)

    Object ESourceBackend

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceBackendPrivate = ...
    def __init__(
        self, backend_name: typing.Optional[str] = ..., source: Source = ...
    ) -> None: ...
    def dup_backend_name(self) -> typing.Optional[str]: ...
    def get_backend_name(self) -> typing.Optional[str]: ...
    def set_backend_name(self, backend_name: typing.Optional[str] = None) -> None: ...

class SourceBackendClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceBackendClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceBackendPrivate(GObject.GPointer): ...

class SourceCalendar(SourceSelectable):
    """
    :Constructors:

    ::

        SourceCalendar(**properties)

    Object ESourceCalendar

    Properties from ESourceSelectable:
      color -> gchararray: Color
        Textual specification of a color
      selected -> gboolean: Selected
        Whether the data source is selected
      order -> guint: Order
        Preferred sorting order

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceSelectable.Props):
        color: typing.Optional[str]
        order: int
        selected: bool
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceSelectable = ...
    priv: SourceCalendarPrivate = ...
    def __init__(
        self,
        color: typing.Optional[str] = ...,
        order: int = ...,
        selected: bool = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...

class SourceCalendarClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCalendarClass()
    """

    parent_class: SourceSelectableClass = ...

class SourceCalendarPrivate(GObject.GPointer): ...

class SourceCamel(SourceExtension):
    """
    :Constructors:

    ::

        SourceCamel(**properties)

    Object ESourceCamel

    Properties from ESourceCamel:
      settings -> CamelSettings: Settings
        The CamelSettings instance being proxied

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        settings: Camel.Settings
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceCamelPrivate = ...
    def __init__(self, source: Source = ...) -> None: ...
    @staticmethod
    def generate_subtype(
        protocol: str, settings_type: typing.Type[typing.Any]
    ) -> typing.Type[typing.Any]: ...
    @staticmethod
    def get_extension_name(protocol: str) -> str: ...
    def get_settings(self) -> Camel.Settings: ...
    @staticmethod
    def get_type_name(protocol: str) -> str: ...
    @staticmethod
    def register_types() -> None: ...

class SourceCamelClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCamelClass()
    """

    parent_class: SourceExtensionClass = ...
    settings_type: typing.Type[typing.Any] = ...

class SourceCamelPrivate(GObject.GPointer): ...

class SourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceClass()
    """

    parent_class: GObject.ObjectClass = ...
    changed: typing.Callable[[Source], None] = ...
    credentials_required: typing.Callable[
        [Source, SourceCredentialsReason, str, Gio.TlsCertificateFlags, GLib.Error],
        None,
    ] = ...
    authenticate: typing.Callable[[Source, NamedParameters], None] = ...
    remove_sync: typing.Callable[[Source, typing.Optional[Gio.Cancellable]], bool] = ...
    remove: typing.Callable[..., None] = ...
    remove_finish: typing.Callable[[Source, Gio.AsyncResult], bool] = ...
    write_sync: typing.Callable[[Source, typing.Optional[Gio.Cancellable]], bool] = ...
    write: typing.Callable[..., None] = ...
    write_finish: typing.Callable[[Source, Gio.AsyncResult], bool] = ...
    remote_create_sync: typing.Callable[
        [Source, Source, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    remote_create: typing.Callable[..., None] = ...
    remote_create_finish: typing.Callable[[Source, Gio.AsyncResult], bool] = ...
    remote_delete_sync: typing.Callable[
        [Source, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    remote_delete: typing.Callable[..., None] = ...
    remote_delete_finish: typing.Callable[[Source, Gio.AsyncResult], bool] = ...
    get_oauth2_access_token_sync: typing.Callable[
        [Source, typing.Optional[Gio.Cancellable]], typing.Tuple[bool, str, int]
    ] = ...
    get_oauth2_access_token: typing.Callable[..., None] = ...
    get_oauth2_access_token_finish: typing.Callable[
        [Source, Gio.AsyncResult], typing.Tuple[bool, str, int]
    ] = ...
    invoke_credentials_required_impl: typing.Callable[
        [Source, None, str, str, str, str, str, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    invoke_authenticate_impl: typing.Callable[
        [Source, None, str, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    unset_last_credentials_required_arguments_impl: typing.Callable[
        [Source, typing.Optional[Gio.Cancellable]], bool
    ] = ...
    reserved: list[None] = ...

class SourceCollection(SourceBackend):
    """
    :Constructors:

    ::

        SourceCollection(**properties)

    Object ESourceCollection

    Properties from ESourceCollection:
      calendar-enabled -> gboolean: Calendar Enabled
        Whether calendar resources are enabled
      contacts-enabled -> gboolean: Contacts Enabled
        Whether contact resources are enabled
      identity -> gchararray: Identity
        Uniquely identifies the account at the service provider
      mail-enabled -> gboolean: Mail Enabled
        Whether mail resources are enabled
      allow-sources-rename -> gboolean: Allow Sources Rename
        Set to TRUE when the collection source allows user rename the child sources
      calendar-url -> gchararray: Calendar URL
        Calendar top URL
      contacts-url -> gchararray: Contacts URL
        Contacts top URL

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceBackend.Props):
        allow_sources_rename: bool
        calendar_enabled: bool
        calendar_url: typing.Optional[str]
        contacts_enabled: bool
        contacts_url: typing.Optional[str]
        identity: typing.Optional[str]
        mail_enabled: bool
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceBackend = ...
    priv: SourceCollectionPrivate = ...
    def __init__(
        self,
        allow_sources_rename: bool = ...,
        calendar_enabled: bool = ...,
        calendar_url: typing.Optional[str] = ...,
        contacts_enabled: bool = ...,
        contacts_url: typing.Optional[str] = ...,
        identity: typing.Optional[str] = ...,
        mail_enabled: bool = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_calendar_url(self) -> typing.Optional[str]: ...
    def dup_contacts_url(self) -> typing.Optional[str]: ...
    def dup_identity(self) -> typing.Optional[str]: ...
    def get_allow_sources_rename(self) -> bool: ...
    def get_calendar_enabled(self) -> bool: ...
    def get_calendar_url(self) -> typing.Optional[str]: ...
    def get_contacts_enabled(self) -> bool: ...
    def get_contacts_url(self) -> typing.Optional[str]: ...
    def get_identity(self) -> typing.Optional[str]: ...
    def get_mail_enabled(self) -> bool: ...
    def set_allow_sources_rename(self, allow_sources_rename: bool) -> None: ...
    def set_calendar_enabled(self, calendar_enabled: bool) -> None: ...
    def set_calendar_url(self, calendar_url: typing.Optional[str] = None) -> None: ...
    def set_contacts_enabled(self, contacts_enabled: bool) -> None: ...
    def set_contacts_url(self, contacts_url: typing.Optional[str] = None) -> None: ...
    def set_identity(self, identity: typing.Optional[str] = None) -> None: ...
    def set_mail_enabled(self, mail_enabled: bool) -> None: ...

class SourceCollectionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCollectionClass()
    """

    parent_class: SourceBackendClass = ...

class SourceCollectionPrivate(GObject.GPointer): ...

class SourceContacts(SourceExtension):
    """
    :Constructors:

    ::

        SourceContacts(**properties)

    Object ESourceContacts

    Properties from ESourceContacts:
      include-me -> gboolean: Include Me
        Include this address book in the contacts calendar

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        include_me: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceContactsPrivate = ...
    def __init__(self, include_me: bool = ..., source: Source = ...) -> None: ...
    def get_include_me(self) -> bool: ...
    def set_include_me(self, include_me: bool) -> None: ...

class SourceContactsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceContactsClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceContactsPrivate(GObject.GPointer): ...

class SourceCredentialsProvider(GObject.Object, Extensible):
    """
    :Constructors:

    ::

        SourceCredentialsProvider(**properties)
        new(registry:EDataServer.SourceRegistry) -> EDataServer.SourceCredentialsProvider

    Object ESourceCredentialsProvider

    Properties from ESourceCredentialsProvider:
      registry -> GObject: Registry
        An ESourceRegistry

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        registry: GObject.Object

    props: Props = ...
    parent: GObject.Object = ...
    priv: SourceCredentialsProviderPrivate = ...
    def __init__(self, registry: GObject.Object = ...) -> None: ...
    def can_prompt(self, source: Source) -> bool: ...
    def can_store(self, source: Source) -> bool: ...
    def delete(
        self,
        source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def delete_finish(self, result: Gio.AsyncResult) -> bool: ...
    def delete_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_ref_source(self, uid: str) -> typing.Optional[Source]: ...
    def lookup(
        self,
        source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def lookup_finish(
        self, result: Gio.AsyncResult
    ) -> typing.Tuple[bool, NamedParameters]: ...
    def lookup_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, NamedParameters]: ...
    @classmethod
    def new(cls, registry: SourceRegistry) -> SourceCredentialsProvider: ...
    def ref_credentials_source(self, source: Source) -> typing.Optional[Source]: ...
    def ref_registry(self) -> GObject.Object: ...
    def ref_source(self, uid: str) -> typing.Optional[Source]: ...
    def register_impl(self, provider_impl: SourceCredentialsProviderImpl) -> bool: ...
    def store(
        self,
        source: Source,
        credentials: NamedParameters,
        permanently: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def store_finish(self, result: Gio.AsyncResult) -> bool: ...
    def store_sync(
        self,
        source: Source,
        credentials: NamedParameters,
        permanently: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def unregister_impl(self, provider_impl: SourceCredentialsProviderImpl) -> None: ...

class SourceCredentialsProviderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCredentialsProviderClass()
    """

    parent_class: GObject.ObjectClass = ...
    ref_source: typing.Callable[
        [SourceCredentialsProvider, str], typing.Optional[Source]
    ] = ...

class SourceCredentialsProviderImpl(Extension):
    """
    :Constructors:

    ::

        SourceCredentialsProviderImpl(**properties)

    Object ESourceCredentialsProviderImpl

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(Extension.Props):
        extensible: Extensible

    props: Props = ...
    parent: Extension = ...
    priv: SourceCredentialsProviderImplPrivate = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...
    def can_process(self, source: Source) -> bool: ...
    def can_prompt(self) -> bool: ...
    def can_store(self) -> bool: ...
    def delete_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_can_process(self, source: Source) -> bool: ...
    def do_can_prompt(self) -> bool: ...
    def do_can_store(self) -> bool: ...
    def do_delete_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def do_lookup_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, NamedParameters]: ...
    def do_store_sync(
        self,
        source: Source,
        credentials: NamedParameters,
        permanently: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def get_provider(self) -> None: ...
    def lookup_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, NamedParameters]: ...
    def store_sync(
        self,
        source: Source,
        credentials: NamedParameters,
        permanently: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...

class SourceCredentialsProviderImplClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCredentialsProviderImplClass()
    """

    parent_class: ExtensionClass = ...
    can_process: typing.Callable[[SourceCredentialsProviderImpl, Source], bool] = ...
    can_store: typing.Callable[[SourceCredentialsProviderImpl], bool] = ...
    can_prompt: typing.Callable[[SourceCredentialsProviderImpl], bool] = ...
    lookup_sync: typing.Callable[
        [SourceCredentialsProviderImpl, Source, typing.Optional[Gio.Cancellable]],
        typing.Tuple[bool, NamedParameters],
    ] = ...
    store_sync: typing.Callable[
        [
            SourceCredentialsProviderImpl,
            Source,
            NamedParameters,
            bool,
            typing.Optional[Gio.Cancellable],
        ],
        bool,
    ] = ...
    delete_sync: typing.Callable[
        [SourceCredentialsProviderImpl, Source, typing.Optional[Gio.Cancellable]], bool
    ] = ...

class SourceCredentialsProviderImplOAuth2(SourceCredentialsProviderImpl):
    """
    :Constructors:

    ::

        SourceCredentialsProviderImplOAuth2(**properties)

    Object ESourceCredentialsProviderImplOAuth2

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceCredentialsProviderImpl.Props):
        extensible: Extensible

    props: Props = ...
    parent: SourceCredentialsProviderImpl = ...
    priv: SourceCredentialsProviderImplOAuth2Private = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...

class SourceCredentialsProviderImplOAuth2Class(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCredentialsProviderImplOAuth2Class()
    """

    parent_class: SourceCredentialsProviderImplClass = ...

class SourceCredentialsProviderImplOAuth2Private(GObject.GPointer): ...

class SourceCredentialsProviderImplPassword(SourceCredentialsProviderImpl):
    """
    :Constructors:

    ::

        SourceCredentialsProviderImplPassword(**properties)

    Object ESourceCredentialsProviderImplPassword

    Properties from EExtension:
      extensible -> EExtensible: Extensible Object
        The object being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceCredentialsProviderImpl.Props):
        extensible: Extensible

    props: Props = ...
    parent: SourceCredentialsProviderImpl = ...
    priv: SourceCredentialsProviderImplPasswordPrivate = ...
    def __init__(self, extensible: Extensible = ...) -> None: ...

class SourceCredentialsProviderImplPasswordClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceCredentialsProviderImplPasswordClass()
    """

    parent_class: SourceCredentialsProviderImplClass = ...

class SourceCredentialsProviderImplPasswordPrivate(GObject.GPointer): ...
class SourceCredentialsProviderImplPrivate(GObject.GPointer): ...
class SourceCredentialsProviderPrivate(GObject.GPointer): ...

class SourceExtension(GObject.Object):
    """
    :Constructors:

    ::

        SourceExtension(**properties)

    Object ESourceExtension

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        source: Source

    props: Props = ...
    parent: GObject.Object = ...
    priv: SourceExtensionPrivate = ...
    def __init__(self, source: Source = ...) -> None: ...
    def get_source(self) -> Source: ...
    def property_lock(self) -> None: ...
    def property_unlock(self) -> None: ...
    def ref_source(self) -> Source: ...

class SourceExtensionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceExtensionClass()
    """

    parent_class: GObject.ObjectClass = ...
    name: str = ...

class SourceExtensionPrivate(GObject.GPointer): ...

class SourceGoa(SourceExtension):
    """
    :Constructors:

    ::

        SourceGoa(**properties)

    Object ESourceGoa

    Properties from ESourceGoa:
      account-id -> gchararray: Account ID
        GNOME Online Account ID
      calendar-url -> gchararray: Calendar URL
        GNOME Online Calendar URL
      contacts-url -> gchararray: Contacts URL
        GNOME Online Contacts URL
      name -> gchararray: Name
        GNOME Online Account's original Name
      address -> gchararray: Address
        GNOME Online Account's original Address

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        account_id: typing.Optional[str]
        address: typing.Optional[str]
        calendar_url: typing.Optional[str]
        contacts_url: typing.Optional[str]
        name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceGoaPrivate = ...
    def __init__(
        self,
        account_id: typing.Optional[str] = ...,
        address: typing.Optional[str] = ...,
        calendar_url: typing.Optional[str] = ...,
        contacts_url: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_account_id(self) -> typing.Optional[str]: ...
    def dup_address(self) -> typing.Optional[str]: ...
    def dup_calendar_url(self) -> typing.Optional[str]: ...
    def dup_contacts_url(self) -> typing.Optional[str]: ...
    def dup_name(self) -> typing.Optional[str]: ...
    def get_account_id(self) -> typing.Optional[str]: ...
    def get_address(self) -> typing.Optional[str]: ...
    def get_calendar_url(self) -> typing.Optional[str]: ...
    def get_contacts_url(self) -> typing.Optional[str]: ...
    def get_name(self) -> typing.Optional[str]: ...
    def set_account_id(self, account_id: typing.Optional[str] = None) -> None: ...
    def set_address(self, address: typing.Optional[str] = None) -> None: ...
    def set_calendar_url(self, calendar_url: typing.Optional[str] = None) -> None: ...
    def set_contacts_url(self, contacts_url: typing.Optional[str] = None) -> None: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...

class SourceGoaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceGoaClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceGoaPrivate(GObject.GPointer): ...

class SourceLDAP(SourceExtension):
    """
    :Constructors:

    ::

        SourceLDAP(**properties)

    Object ESourceLDAP

    Properties from ESourceLDAP:
      authentication -> ESourceLDAPAuthentication: Authentication
        LDAP authentication method
      can-browse -> gboolean: Can Browse
        Allow browsing contacts
      filter -> gchararray: Filter
        LDAP search filter
      limit -> guint: Limit
        Download limit
      root-dn -> gchararray: Root DN
        LDAP search base
      scope -> ESourceLDAPScope: Scope
        LDAP search scope
      security -> ESourceLDAPSecurity: Security
        LDAP security method

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        authentication: SourceLDAPAuthentication
        can_browse: bool
        filter: str
        limit: int
        root_dn: str
        scope: SourceLDAPScope
        security: SourceLDAPSecurity
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceLDAPPrivate = ...
    def __init__(
        self,
        authentication: SourceLDAPAuthentication = ...,
        can_browse: bool = ...,
        filter: str = ...,
        limit: int = ...,
        root_dn: str = ...,
        scope: SourceLDAPScope = ...,
        security: SourceLDAPSecurity = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_filter(self) -> str: ...
    def dup_root_dn(self) -> str: ...
    def get_authentication(self) -> SourceLDAPAuthentication: ...
    def get_can_browse(self) -> bool: ...
    def get_filter(self) -> str: ...
    def get_limit(self) -> int: ...
    def get_root_dn(self) -> str: ...
    def get_scope(self) -> SourceLDAPScope: ...
    def get_security(self) -> SourceLDAPSecurity: ...
    def set_authentication(self, authentication: SourceLDAPAuthentication) -> None: ...
    def set_can_browse(self, can_browse: bool) -> None: ...
    def set_filter(self, filter: str) -> None: ...
    def set_limit(self, limit: int) -> None: ...
    def set_root_dn(self, root_dn: str) -> None: ...
    def set_scope(self, scope: SourceLDAPScope) -> None: ...
    def set_security(self, security: SourceLDAPSecurity) -> None: ...

class SourceLDAPClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceLDAPClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceLDAPPrivate(GObject.GPointer): ...

class SourceLocal(SourceExtension):
    """
    :Constructors:

    ::

        SourceLocal(**properties)

    Object ESourceLocal

    Properties from ESourceLocal:
      custom-file -> GFile: Custom File
        Custom iCalendar file
      email-address -> gchararray: Email Address
        Email address associated with the calendar
      writable -> gboolean: Writable
        Whether the file can be opened in writable mode

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        custom_file: typing.Optional[Gio.File]
        email_address: typing.Optional[str]
        writable: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceLocalPrivate = ...
    def __init__(
        self,
        custom_file: typing.Optional[Gio.File] = ...,
        email_address: typing.Optional[str] = ...,
        writable: bool = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_custom_file(self) -> typing.Optional[Gio.File]: ...
    def dup_email_address(self) -> str: ...
    def get_custom_file(self) -> typing.Optional[Gio.File]: ...
    def get_email_address(self) -> typing.Optional[str]: ...
    def get_writable(self) -> bool: ...
    def set_custom_file(
        self, custom_file: typing.Optional[Gio.File] = None
    ) -> None: ...
    def set_email_address(self, email_address: typing.Optional[str] = None) -> None: ...
    def set_writable(self, writable: bool) -> None: ...

class SourceLocalClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceLocalClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceLocalPrivate(GObject.GPointer): ...

class SourceMDN(SourceExtension):
    """
    :Constructors:

    ::

        SourceMDN(**properties)

    Object ESourceMDN

    Properties from ESourceMDN:
      response-policy -> EMdnResponsePolicy: Response Policy
        Policy for responding to MDN requests

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        response_policy: MdnResponsePolicy
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceMDNPrivate = ...
    def __init__(
        self, response_policy: MdnResponsePolicy = ..., source: Source = ...
    ) -> None: ...
    def get_response_policy(self) -> MdnResponsePolicy: ...
    def set_response_policy(self, response_policy: MdnResponsePolicy) -> None: ...

class SourceMDNClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMDNClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceMDNPrivate(GObject.GPointer): ...

class SourceMailAccount(SourceBackend):
    """
    :Constructors:

    ::

        SourceMailAccount(**properties)

    Object ESourceMailAccount

    Properties from ESourceMailAccount:
      identity-uid -> gchararray: Identity UID
        ESource UID of a Mail Identity
      archive-folder -> gchararray: Archive Folder
        Folder to Archive messages in
      needs-initial-setup -> gboolean: Needs Initial Setup
        Whether the account needs to do an initial setup
      mark-seen -> EThreeState: Mark Seen
        Three-state option for Mark messages as read after N seconds
      mark-seen-timeout -> gint: Mark Seen Timeout
        Timeout in milliseconds for Mark messages as read after N seconds
      builtin -> gboolean: Builtin
        Whether the account is builtin

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceBackend.Props):
        archive_folder: typing.Optional[str]
        builtin: bool
        identity_uid: typing.Optional[str]
        mark_seen: ThreeState
        mark_seen_timeout: int
        needs_initial_setup: bool
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceBackend = ...
    priv: SourceMailAccountPrivate = ...
    def __init__(
        self,
        archive_folder: typing.Optional[str] = ...,
        builtin: bool = ...,
        identity_uid: typing.Optional[str] = ...,
        mark_seen: ThreeState = ...,
        mark_seen_timeout: int = ...,
        needs_initial_setup: bool = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_archive_folder(self) -> typing.Optional[str]: ...
    def dup_identity_uid(self) -> typing.Optional[str]: ...
    def get_archive_folder(self) -> typing.Optional[str]: ...
    def get_builtin(self) -> bool: ...
    def get_identity_uid(self) -> typing.Optional[str]: ...
    def get_mark_seen(self) -> ThreeState: ...
    def get_mark_seen_timeout(self) -> int: ...
    def get_needs_initial_setup(self) -> bool: ...
    def set_archive_folder(
        self, archive_folder: typing.Optional[str] = None
    ) -> None: ...
    def set_builtin(self, builtin: int) -> None: ...
    def set_identity_uid(self, identity_uid: typing.Optional[str] = None) -> None: ...
    def set_mark_seen(self, mark_seen: ThreeState) -> None: ...
    def set_mark_seen_timeout(self, timeout: int) -> None: ...
    def set_needs_initial_setup(self, needs_initial_setup: bool) -> None: ...

class SourceMailAccountClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMailAccountClass()
    """

    parent_class: SourceBackendClass = ...

class SourceMailAccountPrivate(GObject.GPointer): ...

class SourceMailComposition(SourceExtension):
    """
    :Constructors:

    ::

        SourceMailComposition(**properties)

    Object ESourceMailComposition

    Properties from ESourceMailComposition:
      bcc -> GStrv: Bcc
        Recipients to blind carbon-copy
      cc -> GStrv: Cc
        Recipients to carbon-copy
      drafts-folder -> gchararray: Drafts Folder
        Preferred folder for draft messages
      reply-style -> ESourceMailCompositionReplyStyle: Reply Style
        What reply style to prefer
      sign-imip -> gboolean: Sign iMIP
        Include iMIP messages when signing
      templates-folder -> gchararray: Templates Folder
        Preferred folder for message templates
      start-bottom -> EThreeState: Start Bottom
        Whether start at bottom on reply or forward
      top-signature -> EThreeState: Top Signature
        Whether place signature at the top on reply or forward
      language -> gchararray: Language
        Preferred language

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        bcc: list[str]
        cc: list[str]
        drafts_folder: typing.Optional[str]
        language: typing.Optional[str]
        reply_style: SourceMailCompositionReplyStyle
        sign_imip: bool
        start_bottom: ThreeState
        templates_folder: typing.Optional[str]
        top_signature: ThreeState
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceMailCompositionPrivate = ...
    def __init__(
        self,
        bcc: typing.Sequence[str] = ...,
        cc: typing.Sequence[str] = ...,
        drafts_folder: typing.Optional[str] = ...,
        language: typing.Optional[str] = ...,
        reply_style: SourceMailCompositionReplyStyle = ...,
        sign_imip: bool = ...,
        start_bottom: ThreeState = ...,
        templates_folder: typing.Optional[str] = ...,
        top_signature: ThreeState = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_bcc(self) -> list[str]: ...
    def dup_cc(self) -> list[str]: ...
    def dup_drafts_folder(self) -> typing.Optional[str]: ...
    def dup_language(self) -> typing.Optional[str]: ...
    def dup_templates_folder(self) -> typing.Optional[str]: ...
    def get_bcc(self) -> list[str]: ...
    def get_cc(self) -> list[str]: ...
    def get_drafts_folder(self) -> typing.Optional[str]: ...
    def get_language(self) -> typing.Optional[str]: ...
    def get_reply_style(self) -> SourceMailCompositionReplyStyle: ...
    def get_sign_imip(self) -> bool: ...
    def get_start_bottom(self) -> ThreeState: ...
    def get_templates_folder(self) -> typing.Optional[str]: ...
    def get_top_signature(self) -> ThreeState: ...
    def set_bcc(self, bcc: typing.Sequence[str]) -> None: ...
    def set_cc(self, cc: typing.Sequence[str]) -> None: ...
    def set_drafts_folder(self, drafts_folder: typing.Optional[str] = None) -> None: ...
    def set_language(self, language: typing.Optional[str] = None) -> None: ...
    def set_reply_style(self, reply_style: SourceMailCompositionReplyStyle) -> None: ...
    def set_sign_imip(self, sign_imip: bool) -> None: ...
    def set_start_bottom(self, start_bottom: ThreeState) -> None: ...
    def set_templates_folder(
        self, templates_folder: typing.Optional[str] = None
    ) -> None: ...
    def set_top_signature(self, top_signature: ThreeState) -> None: ...

class SourceMailCompositionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMailCompositionClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceMailCompositionPrivate(GObject.GPointer): ...

class SourceMailIdentity(SourceExtension):
    """
    :Constructors:

    ::

        SourceMailIdentity(**properties)

    Object ESourceMailIdentity

    Properties from ESourceMailIdentity:
      address -> gchararray: Address
        Sender's email address
      aliases -> gchararray: Aliases
        Sender's email address aliases
      name -> gchararray: Name
        Sender's name
      organization -> gchararray: Organization
        Sender's organization
      reply-to -> gchararray: Reply-To
        Sender's reply-to address
      signature-uid -> gchararray: Signature UID
        ESource UID of the sender's signature

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        address: typing.Optional[str]
        aliases: typing.Optional[str]
        name: typing.Optional[str]
        organization: typing.Optional[str]
        reply_to: typing.Optional[str]
        signature_uid: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceMailIdentityPrivate = ...
    def __init__(
        self,
        address: typing.Optional[str] = ...,
        aliases: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        organization: typing.Optional[str] = ...,
        reply_to: typing.Optional[str] = ...,
        signature_uid: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_address(self) -> typing.Optional[str]: ...
    def dup_aliases(self) -> typing.Optional[str]: ...
    def dup_name(self) -> typing.Optional[str]: ...
    def dup_organization(self) -> typing.Optional[str]: ...
    def dup_reply_to(self) -> typing.Optional[str]: ...
    def dup_signature_uid(self) -> typing.Optional[str]: ...
    def get_address(self) -> typing.Optional[str]: ...
    def get_aliases(self) -> typing.Optional[str]: ...
    def get_aliases_as_hash_table(self) -> typing.Optional[dict[str, str]]: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_organization(self) -> typing.Optional[str]: ...
    def get_reply_to(self) -> typing.Optional[str]: ...
    def get_signature_uid(self) -> typing.Optional[str]: ...
    def set_address(self, address: typing.Optional[str] = None) -> None: ...
    def set_aliases(self, aliases: typing.Optional[str] = None) -> None: ...
    def set_name(self, name: typing.Optional[str] = None) -> None: ...
    def set_organization(self, organization: typing.Optional[str] = None) -> None: ...
    def set_reply_to(self, reply_to: typing.Optional[str] = None) -> None: ...
    def set_signature_uid(self, signature_uid: typing.Optional[str] = None) -> None: ...

class SourceMailIdentityClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMailIdentityClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceMailIdentityPrivate(GObject.GPointer): ...

class SourceMailSignature(SourceExtension):
    """
    :Constructors:

    ::

        SourceMailSignature(**properties)

    Object ESourceMailSignature

    Properties from ESourceMailSignature:
      file -> GFile: File
        File containing signature content
      mime-type -> gchararray: MIME Type
        MIME type of the signature content

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        file: Gio.File
        mime_type: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceMailSignaturePrivate = ...
    def __init__(
        self, mime_type: typing.Optional[str] = ..., source: Source = ...
    ) -> None: ...
    def dup_mime_type(self) -> typing.Optional[str]: ...
    def get_file(self) -> Gio.File: ...
    def get_mime_type(self) -> typing.Optional[str]: ...
    def set_mime_type(self, mime_type: typing.Optional[str] = None) -> None: ...

class SourceMailSignatureClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMailSignatureClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceMailSignaturePrivate(GObject.GPointer): ...

class SourceMailSubmission(SourceExtension):
    """
    :Constructors:

    ::

        SourceMailSubmission(**properties)

    Object ESourceMailSubmission

    Properties from ESourceMailSubmission:
      sent-folder -> gchararray: Sent Folder
        Preferred folder for sent messages
      transport-uid -> gchararray: Transport UID
        ESource UID of a Mail Transport
      replies-to-origin-folder -> gboolean: Replies to origin folder
        Whether to save replies to folder of the message being replied to, instead of the Sent folder
      use-sent-folder -> gboolean: Use Sent Folder
        Whether to save sent messages to sent-folder

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        replies_to_origin_folder: bool
        sent_folder: typing.Optional[str]
        transport_uid: typing.Optional[str]
        use_sent_folder: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceMailSubmissionPrivate = ...
    def __init__(
        self,
        replies_to_origin_folder: bool = ...,
        sent_folder: typing.Optional[str] = ...,
        transport_uid: typing.Optional[str] = ...,
        use_sent_folder: bool = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_sent_folder(self) -> typing.Optional[str]: ...
    def dup_transport_uid(self) -> typing.Optional[str]: ...
    def get_replies_to_origin_folder(self) -> bool: ...
    def get_sent_folder(self) -> typing.Optional[str]: ...
    def get_transport_uid(self) -> typing.Optional[str]: ...
    def get_use_sent_folder(self) -> bool: ...
    def set_replies_to_origin_folder(self, replies_to_origin_folder: bool) -> None: ...
    def set_sent_folder(self, sent_folder: typing.Optional[str] = None) -> None: ...
    def set_transport_uid(self, transport_uid: typing.Optional[str] = None) -> None: ...
    def set_use_sent_folder(self, use_sent_folder: bool) -> None: ...

class SourceMailSubmissionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMailSubmissionClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceMailSubmissionPrivate(GObject.GPointer): ...

class SourceMailTransport(SourceBackend):
    """
    :Constructors:

    ::

        SourceMailTransport(**properties)

    Object ESourceMailTransport

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceBackend.Props):
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceBackend = ...
    priv: SourceMailTransportPrivate = ...
    def __init__(
        self, backend_name: typing.Optional[str] = ..., source: Source = ...
    ) -> None: ...

class SourceMailTransportClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMailTransportClass()
    """

    parent_class: SourceBackendClass = ...

class SourceMailTransportPrivate(GObject.GPointer): ...

class SourceMemoList(SourceSelectable):
    """
    :Constructors:

    ::

        SourceMemoList(**properties)

    Object ESourceMemoList

    Properties from ESourceSelectable:
      color -> gchararray: Color
        Textual specification of a color
      selected -> gboolean: Selected
        Whether the data source is selected
      order -> guint: Order
        Preferred sorting order

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceSelectable.Props):
        color: typing.Optional[str]
        order: int
        selected: bool
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceSelectable = ...
    priv: SourceMemoListPrivate = ...
    def __init__(
        self,
        color: typing.Optional[str] = ...,
        order: int = ...,
        selected: bool = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...

class SourceMemoListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceMemoListClass()
    """

    parent_class: SourceSelectableClass = ...

class SourceMemoListPrivate(GObject.GPointer): ...

class SourceOffline(SourceExtension):
    """
    :Constructors:

    ::

        SourceOffline(**properties)

    Object ESourceOffline

    Properties from ESourceOffline:
      stay-synchronized -> gboolean: StaySynchronized
        Keep remote content synchronized locally

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        stay_synchronized: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceOfflinePrivate = ...
    def __init__(self, stay_synchronized: bool = ..., source: Source = ...) -> None: ...
    def get_stay_synchronized(self) -> bool: ...
    def set_stay_synchronized(self, stay_synchronized: bool) -> None: ...

class SourceOfflineClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceOfflineClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceOfflinePrivate(GObject.GPointer): ...

class SourceOpenPGP(SourceExtension):
    """
    :Constructors:

    ::

        SourceOpenPGP(**properties)

    Object ESourceOpenPGP

    Properties from ESourceOpenPGP:
      always-trust -> gboolean: Always Trust
        Always trust keys in my keyring
      encrypt-to-self -> gboolean: Encrypt To Self
        Always encrypt to myself
      key-id -> gchararray: Key ID
        PGP/GPG Key ID
      signing-algorithm -> gchararray: Signing Algorithm
        Hash algorithm used to sign messages
      sign-by-default -> gboolean: Sign By Default
        Sign outgoing messages by default
      encrypt-by-default -> gboolean: Encrypt By Default
        Encrypt outgoing messages by default
      prefer-inline -> gboolean: Prefer inline
        Prefer inline sign/encrypt
      locate-keys -> gboolean: Locate Keys
        Locate keys in WKD for encryption
      send-public-key -> gboolean: Send Public Key
        Send public key in messages
      send-prefer-encrypt -> gboolean: Send Prefer Encrypt
        Send whether prefers encryption together with the public key in messages
      ask-send-public-key -> gboolean: Ask Send Public Key
        Ask before sending public key in messages

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        always_trust: bool
        ask_send_public_key: bool
        encrypt_by_default: bool
        encrypt_to_self: bool
        key_id: str
        locate_keys: bool
        prefer_inline: bool
        send_prefer_encrypt: bool
        send_public_key: bool
        sign_by_default: bool
        signing_algorithm: str
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceOpenPGPPrivate = ...
    def __init__(
        self,
        always_trust: bool = ...,
        ask_send_public_key: bool = ...,
        encrypt_by_default: bool = ...,
        encrypt_to_self: bool = ...,
        key_id: str = ...,
        locate_keys: bool = ...,
        prefer_inline: bool = ...,
        send_prefer_encrypt: bool = ...,
        send_public_key: bool = ...,
        sign_by_default: bool = ...,
        signing_algorithm: str = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_key_id(self) -> str: ...
    def dup_signing_algorithm(self) -> str: ...
    def get_always_trust(self) -> bool: ...
    def get_ask_send_public_key(self) -> bool: ...
    def get_encrypt_by_default(self) -> bool: ...
    def get_encrypt_to_self(self) -> bool: ...
    def get_key_id(self) -> str: ...
    def get_locate_keys(self) -> bool: ...
    def get_prefer_inline(self) -> bool: ...
    def get_send_prefer_encrypt(self) -> bool: ...
    def get_send_public_key(self) -> bool: ...
    def get_sign_by_default(self) -> bool: ...
    def get_signing_algorithm(self) -> str: ...
    def set_always_trust(self, always_trust: bool) -> None: ...
    def set_ask_send_public_key(self, ask_send_public_key: bool) -> None: ...
    def set_encrypt_by_default(self, encrypt_by_default: bool) -> None: ...
    def set_encrypt_to_self(self, encrypt_to_self: bool) -> None: ...
    def set_key_id(self, key_id: str) -> None: ...
    def set_locate_keys(self, locate_keys: bool) -> None: ...
    def set_prefer_inline(self, prefer_inline: bool) -> None: ...
    def set_send_prefer_encrypt(self, send_prefer_encrypt: bool) -> None: ...
    def set_send_public_key(self, send_public_key: bool) -> None: ...
    def set_sign_by_default(self, sign_by_default: bool) -> None: ...
    def set_signing_algorithm(self, signing_algorithm: str) -> None: ...

class SourceOpenPGPClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceOpenPGPClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceOpenPGPPrivate(GObject.GPointer): ...
class SourcePrivate(GObject.GPointer): ...

class SourceProxy(SourceExtension):
    """
    :Constructors:

    ::

        SourceProxy(**properties)

    Object ESourceProxy

    Properties from ESourceProxy:
      autoconfig-url -> gchararray: Autoconfig URL
        Proxy autoconfiguration URL
      ftp-host -> gchararray: FTP Host
        FTP proxy host name
      ftp-port -> guint: FTP Port
        FTP proxy port
      http-auth-password -> gchararray: HTTP Auth Password
        HTTP proxy password
      http-auth-user -> gchararray: HTTP Auth User
        HTTP proxy username
      http-host -> gchararray: HTTP Host
        HTTP proxy host name
      http-port -> guint: HTTP Port
        HTTP proxy port
      http-use-auth -> gboolean: HTTP Use Auth
        Whether HTTP proxy server connections require authentication
      https-host -> gchararray: HTTPS Host
        Secure HTTP proxy host name
      https-port -> guint: HTTPS Port
        Secure HTTP proxy port
      ignore-hosts -> GStrv: Ignore Hosts
        Hosts to connect directly
      method -> EProxyMethod: Method
        Proxy configuration method
      socks-host -> gchararray: SOCKS Host
        SOCKS proxy host name
      socks-port -> guint: SOCKS Port
        SOCKS proxy port

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        autoconfig_url: str
        ftp_host: str
        ftp_port: int
        http_auth_password: str
        http_auth_user: str
        http_host: str
        http_port: int
        http_use_auth: bool
        https_host: str
        https_port: int
        ignore_hosts: list[str]
        method: ProxyMethod
        socks_host: str
        socks_port: int
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceProxyPrivate = ...
    def __init__(
        self,
        autoconfig_url: str = ...,
        ftp_host: str = ...,
        ftp_port: int = ...,
        http_auth_password: str = ...,
        http_auth_user: str = ...,
        http_host: str = ...,
        http_port: int = ...,
        http_use_auth: bool = ...,
        https_host: str = ...,
        https_port: int = ...,
        ignore_hosts: typing.Sequence[str] = ...,
        method: ProxyMethod = ...,
        socks_host: str = ...,
        socks_port: int = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_autoconfig_url(self) -> str: ...
    def dup_ftp_host(self) -> str: ...
    def dup_http_auth_password(self) -> str: ...
    def dup_http_auth_user(self) -> str: ...
    def dup_http_host(self) -> str: ...
    def dup_https_host(self) -> str: ...
    def dup_ignore_hosts(self) -> list[str]: ...
    def dup_socks_host(self) -> str: ...
    def get_autoconfig_url(self) -> str: ...
    def get_ftp_host(self) -> str: ...
    def get_ftp_port(self) -> int: ...
    def get_http_auth_password(self) -> str: ...
    def get_http_auth_user(self) -> str: ...
    def get_http_host(self) -> str: ...
    def get_http_port(self) -> int: ...
    def get_http_use_auth(self) -> bool: ...
    def get_https_host(self) -> str: ...
    def get_https_port(self) -> int: ...
    def get_ignore_hosts(self) -> list[str]: ...
    def get_method(self) -> ProxyMethod: ...
    def get_socks_host(self) -> str: ...
    def get_socks_port(self) -> int: ...
    def set_autoconfig_url(self, autoconfig_url: str) -> None: ...
    def set_ftp_host(self, ftp_host: str) -> None: ...
    def set_ftp_port(self, ftp_port: int) -> None: ...
    def set_http_auth_password(self, http_auth_password: str) -> None: ...
    def set_http_auth_user(self, http_auth_user: str) -> None: ...
    def set_http_host(self, http_host: str) -> None: ...
    def set_http_port(self, http_port: int) -> None: ...
    def set_http_use_auth(self, http_use_auth: bool) -> None: ...
    def set_https_host(self, https_host: str) -> None: ...
    def set_https_port(self, https_port: int) -> None: ...
    def set_ignore_hosts(self, ignore_hosts: str) -> None: ...
    def set_method(self, method: ProxyMethod) -> None: ...
    def set_socks_host(self, socks_host: str) -> None: ...
    def set_socks_port(self, socks_port: int) -> None: ...

class SourceProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceProxyClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceProxyPrivate(GObject.GPointer): ...

class SourceRefresh(SourceExtension):
    """
    :Constructors:

    ::

        SourceRefresh(**properties)

    Object ESourceRefresh

    Properties from ESourceRefresh:
      enabled -> gboolean: Enabled
        Whether to periodically refresh
      enabled-on-metered-network -> gboolean: Enabled on Metered Network
        Whether to enable refresh on metered network
      interval-minutes -> guint: Interval in Minutes
        Refresh interval in minutes

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        enabled: bool
        enabled_on_metered_network: bool
        interval_minutes: int
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceRefreshPrivate = ...
    def __init__(
        self,
        enabled: bool = ...,
        enabled_on_metered_network: bool = ...,
        interval_minutes: int = ...,
        source: Source = ...,
    ) -> None: ...
    def get_enabled(self) -> bool: ...
    def get_enabled_on_metered_network(self) -> bool: ...
    def get_interval_minutes(self) -> int: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_enabled_on_metered_network(self, enabled: bool) -> None: ...
    def set_interval_minutes(self, interval_minutes: int) -> None: ...

class SourceRefreshClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceRefreshClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceRefreshPrivate(GObject.GPointer): ...

class SourceRegistry(GObject.Object, Gio.AsyncInitable, Gio.Initable):
    """
    :Constructors:

    ::

        SourceRegistry(**properties)
        new_finish(result:Gio.AsyncResult) -> EDataServer.SourceRegistry
        new_sync(cancellable:Gio.Cancellable=None) -> EDataServer.SourceRegistry

    Object ESourceRegistry

    Signals from ESourceRegistry:
      credentials-required (ESource, ESourceCredentialsReason, gchararray, GTlsCertificateFlags, GError)
      source-added (ESource)
      source-changed (ESource)
      source-removed (ESource)
      source-enabled (ESource)
      source-disabled (ESource)

    Properties from ESourceRegistry:
      default-address-book -> ESource: Default Address Book
        The default address book ESource
      default-calendar -> ESource: Default Calendar
        The default calendar ESource
      default-mail-account -> ESource: Default Mail Account
        The default mail account ESource
      default-mail-identity -> ESource: Default Mail Identity
        The default mail identity ESource
      default-memo-list -> ESource: Default Memo List
        The default memo list ESource
      default-task-list -> ESource: Default Task List
        The default task list ESource

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        default_address_book: typing.Optional[Source]
        default_calendar: typing.Optional[Source]
        default_mail_account: typing.Optional[Source]
        default_mail_identity: typing.Optional[Source]
        default_memo_list: typing.Optional[Source]
        default_task_list: typing.Optional[Source]

    props: Props = ...
    parent: GObject.Object = ...
    priv: SourceRegistryPrivate = ...
    def __init__(
        self,
        default_address_book: typing.Optional[Source] = ...,
        default_calendar: typing.Optional[Source] = ...,
        default_mail_account: typing.Optional[Source] = ...,
        default_mail_identity: typing.Optional[Source] = ...,
        default_memo_list: typing.Optional[Source] = ...,
        default_task_list: typing.Optional[Source] = ...,
    ) -> None: ...
    def check_enabled(self, source: Source) -> bool: ...
    def commit_source(
        self,
        source: Source,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def commit_source_finish(self, result: Gio.AsyncResult) -> bool: ...
    def commit_source_sync(
        self, source: Source, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def create_sources(
        self,
        list_of_sources: list[Source],
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def create_sources_finish(self, result: Gio.AsyncResult) -> bool: ...
    def create_sources_sync(
        self,
        list_of_sources: list[Source],
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def debug_dump(self, extension_name: typing.Optional[str] = None) -> None: ...
    @staticmethod
    def debug_enabled() -> bool: ...
    def do_credentials_required(
        self,
        source: Source,
        reason: SourceCredentialsReason,
        certificate_pem: str,
        certificate_errors: Gio.TlsCertificateFlags,
        op_error: GLib.Error,
    ) -> None: ...
    def do_source_added(self, source: Source) -> None: ...
    def do_source_changed(self, source: Source) -> None: ...
    def do_source_disabled(self, source: Source) -> None: ...
    def do_source_enabled(self, source: Source) -> None: ...
    def do_source_removed(self, source: Source) -> None: ...
    def dup_unique_display_name(
        self, source: Source, extension_name: typing.Optional[str] = None
    ) -> str: ...
    def find_extension(
        self, source: Source, extension_name: str
    ) -> typing.Optional[Source]: ...
    @staticmethod
    def free_display_tree(display_tree: GLib.Node) -> None: ...
    def get_oauth2_services(self) -> OAuth2Services: ...
    def list_enabled(
        self, extension_name: typing.Optional[str] = None
    ) -> list[Source]: ...
    def list_sources(
        self, extension_name: typing.Optional[str] = None
    ) -> list[Source]: ...
    @staticmethod
    def new(
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    @classmethod
    def new_finish(cls, result: Gio.AsyncResult) -> SourceRegistry: ...
    @classmethod
    def new_sync(
        cls, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> SourceRegistry: ...
    def ref_builtin_address_book(self) -> Source: ...
    def ref_builtin_calendar(self) -> Source: ...
    def ref_builtin_mail_account(self) -> Source: ...
    def ref_builtin_memo_list(self) -> Source: ...
    def ref_builtin_proxy(self) -> Source: ...
    def ref_builtin_task_list(self) -> Source: ...
    def ref_default_address_book(self) -> Source: ...
    def ref_default_calendar(self) -> Source: ...
    def ref_default_for_extension_name(
        self, extension_name: str
    ) -> typing.Optional[Source]: ...
    def ref_default_mail_account(self) -> Source: ...
    def ref_default_mail_identity(self) -> typing.Optional[Source]: ...
    def ref_default_memo_list(self) -> Source: ...
    def ref_default_task_list(self) -> Source: ...
    def ref_source(self, uid: str) -> typing.Optional[Source]: ...
    def refresh_backend(
        self,
        source_uid: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        callback: typing.Optional[typing.Callable[..., None]] = None,
        *user_data: typing.Any,
    ) -> None: ...
    def refresh_backend_finish(self, result: Gio.AsyncResult) -> bool: ...
    def refresh_backend_sync(
        self, source_uid: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def set_default_address_book(
        self, default_source: typing.Optional[Source] = None
    ) -> None: ...
    def set_default_calendar(
        self, default_source: typing.Optional[Source] = None
    ) -> None: ...
    def set_default_for_extension_name(
        self, extension_name: str, default_source: typing.Optional[Source] = None
    ) -> None: ...
    def set_default_mail_account(
        self, default_source: typing.Optional[Source] = None
    ) -> None: ...
    def set_default_mail_identity(
        self, default_source: typing.Optional[Source] = None
    ) -> None: ...
    def set_default_memo_list(
        self, default_source: typing.Optional[Source] = None
    ) -> None: ...
    def set_default_task_list(
        self, default_source: typing.Optional[Source] = None
    ) -> None: ...

class SourceRegistryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceRegistryClass()
    """

    parent_class: GObject.ObjectClass = ...
    source_added: typing.Callable[[SourceRegistry, Source], None] = ...
    source_changed: typing.Callable[[SourceRegistry, Source], None] = ...
    source_removed: typing.Callable[[SourceRegistry, Source], None] = ...
    source_enabled: typing.Callable[[SourceRegistry, Source], None] = ...
    source_disabled: typing.Callable[[SourceRegistry, Source], None] = ...
    credentials_required: typing.Callable[
        [
            SourceRegistry,
            Source,
            SourceCredentialsReason,
            str,
            Gio.TlsCertificateFlags,
            GLib.Error,
        ],
        None,
    ] = ...

class SourceRegistryPrivate(GObject.GPointer): ...

class SourceRegistryWatcher(GObject.Object):
    """
    :Constructors:

    ::

        SourceRegistryWatcher(**properties)
        new(registry:EDataServer.SourceRegistry, extension_name:str=None) -> EDataServer.SourceRegistryWatcher

    Object ESourceRegistryWatcher

    Signals from ESourceRegistryWatcher:
      filter (ESource) -> gboolean
      appeared (ESource)
      disappeared (ESource)

    Properties from ESourceRegistryWatcher:
      extension-name -> gchararray: ExtensionName
      registry -> ESourceRegistry: Registry
        Data source registry

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        extension_name: typing.Optional[str]
        registry: SourceRegistry

    props: Props = ...
    parent: GObject.Object = ...
    priv: SourceRegistryWatcherPrivate = ...
    def __init__(
        self, extension_name: str = ..., registry: SourceRegistry = ...
    ) -> None: ...
    def do_appeared(self, source: Source) -> None: ...
    def do_disappeared(self, source: Source) -> None: ...
    def do_filter(self, source: Source) -> bool: ...
    def get_extension_name(self) -> typing.Optional[str]: ...
    def get_registry(self) -> SourceRegistry: ...
    @classmethod
    def new(
        cls, registry: SourceRegistry, extension_name: typing.Optional[str] = None
    ) -> SourceRegistryWatcher: ...
    def reclaim(self) -> None: ...

class SourceRegistryWatcherClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceRegistryWatcherClass()
    """

    parent_class: GObject.ObjectClass = ...
    filter: typing.Callable[[SourceRegistryWatcher, Source], bool] = ...
    appeared: typing.Callable[[SourceRegistryWatcher, Source], None] = ...
    disappeared: typing.Callable[[SourceRegistryWatcher, Source], None] = ...

class SourceRegistryWatcherPrivate(GObject.GPointer): ...

class SourceResource(SourceExtension):
    """
    :Constructors:

    ::

        SourceResource(**properties)

    Object ESourceResource

    Properties from ESourceResource:
      identity -> gchararray: Identity
        Resource identity

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        identity: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceResourcePrivate = ...
    def __init__(
        self, identity: typing.Optional[str] = ..., source: Source = ...
    ) -> None: ...
    def dup_identity(self) -> typing.Optional[str]: ...
    def get_identity(self) -> typing.Optional[str]: ...
    def set_identity(self, identity: typing.Optional[str] = None) -> None: ...

class SourceResourceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceResourceClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceResourcePrivate(GObject.GPointer): ...

class SourceRevisionGuards(SourceExtension):
    """
    :Constructors:

    ::

        SourceRevisionGuards(**properties)

    Object ESourceRevisionGuards

    Properties from ESourceRevisionGuards:
      enabled -> gboolean: Enabled
        Whether to enable or disable the revision guards

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        enabled: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceRevisionGuardsPrivate = ...
    def __init__(self, enabled: bool = ..., source: Source = ...) -> None: ...
    def get_enabled(self) -> bool: ...
    def set_enabled(self, enabled: bool) -> None: ...

class SourceRevisionGuardsClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceRevisionGuardsClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceRevisionGuardsPrivate(GObject.GPointer): ...

class SourceSMIME(SourceExtension):
    """
    :Constructors:

    ::

        SourceSMIME(**properties)

    Object ESourceSMIME

    Properties from ESourceSMIME:
      encryption-certificate -> gchararray: Encryption Certificate
        S/MIME certificate for encrypting messages
      encrypt-by-default -> gboolean: Encrypt By Default
        Encrypt outgoing messages by default
      encrypt-to-self -> gboolean: Encrypt To Self
        Always encrypt to myself
      signing-algorithm -> gchararray: Signing Algorithm
        Hash algorithm used to sign messages
      signing-certificate -> gchararray: Signing Certificate
        S/MIME certificate for signing messages
      sign-by-default -> gboolean: Sign By Default
        Sign outgoing messages by default

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        encrypt_by_default: bool
        encrypt_to_self: bool
        encryption_certificate: typing.Optional[str]
        sign_by_default: bool
        signing_algorithm: typing.Optional[str]
        signing_certificate: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceSMIMEPrivate = ...
    def __init__(
        self,
        encrypt_by_default: bool = ...,
        encrypt_to_self: bool = ...,
        encryption_certificate: typing.Optional[str] = ...,
        sign_by_default: bool = ...,
        signing_algorithm: typing.Optional[str] = ...,
        signing_certificate: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_encryption_certificate(self) -> typing.Optional[str]: ...
    def dup_signing_algorithm(self) -> typing.Optional[str]: ...
    def dup_signing_certificate(self) -> typing.Optional[str]: ...
    def get_encrypt_by_default(self) -> bool: ...
    def get_encrypt_to_self(self) -> bool: ...
    def get_encryption_certificate(self) -> typing.Optional[str]: ...
    def get_sign_by_default(self) -> bool: ...
    def get_signing_algorithm(self) -> typing.Optional[str]: ...
    def get_signing_certificate(self) -> typing.Optional[str]: ...
    def set_encrypt_by_default(self, encrypt_by_default: bool) -> None: ...
    def set_encrypt_to_self(self, encrypt_to_self: bool) -> None: ...
    def set_encryption_certificate(
        self, encryption_certificate: typing.Optional[str] = None
    ) -> None: ...
    def set_sign_by_default(self, sign_by_default: bool) -> None: ...
    def set_signing_algorithm(
        self, signing_algorithm: typing.Optional[str] = None
    ) -> None: ...
    def set_signing_certificate(
        self, signing_certificate: typing.Optional[str] = None
    ) -> None: ...

class SourceSMIMEClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceSMIMEClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceSMIMEPrivate(GObject.GPointer): ...

class SourceSecurity(SourceExtension):
    """
    :Constructors:

    ::

        SourceSecurity(**properties)

    Object ESourceSecurity

    Properties from ESourceSecurity:
      method -> gchararray: Method
        Security method
      secure -> gboolean: Secure
        Secure the network connection

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        method: str
        secure: bool
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceSecurityPrivate = ...
    def __init__(
        self,
        method: typing.Optional[str] = ...,
        secure: bool = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_method(self) -> str: ...
    def get_method(self) -> str: ...
    def get_secure(self) -> bool: ...
    def set_method(self, method: typing.Optional[str] = None) -> None: ...
    def set_secure(self, secure: bool) -> None: ...

class SourceSecurityClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceSecurityClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceSecurityPrivate(GObject.GPointer): ...

class SourceSelectable(SourceBackend):
    """
    :Constructors:

    ::

        SourceSelectable(**properties)

    Object ESourceSelectable

    Properties from ESourceSelectable:
      color -> gchararray: Color
        Textual specification of a color
      selected -> gboolean: Selected
        Whether the data source is selected
      order -> guint: Order
        Preferred sorting order

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceBackend.Props):
        color: typing.Optional[str]
        order: int
        selected: bool
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceBackend = ...
    priv: SourceSelectablePrivate = ...
    def __init__(
        self,
        color: typing.Optional[str] = ...,
        order: int = ...,
        selected: bool = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_color(self) -> typing.Optional[str]: ...
    def get_color(self) -> typing.Optional[str]: ...
    def get_order(self) -> int: ...
    def get_selected(self) -> bool: ...
    def set_color(self, color: typing.Optional[str] = None) -> None: ...
    def set_order(self, order: int) -> None: ...
    def set_selected(self, selected: bool) -> None: ...

class SourceSelectableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceSelectableClass()
    """

    parent_class: SourceBackendClass = ...

class SourceSelectablePrivate(GObject.GPointer): ...

class SourceTaskList(SourceSelectable):
    """
    :Constructors:

    ::

        SourceTaskList(**properties)

    Object ESourceTaskList

    Properties from ESourceSelectable:
      color -> gchararray: Color
        Textual specification of a color
      selected -> gboolean: Selected
        Whether the data source is selected
      order -> guint: Order
        Preferred sorting order

    Properties from ESourceBackend:
      backend-name -> gchararray: Backend Name
        The name of the backend handling the data source

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceSelectable.Props):
        color: typing.Optional[str]
        order: int
        selected: bool
        backend_name: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceSelectable = ...
    priv: SourceTaskListPrivate = ...
    def __init__(
        self,
        color: typing.Optional[str] = ...,
        order: int = ...,
        selected: bool = ...,
        backend_name: typing.Optional[str] = ...,
        source: Source = ...,
    ) -> None: ...

class SourceTaskListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceTaskListClass()
    """

    parent_class: SourceSelectableClass = ...

class SourceTaskListPrivate(GObject.GPointer): ...

class SourceUoa(SourceExtension):
    """
    :Constructors:

    ::

        SourceUoa(**properties)

    Object ESourceUoa

    Properties from ESourceUoa:
      account-id -> guint: Account ID
        Ubuntu Online Account ID

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        account_id: int
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceUoaPrivate = ...
    def __init__(self, account_id: int = ..., source: Source = ...) -> None: ...
    def get_account_id(self) -> int: ...
    def set_account_id(self, account_id: int) -> None: ...

class SourceUoaClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceUoaClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceUoaPrivate(GObject.GPointer): ...

class SourceWeather(SourceExtension):
    """
    :Constructors:

    ::

        SourceWeather(**properties)

    Object ESourceWeather

    Properties from ESourceWeather:
      location -> gchararray: Location
        Weather location code
      units -> ESourceWeatherUnits: Units
        Fahrenheit, Centigrade or Kelvin units

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        location: str
        units: SourceWeatherUnits
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceWeatherPrivate = ...
    def __init__(
        self, location: str = ..., units: SourceWeatherUnits = ..., source: Source = ...
    ) -> None: ...
    def dup_location(self) -> str: ...
    def get_location(self) -> str: ...
    def get_units(self) -> SourceWeatherUnits: ...
    def set_location(self, location: str) -> None: ...
    def set_units(self, units: SourceWeatherUnits) -> None: ...

class SourceWeatherClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceWeatherClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceWeatherPrivate(GObject.GPointer): ...

class SourceWebDAVNotes(SourceExtension):
    """
    :Constructors:

    ::

        SourceWebDAVNotes(**properties)

    Object ESourceWebDAVNotes

    Properties from ESourceWebDAVNotes:
      default-ext -> gchararray: Default Ext
        Default file extension for new notes

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        default_ext: typing.Optional[str]
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceWebDAVNotesPrivate = ...
    def __init__(
        self, default_ext: typing.Optional[str] = ..., source: Source = ...
    ) -> None: ...
    def dup_default_ext(self) -> typing.Optional[str]: ...
    def get_default_ext(self) -> typing.Optional[str]: ...
    def set_default_ext(self, default_ext: typing.Optional[str] = None) -> None: ...

class SourceWebDAVNotesClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceWebDAVNotesClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceWebDAVNotesPrivate(GObject.GPointer): ...

class SourceWebdav(SourceExtension):
    """
    :Constructors:

    ::

        SourceWebdav(**properties)

    Object ESourceWebdav

    Properties from ESourceWebdav:
      avoid-ifmatch -> gboolean: Avoid If-Match
        Work around a bug in old Apache servers
      calendar-auto-schedule -> gboolean: Calendar Auto-Schedule
        Whether the server handles meeting invitations (CalDAV-only)
      color -> gchararray: Color
        Color of the WebDAV resource
      display-name -> gchararray: Display Name
        Display name of the WebDAV resource
      email-address -> gchararray: Email Address
        The user's email address
      resource-path -> gchararray: Resource Path
        Absolute path to a WebDAV resource
      resource-query -> gchararray: Resource Query
        Query to access a WebDAV resource
      uri -> GUri: Uri
        WebDAV service as a GUri
      ssl-trust -> gchararray: SSL/TLS Trust
        SSL/TLS certificate trust setting, for invalid server certificates
      order -> guint: Order
        A sorting order of the resource

    Properties from ESourceExtension:
      source -> ESource: Source
        The ESource being extended

    Signals from GObject:
      notify (GParam)
    """
    class Props(SourceExtension.Props):
        avoid_ifmatch: bool
        calendar_auto_schedule: bool
        color: typing.Optional[str]
        display_name: typing.Optional[str]
        email_address: typing.Optional[str]
        order: int
        resource_path: typing.Optional[str]
        resource_query: typing.Optional[str]
        ssl_trust: typing.Optional[str]
        uri: GLib.Uri
        source: Source

    props: Props = ...
    parent: SourceExtension = ...
    priv: SourceWebdavPrivate = ...
    def __init__(
        self,
        avoid_ifmatch: bool = ...,
        calendar_auto_schedule: bool = ...,
        color: typing.Optional[str] = ...,
        display_name: typing.Optional[str] = ...,
        email_address: typing.Optional[str] = ...,
        order: int = ...,
        resource_path: typing.Optional[str] = ...,
        resource_query: typing.Optional[str] = ...,
        ssl_trust: typing.Optional[str] = ...,
        uri: GLib.Uri = ...,
        source: Source = ...,
    ) -> None: ...
    def dup_color(self) -> typing.Optional[str]: ...
    def dup_display_name(self) -> typing.Optional[str]: ...
    def dup_email_address(self) -> typing.Optional[str]: ...
    def dup_resource_path(self) -> typing.Optional[str]: ...
    def dup_resource_query(self) -> typing.Optional[str]: ...
    def dup_ssl_trust(self) -> typing.Optional[str]: ...
    def dup_uri(self) -> GLib.Uri: ...
    def get_avoid_ifmatch(self) -> bool: ...
    def get_calendar_auto_schedule(self) -> bool: ...
    def get_color(self) -> typing.Optional[str]: ...
    def get_display_name(self) -> typing.Optional[str]: ...
    def get_email_address(self) -> typing.Optional[str]: ...
    def get_order(self) -> int: ...
    def get_resource_path(self) -> typing.Optional[str]: ...
    def get_resource_query(self) -> typing.Optional[str]: ...
    def get_ssl_trust(self) -> typing.Optional[str]: ...
    def get_ssl_trust_response(self) -> TrustPromptResponse: ...
    def set_avoid_ifmatch(self, avoid_ifmatch: bool) -> None: ...
    def set_calendar_auto_schedule(self, calendar_auto_schedule: bool) -> None: ...
    def set_color(self, color: typing.Optional[str] = None) -> None: ...
    def set_display_name(self, display_name: typing.Optional[str] = None) -> None: ...
    def set_email_address(self, email_address: typing.Optional[str] = None) -> None: ...
    def set_order(self, order: int) -> None: ...
    def set_resource_path(self, resource_path: typing.Optional[str] = None) -> None: ...
    def set_resource_query(
        self, resource_query: typing.Optional[str] = None
    ) -> None: ...
    def set_ssl_trust(self, ssl_trust: typing.Optional[str] = None) -> None: ...
    def set_ssl_trust_response(self, response: TrustPromptResponse) -> None: ...
    def set_uri(self, uri: GLib.Uri) -> None: ...
    def unset_temporary_ssl_trust(self) -> None: ...
    def update_ssl_trust(
        self, host: str, cert: Gio.TlsCertificate, response: TrustPromptResponse
    ) -> None: ...
    def verify_ssl_trust(
        self, host: str, cert: Gio.TlsCertificate, cert_errors: Gio.TlsCertificateFlags
    ) -> TrustPromptResponse: ...

class SourceWebdavClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SourceWebdavClass()
    """

    parent_class: SourceExtensionClass = ...

class SourceWebdavPrivate(GObject.GPointer): ...

class WebDAVAccessControlEntry(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebDAVAccessControlEntry()
        new(principal_kind:EDataServer.WebDAVACEPrincipalKind, principal_href:str=None, flags:int, inherited_href:str=None) -> EDataServer.WebDAVAccessControlEntry
    """

    principal_kind: WebDAVACEPrincipalKind = ...
    principal_href: str = ...
    flags: int = ...
    inherited_href: str = ...
    privileges: list[None] = ...
    def append_privilege(self, privilege: WebDAVPrivilege) -> None: ...
    def copy(self) -> typing.Optional[WebDAVAccessControlEntry]: ...
    @staticmethod
    def free(ptr: None) -> None: ...
    def get_privileges(self) -> list[WebDAVPrivilege]: ...
    @classmethod
    def new(
        cls,
        principal_kind: WebDAVACEPrincipalKind,
        principal_href: typing.Optional[str],
        flags: int,
        inherited_href: typing.Optional[str] = None,
    ) -> WebDAVAccessControlEntry: ...

class WebDAVDiscoveredSource(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebDAVDiscoveredSource()
    """

    href: str = ...
    supports: int = ...
    display_name: str = ...
    description: str = ...
    color: str = ...
    order: int = ...
    def copy(self) -> WebDAVDiscoveredSource: ...
    def free(self) -> None: ...

class WebDAVPrivilege(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebDAVPrivilege()
        new(ns_uri:str=None, name:str=None, description:str=None, kind:EDataServer.WebDAVPrivilegeKind, hint:EDataServer.WebDAVPrivilegeHint) -> EDataServer.WebDAVPrivilege
    """

    ns_uri: str = ...
    name: str = ...
    description: str = ...
    kind: WebDAVPrivilegeKind = ...
    hint: WebDAVPrivilegeHint = ...
    def copy(self) -> typing.Optional[WebDAVPrivilege]: ...
    @staticmethod
    def free(ptr: None) -> None: ...
    @classmethod
    def new(
        cls,
        ns_uri: typing.Optional[str],
        name: typing.Optional[str],
        description: typing.Optional[str],
        kind: WebDAVPrivilegeKind,
        hint: WebDAVPrivilegeHint,
    ) -> WebDAVPrivilege: ...

class WebDAVPropertyChange(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebDAVPropertyChange()
        new_remove(ns_uri:str, name:str) -> EDataServer.WebDAVPropertyChange
        new_set(ns_uri:str, name:str, value:str=None) -> EDataServer.WebDAVPropertyChange
    """

    kind: WebDAVPropertyChangeKind = ...
    ns_uri: str = ...
    name: str = ...
    value: str = ...
    def copy(self) -> typing.Optional[WebDAVPropertyChange]: ...
    @staticmethod
    def free(ptr: None) -> None: ...
    @classmethod
    def new_remove(cls, ns_uri: str, name: str) -> WebDAVPropertyChange: ...
    @classmethod
    def new_set(
        cls, ns_uri: str, name: str, value: typing.Optional[str] = None
    ) -> WebDAVPropertyChange: ...

class WebDAVResource(GObject.GBoxed):
    """
    :Constructors:

    ::

        WebDAVResource()
        new(kind:EDataServer.WebDAVResourceKind, supports:int, href:str, etag:str=None, display_name:str=None, content_type:str=None, content_length:int, creation_date:int, last_modified:int, description:str=None, color:str=None, order:int) -> EDataServer.WebDAVResource
    """

    kind: WebDAVResourceKind = ...
    supports: int = ...
    href: str = ...
    etag: str = ...
    display_name: str = ...
    content_type: str = ...
    content_length: int = ...
    creation_date: int = ...
    last_modified: int = ...
    description: str = ...
    color: str = ...
    order: int = ...
    def copy(self) -> typing.Optional[WebDAVResource]: ...
    @staticmethod
    def free(ptr: None) -> None: ...
    @classmethod
    def new(
        cls,
        kind: WebDAVResourceKind,
        supports: int,
        href: str,
        etag: typing.Optional[str],
        display_name: typing.Optional[str],
        content_type: typing.Optional[str],
        content_length: int,
        creation_date: int,
        last_modified: int,
        description: typing.Optional[str],
        color: typing.Optional[str],
        order: int,
    ) -> WebDAVResource: ...

class WebDAVSession(SoupSession):
    """
    :Constructors:

    ::

        WebDAVSession(**properties)
        new(source:EDataServer.Source) -> EDataServer.WebDAVSession

    Object EWebDAVSession

    Properties from ESoupSession:
      source -> ESource: Source
      credentials -> ENamedParameters: Credentials
      force-http1 -> gboolean: Force HTTP/1

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
    class Props(SoupSession.Props):
        credentials: typing.Optional[NamedParameters]
        force_http1: bool
        source: typing.Optional[Source]
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
    parent: SoupSession = ...
    priv: WebDAVSessionPrivate = ...
    def __init__(
        self,
        credentials: typing.Optional[NamedParameters] = ...,
        force_http1: bool = ...,
        source: Source = ...,
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
    def acl_sync(
        self,
        uri: typing.Optional[str],
        xml: XmlDocument,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def copy_sync(
        self,
        source_uri: str,
        destination_uri: str,
        depth: str,
        can_overwrite: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def delete_sync(
        self,
        uri: str,
        depth: typing.Optional[str] = None,
        etag: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def delete_with_headers_sync(
        self,
        uri: str,
        depth: typing.Optional[str] = None,
        etag: typing.Optional[str] = None,
        in_headers: typing.Optional[Soup.MessageHeaders] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def ensure_full_uri(
        self, request_uri: typing.Optional[GLib.Uri], href: str
    ) -> str: ...
    def get_acl_restrictions_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, int, WebDAVACEPrincipalKind, list[str]]: ...
    def get_acl_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, list[WebDAVAccessControlEntry]]: ...
    def get_current_user_privilege_set_full_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[
        bool, list[WebDAVPrivilege], dict[None, None], dict[None, None]
    ]: ...
    def get_current_user_privilege_set_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, list[WebDAVPrivilege]]: ...
    def get_data_sync(
        self, uri: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str, str, Soup.MessageHeaders, str, int]: ...
    def get_last_dav_error_code(self) -> typing.Optional[str]: ...
    def get_last_dav_error_is_permission(self) -> bool: ...
    def get_principal_collection_set_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, list[str]]: ...
    def get_supported_privilege_set_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, GLib.Node]: ...
    def get_sync(
        self, uri: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> typing.Tuple[bool, str, str, Soup.MessageHeaders, Gio.OutputStream]: ...
    def getctag_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, str]: ...
    def list_sync(
        self,
        uri: typing.Optional[str],
        depth: str,
        flags: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, list[WebDAVResource]]: ...
    def lock_resource_sync(
        self,
        uri: typing.Optional[str],
        lock_scope: WebDAVLockScope,
        lock_timeout: int,
        owner: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, str]: ...
    def lock_sync(
        self,
        uri: typing.Optional[str],
        depth: str,
        lock_timeout: int,
        xml: XmlDocument,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, str, libxml2.Doc]: ...
    def mkcalendar_sync(
        self,
        uri: str,
        display_name: typing.Optional[str],
        description: typing.Optional[str],
        color: typing.Optional[str],
        supports: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def mkcol_addressbook_sync(
        self,
        uri: str,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def mkcol_sync(
        self, uri: str, cancellable: typing.Optional[Gio.Cancellable] = None
    ) -> bool: ...
    def move_sync(
        self,
        source_uri: str,
        destination_uri: str,
        can_overwrite: bool,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    @classmethod
    def new(cls, source: Source) -> WebDAVSession: ...
    def new_message(
        self, method: str, uri: typing.Optional[str] = None
    ) -> Soup.Message: ...
    def options_sync(
        self,
        uri: typing.Optional[str] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, dict[None, None], dict[None, None]]: ...
    def post_sync(
        self,
        uri: typing.Optional[str],
        data: str,
        data_length: int,
        in_content_type: typing.Optional[str] = None,
        in_headers: typing.Optional[Soup.MessageHeaders] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, str, Soup.MessageHeaders, bytes]: ...
    def principal_property_search_sync(
        self,
        uri: typing.Optional[str],
        apply_to_principal_collection_set: bool,
        match_ns_uri: typing.Optional[str],
        match_property: str,
        match_value: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, list[WebDAVResource]]: ...
    def propfind_sync(
        self,
        uri: typing.Optional[str],
        depth: str,
        xml: typing.Optional[XmlDocument] = None,
        func: typing.Optional[typing.Callable[..., bool]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *func_user_data: typing.Any,
    ) -> bool: ...
    def proppatch_sync(
        self,
        uri: typing.Optional[str],
        xml: XmlDocument,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def put_data_sync(
        self,
        uri: str,
        etag: typing.Optional[str],
        content_type: str,
        in_headers: typing.Optional[Soup.MessageHeaders],
        bytes: str,
        length: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, str, str, Soup.MessageHeaders]: ...
    def put_sync(
        self,
        uri: str,
        etag: typing.Optional[str],
        content_type: str,
        in_headers: typing.Optional[Soup.MessageHeaders],
        stream: Gio.InputStream,
        stream_length: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> typing.Tuple[bool, str, str, Soup.MessageHeaders]: ...
    def refresh_lock_sync(
        self,
        uri: typing.Optional[str],
        lock_token: str,
        lock_timeout: int,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def replace_with_detailed_error(
        self,
        message: Soup.Message,
        response_data: typing.Optional[typing.Sequence[int]],
        ignore_multistatus: bool,
        prefix: typing.Optional[str] = None,
    ) -> bool: ...
    def report_sync(
        self,
        uri: typing.Optional[str],
        depth: typing.Optional[str],
        xml: XmlDocument,
        func: typing.Optional[typing.Callable[..., bool]] = None,
        out_content_type: typing.Optional[str] = None,
        out_content: typing.Optional[typing.Sequence[int]] = None,
        cancellable: typing.Optional[Gio.Cancellable] = None,
        *func_user_data: typing.Any,
    ) -> bool: ...
    def set_acl_sync(
        self,
        uri: typing.Optional[str],
        entries: list[WebDAVAccessControlEntry],
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def traverse_mkcalendar_response(
        self,
        message: typing.Optional[Soup.Message],
        xml_data: typing.Sequence[int],
        func: typing.Optional[typing.Callable[..., bool]] = None,
        *func_user_data: typing.Any,
    ) -> bool: ...
    def traverse_mkcol_response(
        self,
        message: typing.Optional[Soup.Message],
        xml_data: typing.Sequence[int],
        func: typing.Optional[typing.Callable[..., bool]] = None,
        *func_user_data: typing.Any,
    ) -> bool: ...
    def traverse_multistatus_response(
        self,
        message: typing.Optional[Soup.Message],
        xml_data: typing.Sequence[int],
        func: typing.Optional[typing.Callable[..., bool]] = None,
        *func_user_data: typing.Any,
    ) -> bool: ...
    def unlock_sync(
        self,
        uri: typing.Optional[str],
        lock_token: str,
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    def update_properties_sync(
        self,
        uri: typing.Optional[str],
        changes: list[WebDAVPropertyChange],
        cancellable: typing.Optional[Gio.Cancellable] = None,
    ) -> bool: ...
    @staticmethod
    def util_free_privileges(privileges: typing.Optional[GLib.Node] = None) -> None: ...
    @staticmethod
    def util_item_href_equal(href1: str, href2: str) -> bool: ...
    @staticmethod
    def util_maybe_dequote() -> typing.Tuple[str, str]: ...

class WebDAVSessionClass(GObject.GPointer):
    """
    :Constructors:

    ::

        WebDAVSessionClass()
    """

    parent_class: SoupSessionClass = ...
    reserved: list[None] = ...

class WebDAVSessionPrivate(GObject.GPointer): ...

class XmlDocument(GObject.Object):
    """
    :Constructors:

    ::

        XmlDocument(**properties)
        new(ns_href:str=None, root_element:str) -> EDataServer.XmlDocument

    Object EXmlDocument

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.Object = ...
    priv: XmlDocumentPrivate = ...
    def add_attribute(
        self, ns_href: typing.Optional[str], name: str, value: str
    ) -> None: ...
    def add_attribute_double(
        self, ns_href: typing.Optional[str], name: str, value: float
    ) -> None: ...
    def add_attribute_int(
        self, ns_href: typing.Optional[str], name: str, value: int
    ) -> None: ...
    def add_attribute_time(
        self, ns_href: typing.Optional[str], name: str, value: int
    ) -> None: ...
    def add_attribute_time_ical(
        self, ns_href: typing.Optional[str], name: str, value: int
    ) -> None: ...
    def add_empty_element(self, ns_href: typing.Optional[str], name: str) -> None: ...
    def end_element(self) -> None: ...
    def get_content(self) -> typing.Tuple[str, int]: ...
    def get_xmldoc(self) -> libxml2.Doc: ...
    @classmethod
    def new(cls, ns_href: typing.Optional[str], root_element: str) -> XmlDocument: ...
    def start_element(self, ns_href: typing.Optional[str], name: str) -> None: ...
    def start_text_element(self, ns_href: typing.Optional[str], name: str) -> None: ...
    def write_base64(self, value: str, len: int) -> None: ...
    def write_buffer(self, value: str, len: int) -> None: ...
    def write_double(self, value: float) -> None: ...
    def write_int(self, value: int) -> None: ...
    def write_string(self, value: str) -> None: ...
    def write_time(self, value: int) -> None: ...

class XmlDocumentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        XmlDocumentClass()
    """

    parent_class: GObject.ObjectClass = ...
    reserved: list[None] = ...

class XmlDocumentPrivate(GObject.GPointer): ...
class XmlHash(GObject.GPointer): ...

class OAuth2ServiceFlags(GObject.GFlags):
    EXTRACT_REQUIRES_PAGE_CONTENT = 2
    NONE = 0

class WebDAVACEFlag(GObject.GFlags):
    DENY = 2
    GRANT = 1
    INHERITED = 16
    INVERT = 4
    PROTECTED = 8
    UNKNOWN = 0

class WebDAVACLRestrictions(GObject.GFlags):
    DENY_BEFORE_GRANT = 4
    GRANT_ONLY = 1
    NONE = 0
    NO_INVERT = 2
    REQUIRED_PRINCIPAL = 8

class WebDAVDiscoverSupports(GObject.GFlags):
    CALENDAR_AUTO_SCHEDULE = 128
    CONTACTS = 1
    EVENTS = 2
    MEMOS = 4
    NONE = 0
    SUBSCRIBED_ICALENDAR = 256
    TASKS = 8
    WEBDAV_NOTES = 64

class WebDAVListFlags(GObject.GFlags):
    ALL = 16777215
    COLOR = 256
    CONTENT_LENGTH = 16
    CONTENT_TYPE = 8
    CREATION_DATE = 32
    DESCRIPTION = 128
    DISPLAY_NAME = 4
    ETAG = 2
    LAST_MODIFIED = 64
    NONE = 0
    ONLY_ADDRESSBOOK = 536870912
    ONLY_CALENDAR = 268435456
    ORDER = 512
    SUPPORTS = 1

class WebDAVResourceSupports(GObject.GFlags):
    CONTACTS = 1
    EVENTS = 2
    FREEBUSY = 16
    LAST = 64
    MEMOS = 4
    NONE = 0
    TASKS = 8
    TIMEZONE = 32
    WEBDAV_NOTES = 64

class ClientError(GObject.GEnum):
    AUTHENTICATION_FAILED = 4
    AUTHENTICATION_REQUIRED = 5
    BUSY = 1
    CANCELLED = 9
    COULD_NOT_CANCEL = 10
    DBUS_ERROR = 18
    INVALID_ARG = 0
    INVALID_QUERY = 16
    NOT_OPENED = 20
    NOT_SUPPORTED = 11
    OFFLINE_UNAVAILABLE = 7
    OTHER_ERROR = 19
    OUT_OF_SYNC = 21
    PERMISSION_DENIED = 8
    QUERY_REFUSED = 17
    REPOSITORY_OFFLINE = 6
    SEARCH_SIZE_LIMIT_EXCEEDED = 14
    SEARCH_TIME_LIMIT_EXCEEDED = 15
    SOURCE_ALREADY_LOADED = 3
    SOURCE_NOT_LOADED = 2
    TLS_NOT_AVAILABLE = 12
    UNSUPPORTED_AUTHENTICATION_METHOD = 13

class CollatorError(GObject.GEnum):
    CONVERSION = 1
    INVALID_LOCALE = 2
    OPEN = 0

class ConflictResolution(GObject.GEnum):
    FAIL = 0
    KEEP_LOCAL = 3
    KEEP_SERVER = 2
    USE_NEWER = 1
    WRITE_COPY = 4

class GDataTaskStatus(GObject.GEnum):
    COMPLETED = 2
    NEEDS_ACTION = 1
    UNKNOWN = 0

class MdnResponsePolicy(GObject.GEnum):
    ALWAYS = 1
    ASK = 2
    NEVER = 0

class OAuth2ServiceNavigationPolicy(GObject.GEnum):
    ABORT = 2
    ALLOW = 1
    DENY = 0

class ProxyMethod(GObject.GEnum):
    AUTO = 2
    DEFAULT = 0
    MANUAL = 1
    NONE = 3

class SourceAuthenticationResult(GObject.GEnum):
    ACCEPTED = 2
    ERROR = 0
    ERROR_SSL_FAILED = 1
    REJECTED = 3
    REQUIRED = 4
    UNKNOWN = -1

class SourceConnectionStatus(GObject.GEnum):
    AWAITING_CREDENTIALS = 1
    CONNECTED = 4
    CONNECTING = 3
    DISCONNECTED = 0
    SSL_FAILED = 2

class SourceCredentialsReason(GObject.GEnum):
    ERROR = 4
    REJECTED = 2
    REQUIRED = 1
    SSL_FAILED = 3
    UNKNOWN = 0

class SourceLDAPAuthentication(GObject.GEnum):
    BINDDN = 2
    EMAIL = 1
    NONE = 0

class SourceLDAPScope(GObject.GEnum):
    ONELEVEL = 0
    SUBTREE = 1

class SourceLDAPSecurity(GObject.GEnum):
    LDAPS = 1
    NONE = 0
    STARTTLS = 2

class SourceMailCompositionReplyStyle(GObject.GEnum):
    ATTACH = 3
    DEFAULT = 0
    DO_NOT_QUOTE = 2
    OUTLOOK = 4
    QUOTED = 1

class SourceWeatherUnits(GObject.GEnum):
    CENTIGRADE = 1
    FAHRENHEIT = 0
    KELVIN = 2

class ThreeState(GObject.GEnum):
    INCONSISTENT = 2
    OFF = 0
    ON = 1

class TimeParseStatus(GObject.GEnum):
    INVALID = 2
    NONE = 1
    OK = 0

class TrustPromptResponse(GObject.GEnum):
    ACCEPT = 1
    ACCEPT_TEMPORARILY = 2
    REJECT = 0
    REJECT_TEMPORARILY = 3
    UNKNOWN = -1

class WebDAVACEPrincipalKind(GObject.GEnum):
    ALL = 2
    AUTHENTICATED = 3
    HREF = 1
    OWNER = 7
    PROPERTY = 5
    SELF = 6
    UNAUTHENTICATED = 4
    UNKNOWN = 0

class WebDAVLockScope(GObject.GEnum):
    EXCLUSIVE = 0
    SHARED = 1

class WebDAVPrivilegeHint(GObject.GEnum):
    ALL = 11
    BIND = 9
    CALDAV_READ_FREE_BUSY = 12
    READ = 1
    READ_ACL = 6
    READ_CURRENT_USER_PRIVILEGE_SET = 8
    UNBIND = 10
    UNKNOWN = 0
    UNLOCK = 5
    WRITE = 2
    WRITE_ACL = 7
    WRITE_CONTENT = 4
    WRITE_PROPERTIES = 3

class WebDAVPrivilegeKind(GObject.GEnum):
    ABSTRACT = 1
    AGGREGATE = 2
    COMMON = 3
    UNKNOWN = 0

class WebDAVPropertyChangeKind(GObject.GEnum):
    REMOVE = 1
    SET = 0

class WebDAVResourceKind(GObject.GEnum):
    ADDRESSBOOK = 1
    CALENDAR = 2
    COLLECTION = 4
    PRINCIPAL = 3
    RESOURCE = 5
    SCHEDULE_INBOX = 8
    SCHEDULE_OUTBOX = 9
    SUBSCRIBED_ICALENDAR = 6
    UNKNOWN = 0
    WEBDAV_NOTES = 7

class XmlHashStatus(GObject.GEnum):
    DIFFERENT = 1
    NOT_FOUND = 2
    SAME = 0

class XmlHashType(GObject.GEnum):
    OBJECT_UID = 0
    PROPERTY = 1
