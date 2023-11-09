from typing import Any, List, Optional, Union

from boto3.exceptions import ResourceNotExistsError as ResourceNotExistsError
from boto3.exceptions import UnknownAPIVersionError as UnknownAPIVersionError
from boto3.resources.factory import ResourceFactory
from botocore.config import Config
from botocore.credentials import Credentials
from botocore.exceptions import DataNotFoundError as DataNotFoundError
from botocore.exceptions import UnknownServiceError as UnknownServiceError
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
        self.resource_factory: ResourceFactory
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
    def get_credentials(self) -> Optional[Credentials]: ...
    def get_partition_for_region(self, region_name: str) -> str: ...
    def _register_default_handlers(self) -> None: ...
    def client(
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
        config: Optional[Config] = ...,
    ) -> Any: ...
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
        config: Optional[Config] = ...,
    ) -> Any: ...
