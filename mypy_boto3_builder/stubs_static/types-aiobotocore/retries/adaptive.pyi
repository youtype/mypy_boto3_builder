"""
Type annotations for aiobotocore.retries.adaptive module.

Copyright 2024 Vlad Emelianov
"""

import logging
from typing import Any

from aiobotocore.client import AioBaseClient
from botocore.retries.adaptive import RateClocker
from botocore.retries.bucket import Clock, TokenBucket
from botocore.retries.standard import ThrottlingErrorDetector
from botocore.retries.throttling import CubicCalculator

logger: logging.Logger = ...

def register_retry_handler(client: AioBaseClient) -> AsyncClientRateLimiter: ...

class AsyncClientRateLimiter:
    def __init__(
        self,
        rate_adjustor: CubicCalculator,
        rate_clocker: RateClocker,
        token_bucket: TokenBucket,
        throttling_detector: ThrottlingErrorDetector,
        clock: Clock,
    ) -> None: ...
    async def on_sending_request(self, request: Any, **kwargs: Any) -> None: ...
    async def on_receiving_response(self, **kwargs: Any) -> None: ...
