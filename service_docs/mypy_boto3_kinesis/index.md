# Type annotations for boto3 Kinesis module

> [Index](../index.md) > Kinesis

Auto-generated documentation for [Kinesis](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis)
type annotations stubs module [mypy_boto3_kinesis](https://pypi.org/project/mypy-boto3-kinesis/).

```bash
pip install mypy-boto3-kinesis
```

- [Type annotations for boto3 Kinesis module](#type-annotations-for-boto3-kinesis-module)
  - [KinesisClient](#kinesisclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisClient

Type annotations for  `boto3.client("kinesis")` as [KinesisClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesis.client import KinesisClient
```


KinesisClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags_to_stream](./client.md#add-tags-to-stream)
- [can_paginate](./client.md#can-paginate)
- [create_stream](./client.md#create-stream)
- [decrease_stream_retention_period](./client.md#decrease-stream-retention-period)
- [delete_stream](./client.md#delete-stream)
- [deregister_stream_consumer](./client.md#deregister-stream-consumer)
- [describe_limits](./client.md#describe-limits)
- [describe_stream](./client.md#describe-stream)
- [describe_stream_consumer](./client.md#describe-stream-consumer)
- [describe_stream_summary](./client.md#describe-stream-summary)
- [disable_enhanced_monitoring](./client.md#disable-enhanced-monitoring)
- [enable_enhanced_monitoring](./client.md#enable-enhanced-monitoring)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_records](./client.md#get-records)
- [get_shard_iterator](./client.md#get-shard-iterator)
- [get_waiter](./client.md#get-waiter)
- [increase_stream_retention_period](./client.md#increase-stream-retention-period)
- [list_shards](./client.md#list-shards)
- [list_stream_consumers](./client.md#list-stream-consumers)
- [list_streams](./client.md#list-streams)
- [list_tags_for_stream](./client.md#list-tags-for-stream)
- [merge_shards](./client.md#merge-shards)
- [put_record](./client.md#put-record)
- [put_records](./client.md#put-records)
- [register_stream_consumer](./client.md#register-stream-consumer)
- [remove_tags_from_stream](./client.md#remove-tags-from-stream)
- [split_shard](./client.md#split-shard)
- [start_stream_encryption](./client.md#start-stream-encryption)
- [stop_stream_encryption](./client.md#stop-stream-encryption)
- [subscribe_to_shard](./client.md#subscribe-to-shard)
- [update_shard_count](./client.md#update-shard-count)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ExpiredIteratorException](./client.md#expirediteratorexception)
- [ExpiredNextTokenException](./client.md#expirednexttokenexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [KMSAccessDeniedException](./client.md#kmsaccessdeniedexception)
- [KMSDisabledException](./client.md#kmsdisabledexception)
- [KMSInvalidStateException](./client.md#kmsinvalidstateexception)
- [KMSNotFoundException](./client.md#kmsnotfoundexception)
- [KMSOptInRequired](./client.md#kmsoptinrequired)
- [KMSThrottlingException](./client.md#kmsthrottlingexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ProvisionedThroughputExceededException](./client.md#provisionedthroughputexceededexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("kinesis").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_kinesis.paginators import DescribeStreamPaginator, ...
```

- [DescribeStreamPaginator](./paginators.md#describestreampaginator)
- [ListShardsPaginator](./paginators.md#listshardspaginator)
- [ListStreamConsumersPaginator](./paginators.md#liststreamconsumerspaginator)
- [ListStreamsPaginator](./paginators.md#liststreamspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("kinesis").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_kinesis.waiters import StreamExistsWaiter, ...
```

- [StreamExistsWaiter](./waiters.md#streamexistswaiter)
- [StreamNotExistsWaiter](./waiters.md#streamnotexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis.literals import ConsumerStatus, ...
```

- [ConsumerStatus](./literals.md#consumerstatus)
- [DescribeStreamPaginatorName](./literals.md#describestreampaginatorname)
- [EncryptionType](./literals.md#encryptiontype)
- [ListShardsPaginatorName](./literals.md#listshardspaginatorname)
- [ListStreamConsumersPaginatorName](./literals.md#liststreamconsumerspaginatorname)
- [ListStreamsPaginatorName](./literals.md#liststreamspaginatorname)
- [MetricsName](./literals.md#metricsname)
- [ScalingType](./literals.md#scalingtype)
- [ShardFilterType](./literals.md#shardfiltertype)
- [ShardIteratorType](./literals.md#sharditeratortype)
- [StreamExistsWaiterName](./literals.md#streamexistswaitername)
- [StreamNotExistsWaiterName](./literals.md#streamnotexistswaitername)
- [StreamStatus](./literals.md#streamstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis.type_defs import ChildShardTypeDef, ...
```

- [ChildShardTypeDef](./type_defs.md#childshardtypedef)
- [ConsumerDescriptionTypeDef](./type_defs.md#consumerdescriptiontypedef)
- [ConsumerTypeDef](./type_defs.md#consumertypedef)
- [EnhancedMetricsTypeDef](./type_defs.md#enhancedmetricstypedef)
- [HashKeyRangeTypeDef](./type_defs.md#hashkeyrangetypedef)
- [InternalFailureExceptionTypeDef](./type_defs.md#internalfailureexceptiontypedef)
- [KMSAccessDeniedExceptionTypeDef](./type_defs.md#kmsaccessdeniedexceptiontypedef)
- [KMSDisabledExceptionTypeDef](./type_defs.md#kmsdisabledexceptiontypedef)
- [KMSInvalidStateExceptionTypeDef](./type_defs.md#kmsinvalidstateexceptiontypedef)
- [KMSNotFoundExceptionTypeDef](./type_defs.md#kmsnotfoundexceptiontypedef)
- [KMSOptInRequiredTypeDef](./type_defs.md#kmsoptinrequiredtypedef)
- [KMSThrottlingExceptionTypeDef](./type_defs.md#kmsthrottlingexceptiontypedef)
- [PutRecordsResultEntryTypeDef](./type_defs.md#putrecordsresultentrytypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [ResourceInUseExceptionTypeDef](./type_defs.md#resourceinuseexceptiontypedef)
- [ResourceNotFoundExceptionTypeDef](./type_defs.md#resourcenotfoundexceptiontypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SequenceNumberRangeTypeDef](./type_defs.md#sequencenumberrangetypedef)
- [ShardTypeDef](./type_defs.md#shardtypedef)
- [StreamDescriptionSummaryTypeDef](./type_defs.md#streamdescriptionsummarytypedef)
- [StreamDescriptionTypeDef](./type_defs.md#streamdescriptiontypedef)
- [SubscribeToShardEventStreamTypeDef](./type_defs.md#subscribetoshardeventstreamtypedef)
- [SubscribeToShardEventTypeDef](./type_defs.md#subscribetoshardeventtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [DescribeLimitsOutputTypeDef](./type_defs.md#describelimitsoutputtypedef)
- [DescribeStreamConsumerOutputTypeDef](./type_defs.md#describestreamconsumeroutputtypedef)
- [DescribeStreamOutputTypeDef](./type_defs.md#describestreamoutputtypedef)
- [DescribeStreamSummaryOutputTypeDef](./type_defs.md#describestreamsummaryoutputtypedef)
- [EnhancedMonitoringOutputTypeDef](./type_defs.md#enhancedmonitoringoutputtypedef)
- [GetRecordsOutputTypeDef](./type_defs.md#getrecordsoutputtypedef)
- [GetShardIteratorOutputTypeDef](./type_defs.md#getsharditeratoroutputtypedef)
- [ListShardsOutputTypeDef](./type_defs.md#listshardsoutputtypedef)
- [ListStreamConsumersOutputTypeDef](./type_defs.md#liststreamconsumersoutputtypedef)
- [ListStreamsOutputTypeDef](./type_defs.md#liststreamsoutputtypedef)
- [ListTagsForStreamOutputTypeDef](./type_defs.md#listtagsforstreamoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutRecordOutputTypeDef](./type_defs.md#putrecordoutputtypedef)
- [PutRecordsOutputTypeDef](./type_defs.md#putrecordsoutputtypedef)
- [PutRecordsRequestEntryTypeDef](./type_defs.md#putrecordsrequestentrytypedef)
- [RegisterStreamConsumerOutputTypeDef](./type_defs.md#registerstreamconsumeroutputtypedef)
- [ShardFilterTypeDef](./type_defs.md#shardfiltertypedef)
- [StartingPositionTypeDef](./type_defs.md#startingpositiontypedef)
- [SubscribeToShardOutputTypeDef](./type_defs.md#subscribetoshardoutputtypedef)
- [UpdateShardCountOutputTypeDef](./type_defs.md#updateshardcountoutputtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
