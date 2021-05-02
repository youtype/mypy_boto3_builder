# Structures for boto3 TimestreamQuery module

> [Index](../index.md) > [TimestreamQuery](./index.md) > Structures

Auto-generated documentation for [TimestreamQuery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery)
type annotations stubs module [mypy_boto3_timestream_query](https://pypi.org/project/mypy-boto3-timestream-query/).

- [Structures for boto3 TimestreamQuery module](#structures-for-boto3-timestreamquery-module)
  - [EndpointTypeDef](#endpointtypedef)
  - [QueryStatusTypeDef](#querystatustypedef)
  - [TimeSeriesDataPointTypeDef](#timeseriesdatapointtypedef)
  - [TypeTypeDef](#typetypedef)
  - [CancelQueryResponseTypeDef](#cancelqueryresponsetypedef)
  - [DescribeEndpointsResponseTypeDef](#describeendpointsresponsetypedef)
  - [DatumTypeDef](#datumtypedef)
  - [RowTypeDef](#rowtypedef)
  - [ColumnInfoTypeDef](#columninfotypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [QueryResponseTypeDef](#queryresponsetypedef)

## EndpointTypeDef

```python
from mypy_boto3_timestream_query.type_defs import EndpointTypeDef
```


Required fields:
- `Address`: `str`
- `CachePeriodInMinutes`: `int`




## QueryStatusTypeDef

```python
from mypy_boto3_timestream_query.type_defs import QueryStatusTypeDef
```




Optional fields:
- `ProgressPercentage`: `float`
- `CumulativeBytesScanned`: `int`
- `CumulativeBytesMetered`: `int`


## TimeSeriesDataPointTypeDef

```python
from mypy_boto3_timestream_query.type_defs import TimeSeriesDataPointTypeDef
```


Required fields:
- `Time`: `str`
- `Value`: `Dict[str, Any]`




## TypeTypeDef

```python
from mypy_boto3_timestream_query.type_defs import TypeTypeDef
```




Optional fields:
- `ScalarType`: `ScalarType`
- `ArrayColumnInfo`: `Dict[str, Any]`
- `TimeSeriesMeasureValueColumnInfo`: `Dict[str, Any]`
- `RowColumnInfo`: `List[Dict[str, Any]]`


## CancelQueryResponseTypeDef

```python
from mypy_boto3_timestream_query.type_defs import CancelQueryResponseTypeDef
```




Optional fields:
- `CancellationMessage`: `str`


## DescribeEndpointsResponseTypeDef

```python
from mypy_boto3_timestream_query.type_defs import DescribeEndpointsResponseTypeDef
```


Required fields:
- `Endpoints`: `List["EndpointTypeDef"]`




## DatumTypeDef

```python
from mypy_boto3_timestream_query.type_defs import DatumTypeDef
```




Optional fields:
- `ScalarValue`: `str`
- `TimeSeriesValue`: `List["TimeSeriesDataPointTypeDef"]`
- `ArrayValue`: `List[Dict[str, Any]]`
- `RowValue`: `Dict[str, Any]`
- `NullValue`: `bool`


## RowTypeDef

```python
from mypy_boto3_timestream_query.type_defs import RowTypeDef
```


Required fields:
- `Data`: `List[Dict[str, Any]]`




## ColumnInfoTypeDef

```python
from mypy_boto3_timestream_query.type_defs import ColumnInfoTypeDef
```


Required fields:
- `Type`: `"TypeTypeDef"`



Optional fields:
- `Name`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_timestream_query.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## QueryResponseTypeDef

```python
from mypy_boto3_timestream_query.type_defs import QueryResponseTypeDef
```


Required fields:
- `QueryId`: `str`
- `Rows`: `List[Dict[str, Any]]`
- `ColumnInfo`: `List[Dict[str, Any]]`



Optional fields:
- `NextToken`: `str`
- `QueryStatus`: `"QueryStatusTypeDef"`

