from typing import Any, Dict, Optional, Type

from aiobotocore.httpsession import AIOHTTPSession as AIOHTTPSession
from aiobotocore.response import StreamingBody as StreamingBody
from botocore.endpoint import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from botocore.endpoint import MAX_POOL_CONNECTIONS as MAX_POOL_CONNECTIONS
from botocore.endpoint import Endpoint, EndpointCreator
from botocore.model import OperationModel, ServiceModel
from requests.models import Request, Response

async def convert_to_response_dict(
    http_response: Response, operation_model: OperationModel
) -> Dict[str, Any]: ...

class AioEndpoint(Endpoint):
    async def create_request(
        self, params: Any, operation_model: Optional[Any] = ...
    ) -> Request: ...

class AioEndpointCreator(EndpointCreator):
    def create_endpoint(  # type: ignore [override]
        self,
        service_model: ServiceModel,
        region_name: str,
        endpoint_url: str,
        verify: Optional[Any] = ...,
        response_parser_factory: Optional[Any] = ...,
        timeout: int = ...,
        max_pool_connections: int = ...,
        http_session_cls: Type[AIOHTTPSession] = ...,
        proxies: Optional[Any] = ...,
        socket_options: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        proxies_config: Optional[Any] = ...,
        connector_args: Optional[Any] = ...,
    ) -> AioEndpoint: ...
