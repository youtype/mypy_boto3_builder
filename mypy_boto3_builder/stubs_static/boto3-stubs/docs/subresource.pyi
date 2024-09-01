from .base import NestedDocumenter
from botocore.docs.bcdoc.restdoc import DocumentStructure
from boto3.resources.model import ResourceModel
from botocore.model import ServiceModel

class SubResourceDocumenter(NestedDocumenter):
    def document_sub_resources(self, section: DocumentStructure) -> None: ...

def document_sub_resource(
    section: DocumentStructure,
    resource_name: str,
    sub_resource_model: ResourceModel,
    service_model: ServiceModel,
    include_signature: bool = ...,
) -> None: ...
