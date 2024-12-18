"""
Type annotations for aiobotocore.tokens module.

Copyright 2024 Vlad Emelianov
"""

import datetime
from logging import Logger
from typing import Any, Callable

from botocore.session import Session
from botocore.tokens import (
    DeferredRefreshableToken,
    FrozenAuthToken,
    SSOTokenProvider,
    TokenProviderChain,
)

logger: Logger

def create_token_resolver(session: Session) -> TokenProviderChain: ...

class AioDeferredRefreshableToken(DeferredRefreshableToken):
    def __init__(
        self,
        method: Any,
        refresh_using: Callable[[], FrozenAuthToken],
        time_fetcher: Callable[[], datetime.datetime] = ...,
    ) -> None: ...
    async def get_frozen_token(self) -> FrozenAuthToken: ...  # type: ignore[override]

class AioSSOTokenProvider(SSOTokenProvider):
    def load_token(self) -> AioDeferredRefreshableToken: ...
