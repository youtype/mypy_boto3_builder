from typing import Any

from botocore.retries.base import BaseRetryableChecker as BaseRetryableChecker

class RetryIDPCommunicationError(BaseRetryableChecker):
    def is_retryable(self, context: Any) -> Any: ...

class RetryDDBChecksumError(BaseRetryableChecker):
    def is_retryable(self, context: Any) -> Any: ...
