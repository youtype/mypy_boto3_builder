"""
Type annotations for aiobotocore.hooks module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from botocore.hooks import HierarchicalEmitter
from requests.models import Response

class AioHierarchicalEmitter(HierarchicalEmitter):
    async def emit_until_response(self, event_name: str, **kwargs: Any) -> list[Response]: ...
