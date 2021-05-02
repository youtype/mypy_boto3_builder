# DataSyncClient for boto3 DataSync module

> [Index](../index.md) > [DataSync](./index.md) > DataSyncClient

Auto-generated documentation for [DataSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync)
type annotations stubs module [mypy_boto3_datasync](https://pypi.org/project/mypy-boto3-datasync/).

- [DataSyncClient for boto3 DataSync module](#datasyncclient-for-boto3-datasync-module)
  - [DataSyncClient](#datasyncclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_task_execution](#cancel_task_execution)
    - [create_agent](#create_agent)
    - [create_location_efs](#create_location_efs)
    - [create_location_fsx_windows](#create_location_fsx_windows)
    - [create_location_nfs](#create_location_nfs)
    - [create_location_object_storage](#create_location_object_storage)
    - [create_location_s3](#create_location_s3)
    - [create_location_smb](#create_location_smb)
    - [create_task](#create_task)
    - [delete_agent](#delete_agent)
    - [delete_location](#delete_location)
    - [delete_task](#delete_task)
    - [describe_agent](#describe_agent)
    - [describe_location_efs](#describe_location_efs)
    - [describe_location_fsx_windows](#describe_location_fsx_windows)
    - [describe_location_nfs](#describe_location_nfs)
    - [describe_location_object_storage](#describe_location_object_storage)
    - [describe_location_s3](#describe_location_s3)
    - [describe_location_smb](#describe_location_smb)
    - [describe_task](#describe_task)
    - [describe_task_execution](#describe_task_execution)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_agents](#list_agents)
    - [list_locations](#list_locations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_task_executions](#list_task_executions)
    - [list_tasks](#list_tasks)
    - [start_task_execution](#start_task_execution)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_agent](#update_agent)
    - [update_location_nfs](#update_location_nfs)
    - [update_location_object_storage](#update_location_object_storage)
    - [update_location_smb](#update_location_smb)
    - [update_task](#update_task)
    - [update_task_execution](#update_task_execution)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)

## DataSyncClient

Type annotations for `boto3.client("datasync")`

Can be used directly:

```python
from mypy_boto3_datasync.client import DataSyncClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_datasync.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalException`
- `Exceptions.InvalidRequestException`


## Methods


### can_paginate

Type annotations for `boto3.client("datasync").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_task_execution

Type annotations for `boto3.client("datasync").cancel_task_execution` method.

[Client.cancel_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.cancel_task_execution)

```python
def cancel_task_execution(
    self,
    TaskExecutionArn: str
) -> Dict[str, Any]:
    pass
```

### create_agent

Type annotations for `boto3.client("datasync").create_agent` method.

[Client.create_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_agent)

```python
def create_agent(
    self,
    ActivationKey: str,
    AgentName: str = None,
    Tags: List["TagListEntryTypeDef"] = None,
    VpcEndpointId: str = None,
    SubnetArns: List[str] = None,
    SecurityGroupArns: List[str] = None
) -> CreateAgentResponseTypeDef:
    pass
```

### create_location_efs

Type annotations for `boto3.client("datasync").create_location_efs` method.

[Client.create_location_efs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_location_efs)

```python
def create_location_efs(
    self,
    EfsFilesystemArn: str,
    Ec2Config: "Ec2ConfigTypeDef",
    Subdirectory: str = None,
    Tags: List["TagListEntryTypeDef"] = None
) -> CreateLocationEfsResponseTypeDef:
    pass
```

### create_location_fsx_windows

Type annotations for `boto3.client("datasync").create_location_fsx_windows` method.

[Client.create_location_fsx_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_location_fsx_windows)

```python
def create_location_fsx_windows(
    self,
    FsxFilesystemArn: str,
    SecurityGroupArns: List[str],
    User: str,
    Password: str,
    Subdirectory: str = None,
    Tags: List["TagListEntryTypeDef"] = None,
    Domain: str = None
) -> CreateLocationFsxWindowsResponseTypeDef:
    pass
```

### create_location_nfs

Type annotations for `boto3.client("datasync").create_location_nfs` method.

[Client.create_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_location_nfs)

```python
def create_location_nfs(
    self,
    Subdirectory: str,
    ServerHostname: str,
    OnPremConfig: "OnPremConfigTypeDef",
    MountOptions: "NfsMountOptionsTypeDef" = None,
    Tags: List["TagListEntryTypeDef"] = None
) -> CreateLocationNfsResponseTypeDef:
    pass
```

### create_location_object_storage

Type annotations for `boto3.client("datasync").create_location_object_storage` method.

[Client.create_location_object_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_location_object_storage)

```python
def create_location_object_storage(
    self,
    ServerHostname: str,
    BucketName: str,
    AgentArns: List[str],
    ServerPort: int = None,
    ServerProtocol: ObjectStorageServerProtocol = None,
    Subdirectory: str = None,
    AccessKey: str = None,
    SecretKey: str = None,
    Tags: List["TagListEntryTypeDef"] = None
) -> CreateLocationObjectStorageResponseTypeDef:
    pass
```

### create_location_s3

Type annotations for `boto3.client("datasync").create_location_s3` method.

[Client.create_location_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_location_s3)

```python
def create_location_s3(
    self,
    S3BucketArn: str,
    S3Config: "S3ConfigTypeDef",
    Subdirectory: str = None,
    S3StorageClass: S3StorageClass = None,
    AgentArns: List[str] = None,
    Tags: List["TagListEntryTypeDef"] = None
) -> CreateLocationS3ResponseTypeDef:
    pass
```

### create_location_smb

Type annotations for `boto3.client("datasync").create_location_smb` method.

[Client.create_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_location_smb)

```python
def create_location_smb(
    self,
    Subdirectory: str,
    ServerHostname: str,
    User: str,
    Password: str,
    AgentArns: List[str],
    Domain: str = None,
    MountOptions: "SmbMountOptionsTypeDef" = None,
    Tags: List["TagListEntryTypeDef"] = None
) -> CreateLocationSmbResponseTypeDef:
    pass
```

### create_task

Type annotations for `boto3.client("datasync").create_task` method.

[Client.create_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.create_task)

```python
def create_task(
    self,
    SourceLocationArn: str,
    DestinationLocationArn: str,
    CloudWatchLogGroupArn: str = None,
    Name: str = None,
    Options: "OptionsTypeDef" = None,
    Excludes: List["FilterRuleTypeDef"] = None,
    Schedule: "TaskScheduleTypeDef" = None,
    Tags: List["TagListEntryTypeDef"] = None
) -> CreateTaskResponseTypeDef:
    pass
```

### delete_agent

Type annotations for `boto3.client("datasync").delete_agent` method.

[Client.delete_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.delete_agent)

```python
def delete_agent(
    self,
    AgentArn: str
) -> Dict[str, Any]:
    pass
```

### delete_location

Type annotations for `boto3.client("datasync").delete_location` method.

[Client.delete_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.delete_location)

```python
def delete_location(
    self,
    LocationArn: str
) -> Dict[str, Any]:
    pass
```

### delete_task

Type annotations for `boto3.client("datasync").delete_task` method.

[Client.delete_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.delete_task)

```python
def delete_task(
    self,
    TaskArn: str
) -> Dict[str, Any]:
    pass
```

### describe_agent

Type annotations for `boto3.client("datasync").describe_agent` method.

[Client.describe_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_agent)

```python
def describe_agent(
    self,
    AgentArn: str
) -> DescribeAgentResponseTypeDef:
    pass
```

### describe_location_efs

Type annotations for `boto3.client("datasync").describe_location_efs` method.

[Client.describe_location_efs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_location_efs)

```python
def describe_location_efs(
    self,
    LocationArn: str
) -> DescribeLocationEfsResponseTypeDef:
    pass
```

### describe_location_fsx_windows

Type annotations for `boto3.client("datasync").describe_location_fsx_windows` method.

[Client.describe_location_fsx_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_location_fsx_windows)

```python
def describe_location_fsx_windows(
    self,
    LocationArn: str
) -> DescribeLocationFsxWindowsResponseTypeDef:
    pass
```

### describe_location_nfs

Type annotations for `boto3.client("datasync").describe_location_nfs` method.

[Client.describe_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_location_nfs)

```python
def describe_location_nfs(
    self,
    LocationArn: str
) -> DescribeLocationNfsResponseTypeDef:
    pass
```

### describe_location_object_storage

Type annotations for `boto3.client("datasync").describe_location_object_storage` method.

[Client.describe_location_object_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_location_object_storage)

```python
def describe_location_object_storage(
    self,
    LocationArn: str
) -> DescribeLocationObjectStorageResponseTypeDef:
    pass
```

### describe_location_s3

Type annotations for `boto3.client("datasync").describe_location_s3` method.

[Client.describe_location_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_location_s3)

```python
def describe_location_s3(
    self,
    LocationArn: str
) -> DescribeLocationS3ResponseTypeDef:
    pass
```

### describe_location_smb

Type annotations for `boto3.client("datasync").describe_location_smb` method.

[Client.describe_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_location_smb)

```python
def describe_location_smb(
    self,
    LocationArn: str
) -> DescribeLocationSmbResponseTypeDef:
    pass
```

### describe_task

Type annotations for `boto3.client("datasync").describe_task` method.

[Client.describe_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_task)

```python
def describe_task(
    self,
    TaskArn: str
) -> DescribeTaskResponseTypeDef:
    pass
```

### describe_task_execution

Type annotations for `boto3.client("datasync").describe_task_execution` method.

[Client.describe_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.describe_task_execution)

```python
def describe_task_execution(
    self,
    TaskExecutionArn: str
) -> DescribeTaskExecutionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("datasync").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.generate_presigned_url)

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

### list_agents

Type annotations for `boto3.client("datasync").list_agents` method.

[Client.list_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.list_agents)

```python
def list_agents(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAgentsResponseTypeDef:
    pass
```

### list_locations

Type annotations for `boto3.client("datasync").list_locations` method.

[Client.list_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.list_locations)

```python
def list_locations(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[LocationFilterTypeDef] = None
) -> ListLocationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("datasync").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_task_executions

Type annotations for `boto3.client("datasync").list_task_executions` method.

[Client.list_task_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.list_task_executions)

```python
def list_task_executions(
    self,
    TaskArn: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTaskExecutionsResponseTypeDef:
    pass
```

### list_tasks

Type annotations for `boto3.client("datasync").list_tasks` method.

[Client.list_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.list_tasks)

```python
def list_tasks(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[TaskFilterTypeDef] = None
) -> ListTasksResponseTypeDef:
    pass
```

### start_task_execution

Type annotations for `boto3.client("datasync").start_task_execution` method.

[Client.start_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.start_task_execution)

```python
def start_task_execution(
    self,
    TaskArn: str,
    OverrideOptions: "OptionsTypeDef" = None,
    Includes: List["FilterRuleTypeDef"] = None
) -> StartTaskExecutionResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("datasync").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagListEntryTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("datasync").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    Keys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_agent

Type annotations for `boto3.client("datasync").update_agent` method.

[Client.update_agent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.update_agent)

```python
def update_agent(
    self,
    AgentArn: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_location_nfs

Type annotations for `boto3.client("datasync").update_location_nfs` method.

[Client.update_location_nfs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.update_location_nfs)

```python
def update_location_nfs(
    self,
    LocationArn: str,
    Subdirectory: str = None,
    OnPremConfig: "OnPremConfigTypeDef" = None,
    MountOptions: "NfsMountOptionsTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_location_object_storage

Type annotations for `boto3.client("datasync").update_location_object_storage` method.

[Client.update_location_object_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.update_location_object_storage)

```python
def update_location_object_storage(
    self,
    LocationArn: str,
    ServerPort: int = None,
    ServerProtocol: ObjectStorageServerProtocol = None,
    Subdirectory: str = None,
    AccessKey: str = None,
    SecretKey: str = None,
    AgentArns: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_location_smb

Type annotations for `boto3.client("datasync").update_location_smb` method.

[Client.update_location_smb documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.update_location_smb)

```python
def update_location_smb(
    self,
    LocationArn: str,
    Subdirectory: str = None,
    User: str = None,
    Domain: str = None,
    Password: str = None,
    AgentArns: List[str] = None,
    MountOptions: "SmbMountOptionsTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_task

Type annotations for `boto3.client("datasync").update_task` method.

[Client.update_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.update_task)

```python
def update_task(
    self,
    TaskArn: str,
    Options: "OptionsTypeDef" = None,
    Excludes: List["FilterRuleTypeDef"] = None,
    Schedule: "TaskScheduleTypeDef" = None,
    Name: str = None,
    CloudWatchLogGroupArn: str = None
) -> Dict[str, Any]:
    pass
```

### update_task_execution

Type annotations for `boto3.client("datasync").update_task_execution` method.

[Client.update_task_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Client.update_task_execution)

```python
def update_task_execution(
    self,
    TaskExecutionArn: str,
    Options: "OptionsTypeDef"
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("datasync").get_paginator` method.

[Paginator.ListAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListAgents)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAgentsPaginatorName
) -> ListAgentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("datasync").get_paginator` method.

[Paginator.ListLocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListLocations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListLocationsPaginatorName
) -> ListLocationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("datasync").get_paginator` method.

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListTagsForResource)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsForResourcePaginatorName
) -> ListTagsForResourcePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("datasync").get_paginator` method.

[Paginator.ListTaskExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListTaskExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTaskExecutionsPaginatorName
) -> ListTaskExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("datasync").get_paginator` method.

[Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync.Paginator.ListTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTasksPaginatorName
) -> ListTasksPaginator:
    pass
```