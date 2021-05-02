# Structures for boto3 MarketplaceEntitlementService module

> [Index](../index.md) > [MarketplaceEntitlementService](./index.md) > Structures

Auto-generated documentation for [MarketplaceEntitlementService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService)
type annotations stubs module [mypy_boto3_marketplace_entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/).

- [Structures for boto3 MarketplaceEntitlementService module](#structures-for-boto3-marketplaceentitlementservice-module)
  - [EntitlementTypeDef](#entitlementtypedef)
  - [EntitlementValueTypeDef](#entitlementvaluetypedef)
  - [GetEntitlementsResultTypeDef](#getentitlementsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## EntitlementTypeDef

```python
from mypy_boto3_marketplace_entitlement.type_defs import EntitlementTypeDef
```




Optional fields:
- `ProductCode`: `str`
- `Dimension`: `str`
- `CustomerIdentifier`: `str`
- `Value`: `"EntitlementValueTypeDef"`
- `ExpirationDate`: `datetime`


## EntitlementValueTypeDef

```python
from mypy_boto3_marketplace_entitlement.type_defs import EntitlementValueTypeDef
```




Optional fields:
- `IntegerValue`: `int`
- `DoubleValue`: `float`
- `BooleanValue`: `bool`
- `StringValue`: `str`


## GetEntitlementsResultTypeDef

```python
from mypy_boto3_marketplace_entitlement.type_defs import GetEntitlementsResultTypeDef
```




Optional fields:
- `Entitlements`: `List["EntitlementTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_marketplace_entitlement.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

