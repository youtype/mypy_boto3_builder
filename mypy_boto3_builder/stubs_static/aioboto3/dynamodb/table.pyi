import asyncio
import logging
from typing import Any, Dict, List, Optional, Type, TypeVar

from boto3.dynamodb.table import TableResource
from botocore.client import BaseClient

logger: logging.Logger

_R = TypeVar("_R")

def register_table_methods(base_classes: List[Any], **kwargs: Any) -> None: ...

class CustomTableResource(TableResource):
    # FIXME: Signature of "batch_writer" incompatible with supertype "TableResource"
    def batch_writer(  # type: ignore [override]
        self,
        overwrite_by_pkeys: Optional[List[str]] = ...,
        flush_amount: int = ...,
        on_exit_loop_sleep: int = ...,
    ) -> "BatchWriter": ...

class BatchWriter:
    def __init__(
        self,
        table_name: str,
        client: BaseClient,
        flush_amount: int = ...,
        overwrite_by_pkeys: Optional[List[str]] = ...,
        on_exit_loop_sleep: int = ...,
    ) -> None: ...
    async def put_item(self, Item: Dict[str, Any]) -> None: ...
    async def delete_item(self, Key: Dict[str, Any]) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        # tb: TracebackType,
        tb: Any,
    ) -> None: ...
