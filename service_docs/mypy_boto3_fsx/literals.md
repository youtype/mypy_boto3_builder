# Literals for boto3 FSx module

> [Index](../index.md) > [FSx](./index.md) > Literals

Auto-generated documentation for [FSx](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx)
type annotations stubs module [mypy_boto3_fsx](https://pypi.org/project/mypy-boto3-fsx/).

- [Literals for boto3 FSx module](#literals-for-boto3-fsx-module)
  - [AliasLifecycle](#aliaslifecycle)
  - [AutoImportPolicyType](#autoimportpolicytype)
  - [BackupLifecycle](#backuplifecycle)
  - [BackupType](#backuptype)
  - [DataRepositoryTaskFilterName](#datarepositorytaskfiltername)
  - [DataRepositoryTaskLifecycle](#datarepositorytasklifecycle)
  - [DataRepositoryTaskType](#datarepositorytasktype)
  - [DescribeBackupsPaginatorName](#describebackupspaginatorname)
  - [DescribeFileSystemsPaginatorName](#describefilesystemspaginatorname)
  - [DriveCacheType](#drivecachetype)
  - [FileSystemLifecycle](#filesystemlifecycle)
  - [FileSystemType](#filesystemtype)
  - [FilterName](#filtername)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [LustreDeploymentType](#lustredeploymenttype)
  - [ReportFormat](#reportformat)
  - [ReportScope](#reportscope)
  - [StorageType](#storagetype)
  - [WindowsDeploymentType](#windowsdeploymenttype)

## AliasLifecycle

```python
from mypy_boto3_fsx.literals import AliasLifecycle
```

Values:

- `AVAILABLE`
- `CREATE_FAILED`
- `CREATING`
- `DELETE_FAILED`
- `DELETING`

## AutoImportPolicyType

```python
from mypy_boto3_fsx.literals import AutoImportPolicyType
```

Values:

- `NEW`
- `NEW_CHANGED`
- `NONE`

## BackupLifecycle

```python
from mypy_boto3_fsx.literals import BackupLifecycle
```

Values:

- `AVAILABLE`
- `COPYING`
- `CREATING`
- `DELETED`
- `FAILED`
- `PENDING`
- `TRANSFERRING`

## BackupType

```python
from mypy_boto3_fsx.literals import BackupType
```

Values:

- `AUTOMATIC`
- `AWS_BACKUP`
- `USER_INITIATED`

## DataRepositoryTaskFilterName

```python
from mypy_boto3_fsx.literals import DataRepositoryTaskFilterName
```

Values:

- `file-system-id`
- `task-lifecycle`

## DataRepositoryTaskLifecycle

```python
from mypy_boto3_fsx.literals import DataRepositoryTaskLifecycle
```

Values:

- `CANCELED`
- `CANCELING`
- `EXECUTING`
- `FAILED`
- `PENDING`
- `SUCCEEDED`

## DataRepositoryTaskType

```python
from mypy_boto3_fsx.literals import DataRepositoryTaskType
```

Values:

- `EXPORT_TO_REPOSITORY`

## DescribeBackupsPaginatorName

```python
from mypy_boto3_fsx.literals import DescribeBackupsPaginatorName
```

Values:

- `describe_backups`

## DescribeFileSystemsPaginatorName

```python
from mypy_boto3_fsx.literals import DescribeFileSystemsPaginatorName
```

Values:

- `describe_file_systems`

## DriveCacheType

```python
from mypy_boto3_fsx.literals import DriveCacheType
```

Values:

- `NONE`
- `READ`

## FileSystemLifecycle

```python
from mypy_boto3_fsx.literals import FileSystemLifecycle
```

Values:

- `AVAILABLE`
- `CREATING`
- `DELETING`
- `FAILED`
- `MISCONFIGURED`
- `UPDATING`

## FileSystemType

```python
from mypy_boto3_fsx.literals import FileSystemType
```

Values:

- `LUSTRE`
- `WINDOWS`

## FilterName

```python
from mypy_boto3_fsx.literals import FilterName
```

Values:

- `backup-type`
- `file-system-id`
- `file-system-type`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_fsx.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## LustreDeploymentType

```python
from mypy_boto3_fsx.literals import LustreDeploymentType
```

Values:

- `PERSISTENT_1`
- `SCRATCH_1`
- `SCRATCH_2`

## ReportFormat

```python
from mypy_boto3_fsx.literals import ReportFormat
```

Values:

- `REPORT_CSV_20191124`

## ReportScope

```python
from mypy_boto3_fsx.literals import ReportScope
```

Values:

- `FAILED_FILES_ONLY`

## StorageType

```python
from mypy_boto3_fsx.literals import StorageType
```

Values:

- `HDD`
- `SSD`

## WindowsDeploymentType

```python
from mypy_boto3_fsx.literals import WindowsDeploymentType
```

Values:

- `MULTI_AZ_1`
- `SINGLE_AZ_1`
- `SINGLE_AZ_2`
