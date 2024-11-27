from typing import Any
from .base import BaseDocumenter
from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.session import Session

class ResourceDocumenter(BaseDocumenter):
    def __init__(self, resource: Any, botocore_session: Session, root_docs_path: str) -> None: ...
    def document_resource(self, section: DocumentStructure) -> None: ...

class ServiceResourceDocumenter(ResourceDocumenter):
    @property
    def class_name(self) -> str: ...
