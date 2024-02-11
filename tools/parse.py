from typing import Optional

import ast
import re

ParseResult = dict[str, str]

OVERRIDE_PATTERN = r"^.*#\s*override.*$"
CLASS_PATTERN = r"^\s*class\s(?P<symbol>\w*)\s*(\(|:)"
CONSTANT_INDEX = 2
SYMBOLS_PATTERNS = [
    r"^\s*def\s+(?P<symbol>\w*)\s*\(",  # Functions
    CLASS_PATTERN,
    r"^\s*(?P<symbol>\w*)\s*(:|=)[^,)]*$",  # Constants
]
DOCUMENTATION_PATTERN = r'^\s*"""\s*$'
INDENTATION_SPACES = 4

OverridableSymbols = ast.ClassDef | ast.FunctionDef | ast.AnnAssign | ast.Assign


class ParseError(Exception):
    pass


def _search_overridden_symbols(input: str) -> list[str]:
    symbols: list[str] = []
    parents: list[str] = []

    last_class: Optional[str] = None
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
    result: ParseResult,
) -> None:
    parents = parents[:]
    if isinstance(node, ast.FunctionDef | ast.ClassDef):
        name = node.name
        parents.append(name)
        full_name = ".".join(parents)
        if full_name in overridden_symbols:
            result[full_name] = ast.unparse(node)
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
    result: ParseResult = {}
    parents: list[str] = []
    body = root.body

    for child in body:
        if not isinstance(child, OverridableSymbols):
            print(f"Skipped root.{child}")
            continue
        _generate_result_node(parents, child, overridden_symbols, result)

    return result


def parse(input: str) -> ParseResult:
    overridden_symbols = _search_overridden_symbols(input)
    root = ast.parse(input)
    return _generate_result(root, overridden_symbols)
