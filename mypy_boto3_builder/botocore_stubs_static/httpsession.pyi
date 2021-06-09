from typing import Any, Optional

from botocore.compat import filter_ssl_warnings as filter_ssl_warnings
from botocore.compat import urlparse as urlparse
from botocore.exceptions import ConnectionClosedError as ConnectionClosedError
from botocore.exceptions import ConnectTimeoutError as ConnectTimeoutError
from botocore.exceptions import EndpointConnectionError as EndpointConnectionError
from botocore.exceptions import HTTPClientError as HTTPClientError
from botocore.exceptions import InvalidProxiesConfigError as InvalidProxiesConfigError
from botocore.exceptions import ProxyConnectionError as ProxyConnectionError
from botocore.exceptions import ReadTimeoutError as ReadTimeoutError
from botocore.exceptions import SSLError as SSLError
from requests.packages.urllib3 import ProxyManager as ProxyManager

DEFAULT_TIMEOUT: int
MAX_POOL_CONNECTIONS: int
DEFAULT_CA_BUNDLE: Any

def get_cert_path(verify: Any) -> Any: ...
def create_urllib3_context(
    ssl_version: Optional[Any] = ...,
    cert_reqs: Optional[Any] = ...,
    options: Optional[Any] = ...,
    ciphers: Optional[Any] = ...,
) -> Any: ...

class ProxyConfiguration:
    def __init__(
        self, proxies: Optional[Any] = ..., proxies_settings: Optional[Any] = ...
    ) -> None: ...
    def proxy_url_for(self, url: Any) -> Any: ...
    def proxy_headers_for(self, proxy_url: Any) -> Any: ...
    @property
    def settings(self) -> Any: ...

class URLLib3Session:
    def __init__(
        self,
        verify: bool = ...,
        proxies: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        max_pool_connections: Any = ...,
        socket_options: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        proxies_config: Optional[Any] = ...,
    ) -> None: ...
    def send(self, request: Any) -> Any: ...
