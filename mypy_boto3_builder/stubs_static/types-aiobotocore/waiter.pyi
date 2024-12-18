"""
Type annotations for aiobotocore.waiter module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from botocore.client import BaseClient
from botocore.waiter import NormalizedOperationMethod as _NormalizedOperationMethod
from botocore.waiter import Waiter
from botocore.waiter import WaiterModel as WaiterModel

class NormalizedOperationMethod(_NormalizedOperationMethod):
    async def __call__(self, **kwargs: Any) -> Any: ...

class AIOWaiter(Waiter):
    async def wait(self, **kwargs: Any) -> None: ...  # type: ignore[override]

def create_waiter_with_client(
    waiter_name: str, waiter_model: WaiterModel, client: BaseClient
) -> AIOWaiter: ...
