from typing import Any, Optional
from botocore.hooks import BaseEventHooks

def document_model_driven_resource_method(
    section: Any,
    method_name: str,
    operation_model: Any,
    event_emitter: BaseEventHooks,
    method_description: Optional[str] = ...,
    example_prefix: Optional[str] = ...,
    include_input: Optional[Any] = ...,
    include_output: Optional[Any] = ...,
    exclude_input: Optional[Any] = ...,
    exclude_output: Optional[Any] = ...,
    document_output: bool = ...,
    resource_action_model: Optional[Any] = ...,
    include_signature: bool = ...,
) -> None: ...
