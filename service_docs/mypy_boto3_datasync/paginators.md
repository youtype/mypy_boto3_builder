# Paginators for boto3 DataSync module

> [Index](../index.md) > [DataSync](./index.md) > Paginators

Auto-generated documentation for [DataSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync)
type annotations stubs module [mypy_boto3_datasync](https://pypi.org/project/mypy-boto3-datasync/).

- [Paginators for boto3 DataSync module](#paginators-for-boto3-datasync-module)
  - [ListAgentsPaginator](#listagentspaginator)
  - [ListLocationsPaginator](#listlocationspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [ListTaskExecutionsPaginator](#listtaskexecutionspaginator)
  - [ListTasksPaginator](#listtaskspaginator)

## ListAgentsPaginator

Type annotations for `boto3.client("datasync").get_paginator("list_agents")`.

Can be used directly:

```python
from mypy_boto3_datasync.paginators import ListAgentsPaginator

def get_list_agents_paginator() -> ListAgentsPaginator:
    return boto3.client("datasync").get_paginator("list_agents")
```

[Paginator.ListAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListAgents)

```python
class ListAgentsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentsResponseTypeDef]:
        pass
```
## ListLocationsPaginator

Type annotations for `boto3.client("datasync").get_paginator("list_locations")`.

Can be used directly:

```python
from mypy_boto3_datasync.paginators import ListLocationsPaginator

def get_list_locations_paginator() -> ListLocationsPaginator:
    return boto3.client("datasync").get_paginator("list_locations")
```

[Paginator.ListLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListLocations)

```python
class ListLocationsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[LocationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLocationsResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("datasync").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_datasync.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("datasync").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```
## ListTaskExecutionsPaginator

Type annotations for `boto3.client("datasync").get_paginator("list_task_executions")`.

Can be used directly:

```python
from mypy_boto3_datasync.paginators import ListTaskExecutionsPaginator

def get_list_task_executions_paginator() -> ListTaskExecutionsPaginator:
    return boto3.client("datasync").get_paginator("list_task_executions")
```

[Paginator.ListTaskExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)

```python
class ListTaskExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        TaskArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTaskExecutionsResponseTypeDef]:
        pass
```
## ListTasksPaginator

Type annotations for `boto3.client("datasync").get_paginator("list_tasks")`.

Can be used directly:

```python
from mypy_boto3_datasync.paginators import ListTasksPaginator

def get_list_tasks_paginator() -> ListTasksPaginator:
    return boto3.client("datasync").get_paginator("list_tasks")
```

[Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListTasks)

```python
class ListTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[TaskFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTasksResponseTypeDef]:
        pass
```