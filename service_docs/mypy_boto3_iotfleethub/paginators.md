# Paginators for boto3 IoTFleetHub module

> [Index](../index.md) > [IoTFleetHub](./index.md) > Paginators

Auto-generated documentation for [IoTFleetHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub)
type annotations stubs module [mypy_boto3_iotfleethub](https://pypi.org/project/mypy-boto3-iotfleethub/).

- [Paginators for boto3 IoTFleetHub module](#paginators-for-boto3-iotfleethub-module)
  - [ListApplicationsPaginator](#listapplicationspaginator)

## ListApplicationsPaginator

Type annotations for `boto3.client("iotfleethub").get_paginator("list_applications")`.

Can be used directly:

```python
from mypy_boto3_iotfleethub.paginators import ListApplicationsPaginator

def get_list_applications_paginator() -> ListApplicationsPaginator:
    return boto3.client("iotfleethub").get_paginator("list_applications")
```

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub.Paginator.ListApplications)

```python
class ListApplicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        pass
```