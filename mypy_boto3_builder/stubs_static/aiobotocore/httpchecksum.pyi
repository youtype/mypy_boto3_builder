from typing import Any, Dict, Mapping, TypeVar

from botocore.awsrequest import AWSHTTPResponse, AWSRequest
from botocore.httpchecksum import AwsChunkedWrapper
from botocore.model import OperationModel

_R = TypeVar("_R")

class AioAwsChunkedWrapper(AwsChunkedWrapper):
    async def _make_chunk(self) -> bytes: ...
    def __aiter__(self: _R) -> _R: ...
    async def __anext__(self) -> bytes: ...

async def handle_checksum_body(
    http_response: AWSHTTPResponse,
    response: Dict[str, Any],
    context: Mapping[str, Any],
    operation_model: OperationModel,
) -> None: ...
def apply_request_checksum(request: AWSRequest) -> None: ...
