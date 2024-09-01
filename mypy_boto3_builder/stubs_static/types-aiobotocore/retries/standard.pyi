from typing import Any, Optional

from botocore.client import BaseClient
from botocore.retries.standard import (
    OrRetryChecker,
    RetryContext,
    RetryHandler,
    RetryPolicy,
    StandardRetryConditions,
)

def register_retry_handler(client: BaseClient, max_attempts: int = ...) -> "AioRetryHandler": ...

class AioRetryHandler(RetryHandler):
    async def needs_retry(self, **kwargs: Any) -> Optional[float]: ...  # type: ignore

class AioRetryPolicy(RetryPolicy):
    async def should_retry(self, context: RetryContext) -> bool: ...

class AioStandardRetryConditions(StandardRetryConditions):
    def __init__(self, max_attempts: int = ...) -> None: ...
    async def is_retryable(self, context: RetryContext) -> bool: ...  # type: ignore

class AioOrRetryChecker(OrRetryChecker):
    async def is_retryable(self, context: RetryContext) -> bool: ...  # type: ignore
