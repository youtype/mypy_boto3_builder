# Paginators for boto3 SSO module

> [Index](../index.md) > [SSO](./index.md) > Paginators

Auto-generated documentation for [SSO](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO)
type annotations stubs module [mypy_boto3_sso](https://pypi.org/project/mypy-boto3-sso/).

- [Paginators for boto3 SSO module](#paginators-for-boto3-sso-module)
  - [ListAccountRolesPaginator](#listaccountrolespaginator)
  - [ListAccountsPaginator](#listaccountspaginator)

## ListAccountRolesPaginator

Type annotations for `boto3.client("sso").get_paginator("list_account_roles")`.

Can be used directly:

```python
from mypy_boto3_sso.paginators import ListAccountRolesPaginator

def get_list_account_roles_paginator() -> ListAccountRolesPaginator:
    return boto3.client("sso").get_paginator("list_account_roles")
```

[Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Paginator.ListAccountRoles)

```python
class ListAccountRolesPaginator(Boto3Paginator):
    def paginate(
        self,
        accessToken: str,
        accountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountRolesResponseTypeDef]:
        pass
```
## ListAccountsPaginator

Type annotations for `boto3.client("sso").get_paginator("list_accounts")`.

Can be used directly:

```python
from mypy_boto3_sso.paginators import ListAccountsPaginator

def get_list_accounts_paginator() -> ListAccountsPaginator:
    return boto3.client("sso").get_paginator("list_accounts")
```

[Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Paginator.ListAccounts)

```python
class ListAccountsPaginator(Boto3Paginator):
    def paginate(
        self,
        accessToken: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        pass
```