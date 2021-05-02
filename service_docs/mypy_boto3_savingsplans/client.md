# SavingsPlansClient for boto3 SavingsPlans module

> [Index](../index.md) > [SavingsPlans](./index.md) > SavingsPlansClient

Auto-generated documentation for [SavingsPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans)
type annotations stubs module [mypy_boto3_savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/).

- [SavingsPlansClient for boto3 SavingsPlans module](#savingsplansclient-for-boto3-savingsplans-module)
  - [SavingsPlansClient](#savingsplansclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_savings_plan](#create_savings_plan)
    - [delete_queued_savings_plan](#delete_queued_savings_plan)
    - [describe_savings_plan_rates](#describe_savings_plan_rates)
    - [describe_savings_plans](#describe_savings_plans)
    - [describe_savings_plans_offering_rates](#describe_savings_plans_offering_rates)
    - [describe_savings_plans_offerings](#describe_savings_plans_offerings)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)

## SavingsPlansClient

Type annotations for `boto3.client("savingsplans")`

Can be used directly:

```python
from mypy_boto3_savingsplans.client import SavingsPlansClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_savingsplans.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("savingsplans").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_savings_plan

Type annotations for `boto3.client("savingsplans").create_savings_plan` method.

[Client.create_savings_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.create_savings_plan)

```python
def create_savings_plan(
    self,
    savingsPlanOfferingId: str,
    commitment: str,
    upfrontPaymentAmount: str = None,
    purchaseTime: datetime = None,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateSavingsPlanResponseTypeDef:
    pass
```

### delete_queued_savings_plan

Type annotations for `boto3.client("savingsplans").delete_queued_savings_plan` method.

[Client.delete_queued_savings_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.delete_queued_savings_plan)

```python
def delete_queued_savings_plan(
    self,
    savingsPlanId: str
) -> Dict[str, Any]:
    pass
```

### describe_savings_plan_rates

Type annotations for `boto3.client("savingsplans").describe_savings_plan_rates` method.

[Client.describe_savings_plan_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plan_rates)

```python
def describe_savings_plan_rates(
    self,
    savingsPlanId: str,
    filters: List[SavingsPlanRateFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeSavingsPlanRatesResponseTypeDef:
    pass
```

### describe_savings_plans

Type annotations for `boto3.client("savingsplans").describe_savings_plans` method.

[Client.describe_savings_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans)

```python
def describe_savings_plans(
    self,
    savingsPlanArns: List[str] = None,
    savingsPlanIds: List[str] = None,
    nextToken: str = None,
    maxResults: int = None,
    states: List[SavingsPlanState] = None,
    filters: List[SavingsPlanFilterTypeDef] = None
) -> DescribeSavingsPlansResponseTypeDef:
    pass
```

### describe_savings_plans_offering_rates

Type annotations for `boto3.client("savingsplans").describe_savings_plans_offering_rates` method.

[Client.describe_savings_plans_offering_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offering_rates)

```python
def describe_savings_plans_offering_rates(
    self,
    savingsPlanOfferingIds: List[str] = None,
    savingsPlanPaymentOptions: List[SavingsPlanPaymentOption] = None,
    savingsPlanTypes: List[SavingsPlanType] = None,
    products: List[SavingsPlanProductType] = None,
    serviceCodes: List[SavingsPlanRateServiceCode] = None,
    usageTypes: List[str] = None,
    operations: List[str] = None,
    filters: List[SavingsPlanOfferingRateFilterElementTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeSavingsPlansOfferingRatesResponseTypeDef:
    pass
```

### describe_savings_plans_offerings

Type annotations for `boto3.client("savingsplans").describe_savings_plans_offerings` method.

[Client.describe_savings_plans_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offerings)

```python
def describe_savings_plans_offerings(
    self,
    offeringIds: List[str] = None,
    paymentOptions: List[SavingsPlanPaymentOption] = None,
    productType: SavingsPlanProductType = None,
    planTypes: List[SavingsPlanType] = None,
    durations: List[int] = None,
    currencies: List[CurrencyCode] = None,
    descriptions: List[str] = None,
    serviceCodes: List[str] = None,
    usageTypes: List[str] = None,
    operations: List[str] = None,
    filters: List[SavingsPlanOfferingFilterElementTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeSavingsPlansOfferingsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("savingsplans").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.generate_presigned_url)

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

### list_tags_for_resource

Type annotations for `boto3.client("savingsplans").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("savingsplans").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("savingsplans").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```