import sys
from typing import Any, Mapping, Optional, Type

from botocore.awsrequest import AWSResponse as AWSResponse
from botocore.client import BaseClient
from botocore.exceptions import ParamValidationError as ParamValidationError
from botocore.exceptions import StubAssertionError as StubAssertionError
from botocore.exceptions import StubResponseError as StubResponseError
from botocore.exceptions import UnStubbedResponseError as UnStubbedResponseError
from botocore.validate import validate_parameters as validate_parameters

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

class _ANY:
    def __eq__(self, other: object) -> Literal[True]: ...
    def __ne__(self, other: object) -> Literal[False]: ...

ANY: _ANY

class Stubber:
    client: BaseClient = ...
    def __init__(self, client: BaseClient) -> None: ...
    def __enter__(self) -> Stubber: ...
    def __exit__(
        self, exception_type: Type[Exception], exception_value: Any, traceback: Any
    ) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def add_response(
        self,
        method: str,
        service_response: Mapping[str, Any],
        expected_params: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    def add_client_error(
        self,
        method: str,
        service_error_code: str = ...,
        service_message: str = ...,
        http_status_code: int = ...,
        service_error_meta: Optional[Mapping[str, Any]] = ...,
        expected_params: Optional[Mapping[str, Any]] = ...,
        response_meta: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    def assert_no_pending_responses(self) -> None: ...
