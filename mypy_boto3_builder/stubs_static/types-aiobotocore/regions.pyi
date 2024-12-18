"""
Type annotations for aiobotocore.regions module.

Copyright 2024 Vlad Emelianov
"""

from logging import Logger
from typing import Any, Mapping

from botocore.endpoint_provider import RuleSetEndpoint
from botocore.model import OperationModel
from botocore.regions import EndpointRulesetResolver

LOG: Logger

class AioEndpointRulesetResolver(EndpointRulesetResolver):
    async def construct_endpoint(  # type: ignore[override]
        self,
        operation_model: OperationModel,
        call_args: Mapping[str, Any] | None,
        request_context: Mapping[str, Any] | None,
    ) -> RuleSetEndpoint: ...
