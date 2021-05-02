# Literals for boto3 SavingsPlans module

> [Index](../index.md) > [SavingsPlans](./index.md) > Literals

Auto-generated documentation for [SavingsPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans)
type annotations stubs module [mypy_boto3_savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/).

- [Literals for boto3 SavingsPlans module](#literals-for-boto3-savingsplans-module)
  - [CurrencyCode](#currencycode)
  - [SavingsPlanOfferingFilterAttribute](#savingsplanofferingfilterattribute)
  - [SavingsPlanOfferingPropertyKey](#savingsplanofferingpropertykey)
  - [SavingsPlanPaymentOption](#savingsplanpaymentoption)
  - [SavingsPlanProductType](#savingsplanproducttype)
  - [SavingsPlanRateFilterAttribute](#savingsplanratefilterattribute)
  - [SavingsPlanRateFilterName](#savingsplanratefiltername)
  - [SavingsPlanRatePropertyKey](#savingsplanratepropertykey)
  - [SavingsPlanRateServiceCode](#savingsplanrateservicecode)
  - [SavingsPlanRateUnit](#savingsplanrateunit)
  - [SavingsPlanState](#savingsplanstate)
  - [SavingsPlanType](#savingsplantype)
  - [SavingsPlansFilterName](#savingsplansfiltername)

## CurrencyCode

```python
from mypy_boto3_savingsplans.literals import CurrencyCode
```

Values:

- `CNY`
- `USD`

## SavingsPlanOfferingFilterAttribute

```python
from mypy_boto3_savingsplans.literals import SavingsPlanOfferingFilterAttribute
```

Values:

- `instanceFamily`
- `region`

## SavingsPlanOfferingPropertyKey

```python
from mypy_boto3_savingsplans.literals import SavingsPlanOfferingPropertyKey
```

Values:

- `instanceFamily`
- `region`

## SavingsPlanPaymentOption

```python
from mypy_boto3_savingsplans.literals import SavingsPlanPaymentOption
```

Values:

- `All Upfront`
- `No Upfront`
- `Partial Upfront`

## SavingsPlanProductType

```python
from mypy_boto3_savingsplans.literals import SavingsPlanProductType
```

Values:

- `EC2`
- `Fargate`
- `Lambda`
- `SageMaker`

## SavingsPlanRateFilterAttribute

```python
from mypy_boto3_savingsplans.literals import SavingsPlanRateFilterAttribute
```

Values:

- `instanceFamily`
- `instanceType`
- `productDescription`
- `productId`
- `region`
- `tenancy`

## SavingsPlanRateFilterName

```python
from mypy_boto3_savingsplans.literals import SavingsPlanRateFilterName
```

Values:

- `instanceType`
- `operation`
- `productDescription`
- `productType`
- `region`
- `serviceCode`
- `tenancy`
- `usageType`

## SavingsPlanRatePropertyKey

```python
from mypy_boto3_savingsplans.literals import SavingsPlanRatePropertyKey
```

Values:

- `instanceFamily`
- `instanceType`
- `productDescription`
- `region`
- `tenancy`

## SavingsPlanRateServiceCode

```python
from mypy_boto3_savingsplans.literals import SavingsPlanRateServiceCode
```

Values:

- `AmazonEC2`
- `AmazonECS`
- `AmazonEKS`
- `AmazonSageMaker`
- `AWSLambda`

## SavingsPlanRateUnit

```python
from mypy_boto3_savingsplans.literals import SavingsPlanRateUnit
```

Values:

- `Hrs`
- `Lambda-GB-Second`
- `Request`

## SavingsPlanState

```python
from mypy_boto3_savingsplans.literals import SavingsPlanState
```

Values:

- `active`
- `payment-failed`
- `payment-pending`
- `queued`
- `queued-deleted`
- `retired`

## SavingsPlanType

```python
from mypy_boto3_savingsplans.literals import SavingsPlanType
```

Values:

- `Compute`
- `EC2Instance`
- `SageMaker`

## SavingsPlansFilterName

```python
from mypy_boto3_savingsplans.literals import SavingsPlansFilterName
```

Values:

- `commitment`
- `ec2-instance-family`
- `end`
- `payment-option`
- `region`
- `savings-plan-type`
- `start`
- `term`
- `upfront`
