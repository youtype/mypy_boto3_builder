# Type annotations for boto3 TimestreamWrite module

> [Index](../index.md) > TimestreamWrite

Auto-generated documentation for [TimestreamWrite](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite)
type annotations stubs module [mypy_boto3_timestream_write](https://pypi.org/project/mypy-boto3-timestream-write/).

```bash
pip install mypy-boto3-timestream-write
```

- [Type annotations for boto3 TimestreamWrite module](#type-annotations-for-boto3-timestreamwrite-module)
  - [TimestreamWriteClient](#timestreamwriteclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## TimestreamWriteClient

Type annotations for  `boto3.client("timestream-write")` as [TimestreamWriteClient](./client.md)

Can be used directly:

```python
from mypy_boto3_timestream_write.client import TimestreamWriteClient
```


TimestreamWriteClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_database](./client.md#create-database)
- [create_table](./client.md#create-table)
- [delete_database](./client.md#delete-database)
- [delete_table](./client.md#delete-table)
- [describe_database](./client.md#describe-database)
- [describe_endpoints](./client.md#describe-endpoints)
- [describe_table](./client.md#describe-table)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_databases](./client.md#list-databases)
- [list_tables](./client.md#list-tables)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_database](./client.md#update-database)
- [update_table](./client.md#update-table)
- [write_records](./client.md#write-records)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidEndpointException](./client.md#invalidendpointexception)
- [RejectedRecordsException](./client.md#rejectedrecordsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_timestream_write.literals import DimensionValueType, ...
```

- [DimensionValueType](./literals.md#dimensionvaluetype)
- [MeasureValueType](./literals.md#measurevaluetype)
- [TableStatus](./literals.md#tablestatus)
- [TimeUnit](./literals.md#timeunit)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_timestream_write.type_defs import CreateDatabaseResponseTypeDef, ...
```

- [CreateDatabaseResponseTypeDef](./type_defs.md#createdatabaseresponsetypedef)
- [CreateTableResponseTypeDef](./type_defs.md#createtableresponsetypedef)
- [DatabaseTypeDef](./type_defs.md#databasetypedef)
- [DescribeDatabaseResponseTypeDef](./type_defs.md#describedatabaseresponsetypedef)
- [DescribeEndpointsResponseTypeDef](./type_defs.md#describeendpointsresponsetypedef)
- [DescribeTableResponseTypeDef](./type_defs.md#describetableresponsetypedef)
- [DimensionTypeDef](./type_defs.md#dimensiontypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [ListDatabasesResponseTypeDef](./type_defs.md#listdatabasesresponsetypedef)
- [ListTablesResponseTypeDef](./type_defs.md#listtablesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [RetentionPropertiesTypeDef](./type_defs.md#retentionpropertiestypedef)
- [TableTypeDef](./type_defs.md#tabletypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateDatabaseResponseTypeDef](./type_defs.md#updatedatabaseresponsetypedef)
- [UpdateTableResponseTypeDef](./type_defs.md#updatetableresponsetypedef)
