# Literals for boto3 CostExplorer module

> [Index](../index.md) > [CostExplorer](./index.md) > Literals

Auto-generated documentation for [CostExplorer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer)
type annotations stubs module [mypy_boto3_ce](https://pypi.org/project/mypy-boto3-ce/).

- [Literals for boto3 CostExplorer module](#literals-for-boto3-costexplorer-module)
  - [AccountScope](#accountscope)
  - [AnomalyFeedbackType](#anomalyfeedbacktype)
  - [AnomalySubscriptionFrequency](#anomalysubscriptionfrequency)
  - [Context](#context)
  - [CostCategoryInheritedValueDimensionName](#costcategoryinheritedvaluedimensionname)
  - [CostCategoryRuleType](#costcategoryruletype)
  - [CostCategoryRuleVersion](#costcategoryruleversion)
  - [CostCategoryStatus](#costcategorystatus)
  - [CostCategoryStatusComponent](#costcategorystatuscomponent)
  - [Dimension](#dimension)
  - [Granularity](#granularity)
  - [GroupDefinitionType](#groupdefinitiontype)
  - [LookbackPeriodInDays](#lookbackperiodindays)
  - [MatchOption](#matchoption)
  - [Metric](#metric)
  - [MonitorDimension](#monitordimension)
  - [MonitorType](#monitortype)
  - [NumericOperator](#numericoperator)
  - [OfferingClass](#offeringclass)
  - [PaymentOption](#paymentoption)
  - [RecommendationTarget](#recommendationtarget)
  - [RightsizingType](#rightsizingtype)
  - [SavingsPlansDataType](#savingsplansdatatype)
  - [SortOrder](#sortorder)
  - [SubscriberStatus](#subscriberstatus)
  - [SubscriberType](#subscribertype)
  - [SupportedSavingsPlansType](#supportedsavingsplanstype)
  - [TermInYears](#terminyears)

## AccountScope

```python
from mypy_boto3_ce.literals import AccountScope
```

Values:

- `LINKED`
- `PAYER`

## AnomalyFeedbackType

```python
from mypy_boto3_ce.literals import AnomalyFeedbackType
```

Values:

- `NO`
- `PLANNED_ACTIVITY`
- `YES`

## AnomalySubscriptionFrequency

```python
from mypy_boto3_ce.literals import AnomalySubscriptionFrequency
```

Values:

- `DAILY`
- `IMMEDIATE`
- `WEEKLY`

## Context

```python
from mypy_boto3_ce.literals import Context
```

Values:

- `COST_AND_USAGE`
- `RESERVATIONS`
- `SAVINGS_PLANS`

## CostCategoryInheritedValueDimensionName

```python
from mypy_boto3_ce.literals import CostCategoryInheritedValueDimensionName
```

Values:

- `LINKED_ACCOUNT_NAME`
- `TAG`

## CostCategoryRuleType

```python
from mypy_boto3_ce.literals import CostCategoryRuleType
```

Values:

- `INHERITED_VALUE`
- `REGULAR`

## CostCategoryRuleVersion

```python
from mypy_boto3_ce.literals import CostCategoryRuleVersion
```

Values:

- `CostCategoryExpression.v1`

## CostCategoryStatus

```python
from mypy_boto3_ce.literals import CostCategoryStatus
```

Values:

- `APPLIED`
- `PROCESSING`

## CostCategoryStatusComponent

```python
from mypy_boto3_ce.literals import CostCategoryStatusComponent
```

Values:

- `COST_EXPLORER`

## Dimension

```python
from mypy_boto3_ce.literals import Dimension
```

Values:

- `AGREEMENT_END_DATE_TIME_AFTER`
- `AGREEMENT_END_DATE_TIME_BEFORE`
- `AZ`
- `BILLING_ENTITY`
- `CACHE_ENGINE`
- `DATABASE_ENGINE`
- `DEPLOYMENT_OPTION`
- `INSTANCE_TYPE`
- `INSTANCE_TYPE_FAMILY`
- `LEGAL_ENTITY_NAME`
- `LINKED_ACCOUNT`
- `LINKED_ACCOUNT_NAME`
- `OPERATING_SYSTEM`
- `OPERATION`
- `PAYMENT_OPTION`
- `PLATFORM`
- `PURCHASE_TYPE`
- `RECORD_TYPE`
- `REGION`
- `RESERVATION_ID`
- `RESOURCE_ID`
- `RIGHTSIZING_TYPE`
- `SAVINGS_PLAN_ARN`
- `SAVINGS_PLANS_TYPE`
- `SCOPE`
- `SERVICE`
- `SERVICE_CODE`
- `SUBSCRIPTION_ID`
- `TENANCY`
- `USAGE_TYPE`
- `USAGE_TYPE_GROUP`

## Granularity

```python
from mypy_boto3_ce.literals import Granularity
```

Values:

- `DAILY`
- `HOURLY`
- `MONTHLY`

## GroupDefinitionType

```python
from mypy_boto3_ce.literals import GroupDefinitionType
```

Values:

- `COST_CATEGORY`
- `DIMENSION`
- `TAG`

## LookbackPeriodInDays

```python
from mypy_boto3_ce.literals import LookbackPeriodInDays
```

Values:

- `SEVEN_DAYS`
- `SIXTY_DAYS`
- `THIRTY_DAYS`

## MatchOption

```python
from mypy_boto3_ce.literals import MatchOption
```

Values:

- `ABSENT`
- `CASE_INSENSITIVE`
- `CASE_SENSITIVE`
- `CONTAINS`
- `ENDS_WITH`
- `EQUALS`
- `STARTS_WITH`

## Metric

```python
from mypy_boto3_ce.literals import Metric
```

Values:

- `AMORTIZED_COST`
- `BLENDED_COST`
- `NET_AMORTIZED_COST`
- `NET_UNBLENDED_COST`
- `NORMALIZED_USAGE_AMOUNT`
- `UNBLENDED_COST`
- `USAGE_QUANTITY`

## MonitorDimension

```python
from mypy_boto3_ce.literals import MonitorDimension
```

Values:

- `SERVICE`

## MonitorType

```python
from mypy_boto3_ce.literals import MonitorType
```

Values:

- `CUSTOM`
- `DIMENSIONAL`

## NumericOperator

```python
from mypy_boto3_ce.literals import NumericOperator
```

Values:

- `BETWEEN`
- `EQUAL`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL`

## OfferingClass

```python
from mypy_boto3_ce.literals import OfferingClass
```

Values:

- `CONVERTIBLE`
- `STANDARD`

## PaymentOption

```python
from mypy_boto3_ce.literals import PaymentOption
```

Values:

- `ALL_UPFRONT`
- `HEAVY_UTILIZATION`
- `LIGHT_UTILIZATION`
- `MEDIUM_UTILIZATION`
- `NO_UPFRONT`
- `PARTIAL_UPFRONT`

## RecommendationTarget

```python
from mypy_boto3_ce.literals import RecommendationTarget
```

Values:

- `CROSS_INSTANCE_FAMILY`
- `SAME_INSTANCE_FAMILY`

## RightsizingType

```python
from mypy_boto3_ce.literals import RightsizingType
```

Values:

- `MODIFY`
- `TERMINATE`

## SavingsPlansDataType

```python
from mypy_boto3_ce.literals import SavingsPlansDataType
```

Values:

- `AMORTIZED_COMMITMENT`
- `ATTRIBUTES`
- `SAVINGS`
- `UTILIZATION`

## SortOrder

```python
from mypy_boto3_ce.literals import SortOrder
```

Values:

- `ASCENDING`
- `DESCENDING`

## SubscriberStatus

```python
from mypy_boto3_ce.literals import SubscriberStatus
```

Values:

- `CONFIRMED`
- `DECLINED`

## SubscriberType

```python
from mypy_boto3_ce.literals import SubscriberType
```

Values:

- `EMAIL`
- `SNS`

## SupportedSavingsPlansType

```python
from mypy_boto3_ce.literals import SupportedSavingsPlansType
```

Values:

- `COMPUTE_SP`
- `EC2_INSTANCE_SP`
- `SAGEMAKER_SP`

## TermInYears

```python
from mypy_boto3_ce.literals import TermInYears
```

Values:

- `ONE_YEAR`
- `THREE_YEARS`
