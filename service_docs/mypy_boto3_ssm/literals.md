# Literals for boto3 SSM module

> [Index](../index.md) > [SSM](./index.md) > Literals

Auto-generated documentation for [SSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM)
type annotations stubs module [mypy_boto3_ssm](https://pypi.org/project/mypy-boto3-ssm/).

- [Literals for boto3 SSM module](#literals-for-boto3-ssm-module)
  - [AssociationComplianceSeverity](#associationcomplianceseverity)
  - [AssociationExecutionFilterKey](#associationexecutionfilterkey)
  - [AssociationExecutionTargetsFilterKey](#associationexecutiontargetsfilterkey)
  - [AssociationFilterKey](#associationfilterkey)
  - [AssociationFilterOperatorType](#associationfilteroperatortype)
  - [AssociationStatusName](#associationstatusname)
  - [AssociationSyncCompliance](#associationsynccompliance)
  - [AttachmentHashType](#attachmenthashtype)
  - [AttachmentsSourceKey](#attachmentssourcekey)
  - [AutomationExecutionFilterKey](#automationexecutionfilterkey)
  - [AutomationExecutionStatus](#automationexecutionstatus)
  - [AutomationSubtype](#automationsubtype)
  - [AutomationType](#automationtype)
  - [CalendarState](#calendarstate)
  - [CommandExecutedWaiterName](#commandexecutedwaitername)
  - [CommandFilterKey](#commandfilterkey)
  - [CommandInvocationStatus](#commandinvocationstatus)
  - [CommandPluginStatus](#commandpluginstatus)
  - [CommandStatus](#commandstatus)
  - [ComplianceQueryOperatorType](#compliancequeryoperatortype)
  - [ComplianceSeverity](#complianceseverity)
  - [ComplianceStatus](#compliancestatus)
  - [ComplianceUploadType](#complianceuploadtype)
  - [ConnectionStatus](#connectionstatus)
  - [DescribeActivationsFilterKeys](#describeactivationsfilterkeys)
  - [DescribeActivationsPaginatorName](#describeactivationspaginatorname)
  - [DescribeAssociationExecutionTargetsPaginatorName](#describeassociationexecutiontargetspaginatorname)
  - [DescribeAssociationExecutionsPaginatorName](#describeassociationexecutionspaginatorname)
  - [DescribeAutomationExecutionsPaginatorName](#describeautomationexecutionspaginatorname)
  - [DescribeAutomationStepExecutionsPaginatorName](#describeautomationstepexecutionspaginatorname)
  - [DescribeAvailablePatchesPaginatorName](#describeavailablepatchespaginatorname)
  - [DescribeEffectiveInstanceAssociationsPaginatorName](#describeeffectiveinstanceassociationspaginatorname)
  - [DescribeEffectivePatchesForPatchBaselinePaginatorName](#describeeffectivepatchesforpatchbaselinepaginatorname)
  - [DescribeInstanceAssociationsStatusPaginatorName](#describeinstanceassociationsstatuspaginatorname)
  - [DescribeInstanceInformationPaginatorName](#describeinstanceinformationpaginatorname)
  - [DescribeInstancePatchStatesForPatchGroupPaginatorName](#describeinstancepatchstatesforpatchgrouppaginatorname)
  - [DescribeInstancePatchStatesPaginatorName](#describeinstancepatchstatespaginatorname)
  - [DescribeInstancePatchesPaginatorName](#describeinstancepatchespaginatorname)
  - [DescribeInventoryDeletionsPaginatorName](#describeinventorydeletionspaginatorname)
  - [DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName](#describemaintenancewindowexecutiontaskinvocationspaginatorname)
  - [DescribeMaintenanceWindowExecutionTasksPaginatorName](#describemaintenancewindowexecutiontaskspaginatorname)
  - [DescribeMaintenanceWindowExecutionsPaginatorName](#describemaintenancewindowexecutionspaginatorname)
  - [DescribeMaintenanceWindowSchedulePaginatorName](#describemaintenancewindowschedulepaginatorname)
  - [DescribeMaintenanceWindowTargetsPaginatorName](#describemaintenancewindowtargetspaginatorname)
  - [DescribeMaintenanceWindowTasksPaginatorName](#describemaintenancewindowtaskspaginatorname)
  - [DescribeMaintenanceWindowsForTargetPaginatorName](#describemaintenancewindowsfortargetpaginatorname)
  - [DescribeMaintenanceWindowsPaginatorName](#describemaintenancewindowspaginatorname)
  - [DescribeOpsItemsPaginatorName](#describeopsitemspaginatorname)
  - [DescribeParametersPaginatorName](#describeparameterspaginatorname)
  - [DescribePatchBaselinesPaginatorName](#describepatchbaselinespaginatorname)
  - [DescribePatchGroupsPaginatorName](#describepatchgroupspaginatorname)
  - [DescribePatchPropertiesPaginatorName](#describepatchpropertiespaginatorname)
  - [DescribeSessionsPaginatorName](#describesessionspaginatorname)
  - [DocumentFilterKey](#documentfilterkey)
  - [DocumentFormat](#documentformat)
  - [DocumentHashType](#documenthashtype)
  - [DocumentMetadataEnum](#documentmetadataenum)
  - [DocumentParameterType](#documentparametertype)
  - [DocumentPermissionType](#documentpermissiontype)
  - [DocumentReviewAction](#documentreviewaction)
  - [DocumentReviewCommentType](#documentreviewcommenttype)
  - [DocumentStatus](#documentstatus)
  - [DocumentType](#documenttype)
  - [ExecutionMode](#executionmode)
  - [Fault](#fault)
  - [GetInventoryPaginatorName](#getinventorypaginatorname)
  - [GetInventorySchemaPaginatorName](#getinventoryschemapaginatorname)
  - [GetOpsSummaryPaginatorName](#getopssummarypaginatorname)
  - [GetParameterHistoryPaginatorName](#getparameterhistorypaginatorname)
  - [GetParametersByPathPaginatorName](#getparametersbypathpaginatorname)
  - [InstanceInformationFilterKey](#instanceinformationfilterkey)
  - [InstancePatchStateOperatorType](#instancepatchstateoperatortype)
  - [InventoryAttributeDataType](#inventoryattributedatatype)
  - [InventoryDeletionStatus](#inventorydeletionstatus)
  - [InventoryQueryOperatorType](#inventoryqueryoperatortype)
  - [InventorySchemaDeleteOption](#inventoryschemadeleteoption)
  - [LastResourceDataSyncStatus](#lastresourcedatasyncstatus)
  - [ListAssociationVersionsPaginatorName](#listassociationversionspaginatorname)
  - [ListAssociationsPaginatorName](#listassociationspaginatorname)
  - [ListCommandInvocationsPaginatorName](#listcommandinvocationspaginatorname)
  - [ListCommandsPaginatorName](#listcommandspaginatorname)
  - [ListComplianceItemsPaginatorName](#listcomplianceitemspaginatorname)
  - [ListComplianceSummariesPaginatorName](#listcompliancesummariespaginatorname)
  - [ListDocumentVersionsPaginatorName](#listdocumentversionspaginatorname)
  - [ListDocumentsPaginatorName](#listdocumentspaginatorname)
  - [ListOpsItemEventsPaginatorName](#listopsitemeventspaginatorname)
  - [ListOpsMetadataPaginatorName](#listopsmetadatapaginatorname)
  - [ListResourceComplianceSummariesPaginatorName](#listresourcecompliancesummariespaginatorname)
  - [ListResourceDataSyncPaginatorName](#listresourcedatasyncpaginatorname)
  - [MaintenanceWindowExecutionStatus](#maintenancewindowexecutionstatus)
  - [MaintenanceWindowResourceType](#maintenancewindowresourcetype)
  - [MaintenanceWindowTaskType](#maintenancewindowtasktype)
  - [NotificationEvent](#notificationevent)
  - [NotificationType](#notificationtype)
  - [OperatingSystem](#operatingsystem)
  - [OpsFilterOperatorType](#opsfilteroperatortype)
  - [OpsItemDataType](#opsitemdatatype)
  - [OpsItemEventFilterKey](#opsitemeventfilterkey)
  - [OpsItemEventFilterOperator](#opsitemeventfilteroperator)
  - [OpsItemFilterKey](#opsitemfilterkey)
  - [OpsItemFilterOperator](#opsitemfilteroperator)
  - [OpsItemStatus](#opsitemstatus)
  - [ParameterTier](#parametertier)
  - [ParameterType](#parametertype)
  - [ParametersFilterKey](#parametersfilterkey)
  - [PatchAction](#patchaction)
  - [PatchComplianceDataState](#patchcompliancedatastate)
  - [PatchComplianceLevel](#patchcompliancelevel)
  - [PatchDeploymentStatus](#patchdeploymentstatus)
  - [PatchFilterKey](#patchfilterkey)
  - [PatchOperationType](#patchoperationtype)
  - [PatchProperty](#patchproperty)
  - [PatchSet](#patchset)
  - [PingStatus](#pingstatus)
  - [PlatformType](#platformtype)
  - [RebootOption](#rebootoption)
  - [ResourceDataSyncS3Format](#resourcedatasyncs3format)
  - [ResourceType](#resourcetype)
  - [ResourceTypeForTagging](#resourcetypefortagging)
  - [ReviewStatus](#reviewstatus)
  - [SessionFilterKey](#sessionfilterkey)
  - [SessionState](#sessionstate)
  - [SessionStatus](#sessionstatus)
  - [SignalType](#signaltype)
  - [StepExecutionFilterKey](#stepexecutionfilterkey)
  - [StopType](#stoptype)

## AssociationComplianceSeverity

```python
from mypy_boto3_ssm.literals import AssociationComplianceSeverity
```

Values:

- `CRITICAL`
- `HIGH`
- `LOW`
- `MEDIUM`
- `UNSPECIFIED`

## AssociationExecutionFilterKey

```python
from mypy_boto3_ssm.literals import AssociationExecutionFilterKey
```

Values:

- `CreatedTime`
- `ExecutionId`
- `Status`

## AssociationExecutionTargetsFilterKey

```python
from mypy_boto3_ssm.literals import AssociationExecutionTargetsFilterKey
```

Values:

- `ResourceId`
- `ResourceType`
- `Status`

## AssociationFilterKey

```python
from mypy_boto3_ssm.literals import AssociationFilterKey
```

Values:

- `AssociationId`
- `AssociationName`
- `AssociationStatusName`
- `InstanceId`
- `LastExecutedAfter`
- `LastExecutedBefore`
- `Name`
- `ResourceGroupName`

## AssociationFilterOperatorType

```python
from mypy_boto3_ssm.literals import AssociationFilterOperatorType
```

Values:

- `EQUAL`
- `GREATER_THAN`
- `LESS_THAN`

## AssociationStatusName

```python
from mypy_boto3_ssm.literals import AssociationStatusName
```

Values:

- `Failed`
- `Pending`
- `Success`

## AssociationSyncCompliance

```python
from mypy_boto3_ssm.literals import AssociationSyncCompliance
```

Values:

- `AUTO`
- `MANUAL`

## AttachmentHashType

```python
from mypy_boto3_ssm.literals import AttachmentHashType
```

Values:

- `Sha256`

## AttachmentsSourceKey

```python
from mypy_boto3_ssm.literals import AttachmentsSourceKey
```

Values:

- `AttachmentReference`
- `S3FileUrl`
- `SourceUrl`

## AutomationExecutionFilterKey

```python
from mypy_boto3_ssm.literals import AutomationExecutionFilterKey
```

Values:

- `AutomationSubtype`
- `AutomationType`
- `CurrentAction`
- `DocumentNamePrefix`
- `ExecutionId`
- `ExecutionStatus`
- `OpsItemId`
- `ParentExecutionId`
- `StartTimeAfter`
- `StartTimeBefore`
- `TagKey`
- `TargetResourceGroup`

## AutomationExecutionStatus

```python
from mypy_boto3_ssm.literals import AutomationExecutionStatus
```

Values:

- `Approved`
- `Cancelled`
- `Cancelling`
- `ChangeCalendarOverrideApproved`
- `ChangeCalendarOverrideRejected`
- `CompletedWithFailure`
- `CompletedWithSuccess`
- `Failed`
- `InProgress`
- `Pending`
- `PendingApproval`
- `PendingChangeCalendarOverride`
- `Rejected`
- `RunbookInProgress`
- `Scheduled`
- `Success`
- `TimedOut`
- `Waiting`

## AutomationSubtype

```python
from mypy_boto3_ssm.literals import AutomationSubtype
```

Values:

- `ChangeRequest`

## AutomationType

```python
from mypy_boto3_ssm.literals import AutomationType
```

Values:

- `CrossAccount`
- `Local`

## CalendarState

```python
from mypy_boto3_ssm.literals import CalendarState
```

Values:

- `CLOSED`
- `OPEN`

## CommandExecutedWaiterName

```python
from mypy_boto3_ssm.literals import CommandExecutedWaiterName
```

Values:

- `command_executed`

## CommandFilterKey

```python
from mypy_boto3_ssm.literals import CommandFilterKey
```

Values:

- `DocumentName`
- `ExecutionStage`
- `InvokedAfter`
- `InvokedBefore`
- `Status`

## CommandInvocationStatus

```python
from mypy_boto3_ssm.literals import CommandInvocationStatus
```

Values:

- `Cancelled`
- `Cancelling`
- `Delayed`
- `Failed`
- `InProgress`
- `Pending`
- `Success`
- `TimedOut`

## CommandPluginStatus

```python
from mypy_boto3_ssm.literals import CommandPluginStatus
```

Values:

- `Cancelled`
- `Failed`
- `InProgress`
- `Pending`
- `Success`
- `TimedOut`

## CommandStatus

```python
from mypy_boto3_ssm.literals import CommandStatus
```

Values:

- `Cancelled`
- `Cancelling`
- `Failed`
- `InProgress`
- `Pending`
- `Success`
- `TimedOut`

## ComplianceQueryOperatorType

```python
from mypy_boto3_ssm.literals import ComplianceQueryOperatorType
```

Values:

- `BEGIN_WITH`
- `EQUAL`
- `GREATER_THAN`
- `LESS_THAN`
- `NOT_EQUAL`

## ComplianceSeverity

```python
from mypy_boto3_ssm.literals import ComplianceSeverity
```

Values:

- `CRITICAL`
- `HIGH`
- `INFORMATIONAL`
- `LOW`
- `MEDIUM`
- `UNSPECIFIED`

## ComplianceStatus

```python
from mypy_boto3_ssm.literals import ComplianceStatus
```

Values:

- `COMPLIANT`
- `NON_COMPLIANT`

## ComplianceUploadType

```python
from mypy_boto3_ssm.literals import ComplianceUploadType
```

Values:

- `COMPLETE`
- `PARTIAL`

## ConnectionStatus

```python
from mypy_boto3_ssm.literals import ConnectionStatus
```

Values:

- `Connected`
- `NotConnected`

## DescribeActivationsFilterKeys

```python
from mypy_boto3_ssm.literals import DescribeActivationsFilterKeys
```

Values:

- `ActivationIds`
- `DefaultInstanceName`
- `IamRole`

## DescribeActivationsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeActivationsPaginatorName
```

Values:

- `describe_activations`

## DescribeAssociationExecutionTargetsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeAssociationExecutionTargetsPaginatorName
```

Values:

- `describe_association_execution_targets`

## DescribeAssociationExecutionsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeAssociationExecutionsPaginatorName
```

Values:

- `describe_association_executions`

## DescribeAutomationExecutionsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeAutomationExecutionsPaginatorName
```

Values:

- `describe_automation_executions`

## DescribeAutomationStepExecutionsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeAutomationStepExecutionsPaginatorName
```

Values:

- `describe_automation_step_executions`

## DescribeAvailablePatchesPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeAvailablePatchesPaginatorName
```

Values:

- `describe_available_patches`

## DescribeEffectiveInstanceAssociationsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeEffectiveInstanceAssociationsPaginatorName
```

Values:

- `describe_effective_instance_associations`

## DescribeEffectivePatchesForPatchBaselinePaginatorName

```python
from mypy_boto3_ssm.literals import DescribeEffectivePatchesForPatchBaselinePaginatorName
```

Values:

- `describe_effective_patches_for_patch_baseline`

## DescribeInstanceAssociationsStatusPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeInstanceAssociationsStatusPaginatorName
```

Values:

- `describe_instance_associations_status`

## DescribeInstanceInformationPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeInstanceInformationPaginatorName
```

Values:

- `describe_instance_information`

## DescribeInstancePatchStatesForPatchGroupPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeInstancePatchStatesForPatchGroupPaginatorName
```

Values:

- `describe_instance_patch_states_for_patch_group`

## DescribeInstancePatchStatesPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeInstancePatchStatesPaginatorName
```

Values:

- `describe_instance_patch_states`

## DescribeInstancePatchesPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeInstancePatchesPaginatorName
```

Values:

- `describe_instance_patches`

## DescribeInventoryDeletionsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeInventoryDeletionsPaginatorName
```

Values:

- `describe_inventory_deletions`

## DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName
```

Values:

- `describe_maintenance_window_execution_task_invocations`

## DescribeMaintenanceWindowExecutionTasksPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowExecutionTasksPaginatorName
```

Values:

- `describe_maintenance_window_execution_tasks`

## DescribeMaintenanceWindowExecutionsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowExecutionsPaginatorName
```

Values:

- `describe_maintenance_window_executions`

## DescribeMaintenanceWindowSchedulePaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowSchedulePaginatorName
```

Values:

- `describe_maintenance_window_schedule`

## DescribeMaintenanceWindowTargetsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowTargetsPaginatorName
```

Values:

- `describe_maintenance_window_targets`

## DescribeMaintenanceWindowTasksPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowTasksPaginatorName
```

Values:

- `describe_maintenance_window_tasks`

## DescribeMaintenanceWindowsForTargetPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowsForTargetPaginatorName
```

Values:

- `describe_maintenance_windows_for_target`

## DescribeMaintenanceWindowsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeMaintenanceWindowsPaginatorName
```

Values:

- `describe_maintenance_windows`

## DescribeOpsItemsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeOpsItemsPaginatorName
```

Values:

- `describe_ops_items`

## DescribeParametersPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeParametersPaginatorName
```

Values:

- `describe_parameters`

## DescribePatchBaselinesPaginatorName

```python
from mypy_boto3_ssm.literals import DescribePatchBaselinesPaginatorName
```

Values:

- `describe_patch_baselines`

## DescribePatchGroupsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribePatchGroupsPaginatorName
```

Values:

- `describe_patch_groups`

## DescribePatchPropertiesPaginatorName

```python
from mypy_boto3_ssm.literals import DescribePatchPropertiesPaginatorName
```

Values:

- `describe_patch_properties`

## DescribeSessionsPaginatorName

```python
from mypy_boto3_ssm.literals import DescribeSessionsPaginatorName
```

Values:

- `describe_sessions`

## DocumentFilterKey

```python
from mypy_boto3_ssm.literals import DocumentFilterKey
```

Values:

- `DocumentType`
- `Name`
- `Owner`
- `PlatformTypes`

## DocumentFormat

```python
from mypy_boto3_ssm.literals import DocumentFormat
```

Values:

- `JSON`
- `TEXT`
- `YAML`

## DocumentHashType

```python
from mypy_boto3_ssm.literals import DocumentHashType
```

Values:

- `Sha1`
- `Sha256`

## DocumentMetadataEnum

```python
from mypy_boto3_ssm.literals import DocumentMetadataEnum
```

Values:

- `DocumentReviews`

## DocumentParameterType

```python
from mypy_boto3_ssm.literals import DocumentParameterType
```

Values:

- `String`
- `StringList`

## DocumentPermissionType

```python
from mypy_boto3_ssm.literals import DocumentPermissionType
```

Values:

- `Share`

## DocumentReviewAction

```python
from mypy_boto3_ssm.literals import DocumentReviewAction
```

Values:

- `Approve`
- `Reject`
- `SendForReview`
- `UpdateReview`

## DocumentReviewCommentType

```python
from mypy_boto3_ssm.literals import DocumentReviewCommentType
```

Values:

- `Comment`

## DocumentStatus

```python
from mypy_boto3_ssm.literals import DocumentStatus
```

Values:

- `Active`
- `Creating`
- `Deleting`
- `Failed`
- `Updating`

## DocumentType

```python
from mypy_boto3_ssm.literals import DocumentType
```

Values:

- `ApplicationConfiguration`
- `ApplicationConfigurationSchema`
- `Automation`
- `Automation.ChangeTemplate`
- `ChangeCalendar`
- `Command`
- `DeploymentStrategy`
- `Package`
- `Policy`
- `Session`

## ExecutionMode

```python
from mypy_boto3_ssm.literals import ExecutionMode
```

Values:

- `Auto`
- `Interactive`

## Fault

```python
from mypy_boto3_ssm.literals import Fault
```

Values:

- `Client`
- `Server`
- `Unknown`

## GetInventoryPaginatorName

```python
from mypy_boto3_ssm.literals import GetInventoryPaginatorName
```

Values:

- `get_inventory`

## GetInventorySchemaPaginatorName

```python
from mypy_boto3_ssm.literals import GetInventorySchemaPaginatorName
```

Values:

- `get_inventory_schema`

## GetOpsSummaryPaginatorName

```python
from mypy_boto3_ssm.literals import GetOpsSummaryPaginatorName
```

Values:

- `get_ops_summary`

## GetParameterHistoryPaginatorName

```python
from mypy_boto3_ssm.literals import GetParameterHistoryPaginatorName
```

Values:

- `get_parameter_history`

## GetParametersByPathPaginatorName

```python
from mypy_boto3_ssm.literals import GetParametersByPathPaginatorName
```

Values:

- `get_parameters_by_path`

## InstanceInformationFilterKey

```python
from mypy_boto3_ssm.literals import InstanceInformationFilterKey
```

Values:

- `ActivationIds`
- `AgentVersion`
- `AssociationStatus`
- `IamRole`
- `InstanceIds`
- `PingStatus`
- `PlatformTypes`
- `ResourceType`

## InstancePatchStateOperatorType

```python
from mypy_boto3_ssm.literals import InstancePatchStateOperatorType
```

Values:

- `Equal`
- `GreaterThan`
- `LessThan`
- `NotEqual`

## InventoryAttributeDataType

```python
from mypy_boto3_ssm.literals import InventoryAttributeDataType
```

Values:

- `number`
- `string`

## InventoryDeletionStatus

```python
from mypy_boto3_ssm.literals import InventoryDeletionStatus
```

Values:

- `Complete`
- `InProgress`

## InventoryQueryOperatorType

```python
from mypy_boto3_ssm.literals import InventoryQueryOperatorType
```

Values:

- `BeginWith`
- `Equal`
- `Exists`
- `GreaterThan`
- `LessThan`
- `NotEqual`

## InventorySchemaDeleteOption

```python
from mypy_boto3_ssm.literals import InventorySchemaDeleteOption
```

Values:

- `DeleteSchema`
- `DisableSchema`

## LastResourceDataSyncStatus

```python
from mypy_boto3_ssm.literals import LastResourceDataSyncStatus
```

Values:

- `Failed`
- `InProgress`
- `Successful`

## ListAssociationVersionsPaginatorName

```python
from mypy_boto3_ssm.literals import ListAssociationVersionsPaginatorName
```

Values:

- `list_association_versions`

## ListAssociationsPaginatorName

```python
from mypy_boto3_ssm.literals import ListAssociationsPaginatorName
```

Values:

- `list_associations`

## ListCommandInvocationsPaginatorName

```python
from mypy_boto3_ssm.literals import ListCommandInvocationsPaginatorName
```

Values:

- `list_command_invocations`

## ListCommandsPaginatorName

```python
from mypy_boto3_ssm.literals import ListCommandsPaginatorName
```

Values:

- `list_commands`

## ListComplianceItemsPaginatorName

```python
from mypy_boto3_ssm.literals import ListComplianceItemsPaginatorName
```

Values:

- `list_compliance_items`

## ListComplianceSummariesPaginatorName

```python
from mypy_boto3_ssm.literals import ListComplianceSummariesPaginatorName
```

Values:

- `list_compliance_summaries`

## ListDocumentVersionsPaginatorName

```python
from mypy_boto3_ssm.literals import ListDocumentVersionsPaginatorName
```

Values:

- `list_document_versions`

## ListDocumentsPaginatorName

```python
from mypy_boto3_ssm.literals import ListDocumentsPaginatorName
```

Values:

- `list_documents`

## ListOpsItemEventsPaginatorName

```python
from mypy_boto3_ssm.literals import ListOpsItemEventsPaginatorName
```

Values:

- `list_ops_item_events`

## ListOpsMetadataPaginatorName

```python
from mypy_boto3_ssm.literals import ListOpsMetadataPaginatorName
```

Values:

- `list_ops_metadata`

## ListResourceComplianceSummariesPaginatorName

```python
from mypy_boto3_ssm.literals import ListResourceComplianceSummariesPaginatorName
```

Values:

- `list_resource_compliance_summaries`

## ListResourceDataSyncPaginatorName

```python
from mypy_boto3_ssm.literals import ListResourceDataSyncPaginatorName
```

Values:

- `list_resource_data_sync`

## MaintenanceWindowExecutionStatus

```python
from mypy_boto3_ssm.literals import MaintenanceWindowExecutionStatus
```

Values:

- `CANCELLED`
- `CANCELLING`
- `FAILED`
- `IN_PROGRESS`
- `PENDING`
- `SKIPPED_OVERLAPPING`
- `SUCCESS`
- `TIMED_OUT`

## MaintenanceWindowResourceType

```python
from mypy_boto3_ssm.literals import MaintenanceWindowResourceType
```

Values:

- `INSTANCE`
- `RESOURCE_GROUP`

## MaintenanceWindowTaskType

```python
from mypy_boto3_ssm.literals import MaintenanceWindowTaskType
```

Values:

- `AUTOMATION`
- `LAMBDA`
- `RUN_COMMAND`
- `STEP_FUNCTIONS`

## NotificationEvent

```python
from mypy_boto3_ssm.literals import NotificationEvent
```

Values:

- `All`
- `Cancelled`
- `Failed`
- `InProgress`
- `Success`
- `TimedOut`

## NotificationType

```python
from mypy_boto3_ssm.literals import NotificationType
```

Values:

- `Command`
- `Invocation`

## OperatingSystem

```python
from mypy_boto3_ssm.literals import OperatingSystem
```

Values:

- `AMAZON_LINUX`
- `AMAZON_LINUX_2`
- `CENTOS`
- `DEBIAN`
- `MACOS`
- `ORACLE_LINUX`
- `REDHAT_ENTERPRISE_LINUX`
- `SUSE`
- `UBUNTU`
- `WINDOWS`

## OpsFilterOperatorType

```python
from mypy_boto3_ssm.literals import OpsFilterOperatorType
```

Values:

- `BeginWith`
- `Equal`
- `Exists`
- `GreaterThan`
- `LessThan`
- `NotEqual`

## OpsItemDataType

```python
from mypy_boto3_ssm.literals import OpsItemDataType
```

Values:

- `SearchableString`
- `String`

## OpsItemEventFilterKey

```python
from mypy_boto3_ssm.literals import OpsItemEventFilterKey
```

Values:

- `OpsItemId`

## OpsItemEventFilterOperator

```python
from mypy_boto3_ssm.literals import OpsItemEventFilterOperator
```

Values:

- `Equal`

## OpsItemFilterKey

```python
from mypy_boto3_ssm.literals import OpsItemFilterKey
```

Values:

- `ActualEndTime`
- `ActualStartTime`
- `AutomationId`
- `Category`
- `ChangeRequestByApproverArn`
- `ChangeRequestByApproverName`
- `ChangeRequestByRequesterArn`
- `ChangeRequestByRequesterName`
- `ChangeRequestByTargetsResourceGroup`
- `ChangeRequestByTemplate`
- `CreatedBy`
- `CreatedTime`
- `LastModifiedTime`
- `OperationalData`
- `OperationalDataKey`
- `OperationalDataValue`
- `OpsItemId`
- `OpsItemType`
- `PlannedEndTime`
- `PlannedStartTime`
- `Priority`
- `ResourceId`
- `Severity`
- `Source`
- `Status`
- `Title`

## OpsItemFilterOperator

```python
from mypy_boto3_ssm.literals import OpsItemFilterOperator
```

Values:

- `Contains`
- `Equal`
- `GreaterThan`
- `LessThan`

## OpsItemStatus

```python
from mypy_boto3_ssm.literals import OpsItemStatus
```

Values:

- `Approved`
- `Cancelled`
- `Cancelling`
- `ChangeCalendarOverrideApproved`
- `ChangeCalendarOverrideRejected`
- `CompletedWithFailure`
- `CompletedWithSuccess`
- `Failed`
- `InProgress`
- `Open`
- `Pending`
- `PendingApproval`
- `PendingChangeCalendarOverride`
- `Rejected`
- `Resolved`
- `RunbookInProgress`
- `Scheduled`
- `TimedOut`

## ParameterTier

```python
from mypy_boto3_ssm.literals import ParameterTier
```

Values:

- `Advanced`
- `Intelligent-Tiering`
- `Standard`

## ParameterType

```python
from mypy_boto3_ssm.literals import ParameterType
```

Values:

- `SecureString`
- `String`
- `StringList`

## ParametersFilterKey

```python
from mypy_boto3_ssm.literals import ParametersFilterKey
```

Values:

- `KeyId`
- `Name`
- `Type`

## PatchAction

```python
from mypy_boto3_ssm.literals import PatchAction
```

Values:

- `ALLOW_AS_DEPENDENCY`
- `BLOCK`

## PatchComplianceDataState

```python
from mypy_boto3_ssm.literals import PatchComplianceDataState
```

Values:

- `FAILED`
- `INSTALLED`
- `INSTALLED_OTHER`
- `INSTALLED_PENDING_REBOOT`
- `INSTALLED_REJECTED`
- `MISSING`
- `NOT_APPLICABLE`

## PatchComplianceLevel

```python
from mypy_boto3_ssm.literals import PatchComplianceLevel
```

Values:

- `CRITICAL`
- `HIGH`
- `INFORMATIONAL`
- `LOW`
- `MEDIUM`
- `UNSPECIFIED`

## PatchDeploymentStatus

```python
from mypy_boto3_ssm.literals import PatchDeploymentStatus
```

Values:

- `APPROVED`
- `EXPLICIT_APPROVED`
- `EXPLICIT_REJECTED`
- `PENDING_APPROVAL`

## PatchFilterKey

```python
from mypy_boto3_ssm.literals import PatchFilterKey
```

Values:

- `ADVISORY_ID`
- `ARCH`
- `BUGZILLA_ID`
- `CLASSIFICATION`
- `CVE_ID`
- `EPOCH`
- `MSRC_SEVERITY`
- `NAME`
- `PATCH_ID`
- `PATCH_SET`
- `PRIORITY`
- `PRODUCT`
- `PRODUCT_FAMILY`
- `RELEASE`
- `REPOSITORY`
- `SECTION`
- `SECURITY`
- `SEVERITY`
- `VERSION`

## PatchOperationType

```python
from mypy_boto3_ssm.literals import PatchOperationType
```

Values:

- `Install`
- `Scan`

## PatchProperty

```python
from mypy_boto3_ssm.literals import PatchProperty
```

Values:

- `CLASSIFICATION`
- `MSRC_SEVERITY`
- `PRIORITY`
- `PRODUCT`
- `PRODUCT_FAMILY`
- `SEVERITY`

## PatchSet

```python
from mypy_boto3_ssm.literals import PatchSet
```

Values:

- `APPLICATION`
- `OS`

## PingStatus

```python
from mypy_boto3_ssm.literals import PingStatus
```

Values:

- `ConnectionLost`
- `Inactive`
- `Online`

## PlatformType

```python
from mypy_boto3_ssm.literals import PlatformType
```

Values:

- `Linux`
- `Windows`

## RebootOption

```python
from mypy_boto3_ssm.literals import RebootOption
```

Values:

- `NoReboot`
- `RebootIfNeeded`

## ResourceDataSyncS3Format

```python
from mypy_boto3_ssm.literals import ResourceDataSyncS3Format
```

Values:

- `JsonSerDe`

## ResourceType

```python
from mypy_boto3_ssm.literals import ResourceType
```

Values:

- `Document`
- `EC2Instance`
- `ManagedInstance`

## ResourceTypeForTagging

```python
from mypy_boto3_ssm.literals import ResourceTypeForTagging
```

Values:

- `Document`
- `MaintenanceWindow`
- `ManagedInstance`
- `OpsItem`
- `OpsMetadata`
- `Parameter`
- `PatchBaseline`

## ReviewStatus

```python
from mypy_boto3_ssm.literals import ReviewStatus
```

Values:

- `APPROVED`
- `NOT_REVIEWED`
- `PENDING`
- `REJECTED`

## SessionFilterKey

```python
from mypy_boto3_ssm.literals import SessionFilterKey
```

Values:

- `InvokedAfter`
- `InvokedBefore`
- `Owner`
- `SessionId`
- `Status`
- `Target`

## SessionState

```python
from mypy_boto3_ssm.literals import SessionState
```

Values:

- `Active`
- `History`

## SessionStatus

```python
from mypy_boto3_ssm.literals import SessionStatus
```

Values:

- `Connected`
- `Connecting`
- `Disconnected`
- `Failed`
- `Terminated`
- `Terminating`

## SignalType

```python
from mypy_boto3_ssm.literals import SignalType
```

Values:

- `Approve`
- `Reject`
- `Resume`
- `StartStep`
- `StopStep`

## StepExecutionFilterKey

```python
from mypy_boto3_ssm.literals import StepExecutionFilterKey
```

Values:

- `Action`
- `StartTimeAfter`
- `StartTimeBefore`
- `StepExecutionId`
- `StepExecutionStatus`
- `StepName`

## StopType

```python
from mypy_boto3_ssm.literals import StopType
```

Values:

- `Cancel`
- `Complete`
