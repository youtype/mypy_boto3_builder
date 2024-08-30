from typing import Any
from botocore.docs.params import ResponseParamsDocumenter
from botocore.hooks import BaseEventHooks

class ResourceShapeDocumenter(ResponseParamsDocumenter):
    EVENT_NAME: str

def document_attribute(
    section: Any,
    service_name: str,
    resource_name: str,
    attr_name: str,
    event_emitter: BaseEventHooks,
    attr_model: Any,
    include_signature: bool = True,
) -> None: ...
def document_identifier(
    section: Any, resource_name: str, identifier_model: Any, include_signature: bool = ...
) -> None: ...
def document_reference(
    section: Any, reference_model: Any, include_signature: bool = ...
) -> None: ...
