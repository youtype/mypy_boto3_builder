import logging
from typing import Any, Dict, Generic, List, Optional, TypeVar

from boto3.resources.model import ResourceModel
from botocore.client import BaseClient

logger: logging.Logger

_ResourceMeta = TypeVar("_ResourceMeta")
_Client = TypeVar("_Client", bound=BaseClient)

class ResourceMeta(Generic[_Client]):
    def __init__(
        self,
        service_name: str,
        identifiers: Optional[List[str]] = ...,
        client: Optional[_Client] = ...,
        data: Optional[Dict[str, Any]] = ...,
        resource_model: Optional[ResourceModel] = ...,
    ) -> None:
        self.service_name: str
        self.identifiers: List[str]
        self.client: _Client
        self.data: Dict[str, Any]
        self.resource_model: ResourceModel
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def copy(self: _ResourceMeta) -> _ResourceMeta: ...

class ServiceResource(Generic[_Client]):
    def __init__(self, *args: Any, client: Optional[_Client] = ..., **kwargs: Any) -> None:
        self.meta: ResourceMeta[_Client]
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
