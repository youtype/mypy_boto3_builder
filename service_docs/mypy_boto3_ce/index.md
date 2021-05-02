# Type annotations for boto3 CostExplorer module

> [Index](../index.md) > CostExplorer

Auto-generated documentation for [CostExplorer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer)
type annotations stubs module [mypy_boto3_ce](https://pypi.org/project/mypy-boto3-ce/).

```bash
pip install mypy-boto3-ce
```

- [Type annotations for boto3 CostExplorer module](#type-annotations-for-boto3-costexplorer-module)
  - [CostExplorerClient](#costexplorerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## CostExplorerClient

Type annotations for  `boto3.client("ce")` as [CostExplorerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ce.client import CostExplorerClient
```


CostExplorerClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_anomaly_monitor](./client.md#create-anomaly-monitor)
- [create_anomaly_subscription](./client.md#create-anomaly-subscription)
- [create_cost_category_definition](./client.md#create-cost-category-definition)
- [delete_anomaly_monitor](./client.md#delete-anomaly-monitor)
- [delete_anomaly_subscription](./client.md#delete-anomaly-subscription)
- [delete_cost_category_definition](./client.md#delete-cost-category-definition)
- [describe_cost_category_definition](./client.md#describe-cost-category-definition)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_anomalies](./client.md#get-anomalies)
- [get_anomaly_monitors](./client.md#get-anomaly-monitors)
- [get_anomaly_subscriptions](./client.md#get-anomaly-subscriptions)
- [get_cost_and_usage](./client.md#get-cost-and-usage)
- [get_cost_and_usage_with_resources](./client.md#get-cost-and-usage-with-resources)
- [get_cost_categories](./client.md#get-cost-categories)
- [get_cost_forecast](./client.md#get-cost-forecast)
- [get_dimension_values](./client.md#get-dimension-values)
- [get_reservation_coverage](./client.md#get-reservation-coverage)
- [get_reservation_purchase_recommendation](./client.md#get-reservation-purchase-recommendation)
- [get_reservation_utilization](./client.md#get-reservation-utilization)
- [get_rightsizing_recommendation](./client.md#get-rightsizing-recommendation)
- [get_savings_plans_coverage](./client.md#get-savings-plans-coverage)
- [get_savings_plans_purchase_recommendation](./client.md#get-savings-plans-purchase-recommendation)
- [get_savings_plans_utilization](./client.md#get-savings-plans-utilization)
- [get_savings_plans_utilization_details](./client.md#get-savings-plans-utilization-details)
- [get_tags](./client.md#get-tags)
- [get_usage_forecast](./client.md#get-usage-forecast)
- [list_cost_category_definitions](./client.md#list-cost-category-definitions)
- [provide_anomaly_feedback](./client.md#provide-anomaly-feedback)
- [update_anomaly_monitor](./client.md#update-anomaly-monitor)
- [update_anomaly_subscription](./client.md#update-anomaly-subscription)
- [update_cost_category_definition](./client.md#update-cost-category-definition)




### Exceptions
- [BillExpirationException](./client.md#billexpirationexception)
- [ClientError](./client.md#clienterror)
- [DataUnavailableException](./client.md#dataunavailableexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [RequestChangedException](./client.md#requestchangedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [UnknownMonitorException](./client.md#unknownmonitorexception)
- [UnknownSubscriptionException](./client.md#unknownsubscriptionexception)
- [UnresolvableUsageUnitException](./client.md#unresolvableusageunitexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ce.literals import AccountScope, ...
```

- [AccountScope](./literals.md#accountscope)
- [AnomalyFeedbackType](./literals.md#anomalyfeedbacktype)
- [AnomalySubscriptionFrequency](./literals.md#anomalysubscriptionfrequency)
- [Context](./literals.md#context)
- [CostCategoryInheritedValueDimensionName](./literals.md#costcategoryinheritedvaluedimensionname)
- [CostCategoryRuleType](./literals.md#costcategoryruletype)
- [CostCategoryRuleVersion](./literals.md#costcategoryruleversion)
- [CostCategoryStatus](./literals.md#costcategorystatus)
- [CostCategoryStatusComponent](./literals.md#costcategorystatuscomponent)
- [Dimension](./literals.md#dimension)
- [Granularity](./literals.md#granularity)
- [GroupDefinitionType](./literals.md#groupdefinitiontype)
- [LookbackPeriodInDays](./literals.md#lookbackperiodindays)
- [MatchOption](./literals.md#matchoption)
- [Metric](./literals.md#metric)
- [MonitorDimension](./literals.md#monitordimension)
- [MonitorType](./literals.md#monitortype)
- [NumericOperator](./literals.md#numericoperator)
- [OfferingClass](./literals.md#offeringclass)
- [PaymentOption](./literals.md#paymentoption)
- [RecommendationTarget](./literals.md#recommendationtarget)
- [RightsizingType](./literals.md#rightsizingtype)
- [SavingsPlansDataType](./literals.md#savingsplansdatatype)
- [SortOrder](./literals.md#sortorder)
- [SubscriberStatus](./literals.md#subscriberstatus)
- [SubscriberType](./literals.md#subscribertype)
- [SupportedSavingsPlansType](./literals.md#supportedsavingsplanstype)
- [TermInYears](./literals.md#terminyears)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ce.type_defs import AnomalyMonitorTypeDef, ...
```

- [AnomalyMonitorTypeDef](./type_defs.md#anomalymonitortypedef)
- [AnomalyScoreTypeDef](./type_defs.md#anomalyscoretypedef)
- [AnomalySubscriptionTypeDef](./type_defs.md#anomalysubscriptiontypedef)
- [AnomalyTypeDef](./type_defs.md#anomalytypedef)
- [CostCategoryInheritedValueDimensionTypeDef](./type_defs.md#costcategoryinheritedvaluedimensiontypedef)
- [CostCategoryProcessingStatusTypeDef](./type_defs.md#costcategoryprocessingstatustypedef)
- [CostCategoryReferenceTypeDef](./type_defs.md#costcategoryreferencetypedef)
- [CostCategoryRuleTypeDef](./type_defs.md#costcategoryruletypedef)
- [CostCategoryTypeDef](./type_defs.md#costcategorytypedef)
- [CostCategoryValuesTypeDef](./type_defs.md#costcategoryvaluestypedef)
- [CoverageByTimeTypeDef](./type_defs.md#coveragebytimetypedef)
- [CoverageCostTypeDef](./type_defs.md#coveragecosttypedef)
- [CoverageHoursTypeDef](./type_defs.md#coveragehourstypedef)
- [CoverageNormalizedUnitsTypeDef](./type_defs.md#coveragenormalizedunitstypedef)
- [CoverageTypeDef](./type_defs.md#coveragetypedef)
- [CurrentInstanceTypeDef](./type_defs.md#currentinstancetypedef)
- [DateIntervalTypeDef](./type_defs.md#dateintervaltypedef)
- [DimensionValuesTypeDef](./type_defs.md#dimensionvaluestypedef)
- [DimensionValuesWithAttributesTypeDef](./type_defs.md#dimensionvalueswithattributestypedef)
- [EBSResourceUtilizationTypeDef](./type_defs.md#ebsresourceutilizationtypedef)
- [EC2InstanceDetailsTypeDef](./type_defs.md#ec2instancedetailstypedef)
- [EC2ResourceDetailsTypeDef](./type_defs.md#ec2resourcedetailstypedef)
- [EC2ResourceUtilizationTypeDef](./type_defs.md#ec2resourceutilizationtypedef)
- [EC2SpecificationTypeDef](./type_defs.md#ec2specificationtypedef)
- [ESInstanceDetailsTypeDef](./type_defs.md#esinstancedetailstypedef)
- [ElastiCacheInstanceDetailsTypeDef](./type_defs.md#elasticacheinstancedetailstypedef)
- [ForecastResultTypeDef](./type_defs.md#forecastresulttypedef)
- [GroupDefinitionTypeDef](./type_defs.md#groupdefinitiontypedef)
- [GroupTypeDef](./type_defs.md#grouptypedef)
- [ImpactTypeDef](./type_defs.md#impacttypedef)
- [InstanceDetailsTypeDef](./type_defs.md#instancedetailstypedef)
- [MetricValueTypeDef](./type_defs.md#metricvaluetypedef)
- [ModifyRecommendationDetailTypeDef](./type_defs.md#modifyrecommendationdetailtypedef)
- [RDSInstanceDetailsTypeDef](./type_defs.md#rdsinstancedetailstypedef)
- [RedshiftInstanceDetailsTypeDef](./type_defs.md#redshiftinstancedetailstypedef)
- [ReservationAggregatesTypeDef](./type_defs.md#reservationaggregatestypedef)
- [ReservationCoverageGroupTypeDef](./type_defs.md#reservationcoveragegrouptypedef)
- [ReservationPurchaseRecommendationDetailTypeDef](./type_defs.md#reservationpurchaserecommendationdetailtypedef)
- [ReservationPurchaseRecommendationMetadataTypeDef](./type_defs.md#reservationpurchaserecommendationmetadatatypedef)
- [ReservationPurchaseRecommendationSummaryTypeDef](./type_defs.md#reservationpurchaserecommendationsummarytypedef)
- [ReservationPurchaseRecommendationTypeDef](./type_defs.md#reservationpurchaserecommendationtypedef)
- [ReservationUtilizationGroupTypeDef](./type_defs.md#reservationutilizationgrouptypedef)
- [ResourceDetailsTypeDef](./type_defs.md#resourcedetailstypedef)
- [ResourceUtilizationTypeDef](./type_defs.md#resourceutilizationtypedef)
- [ResultByTimeTypeDef](./type_defs.md#resultbytimetypedef)
- [RightsizingRecommendationConfigurationTypeDef](./type_defs.md#rightsizingrecommendationconfigurationtypedef)
- [RightsizingRecommendationMetadataTypeDef](./type_defs.md#rightsizingrecommendationmetadatatypedef)
- [RightsizingRecommendationSummaryTypeDef](./type_defs.md#rightsizingrecommendationsummarytypedef)
- [RightsizingRecommendationTypeDef](./type_defs.md#rightsizingrecommendationtypedef)
- [RootCauseTypeDef](./type_defs.md#rootcausetypedef)
- [SavingsPlansAmortizedCommitmentTypeDef](./type_defs.md#savingsplansamortizedcommitmenttypedef)
- [SavingsPlansCoverageDataTypeDef](./type_defs.md#savingsplanscoveragedatatypedef)
- [SavingsPlansCoverageTypeDef](./type_defs.md#savingsplanscoveragetypedef)
- [SavingsPlansDetailsTypeDef](./type_defs.md#savingsplansdetailstypedef)
- [SavingsPlansPurchaseRecommendationDetailTypeDef](./type_defs.md#savingsplanspurchaserecommendationdetailtypedef)
- [SavingsPlansPurchaseRecommendationMetadataTypeDef](./type_defs.md#savingsplanspurchaserecommendationmetadatatypedef)
- [SavingsPlansPurchaseRecommendationSummaryTypeDef](./type_defs.md#savingsplanspurchaserecommendationsummarytypedef)
- [SavingsPlansPurchaseRecommendationTypeDef](./type_defs.md#savingsplanspurchaserecommendationtypedef)
- [SavingsPlansSavingsTypeDef](./type_defs.md#savingsplanssavingstypedef)
- [SavingsPlansUtilizationAggregatesTypeDef](./type_defs.md#savingsplansutilizationaggregatestypedef)
- [SavingsPlansUtilizationByTimeTypeDef](./type_defs.md#savingsplansutilizationbytimetypedef)
- [SavingsPlansUtilizationDetailTypeDef](./type_defs.md#savingsplansutilizationdetailtypedef)
- [SavingsPlansUtilizationTypeDef](./type_defs.md#savingsplansutilizationtypedef)
- [ServiceSpecificationTypeDef](./type_defs.md#servicespecificationtypedef)
- [SubscriberTypeDef](./type_defs.md#subscribertypedef)
- [TagValuesTypeDef](./type_defs.md#tagvaluestypedef)
- [TargetInstanceTypeDef](./type_defs.md#targetinstancetypedef)
- [TerminateRecommendationDetailTypeDef](./type_defs.md#terminaterecommendationdetailtypedef)
- [UtilizationByTimeTypeDef](./type_defs.md#utilizationbytimetypedef)
- [AnomalyDateIntervalTypeDef](./type_defs.md#anomalydateintervaltypedef)
- [CreateAnomalyMonitorResponseTypeDef](./type_defs.md#createanomalymonitorresponsetypedef)
- [CreateAnomalySubscriptionResponseTypeDef](./type_defs.md#createanomalysubscriptionresponsetypedef)
- [CreateCostCategoryDefinitionResponseTypeDef](./type_defs.md#createcostcategorydefinitionresponsetypedef)
- [DeleteCostCategoryDefinitionResponseTypeDef](./type_defs.md#deletecostcategorydefinitionresponsetypedef)
- [DescribeCostCategoryDefinitionResponseTypeDef](./type_defs.md#describecostcategorydefinitionresponsetypedef)
- [ExpressionTypeDef](./type_defs.md#expressiontypedef)
- [GetAnomaliesResponseTypeDef](./type_defs.md#getanomaliesresponsetypedef)
- [GetAnomalyMonitorsResponseTypeDef](./type_defs.md#getanomalymonitorsresponsetypedef)
- [GetAnomalySubscriptionsResponseTypeDef](./type_defs.md#getanomalysubscriptionsresponsetypedef)
- [GetCostAndUsageResponseTypeDef](./type_defs.md#getcostandusageresponsetypedef)
- [GetCostAndUsageWithResourcesResponseTypeDef](./type_defs.md#getcostandusagewithresourcesresponsetypedef)
- [GetCostCategoriesResponseTypeDef](./type_defs.md#getcostcategoriesresponsetypedef)
- [GetCostForecastResponseTypeDef](./type_defs.md#getcostforecastresponsetypedef)
- [GetDimensionValuesResponseTypeDef](./type_defs.md#getdimensionvaluesresponsetypedef)
- [GetReservationCoverageResponseTypeDef](./type_defs.md#getreservationcoverageresponsetypedef)
- [GetReservationPurchaseRecommendationResponseTypeDef](./type_defs.md#getreservationpurchaserecommendationresponsetypedef)
- [GetReservationUtilizationResponseTypeDef](./type_defs.md#getreservationutilizationresponsetypedef)
- [GetRightsizingRecommendationResponseTypeDef](./type_defs.md#getrightsizingrecommendationresponsetypedef)
- [GetSavingsPlansCoverageResponseTypeDef](./type_defs.md#getsavingsplanscoverageresponsetypedef)
- [GetSavingsPlansPurchaseRecommendationResponseTypeDef](./type_defs.md#getsavingsplanspurchaserecommendationresponsetypedef)
- [GetSavingsPlansUtilizationDetailsResponseTypeDef](./type_defs.md#getsavingsplansutilizationdetailsresponsetypedef)
- [GetSavingsPlansUtilizationResponseTypeDef](./type_defs.md#getsavingsplansutilizationresponsetypedef)
- [GetTagsResponseTypeDef](./type_defs.md#gettagsresponsetypedef)
- [GetUsageForecastResponseTypeDef](./type_defs.md#getusageforecastresponsetypedef)
- [ListCostCategoryDefinitionsResponseTypeDef](./type_defs.md#listcostcategorydefinitionsresponsetypedef)
- [ProvideAnomalyFeedbackResponseTypeDef](./type_defs.md#provideanomalyfeedbackresponsetypedef)
- [SortDefinitionTypeDef](./type_defs.md#sortdefinitiontypedef)
- [TotalImpactFilterTypeDef](./type_defs.md#totalimpactfiltertypedef)
- [UpdateAnomalyMonitorResponseTypeDef](./type_defs.md#updateanomalymonitorresponsetypedef)
- [UpdateAnomalySubscriptionResponseTypeDef](./type_defs.md#updateanomalysubscriptionresponsetypedef)
- [UpdateCostCategoryDefinitionResponseTypeDef](./type_defs.md#updatecostcategorydefinitionresponsetypedef)
