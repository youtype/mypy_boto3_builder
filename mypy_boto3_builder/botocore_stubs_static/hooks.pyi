from typing import Any, NamedTuple, Optional

from botocore.compat import accepts_kwargs as accepts_kwargs
from botocore.utils import EVENT_ALIASES as EVENT_ALIASES

class _NodeList(NamedTuple):
    first: Any
    middle: Any
    last: Any

class NodeList(_NodeList): ...

def first_non_none_response(responses: Any, default: Optional[Any] = ...) -> Any: ...

class BaseEventHooks:
    def emit(self, event_name: Any, **kwargs: Any) -> Any: ...
    def register(
        self,
        event_name: Any,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def register_first(
        self,
        event_name: Any,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def register_last(
        self,
        event_name: Any,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def unregister(
        self,
        event_name: Any,
        handler: Optional[Any] = ...,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...

class HierarchicalEmitter(BaseEventHooks):
    def __init__(self) -> None: ...
    def emit(self, event_name: Any, **kwargs: Any) -> Any: ...
    def emit_until_response(self, event_name: Any, **kwargs: Any) -> Any: ...
    def unregister(
        self,
        event_name: Any,
        handler: Optional[Any] = ...,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...

class EventAliaser(BaseEventHooks):
    def __init__(self, event_emitter: Any, event_aliases: Optional[Any] = ...) -> None: ...
    def emit(self, event_name: Any, **kwargs: Any) -> Any: ...
    def emit_until_response(self, event_name: Any, **kwargs: Any) -> Any: ...
    def register(
        self,
        event_name: Any,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> Any: ...
    def register_first(
        self,
        event_name: Any,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> Any: ...
    def register_last(
        self,
        event_name: Any,
        handler: Any,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> Any: ...
    def unregister(
        self,
        event_name: Any,
        handler: Optional[Any] = ...,
        unique_id: Optional[Any] = ...,
        unique_id_uses_count: bool = ...,
    ) -> Any: ...

class _PrefixTrie:
    def __init__(self) -> None: ...
    def append_item(self, key: Any, value: Any, section: Any = ...) -> None: ...
    def prefix_search(self, key: Any) -> Any: ...
    def remove_item(self, key: Any, value: Any) -> None: ...
