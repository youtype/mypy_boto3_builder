from typing import AsyncIterator, Generic, Iterator, TypeVar

from botocore.eventstream import EventStream

_T = TypeVar("_T")

class AioEventStream(Generic[_T], EventStream[_T]):
    def __iter__(self) -> Iterator[_T]: ...
    def __aiter__(self) -> AsyncIterator[_T]: ...
    async def __anext__(self) -> _T: ...
    async def get_initial_response(self) -> _T: ...  # type: ignore [override]
