# SSMClient for boto3 SSM module

> [Index](../index.md) > [SSM](./index.md) > SSMClient

Auto-generated documentation for [SSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM)
type annotations stubs module [mypy_boto3_ssm](https://pypi.org/project/mypy-boto3-ssm/).

- [SSMClient for boto3 SSM module](#ssmclient-for-boto3-ssm-module)
  - [SSMClient](#ssmclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [can_paginate](#can_paginate)
    - [cancel_command](#cancel_command)
    - [cancel_maintenance_window_execution](#cancel_maintenance_window_execution)
    - [create_activation](#create_activation)
    - [create_association](#create_association)
    - [create_association_batch](#create_association_batch)
    - [create_document](#create_document)
    - [create_maintenance_window](#create_maintenance_window)
    - [create_ops_item](#create_ops_item)
    - [create_ops_metadata](#create_ops_metadata)
    - [create_patch_baseline](#create_patch_baseline)
    - [create_resource_data_sync](#create_resource_data_sync)
    - [delete_activation](#delete_activation)
    - [delete_association](#delete_association)
    - [delete_document](#delete_document)
    - [delete_inventory](#delete_inventory)
    - [delete_maintenance_window](#delete_maintenance_window)
    - [delete_ops_metadata](#delete_ops_metadata)
    - [delete_parameter](#delete_parameter)
    - [delete_parameters](#delete_parameters)
    - [delete_patch_baseline](#delete_patch_baseline)
    - [delete_resource_data_sync](#delete_resource_data_sync)
    - [deregister_managed_instance](#deregister_managed_instance)
    - [deregister_patch_baseline_for_patch_group](#deregister_patch_baseline_for_patch_group)
    - [deregister_target_from_maintenance_window](#deregister_target_from_maintenance_window)
    - [deregister_task_from_maintenance_window](#deregister_task_from_maintenance_window)
    - [describe_activations](#describe_activations)
    - [describe_association](#describe_association)
    - [describe_association_execution_targets](#describe_association_execution_targets)
    - [describe_association_executions](#describe_association_executions)
    - [describe_automation_executions](#describe_automation_executions)
    - [describe_automation_step_executions](#describe_automation_step_executions)
    - [describe_available_patches](#describe_available_patches)
    - [describe_document](#describe_document)
    - [describe_document_permission](#describe_document_permission)
    - [describe_effective_instance_associations](#describe_effective_instance_associations)
    - [describe_effective_patches_for_patch_baseline](#describe_effective_patches_for_patch_baseline)
    - [describe_instance_associations_status](#describe_instance_associations_status)
    - [describe_instance_information](#describe_instance_information)
    - [describe_instance_patch_states](#describe_instance_patch_states)
    - [describe_instance_patch_states_for_patch_group](#describe_instance_patch_states_for_patch_group)
    - [describe_instance_patches](#describe_instance_patches)
    - [describe_inventory_deletions](#describe_inventory_deletions)
    - [describe_maintenance_window_execution_task_invocations](#describe_maintenance_window_execution_task_invocations)
    - [describe_maintenance_window_execution_tasks](#describe_maintenance_window_execution_tasks)
    - [describe_maintenance_window_executions](#describe_maintenance_window_executions)
    - [describe_maintenance_window_schedule](#describe_maintenance_window_schedule)
    - [describe_maintenance_window_targets](#describe_maintenance_window_targets)
    - [describe_maintenance_window_tasks](#describe_maintenance_window_tasks)
    - [describe_maintenance_windows](#describe_maintenance_windows)
    - [describe_maintenance_windows_for_target](#describe_maintenance_windows_for_target)
    - [describe_ops_items](#describe_ops_items)
    - [describe_parameters](#describe_parameters)
    - [describe_patch_baselines](#describe_patch_baselines)
    - [describe_patch_group_state](#describe_patch_group_state)
    - [describe_patch_groups](#describe_patch_groups)
    - [describe_patch_properties](#describe_patch_properties)
    - [describe_sessions](#describe_sessions)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_automation_execution](#get_automation_execution)
    - [get_calendar_state](#get_calendar_state)
    - [get_command_invocation](#get_command_invocation)
    - [get_connection_status](#get_connection_status)
    - [get_default_patch_baseline](#get_default_patch_baseline)
    - [get_deployable_patch_snapshot_for_instance](#get_deployable_patch_snapshot_for_instance)
    - [get_document](#get_document)
    - [get_inventory](#get_inventory)
    - [get_inventory_schema](#get_inventory_schema)
    - [get_maintenance_window](#get_maintenance_window)
    - [get_maintenance_window_execution](#get_maintenance_window_execution)
    - [get_maintenance_window_execution_task](#get_maintenance_window_execution_task)
    - [get_maintenance_window_execution_task_invocation](#get_maintenance_window_execution_task_invocation)
    - [get_maintenance_window_task](#get_maintenance_window_task)
    - [get_ops_item](#get_ops_item)
    - [get_ops_metadata](#get_ops_metadata)
    - [get_ops_summary](#get_ops_summary)
    - [get_parameter](#get_parameter)
    - [get_parameter_history](#get_parameter_history)
    - [get_parameters](#get_parameters)
    - [get_parameters_by_path](#get_parameters_by_path)
    - [get_patch_baseline](#get_patch_baseline)
    - [get_patch_baseline_for_patch_group](#get_patch_baseline_for_patch_group)
    - [get_service_setting](#get_service_setting)
    - [label_parameter_version](#label_parameter_version)
    - [list_association_versions](#list_association_versions)
    - [list_associations](#list_associations)
    - [list_command_invocations](#list_command_invocations)
    - [list_commands](#list_commands)
    - [list_compliance_items](#list_compliance_items)
    - [list_compliance_summaries](#list_compliance_summaries)
    - [list_document_metadata_history](#list_document_metadata_history)
    - [list_document_versions](#list_document_versions)
    - [list_documents](#list_documents)
    - [list_inventory_entries](#list_inventory_entries)
    - [list_ops_item_events](#list_ops_item_events)
    - [list_ops_metadata](#list_ops_metadata)
    - [list_resource_compliance_summaries](#list_resource_compliance_summaries)
    - [list_resource_data_sync](#list_resource_data_sync)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_document_permission](#modify_document_permission)
    - [put_compliance_items](#put_compliance_items)
    - [put_inventory](#put_inventory)
    - [put_parameter](#put_parameter)
    - [register_default_patch_baseline](#register_default_patch_baseline)
    - [register_patch_baseline_for_patch_group](#register_patch_baseline_for_patch_group)
    - [register_target_with_maintenance_window](#register_target_with_maintenance_window)
    - [register_task_with_maintenance_window](#register_task_with_maintenance_window)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [reset_service_setting](#reset_service_setting)
    - [resume_session](#resume_session)
    - [send_automation_signal](#send_automation_signal)
    - [send_command](#send_command)
    - [start_associations_once](#start_associations_once)
    - [start_automation_execution](#start_automation_execution)
    - [start_change_request_execution](#start_change_request_execution)
    - [start_session](#start_session)
    - [stop_automation_execution](#stop_automation_execution)
    - [terminate_session](#terminate_session)
    - [unlabel_parameter_version](#unlabel_parameter_version)
    - [update_association](#update_association)
    - [update_association_status](#update_association_status)
    - [update_document](#update_document)
    - [update_document_default_version](#update_document_default_version)
    - [update_document_metadata](#update_document_metadata)
    - [update_maintenance_window](#update_maintenance_window)
    - [update_maintenance_window_target](#update_maintenance_window_target)
    - [update_maintenance_window_task](#update_maintenance_window_task)
    - [update_managed_instance_role](#update_managed_instance_role)
    - [update_ops_item](#update_ops_item)
    - [update_ops_metadata](#update_ops_metadata)
    - [update_patch_baseline](#update_patch_baseline)
    - [update_resource_data_sync](#update_resource_data_sync)
    - [update_service_setting](#update_service_setting)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)
    - [get_paginator](#get_paginator-19)
    - [get_paginator](#get_paginator-20)
    - [get_paginator](#get_paginator-21)
    - [get_paginator](#get_paginator-22)
    - [get_paginator](#get_paginator-23)
    - [get_paginator](#get_paginator-24)
    - [get_paginator](#get_paginator-25)
    - [get_paginator](#get_paginator-26)
    - [get_paginator](#get_paginator-27)
    - [get_paginator](#get_paginator-28)
    - [get_paginator](#get_paginator-29)
    - [get_paginator](#get_paginator-30)
    - [get_paginator](#get_paginator-31)
    - [get_paginator](#get_paginator-32)
    - [get_paginator](#get_paginator-33)
    - [get_paginator](#get_paginator-34)
    - [get_paginator](#get_paginator-35)
    - [get_paginator](#get_paginator-36)
    - [get_paginator](#get_paginator-37)
    - [get_paginator](#get_paginator-38)
    - [get_paginator](#get_paginator-39)
    - [get_paginator](#get_paginator-40)
    - [get_paginator](#get_paginator-41)
    - [get_paginator](#get_paginator-42)
    - [get_paginator](#get_paginator-43)
    - [get_paginator](#get_paginator-44)
    - [get_waiter](#get_waiter)

## SSMClient

Type annotations for `boto3.client("ssm")`

Can be used directly:

```python
from mypy_boto3_ssm.client import SSMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ssm.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.AssociatedInstances`
- `Exceptions.AssociationAlreadyExists`
- `Exceptions.AssociationDoesNotExist`
- `Exceptions.AssociationExecutionDoesNotExist`
- `Exceptions.AssociationLimitExceeded`
- `Exceptions.AssociationVersionLimitExceeded`
- `Exceptions.AutomationDefinitionNotApprovedException`
- `Exceptions.AutomationDefinitionNotFoundException`
- `Exceptions.AutomationDefinitionVersionNotFoundException`
- `Exceptions.AutomationExecutionLimitExceededException`
- `Exceptions.AutomationExecutionNotFoundException`
- `Exceptions.AutomationStepNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.ComplianceTypeCountLimitExceededException`
- `Exceptions.CustomSchemaCountLimitExceededException`
- `Exceptions.DocumentAlreadyExists`
- `Exceptions.DocumentLimitExceeded`
- `Exceptions.DocumentPermissionLimit`
- `Exceptions.DocumentVersionLimitExceeded`
- `Exceptions.DoesNotExistException`
- `Exceptions.DuplicateDocumentContent`
- `Exceptions.DuplicateDocumentVersionName`
- `Exceptions.DuplicateInstanceId`
- `Exceptions.FeatureNotAvailableException`
- `Exceptions.HierarchyLevelLimitExceededException`
- `Exceptions.HierarchyTypeMismatchException`
- `Exceptions.IdempotentParameterMismatch`
- `Exceptions.IncompatiblePolicyException`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidActivation`
- `Exceptions.InvalidActivationId`
- `Exceptions.InvalidAggregatorException`
- `Exceptions.InvalidAllowedPatternException`
- `Exceptions.InvalidAssociation`
- `Exceptions.InvalidAssociationVersion`
- `Exceptions.InvalidAutomationExecutionParametersException`
- `Exceptions.InvalidAutomationSignalException`
- `Exceptions.InvalidAutomationStatusUpdateException`
- `Exceptions.InvalidCommandId`
- `Exceptions.InvalidDeleteInventoryParametersException`
- `Exceptions.InvalidDeletionIdException`
- `Exceptions.InvalidDocument`
- `Exceptions.InvalidDocumentContent`
- `Exceptions.InvalidDocumentOperation`
- `Exceptions.InvalidDocumentSchemaVersion`
- `Exceptions.InvalidDocumentType`
- `Exceptions.InvalidDocumentVersion`
- `Exceptions.InvalidFilter`
- `Exceptions.InvalidFilterKey`
- `Exceptions.InvalidFilterOption`
- `Exceptions.InvalidFilterValue`
- `Exceptions.InvalidInstanceId`
- `Exceptions.InvalidInstanceInformationFilterValue`
- `Exceptions.InvalidInventoryGroupException`
- `Exceptions.InvalidInventoryItemContextException`
- `Exceptions.InvalidInventoryRequestException`
- `Exceptions.InvalidItemContentException`
- `Exceptions.InvalidKeyId`
- `Exceptions.InvalidNextToken`
- `Exceptions.InvalidNotificationConfig`
- `Exceptions.InvalidOptionException`
- `Exceptions.InvalidOutputFolder`
- `Exceptions.InvalidOutputLocation`
- `Exceptions.InvalidParameters`
- `Exceptions.InvalidPermissionType`
- `Exceptions.InvalidPluginName`
- `Exceptions.InvalidPolicyAttributeException`
- `Exceptions.InvalidPolicyTypeException`
- `Exceptions.InvalidResourceId`
- `Exceptions.InvalidResourceType`
- `Exceptions.InvalidResultAttributeException`
- `Exceptions.InvalidRole`
- `Exceptions.InvalidSchedule`
- `Exceptions.InvalidTarget`
- `Exceptions.InvalidTypeNameException`
- `Exceptions.InvalidUpdate`
- `Exceptions.InvocationDoesNotExist`
- `Exceptions.ItemContentMismatchException`
- `Exceptions.ItemSizeLimitExceededException`
- `Exceptions.MaxDocumentSizeExceeded`
- `Exceptions.OpsItemAlreadyExistsException`
- `Exceptions.OpsItemInvalidParameterException`
- `Exceptions.OpsItemLimitExceededException`
- `Exceptions.OpsItemNotFoundException`
- `Exceptions.OpsMetadataAlreadyExistsException`
- `Exceptions.OpsMetadataInvalidArgumentException`
- `Exceptions.OpsMetadataKeyLimitExceededException`
- `Exceptions.OpsMetadataLimitExceededException`
- `Exceptions.OpsMetadataNotFoundException`
- `Exceptions.OpsMetadataTooManyUpdatesException`
- `Exceptions.ParameterAlreadyExists`
- `Exceptions.ParameterLimitExceeded`
- `Exceptions.ParameterMaxVersionLimitExceeded`
- `Exceptions.ParameterNotFound`
- `Exceptions.ParameterPatternMismatchException`
- `Exceptions.ParameterVersionLabelLimitExceeded`
- `Exceptions.ParameterVersionNotFound`
- `Exceptions.PoliciesLimitExceededException`
- `Exceptions.ResourceDataSyncAlreadyExistsException`
- `Exceptions.ResourceDataSyncConflictException`
- `Exceptions.ResourceDataSyncCountExceededException`
- `Exceptions.ResourceDataSyncInvalidConfigurationException`
- `Exceptions.ResourceDataSyncNotFoundException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ServiceSettingNotFound`
- `Exceptions.StatusUnchanged`
- `Exceptions.SubTypeCountLimitExceededException`
- `Exceptions.TargetInUseException`
- `Exceptions.TargetNotConnected`
- `Exceptions.TooManyTagsError`
- `Exceptions.TooManyUpdates`
- `Exceptions.TotalSizeLimitExceededException`
- `Exceptions.UnsupportedCalendarException`
- `Exceptions.UnsupportedFeatureRequiredException`
- `Exceptions.UnsupportedInventoryItemContextException`
- `Exceptions.UnsupportedInventorySchemaVersionException`
- `Exceptions.UnsupportedOperatingSystem`
- `Exceptions.UnsupportedParameterType`
- `Exceptions.UnsupportedPlatformType`


## Methods


### add_tags_to_resource

Type annotations for `boto3.client("ssm").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceType: ResourceTypeForTagging,
    ResourceId: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("ssm").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_command

Type annotations for `boto3.client("ssm").cancel_command` method.

[Client.cancel_command documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.cancel_command)

```python
def cancel_command(
    self,
    CommandId: str,
    InstanceIds: List[str] = None
) -> Dict[str, Any]:
    pass
```

### cancel_maintenance_window_execution

Type annotations for `boto3.client("ssm").cancel_maintenance_window_execution` method.

[Client.cancel_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.cancel_maintenance_window_execution)

```python
def cancel_maintenance_window_execution(
    self,
    WindowExecutionId: str
) -> CancelMaintenanceWindowExecutionResultTypeDef:
    pass
```

### create_activation

Type annotations for `boto3.client("ssm").create_activation` method.

[Client.create_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_activation)

```python
def create_activation(
    self,
    IamRole: str,
    Description: str = None,
    DefaultInstanceName: str = None,
    RegistrationLimit: int = None,
    ExpirationDate: datetime = None,
    Tags: List["TagTypeDef"] = None
) -> CreateActivationResultTypeDef:
    pass
```

### create_association

Type annotations for `boto3.client("ssm").create_association` method.

[Client.create_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_association)

```python
def create_association(
    self,
    Name: str,
    DocumentVersion: str = None,
    InstanceId: str = None,
    Parameters: Dict[str, List[str]] = None,
    Targets: List["TargetTypeDef"] = None,
    ScheduleExpression: str = None,
    OutputLocation: "InstanceAssociationOutputLocationTypeDef" = None,
    AssociationName: str = None,
    AutomationTargetParameterName: str = None,
    MaxErrors: str = None,
    MaxConcurrency: str = None,
    ComplianceSeverity: AssociationComplianceSeverity = None,
    SyncCompliance: AssociationSyncCompliance = None,
    ApplyOnlyAtCronInterval: bool = None,
    TargetLocations: List["TargetLocationTypeDef"] = None
) -> CreateAssociationResultTypeDef:
    pass
```

### create_association_batch

Type annotations for `boto3.client("ssm").create_association_batch` method.

[Client.create_association_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_association_batch)

```python
def create_association_batch(
    self,
    Entries: List["CreateAssociationBatchRequestEntryTypeDef"]
) -> CreateAssociationBatchResultTypeDef:
    pass
```

### create_document

Type annotations for `boto3.client("ssm").create_document` method.

[Client.create_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_document)

```python
def create_document(
    self,
    Content: str,
    Name: str,
    Requires: List["DocumentRequiresTypeDef"] = None,
    Attachments: List[AttachmentsSourceTypeDef] = None,
    VersionName: str = None,
    DocumentType: DocumentType = None,
    DocumentFormat: DocumentFormat = None,
    TargetType: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDocumentResultTypeDef:
    pass
```

### create_maintenance_window

Type annotations for `boto3.client("ssm").create_maintenance_window` method.

[Client.create_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_maintenance_window)

```python
def create_maintenance_window(
    self,
    Name: str,
    Schedule: str,
    Duration: int,
    Cutoff: int,
    AllowUnassociatedTargets: bool,
    Description: str = None,
    StartDate: str = None,
    EndDate: str = None,
    ScheduleTimezone: str = None,
    ScheduleOffset: int = None,
    ClientToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateMaintenanceWindowResultTypeDef:
    pass
```

### create_ops_item

Type annotations for `boto3.client("ssm").create_ops_item` method.

[Client.create_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_ops_item)

```python
def create_ops_item(
    self,
    Description: str,
    Source: str,
    Title: str,
    OpsItemType: str = None,
    OperationalData: Dict[str, "OpsItemDataValueTypeDef"] = None,
    Notifications: List["OpsItemNotificationTypeDef"] = None,
    Priority: int = None,
    RelatedOpsItems: List["RelatedOpsItemTypeDef"] = None,
    Tags: List["TagTypeDef"] = None,
    Category: str = None,
    Severity: str = None,
    ActualStartTime: datetime = None,
    ActualEndTime: datetime = None,
    PlannedStartTime: datetime = None,
    PlannedEndTime: datetime = None
) -> CreateOpsItemResponseTypeDef:
    pass
```

### create_ops_metadata

Type annotations for `boto3.client("ssm").create_ops_metadata` method.

[Client.create_ops_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_ops_metadata)

```python
def create_ops_metadata(
    self,
    ResourceId: str,
    Metadata: Dict[str, "MetadataValueTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateOpsMetadataResultTypeDef:
    pass
```

### create_patch_baseline

Type annotations for `boto3.client("ssm").create_patch_baseline` method.

[Client.create_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_patch_baseline)

```python
def create_patch_baseline(
    self,
    Name: str,
    OperatingSystem: OperatingSystem = None,
    GlobalFilters: "PatchFilterGroupTypeDef" = None,
    ApprovalRules: "PatchRuleGroupTypeDef" = None,
    ApprovedPatches: List[str] = None,
    ApprovedPatchesComplianceLevel: PatchComplianceLevel = None,
    ApprovedPatchesEnableNonSecurity: bool = None,
    RejectedPatches: List[str] = None,
    RejectedPatchesAction: PatchAction = None,
    Description: str = None,
    Sources: List["PatchSourceTypeDef"] = None,
    ClientToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePatchBaselineResultTypeDef:
    pass
```

### create_resource_data_sync

Type annotations for `boto3.client("ssm").create_resource_data_sync` method.

[Client.create_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.create_resource_data_sync)

```python
def create_resource_data_sync(
    self,
    SyncName: str,
    S3Destination: "ResourceDataSyncS3DestinationTypeDef" = None,
    SyncType: str = None,
    SyncSource: ResourceDataSyncSourceTypeDef = None
) -> Dict[str, Any]:
    pass
```

### delete_activation

Type annotations for `boto3.client("ssm").delete_activation` method.

[Client.delete_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_activation)

```python
def delete_activation(
    self,
    ActivationId: str
) -> Dict[str, Any]:
    pass
```

### delete_association

Type annotations for `boto3.client("ssm").delete_association` method.

[Client.delete_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_association)

```python
def delete_association(
    self,
    Name: str = None,
    InstanceId: str = None,
    AssociationId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_document

Type annotations for `boto3.client("ssm").delete_document` method.

[Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_document)

```python
def delete_document(
    self,
    Name: str,
    DocumentVersion: str = None,
    VersionName: str = None,
    Force: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_inventory

Type annotations for `boto3.client("ssm").delete_inventory` method.

[Client.delete_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_inventory)

```python
def delete_inventory(
    self,
    TypeName: str,
    SchemaDeleteOption: InventorySchemaDeleteOption = None,
    DryRun: bool = None,
    ClientToken: str = None
) -> DeleteInventoryResultTypeDef:
    pass
```

### delete_maintenance_window

Type annotations for `boto3.client("ssm").delete_maintenance_window` method.

[Client.delete_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_maintenance_window)

```python
def delete_maintenance_window(
    self,
    WindowId: str
) -> DeleteMaintenanceWindowResultTypeDef:
    pass
```

### delete_ops_metadata

Type annotations for `boto3.client("ssm").delete_ops_metadata` method.

[Client.delete_ops_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_ops_metadata)

```python
def delete_ops_metadata(
    self,
    OpsMetadataArn: str
) -> Dict[str, Any]:
    pass
```

### delete_parameter

Type annotations for `boto3.client("ssm").delete_parameter` method.

[Client.delete_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_parameter)

```python
def delete_parameter(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_parameters

Type annotations for `boto3.client("ssm").delete_parameters` method.

[Client.delete_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_parameters)

```python
def delete_parameters(
    self,
    Names: List[str]
) -> DeleteParametersResultTypeDef:
    pass
```

### delete_patch_baseline

Type annotations for `boto3.client("ssm").delete_patch_baseline` method.

[Client.delete_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_patch_baseline)

```python
def delete_patch_baseline(
    self,
    BaselineId: str
) -> DeletePatchBaselineResultTypeDef:
    pass
```

### delete_resource_data_sync

Type annotations for `boto3.client("ssm").delete_resource_data_sync` method.

[Client.delete_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.delete_resource_data_sync)

```python
def delete_resource_data_sync(
    self,
    SyncName: str,
    SyncType: str = None
) -> Dict[str, Any]:
    pass
```

### deregister_managed_instance

Type annotations for `boto3.client("ssm").deregister_managed_instance` method.

[Client.deregister_managed_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.deregister_managed_instance)

```python
def deregister_managed_instance(
    self,
    InstanceId: str
) -> Dict[str, Any]:
    pass
```

### deregister_patch_baseline_for_patch_group

Type annotations for `boto3.client("ssm").deregister_patch_baseline_for_patch_group` method.

[Client.deregister_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.deregister_patch_baseline_for_patch_group)

```python
def deregister_patch_baseline_for_patch_group(
    self,
    BaselineId: str,
    PatchGroup: str
) -> DeregisterPatchBaselineForPatchGroupResultTypeDef:
    pass
```

### deregister_target_from_maintenance_window

Type annotations for `boto3.client("ssm").deregister_target_from_maintenance_window` method.

[Client.deregister_target_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.deregister_target_from_maintenance_window)

```python
def deregister_target_from_maintenance_window(
    self,
    WindowId: str,
    WindowTargetId: str,
    Safe: bool = None
) -> DeregisterTargetFromMaintenanceWindowResultTypeDef:
    pass
```

### deregister_task_from_maintenance_window

Type annotations for `boto3.client("ssm").deregister_task_from_maintenance_window` method.

[Client.deregister_task_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.deregister_task_from_maintenance_window)

```python
def deregister_task_from_maintenance_window(
    self,
    WindowId: str,
    WindowTaskId: str
) -> DeregisterTaskFromMaintenanceWindowResultTypeDef:
    pass
```

### describe_activations

Type annotations for `boto3.client("ssm").describe_activations` method.

[Client.describe_activations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_activations)

```python
def describe_activations(
    self,
    Filters: List[DescribeActivationsFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeActivationsResultTypeDef:
    pass
```

### describe_association

Type annotations for `boto3.client("ssm").describe_association` method.

[Client.describe_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_association)

```python
def describe_association(
    self,
    Name: str = None,
    InstanceId: str = None,
    AssociationId: str = None,
    AssociationVersion: str = None
) -> DescribeAssociationResultTypeDef:
    pass
```

### describe_association_execution_targets

Type annotations for `boto3.client("ssm").describe_association_execution_targets` method.

[Client.describe_association_execution_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_association_execution_targets)

```python
def describe_association_execution_targets(
    self,
    AssociationId: str,
    ExecutionId: str,
    Filters: List[AssociationExecutionTargetsFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeAssociationExecutionTargetsResultTypeDef:
    pass
```

### describe_association_executions

Type annotations for `boto3.client("ssm").describe_association_executions` method.

[Client.describe_association_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_association_executions)

```python
def describe_association_executions(
    self,
    AssociationId: str,
    Filters: List[AssociationExecutionFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeAssociationExecutionsResultTypeDef:
    pass
```

### describe_automation_executions

Type annotations for `boto3.client("ssm").describe_automation_executions` method.

[Client.describe_automation_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_automation_executions)

```python
def describe_automation_executions(
    self,
    Filters: List[AutomationExecutionFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeAutomationExecutionsResultTypeDef:
    pass
```

### describe_automation_step_executions

Type annotations for `boto3.client("ssm").describe_automation_step_executions` method.

[Client.describe_automation_step_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_automation_step_executions)

```python
def describe_automation_step_executions(
    self,
    AutomationExecutionId: str,
    Filters: List[StepExecutionFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None,
    ReverseOrder: bool = None
) -> DescribeAutomationStepExecutionsResultTypeDef:
    pass
```

### describe_available_patches

Type annotations for `boto3.client("ssm").describe_available_patches` method.

[Client.describe_available_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_available_patches)

```python
def describe_available_patches(
    self,
    Filters: List[PatchOrchestratorFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeAvailablePatchesResultTypeDef:
    pass
```

### describe_document

Type annotations for `boto3.client("ssm").describe_document` method.

[Client.describe_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_document)

```python
def describe_document(
    self,
    Name: str,
    DocumentVersion: str = None,
    VersionName: str = None
) -> DescribeDocumentResultTypeDef:
    pass
```

### describe_document_permission

Type annotations for `boto3.client("ssm").describe_document_permission` method.

[Client.describe_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_document_permission)

```python
def describe_document_permission(
    self,
    Name: str,
    PermissionType: DocumentPermissionType,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeDocumentPermissionResponseTypeDef:
    pass
```

### describe_effective_instance_associations

Type annotations for `boto3.client("ssm").describe_effective_instance_associations` method.

[Client.describe_effective_instance_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_effective_instance_associations)

```python
def describe_effective_instance_associations(
    self,
    InstanceId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeEffectiveInstanceAssociationsResultTypeDef:
    pass
```

### describe_effective_patches_for_patch_baseline

Type annotations for `boto3.client("ssm").describe_effective_patches_for_patch_baseline` method.

[Client.describe_effective_patches_for_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_effective_patches_for_patch_baseline)

```python
def describe_effective_patches_for_patch_baseline(
    self,
    BaselineId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeEffectivePatchesForPatchBaselineResultTypeDef:
    pass
```

### describe_instance_associations_status

Type annotations for `boto3.client("ssm").describe_instance_associations_status` method.

[Client.describe_instance_associations_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_instance_associations_status)

```python
def describe_instance_associations_status(
    self,
    InstanceId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInstanceAssociationsStatusResultTypeDef:
    pass
```

### describe_instance_information

Type annotations for `boto3.client("ssm").describe_instance_information` method.

[Client.describe_instance_information documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_instance_information)

```python
def describe_instance_information(
    self,
    InstanceInformationFilterList: List[InstanceInformationFilterTypeDef] = None,
    Filters: List[InstanceInformationStringFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInstanceInformationResultTypeDef:
    pass
```

### describe_instance_patch_states

Type annotations for `boto3.client("ssm").describe_instance_patch_states` method.

[Client.describe_instance_patch_states documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_instance_patch_states)

```python
def describe_instance_patch_states(
    self,
    InstanceIds: List[str],
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeInstancePatchStatesResultTypeDef:
    pass
```

### describe_instance_patch_states_for_patch_group

Type annotations for `boto3.client("ssm").describe_instance_patch_states_for_patch_group` method.

[Client.describe_instance_patch_states_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_instance_patch_states_for_patch_group)

```python
def describe_instance_patch_states_for_patch_group(
    self,
    PatchGroup: str,
    Filters: List[InstancePatchStateFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeInstancePatchStatesForPatchGroupResultTypeDef:
    pass
```

### describe_instance_patches

Type annotations for `boto3.client("ssm").describe_instance_patches` method.

[Client.describe_instance_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_instance_patches)

```python
def describe_instance_patches(
    self,
    InstanceId: str,
    Filters: List[PatchOrchestratorFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeInstancePatchesResultTypeDef:
    pass
```

### describe_inventory_deletions

Type annotations for `boto3.client("ssm").describe_inventory_deletions` method.

[Client.describe_inventory_deletions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_inventory_deletions)

```python
def describe_inventory_deletions(
    self,
    DeletionId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeInventoryDeletionsResultTypeDef:
    pass
```

### describe_maintenance_window_execution_task_invocations

Type annotations for `boto3.client("ssm").describe_maintenance_window_execution_task_invocations` method.

[Client.describe_maintenance_window_execution_task_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_task_invocations)

```python
def describe_maintenance_window_execution_task_invocations(
    self,
    WindowExecutionId: str,
    TaskId: str,
    Filters: List[MaintenanceWindowFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef:
    pass
```

### describe_maintenance_window_execution_tasks

Type annotations for `boto3.client("ssm").describe_maintenance_window_execution_tasks` method.

[Client.describe_maintenance_window_execution_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_tasks)

```python
def describe_maintenance_window_execution_tasks(
    self,
    WindowExecutionId: str,
    Filters: List[MaintenanceWindowFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowExecutionTasksResultTypeDef:
    pass
```

### describe_maintenance_window_executions

Type annotations for `boto3.client("ssm").describe_maintenance_window_executions` method.

[Client.describe_maintenance_window_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_window_executions)

```python
def describe_maintenance_window_executions(
    self,
    WindowId: str,
    Filters: List[MaintenanceWindowFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowExecutionsResultTypeDef:
    pass
```

### describe_maintenance_window_schedule

Type annotations for `boto3.client("ssm").describe_maintenance_window_schedule` method.

[Client.describe_maintenance_window_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_window_schedule)

```python
def describe_maintenance_window_schedule(
    self,
    WindowId: str = None,
    Targets: List["TargetTypeDef"] = None,
    ResourceType: MaintenanceWindowResourceType = None,
    Filters: List[PatchOrchestratorFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowScheduleResultTypeDef:
    pass
```

### describe_maintenance_window_targets

Type annotations for `boto3.client("ssm").describe_maintenance_window_targets` method.

[Client.describe_maintenance_window_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_window_targets)

```python
def describe_maintenance_window_targets(
    self,
    WindowId: str,
    Filters: List[MaintenanceWindowFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowTargetsResultTypeDef:
    pass
```

### describe_maintenance_window_tasks

Type annotations for `boto3.client("ssm").describe_maintenance_window_tasks` method.

[Client.describe_maintenance_window_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_window_tasks)

```python
def describe_maintenance_window_tasks(
    self,
    WindowId: str,
    Filters: List[MaintenanceWindowFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowTasksResultTypeDef:
    pass
```

### describe_maintenance_windows

Type annotations for `boto3.client("ssm").describe_maintenance_windows` method.

[Client.describe_maintenance_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_windows)

```python
def describe_maintenance_windows(
    self,
    Filters: List[MaintenanceWindowFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowsResultTypeDef:
    pass
```

### describe_maintenance_windows_for_target

Type annotations for `boto3.client("ssm").describe_maintenance_windows_for_target` method.

[Client.describe_maintenance_windows_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_maintenance_windows_for_target)

```python
def describe_maintenance_windows_for_target(
    self,
    Targets: List["TargetTypeDef"],
    ResourceType: MaintenanceWindowResourceType,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeMaintenanceWindowsForTargetResultTypeDef:
    pass
```

### describe_ops_items

Type annotations for `boto3.client("ssm").describe_ops_items` method.

[Client.describe_ops_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_ops_items)

```python
def describe_ops_items(
    self,
    OpsItemFilters: List[OpsItemFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeOpsItemsResponseTypeDef:
    pass
```

### describe_parameters

Type annotations for `boto3.client("ssm").describe_parameters` method.

[Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_parameters)

```python
def describe_parameters(
    self,
    Filters: List[ParametersFilterTypeDef] = None,
    ParameterFilters: List[ParameterStringFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeParametersResultTypeDef:
    pass
```

### describe_patch_baselines

Type annotations for `boto3.client("ssm").describe_patch_baselines` method.

[Client.describe_patch_baselines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_patch_baselines)

```python
def describe_patch_baselines(
    self,
    Filters: List[PatchOrchestratorFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribePatchBaselinesResultTypeDef:
    pass
```

### describe_patch_group_state

Type annotations for `boto3.client("ssm").describe_patch_group_state` method.

[Client.describe_patch_group_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_patch_group_state)

```python
def describe_patch_group_state(
    self,
    PatchGroup: str
) -> DescribePatchGroupStateResultTypeDef:
    pass
```

### describe_patch_groups

Type annotations for `boto3.client("ssm").describe_patch_groups` method.

[Client.describe_patch_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_patch_groups)

```python
def describe_patch_groups(
    self,
    MaxResults: int = None,
    Filters: List[PatchOrchestratorFilterTypeDef] = None,
    NextToken: str = None
) -> DescribePatchGroupsResultTypeDef:
    pass
```

### describe_patch_properties

Type annotations for `boto3.client("ssm").describe_patch_properties` method.

[Client.describe_patch_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_patch_properties)

```python
def describe_patch_properties(
    self,
    OperatingSystem: OperatingSystem,
    Property: PatchProperty,
    PatchSet: PatchSet = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribePatchPropertiesResultTypeDef:
    pass
```

### describe_sessions

Type annotations for `boto3.client("ssm").describe_sessions` method.

[Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.describe_sessions)

```python
def describe_sessions(
    self,
    State: SessionState,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[SessionFilterTypeDef] = None
) -> DescribeSessionsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ssm").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.generate_presigned_url)

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

### get_automation_execution

Type annotations for `boto3.client("ssm").get_automation_execution` method.

[Client.get_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_automation_execution)

```python
def get_automation_execution(
    self,
    AutomationExecutionId: str
) -> GetAutomationExecutionResultTypeDef:
    pass
```

### get_calendar_state

Type annotations for `boto3.client("ssm").get_calendar_state` method.

[Client.get_calendar_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_calendar_state)

```python
def get_calendar_state(
    self,
    CalendarNames: List[str],
    AtTime: str = None
) -> GetCalendarStateResponseTypeDef:
    pass
```

### get_command_invocation

Type annotations for `boto3.client("ssm").get_command_invocation` method.

[Client.get_command_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_command_invocation)

```python
def get_command_invocation(
    self,
    CommandId: str,
    InstanceId: str,
    PluginName: str = None
) -> GetCommandInvocationResultTypeDef:
    pass
```

### get_connection_status

Type annotations for `boto3.client("ssm").get_connection_status` method.

[Client.get_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_connection_status)

```python
def get_connection_status(
    self,
    Target: str
) -> GetConnectionStatusResponseTypeDef:
    pass
```

### get_default_patch_baseline

Type annotations for `boto3.client("ssm").get_default_patch_baseline` method.

[Client.get_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_default_patch_baseline)

```python
def get_default_patch_baseline(
    self,
    OperatingSystem: OperatingSystem = None
) -> GetDefaultPatchBaselineResultTypeDef:
    pass
```

### get_deployable_patch_snapshot_for_instance

Type annotations for `boto3.client("ssm").get_deployable_patch_snapshot_for_instance` method.

[Client.get_deployable_patch_snapshot_for_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_deployable_patch_snapshot_for_instance)

```python
def get_deployable_patch_snapshot_for_instance(
    self,
    InstanceId: str,
    SnapshotId: str,
    BaselineOverride: BaselineOverrideTypeDef = None
) -> GetDeployablePatchSnapshotForInstanceResultTypeDef:
    pass
```

### get_document

Type annotations for `boto3.client("ssm").get_document` method.

[Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_document)

```python
def get_document(
    self,
    Name: str,
    VersionName: str = None,
    DocumentVersion: str = None,
    DocumentFormat: DocumentFormat = None
) -> GetDocumentResultTypeDef:
    pass
```

### get_inventory

Type annotations for `boto3.client("ssm").get_inventory` method.

[Client.get_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_inventory)

```python
def get_inventory(
    self,
    Filters: List["InventoryFilterTypeDef"] = None,
    Aggregators: List[Dict[str, Any]] = None,
    ResultAttributes: List[ResultAttributeTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetInventoryResultTypeDef:
    pass
```

### get_inventory_schema

Type annotations for `boto3.client("ssm").get_inventory_schema` method.

[Client.get_inventory_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_inventory_schema)

```python
def get_inventory_schema(
    self,
    TypeName: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    Aggregator: bool = None,
    SubType: bool = None
) -> GetInventorySchemaResultTypeDef:
    pass
```

### get_maintenance_window

Type annotations for `boto3.client("ssm").get_maintenance_window` method.

[Client.get_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_maintenance_window)

```python
def get_maintenance_window(
    self,
    WindowId: str
) -> GetMaintenanceWindowResultTypeDef:
    pass
```

### get_maintenance_window_execution

Type annotations for `boto3.client("ssm").get_maintenance_window_execution` method.

[Client.get_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution)

```python
def get_maintenance_window_execution(
    self,
    WindowExecutionId: str
) -> GetMaintenanceWindowExecutionResultTypeDef:
    pass
```

### get_maintenance_window_execution_task

Type annotations for `boto3.client("ssm").get_maintenance_window_execution_task` method.

[Client.get_maintenance_window_execution_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task)

```python
def get_maintenance_window_execution_task(
    self,
    WindowExecutionId: str,
    TaskId: str
) -> GetMaintenanceWindowExecutionTaskResultTypeDef:
    pass
```

### get_maintenance_window_execution_task_invocation

Type annotations for `boto3.client("ssm").get_maintenance_window_execution_task_invocation` method.

[Client.get_maintenance_window_execution_task_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task_invocation)

```python
def get_maintenance_window_execution_task_invocation(
    self,
    WindowExecutionId: str,
    TaskId: str,
    InvocationId: str
) -> GetMaintenanceWindowExecutionTaskInvocationResultTypeDef:
    pass
```

### get_maintenance_window_task

Type annotations for `boto3.client("ssm").get_maintenance_window_task` method.

[Client.get_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_maintenance_window_task)

```python
def get_maintenance_window_task(
    self,
    WindowId: str,
    WindowTaskId: str
) -> GetMaintenanceWindowTaskResultTypeDef:
    pass
```

### get_ops_item

Type annotations for `boto3.client("ssm").get_ops_item` method.

[Client.get_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_ops_item)

```python
def get_ops_item(
    self,
    OpsItemId: str
) -> GetOpsItemResponseTypeDef:
    pass
```

### get_ops_metadata

Type annotations for `boto3.client("ssm").get_ops_metadata` method.

[Client.get_ops_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_ops_metadata)

```python
def get_ops_metadata(
    self,
    OpsMetadataArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetOpsMetadataResultTypeDef:
    pass
```

### get_ops_summary

Type annotations for `boto3.client("ssm").get_ops_summary` method.

[Client.get_ops_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_ops_summary)

```python
def get_ops_summary(
    self,
    SyncName: str = None,
    Filters: List["OpsFilterTypeDef"] = None,
    Aggregators: List[Dict[str, Any]] = None,
    ResultAttributes: List[OpsResultAttributeTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetOpsSummaryResultTypeDef:
    pass
```

### get_parameter

Type annotations for `boto3.client("ssm").get_parameter` method.

[Client.get_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_parameter)

```python
def get_parameter(
    self,
    Name: str,
    WithDecryption: bool = None
) -> GetParameterResultTypeDef:
    pass
```

### get_parameter_history

Type annotations for `boto3.client("ssm").get_parameter_history` method.

[Client.get_parameter_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_parameter_history)

```python
def get_parameter_history(
    self,
    Name: str,
    WithDecryption: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetParameterHistoryResultTypeDef:
    pass
```

### get_parameters

Type annotations for `boto3.client("ssm").get_parameters` method.

[Client.get_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_parameters)

```python
def get_parameters(
    self,
    Names: List[str],
    WithDecryption: bool = None
) -> GetParametersResultTypeDef:
    pass
```

### get_parameters_by_path

Type annotations for `boto3.client("ssm").get_parameters_by_path` method.

[Client.get_parameters_by_path documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_parameters_by_path)

```python
def get_parameters_by_path(
    self,
    Path: str,
    Recursive: bool = None,
    ParameterFilters: List[ParameterStringFilterTypeDef] = None,
    WithDecryption: bool = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetParametersByPathResultTypeDef:
    pass
```

### get_patch_baseline

Type annotations for `boto3.client("ssm").get_patch_baseline` method.

[Client.get_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_patch_baseline)

```python
def get_patch_baseline(
    self,
    BaselineId: str
) -> GetPatchBaselineResultTypeDef:
    pass
```

### get_patch_baseline_for_patch_group

Type annotations for `boto3.client("ssm").get_patch_baseline_for_patch_group` method.

[Client.get_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_patch_baseline_for_patch_group)

```python
def get_patch_baseline_for_patch_group(
    self,
    PatchGroup: str,
    OperatingSystem: OperatingSystem = None
) -> GetPatchBaselineForPatchGroupResultTypeDef:
    pass
```

### get_service_setting

Type annotations for `boto3.client("ssm").get_service_setting` method.

[Client.get_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_service_setting)

```python
def get_service_setting(
    self,
    SettingId: str
) -> GetServiceSettingResultTypeDef:
    pass
```

### label_parameter_version

Type annotations for `boto3.client("ssm").label_parameter_version` method.

[Client.label_parameter_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.label_parameter_version)

```python
def label_parameter_version(
    self,
    Name: str,
    Labels: List[str],
    ParameterVersion: int = None
) -> LabelParameterVersionResultTypeDef:
    pass
```

### list_association_versions

Type annotations for `boto3.client("ssm").list_association_versions` method.

[Client.list_association_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_association_versions)

```python
def list_association_versions(
    self,
    AssociationId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAssociationVersionsResultTypeDef:
    pass
```

### list_associations

Type annotations for `boto3.client("ssm").list_associations` method.

[Client.list_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_associations)

```python
def list_associations(
    self,
    AssociationFilterList: List[AssociationFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAssociationsResultTypeDef:
    pass
```

### list_command_invocations

Type annotations for `boto3.client("ssm").list_command_invocations` method.

[Client.list_command_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_command_invocations)

```python
def list_command_invocations(
    self,
    CommandId: str = None,
    InstanceId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[CommandFilterTypeDef] = None,
    Details: bool = None
) -> ListCommandInvocationsResultTypeDef:
    pass
```

### list_commands

Type annotations for `boto3.client("ssm").list_commands` method.

[Client.list_commands documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_commands)

```python
def list_commands(
    self,
    CommandId: str = None,
    InstanceId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[CommandFilterTypeDef] = None
) -> ListCommandsResultTypeDef:
    pass
```

### list_compliance_items

Type annotations for `boto3.client("ssm").list_compliance_items` method.

[Client.list_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_compliance_items)

```python
def list_compliance_items(
    self,
    Filters: List[ComplianceStringFilterTypeDef] = None,
    ResourceIds: List[str] = None,
    ResourceTypes: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListComplianceItemsResultTypeDef:
    pass
```

### list_compliance_summaries

Type annotations for `boto3.client("ssm").list_compliance_summaries` method.

[Client.list_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_compliance_summaries)

```python
def list_compliance_summaries(
    self,
    Filters: List[ComplianceStringFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListComplianceSummariesResultTypeDef:
    pass
```

### list_document_metadata_history

Type annotations for `boto3.client("ssm").list_document_metadata_history` method.

[Client.list_document_metadata_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_document_metadata_history)

```python
def list_document_metadata_history(
    self,
    Name: str,
    Metadata: DocumentMetadataEnum,
    DocumentVersion: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDocumentMetadataHistoryResponseTypeDef:
    pass
```

### list_document_versions

Type annotations for `boto3.client("ssm").list_document_versions` method.

[Client.list_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_document_versions)

```python
def list_document_versions(
    self,
    Name: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDocumentVersionsResultTypeDef:
    pass
```

### list_documents

Type annotations for `boto3.client("ssm").list_documents` method.

[Client.list_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_documents)

```python
def list_documents(
    self,
    DocumentFilterList: List[DocumentFilterTypeDef] = None,
    Filters: List[DocumentKeyValuesFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDocumentsResultTypeDef:
    pass
```

### list_inventory_entries

Type annotations for `boto3.client("ssm").list_inventory_entries` method.

[Client.list_inventory_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_inventory_entries)

```python
def list_inventory_entries(
    self,
    InstanceId: str,
    TypeName: str,
    Filters: List["InventoryFilterTypeDef"] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListInventoryEntriesResultTypeDef:
    pass
```

### list_ops_item_events

Type annotations for `boto3.client("ssm").list_ops_item_events` method.

[Client.list_ops_item_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_ops_item_events)

```python
def list_ops_item_events(
    self,
    Filters: List[OpsItemEventFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListOpsItemEventsResponseTypeDef:
    pass
```

### list_ops_metadata

Type annotations for `boto3.client("ssm").list_ops_metadata` method.

[Client.list_ops_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_ops_metadata)

```python
def list_ops_metadata(
    self,
    Filters: List[OpsMetadataFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListOpsMetadataResultTypeDef:
    pass
```

### list_resource_compliance_summaries

Type annotations for `boto3.client("ssm").list_resource_compliance_summaries` method.

[Client.list_resource_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_resource_compliance_summaries)

```python
def list_resource_compliance_summaries(
    self,
    Filters: List[ComplianceStringFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListResourceComplianceSummariesResultTypeDef:
    pass
```

### list_resource_data_sync

Type annotations for `boto3.client("ssm").list_resource_data_sync` method.

[Client.list_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_resource_data_sync)

```python
def list_resource_data_sync(
    self,
    SyncType: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListResourceDataSyncResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("ssm").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceType: ResourceTypeForTagging,
    ResourceId: str
) -> ListTagsForResourceResultTypeDef:
    pass
```

### modify_document_permission

Type annotations for `boto3.client("ssm").modify_document_permission` method.

[Client.modify_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.modify_document_permission)

```python
def modify_document_permission(
    self,
    Name: str,
    PermissionType: DocumentPermissionType,
    AccountIdsToAdd: List[str] = None,
    AccountIdsToRemove: List[str] = None,
    SharedDocumentVersion: str = None
) -> Dict[str, Any]:
    pass
```

### put_compliance_items

Type annotations for `boto3.client("ssm").put_compliance_items` method.

[Client.put_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.put_compliance_items)

```python
def put_compliance_items(
    self,
    ResourceId: str,
    ResourceType: str,
    ComplianceType: str,
    ExecutionSummary: "ComplianceExecutionSummaryTypeDef",
    Items: List[ComplianceItemEntryTypeDef],
    ItemContentHash: str = None,
    UploadType: ComplianceUploadType = None
) -> Dict[str, Any]:
    pass
```

### put_inventory

Type annotations for `boto3.client("ssm").put_inventory` method.

[Client.put_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.put_inventory)

```python
def put_inventory(
    self,
    InstanceId: str,
    Items: List[InventoryItemTypeDef]
) -> PutInventoryResultTypeDef:
    pass
```

### put_parameter

Type annotations for `boto3.client("ssm").put_parameter` method.

[Client.put_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.put_parameter)

```python
def put_parameter(
    self,
    Name: str,
    Value: str,
    Description: str = None,
    Type: ParameterType = None,
    KeyId: str = None,
    Overwrite: bool = None,
    AllowedPattern: str = None,
    Tags: List["TagTypeDef"] = None,
    Tier: ParameterTier = None,
    Policies: str = None,
    DataType: str = None
) -> PutParameterResultTypeDef:
    pass
```

### register_default_patch_baseline

Type annotations for `boto3.client("ssm").register_default_patch_baseline` method.

[Client.register_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.register_default_patch_baseline)

```python
def register_default_patch_baseline(
    self,
    BaselineId: str
) -> RegisterDefaultPatchBaselineResultTypeDef:
    pass
```

### register_patch_baseline_for_patch_group

Type annotations for `boto3.client("ssm").register_patch_baseline_for_patch_group` method.

[Client.register_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.register_patch_baseline_for_patch_group)

```python
def register_patch_baseline_for_patch_group(
    self,
    BaselineId: str,
    PatchGroup: str
) -> RegisterPatchBaselineForPatchGroupResultTypeDef:
    pass
```

### register_target_with_maintenance_window

Type annotations for `boto3.client("ssm").register_target_with_maintenance_window` method.

[Client.register_target_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.register_target_with_maintenance_window)

```python
def register_target_with_maintenance_window(
    self,
    WindowId: str,
    ResourceType: MaintenanceWindowResourceType,
    Targets: List["TargetTypeDef"],
    OwnerInformation: str = None,
    Name: str = None,
    Description: str = None,
    ClientToken: str = None
) -> RegisterTargetWithMaintenanceWindowResultTypeDef:
    pass
```

### register_task_with_maintenance_window

Type annotations for `boto3.client("ssm").register_task_with_maintenance_window` method.

[Client.register_task_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.register_task_with_maintenance_window)

```python
def register_task_with_maintenance_window(
    self,
    WindowId: str,
    TaskArn: str,
    TaskType: MaintenanceWindowTaskType,
    Targets: List["TargetTypeDef"] = None,
    ServiceRoleArn: str = None,
    TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"] = None,
    TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef" = None,
    Priority: int = None,
    MaxConcurrency: str = None,
    MaxErrors: str = None,
    LoggingInfo: "LoggingInfoTypeDef" = None,
    Name: str = None,
    Description: str = None,
    ClientToken: str = None
) -> RegisterTaskWithMaintenanceWindowResultTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("ssm").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceType: ResourceTypeForTagging,
    ResourceId: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### reset_service_setting

Type annotations for `boto3.client("ssm").reset_service_setting` method.

[Client.reset_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.reset_service_setting)

```python
def reset_service_setting(
    self,
    SettingId: str
) -> ResetServiceSettingResultTypeDef:
    pass
```

### resume_session

Type annotations for `boto3.client("ssm").resume_session` method.

[Client.resume_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.resume_session)

```python
def resume_session(
    self,
    SessionId: str
) -> ResumeSessionResponseTypeDef:
    pass
```

### send_automation_signal

Type annotations for `boto3.client("ssm").send_automation_signal` method.

[Client.send_automation_signal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.send_automation_signal)

```python
def send_automation_signal(
    self,
    AutomationExecutionId: str,
    SignalType: SignalType,
    Payload: Dict[str, List[str]] = None
) -> Dict[str, Any]:
    pass
```

### send_command

Type annotations for `boto3.client("ssm").send_command` method.

[Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.send_command)

```python
def send_command(
    self,
    DocumentName: str,
    InstanceIds: List[str] = None,
    Targets: List["TargetTypeDef"] = None,
    DocumentVersion: str = None,
    DocumentHash: str = None,
    DocumentHashType: DocumentHashType = None,
    TimeoutSeconds: int = None,
    Comment: str = None,
    Parameters: Dict[str, List[str]] = None,
    OutputS3Region: str = None,
    OutputS3BucketName: str = None,
    OutputS3KeyPrefix: str = None,
    MaxConcurrency: str = None,
    MaxErrors: str = None,
    ServiceRoleArn: str = None,
    NotificationConfig: "NotificationConfigTypeDef" = None,
    CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef" = None
) -> SendCommandResultTypeDef:
    pass
```

### start_associations_once

Type annotations for `boto3.client("ssm").start_associations_once` method.

[Client.start_associations_once documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.start_associations_once)

```python
def start_associations_once(
    self,
    AssociationIds: List[str]
) -> Dict[str, Any]:
    pass
```

### start_automation_execution

Type annotations for `boto3.client("ssm").start_automation_execution` method.

[Client.start_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.start_automation_execution)

```python
def start_automation_execution(
    self,
    DocumentName: str,
    DocumentVersion: str = None,
    Parameters: Dict[str, List[str]] = None,
    ClientToken: str = None,
    Mode: ExecutionMode = None,
    TargetParameterName: str = None,
    Targets: List["TargetTypeDef"] = None,
    TargetMaps: List[Dict[str, List[str]]] = None,
    MaxConcurrency: str = None,
    MaxErrors: str = None,
    TargetLocations: List["TargetLocationTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> StartAutomationExecutionResultTypeDef:
    pass
```

### start_change_request_execution

Type annotations for `boto3.client("ssm").start_change_request_execution` method.

[Client.start_change_request_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.start_change_request_execution)

```python
def start_change_request_execution(
    self,
    DocumentName: str,
    Runbooks: List["RunbookTypeDef"],
    ScheduledTime: datetime = None,
    DocumentVersion: str = None,
    Parameters: Dict[str, List[str]] = None,
    ChangeRequestName: str = None,
    ClientToken: str = None,
    Tags: List["TagTypeDef"] = None,
    ScheduledEndTime: datetime = None,
    ChangeDetails: str = None
) -> StartChangeRequestExecutionResultTypeDef:
    pass
```

### start_session

Type annotations for `boto3.client("ssm").start_session` method.

[Client.start_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.start_session)

```python
def start_session(
    self,
    Target: str,
    DocumentName: str = None,
    Parameters: Dict[str, List[str]] = None
) -> StartSessionResponseTypeDef:
    pass
```

### stop_automation_execution

Type annotations for `boto3.client("ssm").stop_automation_execution` method.

[Client.stop_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.stop_automation_execution)

```python
def stop_automation_execution(
    self,
    AutomationExecutionId: str,
    Type: StopType = None
) -> Dict[str, Any]:
    pass
```

### terminate_session

Type annotations for `boto3.client("ssm").terminate_session` method.

[Client.terminate_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.terminate_session)

```python
def terminate_session(
    self,
    SessionId: str
) -> TerminateSessionResponseTypeDef:
    pass
```

### unlabel_parameter_version

Type annotations for `boto3.client("ssm").unlabel_parameter_version` method.

[Client.unlabel_parameter_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.unlabel_parameter_version)

```python
def unlabel_parameter_version(
    self,
    Name: str,
    ParameterVersion: int,
    Labels: List[str]
) -> UnlabelParameterVersionResultTypeDef:
    pass
```

### update_association

Type annotations for `boto3.client("ssm").update_association` method.

[Client.update_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_association)

```python
def update_association(
    self,
    AssociationId: str,
    Parameters: Dict[str, List[str]] = None,
    DocumentVersion: str = None,
    ScheduleExpression: str = None,
    OutputLocation: "InstanceAssociationOutputLocationTypeDef" = None,
    Name: str = None,
    Targets: List["TargetTypeDef"] = None,
    AssociationName: str = None,
    AssociationVersion: str = None,
    AutomationTargetParameterName: str = None,
    MaxErrors: str = None,
    MaxConcurrency: str = None,
    ComplianceSeverity: AssociationComplianceSeverity = None,
    SyncCompliance: AssociationSyncCompliance = None,
    ApplyOnlyAtCronInterval: bool = None,
    TargetLocations: List["TargetLocationTypeDef"] = None
) -> UpdateAssociationResultTypeDef:
    pass
```

### update_association_status

Type annotations for `boto3.client("ssm").update_association_status` method.

[Client.update_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_association_status)

```python
def update_association_status(
    self,
    Name: str,
    InstanceId: str,
    AssociationStatus: "AssociationStatusTypeDef"
) -> UpdateAssociationStatusResultTypeDef:
    pass
```

### update_document

Type annotations for `boto3.client("ssm").update_document` method.

[Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_document)

```python
def update_document(
    self,
    Content: str,
    Name: str,
    Attachments: List[AttachmentsSourceTypeDef] = None,
    VersionName: str = None,
    DocumentVersion: str = None,
    DocumentFormat: DocumentFormat = None,
    TargetType: str = None
) -> UpdateDocumentResultTypeDef:
    pass
```

### update_document_default_version

Type annotations for `boto3.client("ssm").update_document_default_version` method.

[Client.update_document_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_document_default_version)

```python
def update_document_default_version(
    self,
    Name: str,
    DocumentVersion: str
) -> UpdateDocumentDefaultVersionResultTypeDef:
    pass
```

### update_document_metadata

Type annotations for `boto3.client("ssm").update_document_metadata` method.

[Client.update_document_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_document_metadata)

```python
def update_document_metadata(
    self,
    Name: str,
    DocumentReviews: DocumentReviewsTypeDef,
    DocumentVersion: str = None
) -> Dict[str, Any]:
    pass
```

### update_maintenance_window

Type annotations for `boto3.client("ssm").update_maintenance_window` method.

[Client.update_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_maintenance_window)

```python
def update_maintenance_window(
    self,
    WindowId: str,
    Name: str = None,
    Description: str = None,
    StartDate: str = None,
    EndDate: str = None,
    Schedule: str = None,
    ScheduleTimezone: str = None,
    ScheduleOffset: int = None,
    Duration: int = None,
    Cutoff: int = None,
    AllowUnassociatedTargets: bool = None,
    Enabled: bool = None,
    Replace: bool = None
) -> UpdateMaintenanceWindowResultTypeDef:
    pass
```

### update_maintenance_window_target

Type annotations for `boto3.client("ssm").update_maintenance_window_target` method.

[Client.update_maintenance_window_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_maintenance_window_target)

```python
def update_maintenance_window_target(
    self,
    WindowId: str,
    WindowTargetId: str,
    Targets: List["TargetTypeDef"] = None,
    OwnerInformation: str = None,
    Name: str = None,
    Description: str = None,
    Replace: bool = None
) -> UpdateMaintenanceWindowTargetResultTypeDef:
    pass
```

### update_maintenance_window_task

Type annotations for `boto3.client("ssm").update_maintenance_window_task` method.

[Client.update_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_maintenance_window_task)

```python
def update_maintenance_window_task(
    self,
    WindowId: str,
    WindowTaskId: str,
    Targets: List["TargetTypeDef"] = None,
    TaskArn: str = None,
    ServiceRoleArn: str = None,
    TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"] = None,
    TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef" = None,
    Priority: int = None,
    MaxConcurrency: str = None,
    MaxErrors: str = None,
    LoggingInfo: "LoggingInfoTypeDef" = None,
    Name: str = None,
    Description: str = None,
    Replace: bool = None
) -> UpdateMaintenanceWindowTaskResultTypeDef:
    pass
```

### update_managed_instance_role

Type annotations for `boto3.client("ssm").update_managed_instance_role` method.

[Client.update_managed_instance_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_managed_instance_role)

```python
def update_managed_instance_role(
    self,
    InstanceId: str,
    IamRole: str
) -> Dict[str, Any]:
    pass
```

### update_ops_item

Type annotations for `boto3.client("ssm").update_ops_item` method.

[Client.update_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_ops_item)

```python
def update_ops_item(
    self,
    OpsItemId: str,
    Description: str = None,
    OperationalData: Dict[str, "OpsItemDataValueTypeDef"] = None,
    OperationalDataToDelete: List[str] = None,
    Notifications: List["OpsItemNotificationTypeDef"] = None,
    Priority: int = None,
    RelatedOpsItems: List["RelatedOpsItemTypeDef"] = None,
    Status: OpsItemStatus = None,
    Title: str = None,
    Category: str = None,
    Severity: str = None,
    ActualStartTime: datetime = None,
    ActualEndTime: datetime = None,
    PlannedStartTime: datetime = None,
    PlannedEndTime: datetime = None
) -> Dict[str, Any]:
    pass
```

### update_ops_metadata

Type annotations for `boto3.client("ssm").update_ops_metadata` method.

[Client.update_ops_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_ops_metadata)

```python
def update_ops_metadata(
    self,
    OpsMetadataArn: str,
    MetadataToUpdate: Dict[str, "MetadataValueTypeDef"] = None,
    KeysToDelete: List[str] = None
) -> UpdateOpsMetadataResultTypeDef:
    pass
```

### update_patch_baseline

Type annotations for `boto3.client("ssm").update_patch_baseline` method.

[Client.update_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_patch_baseline)

```python
def update_patch_baseline(
    self,
    BaselineId: str,
    Name: str = None,
    GlobalFilters: "PatchFilterGroupTypeDef" = None,
    ApprovalRules: "PatchRuleGroupTypeDef" = None,
    ApprovedPatches: List[str] = None,
    ApprovedPatchesComplianceLevel: PatchComplianceLevel = None,
    ApprovedPatchesEnableNonSecurity: bool = None,
    RejectedPatches: List[str] = None,
    RejectedPatchesAction: PatchAction = None,
    Description: str = None,
    Sources: List["PatchSourceTypeDef"] = None,
    Replace: bool = None
) -> UpdatePatchBaselineResultTypeDef:
    pass
```

### update_resource_data_sync

Type annotations for `boto3.client("ssm").update_resource_data_sync` method.

[Client.update_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_resource_data_sync)

```python
def update_resource_data_sync(
    self,
    SyncName: str,
    SyncType: str,
    SyncSource: ResourceDataSyncSourceTypeDef
) -> Dict[str, Any]:
    pass
```

### update_service_setting

Type annotations for `boto3.client("ssm").update_service_setting` method.

[Client.update_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.update_service_setting)

```python
def update_service_setting(
    self,
    SettingId: str,
    SettingValue: str
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeActivations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeActivationsPaginatorName
) -> DescribeActivationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAssociationExecutionTargetsPaginatorName
) -> DescribeAssociationExecutionTargetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAssociationExecutionsPaginatorName
) -> DescribeAssociationExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAutomationExecutionsPaginatorName
) -> DescribeAutomationExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAutomationStepExecutionsPaginatorName
) -> DescribeAutomationStepExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAvailablePatchesPaginatorName
) -> DescribeAvailablePatchesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEffectiveInstanceAssociationsPaginatorName
) -> DescribeEffectiveInstanceAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEffectivePatchesForPatchBaselinePaginatorName
) -> DescribeEffectivePatchesForPatchBaselinePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInstanceAssociationsStatusPaginatorName
) -> DescribeInstanceAssociationsStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInstanceInformationPaginatorName
) -> DescribeInstanceInformationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInstancePatchStatesPaginatorName
) -> DescribeInstancePatchStatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInstancePatchStatesForPatchGroupPaginatorName
) -> DescribeInstancePatchStatesForPatchGroupPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInstancePatchesPaginatorName
) -> DescribeInstancePatchesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeInventoryDeletionsPaginatorName
) -> DescribeInventoryDeletionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName
) -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowExecutionTasksPaginatorName
) -> DescribeMaintenanceWindowExecutionTasksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowExecutionsPaginatorName
) -> DescribeMaintenanceWindowExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowSchedulePaginatorName
) -> DescribeMaintenanceWindowSchedulePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowTargetsPaginatorName
) -> DescribeMaintenanceWindowTargetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowTasksPaginatorName
) -> DescribeMaintenanceWindowTasksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowsPaginatorName
) -> DescribeMaintenanceWindowsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMaintenanceWindowsForTargetPaginatorName
) -> DescribeMaintenanceWindowsForTargetPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeOpsItems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeOpsItemsPaginatorName
) -> DescribeOpsItemsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeParametersPaginatorName
) -> DescribeParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePatchBaselinesPaginatorName
) -> DescribePatchBaselinesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePatchGroupsPaginatorName
) -> DescribePatchGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribePatchProperties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePatchPropertiesPaginatorName
) -> DescribePatchPropertiesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeSessions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSessionsPaginatorName
) -> DescribeSessionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetInventory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetInventoryPaginatorName
) -> GetInventoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)

```python
@overload
def get_paginator(
    self,
    operation_name: GetInventorySchemaPaginatorName
) -> GetInventorySchemaPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.GetOpsSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetOpsSummary)

```python
@overload
def get_paginator(
    self,
    operation_name: GetOpsSummaryPaginatorName
) -> GetOpsSummaryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetParameterHistoryPaginatorName
) -> GetParameterHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)

```python
@overload
def get_paginator(
    self,
    operation_name: GetParametersByPathPaginatorName
) -> GetParametersByPathPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociationVersionsPaginatorName
) -> ListAssociationVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociationsPaginatorName
) -> ListAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCommandInvocationsPaginatorName
) -> ListCommandInvocationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListCommands)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCommandsPaginatorName
) -> ListCommandsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)

```python
@overload
def get_paginator(
    self,
    operation_name: ListComplianceItemsPaginatorName
) -> ListComplianceItemsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)

```python
@overload
def get_paginator(
    self,
    operation_name: ListComplianceSummariesPaginatorName
) -> ListComplianceSummariesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDocumentVersionsPaginatorName
) -> ListDocumentVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListDocuments)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDocumentsPaginatorName
) -> ListDocumentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListOpsItemEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListOpsItemEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOpsItemEventsPaginatorName
) -> ListOpsItemEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListOpsMetadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListOpsMetadata)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOpsMetadataPaginatorName
) -> ListOpsMetadataPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)

```python
@overload
def get_paginator(
    self,
    operation_name: ListResourceComplianceSummariesPaginatorName
) -> ListResourceComplianceSummariesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("ssm").get_paginator` method.

[Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)

```python
@overload
def get_paginator(
    self,
    operation_name: ListResourceDataSyncPaginatorName
) -> ListResourceDataSyncPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("ssm").get_waiter` method.

[Waiter.CommandExecuted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Waiter.CommandExecuted)

```python
def get_waiter(
    self,
    waiter_name: CommandExecutedWaiterName
) -> CommandExecutedWaiter:
    pass
```