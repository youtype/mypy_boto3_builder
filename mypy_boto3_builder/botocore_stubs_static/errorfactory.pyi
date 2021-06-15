from typing import Mapping, Type

from botocore.exceptions import ClientError as ClientError
from botocore.exceptions import ClientError as _ClientError
from botocore.model import ServiceModel
from botocore.utils import get_service_module_name as get_service_module_name

class BaseClientExceptions:
    ClientError: Type[_ClientError] = ...
    def __init__(self, code_to_exception: Mapping[str, Type[_ClientError]]) -> None: ...
    def from_code(self, error_code: str) -> ClientError: ...
    def __getattr__(self, name: str) -> None: ...

class ClientExceptionsFactory:
    def __init__(self) -> None: ...
    def create_client_exceptions(self, service_model: ServiceModel) -> BaseClientExceptions: ...
