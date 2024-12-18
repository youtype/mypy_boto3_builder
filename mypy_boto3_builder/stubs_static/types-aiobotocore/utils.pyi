"""
Type annotations for aiobotocore.utils module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, Mapping

from aiobotocore.credentials import AioCredentials
from botocore.utils import DEFAULT_METADATA_SERVICE_TIMEOUT as DEFAULT_METADATA_SERVICE_TIMEOUT
from botocore.utils import METADATA_BASE_URL as METADATA_BASE_URL
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

logger: Any
RETRYABLE_HTTP_ERRORS: Any

class AioIMDSFetcher(IMDSFetcher):
    def __init__(
        self,
        timeout: int = ...,
        num_attempts: int = ...,
        base_url: str = ...,
        env: str | None = ...,
        user_agent: str | None = ...,
        config: Any | None = ...,
        session: Any | None = ...,
    ) -> None: ...

class AioInstanceMetadataFetcher(AioIMDSFetcher, InstanceMetadataFetcher):
    async def retrieve_iam_role_credentials(self) -> dict[str, Any]: ...

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
        operation: Any,
        **kwargs: Any,
    ) -> None: ...
    async def get_bucket_region(self, bucket: Any, response: Response) -> Any: ...

class AioS3RegionRedirector(S3RegionRedirector):
    async def redirect_from_error(
        self, request_dict: Mapping[str, Any], response: Response, operation: Any, **kwargs: Any
    ) -> int | None: ...
    async def get_bucket_region(self, bucket: str, response: Response) -> str: ...

class AioContainerMetadataFetcher(ContainerMetadataFetcher):
    def __init__(self, session: Any | None = ..., sleep: Any = ...) -> None: ...
    async def retrieve_full_uri(self, full_url: str, headers: Any | None = ...) -> str: ...
    async def retrieve_uri(self, relative_uri: str) -> Any: ...
