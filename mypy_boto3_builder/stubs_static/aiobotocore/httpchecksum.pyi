from botocore.httpchecksum import AwsChunkedWrapper
from botocore.awsrequest import AWSHTTPResponse, AWSRequest
from botocore.model import OperationModel

from typing import TypeVar, Dict, Any, Mapping


_R = TypeVar("_R")


class AioAwsChunkedWrapper(AwsChunkedWrapper):
    async def _make_chunk(self) -> bytes: ...

    def __aiter__(self: _R) -> _R:
        return self

    async def __anext__(self) -> bytes: ...


async def handle_checksum_body(
    http_response: AWSHTTPResponse,
    response: Dict[str, Any],
    context: Mapping[str, Any],
    operation_model: OperationModel,
) -> None: ...

def apply_request_checksum(request: AWSRequest) -> None: ...