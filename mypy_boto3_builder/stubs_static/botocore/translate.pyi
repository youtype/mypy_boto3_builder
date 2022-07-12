from typing import Any, Optional

from botocore.utils import merge_dicts as merge_dicts

def build_retry_config(
    endpoint_prefix: str,
    retry_model: Any,
    definitions: Any,
    client_retry_config: Optional[Any] = ...,
) -> Any: ...
def resolve_references(config: Any, definitions: Any) -> None: ...
