from typing import cast
from typing import Final
from typing import Protocol
from typing import TypeAlias
from typing_extensions import Self

import ast
import re
from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class Import:
    module: str
    import_as: str | None = None

    @property
    def symbol(self) -> str:
        return self.import_as or self.module

    def __str__(self) -> str:
        suffix = "" if self.import_as is None else f" as {self.import_as}"
        return f"import {self.module}{suffix}"


_versioned_import_re: Final = re.compile(r"^_(?P<name>\w+)\d+$")


@dataclass(slots=True)
class FromImport:
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


class StubProtocol(Protocol):
    def get_import(self, module: str, name: str | None = None) -> str: ...


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

    def build(self, stub: StubProtocol, /) -> str:
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
            name=cast(str, cast(ast.Constant, name).value),
            default=kwargs.get("default"),
            constraints=tuple(ast.unparse(arg) for arg in args) if args else None,
            bound=kwargs.get("bound"),
            contravariant=kwargs.get("contravariant", "False") == "True",
            covariant=kwargs.get("covariant", "False") == "True",
            infer_variance=kwargs.get("infer_variance", "False") == "True",
        )


@dataclass(slots=True, frozen=True)
class TypeVarTupleInfo(_BaseTypeVarInfo):
    def build(self, stub: StubProtocol, /) -> str:
        args = [f'"{self.name}"']

        if self.default is not None:
            args.append(f"default={self.default}")

        return f"{self.name} = {stub.get_import('typing', 'TypeVarTuple')}({', '.join(args)})"

    @classmethod
    def from_call(cls, node: ast.Call, /) -> Self:
        name, *_ = node.args
        kwargs = {kw.arg: ast.unparse(kw.value) for kw in node.keywords}
        return cls(
            name=cast(str, cast(ast.Constant, name).value),
            default=kwargs.get("default"),
        )


Overrides: TypeAlias = dict[str, str]
Imports: TypeAlias = list[Import | FromImport]
TypeVars: TypeAlias = list[TypeVarInfo | TypeVarTupleInfo]
ParseResult: TypeAlias = tuple[Overrides, Imports, TypeVars]

OVERRIDE_PATTERN = r"^.*#\s*override.*$"
CLASS_PATTERN = r"^\s*class\s(?P<symbol>\w*)\s*(\(|:)"
CONSTANT_INDEX = 2
SYMBOLS_PATTERNS = [
    r"^\s*def\s+(?P<symbol>\w*)\s*\(",  # Functions
    CLASS_PATTERN,
    r"^\s*(?P<symbol>\w*)\s*(:|=).*[^,)\s]\s*$",  # Constants
]
DOCUMENTATION_PATTERN = r'^\s*""".*$'
INDENTATION_SPACES = 4

OverridableSymbols = ast.ClassDef | ast.FunctionDef | ast.AnnAssign | ast.Assign


class ParseError(Exception):
    pass


def _search_overridden_symbols(input: str) -> list[str]:
    symbols: list[str] = []
    parents: list[str] = []

    last_class: str | None = None
    last_indentation_level: int = 0

    is_override: bool = False

    is_doc: bool = False

    for i, line in enumerate(input.splitlines()):
        if re.match(DOCUMENTATION_PATTERN, line):
            is_doc = not is_doc

        if is_doc:
            continue

        if re.match(OVERRIDE_PATTERN, line):
            is_override = True

        for index, pattern in enumerate(SYMBOLS_PATTERNS):
            res = re.match(pattern, line)
            if res and res["symbol"]:
                symbol = res["symbol"]

                indentation_level = (
                    len(line) - len(line.lstrip(" "))
                ) / INDENTATION_SPACES
                if indentation_level != int(indentation_level):
                    raise ParseError(
                        f"Wrong indentation at line: {i}, {indentation_level} != {int(indentation_level)}"
                    )
                indentation_level = int(indentation_level)

                if indentation_level > last_indentation_level:
                    if last_class:
                        parents.append(last_class)
                        last_class = None
                    else:
                        if index != CONSTANT_INDEX:
                            raise ParseError(f"Wrong indentation at line: {i}")
                        else:
                            # Regex for constant trigger also on functions arguments
                            print(
                                f"Wrong indentation for constant at line {i}, skipping"
                            )
                            continue
                elif indentation_level < last_indentation_level:
                    while indentation_level < last_indentation_level:
                        parents.pop()
                        last_indentation_level -= 1
                last_indentation_level = indentation_level

                if is_override:
                    is_override = False
                    full_list = parents + [symbol]
                    symbols.append(".".join(full_list))

                break
            elif res:
                raise ParseError(f"Unable to parse line {i}: '{line}'")

        class_res = re.match(CLASS_PATTERN, line)
        if class_res and class_res["symbol"]:
            last_class = class_res["symbol"]
        elif class_res:
            raise ParseError(f"Unable to parse line {i}: '{line}'")

    return symbols


