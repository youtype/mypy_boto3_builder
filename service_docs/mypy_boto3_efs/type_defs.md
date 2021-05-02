# Structures for boto3 EFS module

> [Index](../index.md) > [EFS](./index.md) > Structures

Auto-generated documentation for [EFS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html#EFS)
type annotations stubs module [mypy_boto3_efs](https://pypi.org/project/mypy-boto3-efs/).

- [Structures for boto3 EFS module](#structures-for-boto3-efs-module)
  - [AccessPointDescriptionTypeDef](#accesspointdescriptiontypedef)
  - [BackupPolicyTypeDef](#backuppolicytypedef)
  - [CreationInfoTypeDef](#creationinfotypedef)
  - [FileSystemDescriptionTypeDef](#filesystemdescriptiontypedef)
  - [FileSystemSizeTypeDef](#filesystemsizetypedef)
  - [LifecyclePolicyTypeDef](#lifecyclepolicytypedef)
  - [MountTargetDescriptionTypeDef](#mounttargetdescriptiontypedef)
  - [PosixUserTypeDef](#posixusertypedef)
  - [RootDirectoryTypeDef](#rootdirectorytypedef)
  - [TagTypeDef](#tagtypedef)
  - [BackupPolicyDescriptionTypeDef](#backuppolicydescriptiontypedef)
  - [DescribeAccessPointsResponseTypeDef](#describeaccesspointsresponsetypedef)
  - [DescribeFileSystemsResponseTypeDef](#describefilesystemsresponsetypedef)
  - [DescribeMountTargetSecurityGroupsResponseTypeDef](#describemounttargetsecuritygroupsresponsetypedef)
  - [DescribeMountTargetsResponseTypeDef](#describemounttargetsresponsetypedef)
  - [DescribeTagsResponseTypeDef](#describetagsresponsetypedef)
  - [FileSystemPolicyDescriptionTypeDef](#filesystempolicydescriptiontypedef)
  - [LifecycleConfigurationDescriptionTypeDef](#lifecycleconfigurationdescriptiontypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## AccessPointDescriptionTypeDef

```python
from mypy_boto3_efs.type_defs import AccessPointDescriptionTypeDef
```




Optional fields:
- `ClientToken`: `str`
- `Name`: `str`
- `Tags`: `List["TagTypeDef"]`
- `AccessPointId`: `str`
- `AccessPointArn`: `str`
- `FileSystemId`: `str`
- `PosixUser`: `"PosixUserTypeDef"`
- `RootDirectory`: `"RootDirectoryTypeDef"`
- `OwnerId`: `str`
- `LifeCycleState`: `LifeCycleState`


## BackupPolicyTypeDef

```python
from mypy_boto3_efs.type_defs import BackupPolicyTypeDef
```


Required fields:
- `Status`: `Status`




## CreationInfoTypeDef

```python
from mypy_boto3_efs.type_defs import CreationInfoTypeDef
```


Required fields:
- `OwnerUid`: `int`
- `OwnerGid`: `int`
- `Permissions`: `str`




## FileSystemDescriptionTypeDef

```python
from mypy_boto3_efs.type_defs import FileSystemDescriptionTypeDef
```


Required fields:
- `OwnerId`: `str`
- `CreationToken`: `str`
- `FileSystemId`: `str`
- `CreationTime`: `datetime`
- `LifeCycleState`: `LifeCycleState`
- `NumberOfMountTargets`: `int`
- `SizeInBytes`: `"FileSystemSizeTypeDef"`
- `PerformanceMode`: `PerformanceMode`
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `FileSystemArn`: `str`
- `Name`: `str`
- `Encrypted`: `bool`
- `KmsKeyId`: `str`
- `ThroughputMode`: `ThroughputMode`
- `ProvisionedThroughputInMibps`: `float`
- `AvailabilityZoneName`: `str`
- `AvailabilityZoneId`: `str`


## FileSystemSizeTypeDef

```python
from mypy_boto3_efs.type_defs import FileSystemSizeTypeDef
```


Required fields:
- `Value`: `int`



Optional fields:
- `Timestamp`: `datetime`
- `ValueInIA`: `int`
- `ValueInStandard`: `int`


## LifecyclePolicyTypeDef

```python
from mypy_boto3_efs.type_defs import LifecyclePolicyTypeDef
```




Optional fields:
- `TransitionToIA`: `TransitionToIARules`


## MountTargetDescriptionTypeDef

```python
from mypy_boto3_efs.type_defs import MountTargetDescriptionTypeDef
```


Required fields:
- `MountTargetId`: `str`
- `FileSystemId`: `str`
- `SubnetId`: `str`
- `LifeCycleState`: `LifeCycleState`



Optional fields:
- `OwnerId`: `str`
- `IpAddress`: `str`
- `NetworkInterfaceId`: `str`
- `AvailabilityZoneId`: `str`
- `AvailabilityZoneName`: `str`
- `VpcId`: `str`


## PosixUserTypeDef

```python
from mypy_boto3_efs.type_defs import PosixUserTypeDef
```


Required fields:
- `Uid`: `int`
- `Gid`: `int`



Optional fields:
- `SecondaryGids`: `List[int]`


## RootDirectoryTypeDef

```python
from mypy_boto3_efs.type_defs import RootDirectoryTypeDef
```




Optional fields:
- `Path`: `str`
- `CreationInfo`: `"CreationInfoTypeDef"`


## TagTypeDef

```python
from mypy_boto3_efs.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## BackupPolicyDescriptionTypeDef

```python
from mypy_boto3_efs.type_defs import BackupPolicyDescriptionTypeDef
```




Optional fields:
- `BackupPolicy`: `"BackupPolicyTypeDef"`


## DescribeAccessPointsResponseTypeDef

```python
from mypy_boto3_efs.type_defs import DescribeAccessPointsResponseTypeDef
```




Optional fields:
- `AccessPoints`: `List["AccessPointDescriptionTypeDef"]`
- `NextToken`: `str`


## DescribeFileSystemsResponseTypeDef

```python
from mypy_boto3_efs.type_defs import DescribeFileSystemsResponseTypeDef
```




Optional fields:
- `Marker`: `str`
- `FileSystems`: `List["FileSystemDescriptionTypeDef"]`
- `NextMarker`: `str`


## DescribeMountTargetSecurityGroupsResponseTypeDef

```python
from mypy_boto3_efs.type_defs import DescribeMountTargetSecurityGroupsResponseTypeDef
```


Required fields:
- `SecurityGroups`: `List[str]`




## DescribeMountTargetsResponseTypeDef

```python
from mypy_boto3_efs.type_defs import DescribeMountTargetsResponseTypeDef
```




Optional fields:
- `Marker`: `str`
- `MountTargets`: `List["MountTargetDescriptionTypeDef"]`
- `NextMarker`: `str`


## DescribeTagsResponseTypeDef

```python
from mypy_boto3_efs.type_defs import DescribeTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `Marker`: `str`
- `NextMarker`: `str`


## FileSystemPolicyDescriptionTypeDef

```python
from mypy_boto3_efs.type_defs import FileSystemPolicyDescriptionTypeDef
```




Optional fields:
- `FileSystemId`: `str`
- `Policy`: `str`


## LifecycleConfigurationDescriptionTypeDef

```python
from mypy_boto3_efs.type_defs import LifecycleConfigurationDescriptionTypeDef
```




Optional fields:
- `LifecyclePolicies`: `List["LifecyclePolicyTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_efs.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_efs.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

