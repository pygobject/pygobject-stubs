from __future__ import annotations

from typing import cast
from typing import Final
from typing import Literal
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeAlias
from typing_extensions import TypeVar

from collections.abc import Callable
from functools import wraps

from gi import _gi as GI

_T = TypeVar("_T")


def make_nullable(type_str: str) -> str:
    if not type_str.endswith(" | None") and type_str != "None":
        return f"{type_str} | None"

    return type_str


def get_return_type(return_args: list[str], /) -> str:
    return (
        "None"
        if not return_args
        else return_args[0]
        if len(return_args) == 1
        else f"tuple[{', '.join(return_args)}]"
    )


def generate_full_name(prefix: str, name: str) -> str:
    return f"{prefix}.{name}" if prefix else name


_SCALAR_TAGS: Final = {
    GI.TypeTag.BOOLEAN,
    GI.TypeTag.INT8,
    GI.TypeTag.UINT8,
    GI.TypeTag.INT16,
    GI.TypeTag.UINT16,
    GI.TypeTag.INT32,
    GI.TypeTag.UINT32,
    GI.TypeTag.INT64,
    GI.TypeTag.UINT64,
    GI.TypeTag.FLOAT,
    GI.TypeTag.DOUBLE,
    GI.TypeTag.GTYPE,
    GI.TypeTag.UNICHAR,
}


def is_ref_type(type_info: GI.TypeInfo, /) -> bool:
    """A 'ref type' is one whose GValue payload can be NULL.

    Scalars (bool/int/float/gtype/unichar/enum/flags) cannot.
    Strings, objects, interfaces, boxed, variants, pointers, and
    collections can.
    """

    tag = type_info.get_tag()

    if tag in _SCALAR_TAGS:
        return False

    if tag == GI.TypeTag.INTERFACE:
        # Enums and flags are scalars
        return not isinstance(type_info.get_interface(), GI.EnumInfo)

    return True


if TYPE_CHECKING:
    import enum

    class _MISSING_TYPE(enum.Enum):
        MISSING = enum.auto()

        def __eq__(self, other: object) -> Literal[False]: ...

        def __bool__(self) -> Literal[False]: ...

        def __hash__(self) -> int: ...

        def __repr__(self) -> str: ...

    MissingType: TypeAlias = Literal[_MISSING_TYPE.MISSING]
    MISSING: Final = _MISSING_TYPE.MISSING
else:

    class _MissingSentinel:
        __slots__ = ()

        def __eq__(self, other: object) -> bool:
            return False

        def __bool__(self) -> Literal[False]:
            return False

        def __hash__(self) -> int:
            return 0

        def __repr__(self) -> str:
            return "..."

    MissingType: TypeAlias = _MissingSentinel
    MISSING: Final[MissingType] = _MissingSentinel()


def get_value(value: _T | MissingType, default: _T, /) -> _T:
    return default if value is MISSING else value


def get_finish_func(func: GI.FunctionInfo, /) -> GI.FunctionInfo | None:
    try:
        finish_func = func.get_finish_func()
    except Exception:
        # This can be triggered when functions like `g_set_prgname_once`
        # are defined in the typelib but aren't in the library
        finish_func = None

    return finish_func


_SelfT = TypeVar("_SelfT")
_ReturnT = TypeVar("_ReturnT")
_GetterT: TypeAlias = Callable[[_SelfT], _ReturnT]


@overload
def cache_slot(func: _GetterT[_SelfT, _ReturnT], /) -> _GetterT[_SelfT, _ReturnT]: ...


@overload
def cache_slot(
    *,
    slot_name: str | None = None,
    default: object | None = None,
) -> Callable[[_GetterT[_SelfT, _ReturnT]], _GetterT[_SelfT, _ReturnT]]: ...


def cache_slot(
    func: _GetterT[_SelfT, _ReturnT] | None = None,
    /,
    slot_name: str | None = None,
    default: object | None = None,
) -> (
    _GetterT[_SelfT, _ReturnT]
    | Callable[[_GetterT[_SelfT, _ReturnT]], _GetterT[_SelfT, _ReturnT]]
):
    def wrap(func: _GetterT[_SelfT, _ReturnT]) -> _GetterT[_SelfT, _ReturnT]:
        _slot_name = f"_{func.__name__}" if slot_name is None else slot_name

        @wraps(func)
        def wrapper(self: _SelfT) -> _ReturnT:
            value = getattr(self, _slot_name, default)
            if value is not default:
                return cast("_ReturnT", value)

            value = func(self)

            try:
                setattr(self, _slot_name, value)
            except AttributeError:
                # use object.__setattr__ to bypass frozen dataclass's __setattr
                object.__setattr__(self, _slot_name, value)

            return value

        return wrapper

    if func is None:
        return wrap

    return wrap(func)
