"""
Type annotations for aioboto3.resources.base module.

Copyright 2024 Vlad Emelianov
"""

import logging
from types import TracebackType
from typing import TypeVar

from boto3.resources.base import ServiceResource

_R = TypeVar("_R", bound=AIOBoto3ServiceResource)

logger: logging.Logger

class AIOBoto3ServiceResource(ServiceResource):
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
