from types import TracebackType
from typing import Any, Optional, Type, TypeVar, Union

from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter
from botocore.client import BaseClient, ClientCreator
from botocore.config import Config
from botocore.history import HistoryRecorder

history_recorder: HistoryRecorder

_R = TypeVar("_R")

class AioClientCreator(ClientCreator):
    async def create_client(  # type: ignore [override]
        self,
        service_name: str,
        region_name: str,
        is_secure: bool = ...,
        endpoint_url: Optional[str] = ...,
        verify: Optional[Union[str, bool]] = ...,
        credentials: Optional[Any] = ...,
        scoped_config: Optional[Any] = ...,
        api_version: Optional[str] = ...,
        client_config: Optional[Config] = ...,
        auth_token: Optional[str] = ...,
    ) -> AioBaseClient: ...

class AioBaseClient(BaseClient):
    def get_paginator(self, operation_name: str) -> AioPaginator: ...
    def get_waiter(self, waiter_name: str) -> AIOWaiter: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_val: Optional[Exception],
        tb: Optional[TracebackType],
    ) -> Any: ...
    async def close(self) -> None: ...  # type: ignore [override]
