from typing import Any, TypeVar

from botocore.config import Config

_AioConfig = TypeVar("_AioConfig", bound="AioConfig")

class AioConfig(Config):
    def __init__(self, connector_args: Any = ..., **kwargs: Any) -> None: ...
    def merge(self: _AioConfig, other_config: Config) -> _AioConfig: ...
