# Type annotations for boto3 ApiGatewayManagementApi module

> [Index](../index.md) > ApiGatewayManagementApi

Auto-generated documentation for [ApiGatewayManagementApi](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi)
type annotations stubs module [mypy_boto3_apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/).

```bash
pip install mypy-boto3-apigatewaymanagementapi
```

- [Type annotations for boto3 ApiGatewayManagementApi module](#type-annotations-for-boto3-apigatewaymanagementapi-module)
  - [ApiGatewayManagementApiClient](#apigatewaymanagementapiclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## ApiGatewayManagementApiClient

Type annotations for  `boto3.client("apigatewaymanagementapi")` as [ApiGatewayManagementApiClient](./client.md)

Can be used directly:

```python
from mypy_boto3_apigatewaymanagementapi.client import ApiGatewayManagementApiClient
```


ApiGatewayManagementApiClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_connection](./client.md#delete-connection)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_connection](./client.md#get-connection)
- [post_to_connection](./client.md#post-to-connection)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ForbiddenException](./client.md#forbiddenexception)
- [GoneException](./client.md#goneexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [PayloadTooLargeException](./client.md#payloadtoolargeexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_apigatewaymanagementapi.type_defs import GetConnectionResponseTypeDef, ...
```

- [GetConnectionResponseTypeDef](./type_defs.md#getconnectionresponsetypedef)
- [IdentityTypeDef](./type_defs.md#identitytypedef)
