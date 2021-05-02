# Paginators for boto3 MigrationHub module

> [Index](../index.md) > [MigrationHub](./index.md) > Paginators

Auto-generated documentation for [MigrationHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub)
type annotations stubs module [mypy_boto3_mgh](https://pypi.org/project/mypy-boto3-mgh/).

- [Paginators for boto3 MigrationHub module](#paginators-for-boto3-migrationhub-module)
  - [ListApplicationStatesPaginator](#listapplicationstatespaginator)
  - [ListCreatedArtifactsPaginator](#listcreatedartifactspaginator)
  - [ListDiscoveredResourcesPaginator](#listdiscoveredresourcespaginator)
  - [ListMigrationTasksPaginator](#listmigrationtaskspaginator)
  - [ListProgressUpdateStreamsPaginator](#listprogressupdatestreamspaginator)

## ListApplicationStatesPaginator

Type annotations for `boto3.client("mgh").get_paginator("list_application_states")`.

Can be used directly:

```python
from mypy_boto3_mgh.paginators import ListApplicationStatesPaginator

def get_list_application_states_paginator() -> ListApplicationStatesPaginator:
    return boto3.client("mgh").get_paginator("list_application_states")
```

[Paginator.ListApplicationStates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Paginator.ListApplicationStates)

```python
class ListApplicationStatesPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationStatesResultTypeDef]:
        pass
```
## ListCreatedArtifactsPaginator

Type annotations for `boto3.client("mgh").get_paginator("list_created_artifacts")`.

Can be used directly:

```python
from mypy_boto3_mgh.paginators import ListCreatedArtifactsPaginator

def get_list_created_artifacts_paginator() -> ListCreatedArtifactsPaginator:
    return boto3.client("mgh").get_paginator("list_created_artifacts")
```

[Paginator.ListCreatedArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)

```python
class ListCreatedArtifactsPaginator(Boto3Paginator):
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCreatedArtifactsResultTypeDef]:
        pass
```
## ListDiscoveredResourcesPaginator

Type annotations for `boto3.client("mgh").get_paginator("list_discovered_resources")`.

Can be used directly:

```python
from mypy_boto3_mgh.paginators import ListDiscoveredResourcesPaginator

def get_list_discovered_resources_paginator() -> ListDiscoveredResourcesPaginator:
    return boto3.client("mgh").get_paginator("list_discovered_resources")
```

[Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)

```python
class ListDiscoveredResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDiscoveredResourcesResultTypeDef]:
        pass
```
## ListMigrationTasksPaginator

Type annotations for `boto3.client("mgh").get_paginator("list_migration_tasks")`.

Can be used directly:

```python
from mypy_boto3_mgh.paginators import ListMigrationTasksPaginator

def get_list_migration_tasks_paginator() -> ListMigrationTasksPaginator:
    return boto3.client("mgh").get_paginator("list_migration_tasks")
```

[Paginator.ListMigrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)

```python
class ListMigrationTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMigrationTasksResultTypeDef]:
        pass
```
## ListProgressUpdateStreamsPaginator

Type annotations for `boto3.client("mgh").get_paginator("list_progress_update_streams")`.

Can be used directly:

```python
from mypy_boto3_mgh.paginators import ListProgressUpdateStreamsPaginator

def get_list_progress_update_streams_paginator() -> ListProgressUpdateStreamsPaginator:
    return boto3.client("mgh").get_paginator("list_progress_update_streams")
```

[Paginator.ListProgressUpdateStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)

```python
class ListProgressUpdateStreamsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProgressUpdateStreamsResultTypeDef]:
        pass
```