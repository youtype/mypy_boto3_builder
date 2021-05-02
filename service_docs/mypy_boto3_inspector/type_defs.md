# Structures for boto3 Inspector module

> [Index](../index.md) > [Inspector](./index.md) > Structures

Auto-generated documentation for [Inspector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector)
type annotations stubs module [mypy_boto3_inspector](https://pypi.org/project/mypy-boto3-inspector/).

- [Structures for boto3 Inspector module](#structures-for-boto3-inspector-module)
  - [AddAttributesToFindingsResponseTypeDef](#addattributestofindingsresponsetypedef)
  - [AgentFilterTypeDef](#agentfiltertypedef)
  - [AgentPreviewTypeDef](#agentpreviewtypedef)
  - [AssessmentRunAgentTypeDef](#assessmentrunagenttypedef)
  - [AssessmentRunFilterTypeDef](#assessmentrunfiltertypedef)
  - [AssessmentRunNotificationTypeDef](#assessmentrunnotificationtypedef)
  - [AssessmentRunStateChangeTypeDef](#assessmentrunstatechangetypedef)
  - [AssessmentRunTypeDef](#assessmentruntypedef)
  - [AssessmentTargetFilterTypeDef](#assessmenttargetfiltertypedef)
  - [AssessmentTargetTypeDef](#assessmenttargettypedef)
  - [AssessmentTemplateFilterTypeDef](#assessmenttemplatefiltertypedef)
  - [AssessmentTemplateTypeDef](#assessmenttemplatetypedef)
  - [AssetAttributesTypeDef](#assetattributestypedef)
  - [AttributeTypeDef](#attributetypedef)
  - [CreateAssessmentTargetResponseTypeDef](#createassessmenttargetresponsetypedef)
  - [CreateAssessmentTemplateResponseTypeDef](#createassessmenttemplateresponsetypedef)
  - [CreateExclusionsPreviewResponseTypeDef](#createexclusionspreviewresponsetypedef)
  - [CreateResourceGroupResponseTypeDef](#createresourcegroupresponsetypedef)
  - [DescribeAssessmentRunsResponseTypeDef](#describeassessmentrunsresponsetypedef)
  - [DescribeAssessmentTargetsResponseTypeDef](#describeassessmenttargetsresponsetypedef)
  - [DescribeAssessmentTemplatesResponseTypeDef](#describeassessmenttemplatesresponsetypedef)
  - [DescribeCrossAccountAccessRoleResponseTypeDef](#describecrossaccountaccessroleresponsetypedef)
  - [DescribeExclusionsResponseTypeDef](#describeexclusionsresponsetypedef)
  - [DescribeFindingsResponseTypeDef](#describefindingsresponsetypedef)
  - [DescribeResourceGroupsResponseTypeDef](#describeresourcegroupsresponsetypedef)
  - [DescribeRulesPackagesResponseTypeDef](#describerulespackagesresponsetypedef)
  - [DurationRangeTypeDef](#durationrangetypedef)
  - [EventSubscriptionTypeDef](#eventsubscriptiontypedef)
  - [ExclusionPreviewTypeDef](#exclusionpreviewtypedef)
  - [ExclusionTypeDef](#exclusiontypedef)
  - [FailedItemDetailsTypeDef](#faileditemdetailstypedef)
  - [FindingFilterTypeDef](#findingfiltertypedef)
  - [FindingTypeDef](#findingtypedef)
  - [GetAssessmentReportResponseTypeDef](#getassessmentreportresponsetypedef)
  - [GetExclusionsPreviewResponseTypeDef](#getexclusionspreviewresponsetypedef)
  - [GetTelemetryMetadataResponseTypeDef](#gettelemetrymetadataresponsetypedef)
  - [InspectorServiceAttributesTypeDef](#inspectorserviceattributestypedef)
  - [ListAssessmentRunAgentsResponseTypeDef](#listassessmentrunagentsresponsetypedef)
  - [ListAssessmentRunsResponseTypeDef](#listassessmentrunsresponsetypedef)
  - [ListAssessmentTargetsResponseTypeDef](#listassessmenttargetsresponsetypedef)
  - [ListAssessmentTemplatesResponseTypeDef](#listassessmenttemplatesresponsetypedef)
  - [ListEventSubscriptionsResponseTypeDef](#listeventsubscriptionsresponsetypedef)
  - [ListExclusionsResponseTypeDef](#listexclusionsresponsetypedef)
  - [ListFindingsResponseTypeDef](#listfindingsresponsetypedef)
  - [ListRulesPackagesResponseTypeDef](#listrulespackagesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PreviewAgentsResponseTypeDef](#previewagentsresponsetypedef)
  - [PrivateIpTypeDef](#privateiptypedef)
  - [RemoveAttributesFromFindingsResponseTypeDef](#removeattributesfromfindingsresponsetypedef)
  - [ResourceGroupTagTypeDef](#resourcegrouptagtypedef)
  - [ResourceGroupTypeDef](#resourcegrouptypedef)
  - [RulesPackageTypeDef](#rulespackagetypedef)
  - [ScopeTypeDef](#scopetypedef)
  - [SecurityGroupTypeDef](#securitygrouptypedef)
  - [StartAssessmentRunResponseTypeDef](#startassessmentrunresponsetypedef)
  - [SubscriptionTypeDef](#subscriptiontypedef)
  - [TagTypeDef](#tagtypedef)
  - [TelemetryMetadataTypeDef](#telemetrymetadatatypedef)
  - [TimestampRangeTypeDef](#timestamprangetypedef)

## AddAttributesToFindingsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import AddAttributesToFindingsResponseTypeDef
```


Required fields:
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## AgentFilterTypeDef

```python
from mypy_boto3_inspector.type_defs import AgentFilterTypeDef
```


Required fields:
- `agentHealths`: `List[AgentHealth]`
- `agentHealthCodes`: `List[AgentHealthCode]`




## AgentPreviewTypeDef

```python
from mypy_boto3_inspector.type_defs import AgentPreviewTypeDef
```


Required fields:
- `agentId`: `str`



Optional fields:
- `hostname`: `str`
- `autoScalingGroup`: `str`
- `agentHealth`: `AgentHealth`
- `agentVersion`: `str`
- `operatingSystem`: `str`
- `kernelVersion`: `str`
- `ipv4Address`: `str`


## AssessmentRunAgentTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentRunAgentTypeDef
```


Required fields:
- `agentId`: `str`
- `assessmentRunArn`: `str`
- `agentHealth`: `AgentHealth`
- `agentHealthCode`: `AgentHealthCode`
- `telemetryMetadata`: `List["TelemetryMetadataTypeDef"]`



Optional fields:
- `agentHealthDetails`: `str`
- `autoScalingGroup`: `str`


## AssessmentRunFilterTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentRunFilterTypeDef
```




Optional fields:
- `namePattern`: `str`
- `states`: `List[AssessmentRunState]`
- `durationRange`: `"DurationRangeTypeDef"`
- `rulesPackageArns`: `List[str]`
- `startTimeRange`: `"TimestampRangeTypeDef"`
- `completionTimeRange`: `"TimestampRangeTypeDef"`
- `stateChangeTimeRange`: `"TimestampRangeTypeDef"`


## AssessmentRunNotificationTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentRunNotificationTypeDef
```


Required fields:
- `date`: `datetime`
- `event`: `InspectorEvent`
- `error`: `bool`



Optional fields:
- `message`: `str`
- `snsTopicArn`: `str`
- `snsPublishStatusCode`: `AssessmentRunNotificationSnsStatusCode`


## AssessmentRunStateChangeTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentRunStateChangeTypeDef
```


Required fields:
- `stateChangedAt`: `datetime`
- `state`: `AssessmentRunState`




## AssessmentRunTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentRunTypeDef
```


Required fields:
- `arn`: `str`
- `name`: `str`
- `assessmentTemplateArn`: `str`
- `state`: `AssessmentRunState`
- `durationInSeconds`: `int`
- `rulesPackageArns`: `List[str]`
- `userAttributesForFindings`: `List["AttributeTypeDef"]`
- `createdAt`: `datetime`
- `stateChangedAt`: `datetime`
- `dataCollected`: `bool`
- `stateChanges`: `List["AssessmentRunStateChangeTypeDef"]`
- `notifications`: `List["AssessmentRunNotificationTypeDef"]`
- `findingCounts`: `Dict[Severity, int]`



Optional fields:
- `startedAt`: `datetime`
- `completedAt`: `datetime`


## AssessmentTargetFilterTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentTargetFilterTypeDef
```




Optional fields:
- `assessmentTargetNamePattern`: `str`


## AssessmentTargetTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentTargetTypeDef
```


Required fields:
- `arn`: `str`
- `name`: `str`
- `createdAt`: `datetime`
- `updatedAt`: `datetime`



Optional fields:
- `resourceGroupArn`: `str`


## AssessmentTemplateFilterTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentTemplateFilterTypeDef
```




Optional fields:
- `namePattern`: `str`
- `durationRange`: `"DurationRangeTypeDef"`
- `rulesPackageArns`: `List[str]`


## AssessmentTemplateTypeDef

```python
from mypy_boto3_inspector.type_defs import AssessmentTemplateTypeDef
```


Required fields:
- `arn`: `str`
- `name`: `str`
- `assessmentTargetArn`: `str`
- `durationInSeconds`: `int`
- `rulesPackageArns`: `List[str]`
- `userAttributesForFindings`: `List["AttributeTypeDef"]`
- `assessmentRunCount`: `int`
- `createdAt`: `datetime`



Optional fields:
- `lastAssessmentRunArn`: `str`


## AssetAttributesTypeDef

```python
from mypy_boto3_inspector.type_defs import AssetAttributesTypeDef
```


Required fields:
- `schemaVersion`: `int`



Optional fields:
- `agentId`: `str`
- `autoScalingGroup`: `str`
- `amiId`: `str`
- `hostname`: `str`
- `ipv4Addresses`: `List[str]`
- `tags`: `List["TagTypeDef"]`
- `networkInterfaces`: `List["NetworkInterfaceTypeDef"]`


## AttributeTypeDef

```python
from mypy_boto3_inspector.type_defs import AttributeTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `value`: `str`


## CreateAssessmentTargetResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import CreateAssessmentTargetResponseTypeDef
```


Required fields:
- `assessmentTargetArn`: `str`




## CreateAssessmentTemplateResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import CreateAssessmentTemplateResponseTypeDef
```


Required fields:
- `assessmentTemplateArn`: `str`




## CreateExclusionsPreviewResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import CreateExclusionsPreviewResponseTypeDef
```


Required fields:
- `previewToken`: `str`




## CreateResourceGroupResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import CreateResourceGroupResponseTypeDef
```


Required fields:
- `resourceGroupArn`: `str`




## DescribeAssessmentRunsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeAssessmentRunsResponseTypeDef
```


Required fields:
- `assessmentRuns`: `List["AssessmentRunTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DescribeAssessmentTargetsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeAssessmentTargetsResponseTypeDef
```


Required fields:
- `assessmentTargets`: `List["AssessmentTargetTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DescribeAssessmentTemplatesResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeAssessmentTemplatesResponseTypeDef
```


Required fields:
- `assessmentTemplates`: `List["AssessmentTemplateTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DescribeCrossAccountAccessRoleResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeCrossAccountAccessRoleResponseTypeDef
```


Required fields:
- `roleArn`: `str`
- `valid`: `bool`
- `registeredAt`: `datetime`




## DescribeExclusionsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeExclusionsResponseTypeDef
```


Required fields:
- `exclusions`: `Dict[str, "ExclusionTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DescribeFindingsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeFindingsResponseTypeDef
```


Required fields:
- `findings`: `List["FindingTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DescribeResourceGroupsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeResourceGroupsResponseTypeDef
```


Required fields:
- `resourceGroups`: `List["ResourceGroupTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DescribeRulesPackagesResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import DescribeRulesPackagesResponseTypeDef
```


Required fields:
- `rulesPackages`: `List["RulesPackageTypeDef"]`
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## DurationRangeTypeDef

```python
from mypy_boto3_inspector.type_defs import DurationRangeTypeDef
```




Optional fields:
- `minSeconds`: `int`
- `maxSeconds`: `int`


## EventSubscriptionTypeDef

```python
from mypy_boto3_inspector.type_defs import EventSubscriptionTypeDef
```


Required fields:
- `event`: `InspectorEvent`
- `subscribedAt`: `datetime`




## ExclusionPreviewTypeDef

```python
from mypy_boto3_inspector.type_defs import ExclusionPreviewTypeDef
```


Required fields:
- `title`: `str`
- `description`: `str`
- `recommendation`: `str`
- `scopes`: `List["ScopeTypeDef"]`



Optional fields:
- `attributes`: `List["AttributeTypeDef"]`


## ExclusionTypeDef

```python
from mypy_boto3_inspector.type_defs import ExclusionTypeDef
```


Required fields:
- `arn`: `str`
- `title`: `str`
- `description`: `str`
- `recommendation`: `str`
- `scopes`: `List["ScopeTypeDef"]`



Optional fields:
- `attributes`: `List["AttributeTypeDef"]`


## FailedItemDetailsTypeDef

```python
from mypy_boto3_inspector.type_defs import FailedItemDetailsTypeDef
```


Required fields:
- `failureCode`: `FailedItemErrorCode`
- `retryable`: `bool`




## FindingFilterTypeDef

```python
from mypy_boto3_inspector.type_defs import FindingFilterTypeDef
```




Optional fields:
- `agentIds`: `List[str]`
- `autoScalingGroups`: `List[str]`
- `ruleNames`: `List[str]`
- `severities`: `List[Severity]`
- `rulesPackageArns`: `List[str]`
- `attributes`: `List["AttributeTypeDef"]`
- `userAttributes`: `List["AttributeTypeDef"]`
- `creationTimeRange`: `"TimestampRangeTypeDef"`


## FindingTypeDef

```python
from mypy_boto3_inspector.type_defs import FindingTypeDef
```


Required fields:
- `arn`: `str`
- `attributes`: `List["AttributeTypeDef"]`
- `userAttributes`: `List["AttributeTypeDef"]`
- `createdAt`: `datetime`
- `updatedAt`: `datetime`



Optional fields:
- `schemaVersion`: `int`
- `service`: `str`
- `serviceAttributes`: `"InspectorServiceAttributesTypeDef"`
- `assetType`: `Literal['ec2-instance']`
- `assetAttributes`: `"AssetAttributesTypeDef"`
- `id`: `str`
- `title`: `str`
- `description`: `str`
- `recommendation`: `str`
- `severity`: `Severity`
- `numericSeverity`: `float`
- `confidence`: `int`
- `indicatorOfCompromise`: `bool`


## GetAssessmentReportResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import GetAssessmentReportResponseTypeDef
```


Required fields:
- `status`: `ReportStatus`



Optional fields:
- `url`: `str`


## GetExclusionsPreviewResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import GetExclusionsPreviewResponseTypeDef
```


Required fields:
- `previewStatus`: `PreviewStatus`



Optional fields:
- `exclusionPreviews`: `List["ExclusionPreviewTypeDef"]`
- `nextToken`: `str`


## GetTelemetryMetadataResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import GetTelemetryMetadataResponseTypeDef
```


Required fields:
- `telemetryMetadata`: `List["TelemetryMetadataTypeDef"]`




## InspectorServiceAttributesTypeDef

```python
from mypy_boto3_inspector.type_defs import InspectorServiceAttributesTypeDef
```


Required fields:
- `schemaVersion`: `int`



Optional fields:
- `assessmentRunArn`: `str`
- `rulesPackageArn`: `str`


## ListAssessmentRunAgentsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListAssessmentRunAgentsResponseTypeDef
```


Required fields:
- `assessmentRunAgents`: `List["AssessmentRunAgentTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListAssessmentRunsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListAssessmentRunsResponseTypeDef
```


Required fields:
- `assessmentRunArns`: `List[str]`



Optional fields:
- `nextToken`: `str`


## ListAssessmentTargetsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListAssessmentTargetsResponseTypeDef
```


Required fields:
- `assessmentTargetArns`: `List[str]`



Optional fields:
- `nextToken`: `str`


## ListAssessmentTemplatesResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListAssessmentTemplatesResponseTypeDef
```


Required fields:
- `assessmentTemplateArns`: `List[str]`



Optional fields:
- `nextToken`: `str`


## ListEventSubscriptionsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListEventSubscriptionsResponseTypeDef
```


Required fields:
- `subscriptions`: `List["SubscriptionTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListExclusionsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListExclusionsResponseTypeDef
```


Required fields:
- `exclusionArns`: `List[str]`



Optional fields:
- `nextToken`: `str`


## ListFindingsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListFindingsResponseTypeDef
```


Required fields:
- `findingArns`: `List[str]`



Optional fields:
- `nextToken`: `str`


## ListRulesPackagesResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListRulesPackagesResponseTypeDef
```


Required fields:
- `rulesPackageArns`: `List[str]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import ListTagsForResourceResponseTypeDef
```


Required fields:
- `tags`: `List["TagTypeDef"]`




## NetworkInterfaceTypeDef

```python
from mypy_boto3_inspector.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `networkInterfaceId`: `str`
- `subnetId`: `str`
- `vpcId`: `str`
- `privateDnsName`: `str`
- `privateIpAddress`: `str`
- `privateIpAddresses`: `List["PrivateIpTypeDef"]`
- `publicDnsName`: `str`
- `publicIp`: `str`
- `ipv6Addresses`: `List[str]`
- `securityGroups`: `List["SecurityGroupTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_inspector.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PreviewAgentsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import PreviewAgentsResponseTypeDef
```


Required fields:
- `agentPreviews`: `List["AgentPreviewTypeDef"]`



Optional fields:
- `nextToken`: `str`


## PrivateIpTypeDef

```python
from mypy_boto3_inspector.type_defs import PrivateIpTypeDef
```




Optional fields:
- `privateDnsName`: `str`
- `privateIpAddress`: `str`


## RemoveAttributesFromFindingsResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import RemoveAttributesFromFindingsResponseTypeDef
```


Required fields:
- `failedItems`: `Dict[str, "FailedItemDetailsTypeDef"]`




## ResourceGroupTagTypeDef

```python
from mypy_boto3_inspector.type_defs import ResourceGroupTagTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `value`: `str`


## ResourceGroupTypeDef

```python
from mypy_boto3_inspector.type_defs import ResourceGroupTypeDef
```


Required fields:
- `arn`: `str`
- `tags`: `List["ResourceGroupTagTypeDef"]`
- `createdAt`: `datetime`




## RulesPackageTypeDef

```python
from mypy_boto3_inspector.type_defs import RulesPackageTypeDef
```


Required fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `provider`: `str`



Optional fields:
- `description`: `str`


## ScopeTypeDef

```python
from mypy_boto3_inspector.type_defs import ScopeTypeDef
```




Optional fields:
- `key`: `ScopeType`
- `value`: `str`


## SecurityGroupTypeDef

```python
from mypy_boto3_inspector.type_defs import SecurityGroupTypeDef
```




Optional fields:
- `groupName`: `str`
- `groupId`: `str`


## StartAssessmentRunResponseTypeDef

```python
from mypy_boto3_inspector.type_defs import StartAssessmentRunResponseTypeDef
```


Required fields:
- `assessmentRunArn`: `str`




## SubscriptionTypeDef

```python
from mypy_boto3_inspector.type_defs import SubscriptionTypeDef
```


Required fields:
- `resourceArn`: `str`
- `topicArn`: `str`
- `eventSubscriptions`: `List["EventSubscriptionTypeDef"]`




## TagTypeDef

```python
from mypy_boto3_inspector.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `value`: `str`


## TelemetryMetadataTypeDef

```python
from mypy_boto3_inspector.type_defs import TelemetryMetadataTypeDef
```


Required fields:
- `messageType`: `str`
- `count`: `int`



Optional fields:
- `dataSize`: `int`


## TimestampRangeTypeDef

```python
from mypy_boto3_inspector.type_defs import TimestampRangeTypeDef
```




Optional fields:
- `beginDate`: `datetime`
- `endDate`: `datetime`

