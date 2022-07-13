import logging
from typing import Any, Dict, List, Union

from aioboto3.resources.base import ServiceResource
from aioboto3.resources.collection import ResourceCollection
from aioboto3.resources.factory import ResourceFactory
from aioboto3.resources.response import AIORawHandler, AIOResourceHandler
from boto3.resources.action import ServiceAction, WaiterAction
from boto3.resources.model import Action
from boto3.utils import ServiceContext

logger: logging.Logger

class AIOServiceAction(ServiceAction):
    def __init__(
        self,
        action_model: Action,
        factory: ResourceFactory = ...,
        service_context: ServiceContext = ...,
    ) -> None: ...
    async def __call__(
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> Union[ServiceResource, List[ServiceResource], Dict[str, Any]]: ...

class AioBatchAction(ServiceAction):
    async def __call__(
        self, parent: ResourceCollection, *args: Any, **kwargs: Any
    ) -> List[Dict[str, Any]]: ...

class AIOWaiterAction(WaiterAction):
    async def __call__(self, parent: ServiceResource, *args: Any, **kwargs: Any) -> None: ...
