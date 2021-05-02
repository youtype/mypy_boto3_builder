# Paginators for boto3 PrometheusService module

> [Index](../index.md) > [PrometheusService](./index.md) > Paginators

Auto-generated documentation for [PrometheusService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService)
type annotations stubs module [mypy_boto3_amp](https://pypi.org/project/mypy-boto3-amp/).

- [Paginators for boto3 PrometheusService module](#paginators-for-boto3-prometheusservice-module)
  - [ListWorkspacesPaginator](#listworkspacespaginator)

## ListWorkspacesPaginator

Type annotations for `boto3.client("amp").get_paginator("list_workspaces")`.

Can be used directly:

```python
from mypy_boto3_amp.paginators import ListWorkspacesPaginator

def get_list_workspaces_paginator() -> ListWorkspacesPaginator:
    return boto3.client("amp").get_paginator("list_workspaces")
```

[Paginator.ListWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)

```python
class ListWorkspacesPaginator(Boto3Paginator):
    def paginate(
        self,
        alias: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkspacesResponseTypeDef]:
        pass
```