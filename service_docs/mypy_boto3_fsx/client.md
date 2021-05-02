# FSxClient for boto3 FSx module

> [Index](../index.md) > [FSx](./index.md) > FSxClient

Auto-generated documentation for [FSx](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx)
type annotations stubs module [mypy_boto3_fsx](https://pypi.org/project/mypy-boto3-fsx/).

- [FSxClient for boto3 FSx module](#fsxclient-for-boto3-fsx-module)
  - [FSxClient](#fsxclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_file_system_aliases](#associate_file_system_aliases)
    - [can_paginate](#can_paginate)
    - [cancel_data_repository_task](#cancel_data_repository_task)
    - [copy_backup](#copy_backup)
    - [create_backup](#create_backup)
    - [create_data_repository_task](#create_data_repository_task)
    - [create_file_system](#create_file_system)
    - [create_file_system_from_backup](#create_file_system_from_backup)
    - [delete_backup](#delete_backup)
    - [delete_file_system](#delete_file_system)
    - [describe_backups](#describe_backups)
    - [describe_data_repository_tasks](#describe_data_repository_tasks)
    - [describe_file_system_aliases](#describe_file_system_aliases)
    - [describe_file_systems](#describe_file_systems)
    - [disassociate_file_system_aliases](#disassociate_file_system_aliases)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_file_system](#update_file_system)
    - [get_paginator](#get_paginator)

## FSxClient

Type annotations for `boto3.client("fsx")`

Can be used directly:

```python
from mypy_boto3_fsx.client import FSxClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_fsx.client import Exceptions

def handle_error(exc: Exceptions.ActiveDirectoryError) -> None:
    ...
```


Exceptions:

- `Exceptions.ActiveDirectoryError`
- `Exceptions.BackupBeingCopied`
- `Exceptions.BackupInProgress`
- `Exceptions.BackupNotFound`
- `Exceptions.BackupRestoring`
- `Exceptions.BadRequest`
- `Exceptions.ClientError`
- `Exceptions.DataRepositoryTaskEnded`
- `Exceptions.DataRepositoryTaskExecuting`
- `Exceptions.DataRepositoryTaskNotFound`
- `Exceptions.FileSystemNotFound`
- `Exceptions.IncompatibleParameterError`
- `Exceptions.IncompatibleRegionForMultiAZ`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidDestinationKmsKey`
- `Exceptions.InvalidExportPath`
- `Exceptions.InvalidImportPath`
- `Exceptions.InvalidNetworkSettings`
- `Exceptions.InvalidPerUnitStorageThroughput`
- `Exceptions.InvalidRegion`
- `Exceptions.InvalidSourceKmsKey`
- `Exceptions.MissingFileSystemConfiguration`
- `Exceptions.NotServiceResourceError`
- `Exceptions.ResourceDoesNotSupportTagging`
- `Exceptions.ResourceNotFound`
- `Exceptions.ServiceLimitExceeded`
- `Exceptions.SourceBackupUnavailable`
- `Exceptions.UnsupportedOperation`


## Methods


### associate_file_system_aliases

Type annotations for `boto3.client("fsx").associate_file_system_aliases` method.

[Client.associate_file_system_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.associate_file_system_aliases)

```python
def associate_file_system_aliases(
    self,
    FileSystemId: str,
    Aliases: List[str],
    ClientRequestToken: str = None
) -> AssociateFileSystemAliasesResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("fsx").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_data_repository_task

Type annotations for `boto3.client("fsx").cancel_data_repository_task` method.

[Client.cancel_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)

```python
def cancel_data_repository_task(
    self,
    TaskId: str
) -> CancelDataRepositoryTaskResponseTypeDef:
    pass
```

### copy_backup

Type annotations for `boto3.client("fsx").copy_backup` method.

[Client.copy_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.copy_backup)

```python
def copy_backup(
    self,
    SourceBackupId: str,
    ClientRequestToken: str = None,
    SourceRegion: str = None,
    KmsKeyId: str = None,
    CopyTags: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CopyBackupResponseTypeDef:
    pass
```

### create_backup

Type annotations for `boto3.client("fsx").create_backup` method.

[Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.create_backup)

```python
def create_backup(
    self,
    FileSystemId: str,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateBackupResponseTypeDef:
    pass
```

### create_data_repository_task

Type annotations for `boto3.client("fsx").create_data_repository_task` method.

[Client.create_data_repository_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.create_data_repository_task)

```python
def create_data_repository_task(
    self,
    Type: Literal['EXPORT_TO_REPOSITORY'],
    FileSystemId: str,
    Report: "CompletionReportTypeDef",
    Paths: List[str] = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDataRepositoryTaskResponseTypeDef:
    pass
```

### create_file_system

Type annotations for `boto3.client("fsx").create_file_system` method.

[Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.create_file_system)

```python
def create_file_system(
    self,
    FileSystemType: FileSystemType,
    StorageCapacity: int,
    SubnetIds: List[str],
    ClientRequestToken: str = None,
    StorageType: StorageType = None,
    SecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None,
    WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
    LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None
) -> CreateFileSystemResponseTypeDef:
    pass
```

### create_file_system_from_backup

Type annotations for `boto3.client("fsx").create_file_system_from_backup` method.

[Client.create_file_system_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)

```python
def create_file_system_from_backup(
    self,
    BackupId: str,
    SubnetIds: List[str],
    ClientRequestToken: str = None,
    SecurityGroupIds: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
    LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None,
    StorageType: StorageType = None,
    KmsKeyId: str = None
) -> CreateFileSystemFromBackupResponseTypeDef:
    pass
```

### delete_backup

Type annotations for `boto3.client("fsx").delete_backup` method.

[Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.delete_backup)

```python
def delete_backup(
    self,
    BackupId: str,
    ClientRequestToken: str = None
) -> DeleteBackupResponseTypeDef:
    pass
```

### delete_file_system

Type annotations for `boto3.client("fsx").delete_file_system` method.

[Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.delete_file_system)

```python
def delete_file_system(
    self,
    FileSystemId: str,
    ClientRequestToken: str = None,
    WindowsConfiguration: DeleteFileSystemWindowsConfigurationTypeDef = None,
    LustreConfiguration: DeleteFileSystemLustreConfigurationTypeDef = None
) -> DeleteFileSystemResponseTypeDef:
    pass
```

### describe_backups

Type annotations for `boto3.client("fsx").describe_backups` method.

[Client.describe_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.describe_backups)

```python
def describe_backups(
    self,
    BackupIds: List[str] = None,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBackupsResponseTypeDef:
    pass
```

### describe_data_repository_tasks

Type annotations for `boto3.client("fsx").describe_data_repository_tasks` method.

[Client.describe_data_repository_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)

```python
def describe_data_repository_tasks(
    self,
    TaskIds: List[str] = None,
    Filters: List[DataRepositoryTaskFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeDataRepositoryTasksResponseTypeDef:
    pass
```

### describe_file_system_aliases

Type annotations for `boto3.client("fsx").describe_file_system_aliases` method.

[Client.describe_file_system_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.describe_file_system_aliases)

```python
def describe_file_system_aliases(
    self,
    FileSystemId: str,
    ClientRequestToken: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeFileSystemAliasesResponseTypeDef:
    pass
```

### describe_file_systems

Type annotations for `boto3.client("fsx").describe_file_systems` method.

[Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.describe_file_systems)

```python
def describe_file_systems(
    self,
    FileSystemIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeFileSystemsResponseTypeDef:
    pass
```

### disassociate_file_system_aliases

Type annotations for `boto3.client("fsx").disassociate_file_system_aliases` method.

[Client.disassociate_file_system_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.disassociate_file_system_aliases)

```python
def disassociate_file_system_aliases(
    self,
    FileSystemId: str,
    Aliases: List[str],
    ClientRequestToken: str = None
) -> DisassociateFileSystemAliasesResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("fsx").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.generate_presigned_url)

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

### list_tags_for_resource

Type annotations for `boto3.client("fsx").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("fsx").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("fsx").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_file_system

Type annotations for `boto3.client("fsx").update_file_system` method.

[Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx.Client.update_file_system)

```python
def update_file_system(
    self,
    FileSystemId: str,
    ClientRequestToken: str = None,
    StorageCapacity: int = None,
    WindowsConfiguration: UpdateFileSystemWindowsConfigurationTypeDef = None,
    LustreConfiguration: UpdateFileSystemLustreConfigurationTypeDef = None
) -> UpdateFileSystemResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("fsx").get_paginator` method with overloads.

- `client.get_paginator("describe_backups")` -> [DescribeBackupsPaginator](./paginators.md#describebackupspaginator)
- `client.get_paginator("describe_file_systems")` -> [DescribeFileSystemsPaginator](./paginators.md#describefilesystemspaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)


