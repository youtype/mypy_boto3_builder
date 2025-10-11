"""
Type annotations for aiobotocore.utils module.

Copyright 2025 Vlad Emelianov
"""

import contextlib
import logging
from collections.abc import AsyncIterator, Callable, Coroutine, Mapping
from typing import Any

from aiobotocore.client import AioBaseClient
from aiobotocore.credentials import AioCredentials
from botocore.model import OperationModel
from botocore.session import Session
from botocore.utils import DEFAULT_METADATA_SERVICE_TIMEOUT as DEFAULT_METADATA_SERVICE_TIMEOUT
from botocore.utils import METADATA_BASE_URL as METADATA_BASE_URL
from botocore.utils import RETRYABLE_HTTP_ERRORS as RETRYABLE_HTTP_ERRORS
from botocore.utils import (
    ContainerMetadataFetcher,
    IdentityCache,
    IMDSFetcher,
    IMDSRegionProvider,
    InstanceMetadataFetcher,
    InstanceMetadataRegionFetcher,
    S3ExpressIdentityCache,
    S3ExpressIdentityResolver,
    S3RegionRedirector,
    S3RegionRedirectorv2,
)
from requests.models import Response

logger: logging.Logger = ...

class AioIMDSFetcher(IMDSFetcher):
    def __init__(
        self,
        timeout: int = ...,
        num_attempts: int = ...,
        base_url: str = ...,
        env: str | None = ...,
        user_agent: str | None = ...,
        config: Any | None = ...,
        session: Session | None = ...,
    ) -> None: ...

class AioInstanceMetadataFetcher(AioIMDSFetcher, InstanceMetadataFetcher):
    async def retrieve_iam_role_credentials(self) -> dict[str, Any]: ...  # type: ignore[override]

class AioIMDSRegionProvider(IMDSRegionProvider):
    async def provide(self) -> str: ...

class AioInstanceMetadataRegionFetcher(AioIMDSFetcher, InstanceMetadataRegionFetcher):
    async def retrieve_region(self) -> str | None: ...  # type: ignore[override]

class AioIdentityCache(IdentityCache):
    async def get_credentials(self, **kwargs: Any) -> AioCredentials: ...  # type: ignore[override]

class AioS3ExpressIdentityCache(AioIdentityCache, S3ExpressIdentityCache):
    async def get_credentials(self, bucket: str) -> AioCredentials: ...  # type: ignore[override]

class AioS3ExpressIdentityResolver(S3ExpressIdentityResolver): ...

class AioS3RegionRedirectorv2(S3RegionRedirectorv2):
    async def redirect_from_error(
        self,
        request_dict: Mapping[str, Any],
        response: Response,
        operation: OperationModel,
        **kwargs: Any,
    ) -> None: ...
    async def get_bucket_region(self, bucket: Any, response: Response) -> str: ...

class AioS3RegionRedirector(S3RegionRedirector):
    async def redirect_from_error(
        self,
        request_dict: Mapping[str, Any],
        response: Response,
        operation: OperationModel,
        **kwargs: Any,
    ) -> int | None: ...
    async def get_bucket_region(self, bucket: str, response: Response) -> str: ...

class AioContainerMetadataFetcher(ContainerMetadataFetcher):
    def __init__(
        self,
        session: Session | None = ...,
        sleep: Callable[[float], Coroutine[Any, Any, None]] = ...,
    ) -> None: ...
    async def retrieve_full_uri(
        self, full_url: str, headers: Mapping[str, Any] | None = ...
    ) -> str: ...
    async def retrieve_uri(self, relative_uri: str) -> dict[str, Any]: ...

@contextlib.asynccontextmanager
def create_nested_client(
    session: Session, service_name: str, **kwargs: Any
) -> AsyncIterator[AioBaseClient]: ...
