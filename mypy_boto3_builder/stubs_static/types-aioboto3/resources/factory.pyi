"""
Type annotations for aioboto3.resources.factory module.

Copyright 2024 Vlad Emelianov
"""

import logging
from typing import Any

from aioboto3.resources.base import AIOBoto3ServiceResource
from boto3.resources.factory import ResourceFactory
from boto3.utils import ServiceContext
from botocore.hooks import BaseEventHooks

logger: logging.Logger

class AIOBoto3ResourceFactory(ResourceFactory):
    def __init__(self, emitter: BaseEventHooks) -> None: ...
    async def load_from_definition(  # type: ignore[override]
        self,
        resource_name: str,
        single_resource_json_definition: Any,
        service_context: ServiceContext,
    ) -> AIOBoto3ServiceResource: ...
