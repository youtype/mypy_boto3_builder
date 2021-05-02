# Paginators for boto3 SimpleDB module

> [Index](../index.md) > [SimpleDB](./index.md) > Paginators

Auto-generated documentation for [SimpleDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB)
type annotations stubs module [mypy_boto3_sdb](https://pypi.org/project/mypy-boto3-sdb/).

- [Paginators for boto3 SimpleDB module](#paginators-for-boto3-simpledb-module)
  - [ListDomainsPaginator](#listdomainspaginator)
  - [SelectPaginator](#selectpaginator)

## ListDomainsPaginator

Type annotations for `boto3.client("sdb").get_paginator("list_domains")`.

Can be used directly:

```python
from mypy_boto3_sdb.paginators import ListDomainsPaginator

def get_list_domains_paginator() -> ListDomainsPaginator:
    return boto3.client("sdb").get_paginator("list_domains")
```

[Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB.Paginator.ListDomains)

```python
class ListDomainsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResultTypeDef]:
        pass
```
## SelectPaginator

Type annotations for `boto3.client("sdb").get_paginator("select")`.

Can be used directly:

```python
from mypy_boto3_sdb.paginators import SelectPaginator

def get_select_paginator() -> SelectPaginator:
    return boto3.client("sdb").get_paginator("select")
```

[Paginator.Select documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html#SimpleDB.Paginator.Select)

```python
class SelectPaginator(Boto3Paginator):
    def paginate(
        self,
        SelectExpression: str,
        ConsistentRead: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SelectResultTypeDef]:
        pass
```