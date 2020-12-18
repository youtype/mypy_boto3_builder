import logging
from typing import Any, Dict, Type

from boto3.resources.base import ServiceResource
from boto3.utils import ServiceContext
from botocore.hooks import HierarchicalEmitter

logger: logging.Logger

class ResourceFactory:
    def __init__(self, emitter: HierarchicalEmitter) -> None: ...
    def load_from_definition(
        self,
        resource_name: str,
        single_resource_json_definition: Dict[str, Any],
        service_context: ServiceContext,
    ) -> Type[ServiceResource]: ...