def _generate_result_node(
    parents: list[str],
    node: OverridableSymbols,
    overridden_symbols: list[str],
    result: Overrides,
    typevars: TypeVars | None = None,
) -> None:
    parents = parents[:]
    if isinstance(node, ast.FunctionDef | ast.ClassDef):
        name = node.name
        parents.append(name)
        full_name = ".".join(parents)
        if full_name in overridden_symbols:
            unparsed = ast.unparse(node)
            if (
                full_name in result
                and isinstance(node, ast.FunctionDef)
                and any(
                    (isinstance(deco, ast.Name) and deco.id == "overload")
                    or (isinstance(deco, ast.Attribute) and deco.attr == "overload")
                    for deco in node.decorator_list
                )
            ):
                # Function overloads share a single override block; append
                # subsequent overloads to the existing entry.
                result[full_name] = result[full_name] + "\n" + unparsed
            else:
                result[full_name] = unparsed
            return

        if isinstance(node, ast.ClassDef):
            for child in node.body:
                if (
                    isinstance(child, ast.Expr)
                    and isinstance(child.value, ast.Constant)
                    and child.value.value == Ellipsis
                ):
                    continue

                if not isinstance(child, OverridableSymbols):
                    print(
                        f"Skipping {'.'.join(parents)} {child} no overridable",
                        ast.dump(child, indent=4),
                    )
                    continue
                _generate_result_node(parents, child, overridden_symbols, result)

    if isinstance(node, ast.AnnAssign):
        if not hasattr(node.target, "id"):
            print(f"Skipping {'.'.join(parents)} {node} no id attribute")
            return
        name = node.target.id  # type: ignore
        parents.append(name)
        full_name = ".".join(parents)
        if full_name in overridden_symbols:
            result[full_name] = ast.unparse(node)
            return

    if isinstance(node, ast.Assign):
        if typevars is not None:
            if isinstance(node.value, ast.Call) and isinstance(
                node.value.func, ast.Name
            ):
                if node.value.func.id == "TypeVar":
                    typevars.append(TypeVarInfo.from_call(node.value))

                if node.value.func.id == "TypeVarTuple":
                    typevars.append(TypeVarTupleInfo.from_call(node.value))

        if not hasattr(node.targets[0], "id"):
            print(f"Skipping {'.'.join(parents)} {node} no id attribute")
            return
        name = node.targets[0].id  # type: ignore
        parents.append(name)
        full_name = ".".join(parents)
        if full_name in overridden_symbols:
            result[full_name] = ast.unparse(node)
            return


def _generate_result(root: ast.Module, overridden_symbols: list[str]) -> ParseResult:
    result: Overrides = {}
    imports: Imports = []
    typevars: list[TypeVarInfo | TypeVarTupleInfo] = []
    parents: list[str] = []
    body = root.body

    for child in body:
        if isinstance(child, ast.Import):
            imports.extend(Import(module.name, module.asname) for module in child.names)
        if isinstance(child, ast.ImportFrom):
            imports.extend(FromImport.from_ast(child, alias) for alias in child.names)
        if not isinstance(child, OverridableSymbols):
            print(f"Skipped root.{child}")
            continue
        _generate_result_node(parents, child, overridden_symbols, result, typevars)

    return result, imports, typevars


def parse(input: str) -> ParseResult:
    overridden_symbols = _search_overridden_symbols(input)
    root = ast.parse(input)
    return _generate_result(root, overridden_symbols)
