# Paginators for boto3 CognitoIdentity module

> [Index](../index.md) > [CognitoIdentity](./index.md) > Paginators

Auto-generated documentation for [CognitoIdentity](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity)
type annotations stubs module [mypy_boto3_cognito_identity](https://pypi.org/project/mypy-boto3-cognito-identity/).

- [Paginators for boto3 CognitoIdentity module](#paginators-for-boto3-cognitoidentity-module)
  - [ListIdentityPoolsPaginator](#listidentitypoolspaginator)

## ListIdentityPoolsPaginator

Type annotations for `boto3.client("cognito-identity").get_paginator("list_identity_pools")`.

Can be used directly:

```python
from mypy_boto3_cognito_identity.paginators import ListIdentityPoolsPaginator

def get_list_identity_pools_paginator() -> ListIdentityPoolsPaginator:
    return boto3.client("cognito-identity").get_paginator("list_identity_pools")
```

[Paginator.ListIdentityPools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools)

```python
class ListIdentityPoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityPoolsResponseTypeDef]:
        pass
```