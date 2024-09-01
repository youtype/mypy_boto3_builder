from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, Union

from boto3.resources.base import ServiceResource
from boto3.resources.factory import ResourceFactory
from boto3.resources.model import Parameter, ResponseResource
from boto3.utils import ServiceContext
from botocore.model import ServiceModel

def all_not_none(iterable: Iterable[Any]) -> bool: ...
def build_identifiers(
    identifiers: List[Parameter],
    parent: ServiceResource,
    params: Optional[Dict[str, Any]] = ...,
    raw_response: Optional[Dict[str, Any]] = ...,
) -> List[Tuple[str, Any]]: ...
def build_empty_response(
    search_path: str, operation_name: str, service_model: ServiceModel
) -> Union[Dict[str, Any], List[Any], None]: ...

class RawHandler:
    def __init__(self, search_path: str) -> None: ...
    def __call__(
        self, parent: ServiceResource, params: Dict[str, Any], response: Dict[str, Any]
    ) -> Dict[str, Any]: ...

class ResourceHandler:
    def __init__(
        self,
        search_path: str,
        factory: ResourceFactory,
        resource_model: ResponseResource,
        service_context: ServiceContext,
        operation_name: Optional[str] = ...,
    ) -> None: ...
    def __call__(
        self, parent: ServiceResource, params: Dict[str, Any], response: Dict[str, Any]
    ) -> Union[ServiceResource, List[ServiceResource]]: ...
    def handle_response_item(
        self,
        resource_cls: Type[ServiceResource],
        parent: ServiceResource,
        identifiers: Dict[str, Any],
        resource_data: Optional[Dict[str, Any]],
    ) -> ServiceResource: ...
