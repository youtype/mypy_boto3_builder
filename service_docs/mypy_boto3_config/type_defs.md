# Structures for boto3 ConfigService module

> [Index](../index.md) > [ConfigService](./index.md) > Structures

Auto-generated documentation for [ConfigService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService)
type annotations stubs module [mypy_boto3_config](https://pypi.org/project/mypy-boto3-config/).

- [Structures for boto3 ConfigService module](#structures-for-boto3-configservice-module)
  - [AccountAggregationSourceTypeDef](#accountaggregationsourcetypedef)
  - [AggregateComplianceByConfigRuleTypeDef](#aggregatecompliancebyconfigruletypedef)
  - [AggregateComplianceByConformancePackTypeDef](#aggregatecompliancebyconformancepacktypedef)
  - [AggregateComplianceCountTypeDef](#aggregatecompliancecounttypedef)
  - [AggregateConformancePackComplianceCountTypeDef](#aggregateconformancepackcompliancecounttypedef)
  - [AggregateConformancePackComplianceFiltersTypeDef](#aggregateconformancepackcompliancefilterstypedef)
  - [AggregateConformancePackComplianceSummaryFiltersTypeDef](#aggregateconformancepackcompliancesummaryfilterstypedef)
  - [AggregateConformancePackComplianceSummaryTypeDef](#aggregateconformancepackcompliancesummarytypedef)
  - [AggregateConformancePackComplianceTypeDef](#aggregateconformancepackcompliancetypedef)
  - [AggregateEvaluationResultTypeDef](#aggregateevaluationresulttypedef)
  - [AggregateResourceIdentifierTypeDef](#aggregateresourceidentifiertypedef)
  - [AggregatedSourceStatusTypeDef](#aggregatedsourcestatustypedef)
  - [AggregationAuthorizationTypeDef](#aggregationauthorizationtypedef)
  - [BaseConfigurationItemTypeDef](#baseconfigurationitemtypedef)
  - [BatchGetAggregateResourceConfigResponseTypeDef](#batchgetaggregateresourceconfigresponsetypedef)
  - [BatchGetResourceConfigResponseTypeDef](#batchgetresourceconfigresponsetypedef)
  - [ComplianceByConfigRuleTypeDef](#compliancebyconfigruletypedef)
  - [ComplianceByResourceTypeDef](#compliancebyresourcetypedef)
  - [ComplianceContributorCountTypeDef](#compliancecontributorcounttypedef)
  - [ComplianceSummaryByResourceTypeTypeDef](#compliancesummarybyresourcetypetypedef)
  - [ComplianceSummaryTypeDef](#compliancesummarytypedef)
  - [ComplianceTypeDef](#compliancetypedef)
  - [ConfigExportDeliveryInfoTypeDef](#configexportdeliveryinfotypedef)
  - [ConfigRuleComplianceFiltersTypeDef](#configrulecompliancefilterstypedef)
  - [ConfigRuleComplianceSummaryFiltersTypeDef](#configrulecompliancesummaryfilterstypedef)
  - [ConfigRuleEvaluationStatusTypeDef](#configruleevaluationstatustypedef)
  - [ConfigRuleTypeDef](#configruletypedef)
  - [ConfigSnapshotDeliveryPropertiesTypeDef](#configsnapshotdeliverypropertiestypedef)
  - [ConfigStreamDeliveryInfoTypeDef](#configstreamdeliveryinfotypedef)
  - [ConfigurationAggregatorTypeDef](#configurationaggregatortypedef)
  - [ConfigurationItemTypeDef](#configurationitemtypedef)
  - [ConfigurationRecorderStatusTypeDef](#configurationrecorderstatustypedef)
  - [ConfigurationRecorderTypeDef](#configurationrecordertypedef)
  - [ConformancePackComplianceFiltersTypeDef](#conformancepackcompliancefilterstypedef)
  - [ConformancePackComplianceSummaryTypeDef](#conformancepackcompliancesummarytypedef)
  - [ConformancePackDetailTypeDef](#conformancepackdetailtypedef)
  - [ConformancePackEvaluationFiltersTypeDef](#conformancepackevaluationfilterstypedef)
  - [ConformancePackEvaluationResultTypeDef](#conformancepackevaluationresulttypedef)
  - [ConformancePackInputParameterTypeDef](#conformancepackinputparametertypedef)
  - [ConformancePackRuleComplianceTypeDef](#conformancepackrulecompliancetypedef)
  - [ConformancePackStatusDetailTypeDef](#conformancepackstatusdetailtypedef)
  - [DeleteRemediationExceptionsResponseTypeDef](#deleteremediationexceptionsresponsetypedef)
  - [DeliverConfigSnapshotResponseTypeDef](#deliverconfigsnapshotresponsetypedef)
  - [DeliveryChannelStatusTypeDef](#deliverychannelstatustypedef)
  - [DeliveryChannelTypeDef](#deliverychanneltypedef)
  - [DescribeAggregateComplianceByConfigRulesResponseTypeDef](#describeaggregatecompliancebyconfigrulesresponsetypedef)
  - [DescribeAggregateComplianceByConformancePacksResponseTypeDef](#describeaggregatecompliancebyconformancepacksresponsetypedef)
  - [DescribeAggregationAuthorizationsResponseTypeDef](#describeaggregationauthorizationsresponsetypedef)
  - [DescribeComplianceByConfigRuleResponseTypeDef](#describecompliancebyconfigruleresponsetypedef)
  - [DescribeComplianceByResourceResponseTypeDef](#describecompliancebyresourceresponsetypedef)
  - [DescribeConfigRuleEvaluationStatusResponseTypeDef](#describeconfigruleevaluationstatusresponsetypedef)
  - [DescribeConfigRulesResponseTypeDef](#describeconfigrulesresponsetypedef)
  - [DescribeConfigurationAggregatorSourcesStatusResponseTypeDef](#describeconfigurationaggregatorsourcesstatusresponsetypedef)
  - [DescribeConfigurationAggregatorsResponseTypeDef](#describeconfigurationaggregatorsresponsetypedef)
  - [DescribeConfigurationRecorderStatusResponseTypeDef](#describeconfigurationrecorderstatusresponsetypedef)
  - [DescribeConfigurationRecordersResponseTypeDef](#describeconfigurationrecordersresponsetypedef)
  - [DescribeConformancePackComplianceResponseTypeDef](#describeconformancepackcomplianceresponsetypedef)
  - [DescribeConformancePackStatusResponseTypeDef](#describeconformancepackstatusresponsetypedef)
  - [DescribeConformancePacksResponseTypeDef](#describeconformancepacksresponsetypedef)
  - [DescribeDeliveryChannelStatusResponseTypeDef](#describedeliverychannelstatusresponsetypedef)
  - [DescribeDeliveryChannelsResponseTypeDef](#describedeliverychannelsresponsetypedef)
  - [DescribeOrganizationConfigRuleStatusesResponseTypeDef](#describeorganizationconfigrulestatusesresponsetypedef)
  - [DescribeOrganizationConfigRulesResponseTypeDef](#describeorganizationconfigrulesresponsetypedef)
  - [DescribeOrganizationConformancePackStatusesResponseTypeDef](#describeorganizationconformancepackstatusesresponsetypedef)
  - [DescribeOrganizationConformancePacksResponseTypeDef](#describeorganizationconformancepacksresponsetypedef)
  - [DescribePendingAggregationRequestsResponseTypeDef](#describependingaggregationrequestsresponsetypedef)
  - [DescribeRemediationConfigurationsResponseTypeDef](#describeremediationconfigurationsresponsetypedef)
  - [DescribeRemediationExceptionsResponseTypeDef](#describeremediationexceptionsresponsetypedef)
  - [DescribeRemediationExecutionStatusResponseTypeDef](#describeremediationexecutionstatusresponsetypedef)
  - [DescribeRetentionConfigurationsResponseTypeDef](#describeretentionconfigurationsresponsetypedef)
  - [EvaluationResultIdentifierTypeDef](#evaluationresultidentifiertypedef)
  - [EvaluationResultQualifierTypeDef](#evaluationresultqualifiertypedef)
  - [EvaluationResultTypeDef](#evaluationresulttypedef)
  - [EvaluationTypeDef](#evaluationtypedef)
  - [ExecutionControlsTypeDef](#executioncontrolstypedef)
  - [ExternalEvaluationTypeDef](#externalevaluationtypedef)
  - [FailedDeleteRemediationExceptionsBatchTypeDef](#faileddeleteremediationexceptionsbatchtypedef)
  - [FailedRemediationBatchTypeDef](#failedremediationbatchtypedef)
  - [FailedRemediationExceptionBatchTypeDef](#failedremediationexceptionbatchtypedef)
  - [FieldInfoTypeDef](#fieldinfotypedef)
  - [GetAggregateComplianceDetailsByConfigRuleResponseTypeDef](#getaggregatecompliancedetailsbyconfigruleresponsetypedef)
  - [GetAggregateConfigRuleComplianceSummaryResponseTypeDef](#getaggregateconfigrulecompliancesummaryresponsetypedef)
  - [GetAggregateConformancePackComplianceSummaryResponseTypeDef](#getaggregateconformancepackcompliancesummaryresponsetypedef)
  - [GetAggregateDiscoveredResourceCountsResponseTypeDef](#getaggregatediscoveredresourcecountsresponsetypedef)
  - [GetAggregateResourceConfigResponseTypeDef](#getaggregateresourceconfigresponsetypedef)
  - [GetComplianceDetailsByConfigRuleResponseTypeDef](#getcompliancedetailsbyconfigruleresponsetypedef)
  - [GetComplianceDetailsByResourceResponseTypeDef](#getcompliancedetailsbyresourceresponsetypedef)
  - [GetComplianceSummaryByConfigRuleResponseTypeDef](#getcompliancesummarybyconfigruleresponsetypedef)
  - [GetComplianceSummaryByResourceTypeResponseTypeDef](#getcompliancesummarybyresourcetyperesponsetypedef)
  - [GetConformancePackComplianceDetailsResponseTypeDef](#getconformancepackcompliancedetailsresponsetypedef)
  - [GetConformancePackComplianceSummaryResponseTypeDef](#getconformancepackcompliancesummaryresponsetypedef)
  - [GetDiscoveredResourceCountsResponseTypeDef](#getdiscoveredresourcecountsresponsetypedef)
  - [GetOrganizationConfigRuleDetailedStatusResponseTypeDef](#getorganizationconfigruledetailedstatusresponsetypedef)
  - [GetOrganizationConformancePackDetailedStatusResponseTypeDef](#getorganizationconformancepackdetailedstatusresponsetypedef)
  - [GetResourceConfigHistoryResponseTypeDef](#getresourceconfighistoryresponsetypedef)
  - [GetStoredQueryResponseTypeDef](#getstoredqueryresponsetypedef)
  - [GroupedResourceCountTypeDef](#groupedresourcecounttypedef)
  - [ListAggregateDiscoveredResourcesResponseTypeDef](#listaggregatediscoveredresourcesresponsetypedef)
  - [ListDiscoveredResourcesResponseTypeDef](#listdiscoveredresourcesresponsetypedef)
  - [ListStoredQueriesResponseTypeDef](#liststoredqueriesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MemberAccountStatusTypeDef](#memberaccountstatustypedef)
  - [OrganizationAggregationSourceTypeDef](#organizationaggregationsourcetypedef)
  - [OrganizationConfigRuleStatusTypeDef](#organizationconfigrulestatustypedef)
  - [OrganizationConfigRuleTypeDef](#organizationconfigruletypedef)
  - [OrganizationConformancePackDetailedStatusTypeDef](#organizationconformancepackdetailedstatustypedef)
  - [OrganizationConformancePackStatusTypeDef](#organizationconformancepackstatustypedef)
  - [OrganizationConformancePackTypeDef](#organizationconformancepacktypedef)
  - [OrganizationCustomRuleMetadataTypeDef](#organizationcustomrulemetadatatypedef)
  - [OrganizationManagedRuleMetadataTypeDef](#organizationmanagedrulemetadatatypedef)
  - [OrganizationResourceDetailedStatusFiltersTypeDef](#organizationresourcedetailedstatusfilterstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PendingAggregationRequestTypeDef](#pendingaggregationrequesttypedef)
  - [PutAggregationAuthorizationResponseTypeDef](#putaggregationauthorizationresponsetypedef)
  - [PutConfigurationAggregatorResponseTypeDef](#putconfigurationaggregatorresponsetypedef)
  - [PutConformancePackResponseTypeDef](#putconformancepackresponsetypedef)
  - [PutEvaluationsResponseTypeDef](#putevaluationsresponsetypedef)
  - [PutOrganizationConfigRuleResponseTypeDef](#putorganizationconfigruleresponsetypedef)
  - [PutOrganizationConformancePackResponseTypeDef](#putorganizationconformancepackresponsetypedef)
  - [PutRemediationConfigurationsResponseTypeDef](#putremediationconfigurationsresponsetypedef)
  - [PutRemediationExceptionsResponseTypeDef](#putremediationexceptionsresponsetypedef)
  - [PutRetentionConfigurationResponseTypeDef](#putretentionconfigurationresponsetypedef)
  - [PutStoredQueryResponseTypeDef](#putstoredqueryresponsetypedef)
  - [QueryInfoTypeDef](#queryinfotypedef)
  - [RecordingGroupTypeDef](#recordinggrouptypedef)
  - [RelationshipTypeDef](#relationshiptypedef)
  - [RemediationConfigurationTypeDef](#remediationconfigurationtypedef)
  - [RemediationExceptionResourceKeyTypeDef](#remediationexceptionresourcekeytypedef)
  - [RemediationExceptionTypeDef](#remediationexceptiontypedef)
  - [RemediationExecutionStatusTypeDef](#remediationexecutionstatustypedef)
  - [RemediationExecutionStepTypeDef](#remediationexecutionsteptypedef)
  - [RemediationParameterValueTypeDef](#remediationparametervaluetypedef)
  - [ResourceCountFiltersTypeDef](#resourcecountfilterstypedef)
  - [ResourceCountTypeDef](#resourcecounttypedef)
  - [ResourceFiltersTypeDef](#resourcefilterstypedef)
  - [ResourceIdentifierTypeDef](#resourceidentifiertypedef)
  - [ResourceKeyTypeDef](#resourcekeytypedef)
  - [ResourceValueTypeDef](#resourcevaluetypedef)
  - [RetentionConfigurationTypeDef](#retentionconfigurationtypedef)
  - [ScopeTypeDef](#scopetypedef)
  - [SelectAggregateResourceConfigResponseTypeDef](#selectaggregateresourceconfigresponsetypedef)
  - [SelectResourceConfigResponseTypeDef](#selectresourceconfigresponsetypedef)
  - [SourceDetailTypeDef](#sourcedetailtypedef)
  - [SourceTypeDef](#sourcetypedef)
  - [SsmControlsTypeDef](#ssmcontrolstypedef)
  - [StartRemediationExecutionResponseTypeDef](#startremediationexecutionresponsetypedef)
  - [StaticValueTypeDef](#staticvaluetypedef)
  - [StatusDetailFiltersTypeDef](#statusdetailfilterstypedef)
  - [StoredQueryMetadataTypeDef](#storedquerymetadatatypedef)
  - [StoredQueryTypeDef](#storedquerytypedef)
  - [TagTypeDef](#tagtypedef)

## AccountAggregationSourceTypeDef

```python
from mypy_boto3_config.type_defs import AccountAggregationSourceTypeDef
```


Required fields:
- `AccountIds`: `List[str]`



Optional fields:
- `AllAwsRegions`: `bool`
- `AwsRegions`: `List[str]`


## AggregateComplianceByConfigRuleTypeDef

```python
from mypy_boto3_config.type_defs import AggregateComplianceByConfigRuleTypeDef
```




Optional fields:
- `ConfigRuleName`: `str`
- `Compliance`: `"ComplianceTypeDef"`
- `AccountId`: `str`
- `AwsRegion`: `str`


## AggregateComplianceByConformancePackTypeDef

```python
from mypy_boto3_config.type_defs import AggregateComplianceByConformancePackTypeDef
```




Optional fields:
- `ConformancePackName`: `str`
- `Compliance`: `"AggregateConformancePackComplianceTypeDef"`
- `AccountId`: `str`
- `AwsRegion`: `str`


## AggregateComplianceCountTypeDef

```python
from mypy_boto3_config.type_defs import AggregateComplianceCountTypeDef
```




Optional fields:
- `GroupName`: `str`
- `ComplianceSummary`: `"ComplianceSummaryTypeDef"`


## AggregateConformancePackComplianceCountTypeDef

```python
from mypy_boto3_config.type_defs import AggregateConformancePackComplianceCountTypeDef
```




Optional fields:
- `CompliantConformancePackCount`: `int`
- `NonCompliantConformancePackCount`: `int`


## AggregateConformancePackComplianceFiltersTypeDef

```python
from mypy_boto3_config.type_defs import AggregateConformancePackComplianceFiltersTypeDef
```




Optional fields:
- `ConformancePackName`: `str`
- `ComplianceType`: `ConformancePackComplianceType`
- `AccountId`: `str`
- `AwsRegion`: `str`


## AggregateConformancePackComplianceSummaryFiltersTypeDef

```python
from mypy_boto3_config.type_defs import AggregateConformancePackComplianceSummaryFiltersTypeDef
```




Optional fields:
- `AccountId`: `str`
- `AwsRegion`: `str`


## AggregateConformancePackComplianceSummaryTypeDef

```python
from mypy_boto3_config.type_defs import AggregateConformancePackComplianceSummaryTypeDef
```




Optional fields:
- `ComplianceSummary`: `"AggregateConformancePackComplianceCountTypeDef"`
- `GroupName`: `str`


## AggregateConformancePackComplianceTypeDef

```python
from mypy_boto3_config.type_defs import AggregateConformancePackComplianceTypeDef
```




Optional fields:
- `ComplianceType`: `ConformancePackComplianceType`
- `CompliantRuleCount`: `int`
- `NonCompliantRuleCount`: `int`
- `TotalRuleCount`: `int`


## AggregateEvaluationResultTypeDef

```python
from mypy_boto3_config.type_defs import AggregateEvaluationResultTypeDef
```




Optional fields:
- `EvaluationResultIdentifier`: `"EvaluationResultIdentifierTypeDef"`
- `ComplianceType`: `ComplianceType`
- `ResultRecordedTime`: `datetime`
- `ConfigRuleInvokedTime`: `datetime`
- `Annotation`: `str`
- `AccountId`: `str`
- `AwsRegion`: `str`


## AggregateResourceIdentifierTypeDef

```python
from mypy_boto3_config.type_defs import AggregateResourceIdentifierTypeDef
```


Required fields:
- `SourceAccountId`: `str`
- `SourceRegion`: `str`
- `ResourceId`: `str`
- `ResourceType`: `ResourceType`



Optional fields:
- `ResourceName`: `str`


## AggregatedSourceStatusTypeDef

```python
from mypy_boto3_config.type_defs import AggregatedSourceStatusTypeDef
```




Optional fields:
- `SourceId`: `str`
- `SourceType`: `AggregatedSourceType`
- `AwsRegion`: `str`
- `LastUpdateStatus`: `AggregatedSourceStatusType`
- `LastUpdateTime`: `datetime`
- `LastErrorCode`: `str`
- `LastErrorMessage`: `str`


## AggregationAuthorizationTypeDef

```python
from mypy_boto3_config.type_defs import AggregationAuthorizationTypeDef
```




Optional fields:
- `AggregationAuthorizationArn`: `str`
- `AuthorizedAccountId`: `str`
- `AuthorizedAwsRegion`: `str`
- `CreationTime`: `datetime`


## BaseConfigurationItemTypeDef

```python
from mypy_boto3_config.type_defs import BaseConfigurationItemTypeDef
```




Optional fields:
- `version`: `str`
- `accountId`: `str`
- `configurationItemCaptureTime`: `datetime`
- `configurationItemStatus`: `ConfigurationItemStatus`
- `configurationStateId`: `str`
- `arn`: `str`
- `resourceType`: `ResourceType`
- `resourceId`: `str`
- `resourceName`: `str`
- `awsRegion`: `str`
- `availabilityZone`: `str`
- `resourceCreationTime`: `datetime`
- `configuration`: `str`
- `supplementaryConfiguration`: `Dict[str, str]`


## BatchGetAggregateResourceConfigResponseTypeDef

```python
from mypy_boto3_config.type_defs import BatchGetAggregateResourceConfigResponseTypeDef
```




Optional fields:
- `BaseConfigurationItems`: `List["BaseConfigurationItemTypeDef"]`
- `UnprocessedResourceIdentifiers`: `List["AggregateResourceIdentifierTypeDef"]`


## BatchGetResourceConfigResponseTypeDef

```python
from mypy_boto3_config.type_defs import BatchGetResourceConfigResponseTypeDef
```




Optional fields:
- `baseConfigurationItems`: `List["BaseConfigurationItemTypeDef"]`
- `unprocessedResourceKeys`: `List["ResourceKeyTypeDef"]`


## ComplianceByConfigRuleTypeDef

```python
from mypy_boto3_config.type_defs import ComplianceByConfigRuleTypeDef
```




Optional fields:
- `ConfigRuleName`: `str`
- `Compliance`: `"ComplianceTypeDef"`


## ComplianceByResourceTypeDef

```python
from mypy_boto3_config.type_defs import ComplianceByResourceTypeDef
```




Optional fields:
- `ResourceType`: `str`
- `ResourceId`: `str`
- `Compliance`: `"ComplianceTypeDef"`


## ComplianceContributorCountTypeDef

```python
from mypy_boto3_config.type_defs import ComplianceContributorCountTypeDef
```




Optional fields:
- `CappedCount`: `int`
- `CapExceeded`: `bool`


## ComplianceSummaryByResourceTypeTypeDef

```python
from mypy_boto3_config.type_defs import ComplianceSummaryByResourceTypeTypeDef
```




Optional fields:
- `ResourceType`: `str`
- `ComplianceSummary`: `"ComplianceSummaryTypeDef"`


## ComplianceSummaryTypeDef

```python
from mypy_boto3_config.type_defs import ComplianceSummaryTypeDef
```




Optional fields:
- `CompliantResourceCount`: `"ComplianceContributorCountTypeDef"`
- `NonCompliantResourceCount`: `"ComplianceContributorCountTypeDef"`
- `ComplianceSummaryTimestamp`: `datetime`


## ComplianceTypeDef

```python
from mypy_boto3_config.type_defs import ComplianceTypeDef
```




Optional fields:
- `ComplianceType`: `ComplianceType`
- `ComplianceContributorCount`: `"ComplianceContributorCountTypeDef"`


## ConfigExportDeliveryInfoTypeDef

```python
from mypy_boto3_config.type_defs import ConfigExportDeliveryInfoTypeDef
```




Optional fields:
- `lastStatus`: `DeliveryStatus`
- `lastErrorCode`: `str`
- `lastErrorMessage`: `str`
- `lastAttemptTime`: `datetime`
- `lastSuccessfulTime`: `datetime`
- `nextDeliveryTime`: `datetime`


## ConfigRuleComplianceFiltersTypeDef

```python
from mypy_boto3_config.type_defs import ConfigRuleComplianceFiltersTypeDef
```




Optional fields:
- `ConfigRuleName`: `str`
- `ComplianceType`: `ComplianceType`
- `AccountId`: `str`
- `AwsRegion`: `str`


## ConfigRuleComplianceSummaryFiltersTypeDef

```python
from mypy_boto3_config.type_defs import ConfigRuleComplianceSummaryFiltersTypeDef
```




Optional fields:
- `AccountId`: `str`
- `AwsRegion`: `str`


## ConfigRuleEvaluationStatusTypeDef

```python
from mypy_boto3_config.type_defs import ConfigRuleEvaluationStatusTypeDef
```




Optional fields:
- `ConfigRuleName`: `str`
- `ConfigRuleArn`: `str`
- `ConfigRuleId`: `str`
- `LastSuccessfulInvocationTime`: `datetime`
- `LastFailedInvocationTime`: `datetime`
- `LastSuccessfulEvaluationTime`: `datetime`
- `LastFailedEvaluationTime`: `datetime`
- `FirstActivatedTime`: `datetime`
- `LastDeactivatedTime`: `datetime`
- `LastErrorCode`: `str`
- `LastErrorMessage`: `str`
- `FirstEvaluationStarted`: `bool`


## ConfigRuleTypeDef

```python
from mypy_boto3_config.type_defs import ConfigRuleTypeDef
```


Required fields:
- `Source`: `"SourceTypeDef"`



Optional fields:
- `ConfigRuleName`: `str`
- `ConfigRuleArn`: `str`
- `ConfigRuleId`: `str`
- `Description`: `str`
- `Scope`: `"ScopeTypeDef"`
- `InputParameters`: `str`
- `MaximumExecutionFrequency`: `MaximumExecutionFrequency`
- `ConfigRuleState`: `ConfigRuleState`
- `CreatedBy`: `str`


## ConfigSnapshotDeliveryPropertiesTypeDef

```python
from mypy_boto3_config.type_defs import ConfigSnapshotDeliveryPropertiesTypeDef
```




Optional fields:
- `deliveryFrequency`: `MaximumExecutionFrequency`


## ConfigStreamDeliveryInfoTypeDef

```python
from mypy_boto3_config.type_defs import ConfigStreamDeliveryInfoTypeDef
```




Optional fields:
- `lastStatus`: `DeliveryStatus`
- `lastErrorCode`: `str`
- `lastErrorMessage`: `str`
- `lastStatusChangeTime`: `datetime`


## ConfigurationAggregatorTypeDef

```python
from mypy_boto3_config.type_defs import ConfigurationAggregatorTypeDef
```




Optional fields:
- `ConfigurationAggregatorName`: `str`
- `ConfigurationAggregatorArn`: `str`
- `AccountAggregationSources`: `List["AccountAggregationSourceTypeDef"]`
- `OrganizationAggregationSource`: `"OrganizationAggregationSourceTypeDef"`
- `CreationTime`: `datetime`
- `LastUpdatedTime`: `datetime`
- `CreatedBy`: `str`


## ConfigurationItemTypeDef

```python
from mypy_boto3_config.type_defs import ConfigurationItemTypeDef
```




Optional fields:
- `version`: `str`
- `accountId`: `str`
- `configurationItemCaptureTime`: `datetime`
- `configurationItemStatus`: `ConfigurationItemStatus`
- `configurationStateId`: `str`
- `configurationItemMD5Hash`: `str`
- `arn`: `str`
- `resourceType`: `ResourceType`
- `resourceId`: `str`
- `resourceName`: `str`
- `awsRegion`: `str`
- `availabilityZone`: `str`
- `resourceCreationTime`: `datetime`
- `tags`: `Dict[str, str]`
- `relatedEvents`: `List[str]`
- `relationships`: `List["RelationshipTypeDef"]`
- `configuration`: `str`
- `supplementaryConfiguration`: `Dict[str, str]`


## ConfigurationRecorderStatusTypeDef

```python
from mypy_boto3_config.type_defs import ConfigurationRecorderStatusTypeDef
```




Optional fields:
- `name`: `str`
- `lastStartTime`: `datetime`
- `lastStopTime`: `datetime`
- `recording`: `bool`
- `lastStatus`: `RecorderStatus`
- `lastErrorCode`: `str`
- `lastErrorMessage`: `str`
- `lastStatusChangeTime`: `datetime`


## ConfigurationRecorderTypeDef

```python
from mypy_boto3_config.type_defs import ConfigurationRecorderTypeDef
```




Optional fields:
- `name`: `str`
- `roleARN`: `str`
- `recordingGroup`: `"RecordingGroupTypeDef"`


## ConformancePackComplianceFiltersTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackComplianceFiltersTypeDef
```




Optional fields:
- `ConfigRuleNames`: `List[str]`
- `ComplianceType`: `ConformancePackComplianceType`


## ConformancePackComplianceSummaryTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackComplianceSummaryTypeDef
```


Required fields:
- `ConformancePackName`: `str`
- `ConformancePackComplianceStatus`: `ConformancePackComplianceType`




## ConformancePackDetailTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackDetailTypeDef
```


Required fields:
- `ConformancePackName`: `str`
- `ConformancePackArn`: `str`
- `ConformancePackId`: `str`



Optional fields:
- `DeliveryS3Bucket`: `str`
- `DeliveryS3KeyPrefix`: `str`
- `ConformancePackInputParameters`: `List["ConformancePackInputParameterTypeDef"]`
- `LastUpdateRequestedTime`: `datetime`
- `CreatedBy`: `str`


## ConformancePackEvaluationFiltersTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackEvaluationFiltersTypeDef
```




Optional fields:
- `ConfigRuleNames`: `List[str]`
- `ComplianceType`: `ConformancePackComplianceType`
- `ResourceType`: `str`
- `ResourceIds`: `List[str]`


## ConformancePackEvaluationResultTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackEvaluationResultTypeDef
```


Required fields:
- `ComplianceType`: `ConformancePackComplianceType`
- `EvaluationResultIdentifier`: `"EvaluationResultIdentifierTypeDef"`
- `ConfigRuleInvokedTime`: `datetime`
- `ResultRecordedTime`: `datetime`



Optional fields:
- `Annotation`: `str`


## ConformancePackInputParameterTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackInputParameterTypeDef
```


Required fields:
- `ParameterName`: `str`
- `ParameterValue`: `str`




## ConformancePackRuleComplianceTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackRuleComplianceTypeDef
```




Optional fields:
- `ConfigRuleName`: `str`
- `ComplianceType`: `ConformancePackComplianceType`
- `Controls`: `List[str]`


## ConformancePackStatusDetailTypeDef

```python
from mypy_boto3_config.type_defs import ConformancePackStatusDetailTypeDef
```


Required fields:
- `ConformancePackName`: `str`
- `ConformancePackId`: `str`
- `ConformancePackArn`: `str`
- `ConformancePackState`: `ConformancePackState`
- `StackArn`: `str`
- `LastUpdateRequestedTime`: `datetime`



Optional fields:
- `ConformancePackStatusReason`: `str`
- `LastUpdateCompletedTime`: `datetime`


## DeleteRemediationExceptionsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DeleteRemediationExceptionsResponseTypeDef
```




Optional fields:
- `FailedBatches`: `List["FailedDeleteRemediationExceptionsBatchTypeDef"]`


## DeliverConfigSnapshotResponseTypeDef

```python
from mypy_boto3_config.type_defs import DeliverConfigSnapshotResponseTypeDef
```




Optional fields:
- `configSnapshotId`: `str`


## DeliveryChannelStatusTypeDef

```python
from mypy_boto3_config.type_defs import DeliveryChannelStatusTypeDef
```




Optional fields:
- `name`: `str`
- `configSnapshotDeliveryInfo`: `"ConfigExportDeliveryInfoTypeDef"`
- `configHistoryDeliveryInfo`: `"ConfigExportDeliveryInfoTypeDef"`
- `configStreamDeliveryInfo`: `"ConfigStreamDeliveryInfoTypeDef"`


## DeliveryChannelTypeDef

```python
from mypy_boto3_config.type_defs import DeliveryChannelTypeDef
```




Optional fields:
- `name`: `str`
- `s3BucketName`: `str`
- `s3KeyPrefix`: `str`
- `s3KmsKeyArn`: `str`
- `snsTopicARN`: `str`
- `configSnapshotDeliveryProperties`: `"ConfigSnapshotDeliveryPropertiesTypeDef"`


## DescribeAggregateComplianceByConfigRulesResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeAggregateComplianceByConfigRulesResponseTypeDef
```




Optional fields:
- `AggregateComplianceByConfigRules`: `List["AggregateComplianceByConfigRuleTypeDef"]`
- `NextToken`: `str`


## DescribeAggregateComplianceByConformancePacksResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeAggregateComplianceByConformancePacksResponseTypeDef
```




Optional fields:
- `AggregateComplianceByConformancePacks`: `List["AggregateComplianceByConformancePackTypeDef"]`
- `NextToken`: `str`


## DescribeAggregationAuthorizationsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeAggregationAuthorizationsResponseTypeDef
```




Optional fields:
- `AggregationAuthorizations`: `List["AggregationAuthorizationTypeDef"]`
- `NextToken`: `str`


## DescribeComplianceByConfigRuleResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeComplianceByConfigRuleResponseTypeDef
```




Optional fields:
- `ComplianceByConfigRules`: `List["ComplianceByConfigRuleTypeDef"]`
- `NextToken`: `str`


## DescribeComplianceByResourceResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeComplianceByResourceResponseTypeDef
```




Optional fields:
- `ComplianceByResources`: `List["ComplianceByResourceTypeDef"]`
- `NextToken`: `str`


## DescribeConfigRuleEvaluationStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConfigRuleEvaluationStatusResponseTypeDef
```




Optional fields:
- `ConfigRulesEvaluationStatus`: `List["ConfigRuleEvaluationStatusTypeDef"]`
- `NextToken`: `str`


## DescribeConfigRulesResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConfigRulesResponseTypeDef
```




Optional fields:
- `ConfigRules`: `List["ConfigRuleTypeDef"]`
- `NextToken`: `str`


## DescribeConfigurationAggregatorSourcesStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConfigurationAggregatorSourcesStatusResponseTypeDef
```




Optional fields:
- `AggregatedSourceStatusList`: `List["AggregatedSourceStatusTypeDef"]`
- `NextToken`: `str`


## DescribeConfigurationAggregatorsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConfigurationAggregatorsResponseTypeDef
```




Optional fields:
- `ConfigurationAggregators`: `List["ConfigurationAggregatorTypeDef"]`
- `NextToken`: `str`


## DescribeConfigurationRecorderStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConfigurationRecorderStatusResponseTypeDef
```




Optional fields:
- `ConfigurationRecordersStatus`: `List["ConfigurationRecorderStatusTypeDef"]`


## DescribeConfigurationRecordersResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConfigurationRecordersResponseTypeDef
```




Optional fields:
- `ConfigurationRecorders`: `List["ConfigurationRecorderTypeDef"]`


## DescribeConformancePackComplianceResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConformancePackComplianceResponseTypeDef
```


Required fields:
- `ConformancePackName`: `str`
- `ConformancePackRuleComplianceList`: `List["ConformancePackRuleComplianceTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeConformancePackStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConformancePackStatusResponseTypeDef
```




Optional fields:
- `ConformancePackStatusDetails`: `List["ConformancePackStatusDetailTypeDef"]`
- `NextToken`: `str`


## DescribeConformancePacksResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeConformancePacksResponseTypeDef
```




Optional fields:
- `ConformancePackDetails`: `List["ConformancePackDetailTypeDef"]`
- `NextToken`: `str`


## DescribeDeliveryChannelStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeDeliveryChannelStatusResponseTypeDef
```




Optional fields:
- `DeliveryChannelsStatus`: `List["DeliveryChannelStatusTypeDef"]`


## DescribeDeliveryChannelsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeDeliveryChannelsResponseTypeDef
```




Optional fields:
- `DeliveryChannels`: `List["DeliveryChannelTypeDef"]`


## DescribeOrganizationConfigRuleStatusesResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeOrganizationConfigRuleStatusesResponseTypeDef
```




Optional fields:
- `OrganizationConfigRuleStatuses`: `List["OrganizationConfigRuleStatusTypeDef"]`
- `NextToken`: `str`


## DescribeOrganizationConfigRulesResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeOrganizationConfigRulesResponseTypeDef
```




Optional fields:
- `OrganizationConfigRules`: `List["OrganizationConfigRuleTypeDef"]`
- `NextToken`: `str`


## DescribeOrganizationConformancePackStatusesResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeOrganizationConformancePackStatusesResponseTypeDef
```




Optional fields:
- `OrganizationConformancePackStatuses`: `List["OrganizationConformancePackStatusTypeDef"]`
- `NextToken`: `str`


## DescribeOrganizationConformancePacksResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeOrganizationConformancePacksResponseTypeDef
```




Optional fields:
- `OrganizationConformancePacks`: `List["OrganizationConformancePackTypeDef"]`
- `NextToken`: `str`


## DescribePendingAggregationRequestsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribePendingAggregationRequestsResponseTypeDef
```




Optional fields:
- `PendingAggregationRequests`: `List["PendingAggregationRequestTypeDef"]`
- `NextToken`: `str`


## DescribeRemediationConfigurationsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeRemediationConfigurationsResponseTypeDef
```




Optional fields:
- `RemediationConfigurations`: `List["RemediationConfigurationTypeDef"]`


## DescribeRemediationExceptionsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeRemediationExceptionsResponseTypeDef
```




Optional fields:
- `RemediationExceptions`: `List["RemediationExceptionTypeDef"]`
- `NextToken`: `str`


## DescribeRemediationExecutionStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeRemediationExecutionStatusResponseTypeDef
```




Optional fields:
- `RemediationExecutionStatuses`: `List["RemediationExecutionStatusTypeDef"]`
- `NextToken`: `str`


## DescribeRetentionConfigurationsResponseTypeDef

```python
from mypy_boto3_config.type_defs import DescribeRetentionConfigurationsResponseTypeDef
```




Optional fields:
- `RetentionConfigurations`: `List["RetentionConfigurationTypeDef"]`
- `NextToken`: `str`


## EvaluationResultIdentifierTypeDef

```python
from mypy_boto3_config.type_defs import EvaluationResultIdentifierTypeDef
```




Optional fields:
- `EvaluationResultQualifier`: `"EvaluationResultQualifierTypeDef"`
- `OrderingTimestamp`: `datetime`


## EvaluationResultQualifierTypeDef

```python
from mypy_boto3_config.type_defs import EvaluationResultQualifierTypeDef
```




Optional fields:
- `ConfigRuleName`: `str`
- `ResourceType`: `str`
- `ResourceId`: `str`


## EvaluationResultTypeDef

```python
from mypy_boto3_config.type_defs import EvaluationResultTypeDef
```




Optional fields:
- `EvaluationResultIdentifier`: `"EvaluationResultIdentifierTypeDef"`
- `ComplianceType`: `ComplianceType`
- `ResultRecordedTime`: `datetime`
- `ConfigRuleInvokedTime`: `datetime`
- `Annotation`: `str`
- `ResultToken`: `str`


## EvaluationTypeDef

```python
from mypy_boto3_config.type_defs import EvaluationTypeDef
```


Required fields:
- `ComplianceResourceType`: `str`
- `ComplianceResourceId`: `str`
- `ComplianceType`: `ComplianceType`
- `OrderingTimestamp`: `datetime`



Optional fields:
- `Annotation`: `str`


## ExecutionControlsTypeDef

```python
from mypy_boto3_config.type_defs import ExecutionControlsTypeDef
```




Optional fields:
- `SsmControls`: `"SsmControlsTypeDef"`


## ExternalEvaluationTypeDef

```python
from mypy_boto3_config.type_defs import ExternalEvaluationTypeDef
```


Required fields:
- `ComplianceResourceType`: `str`
- `ComplianceResourceId`: `str`
- `ComplianceType`: `ComplianceType`
- `OrderingTimestamp`: `datetime`



Optional fields:
- `Annotation`: `str`


## FailedDeleteRemediationExceptionsBatchTypeDef

```python
from mypy_boto3_config.type_defs import FailedDeleteRemediationExceptionsBatchTypeDef
```




Optional fields:
- `FailureMessage`: `str`
- `FailedItems`: `List["RemediationExceptionResourceKeyTypeDef"]`


## FailedRemediationBatchTypeDef

```python
from mypy_boto3_config.type_defs import FailedRemediationBatchTypeDef
```




Optional fields:
- `FailureMessage`: `str`
- `FailedItems`: `List["RemediationConfigurationTypeDef"]`


## FailedRemediationExceptionBatchTypeDef

```python
from mypy_boto3_config.type_defs import FailedRemediationExceptionBatchTypeDef
```




Optional fields:
- `FailureMessage`: `str`
- `FailedItems`: `List["RemediationExceptionTypeDef"]`


## FieldInfoTypeDef

```python
from mypy_boto3_config.type_defs import FieldInfoTypeDef
```




Optional fields:
- `Name`: `str`


## GetAggregateComplianceDetailsByConfigRuleResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetAggregateComplianceDetailsByConfigRuleResponseTypeDef
```




Optional fields:
- `AggregateEvaluationResults`: `List["AggregateEvaluationResultTypeDef"]`
- `NextToken`: `str`


## GetAggregateConfigRuleComplianceSummaryResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetAggregateConfigRuleComplianceSummaryResponseTypeDef
```




Optional fields:
- `GroupByKey`: `str`
- `AggregateComplianceCounts`: `List["AggregateComplianceCountTypeDef"]`
- `NextToken`: `str`


## GetAggregateConformancePackComplianceSummaryResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetAggregateConformancePackComplianceSummaryResponseTypeDef
```




Optional fields:
- `AggregateConformancePackComplianceSummaries`: `List["AggregateConformancePackComplianceSummaryTypeDef"]`
- `GroupByKey`: `str`
- `NextToken`: `str`


## GetAggregateDiscoveredResourceCountsResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetAggregateDiscoveredResourceCountsResponseTypeDef
```


Required fields:
- `TotalDiscoveredResources`: `int`



Optional fields:
- `GroupByKey`: `str`
- `GroupedResourceCounts`: `List["GroupedResourceCountTypeDef"]`
- `NextToken`: `str`


## GetAggregateResourceConfigResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetAggregateResourceConfigResponseTypeDef
```




Optional fields:
- `ConfigurationItem`: `"ConfigurationItemTypeDef"`


## GetComplianceDetailsByConfigRuleResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetComplianceDetailsByConfigRuleResponseTypeDef
```




Optional fields:
- `EvaluationResults`: `List["EvaluationResultTypeDef"]`
- `NextToken`: `str`


## GetComplianceDetailsByResourceResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetComplianceDetailsByResourceResponseTypeDef
```




Optional fields:
- `EvaluationResults`: `List["EvaluationResultTypeDef"]`
- `NextToken`: `str`


## GetComplianceSummaryByConfigRuleResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetComplianceSummaryByConfigRuleResponseTypeDef
```




Optional fields:
- `ComplianceSummary`: `"ComplianceSummaryTypeDef"`


## GetComplianceSummaryByResourceTypeResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetComplianceSummaryByResourceTypeResponseTypeDef
```




Optional fields:
- `ComplianceSummariesByResourceType`: `List["ComplianceSummaryByResourceTypeTypeDef"]`


## GetConformancePackComplianceDetailsResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetConformancePackComplianceDetailsResponseTypeDef
```


Required fields:
- `ConformancePackName`: `str`



Optional fields:
- `ConformancePackRuleEvaluationResults`: `List["ConformancePackEvaluationResultTypeDef"]`
- `NextToken`: `str`


## GetConformancePackComplianceSummaryResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetConformancePackComplianceSummaryResponseTypeDef
```




Optional fields:
- `ConformancePackComplianceSummaryList`: `List["ConformancePackComplianceSummaryTypeDef"]`
- `NextToken`: `str`


## GetDiscoveredResourceCountsResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetDiscoveredResourceCountsResponseTypeDef
```




Optional fields:
- `totalDiscoveredResources`: `int`
- `resourceCounts`: `List["ResourceCountTypeDef"]`
- `nextToken`: `str`


## GetOrganizationConfigRuleDetailedStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetOrganizationConfigRuleDetailedStatusResponseTypeDef
```




Optional fields:
- `OrganizationConfigRuleDetailedStatus`: `List["MemberAccountStatusTypeDef"]`
- `NextToken`: `str`


## GetOrganizationConformancePackDetailedStatusResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetOrganizationConformancePackDetailedStatusResponseTypeDef
```




Optional fields:
- `OrganizationConformancePackDetailedStatuses`: `List["OrganizationConformancePackDetailedStatusTypeDef"]`
- `NextToken`: `str`


## GetResourceConfigHistoryResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetResourceConfigHistoryResponseTypeDef
```




Optional fields:
- `configurationItems`: `List["ConfigurationItemTypeDef"]`
- `nextToken`: `str`


## GetStoredQueryResponseTypeDef

```python
from mypy_boto3_config.type_defs import GetStoredQueryResponseTypeDef
```




Optional fields:
- `StoredQuery`: `"StoredQueryTypeDef"`


## GroupedResourceCountTypeDef

```python
from mypy_boto3_config.type_defs import GroupedResourceCountTypeDef
```


Required fields:
- `GroupName`: `str`
- `ResourceCount`: `int`




## ListAggregateDiscoveredResourcesResponseTypeDef

```python
from mypy_boto3_config.type_defs import ListAggregateDiscoveredResourcesResponseTypeDef
```




Optional fields:
- `ResourceIdentifiers`: `List["AggregateResourceIdentifierTypeDef"]`
- `NextToken`: `str`


## ListDiscoveredResourcesResponseTypeDef

```python
from mypy_boto3_config.type_defs import ListDiscoveredResourcesResponseTypeDef
```




Optional fields:
- `resourceIdentifiers`: `List["ResourceIdentifierTypeDef"]`
- `nextToken`: `str`


## ListStoredQueriesResponseTypeDef

```python
from mypy_boto3_config.type_defs import ListStoredQueriesResponseTypeDef
```




Optional fields:
- `StoredQueryMetadata`: `List["StoredQueryMetadataTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_config.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## MemberAccountStatusTypeDef

```python
from mypy_boto3_config.type_defs import MemberAccountStatusTypeDef
```


Required fields:
- `AccountId`: `str`
- `ConfigRuleName`: `str`
- `MemberAccountRuleStatus`: `MemberAccountRuleStatus`



Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`
- `LastUpdateTime`: `datetime`


## OrganizationAggregationSourceTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationAggregationSourceTypeDef
```


Required fields:
- `RoleArn`: `str`



Optional fields:
- `AwsRegions`: `List[str]`
- `AllAwsRegions`: `bool`


## OrganizationConfigRuleStatusTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationConfigRuleStatusTypeDef
```


Required fields:
- `OrganizationConfigRuleName`: `str`
- `OrganizationRuleStatus`: `OrganizationRuleStatus`



Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`
- `LastUpdateTime`: `datetime`


## OrganizationConfigRuleTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationConfigRuleTypeDef
```


Required fields:
- `OrganizationConfigRuleName`: `str`
- `OrganizationConfigRuleArn`: `str`



Optional fields:
- `OrganizationManagedRuleMetadata`: `"OrganizationManagedRuleMetadataTypeDef"`
- `OrganizationCustomRuleMetadata`: `"OrganizationCustomRuleMetadataTypeDef"`
- `ExcludedAccounts`: `List[str]`
- `LastUpdateTime`: `datetime`


## OrganizationConformancePackDetailedStatusTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationConformancePackDetailedStatusTypeDef
```


Required fields:
- `AccountId`: `str`
- `ConformancePackName`: `str`
- `Status`: `OrganizationResourceDetailedStatus`



Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`
- `LastUpdateTime`: `datetime`


## OrganizationConformancePackStatusTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationConformancePackStatusTypeDef
```


Required fields:
- `OrganizationConformancePackName`: `str`
- `Status`: `OrganizationResourceStatus`



Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`
- `LastUpdateTime`: `datetime`


## OrganizationConformancePackTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationConformancePackTypeDef
```


Required fields:
- `OrganizationConformancePackName`: `str`
- `OrganizationConformancePackArn`: `str`
- `LastUpdateTime`: `datetime`



Optional fields:
- `DeliveryS3Bucket`: `str`
- `DeliveryS3KeyPrefix`: `str`
- `ConformancePackInputParameters`: `List["ConformancePackInputParameterTypeDef"]`
- `ExcludedAccounts`: `List[str]`


## OrganizationCustomRuleMetadataTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationCustomRuleMetadataTypeDef
```


Required fields:
- `LambdaFunctionArn`: `str`
- `OrganizationConfigRuleTriggerTypes`: `List[OrganizationConfigRuleTriggerType]`



Optional fields:
- `Description`: `str`
- `InputParameters`: `str`
- `MaximumExecutionFrequency`: `MaximumExecutionFrequency`
- `ResourceTypesScope`: `List[str]`
- `ResourceIdScope`: `str`
- `TagKeyScope`: `str`
- `TagValueScope`: `str`


## OrganizationManagedRuleMetadataTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationManagedRuleMetadataTypeDef
```


Required fields:
- `RuleIdentifier`: `str`



Optional fields:
- `Description`: `str`
- `InputParameters`: `str`
- `MaximumExecutionFrequency`: `MaximumExecutionFrequency`
- `ResourceTypesScope`: `List[str]`
- `ResourceIdScope`: `str`
- `TagKeyScope`: `str`
- `TagValueScope`: `str`


## OrganizationResourceDetailedStatusFiltersTypeDef

```python
from mypy_boto3_config.type_defs import OrganizationResourceDetailedStatusFiltersTypeDef
```




Optional fields:
- `AccountId`: `str`
- `Status`: `OrganizationResourceDetailedStatus`


## PaginatorConfigTypeDef

```python
from mypy_boto3_config.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PendingAggregationRequestTypeDef

```python
from mypy_boto3_config.type_defs import PendingAggregationRequestTypeDef
```




Optional fields:
- `RequesterAccountId`: `str`
- `RequesterAwsRegion`: `str`


## PutAggregationAuthorizationResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutAggregationAuthorizationResponseTypeDef
```




Optional fields:
- `AggregationAuthorization`: `"AggregationAuthorizationTypeDef"`


## PutConfigurationAggregatorResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutConfigurationAggregatorResponseTypeDef
```




Optional fields:
- `ConfigurationAggregator`: `"ConfigurationAggregatorTypeDef"`


## PutConformancePackResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutConformancePackResponseTypeDef
```




Optional fields:
- `ConformancePackArn`: `str`


## PutEvaluationsResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutEvaluationsResponseTypeDef
```




Optional fields:
- `FailedEvaluations`: `List["EvaluationTypeDef"]`


## PutOrganizationConfigRuleResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutOrganizationConfigRuleResponseTypeDef
```




Optional fields:
- `OrganizationConfigRuleArn`: `str`


## PutOrganizationConformancePackResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutOrganizationConformancePackResponseTypeDef
```




Optional fields:
- `OrganizationConformancePackArn`: `str`


## PutRemediationConfigurationsResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutRemediationConfigurationsResponseTypeDef
```




Optional fields:
- `FailedBatches`: `List["FailedRemediationBatchTypeDef"]`


## PutRemediationExceptionsResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutRemediationExceptionsResponseTypeDef
```




Optional fields:
- `FailedBatches`: `List["FailedRemediationExceptionBatchTypeDef"]`


## PutRetentionConfigurationResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutRetentionConfigurationResponseTypeDef
```




Optional fields:
- `RetentionConfiguration`: `"RetentionConfigurationTypeDef"`


## PutStoredQueryResponseTypeDef

```python
from mypy_boto3_config.type_defs import PutStoredQueryResponseTypeDef
```




Optional fields:
- `QueryArn`: `str`


## QueryInfoTypeDef

```python
from mypy_boto3_config.type_defs import QueryInfoTypeDef
```




Optional fields:
- `SelectFields`: `List["FieldInfoTypeDef"]`


## RecordingGroupTypeDef

```python
from mypy_boto3_config.type_defs import RecordingGroupTypeDef
```




Optional fields:
- `allSupported`: `bool`
- `includeGlobalResourceTypes`: `bool`
- `resourceTypes`: `List[ResourceType]`


## RelationshipTypeDef

```python
from mypy_boto3_config.type_defs import RelationshipTypeDef
```




Optional fields:
- `resourceType`: `ResourceType`
- `resourceId`: `str`
- `resourceName`: `str`
- `relationshipName`: `str`


## RemediationConfigurationTypeDef

```python
from mypy_boto3_config.type_defs import RemediationConfigurationTypeDef
```


Required fields:
- `ConfigRuleName`: `str`
- `TargetType`: `Literal['SSM_DOCUMENT']`
- `TargetId`: `str`



Optional fields:
- `TargetVersion`: `str`
- `Parameters`: `Dict[str, "RemediationParameterValueTypeDef"]`
- `ResourceType`: `str`
- `Automatic`: `bool`
- `ExecutionControls`: `"ExecutionControlsTypeDef"`
- `MaximumAutomaticAttempts`: `int`
- `RetryAttemptSeconds`: `int`
- `Arn`: `str`
- `CreatedByService`: `str`


## RemediationExceptionResourceKeyTypeDef

```python
from mypy_boto3_config.type_defs import RemediationExceptionResourceKeyTypeDef
```




Optional fields:
- `ResourceType`: `str`
- `ResourceId`: `str`


## RemediationExceptionTypeDef

```python
from mypy_boto3_config.type_defs import RemediationExceptionTypeDef
```


Required fields:
- `ConfigRuleName`: `str`
- `ResourceType`: `str`
- `ResourceId`: `str`



Optional fields:
- `Message`: `str`
- `ExpirationTime`: `datetime`


## RemediationExecutionStatusTypeDef

```python
from mypy_boto3_config.type_defs import RemediationExecutionStatusTypeDef
```




Optional fields:
- `ResourceKey`: `"ResourceKeyTypeDef"`
- `State`: `RemediationExecutionState`
- `StepDetails`: `List["RemediationExecutionStepTypeDef"]`
- `InvocationTime`: `datetime`
- `LastUpdatedTime`: `datetime`


## RemediationExecutionStepTypeDef

```python
from mypy_boto3_config.type_defs import RemediationExecutionStepTypeDef
```




Optional fields:
- `Name`: `str`
- `State`: `RemediationExecutionStepState`
- `ErrorMessage`: `str`
- `StartTime`: `datetime`
- `StopTime`: `datetime`


## RemediationParameterValueTypeDef

```python
from mypy_boto3_config.type_defs import RemediationParameterValueTypeDef
```




Optional fields:
- `ResourceValue`: `"ResourceValueTypeDef"`
- `StaticValue`: `"StaticValueTypeDef"`


## ResourceCountFiltersTypeDef

```python
from mypy_boto3_config.type_defs import ResourceCountFiltersTypeDef
```




Optional fields:
- `ResourceType`: `ResourceType`
- `AccountId`: `str`
- `Region`: `str`


## ResourceCountTypeDef

```python
from mypy_boto3_config.type_defs import ResourceCountTypeDef
```




Optional fields:
- `resourceType`: `ResourceType`
- `count`: `int`


## ResourceFiltersTypeDef

```python
from mypy_boto3_config.type_defs import ResourceFiltersTypeDef
```




Optional fields:
- `AccountId`: `str`
- `ResourceId`: `str`
- `ResourceName`: `str`
- `Region`: `str`


## ResourceIdentifierTypeDef

```python
from mypy_boto3_config.type_defs import ResourceIdentifierTypeDef
```




Optional fields:
- `resourceType`: `ResourceType`
- `resourceId`: `str`
- `resourceName`: `str`
- `resourceDeletionTime`: `datetime`


## ResourceKeyTypeDef

```python
from mypy_boto3_config.type_defs import ResourceKeyTypeDef
```


Required fields:
- `resourceType`: `ResourceType`
- `resourceId`: `str`




## ResourceValueTypeDef

```python
from mypy_boto3_config.type_defs import ResourceValueTypeDef
```


Required fields:
- `Value`: `Literal['RESOURCE_ID']`




## RetentionConfigurationTypeDef

```python
from mypy_boto3_config.type_defs import RetentionConfigurationTypeDef
```


Required fields:
- `Name`: `str`
- `RetentionPeriodInDays`: `int`




## ScopeTypeDef

```python
from mypy_boto3_config.type_defs import ScopeTypeDef
```




Optional fields:
- `ComplianceResourceTypes`: `List[str]`
- `TagKey`: `str`
- `TagValue`: `str`
- `ComplianceResourceId`: `str`


## SelectAggregateResourceConfigResponseTypeDef

```python
from mypy_boto3_config.type_defs import SelectAggregateResourceConfigResponseTypeDef
```




Optional fields:
- `Results`: `List[str]`
- `QueryInfo`: `"QueryInfoTypeDef"`
- `NextToken`: `str`


## SelectResourceConfigResponseTypeDef

```python
from mypy_boto3_config.type_defs import SelectResourceConfigResponseTypeDef
```




Optional fields:
- `Results`: `List[str]`
- `QueryInfo`: `"QueryInfoTypeDef"`
- `NextToken`: `str`


## SourceDetailTypeDef

```python
from mypy_boto3_config.type_defs import SourceDetailTypeDef
```




Optional fields:
- `EventSource`: `Literal['aws.config']`
- `MessageType`: `MessageType`
- `MaximumExecutionFrequency`: `MaximumExecutionFrequency`


## SourceTypeDef

```python
from mypy_boto3_config.type_defs import SourceTypeDef
```


Required fields:
- `Owner`: `Owner`
- `SourceIdentifier`: `str`



Optional fields:
- `SourceDetails`: `List["SourceDetailTypeDef"]`


## SsmControlsTypeDef

```python
from mypy_boto3_config.type_defs import SsmControlsTypeDef
```




Optional fields:
- `ConcurrentExecutionRatePercentage`: `int`
- `ErrorPercentage`: `int`


## StartRemediationExecutionResponseTypeDef

```python
from mypy_boto3_config.type_defs import StartRemediationExecutionResponseTypeDef
```




Optional fields:
- `FailureMessage`: `str`
- `FailedItems`: `List["ResourceKeyTypeDef"]`


## StaticValueTypeDef

```python
from mypy_boto3_config.type_defs import StaticValueTypeDef
```


Required fields:
- `Values`: `List[str]`




## StatusDetailFiltersTypeDef

```python
from mypy_boto3_config.type_defs import StatusDetailFiltersTypeDef
```




Optional fields:
- `AccountId`: `str`
- `MemberAccountRuleStatus`: `MemberAccountRuleStatus`


## StoredQueryMetadataTypeDef

```python
from mypy_boto3_config.type_defs import StoredQueryMetadataTypeDef
```


Required fields:
- `QueryId`: `str`
- `QueryArn`: `str`
- `QueryName`: `str`



Optional fields:
- `Description`: `str`


## StoredQueryTypeDef

```python
from mypy_boto3_config.type_defs import StoredQueryTypeDef
```


Required fields:
- `QueryName`: `str`



Optional fields:
- `QueryId`: `str`
- `QueryArn`: `str`
- `Description`: `str`
- `Expression`: `str`


## TagTypeDef

```python
from mypy_boto3_config.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`

