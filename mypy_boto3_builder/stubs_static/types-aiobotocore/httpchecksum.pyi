"""
Type annotations for aiobotocore.httpchecksum module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, Mapping, TypeVar

from aiobotocore.response import StreamingBody
from aiohttp import StreamReader
from botocore.awsrequest import AWSHTTPResponse, AWSRequest
from botocore.httpchecksum import AwsChunkedWrapper, BaseChecksum
from botocore.model import OperationModel

_R = TypeVar("_R")

class AioAwsChunkedWrapper(AwsChunkedWrapper):
    async def _make_chunk(self) -> bytes: ...
    def __aiter__(self: _R) -> _R: ...
    async def __anext__(self) -> bytes: ...

class StreamingChecksumBody(StreamingBody):
    def __init__(
        self,
        raw_stream: StreamReader,
        content_length: str,
        checksum: BaseChecksum,
        expected: BaseChecksum,
    ) -> None: ...
    async def read(self, amt: int | None = ...) -> bytes: ...

async def handle_checksum_body(
    http_response: AWSHTTPResponse,
    response: dict[str, Any],
    context: Mapping[str, Any],
    operation_model: OperationModel,
) -> None: ...
def apply_request_checksum(request: AWSRequest) -> None: ...
