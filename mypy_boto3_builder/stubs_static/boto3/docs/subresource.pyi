from typing import Any
from boto3.docs.base import NestedDocumenter

class SubResourceDocumenter(NestedDocumenter):
    def document_sub_resources(self, section: Any) -> None: ...

def document_sub_resource(
    section: Any,
    resource_name: str,
    sub_resource_model: Any,
    service_model: Any,
    include_signature: bool = ...,
) -> None: ...
