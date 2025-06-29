"""
Type annotations for aiobotocore.stub module.

Copyright 2025 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Any

from botocore.stub import Stubber

class AioStubber(Stubber):
    def add_client_error(
        self,
        method: str,
        service_error_code: str = ...,
        service_message: str = ...,
        http_status_code: int = ...,
        service_error_meta: Mapping[str, Any] | None = ...,
        expected_params: Mapping[str, Any] | None = ...,
        response_meta: Mapping[str, Any] | None = ...,
        modeled_fields: Mapping[str, Any] | None = ...,
    ) -> None: ...
