# Type annotations for boto3 FSx module

> [Index](../index.md) > FSx

Auto-generated documentation for [FSx](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html#FSx)
type annotations stubs module [mypy_boto3_fsx](https://pypi.org/project/mypy-boto3-fsx/).

```bash
pip install mypy-boto3-fsx
```

- [Type annotations for boto3 FSx module](#type-annotations-for-boto3-fsx-module)
  - [FSxClient](#fsxclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## FSxClient

Type annotations for  `boto3.client("fsx")` as [FSxClient](./client.md)

Can be used directly:

```python
from mypy_boto3_fsx.client import FSxClient
```


FSxClient [exceptions](./client.md#exceptions)



### Methods
- [associate_file_system_aliases](./client.md#associate-file-system-aliases)
- [can_paginate](./client.md#can-paginate)
- [cancel_data_repository_task](./client.md#cancel-data-repository-task)
- [copy_backup](./client.md#copy-backup)
- [create_backup](./client.md#create-backup)
- [create_data_repository_task](./client.md#create-data-repository-task)
- [create_file_system](./client.md#create-file-system)
- [create_file_system_from_backup](./client.md#create-file-system-from-backup)
- [delete_backup](./client.md#delete-backup)
- [delete_file_system](./client.md#delete-file-system)
- [describe_backups](./client.md#describe-backups)
- [describe_data_repository_tasks](./client.md#describe-data-repository-tasks)
- [describe_file_system_aliases](./client.md#describe-file-system-aliases)
- [describe_file_systems](./client.md#describe-file-systems)
- [disassociate_file_system_aliases](./client.md#disassociate-file-system-aliases)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_file_system](./client.md#update-file-system)




### Exceptions
- [ActiveDirectoryError](./client.md#activedirectoryerror)
- [BackupBeingCopied](./client.md#backupbeingcopied)
- [BackupInProgress](./client.md#backupinprogress)
- [BackupNotFound](./client.md#backupnotfound)
- [BackupRestoring](./client.md#backuprestoring)
- [BadRequest](./client.md#badrequest)
- [ClientError](./client.md#clienterror)
- [DataRepositoryTaskEnded](./client.md#datarepositorytaskended)
- [DataRepositoryTaskExecuting](./client.md#datarepositorytaskexecuting)
- [DataRepositoryTaskNotFound](./client.md#datarepositorytasknotfound)
- [FileSystemNotFound](./client.md#filesystemnotfound)
- [IncompatibleParameterError](./client.md#incompatibleparametererror)
- [IncompatibleRegionForMultiAZ](./client.md#incompatibleregionformultiaz)
- [InternalServerError](./client.md#internalservererror)
- [InvalidDestinationKmsKey](./client.md#invaliddestinationkmskey)
- [InvalidExportPath](./client.md#invalidexportpath)
- [InvalidImportPath](./client.md#invalidimportpath)
- [InvalidNetworkSettings](./client.md#invalidnetworksettings)
- [InvalidPerUnitStorageThroughput](./client.md#invalidperunitstoragethroughput)
- [InvalidRegion](./client.md#invalidregion)
- [InvalidSourceKmsKey](./client.md#invalidsourcekmskey)
- [MissingFileSystemConfiguration](./client.md#missingfilesystemconfiguration)
- [NotServiceResourceError](./client.md#notserviceresourceerror)
- [ResourceDoesNotSupportTagging](./client.md#resourcedoesnotsupporttagging)
- [ResourceNotFound](./client.md#resourcenotfound)
- [ServiceLimitExceeded](./client.md#servicelimitexceeded)
- [SourceBackupUnavailable](./client.md#sourcebackupunavailable)
- [UnsupportedOperation](./client.md#unsupportedoperation)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("fsx").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_fsx.paginators import DescribeBackupsPaginator, ...
```

- [DescribeBackupsPaginator](./paginators.md#describebackupspaginator)
- [DescribeFileSystemsPaginator](./paginators.md#describefilesystemspaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_fsx.literals import AliasLifecycle, ...
```

- [AliasLifecycle](./literals.md#aliaslifecycle)
- [AutoImportPolicyType](./literals.md#autoimportpolicytype)
- [BackupLifecycle](./literals.md#backuplifecycle)
- [BackupType](./literals.md#backuptype)
- [DataRepositoryTaskFilterName](./literals.md#datarepositorytaskfiltername)
- [DataRepositoryTaskLifecycle](./literals.md#datarepositorytasklifecycle)
- [DataRepositoryTaskType](./literals.md#datarepositorytasktype)
- [DescribeBackupsPaginatorName](./literals.md#describebackupspaginatorname)
- [DescribeFileSystemsPaginatorName](./literals.md#describefilesystemspaginatorname)
- [DriveCacheType](./literals.md#drivecachetype)
- [FileSystemLifecycle](./literals.md#filesystemlifecycle)
- [FileSystemType](./literals.md#filesystemtype)
- [FilterName](./literals.md#filtername)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [LustreDeploymentType](./literals.md#lustredeploymenttype)
- [ReportFormat](./literals.md#reportformat)
- [ReportScope](./literals.md#reportscope)
- [StorageType](./literals.md#storagetype)
- [WindowsDeploymentType](./literals.md#windowsdeploymenttype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef, ...
```

- [ActiveDirectoryBackupAttributesTypeDef](./type_defs.md#activedirectorybackupattributestypedef)
- [AdministrativeActionFailureDetailsTypeDef](./type_defs.md#administrativeactionfailuredetailstypedef)
- [AdministrativeActionTypeDef](./type_defs.md#administrativeactiontypedef)
- [AliasTypeDef](./type_defs.md#aliastypedef)
- [AssociateFileSystemAliasesResponseTypeDef](./type_defs.md#associatefilesystemaliasesresponsetypedef)
- [BackupFailureDetailsTypeDef](./type_defs.md#backupfailuredetailstypedef)
- [BackupTypeDef](./type_defs.md#backuptypedef)
- [CancelDataRepositoryTaskResponseTypeDef](./type_defs.md#canceldatarepositorytaskresponsetypedef)
- [CompletionReportTypeDef](./type_defs.md#completionreporttypedef)
- [CopyBackupResponseTypeDef](./type_defs.md#copybackupresponsetypedef)
- [CreateBackupResponseTypeDef](./type_defs.md#createbackupresponsetypedef)
- [CreateDataRepositoryTaskResponseTypeDef](./type_defs.md#createdatarepositorytaskresponsetypedef)
- [CreateFileSystemFromBackupResponseTypeDef](./type_defs.md#createfilesystemfrombackupresponsetypedef)
- [CreateFileSystemLustreConfigurationTypeDef](./type_defs.md#createfilesystemlustreconfigurationtypedef)
- [CreateFileSystemResponseTypeDef](./type_defs.md#createfilesystemresponsetypedef)
- [CreateFileSystemWindowsConfigurationTypeDef](./type_defs.md#createfilesystemwindowsconfigurationtypedef)
- [DataRepositoryConfigurationTypeDef](./type_defs.md#datarepositoryconfigurationtypedef)
- [DataRepositoryFailureDetailsTypeDef](./type_defs.md#datarepositoryfailuredetailstypedef)
- [DataRepositoryTaskFailureDetailsTypeDef](./type_defs.md#datarepositorytaskfailuredetailstypedef)
- [DataRepositoryTaskFilterTypeDef](./type_defs.md#datarepositorytaskfiltertypedef)
- [DataRepositoryTaskStatusTypeDef](./type_defs.md#datarepositorytaskstatustypedef)
- [DataRepositoryTaskTypeDef](./type_defs.md#datarepositorytasktypedef)
- [DeleteBackupResponseTypeDef](./type_defs.md#deletebackupresponsetypedef)
- [DeleteFileSystemLustreConfigurationTypeDef](./type_defs.md#deletefilesystemlustreconfigurationtypedef)
- [DeleteFileSystemLustreResponseTypeDef](./type_defs.md#deletefilesystemlustreresponsetypedef)
- [DeleteFileSystemResponseTypeDef](./type_defs.md#deletefilesystemresponsetypedef)
- [DeleteFileSystemWindowsConfigurationTypeDef](./type_defs.md#deletefilesystemwindowsconfigurationtypedef)
- [DeleteFileSystemWindowsResponseTypeDef](./type_defs.md#deletefilesystemwindowsresponsetypedef)
- [DescribeBackupsResponseTypeDef](./type_defs.md#describebackupsresponsetypedef)
- [DescribeDataRepositoryTasksResponseTypeDef](./type_defs.md#describedatarepositorytasksresponsetypedef)
- [DescribeFileSystemAliasesResponseTypeDef](./type_defs.md#describefilesystemaliasesresponsetypedef)
- [DescribeFileSystemsResponseTypeDef](./type_defs.md#describefilesystemsresponsetypedef)
- [DisassociateFileSystemAliasesResponseTypeDef](./type_defs.md#disassociatefilesystemaliasesresponsetypedef)
- [FileSystemFailureDetailsTypeDef](./type_defs.md#filesystemfailuredetailstypedef)
- [FileSystemTypeDef](./type_defs.md#filesystemtypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [LustreFileSystemConfigurationTypeDef](./type_defs.md#lustrefilesystemconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [SelfManagedActiveDirectoryAttributesTypeDef](./type_defs.md#selfmanagedactivedirectoryattributestypedef)
- [SelfManagedActiveDirectoryConfigurationTypeDef](./type_defs.md#selfmanagedactivedirectoryconfigurationtypedef)
- [SelfManagedActiveDirectoryConfigurationUpdatesTypeDef](./type_defs.md#selfmanagedactivedirectoryconfigurationupdatestypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateFileSystemLustreConfigurationTypeDef](./type_defs.md#updatefilesystemlustreconfigurationtypedef)
- [UpdateFileSystemResponseTypeDef](./type_defs.md#updatefilesystemresponsetypedef)
- [UpdateFileSystemWindowsConfigurationTypeDef](./type_defs.md#updatefilesystemwindowsconfigurationtypedef)
- [WindowsFileSystemConfigurationTypeDef](./type_defs.md#windowsfilesystemconfigurationtypedef)
