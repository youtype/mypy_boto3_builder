from typing import Any, Dict, Optional

from botocore.utils import (
    ContainerMetadataFetcher,
    IMDSFetcher,
    InstanceMetadataFetcher,
    S3RegionRedirector,
)
from requests.models import Response

logger: Any
RETRYABLE_HTTP_ERRORS: Any

class AioIMDSFetcher(IMDSFetcher):
    class Response:
        status_code: Any
        url: Any
        text: Any
        content: Any
        def __init__(self, status_code: int, text: str, url: str) -> None: ...

    def __init__(self, *args: Any, session: Optional[Any] = ..., **kwargs: Any) -> None: ...

class AioInstanceMetadataFetcher(AioIMDSFetcher, InstanceMetadataFetcher):
    async def retrieve_iam_role_credentials(self) -> Dict[str, Any]: ...

class AioS3RegionRedirector(S3RegionRedirector):
    async def redirect_from_error(
        self, request_dict: Dict[str, Any], response: Response, operation: Any, **kwargs: Any
    ) -> Optional[int]: ...
    async def get_bucket_region(self, bucket: str, response: Response) -> str: ...

class AioContainerMetadataFetcher(ContainerMetadataFetcher):
    def __init__(self, session: Optional[Any] = ..., sleep: Any = ...) -> None: ...
    async def retrieve_full_uri(self, full_url: str, headers: Optional[Any] = ...) -> str: ...
    async def retrieve_uri(self, relative_uri: str) -> Any: ...
