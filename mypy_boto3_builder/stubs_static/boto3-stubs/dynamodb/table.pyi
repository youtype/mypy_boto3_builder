import logging
from types import TracebackType
from typing import Any, Dict, List, Optional, Type, TypeVar

from botocore.client import BaseClient

logger: logging.Logger

def register_table_methods(base_classes: List[Any], **kwargs: Any) -> None: ...

class TableResource:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def batch_writer(self, overwrite_by_pkeys: Optional[List[str]] = ...) -> "BatchWriter": ...

_R = TypeVar("_R")

class BatchWriter:
    def __init__(
        self,
        table_name: str,
        client: BaseClient,
        flush_amount: int = ...,
        overwrite_by_pkeys: Optional[List[str]] = ...,
    ) -> None: ...
    def put_item(self, Item: Dict[str, Any]) -> None: ...
    def delete_item(self, Key: Dict[str, Any]) -> None: ...
    def __enter__(self: _R) -> _R: ...
    def __exit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_value: Optional[Exception],
        tb: Optional[TracebackType],
    ) -> None: ...
