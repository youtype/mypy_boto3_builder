# Paginators for boto3 Braket module

> [Index](../index.md) > [Braket](./index.md) > Paginators

Auto-generated documentation for [Braket](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket)
type annotations stubs module [mypy_boto3_braket](https://pypi.org/project/mypy-boto3-braket/).

- [Paginators for boto3 Braket module](#paginators-for-boto3-braket-module)
  - [SearchDevicesPaginator](#searchdevicespaginator)
  - [SearchQuantumTasksPaginator](#searchquantumtaskspaginator)

## SearchDevicesPaginator

Type annotations for `boto3.client("braket").get_paginator("search_devices")`.

Can be used directly:

```python
from mypy_boto3_braket.paginators import SearchDevicesPaginator

def get_search_devices_paginator() -> SearchDevicesPaginator:
    return boto3.client("braket").get_paginator("search_devices")
```

[Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Paginator.SearchDevices)

```python
class SearchDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        filters: List[SearchDevicesFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDevicesResponseTypeDef]:
        pass
```
## SearchQuantumTasksPaginator

Type annotations for `boto3.client("braket").get_paginator("search_quantum_tasks")`.

Can be used directly:

```python
from mypy_boto3_braket.paginators import SearchQuantumTasksPaginator

def get_search_quantum_tasks_paginator() -> SearchQuantumTasksPaginator:
    return boto3.client("braket").get_paginator("search_quantum_tasks")
```

[Paginator.SearchQuantumTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)

```python
class SearchQuantumTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        filters: List[SearchQuantumTasksFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchQuantumTasksResponseTypeDef]:
        pass
```