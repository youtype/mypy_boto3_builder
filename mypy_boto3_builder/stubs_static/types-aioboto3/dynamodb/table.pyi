"""
Type annotations for aioboto3.dynamodb.table module.

Copyright 2024 Vlad Emelianov
"""

import logging
from types import TracebackType
from typing import Any, TypeVar

from boto3.dynamodb.table import TableResource
from botocore.client import BaseClient

logger: logging.Logger

_R = TypeVar("_R")

def register_table_methods(base_classes: list[Any], **kwargs: Any) -> None: ...

class CustomTableResource(TableResource):
    def batch_writer(  # type: ignore[override]
        self,
        overwrite_by_pkeys: list[str] | None = ...,
        flush_amount: int = ...,
        on_exit_loop_sleep: int = ...,
    ) -> BatchWriter: ...

class BatchWriter:
    def __init__(
        self,
        table_name: str,
        client: BaseClient,
        flush_amount: int = ...,
        overwrite_by_pkeys: list[str] | None = ...,
        on_exit_loop_sleep: int = ...,
    ) -> None: ...
    async def put_item(self, Item: dict[str, Any]) -> None: ...
    async def delete_item(self, Key: dict[str, Any]) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
