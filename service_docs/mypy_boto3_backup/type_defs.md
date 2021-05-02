# Structures for boto3 Backup module

> [Index](../index.md) > [Backup](./index.md) > Structures

Auto-generated documentation for [Backup](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup)
type annotations stubs module [mypy_boto3_backup](https://pypi.org/project/mypy-boto3-backup/).

- [Structures for boto3 Backup module](#structures-for-boto3-backup-module)
  - [AdvancedBackupSettingTypeDef](#advancedbackupsettingtypedef)
  - [BackupJobTypeDef](#backupjobtypedef)
  - [BackupPlanTemplatesListMemberTypeDef](#backupplantemplateslistmembertypedef)
  - [BackupPlanTypeDef](#backupplantypedef)
  - [BackupPlansListMemberTypeDef](#backupplanslistmembertypedef)
  - [BackupRuleInputTypeDef](#backupruleinputtypedef)
  - [BackupRuleTypeDef](#backupruletypedef)
  - [BackupSelectionTypeDef](#backupselectiontypedef)
  - [BackupSelectionsListMemberTypeDef](#backupselectionslistmembertypedef)
  - [BackupVaultListMemberTypeDef](#backupvaultlistmembertypedef)
  - [CalculatedLifecycleTypeDef](#calculatedlifecycletypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [CopyActionTypeDef](#copyactiontypedef)
  - [CopyJobTypeDef](#copyjobtypedef)
  - [LifecycleTypeDef](#lifecycletypedef)
  - [ProtectedResourceTypeDef](#protectedresourcetypedef)
  - [RecoveryPointByBackupVaultTypeDef](#recoverypointbybackupvaulttypedef)
  - [RecoveryPointByResourceTypeDef](#recoverypointbyresourcetypedef)
  - [RecoveryPointCreatorTypeDef](#recoverypointcreatortypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RestoreJobsListMemberTypeDef](#restorejobslistmembertypedef)
  - [BackupPlanInputTypeDef](#backupplaninputtypedef)
  - [CreateBackupPlanOutputTypeDef](#createbackupplanoutputtypedef)
  - [CreateBackupSelectionOutputTypeDef](#createbackupselectionoutputtypedef)
  - [CreateBackupVaultOutputTypeDef](#createbackupvaultoutputtypedef)
  - [DeleteBackupPlanOutputTypeDef](#deletebackupplanoutputtypedef)
  - [DescribeBackupJobOutputTypeDef](#describebackupjoboutputtypedef)
  - [DescribeBackupVaultOutputTypeDef](#describebackupvaultoutputtypedef)
  - [DescribeCopyJobOutputTypeDef](#describecopyjoboutputtypedef)
  - [DescribeGlobalSettingsOutputTypeDef](#describeglobalsettingsoutputtypedef)
  - [DescribeProtectedResourceOutputTypeDef](#describeprotectedresourceoutputtypedef)
  - [DescribeRecoveryPointOutputTypeDef](#describerecoverypointoutputtypedef)
  - [DescribeRegionSettingsOutputTypeDef](#describeregionsettingsoutputtypedef)
  - [DescribeRestoreJobOutputTypeDef](#describerestorejoboutputtypedef)
  - [ExportBackupPlanTemplateOutputTypeDef](#exportbackupplantemplateoutputtypedef)
  - [GetBackupPlanFromJSONOutputTypeDef](#getbackupplanfromjsonoutputtypedef)
  - [GetBackupPlanFromTemplateOutputTypeDef](#getbackupplanfromtemplateoutputtypedef)
  - [GetBackupPlanOutputTypeDef](#getbackupplanoutputtypedef)
  - [GetBackupSelectionOutputTypeDef](#getbackupselectionoutputtypedef)
  - [GetBackupVaultAccessPolicyOutputTypeDef](#getbackupvaultaccesspolicyoutputtypedef)
  - [GetBackupVaultNotificationsOutputTypeDef](#getbackupvaultnotificationsoutputtypedef)
  - [GetRecoveryPointRestoreMetadataOutputTypeDef](#getrecoverypointrestoremetadataoutputtypedef)
  - [GetSupportedResourceTypesOutputTypeDef](#getsupportedresourcetypesoutputtypedef)
  - [ListBackupJobsOutputTypeDef](#listbackupjobsoutputtypedef)
  - [ListBackupPlanTemplatesOutputTypeDef](#listbackupplantemplatesoutputtypedef)
  - [ListBackupPlanVersionsOutputTypeDef](#listbackupplanversionsoutputtypedef)
  - [ListBackupPlansOutputTypeDef](#listbackupplansoutputtypedef)
  - [ListBackupSelectionsOutputTypeDef](#listbackupselectionsoutputtypedef)
  - [ListBackupVaultsOutputTypeDef](#listbackupvaultsoutputtypedef)
  - [ListCopyJobsOutputTypeDef](#listcopyjobsoutputtypedef)
  - [ListProtectedResourcesOutputTypeDef](#listprotectedresourcesoutputtypedef)
  - [ListRecoveryPointsByBackupVaultOutputTypeDef](#listrecoverypointsbybackupvaultoutputtypedef)
  - [ListRecoveryPointsByResourceOutputTypeDef](#listrecoverypointsbyresourceoutputtypedef)
  - [ListRestoreJobsOutputTypeDef](#listrestorejobsoutputtypedef)
  - [ListTagsOutputTypeDef](#listtagsoutputtypedef)
  - [StartBackupJobOutputTypeDef](#startbackupjoboutputtypedef)
  - [StartCopyJobOutputTypeDef](#startcopyjoboutputtypedef)
  - [StartRestoreJobOutputTypeDef](#startrestorejoboutputtypedef)
  - [UpdateBackupPlanOutputTypeDef](#updatebackupplanoutputtypedef)
  - [UpdateRecoveryPointLifecycleOutputTypeDef](#updaterecoverypointlifecycleoutputtypedef)

## AdvancedBackupSettingTypeDef

```python
from mypy_boto3_backup.type_defs import AdvancedBackupSettingTypeDef
```




Optional fields:
- `ResourceType`: `str`
- `BackupOptions`: `Dict[str, str]`


## BackupJobTypeDef

```python
from mypy_boto3_backup.type_defs import BackupJobTypeDef
```




Optional fields:
- `AccountId`: `str`
- `BackupJobId`: `str`
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `RecoveryPointArn`: `str`
- `ResourceArn`: `str`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `State`: `BackupJobState`
- `StatusMessage`: `str`
- `PercentDone`: `str`
- `BackupSizeInBytes`: `int`
- `IamRoleArn`: `str`
- `CreatedBy`: `"RecoveryPointCreatorTypeDef"`
- `ExpectedCompletionDate`: `datetime`
- `StartBy`: `datetime`
- `ResourceType`: `str`
- `BytesTransferred`: `int`
- `BackupOptions`: `Dict[str, str]`
- `BackupType`: `str`


## BackupPlanTemplatesListMemberTypeDef

```python
from mypy_boto3_backup.type_defs import BackupPlanTemplatesListMemberTypeDef
```




Optional fields:
- `BackupPlanTemplateId`: `str`
- `BackupPlanTemplateName`: `str`


## BackupPlanTypeDef

```python
from mypy_boto3_backup.type_defs import BackupPlanTypeDef
```


Required fields:
- `BackupPlanName`: `str`
- `Rules`: `List["BackupRuleTypeDef"]`



Optional fields:
- `AdvancedBackupSettings`: `List["AdvancedBackupSettingTypeDef"]`


## BackupPlansListMemberTypeDef

```python
from mypy_boto3_backup.type_defs import BackupPlansListMemberTypeDef
```




Optional fields:
- `BackupPlanArn`: `str`
- `BackupPlanId`: `str`
- `CreationDate`: `datetime`
- `DeletionDate`: `datetime`
- `VersionId`: `str`
- `BackupPlanName`: `str`
- `CreatorRequestId`: `str`
- `LastExecutionDate`: `datetime`
- `AdvancedBackupSettings`: `List["AdvancedBackupSettingTypeDef"]`


## BackupRuleInputTypeDef

```python
from mypy_boto3_backup.type_defs import BackupRuleInputTypeDef
```


Required fields:
- `RuleName`: `str`
- `TargetBackupVaultName`: `str`



Optional fields:
- `ScheduleExpression`: `str`
- `StartWindowMinutes`: `int`
- `CompletionWindowMinutes`: `int`
- `Lifecycle`: `"LifecycleTypeDef"`
- `RecoveryPointTags`: `Dict[str, str]`
- `CopyActions`: `List["CopyActionTypeDef"]`
- `EnableContinuousBackup`: `bool`


## BackupRuleTypeDef

```python
from mypy_boto3_backup.type_defs import BackupRuleTypeDef
```


Required fields:
- `RuleName`: `str`
- `TargetBackupVaultName`: `str`



Optional fields:
- `ScheduleExpression`: `str`
- `StartWindowMinutes`: `int`
- `CompletionWindowMinutes`: `int`
- `Lifecycle`: `"LifecycleTypeDef"`
- `RecoveryPointTags`: `Dict[str, str]`
- `RuleId`: `str`
- `CopyActions`: `List["CopyActionTypeDef"]`
- `EnableContinuousBackup`: `bool`


## BackupSelectionTypeDef

```python
from mypy_boto3_backup.type_defs import BackupSelectionTypeDef
```


Required fields:
- `SelectionName`: `str`
- `IamRoleArn`: `str`



Optional fields:
- `Resources`: `List[str]`
- `ListOfTags`: `List["ConditionTypeDef"]`


## BackupSelectionsListMemberTypeDef

```python
from mypy_boto3_backup.type_defs import BackupSelectionsListMemberTypeDef
```




Optional fields:
- `SelectionId`: `str`
- `SelectionName`: `str`
- `BackupPlanId`: `str`
- `CreationDate`: `datetime`
- `CreatorRequestId`: `str`
- `IamRoleArn`: `str`


## BackupVaultListMemberTypeDef

```python
from mypy_boto3_backup.type_defs import BackupVaultListMemberTypeDef
```




Optional fields:
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `CreationDate`: `datetime`
- `EncryptionKeyArn`: `str`
- `CreatorRequestId`: `str`
- `NumberOfRecoveryPoints`: `int`


## CalculatedLifecycleTypeDef

```python
from mypy_boto3_backup.type_defs import CalculatedLifecycleTypeDef
```




Optional fields:
- `MoveToColdStorageAt`: `datetime`
- `DeleteAt`: `datetime`


## ConditionTypeDef

```python
from mypy_boto3_backup.type_defs import ConditionTypeDef
```


Required fields:
- `ConditionType`: `ConditionType`
- `ConditionKey`: `str`
- `ConditionValue`: `str`




## CopyActionTypeDef

```python
from mypy_boto3_backup.type_defs import CopyActionTypeDef
```


Required fields:
- `DestinationBackupVaultArn`: `str`



Optional fields:
- `Lifecycle`: `"LifecycleTypeDef"`


## CopyJobTypeDef

```python
from mypy_boto3_backup.type_defs import CopyJobTypeDef
```




Optional fields:
- `AccountId`: `str`
- `CopyJobId`: `str`
- `SourceBackupVaultArn`: `str`
- `SourceRecoveryPointArn`: `str`
- `DestinationBackupVaultArn`: `str`
- `DestinationRecoveryPointArn`: `str`
- `ResourceArn`: `str`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `State`: `CopyJobState`
- `StatusMessage`: `str`
- `BackupSizeInBytes`: `int`
- `IamRoleArn`: `str`
- `CreatedBy`: `"RecoveryPointCreatorTypeDef"`
- `ResourceType`: `str`


## LifecycleTypeDef

```python
from mypy_boto3_backup.type_defs import LifecycleTypeDef
```




Optional fields:
- `MoveToColdStorageAfterDays`: `int`
- `DeleteAfterDays`: `int`


## ProtectedResourceTypeDef

```python
from mypy_boto3_backup.type_defs import ProtectedResourceTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceType`: `str`
- `LastBackupTime`: `datetime`


## RecoveryPointByBackupVaultTypeDef

```python
from mypy_boto3_backup.type_defs import RecoveryPointByBackupVaultTypeDef
```




Optional fields:
- `RecoveryPointArn`: `str`
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `SourceBackupVaultArn`: `str`
- `ResourceArn`: `str`
- `ResourceType`: `str`
- `CreatedBy`: `"RecoveryPointCreatorTypeDef"`
- `IamRoleArn`: `str`
- `Status`: `RecoveryPointStatus`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `BackupSizeInBytes`: `int`
- `CalculatedLifecycle`: `"CalculatedLifecycleTypeDef"`
- `Lifecycle`: `"LifecycleTypeDef"`
- `EncryptionKeyArn`: `str`
- `IsEncrypted`: `bool`
- `LastRestoreTime`: `datetime`


## RecoveryPointByResourceTypeDef

```python
from mypy_boto3_backup.type_defs import RecoveryPointByResourceTypeDef
```




Optional fields:
- `RecoveryPointArn`: `str`
- `CreationDate`: `datetime`
- `Status`: `RecoveryPointStatus`
- `EncryptionKeyArn`: `str`
- `BackupSizeBytes`: `int`
- `BackupVaultName`: `str`


## RecoveryPointCreatorTypeDef

```python
from mypy_boto3_backup.type_defs import RecoveryPointCreatorTypeDef
```




Optional fields:
- `BackupPlanId`: `str`
- `BackupPlanArn`: `str`
- `BackupPlanVersion`: `str`
- `BackupRuleId`: `str`


## ResponseMetadata

```python
from mypy_boto3_backup.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RestoreJobsListMemberTypeDef

```python
from mypy_boto3_backup.type_defs import RestoreJobsListMemberTypeDef
```




Optional fields:
- `AccountId`: `str`
- `RestoreJobId`: `str`
- `RecoveryPointArn`: `str`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `Status`: `RestoreJobStatus`
- `StatusMessage`: `str`
- `PercentDone`: `str`
- `BackupSizeInBytes`: `int`
- `IamRoleArn`: `str`
- `ExpectedCompletionTimeMinutes`: `int`
- `CreatedResourceArn`: `str`
- `ResourceType`: `str`


## BackupPlanInputTypeDef

```python
from mypy_boto3_backup.type_defs import BackupPlanInputTypeDef
```


Required fields:
- `BackupPlanName`: `str`
- `Rules`: `List["BackupRuleInputTypeDef"]`



Optional fields:
- `AdvancedBackupSettings`: `List["AdvancedBackupSettingTypeDef"]`


## CreateBackupPlanOutputTypeDef

```python
from mypy_boto3_backup.type_defs import CreateBackupPlanOutputTypeDef
```




Optional fields:
- `BackupPlanId`: `str`
- `BackupPlanArn`: `str`
- `CreationDate`: `datetime`
- `VersionId`: `str`
- `AdvancedBackupSettings`: `List["AdvancedBackupSettingTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateBackupSelectionOutputTypeDef

```python
from mypy_boto3_backup.type_defs import CreateBackupSelectionOutputTypeDef
```




Optional fields:
- `SelectionId`: `str`
- `BackupPlanId`: `str`
- `CreationDate`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateBackupVaultOutputTypeDef

```python
from mypy_boto3_backup.type_defs import CreateBackupVaultOutputTypeDef
```




Optional fields:
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `CreationDate`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteBackupPlanOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DeleteBackupPlanOutputTypeDef
```




Optional fields:
- `BackupPlanId`: `str`
- `BackupPlanArn`: `str`
- `DeletionDate`: `datetime`
- `VersionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeBackupJobOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeBackupJobOutputTypeDef
```




Optional fields:
- `AccountId`: `str`
- `BackupJobId`: `str`
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `RecoveryPointArn`: `str`
- `ResourceArn`: `str`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `State`: `BackupJobState`
- `StatusMessage`: `str`
- `PercentDone`: `str`
- `BackupSizeInBytes`: `int`
- `IamRoleArn`: `str`
- `CreatedBy`: `"RecoveryPointCreatorTypeDef"`
- `ResourceType`: `str`
- `BytesTransferred`: `int`
- `ExpectedCompletionDate`: `datetime`
- `StartBy`: `datetime`
- `BackupOptions`: `Dict[str, str]`
- `BackupType`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeBackupVaultOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeBackupVaultOutputTypeDef
```




Optional fields:
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `EncryptionKeyArn`: `str`
- `CreationDate`: `datetime`
- `CreatorRequestId`: `str`
- `NumberOfRecoveryPoints`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeCopyJobOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeCopyJobOutputTypeDef
```




Optional fields:
- `CopyJob`: `"CopyJobTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGlobalSettingsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeGlobalSettingsOutputTypeDef
```




Optional fields:
- `GlobalSettings`: `Dict[str, str]`
- `LastUpdateTime`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProtectedResourceOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeProtectedResourceOutputTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceType`: `str`
- `LastBackupTime`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRecoveryPointOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeRecoveryPointOutputTypeDef
```




Optional fields:
- `RecoveryPointArn`: `str`
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `SourceBackupVaultArn`: `str`
- `ResourceArn`: `str`
- `ResourceType`: `str`
- `CreatedBy`: `"RecoveryPointCreatorTypeDef"`
- `IamRoleArn`: `str`
- `Status`: `RecoveryPointStatus`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `BackupSizeInBytes`: `int`
- `CalculatedLifecycle`: `"CalculatedLifecycleTypeDef"`
- `Lifecycle`: `"LifecycleTypeDef"`
- `EncryptionKeyArn`: `str`
- `IsEncrypted`: `bool`
- `StorageClass`: `StorageClass`
- `LastRestoreTime`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRegionSettingsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeRegionSettingsOutputTypeDef
```




Optional fields:
- `ResourceTypeOptInPreference`: `Dict[str, bool]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRestoreJobOutputTypeDef

```python
from mypy_boto3_backup.type_defs import DescribeRestoreJobOutputTypeDef
```




Optional fields:
- `AccountId`: `str`
- `RestoreJobId`: `str`
- `RecoveryPointArn`: `str`
- `CreationDate`: `datetime`
- `CompletionDate`: `datetime`
- `Status`: `RestoreJobStatus`
- `StatusMessage`: `str`
- `PercentDone`: `str`
- `BackupSizeInBytes`: `int`
- `IamRoleArn`: `str`
- `ExpectedCompletionTimeMinutes`: `int`
- `CreatedResourceArn`: `str`
- `ResourceType`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ExportBackupPlanTemplateOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ExportBackupPlanTemplateOutputTypeDef
```




Optional fields:
- `BackupPlanTemplateJson`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBackupPlanFromJSONOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetBackupPlanFromJSONOutputTypeDef
```




Optional fields:
- `BackupPlan`: `"BackupPlanTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBackupPlanFromTemplateOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetBackupPlanFromTemplateOutputTypeDef
```




Optional fields:
- `BackupPlanDocument`: `"BackupPlanTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBackupPlanOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetBackupPlanOutputTypeDef
```




Optional fields:
- `BackupPlan`: `"BackupPlanTypeDef"`
- `BackupPlanId`: `str`
- `BackupPlanArn`: `str`
- `VersionId`: `str`
- `CreatorRequestId`: `str`
- `CreationDate`: `datetime`
- `DeletionDate`: `datetime`
- `LastExecutionDate`: `datetime`
- `AdvancedBackupSettings`: `List["AdvancedBackupSettingTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBackupSelectionOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetBackupSelectionOutputTypeDef
```




Optional fields:
- `BackupSelection`: `"BackupSelectionTypeDef"`
- `SelectionId`: `str`
- `BackupPlanId`: `str`
- `CreationDate`: `datetime`
- `CreatorRequestId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBackupVaultAccessPolicyOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetBackupVaultAccessPolicyOutputTypeDef
```




Optional fields:
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `Policy`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBackupVaultNotificationsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetBackupVaultNotificationsOutputTypeDef
```




Optional fields:
- `BackupVaultName`: `str`
- `BackupVaultArn`: `str`
- `SNSTopicArn`: `str`
- `BackupVaultEvents`: `List[BackupVaultEvent]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetRecoveryPointRestoreMetadataOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetRecoveryPointRestoreMetadataOutputTypeDef
```




Optional fields:
- `BackupVaultArn`: `str`
- `RecoveryPointArn`: `str`
- `RestoreMetadata`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetSupportedResourceTypesOutputTypeDef

```python
from mypy_boto3_backup.type_defs import GetSupportedResourceTypesOutputTypeDef
```




Optional fields:
- `ResourceTypes`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupJobsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListBackupJobsOutputTypeDef
```




Optional fields:
- `BackupJobs`: `List["BackupJobTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupPlanTemplatesOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListBackupPlanTemplatesOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `BackupPlanTemplatesList`: `List["BackupPlanTemplatesListMemberTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupPlanVersionsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListBackupPlanVersionsOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `BackupPlanVersionsList`: `List["BackupPlansListMemberTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupPlansOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListBackupPlansOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `BackupPlansList`: `List["BackupPlansListMemberTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupSelectionsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListBackupSelectionsOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `BackupSelectionsList`: `List["BackupSelectionsListMemberTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBackupVaultsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListBackupVaultsOutputTypeDef
```




Optional fields:
- `BackupVaultList`: `List["BackupVaultListMemberTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListCopyJobsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListCopyJobsOutputTypeDef
```




Optional fields:
- `CopyJobs`: `List["CopyJobTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProtectedResourcesOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListProtectedResourcesOutputTypeDef
```




Optional fields:
- `Results`: `List["ProtectedResourceTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRecoveryPointsByBackupVaultOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListRecoveryPointsByBackupVaultOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `RecoveryPoints`: `List["RecoveryPointByBackupVaultTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRecoveryPointsByResourceOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListRecoveryPointsByResourceOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `RecoveryPoints`: `List["RecoveryPointByResourceTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRestoreJobsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListRestoreJobsOutputTypeDef
```




Optional fields:
- `RestoreJobs`: `List["RestoreJobsListMemberTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsOutputTypeDef

```python
from mypy_boto3_backup.type_defs import ListTagsOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartBackupJobOutputTypeDef

```python
from mypy_boto3_backup.type_defs import StartBackupJobOutputTypeDef
```




Optional fields:
- `BackupJobId`: `str`
- `RecoveryPointArn`: `str`
- `CreationDate`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartCopyJobOutputTypeDef

```python
from mypy_boto3_backup.type_defs import StartCopyJobOutputTypeDef
```




Optional fields:
- `CopyJobId`: `str`
- `CreationDate`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartRestoreJobOutputTypeDef

```python
from mypy_boto3_backup.type_defs import StartRestoreJobOutputTypeDef
```




Optional fields:
- `RestoreJobId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateBackupPlanOutputTypeDef

```python
from mypy_boto3_backup.type_defs import UpdateBackupPlanOutputTypeDef
```




Optional fields:
- `BackupPlanId`: `str`
- `BackupPlanArn`: `str`
- `CreationDate`: `datetime`
- `VersionId`: `str`
- `AdvancedBackupSettings`: `List["AdvancedBackupSettingTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateRecoveryPointLifecycleOutputTypeDef

```python
from mypy_boto3_backup.type_defs import UpdateRecoveryPointLifecycleOutputTypeDef
```




Optional fields:
- `BackupVaultArn`: `str`
- `RecoveryPointArn`: `str`
- `Lifecycle`: `"LifecycleTypeDef"`
- `CalculatedLifecycle`: `"CalculatedLifecycleTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`

