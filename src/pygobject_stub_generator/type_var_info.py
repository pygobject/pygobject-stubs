from __future__ import annotations

from typing import cast
from typing import TYPE_CHECKING

import ast
from dataclasses import dataclass
from dataclasses import field

if TYPE_CHECKING:
    from typing_extensions import Self

    from .stub import Stub


@dataclass(slots=True, frozen=True)
class _BaseTypeVarInfo:
    name: str
    default: str | None = None


@dataclass(slots=True, frozen=True)
class TypeVarInfo(_BaseTypeVarInfo):
    constraints: tuple[str, ...] | None = None
    bound: str | None = None
    contravariant: bool = field(kw_only=True, default=False)
    covariant: bool = field(kw_only=True, default=False)
    infer_variance: bool = field(kw_only=True, default=False)

    def build(self, stub: Stub, /) -> str:
        args = [f'"{self.name}"']

        if self.constraints:
            args.extend(self.constraints)

        if self.covariant and not self.contravariant:
            args.append("covariant=True")

        if self.contravariant and not self.covariant:
            args.append("contravariant=True")

        if self.infer_variance:
            args.append("infer_variance=True")

        if self.bound is not None:
            args.append(f"bound={self.bound}")

        if self.default is not None:
            args.append(f"default={self.default}")

        return (
            f"{self.name} = {stub.get_import('typing', 'TypeVar')}({', '.join(args)})"
        )

    @classmethod
    def from_call(cls, node: ast.Call, /) -> Self:
        name, *args = node.args
        kwargs = {kw.arg: ast.unparse(kw.value) for kw in node.keywords}
        return cls(
            name=cast("str", cast("ast.Constant", name).value),
            default=kwargs.get("default"),
            constraints=tuple(ast.unparse(arg) for arg in args) if args else None,
            bound=kwargs.get("bound"),
            contravariant=kwargs.get("contravariant", "False") == "True",
            covariant=kwargs.get("covariant", "False") == "True",
            infer_variance=kwargs.get("infer_variance", "False") == "True",
        )


@dataclass(slots=True, frozen=True)
class TypeVarTupleInfo(_BaseTypeVarInfo):
    def build(self, stub: Stub, /) -> str:
        args = [f'"{self.name}"']

        if self.default is not None:
            args.append(f"default={self.default}")

        return f"{self.name} = {stub.get_import('typing', 'TypeVarTuple')}({', '.join(args)})"

    @classmethod
    def from_call(cls, node: ast.Call, /) -> Self:
        name, *_ = node.args
        kwargs = {kw.arg: ast.unparse(kw.value) for kw in node.keywords}
        return cls(
            name=cast("str", cast("ast.Constant", name).value),
            default=kwargs.get("default"),
        )
