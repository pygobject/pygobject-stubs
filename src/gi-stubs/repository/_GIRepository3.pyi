import typing

from gi.repository import GLib
from gi.repository import GObject

T = typing.TypeVar("T")

TYPE_TAG_N_TYPES: int = 22
_lock = ...  # FIXME Constant
_namespace: str = "GIRepository"
_version: str = "3.0"

def invoke_error_quark() -> int: ...
def type_tag_argument_from_hash_pointer(
    storage_type: TypeTag, hash_pointer: None
) -> Argument: ...
def type_tag_hash_pointer_from_argument(
    storage_type: TypeTag, arg: Argument
) -> None: ...
def type_tag_to_string(type: TypeTag) -> str: ...

class ArgInfo(BaseInfo):
    """
    :Constructors:

    ::

        ArgInfo(**properties)
    """

    parent: BaseInfoStack = ...
    padding: list[None] = ...
    def get_closure_index(self) -> typing.Tuple[bool, int]: ...
    def get_destroy_index(self) -> typing.Tuple[bool, int]: ...
    def get_direction(self) -> Direction: ...
    def get_ownership_transfer(self) -> Transfer: ...
    def get_scope(self) -> ScopeType: ...
    def get_type_info(self) -> TypeInfo: ...
    def is_caller_allocates(self) -> bool: ...
    def is_optional(self) -> bool: ...
    def is_return_value(self) -> bool: ...
    def is_skip(self) -> bool: ...
    def load_type_info(self) -> TypeInfo: ...
    def may_be_null(self) -> bool: ...

class Argument(GObject.GPointer):
    v_boolean = ...  # FIXME Constant
    v_double = ...  # FIXME Constant
    v_float = ...  # FIXME Constant
    v_int = ...  # FIXME Constant
    v_int16 = ...  # FIXME Constant
    v_int32 = ...  # FIXME Constant
    v_int64 = ...  # FIXME Constant
    v_int8 = ...  # FIXME Constant
    v_long = ...  # FIXME Constant
    v_pointer = ...  # FIXME Constant
    v_short = ...  # FIXME Constant
    v_size = ...  # FIXME Constant
    v_ssize = ...  # FIXME Constant
    v_string = ...  # FIXME Constant
    v_uint = ...  # FIXME Constant
    v_uint16 = ...  # FIXME Constant
    v_uint32 = ...  # FIXME Constant
    v_uint64 = ...  # FIXME Constant
    v_uint8 = ...  # FIXME Constant
    v_ulong = ...  # FIXME Constant
    v_ushort = ...  # FIXME Constant

class ArrayType:
    ARRAY: ArrayType = 1
    BYTE_ARRAY: ArrayType = 3
    C: ArrayType = 0
    PTR_ARRAY: ArrayType = 2
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class AttributeIter(GObject.GPointer):
    """
    :Constructors:

    ::

        AttributeIter()
    """

    data: None = ...
    _dummy: list[None] = ...

class BaseInfo:
    """
    :Constructors:

    ::

        BaseInfo(**properties)
    """

    def clear(self) -> None: ...
    def equal(self, info2: BaseInfo) -> bool: ...
    def get_attribute(self, name: str) -> typing.Optional[str]: ...
    def get_container(self) -> BaseInfo: ...
    def get_name(self) -> typing.Optional[str]: ...
    def get_namespace(self) -> str: ...
    def get_typelib(self) -> Typelib: ...
    def is_deprecated(self) -> bool: ...
    def iterate_attributes(self) -> typing.Tuple[bool, AttributeIter, str, str]: ...
    def ref(self) -> BaseInfo: ...
    def unref(self) -> None: ...

class BaseInfoClass(GObject.GPointer): ...

class BaseInfoStack(GObject.GPointer):
    """
    :Constructors:

    ::

        BaseInfoStack()
    """

    parent_instance: GObject.TypeInstance = ...
    dummy0: int = ...
    dummy1: list[None] = ...
    dummy2: list[int] = ...
    dummy3: list[None] = ...

