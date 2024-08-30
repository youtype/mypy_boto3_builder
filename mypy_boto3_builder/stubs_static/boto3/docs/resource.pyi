from typing import Any
from boto3.docs.base import BaseDocumenter

class ResourceDocumenter(BaseDocumenter):
    def __init__(self, resource: Any, botocore_session: Any, root_docs_path: str) -> None: ...
    def document_resource(self, section: Any) -> None: ...

class ServiceResourceDocumenter(ResourceDocumenter):
    @property
    def class_name(self) -> str: ...
