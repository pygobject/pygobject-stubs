from __future__ import annotations

from typing import TYPE_CHECKING

from dataclasses import dataclass
from dataclasses import field

from gi.repository import GObject

from .utils import make_nullable

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

    _init_type: str | None = field(init=False, default=None)
    _prop_type: str | None = field(init=False, default=None)

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
    def prop_type(self) -> str:
        if self._prop_type is not None:
            return self._prop_type

        py_type = self.stub.type_info_to_python(self.gi_info.get_type_info(), out=True)
        getter = self.gir_info.get_getter()
        setter = self.gir_info.get_setter()

        if (getter and getter.may_return_null()) or (
            # If it is wratable only prop, check if setter can accept NULL
            setter and setter.get_arg(0).may_be_null()
        ):
            py_type = make_nullable(py_type)

        self._prop_type = py_type

        return py_type

    @property
    def init_type(self) -> str:
        if self._init_type is not None:
            return self._init_type

        setter = self.gir_info.get_setter()
        py_type = self.stub.type_info_to_python(
            self.gi_info.get_type_info(),
            nullable=bool(setter and setter.get_arg(0).may_be_null()),
        )

        self._init_type = py_type

        return py_type
