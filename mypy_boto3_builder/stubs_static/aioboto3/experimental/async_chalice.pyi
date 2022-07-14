from contextlib import AsyncExitStack as AsyncExitStack
from contextlib import asynccontextmanager as asynccontextmanager
from typing import Any, Optional

from aioboto3 import Session as Session
from chalice import Chalice  # type: ignore
from chalice.app import RestAPIEventHandler  # type: ignore

class AsyncRestAPIEventHandler(RestAPIEventHandler): ...

class AsyncChalice(Chalice):
    aioboto3: Any
    def __init__(
        self, *args: Any, aioboto3_session: Optional[Session] = ..., **kwargs: Any
    ) -> None: ...
    lambda_context: Any
    current_request: Any
    def __call__(self, event: Any, context: Any) -> Any: ...
