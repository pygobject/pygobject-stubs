import typing

T = typing.TypeVar("T")

_lock = ...  # FIXME Constant
_namespace: str = "GLibWin32"
_version: str = "2.0"

def check_windows_version(
    major: int, minor: int, spver: int, os_type: OSType
) -> bool: ...
def error_message(error: int) -> str: ...
def ftruncate(f: int, size: int) -> int: ...
def get_package_installation_directory(package: str, dll_name: str) -> str: ...
def get_package_installation_directory_of_module(hmodule: None) -> str: ...
def get_package_installation_subdirectory(
    package: str, dll_name: str, subdir: str
) -> str: ...
def get_windows_version() -> int: ...
def getlocale() -> str: ...
def locale_filename_from_utf8(utf8filename: str) -> str: ...

class OSType:
    ANY: OSType = 0
    SERVER: OSType = 2
    WORKSTATION: OSType = 1
    denominator = ...  # FIXME Constant
    imag = ...  # FIXME Constant
    numerator = ...  # FIXME Constant
    real = ...  # FIXME Constant

    def as_integer_ratio(self, /): ...  # FIXME Function
    def bit_count(self, /): ...  # FIXME Function
    def bit_length(self, /): ...  # FIXME Function
    def conjugate(self, *args, **kwargs): ...  # FIXME Function
    def from_bytes(bytes, byteorder="big", *, signed=False): ...  # FIXME Function
    def is_integer(self, /): ...  # FIXME Function
    def to_bytes(
        self, /, length=1, byteorder="big", *, signed=False
    ): ...  # FIXME Function
