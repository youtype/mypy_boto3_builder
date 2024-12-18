"""
Type annotations for aiobotocore.session module.

Copyright 2024 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, Generic, TypeVar

from aiobotocore.client import AioBaseClient as AioBaseClient
from aiobotocore.client import AioClientCreator as AioClientCreator
from aiobotocore.credentials import AioCredentials as AioCredentials
from aiobotocore.credentials import create_credential_resolver as create_credential_resolver
from aiobotocore.hooks import AioHierarchicalEmitter as AioHierarchicalEmitter
from aiobotocore.parsers import AioResponseParserFactory as AioResponseParserFactory
from botocore.config import Config
from botocore.model import ServiceModel
from botocore.session import EVENT_ALIASES as EVENT_ALIASES
from botocore.session import Session

_AioBaseClient = TypeVar("_AioBaseClient", bound=AioBaseClient)

class ClientCreatorContext(Generic[_AioBaseClient]):
    def __init__(self, coro: Any) -> None: ...
    async def __aenter__(self) -> _AioBaseClient: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...

class AioSession(Session):
    def __init__(
        self,
        session_vars: Any | None = ...,
        event_hooks: Any | None = ...,
        include_builtin_handlers: bool = ...,
        profile: Any | None = ...,
    ) -> None: ...
    def register(
        self,
        event_name: str,
        handler: Any,
        unique_id: Any | None = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def create_client(  # type: ignore[override]
        self,
        service_name: str,
        region_name: str | None = ...,
        api_version: str | None = ...,
        use_ssl: bool | None = ...,
        verify: bool | str | None = ...,
        endpoint_url: str | None = ...,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        config: Config | None = ...,
    ) -> ClientCreatorContext[AioBaseClient]: ...
    async def get_credentials(self) -> AioCredentials | None: ...  # type: ignore[override]
    def set_credentials(
        self, access_key: str, secret_key: str, token: Any | None = ...
    ) -> None: ...
    async def get_service_model(  # type: ignore[override]
        self, service_name: str, api_version: Any | None = ...
    ) -> ServiceModel: ...
    async def get_service_data(self, service_name: str, api_version: Any | None = ...) -> Any: ...
    async def get_available_regions(  # type: ignore[override]
        self, service_name: str, partition_name: str = ..., allow_non_regional: bool = ...
    ) -> list[str]: ...

def get_session(env_vars: Any | None = ...) -> AioSession: ...
