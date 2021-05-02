# Structures for boto3 CloudFormation module

> [Index](../index.md) > [CloudFormation](./index.md) > Structures

Auto-generated documentation for [CloudFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
type annotations stubs module [mypy_boto3_cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/).

- [Structures for boto3 CloudFormation module](#structures-for-boto3-cloudformation-module)
  - [AccountGateResultTypeDef](#accountgateresulttypedef)
  - [AccountLimitTypeDef](#accountlimittypedef)
  - [AutoDeploymentTypeDef](#autodeploymenttypedef)
  - [ChangeSetSummaryTypeDef](#changesetsummarytypedef)
  - [ChangeTypeDef](#changetypedef)
  - [DeploymentTargetsTypeDef](#deploymenttargetstypedef)
  - [ExportTypeDef](#exporttypedef)
  - [LoggingConfigTypeDef](#loggingconfigtypedef)
  - [ModuleInfoTypeDef](#moduleinfotypedef)
  - [OutputTypeDef](#outputtypedef)
  - [ParameterConstraintsTypeDef](#parameterconstraintstypedef)
  - [ParameterDeclarationTypeDef](#parameterdeclarationtypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [PhysicalResourceIdContextKeyValuePairTypeDef](#physicalresourceidcontextkeyvaluepairtypedef)
  - [PropertyDifferenceTypeDef](#propertydifferencetypedef)
  - [ResourceChangeDetailTypeDef](#resourcechangedetailtypedef)
  - [ResourceChangeTypeDef](#resourcechangetypedef)
  - [ResourceIdentifierSummaryTypeDef](#resourceidentifiersummarytypedef)
  - [ResourceTargetDefinitionTypeDef](#resourcetargetdefinitiontypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RollbackConfigurationTypeDef](#rollbackconfigurationtypedef)
  - [RollbackTriggerTypeDef](#rollbacktriggertypedef)
  - [StackDriftInformationSummaryTypeDef](#stackdriftinformationsummarytypedef)
  - [StackDriftInformationTypeDef](#stackdriftinformationtypedef)
  - [StackEventTypeDef](#stackeventtypedef)
  - [StackInstanceComprehensiveStatusTypeDef](#stackinstancecomprehensivestatustypedef)
  - [StackInstanceSummaryTypeDef](#stackinstancesummarytypedef)
  - [StackInstanceTypeDef](#stackinstancetypedef)
  - [StackResourceDetailTypeDef](#stackresourcedetailtypedef)
  - [StackResourceDriftInformationSummaryTypeDef](#stackresourcedriftinformationsummarytypedef)
  - [StackResourceDriftInformationTypeDef](#stackresourcedriftinformationtypedef)
  - [StackResourceDriftTypeDef](#stackresourcedrifttypedef)
  - [StackResourceSummaryTypeDef](#stackresourcesummarytypedef)
  - [StackResourceTypeDef](#stackresourcetypedef)
  - [StackSetDriftDetectionDetailsTypeDef](#stacksetdriftdetectiondetailstypedef)
  - [StackSetOperationPreferencesTypeDef](#stacksetoperationpreferencestypedef)
  - [StackSetOperationResultSummaryTypeDef](#stacksetoperationresultsummarytypedef)
  - [StackSetOperationSummaryTypeDef](#stacksetoperationsummarytypedef)
  - [StackSetOperationTypeDef](#stacksetoperationtypedef)
  - [StackSetSummaryTypeDef](#stacksetsummarytypedef)
  - [StackSetTypeDef](#stacksettypedef)
  - [StackSummaryTypeDef](#stacksummarytypedef)
  - [StackTypeDef](#stacktypedef)
  - [TagTypeDef](#tagtypedef)
  - [TemplateParameterTypeDef](#templateparametertypedef)
  - [TypeSummaryTypeDef](#typesummarytypedef)
  - [TypeVersionSummaryTypeDef](#typeversionsummarytypedef)
  - [CreateChangeSetOutputTypeDef](#createchangesetoutputtypedef)
  - [CreateStackInstancesOutputTypeDef](#createstackinstancesoutputtypedef)
  - [CreateStackOutputTypeDef](#createstackoutputtypedef)
  - [CreateStackSetOutputTypeDef](#createstacksetoutputtypedef)
  - [DeleteStackInstancesOutputTypeDef](#deletestackinstancesoutputtypedef)
  - [DescribeAccountLimitsOutputTypeDef](#describeaccountlimitsoutputtypedef)
  - [DescribeChangeSetOutputTypeDef](#describechangesetoutputtypedef)
  - [DescribeStackDriftDetectionStatusOutputTypeDef](#describestackdriftdetectionstatusoutputtypedef)
  - [DescribeStackEventsOutputTypeDef](#describestackeventsoutputtypedef)
  - [DescribeStackInstanceOutputTypeDef](#describestackinstanceoutputtypedef)
  - [DescribeStackResourceDriftsOutputTypeDef](#describestackresourcedriftsoutputtypedef)
  - [DescribeStackResourceOutputTypeDef](#describestackresourceoutputtypedef)
  - [DescribeStackResourcesOutputTypeDef](#describestackresourcesoutputtypedef)
  - [DescribeStackSetOperationOutputTypeDef](#describestacksetoperationoutputtypedef)
  - [DescribeStackSetOutputTypeDef](#describestacksetoutputtypedef)
  - [DescribeStacksOutputTypeDef](#describestacksoutputtypedef)
  - [DescribeTypeOutputTypeDef](#describetypeoutputtypedef)
  - [DescribeTypeRegistrationOutputTypeDef](#describetyperegistrationoutputtypedef)
  - [DetectStackDriftOutputTypeDef](#detectstackdriftoutputtypedef)
  - [DetectStackResourceDriftOutputTypeDef](#detectstackresourcedriftoutputtypedef)
  - [DetectStackSetDriftOutputTypeDef](#detectstacksetdriftoutputtypedef)
  - [EstimateTemplateCostOutputTypeDef](#estimatetemplatecostoutputtypedef)
  - [GetStackPolicyOutputTypeDef](#getstackpolicyoutputtypedef)
  - [GetTemplateOutputTypeDef](#gettemplateoutputtypedef)
  - [GetTemplateSummaryOutputTypeDef](#gettemplatesummaryoutputtypedef)
  - [ListChangeSetsOutputTypeDef](#listchangesetsoutputtypedef)
  - [ListExportsOutputTypeDef](#listexportsoutputtypedef)
  - [ListImportsOutputTypeDef](#listimportsoutputtypedef)
  - [ListStackInstancesOutputTypeDef](#liststackinstancesoutputtypedef)
  - [ListStackResourcesOutputTypeDef](#liststackresourcesoutputtypedef)
  - [ListStackSetOperationResultsOutputTypeDef](#liststacksetoperationresultsoutputtypedef)
  - [ListStackSetOperationsOutputTypeDef](#liststacksetoperationsoutputtypedef)
  - [ListStackSetsOutputTypeDef](#liststacksetsoutputtypedef)
  - [ListStacksOutputTypeDef](#liststacksoutputtypedef)
  - [ListTypeRegistrationsOutputTypeDef](#listtyperegistrationsoutputtypedef)
  - [ListTypeVersionsOutputTypeDef](#listtypeversionsoutputtypedef)
  - [ListTypesOutputTypeDef](#listtypesoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RegisterTypeOutputTypeDef](#registertypeoutputtypedef)
  - [ResourceToImportTypeDef](#resourcetoimporttypedef)
  - [StackInstanceFilterTypeDef](#stackinstancefiltertypedef)
  - [UpdateStackInstancesOutputTypeDef](#updatestackinstancesoutputtypedef)
  - [UpdateStackOutputTypeDef](#updatestackoutputtypedef)
  - [UpdateStackSetOutputTypeDef](#updatestacksetoutputtypedef)
  - [UpdateTerminationProtectionOutputTypeDef](#updateterminationprotectionoutputtypedef)
  - [ValidateTemplateOutputTypeDef](#validatetemplateoutputtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountGateResultTypeDef

```python
from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef
```




Optional fields:
- `Status`: `AccountGateStatus`
- `StatusReason`: `str`


## AccountLimitTypeDef

```python
from mypy_boto3_cloudformation.type_defs import AccountLimitTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `int`


## AutoDeploymentTypeDef

```python
from mypy_boto3_cloudformation.type_defs import AutoDeploymentTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `RetainStacksOnAccountRemoval`: `bool`


## ChangeSetSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ChangeSetSummaryTypeDef
```




Optional fields:
- `StackId`: `str`
- `StackName`: `str`
- `ChangeSetId`: `str`
- `ChangeSetName`: `str`
- `ExecutionStatus`: `ExecutionStatus`
- `Status`: `ChangeSetStatus`
- `StatusReason`: `str`
- `CreationTime`: `datetime`
- `Description`: `str`
- `IncludeNestedStacks`: `bool`
- `ParentChangeSetId`: `str`
- `RootChangeSetId`: `str`


## ChangeTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ChangeTypeDef
```




Optional fields:
- `Type`: `ChangeType`
- `ResourceChange`: `"ResourceChangeTypeDef"`


## DeploymentTargetsTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DeploymentTargetsTypeDef
```




Optional fields:
- `Accounts`: `List[str]`
- `AccountsUrl`: `str`
- `OrganizationalUnitIds`: `List[str]`


## ExportTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ExportTypeDef
```




Optional fields:
- `ExportingStackId`: `str`
- `Name`: `str`
- `Value`: `str`


## LoggingConfigTypeDef

```python
from mypy_boto3_cloudformation.type_defs import LoggingConfigTypeDef
```


Required fields:
- `LogRoleArn`: `str`
- `LogGroupName`: `str`




## ModuleInfoTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ModuleInfoTypeDef
```




Optional fields:
- `TypeHierarchy`: `str`
- `LogicalIdHierarchy`: `str`


## OutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import OutputTypeDef
```




Optional fields:
- `OutputKey`: `str`
- `OutputValue`: `str`
- `Description`: `str`
- `ExportName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ParameterConstraintsTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ParameterConstraintsTypeDef
```




Optional fields:
- `AllowedValues`: `List[str]`


## ParameterDeclarationTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ParameterDeclarationTypeDef
```




Optional fields:
- `ParameterKey`: `str`
- `DefaultValue`: `str`
- `ParameterType`: `str`
- `NoEcho`: `bool`
- `Description`: `str`
- `ParameterConstraints`: `"ParameterConstraintsTypeDef"`


## ParameterTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ParameterTypeDef
```




Optional fields:
- `ParameterKey`: `str`
- `ParameterValue`: `str`
- `UsePreviousValue`: `bool`
- `ResolvedValue`: `str`


## PhysicalResourceIdContextKeyValuePairTypeDef

```python
from mypy_boto3_cloudformation.type_defs import PhysicalResourceIdContextKeyValuePairTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## PropertyDifferenceTypeDef

```python
from mypy_boto3_cloudformation.type_defs import PropertyDifferenceTypeDef
```


Required fields:
- `PropertyPath`: `str`
- `ExpectedValue`: `str`
- `ActualValue`: `str`
- `DifferenceType`: `DifferenceType`




## ResourceChangeDetailTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ResourceChangeDetailTypeDef
```




Optional fields:
- `Target`: `"ResourceTargetDefinitionTypeDef"`
- `Evaluation`: `EvaluationType`
- `ChangeSource`: `ChangeSource`
- `CausingEntity`: `str`


## ResourceChangeTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ResourceChangeTypeDef
```




Optional fields:
- `Action`: `ChangeAction`
- `LogicalResourceId`: `str`
- `PhysicalResourceId`: `str`
- `ResourceType`: `str`
- `Replacement`: `Replacement`
- `Scope`: `List[ResourceAttribute]`
- `Details`: `List["ResourceChangeDetailTypeDef"]`
- `ChangeSetId`: `str`
- `ModuleInfo`: `"ModuleInfoTypeDef"`


## ResourceIdentifierSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ResourceIdentifierSummaryTypeDef
```




Optional fields:
- `ResourceType`: `str`
- `LogicalResourceIds`: `List[str]`
- `ResourceIdentifiers`: `List[str]`


## ResourceTargetDefinitionTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ResourceTargetDefinitionTypeDef
```




Optional fields:
- `Attribute`: `ResourceAttribute`
- `Name`: `str`
- `RequiresRecreation`: `RequiresRecreation`


## ResponseMetadata

```python
from mypy_boto3_cloudformation.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RollbackConfigurationTypeDef

```python
from mypy_boto3_cloudformation.type_defs import RollbackConfigurationTypeDef
```




Optional fields:
- `RollbackTriggers`: `List["RollbackTriggerTypeDef"]`
- `MonitoringTimeInMinutes`: `int`


## RollbackTriggerTypeDef

```python
from mypy_boto3_cloudformation.type_defs import RollbackTriggerTypeDef
```


Required fields:
- `Arn`: `str`
- `Type`: `str`




## StackDriftInformationSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackDriftInformationSummaryTypeDef
```


Required fields:
- `StackDriftStatus`: `StackDriftStatus`



Optional fields:
- `LastCheckTimestamp`: `datetime`


## StackDriftInformationTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackDriftInformationTypeDef
```


Required fields:
- `StackDriftStatus`: `StackDriftStatus`



Optional fields:
- `LastCheckTimestamp`: `datetime`


## StackEventTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackEventTypeDef
```


Required fields:
- `StackId`: `str`
- `EventId`: `str`
- `StackName`: `str`
- `Timestamp`: `datetime`



Optional fields:
- `LogicalResourceId`: `str`
- `PhysicalResourceId`: `str`
- `ResourceType`: `str`
- `ResourceStatus`: `ResourceStatus`
- `ResourceStatusReason`: `str`
- `ResourceProperties`: `str`
- `ClientRequestToken`: `str`


## StackInstanceComprehensiveStatusTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackInstanceComprehensiveStatusTypeDef
```




Optional fields:
- `DetailedStatus`: `StackInstanceDetailedStatus`


## StackInstanceSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackInstanceSummaryTypeDef
```




Optional fields:
- `StackSetId`: `str`
- `Region`: `str`
- `Account`: `str`
- `StackId`: `str`
- `Status`: `StackInstanceStatus`
- `StatusReason`: `str`
- `StackInstanceStatus`: `"StackInstanceComprehensiveStatusTypeDef"`
- `OrganizationalUnitId`: `str`
- `DriftStatus`: `StackDriftStatus`
- `LastDriftCheckTimestamp`: `datetime`


## StackInstanceTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackInstanceTypeDef
```




Optional fields:
- `StackSetId`: `str`
- `Region`: `str`
- `Account`: `str`
- `StackId`: `str`
- `ParameterOverrides`: `List["ParameterTypeDef"]`
- `Status`: `StackInstanceStatus`
- `StackInstanceStatus`: `"StackInstanceComprehensiveStatusTypeDef"`
- `StatusReason`: `str`
- `OrganizationalUnitId`: `str`
- `DriftStatus`: `StackDriftStatus`
- `LastDriftCheckTimestamp`: `datetime`


## StackResourceDetailTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackResourceDetailTypeDef
```


Required fields:
- `LogicalResourceId`: `str`
- `ResourceType`: `str`
- `LastUpdatedTimestamp`: `datetime`
- `ResourceStatus`: `ResourceStatus`



Optional fields:
- `StackName`: `str`
- `StackId`: `str`
- `PhysicalResourceId`: `str`
- `ResourceStatusReason`: `str`
- `Description`: `str`
- `Metadata`: `str`
- `DriftInformation`: `"StackResourceDriftInformationTypeDef"`
- `ModuleInfo`: `"ModuleInfoTypeDef"`


## StackResourceDriftInformationSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackResourceDriftInformationSummaryTypeDef
```


Required fields:
- `StackResourceDriftStatus`: `StackResourceDriftStatus`



Optional fields:
- `LastCheckTimestamp`: `datetime`


## StackResourceDriftInformationTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackResourceDriftInformationTypeDef
```


Required fields:
- `StackResourceDriftStatus`: `StackResourceDriftStatus`



Optional fields:
- `LastCheckTimestamp`: `datetime`


## StackResourceDriftTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackResourceDriftTypeDef
```


Required fields:
- `StackId`: `str`
- `LogicalResourceId`: `str`
- `ResourceType`: `str`
- `StackResourceDriftStatus`: `StackResourceDriftStatus`
- `Timestamp`: `datetime`



Optional fields:
- `PhysicalResourceId`: `str`
- `PhysicalResourceIdContext`: `List["PhysicalResourceIdContextKeyValuePairTypeDef"]`
- `ExpectedProperties`: `str`
- `ActualProperties`: `str`
- `PropertyDifferences`: `List["PropertyDifferenceTypeDef"]`
- `ModuleInfo`: `"ModuleInfoTypeDef"`


## StackResourceSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackResourceSummaryTypeDef
```


Required fields:
- `LogicalResourceId`: `str`
- `ResourceType`: `str`
- `LastUpdatedTimestamp`: `datetime`
- `ResourceStatus`: `ResourceStatus`



Optional fields:
- `PhysicalResourceId`: `str`
- `ResourceStatusReason`: `str`
- `DriftInformation`: `"StackResourceDriftInformationSummaryTypeDef"`
- `ModuleInfo`: `"ModuleInfoTypeDef"`


## StackResourceTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackResourceTypeDef
```


Required fields:
- `LogicalResourceId`: `str`
- `ResourceType`: `str`
- `Timestamp`: `datetime`
- `ResourceStatus`: `ResourceStatus`



Optional fields:
- `StackName`: `str`
- `StackId`: `str`
- `PhysicalResourceId`: `str`
- `ResourceStatusReason`: `str`
- `Description`: `str`
- `DriftInformation`: `"StackResourceDriftInformationTypeDef"`
- `ModuleInfo`: `"ModuleInfoTypeDef"`


## StackSetDriftDetectionDetailsTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetDriftDetectionDetailsTypeDef
```




Optional fields:
- `DriftStatus`: `StackSetDriftStatus`
- `DriftDetectionStatus`: `StackSetDriftDetectionStatus`
- `LastDriftCheckTimestamp`: `datetime`
- `TotalStackInstancesCount`: `int`
- `DriftedStackInstancesCount`: `int`
- `InSyncStackInstancesCount`: `int`
- `InProgressStackInstancesCount`: `int`
- `FailedStackInstancesCount`: `int`


## StackSetOperationPreferencesTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetOperationPreferencesTypeDef
```




Optional fields:
- `RegionConcurrencyType`: `RegionConcurrencyType`
- `RegionOrder`: `List[str]`
- `FailureToleranceCount`: `int`
- `FailureTolerancePercentage`: `int`
- `MaxConcurrentCount`: `int`
- `MaxConcurrentPercentage`: `int`


## StackSetOperationResultSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetOperationResultSummaryTypeDef
```




Optional fields:
- `Account`: `str`
- `Region`: `str`
- `Status`: `StackSetOperationResultStatus`
- `StatusReason`: `str`
- `AccountGateResult`: `"AccountGateResultTypeDef"`
- `OrganizationalUnitId`: `str`


## StackSetOperationSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetOperationSummaryTypeDef
```




Optional fields:
- `OperationId`: `str`
- `Action`: `StackSetOperationAction`
- `Status`: `StackSetOperationStatus`
- `CreationTimestamp`: `datetime`
- `EndTimestamp`: `datetime`


## StackSetOperationTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetOperationTypeDef
```




Optional fields:
- `OperationId`: `str`
- `StackSetId`: `str`
- `Action`: `StackSetOperationAction`
- `Status`: `StackSetOperationStatus`
- `OperationPreferences`: `"StackSetOperationPreferencesTypeDef"`
- `RetainStacks`: `bool`
- `AdministrationRoleARN`: `str`
- `ExecutionRoleName`: `str`
- `CreationTimestamp`: `datetime`
- `EndTimestamp`: `datetime`
- `DeploymentTargets`: `"DeploymentTargetsTypeDef"`
- `StackSetDriftDetectionDetails`: `"StackSetDriftDetectionDetailsTypeDef"`


## StackSetSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetSummaryTypeDef
```




Optional fields:
- `StackSetName`: `str`
- `StackSetId`: `str`
- `Description`: `str`
- `Status`: `StackSetStatus`
- `AutoDeployment`: `"AutoDeploymentTypeDef"`
- `PermissionModel`: `PermissionModels`
- `DriftStatus`: `StackDriftStatus`
- `LastDriftCheckTimestamp`: `datetime`


## StackSetTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSetTypeDef
```




Optional fields:
- `StackSetName`: `str`
- `StackSetId`: `str`
- `Description`: `str`
- `Status`: `StackSetStatus`
- `TemplateBody`: `str`
- `Parameters`: `List["ParameterTypeDef"]`
- `Capabilities`: `List[Capability]`
- `Tags`: `List["TagTypeDef"]`
- `StackSetARN`: `str`
- `AdministrationRoleARN`: `str`
- `ExecutionRoleName`: `str`
- `StackSetDriftDetectionDetails`: `"StackSetDriftDetectionDetailsTypeDef"`
- `AutoDeployment`: `"AutoDeploymentTypeDef"`
- `PermissionModel`: `PermissionModels`
- `OrganizationalUnitIds`: `List[str]`


## StackSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackSummaryTypeDef
```


Required fields:
- `StackName`: `str`
- `CreationTime`: `datetime`
- `StackStatus`: `StackStatus`



Optional fields:
- `StackId`: `str`
- `TemplateDescription`: `str`
- `LastUpdatedTime`: `datetime`
- `DeletionTime`: `datetime`
- `StackStatusReason`: `str`
- `ParentId`: `str`
- `RootId`: `str`
- `DriftInformation`: `"StackDriftInformationSummaryTypeDef"`


## StackTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackTypeDef
```


Required fields:
- `StackName`: `str`
- `CreationTime`: `datetime`
- `StackStatus`: `StackStatus`



Optional fields:
- `StackId`: `str`
- `ChangeSetId`: `str`
- `Description`: `str`
- `Parameters`: `List["ParameterTypeDef"]`
- `DeletionTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `RollbackConfiguration`: `"RollbackConfigurationTypeDef"`
- `StackStatusReason`: `str`
- `DisableRollback`: `bool`
- `NotificationARNs`: `List[str]`
- `TimeoutInMinutes`: `int`
- `Capabilities`: `List[Capability]`
- `Outputs`: `List["OutputTypeDef"]`
- `RoleARN`: `str`
- `Tags`: `List["TagTypeDef"]`
- `EnableTerminationProtection`: `bool`
- `ParentId`: `str`
- `RootId`: `str`
- `DriftInformation`: `"StackDriftInformationTypeDef"`


## TagTypeDef

```python
from mypy_boto3_cloudformation.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TemplateParameterTypeDef

```python
from mypy_boto3_cloudformation.type_defs import TemplateParameterTypeDef
```




Optional fields:
- `ParameterKey`: `str`
- `DefaultValue`: `str`
- `NoEcho`: `bool`
- `Description`: `str`


## TypeSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import TypeSummaryTypeDef
```




Optional fields:
- `Type`: `RegistryType`
- `TypeName`: `str`
- `DefaultVersionId`: `str`
- `TypeArn`: `str`
- `LastUpdated`: `datetime`
- `Description`: `str`


## TypeVersionSummaryTypeDef

```python
from mypy_boto3_cloudformation.type_defs import TypeVersionSummaryTypeDef
```




Optional fields:
- `Type`: `RegistryType`
- `TypeName`: `str`
- `VersionId`: `str`
- `IsDefaultVersion`: `bool`
- `Arn`: `str`
- `TimeCreated`: `datetime`
- `Description`: `str`


## CreateChangeSetOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import CreateChangeSetOutputTypeDef
```




Optional fields:
- `Id`: `str`
- `StackId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStackInstancesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import CreateStackInstancesOutputTypeDef
```




Optional fields:
- `OperationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStackOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import CreateStackOutputTypeDef
```




Optional fields:
- `StackId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStackSetOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import CreateStackSetOutputTypeDef
```




Optional fields:
- `StackSetId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteStackInstancesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DeleteStackInstancesOutputTypeDef
```




Optional fields:
- `OperationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAccountLimitsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeAccountLimitsOutputTypeDef
```




Optional fields:
- `AccountLimits`: `List["AccountLimitTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeChangeSetOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeChangeSetOutputTypeDef
```




Optional fields:
- `ChangeSetName`: `str`
- `ChangeSetId`: `str`
- `StackId`: `str`
- `StackName`: `str`
- `Description`: `str`
- `Parameters`: `List["ParameterTypeDef"]`
- `CreationTime`: `datetime`
- `ExecutionStatus`: `ExecutionStatus`
- `Status`: `ChangeSetStatus`
- `StatusReason`: `str`
- `NotificationARNs`: `List[str]`
- `RollbackConfiguration`: `"RollbackConfigurationTypeDef"`
- `Capabilities`: `List[Capability]`
- `Tags`: `List["TagTypeDef"]`
- `Changes`: `List["ChangeTypeDef"]`
- `NextToken`: `str`
- `IncludeNestedStacks`: `bool`
- `ParentChangeSetId`: `str`
- `RootChangeSetId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackDriftDetectionStatusOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackDriftDetectionStatusOutputTypeDef
```


Required fields:
- `StackId`: `str`
- `StackDriftDetectionId`: `str`
- `DetectionStatus`: `StackDriftDetectionStatus`
- `Timestamp`: `datetime`



Optional fields:
- `StackDriftStatus`: `StackDriftStatus`
- `DetectionStatusReason`: `str`
- `DriftedStackResourceCount`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackEventsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackEventsOutputTypeDef
```




Optional fields:
- `StackEvents`: `List["StackEventTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackInstanceOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackInstanceOutputTypeDef
```




Optional fields:
- `StackInstance`: `"StackInstanceTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackResourceDriftsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackResourceDriftsOutputTypeDef
```


Required fields:
- `StackResourceDrifts`: `List["StackResourceDriftTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackResourceOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackResourceOutputTypeDef
```




Optional fields:
- `StackResourceDetail`: `"StackResourceDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackResourcesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackResourcesOutputTypeDef
```




Optional fields:
- `StackResources`: `List["StackResourceTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackSetOperationOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackSetOperationOutputTypeDef
```




Optional fields:
- `StackSetOperation`: `"StackSetOperationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStackSetOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStackSetOutputTypeDef
```




Optional fields:
- `StackSet`: `"StackSetTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStacksOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeStacksOutputTypeDef
```




Optional fields:
- `Stacks`: `List["StackTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTypeOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeTypeOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `Type`: `RegistryType`
- `TypeName`: `str`
- `DefaultVersionId`: `str`
- `IsDefaultVersion`: `bool`
- `Description`: `str`
- `Schema`: `str`
- `ProvisioningType`: `ProvisioningType`
- `DeprecatedStatus`: `DeprecatedStatus`
- `LoggingConfig`: `"LoggingConfigTypeDef"`
- `ExecutionRoleArn`: `str`
- `Visibility`: `Visibility`
- `SourceUrl`: `str`
- `DocumentationUrl`: `str`
- `LastUpdated`: `datetime`
- `TimeCreated`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTypeRegistrationOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DescribeTypeRegistrationOutputTypeDef
```




Optional fields:
- `ProgressStatus`: `RegistrationStatus`
- `Description`: `str`
- `TypeArn`: `str`
- `TypeVersionArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DetectStackDriftOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DetectStackDriftOutputTypeDef
```


Required fields:
- `StackDriftDetectionId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DetectStackResourceDriftOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DetectStackResourceDriftOutputTypeDef
```


Required fields:
- `StackResourceDrift`: `"StackResourceDriftTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DetectStackSetDriftOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import DetectStackSetDriftOutputTypeDef
```




Optional fields:
- `OperationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## EstimateTemplateCostOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import EstimateTemplateCostOutputTypeDef
```




Optional fields:
- `Url`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetStackPolicyOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import GetStackPolicyOutputTypeDef
```




Optional fields:
- `StackPolicyBody`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTemplateOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import GetTemplateOutputTypeDef
```




Optional fields:
- `TemplateBody`: `str`
- `StagesAvailable`: `List[TemplateStage]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTemplateSummaryOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import GetTemplateSummaryOutputTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterDeclarationTypeDef"]`
- `Description`: `str`
- `Capabilities`: `List[Capability]`
- `CapabilitiesReason`: `str`
- `ResourceTypes`: `List[str]`
- `Version`: `str`
- `Metadata`: `str`
- `DeclaredTransforms`: `List[str]`
- `ResourceIdentifierSummaries`: `List["ResourceIdentifierSummaryTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListChangeSetsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListChangeSetsOutputTypeDef
```




Optional fields:
- `Summaries`: `List["ChangeSetSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListExportsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListExportsOutputTypeDef
```




Optional fields:
- `Exports`: `List["ExportTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListImportsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListImportsOutputTypeDef
```




Optional fields:
- `Imports`: `List[str]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStackInstancesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListStackInstancesOutputTypeDef
```




Optional fields:
- `Summaries`: `List["StackInstanceSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStackResourcesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListStackResourcesOutputTypeDef
```




Optional fields:
- `StackResourceSummaries`: `List["StackResourceSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStackSetOperationResultsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListStackSetOperationResultsOutputTypeDef
```




Optional fields:
- `Summaries`: `List["StackSetOperationResultSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStackSetOperationsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListStackSetOperationsOutputTypeDef
```




Optional fields:
- `Summaries`: `List["StackSetOperationSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStackSetsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListStackSetsOutputTypeDef
```




Optional fields:
- `Summaries`: `List["StackSetSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStacksOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListStacksOutputTypeDef
```




Optional fields:
- `StackSummaries`: `List["StackSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTypeRegistrationsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListTypeRegistrationsOutputTypeDef
```




Optional fields:
- `RegistrationTokenList`: `List[str]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTypeVersionsOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListTypeVersionsOutputTypeDef
```




Optional fields:
- `TypeVersionSummaries`: `List["TypeVersionSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTypesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ListTypesOutputTypeDef
```




Optional fields:
- `TypeSummaries`: `List["TypeSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cloudformation.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RegisterTypeOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import RegisterTypeOutputTypeDef
```




Optional fields:
- `RegistrationToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResourceToImportTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ResourceToImportTypeDef
```


Required fields:
- `ResourceType`: `str`
- `LogicalResourceId`: `str`
- `ResourceIdentifier`: `Dict[str, str]`




## StackInstanceFilterTypeDef

```python
from mypy_boto3_cloudformation.type_defs import StackInstanceFilterTypeDef
```




Optional fields:
- `Name`: `StackInstanceFilterName`
- `Values`: `str`


## UpdateStackInstancesOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import UpdateStackInstancesOutputTypeDef
```




Optional fields:
- `OperationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateStackOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import UpdateStackOutputTypeDef
```




Optional fields:
- `StackId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateStackSetOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import UpdateStackSetOutputTypeDef
```




Optional fields:
- `OperationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateTerminationProtectionOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import UpdateTerminationProtectionOutputTypeDef
```




Optional fields:
- `StackId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ValidateTemplateOutputTypeDef

```python
from mypy_boto3_cloudformation.type_defs import ValidateTemplateOutputTypeDef
```




Optional fields:
- `Parameters`: `List["TemplateParameterTypeDef"]`
- `Description`: `str`
- `Capabilities`: `List[Capability]`
- `CapabilitiesReason`: `str`
- `DeclaredTransforms`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## WaiterConfigTypeDef

```python
from mypy_boto3_cloudformation.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

