import logging
from typing import Any, Dict, List, Optional, Union

from boto3.resources.action import ServiceAction, WaiterAction
from boto3.resources.base import ServiceResource
from boto3.resources.factory import ResourceFactory
from boto3.resources.model import Action
from boto3.utils import ServiceContext

logger: logging.Logger

class AIOServiceAction(ServiceAction):
    def __init__(
        self,
        action_model: Action,
        factory: Optional[ResourceFactory] = ...,
        service_context: Optional[ServiceContext] = ...,
    ) -> None: ...
    async def __call__(  # type: ignore [override]
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> Union[ServiceResource, List[ServiceResource], Dict[str, Any]]: ...

class AioBatchAction(ServiceAction):
    async def __call__(  # type: ignore [override]
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> List[Dict[str, Any]]: ...

class AIOWaiterAction(WaiterAction):
    async def __call__(  # type: ignore [override]
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> None: ...
