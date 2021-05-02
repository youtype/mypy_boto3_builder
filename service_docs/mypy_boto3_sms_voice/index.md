# Type annotations for boto3 SMSVoice module

> [Index](../index.md) > SMSVoice

Auto-generated documentation for [SMSVoice](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice)
type annotations stubs module [mypy_boto3_sms_voice](https://pypi.org/project/mypy-boto3-sms-voice/).

```bash
pip install mypy-boto3-sms-voice
```

- [Type annotations for boto3 SMSVoice module](#type-annotations-for-boto3-smsvoice-module)
  - [SMSVoiceClient](#smsvoiceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## SMSVoiceClient

Type annotations for  `boto3.client("sms-voice")` as [SMSVoiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sms_voice.client import SMSVoiceClient
```


SMSVoiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_configuration_set](./client.md#create-configuration-set)
- [create_configuration_set_event_destination](./client.md#create-configuration-set-event-destination)
- [delete_configuration_set](./client.md#delete-configuration-set)
- [delete_configuration_set_event_destination](./client.md#delete-configuration-set-event-destination)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_configuration_set_event_destinations](./client.md#get-configuration-set-event-destinations)
- [list_configuration_sets](./client.md#list-configuration-sets)
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
from mypy_boto3_sms_voice.literals import EventType, ...
```

- [EventType](./literals.md#eventtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef, ...
```

- [CallInstructionsMessageTypeTypeDef](./type_defs.md#callinstructionsmessagetypetypedef)
- [CloudWatchLogsDestinationTypeDef](./type_defs.md#cloudwatchlogsdestinationtypedef)
- [EventDestinationTypeDef](./type_defs.md#eventdestinationtypedef)
- [KinesisFirehoseDestinationTypeDef](./type_defs.md#kinesisfirehosedestinationtypedef)
- [PlainTextMessageTypeTypeDef](./type_defs.md#plaintextmessagetypetypedef)
- [SSMLMessageTypeTypeDef](./type_defs.md#ssmlmessagetypetypedef)
- [SnsDestinationTypeDef](./type_defs.md#snsdestinationtypedef)
- [EventDestinationDefinitionTypeDef](./type_defs.md#eventdestinationdefinitiontypedef)
- [GetConfigurationSetEventDestinationsResponseTypeDef](./type_defs.md#getconfigurationseteventdestinationsresponsetypedef)
- [ListConfigurationSetsResponseTypeDef](./type_defs.md#listconfigurationsetsresponsetypedef)
- [SendVoiceMessageResponseTypeDef](./type_defs.md#sendvoicemessageresponsetypedef)
- [VoiceMessageContentTypeDef](./type_defs.md#voicemessagecontenttypedef)
