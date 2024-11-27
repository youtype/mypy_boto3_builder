"""
Type annotations for aiobotocore.retries.standard module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from botocore.client import BaseClient
from botocore.retries.standard import (
    OrRetryChecker,
    RetryContext,
    RetryHandler,
    RetryPolicy,
    StandardRetryConditions,
)

def register_retry_handler(client: BaseClient, max_attempts: int = ...) -> AioRetryHandler: ...

class AioRetryHandler(RetryHandler):
    async def needs_retry(self, **kwargs: Any) -> float | None: ...  # type: ignore

class AioRetryPolicy(RetryPolicy):
    async def should_retry(self, context: RetryContext) -> bool: ...

class AioStandardRetryConditions(StandardRetryConditions):
    def __init__(self, max_attempts: int = ...) -> None: ...
    async def is_retryable(self, context: RetryContext) -> bool: ...  # type: ignore

class AioOrRetryChecker(OrRetryChecker):
    async def is_retryable(self, context: RetryContext) -> bool: ...  # type: ignore
