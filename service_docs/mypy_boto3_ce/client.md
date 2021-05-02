# CostExplorerClient for boto3 CostExplorer module

> [Index](../index.md) > [CostExplorer](./index.md) > CostExplorerClient

Auto-generated documentation for [CostExplorer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer)
type annotations stubs module [mypy_boto3_ce](https://pypi.org/project/mypy-boto3-ce/).

- [CostExplorerClient for boto3 CostExplorer module](#costexplorerclient-for-boto3-costexplorer-module)
  - [CostExplorerClient](#costexplorerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_anomaly_monitor](#create_anomaly_monitor)
    - [create_anomaly_subscription](#create_anomaly_subscription)
    - [create_cost_category_definition](#create_cost_category_definition)
    - [delete_anomaly_monitor](#delete_anomaly_monitor)
    - [delete_anomaly_subscription](#delete_anomaly_subscription)
    - [delete_cost_category_definition](#delete_cost_category_definition)
    - [describe_cost_category_definition](#describe_cost_category_definition)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_anomalies](#get_anomalies)
    - [get_anomaly_monitors](#get_anomaly_monitors)
    - [get_anomaly_subscriptions](#get_anomaly_subscriptions)
    - [get_cost_and_usage](#get_cost_and_usage)
    - [get_cost_and_usage_with_resources](#get_cost_and_usage_with_resources)
    - [get_cost_categories](#get_cost_categories)
    - [get_cost_forecast](#get_cost_forecast)
    - [get_dimension_values](#get_dimension_values)
    - [get_reservation_coverage](#get_reservation_coverage)
    - [get_reservation_purchase_recommendation](#get_reservation_purchase_recommendation)
    - [get_reservation_utilization](#get_reservation_utilization)
    - [get_rightsizing_recommendation](#get_rightsizing_recommendation)
    - [get_savings_plans_coverage](#get_savings_plans_coverage)
    - [get_savings_plans_purchase_recommendation](#get_savings_plans_purchase_recommendation)
    - [get_savings_plans_utilization](#get_savings_plans_utilization)
    - [get_savings_plans_utilization_details](#get_savings_plans_utilization_details)
    - [get_tags](#get_tags)
    - [get_usage_forecast](#get_usage_forecast)
    - [list_cost_category_definitions](#list_cost_category_definitions)
    - [provide_anomaly_feedback](#provide_anomaly_feedback)
    - [update_anomaly_monitor](#update_anomaly_monitor)
    - [update_anomaly_subscription](#update_anomaly_subscription)
    - [update_cost_category_definition](#update_cost_category_definition)

## CostExplorerClient

Type annotations for `boto3.client("ce")`

Can be used directly:

```python
from mypy_boto3_ce.client import CostExplorerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ce.client import Exceptions

def handle_error(exc: Exceptions.BillExpirationException) -> None:
    ...
```


Exceptions:

- `Exceptions.BillExpirationException`
- `Exceptions.ClientError`
- `Exceptions.DataUnavailableException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.RequestChangedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.UnknownMonitorException`
- `Exceptions.UnknownSubscriptionException`
- `Exceptions.UnresolvableUsageUnitException`


## Methods


### can_paginate

Type annotations for `boto3.client("ce").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_anomaly_monitor

Type annotations for `boto3.client("ce").create_anomaly_monitor` method.

[Client.create_anomaly_monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.create_anomaly_monitor)

```python
def create_anomaly_monitor(
    self,
    AnomalyMonitor: "AnomalyMonitorTypeDef"
) -> CreateAnomalyMonitorResponseTypeDef:
    pass
```

### create_anomaly_subscription

Type annotations for `boto3.client("ce").create_anomaly_subscription` method.

[Client.create_anomaly_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.create_anomaly_subscription)

```python
def create_anomaly_subscription(
    self,
    AnomalySubscription: "AnomalySubscriptionTypeDef"
) -> CreateAnomalySubscriptionResponseTypeDef:
    pass
```

### create_cost_category_definition

Type annotations for `boto3.client("ce").create_cost_category_definition` method.

[Client.create_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)

```python
def create_cost_category_definition(
    self,
    Name: str,
    RuleVersion: CostCategoryRuleVersion,
    Rules: List["CostCategoryRuleTypeDef"],
    DefaultValue: str = None
) -> CreateCostCategoryDefinitionResponseTypeDef:
    pass
```

### delete_anomaly_monitor

Type annotations for `boto3.client("ce").delete_anomaly_monitor` method.

[Client.delete_anomaly_monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.delete_anomaly_monitor)

```python
def delete_anomaly_monitor(
    self,
    MonitorArn: str
) -> Dict[str, Any]:
    pass
```

### delete_anomaly_subscription

Type annotations for `boto3.client("ce").delete_anomaly_subscription` method.

[Client.delete_anomaly_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.delete_anomaly_subscription)

```python
def delete_anomaly_subscription(
    self,
    SubscriptionArn: str
) -> Dict[str, Any]:
    pass
```

### delete_cost_category_definition

Type annotations for `boto3.client("ce").delete_cost_category_definition` method.

[Client.delete_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)

```python
def delete_cost_category_definition(
    self,
    CostCategoryArn: str
) -> DeleteCostCategoryDefinitionResponseTypeDef:
    pass
```

### describe_cost_category_definition

Type annotations for `boto3.client("ce").describe_cost_category_definition` method.

[Client.describe_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)

```python
def describe_cost_category_definition(
    self,
    CostCategoryArn: str,
    EffectiveOn: str = None
) -> DescribeCostCategoryDefinitionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ce").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)

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

### get_anomalies

Type annotations for `boto3.client("ce").get_anomalies` method.

[Client.get_anomalies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_anomalies)

```python
def get_anomalies(
    self,
    DateInterval: AnomalyDateIntervalTypeDef,
    MonitorArn: str = None,
    Feedback: AnomalyFeedbackType = None,
    TotalImpact: TotalImpactFilterTypeDef = None,
    NextPageToken: str = None,
    MaxResults: int = None
) -> GetAnomaliesResponseTypeDef:
    pass
```

### get_anomaly_monitors

Type annotations for `boto3.client("ce").get_anomaly_monitors` method.

[Client.get_anomaly_monitors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_anomaly_monitors)

```python
def get_anomaly_monitors(
    self,
    MonitorArnList: List[str] = None,
    NextPageToken: str = None,
    MaxResults: int = None
) -> GetAnomalyMonitorsResponseTypeDef:
    pass
```

### get_anomaly_subscriptions

Type annotations for `boto3.client("ce").get_anomaly_subscriptions` method.

[Client.get_anomaly_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_anomaly_subscriptions)

```python
def get_anomaly_subscriptions(
    self,
    SubscriptionArnList: List[str] = None,
    MonitorArn: str = None,
    NextPageToken: str = None,
    MaxResults: int = None
) -> GetAnomalySubscriptionsResponseTypeDef:
    pass
```

### get_cost_and_usage

Type annotations for `boto3.client("ce").get_cost_and_usage` method.

[Client.get_cost_and_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)

```python
def get_cost_and_usage(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Granularity: Granularity,
    Metrics: List[str],
    Filter: Dict[str, Any] = None,
    GroupBy: List["GroupDefinitionTypeDef"] = None,
    NextPageToken: str = None
) -> GetCostAndUsageResponseTypeDef:
    pass
```

### get_cost_and_usage_with_resources

Type annotations for `boto3.client("ce").get_cost_and_usage_with_resources` method.

[Client.get_cost_and_usage_with_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)

```python
def get_cost_and_usage_with_resources(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Granularity: Granularity,
    Filter: Dict[str, Any],
    Metrics: List[str] = None,
    GroupBy: List["GroupDefinitionTypeDef"] = None,
    NextPageToken: str = None
) -> GetCostAndUsageWithResourcesResponseTypeDef:
    pass
```

### get_cost_categories

Type annotations for `boto3.client("ce").get_cost_categories` method.

[Client.get_cost_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_categories)

```python
def get_cost_categories(
    self,
    TimePeriod: "DateIntervalTypeDef",
    SearchString: str = None,
    CostCategoryName: str = None,
    Filter: Dict[str, Any] = None,
    SortBy: List[SortDefinitionTypeDef] = None,
    MaxResults: int = None,
    NextPageToken: str = None
) -> GetCostCategoriesResponseTypeDef:
    pass
```

### get_cost_forecast

Type annotations for `boto3.client("ce").get_cost_forecast` method.

[Client.get_cost_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)

```python
def get_cost_forecast(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Metric: Metric,
    Granularity: Granularity,
    Filter: Dict[str, Any] = None,
    PredictionIntervalLevel: int = None
) -> GetCostForecastResponseTypeDef:
    pass
```

### get_dimension_values

Type annotations for `boto3.client("ce").get_dimension_values` method.

[Client.get_dimension_values documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_dimension_values)

```python
def get_dimension_values(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Dimension: Dimension,
    SearchString: str = None,
    Context: Context = None,
    Filter: Dict[str, Any] = None,
    SortBy: List[SortDefinitionTypeDef] = None,
    MaxResults: int = None,
    NextPageToken: str = None
) -> GetDimensionValuesResponseTypeDef:
    pass
```

### get_reservation_coverage

Type annotations for `boto3.client("ce").get_reservation_coverage` method.

[Client.get_reservation_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)

```python
def get_reservation_coverage(
    self,
    TimePeriod: "DateIntervalTypeDef",
    GroupBy: List["GroupDefinitionTypeDef"] = None,
    Granularity: Granularity = None,
    Filter: Dict[str, Any] = None,
    Metrics: List[str] = None,
    NextPageToken: str = None,
    SortBy: SortDefinitionTypeDef = None,
    MaxResults: int = None
) -> GetReservationCoverageResponseTypeDef:
    pass
```

### get_reservation_purchase_recommendation

Type annotations for `boto3.client("ce").get_reservation_purchase_recommendation` method.

[Client.get_reservation_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)

```python
def get_reservation_purchase_recommendation(
    self,
    Service: str,
    AccountId: str = None,
    Filter: Dict[str, Any] = None,
    AccountScope: AccountScope = None,
    LookbackPeriodInDays: LookbackPeriodInDays = None,
    TermInYears: TermInYears = None,
    PaymentOption: PaymentOption = None,
    ServiceSpecification: "ServiceSpecificationTypeDef" = None,
    PageSize: int = None,
    NextPageToken: str = None
) -> GetReservationPurchaseRecommendationResponseTypeDef:
    pass
```

### get_reservation_utilization

Type annotations for `boto3.client("ce").get_reservation_utilization` method.

[Client.get_reservation_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)

```python
def get_reservation_utilization(
    self,
    TimePeriod: "DateIntervalTypeDef",
    GroupBy: List["GroupDefinitionTypeDef"] = None,
    Granularity: Granularity = None,
    Filter: Dict[str, Any] = None,
    SortBy: SortDefinitionTypeDef = None,
    NextPageToken: str = None,
    MaxResults: int = None
) -> GetReservationUtilizationResponseTypeDef:
    pass
```

### get_rightsizing_recommendation

Type annotations for `boto3.client("ce").get_rightsizing_recommendation` method.

[Client.get_rightsizing_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)

```python
def get_rightsizing_recommendation(
    self,
    Service: str,
    Filter: Dict[str, Any] = None,
    Configuration: "RightsizingRecommendationConfigurationTypeDef" = None,
    PageSize: int = None,
    NextPageToken: str = None
) -> GetRightsizingRecommendationResponseTypeDef:
    pass
```

### get_savings_plans_coverage

Type annotations for `boto3.client("ce").get_savings_plans_coverage` method.

[Client.get_savings_plans_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)

```python
def get_savings_plans_coverage(
    self,
    TimePeriod: "DateIntervalTypeDef",
    GroupBy: List["GroupDefinitionTypeDef"] = None,
    Granularity: Granularity = None,
    Filter: Dict[str, Any] = None,
    Metrics: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: SortDefinitionTypeDef = None
) -> GetSavingsPlansCoverageResponseTypeDef:
    pass
```

### get_savings_plans_purchase_recommendation

Type annotations for `boto3.client("ce").get_savings_plans_purchase_recommendation` method.

[Client.get_savings_plans_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)

```python
def get_savings_plans_purchase_recommendation(
    self,
    SavingsPlansType: SupportedSavingsPlansType,
    TermInYears: TermInYears,
    PaymentOption: PaymentOption,
    LookbackPeriodInDays: LookbackPeriodInDays,
    AccountScope: AccountScope = None,
    NextPageToken: str = None,
    PageSize: int = None,
    Filter: Dict[str, Any] = None
) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
    pass
```

### get_savings_plans_utilization

Type annotations for `boto3.client("ce").get_savings_plans_utilization` method.

[Client.get_savings_plans_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)

```python
def get_savings_plans_utilization(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Granularity: Granularity = None,
    Filter: Dict[str, Any] = None,
    SortBy: SortDefinitionTypeDef = None
) -> GetSavingsPlansUtilizationResponseTypeDef:
    pass
```

### get_savings_plans_utilization_details

Type annotations for `boto3.client("ce").get_savings_plans_utilization_details` method.

[Client.get_savings_plans_utilization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)

```python
def get_savings_plans_utilization_details(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Filter: Dict[str, Any] = None,
    DataType: List[SavingsPlansDataType] = None,
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: SortDefinitionTypeDef = None
) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
    pass
```

### get_tags

Type annotations for `boto3.client("ce").get_tags` method.

[Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_tags)

```python
def get_tags(
    self,
    TimePeriod: "DateIntervalTypeDef",
    SearchString: str = None,
    TagKey: str = None,
    Filter: Dict[str, Any] = None,
    SortBy: List[SortDefinitionTypeDef] = None,
    MaxResults: int = None,
    NextPageToken: str = None
) -> GetTagsResponseTypeDef:
    pass
```

### get_usage_forecast

Type annotations for `boto3.client("ce").get_usage_forecast` method.

[Client.get_usage_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)

```python
def get_usage_forecast(
    self,
    TimePeriod: "DateIntervalTypeDef",
    Metric: Metric,
    Granularity: Granularity,
    Filter: Dict[str, Any] = None,
    PredictionIntervalLevel: int = None
) -> GetUsageForecastResponseTypeDef:
    pass
```

### list_cost_category_definitions

Type annotations for `boto3.client("ce").list_cost_category_definitions` method.

[Client.list_cost_category_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)

```python
def list_cost_category_definitions(
    self,
    EffectiveOn: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListCostCategoryDefinitionsResponseTypeDef:
    pass
```

### provide_anomaly_feedback

Type annotations for `boto3.client("ce").provide_anomaly_feedback` method.

[Client.provide_anomaly_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.provide_anomaly_feedback)

```python
def provide_anomaly_feedback(
    self,
    AnomalyId: str,
    Feedback: AnomalyFeedbackType
) -> ProvideAnomalyFeedbackResponseTypeDef:
    pass
```

### update_anomaly_monitor

Type annotations for `boto3.client("ce").update_anomaly_monitor` method.

[Client.update_anomaly_monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_anomaly_monitor)

```python
def update_anomaly_monitor(
    self,
    MonitorArn: str,
    MonitorName: str = None
) -> UpdateAnomalyMonitorResponseTypeDef:
    pass
```

### update_anomaly_subscription

Type annotations for `boto3.client("ce").update_anomaly_subscription` method.

[Client.update_anomaly_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_anomaly_subscription)

```python
def update_anomaly_subscription(
    self,
    SubscriptionArn: str,
    Threshold: float = None,
    Frequency: AnomalySubscriptionFrequency = None,
    MonitorArnList: List[str] = None,
    Subscribers: List["SubscriberTypeDef"] = None,
    SubscriptionName: str = None
) -> UpdateAnomalySubscriptionResponseTypeDef:
    pass
```

### update_cost_category_definition

Type annotations for `boto3.client("ce").update_cost_category_definition` method.

[Client.update_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)

```python
def update_cost_category_definition(
    self,
    CostCategoryArn: str,
    RuleVersion: CostCategoryRuleVersion,
    Rules: List["CostCategoryRuleTypeDef"],
    DefaultValue: str = None
) -> UpdateCostCategoryDefinitionResponseTypeDef:
    pass
```