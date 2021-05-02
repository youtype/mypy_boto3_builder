# Structures for boto3 Pricing module

> [Index](../index.md) > [Pricing](./index.md) > Structures

Auto-generated documentation for [Pricing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html#Pricing)
type annotations stubs module [mypy_boto3_pricing](https://pypi.org/project/mypy-boto3-pricing/).

- [Structures for boto3 Pricing module](#structures-for-boto3-pricing-module)
  - [AttributeValueTypeDef](#attributevaluetypedef)
  - [ServiceTypeDef](#servicetypedef)
  - [DescribeServicesResponseTypeDef](#describeservicesresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetAttributeValuesResponseTypeDef](#getattributevaluesresponsetypedef)
  - [GetProductsResponseTypeDef](#getproductsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## AttributeValueTypeDef

```python
from mypy_boto3_pricing.type_defs import AttributeValueTypeDef
```




Optional fields:
- `Value`: `str`


## ServiceTypeDef

```python
from mypy_boto3_pricing.type_defs import ServiceTypeDef
```




Optional fields:
- `ServiceCode`: `str`
- `AttributeNames`: `List[str]`


## DescribeServicesResponseTypeDef

```python
from mypy_boto3_pricing.type_defs import DescribeServicesResponseTypeDef
```




Optional fields:
- `Services`: `List["ServiceTypeDef"]`
- `FormatVersion`: `str`
- `NextToken`: `str`


## FilterTypeDef

```python
from mypy_boto3_pricing.type_defs import FilterTypeDef
```


Required fields:
- `Type`: `FilterType`
- `Field`: `str`
- `Value`: `str`




## GetAttributeValuesResponseTypeDef

```python
from mypy_boto3_pricing.type_defs import GetAttributeValuesResponseTypeDef
```




Optional fields:
- `AttributeValues`: `List["AttributeValueTypeDef"]`
- `NextToken`: `str`


## GetProductsResponseTypeDef

```python
from mypy_boto3_pricing.type_defs import GetProductsResponseTypeDef
```




Optional fields:
- `FormatVersion`: `str`
- `PriceList`: `List[str]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_pricing.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

