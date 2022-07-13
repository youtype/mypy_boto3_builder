from typing import Any, List, Optional, Union

from aioboto3.resources.base import AIOBoto3ServiceResource
from aioboto3.resources.factory import AIOBoto3ResourceFactory
from aiobotocore.config import AioConfig
from botocore.credentials import Credentials
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
    def events(self) -> List[Any]: ...
    @property
    def available_profiles(self) -> List[Any]: ...
    def _setup_loader(self) -> None: ...
    def get_available_services(self) -> List[str]: ...
    def get_available_resources(self) -> List[str]: ...
    def get_available_partitions(self) -> List[str]: ...
    def get_available_regions(
        self,
        service_name: str,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> List[str]: ...
    def get_credentials(self) -> Credentials: ...
    def _register_default_handlers(self) -> None: ...
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
