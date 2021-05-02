# Type annotations for boto3 RDSDataService module

> [Index](../index.md) > RDSDataService

Auto-generated documentation for [RDSDataService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService)
type annotations stubs module [mypy_boto3_rds_data](https://pypi.org/project/mypy-boto3-rds-data/).

```bash
pip install mypy-boto3-rds-data
```

- [Type annotations for boto3 RDSDataService module](#type-annotations-for-boto3-rdsdataservice-module)
  - [RDSDataServiceClient](#rdsdataserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## RDSDataServiceClient

Type annotations for  `boto3.client("rds-data")` as [RDSDataServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_rds_data.client import RDSDataServiceClient
```


RDSDataServiceClient [exceptions](./client.md#exceptions)



### Methods
- [batch_execute_statement](./client.md#batch-execute-statement)
- [begin_transaction](./client.md#begin-transaction)
- [can_paginate](./client.md#can-paginate)
- [commit_transaction](./client.md#commit-transaction)
- [execute_sql](./client.md#execute-sql)
- [execute_statement](./client.md#execute-statement)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [rollback_transaction](./client.md#rollback-transaction)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceUnavailableError](./client.md#serviceunavailableerror)
- [StatementTimeoutException](./client.md#statementtimeoutexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_rds_data.literals import DecimalReturnType, ...
```

- [DecimalReturnType](./literals.md#decimalreturntype)
- [TypeHint](./literals.md#typehint)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_rds_data.type_defs import ColumnMetadataTypeDef, ...
```

- [ColumnMetadataTypeDef](./type_defs.md#columnmetadatatypedef)
- [FieldTypeDef](./type_defs.md#fieldtypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [ResultFrameTypeDef](./type_defs.md#resultframetypedef)
- [ResultSetMetadataTypeDef](./type_defs.md#resultsetmetadatatypedef)
- [SqlStatementResultTypeDef](./type_defs.md#sqlstatementresulttypedef)
- [StructValueTypeDef](./type_defs.md#structvaluetypedef)
- [UpdateResultTypeDef](./type_defs.md#updateresulttypedef)
- [BatchExecuteStatementResponseTypeDef](./type_defs.md#batchexecutestatementresponsetypedef)
- [BeginTransactionResponseTypeDef](./type_defs.md#begintransactionresponsetypedef)
- [CommitTransactionResponseTypeDef](./type_defs.md#committransactionresponsetypedef)
- [ValueTypeDef](./type_defs.md#valuetypedef)
- [ArrayValueTypeDef](./type_defs.md#arrayvaluetypedef)
- [ExecuteSqlResponseTypeDef](./type_defs.md#executesqlresponsetypedef)
- [ExecuteStatementResponseTypeDef](./type_defs.md#executestatementresponsetypedef)
- [ResultSetOptionsTypeDef](./type_defs.md#resultsetoptionstypedef)
- [RollbackTransactionResponseTypeDef](./type_defs.md#rollbacktransactionresponsetypedef)
- [SqlParameterTypeDef](./type_defs.md#sqlparametertypedef)
