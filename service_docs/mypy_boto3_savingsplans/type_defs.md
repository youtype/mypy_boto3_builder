# Structures for boto3 SavingsPlans module

> [Index](../index.md) > [SavingsPlans](./index.md) > Structures

Auto-generated documentation for [SavingsPlans](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans)
type annotations stubs module [mypy_boto3_savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/).

- [Structures for boto3 SavingsPlans module](#structures-for-boto3-savingsplans-module)
  - [ParentSavingsPlanOfferingTypeDef](#parentsavingsplanofferingtypedef)
  - [SavingsPlanOfferingPropertyTypeDef](#savingsplanofferingpropertytypedef)
  - [SavingsPlanOfferingRatePropertyTypeDef](#savingsplanofferingratepropertytypedef)
  - [SavingsPlanOfferingRateTypeDef](#savingsplanofferingratetypedef)
  - [SavingsPlanOfferingTypeDef](#savingsplanofferingtypedef)
  - [SavingsPlanRatePropertyTypeDef](#savingsplanratepropertytypedef)
  - [SavingsPlanRateTypeDef](#savingsplanratetypedef)
  - [SavingsPlanTypeDef](#savingsplantypedef)
  - [CreateSavingsPlanResponseTypeDef](#createsavingsplanresponsetypedef)
  - [DescribeSavingsPlanRatesResponseTypeDef](#describesavingsplanratesresponsetypedef)
  - [DescribeSavingsPlansOfferingRatesResponseTypeDef](#describesavingsplansofferingratesresponsetypedef)
  - [DescribeSavingsPlansOfferingsResponseTypeDef](#describesavingsplansofferingsresponsetypedef)
  - [DescribeSavingsPlansResponseTypeDef](#describesavingsplansresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [SavingsPlanFilterTypeDef](#savingsplanfiltertypedef)
  - [SavingsPlanOfferingFilterElementTypeDef](#savingsplanofferingfilterelementtypedef)
  - [SavingsPlanOfferingRateFilterElementTypeDef](#savingsplanofferingratefilterelementtypedef)
  - [SavingsPlanRateFilterTypeDef](#savingsplanratefiltertypedef)

## ParentSavingsPlanOfferingTypeDef

```python
from mypy_boto3_savingsplans.type_defs import ParentSavingsPlanOfferingTypeDef
```




Optional fields:
- `offeringId`: `str`
- `paymentOption`: `SavingsPlanPaymentOption`
- `planType`: `SavingsPlanType`
- `durationSeconds`: `int`
- `currency`: `CurrencyCode`
- `planDescription`: `str`


## SavingsPlanOfferingPropertyTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanOfferingPropertyTypeDef
```




Optional fields:
- `name`: `SavingsPlanOfferingPropertyKey`
- `value`: `str`


## SavingsPlanOfferingRatePropertyTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanOfferingRatePropertyTypeDef
```




Optional fields:
- `name`: `str`
- `value`: `str`


## SavingsPlanOfferingRateTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanOfferingRateTypeDef
```




Optional fields:
- `savingsPlanOffering`: `"ParentSavingsPlanOfferingTypeDef"`
- `rate`: `str`
- `unit`: `SavingsPlanRateUnit`
- `productType`: `SavingsPlanProductType`
- `serviceCode`: `SavingsPlanRateServiceCode`
- `usageType`: `str`
- `operation`: `str`
- `properties`: `List["SavingsPlanOfferingRatePropertyTypeDef"]`


## SavingsPlanOfferingTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanOfferingTypeDef
```




Optional fields:
- `offeringId`: `str`
- `productTypes`: `List[SavingsPlanProductType]`
- `planType`: `SavingsPlanType`
- `description`: `str`
- `paymentOption`: `SavingsPlanPaymentOption`
- `durationSeconds`: `int`
- `currency`: `CurrencyCode`
- `serviceCode`: `str`
- `usageType`: `str`
- `operation`: `str`
- `properties`: `List["SavingsPlanOfferingPropertyTypeDef"]`


## SavingsPlanRatePropertyTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanRatePropertyTypeDef
```




Optional fields:
- `name`: `SavingsPlanRatePropertyKey`
- `value`: `str`


## SavingsPlanRateTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanRateTypeDef
```




Optional fields:
- `rate`: `str`
- `currency`: `CurrencyCode`
- `unit`: `SavingsPlanRateUnit`
- `productType`: `SavingsPlanProductType`
- `serviceCode`: `SavingsPlanRateServiceCode`
- `usageType`: `str`
- `operation`: `str`
- `properties`: `List["SavingsPlanRatePropertyTypeDef"]`


## SavingsPlanTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanTypeDef
```




Optional fields:
- `offeringId`: `str`
- `savingsPlanId`: `str`
- `savingsPlanArn`: `str`
- `description`: `str`
- `start`: `str`
- `end`: `str`
- `state`: `SavingsPlanState`
- `region`: `str`
- `ec2InstanceFamily`: `str`
- `savingsPlanType`: `SavingsPlanType`
- `paymentOption`: `SavingsPlanPaymentOption`
- `productTypes`: `List[SavingsPlanProductType]`
- `currency`: `CurrencyCode`
- `commitment`: `str`
- `upfrontPaymentAmount`: `str`
- `recurringPaymentAmount`: `str`
- `termDurationInSeconds`: `int`
- `tags`: `Dict[str, str]`


## CreateSavingsPlanResponseTypeDef

```python
from mypy_boto3_savingsplans.type_defs import CreateSavingsPlanResponseTypeDef
```




Optional fields:
- `savingsPlanId`: `str`


## DescribeSavingsPlanRatesResponseTypeDef

```python
from mypy_boto3_savingsplans.type_defs import DescribeSavingsPlanRatesResponseTypeDef
```




Optional fields:
- `savingsPlanId`: `str`
- `searchResults`: `List["SavingsPlanRateTypeDef"]`
- `nextToken`: `str`


## DescribeSavingsPlansOfferingRatesResponseTypeDef

```python
from mypy_boto3_savingsplans.type_defs import DescribeSavingsPlansOfferingRatesResponseTypeDef
```




Optional fields:
- `searchResults`: `List["SavingsPlanOfferingRateTypeDef"]`
- `nextToken`: `str`


## DescribeSavingsPlansOfferingsResponseTypeDef

```python
from mypy_boto3_savingsplans.type_defs import DescribeSavingsPlansOfferingsResponseTypeDef
```




Optional fields:
- `searchResults`: `List["SavingsPlanOfferingTypeDef"]`
- `nextToken`: `str`


## DescribeSavingsPlansResponseTypeDef

```python
from mypy_boto3_savingsplans.type_defs import DescribeSavingsPlansResponseTypeDef
```




Optional fields:
- `savingsPlans`: `List["SavingsPlanTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_savingsplans.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## SavingsPlanFilterTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanFilterTypeDef
```




Optional fields:
- `name`: `SavingsPlansFilterName`
- `values`: `List[str]`


## SavingsPlanOfferingFilterElementTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanOfferingFilterElementTypeDef
```




Optional fields:
- `name`: `SavingsPlanOfferingFilterAttribute`
- `values`: `List[str]`


## SavingsPlanOfferingRateFilterElementTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanOfferingRateFilterElementTypeDef
```




Optional fields:
- `name`: `SavingsPlanRateFilterAttribute`
- `values`: `List[str]`


## SavingsPlanRateFilterTypeDef

```python
from mypy_boto3_savingsplans.type_defs import SavingsPlanRateFilterTypeDef
```




Optional fields:
- `name`: `SavingsPlanRateFilterName`
- `values`: `List[str]`

