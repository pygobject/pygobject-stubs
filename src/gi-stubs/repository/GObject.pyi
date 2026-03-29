from typing import Any
from typing import Final
from typing import TypeVar

from builtins import property as _property
from collections.abc import Callable
from collections.abc import Sequence
from contextlib import AbstractContextManager
from enum import IntFlag

from gi import _gi
from gi._propertyhelper import Property as _Property
from gi._signalhelper import Signal as _Signal
from gi._signalhelper import SignalOverride as _SignalOverride
from gi.repository import GLib

T = TypeVar("T")

G_MAXDOUBLE: float = 1.7976931348623157e308
G_MAXFLOAT: float = 3.4028234663852886e38
G_MAXINT: int = 2147483647
G_MAXINT16: int = 32767
G_MAXINT32: int = 2147483647
G_MAXINT64: int = 9223372036854775807
G_MAXINT8: int = 127
G_MAXLONG: int = 9223372036854775807
G_MAXOFFSET: int = 9223372036854775807
G_MAXSHORT: int = 32767
G_MAXSIZE: int = 18446744073709551615
G_MAXSSIZE: int = 9223372036854775807
G_MAXUINT: int = 4294967295
G_MAXUINT16: int = 65535
G_MAXUINT32: int = 4294967295
G_MAXUINT64: int = 18446744073709551615
G_MAXUINT8: int = 255
G_MAXULONG: int = 18446744073709551615
G_MAXUSHORT: int = 65535
G_MINDOUBLE: float = 2.2250738585072014e-308
G_MINFLOAT: float = 1.1754943508222875e-38
G_MININT: int = -2147483648
G_MININT16: int = -32768
G_MININT32: int = -2147483648
G_MININT64: int = -9223372036854775808
G_MININT8: int = -128
G_MINLONG: int = -9223372036854775808
G_MINOFFSET: int = -9223372036854775808
G_MINSHORT: int = -32768
G_MINSSIZE: int = -9223372036854775808
IO_ERR: int = 8
IO_FLAG_APPEND: int = 1
IO_FLAG_GET_MASK: int = 31
IO_FLAG_IS_READABLE: int = 4
IO_FLAG_IS_SEEKABLE: int = 16
IO_FLAG_IS_WRITEABLE: int = 8
IO_FLAG_MASK: int = 31
IO_FLAG_NONBLOCK: int = 2
IO_FLAG_SET_MASK: int = 3
IO_HUP: int = 16
IO_IN: int = 1
IO_NVAL: int = 32
IO_OUT: int = 4
IO_PRI: int = 2
IO_STATUS_AGAIN: int = 3
IO_STATUS_EOF: int = 2
IO_STATUS_ERROR: int = 0
IO_STATUS_NORMAL: int = 1
OPTION_ERROR_BAD_VALUE: int = 1
OPTION_ERROR_FAILED: int = 2
OPTION_ERROR_UNKNOWN_OPTION: int = 0
OPTION_FLAG_FILENAME: int = 16
OPTION_FLAG_HIDDEN: int = 1
OPTION_FLAG_IN_MAIN: int = 2
OPTION_FLAG_NOALIAS: int = 64
OPTION_FLAG_NO_ARG: int = 8
OPTION_FLAG_OPTIONAL_ARG: int = 32
OPTION_FLAG_REVERSE: int = 4
OPTION_REMAINING: str = ""
PARAM_CONSTRUCT: int = 4
PARAM_CONSTRUCT_ONLY: int = 8
PARAM_LAX_VALIDATION: int = 16
PARAM_MASK: int = 255
PARAM_READABLE: int = 1
PARAM_READWRITE: int = 3
PARAM_STATIC_STRINGS: int = 224
PARAM_USER_SHIFT: int = 8
PARAM_WRITABLE: int = 2
PRIORITY_DEFAULT: int = 0
PRIORITY_DEFAULT_IDLE: int = 200
PRIORITY_HIGH: int = -100
PRIORITY_HIGH_IDLE: int = 100
PRIORITY_LOW: int = 300
SIGNAL_ACTION: int = 32
SIGNAL_DETAILED: int = 16
SIGNAL_FLAGS_MASK: int = 511
SIGNAL_MATCH_MASK: int = 63
SIGNAL_NO_HOOKS: int = 64
SIGNAL_NO_RECURSE: int = 8
SIGNAL_RUN_CLEANUP: int = 4
SIGNAL_RUN_FIRST: int = 1
SIGNAL_RUN_LAST: int = 2
SPAWN_CHILD_INHERITS_STDIN: int = 32
SPAWN_DO_NOT_REAP_CHILD: int = 2
SPAWN_FILE_AND_ARGV_ZERO: int = 64
SPAWN_LEAVE_DESCRIPTORS_OPEN: int = 1
SPAWN_SEARCH_PATH: int = 4
SPAWN_STDERR_TO_DEV_NULL: int = 16
SPAWN_STDOUT_TO_DEV_NULL: int = 8
TYPE_BOOLEAN: GType = ...
TYPE_BOXED: GType = ...
TYPE_CHAR: GType = ...
TYPE_DOUBLE: GType = ...
TYPE_ENUM: GType = ...
TYPE_FLAGS: GType = ...
TYPE_FLAG_RESERVED_ID_BIT: int = 1
TYPE_FLOAT: GType = ...
TYPE_FUNDAMENTAL_MAX: int = 1020
TYPE_FUNDAMENTAL_SHIFT: int = 2
TYPE_GSTRING: GType = ...
TYPE_GTYPE: GType = ...
TYPE_INT: GType = ...
TYPE_INT64: GType = ...
TYPE_INTERFACE: GType = ...
TYPE_INVALID: GType = ...
TYPE_LONG: GType = ...
TYPE_NONE: GType = ...
TYPE_OBJECT: GType = ...
TYPE_PARAM: GType = ...
TYPE_POINTER: GType = ...
TYPE_PYOBJECT: GType = ...
TYPE_RESERVED_BSE_FIRST: int = 32
TYPE_RESERVED_BSE_LAST: int = 48
TYPE_RESERVED_GLIB_FIRST: int = 22
TYPE_RESERVED_GLIB_LAST: int = 31
TYPE_RESERVED_USER_FIRST: int = 49
TYPE_STRING: GType = ...
TYPE_STRV: GType = ...
TYPE_UCHAR: GType = ...
TYPE_UINT: GType = ...
TYPE_UINT64: GType = ...
TYPE_ULONG: GType = ...
TYPE_UNICHAR: GType = ...
TYPE_VALUE: GType = ...
TYPE_VARIANT: GType = ...
VALUE_COLLECT_FORMAT_MAX_LENGTH: int = 8
VALUE_INTERNED_STRING: int = 268435456
VALUE_NOCOPY_CONTENTS: int = 134217728
features: dict = ...
glib_version: tuple = ...
# override
pygobject_version: Final = _gi.pygobject_version

# override
add_emission_hook: Final = _gi.add_emission_hook

