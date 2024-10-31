from types import TracebackType
from typing import Any, List, Optional, Type, Union

from aioboto3.resources.base import AIOBoto3ServiceResource
from aioboto3.resources.factory import AIOBoto3ResourceFactory
from aiobotocore.client import AioBaseClient
from aiobotocore.config import AioConfig
from aiobotocore.credentials import AioCredentials
from botocore.hooks import BaseEventHooks
from botocore.loaders import Loader
from botocore.session import Session as BotocoreSession

class Session:
    def __init__(
        self,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        region_name: Optional[str] = ...,
        botocore_session: Optional[BotocoreSession] = ...,
        profile_name: Optional[str] = ...,
    ) -> None:
        self._session: BotocoreSession
        self.resource_factory: AIOBoto3ResourceFactory
        self._loader: Loader

    def __repr__(self) -> str: ...
    @property
    def profile_name(self) -> str: ...
    @property
    def region_name(self) -> str: ...
    @property
    def events(self) -> BaseEventHooks: ...
    @property
    def available_profiles(self) -> List[str]: ...
    def _setup_loader(self) -> None: ...
    def get_available_services(self) -> List[str]: ...
    def get_available_resources(self) -> List[str]: ...
    def get_available_partitions(self) -> List[str]: ...
    def get_available_regions(
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> List[str]: ...
    def get_credentials(self) -> Optional[AioCredentials]: ...
    def _register_default_handlers(self) -> None: ...
    def client(  # type: ignore [override]
        self,
        service_name: str,
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: Optional[bool] = ...,
        verify: Union[str, bool, None] = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[AioConfig] = ...,
    ) -> AioBaseClient: ...
    def resource(
        self,
        service_name: str,
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: Optional[bool] = ...,
        verify: Union[bool, str, None] = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[AioConfig] = ...,
    ) -> AIOBoto3ServiceResource: ...

class ResourceCreatorContext:
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
    async def __aenter__(self) -> AIOBoto3ServiceResource: ...
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None: ...
