from .base import NestedDocumenter
from botocore.hooks import BaseEventHooks
from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.model import ServiceModel
from boto3.resources.model import Collection
from boto3.resources.model import Action

class CollectionDocumenter(NestedDocumenter):
    def document_collections(self, section: DocumentStructure) -> None: ...

def document_collection_object(
    section: DocumentStructure, collection_model: Collection, include_signature: bool = ...
) -> None: ...
def document_batch_action(
    section: DocumentStructure,
    resource_name: str,
    event_emitter: BaseEventHooks,
    batch_action_model: Action,
    service_model: ServiceModel,
    collection_model: Collection,
    include_signature: bool = ...,
) -> None: ...
def document_collection_method(
    section: DocumentStructure,
    resource_name: str,
    action_name: str,
    event_emitter: BaseEventHooks,
    collection_model: Collection,
    service_model: ServiceModel,
    include_signature: bool = ...,
) -> None: ...
