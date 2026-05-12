from __future__ import annotations

from typing import Any
from typing import cast
from typing import Generic
from typing import get_args
from typing import get_origin
from typing import Protocol
from typing import TYPE_CHECKING
from typing import TypeAlias
from typing_extensions import get_original_bases

import itertools
import textwrap
from dataclasses import dataclass
from dataclasses import field
from types import GenericAlias

import gi
import gi._gi as GI

from .property_info import PropertyInfo
from .utils import generate_full_name

gi.require_version("GIRepository", "3.0")

if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Iterable
    from collections.abc import Iterator

    from gi.repository import _GIRepository3 as GIRepository

    from .stub import Stub
else:
    from gi.repository import GIRepository

PropertyInfoDict: TypeAlias = dict[str, PropertyInfo]
_MISSING = object()


def _find_attributes(obj: type[Any]) -> list[str]:
    # Get all attributes resolved in this class, excluding inherited ones.
    # This includes overridden attributes that could have a different signature
    # in parent classes.
    obj_attrs = set(obj.__dict__.keys())

    # Add inherited GI attributes if we are a direct override of a GI class.
    if "__info__" not in obj.__dict__:
        for base in obj.__bases__:
            if "__info__" in base.__dict__:
                obj_attrs.update(base.__dict__.keys())

    return sorted(obj_attrs)


