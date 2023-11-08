from types import TracebackType
from typing import Any, Dict, Optional, Type, TypeVar

from botocore.endpoint import MAX_POOL_CONNECTIONS as MAX_POOL_CONNECTIONS
from requests.models import Request, Response

_R = TypeVar("_R")

class AIOHTTPSession:
    def __init__(
        self,
        verify: bool = ...,
        proxies: Optional[Dict[str, str]] = ...,
        timeout: Optional[float] = ...,
        max_pool_connections: int = ...,
        socket_options: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        proxies_config: Optional[Any] = ...,
        connector_args: Optional[Any] = ...,
    ) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_val: Optional[Exception],
        tb: Optional[TracebackType],
    ) -> None: ...
    async def close(self) -> None: ...
    async def send(self, request: Request) -> Response: ...
