from typing import Any, Optional

from botocore.exceptions import NoRegionError as NoRegionError

DEFAULT_URI_TEMPLATE: str
DEFAULT_SERVICE_DATA: Any

class BaseEndpointResolver:
    def construct_endpoint(self, service_name: Any, region_name: Optional[str] = ...) -> None: ...
    def get_available_partitions(self) -> None: ...
    def get_available_endpoints(
        self,
        service_name: Any,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> None: ...

class EndpointResolver(BaseEndpointResolver):
    def __init__(self, endpoint_data: Any) -> None: ...
    def get_available_partitions(self) -> Any: ...
    def get_available_endpoints(
        self,
        service_name: Any,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> Any: ...
    def construct_endpoint(
        self,
        service_name: Any,
        region_name: Optional[str] = ...,
        partition_name: Optional[Any] = ...,
    ) -> Any: ...
