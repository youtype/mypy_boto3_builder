# RDSDataServiceClient for boto3 RDSDataService module

> [Index](../index.md) > [RDSDataService](./index.md) > RDSDataServiceClient

Auto-generated documentation for [RDSDataService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService)
type annotations stubs module [mypy_boto3_rds_data](https://pypi.org/project/mypy-boto3-rds-data/).

- [RDSDataServiceClient for boto3 RDSDataService module](#rdsdataserviceclient-for-boto3-rdsdataservice-module)
  - [RDSDataServiceClient](#rdsdataserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_execute_statement](#batch_execute_statement)
    - [begin_transaction](#begin_transaction)
    - [can_paginate](#can_paginate)
    - [commit_transaction](#commit_transaction)
    - [execute_sql](#execute_sql)
    - [execute_statement](#execute_statement)
    - [generate_presigned_url](#generate_presigned_url)
    - [rollback_transaction](#rollback_transaction)

## RDSDataServiceClient

Type annotations for `boto3.client("rds-data")`

Can be used directly:

```python
from mypy_boto3_rds_data.client import RDSDataServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_rds_data.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceUnavailableError`
- `Exceptions.StatementTimeoutException`


## Methods


### batch_execute_statement

Type annotations for `boto3.client("rds-data").batch_execute_statement` method.

[Client.batch_execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.batch_execute_statement)

```python
def batch_execute_statement(
    self,
    resourceArn: str,
    secretArn: str,
    sql: str,
    database: str = None,
    parameterSets: List[List[SqlParameterTypeDef]] = None,
    schema: str = None,
    transactionId: str = None
) -> BatchExecuteStatementResponseTypeDef:
    pass
```

### begin_transaction

Type annotations for `boto3.client("rds-data").begin_transaction` method.

[Client.begin_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.begin_transaction)

```python
def begin_transaction(
    self,
    resourceArn: str,
    secretArn: str,
    database: str = None,
    schema: str = None
) -> BeginTransactionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("rds-data").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### commit_transaction

Type annotations for `boto3.client("rds-data").commit_transaction` method.

[Client.commit_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.commit_transaction)

```python
def commit_transaction(
    self,
    resourceArn: str,
    secretArn: str,
    transactionId: str
) -> CommitTransactionResponseTypeDef:
    pass
```

### execute_sql

Type annotations for `boto3.client("rds-data").execute_sql` method.

[Client.execute_sql documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.execute_sql)

```python
def execute_sql(
    self,
    awsSecretStoreArn: str,
    dbClusterOrInstanceArn: str,
    sqlStatements: str,
    database: str = None,
    schema: str = None
) -> ExecuteSqlResponseTypeDef:
    pass
```

### execute_statement

Type annotations for `boto3.client("rds-data").execute_statement` method.

[Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.execute_statement)

```python
def execute_statement(
    self,
    resourceArn: str,
    secretArn: str,
    sql: str,
    continueAfterTimeout: bool = None,
    database: str = None,
    includeResultMetadata: bool = None,
    parameters: List[SqlParameterTypeDef] = None,
    resultSetOptions: ResultSetOptionsTypeDef = None,
    schema: str = None,
    transactionId: str = None
) -> ExecuteStatementResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("rds-data").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.generate_presigned_url)

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

### rollback_transaction

Type annotations for `boto3.client("rds-data").rollback_transaction` method.

[Client.rollback_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.rollback_transaction)

```python
def rollback_transaction(
    self,
    resourceArn: str,
    secretArn: str,
    transactionId: str
) -> RollbackTransactionResponseTypeDef:
    pass
```



