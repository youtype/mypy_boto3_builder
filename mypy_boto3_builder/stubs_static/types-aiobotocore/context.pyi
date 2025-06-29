"""
Type annotations for aiobotocore.context module.

Copyright 2025 Vlad Emelianov
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any, Callable

from botocore.context import ClientContext

@asynccontextmanager  # type: ignore[misc, arg-type]
async def start_as_current_context(
    ctx: ClientContext | None = ...,
) -> AsyncGenerator[None, None]: ...
def with_current_context(
    hook: Callable[[], Any] | None = ...,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
