from typing import Dict, List
from .base import NestedDocumenter
from botocore.hooks import BaseEventHooks
from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.model import ServiceModel
from boto3.resources.model import Action

PUT_DATA_WARNING_MESSAGE: str
WARNING_MESSAGES: Dict[str, Dict[str, str]]
IGNORE_PARAMS: Dict[str, Dict[str, List[str]]]

class ActionDocumenter(NestedDocumenter):
    def document_actions(self, section: DocumentStructure) -> None: ...

def document_action(
    section: DocumentStructure,
    resource_name: str,
    event_emitter: BaseEventHooks,
    action_model: Action,
    service_model: ServiceModel,
    include_signature: bool = ...,
) -> None: ...
def document_load_reload_action(
    section: DocumentStructure,
    action_name: str,
    resource_name: str,
    event_emitter: BaseEventHooks,
    load_model: Action,
    service_model: ServiceModel,
    include_signature: bool = ...,
) -> None: ...
