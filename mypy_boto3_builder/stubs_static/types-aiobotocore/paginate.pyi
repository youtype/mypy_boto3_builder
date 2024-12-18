"""
Type annotations for aiobotocore.paginate module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, AsyncIterator, Iterator

from botocore.paginate import PageIterator, Paginator

class AioPageIterator(PageIterator):
    def __aiter__(self) -> Any: ...
    resume_token: Any
    async def __anext__(self) -> Any: ...
    def result_key_iters(self) -> Any: ...
    async def build_full_result(self) -> Any: ...
    async def search(self, expression: str) -> Iterator[Any]: ...  # type: ignore[override]

class AioPaginator(Paginator):
    PAGE_ITERATOR_CLS: type[AioPageIterator]

class ResultKeyIterator:
    result_key: str
    def __init__(self, pages_iterator: PageIterator, result_key: str) -> None: ...
    def __aiter__(self) -> AsyncIterator[Any]: ...
    async def __anext__(self) -> Any: ...
