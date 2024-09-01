from typing import Any, Optional

from aioboto3.session import Session as Session
from chalice import Chalice  # type: ignore
from chalice.app import RestAPIEventHandler  # type: ignore

class AsyncRestAPIEventHandler(RestAPIEventHandler): ...  # type: ignore

class AsyncChalice(Chalice):  # type: ignore
    aioboto3: Any
    def __init__(
        self, *args: Any, aioboto3_session: Optional[Session] = ..., **kwargs: Any
    ) -> None: ...
    lambda_context: Any
    current_request: Any
    def __call__(self, event: Any, context: Any) -> Any: ...
