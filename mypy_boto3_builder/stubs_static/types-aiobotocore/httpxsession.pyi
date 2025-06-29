"""
Type annotations for aiobotocore.httpxsession module.

Copyright 2025 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, TypeVar

from aiobotocore.awsrequest import HttpxAWSResponse
from botocore.awsrequest import AWSPreparedRequest

_R = TypeVar("_R", bound=HttpxSession)

class HttpxSession:
    def __init__(
        self,
        verify: bool = ...,
        proxies: dict[str, str] | None = ...,
        timeout: float | list[float] | tuple[float, float] | None = ...,
        max_pool_connections: int = ...,
        socket_options: list[Any] | None = ...,
        client_cert: str | tuple[str, str] | None = ...,
        proxies_config: dict[str, str] | None = ...,
        connector_args: dict[str, Any] | None = ...,
    ) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    async def close(self) -> None: ...
    async def send(self, request: AWSPreparedRequest) -> HttpxAWSResponse: ...
