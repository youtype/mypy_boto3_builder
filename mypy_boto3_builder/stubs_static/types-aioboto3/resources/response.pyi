"""
Type annotations for aioboto3.resources.response module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from boto3.resources.base import ServiceResource
from boto3.resources.response import RawHandler, ResourceHandler

class AIOResourceHandler(ResourceHandler):
    async def __call__(  # type: ignore[override]
        self, parent: ServiceResource, params: dict[str, Any], response: dict[str, Any]
    ) -> ServiceResource | list[ServiceResource]: ...

class AIORawHandler(RawHandler):
    async def __call__(  # type: ignore[override]
        self, parent: ServiceResource, params: dict[str, Any], response: dict[str, Any]
    ) -> dict[str, Any]: ...
