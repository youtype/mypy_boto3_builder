from typing import Any, Dict, Optional, Pattern

from boto3.resources.base import ServiceResource
from boto3.resources.model import Request

INDEX_RE: Pattern[str]

def get_data_member(parent: ServiceResource, path: str) -> Optional[Dict[str, Any]]: ...
def create_request_parameters(
    parent: ServiceResource,
    request_model: Request,
    params: Optional[Dict[str, Any]] = ...,
    index: Optional[int] = ...,
) -> Dict[str, Any]: ...
def build_param_structure(
    params: Dict[str, Any], target: str, value: Any, index: Optional[int] = ...
) -> None: ...
