from typing import Any
from typing import Final

from inspect import Signature

from ._gi import CallableInfo
from ._gi import TypeInfo

__all__ = ["generate_signature"]
tag_pytype: Final[dict[int, type[Any]]]
list_tag_types: Final[set[int]]

def get_pytype(gi_type: TypeInfo) -> object: ...
def generate_signature(info: CallableInfo) -> Signature: ...
