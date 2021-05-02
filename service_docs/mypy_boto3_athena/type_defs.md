# Structures for boto3 Athena module

> [Index](../index.md) > [Athena](./index.md) > Structures

Auto-generated documentation for [Athena](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena)
type annotations stubs module [mypy_boto3_athena](https://pypi.org/project/mypy-boto3-athena/).

- [Structures for boto3 Athena module](#structures-for-boto3-athena-module)
  - [ColumnInfoTypeDef](#columninfotypedef)
  - [ColumnTypeDef](#columntypedef)
  - [DataCatalogSummaryTypeDef](#datacatalogsummarytypedef)
  - [DataCatalogTypeDef](#datacatalogtypedef)
  - [DatabaseTypeDef](#databasetypedef)
  - [DatumTypeDef](#datumtypedef)
  - [EncryptionConfigurationTypeDef](#encryptionconfigurationtypedef)
  - [EngineVersionTypeDef](#engineversiontypedef)
  - [NamedQueryTypeDef](#namedquerytypedef)
  - [PreparedStatementSummaryTypeDef](#preparedstatementsummarytypedef)
  - [PreparedStatementTypeDef](#preparedstatementtypedef)
  - [QueryExecutionContextTypeDef](#queryexecutioncontexttypedef)
  - [QueryExecutionStatisticsTypeDef](#queryexecutionstatisticstypedef)
  - [QueryExecutionStatusTypeDef](#queryexecutionstatustypedef)
  - [QueryExecutionTypeDef](#queryexecutiontypedef)
  - [ResponseMetadata](#responsemetadata)
  - [ResultConfigurationTypeDef](#resultconfigurationtypedef)
  - [ResultConfigurationUpdatesTypeDef](#resultconfigurationupdatestypedef)
  - [ResultSetMetadataTypeDef](#resultsetmetadatatypedef)
  - [ResultSetTypeDef](#resultsettypedef)
  - [RowTypeDef](#rowtypedef)
  - [TableMetadataTypeDef](#tablemetadatatypedef)
  - [TagTypeDef](#tagtypedef)
  - [UnprocessedNamedQueryIdTypeDef](#unprocessednamedqueryidtypedef)
  - [UnprocessedQueryExecutionIdTypeDef](#unprocessedqueryexecutionidtypedef)
  - [WorkGroupConfigurationTypeDef](#workgroupconfigurationtypedef)
  - [WorkGroupSummaryTypeDef](#workgroupsummarytypedef)
  - [WorkGroupTypeDef](#workgrouptypedef)
  - [BatchGetNamedQueryOutputTypeDef](#batchgetnamedqueryoutputtypedef)
  - [BatchGetQueryExecutionOutputTypeDef](#batchgetqueryexecutionoutputtypedef)
  - [CreateNamedQueryOutputTypeDef](#createnamedqueryoutputtypedef)
  - [GetDataCatalogOutputTypeDef](#getdatacatalogoutputtypedef)
  - [GetDatabaseOutputTypeDef](#getdatabaseoutputtypedef)
  - [GetNamedQueryOutputTypeDef](#getnamedqueryoutputtypedef)
  - [GetPreparedStatementOutputTypeDef](#getpreparedstatementoutputtypedef)
  - [GetQueryExecutionOutputTypeDef](#getqueryexecutionoutputtypedef)
  - [GetQueryResultsOutputTypeDef](#getqueryresultsoutputtypedef)
  - [GetTableMetadataOutputTypeDef](#gettablemetadataoutputtypedef)
  - [GetWorkGroupOutputTypeDef](#getworkgroupoutputtypedef)
  - [ListDataCatalogsOutputTypeDef](#listdatacatalogsoutputtypedef)
  - [ListDatabasesOutputTypeDef](#listdatabasesoutputtypedef)
  - [ListEngineVersionsOutputTypeDef](#listengineversionsoutputtypedef)
  - [ListNamedQueriesOutputTypeDef](#listnamedqueriesoutputtypedef)
  - [ListPreparedStatementsOutputTypeDef](#listpreparedstatementsoutputtypedef)
  - [ListQueryExecutionsOutputTypeDef](#listqueryexecutionsoutputtypedef)
  - [ListTableMetadataOutputTypeDef](#listtablemetadataoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ListWorkGroupsOutputTypeDef](#listworkgroupsoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [StartQueryExecutionOutputTypeDef](#startqueryexecutionoutputtypedef)
  - [WorkGroupConfigurationUpdatesTypeDef](#workgroupconfigurationupdatestypedef)

## ColumnInfoTypeDef

```python
from mypy_boto3_athena.type_defs import ColumnInfoTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `str`



Optional fields:
- `CatalogName`: `str`
- `SchemaName`: `str`
- `TableName`: `str`
- `Label`: `str`
- `Precision`: `int`
- `Scale`: `int`
- `Nullable`: `ColumnNullable`
- `CaseSensitive`: `bool`


## ColumnTypeDef

```python
from mypy_boto3_athena.type_defs import ColumnTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Type`: `str`
- `Comment`: `str`


## DataCatalogSummaryTypeDef

```python
from mypy_boto3_athena.type_defs import DataCatalogSummaryTypeDef
```




Optional fields:
- `CatalogName`: `str`
- `Type`: `DataCatalogType`


## DataCatalogTypeDef

```python
from mypy_boto3_athena.type_defs import DataCatalogTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `DataCatalogType`



Optional fields:
- `Description`: `str`
- `Parameters`: `Dict[str, str]`


## DatabaseTypeDef

```python
from mypy_boto3_athena.type_defs import DatabaseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Description`: `str`
- `Parameters`: `Dict[str, str]`


## DatumTypeDef

```python
from mypy_boto3_athena.type_defs import DatumTypeDef
```




Optional fields:
- `VarCharValue`: `str`


## EncryptionConfigurationTypeDef

```python
from mypy_boto3_athena.type_defs import EncryptionConfigurationTypeDef
```


Required fields:
- `EncryptionOption`: `EncryptionOption`



Optional fields:
- `KmsKey`: `str`


## EngineVersionTypeDef

```python
from mypy_boto3_athena.type_defs import EngineVersionTypeDef
```




Optional fields:
- `SelectedEngineVersion`: `str`
- `EffectiveEngineVersion`: `str`


## NamedQueryTypeDef

```python
from mypy_boto3_athena.type_defs import NamedQueryTypeDef
```


Required fields:
- `Name`: `str`
- `Database`: `str`
- `QueryString`: `str`



Optional fields:
- `Description`: `str`
- `NamedQueryId`: `str`
- `WorkGroup`: `str`


## PreparedStatementSummaryTypeDef

```python
from mypy_boto3_athena.type_defs import PreparedStatementSummaryTypeDef
```




Optional fields:
- `StatementName`: `str`
- `LastModifiedTime`: `datetime`


## PreparedStatementTypeDef

```python
from mypy_boto3_athena.type_defs import PreparedStatementTypeDef
```




Optional fields:
- `StatementName`: `str`
- `QueryStatement`: `str`
- `WorkGroupName`: `str`
- `Description`: `str`
- `LastModifiedTime`: `datetime`


## QueryExecutionContextTypeDef

```python
from mypy_boto3_athena.type_defs import QueryExecutionContextTypeDef
```




Optional fields:
- `Database`: `str`
- `Catalog`: `str`


## QueryExecutionStatisticsTypeDef

```python
from mypy_boto3_athena.type_defs import QueryExecutionStatisticsTypeDef
```




Optional fields:
- `EngineExecutionTimeInMillis`: `int`
- `DataScannedInBytes`: `int`
- `DataManifestLocation`: `str`
- `TotalExecutionTimeInMillis`: `int`
- `QueryQueueTimeInMillis`: `int`
- `QueryPlanningTimeInMillis`: `int`
- `ServiceProcessingTimeInMillis`: `int`


## QueryExecutionStatusTypeDef

```python
from mypy_boto3_athena.type_defs import QueryExecutionStatusTypeDef
```




Optional fields:
- `State`: `QueryExecutionState`
- `StateChangeReason`: `str`
- `SubmissionDateTime`: `datetime`
- `CompletionDateTime`: `datetime`


## QueryExecutionTypeDef

```python
from mypy_boto3_athena.type_defs import QueryExecutionTypeDef
```




Optional fields:
- `QueryExecutionId`: `str`
- `Query`: `str`
- `StatementType`: `StatementType`
- `ResultConfiguration`: `"ResultConfigurationTypeDef"`
- `QueryExecutionContext`: `"QueryExecutionContextTypeDef"`
- `Status`: `"QueryExecutionStatusTypeDef"`
- `Statistics`: `"QueryExecutionStatisticsTypeDef"`
- `WorkGroup`: `str`
- `EngineVersion`: `"EngineVersionTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_athena.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## ResultConfigurationTypeDef

```python
from mypy_boto3_athena.type_defs import ResultConfigurationTypeDef
```




Optional fields:
- `OutputLocation`: `str`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`


## ResultConfigurationUpdatesTypeDef

```python
from mypy_boto3_athena.type_defs import ResultConfigurationUpdatesTypeDef
```




Optional fields:
- `OutputLocation`: `str`
- `RemoveOutputLocation`: `bool`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`
- `RemoveEncryptionConfiguration`: `bool`


## ResultSetMetadataTypeDef

```python
from mypy_boto3_athena.type_defs import ResultSetMetadataTypeDef
```




Optional fields:
- `ColumnInfo`: `List["ColumnInfoTypeDef"]`


## ResultSetTypeDef

```python
from mypy_boto3_athena.type_defs import ResultSetTypeDef
```




Optional fields:
- `Rows`: `List["RowTypeDef"]`
- `ResultSetMetadata`: `"ResultSetMetadataTypeDef"`


## RowTypeDef

```python
from mypy_boto3_athena.type_defs import RowTypeDef
```




Optional fields:
- `Data`: `List["DatumTypeDef"]`


## TableMetadataTypeDef

```python
from mypy_boto3_athena.type_defs import TableMetadataTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CreateTime`: `datetime`
- `LastAccessTime`: `datetime`
- `TableType`: `str`
- `Columns`: `List["ColumnTypeDef"]`
- `PartitionKeys`: `List["ColumnTypeDef"]`
- `Parameters`: `Dict[str, str]`


## TagTypeDef

```python
from mypy_boto3_athena.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## UnprocessedNamedQueryIdTypeDef

```python
from mypy_boto3_athena.type_defs import UnprocessedNamedQueryIdTypeDef
```




Optional fields:
- `NamedQueryId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## UnprocessedQueryExecutionIdTypeDef

```python
from mypy_boto3_athena.type_defs import UnprocessedQueryExecutionIdTypeDef
```




Optional fields:
- `QueryExecutionId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## WorkGroupConfigurationTypeDef

```python
from mypy_boto3_athena.type_defs import WorkGroupConfigurationTypeDef
```




Optional fields:
- `ResultConfiguration`: `"ResultConfigurationTypeDef"`
- `EnforceWorkGroupConfiguration`: `bool`
- `PublishCloudWatchMetricsEnabled`: `bool`
- `BytesScannedCutoffPerQuery`: `int`
- `RequesterPaysEnabled`: `bool`
- `EngineVersion`: `"EngineVersionTypeDef"`


## WorkGroupSummaryTypeDef

```python
from mypy_boto3_athena.type_defs import WorkGroupSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `State`: `WorkGroupState`
- `Description`: `str`
- `CreationTime`: `datetime`
- `EngineVersion`: `"EngineVersionTypeDef"`


## WorkGroupTypeDef

```python
from mypy_boto3_athena.type_defs import WorkGroupTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `State`: `WorkGroupState`
- `Configuration`: `"WorkGroupConfigurationTypeDef"`
- `Description`: `str`
- `CreationTime`: `datetime`


## BatchGetNamedQueryOutputTypeDef

```python
from mypy_boto3_athena.type_defs import BatchGetNamedQueryOutputTypeDef
```




Optional fields:
- `NamedQueries`: `List["NamedQueryTypeDef"]`
- `UnprocessedNamedQueryIds`: `List["UnprocessedNamedQueryIdTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetQueryExecutionOutputTypeDef

```python
from mypy_boto3_athena.type_defs import BatchGetQueryExecutionOutputTypeDef
```




Optional fields:
- `QueryExecutions`: `List["QueryExecutionTypeDef"]`
- `UnprocessedQueryExecutionIds`: `List["UnprocessedQueryExecutionIdTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateNamedQueryOutputTypeDef

```python
from mypy_boto3_athena.type_defs import CreateNamedQueryOutputTypeDef
```




Optional fields:
- `NamedQueryId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDataCatalogOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetDataCatalogOutputTypeDef
```




Optional fields:
- `DataCatalog`: `"DataCatalogTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDatabaseOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetDatabaseOutputTypeDef
```




Optional fields:
- `Database`: `"DatabaseTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetNamedQueryOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetNamedQueryOutputTypeDef
```




Optional fields:
- `NamedQuery`: `"NamedQueryTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPreparedStatementOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetPreparedStatementOutputTypeDef
```




Optional fields:
- `PreparedStatement`: `"PreparedStatementTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetQueryExecutionOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetQueryExecutionOutputTypeDef
```




Optional fields:
- `QueryExecution`: `"QueryExecutionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetQueryResultsOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetQueryResultsOutputTypeDef
```




Optional fields:
- `UpdateCount`: `int`
- `ResultSet`: `"ResultSetTypeDef"`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTableMetadataOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetTableMetadataOutputTypeDef
```




Optional fields:
- `TableMetadata`: `"TableMetadataTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetWorkGroupOutputTypeDef

```python
from mypy_boto3_athena.type_defs import GetWorkGroupOutputTypeDef
```




Optional fields:
- `WorkGroup`: `"WorkGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDataCatalogsOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListDataCatalogsOutputTypeDef
```




Optional fields:
- `DataCatalogsSummary`: `List["DataCatalogSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListDatabasesOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListDatabasesOutputTypeDef
```




Optional fields:
- `DatabaseList`: `List["DatabaseTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListEngineVersionsOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListEngineVersionsOutputTypeDef
```




Optional fields:
- `EngineVersions`: `List["EngineVersionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListNamedQueriesOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListNamedQueriesOutputTypeDef
```




Optional fields:
- `NamedQueryIds`: `List[str]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPreparedStatementsOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListPreparedStatementsOutputTypeDef
```




Optional fields:
- `PreparedStatements`: `List["PreparedStatementSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListQueryExecutionsOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListQueryExecutionsOutputTypeDef
```




Optional fields:
- `QueryExecutionIds`: `List[str]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTableMetadataOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListTableMetadataOutputTypeDef
```




Optional fields:
- `TableMetadataList`: `List["TableMetadataTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListWorkGroupsOutputTypeDef

```python
from mypy_boto3_athena.type_defs import ListWorkGroupsOutputTypeDef
```




Optional fields:
- `WorkGroups`: `List["WorkGroupSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_athena.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## StartQueryExecutionOutputTypeDef

```python
from mypy_boto3_athena.type_defs import StartQueryExecutionOutputTypeDef
```




Optional fields:
- `QueryExecutionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## WorkGroupConfigurationUpdatesTypeDef

```python
from mypy_boto3_athena.type_defs import WorkGroupConfigurationUpdatesTypeDef
```




Optional fields:
- `EnforceWorkGroupConfiguration`: `bool`
- `ResultConfigurationUpdates`: `"ResultConfigurationUpdatesTypeDef"`
- `PublishCloudWatchMetricsEnabled`: `bool`
- `BytesScannedCutoffPerQuery`: `int`
- `RemoveBytesScannedCutoffPerQuery`: `bool`
- `RequesterPaysEnabled`: `bool`
- `EngineVersion`: `"EngineVersionTypeDef"`

