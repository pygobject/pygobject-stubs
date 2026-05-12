from __future__ import annotations

from typing import Final

from gi import _gi as GI


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
