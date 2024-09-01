from typing import Any, Dict, List, Union

from boto3.resources.base import ServiceResource
from boto3.resources.response import RawHandler, ResourceHandler

class AIOResourceHandler(ResourceHandler):
    async def __call__(  # type: ignore [override]
        self, parent: ServiceResource, params: Dict[str, Any], response: Dict[str, Any]
    ) -> Union[ServiceResource, List[ServiceResource]]: ...

class AIORawHandler(RawHandler):
    async def __call__(  # type: ignore [override]
        self, parent: ServiceResource, params: Dict[str, Any], response: Dict[str, Any]
    ) -> Dict[str, Any]: ...