class CallableInfo(BaseInfo):
    """
    :Constructors:

    ::

        CallableInfo(**properties)
    """

    def can_throw_gerror(self) -> bool: ...
    def get_arg(self, n: int) -> ArgInfo: ...
    def get_async_function(self) -> typing.Optional[CallableInfo]: ...
    def get_caller_owns(self) -> Transfer: ...
    def get_finish_function(self) -> typing.Optional[CallableInfo]: ...
    def get_instance_ownership_transfer(self) -> Transfer: ...
    def get_n_args(self) -> int: ...
    def get_return_attribute(self, name: str) -> typing.Optional[str]: ...
    def get_return_type(self) -> TypeInfo: ...
    def get_sync_function(self) -> typing.Optional[CallableInfo]: ...
    def invoke(
        self,
        function: None,
        in_args: typing.Sequence[Argument],
        out_args: typing.Sequence[Argument],
    ) -> typing.Tuple[bool, Argument]: ...
    def is_async(self) -> bool: ...
    def is_method(self) -> bool: ...
    def iterate_return_attributes(
        self,
    ) -> typing.Tuple[bool, AttributeIter, str, str]: ...
    def load_arg(self, n: int) -> ArgInfo: ...
    def load_return_type(self) -> TypeInfo: ...
    def may_return_null(self) -> bool: ...
    def skip_return(self) -> bool: ...

class CallbackInfo(CallableInfo): ...

class ConstantInfo(BaseInfo):
    """
    :Constructors:

    ::

        ConstantInfo(**properties)
    """

    def get_type_info(self) -> TypeInfo: ...

class Direction:
    IN: Direction = 0
    INOUT: Direction = 2
    OUT: Direction = 1
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class EnumInfo(RegisteredTypeInfo):
    """
    :Constructors:

    ::

        EnumInfo(**properties)
    """

    def get_error_domain(self) -> typing.Optional[str]: ...
    def get_method(self, n: int) -> FunctionInfo: ...
    def get_n_methods(self) -> int: ...
    def get_n_values(self) -> int: ...
    def get_storage_type(self) -> TypeTag: ...
    def get_value(self, n: int) -> ValueInfo: ...

class FieldInfo(BaseInfo):
    """
    :Constructors:

    ::

        FieldInfo(**properties)
    """

    def get_flags(self) -> FieldInfoFlags: ...
    def get_offset(self) -> int: ...
    def get_size(self) -> int: ...
    def get_type_info(self) -> TypeInfo: ...

class FieldInfoFlags:
    READABLE: FieldInfoFlags = 1
    WRITABLE: FieldInfoFlags = 2
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class FlagsInfo(EnumInfo): ...

class FunctionInfo(CallableInfo):
    """
    :Constructors:

    ::

        FunctionInfo(**properties)
    """

    def get_flags(self) -> FunctionInfoFlags: ...
    def get_property(self) -> typing.Optional[PropertyInfo]: ...
    def get_symbol(self) -> str: ...
    def get_vfunc(self) -> typing.Optional[VFuncInfo]: ...

class FunctionInfoFlags:
    IS_ASYNC: FunctionInfoFlags = 32
    IS_CONSTRUCTOR: FunctionInfoFlags = 2
    IS_GETTER: FunctionInfoFlags = 4
    IS_METHOD: FunctionInfoFlags = 1
    IS_SETTER: FunctionInfoFlags = 8
    WRAPS_VFUNC: FunctionInfoFlags = 16
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class InterfaceInfo(RegisteredTypeInfo):
    """
    :Constructors:

    ::

        InterfaceInfo(**properties)
    """

    def find_method(self, name: str) -> typing.Optional[FunctionInfo]: ...
    def find_signal(self, name: str) -> typing.Optional[SignalInfo]: ...
    def find_vfunc(self, name: str) -> typing.Optional[VFuncInfo]: ...
    def get_constant(self, n: int) -> ConstantInfo: ...
    def get_iface_struct(self) -> typing.Optional[StructInfo]: ...
    def get_method(self, n: int) -> FunctionInfo: ...
    def get_n_constants(self) -> int: ...
    def get_n_methods(self) -> int: ...
    def get_n_prerequisites(self) -> int: ...
    def get_n_properties(self) -> int: ...
    def get_n_signals(self) -> int: ...
    def get_n_vfuncs(self) -> int: ...
    def get_prerequisite(self, n: int) -> BaseInfo: ...
    def get_property(self, n: int) -> PropertyInfo: ...
    def get_signal(self, n: int) -> SignalInfo: ...
    def get_vfunc(self, n: int) -> VFuncInfo: ...

