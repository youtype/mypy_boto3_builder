"""
Type annotations for boto3.session module.

Copyright 2024 Vlad Emelianov
"""

from boto3.exceptions import ResourceNotExistsError as ResourceNotExistsError
from boto3.exceptions import UnknownAPIVersionError as UnknownAPIVersionError
from boto3.resources.base import ServiceResource
from boto3.resources.factory import ResourceFactory
from botocore.client import BaseClient
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
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        region_name: str | None = ...,
        botocore_session: BotocoreSession | None = ...,
        profile_name: str | None = ...,
    ) -> None:
        self._session: BotocoreSession
        self.resource_factory: ResourceFactory
        self._loader: Loader

    @property
    def profile_name(self) -> str: ...
    @property
    def region_name(self) -> str: ...
    @property
    def events(self) -> BaseEventHooks: ...
    @property
    def available_profiles(self) -> list[str]: ...
    def get_available_services(self) -> list[str]: ...
    def get_available_resources(self) -> list[str]: ...
    def get_available_partitions(self) -> list[str]: ...
    def get_available_regions(
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> list[str]: ...
    def get_credentials(self) -> Credentials | None: ...
    def get_partition_for_region(self, region_name: str) -> str: ...
    def client(
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
    ) -> BaseClient: ...
    def resource(
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
    ) -> ServiceResource: ...
