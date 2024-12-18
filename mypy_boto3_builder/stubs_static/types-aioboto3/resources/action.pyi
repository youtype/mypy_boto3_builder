"""
Type annotations for aioboto3.resources.action module.

Copyright 2024 Vlad Emelianov
"""

import logging
from typing import Any

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
        factory: ResourceFactory | None = ...,
        service_context: ServiceContext | None = ...,
    ) -> None: ...
    async def __call__(  # type: ignore[override]
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> ServiceResource | list[ServiceResource] | dict[str, Any]: ...

class AioBatchAction(ServiceAction):
    async def __call__(  # type: ignore[override]
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> list[dict[str, Any]]: ...

class AIOWaiterAction(WaiterAction):
    async def __call__(  # type: ignore[override]
        self, parent: ServiceResource, *args: Any, **kwargs: Any
    ) -> None: ...
