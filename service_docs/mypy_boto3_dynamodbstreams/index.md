# Type annotations for boto3 DynamoDBStreams module

> [Index](../index.md) > DynamoDBStreams

Auto-generated documentation for [DynamoDBStreams](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams)
type annotations stubs module [mypy_boto3_dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/).

```bash
pip install mypy-boto3-dynamodbstreams
```

- [Type annotations for boto3 DynamoDBStreams module](#type-annotations-for-boto3-dynamodbstreams-module)
  - [DynamoDBStreamsClient](#dynamodbstreamsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## DynamoDBStreamsClient

Type annotations for  `boto3.client("dynamodbstreams")` as [DynamoDBStreamsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_dynamodbstreams.client import DynamoDBStreamsClient
```


DynamoDBStreamsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_stream](./client.md#describe-stream)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_records](./client.md#get-records)
- [get_shard_iterator](./client.md#get-shard-iterator)
- [list_streams](./client.md#list-streams)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ExpiredIteratorException](./client.md#expirediteratorexception)
- [InternalServerError](./client.md#internalservererror)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TrimmedDataAccessException](./client.md#trimmeddataaccessexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dynamodbstreams.literals import KeyType, ...
```

- [KeyType](./literals.md#keytype)
- [OperationType](./literals.md#operationtype)
- [ShardIteratorType](./literals.md#sharditeratortype)
- [StreamStatus](./literals.md#streamstatus)
- [StreamViewType](./literals.md#streamviewtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dynamodbstreams.type_defs import IdentityTypeDef, ...
```

- [IdentityTypeDef](./type_defs.md#identitytypedef)
- [KeySchemaElementTypeDef](./type_defs.md#keyschemaelementtypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SequenceNumberRangeTypeDef](./type_defs.md#sequencenumberrangetypedef)
- [ShardTypeDef](./type_defs.md#shardtypedef)
- [StreamDescriptionTypeDef](./type_defs.md#streamdescriptiontypedef)
- [StreamRecordTypeDef](./type_defs.md#streamrecordtypedef)
- [StreamTypeDef](./type_defs.md#streamtypedef)
- [DescribeStreamOutputTypeDef](./type_defs.md#describestreamoutputtypedef)
- [AttributeValueTypeDef](./type_defs.md#attributevaluetypedef)
- [GetRecordsOutputTypeDef](./type_defs.md#getrecordsoutputtypedef)
- [GetShardIteratorOutputTypeDef](./type_defs.md#getsharditeratoroutputtypedef)
- [ListStreamsOutputTypeDef](./type_defs.md#liststreamsoutputtypedef)
