# IoTEventsDataClient for boto3 IoTEventsData module

> [Index](../index.md) > [IoTEventsData](./index.md) > IoTEventsDataClient

Auto-generated documentation for [IoTEventsData](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData)
type annotations stubs module [mypy_boto3_iotevents_data](https://pypi.org/project/mypy-boto3-iotevents-data/).

- [IoTEventsDataClient for boto3 IoTEventsData module](#ioteventsdataclient-for-boto3-ioteventsdata-module)
  - [IoTEventsDataClient](#ioteventsdataclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_put_message](#batch_put_message)
    - [batch_update_detector](#batch_update_detector)
    - [can_paginate](#can_paginate)
    - [describe_detector](#describe_detector)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_detectors](#list_detectors)

## IoTEventsDataClient

Type annotations for `boto3.client("iotevents-data")`

Can be used directly:

```python
from mypy_boto3_iotevents_data.client import IoTEventsDataClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotevents_data.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`


## Methods


### batch_put_message

Type annotations for `boto3.client("iotevents-data").batch_put_message` method.

[Client.batch_put_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client.batch_put_message)

```python
def batch_put_message(
    self,
    messages: List[MessageTypeDef]
) -> BatchPutMessageResponseTypeDef:
    pass
```

### batch_update_detector

Type annotations for `boto3.client("iotevents-data").batch_update_detector` method.

[Client.batch_update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client.batch_update_detector)

```python
def batch_update_detector(
    self,
    detectors: List[UpdateDetectorRequestTypeDef]
) -> BatchUpdateDetectorResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("iotevents-data").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_detector

Type annotations for `boto3.client("iotevents-data").describe_detector` method.

[Client.describe_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client.describe_detector)

```python
def describe_detector(
    self,
    detectorModelName: str,
    keyValue: str = None
) -> DescribeDetectorResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotevents-data").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client.generate_presigned_url)

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

### list_detectors

Type annotations for `boto3.client("iotevents-data").list_detectors` method.

[Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client.list_detectors)

```python
def list_detectors(
    self,
    detectorModelName: str,
    stateName: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListDetectorsResponseTypeDef:
    pass
```



