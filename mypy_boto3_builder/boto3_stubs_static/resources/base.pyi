import logging
from typing import Any, Dict, List, Optional

from boto3.resources.model import ResourceModel
from botocore.client import BaseClient

logger: logging.Logger

class ResourceMeta:
    def __init__(
        self,
        service_name: str,
        identifiers: Optional[List[str]] = ...,
        client: Optional[BaseClient] = ...,
        data: Optional[Dict[str, Any]] = ...,
        resource_model: Optional[ResourceModel] = ...,
    ) -> None:
        self.service_name: str
        self.identifiers: List[str]
        self.client: BaseClient
        self.data: Dict[str, Any]
        self.resource_model: ResourceModel
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def copy(self) -> "ResourceMeta": ...

class ServiceResource:
    def __init__(self, *args: Any, client: Optional[BaseClient] = ..., **kwargs: Any) -> None:
        self.meta: ResourceMeta
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
