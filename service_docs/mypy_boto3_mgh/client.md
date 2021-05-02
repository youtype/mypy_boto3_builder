# MigrationHubClient for boto3 MigrationHub module

> [Index](../index.md) > [MigrationHub](./index.md) > MigrationHubClient

Auto-generated documentation for [MigrationHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub)
type annotations stubs module [mypy_boto3_mgh](https://pypi.org/project/mypy-boto3-mgh/).

- [MigrationHubClient for boto3 MigrationHub module](#migrationhubclient-for-boto3-migrationhub-module)
  - [MigrationHubClient](#migrationhubclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_created_artifact](#associate_created_artifact)
    - [associate_discovered_resource](#associate_discovered_resource)
    - [can_paginate](#can_paginate)
    - [create_progress_update_stream](#create_progress_update_stream)
    - [delete_progress_update_stream](#delete_progress_update_stream)
    - [describe_application_state](#describe_application_state)
    - [describe_migration_task](#describe_migration_task)
    - [disassociate_created_artifact](#disassociate_created_artifact)
    - [disassociate_discovered_resource](#disassociate_discovered_resource)
    - [generate_presigned_url](#generate_presigned_url)
    - [import_migration_task](#import_migration_task)
    - [list_application_states](#list_application_states)
    - [list_created_artifacts](#list_created_artifacts)
    - [list_discovered_resources](#list_discovered_resources)
    - [list_migration_tasks](#list_migration_tasks)
    - [list_progress_update_streams](#list_progress_update_streams)
    - [notify_application_state](#notify_application_state)
    - [notify_migration_task_state](#notify_migration_task_state)
    - [put_resource_attributes](#put_resource_attributes)
    - [get_paginator](#get_paginator)

## MigrationHubClient

Type annotations for `boto3.client("mgh")`

Can be used directly:

```python
from mypy_boto3_mgh.client import MigrationHubClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mgh.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.DryRunOperation`
- `Exceptions.HomeRegionNotSetException`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidInputException`
- `Exceptions.PolicyErrorException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnauthorizedOperation`


## Methods


### associate_created_artifact

Type annotations for `boto3.client("mgh").associate_created_artifact` method.

[Client.associate_created_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.associate_created_artifact)

```python
def associate_created_artifact(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    CreatedArtifact: "CreatedArtifactTypeDef",
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### associate_discovered_resource

Type annotations for `boto3.client("mgh").associate_discovered_resource` method.

[Client.associate_discovered_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.associate_discovered_resource)

```python
def associate_discovered_resource(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    DiscoveredResource: "DiscoveredResourceTypeDef",
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("mgh").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_progress_update_stream

Type annotations for `boto3.client("mgh").create_progress_update_stream` method.

[Client.create_progress_update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.create_progress_update_stream)

```python
def create_progress_update_stream(
    self,
    ProgressUpdateStreamName: str,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_progress_update_stream

Type annotations for `boto3.client("mgh").delete_progress_update_stream` method.

[Client.delete_progress_update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.delete_progress_update_stream)

```python
def delete_progress_update_stream(
    self,
    ProgressUpdateStreamName: str,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### describe_application_state

Type annotations for `boto3.client("mgh").describe_application_state` method.

[Client.describe_application_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.describe_application_state)

```python
def describe_application_state(
    self,
    ApplicationId: str
) -> DescribeApplicationStateResultTypeDef:
    pass
```

### describe_migration_task

Type annotations for `boto3.client("mgh").describe_migration_task` method.

[Client.describe_migration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.describe_migration_task)

```python
def describe_migration_task(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str
) -> DescribeMigrationTaskResultTypeDef:
    pass
```

### disassociate_created_artifact

Type annotations for `boto3.client("mgh").disassociate_created_artifact` method.

[Client.disassociate_created_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.disassociate_created_artifact)

```python
def disassociate_created_artifact(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    CreatedArtifactName: str,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### disassociate_discovered_resource

Type annotations for `boto3.client("mgh").disassociate_discovered_resource` method.

[Client.disassociate_discovered_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.disassociate_discovered_resource)

```python
def disassociate_discovered_resource(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    ConfigurationId: str,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mgh").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### import_migration_task

Type annotations for `boto3.client("mgh").import_migration_task` method.

[Client.import_migration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.import_migration_task)

```python
def import_migration_task(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### list_application_states

Type annotations for `boto3.client("mgh").list_application_states` method.

[Client.list_application_states documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.list_application_states)

```python
def list_application_states(
    self,
    ApplicationIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListApplicationStatesResultTypeDef:
    pass
```

### list_created_artifacts

Type annotations for `boto3.client("mgh").list_created_artifacts` method.

[Client.list_created_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.list_created_artifacts)

```python
def list_created_artifacts(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListCreatedArtifactsResultTypeDef:
    pass
```

### list_discovered_resources

Type annotations for `boto3.client("mgh").list_discovered_resources` method.

[Client.list_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.list_discovered_resources)

```python
def list_discovered_resources(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDiscoveredResourcesResultTypeDef:
    pass
```

### list_migration_tasks

Type annotations for `boto3.client("mgh").list_migration_tasks` method.

[Client.list_migration_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.list_migration_tasks)

```python
def list_migration_tasks(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    ResourceName: str = None
) -> ListMigrationTasksResultTypeDef:
    pass
```

### list_progress_update_streams

Type annotations for `boto3.client("mgh").list_progress_update_streams` method.

[Client.list_progress_update_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.list_progress_update_streams)

```python
def list_progress_update_streams(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProgressUpdateStreamsResultTypeDef:
    pass
```

### notify_application_state

Type annotations for `boto3.client("mgh").notify_application_state` method.

[Client.notify_application_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.notify_application_state)

```python
def notify_application_state(
    self,
    ApplicationId: str,
    Status: ApplicationStatus,
    UpdateDateTime: datetime = None,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### notify_migration_task_state

Type annotations for `boto3.client("mgh").notify_migration_task_state` method.

[Client.notify_migration_task_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.notify_migration_task_state)

```python
def notify_migration_task_state(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    Task: "TaskTypeDef",
    UpdateDateTime: datetime,
    NextUpdateSeconds: int,
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```

### put_resource_attributes

Type annotations for `boto3.client("mgh").put_resource_attributes` method.

[Client.put_resource_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub.Client.put_resource_attributes)

```python
def put_resource_attributes(
    self,
    ProgressUpdateStream: str,
    MigrationTaskName: str,
    ResourceAttributeList: List["ResourceAttributeTypeDef"],
    DryRun: bool = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("mgh").get_paginator` method with overloads.

- `client.get_paginator("list_application_states")` -> [ListApplicationStatesPaginator](./paginators.md#listapplicationstatespaginator)
- `client.get_paginator("list_created_artifacts")` -> [ListCreatedArtifactsPaginator](./paginators.md#listcreatedartifactspaginator)
- `client.get_paginator("list_discovered_resources")` -> [ListDiscoveredResourcesPaginator](./paginators.md#listdiscoveredresourcespaginator)
- `client.get_paginator("list_migration_tasks")` -> [ListMigrationTasksPaginator](./paginators.md#listmigrationtaskspaginator)
- `client.get_paginator("list_progress_update_streams")` -> [ListProgressUpdateStreamsPaginator](./paginators.md#listprogressupdatestreamspaginator)


