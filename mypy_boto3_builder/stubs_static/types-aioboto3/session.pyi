"""
Type annotations for aioboto3.session module.

Copyright 2025 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, Generic, TypeVar

from aioboto3.resources.base import AIOBoto3ServiceResource
from aioboto3.resources.factory import AIOBoto3ResourceFactory
from aiobotocore.config import AioConfig
from aiobotocore.credentials import AioCredentials
from aiobotocore.session import AioSession as AioBotocoreSession
from aiobotocore.session import ClientCreatorContext
from boto3.session import Session as Boto3Session
from botocore.loaders import Loader

class Session(Boto3Session):
    def __init__(
        self,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        region_name: str | None = ...,
        botocore_session: AioBotocoreSession | None = ...,
        profile_name: str | None = ...,
        aws_account_id: str | None = ...,
    ) -> None:
        self._session: AioBotocoreSession  # type: ignore[override]
        self.resource_factory: AIOBoto3ResourceFactory  # type: ignore[override]
        self._loader: Loader

    async def get_credentials(self) -> AioCredentials | None: ...  # type: ignore[override]
    def client(  # type: ignore[override]
        self,
        service_name: str,
        region_name: str | None = ...,
        api_version: str | None = ...,
        use_ssl: bool | None = ...,
        verify: str | bool | None = ...,
        endpoint_url: str | None = ...,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        config: AioConfig | None = ...,
        aws_account_id: str | None = ...,
    ) -> ClientCreatorContext[Any]: ...
    def resource(  # type: ignore[override]
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
        config: AioConfig | None = ...,
    ) -> ResourceCreatorContext[Any]: ...
    async def get_available_regions(  # type: ignore[override]
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> list[str]: ...

_AIOBoto3ServiceResource = TypeVar("_AIOBoto3ServiceResource", bound=AIOBoto3ServiceResource)

class ResourceCreatorContext(Generic[_AIOBoto3ServiceResource]):
    def __init__(
        self,
        session: Session,
        service_name: str,
        region_name: str,
        api_version: str,
        use_ssl: bool,
        verify: bool,
        endpoint_url: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        aws_session_token: str,
        config: AioConfig,
        resource_model: Any,
    ) -> None: ...
    async def __aenter__(self) -> _AIOBoto3ServiceResource: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
