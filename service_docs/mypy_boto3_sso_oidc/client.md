# SSOOIDCClient for boto3 SSOOIDC module

> [Index](../index.md) > [SSOOIDC](./index.md) > SSOOIDCClient

Auto-generated documentation for [SSOOIDC](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC)
type annotations stubs module [mypy_boto3_sso_oidc](https://pypi.org/project/mypy-boto3-sso-oidc/).

- [SSOOIDCClient for boto3 SSOOIDC module](#ssooidcclient-for-boto3-ssooidc-module)
  - [SSOOIDCClient](#ssooidcclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_token](#create_token)
    - [generate_presigned_url](#generate_presigned_url)
    - [register_client](#register_client)
    - [start_device_authorization](#start_device_authorization)

## SSOOIDCClient

Type annotations for `boto3.client("sso-oidc")`

Can be used directly:

```python
from mypy_boto3_sso_oidc.client import SSOOIDCClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sso_oidc.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AuthorizationPendingException`
- `Exceptions.ClientError`
- `Exceptions.ExpiredTokenException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidClientException`
- `Exceptions.InvalidClientMetadataException`
- `Exceptions.InvalidGrantException`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidScopeException`
- `Exceptions.SlowDownException`
- `Exceptions.UnauthorizedClientException`
- `Exceptions.UnsupportedGrantTypeException`


## Methods


### can_paginate

Type annotations for `boto3.client("sso-oidc").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_token

Type annotations for `boto3.client("sso-oidc").create_token` method.

[Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client.create_token)

```python
def create_token(
    self,
    clientId: str,
    clientSecret: str,
    grantType: str,
    deviceCode: str,
    code: str = None,
    refreshToken: str = None,
    scope: List[str] = None,
    redirectUri: str = None
) -> CreateTokenResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sso-oidc").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### register_client

Type annotations for `boto3.client("sso-oidc").register_client` method.

[Client.register_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client.register_client)

```python
def register_client(
    self,
    clientName: str,
    clientType: str,
    scopes: List[str] = None
) -> RegisterClientResponseTypeDef:
    pass
```

### start_device_authorization

Type annotations for `boto3.client("sso-oidc").start_device_authorization` method.

[Client.start_device_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client.start_device_authorization)

```python
def start_device_authorization(
    self,
    clientId: str,
    clientSecret: str,
    startUrl: str
) -> StartDeviceAuthorizationResponseTypeDef:
    pass
```