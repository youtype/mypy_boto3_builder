from contextlib import AsyncExitStack as AsyncExitStack
from contextlib import asynccontextmanager as asynccontextmanager
from typing import Any, Optional

from aioboto3 import Session as Session
from chalice import Chalice
from chalice.app import RestAPIEventHandler

class AsyncRestAPIEventHandler(RestAPIEventHandler): ...

class AsyncChalice(Chalice):
    aioboto3: Any
    def __init__(self, *args, aioboto3_session: Optional[Session] = ..., **kwargs) -> None: ...
    lambda_context: Any
    current_request: Any
    def __call__(self, event, context): ...
