from typing import Any, Type, TypeVar

from aiobotocore.httpsession import AIOHTTPSession
from botocore.config import Config

_AioConfig = TypeVar("_AioConfig", bound="AioConfig")

class AioConfig(Config):
    def __init__(
        self, connector_args: Any = ..., http_session_cls: Type[AIOHTTPSession] = ..., **kwargs: Any
    ) -> None: ...
    def merge(self: _AioConfig, other_config: Config) -> _AioConfig: ...
