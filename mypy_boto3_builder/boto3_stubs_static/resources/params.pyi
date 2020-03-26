# pylint: disable=unused-argument,multiple-statements
from typing import Pattern, Optional, Dict, Any

from boto3.resources.base import ServiceResource
from boto3.resources.model import Request

INDEX_RE: Pattern[str]

def get_data_member(parent: ServiceResource, path: str) -> Optional[Dict]: ...
def create_request_parameters(
    parent: ServiceResource,
    request_model: Request,
    params: Optional[Dict[str, Any]] = ...,
    index: Optional[int] = None,
) -> Dict[str, Any]: ...
def build_param_structure(
    params: Dict[str, Any], target: str, value: Any, index: Optional[int] = ...
) -> None: ...
