# Literals for boto3 Firehose module

> [Index](../index.md) > [Firehose](./index.md) > Literals

Auto-generated documentation for [Firehose](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose)
type annotations stubs module [mypy_boto3_firehose](https://pypi.org/project/mypy-boto3-firehose/).

- [Literals for boto3 Firehose module](#literals-for-boto3-firehose-module)
  - [CompressionFormat](#compressionformat)
  - [ContentEncoding](#contentencoding)
  - [DeliveryStreamEncryptionStatus](#deliverystreamencryptionstatus)
  - [DeliveryStreamFailureType](#deliverystreamfailuretype)
  - [DeliveryStreamStatus](#deliverystreamstatus)
  - [DeliveryStreamType](#deliverystreamtype)
  - [ElasticsearchIndexRotationPeriod](#elasticsearchindexrotationperiod)
  - [ElasticsearchS3BackupMode](#elasticsearchs3backupmode)
  - [HECEndpointType](#hecendpointtype)
  - [HttpEndpointS3BackupMode](#httpendpoints3backupmode)
  - [KeyType](#keytype)
  - [NoEncryptionConfig](#noencryptionconfig)
  - [OrcCompression](#orccompression)
  - [OrcFormatVersion](#orcformatversion)
  - [ParquetCompression](#parquetcompression)
  - [ParquetWriterVersion](#parquetwriterversion)
  - [ProcessorParameterName](#processorparametername)
  - [ProcessorType](#processortype)
  - [RedshiftS3BackupMode](#redshifts3backupmode)
  - [S3BackupMode](#s3backupmode)
  - [SplunkS3BackupMode](#splunks3backupmode)

## CompressionFormat

```python
from mypy_boto3_firehose.literals import CompressionFormat
```

Values:

- `GZIP`
- `HADOOP_SNAPPY`
- `Snappy`
- `UNCOMPRESSED`
- `ZIP`

## ContentEncoding

```python
from mypy_boto3_firehose.literals import ContentEncoding
```

Values:

- `GZIP`
- `NONE`

## DeliveryStreamEncryptionStatus

```python
from mypy_boto3_firehose.literals import DeliveryStreamEncryptionStatus
```

Values:

- `DISABLED`
- `DISABLING`
- `DISABLING_FAILED`
- `ENABLED`
- `ENABLING`
- `ENABLING_FAILED`

## DeliveryStreamFailureType

```python
from mypy_boto3_firehose.literals import DeliveryStreamFailureType
```

Values:

- `CREATE_ENI_FAILED`
- `CREATE_KMS_GRANT_FAILED`
- `DELETE_ENI_FAILED`
- `DISABLED_KMS_KEY`
- `ENI_ACCESS_DENIED`
- `INVALID_KMS_KEY`
- `KMS_ACCESS_DENIED`
- `KMS_KEY_NOT_FOUND`
- `KMS_OPT_IN_REQUIRED`
- `RETIRE_KMS_GRANT_FAILED`
- `SECURITY_GROUP_ACCESS_DENIED`
- `SECURITY_GROUP_NOT_FOUND`
- `SUBNET_ACCESS_DENIED`
- `SUBNET_NOT_FOUND`
- `UNKNOWN_ERROR`

## DeliveryStreamStatus

```python
from mypy_boto3_firehose.literals import DeliveryStreamStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `CREATING_FAILED`
- `DELETING`
- `DELETING_FAILED`

## DeliveryStreamType

```python
from mypy_boto3_firehose.literals import DeliveryStreamType
```

Values:

- `DirectPut`
- `KinesisStreamAsSource`

## ElasticsearchIndexRotationPeriod

```python
from mypy_boto3_firehose.literals import ElasticsearchIndexRotationPeriod
```

Values:

- `NoRotation`
- `OneDay`
- `OneHour`
- `OneMonth`
- `OneWeek`

## ElasticsearchS3BackupMode

```python
from mypy_boto3_firehose.literals import ElasticsearchS3BackupMode
```

Values:

- `AllDocuments`
- `FailedDocumentsOnly`

## HECEndpointType

```python
from mypy_boto3_firehose.literals import HECEndpointType
```

Values:

- `Event`
- `Raw`

## HttpEndpointS3BackupMode

```python
from mypy_boto3_firehose.literals import HttpEndpointS3BackupMode
```

Values:

- `AllData`
- `FailedDataOnly`

## KeyType

```python
from mypy_boto3_firehose.literals import KeyType
```

Values:

- `AWS_OWNED_CMK`
- `CUSTOMER_MANAGED_CMK`

## NoEncryptionConfig

```python
from mypy_boto3_firehose.literals import NoEncryptionConfig
```

Values:

- `NoEncryption`

## OrcCompression

```python
from mypy_boto3_firehose.literals import OrcCompression
```

Values:

- `NONE`
- `SNAPPY`
- `ZLIB`

## OrcFormatVersion

```python
from mypy_boto3_firehose.literals import OrcFormatVersion
```

Values:

- `V0_11`
- `V0_12`

## ParquetCompression

```python
from mypy_boto3_firehose.literals import ParquetCompression
```

Values:

- `GZIP`
- `SNAPPY`
- `UNCOMPRESSED`

## ParquetWriterVersion

```python
from mypy_boto3_firehose.literals import ParquetWriterVersion
```

Values:

- `V1`
- `V2`

## ProcessorParameterName

```python
from mypy_boto3_firehose.literals import ProcessorParameterName
```

Values:

- `BufferIntervalInSeconds`
- `BufferSizeInMBs`
- `LambdaArn`
- `NumberOfRetries`
- `RoleArn`

## ProcessorType

```python
from mypy_boto3_firehose.literals import ProcessorType
```

Values:

- `Lambda`

## RedshiftS3BackupMode

```python
from mypy_boto3_firehose.literals import RedshiftS3BackupMode
```

Values:

- `Disabled`
- `Enabled`

## S3BackupMode

```python
from mypy_boto3_firehose.literals import S3BackupMode
```

Values:

- `Disabled`
- `Enabled`

## SplunkS3BackupMode

```python
from mypy_boto3_firehose.literals import SplunkS3BackupMode
```

Values:

- `AllEvents`
- `FailedEventsOnly`
