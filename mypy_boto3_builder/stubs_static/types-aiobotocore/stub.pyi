from typing import Any, Mapping, Optional

from botocore.stub import Stubber

class AioStubber(Stubber):
    def add_client_error(
        self,
        method: str,
        service_error_code: str = ...,
        service_message: str = ...,
        http_status_code: int = ...,
        service_error_meta: Optional[Mapping[str, Any]] = ...,
        expected_params: Optional[Mapping[str, Any]] = ...,
        response_meta: Optional[Mapping[str, Any]] = ...,
        modeled_fields: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
