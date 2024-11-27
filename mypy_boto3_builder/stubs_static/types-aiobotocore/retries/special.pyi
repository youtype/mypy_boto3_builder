"""
Type annotations for aiobotocore.retries.special module.

Copyright 2024 Vlad Emelianov
"""

from botocore.retries.special import RetryDDBChecksumError
from botocore.retries.standard import RetryContext

class AioRetryDDBChecksumError(RetryDDBChecksumError):
    async def is_retryable(self, context: RetryContext) -> bool: ...  # type: ignore
