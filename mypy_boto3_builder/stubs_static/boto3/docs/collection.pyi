from typing import Any
from boto3.docs.base import NestedDocumenter
from botocore.hooks import BaseEventHooks

class CollectionDocumenter(NestedDocumenter):
    def document_collections(self, section: Any) -> None: ...

def document_collection_object(
    section: Any, collection_model: Any, include_signature: bool = ...
) -> None: ...
def document_batch_action(
    section: Any,
    resource_name: str,
    event_emitter: BaseEventHooks,
    batch_action_model: Any,
    service_model: Any,
    collection_model: Any,
    include_signature: bool = ...,
) -> None: ...
def document_collection_method(
    section: Any,
    resource_name: str,
    action_name: str,
    event_emitter: BaseEventHooks,
    collection_model: Any,
    service_model: Any,
    include_signature: bool = ...,
) -> None: ...
