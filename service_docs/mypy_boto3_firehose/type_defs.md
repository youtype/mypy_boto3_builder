# Structures for boto3 Firehose module

> [Index](../index.md) > [Firehose](./index.md) > Structures

Auto-generated documentation for [Firehose](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose)
type annotations stubs module [mypy_boto3_firehose](https://pypi.org/project/mypy-boto3-firehose/).

- [Structures for boto3 Firehose module](#structures-for-boto3-firehose-module)
  - [BufferingHintsTypeDef](#bufferinghintstypedef)
  - [CloudWatchLoggingOptionsTypeDef](#cloudwatchloggingoptionstypedef)
  - [CopyCommandTypeDef](#copycommandtypedef)
  - [CreateDeliveryStreamOutputTypeDef](#createdeliverystreamoutputtypedef)
  - [DataFormatConversionConfigurationTypeDef](#dataformatconversionconfigurationtypedef)
  - [DeliveryStreamDescriptionTypeDef](#deliverystreamdescriptiontypedef)
  - [DeliveryStreamEncryptionConfigurationInputTypeDef](#deliverystreamencryptionconfigurationinputtypedef)
  - [DeliveryStreamEncryptionConfigurationTypeDef](#deliverystreamencryptionconfigurationtypedef)
  - [DescribeDeliveryStreamOutputTypeDef](#describedeliverystreamoutputtypedef)
  - [DeserializerTypeDef](#deserializertypedef)
  - [DestinationDescriptionTypeDef](#destinationdescriptiontypedef)
  - [ElasticsearchBufferingHintsTypeDef](#elasticsearchbufferinghintstypedef)
  - [ElasticsearchDestinationConfigurationTypeDef](#elasticsearchdestinationconfigurationtypedef)
  - [ElasticsearchDestinationDescriptionTypeDef](#elasticsearchdestinationdescriptiontypedef)
  - [ElasticsearchDestinationUpdateTypeDef](#elasticsearchdestinationupdatetypedef)
  - [ElasticsearchRetryOptionsTypeDef](#elasticsearchretryoptionstypedef)
  - [EncryptionConfigurationTypeDef](#encryptionconfigurationtypedef)
  - [ExtendedS3DestinationConfigurationTypeDef](#extendeds3destinationconfigurationtypedef)
  - [ExtendedS3DestinationDescriptionTypeDef](#extendeds3destinationdescriptiontypedef)
  - [ExtendedS3DestinationUpdateTypeDef](#extendeds3destinationupdatetypedef)
  - [FailureDescriptionTypeDef](#failuredescriptiontypedef)
  - [HiveJsonSerDeTypeDef](#hivejsonserdetypedef)
  - [HttpEndpointBufferingHintsTypeDef](#httpendpointbufferinghintstypedef)
  - [HttpEndpointCommonAttributeTypeDef](#httpendpointcommonattributetypedef)
  - [HttpEndpointConfigurationTypeDef](#httpendpointconfigurationtypedef)
  - [HttpEndpointDescriptionTypeDef](#httpendpointdescriptiontypedef)
  - [HttpEndpointDestinationConfigurationTypeDef](#httpendpointdestinationconfigurationtypedef)
  - [HttpEndpointDestinationDescriptionTypeDef](#httpendpointdestinationdescriptiontypedef)
  - [HttpEndpointDestinationUpdateTypeDef](#httpendpointdestinationupdatetypedef)
  - [HttpEndpointRequestConfigurationTypeDef](#httpendpointrequestconfigurationtypedef)
  - [HttpEndpointRetryOptionsTypeDef](#httpendpointretryoptionstypedef)
  - [InputFormatConfigurationTypeDef](#inputformatconfigurationtypedef)
  - [KMSEncryptionConfigTypeDef](#kmsencryptionconfigtypedef)
  - [KinesisStreamSourceConfigurationTypeDef](#kinesisstreamsourceconfigurationtypedef)
  - [KinesisStreamSourceDescriptionTypeDef](#kinesisstreamsourcedescriptiontypedef)
  - [ListDeliveryStreamsOutputTypeDef](#listdeliverystreamsoutputtypedef)
  - [ListTagsForDeliveryStreamOutputTypeDef](#listtagsfordeliverystreamoutputtypedef)
  - [OpenXJsonSerDeTypeDef](#openxjsonserdetypedef)
  - [OrcSerDeTypeDef](#orcserdetypedef)
  - [OutputFormatConfigurationTypeDef](#outputformatconfigurationtypedef)
  - [ParquetSerDeTypeDef](#parquetserdetypedef)
  - [ProcessingConfigurationTypeDef](#processingconfigurationtypedef)
  - [ProcessorParameterTypeDef](#processorparametertypedef)
  - [ProcessorTypeDef](#processortypedef)
  - [PutRecordBatchOutputTypeDef](#putrecordbatchoutputtypedef)
  - [PutRecordBatchResponseEntryTypeDef](#putrecordbatchresponseentrytypedef)
  - [PutRecordOutputTypeDef](#putrecordoutputtypedef)
  - [RecordTypeDef](#recordtypedef)
  - [RedshiftDestinationConfigurationTypeDef](#redshiftdestinationconfigurationtypedef)
  - [RedshiftDestinationDescriptionTypeDef](#redshiftdestinationdescriptiontypedef)
  - [RedshiftDestinationUpdateTypeDef](#redshiftdestinationupdatetypedef)
  - [RedshiftRetryOptionsTypeDef](#redshiftretryoptionstypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3DestinationConfigurationTypeDef](#s3destinationconfigurationtypedef)
  - [S3DestinationDescriptionTypeDef](#s3destinationdescriptiontypedef)
  - [S3DestinationUpdateTypeDef](#s3destinationupdatetypedef)
  - [SchemaConfigurationTypeDef](#schemaconfigurationtypedef)
  - [SerializerTypeDef](#serializertypedef)
  - [SourceDescriptionTypeDef](#sourcedescriptiontypedef)
  - [SplunkDestinationConfigurationTypeDef](#splunkdestinationconfigurationtypedef)
  - [SplunkDestinationDescriptionTypeDef](#splunkdestinationdescriptiontypedef)
  - [SplunkDestinationUpdateTypeDef](#splunkdestinationupdatetypedef)
  - [SplunkRetryOptionsTypeDef](#splunkretryoptionstypedef)
  - [TagTypeDef](#tagtypedef)
  - [VpcConfigurationDescriptionTypeDef](#vpcconfigurationdescriptiontypedef)
  - [VpcConfigurationTypeDef](#vpcconfigurationtypedef)

## BufferingHintsTypeDef

```python
from mypy_boto3_firehose.type_defs import BufferingHintsTypeDef
```




Optional fields:
- `SizeInMBs`: `int`
- `IntervalInSeconds`: `int`


## CloudWatchLoggingOptionsTypeDef

```python
from mypy_boto3_firehose.type_defs import CloudWatchLoggingOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `LogGroupName`: `str`
- `LogStreamName`: `str`


## CopyCommandTypeDef

```python
from mypy_boto3_firehose.type_defs import CopyCommandTypeDef
```


Required fields:
- `DataTableName`: `str`



Optional fields:
- `DataTableColumns`: `str`
- `CopyOptions`: `str`


## CreateDeliveryStreamOutputTypeDef

```python
from mypy_boto3_firehose.type_defs import CreateDeliveryStreamOutputTypeDef
```




Optional fields:
- `DeliveryStreamARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DataFormatConversionConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import DataFormatConversionConfigurationTypeDef
```




Optional fields:
- `SchemaConfiguration`: `"SchemaConfigurationTypeDef"`
- `InputFormatConfiguration`: `"InputFormatConfigurationTypeDef"`
- `OutputFormatConfiguration`: `"OutputFormatConfigurationTypeDef"`
- `Enabled`: `bool`


## DeliveryStreamDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import DeliveryStreamDescriptionTypeDef
```


Required fields:
- `DeliveryStreamName`: `str`
- `DeliveryStreamARN`: `str`
- `DeliveryStreamStatus`: `DeliveryStreamStatus`
- `DeliveryStreamType`: `DeliveryStreamType`
- `VersionId`: `str`
- `Destinations`: `List["DestinationDescriptionTypeDef"]`
- `HasMoreDestinations`: `bool`



Optional fields:
- `FailureDescription`: `"FailureDescriptionTypeDef"`
- `DeliveryStreamEncryptionConfiguration`: `"DeliveryStreamEncryptionConfigurationTypeDef"`
- `CreateTimestamp`: `datetime`
- `LastUpdateTimestamp`: `datetime`
- `Source`: `"SourceDescriptionTypeDef"`


## DeliveryStreamEncryptionConfigurationInputTypeDef

```python
from mypy_boto3_firehose.type_defs import DeliveryStreamEncryptionConfigurationInputTypeDef
```


Required fields:
- `KeyType`: `KeyType`



Optional fields:
- `KeyARN`: `str`


## DeliveryStreamEncryptionConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import DeliveryStreamEncryptionConfigurationTypeDef
```




Optional fields:
- `KeyARN`: `str`
- `KeyType`: `KeyType`
- `Status`: `DeliveryStreamEncryptionStatus`
- `FailureDescription`: `"FailureDescriptionTypeDef"`


## DescribeDeliveryStreamOutputTypeDef

```python
from mypy_boto3_firehose.type_defs import DescribeDeliveryStreamOutputTypeDef
```


Required fields:
- `DeliveryStreamDescription`: `"DeliveryStreamDescriptionTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeserializerTypeDef

```python
from mypy_boto3_firehose.type_defs import DeserializerTypeDef
```




Optional fields:
- `OpenXJsonSerDe`: `"OpenXJsonSerDeTypeDef"`
- `HiveJsonSerDe`: `"HiveJsonSerDeTypeDef"`


## DestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import DestinationDescriptionTypeDef
```


Required fields:
- `DestinationId`: `str`



Optional fields:
- `S3DestinationDescription`: `"S3DestinationDescriptionTypeDef"`
- `ExtendedS3DestinationDescription`: `"ExtendedS3DestinationDescriptionTypeDef"`
- `RedshiftDestinationDescription`: `"RedshiftDestinationDescriptionTypeDef"`
- `ElasticsearchDestinationDescription`: `"ElasticsearchDestinationDescriptionTypeDef"`
- `SplunkDestinationDescription`: `"SplunkDestinationDescriptionTypeDef"`
- `HttpEndpointDestinationDescription`: `"HttpEndpointDestinationDescriptionTypeDef"`


## ElasticsearchBufferingHintsTypeDef

```python
from mypy_boto3_firehose.type_defs import ElasticsearchBufferingHintsTypeDef
```




Optional fields:
- `IntervalInSeconds`: `int`
- `SizeInMBs`: `int`


## ElasticsearchDestinationConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import ElasticsearchDestinationConfigurationTypeDef
```


Required fields:
- `RoleARN`: `str`
- `IndexName`: `str`
- `S3Configuration`: `"S3DestinationConfigurationTypeDef"`



Optional fields:
- `DomainARN`: `str`
- `ClusterEndpoint`: `str`
- `TypeName`: `str`
- `IndexRotationPeriod`: `ElasticsearchIndexRotationPeriod`
- `BufferingHints`: `"ElasticsearchBufferingHintsTypeDef"`
- `RetryOptions`: `"ElasticsearchRetryOptionsTypeDef"`
- `S3BackupMode`: `ElasticsearchS3BackupMode`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `VpcConfiguration`: `"VpcConfigurationTypeDef"`


## ElasticsearchDestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import ElasticsearchDestinationDescriptionTypeDef
```




Optional fields:
- `RoleARN`: `str`
- `DomainARN`: `str`
- `ClusterEndpoint`: `str`
- `IndexName`: `str`
- `TypeName`: `str`
- `IndexRotationPeriod`: `ElasticsearchIndexRotationPeriod`
- `BufferingHints`: `"ElasticsearchBufferingHintsTypeDef"`
- `RetryOptions`: `"ElasticsearchRetryOptionsTypeDef"`
- `S3BackupMode`: `ElasticsearchS3BackupMode`
- `S3DestinationDescription`: `"S3DestinationDescriptionTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `VpcConfigurationDescription`: `"VpcConfigurationDescriptionTypeDef"`


## ElasticsearchDestinationUpdateTypeDef

```python
from mypy_boto3_firehose.type_defs import ElasticsearchDestinationUpdateTypeDef
```




Optional fields:
- `RoleARN`: `str`
- `DomainARN`: `str`
- `ClusterEndpoint`: `str`
- `IndexName`: `str`
- `TypeName`: `str`
- `IndexRotationPeriod`: `ElasticsearchIndexRotationPeriod`
- `BufferingHints`: `"ElasticsearchBufferingHintsTypeDef"`
- `RetryOptions`: `"ElasticsearchRetryOptionsTypeDef"`
- `S3Update`: `"S3DestinationUpdateTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## ElasticsearchRetryOptionsTypeDef

```python
from mypy_boto3_firehose.type_defs import ElasticsearchRetryOptionsTypeDef
```




Optional fields:
- `DurationInSeconds`: `int`


## EncryptionConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import EncryptionConfigurationTypeDef
```




Optional fields:
- `NoEncryptionConfig`: `Literal['NoEncryption']`
- `KMSEncryptionConfig`: `"KMSEncryptionConfigTypeDef"`


## ExtendedS3DestinationConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import ExtendedS3DestinationConfigurationTypeDef
```


Required fields:
- `RoleARN`: `str`
- `BucketARN`: `str`



Optional fields:
- `Prefix`: `str`
- `ErrorOutputPrefix`: `str`
- `BufferingHints`: `"BufferingHintsTypeDef"`
- `CompressionFormat`: `CompressionFormat`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `S3BackupMode`: `S3BackupMode`
- `S3BackupConfiguration`: `"S3DestinationConfigurationTypeDef"`
- `DataFormatConversionConfiguration`: `"DataFormatConversionConfigurationTypeDef"`


## ExtendedS3DestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import ExtendedS3DestinationDescriptionTypeDef
```


Required fields:
- `RoleARN`: `str`
- `BucketARN`: `str`
- `BufferingHints`: `"BufferingHintsTypeDef"`
- `CompressionFormat`: `CompressionFormat`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`



Optional fields:
- `Prefix`: `str`
- `ErrorOutputPrefix`: `str`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `S3BackupMode`: `S3BackupMode`
- `S3BackupDescription`: `"S3DestinationDescriptionTypeDef"`
- `DataFormatConversionConfiguration`: `"DataFormatConversionConfigurationTypeDef"`


## ExtendedS3DestinationUpdateTypeDef

```python
from mypy_boto3_firehose.type_defs import ExtendedS3DestinationUpdateTypeDef
```




Optional fields:
- `RoleARN`: `str`
- `BucketARN`: `str`
- `Prefix`: `str`
- `ErrorOutputPrefix`: `str`
- `BufferingHints`: `"BufferingHintsTypeDef"`
- `CompressionFormat`: `CompressionFormat`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `S3BackupMode`: `S3BackupMode`
- `S3BackupUpdate`: `"S3DestinationUpdateTypeDef"`
- `DataFormatConversionConfiguration`: `"DataFormatConversionConfigurationTypeDef"`


## FailureDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import FailureDescriptionTypeDef
```


Required fields:
- `Type`: `DeliveryStreamFailureType`
- `Details`: `str`




## HiveJsonSerDeTypeDef

```python
from mypy_boto3_firehose.type_defs import HiveJsonSerDeTypeDef
```




Optional fields:
- `TimestampFormats`: `List[str]`


## HttpEndpointBufferingHintsTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointBufferingHintsTypeDef
```




Optional fields:
- `SizeInMBs`: `int`
- `IntervalInSeconds`: `int`


## HttpEndpointCommonAttributeTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointCommonAttributeTypeDef
```


Required fields:
- `AttributeName`: `str`
- `AttributeValue`: `str`




## HttpEndpointConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointConfigurationTypeDef
```


Required fields:
- `Url`: `str`



Optional fields:
- `Name`: `str`
- `AccessKey`: `str`


## HttpEndpointDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointDescriptionTypeDef
```




Optional fields:
- `Url`: `str`
- `Name`: `str`


## HttpEndpointDestinationConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointDestinationConfigurationTypeDef
```


Required fields:
- `EndpointConfiguration`: `"HttpEndpointConfigurationTypeDef"`
- `S3Configuration`: `"S3DestinationConfigurationTypeDef"`



Optional fields:
- `BufferingHints`: `"HttpEndpointBufferingHintsTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `RequestConfiguration`: `"HttpEndpointRequestConfigurationTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `RoleARN`: `str`
- `RetryOptions`: `"HttpEndpointRetryOptionsTypeDef"`
- `S3BackupMode`: `HttpEndpointS3BackupMode`


## HttpEndpointDestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointDestinationDescriptionTypeDef
```




Optional fields:
- `EndpointConfiguration`: `"HttpEndpointDescriptionTypeDef"`
- `BufferingHints`: `"HttpEndpointBufferingHintsTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `RequestConfiguration`: `"HttpEndpointRequestConfigurationTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `RoleARN`: `str`
- `RetryOptions`: `"HttpEndpointRetryOptionsTypeDef"`
- `S3BackupMode`: `HttpEndpointS3BackupMode`
- `S3DestinationDescription`: `"S3DestinationDescriptionTypeDef"`


## HttpEndpointDestinationUpdateTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointDestinationUpdateTypeDef
```




Optional fields:
- `EndpointConfiguration`: `"HttpEndpointConfigurationTypeDef"`
- `BufferingHints`: `"HttpEndpointBufferingHintsTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`
- `RequestConfiguration`: `"HttpEndpointRequestConfigurationTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `RoleARN`: `str`
- `RetryOptions`: `"HttpEndpointRetryOptionsTypeDef"`
- `S3BackupMode`: `HttpEndpointS3BackupMode`
- `S3Update`: `"S3DestinationUpdateTypeDef"`


## HttpEndpointRequestConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointRequestConfigurationTypeDef
```




Optional fields:
- `ContentEncoding`: `ContentEncoding`
- `CommonAttributes`: `List["HttpEndpointCommonAttributeTypeDef"]`


## HttpEndpointRetryOptionsTypeDef

```python
from mypy_boto3_firehose.type_defs import HttpEndpointRetryOptionsTypeDef
```




Optional fields:
- `DurationInSeconds`: `int`


## InputFormatConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import InputFormatConfigurationTypeDef
```




Optional fields:
- `Deserializer`: `"DeserializerTypeDef"`


## KMSEncryptionConfigTypeDef

```python
from mypy_boto3_firehose.type_defs import KMSEncryptionConfigTypeDef
```


Required fields:
- `AWSKMSKeyARN`: `str`




## KinesisStreamSourceConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import KinesisStreamSourceConfigurationTypeDef
```


Required fields:
- `KinesisStreamARN`: `str`
- `RoleARN`: `str`




## KinesisStreamSourceDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import KinesisStreamSourceDescriptionTypeDef
```




Optional fields:
- `KinesisStreamARN`: `str`
- `RoleARN`: `str`
- `DeliveryStartTimestamp`: `datetime`


## ListDeliveryStreamsOutputTypeDef

```python
from mypy_boto3_firehose.type_defs import ListDeliveryStreamsOutputTypeDef
```


Required fields:
- `DeliveryStreamNames`: `List[str]`
- `HasMoreDeliveryStreams`: `bool`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForDeliveryStreamOutputTypeDef

```python
from mypy_boto3_firehose.type_defs import ListTagsForDeliveryStreamOutputTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`
- `HasMoreTags`: `bool`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## OpenXJsonSerDeTypeDef

```python
from mypy_boto3_firehose.type_defs import OpenXJsonSerDeTypeDef
```




Optional fields:
- `ConvertDotsInJsonKeysToUnderscores`: `bool`
- `CaseInsensitive`: `bool`
- `ColumnToJsonKeyMappings`: `Dict[str, str]`


## OrcSerDeTypeDef

```python
from mypy_boto3_firehose.type_defs import OrcSerDeTypeDef
```




Optional fields:
- `StripeSizeBytes`: `int`
- `BlockSizeBytes`: `int`
- `RowIndexStride`: `int`
- `EnablePadding`: `bool`
- `PaddingTolerance`: `float`
- `Compression`: `OrcCompression`
- `BloomFilterColumns`: `List[str]`
- `BloomFilterFalsePositiveProbability`: `float`
- `DictionaryKeyThreshold`: `float`
- `FormatVersion`: `OrcFormatVersion`


## OutputFormatConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import OutputFormatConfigurationTypeDef
```




Optional fields:
- `Serializer`: `"SerializerTypeDef"`


## ParquetSerDeTypeDef

```python
from mypy_boto3_firehose.type_defs import ParquetSerDeTypeDef
```




Optional fields:
- `BlockSizeBytes`: `int`
- `PageSizeBytes`: `int`
- `Compression`: `ParquetCompression`
- `EnableDictionaryCompression`: `bool`
- `MaxPaddingBytes`: `int`
- `WriterVersion`: `ParquetWriterVersion`


## ProcessingConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import ProcessingConfigurationTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `Processors`: `List["ProcessorTypeDef"]`


## ProcessorParameterTypeDef

```python
from mypy_boto3_firehose.type_defs import ProcessorParameterTypeDef
```


Required fields:
- `ParameterName`: `ProcessorParameterName`
- `ParameterValue`: `str`




## ProcessorTypeDef

```python
from mypy_boto3_firehose.type_defs import ProcessorTypeDef
```


Required fields:
- `Type`: `Literal['Lambda']`



Optional fields:
- `Parameters`: `List["ProcessorParameterTypeDef"]`


## PutRecordBatchOutputTypeDef

```python
from mypy_boto3_firehose.type_defs import PutRecordBatchOutputTypeDef
```


Required fields:
- `FailedPutCount`: `int`
- `RequestResponses`: `List["PutRecordBatchResponseEntryTypeDef"]`



Optional fields:
- `Encrypted`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutRecordBatchResponseEntryTypeDef

```python
from mypy_boto3_firehose.type_defs import PutRecordBatchResponseEntryTypeDef
```




Optional fields:
- `RecordId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## PutRecordOutputTypeDef

```python
from mypy_boto3_firehose.type_defs import PutRecordOutputTypeDef
```


Required fields:
- `RecordId`: `str`



Optional fields:
- `Encrypted`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## RecordTypeDef

```python
from mypy_boto3_firehose.type_defs import RecordTypeDef
```


Required fields:
- `Data`: `Union[bytes, IO[bytes]]`




## RedshiftDestinationConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import RedshiftDestinationConfigurationTypeDef
```


Required fields:
- `RoleARN`: `str`
- `ClusterJDBCURL`: `str`
- `CopyCommand`: `"CopyCommandTypeDef"`
- `Username`: `str`
- `Password`: `str`
- `S3Configuration`: `"S3DestinationConfigurationTypeDef"`



Optional fields:
- `RetryOptions`: `"RedshiftRetryOptionsTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `S3BackupMode`: `RedshiftS3BackupMode`
- `S3BackupConfiguration`: `"S3DestinationConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## RedshiftDestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import RedshiftDestinationDescriptionTypeDef
```


Required fields:
- `RoleARN`: `str`
- `ClusterJDBCURL`: `str`
- `CopyCommand`: `"CopyCommandTypeDef"`
- `Username`: `str`
- `S3DestinationDescription`: `"S3DestinationDescriptionTypeDef"`



Optional fields:
- `RetryOptions`: `"RedshiftRetryOptionsTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `S3BackupMode`: `RedshiftS3BackupMode`
- `S3BackupDescription`: `"S3DestinationDescriptionTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## RedshiftDestinationUpdateTypeDef

```python
from mypy_boto3_firehose.type_defs import RedshiftDestinationUpdateTypeDef
```




Optional fields:
- `RoleARN`: `str`
- `ClusterJDBCURL`: `str`
- `CopyCommand`: `"CopyCommandTypeDef"`
- `Username`: `str`
- `Password`: `str`
- `RetryOptions`: `"RedshiftRetryOptionsTypeDef"`
- `S3Update`: `"S3DestinationUpdateTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `S3BackupMode`: `RedshiftS3BackupMode`
- `S3BackupUpdate`: `"S3DestinationUpdateTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## RedshiftRetryOptionsTypeDef

```python
from mypy_boto3_firehose.type_defs import RedshiftRetryOptionsTypeDef
```




Optional fields:
- `DurationInSeconds`: `int`


## ResponseMetadata

```python
from mypy_boto3_firehose.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3DestinationConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import S3DestinationConfigurationTypeDef
```


Required fields:
- `RoleARN`: `str`
- `BucketARN`: `str`



Optional fields:
- `Prefix`: `str`
- `ErrorOutputPrefix`: `str`
- `BufferingHints`: `"BufferingHintsTypeDef"`
- `CompressionFormat`: `CompressionFormat`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## S3DestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import S3DestinationDescriptionTypeDef
```


Required fields:
- `RoleARN`: `str`
- `BucketARN`: `str`
- `BufferingHints`: `"BufferingHintsTypeDef"`
- `CompressionFormat`: `CompressionFormat`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`



Optional fields:
- `Prefix`: `str`
- `ErrorOutputPrefix`: `str`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## S3DestinationUpdateTypeDef

```python
from mypy_boto3_firehose.type_defs import S3DestinationUpdateTypeDef
```




Optional fields:
- `RoleARN`: `str`
- `BucketARN`: `str`
- `Prefix`: `str`
- `ErrorOutputPrefix`: `str`
- `BufferingHints`: `"BufferingHintsTypeDef"`
- `CompressionFormat`: `CompressionFormat`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## SchemaConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import SchemaConfigurationTypeDef
```




Optional fields:
- `RoleARN`: `str`
- `CatalogId`: `str`
- `DatabaseName`: `str`
- `TableName`: `str`
- `Region`: `str`
- `VersionId`: `str`


## SerializerTypeDef

```python
from mypy_boto3_firehose.type_defs import SerializerTypeDef
```




Optional fields:
- `ParquetSerDe`: `"ParquetSerDeTypeDef"`
- `OrcSerDe`: `"OrcSerDeTypeDef"`


## SourceDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import SourceDescriptionTypeDef
```




Optional fields:
- `KinesisStreamSourceDescription`: `"KinesisStreamSourceDescriptionTypeDef"`


## SplunkDestinationConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import SplunkDestinationConfigurationTypeDef
```


Required fields:
- `HECEndpoint`: `str`
- `HECEndpointType`: `HECEndpointType`
- `HECToken`: `str`
- `S3Configuration`: `"S3DestinationConfigurationTypeDef"`



Optional fields:
- `HECAcknowledgmentTimeoutInSeconds`: `int`
- `RetryOptions`: `"SplunkRetryOptionsTypeDef"`
- `S3BackupMode`: `SplunkS3BackupMode`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## SplunkDestinationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import SplunkDestinationDescriptionTypeDef
```




Optional fields:
- `HECEndpoint`: `str`
- `HECEndpointType`: `HECEndpointType`
- `HECToken`: `str`
- `HECAcknowledgmentTimeoutInSeconds`: `int`
- `RetryOptions`: `"SplunkRetryOptionsTypeDef"`
- `S3BackupMode`: `SplunkS3BackupMode`
- `S3DestinationDescription`: `"S3DestinationDescriptionTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## SplunkDestinationUpdateTypeDef

```python
from mypy_boto3_firehose.type_defs import SplunkDestinationUpdateTypeDef
```




Optional fields:
- `HECEndpoint`: `str`
- `HECEndpointType`: `HECEndpointType`
- `HECToken`: `str`
- `HECAcknowledgmentTimeoutInSeconds`: `int`
- `RetryOptions`: `"SplunkRetryOptionsTypeDef"`
- `S3BackupMode`: `SplunkS3BackupMode`
- `S3Update`: `"S3DestinationUpdateTypeDef"`
- `ProcessingConfiguration`: `"ProcessingConfigurationTypeDef"`
- `CloudWatchLoggingOptions`: `"CloudWatchLoggingOptionsTypeDef"`


## SplunkRetryOptionsTypeDef

```python
from mypy_boto3_firehose.type_defs import SplunkRetryOptionsTypeDef
```




Optional fields:
- `DurationInSeconds`: `int`


## TagTypeDef

```python
from mypy_boto3_firehose.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## VpcConfigurationDescriptionTypeDef

```python
from mypy_boto3_firehose.type_defs import VpcConfigurationDescriptionTypeDef
```


Required fields:
- `SubnetIds`: `List[str]`
- `RoleARN`: `str`
- `SecurityGroupIds`: `List[str]`
- `VpcId`: `str`




## VpcConfigurationTypeDef

```python
from mypy_boto3_firehose.type_defs import VpcConfigurationTypeDef
```


Required fields:
- `SubnetIds`: `List[str]`
- `RoleARN`: `str`
- `SecurityGroupIds`: `List[str]`



