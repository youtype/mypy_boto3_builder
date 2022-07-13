from typing import Any, Dict, List, Union

from aioboto3.resources.base import AIOBoto3ServiceResource
from boto3.resources.response import RawHandler, ResourceHandler

class AIOResourceHandler(ResourceHandler):
    async def __call__(
        self, parent: AIOBoto3ServiceResource, params: Dict[str, Any], response: Dict[str, Any]
    ) -> Union[AIOBoto3ServiceResource, List[AIOBoto3ServiceResource]]: ...

class AIORawHandler(RawHandler):
    async def __call__(
        self, parent: AIOBoto3ServiceResource, params: Dict[str, Any], response: Dict[str, Any]
    ) -> Dict[str, Any]: ...
