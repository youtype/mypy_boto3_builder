# Type annotations for boto3 SavingsPlans module

> [Index](../index.md) > SavingsPlans

Auto-generated documentation for [SavingsPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans)
type annotations stubs module [mypy_boto3_savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/).

```bash
pip install mypy-boto3-savingsplans
```

- [Type annotations for boto3 SavingsPlans module](#type-annotations-for-boto3-savingsplans-module)
  - [SavingsPlansClient](#savingsplansclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## SavingsPlansClient

Type annotations for  `boto3.client("savingsplans")` as [SavingsPlansClient](./client.md)

Can be used directly:

```python
from mypy_boto3_savingsplans.client import SavingsPlansClient
```


SavingsPlansClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_savings_plan](./client.md#create-savings-plan)
- [delete_queued_savings_plan](./client.md#delete-queued-savings-plan)
- [describe_savings_plan_rates](./client.md#describe-savings-plan-rates)
- [describe_savings_plans](./client.md#describe-savings-plans)
- [describe_savings_plans_offering_rates](./client.md#describe-savings-plans-offering-rates)
- [describe_savings_plans_offerings](./client.md#describe-savings-plans-offerings)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_savingsplans.literals import CurrencyCode, ...
```

- [CurrencyCode](./literals.md#currencycode)
- [SavingsPlanOfferingFilterAttribute](./literals.md#savingsplanofferingfilterattribute)
- [SavingsPlanOfferingPropertyKey](./literals.md#savingsplanofferingpropertykey)
- [SavingsPlanPaymentOption](./literals.md#savingsplanpaymentoption)
- [SavingsPlanProductType](./literals.md#savingsplanproducttype)
- [SavingsPlanRateFilterAttribute](./literals.md#savingsplanratefilterattribute)
- [SavingsPlanRateFilterName](./literals.md#savingsplanratefiltername)
- [SavingsPlanRatePropertyKey](./literals.md#savingsplanratepropertykey)
- [SavingsPlanRateServiceCode](./literals.md#savingsplanrateservicecode)
- [SavingsPlanRateUnit](./literals.md#savingsplanrateunit)
- [SavingsPlanState](./literals.md#savingsplanstate)
- [SavingsPlanType](./literals.md#savingsplantype)
- [SavingsPlansFilterName](./literals.md#savingsplansfiltername)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_savingsplans.type_defs import CreateSavingsPlanResponseTypeDef, ...
```

- [CreateSavingsPlanResponseTypeDef](./type_defs.md#createsavingsplanresponsetypedef)
- [DescribeSavingsPlanRatesResponseTypeDef](./type_defs.md#describesavingsplanratesresponsetypedef)
- [DescribeSavingsPlansOfferingRatesResponseTypeDef](./type_defs.md#describesavingsplansofferingratesresponsetypedef)
- [DescribeSavingsPlansOfferingsResponseTypeDef](./type_defs.md#describesavingsplansofferingsresponsetypedef)
- [DescribeSavingsPlansResponseTypeDef](./type_defs.md#describesavingsplansresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ParentSavingsPlanOfferingTypeDef](./type_defs.md#parentsavingsplanofferingtypedef)
- [SavingsPlanFilterTypeDef](./type_defs.md#savingsplanfiltertypedef)
- [SavingsPlanOfferingFilterElementTypeDef](./type_defs.md#savingsplanofferingfilterelementtypedef)
- [SavingsPlanOfferingPropertyTypeDef](./type_defs.md#savingsplanofferingpropertytypedef)
- [SavingsPlanOfferingRateFilterElementTypeDef](./type_defs.md#savingsplanofferingratefilterelementtypedef)
- [SavingsPlanOfferingRatePropertyTypeDef](./type_defs.md#savingsplanofferingratepropertytypedef)
- [SavingsPlanOfferingRateTypeDef](./type_defs.md#savingsplanofferingratetypedef)
- [SavingsPlanOfferingTypeDef](./type_defs.md#savingsplanofferingtypedef)
- [SavingsPlanRateFilterTypeDef](./type_defs.md#savingsplanratefiltertypedef)
- [SavingsPlanRatePropertyTypeDef](./type_defs.md#savingsplanratepropertytypedef)
- [SavingsPlanRateTypeDef](./type_defs.md#savingsplanratetypedef)
- [SavingsPlanTypeDef](./type_defs.md#savingsplantypedef)
