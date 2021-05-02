# EFSClient for boto3 EFS module

> [Index](../index.md) > [EFS](./index.md) > EFSClient

Auto-generated documentation for [EFS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS)
type annotations stubs module [mypy_boto3_efs](https://pypi.org/project/mypy-boto3-efs/).

- [EFSClient for boto3 EFS module](#efsclient-for-boto3-efs-module)
  - [EFSClient](#efsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_access_point](#create_access_point)
    - [create_file_system](#create_file_system)
    - [create_mount_target](#create_mount_target)
    - [create_tags](#create_tags)
    - [delete_access_point](#delete_access_point)
    - [delete_file_system](#delete_file_system)
    - [delete_file_system_policy](#delete_file_system_policy)
    - [delete_mount_target](#delete_mount_target)
    - [delete_tags](#delete_tags)
    - [describe_access_points](#describe_access_points)
    - [describe_backup_policy](#describe_backup_policy)
    - [describe_file_system_policy](#describe_file_system_policy)
    - [describe_file_systems](#describe_file_systems)
    - [describe_lifecycle_configuration](#describe_lifecycle_configuration)
    - [describe_mount_target_security_groups](#describe_mount_target_security_groups)
    - [describe_mount_targets](#describe_mount_targets)
    - [describe_tags](#describe_tags)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_mount_target_security_groups](#modify_mount_target_security_groups)
    - [put_backup_policy](#put_backup_policy)
    - [put_file_system_policy](#put_file_system_policy)
    - [put_lifecycle_configuration](#put_lifecycle_configuration)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_file_system](#update_file_system)
    - [get_paginator](#get_paginator)

## EFSClient

Type annotations for `boto3.client("efs")`

Can be used directly:

```python
from mypy_boto3_efs.client import EFSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_efs.client import Exceptions

def handle_error(exc: Exceptions.AccessPointAlreadyExists) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessPointAlreadyExists`
- `Exceptions.AccessPointLimitExceeded`
- `Exceptions.AccessPointNotFound`
- `Exceptions.AvailabilityZonesMismatch`
- `Exceptions.BadRequest`
- `Exceptions.ClientError`
- `Exceptions.DependencyTimeout`
- `Exceptions.FileSystemAlreadyExists`
- `Exceptions.FileSystemInUse`
- `Exceptions.FileSystemLimitExceeded`
- `Exceptions.FileSystemNotFound`
- `Exceptions.IncorrectFileSystemLifeCycleState`
- `Exceptions.IncorrectMountTargetState`
- `Exceptions.InsufficientThroughputCapacity`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidPolicyException`
- `Exceptions.IpAddressInUse`
- `Exceptions.MountTargetConflict`
- `Exceptions.MountTargetNotFound`
- `Exceptions.NetworkInterfaceLimitExceeded`
- `Exceptions.NoFreeAddressesInSubnet`
- `Exceptions.PolicyNotFound`
- `Exceptions.SecurityGroupLimitExceeded`
- `Exceptions.SecurityGroupNotFound`
- `Exceptions.SubnetNotFound`
- `Exceptions.ThroughputLimitExceeded`
- `Exceptions.TooManyRequests`
- `Exceptions.UnsupportedAvailabilityZone`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("efs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_access_point

Type annotations for `boto3.client("efs").create_access_point` method.

[Client.create_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.create_access_point)

```python
def create_access_point(
    self,
    ClientToken: str,
    FileSystemId: str,
    Tags: List["TagTypeDef"] = None,
    PosixUser: "PosixUserTypeDef" = None,
    RootDirectory: "RootDirectoryTypeDef" = None
) -> "AccessPointDescriptionTypeDef":
    pass
```

### create_file_system

Type annotations for `boto3.client("efs").create_file_system` method.

[Client.create_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.create_file_system)

```python
def create_file_system(
    self,
    CreationToken: str,
    PerformanceMode: PerformanceMode = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    ThroughputMode: ThroughputMode = None,
    ProvisionedThroughputInMibps: float = None,
    AvailabilityZoneName: str = None,
    Backup: bool = None,
    Tags: List["TagTypeDef"] = None
) -> "FileSystemDescriptionTypeDef":
    pass
```

### create_mount_target

Type annotations for `boto3.client("efs").create_mount_target` method.

[Client.create_mount_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.create_mount_target)

```python
def create_mount_target(
    self,
    FileSystemId: str,
    SubnetId: str,
    IpAddress: str = None,
    SecurityGroups: List[str] = None
) -> "MountTargetDescriptionTypeDef":
    pass
```

### create_tags

Type annotations for `boto3.client("efs").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.create_tags)

```python
def create_tags(
    self,
    FileSystemId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### delete_access_point

Type annotations for `boto3.client("efs").delete_access_point` method.

[Client.delete_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.delete_access_point)

```python
def delete_access_point(
    self,
    AccessPointId: str
) -> None:
    pass
```

### delete_file_system

Type annotations for `boto3.client("efs").delete_file_system` method.

[Client.delete_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.delete_file_system)

```python
def delete_file_system(
    self,
    FileSystemId: str
) -> None:
    pass
```

### delete_file_system_policy

Type annotations for `boto3.client("efs").delete_file_system_policy` method.

[Client.delete_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.delete_file_system_policy)

```python
def delete_file_system_policy(
    self,
    FileSystemId: str
) -> None:
    pass
```

### delete_mount_target

Type annotations for `boto3.client("efs").delete_mount_target` method.

[Client.delete_mount_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.delete_mount_target)

```python
def delete_mount_target(
    self,
    MountTargetId: str
) -> None:
    pass
```

### delete_tags

Type annotations for `boto3.client("efs").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.delete_tags)

```python
def delete_tags(
    self,
    FileSystemId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### describe_access_points

Type annotations for `boto3.client("efs").describe_access_points` method.

[Client.describe_access_points documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_access_points)

```python
def describe_access_points(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    AccessPointId: str = None,
    FileSystemId: str = None
) -> DescribeAccessPointsResponseTypeDef:
    pass
```

### describe_backup_policy

Type annotations for `boto3.client("efs").describe_backup_policy` method.

[Client.describe_backup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_backup_policy)

```python
def describe_backup_policy(
    self,
    FileSystemId: str
) -> BackupPolicyDescriptionTypeDef:
    pass
```

### describe_file_system_policy

Type annotations for `boto3.client("efs").describe_file_system_policy` method.

[Client.describe_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_file_system_policy)

```python
def describe_file_system_policy(
    self,
    FileSystemId: str
) -> FileSystemPolicyDescriptionTypeDef:
    pass
```

### describe_file_systems

Type annotations for `boto3.client("efs").describe_file_systems` method.

[Client.describe_file_systems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_file_systems)

```python
def describe_file_systems(
    self,
    MaxItems: int = None,
    Marker: str = None,
    CreationToken: str = None,
    FileSystemId: str = None
) -> DescribeFileSystemsResponseTypeDef:
    pass
```

### describe_lifecycle_configuration

Type annotations for `boto3.client("efs").describe_lifecycle_configuration` method.

[Client.describe_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_lifecycle_configuration)

```python
def describe_lifecycle_configuration(
    self,
    FileSystemId: str
) -> LifecycleConfigurationDescriptionTypeDef:
    pass
```

### describe_mount_target_security_groups

Type annotations for `boto3.client("efs").describe_mount_target_security_groups` method.

[Client.describe_mount_target_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_mount_target_security_groups)

```python
def describe_mount_target_security_groups(
    self,
    MountTargetId: str
) -> DescribeMountTargetSecurityGroupsResponseTypeDef:
    pass
```

### describe_mount_targets

Type annotations for `boto3.client("efs").describe_mount_targets` method.

[Client.describe_mount_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_mount_targets)

```python
def describe_mount_targets(
    self,
    MaxItems: int = None,
    Marker: str = None,
    FileSystemId: str = None,
    MountTargetId: str = None,
    AccessPointId: str = None
) -> DescribeMountTargetsResponseTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("efs").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.describe_tags)

```python
def describe_tags(
    self,
    FileSystemId: str,
    MaxItems: int = None,
    Marker: str = None
) -> DescribeTagsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("efs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.generate_presigned_url)

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

Type annotations for `boto3.client("efs").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### modify_mount_target_security_groups

Type annotations for `boto3.client("efs").modify_mount_target_security_groups` method.

[Client.modify_mount_target_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.modify_mount_target_security_groups)

```python
def modify_mount_target_security_groups(
    self,
    MountTargetId: str,
    SecurityGroups: List[str] = None
) -> None:
    pass
```

### put_backup_policy

Type annotations for `boto3.client("efs").put_backup_policy` method.

[Client.put_backup_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.put_backup_policy)

```python
def put_backup_policy(
    self,
    FileSystemId: str,
    BackupPolicy: "BackupPolicyTypeDef"
) -> BackupPolicyDescriptionTypeDef:
    pass
```

### put_file_system_policy

Type annotations for `boto3.client("efs").put_file_system_policy` method.

[Client.put_file_system_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.put_file_system_policy)

```python
def put_file_system_policy(
    self,
    FileSystemId: str,
    Policy: str,
    BypassPolicyLockoutSafetyCheck: bool = None
) -> FileSystemPolicyDescriptionTypeDef:
    pass
```

### put_lifecycle_configuration

Type annotations for `boto3.client("efs").put_lifecycle_configuration` method.

[Client.put_lifecycle_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.put_lifecycle_configuration)

```python
def put_lifecycle_configuration(
    self,
    FileSystemId: str,
    LifecyclePolicies: List["LifecyclePolicyTypeDef"]
) -> LifecycleConfigurationDescriptionTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("efs").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("efs").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_file_system

Type annotations for `boto3.client("efs").update_file_system` method.

[Client.update_file_system documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS.Client.update_file_system)

```python
def update_file_system(
    self,
    FileSystemId: str,
    ThroughputMode: ThroughputMode = None,
    ProvisionedThroughputInMibps: float = None
) -> "FileSystemDescriptionTypeDef":
    pass
```



### get_paginator

Type annotations for `boto3.client("efs").get_paginator` method with overloads.

- `client.get_paginator("describe_file_systems")` -> [DescribeFileSystemsPaginator](./paginators.md#describefilesystemspaginator)
- `client.get_paginator("describe_mount_targets")` -> [DescribeMountTargetsPaginator](./paginators.md#describemounttargetspaginator)
- `client.get_paginator("describe_tags")` -> [DescribeTagsPaginator](./paginators.md#describetagspaginator)