class InvokeError:
    ARGUMENT_MISMATCH: InvokeError = 2
    FAILED: InvokeError = 0
    SYMBOL_NOT_FOUND: InvokeError = 1
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class ObjectInfo(RegisteredTypeInfo):
    """
    :Constructors:

    ::

        ObjectInfo(**properties)
    """

    def find_method(self, name: str) -> typing.Optional[FunctionInfo]: ...
    def find_method_using_interfaces(
        self, name: str
    ) -> typing.Tuple[typing.Optional[FunctionInfo], BaseInfo]: ...
    def find_signal(self, name: str) -> typing.Optional[SignalInfo]: ...
    def find_vfunc(self, name: str) -> typing.Optional[VFuncInfo]: ...
    def find_vfunc_using_interfaces(
        self, name: str
    ) -> typing.Tuple[typing.Optional[VFuncInfo], BaseInfo]: ...
    def get_abstract(self) -> bool: ...
    def get_class_struct(self) -> typing.Optional[StructInfo]: ...
    def get_constant(self, n: int) -> ConstantInfo: ...
    def get_field(self, n: int) -> FieldInfo: ...
    def get_final(self) -> bool: ...
    def get_fundamental(self) -> bool: ...
    def get_get_value_function_name(self) -> typing.Optional[str]: ...
    def get_interface(self, n: int) -> InterfaceInfo: ...
    def get_method(self, n: int) -> FunctionInfo: ...
    def get_n_constants(self) -> int: ...
    def get_n_fields(self) -> int: ...
    def get_n_interfaces(self) -> int: ...
    def get_n_methods(self) -> int: ...
    def get_n_properties(self) -> int: ...
    def get_n_signals(self) -> int: ...
    def get_n_vfuncs(self) -> int: ...
    def get_parent(self) -> typing.Optional[ObjectInfo]: ...
    def get_property(self, n: int) -> PropertyInfo: ...
    def get_ref_function_name(self) -> typing.Optional[str]: ...
    def get_set_value_function_name(self) -> typing.Optional[str]: ...
    def get_signal(self, n: int) -> SignalInfo: ...
    def get_type_init_function_name(self) -> str: ...
    def get_type_name(self) -> str: ...
    def get_unref_function_name(self) -> typing.Optional[str]: ...
    def get_vfunc(self, n: int) -> VFuncInfo: ...

class PropertyInfo(BaseInfo):
    """
    :Constructors:

    ::

        PropertyInfo(**properties)
    """

    def get_flags(self) -> GObject.ParamFlags: ...
    def get_getter(self) -> typing.Optional[FunctionInfo]: ...
    def get_ownership_transfer(self) -> Transfer: ...
    def get_setter(self) -> typing.Optional[FunctionInfo]: ...
    def get_type_info(self) -> TypeInfo: ...

class RegisteredTypeInfo(BaseInfo):
    """
    :Constructors:

    ::

        RegisteredTypeInfo(**properties)
    """

    def get_g_type(self) -> typing.Type[typing.Any]: ...
    def get_type_init_function_name(self) -> typing.Optional[str]: ...
    def get_type_name(self) -> typing.Optional[str]: ...
    def is_boxed(self) -> bool: ...

