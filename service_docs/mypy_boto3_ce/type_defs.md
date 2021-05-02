# Structures for boto3 CostExplorer module

> [Index](../index.md) > [CostExplorer](./index.md) > Structures

Auto-generated documentation for [CostExplorer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer)
type annotations stubs module [mypy_boto3_ce](https://pypi.org/project/mypy-boto3-ce/).

- [Structures for boto3 CostExplorer module](#structures-for-boto3-costexplorer-module)
  - [AnomalyDateIntervalTypeDef](#anomalydateintervaltypedef)
  - [AnomalyMonitorTypeDef](#anomalymonitortypedef)
  - [AnomalyScoreTypeDef](#anomalyscoretypedef)
  - [AnomalySubscriptionTypeDef](#anomalysubscriptiontypedef)
  - [AnomalyTypeDef](#anomalytypedef)
  - [CostCategoryInheritedValueDimensionTypeDef](#costcategoryinheritedvaluedimensiontypedef)
  - [CostCategoryProcessingStatusTypeDef](#costcategoryprocessingstatustypedef)
  - [CostCategoryReferenceTypeDef](#costcategoryreferencetypedef)
  - [CostCategoryRuleTypeDef](#costcategoryruletypedef)
  - [CostCategoryTypeDef](#costcategorytypedef)
  - [CostCategoryValuesTypeDef](#costcategoryvaluestypedef)
  - [CoverageByTimeTypeDef](#coveragebytimetypedef)
  - [CoverageCostTypeDef](#coveragecosttypedef)
  - [CoverageHoursTypeDef](#coveragehourstypedef)
  - [CoverageNormalizedUnitsTypeDef](#coveragenormalizedunitstypedef)
  - [CoverageTypeDef](#coveragetypedef)
  - [CreateAnomalyMonitorResponseTypeDef](#createanomalymonitorresponsetypedef)
  - [CreateAnomalySubscriptionResponseTypeDef](#createanomalysubscriptionresponsetypedef)
  - [CreateCostCategoryDefinitionResponseTypeDef](#createcostcategorydefinitionresponsetypedef)
  - [CurrentInstanceTypeDef](#currentinstancetypedef)
  - [DateIntervalTypeDef](#dateintervaltypedef)
  - [DeleteCostCategoryDefinitionResponseTypeDef](#deletecostcategorydefinitionresponsetypedef)
  - [DescribeCostCategoryDefinitionResponseTypeDef](#describecostcategorydefinitionresponsetypedef)
  - [DimensionValuesTypeDef](#dimensionvaluestypedef)
  - [DimensionValuesWithAttributesTypeDef](#dimensionvalueswithattributestypedef)
  - [EBSResourceUtilizationTypeDef](#ebsresourceutilizationtypedef)
  - [EC2InstanceDetailsTypeDef](#ec2instancedetailstypedef)
  - [EC2ResourceDetailsTypeDef](#ec2resourcedetailstypedef)
  - [EC2ResourceUtilizationTypeDef](#ec2resourceutilizationtypedef)
  - [EC2SpecificationTypeDef](#ec2specificationtypedef)
  - [ESInstanceDetailsTypeDef](#esinstancedetailstypedef)
  - [ElastiCacheInstanceDetailsTypeDef](#elasticacheinstancedetailstypedef)
  - [ExpressionTypeDef](#expressiontypedef)
  - [ForecastResultTypeDef](#forecastresulttypedef)
  - [GetAnomaliesResponseTypeDef](#getanomaliesresponsetypedef)
  - [GetAnomalyMonitorsResponseTypeDef](#getanomalymonitorsresponsetypedef)
  - [GetAnomalySubscriptionsResponseTypeDef](#getanomalysubscriptionsresponsetypedef)
  - [GetCostAndUsageResponseTypeDef](#getcostandusageresponsetypedef)
  - [GetCostAndUsageWithResourcesResponseTypeDef](#getcostandusagewithresourcesresponsetypedef)
  - [GetCostCategoriesResponseTypeDef](#getcostcategoriesresponsetypedef)
  - [GetCostForecastResponseTypeDef](#getcostforecastresponsetypedef)
  - [GetDimensionValuesResponseTypeDef](#getdimensionvaluesresponsetypedef)
  - [GetReservationCoverageResponseTypeDef](#getreservationcoverageresponsetypedef)
  - [GetReservationPurchaseRecommendationResponseTypeDef](#getreservationpurchaserecommendationresponsetypedef)
  - [GetReservationUtilizationResponseTypeDef](#getreservationutilizationresponsetypedef)
  - [GetRightsizingRecommendationResponseTypeDef](#getrightsizingrecommendationresponsetypedef)
  - [GetSavingsPlansCoverageResponseTypeDef](#getsavingsplanscoverageresponsetypedef)
  - [GetSavingsPlansPurchaseRecommendationResponseTypeDef](#getsavingsplanspurchaserecommendationresponsetypedef)
  - [GetSavingsPlansUtilizationDetailsResponseTypeDef](#getsavingsplansutilizationdetailsresponsetypedef)
  - [GetSavingsPlansUtilizationResponseTypeDef](#getsavingsplansutilizationresponsetypedef)
  - [GetTagsResponseTypeDef](#gettagsresponsetypedef)
  - [GetUsageForecastResponseTypeDef](#getusageforecastresponsetypedef)
  - [GroupDefinitionTypeDef](#groupdefinitiontypedef)
  - [GroupTypeDef](#grouptypedef)
  - [ImpactTypeDef](#impacttypedef)
  - [InstanceDetailsTypeDef](#instancedetailstypedef)
  - [ListCostCategoryDefinitionsResponseTypeDef](#listcostcategorydefinitionsresponsetypedef)
  - [MetricValueTypeDef](#metricvaluetypedef)
  - [ModifyRecommendationDetailTypeDef](#modifyrecommendationdetailtypedef)
  - [ProvideAnomalyFeedbackResponseTypeDef](#provideanomalyfeedbackresponsetypedef)
  - [RDSInstanceDetailsTypeDef](#rdsinstancedetailstypedef)
  - [RedshiftInstanceDetailsTypeDef](#redshiftinstancedetailstypedef)
  - [ReservationAggregatesTypeDef](#reservationaggregatestypedef)
  - [ReservationCoverageGroupTypeDef](#reservationcoveragegrouptypedef)
  - [ReservationPurchaseRecommendationDetailTypeDef](#reservationpurchaserecommendationdetailtypedef)
  - [ReservationPurchaseRecommendationMetadataTypeDef](#reservationpurchaserecommendationmetadatatypedef)
  - [ReservationPurchaseRecommendationSummaryTypeDef](#reservationpurchaserecommendationsummarytypedef)
  - [ReservationPurchaseRecommendationTypeDef](#reservationpurchaserecommendationtypedef)
  - [ReservationUtilizationGroupTypeDef](#reservationutilizationgrouptypedef)
  - [ResourceDetailsTypeDef](#resourcedetailstypedef)
  - [ResourceUtilizationTypeDef](#resourceutilizationtypedef)
  - [ResultByTimeTypeDef](#resultbytimetypedef)
  - [RightsizingRecommendationConfigurationTypeDef](#rightsizingrecommendationconfigurationtypedef)
  - [RightsizingRecommendationMetadataTypeDef](#rightsizingrecommendationmetadatatypedef)
  - [RightsizingRecommendationSummaryTypeDef](#rightsizingrecommendationsummarytypedef)
  - [RightsizingRecommendationTypeDef](#rightsizingrecommendationtypedef)
  - [RootCauseTypeDef](#rootcausetypedef)
  - [SavingsPlansAmortizedCommitmentTypeDef](#savingsplansamortizedcommitmenttypedef)
  - [SavingsPlansCoverageDataTypeDef](#savingsplanscoveragedatatypedef)
  - [SavingsPlansCoverageTypeDef](#savingsplanscoveragetypedef)
  - [SavingsPlansDetailsTypeDef](#savingsplansdetailstypedef)
  - [SavingsPlansPurchaseRecommendationDetailTypeDef](#savingsplanspurchaserecommendationdetailtypedef)
  - [SavingsPlansPurchaseRecommendationMetadataTypeDef](#savingsplanspurchaserecommendationmetadatatypedef)
  - [SavingsPlansPurchaseRecommendationSummaryTypeDef](#savingsplanspurchaserecommendationsummarytypedef)
  - [SavingsPlansPurchaseRecommendationTypeDef](#savingsplanspurchaserecommendationtypedef)
  - [SavingsPlansSavingsTypeDef](#savingsplanssavingstypedef)
  - [SavingsPlansUtilizationAggregatesTypeDef](#savingsplansutilizationaggregatestypedef)
  - [SavingsPlansUtilizationByTimeTypeDef](#savingsplansutilizationbytimetypedef)
  - [SavingsPlansUtilizationDetailTypeDef](#savingsplansutilizationdetailtypedef)
  - [SavingsPlansUtilizationTypeDef](#savingsplansutilizationtypedef)
  - [ServiceSpecificationTypeDef](#servicespecificationtypedef)
  - [SortDefinitionTypeDef](#sortdefinitiontypedef)
  - [SubscriberTypeDef](#subscribertypedef)
  - [TagValuesTypeDef](#tagvaluestypedef)
  - [TargetInstanceTypeDef](#targetinstancetypedef)
  - [TerminateRecommendationDetailTypeDef](#terminaterecommendationdetailtypedef)
  - [TotalImpactFilterTypeDef](#totalimpactfiltertypedef)
  - [UpdateAnomalyMonitorResponseTypeDef](#updateanomalymonitorresponsetypedef)
  - [UpdateAnomalySubscriptionResponseTypeDef](#updateanomalysubscriptionresponsetypedef)
  - [UpdateCostCategoryDefinitionResponseTypeDef](#updatecostcategorydefinitionresponsetypedef)
  - [UtilizationByTimeTypeDef](#utilizationbytimetypedef)

## AnomalyDateIntervalTypeDef

```python
from mypy_boto3_ce.type_defs import AnomalyDateIntervalTypeDef
```


Required fields:
- `StartDate`: `str`



Optional fields:
- `EndDate`: `str`


## AnomalyMonitorTypeDef

```python
from mypy_boto3_ce.type_defs import AnomalyMonitorTypeDef
```


Required fields:
- `MonitorName`: `str`
- `MonitorType`: `MonitorType`



Optional fields:
- `MonitorArn`: `str`
- `CreationDate`: `str`
- `LastUpdatedDate`: `str`
- `LastEvaluatedDate`: `str`
- `MonitorDimension`: `Literal['SERVICE']`
- `MonitorSpecification`: `Dict[str, Any]`
- `DimensionalValueCount`: `int`


## AnomalyScoreTypeDef

```python
from mypy_boto3_ce.type_defs import AnomalyScoreTypeDef
```


Required fields:
- `MaxScore`: `float`
- `CurrentScore`: `float`




## AnomalySubscriptionTypeDef

```python
from mypy_boto3_ce.type_defs import AnomalySubscriptionTypeDef
```


Required fields:
- `MonitorArnList`: `List[str]`
- `Subscribers`: `List["SubscriberTypeDef"]`
- `Threshold`: `float`
- `Frequency`: `AnomalySubscriptionFrequency`
- `SubscriptionName`: `str`



Optional fields:
- `SubscriptionArn`: `str`
- `AccountId`: `str`


## AnomalyTypeDef

```python
from mypy_boto3_ce.type_defs import AnomalyTypeDef
```


Required fields:
- `AnomalyId`: `str`
- `AnomalyScore`: `"AnomalyScoreTypeDef"`
- `Impact`: `"ImpactTypeDef"`
- `MonitorArn`: `str`



Optional fields:
- `AnomalyStartDate`: `str`
- `AnomalyEndDate`: `str`
- `DimensionValue`: `str`
- `RootCauses`: `List["RootCauseTypeDef"]`
- `Feedback`: `AnomalyFeedbackType`


## CostCategoryInheritedValueDimensionTypeDef

```python
from mypy_boto3_ce.type_defs import CostCategoryInheritedValueDimensionTypeDef
```




Optional fields:
- `DimensionName`: `CostCategoryInheritedValueDimensionName`
- `DimensionKey`: `str`


## CostCategoryProcessingStatusTypeDef

```python
from mypy_boto3_ce.type_defs import CostCategoryProcessingStatusTypeDef
```




Optional fields:
- `Component`: `Literal['COST_EXPLORER']`
- `Status`: `CostCategoryStatus`


## CostCategoryReferenceTypeDef

```python
from mypy_boto3_ce.type_defs import CostCategoryReferenceTypeDef
```




Optional fields:
- `CostCategoryArn`: `str`
- `Name`: `str`
- `EffectiveStart`: `str`
- `EffectiveEnd`: `str`
- `NumberOfRules`: `int`
- `ProcessingStatus`: `List["CostCategoryProcessingStatusTypeDef"]`
- `Values`: `List[str]`
- `DefaultValue`: `str`


## CostCategoryRuleTypeDef

```python
from mypy_boto3_ce.type_defs import CostCategoryRuleTypeDef
```




Optional fields:
- `Value`: `str`
- `Rule`: `Dict[str, Any]`
- `InheritedValue`: `"CostCategoryInheritedValueDimensionTypeDef"`
- `Type`: `CostCategoryRuleType`


## CostCategoryTypeDef

```python
from mypy_boto3_ce.type_defs import CostCategoryTypeDef
```


Required fields:
- `CostCategoryArn`: `str`
- `EffectiveStart`: `str`
- `Name`: `str`
- `RuleVersion`: `Literal['CostCategoryExpression.v1']`
- `Rules`: `List["CostCategoryRuleTypeDef"]`



Optional fields:
- `EffectiveEnd`: `str`
- `ProcessingStatus`: `List["CostCategoryProcessingStatusTypeDef"]`
- `DefaultValue`: `str`


## CostCategoryValuesTypeDef

```python
from mypy_boto3_ce.type_defs import CostCategoryValuesTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`
- `MatchOptions`: `List[MatchOption]`


## CoverageByTimeTypeDef

```python
from mypy_boto3_ce.type_defs import CoverageByTimeTypeDef
```




Optional fields:
- `TimePeriod`: `"DateIntervalTypeDef"`
- `Groups`: `List["ReservationCoverageGroupTypeDef"]`
- `Total`: `"CoverageTypeDef"`


## CoverageCostTypeDef

```python
from mypy_boto3_ce.type_defs import CoverageCostTypeDef
```




Optional fields:
- `OnDemandCost`: `str`


## CoverageHoursTypeDef

```python
from mypy_boto3_ce.type_defs import CoverageHoursTypeDef
```




Optional fields:
- `OnDemandHours`: `str`
- `ReservedHours`: `str`
- `TotalRunningHours`: `str`
- `CoverageHoursPercentage`: `str`


## CoverageNormalizedUnitsTypeDef

```python
from mypy_boto3_ce.type_defs import CoverageNormalizedUnitsTypeDef
```




Optional fields:
- `OnDemandNormalizedUnits`: `str`
- `ReservedNormalizedUnits`: `str`
- `TotalRunningNormalizedUnits`: `str`
- `CoverageNormalizedUnitsPercentage`: `str`


## CoverageTypeDef

```python
from mypy_boto3_ce.type_defs import CoverageTypeDef
```




Optional fields:
- `CoverageHours`: `"CoverageHoursTypeDef"`
- `CoverageNormalizedUnits`: `"CoverageNormalizedUnitsTypeDef"`
- `CoverageCost`: `"CoverageCostTypeDef"`


## CreateAnomalyMonitorResponseTypeDef

```python
from mypy_boto3_ce.type_defs import CreateAnomalyMonitorResponseTypeDef
```


Required fields:
- `MonitorArn`: `str`




## CreateAnomalySubscriptionResponseTypeDef

```python
from mypy_boto3_ce.type_defs import CreateAnomalySubscriptionResponseTypeDef
```


Required fields:
- `SubscriptionArn`: `str`




## CreateCostCategoryDefinitionResponseTypeDef

```python
from mypy_boto3_ce.type_defs import CreateCostCategoryDefinitionResponseTypeDef
```




Optional fields:
- `CostCategoryArn`: `str`
- `EffectiveStart`: `str`


## CurrentInstanceTypeDef

```python
from mypy_boto3_ce.type_defs import CurrentInstanceTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `InstanceName`: `str`
- `Tags`: `List["TagValuesTypeDef"]`
- `ResourceDetails`: `"ResourceDetailsTypeDef"`
- `ResourceUtilization`: `"ResourceUtilizationTypeDef"`
- `ReservationCoveredHoursInLookbackPeriod`: `str`
- `SavingsPlansCoveredHoursInLookbackPeriod`: `str`
- `OnDemandHoursInLookbackPeriod`: `str`
- `TotalRunningHoursInLookbackPeriod`: `str`
- `MonthlyCost`: `str`
- `CurrencyCode`: `str`


## DateIntervalTypeDef

```python
from mypy_boto3_ce.type_defs import DateIntervalTypeDef
```


Required fields:
- `Start`: `str`
- `End`: `str`




## DeleteCostCategoryDefinitionResponseTypeDef

```python
from mypy_boto3_ce.type_defs import DeleteCostCategoryDefinitionResponseTypeDef
```




Optional fields:
- `CostCategoryArn`: `str`
- `EffectiveEnd`: `str`


## DescribeCostCategoryDefinitionResponseTypeDef

```python
from mypy_boto3_ce.type_defs import DescribeCostCategoryDefinitionResponseTypeDef
```




Optional fields:
- `CostCategory`: `"CostCategoryTypeDef"`


## DimensionValuesTypeDef

```python
from mypy_boto3_ce.type_defs import DimensionValuesTypeDef
```




Optional fields:
- `Key`: `Dimension`
- `Values`: `List[str]`
- `MatchOptions`: `List[MatchOption]`


## DimensionValuesWithAttributesTypeDef

```python
from mypy_boto3_ce.type_defs import DimensionValuesWithAttributesTypeDef
```




Optional fields:
- `Value`: `str`
- `Attributes`: `Dict[str, str]`


## EBSResourceUtilizationTypeDef

```python
from mypy_boto3_ce.type_defs import EBSResourceUtilizationTypeDef
```




Optional fields:
- `EbsReadOpsPerSecond`: `str`
- `EbsWriteOpsPerSecond`: `str`
- `EbsReadBytesPerSecond`: `str`
- `EbsWriteBytesPerSecond`: `str`


## EC2InstanceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import EC2InstanceDetailsTypeDef
```




Optional fields:
- `Family`: `str`
- `InstanceType`: `str`
- `Region`: `str`
- `AvailabilityZone`: `str`
- `Platform`: `str`
- `Tenancy`: `str`
- `CurrentGeneration`: `bool`
- `SizeFlexEligible`: `bool`


## EC2ResourceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import EC2ResourceDetailsTypeDef
```




Optional fields:
- `HourlyOnDemandRate`: `str`
- `InstanceType`: `str`
- `Platform`: `str`
- `Region`: `str`
- `Sku`: `str`
- `Memory`: `str`
- `NetworkPerformance`: `str`
- `Storage`: `str`
- `Vcpu`: `str`


## EC2ResourceUtilizationTypeDef

```python
from mypy_boto3_ce.type_defs import EC2ResourceUtilizationTypeDef
```




Optional fields:
- `MaxCpuUtilizationPercentage`: `str`
- `MaxMemoryUtilizationPercentage`: `str`
- `MaxStorageUtilizationPercentage`: `str`
- `EBSResourceUtilization`: `"EBSResourceUtilizationTypeDef"`


## EC2SpecificationTypeDef

```python
from mypy_boto3_ce.type_defs import EC2SpecificationTypeDef
```




Optional fields:
- `OfferingClass`: `OfferingClass`


## ESInstanceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import ESInstanceDetailsTypeDef
```




Optional fields:
- `InstanceClass`: `str`
- `InstanceSize`: `str`
- `Region`: `str`
- `CurrentGeneration`: `bool`
- `SizeFlexEligible`: `bool`


## ElastiCacheInstanceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import ElastiCacheInstanceDetailsTypeDef
```




Optional fields:
- `Family`: `str`
- `NodeType`: `str`
- `Region`: `str`
- `ProductDescription`: `str`
- `CurrentGeneration`: `bool`
- `SizeFlexEligible`: `bool`


## ExpressionTypeDef

```python
from mypy_boto3_ce.type_defs import ExpressionTypeDef
```




Optional fields:
- `Or`: `List[Dict[str, Any]]`
- `And`: `List[Dict[str, Any]]`
- `Not`: `Dict[str, Any]`
- `Dimensions`: `"DimensionValuesTypeDef"`
- `Tags`: `"TagValuesTypeDef"`
- `CostCategories`: `"CostCategoryValuesTypeDef"`


## ForecastResultTypeDef

```python
from mypy_boto3_ce.type_defs import ForecastResultTypeDef
```




Optional fields:
- `TimePeriod`: `"DateIntervalTypeDef"`
- `MeanValue`: `str`
- `PredictionIntervalLowerBound`: `str`
- `PredictionIntervalUpperBound`: `str`


## GetAnomaliesResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetAnomaliesResponseTypeDef
```


Required fields:
- `Anomalies`: `List["AnomalyTypeDef"]`



Optional fields:
- `NextPageToken`: `str`


## GetAnomalyMonitorsResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetAnomalyMonitorsResponseTypeDef
```


Required fields:
- `AnomalyMonitors`: `List["AnomalyMonitorTypeDef"]`



Optional fields:
- `NextPageToken`: `str`


## GetAnomalySubscriptionsResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetAnomalySubscriptionsResponseTypeDef
```


Required fields:
- `AnomalySubscriptions`: `List["AnomalySubscriptionTypeDef"]`



Optional fields:
- `NextPageToken`: `str`


## GetCostAndUsageResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetCostAndUsageResponseTypeDef
```




Optional fields:
- `NextPageToken`: `str`
- `GroupDefinitions`: `List["GroupDefinitionTypeDef"]`
- `ResultsByTime`: `List["ResultByTimeTypeDef"]`
- `DimensionValueAttributes`: `List["DimensionValuesWithAttributesTypeDef"]`


## GetCostAndUsageWithResourcesResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetCostAndUsageWithResourcesResponseTypeDef
```




Optional fields:
- `NextPageToken`: `str`
- `GroupDefinitions`: `List["GroupDefinitionTypeDef"]`
- `ResultsByTime`: `List["ResultByTimeTypeDef"]`
- `DimensionValueAttributes`: `List["DimensionValuesWithAttributesTypeDef"]`


## GetCostCategoriesResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetCostCategoriesResponseTypeDef
```


Required fields:
- `ReturnSize`: `int`
- `TotalSize`: `int`



Optional fields:
- `NextPageToken`: `str`
- `CostCategoryNames`: `List[str]`
- `CostCategoryValues`: `List[str]`


## GetCostForecastResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetCostForecastResponseTypeDef
```




Optional fields:
- `Total`: `"MetricValueTypeDef"`
- `ForecastResultsByTime`: `List["ForecastResultTypeDef"]`


## GetDimensionValuesResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetDimensionValuesResponseTypeDef
```


Required fields:
- `DimensionValues`: `List["DimensionValuesWithAttributesTypeDef"]`
- `ReturnSize`: `int`
- `TotalSize`: `int`



Optional fields:
- `NextPageToken`: `str`


## GetReservationCoverageResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetReservationCoverageResponseTypeDef
```


Required fields:
- `CoveragesByTime`: `List["CoverageByTimeTypeDef"]`



Optional fields:
- `Total`: `"CoverageTypeDef"`
- `NextPageToken`: `str`


## GetReservationPurchaseRecommendationResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetReservationPurchaseRecommendationResponseTypeDef
```




Optional fields:
- `Metadata`: `"ReservationPurchaseRecommendationMetadataTypeDef"`
- `Recommendations`: `List["ReservationPurchaseRecommendationTypeDef"]`
- `NextPageToken`: `str`


## GetReservationUtilizationResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetReservationUtilizationResponseTypeDef
```


Required fields:
- `UtilizationsByTime`: `List["UtilizationByTimeTypeDef"]`



Optional fields:
- `Total`: `"ReservationAggregatesTypeDef"`
- `NextPageToken`: `str`


## GetRightsizingRecommendationResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetRightsizingRecommendationResponseTypeDef
```




Optional fields:
- `Metadata`: `"RightsizingRecommendationMetadataTypeDef"`
- `Summary`: `"RightsizingRecommendationSummaryTypeDef"`
- `RightsizingRecommendations`: `List["RightsizingRecommendationTypeDef"]`
- `NextPageToken`: `str`
- `Configuration`: `"RightsizingRecommendationConfigurationTypeDef"`


## GetSavingsPlansCoverageResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetSavingsPlansCoverageResponseTypeDef
```


Required fields:
- `SavingsPlansCoverages`: `List["SavingsPlansCoverageTypeDef"]`



Optional fields:
- `NextToken`: `str`


## GetSavingsPlansPurchaseRecommendationResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetSavingsPlansPurchaseRecommendationResponseTypeDef
```




Optional fields:
- `Metadata`: `"SavingsPlansPurchaseRecommendationMetadataTypeDef"`
- `SavingsPlansPurchaseRecommendation`: `"SavingsPlansPurchaseRecommendationTypeDef"`
- `NextPageToken`: `str`


## GetSavingsPlansUtilizationDetailsResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetSavingsPlansUtilizationDetailsResponseTypeDef
```


Required fields:
- `SavingsPlansUtilizationDetails`: `List["SavingsPlansUtilizationDetailTypeDef"]`
- `TimePeriod`: `"DateIntervalTypeDef"`



Optional fields:
- `Total`: `"SavingsPlansUtilizationAggregatesTypeDef"`
- `NextToken`: `str`


## GetSavingsPlansUtilizationResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetSavingsPlansUtilizationResponseTypeDef
```


Required fields:
- `Total`: `"SavingsPlansUtilizationAggregatesTypeDef"`



Optional fields:
- `SavingsPlansUtilizationsByTime`: `List["SavingsPlansUtilizationByTimeTypeDef"]`


## GetTagsResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetTagsResponseTypeDef
```


Required fields:
- `Tags`: `List[str]`
- `ReturnSize`: `int`
- `TotalSize`: `int`



Optional fields:
- `NextPageToken`: `str`


## GetUsageForecastResponseTypeDef

```python
from mypy_boto3_ce.type_defs import GetUsageForecastResponseTypeDef
```




Optional fields:
- `Total`: `"MetricValueTypeDef"`
- `ForecastResultsByTime`: `List["ForecastResultTypeDef"]`


## GroupDefinitionTypeDef

```python
from mypy_boto3_ce.type_defs import GroupDefinitionTypeDef
```




Optional fields:
- `Type`: `GroupDefinitionType`
- `Key`: `str`


## GroupTypeDef

```python
from mypy_boto3_ce.type_defs import GroupTypeDef
```




Optional fields:
- `Keys`: `List[str]`
- `Metrics`: `Dict[str, "MetricValueTypeDef"]`


## ImpactTypeDef

```python
from mypy_boto3_ce.type_defs import ImpactTypeDef
```


Required fields:
- `MaxImpact`: `float`



Optional fields:
- `TotalImpact`: `float`


## InstanceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import InstanceDetailsTypeDef
```




Optional fields:
- `EC2InstanceDetails`: `"EC2InstanceDetailsTypeDef"`
- `RDSInstanceDetails`: `"RDSInstanceDetailsTypeDef"`
- `RedshiftInstanceDetails`: `"RedshiftInstanceDetailsTypeDef"`
- `ElastiCacheInstanceDetails`: `"ElastiCacheInstanceDetailsTypeDef"`
- `ESInstanceDetails`: `"ESInstanceDetailsTypeDef"`


## ListCostCategoryDefinitionsResponseTypeDef

```python
from mypy_boto3_ce.type_defs import ListCostCategoryDefinitionsResponseTypeDef
```




Optional fields:
- `CostCategoryReferences`: `List["CostCategoryReferenceTypeDef"]`
- `NextToken`: `str`


## MetricValueTypeDef

```python
from mypy_boto3_ce.type_defs import MetricValueTypeDef
```




Optional fields:
- `Amount`: `str`
- `Unit`: `str`


## ModifyRecommendationDetailTypeDef

```python
from mypy_boto3_ce.type_defs import ModifyRecommendationDetailTypeDef
```




Optional fields:
- `TargetInstances`: `List["TargetInstanceTypeDef"]`


## ProvideAnomalyFeedbackResponseTypeDef

```python
from mypy_boto3_ce.type_defs import ProvideAnomalyFeedbackResponseTypeDef
```


Required fields:
- `AnomalyId`: `str`




## RDSInstanceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import RDSInstanceDetailsTypeDef
```




Optional fields:
- `Family`: `str`
- `InstanceType`: `str`
- `Region`: `str`
- `DatabaseEngine`: `str`
- `DatabaseEdition`: `str`
- `DeploymentOption`: `str`
- `LicenseModel`: `str`
- `CurrentGeneration`: `bool`
- `SizeFlexEligible`: `bool`


## RedshiftInstanceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import RedshiftInstanceDetailsTypeDef
```




Optional fields:
- `Family`: `str`
- `NodeType`: `str`
- `Region`: `str`
- `CurrentGeneration`: `bool`
- `SizeFlexEligible`: `bool`


## ReservationAggregatesTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationAggregatesTypeDef
```




Optional fields:
- `UtilizationPercentage`: `str`
- `UtilizationPercentageInUnits`: `str`
- `PurchasedHours`: `str`
- `PurchasedUnits`: `str`
- `TotalActualHours`: `str`
- `TotalActualUnits`: `str`
- `UnusedHours`: `str`
- `UnusedUnits`: `str`
- `OnDemandCostOfRIHoursUsed`: `str`
- `NetRISavings`: `str`
- `TotalPotentialRISavings`: `str`
- `AmortizedUpfrontFee`: `str`
- `AmortizedRecurringFee`: `str`
- `TotalAmortizedFee`: `str`
- `RICostForUnusedHours`: `str`
- `RealizedSavings`: `str`
- `UnrealizedSavings`: `str`


## ReservationCoverageGroupTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationCoverageGroupTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`
- `Coverage`: `"CoverageTypeDef"`


## ReservationPurchaseRecommendationDetailTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationPurchaseRecommendationDetailTypeDef
```




Optional fields:
- `AccountId`: `str`
- `InstanceDetails`: `"InstanceDetailsTypeDef"`
- `RecommendedNumberOfInstancesToPurchase`: `str`
- `RecommendedNormalizedUnitsToPurchase`: `str`
- `MinimumNumberOfInstancesUsedPerHour`: `str`
- `MinimumNormalizedUnitsUsedPerHour`: `str`
- `MaximumNumberOfInstancesUsedPerHour`: `str`
- `MaximumNormalizedUnitsUsedPerHour`: `str`
- `AverageNumberOfInstancesUsedPerHour`: `str`
- `AverageNormalizedUnitsUsedPerHour`: `str`
- `AverageUtilization`: `str`
- `EstimatedBreakEvenInMonths`: `str`
- `CurrencyCode`: `str`
- `EstimatedMonthlySavingsAmount`: `str`
- `EstimatedMonthlySavingsPercentage`: `str`
- `EstimatedMonthlyOnDemandCost`: `str`
- `EstimatedReservationCostForLookbackPeriod`: `str`
- `UpfrontCost`: `str`
- `RecurringStandardMonthlyCost`: `str`


## ReservationPurchaseRecommendationMetadataTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationPurchaseRecommendationMetadataTypeDef
```




Optional fields:
- `RecommendationId`: `str`
- `GenerationTimestamp`: `str`


## ReservationPurchaseRecommendationSummaryTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationPurchaseRecommendationSummaryTypeDef
```




Optional fields:
- `TotalEstimatedMonthlySavingsAmount`: `str`
- `TotalEstimatedMonthlySavingsPercentage`: `str`
- `CurrencyCode`: `str`


## ReservationPurchaseRecommendationTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationPurchaseRecommendationTypeDef
```




Optional fields:
- `AccountScope`: `AccountScope`
- `LookbackPeriodInDays`: `LookbackPeriodInDays`
- `TermInYears`: `TermInYears`
- `PaymentOption`: `PaymentOption`
- `ServiceSpecification`: `"ServiceSpecificationTypeDef"`
- `RecommendationDetails`: `List["ReservationPurchaseRecommendationDetailTypeDef"]`
- `RecommendationSummary`: `"ReservationPurchaseRecommendationSummaryTypeDef"`


## ReservationUtilizationGroupTypeDef

```python
from mypy_boto3_ce.type_defs import ReservationUtilizationGroupTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `Attributes`: `Dict[str, str]`
- `Utilization`: `"ReservationAggregatesTypeDef"`


## ResourceDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import ResourceDetailsTypeDef
```




Optional fields:
- `EC2ResourceDetails`: `"EC2ResourceDetailsTypeDef"`


## ResourceUtilizationTypeDef

```python
from mypy_boto3_ce.type_defs import ResourceUtilizationTypeDef
```




Optional fields:
- `EC2ResourceUtilization`: `"EC2ResourceUtilizationTypeDef"`


## ResultByTimeTypeDef

```python
from mypy_boto3_ce.type_defs import ResultByTimeTypeDef
```




Optional fields:
- `TimePeriod`: `"DateIntervalTypeDef"`
- `Total`: `Dict[str, "MetricValueTypeDef"]`
- `Groups`: `List["GroupTypeDef"]`
- `Estimated`: `bool`


## RightsizingRecommendationConfigurationTypeDef

```python
from mypy_boto3_ce.type_defs import RightsizingRecommendationConfigurationTypeDef
```


Required fields:
- `RecommendationTarget`: `RecommendationTarget`
- `BenefitsConsidered`: `bool`




## RightsizingRecommendationMetadataTypeDef

```python
from mypy_boto3_ce.type_defs import RightsizingRecommendationMetadataTypeDef
```




Optional fields:
- `RecommendationId`: `str`
- `GenerationTimestamp`: `str`
- `LookbackPeriodInDays`: `LookbackPeriodInDays`
- `AdditionalMetadata`: `str`


## RightsizingRecommendationSummaryTypeDef

```python
from mypy_boto3_ce.type_defs import RightsizingRecommendationSummaryTypeDef
```




Optional fields:
- `TotalRecommendationCount`: `str`
- `EstimatedTotalMonthlySavingsAmount`: `str`
- `SavingsCurrencyCode`: `str`
- `SavingsPercentage`: `str`


## RightsizingRecommendationTypeDef

```python
from mypy_boto3_ce.type_defs import RightsizingRecommendationTypeDef
```




Optional fields:
- `AccountId`: `str`
- `CurrentInstance`: `"CurrentInstanceTypeDef"`
- `RightsizingType`: `RightsizingType`
- `ModifyRecommendationDetail`: `"ModifyRecommendationDetailTypeDef"`
- `TerminateRecommendationDetail`: `"TerminateRecommendationDetailTypeDef"`


## RootCauseTypeDef

```python
from mypy_boto3_ce.type_defs import RootCauseTypeDef
```




Optional fields:
- `Service`: `str`
- `Region`: `str`
- `LinkedAccount`: `str`
- `UsageType`: `str`


## SavingsPlansAmortizedCommitmentTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansAmortizedCommitmentTypeDef
```




Optional fields:
- `AmortizedRecurringCommitment`: `str`
- `AmortizedUpfrontCommitment`: `str`
- `TotalAmortizedCommitment`: `str`


## SavingsPlansCoverageDataTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansCoverageDataTypeDef
```




Optional fields:
- `SpendCoveredBySavingsPlans`: `str`
- `OnDemandCost`: `str`
- `TotalCost`: `str`
- `CoveragePercentage`: `str`


## SavingsPlansCoverageTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansCoverageTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`
- `Coverage`: `"SavingsPlansCoverageDataTypeDef"`
- `TimePeriod`: `"DateIntervalTypeDef"`


## SavingsPlansDetailsTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansDetailsTypeDef
```




Optional fields:
- `Region`: `str`
- `InstanceFamily`: `str`
- `OfferingId`: `str`


## SavingsPlansPurchaseRecommendationDetailTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansPurchaseRecommendationDetailTypeDef
```




Optional fields:
- `SavingsPlansDetails`: `"SavingsPlansDetailsTypeDef"`
- `AccountId`: `str`
- `UpfrontCost`: `str`
- `EstimatedROI`: `str`
- `CurrencyCode`: `str`
- `EstimatedSPCost`: `str`
- `EstimatedOnDemandCost`: `str`
- `EstimatedOnDemandCostWithCurrentCommitment`: `str`
- `EstimatedSavingsAmount`: `str`
- `EstimatedSavingsPercentage`: `str`
- `HourlyCommitmentToPurchase`: `str`
- `EstimatedAverageUtilization`: `str`
- `EstimatedMonthlySavingsAmount`: `str`
- `CurrentMinimumHourlyOnDemandSpend`: `str`
- `CurrentMaximumHourlyOnDemandSpend`: `str`
- `CurrentAverageHourlyOnDemandSpend`: `str`


## SavingsPlansPurchaseRecommendationMetadataTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansPurchaseRecommendationMetadataTypeDef
```




Optional fields:
- `RecommendationId`: `str`
- `GenerationTimestamp`: `str`
- `AdditionalMetadata`: `str`


## SavingsPlansPurchaseRecommendationSummaryTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansPurchaseRecommendationSummaryTypeDef
```




Optional fields:
- `EstimatedROI`: `str`
- `CurrencyCode`: `str`
- `EstimatedTotalCost`: `str`
- `CurrentOnDemandSpend`: `str`
- `EstimatedSavingsAmount`: `str`
- `TotalRecommendationCount`: `str`
- `DailyCommitmentToPurchase`: `str`
- `HourlyCommitmentToPurchase`: `str`
- `EstimatedSavingsPercentage`: `str`
- `EstimatedMonthlySavingsAmount`: `str`
- `EstimatedOnDemandCostWithCurrentCommitment`: `str`


## SavingsPlansPurchaseRecommendationTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansPurchaseRecommendationTypeDef
```




Optional fields:
- `AccountScope`: `AccountScope`
- `SavingsPlansType`: `SupportedSavingsPlansType`
- `TermInYears`: `TermInYears`
- `PaymentOption`: `PaymentOption`
- `LookbackPeriodInDays`: `LookbackPeriodInDays`
- `SavingsPlansPurchaseRecommendationDetails`: `List["SavingsPlansPurchaseRecommendationDetailTypeDef"]`
- `SavingsPlansPurchaseRecommendationSummary`: `"SavingsPlansPurchaseRecommendationSummaryTypeDef"`


## SavingsPlansSavingsTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansSavingsTypeDef
```




Optional fields:
- `NetSavings`: `str`
- `OnDemandCostEquivalent`: `str`


## SavingsPlansUtilizationAggregatesTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansUtilizationAggregatesTypeDef
```


Required fields:
- `Utilization`: `"SavingsPlansUtilizationTypeDef"`



Optional fields:
- `Savings`: `"SavingsPlansSavingsTypeDef"`
- `AmortizedCommitment`: `"SavingsPlansAmortizedCommitmentTypeDef"`


## SavingsPlansUtilizationByTimeTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansUtilizationByTimeTypeDef
```


Required fields:
- `TimePeriod`: `"DateIntervalTypeDef"`
- `Utilization`: `"SavingsPlansUtilizationTypeDef"`



Optional fields:
- `Savings`: `"SavingsPlansSavingsTypeDef"`
- `AmortizedCommitment`: `"SavingsPlansAmortizedCommitmentTypeDef"`


## SavingsPlansUtilizationDetailTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansUtilizationDetailTypeDef
```




Optional fields:
- `SavingsPlanArn`: `str`
- `Attributes`: `Dict[str, str]`
- `Utilization`: `"SavingsPlansUtilizationTypeDef"`
- `Savings`: `"SavingsPlansSavingsTypeDef"`
- `AmortizedCommitment`: `"SavingsPlansAmortizedCommitmentTypeDef"`


## SavingsPlansUtilizationTypeDef

```python
from mypy_boto3_ce.type_defs import SavingsPlansUtilizationTypeDef
```




Optional fields:
- `TotalCommitment`: `str`
- `UsedCommitment`: `str`
- `UnusedCommitment`: `str`
- `UtilizationPercentage`: `str`


## ServiceSpecificationTypeDef

```python
from mypy_boto3_ce.type_defs import ServiceSpecificationTypeDef
```




Optional fields:
- `EC2Specification`: `"EC2SpecificationTypeDef"`


## SortDefinitionTypeDef

```python
from mypy_boto3_ce.type_defs import SortDefinitionTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `SortOrder`: `SortOrder`


## SubscriberTypeDef

```python
from mypy_boto3_ce.type_defs import SubscriberTypeDef
```




Optional fields:
- `Address`: `str`
- `Type`: `SubscriberType`
- `Status`: `SubscriberStatus`


## TagValuesTypeDef

```python
from mypy_boto3_ce.type_defs import TagValuesTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`
- `MatchOptions`: `List[MatchOption]`


## TargetInstanceTypeDef

```python
from mypy_boto3_ce.type_defs import TargetInstanceTypeDef
```




Optional fields:
- `EstimatedMonthlyCost`: `str`
- `EstimatedMonthlySavings`: `str`
- `CurrencyCode`: `str`
- `DefaultTargetInstance`: `bool`
- `ResourceDetails`: `"ResourceDetailsTypeDef"`
- `ExpectedResourceUtilization`: `"ResourceUtilizationTypeDef"`


## TerminateRecommendationDetailTypeDef

```python
from mypy_boto3_ce.type_defs import TerminateRecommendationDetailTypeDef
```




Optional fields:
- `EstimatedMonthlySavings`: `str`
- `CurrencyCode`: `str`


## TotalImpactFilterTypeDef

```python
from mypy_boto3_ce.type_defs import TotalImpactFilterTypeDef
```


Required fields:
- `NumericOperator`: `NumericOperator`
- `StartValue`: `float`



Optional fields:
- `EndValue`: `float`


## UpdateAnomalyMonitorResponseTypeDef

```python
from mypy_boto3_ce.type_defs import UpdateAnomalyMonitorResponseTypeDef
```


Required fields:
- `MonitorArn`: `str`




## UpdateAnomalySubscriptionResponseTypeDef

```python
from mypy_boto3_ce.type_defs import UpdateAnomalySubscriptionResponseTypeDef
```


Required fields:
- `SubscriptionArn`: `str`




## UpdateCostCategoryDefinitionResponseTypeDef

```python
from mypy_boto3_ce.type_defs import UpdateCostCategoryDefinitionResponseTypeDef
```




Optional fields:
- `CostCategoryArn`: `str`
- `EffectiveStart`: `str`


## UtilizationByTimeTypeDef

```python
from mypy_boto3_ce.type_defs import UtilizationByTimeTypeDef
```




Optional fields:
- `TimePeriod`: `"DateIntervalTypeDef"`
- `Groups`: `List["ReservationUtilizationGroupTypeDef"]`
- `Total`: `"ReservationAggregatesTypeDef"`

