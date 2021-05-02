# Structures for boto3 SSM module

> [Index](../index.md) > [SSM](./index.md) > Structures

Auto-generated documentation for [SSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM)
type annotations stubs module [mypy_boto3_ssm](https://pypi.org/project/mypy-boto3-ssm/).

- [Structures for boto3 SSM module](#structures-for-boto3-ssm-module)
  - [AccountSharingInfoTypeDef](#accountsharinginfotypedef)
  - [ActivationTypeDef](#activationtypedef)
  - [AssociationDescriptionTypeDef](#associationdescriptiontypedef)
  - [AssociationExecutionTargetTypeDef](#associationexecutiontargettypedef)
  - [AssociationExecutionTypeDef](#associationexecutiontypedef)
  - [AssociationOverviewTypeDef](#associationoverviewtypedef)
  - [AssociationStatusTypeDef](#associationstatustypedef)
  - [AssociationTypeDef](#associationtypedef)
  - [AssociationVersionInfoTypeDef](#associationversioninfotypedef)
  - [AttachmentContentTypeDef](#attachmentcontenttypedef)
  - [AttachmentInformationTypeDef](#attachmentinformationtypedef)
  - [AutomationExecutionMetadataTypeDef](#automationexecutionmetadatatypedef)
  - [AutomationExecutionTypeDef](#automationexecutiontypedef)
  - [CloudWatchOutputConfigTypeDef](#cloudwatchoutputconfigtypedef)
  - [CommandInvocationTypeDef](#commandinvocationtypedef)
  - [CommandPluginTypeDef](#commandplugintypedef)
  - [CommandTypeDef](#commandtypedef)
  - [ComplianceExecutionSummaryTypeDef](#complianceexecutionsummarytypedef)
  - [ComplianceItemTypeDef](#complianceitemtypedef)
  - [ComplianceSummaryItemTypeDef](#compliancesummaryitemtypedef)
  - [CompliantSummaryTypeDef](#compliantsummarytypedef)
  - [CreateAssociationBatchRequestEntryTypeDef](#createassociationbatchrequestentrytypedef)
  - [DocumentDefaultVersionDescriptionTypeDef](#documentdefaultversiondescriptiontypedef)
  - [DocumentDescriptionTypeDef](#documentdescriptiontypedef)
  - [DocumentIdentifierTypeDef](#documentidentifiertypedef)
  - [DocumentMetadataResponseInfoTypeDef](#documentmetadataresponseinfotypedef)
  - [DocumentParameterTypeDef](#documentparametertypedef)
  - [DocumentRequiresTypeDef](#documentrequirestypedef)
  - [DocumentReviewCommentSourceTypeDef](#documentreviewcommentsourcetypedef)
  - [DocumentReviewerResponseSourceTypeDef](#documentreviewerresponsesourcetypedef)
  - [DocumentVersionInfoTypeDef](#documentversioninfotypedef)
  - [EffectivePatchTypeDef](#effectivepatchtypedef)
  - [FailedCreateAssociationTypeDef](#failedcreateassociationtypedef)
  - [FailureDetailsTypeDef](#failuredetailstypedef)
  - [InstanceAggregatedAssociationOverviewTypeDef](#instanceaggregatedassociationoverviewtypedef)
  - [InstanceAssociationOutputLocationTypeDef](#instanceassociationoutputlocationtypedef)
  - [InstanceAssociationOutputUrlTypeDef](#instanceassociationoutputurltypedef)
  - [InstanceAssociationStatusInfoTypeDef](#instanceassociationstatusinfotypedef)
  - [InstanceAssociationTypeDef](#instanceassociationtypedef)
  - [InstanceInformationTypeDef](#instanceinformationtypedef)
  - [InstancePatchStateTypeDef](#instancepatchstatetypedef)
  - [InventoryDeletionStatusItemTypeDef](#inventorydeletionstatusitemtypedef)
  - [InventoryDeletionSummaryItemTypeDef](#inventorydeletionsummaryitemtypedef)
  - [InventoryDeletionSummaryTypeDef](#inventorydeletionsummarytypedef)
  - [InventoryFilterTypeDef](#inventoryfiltertypedef)
  - [InventoryGroupTypeDef](#inventorygrouptypedef)
  - [InventoryItemAttributeTypeDef](#inventoryitemattributetypedef)
  - [InventoryItemSchemaTypeDef](#inventoryitemschematypedef)
  - [InventoryResultEntityTypeDef](#inventoryresultentitytypedef)
  - [InventoryResultItemTypeDef](#inventoryresultitemtypedef)
  - [LoggingInfoTypeDef](#logginginfotypedef)
  - [MaintenanceWindowAutomationParametersTypeDef](#maintenancewindowautomationparameterstypedef)
  - [MaintenanceWindowExecutionTaskIdentityTypeDef](#maintenancewindowexecutiontaskidentitytypedef)
  - [MaintenanceWindowExecutionTaskInvocationIdentityTypeDef](#maintenancewindowexecutiontaskinvocationidentitytypedef)
  - [MaintenanceWindowExecutionTypeDef](#maintenancewindowexecutiontypedef)
  - [MaintenanceWindowIdentityForTargetTypeDef](#maintenancewindowidentityfortargettypedef)
  - [MaintenanceWindowIdentityTypeDef](#maintenancewindowidentitytypedef)
  - [MaintenanceWindowLambdaParametersTypeDef](#maintenancewindowlambdaparameterstypedef)
  - [MaintenanceWindowRunCommandParametersTypeDef](#maintenancewindowruncommandparameterstypedef)
  - [MaintenanceWindowStepFunctionsParametersTypeDef](#maintenancewindowstepfunctionsparameterstypedef)
  - [MaintenanceWindowTargetTypeDef](#maintenancewindowtargettypedef)
  - [MaintenanceWindowTaskInvocationParametersTypeDef](#maintenancewindowtaskinvocationparameterstypedef)
  - [MaintenanceWindowTaskParameterValueExpressionTypeDef](#maintenancewindowtaskparametervalueexpressiontypedef)
  - [MaintenanceWindowTaskTypeDef](#maintenancewindowtasktypedef)
  - [MetadataValueTypeDef](#metadatavaluetypedef)
  - [NonCompliantSummaryTypeDef](#noncompliantsummarytypedef)
  - [NotificationConfigTypeDef](#notificationconfigtypedef)
  - [OpsEntityItemTypeDef](#opsentityitemtypedef)
  - [OpsEntityTypeDef](#opsentitytypedef)
  - [OpsFilterTypeDef](#opsfiltertypedef)
  - [OpsItemDataValueTypeDef](#opsitemdatavaluetypedef)
  - [OpsItemEventSummaryTypeDef](#opsitemeventsummarytypedef)
  - [OpsItemIdentityTypeDef](#opsitemidentitytypedef)
  - [OpsItemNotificationTypeDef](#opsitemnotificationtypedef)
  - [OpsItemSummaryTypeDef](#opsitemsummarytypedef)
  - [OpsItemTypeDef](#opsitemtypedef)
  - [OpsMetadataTypeDef](#opsmetadatatypedef)
  - [OutputSourceTypeDef](#outputsourcetypedef)
  - [ParameterHistoryTypeDef](#parameterhistorytypedef)
  - [ParameterInlinePolicyTypeDef](#parameterinlinepolicytypedef)
  - [ParameterMetadataTypeDef](#parametermetadatatypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [PatchBaselineIdentityTypeDef](#patchbaselineidentitytypedef)
  - [PatchComplianceDataTypeDef](#patchcompliancedatatypedef)
  - [PatchFilterGroupTypeDef](#patchfiltergrouptypedef)
  - [PatchFilterTypeDef](#patchfiltertypedef)
  - [PatchGroupPatchBaselineMappingTypeDef](#patchgrouppatchbaselinemappingtypedef)
  - [PatchRuleGroupTypeDef](#patchrulegrouptypedef)
  - [PatchRuleTypeDef](#patchruletypedef)
  - [PatchSourceTypeDef](#patchsourcetypedef)
  - [PatchStatusTypeDef](#patchstatustypedef)
  - [PatchTypeDef](#patchtypedef)
  - [ProgressCountersTypeDef](#progresscounterstypedef)
  - [RelatedOpsItemTypeDef](#relatedopsitemtypedef)
  - [ResolvedTargetsTypeDef](#resolvedtargetstypedef)
  - [ResourceComplianceSummaryItemTypeDef](#resourcecompliancesummaryitemtypedef)
  - [ResourceDataSyncAwsOrganizationsSourceTypeDef](#resourcedatasyncawsorganizationssourcetypedef)
  - [ResourceDataSyncDestinationDataSharingTypeDef](#resourcedatasyncdestinationdatasharingtypedef)
  - [ResourceDataSyncItemTypeDef](#resourcedatasyncitemtypedef)
  - [ResourceDataSyncOrganizationalUnitTypeDef](#resourcedatasyncorganizationalunittypedef)
  - [ResourceDataSyncS3DestinationTypeDef](#resourcedatasyncs3destinationtypedef)
  - [ResourceDataSyncSourceWithStateTypeDef](#resourcedatasyncsourcewithstatetypedef)
  - [ReviewInformationTypeDef](#reviewinformationtypedef)
  - [RunbookTypeDef](#runbooktypedef)
  - [S3OutputLocationTypeDef](#s3outputlocationtypedef)
  - [S3OutputUrlTypeDef](#s3outputurltypedef)
  - [ScheduledWindowExecutionTypeDef](#scheduledwindowexecutiontypedef)
  - [ServiceSettingTypeDef](#servicesettingtypedef)
  - [SessionManagerOutputUrlTypeDef](#sessionmanageroutputurltypedef)
  - [SessionTypeDef](#sessiontypedef)
  - [SeveritySummaryTypeDef](#severitysummarytypedef)
  - [StepExecutionTypeDef](#stepexecutiontypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetLocationTypeDef](#targetlocationtypedef)
  - [TargetTypeDef](#targettypedef)
  - [AssociationExecutionFilterTypeDef](#associationexecutionfiltertypedef)
  - [AssociationExecutionTargetsFilterTypeDef](#associationexecutiontargetsfiltertypedef)
  - [AssociationFilterTypeDef](#associationfiltertypedef)
  - [AttachmentsSourceTypeDef](#attachmentssourcetypedef)
  - [AutomationExecutionFilterTypeDef](#automationexecutionfiltertypedef)
  - [BaselineOverrideTypeDef](#baselineoverridetypedef)
  - [CancelMaintenanceWindowExecutionResultTypeDef](#cancelmaintenancewindowexecutionresulttypedef)
  - [CommandFilterTypeDef](#commandfiltertypedef)
  - [ComplianceItemEntryTypeDef](#complianceitementrytypedef)
  - [ComplianceStringFilterTypeDef](#compliancestringfiltertypedef)
  - [CreateActivationResultTypeDef](#createactivationresulttypedef)
  - [CreateAssociationBatchResultTypeDef](#createassociationbatchresulttypedef)
  - [CreateAssociationResultTypeDef](#createassociationresulttypedef)
  - [CreateDocumentResultTypeDef](#createdocumentresulttypedef)
  - [CreateMaintenanceWindowResultTypeDef](#createmaintenancewindowresulttypedef)
  - [CreateOpsItemResponseTypeDef](#createopsitemresponsetypedef)
  - [CreateOpsMetadataResultTypeDef](#createopsmetadataresulttypedef)
  - [CreatePatchBaselineResultTypeDef](#createpatchbaselineresulttypedef)
  - [DeleteInventoryResultTypeDef](#deleteinventoryresulttypedef)
  - [DeleteMaintenanceWindowResultTypeDef](#deletemaintenancewindowresulttypedef)
  - [DeleteParametersResultTypeDef](#deleteparametersresulttypedef)
  - [DeletePatchBaselineResultTypeDef](#deletepatchbaselineresulttypedef)
  - [DeregisterPatchBaselineForPatchGroupResultTypeDef](#deregisterpatchbaselineforpatchgroupresulttypedef)
  - [DeregisterTargetFromMaintenanceWindowResultTypeDef](#deregistertargetfrommaintenancewindowresulttypedef)
  - [DeregisterTaskFromMaintenanceWindowResultTypeDef](#deregistertaskfrommaintenancewindowresulttypedef)
  - [DescribeActivationsFilterTypeDef](#describeactivationsfiltertypedef)
  - [DescribeActivationsResultTypeDef](#describeactivationsresulttypedef)
  - [DescribeAssociationExecutionTargetsResultTypeDef](#describeassociationexecutiontargetsresulttypedef)
  - [DescribeAssociationExecutionsResultTypeDef](#describeassociationexecutionsresulttypedef)
  - [DescribeAssociationResultTypeDef](#describeassociationresulttypedef)
  - [DescribeAutomationExecutionsResultTypeDef](#describeautomationexecutionsresulttypedef)
  - [DescribeAutomationStepExecutionsResultTypeDef](#describeautomationstepexecutionsresulttypedef)
  - [DescribeAvailablePatchesResultTypeDef](#describeavailablepatchesresulttypedef)
  - [DescribeDocumentPermissionResponseTypeDef](#describedocumentpermissionresponsetypedef)
  - [DescribeDocumentResultTypeDef](#describedocumentresulttypedef)
  - [DescribeEffectiveInstanceAssociationsResultTypeDef](#describeeffectiveinstanceassociationsresulttypedef)
  - [DescribeEffectivePatchesForPatchBaselineResultTypeDef](#describeeffectivepatchesforpatchbaselineresulttypedef)
  - [DescribeInstanceAssociationsStatusResultTypeDef](#describeinstanceassociationsstatusresulttypedef)
  - [DescribeInstanceInformationResultTypeDef](#describeinstanceinformationresulttypedef)
  - [DescribeInstancePatchStatesForPatchGroupResultTypeDef](#describeinstancepatchstatesforpatchgroupresulttypedef)
  - [DescribeInstancePatchStatesResultTypeDef](#describeinstancepatchstatesresulttypedef)
  - [DescribeInstancePatchesResultTypeDef](#describeinstancepatchesresulttypedef)
  - [DescribeInventoryDeletionsResultTypeDef](#describeinventorydeletionsresulttypedef)
  - [DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef](#describemaintenancewindowexecutiontaskinvocationsresulttypedef)
  - [DescribeMaintenanceWindowExecutionTasksResultTypeDef](#describemaintenancewindowexecutiontasksresulttypedef)
  - [DescribeMaintenanceWindowExecutionsResultTypeDef](#describemaintenancewindowexecutionsresulttypedef)
  - [DescribeMaintenanceWindowScheduleResultTypeDef](#describemaintenancewindowscheduleresulttypedef)
  - [DescribeMaintenanceWindowTargetsResultTypeDef](#describemaintenancewindowtargetsresulttypedef)
  - [DescribeMaintenanceWindowTasksResultTypeDef](#describemaintenancewindowtasksresulttypedef)
  - [DescribeMaintenanceWindowsForTargetResultTypeDef](#describemaintenancewindowsfortargetresulttypedef)
  - [DescribeMaintenanceWindowsResultTypeDef](#describemaintenancewindowsresulttypedef)
  - [DescribeOpsItemsResponseTypeDef](#describeopsitemsresponsetypedef)
  - [DescribeParametersResultTypeDef](#describeparametersresulttypedef)
  - [DescribePatchBaselinesResultTypeDef](#describepatchbaselinesresulttypedef)
  - [DescribePatchGroupStateResultTypeDef](#describepatchgroupstateresulttypedef)
  - [DescribePatchGroupsResultTypeDef](#describepatchgroupsresulttypedef)
  - [DescribePatchPropertiesResultTypeDef](#describepatchpropertiesresulttypedef)
  - [DescribeSessionsResponseTypeDef](#describesessionsresponsetypedef)
  - [OpsAggregatorTypeDef](#opsaggregatortypedef)
  - [InventoryAggregatorTypeDef](#inventoryaggregatortypedef)
  - [DocumentFilterTypeDef](#documentfiltertypedef)
  - [DocumentKeyValuesFilterTypeDef](#documentkeyvaluesfiltertypedef)
  - [DocumentReviewsTypeDef](#documentreviewstypedef)
  - [GetAutomationExecutionResultTypeDef](#getautomationexecutionresulttypedef)
  - [GetCalendarStateResponseTypeDef](#getcalendarstateresponsetypedef)
  - [GetCommandInvocationResultTypeDef](#getcommandinvocationresulttypedef)
  - [GetConnectionStatusResponseTypeDef](#getconnectionstatusresponsetypedef)
  - [GetDefaultPatchBaselineResultTypeDef](#getdefaultpatchbaselineresulttypedef)
  - [GetDeployablePatchSnapshotForInstanceResultTypeDef](#getdeployablepatchsnapshotforinstanceresulttypedef)
  - [GetDocumentResultTypeDef](#getdocumentresulttypedef)
  - [GetInventoryResultTypeDef](#getinventoryresulttypedef)
  - [GetInventorySchemaResultTypeDef](#getinventoryschemaresulttypedef)
  - [GetMaintenanceWindowExecutionResultTypeDef](#getmaintenancewindowexecutionresulttypedef)
  - [GetMaintenanceWindowExecutionTaskInvocationResultTypeDef](#getmaintenancewindowexecutiontaskinvocationresulttypedef)
  - [GetMaintenanceWindowExecutionTaskResultTypeDef](#getmaintenancewindowexecutiontaskresulttypedef)
  - [GetMaintenanceWindowResultTypeDef](#getmaintenancewindowresulttypedef)
  - [GetMaintenanceWindowTaskResultTypeDef](#getmaintenancewindowtaskresulttypedef)
  - [GetOpsItemResponseTypeDef](#getopsitemresponsetypedef)
  - [GetOpsMetadataResultTypeDef](#getopsmetadataresulttypedef)
  - [GetOpsSummaryResultTypeDef](#getopssummaryresulttypedef)
  - [GetParameterHistoryResultTypeDef](#getparameterhistoryresulttypedef)
  - [GetParameterResultTypeDef](#getparameterresulttypedef)
  - [GetParametersByPathResultTypeDef](#getparametersbypathresulttypedef)
  - [GetParametersResultTypeDef](#getparametersresulttypedef)
  - [GetPatchBaselineForPatchGroupResultTypeDef](#getpatchbaselineforpatchgroupresulttypedef)
  - [GetPatchBaselineResultTypeDef](#getpatchbaselineresulttypedef)
  - [GetServiceSettingResultTypeDef](#getservicesettingresulttypedef)
  - [InstanceInformationFilterTypeDef](#instanceinformationfiltertypedef)
  - [InstanceInformationStringFilterTypeDef](#instanceinformationstringfiltertypedef)
  - [InstancePatchStateFilterTypeDef](#instancepatchstatefiltertypedef)
  - [InventoryItemTypeDef](#inventoryitemtypedef)
  - [LabelParameterVersionResultTypeDef](#labelparameterversionresulttypedef)
  - [ListAssociationVersionsResultTypeDef](#listassociationversionsresulttypedef)
  - [ListAssociationsResultTypeDef](#listassociationsresulttypedef)
  - [ListCommandInvocationsResultTypeDef](#listcommandinvocationsresulttypedef)
  - [ListCommandsResultTypeDef](#listcommandsresulttypedef)
  - [ListComplianceItemsResultTypeDef](#listcomplianceitemsresulttypedef)
  - [ListComplianceSummariesResultTypeDef](#listcompliancesummariesresulttypedef)
  - [ListDocumentMetadataHistoryResponseTypeDef](#listdocumentmetadatahistoryresponsetypedef)
  - [ListDocumentVersionsResultTypeDef](#listdocumentversionsresulttypedef)
  - [ListDocumentsResultTypeDef](#listdocumentsresulttypedef)
  - [ListInventoryEntriesResultTypeDef](#listinventoryentriesresulttypedef)
  - [ListOpsItemEventsResponseTypeDef](#listopsitemeventsresponsetypedef)
  - [ListOpsMetadataResultTypeDef](#listopsmetadataresulttypedef)
  - [ListResourceComplianceSummariesResultTypeDef](#listresourcecompliancesummariesresulttypedef)
  - [ListResourceDataSyncResultTypeDef](#listresourcedatasyncresulttypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [MaintenanceWindowFilterTypeDef](#maintenancewindowfiltertypedef)
  - [OpsItemEventFilterTypeDef](#opsitemeventfiltertypedef)
  - [OpsItemFilterTypeDef](#opsitemfiltertypedef)
  - [OpsMetadataFilterTypeDef](#opsmetadatafiltertypedef)
  - [OpsResultAttributeTypeDef](#opsresultattributetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParameterStringFilterTypeDef](#parameterstringfiltertypedef)
  - [ParametersFilterTypeDef](#parametersfiltertypedef)
  - [PatchOrchestratorFilterTypeDef](#patchorchestratorfiltertypedef)
  - [PutInventoryResultTypeDef](#putinventoryresulttypedef)
  - [PutParameterResultTypeDef](#putparameterresulttypedef)
  - [RegisterDefaultPatchBaselineResultTypeDef](#registerdefaultpatchbaselineresulttypedef)
  - [RegisterPatchBaselineForPatchGroupResultTypeDef](#registerpatchbaselineforpatchgroupresulttypedef)
  - [RegisterTargetWithMaintenanceWindowResultTypeDef](#registertargetwithmaintenancewindowresulttypedef)
  - [RegisterTaskWithMaintenanceWindowResultTypeDef](#registertaskwithmaintenancewindowresulttypedef)
  - [ResetServiceSettingResultTypeDef](#resetservicesettingresulttypedef)
  - [ResourceDataSyncSourceTypeDef](#resourcedatasyncsourcetypedef)
  - [ResultAttributeTypeDef](#resultattributetypedef)
  - [ResumeSessionResponseTypeDef](#resumesessionresponsetypedef)
  - [SendCommandResultTypeDef](#sendcommandresulttypedef)
  - [SessionFilterTypeDef](#sessionfiltertypedef)
  - [StartAutomationExecutionResultTypeDef](#startautomationexecutionresulttypedef)
  - [StartChangeRequestExecutionResultTypeDef](#startchangerequestexecutionresulttypedef)
  - [StartSessionResponseTypeDef](#startsessionresponsetypedef)
  - [StepExecutionFilterTypeDef](#stepexecutionfiltertypedef)
  - [TerminateSessionResponseTypeDef](#terminatesessionresponsetypedef)
  - [UnlabelParameterVersionResultTypeDef](#unlabelparameterversionresulttypedef)
  - [UpdateAssociationResultTypeDef](#updateassociationresulttypedef)
  - [UpdateAssociationStatusResultTypeDef](#updateassociationstatusresulttypedef)
  - [UpdateDocumentDefaultVersionResultTypeDef](#updatedocumentdefaultversionresulttypedef)
  - [UpdateDocumentResultTypeDef](#updatedocumentresulttypedef)
  - [UpdateMaintenanceWindowResultTypeDef](#updatemaintenancewindowresulttypedef)
  - [UpdateMaintenanceWindowTargetResultTypeDef](#updatemaintenancewindowtargetresulttypedef)
  - [UpdateMaintenanceWindowTaskResultTypeDef](#updatemaintenancewindowtaskresulttypedef)
  - [UpdateOpsMetadataResultTypeDef](#updateopsmetadataresulttypedef)
  - [UpdatePatchBaselineResultTypeDef](#updatepatchbaselineresulttypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountSharingInfoTypeDef

```python
from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef
```




Optional fields:
- `AccountId`: `str`
- `SharedDocumentVersion`: `str`


## ActivationTypeDef

```python
from mypy_boto3_ssm.type_defs import ActivationTypeDef
```




Optional fields:
- `ActivationId`: `str`
- `Description`: `str`
- `DefaultInstanceName`: `str`
- `IamRole`: `str`
- `RegistrationLimit`: `int`
- `RegistrationsCount`: `int`
- `ExpirationDate`: `datetime`
- `Expired`: `bool`
- `CreatedDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## AssociationDescriptionTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationDescriptionTypeDef
```




Optional fields:
- `Name`: `str`
- `InstanceId`: `str`
- `AssociationVersion`: `str`
- `Date`: `datetime`
- `LastUpdateAssociationDate`: `datetime`
- `Status`: `"AssociationStatusTypeDef"`
- `Overview`: `"AssociationOverviewTypeDef"`
- `DocumentVersion`: `str`
- `AutomationTargetParameterName`: `str`
- `Parameters`: `Dict[str, List[str]]`
- `AssociationId`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `ScheduleExpression`: `str`
- `OutputLocation`: `"InstanceAssociationOutputLocationTypeDef"`
- `LastExecutionDate`: `datetime`
- `LastSuccessfulExecutionDate`: `datetime`
- `AssociationName`: `str`
- `MaxErrors`: `str`
- `MaxConcurrency`: `str`
- `ComplianceSeverity`: `AssociationComplianceSeverity`
- `SyncCompliance`: `AssociationSyncCompliance`
- `ApplyOnlyAtCronInterval`: `bool`
- `TargetLocations`: `List["TargetLocationTypeDef"]`


## AssociationExecutionTargetTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationExecutionTargetTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `AssociationVersion`: `str`
- `ExecutionId`: `str`
- `ResourceId`: `str`
- `ResourceType`: `str`
- `Status`: `str`
- `DetailedStatus`: `str`
- `LastExecutionDate`: `datetime`
- `OutputSource`: `"OutputSourceTypeDef"`


## AssociationExecutionTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationExecutionTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `AssociationVersion`: `str`
- `ExecutionId`: `str`
- `Status`: `str`
- `DetailedStatus`: `str`
- `CreatedTime`: `datetime`
- `LastExecutionDate`: `datetime`
- `ResourceCountByStatus`: `str`


## AssociationOverviewTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationOverviewTypeDef
```




Optional fields:
- `Status`: `str`
- `DetailedStatus`: `str`
- `AssociationStatusAggregatedCount`: `Dict[str, int]`


## AssociationStatusTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationStatusTypeDef
```


Required fields:
- `Date`: `datetime`
- `Name`: `AssociationStatusName`
- `Message`: `str`



Optional fields:
- `AdditionalInfo`: `str`


## AssociationTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationTypeDef
```




Optional fields:
- `Name`: `str`
- `InstanceId`: `str`
- `AssociationId`: `str`
- `AssociationVersion`: `str`
- `DocumentVersion`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `LastExecutionDate`: `datetime`
- `Overview`: `"AssociationOverviewTypeDef"`
- `ScheduleExpression`: `str`
- `AssociationName`: `str`


## AssociationVersionInfoTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationVersionInfoTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `AssociationVersion`: `str`
- `CreatedDate`: `datetime`
- `Name`: `str`
- `DocumentVersion`: `str`
- `Parameters`: `Dict[str, List[str]]`
- `Targets`: `List["TargetTypeDef"]`
- `ScheduleExpression`: `str`
- `OutputLocation`: `"InstanceAssociationOutputLocationTypeDef"`
- `AssociationName`: `str`
- `MaxErrors`: `str`
- `MaxConcurrency`: `str`
- `ComplianceSeverity`: `AssociationComplianceSeverity`
- `SyncCompliance`: `AssociationSyncCompliance`
- `ApplyOnlyAtCronInterval`: `bool`
- `TargetLocations`: `List["TargetLocationTypeDef"]`


## AttachmentContentTypeDef

```python
from mypy_boto3_ssm.type_defs import AttachmentContentTypeDef
```




Optional fields:
- `Name`: `str`
- `Size`: `int`
- `Hash`: `str`
- `HashType`: `AttachmentHashType`
- `Url`: `str`


## AttachmentInformationTypeDef

```python
from mypy_boto3_ssm.type_defs import AttachmentInformationTypeDef
```




Optional fields:
- `Name`: `str`


## AutomationExecutionMetadataTypeDef

```python
from mypy_boto3_ssm.type_defs import AutomationExecutionMetadataTypeDef
```




Optional fields:
- `AutomationExecutionId`: `str`
- `DocumentName`: `str`
- `DocumentVersion`: `str`
- `AutomationExecutionStatus`: `AutomationExecutionStatus`
- `ExecutionStartTime`: `datetime`
- `ExecutionEndTime`: `datetime`
- `ExecutedBy`: `str`
- `LogFile`: `str`
- `Outputs`: `Dict[str, List[str]]`
- `Mode`: `ExecutionMode`
- `ParentAutomationExecutionId`: `str`
- `CurrentStepName`: `str`
- `CurrentAction`: `str`
- `FailureMessage`: `str`
- `TargetParameterName`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `TargetMaps`: `List[Dict[str, List[str]]]`
- `ResolvedTargets`: `"ResolvedTargetsTypeDef"`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `Target`: `str`
- `AutomationType`: `AutomationType`
- `AutomationSubtype`: `AutomationSubtype`
- `ScheduledTime`: `datetime`
- `Runbooks`: `List["RunbookTypeDef"]`
- `OpsItemId`: `str`
- `AssociationId`: `str`
- `ChangeRequestName`: `str`


## AutomationExecutionTypeDef

```python
from mypy_boto3_ssm.type_defs import AutomationExecutionTypeDef
```




Optional fields:
- `AutomationExecutionId`: `str`
- `DocumentName`: `str`
- `DocumentVersion`: `str`
- `ExecutionStartTime`: `datetime`
- `ExecutionEndTime`: `datetime`
- `AutomationExecutionStatus`: `AutomationExecutionStatus`
- `StepExecutions`: `List["StepExecutionTypeDef"]`
- `StepExecutionsTruncated`: `bool`
- `Parameters`: `Dict[str, List[str]]`
- `Outputs`: `Dict[str, List[str]]`
- `FailureMessage`: `str`
- `Mode`: `ExecutionMode`
- `ParentAutomationExecutionId`: `str`
- `ExecutedBy`: `str`
- `CurrentStepName`: `str`
- `CurrentAction`: `str`
- `TargetParameterName`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `TargetMaps`: `List[Dict[str, List[str]]]`
- `ResolvedTargets`: `"ResolvedTargetsTypeDef"`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `Target`: `str`
- `TargetLocations`: `List["TargetLocationTypeDef"]`
- `ProgressCounters`: `"ProgressCountersTypeDef"`
- `AutomationSubtype`: `AutomationSubtype`
- `ScheduledTime`: `datetime`
- `Runbooks`: `List["RunbookTypeDef"]`
- `OpsItemId`: `str`
- `AssociationId`: `str`
- `ChangeRequestName`: `str`


## CloudWatchOutputConfigTypeDef

```python
from mypy_boto3_ssm.type_defs import CloudWatchOutputConfigTypeDef
```




Optional fields:
- `CloudWatchLogGroupName`: `str`
- `CloudWatchOutputEnabled`: `bool`


## CommandInvocationTypeDef

```python
from mypy_boto3_ssm.type_defs import CommandInvocationTypeDef
```




Optional fields:
- `CommandId`: `str`
- `InstanceId`: `str`
- `InstanceName`: `str`
- `Comment`: `str`
- `DocumentName`: `str`
- `DocumentVersion`: `str`
- `RequestedDateTime`: `datetime`
- `Status`: `CommandInvocationStatus`
- `StatusDetails`: `str`
- `TraceOutput`: `str`
- `StandardOutputUrl`: `str`
- `StandardErrorUrl`: `str`
- `CommandPlugins`: `List["CommandPluginTypeDef"]`
- `ServiceRole`: `str`
- `NotificationConfig`: `"NotificationConfigTypeDef"`
- `CloudWatchOutputConfig`: `"CloudWatchOutputConfigTypeDef"`


## CommandPluginTypeDef

```python
from mypy_boto3_ssm.type_defs import CommandPluginTypeDef
```




Optional fields:
- `Name`: `str`
- `Status`: `CommandPluginStatus`
- `StatusDetails`: `str`
- `ResponseCode`: `int`
- `ResponseStartDateTime`: `datetime`
- `ResponseFinishDateTime`: `datetime`
- `Output`: `str`
- `StandardOutputUrl`: `str`
- `StandardErrorUrl`: `str`
- `OutputS3Region`: `str`
- `OutputS3BucketName`: `str`
- `OutputS3KeyPrefix`: `str`


## CommandTypeDef

```python
from mypy_boto3_ssm.type_defs import CommandTypeDef
```




Optional fields:
- `CommandId`: `str`
- `DocumentName`: `str`
- `DocumentVersion`: `str`
- `Comment`: `str`
- `ExpiresAfter`: `datetime`
- `Parameters`: `Dict[str, List[str]]`
- `InstanceIds`: `List[str]`
- `Targets`: `List["TargetTypeDef"]`
- `RequestedDateTime`: `datetime`
- `Status`: `CommandStatus`
- `StatusDetails`: `str`
- `OutputS3Region`: `str`
- `OutputS3BucketName`: `str`
- `OutputS3KeyPrefix`: `str`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `TargetCount`: `int`
- `CompletedCount`: `int`
- `ErrorCount`: `int`
- `DeliveryTimedOutCount`: `int`
- `ServiceRole`: `str`
- `NotificationConfig`: `"NotificationConfigTypeDef"`
- `CloudWatchOutputConfig`: `"CloudWatchOutputConfigTypeDef"`
- `TimeoutSeconds`: `int`


## ComplianceExecutionSummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import ComplianceExecutionSummaryTypeDef
```


Required fields:
- `ExecutionTime`: `datetime`



Optional fields:
- `ExecutionId`: `str`
- `ExecutionType`: `str`


## ComplianceItemTypeDef

```python
from mypy_boto3_ssm.type_defs import ComplianceItemTypeDef
```




Optional fields:
- `ComplianceType`: `str`
- `ResourceType`: `str`
- `ResourceId`: `str`
- `Id`: `str`
- `Title`: `str`
- `Status`: `ComplianceStatus`
- `Severity`: `ComplianceSeverity`
- `ExecutionSummary`: `"ComplianceExecutionSummaryTypeDef"`
- `Details`: `Dict[str, str]`


## ComplianceSummaryItemTypeDef

```python
from mypy_boto3_ssm.type_defs import ComplianceSummaryItemTypeDef
```




Optional fields:
- `ComplianceType`: `str`
- `CompliantSummary`: `"CompliantSummaryTypeDef"`
- `NonCompliantSummary`: `"NonCompliantSummaryTypeDef"`


## CompliantSummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import CompliantSummaryTypeDef
```




Optional fields:
- `CompliantCount`: `int`
- `SeveritySummary`: `"SeveritySummaryTypeDef"`


## CreateAssociationBatchRequestEntryTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateAssociationBatchRequestEntryTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `InstanceId`: `str`
- `Parameters`: `Dict[str, List[str]]`
- `AutomationTargetParameterName`: `str`
- `DocumentVersion`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `ScheduleExpression`: `str`
- `OutputLocation`: `"InstanceAssociationOutputLocationTypeDef"`
- `AssociationName`: `str`
- `MaxErrors`: `str`
- `MaxConcurrency`: `str`
- `ComplianceSeverity`: `AssociationComplianceSeverity`
- `SyncCompliance`: `AssociationSyncCompliance`
- `ApplyOnlyAtCronInterval`: `bool`
- `TargetLocations`: `List["TargetLocationTypeDef"]`


## DocumentDefaultVersionDescriptionTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentDefaultVersionDescriptionTypeDef
```




Optional fields:
- `Name`: `str`
- `DefaultVersion`: `str`
- `DefaultVersionName`: `str`


## DocumentDescriptionTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentDescriptionTypeDef
```




Optional fields:
- `Sha1`: `str`
- `Hash`: `str`
- `HashType`: `DocumentHashType`
- `Name`: `str`
- `VersionName`: `str`
- `Owner`: `str`
- `CreatedDate`: `datetime`
- `Status`: `DocumentStatus`
- `StatusInformation`: `str`
- `DocumentVersion`: `str`
- `Description`: `str`
- `Parameters`: `List["DocumentParameterTypeDef"]`
- `PlatformTypes`: `List[PlatformType]`
- `DocumentType`: `DocumentType`
- `SchemaVersion`: `str`
- `LatestVersion`: `str`
- `DefaultVersion`: `str`
- `DocumentFormat`: `DocumentFormat`
- `TargetType`: `str`
- `Tags`: `List["TagTypeDef"]`
- `AttachmentsInformation`: `List["AttachmentInformationTypeDef"]`
- `Requires`: `List["DocumentRequiresTypeDef"]`
- `Author`: `str`
- `ReviewInformation`: `List["ReviewInformationTypeDef"]`
- `ApprovedVersion`: `str`
- `PendingReviewVersion`: `str`
- `ReviewStatus`: `ReviewStatus`


## DocumentIdentifierTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentIdentifierTypeDef
```




Optional fields:
- `Name`: `str`
- `Owner`: `str`
- `VersionName`: `str`
- `PlatformTypes`: `List[PlatformType]`
- `DocumentVersion`: `str`
- `DocumentType`: `DocumentType`
- `SchemaVersion`: `str`
- `DocumentFormat`: `DocumentFormat`
- `TargetType`: `str`
- `Tags`: `List["TagTypeDef"]`
- `Requires`: `List["DocumentRequiresTypeDef"]`
- `ReviewStatus`: `ReviewStatus`
- `Author`: `str`


## DocumentMetadataResponseInfoTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentMetadataResponseInfoTypeDef
```




Optional fields:
- `ReviewerResponse`: `List["DocumentReviewerResponseSourceTypeDef"]`


## DocumentParameterTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentParameterTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `DocumentParameterType`
- `Description`: `str`
- `DefaultValue`: `str`


## DocumentRequiresTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentRequiresTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Version`: `str`


## DocumentReviewCommentSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentReviewCommentSourceTypeDef
```




Optional fields:
- `Type`: `DocumentReviewCommentType`
- `Content`: `str`


## DocumentReviewerResponseSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentReviewerResponseSourceTypeDef
```




Optional fields:
- `CreateTime`: `datetime`
- `UpdatedTime`: `datetime`
- `ReviewStatus`: `ReviewStatus`
- `Comment`: `List["DocumentReviewCommentSourceTypeDef"]`
- `Reviewer`: `str`


## DocumentVersionInfoTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentVersionInfoTypeDef
```




Optional fields:
- `Name`: `str`
- `DocumentVersion`: `str`
- `VersionName`: `str`
- `CreatedDate`: `datetime`
- `IsDefaultVersion`: `bool`
- `DocumentFormat`: `DocumentFormat`
- `Status`: `DocumentStatus`
- `StatusInformation`: `str`
- `ReviewStatus`: `ReviewStatus`


## EffectivePatchTypeDef

```python
from mypy_boto3_ssm.type_defs import EffectivePatchTypeDef
```




Optional fields:
- `Patch`: `"PatchTypeDef"`
- `PatchStatus`: `"PatchStatusTypeDef"`


## FailedCreateAssociationTypeDef

```python
from mypy_boto3_ssm.type_defs import FailedCreateAssociationTypeDef
```




Optional fields:
- `Entry`: `"CreateAssociationBatchRequestEntryTypeDef"`
- `Message`: `str`
- `Fault`: `Fault`


## FailureDetailsTypeDef

```python
from mypy_boto3_ssm.type_defs import FailureDetailsTypeDef
```




Optional fields:
- `FailureStage`: `str`
- `FailureType`: `str`
- `Details`: `Dict[str, List[str]]`


## InstanceAggregatedAssociationOverviewTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceAggregatedAssociationOverviewTypeDef
```




Optional fields:
- `DetailedStatus`: `str`
- `InstanceAssociationStatusAggregatedCount`: `Dict[str, int]`


## InstanceAssociationOutputLocationTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceAssociationOutputLocationTypeDef
```




Optional fields:
- `S3Location`: `"S3OutputLocationTypeDef"`


## InstanceAssociationOutputUrlTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceAssociationOutputUrlTypeDef
```




Optional fields:
- `S3OutputUrl`: `"S3OutputUrlTypeDef"`


## InstanceAssociationStatusInfoTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceAssociationStatusInfoTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Name`: `str`
- `DocumentVersion`: `str`
- `AssociationVersion`: `str`
- `InstanceId`: `str`
- `ExecutionDate`: `datetime`
- `Status`: `str`
- `DetailedStatus`: `str`
- `ExecutionSummary`: `str`
- `ErrorCode`: `str`
- `OutputUrl`: `"InstanceAssociationOutputUrlTypeDef"`
- `AssociationName`: `str`


## InstanceAssociationTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `InstanceId`: `str`
- `Content`: `str`
- `AssociationVersion`: `str`


## InstanceInformationTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceInformationTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `PingStatus`: `PingStatus`
- `LastPingDateTime`: `datetime`
- `AgentVersion`: `str`
- `IsLatestVersion`: `bool`
- `PlatformType`: `PlatformType`
- `PlatformName`: `str`
- `PlatformVersion`: `str`
- `ActivationId`: `str`
- `IamRole`: `str`
- `RegistrationDate`: `datetime`
- `ResourceType`: `ResourceType`
- `Name`: `str`
- `IPAddress`: `str`
- `ComputerName`: `str`
- `AssociationStatus`: `str`
- `LastAssociationExecutionDate`: `datetime`
- `LastSuccessfulAssociationExecutionDate`: `datetime`
- `AssociationOverview`: `"InstanceAggregatedAssociationOverviewTypeDef"`


## InstancePatchStateTypeDef

```python
from mypy_boto3_ssm.type_defs import InstancePatchStateTypeDef
```


Required fields:
- `InstanceId`: `str`
- `PatchGroup`: `str`
- `BaselineId`: `str`
- `OperationStartTime`: `datetime`
- `OperationEndTime`: `datetime`
- `Operation`: `PatchOperationType`



Optional fields:
- `SnapshotId`: `str`
- `InstallOverrideList`: `str`
- `OwnerInformation`: `str`
- `InstalledCount`: `int`
- `InstalledOtherCount`: `int`
- `InstalledPendingRebootCount`: `int`
- `InstalledRejectedCount`: `int`
- `MissingCount`: `int`
- `FailedCount`: `int`
- `UnreportedNotApplicableCount`: `int`
- `NotApplicableCount`: `int`
- `LastNoRebootInstallOperationTime`: `datetime`
- `RebootOption`: `RebootOption`
- `CriticalNonCompliantCount`: `int`
- `SecurityNonCompliantCount`: `int`
- `OtherNonCompliantCount`: `int`


## InventoryDeletionStatusItemTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryDeletionStatusItemTypeDef
```




Optional fields:
- `DeletionId`: `str`
- `TypeName`: `str`
- `DeletionStartTime`: `datetime`
- `LastStatus`: `InventoryDeletionStatus`
- `LastStatusMessage`: `str`
- `DeletionSummary`: `"InventoryDeletionSummaryTypeDef"`
- `LastStatusUpdateTime`: `datetime`


## InventoryDeletionSummaryItemTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryDeletionSummaryItemTypeDef
```




Optional fields:
- `Version`: `str`
- `Count`: `int`
- `RemainingCount`: `int`


## InventoryDeletionSummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryDeletionSummaryTypeDef
```




Optional fields:
- `TotalCount`: `int`
- `RemainingCount`: `int`
- `SummaryItems`: `List["InventoryDeletionSummaryItemTypeDef"]`


## InventoryFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryFilterTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`



Optional fields:
- `Type`: `InventoryQueryOperatorType`


## InventoryGroupTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryGroupTypeDef
```


Required fields:
- `Name`: `str`
- `Filters`: `List["InventoryFilterTypeDef"]`




## InventoryItemAttributeTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryItemAttributeTypeDef
```


Required fields:
- `Name`: `str`
- `DataType`: `InventoryAttributeDataType`




## InventoryItemSchemaTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryItemSchemaTypeDef
```


Required fields:
- `TypeName`: `str`
- `Attributes`: `List["InventoryItemAttributeTypeDef"]`



Optional fields:
- `Version`: `str`
- `DisplayName`: `str`


## InventoryResultEntityTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryResultEntityTypeDef
```




Optional fields:
- `Id`: `str`
- `Data`: `Dict[str, "InventoryResultItemTypeDef"]`


## InventoryResultItemTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryResultItemTypeDef
```


Required fields:
- `TypeName`: `str`
- `SchemaVersion`: `str`
- `Content`: `List[Dict[str, str]]`



Optional fields:
- `CaptureTime`: `str`
- `ContentHash`: `str`


## LoggingInfoTypeDef

```python
from mypy_boto3_ssm.type_defs import LoggingInfoTypeDef
```


Required fields:
- `S3BucketName`: `str`
- `S3Region`: `str`



Optional fields:
- `S3KeyPrefix`: `str`


## MaintenanceWindowAutomationParametersTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowAutomationParametersTypeDef
```




Optional fields:
- `DocumentVersion`: `str`
- `Parameters`: `Dict[str, List[str]]`


## MaintenanceWindowExecutionTaskIdentityTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowExecutionTaskIdentityTypeDef
```




Optional fields:
- `WindowExecutionId`: `str`
- `TaskExecutionId`: `str`
- `Status`: `MaintenanceWindowExecutionStatus`
- `StatusDetails`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `TaskArn`: `str`
- `TaskType`: `MaintenanceWindowTaskType`


## MaintenanceWindowExecutionTaskInvocationIdentityTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowExecutionTaskInvocationIdentityTypeDef
```




Optional fields:
- `WindowExecutionId`: `str`
- `TaskExecutionId`: `str`
- `InvocationId`: `str`
- `ExecutionId`: `str`
- `TaskType`: `MaintenanceWindowTaskType`
- `Parameters`: `str`
- `Status`: `MaintenanceWindowExecutionStatus`
- `StatusDetails`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `OwnerInformation`: `str`
- `WindowTargetId`: `str`


## MaintenanceWindowExecutionTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowExecutionTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowExecutionId`: `str`
- `Status`: `MaintenanceWindowExecutionStatus`
- `StatusDetails`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## MaintenanceWindowIdentityForTargetTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowIdentityForTargetTypeDef
```




Optional fields:
- `WindowId`: `str`
- `Name`: `str`


## MaintenanceWindowIdentityTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowIdentityTypeDef
```




Optional fields:
- `WindowId`: `str`
- `Name`: `str`
- `Description`: `str`
- `Enabled`: `bool`
- `Duration`: `int`
- `Cutoff`: `int`
- `Schedule`: `str`
- `ScheduleTimezone`: `str`
- `ScheduleOffset`: `int`
- `EndDate`: `str`
- `StartDate`: `str`
- `NextExecutionTime`: `str`


## MaintenanceWindowLambdaParametersTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowLambdaParametersTypeDef
```




Optional fields:
- `ClientContext`: `str`
- `Qualifier`: `str`
- `Payload`: `Union[bytes, IO[bytes]]`


## MaintenanceWindowRunCommandParametersTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowRunCommandParametersTypeDef
```




Optional fields:
- `Comment`: `str`
- `CloudWatchOutputConfig`: `"CloudWatchOutputConfigTypeDef"`
- `DocumentHash`: `str`
- `DocumentHashType`: `DocumentHashType`
- `DocumentVersion`: `str`
- `NotificationConfig`: `"NotificationConfigTypeDef"`
- `OutputS3BucketName`: `str`
- `OutputS3KeyPrefix`: `str`
- `Parameters`: `Dict[str, List[str]]`
- `ServiceRoleArn`: `str`
- `TimeoutSeconds`: `int`


## MaintenanceWindowStepFunctionsParametersTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowStepFunctionsParametersTypeDef
```




Optional fields:
- `Input`: `str`
- `Name`: `str`


## MaintenanceWindowTargetTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowTargetTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTargetId`: `str`
- `ResourceType`: `MaintenanceWindowResourceType`
- `Targets`: `List["TargetTypeDef"]`
- `OwnerInformation`: `str`
- `Name`: `str`
- `Description`: `str`


## MaintenanceWindowTaskInvocationParametersTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowTaskInvocationParametersTypeDef
```




Optional fields:
- `RunCommand`: `"MaintenanceWindowRunCommandParametersTypeDef"`
- `Automation`: `"MaintenanceWindowAutomationParametersTypeDef"`
- `StepFunctions`: `"MaintenanceWindowStepFunctionsParametersTypeDef"`
- `Lambda`: `"MaintenanceWindowLambdaParametersTypeDef"`


## MaintenanceWindowTaskParameterValueExpressionTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowTaskParameterValueExpressionTypeDef
```




Optional fields:
- `Values`: `List[str]`


## MaintenanceWindowTaskTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowTaskTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTaskId`: `str`
- `TaskArn`: `str`
- `Type`: `MaintenanceWindowTaskType`
- `Targets`: `List["TargetTypeDef"]`
- `TaskParameters`: `Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]`
- `Priority`: `int`
- `LoggingInfo`: `"LoggingInfoTypeDef"`
- `ServiceRoleArn`: `str`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `Name`: `str`
- `Description`: `str`


## MetadataValueTypeDef

```python
from mypy_boto3_ssm.type_defs import MetadataValueTypeDef
```




Optional fields:
- `Value`: `str`


## NonCompliantSummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import NonCompliantSummaryTypeDef
```




Optional fields:
- `NonCompliantCount`: `int`
- `SeveritySummary`: `"SeveritySummaryTypeDef"`


## NotificationConfigTypeDef

```python
from mypy_boto3_ssm.type_defs import NotificationConfigTypeDef
```




Optional fields:
- `NotificationArn`: `str`
- `NotificationEvents`: `List[NotificationEvent]`
- `NotificationType`: `NotificationType`


## OpsEntityItemTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsEntityItemTypeDef
```




Optional fields:
- `CaptureTime`: `str`
- `Content`: `List[Dict[str, str]]`


## OpsEntityTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsEntityTypeDef
```




Optional fields:
- `Id`: `str`
- `Data`: `Dict[str, "OpsEntityItemTypeDef"]`


## OpsFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsFilterTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`



Optional fields:
- `Type`: `OpsFilterOperatorType`


## OpsItemDataValueTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemDataValueTypeDef
```




Optional fields:
- `Value`: `str`
- `Type`: `OpsItemDataType`


## OpsItemEventSummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemEventSummaryTypeDef
```




Optional fields:
- `OpsItemId`: `str`
- `EventId`: `str`
- `Source`: `str`
- `DetailType`: `str`
- `Detail`: `str`
- `CreatedBy`: `"OpsItemIdentityTypeDef"`
- `CreatedTime`: `datetime`


## OpsItemIdentityTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemIdentityTypeDef
```




Optional fields:
- `Arn`: `str`


## OpsItemNotificationTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemNotificationTypeDef
```




Optional fields:
- `Arn`: `str`


## OpsItemSummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemSummaryTypeDef
```




Optional fields:
- `CreatedBy`: `str`
- `CreatedTime`: `datetime`
- `LastModifiedBy`: `str`
- `LastModifiedTime`: `datetime`
- `Priority`: `int`
- `Source`: `str`
- `Status`: `OpsItemStatus`
- `OpsItemId`: `str`
- `Title`: `str`
- `OperationalData`: `Dict[str, "OpsItemDataValueTypeDef"]`
- `Category`: `str`
- `Severity`: `str`
- `OpsItemType`: `str`
- `ActualStartTime`: `datetime`
- `ActualEndTime`: `datetime`
- `PlannedStartTime`: `datetime`
- `PlannedEndTime`: `datetime`


## OpsItemTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemTypeDef
```




Optional fields:
- `CreatedBy`: `str`
- `OpsItemType`: `str`
- `CreatedTime`: `datetime`
- `Description`: `str`
- `LastModifiedBy`: `str`
- `LastModifiedTime`: `datetime`
- `Notifications`: `List["OpsItemNotificationTypeDef"]`
- `Priority`: `int`
- `RelatedOpsItems`: `List["RelatedOpsItemTypeDef"]`
- `Status`: `OpsItemStatus`
- `OpsItemId`: `str`
- `Version`: `str`
- `Title`: `str`
- `Source`: `str`
- `OperationalData`: `Dict[str, "OpsItemDataValueTypeDef"]`
- `Category`: `str`
- `Severity`: `str`
- `ActualStartTime`: `datetime`
- `ActualEndTime`: `datetime`
- `PlannedStartTime`: `datetime`
- `PlannedEndTime`: `datetime`


## OpsMetadataTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsMetadataTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `OpsMetadataArn`: `str`
- `LastModifiedDate`: `datetime`
- `LastModifiedUser`: `str`
- `CreationDate`: `datetime`


## OutputSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import OutputSourceTypeDef
```




Optional fields:
- `OutputSourceId`: `str`
- `OutputSourceType`: `str`


## ParameterHistoryTypeDef

```python
from mypy_boto3_ssm.type_defs import ParameterHistoryTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `ParameterType`
- `KeyId`: `str`
- `LastModifiedDate`: `datetime`
- `LastModifiedUser`: `str`
- `Description`: `str`
- `Value`: `str`
- `AllowedPattern`: `str`
- `Version`: `int`
- `Labels`: `List[str]`
- `Tier`: `ParameterTier`
- `Policies`: `List["ParameterInlinePolicyTypeDef"]`
- `DataType`: `str`


## ParameterInlinePolicyTypeDef

```python
from mypy_boto3_ssm.type_defs import ParameterInlinePolicyTypeDef
```




Optional fields:
- `PolicyText`: `str`
- `PolicyType`: `str`
- `PolicyStatus`: `str`


## ParameterMetadataTypeDef

```python
from mypy_boto3_ssm.type_defs import ParameterMetadataTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `ParameterType`
- `KeyId`: `str`
- `LastModifiedDate`: `datetime`
- `LastModifiedUser`: `str`
- `Description`: `str`
- `AllowedPattern`: `str`
- `Version`: `int`
- `Tier`: `ParameterTier`
- `Policies`: `List["ParameterInlinePolicyTypeDef"]`
- `DataType`: `str`


## ParameterTypeDef

```python
from mypy_boto3_ssm.type_defs import ParameterTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `ParameterType`
- `Value`: `str`
- `Version`: `int`
- `Selector`: `str`
- `SourceResult`: `str`
- `LastModifiedDate`: `datetime`
- `ARN`: `str`
- `DataType`: `str`


## PatchBaselineIdentityTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchBaselineIdentityTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `BaselineName`: `str`
- `OperatingSystem`: `OperatingSystem`
- `BaselineDescription`: `str`
- `DefaultBaseline`: `bool`


## PatchComplianceDataTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchComplianceDataTypeDef
```


Required fields:
- `Title`: `str`
- `KBId`: `str`
- `Classification`: `str`
- `Severity`: `str`
- `State`: `PatchComplianceDataState`
- `InstalledTime`: `datetime`



Optional fields:
- `CVEIds`: `str`


## PatchFilterGroupTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchFilterGroupTypeDef
```


Required fields:
- `PatchFilters`: `List["PatchFilterTypeDef"]`




## PatchFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchFilterTypeDef
```


Required fields:
- `Key`: `PatchFilterKey`
- `Values`: `List[str]`




## PatchGroupPatchBaselineMappingTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchGroupPatchBaselineMappingTypeDef
```




Optional fields:
- `PatchGroup`: `str`
- `BaselineIdentity`: `"PatchBaselineIdentityTypeDef"`


## PatchRuleGroupTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchRuleGroupTypeDef
```


Required fields:
- `PatchRules`: `List["PatchRuleTypeDef"]`




## PatchRuleTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchRuleTypeDef
```


Required fields:
- `PatchFilterGroup`: `"PatchFilterGroupTypeDef"`



Optional fields:
- `ComplianceLevel`: `PatchComplianceLevel`
- `ApproveAfterDays`: `int`
- `ApproveUntilDate`: `str`
- `EnableNonSecurity`: `bool`


## PatchSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchSourceTypeDef
```


Required fields:
- `Name`: `str`
- `Products`: `List[str]`
- `Configuration`: `str`




## PatchStatusTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchStatusTypeDef
```




Optional fields:
- `DeploymentStatus`: `PatchDeploymentStatus`
- `ComplianceLevel`: `PatchComplianceLevel`
- `ApprovalDate`: `datetime`


## PatchTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchTypeDef
```




Optional fields:
- `Id`: `str`
- `ReleaseDate`: `datetime`
- `Title`: `str`
- `Description`: `str`
- `ContentUrl`: `str`
- `Vendor`: `str`
- `ProductFamily`: `str`
- `Product`: `str`
- `Classification`: `str`
- `MsrcSeverity`: `str`
- `KbNumber`: `str`
- `MsrcNumber`: `str`
- `Language`: `str`
- `AdvisoryIds`: `List[str]`
- `BugzillaIds`: `List[str]`
- `CVEIds`: `List[str]`
- `Name`: `str`
- `Epoch`: `int`
- `Version`: `str`
- `Release`: `str`
- `Arch`: `str`
- `Severity`: `str`
- `Repository`: `str`


## ProgressCountersTypeDef

```python
from mypy_boto3_ssm.type_defs import ProgressCountersTypeDef
```




Optional fields:
- `TotalSteps`: `int`
- `SuccessSteps`: `int`
- `FailedSteps`: `int`
- `CancelledSteps`: `int`
- `TimedOutSteps`: `int`


## RelatedOpsItemTypeDef

```python
from mypy_boto3_ssm.type_defs import RelatedOpsItemTypeDef
```


Required fields:
- `OpsItemId`: `str`




## ResolvedTargetsTypeDef

```python
from mypy_boto3_ssm.type_defs import ResolvedTargetsTypeDef
```




Optional fields:
- `ParameterValues`: `List[str]`
- `Truncated`: `bool`


## ResourceComplianceSummaryItemTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceComplianceSummaryItemTypeDef
```




Optional fields:
- `ComplianceType`: `str`
- `ResourceType`: `str`
- `ResourceId`: `str`
- `Status`: `ComplianceStatus`
- `OverallSeverity`: `ComplianceSeverity`
- `ExecutionSummary`: `"ComplianceExecutionSummaryTypeDef"`
- `CompliantSummary`: `"CompliantSummaryTypeDef"`
- `NonCompliantSummary`: `"NonCompliantSummaryTypeDef"`


## ResourceDataSyncAwsOrganizationsSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncAwsOrganizationsSourceTypeDef
```


Required fields:
- `OrganizationSourceType`: `str`



Optional fields:
- `OrganizationalUnits`: `List["ResourceDataSyncOrganizationalUnitTypeDef"]`


## ResourceDataSyncDestinationDataSharingTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncDestinationDataSharingTypeDef
```




Optional fields:
- `DestinationDataSharingType`: `str`


## ResourceDataSyncItemTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncItemTypeDef
```




Optional fields:
- `SyncName`: `str`
- `SyncType`: `str`
- `SyncSource`: `"ResourceDataSyncSourceWithStateTypeDef"`
- `S3Destination`: `"ResourceDataSyncS3DestinationTypeDef"`
- `LastSyncTime`: `datetime`
- `LastSuccessfulSyncTime`: `datetime`
- `SyncLastModifiedTime`: `datetime`
- `LastStatus`: `LastResourceDataSyncStatus`
- `SyncCreatedTime`: `datetime`
- `LastSyncStatusMessage`: `str`


## ResourceDataSyncOrganizationalUnitTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncOrganizationalUnitTypeDef
```




Optional fields:
- `OrganizationalUnitId`: `str`


## ResourceDataSyncS3DestinationTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncS3DestinationTypeDef
```


Required fields:
- `BucketName`: `str`
- `SyncFormat`: `ResourceDataSyncS3Format`
- `Region`: `str`



Optional fields:
- `Prefix`: `str`
- `AWSKMSKeyARN`: `str`
- `DestinationDataSharing`: `"ResourceDataSyncDestinationDataSharingTypeDef"`


## ResourceDataSyncSourceWithStateTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncSourceWithStateTypeDef
```




Optional fields:
- `SourceType`: `str`
- `AwsOrganizationsSource`: `"ResourceDataSyncAwsOrganizationsSourceTypeDef"`
- `SourceRegions`: `List[str]`
- `IncludeFutureRegions`: `bool`
- `State`: `str`
- `EnableAllOpsDataSources`: `bool`


## ReviewInformationTypeDef

```python
from mypy_boto3_ssm.type_defs import ReviewInformationTypeDef
```




Optional fields:
- `ReviewedTime`: `datetime`
- `Status`: `ReviewStatus`
- `Reviewer`: `str`


## RunbookTypeDef

```python
from mypy_boto3_ssm.type_defs import RunbookTypeDef
```


Required fields:
- `DocumentName`: `str`



Optional fields:
- `DocumentVersion`: `str`
- `Parameters`: `Dict[str, List[str]]`
- `TargetParameterName`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `TargetLocations`: `List["TargetLocationTypeDef"]`


## S3OutputLocationTypeDef

```python
from mypy_boto3_ssm.type_defs import S3OutputLocationTypeDef
```




Optional fields:
- `OutputS3Region`: `str`
- `OutputS3BucketName`: `str`
- `OutputS3KeyPrefix`: `str`


## S3OutputUrlTypeDef

```python
from mypy_boto3_ssm.type_defs import S3OutputUrlTypeDef
```




Optional fields:
- `OutputUrl`: `str`


## ScheduledWindowExecutionTypeDef

```python
from mypy_boto3_ssm.type_defs import ScheduledWindowExecutionTypeDef
```




Optional fields:
- `WindowId`: `str`
- `Name`: `str`
- `ExecutionTime`: `str`


## ServiceSettingTypeDef

```python
from mypy_boto3_ssm.type_defs import ServiceSettingTypeDef
```




Optional fields:
- `SettingId`: `str`
- `SettingValue`: `str`
- `LastModifiedDate`: `datetime`
- `LastModifiedUser`: `str`
- `ARN`: `str`
- `Status`: `str`


## SessionManagerOutputUrlTypeDef

```python
from mypy_boto3_ssm.type_defs import SessionManagerOutputUrlTypeDef
```




Optional fields:
- `S3OutputUrl`: `str`
- `CloudWatchOutputUrl`: `str`


## SessionTypeDef

```python
from mypy_boto3_ssm.type_defs import SessionTypeDef
```




Optional fields:
- `SessionId`: `str`
- `Target`: `str`
- `Status`: `SessionStatus`
- `StartDate`: `datetime`
- `EndDate`: `datetime`
- `DocumentName`: `str`
- `Owner`: `str`
- `Details`: `str`
- `OutputUrl`: `"SessionManagerOutputUrlTypeDef"`


## SeveritySummaryTypeDef

```python
from mypy_boto3_ssm.type_defs import SeveritySummaryTypeDef
```




Optional fields:
- `CriticalCount`: `int`
- `HighCount`: `int`
- `MediumCount`: `int`
- `LowCount`: `int`
- `InformationalCount`: `int`
- `UnspecifiedCount`: `int`


## StepExecutionTypeDef

```python
from mypy_boto3_ssm.type_defs import StepExecutionTypeDef
```




Optional fields:
- `StepName`: `str`
- `Action`: `str`
- `TimeoutSeconds`: `int`
- `OnFailure`: `str`
- `MaxAttempts`: `int`
- `ExecutionStartTime`: `datetime`
- `ExecutionEndTime`: `datetime`
- `StepStatus`: `AutomationExecutionStatus`
- `ResponseCode`: `str`
- `Inputs`: `Dict[str, str]`
- `Outputs`: `Dict[str, List[str]]`
- `Response`: `str`
- `FailureMessage`: `str`
- `FailureDetails`: `"FailureDetailsTypeDef"`
- `StepExecutionId`: `str`
- `OverriddenParameters`: `Dict[str, List[str]]`
- `IsEnd`: `bool`
- `NextStep`: `str`
- `IsCritical`: `bool`
- `ValidNextSteps`: `List[str]`
- `Targets`: `List["TargetTypeDef"]`
- `TargetLocation`: `"TargetLocationTypeDef"`


## TagTypeDef

```python
from mypy_boto3_ssm.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TargetLocationTypeDef

```python
from mypy_boto3_ssm.type_defs import TargetLocationTypeDef
```




Optional fields:
- `Accounts`: `List[str]`
- `Regions`: `List[str]`
- `TargetLocationMaxConcurrency`: `str`
- `TargetLocationMaxErrors`: `str`
- `ExecutionRoleName`: `str`


## TargetTypeDef

```python
from mypy_boto3_ssm.type_defs import TargetTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## AssociationExecutionFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationExecutionFilterTypeDef
```


Required fields:
- `Key`: `AssociationExecutionFilterKey`
- `Value`: `str`
- `Type`: `AssociationFilterOperatorType`




## AssociationExecutionTargetsFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationExecutionTargetsFilterTypeDef
```


Required fields:
- `Key`: `AssociationExecutionTargetsFilterKey`
- `Value`: `str`




## AssociationFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import AssociationFilterTypeDef
```


Required fields:
- `key`: `AssociationFilterKey`
- `value`: `str`




## AttachmentsSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import AttachmentsSourceTypeDef
```




Optional fields:
- `Key`: `AttachmentsSourceKey`
- `Values`: `List[str]`
- `Name`: `str`


## AutomationExecutionFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import AutomationExecutionFilterTypeDef
```


Required fields:
- `Key`: `AutomationExecutionFilterKey`
- `Values`: `List[str]`




## BaselineOverrideTypeDef

```python
from mypy_boto3_ssm.type_defs import BaselineOverrideTypeDef
```




Optional fields:
- `OperatingSystem`: `OperatingSystem`
- `GlobalFilters`: `"PatchFilterGroupTypeDef"`
- `ApprovalRules`: `"PatchRuleGroupTypeDef"`
- `ApprovedPatches`: `List[str]`
- `ApprovedPatchesComplianceLevel`: `PatchComplianceLevel`
- `RejectedPatches`: `List[str]`
- `RejectedPatchesAction`: `PatchAction`
- `ApprovedPatchesEnableNonSecurity`: `bool`
- `Sources`: `List["PatchSourceTypeDef"]`


## CancelMaintenanceWindowExecutionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CancelMaintenanceWindowExecutionResultTypeDef
```




Optional fields:
- `WindowExecutionId`: `str`


## CommandFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import CommandFilterTypeDef
```


Required fields:
- `key`: `CommandFilterKey`
- `value`: `str`




## ComplianceItemEntryTypeDef

```python
from mypy_boto3_ssm.type_defs import ComplianceItemEntryTypeDef
```


Required fields:
- `Severity`: `ComplianceSeverity`
- `Status`: `ComplianceStatus`



Optional fields:
- `Id`: `str`
- `Title`: `str`
- `Details`: `Dict[str, str]`


## ComplianceStringFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import ComplianceStringFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`
- `Type`: `ComplianceQueryOperatorType`


## CreateActivationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateActivationResultTypeDef
```




Optional fields:
- `ActivationId`: `str`
- `ActivationCode`: `str`


## CreateAssociationBatchResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateAssociationBatchResultTypeDef
```




Optional fields:
- `Successful`: `List["AssociationDescriptionTypeDef"]`
- `Failed`: `List["FailedCreateAssociationTypeDef"]`


## CreateAssociationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateAssociationResultTypeDef
```




Optional fields:
- `AssociationDescription`: `"AssociationDescriptionTypeDef"`


## CreateDocumentResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateDocumentResultTypeDef
```




Optional fields:
- `DocumentDescription`: `"DocumentDescriptionTypeDef"`


## CreateMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowId`: `str`


## CreateOpsItemResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateOpsItemResponseTypeDef
```




Optional fields:
- `OpsItemId`: `str`


## CreateOpsMetadataResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreateOpsMetadataResultTypeDef
```




Optional fields:
- `OpsMetadataArn`: `str`


## CreatePatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import CreatePatchBaselineResultTypeDef
```




Optional fields:
- `BaselineId`: `str`


## DeleteInventoryResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeleteInventoryResultTypeDef
```




Optional fields:
- `DeletionId`: `str`
- `TypeName`: `str`
- `DeletionSummary`: `"InventoryDeletionSummaryTypeDef"`


## DeleteMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeleteMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowId`: `str`


## DeleteParametersResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeleteParametersResultTypeDef
```




Optional fields:
- `DeletedParameters`: `List[str]`
- `InvalidParameters`: `List[str]`


## DeletePatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeletePatchBaselineResultTypeDef
```




Optional fields:
- `BaselineId`: `str`


## DeregisterPatchBaselineForPatchGroupResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeregisterPatchBaselineForPatchGroupResultTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `PatchGroup`: `str`


## DeregisterTargetFromMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeregisterTargetFromMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTargetId`: `str`


## DeregisterTaskFromMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DeregisterTaskFromMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTaskId`: `str`


## DescribeActivationsFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeActivationsFilterTypeDef
```




Optional fields:
- `FilterKey`: `DescribeActivationsFilterKeys`
- `FilterValues`: `List[str]`


## DescribeActivationsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeActivationsResultTypeDef
```




Optional fields:
- `ActivationList`: `List["ActivationTypeDef"]`
- `NextToken`: `str`


## DescribeAssociationExecutionTargetsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeAssociationExecutionTargetsResultTypeDef
```




Optional fields:
- `AssociationExecutionTargets`: `List["AssociationExecutionTargetTypeDef"]`
- `NextToken`: `str`


## DescribeAssociationExecutionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeAssociationExecutionsResultTypeDef
```




Optional fields:
- `AssociationExecutions`: `List["AssociationExecutionTypeDef"]`
- `NextToken`: `str`


## DescribeAssociationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeAssociationResultTypeDef
```




Optional fields:
- `AssociationDescription`: `"AssociationDescriptionTypeDef"`


## DescribeAutomationExecutionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeAutomationExecutionsResultTypeDef
```




Optional fields:
- `AutomationExecutionMetadataList`: `List["AutomationExecutionMetadataTypeDef"]`
- `NextToken`: `str`


## DescribeAutomationStepExecutionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeAutomationStepExecutionsResultTypeDef
```




Optional fields:
- `StepExecutions`: `List["StepExecutionTypeDef"]`
- `NextToken`: `str`


## DescribeAvailablePatchesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeAvailablePatchesResultTypeDef
```




Optional fields:
- `Patches`: `List["PatchTypeDef"]`
- `NextToken`: `str`


## DescribeDocumentPermissionResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeDocumentPermissionResponseTypeDef
```




Optional fields:
- `AccountIds`: `List[str]`
- `AccountSharingInfoList`: `List["AccountSharingInfoTypeDef"]`
- `NextToken`: `str`


## DescribeDocumentResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeDocumentResultTypeDef
```




Optional fields:
- `Document`: `"DocumentDescriptionTypeDef"`


## DescribeEffectiveInstanceAssociationsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeEffectiveInstanceAssociationsResultTypeDef
```




Optional fields:
- `Associations`: `List["InstanceAssociationTypeDef"]`
- `NextToken`: `str`


## DescribeEffectivePatchesForPatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeEffectivePatchesForPatchBaselineResultTypeDef
```




Optional fields:
- `EffectivePatches`: `List["EffectivePatchTypeDef"]`
- `NextToken`: `str`


## DescribeInstanceAssociationsStatusResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeInstanceAssociationsStatusResultTypeDef
```




Optional fields:
- `InstanceAssociationStatusInfos`: `List["InstanceAssociationStatusInfoTypeDef"]`
- `NextToken`: `str`


## DescribeInstanceInformationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeInstanceInformationResultTypeDef
```




Optional fields:
- `InstanceInformationList`: `List["InstanceInformationTypeDef"]`
- `NextToken`: `str`


## DescribeInstancePatchStatesForPatchGroupResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeInstancePatchStatesForPatchGroupResultTypeDef
```




Optional fields:
- `InstancePatchStates`: `List["InstancePatchStateTypeDef"]`
- `NextToken`: `str`


## DescribeInstancePatchStatesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeInstancePatchStatesResultTypeDef
```




Optional fields:
- `InstancePatchStates`: `List["InstancePatchStateTypeDef"]`
- `NextToken`: `str`


## DescribeInstancePatchesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeInstancePatchesResultTypeDef
```




Optional fields:
- `Patches`: `List["PatchComplianceDataTypeDef"]`
- `NextToken`: `str`


## DescribeInventoryDeletionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeInventoryDeletionsResultTypeDef
```




Optional fields:
- `InventoryDeletions`: `List["InventoryDeletionStatusItemTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef
```




Optional fields:
- `WindowExecutionTaskInvocationIdentities`: `List["MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowExecutionTasksResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowExecutionTasksResultTypeDef
```




Optional fields:
- `WindowExecutionTaskIdentities`: `List["MaintenanceWindowExecutionTaskIdentityTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowExecutionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowExecutionsResultTypeDef
```




Optional fields:
- `WindowExecutions`: `List["MaintenanceWindowExecutionTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowScheduleResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowScheduleResultTypeDef
```




Optional fields:
- `ScheduledWindowExecutions`: `List["ScheduledWindowExecutionTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowTargetsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowTargetsResultTypeDef
```




Optional fields:
- `Targets`: `List["MaintenanceWindowTargetTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowTasksResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowTasksResultTypeDef
```




Optional fields:
- `Tasks`: `List["MaintenanceWindowTaskTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowsForTargetResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowsForTargetResultTypeDef
```




Optional fields:
- `WindowIdentities`: `List["MaintenanceWindowIdentityForTargetTypeDef"]`
- `NextToken`: `str`


## DescribeMaintenanceWindowsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeMaintenanceWindowsResultTypeDef
```




Optional fields:
- `WindowIdentities`: `List["MaintenanceWindowIdentityTypeDef"]`
- `NextToken`: `str`


## DescribeOpsItemsResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeOpsItemsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `OpsItemSummaries`: `List["OpsItemSummaryTypeDef"]`


## DescribeParametersResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeParametersResultTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterMetadataTypeDef"]`
- `NextToken`: `str`


## DescribePatchBaselinesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribePatchBaselinesResultTypeDef
```




Optional fields:
- `BaselineIdentities`: `List["PatchBaselineIdentityTypeDef"]`
- `NextToken`: `str`


## DescribePatchGroupStateResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribePatchGroupStateResultTypeDef
```




Optional fields:
- `Instances`: `int`
- `InstancesWithInstalledPatches`: `int`
- `InstancesWithInstalledOtherPatches`: `int`
- `InstancesWithInstalledPendingRebootPatches`: `int`
- `InstancesWithInstalledRejectedPatches`: `int`
- `InstancesWithMissingPatches`: `int`
- `InstancesWithFailedPatches`: `int`
- `InstancesWithNotApplicablePatches`: `int`
- `InstancesWithUnreportedNotApplicablePatches`: `int`
- `InstancesWithCriticalNonCompliantPatches`: `int`
- `InstancesWithSecurityNonCompliantPatches`: `int`
- `InstancesWithOtherNonCompliantPatches`: `int`


## DescribePatchGroupsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribePatchGroupsResultTypeDef
```




Optional fields:
- `Mappings`: `List["PatchGroupPatchBaselineMappingTypeDef"]`
- `NextToken`: `str`


## DescribePatchPropertiesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribePatchPropertiesResultTypeDef
```




Optional fields:
- `Properties`: `List[Dict[str, str]]`
- `NextToken`: `str`


## DescribeSessionsResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import DescribeSessionsResponseTypeDef
```




Optional fields:
- `Sessions`: `List["SessionTypeDef"]`
- `NextToken`: `str`


## OpsAggregatorTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsAggregatorTypeDef
```




Optional fields:
- `AggregatorType`: `str`
- `TypeName`: `str`
- `AttributeName`: `str`
- `Values`: `Dict[str, str]`
- `Filters`: `List["OpsFilterTypeDef"]`
- `Aggregators`: `List[Dict[str, Any]]`


## InventoryAggregatorTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryAggregatorTypeDef
```




Optional fields:
- `Expression`: `str`
- `Aggregators`: `List[Dict[str, Any]]`
- `Groups`: `List["InventoryGroupTypeDef"]`


## DocumentFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentFilterTypeDef
```


Required fields:
- `key`: `DocumentFilterKey`
- `value`: `str`




## DocumentKeyValuesFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentKeyValuesFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## DocumentReviewsTypeDef

```python
from mypy_boto3_ssm.type_defs import DocumentReviewsTypeDef
```


Required fields:
- `Action`: `DocumentReviewAction`



Optional fields:
- `Comment`: `List["DocumentReviewCommentSourceTypeDef"]`


## GetAutomationExecutionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetAutomationExecutionResultTypeDef
```




Optional fields:
- `AutomationExecution`: `"AutomationExecutionTypeDef"`


## GetCalendarStateResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import GetCalendarStateResponseTypeDef
```




Optional fields:
- `State`: `CalendarState`
- `AtTime`: `str`
- `NextTransitionTime`: `str`


## GetCommandInvocationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetCommandInvocationResultTypeDef
```




Optional fields:
- `CommandId`: `str`
- `InstanceId`: `str`
- `Comment`: `str`
- `DocumentName`: `str`
- `DocumentVersion`: `str`
- `PluginName`: `str`
- `ResponseCode`: `int`
- `ExecutionStartDateTime`: `str`
- `ExecutionElapsedTime`: `str`
- `ExecutionEndDateTime`: `str`
- `Status`: `CommandInvocationStatus`
- `StatusDetails`: `str`
- `StandardOutputContent`: `str`
- `StandardOutputUrl`: `str`
- `StandardErrorContent`: `str`
- `StandardErrorUrl`: `str`
- `CloudWatchOutputConfig`: `"CloudWatchOutputConfigTypeDef"`


## GetConnectionStatusResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import GetConnectionStatusResponseTypeDef
```




Optional fields:
- `Target`: `str`
- `Status`: `ConnectionStatus`


## GetDefaultPatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetDefaultPatchBaselineResultTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `OperatingSystem`: `OperatingSystem`


## GetDeployablePatchSnapshotForInstanceResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetDeployablePatchSnapshotForInstanceResultTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `SnapshotId`: `str`
- `SnapshotDownloadUrl`: `str`
- `Product`: `str`


## GetDocumentResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetDocumentResultTypeDef
```




Optional fields:
- `Name`: `str`
- `VersionName`: `str`
- `DocumentVersion`: `str`
- `Status`: `DocumentStatus`
- `StatusInformation`: `str`
- `Content`: `str`
- `DocumentType`: `DocumentType`
- `DocumentFormat`: `DocumentFormat`
- `Requires`: `List["DocumentRequiresTypeDef"]`
- `AttachmentsContent`: `List["AttachmentContentTypeDef"]`
- `ReviewStatus`: `ReviewStatus`


## GetInventoryResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetInventoryResultTypeDef
```




Optional fields:
- `Entities`: `List["InventoryResultEntityTypeDef"]`
- `NextToken`: `str`


## GetInventorySchemaResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetInventorySchemaResultTypeDef
```




Optional fields:
- `Schemas`: `List["InventoryItemSchemaTypeDef"]`
- `NextToken`: `str`


## GetMaintenanceWindowExecutionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetMaintenanceWindowExecutionResultTypeDef
```




Optional fields:
- `WindowExecutionId`: `str`
- `TaskIds`: `List[str]`
- `Status`: `MaintenanceWindowExecutionStatus`
- `StatusDetails`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## GetMaintenanceWindowExecutionTaskInvocationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetMaintenanceWindowExecutionTaskInvocationResultTypeDef
```




Optional fields:
- `WindowExecutionId`: `str`
- `TaskExecutionId`: `str`
- `InvocationId`: `str`
- `ExecutionId`: `str`
- `TaskType`: `MaintenanceWindowTaskType`
- `Parameters`: `str`
- `Status`: `MaintenanceWindowExecutionStatus`
- `StatusDetails`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `OwnerInformation`: `str`
- `WindowTargetId`: `str`


## GetMaintenanceWindowExecutionTaskResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetMaintenanceWindowExecutionTaskResultTypeDef
```




Optional fields:
- `WindowExecutionId`: `str`
- `TaskExecutionId`: `str`
- `TaskArn`: `str`
- `ServiceRole`: `str`
- `Type`: `MaintenanceWindowTaskType`
- `TaskParameters`: `List[Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]]`
- `Priority`: `int`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `Status`: `MaintenanceWindowExecutionStatus`
- `StatusDetails`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## GetMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `Name`: `str`
- `Description`: `str`
- `StartDate`: `str`
- `EndDate`: `str`
- `Schedule`: `str`
- `ScheduleTimezone`: `str`
- `ScheduleOffset`: `int`
- `NextExecutionTime`: `str`
- `Duration`: `int`
- `Cutoff`: `int`
- `AllowUnassociatedTargets`: `bool`
- `Enabled`: `bool`
- `CreatedDate`: `datetime`
- `ModifiedDate`: `datetime`


## GetMaintenanceWindowTaskResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetMaintenanceWindowTaskResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTaskId`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `TaskArn`: `str`
- `ServiceRoleArn`: `str`
- `TaskType`: `MaintenanceWindowTaskType`
- `TaskParameters`: `Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]`
- `TaskInvocationParameters`: `"MaintenanceWindowTaskInvocationParametersTypeDef"`
- `Priority`: `int`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `LoggingInfo`: `"LoggingInfoTypeDef"`
- `Name`: `str`
- `Description`: `str`


## GetOpsItemResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import GetOpsItemResponseTypeDef
```




Optional fields:
- `OpsItem`: `"OpsItemTypeDef"`


## GetOpsMetadataResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetOpsMetadataResultTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `Metadata`: `Dict[str, "MetadataValueTypeDef"]`
- `NextToken`: `str`


## GetOpsSummaryResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetOpsSummaryResultTypeDef
```




Optional fields:
- `Entities`: `List["OpsEntityTypeDef"]`
- `NextToken`: `str`


## GetParameterHistoryResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetParameterHistoryResultTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterHistoryTypeDef"]`
- `NextToken`: `str`


## GetParameterResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetParameterResultTypeDef
```




Optional fields:
- `Parameter`: `"ParameterTypeDef"`


## GetParametersByPathResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetParametersByPathResultTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `NextToken`: `str`


## GetParametersResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetParametersResultTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `InvalidParameters`: `List[str]`


## GetPatchBaselineForPatchGroupResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetPatchBaselineForPatchGroupResultTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `PatchGroup`: `str`
- `OperatingSystem`: `OperatingSystem`


## GetPatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetPatchBaselineResultTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `Name`: `str`
- `OperatingSystem`: `OperatingSystem`
- `GlobalFilters`: `"PatchFilterGroupTypeDef"`
- `ApprovalRules`: `"PatchRuleGroupTypeDef"`
- `ApprovedPatches`: `List[str]`
- `ApprovedPatchesComplianceLevel`: `PatchComplianceLevel`
- `ApprovedPatchesEnableNonSecurity`: `bool`
- `RejectedPatches`: `List[str]`
- `RejectedPatchesAction`: `PatchAction`
- `PatchGroups`: `List[str]`
- `CreatedDate`: `datetime`
- `ModifiedDate`: `datetime`
- `Description`: `str`
- `Sources`: `List["PatchSourceTypeDef"]`


## GetServiceSettingResultTypeDef

```python
from mypy_boto3_ssm.type_defs import GetServiceSettingResultTypeDef
```




Optional fields:
- `ServiceSetting`: `"ServiceSettingTypeDef"`


## InstanceInformationFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceInformationFilterTypeDef
```


Required fields:
- `key`: `InstanceInformationFilterKey`
- `valueSet`: `List[str]`




## InstanceInformationStringFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import InstanceInformationStringFilterTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`




## InstancePatchStateFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import InstancePatchStateFilterTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`
- `Type`: `InstancePatchStateOperatorType`




## InventoryItemTypeDef

```python
from mypy_boto3_ssm.type_defs import InventoryItemTypeDef
```


Required fields:
- `TypeName`: `str`
- `SchemaVersion`: `str`
- `CaptureTime`: `str`



Optional fields:
- `ContentHash`: `str`
- `Content`: `List[Dict[str, str]]`
- `Context`: `Dict[str, str]`


## LabelParameterVersionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import LabelParameterVersionResultTypeDef
```




Optional fields:
- `InvalidLabels`: `List[str]`
- `ParameterVersion`: `int`


## ListAssociationVersionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListAssociationVersionsResultTypeDef
```




Optional fields:
- `AssociationVersions`: `List["AssociationVersionInfoTypeDef"]`
- `NextToken`: `str`


## ListAssociationsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListAssociationsResultTypeDef
```




Optional fields:
- `Associations`: `List["AssociationTypeDef"]`
- `NextToken`: `str`


## ListCommandInvocationsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListCommandInvocationsResultTypeDef
```




Optional fields:
- `CommandInvocations`: `List["CommandInvocationTypeDef"]`
- `NextToken`: `str`


## ListCommandsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListCommandsResultTypeDef
```




Optional fields:
- `Commands`: `List["CommandTypeDef"]`
- `NextToken`: `str`


## ListComplianceItemsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListComplianceItemsResultTypeDef
```




Optional fields:
- `ComplianceItems`: `List["ComplianceItemTypeDef"]`
- `NextToken`: `str`


## ListComplianceSummariesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListComplianceSummariesResultTypeDef
```




Optional fields:
- `ComplianceSummaryItems`: `List["ComplianceSummaryItemTypeDef"]`
- `NextToken`: `str`


## ListDocumentMetadataHistoryResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import ListDocumentMetadataHistoryResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `DocumentVersion`: `str`
- `Author`: `str`
- `Metadata`: `"DocumentMetadataResponseInfoTypeDef"`
- `NextToken`: `str`


## ListDocumentVersionsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListDocumentVersionsResultTypeDef
```




Optional fields:
- `DocumentVersions`: `List["DocumentVersionInfoTypeDef"]`
- `NextToken`: `str`


## ListDocumentsResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListDocumentsResultTypeDef
```




Optional fields:
- `DocumentIdentifiers`: `List["DocumentIdentifierTypeDef"]`
- `NextToken`: `str`


## ListInventoryEntriesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListInventoryEntriesResultTypeDef
```




Optional fields:
- `TypeName`: `str`
- `InstanceId`: `str`
- `SchemaVersion`: `str`
- `CaptureTime`: `str`
- `Entries`: `List[Dict[str, str]]`
- `NextToken`: `str`


## ListOpsItemEventsResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import ListOpsItemEventsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Summaries`: `List["OpsItemEventSummaryTypeDef"]`


## ListOpsMetadataResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListOpsMetadataResultTypeDef
```




Optional fields:
- `OpsMetadataList`: `List["OpsMetadataTypeDef"]`
- `NextToken`: `str`


## ListResourceComplianceSummariesResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListResourceComplianceSummariesResultTypeDef
```




Optional fields:
- `ResourceComplianceSummaryItems`: `List["ResourceComplianceSummaryItemTypeDef"]`
- `NextToken`: `str`


## ListResourceDataSyncResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListResourceDataSyncResultTypeDef
```




Optional fields:
- `ResourceDataSyncItems`: `List["ResourceDataSyncItemTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ListTagsForResourceResultTypeDef
```




Optional fields:
- `TagList`: `List["TagTypeDef"]`


## MaintenanceWindowFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import MaintenanceWindowFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## OpsItemEventFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemEventFilterTypeDef
```


Required fields:
- `Key`: `OpsItemEventFilterKey`
- `Values`: `List[str]`
- `Operator`: `OpsItemEventFilterOperator`




## OpsItemFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsItemFilterTypeDef
```


Required fields:
- `Key`: `OpsItemFilterKey`
- `Values`: `List[str]`
- `Operator`: `OpsItemFilterOperator`




## OpsMetadataFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsMetadataFilterTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`




## OpsResultAttributeTypeDef

```python
from mypy_boto3_ssm.type_defs import OpsResultAttributeTypeDef
```


Required fields:
- `TypeName`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_ssm.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParameterStringFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import ParameterStringFilterTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Option`: `str`
- `Values`: `List[str]`


## ParametersFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import ParametersFilterTypeDef
```


Required fields:
- `Key`: `ParametersFilterKey`
- `Values`: `List[str]`




## PatchOrchestratorFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import PatchOrchestratorFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## PutInventoryResultTypeDef

```python
from mypy_boto3_ssm.type_defs import PutInventoryResultTypeDef
```




Optional fields:
- `Message`: `str`


## PutParameterResultTypeDef

```python
from mypy_boto3_ssm.type_defs import PutParameterResultTypeDef
```




Optional fields:
- `Version`: `int`
- `Tier`: `ParameterTier`


## RegisterDefaultPatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import RegisterDefaultPatchBaselineResultTypeDef
```




Optional fields:
- `BaselineId`: `str`


## RegisterPatchBaselineForPatchGroupResultTypeDef

```python
from mypy_boto3_ssm.type_defs import RegisterPatchBaselineForPatchGroupResultTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `PatchGroup`: `str`


## RegisterTargetWithMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import RegisterTargetWithMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowTargetId`: `str`


## RegisterTaskWithMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import RegisterTaskWithMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowTaskId`: `str`


## ResetServiceSettingResultTypeDef

```python
from mypy_boto3_ssm.type_defs import ResetServiceSettingResultTypeDef
```




Optional fields:
- `ServiceSetting`: `"ServiceSettingTypeDef"`


## ResourceDataSyncSourceTypeDef

```python
from mypy_boto3_ssm.type_defs import ResourceDataSyncSourceTypeDef
```


Required fields:
- `SourceType`: `str`
- `SourceRegions`: `List[str]`



Optional fields:
- `AwsOrganizationsSource`: `"ResourceDataSyncAwsOrganizationsSourceTypeDef"`
- `IncludeFutureRegions`: `bool`
- `EnableAllOpsDataSources`: `bool`


## ResultAttributeTypeDef

```python
from mypy_boto3_ssm.type_defs import ResultAttributeTypeDef
```


Required fields:
- `TypeName`: `str`




## ResumeSessionResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import ResumeSessionResponseTypeDef
```




Optional fields:
- `SessionId`: `str`
- `TokenValue`: `str`
- `StreamUrl`: `str`


## SendCommandResultTypeDef

```python
from mypy_boto3_ssm.type_defs import SendCommandResultTypeDef
```




Optional fields:
- `Command`: `"CommandTypeDef"`


## SessionFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import SessionFilterTypeDef
```


Required fields:
- `key`: `SessionFilterKey`
- `value`: `str`




## StartAutomationExecutionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import StartAutomationExecutionResultTypeDef
```




Optional fields:
- `AutomationExecutionId`: `str`


## StartChangeRequestExecutionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import StartChangeRequestExecutionResultTypeDef
```




Optional fields:
- `AutomationExecutionId`: `str`


## StartSessionResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import StartSessionResponseTypeDef
```




Optional fields:
- `SessionId`: `str`
- `TokenValue`: `str`
- `StreamUrl`: `str`


## StepExecutionFilterTypeDef

```python
from mypy_boto3_ssm.type_defs import StepExecutionFilterTypeDef
```


Required fields:
- `Key`: `StepExecutionFilterKey`
- `Values`: `List[str]`




## TerminateSessionResponseTypeDef

```python
from mypy_boto3_ssm.type_defs import TerminateSessionResponseTypeDef
```




Optional fields:
- `SessionId`: `str`


## UnlabelParameterVersionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UnlabelParameterVersionResultTypeDef
```




Optional fields:
- `RemovedLabels`: `List[str]`
- `InvalidLabels`: `List[str]`


## UpdateAssociationResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateAssociationResultTypeDef
```




Optional fields:
- `AssociationDescription`: `"AssociationDescriptionTypeDef"`


## UpdateAssociationStatusResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateAssociationStatusResultTypeDef
```




Optional fields:
- `AssociationDescription`: `"AssociationDescriptionTypeDef"`


## UpdateDocumentDefaultVersionResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateDocumentDefaultVersionResultTypeDef
```




Optional fields:
- `Description`: `"DocumentDefaultVersionDescriptionTypeDef"`


## UpdateDocumentResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateDocumentResultTypeDef
```




Optional fields:
- `DocumentDescription`: `"DocumentDescriptionTypeDef"`


## UpdateMaintenanceWindowResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateMaintenanceWindowResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `Name`: `str`
- `Description`: `str`
- `StartDate`: `str`
- `EndDate`: `str`
- `Schedule`: `str`
- `ScheduleTimezone`: `str`
- `ScheduleOffset`: `int`
- `Duration`: `int`
- `Cutoff`: `int`
- `AllowUnassociatedTargets`: `bool`
- `Enabled`: `bool`


## UpdateMaintenanceWindowTargetResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateMaintenanceWindowTargetResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTargetId`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `OwnerInformation`: `str`
- `Name`: `str`
- `Description`: `str`


## UpdateMaintenanceWindowTaskResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateMaintenanceWindowTaskResultTypeDef
```




Optional fields:
- `WindowId`: `str`
- `WindowTaskId`: `str`
- `Targets`: `List["TargetTypeDef"]`
- `TaskArn`: `str`
- `ServiceRoleArn`: `str`
- `TaskParameters`: `Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]`
- `TaskInvocationParameters`: `"MaintenanceWindowTaskInvocationParametersTypeDef"`
- `Priority`: `int`
- `MaxConcurrency`: `str`
- `MaxErrors`: `str`
- `LoggingInfo`: `"LoggingInfoTypeDef"`
- `Name`: `str`
- `Description`: `str`


## UpdateOpsMetadataResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdateOpsMetadataResultTypeDef
```




Optional fields:
- `OpsMetadataArn`: `str`


## UpdatePatchBaselineResultTypeDef

```python
from mypy_boto3_ssm.type_defs import UpdatePatchBaselineResultTypeDef
```




Optional fields:
- `BaselineId`: `str`
- `Name`: `str`
- `OperatingSystem`: `OperatingSystem`
- `GlobalFilters`: `"PatchFilterGroupTypeDef"`
- `ApprovalRules`: `"PatchRuleGroupTypeDef"`
- `ApprovedPatches`: `List[str]`
- `ApprovedPatchesComplianceLevel`: `PatchComplianceLevel`
- `ApprovedPatchesEnableNonSecurity`: `bool`
- `RejectedPatches`: `List[str]`
- `RejectedPatchesAction`: `PatchAction`
- `CreatedDate`: `datetime`
- `ModifiedDate`: `datetime`
- `Description`: `str`
- `Sources`: `List["PatchSourceTypeDef"]`


## WaiterConfigTypeDef

```python
from mypy_boto3_ssm.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

