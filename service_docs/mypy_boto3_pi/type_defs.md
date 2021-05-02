# Structures for boto3 PI module

> [Index](../index.md) > [PI](./index.md) > Structures

Auto-generated documentation for [PI](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI)
type annotations stubs module [mypy_boto3_pi](https://pypi.org/project/mypy-boto3-pi/).

- [Structures for boto3 PI module](#structures-for-boto3-pi-module)
  - [DataPointTypeDef](#datapointtypedef)
  - [DimensionGroupTypeDef](#dimensiongrouptypedef)
  - [DimensionKeyDescriptionTypeDef](#dimensionkeydescriptiontypedef)
  - [MetricKeyDataPointsTypeDef](#metrickeydatapointstypedef)
  - [ResponsePartitionKeyTypeDef](#responsepartitionkeytypedef)
  - [ResponseResourceMetricKeyTypeDef](#responseresourcemetrickeytypedef)
  - [DescribeDimensionKeysResponseTypeDef](#describedimensionkeysresponsetypedef)
  - [GetResourceMetricsResponseTypeDef](#getresourcemetricsresponsetypedef)
  - [MetricQueryTypeDef](#metricquerytypedef)

## DataPointTypeDef

```python
from mypy_boto3_pi.type_defs import DataPointTypeDef
```


Required fields:
- `Timestamp`: `datetime`
- `Value`: `float`




## DimensionGroupTypeDef

```python
from mypy_boto3_pi.type_defs import DimensionGroupTypeDef
```


Required fields:
- `Group`: `str`



Optional fields:
- `Dimensions`: `List[str]`
- `Limit`: `int`


## DimensionKeyDescriptionTypeDef

```python
from mypy_boto3_pi.type_defs import DimensionKeyDescriptionTypeDef
```




Optional fields:
- `Dimensions`: `Dict[str, str]`
- `Total`: `float`
- `Partitions`: `List[float]`


## MetricKeyDataPointsTypeDef

```python
from mypy_boto3_pi.type_defs import MetricKeyDataPointsTypeDef
```




Optional fields:
- `Key`: `"ResponseResourceMetricKeyTypeDef"`
- `DataPoints`: `List["DataPointTypeDef"]`


## ResponsePartitionKeyTypeDef

```python
from mypy_boto3_pi.type_defs import ResponsePartitionKeyTypeDef
```


Required fields:
- `Dimensions`: `Dict[str, str]`




## ResponseResourceMetricKeyTypeDef

```python
from mypy_boto3_pi.type_defs import ResponseResourceMetricKeyTypeDef
```


Required fields:
- `Metric`: `str`



Optional fields:
- `Dimensions`: `Dict[str, str]`


## DescribeDimensionKeysResponseTypeDef

```python
from mypy_boto3_pi.type_defs import DescribeDimensionKeysResponseTypeDef
```




Optional fields:
- `AlignedStartTime`: `datetime`
- `AlignedEndTime`: `datetime`
- `PartitionKeys`: `List["ResponsePartitionKeyTypeDef"]`
- `Keys`: `List["DimensionKeyDescriptionTypeDef"]`
- `NextToken`: `str`


## GetResourceMetricsResponseTypeDef

```python
from mypy_boto3_pi.type_defs import GetResourceMetricsResponseTypeDef
```




Optional fields:
- `AlignedStartTime`: `datetime`
- `AlignedEndTime`: `datetime`
- `Identifier`: `str`
- `MetricList`: `List["MetricKeyDataPointsTypeDef"]`
- `NextToken`: `str`


## MetricQueryTypeDef

```python
from mypy_boto3_pi.type_defs import MetricQueryTypeDef
```


Required fields:
- `Metric`: `str`



Optional fields:
- `GroupBy`: `"DimensionGroupTypeDef"`
- `Filter`: `Dict[str, str]`

