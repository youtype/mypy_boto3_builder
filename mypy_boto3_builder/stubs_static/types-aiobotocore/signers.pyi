"""
Type annotations for aiobotocore.signers module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, Mapping

from aiobotocore.credentials import AioCredentials
from botocore.auth import BaseSigner
from botocore.signers import RequestSigner, S3PostPresigner
from requests.models import Request

class AioRequestSigner(RequestSigner):
    async def handler(
        self, operation_name: Any | None = ..., request: Any | None = ..., **kwargs: Any
    ) -> None: ...
    async def sign(  # type: ignore[override]
        self,
        operation_name: str,
        request: Request,
        region_name: Any | None = ...,
        signing_type: str = ...,
        expires_in: Any | None = ...,
        signing_name: Any | None = ...,
    ) -> None: ...
    async def get_auth_instance(  # type: ignore[override]
        self,
        signing_name: str,
        region_name: str,
        signature_version: Any | None = ...,
        request_credentials: AioCredentials | None = ...,
        **kwargs: Any,
    ) -> BaseSigner: ...
    get_auth: Any
    async def generate_presigned_url(
        self,
        request_dict: Mapping[str, Any],
        operation_name: str,
        expires_in: int = ...,
        region_name: str | None = ...,
        signing_name: str | None = ...,
    ) -> str: ...

def add_generate_db_auth_token(class_attributes: dict[str, Any], **kwargs: Any) -> None: ...
def add_dsql_generate_db_auth_token_methods(
    class_attributes: dict[str, Any], **kwargs: Any
) -> None: ...
async def generate_db_auth_token(
    self: Any, DBHostname: str, Port: int, DBUsername: str, Region: str | None = ...
) -> str: ...
async def dsql_generate_db_connect_auth_token(
    self: Any, Hostname: str, Region: str | None = ..., ExpiresIn: int = ...
) -> str: ...
async def dsql_generate_db_connect_admin_auth_token(
    self: Any, Hostname: str, Region: str | None = ..., ExpiresIn: int = ...
) -> str: ...

class AioS3PostPresigner(S3PostPresigner):
    async def generate_presigned_post(
        self,
        request_dict: Mapping[str, Any],
        fields: Any | None = ...,
        conditions: Any | None = ...,
        expires_in: int = ...,
        region_name: str | None = ...,
    ) -> Any: ...

def add_generate_presigned_url(class_attributes: dict[str, Any], **kwargs: Any) -> None: ...
async def generate_presigned_url(
    self: Any,
    ClientMethod: str,
    Params: Any | None = ...,
    ExpiresIn: int = ...,
    HttpMethod: str | None = ...,
) -> Any: ...
def add_generate_presigned_post(class_attributes: Any, **kwargs: Any) -> None: ...
async def generate_presigned_post(
    self: Any,
    Bucket: str,
    Key: str,
    Fields: Any | None = ...,
    Conditions: Any | None = ...,
    ExpiresIn: int = ...,
) -> Any: ...
