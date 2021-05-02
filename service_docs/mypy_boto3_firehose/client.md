# FirehoseClient for boto3 Firehose module

> [Index](../index.md) > [Firehose](./index.md) > FirehoseClient

Auto-generated documentation for [Firehose](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose)
type annotations stubs module [mypy_boto3_firehose](https://pypi.org/project/mypy-boto3-firehose/).

- [FirehoseClient for boto3 Firehose module](#firehoseclient-for-boto3-firehose-module)
  - [FirehoseClient](#firehoseclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_delivery_stream](#create_delivery_stream)
    - [delete_delivery_stream](#delete_delivery_stream)
    - [describe_delivery_stream](#describe_delivery_stream)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_delivery_streams](#list_delivery_streams)
    - [list_tags_for_delivery_stream](#list_tags_for_delivery_stream)
    - [put_record](#put_record)
    - [put_record_batch](#put_record_batch)
    - [start_delivery_stream_encryption](#start_delivery_stream_encryption)
    - [stop_delivery_stream_encryption](#stop_delivery_stream_encryption)
    - [tag_delivery_stream](#tag_delivery_stream)
    - [untag_delivery_stream](#untag_delivery_stream)
    - [update_destination](#update_destination)

## FirehoseClient

Type annotations for `boto3.client("firehose")`

Can be used directly:

```python
from mypy_boto3_firehose.client import FirehoseClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_firehose.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidKMSResourceException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`


## Methods


### can_paginate

Type annotations for `boto3.client("firehose").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_delivery_stream

Type annotations for `boto3.client("firehose").create_delivery_stream` method.

[Client.create_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.create_delivery_stream)

```python
def create_delivery_stream(
    self,
    DeliveryStreamName: str,
    DeliveryStreamType: DeliveryStreamType = None,
    KinesisStreamSourceConfiguration: KinesisStreamSourceConfigurationTypeDef = None,
    DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
    S3DestinationConfiguration: "S3DestinationConfigurationTypeDef" = None,
    ExtendedS3DestinationConfiguration: ExtendedS3DestinationConfigurationTypeDef = None,
    RedshiftDestinationConfiguration: RedshiftDestinationConfigurationTypeDef = None,
    ElasticsearchDestinationConfiguration: ElasticsearchDestinationConfigurationTypeDef = None,
    SplunkDestinationConfiguration: SplunkDestinationConfigurationTypeDef = None,
    HttpEndpointDestinationConfiguration: HttpEndpointDestinationConfigurationTypeDef = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDeliveryStreamOutputTypeDef:
    pass
```

### delete_delivery_stream

Type annotations for `boto3.client("firehose").delete_delivery_stream` method.

[Client.delete_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.delete_delivery_stream)

```python
def delete_delivery_stream(
    self,
    DeliveryStreamName: str,
    AllowForceDelete: bool = None
) -> Dict[str, Any]:
    pass
```

### describe_delivery_stream

Type annotations for `boto3.client("firehose").describe_delivery_stream` method.

[Client.describe_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.describe_delivery_stream)

```python
def describe_delivery_stream(
    self,
    DeliveryStreamName: str,
    Limit: int = None,
    ExclusiveStartDestinationId: str = None
) -> DescribeDeliveryStreamOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("firehose").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.generate_presigned_url)

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

### list_delivery_streams

Type annotations for `boto3.client("firehose").list_delivery_streams` method.

[Client.list_delivery_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.list_delivery_streams)

```python
def list_delivery_streams(
    self,
    Limit: int = None,
    DeliveryStreamType: DeliveryStreamType = None,
    ExclusiveStartDeliveryStreamName: str = None
) -> ListDeliveryStreamsOutputTypeDef:
    pass
```

### list_tags_for_delivery_stream

Type annotations for `boto3.client("firehose").list_tags_for_delivery_stream` method.

[Client.list_tags_for_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.list_tags_for_delivery_stream)

```python
def list_tags_for_delivery_stream(
    self,
    DeliveryStreamName: str,
    ExclusiveStartTagKey: str = None,
    Limit: int = None
) -> ListTagsForDeliveryStreamOutputTypeDef:
    pass
```

### put_record

Type annotations for `boto3.client("firehose").put_record` method.

[Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.put_record)

```python
def put_record(
    self,
    DeliveryStreamName: str,
    Record: RecordTypeDef
) -> PutRecordOutputTypeDef:
    pass
```

### put_record_batch

Type annotations for `boto3.client("firehose").put_record_batch` method.

[Client.put_record_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.put_record_batch)

```python
def put_record_batch(
    self,
    DeliveryStreamName: str,
    Records: List[RecordTypeDef]
) -> PutRecordBatchOutputTypeDef:
    pass
```

### start_delivery_stream_encryption

Type annotations for `boto3.client("firehose").start_delivery_stream_encryption` method.

[Client.start_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.start_delivery_stream_encryption)

```python
def start_delivery_stream_encryption(
    self,
    DeliveryStreamName: str,
    DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None
) -> Dict[str, Any]:
    pass
```

### stop_delivery_stream_encryption

Type annotations for `boto3.client("firehose").stop_delivery_stream_encryption` method.

[Client.stop_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.stop_delivery_stream_encryption)

```python
def stop_delivery_stream_encryption(
    self,
    DeliveryStreamName: str
) -> Dict[str, Any]:
    pass
```

### tag_delivery_stream

Type annotations for `boto3.client("firehose").tag_delivery_stream` method.

[Client.tag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.tag_delivery_stream)

```python
def tag_delivery_stream(
    self,
    DeliveryStreamName: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_delivery_stream

Type annotations for `boto3.client("firehose").untag_delivery_stream` method.

[Client.untag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.untag_delivery_stream)

```python
def untag_delivery_stream(
    self,
    DeliveryStreamName: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_destination

Type annotations for `boto3.client("firehose").update_destination` method.

[Client.update_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html#Firehose.Client.update_destination)

```python
def update_destination(
    self,
    DeliveryStreamName: str,
    CurrentDeliveryStreamVersionId: str,
    DestinationId: str,
    S3DestinationUpdate: "S3DestinationUpdateTypeDef" = None,
    ExtendedS3DestinationUpdate: ExtendedS3DestinationUpdateTypeDef = None,
    RedshiftDestinationUpdate: RedshiftDestinationUpdateTypeDef = None,
    ElasticsearchDestinationUpdate: ElasticsearchDestinationUpdateTypeDef = None,
    SplunkDestinationUpdate: SplunkDestinationUpdateTypeDef = None,
    HttpEndpointDestinationUpdate: HttpEndpointDestinationUpdateTypeDef = None
) -> Dict[str, Any]:
    pass
```