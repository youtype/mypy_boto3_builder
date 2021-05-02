# ApiGatewayManagementApiClient for boto3 ApiGatewayManagementApi module

> [Index](../index.md) > [ApiGatewayManagementApi](./index.md) > ApiGatewayManagementApiClient

Auto-generated documentation for [ApiGatewayManagementApi](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi)
type annotations stubs module [mypy_boto3_apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/).

- [ApiGatewayManagementApiClient for boto3 ApiGatewayManagementApi module](#apigatewaymanagementapiclient-for-boto3-apigatewaymanagementapi-module)
  - [ApiGatewayManagementApiClient](#apigatewaymanagementapiclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_connection](#delete_connection)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_connection](#get_connection)
    - [post_to_connection](#post_to_connection)

## ApiGatewayManagementApiClient

Type annotations for `boto3.client("apigatewaymanagementapi")`

Can be used directly:

```python
from mypy_boto3_apigatewaymanagementapi.client import ApiGatewayManagementApiClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_apigatewaymanagementapi.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ForbiddenException`
- `Exceptions.GoneException`
- `Exceptions.LimitExceededException`
- `Exceptions.PayloadTooLargeException`


## Methods


### can_paginate

Type annotations for `boto3.client("apigatewaymanagementapi").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_connection

Type annotations for `boto3.client("apigatewaymanagementapi").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.delete_connection)

```python
def delete_connection(
    self,
    ConnectionId: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("apigatewaymanagementapi").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.generate_presigned_url)

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

### get_connection

Type annotations for `boto3.client("apigatewaymanagementapi").get_connection` method.

[Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.get_connection)

```python
def get_connection(
    self,
    ConnectionId: str
) -> GetConnectionResponseTypeDef:
    pass
```

### post_to_connection

Type annotations for `boto3.client("apigatewaymanagementapi").post_to_connection` method.

[Client.post_to_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.post_to_connection)

```python
def post_to_connection(
    self,
    Data: Union[bytes, IO[bytes]],
    ConnectionId: str
) -> None:
    pass
```



