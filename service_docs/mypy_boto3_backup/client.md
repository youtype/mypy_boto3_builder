# BackupClient for boto3 Backup module

> [Index](../index.md) > [Backup](./index.md) > BackupClient

Auto-generated documentation for [Backup](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup)
type annotations stubs module [mypy_boto3_backup](https://pypi.org/project/mypy-boto3-backup/).

- [BackupClient for boto3 Backup module](#backupclient-for-boto3-backup-module)
  - [BackupClient](#backupclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_backup_plan](#create_backup_plan)
    - [create_backup_selection](#create_backup_selection)
    - [create_backup_vault](#create_backup_vault)
    - [delete_backup_plan](#delete_backup_plan)
    - [delete_backup_selection](#delete_backup_selection)
    - [delete_backup_vault](#delete_backup_vault)
    - [delete_backup_vault_access_policy](#delete_backup_vault_access_policy)
    - [delete_backup_vault_notifications](#delete_backup_vault_notifications)
    - [delete_recovery_point](#delete_recovery_point)
    - [describe_backup_job](#describe_backup_job)
    - [describe_backup_vault](#describe_backup_vault)
    - [describe_copy_job](#describe_copy_job)
    - [describe_global_settings](#describe_global_settings)
    - [describe_protected_resource](#describe_protected_resource)
    - [describe_recovery_point](#describe_recovery_point)
    - [describe_region_settings](#describe_region_settings)
    - [describe_restore_job](#describe_restore_job)
    - [disassociate_recovery_point](#disassociate_recovery_point)
    - [export_backup_plan_template](#export_backup_plan_template)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_backup_plan](#get_backup_plan)
    - [get_backup_plan_from_json](#get_backup_plan_from_json)
    - [get_backup_plan_from_template](#get_backup_plan_from_template)
    - [get_backup_selection](#get_backup_selection)
    - [get_backup_vault_access_policy](#get_backup_vault_access_policy)
    - [get_backup_vault_notifications](#get_backup_vault_notifications)
    - [get_recovery_point_restore_metadata](#get_recovery_point_restore_metadata)
    - [get_supported_resource_types](#get_supported_resource_types)
    - [list_backup_jobs](#list_backup_jobs)
    - [list_backup_plan_templates](#list_backup_plan_templates)
    - [list_backup_plan_versions](#list_backup_plan_versions)
    - [list_backup_plans](#list_backup_plans)
    - [list_backup_selections](#list_backup_selections)
    - [list_backup_vaults](#list_backup_vaults)
    - [list_copy_jobs](#list_copy_jobs)
    - [list_protected_resources](#list_protected_resources)
    - [list_recovery_points_by_backup_vault](#list_recovery_points_by_backup_vault)
    - [list_recovery_points_by_resource](#list_recovery_points_by_resource)
    - [list_restore_jobs](#list_restore_jobs)
    - [list_tags](#list_tags)
    - [put_backup_vault_access_policy](#put_backup_vault_access_policy)
    - [put_backup_vault_notifications](#put_backup_vault_notifications)
    - [start_backup_job](#start_backup_job)
    - [start_copy_job](#start_copy_job)
    - [start_restore_job](#start_restore_job)
    - [stop_backup_job](#stop_backup_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_backup_plan](#update_backup_plan)
    - [update_global_settings](#update_global_settings)
    - [update_recovery_point_lifecycle](#update_recovery_point_lifecycle)
    - [update_region_settings](#update_region_settings)

## BackupClient

Type annotations for `boto3.client("backup")`

Can be used directly:

```python
from mypy_boto3_backup.client import BackupClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_backup.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.ClientError`
- `Exceptions.DependencyFailureException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidResourceStateException`
- `Exceptions.LimitExceededException`
- `Exceptions.MissingParameterValueException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`


## Methods


### can_paginate

Type annotations for `boto3.client("backup").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_backup_plan

Type annotations for `boto3.client("backup").create_backup_plan` method.

[Client.create_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_backup_plan)

```python
def create_backup_plan(
    self,
    BackupPlan: BackupPlanInputTypeDef,
    BackupPlanTags: Dict[str, str] = None,
    CreatorRequestId: str = None
) -> CreateBackupPlanOutputTypeDef:
    pass
```

### create_backup_selection

Type annotations for `boto3.client("backup").create_backup_selection` method.

[Client.create_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_backup_selection)

```python
def create_backup_selection(
    self,
    BackupPlanId: str,
    BackupSelection: "BackupSelectionTypeDef",
    CreatorRequestId: str = None
) -> CreateBackupSelectionOutputTypeDef:
    pass
```

### create_backup_vault

Type annotations for `boto3.client("backup").create_backup_vault` method.

[Client.create_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.create_backup_vault)

```python
def create_backup_vault(
    self,
    BackupVaultName: str,
    BackupVaultTags: Dict[str, str] = None,
    EncryptionKeyArn: str = None,
    CreatorRequestId: str = None
) -> CreateBackupVaultOutputTypeDef:
    pass
```

### delete_backup_plan

Type annotations for `boto3.client("backup").delete_backup_plan` method.

[Client.delete_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_plan)

```python
def delete_backup_plan(
    self,
    BackupPlanId: str
) -> DeleteBackupPlanOutputTypeDef:
    pass
```

### delete_backup_selection

Type annotations for `boto3.client("backup").delete_backup_selection` method.

[Client.delete_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_selection)

```python
def delete_backup_selection(
    self,
    BackupPlanId: str,
    SelectionId: str
) -> None:
    pass
```

### delete_backup_vault

Type annotations for `boto3.client("backup").delete_backup_vault` method.

[Client.delete_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault)

```python
def delete_backup_vault(
    self,
    BackupVaultName: str
) -> None:
    pass
```

### delete_backup_vault_access_policy

Type annotations for `boto3.client("backup").delete_backup_vault_access_policy` method.

[Client.delete_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault_access_policy)

```python
def delete_backup_vault_access_policy(
    self,
    BackupVaultName: str
) -> None:
    pass
```

### delete_backup_vault_notifications

Type annotations for `boto3.client("backup").delete_backup_vault_notifications` method.

[Client.delete_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_backup_vault_notifications)

```python
def delete_backup_vault_notifications(
    self,
    BackupVaultName: str
) -> None:
    pass
```

### delete_recovery_point

Type annotations for `boto3.client("backup").delete_recovery_point` method.

[Client.delete_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.delete_recovery_point)

```python
def delete_recovery_point(
    self,
    BackupVaultName: str,
    RecoveryPointArn: str
) -> None:
    pass
```

### describe_backup_job

Type annotations for `boto3.client("backup").describe_backup_job` method.

[Client.describe_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_backup_job)

```python
def describe_backup_job(
    self,
    BackupJobId: str
) -> DescribeBackupJobOutputTypeDef:
    pass
```

### describe_backup_vault

Type annotations for `boto3.client("backup").describe_backup_vault` method.

[Client.describe_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_backup_vault)

```python
def describe_backup_vault(
    self,
    BackupVaultName: str
) -> DescribeBackupVaultOutputTypeDef:
    pass
```

### describe_copy_job

Type annotations for `boto3.client("backup").describe_copy_job` method.

[Client.describe_copy_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_copy_job)

```python
def describe_copy_job(
    self,
    CopyJobId: str
) -> DescribeCopyJobOutputTypeDef:
    pass
```

### describe_global_settings

Type annotations for `boto3.client("backup").describe_global_settings` method.

[Client.describe_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_global_settings)

```python
def describe_global_settings(
    self
) -> DescribeGlobalSettingsOutputTypeDef:
    pass
```

### describe_protected_resource

Type annotations for `boto3.client("backup").describe_protected_resource` method.

[Client.describe_protected_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_protected_resource)

```python
def describe_protected_resource(
    self,
    ResourceArn: str
) -> DescribeProtectedResourceOutputTypeDef:
    pass
```

### describe_recovery_point

Type annotations for `boto3.client("backup").describe_recovery_point` method.

[Client.describe_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_recovery_point)

```python
def describe_recovery_point(
    self,
    BackupVaultName: str,
    RecoveryPointArn: str
) -> DescribeRecoveryPointOutputTypeDef:
    pass
```

### describe_region_settings

Type annotations for `boto3.client("backup").describe_region_settings` method.

[Client.describe_region_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_region_settings)

```python
def describe_region_settings(
    self
) -> DescribeRegionSettingsOutputTypeDef:
    pass
```

### describe_restore_job

Type annotations for `boto3.client("backup").describe_restore_job` method.

[Client.describe_restore_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.describe_restore_job)

```python
def describe_restore_job(
    self,
    RestoreJobId: str
) -> DescribeRestoreJobOutputTypeDef:
    pass
```

### disassociate_recovery_point

Type annotations for `boto3.client("backup").disassociate_recovery_point` method.

[Client.disassociate_recovery_point documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.disassociate_recovery_point)

```python
def disassociate_recovery_point(
    self,
    BackupVaultName: str,
    RecoveryPointArn: str
) -> None:
    pass
```

### export_backup_plan_template

Type annotations for `boto3.client("backup").export_backup_plan_template` method.

[Client.export_backup_plan_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.export_backup_plan_template)

```python
def export_backup_plan_template(
    self,
    BackupPlanId: str
) -> ExportBackupPlanTemplateOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("backup").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.generate_presigned_url)

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

### get_backup_plan

Type annotations for `boto3.client("backup").get_backup_plan` method.

[Client.get_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_plan)

```python
def get_backup_plan(
    self,
    BackupPlanId: str,
    VersionId: str = None
) -> GetBackupPlanOutputTypeDef:
    pass
```

### get_backup_plan_from_json

Type annotations for `boto3.client("backup").get_backup_plan_from_json` method.

[Client.get_backup_plan_from_json documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_plan_from_json)

```python
def get_backup_plan_from_json(
    self,
    BackupPlanTemplateJson: str
) -> GetBackupPlanFromJSONOutputTypeDef:
    pass
```

### get_backup_plan_from_template

Type annotations for `boto3.client("backup").get_backup_plan_from_template` method.

[Client.get_backup_plan_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_plan_from_template)

```python
def get_backup_plan_from_template(
    self,
    BackupPlanTemplateId: str
) -> GetBackupPlanFromTemplateOutputTypeDef:
    pass
```

### get_backup_selection

Type annotations for `boto3.client("backup").get_backup_selection` method.

[Client.get_backup_selection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_selection)

```python
def get_backup_selection(
    self,
    BackupPlanId: str,
    SelectionId: str
) -> GetBackupSelectionOutputTypeDef:
    pass
```

### get_backup_vault_access_policy

Type annotations for `boto3.client("backup").get_backup_vault_access_policy` method.

[Client.get_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_vault_access_policy)

```python
def get_backup_vault_access_policy(
    self,
    BackupVaultName: str
) -> GetBackupVaultAccessPolicyOutputTypeDef:
    pass
```

### get_backup_vault_notifications

Type annotations for `boto3.client("backup").get_backup_vault_notifications` method.

[Client.get_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_backup_vault_notifications)

```python
def get_backup_vault_notifications(
    self,
    BackupVaultName: str
) -> GetBackupVaultNotificationsOutputTypeDef:
    pass
```

### get_recovery_point_restore_metadata

Type annotations for `boto3.client("backup").get_recovery_point_restore_metadata` method.

[Client.get_recovery_point_restore_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_recovery_point_restore_metadata)

```python
def get_recovery_point_restore_metadata(
    self,
    BackupVaultName: str,
    RecoveryPointArn: str
) -> GetRecoveryPointRestoreMetadataOutputTypeDef:
    pass
```

### get_supported_resource_types

Type annotations for `boto3.client("backup").get_supported_resource_types` method.

[Client.get_supported_resource_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.get_supported_resource_types)

```python
def get_supported_resource_types(
    self
) -> GetSupportedResourceTypesOutputTypeDef:
    pass
```

### list_backup_jobs

Type annotations for `boto3.client("backup").list_backup_jobs` method.

[Client.list_backup_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_jobs)

```python
def list_backup_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    ByResourceArn: str = None,
    ByState: BackupJobState = None,
    ByBackupVaultName: str = None,
    ByCreatedBefore: datetime = None,
    ByCreatedAfter: datetime = None,
    ByResourceType: str = None,
    ByAccountId: str = None
) -> ListBackupJobsOutputTypeDef:
    pass
```

### list_backup_plan_templates

Type annotations for `boto3.client("backup").list_backup_plan_templates` method.

[Client.list_backup_plan_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_plan_templates)

```python
def list_backup_plan_templates(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListBackupPlanTemplatesOutputTypeDef:
    pass
```

### list_backup_plan_versions

Type annotations for `boto3.client("backup").list_backup_plan_versions` method.

[Client.list_backup_plan_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_plan_versions)

```python
def list_backup_plan_versions(
    self,
    BackupPlanId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListBackupPlanVersionsOutputTypeDef:
    pass
```

### list_backup_plans

Type annotations for `boto3.client("backup").list_backup_plans` method.

[Client.list_backup_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_plans)

```python
def list_backup_plans(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    IncludeDeleted: bool = None
) -> ListBackupPlansOutputTypeDef:
    pass
```

### list_backup_selections

Type annotations for `boto3.client("backup").list_backup_selections` method.

[Client.list_backup_selections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_selections)

```python
def list_backup_selections(
    self,
    BackupPlanId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListBackupSelectionsOutputTypeDef:
    pass
```

### list_backup_vaults

Type annotations for `boto3.client("backup").list_backup_vaults` method.

[Client.list_backup_vaults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_backup_vaults)

```python
def list_backup_vaults(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListBackupVaultsOutputTypeDef:
    pass
```

### list_copy_jobs

Type annotations for `boto3.client("backup").list_copy_jobs` method.

[Client.list_copy_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_copy_jobs)

```python
def list_copy_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    ByResourceArn: str = None,
    ByState: CopyJobState = None,
    ByCreatedBefore: datetime = None,
    ByCreatedAfter: datetime = None,
    ByResourceType: str = None,
    ByDestinationVaultArn: str = None,
    ByAccountId: str = None
) -> ListCopyJobsOutputTypeDef:
    pass
```

### list_protected_resources

Type annotations for `boto3.client("backup").list_protected_resources` method.

[Client.list_protected_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_protected_resources)

```python
def list_protected_resources(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProtectedResourcesOutputTypeDef:
    pass
```

### list_recovery_points_by_backup_vault

Type annotations for `boto3.client("backup").list_recovery_points_by_backup_vault` method.

[Client.list_recovery_points_by_backup_vault documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_recovery_points_by_backup_vault)

```python
def list_recovery_points_by_backup_vault(
    self,
    BackupVaultName: str,
    NextToken: str = None,
    MaxResults: int = None,
    ByResourceArn: str = None,
    ByResourceType: str = None,
    ByBackupPlanId: str = None,
    ByCreatedBefore: datetime = None,
    ByCreatedAfter: datetime = None
) -> ListRecoveryPointsByBackupVaultOutputTypeDef:
    pass
```

### list_recovery_points_by_resource

Type annotations for `boto3.client("backup").list_recovery_points_by_resource` method.

[Client.list_recovery_points_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_recovery_points_by_resource)

```python
def list_recovery_points_by_resource(
    self,
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRecoveryPointsByResourceOutputTypeDef:
    pass
```

### list_restore_jobs

Type annotations for `boto3.client("backup").list_restore_jobs` method.

[Client.list_restore_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_restore_jobs)

```python
def list_restore_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    ByAccountId: str = None,
    ByCreatedBefore: datetime = None,
    ByCreatedAfter: datetime = None,
    ByStatus: RestoreJobStatus = None
) -> ListRestoreJobsOutputTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("backup").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.list_tags)

```python
def list_tags(
    self,
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsOutputTypeDef:
    pass
```

### put_backup_vault_access_policy

Type annotations for `boto3.client("backup").put_backup_vault_access_policy` method.

[Client.put_backup_vault_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.put_backup_vault_access_policy)

```python
def put_backup_vault_access_policy(
    self,
    BackupVaultName: str,
    Policy: str = None
) -> None:
    pass
```

### put_backup_vault_notifications

Type annotations for `boto3.client("backup").put_backup_vault_notifications` method.

[Client.put_backup_vault_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.put_backup_vault_notifications)

```python
def put_backup_vault_notifications(
    self,
    BackupVaultName: str,
    SNSTopicArn: str,
    BackupVaultEvents: List[BackupVaultEvent]
) -> None:
    pass
```

### start_backup_job

Type annotations for `boto3.client("backup").start_backup_job` method.

[Client.start_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_backup_job)

```python
def start_backup_job(
    self,
    BackupVaultName: str,
    ResourceArn: str,
    IamRoleArn: str,
    IdempotencyToken: str = None,
    StartWindowMinutes: int = None,
    CompleteWindowMinutes: int = None,
    Lifecycle: "LifecycleTypeDef" = None,
    RecoveryPointTags: Dict[str, str] = None,
    BackupOptions: Dict[str, str] = None
) -> StartBackupJobOutputTypeDef:
    pass
```

### start_copy_job

Type annotations for `boto3.client("backup").start_copy_job` method.

[Client.start_copy_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_copy_job)

```python
def start_copy_job(
    self,
    RecoveryPointArn: str,
    SourceBackupVaultName: str,
    DestinationBackupVaultArn: str,
    IamRoleArn: str,
    IdempotencyToken: str = None,
    Lifecycle: "LifecycleTypeDef" = None
) -> StartCopyJobOutputTypeDef:
    pass
```

### start_restore_job

Type annotations for `boto3.client("backup").start_restore_job` method.

[Client.start_restore_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.start_restore_job)

```python
def start_restore_job(
    self,
    RecoveryPointArn: str,
    Metadata: Dict[str, str],
    IamRoleArn: str,
    IdempotencyToken: str = None,
    ResourceType: str = None
) -> StartRestoreJobOutputTypeDef:
    pass
```

### stop_backup_job

Type annotations for `boto3.client("backup").stop_backup_job` method.

[Client.stop_backup_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.stop_backup_job)

```python
def stop_backup_job(
    self,
    BackupJobId: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("backup").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("backup").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeyList: List[str]
) -> None:
    pass
```

### update_backup_plan

Type annotations for `boto3.client("backup").update_backup_plan` method.

[Client.update_backup_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_backup_plan)

```python
def update_backup_plan(
    self,
    BackupPlanId: str,
    BackupPlan: BackupPlanInputTypeDef
) -> UpdateBackupPlanOutputTypeDef:
    pass
```

### update_global_settings

Type annotations for `boto3.client("backup").update_global_settings` method.

[Client.update_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_global_settings)

```python
def update_global_settings(
    self,
    GlobalSettings: Dict[str, str] = None
) -> None:
    pass
```

### update_recovery_point_lifecycle

Type annotations for `boto3.client("backup").update_recovery_point_lifecycle` method.

[Client.update_recovery_point_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_recovery_point_lifecycle)

```python
def update_recovery_point_lifecycle(
    self,
    BackupVaultName: str,
    RecoveryPointArn: str,
    Lifecycle: "LifecycleTypeDef" = None
) -> UpdateRecoveryPointLifecycleOutputTypeDef:
    pass
```

### update_region_settings

Type annotations for `boto3.client("backup").update_region_settings` method.

[Client.update_region_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup.Client.update_region_settings)

```python
def update_region_settings(
    self,
    ResourceTypeOptInPreference: Dict[str, bool] = None
) -> None:
    pass
```