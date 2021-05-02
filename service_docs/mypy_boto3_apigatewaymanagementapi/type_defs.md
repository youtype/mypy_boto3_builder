# Structures for boto3 ApiGatewayManagementApi module

> [Index](../index.md) > [ApiGatewayManagementApi](./index.md) > Structures

Auto-generated documentation for [ApiGatewayManagementApi](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi)
type annotations stubs module [mypy_boto3_apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/).

- [Structures for boto3 ApiGatewayManagementApi module](#structures-for-boto3-apigatewaymanagementapi-module)
  - [IdentityTypeDef](#identitytypedef)
  - [GetConnectionResponseTypeDef](#getconnectionresponsetypedef)

## IdentityTypeDef

```python
from mypy_boto3_apigatewaymanagementapi.type_defs import IdentityTypeDef
```


Required fields:
- `SourceIp`: `str`
- `UserAgent`: `str`




## GetConnectionResponseTypeDef

```python
from mypy_boto3_apigatewaymanagementapi.type_defs import GetConnectionResponseTypeDef
```




Optional fields:
- `ConnectedAt`: `datetime`
- `Identity`: `"IdentityTypeDef"`
- `LastActiveAt`: `datetime`

