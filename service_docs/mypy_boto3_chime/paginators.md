# Paginators for boto3 Chime module

> [Index](../index.md) > [Chime](./index.md) > Paginators

Auto-generated documentation for [Chime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime)
type annotations stubs module [mypy_boto3_chime](https://pypi.org/project/mypy-boto3-chime/).

- [Paginators for boto3 Chime module](#paginators-for-boto3-chime-module)
  - [ListAccountsPaginator](#listaccountspaginator)
  - [ListUsersPaginator](#listuserspaginator)

## ListAccountsPaginator

Type annotations for `boto3.client("chime").get_paginator("list_accounts")`.

Can be used directly:

```python
from mypy_boto3_chime.paginators import ListAccountsPaginator

def get_list_accounts_paginator() -> ListAccountsPaginator:
    return boto3.client("chime").get_paginator("list_accounts")
```

[Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Paginator.ListAccounts)

```python
class ListAccountsPaginator(Boto3Paginator):
    def paginate(
        self,
        Name: str = None,
        UserEmail: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountsResponseTypeDef]:
        pass
```
## ListUsersPaginator

Type annotations for `boto3.client("chime").get_paginator("list_users")`.

Can be used directly:

```python
from mypy_boto3_chime.paginators import ListUsersPaginator

def get_list_users_paginator() -> ListUsersPaginator:
    return boto3.client("chime").get_paginator("list_users")
```

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Paginator.ListUsers)

```python
class ListUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        UserEmail: str = None,
        UserType: UserType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        pass
```