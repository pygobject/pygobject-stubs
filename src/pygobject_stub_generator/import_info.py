from __future__ import annotations

from typing import cast
from typing import Final
from typing import TYPE_CHECKING
from typing_extensions import Self

import re
from dataclasses import dataclass

if TYPE_CHECKING:
    import ast

_versioned_import_re: Final = re.compile(r"^_(?P<name>\w+)\d+$")


@dataclass(slots=True)
class ImportInfo:
    module: str
    import_as: str | None = None

    @property
    def symbol(self) -> str:
        return self.import_as or self.module

    def __str__(self) -> str:
        suffix = "" if self.import_as is None else f" as {self.import_as}"
        return f"import {self.module}{suffix}"


@dataclass(slots=True)
class FromImportInfo:
    module: str
    name: str
    import_as: str | None = None
    versioned_import: str | None = None

    @property
    def symbol(self) -> str:
        return self.versioned_import or self.import_as or self.name

    def __str__(self) -> str:
        suffix = "" if self.import_as is None else f" as {self.import_as}"
        return f"from {self.module} import {self.versioned_import or self.name}{suffix}"

    @classmethod
    def from_ast(cls, node: ast.ImportFrom, alias: ast.alias, /) -> Self:
        name = alias.name
        pyi_import: str | None = None

        if node.module == "gi.repository" and (
            match := _versioned_import_re.match(name)
        ):
            pyi_import = alias.name
            name = match.group("name")

        return cls(cast("str", node.module), name, alias.asname, pyi_import)
