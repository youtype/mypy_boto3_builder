# Type annotations for boto3 PinpointSMSVoice module

> [Index](../index.md) > PinpointSMSVoice

Auto-generated documentation for [PinpointSMSVoice](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice)
type annotations stubs module [mypy_boto3_pinpoint_sms_voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice/).

```bash
pip install mypy-boto3-pinpoint-sms-voice
```

- [Type annotations for boto3 PinpointSMSVoice module](#type-annotations-for-boto3-pinpointsmsvoice-module)
  - [PinpointSMSVoiceClient](#pinpointsmsvoiceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## PinpointSMSVoiceClient

Type annotations for  `boto3.client("pinpoint-sms-voice")` as [PinpointSMSVoiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_pinpoint_sms_voice.client import PinpointSMSVoiceClient
```


PinpointSMSVoiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_configuration_set](./client.md#create-configuration-set)
- [create_configuration_set_event_destination](./client.md#create-configuration-set-event-destination)
- [delete_configuration_set](./client.md#delete-configuration-set)
- [delete_configuration_set_event_destination](./client.md#delete-configuration-set-event-destination)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_configuration_set_event_destinations](./client.md#get-configuration-set-event-destinations)
- [send_voice_message](./client.md#send-voice-message)
- [update_configuration_set_event_destination](./client.md#update-configuration-set-event-destination)




### Exceptions
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_pinpoint_sms_voice.literals import EventType, ...
```

- [EventType](./literals.md#eventtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef, ...
```

- [CallInstructionsMessageTypeTypeDef](./type_defs.md#callinstructionsmessagetypetypedef)
- [CloudWatchLogsDestinationTypeDef](./type_defs.md#cloudwatchlogsdestinationtypedef)
- [EventDestinationDefinitionTypeDef](./type_defs.md#eventdestinationdefinitiontypedef)
- [EventDestinationTypeDef](./type_defs.md#eventdestinationtypedef)
- [GetConfigurationSetEventDestinationsResponseTypeDef](./type_defs.md#getconfigurationseteventdestinationsresponsetypedef)
- [KinesisFirehoseDestinationTypeDef](./type_defs.md#kinesisfirehosedestinationtypedef)
- [PlainTextMessageTypeTypeDef](./type_defs.md#plaintextmessagetypetypedef)
- [SSMLMessageTypeTypeDef](./type_defs.md#ssmlmessagetypetypedef)
- [SendVoiceMessageResponseTypeDef](./type_defs.md#sendvoicemessageresponsetypedef)
- [SnsDestinationTypeDef](./type_defs.md#snsdestinationtypedef)
- [VoiceMessageContentTypeDef](./type_defs.md#voicemessagecontenttypedef)
