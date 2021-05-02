# Paginators for boto3 Macie module

> [Index](../index.md) > [Macie](./index.md) > Paginators

Auto-generated documentation for [Macie](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie)
type annotations stubs module [mypy_boto3_macie](https://pypi.org/project/mypy-boto3-macie/).

- [Paginators for boto3 Macie module](#paginators-for-boto3-macie-module)
  - [ListMemberAccountsPaginator](#listmemberaccountspaginator)
  - [ListS3ResourcesPaginator](#lists3resourcespaginator)

## ListMemberAccountsPaginator

Type annotations for `boto3.client("macie").get_paginator("list_member_accounts")`.

Can be used directly:

```python
from mypy_boto3_macie.paginators import ListMemberAccountsPaginator

def get_list_member_accounts_paginator() -> ListMemberAccountsPaginator:
    return boto3.client("macie").get_paginator("list_member_accounts")
```

[Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)

```python
class ListMemberAccountsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMemberAccountsResultTypeDef]:
        pass
```
## ListS3ResourcesPaginator

Type annotations for `boto3.client("macie").get_paginator("list_s3_resources")`.

Can be used directly:

```python
from mypy_boto3_macie.paginators import ListS3ResourcesPaginator

def get_list_s3_resources_paginator() -> ListS3ResourcesPaginator:
    return boto3.client("macie").get_paginator("list_s3_resources")
```

[Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Paginator.ListS3Resources)

```python
class ListS3ResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        memberAccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListS3ResourcesResultTypeDef]:
        pass
```