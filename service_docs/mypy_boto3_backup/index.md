# Type annotations for boto3 Backup module

> [Index](../index.md) > Backup

Auto-generated documentation for [Backup](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup)
type annotations stubs module [mypy_boto3_backup](https://pypi.org/project/mypy-boto3-backup/).

```bash
pip install mypy-boto3-backup
```

- [Type annotations for boto3 Backup module](#type-annotations-for-boto3-backup-module)
  - [BackupClient](#backupclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## BackupClient

Type annotations for  `boto3.client("backup")` as [BackupClient](./client.md)

Can be used directly:

```python
from mypy_boto3_backup.client import BackupClient
```


BackupClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_backup_plan](./client.md#create-backup-plan)
- [create_backup_selection](./client.md#create-backup-selection)
- [create_backup_vault](./client.md#create-backup-vault)
- [delete_backup_plan](./client.md#delete-backup-plan)
- [delete_backup_selection](./client.md#delete-backup-selection)
- [delete_backup_vault](./client.md#delete-backup-vault)
- [delete_backup_vault_access_policy](./client.md#delete-backup-vault-access-policy)
- [delete_backup_vault_notifications](./client.md#delete-backup-vault-notifications)
- [delete_recovery_point](./client.md#delete-recovery-point)
- [describe_backup_job](./client.md#describe-backup-job)
- [describe_backup_vault](./client.md#describe-backup-vault)
- [describe_copy_job](./client.md#describe-copy-job)
- [describe_global_settings](./client.md#describe-global-settings)
- [describe_protected_resource](./client.md#describe-protected-resource)
- [describe_recovery_point](./client.md#describe-recovery-point)
- [describe_region_settings](./client.md#describe-region-settings)
- [describe_restore_job](./client.md#describe-restore-job)
- [disassociate_recovery_point](./client.md#disassociate-recovery-point)
- [export_backup_plan_template](./client.md#export-backup-plan-template)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_backup_plan](./client.md#get-backup-plan)
- [get_backup_plan_from_json](./client.md#get-backup-plan-from-json)
- [get_backup_plan_from_template](./client.md#get-backup-plan-from-template)
- [get_backup_selection](./client.md#get-backup-selection)
- [get_backup_vault_access_policy](./client.md#get-backup-vault-access-policy)
- [get_backup_vault_notifications](./client.md#get-backup-vault-notifications)
- [get_recovery_point_restore_metadata](./client.md#get-recovery-point-restore-metadata)
- [get_supported_resource_types](./client.md#get-supported-resource-types)
- [list_backup_jobs](./client.md#list-backup-jobs)
- [list_backup_plan_templates](./client.md#list-backup-plan-templates)
- [list_backup_plan_versions](./client.md#list-backup-plan-versions)
- [list_backup_plans](./client.md#list-backup-plans)
- [list_backup_selections](./client.md#list-backup-selections)
- [list_backup_vaults](./client.md#list-backup-vaults)
- [list_copy_jobs](./client.md#list-copy-jobs)
- [list_protected_resources](./client.md#list-protected-resources)
- [list_recovery_points_by_backup_vault](./client.md#list-recovery-points-by-backup-vault)
- [list_recovery_points_by_resource](./client.md#list-recovery-points-by-resource)
- [list_restore_jobs](./client.md#list-restore-jobs)
- [list_tags](./client.md#list-tags)
- [put_backup_vault_access_policy](./client.md#put-backup-vault-access-policy)
- [put_backup_vault_notifications](./client.md#put-backup-vault-notifications)
- [start_backup_job](./client.md#start-backup-job)
- [start_copy_job](./client.md#start-copy-job)
- [start_restore_job](./client.md#start-restore-job)
- [stop_backup_job](./client.md#stop-backup-job)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_backup_plan](./client.md#update-backup-plan)
- [update_global_settings](./client.md#update-global-settings)
- [update_recovery_point_lifecycle](./client.md#update-recovery-point-lifecycle)
- [update_region_settings](./client.md#update-region-settings)




### Exceptions
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [ClientError](./client.md#clienterror)
- [DependencyFailureException](./client.md#dependencyfailureexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [InvalidResourceStateException](./client.md#invalidresourcestateexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MissingParameterValueException](./client.md#missingparametervalueexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_backup.literals import BackupJobState, ...
```

- [BackupJobState](./literals.md#backupjobstate)
- [BackupVaultEvent](./literals.md#backupvaultevent)
- [ConditionType](./literals.md#conditiontype)
- [CopyJobState](./literals.md#copyjobstate)
- [RecoveryPointStatus](./literals.md#recoverypointstatus)
- [RestoreJobStatus](./literals.md#restorejobstatus)
- [StorageClass](./literals.md#storageclass)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_backup.type_defs import AdvancedBackupSettingTypeDef, ...
```

- [AdvancedBackupSettingTypeDef](./type_defs.md#advancedbackupsettingtypedef)
- [BackupJobTypeDef](./type_defs.md#backupjobtypedef)
- [BackupPlanInputTypeDef](./type_defs.md#backupplaninputtypedef)
- [BackupPlanTemplatesListMemberTypeDef](./type_defs.md#backupplantemplateslistmembertypedef)
- [BackupPlanTypeDef](./type_defs.md#backupplantypedef)
- [BackupPlansListMemberTypeDef](./type_defs.md#backupplanslistmembertypedef)
- [BackupRuleInputTypeDef](./type_defs.md#backupruleinputtypedef)
- [BackupRuleTypeDef](./type_defs.md#backupruletypedef)
- [BackupSelectionTypeDef](./type_defs.md#backupselectiontypedef)
- [BackupSelectionsListMemberTypeDef](./type_defs.md#backupselectionslistmembertypedef)
- [BackupVaultListMemberTypeDef](./type_defs.md#backupvaultlistmembertypedef)
- [CalculatedLifecycleTypeDef](./type_defs.md#calculatedlifecycletypedef)
- [ConditionTypeDef](./type_defs.md#conditiontypedef)
- [CopyActionTypeDef](./type_defs.md#copyactiontypedef)
- [CopyJobTypeDef](./type_defs.md#copyjobtypedef)
- [CreateBackupPlanOutputTypeDef](./type_defs.md#createbackupplanoutputtypedef)
- [CreateBackupSelectionOutputTypeDef](./type_defs.md#createbackupselectionoutputtypedef)
- [CreateBackupVaultOutputTypeDef](./type_defs.md#createbackupvaultoutputtypedef)
- [DeleteBackupPlanOutputTypeDef](./type_defs.md#deletebackupplanoutputtypedef)
- [DescribeBackupJobOutputTypeDef](./type_defs.md#describebackupjoboutputtypedef)
- [DescribeBackupVaultOutputTypeDef](./type_defs.md#describebackupvaultoutputtypedef)
- [DescribeCopyJobOutputTypeDef](./type_defs.md#describecopyjoboutputtypedef)
- [DescribeGlobalSettingsOutputTypeDef](./type_defs.md#describeglobalsettingsoutputtypedef)
- [DescribeProtectedResourceOutputTypeDef](./type_defs.md#describeprotectedresourceoutputtypedef)
- [DescribeRecoveryPointOutputTypeDef](./type_defs.md#describerecoverypointoutputtypedef)
- [DescribeRegionSettingsOutputTypeDef](./type_defs.md#describeregionsettingsoutputtypedef)
- [DescribeRestoreJobOutputTypeDef](./type_defs.md#describerestorejoboutputtypedef)
- [ExportBackupPlanTemplateOutputTypeDef](./type_defs.md#exportbackupplantemplateoutputtypedef)
- [GetBackupPlanFromJSONOutputTypeDef](./type_defs.md#getbackupplanfromjsonoutputtypedef)
- [GetBackupPlanFromTemplateOutputTypeDef](./type_defs.md#getbackupplanfromtemplateoutputtypedef)
- [GetBackupPlanOutputTypeDef](./type_defs.md#getbackupplanoutputtypedef)
- [GetBackupSelectionOutputTypeDef](./type_defs.md#getbackupselectionoutputtypedef)
- [GetBackupVaultAccessPolicyOutputTypeDef](./type_defs.md#getbackupvaultaccesspolicyoutputtypedef)
- [GetBackupVaultNotificationsOutputTypeDef](./type_defs.md#getbackupvaultnotificationsoutputtypedef)
- [GetRecoveryPointRestoreMetadataOutputTypeDef](./type_defs.md#getrecoverypointrestoremetadataoutputtypedef)
- [GetSupportedResourceTypesOutputTypeDef](./type_defs.md#getsupportedresourcetypesoutputtypedef)
- [LifecycleTypeDef](./type_defs.md#lifecycletypedef)
- [ListBackupJobsOutputTypeDef](./type_defs.md#listbackupjobsoutputtypedef)
- [ListBackupPlanTemplatesOutputTypeDef](./type_defs.md#listbackupplantemplatesoutputtypedef)
- [ListBackupPlanVersionsOutputTypeDef](./type_defs.md#listbackupplanversionsoutputtypedef)
- [ListBackupPlansOutputTypeDef](./type_defs.md#listbackupplansoutputtypedef)
- [ListBackupSelectionsOutputTypeDef](./type_defs.md#listbackupselectionsoutputtypedef)
- [ListBackupVaultsOutputTypeDef](./type_defs.md#listbackupvaultsoutputtypedef)
- [ListCopyJobsOutputTypeDef](./type_defs.md#listcopyjobsoutputtypedef)
- [ListProtectedResourcesOutputTypeDef](./type_defs.md#listprotectedresourcesoutputtypedef)
- [ListRecoveryPointsByBackupVaultOutputTypeDef](./type_defs.md#listrecoverypointsbybackupvaultoutputtypedef)
- [ListRecoveryPointsByResourceOutputTypeDef](./type_defs.md#listrecoverypointsbyresourceoutputtypedef)
- [ListRestoreJobsOutputTypeDef](./type_defs.md#listrestorejobsoutputtypedef)
- [ListTagsOutputTypeDef](./type_defs.md#listtagsoutputtypedef)
- [ProtectedResourceTypeDef](./type_defs.md#protectedresourcetypedef)
- [RecoveryPointByBackupVaultTypeDef](./type_defs.md#recoverypointbybackupvaulttypedef)
- [RecoveryPointByResourceTypeDef](./type_defs.md#recoverypointbyresourcetypedef)
- [RecoveryPointCreatorTypeDef](./type_defs.md#recoverypointcreatortypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RestoreJobsListMemberTypeDef](./type_defs.md#restorejobslistmembertypedef)
- [StartBackupJobOutputTypeDef](./type_defs.md#startbackupjoboutputtypedef)
- [StartCopyJobOutputTypeDef](./type_defs.md#startcopyjoboutputtypedef)
- [StartRestoreJobOutputTypeDef](./type_defs.md#startrestorejoboutputtypedef)
- [UpdateBackupPlanOutputTypeDef](./type_defs.md#updatebackupplanoutputtypedef)
- [UpdateRecoveryPointLifecycleOutputTypeDef](./type_defs.md#updaterecoverypointlifecycleoutputtypedef)