def boxed_copy(boxed_type: type[Any], src_boxed: None) -> None: ...
def boxed_free(boxed_type: type[Any], boxed: None) -> None: ...
def boxed_type_register_static(
    name: str, boxed_copy: Callable[[None], None], boxed_free: Callable[[None], None]
) -> type[Any]: ...
def cclosure_marshal_BOOLEAN__BOXED_BOXED(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_BOOLEAN__FLAGS(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_STRING__OBJECT_POINTER(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__BOOLEAN(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__BOXED(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__CHAR(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__DOUBLE(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__ENUM(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__FLAGS(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__FLOAT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__INT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__LONG(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__OBJECT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__PARAM(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__POINTER(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__STRING(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__UCHAR(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__UINT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__UINT_POINTER(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__ULONG(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__VARIANT(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_VOID__VOID(
    closure: Callable[..., Any],
    return_value: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...
def cclosure_marshal_generic(
    closure: Callable[..., Any],
    return_gvalue: Any,
    n_param_values: int,
    param_values: Any,
    invocation_hint: None,
    marshal_data: None,
) -> None: ...

child_watch_add: Final = GLib.child_watch_add

def clear_signal_handler(handler_id_ptr: int, instance: Object) -> None: ...
def enum_complete_type_info(
    g_enum_type: type[Any], const_values: Sequence[EnumValue]
) -> TypeInfo: ...
def enum_get_value(enum_class: EnumClass, value: int) -> EnumValue | None: ...
def enum_get_value_by_name(enum_class: EnumClass, name: str) -> EnumValue | None: ...
def enum_get_value_by_nick(enum_class: EnumClass, nick: str) -> EnumValue | None: ...
def enum_register_static(
    name: str, const_static_values: Sequence[EnumValue]
) -> type[Any]: ...
def enum_to_string(g_enum_type: type[Any], value: int) -> str: ...

filename_display_basename: Final = GLib.filename_display_basename
filename_display_name: Final = GLib.filename_display_name
filename_from_utf8: Final = GLib.filename_from_utf8

def flags_complete_type_info(
    g_flags_type: type[Any], const_values: Sequence[FlagsValue]
) -> TypeInfo: ...
def flags_get_first_value(flags_class: FlagsClass, value: int) -> FlagsValue | None: ...
def flags_get_value_by_name(
    flags_class: FlagsClass, name: str
) -> FlagsValue | None: ...
def flags_get_value_by_nick(
    flags_class: FlagsClass, nick: str
) -> FlagsValue | None: ...
def flags_register_static(
    name: str, const_static_values: Sequence[FlagsValue]
) -> type[Any]: ...
def flags_to_string(flags_type: type[Any], value: int) -> str: ...

get_application_name: Final = GLib.get_application_name
get_current_time: Final = GLib.get_current_time
get_prgname: Final = GLib.get_prgname

def gtype_get_type() -> type[Any]: ...

idle_add: Final = GLib.idle_add
io_add_watch: Final = GLib.io_add_watch
# override
list_properties: Final = _gi.list_properties
main_context_default: Final = GLib.main_context_default
main_depth: Final = GLib.main_depth
markup_escape_text: Final = GLib.markup_escape_text
# override
new: Final = _gi.new

def param_spec_boolean(
    name: str,
    nick: str | None,
    blurb: str | None,
    default_value: bool,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_boxed(
    name: str,
    nick: str | None,
    blurb: str | None,
    boxed_type: type[Any],
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_char(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_double(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: float,
    maximum: float,
    default_value: float,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_enum(
    name: str,
    nick: str | None,
    blurb: str | None,
    enum_type: type[Any],
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_flags(
    name: str,
    nick: str | None,
    blurb: str | None,
    flags_type: type[Any],
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_float(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: float,
    maximum: float,
    default_value: float,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_gtype(
    name: str,
    nick: str | None,
    blurb: str | None,
    is_a_type: type[Any],
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_int(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_int64(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_long(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_object(
    name: str,
    nick: str | None,
    blurb: str | None,
    object_type: type[Any],
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_param(
    name: str,
    nick: str | None,
    blurb: str | None,
    param_type: type[Any],
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_pointer(
    name: str, nick: str | None, blurb: str | None, flags: ParamFlags
) -> ParamSpec: ...
def param_spec_string(
    name: str,
    nick: str | None,
    blurb: str | None,
    default_value: str | None,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_uchar(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_uint(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_uint64(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_ulong(
    name: str,
    nick: str | None,
    blurb: str | None,
    minimum: int,
    maximum: int,
    default_value: int,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_unichar(
    name: str,
    nick: str | None,
    blurb: str | None,
    default_value: str,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_spec_variant(
    name: str,
    nick: str | None,
    blurb: str | None,
    type: GLib.VariantType,
    default_value: GLib.Variant | None,
    flags: ParamFlags,
) -> ParamSpec: ...
def param_type_register_static(
    name: str, pspec_info: ParamSpecTypeInfo
) -> type[Any]: ...
def param_value_convert(
    pspec: ParamSpec, src_value: Any, dest_value: Any, strict_validation: bool
) -> bool: ...
def param_value_defaults(pspec: ParamSpec, value: Any) -> bool: ...
def param_value_is_valid(pspec: ParamSpec, value: Any) -> bool: ...
def param_value_set_default(pspec: ParamSpec, value: Any) -> None: ...
def param_value_validate(pspec: ParamSpec, value: Any) -> bool: ...
def param_values_cmp(pspec: ParamSpec, value1: Any, value2: Any) -> int: ...
def pointer_type_register_static(name: str) -> type[Any]: ...
def remove_emission_hook(obj: Object, detailed_signal: str, hook_id: int) -> None: ...

set_application_name: Final = GLib.set_application_name
set_prgname: Final = GLib.set_prgname

def signal_accumulator_first_wins(
    ihint, return_accu, handler_return, user_data=None
): ...  # FIXME: Override is missing typing annotation
def signal_accumulator_true_handled(
    ihint, return_accu, handler_return, user_data=None
): ...  # FIXME: Override is missing typing annotation
def signal_add_emission_hook(
    signal_id: int, detail: int, hook_func: Callable[..., bool], *hook_data: Any
) -> int: ...
def signal_chain_from_overridden(
    instance_and_params: Sequence[Any], return_value: Any
) -> None: ...
def signal_connect_closure(
    instance: Object, detailed_signal: str, closure: Callable[..., Any], after: bool
) -> int: ...
def signal_connect_closure_by_id(
    instance: Object,
    signal_id: int,
    detail: int,
    closure: Callable[..., Any],
    after: bool,
) -> int: ...
def signal_emitv(
    instance_and_params: Sequence[Any], signal_id: int, detail: int
) -> Any: ...
def signal_get_invocation_hint(instance: Object) -> SignalInvocationHint | None: ...
def signal_handler_block(obj: Object, handler_id: int) -> AbstractContextManager[None]:
    """
    Blocks the signal handler from being invoked until
    handler_unblock() is called.

    :param GObject.Object obj:
        Object instance to block handlers for.
    :param int handler_id:
        Id of signal to block.
    :returns:
        A context manager which optionally can be used to
        automatically unblock the handler:

    .. code-block:: python

        with GObject.signal_handler_block(obj, id):
            pass
    """

def signal_handler_disconnect(instance: Object, handler_id: int) -> None: ...

# override
def signal_handler_find(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Callable[..., Any] | None,
    func: None,
    data: None,
    *closure: Any,
) -> int: ...
def signal_handler_is_connected(instance: Object, handler_id: int) -> bool: ...
def signal_handler_unblock(instance: Object, handler_id: int) -> None: ...

# override
def signal_handlers_block_matched(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Callable[..., Any] | None,
    func: None,
    data: None,
    *closure: Any,
) -> int: ...
def signal_handlers_destroy(instance: Object) -> None: ...

# override
def signal_handlers_disconnect_matched(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Callable[..., Any] | None,
    func: None,
    data: None,
    *closure: Any,
) -> int: ...

# override
def signal_handlers_unblock_matched(
    instance: Object,
    mask: SignalMatchType,
    signal_id: int,
    detail: int,
    _closure: Callable[..., Any] | None,
    func: None,
    data: None,
    *closure: Any,
) -> int: ...
def signal_has_handler_pending(
    instance: Object, signal_id: int, detail: int, may_be_blocked: bool
) -> bool: ...
def signal_is_valid_name(name: str) -> bool: ...
def signal_list_ids(type_: GType | Object) -> tuple[int, ...]: ...
def signal_list_names(type_: GType | Object) -> tuple[str, ...]: ...
def signal_lookup(name: str, type_: GType | Object) -> int: ...
def signal_name(signal_id: int) -> str | None: ...

# override
signal_new: Final = _gi.signal_new

def signal_override_class_closure(
    signal_id: int, instance_type: type[Any], class_closure: Callable[..., Any]
) -> None: ...
def signal_override_class_handler(
    signal_name: str, instance_type: type[Any], class_handler: Callable[[], None]
) -> None: ...
def signal_parse_name(
    detailed_signal: str, itype: GType | Object, force_detail_quark: bool
) -> tuple[int, int]:
    """
    Parse a detailed signal name into (signal_id, detail).

    :param str detailed_signal:
        Signal name which can include detail.
        For example: "notify:prop_name"
    :returns:
        Tuple of (signal_id, detail)
    :raises ValueError:
        If the given signal is unknown.
    """

def signal_query(
    id_or_name: int | str, type_: GType | Object | None = None
) -> SignalQuery | None: ...
def signal_remove_emission_hook(signal_id: int, hook_id: int) -> None: ...
def signal_stop_emission(instance: Object, signal_id: int, detail: int) -> None: ...
def signal_stop_emission_by_name(instance: Object, detailed_signal: str) -> None: ...
def signal_type_cclosure_new(
    itype: type[Any], struct_offset: int
) -> Callable[..., Any]: ...

source_remove: Final = GLib.source_remove

def source_set_closure(source: GLib.Source, closure: Callable[..., Any]) -> None: ...
def source_set_dummy_callback(source: GLib.Source) -> None: ...

spawn_async: Final = GLib.spawn_async

def strdup_value_contents(value: Any) -> str: ...

threads_init: Final = GLib.threads_init
timeout_add: Final = GLib.timeout_add
timeout_add_seconds: Final = GLib.timeout_add_seconds

def type_add_class_private(class_type: type[Any], private_size: int) -> None: ...
def type_add_instance_private(class_type: type[Any], private_size: int) -> int: ...
def type_add_interface_dynamic(
    instance_type: type[Any], interface_type: type[Any], plugin: TypePlugin
) -> None: ...
def type_add_interface_static(
    instance_type: type[Any], interface_type: type[Any], info: InterfaceInfo
) -> None: ...
def type_check_class_is_a(g_class: TypeClass, is_a_type: type[Any]) -> bool: ...
def type_check_instance(instance: TypeInstance) -> bool: ...
def type_check_instance_is_a(instance: TypeInstance, iface_type: type[Any]) -> bool: ...
def type_check_instance_is_fundamentally_a(
    instance: TypeInstance, fundamental_type: type[Any]
) -> bool: ...
def type_check_is_value_type(type: type[Any]) -> bool: ...
def type_check_value(value: Any) -> bool: ...
def type_check_value_holds(value: Any, type: type[Any]) -> bool: ...
def type_children(type: type[Any]) -> list[type[Any]]: ...
def type_class_adjust_private_offset(
    g_class: None, private_size_or_offset: int
) -> None: ...
def type_class_get(type: type[Any]) -> TypeClass: ...
def type_class_peek(type: type[Any]) -> TypeClass | None: ...
def type_class_peek_static(type: type[Any]) -> TypeClass | None: ...
def type_class_ref(type: type[Any]) -> TypeClass: ...
def type_default_interface_get(g_type: type[Any]) -> TypeInterface: ...
def type_default_interface_peek(g_type: type[Any]) -> TypeInterface: ...
def type_default_interface_ref(g_type: type[Any]) -> TypeInterface: ...
def type_default_interface_unref(g_iface: TypeInterface) -> None: ...
def type_depth(type: type[Any]) -> int: ...
def type_ensure(type: type[Any]) -> None: ...
def type_free_instance(instance: TypeInstance) -> None: ...
def type_from_name(name: str) -> GType: ...
def type_fundamental(type_id: type[Any]) -> type[Any]: ...
def type_fundamental_next() -> type[Any]: ...
def type_get_instance_count(type: type[Any]) -> int: ...
def type_get_plugin(type: type[Any]) -> TypePlugin: ...
def type_get_qdata(type: type[Any], quark: int) -> None: ...
def type_get_type_registration_serial() -> int: ...
def type_init() -> None: ...
def type_init_with_debug_flags(debug_flags: TypeDebugFlags) -> None: ...
def type_interface_add_prerequisite(
    interface_type: type[Any], prerequisite_type: type[Any]
) -> None: ...
def type_interface_get_plugin(
    instance_type: type[Any], interface_type: type[Any]
) -> TypePlugin: ...
def type_interface_instantiatable_prerequisite(
    interface_type: type[Any],
) -> type[Any]: ...
def type_interface_peek(
    instance_class: TypeClass, iface_type: type[Any]
) -> TypeInterface | None: ...
def type_interface_prerequisites(interface_type: type[Any]) -> list[type[Any]]: ...
def type_interfaces(type: type[Any]) -> list[type[Any]]: ...
def type_is_a(type: type[Any], is_a_type: type[Any]) -> bool: ...
def type_name(type: type[Any]) -> str | None: ...
def type_name_from_class(g_class: TypeClass) -> str: ...
def type_name_from_instance(instance: TypeInstance) -> str: ...
def type_next_base(leaf_type: type[Any], root_type: type[Any]) -> type[Any]: ...
def type_parent(type_: GType | Object) -> GType: ...
def type_qname(type: type[Any]) -> int: ...
def type_query(type: type[Any]) -> TypeQuery: ...

# override
type_register: Final = _gi.type_register

def type_register_dynamic(
    parent_type: type[Any], type_name: str, plugin: TypePlugin, flags: TypeFlags
) -> type[Any]: ...
def type_register_fundamental(
    type_id: type[Any],
    type_name: str,
    info: TypeInfo,
    finfo: TypeFundamentalInfo,
    flags: TypeFlags,
) -> type[Any]: ...
def type_register_static(
    parent_type: type[Any], type_name: str, info: TypeInfo, flags: TypeFlags
) -> type[Any]: ...
def type_set_qdata(type: type[Any], quark: int, data: None) -> None: ...
def type_test_flags(type: type[Any], flags: int) -> bool: ...

uri_list_extract_uris: Final = GLib.uri_list_extract_uris

def value_type_compatible(src_type: type[Any], dest_type: type[Any]) -> bool: ...
def value_type_transformable(src_type: type[Any], dest_type: type[Any]) -> bool: ...
def variant_get_gtype() -> type[Any]: ...

class Array(GBoxed): ...

class Binding(Object):
    """
    :Constructors:

    ::

        Binding(**properties)

    Object GBinding

    Properties from GBinding:
      source -> GObject: source
      target -> GObject: target
      source-property -> gchararray: source-property
      target-property -> gchararray: target-property
      flags -> GBindingFlags: flags

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        flags: BindingFlags
        source: Object | None
        source_property: str
        target: Object | None
        target_property: str

    @_property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        flags: BindingFlags = ...,
        source: Object = ...,
        source_property: str = ...,
        target: Object = ...,
        target_property: str = ...,
    ) -> None: ...
    def dup_source(self) -> Object | None: ...
    def dup_target(self) -> Object | None: ...
    def get_flags(self) -> BindingFlags: ...
    def get_source(self) -> Object | None: ...
    def get_source_property(self) -> str: ...
    def get_target(self) -> Object | None: ...
    def get_target_property(self) -> str: ...
    def unbind(self) -> None: ...

class BindingGroup(Object):
    """
    :Constructors:

    ::

        BindingGroup(**properties)
        new() -> GObject.BindingGroup

    Object GBindingGroup

    Properties from GBindingGroup:
      source -> GObject: source

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        source: Object | None

    @_property
    def props(self) -> Props: ...
    def __init__(self, *, source: Object | None = ...) -> None: ...
    def bind(
        self,
        source_property: str,
        target: Object,
        target_property: str,
        flags: BindingFlags,
    ) -> None: ...
    def bind_full(
        self,
        source_property: str,
        target: Object,
        target_property: str,
        flags: BindingFlags,
        transform_to: Callable[..., Any] | None = None,
        transform_from: Callable[..., Any] | None = None,
    ) -> None: ...
    def dup_source(self) -> Object | None: ...
    @classmethod
    def new(cls) -> BindingGroup: ...
    def set_source(self, source: Object | None = None) -> None: ...

class BookmarkFile(GBoxed): ...
class ByteArray(GBoxed): ...
class Bytes(GBoxed): ...

class CClosure(GPointer):
    """
    :Constructors:

    ::

        CClosure()
    """

    closure: Callable[..., Any] = ...
    callback: None = ...
    @staticmethod
    def marshal_BOOLEAN__BOXED_BOXED(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_BOOLEAN__FLAGS(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_STRING__OBJECT_POINTER(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__BOOLEAN(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__BOXED(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__CHAR(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__DOUBLE(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__ENUM(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__FLAGS(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__FLOAT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__INT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__LONG(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__OBJECT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__PARAM(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__POINTER(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__STRING(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__UCHAR(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__UINT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__UINT_POINTER(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__ULONG(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__VARIANT(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_VOID__VOID(
        closure: Callable[..., Any],
        return_value: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...
    @staticmethod
    def marshal_generic(
        closure: Callable[..., Any],
        return_gvalue: Any,
        n_param_values: int,
        param_values: Any,
        invocation_hint: None,
        marshal_data: None,
    ) -> None: ...

class Checksum(GBoxed): ...

class Closure(GBoxed):
    """
    :Constructors:

    ::

        Closure()
        new_object(sizeof_closure:int, object:GObject.Object) -> GObject.Closure
        new_simple(sizeof_closure:int, data=None) -> GObject.Closure
    """
    @_property
    def ref_count(self) -> int: ...
    @_property
    def meta_marshal_nouse(self) -> int: ...
    @_property
    def n_guards(self) -> int: ...
    @_property
    def n_fnotifiers(self) -> int: ...
    @_property
    def n_inotifiers(self) -> int: ...
    @_property
    def in_inotify(self) -> int: ...
    @_property
    def floating(self) -> int: ...
    @_property
    def derivative_flag(self) -> int: ...
    in_marshal: int = ...
    is_invalid: int = ...
    @_property
    def marshal(
        self,
    ) -> Callable[[Callable[..., Any], Any, int, Any, None, None], None]: ...
    @_property
    def data(self) -> None: ...
    @_property
    def notifiers(self) -> ClosureNotifyData: ...
    def invalidate(self) -> None: ...
    def invoke(self, param_values: Sequence[Any], invocation_hint: None) -> Any: ...
    @classmethod
    def new_object(cls, sizeof_closure: int, object: Object) -> Closure: ...
    @classmethod
    def new_simple(cls, sizeof_closure: int, data: None) -> Closure: ...
    def ref(self) -> Callable[..., Any]: ...
    def sink(self) -> None: ...
    def unref(self) -> None: ...

class ClosureNotifyData(GPointer):
    """
    :Constructors:

    ::

        ClosureNotifyData()
    """

    data: None = ...
    notify: Callable[[None, Callable[..., Any]], None] = ...

class Date(GBoxed): ...
class DateTime(GBoxed): ...
class Dir(GBoxed): ...

class EnumClass(GPointer):
    """
    :Constructors:

    ::

        EnumClass()
    """

    g_type_class: TypeClass = ...
    minimum: int = ...
    maximum: int = ...
    n_values: int = ...
    values: list[EnumValue] = ...

class EnumValue(GPointer):
    """
    :Constructors:

    ::

        EnumValue()
    """

    value: int = ...
    value_name: str = ...
    value_nick: str = ...

Error = GLib.Error

class FlagsClass(GPointer):
    """
    :Constructors:

    ::

        FlagsClass()
    """

    g_type_class: TypeClass = ...
    mask: int = ...
    n_values: int = ...
    values: list[FlagsValue] = ...

class FlagsValue(GPointer):
    """
    :Constructors:

    ::

        FlagsValue()
    """

    value: int = ...
    value_name: str = ...
    value_nick: str = ...

class Float(float): ...

GBoxed = _gi.GBoxed
GError = GLib.GError
GInterface = _gi.GInterface
GObject = Object
GObjectWeakRef = _gi.GObjectWeakRef
GParamSpec = ParamSpec
GPointer = _gi.GPointer
GType = _gi.GType

class HashTable(GBoxed): ...
class Hmac(GBoxed): ...

IOChannel = GLib.IOChannel
Idle = GLib.Idle

class InitiallyUnowned(Object):
    """
    :Constructors:

    ::

        InitiallyUnowned(**properties)

    Object GInitiallyUnowned

    Signals from GObject:
      notify (GParam)
    """
    @_property
    def g_type_instance(self) -> TypeInstance: ...
    @_property
    def ref_count(self) -> int: ...
    @_property
    def qdata(self) -> GLib.Data: ...

class InitiallyUnownedClass(GPointer):
    """
    :Constructors:

    ::

        InitiallyUnownedClass()
    """
    @_property
    def g_type_class(self) -> TypeClass: ...
    @_property
    def construct_properties(self) -> list[None]: ...
    @_property
    def constructor(self) -> None: ...
    @_property
    def set_property(self) -> Callable[[Object, int, Any, ParamSpec], None]: ...
    @_property
    def get_property(self) -> Callable[[Object, int, Any, ParamSpec], None]: ...
    @_property
    def dispose(self) -> Callable[[Object], None]: ...
    @_property
    def finalize(self) -> Callable[[Object], None]: ...
    @_property
    def dispatch_properties_changed(
        self,
    ) -> Callable[[Object, int, ParamSpec], None]: ...
    @_property
    def notify(self) -> Callable[[Object, ParamSpec], None]: ...
    @_property
    def constructed(self) -> Callable[[Object], None]: ...
    @_property
    def flags(self) -> int: ...
    @_property
    def n_construct_properties(self) -> int: ...
    @_property
    def pspecs(self) -> None: ...
    @_property
    def n_pspecs(self) -> int: ...
    @_property
    def pdummy(self) -> list[None]: ...

class InterfaceInfo(GPointer):
    """
    :Constructors:

    ::

        InterfaceInfo()
    """

    interface_init: Callable[[TypeInterface, None], None] = ...
    interface_finalize: Callable[[TypeInterface, None], None] = ...
    interface_data: None = ...

class KeyFile(GBoxed): ...

MainContext = GLib.MainContext
MainLoop = GLib.MainLoop

class MappedFile(GBoxed): ...
class MarkupParseContext(GBoxed): ...
class MatchInfo(GBoxed): ...

# override
class Object(_gi.GObject):
    """
    :Constructors:

    ::

        Object(**properties)
        newv(object_type:GType, parameters:list) -> Object

    Object GObject

    Signals from GObject:
      notify (GParam)
    """

    @_property
    def g_type_instance(self) -> TypeInstance: ...
    @_property
    def ref_count(self) -> int: ...
    @_property
    def qdata(self) -> GLib.Data: ...
    def bind_property_full(self, *args: object, **kargs: object): ...
    def compat_control(self, *args: object, **kargs: object): ...
    def connect_data(
        self,
        detailed_signal: str,
        handler: Callable[..., Any],
        *data: object,
        connect_flags: ConnectFlags = ConnectFlags.DEFAULT,
    ) -> int: ...
    def disconnect(self, /, id: int) -> None: ...
    def emit_stop_by_name(self, detailed_signal: str) -> None: ...
    def force_floating(self, *args: object, **kargs: object): ...
    def freeze_notify(self) -> AbstractContextManager[None]: ...
    def get_data(self, *args: object, **kargs: object): ...
    def get_qdata(self, *args: object, **kargs: object): ...
    def getv(self, names: Sequence[str], values: Sequence[Any]) -> None: ...
    def handler_block(self, handler_id: int) -> AbstractContextManager[None]: ...
    def handler_disconnect(self, handler_id: int, /) -> None: ...
    def handler_is_connected(self, handler_id: int, /) -> bool: ...
    def handler_unblock(self, handler_id: int, /) -> None: ...
    def install_properties(self, pspecs: Sequence[ParamSpec]) -> None: ...
    def install_property(self, property_id: int, pspec: ParamSpec) -> None: ...
    def interface_find_property(self, *args: object, **kargs: object): ...
    def interface_install_property(self, *args: object, **kargs: object): ...
    def interface_list_properties(self, *args: object, **kargs: object): ...
    def is_floating(self) -> bool: ...
    def list_properties(self) -> list[ParamSpec]: ...
    @classmethod
    def newv(
        cls, object_type: type[Any], parameters: Sequence[Parameter]
    ) -> Object: ...
    def notify(self, property_name: str, /) -> None: ...
    def notify_by_pspec(self, *args: object, **kargs: object): ...
    def override_property(self, property_id: int, name: str, /) -> None: ...
    def ref(self, *args: object, **kargs: object): ...
    def ref_sink(self, *args: object, **kargs: object): ...
    def replace_data(self, *args: object, **kargs: object): ...
    def replace_qdata(self, *args: object, **kargs: object): ...
    def run_dispose(self) -> None: ...
    def set_data(self, *args: object, **kargs: object): ...
    def steal_data(self, *args: object, **kargs: object): ...
    def steal_qdata(self, *args: object, **kargs: object): ...
    def stop_emission(self, detailed_signal: str) -> None: ...
    def stop_emission_by_name(self, detailed_signal: str, /) -> None: ...
    def thaw_notify(self) -> None: ...
    def unref(self, *args: object, **kargs: object): ...
    def watch_closure(self, *args: object, **kargs: object): ...

class ObjectClass(GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """
    @_property
    def g_type_class(self) -> TypeClass: ...
    @_property
    def construct_properties(self) -> list[None]: ...
    @_property
    def constructor(self) -> None: ...
    @_property
    def set_property(self) -> Callable[[Object, int, Any, ParamSpec], None]: ...
    @_property
    def get_property(self) -> Callable[[Object, int, Any, ParamSpec], None]: ...
    @_property
    def dispose(self) -> Callable[[Object], None]: ...
    @_property
    def finalize(self) -> Callable[[Object], None]: ...
    @_property
    def dispatch_properties_changed(
        self,
    ) -> Callable[[Object, int, ParamSpec], None]: ...
    @_property
    def notify(self) -> Callable[[Object, ParamSpec], None]: ...
    @_property
    def constructed(self) -> Callable[[Object], None]: ...
    @_property
    def flags(self) -> int: ...
    @_property
    def n_construct_properties(self) -> int: ...
    @_property
    def pspecs(self) -> None: ...
    @_property
    def n_pspecs(self) -> int: ...
    @_property
    def pdummy(self) -> list[None]: ...
    def find_property(self, property_name: str) -> ParamSpec: ...
    def install_properties(self, pspecs: Sequence[ParamSpec]) -> None: ...
    def install_property(self, property_id: int, pspec: ParamSpec) -> None: ...
    def list_properties(self) -> list[ParamSpec]: ...
    def override_property(self, property_id: int, name: str) -> None: ...

class ObjectConstructParam(GPointer):
    """
    :Constructors:

    ::

        ObjectConstructParam()
    """

    pspec: ParamSpec = ...
    value: Any = ...

OptionContext = GLib.OptionContext
OptionGroup = GLib.OptionGroup

class ParamSpec(_gi.Fundamental):
    """
    :Constructors:

    ::

        ParamSpec(**properties)
    """
    @_property
    def g_type_instance(self) -> TypeInstance: ...
    @_property
    def name(self) -> str: ...
    @_property
    def flags(self) -> ParamFlags: ...
    @_property
    def value_type(self) -> type[Any]: ...
    @_property
    def owner_type(self) -> type[Any]: ...
    @_property
    def qdata(self) -> GLib.Data: ...
    @_property
    def ref_count(self) -> int: ...
    @_property
    def param_id(self) -> int: ...
    def blurb(fget): ...  # FIXME: Override is missing typing annotation
    def do_finalize(self) -> None: ...
    def do_get_property(
        self, pspec
    ): ...  # FIXME: Override is missing typing annotation
    def do_set_property(
        self, pspec, value
    ): ...  # FIXME: Override is missing typing annotation
    def do_value_is_valid(self, value: Any) -> bool: ...
    def do_value_set_default(self, value: Any) -> None: ...
    def do_value_validate(self, value: Any) -> bool: ...
    def do_values_cmp(self, value1: Any, value2: Any) -> int: ...
    def get_blurb(self) -> str | None: ...
    def get_default_value(self) -> Any: ...
    def get_name(self) -> str: ...
    def get_name_quark(self) -> int: ...
    def get_nick(self) -> str: ...
    def get_qdata(self, quark: int) -> None: ...
    def get_redirect_target(self) -> ParamSpec | None: ...
    @staticmethod
    def is_valid_name(name: str) -> bool: ...
    def nick(fget): ...  # FIXME: Override is missing typing annotation
    def set_qdata(self, quark: int, data: None) -> None: ...
    def sink(self) -> None: ...
    def steal_qdata(self, quark: int) -> None: ...

class ParamSpecBoolean(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecBoolean(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def default_value(self) -> bool: ...

class ParamSpecBoxed(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecBoxed(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...

class ParamSpecChar(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecChar(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecClass(GPointer):
    """
    :Constructors:

    ::

        ParamSpecClass()
    """
    @_property
    def g_type_class(self) -> TypeClass: ...
    @_property
    def value_type(self) -> type[Any]: ...
    @_property
    def finalize(self) -> Callable[[ParamSpec], None]: ...
    @_property
    def value_set_default(self) -> Callable[[ParamSpec, Any], None]: ...
    @_property
    def value_validate(self) -> Callable[[ParamSpec, Any], bool]: ...
    @_property
    def values_cmp(self) -> Callable[[ParamSpec, Any, Any], int]: ...
    @_property
    def value_is_valid(self) -> Callable[[ParamSpec, Any], bool]: ...
    @_property
    def dummy(self) -> list[None]: ...

class ParamSpecDouble(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecDouble(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> float: ...
    @_property
    def maximum(self) -> float: ...
    @_property
    def default_value(self) -> float: ...
    @_property
    def epsilon(self) -> float: ...

class ParamSpecEnum(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecEnum(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def default_value(self) -> int: ...
    def do_get_property(
        self, pspec
    ): ...  # FIXME: Override is missing typing annotation
    def do_set_property(
        self, pspec, value
    ): ...  # FIXME: Override is missing typing annotation
    def enum_class(fget): ...  # FIXME: Override is missing typing annotation

class ParamSpecFlags(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecFlags(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def default_value(self) -> int: ...
    def do_get_property(
        self, pspec
    ): ...  # FIXME: Override is missing typing annotation
    def do_set_property(
        self, pspec, value
    ): ...  # FIXME: Override is missing typing annotation
    def flags_class(fget): ...  # FIXME: Override is missing typing annotation

class ParamSpecFloat(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecFloat(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> float: ...
    @_property
    def maximum(self) -> float: ...
    @_property
    def default_value(self) -> float: ...
    @_property
    def epsilon(self) -> float: ...

class ParamSpecGType(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecGType(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def is_a_type(self) -> type[Any]: ...

class ParamSpecInt(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecInt(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecInt64(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecInt64(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecLong(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecLong(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecObject(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecObject(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...

class ParamSpecOverride(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecOverride(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def overridden(self) -> ParamSpec: ...

class ParamSpecParam(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecParam(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...

class ParamSpecPointer(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecPointer(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...

class ParamSpecPool(GPointer):
    def free(self) -> None: ...
    def insert(self, pspec: ParamSpec, owner_type: type[Any]) -> None: ...
    def list(self, owner_type: type[Any]) -> list[ParamSpec]: ...
    def list_owned(self, owner_type: type[Any]) -> list[ParamSpec]: ...
    def lookup(
        self, param_name: str, owner_type: type[Any], walk_ancestors: bool
    ) -> ParamSpec | None: ...
    def remove(self, pspec: ParamSpec) -> None: ...

class ParamSpecString(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecString(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def default_value(self) -> str: ...
    @_property
    def cset_first(self) -> str: ...
    @_property
    def cset_nth(self) -> str: ...
    @_property
    def substitutor(self) -> int: ...
    @_property
    def null_fold_if_empty(self) -> int: ...
    @_property
    def ensure_non_null(self) -> int: ...

class ParamSpecTypeInfo(GPointer):
    """
    :Constructors:

    ::

        ParamSpecTypeInfo()
    """

    instance_size: int = ...
    n_preallocs: int = ...
    @_property
    def instance_init(self) -> Callable[[ParamSpec], None]: ...
    value_type: type[Any] = ...
    @_property
    def finalize(self) -> Callable[[ParamSpec], None]: ...
    @_property
    def value_set_default(self) -> Callable[[ParamSpec, Any], None]: ...
    @_property
    def value_validate(self) -> Callable[[ParamSpec, Any], bool]: ...
    @_property
    def values_cmp(self) -> Callable[[ParamSpec, Any, Any], int]: ...

class ParamSpecUChar(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUChar(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecUInt(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUInt(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecUInt64(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUInt64(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecULong(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecULong(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def minimum(self) -> int: ...
    @_property
    def maximum(self) -> int: ...
    @_property
    def default_value(self) -> int: ...

class ParamSpecUnichar(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecUnichar(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def default_value(self) -> str: ...

class ParamSpecValueArray(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecValueArray(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def element_spec(self) -> ParamSpec: ...
    @_property
    def fixed_n_elements(self) -> int: ...

class ParamSpecVariant(ParamSpec):
    """
    :Constructors:

    ::

        ParamSpecVariant(**properties)
    """
    @_property
    def parent_instance(self) -> ParamSpec: ...
    @_property
    def type(self) -> GLib.VariantType: ...
    @_property
    def default_value(self) -> GLib.Variant: ...
    @_property
    def padding(self) -> list[None]: ...

class Parameter(GPointer):
    """
    :Constructors:

    ::

        Parameter()
    """

    name: str = ...
    value: Any = ...

class PatternSpec(GBoxed): ...

Pid = GLib.Pid
PollFD = GLib.PollFD
# override
Property = _Property

class PtrArray(GBoxed): ...
class Rand(GBoxed): ...
class Regex(GBoxed): ...

# override
Signal = _Signal

class SignalGroup(Object):
    """
    :Constructors:

    ::

        SignalGroup(**properties)
        new(target_type:GType) -> GObject.SignalGroup

    Object GSignalGroup

    Signals from GSignalGroup:
      bind (GObject)
      unbind ()

    Properties from GSignalGroup:
      target -> GObject: target
      target-type -> GType: target-type

    Signals from GObject:
      notify (GParam)
    """
    class Props(Object.Props):
        target: Object | None
        target_type: type[Any]

    @_property
    def props(self) -> Props: ...
    def __init__(
        self, *, target: Object | None = ..., target_type: type[Any] = ...
    ) -> None: ...
    def block(self) -> None: ...
    def connect_closure(
        self, detailed_signal: str, closure: Callable[..., Any], after: bool
    ) -> None: ...
    def connect_data(
        self,
        detailed_signal: str,
        c_handler: Callable[..., None],
        flags: ConnectFlags,
        *data: Any,
    ) -> None: ...
    def connect_swapped(
        self, detailed_signal: str, c_handler: Callable[..., None], *data: Any
    ) -> None: ...
    def dup_target(self) -> Object | None: ...
    @classmethod
    def new(cls, target_type: type[Any]) -> SignalGroup: ...
    def set_target(self, target: Object | None = None) -> None: ...
    def unblock(self) -> None: ...

class SignalInvocationHint(GPointer):
    """
    :Constructors:

    ::

        SignalInvocationHint()
    """

    signal_id: int = ...
    detail: int = ...
    run_type: SignalFlags = ...

# override
SignalOverride = _SignalOverride

class SignalQuery(GPointer):
    """
    :Constructors:

    ::

        SignalQuery()
    """

    signal_id: int = ...
    signal_name: str = ...
    itype: type[Any] = ...
    signal_flags: SignalFlags = ...
    return_type: type[Any] = ...
    n_params: int = ...
    param_types: list[type[Any]] = ...

Source = GLib.Source

class String(GBoxed): ...
class Strv(GBoxed): ...
class StrvBuilder(GBoxed): ...
class Thread(GBoxed): ...
class TimeZone(GBoxed): ...

Timeout = GLib.Timeout

class Tree(GBoxed): ...

class TypeCValue(GPointer):
    v_double = ...  # FIXME: Constant is missing typing annotation
    v_int = ...  # FIXME: Constant is missing typing annotation
    v_int64 = ...  # FIXME: Constant is missing typing annotation
    v_long = ...  # FIXME: Constant is missing typing annotation
    v_pointer = ...  # FIXME: Constant is missing typing annotation

class TypeClass(GPointer):
    """
    :Constructors:

    ::

        TypeClass()
    """
    @_property
    def g_type(self) -> type[Any]: ...
    def add_private(self, private_size: int) -> None: ...
    @staticmethod
    def adjust_private_offset(g_class: None, private_size_or_offset: int) -> None: ...
    @staticmethod
    def get(type: type[Any]) -> TypeClass: ...
    def get_private(self, private_type: type[Any]) -> None: ...
    @staticmethod
    def peek(type: type[Any]) -> TypeClass | None: ...
    def peek_parent(self) -> TypeClass: ...
    @staticmethod
    def peek_static(type: type[Any]) -> TypeClass | None: ...
    @staticmethod
    def ref(type: type[Any]) -> TypeClass: ...
    def unref(self) -> None: ...

class TypeFundamentalInfo(GPointer):
    """
    :Constructors:

    ::

        TypeFundamentalInfo()
    """

    type_flags: TypeFundamentalFlags = ...

class TypeInfo(GPointer):
    """
    :Constructors:

    ::

        TypeInfo()
    """

    class_size: int = ...
    base_init: Callable[[TypeClass], None] = ...
    base_finalize: Callable[[TypeClass], None] = ...
    class_init: Callable[[TypeClass, None], None] = ...
    class_finalize: Callable[[TypeClass, None], None] = ...
    class_data: None = ...
    instance_size: int = ...
    n_preallocs: int = ...
    instance_init: Callable[[TypeInstance, TypeClass], None] = ...
    value_table: TypeValueTable = ...

class TypeInstance(GPointer):
    """
    :Constructors:

    ::

        TypeInstance()
    """
    @_property
    def g_class(self) -> TypeClass: ...
    def get_private(self, private_type: type[Any]) -> None: ...

class TypeInterface(GPointer):
    """
    :Constructors:

    ::

        TypeInterface()
    """
    @_property
    def g_type(self) -> type[Any]: ...
    @_property
    def g_instance_type(self) -> type[Any]: ...
    @staticmethod
    def add_prerequisite(
        interface_type: type[Any], prerequisite_type: type[Any]
    ) -> None: ...
    @staticmethod
    def get_plugin(
        instance_type: type[Any], interface_type: type[Any]
    ) -> TypePlugin: ...
    @staticmethod
    def instantiatable_prerequisite(interface_type: type[Any]) -> type[Any]: ...
    @staticmethod
    def peek(
        instance_class: TypeClass, iface_type: type[Any]
    ) -> TypeInterface | None: ...
    def peek_parent(self) -> TypeInterface | None: ...
    @staticmethod
    def prerequisites(interface_type: type[Any]) -> list[type[Any]]: ...

# override
class TypeModule(Object, TypePlugin):
    @_property
    def parent_instance(self) -> Object: ...
    @_property
    def use_count(self) -> int: ...
    @_property
    def type_infos(self) -> list[None]: ...
    @_property
    def interface_infos(self) -> list[None]: ...
    @_property
    def name(self) -> str: ...
    def add_interface(
        self,
        instance_type: type[Any],
        interface_type: type[Any],
        interface_info: InterfaceInfo,
    ) -> None: ...
    def do_load(self) -> bool: ...
    def do_unload(self) -> None: ...
    def register_enum(
        self, name: str, const_static_values: Sequence[EnumValue]
    ) -> type[Any]: ...
    def register_flags(
        self, name: str, const_static_values: Sequence[FlagsValue]
    ) -> type[Any]: ...
    def register_type(
        self,
        parent_type: type[Any],
        type_name: str,
        type_info: TypeInfo,
        flags: TypeFlags,
    ) -> type[Any]: ...
    def set_name(self, name: str) -> None: ...
    def unuse(self) -> None: ...
    def use(self) -> bool: ...

class TypeModuleClass(GPointer):
    """
    :Constructors:

    ::

        TypeModuleClass()
    """
    @_property
    def parent_class(self) -> ObjectClass: ...
    @_property
    def load(self) -> Callable[[TypeModule], bool]: ...
    @_property
    def unload(self) -> Callable[[TypeModule], None]: ...
    @_property
    def reserved1(self) -> Callable[[], None]: ...
    @_property
    def reserved2(self) -> Callable[[], None]: ...
    @_property
    def reserved3(self) -> Callable[[], None]: ...
    @_property
    def reserved4(self) -> Callable[[], None]: ...

class TypePlugin(GInterface):
    """
    Interface GTypePlugin
    """
    def complete_interface_info(
        self, instance_type: type[Any], interface_type: type[Any], info: InterfaceInfo
    ) -> None: ...
    def complete_type_info(
        self, g_type: type[Any], info: TypeInfo, value_table: TypeValueTable
    ) -> None: ...
    def unuse(self) -> None: ...
    def use(self) -> None: ...

class TypePluginClass(GPointer):
    """
    :Constructors:

    ::

        TypePluginClass()
    """
    @_property
    def base_iface(self) -> TypeInterface: ...
    use_plugin: Callable[[TypePlugin], None] = ...
    unuse_plugin: Callable[[TypePlugin], None] = ...
    complete_type_info: Callable[
        [TypePlugin, type[Any], TypeInfo, TypeValueTable], None
    ] = ...
    complete_interface_info: Callable[
        [TypePlugin, type[Any], type[Any], InterfaceInfo], None
    ] = ...

class TypeQuery(GPointer):
    """
    :Constructors:

    ::

        TypeQuery()
    """

    type: type[Any] = ...
    type_name: str = ...
    class_size: int = ...
    instance_size: int = ...

class TypeValueTable(GPointer):
    """
    :Constructors:

    ::

        TypeValueTable()
    """

    value_init: Callable[[Any], None] = ...
    value_free: Callable[[Any], None] = ...
    value_copy: Callable[[Any], Any] = ...
    value_peek_pointer: Callable[[Any], None] = ...
    collect_format: str = ...
    collect_value: Callable[[Any, Sequence[TypeCValue], int], str | None] = ...
    lcopy_format: str = ...
    lcopy_value: Callable[[Any, Sequence[TypeCValue], int], str | None] = ...

class Uri(GBoxed): ...

class Value(GBoxed):
    """
    :Constructors:

    ::

        Value()
    """
    @_property
    def g_type(self) -> type[Any]: ...
    data: list[_Value__data__union] = ...
    def __init__(
        self, value_type: GType | None = None, py_value: Any | None = None
    ) -> None: ...
    def copy(self, dest_value: Any) -> None: ...
    def dup_object(self) -> Object | None: ...
    def dup_string(self) -> str | None: ...
    def dup_variant(self) -> GLib.Variant | None: ...
    def fits_pointer(self) -> bool: ...
    def get_boolean(self) -> bool: ...
    def get_boxed(self) -> GBoxed: ...
    def get_char(self) -> int: ...
    def get_double(self) -> float: ...
    def get_enum(self) -> int: ...
    def get_flags(self) -> int: ...
    def get_float(self) -> float: ...
    def get_gtype(self) -> type[Any]: ...
    def get_int(self) -> int: ...
    def get_int64(self) -> int: ...
    def get_long(self) -> int: ...
    def get_object(self) -> Object | None: ...
    def get_param(self) -> ParamSpec: ...
    def get_pointer(self) -> None: ...
    def get_schar(self) -> int: ...
    def get_string(self) -> str | None: ...
    def get_uchar(self) -> int: ...
    def get_uint(self) -> int: ...
    def get_uint64(self) -> int: ...
    def get_ulong(self) -> int: ...
    def get_value(self) -> Any: ...
    def get_variant(self) -> GLib.Variant | None: ...
    def init(self, g_type: type[Any]) -> Any: ...
    def init_from_instance(self, instance: TypeInstance) -> None: ...
    def peek_pointer(self) -> None: ...
    def reset(self) -> Any: ...
    def set_boolean(self, v_boolean: bool) -> None: ...
    def set_boxed(
        self, boxed: GBoxed
    ): ...  # FIXME: Override is missing typing annotation
    def set_boxed_take_ownership(self, v_boxed: None) -> None: ...
    def set_char(self, v_char: int) -> None: ...
    def set_double(self, v_double: float) -> None: ...
    def set_enum(self, v_enum: int) -> None: ...
    def set_flags(self, v_flags: int) -> None: ...
    def set_float(self, v_float: float) -> None: ...
    def set_gtype(self, v_gtype: type[Any]) -> None: ...
    def set_instance(self, instance: None) -> None: ...
    def set_int(self, v_int: int) -> None: ...
    def set_int64(self, v_int64: int) -> None: ...
    def set_interned_string(self, v_string: str | None = None) -> None: ...
    def set_long(self, v_long: int) -> None: ...
    def set_object(self, v_object: Object | None = None) -> None: ...
    def set_param(self, param: ParamSpec | None = None) -> None: ...
    def set_pointer(self, v_pointer: None) -> None: ...
    def set_schar(self, v_char: int) -> None: ...
    def set_static_boxed(self, v_boxed: None) -> None: ...
    def set_static_string(self, v_string: str | None = None) -> None: ...
    def set_string(self, v_string: str | None = None) -> None: ...
    def set_string_take_ownership(self, v_string: str | None = None) -> None: ...
    def set_uchar(self, v_uchar: int) -> None: ...
    def set_uint(self, v_uint: int) -> None: ...
    def set_uint64(self, v_uint64: int) -> None: ...
    def set_ulong(self, v_ulong: int) -> None: ...
    def set_value(self, py_value: Any) -> None: ...
    def set_variant(self, variant: GLib.Variant | None = None) -> None: ...
    def steal_string(self) -> str | None: ...
    def take_boxed(self, v_boxed: None) -> None: ...
    def take_string(self, v_string: str | None = None) -> None: ...
    def take_variant(self, variant: GLib.Variant | None = None) -> None: ...
    def transform(self, dest_value: Any) -> bool: ...
    @staticmethod
    def type_compatible(src_type: type[Any], dest_type: type[Any]) -> bool: ...
    @staticmethod
    def type_transformable(src_type: type[Any], dest_type: type[Any]) -> bool: ...
    def unset(self) -> None: ...

class ValueArray(GBoxed):
    """
    :Constructors:

    ::

        ValueArray()
        new(n_prealloced:int) -> GObject.ValueArray
    """

    n_values: int = ...
    values: Any = ...
    @_property
    def n_prealloced(self) -> int: ...
    def append(self, value: Any | None = None) -> ValueArray: ...
    def copy(self) -> ValueArray: ...
    def get_nth(self, index_: int) -> Any: ...
    def insert(self, index_: int, value: Any | None = None) -> ValueArray: ...
    @classmethod
    def new(cls, n_prealloced: int) -> ValueArray: ...
    def prepend(self, value: Any | None = None) -> ValueArray: ...
    def remove(self, index_: int) -> ValueArray: ...
    def sort(self, compare_func: Callable[..., int], *user_data: Any) -> ValueArray: ...

class VariantBuilder(GBoxed): ...
class VariantDict(GBoxed): ...
class VariantType(GBoxed): ...

Warning = _gi.Warning

class WeakRef(GPointer): ...

class _Value__data__union(GPointer):
    v_double = ...  # FIXME: Constant is missing typing annotation
    v_float = ...  # FIXME: Constant is missing typing annotation
    v_int = ...  # FIXME: Constant is missing typing annotation
    v_int64 = ...  # FIXME: Constant is missing typing annotation
    v_long = ...  # FIXME: Constant is missing typing annotation
    v_pointer = ...  # FIXME: Constant is missing typing annotation
    v_uint = ...  # FIXME: Constant is missing typing annotation
    v_uint64 = ...  # FIXME: Constant is missing typing annotation
    v_ulong = ...  # FIXME: Constant is missing typing annotation

# override
property = Property

class BindingFlags(GFlags):
    BIDIRECTIONAL = 1
    DEFAULT = 0
    INVERT_BOOLEAN = 4
    SYNC_CREATE = 2

class ConnectFlags(IntFlag):
    AFTER = 1
    DEFAULT = 0
    SWAPPED = 2

GFlags = _gi.GFlags
IOCondition = GLib.IOCondition

class ParamFlags(IntFlag):
    CONSTRUCT = 4
    CONSTRUCT_ONLY = 8
    DEPRECATED = 2147483648
    EXPLICIT_NOTIFY = 1073741824
    LAX_VALIDATION = 16
    PRIVATE = 32
    READABLE = 1
    READWRITE = 3
    STATIC_BLURB = 128
    STATIC_NAME = 32
    STATIC_NICK = 64
    WRITABLE = 2

class SignalFlags(IntFlag):
    ACCUMULATOR_FIRST_RUN = 131072
    ACTION = 32
    DEPRECATED = 256
    DETAILED = 16
    MUST_COLLECT = 128
    NO_HOOKS = 64
    NO_RECURSE = 8
    RUN_CLEANUP = 4
    RUN_FIRST = 1
    RUN_LAST = 2

class SignalMatchType(IntFlag):
    CLOSURE = 4
    DATA = 16
    DETAIL = 2
    FUNC = 8
    ID = 1
    UNBLOCKED = 32

class TypeDebugFlags(IntFlag):
    INSTANCE_COUNT = 4
    MASK = 7
    NONE = 0
    OBJECTS = 1
    SIGNALS = 2

class TypeFlags(IntFlag):
    ABSTRACT = 16
    DEPRECATED = 128
    FINAL = 64
    NONE = 0
    VALUE_ABSTRACT = 32

class TypeFundamentalFlags(IntFlag):
    CLASSED = 1
    DEEP_DERIVABLE = 8
    DERIVABLE = 4
    INSTANTIATABLE = 2

# override
GEnum = _gi.GEnum
