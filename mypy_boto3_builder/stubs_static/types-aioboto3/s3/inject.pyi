"""
Type annotations for aioboto3.s3.inject module.

Copyright 2024 Vlad Emelianov
"""

import logging
from abc import abstractmethod
from typing import Any, BinaryIO, Callable, Sequence

from boto3.s3.transfer import TransferConfig as S3TransferConfig

logger: logging.Logger

class _AsyncBinaryIO:
    @abstractmethod
    async def seek(self, offset: int, whence: int = 0) -> int: ...
    @abstractmethod
    async def write(self, s: bytes | bytearray) -> int: ...

def inject_s3_transfer_methods(class_attributes: Sequence[Any], **kwargs: Any) -> None: ...
def inject_object_summary_methods(class_attributes: Sequence[Any], **kwargs: Any) -> None: ...
def inject_bucket_methods(class_attributes: Sequence[Any], **kwargs: Any) -> None: ...
async def object_summary_load(self: Any, *args: Any, **kwargs: Any) -> None: ...
async def download_file(
    self: Any,
    Bucket: str,
    Key: str,
    Filename: str,
    ExtraArgs: list[str] | None = ...,
    Callback: Callable[[int], None] | None = ...,
    Config: S3TransferConfig | None = ...,
) -> None: ...
async def download_fileobj(
    self: Any,
    Bucket: str,
    Key: str,
    Fileobj: _AsyncBinaryIO | BinaryIO,
    ExtraArgs: dict[str, Any] | None = ...,
    Callback: Callable[[int], None] | None = ...,
    Config: S3TransferConfig | None = ...,
) -> None: ...
async def upload_fileobj(
    self: Any,
    Fileobj: _AsyncBinaryIO | BinaryIO,
    Bucket: str,
    Key: str,
    ExtraArgs: dict[str, Any] | None = ...,
    Callback: Callable[[int], None] | None = ...,
    Config: S3TransferConfig | None = ...,
    Processing: Callable[[bytes], bytes] | None = ...,
) -> Any: ...
async def upload_file(
    self: Any,
    Filename: str,
    Bucket: str,
    Key: str,
    ExtraArgs: dict[str, Any] | None = ...,
    Callback: Callable[[int], None] | None = ...,
    Config: S3TransferConfig | None = ...,
) -> None: ...
async def copy(
    self: Any,
    CopySource: Any,
    Bucket: str,
    Key: str,
    ExtraArgs: dict[str, Any] | None = ...,
    Callback: Callable[[int], None] | None = ...,
    SourceClient: Any | None = ...,
    Config: S3TransferConfig | None = ...,
) -> None: ...
async def bucket_load(self: Any, *args: Any, **kwargs: Any) -> None: ...
