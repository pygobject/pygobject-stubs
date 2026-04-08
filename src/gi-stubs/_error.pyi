from typing_extensions import Self

class GError(RuntimeError):
    message: str
    domain: str
    code: int

    def __init__(
        self,
        message: str = "unknown error",
        domain: str = "pygi-error",
        code: int = 0,
    ) -> None: ...
    def copy(self) -> Self: ...
    def matches(self, domain: str | int, code: int) -> bool: ...
    @staticmethod
    def new_literal(domain: int, message: str, code: int) -> Self: ...
