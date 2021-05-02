# SSOClient for boto3 SSO module

> [Index](../index.md) > [SSO](./index.md) > SSOClient

Auto-generated documentation for [SSO](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO)
type annotations stubs module [mypy_boto3_sso](https://pypi.org/project/mypy-boto3-sso/).

- [SSOClient for boto3 SSO module](#ssoclient-for-boto3-sso-module)
  - [SSOClient](#ssoclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_role_credentials](#get_role_credentials)
    - [list_account_roles](#list_account_roles)
    - [list_accounts](#list_accounts)
    - [logout](#logout)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)

## SSOClient

Type annotations for `boto3.client("sso")`

Can be used directly:

```python
from mypy_boto3_sso.client import SSOClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sso.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("sso").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sso").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client.generate_presigned_url)

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

### get_role_credentials

Type annotations for `boto3.client("sso").get_role_credentials` method.

[Client.get_role_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client.get_role_credentials)

```python
def get_role_credentials(
    self,
    roleName: str,
    accountId: str,
    accessToken: str
) -> GetRoleCredentialsResponseTypeDef:
    pass
```

### list_account_roles

Type annotations for `boto3.client("sso").list_account_roles` method.

[Client.list_account_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client.list_account_roles)

```python
def list_account_roles(
    self,
    accessToken: str,
    accountId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListAccountRolesResponseTypeDef:
    pass
```

### list_accounts

Type annotations for `boto3.client("sso").list_accounts` method.

[Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client.list_accounts)

```python
def list_accounts(
    self,
    accessToken: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListAccountsResponseTypeDef:
    pass
```

### logout

Type annotations for `boto3.client("sso").logout` method.

[Client.logout documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client.logout)

```python
def logout(
    self,
    accessToken: str
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("sso").get_paginator` method.

[Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Paginator.ListAccountRoles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccountRolesPaginatorName
) -> ListAccountRolesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("sso").get_paginator` method.

[Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Paginator.ListAccounts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccountsPaginatorName
) -> ListAccountsPaginator:
    pass
```