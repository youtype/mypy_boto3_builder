# Type annotations for boto3 EFS module

> [Index](../index.md) > EFS

Auto-generated documentation for [EFS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS)
type annotations stubs module [mypy_boto3_efs](https://pypi.org/project/mypy-boto3-efs/).

```bash
pip install mypy-boto3-efs
```

- [Type annotations for boto3 EFS module](#type-annotations-for-boto3-efs-module)
  - [EFSClient](#efsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## EFSClient

Type annotations for  `boto3.client("efs")` as [EFSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_efs.client import EFSClient
```


EFSClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_access_point](./client.md#create-access-point)
- [create_file_system](./client.md#create-file-system)
- [create_mount_target](./client.md#create-mount-target)
- [create_tags](./client.md#create-tags)
- [delete_access_point](./client.md#delete-access-point)
- [delete_file_system](./client.md#delete-file-system)
- [delete_file_system_policy](./client.md#delete-file-system-policy)
- [delete_mount_target](./client.md#delete-mount-target)
- [delete_tags](./client.md#delete-tags)
- [describe_access_points](./client.md#describe-access-points)
- [describe_backup_policy](./client.md#describe-backup-policy)
- [describe_file_system_policy](./client.md#describe-file-system-policy)
- [describe_file_systems](./client.md#describe-file-systems)
- [describe_lifecycle_configuration](./client.md#describe-lifecycle-configuration)
- [describe_mount_target_security_groups](./client.md#describe-mount-target-security-groups)
- [describe_mount_targets](./client.md#describe-mount-targets)
- [describe_tags](./client.md#describe-tags)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [modify_mount_target_security_groups](./client.md#modify-mount-target-security-groups)
- [put_backup_policy](./client.md#put-backup-policy)
- [put_file_system_policy](./client.md#put-file-system-policy)
- [put_lifecycle_configuration](./client.md#put-lifecycle-configuration)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_file_system](./client.md#update-file-system)




### Exceptions
- [AccessPointAlreadyExists](./client.md#accesspointalreadyexists)
- [AccessPointLimitExceeded](./client.md#accesspointlimitexceeded)
- [AccessPointNotFound](./client.md#accesspointnotfound)
- [AvailabilityZonesMismatch](./client.md#availabilityzonesmismatch)
- [BadRequest](./client.md#badrequest)
- [ClientError](./client.md#clienterror)
- [DependencyTimeout](./client.md#dependencytimeout)
- [FileSystemAlreadyExists](./client.md#filesystemalreadyexists)
- [FileSystemInUse](./client.md#filesysteminuse)
- [FileSystemLimitExceeded](./client.md#filesystemlimitexceeded)
- [FileSystemNotFound](./client.md#filesystemnotfound)
- [IncorrectFileSystemLifeCycleState](./client.md#incorrectfilesystemlifecyclestate)
- [IncorrectMountTargetState](./client.md#incorrectmounttargetstate)
- [InsufficientThroughputCapacity](./client.md#insufficientthroughputcapacity)
- [InternalServerError](./client.md#internalservererror)
- [InvalidPolicyException](./client.md#invalidpolicyexception)
- [IpAddressInUse](./client.md#ipaddressinuse)
- [MountTargetConflict](./client.md#mounttargetconflict)
- [MountTargetNotFound](./client.md#mounttargetnotfound)
- [NetworkInterfaceLimitExceeded](./client.md#networkinterfacelimitexceeded)
- [NoFreeAddressesInSubnet](./client.md#nofreeaddressesinsubnet)
- [PolicyNotFound](./client.md#policynotfound)
- [SecurityGroupLimitExceeded](./client.md#securitygrouplimitexceeded)
- [SecurityGroupNotFound](./client.md#securitygroupnotfound)
- [SubnetNotFound](./client.md#subnetnotfound)
- [ThroughputLimitExceeded](./client.md#throughputlimitexceeded)
- [TooManyRequests](./client.md#toomanyrequests)
- [UnsupportedAvailabilityZone](./client.md#unsupportedavailabilityzone)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("efs").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_efs.paginators import DescribeFileSystemsPaginator, ...
```

- [DescribeFileSystemsPaginator](./paginators.md#describefilesystemspaginator)
- [DescribeMountTargetsPaginator](./paginators.md#describemounttargetspaginator)
- [DescribeTagsPaginator](./paginators.md#describetagspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_efs.literals import DescribeFileSystemsPaginatorName, ...
```

- [DescribeFileSystemsPaginatorName](./literals.md#describefilesystemspaginatorname)
- [DescribeMountTargetsPaginatorName](./literals.md#describemounttargetspaginatorname)
- [DescribeTagsPaginatorName](./literals.md#describetagspaginatorname)
- [LifeCycleState](./literals.md#lifecyclestate)
- [PerformanceMode](./literals.md#performancemode)
- [Status](./literals.md#status)
- [ThroughputMode](./literals.md#throughputmode)
- [TransitionToIARules](./literals.md#transitiontoiarules)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_efs.type_defs import AccessPointDescriptionTypeDef, ...
```

- [AccessPointDescriptionTypeDef](./type_defs.md#accesspointdescriptiontypedef)
- [BackupPolicyDescriptionTypeDef](./type_defs.md#backuppolicydescriptiontypedef)
- [BackupPolicyTypeDef](./type_defs.md#backuppolicytypedef)
- [CreationInfoTypeDef](./type_defs.md#creationinfotypedef)
- [DescribeAccessPointsResponseTypeDef](./type_defs.md#describeaccesspointsresponsetypedef)
- [DescribeFileSystemsResponseTypeDef](./type_defs.md#describefilesystemsresponsetypedef)
- [DescribeMountTargetSecurityGroupsResponseTypeDef](./type_defs.md#describemounttargetsecuritygroupsresponsetypedef)
- [DescribeMountTargetsResponseTypeDef](./type_defs.md#describemounttargetsresponsetypedef)
- [DescribeTagsResponseTypeDef](./type_defs.md#describetagsresponsetypedef)
- [FileSystemDescriptionTypeDef](./type_defs.md#filesystemdescriptiontypedef)
- [FileSystemPolicyDescriptionTypeDef](./type_defs.md#filesystempolicydescriptiontypedef)
- [FileSystemSizeTypeDef](./type_defs.md#filesystemsizetypedef)
- [LifecycleConfigurationDescriptionTypeDef](./type_defs.md#lifecycleconfigurationdescriptiontypedef)
- [LifecyclePolicyTypeDef](./type_defs.md#lifecyclepolicytypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MountTargetDescriptionTypeDef](./type_defs.md#mounttargetdescriptiontypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PosixUserTypeDef](./type_defs.md#posixusertypedef)
- [RootDirectoryTypeDef](./type_defs.md#rootdirectorytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
