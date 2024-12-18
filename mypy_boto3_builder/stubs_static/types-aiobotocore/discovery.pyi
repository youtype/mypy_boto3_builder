"""
Type annotations for aiobotocore.discovery module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from botocore.discovery import EndpointDiscoveryHandler, EndpointDiscoveryManager
from requests.models import Request

class AioEndpointDiscoveryManager(EndpointDiscoveryManager):
    async def describe_endpoint(self, **kwargs: Any) -> Any: ...

class AioEndpointDiscoveryHandler(EndpointDiscoveryHandler):
    async def discover_endpoint(  # type: ignore[override]
        self, request: Request, operation_name: str, **kwargs: Any
    ) -> None: ...
