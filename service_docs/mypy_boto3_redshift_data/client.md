# RedshiftDataAPIServiceClient for boto3 RedshiftDataAPIService module

> [Index](../index.md) > [RedshiftDataAPIService](./index.md) > RedshiftDataAPIServiceClient

Auto-generated documentation for [RedshiftDataAPIService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService)
type annotations stubs module [mypy_boto3_redshift_data](https://pypi.org/project/mypy-boto3-redshift-data/).

- [RedshiftDataAPIServiceClient for boto3 RedshiftDataAPIService module](#redshiftdataapiserviceclient-for-boto3-redshiftdataapiservice-module)
  - [RedshiftDataAPIServiceClient](#redshiftdataapiserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_statement](#cancel_statement)
    - [describe_statement](#describe_statement)
    - [describe_table](#describe_table)
    - [execute_statement](#execute_statement)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_statement_result](#get_statement_result)
    - [list_databases](#list_databases)
    - [list_schemas](#list_schemas)
    - [list_statements](#list_statements)
    - [list_tables](#list_tables)
    - [get_paginator](#get_paginator)

## RedshiftDataAPIServiceClient

Type annotations for `boto3.client("redshift-data")`

Can be used directly:

```python
from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_redshift_data.client import Exceptions

def handle_error(exc: Exceptions.ActiveStatementsExceededException) -> None:
    ...
```


Exceptions:

- `Exceptions.ActiveStatementsExceededException`
- `Exceptions.ClientError`
- `Exceptions.ExecuteStatementException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("redshift-data").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_statement

Type annotations for `boto3.client("redshift-data").cancel_statement` method.

[Client.cancel_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.cancel_statement)

```python
def cancel_statement(
    self,
    Id: str
) -> CancelStatementResponseTypeDef:
    pass
```

### describe_statement

Type annotations for `boto3.client("redshift-data").describe_statement` method.

[Client.describe_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_statement)

```python
def describe_statement(
    self,
    Id: str
) -> DescribeStatementResponseTypeDef:
    pass
```

### describe_table

Type annotations for `boto3.client("redshift-data").describe_table` method.

[Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_table)

```python
def describe_table(
    self,
    ClusterIdentifier: str,
    Database: str,
    ConnectedDatabase: str = None,
    DbUser: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Schema: str = None,
    SecretArn: str = None,
    Table: str = None
) -> DescribeTableResponseTypeDef:
    pass
```

### execute_statement

Type annotations for `boto3.client("redshift-data").execute_statement` method.

[Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.execute_statement)

```python
def execute_statement(
    self,
    ClusterIdentifier: str,
    Sql: str,
    Database: str = None,
    DbUser: str = None,
    SecretArn: str = None,
    StatementName: str = None,
    WithEvent: bool = None
) -> ExecuteStatementOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("redshift-data").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.generate_presigned_url)

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

### get_statement_result

Type annotations for `boto3.client("redshift-data").get_statement_result` method.

[Client.get_statement_result documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_statement_result)

```python
def get_statement_result(
    self,
    Id: str,
    NextToken: str = None
) -> GetStatementResultResponseTypeDef:
    pass
```

### list_databases

Type annotations for `boto3.client("redshift-data").list_databases` method.

[Client.list_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_databases)

```python
def list_databases(
    self,
    ClusterIdentifier: str,
    Database: str = None,
    DbUser: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    SecretArn: str = None
) -> ListDatabasesResponseTypeDef:
    pass
```

### list_schemas

Type annotations for `boto3.client("redshift-data").list_schemas` method.

[Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_schemas)

```python
def list_schemas(
    self,
    ClusterIdentifier: str,
    Database: str,
    ConnectedDatabase: str = None,
    DbUser: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    SchemaPattern: str = None,
    SecretArn: str = None
) -> ListSchemasResponseTypeDef:
    pass
```

### list_statements

Type annotations for `boto3.client("redshift-data").list_statements` method.

[Client.list_statements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_statements)

```python
def list_statements(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    RoleLevel: bool = None,
    StatementName: str = None,
    Status: StatusString = None
) -> ListStatementsResponseTypeDef:
    pass
```

### list_tables

Type annotations for `boto3.client("redshift-data").list_tables` method.

[Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_tables)

```python
def list_tables(
    self,
    ClusterIdentifier: str,
    Database: str,
    ConnectedDatabase: str = None,
    DbUser: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    SchemaPattern: str = None,
    SecretArn: str = None,
    TablePattern: str = None
) -> ListTablesResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("redshift-data").get_paginator` method with overloads.

- `client.get_paginator("describe_table")` -> [DescribeTablePaginator](./paginators.md#describetablepaginator)
- `client.get_paginator("get_statement_result")` -> [GetStatementResultPaginator](./paginators.md#getstatementresultpaginator)
- `client.get_paginator("list_databases")` -> [ListDatabasesPaginator](./paginators.md#listdatabasespaginator)
- `client.get_paginator("list_schemas")` -> [ListSchemasPaginator](./paginators.md#listschemaspaginator)
- `client.get_paginator("list_statements")` -> [ListStatementsPaginator](./paginators.md#liststatementspaginator)
- `client.get_paginator("list_tables")` -> [ListTablesPaginator](./paginators.md#listtablespaginator)


