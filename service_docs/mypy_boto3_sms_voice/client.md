# SMSVoiceClient for boto3 SMSVoice module

> [Index](../index.md) > [SMSVoice](./index.md) > SMSVoiceClient

Auto-generated documentation for [SMSVoice](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice)
type annotations stubs module [mypy_boto3_sms_voice](https://pypi.org/project/mypy-boto3-sms-voice/).

- [SMSVoiceClient for boto3 SMSVoice module](#smsvoiceclient-for-boto3-smsvoice-module)
  - [SMSVoiceClient](#smsvoiceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_configuration_set](#create_configuration_set)
    - [create_configuration_set_event_destination](#create_configuration_set_event_destination)
    - [delete_configuration_set](#delete_configuration_set)
    - [delete_configuration_set_event_destination](#delete_configuration_set_event_destination)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_configuration_set_event_destinations](#get_configuration_set_event_destinations)
    - [list_configuration_sets](#list_configuration_sets)
    - [send_voice_message](#send_voice_message)
    - [update_configuration_set_event_destination](#update_configuration_set_event_destination)

## SMSVoiceClient

Type annotations for `boto3.client("sms-voice")`

Can be used directly:

```python
from mypy_boto3_sms_voice.client import SMSVoiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sms_voice.client import Exceptions

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

Type annotations for `boto3.client("sms-voice").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_configuration_set

Type annotations for `boto3.client("sms-voice").create_configuration_set` method.

[Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set)

```python
def create_configuration_set(
    self,
    ConfigurationSetName: str = None
) -> Dict[str, Any]:
    pass
```

### create_configuration_set_event_destination

Type annotations for `boto3.client("sms-voice").create_configuration_set_event_destination` method.

[Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set_event_destination)

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

Type annotations for `boto3.client("sms-voice").delete_configuration_set` method.

[Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set)

```python
def delete_configuration_set(
    self,
    ConfigurationSetName: str
) -> Dict[str, Any]:
    pass
```

### delete_configuration_set_event_destination

Type annotations for `boto3.client("sms-voice").delete_configuration_set_event_destination` method.

[Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set_event_destination)

```python
def delete_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sms-voice").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.generate_presigned_url)

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

Type annotations for `boto3.client("sms-voice").get_configuration_set_event_destinations` method.

[Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.get_configuration_set_event_destinations)

```python
def get_configuration_set_event_destinations(
    self,
    ConfigurationSetName: str
) -> GetConfigurationSetEventDestinationsResponseTypeDef:
    pass
```

### list_configuration_sets

Type annotations for `boto3.client("sms-voice").list_configuration_sets` method.

[Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.list_configuration_sets)

```python
def list_configuration_sets(
    self,
    NextToken: str = None,
    PageSize: str = None
) -> ListConfigurationSetsResponseTypeDef:
    pass
```

### send_voice_message

Type annotations for `boto3.client("sms-voice").send_voice_message` method.

[Client.send_voice_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.send_voice_message)

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

Type annotations for `boto3.client("sms-voice").update_configuration_set_event_destination` method.

[Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice.Client.update_configuration_set_event_destination)

```python
def update_configuration_set_event_destination(
    self,
    ConfigurationSetName: str,
    EventDestinationName: str,
    EventDestination: EventDestinationDefinitionTypeDef = None
) -> Dict[str, Any]:
    pass
```



