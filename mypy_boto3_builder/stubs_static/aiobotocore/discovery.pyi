from typing import Any

from botocore.discovery import EndpointDiscoveryHandler, EndpointDiscoveryManager
from requests.models import Request

class AioEndpointDiscoveryManager(EndpointDiscoveryManager):
    async def describe_endpoint(self, **kwargs: Any) -> Any: ...

class AioEndpointDiscoveryHandler(EndpointDiscoveryHandler):
    async def discover_endpoint(
        self, request: Request, operation_name: str, **kwargs: Any
    ) -> None: ...
