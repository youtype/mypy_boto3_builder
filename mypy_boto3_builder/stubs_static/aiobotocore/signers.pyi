from typing import Any, Mapping, Optional

from botocore.auth import BaseSigner
from botocore.signers import RequestSigner, S3PostPresigner
from requests.models import Request

class AioRequestSigner(RequestSigner):
    async def handler(
        self, operation_name: Optional[Any] = ..., request: Optional[Any] = ..., **kwargs: Any
    ) -> None: ...
    async def sign(  # type: ignore [override]
        self,
        operation_name: str,
        request: Request,
        region_name: Optional[Any] = ...,
        signing_type: str = ...,
        expires_in: Optional[Any] = ...,
        signing_name: Optional[Any] = ...,
    ) -> None: ...
    async def get_auth_instance(
        self,
        signing_name: str,
        region_name: str,
        signature_version: Optional[Any] = ...,
        **kwargs: Any,
    ) -> BaseSigner: ...
    get_auth: Any
    async def generate_presigned_url(
        self,
        request_dict: Mapping[str, Any],
        operation_name: str,
        expires_in: int = ...,
        region_name: Optional[Any] = ...,
        signing_name: Optional[Any] = ...,
    ) -> Any: ...

def add_generate_db_auth_token(class_attributes: Any, **kwargs: Any) -> None: ...
async def generate_db_auth_token(
    self: Any, DBHostname: Any, Port: Any, DBUsername: Any, Region: Optional[Any] = ...
) -> Any: ...
def add_generate_presigned_url(class_attributes: Any, **kwargs: Any) -> None: ...
async def generate_presigned_url(
    self: Any,
    ClientMethod: str,
    Params: Optional[Any] = ...,
    ExpiresIn: int = ...,
    HttpMethod: Optional[Any] = ...,
) -> Any: ...

class AioS3PostPresigner(S3PostPresigner):
    async def generate_presigned_post(
        self,
        request_dict: Mapping[str, Any],
        fields: Optional[Any] = ...,
        conditions: Optional[Any] = ...,
        expires_in: int = ...,
        region_name: Optional[Any] = ...,
    ) -> Any: ...

def add_generate_presigned_post(class_attributes: Any, **kwargs: Any) -> None: ...
async def generate_presigned_post(
    self: Any,
    Bucket: str,
    Key: str,
    Fields: Optional[Any] = ...,
    Conditions: Optional[Any] = ...,
    ExpiresIn: int = ...,
) -> Any: ...
