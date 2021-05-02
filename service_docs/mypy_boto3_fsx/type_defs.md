# Structures for boto3 FSx module

> [Index](../index.md) > [FSx](./index.md) > Structures

Auto-generated documentation for [FSx](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx)
type annotations stubs module [mypy_boto3_fsx](https://pypi.org/project/mypy-boto3-fsx/).

- [Structures for boto3 FSx module](#structures-for-boto3-fsx-module)
  - [ActiveDirectoryBackupAttributesTypeDef](#activedirectorybackupattributestypedef)
  - [AdministrativeActionFailureDetailsTypeDef](#administrativeactionfailuredetailstypedef)
  - [AdministrativeActionTypeDef](#administrativeactiontypedef)
  - [AliasTypeDef](#aliastypedef)
  - [BackupFailureDetailsTypeDef](#backupfailuredetailstypedef)
  - [BackupTypeDef](#backuptypedef)
  - [CompletionReportTypeDef](#completionreporttypedef)
  - [DataRepositoryConfigurationTypeDef](#datarepositoryconfigurationtypedef)
  - [DataRepositoryFailureDetailsTypeDef](#datarepositoryfailuredetailstypedef)
  - [DataRepositoryTaskFailureDetailsTypeDef](#datarepositorytaskfailuredetailstypedef)
  - [DataRepositoryTaskStatusTypeDef](#datarepositorytaskstatustypedef)
  - [DataRepositoryTaskTypeDef](#datarepositorytasktypedef)
  - [DeleteFileSystemLustreResponseTypeDef](#deletefilesystemlustreresponsetypedef)
  - [DeleteFileSystemWindowsResponseTypeDef](#deletefilesystemwindowsresponsetypedef)
  - [FileSystemFailureDetailsTypeDef](#filesystemfailuredetailstypedef)
  - [LustreFileSystemConfigurationTypeDef](#lustrefilesystemconfigurationtypedef)
  - [SelfManagedActiveDirectoryAttributesTypeDef](#selfmanagedactivedirectoryattributestypedef)
  - [SelfManagedActiveDirectoryConfigurationTypeDef](#selfmanagedactivedirectoryconfigurationtypedef)
  - [SelfManagedActiveDirectoryConfigurationUpdatesTypeDef](#selfmanagedactivedirectoryconfigurationupdatestypedef)
  - [TagTypeDef](#tagtypedef)
  - [WindowsFileSystemConfigurationTypeDef](#windowsfilesystemconfigurationtypedef)
  - [AssociateFileSystemAliasesResponseTypeDef](#associatefilesystemaliasesresponsetypedef)
  - [CancelDataRepositoryTaskResponseTypeDef](#canceldatarepositorytaskresponsetypedef)
  - [CopyBackupResponseTypeDef](#copybackupresponsetypedef)
  - [CreateBackupResponseTypeDef](#createbackupresponsetypedef)
  - [CreateDataRepositoryTaskResponseTypeDef](#createdatarepositorytaskresponsetypedef)
  - [CreateFileSystemFromBackupResponseTypeDef](#createfilesystemfrombackupresponsetypedef)
  - [CreateFileSystemLustreConfigurationTypeDef](#createfilesystemlustreconfigurationtypedef)
  - [CreateFileSystemResponseTypeDef](#createfilesystemresponsetypedef)
  - [CreateFileSystemWindowsConfigurationTypeDef](#createfilesystemwindowsconfigurationtypedef)
  - [DataRepositoryTaskFilterTypeDef](#datarepositorytaskfiltertypedef)
  - [DeleteBackupResponseTypeDef](#deletebackupresponsetypedef)
  - [DeleteFileSystemLustreConfigurationTypeDef](#deletefilesystemlustreconfigurationtypedef)
  - [DeleteFileSystemResponseTypeDef](#deletefilesystemresponsetypedef)
  - [DeleteFileSystemWindowsConfigurationTypeDef](#deletefilesystemwindowsconfigurationtypedef)
  - [DescribeBackupsResponseTypeDef](#describebackupsresponsetypedef)
  - [DescribeDataRepositoryTasksResponseTypeDef](#describedatarepositorytasksresponsetypedef)
  - [DescribeFileSystemAliasesResponseTypeDef](#describefilesystemaliasesresponsetypedef)
  - [DescribeFileSystemsResponseTypeDef](#describefilesystemsresponsetypedef)
  - [FileSystemTypeDef](#filesystemtypedef)
  - [DisassociateFileSystemAliasesResponseTypeDef](#disassociatefilesystemaliasesresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateFileSystemLustreConfigurationTypeDef](#updatefilesystemlustreconfigurationtypedef)
  - [UpdateFileSystemResponseTypeDef](#updatefilesystemresponsetypedef)
  - [UpdateFileSystemWindowsConfigurationTypeDef](#updatefilesystemwindowsconfigurationtypedef)

## ActiveDirectoryBackupAttributesTypeDef

```python
from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef
```




Optional fields:
- `DomainName`: `str`
- `ActiveDirectoryId`: `str`
- `ResourceARN`: `str`


## AdministrativeActionFailureDetailsTypeDef

```python
from mypy_boto3_fsx.type_defs import AdministrativeActionFailureDetailsTypeDef
```




Optional fields:
- `Message`: `str`


## AdministrativeActionTypeDef

```python
from mypy_boto3_fsx.type_defs import AdministrativeActionTypeDef
```




Optional fields:
- `AdministrativeActionType`: `AdministrativeActionType`
- `ProgressPercent`: `int`
- `RequestTime`: `datetime`
- `Status`: `Status`
- `TargetFileSystemValues`: `Dict[str, Any]`
- `FailureDetails`: `"AdministrativeActionFailureDetailsTypeDef"`


## AliasTypeDef

```python
from mypy_boto3_fsx.type_defs import AliasTypeDef
```




Optional fields:
- `Name`: `str`
- `Lifecycle`: `AliasLifecycle`


## BackupFailureDetailsTypeDef

```python
from mypy_boto3_fsx.type_defs import BackupFailureDetailsTypeDef
```




Optional fields:
- `Message`: `str`


## BackupTypeDef

```python
from mypy_boto3_fsx.type_defs import BackupTypeDef
```


Required fields:
- `BackupId`: `str`
- `Lifecycle`: `BackupLifecycle`
- `Type`: `BackupType`
- `CreationTime`: `datetime`
- `FileSystem`: `Dict[str, Any]`



Optional fields:
- `FailureDetails`: `"BackupFailureDetailsTypeDef"`
- `ProgressPercent`: `int`
- `KmsKeyId`: `str`
- `ResourceARN`: `str`
- `Tags`: `List["TagTypeDef"]`
- `DirectoryInformation`: `"ActiveDirectoryBackupAttributesTypeDef"`
- `OwnerId`: `str`
- `SourceBackupId`: `str`
- `SourceBackupRegion`: `str`


## CompletionReportTypeDef

```python
from mypy_boto3_fsx.type_defs import CompletionReportTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `Path`: `str`
- `Format`: `ReportFormat`
- `Scope`: `ReportScope`


## DataRepositoryConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import DataRepositoryConfigurationTypeDef
```




Optional fields:
- `Lifecycle`: `DataRepositoryLifecycle`
- `ImportPath`: `str`
- `ExportPath`: `str`
- `ImportedFileChunkSize`: `int`
- `AutoImportPolicy`: `AutoImportPolicyType`
- `FailureDetails`: `"DataRepositoryFailureDetailsTypeDef"`


## DataRepositoryFailureDetailsTypeDef

```python
from mypy_boto3_fsx.type_defs import DataRepositoryFailureDetailsTypeDef
```




Optional fields:
- `Message`: `str`


## DataRepositoryTaskFailureDetailsTypeDef

```python
from mypy_boto3_fsx.type_defs import DataRepositoryTaskFailureDetailsTypeDef
```




Optional fields:
- `Message`: `str`


## DataRepositoryTaskStatusTypeDef

```python
from mypy_boto3_fsx.type_defs import DataRepositoryTaskStatusTypeDef
```




Optional fields:
- `TotalCount`: `int`
- `SucceededCount`: `int`
- `FailedCount`: `int`
- `LastUpdatedTime`: `datetime`


## DataRepositoryTaskTypeDef

```python
from mypy_boto3_fsx.type_defs import DataRepositoryTaskTypeDef
```


Required fields:
- `TaskId`: `str`
- `Lifecycle`: `DataRepositoryTaskLifecycle`
- `Type`: `DataRepositoryTaskType`
- `CreationTime`: `datetime`
- `FileSystemId`: `str`



Optional fields:
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `ResourceARN`: `str`
- `Tags`: `List["TagTypeDef"]`
- `Paths`: `List[str]`
- `FailureDetails`: `"DataRepositoryTaskFailureDetailsTypeDef"`
- `Status`: `"DataRepositoryTaskStatusTypeDef"`
- `Report`: `"CompletionReportTypeDef"`


## DeleteFileSystemLustreResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DeleteFileSystemLustreResponseTypeDef
```




Optional fields:
- `FinalBackupId`: `str`
- `FinalBackupTags`: `List["TagTypeDef"]`


## DeleteFileSystemWindowsResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DeleteFileSystemWindowsResponseTypeDef
```




Optional fields:
- `FinalBackupId`: `str`
- `FinalBackupTags`: `List["TagTypeDef"]`


## FileSystemFailureDetailsTypeDef

```python
from mypy_boto3_fsx.type_defs import FileSystemFailureDetailsTypeDef
```




Optional fields:
- `Message`: `str`


## LustreFileSystemConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import LustreFileSystemConfigurationTypeDef
```




Optional fields:
- `WeeklyMaintenanceStartTime`: `str`
- `DataRepositoryConfiguration`: `"DataRepositoryConfigurationTypeDef"`
- `DeploymentType`: `LustreDeploymentType`
- `PerUnitStorageThroughput`: `int`
- `MountName`: `str`
- `DailyAutomaticBackupStartTime`: `str`
- `AutomaticBackupRetentionDays`: `int`
- `CopyTagsToBackups`: `bool`
- `DriveCacheType`: `DriveCacheType`


## SelfManagedActiveDirectoryAttributesTypeDef

```python
from mypy_boto3_fsx.type_defs import SelfManagedActiveDirectoryAttributesTypeDef
```




Optional fields:
- `DomainName`: `str`
- `OrganizationalUnitDistinguishedName`: `str`
- `FileSystemAdministratorsGroup`: `str`
- `UserName`: `str`
- `DnsIps`: `List[str]`


## SelfManagedActiveDirectoryConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import SelfManagedActiveDirectoryConfigurationTypeDef
```


Required fields:
- `DomainName`: `str`
- `UserName`: `str`
- `Password`: `str`
- `DnsIps`: `List[str]`



Optional fields:
- `OrganizationalUnitDistinguishedName`: `str`
- `FileSystemAdministratorsGroup`: `str`


## SelfManagedActiveDirectoryConfigurationUpdatesTypeDef

```python
from mypy_boto3_fsx.type_defs import SelfManagedActiveDirectoryConfigurationUpdatesTypeDef
```




Optional fields:
- `UserName`: `str`
- `Password`: `str`
- `DnsIps`: `List[str]`


## TagTypeDef

```python
from mypy_boto3_fsx.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## WindowsFileSystemConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import WindowsFileSystemConfigurationTypeDef
```




Optional fields:
- `ActiveDirectoryId`: `str`
- `SelfManagedActiveDirectoryConfiguration`: `"SelfManagedActiveDirectoryAttributesTypeDef"`
- `DeploymentType`: `WindowsDeploymentType`
- `RemoteAdministrationEndpoint`: `str`
- `PreferredSubnetId`: `str`
- `PreferredFileServerIp`: `str`
- `ThroughputCapacity`: `int`
- `MaintenanceOperationsInProgress`: `List[FileSystemMaintenanceOperation]`
- `WeeklyMaintenanceStartTime`: `str`
- `DailyAutomaticBackupStartTime`: `str`
- `AutomaticBackupRetentionDays`: `int`
- `CopyTagsToBackups`: `bool`
- `Aliases`: `List["AliasTypeDef"]`


## AssociateFileSystemAliasesResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import AssociateFileSystemAliasesResponseTypeDef
```




Optional fields:
- `Aliases`: `List["AliasTypeDef"]`


## CancelDataRepositoryTaskResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import CancelDataRepositoryTaskResponseTypeDef
```




Optional fields:
- `Lifecycle`: `DataRepositoryTaskLifecycle`
- `TaskId`: `str`


## CopyBackupResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import CopyBackupResponseTypeDef
```




Optional fields:
- `Backup`: `"BackupTypeDef"`


## CreateBackupResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import CreateBackupResponseTypeDef
```




Optional fields:
- `Backup`: `"BackupTypeDef"`


## CreateDataRepositoryTaskResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import CreateDataRepositoryTaskResponseTypeDef
```




Optional fields:
- `DataRepositoryTask`: `"DataRepositoryTaskTypeDef"`


## CreateFileSystemFromBackupResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import CreateFileSystemFromBackupResponseTypeDef
```




Optional fields:
- `FileSystem`: `Dict[str, Any]`


## CreateFileSystemLustreConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import CreateFileSystemLustreConfigurationTypeDef
```




Optional fields:
- `WeeklyMaintenanceStartTime`: `str`
- `ImportPath`: `str`
- `ExportPath`: `str`
- `ImportedFileChunkSize`: `int`
- `DeploymentType`: `LustreDeploymentType`
- `AutoImportPolicy`: `AutoImportPolicyType`
- `PerUnitStorageThroughput`: `int`
- `DailyAutomaticBackupStartTime`: `str`
- `AutomaticBackupRetentionDays`: `int`
- `CopyTagsToBackups`: `bool`
- `DriveCacheType`: `DriveCacheType`


## CreateFileSystemResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import CreateFileSystemResponseTypeDef
```




Optional fields:
- `FileSystem`: `Dict[str, Any]`


## CreateFileSystemWindowsConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import CreateFileSystemWindowsConfigurationTypeDef
```


Required fields:
- `ThroughputCapacity`: `int`



Optional fields:
- `ActiveDirectoryId`: `str`
- `SelfManagedActiveDirectoryConfiguration`: `"SelfManagedActiveDirectoryConfigurationTypeDef"`
- `DeploymentType`: `WindowsDeploymentType`
- `PreferredSubnetId`: `str`
- `WeeklyMaintenanceStartTime`: `str`
- `DailyAutomaticBackupStartTime`: `str`
- `AutomaticBackupRetentionDays`: `int`
- `CopyTagsToBackups`: `bool`
- `Aliases`: `List[str]`


## DataRepositoryTaskFilterTypeDef

```python
from mypy_boto3_fsx.type_defs import DataRepositoryTaskFilterTypeDef
```




Optional fields:
- `Name`: `DataRepositoryTaskFilterName`
- `Values`: `List[str]`


## DeleteBackupResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DeleteBackupResponseTypeDef
```




Optional fields:
- `BackupId`: `str`
- `Lifecycle`: `BackupLifecycle`


## DeleteFileSystemLustreConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import DeleteFileSystemLustreConfigurationTypeDef
```




Optional fields:
- `SkipFinalBackup`: `bool`
- `FinalBackupTags`: `List["TagTypeDef"]`


## DeleteFileSystemResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DeleteFileSystemResponseTypeDef
```




Optional fields:
- `FileSystemId`: `str`
- `Lifecycle`: `FileSystemLifecycle`
- `WindowsResponse`: `"DeleteFileSystemWindowsResponseTypeDef"`
- `LustreResponse`: `"DeleteFileSystemLustreResponseTypeDef"`


## DeleteFileSystemWindowsConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import DeleteFileSystemWindowsConfigurationTypeDef
```




Optional fields:
- `SkipFinalBackup`: `bool`
- `FinalBackupTags`: `List["TagTypeDef"]`


## DescribeBackupsResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DescribeBackupsResponseTypeDef
```




Optional fields:
- `Backups`: `List["BackupTypeDef"]`
- `NextToken`: `str`


## DescribeDataRepositoryTasksResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DescribeDataRepositoryTasksResponseTypeDef
```




Optional fields:
- `DataRepositoryTasks`: `List["DataRepositoryTaskTypeDef"]`
- `NextToken`: `str`


## DescribeFileSystemAliasesResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DescribeFileSystemAliasesResponseTypeDef
```




Optional fields:
- `Aliases`: `List["AliasTypeDef"]`
- `NextToken`: `str`


## DescribeFileSystemsResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DescribeFileSystemsResponseTypeDef
```




Optional fields:
- `FileSystems`: `List[Dict[str, Any]]`
- `NextToken`: `str`


## FileSystemTypeDef

```python
from mypy_boto3_fsx.type_defs import FileSystemTypeDef
```




Optional fields:
- `OwnerId`: `str`
- `CreationTime`: `datetime`
- `FileSystemId`: `str`
- `FileSystemType`: `FileSystemType`
- `Lifecycle`: `FileSystemLifecycle`
- `FailureDetails`: `"FileSystemFailureDetailsTypeDef"`
- `StorageCapacity`: `int`
- `StorageType`: `StorageType`
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `NetworkInterfaceIds`: `List[str]`
- `DNSName`: `str`
- `KmsKeyId`: `str`
- `ResourceARN`: `str`
- `Tags`: `List["TagTypeDef"]`
- `WindowsConfiguration`: `"WindowsFileSystemConfigurationTypeDef"`
- `LustreConfiguration`: `"LustreFileSystemConfigurationTypeDef"`
- `AdministrativeActions`: `List["AdministrativeActionTypeDef"]`


## DisassociateFileSystemAliasesResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import DisassociateFileSystemAliasesResponseTypeDef
```




Optional fields:
- `Aliases`: `List["AliasTypeDef"]`


## FilterTypeDef

```python
from mypy_boto3_fsx.type_defs import FilterTypeDef
```




Optional fields:
- `Name`: `FilterName`
- `Values`: `List[str]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_fsx.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateFileSystemLustreConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import UpdateFileSystemLustreConfigurationTypeDef
```




Optional fields:
- `WeeklyMaintenanceStartTime`: `str`
- `DailyAutomaticBackupStartTime`: `str`
- `AutomaticBackupRetentionDays`: `int`
- `AutoImportPolicy`: `AutoImportPolicyType`


## UpdateFileSystemResponseTypeDef

```python
from mypy_boto3_fsx.type_defs import UpdateFileSystemResponseTypeDef
```




Optional fields:
- `FileSystem`: `Dict[str, Any]`


## UpdateFileSystemWindowsConfigurationTypeDef

```python
from mypy_boto3_fsx.type_defs import UpdateFileSystemWindowsConfigurationTypeDef
```




Optional fields:
- `WeeklyMaintenanceStartTime`: `str`
- `DailyAutomaticBackupStartTime`: `str`
- `AutomaticBackupRetentionDays`: `int`
- `ThroughputCapacity`: `int`
- `SelfManagedActiveDirectoryConfiguration`: `"SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"`

