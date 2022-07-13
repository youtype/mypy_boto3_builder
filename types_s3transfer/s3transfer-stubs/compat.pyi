import os
from multiprocessing.managers import BaseManager as BaseManager
from typing import IO, Any, Callable, Type

rename_file = os.rename

def accepts_kwargs(func: Callable[..., Any]) -> bool: ...

SOCKET_ERROR: Type[ConnectionError]
MAXINT: None

def seekable(fileobj: IO[Any]) -> bool: ...
def readable(fileobj: IO[Any]) -> bool: ...
def fallocate(fileobj: IO[Any], size: int) -> None: ...
