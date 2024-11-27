"""
Type annotations for aiobotocore.httpsession module.

Copyright 2024 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, TypeVar

from botocore.endpoint import MAX_POOL_CONNECTIONS as MAX_POOL_CONNECTIONS
from requests.models import Request, Response

_R = TypeVar("_R")

class AIOHTTPSession:
    def __init__(
        self,
        verify: bool = ...,
        proxies: dict[str, str] | None = ...,
        timeout: float | None = ...,
        max_pool_connections: int = ...,
        socket_options: Any | None = ...,
        client_cert: Any | None = ...,
        proxies_config: Any | None = ...,
        connector_args: Any | None = ...,
    ) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    async def close(self) -> None: ...
    async def send(self, request: Request) -> Response: ...
