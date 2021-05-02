# PinpointSMSVoiceClient for boto3 PinpointSMSVoice module

> [Index](../index.md) > [PinpointSMSVoice](./index.md) > PinpointSMSVoiceClient

Auto-generated documentation for [PinpointSMSVoice](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice)
type annotations stubs module [mypy_boto3_pinpoint_sms_voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice/).

- [PinpointSMSVoiceClient for boto3 PinpointSMSVoice module](#pinpointsmsvoiceclient-for-boto3-pinpointsmsvoice-module)
  - [PinpointSMSVoiceClient](#pinpointsmsvoiceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_configuration_set](#create_configuration_set)
    - [create_configuration_set_event_destination](#create_configuration_set_event_destination)
    - [delete_configuration_set](#delete_configuration_set)
    - [delete_configuration_set_event_destination](#delete_configuration_set_event_destination)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_configuration_set_event_destinations](#get_configuration_set_event_destinations)
    - [send_voice_message](#send_voice_message)
    - [update_configuration_set_event_destination](#update_configuration_set_event_destination)

## PinpointSMSVoiceClient

Type annotations for `boto3.client("pinpoint-sms-voice")`

Can be used directly:

```python
from mypy_boto3_pinpoint_sms_voice.client import PinpointSMSVoiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_pinpoint_sms_voice.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("pinpoint-sms-voice").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_configuration_set

Type annotations for `boto3.client("pinpoint-sms-voice").create_configuration_set` method.

[Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.create_configuration_set)

```python
def create_configuration_set(
    self,
    ConfigurationSetName: str = None
) -> Dict[str, Any]:
    pass
```

### create_configuration_set_event_destination

Type annotations for `boto3.client("pinpoint-sms-voice").create_configuration_set_event_destination` method.

[Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.create_configuration_set_event_destination)

```python
def create_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestination: EventDestinationDefinitionTypeDef = None,
    EventDestinationName: str = None
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set

Type annotations for `boto3.client("pinpoint-sms-voice").delete_configuration_set` method.

[Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.delete_configuration_set)

```python
def delete_configuration_set(
    self,
    ConfigurationSetName: str
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set_event_destination

Type annotations for `boto3.client("pinpoint-sms-voice").delete_configuration_set_event_destination` method.

[Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.delete_configuration_set_event_destination)

```python
def delete_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("pinpoint-sms-voice").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.generate_presigned_url)

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

### get_configuration_set_event_destinations

Type annotations for `boto3.client("pinpoint-sms-voice").get_configuration_set_event_destinations` method.

[Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.get_configuration_set_event_destinations)

```python
def get_configuration_set_event_destinations(
    self,
    ConfigurationSetName: str
) -> GetConfigurationSetEventDestinationsResponseTypeDef:
    pass
```

### send_voice_message

Type annotations for `boto3.client("pinpoint-sms-voice").send_voice_message` method.

[Client.send_voice_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.send_voice_message)

```python
def send_voice_message(
    self,
    CallerId: str = None,
    ConfigurationSetName: str = None,
    Content: VoiceMessageContentTypeDef = None,
    DestinationPhoneNumber: str = None,
    OriginationPhoneNumber: str = None
) -> SendVoiceMessageResponseTypeDef:
    pass
```

### update_configuration_set_event_destination

Type annotations for `boto3.client("pinpoint-sms-voice").update_configuration_set_event_destination` method.

[Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice.Client.update_configuration_set_event_destination)

```python
def update_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: EventDestinationDefinitionTypeDef = None
) -> Dict[str, Any]:
    pass
```



