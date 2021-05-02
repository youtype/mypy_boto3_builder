# Paginators for boto3 Honeycode module

> [Index](../index.md) > [Honeycode](./index.md) > Paginators

Auto-generated documentation for [Honeycode](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode)
type annotations stubs module [mypy_boto3_honeycode](https://pypi.org/project/mypy-boto3-honeycode/).

- [Paginators for boto3 Honeycode module](#paginators-for-boto3-honeycode-module)
  - [ListTableColumnsPaginator](#listtablecolumnspaginator)
  - [ListTableRowsPaginator](#listtablerowspaginator)
  - [ListTablesPaginator](#listtablespaginator)
  - [QueryTableRowsPaginator](#querytablerowspaginator)

## ListTableColumnsPaginator

Type annotations for `boto3.client("honeycode").get_paginator("list_table_columns")`.

Can be used directly:

```python
from mypy_boto3_honeycode.paginators import ListTableColumnsPaginator

def get_list_table_columns_paginator() -> ListTableColumnsPaginator:
    return boto3.client("honeycode").get_paginator("list_table_columns")
```

[Paginator.ListTableColumns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns)

```python
class ListTableColumnsPaginator(Boto3Paginator):
    def paginate(
        self,
        workbookId: str,
        tableId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableColumnsResultTypeDef]:
        pass
```
## ListTableRowsPaginator

Type annotations for `boto3.client("honeycode").get_paginator("list_table_rows")`.

Can be used directly:

```python
from mypy_boto3_honeycode.paginators import ListTableRowsPaginator

def get_list_table_rows_paginator() -> ListTableRowsPaginator:
    return boto3.client("honeycode").get_paginator("list_table_rows")
```

[Paginator.ListTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows)

```python
class ListTableRowsPaginator(Boto3Paginator):
    def paginate(
        self,
        workbookId: str,
        tableId: str,
        rowIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableRowsResultTypeDef]:
        pass
```
## ListTablesPaginator

Type annotations for `boto3.client("honeycode").get_paginator("list_tables")`.

Can be used directly:

```python
from mypy_boto3_honeycode.paginators import ListTablesPaginator

def get_list_tables_paginator() -> ListTablesPaginator:
    return boto3.client("honeycode").get_paginator("list_tables")
```

[Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.ListTables)

```python
class ListTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        workbookId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTablesResultTypeDef]:
        pass
```
## QueryTableRowsPaginator

Type annotations for `boto3.client("honeycode").get_paginator("query_table_rows")`.

Can be used directly:

```python
from mypy_boto3_honeycode.paginators import QueryTableRowsPaginator

def get_query_table_rows_paginator() -> QueryTableRowsPaginator:
    return boto3.client("honeycode").get_paginator("query_table_rows")
```

[Paginator.QueryTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows)

```python
class QueryTableRowsPaginator(Boto3Paginator):
    def paginate(
        self,
        workbookId: str,
        tableId: str,
        filterFormula: "FilterTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[QueryTableRowsResultTypeDef]:
        pass
```