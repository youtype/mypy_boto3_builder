# AthenaClient for boto3 Athena module

> [Index](../index.md) > [Athena](./index.md) > AthenaClient

Auto-generated documentation for [Athena](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena)
type annotations stubs module [mypy_boto3_athena](https://pypi.org/project/mypy-boto3-athena/).

- [AthenaClient for boto3 Athena module](#athenaclient-for-boto3-athena-module)
  - [AthenaClient](#athenaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_get_named_query](#batch_get_named_query)
    - [batch_get_query_execution](#batch_get_query_execution)
    - [can_paginate](#can_paginate)
    - [create_data_catalog](#create_data_catalog)
    - [create_named_query](#create_named_query)
    - [create_prepared_statement](#create_prepared_statement)
    - [create_work_group](#create_work_group)
    - [delete_data_catalog](#delete_data_catalog)
    - [delete_named_query](#delete_named_query)
    - [delete_prepared_statement](#delete_prepared_statement)
    - [delete_work_group](#delete_work_group)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_data_catalog](#get_data_catalog)
    - [get_database](#get_database)
    - [get_named_query](#get_named_query)
    - [get_prepared_statement](#get_prepared_statement)
    - [get_query_execution](#get_query_execution)
    - [get_query_results](#get_query_results)
    - [get_table_metadata](#get_table_metadata)
    - [get_work_group](#get_work_group)
    - [list_data_catalogs](#list_data_catalogs)
    - [list_databases](#list_databases)
    - [list_engine_versions](#list_engine_versions)
    - [list_named_queries](#list_named_queries)
    - [list_prepared_statements](#list_prepared_statements)
    - [list_query_executions](#list_query_executions)
    - [list_table_metadata](#list_table_metadata)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_work_groups](#list_work_groups)
    - [start_query_execution](#start_query_execution)
    - [stop_query_execution](#stop_query_execution)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_data_catalog](#update_data_catalog)
    - [update_prepared_statement](#update_prepared_statement)
    - [update_work_group](#update_work_group)
    - [get_paginator](#get_paginator)

## AthenaClient

Type annotations for `boto3.client("athena")`

Can be used directly:

```python
from mypy_boto3_athena.client import AthenaClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_athena.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidRequestException`
- `Exceptions.MetadataException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### batch_get_named_query

Type annotations for `boto3.client("athena").batch_get_named_query` method.

[Client.batch_get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.batch_get_named_query)

```python
def batch_get_named_query(
    self,
    NamedQueryIds: List[str]
) -> BatchGetNamedQueryOutputTypeDef:
    pass
```

### batch_get_query_execution

Type annotations for `boto3.client("athena").batch_get_query_execution` method.

[Client.batch_get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.batch_get_query_execution)

```python
def batch_get_query_execution(
    self,
    QueryExecutionIds: List[str]
) -> BatchGetQueryExecutionOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("athena").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_data_catalog

Type annotations for `boto3.client("athena").create_data_catalog` method.

[Client.create_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_data_catalog)

```python
def create_data_catalog(
    self,
    Name: str,
    Type: DataCatalogType,
    Description: str = None,
    Parameters: Dict[str, str] = None,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### create_named_query

Type annotations for `boto3.client("athena").create_named_query` method.

[Client.create_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_named_query)

```python
def create_named_query(
    self,
    Name: str,
    Database: str,
    QueryString: str,
    Description: str = None,
    ClientRequestToken: str = None,
    WorkGroup: str = None
) -> CreateNamedQueryOutputTypeDef:
    pass
```

### create_prepared_statement

Type annotations for `boto3.client("athena").create_prepared_statement` method.

[Client.create_prepared_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_prepared_statement)

```python
def create_prepared_statement(
    self,
    StatementName: str,
    WorkGroup: str,
    QueryStatement: str,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### create_work_group

Type annotations for `boto3.client("athena").create_work_group` method.

[Client.create_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_work_group)

```python
def create_work_group(
    self,
    Name: str,
    Configuration: "WorkGroupConfigurationTypeDef" = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### delete_data_catalog

Type annotations for `boto3.client("athena").delete_data_catalog` method.

[Client.delete_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_data_catalog)

```python
def delete_data_catalog(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_named_query

Type annotations for `boto3.client("athena").delete_named_query` method.

[Client.delete_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_named_query)

```python
def delete_named_query(
    self,
    NamedQueryId: str
) -> Dict[str, Any]:
    pass
```

### delete_prepared_statement

Type annotations for `boto3.client("athena").delete_prepared_statement` method.

[Client.delete_prepared_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_prepared_statement)

```python
def delete_prepared_statement(
    self,
    StatementName: str,
    WorkGroup: str
) -> Dict[str, Any]:
    pass
```

### delete_work_group

Type annotations for `boto3.client("athena").delete_work_group` method.

[Client.delete_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_work_group)

```python
def delete_work_group(
    self,
    WorkGroup: str,
    RecursiveDeleteOption: bool = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("athena").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.generate_presigned_url)

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

### get_data_catalog

Type annotations for `boto3.client("athena").get_data_catalog` method.

[Client.get_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_data_catalog)

```python
def get_data_catalog(
    self,
    Name: str
) -> GetDataCatalogOutputTypeDef:
    pass
```

### get_database

Type annotations for `boto3.client("athena").get_database` method.

[Client.get_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_database)

```python
def get_database(
    self,
    CatalogName: str,
    DatabaseName: str
) -> GetDatabaseOutputTypeDef:
    pass
```

### get_named_query

Type annotations for `boto3.client("athena").get_named_query` method.

[Client.get_named_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_named_query)

```python
def get_named_query(
    self,
    NamedQueryId: str
) -> GetNamedQueryOutputTypeDef:
    pass
```

### get_prepared_statement

Type annotations for `boto3.client("athena").get_prepared_statement` method.

[Client.get_prepared_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_prepared_statement)

```python
def get_prepared_statement(
    self,
    StatementName: str,
    WorkGroup: str
) -> GetPreparedStatementOutputTypeDef:
    pass
```

### get_query_execution

Type annotations for `boto3.client("athena").get_query_execution` method.

[Client.get_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_query_execution)

```python
def get_query_execution(
    self,
    QueryExecutionId: str
) -> GetQueryExecutionOutputTypeDef:
    pass
```

### get_query_results

Type annotations for `boto3.client("athena").get_query_results` method.

[Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_query_results)

```python
def get_query_results(
    self,
    QueryExecutionId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> GetQueryResultsOutputTypeDef:
    pass
```

### get_table_metadata

Type annotations for `boto3.client("athena").get_table_metadata` method.

[Client.get_table_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_table_metadata)

```python
def get_table_metadata(
    self,
    CatalogName: str,
    DatabaseName: str,
    TableName: str
) -> GetTableMetadataOutputTypeDef:
    pass
```

### get_work_group

Type annotations for `boto3.client("athena").get_work_group` method.

[Client.get_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_work_group)

```python
def get_work_group(
    self,
    WorkGroup: str
) -> GetWorkGroupOutputTypeDef:
    pass
```

### list_data_catalogs

Type annotations for `boto3.client("athena").list_data_catalogs` method.

[Client.list_data_catalogs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_data_catalogs)

```python
def list_data_catalogs(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDataCatalogsOutputTypeDef:
    pass
```

### list_databases

Type annotations for `boto3.client("athena").list_databases` method.

[Client.list_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_databases)

```python
def list_databases(
    self,
    CatalogName: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDatabasesOutputTypeDef:
    pass
```

### list_engine_versions

Type annotations for `boto3.client("athena").list_engine_versions` method.

[Client.list_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_engine_versions)

```python
def list_engine_versions(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEngineVersionsOutputTypeDef:
    pass
```

### list_named_queries

Type annotations for `boto3.client("athena").list_named_queries` method.

[Client.list_named_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_named_queries)

```python
def list_named_queries(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    WorkGroup: str = None
) -> ListNamedQueriesOutputTypeDef:
    pass
```

### list_prepared_statements

Type annotations for `boto3.client("athena").list_prepared_statements` method.

[Client.list_prepared_statements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_prepared_statements)

```python
def list_prepared_statements(
    self,
    WorkGroup: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPreparedStatementsOutputTypeDef:
    pass
```

### list_query_executions

Type annotations for `boto3.client("athena").list_query_executions` method.

[Client.list_query_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_query_executions)

```python
def list_query_executions(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    WorkGroup: str = None
) -> ListQueryExecutionsOutputTypeDef:
    pass
```

### list_table_metadata

Type annotations for `boto3.client("athena").list_table_metadata` method.

[Client.list_table_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_table_metadata)

```python
def list_table_metadata(
    self,
    CatalogName: str,
    DatabaseName: str,
    Expression: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTableMetadataOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("athena").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_work_groups

Type annotations for `boto3.client("athena").list_work_groups` method.

[Client.list_work_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_work_groups)

```python
def list_work_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkGroupsOutputTypeDef:
    pass
```

### start_query_execution

Type annotations for `boto3.client("athena").start_query_execution` method.

[Client.start_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.start_query_execution)

```python
def start_query_execution(
    self,
    QueryString: str,
    ClientRequestToken: str = None,
    QueryExecutionContext: "QueryExecutionContextTypeDef" = None,
    ResultConfiguration: "ResultConfigurationTypeDef" = None,
    WorkGroup: str = None
) -> StartQueryExecutionOutputTypeDef:
    pass
```

### stop_query_execution

Type annotations for `boto3.client("athena").stop_query_execution` method.

[Client.stop_query_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.stop_query_execution)

```python
def stop_query_execution(
    self,
    QueryExecutionId: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("athena").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("athena").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_data_catalog

Type annotations for `boto3.client("athena").update_data_catalog` method.

[Client.update_data_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_data_catalog)

```python
def update_data_catalog(
    self,
    Name: str,
    Type: DataCatalogType,
    Description: str = None,
    Parameters: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### update_prepared_statement

Type annotations for `boto3.client("athena").update_prepared_statement` method.

[Client.update_prepared_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_prepared_statement)

```python
def update_prepared_statement(
    self,
    StatementName: str,
    WorkGroup: str,
    QueryStatement: str,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### update_work_group

Type annotations for `boto3.client("athena").update_work_group` method.

[Client.update_work_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_work_group)

```python
def update_work_group(
    self,
    WorkGroup: str,
    Description: str = None,
    ConfigurationUpdates: WorkGroupConfigurationUpdatesTypeDef = None,
    State: WorkGroupState = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("athena").get_paginator` method with overloads.

- `client.get_paginator("get_query_results")` -> [GetQueryResultsPaginator](./paginators.md#getqueryresultspaginator)
- `client.get_paginator("list_data_catalogs")` -> [ListDataCatalogsPaginator](./paginators.md#listdatacatalogspaginator)
- `client.get_paginator("list_databases")` -> [ListDatabasesPaginator](./paginators.md#listdatabasespaginator)
- `client.get_paginator("list_named_queries")` -> [ListNamedQueriesPaginator](./paginators.md#listnamedqueriespaginator)
- `client.get_paginator("list_query_executions")` -> [ListQueryExecutionsPaginator](./paginators.md#listqueryexecutionspaginator)
- `client.get_paginator("list_table_metadata")` -> [ListTableMetadataPaginator](./paginators.md#listtablemetadatapaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)


