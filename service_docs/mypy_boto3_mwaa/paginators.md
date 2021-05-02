# Paginators for boto3 MWAA module

> [Index](../index.md) > [MWAA](./index.md) > Paginators

Auto-generated documentation for [MWAA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA)
type annotations stubs module [mypy_boto3_mwaa](https://pypi.org/project/mypy-boto3-mwaa/).

- [Paginators for boto3 MWAA module](#paginators-for-boto3-mwaa-module)
  - [ListEnvironmentsPaginator](#listenvironmentspaginator)

## ListEnvironmentsPaginator

Type annotations for `boto3.client("mwaa").get_paginator("list_environments")`.

Can be used directly:

```python
from mypy_boto3_mwaa.paginators import ListEnvironmentsPaginator

def get_list_environments_paginator() -> ListEnvironmentsPaginator:
    return boto3.client("mwaa").get_paginator("list_environments")
```

[Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments)

```python
class ListEnvironmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsOutputTypeDef]:
        pass
```