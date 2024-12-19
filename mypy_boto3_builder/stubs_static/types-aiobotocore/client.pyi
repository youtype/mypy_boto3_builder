"""
Type annotations for aiobotocore.client module.

Copyright 2024 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, TypeVar

from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter
from botocore.client import BaseClient, ClientCreator
from botocore.config import Config
from botocore.history import HistoryRecorder

_R = TypeVar("_R")

history_recorder: HistoryRecorder

class AioClientCreator(ClientCreator):
    async def create_client(  # type: ignore[override]
        self,
        service_name: str,
        region_name: str,
        is_secure: bool = ...,
        endpoint_url: str | None = ...,
        verify: str | bool | None = ...,
        credentials: Any | None = ...,
        scoped_config: Any | None = ...,
        api_version: str | None = ...,
        client_config: Config | None = ...,
        auth_token: str | None = ...,
    ) -> AioBaseClient: ...

class AioBaseClient(BaseClient):
    def get_paginator(self, operation_name: str) -> AioPaginator[Any]: ...
    def get_waiter(self, waiter_name: str) -> AIOWaiter: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    async def close(self) -> None: ...  # type: ignore[override]
