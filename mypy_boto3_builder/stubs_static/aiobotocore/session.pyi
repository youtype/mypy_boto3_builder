from typing import Any, List, Optional, Union

from aiobotocore.client import AioBaseClient as AioBaseClient
from aiobotocore.client import AioClientCreator as AioClientCreator
from aiobotocore.credentials import AioCredentials as AioCredentials
from aiobotocore.credentials import create_credential_resolver as create_credential_resolver
from aiobotocore.hooks import AioHierarchicalEmitter as AioHierarchicalEmitter
from aiobotocore.parsers import AioResponseParserFactory as AioResponseParserFactory
from botocore.client import Config
from botocore.model import ServiceModel
from botocore.session import EVENT_ALIASES as EVENT_ALIASES
from botocore.session import Session

class ClientCreatorContext:
    def __init__(self, coro: Any) -> None: ...
    async def __aenter__(self) -> AioBaseClient: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class AioSession(Session):
    def __init__(
        self,
        session_vars: Optional[Any] = ...,
        event_hooks: Optional[Any] = ...,
        include_builtin_handlers: bool = ...,
        profile: Optional[Any] = ...,
    ) -> None: ...
    def register(
        self,
        event_name: str,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def create_client(  # type: ignore [override]
        self,
        service_name: str,
        region_name: Optional[str] = ...,
        use_ssl: Optional[bool] = ...,
        endpoint_url: Optional[str] = ...,
        verify: Union[str, bool, None] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        api_version: Optional[str] = ...,
        config: Optional[Config] = ...,
    ) -> AioBaseClient: ...
    async def get_credentials(self) -> AioCredentials: ...  # type: ignore [override]
    def set_credentials(
        self, access_key: str, secret_key: str, token: Optional[Any] = ...
    ) -> None: ...
    async def get_service_model(  # type: ignore [override]
        self, service_name: str, api_version: Optional[Any] = ...
    ) -> ServiceModel: ...
    async def get_service_data(
        self, service_name: str, api_version: Optional[Any] = ...
    ) -> Any: ...
    async def get_available_regions(  # type: ignore [override]
        self, service_name: str, partition_name: str = ..., allow_non_regional: bool = ...
    ) -> List[str]: ...

def get_session(env_vars: Optional[Any] = ...) -> AioSession: ...
