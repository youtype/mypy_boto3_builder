from botocore.docs.params import ResponseParamsDocumenter
from botocore.hooks import BaseEventHooks
from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.model import Shape
from boto3.resources.model import Identifier

class ResourceShapeDocumenter(ResponseParamsDocumenter):
    EVENT_NAME: str

def document_attribute(
    section: DocumentStructure,
    service_name: str,
    resource_name: str,
    attr_name: str,
    event_emitter: BaseEventHooks,
    attr_model: Shape,
    include_signature: bool = True,
) -> None: ...
def document_identifier(
    section: DocumentStructure,
    resource_name: str,
    identifier_model: Identifier,
    include_signature: bool = ...,
) -> None: ...
def document_reference(
    section: DocumentStructure, reference_model: Shape, include_signature: bool = ...
) -> None: ...
