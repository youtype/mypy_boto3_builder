"""
Type annotations for aioboto3.s3.cse module.

Copyright 2024 Vlad Emelianov
"""

import asyncio
from types import TracebackType
from typing import IO, Any, Mapping, TypeVar

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

_R = TypeVar("_R")

RANGE_REGEX: Any
AES_BLOCK_SIZE: int
AES_BLOCK_SIZE_BYTES: int
JAVA_LONG_MAX_VALUE: int

class DummyAIOFile:
    file: IO[Any]
    def __init__(self, data: bytes) -> None: ...
    async def read(self, n: int = ...) -> bytes: ...
    async def readany(self) -> bytes: ...
    async def readexactly(self, n: int) -> bytes: ...
    async def readchunk(self) -> bytes: ...

class DecryptError(Exception): ...

class CryptoContext:
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> tuple[bytes, dict[str, str], str]: ...

class AsymmetricCryptoContext(CryptoContext):
    public_key: RSAPublicKey
    private_key: RSAPrivateKey
    def __init__(
        self,
        public_key: RSAPublicKey | None = ...,
        private_key: RSAPrivateKey | None = ...,
        loop: asyncio.AbstractEventLoop | None = ...,
    ) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> tuple[bytes, dict[str, str], str]: ...
    @staticmethod
    def from_der_public_key(data: bytes) -> RSAPublicKey: ...
    @staticmethod
    def from_der_private_key(data: bytes, password: str | None = ...) -> RSAPrivateKey: ...

class SymmetricCryptoContext(CryptoContext):
    key: bytes
    def __init__(self, key: bytes, loop: asyncio.AbstractEventLoop | None = ...) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> tuple[bytes, dict[str, str], str]: ...

class KMSCryptoContext(CryptoContext):
    kms_key: str
    authenticated_encryption: bool
    def __init__(
        self,
        keyid: str | None = ...,
        kms_client_args: dict[str, Any] | None = ...,
        authenticated_encryption: bool = ...,
    ) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> tuple[bytes, dict[str, str], str]: ...

class MockKMSCryptoContext(KMSCryptoContext):
    aes_key: bytes
    material_description: dict[str, Any]
    encrypted_key: bytes
    authenticated_encryption: bool
    def __init__(
        self,
        aes_key: bytes,
        material_description: dict[str, Any],
        encrypted_key: bytes,
        authenticated_encryption: bool = ...,
    ) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def get_decryption_aes_key(
        self, key: bytes, material_description: dict[str, Any]
    ) -> bytes: ...
    async def get_encryption_aes_key(self) -> tuple[bytes, dict[str, str], str]: ...

class S3CSE:
    def __init__(
        self, crypto_context: CryptoContext, s3_client_args: dict[str, Any] | None = ...
    ) -> None: ...
    async def setup(self) -> None: ...
    async def close(self) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    async def get_object(self, Bucket: str, Key: str, **kwargs: Any) -> dict[str, Any]: ...
    async def put_object(
        self,
        Body: bytes | IO[Any],
        Bucket: str,
        Key: str,
        Metadata: Mapping[str, Any] | None = ...,
        **kwargs: Any,
    ) -> Any: ...