@dataclass(slots=True)
class ClassInfo:
    stub: Stub
    cls: type[Any]
    name: str
    prefix: str
    in_class: Any | None
    full_name: str = field(init=False)

    _bases: tuple[type[Any], ...] | None = field(init=False, default=None)
    _gi_info: GI.RegisteredTypeInfo | None = field(
        init=False, default=cast("Any", _MISSING)
    )
    _class_properties: PropertyInfoDict | None = field(init=False, default=None)
    _init_properties: PropertyInfoDict | None = field(init=False, default=None)
    _class_content: str | None = field(init=False, default=None)
    _fields: list[GI.FieldInfo] | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.full_name = generate_full_name(self.prefix, self.name)

    @property
    def is_interface(self) -> bool:
        return isinstance(self.gi_info, GI.InterfaceInfo)

    @property
    def is_object(self) -> bool:
        return isinstance(self.gi_info, GI.ObjectInfo)

    @property
    def bases(self) -> tuple[type[Any], ...]:
        if self._bases is not None:
            return self._bases

        self._bases, self._gi_info = self.__get_bases_and_gi_info()

        return self._bases

    @property
    def gi_info(self) -> GI.RegisteredTypeInfo | None:
        if self._gi_info is not _MISSING:
            return self._gi_info

        self._bases, self._gi_info = self.__get_bases_and_gi_info()

        return self._gi_info

    @property
    def properties(self) -> PropertyInfoDict:
        if self._class_properties is not None:
            return self._class_properties

        self._class_properties, self._init_properties = self.__get_properties()

        return self._class_properties

    @property
    def init_properties(self) -> PropertyInfoDict:
        if self._init_properties is not None:
            return self._init_properties

        self._class_properties, self._init_properties = self.__get_properties()

        return self._init_properties

    @property
    def contents(self) -> str:
        if self._class_content is not None:
            return self._class_content

        self._class_content, self._fields = self.__get_contents_and_fields()

        return self._class_content

    @property
    def fields(self) -> list[GI.FieldInfo]:
        if self._fields is not None:
            return self._fields

        self._class_content, self._fields = self.__get_contents_and_fields()

        return self._fields

    def __get_bases_and_gi_info(
        self,
    ) -> tuple[tuple[type[Any], ...], GI.RegisteredTypeInfo | None]:
        full_module_name = f"{self.cls.__module__}.{self.cls.__qualname__}"
        object_info: GI.RegisteredTypeInfo | None = self.cls.__dict__.get("__info__")
        bases = list(get_original_bases(self.cls))

        # Because we're generating types for gi.repository, we have to generate stubs
        # for override classes that come from gi.repository and inherit from
        # gi.repository classes. Effectively, we want to write the stubs as if the
        # override class and repository class are one class in the MRO. What this means
        # is that the following transformations need to happen:
        # 1. For the following:
        #    gi.repository.X.One(<One repository bases>)
        #    gi.overrides.X.One(
        #        <One prefix override bases>,
        #        gi.repository.X.One,
        #        <One suffix override bases>
        #    ) -> gi.repository.X.One(
        #        <One prefix override bases>,
        #        <One repository bases>,
        #        <One override bases>
        #    )
        # 2. gi.overrides.X.Two(float) -> gi.repository.X.Two(float)
        # 3. gi.overrides.X.Three(gi.overrides.X.Four, ...) -> gi.repository.X.Three(
        #        gi.repository.X.Four, ...
        #    )
        if full_module_name.startswith("gi.overrides.") and any(
            base.__module__.startswith("gi.repository.") for base in bases
        ):
            bases = []
            gi_repo_full_name = full_module_name.replace(
                "gi.overrides.", "gi.repository.", 1
            )

            for base in get_original_bases(self.cls):
                if f"{base.__module__}.{base.__qualname__}" == gi_repo_full_name:
                    bases.extend(get_original_bases(base))

                    if object_info is None:
                        object_info = base.__dict__.get("__info__")
                elif base is not object and base not in bases:
                    bases.append(base)

        if GI.GInterface in bases and not any(
            get_origin(base) is Protocol for base in bases
        ):
            # Most overrides use Generic instead of Protocol for interfaces
            index = next(
                (
                    i
                    for i, base in enumerate(bases)
                    if get_origin(base) is Generic and get_args(base)
                ),
                None,
            )
            if index is None:
                bases.append(Protocol)
            else:
                args = get_args(bases[index])
                bases[index] = GenericAlias(cast("Any", Protocol), args)

        return tuple(bases), object_info

    def __find_repo_property(
        self, prop_info: GI.PropertyInfo, /
    ) -> GIRepository.PropertyInfo | None:
        class_info = self.stub.repo.find_by_name(
            prop_info.get_namespace(), f"{prop_info.get_container().get_name()}"
        )
        prop_name = prop_info.get_name()

        if isinstance(
            class_info, (GIRepository.ObjectInfo, GIRepository.InterfaceInfo)
        ):
            for i in range(class_info.get_n_properties()):
                property = class_info.get_property(i)
                if property.get_name() == prop_name:
                    return property

        return None

    def __iterate_class_properties(
        self,
        gi_info: GI.ObjectInfo | GI.InterfaceInfo,
        *,
        include_interfaces: bool = False,
    ) -> Iterator[PropertyInfo]:
        interface_properties: Iterable[tuple[GI.PropertyInfo, ...]] = (
            (iface.get_properties() for iface in gi_info.get_interfaces())
            if isinstance(gi_info, GI.ObjectInfo) and include_interfaces
            else []
        )

        yield from (
            PropertyInfo(self.stub, prop, prop_info)
            for prop in itertools.chain(gi_info.get_properties(), *interface_properties)
            if (prop_info := self.__find_repo_property(prop)) is not None
        )

    def __iterate_parents(self) -> Iterator[GI.ObjectInfo]:
        if not isinstance(self.gi_info, GI.ObjectInfo):
            return

        current = self.gi_info.get_parent()
        while current is not None:
            yield current
            current = current.get_parent()

    def __iterate_parent_class_properties(self) -> Iterator[PropertyInfo]:
        for parent in self.__iterate_parents():
            yield from self.__iterate_class_properties(parent)

    def __get_properties(self) -> tuple[PropertyInfoDict, PropertyInfoDict]:
        if not isinstance(self.gi_info, (GI.ObjectInfo, GI.InterfaceInfo)):
            return {}, {}

        names: set[str] = set()
        class_props: PropertyInfoDict = {}
        init_props: PropertyInfoDict = {}

        for prop_info in self.__iterate_class_properties(
            self.gi_info, include_interfaces=True
        ):
            if (name := prop_info.name) in names:
                continue

            names.add(name)

            if prop_info.readable or (
                prop_info.writable and not prop_info.construct_only
            ):
                class_props[name] = prop_info

            if prop_info.writable or prop_info.construct or prop_info.construct_only:
                init_props[name] = prop_info

        for prop_info in self.__iterate_parent_class_properties():
            if (name := prop_info.name) in names:
                continue

            names.add(name)

            if prop_info.writable or prop_info.construct or prop_info.construct_only:
                init_props[name] = prop_info

        return class_props, init_props

    def __get_contents_and_fields(self) -> tuple[str, list[GI.FieldInfo]]:
        return self.stub.build_contents_and_fields(
            self.cls, _find_attributes(self.cls), self.cls, self.full_name
        )

    def __build_docstring(self) -> str | None:
        # extracting docs
        docs = (
            f"{(getattr(self.cls, '__doc__', '') or '').strip()}\n\n{
                getattr(self.cls, '__gdoc__', '') or ''
            }"
        ).strip()

        if docs:
            return '"""\n' + docs.strip() + '\n"""'

        return None

    def __build_props_class(self) -> str | None:
        if override := self.stub.check_override(self.full_name, "Props"):
            return override

        if (
            not isinstance(self.gi_info, (GI.ObjectInfo, GI.InterfaceInfo))
            or not self.properties
        ):
            return None

        lines: list[str] = []

        for name, prop_info in self.properties.items():
            if prop_definition := self.stub.get_property(name, prop_info.prop_type):
                lines.append(prop_definition)

        props_string = "\n".join(lines) if lines else "..."

        parents_string = ""
        if isinstance(self.gi_info, GI.ObjectInfo) and (
            parent := self.gi_info.get_parent()
        ):
            parent_name = f"{parent.get_name()}"
            parents_string = f"({
                self.stub.get_namespace_member(parent.get_namespace(), parent_name)
            }.Props)"

        return f"""@{self.stub.get_import("typing", "type_check_only")}
class Props{parents_string}:
{textwrap.indent(props_string, "    ")}"""

    def __build_props_property(self, props_class: str | None) -> str | None:
        if override := self.stub.check_override(self.full_name, "props"):
            return override

        if isinstance(self.gi_info, GI.ObjectInfo) and props_class is not None:
            return self.stub.get_property("props", ("Props", None))

        return None

    def __build_props(self) -> str | None:
        lines: list[str] = []

        if (props_class := self.__build_props_class()) is not None:
            lines.append(props_class)

        if (props_property := self.__build_props_property(props_class)) is not None:
            lines.append(props_property)

        return "\n".join(lines) if lines else None

    def __build_fields(self) -> str:
        lines: list[str] = []

        for field in self.fields:  # noqa: F402
            name = f"{field.get_name()}"

            if override := self.stub.check_override(self.full_name, name):
                lines.append(override)
            else:
                py_type = self.stub.type_info_to_python(field.get_type_info(), out=True)
                flags = field.get_flags()
                if not (flags & GI.FieldInfoFlags.IS_WRITABLE):
                    lines.append(self.stub.get_property(name, (py_type, None)))
                else:
                    lines.append(f"{name}: {py_type}")

        return "\n".join(lines)

    def __build_init(self) -> str | None:
        if override := self.stub.check_override(self.full_name, "__init__"):
            return override

        # Structs and Boxed use __new__ as constructor with a dummy __init__, but
        # overrides can introduce either __new__ or __init__. The priority below is:
        # 1. __new__ is the same as the "new" method from __info__
        # 2. __new__ exists on this class
        # 3. __init__ exists on this class
        if issubclass(self.cls, (GI.Boxed, GI.Struct)):
            if isinstance(self.cls.__new__, GI.BaseInfo) and isinstance(
                self.gi_info, (GI.StructInfo, GI.UnionInfo)
            ):
                for method_info in self.gi_info.get_methods():
                    if method_info.equal(self.cls.__new__):
                        return self.stub.build_function(
                            "__init__", method_info, self.cls
                        )

            if "__new__" in self.cls.__dict__:
                return self.stub.build_function(
                    "__init__", cast("Callable[..., Any]", self.cls.__new__), self.cls
                )

            if "__init__" in self.cls.__dict__:
                return self.stub.build_function("__init__", self.cls.__init__, self.cls)

        if not isinstance(self.gi_info, GI.ObjectInfo):
            return None

        if not self.init_properties:
            # Pango.Layout and Pango.FontDescription override __new__
            if "__new__" in self.cls.__dict__:
                return self.stub.build_function(
                    "__init__", cast("Callable[..., Any]", self.cls.__new__), self.cls
                )

            return None

        args: list[str] = []

        for name, init_prop in self.init_properties.items():
            args.append(f"{name}: {init_prop.init_type} = ...")

        return f"def __init__(self, *, {', '.join(args)}) -> None: ..."

    def build(self) -> str:
        if override := self.stub.check_override(self.prefix, self.name):
            return override

        if (
            not self.in_class
            and (alias := self.stub.get_alias(self.name, self.cls)) is not None
        ):
            # Set up a constant for classes that are aliases
            # NOTE: this should not use `Final` because doing so turns the alias into
            # a variable rather than a class
            return f"{self.name} = {alias}"

        string_parents = ""
        if self.bases:
            bases_strings = [
                self.stub.get_class_import(base)
                for base in self.bases
                if base is not object
            ]

            string_parents = f"({', '.join(bases_strings)})"

        lines = [f"class {self.name}{string_parents}:"]

        if docs := self.__build_docstring():
            lines.append(textwrap.indent(docs, "    "))

        if self.is_object and (props := self.__build_props()) is not None:
            lines.append(textwrap.indent(props, "    "))

        if class_fields := self.__build_fields():
            lines.append(textwrap.indent(class_fields, "    "))

        if class_constructor := self.__build_init():
            lines.append(textwrap.indent(class_constructor.strip(), "    "))

        lines.append(textwrap.indent(self.contents, "    "))

        class_string = "\n".join(lines).strip()

        if class_string.endswith(":"):
            class_string += " ..."

        return class_string
