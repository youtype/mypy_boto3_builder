# Paginators for boto3 RedshiftDataAPIService module

> [Index](../index.md) > [RedshiftDataAPIService](./index.md) > Paginators

Auto-generated documentation for [RedshiftDataAPIService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService)
type annotations stubs module [mypy_boto3_redshift_data](https://pypi.org/project/mypy-boto3-redshift-data/).

- [Paginators for boto3 RedshiftDataAPIService module](#paginators-for-boto3-redshiftdataapiservice-module)
  - [DescribeTablePaginator](#describetablepaginator)
  - [GetStatementResultPaginator](#getstatementresultpaginator)
  - [ListDatabasesPaginator](#listdatabasespaginator)
  - [ListSchemasPaginator](#listschemaspaginator)
  - [ListStatementsPaginator](#liststatementspaginator)
  - [ListTablesPaginator](#listtablespaginator)

## DescribeTablePaginator

Type annotations for `boto3.client("redshift-data").get_paginator("describe_table")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import DescribeTablePaginator

def get_describe_table_paginator() -> DescribeTablePaginator:
    return boto3.client("redshift-data").get_paginator("describe_table")
```

[Paginator.DescribeTable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.DescribeTable)

```python
class DescribeTablePaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str,
        ConnectedDatabase: str = None,
        DbUser: str = None,
        Schema: str = None,
        SecretArn: str = None,
        Table: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTableResponseTypeDef]:
        pass
```
## GetStatementResultPaginator

Type annotations for `boto3.client("redshift-data").get_paginator("get_statement_result")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import GetStatementResultPaginator

def get_get_statement_result_paginator() -> GetStatementResultPaginator:
    return boto3.client("redshift-data").get_paginator("get_statement_result")
```

[Paginator.GetStatementResult documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.GetStatementResult)

```python
class GetStatementResultPaginator(Boto3Paginator):
    def paginate(
        self,
        Id: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetStatementResultResponseTypeDef]:
        pass
```
## ListDatabasesPaginator

Type annotations for `boto3.client("redshift-data").get_paginator("list_databases")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import ListDatabasesPaginator

def get_list_databases_paginator() -> ListDatabasesPaginator:
    return boto3.client("redshift-data").get_paginator("list_databases")
```

[Paginator.ListDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListDatabases)

```python
class ListDatabasesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str = None,
        DbUser: str = None,
        SecretArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatabasesResponseTypeDef]:
        pass
```
## ListSchemasPaginator

Type annotations for `boto3.client("redshift-data").get_paginator("list_schemas")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import ListSchemasPaginator

def get_list_schemas_paginator() -> ListSchemasPaginator:
    return boto3.client("redshift-data").get_paginator("list_schemas")
```

[Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListSchemas)

```python
class ListSchemasPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str,
        ConnectedDatabase: str = None,
        DbUser: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasResponseTypeDef]:
        pass
```
## ListStatementsPaginator

Type annotations for `boto3.client("redshift-data").get_paginator("list_statements")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import ListStatementsPaginator

def get_list_statements_paginator() -> ListStatementsPaginator:
    return boto3.client("redshift-data").get_paginator("list_statements")
```

[Paginator.ListStatements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListStatements)

```python
class ListStatementsPaginator(Boto3Paginator):
    def paginate(
        self,
        RoleLevel: bool = None,
        StatementName: str = None,
        Status: StatusString = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStatementsResponseTypeDef]:
        pass
```
## ListTablesPaginator

Type annotations for `boto3.client("redshift-data").get_paginator("list_tables")`.

Can be used directly:

```python
from mypy_boto3_redshift_data.paginators import ListTablesPaginator

def get_list_tables_paginator() -> ListTablesPaginator:
    return boto3.client("redshift-data").get_paginator("list_tables")
```

[Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListTables)

```python
class ListTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str,
        ConnectedDatabase: str = None,
        DbUser: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        TablePattern: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTablesResponseTypeDef]:
        pass
```