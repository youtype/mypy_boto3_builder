"""
Type annotations for aiobotocore.retryhandler module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from botocore.config import Config
from botocore.retryhandler import CRC32Checker, MaxAttemptsDecorator, MultiChecker, RetryHandler

def create_retry_handler(config: Config, operation_name: str | None = ...) -> AioRetryHandler: ...
def create_checker_from_retry_config(
    config: Config, operation_name: str | None = ...
) -> AioMaxAttemptsDecorator: ...

class AioRetryHandler(RetryHandler):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class AioMaxAttemptsDecorator(MaxAttemptsDecorator):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class AioMultiChecker(MultiChecker):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class AioCRC32Checker(CRC32Checker):
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
