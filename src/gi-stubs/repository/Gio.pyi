from typing import Any
from typing import Final
from typing import Generic
from typing import Literal
from typing import overload
from typing import Protocol
from typing import type_check_only
from typing import TypeAlias
from typing_extensions import Never
from typing_extensions import Self
from typing_extensions import TypeVar
from typing_extensions import TypeVarTuple
from typing_extensions import Unpack

import asyncio
from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Sequence

from gi import _gi
from gi.repository import GioUnix
from gi.repository import GLib
from gi.repository import GObject

_T = TypeVar("_T")
ObjectItemType = TypeVar("ObjectItemType", bound=GObject.Object, default=Any)
ObjectPropsItemType = TypeVar("ObjectPropsItemType", bound=GObject.Object, default=Any)
_DataTs = TypeVarTuple("_DataTs", default=Unpack[tuple[()]])
_SourceObjectT = TypeVar("_SourceObjectT", bound=GObject.ObjectProtocol | None)
_T_co = TypeVar("_T_co", covariant=True, default=Any)

_AsyncReadyCallback: TypeAlias = Callable[[_SourceObjectT, AsyncResult, _T_co], None]
_AsyncReadyVarArgsCallback: TypeAlias = Callable[
    [_SourceObjectT, AsyncResult, Unpack[_DataTs]], None
]

DBUS_METHOD_INVOCATION_HANDLED: Final = True
DBUS_METHOD_INVOCATION_UNHANDLED: Final = False
DEBUG_CONTROLLER_EXTENSION_POINT_NAME: Final = "gio-debug-controller"
DESKTOP_APP_INFO_LOOKUP_EXTENSION_POINT_NAME: Final = "gio-desktop-app-info-lookup"
DRIVE_IDENTIFIER_KIND_UNIX_DEVICE: Final = "unix-device"
FILE_ATTRIBUTE_ACCESS_CAN_DELETE: Final = "access::can-delete"
FILE_ATTRIBUTE_ACCESS_CAN_EXECUTE: Final = "access::can-execute"
FILE_ATTRIBUTE_ACCESS_CAN_READ: Final = "access::can-read"
FILE_ATTRIBUTE_ACCESS_CAN_RENAME: Final = "access::can-rename"
FILE_ATTRIBUTE_ACCESS_CAN_TRASH: Final = "access::can-trash"
FILE_ATTRIBUTE_ACCESS_CAN_WRITE: Final = "access::can-write"
FILE_ATTRIBUTE_DOS_IS_ARCHIVE: Final = "dos::is-archive"
FILE_ATTRIBUTE_DOS_IS_MOUNTPOINT: Final = "dos::is-mountpoint"
FILE_ATTRIBUTE_DOS_IS_SYSTEM: Final = "dos::is-system"
FILE_ATTRIBUTE_DOS_REPARSE_POINT_TAG: Final = "dos::reparse-point-tag"
FILE_ATTRIBUTE_ETAG_VALUE: Final = "etag::value"
FILE_ATTRIBUTE_FILESYSTEM_FREE: Final = "filesystem::free"
FILE_ATTRIBUTE_FILESYSTEM_READONLY: Final = "filesystem::readonly"
FILE_ATTRIBUTE_FILESYSTEM_REMOTE: Final = "filesystem::remote"
FILE_ATTRIBUTE_FILESYSTEM_SIZE: Final = "filesystem::size"
FILE_ATTRIBUTE_FILESYSTEM_TYPE: Final = "filesystem::type"
FILE_ATTRIBUTE_FILESYSTEM_USED: Final = "filesystem::used"
FILE_ATTRIBUTE_FILESYSTEM_USE_PREVIEW: Final = "filesystem::use-preview"
FILE_ATTRIBUTE_GVFS_BACKEND: Final = "gvfs::backend"
FILE_ATTRIBUTE_ID_FILE: Final = "id::file"
FILE_ATTRIBUTE_ID_FILESYSTEM: Final = "id::filesystem"
FILE_ATTRIBUTE_MOUNTABLE_CAN_EJECT: Final = "mountable::can-eject"
FILE_ATTRIBUTE_MOUNTABLE_CAN_MOUNT: Final = "mountable::can-mount"
FILE_ATTRIBUTE_MOUNTABLE_CAN_POLL: Final = "mountable::can-poll"
FILE_ATTRIBUTE_MOUNTABLE_CAN_START: Final = "mountable::can-start"
FILE_ATTRIBUTE_MOUNTABLE_CAN_START_DEGRADED: Final = "mountable::can-start-degraded"
FILE_ATTRIBUTE_MOUNTABLE_CAN_STOP: Final = "mountable::can-stop"
FILE_ATTRIBUTE_MOUNTABLE_CAN_UNMOUNT: Final = "mountable::can-unmount"
FILE_ATTRIBUTE_MOUNTABLE_HAL_UDI: Final = "mountable::hal-udi"
FILE_ATTRIBUTE_MOUNTABLE_IS_MEDIA_CHECK_AUTOMATIC: Final = (
    "mountable::is-media-check-automatic"
)
FILE_ATTRIBUTE_MOUNTABLE_START_STOP_TYPE: Final = "mountable::start-stop-type"
FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE: Final = "mountable::unix-device"
FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE_FILE: Final = "mountable::unix-device-file"
FILE_ATTRIBUTE_OWNER_GROUP: Final = "owner::group"
FILE_ATTRIBUTE_OWNER_USER: Final = "owner::user"
FILE_ATTRIBUTE_OWNER_USER_REAL: Final = "owner::user-real"
FILE_ATTRIBUTE_PREVIEW_ICON: Final = "preview::icon"
FILE_ATTRIBUTE_RECENT_MODIFIED: Final = "recent::modified"
FILE_ATTRIBUTE_SELINUX_CONTEXT: Final = "selinux::context"
FILE_ATTRIBUTE_STANDARD_ALLOCATED_SIZE: Final = "standard::allocated-size"
FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE: Final = "standard::content-type"
FILE_ATTRIBUTE_STANDARD_COPY_NAME: Final = "standard::copy-name"
FILE_ATTRIBUTE_STANDARD_DESCRIPTION: Final = "standard::description"
FILE_ATTRIBUTE_STANDARD_DISPLAY_NAME: Final = "standard::display-name"
FILE_ATTRIBUTE_STANDARD_EDIT_NAME: Final = "standard::edit-name"
FILE_ATTRIBUTE_STANDARD_FAST_CONTENT_TYPE: Final = "standard::fast-content-type"
FILE_ATTRIBUTE_STANDARD_ICON: Final = "standard::icon"
FILE_ATTRIBUTE_STANDARD_IS_BACKUP: Final = "standard::is-backup"
FILE_ATTRIBUTE_STANDARD_IS_HIDDEN: Final = "standard::is-hidden"
FILE_ATTRIBUTE_STANDARD_IS_SYMLINK: Final = "standard::is-symlink"
FILE_ATTRIBUTE_STANDARD_IS_VIRTUAL: Final = "standard::is-virtual"
FILE_ATTRIBUTE_STANDARD_IS_VOLATILE: Final = "standard::is-volatile"
FILE_ATTRIBUTE_STANDARD_NAME: Final = "standard::name"
FILE_ATTRIBUTE_STANDARD_SIZE: Final = "standard::size"
FILE_ATTRIBUTE_STANDARD_SORT_ORDER: Final = "standard::sort-order"
FILE_ATTRIBUTE_STANDARD_SYMBOLIC_ICON: Final = "standard::symbolic-icon"
FILE_ATTRIBUTE_STANDARD_SYMLINK_TARGET: Final = "standard::symlink-target"
FILE_ATTRIBUTE_STANDARD_TARGET_URI: Final = "standard::target-uri"
FILE_ATTRIBUTE_STANDARD_TYPE: Final = "standard::type"
FILE_ATTRIBUTE_THUMBNAILING_FAILED: Final = "thumbnail::failed"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_LARGE: Final = "thumbnail::failed-large"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_NORMAL: Final = "thumbnail::failed-normal"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_XLARGE: Final = "thumbnail::failed-xlarge"
FILE_ATTRIBUTE_THUMBNAILING_FAILED_XXLARGE: Final = "thumbnail::failed-xxlarge"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID: Final = "thumbnail::is-valid"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_LARGE: Final = "thumbnail::is-valid-large"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_NORMAL: Final = "thumbnail::is-valid-normal"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_XLARGE: Final = "thumbnail::is-valid-xlarge"
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_XXLARGE: Final = "thumbnail::is-valid-xxlarge"
FILE_ATTRIBUTE_THUMBNAIL_PATH: Final = "thumbnail::path"
FILE_ATTRIBUTE_THUMBNAIL_PATH_LARGE: Final = "thumbnail::path-large"
FILE_ATTRIBUTE_THUMBNAIL_PATH_NORMAL: Final = "thumbnail::path-normal"
FILE_ATTRIBUTE_THUMBNAIL_PATH_XLARGE: Final = "thumbnail::path-xlarge"
FILE_ATTRIBUTE_THUMBNAIL_PATH_XXLARGE: Final = "thumbnail::path-xxlarge"
FILE_ATTRIBUTE_TIME_ACCESS: Final = "time::access"
FILE_ATTRIBUTE_TIME_ACCESS_NSEC: Final = "time::access-nsec"
FILE_ATTRIBUTE_TIME_ACCESS_USEC: Final = "time::access-usec"
FILE_ATTRIBUTE_TIME_CHANGED: Final = "time::changed"
FILE_ATTRIBUTE_TIME_CHANGED_NSEC: Final = "time::changed-nsec"
FILE_ATTRIBUTE_TIME_CHANGED_USEC: Final = "time::changed-usec"
FILE_ATTRIBUTE_TIME_CREATED: Final = "time::created"
FILE_ATTRIBUTE_TIME_CREATED_NSEC: Final = "time::created-nsec"
FILE_ATTRIBUTE_TIME_CREATED_USEC: Final = "time::created-usec"
FILE_ATTRIBUTE_TIME_MODIFIED: Final = "time::modified"
FILE_ATTRIBUTE_TIME_MODIFIED_NSEC: Final = "time::modified-nsec"
FILE_ATTRIBUTE_TIME_MODIFIED_USEC: Final = "time::modified-usec"
FILE_ATTRIBUTE_TRASH_DELETION_DATE: Final = "trash::deletion-date"
FILE_ATTRIBUTE_TRASH_ITEM_COUNT: Final = "trash::item-count"
FILE_ATTRIBUTE_TRASH_ORIG_PATH: Final = "trash::orig-path"
FILE_ATTRIBUTE_UNIX_BLOCKS: Final = "unix::blocks"
FILE_ATTRIBUTE_UNIX_BLOCK_SIZE: Final = "unix::block-size"
FILE_ATTRIBUTE_UNIX_DEVICE: Final = "unix::device"
FILE_ATTRIBUTE_UNIX_GID: Final = "unix::gid"
FILE_ATTRIBUTE_UNIX_INODE: Final = "unix::inode"
FILE_ATTRIBUTE_UNIX_IS_MOUNTPOINT: Final = "unix::is-mountpoint"
FILE_ATTRIBUTE_UNIX_MODE: Final = "unix::mode"
FILE_ATTRIBUTE_UNIX_NLINK: Final = "unix::nlink"
FILE_ATTRIBUTE_UNIX_RDEV: Final = "unix::rdev"
FILE_ATTRIBUTE_UNIX_UID: Final = "unix::uid"
MEMORY_MONITOR_EXTENSION_POINT_NAME: Final = "gio-memory-monitor"
MENU_ATTRIBUTE_ACTION: Final = "action"
MENU_ATTRIBUTE_ACTION_NAMESPACE: Final = "action-namespace"
MENU_ATTRIBUTE_ICON: Final = "icon"
MENU_ATTRIBUTE_LABEL: Final = "label"
MENU_ATTRIBUTE_TARGET: Final = "target"
MENU_EXPORTER_MAX_SECTION_SIZE: Final[int]
MENU_LINK_SECTION: Final = "section"
MENU_LINK_SUBMENU: Final = "submenu"
NATIVE_VOLUME_MONITOR_EXTENSION_POINT_NAME: Final = "gio-native-volume-monitor"
NETWORK_MONITOR_EXTENSION_POINT_NAME: Final = "gio-network-monitor"
POWER_PROFILE_MONITOR_EXTENSION_POINT_NAME: Final = "gio-power-profile-monitor"
PROXY_EXTENSION_POINT_NAME: Final = "gio-proxy"
PROXY_RESOLVER_EXTENSION_POINT_NAME: Final = "gio-proxy-resolver"
SETTINGS_BACKEND_EXTENSION_POINT_NAME: Final = "gsettings-backend"
TLS_BACKEND_EXTENSION_POINT_NAME: Final = "gio-tls-backend"
TLS_DATABASE_PURPOSE_AUTHENTICATE_CLIENT: Final = "1.3.6.1.5.5.7.3.2"
TLS_DATABASE_PURPOSE_AUTHENTICATE_SERVER: Final = "1.3.6.1.5.5.7.3.1"
VFS_EXTENSION_POINT_NAME: Final = "gio-vfs"
VOLUME_IDENTIFIER_KIND_CLASS: Final = "class"
VOLUME_IDENTIFIER_KIND_HAL_UDI: Final = "hal-udi"
VOLUME_IDENTIFIER_KIND_LABEL: Final = "label"
VOLUME_IDENTIFIER_KIND_NFS_MOUNT: Final = "nfs-mount"
VOLUME_IDENTIFIER_KIND_UNIX_DEVICE: Final = "unix-device"
VOLUME_IDENTIFIER_KIND_UUID: Final = "uuid"
VOLUME_MONITOR_EXTENSION_POINT_NAME: Final = "gio-volume-monitor"

def action_name_is_valid(action_name: str) -> bool: ...
def action_parse_detailed_name(
    detailed_name: str,
) -> tuple[bool, str, GLib.Variant | None]: ...
def action_print_detailed_name(
    action_name: str, target_value: GLib.Variant | None = None
) -> str: ...
def app_info_create_from_commandline(
    commandline: str, application_name: str | None, flags: _AppInfoCreateFlagsValueType
) -> AppInfo: ...
def app_info_get_all() -> list[AppInfo]: ...
def app_info_get_all_for_type(content_type: str) -> list[AppInfo]: ...
def app_info_get_default_for_type(
    content_type: str, must_support_uris: bool
) -> AppInfo | None: ...
@overload
def app_info_get_default_for_type_async(
    content_type: str, must_support_uris: bool, cancellable: Cancellable | None = None
) -> _gi.Async[AppInfo]: ...
@overload
def app_info_get_default_for_type_async(
    content_type: str,
    must_support_uris: bool,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def app_info_get_default_for_type_async(
    content_type: str,
    must_support_uris: bool,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
def app_info_get_default_for_type_finish(result: AsyncResult) -> AppInfo: ...
def app_info_get_default_for_uri_scheme(uri_scheme: str) -> AppInfo | None: ...
@overload
def app_info_get_default_for_uri_scheme_async(
    uri_scheme: str, cancellable: Cancellable | None = None
) -> _gi.Async[AppInfo]: ...
@overload
def app_info_get_default_for_uri_scheme_async(
    uri_scheme: str,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def app_info_get_default_for_uri_scheme_async(
    uri_scheme: str,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
def app_info_get_default_for_uri_scheme_finish(result: AsyncResult) -> AppInfo: ...
def app_info_get_fallback_for_type(content_type: str) -> list[AppInfo]: ...
def app_info_get_recommended_for_type(content_type: str) -> list[AppInfo]: ...
def app_info_launch_default_for_uri(
    uri: str, context: AppLaunchContext | None = None
) -> bool: ...
@overload
def app_info_launch_default_for_uri_async(
    uri: str,
    context: AppLaunchContext | None = None,
    cancellable: Cancellable | None = None,
) -> _gi.Async[bool]: ...
@overload
def app_info_launch_default_for_uri_async(
    uri: str,
    context: AppLaunchContext | None,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def app_info_launch_default_for_uri_async(
    uri: str,
    context: AppLaunchContext | None = None,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
def app_info_launch_default_for_uri_finish(result: AsyncResult) -> bool: ...
def app_info_reset_type_associations(content_type: str) -> None: ...
def async_initable_newv_async(
    object_type: type[Any],
    n_parameters: int,
    parameters: GObject.Parameter,
    io_priority: int,
    cancellable: Cancellable | None = None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None = None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def bus_get(
    bus_type: _BusTypeValueType, cancellable: Cancellable | None = None
) -> _gi.Async[DBusConnection]: ...
@overload
def bus_get(
    bus_type: _BusTypeValueType,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def bus_get(
    bus_type: _BusTypeValueType,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
def bus_get_finish(res: AsyncResult) -> DBusConnection: ...
def bus_get_sync(
    bus_type: _BusTypeValueType, cancellable: Cancellable | None = None
) -> DBusConnection: ...
def bus_own_name(
    bus_type: _BusTypeValueType,
    name: str,
    flags: _BusNameOwnerFlagsValueType,
    bus_acquired_closure: Callable[..., Any] | None = None,
    name_acquired_closure: Callable[..., Any] | None = None,
    name_lost_closure: Callable[..., Any] | None = None,
) -> int: ...
def bus_own_name_on_connection(
    connection: DBusConnection,
    name: str,
    flags: _BusNameOwnerFlagsValueType,
    name_acquired_closure: Callable[..., Any] | None = None,
    name_lost_closure: Callable[..., Any] | None = None,
) -> int: ...
def bus_unown_name(owner_id: int) -> None: ...
def bus_unwatch_name(watcher_id: int) -> None: ...
def bus_watch_name(
    bus_type: _BusTypeValueType,
    name: str,
    flags: _BusNameWatcherFlagsValueType,
    name_appeared_closure: Callable[..., Any] | None = None,
    name_vanished_closure: Callable[..., Any] | None = None,
) -> int: ...
def bus_watch_name_on_connection(
    connection: DBusConnection,
    name: str,
    flags: _BusNameWatcherFlagsValueType,
    name_appeared_closure: Callable[..., Any] | None = None,
    name_vanished_closure: Callable[..., Any] | None = None,
) -> int: ...
def content_type_can_be_executable(type: str) -> bool: ...
def content_type_equals(type1: str, type2: str) -> bool: ...
def content_type_from_mime_type(mime_type: str) -> str | None: ...
def content_type_get_description(type: str) -> str: ...
def content_type_get_generic_icon_name(type: str) -> str | None: ...
def content_type_get_icon(type: str) -> Icon: ...
def content_type_get_mime_dirs() -> list[str]: ...
def content_type_get_mime_type(type: str) -> str | None: ...
def content_type_get_symbolic_icon(type: str) -> Icon: ...
def content_type_guess(
    filename: str | None = None, data: Sequence[int] | None = None
) -> tuple[str, bool]: ...
def content_type_guess_for_tree(root: File) -> list[str]: ...
def content_type_is_a(type: str, supertype: str) -> bool: ...
def content_type_is_mime_type(type: str, mime_type: str) -> bool: ...
def content_type_is_unknown(type: str) -> bool: ...
def content_type_set_mime_dirs(dirs: Sequence[str] | None = None) -> None: ...
def content_types_get_registered() -> list[str]: ...
def dbus_address_escape_value(string: str) -> str: ...
def dbus_address_get_for_bus_sync(
    bus_type: _BusTypeValueType, cancellable: Cancellable | None = None
) -> str: ...
@overload
def dbus_address_get_stream(
    address: str, cancellable: Cancellable | None = None
) -> _gi.Async[tuple[IOStream, str | None]]: ...
@overload
def dbus_address_get_stream(
    address: str,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def dbus_address_get_stream(
    address: str,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
def dbus_address_get_stream_finish(res: AsyncResult) -> tuple[IOStream, str | None]: ...
def dbus_address_get_stream_sync(
    address: str, cancellable: Cancellable | None = None
) -> tuple[IOStream, str | None]: ...
def dbus_annotation_info_lookup(
    annotations: Sequence[DBusAnnotationInfo] | None, name: str
) -> str | None: ...
def dbus_error_encode_gerror(error: GLib.Error) -> str: ...
def dbus_error_get_remote_error(error: GLib.Error) -> str | None: ...
def dbus_error_is_remote_error(error: GLib.Error) -> bool: ...
def dbus_error_new_for_dbus_error(
    dbus_error_name: str, dbus_error_message: str
) -> GLib.Error: ...
def dbus_error_quark() -> int: ...
def dbus_error_register_error(
    error_domain: int, error_code: int, dbus_error_name: str
) -> bool: ...
def dbus_error_register_error_domain(
    error_domain_quark_name: str, quark_volatile: int, entries: Sequence[DBusErrorEntry]
) -> None: ...
def dbus_error_strip_remote_error(error: GLib.Error) -> bool: ...
def dbus_error_unregister_error(
    error_domain: int, error_code: int, dbus_error_name: str
) -> bool: ...
def dbus_escape_object_path(s: str) -> str: ...
def dbus_escape_object_path_bytestring(bytes: Sequence[int]) -> str: ...
def dbus_generate_guid() -> str: ...
def dbus_gvalue_to_gvariant(gvalue: Any, type: GLib.VariantType) -> GLib.Variant: ...
def dbus_gvariant_to_gvalue(value: GLib.Variant) -> Any: ...
def dbus_is_address(string: str) -> bool: ...
def dbus_is_error_name(string: str) -> bool: ...
def dbus_is_guid(string: str) -> bool: ...
def dbus_is_interface_name(string: str) -> bool: ...
def dbus_is_member_name(string: str) -> bool: ...
def dbus_is_name(string: str) -> bool: ...
def dbus_is_supported_address(string: str) -> bool: ...
def dbus_is_unique_name(string: str) -> bool: ...
def dbus_unescape_object_path(s: str) -> bytes: ...
def dtls_client_connection_new(
    base_socket: DatagramBased, server_identity: SocketConnectable | None = None
) -> DtlsClientConnection: ...
def dtls_server_connection_new(
    base_socket: DatagramBased, certificate: TlsCertificate | None = None
) -> DtlsServerConnection: ...
def file_new_build_filenamev(args: Sequence[str]) -> File: ...
def file_new_for_commandline_arg(arg: str) -> File: ...
def file_new_for_commandline_arg_and_cwd(arg: str, cwd: str) -> File: ...
def file_new_for_path(path: str) -> File: ...
def file_new_for_uri(uri: str) -> File: ...
def file_new_tmp(tmpl: str | None = None) -> tuple[File, FileIOStream]: ...
@overload
def file_new_tmp_async(
    tmpl: str | None, io_priority: int, cancellable: Cancellable | None = None
) -> _gi.Async[tuple[File, FileIOStream]]: ...
@overload
def file_new_tmp_async(
    tmpl: str | None,
    io_priority: int,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def file_new_tmp_async(
    tmpl: str | None,
    io_priority: int,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
@overload
def file_new_tmp_dir_async(
    tmpl: str | None, io_priority: int, cancellable: Cancellable | None = None
) -> _gi.Async[File]: ...
@overload
def file_new_tmp_dir_async(
    tmpl: str | None,
    io_priority: int,
    cancellable: Cancellable | None,
    callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
    *user_data: Unpack[_DataTs],
) -> None: ...
@overload
def file_new_tmp_dir_async(
    tmpl: str | None,
    io_priority: int,
    cancellable: Cancellable | None = None,
    *,
    callback: _AsyncReadyVarArgsCallback[None] | None,
) -> None: ...
def file_new_tmp_dir_finish(result: AsyncResult) -> File: ...
def file_new_tmp_finish(result: AsyncResult) -> tuple[File, FileIOStream]: ...
def file_parse_name(parse_name: str) -> File: ...
def icon_deserialize(value: GLib.Variant) -> Icon | None: ...
def icon_new_for_string(str: str) -> Icon: ...
def initable_newv(
    object_type: type[Any],
    parameters: Sequence[GObject.Parameter],
    cancellable: Cancellable | None = None,
) -> GObject.Object: ...
def io_error_from_errno(err_no: int) -> IOErrorEnum: ...
def io_error_from_file_error(file_error: GLib.FileError) -> IOErrorEnum: ...
def io_error_quark() -> int: ...
def io_extension_point_implement(
    extension_point_name: str, type: type[Any], extension_name: str, priority: int
) -> IOExtension: ...
def io_extension_point_lookup(name: str) -> IOExtensionPoint: ...
def io_extension_point_register(name: str) -> IOExtensionPoint: ...
def io_modules_load_all_in_directory(dirname: str) -> list[IOModule]: ...
def io_modules_load_all_in_directory_with_scope(
    dirname: str, scope: IOModuleScope
) -> list[IOModule]: ...
def io_modules_scan_all_in_directory(dirname: str) -> None: ...
def io_modules_scan_all_in_directory_with_scope(
    dirname: str, scope: IOModuleScope
) -> None: ...
def io_scheduler_cancel_all_jobs() -> None: ...
def io_scheduler_push_job(
    job_func: Callable[[IOSchedulerJob, Cancellable | None, Any | None], bool],
    user_data: Any | None,
    io_priority: int,
    cancellable: Cancellable | None = None,
) -> None: ...
def keyfile_settings_backend_new(
    filename: str, root_path: str, root_group: str | None = None
) -> SettingsBackend: ...
def memory_monitor_dup_default() -> MemoryMonitor: ...
def memory_settings_backend_new() -> SettingsBackend: ...
def network_monitor_get_default() -> NetworkMonitor: ...
def networking_init() -> None: ...
def null_settings_backend_new() -> SettingsBackend: ...
def pollable_source_new(pollable_stream: GObject.Object) -> GLib.Source: ...
def pollable_source_new_full(
    pollable_stream: GObject.Object,
    child_source: GLib.Source | None = None,
    cancellable: Cancellable | None = None,
) -> GLib.Source: ...
def pollable_stream_read(
    stream: InputStream,
    buffer: Sequence[int],
    blocking: bool,
    cancellable: Cancellable | None = None,
) -> int: ...
def pollable_stream_write(
    stream: OutputStream,
    buffer: Sequence[int],
    blocking: bool,
    cancellable: Cancellable | None = None,
) -> int: ...
def pollable_stream_write_all(
    stream: OutputStream,
    buffer: Sequence[int],
    blocking: bool,
    cancellable: Cancellable | None = None,
) -> tuple[bool, int]: ...
def power_profile_monitor_dup_default() -> PowerProfileMonitor: ...
def proxy_get_default_for_protocol(protocol: str) -> Proxy | None: ...
def proxy_resolver_get_default() -> ProxyResolver: ...
def resolver_error_quark() -> int: ...
def resource_error_quark() -> int: ...
def resource_load(filename: str) -> Resource: ...
def resources_enumerate_children(
    path: str, lookup_flags: _ResourceLookupFlagsValueType
) -> list[str]: ...
def resources_get_info(
    path: str, lookup_flags: _ResourceLookupFlagsValueType
) -> tuple[bool, int, int]: ...
def resources_has_children(path: str) -> bool: ...
def resources_lookup_data(
    path: str, lookup_flags: _ResourceLookupFlagsValueType
) -> GLib.Bytes: ...
def resources_open_stream(
    path: str, lookup_flags: _ResourceLookupFlagsValueType
) -> InputStream: ...
def resources_register(resource: Resource) -> None: ...
def resources_unregister(resource: Resource) -> None: ...
def settings_schema_source_get_default() -> SettingsSchemaSource | None: ...
def simple_async_report_gerror_in_idle(
    object: GObject.Object | None,
    callback: _AsyncReadyCallback[None, Any | None] | None,
    user_data: Any | None,
    error: GLib.Error,
) -> None: ...
def tls_backend_get_default() -> TlsBackend: ...
def tls_channel_binding_error_quark() -> int: ...
def tls_client_connection_new(
    base_io_stream: IOStream, server_identity: SocketConnectable | None = None
) -> TlsClientConnection: ...
def tls_error_quark() -> int: ...
def tls_file_database_new(anchors: str) -> TlsFileDatabase: ...
def tls_server_connection_new(
    base_io_stream: IOStream, certificate: TlsCertificate | None = None
) -> TlsServerConnection: ...

unix_is_mount_path_system_internal: Final = GioUnix.is_mount_path_system_internal
unix_is_system_device_path: Final = GioUnix.is_system_device_path
unix_is_system_fs_type: Final = GioUnix.is_system_fs_type
unix_mount_at: Final = GioUnix.mount_at
unix_mount_compare: Final = GioUnix.mount_compare
unix_mount_copy: Final = GioUnix.mount_copy
unix_mount_entries_changed_since: Final = GioUnix.mount_entries_changed_since
unix_mount_entries_get: Final = GioUnix.mount_entries_get
unix_mount_entries_get_from_file: Final = GioUnix.mount_entries_get_from_file
unix_mount_entry_at: Final = GioUnix.mount_entry_at
unix_mount_entry_for: Final = GioUnix.mount_entry_for
unix_mount_for: Final = GioUnix.mount_for
unix_mount_free: Final = GioUnix.mount_free
unix_mount_get_device_path: Final = GioUnix.mount_get_device_path
unix_mount_get_fs_type: Final = GioUnix.mount_get_fs_type
unix_mount_get_mount_path: Final = GioUnix.mount_get_mount_path
unix_mount_get_options: Final = GioUnix.mount_get_options
unix_mount_get_root_path: Final = GioUnix.mount_get_root_path
unix_mount_guess_can_eject: Final = GioUnix.mount_guess_can_eject
unix_mount_guess_icon: Final = GioUnix.mount_guess_icon
unix_mount_guess_name: Final = GioUnix.mount_guess_name
unix_mount_guess_should_display: Final = GioUnix.mount_guess_should_display
unix_mount_guess_symbolic_icon: Final = GioUnix.mount_guess_symbolic_icon
unix_mount_is_readonly: Final = GioUnix.mount_is_readonly
unix_mount_is_system_internal: Final = GioUnix.mount_is_system_internal
unix_mount_point_at: Final = GioUnix.mount_point_at
unix_mount_points_changed_since: Final = GioUnix.mount_points_changed_since
unix_mount_points_get: Final = GioUnix.mount_points_get
unix_mount_points_get_from_file: Final = GioUnix.mount_points_get_from_file
unix_mounts_changed_since: Final = GioUnix.mounts_changed_since
unix_mounts_get: Final = GioUnix.mounts_get
unix_mounts_get_from_file: Final = GioUnix.mounts_get_from_file

class Action(GObject.GInterface, Protocol):
    """
    Interface GAction

    Signals from GObject:
      notify (GParam)
    """
    def activate(self, parameter: GLib.Variant | None = None) -> None: ...
    def change_state(self, value: GLib.Variant) -> None: ...
    def get_enabled(self) -> bool: ...
    def get_name(self) -> str: ...
    def get_parameter_type(self) -> GLib.VariantType | None: ...
    def get_state(self) -> GLib.Variant | None: ...
    def get_state_hint(self) -> GLib.Variant | None: ...
    def get_state_type(self) -> GLib.VariantType | None: ...
    @staticmethod
    def name_is_valid(action_name: str) -> bool: ...
    @staticmethod
    def parse_detailed_name(
        detailed_name: str,
    ) -> tuple[bool, str, GLib.Variant | None]: ...
    @staticmethod
    def print_detailed_name(
        action_name: str, target_value: GLib.Variant | None = None
    ) -> str: ...

class ActionEntry(_gi.Struct):
    """
    :Constructors:

    ::

        ActionEntry()
    """

    name: str
    @property
    def activate(self) -> Callable[[SimpleAction, GLib.Variant, Any | None], None]: ...
    parameter_type: str
    state: str
    @property
    def change_state(
        self,
    ) -> Callable[[SimpleAction, GLib.Variant, Any | None], None]: ...
    @property
    def padding(self) -> list[int]: ...

class ActionGroup(GObject.GInterface, Protocol):
    """
    Interface GActionGroup

    Signals from GObject:
      notify (GParam)
    """
    def action_added(self, action_name: str) -> None: ...
    def action_enabled_changed(self, action_name: str, enabled: bool) -> None: ...
    def action_removed(self, action_name: str) -> None: ...
    def action_state_changed(self, action_name: str, state: GLib.Variant) -> None: ...
    def activate_action(
        self, action_name: str, parameter: GLib.Variant | None = None
    ) -> None: ...
    def change_action_state(self, action_name: str, value: GLib.Variant) -> None: ...
    def get_action_enabled(self, action_name: str) -> bool: ...
    def get_action_parameter_type(
        self, action_name: str
    ) -> GLib.VariantType | None: ...
    def get_action_state(self, action_name: str) -> GLib.Variant | None: ...
    def get_action_state_hint(self, action_name: str) -> GLib.Variant | None: ...
    def get_action_state_type(self, action_name: str) -> GLib.VariantType | None: ...
    def has_action(self, action_name: str) -> bool: ...
    def list_actions(self) -> list[str]: ...
    def query_action(
        self, action_name: str
    ) -> tuple[
        bool, bool, GLib.VariantType, GLib.VariantType, GLib.Variant, GLib.Variant
    ]: ...

class ActionGroupInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ActionGroupInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def has_action(self) -> Callable[[ActionGroup, str], bool]: ...
    @property
    def list_actions(self) -> Callable[[ActionGroup], list[str]]: ...
    @property
    def get_action_enabled(self) -> Callable[[ActionGroup, str], bool]: ...
    @property
    def get_action_parameter_type(
        self,
    ) -> Callable[[ActionGroup, str], GLib.VariantType | None]: ...
    @property
    def get_action_state_type(
        self,
    ) -> Callable[[ActionGroup, str], GLib.VariantType | None]: ...
    @property
    def get_action_state_hint(
        self,
    ) -> Callable[[ActionGroup, str], GLib.Variant | None]: ...
    @property
    def get_action_state(self) -> Callable[[ActionGroup, str], GLib.Variant | None]: ...
    @property
    def change_action_state(
        self,
    ) -> Callable[[ActionGroup, str, GLib.Variant], None]: ...
    @property
    def activate_action(
        self,
    ) -> Callable[[ActionGroup, str, GLib.Variant | None], None]: ...
    @property
    def action_added(self) -> Callable[[ActionGroup, str], None]: ...
    @property
    def action_removed(self) -> Callable[[ActionGroup, str], None]: ...
    @property
    def action_enabled_changed(self) -> Callable[[ActionGroup, str, bool], None]: ...
    @property
    def action_state_changed(
        self,
    ) -> Callable[[ActionGroup, str, GLib.Variant], None]: ...
    @property
    def query_action(
        self,
    ) -> Callable[
        [ActionGroup, str],
        tuple[
            bool, bool, GLib.VariantType, GLib.VariantType, GLib.Variant, GLib.Variant
        ],
    ]: ...

class ActionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ActionInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_name(self) -> Callable[[Action], str]: ...
    @property
    def get_parameter_type(self) -> Callable[[Action], GLib.VariantType | None]: ...
    @property
    def get_state_type(self) -> Callable[[Action], GLib.VariantType | None]: ...
    @property
    def get_state_hint(self) -> Callable[[Action], GLib.Variant | None]: ...
    @property
    def get_enabled(self) -> Callable[[Action], bool]: ...
    @property
    def get_state(self) -> Callable[[Action], GLib.Variant | None]: ...
    @property
    def change_state(self) -> Callable[[Action, GLib.Variant], None]: ...
    @property
    def activate(self) -> Callable[[Action, GLib.Variant | None], None]: ...

class ActionMap(GObject.GInterface, Protocol):
    """
    Interface GActionMap

    Signals from GObject:
      notify (GParam)
    """
    def add_action(self, action: Action) -> None: ...
    def add_action_entries(self, entries, user_data=None):
        """
        The ``add_action_entries()`` method is a convenience function for creating
        multiple :class:`~gi.repository.Gio.SimpleAction` instances and adding them
        to a :class:`~gi.repository.Gio.ActionMap`.
        Each action is constructed as per one entry.

        :param list entries:
            List of entry tuples for :meth:`add_action` method. The entry tuple can
            vary in size with the following information:

            * The name of the action. Must be specified.
            * The callback to connect to the "activate" signal of the
              action. Since GLib 2.40, this can be ``None`` for stateful
              actions, in which case the default handler is used. For
              boolean-stated actions with no parameter, this is a toggle.
              For other state types (and parameter type equal to the state
              type) this will be a function that just calls change_state
              (which you should provide).
            * The type of the parameter that must be passed to the activate
              function for this action, given as a single :class:`~gi.repository.GLib.Variant` type
              string (or ``None`` for no parameter)
            * The initial state for this action, given in GLib.Variant text
              format. The state is parsed with no extra type information, so
              type tags must be added to the string if they are necessary.
              Stateless actions should give ``None`` here.
            * The callback to connect to the "change-state" signal of the
              action. All stateful actions should provide a handler here;
              stateless actions should not.

        :param user_data:
            The user data for signal connections, or ``None``
        """  # FIXME: Override is missing typing annotation
    def lookup_action(self, action_name: str) -> Action | None: ...
    def remove_action(self, action_name: str) -> None: ...
    def remove_action_entries(self, entries: Sequence[ActionEntry]) -> None: ...

class ActionMapInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ActionMapInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def lookup_action(self) -> Callable[[ActionMap, str], Action | None]: ...
    @property
    def add_action(self) -> Callable[[ActionMap, Action], None]: ...
    @property
    def remove_action(self) -> Callable[[ActionMap, str], None]: ...

class AppInfo(GObject.GInterface, Protocol):
    """
    Interface GAppInfo

    Signals from GObject:
      notify (GParam)
    """
    def add_supports_type(self, content_type: str) -> bool: ...
    def can_delete(self) -> bool: ...
    def can_remove_supports_type(self) -> bool: ...
    @staticmethod
    def create_from_commandline(
        commandline: str,
        application_name: str | None,
        flags: _AppInfoCreateFlagsValueType,
    ) -> AppInfo: ...
    def delete(self) -> bool: ...
    def dup(self) -> AppInfo: ...
    def equal(self, appinfo2: AppInfo) -> bool: ...
    @staticmethod
    def get_all() -> list[AppInfo]: ...
    @staticmethod
    def get_all_for_type(content_type: str) -> list[AppInfo]: ...
    def get_commandline(self) -> str | None: ...
    @staticmethod
    def get_default_for_type(
        content_type: str, must_support_uris: bool
    ) -> AppInfo | None: ...
    @overload
    @staticmethod
    def get_default_for_type_async(
        content_type: str,
        must_support_uris: bool,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[AppInfo]: ...
    @overload
    @staticmethod
    def get_default_for_type_async(
        content_type: str,
        must_support_uris: bool,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def get_default_for_type_async(
        content_type: str,
        must_support_uris: bool,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @staticmethod
    def get_default_for_type_finish(result: AsyncResult) -> AppInfo: ...
    @staticmethod
    def get_default_for_uri_scheme(uri_scheme: str) -> AppInfo | None: ...
    @overload
    @staticmethod
    def get_default_for_uri_scheme_async(
        uri_scheme: str, cancellable: Cancellable | None = None
    ) -> _gi.Async[AppInfo]: ...
    @overload
    @staticmethod
    def get_default_for_uri_scheme_async(
        uri_scheme: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def get_default_for_uri_scheme_async(
        uri_scheme: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @staticmethod
    def get_default_for_uri_scheme_finish(result: AsyncResult) -> AppInfo: ...
    def get_description(self) -> str | None: ...
    def get_display_name(self) -> str: ...
    def get_executable(self) -> str: ...
    @staticmethod
    def get_fallback_for_type(content_type: str) -> list[AppInfo]: ...
    def get_icon(self) -> Icon | None: ...
    def get_id(self) -> str | None: ...
    def get_name(self) -> str: ...
    @staticmethod
    def get_recommended_for_type(content_type: str) -> list[AppInfo]: ...
    def get_supported_types(self) -> list[str]: ...
    def launch(
        self, files: list[File] | None = None, context: AppLaunchContext | None = None
    ) -> bool: ...
    @staticmethod
    def launch_default_for_uri(
        uri: str, context: AppLaunchContext | None = None
    ) -> bool: ...
    @overload
    @staticmethod
    def launch_default_for_uri_async(
        uri: str,
        context: AppLaunchContext | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    @staticmethod
    def launch_default_for_uri_async(
        uri: str,
        context: AppLaunchContext | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def launch_default_for_uri_async(
        uri: str,
        context: AppLaunchContext | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @staticmethod
    def launch_default_for_uri_finish(result: AsyncResult) -> bool: ...
    def launch_uris(
        self, uris: list[str] | None = None, context: AppLaunchContext | None = None
    ) -> bool: ...
    @overload
    def launch_uris_async(
        self,
        uris: list[str] | None = None,
        context: AppLaunchContext | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def launch_uris_async(
        self,
        uris: list[str] | None,
        context: AppLaunchContext | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[AppInfo, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def launch_uris_async(
        self,
        uris: list[str] | None = None,
        context: AppLaunchContext | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[AppInfo] | None,
    ) -> None: ...
    def launch_uris_finish(self, result: AsyncResult) -> bool: ...
    def remove_supports_type(self, content_type: str) -> bool: ...
    @staticmethod
    def reset_type_associations(content_type: str) -> None: ...
    def set_as_default_for_extension(self, extension: str) -> bool: ...
    def set_as_default_for_type(self, content_type: str) -> bool: ...
    def set_as_last_used_for_type(self, content_type: str) -> bool: ...
    def should_show(self) -> bool: ...
    def supports_files(self) -> bool: ...
    def supports_uris(self) -> bool: ...

class AppInfoIface(_gi.Struct):
    """
    :Constructors:

    ::

        AppInfoIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def dup(self) -> Callable[[AppInfo], AppInfo]: ...
    @property
    def equal(self) -> Callable[[AppInfo, AppInfo], bool]: ...
    @property
    def get_id(self) -> Callable[[AppInfo], str | None]: ...
    @property
    def get_name(self) -> Callable[[AppInfo], str]: ...
    @property
    def get_description(self) -> Callable[[AppInfo], str | None]: ...
    @property
    def get_executable(self) -> Callable[[AppInfo], str]: ...
    @property
    def get_icon(self) -> Callable[[AppInfo], Icon | None]: ...
    @property
    def launch(
        self,
    ) -> Callable[[AppInfo, list[File] | None, AppLaunchContext | None], bool]: ...
    @property
    def supports_uris(self) -> Callable[[AppInfo], bool]: ...
    @property
    def supports_files(self) -> Callable[[AppInfo], bool]: ...
    @property
    def launch_uris(
        self,
    ) -> Callable[[AppInfo, list[str] | None, AppLaunchContext | None], bool]: ...
    @property
    def should_show(self) -> Callable[[AppInfo], bool]: ...
    @property
    def set_as_default_for_type(self) -> Callable[[AppInfo, str], bool]: ...
    @property
    def set_as_default_for_extension(self) -> Callable[[AppInfo, str], bool]: ...
    @property
    def add_supports_type(self) -> Callable[[AppInfo, str], bool]: ...
    @property
    def can_remove_supports_type(self) -> Callable[[AppInfo], bool]: ...
    @property
    def remove_supports_type(self) -> Callable[[AppInfo, str], bool]: ...
    @property
    def can_delete(self) -> Callable[[AppInfo], bool]: ...
    @property
    def do_delete(self) -> Callable[[AppInfo], bool]: ...
    @property
    def get_commandline(self) -> Callable[[AppInfo], str | None]: ...
    @property
    def get_display_name(self) -> Callable[[AppInfo], str]: ...
    @property
    def set_as_last_used_for_type(self) -> Callable[[AppInfo, str], bool]: ...
    @property
    def get_supported_types(self) -> Callable[[AppInfo], list[str]]: ...
    @property
    def launch_uris_async(
        self,
    ) -> Callable[
        [
            AppInfo,
            list[str] | None,
            AppLaunchContext | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def launch_uris_finish(self) -> Callable[[AppInfo, AsyncResult], bool]: ...

class AppInfoMonitor(GObject.Object):
    """
    :Constructors:

    ::

        AppInfoMonitor(**properties)

    Object GAppInfoMonitor

    Signals from GAppInfoMonitor:
      changed ()

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get() -> AppInfoMonitor: ...

class AppLaunchContext(GObject.Object):
    """
    :Constructors:

    ::

        AppLaunchContext(**properties)
        new() -> Gio.AppLaunchContext

    Object GAppLaunchContext

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> AppLaunchContextPrivate: ...
    def do_get_display(self, info: AppInfo, files: list[File], /) -> str | None: ...
    def do_get_startup_notify_id(
        self, info: AppInfo | None, files: list[File] | None, /
    ) -> str | None: ...
    def do_launch_failed(self, startup_notify_id: str, /) -> None: ...
    def do_launch_started(
        self, info: AppInfo, platform_data: GLib.Variant, /
    ) -> None: ...
    def do_launched(self, info: AppInfo, platform_data: GLib.Variant, /) -> None: ...
    def get_display(self, info: AppInfo, files: list[File]) -> str | None: ...
    def get_environment(self) -> list[str]: ...
    def get_startup_notify_id(
        self, info: AppInfo | None = None, files: list[File] | None = None
    ) -> str | None: ...
    def launch_failed(self, startup_notify_id: str) -> None: ...
    @classmethod
    def new(cls) -> AppLaunchContext: ...
    def setenv(self, variable: str, value: str) -> None: ...
    def unsetenv(self, variable: str) -> None: ...

class AppLaunchContextClass(_gi.Struct):
    """
    :Constructors:

    ::

        AppLaunchContextClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_display(
        self,
    ) -> Callable[[AppLaunchContext, AppInfo, list[File]], str | None]: ...
    @property
    def get_startup_notify_id(
        self,
    ) -> Callable[
        [AppLaunchContext, AppInfo | None, list[File] | None], str | None
    ]: ...
    @property
    def launch_failed(self) -> Callable[[AppLaunchContext, str], None]: ...
    @property
    def launched(self) -> Callable[[AppLaunchContext, AppInfo, GLib.Variant], None]: ...
    @property
    def launch_started(
        self,
    ) -> Callable[[AppLaunchContext, AppInfo, GLib.Variant], None]: ...

class AppLaunchContextPrivate(_gi.Struct): ...

class Application(GObject.Object, ActionGroup, ActionMap):
    """
    :Constructors:

    ::

        Application(**properties)
        new(application_id:str=None, flags:Gio.ApplicationFlags) -> Gio.Application

    Object GApplication

    Signals from GApplication:
      startup ()
      shutdown ()
      activate ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean

    Properties from GApplication:
      application-id -> gchararray: application-id
      version -> gchararray: version
      flags -> GApplicationFlags: flags
      resource-base-path -> gchararray: resource-base-path
      is-registered -> gboolean: is-registered
      is-remote -> gboolean: is-remote
      inactivity-timeout -> guint: inactivity-timeout
      action-group -> GActionGroup: action-group
      is-busy -> gboolean: is-busy

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def action_group(self) -> Never: ...
        @action_group.setter
        def action_group(self, value: ActionGroup | None) -> None: ...
        application_id: str | None
        @property
        def flags(self) -> ApplicationFlags: ...
        @flags.setter
        def flags(self, value: _ApplicationFlagsValueType) -> None: ...
        inactivity_timeout: int
        @property
        def is_busy(self) -> bool: ...
        @property
        def is_registered(self) -> bool: ...
        @property
        def is_remote(self) -> bool: ...
        resource_base_path: str | None
        @property
        def version(self) -> str | None: ...
        @version.setter
        def version(self, value: str) -> None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> ApplicationPrivate: ...
    def __init__(
        self,
        *,
        action_group: ActionGroup | None = ...,
        application_id: str | None = ...,
        flags: _ApplicationFlagsValueType = ...,
        inactivity_timeout: int = ...,
        resource_base_path: str | None = ...,
        version: str = ...,
    ) -> None: ...
    def activate(self) -> None: ...
    def add_main_option(
        self,
        long_name: str,
        short_name: int,
        flags: GLib.OptionFlags,
        arg: GLib.OptionArg,
        description: str,
        arg_description: str | None = None,
    ) -> None: ...
    def add_main_option_entries(self, entries: Sequence[GLib.OptionEntry]) -> None: ...
    def add_option_group(self, group: GLib.OptionGroup) -> None: ...
    def bind_busy_property(self, object: GObject.Object, property: str) -> None: ...
    # override
    def create_asyncio_task(self, coro: asyncio._CoroutineLike[_T]) -> asyncio.Task[_T]:
        """
        Safely create an asyncio task. The application will not quit until the
        task completes. For potentially longer running tasks, you should add
        cancellation logic to abort a task when it is not needed anymore (e.g.
        cancelling it from the Gtk.Window.do_unmap event).

        Note that python will only log a raised exception if the Task is
        destroyed without the result having been collected. However, this does
        also not happen when the task is cancelled. As such, be careful to not
        cancel tasks that are already finished.

        You can deal with this by either only storing a weak reference to the
        Task, by explicitly collecting the result, or by only cancelling it if
        it is not done already.
        """
    def do_activate(self) -> None: ...
    def do_add_platform_data(self, builder: GLib.VariantBuilder, /) -> None: ...
    def do_after_emit(self, platform_data: GLib.Variant, /) -> None: ...
    def do_before_emit(self, platform_data: GLib.Variant, /) -> None: ...
    def do_command_line(self, command_line: ApplicationCommandLine, /) -> int: ...
    def do_dbus_register(
        self, connection: DBusConnection, object_path: str, /
    ) -> bool: ...
    def do_dbus_unregister(
        self, connection: DBusConnection, object_path: str, /
    ) -> None: ...
    def do_handle_local_options(self, options: GLib.VariantDict, /) -> int: ...
    def do_local_command_line(
        self, arguments: Sequence[str], /
    ) -> tuple[bool, list[str], int]: ...
    def do_name_lost(self) -> bool: ...
    # override
    def do_open(self, files: Sequence[File], n_files: int, hint: str) -> None: ...
    def do_quit_mainloop(self) -> None: ...
    def do_run_mainloop(self) -> None: ...
    def do_shutdown(self) -> None: ...
    def do_startup(self) -> None: ...
    def get_application_id(self) -> str | None: ...
    def get_dbus_connection(self) -> DBusConnection | None: ...
    def get_dbus_object_path(self) -> str | None: ...
    @staticmethod
    def get_default() -> Application | None: ...
    def get_flags(self) -> ApplicationFlags: ...
    def get_inactivity_timeout(self) -> int: ...
    def get_is_busy(self) -> bool: ...
    def get_is_registered(self) -> bool: ...
    def get_is_remote(self) -> bool: ...
    def get_resource_base_path(self) -> str | None: ...
    def get_version(self) -> str | None: ...
    def hold(self) -> None: ...
    @staticmethod
    def id_is_valid(application_id: str) -> bool: ...
    def mark_busy(self) -> None: ...
    @classmethod
    def new(
        cls, application_id: str | None, flags: _ApplicationFlagsValueType
    ) -> Application: ...
    def open(self, files: Sequence[File], hint: str) -> None: ...
    def quit(self) -> None: ...
    def register(self, cancellable: Cancellable | None = None) -> bool: ...
    def release(self) -> None: ...
    # override
    def run(self, argv: list[str] | None = None) -> int: ...
    def send_notification(self, id: str | None, notification: Notification) -> None: ...
    def set_action_group(self, action_group: ActionGroup | None = None) -> None: ...
    def set_application_id(self, application_id: str | None = None) -> None: ...
    def set_default(self) -> None: ...
    def set_flags(self, flags: _ApplicationFlagsValueType) -> None: ...
    def set_inactivity_timeout(self, inactivity_timeout: int) -> None: ...
    def set_option_context_description(
        self, description: str | None = None
    ) -> None: ...
    def set_option_context_parameter_string(
        self, parameter_string: str | None = None
    ) -> None: ...
    def set_option_context_summary(self, summary: str | None = None) -> None: ...
    def set_resource_base_path(self, resource_path: str | None = None) -> None: ...
    def set_version(self, version: str) -> None: ...
    def unbind_busy_property(self, object: GObject.Object, property: str) -> None: ...
    def unmark_busy(self) -> None: ...
    def withdraw_notification(self, id: str) -> None: ...

class ApplicationClass(_gi.Struct):
    """
    :Constructors:

    ::

        ApplicationClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def startup(self) -> Callable[[Application], None]: ...
    @property
    def activate(self) -> Callable[[Application], None]: ...
    @property
    def open(self) -> Callable[[Application, Sequence[File], int, str], None]: ...
    @property
    def command_line(self) -> Callable[[Application, ApplicationCommandLine], int]: ...
    @property
    def local_command_line(
        self,
    ) -> Callable[[Application, Sequence[str]], tuple[bool, list[str], int]]: ...
    @property
    def before_emit(self) -> Callable[[Application, GLib.Variant], None]: ...
    @property
    def after_emit(self) -> Callable[[Application, GLib.Variant], None]: ...
    @property
    def add_platform_data(
        self,
    ) -> Callable[[Application, GLib.VariantBuilder], None]: ...
    @property
    def quit_mainloop(self) -> Callable[[Application], None]: ...
    @property
    def run_mainloop(self) -> Callable[[Application], None]: ...
    @property
    def shutdown(self) -> Callable[[Application], None]: ...
    @property
    def dbus_register(self) -> Callable[[Application, DBusConnection, str], bool]: ...
    @property
    def dbus_unregister(self) -> Callable[[Application, DBusConnection, str], None]: ...
    @property
    def handle_local_options(
        self,
    ) -> Callable[[Application, GLib.VariantDict], int]: ...
    @property
    def name_lost(self) -> Callable[[Application], bool]: ...
    @property
    def padding(self) -> list[int]: ...

class ApplicationCommandLine(GObject.Object):
    """
    :Constructors:

    ::

        ApplicationCommandLine(**properties)

    Object GApplicationCommandLine

    Properties from GApplicationCommandLine:
      arguments -> GVariant: arguments
      options -> GVariant: options
      platform-data -> GVariant: platform-data
      is-remote -> gboolean: is-remote

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def is_remote(self) -> bool: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> ApplicationCommandLinePrivate: ...
    def __init__(
        self,
        *,
        arguments: GLib.Variant | None = ...,
        options: GLib.Variant | None = ...,
        platform_data: GLib.Variant | None = ...,
    ) -> None: ...
    def create_file_for_arg(self, arg: str) -> File: ...
    def do_done(self) -> None: ...
    def do_get_stdin(self) -> InputStream | None: ...
    def do_print_literal(self, message: str, /) -> None: ...
    def do_printerr_literal(self, message: str, /) -> None: ...
    def done(self) -> None: ...
    def get_arguments(self) -> list[str]: ...
    def get_cwd(self) -> str | None: ...
    def get_environ(self) -> list[str]: ...
    def get_exit_status(self) -> int: ...
    def get_is_remote(self) -> bool: ...
    def get_options_dict(self) -> GLib.VariantDict: ...
    def get_platform_data(self) -> GLib.Variant | None: ...
    def get_stdin(self) -> InputStream | None: ...
    def getenv(self, name: str) -> str | None: ...
    def print_literal(self, message: str) -> None: ...
    def printerr_literal(self, message: str) -> None: ...
    def set_exit_status(self, exit_status: int) -> None: ...

class ApplicationCommandLineClass(_gi.Struct):
    """
    :Constructors:

    ::

        ApplicationCommandLineClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def print_literal(self) -> Callable[[ApplicationCommandLine, str], None]: ...
    @property
    def printerr_literal(self) -> Callable[[ApplicationCommandLine, str], None]: ...
    @property
    def get_stdin(self) -> Callable[[ApplicationCommandLine], InputStream | None]: ...
    @property
    def done(self) -> Callable[[ApplicationCommandLine], None]: ...
    @property
    def padding(self) -> list[int]: ...

class ApplicationCommandLinePrivate(_gi.Struct): ...
class ApplicationPrivate(_gi.Struct): ...

class AsyncInitable(GObject.GInterface, Protocol):
    """
    Interface GAsyncInitable

    Signals from GObject:
      notify (GParam)
    """
    @overload
    def init_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def init_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[AsyncInitable, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def init_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[AsyncInitable] | None,
    ) -> None: ...
    def init_finish(self, res: AsyncResult) -> bool: ...
    def new_finish(self, res: AsyncResult) -> GObject.Object: ...
    @staticmethod
    def newv_async(
        object_type: type[Any],
        n_parameters: int,
        parameters: GObject.Parameter,
        io_priority: int,
        cancellable: Cancellable | None = None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None = None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...

class AsyncInitableIface(_gi.Struct):
    """
    :Constructors:

    ::

        AsyncInitableIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def init_async(
        self,
    ) -> Callable[
        [
            AsyncInitable,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def init_finish(self) -> Callable[[AsyncInitable, AsyncResult], bool]: ...

class AsyncResult(GObject.GInterface, Protocol):
    """
    Interface GAsyncResult

    Signals from GObject:
      notify (GParam)
    """
    def get_source_object(self) -> GObject.Object | None: ...
    def get_user_data(self) -> int: ...
    def is_tagged(self, source_tag: int | Any | None = None) -> bool: ...
    def legacy_propagate_error(self) -> bool: ...

class AsyncResultIface(_gi.Struct):
    """
    :Constructors:

    ::

        AsyncResultIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_user_data(self) -> Callable[[AsyncResult], int]: ...
    @property
    def get_source_object(self) -> Callable[[AsyncResult], GObject.Object | None]: ...
    @property
    def is_tagged(self) -> Callable[[AsyncResult, Any | None], bool]: ...

class BufferedInputStream(FilterInputStream, Seekable):
    """
    :Constructors:

    ::

        BufferedInputStream(**properties)
        new(base_stream:Gio.InputStream) -> Gio.InputStream
        new_sized(base_stream:Gio.InputStream, size:int) -> Gio.InputStream

    Object GBufferedInputStream

    Properties from GBufferedInputStream:
      buffer-size -> guint: buffer-size

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(FilterInputStream.Props):
        buffer_size: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> FilterInputStream: ...
    @property
    def priv(self) -> BufferedInputStreamPrivate: ...
    def __init__(
        self,
        *,
        buffer_size: int = ...,
        base_stream: InputStream | None = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def do_fill(self, count: int, cancellable: Cancellable | None, /) -> int: ...
    def do_fill_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[BufferedInputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_fill_finish(self, result: AsyncResult, /) -> int: ...
    def fill(self, count: int, cancellable: Cancellable | None = None) -> int: ...
    @overload
    def fill_async(
        self, count: int, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[int]: ...
    @overload
    def fill_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[BufferedInputStream, Unpack[_DataTs]]
        | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def fill_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[BufferedInputStream] | None,
    ) -> None: ...
    def fill_finish(self, result: AsyncResult) -> int: ...
    def get_available(self) -> int: ...
    def get_buffer_size(self) -> int: ...
    @classmethod
    def new(cls, base_stream: InputStream) -> BufferedInputStream: ...
    @classmethod
    def new_sized(cls, base_stream: InputStream, size: int) -> BufferedInputStream: ...
    def peek(self, buffer: Sequence[int], offset: int) -> int: ...
    def peek_buffer(self) -> bytes: ...
    def read_byte(self, cancellable: Cancellable | None = None) -> int: ...
    def set_buffer_size(self, size: int) -> None: ...

class BufferedInputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        BufferedInputStreamClass()
    """
    @property
    def parent_class(self) -> FilterInputStreamClass: ...
    @property
    def fill(self) -> Callable[[BufferedInputStream, int, Cancellable | None], int]: ...
    @property
    def fill_async(
        self,
    ) -> Callable[
        [
            BufferedInputStream,
            int,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def fill_finish(self) -> Callable[[BufferedInputStream, AsyncResult], int]: ...

class BufferedInputStreamPrivate(_gi.Struct): ...

class BufferedOutputStream(FilterOutputStream, Seekable):
    """
    :Constructors:

    ::

        BufferedOutputStream(**properties)
        new(base_stream:Gio.OutputStream) -> Gio.OutputStream
        new_sized(base_stream:Gio.OutputStream, size:int) -> Gio.OutputStream

    Object GBufferedOutputStream

    Properties from GBufferedOutputStream:
      buffer-size -> guint: buffer-size
      auto-grow -> gboolean: auto-grow

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(FilterOutputStream.Props):
        auto_grow: bool
        buffer_size: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> FilterOutputStream: ...
    @property
    def priv(self) -> BufferedOutputStreamPrivate: ...
    def __init__(
        self,
        *,
        auto_grow: bool = ...,
        buffer_size: int = ...,
        base_stream: OutputStream | None = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_auto_grow(self) -> bool: ...
    def get_buffer_size(self) -> int: ...
    @classmethod
    def new(cls, base_stream: OutputStream) -> BufferedOutputStream: ...
    @classmethod
    def new_sized(
        cls, base_stream: OutputStream, size: int
    ) -> BufferedOutputStream: ...
    def set_auto_grow(self, auto_grow: bool) -> None: ...
    def set_buffer_size(self, size: int) -> None: ...

class BufferedOutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        BufferedOutputStreamClass()
    """
    @property
    def parent_class(self) -> FilterOutputStreamClass: ...

class BufferedOutputStreamPrivate(_gi.Struct): ...

class BytesIcon(GObject.Object, Icon, LoadableIcon):
    """
    :Constructors:

    ::

        BytesIcon(**properties)
        new(bytes:GLib.Bytes) -> Gio.BytesIcon

    Object GBytesIcon

    Properties from GBytesIcon:
      bytes -> GBytes: bytes

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def bytes(self) -> GLib.Bytes: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, bytes: GLib.Bytes | None = ...) -> None: ...
    def get_bytes(self) -> GLib.Bytes: ...
    @classmethod
    def new(cls, bytes: GLib.Bytes) -> BytesIcon: ...

class Cancellable(GObject.Object):
    """
    :Constructors:

    ::

        Cancellable(**properties)
        new() -> Gio.Cancellable

    Object GCancellable

    Signals from GCancellable:
      cancelled ()

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> CancellablePrivate: ...
    def cancel(self) -> None: ...
    def connect(self, callback: Callable[[], None], *data: Unpack[_DataTs]) -> int: ...
    def disconnect(self, handler_id: int) -> None: ...
    def do_cancelled(self) -> None: ...
    @staticmethod
    def get_current() -> Cancellable | None: ...
    def get_fd(self) -> int: ...
    def is_cancelled(self) -> bool: ...
    def make_pollfd(self, pollfd: GLib.PollFD) -> bool: ...
    @classmethod
    def new(cls) -> Cancellable: ...
    def pop_current(self) -> None: ...
    def push_current(self) -> None: ...
    def release_fd(self) -> None: ...
    def reset(self) -> None: ...
    def set_error_if_cancelled(self) -> bool: ...
    def source_new(self) -> GLib.Source: ...

class CancellableClass(_gi.Struct):
    """
    :Constructors:

    ::

        CancellableClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def cancelled(self) -> Callable[[Cancellable | None], None]: ...

class CancellablePrivate(_gi.Struct): ...

class CharsetConverter(GObject.Object, Converter, Initable):
    """
    :Constructors:

    ::

        CharsetConverter(**properties)
        new(to_charset:str, from_charset:str) -> Gio.CharsetConverter

    Object GCharsetConverter

    Properties from GCharsetConverter:
      from-charset -> gchararray: from-charset
      to-charset -> gchararray: to-charset
      use-fallback -> gboolean: use-fallback

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def from_charset(self) -> str | None: ...
        @property
        def to_charset(self) -> str | None: ...
        use_fallback: bool

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        from_charset: str | None = ...,
        to_charset: str | None = ...,
        use_fallback: bool = ...,
    ) -> None: ...
    def get_num_fallbacks(self) -> int: ...
    def get_use_fallback(self) -> bool: ...
    @classmethod
    def new(cls, to_charset: str, from_charset: str) -> CharsetConverter: ...
    def set_use_fallback(self, use_fallback: bool) -> None: ...

class CharsetConverterClass(_gi.Struct):
    """
    :Constructors:

    ::

        CharsetConverterClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class Converter(GObject.GInterface, Protocol):
    """
    Interface GConverter

    Signals from GObject:
      notify (GParam)
    """
    def convert(
        self,
        inbuf: Sequence[int],
        outbuf: Sequence[int],
        flags: _ConverterFlagsValueType,
    ) -> tuple[ConverterResult, int, int]: ...
    def convert_bytes(self, bytes: GLib.Bytes) -> GLib.Bytes: ...
    def reset(self) -> None: ...

class ConverterIface(_gi.Struct):
    """
    :Constructors:

    ::

        ConverterIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def convert(
        self,
    ) -> Callable[
        [
            Converter,
            Sequence[int] | None,
            int,
            Sequence[int],
            int,
            _ConverterFlagsValueType,
        ],
        tuple[ConverterResult, int, int],
    ]: ...
    @property
    def reset(self) -> Callable[[Converter], None]: ...

class ConverterInputStream(FilterInputStream, PollableInputStream):
    """
    :Constructors:

    ::

        ConverterInputStream(**properties)
        new(base_stream:Gio.InputStream, converter:Gio.Converter) -> Gio.InputStream

    Object GConverterInputStream

    Properties from GConverterInputStream:
      converter -> GConverter: converter

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(FilterInputStream.Props):
        @property
        def converter(self) -> Converter: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> FilterInputStream: ...
    @property
    def priv(self) -> ConverterInputStreamPrivate: ...
    def __init__(
        self,
        *,
        converter: Converter | None = ...,
        base_stream: InputStream | None = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_converter(self) -> Converter: ...
    @classmethod
    def new(
        cls, base_stream: InputStream, converter: Converter
    ) -> ConverterInputStream: ...

class ConverterInputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        ConverterInputStreamClass()
    """
    @property
    def parent_class(self) -> FilterInputStreamClass: ...

class ConverterInputStreamPrivate(_gi.Struct): ...

class ConverterOutputStream(FilterOutputStream, PollableOutputStream):
    """
    :Constructors:

    ::

        ConverterOutputStream(**properties)
        new(base_stream:Gio.OutputStream, converter:Gio.Converter) -> Gio.OutputStream

    Object GConverterOutputStream

    Properties from GConverterOutputStream:
      converter -> GConverter: converter

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(FilterOutputStream.Props):
        @property
        def converter(self) -> Converter: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> FilterOutputStream: ...
    @property
    def priv(self) -> ConverterOutputStreamPrivate: ...
    def __init__(
        self,
        *,
        converter: Converter | None = ...,
        base_stream: OutputStream | None = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_converter(self) -> Converter: ...
    @classmethod
    def new(
        cls, base_stream: OutputStream, converter: Converter
    ) -> ConverterOutputStream: ...

class ConverterOutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        ConverterOutputStreamClass()
    """
    @property
    def parent_class(self) -> FilterOutputStreamClass: ...

class ConverterOutputStreamPrivate(_gi.Struct): ...

class Credentials(GObject.Object):
    """
    :Constructors:

    ::

        Credentials(**properties)
        new() -> Gio.Credentials

    Object GCredentials

    Signals from GObject:
      notify (GParam)
    """
    def get_unix_pid(self) -> int: ...
    def get_unix_user(self) -> int: ...
    def is_same_user(self, other_credentials: Credentials) -> bool: ...
    @classmethod
    def new(cls) -> Credentials: ...
    def set_native(
        self, native_type: _CredentialsTypeValueType, native: int | Any | None
    ) -> None: ...
    def set_unix_user(self, uid: int) -> bool: ...
    def to_string(self) -> str: ...

class CredentialsClass(_gi.Struct): ...

class DBusActionGroup(GObject.Object, ActionGroup, RemoteActionGroup):
    """
    :Constructors:

    ::

        DBusActionGroup(**properties)

    Object GDBusActionGroup

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get(
        connection: DBusConnection, bus_name: str | None, object_path: str
    ) -> DBusActionGroup: ...

class DBusAnnotationInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusAnnotationInfo()
    """

    ref_count: int
    key: str
    value: str
    annotations: list[DBusAnnotationInfo]
    def __init__(
        self, *args, **kwargs
    ) -> None: ...  # FIXME: Override is missing typing annotation
    @staticmethod
    def lookup(
        annotations: Sequence[DBusAnnotationInfo] | None, name: str
    ) -> str | None: ...
    def ref(self) -> DBusAnnotationInfo: ...
    def unref(self) -> None: ...

class DBusArgInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusArgInfo()
    """

    ref_count: int
    name: str
    signature: str
    annotations: list[DBusAnnotationInfo]
    def __init__(
        self, *args, **kwargs
    ) -> None: ...  # FIXME: Override is missing typing annotation
    def ref(self) -> DBusArgInfo: ...
    def unref(self) -> None: ...

class DBusAuthObserver(GObject.Object):
    """
    :Constructors:

    ::

        DBusAuthObserver(**properties)
        new() -> Gio.DBusAuthObserver

    Object GDBusAuthObserver

    Signals from GDBusAuthObserver:
      authorize-authenticated-peer (GIOStream, GCredentials) -> gboolean
      allow-mechanism (gchararray) -> gboolean

    Signals from GObject:
      notify (GParam)
    """
    def allow_mechanism(self, mechanism: str) -> bool: ...
    def authorize_authenticated_peer(
        self, stream: IOStream, credentials: Credentials | None = None
    ) -> bool: ...
    @classmethod
    def new(cls) -> DBusAuthObserver: ...

class DBusConnection(GObject.Object, AsyncInitable, Initable):
    """
    :Constructors:

    ::

        DBusConnection(**properties)
        new_finish(res:Gio.AsyncResult) -> Gio.DBusConnection
        new_for_address_finish(res:Gio.AsyncResult) -> Gio.DBusConnection
        new_for_address_sync(address:str, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection
        new_sync(stream:Gio.IOStream, guid:str=None, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection

    Object GDBusConnection

    Signals from GDBusConnection:
      closed (gboolean, GError)

    Properties from GDBusConnection:
      stream -> GIOStream: stream
      address -> gchararray: address
      flags -> GDBusConnectionFlags: flags
      guid -> gchararray: guid
      unique-name -> gchararray: unique-name
      closed -> gboolean: closed
      exit-on-close -> gboolean: exit-on-close
      capabilities -> GDBusCapabilityFlags: capabilities
      authentication-observer -> GDBusAuthObserver: authentication-observer

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def capabilities(self) -> DBusCapabilityFlags: ...
        @property
        def closed(self) -> bool: ...
        exit_on_close: bool
        @property
        def flags(self) -> DBusConnectionFlags: ...
        @property
        def guid(self) -> str: ...
        @property
        def stream(self) -> IOStream: ...
        @property
        def unique_name(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        address: str | None = ...,
        authentication_observer: DBusAuthObserver | None = ...,
        exit_on_close: bool = ...,
        flags: _DBusConnectionFlagsValueType = ...,
        guid: str | None = ...,
        stream: IOStream | None = ...,
    ) -> None: ...
    def add_filter(
        self,
        filter_function: Callable[
            [DBusConnection, DBusMessage, bool, Unpack[_DataTs]], DBusMessage | None
        ],
        *user_data: Unpack[_DataTs],
    ) -> int: ...
    @overload
    def call(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[GLib.Variant]: ...
    @overload
    def call(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DBusConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def call(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DBusConnection] | None,
    ) -> None: ...
    def call_finish(self, res: AsyncResult) -> GLib.Variant: ...
    def call_sync(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
    ) -> GLib.Variant: ...
    @overload
    def call_with_unix_fd_list(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[GLib.Variant, UnixFDList | None]]: ...
    @overload
    def call_with_unix_fd_list(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DBusConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def call_with_unix_fd_list(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DBusConnection] | None,
    ) -> None: ...
    def call_with_unix_fd_list_finish(
        self, res: AsyncResult
    ) -> tuple[GLib.Variant, UnixFDList | None]: ...
    def call_with_unix_fd_list_sync(
        self,
        bus_name: str | None,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant | None,
        reply_type: GLib.VariantType | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None = None,
        cancellable: Cancellable | None = None,
    ) -> tuple[GLib.Variant, UnixFDList | None]: ...
    @overload
    def close(self, cancellable: Cancellable | None = None) -> _gi.Async[bool]: ...
    @overload
    def close(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DBusConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def close(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DBusConnection] | None,
    ) -> None: ...
    def close_finish(self, res: AsyncResult) -> bool: ...
    def close_sync(self, cancellable: Cancellable | None = None) -> bool: ...
    def emit_signal(
        self,
        destination_bus_name: str | None,
        object_path: str,
        interface_name: str,
        signal_name: str,
        parameters: GLib.Variant | None = None,
    ) -> bool: ...
    def export_action_group(
        self, object_path: str, action_group: ActionGroup
    ) -> int: ...
    def export_menu_model(self, object_path: str, menu: MenuModel) -> int: ...
    @overload
    def flush(self, cancellable: Cancellable | None = None) -> _gi.Async[bool]: ...
    @overload
    def flush(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DBusConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def flush(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DBusConnection] | None,
    ) -> None: ...
    def flush_finish(self, res: AsyncResult) -> bool: ...
    def flush_sync(self, cancellable: Cancellable | None = None) -> bool: ...
    def get_capabilities(self) -> DBusCapabilityFlags: ...
    def get_exit_on_close(self) -> bool: ...
    def get_flags(self) -> DBusConnectionFlags: ...
    def get_guid(self) -> str: ...
    def get_last_serial(self) -> int: ...
    def get_peer_credentials(self) -> Credentials | None: ...
    def get_stream(self) -> IOStream: ...
    def get_unique_name(self) -> str | None: ...
    def is_closed(self) -> bool: ...
    @overload
    @staticmethod
    def new(
        stream: IOStream,
        guid: str | None,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[DBusConnection]: ...
    @overload
    @staticmethod
    def new(
        stream: IOStream,
        guid: str | None,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new(
        stream: IOStream,
        guid: str | None,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: AsyncResult) -> DBusConnection: ...
    @overload
    @staticmethod
    def new_for_address(
        address: str,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[DBusConnection]: ...
    @overload
    @staticmethod
    def new_for_address(
        address: str,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new_for_address(
        address: str,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @classmethod
    def new_for_address_finish(cls, res: AsyncResult) -> DBusConnection: ...
    @classmethod
    def new_for_address_sync(
        cls,
        address: str,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
    ) -> DBusConnection: ...
    @classmethod
    def new_sync(
        cls,
        stream: IOStream,
        guid: str | None,
        flags: _DBusConnectionFlagsValueType,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
    ) -> DBusConnection: ...
    # override
    def register_object(
        self,
        object_path: str,
        interface_info: DBusInterfaceInfo,
        method_call_closure: Callable[
            [DBusConnection, str, str, str, str, GLib.Variant, DBusMethodInvocation],
            None,
        ]
        | None = None,
        get_property_closure: Callable[
            [DBusConnection, str, str, str, str], GLib.Variant
        ]
        | None = None,
        set_property_closure: Callable[
            [DBusConnection, str, str, str, str, GLib.Variant], bool
        ]
        | None = None,
    ) -> int: ...
    # override
    def register_object_with_closures2(
        self,
        object_path: str,
        interface_info: DBusInterfaceInfo,
        method_call_closure: Callable[
            [DBusConnection, str, str, str, str, GLib.Variant, DBusMethodInvocation],
            None,
        ]
        | None = None,
        get_property_closure: Callable[
            [DBusConnection, str, str, str, str], GLib.Variant
        ]
        | None = None,
        set_property_closure: Callable[
            [DBusConnection, str, str, str, str, GLib.Variant], bool
        ]
        | None = None,
    ) -> int: ...
    def register_subtree(
        self,
        object_path: str,
        vtable: DBusSubtreeVTable,
        flags: _DBusSubtreeFlagsValueType,
        user_data: int | Any | None,
        user_data_free_func: Callable[[Any | None], None],
    ) -> int: ...
    def remove_filter(self, filter_id: int) -> None: ...
    def send_message(
        self, message: DBusMessage, flags: _DBusSendMessageFlagsValueType
    ) -> tuple[bool, int]: ...
    def send_message_with_reply(
        self,
        message: DBusMessage,
        flags: _DBusSendMessageFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
        callback: _AsyncReadyVarArgsCallback[DBusConnection, Unpack[_DataTs]]
        | None = None,
        *user_data: Unpack[_DataTs],
    ) -> int: ...
    def send_message_with_reply_finish(self, res: AsyncResult) -> DBusMessage: ...
    def send_message_with_reply_sync(
        self,
        message: DBusMessage,
        flags: _DBusSendMessageFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
    ) -> tuple[DBusMessage, int]: ...
    def set_exit_on_close(self, exit_on_close: bool) -> None: ...
    def signal_subscribe(
        self,
        sender: str | None,
        interface_name: str | None,
        member: str | None,
        object_path: str | None,
        arg0: str | None,
        flags: _DBusSignalFlagsValueType,
        callback: Callable[
            [DBusConnection, str | None, str, str, str, GLib.Variant, Unpack[_DataTs]],
            None,
        ],
        *user_data: Unpack[_DataTs],
    ) -> int: ...
    def signal_unsubscribe(self, subscription_id: int) -> None: ...
    def start_message_processing(self) -> None: ...
    def unexport_action_group(self, export_id: int) -> None: ...
    def unexport_menu_model(self, export_id: int) -> None: ...
    def unregister_object(self, registration_id: int) -> bool: ...
    def unregister_subtree(self, registration_id: int) -> bool: ...

class DBusErrorEntry(_gi.Struct):
    """
    :Constructors:

    ::

        DBusErrorEntry()
    """

    error_code: int
    dbus_error_name: str

class DBusInterface(GObject.GInterface, Protocol):
    """
    Interface GDBusInterface

    Signals from GObject:
      notify (GParam)
    """
    def get_info(self) -> DBusInterfaceInfo: ...
    def get_object(self) -> DBusObject | None: ...
    def set_object(self, object: DBusObject | None = None) -> None: ...

class DBusInterfaceIface(_gi.Struct):
    """
    :Constructors:

    ::

        DBusInterfaceIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_info(self) -> Callable[[DBusInterface], DBusInterfaceInfo]: ...
    @property
    def get_object(self) -> Callable[[DBusInterface], DBusObject | None]: ...
    @property
    def set_object(self) -> Callable[[DBusInterface, DBusObject | None], None]: ...
    @property
    def dup_object(self) -> Callable[[DBusInterface], DBusObject | None]: ...

class DBusInterfaceInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusInterfaceInfo()
    """

    ref_count: int
    name: str
    methods: list[DBusMethodInfo]
    signals: list[DBusSignalInfo]
    properties: list[DBusPropertyInfo]
    annotations: list[DBusAnnotationInfo]
    def __init__(
        self, *args, **kwargs
    ) -> None: ...  # FIXME: Override is missing typing annotation
    def cache_build(self) -> None: ...
    def cache_release(self) -> None: ...
    def generate_xml(self, indent: int, string_builder: GLib.String) -> None: ...
    def lookup_method(self, name: str) -> DBusMethodInfo | None: ...
    def lookup_property(self, name: str) -> DBusPropertyInfo | None: ...
    def lookup_signal(self, name: str) -> DBusSignalInfo | None: ...
    def ref(self) -> DBusInterfaceInfo: ...
    def unref(self) -> None: ...

class DBusInterfaceSkeleton(GObject.Object, DBusInterface):
    """
    :Constructors:

    ::

        DBusInterfaceSkeleton(**properties)

    Object GDBusInterfaceSkeleton

    Signals from GDBusInterfaceSkeleton:
      g-authorize-method (GDBusMethodInvocation) -> gboolean

    Properties from GDBusInterfaceSkeleton:
      g-flags -> GDBusInterfaceSkeletonFlags: g-flags

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def g_flags(self) -> DBusInterfaceSkeletonFlags: ...
        @g_flags.setter
        def g_flags(self, value: _DBusInterfaceSkeletonFlagsValueType) -> None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> DBusInterfaceSkeletonPrivate: ...
    def __init__(
        self, *, g_flags: _DBusInterfaceSkeletonFlagsValueType = ...
    ) -> None: ...
    def do_flush(self) -> None: ...
    def do_g_authorize_method(self, invocation: DBusMethodInvocation, /) -> bool: ...
    def do_get_info(self) -> DBusInterfaceInfo: ...
    def do_get_properties(self) -> GLib.Variant: ...
    def do_get_vtable(self) -> DBusInterfaceVTable: ...
    def export(self, connection: DBusConnection, object_path: str) -> bool: ...
    def flush(self) -> None: ...
    def get_connection(self) -> DBusConnection | None: ...
    def get_connections(self) -> list[DBusConnection]: ...
    def get_flags(self) -> DBusInterfaceSkeletonFlags: ...
    def get_info(self) -> DBusInterfaceInfo: ...
    def get_object_path(self) -> str | None: ...
    def get_properties(self) -> GLib.Variant: ...
    def get_vtable(self) -> DBusInterfaceVTable: ...
    def has_connection(self, connection: DBusConnection) -> bool: ...
    def set_flags(self, flags: _DBusInterfaceSkeletonFlagsValueType) -> None: ...
    def unexport(self) -> None: ...
    def unexport_from_connection(self, connection: DBusConnection) -> None: ...

class DBusInterfaceSkeletonClass(_gi.Struct):
    """
    :Constructors:

    ::

        DBusInterfaceSkeletonClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_info(self) -> Callable[[DBusInterfaceSkeleton], DBusInterfaceInfo]: ...
    @property
    def get_vtable(self) -> Callable[[DBusInterfaceSkeleton], DBusInterfaceVTable]: ...
    @property
    def get_properties(self) -> Callable[[DBusInterfaceSkeleton], GLib.Variant]: ...
    @property
    def flush(self) -> Callable[[DBusInterfaceSkeleton], None]: ...
    @property
    def vfunc_padding(self) -> list[int]: ...
    @property
    def g_authorize_method(
        self,
    ) -> Callable[[DBusInterfaceSkeleton, DBusMethodInvocation], bool]: ...
    @property
    def signal_padding(self) -> list[int]: ...

class DBusInterfaceSkeletonPrivate(_gi.Struct): ...

class DBusInterfaceVTable(_gi.Struct):
    """
    :Constructors:

    ::

        DBusInterfaceVTable()
    """

    method_call: Callable[
        [
            DBusConnection,
            str | None,
            str,
            str | None,
            str,
            GLib.Variant,
            DBusMethodInvocation,
            Any | None,
        ],
        None,
    ]
    get_property: Callable[
        [DBusConnection, str | None, str, str, str, GLib.Error, Any | None],
        GLib.Variant,
    ]
    set_property: Callable[
        [
            DBusConnection,
            str | None,
            str,
            str,
            str,
            GLib.Variant,
            GLib.Error,
            Any | None,
        ],
        bool,
    ]
    @property
    def padding(self) -> list[int]: ...

class DBusMenuModel(MenuModel):
    """
    :Constructors:

    ::

        DBusMenuModel(**properties)

    Object GDBusMenuModel

    Signals from GMenuModel:
      items-changed (gint, gint, gint)

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get(
        connection: DBusConnection, bus_name: str | None, object_path: str
    ) -> DBusMenuModel: ...

class DBusMessage(GObject.Object):
    """
    :Constructors:

    ::

        DBusMessage(**properties)
        new() -> Gio.DBusMessage
        new_from_blob(blob:list, capabilities:Gio.DBusCapabilityFlags) -> Gio.DBusMessage
        new_method_call(name:str=None, path:str, interface_:str=None, method:str) -> Gio.DBusMessage
        new_signal(path:str, interface_:str, signal:str) -> Gio.DBusMessage

    Object GDBusMessage

    Properties from GDBusMessage:
      locked -> gboolean: locked

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def locked(self) -> bool: ...

    @property
    def props(self) -> Props: ...
    @staticmethod
    def bytes_needed(blob: Sequence[int]) -> int: ...
    def copy(self) -> DBusMessage: ...
    def get_arg0(self) -> str | None: ...
    def get_arg0_path(self) -> str | None: ...
    def get_body(self) -> GLib.Variant | None: ...
    def get_byte_order(self) -> DBusMessageByteOrder: ...
    def get_destination(self) -> str | None: ...
    def get_error_name(self) -> str | None: ...
    def get_flags(self) -> DBusMessageFlags: ...
    def get_header(
        self, header_field: _DBusMessageHeaderFieldValueType
    ) -> GLib.Variant | None: ...
    def get_header_fields(self) -> bytes: ...
    def get_interface(self) -> str | None: ...
    def get_locked(self) -> bool: ...
    def get_member(self) -> str | None: ...
    def get_message_type(self) -> DBusMessageType: ...
    def get_num_unix_fds(self) -> int: ...
    def get_path(self) -> str | None: ...
    def get_reply_serial(self) -> int: ...
    def get_sender(self) -> str | None: ...
    def get_serial(self) -> int: ...
    def get_signature(self) -> str: ...
    def get_unix_fd_list(self) -> UnixFDList | None: ...
    def lock(self) -> None: ...
    @classmethod
    def new(cls) -> DBusMessage: ...
    @classmethod
    def new_from_blob(
        cls, blob: Sequence[int], capabilities: _DBusCapabilityFlagsValueType
    ) -> DBusMessage: ...
    @classmethod
    def new_method_call(
        cls, name: str | None, path: str, interface_: str | None, method: str
    ) -> DBusMessage: ...
    def new_method_error_literal(
        self, error_name: str, error_message: str
    ) -> DBusMessage: ...
    def new_method_reply(self) -> DBusMessage: ...
    @classmethod
    def new_signal(cls, path: str, interface_: str, signal: str) -> DBusMessage: ...
    def print_(self, indent: int) -> str: ...
    def set_body(self, body: GLib.Variant) -> None: ...
    def set_byte_order(self, byte_order: _DBusMessageByteOrderValueType) -> None: ...
    def set_destination(self, value: str | None = None) -> None: ...
    def set_error_name(self, value: str) -> None: ...
    def set_flags(self, flags: _DBusMessageFlagsValueType) -> None: ...
    def set_header(
        self,
        header_field: _DBusMessageHeaderFieldValueType,
        value: GLib.Variant | None = None,
    ) -> None: ...
    def set_interface(self, value: str | None = None) -> None: ...
    def set_member(self, value: str | None = None) -> None: ...
    def set_message_type(self, type: _DBusMessageTypeValueType) -> None: ...
    def set_num_unix_fds(self, value: int) -> None: ...
    def set_path(self, value: str | None = None) -> None: ...
    def set_reply_serial(self, value: int) -> None: ...
    def set_sender(self, value: str | None = None) -> None: ...
    def set_serial(self, serial: int) -> None: ...
    def set_signature(self, value: str | None = None) -> None: ...
    def set_unix_fd_list(self, fd_list: UnixFDList | None = None) -> None: ...
    def to_blob(self, capabilities: _DBusCapabilityFlagsValueType) -> bytes: ...
    def to_gerror(self) -> bool: ...

class DBusMethodInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusMethodInfo()
    """

    ref_count: int
    name: str
    in_args: list[DBusArgInfo]
    out_args: list[DBusArgInfo]
    annotations: list[DBusAnnotationInfo]
    def __init__(
        self, *args, **kwargs
    ) -> None: ...  # FIXME: Override is missing typing annotation
    def ref(self) -> DBusMethodInfo: ...
    def unref(self) -> None: ...

class DBusMethodInvocation(GObject.Object):
    """
    :Constructors:

    ::

        DBusMethodInvocation(**properties)

    Object GDBusMethodInvocation

    Signals from GObject:
      notify (GParam)
    """
    def get_connection(self) -> DBusConnection: ...
    def get_interface_name(self) -> str | None: ...
    def get_message(self) -> DBusMessage: ...
    def get_method_info(self) -> DBusMethodInfo | None: ...
    def get_method_name(self) -> str: ...
    def get_object_path(self) -> str: ...
    def get_parameters(self) -> GLib.Variant: ...
    def get_property_info(self) -> DBusPropertyInfo | None: ...
    def get_sender(self) -> str | None: ...
    def return_dbus_error(self, error_name: str, error_message: str) -> None: ...
    def return_error_literal(self, domain: int, code: int, message: str) -> None: ...
    def return_gerror(self, error: GLib.Error) -> None: ...
    def return_value(self, parameters: GLib.Variant | None = None) -> None: ...
    def return_value_with_unix_fd_list(
        self, parameters: GLib.Variant | None = None, fd_list: UnixFDList | None = None
    ) -> None: ...

class DBusNodeInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusNodeInfo()
        new_for_xml(xml_data:str) -> Gio.DBusNodeInfo
    """

    ref_count: int
    path: str
    interfaces: list[DBusInterfaceInfo]
    nodes: list[DBusNodeInfo]
    annotations: list[DBusAnnotationInfo]
    def __init__(
        self, *args, **kwargs
    ) -> None: ...  # FIXME: Override is missing typing annotation
    def generate_xml(self, indent: int, string_builder: GLib.String) -> None: ...
    def lookup_interface(self, name: str) -> DBusInterfaceInfo | None: ...
    @classmethod
    def new_for_xml(cls, xml_data: str) -> DBusNodeInfo: ...
    def ref(self) -> DBusNodeInfo: ...
    def unref(self) -> None: ...

class DBusObject(GObject.GInterface, Protocol):
    """
    Interface GDBusObject

    Signals from GObject:
      notify (GParam)
    """
    def get_interface(self, interface_name: str) -> DBusInterface | None: ...
    def get_interfaces(self) -> list[DBusInterface]: ...
    def get_object_path(self) -> str: ...

class DBusObjectIface(_gi.Struct):
    """
    :Constructors:

    ::

        DBusObjectIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_object_path(self) -> Callable[[DBusObject], str]: ...
    @property
    def get_interfaces(self) -> Callable[[DBusObject], list[DBusInterface]]: ...
    @property
    def get_interface(self) -> Callable[[DBusObject, str], DBusInterface | None]: ...
    @property
    def interface_added(self) -> Callable[[DBusObject, DBusInterface], None]: ...
    @property
    def interface_removed(self) -> Callable[[DBusObject, DBusInterface], None]: ...

class DBusObjectManager(GObject.GInterface, Protocol):
    """
    Interface GDBusObjectManager

    Signals from GObject:
      notify (GParam)
    """
    def get_interface(
        self, object_path: str, interface_name: str
    ) -> DBusInterface | None: ...
    def get_object(self, object_path: str) -> DBusObject | None: ...
    def get_object_path(self) -> str: ...
    def get_objects(self) -> list[DBusObject]: ...

class DBusObjectManagerClient(
    GObject.Object, AsyncInitable, DBusObjectManager, Initable
):
    """
    :Constructors:

    ::

        DBusObjectManagerClient(**properties)
        new_finish(res:Gio.AsyncResult) -> Gio.DBusObjectManagerClient
        new_for_bus_finish(res:Gio.AsyncResult) -> Gio.DBusObjectManagerClient
        new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, get_proxy_type_func:Gio.DBusProxyTypeFunc=None, get_proxy_type_user_data=None, cancellable:Gio.Cancellable=None) -> Gio.DBusObjectManagerClient
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, name:str=None, object_path:str, get_proxy_type_func:Gio.DBusProxyTypeFunc=None, get_proxy_type_user_data=None, cancellable:Gio.Cancellable=None) -> Gio.DBusObjectManagerClient

    Object GDBusObjectManagerClient

    Signals from GDBusObjectManagerClient:
      interface-proxy-signal (GDBusObjectProxy, GDBusProxy, gchararray, gchararray, GVariant)
      interface-proxy-properties-changed (GDBusObjectProxy, GDBusProxy, GVariant, GStrv)

    Properties from GDBusObjectManagerClient:
      bus-type -> GBusType: bus-type
      connection -> GDBusConnection: connection
      flags -> GDBusObjectManagerClientFlags: flags
      object-path -> gchararray: object-path
      name -> gchararray: name
      name-owner -> gchararray: name-owner
      get-proxy-type-func -> gpointer: get-proxy-type-func
      get-proxy-type-user-data -> gpointer: get-proxy-type-user-data
      get-proxy-type-destroy-notify -> gpointer: get-proxy-type-destroy-notify

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def connection(self) -> DBusConnection: ...
        @property
        def flags(self) -> DBusObjectManagerClientFlags: ...
        @property
        def get_proxy_type_destroy_notify(self) -> int: ...
        @property
        def get_proxy_type_func(self) -> int: ...
        @property
        def get_proxy_type_user_data(self) -> int: ...
        @property
        def name(self) -> str: ...
        @property
        def name_owner(self) -> str | None: ...
        @property
        def object_path(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> DBusObjectManagerClientPrivate: ...
    def __init__(
        self,
        *,
        bus_type: _BusTypeValueType = ...,
        connection: DBusConnection | None = ...,
        flags: _DBusObjectManagerClientFlagsValueType = ...,
        get_proxy_type_destroy_notify: int | Any | None = ...,
        get_proxy_type_func: int | Any | None = ...,
        get_proxy_type_user_data: int | Any | None = ...,
        name: str | None = ...,
        object_path: str | None = ...,
    ) -> None: ...
    def do_interface_proxy_properties_changed(
        self,
        object_proxy: DBusObjectProxy,
        interface_proxy: DBusProxy,
        changed_properties: GLib.Variant,
        invalidated_properties: str,
        /,
    ) -> None: ...
    def do_interface_proxy_signal(
        self,
        object_proxy: DBusObjectProxy,
        interface_proxy: DBusProxy,
        sender_name: str,
        signal_name: str,
        parameters: GLib.Variant,
        /,
    ) -> None: ...
    def get_connection(self) -> DBusConnection: ...
    def get_flags(self) -> DBusObjectManagerClientFlags: ...
    def get_name(self) -> str: ...
    def get_name_owner(self) -> str | None: ...
    @overload
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None = None,
        get_proxy_type_user_data: Any | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[DBusObjectManagerClient]: ...
    @overload
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None,
        get_proxy_type_user_data: Any | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None = None,
        get_proxy_type_user_data: Any | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: AsyncResult) -> DBusObjectManagerClient: ...
    @overload
    @staticmethod
    def new_for_bus(
        bus_type: _BusTypeValueType,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None = None,
        get_proxy_type_user_data: Any | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[DBusObjectManagerClient]: ...
    @overload
    @staticmethod
    def new_for_bus(
        bus_type: _BusTypeValueType,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None,
        get_proxy_type_user_data: Any | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new_for_bus(
        bus_type: _BusTypeValueType,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None = None,
        get_proxy_type_user_data: Any | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: AsyncResult) -> DBusObjectManagerClient: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: _BusTypeValueType,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None = None,
        get_proxy_type_user_data: Any | None = None,
        cancellable: Cancellable | None = None,
    ) -> DBusObjectManagerClient: ...
    @classmethod
    def new_sync(
        cls,
        connection: DBusConnection,
        flags: _DBusObjectManagerClientFlagsValueType,
        name: str | None,
        object_path: str,
        get_proxy_type_func: Callable[
            [DBusObjectManagerClient, str, str | None, Any | None], type[Any]
        ]
        | None = None,
        get_proxy_type_user_data: Any | None = None,
        cancellable: Cancellable | None = None,
    ) -> DBusObjectManagerClient: ...

class DBusObjectManagerClientClass(_gi.Struct):
    """
    :Constructors:

    ::

        DBusObjectManagerClientClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def interface_proxy_signal(
        self,
    ) -> Callable[
        [DBusObjectManagerClient, DBusObjectProxy, DBusProxy, str, str, GLib.Variant],
        None,
    ]: ...
    @property
    def interface_proxy_properties_changed(
        self,
    ) -> Callable[
        [DBusObjectManagerClient, DBusObjectProxy, DBusProxy, GLib.Variant, str], None
    ]: ...
    @property
    def padding(self) -> list[int]: ...

class DBusObjectManagerClientPrivate(_gi.Struct): ...

class DBusObjectManagerIface(_gi.Struct):
    """
    :Constructors:

    ::

        DBusObjectManagerIface()
    """
    @property
    def parent_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_object_path(self) -> Callable[[DBusObjectManager], str]: ...
    @property
    def get_objects(self) -> Callable[[DBusObjectManager], list[DBusObject]]: ...
    @property
    def get_object(self) -> Callable[[DBusObjectManager, str], DBusObject | None]: ...
    @property
    def get_interface(
        self,
    ) -> Callable[[DBusObjectManager, str, str], DBusInterface | None]: ...
    @property
    def object_added(self) -> Callable[[DBusObjectManager, DBusObject], None]: ...
    @property
    def object_removed(self) -> Callable[[DBusObjectManager, DBusObject], None]: ...
    @property
    def interface_added(
        self,
    ) -> Callable[[DBusObjectManager, DBusObject, DBusInterface], None]: ...
    @property
    def interface_removed(
        self,
    ) -> Callable[[DBusObjectManager, DBusObject, DBusInterface], None]: ...

class DBusObjectManagerServer(GObject.Object, DBusObjectManager):
    """
    :Constructors:

    ::

        DBusObjectManagerServer(**properties)
        new(object_path:str) -> Gio.DBusObjectManagerServer

    Object GDBusObjectManagerServer

    Properties from GDBusObjectManagerServer:
      connection -> GDBusConnection: connection
      object-path -> gchararray: object-path

    Signals from GDBusObjectManager:
      object-added (GDBusObject)
      object-removed (GDBusObject)
      interface-added (GDBusObject, GDBusInterface)
      interface-removed (GDBusObject, GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        connection: DBusConnection | None
        @property
        def object_path(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> DBusObjectManagerServerPrivate: ...
    def __init__(
        self, *, connection: DBusConnection | None = ..., object_path: str | None = ...
    ) -> None: ...
    def export(self, object: DBusObjectSkeleton) -> None: ...
    def export_uniquely(self, object: DBusObjectSkeleton) -> None: ...
    def get_connection(self) -> DBusConnection | None: ...
    def is_exported(self, object: DBusObjectSkeleton) -> bool: ...
    @classmethod
    def new(cls, object_path: str) -> DBusObjectManagerServer: ...
    def set_connection(self, connection: DBusConnection | None = None) -> None: ...
    def unexport(self, object_path: str) -> bool: ...

class DBusObjectManagerServerClass(_gi.Struct):
    """
    :Constructors:

    ::

        DBusObjectManagerServerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[int]: ...

class DBusObjectManagerServerPrivate(_gi.Struct): ...

class DBusObjectProxy(GObject.Object, DBusObject):
    """
    :Constructors:

    ::

        DBusObjectProxy(**properties)
        new(connection:Gio.DBusConnection, object_path:str) -> Gio.DBusObjectProxy

    Object GDBusObjectProxy

    Properties from GDBusObjectProxy:
      g-object-path -> gchararray: g-object-path
      g-connection -> GDBusConnection: g-connection

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def g_connection(self) -> DBusConnection | None: ...
        @property
        def g_object_path(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> DBusObjectProxyPrivate: ...
    def __init__(
        self,
        *,
        g_connection: DBusConnection | None = ...,
        g_object_path: str | None = ...,
    ) -> None: ...
    def get_connection(self) -> DBusConnection: ...
    @classmethod
    def new(cls, connection: DBusConnection, object_path: str) -> DBusObjectProxy: ...

class DBusObjectProxyClass(_gi.Struct):
    """
    :Constructors:

    ::

        DBusObjectProxyClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[int]: ...

class DBusObjectProxyPrivate(_gi.Struct): ...

class DBusObjectSkeleton(GObject.Object, DBusObject):
    """
    :Constructors:

    ::

        DBusObjectSkeleton(**properties)
        new(object_path:str) -> Gio.DBusObjectSkeleton

    Object GDBusObjectSkeleton

    Signals from GDBusObjectSkeleton:
      authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean

    Properties from GDBusObjectSkeleton:
      g-object-path -> gchararray: g-object-path

    Signals from GDBusObject:
      interface-added (GDBusInterface)
      interface-removed (GDBusInterface)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        g_object_path: str | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> DBusObjectSkeletonPrivate: ...
    def __init__(self, *, g_object_path: str | None = ...) -> None: ...
    def add_interface(self, interface_: DBusInterfaceSkeleton) -> None: ...
    def do_authorize_method(
        self, interface_: DBusInterfaceSkeleton, invocation: DBusMethodInvocation, /
    ) -> bool: ...
    def flush(self) -> None: ...
    @classmethod
    def new(cls, object_path: str) -> DBusObjectSkeleton: ...
    def remove_interface(self, interface_: DBusInterfaceSkeleton) -> None: ...
    def remove_interface_by_name(self, interface_name: str) -> None: ...
    def set_object_path(self, object_path: str) -> None: ...

class DBusObjectSkeletonClass(_gi.Struct):
    """
    :Constructors:

    ::

        DBusObjectSkeletonClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def authorize_method(
        self,
    ) -> Callable[
        [DBusObjectSkeleton, DBusInterfaceSkeleton, DBusMethodInvocation], bool
    ]: ...
    @property
    def padding(self) -> list[int]: ...

class DBusObjectSkeletonPrivate(_gi.Struct): ...

class DBusPropertyInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusPropertyInfo()
    """

    ref_count: int
    name: str
    signature: str
    flags: DBusPropertyInfoFlags
    annotations: list[DBusAnnotationInfo]
    def ref(self) -> DBusPropertyInfo: ...
    def unref(self) -> None: ...

class DBusProxy(GObject.Object, AsyncInitable, DBusInterface, Initable):
    """
    Provide comfortable and pythonic method calls.

    This marshalls the method arguments into a GVariant, invokes the
    call_sync() method on the DBusProxy object, and unmarshalls the result
    GVariant back into a Python tuple.

    The first argument always needs to be the D-Bus signature tuple of the
    method call. Example:

      proxy = Gio.DBusProxy.new_sync(...)
      result = proxy.MyMethod('(is)', 42, 'hello')

    The exception are methods which take no arguments, like
    proxy.MyMethod('()'). For these you can omit the signature and just write
    proxy.MyMethod().

    Optional keyword arguments:

    - timeout: timeout for the call in milliseconds (default to D-Bus timeout)

    - flags: Combination of Gio.DBusCallFlags.*

    - result_handler: Do an asynchronous method call and invoke
         result_handler(proxy_object, result, user_data) when it finishes.

    - error_handler: If the asynchronous call raises an exception,
      error_handler(proxy_object, exception, user_data) is called when it
      finishes. If error_handler is not given, result_handler is called with
      the exception object as result instead.

    - user_data: Optional user data to pass to result_handler for
      asynchronous calls.

    Example for asynchronous calls:

      def mymethod_done(proxy, result, user_data):
          if isinstance(result, Exception):
              # handle error
          else:
              # do something with result

      proxy.MyMethod('(is)', 42, 'hello',
          result_handler=mymethod_done, user_data='data')

    Object GDBusProxy

    Provide comfortable and pythonic method calls.

    This marshalls the method arguments into a GVariant, invokes the
    call_sync() method on the DBusProxy object, and unmarshalls the result
    GVariant back into a Python tuple.

    The first argument always needs to be the D-Bus signature tuple of the
    method call. Example:

      proxy = Gio.DBusProxy.new_sync(...)
      result = proxy.MyMethod('(is)', 42, 'hello')

    The exception are methods which take no arguments, like
    proxy.MyMethod('()'). For these you can omit the signature and just write
    proxy.MyMethod().

    Optional keyword arguments:

    - timeout: timeout for the call in milliseconds (default to D-Bus timeout)

    - flags: Combination of Gio.DBusCallFlags.*

    - result_handler: Do an asynchronous method call and invoke
         result_handler(proxy_object, result, user_data) when it finishes.

    - error_handler: If the asynchronous call raises an exception,
      error_handler(proxy_object, exception, user_data) is called when it
      finishes. If error_handler is not given, result_handler is called with
      the exception object as result instead.

    - user_data: Optional user data to pass to result_handler for
      asynchronous calls.

    Example for asynchronous calls:

      def mymethod_done(proxy, result, user_data):
          if isinstance(result, Exception):
              # handle error
          else:
              # do something with result

      proxy.MyMethod('(is)', 42, 'hello',
          result_handler=mymethod_done, user_data='data')


    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def g_connection(self) -> DBusConnection | None: ...
        g_default_timeout: int
        @property
        def g_flags(self) -> DBusProxyFlags: ...
        g_interface_info: DBusInterfaceInfo | None
        @property
        def g_interface_name(self) -> str | None: ...
        @property
        def g_name(self) -> str | None: ...
        @property
        def g_name_owner(self) -> str | None: ...
        @property
        def g_object_path(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> DBusProxyPrivate: ...
    def __init__(
        self,
        *,
        g_bus_type: _BusTypeValueType = ...,
        g_connection: DBusConnection | None = ...,
        g_default_timeout: int = ...,
        g_flags: _DBusProxyFlagsValueType = ...,
        g_interface_info: DBusInterfaceInfo | None = ...,
        g_interface_name: str | None = ...,
        g_name: str | None = ...,
        g_object_path: str | None = ...,
    ) -> None: ...
    @overload
    def call(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[GLib.Variant]: ...
    @overload
    def call(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DBusProxy, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def call(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DBusProxy] | None,
    ) -> None: ...
    def call_finish(self, res: AsyncResult) -> GLib.Variant: ...
    def call_sync(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        cancellable: Cancellable | None = None,
    ) -> GLib.Variant: ...
    @overload
    def call_with_unix_fd_list(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[GLib.Variant, UnixFDList | None]]: ...
    @overload
    def call_with_unix_fd_list(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DBusProxy, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def call_with_unix_fd_list(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DBusProxy] | None,
    ) -> None: ...
    def call_with_unix_fd_list_finish(
        self, res: AsyncResult
    ) -> tuple[GLib.Variant, UnixFDList | None]: ...
    def call_with_unix_fd_list_sync(
        self,
        method_name: str,
        parameters: GLib.Variant | None,
        flags: _DBusCallFlagsValueType,
        timeout_msec: int,
        fd_list: UnixFDList | None = None,
        cancellable: Cancellable | None = None,
    ) -> tuple[GLib.Variant, UnixFDList | None]: ...
    def do_g_properties_changed(
        self, changed_properties: GLib.Variant, invalidated_properties: str, /
    ) -> None: ...
    def do_g_signal(
        self, sender_name: str, signal_name: str, parameters: GLib.Variant, /
    ) -> None: ...
    def get_cached_property(self, property_name: str) -> GLib.Variant | None: ...
    def get_cached_property_names(self) -> list[str]: ...
    def get_connection(self) -> DBusConnection: ...
    def get_default_timeout(self) -> int: ...
    def get_flags(self) -> DBusProxyFlags: ...
    def get_interface_info(self) -> DBusInterfaceInfo | None: ...
    def get_interface_name(self) -> str: ...
    def get_name(self) -> str | None: ...
    def get_name_owner(self) -> str | None: ...
    def get_object_path(self) -> str: ...
    @overload
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str | None,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[DBusProxy]: ...
    @overload
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str | None,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new(
        connection: DBusConnection,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str | None,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @classmethod
    def new_finish(cls, res: AsyncResult) -> DBusProxy: ...
    @overload
    @staticmethod
    def new_for_bus(
        bus_type: _BusTypeValueType,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[DBusProxy]: ...
    @overload
    @staticmethod
    def new_for_bus(
        bus_type: _BusTypeValueType,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new_for_bus(
        bus_type: _BusTypeValueType,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @classmethod
    def new_for_bus_finish(cls, res: AsyncResult) -> DBusProxy: ...
    @classmethod
    def new_for_bus_sync(
        cls,
        bus_type: _BusTypeValueType,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None = None,
    ) -> DBusProxy: ...
    @classmethod
    def new_sync(
        cls,
        connection: DBusConnection,
        flags: _DBusProxyFlagsValueType,
        info: DBusInterfaceInfo | None,
        name: str | None,
        object_path: str,
        interface_name: str,
        cancellable: Cancellable | None = None,
    ) -> DBusProxy: ...
    def set_cached_property(
        self, property_name: str, value: GLib.Variant | None = None
    ) -> None: ...
    def set_default_timeout(self, timeout_msec: int) -> None: ...
    def set_interface_info(self, info: DBusInterfaceInfo | None = None) -> None: ...

class DBusProxyClass(_gi.Struct):
    """
    :Constructors:

    ::

        DBusProxyClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def g_properties_changed(
        self,
    ) -> Callable[[DBusProxy, GLib.Variant, str], None]: ...
    @property
    def g_signal(self) -> Callable[[DBusProxy, str, str, GLib.Variant], None]: ...
    @property
    def padding(self) -> list[int]: ...

class DBusProxyPrivate(_gi.Struct): ...

class DBusServer(GObject.Object, Initable):
    """
    :Constructors:

    ::

        DBusServer(**properties)
        new_sync(address:str, flags:Gio.DBusServerFlags, guid:str, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusServer

    Object GDBusServer

    Signals from GDBusServer:
      new-connection (GDBusConnection) -> gboolean

    Properties from GDBusServer:
      address -> gchararray: address
      client-address -> gchararray: client-address
      flags -> GDBusServerFlags: flags
      guid -> gchararray: guid
      active -> gboolean: active
      authentication-observer -> GDBusAuthObserver: authentication-observer

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def active(self) -> bool: ...
        @property
        def address(self) -> str | None: ...
        @property
        def authentication_observer(self) -> DBusAuthObserver | None: ...
        @property
        def client_address(self) -> str: ...
        @property
        def flags(self) -> DBusServerFlags: ...
        @property
        def guid(self) -> str: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        address: str | None = ...,
        authentication_observer: DBusAuthObserver | None = ...,
        flags: _DBusServerFlagsValueType = ...,
        guid: str | None = ...,
    ) -> None: ...
    def get_client_address(self) -> str: ...
    def get_flags(self) -> DBusServerFlags: ...
    def get_guid(self) -> str: ...
    def is_active(self) -> bool: ...
    @classmethod
    def new_sync(
        cls,
        address: str,
        flags: _DBusServerFlagsValueType,
        guid: str,
        observer: DBusAuthObserver | None = None,
        cancellable: Cancellable | None = None,
    ) -> DBusServer: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class DBusSignalInfo(GObject.GBoxed):
    """
    :Constructors:

    ::

        DBusSignalInfo()
    """

    ref_count: int
    name: str
    args: list[DBusArgInfo]
    annotations: list[DBusAnnotationInfo]
    def __init__(
        self, *args, **kwargs
    ) -> None: ...  # FIXME: Override is missing typing annotation
    def ref(self) -> DBusSignalInfo: ...
    def unref(self) -> None: ...

class DBusSubtreeVTable(_gi.Struct):
    """
    :Constructors:

    ::

        DBusSubtreeVTable()
    """

    enumerate: Callable[[DBusConnection, str, str, Any | None], list[str]]
    introspect: Callable[
        [DBusConnection, str, str, str, Any | None], list[DBusInterfaceInfo]
    ]
    dispatch: Callable[
        [DBusConnection, str, str, str, str, int | Any | None, Any | None],
        DBusInterfaceVTable | None,
    ]
    @property
    def padding(self) -> list[int]: ...

class DataInputStream(BufferedInputStream):
    """
    :Constructors:

    ::

        DataInputStream(**properties)
        new(base_stream:Gio.InputStream) -> Gio.DataInputStream

    Object GDataInputStream

    Properties from GDataInputStream:
      byte-order -> GDataStreamByteOrder: byte-order
      newline-type -> GDataStreamNewlineType: newline-type

    Properties from GBufferedInputStream:
      buffer-size -> guint: buffer-size

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(BufferedInputStream.Props):
        @property
        def byte_order(self) -> DataStreamByteOrder: ...
        @byte_order.setter
        def byte_order(self, value: _DataStreamByteOrderValueType) -> None: ...
        @property
        def newline_type(self) -> DataStreamNewlineType: ...
        @newline_type.setter
        def newline_type(self, value: _DataStreamNewlineTypeValueType) -> None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> BufferedInputStream: ...
    @property
    def priv(self) -> DataInputStreamPrivate: ...
    def __init__(
        self,
        *,
        byte_order: _DataStreamByteOrderValueType = ...,
        newline_type: _DataStreamNewlineTypeValueType = ...,
        buffer_size: int = ...,
        base_stream: InputStream | None = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    # override
    def __iter__(self) -> Self: ...
    # override
    def __next__(self) -> str: ...
    def get_byte_order(self) -> DataStreamByteOrder: ...
    def get_newline_type(self) -> DataStreamNewlineType: ...
    @classmethod
    def new(cls, base_stream: InputStream) -> DataInputStream: ...
    def read_byte(self, cancellable: Cancellable | None = None) -> int: ...
    def read_int16(self, cancellable: Cancellable | None = None) -> int: ...
    def read_int32(self, cancellable: Cancellable | None = None) -> int: ...
    def read_int64(self, cancellable: Cancellable | None = None) -> int: ...
    def read_line(
        self, cancellable: Cancellable | None = None
    ) -> tuple[bytes, int]: ...
    @overload
    def read_line_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[bytes, int]]: ...
    @overload
    def read_line_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DataInputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def read_line_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DataInputStream] | None,
    ) -> None: ...
    def read_line_finish(self, result: AsyncResult) -> tuple[bytes, int]: ...
    def read_line_finish_utf8(self, result: AsyncResult) -> tuple[str | None, int]: ...
    def read_line_utf8(
        self, cancellable: Cancellable | None = None
    ) -> tuple[str | None, int]: ...
    def read_uint16(self, cancellable: Cancellable | None = None) -> int: ...
    def read_uint32(self, cancellable: Cancellable | None = None) -> int: ...
    def read_uint64(self, cancellable: Cancellable | None = None) -> int: ...
    def read_until(
        self, stop_chars: str, cancellable: Cancellable | None = None
    ) -> tuple[str, int]: ...
    @overload
    def read_until_async(
        self, stop_chars: str, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[str, int]]: ...
    @overload
    def read_until_async(
        self,
        stop_chars: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DataInputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def read_until_async(
        self,
        stop_chars: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DataInputStream] | None,
    ) -> None: ...
    def read_until_finish(self, result: AsyncResult) -> tuple[str, int]: ...
    def read_upto(
        self,
        stop_chars: str,
        stop_chars_len: int,
        cancellable: Cancellable | None = None,
    ) -> tuple[str, int]: ...
    @overload
    def read_upto_async(
        self,
        stop_chars: str,
        stop_chars_len: int,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[str, int]]: ...
    @overload
    def read_upto_async(
        self,
        stop_chars: str,
        stop_chars_len: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DataInputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def read_upto_async(
        self,
        stop_chars: str,
        stop_chars_len: int,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DataInputStream] | None,
    ) -> None: ...
    def read_upto_finish(self, result: AsyncResult) -> tuple[str, int]: ...
    def set_byte_order(self, order: _DataStreamByteOrderValueType) -> None: ...
    def set_newline_type(self, type: _DataStreamNewlineTypeValueType) -> None: ...

class DataInputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        DataInputStreamClass()
    """
    @property
    def parent_class(self) -> BufferedInputStreamClass: ...

class DataInputStreamPrivate(_gi.Struct): ...

class DataOutputStream(FilterOutputStream, Seekable):
    """
    :Constructors:

    ::

        DataOutputStream(**properties)
        new(base_stream:Gio.OutputStream) -> Gio.DataOutputStream

    Object GDataOutputStream

    Properties from GDataOutputStream:
      byte-order -> GDataStreamByteOrder: byte-order

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(FilterOutputStream.Props):
        @property
        def byte_order(self) -> DataStreamByteOrder: ...
        @byte_order.setter
        def byte_order(self, value: _DataStreamByteOrderValueType) -> None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> FilterOutputStream: ...
    @property
    def priv(self) -> DataOutputStreamPrivate: ...
    def __init__(
        self,
        *,
        byte_order: _DataStreamByteOrderValueType = ...,
        base_stream: OutputStream | None = ...,
        close_base_stream: bool = ...,
    ) -> None: ...
    def get_byte_order(self) -> DataStreamByteOrder: ...
    @classmethod
    def new(cls, base_stream: OutputStream) -> DataOutputStream: ...
    def put_byte(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def put_int16(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def put_int32(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def put_int64(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def put_string(self, str: str, cancellable: Cancellable | None = None) -> bool: ...
    def put_uint16(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def put_uint32(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def put_uint64(self, data: int, cancellable: Cancellable | None = None) -> bool: ...
    def set_byte_order(self, order: _DataStreamByteOrderValueType) -> None: ...

class DataOutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        DataOutputStreamClass()
    """
    @property
    def parent_class(self) -> FilterOutputStreamClass: ...

class DataOutputStreamPrivate(_gi.Struct): ...

class DatagramBased(GObject.GInterface, Protocol):
    """
    Interface GDatagramBased

    Signals from GObject:
      notify (GParam)
    """
    def condition_check(
        self, condition: GLib._IOConditionValueType
    ) -> GLib.IOCondition: ...
    def condition_wait(
        self,
        condition: GLib._IOConditionValueType,
        timeout: int,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def create_source(
        self,
        condition: GLib._IOConditionValueType,
        cancellable: Cancellable | None = None,
    ) -> GLib.Source: ...
    def receive_messages(
        self,
        messages: Sequence[InputMessage],
        flags: int,
        timeout: int,
        cancellable: Cancellable | None = None,
    ) -> int: ...
    def send_messages(
        self,
        messages: Sequence[OutputMessage],
        flags: int,
        timeout: int,
        cancellable: Cancellable | None = None,
    ) -> int: ...

class DatagramBasedInterface(_gi.Struct):
    """
    :Constructors:

    ::

        DatagramBasedInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def receive_messages(
        self,
    ) -> Callable[
        [DatagramBased, Sequence[InputMessage], int, int, int, Cancellable | None], int
    ]: ...
    @property
    def send_messages(
        self,
    ) -> Callable[
        [DatagramBased, Sequence[OutputMessage], int, int, int, Cancellable | None], int
    ]: ...
    @property
    def create_source(
        self,
    ) -> Callable[
        [DatagramBased, GLib._IOConditionValueType, Cancellable | None], GLib.Source
    ]: ...
    @property
    def condition_check(
        self,
    ) -> Callable[[DatagramBased, GLib._IOConditionValueType], GLib.IOCondition]: ...
    @property
    def condition_wait(
        self,
    ) -> Callable[
        [DatagramBased, GLib._IOConditionValueType, int, Cancellable | None], bool
    ]: ...

class DebugController(GObject.GInterface, Protocol):
    """
    Interface GDebugController

    Signals from GObject:
      notify (GParam)
    """
    def get_debug_enabled(self) -> bool: ...
    def set_debug_enabled(self, debug_enabled: bool) -> None: ...

class DebugControllerDBus(GObject.Object, DebugController, Initable):
    """
    :Constructors:

    ::

        DebugControllerDBus(**properties)
        new(connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> Gio.DebugControllerDBus or None

    Object GDebugControllerDBus

    Signals from GDebugControllerDBus:
      authorize (GDBusMethodInvocation) -> gboolean

    Properties from GDebugControllerDBus:
      connection -> GDBusConnection: connection

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def connection(self) -> DBusConnection | None: ...
        debug_enabled: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(
        self, *, connection: DBusConnection | None = ..., debug_enabled: bool = ...
    ) -> None: ...
    def do_authorize(self, invocation: DBusMethodInvocation, /) -> bool: ...
    @classmethod
    def new(
        cls, connection: DBusConnection, cancellable: Cancellable | None = None
    ) -> DebugControllerDBus | None: ...
    def stop(self) -> None: ...

class DebugControllerDBusClass(_gi.Struct):
    """
    :Constructors:

    ::

        DebugControllerDBusClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def authorize(
        self,
    ) -> Callable[[DebugControllerDBus, DBusMethodInvocation], bool]: ...
    @property
    def padding(self) -> list[int]: ...

class DebugControllerInterface(_gi.Struct):
    """
    :Constructors:

    ::

        DebugControllerInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...

DesktopAppInfo = GioUnix.DesktopAppInfo
DesktopAppInfoLookup = GioUnix.DesktopAppInfoLookup

class Drive(GObject.GInterface, Protocol):
    """
    Interface GDrive

    Signals from GObject:
      notify (GParam)
    """
    def can_eject(self) -> bool: ...
    def can_poll_for_media(self) -> bool: ...
    def can_start(self) -> bool: ...
    def can_start_degraded(self) -> bool: ...
    def can_stop(self) -> bool: ...
    @overload
    def eject(
        self, flags: _MountUnmountFlagsValueType, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def eject(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Drive, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Drive] | None,
    ) -> None: ...
    def eject_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Drive, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Drive] | None,
    ) -> None: ...
    def eject_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def enumerate_identifiers(self) -> list[str]: ...
    def get_icon(self) -> Icon: ...
    def get_identifier(self, kind: str) -> str | None: ...
    def get_name(self) -> str: ...
    def get_sort_key(self) -> str | None: ...
    def get_start_stop_type(self) -> DriveStartStopType: ...
    def get_symbolic_icon(self) -> Icon: ...
    def get_volumes(self) -> list[Volume]: ...
    def has_media(self) -> bool: ...
    def has_volumes(self) -> bool: ...
    def is_media_check_automatic(self) -> bool: ...
    def is_media_removable(self) -> bool: ...
    def is_removable(self) -> bool: ...
    @overload
    def poll_for_media(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def poll_for_media(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Drive, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def poll_for_media(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Drive] | None,
    ) -> None: ...
    def poll_for_media_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def start(
        self,
        flags: _DriveStartFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def start(
        self,
        flags: _DriveStartFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Drive, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def start(
        self,
        flags: _DriveStartFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Drive] | None,
    ) -> None: ...
    def start_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def stop(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def stop(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Drive, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def stop(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Drive] | None,
    ) -> None: ...
    def stop_finish(self, result: AsyncResult) -> bool: ...

class DriveIface(_gi.Struct):
    """
    :Constructors:

    ::

        DriveIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def changed(self) -> Callable[[Drive], None]: ...
    @property
    def disconnected(self) -> Callable[[Drive], None]: ...
    @property
    def eject_button(self) -> Callable[[Drive], None]: ...
    @property
    def get_name(self) -> Callable[[Drive], str]: ...
    @property
    def get_icon(self) -> Callable[[Drive], Icon]: ...
    @property
    def has_volumes(self) -> Callable[[Drive], bool]: ...
    @property
    def get_volumes(self) -> Callable[[Drive], list[Volume]]: ...
    @property
    def is_media_removable(self) -> Callable[[Drive], bool]: ...
    @property
    def has_media(self) -> Callable[[Drive], bool]: ...
    @property
    def is_media_check_automatic(self) -> Callable[[Drive], bool]: ...
    @property
    def can_eject(self) -> Callable[[Drive], bool]: ...
    @property
    def can_poll_for_media(self) -> Callable[[Drive], bool]: ...
    @property
    def eject(
        self,
    ) -> Callable[
        [
            Drive,
            _MountUnmountFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_finish(self) -> Callable[[Drive, AsyncResult], bool]: ...
    @property
    def poll_for_media(
        self,
    ) -> Callable[
        [
            Drive,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def poll_for_media_finish(self) -> Callable[[Drive, AsyncResult], bool]: ...
    @property
    def get_identifier(self) -> Callable[[Drive, str], str | None]: ...
    @property
    def enumerate_identifiers(self) -> Callable[[Drive], list[str]]: ...
    @property
    def get_start_stop_type(self) -> Callable[[Drive], DriveStartStopType]: ...
    @property
    def can_start(self) -> Callable[[Drive], bool]: ...
    @property
    def can_start_degraded(self) -> Callable[[Drive], bool]: ...
    @property
    def start(
        self,
    ) -> Callable[
        [
            Drive,
            _DriveStartFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def start_finish(self) -> Callable[[Drive, AsyncResult], bool]: ...
    @property
    def can_stop(self) -> Callable[[Drive], bool]: ...
    @property
    def stop(
        self,
    ) -> Callable[
        [
            Drive,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def stop_finish(self) -> Callable[[Drive, AsyncResult], bool]: ...
    @property
    def stop_button(self) -> Callable[[Drive], None]: ...
    @property
    def eject_with_operation(
        self,
    ) -> Callable[
        [
            Drive,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_with_operation_finish(self) -> Callable[[Drive, AsyncResult], bool]: ...
    @property
    def get_sort_key(self) -> Callable[[Drive], str | None]: ...
    @property
    def get_symbolic_icon(self) -> Callable[[Drive], Icon]: ...
    @property
    def is_removable(self) -> Callable[[Drive], bool]: ...

class DtlsClientConnection(GObject.GInterface, Protocol):
    """
    Interface GDtlsClientConnection

    Signals from GObject:
      notify (GParam)
    """
    def get_accepted_cas(self) -> list[bytes]: ...
    def get_server_identity(self) -> SocketConnectable: ...
    def get_validation_flags(self) -> TlsCertificateFlags: ...
    @staticmethod
    def new(
        base_socket: DatagramBased, server_identity: SocketConnectable | None = None
    ) -> DtlsClientConnection: ...
    def set_server_identity(self, identity: SocketConnectable) -> None: ...
    def set_validation_flags(self, flags: _TlsCertificateFlagsValueType) -> None: ...

class DtlsClientConnectionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        DtlsClientConnectionInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...

class DtlsConnection(GObject.GInterface, Protocol):
    """
    Interface GDtlsConnection

    Signals from GObject:
      notify (GParam)
    """
    def close(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def close_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DtlsConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DtlsConnection] | None,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def emit_accept_certificate(
        self, peer_cert: TlsCertificate, errors: _TlsCertificateFlagsValueType
    ) -> bool: ...
    def get_certificate(self) -> TlsCertificate | None: ...
    def get_channel_binding_data(
        self, type: _TlsChannelBindingTypeValueType
    ) -> tuple[bool, bytes]: ...
    def get_ciphersuite_name(self) -> str | None: ...
    def get_database(self) -> TlsDatabase | None: ...
    def get_interaction(self) -> TlsInteraction | None: ...
    def get_negotiated_protocol(self) -> str | None: ...
    def get_peer_certificate(self) -> TlsCertificate | None: ...
    def get_peer_certificate_errors(self) -> TlsCertificateFlags: ...
    def get_protocol_version(self) -> TlsProtocolVersion: ...
    def get_rehandshake_mode(self) -> TlsRehandshakeMode: ...
    def get_require_close_notify(self) -> bool: ...
    def handshake(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def handshake_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def handshake_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DtlsConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def handshake_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DtlsConnection] | None,
    ) -> None: ...
    def handshake_finish(self, result: AsyncResult) -> bool: ...
    def set_advertised_protocols(
        self, protocols: Sequence[str] | None = None
    ) -> None: ...
    def set_certificate(self, certificate: TlsCertificate) -> None: ...
    def set_database(self, database: TlsDatabase | None = None) -> None: ...
    def set_interaction(self, interaction: TlsInteraction | None = None) -> None: ...
    def set_rehandshake_mode(self, mode: _TlsRehandshakeModeValueType) -> None: ...
    def set_require_close_notify(self, require_close_notify: bool) -> None: ...
    def shutdown(
        self,
        shutdown_read: bool,
        shutdown_write: bool,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    @overload
    def shutdown_async(
        self,
        shutdown_read: bool,
        shutdown_write: bool,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def shutdown_async(
        self,
        shutdown_read: bool,
        shutdown_write: bool,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[DtlsConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def shutdown_async(
        self,
        shutdown_read: bool,
        shutdown_write: bool,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[DtlsConnection] | None,
    ) -> None: ...
    def shutdown_finish(self, result: AsyncResult) -> bool: ...

class DtlsConnectionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        DtlsConnectionInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def accept_certificate(
        self,
    ) -> Callable[
        [DtlsConnection, TlsCertificate, _TlsCertificateFlagsValueType], bool
    ]: ...
    @property
    def handshake(self) -> Callable[[DtlsConnection, Cancellable | None], bool]: ...
    @property
    def handshake_async(
        self,
    ) -> Callable[
        [
            DtlsConnection,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def handshake_finish(self) -> Callable[[DtlsConnection, AsyncResult], bool]: ...
    @property
    def shutdown(
        self,
    ) -> Callable[[DtlsConnection, bool, bool, Cancellable | None], bool]: ...
    @property
    def shutdown_async(
        self,
    ) -> Callable[
        [
            DtlsConnection,
            bool,
            bool,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def shutdown_finish(self) -> Callable[[DtlsConnection, AsyncResult], bool]: ...
    @property
    def set_advertised_protocols(
        self,
    ) -> Callable[[DtlsConnection, Sequence[str] | None], None]: ...
    @property
    def get_negotiated_protocol(self) -> Callable[[DtlsConnection], str | None]: ...
    @property
    def get_binding_data(
        self,
    ) -> Callable[
        [DtlsConnection, _TlsChannelBindingTypeValueType, Sequence[int]], bool
    ]: ...

class DtlsServerConnection(GObject.GInterface, Protocol):
    """
    Interface GDtlsServerConnection

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def new(
        base_socket: DatagramBased, certificate: TlsCertificate | None = None
    ) -> DtlsServerConnection: ...

class DtlsServerConnectionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        DtlsServerConnectionInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...

class Emblem(GObject.Object, Icon):
    """
    :Constructors:

    ::

        Emblem(**properties)
        new(icon:Gio.Icon) -> Gio.Emblem
        new_with_origin(icon:Gio.Icon, origin:Gio.EmblemOrigin) -> Gio.Emblem

    Object GEmblem

    Properties from GEmblem:
      icon -> GObject: icon
      origin -> GEmblemOrigin: origin

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def icon(self) -> GObject.Object: ...
        @property
        def origin(self) -> EmblemOrigin: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, icon: GObject.Object | None = ..., origin: _EmblemOriginValueType = ...
    ) -> None: ...
    def get_icon(self) -> Icon: ...
    def get_origin(self) -> EmblemOrigin: ...
    @classmethod
    def new(cls, icon: Icon) -> Emblem: ...
    @classmethod
    def new_with_origin(cls, icon: Icon, origin: _EmblemOriginValueType) -> Emblem: ...

class EmblemClass(_gi.Struct): ...

class EmblemedIcon(GObject.Object, Icon):
    """
    :Constructors:

    ::

        EmblemedIcon(**properties)
        new(icon:Gio.Icon, emblem:Gio.Emblem=None) -> Gio.EmblemedIcon

    Object GEmblemedIcon

    Properties from GEmblemedIcon:
      gicon -> GIcon: gicon

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def gicon(self) -> Icon | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> EmblemedIconPrivate: ...
    def __init__(self, *, gicon: Icon | None = ...) -> None: ...
    def add_emblem(self, emblem: Emblem) -> None: ...
    def clear_emblems(self) -> None: ...
    def get_emblems(self) -> list[Emblem]: ...
    def get_icon(self) -> Icon: ...
    @classmethod
    def new(cls, icon: Icon, emblem: Emblem | None = None) -> EmblemedIcon: ...

class EmblemedIconClass(_gi.Struct):
    """
    :Constructors:

    ::

        EmblemedIconClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class EmblemedIconPrivate(_gi.Struct): ...

class File(GObject.GInterface, Protocol):
    """
    Interface GFile

    Signals from GObject:
      notify (GParam)
    """
    def append_to(
        self, flags: _FileCreateFlagsValueType, cancellable: Cancellable | None = None
    ) -> FileOutputStream: ...
    @overload
    def append_to_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileOutputStream]: ...
    @overload
    def append_to_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def append_to_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def append_to_finish(self, res: AsyncResult) -> FileOutputStream: ...
    def build_attribute_list_for_copy(
        self, flags: _FileCopyFlagsValueType, cancellable: Cancellable | None = None
    ) -> str: ...
    def copy(
        self,
        destination: File,
        flags: _FileCopyFlagsValueType,
        cancellable: Cancellable | None = None,
        progress_callback: Callable[[int, int, Unpack[_DataTs]], None] | None = None,
        *progress_callback_data: Unpack[_DataTs],
    ) -> bool: ...
    def copy_async(
        self,
        destination: File,
        flags: _FileCopyFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        progress_callback_closure: Callable[..., Any] | None,
        ready_callback_closure: Callable[..., Any],
    ) -> None: ...
    def copy_attributes(
        self,
        destination: File,
        flags: _FileCopyFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def copy_finish(self, res: AsyncResult) -> bool: ...
    def create(
        self, flags: _FileCreateFlagsValueType, cancellable: Cancellable | None = None
    ) -> FileOutputStream: ...
    @overload
    def create_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileOutputStream]: ...
    @overload
    def create_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def create_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def create_finish(self, res: AsyncResult) -> FileOutputStream: ...
    def create_readwrite(
        self, flags: _FileCreateFlagsValueType, cancellable: Cancellable | None = None
    ) -> FileIOStream: ...
    @overload
    def create_readwrite_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileIOStream]: ...
    @overload
    def create_readwrite_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def create_readwrite_async(
        self,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def create_readwrite_finish(self, res: AsyncResult) -> FileIOStream: ...
    def delete(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def delete_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def delete_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def delete_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def delete_finish(self, result: AsyncResult) -> bool: ...
    def dup(self) -> File: ...
    @overload
    def eject_mountable(
        self, flags: _MountUnmountFlagsValueType, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def eject_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def eject_mountable_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def eject_mountable_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def eject_mountable_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject_mountable_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def eject_mountable_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def enumerate_children(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> FileEnumerator: ...
    @overload
    def enumerate_children_async(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileEnumerator]: ...
    @overload
    def enumerate_children_async(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def enumerate_children_async(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def enumerate_children_finish(self, res: AsyncResult) -> FileEnumerator: ...
    def equal(self, file2: File) -> bool: ...
    def find_enclosing_mount(self, cancellable: Cancellable | None = None) -> Mount: ...
    @overload
    def find_enclosing_mount_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[Mount]: ...
    @overload
    def find_enclosing_mount_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def find_enclosing_mount_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def find_enclosing_mount_finish(self, res: AsyncResult) -> Mount: ...
    def get_basename(self) -> str | None: ...
    def get_child(self, name: str) -> File: ...
    def get_child_for_display_name(self, display_name: str) -> File: ...
    def get_parent(self) -> File | None: ...
    def get_parse_name(self) -> str: ...
    def get_path(self) -> str | None: ...
    def get_relative_path(self, descendant: File) -> str | None: ...
    def get_uri(self) -> str: ...
    def get_uri_scheme(self) -> str | None: ...
    def has_parent(self, parent: File | None = None) -> bool: ...
    def has_prefix(self, prefix: File) -> bool: ...
    def has_uri_scheme(self, uri_scheme: str) -> bool: ...
    def hash(self) -> int: ...
    def is_native(self) -> bool: ...
    def load_bytes(
        self, cancellable: Cancellable | None = None
    ) -> tuple[GLib.Bytes, str | None]: ...
    @overload
    def load_bytes_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[GLib.Bytes, str | None]]: ...
    @overload
    def load_bytes_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def load_bytes_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def load_bytes_finish(
        self, result: AsyncResult
    ) -> tuple[GLib.Bytes, str | None]: ...
    def load_contents(
        self, cancellable: Cancellable | None = None
    ) -> tuple[bool, bytes, str | None]: ...
    @overload
    def load_contents_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[bool, bytes, str | None]]: ...
    @overload
    def load_contents_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def load_contents_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def load_contents_finish(
        self, res: AsyncResult
    ) -> tuple[bool, bytes, str | None]: ...
    def load_partial_contents_finish(
        self, res: AsyncResult
    ) -> tuple[bool, bytes, str | None]: ...
    def make_directory(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def make_directory_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def make_directory_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def make_directory_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def make_directory_finish(self, result: AsyncResult) -> bool: ...
    def make_directory_with_parents(
        self, cancellable: Cancellable | None = None
    ) -> bool: ...
    def make_symbolic_link(
        self, symlink_value: str, cancellable: Cancellable | None = None
    ) -> bool: ...
    @overload
    def make_symbolic_link_async(
        self,
        symlink_value: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def make_symbolic_link_async(
        self,
        symlink_value: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def make_symbolic_link_async(
        self,
        symlink_value: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def make_symbolic_link_finish(self, result: AsyncResult) -> bool: ...
    def measure_disk_usage(
        self,
        flags: _FileMeasureFlagsValueType,
        cancellable: Cancellable | None = None,
        progress_callback: Callable[[bool, int, int, int, Unpack[_DataTs]], None]
        | None = None,
        *progress_data: Unpack[_DataTs],
    ) -> tuple[bool, int, int, int]: ...
    def measure_disk_usage_finish(
        self, result: AsyncResult
    ) -> tuple[bool, int, int, int]: ...
    def monitor(
        self, flags: _FileMonitorFlagsValueType, cancellable: Cancellable | None = None
    ) -> FileMonitor: ...
    def monitor_directory(
        self, flags: _FileMonitorFlagsValueType, cancellable: Cancellable | None = None
    ) -> FileMonitor: ...
    def monitor_file(
        self, flags: _FileMonitorFlagsValueType, cancellable: Cancellable | None = None
    ) -> FileMonitor: ...
    @overload
    def mount_enclosing_volume(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def mount_enclosing_volume(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def mount_enclosing_volume(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def mount_enclosing_volume_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def mount_mountable(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[File]: ...
    @overload
    def mount_mountable(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def mount_mountable(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def mount_mountable_finish(self, result: AsyncResult) -> File: ...
    def move(
        self,
        destination: File,
        flags: _FileCopyFlagsValueType,
        cancellable: Cancellable | None = None,
        progress_callback: Callable[[int, int, Unpack[_DataTs]], None] | None = None,
        *progress_callback_data: Unpack[_DataTs],
    ) -> bool: ...
    def move_async(
        self,
        destination: File,
        flags: _FileCopyFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        progress_callback_closure: Callable[..., Any] | None,
        ready_callback_closure: Callable[..., Any],
    ) -> None: ...
    def move_finish(self, result: AsyncResult) -> bool: ...
    @staticmethod
    def new_build_filenamev(args: Sequence[str]) -> File: ...
    @staticmethod
    def new_for_commandline_arg(arg: str) -> File: ...
    @staticmethod
    def new_for_commandline_arg_and_cwd(arg: str, cwd: str) -> File: ...
    @staticmethod
    def new_for_path(path: str) -> File: ...
    @staticmethod
    def new_for_uri(uri: str) -> File: ...
    @staticmethod
    def new_tmp(tmpl: str | None = None) -> tuple[File, FileIOStream]: ...
    @overload
    @staticmethod
    def new_tmp_async(
        tmpl: str | None, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[File, FileIOStream]]: ...
    @overload
    @staticmethod
    def new_tmp_async(
        tmpl: str | None,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new_tmp_async(
        tmpl: str | None,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @overload
    @staticmethod
    def new_tmp_dir_async(
        tmpl: str | None, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[File]: ...
    @overload
    @staticmethod
    def new_tmp_dir_async(
        tmpl: str | None,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[None, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    @staticmethod
    def new_tmp_dir_async(
        tmpl: str | None,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[None] | None,
    ) -> None: ...
    @staticmethod
    def new_tmp_dir_finish(result: AsyncResult) -> File: ...
    @staticmethod
    def new_tmp_finish(result: AsyncResult) -> tuple[File, FileIOStream]: ...
    def open_readwrite(
        self, cancellable: Cancellable | None = None
    ) -> FileIOStream: ...
    @overload
    def open_readwrite_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[FileIOStream]: ...
    @overload
    def open_readwrite_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def open_readwrite_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def open_readwrite_finish(self, res: AsyncResult) -> FileIOStream: ...
    @staticmethod
    def parse_name(parse_name: str) -> File: ...
    def peek_path(self) -> str | None: ...
    @overload
    def poll_mountable(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def poll_mountable(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def poll_mountable(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def poll_mountable_finish(self, result: AsyncResult) -> bool: ...
    def query_default_handler(
        self, cancellable: Cancellable | None = None
    ) -> AppInfo: ...
    @overload
    def query_default_handler_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[AppInfo]: ...
    @overload
    def query_default_handler_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def query_default_handler_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def query_default_handler_finish(self, result: AsyncResult) -> AppInfo: ...
    def query_exists(self, cancellable: Cancellable | None = None) -> bool: ...
    def query_file_type(
        self,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> FileType: ...
    def query_filesystem_info(
        self, attributes: str, cancellable: Cancellable | None = None
    ) -> FileInfo: ...
    @overload
    def query_filesystem_info_async(
        self, attributes: str, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[FileInfo]: ...
    @overload
    def query_filesystem_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def query_filesystem_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def query_filesystem_info_finish(self, res: AsyncResult) -> FileInfo: ...
    def query_info(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> FileInfo: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileInfo]: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def query_info_finish(self, res: AsyncResult) -> FileInfo: ...
    def query_settable_attributes(
        self, cancellable: Cancellable | None = None
    ) -> FileAttributeInfoList: ...
    def query_writable_namespaces(
        self, cancellable: Cancellable | None = None
    ) -> FileAttributeInfoList: ...
    def read(self, cancellable: Cancellable | None = None) -> FileInputStream: ...
    @overload
    def read_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[FileInputStream]: ...
    @overload
    def read_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def read_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def read_finish(self, res: AsyncResult) -> FileInputStream: ...
    def replace(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> FileOutputStream: ...
    @overload
    def replace_async(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileOutputStream]: ...
    @overload
    def replace_async(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def replace_async(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def replace_contents(
        self,
        contents: Sequence[int],
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> tuple[bool, str | None]: ...
    @overload
    def replace_contents_async(
        self,
        contents: Sequence[int],
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[bool, str | None]]: ...
    @overload
    def replace_contents_async(
        self,
        contents: Sequence[int],
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def replace_contents_async(
        self,
        contents: Sequence[int],
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def replace_contents_bytes_async(
        self,
        contents: GLib.Bytes,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None = None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None = None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    def replace_contents_finish(self, res: AsyncResult) -> tuple[bool, str | None]: ...
    def replace_finish(self, res: AsyncResult) -> FileOutputStream: ...
    def replace_readwrite(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> FileIOStream: ...
    @overload
    def replace_readwrite_async(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[FileIOStream]: ...
    @overload
    def replace_readwrite_async(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def replace_readwrite_async(
        self,
        etag: str | None,
        make_backup: bool,
        flags: _FileCreateFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def replace_readwrite_finish(self, res: AsyncResult) -> FileIOStream: ...
    def resolve_relative_path(self, relative_path: str) -> File: ...
    def set_attribute(
        self,
        attribute: str,
        type: _FileAttributeTypeValueType,
        value_p: int | Any | None,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_attribute_byte_string(
        self,
        attribute: str,
        value: str,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_attribute_int32(
        self,
        attribute: str,
        value: int,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_attribute_int64(
        self,
        attribute: str,
        value: int,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_attribute_string(
        self,
        attribute: str,
        value: str,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_attribute_uint32(
        self,
        attribute: str,
        value: int,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_attribute_uint64(
        self,
        attribute: str,
        value: int,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    @overload
    def set_attributes_async(
        self,
        info: FileInfo,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[bool, FileInfo]]: ...
    @overload
    def set_attributes_async(
        self,
        info: FileInfo,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def set_attributes_async(
        self,
        info: FileInfo,
        flags: _FileQueryInfoFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def set_attributes_finish(self, result: AsyncResult) -> tuple[bool, FileInfo]: ...
    def set_attributes_from_info(
        self,
        info: FileInfo,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def set_display_name(
        self, display_name: str, cancellable: Cancellable | None = None
    ) -> File: ...
    @overload
    def set_display_name_async(
        self,
        display_name: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[File]: ...
    @overload
    def set_display_name_async(
        self,
        display_name: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def set_display_name_async(
        self,
        display_name: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def set_display_name_finish(self, res: AsyncResult) -> File: ...
    @overload
    def start_mountable(
        self,
        flags: _DriveStartFlagsValueType,
        start_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def start_mountable(
        self,
        flags: _DriveStartFlagsValueType,
        start_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def start_mountable(
        self,
        flags: _DriveStartFlagsValueType,
        start_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def start_mountable_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def stop_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def stop_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def stop_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def stop_mountable_finish(self, result: AsyncResult) -> bool: ...
    def supports_thread_contexts(self) -> bool: ...
    def trash(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def trash_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def trash_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def trash_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def trash_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def unmount_mountable(
        self, flags: _MountUnmountFlagsValueType, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def unmount_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def unmount_mountable(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def unmount_mountable_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def unmount_mountable_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def unmount_mountable_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[File, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def unmount_mountable_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[File] | None,
    ) -> None: ...
    def unmount_mountable_with_operation_finish(self, result: AsyncResult) -> bool: ...

class FileAttributeInfo(_gi.Struct):
    """
    :Constructors:

    ::

        FileAttributeInfo()
    """

    name: str
    type: FileAttributeType
    flags: FileAttributeInfoFlags

class FileAttributeInfoList(GObject.GBoxed):
    """
    :Constructors:

    ::

        FileAttributeInfoList()
        new() -> Gio.FileAttributeInfoList
    """

    infos: FileAttributeInfo
    n_infos: int
    def __init__(self) -> None: ...
    def add(
        self,
        name: str,
        type: _FileAttributeTypeValueType,
        flags: _FileAttributeInfoFlagsValueType,
    ) -> None: ...
    def dup(self) -> FileAttributeInfoList: ...
    def lookup(self, name: str) -> FileAttributeInfo: ...
    @classmethod
    def new(cls) -> FileAttributeInfoList: ...
    def ref(self) -> FileAttributeInfoList: ...
    def unref(self) -> None: ...

class FileAttributeMatcher(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(attributes:str) -> Gio.FileAttributeMatcher
    """
    def __init__(self, attributes: str) -> None: ...
    def enumerate_namespace(self, ns: str) -> bool: ...
    def enumerate_next(self) -> str | None: ...
    def matches(self, attribute: str) -> bool: ...
    def matches_only(self, attribute: str) -> bool: ...
    @classmethod
    def new(cls, attributes: str) -> FileAttributeMatcher: ...
    def ref(self) -> FileAttributeMatcher: ...
    def subtract(
        self, subtract: FileAttributeMatcher | None = None
    ) -> FileAttributeMatcher | None: ...
    def to_string(self) -> str: ...
    def unref(self) -> None: ...

FileDescriptorBased = GioUnix.FileDescriptorBased

class FileEnumerator(GObject.Object):
    """
    :Constructors:

    ::

        FileEnumerator(**properties)

    Object GFileEnumerator

    Properties from GFileEnumerator:
      container -> GFile: container

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> FileEnumeratorPrivate: ...
    def __init__(self, *, container: File | None = ...) -> None: ...
    # override
    def __iter__(self) -> Self: ...
    # override
    def __next__(self) -> FileInfo: ...
    def close(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def close_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[FileEnumerator, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[FileEnumerator] | None,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[FileEnumerator, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult, /) -> bool: ...
    def do_close_fn(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_next_file(self, cancellable: Cancellable | None, /) -> FileInfo | None: ...
    def do_next_files_async(
        self,
        num_files: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[FileEnumerator, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_next_files_finish(self, result: AsyncResult, /) -> list[FileInfo]: ...
    def get_child(self, info: FileInfo) -> File: ...
    def get_container(self) -> File: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def iterate(
        self, cancellable: Cancellable | None = None
    ) -> tuple[bool, FileInfo, File]: ...
    def next_file(self, cancellable: Cancellable | None = None) -> FileInfo | None: ...
    @overload
    def next_files_async(
        self, num_files: int, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[list[FileInfo]]: ...
    @overload
    def next_files_async(
        self,
        num_files: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[FileEnumerator, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def next_files_async(
        self,
        num_files: int,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[FileEnumerator] | None,
    ) -> None: ...
    def next_files_finish(self, result: AsyncResult) -> list[FileInfo]: ...
    def set_pending(self, pending: bool) -> None: ...

class FileEnumeratorClass(_gi.Struct):
    """
    :Constructors:

    ::

        FileEnumeratorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def next_file(
        self,
    ) -> Callable[[FileEnumerator, Cancellable | None], FileInfo | None]: ...
    @property
    def close_fn(self) -> Callable[[FileEnumerator, Cancellable | None], bool]: ...
    @property
    def next_files_async(
        self,
    ) -> Callable[
        [
            FileEnumerator,
            int,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def next_files_finish(
        self,
    ) -> Callable[[FileEnumerator, AsyncResult], list[FileInfo]]: ...
    @property
    def close_async(
        self,
    ) -> Callable[
        [
            FileEnumerator,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def close_finish(self) -> Callable[[FileEnumerator, AsyncResult], bool]: ...

class FileEnumeratorPrivate(_gi.Struct): ...

class FileIOStream(IOStream, Seekable):
    """
    :Constructors:

    ::

        FileIOStream(**properties)

    Object GFileIOStream

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> IOStream: ...
    @property
    def priv(self) -> FileIOStreamPrivate: ...
    def do_can_seek(self) -> bool: ...
    def do_can_truncate(self) -> bool: ...
    def do_get_etag(self) -> str | None: ...
    def do_query_info(
        self, attributes: str, cancellable: Cancellable | None, /
    ) -> FileInfo: ...
    def do_query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[FileIOStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_query_info_finish(self, result: AsyncResult, /) -> FileInfo: ...
    def do_seek(
        self, offset: int, type: GLib.SeekType, cancellable: Cancellable | None, /
    ) -> bool: ...
    def do_tell(self) -> int: ...
    def do_truncate_fn(self, size: int, cancellable: Cancellable | None, /) -> bool: ...
    def get_etag(self) -> str | None: ...
    def query_info(
        self, attributes: str, cancellable: Cancellable | None = None
    ) -> FileInfo: ...
    @overload
    def query_info_async(
        self, attributes: str, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[FileInfo]: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[FileIOStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[FileIOStream] | None,
    ) -> None: ...
    def query_info_finish(self, result: AsyncResult) -> FileInfo: ...

class FileIOStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        FileIOStreamClass()
    """
    @property
    def parent_class(self) -> IOStreamClass: ...
    @property
    def tell(self) -> Callable[[FileIOStream], int]: ...
    @property
    def can_seek(self) -> Callable[[FileIOStream], bool]: ...
    @property
    def seek(
        self,
    ) -> Callable[[FileIOStream, int, GLib.SeekType, Cancellable | None], bool]: ...
    @property
    def can_truncate(self) -> Callable[[FileIOStream], bool]: ...
    @property
    def truncate_fn(
        self,
    ) -> Callable[[FileIOStream, int, Cancellable | None], bool]: ...
    @property
    def query_info(
        self,
    ) -> Callable[[FileIOStream, str, Cancellable | None], FileInfo]: ...
    @property
    def query_info_async(
        self,
    ) -> Callable[
        [
            FileIOStream,
            str,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def query_info_finish(self) -> Callable[[FileIOStream, AsyncResult], FileInfo]: ...
    @property
    def get_etag(self) -> Callable[[FileIOStream], str | None]: ...

class FileIOStreamPrivate(_gi.Struct): ...

class FileIcon(GObject.Object, Icon, LoadableIcon):
    """
    :Constructors:

    ::

        FileIcon(**properties)
        new(file:Gio.File) -> Gio.FileIcon

    Object GFileIcon

    Properties from GFileIcon:
      file -> GFile: file

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def file(self) -> File: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, file: File | None = ...) -> None: ...
    def get_file(self) -> File: ...
    @classmethod
    def new(cls, file: File) -> FileIcon: ...

class FileIconClass(_gi.Struct): ...

class FileIface(_gi.Struct):
    """
    :Constructors:

    ::

        FileIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def dup(self) -> Callable[[File], File]: ...
    @property
    def hash(self) -> Callable[[File], int]: ...
    @property
    def equal(self) -> Callable[[File, File], bool]: ...
    @property
    def is_native(self) -> Callable[[File], bool]: ...
    @property
    def has_uri_scheme(self) -> Callable[[File, str], bool]: ...
    @property
    def get_uri_scheme(self) -> Callable[[File], str | None]: ...
    @property
    def get_basename(self) -> Callable[[File], str | None]: ...
    @property
    def get_path(self) -> Callable[[File], str | None]: ...
    @property
    def get_uri(self) -> Callable[[File], str]: ...
    @property
    def get_parse_name(self) -> Callable[[File], str]: ...
    @property
    def get_parent(self) -> Callable[[File], File | None]: ...
    @property
    def prefix_matches(self) -> Callable[[File, File], bool]: ...
    @property
    def get_relative_path(self) -> Callable[[File, File], str | None]: ...
    @property
    def resolve_relative_path(self) -> Callable[[File, str], File]: ...
    @property
    def get_child_for_display_name(self) -> Callable[[File, str], File]: ...
    @property
    def enumerate_children(
        self,
    ) -> Callable[
        [File, str, _FileQueryInfoFlagsValueType, Cancellable | None], FileEnumerator
    ]: ...
    @property
    def enumerate_children_async(
        self,
    ) -> Callable[
        [
            File,
            str,
            _FileQueryInfoFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def enumerate_children_finish(
        self,
    ) -> Callable[[File, AsyncResult], FileEnumerator]: ...
    @property
    def query_info(
        self,
    ) -> Callable[
        [File, str, _FileQueryInfoFlagsValueType, Cancellable | None], FileInfo
    ]: ...
    @property
    def query_info_async(
        self,
    ) -> Callable[
        [
            File,
            str,
            _FileQueryInfoFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def query_info_finish(self) -> Callable[[File, AsyncResult], FileInfo]: ...
    @property
    def query_filesystem_info(
        self,
    ) -> Callable[[File, str, Cancellable | None], FileInfo]: ...
    @property
    def query_filesystem_info_async(
        self,
    ) -> Callable[
        [
            File,
            str,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def query_filesystem_info_finish(
        self,
    ) -> Callable[[File, AsyncResult], FileInfo]: ...
    @property
    def find_enclosing_mount(self) -> Callable[[File, Cancellable | None], Mount]: ...
    @property
    def find_enclosing_mount_async(
        self,
    ) -> Callable[
        [
            File,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def find_enclosing_mount_finish(self) -> Callable[[File, AsyncResult], Mount]: ...
    @property
    def set_display_name(self) -> Callable[[File, str, Cancellable | None], File]: ...
    @property
    def set_display_name_async(
        self,
    ) -> Callable[
        [
            File,
            str,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def set_display_name_finish(self) -> Callable[[File, AsyncResult], File]: ...
    @property
    def query_settable_attributes(
        self,
    ) -> Callable[[File, Cancellable | None], FileAttributeInfoList]: ...
    @property
    def query_writable_namespaces(
        self,
    ) -> Callable[[File, Cancellable | None], FileAttributeInfoList]: ...
    @property
    def set_attribute(
        self,
    ) -> Callable[
        [
            File,
            str,
            _FileAttributeTypeValueType,
            Any | None,
            _FileQueryInfoFlagsValueType,
            Cancellable | None,
        ],
        bool,
    ]: ...
    @property
    def set_attributes_from_info(
        self,
    ) -> Callable[
        [File, FileInfo, _FileQueryInfoFlagsValueType, Cancellable | None], bool
    ]: ...
    @property
    def set_attributes_async(
        self,
    ) -> Callable[
        [
            File,
            FileInfo,
            _FileQueryInfoFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def set_attributes_finish(
        self,
    ) -> Callable[[File, AsyncResult], tuple[bool, FileInfo]]: ...
    @property
    def read_fn(self) -> Callable[[File, Cancellable | None], FileInputStream]: ...
    @property
    def read_async(
        self,
    ) -> Callable[
        [
            File,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def read_finish(self) -> Callable[[File, AsyncResult], FileInputStream]: ...
    @property
    def append_to(
        self,
    ) -> Callable[
        [File, _FileCreateFlagsValueType, Cancellable | None], FileOutputStream
    ]: ...
    @property
    def append_to_async(
        self,
    ) -> Callable[
        [
            File,
            _FileCreateFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def append_to_finish(self) -> Callable[[File, AsyncResult], FileOutputStream]: ...
    @property
    def create(
        self,
    ) -> Callable[
        [File, _FileCreateFlagsValueType, Cancellable | None], FileOutputStream
    ]: ...
    @property
    def create_async(
        self,
    ) -> Callable[
        [
            File,
            _FileCreateFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def create_finish(self) -> Callable[[File, AsyncResult], FileOutputStream]: ...
    @property
    def replace(
        self,
    ) -> Callable[
        [File, str | None, bool, _FileCreateFlagsValueType, Cancellable | None],
        FileOutputStream,
    ]: ...
    @property
    def replace_async(
        self,
    ) -> Callable[
        [
            File,
            str | None,
            bool,
            _FileCreateFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def replace_finish(self) -> Callable[[File, AsyncResult], FileOutputStream]: ...
    @property
    def delete_file(self) -> Callable[[File, Cancellable | None], bool]: ...
    @property
    def delete_file_async(
        self,
    ) -> Callable[
        [
            File,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def delete_file_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def trash(self) -> Callable[[File, Cancellable | None], bool]: ...
    @property
    def trash_async(
        self,
    ) -> Callable[
        [
            File,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def trash_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def make_directory(self) -> Callable[[File, Cancellable | None], bool]: ...
    @property
    def make_directory_async(
        self,
    ) -> Callable[
        [
            File,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def make_directory_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def make_symbolic_link(self) -> Callable[[File, str, Cancellable | None], bool]: ...
    @property
    def make_symbolic_link_async(
        self,
    ) -> Callable[
        [
            File,
            str,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def make_symbolic_link_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def copy(
        self,
    ) -> Callable[
        [
            File,
            File,
            _FileCopyFlagsValueType,
            Cancellable | None,
            Callable[[int, int, Any | None], None] | None,
            Any | None,
        ],
        bool,
    ]: ...
    @property
    def copy_async(
        self,
    ) -> Callable[
        [
            File,
            File,
            _FileCopyFlagsValueType,
            int,
            Cancellable | None,
            Callable[[int, int, Any | None], None] | None,
            int | Any | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def copy_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def move(
        self,
    ) -> Callable[
        [
            File,
            File,
            _FileCopyFlagsValueType,
            Cancellable | None,
            Callable[[int, int, Any | None], None] | None,
            Any | None,
        ],
        bool,
    ]: ...
    @property
    def move_async(
        self,
    ) -> Callable[
        [
            File,
            File,
            _FileCopyFlagsValueType,
            int,
            Cancellable | None,
            Callable[[int, int, Any | None], None] | None,
            int | Any | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def move_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def mount_mountable(
        self,
    ) -> Callable[
        [
            File,
            _MountMountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def mount_mountable_finish(self) -> Callable[[File, AsyncResult], File]: ...
    @property
    def unmount_mountable(
        self,
    ) -> Callable[
        [
            File,
            _MountUnmountFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def unmount_mountable_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def eject_mountable(
        self,
    ) -> Callable[
        [
            File,
            _MountUnmountFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_mountable_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def mount_enclosing_volume(
        self,
    ) -> Callable[
        [
            File,
            _MountMountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def mount_enclosing_volume_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def monitor_dir(
        self,
    ) -> Callable[
        [File, _FileMonitorFlagsValueType, Cancellable | None], FileMonitor
    ]: ...
    @property
    def monitor_file(
        self,
    ) -> Callable[
        [File, _FileMonitorFlagsValueType, Cancellable | None], FileMonitor
    ]: ...
    @property
    def open_readwrite(self) -> Callable[[File, Cancellable | None], FileIOStream]: ...
    @property
    def open_readwrite_async(
        self,
    ) -> Callable[
        [
            File,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def open_readwrite_finish(self) -> Callable[[File, AsyncResult], FileIOStream]: ...
    @property
    def create_readwrite(
        self,
    ) -> Callable[
        [File, _FileCreateFlagsValueType, Cancellable | None], FileIOStream
    ]: ...
    @property
    def create_readwrite_async(
        self,
    ) -> Callable[
        [
            File,
            _FileCreateFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def create_readwrite_finish(
        self,
    ) -> Callable[[File, AsyncResult], FileIOStream]: ...
    @property
    def replace_readwrite(
        self,
    ) -> Callable[
        [File, str | None, bool, _FileCreateFlagsValueType, Cancellable | None],
        FileIOStream,
    ]: ...
    @property
    def replace_readwrite_async(
        self,
    ) -> Callable[
        [
            File,
            str | None,
            bool,
            _FileCreateFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def replace_readwrite_finish(
        self,
    ) -> Callable[[File, AsyncResult], FileIOStream]: ...
    @property
    def start_mountable(
        self,
    ) -> Callable[
        [
            File,
            _DriveStartFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def start_mountable_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def stop_mountable(
        self,
    ) -> Callable[
        [
            File,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def stop_mountable_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def supports_thread_contexts(self) -> bool: ...
    @property
    def unmount_mountable_with_operation(
        self,
    ) -> Callable[
        [
            File,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def unmount_mountable_with_operation_finish(
        self,
    ) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def eject_mountable_with_operation(
        self,
    ) -> Callable[
        [
            File,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_mountable_with_operation_finish(
        self,
    ) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def poll_mountable(
        self,
    ) -> Callable[
        [
            File,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def poll_mountable_finish(self) -> Callable[[File, AsyncResult], bool]: ...
    @property
    def measure_disk_usage(
        self,
    ) -> Callable[
        [
            File,
            _FileMeasureFlagsValueType,
            Cancellable | None,
            Callable[[bool, int, int, int, Any | None], None] | None,
            Any | None,
        ],
        tuple[bool, int, int, int],
    ]: ...
    @property
    def measure_disk_usage_async(self) -> int: ...
    @property
    def measure_disk_usage_finish(
        self,
    ) -> Callable[[File, AsyncResult], tuple[bool, int, int, int]]: ...
    @property
    def query_exists(self) -> Callable[[File, Cancellable | None], bool]: ...

class FileInfo(GObject.Object):
    """
    :Constructors:

    ::

        FileInfo(**properties)
        new() -> Gio.FileInfo

    Object GFileInfo

    Signals from GObject:
      notify (GParam)
    """
    def clear_status(self) -> None: ...
    def copy_into(self, dest_info: FileInfo) -> None: ...
    def dup(self) -> FileInfo: ...
    def get_access_date_time(self) -> GLib.DateTime | None: ...
    def get_attribute_as_string(self, attribute: str) -> str | None: ...
    def get_attribute_boolean(self, attribute: str) -> bool: ...
    def get_attribute_byte_string(self, attribute: str) -> str | None: ...
    def get_attribute_data(
        self, attribute: str
    ) -> tuple[bool, FileAttributeType, int, FileAttributeStatus]: ...
    def get_attribute_file_path(self, attribute: str) -> str | None: ...
    def get_attribute_int32(self, attribute: str) -> int: ...
    def get_attribute_int64(self, attribute: str) -> int: ...
    def get_attribute_object(self, attribute: str) -> GObject.Object | None: ...
    def get_attribute_status(self, attribute: str) -> FileAttributeStatus: ...
    def get_attribute_string(self, attribute: str) -> str | None: ...
    def get_attribute_stringv(self, attribute: str) -> list[str]: ...
    def get_attribute_type(self, attribute: str) -> FileAttributeType: ...
    def get_attribute_uint32(self, attribute: str) -> int: ...
    def get_attribute_uint64(self, attribute: str) -> int: ...
    def get_content_type(self) -> str | None: ...
    def get_creation_date_time(self) -> GLib.DateTime | None: ...
    def get_deletion_date(self) -> GLib.DateTime | None: ...
    def get_display_name(self) -> str: ...
    def get_edit_name(self) -> str: ...
    def get_etag(self) -> str | None: ...
    def get_file_type(self) -> FileType: ...
    def get_icon(self) -> Icon | None: ...
    def get_is_backup(self) -> bool: ...
    def get_is_hidden(self) -> bool: ...
    def get_is_symlink(self) -> bool: ...
    def get_modification_date_time(self) -> GLib.DateTime | None: ...
    def get_modification_time(self) -> GLib.TimeVal: ...
    def get_name(self) -> str: ...
    def get_size(self) -> int: ...
    def get_sort_order(self) -> int: ...
    def get_symbolic_icon(self) -> Icon | None: ...
    def get_symlink_target(self) -> str | None: ...
    def has_attribute(self, attribute: str) -> bool: ...
    def has_namespace(self, name_space: str) -> bool: ...
    def list_attributes(self, name_space: str | None = None) -> list[str]: ...
    @classmethod
    def new(cls) -> FileInfo: ...
    def remove_attribute(self, attribute: str) -> None: ...
    def set_access_date_time(self, atime: GLib.DateTime) -> None: ...
    def set_attribute(
        self,
        attribute: str,
        type: _FileAttributeTypeValueType,
        value_p: int | Any | None,
    ) -> None: ...
    def set_attribute_boolean(self, attribute: str, attr_value: bool) -> None: ...
    def set_attribute_byte_string(self, attribute: str, attr_value: str) -> None: ...
    def set_attribute_file_path(self, attribute: str, attr_value: str) -> None: ...
    def set_attribute_int32(self, attribute: str, attr_value: int) -> None: ...
    def set_attribute_int64(self, attribute: str, attr_value: int) -> None: ...
    def set_attribute_mask(self, mask: FileAttributeMatcher) -> None: ...
    def set_attribute_object(
        self, attribute: str, attr_value: GObject.Object
    ) -> None: ...
    def set_attribute_status(
        self, attribute: str, status: _FileAttributeStatusValueType
    ) -> bool: ...
    def set_attribute_string(self, attribute: str, attr_value: str) -> None: ...
    def set_attribute_stringv(
        self, attribute: str, attr_value: Sequence[str]
    ) -> None: ...
    def set_attribute_uint32(self, attribute: str, attr_value: int) -> None: ...
    def set_attribute_uint64(self, attribute: str, attr_value: int) -> None: ...
    def set_content_type(self, content_type: str) -> None: ...
    def set_creation_date_time(self, creation_time: GLib.DateTime) -> None: ...
    def set_display_name(self, display_name: str) -> None: ...
    def set_edit_name(self, edit_name: str) -> None: ...
    def set_file_type(self, type: _FileTypeValueType) -> None: ...
    def set_icon(self, icon: Icon) -> None: ...
    def set_is_hidden(self, is_hidden: bool) -> None: ...
    def set_is_symlink(self, is_symlink: bool) -> None: ...
    def set_modification_date_time(self, mtime: GLib.DateTime) -> None: ...
    def set_modification_time(self, mtime: GLib.TimeVal) -> None: ...
    def set_name(self, name: str) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_sort_order(self, sort_order: int) -> None: ...
    def set_symbolic_icon(self, icon: Icon) -> None: ...
    def set_symlink_target(self, symlink_target: str) -> None: ...
    def unset_attribute_mask(self) -> None: ...

class FileInfoClass(_gi.Struct): ...

class FileInputStream(InputStream, Seekable):
    """
    :Constructors:

    ::

        FileInputStream(**properties)

    Object GFileInputStream

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> InputStream: ...
    @property
    def priv(self) -> FileInputStreamPrivate: ...
    def do_can_seek(self) -> bool: ...
    def do_query_info(
        self, attributes: str, cancellable: Cancellable | None, /
    ) -> FileInfo: ...
    def do_query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[FileInputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_query_info_finish(self, result: AsyncResult, /) -> FileInfo: ...
    def do_seek(
        self, offset: int, type: GLib.SeekType, cancellable: Cancellable | None, /
    ) -> bool: ...
    def do_tell(self) -> int: ...
    def query_info(
        self, attributes: str, cancellable: Cancellable | None = None
    ) -> FileInfo: ...
    @overload
    def query_info_async(
        self, attributes: str, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[FileInfo]: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[FileInputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[FileInputStream] | None,
    ) -> None: ...
    def query_info_finish(self, result: AsyncResult) -> FileInfo: ...

class FileInputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        FileInputStreamClass()
    """
    @property
    def parent_class(self) -> InputStreamClass: ...
    @property
    def tell(self) -> Callable[[FileInputStream], int]: ...
    @property
    def can_seek(self) -> Callable[[FileInputStream], bool]: ...
    @property
    def seek(
        self,
    ) -> Callable[[FileInputStream, int, GLib.SeekType, Cancellable | None], bool]: ...
    @property
    def query_info(
        self,
    ) -> Callable[[FileInputStream, str, Cancellable | None], FileInfo]: ...
    @property
    def query_info_async(
        self,
    ) -> Callable[
        [
            FileInputStream,
            str,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def query_info_finish(
        self,
    ) -> Callable[[FileInputStream, AsyncResult], FileInfo]: ...

class FileInputStreamPrivate(_gi.Struct): ...

class FileMonitor(GObject.Object):
    """
    :Constructors:

    ::

        FileMonitor(**properties)

    Object GFileMonitor

    Signals from GFileMonitor:
      changed (GFile, GFile, GFileMonitorEvent)

    Properties from GFileMonitor:
      rate-limit -> gint: rate-limit
      cancelled -> gboolean: cancelled

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def cancelled(self) -> bool: ...
        rate_limit: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> FileMonitorPrivate: ...
    def __init__(self, *, rate_limit: int = ...) -> None: ...
    def cancel(self) -> bool: ...
    def do_cancel(self) -> bool: ...
    def do_changed(
        self, file: File, other_file: File, event_type: _FileMonitorEventValueType, /
    ) -> None: ...
    def emit_event(
        self,
        child: File,
        other_file: File | None,
        event_type: _FileMonitorEventValueType,
    ) -> None: ...
    def is_cancelled(self) -> bool: ...
    def set_rate_limit(self, limit_msecs: int) -> None: ...

class FileMonitorClass(_gi.Struct):
    """
    :Constructors:

    ::

        FileMonitorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def changed(
        self,
    ) -> Callable[[FileMonitor, File, File, _FileMonitorEventValueType], None]: ...
    @property
    def cancel(self) -> Callable[[FileMonitor], bool]: ...

class FileMonitorPrivate(_gi.Struct): ...

class FileOutputStream(OutputStream, Seekable):
    """
    :Constructors:

    ::

        FileOutputStream(**properties)

    Object GFileOutputStream

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> OutputStream: ...
    @property
    def priv(self) -> FileOutputStreamPrivate: ...
    def do_can_seek(self) -> bool: ...
    def do_can_truncate(self) -> bool: ...
    def do_get_etag(self) -> str | None: ...
    def do_query_info(
        self, attributes: str, cancellable: Cancellable | None, /
    ) -> FileInfo: ...
    def do_query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[FileOutputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_query_info_finish(self, result: AsyncResult, /) -> FileInfo: ...
    def do_seek(
        self, offset: int, type: GLib.SeekType, cancellable: Cancellable | None, /
    ) -> bool: ...
    def do_tell(self) -> int: ...
    def do_truncate_fn(self, size: int, cancellable: Cancellable | None, /) -> bool: ...
    def get_etag(self) -> str | None: ...
    def query_info(
        self, attributes: str, cancellable: Cancellable | None = None
    ) -> FileInfo: ...
    @overload
    def query_info_async(
        self, attributes: str, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[FileInfo]: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[FileOutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def query_info_async(
        self,
        attributes: str,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[FileOutputStream] | None,
    ) -> None: ...
    def query_info_finish(self, result: AsyncResult) -> FileInfo: ...

class FileOutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        FileOutputStreamClass()
    """
    @property
    def parent_class(self) -> OutputStreamClass: ...
    @property
    def tell(self) -> Callable[[FileOutputStream], int]: ...
    @property
    def can_seek(self) -> Callable[[FileOutputStream], bool]: ...
    @property
    def seek(
        self,
    ) -> Callable[[FileOutputStream, int, GLib.SeekType, Cancellable | None], bool]: ...
    @property
    def can_truncate(self) -> Callable[[FileOutputStream], bool]: ...
    @property
    def truncate_fn(
        self,
    ) -> Callable[[FileOutputStream, int, Cancellable | None], bool]: ...
    @property
    def query_info(
        self,
    ) -> Callable[[FileOutputStream, str, Cancellable | None], FileInfo]: ...
    @property
    def query_info_async(
        self,
    ) -> Callable[
        [
            FileOutputStream,
            str,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def query_info_finish(
        self,
    ) -> Callable[[FileOutputStream, AsyncResult], FileInfo]: ...
    @property
    def get_etag(self) -> Callable[[FileOutputStream], str | None]: ...

class FileOutputStreamPrivate(_gi.Struct): ...

class FilenameCompleter(GObject.Object):
    """
    :Constructors:

    ::

        FilenameCompleter(**properties)
        new() -> Gio.FilenameCompleter

    Object GFilenameCompleter

    Signals from GFilenameCompleter:
      got-completion-data ()

    Signals from GObject:
      notify (GParam)
    """
    def do_got_completion_data(self) -> None: ...
    def get_completion_suffix(self, initial_text: str) -> str | None: ...
    def get_completions(self, initial_text: str) -> list[str]: ...
    @classmethod
    def new(cls) -> FilenameCompleter: ...
    def set_dirs_only(self, dirs_only: bool) -> None: ...

class FilenameCompleterClass(_gi.Struct):
    """
    :Constructors:

    ::

        FilenameCompleterClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def got_completion_data(self) -> Callable[[FilenameCompleter], None]: ...

class FilterInputStream(InputStream):
    """
    :Constructors:

    ::

        FilterInputStream(**properties)

    Object GFilterInputStream

    Properties from GFilterInputStream:
      base-stream -> GInputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(InputStream.Props):
        @property
        def base_stream(self) -> InputStream: ...
        close_base_stream: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> InputStream: ...
    @property
    def base_stream(self) -> InputStream: ...
    def __init__(
        self, *, base_stream: InputStream | None = ..., close_base_stream: bool = ...
    ) -> None: ...
    def get_base_stream(self) -> InputStream: ...
    def get_close_base_stream(self) -> bool: ...
    def set_close_base_stream(self, close_base: bool) -> None: ...

class FilterInputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        FilterInputStreamClass()
    """
    @property
    def parent_class(self) -> InputStreamClass: ...

class FilterOutputStream(OutputStream):
    """
    :Constructors:

    ::

        FilterOutputStream(**properties)

    Object GFilterOutputStream

    Properties from GFilterOutputStream:
      base-stream -> GOutputStream: base-stream
      close-base-stream -> gboolean: close-base-stream

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(OutputStream.Props):
        @property
        def base_stream(self) -> OutputStream: ...
        @property
        def close_base_stream(self) -> bool: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> OutputStream: ...
    @property
    def base_stream(self) -> OutputStream: ...
    def __init__(
        self, *, base_stream: OutputStream | None = ..., close_base_stream: bool = ...
    ) -> None: ...
    def get_base_stream(self) -> OutputStream: ...
    def get_close_base_stream(self) -> bool: ...
    def set_close_base_stream(self, close_base: bool) -> None: ...

class FilterOutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        FilterOutputStreamClass()
    """
    @property
    def parent_class(self) -> OutputStreamClass: ...

class IOExtension(_gi.Struct):
    def get_name(self) -> str: ...
    def get_priority(self) -> int: ...
    def get_type(self) -> type[Any]: ...

class IOExtensionPoint(_gi.Struct):
    def get_extension_by_name(self, name: str) -> IOExtension: ...
    def get_extensions(self) -> list[IOExtension]: ...
    def get_required_type(self) -> type[Any]: ...
    @staticmethod
    def implement(
        extension_point_name: str, type: type[Any], extension_name: str, priority: int
    ) -> IOExtension: ...
    @staticmethod
    def lookup(name: str) -> IOExtensionPoint: ...
    @staticmethod
    def register(name: str) -> IOExtensionPoint: ...
    def set_required_type(self, type: type[Any]) -> None: ...

class IOModule(GObject.TypeModule):
    """
    :Constructors:

    ::

        IOModule(**properties)
        new(filename:str) -> Gio.IOModule

    Object GIOModule

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls, filename: str) -> IOModule: ...
    @staticmethod
    def query() -> list[str]: ...

class IOModuleClass(_gi.Struct): ...

class IOModuleScope(_gi.Struct):
    def block(self, basename: str) -> None: ...
    def free(self) -> None: ...

class IOSchedulerJob(_gi.Struct):
    def send_to_mainloop(
        self, func: Callable[[Unpack[_DataTs]], bool], *user_data: Unpack[_DataTs]
    ) -> bool: ...
    def send_to_mainloop_async(
        self, func: Callable[[Unpack[_DataTs]], bool], *user_data: Unpack[_DataTs]
    ) -> None: ...

class IOStream(GObject.Object):
    """
    :Constructors:

    ::

        IOStream(**properties)

    Object GIOStream

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def closed(self) -> bool: ...
        @property
        def input_stream(self) -> InputStream: ...
        @property
        def output_stream(self) -> OutputStream: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> IOStreamPrivate: ...
    def clear_pending(self) -> None: ...
    def close(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def close_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[IOStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[IOStream] | None,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[IOStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult, /) -> bool: ...
    def do_close_fn(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_get_input_stream(self) -> InputStream: ...
    def do_get_output_stream(self) -> OutputStream: ...
    def get_input_stream(self) -> InputStream: ...
    def get_output_stream(self) -> OutputStream: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def set_pending(self) -> bool: ...
    @overload
    def splice_async(
        self,
        stream2: IOStream,
        flags: _IOStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def splice_async(
        self,
        stream2: IOStream,
        flags: _IOStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[IOStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def splice_async(
        self,
        stream2: IOStream,
        flags: _IOStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[IOStream] | None,
    ) -> None: ...
    @staticmethod
    def splice_finish(result: AsyncResult) -> bool: ...

class IOStreamAdapter(_gi.Struct): ...

class IOStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        IOStreamClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_input_stream(self) -> Callable[[IOStream], InputStream]: ...
    @property
    def get_output_stream(self) -> Callable[[IOStream], OutputStream]: ...
    @property
    def close_fn(self) -> Callable[[IOStream, Cancellable | None], bool]: ...
    @property
    def close_async(
        self,
    ) -> Callable[
        [
            IOStream,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def close_finish(self) -> Callable[[IOStream, AsyncResult], bool]: ...

class IOStreamPrivate(_gi.Struct): ...

class Icon(GObject.GInterface, Protocol):
    """
    Interface GIcon

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def deserialize(value: GLib.Variant) -> Icon | None: ...
    def equal(self, icon2: Icon | None = None) -> bool: ...
    def hash(self) -> int: ...
    @staticmethod
    def new_for_string(str: str) -> Icon: ...
    def serialize(self) -> GLib.Variant | None: ...
    def to_string(self) -> str | None: ...

class IconIface(_gi.Struct):
    """
    :Constructors:

    ::

        IconIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def hash(self) -> Callable[[Icon], int]: ...
    @property
    def equal(self) -> Callable[[Icon | None, Icon | None], bool]: ...
    @property
    def to_tokens(self) -> Callable[[Icon], tuple[bool, list[str], int]]: ...
    @property
    def from_tokens(self) -> int: ...
    @property
    def serialize(self) -> Callable[[Icon], GLib.Variant | None]: ...

class InetAddress(GObject.Object):
    """
    :Constructors:

    ::

        InetAddress(**properties)
        new_any(family:Gio.SocketFamily) -> Gio.InetAddress
        new_from_bytes(bytes:list, family:Gio.SocketFamily) -> Gio.InetAddress
        new_from_bytes_with_ipv6_info(bytes:list, family:Gio.SocketFamily, flowinfo:int, scope_id:int) -> Gio.InetAddress
        new_from_string(string:str) -> Gio.InetAddress or None
        new_loopback(family:Gio.SocketFamily) -> Gio.InetAddress

    Object GInetAddress

    Properties from GInetAddress:
      family -> GSocketFamily: family
      bytes -> gpointer: bytes
      is-any -> gboolean: is-any
      is-loopback -> gboolean: is-loopback
      is-link-local -> gboolean: is-link-local
      is-site-local -> gboolean: is-site-local
      is-multicast -> gboolean: is-multicast
      is-mc-global -> gboolean: is-mc-global
      is-mc-link-local -> gboolean: is-mc-link-local
      is-mc-node-local -> gboolean: is-mc-node-local
      is-mc-org-local -> gboolean: is-mc-org-local
      is-mc-site-local -> gboolean: is-mc-site-local
      flowinfo -> guint: flowinfo
      scope-id -> guint: scope-id

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def bytes(self) -> int: ...
        @property
        def family(self) -> SocketFamily: ...
        @property
        def flowinfo(self) -> int: ...
        @property
        def is_any(self) -> bool: ...
        @property
        def is_link_local(self) -> bool: ...
        @property
        def is_loopback(self) -> bool: ...
        @property
        def is_mc_global(self) -> bool: ...
        @property
        def is_mc_link_local(self) -> bool: ...
        @property
        def is_mc_node_local(self) -> bool: ...
        @property
        def is_mc_org_local(self) -> bool: ...
        @property
        def is_mc_site_local(self) -> bool: ...
        @property
        def is_multicast(self) -> bool: ...
        @property
        def is_site_local(self) -> bool: ...
        @property
        def scope_id(self) -> int: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> InetAddressPrivate: ...
    def __init__(
        self,
        *,
        bytes: int | Any | None = ...,
        family: _SocketFamilyValueType = ...,
        flowinfo: int = ...,
        scope_id: int = ...,
    ) -> None: ...
    def do_to_string(self) -> str: ...
    def equal(self, other_address: InetAddress) -> bool: ...
    def get_family(self) -> SocketFamily: ...
    def get_flowinfo(self) -> int: ...
    def get_is_any(self) -> bool: ...
    def get_is_link_local(self) -> bool: ...
    def get_is_loopback(self) -> bool: ...
    def get_is_mc_global(self) -> bool: ...
    def get_is_mc_link_local(self) -> bool: ...
    def get_is_mc_node_local(self) -> bool: ...
    def get_is_mc_org_local(self) -> bool: ...
    def get_is_mc_site_local(self) -> bool: ...
    def get_is_multicast(self) -> bool: ...
    def get_is_site_local(self) -> bool: ...
    def get_native_size(self) -> int: ...
    def get_scope_id(self) -> int: ...
    @classmethod
    def new_any(cls, family: _SocketFamilyValueType) -> InetAddress: ...
    @classmethod
    def new_from_bytes(
        cls, bytes: Sequence[int], family: _SocketFamilyValueType
    ) -> InetAddress: ...
    @classmethod
    def new_from_bytes_with_ipv6_info(
        cls,
        bytes: Sequence[int],
        family: _SocketFamilyValueType,
        flowinfo: int,
        scope_id: int,
    ) -> InetAddress: ...
    @classmethod
    def new_from_string(cls, string: str) -> InetAddress | None: ...
    @classmethod
    def new_loopback(cls, family: _SocketFamilyValueType) -> InetAddress: ...
    def to_string(self) -> str: ...

class InetAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        InetAddressClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def to_string(self) -> Callable[[InetAddress], str]: ...
    @property
    def to_bytes(self) -> Callable[[InetAddress], int]: ...

class InetAddressMask(GObject.Object, Initable):
    """
    :Constructors:

    ::

        InetAddressMask(**properties)
        new(addr:Gio.InetAddress, length:int) -> Gio.InetAddressMask
        new_from_string(mask_string:str) -> Gio.InetAddressMask

    Object GInetAddressMask

    Properties from GInetAddressMask:
      family -> GSocketFamily: family
      address -> GInetAddress: address
      length -> guint: length

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def address(self) -> InetAddress: ...
        @address.setter
        def address(self, value: InetAddress | None) -> None: ...
        @property
        def family(self) -> SocketFamily: ...
        length: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> InetAddressMaskPrivate: ...
    def __init__(
        self, *, address: InetAddress | None = ..., length: int = ...
    ) -> None: ...
    def equal(self, mask2: InetAddressMask) -> bool: ...
    def get_address(self) -> InetAddress: ...
    def get_family(self) -> SocketFamily: ...
    def get_length(self) -> int: ...
    def matches(self, address: InetAddress) -> bool: ...
    @classmethod
    def new(cls, addr: InetAddress, length: int) -> InetAddressMask: ...
    @classmethod
    def new_from_string(cls, mask_string: str) -> InetAddressMask: ...
    def to_string(self) -> str: ...

class InetAddressMaskClass(_gi.Struct):
    """
    :Constructors:

    ::

        InetAddressMaskClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class InetAddressMaskPrivate(_gi.Struct): ...
class InetAddressPrivate(_gi.Struct): ...

class InetSocketAddress(SocketAddress):
    """
    :Constructors:

    ::

        InetSocketAddress(**properties)
        new(address:Gio.InetAddress, port:int) -> Gio.SocketAddress
        new_from_string(address:str, port:int) -> Gio.SocketAddress or None

    Object GInetSocketAddress

    Properties from GInetSocketAddress:
      address -> GInetAddress: address
      port -> guint: port
      flowinfo -> guint: flowinfo
      scope-id -> guint: scope-id

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketAddress.Props):
        @property
        def address(self) -> InetAddress: ...
        @property
        def flowinfo(self) -> int: ...
        @property
        def port(self) -> int: ...
        @property
        def scope_id(self) -> int: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketAddress: ...
    @property
    def priv(self) -> InetSocketAddressPrivate: ...
    def __init__(
        self,
        *,
        address: InetAddress | None = ...,
        flowinfo: int = ...,
        port: int = ...,
        scope_id: int = ...,
    ) -> None: ...
    def get_address(self) -> InetAddress: ...
    def get_flowinfo(self) -> int: ...
    def get_port(self) -> int: ...
    def get_scope_id(self) -> int: ...
    @classmethod
    def new(cls, address: InetAddress, port: int) -> InetSocketAddress: ...
    @classmethod
    def new_from_string(cls, address: str, port: int) -> InetSocketAddress: ...

class InetSocketAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        InetSocketAddressClass()
    """
    @property
    def parent_class(self) -> SocketAddressClass: ...

class InetSocketAddressPrivate(_gi.Struct): ...

class Initable(GObject.GInterface, Protocol):
    """
    Interface GInitable

    Signals from GObject:
      notify (GParam)
    """
    def init(self, cancellable: Cancellable | None = None) -> bool: ...
    @staticmethod
    def newv(
        object_type: type[Any],
        parameters: Sequence[GObject.Parameter],
        cancellable: Cancellable | None = None,
    ) -> GObject.Object: ...

class InitableIface(_gi.Struct):
    """
    :Constructors:

    ::

        InitableIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def init(self) -> Callable[[Initable, Cancellable | None], bool]: ...

class InputMessage(_gi.Struct):
    """
    :Constructors:

    ::

        InputMessage()
    """

    address: SocketAddress
    vectors: list[InputVector]
    num_vectors: int
    bytes_received: int
    flags: int
    control_messages: list[SocketControlMessage]
    num_control_messages: int

class InputStream(GObject.Object):
    """
    :Constructors:

    ::

        InputStream(**properties)

    Object GInputStream

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> InputStreamPrivate: ...
    def clear_pending(self) -> None: ...
    def close(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def close_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[InputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[InputStream] | None,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[InputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult, /) -> bool: ...
    def do_close_fn(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_read_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[InputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> bytes: ...
    def do_read_finish(self, result: AsyncResult, /) -> int: ...
    def do_read_fn(
        self, buffer: int | Any | None, count: int, cancellable: Cancellable | None, /
    ) -> int: ...
    def do_skip(self, count: int, cancellable: Cancellable | None, /) -> int: ...
    def do_skip_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[InputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_skip_finish(self, result: AsyncResult, /) -> int: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def read(self, cancellable: Cancellable | None = None) -> tuple[int, bytes]: ...
    def read_all(
        self, cancellable: Cancellable | None = None
    ) -> tuple[bool, bytes, int]: ...
    def read_all_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        callback: _AsyncReadyVarArgsCallback[InputStream, Unpack[_DataTs]]
        | None = None,
        *user_data: Unpack[_DataTs],
    ) -> bytes: ...
    def read_all_finish(self, result: AsyncResult) -> tuple[bool, int]: ...
    def read_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        callback: _AsyncReadyVarArgsCallback[InputStream, Unpack[_DataTs]]
        | None = None,
        *user_data: Unpack[_DataTs],
    ) -> bytes: ...
    def read_bytes(
        self, count: int, cancellable: Cancellable | None = None
    ) -> GLib.Bytes: ...
    @overload
    def read_bytes_async(
        self, count: int, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[GLib.Bytes]: ...
    @overload
    def read_bytes_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[InputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def read_bytes_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[InputStream] | None,
    ) -> None: ...
    def read_bytes_finish(self, result: AsyncResult) -> GLib.Bytes: ...
    def read_finish(self, result: AsyncResult) -> int: ...
    def set_pending(self) -> bool: ...
    def skip(self, count: int, cancellable: Cancellable | None = None) -> int: ...
    @overload
    def skip_async(
        self, count: int, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[int]: ...
    @overload
    def skip_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[InputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def skip_async(
        self,
        count: int,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[InputStream] | None,
    ) -> None: ...
    def skip_finish(self, result: AsyncResult) -> int: ...

class InputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        InputStreamClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def read_fn(
        self,
    ) -> Callable[[InputStream, Any | None, int, Cancellable | None], int]: ...
    @property
    def skip(self) -> Callable[[InputStream, int, Cancellable | None], int]: ...
    @property
    def close_fn(self) -> Callable[[InputStream, Cancellable | None], bool]: ...
    @property
    def read_async(
        self,
    ) -> Callable[
        [
            InputStream,
            int,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        bytes,
    ]: ...
    @property
    def read_finish(self) -> Callable[[InputStream, AsyncResult], int]: ...
    @property
    def skip_async(
        self,
    ) -> Callable[
        [
            InputStream,
            int,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def skip_finish(self) -> Callable[[InputStream, AsyncResult], int]: ...
    @property
    def close_async(
        self,
    ) -> Callable[
        [
            InputStream,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def close_finish(self) -> Callable[[InputStream, AsyncResult], bool]: ...

class InputStreamPrivate(_gi.Struct): ...

class InputVector(_gi.Struct):
    """
    :Constructors:

    ::

        InputVector()
    """

    buffer: int
    size: int

class ListModel(GObject.GInterface, Protocol[ObjectItemType]):
    """
    Interface GListModel

    Signals from GObject:
      notify (GParam)
    """
    def __contains__(self, item: ObjectItemType) -> bool: ...
    @overload
    def __getitem__(self, key: slice) -> list[ObjectItemType]: ...
    @overload
    def __getitem__(self, key: int) -> ObjectItemType: ...
    def __iter__(self) -> Iterator[ObjectItemType]: ...
    def __len__(self) -> int: ...
    # override
    def get_item(self, position: int) -> ObjectItemType | None: ...
    # override
    def get_item_type(self) -> type[ObjectItemType]: ...
    def get_n_items(self) -> int: ...
    def items_changed(self, position: int, removed: int, added: int) -> None: ...

class ListModelInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ListModelInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def get_item_type(self) -> Callable[[ListModel], type[Any]]: ...
    @property
    def get_n_items(self) -> Callable[[ListModel], int]: ...
    @property
    def get_item(self) -> Callable[[ListModel, int], GObject.Object | None]: ...

# override
class ListStore(GObject.Object, ListModel[ObjectItemType], Generic[ObjectItemType]):
    """
    :Constructors:

    ::

        ListStore(**properties)
        new(item_type:GType) -> ListStore

    Object GListStore

    Properties from GListStore:
      itemtype -> GType: itemtype
      nitems -> guint: nitems

    Signals from GListModel:
      itemschanged (guint, guint, guint)

    Signals from GObject:
      notify (GParam)
    """

    @type_check_only
    class Props(GObject.Object.Props, Generic[ObjectPropsItemType]):
        @property
        def item_type(self) -> type[ObjectPropsItemType]: ...
        @property
        def n_items(self) -> int: ...

    @property
    def props(self) -> Props[ObjectItemType]: ...
    def __init__(self, *, item_type: type[ObjectItemType] = ...) -> None: ...
    def __delitem__(self, key: int | slice) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Sequence[ObjectItemType]) -> None: ...
    @overload
    def __setitem__(self, key: int, value: ObjectItemType) -> None: ...
    def append(self, item: ObjectItemType) -> None: ...
    def find(self, item: ObjectItemType) -> tuple[bool, int]: ...
    def find_with_equal_func(
        self,
        item: ObjectItemType | None,
        equal_func: Callable[
            [ObjectItemType | None, ObjectItemType | None, Unpack[_DataTs]], bool
        ],
        *user_data: Unpack[_DataTs],
    ) -> tuple[bool, int]: ...
    def find_with_equal_func_full(
        self,
        item: ObjectItemType | None,
        equal_func: Callable[
            [ObjectItemType | None, ObjectItemType | None, Unpack[_DataTs]], bool
        ],
        *user_data: Unpack[_DataTs],
    ) -> tuple[bool, int]: ...
    def insert(self, position: int, item: ObjectItemType) -> None: ...
    def insert_sorted(
        self,
        item: ObjectItemType,
        compare_func: Callable[
            [ObjectItemType | None, ObjectItemType | None, Unpack[_DataTs]], int
        ],
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @classmethod
    def new(cls, item_type: type[ObjectItemType]) -> ListStore[ObjectItemType]: ...
    def remove(self, position: int) -> None: ...
    def remove_all(self) -> None: ...
    def sort(
        self,
        compare_func: Callable[
            [ObjectItemType | None, ObjectItemType | None, Unpack[_DataTs]], int
        ],
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    def splice(
        self, position: int, n_removals: int, additions: Sequence[ObjectItemType]
    ) -> None: ...

class ListStoreClass(_gi.Struct):
    """
    :Constructors:

    ::

        ListStoreClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class LoadableIcon(GObject.GInterface, Protocol):
    """
    Interface GLoadableIcon

    Signals from GObject:
      notify (GParam)
    """
    def load(
        self, size: int, cancellable: Cancellable | None = None
    ) -> tuple[InputStream, str]: ...
    @overload
    def load_async(
        self, size: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[InputStream, str]]: ...
    @overload
    def load_async(
        self,
        size: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[LoadableIcon, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def load_async(
        self,
        size: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[LoadableIcon] | None,
    ) -> None: ...
    def load_finish(self, res: AsyncResult) -> tuple[InputStream, str]: ...

class LoadableIconIface(_gi.Struct):
    """
    :Constructors:

    ::

        LoadableIconIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def load(
        self,
    ) -> Callable[[LoadableIcon, int, Cancellable | None], tuple[InputStream, str]]: ...
    @property
    def load_async(
        self,
    ) -> Callable[
        [
            LoadableIcon,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def load_finish(
        self,
    ) -> Callable[[LoadableIcon, AsyncResult], tuple[InputStream, str]]: ...

class MemoryInputStream(InputStream, PollableInputStream, Seekable):
    """
    :Constructors:

    ::

        MemoryInputStream(**properties)
        new() -> Gio.InputStream
        new_from_bytes(bytes:GLib.Bytes) -> Gio.InputStream
        new_from_data(data:list, destroy:GLib.DestroyNotify=None) -> Gio.InputStream

    Object GMemoryInputStream

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> InputStream: ...
    @property
    def priv(self) -> MemoryInputStreamPrivate: ...
    def add_bytes(self, bytes: GLib.Bytes) -> None: ...
    def add_data(
        self, data: Sequence[int], destroy: Callable[[Any | None], None] | None = None
    ) -> None: ...
    @classmethod
    def new(cls) -> MemoryInputStream: ...
    @classmethod
    def new_from_bytes(cls, bytes: GLib.Bytes) -> MemoryInputStream: ...
    @classmethod
    def new_from_data(
        cls, data: Sequence[int], destroy: Callable[[Any | None], None] | None = None
    ) -> MemoryInputStream: ...

class MemoryInputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        MemoryInputStreamClass()
    """
    @property
    def parent_class(self) -> InputStreamClass: ...

class MemoryInputStreamPrivate(_gi.Struct): ...

class MemoryMonitor(GObject.GInterface, Protocol):
    """
    Interface GMemoryMonitor

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def dup_default() -> MemoryMonitor: ...

class MemoryMonitorInterface(_gi.Struct):
    """
    :Constructors:

    ::

        MemoryMonitorInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def low_memory_warning(
        self,
    ) -> Callable[[MemoryMonitor, _MemoryMonitorWarningLevelValueType], None]: ...

class MemoryOutputStream(OutputStream, PollableOutputStream, Seekable):
    """
    :Constructors:

    ::

        MemoryOutputStream(**properties)
        new_resizable() -> Gio.OutputStream

    Object GMemoryOutputStream

    Properties from GMemoryOutputStream:
      data -> gpointer: data
      size -> gulong: size
      data-size -> gulong: data-size
      realloc-function -> gpointer: realloc-function
      destroy-function -> gpointer: destroy-function

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(OutputStream.Props):
        @property
        def data(self) -> int: ...
        @property
        def data_size(self) -> int: ...
        @property
        def size(self) -> int: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> OutputStream: ...
    @property
    def priv(self) -> MemoryOutputStreamPrivate: ...
    def __init__(self, *, data: int | Any | None = ..., size: int = ...) -> None: ...
    def get_data(self) -> int: ...
    def get_data_size(self) -> int: ...
    def get_size(self) -> int: ...
    @classmethod
    def new_resizable(cls) -> MemoryOutputStream: ...
    def steal_as_bytes(self) -> GLib.Bytes: ...
    def steal_data(self) -> int: ...

class MemoryOutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        MemoryOutputStreamClass()
    """
    @property
    def parent_class(self) -> OutputStreamClass: ...

class MemoryOutputStreamPrivate(_gi.Struct): ...

class Menu(MenuModel):
    """
    :Constructors:

    ::

        Menu(**properties)
        new() -> Gio.Menu

    Object GMenu

    Signals from GMenuModel:
      items-changed (gint, gint, gint)

    Signals from GObject:
      notify (GParam)
    """
    def append(
        self, label: str | None = None, detailed_action: str | None = None
    ) -> None: ...
    def append_item(self, item: MenuItem) -> None: ...
    def append_section(self, label: str | None, section: MenuModel) -> None: ...
    def append_submenu(self, label: str | None, submenu: MenuModel) -> None: ...
    def freeze(self) -> None: ...
    def insert(
        self,
        position: int,
        label: str | None = None,
        detailed_action: str | None = None,
    ) -> None: ...
    def insert_item(self, position: int, item: MenuItem) -> None: ...
    def insert_section(
        self, position: int, label: str | None, section: MenuModel
    ) -> None: ...
    def insert_submenu(
        self, position: int, label: str | None, submenu: MenuModel
    ) -> None: ...
    @classmethod
    def new(cls) -> Menu: ...
    def prepend(
        self, label: str | None = None, detailed_action: str | None = None
    ) -> None: ...
    def prepend_item(self, item: MenuItem) -> None: ...
    def prepend_section(self, label: str | None, section: MenuModel) -> None: ...
    def prepend_submenu(self, label: str | None, submenu: MenuModel) -> None: ...
    def remove(self, position: int) -> None: ...
    def remove_all(self) -> None: ...

class MenuAttributeIter(GObject.Object):
    """
    :Constructors:

    ::

        MenuAttributeIter(**properties)

    Object GMenuAttributeIter

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> MenuAttributeIterPrivate: ...
    def do_get_next(self) -> tuple[bool, str, GLib.Variant]: ...
    def get_name(self) -> str: ...
    def get_next(self) -> tuple[bool, str, GLib.Variant]: ...
    def get_value(self) -> GLib.Variant: ...
    def next(self) -> bool: ...

class MenuAttributeIterClass(_gi.Struct):
    """
    :Constructors:

    ::

        MenuAttributeIterClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_next(
        self,
    ) -> Callable[[MenuAttributeIter], tuple[bool, str, GLib.Variant]]: ...

class MenuAttributeIterPrivate(_gi.Struct): ...

class MenuItem(GObject.Object):
    """
    :Constructors:

    ::

        MenuItem(**properties)
        new(label:str=None, detailed_action:str=None) -> Gio.MenuItem
        new_from_model(model:Gio.MenuModel, item_index:int) -> Gio.MenuItem
        new_section(label:str=None, section:Gio.MenuModel) -> Gio.MenuItem
        new_submenu(label:str=None, submenu:Gio.MenuModel) -> Gio.MenuItem

    Object GMenuItem

    Signals from GObject:
      notify (GParam)
    """
    def get_attribute_value(
        self, attribute: str, expected_type: GLib.VariantType | None = None
    ) -> GLib.Variant | None: ...
    def get_link(self, link: str) -> MenuModel | None: ...
    @classmethod
    def new(
        cls, label: str | None = None, detailed_action: str | None = None
    ) -> MenuItem: ...
    @classmethod
    def new_from_model(cls, model: MenuModel, item_index: int) -> MenuItem: ...
    @classmethod
    def new_section(cls, label: str | None, section: MenuModel) -> MenuItem: ...
    @classmethod
    def new_submenu(cls, label: str | None, submenu: MenuModel) -> MenuItem: ...
    def set_action_and_target_value(
        self, action: str | None = None, target_value: GLib.Variant | None = None
    ) -> None: ...
    # override
    def set_attribute(self, attributes: list[tuple[str, str, Any]]) -> None: ...
    def set_attribute_value(
        self, attribute: str, value: GLib.Variant | None = None
    ) -> None: ...
    def set_detailed_action(self, detailed_action: str) -> None: ...
    def set_icon(self, icon: Icon) -> None: ...
    def set_label(self, label: str | None = None) -> None: ...
    def set_link(self, link: str, model: MenuModel | None = None) -> None: ...
    def set_section(self, section: MenuModel | None = None) -> None: ...
    def set_submenu(self, submenu: MenuModel | None = None) -> None: ...

class MenuLinkIter(GObject.Object):
    """
    :Constructors:

    ::

        MenuLinkIter(**properties)

    Object GMenuLinkIter

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> MenuLinkIterPrivate: ...
    def do_get_next(self) -> tuple[bool, str, MenuModel]: ...
    def get_name(self) -> str: ...
    def get_next(self) -> tuple[bool, str, MenuModel]: ...
    def get_value(self) -> MenuModel: ...
    def next(self) -> bool: ...

class MenuLinkIterClass(_gi.Struct):
    """
    :Constructors:

    ::

        MenuLinkIterClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_next(self) -> Callable[[MenuLinkIter], tuple[bool, str, MenuModel]]: ...

class MenuLinkIterPrivate(_gi.Struct): ...

class MenuModel(GObject.Object):
    """
    :Constructors:

    ::

        MenuModel(**properties)

    Object GMenuModel

    Signals from GMenuModel:
      items-changed (gint, gint, gint)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> MenuModelPrivate: ...
    def do_get_item_attribute_value(
        self, item_index: int, attribute: str, expected_type: GLib.VariantType | None, /
    ) -> GLib.Variant | None: ...
    def do_get_item_attributes(self, item_index: int, /) -> dict[str, GLib.Variant]: ...
    def do_get_item_link(self, item_index: int, link: str, /) -> MenuModel | None: ...
    def do_get_item_links(self, item_index: int, /) -> dict[str, MenuModel]: ...
    def do_get_n_items(self) -> int: ...
    def do_is_mutable(self) -> bool: ...
    def do_iterate_item_attributes(self, item_index: int, /) -> MenuAttributeIter: ...
    def do_iterate_item_links(self, item_index: int, /) -> MenuLinkIter: ...
    def get_item_attribute_value(
        self,
        item_index: int,
        attribute: str,
        expected_type: GLib.VariantType | None = None,
    ) -> GLib.Variant | None: ...
    def get_item_link(self, item_index: int, link: str) -> MenuModel | None: ...
    def get_n_items(self) -> int: ...
    def is_mutable(self) -> bool: ...
    def items_changed(self, position: int, removed: int, added: int) -> None: ...
    def iterate_item_attributes(self, item_index: int) -> MenuAttributeIter: ...
    def iterate_item_links(self, item_index: int) -> MenuLinkIter: ...

class MenuModelClass(_gi.Struct):
    """
    :Constructors:

    ::

        MenuModelClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def is_mutable(self) -> Callable[[MenuModel], bool]: ...
    @property
    def get_n_items(self) -> Callable[[MenuModel], int]: ...
    @property
    def get_item_attributes(
        self,
    ) -> Callable[[MenuModel, int], dict[str, GLib.Variant]]: ...
    @property
    def iterate_item_attributes(
        self,
    ) -> Callable[[MenuModel, int], MenuAttributeIter]: ...
    @property
    def get_item_attribute_value(
        self,
    ) -> Callable[
        [MenuModel, int, str, GLib.VariantType | None], GLib.Variant | None
    ]: ...
    @property
    def get_item_links(self) -> Callable[[MenuModel, int], dict[str, MenuModel]]: ...
    @property
    def iterate_item_links(self) -> Callable[[MenuModel, int], MenuLinkIter]: ...
    @property
    def get_item_link(self) -> Callable[[MenuModel, int, str], MenuModel | None]: ...

class MenuModelPrivate(_gi.Struct): ...

class Mount(GObject.GInterface, Protocol):
    """
    Interface GMount

    Signals from GObject:
      notify (GParam)
    """
    def can_eject(self) -> bool: ...
    def can_unmount(self) -> bool: ...
    @overload
    def eject(
        self, flags: _MountUnmountFlagsValueType, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def eject(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Mount, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Mount] | None,
    ) -> None: ...
    def eject_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Mount, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Mount] | None,
    ) -> None: ...
    def eject_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def get_default_location(self) -> File: ...
    def get_drive(self) -> Drive | None: ...
    def get_icon(self) -> Icon: ...
    def get_name(self) -> str: ...
    def get_root(self) -> File: ...
    def get_sort_key(self) -> str | None: ...
    def get_symbolic_icon(self) -> Icon: ...
    def get_uuid(self) -> str | None: ...
    def get_volume(self) -> Volume | None: ...
    @overload
    def guess_content_type(
        self, force_rescan: bool, cancellable: Cancellable | None = None
    ) -> _gi.Async[list[str]]: ...
    @overload
    def guess_content_type(
        self,
        force_rescan: bool,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Mount, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def guess_content_type(
        self,
        force_rescan: bool,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Mount] | None,
    ) -> None: ...
    def guess_content_type_finish(self, result: AsyncResult) -> list[str]: ...
    def guess_content_type_sync(
        self, force_rescan: bool, cancellable: Cancellable | None = None
    ) -> list[str]: ...
    def is_shadowed(self) -> bool: ...
    @overload
    def remount(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def remount(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Mount, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def remount(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Mount] | None,
    ) -> None: ...
    def remount_finish(self, result: AsyncResult) -> bool: ...
    def shadow(self) -> None: ...
    @overload
    def unmount(
        self, flags: _MountUnmountFlagsValueType, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def unmount(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Mount, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def unmount(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Mount] | None,
    ) -> None: ...
    def unmount_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def unmount_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def unmount_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Mount, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def unmount_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Mount] | None,
    ) -> None: ...
    def unmount_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def unshadow(self) -> None: ...

class MountIface(_gi.Struct):
    """
    :Constructors:

    ::

        MountIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def changed(self) -> Callable[[Mount], None]: ...
    @property
    def unmounted(self) -> Callable[[Mount], None]: ...
    @property
    def get_root(self) -> Callable[[Mount], File]: ...
    @property
    def get_name(self) -> Callable[[Mount], str]: ...
    @property
    def get_icon(self) -> Callable[[Mount], Icon]: ...
    @property
    def get_uuid(self) -> Callable[[Mount], str | None]: ...
    @property
    def get_volume(self) -> Callable[[Mount], Volume | None]: ...
    @property
    def get_drive(self) -> Callable[[Mount], Drive | None]: ...
    @property
    def can_unmount(self) -> Callable[[Mount], bool]: ...
    @property
    def can_eject(self) -> Callable[[Mount], bool]: ...
    @property
    def unmount(
        self,
    ) -> Callable[
        [
            Mount,
            _MountUnmountFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def unmount_finish(self) -> Callable[[Mount, AsyncResult], bool]: ...
    @property
    def eject(
        self,
    ) -> Callable[
        [
            Mount,
            _MountUnmountFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_finish(self) -> Callable[[Mount, AsyncResult], bool]: ...
    @property
    def remount(
        self,
    ) -> Callable[
        [
            Mount,
            _MountMountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def remount_finish(self) -> Callable[[Mount, AsyncResult], bool]: ...
    @property
    def guess_content_type(
        self,
    ) -> Callable[
        [
            Mount,
            bool,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def guess_content_type_finish(
        self,
    ) -> Callable[[Mount, AsyncResult], list[str]]: ...
    @property
    def guess_content_type_sync(
        self,
    ) -> Callable[[Mount, bool, Cancellable | None], list[str]]: ...
    @property
    def pre_unmount(self) -> Callable[[Mount], None]: ...
    @property
    def unmount_with_operation(
        self,
    ) -> Callable[
        [
            Mount,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def unmount_with_operation_finish(self) -> Callable[[Mount, AsyncResult], bool]: ...
    @property
    def eject_with_operation(
        self,
    ) -> Callable[
        [
            Mount,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_with_operation_finish(self) -> Callable[[Mount, AsyncResult], bool]: ...
    @property
    def get_default_location(self) -> Callable[[Mount], File]: ...
    @property
    def get_sort_key(self) -> Callable[[Mount], str | None]: ...
    @property
    def get_symbolic_icon(self) -> Callable[[Mount], Icon]: ...

class MountOperation(GObject.Object):
    """
    :Constructors:

    ::

        MountOperation(**properties)
        new() -> Gio.MountOperation

    Object GMountOperation

    Signals from GMountOperation:
      ask-password (gchararray, gchararray, gchararray, GAskPasswordFlags)
      ask-question (gchararray, GStrv)
      reply (GMountOperationResult)
      aborted ()
      show-processes (gchararray, GArray, GStrv)
      show-unmount-progress (gchararray, gint64, gint64)

    Properties from GMountOperation:
      username -> gchararray: username
      password -> gchararray: password
      anonymous -> gboolean: anonymous
      domain -> gchararray: domain
      password-save -> GPasswordSave: password-save
      choice -> gint: choice
      is-tcrypt-hidden-volume -> gboolean: is-tcrypt-hidden-volume
      is-tcrypt-system-volume -> gboolean: is-tcrypt-system-volume
      pim -> guint: pim

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        anonymous: bool
        choice: int
        domain: str | None
        is_tcrypt_hidden_volume: bool
        is_tcrypt_system_volume: bool
        password: str | None
        @property
        def password_save(self) -> PasswordSave: ...
        @password_save.setter
        def password_save(self, value: _PasswordSaveValueType) -> None: ...
        pim: int
        username: str | None

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> MountOperationPrivate: ...
    def __init__(
        self,
        *,
        anonymous: bool = ...,
        choice: int = ...,
        domain: str | None = ...,
        is_tcrypt_hidden_volume: bool = ...,
        is_tcrypt_system_volume: bool = ...,
        password: str | None = ...,
        password_save: _PasswordSaveValueType = ...,
        pim: int = ...,
        username: str | None = ...,
    ) -> None: ...
    def do_aborted(self) -> None: ...
    def do_ask_password(
        self,
        message: str,
        default_user: str,
        default_domain: str,
        flags: _AskPasswordFlagsValueType,
        /,
    ) -> None: ...
    def do_ask_question(self, message: str, choices: Sequence[str], /) -> None: ...
    def do_reply(self, result: _MountOperationResultValueType, /) -> None: ...
    def do_show_processes(
        self, message: str, processes: Sequence[int], choices: Sequence[str], /
    ) -> None: ...
    def do_show_unmount_progress(
        self, message: str, time_left: int, bytes_left: int, /
    ) -> None: ...
    def get_anonymous(self) -> bool: ...
    def get_choice(self) -> int: ...
    def get_domain(self) -> str | None: ...
    def get_is_tcrypt_hidden_volume(self) -> bool: ...
    def get_is_tcrypt_system_volume(self) -> bool: ...
    def get_password(self) -> str | None: ...
    def get_password_save(self) -> PasswordSave: ...
    def get_pim(self) -> int: ...
    def get_username(self) -> str | None: ...
    @classmethod
    def new(cls) -> MountOperation: ...
    def reply(self, result: _MountOperationResultValueType) -> None: ...
    def set_anonymous(self, anonymous: bool) -> None: ...
    def set_choice(self, choice: int) -> None: ...
    def set_domain(self, domain: str | None = None) -> None: ...
    def set_is_tcrypt_hidden_volume(self, hidden_volume: bool) -> None: ...
    def set_is_tcrypt_system_volume(self, system_volume: bool) -> None: ...
    def set_password(self, password: str | None = None) -> None: ...
    def set_password_save(self, save: _PasswordSaveValueType) -> None: ...
    def set_pim(self, pim: int) -> None: ...
    def set_username(self, username: str | None = None) -> None: ...

class MountOperationClass(_gi.Struct):
    """
    :Constructors:

    ::

        MountOperationClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def ask_password(
        self,
    ) -> Callable[
        [MountOperation, str, str, str, _AskPasswordFlagsValueType], None
    ]: ...
    @property
    def ask_question(self) -> Callable[[MountOperation, str, Sequence[str]], None]: ...
    @property
    def reply(
        self,
    ) -> Callable[[MountOperation, _MountOperationResultValueType], None]: ...
    @property
    def aborted(self) -> Callable[[MountOperation], None]: ...
    @property
    def show_processes(
        self,
    ) -> Callable[[MountOperation, str, Sequence[int], Sequence[str]], None]: ...
    @property
    def show_unmount_progress(
        self,
    ) -> Callable[[MountOperation, str, int, int], None]: ...

class MountOperationPrivate(_gi.Struct): ...

class NativeSocketAddress(SocketAddress):
    """
    :Constructors:

    ::

        NativeSocketAddress(**properties)
        new(native=None, len:int) -> Gio.SocketAddress

    Object GNativeSocketAddress

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> SocketAddress: ...
    @property
    def priv(self) -> NativeSocketAddressPrivate: ...
    @classmethod
    def new(cls, native: int | Any | None, len: int) -> NativeSocketAddress: ...

class NativeSocketAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        NativeSocketAddressClass()
    """
    @property
    def parent_class(self) -> SocketAddressClass: ...

class NativeSocketAddressPrivate(_gi.Struct): ...

class NativeVolumeMonitor(VolumeMonitor):
    """
    :Constructors:

    ::

        NativeVolumeMonitor(**properties)

    Object GNativeVolumeMonitor

    Signals from GVolumeMonitor:
      volume-added (GVolume)
      volume-removed (GVolume)
      volume-changed (GVolume)
      mount-added (GMount)
      mount-removed (GMount)
      mount-pre-unmount (GMount)
      mount-changed (GMount)
      drive-connected (GDrive)
      drive-disconnected (GDrive)
      drive-changed (GDrive)
      drive-eject-button (GDrive)
      drive-stop-button (GDrive)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> VolumeMonitor: ...

class NativeVolumeMonitorClass(_gi.Struct):
    """
    :Constructors:

    ::

        NativeVolumeMonitorClass()
    """
    @property
    def parent_class(self) -> VolumeMonitorClass: ...
    @property
    def get_mount_for_mount_path(self) -> int: ...

class NetworkAddress(GObject.Object, SocketConnectable):
    """
    :Constructors:

    ::

        NetworkAddress(**properties)
        new(hostname:str, port:int) -> Gio.NetworkAddress
        new_loopback(port:int) -> Gio.NetworkAddress

    Object GNetworkAddress

    Properties from GNetworkAddress:
      hostname -> gchararray: hostname
      port -> guint: port
      scheme -> gchararray: scheme

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def hostname(self) -> str: ...
        @property
        def port(self) -> int: ...
        @property
        def scheme(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> NetworkAddressPrivate: ...
    def __init__(
        self, *, hostname: str | None = ..., port: int = ..., scheme: str | None = ...
    ) -> None: ...
    def get_hostname(self) -> str: ...
    def get_port(self) -> int: ...
    def get_scheme(self) -> str | None: ...
    @classmethod
    def new(cls, hostname: str, port: int) -> NetworkAddress: ...
    @classmethod
    def new_loopback(cls, port: int) -> NetworkAddress: ...
    @staticmethod
    def parse(host_and_port: str, default_port: int) -> NetworkAddress: ...
    @staticmethod
    def parse_uri(uri: str, default_port: int) -> NetworkAddress: ...

class NetworkAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        NetworkAddressClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class NetworkAddressPrivate(_gi.Struct): ...

class NetworkMonitor(GObject.GInterface, Protocol):
    """
    Interface GNetworkMonitor

    Signals from GObject:
      notify (GParam)
    """
    def can_reach(
        self, connectable: SocketConnectable, cancellable: Cancellable | None = None
    ) -> bool: ...
    @overload
    def can_reach_async(
        self, connectable: SocketConnectable, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def can_reach_async(
        self,
        connectable: SocketConnectable,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[NetworkMonitor, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def can_reach_async(
        self,
        connectable: SocketConnectable,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[NetworkMonitor] | None,
    ) -> None: ...
    def can_reach_finish(self, result: AsyncResult) -> bool: ...
    def get_connectivity(self) -> NetworkConnectivity: ...
    @staticmethod
    def get_default() -> NetworkMonitor: ...
    def get_network_available(self) -> bool: ...
    def get_network_metered(self) -> bool: ...

class NetworkMonitorInterface(_gi.Struct):
    """
    :Constructors:

    ::

        NetworkMonitorInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def network_changed(self) -> Callable[[NetworkMonitor, bool], None]: ...
    @property
    def can_reach(
        self,
    ) -> Callable[[NetworkMonitor, SocketConnectable, Cancellable | None], bool]: ...
    @property
    def can_reach_async(
        self,
    ) -> Callable[
        [
            NetworkMonitor,
            SocketConnectable,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def can_reach_finish(self) -> Callable[[NetworkMonitor, AsyncResult], bool]: ...

class NetworkService(GObject.Object, SocketConnectable):
    """
    :Constructors:

    ::

        NetworkService(**properties)
        new(service:str, protocol:str, domain:str) -> Gio.NetworkService

    Object GNetworkService

    Properties from GNetworkService:
      service -> gchararray: service
      protocol -> gchararray: protocol
      domain -> gchararray: domain
      scheme -> gchararray: scheme

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def domain(self) -> str: ...
        @property
        def protocol(self) -> str: ...
        scheme: str
        @property
        def service(self) -> str: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> NetworkServicePrivate: ...
    def __init__(
        self,
        *,
        domain: str | None = ...,
        protocol: str | None = ...,
        scheme: str = ...,
        service: str | None = ...,
    ) -> None: ...
    def get_domain(self) -> str: ...
    def get_protocol(self) -> str: ...
    def get_scheme(self) -> str: ...
    def get_service(self) -> str: ...
    @classmethod
    def new(cls, service: str, protocol: str, domain: str) -> NetworkService: ...
    def set_scheme(self, scheme: str) -> None: ...

class NetworkServiceClass(_gi.Struct):
    """
    :Constructors:

    ::

        NetworkServiceClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class NetworkServicePrivate(_gi.Struct): ...

class Notification(GObject.Object):
    """
    :Constructors:

    ::

        Notification(**properties)
        new(title:str) -> Gio.Notification

    Object GNotification

    Signals from GObject:
      notify (GParam)
    """
    def add_button(self, label: str, detailed_action: str) -> None: ...
    def add_button_with_target(
        self, label: str, action: str, target: GLib.Variant | None = None
    ) -> None: ...
    @classmethod
    def new(cls, title: str) -> Notification: ...
    def set_body(self, body: str | None = None) -> None: ...
    def set_category(self, category: str | None = None) -> None: ...
    def set_default_action(self, detailed_action: str) -> None: ...
    def set_default_action_and_target(
        self, action: str, target: GLib.Variant | None = None
    ) -> None: ...
    def set_icon(self, icon: Icon) -> None: ...
    def set_priority(self, priority: _NotificationPriorityValueType) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_urgent(self, urgent: bool) -> None: ...

class OutputMessage(_gi.Struct):
    """
    :Constructors:

    ::

        OutputMessage()
    """

    address: SocketAddress
    vectors: OutputVector
    num_vectors: int
    bytes_sent: int
    control_messages: list[SocketControlMessage]
    num_control_messages: int

class OutputStream(GObject.Object):
    """
    :Constructors:

    ::

        OutputStream(**properties)

    Object GOutputStream

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> OutputStreamPrivate: ...
    def clear_pending(self) -> None: ...
    def close(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def close_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def close_finish(self, result: AsyncResult) -> bool: ...
    def do_close_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[OutputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_close_finish(self, result: AsyncResult, /) -> bool: ...
    def do_close_fn(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_flush(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_flush_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[OutputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_flush_finish(self, result: AsyncResult, /) -> bool: ...
    def do_splice(
        self,
        source: InputStream,
        flags: _OutputStreamSpliceFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> int: ...
    def do_splice_async(
        self,
        source: InputStream,
        flags: _OutputStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[OutputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_splice_finish(self, result: AsyncResult, /) -> int: ...
    def do_write_async(
        self,
        buffer: Sequence[int] | None,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[OutputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_write_finish(self, result: AsyncResult, /) -> int: ...
    def do_write_fn(
        self, buffer: Sequence[int] | None, cancellable: Cancellable | None, /
    ) -> int: ...
    def do_writev_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[OutputStream, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_writev_finish(self, result: AsyncResult, /) -> tuple[bool, int]: ...
    def do_writev_fn(
        self, vectors: Sequence[OutputVector], cancellable: Cancellable | None, /
    ) -> tuple[bool, int]: ...
    def flush(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def flush_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def flush_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def flush_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def flush_finish(self, result: AsyncResult) -> bool: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def is_closing(self) -> bool: ...
    def set_pending(self) -> bool: ...
    def splice(
        self,
        source: InputStream,
        flags: _OutputStreamSpliceFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> int: ...
    @overload
    def splice_async(
        self,
        source: InputStream,
        flags: _OutputStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[int]: ...
    @overload
    def splice_async(
        self,
        source: InputStream,
        flags: _OutputStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def splice_async(
        self,
        source: InputStream,
        flags: _OutputStreamSpliceFlagsValueType,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def splice_finish(self, result: AsyncResult) -> int: ...
    def write(
        self, buffer: Sequence[int], cancellable: Cancellable | None = None
    ) -> int: ...
    def write_all(
        self, buffer: Sequence[int], cancellable: Cancellable | None = None
    ) -> tuple[bool, int]: ...
    @overload
    def write_all_async(
        self,
        buffer: Sequence[int],
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[bool, int]]: ...
    @overload
    def write_all_async(
        self,
        buffer: Sequence[int],
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def write_all_async(
        self,
        buffer: Sequence[int],
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def write_all_finish(self, result: AsyncResult) -> tuple[bool, int]: ...
    @overload
    def write_async(
        self,
        buffer: Sequence[int],
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[int]: ...
    @overload
    def write_async(
        self,
        buffer: Sequence[int],
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def write_async(
        self,
        buffer: Sequence[int],
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def write_bytes(
        self, bytes: GLib.Bytes, cancellable: Cancellable | None = None
    ) -> int: ...
    @overload
    def write_bytes_async(
        self,
        bytes: GLib.Bytes,
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[int]: ...
    @overload
    def write_bytes_async(
        self,
        bytes: GLib.Bytes,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def write_bytes_async(
        self,
        bytes: GLib.Bytes,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def write_bytes_finish(self, result: AsyncResult) -> int: ...
    def write_finish(self, result: AsyncResult) -> int: ...
    def writev(
        self, vectors: Sequence[OutputVector], cancellable: Cancellable | None = None
    ) -> tuple[bool, int]: ...
    def writev_all(
        self, vectors: Sequence[OutputVector], cancellable: Cancellable | None = None
    ) -> tuple[bool, int]: ...
    @overload
    def writev_all_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[bool, int]]: ...
    @overload
    def writev_all_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def writev_all_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def writev_all_finish(self, result: AsyncResult) -> tuple[bool, int]: ...
    @overload
    def writev_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[bool, int]]: ...
    @overload
    def writev_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[OutputStream, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def writev_async(
        self,
        vectors: Sequence[OutputVector],
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[OutputStream] | None,
    ) -> None: ...
    def writev_finish(self, result: AsyncResult) -> tuple[bool, int]: ...

class OutputStreamClass(_gi.Struct):
    """
    :Constructors:

    ::

        OutputStreamClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def write_fn(
        self,
    ) -> Callable[
        [OutputStream, Sequence[int] | None, int, Cancellable | None], int
    ]: ...
    @property
    def splice(
        self,
    ) -> Callable[
        [
            OutputStream,
            InputStream,
            _OutputStreamSpliceFlagsValueType,
            Cancellable | None,
        ],
        int,
    ]: ...
    @property
    def flush(self) -> Callable[[OutputStream, Cancellable | None], bool]: ...
    @property
    def close_fn(self) -> Callable[[OutputStream, Cancellable | None], bool]: ...
    @property
    def write_async(
        self,
    ) -> Callable[
        [
            OutputStream,
            Sequence[int] | None,
            int,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def write_finish(self) -> Callable[[OutputStream, AsyncResult], int]: ...
    @property
    def splice_async(
        self,
    ) -> Callable[
        [
            OutputStream,
            InputStream,
            _OutputStreamSpliceFlagsValueType,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def splice_finish(self) -> Callable[[OutputStream, AsyncResult], int]: ...
    @property
    def flush_async(
        self,
    ) -> Callable[
        [
            OutputStream,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def flush_finish(self) -> Callable[[OutputStream, AsyncResult], bool]: ...
    @property
    def close_async(
        self,
    ) -> Callable[
        [
            OutputStream,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def close_finish(self) -> Callable[[OutputStream, AsyncResult], bool]: ...
    @property
    def writev_fn(
        self,
    ) -> Callable[
        [OutputStream, Sequence[OutputVector], int, Cancellable | None],
        tuple[bool, int],
    ]: ...
    @property
    def writev_async(
        self,
    ) -> Callable[
        [
            OutputStream,
            Sequence[OutputVector],
            int,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def writev_finish(
        self,
    ) -> Callable[[OutputStream, AsyncResult], tuple[bool, int]]: ...

class OutputStreamPrivate(_gi.Struct): ...

class OutputVector(_gi.Struct):
    """
    :Constructors:

    ::

        OutputVector()
    """

    buffer: int
    size: int

class Permission(GObject.Object):
    """
    :Constructors:

    ::

        Permission(**properties)

    Object GPermission

    Properties from GPermission:
      allowed -> gboolean: allowed
      can-acquire -> gboolean: can-acquire
      can-release -> gboolean: can-release

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def allowed(self) -> bool: ...
        @property
        def can_acquire(self) -> bool: ...
        @property
        def can_release(self) -> bool: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> PermissionPrivate: ...
    def acquire(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def acquire_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def acquire_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Permission, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def acquire_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Permission] | None,
    ) -> None: ...
    def acquire_finish(self, result: AsyncResult) -> bool: ...
    def do_acquire(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_acquire_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Permission, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_acquire_finish(self, result: AsyncResult, /) -> bool: ...
    def do_release(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_release_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Permission, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_release_finish(self, result: AsyncResult, /) -> bool: ...
    def get_allowed(self) -> bool: ...
    def get_can_acquire(self) -> bool: ...
    def get_can_release(self) -> bool: ...
    def impl_update(
        self, allowed: bool, can_acquire: bool, can_release: bool
    ) -> None: ...
    def release(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def release_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def release_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Permission, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def release_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Permission] | None,
    ) -> None: ...
    def release_finish(self, result: AsyncResult) -> bool: ...

class PermissionClass(_gi.Struct):
    """
    :Constructors:

    ::

        PermissionClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def acquire(self) -> Callable[[Permission, Cancellable | None], bool]: ...
    @property
    def acquire_async(
        self,
    ) -> Callable[
        [
            Permission,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def acquire_finish(self) -> Callable[[Permission, AsyncResult], bool]: ...
    @property
    def release(self) -> Callable[[Permission, Cancellable | None], bool]: ...
    @property
    def release_async(
        self,
    ) -> Callable[
        [
            Permission,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def release_finish(self) -> Callable[[Permission, AsyncResult], bool]: ...
    @property
    def reserved(self) -> list[int]: ...

class PermissionPrivate(_gi.Struct): ...

class PollableInputStream(GObject.GInterface, Protocol):
    """
    Interface GPollableInputStream

    Signals from GObject:
      notify (GParam)
    """
    def can_poll(self) -> bool: ...
    def create_source(self, cancellable: Cancellable | None = None) -> GLib.Source: ...
    def is_readable(self) -> bool: ...
    def read_nonblocking(
        self, cancellable: Cancellable | None = None
    ) -> tuple[int, bytes]: ...

class PollableInputStreamInterface(_gi.Struct):
    """
    :Constructors:

    ::

        PollableInputStreamInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def can_poll(self) -> Callable[[PollableInputStream], bool]: ...
    @property
    def is_readable(self) -> Callable[[PollableInputStream], bool]: ...
    @property
    def create_source(
        self,
    ) -> Callable[[PollableInputStream, Cancellable | None], GLib.Source]: ...
    @property
    def read_nonblocking(
        self,
    ) -> Callable[[PollableInputStream, int], tuple[int, bytes]]: ...

class PollableOutputStream(GObject.GInterface, Protocol):
    """
    Interface GPollableOutputStream

    Signals from GObject:
      notify (GParam)
    """
    def can_poll(self) -> bool: ...
    def create_source(self, cancellable: Cancellable | None = None) -> GLib.Source: ...
    def is_writable(self) -> bool: ...
    def write_nonblocking(
        self, buffer: Sequence[int], cancellable: Cancellable | None = None
    ) -> int: ...
    def writev_nonblocking(
        self, vectors: Sequence[OutputVector], cancellable: Cancellable | None = None
    ) -> tuple[PollableReturn, int]: ...

class PollableOutputStreamInterface(_gi.Struct):
    """
    :Constructors:

    ::

        PollableOutputStreamInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def can_poll(self) -> Callable[[PollableOutputStream], bool]: ...
    @property
    def is_writable(self) -> Callable[[PollableOutputStream], bool]: ...
    @property
    def create_source(
        self,
    ) -> Callable[[PollableOutputStream, Cancellable | None], GLib.Source]: ...
    @property
    def write_nonblocking(
        self,
    ) -> Callable[[PollableOutputStream, Sequence[int] | None, int], int]: ...
    @property
    def writev_nonblocking(
        self,
    ) -> Callable[
        [PollableOutputStream, Sequence[OutputVector], int], tuple[PollableReturn, int]
    ]: ...

class PowerProfileMonitor(GObject.GInterface, Protocol):
    """
    Interface GPowerProfileMonitor

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def dup_default() -> PowerProfileMonitor: ...
    def get_power_saver_enabled(self) -> bool: ...

class PowerProfileMonitorInterface(_gi.Struct):
    """
    :Constructors:

    ::

        PowerProfileMonitorInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...

class PropertyAction(GObject.Object, Action):
    """
    :Constructors:

    ::

        PropertyAction(**properties)
        new(name:str, object:GObject.Object, property_name:str) -> Gio.PropertyAction

    Object GPropertyAction

    Properties from GPropertyAction:
      name -> gchararray: name
      parameter-type -> GVariantType: parameter-type
      enabled -> gboolean: enabled
      state-type -> GVariantType: state-type
      state -> GVariant: state
      object -> GObject: object
      property-name -> gchararray: property-name
      invert-boolean -> gboolean: invert-boolean

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def enabled(self) -> bool: ...
        @property
        def invert_boolean(self) -> bool: ...
        @property
        def name(self) -> str | None: ...
        @property
        def parameter_type(self) -> GLib.VariantType | None: ...
        @property
        def state(self) -> GLib.Variant | None: ...
        @property
        def state_type(self) -> GLib.VariantType | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        invert_boolean: bool = ...,
        name: str | None = ...,
        object: GObject.Object | None = ...,
        property_name: str | None = ...,
    ) -> None: ...
    @classmethod
    def new(
        cls, name: str, object: GObject.Object, property_name: str
    ) -> PropertyAction: ...

class Proxy(GObject.GInterface, Protocol):
    """
    Interface GProxy

    Signals from GObject:
      notify (GParam)
    """
    def connect(
        self,
        connection: IOStream,
        proxy_address: ProxyAddress,
        cancellable: Cancellable | None = None,
    ) -> IOStream: ...
    @overload
    def connect_async(
        self,
        connection: IOStream,
        proxy_address: ProxyAddress,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[IOStream]: ...
    @overload
    def connect_async(
        self,
        connection: IOStream,
        proxy_address: ProxyAddress,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Proxy, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def connect_async(
        self,
        connection: IOStream,
        proxy_address: ProxyAddress,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Proxy] | None,
    ) -> None: ...
    def connect_finish(self, result: AsyncResult) -> IOStream: ...
    @staticmethod
    def get_default_for_protocol(protocol: str) -> Proxy | None: ...
    def supports_hostname(self) -> bool: ...

class ProxyAddress(InetSocketAddress):
    """
    :Constructors:

    ::

        ProxyAddress(**properties)
        new(inetaddr:Gio.InetAddress, port:int, protocol:str, dest_hostname:str, dest_port:int, username:str=None, password:str=None) -> Gio.SocketAddress

    Object GProxyAddress

    Properties from GProxyAddress:
      protocol -> gchararray: protocol
      destination-protocol -> gchararray: destination-protocol
      destination-hostname -> gchararray: destination-hostname
      destination-port -> guint: destination-port
      username -> gchararray: username
      password -> gchararray: password
      uri -> gchararray: uri

    Properties from GInetSocketAddress:
      address -> GInetAddress: address
      port -> guint: port
      flowinfo -> guint: flowinfo
      scope-id -> guint: scope-id

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(InetSocketAddress.Props):
        @property
        def destination_hostname(self) -> str: ...
        @property
        def destination_port(self) -> int: ...
        @property
        def destination_protocol(self) -> str: ...
        @property
        def password(self) -> str | None: ...
        @property
        def protocol(self) -> str: ...
        @property
        def uri(self) -> str | None: ...
        @property
        def username(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> InetSocketAddress: ...
    @property
    def priv(self) -> ProxyAddressPrivate: ...
    def __init__(
        self,
        *,
        destination_hostname: str | None = ...,
        destination_port: int = ...,
        destination_protocol: str | None = ...,
        password: str | None = ...,
        protocol: str | None = ...,
        uri: str | None = ...,
        username: str | None = ...,
        address: InetAddress | None = ...,
        flowinfo: int = ...,
        port: int = ...,
        scope_id: int = ...,
    ) -> None: ...
    def get_destination_hostname(self) -> str: ...
    def get_destination_port(self) -> int: ...
    def get_destination_protocol(self) -> str: ...
    def get_password(self) -> str | None: ...
    def get_protocol(self) -> str: ...
    def get_uri(self) -> str | None: ...
    def get_username(self) -> str | None: ...
    @classmethod
    def new(
        cls,
        inetaddr: InetAddress,
        port: int,
        protocol: str,
        dest_hostname: str,
        dest_port: int,
        username: str | None = None,
        password: str | None = None,
    ) -> ProxyAddress: ...

class ProxyAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        ProxyAddressClass()
    """
    @property
    def parent_class(self) -> InetSocketAddressClass: ...

class ProxyAddressEnumerator(SocketAddressEnumerator):
    """
    :Constructors:

    ::

        ProxyAddressEnumerator(**properties)

    Object GProxyAddressEnumerator

    Properties from GProxyAddressEnumerator:
      uri -> gchararray: uri
      default-port -> guint: default-port
      connectable -> GSocketConnectable: connectable
      proxy-resolver -> GProxyResolver: proxy-resolver

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketAddressEnumerator.Props):
        @property
        def connectable(self) -> SocketConnectable | None: ...
        @property
        def default_port(self) -> int: ...
        proxy_resolver: ProxyResolver | None
        @property
        def uri(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketAddressEnumerator: ...
    @property
    def priv(self) -> ProxyAddressEnumeratorPrivate: ...
    def __init__(
        self,
        *,
        connectable: SocketConnectable | None = ...,
        default_port: int = ...,
        proxy_resolver: ProxyResolver | None = ...,
        uri: str | None = ...,
    ) -> None: ...

class ProxyAddressEnumeratorClass(_gi.Struct):
    """
    :Constructors:

    ::

        ProxyAddressEnumeratorClass()
    """
    @property
    def parent_class(self) -> SocketAddressEnumeratorClass: ...

class ProxyAddressEnumeratorPrivate(_gi.Struct): ...
class ProxyAddressPrivate(_gi.Struct): ...

class ProxyInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ProxyInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def connect(
        self,
    ) -> Callable[[Proxy, IOStream, ProxyAddress, Cancellable | None], IOStream]: ...
    @property
    def connect_async(
        self,
    ) -> Callable[
        [
            Proxy,
            IOStream,
            ProxyAddress,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def connect_finish(self) -> Callable[[Proxy, AsyncResult], IOStream]: ...
    @property
    def supports_hostname(self) -> Callable[[Proxy], bool]: ...

class ProxyResolver(GObject.GInterface, Protocol):
    """
    Interface GProxyResolver

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get_default() -> ProxyResolver: ...
    def is_supported(self) -> bool: ...
    def lookup(self, uri: str, cancellable: Cancellable | None = None) -> list[str]: ...
    @overload
    def lookup_async(
        self, uri: str, cancellable: Cancellable | None = None
    ) -> _gi.Async[list[str]]: ...
    @overload
    def lookup_async(
        self,
        uri: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[ProxyResolver, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_async(
        self,
        uri: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[ProxyResolver] | None,
    ) -> None: ...
    def lookup_finish(self, result: AsyncResult) -> list[str]: ...

class ProxyResolverInterface(_gi.Struct):
    """
    :Constructors:

    ::

        ProxyResolverInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def is_supported(self) -> Callable[[ProxyResolver], bool]: ...
    @property
    def lookup(
        self,
    ) -> Callable[[ProxyResolver, str, Cancellable | None], list[str]]: ...
    @property
    def lookup_async(
        self,
    ) -> Callable[
        [
            ProxyResolver,
            str,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_finish(self) -> Callable[[ProxyResolver, AsyncResult], list[str]]: ...

class RemoteActionGroup(GObject.GInterface, Protocol):
    """
    Interface GRemoteActionGroup

    Signals from GObject:
      notify (GParam)
    """
    def activate_action_full(
        self,
        action_name: str,
        parameter: GLib.Variant | None,
        platform_data: GLib.Variant,
    ) -> None: ...
    def change_action_state_full(
        self, action_name: str, value: GLib.Variant, platform_data: GLib.Variant
    ) -> None: ...

class RemoteActionGroupInterface(_gi.Struct):
    """
    :Constructors:

    ::

        RemoteActionGroupInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def activate_action_full(
        self,
    ) -> Callable[
        [RemoteActionGroup, str, GLib.Variant | None, GLib.Variant], None
    ]: ...
    @property
    def change_action_state_full(
        self,
    ) -> Callable[[RemoteActionGroup, str, GLib.Variant, GLib.Variant], None]: ...

class Resolver(GObject.Object):
    """
    :Constructors:

    ::

        Resolver(**properties)

    Object GResolver

    Signals from GResolver:
      reload ()

    Properties from GResolver:
      timeout -> guint: timeout

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        timeout: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> ResolverPrivate: ...
    def __init__(self, *, timeout: int = ...) -> None: ...
    def do_lookup_by_address(
        self, address: InetAddress, cancellable: Cancellable | None, /
    ) -> str: ...
    def do_lookup_by_address_async(
        self,
        address: InetAddress,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Resolver, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_by_address_finish(self, result: AsyncResult, /) -> str: ...
    def do_lookup_by_name(
        self, hostname: str, cancellable: Cancellable | None, /
    ) -> list[InetAddress]: ...
    def do_lookup_by_name_async(
        self,
        hostname: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Resolver, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_by_name_finish(self, result: AsyncResult, /) -> list[InetAddress]: ...
    def do_lookup_by_name_with_flags(
        self,
        hostname: str,
        flags: _ResolverNameLookupFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> list[InetAddress]: ...
    def do_lookup_by_name_with_flags_async(
        self,
        hostname: str,
        flags: _ResolverNameLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Resolver, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_by_name_with_flags_finish(
        self, result: AsyncResult, /
    ) -> list[InetAddress]: ...
    def do_lookup_records(
        self,
        rrname: str,
        record_type: _ResolverRecordTypeValueType,
        cancellable: Cancellable | None,
        /,
    ) -> list[GLib.Variant]: ...
    def do_lookup_records_async(
        self,
        rrname: str,
        record_type: _ResolverRecordTypeValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Resolver, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_records_finish(
        self, result: AsyncResult, /
    ) -> list[GLib.Variant]: ...
    def do_lookup_service_async(
        self,
        rrname: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[Resolver, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_service_finish(self, result: AsyncResult, /) -> list[SrvTarget]: ...
    def do_reload(self) -> None: ...
    @staticmethod
    def get_default() -> Resolver: ...
    def get_timeout(self) -> int: ...
    def lookup_by_address(
        self, address: InetAddress, cancellable: Cancellable | None = None
    ) -> str: ...
    @overload
    def lookup_by_address_async(
        self, address: InetAddress, cancellable: Cancellable | None = None
    ) -> _gi.Async[str]: ...
    @overload
    def lookup_by_address_async(
        self,
        address: InetAddress,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Resolver, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_by_address_async(
        self,
        address: InetAddress,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Resolver] | None,
    ) -> None: ...
    def lookup_by_address_finish(self, result: AsyncResult) -> str: ...
    def lookup_by_name(
        self, hostname: str, cancellable: Cancellable | None = None
    ) -> list[InetAddress]: ...
    @overload
    def lookup_by_name_async(
        self, hostname: str, cancellable: Cancellable | None = None
    ) -> _gi.Async[list[InetAddress]]: ...
    @overload
    def lookup_by_name_async(
        self,
        hostname: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Resolver, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_by_name_async(
        self,
        hostname: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Resolver] | None,
    ) -> None: ...
    def lookup_by_name_finish(self, result: AsyncResult) -> list[InetAddress]: ...
    def lookup_by_name_with_flags(
        self,
        hostname: str,
        flags: _ResolverNameLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> list[InetAddress]: ...
    @overload
    def lookup_by_name_with_flags_async(
        self,
        hostname: str,
        flags: _ResolverNameLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[list[InetAddress]]: ...
    @overload
    def lookup_by_name_with_flags_async(
        self,
        hostname: str,
        flags: _ResolverNameLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Resolver, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_by_name_with_flags_async(
        self,
        hostname: str,
        flags: _ResolverNameLookupFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Resolver] | None,
    ) -> None: ...
    def lookup_by_name_with_flags_finish(
        self, result: AsyncResult
    ) -> list[InetAddress]: ...
    def lookup_records(
        self,
        rrname: str,
        record_type: _ResolverRecordTypeValueType,
        cancellable: Cancellable | None = None,
    ) -> list[GLib.Variant]: ...
    @overload
    def lookup_records_async(
        self,
        rrname: str,
        record_type: _ResolverRecordTypeValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[list[GLib.Variant]]: ...
    @overload
    def lookup_records_async(
        self,
        rrname: str,
        record_type: _ResolverRecordTypeValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Resolver, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_records_async(
        self,
        rrname: str,
        record_type: _ResolverRecordTypeValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Resolver] | None,
    ) -> None: ...
    def lookup_records_finish(self, result: AsyncResult) -> list[GLib.Variant]: ...
    def lookup_service(
        self,
        service: str,
        protocol: str,
        domain: str,
        cancellable: Cancellable | None = None,
    ) -> list[SrvTarget]: ...
    @overload
    def lookup_service_async(
        self,
        service: str,
        protocol: str,
        domain: str,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[list[SrvTarget]]: ...
    @overload
    def lookup_service_async(
        self,
        service: str,
        protocol: str,
        domain: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Resolver, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_service_async(
        self,
        service: str,
        protocol: str,
        domain: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Resolver] | None,
    ) -> None: ...
    def lookup_service_finish(self, result: AsyncResult) -> list[SrvTarget]: ...
    def set_default(self) -> None: ...
    def set_timeout(self, timeout_ms: int) -> None: ...

class ResolverClass(_gi.Struct):
    """
    :Constructors:

    ::

        ResolverClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def reload(self) -> Callable[[Resolver], None]: ...
    @property
    def lookup_by_name(
        self,
    ) -> Callable[[Resolver, str, Cancellable | None], list[InetAddress]]: ...
    @property
    def lookup_by_name_async(
        self,
    ) -> Callable[
        [
            Resolver,
            str,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_by_name_finish(
        self,
    ) -> Callable[[Resolver, AsyncResult], list[InetAddress]]: ...
    @property
    def lookup_by_address(
        self,
    ) -> Callable[[Resolver, InetAddress, Cancellable | None], str]: ...
    @property
    def lookup_by_address_async(
        self,
    ) -> Callable[
        [
            Resolver,
            InetAddress,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_by_address_finish(self) -> Callable[[Resolver, AsyncResult], str]: ...
    @property
    def lookup_service(self) -> int: ...
    @property
    def lookup_service_async(
        self,
    ) -> Callable[
        [
            Resolver,
            str,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_service_finish(
        self,
    ) -> Callable[[Resolver, AsyncResult], list[SrvTarget]]: ...
    @property
    def lookup_records(
        self,
    ) -> Callable[
        [Resolver, str, _ResolverRecordTypeValueType, Cancellable | None],
        list[GLib.Variant],
    ]: ...
    @property
    def lookup_records_async(
        self,
    ) -> Callable[
        [
            Resolver,
            str,
            _ResolverRecordTypeValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_records_finish(
        self,
    ) -> Callable[[Resolver, AsyncResult], list[GLib.Variant]]: ...
    @property
    def lookup_by_name_with_flags_async(
        self,
    ) -> Callable[
        [
            Resolver,
            str,
            _ResolverNameLookupFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_by_name_with_flags_finish(
        self,
    ) -> Callable[[Resolver, AsyncResult], list[InetAddress]]: ...
    @property
    def lookup_by_name_with_flags(
        self,
    ) -> Callable[
        [Resolver, str, _ResolverNameLookupFlagsValueType, Cancellable | None],
        list[InetAddress],
    ]: ...

class ResolverPrivate(_gi.Struct): ...

class Resource(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_data(data:GLib.Bytes) -> Gio.Resource
    """
    def enumerate_children(
        self, path: str, lookup_flags: _ResourceLookupFlagsValueType
    ) -> list[str]: ...
    def get_info(
        self, path: str, lookup_flags: _ResourceLookupFlagsValueType
    ) -> tuple[bool, int, int]: ...
    def has_children(self, path: str) -> bool: ...
    @staticmethod
    def load(filename: str) -> Resource: ...
    def lookup_data(
        self, path: str, lookup_flags: _ResourceLookupFlagsValueType
    ) -> GLib.Bytes: ...
    @classmethod
    def new_from_data(cls, data: GLib.Bytes) -> Resource: ...
    def open_stream(
        self, path: str, lookup_flags: _ResourceLookupFlagsValueType
    ) -> InputStream: ...
    def ref(self) -> Resource: ...
    def unref(self) -> None: ...

class Seekable(GObject.GInterface, Protocol):
    """
    Interface GSeekable

    Signals from GObject:
      notify (GParam)
    """
    def can_seek(self) -> bool: ...
    def can_truncate(self) -> bool: ...
    def seek(
        self, offset: int, type: GLib.SeekType, cancellable: Cancellable | None = None
    ) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, offset: int, cancellable: Cancellable | None = None) -> bool: ...

class SeekableIface(_gi.Struct):
    """
    :Constructors:

    ::

        SeekableIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def tell(self) -> Callable[[Seekable], int]: ...
    @property
    def can_seek(self) -> Callable[[Seekable], bool]: ...
    @property
    def seek(
        self,
    ) -> Callable[[Seekable, int, GLib.SeekType, Cancellable | None], bool]: ...
    @property
    def can_truncate(self) -> Callable[[Seekable], bool]: ...
    @property
    def truncate_fn(self) -> Callable[[Seekable, int, Cancellable | None], bool]: ...

class Settings(GObject.Object):
    """
    Provide dictionary-like access to GLib.Settings.

    Object GSettings

    Provide dictionary-like access to GLib.Settings.

    Signals from GSettings:
      changed (gchararray)
      change-event (gpointer, gint) -> gboolean
      writable-changed (gchararray)
      writable-change-event (guint) -> gboolean

    Properties from GSettings:
      settings-schema -> GSettingsSchema: settings-schema
      schema -> gchararray: schema
      schema-id -> gchararray: schema-id
      backend -> GSettingsBackend: backend
      path -> gchararray: path
      has-unapplied -> gboolean: has-unapplied
      delay-apply -> gboolean: delay-apply

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def backend(self) -> SettingsBackend | None: ...
        @property
        def delay_apply(self) -> bool: ...
        @property
        def has_unapplied(self) -> bool: ...
        @property
        def path(self) -> str | None: ...
        @property
        def schema(self) -> str | None: ...
        @property
        def schema_id(self) -> str | None: ...
        @property
        def settings_schema(self) -> SettingsSchema | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SettingsPrivate: ...
    def __init__(
        self,
        *,
        backend: SettingsBackend | None = ...,
        path: str | None = ...,
        schema: str | None = ...,
        schema_id: str | None = ...,
        settings_schema: SettingsSchema | None = ...,
    ) -> None: ...
    def __bool__(self): ...  # FIXME: Override is missing typing annotation
    def __contains__(self, key): ...  # FIXME: Override is missing typing annotation
    def __getitem__(self, key): ...  # FIXME: Override is missing typing annotation
    def __iter__(self): ...  # FIXME: Override is missing typing annotation
    def __len__(self): ...  # FIXME: Override is missing typing annotation
    def __setitem__(
        self, key, value
    ): ...  # FIXME: Override is missing typing annotation
    def apply(self) -> None: ...
    def bind(
        self,
        key: str,
        object: GObject.Object,
        property: str,
        flags: _SettingsBindFlagsValueType,
    ) -> None: ...
    def bind_with_mapping(
        self,
        key: str,
        object: GObject.Object,
        property: str,
        flags: _SettingsBindFlagsValueType,
        get_mapping: Callable[..., Any] | None = None,
        set_mapping: Callable[..., Any] | None = None,
    ) -> None: ...
    def bind_writable(
        self, key: str, object: GObject.Object, property: str, inverted: bool
    ) -> None: ...
    def create_action(self, key: str) -> Action: ...
    def delay(self) -> None: ...
    def do_change_event(self, keys: int, n_keys: int, /) -> bool: ...
    def do_changed(self, key: str, /) -> None: ...
    def do_writable_change_event(self, key: int, /) -> bool: ...
    def do_writable_changed(self, key: str, /) -> None: ...
    def get_boolean(self, key: str) -> bool: ...
    def get_child(self, name: str) -> Settings: ...
    def get_default_value(self, key: str) -> GLib.Variant | None: ...
    def get_double(self, key: str) -> float: ...
    def get_enum(self, key: str) -> int: ...
    def get_flags(self, key: str) -> int: ...
    def get_has_unapplied(self) -> bool: ...
    def get_int(self, key: str) -> int: ...
    def get_int64(self, key: str) -> int: ...
    def get_mapped(
        self,
        key: str,
        mapping: Callable[[GLib.Variant | None, Unpack[_DataTs]], tuple[bool, int]],
        *user_data: Unpack[_DataTs],
    ) -> int: ...
    def get_range(self, key: str) -> GLib.Variant: ...
    def get_string(self, key: str) -> str: ...
    def get_strv(self, key: str) -> list[str]: ...
    def get_uint(self, key: str) -> int: ...
    def get_uint64(self, key: str) -> int: ...
    def get_user_value(self, key: str) -> GLib.Variant | None: ...
    def get_value(self, key: str) -> GLib.Variant: ...
    def is_writable(self, name: str) -> bool: ...
    def keys(self): ...  # FIXME: Override is missing typing annotation
    def list_children(self) -> list[str]: ...
    def list_keys(self) -> list[str]: ...
    @staticmethod
    def list_relocatable_schemas() -> list[str]: ...
    @staticmethod
    def list_schemas() -> list[str]: ...
    @classmethod
    def new(cls, schema_id: str) -> Settings: ...
    @classmethod
    def new_full(
        cls,
        schema: SettingsSchema,
        backend: SettingsBackend | None = None,
        path: str | None = None,
    ) -> Settings: ...
    @classmethod
    def new_with_backend(cls, schema_id: str, backend: SettingsBackend) -> Settings: ...
    @classmethod
    def new_with_backend_and_path(
        cls, schema_id: str, backend: SettingsBackend, path: str
    ) -> Settings: ...
    @classmethod
    def new_with_path(cls, schema_id: str, path: str) -> Settings: ...
    def range_check(self, key: str, value: GLib.Variant) -> bool: ...
    def reset(self, key: str) -> None: ...
    def revert(self) -> None: ...
    def set_boolean(self, key: str, value: bool) -> bool: ...
    def set_double(self, key: str, value: float) -> bool: ...
    def set_enum(self, key: str, value: int) -> bool: ...
    def set_flags(self, key: str, value: int) -> bool: ...
    def set_int(self, key: str, value: int) -> bool: ...
    def set_int64(self, key: str, value: int) -> bool: ...
    def set_string(self, key: str, value: str) -> bool: ...
    def set_strv(self, key: str, value: Sequence[str] | None = None) -> bool: ...
    def set_uint(self, key: str, value: int) -> bool: ...
    def set_uint64(self, key: str, value: int) -> bool: ...
    def set_value(self, key: str, value: GLib.Variant) -> bool: ...
    @staticmethod
    def sync() -> None: ...
    @staticmethod
    def unbind(object: GObject.Object, property: str) -> None: ...

class SettingsBackend(GObject.Object):
    """
    :Constructors:

    ::

        SettingsBackend(**properties)

    Object GSettingsBackend

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SettingsBackendPrivate: ...
    def changed(self, key: str, origin_tag: int | Any | None = None) -> None: ...
    def changed_tree(
        self, tree: GLib.Tree, origin_tag: int | Any | None = None
    ) -> None: ...
    def do_get_writable(self, key: str, /) -> bool: ...
    def do_read(
        self, key: str, expected_type: GLib.VariantType, default_value: bool, /
    ) -> GLib.Variant: ...
    def do_read_user_value(
        self, key: str, expected_type: GLib.VariantType, /
    ) -> GLib.Variant: ...
    def do_reset(self, key: str, origin_tag: int | Any | None, /) -> None: ...
    def do_subscribe(self, name: str, /) -> None: ...
    def do_sync(self) -> None: ...
    def do_unsubscribe(self, name: str, /) -> None: ...
    def do_write(
        self, key: str, value: GLib.Variant, origin_tag: int | Any | None, /
    ) -> bool: ...
    def do_write_tree(
        self, tree: GLib.Tree, origin_tag: int | Any | None, /
    ) -> bool: ...
    @staticmethod
    def flatten_tree(tree: GLib.Tree) -> tuple[str, list[str], list[GLib.Variant]]: ...
    @staticmethod
    def get_default() -> SettingsBackend: ...
    def keys_changed(
        self, path: str, items: Sequence[str], origin_tag: int | Any | None = None
    ) -> None: ...
    def path_changed(self, path: str, origin_tag: int | Any | None = None) -> None: ...
    def path_writable_changed(self, path: str) -> None: ...
    def writable_changed(self, key: str) -> None: ...

class SettingsBackendClass(_gi.Struct):
    """
    :Constructors:

    ::

        SettingsBackendClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def read(
        self,
    ) -> Callable[[SettingsBackend, str, GLib.VariantType, bool], GLib.Variant]: ...
    @property
    def get_writable(self) -> Callable[[SettingsBackend, str], bool]: ...
    @property
    def write(
        self,
    ) -> Callable[[SettingsBackend, str, GLib.Variant, Any | None], bool]: ...
    @property
    def write_tree(
        self,
    ) -> Callable[[SettingsBackend, GLib.Tree, Any | None], bool]: ...
    @property
    def reset(self) -> Callable[[SettingsBackend, str, Any | None], None]: ...
    @property
    def subscribe(self) -> Callable[[SettingsBackend, str], None]: ...
    @property
    def unsubscribe(self) -> Callable[[SettingsBackend, str], None]: ...
    @property
    def sync(self) -> Callable[[SettingsBackend], None]: ...
    @property
    def get_permission(self) -> int: ...
    @property
    def read_user_value(
        self,
    ) -> Callable[[SettingsBackend, str, GLib.VariantType], GLib.Variant]: ...
    @property
    def padding(self) -> list[int]: ...

class SettingsBackendPrivate(_gi.Struct): ...

class SettingsClass(_gi.Struct):
    """
    :Constructors:

    ::

        SettingsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def writable_changed(self) -> Callable[[Settings, str], None]: ...
    @property
    def changed(self) -> Callable[[Settings, str], None]: ...
    @property
    def writable_change_event(self) -> Callable[[Settings, int], bool]: ...
    @property
    def change_event(self) -> Callable[[Settings, int, int], bool]: ...
    @property
    def padding(self) -> list[int]: ...

class SettingsPrivate(_gi.Struct): ...

class SettingsSchema(GObject.GBoxed):
    def get_id(self) -> str: ...
    def get_key(self, name: str) -> SettingsSchemaKey: ...
    def get_path(self) -> str | None: ...
    def has_key(self, name: str) -> bool: ...
    def list_children(self) -> list[str]: ...
    def list_keys(self) -> list[str]: ...
    def ref(self) -> SettingsSchema: ...
    def unref(self) -> None: ...

class SettingsSchemaKey(GObject.GBoxed):
    def get_default_value(self) -> GLib.Variant: ...
    def get_description(self) -> str | None: ...
    def get_name(self) -> str: ...
    def get_range(self) -> GLib.Variant: ...
    def get_summary(self) -> str | None: ...
    def get_value_type(self) -> GLib.VariantType: ...
    def range_check(self, value: GLib.Variant) -> bool: ...
    def ref(self) -> SettingsSchemaKey: ...
    def unref(self) -> None: ...

class SettingsSchemaSource(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_directory(directory:str, parent:Gio.SettingsSchemaSource=None, trusted:bool) -> Gio.SettingsSchemaSource
    """
    @staticmethod
    def get_default() -> SettingsSchemaSource | None: ...
    def list_schemas(self, recursive: bool) -> tuple[list[str], list[str]]: ...
    def lookup(self, schema_id: str, recursive: bool) -> SettingsSchema | None: ...
    @classmethod
    def new_from_directory(
        cls, directory: str, parent: SettingsSchemaSource | None, trusted: bool
    ) -> SettingsSchemaSource: ...
    def ref(self) -> SettingsSchemaSource: ...
    def unref(self) -> None: ...

class SimpleAction(GObject.Object, Action):
    """
    :Constructors:

    ::

        SimpleAction(**properties)
        new(name:str, parameter_type:GLib.VariantType=None) -> Gio.SimpleAction
        new_stateful(name:str, parameter_type:GLib.VariantType=None, state:GLib.Variant) -> Gio.SimpleAction

    Object GSimpleAction

    Signals from GSimpleAction:
      activate (GVariant)
      change-state (GVariant)

    Properties from GSimpleAction:
      name -> gchararray: name
      parameter-type -> GVariantType: parameter-type
      enabled -> gboolean: enabled
      state-type -> GVariantType: state-type
      state -> GVariant: state

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        enabled: bool
        @property
        def name(self) -> str | None: ...
        @property
        def parameter_type(self) -> GLib.VariantType | None: ...
        @property
        def state(self) -> GLib.Variant | None: ...
        @state.setter
        def state(self, value: GLib.Variant) -> None: ...
        @property
        def state_type(self) -> GLib.VariantType | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        enabled: bool = ...,
        name: str | None = ...,
        parameter_type: GLib.VariantType | None = ...,
        state: GLib.Variant = ...,
    ) -> None: ...
    @classmethod
    def new(
        cls, name: str, parameter_type: GLib.VariantType | None = None
    ) -> SimpleAction: ...
    @classmethod
    def new_stateful(
        cls, name: str, parameter_type: GLib.VariantType | None, state: GLib.Variant
    ) -> SimpleAction: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_state(self, value: GLib.Variant) -> None: ...
    def set_state_hint(self, state_hint: GLib.Variant | None = None) -> None: ...

class SimpleActionGroup(GObject.Object, ActionGroup, ActionMap):
    """
    :Constructors:

    ::

        SimpleActionGroup(**properties)
        new() -> Gio.SimpleActionGroup

    Object GSimpleActionGroup

    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SimpleActionGroupPrivate: ...
    def add_entries(
        self, entries: Sequence[ActionEntry], user_data: int | Any | None = None
    ) -> None: ...
    def insert(self, action: Action) -> None: ...
    def lookup(self, action_name: str) -> Action: ...
    @classmethod
    def new(cls) -> SimpleActionGroup: ...
    def remove(self, action_name: str) -> None: ...

class SimpleActionGroupClass(_gi.Struct):
    """
    :Constructors:

    ::

        SimpleActionGroupClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def padding(self) -> list[int]: ...

class SimpleActionGroupPrivate(_gi.Struct): ...

class SimpleAsyncResult(GObject.Object, AsyncResult):
    """
    :Constructors:

    ::

        SimpleAsyncResult(**properties)
        new(source_object:GObject.Object=None, callback:Gio.AsyncReadyCallback=None, user_data=None, source_tag=None) -> Gio.SimpleAsyncResult
        new_from_error(source_object:GObject.Object=None, callback:Gio.AsyncReadyCallback=None, user_data=None, error:error) -> Gio.SimpleAsyncResult

    Object GSimpleAsyncResult

    Signals from GObject:
      notify (GParam)
    """
    def complete(self) -> None: ...
    def complete_in_idle(self) -> None: ...
    def get_op_res_gboolean(self) -> bool: ...
    def get_op_res_gssize(self) -> int: ...
    @staticmethod
    def is_valid(
        result: AsyncResult,
        source: GObject.Object | None = None,
        source_tag: int | Any | None = None,
    ) -> bool: ...
    @classmethod
    def new(
        cls,
        source_object: GObject.Object | None = None,
        callback: _AsyncReadyCallback[SimpleAsyncResult, Any | None] | None = None,
        user_data: Any | None = None,
        source_tag: int | Any | None = None,
    ) -> SimpleAsyncResult: ...
    @classmethod
    def new_from_error(
        cls,
        source_object: GObject.Object | None,
        callback: _AsyncReadyCallback[SimpleAsyncResult, Any | None] | None,
        user_data: Any | None,
        error: GLib.Error,
    ) -> SimpleAsyncResult: ...
    def propagate_error(self) -> bool: ...
    def set_check_cancellable(
        self, check_cancellable: Cancellable | None = None
    ) -> None: ...
    def set_from_error(self, error: GLib.Error) -> None: ...
    def set_handle_cancellation(self, handle_cancellation: bool) -> None: ...
    def set_op_res_gboolean(self, op_res: bool) -> None: ...
    def set_op_res_gssize(self, op_res: int) -> None: ...

class SimpleAsyncResultClass(_gi.Struct): ...

class SimpleIOStream(IOStream):
    """
    :Constructors:

    ::

        SimpleIOStream(**properties)
        new(input_stream:Gio.InputStream, output_stream:Gio.OutputStream) -> Gio.IOStream

    Object GSimpleIOStream

    Properties from GSimpleIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(IOStream.Props):
        @property
        def input_stream(self) -> InputStream | None: ...
        @property
        def output_stream(self) -> OutputStream | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        input_stream: InputStream | None = ...,
        output_stream: OutputStream | None = ...,
    ) -> None: ...
    @classmethod
    def new(
        cls, input_stream: InputStream, output_stream: OutputStream
    ) -> SimpleIOStream: ...

class SimplePermission(Permission):
    """
    :Constructors:

    ::

        SimplePermission(**properties)
        new(allowed:bool) -> Gio.Permission

    Object GSimplePermission

    Properties from GPermission:
      allowed -> gboolean: allowed
      can-acquire -> gboolean: can-acquire
      can-release -> gboolean: can-release

    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def new(cls, allowed: bool) -> SimplePermission: ...

class SimpleProxyResolver(GObject.Object, ProxyResolver):
    """
    :Constructors:

    ::

        SimpleProxyResolver(**properties)

    Object GSimpleProxyResolver

    Properties from GSimpleProxyResolver:
      default-proxy -> gchararray: default-proxy
      ignore-hosts -> GStrv: ignore-hosts

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        default_proxy: str | None
        @property
        def ignore_hosts(self) -> list[str]: ...
        @ignore_hosts.setter
        def ignore_hosts(self, value: Sequence[str]) -> None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SimpleProxyResolverPrivate: ...
    def __init__(
        self, *, default_proxy: str | None = ..., ignore_hosts: Sequence[str] = ...
    ) -> None: ...
    @staticmethod
    def new(
        default_proxy: str | None = None, ignore_hosts: Sequence[str] | None = None
    ) -> ProxyResolver: ...
    def set_default_proxy(self, default_proxy: str | None = None) -> None: ...
    def set_ignore_hosts(self, ignore_hosts: Sequence[str]) -> None: ...
    def set_uri_proxy(self, uri_scheme: str, proxy: str) -> None: ...

class SimpleProxyResolverClass(_gi.Struct):
    """
    :Constructors:

    ::

        SimpleProxyResolverClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class SimpleProxyResolverPrivate(_gi.Struct): ...

class Socket(GObject.Object, DatagramBased, Initable):
    """
    :Constructors:

    ::

        Socket(**properties)
        new(family:Gio.SocketFamily, type:Gio.SocketType, protocol:Gio.SocketProtocol) -> Gio.Socket
        new_from_fd(fd:int) -> Gio.Socket

    Object GSocket

    Properties from GSocket:
      family -> GSocketFamily: family
      type -> GSocketType: type
      protocol -> GSocketProtocol: protocol
      fd -> gint: fd
      blocking -> gboolean: blocking
      listen-backlog -> gint: listen-backlog
      keepalive -> gboolean: keepalive
      local-address -> GSocketAddress: local-address
      remote-address -> GSocketAddress: remote-address
      timeout -> guint: timeout
      ttl -> guint: ttl
      broadcast -> gboolean: broadcast
      multicast-loopback -> gboolean: multicast-loopback
      multicast-ttl -> guint: multicast-ttl

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        blocking: bool
        broadcast: bool
        @property
        def family(self) -> SocketFamily: ...
        @property
        def fd(self) -> int: ...
        keepalive: bool
        listen_backlog: int
        @property
        def local_address(self) -> SocketAddress: ...
        multicast_loopback: bool
        multicast_ttl: int
        @property
        def protocol(self) -> SocketProtocol: ...
        @property
        def remote_address(self) -> SocketAddress: ...
        timeout: int
        ttl: int
        @property
        def type(self) -> SocketType: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SocketPrivate: ...
    def __init__(
        self,
        *,
        blocking: bool = ...,
        broadcast: bool = ...,
        family: _SocketFamilyValueType = ...,
        fd: int = ...,
        keepalive: bool = ...,
        listen_backlog: int = ...,
        multicast_loopback: bool = ...,
        multicast_ttl: int = ...,
        protocol: _SocketProtocolValueType = ...,
        timeout: int = ...,
        ttl: int = ...,
        type: _SocketTypeValueType = ...,
    ) -> None: ...
    def accept(self, cancellable: Cancellable | None = None) -> Socket: ...
    def bind(self, address: SocketAddress, allow_reuse: bool) -> bool: ...
    def check_connect_result(self) -> bool: ...
    def close(self) -> bool: ...
    def condition_check(
        self, condition: GLib._IOConditionValueType
    ) -> GLib.IOCondition: ...
    def condition_timed_wait(
        self,
        condition: GLib._IOConditionValueType,
        timeout_us: int,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def condition_wait(
        self,
        condition: GLib._IOConditionValueType,
        cancellable: Cancellable | None = None,
    ) -> bool: ...
    def connect(
        self, address: SocketAddress, cancellable: Cancellable | None = None
    ) -> bool: ...
    def connection_factory_create_connection(self) -> SocketConnection: ...
    def get_available_bytes(self) -> int: ...
    def get_blocking(self) -> bool: ...
    def get_broadcast(self) -> bool: ...
    def get_credentials(self) -> Credentials: ...
    def get_family(self) -> SocketFamily: ...
    def get_fd(self) -> int: ...
    def get_keepalive(self) -> bool: ...
    def get_listen_backlog(self) -> int: ...
    def get_local_address(self) -> SocketAddress: ...
    def get_multicast_loopback(self) -> bool: ...
    def get_multicast_ttl(self) -> int: ...
    def get_option(self, level: int, optname: int) -> tuple[bool, int]: ...
    def get_protocol(self) -> SocketProtocol: ...
    def get_remote_address(self) -> SocketAddress: ...
    def get_socket_type(self) -> SocketType: ...
    def get_timeout(self) -> int: ...
    def get_ttl(self) -> int: ...
    def is_closed(self) -> bool: ...
    def is_connected(self) -> bool: ...
    def join_multicast_group(
        self, group: InetAddress, source_specific: bool, iface: str | None = None
    ) -> bool: ...
    def join_multicast_group_ssm(
        self,
        group: InetAddress,
        source_specific: InetAddress | None = None,
        iface: str | None = None,
    ) -> bool: ...
    def leave_multicast_group(
        self, group: InetAddress, source_specific: bool, iface: str | None = None
    ) -> bool: ...
    def leave_multicast_group_ssm(
        self,
        group: InetAddress,
        source_specific: InetAddress | None = None,
        iface: str | None = None,
    ) -> bool: ...
    def listen(self) -> bool: ...
    @classmethod
    def new(
        cls,
        family: _SocketFamilyValueType,
        type: _SocketTypeValueType,
        protocol: _SocketProtocolValueType,
    ) -> Socket: ...
    @classmethod
    def new_from_fd(cls, fd: int) -> Socket: ...
    def receive(self, cancellable: Cancellable | None = None) -> tuple[int, bytes]: ...
    def receive_bytes(
        self, size: int, timeout_us: int, cancellable: Cancellable | None = None
    ) -> GLib.Bytes: ...
    def receive_bytes_from(
        self, size: int, timeout_us: int, cancellable: Cancellable | None = None
    ) -> tuple[GLib.Bytes, SocketAddress]: ...
    def receive_from(
        self, cancellable: Cancellable | None = None
    ) -> tuple[int, SocketAddress, bytes]: ...
    def receive_message(
        self,
        vectors: Sequence[InputVector],
        flags: int,
        cancellable: Cancellable | None = None,
    ) -> tuple[int, SocketAddress, list[SocketControlMessage], int]: ...
    def receive_messages(
        self,
        messages: Sequence[InputMessage],
        flags: int,
        cancellable: Cancellable | None = None,
    ) -> int: ...
    def receive_with_blocking(
        self, blocking: bool, cancellable: Cancellable | None = None
    ) -> tuple[int, bytes]: ...
    def send(
        self, buffer: Sequence[int], cancellable: Cancellable | None = None
    ) -> int: ...
    def send_message(
        self,
        address: SocketAddress | None,
        vectors: Sequence[OutputVector],
        messages: Sequence[SocketControlMessage] | None,
        flags: int,
        cancellable: Cancellable | None = None,
    ) -> int: ...
    def send_message_with_timeout(
        self,
        address: SocketAddress | None,
        vectors: Sequence[OutputVector],
        messages: Sequence[SocketControlMessage] | None,
        flags: int,
        timeout_us: int,
        cancellable: Cancellable | None = None,
    ) -> tuple[PollableReturn, int]: ...
    def send_messages(
        self,
        messages: Sequence[OutputMessage],
        flags: int,
        cancellable: Cancellable | None = None,
    ) -> int: ...
    def send_to(
        self,
        address: SocketAddress | None,
        buffer: Sequence[int],
        cancellable: Cancellable | None = None,
    ) -> int: ...
    def send_with_blocking(
        self,
        buffer: Sequence[int],
        blocking: bool,
        cancellable: Cancellable | None = None,
    ) -> int: ...
    def set_blocking(self, blocking: bool) -> None: ...
    def set_broadcast(self, broadcast: bool) -> None: ...
    def set_keepalive(self, keepalive: bool) -> None: ...
    def set_listen_backlog(self, backlog: int) -> None: ...
    def set_multicast_loopback(self, loopback: bool) -> None: ...
    def set_multicast_ttl(self, ttl: int) -> None: ...
    def set_option(self, level: int, optname: int, value: int) -> bool: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_ttl(self, ttl: int) -> None: ...
    def shutdown(self, shutdown_read: bool, shutdown_write: bool) -> bool: ...
    def speaks_ipv4(self) -> bool: ...

class SocketAddress(GObject.Object, SocketConnectable):
    """
    :Constructors:

    ::

        SocketAddress(**properties)
        new_from_native(native, len:int) -> Gio.SocketAddress

    Object GSocketAddress

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def family(self) -> SocketFamily: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_get_family(self) -> SocketFamily: ...
    def do_get_native_size(self) -> int: ...
    def do_to_native(self, dest: int | Any | None, destlen: int, /) -> bool: ...
    def get_family(self) -> SocketFamily: ...
    def get_native_size(self) -> int: ...
    @classmethod
    def new_from_native(cls, native: int | Any | None, len: int) -> SocketAddress: ...
    def to_native(self, dest: int | Any | None, destlen: int) -> bool: ...

class SocketAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketAddressClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_family(self) -> Callable[[SocketAddress], SocketFamily]: ...
    @property
    def get_native_size(self) -> Callable[[SocketAddress], int]: ...
    @property
    def to_native(self) -> Callable[[SocketAddress, Any | None, int], bool]: ...

class SocketAddressEnumerator(GObject.Object):
    """
    :Constructors:

    ::

        SocketAddressEnumerator(**properties)

    Object GSocketAddressEnumerator

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_next(self, cancellable: Cancellable | None, /) -> SocketAddress | None: ...
    def do_next_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[SocketAddressEnumerator, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_next_finish(self, result: AsyncResult, /) -> SocketAddress | None: ...
    def next(self, cancellable: Cancellable | None = None) -> SocketAddress | None: ...
    @overload
    def next_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[SocketAddress | None]: ...
    @overload
    def next_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketAddressEnumerator, Unpack[_DataTs]]
        | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def next_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketAddressEnumerator] | None,
    ) -> None: ...
    def next_finish(self, result: AsyncResult) -> SocketAddress | None: ...

class SocketAddressEnumeratorClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketAddressEnumeratorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def next(
        self,
    ) -> Callable[
        [SocketAddressEnumerator, Cancellable | None], SocketAddress | None
    ]: ...
    @property
    def next_async(
        self,
    ) -> Callable[
        [
            SocketAddressEnumerator,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def next_finish(
        self,
    ) -> Callable[[SocketAddressEnumerator, AsyncResult], SocketAddress | None]: ...

class SocketClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class SocketClient(GObject.Object):
    """
    :Constructors:

    ::

        SocketClient(**properties)
        new() -> Gio.SocketClient

    Object GSocketClient

    Signals from GSocketClient:
      event (GSocketClientEvent, GSocketConnectable, GIOStream)

    Properties from GSocketClient:
      family -> GSocketFamily: family
      type -> GSocketType: type
      protocol -> GSocketProtocol: protocol
      local-address -> GSocketAddress: local-address
      timeout -> guint: timeout
      enable-proxy -> gboolean: enable-proxy
      tls -> gboolean: tls
      tls-validation-flags -> GTlsCertificateFlags: tls-validation-flags
      proxy-resolver -> GProxyResolver: proxy-resolver

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        enable_proxy: bool
        @property
        def family(self) -> SocketFamily: ...
        @family.setter
        def family(self, value: _SocketFamilyValueType) -> None: ...
        local_address: SocketAddress | None
        @property
        def protocol(self) -> SocketProtocol: ...
        @protocol.setter
        def protocol(self, value: _SocketProtocolValueType) -> None: ...
        @property
        def proxy_resolver(self) -> ProxyResolver: ...
        @proxy_resolver.setter
        def proxy_resolver(self, value: ProxyResolver | None) -> None: ...
        timeout: int
        tls: bool
        @property
        def tls_validation_flags(self) -> TlsCertificateFlags: ...
        @tls_validation_flags.setter
        def tls_validation_flags(
            self, value: _TlsCertificateFlagsValueType
        ) -> None: ...
        @property
        def type(self) -> SocketType: ...
        @type.setter
        def type(self, value: _SocketTypeValueType) -> None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SocketClientPrivate: ...
    def __init__(
        self,
        *,
        enable_proxy: bool = ...,
        family: _SocketFamilyValueType = ...,
        local_address: SocketAddress | None = ...,
        protocol: _SocketProtocolValueType = ...,
        proxy_resolver: ProxyResolver | None = ...,
        timeout: int = ...,
        tls: bool = ...,
        tls_validation_flags: _TlsCertificateFlagsValueType = ...,
        type: _SocketTypeValueType = ...,
    ) -> None: ...
    def add_application_proxy(self, protocol: str) -> None: ...
    def connect(
        self, connectable: SocketConnectable, cancellable: Cancellable | None = None
    ) -> SocketConnection: ...
    @overload
    def connect_async(
        self, connectable: SocketConnectable, cancellable: Cancellable | None = None
    ) -> _gi.Async[SocketConnection]: ...
    @overload
    def connect_async(
        self,
        connectable: SocketConnectable,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketClient, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def connect_async(
        self,
        connectable: SocketConnectable,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketClient] | None,
    ) -> None: ...
    def connect_finish(self, result: AsyncResult) -> SocketConnection: ...
    def connect_to_host(
        self,
        host_and_port: str,
        default_port: int,
        cancellable: Cancellable | None = None,
    ) -> SocketConnection: ...
    @overload
    def connect_to_host_async(
        self,
        host_and_port: str,
        default_port: int,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[SocketConnection]: ...
    @overload
    def connect_to_host_async(
        self,
        host_and_port: str,
        default_port: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketClient, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def connect_to_host_async(
        self,
        host_and_port: str,
        default_port: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketClient] | None,
    ) -> None: ...
    def connect_to_host_finish(self, result: AsyncResult) -> SocketConnection: ...
    def connect_to_service(
        self, domain: str, service: str, cancellable: Cancellable | None = None
    ) -> SocketConnection: ...
    @overload
    def connect_to_service_async(
        self, domain: str, service: str, cancellable: Cancellable | None = None
    ) -> _gi.Async[SocketConnection]: ...
    @overload
    def connect_to_service_async(
        self,
        domain: str,
        service: str,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketClient, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def connect_to_service_async(
        self,
        domain: str,
        service: str,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketClient] | None,
    ) -> None: ...
    def connect_to_service_finish(self, result: AsyncResult) -> SocketConnection: ...
    def connect_to_uri(
        self, uri: str, default_port: int, cancellable: Cancellable | None = None
    ) -> SocketConnection: ...
    @overload
    def connect_to_uri_async(
        self, uri: str, default_port: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[SocketConnection]: ...
    @overload
    def connect_to_uri_async(
        self,
        uri: str,
        default_port: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketClient, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def connect_to_uri_async(
        self,
        uri: str,
        default_port: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketClient] | None,
    ) -> None: ...
    def connect_to_uri_finish(self, result: AsyncResult) -> SocketConnection: ...
    def do_event(
        self,
        event: _SocketClientEventValueType,
        connectable: SocketConnectable,
        connection: IOStream,
        /,
    ) -> None: ...
    def get_enable_proxy(self) -> bool: ...
    def get_family(self) -> SocketFamily: ...
    def get_local_address(self) -> SocketAddress | None: ...
    def get_protocol(self) -> SocketProtocol: ...
    def get_proxy_resolver(self) -> ProxyResolver: ...
    def get_socket_type(self) -> SocketType: ...
    def get_timeout(self) -> int: ...
    def get_tls(self) -> bool: ...
    def get_tls_validation_flags(self) -> TlsCertificateFlags: ...
    @classmethod
    def new(cls) -> SocketClient: ...
    def set_enable_proxy(self, enable: bool) -> None: ...
    def set_family(self, family: _SocketFamilyValueType) -> None: ...
    def set_local_address(self, address: SocketAddress | None = None) -> None: ...
    def set_protocol(self, protocol: _SocketProtocolValueType) -> None: ...
    def set_proxy_resolver(
        self, proxy_resolver: ProxyResolver | None = None
    ) -> None: ...
    def set_socket_type(self, type: _SocketTypeValueType) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_tls(self, tls: bool) -> None: ...
    def set_tls_validation_flags(
        self, flags: _TlsCertificateFlagsValueType
    ) -> None: ...

class SocketClientClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketClientClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def event(
        self,
    ) -> Callable[
        [SocketClient, _SocketClientEventValueType, SocketConnectable, IOStream], None
    ]: ...

class SocketClientPrivate(_gi.Struct): ...

class SocketConnectable(GObject.GInterface, Protocol):
    """
    Interface GSocketConnectable

    Signals from GObject:
      notify (GParam)
    """
    def enumerate(self) -> SocketAddressEnumerator: ...
    def proxy_enumerate(self) -> SocketAddressEnumerator: ...
    def to_string(self) -> str: ...

class SocketConnectableIface(_gi.Struct):
    """
    :Constructors:

    ::

        SocketConnectableIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def enumerate(self) -> Callable[[SocketConnectable], SocketAddressEnumerator]: ...
    @property
    def proxy_enumerate(
        self,
    ) -> Callable[[SocketConnectable], SocketAddressEnumerator]: ...
    @property
    def to_string(self) -> Callable[[SocketConnectable], str]: ...

class SocketConnection(IOStream):
    """
    :Constructors:

    ::

        SocketConnection(**properties)

    Object GSocketConnection

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(IOStream.Props):
        @property
        def socket(self) -> Socket: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> IOStream: ...
    @property
    def priv(self) -> SocketConnectionPrivate: ...
    def __init__(self, *, socket: Socket | None = ...) -> None: ...
    def connect(
        self, address: SocketAddress, cancellable: Cancellable | None = None
    ) -> bool: ...
    @overload
    def connect_async(
        self, address: SocketAddress, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def connect_async(
        self,
        address: SocketAddress,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def connect_async(
        self,
        address: SocketAddress,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketConnection] | None,
    ) -> None: ...
    def connect_finish(self, result: AsyncResult) -> bool: ...
    @staticmethod
    def factory_lookup_type(
        family: _SocketFamilyValueType, type: _SocketTypeValueType, protocol_id: int
    ) -> type[Any]: ...
    @staticmethod
    def factory_register_type(
        g_type: type[Any],
        family: _SocketFamilyValueType,
        type: _SocketTypeValueType,
        protocol: int,
    ) -> None: ...
    def get_local_address(self) -> SocketAddress: ...
    def get_remote_address(self) -> SocketAddress: ...
    def get_socket(self) -> Socket: ...
    def is_connected(self) -> bool: ...

class SocketConnectionClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketConnectionClass()
    """
    @property
    def parent_class(self) -> IOStreamClass: ...

class SocketConnectionPrivate(_gi.Struct): ...

class SocketControlMessage(GObject.Object):
    """
    :Constructors:

    ::

        SocketControlMessage(**properties)

    Object GSocketControlMessage

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SocketControlMessagePrivate: ...
    @staticmethod
    def deserialize(
        level: int, type: int, data: Sequence[int]
    ) -> SocketControlMessage | None: ...
    def do_get_level(self) -> int: ...
    def do_get_size(self) -> int: ...
    def do_get_type(self) -> int: ...
    def do_serialize(self, data: int | Any | None, /) -> None: ...
    def get_level(self) -> int: ...
    def get_msg_type(self) -> int: ...
    def get_size(self) -> int: ...
    def serialize(self, data: int | Any | None) -> None: ...

class SocketControlMessageClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketControlMessageClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_size(self) -> Callable[[SocketControlMessage], int]: ...
    @property
    def get_level(self) -> Callable[[SocketControlMessage], int]: ...
    @property
    def get_type(self) -> Callable[[SocketControlMessage], int]: ...
    @property
    def serialize(self) -> Callable[[SocketControlMessage, Any | None], None]: ...
    @property
    def deserialize(self) -> int: ...

class SocketControlMessagePrivate(_gi.Struct): ...

class SocketListener(GObject.Object):
    """
    :Constructors:

    ::

        SocketListener(**properties)
        new() -> Gio.SocketListener

    Object GSocketListener

    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)

    Properties from GSocketListener:
      listen-backlog -> gint: listen-backlog

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        listen_backlog: int

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> SocketListenerPrivate: ...
    def __init__(self, *, listen_backlog: int = ...) -> None: ...
    def accept(
        self, cancellable: Cancellable | None = None
    ) -> tuple[SocketConnection, GObject.Object | None]: ...
    @overload
    def accept_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[SocketConnection, GObject.Object | None]]: ...
    @overload
    def accept_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketListener, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def accept_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketListener] | None,
    ) -> None: ...
    def accept_finish(
        self, result: AsyncResult
    ) -> tuple[SocketConnection, GObject.Object | None]: ...
    def accept_socket(
        self, cancellable: Cancellable | None = None
    ) -> tuple[Socket, GObject.Object | None]: ...
    @overload
    def accept_socket_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[Socket, GObject.Object | None]]: ...
    @overload
    def accept_socket_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[SocketListener, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def accept_socket_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[SocketListener] | None,
    ) -> None: ...
    def accept_socket_finish(
        self, result: AsyncResult
    ) -> tuple[Socket, GObject.Object | None]: ...
    def add_address(
        self,
        address: SocketAddress,
        type: _SocketTypeValueType,
        protocol: _SocketProtocolValueType,
        source_object: GObject.Object | None = None,
    ) -> tuple[bool, SocketAddress]: ...
    def add_any_inet_port(self, source_object: GObject.Object | None = None) -> int: ...
    def add_inet_port(
        self, port: int, source_object: GObject.Object | None = None
    ) -> bool: ...
    def add_socket(
        self, socket: Socket, source_object: GObject.Object | None = None
    ) -> bool: ...
    def close(self) -> None: ...
    def do_changed(self) -> None: ...
    def do_event(
        self, event: _SocketListenerEventValueType, socket: Socket, /
    ) -> None: ...
    @classmethod
    def new(cls) -> SocketListener: ...
    def set_backlog(self, listen_backlog: int) -> None: ...

class SocketListenerClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketListenerClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def changed(self) -> Callable[[SocketListener], None]: ...
    @property
    def event(
        self,
    ) -> Callable[[SocketListener, _SocketListenerEventValueType, Socket], None]: ...

class SocketListenerPrivate(_gi.Struct): ...
class SocketPrivate(_gi.Struct): ...

class SocketService(SocketListener):
    """
    :Constructors:

    ::

        SocketService(**properties)
        new() -> Gio.SocketService

    Object GSocketService

    Signals from GSocketService:
      incoming (GSocketConnection, GObject) -> gboolean

    Properties from GSocketService:
      active -> gboolean: active

    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)

    Properties from GSocketListener:
      listen-backlog -> gint: listen-backlog

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketListener.Props):
        active: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketListener: ...
    @property
    def priv(self) -> SocketServicePrivate: ...
    def __init__(self, *, active: bool = ..., listen_backlog: int = ...) -> None: ...
    def do_incoming(
        self, connection: SocketConnection, source_object: GObject.Object, /
    ) -> bool: ...
    def is_active(self) -> bool: ...
    @classmethod
    def new(cls) -> SocketService: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class SocketServiceClass(_gi.Struct):
    """
    :Constructors:

    ::

        SocketServiceClass()
    """
    @property
    def parent_class(self) -> SocketListenerClass: ...
    @property
    def incoming(
        self,
    ) -> Callable[[SocketService, SocketConnection, GObject.Object], bool]: ...

class SocketServicePrivate(_gi.Struct): ...

class SrvTarget(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(hostname:str, port:int, priority:int, weight:int) -> Gio.SrvTarget
    """
    def __init__(
        self, hostname: str, port: int, priority: int, weight: int
    ) -> None: ...
    def copy(self) -> SrvTarget: ...
    def free(self) -> None: ...
    def get_hostname(self) -> str: ...
    def get_port(self) -> int: ...
    def get_priority(self) -> int: ...
    def get_weight(self) -> int: ...
    @classmethod
    def new(cls, hostname: str, port: int, priority: int, weight: int) -> SrvTarget: ...

class StaticResource(_gi.Struct):
    """
    :Constructors:

    ::

        StaticResource()
    """
    @property
    def data(self) -> int: ...
    @property
    def data_len(self) -> int: ...
    @property
    def resource(self) -> Resource: ...
    @property
    def next(self) -> StaticResource: ...
    @property
    def padding(self) -> int: ...
    def fini(self) -> None: ...
    def get_resource(self) -> Resource: ...
    def init(self) -> None: ...

class Subprocess(GObject.Object, Initable):
    """
    :Constructors:

    ::

        Subprocess(**properties)
        new(argv:list, flags:Gio.SubprocessFlags) -> Gio.Subprocess

    Object GSubprocess

    Properties from GSubprocess:
      flags -> GSubprocessFlags: flags
      argv -> GStrv: argv

    Signals from GObject:
      notify (GParam)
    """
    def __init__(
        self,
        *,
        argv: Sequence[str] | None = ...,
        flags: _SubprocessFlagsValueType = ...,
    ) -> None: ...
    def communicate(
        self,
        stdin_buf: GLib.Bytes | None = None,
        cancellable: Cancellable | None = None,
    ) -> tuple[bool, GLib.Bytes | None, GLib.Bytes | None]: ...
    @overload
    def communicate_async(
        self,
        stdin_buf: GLib.Bytes | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[tuple[bool, GLib.Bytes | None, GLib.Bytes | None]]: ...
    @overload
    def communicate_async(
        self,
        stdin_buf: GLib.Bytes | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Subprocess, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def communicate_async(
        self,
        stdin_buf: GLib.Bytes | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Subprocess] | None,
    ) -> None: ...
    def communicate_finish(
        self, result: AsyncResult
    ) -> tuple[bool, GLib.Bytes | None, GLib.Bytes | None]: ...
    def communicate_utf8(
        self, stdin_buf: str | None = None, cancellable: Cancellable | None = None
    ) -> tuple[bool, str | None, str | None]: ...
    @overload
    def communicate_utf8_async(
        self, stdin_buf: str | None = None, cancellable: Cancellable | None = None
    ) -> _gi.Async[tuple[bool, str | None, str | None]]: ...
    @overload
    def communicate_utf8_async(
        self,
        stdin_buf: str | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Subprocess, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def communicate_utf8_async(
        self,
        stdin_buf: str | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Subprocess] | None,
    ) -> None: ...
    def communicate_utf8_finish(
        self, result: AsyncResult
    ) -> tuple[bool, str | None, str | None]: ...
    def force_exit(self) -> None: ...
    def get_exit_status(self) -> int: ...
    def get_identifier(self) -> str | None: ...
    def get_if_exited(self) -> bool: ...
    def get_if_signaled(self) -> bool: ...
    def get_status(self) -> int: ...
    def get_stderr_pipe(self) -> InputStream | None: ...
    def get_stdin_pipe(self) -> OutputStream | None: ...
    def get_stdout_pipe(self) -> InputStream | None: ...
    def get_successful(self) -> bool: ...
    def get_term_sig(self) -> int: ...
    @classmethod
    def new(
        cls, argv: Sequence[str], flags: _SubprocessFlagsValueType
    ) -> Subprocess: ...
    def send_signal(self, signal_num: int) -> None: ...
    def wait(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def wait_async(self, cancellable: Cancellable | None = None) -> _gi.Async[bool]: ...
    @overload
    def wait_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Subprocess, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def wait_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Subprocess] | None,
    ) -> None: ...
    def wait_check(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def wait_check_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def wait_check_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Subprocess, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def wait_check_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Subprocess] | None,
    ) -> None: ...
    def wait_check_finish(self, result: AsyncResult) -> bool: ...
    def wait_finish(self, result: AsyncResult) -> bool: ...

class SubprocessLauncher(GObject.Object):
    """
    :Constructors:

    ::

        SubprocessLauncher(**properties)
        new(flags:Gio.SubprocessFlags) -> Gio.SubprocessLauncher

    Object GSubprocessLauncher

    Properties from GSubprocessLauncher:
      flags -> GSubprocessFlags: flags

    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *, flags: _SubprocessFlagsValueType = ...) -> None: ...
    def close(self) -> None: ...
    def getenv(self, variable: str) -> str | None: ...
    @classmethod
    def new(cls, flags: _SubprocessFlagsValueType) -> SubprocessLauncher: ...
    def set_cwd(self, cwd: str) -> None: ...
    def set_environ(self, env: Sequence[str]) -> None: ...
    def set_flags(self, flags: _SubprocessFlagsValueType) -> None: ...
    def set_stderr_file_path(self, path: str | None = None) -> None: ...
    def set_stdin_file_path(self, path: str | None = None) -> None: ...
    def set_stdout_file_path(self, path: str | None = None) -> None: ...
    def setenv(self, variable: str, value: str, overwrite: bool) -> None: ...
    def spawnv(self, argv: Sequence[str]) -> Subprocess: ...
    def take_fd(self, source_fd: int, target_fd: int) -> None: ...
    def take_stderr_fd(self, fd: int) -> None: ...
    def take_stdin_fd(self, fd: int) -> None: ...
    def take_stdout_fd(self, fd: int) -> None: ...
    def unsetenv(self, variable: str) -> None: ...

class Task(GObject.Object, AsyncResult):
    """
    :Constructors:

    ::

        Task(**properties)
        new(source_object:GObject.Object=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, callback_data=None) -> Gio.Task

    Object GTask

    Properties from GTask:
      completed -> gboolean: completed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def completed(self) -> bool: ...

    @property
    def props(self) -> Props: ...
    def get_cancellable(self) -> Cancellable | None: ...
    def get_check_cancellable(self) -> bool: ...
    def get_completed(self) -> bool: ...
    def get_context(self) -> GLib.MainContext: ...
    def get_name(self) -> str | None: ...
    def get_priority(self) -> int: ...
    def get_return_on_cancel(self) -> bool: ...
    def get_source_object(self) -> GObject.Object | None: ...
    def get_source_tag(self) -> int: ...
    def get_task_data(self) -> int: ...
    def had_error(self) -> bool: ...
    @staticmethod
    def is_valid(
        result: AsyncResult, source_object: GObject.Object | None = None
    ) -> bool: ...
    @classmethod
    def new(
        cls,
        source_object: GObject.Object | None = None,
        cancellable: Cancellable | None = None,
        callback: _AsyncReadyVarArgsCallback[Task, Unpack[_DataTs]] | None = None,
        *callback_data: Unpack[_DataTs],
    ) -> Task: ...
    def propagate_boolean(self) -> bool: ...
    def propagate_int(self) -> int: ...
    def propagate_pointer(self) -> int: ...
    def propagate_value(self) -> tuple[bool, Any]: ...
    @staticmethod
    def report_error(
        source_object: GObject.Object | None,
        callback: _AsyncReadyCallback[None, Any | None] | None,
        callback_data: Any | None,
        source_tag: int | Any | None,
        error: GLib.Error,
    ) -> None: ...
    def return_boolean(self, result: bool) -> None: ...
    def return_error(self, error: GLib.Error) -> None: ...
    def return_error_if_cancelled(self) -> bool: ...
    def return_int(self, result: int) -> None: ...
    def return_new_error_literal(
        self, domain: int, code: int, message: str
    ) -> None: ...
    def return_pointer(
        self,
        result: int | Any | None = None,
        result_destroy: Callable[[Any | None], None] | None = None,
    ) -> None: ...
    def return_value(self, result: Any | None = None) -> None: ...
    def run_in_thread(
        self,
        task_func: Callable[
            [Task, GObject.Object, Any | None, Cancellable | None], None
        ],
    ) -> None: ...
    def run_in_thread_sync(
        self,
        task_func: Callable[
            [Task, GObject.Object, Any | None, Cancellable | None], None
        ],
    ) -> None: ...
    def set_check_cancellable(self, check_cancellable: bool) -> None: ...
    def set_name(self, name: str | None = None) -> None: ...
    def set_priority(self, priority: int) -> None: ...
    def set_return_on_cancel(self, return_on_cancel: bool) -> bool: ...
    def set_source_tag(self, source_tag: int | Any | None = None) -> None: ...
    def set_static_name(self, name: str | None = None) -> None: ...
    def set_task_data(
        self,
        task_data: int | Any | None = None,
        task_data_destroy: Callable[[Any | None], None] | None = None,
    ) -> None: ...

class TaskClass(_gi.Struct): ...

class TcpConnection(SocketConnection):
    """
    :Constructors:

    ::

        TcpConnection(**properties)

    Object GTcpConnection

    Properties from GTcpConnection:
      graceful-disconnect -> gboolean: graceful-disconnect

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketConnection.Props):
        graceful_disconnect: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketConnection: ...
    @property
    def priv(self) -> TcpConnectionPrivate: ...
    def __init__(
        self, *, graceful_disconnect: bool = ..., socket: Socket | None = ...
    ) -> None: ...
    def get_graceful_disconnect(self) -> bool: ...
    def set_graceful_disconnect(self, graceful_disconnect: bool) -> None: ...

class TcpConnectionClass(_gi.Struct):
    """
    :Constructors:

    ::

        TcpConnectionClass()
    """
    @property
    def parent_class(self) -> SocketConnectionClass: ...

class TcpConnectionPrivate(_gi.Struct): ...

class TcpWrapperConnection(TcpConnection):
    """
    :Constructors:

    ::

        TcpWrapperConnection(**properties)
        new(base_io_stream:Gio.IOStream, socket:Gio.Socket) -> Gio.SocketConnection

    Object GTcpWrapperConnection

    Properties from GTcpWrapperConnection:
      base-io-stream -> GIOStream: base-io-stream

    Properties from GTcpConnection:
      graceful-disconnect -> gboolean: graceful-disconnect

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(TcpConnection.Props):
        @property
        def base_io_stream(self) -> IOStream: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> TcpConnection: ...
    @property
    def priv(self) -> TcpWrapperConnectionPrivate: ...
    def __init__(
        self,
        *,
        base_io_stream: IOStream | None = ...,
        graceful_disconnect: bool = ...,
        socket: Socket | None = ...,
    ) -> None: ...
    def get_base_io_stream(self) -> IOStream: ...
    @classmethod
    def new(cls, base_io_stream: IOStream, socket: Socket) -> TcpWrapperConnection: ...

class TcpWrapperConnectionClass(_gi.Struct):
    """
    :Constructors:

    ::

        TcpWrapperConnectionClass()
    """
    @property
    def parent_class(self) -> TcpConnectionClass: ...

class TcpWrapperConnectionPrivate(_gi.Struct): ...

class TestDBus(GObject.Object):
    """
    :Constructors:

    ::

        TestDBus(**properties)
        new(flags:Gio.TestDBusFlags) -> Gio.TestDBus

    Object GTestDBus

    Properties from GTestDBus:
      flags -> GTestDBusFlags: flags

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def flags(self) -> TestDBusFlags: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, flags: _TestDBusFlagsValueType = ...) -> None: ...
    def add_service_dir(self, path: str) -> None: ...
    def down(self) -> None: ...
    def get_bus_address(self) -> str | None: ...
    def get_flags(self) -> TestDBusFlags: ...
    @classmethod
    def new(cls, flags: _TestDBusFlagsValueType) -> TestDBus: ...
    def stop(self) -> None: ...
    @staticmethod
    def unset() -> None: ...
    def up(self) -> None: ...

class ThemedIcon(GObject.Object, Icon):
    """
    :Constructors:

    ::

        ThemedIcon(**properties)
        new(iconname:str) -> Gio.ThemedIcon
        new_from_names(iconnames:list) -> Gio.ThemedIcon
        new_with_default_fallbacks(iconname:str) -> Gio.ThemedIcon

    Object GThemedIcon

    Properties from GThemedIcon:
      name -> gchararray: name
      names -> GStrv: names
      use-default-fallbacks -> gboolean: use-default-fallbacks

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def names(self) -> list[str]: ...
        @property
        def use_default_fallbacks(self) -> bool: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        name: str | None = ...,
        names: Sequence[str] | None = ...,
        use_default_fallbacks: bool = ...,
    ) -> None: ...
    def append_name(self, iconname: str) -> None: ...
    def get_names(self) -> list[str]: ...
    @classmethod
    def new(cls, iconname: str) -> ThemedIcon: ...
    @classmethod
    def new_from_names(cls, iconnames: Sequence[str]) -> ThemedIcon: ...
    @classmethod
    def new_with_default_fallbacks(cls, iconname: str) -> ThemedIcon: ...
    def prepend_name(self, iconname: str) -> None: ...

class ThemedIconClass(_gi.Struct): ...

class ThreadedResolver(Resolver):
    """
    :Constructors:

    ::

        ThreadedResolver(**properties)

    Object GThreadedResolver

    Signals from GResolver:
      reload ()

    Properties from GResolver:
      timeout -> guint: timeout

    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *, timeout: int = ...) -> None: ...

class ThreadedResolverClass(_gi.Struct):
    """
    :Constructors:

    ::

        ThreadedResolverClass()
    """
    @property
    def parent_class(self) -> ResolverClass: ...

class ThreadedSocketService(SocketService):
    """
    :Constructors:

    ::

        ThreadedSocketService(**properties)
        new(max_threads:int) -> Gio.SocketService

    Object GThreadedSocketService

    Signals from GThreadedSocketService:
      run (GSocketConnection, GObject) -> gboolean

    Properties from GThreadedSocketService:
      max-threads -> gint: max-threads

    Signals from GSocketService:
      incoming (GSocketConnection, GObject) -> gboolean

    Properties from GSocketService:
      active -> gboolean: active

    Signals from GSocketListener:
      event (GSocketListenerEvent, GSocket)

    Properties from GSocketListener:
      listen-backlog -> gint: listen-backlog

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketService.Props):
        @property
        def max_threads(self) -> int: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketService: ...
    @property
    def priv(self) -> ThreadedSocketServicePrivate: ...
    def __init__(
        self, *, max_threads: int = ..., active: bool = ..., listen_backlog: int = ...
    ) -> None: ...
    def do_run(
        self, connection: SocketConnection, source_object: GObject.Object, /
    ) -> bool: ...
    @classmethod
    def new(cls, max_threads: int) -> ThreadedSocketService: ...

class ThreadedSocketServiceClass(_gi.Struct):
    """
    :Constructors:

    ::

        ThreadedSocketServiceClass()
    """
    @property
    def parent_class(self) -> SocketServiceClass: ...
    @property
    def run(
        self,
    ) -> Callable[[ThreadedSocketService, SocketConnection, GObject.Object], bool]: ...

class ThreadedSocketServicePrivate(_gi.Struct): ...

class TlsBackend(GObject.GInterface, Protocol):
    """
    Interface GTlsBackend

    Signals from GObject:
      notify (GParam)
    """
    def get_certificate_type(self) -> type[Any]: ...
    def get_client_connection_type(self) -> type[Any]: ...
    @staticmethod
    def get_default() -> TlsBackend: ...
    def get_default_database(self) -> TlsDatabase: ...
    def get_dtls_client_connection_type(self) -> type[Any]: ...
    def get_dtls_server_connection_type(self) -> type[Any]: ...
    def get_file_database_type(self) -> type[Any]: ...
    def get_server_connection_type(self) -> type[Any]: ...
    def set_default_database(self, database: TlsDatabase | None = None) -> None: ...
    def supports_dtls(self) -> bool: ...
    def supports_tls(self) -> bool: ...

class TlsBackendInterface(_gi.Struct):
    """
    :Constructors:

    ::

        TlsBackendInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def supports_tls(self) -> Callable[[TlsBackend], bool]: ...
    @property
    def get_certificate_type(self) -> Callable[[], type[Any]]: ...
    @property
    def get_client_connection_type(self) -> Callable[[], type[Any]]: ...
    @property
    def get_server_connection_type(self) -> Callable[[], type[Any]]: ...
    @property
    def get_file_database_type(self) -> Callable[[], type[Any]]: ...
    @property
    def get_default_database(self) -> Callable[[TlsBackend], TlsDatabase]: ...
    @property
    def supports_dtls(self) -> Callable[[TlsBackend], bool]: ...
    @property
    def get_dtls_client_connection_type(self) -> Callable[[], type[Any]]: ...
    @property
    def get_dtls_server_connection_type(self) -> Callable[[], type[Any]]: ...

class TlsCertificate(GObject.Object):
    """
    :Constructors:

    ::

        TlsCertificate(**properties)
        new_from_file(file:str) -> Gio.TlsCertificate
        new_from_file_with_password(file:str, password:str) -> Gio.TlsCertificate
        new_from_files(cert_file:str, key_file:str) -> Gio.TlsCertificate
        new_from_pem(data:str, length:int) -> Gio.TlsCertificate
        new_from_pkcs11_uris(pkcs11_uri:str, private_key_pkcs11_uri:str=None) -> Gio.TlsCertificate
        new_from_pkcs12(data:list, password:str=None) -> Gio.TlsCertificate

    Object GTlsCertificate

    Properties from GTlsCertificate:
      certificate -> GByteArray: certificate
      certificate-pem -> gchararray: certificate-pem
      private-key -> GByteArray: private-key
      private-key-pem -> gchararray: private-key-pem
      issuer -> GTlsCertificate: issuer
      pkcs11-uri -> gchararray: pkcs11-uri
      private-key-pkcs11-uri -> gchararray: private-key-pkcs11-uri
      not-valid-before -> GDateTime: not-valid-before
      not-valid-after -> GDateTime: not-valid-after
      subject-name -> gchararray: subject-name
      issuer-name -> gchararray: issuer-name
      dns-names -> GPtrArray: dns-names
      ip-addresses -> GPtrArray: ip-addresses
      pkcs12-data -> GByteArray: pkcs12-data
      password -> gchararray: password

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def certificate(self) -> bytes: ...
        @property
        def certificate_pem(self) -> str | None: ...
        @property
        def dns_names(self) -> list[int]: ...
        @property
        def ip_addresses(self) -> list[int]: ...
        @property
        def issuer(self) -> TlsCertificate | None: ...
        @property
        def issuer_name(self) -> str | None: ...
        @property
        def not_valid_after(self) -> GLib.DateTime | None: ...
        @property
        def not_valid_before(self) -> GLib.DateTime | None: ...
        @property
        def pkcs11_uri(self) -> str | None: ...
        @property
        def private_key(self) -> bytes: ...
        @property
        def private_key_pem(self) -> str | None: ...
        @property
        def private_key_pkcs11_uri(self) -> str | None: ...
        @property
        def subject_name(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> TlsCertificatePrivate: ...
    def __init__(
        self,
        *,
        certificate: Sequence[int] | None = ...,
        certificate_pem: str | None = ...,
        issuer: TlsCertificate | None = ...,
        password: str | None = ...,
        pkcs11_uri: str | None = ...,
        pkcs12_data: Sequence[int] | None = ...,
        private_key: Sequence[int] | None = ...,
        private_key_pem: str | None = ...,
        private_key_pkcs11_uri: str | None = ...,
    ) -> None: ...
    def do_verify(
        self, identity: SocketConnectable | None, trusted_ca: TlsCertificate | None, /
    ) -> TlsCertificateFlags: ...
    def get_dns_names(self) -> list[GLib.Bytes]: ...
    def get_ip_addresses(self) -> list[InetAddress]: ...
    def get_issuer(self) -> TlsCertificate | None: ...
    def get_issuer_name(self) -> str | None: ...
    def get_not_valid_after(self) -> GLib.DateTime | None: ...
    def get_not_valid_before(self) -> GLib.DateTime | None: ...
    def get_subject_name(self) -> str | None: ...
    def is_same(self, cert_two: TlsCertificate) -> bool: ...
    @staticmethod
    def list_new_from_file(file: str) -> list[TlsCertificate]: ...
    @classmethod
    def new_from_file(cls, file: str) -> TlsCertificate: ...
    @classmethod
    def new_from_file_with_password(
        cls, file: str, password: str
    ) -> TlsCertificate: ...
    @classmethod
    def new_from_files(cls, cert_file: str, key_file: str) -> TlsCertificate: ...
    @classmethod
    def new_from_pem(cls, data: str, length: int) -> TlsCertificate: ...
    @classmethod
    def new_from_pkcs11_uris(
        cls, pkcs11_uri: str, private_key_pkcs11_uri: str | None = None
    ) -> TlsCertificate: ...
    @classmethod
    def new_from_pkcs12(
        cls, data: Sequence[int], password: str | None = None
    ) -> TlsCertificate: ...
    def verify(
        self,
        identity: SocketConnectable | None = None,
        trusted_ca: TlsCertificate | None = None,
    ) -> TlsCertificateFlags: ...

class TlsCertificateClass(_gi.Struct):
    """
    :Constructors:

    ::

        TlsCertificateClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def verify(
        self,
    ) -> Callable[
        [TlsCertificate, SocketConnectable | None, TlsCertificate | None],
        TlsCertificateFlags,
    ]: ...
    @property
    def padding(self) -> list[int]: ...

class TlsCertificatePrivate(_gi.Struct): ...

class TlsClientConnection(GObject.GInterface, Protocol):
    """
    Interface GTlsClientConnection

    Signals from GObject:
      notify (GParam)
    """
    def copy_session_state(self, source: TlsClientConnection) -> None: ...
    def get_accepted_cas(self) -> list[bytes]: ...
    def get_server_identity(self) -> SocketConnectable | None: ...
    def get_use_ssl3(self) -> bool: ...
    def get_validation_flags(self) -> TlsCertificateFlags: ...
    @staticmethod
    def new(
        base_io_stream: IOStream, server_identity: SocketConnectable | None = None
    ) -> TlsClientConnection: ...
    def set_server_identity(self, identity: SocketConnectable) -> None: ...
    def set_use_ssl3(self, use_ssl3: bool) -> None: ...
    def set_validation_flags(self, flags: _TlsCertificateFlagsValueType) -> None: ...

class TlsClientConnectionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        TlsClientConnectionInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def copy_session_state(
        self,
    ) -> Callable[[TlsClientConnection, TlsClientConnection], None]: ...

class TlsConnection(IOStream):
    """
    :Constructors:

    ::

        TlsConnection(**properties)

    Object GTlsConnection

    Signals from GTlsConnection:
      accept-certificate (GTlsCertificate, GTlsCertificateFlags) -> gboolean

    Properties from GTlsConnection:
      base-io-stream -> GIOStream: base-io-stream
      require-close-notify -> gboolean: require-close-notify
      rehandshake-mode -> GTlsRehandshakeMode: rehandshake-mode
      use-system-certdb -> gboolean: use-system-certdb
      database -> GTlsDatabase: database
      interaction -> GTlsInteraction: interaction
      certificate -> GTlsCertificate: certificate
      peer-certificate -> GTlsCertificate: peer-certificate
      peer-certificate-errors -> GTlsCertificateFlags: peer-certificate-errors
      advertised-protocols -> GStrv: advertised-protocols
      negotiated-protocol -> gchararray: negotiated-protocol
      protocol-version -> GTlsProtocolVersion: protocol-version
      ciphersuite-name -> gchararray: ciphersuite-name

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(IOStream.Props):
        @property
        def advertised_protocols(self) -> list[str]: ...
        @advertised_protocols.setter
        def advertised_protocols(self, value: Sequence[str] | None) -> None: ...
        @property
        def base_io_stream(self) -> IOStream | None: ...
        @property
        def certificate(self) -> TlsCertificate | None: ...
        @certificate.setter
        def certificate(self, value: TlsCertificate) -> None: ...
        @property
        def ciphersuite_name(self) -> str | None: ...
        database: TlsDatabase | None
        interaction: TlsInteraction | None
        @property
        def negotiated_protocol(self) -> str | None: ...
        @property
        def peer_certificate(self) -> TlsCertificate | None: ...
        @property
        def peer_certificate_errors(self) -> TlsCertificateFlags: ...
        @property
        def protocol_version(self) -> TlsProtocolVersion: ...
        @property
        def rehandshake_mode(self) -> TlsRehandshakeMode: ...
        @rehandshake_mode.setter
        def rehandshake_mode(self, value: _TlsRehandshakeModeValueType) -> None: ...
        require_close_notify: bool
        use_system_certdb: bool

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> IOStream: ...
    @property
    def priv(self) -> TlsConnectionPrivate: ...
    def __init__(
        self,
        *,
        advertised_protocols: Sequence[str] | None = ...,
        base_io_stream: IOStream | None = ...,
        certificate: TlsCertificate = ...,
        database: TlsDatabase | None = ...,
        interaction: TlsInteraction | None = ...,
        rehandshake_mode: _TlsRehandshakeModeValueType = ...,
        require_close_notify: bool = ...,
        use_system_certdb: bool = ...,
    ) -> None: ...
    def do_accept_certificate(
        self, peer_cert: TlsCertificate, errors: _TlsCertificateFlagsValueType, /
    ) -> bool: ...
    def do_get_binding_data(
        self, type: _TlsChannelBindingTypeValueType, data: Sequence[int], /
    ) -> bool: ...
    def do_get_negotiated_protocol(self) -> str | None: ...
    def do_handshake(self, cancellable: Cancellable | None, /) -> bool: ...
    def do_handshake_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsConnection, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_handshake_finish(self, result: AsyncResult, /) -> bool: ...
    def emit_accept_certificate(
        self, peer_cert: TlsCertificate, errors: _TlsCertificateFlagsValueType
    ) -> bool: ...
    def get_certificate(self) -> TlsCertificate | None: ...
    def get_channel_binding_data(
        self, type: _TlsChannelBindingTypeValueType
    ) -> tuple[bool, bytes]: ...
    def get_ciphersuite_name(self) -> str | None: ...
    def get_database(self) -> TlsDatabase | None: ...
    def get_interaction(self) -> TlsInteraction | None: ...
    def get_negotiated_protocol(self) -> str | None: ...
    def get_peer_certificate(self) -> TlsCertificate | None: ...
    def get_peer_certificate_errors(self) -> TlsCertificateFlags: ...
    def get_protocol_version(self) -> TlsProtocolVersion: ...
    def get_rehandshake_mode(self) -> TlsRehandshakeMode: ...
    def get_require_close_notify(self) -> bool: ...
    def get_use_system_certdb(self) -> bool: ...
    def handshake(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def handshake_async(
        self, io_priority: int, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def handshake_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def handshake_async(
        self,
        io_priority: int,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsConnection] | None,
    ) -> None: ...
    def handshake_finish(self, result: AsyncResult) -> bool: ...
    def set_advertised_protocols(
        self, protocols: Sequence[str] | None = None
    ) -> None: ...
    def set_certificate(self, certificate: TlsCertificate) -> None: ...
    def set_database(self, database: TlsDatabase | None = None) -> None: ...
    def set_interaction(self, interaction: TlsInteraction | None = None) -> None: ...
    def set_rehandshake_mode(self, mode: _TlsRehandshakeModeValueType) -> None: ...
    def set_require_close_notify(self, require_close_notify: bool) -> None: ...
    def set_use_system_certdb(self, use_system_certdb: bool) -> None: ...

class TlsConnectionClass(_gi.Struct):
    """
    :Constructors:

    ::

        TlsConnectionClass()
    """
    @property
    def parent_class(self) -> IOStreamClass: ...
    @property
    def accept_certificate(
        self,
    ) -> Callable[
        [TlsConnection, TlsCertificate, _TlsCertificateFlagsValueType], bool
    ]: ...
    @property
    def handshake(self) -> Callable[[TlsConnection, Cancellable | None], bool]: ...
    @property
    def handshake_async(
        self,
    ) -> Callable[
        [
            TlsConnection,
            int,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def handshake_finish(self) -> Callable[[TlsConnection, AsyncResult], bool]: ...
    @property
    def get_binding_data(
        self,
    ) -> Callable[
        [TlsConnection, _TlsChannelBindingTypeValueType, Sequence[int]], bool
    ]: ...
    @property
    def get_negotiated_protocol(self) -> Callable[[TlsConnection], str | None]: ...
    @property
    def padding(self) -> list[int]: ...

class TlsConnectionPrivate(_gi.Struct): ...

class TlsDatabase(GObject.Object):
    """
    :Constructors:

    ::

        TlsDatabase(**properties)

    Object GTlsDatabase

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> TlsDatabasePrivate: ...
    def create_certificate_handle(self, certificate: TlsCertificate) -> str | None: ...
    def do_create_certificate_handle(
        self, certificate: TlsCertificate, /
    ) -> str | None: ...
    def do_lookup_certificate_for_handle(
        self,
        handle: str,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> TlsCertificate | None: ...
    def do_lookup_certificate_for_handle_async(
        self,
        handle: str,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsDatabase, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_certificate_for_handle_finish(
        self, result: AsyncResult, /
    ) -> TlsCertificate: ...
    def do_lookup_certificate_issuer(
        self,
        certificate: TlsCertificate,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> TlsCertificate: ...
    def do_lookup_certificate_issuer_async(
        self,
        certificate: TlsCertificate,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsDatabase, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_certificate_issuer_finish(
        self, result: AsyncResult, /
    ) -> TlsCertificate: ...
    def do_lookup_certificates_issued_by(
        self,
        issuer_raw_dn: Sequence[int],
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> list[TlsCertificate]: ...
    def do_lookup_certificates_issued_by_async(
        self,
        issuer_raw_dn: Sequence[int],
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsDatabase, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_lookup_certificates_issued_by_finish(
        self, result: AsyncResult, /
    ) -> list[TlsCertificate]: ...
    def do_verify_chain(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: SocketConnectable | None,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseVerifyFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> TlsCertificateFlags: ...
    def do_verify_chain_async(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: SocketConnectable | None,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseVerifyFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsDatabase, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_verify_chain_finish(self, result: AsyncResult, /) -> TlsCertificateFlags: ...
    def lookup_certificate_for_handle(
        self,
        handle: str,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> TlsCertificate | None: ...
    @overload
    def lookup_certificate_for_handle_async(
        self,
        handle: str,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[TlsCertificate]: ...
    @overload
    def lookup_certificate_for_handle_async(
        self,
        handle: str,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_certificate_for_handle_async(
        self,
        handle: str,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase] | None,
    ) -> None: ...
    def lookup_certificate_for_handle_finish(
        self, result: AsyncResult
    ) -> TlsCertificate: ...
    def lookup_certificate_issuer(
        self,
        certificate: TlsCertificate,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> TlsCertificate: ...
    @overload
    def lookup_certificate_issuer_async(
        self,
        certificate: TlsCertificate,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[TlsCertificate]: ...
    @overload
    def lookup_certificate_issuer_async(
        self,
        certificate: TlsCertificate,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_certificate_issuer_async(
        self,
        certificate: TlsCertificate,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase] | None,
    ) -> None: ...
    def lookup_certificate_issuer_finish(
        self, result: AsyncResult
    ) -> TlsCertificate: ...
    def lookup_certificates_issued_by(
        self,
        issuer_raw_dn: Sequence[int],
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> list[TlsCertificate]: ...
    @overload
    def lookup_certificates_issued_by_async(
        self,
        issuer_raw_dn: Sequence[int],
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[list[TlsCertificate]]: ...
    @overload
    def lookup_certificates_issued_by_async(
        self,
        issuer_raw_dn: Sequence[int],
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def lookup_certificates_issued_by_async(
        self,
        issuer_raw_dn: Sequence[int],
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseLookupFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase] | None,
    ) -> None: ...
    def lookup_certificates_issued_by_finish(
        self, result: AsyncResult
    ) -> list[TlsCertificate]: ...
    def verify_chain(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: SocketConnectable | None,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseVerifyFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> TlsCertificateFlags: ...
    @overload
    def verify_chain_async(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: SocketConnectable | None,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseVerifyFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[TlsCertificateFlags]: ...
    @overload
    def verify_chain_async(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: SocketConnectable | None,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseVerifyFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def verify_chain_async(
        self,
        chain: TlsCertificate,
        purpose: str,
        identity: SocketConnectable | None,
        interaction: TlsInteraction | None,
        flags: _TlsDatabaseVerifyFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsDatabase] | None,
    ) -> None: ...
    def verify_chain_finish(self, result: AsyncResult) -> TlsCertificateFlags: ...

class TlsDatabaseClass(_gi.Struct):
    """
    :Constructors:

    ::

        TlsDatabaseClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def verify_chain(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            TlsCertificate,
            str,
            SocketConnectable | None,
            TlsInteraction | None,
            _TlsDatabaseVerifyFlagsValueType,
            Cancellable | None,
        ],
        TlsCertificateFlags,
    ]: ...
    @property
    def verify_chain_async(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            TlsCertificate,
            str,
            SocketConnectable | None,
            TlsInteraction | None,
            _TlsDatabaseVerifyFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def verify_chain_finish(
        self,
    ) -> Callable[[TlsDatabase, AsyncResult], TlsCertificateFlags]: ...
    @property
    def create_certificate_handle(
        self,
    ) -> Callable[[TlsDatabase, TlsCertificate], str | None]: ...
    @property
    def lookup_certificate_for_handle(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            str,
            TlsInteraction | None,
            _TlsDatabaseLookupFlagsValueType,
            Cancellable | None,
        ],
        TlsCertificate | None,
    ]: ...
    @property
    def lookup_certificate_for_handle_async(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            str,
            TlsInteraction | None,
            _TlsDatabaseLookupFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_certificate_for_handle_finish(
        self,
    ) -> Callable[[TlsDatabase, AsyncResult], TlsCertificate]: ...
    @property
    def lookup_certificate_issuer(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            TlsCertificate,
            TlsInteraction | None,
            _TlsDatabaseLookupFlagsValueType,
            Cancellable | None,
        ],
        TlsCertificate,
    ]: ...
    @property
    def lookup_certificate_issuer_async(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            TlsCertificate,
            TlsInteraction | None,
            _TlsDatabaseLookupFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_certificate_issuer_finish(
        self,
    ) -> Callable[[TlsDatabase, AsyncResult], TlsCertificate]: ...
    @property
    def lookup_certificates_issued_by(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            Sequence[int],
            TlsInteraction | None,
            _TlsDatabaseLookupFlagsValueType,
            Cancellable | None,
        ],
        list[TlsCertificate],
    ]: ...
    @property
    def lookup_certificates_issued_by_async(
        self,
    ) -> Callable[
        [
            TlsDatabase,
            Sequence[int],
            TlsInteraction | None,
            _TlsDatabaseLookupFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def lookup_certificates_issued_by_finish(
        self,
    ) -> Callable[[TlsDatabase, AsyncResult], list[TlsCertificate]]: ...
    @property
    def padding(self) -> list[int]: ...

class TlsDatabasePrivate(_gi.Struct): ...

class TlsFileDatabase(GObject.GInterface, Protocol):
    """
    Interface GTlsFileDatabase

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def new(anchors: str) -> TlsFileDatabase: ...

class TlsFileDatabaseInterface(_gi.Struct):
    """
    :Constructors:

    ::

        TlsFileDatabaseInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def padding(self) -> list[int]: ...

class TlsInteraction(GObject.Object):
    """
    :Constructors:

    ::

        TlsInteraction(**properties)

    Object GTlsInteraction

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> TlsInteractionPrivate: ...
    def ask_password(
        self, password: TlsPassword, cancellable: Cancellable | None = None
    ) -> TlsInteractionResult: ...
    @overload
    def ask_password_async(
        self, password: TlsPassword, cancellable: Cancellable | None = None
    ) -> _gi.Async[TlsInteractionResult]: ...
    @overload
    def ask_password_async(
        self,
        password: TlsPassword,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsInteraction, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def ask_password_async(
        self,
        password: TlsPassword,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsInteraction] | None,
    ) -> None: ...
    def ask_password_finish(self, result: AsyncResult) -> TlsInteractionResult: ...
    def do_ask_password(
        self, password: TlsPassword, cancellable: Cancellable | None, /
    ) -> TlsInteractionResult: ...
    def do_ask_password_async(
        self,
        password: TlsPassword,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsInteraction, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_ask_password_finish(
        self, result: AsyncResult, /
    ) -> TlsInteractionResult: ...
    def do_request_certificate(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> TlsInteractionResult: ...
    def do_request_certificate_async(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyCallback[TlsInteraction, int | Any | None] | None,
        user_data: int | Any | None,
        /,
    ) -> None: ...
    def do_request_certificate_finish(
        self, result: AsyncResult, /
    ) -> TlsInteractionResult: ...
    def invoke_ask_password(
        self, password: TlsPassword, cancellable: Cancellable | None = None
    ) -> TlsInteractionResult: ...
    def invoke_request_certificate(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> TlsInteractionResult: ...
    def request_certificate(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> TlsInteractionResult: ...
    @overload
    def request_certificate_async(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[TlsInteractionResult]: ...
    @overload
    def request_certificate_async(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[TlsInteraction, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def request_certificate_async(
        self,
        connection: TlsConnection,
        flags: _TlsCertificateRequestFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[TlsInteraction] | None,
    ) -> None: ...
    def request_certificate_finish(
        self, result: AsyncResult
    ) -> TlsInteractionResult: ...

class TlsInteractionClass(_gi.Struct):
    """
    :Constructors:

    ::

        TlsInteractionClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def ask_password(
        self,
    ) -> Callable[
        [TlsInteraction, TlsPassword, Cancellable | None], TlsInteractionResult
    ]: ...
    @property
    def ask_password_async(
        self,
    ) -> Callable[
        [
            TlsInteraction,
            TlsPassword,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def ask_password_finish(
        self,
    ) -> Callable[[TlsInteraction, AsyncResult], TlsInteractionResult]: ...
    @property
    def request_certificate(
        self,
    ) -> Callable[
        [
            TlsInteraction,
            TlsConnection,
            _TlsCertificateRequestFlagsValueType,
            Cancellable | None,
        ],
        TlsInteractionResult,
    ]: ...
    @property
    def request_certificate_async(
        self,
    ) -> Callable[
        [
            TlsInteraction,
            TlsConnection,
            _TlsCertificateRequestFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def request_certificate_finish(
        self,
    ) -> Callable[[TlsInteraction, AsyncResult], TlsInteractionResult]: ...
    @property
    def padding(self) -> list[int]: ...

class TlsInteractionPrivate(_gi.Struct): ...

class TlsPassword(GObject.Object):
    """
    :Constructors:

    ::

        TlsPassword(**properties)
        new(flags:Gio.TlsPasswordFlags, description:str) -> Gio.TlsPassword

    Object GTlsPassword

    Properties from GTlsPassword:
      flags -> GTlsPasswordFlags: flags
      description -> gchararray: description
      warning -> gchararray: warning

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        description: str
        @property
        def flags(self) -> TlsPasswordFlags: ...
        @flags.setter
        def flags(self, value: _TlsPasswordFlagsValueType) -> None: ...
        warning: str

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> TlsPasswordPrivate: ...
    def __init__(
        self,
        *,
        description: str = ...,
        flags: _TlsPasswordFlagsValueType = ...,
        warning: str = ...,
    ) -> None: ...
    def do_get_default_warning(self) -> str: ...
    def do_get_value(self) -> bytes: ...
    def do_set_value(
        self, value: Sequence[int], destroy: Callable[[Any | None], None] | None, /
    ) -> None: ...
    def get_description(self) -> str: ...
    def get_flags(self) -> TlsPasswordFlags: ...
    def get_value(self) -> bytes: ...
    def get_warning(self) -> str: ...
    @classmethod
    def new(
        cls, flags: _TlsPasswordFlagsValueType, description: str
    ) -> TlsPassword: ...
    def set_description(self, description: str) -> None: ...
    def set_flags(self, flags: _TlsPasswordFlagsValueType) -> None: ...
    def set_value(self, value: Sequence[int]) -> None: ...
    def set_value_full(
        self, value: Sequence[int], destroy: Callable[[Any | None], None] | None = None
    ) -> None: ...
    def set_warning(self, warning: str) -> None: ...

class TlsPasswordClass(_gi.Struct):
    """
    :Constructors:

    ::

        TlsPasswordClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def get_value(self) -> Callable[[TlsPassword], bytes]: ...
    @property
    def set_value(
        self,
    ) -> Callable[
        [TlsPassword, Sequence[int], int, Callable[[Any | None], None] | None], None
    ]: ...
    @property
    def get_default_warning(self) -> Callable[[TlsPassword], str]: ...
    @property
    def padding(self) -> list[int]: ...

class TlsPasswordPrivate(_gi.Struct): ...

class TlsServerConnection(GObject.GInterface, Protocol):
    """
    Interface GTlsServerConnection

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def new(
        base_io_stream: IOStream, certificate: TlsCertificate | None = None
    ) -> TlsServerConnection: ...

class TlsServerConnectionInterface(_gi.Struct):
    """
    :Constructors:

    ::

        TlsServerConnectionInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...

class UnixConnection(SocketConnection):
    """
    :Constructors:

    ::

        UnixConnection(**properties)

    Object GUnixConnection

    Properties from GSocketConnection:
      socket -> GSocket: socket

    Properties from GIOStream:
      input-stream -> GInputStream: input-stream
      output-stream -> GOutputStream: output-stream
      closed -> gboolean: closed

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> SocketConnection: ...
    @property
    def priv(self) -> UnixConnectionPrivate: ...
    def __init__(self, *, socket: Socket | None = ...) -> None: ...
    def receive_credentials(
        self, cancellable: Cancellable | None = None
    ) -> Credentials: ...
    @overload
    def receive_credentials_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[Credentials]: ...
    @overload
    def receive_credentials_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[UnixConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def receive_credentials_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[UnixConnection] | None,
    ) -> None: ...
    def receive_credentials_finish(self, result: AsyncResult) -> Credentials: ...
    def receive_fd(self, cancellable: Cancellable | None = None) -> int: ...
    def send_credentials(self, cancellable: Cancellable | None = None) -> bool: ...
    @overload
    def send_credentials_async(
        self, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def send_credentials_async(
        self,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[UnixConnection, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def send_credentials_async(
        self,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[UnixConnection] | None,
    ) -> None: ...
    def send_credentials_finish(self, result: AsyncResult) -> bool: ...
    def send_fd(self, fd: int, cancellable: Cancellable | None = None) -> bool: ...

class UnixConnectionClass(_gi.Struct):
    """
    :Constructors:

    ::

        UnixConnectionClass()
    """
    @property
    def parent_class(self) -> SocketConnectionClass: ...

class UnixConnectionPrivate(_gi.Struct): ...

class UnixCredentialsMessage(SocketControlMessage):
    """
    :Constructors:

    ::

        UnixCredentialsMessage(**properties)
        new() -> Gio.SocketControlMessage
        new_with_credentials(credentials:Gio.Credentials) -> Gio.SocketControlMessage

    Object GUnixCredentialsMessage

    Properties from GUnixCredentialsMessage:
      credentials -> GCredentials: credentials

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketControlMessage.Props):
        @property
        def credentials(self) -> Credentials: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketControlMessage: ...
    @property
    def priv(self) -> UnixCredentialsMessagePrivate: ...
    def __init__(self, *, credentials: Credentials | None = ...) -> None: ...
    def get_credentials(self) -> Credentials: ...
    @staticmethod
    def is_supported() -> bool: ...
    @classmethod
    def new(cls) -> UnixCredentialsMessage: ...
    @classmethod
    def new_with_credentials(
        cls, credentials: Credentials
    ) -> UnixCredentialsMessage: ...

class UnixCredentialsMessageClass(_gi.Struct):
    """
    :Constructors:

    ::

        UnixCredentialsMessageClass()
    """
    @property
    def parent_class(self) -> SocketControlMessageClass: ...

class UnixCredentialsMessagePrivate(_gi.Struct): ...

UnixDesktopAppInfoClass = GioUnix.DesktopAppInfoClass
UnixDesktopAppInfoLookupIface = GioUnix.DesktopAppInfoLookupIface

class UnixFDList(GObject.Object):
    """
    :Constructors:

    ::

        UnixFDList(**properties)
        new() -> Gio.UnixFDList
        new_from_array(fds:list) -> Gio.UnixFDList

    Object GUnixFDList

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> UnixFDListPrivate: ...
    def append(self, fd: int) -> int: ...
    def get(self, index_: int) -> int: ...
    def get_length(self) -> int: ...
    @classmethod
    def new(cls) -> UnixFDList: ...
    @classmethod
    def new_from_array(cls, fds: Sequence[int]) -> UnixFDList: ...
    def peek_fds(self) -> list[int]: ...
    def steal_fds(self) -> list[int]: ...

class UnixFDListClass(_gi.Struct):
    """
    :Constructors:

    ::

        UnixFDListClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class UnixFDListPrivate(_gi.Struct): ...

UnixFDMessage = GioUnix.FDMessage
UnixFDMessageClass = GioUnix.FDMessageClass
UnixFDMessagePrivate = GioUnix.FDMessagePrivate
UnixFileDescriptorBasedIface = GioUnix.FileDescriptorBasedIface
UnixInputStream = GioUnix.InputStream
UnixInputStreamClass = GioUnix.InputStreamClass
UnixInputStreamPrivate = GioUnix.InputStreamPrivate
UnixMountEntry = GioUnix.MountEntry
UnixMountMonitor = GioUnix.MountMonitor
UnixMountMonitorClass = GioUnix.MountMonitorClass
UnixMountPoint = GioUnix.MountPoint
UnixOutputStream = GioUnix.OutputStream
UnixOutputStreamClass = GioUnix.OutputStreamClass
UnixOutputStreamPrivate = GioUnix.OutputStreamPrivate

class UnixSocketAddress(SocketAddress):
    """
    :Constructors:

    ::

        UnixSocketAddress(**properties)
        new(path:str) -> Gio.SocketAddress
        new_abstract(path:list) -> Gio.SocketAddress
        new_with_type(path:list, type:Gio.UnixSocketAddressType) -> Gio.SocketAddress

    Object GUnixSocketAddress

    Properties from GUnixSocketAddress:
      path -> gchararray: path
      path-as-array -> GByteArray: path-as-array
      abstract -> gboolean: abstract
      address-type -> GUnixSocketAddressType: address-type

    Properties from GSocketAddress:
      family -> GSocketFamily: family

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(SocketAddress.Props):
        @property
        def abstract(self) -> bool: ...
        @property
        def address_type(self) -> UnixSocketAddressType: ...
        @property
        def path(self) -> str: ...
        @property
        def path_as_array(self) -> bytes: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> SocketAddress: ...
    @property
    def priv(self) -> UnixSocketAddressPrivate: ...
    def __init__(
        self,
        *,
        abstract: bool = ...,
        address_type: _UnixSocketAddressTypeValueType = ...,
        path: str | None = ...,
        path_as_array: Sequence[int] | None = ...,
    ) -> None: ...
    @staticmethod
    def abstract_names_supported() -> bool: ...
    def get_address_type(self) -> UnixSocketAddressType: ...
    def get_is_abstract(self) -> bool: ...
    def get_path(self) -> str: ...
    def get_path_len(self) -> int: ...
    @classmethod
    def new(cls, path: str) -> UnixSocketAddress: ...
    @classmethod
    def new_abstract(cls, path: Sequence[int]) -> UnixSocketAddress: ...
    @classmethod
    def new_with_type(
        cls, path: Sequence[int], type: _UnixSocketAddressTypeValueType
    ) -> UnixSocketAddress: ...

class UnixSocketAddressClass(_gi.Struct):
    """
    :Constructors:

    ::

        UnixSocketAddressClass()
    """
    @property
    def parent_class(self) -> SocketAddressClass: ...

class UnixSocketAddressPrivate(_gi.Struct): ...

class Vfs(GObject.Object):
    """
    :Constructors:

    ::

        Vfs(**properties)

    Object GVfs

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    def do_add_writable_namespaces(self, list: FileAttributeInfoList, /) -> None: ...
    def do_get_file_for_path(self, path: str, /) -> File: ...
    def do_get_file_for_uri(self, uri: str, /) -> File: ...
    def do_get_supported_uri_schemes(self) -> list[str]: ...
    def do_is_active(self) -> bool: ...
    def do_local_file_add_info(
        self,
        filename: str,
        device: int,
        attribute_matcher: FileAttributeMatcher,
        info: FileInfo,
        cancellable: Cancellable | None,
        extra_data: int | Any | None,
        free_extra_data: Callable[[Any | None], None],
        /,
    ) -> None: ...
    def do_local_file_moved(self, source: str, dest: str, /) -> None: ...
    def do_local_file_removed(self, filename: str, /) -> None: ...
    def do_local_file_set_attributes(
        self,
        filename: str,
        info: FileInfo,
        flags: _FileQueryInfoFlagsValueType,
        cancellable: Cancellable | None,
        /,
    ) -> bool: ...
    def do_parse_name(self, parse_name: str, /) -> File: ...
    @staticmethod
    def get_default() -> Vfs: ...
    def get_file_for_path(self, path: str) -> File: ...
    def get_file_for_uri(self, uri: str) -> File: ...
    @staticmethod
    def get_local() -> Vfs: ...
    def get_supported_uri_schemes(self) -> list[str]: ...
    def is_active(self) -> bool: ...
    def parse_name(self, parse_name: str) -> File: ...
    def register_uri_scheme(
        self,
        scheme: str,
        uri_func: Callable[[Vfs, str, Any | None], File | None] | None = None,
        uri_data: Any | None = None,
        parse_name_func: Callable[[Vfs, str, Unpack[_DataTs]], File | None]
        | None = None,
        *parse_name_data: Unpack[_DataTs],
    ) -> bool: ...
    def unregister_uri_scheme(self, scheme: str) -> bool: ...

class VfsClass(_gi.Struct):
    """
    :Constructors:

    ::

        VfsClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def is_active(self) -> Callable[[Vfs], bool]: ...
    @property
    def get_file_for_path(self) -> Callable[[Vfs, str], File]: ...
    @property
    def get_file_for_uri(self) -> Callable[[Vfs, str], File]: ...
    @property
    def get_supported_uri_schemes(self) -> Callable[[Vfs], list[str]]: ...
    @property
    def parse_name(self) -> Callable[[Vfs, str], File]: ...
    @property
    def local_file_add_info(
        self,
    ) -> Callable[
        [
            Vfs,
            str,
            int,
            FileAttributeMatcher,
            FileInfo,
            Cancellable | None,
            Any | None,
            Callable[[Any | None], None],
        ],
        None,
    ]: ...
    @property
    def add_writable_namespaces(
        self,
    ) -> Callable[[Vfs, FileAttributeInfoList], None]: ...
    @property
    def local_file_set_attributes(
        self,
    ) -> Callable[
        [Vfs, str, FileInfo, _FileQueryInfoFlagsValueType, Cancellable | None], bool
    ]: ...
    @property
    def local_file_removed(self) -> Callable[[Vfs, str], None]: ...
    @property
    def local_file_moved(self) -> Callable[[Vfs, str, str], None]: ...
    @property
    def deserialize_icon(self) -> int: ...

class Volume(GObject.GInterface, Protocol):
    """
    Interface GVolume

    Signals from GObject:
      notify (GParam)
    """
    def can_eject(self) -> bool: ...
    def can_mount(self) -> bool: ...
    @overload
    def eject(
        self, flags: _MountUnmountFlagsValueType, cancellable: Cancellable | None = None
    ) -> _gi.Async[bool]: ...
    @overload
    def eject(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Volume, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject(
        self,
        flags: _MountUnmountFlagsValueType,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Volume] | None,
    ) -> None: ...
    def eject_finish(self, result: AsyncResult) -> bool: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Volume, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def eject_with_operation(
        self,
        flags: _MountUnmountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Volume] | None,
    ) -> None: ...
    def eject_with_operation_finish(self, result: AsyncResult) -> bool: ...
    def enumerate_identifiers(self) -> list[str]: ...
    def get_activation_root(self) -> File | None: ...
    def get_drive(self) -> Drive | None: ...
    def get_icon(self) -> Icon: ...
    def get_identifier(self, kind: str) -> str | None: ...
    def get_mount(self) -> Mount | None: ...
    def get_name(self) -> str: ...
    def get_sort_key(self) -> str | None: ...
    def get_symbolic_icon(self) -> Icon: ...
    def get_uuid(self) -> str | None: ...
    @overload
    def mount(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
    ) -> _gi.Async[bool]: ...
    @overload
    def mount(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None,
        cancellable: Cancellable | None,
        callback: _AsyncReadyVarArgsCallback[Volume, Unpack[_DataTs]] | None,
        *user_data: Unpack[_DataTs],
    ) -> None: ...
    @overload
    def mount(
        self,
        flags: _MountMountFlagsValueType,
        mount_operation: MountOperation | None = None,
        cancellable: Cancellable | None = None,
        *,
        callback: _AsyncReadyVarArgsCallback[Volume] | None,
    ) -> None: ...
    def mount_finish(self, result: AsyncResult) -> bool: ...
    def should_automount(self) -> bool: ...

class VolumeIface(_gi.Struct):
    """
    :Constructors:

    ::

        VolumeIface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def changed(self) -> Callable[[Volume], None]: ...
    @property
    def removed(self) -> Callable[[Volume], None]: ...
    @property
    def get_name(self) -> Callable[[Volume], str]: ...
    @property
    def get_icon(self) -> Callable[[Volume], Icon]: ...
    @property
    def get_uuid(self) -> Callable[[Volume], str | None]: ...
    @property
    def get_drive(self) -> Callable[[Volume], Drive | None]: ...
    @property
    def get_mount(self) -> Callable[[Volume], Mount | None]: ...
    @property
    def can_mount(self) -> Callable[[Volume], bool]: ...
    @property
    def can_eject(self) -> Callable[[Volume], bool]: ...
    @property
    def mount_fn(
        self,
    ) -> Callable[
        [
            Volume,
            _MountMountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def mount_finish(self) -> Callable[[Volume, AsyncResult], bool]: ...
    @property
    def eject(
        self,
    ) -> Callable[
        [
            Volume,
            _MountUnmountFlagsValueType,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_finish(self) -> Callable[[Volume, AsyncResult], bool]: ...
    @property
    def get_identifier(self) -> Callable[[Volume, str], str | None]: ...
    @property
    def enumerate_identifiers(self) -> Callable[[Volume], list[str]]: ...
    @property
    def should_automount(self) -> Callable[[Volume], bool]: ...
    @property
    def get_activation_root(self) -> Callable[[Volume], File | None]: ...
    @property
    def eject_with_operation(
        self,
    ) -> Callable[
        [
            Volume,
            _MountUnmountFlagsValueType,
            MountOperation | None,
            Cancellable | None,
            Callable[[GObject.Object | None, AsyncResult, Any | None], None] | None,
            Any | None,
        ],
        None,
    ]: ...
    @property
    def eject_with_operation_finish(self) -> Callable[[Volume, AsyncResult], bool]: ...
    @property
    def get_sort_key(self) -> Callable[[Volume], str | None]: ...
    @property
    def get_symbolic_icon(self) -> Callable[[Volume], Icon]: ...

class VolumeMonitor(GObject.Object):
    """
    :Constructors:

    ::

        VolumeMonitor(**properties)

    Object GVolumeMonitor

    Signals from GVolumeMonitor:
      volume-added (GVolume)
      volume-removed (GVolume)
      volume-changed (GVolume)
      mount-added (GMount)
      mount-removed (GMount)
      mount-pre-unmount (GMount)
      mount-changed (GMount)
      drive-connected (GDrive)
      drive-disconnected (GDrive)
      drive-changed (GDrive)
      drive-eject-button (GDrive)
      drive-stop-button (GDrive)

    Signals from GObject:
      notify (GParam)
    """
    @property
    def parent_instance(self) -> GObject.Object: ...
    @property
    def priv(self) -> int: ...
    @staticmethod
    def adopt_orphan_mount(mount: Mount) -> Volume: ...
    def do_drive_changed(self, drive: Drive, /) -> None: ...
    def do_drive_connected(self, drive: Drive, /) -> None: ...
    def do_drive_disconnected(self, drive: Drive, /) -> None: ...
    def do_drive_eject_button(self, drive: Drive, /) -> None: ...
    def do_drive_stop_button(self, drive: Drive, /) -> None: ...
    def do_get_connected_drives(self) -> list[Drive]: ...
    def do_get_mount_for_uuid(self, uuid: str, /) -> Mount | None: ...
    def do_get_mounts(self) -> list[Mount]: ...
    def do_get_volume_for_uuid(self, uuid: str, /) -> Volume | None: ...
    def do_get_volumes(self) -> list[Volume]: ...
    def do_mount_added(self, mount: Mount, /) -> None: ...
    def do_mount_changed(self, mount: Mount, /) -> None: ...
    def do_mount_pre_unmount(self, mount: Mount, /) -> None: ...
    def do_mount_removed(self, mount: Mount, /) -> None: ...
    def do_volume_added(self, volume: Volume, /) -> None: ...
    def do_volume_changed(self, volume: Volume, /) -> None: ...
    def do_volume_removed(self, volume: Volume, /) -> None: ...
    @staticmethod
    def get() -> VolumeMonitor: ...
    def get_connected_drives(self) -> list[Drive]: ...
    def get_mount_for_uuid(self, uuid: str) -> Mount | None: ...
    def get_mounts(self) -> list[Mount]: ...
    def get_volume_for_uuid(self, uuid: str) -> Volume | None: ...
    def get_volumes(self) -> list[Volume]: ...

class VolumeMonitorClass(_gi.Struct):
    """
    :Constructors:

    ::

        VolumeMonitorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def volume_added(self) -> Callable[[VolumeMonitor, Volume], None]: ...
    @property
    def volume_removed(self) -> Callable[[VolumeMonitor, Volume], None]: ...
    @property
    def volume_changed(self) -> Callable[[VolumeMonitor, Volume], None]: ...
    @property
    def mount_added(self) -> Callable[[VolumeMonitor, Mount], None]: ...
    @property
    def mount_removed(self) -> Callable[[VolumeMonitor, Mount], None]: ...
    @property
    def mount_pre_unmount(self) -> Callable[[VolumeMonitor, Mount], None]: ...
    @property
    def mount_changed(self) -> Callable[[VolumeMonitor, Mount], None]: ...
    @property
    def drive_connected(self) -> Callable[[VolumeMonitor, Drive], None]: ...
    @property
    def drive_disconnected(self) -> Callable[[VolumeMonitor, Drive], None]: ...
    @property
    def drive_changed(self) -> Callable[[VolumeMonitor, Drive], None]: ...
    @property
    def is_supported(self) -> Callable[[], bool]: ...
    @property
    def get_connected_drives(self) -> Callable[[VolumeMonitor], list[Drive]]: ...
    @property
    def get_volumes(self) -> Callable[[VolumeMonitor], list[Volume]]: ...
    @property
    def get_mounts(self) -> Callable[[VolumeMonitor], list[Mount]]: ...
    @property
    def get_volume_for_uuid(self) -> Callable[[VolumeMonitor, str], Volume | None]: ...
    @property
    def get_mount_for_uuid(self) -> Callable[[VolumeMonitor, str], Mount | None]: ...
    @property
    def adopt_orphan_mount(self) -> int: ...
    @property
    def drive_eject_button(self) -> Callable[[VolumeMonitor, Drive], None]: ...
    @property
    def drive_stop_button(self) -> Callable[[VolumeMonitor, Drive], None]: ...

class ZlibCompressor(GObject.Object, Converter):
    """
    :Constructors:

    ::

        ZlibCompressor(**properties)
        new(format:Gio.ZlibCompressorFormat, level:int) -> Gio.ZlibCompressor

    Object GZlibCompressor

    Properties from GZlibCompressor:
      format -> GZlibCompressorFormat: format
      level -> gint: level
      file-info -> GFileInfo: file-info
      os -> gint: os

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        file_info: FileInfo | None
        @property
        def format(self) -> ZlibCompressorFormat: ...
        @property
        def level(self) -> int: ...
        os: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        file_info: FileInfo | None = ...,
        format: _ZlibCompressorFormatValueType = ...,
        level: int = ...,
        os: int = ...,
    ) -> None: ...
    def get_file_info(self) -> FileInfo | None: ...
    def get_os(self) -> int: ...
    @classmethod
    def new(
        cls, format: _ZlibCompressorFormatValueType, level: int
    ) -> ZlibCompressor: ...
    def set_file_info(self, file_info: FileInfo | None = None) -> None: ...
    def set_os(self, os: int) -> None: ...

class ZlibCompressorClass(_gi.Struct):
    """
    :Constructors:

    ::

        ZlibCompressorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class ZlibDecompressor(GObject.Object, Converter):
    """
    :Constructors:

    ::

        ZlibDecompressor(**properties)
        new(format:Gio.ZlibCompressorFormat) -> Gio.ZlibDecompressor

    Object GZlibDecompressor

    Properties from GZlibDecompressor:
      format -> GZlibCompressorFormat: format
      file-info -> GFileInfo: file-info

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def file_info(self) -> FileInfo | None: ...
        @property
        def format(self) -> ZlibCompressorFormat: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, format: _ZlibCompressorFormatValueType = ...) -> None: ...
    def get_file_info(self) -> FileInfo | None: ...
    @classmethod
    def new(cls, format: _ZlibCompressorFormatValueType) -> ZlibDecompressor: ...

class ZlibDecompressorClass(_gi.Struct):
    """
    :Constructors:

    ::

        ZlibDecompressorClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...

class AppInfoCreateFlags(GObject.GFlags):
    NEEDS_TERMINAL = 1
    NONE = 0
    SUPPORTS_STARTUP_NOTIFICATION = 4
    SUPPORTS_URIS = 2

_AppInfoCreateFlagsLiteralType: TypeAlias = Literal[
    "G_APP_INFO_CREATE_NEEDS_TERMINAL",
    "G_APP_INFO_CREATE_NONE",
    "G_APP_INFO_CREATE_SUPPORTS_STARTUP_NOTIFICATION",
    "G_APP_INFO_CREATE_SUPPORTS_URIS",
    "needs-terminal",
    "none",
    "supports-startup-notification",
    "supports-uris",
]
_AppInfoCreateFlagsValueType: TypeAlias = (
    AppInfoCreateFlags
    | _AppInfoCreateFlagsLiteralType
    | tuple[_AppInfoCreateFlagsLiteralType, ...]
)

class ApplicationFlags(GObject.GFlags):
    ALLOW_REPLACEMENT = 128
    CAN_OVERRIDE_APP_ID = 64
    DEFAULT_FLAGS = 0
    FLAGS_NONE = 0
    HANDLES_COMMAND_LINE = 8
    HANDLES_OPEN = 4
    IS_LAUNCHER = 2
    IS_SERVICE = 1
    NON_UNIQUE = 32
    REPLACE = 256
    SEND_ENVIRONMENT = 16

_ApplicationFlagsLiteralType: TypeAlias = Literal[
    "G_APPLICATION_ALLOW_REPLACEMENT",
    "G_APPLICATION_CAN_OVERRIDE_APP_ID",
    "G_APPLICATION_DEFAULT_FLAGS",
    "G_APPLICATION_FLAGS_NONE",
    "G_APPLICATION_HANDLES_COMMAND_LINE",
    "G_APPLICATION_HANDLES_OPEN",
    "G_APPLICATION_IS_LAUNCHER",
    "G_APPLICATION_IS_SERVICE",
    "G_APPLICATION_NON_UNIQUE",
    "G_APPLICATION_REPLACE",
    "G_APPLICATION_SEND_ENVIRONMENT",
    "allow-replacement",
    "can-override-app-id",
    "default-flags",
    "flags-none",
    "handles-command-line",
    "handles-open",
    "is-launcher",
    "is-service",
    "non-unique",
    "replace",
    "send-environment",
]
_ApplicationFlagsValueType: TypeAlias = (
    ApplicationFlags
    | _ApplicationFlagsLiteralType
    | tuple[_ApplicationFlagsLiteralType, ...]
)

class AskPasswordFlags(GObject.GFlags):
    ANONYMOUS_SUPPORTED = 16
    NEED_DOMAIN = 4
    NEED_PASSWORD = 1
    NEED_USERNAME = 2
    SAVING_SUPPORTED = 8
    TCRYPT = 32

_AskPasswordFlagsLiteralType: TypeAlias = Literal[
    "G_ASK_PASSWORD_ANONYMOUS_SUPPORTED",
    "G_ASK_PASSWORD_NEED_DOMAIN",
    "G_ASK_PASSWORD_NEED_PASSWORD",
    "G_ASK_PASSWORD_NEED_USERNAME",
    "G_ASK_PASSWORD_SAVING_SUPPORTED",
    "G_ASK_PASSWORD_TCRYPT",
    "anonymous-supported",
    "need-domain",
    "need-password",
    "need-username",
    "saving-supported",
    "tcrypt",
]
_AskPasswordFlagsValueType: TypeAlias = (
    AskPasswordFlags
    | _AskPasswordFlagsLiteralType
    | tuple[_AskPasswordFlagsLiteralType, ...]
)

class BusNameOwnerFlags(GObject.GFlags):
    ALLOW_REPLACEMENT = 1
    DO_NOT_QUEUE = 4
    NONE = 0
    REPLACE = 2

_BusNameOwnerFlagsLiteralType: TypeAlias = Literal[
    "G_BUS_NAME_OWNER_FLAGS_ALLOW_REPLACEMENT",
    "G_BUS_NAME_OWNER_FLAGS_DO_NOT_QUEUE",
    "G_BUS_NAME_OWNER_FLAGS_NONE",
    "G_BUS_NAME_OWNER_FLAGS_REPLACE",
    "allow-replacement",
    "do-not-queue",
    "none",
    "replace",
]
_BusNameOwnerFlagsValueType: TypeAlias = (
    BusNameOwnerFlags
    | _BusNameOwnerFlagsLiteralType
    | tuple[_BusNameOwnerFlagsLiteralType, ...]
)

class BusNameWatcherFlags(GObject.GFlags):
    AUTO_START = 1
    NONE = 0

_BusNameWatcherFlagsLiteralType: TypeAlias = Literal[
    "G_BUS_NAME_WATCHER_FLAGS_AUTO_START",
    "G_BUS_NAME_WATCHER_FLAGS_NONE",
    "auto-start",
    "none",
]
_BusNameWatcherFlagsValueType: TypeAlias = (
    BusNameWatcherFlags
    | _BusNameWatcherFlagsLiteralType
    | tuple[_BusNameWatcherFlagsLiteralType, ...]
)

class ConverterFlags(GObject.GFlags):
    FLUSH = 2
    INPUT_AT_END = 1
    NONE = 0

_ConverterFlagsLiteralType: TypeAlias = Literal[
    "G_CONVERTER_FLUSH",
    "G_CONVERTER_INPUT_AT_END",
    "G_CONVERTER_NO_FLAGS",
    "flush",
    "input-at-end",
    "none",
]
_ConverterFlagsValueType: TypeAlias = (
    ConverterFlags | _ConverterFlagsLiteralType | tuple[_ConverterFlagsLiteralType, ...]
)

class DBusCallFlags(GObject.GFlags):
    ALLOW_INTERACTIVE_AUTHORIZATION = 2
    NONE = 0
    NO_AUTO_START = 1

_DBusCallFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_CALL_FLAGS_ALLOW_INTERACTIVE_AUTHORIZATION",
    "G_DBUS_CALL_FLAGS_NONE",
    "G_DBUS_CALL_FLAGS_NO_AUTO_START",
    "allow-interactive-authorization",
    "no-auto-start",
    "none",
]
_DBusCallFlagsValueType: TypeAlias = (
    DBusCallFlags | _DBusCallFlagsLiteralType | tuple[_DBusCallFlagsLiteralType, ...]
)

class DBusCapabilityFlags(GObject.GFlags):
    NONE = 0
    UNIX_FD_PASSING = 1

_DBusCapabilityFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_CAPABILITY_FLAGS_NONE",
    "G_DBUS_CAPABILITY_FLAGS_UNIX_FD_PASSING",
    "none",
    "unix-fd-passing",
]
_DBusCapabilityFlagsValueType: TypeAlias = (
    DBusCapabilityFlags
    | _DBusCapabilityFlagsLiteralType
    | tuple[_DBusCapabilityFlagsLiteralType, ...]
)

class DBusConnectionFlags(GObject.GFlags):
    AUTHENTICATION_ALLOW_ANONYMOUS = 4
    AUTHENTICATION_CLIENT = 1
    AUTHENTICATION_REQUIRE_SAME_USER = 32
    AUTHENTICATION_SERVER = 2
    CROSS_NAMESPACE = 64
    DELAY_MESSAGE_PROCESSING = 16
    MESSAGE_BUS_CONNECTION = 8
    NONE = 0

_DBusConnectionFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_CONNECTION_FLAGS_AUTHENTICATION_ALLOW_ANONYMOUS",
    "G_DBUS_CONNECTION_FLAGS_AUTHENTICATION_CLIENT",
    "G_DBUS_CONNECTION_FLAGS_AUTHENTICATION_REQUIRE_SAME_USER",
    "G_DBUS_CONNECTION_FLAGS_AUTHENTICATION_SERVER",
    "G_DBUS_CONNECTION_FLAGS_CROSS_NAMESPACE",
    "G_DBUS_CONNECTION_FLAGS_DELAY_MESSAGE_PROCESSING",
    "G_DBUS_CONNECTION_FLAGS_MESSAGE_BUS_CONNECTION",
    "G_DBUS_CONNECTION_FLAGS_NONE",
    "authentication-allow-anonymous",
    "authentication-client",
    "authentication-require-same-user",
    "authentication-server",
    "cross-namespace",
    "delay-message-processing",
    "message-bus-connection",
    "none",
]
_DBusConnectionFlagsValueType: TypeAlias = (
    DBusConnectionFlags
    | _DBusConnectionFlagsLiteralType
    | tuple[_DBusConnectionFlagsLiteralType, ...]
)

class DBusInterfaceSkeletonFlags(GObject.GFlags):
    HANDLE_METHOD_INVOCATIONS_IN_THREAD = 1
    NONE = 0

_DBusInterfaceSkeletonFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_INTERFACE_SKELETON_FLAGS_HANDLE_METHOD_INVOCATIONS_IN_THREAD",
    "G_DBUS_INTERFACE_SKELETON_FLAGS_NONE",
    "handle-method-invocations-in-thread",
    "none",
]
_DBusInterfaceSkeletonFlagsValueType: TypeAlias = (
    DBusInterfaceSkeletonFlags
    | _DBusInterfaceSkeletonFlagsLiteralType
    | tuple[_DBusInterfaceSkeletonFlagsLiteralType, ...]
)

class DBusMessageFlags(GObject.GFlags):
    ALLOW_INTERACTIVE_AUTHORIZATION = 4
    NONE = 0
    NO_AUTO_START = 2
    NO_REPLY_EXPECTED = 1

_DBusMessageFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_MESSAGE_FLAGS_ALLOW_INTERACTIVE_AUTHORIZATION",
    "G_DBUS_MESSAGE_FLAGS_NONE",
    "G_DBUS_MESSAGE_FLAGS_NO_AUTO_START",
    "G_DBUS_MESSAGE_FLAGS_NO_REPLY_EXPECTED",
    "allow-interactive-authorization",
    "no-auto-start",
    "no-reply-expected",
    "none",
]
_DBusMessageFlagsValueType: TypeAlias = (
    DBusMessageFlags
    | _DBusMessageFlagsLiteralType
    | tuple[_DBusMessageFlagsLiteralType, ...]
)

class DBusObjectManagerClientFlags(GObject.GFlags):
    DO_NOT_AUTO_START = 1
    NONE = 0

_DBusObjectManagerClientFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_OBJECT_MANAGER_CLIENT_FLAGS_DO_NOT_AUTO_START",
    "G_DBUS_OBJECT_MANAGER_CLIENT_FLAGS_NONE",
    "do-not-auto-start",
    "none",
]
_DBusObjectManagerClientFlagsValueType: TypeAlias = (
    DBusObjectManagerClientFlags
    | _DBusObjectManagerClientFlagsLiteralType
    | tuple[_DBusObjectManagerClientFlagsLiteralType, ...]
)

class DBusPropertyInfoFlags(GObject.GFlags):
    NONE = 0
    READABLE = 1
    WRITABLE = 2

_DBusPropertyInfoFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_PROPERTY_INFO_FLAGS_NONE",
    "G_DBUS_PROPERTY_INFO_FLAGS_READABLE",
    "G_DBUS_PROPERTY_INFO_FLAGS_WRITABLE",
    "none",
    "readable",
    "writable",
]
_DBusPropertyInfoFlagsValueType: TypeAlias = (
    DBusPropertyInfoFlags
    | _DBusPropertyInfoFlagsLiteralType
    | tuple[_DBusPropertyInfoFlagsLiteralType, ...]
)

class DBusProxyFlags(GObject.GFlags):
    DO_NOT_AUTO_START = 4
    DO_NOT_AUTO_START_AT_CONSTRUCTION = 16
    DO_NOT_CONNECT_SIGNALS = 2
    DO_NOT_LOAD_PROPERTIES = 1
    GET_INVALIDATED_PROPERTIES = 8
    NONE = 0
    NO_MATCH_RULE = 32

_DBusProxyFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_PROXY_FLAGS_DO_NOT_AUTO_START",
    "G_DBUS_PROXY_FLAGS_DO_NOT_AUTO_START_AT_CONSTRUCTION",
    "G_DBUS_PROXY_FLAGS_DO_NOT_CONNECT_SIGNALS",
    "G_DBUS_PROXY_FLAGS_DO_NOT_LOAD_PROPERTIES",
    "G_DBUS_PROXY_FLAGS_GET_INVALIDATED_PROPERTIES",
    "G_DBUS_PROXY_FLAGS_NONE",
    "G_DBUS_PROXY_FLAGS_NO_MATCH_RULE",
    "do-not-auto-start",
    "do-not-auto-start-at-construction",
    "do-not-connect-signals",
    "do-not-load-properties",
    "get-invalidated-properties",
    "no-match-rule",
    "none",
]
_DBusProxyFlagsValueType: TypeAlias = (
    DBusProxyFlags | _DBusProxyFlagsLiteralType | tuple[_DBusProxyFlagsLiteralType, ...]
)

class DBusSendMessageFlags(GObject.GFlags):
    NONE = 0
    PRESERVE_SERIAL = 1

_DBusSendMessageFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_SEND_MESSAGE_FLAGS_NONE",
    "G_DBUS_SEND_MESSAGE_FLAGS_PRESERVE_SERIAL",
    "none",
    "preserve-serial",
]
_DBusSendMessageFlagsValueType: TypeAlias = (
    DBusSendMessageFlags
    | _DBusSendMessageFlagsLiteralType
    | tuple[_DBusSendMessageFlagsLiteralType, ...]
)

class DBusServerFlags(GObject.GFlags):
    AUTHENTICATION_ALLOW_ANONYMOUS = 2
    AUTHENTICATION_REQUIRE_SAME_USER = 4
    NONE = 0
    RUN_IN_THREAD = 1

_DBusServerFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_SERVER_FLAGS_AUTHENTICATION_ALLOW_ANONYMOUS",
    "G_DBUS_SERVER_FLAGS_AUTHENTICATION_REQUIRE_SAME_USER",
    "G_DBUS_SERVER_FLAGS_NONE",
    "G_DBUS_SERVER_FLAGS_RUN_IN_THREAD",
    "authentication-allow-anonymous",
    "authentication-require-same-user",
    "none",
    "run-in-thread",
]
_DBusServerFlagsValueType: TypeAlias = (
    DBusServerFlags
    | _DBusServerFlagsLiteralType
    | tuple[_DBusServerFlagsLiteralType, ...]
)

class DBusSignalFlags(GObject.GFlags):
    MATCH_ARG0_NAMESPACE = 2
    MATCH_ARG0_PATH = 4
    NONE = 0
    NO_MATCH_RULE = 1

_DBusSignalFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_SIGNAL_FLAGS_MATCH_ARG0_NAMESPACE",
    "G_DBUS_SIGNAL_FLAGS_MATCH_ARG0_PATH",
    "G_DBUS_SIGNAL_FLAGS_NONE",
    "G_DBUS_SIGNAL_FLAGS_NO_MATCH_RULE",
    "match-arg0-namespace",
    "match-arg0-path",
    "no-match-rule",
    "none",
]
_DBusSignalFlagsValueType: TypeAlias = (
    DBusSignalFlags
    | _DBusSignalFlagsLiteralType
    | tuple[_DBusSignalFlagsLiteralType, ...]
)

class DBusSubtreeFlags(GObject.GFlags):
    DISPATCH_TO_UNENUMERATED_NODES = 1
    NONE = 0

_DBusSubtreeFlagsLiteralType: TypeAlias = Literal[
    "G_DBUS_SUBTREE_FLAGS_DISPATCH_TO_UNENUMERATED_NODES",
    "G_DBUS_SUBTREE_FLAGS_NONE",
    "dispatch-to-unenumerated-nodes",
    "none",
]
_DBusSubtreeFlagsValueType: TypeAlias = (
    DBusSubtreeFlags
    | _DBusSubtreeFlagsLiteralType
    | tuple[_DBusSubtreeFlagsLiteralType, ...]
)

class DriveStartFlags(GObject.GFlags):
    NONE = 0

_DriveStartFlagsLiteralType: TypeAlias = Literal["G_DRIVE_START_NONE", "none"]
_DriveStartFlagsValueType: TypeAlias = (
    DriveStartFlags
    | _DriveStartFlagsLiteralType
    | tuple[_DriveStartFlagsLiteralType, ...]
)

class FileAttributeInfoFlags(GObject.GFlags):
    COPY_WHEN_MOVED = 2
    COPY_WITH_FILE = 1
    NONE = 0

_FileAttributeInfoFlagsLiteralType: TypeAlias = Literal[
    "G_FILE_ATTRIBUTE_INFO_COPY_WHEN_MOVED",
    "G_FILE_ATTRIBUTE_INFO_COPY_WITH_FILE",
    "G_FILE_ATTRIBUTE_INFO_NONE",
    "copy-when-moved",
    "copy-with-file",
    "none",
]
_FileAttributeInfoFlagsValueType: TypeAlias = (
    FileAttributeInfoFlags
    | _FileAttributeInfoFlagsLiteralType
    | tuple[_FileAttributeInfoFlagsLiteralType, ...]
)

class FileCopyFlags(GObject.GFlags):
    ALL_METADATA = 8
    BACKUP = 2
    NOFOLLOW_SYMLINKS = 4
    NONE = 0
    NO_FALLBACK_FOR_MOVE = 16
    OVERWRITE = 1
    TARGET_DEFAULT_MODIFIED_TIME = 64
    TARGET_DEFAULT_PERMS = 32

_FileCopyFlagsLiteralType: TypeAlias = Literal[
    "G_FILE_COPY_ALL_METADATA",
    "G_FILE_COPY_BACKUP",
    "G_FILE_COPY_NOFOLLOW_SYMLINKS",
    "G_FILE_COPY_NONE",
    "G_FILE_COPY_NO_FALLBACK_FOR_MOVE",
    "G_FILE_COPY_OVERWRITE",
    "G_FILE_COPY_TARGET_DEFAULT_MODIFIED_TIME",
    "G_FILE_COPY_TARGET_DEFAULT_PERMS",
    "all-metadata",
    "backup",
    "no-fallback-for-move",
    "nofollow-symlinks",
    "none",
    "overwrite",
    "target-default-modified-time",
    "target-default-perms",
]
_FileCopyFlagsValueType: TypeAlias = (
    FileCopyFlags | _FileCopyFlagsLiteralType | tuple[_FileCopyFlagsLiteralType, ...]
)

class FileCreateFlags(GObject.GFlags):
    NONE = 0
    PRIVATE = 1
    REPLACE_DESTINATION = 2

_FileCreateFlagsLiteralType: TypeAlias = Literal[
    "G_FILE_CREATE_NONE",
    "G_FILE_CREATE_PRIVATE",
    "G_FILE_CREATE_REPLACE_DESTINATION",
    "none",
    "private",
    "replace-destination",
]
_FileCreateFlagsValueType: TypeAlias = (
    FileCreateFlags
    | _FileCreateFlagsLiteralType
    | tuple[_FileCreateFlagsLiteralType, ...]
)

class FileMeasureFlags(GObject.GFlags):
    APPARENT_SIZE = 4
    NONE = 0
    NO_XDEV = 8
    REPORT_ANY_ERROR = 2

_FileMeasureFlagsLiteralType: TypeAlias = Literal[
    "G_FILE_MEASURE_APPARENT_SIZE",
    "G_FILE_MEASURE_NONE",
    "G_FILE_MEASURE_NO_XDEV",
    "G_FILE_MEASURE_REPORT_ANY_ERROR",
    "apparent-size",
    "no-xdev",
    "none",
    "report-any-error",
]
_FileMeasureFlagsValueType: TypeAlias = (
    FileMeasureFlags
    | _FileMeasureFlagsLiteralType
    | tuple[_FileMeasureFlagsLiteralType, ...]
)

class FileMonitorFlags(GObject.GFlags):
    NONE = 0
    SEND_MOVED = 2
    WATCH_HARD_LINKS = 4
    WATCH_MOUNTS = 1
    WATCH_MOVES = 8

_FileMonitorFlagsLiteralType: TypeAlias = Literal[
    "G_FILE_MONITOR_NONE",
    "G_FILE_MONITOR_SEND_MOVED",
    "G_FILE_MONITOR_WATCH_HARD_LINKS",
    "G_FILE_MONITOR_WATCH_MOUNTS",
    "G_FILE_MONITOR_WATCH_MOVES",
    "none",
    "send-moved",
    "watch-hard-links",
    "watch-mounts",
    "watch-moves",
]
_FileMonitorFlagsValueType: TypeAlias = (
    FileMonitorFlags
    | _FileMonitorFlagsLiteralType
    | tuple[_FileMonitorFlagsLiteralType, ...]
)

class FileQueryInfoFlags(GObject.GFlags):
    NOFOLLOW_SYMLINKS = 1
    NONE = 0

_FileQueryInfoFlagsLiteralType: TypeAlias = Literal[
    "G_FILE_QUERY_INFO_NOFOLLOW_SYMLINKS",
    "G_FILE_QUERY_INFO_NONE",
    "nofollow-symlinks",
    "none",
]
_FileQueryInfoFlagsValueType: TypeAlias = (
    FileQueryInfoFlags
    | _FileQueryInfoFlagsLiteralType
    | tuple[_FileQueryInfoFlagsLiteralType, ...]
)

class IOStreamSpliceFlags(GObject.GFlags):
    CLOSE_STREAM1 = 1
    CLOSE_STREAM2 = 2
    NONE = 0
    WAIT_FOR_BOTH = 4

_IOStreamSpliceFlagsLiteralType: TypeAlias = Literal[
    "G_IO_STREAM_SPLICE_CLOSE_STREAM1",
    "G_IO_STREAM_SPLICE_CLOSE_STREAM2",
    "G_IO_STREAM_SPLICE_NONE",
    "G_IO_STREAM_SPLICE_WAIT_FOR_BOTH",
    "close-stream1",
    "close-stream2",
    "none",
    "wait-for-both",
]
_IOStreamSpliceFlagsValueType: TypeAlias = (
    IOStreamSpliceFlags
    | _IOStreamSpliceFlagsLiteralType
    | tuple[_IOStreamSpliceFlagsLiteralType, ...]
)

class MountMountFlags(GObject.GFlags):
    NONE = 0

_MountMountFlagsLiteralType: TypeAlias = Literal["G_MOUNT_MOUNT_NONE", "none"]
_MountMountFlagsValueType: TypeAlias = (
    MountMountFlags
    | _MountMountFlagsLiteralType
    | tuple[_MountMountFlagsLiteralType, ...]
)

class MountUnmountFlags(GObject.GFlags):
    FORCE = 1
    NONE = 0

_MountUnmountFlagsLiteralType: TypeAlias = Literal[
    "G_MOUNT_UNMOUNT_FORCE", "G_MOUNT_UNMOUNT_NONE", "force", "none"
]
_MountUnmountFlagsValueType: TypeAlias = (
    MountUnmountFlags
    | _MountUnmountFlagsLiteralType
    | tuple[_MountUnmountFlagsLiteralType, ...]
)

class OutputStreamSpliceFlags(GObject.GFlags):
    CLOSE_SOURCE = 1
    CLOSE_TARGET = 2
    NONE = 0

_OutputStreamSpliceFlagsLiteralType: TypeAlias = Literal[
    "G_OUTPUT_STREAM_SPLICE_CLOSE_SOURCE",
    "G_OUTPUT_STREAM_SPLICE_CLOSE_TARGET",
    "G_OUTPUT_STREAM_SPLICE_NONE",
    "close-source",
    "close-target",
    "none",
]
_OutputStreamSpliceFlagsValueType: TypeAlias = (
    OutputStreamSpliceFlags
    | _OutputStreamSpliceFlagsLiteralType
    | tuple[_OutputStreamSpliceFlagsLiteralType, ...]
)

class ResolverNameLookupFlags(GObject.GFlags):
    DEFAULT = 0
    IPV4_ONLY = 1
    IPV6_ONLY = 2

_ResolverNameLookupFlagsLiteralType: TypeAlias = Literal[
    "G_RESOLVER_NAME_LOOKUP_FLAGS_DEFAULT",
    "G_RESOLVER_NAME_LOOKUP_FLAGS_IPV4_ONLY",
    "G_RESOLVER_NAME_LOOKUP_FLAGS_IPV6_ONLY",
    "default",
    "ipv4-only",
    "ipv6-only",
]
_ResolverNameLookupFlagsValueType: TypeAlias = (
    ResolverNameLookupFlags
    | _ResolverNameLookupFlagsLiteralType
    | tuple[_ResolverNameLookupFlagsLiteralType, ...]
)

class ResourceFlags(GObject.GFlags):
    COMPRESSED = 1
    NONE = 0

_ResourceFlagsLiteralType: TypeAlias = Literal[
    "G_RESOURCE_FLAGS_COMPRESSED", "G_RESOURCE_FLAGS_NONE", "compressed", "none"
]
_ResourceFlagsValueType: TypeAlias = (
    ResourceFlags | _ResourceFlagsLiteralType | tuple[_ResourceFlagsLiteralType, ...]
)

class ResourceLookupFlags(GObject.GFlags):
    NONE = 0

_ResourceLookupFlagsLiteralType: TypeAlias = Literal[
    "G_RESOURCE_LOOKUP_FLAGS_NONE", "none"
]
_ResourceLookupFlagsValueType: TypeAlias = (
    ResourceLookupFlags
    | _ResourceLookupFlagsLiteralType
    | tuple[_ResourceLookupFlagsLiteralType, ...]
)

class SettingsBindFlags(GObject.GFlags):
    DEFAULT = 0
    GET = 1
    GET_NO_CHANGES = 8
    INVERT_BOOLEAN = 16
    NO_SENSITIVITY = 4
    SET = 2

_SettingsBindFlagsLiteralType: TypeAlias = Literal[
    "G_SETTINGS_BIND_DEFAULT",
    "G_SETTINGS_BIND_GET",
    "G_SETTINGS_BIND_GET_NO_CHANGES",
    "G_SETTINGS_BIND_INVERT_BOOLEAN",
    "G_SETTINGS_BIND_NO_SENSITIVITY",
    "G_SETTINGS_BIND_SET",
    "default",
    "get",
    "get-no-changes",
    "invert-boolean",
    "no-sensitivity",
    "set",
]
_SettingsBindFlagsValueType: TypeAlias = (
    SettingsBindFlags
    | _SettingsBindFlagsLiteralType
    | tuple[_SettingsBindFlagsLiteralType, ...]
)

class SocketMsgFlags(GObject.GFlags):
    DONTROUTE = 4
    NONE = 0
    OOB = 1
    PEEK = 2

_SocketMsgFlagsLiteralType: TypeAlias = Literal[
    "G_SOCKET_MSG_DONTROUTE",
    "G_SOCKET_MSG_NONE",
    "G_SOCKET_MSG_OOB",
    "G_SOCKET_MSG_PEEK",
    "dontroute",
    "none",
    "oob",
    "peek",
]
_SocketMsgFlagsValueType: TypeAlias = (
    SocketMsgFlags | _SocketMsgFlagsLiteralType | tuple[_SocketMsgFlagsLiteralType, ...]
)

class SubprocessFlags(GObject.GFlags):
    INHERIT_FDS = 128
    NONE = 0
    SEARCH_PATH_FROM_ENVP = 256
    STDERR_MERGE = 64
    STDERR_PIPE = 16
    STDERR_SILENCE = 32
    STDIN_INHERIT = 2
    STDIN_PIPE = 1
    STDOUT_PIPE = 4
    STDOUT_SILENCE = 8

_SubprocessFlagsLiteralType: TypeAlias = Literal[
    "G_SUBPROCESS_FLAGS_INHERIT_FDS",
    "G_SUBPROCESS_FLAGS_NONE",
    "G_SUBPROCESS_FLAGS_SEARCH_PATH_FROM_ENVP",
    "G_SUBPROCESS_FLAGS_STDERR_MERGE",
    "G_SUBPROCESS_FLAGS_STDERR_PIPE",
    "G_SUBPROCESS_FLAGS_STDERR_SILENCE",
    "G_SUBPROCESS_FLAGS_STDIN_INHERIT",
    "G_SUBPROCESS_FLAGS_STDIN_PIPE",
    "G_SUBPROCESS_FLAGS_STDOUT_PIPE",
    "G_SUBPROCESS_FLAGS_STDOUT_SILENCE",
    "inherit-fds",
    "none",
    "search-path-from-envp",
    "stderr-merge",
    "stderr-pipe",
    "stderr-silence",
    "stdin-inherit",
    "stdin-pipe",
    "stdout-pipe",
    "stdout-silence",
]
_SubprocessFlagsValueType: TypeAlias = (
    SubprocessFlags
    | _SubprocessFlagsLiteralType
    | tuple[_SubprocessFlagsLiteralType, ...]
)

class TestDBusFlags(GObject.GFlags):
    NONE = 0

_TestDBusFlagsLiteralType: TypeAlias = Literal["G_TEST_DBUS_NONE", "none"]
_TestDBusFlagsValueType: TypeAlias = (
    TestDBusFlags | _TestDBusFlagsLiteralType | tuple[_TestDBusFlagsLiteralType, ...]
)

class TlsCertificateFlags(GObject.GFlags):
    BAD_IDENTITY = 2
    EXPIRED = 8
    GENERIC_ERROR = 64
    INSECURE = 32
    NOT_ACTIVATED = 4
    NO_FLAGS = 0
    REVOKED = 16
    UNKNOWN_CA = 1
    VALIDATE_ALL = 127

_TlsCertificateFlagsLiteralType: TypeAlias = Literal[
    "G_TLS_CERTIFICATE_BAD_IDENTITY",
    "G_TLS_CERTIFICATE_EXPIRED",
    "G_TLS_CERTIFICATE_GENERIC_ERROR",
    "G_TLS_CERTIFICATE_INSECURE",
    "G_TLS_CERTIFICATE_NOT_ACTIVATED",
    "G_TLS_CERTIFICATE_NO_FLAGS",
    "G_TLS_CERTIFICATE_REVOKED",
    "G_TLS_CERTIFICATE_UNKNOWN_CA",
    "G_TLS_CERTIFICATE_VALIDATE_ALL",
    "bad-identity",
    "expired",
    "generic-error",
    "insecure",
    "no-flags",
    "not-activated",
    "revoked",
    "unknown-ca",
    "validate-all",
]
_TlsCertificateFlagsValueType: TypeAlias = (
    TlsCertificateFlags
    | _TlsCertificateFlagsLiteralType
    | tuple[_TlsCertificateFlagsLiteralType, ...]
)

class TlsDatabaseVerifyFlags(GObject.GFlags):
    NONE = 0

_TlsDatabaseVerifyFlagsLiteralType: TypeAlias = Literal[
    "G_TLS_DATABASE_VERIFY_NONE", "none"
]
_TlsDatabaseVerifyFlagsValueType: TypeAlias = (
    TlsDatabaseVerifyFlags
    | _TlsDatabaseVerifyFlagsLiteralType
    | tuple[_TlsDatabaseVerifyFlagsLiteralType, ...]
)

class TlsPasswordFlags(GObject.GFlags):
    FINAL_TRY = 8
    MANY_TRIES = 4
    NONE = 0
    PKCS11_CONTEXT_SPECIFIC = 64
    PKCS11_SECURITY_OFFICER = 32
    PKCS11_USER = 16
    RETRY = 2

_TlsPasswordFlagsLiteralType: TypeAlias = Literal[
    "G_TLS_PASSWORD_FINAL_TRY",
    "G_TLS_PASSWORD_MANY_TRIES",
    "G_TLS_PASSWORD_NONE",
    "G_TLS_PASSWORD_PKCS11_CONTEXT_SPECIFIC",
    "G_TLS_PASSWORD_PKCS11_SECURITY_OFFICER",
    "G_TLS_PASSWORD_PKCS11_USER",
    "G_TLS_PASSWORD_RETRY",
    "final-try",
    "many-tries",
    "none",
    "pkcs11-context-specific",
    "pkcs11-security-officer",
    "pkcs11-user",
    "retry",
]
_TlsPasswordFlagsValueType: TypeAlias = (
    TlsPasswordFlags
    | _TlsPasswordFlagsLiteralType
    | tuple[_TlsPasswordFlagsLiteralType, ...]
)

class BusType(GObject.GEnum):
    NONE = 0
    SESSION = 2
    STARTER = -1
    SYSTEM = 1

_BusTypeLiteralType: TypeAlias = Literal[
    "G_BUS_TYPE_NONE",
    "G_BUS_TYPE_SESSION",
    "G_BUS_TYPE_STARTER",
    "G_BUS_TYPE_SYSTEM",
    "none",
    "session",
    "starter",
    "system",
]
_BusTypeValueType: TypeAlias = BusType | _BusTypeLiteralType

class ConverterResult(GObject.GEnum):
    CONVERTED = 1
    ERROR = 0
    FINISHED = 2
    FLUSHED = 3

_ConverterResultLiteralType: TypeAlias = Literal[
    "G_CONVERTER_CONVERTED",
    "G_CONVERTER_ERROR",
    "G_CONVERTER_FINISHED",
    "G_CONVERTER_FLUSHED",
    "converted",
    "error",
    "finished",
    "flushed",
]
_ConverterResultValueType: TypeAlias = ConverterResult | _ConverterResultLiteralType

class CredentialsType(GObject.GEnum):
    APPLE_XUCRED = 6
    FREEBSD_CMSGCRED = 2
    INVALID = 0
    LINUX_UCRED = 1
    NETBSD_UNPCBID = 5
    OPENBSD_SOCKPEERCRED = 3
    SOLARIS_UCRED = 4
    WIN32_PID = 7

_CredentialsTypeLiteralType: TypeAlias = Literal[
    "G_CREDENTIALS_TYPE_APPLE_XUCRED",
    "G_CREDENTIALS_TYPE_FREEBSD_CMSGCRED",
    "G_CREDENTIALS_TYPE_INVALID",
    "G_CREDENTIALS_TYPE_LINUX_UCRED",
    "G_CREDENTIALS_TYPE_NETBSD_UNPCBID",
    "G_CREDENTIALS_TYPE_OPENBSD_SOCKPEERCRED",
    "G_CREDENTIALS_TYPE_SOLARIS_UCRED",
    "G_CREDENTIALS_TYPE_WIN32_PID",
    "apple-xucred",
    "freebsd-cmsgcred",
    "invalid",
    "linux-ucred",
    "netbsd-unpcbid",
    "openbsd-sockpeercred",
    "solaris-ucred",
    "win32-pid",
]
_CredentialsTypeValueType: TypeAlias = CredentialsType | _CredentialsTypeLiteralType

class DBusError(GObject.GEnum):
    ACCESS_DENIED = 9
    ADDRESS_IN_USE = 14
    ADT_AUDIT_DATA_UNKNOWN = 39
    AUTH_FAILED = 10
    BAD_ADDRESS = 6
    DISCONNECTED = 15
    FAILED = 0
    FILE_EXISTS = 18
    FILE_NOT_FOUND = 17
    INVALID_ARGS = 16
    INVALID_FILE_CONTENT = 37
    INVALID_SIGNATURE = 36
    IO_ERROR = 5
    LIMITS_EXCEEDED = 8
    MATCH_RULE_INVALID = 22
    MATCH_RULE_NOT_FOUND = 21
    NAME_HAS_NO_OWNER = 3
    NOT_SUPPORTED = 7
    NO_MEMORY = 1
    NO_NETWORK = 13
    NO_REPLY = 4
    NO_SERVER = 11
    OBJECT_PATH_IN_USE = 40
    PROPERTY_READ_ONLY = 44
    SELINUX_SECURITY_CONTEXT_UNKNOWN = 38
    SERVICE_UNKNOWN = 2
    SPAWN_CHILD_EXITED = 25
    SPAWN_CHILD_SIGNALED = 26
    SPAWN_CONFIG_INVALID = 29
    SPAWN_EXEC_FAILED = 23
    SPAWN_FAILED = 27
    SPAWN_FILE_INVALID = 33
    SPAWN_FORK_FAILED = 24
    SPAWN_NO_MEMORY = 34
    SPAWN_PERMISSIONS_INVALID = 32
    SPAWN_SERVICE_INVALID = 30
    SPAWN_SERVICE_NOT_FOUND = 31
    SPAWN_SETUP_FAILED = 28
    TIMED_OUT = 20
    TIMEOUT = 12
    UNIX_PROCESS_ID_UNKNOWN = 35
    UNKNOWN_INTERFACE = 42
    UNKNOWN_METHOD = 19
    UNKNOWN_OBJECT = 41
    UNKNOWN_PROPERTY = 43
    @staticmethod
    def encode_gerror(error: GLib.Error) -> str: ...
    @staticmethod
    def get_remote_error(error: GLib.Error) -> str | None: ...
    @staticmethod
    def is_remote_error(error: GLib.Error) -> bool: ...
    @staticmethod
    def new_for_dbus_error(
        dbus_error_name: str, dbus_error_message: str
    ) -> GLib.Error: ...
    @staticmethod
    def quark() -> int: ...
    @staticmethod
    def register_error(
        error_domain: int, error_code: int, dbus_error_name: str
    ) -> bool: ...
    @staticmethod
    def register_error_domain(
        error_domain_quark_name: str,
        quark_volatile: int,
        entries: Sequence[DBusErrorEntry],
    ) -> None: ...
    @staticmethod
    def strip_remote_error(error: GLib.Error) -> bool: ...
    @staticmethod
    def unregister_error(
        error_domain: int, error_code: int, dbus_error_name: str
    ) -> bool: ...

_DBusErrorLiteralType: TypeAlias = Literal[
    "G_DBUS_ERROR_ACCESS_DENIED",
    "G_DBUS_ERROR_ADDRESS_IN_USE",
    "G_DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN",
    "G_DBUS_ERROR_AUTH_FAILED",
    "G_DBUS_ERROR_BAD_ADDRESS",
    "G_DBUS_ERROR_DISCONNECTED",
    "G_DBUS_ERROR_FAILED",
    "G_DBUS_ERROR_FILE_EXISTS",
    "G_DBUS_ERROR_FILE_NOT_FOUND",
    "G_DBUS_ERROR_INVALID_ARGS",
    "G_DBUS_ERROR_INVALID_FILE_CONTENT",
    "G_DBUS_ERROR_INVALID_SIGNATURE",
    "G_DBUS_ERROR_IO_ERROR",
    "G_DBUS_ERROR_LIMITS_EXCEEDED",
    "G_DBUS_ERROR_MATCH_RULE_INVALID",
    "G_DBUS_ERROR_MATCH_RULE_NOT_FOUND",
    "G_DBUS_ERROR_NAME_HAS_NO_OWNER",
    "G_DBUS_ERROR_NOT_SUPPORTED",
    "G_DBUS_ERROR_NO_MEMORY",
    "G_DBUS_ERROR_NO_NETWORK",
    "G_DBUS_ERROR_NO_REPLY",
    "G_DBUS_ERROR_NO_SERVER",
    "G_DBUS_ERROR_OBJECT_PATH_IN_USE",
    "G_DBUS_ERROR_PROPERTY_READ_ONLY",
    "G_DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN",
    "G_DBUS_ERROR_SERVICE_UNKNOWN",
    "G_DBUS_ERROR_SPAWN_CHILD_EXITED",
    "G_DBUS_ERROR_SPAWN_CHILD_SIGNALED",
    "G_DBUS_ERROR_SPAWN_CONFIG_INVALID",
    "G_DBUS_ERROR_SPAWN_EXEC_FAILED",
    "G_DBUS_ERROR_SPAWN_FAILED",
    "G_DBUS_ERROR_SPAWN_FILE_INVALID",
    "G_DBUS_ERROR_SPAWN_FORK_FAILED",
    "G_DBUS_ERROR_SPAWN_NO_MEMORY",
    "G_DBUS_ERROR_SPAWN_PERMISSIONS_INVALID",
    "G_DBUS_ERROR_SPAWN_SERVICE_INVALID",
    "G_DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND",
    "G_DBUS_ERROR_SPAWN_SETUP_FAILED",
    "G_DBUS_ERROR_TIMED_OUT",
    "G_DBUS_ERROR_TIMEOUT",
    "G_DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN",
    "G_DBUS_ERROR_UNKNOWN_INTERFACE",
    "G_DBUS_ERROR_UNKNOWN_METHOD",
    "G_DBUS_ERROR_UNKNOWN_OBJECT",
    "G_DBUS_ERROR_UNKNOWN_PROPERTY",
    "access-denied",
    "address-in-use",
    "adt-audit-data-unknown",
    "auth-failed",
    "bad-address",
    "disconnected",
    "failed",
    "file-exists",
    "file-not-found",
    "invalid-args",
    "invalid-file-content",
    "invalid-signature",
    "io-error",
    "limits-exceeded",
    "match-rule-invalid",
    "match-rule-not-found",
    "name-has-no-owner",
    "no-memory",
    "no-network",
    "no-reply",
    "no-server",
    "not-supported",
    "object-path-in-use",
    "property-read-only",
    "selinux-security-context-unknown",
    "service-unknown",
    "spawn-child-exited",
    "spawn-child-signaled",
    "spawn-config-invalid",
    "spawn-exec-failed",
    "spawn-failed",
    "spawn-file-invalid",
    "spawn-fork-failed",
    "spawn-no-memory",
    "spawn-permissions-invalid",
    "spawn-service-invalid",
    "spawn-service-not-found",
    "spawn-setup-failed",
    "timed-out",
    "timeout",
    "unix-process-id-unknown",
    "unknown-interface",
    "unknown-method",
    "unknown-object",
    "unknown-property",
]
_DBusErrorValueType: TypeAlias = DBusError | _DBusErrorLiteralType

class DBusMessageByteOrder(GObject.GEnum):
    BIG_ENDIAN = 66
    LITTLE_ENDIAN = 108

_DBusMessageByteOrderLiteralType: TypeAlias = Literal[
    "G_DBUS_MESSAGE_BYTE_ORDER_BIG_ENDIAN",
    "G_DBUS_MESSAGE_BYTE_ORDER_LITTLE_ENDIAN",
    "big-endian",
    "little-endian",
]
_DBusMessageByteOrderValueType: TypeAlias = (
    DBusMessageByteOrder | _DBusMessageByteOrderLiteralType
)

class DBusMessageHeaderField(GObject.GEnum):
    DESTINATION = 6
    ERROR_NAME = 4
    INTERFACE = 2
    INVALID = 0
    MEMBER = 3
    NUM_UNIX_FDS = 9
    PATH = 1
    REPLY_SERIAL = 5
    SENDER = 7
    SIGNATURE = 8

_DBusMessageHeaderFieldLiteralType: TypeAlias = Literal[
    "G_DBUS_MESSAGE_HEADER_FIELD_DESTINATION",
    "G_DBUS_MESSAGE_HEADER_FIELD_ERROR_NAME",
    "G_DBUS_MESSAGE_HEADER_FIELD_INTERFACE",
    "G_DBUS_MESSAGE_HEADER_FIELD_INVALID",
    "G_DBUS_MESSAGE_HEADER_FIELD_MEMBER",
    "G_DBUS_MESSAGE_HEADER_FIELD_NUM_UNIX_FDS",
    "G_DBUS_MESSAGE_HEADER_FIELD_PATH",
    "G_DBUS_MESSAGE_HEADER_FIELD_REPLY_SERIAL",
    "G_DBUS_MESSAGE_HEADER_FIELD_SENDER",
    "G_DBUS_MESSAGE_HEADER_FIELD_SIGNATURE",
    "destination",
    "error-name",
    "interface",
    "invalid",
    "member",
    "num-unix-fds",
    "path",
    "reply-serial",
    "sender",
    "signature",
]
_DBusMessageHeaderFieldValueType: TypeAlias = (
    DBusMessageHeaderField | _DBusMessageHeaderFieldLiteralType
)

class DBusMessageType(GObject.GEnum):
    ERROR = 3
    INVALID = 0
    METHOD_CALL = 1
    METHOD_RETURN = 2
    SIGNAL = 4

_DBusMessageTypeLiteralType: TypeAlias = Literal[
    "G_DBUS_MESSAGE_TYPE_ERROR",
    "G_DBUS_MESSAGE_TYPE_INVALID",
    "G_DBUS_MESSAGE_TYPE_METHOD_CALL",
    "G_DBUS_MESSAGE_TYPE_METHOD_RETURN",
    "G_DBUS_MESSAGE_TYPE_SIGNAL",
    "error",
    "invalid",
    "method-call",
    "method-return",
    "signal",
]
_DBusMessageTypeValueType: TypeAlias = DBusMessageType | _DBusMessageTypeLiteralType

class DataStreamByteOrder(GObject.GEnum):
    BIG_ENDIAN = 0
    HOST_ENDIAN = 2
    LITTLE_ENDIAN = 1

_DataStreamByteOrderLiteralType: TypeAlias = Literal[
    "G_DATA_STREAM_BYTE_ORDER_BIG_ENDIAN",
    "G_DATA_STREAM_BYTE_ORDER_HOST_ENDIAN",
    "G_DATA_STREAM_BYTE_ORDER_LITTLE_ENDIAN",
    "big-endian",
    "host-endian",
    "little-endian",
]
_DataStreamByteOrderValueType: TypeAlias = (
    DataStreamByteOrder | _DataStreamByteOrderLiteralType
)

class DataStreamNewlineType(GObject.GEnum):
    ANY = 3
    CR = 1
    CR_LF = 2
    LF = 0

_DataStreamNewlineTypeLiteralType: TypeAlias = Literal[
    "G_DATA_STREAM_NEWLINE_TYPE_ANY",
    "G_DATA_STREAM_NEWLINE_TYPE_CR",
    "G_DATA_STREAM_NEWLINE_TYPE_CR_LF",
    "G_DATA_STREAM_NEWLINE_TYPE_LF",
    "any",
    "cr",
    "cr-lf",
    "lf",
]
_DataStreamNewlineTypeValueType: TypeAlias = (
    DataStreamNewlineType | _DataStreamNewlineTypeLiteralType
)

class DriveStartStopType(GObject.GEnum):
    MULTIDISK = 3
    NETWORK = 2
    PASSWORD = 4
    SHUTDOWN = 1
    UNKNOWN = 0

_DriveStartStopTypeLiteralType: TypeAlias = Literal[
    "G_DRIVE_START_STOP_TYPE_MULTIDISK",
    "G_DRIVE_START_STOP_TYPE_NETWORK",
    "G_DRIVE_START_STOP_TYPE_PASSWORD",
    "G_DRIVE_START_STOP_TYPE_SHUTDOWN",
    "G_DRIVE_START_STOP_TYPE_UNKNOWN",
    "multidisk",
    "network",
    "password",
    "shutdown",
    "unknown",
]
_DriveStartStopTypeValueType: TypeAlias = (
    DriveStartStopType | _DriveStartStopTypeLiteralType
)

class EmblemOrigin(GObject.GEnum):
    DEVICE = 1
    LIVEMETADATA = 2
    TAG = 3
    UNKNOWN = 0

_EmblemOriginLiteralType: TypeAlias = Literal[
    "G_EMBLEM_ORIGIN_DEVICE",
    "G_EMBLEM_ORIGIN_LIVEMETADATA",
    "G_EMBLEM_ORIGIN_TAG",
    "G_EMBLEM_ORIGIN_UNKNOWN",
    "device",
    "livemetadata",
    "tag",
    "unknown",
]
_EmblemOriginValueType: TypeAlias = EmblemOrigin | _EmblemOriginLiteralType

class FileAttributeStatus(GObject.GEnum):
    ERROR_SETTING = 2
    SET = 1
    UNSET = 0

_FileAttributeStatusLiteralType: TypeAlias = Literal[
    "G_FILE_ATTRIBUTE_STATUS_ERROR_SETTING",
    "G_FILE_ATTRIBUTE_STATUS_SET",
    "G_FILE_ATTRIBUTE_STATUS_UNSET",
    "error-setting",
    "set",
    "unset",
]
_FileAttributeStatusValueType: TypeAlias = (
    FileAttributeStatus | _FileAttributeStatusLiteralType
)

class FileAttributeType(GObject.GEnum):
    BOOLEAN = 3
    BYTE_STRING = 2
    INT32 = 5
    INT64 = 7
    INVALID = 0
    OBJECT = 8
    STRING = 1
    STRINGV = 9
    UINT32 = 4
    UINT64 = 6

_FileAttributeTypeLiteralType: TypeAlias = Literal[
    "G_FILE_ATTRIBUTE_TYPE_BOOLEAN",
    "G_FILE_ATTRIBUTE_TYPE_BYTE_STRING",
    "G_FILE_ATTRIBUTE_TYPE_INT32",
    "G_FILE_ATTRIBUTE_TYPE_INT64",
    "G_FILE_ATTRIBUTE_TYPE_INVALID",
    "G_FILE_ATTRIBUTE_TYPE_OBJECT",
    "G_FILE_ATTRIBUTE_TYPE_STRING",
    "G_FILE_ATTRIBUTE_TYPE_STRINGV",
    "G_FILE_ATTRIBUTE_TYPE_UINT32",
    "G_FILE_ATTRIBUTE_TYPE_UINT64",
    "boolean",
    "byte-string",
    "int32",
    "int64",
    "invalid",
    "object",
    "string",
    "stringv",
    "uint32",
    "uint64",
]
_FileAttributeTypeValueType: TypeAlias = (
    FileAttributeType | _FileAttributeTypeLiteralType
)

class FileMonitorEvent(GObject.GEnum):
    ATTRIBUTE_CHANGED = 4
    CHANGED = 0
    CHANGES_DONE_HINT = 1
    CREATED = 3
    DELETED = 2
    MOVED = 7
    MOVED_IN = 9
    MOVED_OUT = 10
    PRE_UNMOUNT = 5
    RENAMED = 8
    UNMOUNTED = 6

_FileMonitorEventLiteralType: TypeAlias = Literal[
    "G_FILE_MONITOR_EVENT_ATTRIBUTE_CHANGED",
    "G_FILE_MONITOR_EVENT_CHANGED",
    "G_FILE_MONITOR_EVENT_CHANGES_DONE_HINT",
    "G_FILE_MONITOR_EVENT_CREATED",
    "G_FILE_MONITOR_EVENT_DELETED",
    "G_FILE_MONITOR_EVENT_MOVED",
    "G_FILE_MONITOR_EVENT_MOVED_IN",
    "G_FILE_MONITOR_EVENT_MOVED_OUT",
    "G_FILE_MONITOR_EVENT_PRE_UNMOUNT",
    "G_FILE_MONITOR_EVENT_RENAMED",
    "G_FILE_MONITOR_EVENT_UNMOUNTED",
    "attribute-changed",
    "changed",
    "changes-done-hint",
    "created",
    "deleted",
    "moved",
    "moved-in",
    "moved-out",
    "pre-unmount",
    "renamed",
    "unmounted",
]
_FileMonitorEventValueType: TypeAlias = FileMonitorEvent | _FileMonitorEventLiteralType

class FileType(GObject.GEnum):
    DIRECTORY = 2
    MOUNTABLE = 6
    REGULAR = 1
    SHORTCUT = 5
    SPECIAL = 4
    SYMBOLIC_LINK = 3
    UNKNOWN = 0

_FileTypeLiteralType: TypeAlias = Literal[
    "G_FILE_TYPE_DIRECTORY",
    "G_FILE_TYPE_MOUNTABLE",
    "G_FILE_TYPE_REGULAR",
    "G_FILE_TYPE_SHORTCUT",
    "G_FILE_TYPE_SPECIAL",
    "G_FILE_TYPE_SYMBOLIC_LINK",
    "G_FILE_TYPE_UNKNOWN",
    "directory",
    "mountable",
    "regular",
    "shortcut",
    "special",
    "symbolic-link",
    "unknown",
]
_FileTypeValueType: TypeAlias = FileType | _FileTypeLiteralType

class FilesystemPreviewType(GObject.GEnum):
    IF_ALWAYS = 0
    IF_LOCAL = 1
    NEVER = 2

_FilesystemPreviewTypeLiteralType: TypeAlias = Literal[
    "G_FILESYSTEM_PREVIEW_TYPE_IF_ALWAYS",
    "G_FILESYSTEM_PREVIEW_TYPE_IF_LOCAL",
    "G_FILESYSTEM_PREVIEW_TYPE_NEVER",
    "if-always",
    "if-local",
    "never",
]
_FilesystemPreviewTypeValueType: TypeAlias = (
    FilesystemPreviewType | _FilesystemPreviewTypeLiteralType
)

class IOErrorEnum(GObject.GEnum):
    ADDRESS_IN_USE = 33
    ALREADY_MOUNTED = 17
    BROKEN_PIPE = 44
    BUSY = 26
    CANCELLED = 19
    CANT_CREATE_BACKUP = 22
    CLOSED = 18
    CONNECTION_CLOSED = 44
    CONNECTION_REFUSED = 39
    DBUS_ERROR = 36
    DESTINATION_UNSET = 48
    EXISTS = 2
    FAILED = 0
    FAILED_HANDLED = 30
    FILENAME_TOO_LONG = 9
    HOST_NOT_FOUND = 28
    HOST_UNREACHABLE = 37
    INVALID_ARGUMENT = 13
    INVALID_DATA = 35
    INVALID_FILENAME = 10
    IS_DIRECTORY = 3
    MESSAGE_TOO_LARGE = 46
    NETWORK_UNREACHABLE = 38
    NOT_CONNECTED = 45
    NOT_DIRECTORY = 4
    NOT_EMPTY = 5
    NOT_FOUND = 1
    NOT_INITIALIZED = 32
    NOT_MOUNTABLE_FILE = 8
    NOT_MOUNTED = 16
    NOT_REGULAR_FILE = 6
    NOT_SUPPORTED = 15
    NOT_SYMBOLIC_LINK = 7
    NO_SPACE = 12
    NO_SUCH_DEVICE = 47
    PARTIAL_INPUT = 34
    PENDING = 20
    PERMISSION_DENIED = 14
    PROXY_AUTH_FAILED = 41
    PROXY_FAILED = 40
    PROXY_NEED_AUTH = 42
    PROXY_NOT_ALLOWED = 43
    READ_ONLY = 21
    TIMED_OUT = 24
    TOO_MANY_LINKS = 11
    TOO_MANY_OPEN_FILES = 31
    WOULD_BLOCK = 27
    WOULD_MERGE = 29
    WOULD_RECURSE = 25
    WRONG_ETAG = 23

_IOErrorEnumLiteralType: TypeAlias = Literal[
    "G_IO_ERROR_ADDRESS_IN_USE",
    "G_IO_ERROR_ALREADY_MOUNTED",
    "G_IO_ERROR_BROKEN_PIPE",
    "G_IO_ERROR_BUSY",
    "G_IO_ERROR_CANCELLED",
    "G_IO_ERROR_CANT_CREATE_BACKUP",
    "G_IO_ERROR_CLOSED",
    "G_IO_ERROR_CONNECTION_REFUSED",
    "G_IO_ERROR_DBUS_ERROR",
    "G_IO_ERROR_DESTINATION_UNSET",
    "G_IO_ERROR_EXISTS",
    "G_IO_ERROR_FAILED",
    "G_IO_ERROR_FAILED_HANDLED",
    "G_IO_ERROR_FILENAME_TOO_LONG",
    "G_IO_ERROR_HOST_NOT_FOUND",
    "G_IO_ERROR_HOST_UNREACHABLE",
    "G_IO_ERROR_INVALID_ARGUMENT",
    "G_IO_ERROR_INVALID_DATA",
    "G_IO_ERROR_INVALID_FILENAME",
    "G_IO_ERROR_IS_DIRECTORY",
    "G_IO_ERROR_MESSAGE_TOO_LARGE",
    "G_IO_ERROR_NETWORK_UNREACHABLE",
    "G_IO_ERROR_NOT_CONNECTED",
    "G_IO_ERROR_NOT_DIRECTORY",
    "G_IO_ERROR_NOT_EMPTY",
    "G_IO_ERROR_NOT_FOUND",
    "G_IO_ERROR_NOT_INITIALIZED",
    "G_IO_ERROR_NOT_MOUNTABLE_FILE",
    "G_IO_ERROR_NOT_MOUNTED",
    "G_IO_ERROR_NOT_REGULAR_FILE",
    "G_IO_ERROR_NOT_SUPPORTED",
    "G_IO_ERROR_NOT_SYMBOLIC_LINK",
    "G_IO_ERROR_NO_SPACE",
    "G_IO_ERROR_NO_SUCH_DEVICE",
    "G_IO_ERROR_PARTIAL_INPUT",
    "G_IO_ERROR_PENDING",
    "G_IO_ERROR_PERMISSION_DENIED",
    "G_IO_ERROR_PROXY_AUTH_FAILED",
    "G_IO_ERROR_PROXY_FAILED",
    "G_IO_ERROR_PROXY_NEED_AUTH",
    "G_IO_ERROR_PROXY_NOT_ALLOWED",
    "G_IO_ERROR_READ_ONLY",
    "G_IO_ERROR_TIMED_OUT",
    "G_IO_ERROR_TOO_MANY_LINKS",
    "G_IO_ERROR_TOO_MANY_OPEN_FILES",
    "G_IO_ERROR_WOULD_BLOCK",
    "G_IO_ERROR_WOULD_MERGE",
    "G_IO_ERROR_WOULD_RECURSE",
    "G_IO_ERROR_WRONG_ETAG",
    "address-in-use",
    "already-mounted",
    "broken-pipe",
    "busy",
    "cancelled",
    "cant-create-backup",
    "closed",
    "connection-refused",
    "dbus-error",
    "destination-unset",
    "exists",
    "failed",
    "failed-handled",
    "filename-too-long",
    "host-not-found",
    "host-unreachable",
    "invalid-argument",
    "invalid-data",
    "invalid-filename",
    "is-directory",
    "message-too-large",
    "network-unreachable",
    "no-space",
    "no-such-device",
    "not-connected",
    "not-directory",
    "not-empty",
    "not-found",
    "not-initialized",
    "not-mountable-file",
    "not-mounted",
    "not-regular-file",
    "not-supported",
    "not-symbolic-link",
    "partial-input",
    "pending",
    "permission-denied",
    "proxy-auth-failed",
    "proxy-failed",
    "proxy-need-auth",
    "proxy-not-allowed",
    "read-only",
    "timed-out",
    "too-many-links",
    "too-many-open-files",
    "would-block",
    "would-merge",
    "would-recurse",
    "wrong-etag",
]
_IOErrorEnumValueType: TypeAlias = IOErrorEnum | _IOErrorEnumLiteralType

class IOModuleScopeFlags(GObject.GEnum):
    BLOCK_DUPLICATES = 1
    NONE = 0

_IOModuleScopeFlagsLiteralType: TypeAlias = Literal[
    "G_IO_MODULE_SCOPE_BLOCK_DUPLICATES",
    "G_IO_MODULE_SCOPE_NONE",
    "block-duplicates",
    "none",
]
_IOModuleScopeFlagsValueType: TypeAlias = (
    IOModuleScopeFlags | _IOModuleScopeFlagsLiteralType
)

class MemoryMonitorWarningLevel(GObject.GEnum):
    CRITICAL = 255
    LOW = 50
    MEDIUM = 100

_MemoryMonitorWarningLevelLiteralType: TypeAlias = Literal[
    "G_MEMORY_MONITOR_WARNING_LEVEL_CRITICAL",
    "G_MEMORY_MONITOR_WARNING_LEVEL_LOW",
    "G_MEMORY_MONITOR_WARNING_LEVEL_MEDIUM",
    "critical",
    "low",
    "medium",
]
_MemoryMonitorWarningLevelValueType: TypeAlias = (
    MemoryMonitorWarningLevel | _MemoryMonitorWarningLevelLiteralType
)

class MountOperationResult(GObject.GEnum):
    ABORTED = 1
    HANDLED = 0
    UNHANDLED = 2

_MountOperationResultLiteralType: TypeAlias = Literal[
    "G_MOUNT_OPERATION_ABORTED",
    "G_MOUNT_OPERATION_HANDLED",
    "G_MOUNT_OPERATION_UNHANDLED",
    "aborted",
    "handled",
    "unhandled",
]
_MountOperationResultValueType: TypeAlias = (
    MountOperationResult | _MountOperationResultLiteralType
)

class NetworkConnectivity(GObject.GEnum):
    FULL = 4
    LIMITED = 2
    LOCAL = 1
    PORTAL = 3

_NetworkConnectivityLiteralType: TypeAlias = Literal[
    "G_NETWORK_CONNECTIVITY_FULL",
    "G_NETWORK_CONNECTIVITY_LIMITED",
    "G_NETWORK_CONNECTIVITY_LOCAL",
    "G_NETWORK_CONNECTIVITY_PORTAL",
    "full",
    "limited",
    "local",
    "portal",
]
_NetworkConnectivityValueType: TypeAlias = (
    NetworkConnectivity | _NetworkConnectivityLiteralType
)

class NotificationPriority(GObject.GEnum):
    HIGH = 2
    LOW = 1
    NORMAL = 0
    URGENT = 3

_NotificationPriorityLiteralType: TypeAlias = Literal[
    "G_NOTIFICATION_PRIORITY_HIGH",
    "G_NOTIFICATION_PRIORITY_LOW",
    "G_NOTIFICATION_PRIORITY_NORMAL",
    "G_NOTIFICATION_PRIORITY_URGENT",
    "high",
    "low",
    "normal",
    "urgent",
]
_NotificationPriorityValueType: TypeAlias = (
    NotificationPriority | _NotificationPriorityLiteralType
)

class PasswordSave(GObject.GEnum):
    FOR_SESSION = 1
    NEVER = 0
    PERMANENTLY = 2

_PasswordSaveLiteralType: TypeAlias = Literal[
    "G_PASSWORD_SAVE_FOR_SESSION",
    "G_PASSWORD_SAVE_NEVER",
    "G_PASSWORD_SAVE_PERMANENTLY",
    "for-session",
    "never",
    "permanently",
]
_PasswordSaveValueType: TypeAlias = PasswordSave | _PasswordSaveLiteralType

class PollableReturn(GObject.GEnum):
    FAILED = 0
    OK = 1
    WOULD_BLOCK = -27

_PollableReturnLiteralType: TypeAlias = Literal[
    "G_POLLABLE_RETURN_FAILED",
    "G_POLLABLE_RETURN_OK",
    "G_POLLABLE_RETURN_WOULD_BLOCK",
    "failed",
    "ok",
    "would-block",
]
_PollableReturnValueType: TypeAlias = PollableReturn | _PollableReturnLiteralType

class ResolverError(GObject.GEnum):
    INTERNAL = 2
    NOT_FOUND = 0
    TEMPORARY_FAILURE = 1
    @staticmethod
    def quark() -> int: ...

_ResolverErrorLiteralType: TypeAlias = Literal[
    "G_RESOLVER_ERROR_INTERNAL",
    "G_RESOLVER_ERROR_NOT_FOUND",
    "G_RESOLVER_ERROR_TEMPORARY_FAILURE",
    "internal",
    "not-found",
    "temporary-failure",
]
_ResolverErrorValueType: TypeAlias = ResolverError | _ResolverErrorLiteralType

class ResolverRecordType(GObject.GEnum):
    MX = 2
    NS = 5
    SOA = 4
    SRV = 1
    TXT = 3

_ResolverRecordTypeLiteralType: TypeAlias = Literal[
    "G_RESOLVER_RECORD_MX",
    "G_RESOLVER_RECORD_NS",
    "G_RESOLVER_RECORD_SOA",
    "G_RESOLVER_RECORD_SRV",
    "G_RESOLVER_RECORD_TXT",
    "mx",
    "ns",
    "soa",
    "srv",
    "txt",
]
_ResolverRecordTypeValueType: TypeAlias = (
    ResolverRecordType | _ResolverRecordTypeLiteralType
)

class ResourceError(GObject.GEnum):
    INTERNAL = 1
    NOT_FOUND = 0
    @staticmethod
    def quark() -> int: ...

_ResourceErrorLiteralType: TypeAlias = Literal[
    "G_RESOURCE_ERROR_INTERNAL", "G_RESOURCE_ERROR_NOT_FOUND", "internal", "not-found"
]
_ResourceErrorValueType: TypeAlias = ResourceError | _ResourceErrorLiteralType

class SocketClientEvent(GObject.GEnum):
    COMPLETE = 8
    CONNECTED = 3
    CONNECTING = 2
    PROXY_NEGOTIATED = 5
    PROXY_NEGOTIATING = 4
    RESOLVED = 1
    RESOLVING = 0
    TLS_HANDSHAKED = 7
    TLS_HANDSHAKING = 6

_SocketClientEventLiteralType: TypeAlias = Literal[
    "G_SOCKET_CLIENT_COMPLETE",
    "G_SOCKET_CLIENT_CONNECTED",
    "G_SOCKET_CLIENT_CONNECTING",
    "G_SOCKET_CLIENT_PROXY_NEGOTIATED",
    "G_SOCKET_CLIENT_PROXY_NEGOTIATING",
    "G_SOCKET_CLIENT_RESOLVED",
    "G_SOCKET_CLIENT_RESOLVING",
    "G_SOCKET_CLIENT_TLS_HANDSHAKED",
    "G_SOCKET_CLIENT_TLS_HANDSHAKING",
    "complete",
    "connected",
    "connecting",
    "proxy-negotiated",
    "proxy-negotiating",
    "resolved",
    "resolving",
    "tls-handshaked",
    "tls-handshaking",
]
_SocketClientEventValueType: TypeAlias = (
    SocketClientEvent | _SocketClientEventLiteralType
)

class SocketFamily(GObject.GEnum):
    INVALID = 0
    IPV4 = 2
    IPV6 = 10
    UNIX = 1

_SocketFamilyLiteralType: TypeAlias = Literal[
    "G_SOCKET_FAMILY_INVALID",
    "G_SOCKET_FAMILY_IPV4",
    "G_SOCKET_FAMILY_IPV6",
    "G_SOCKET_FAMILY_UNIX",
    "invalid",
    "ipv4",
    "ipv6",
    "unix",
]
_SocketFamilyValueType: TypeAlias = SocketFamily | _SocketFamilyLiteralType

class SocketListenerEvent(GObject.GEnum):
    BINDING = 0
    BOUND = 1
    LISTENED = 3
    LISTENING = 2

_SocketListenerEventLiteralType: TypeAlias = Literal[
    "G_SOCKET_LISTENER_BINDING",
    "G_SOCKET_LISTENER_BOUND",
    "G_SOCKET_LISTENER_LISTENED",
    "G_SOCKET_LISTENER_LISTENING",
    "binding",
    "bound",
    "listened",
    "listening",
]
_SocketListenerEventValueType: TypeAlias = (
    SocketListenerEvent | _SocketListenerEventLiteralType
)

class SocketProtocol(GObject.GEnum):
    DEFAULT = 0
    SCTP = 132
    TCP = 6
    UDP = 17
    UNKNOWN = -1

_SocketProtocolLiteralType: TypeAlias = Literal[
    "G_SOCKET_PROTOCOL_DEFAULT",
    "G_SOCKET_PROTOCOL_SCTP",
    "G_SOCKET_PROTOCOL_TCP",
    "G_SOCKET_PROTOCOL_UDP",
    "G_SOCKET_PROTOCOL_UNKNOWN",
    "default",
    "sctp",
    "tcp",
    "udp",
    "unknown",
]
_SocketProtocolValueType: TypeAlias = SocketProtocol | _SocketProtocolLiteralType

class SocketType(GObject.GEnum):
    DATAGRAM = 2
    INVALID = 0
    SEQPACKET = 3
    STREAM = 1

_SocketTypeLiteralType: TypeAlias = Literal[
    "G_SOCKET_TYPE_DATAGRAM",
    "G_SOCKET_TYPE_INVALID",
    "G_SOCKET_TYPE_SEQPACKET",
    "G_SOCKET_TYPE_STREAM",
    "datagram",
    "invalid",
    "seqpacket",
    "stream",
]
_SocketTypeValueType: TypeAlias = SocketType | _SocketTypeLiteralType

class TlsAuthenticationMode(GObject.GEnum):
    NONE = 0
    REQUESTED = 1
    REQUIRED = 2

_TlsAuthenticationModeLiteralType: TypeAlias = Literal[
    "G_TLS_AUTHENTICATION_NONE",
    "G_TLS_AUTHENTICATION_REQUESTED",
    "G_TLS_AUTHENTICATION_REQUIRED",
    "none",
    "requested",
    "required",
]
_TlsAuthenticationModeValueType: TypeAlias = (
    TlsAuthenticationMode | _TlsAuthenticationModeLiteralType
)

class TlsCertificateRequestFlags(GObject.GEnum):
    NONE = 0

_TlsCertificateRequestFlagsLiteralType: TypeAlias = Literal[
    "G_TLS_CERTIFICATE_REQUEST_NONE", "none"
]
_TlsCertificateRequestFlagsValueType: TypeAlias = (
    TlsCertificateRequestFlags | _TlsCertificateRequestFlagsLiteralType
)

class TlsChannelBindingError(GObject.GEnum):
    GENERAL_ERROR = 4
    INVALID_STATE = 1
    NOT_AVAILABLE = 2
    NOT_IMPLEMENTED = 0
    NOT_SUPPORTED = 3
    @staticmethod
    def quark() -> int: ...

_TlsChannelBindingErrorLiteralType: TypeAlias = Literal[
    "G_TLS_CHANNEL_BINDING_ERROR_GENERAL_ERROR",
    "G_TLS_CHANNEL_BINDING_ERROR_INVALID_STATE",
    "G_TLS_CHANNEL_BINDING_ERROR_NOT_AVAILABLE",
    "G_TLS_CHANNEL_BINDING_ERROR_NOT_IMPLEMENTED",
    "G_TLS_CHANNEL_BINDING_ERROR_NOT_SUPPORTED",
    "general-error",
    "invalid-state",
    "not-available",
    "not-implemented",
    "not-supported",
]
_TlsChannelBindingErrorValueType: TypeAlias = (
    TlsChannelBindingError | _TlsChannelBindingErrorLiteralType
)

class TlsChannelBindingType(GObject.GEnum):
    EXPORTER = 2
    SERVER_END_POINT = 1
    UNIQUE = 0

_TlsChannelBindingTypeLiteralType: TypeAlias = Literal[
    "G_TLS_CHANNEL_BINDING_TLS_EXPORTER",
    "G_TLS_CHANNEL_BINDING_TLS_SERVER_END_POINT",
    "G_TLS_CHANNEL_BINDING_TLS_UNIQUE",
    "exporter",
    "server-end-point",
    "unique",
]
_TlsChannelBindingTypeValueType: TypeAlias = (
    TlsChannelBindingType | _TlsChannelBindingTypeLiteralType
)

class TlsDatabaseLookupFlags(GObject.GEnum):
    KEYPAIR = 1
    NONE = 0

_TlsDatabaseLookupFlagsLiteralType: TypeAlias = Literal[
    "G_TLS_DATABASE_LOOKUP_KEYPAIR", "G_TLS_DATABASE_LOOKUP_NONE", "keypair", "none"
]
_TlsDatabaseLookupFlagsValueType: TypeAlias = (
    TlsDatabaseLookupFlags | _TlsDatabaseLookupFlagsLiteralType
)

class TlsError(GObject.GEnum):
    BAD_CERTIFICATE = 2
    BAD_CERTIFICATE_PASSWORD = 8
    CERTIFICATE_REQUIRED = 5
    EOF = 6
    HANDSHAKE = 4
    INAPPROPRIATE_FALLBACK = 7
    MISC = 1
    NOT_TLS = 3
    UNAVAILABLE = 0
    @staticmethod
    def quark() -> int: ...

_TlsErrorLiteralType: TypeAlias = Literal[
    "G_TLS_ERROR_BAD_CERTIFICATE",
    "G_TLS_ERROR_BAD_CERTIFICATE_PASSWORD",
    "G_TLS_ERROR_CERTIFICATE_REQUIRED",
    "G_TLS_ERROR_EOF",
    "G_TLS_ERROR_HANDSHAKE",
    "G_TLS_ERROR_INAPPROPRIATE_FALLBACK",
    "G_TLS_ERROR_MISC",
    "G_TLS_ERROR_NOT_TLS",
    "G_TLS_ERROR_UNAVAILABLE",
    "bad-certificate",
    "bad-certificate-password",
    "certificate-required",
    "eof",
    "handshake",
    "inappropriate-fallback",
    "misc",
    "not-tls",
    "unavailable",
]
_TlsErrorValueType: TypeAlias = TlsError | _TlsErrorLiteralType

class TlsInteractionResult(GObject.GEnum):
    FAILED = 2
    HANDLED = 1
    UNHANDLED = 0

_TlsInteractionResultLiteralType: TypeAlias = Literal[
    "G_TLS_INTERACTION_FAILED",
    "G_TLS_INTERACTION_HANDLED",
    "G_TLS_INTERACTION_UNHANDLED",
    "failed",
    "handled",
    "unhandled",
]
_TlsInteractionResultValueType: TypeAlias = (
    TlsInteractionResult | _TlsInteractionResultLiteralType
)

class TlsProtocolVersion(GObject.GEnum):
    DTLS_1_0 = 201
    DTLS_1_2 = 202
    SSL_3_0 = 1
    TLS_1_0 = 2
    TLS_1_1 = 3
    TLS_1_2 = 4
    TLS_1_3 = 5
    UNKNOWN = 0

_TlsProtocolVersionLiteralType: TypeAlias = Literal[
    "G_TLS_PROTOCOL_VERSION_DTLS_1_0",
    "G_TLS_PROTOCOL_VERSION_DTLS_1_2",
    "G_TLS_PROTOCOL_VERSION_SSL_3_0",
    "G_TLS_PROTOCOL_VERSION_TLS_1_0",
    "G_TLS_PROTOCOL_VERSION_TLS_1_1",
    "G_TLS_PROTOCOL_VERSION_TLS_1_2",
    "G_TLS_PROTOCOL_VERSION_TLS_1_3",
    "G_TLS_PROTOCOL_VERSION_UNKNOWN",
    "dtls-1-0",
    "dtls-1-2",
    "ssl-3-0",
    "tls-1-0",
    "tls-1-1",
    "tls-1-2",
    "tls-1-3",
    "unknown",
]
_TlsProtocolVersionValueType: TypeAlias = (
    TlsProtocolVersion | _TlsProtocolVersionLiteralType
)

class TlsRehandshakeMode(GObject.GEnum):
    NEVER = 0
    SAFELY = 1
    UNSAFELY = 2

_TlsRehandshakeModeLiteralType: TypeAlias = Literal[
    "G_TLS_REHANDSHAKE_NEVER",
    "G_TLS_REHANDSHAKE_SAFELY",
    "G_TLS_REHANDSHAKE_UNSAFELY",
    "never",
    "safely",
    "unsafely",
]
_TlsRehandshakeModeValueType: TypeAlias = (
    TlsRehandshakeMode | _TlsRehandshakeModeLiteralType
)

class UnixSocketAddressType(GObject.GEnum):
    ABSTRACT = 3
    ABSTRACT_PADDED = 4
    ANONYMOUS = 1
    INVALID = 0
    PATH = 2

_UnixSocketAddressTypeLiteralType: TypeAlias = Literal[
    "G_UNIX_SOCKET_ADDRESS_ABSTRACT",
    "G_UNIX_SOCKET_ADDRESS_ABSTRACT_PADDED",
    "G_UNIX_SOCKET_ADDRESS_ANONYMOUS",
    "G_UNIX_SOCKET_ADDRESS_INVALID",
    "G_UNIX_SOCKET_ADDRESS_PATH",
    "abstract",
    "abstract-padded",
    "anonymous",
    "invalid",
    "path",
]
_UnixSocketAddressTypeValueType: TypeAlias = (
    UnixSocketAddressType | _UnixSocketAddressTypeLiteralType
)

class ZlibCompressorFormat(GObject.GEnum):
    GZIP = 1
    RAW = 2
    ZLIB = 0

_ZlibCompressorFormatLiteralType: TypeAlias = Literal[
    "G_ZLIB_COMPRESSOR_FORMAT_GZIP",
    "G_ZLIB_COMPRESSOR_FORMAT_RAW",
    "G_ZLIB_COMPRESSOR_FORMAT_ZLIB",
    "gzip",
    "raw",
    "zlib",
]
_ZlibCompressorFormatValueType: TypeAlias = (
    ZlibCompressorFormat | _ZlibCompressorFormatLiteralType
)
