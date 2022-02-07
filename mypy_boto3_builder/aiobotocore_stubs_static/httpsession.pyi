from typing import Any, Dict, Optional

from aiobotocore import DEPRECATED_1_4_0_APIS as DEPRECATED_1_4_0_APIS
from requests.models import Request, Response

class AIOHTTPSession:
    def __init__(
        self,
        verify: bool = ...,
        proxies: Dict[str, str] = ...,
        timeout: float = ...,
        max_pool_connections: int = ...,
        socket_options: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        proxies_config: Optional[Any] = ...,
        connector_args: Optional[Any] = ...,
    ) -> None: ...
    async def __aenter__(self) -> Any: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    async def close(self) -> None: ...
    async def send(self, request: Request) -> Response: ...