class Repository(GObject.Object):
    """
    :Constructors:

    ::

        Repository(**properties)
        new() -> GIRepository.Repository

    Object GIRepository

    Signals from GObject:
      notify (GParam)
    """

    @staticmethod
    def dump(input_filename: str, output_filename: str) -> bool: ...
    def enumerate_versions(self, namespace_: str) -> list[str]: ...
    @staticmethod
    def error_quark() -> int: ...
    def find_by_error_domain(self, domain: int) -> typing.Optional[EnumInfo]: ...
    def find_by_gtype(
        self, gtype: typing.Type[typing.Any]
    ) -> typing.Optional[BaseInfo]: ...
    def find_by_name(self, namespace_: str, name: str) -> typing.Optional[BaseInfo]: ...
    def get_c_prefix(self, namespace_: str) -> typing.Optional[str]: ...
    def get_dependencies(self, namespace_: str) -> list[str]: ...
    def get_immediate_dependencies(self, namespace_: str) -> list[str]: ...
    def get_info(self, namespace_: str, idx: int) -> BaseInfo: ...
    def get_library_path(self) -> list[str]: ...
    def get_loaded_namespaces(self) -> list[str]: ...
    def get_n_infos(self, namespace_: str) -> int: ...
    def get_object_gtype_interfaces(
        self, gtype: typing.Type[typing.Any]
    ) -> list[InterfaceInfo]: ...
    @staticmethod
    def get_option_group() -> GLib.OptionGroup: ...
    def get_search_path(self) -> list[str]: ...
    def get_shared_libraries(self, namespace_: str) -> typing.Optional[list[str]]: ...
    def get_typelib_path(self, namespace_: str) -> typing.Optional[str]: ...
    def get_version(self, namespace_: str) -> str: ...
    def is_registered(
        self, namespace_: str, version: typing.Optional[str] = None
    ) -> bool: ...
    def load_typelib(self, typelib: Typelib, flags: RepositoryLoadFlags) -> str: ...
    def new() -> Repository: ...  # FIXME Function
    def prepend_library_path(self, directory: str) -> None: ...
    def prepend_search_path(self, directory: str) -> None: ...
    def require(
        self, namespace_: str, version: typing.Optional[str], flags: RepositoryLoadFlags
    ) -> Typelib: ...
    def require_private(
        self,
        typelib_dir: str,
        namespace_: str,
        version: typing.Optional[str],
        flags: RepositoryLoadFlags,
    ) -> Typelib: ...

class RepositoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RepositoryClass()
    """

    parent_class: GObject.ObjectClass = ...

class RepositoryError:
    LIBRARY_NOT_FOUND: RepositoryError = 3
    NAMESPACE_MISMATCH: RepositoryError = 1
    NAMESPACE_VERSION_CONFLICT: RepositoryError = 2
    TYPELIB_NOT_FOUND: RepositoryError = 0
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class RepositoryLoadFlags:
    LAZY: RepositoryLoadFlags = 1
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class ScopeType:
    ASYNC: ScopeType = 2
    CALL: ScopeType = 1
    FOREVER: ScopeType = 4
    INVALID: ScopeType = 0
    NOTIFIED: ScopeType = 3
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class SignalInfo(CallableInfo):
    """
    :Constructors:

    ::

        SignalInfo(**properties)
    """

    def get_class_closure(self) -> typing.Optional[VFuncInfo]: ...
    def get_flags(self) -> GObject.SignalFlags: ...
    def true_stops_emit(self) -> bool: ...

class StructInfo(RegisteredTypeInfo):
    """
    :Constructors:

    ::

        StructInfo(**properties)
    """

    def find_field(self, name: str) -> typing.Optional[FieldInfo]: ...
    def find_method(self, name: str) -> typing.Optional[FunctionInfo]: ...
    def get_alignment(self) -> int: ...
    def get_copy_function_name(self) -> typing.Optional[str]: ...
    def get_field(self, n: int) -> FieldInfo: ...
    def get_free_function_name(self) -> typing.Optional[str]: ...
    def get_method(self, n: int) -> FunctionInfo: ...
    def get_n_fields(self) -> int: ...
    def get_n_methods(self) -> int: ...
    def get_size(self) -> int: ...
    def is_foreign(self) -> bool: ...
    def is_gtype_struct(self) -> bool: ...

class Transfer:
    CONTAINER: Transfer = 1
    EVERYTHING: Transfer = 2
    NOTHING: Transfer = 0
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class TypeInfo(BaseInfo):
    """
    :Constructors:

    ::

        TypeInfo(**properties)
    """

    parent: BaseInfoStack = ...
    padding: list[None] = ...
    def argument_from_hash_pointer(self, hash_pointer: None) -> Argument: ...
    def get_array_fixed_size(self) -> typing.Tuple[bool, int]: ...
    def get_array_length_index(self) -> typing.Tuple[bool, int]: ...
    def get_array_type(self) -> ArrayType: ...
    def get_interface(self) -> typing.Optional[BaseInfo]: ...
    def get_param_type(self, n: int) -> typing.Optional[TypeInfo]: ...
    def get_storage_type(self) -> TypeTag: ...
    def get_tag(self) -> TypeTag: ...
    def hash_pointer_from_argument(self, arg: Argument) -> None: ...
    def is_pointer(self) -> bool: ...
    def is_zero_terminated(self) -> bool: ...

class TypeTag:
    ARRAY: TypeTag = 15
    BOOLEAN: TypeTag = 1
    DOUBLE: TypeTag = 11
    ERROR: TypeTag = 20
    FILENAME: TypeTag = 14
    FLOAT: TypeTag = 10
    GHASH: TypeTag = 19
    GLIST: TypeTag = 17
    GSLIST: TypeTag = 18
    GTYPE: TypeTag = 12
    INT16: TypeTag = 4
    INT32: TypeTag = 6
    INT64: TypeTag = 8
    INT8: TypeTag = 2
    INTERFACE: TypeTag = 16
    UINT16: TypeTag = 5
    UINT32: TypeTag = 7
    UINT64: TypeTag = 9
    UINT8: TypeTag = 3
    UNICHAR: TypeTag = 21
    UTF8: TypeTag = 13
    VOID: TypeTag = 0
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class Typelib(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_bytes(bytes:GLib.Bytes) -> GIRepository.Typelib
    """

    def get_namespace(self) -> str: ...
    def new_from_bytes(bytes: GLib.Bytes) -> Typelib: ...  # FIXME Function
    def ref(self) -> Typelib: ...
    def symbol(self, symbol_name: str) -> typing.Tuple[bool, None]: ...
    def unref(self) -> None: ...

class UnionInfo(RegisteredTypeInfo):
    """
    :Constructors:

    ::

        UnionInfo(**properties)
    """

    def find_method(self, name: str) -> typing.Optional[FunctionInfo]: ...
    def get_alignment(self) -> int: ...
    def get_copy_function_name(self) -> typing.Optional[str]: ...
    def get_discriminator(self, n: int) -> typing.Optional[ConstantInfo]: ...
    def get_discriminator_offset(self) -> typing.Tuple[bool, int]: ...
    def get_discriminator_type(self) -> typing.Optional[TypeInfo]: ...
    def get_field(self, n: int) -> FieldInfo: ...
    def get_free_function_name(self) -> typing.Optional[str]: ...
    def get_method(self, n: int) -> FunctionInfo: ...
    def get_n_fields(self) -> int: ...
    def get_n_methods(self) -> int: ...
    def get_size(self) -> int: ...
    def is_discriminated(self) -> bool: ...

class UnresolvedInfo(BaseInfo): ...

class VFuncInfo(CallableInfo):
    """
    :Constructors:

    ::

        VFuncInfo(**properties)
    """

    def get_address(self, implementor_gtype: typing.Type[typing.Any]) -> None: ...
    def get_flags(self) -> VFuncInfoFlags: ...
    def get_invoker(self) -> typing.Optional[FunctionInfo]: ...
    def get_offset(self) -> int: ...
    def get_signal(self) -> typing.Optional[SignalInfo]: ...

class VFuncInfoFlags:
    CHAIN_UP: VFuncInfoFlags = 1
    NOT_OVERRIDE: VFuncInfoFlags = 4
    OVERRIDE: VFuncInfoFlags = 2
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function

class ValueInfo(BaseInfo):
    """
    :Constructors:

    ::

        ValueInfo(**properties)
    """

    def get_value(self) -> int: ...
