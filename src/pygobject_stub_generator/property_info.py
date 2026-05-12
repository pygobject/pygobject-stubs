from __future__ import annotations

from typing import TYPE_CHECKING

from dataclasses import dataclass
from dataclasses import field

from gi.repository import GObject

from .utils import is_ref_type

if TYPE_CHECKING:
    import gi._gi as GI
    from gi.repository import _GIRepository3 as GIRepository

    from .stub import Stub


@dataclass(slots=True)
class PropertyInfo:
    stub: Stub
    gi_info: GI.PropertyInfo

    # Needed for get_getter() and get_setter() because GI.PropertyInfo doesn't have them
    gir_info: GIRepository.PropertyInfo

    gobject_name: str = field(init=False)
    name: str = field(init=False)

    _type_info: GI.TypeInfo | None = field(init=False, default=None)
    _nullability: tuple[bool, bool] | None = field(init=False, default=None)
    _init_type: str | None = field(init=False, default=None)
    _prop_type: tuple[str | None, str | None] | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.gobject_name = f"{self.gi_info.get_name()}"
        self.name = self.stub.fix_argument_name(self.gobject_name)

    @property
    def readable(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.READABLE)

    @property
    def writable(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.WRITABLE)

    @property
    def construct(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.CONSTRUCT)

    @property
    def construct_only(self) -> bool:
        return bool(self.gi_info.get_flags() & GObject.ParamFlags.CONSTRUCT_ONLY)

    @property
    def type_info(self) -> GI.TypeInfo:
        if self._type_info is None:
            self._type_info = self.gi_info.get_type_info()

        return self._type_info

    @property
    def nullability(self) -> tuple[bool, bool]:
        if self._nullability is not None:
            return self._nullability

        getter = self.gir_info.get_getter()
        setter = self.gir_info.get_setter()

        getter_nullable = bool(getter and getter.may_return_null())
        setter_nullable = bool(setter and setter.get_arg(0).may_be_null())

        is_ref = is_ref_type(self.type_info)

        if getter is not None:
            read_nullable = getter_nullable
        elif setter is not None:
            read_nullable = setter_nullable or is_ref
        else:
            read_nullable = is_ref

        if setter is not None:
            write_nullable = setter_nullable
        elif getter is not None:
            write_nullable = getter_nullable or is_ref
        else:
            write_nullable = is_ref

        self._nullability = (read_nullable, write_nullable)

        return self._nullability

    @property
    def prop_type(self) -> tuple[str | None, str | None]:
        if self._prop_type is not None:
            return self._prop_type

        read_nullable, write_nullable = self.nullability

        self._prop_type = (
            self.stub.type_info_to_python(
                self.type_info,
                nullable=read_nullable,
                out=True,
            )
            if self.readable
            else None,
            self.stub.type_info_to_python(
                self.type_info,
                nullable=write_nullable,
            )
            if self.writable and not self.construct_only
            else None,
        )

        return self._prop_type

    @property
    def init_type(self) -> str:
        if self._init_type is not None:
            return self._init_type

        write_nullable = self.nullability[1]

        py_type = self.stub.type_info_to_python(
            self.type_info,
            nullable=write_nullable,
        )

        self._init_type = py_type

        return py_type
