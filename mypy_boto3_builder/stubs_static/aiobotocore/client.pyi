from typing import Any, Optional, TypeVar, Union

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
    ) -> AioBaseClient: ...

class AioBaseClient(BaseClient):
    def get_paginator(self, operation_name: str) -> AioPaginator: ...
    def get_waiter(self, waiter_name: str) -> AIOWaiter: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any: ...
    async def close(self) -> None: ...  # type: ignore [override]
