# pylint: disable=unused-argument,multiple-statements,unused-import
import collections.abc as collections_abc
from typing import Type
from os import PathLike

SOCKET_ERROR: Type[ConnectionError]

def rename_file(current_filename: PathLike, new_filename: PathLike) -> None: ...
