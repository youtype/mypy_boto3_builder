# Structures for boto3 SMSVoice module

> [Index](../index.md) > [SMSVoice](./index.md) > Structures

Auto-generated documentation for [SMSVoice](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html#SMSVoice)
type annotations stubs module [mypy_boto3_sms_voice](https://pypi.org/project/mypy-boto3-sms-voice/).

- [Structures for boto3 SMSVoice module](#structures-for-boto3-smsvoice-module)
  - [CallInstructionsMessageTypeTypeDef](#callinstructionsmessagetypetypedef)
  - [CloudWatchLogsDestinationTypeDef](#cloudwatchlogsdestinationtypedef)
  - [EventDestinationTypeDef](#eventdestinationtypedef)
  - [KinesisFirehoseDestinationTypeDef](#kinesisfirehosedestinationtypedef)
  - [PlainTextMessageTypeTypeDef](#plaintextmessagetypetypedef)
  - [SSMLMessageTypeTypeDef](#ssmlmessagetypetypedef)
  - [SnsDestinationTypeDef](#snsdestinationtypedef)
  - [EventDestinationDefinitionTypeDef](#eventdestinationdefinitiontypedef)
  - [GetConfigurationSetEventDestinationsResponseTypeDef](#getconfigurationseteventdestinationsresponsetypedef)
  - [ListConfigurationSetsResponseTypeDef](#listconfigurationsetsresponsetypedef)
  - [SendVoiceMessageResponseTypeDef](#sendvoicemessageresponsetypedef)
  - [VoiceMessageContentTypeDef](#voicemessagecontenttypedef)

## CallInstructionsMessageTypeTypeDef

```python
from mypy_boto3_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef
```




Optional fields:
- `Text`: `str`


## CloudWatchLogsDestinationTypeDef

```python
from mypy_boto3_sms_voice.type_defs import CloudWatchLogsDestinationTypeDef
```




Optional fields:
- `IamRoleArn`: `str`
- `LogGroupArn`: `str`


## EventDestinationTypeDef

```python
from mypy_boto3_sms_voice.type_defs import EventDestinationTypeDef
```




Optional fields:
- `CloudWatchLogsDestination`: `"CloudWatchLogsDestinationTypeDef"`
- `Enabled`: `bool`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `MatchingEventTypes`: `List[EventType]`
- `Name`: `str`
- `SnsDestination`: `"SnsDestinationTypeDef"`


## KinesisFirehoseDestinationTypeDef

```python
from mypy_boto3_sms_voice.type_defs import KinesisFirehoseDestinationTypeDef
```




Optional fields:
- `DeliveryStreamArn`: `str`
- `IamRoleArn`: `str`


## PlainTextMessageTypeTypeDef

```python
from mypy_boto3_sms_voice.type_defs import PlainTextMessageTypeTypeDef
```




Optional fields:
- `LanguageCode`: `str`
- `Text`: `str`
- `VoiceId`: `str`


## SSMLMessageTypeTypeDef

```python
from mypy_boto3_sms_voice.type_defs import SSMLMessageTypeTypeDef
```




Optional fields:
- `LanguageCode`: `str`
- `Text`: `str`
- `VoiceId`: `str`


## SnsDestinationTypeDef

```python
from mypy_boto3_sms_voice.type_defs import SnsDestinationTypeDef
```




Optional fields:
- `TopicArn`: `str`


## EventDestinationDefinitionTypeDef

```python
from mypy_boto3_sms_voice.type_defs import EventDestinationDefinitionTypeDef
```




Optional fields:
- `CloudWatchLogsDestination`: `"CloudWatchLogsDestinationTypeDef"`
- `Enabled`: `bool`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `MatchingEventTypes`: `List[EventType]`
- `SnsDestination`: `"SnsDestinationTypeDef"`


## GetConfigurationSetEventDestinationsResponseTypeDef

```python
from mypy_boto3_sms_voice.type_defs import GetConfigurationSetEventDestinationsResponseTypeDef
```




Optional fields:
- `EventDestinations`: `List["EventDestinationTypeDef"]`


## ListConfigurationSetsResponseTypeDef

```python
from mypy_boto3_sms_voice.type_defs import ListConfigurationSetsResponseTypeDef
```




Optional fields:
- `ConfigurationSets`: `List[str]`
- `NextToken`: `str`


## SendVoiceMessageResponseTypeDef

```python
from mypy_boto3_sms_voice.type_defs import SendVoiceMessageResponseTypeDef
```




Optional fields:
- `MessageId`: `str`


## VoiceMessageContentTypeDef

```python
from mypy_boto3_sms_voice.type_defs import VoiceMessageContentTypeDef
```




Optional fields:
- `CallInstructionsMessage`: `"CallInstructionsMessageTypeTypeDef"`
- `PlainTextMessage`: `"PlainTextMessageTypeTypeDef"`
- `SSMLMessage`: `"SSMLMessageTypeTypeDef"`

