from logging import Logger
from typing import Any, Mapping, Optional

from botocore.endpoint_provider import RuleSetEndpoint
from botocore.model import OperationModel
from botocore.regions import EndpointRulesetResolver

LOG: Logger

class AioEndpointRulesetResolver(EndpointRulesetResolver):
    async def construct_endpoint(  # type: ignore [override]
        self,
        operation_model: OperationModel,
        call_args: Optional[Mapping[str, Any]],
        request_context: Optional[Mapping[str, Any]],
    ) -> RuleSetEndpoint: ...
