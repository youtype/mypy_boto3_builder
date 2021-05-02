# Paginators for boto3 Athena module

> [Index](../index.md) > [Athena](./index.md) > Paginators

Auto-generated documentation for [Athena](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena)
type annotations stubs module [mypy_boto3_athena](https://pypi.org/project/mypy-boto3-athena/).

- [Paginators for boto3 Athena module](#paginators-for-boto3-athena-module)
  - [GetQueryResultsPaginator](#getqueryresultspaginator)
  - [ListDataCatalogsPaginator](#listdatacatalogspaginator)
  - [ListDatabasesPaginator](#listdatabasespaginator)
  - [ListNamedQueriesPaginator](#listnamedqueriespaginator)
  - [ListQueryExecutionsPaginator](#listqueryexecutionspaginator)
  - [ListTableMetadataPaginator](#listtablemetadatapaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)

## GetQueryResultsPaginator

Type annotations for `boto3.client("athena").get_paginator("get_query_results")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import GetQueryResultsPaginator

def get_get_query_results_paginator() -> GetQueryResultsPaginator:
    return boto3.client("athena").get_paginator("get_query_results")
```

[Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.GetQueryResults)

```python
class GetQueryResultsPaginator(Boto3Paginator):
    def paginate(
        self,
        QueryExecutionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetQueryResultsOutputTypeDef]:
        pass
```
## ListDataCatalogsPaginator

Type annotations for `boto3.client("athena").get_paginator("list_data_catalogs")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import ListDataCatalogsPaginator

def get_list_data_catalogs_paginator() -> ListDataCatalogsPaginator:
    return boto3.client("athena").get_paginator("list_data_catalogs")
```

[Paginator.ListDataCatalogs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.ListDataCatalogs)

```python
class ListDataCatalogsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataCatalogsOutputTypeDef]:
        pass
```
## ListDatabasesPaginator

Type annotations for `boto3.client("athena").get_paginator("list_databases")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import ListDatabasesPaginator

def get_list_databases_paginator() -> ListDatabasesPaginator:
    return boto3.client("athena").get_paginator("list_databases")
```

[Paginator.ListDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.ListDatabases)

```python
class ListDatabasesPaginator(Boto3Paginator):
    def paginate(
        self,
        CatalogName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatabasesOutputTypeDef]:
        pass
```
## ListNamedQueriesPaginator

Type annotations for `boto3.client("athena").get_paginator("list_named_queries")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import ListNamedQueriesPaginator

def get_list_named_queries_paginator() -> ListNamedQueriesPaginator:
    return boto3.client("athena").get_paginator("list_named_queries")
```

[Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.ListNamedQueries)

```python
class ListNamedQueriesPaginator(Boto3Paginator):
    def paginate(
        self,
        WorkGroup: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamedQueriesOutputTypeDef]:
        pass
```
## ListQueryExecutionsPaginator

Type annotations for `boto3.client("athena").get_paginator("list_query_executions")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import ListQueryExecutionsPaginator

def get_list_query_executions_paginator() -> ListQueryExecutionsPaginator:
    return boto3.client("athena").get_paginator("list_query_executions")
```

[Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)

```python
class ListQueryExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        WorkGroup: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueryExecutionsOutputTypeDef]:
        pass
```
## ListTableMetadataPaginator

Type annotations for `boto3.client("athena").get_paginator("list_table_metadata")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import ListTableMetadataPaginator

def get_list_table_metadata_paginator() -> ListTableMetadataPaginator:
    return boto3.client("athena").get_paginator("list_table_metadata")
```

[Paginator.ListTableMetadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.ListTableMetadata)

```python
class ListTableMetadataPaginator(Boto3Paginator):
    def paginate(
        self,
        CatalogName: str,
        DatabaseName: str,
        Expression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableMetadataOutputTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("athena").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_athena.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("athena").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        pass
```