# from types import TracebackType
import logging
from typing import Any, Dict, List, Optional, Type

from botocore.client import BaseClient

logger: logging.Logger

def register_table_methods(base_classes: List[type], **kwargs: Any) -> None: ...

class TableResource:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def batch_writer(self, overwrite_by_pkeys: Optional[List[str]] = ...) -> "BatchWriter": ...

class BatchWriter:
    def __init__(
        self,
        table_name: str,
        client: BaseClient,
        flush_amount: int = 25,
        overwrite_by_pkeys: Optional[List[str]] = ...,
    ) -> None: ...
    def put_item(self, Item: Dict[str, Any]) -> None: ...
    def delete_item(self, Key: Dict[str, Any]) -> None: ...
    def __enter__(self) -> "BatchWriter": ...
    def __exit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        # tb: TracebackType,
        tb: Any,
    ) -> None: ...
