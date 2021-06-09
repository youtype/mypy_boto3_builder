from typing import Any, Callable, Dict, List

from botocore.client import BaseClient

from . import xform_name as xform_name

def create_waiter_with_client(
    waiter_name: str, waiter_model: WaiterModel, client: BaseClient
) -> Waiter: ...

class NormalizedOperationMethod:
    def __init__(self, client_method: Callable[..., None]) -> None: ...
    def __call__(self, **kwargs: Any) -> Any: ...

class WaiterModel:
    SUPPORTED_VERSION: int = ...
    def __init__(self, waiter_config: Dict[str, Any]) -> None:
        self.version: str
        self.waiter_names: List[str]
    def get_waiter(self, waiter_name: str) -> "SingleWaiterConfig": ...

class SingleWaiterConfig:
    def __init__(self, single_waiter_config: Dict[str, Any]) -> None:
        self.description: str
        self.operation: str
        self.delay: int
        self.max_attempts: int
    @property
    def acceptors(self) -> List["AcceptorConfig"]: ...

class AcceptorConfig:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.state: str
        self.matcher: str
        self.expected: str
        self.argument: str
        self.matcher_func: Callable[..., Any]
    @property
    def explanation(self) -> str: ...

class Waiter:
    def __init__(
        self, name: str, config: Dict[str, Any], operation_method: Callable[..., Any]
    ) -> None:
        self.name: str
        self.config: Dict[str, Any]
    def wait(self, **kwargs: Any) -> None: ...
