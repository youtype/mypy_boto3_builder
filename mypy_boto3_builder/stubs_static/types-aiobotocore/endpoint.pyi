"""
Type annotations for aiobotocore.endpoint module.

Copyright 2025 Vlad Emelianov
"""

from typing import Any, Mapping

from aiobotocore.httpsession import AIOHTTPSession as AIOHTTPSession
from aiobotocore.response import StreamingBody as StreamingBody
from botocore.endpoint import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from botocore.endpoint import MAX_POOL_CONNECTIONS as MAX_POOL_CONNECTIONS
from botocore.endpoint import Endpoint, EndpointCreator
from botocore.model import OperationModel, ServiceModel
from requests.models import Request, Response

DEFAULT_HTTP_SESSION_CLS: type[AIOHTTPSession] = ...

async def convert_to_response_dict(
    http_response: Response, operation_model: OperationModel
) -> dict[str, Any]: ...

class AioEndpoint(Endpoint):
    async def close(self) -> None: ...  # type: ignore[override]
    async def create_request(
        self, params: Mapping[str, Any], operation_model: OperationModel | None = ...
    ) -> Request: ...

class AioEndpointCreator(EndpointCreator):
    def create_endpoint(  # type: ignore[override]
        self,
        service_model: ServiceModel,
        region_name: str,
        endpoint_url: str,
        verify: str | bool | None = ...,
        response_parser_factory: Any | None = ...,
        timeout: int = ...,
        max_pool_connections: int = ...,
        http_session_cls: type[AIOHTTPSession] = ...,
        proxies: Any | None = ...,
        socket_options: Any | None = ...,
        client_cert: Any | None = ...,
        proxies_config: Any | None = ...,
        connector_args: Any | None = ...,
    ) -> AioEndpoint: ...
