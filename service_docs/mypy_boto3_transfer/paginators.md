# Paginators for boto3 Transfer module

> [Index](../index.md) > [Transfer](./index.md) > Paginators

Auto-generated documentation for [Transfer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer)
type annotations stubs module [mypy_boto3_transfer](https://pypi.org/project/mypy-boto3-transfer/).

- [Paginators for boto3 Transfer module](#paginators-for-boto3-transfer-module)
  - [ListServersPaginator](#listserverspaginator)

## ListServersPaginator

Type annotations for `boto3.client("transfer").get_paginator("list_servers")`.

Can be used directly:

```python
from mypy_boto3_transfer.paginators import ListServersPaginator

def get_list_servers_paginator() -> ListServersPaginator:
    return boto3.client("transfer").get_paginator("list_servers")
```

[Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Paginator.ListServers)

```python
class ListServersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServersResponseTypeDef]:
        pass
```