from typing import Any, List

from botocore.hooks import HierarchicalEmitter
from requests.models import Response

class AioHierarchicalEmitter(HierarchicalEmitter):
    async def emit_until_response(self, event_name: str, **kwargs: Any) -> List[Response]: ...
