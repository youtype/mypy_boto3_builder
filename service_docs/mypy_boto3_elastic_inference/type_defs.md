# Structures for boto3 ElasticInference module

> [Index](../index.md) > [ElasticInference](./index.md) > Structures

Auto-generated documentation for [ElasticInference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html#ElasticInference)
type annotations stubs module [mypy_boto3_elastic_inference](https://pypi.org/project/mypy-boto3-elastic-inference/).

- [Structures for boto3 ElasticInference module](#structures-for-boto3-elasticinference-module)
  - [AcceleratorTypeOfferingTypeDef](#acceleratortypeofferingtypedef)
  - [AcceleratorTypeTypeDef](#acceleratortypetypedef)
  - [ElasticInferenceAcceleratorHealthTypeDef](#elasticinferenceacceleratorhealthtypedef)
  - [ElasticInferenceAcceleratorTypeDef](#elasticinferenceacceleratortypedef)
  - [KeyValuePairTypeDef](#keyvaluepairtypedef)
  - [MemoryInfoTypeDef](#memoryinfotypedef)
  - [DescribeAcceleratorOfferingsResponseTypeDef](#describeacceleratorofferingsresponsetypedef)
  - [DescribeAcceleratorTypesResponseTypeDef](#describeacceleratortypesresponsetypedef)
  - [DescribeAcceleratorsResponseTypeDef](#describeacceleratorsresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## AcceleratorTypeOfferingTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeOfferingTypeDef
```




Optional fields:
- `acceleratorType`: `str`
- `locationType`: `LocationType`
- `location`: `str`


## AcceleratorTypeTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeTypeDef
```




Optional fields:
- `acceleratorTypeName`: `str`
- `memoryInfo`: `"MemoryInfoTypeDef"`
- `throughputInfo`: `List["KeyValuePairTypeDef"]`


## ElasticInferenceAcceleratorHealthTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import ElasticInferenceAcceleratorHealthTypeDef
```




Optional fields:
- `status`: `str`


## ElasticInferenceAcceleratorTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import ElasticInferenceAcceleratorTypeDef
```




Optional fields:
- `acceleratorHealth`: `"ElasticInferenceAcceleratorHealthTypeDef"`
- `acceleratorType`: `str`
- `acceleratorId`: `str`
- `availabilityZone`: `str`
- `attachedResource`: `str`


## KeyValuePairTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import KeyValuePairTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `int`


## MemoryInfoTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import MemoryInfoTypeDef
```




Optional fields:
- `sizeInMiB`: `int`


## DescribeAcceleratorOfferingsResponseTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import DescribeAcceleratorOfferingsResponseTypeDef
```




Optional fields:
- `acceleratorTypeOfferings`: `List["AcceleratorTypeOfferingTypeDef"]`


## DescribeAcceleratorTypesResponseTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import DescribeAcceleratorTypesResponseTypeDef
```




Optional fields:
- `acceleratorTypes`: `List["AcceleratorTypeTypeDef"]`


## DescribeAcceleratorsResponseTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import DescribeAcceleratorsResponseTypeDef
```




Optional fields:
- `acceleratorSet`: `List["ElasticInferenceAcceleratorTypeDef"]`
- `nextToken`: `str`


## FilterTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import FilterTypeDef
```




Optional fields:
- `name`: `str`
- `values`: `List[str]`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import ListTagsForResourceResultTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_elastic_inference.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

