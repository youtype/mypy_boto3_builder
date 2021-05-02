# Literals for boto3 LexModelBuildingService module

> [Index](../index.md) > [LexModelBuildingService](./index.md) > Literals

Auto-generated documentation for [LexModelBuildingService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService)
type annotations stubs module [mypy_boto3_lex_models](https://pypi.org/project/mypy-boto3-lex-models/).

- [Literals for boto3 LexModelBuildingService module](#literals-for-boto3-lexmodelbuildingservice-module)
  - [ChannelStatus](#channelstatus)
  - [ChannelType](#channeltype)
  - [ContentType](#contenttype)
  - [Destination](#destination)
  - [ExportStatus](#exportstatus)
  - [ExportType](#exporttype)
  - [FulfillmentActivityType](#fulfillmentactivitytype)
  - [GetBotAliasesPaginatorName](#getbotaliasespaginatorname)
  - [GetBotChannelAssociationsPaginatorName](#getbotchannelassociationspaginatorname)
  - [GetBotVersionsPaginatorName](#getbotversionspaginatorname)
  - [GetBotsPaginatorName](#getbotspaginatorname)
  - [GetBuiltinIntentsPaginatorName](#getbuiltinintentspaginatorname)
  - [GetBuiltinSlotTypesPaginatorName](#getbuiltinslottypespaginatorname)
  - [GetIntentVersionsPaginatorName](#getintentversionspaginatorname)
  - [GetIntentsPaginatorName](#getintentspaginatorname)
  - [GetSlotTypeVersionsPaginatorName](#getslottypeversionspaginatorname)
  - [GetSlotTypesPaginatorName](#getslottypespaginatorname)
  - [ImportStatus](#importstatus)
  - [Locale](#locale)
  - [LogType](#logtype)
  - [MergeStrategy](#mergestrategy)
  - [ObfuscationSetting](#obfuscationsetting)
  - [ProcessBehavior](#processbehavior)
  - [ResourceType](#resourcetype)
  - [SlotConstraint](#slotconstraint)
  - [SlotValueSelectionStrategy](#slotvalueselectionstrategy)
  - [Status](#status)
  - [StatusType](#statustype)

## ChannelStatus

```python
from mypy_boto3_lex_models.literals import ChannelStatus
```

Values:

- `CREATED`
- `FAILED`
- `IN_PROGRESS`

## ChannelType

```python
from mypy_boto3_lex_models.literals import ChannelType
```

Values:

- `Facebook`
- `Kik`
- `Slack`
- `Twilio-Sms`

## ContentType

```python
from mypy_boto3_lex_models.literals import ContentType
```

Values:

- `CustomPayload`
- `PlainText`
- `SSML`

## Destination

```python
from mypy_boto3_lex_models.literals import Destination
```

Values:

- `CLOUDWATCH_LOGS`
- `S3`

## ExportStatus

```python
from mypy_boto3_lex_models.literals import ExportStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `READY`

## ExportType

```python
from mypy_boto3_lex_models.literals import ExportType
```

Values:

- `ALEXA_SKILLS_KIT`
- `LEX`

## FulfillmentActivityType

```python
from mypy_boto3_lex_models.literals import FulfillmentActivityType
```

Values:

- `CodeHook`
- `ReturnIntent`

## GetBotAliasesPaginatorName

```python
from mypy_boto3_lex_models.literals import GetBotAliasesPaginatorName
```

Values:

- `get_bot_aliases`

## GetBotChannelAssociationsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetBotChannelAssociationsPaginatorName
```

Values:

- `get_bot_channel_associations`

## GetBotVersionsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetBotVersionsPaginatorName
```

Values:

- `get_bot_versions`

## GetBotsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetBotsPaginatorName
```

Values:

- `get_bots`

## GetBuiltinIntentsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetBuiltinIntentsPaginatorName
```

Values:

- `get_builtin_intents`

## GetBuiltinSlotTypesPaginatorName

```python
from mypy_boto3_lex_models.literals import GetBuiltinSlotTypesPaginatorName
```

Values:

- `get_builtin_slot_types`

## GetIntentVersionsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetIntentVersionsPaginatorName
```

Values:

- `get_intent_versions`

## GetIntentsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetIntentsPaginatorName
```

Values:

- `get_intents`

## GetSlotTypeVersionsPaginatorName

```python
from mypy_boto3_lex_models.literals import GetSlotTypeVersionsPaginatorName
```

Values:

- `get_slot_type_versions`

## GetSlotTypesPaginatorName

```python
from mypy_boto3_lex_models.literals import GetSlotTypesPaginatorName
```

Values:

- `get_slot_types`

## ImportStatus

```python
from mypy_boto3_lex_models.literals import ImportStatus
```

Values:

- `COMPLETE`
- `FAILED`
- `IN_PROGRESS`

## Locale

```python
from mypy_boto3_lex_models.literals import Locale
```

Values:

- `de-DE`
- `en-AU`
- `en-GB`
- `en-US`
- `es-419`
- `es-ES`
- `es-US`
- `fr-CA`
- `fr-FR`
- `it-IT`
- `ja-JP`

## LogType

```python
from mypy_boto3_lex_models.literals import LogType
```

Values:

- `AUDIO`
- `TEXT`

## MergeStrategy

```python
from mypy_boto3_lex_models.literals import MergeStrategy
```

Values:

- `FAIL_ON_CONFLICT`
- `OVERWRITE_LATEST`

## ObfuscationSetting

```python
from mypy_boto3_lex_models.literals import ObfuscationSetting
```

Values:

- `DEFAULT_OBFUSCATION`
- `NONE`

## ProcessBehavior

```python
from mypy_boto3_lex_models.literals import ProcessBehavior
```

Values:

- `BUILD`
- `SAVE`

## ResourceType

```python
from mypy_boto3_lex_models.literals import ResourceType
```

Values:

- `BOT`
- `INTENT`
- `SLOT_TYPE`

## SlotConstraint

```python
from mypy_boto3_lex_models.literals import SlotConstraint
```

Values:

- `Optional`
- `Required`

## SlotValueSelectionStrategy

```python
from mypy_boto3_lex_models.literals import SlotValueSelectionStrategy
```

Values:

- `ORIGINAL_VALUE`
- `TOP_RESOLUTION`

## Status

```python
from mypy_boto3_lex_models.literals import Status
```

Values:

- `BUILDING`
- `FAILED`
- `NOT_BUILT`
- `READY`
- `READY_BASIC_TESTING`

## StatusType

```python
from mypy_boto3_lex_models.literals import StatusType
```

Values:

- `Detected`
- `Missed`
