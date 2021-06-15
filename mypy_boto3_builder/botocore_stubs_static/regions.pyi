from typing import Any, Dict, List, Mapping, Optional

from botocore.exceptions import NoRegionError as NoRegionError

DEFAULT_URI_TEMPLATE: str
DEFAULT_SERVICE_DATA: Dict[str, Dict[str, Any]]

class BaseEndpointResolver:
    def construct_endpoint(self, service_name: str, region_name: Optional[str] = ...) -> None: ...
    def get_available_partitions(self) -> List[str]: ...
    def get_available_endpoints(
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> List[str]: ...

class EndpointResolver(BaseEndpointResolver):
    def __init__(self, endpoint_data: Mapping[str, Any]) -> None: ...
    def get_available_partitions(self) -> List[str]: ...
    def get_available_endpoints(
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> List[str]: ...
    def construct_endpoint(  # type: ignore
        self,
        service_name: str,
        region_name: Optional[str] = ...,
        partition_name: Optional[str] = ...,
    ) -> Optional[Dict[str, Any]]: ...
