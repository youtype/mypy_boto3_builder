import collections.abc as collections_abc
from typing import Type

SOCKET_ERROR: Type[ConnectionError]

def rename_file(current_filename: str, new_filename: str) -> None: ...
