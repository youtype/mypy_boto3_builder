import collections.abc as collections_abc
from os import PathLike
from typing import Type

SOCKET_ERROR: Type[ConnectionError]

def rename_file(current_filename: PathLike, new_filename: PathLike) -> None: ...
