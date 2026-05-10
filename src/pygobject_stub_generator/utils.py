from __future__ import annotations


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
