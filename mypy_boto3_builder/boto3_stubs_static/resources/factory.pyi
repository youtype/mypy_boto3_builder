# pylint: disable=unused-argument,multiple-statements,super-init-not-called,no-self-use
import logging
from typing import Dict, Type

from botocore.hooks import HierarchicalEmitter

from boto3.resources.base import ServiceResource
from boto3.utils import ServiceContext

logger: logging.Logger

class ResourceFactory:
    def __init__(self, emitter: HierarchicalEmitter) -> None: ...
    def load_from_definition(
        self,
        resource_name: str,
        single_resource_json_definition: Dict,
        service_context: ServiceContext,
    ) -> Type[ServiceResource]: ...
