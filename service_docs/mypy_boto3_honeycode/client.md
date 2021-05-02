# HoneycodeClient for boto3 Honeycode module

> [Index](../index.md) > [Honeycode](./index.md) > HoneycodeClient

Auto-generated documentation for [Honeycode](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode)
type annotations stubs module [mypy_boto3_honeycode](https://pypi.org/project/mypy-boto3-honeycode/).

- [HoneycodeClient for boto3 Honeycode module](#honeycodeclient-for-boto3-honeycode-module)
  - [HoneycodeClient](#honeycodeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_create_table_rows](#batch_create_table_rows)
    - [batch_delete_table_rows](#batch_delete_table_rows)
    - [batch_update_table_rows](#batch_update_table_rows)
    - [batch_upsert_table_rows](#batch_upsert_table_rows)
    - [can_paginate](#can_paginate)
    - [describe_table_data_import_job](#describe_table_data_import_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_screen_data](#get_screen_data)
    - [invoke_screen_automation](#invoke_screen_automation)
    - [list_table_columns](#list_table_columns)
    - [list_table_rows](#list_table_rows)
    - [list_tables](#list_tables)
    - [query_table_rows](#query_table_rows)
    - [start_table_data_import_job](#start_table_data_import_job)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)

## HoneycodeClient

Type annotations for `boto3.client("honeycode")`

Can be used directly:

```python
from mypy_boto3_honeycode.client import HoneycodeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_honeycode.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AutomationExecutionException`
- `Exceptions.AutomationExecutionTimeoutException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.RequestTimeoutException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### batch_create_table_rows

Type annotations for `boto3.client("honeycode").batch_create_table_rows` method.

[Client.batch_create_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.batch_create_table_rows)

```python
def batch_create_table_rows(
    self,
    workbookId: str,
    tableId: str,
    rowsToCreate: List[CreateRowDataTypeDef],
    clientRequestToken: str = None
) -> BatchCreateTableRowsResultTypeDef:
    pass
```

### batch_delete_table_rows

Type annotations for `boto3.client("honeycode").batch_delete_table_rows` method.

[Client.batch_delete_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.batch_delete_table_rows)

```python
def batch_delete_table_rows(
    self,
    workbookId: str,
    tableId: str,
    rowIds: List[str],
    clientRequestToken: str = None
) -> BatchDeleteTableRowsResultTypeDef:
    pass
```

### batch_update_table_rows

Type annotations for `boto3.client("honeycode").batch_update_table_rows` method.

[Client.batch_update_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.batch_update_table_rows)

```python
def batch_update_table_rows(
    self,
    workbookId: str,
    tableId: str,
    rowsToUpdate: List[UpdateRowDataTypeDef],
    clientRequestToken: str = None
) -> BatchUpdateTableRowsResultTypeDef:
    pass
```

### batch_upsert_table_rows

Type annotations for `boto3.client("honeycode").batch_upsert_table_rows` method.

[Client.batch_upsert_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.batch_upsert_table_rows)

```python
def batch_upsert_table_rows(
    self,
    workbookId: str,
    tableId: str,
    rowsToUpsert: List[UpsertRowDataTypeDef],
    clientRequestToken: str = None
) -> BatchUpsertTableRowsResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("honeycode").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_table_data_import_job

Type annotations for `boto3.client("honeycode").describe_table_data_import_job` method.

[Client.describe_table_data_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.describe_table_data_import_job)

```python
def describe_table_data_import_job(
    self,
    workbookId: str,
    tableId: str,
    jobId: str
) -> DescribeTableDataImportJobResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("honeycode").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_screen_data

Type annotations for `boto3.client("honeycode").get_screen_data` method.

[Client.get_screen_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.get_screen_data)

```python
def get_screen_data(
    self,
    workbookId: str,
    appId: str,
    screenId: str,
    variables: Dict[str, VariableValueTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> GetScreenDataResultTypeDef:
    pass
```

### invoke_screen_automation

Type annotations for `boto3.client("honeycode").invoke_screen_automation` method.

[Client.invoke_screen_automation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.invoke_screen_automation)

```python
def invoke_screen_automation(
    self,
    workbookId: str,
    appId: str,
    screenId: str,
    screenAutomationId: str,
    variables: Dict[str, VariableValueTypeDef] = None,
    rowId: str = None,
    clientRequestToken: str = None
) -> InvokeScreenAutomationResultTypeDef:
    pass
```

### list_table_columns

Type annotations for `boto3.client("honeycode").list_table_columns` method.

[Client.list_table_columns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.list_table_columns)

```python
def list_table_columns(
    self,
    workbookId: str,
    tableId: str,
    nextToken: str = None
) -> ListTableColumnsResultTypeDef:
    pass
```

### list_table_rows

Type annotations for `boto3.client("honeycode").list_table_rows` method.

[Client.list_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.list_table_rows)

```python
def list_table_rows(
    self,
    workbookId: str,
    tableId: str,
    rowIds: List[str] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListTableRowsResultTypeDef:
    pass
```

### list_tables

Type annotations for `boto3.client("honeycode").list_tables` method.

[Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.list_tables)

```python
def list_tables(
    self,
    workbookId: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListTablesResultTypeDef:
    pass
```

### query_table_rows

Type annotations for `boto3.client("honeycode").query_table_rows` method.

[Client.query_table_rows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.query_table_rows)

```python
def query_table_rows(
    self,
    workbookId: str,
    tableId: str,
    filterFormula: "FilterTypeDef",
    maxResults: int = None,
    nextToken: str = None
) -> QueryTableRowsResultTypeDef:
    pass
```

### start_table_data_import_job

Type annotations for `boto3.client("honeycode").start_table_data_import_job` method.

[Client.start_table_data_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Client.start_table_data_import_job)

```python
def start_table_data_import_job(
    self,
    workbookId: str,
    dataSource: "ImportDataSourceTypeDef",
    dataFormat: ImportSourceDataFormat,
    destinationTableId: str,
    importOptions: "ImportOptionsTypeDef",
    clientRequestToken: str
) -> StartTableDataImportJobResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("honeycode").get_paginator` method.

[Paginator.ListTableColumns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTableColumnsPaginatorName
) -> ListTableColumnsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("honeycode").get_paginator` method.

[Paginator.ListTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTableRowsPaginatorName
) -> ListTableRowsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("honeycode").get_paginator` method.

[Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.ListTables)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTablesPaginatorName
) -> ListTablesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("honeycode").get_paginator` method.

[Paginator.QueryTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows)

```python
@overload
def get_paginator(
    self,
    operation_name: QueryTableRowsPaginatorName
) -> QueryTableRowsPaginator:
    pass
```