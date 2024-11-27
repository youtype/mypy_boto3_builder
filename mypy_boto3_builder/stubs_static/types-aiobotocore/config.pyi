"""
Type annotations for aiobotocore.config module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, TypeVar

from aiobotocore.httpsession import AIOHTTPSession
from botocore.config import Config

_Config = TypeVar("_Config", bound=Config)

class AioConfig(Config):
    def __init__(
        self, connector_args: Any = ..., http_session_cls: type[AIOHTTPSession] = ..., **kwargs: Any
    ) -> None: ...
    def merge(self: _Config, other_config: _Config) -> _Config: ...
