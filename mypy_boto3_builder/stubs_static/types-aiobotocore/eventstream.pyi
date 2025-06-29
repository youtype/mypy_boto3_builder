"""
Type annotations for aiobotocore.eventstream module.

Copyright 2025 Vlad Emelianov
"""

from collections.abc import AsyncIterator, Iterator
from typing import Generic, TypeVar

from botocore.eventstream import EventStream

_T = TypeVar("_T")

class AioEventStream(EventStream[_T], Generic[_T]):
    def __iter__(self) -> Iterator[_T]: ...
    def __aiter__(self) -> AsyncIterator[_T]: ...
    async def __anext__(self) -> _T: ...
    async def get_initial_response(self) -> _T: ...  # type: ignore[override]
