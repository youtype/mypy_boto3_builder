# Structures for boto3 MarketplaceMetering module

> [Index](../index.md) > [MarketplaceMetering](./index.md) > Structures

Auto-generated documentation for [MarketplaceMetering](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering)
type annotations stubs module [mypy_boto3_meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace/).

- [Structures for boto3 MarketplaceMetering module](#structures-for-boto3-marketplacemetering-module)
  - [TagTypeDef](#tagtypedef)
  - [UsageAllocationTypeDef](#usageallocationtypedef)
  - [UsageRecordResultTypeDef](#usagerecordresulttypedef)
  - [UsageRecordTypeDef](#usagerecordtypedef)
  - [BatchMeterUsageResultTypeDef](#batchmeterusageresulttypedef)
  - [MeterUsageResultTypeDef](#meterusageresulttypedef)
  - [RegisterUsageResultTypeDef](#registerusageresulttypedef)
  - [ResolveCustomerResultTypeDef](#resolvecustomerresulttypedef)

## TagTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UsageAllocationTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import UsageAllocationTypeDef
```


Required fields:
- `AllocatedUsageQuantity`: `int`



Optional fields:
- `Tags`: `List["TagTypeDef"]`


## UsageRecordResultTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import UsageRecordResultTypeDef
```




Optional fields:
- `UsageRecord`: `"UsageRecordTypeDef"`
- `MeteringRecordId`: `str`
- `Status`: `UsageRecordResultStatus`


## UsageRecordTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import UsageRecordTypeDef
```


Required fields:
- `Timestamp`: `datetime`
- `CustomerIdentifier`: `str`
- `Dimension`: `str`



Optional fields:
- `Quantity`: `int`
- `UsageAllocations`: `List["UsageAllocationTypeDef"]`


## BatchMeterUsageResultTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import BatchMeterUsageResultTypeDef
```




Optional fields:
- `Results`: `List["UsageRecordResultTypeDef"]`
- `UnprocessedRecords`: `List["UsageRecordTypeDef"]`


## MeterUsageResultTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import MeterUsageResultTypeDef
```




Optional fields:
- `MeteringRecordId`: `str`


## RegisterUsageResultTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import RegisterUsageResultTypeDef
```




Optional fields:
- `PublicKeyRotationTimestamp`: `datetime`
- `Signature`: `str`


## ResolveCustomerResultTypeDef

```python
from mypy_boto3_meteringmarketplace.type_defs import ResolveCustomerResultTypeDef
```




Optional fields:
- `CustomerIdentifier`: `str`
- `ProductCode`: `str`

