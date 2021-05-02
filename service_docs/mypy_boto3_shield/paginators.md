# Paginators for boto3 Shield module

> [Index](../index.md) > [Shield](./index.md) > Paginators

Auto-generated documentation for [Shield](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield)
type annotations stubs module [mypy_boto3_shield](https://pypi.org/project/mypy-boto3-shield/).

- [Paginators for boto3 Shield module](#paginators-for-boto3-shield-module)
  - [ListAttacksPaginator](#listattackspaginator)
  - [ListProtectionsPaginator](#listprotectionspaginator)

## ListAttacksPaginator

Type annotations for `boto3.client("shield").get_paginator("list_attacks")`.

Can be used directly:

```python
from mypy_boto3_shield.paginators import ListAttacksPaginator

def get_list_attacks_paginator() -> ListAttacksPaginator:
    return boto3.client("shield").get_paginator("list_attacks")
```

[Paginator.ListAttacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Paginator.ListAttacks)

```python
class ListAttacksPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceArns: List[str] = None,
        StartTime: "TimeRangeTypeDef" = None,
        EndTime: "TimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttacksResponseTypeDef]:
        pass
```
## ListProtectionsPaginator

Type annotations for `boto3.client("shield").get_paginator("list_protections")`.

Can be used directly:

```python
from mypy_boto3_shield.paginators import ListProtectionsPaginator

def get_list_protections_paginator() -> ListProtectionsPaginator:
    return boto3.client("shield").get_paginator("list_protections")
```

[Paginator.ListProtections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Paginator.ListProtections)

```python
class ListProtectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProtectionsResponseTypeDef]:
        pass
```