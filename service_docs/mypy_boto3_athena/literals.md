# Literals for boto3 Athena module

> [Index](../index.md) > [Athena](./index.md) > Literals

Auto-generated documentation for [Athena](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena)
type annotations stubs module [mypy_boto3_athena](https://pypi.org/project/mypy-boto3-athena/).

- [Literals for boto3 Athena module](#literals-for-boto3-athena-module)
  - [ColumnNullable](#columnnullable)
  - [DataCatalogType](#datacatalogtype)
  - [EncryptionOption](#encryptionoption)
  - [GetQueryResultsPaginatorName](#getqueryresultspaginatorname)
  - [ListDataCatalogsPaginatorName](#listdatacatalogspaginatorname)
  - [ListDatabasesPaginatorName](#listdatabasespaginatorname)
  - [ListNamedQueriesPaginatorName](#listnamedqueriespaginatorname)
  - [ListQueryExecutionsPaginatorName](#listqueryexecutionspaginatorname)
  - [ListTableMetadataPaginatorName](#listtablemetadatapaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [QueryExecutionState](#queryexecutionstate)
  - [StatementType](#statementtype)
  - [WorkGroupState](#workgroupstate)

## ColumnNullable

```python
from mypy_boto3_athena.literals import ColumnNullable
```

Values:

- `NOT_NULL`
- `NULLABLE`
- `UNKNOWN`

## DataCatalogType

```python
from mypy_boto3_athena.literals import DataCatalogType
```

Values:

- `GLUE`
- `HIVE`
- `LAMBDA`

## EncryptionOption

```python
from mypy_boto3_athena.literals import EncryptionOption
```

Values:

- `CSE_KMS`
- `SSE_KMS`
- `SSE_S3`

## GetQueryResultsPaginatorName

```python
from mypy_boto3_athena.literals import GetQueryResultsPaginatorName
```

Values:

- `get_query_results`

## ListDataCatalogsPaginatorName

```python
from mypy_boto3_athena.literals import ListDataCatalogsPaginatorName
```

Values:

- `list_data_catalogs`

## ListDatabasesPaginatorName

```python
from mypy_boto3_athena.literals import ListDatabasesPaginatorName
```

Values:

- `list_databases`

## ListNamedQueriesPaginatorName

```python
from mypy_boto3_athena.literals import ListNamedQueriesPaginatorName
```

Values:

- `list_named_queries`

## ListQueryExecutionsPaginatorName

```python
from mypy_boto3_athena.literals import ListQueryExecutionsPaginatorName
```

Values:

- `list_query_executions`

## ListTableMetadataPaginatorName

```python
from mypy_boto3_athena.literals import ListTableMetadataPaginatorName
```

Values:

- `list_table_metadata`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_athena.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## QueryExecutionState

```python
from mypy_boto3_athena.literals import QueryExecutionState
```

Values:

- `CANCELLED`
- `FAILED`
- `QUEUED`
- `RUNNING`
- `SUCCEEDED`

## StatementType

```python
from mypy_boto3_athena.literals import StatementType
```

Values:

- `DDL`
- `DML`
- `UTILITY`

## WorkGroupState

```python
from mypy_boto3_athena.literals import WorkGroupState
```

Values:

- `DISABLED`
- `ENABLED`
