# Structures for boto3 PinpointSMSVoice module

> [Index](../index.md) > [PinpointSMSVoice](./index.md) > Structures

Auto-generated documentation for [PinpointSMSVoice](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html#PinpointSMSVoice)
type annotations stubs module [mypy_boto3_pinpoint_sms_voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice/).

- [Structures for boto3 PinpointSMSVoice module](#structures-for-boto3-pinpointsmsvoice-module)
  - [CallInstructionsMessageTypeTypeDef](#callinstructionsmessagetypetypedef)
  - [CloudWatchLogsDestinationTypeDef](#cloudwatchlogsdestinationtypedef)
  - [EventDestinationDefinitionTypeDef](#eventdestinationdefinitiontypedef)
  - [EventDestinationTypeDef](#eventdestinationtypedef)
  - [GetConfigurationSetEventDestinationsResponseTypeDef](#getconfigurationseteventdestinationsresponsetypedef)
  - [KinesisFirehoseDestinationTypeDef](#kinesisfirehosedestinationtypedef)
  - [PlainTextMessageTypeTypeDef](#plaintextmessagetypetypedef)
  - [SSMLMessageTypeTypeDef](#ssmlmessagetypetypedef)
  - [SendVoiceMessageResponseTypeDef](#sendvoicemessageresponsetypedef)
  - [SnsDestinationTypeDef](#snsdestinationtypedef)
  - [VoiceMessageContentTypeDef](#voicemessagecontenttypedef)

## CallInstructionsMessageTypeTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef
```




Optional fields:
- `Text`: `str`


## CloudWatchLogsDestinationTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import CloudWatchLogsDestinationTypeDef
```




Optional fields:
- `IamRoleArn`: `str`
- `LogGroupArn`: `str`


## EventDestinationDefinitionTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import EventDestinationDefinitionTypeDef
```




Optional fields:
- `CloudWatchLogsDestination`: `"CloudWatchLogsDestinationTypeDef"`
- `Enabled`: `bool`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `MatchingEventTypes`: `List[EventType]`
- `SnsDestination`: `"SnsDestinationTypeDef"`


## EventDestinationTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import EventDestinationTypeDef
```




Optional fields:
- `CloudWatchLogsDestination`: `"CloudWatchLogsDestinationTypeDef"`
- `Enabled`: `bool`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `MatchingEventTypes`: `List[EventType]`
- `Name`: `str`
- `SnsDestination`: `"SnsDestinationTypeDef"`


## GetConfigurationSetEventDestinationsResponseTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import GetConfigurationSetEventDestinationsResponseTypeDef
```




Optional fields:
- `EventDestinations`: `List["EventDestinationTypeDef"]`


## KinesisFirehoseDestinationTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import KinesisFirehoseDestinationTypeDef
```




Optional fields:
- `DeliveryStreamArn`: `str`
- `IamRoleArn`: `str`


## PlainTextMessageTypeTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import PlainTextMessageTypeTypeDef
```




Optional fields:
- `LanguageCode`: `str`
- `Text`: `str`
- `VoiceId`: `str`


## SSMLMessageTypeTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import SSMLMessageTypeTypeDef
```




Optional fields:
- `LanguageCode`: `str`
- `Text`: `str`
- `VoiceId`: `str`


## SendVoiceMessageResponseTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import SendVoiceMessageResponseTypeDef
```




Optional fields:
- `MessageId`: `str`


## SnsDestinationTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import SnsDestinationTypeDef
```




Optional fields:
- `TopicArn`: `str`


## VoiceMessageContentTypeDef

```python
from mypy_boto3_pinpoint_sms_voice.type_defs import VoiceMessageContentTypeDef
```




Optional fields:
- `CallInstructionsMessage`: `"CallInstructionsMessageTypeTypeDef"`
- `PlainTextMessage`: `"PlainTextMessageTypeTypeDef"`
- `SSMLMessage`: `"SSMLMessageTypeTypeDef"`

