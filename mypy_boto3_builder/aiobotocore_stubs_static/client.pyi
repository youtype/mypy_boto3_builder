from typing import Any, Optional, Union

from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter
from botocore.client import BaseClient, ClientCreator
from botocore.config import Config
from botocore.history import HistoryRecorder

history_recorder: HistoryRecorder

class AioClientCreator(ClientCreator):
    async def create_client(
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
