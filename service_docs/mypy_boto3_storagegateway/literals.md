# Literals for boto3 StorageGateway module

> [Index](../index.md) > [StorageGateway](./index.md) > Literals

Auto-generated documentation for [StorageGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html#StorageGateway)
type annotations stubs module [mypy_boto3_storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/).

- [Literals for boto3 StorageGateway module](#literals-for-boto3-storagegateway-module)
  - [ActiveDirectoryStatus](#activedirectorystatus)
  - [AvailabilityMonitorTestStatus](#availabilitymonitorteststatus)
  - [CaseSensitivity](#casesensitivity)
  - [DescribeTapeArchivesPaginatorName](#describetapearchivespaginatorname)
  - [DescribeTapeRecoveryPointsPaginatorName](#describetaperecoverypointspaginatorname)
  - [DescribeTapesPaginatorName](#describetapespaginatorname)
  - [DescribeVTLDevicesPaginatorName](#describevtldevicespaginatorname)
  - [FileShareType](#filesharetype)
  - [HostEnvironment](#hostenvironment)
  - [ListFileSharesPaginatorName](#listfilesharespaginatorname)
  - [ListFileSystemAssociationsPaginatorName](#listfilesystemassociationspaginatorname)
  - [ListGatewaysPaginatorName](#listgatewayspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListTapePoolsPaginatorName](#listtapepoolspaginatorname)
  - [ListTapesPaginatorName](#listtapespaginatorname)
  - [ListVolumesPaginatorName](#listvolumespaginatorname)
  - [ObjectACL](#objectacl)
  - [PoolStatus](#poolstatus)
  - [RetentionLockType](#retentionlocktype)
  - [SMBSecurityStrategy](#smbsecuritystrategy)
  - [TapeStorageClass](#tapestorageclass)

## ActiveDirectoryStatus

```python
from mypy_boto3_storagegateway.literals import ActiveDirectoryStatus
```

Values:

- `ACCESS_DENIED`
- `DETACHED`
- `JOINED`
- `JOINING`
- `NETWORK_ERROR`
- `TIMEOUT`
- `UNKNOWN_ERROR`

## AvailabilityMonitorTestStatus

```python
from mypy_boto3_storagegateway.literals import AvailabilityMonitorTestStatus
```

Values:

- `COMPLETE`
- `FAILED`
- `PENDING`

## CaseSensitivity

```python
from mypy_boto3_storagegateway.literals import CaseSensitivity
```

Values:

- `CaseSensitive`
- `ClientSpecified`

## DescribeTapeArchivesPaginatorName

```python
from mypy_boto3_storagegateway.literals import DescribeTapeArchivesPaginatorName
```

Values:

- `describe_tape_archives`

## DescribeTapeRecoveryPointsPaginatorName

```python
from mypy_boto3_storagegateway.literals import DescribeTapeRecoveryPointsPaginatorName
```

Values:

- `describe_tape_recovery_points`

## DescribeTapesPaginatorName

```python
from mypy_boto3_storagegateway.literals import DescribeTapesPaginatorName
```

Values:

- `describe_tapes`

## DescribeVTLDevicesPaginatorName

```python
from mypy_boto3_storagegateway.literals import DescribeVTLDevicesPaginatorName
```

Values:

- `describe_vtl_devices`

## FileShareType

```python
from mypy_boto3_storagegateway.literals import FileShareType
```

Values:

- `NFS`
- `SMB`

## HostEnvironment

```python
from mypy_boto3_storagegateway.literals import HostEnvironment
```

Values:

- `EC2`
- `HYPER-V`
- `KVM`
- `OTHER`
- `VMWARE`

## ListFileSharesPaginatorName

```python
from mypy_boto3_storagegateway.literals import ListFileSharesPaginatorName
```

Values:

- `list_file_shares`

## ListFileSystemAssociationsPaginatorName

```python
from mypy_boto3_storagegateway.literals import ListFileSystemAssociationsPaginatorName
```

Values:

- `list_file_system_associations`

## ListGatewaysPaginatorName

```python
from mypy_boto3_storagegateway.literals import ListGatewaysPaginatorName
```

Values:

- `list_gateways`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_storagegateway.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListTapePoolsPaginatorName

```python
from mypy_boto3_storagegateway.literals import ListTapePoolsPaginatorName
```

Values:

- `list_tape_pools`

## ListTapesPaginatorName

```python
from mypy_boto3_storagegateway.literals import ListTapesPaginatorName
```

Values:

- `list_tapes`

## ListVolumesPaginatorName

```python
from mypy_boto3_storagegateway.literals import ListVolumesPaginatorName
```

Values:

- `list_volumes`

## ObjectACL

```python
from mypy_boto3_storagegateway.literals import ObjectACL
```

Values:

- `authenticated-read`
- `aws-exec-read`
- `bucket-owner-full-control`
- `bucket-owner-read`
- `private`
- `public-read`
- `public-read-write`

## PoolStatus

```python
from mypy_boto3_storagegateway.literals import PoolStatus
```

Values:

- `ACTIVE`
- `DELETED`

## RetentionLockType

```python
from mypy_boto3_storagegateway.literals import RetentionLockType
```

Values:

- `COMPLIANCE`
- `GOVERNANCE`
- `NONE`

## SMBSecurityStrategy

```python
from mypy_boto3_storagegateway.literals import SMBSecurityStrategy
```

Values:

- `ClientSpecified`
- `MandatoryEncryption`
- `MandatorySigning`

## TapeStorageClass

```python
from mypy_boto3_storagegateway.literals import TapeStorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
