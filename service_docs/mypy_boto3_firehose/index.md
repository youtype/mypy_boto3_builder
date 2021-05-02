# Type annotations for boto3 Firehose module

> [Index](../index.md) > Firehose

Auto-generated documentation for [Firehose](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose)
type annotations stubs module [mypy_boto3_firehose](https://pypi.org/project/mypy-boto3-firehose/).

```bash
pip install mypy-boto3-firehose
```

- [Type annotations for boto3 Firehose module](#type-annotations-for-boto3-firehose-module)
  - [FirehoseClient](#firehoseclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## FirehoseClient

Type annotations for  `boto3.client("firehose")` as [FirehoseClient](./client.md)

Can be used directly:

```python
from mypy_boto3_firehose.client import FirehoseClient
```


FirehoseClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_delivery_stream](./client.md#create-delivery-stream)
- [delete_delivery_stream](./client.md#delete-delivery-stream)
- [describe_delivery_stream](./client.md#describe-delivery-stream)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_delivery_streams](./client.md#list-delivery-streams)
- [list_tags_for_delivery_stream](./client.md#list-tags-for-delivery-stream)
- [put_record](./client.md#put-record)
- [put_record_batch](./client.md#put-record-batch)
- [start_delivery_stream_encryption](./client.md#start-delivery-stream-encryption)
- [stop_delivery_stream_encryption](./client.md#stop-delivery-stream-encryption)
- [tag_delivery_stream](./client.md#tag-delivery-stream)
- [untag_delivery_stream](./client.md#untag-delivery-stream)
- [update_destination](./client.md#update-destination)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidKMSResourceException](./client.md#invalidkmsresourceexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_firehose.literals import CompressionFormat, ...
```

- [CompressionFormat](./literals.md#compressionformat)
- [ContentEncoding](./literals.md#contentencoding)
- [DeliveryStreamEncryptionStatus](./literals.md#deliverystreamencryptionstatus)
- [DeliveryStreamFailureType](./literals.md#deliverystreamfailuretype)
- [DeliveryStreamStatus](./literals.md#deliverystreamstatus)
- [DeliveryStreamType](./literals.md#deliverystreamtype)
- [ElasticsearchIndexRotationPeriod](./literals.md#elasticsearchindexrotationperiod)
- [ElasticsearchS3BackupMode](./literals.md#elasticsearchs3backupmode)
- [HECEndpointType](./literals.md#hecendpointtype)
- [HttpEndpointS3BackupMode](./literals.md#httpendpoints3backupmode)
- [KeyType](./literals.md#keytype)
- [NoEncryptionConfig](./literals.md#noencryptionconfig)
- [OrcCompression](./literals.md#orccompression)
- [OrcFormatVersion](./literals.md#orcformatversion)
- [ParquetCompression](./literals.md#parquetcompression)
- [ParquetWriterVersion](./literals.md#parquetwriterversion)
- [ProcessorParameterName](./literals.md#processorparametername)
- [ProcessorType](./literals.md#processortype)
- [RedshiftS3BackupMode](./literals.md#redshifts3backupmode)
- [S3BackupMode](./literals.md#s3backupmode)
- [SplunkS3BackupMode](./literals.md#splunks3backupmode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_firehose.type_defs import BufferingHintsTypeDef, ...
```

- [BufferingHintsTypeDef](./type_defs.md#bufferinghintstypedef)
- [CloudWatchLoggingOptionsTypeDef](./type_defs.md#cloudwatchloggingoptionstypedef)
- [CopyCommandTypeDef](./type_defs.md#copycommandtypedef)
- [CreateDeliveryStreamOutputTypeDef](./type_defs.md#createdeliverystreamoutputtypedef)
- [DataFormatConversionConfigurationTypeDef](./type_defs.md#dataformatconversionconfigurationtypedef)
- [DeliveryStreamDescriptionTypeDef](./type_defs.md#deliverystreamdescriptiontypedef)
- [DeliveryStreamEncryptionConfigurationInputTypeDef](./type_defs.md#deliverystreamencryptionconfigurationinputtypedef)
- [DeliveryStreamEncryptionConfigurationTypeDef](./type_defs.md#deliverystreamencryptionconfigurationtypedef)
- [DescribeDeliveryStreamOutputTypeDef](./type_defs.md#describedeliverystreamoutputtypedef)
- [DeserializerTypeDef](./type_defs.md#deserializertypedef)
- [DestinationDescriptionTypeDef](./type_defs.md#destinationdescriptiontypedef)
- [ElasticsearchBufferingHintsTypeDef](./type_defs.md#elasticsearchbufferinghintstypedef)
- [ElasticsearchDestinationConfigurationTypeDef](./type_defs.md#elasticsearchdestinationconfigurationtypedef)
- [ElasticsearchDestinationDescriptionTypeDef](./type_defs.md#elasticsearchdestinationdescriptiontypedef)
- [ElasticsearchDestinationUpdateTypeDef](./type_defs.md#elasticsearchdestinationupdatetypedef)
- [ElasticsearchRetryOptionsTypeDef](./type_defs.md#elasticsearchretryoptionstypedef)
- [EncryptionConfigurationTypeDef](./type_defs.md#encryptionconfigurationtypedef)
- [ExtendedS3DestinationConfigurationTypeDef](./type_defs.md#extendeds3destinationconfigurationtypedef)
- [ExtendedS3DestinationDescriptionTypeDef](./type_defs.md#extendeds3destinationdescriptiontypedef)
- [ExtendedS3DestinationUpdateTypeDef](./type_defs.md#extendeds3destinationupdatetypedef)
- [FailureDescriptionTypeDef](./type_defs.md#failuredescriptiontypedef)
- [HiveJsonSerDeTypeDef](./type_defs.md#hivejsonserdetypedef)
- [HttpEndpointBufferingHintsTypeDef](./type_defs.md#httpendpointbufferinghintstypedef)
- [HttpEndpointCommonAttributeTypeDef](./type_defs.md#httpendpointcommonattributetypedef)
- [HttpEndpointConfigurationTypeDef](./type_defs.md#httpendpointconfigurationtypedef)
- [HttpEndpointDescriptionTypeDef](./type_defs.md#httpendpointdescriptiontypedef)
- [HttpEndpointDestinationConfigurationTypeDef](./type_defs.md#httpendpointdestinationconfigurationtypedef)
- [HttpEndpointDestinationDescriptionTypeDef](./type_defs.md#httpendpointdestinationdescriptiontypedef)
- [HttpEndpointDestinationUpdateTypeDef](./type_defs.md#httpendpointdestinationupdatetypedef)
- [HttpEndpointRequestConfigurationTypeDef](./type_defs.md#httpendpointrequestconfigurationtypedef)
- [HttpEndpointRetryOptionsTypeDef](./type_defs.md#httpendpointretryoptionstypedef)
- [InputFormatConfigurationTypeDef](./type_defs.md#inputformatconfigurationtypedef)
- [KMSEncryptionConfigTypeDef](./type_defs.md#kmsencryptionconfigtypedef)
- [KinesisStreamSourceConfigurationTypeDef](./type_defs.md#kinesisstreamsourceconfigurationtypedef)
- [KinesisStreamSourceDescriptionTypeDef](./type_defs.md#kinesisstreamsourcedescriptiontypedef)
- [ListDeliveryStreamsOutputTypeDef](./type_defs.md#listdeliverystreamsoutputtypedef)
- [ListTagsForDeliveryStreamOutputTypeDef](./type_defs.md#listtagsfordeliverystreamoutputtypedef)
- [OpenXJsonSerDeTypeDef](./type_defs.md#openxjsonserdetypedef)
- [OrcSerDeTypeDef](./type_defs.md#orcserdetypedef)
- [OutputFormatConfigurationTypeDef](./type_defs.md#outputformatconfigurationtypedef)
- [ParquetSerDeTypeDef](./type_defs.md#parquetserdetypedef)
- [ProcessingConfigurationTypeDef](./type_defs.md#processingconfigurationtypedef)
- [ProcessorParameterTypeDef](./type_defs.md#processorparametertypedef)
- [ProcessorTypeDef](./type_defs.md#processortypedef)
- [PutRecordBatchOutputTypeDef](./type_defs.md#putrecordbatchoutputtypedef)
- [PutRecordBatchResponseEntryTypeDef](./type_defs.md#putrecordbatchresponseentrytypedef)
- [PutRecordOutputTypeDef](./type_defs.md#putrecordoutputtypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [RedshiftDestinationConfigurationTypeDef](./type_defs.md#redshiftdestinationconfigurationtypedef)
- [RedshiftDestinationDescriptionTypeDef](./type_defs.md#redshiftdestinationdescriptiontypedef)
- [RedshiftDestinationUpdateTypeDef](./type_defs.md#redshiftdestinationupdatetypedef)
- [RedshiftRetryOptionsTypeDef](./type_defs.md#redshiftretryoptionstypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3DestinationConfigurationTypeDef](./type_defs.md#s3destinationconfigurationtypedef)
- [S3DestinationDescriptionTypeDef](./type_defs.md#s3destinationdescriptiontypedef)
- [S3DestinationUpdateTypeDef](./type_defs.md#s3destinationupdatetypedef)
- [SchemaConfigurationTypeDef](./type_defs.md#schemaconfigurationtypedef)
- [SerializerTypeDef](./type_defs.md#serializertypedef)
- [SourceDescriptionTypeDef](./type_defs.md#sourcedescriptiontypedef)
- [SplunkDestinationConfigurationTypeDef](./type_defs.md#splunkdestinationconfigurationtypedef)
- [SplunkDestinationDescriptionTypeDef](./type_defs.md#splunkdestinationdescriptiontypedef)
- [SplunkDestinationUpdateTypeDef](./type_defs.md#splunkdestinationupdatetypedef)
- [SplunkRetryOptionsTypeDef](./type_defs.md#splunkretryoptionstypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [VpcConfigurationDescriptionTypeDef](./type_defs.md#vpcconfigurationdescriptiontypedef)
- [VpcConfigurationTypeDef](./type_defs.md#vpcconfigurationtypedef)
