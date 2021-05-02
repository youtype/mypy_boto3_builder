# Structures for boto3 RedshiftDataAPIService module

> [Index](../index.md) > [RedshiftDataAPIService](./index.md) > Structures

Auto-generated documentation for [RedshiftDataAPIService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService)
type annotations stubs module [mypy_boto3_redshift_data](https://pypi.org/project/mypy-boto3-redshift-data/).

- [Structures for boto3 RedshiftDataAPIService module](#structures-for-boto3-redshiftdataapiservice-module)
  - [CancelStatementResponseTypeDef](#cancelstatementresponsetypedef)
  - [ColumnMetadataTypeDef](#columnmetadatatypedef)
  - [DescribeStatementResponseTypeDef](#describestatementresponsetypedef)
  - [DescribeTableResponseTypeDef](#describetableresponsetypedef)
  - [ExecuteStatementOutputTypeDef](#executestatementoutputtypedef)
  - [FieldTypeDef](#fieldtypedef)
  - [GetStatementResultResponseTypeDef](#getstatementresultresponsetypedef)
  - [ListDatabasesResponseTypeDef](#listdatabasesresponsetypedef)
  - [ListSchemasResponseTypeDef](#listschemasresponsetypedef)
  - [ListStatementsResponseTypeDef](#liststatementsresponsetypedef)
  - [ListTablesResponseTypeDef](#listtablesresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [StatementDataTypeDef](#statementdatatypedef)
  - [TableMemberTypeDef](#tablemembertypedef)

## CancelStatementResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import CancelStatementResponseTypeDef
```




Optional fields:
- `Status`: `bool`


## ColumnMetadataTypeDef

```python
from mypy_boto3_redshift_data.type_defs import ColumnMetadataTypeDef
```




Optional fields:
- `columnDefault`: `str`
- `isCaseSensitive`: `bool`
- `isCurrency`: `bool`
- `isSigned`: `bool`
- `label`: `str`
- `length`: `int`
- `name`: `str`
- `nullable`: `int`
- `precision`: `int`
- `scale`: `int`
- `schemaName`: `str`
- `tableName`: `str`
- `typeName`: `str`


## DescribeStatementResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import DescribeStatementResponseTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `ClusterIdentifier`: `str`
- `CreatedAt`: `datetime`
- `Database`: `str`
- `DbUser`: `str`
- `Duration`: `int`
- `Error`: `str`
- `HasResultSet`: `bool`
- `QueryString`: `str`
- `RedshiftPid`: `int`
- `RedshiftQueryId`: `int`
- `ResultRows`: `int`
- `ResultSize`: `int`
- `SecretArn`: `str`
- `Status`: `StatusString`
- `UpdatedAt`: `datetime`


## DescribeTableResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import DescribeTableResponseTypeDef
```




Optional fields:
- `ColumnList`: `List["ColumnMetadataTypeDef"]`
- `NextToken`: `str`
- `TableName`: `str`


## ExecuteStatementOutputTypeDef

```python
from mypy_boto3_redshift_data.type_defs import ExecuteStatementOutputTypeDef
```




Optional fields:
- `ClusterIdentifier`: `str`
- `CreatedAt`: `datetime`
- `Database`: `str`
- `DbUser`: `str`
- `Id`: `str`
- `SecretArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## FieldTypeDef

```python
from mypy_boto3_redshift_data.type_defs import FieldTypeDef
```




Optional fields:
- `blobValue`: `Union[bytes, IO[bytes]]`
- `booleanValue`: `bool`
- `doubleValue`: `float`
- `isNull`: `bool`
- `longValue`: `int`
- `stringValue`: `str`


## GetStatementResultResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import GetStatementResultResponseTypeDef
```


Required fields:
- `Records`: `List[List["FieldTypeDef"]]`



Optional fields:
- `ColumnMetadata`: `List["ColumnMetadataTypeDef"]`
- `NextToken`: `str`
- `TotalNumRows`: `int`


## ListDatabasesResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import ListDatabasesResponseTypeDef
```




Optional fields:
- `Databases`: `List[str]`
- `NextToken`: `str`


## ListSchemasResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import ListSchemasResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Schemas`: `List[str]`


## ListStatementsResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import ListStatementsResponseTypeDef
```


Required fields:
- `Statements`: `List["StatementDataTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTablesResponseTypeDef

```python
from mypy_boto3_redshift_data.type_defs import ListTablesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Tables`: `List["TableMemberTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_redshift_data.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResponseMetadata

```python
from mypy_boto3_redshift_data.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## StatementDataTypeDef

```python
from mypy_boto3_redshift_data.type_defs import StatementDataTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `CreatedAt`: `datetime`
- `QueryString`: `str`
- `SecretArn`: `str`
- `StatementName`: `str`
- `Status`: `StatusString`
- `UpdatedAt`: `datetime`


## TableMemberTypeDef

```python
from mypy_boto3_redshift_data.type_defs import TableMemberTypeDef
```




Optional fields:
- `name`: `str`
- `schema`: `str`
- `type`: `str`

