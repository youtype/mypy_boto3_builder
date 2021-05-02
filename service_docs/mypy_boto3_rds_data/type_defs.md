# Structures for boto3 RDSDataService module

> [Index](../index.md) > [RDSDataService](./index.md) > Structures

Auto-generated documentation for [RDSDataService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService)
type annotations stubs module [mypy_boto3_rds_data](https://pypi.org/project/mypy-boto3-rds-data/).

- [Structures for boto3 RDSDataService module](#structures-for-boto3-rdsdataservice-module)
  - [ColumnMetadataTypeDef](#columnmetadatatypedef)
  - [FieldTypeDef](#fieldtypedef)
  - [RecordTypeDef](#recordtypedef)
  - [ResultFrameTypeDef](#resultframetypedef)
  - [ResultSetMetadataTypeDef](#resultsetmetadatatypedef)
  - [SqlStatementResultTypeDef](#sqlstatementresulttypedef)
  - [StructValueTypeDef](#structvaluetypedef)
  - [UpdateResultTypeDef](#updateresulttypedef)
  - [BatchExecuteStatementResponseTypeDef](#batchexecutestatementresponsetypedef)
  - [BeginTransactionResponseTypeDef](#begintransactionresponsetypedef)
  - [CommitTransactionResponseTypeDef](#committransactionresponsetypedef)
  - [ValueTypeDef](#valuetypedef)
  - [ArrayValueTypeDef](#arrayvaluetypedef)
  - [ExecuteSqlResponseTypeDef](#executesqlresponsetypedef)
  - [ExecuteStatementResponseTypeDef](#executestatementresponsetypedef)
  - [ResultSetOptionsTypeDef](#resultsetoptionstypedef)
  - [RollbackTransactionResponseTypeDef](#rollbacktransactionresponsetypedef)
  - [SqlParameterTypeDef](#sqlparametertypedef)

## ColumnMetadataTypeDef

```python
from mypy_boto3_rds_data.type_defs import ColumnMetadataTypeDef
```




Optional fields:
- `arrayBaseColumnType`: `int`
- `isAutoIncrement`: `bool`
- `isCaseSensitive`: `bool`
- `isCurrency`: `bool`
- `isSigned`: `bool`
- `label`: `str`
- `name`: `str`
- `nullable`: `int`
- `precision`: `int`
- `scale`: `int`
- `schemaName`: `str`
- `tableName`: `str`
- `type`: `int`
- `typeName`: `str`


## FieldTypeDef

```python
from mypy_boto3_rds_data.type_defs import FieldTypeDef
```




Optional fields:
- `arrayValue`: `Dict[str, Any]`
- `blobValue`: `Union[bytes, IO[bytes]]`
- `booleanValue`: `bool`
- `doubleValue`: `float`
- `isNull`: `bool`
- `longValue`: `int`
- `stringValue`: `str`


## RecordTypeDef

```python
from mypy_boto3_rds_data.type_defs import RecordTypeDef
```




Optional fields:
- `values`: `List[Dict[str, Any]]`


## ResultFrameTypeDef

```python
from mypy_boto3_rds_data.type_defs import ResultFrameTypeDef
```




Optional fields:
- `records`: `List["RecordTypeDef"]`
- `resultSetMetadata`: `"ResultSetMetadataTypeDef"`


## ResultSetMetadataTypeDef

```python
from mypy_boto3_rds_data.type_defs import ResultSetMetadataTypeDef
```




Optional fields:
- `columnCount`: `int`
- `columnMetadata`: `List["ColumnMetadataTypeDef"]`


## SqlStatementResultTypeDef

```python
from mypy_boto3_rds_data.type_defs import SqlStatementResultTypeDef
```




Optional fields:
- `numberOfRecordsUpdated`: `int`
- `resultFrame`: `"ResultFrameTypeDef"`


## StructValueTypeDef

```python
from mypy_boto3_rds_data.type_defs import StructValueTypeDef
```




Optional fields:
- `attributes`: `List[Dict[str, Any]]`


## UpdateResultTypeDef

```python
from mypy_boto3_rds_data.type_defs import UpdateResultTypeDef
```




Optional fields:
- `generatedFields`: `List["FieldTypeDef"]`


## BatchExecuteStatementResponseTypeDef

```python
from mypy_boto3_rds_data.type_defs import BatchExecuteStatementResponseTypeDef
```




Optional fields:
- `updateResults`: `List["UpdateResultTypeDef"]`


## BeginTransactionResponseTypeDef

```python
from mypy_boto3_rds_data.type_defs import BeginTransactionResponseTypeDef
```




Optional fields:
- `transactionId`: `str`


## CommitTransactionResponseTypeDef

```python
from mypy_boto3_rds_data.type_defs import CommitTransactionResponseTypeDef
```




Optional fields:
- `transactionStatus`: `str`


## ValueTypeDef

```python
from mypy_boto3_rds_data.type_defs import ValueTypeDef
```




Optional fields:
- `arrayValues`: `List[Dict[str, Any]]`
- `bigIntValue`: `int`
- `bitValue`: `bool`
- `blobValue`: `Union[bytes, IO[bytes]]`
- `doubleValue`: `float`
- `intValue`: `int`
- `isNull`: `bool`
- `realValue`: `float`
- `stringValue`: `str`
- `structValue`: `"StructValueTypeDef"`


## ArrayValueTypeDef

```python
from mypy_boto3_rds_data.type_defs import ArrayValueTypeDef
```




Optional fields:
- `arrayValues`: `List[Dict[str, Any]]`
- `booleanValues`: `List[bool]`
- `doubleValues`: `List[float]`
- `longValues`: `List[int]`
- `stringValues`: `List[str]`


## ExecuteSqlResponseTypeDef

```python
from mypy_boto3_rds_data.type_defs import ExecuteSqlResponseTypeDef
```




Optional fields:
- `sqlStatementResults`: `List["SqlStatementResultTypeDef"]`


## ExecuteStatementResponseTypeDef

```python
from mypy_boto3_rds_data.type_defs import ExecuteStatementResponseTypeDef
```




Optional fields:
- `columnMetadata`: `List["ColumnMetadataTypeDef"]`
- `generatedFields`: `List["FieldTypeDef"]`
- `numberOfRecordsUpdated`: `int`
- `records`: `List[List["FieldTypeDef"]]`


## ResultSetOptionsTypeDef

```python
from mypy_boto3_rds_data.type_defs import ResultSetOptionsTypeDef
```




Optional fields:
- `decimalReturnType`: `DecimalReturnType`


## RollbackTransactionResponseTypeDef

```python
from mypy_boto3_rds_data.type_defs import RollbackTransactionResponseTypeDef
```




Optional fields:
- `transactionStatus`: `str`


## SqlParameterTypeDef

```python
from mypy_boto3_rds_data.type_defs import SqlParameterTypeDef
```




Optional fields:
- `name`: `str`
- `typeHint`: `TypeHint`
- `value`: `"FieldTypeDef"`

