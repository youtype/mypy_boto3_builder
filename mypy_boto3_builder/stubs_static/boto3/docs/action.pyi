from typing import Dict, List, Any
from boto3.docs.base import NestedDocumenter
from botocore.hooks import BaseEventHooks

PUT_DATA_WARNING_MESSAGE: str
WARNING_MESSAGES: Dict[str, Dict[str, str]]
IGNORE_PARAMS: Dict[str, Dict[str, List[str]]]

class ActionDocumenter(NestedDocumenter):
    def document_actions(self, section: Any) -> None: ...

def document_action(
    section: Any,
    resource_name: str,
    event_emitter: BaseEventHooks,
    action_model: Any,
    service_model: Any,
    include_signature: bool = ...,
) -> None: ...
def document_load_reload_action(
    section: Any,
    action_name: str,
    resource_name: str,
    event_emitter: BaseEventHooks,
    load_model: Any,
    service_model: Any,
    include_signature: bool = ...,
) -> None: ...
