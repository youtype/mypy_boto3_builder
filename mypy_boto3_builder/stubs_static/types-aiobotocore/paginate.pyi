"""
Type annotations for aiobotocore.paginate module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, AsyncIterator, Generic, TypeVar

from botocore.paginate import PageIterator, Paginator

_R = TypeVar("_R")

class AioPageIterator(PageIterator[_R], Generic[_R]):
    def __aiter__(self) -> AsyncIterator[_R]: ...
    async def __anext__(self) -> _R: ...
    def result_key_iters(self) -> Any: ...
    async def build_full_result(self) -> dict[str, Any]: ...  # type: ignore[override]
    def search(self, expression: str) -> AsyncIterator[_R]: ...  # type: ignore[override]

class AioPaginator(Paginator[_R], Generic[_R]):
    PAGE_ITERATOR_CLS: type[AioPageIterator[Any]]  # type: ignore[override]

class ResultKeyIterator(Generic[_R]):
    result_key: str
    def __init__(self, pages_iterator: PageIterator[_R], result_key: str) -> None: ...
    def __aiter__(self) -> AsyncIterator[_R]: ...
    async def __anext__(self) -> _R: ...
