# LexModelsV2Client for boto3 LexModelsV2 module

> [Index](../index.md) > [LexModelsV2](./index.md) > LexModelsV2Client

Auto-generated documentation for [LexModelsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2)
type annotations stubs module [mypy_boto3_lexv2_models](https://pypi.org/project/mypy-boto3-lexv2-models/).

- [LexModelsV2Client for boto3 LexModelsV2 module](#lexmodelsv2client-for-boto3-lexmodelsv2-module)
  - [LexModelsV2Client](#lexmodelsv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [build_bot_locale](#build_bot_locale)
    - [can_paginate](#can_paginate)
    - [create_bot](#create_bot)
    - [create_bot_alias](#create_bot_alias)
    - [create_bot_locale](#create_bot_locale)
    - [create_bot_version](#create_bot_version)
    - [create_intent](#create_intent)
    - [create_slot](#create_slot)
    - [create_slot_type](#create_slot_type)
    - [delete_bot](#delete_bot)
    - [delete_bot_alias](#delete_bot_alias)
    - [delete_bot_locale](#delete_bot_locale)
    - [delete_bot_version](#delete_bot_version)
    - [delete_intent](#delete_intent)
    - [delete_slot](#delete_slot)
    - [delete_slot_type](#delete_slot_type)
    - [describe_bot](#describe_bot)
    - [describe_bot_alias](#describe_bot_alias)
    - [describe_bot_locale](#describe_bot_locale)
    - [describe_bot_version](#describe_bot_version)
    - [describe_intent](#describe_intent)
    - [describe_slot](#describe_slot)
    - [describe_slot_type](#describe_slot_type)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_bot_aliases](#list_bot_aliases)
    - [list_bot_locales](#list_bot_locales)
    - [list_bot_versions](#list_bot_versions)
    - [list_bots](#list_bots)
    - [list_built_in_intents](#list_built_in_intents)
    - [list_built_in_slot_types](#list_built_in_slot_types)
    - [list_intents](#list_intents)
    - [list_slot_types](#list_slot_types)
    - [list_slots](#list_slots)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_bot](#update_bot)
    - [update_bot_alias](#update_bot_alias)
    - [update_bot_locale](#update_bot_locale)
    - [update_intent](#update_intent)
    - [update_slot](#update_slot)
    - [update_slot_type](#update_slot_type)

## LexModelsV2Client

Type annotations for `boto3.client("lexv2-models")`

Can be used directly:

```python
from mypy_boto3_lexv2_models.client import LexModelsV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lexv2_models.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.PreconditionFailedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### build_bot_locale

Type annotations for `boto3.client("lexv2-models").build_bot_locale` method.

[Client.build_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)

```python
def build_bot_locale(
    self,
    botId: str,
    botVersion: str,
    localeId: str
) -> BuildBotLocaleResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("lexv2-models").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_bot

Type annotations for `boto3.client("lexv2-models").create_bot` method.

[Client.create_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)

```python
def create_bot(
    self,
    botName: str,
    roleArn: str,
    dataPrivacy: "DataPrivacyTypeDef",
    idleSessionTTLInSeconds: int,
    description: str = None,
    botTags: Dict[str, str] = None,
    testBotAliasTags: Dict[str, str] = None
) -> CreateBotResponseTypeDef:
    pass
```

### create_bot_alias

Type annotations for `boto3.client("lexv2-models").create_bot_alias` method.

[Client.create_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)

```python
def create_bot_alias(
    self,
    botAliasName: str,
    botId: str,
    description: str = None,
    botVersion: str = None,
    botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
    conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
    sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateBotAliasResponseTypeDef:
    pass
```

### create_bot_locale

Type annotations for `boto3.client("lexv2-models").create_bot_locale` method.

[Client.create_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)

```python
def create_bot_locale(
    self,
    botId: str,
    botVersion: str,
    localeId: str,
    nluIntentConfidenceThreshold: float,
    description: str = None,
    voiceSettings: "VoiceSettingsTypeDef" = None
) -> CreateBotLocaleResponseTypeDef:
    pass
```

### create_bot_version

Type annotations for `boto3.client("lexv2-models").create_bot_version` method.

[Client.create_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)

```python
def create_bot_version(
    self,
    botId: str,
    botVersionLocaleSpecification: Dict[str, "BotVersionLocaleDetailsTypeDef"],
    description: str = None
) -> CreateBotVersionResponseTypeDef:
    pass
```

### create_intent

Type annotations for `boto3.client("lexv2-models").create_intent` method.

[Client.create_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)

```python
def create_intent(
    self,
    intentName: str,
    botId: str,
    botVersion: str,
    localeId: str,
    description: str = None,
    parentIntentSignature: str = None,
    sampleUtterances: List["SampleUtteranceTypeDef"] = None,
    dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
    fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
    intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
    intentClosingSetting: "IntentClosingSettingTypeDef" = None,
    inputContexts: List["InputContextTypeDef"] = None,
    outputContexts: List["OutputContextTypeDef"] = None,
    kendraConfiguration: "KendraConfigurationTypeDef" = None
) -> CreateIntentResponseTypeDef:
    pass
```

### create_slot

Type annotations for `boto3.client("lexv2-models").create_slot` method.

[Client.create_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)

```python
def create_slot(
    self,
    slotName: str,
    slotTypeId: str,
    valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
    botId: str,
    botVersion: str,
    localeId: str,
    intentId: str,
    description: str = None,
    obfuscationSetting: "ObfuscationSettingTypeDef" = None
) -> CreateSlotResponseTypeDef:
    pass
```

### create_slot_type

Type annotations for `boto3.client("lexv2-models").create_slot_type` method.

[Client.create_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)

```python
def create_slot_type(
    self,
    slotTypeName: str,
    valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
    botId: str,
    botVersion: str,
    localeId: str,
    description: str = None,
    slotTypeValues: List["SlotTypeValueTypeDef"] = None,
    parentSlotTypeSignature: str = None
) -> CreateSlotTypeResponseTypeDef:
    pass
```

### delete_bot

Type annotations for `boto3.client("lexv2-models").delete_bot` method.

[Client.delete_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)

```python
def delete_bot(
    self,
    botId: str,
    skipResourceInUseCheck: bool = None
) -> DeleteBotResponseTypeDef:
    pass
```

### delete_bot_alias

Type annotations for `boto3.client("lexv2-models").delete_bot_alias` method.

[Client.delete_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)

```python
def delete_bot_alias(
    self,
    botAliasId: str,
    botId: str,
    skipResourceInUseCheck: bool = None
) -> DeleteBotAliasResponseTypeDef:
    pass
```

### delete_bot_locale

Type annotations for `boto3.client("lexv2-models").delete_bot_locale` method.

[Client.delete_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)

```python
def delete_bot_locale(
    self,
    botId: str,
    botVersion: str,
    localeId: str
) -> DeleteBotLocaleResponseTypeDef:
    pass
```

### delete_bot_version

Type annotations for `boto3.client("lexv2-models").delete_bot_version` method.

[Client.delete_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)

```python
def delete_bot_version(
    self,
    botId: str,
    botVersion: str,
    skipResourceInUseCheck: bool = None
) -> DeleteBotVersionResponseTypeDef:
    pass
```

### delete_intent

Type annotations for `boto3.client("lexv2-models").delete_intent` method.

[Client.delete_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)

```python
def delete_intent(
    self,
    intentId: str,
    botId: str,
    botVersion: str,
    localeId: str
) -> None:
    pass
```

### delete_slot

Type annotations for `boto3.client("lexv2-models").delete_slot` method.

[Client.delete_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)

```python
def delete_slot(
    self,
    slotId: str,
    botId: str,
    botVersion: str,
    localeId: str,
    intentId: str
) -> None:
    pass
```

### delete_slot_type

Type annotations for `boto3.client("lexv2-models").delete_slot_type` method.

[Client.delete_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)

```python
def delete_slot_type(
    self,
    slotTypeId: str,
    botId: str,
    botVersion: str,
    localeId: str,
    skipResourceInUseCheck: bool = None
) -> None:
    pass
```

### describe_bot

Type annotations for `boto3.client("lexv2-models").describe_bot` method.

[Client.describe_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)

```python
def describe_bot(
    self,
    botId: str
) -> DescribeBotResponseTypeDef:
    pass
```

### describe_bot_alias

Type annotations for `boto3.client("lexv2-models").describe_bot_alias` method.

[Client.describe_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)

```python
def describe_bot_alias(
    self,
    botAliasId: str,
    botId: str
) -> DescribeBotAliasResponseTypeDef:
    pass
```

### describe_bot_locale

Type annotations for `boto3.client("lexv2-models").describe_bot_locale` method.

[Client.describe_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)

```python
def describe_bot_locale(
    self,
    botId: str,
    botVersion: str,
    localeId: str
) -> DescribeBotLocaleResponseTypeDef:
    pass
```

### describe_bot_version

Type annotations for `boto3.client("lexv2-models").describe_bot_version` method.

[Client.describe_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)

```python
def describe_bot_version(
    self,
    botId: str,
    botVersion: str
) -> DescribeBotVersionResponseTypeDef:
    pass
```

### describe_intent

Type annotations for `boto3.client("lexv2-models").describe_intent` method.

[Client.describe_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)

```python
def describe_intent(
    self,
    intentId: str,
    botId: str,
    botVersion: str,
    localeId: str
) -> DescribeIntentResponseTypeDef:
    pass
```

### describe_slot

Type annotations for `boto3.client("lexv2-models").describe_slot` method.

[Client.describe_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)

```python
def describe_slot(
    self,
    slotId: str,
    botId: str,
    botVersion: str,
    localeId: str,
    intentId: str
) -> DescribeSlotResponseTypeDef:
    pass
```

### describe_slot_type

Type annotations for `boto3.client("lexv2-models").describe_slot_type` method.

[Client.describe_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)

```python
def describe_slot_type(
    self,
    slotTypeId: str,
    botId: str,
    botVersion: str,
    localeId: str
) -> DescribeSlotTypeResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lexv2-models").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)

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

### list_bot_aliases

Type annotations for `boto3.client("lexv2-models").list_bot_aliases` method.

[Client.list_bot_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)

```python
def list_bot_aliases(
    self,
    botId: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListBotAliasesResponseTypeDef:
    pass
```

### list_bot_locales

Type annotations for `boto3.client("lexv2-models").list_bot_locales` method.

[Client.list_bot_locales documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)

```python
def list_bot_locales(
    self,
    botId: str,
    botVersion: str,
    sortBy: BotLocaleSortByTypeDef = None,
    filters: List[BotLocaleFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListBotLocalesResponseTypeDef:
    pass
```

### list_bot_versions

Type annotations for `boto3.client("lexv2-models").list_bot_versions` method.

[Client.list_bot_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)

```python
def list_bot_versions(
    self,
    botId: str,
    sortBy: BotVersionSortByTypeDef = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListBotVersionsResponseTypeDef:
    pass
```

### list_bots

Type annotations for `boto3.client("lexv2-models").list_bots` method.

[Client.list_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)

```python
def list_bots(
    self,
    sortBy: BotSortByTypeDef = None,
    filters: List[BotFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListBotsResponseTypeDef:
    pass
```

### list_built_in_intents

Type annotations for `boto3.client("lexv2-models").list_built_in_intents` method.

[Client.list_built_in_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)

```python
def list_built_in_intents(
    self,
    localeId: str,
    sortBy: BuiltInIntentSortByTypeDef = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListBuiltInIntentsResponseTypeDef:
    pass
```

### list_built_in_slot_types

Type annotations for `boto3.client("lexv2-models").list_built_in_slot_types` method.

[Client.list_built_in_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)

```python
def list_built_in_slot_types(
    self,
    localeId: str,
    sortBy: BuiltInSlotTypeSortByTypeDef = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListBuiltInSlotTypesResponseTypeDef:
    pass
```

### list_intents

Type annotations for `boto3.client("lexv2-models").list_intents` method.

[Client.list_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)

```python
def list_intents(
    self,
    botId: str,
    botVersion: str,
    localeId: str,
    sortBy: IntentSortByTypeDef = None,
    filters: List[IntentFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListIntentsResponseTypeDef:
    pass
```

### list_slot_types

Type annotations for `boto3.client("lexv2-models").list_slot_types` method.

[Client.list_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)

```python
def list_slot_types(
    self,
    botId: str,
    botVersion: str,
    localeId: str,
    sortBy: SlotTypeSortByTypeDef = None,
    filters: List[SlotTypeFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListSlotTypesResponseTypeDef:
    pass
```

### list_slots

Type annotations for `boto3.client("lexv2-models").list_slots` method.

[Client.list_slots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)

```python
def list_slots(
    self,
    botId: str,
    botVersion: str,
    localeId: str,
    intentId: str,
    sortBy: SlotSortByTypeDef = None,
    filters: List[SlotFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListSlotsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("lexv2-models").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("lexv2-models").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceARN: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("lexv2-models").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceARN: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_bot

Type annotations for `boto3.client("lexv2-models").update_bot` method.

[Client.update_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)

```python
def update_bot(
    self,
    botId: str,
    botName: str,
    roleArn: str,
    dataPrivacy: "DataPrivacyTypeDef",
    idleSessionTTLInSeconds: int,
    description: str = None
) -> UpdateBotResponseTypeDef:
    pass
```

### update_bot_alias

Type annotations for `boto3.client("lexv2-models").update_bot_alias` method.

[Client.update_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)

```python
def update_bot_alias(
    self,
    botAliasId: str,
    botAliasName: str,
    botId: str,
    description: str = None,
    botVersion: str = None,
    botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
    conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
    sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None
) -> UpdateBotAliasResponseTypeDef:
    pass
```

### update_bot_locale

Type annotations for `boto3.client("lexv2-models").update_bot_locale` method.

[Client.update_bot_locale documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)

```python
def update_bot_locale(
    self,
    botId: str,
    botVersion: str,
    localeId: str,
    nluIntentConfidenceThreshold: float,
    description: str = None,
    voiceSettings: "VoiceSettingsTypeDef" = None
) -> UpdateBotLocaleResponseTypeDef:
    pass
```

### update_intent

Type annotations for `boto3.client("lexv2-models").update_intent` method.

[Client.update_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)

```python
def update_intent(
    self,
    intentId: str,
    intentName: str,
    botId: str,
    botVersion: str,
    localeId: str,
    description: str = None,
    parentIntentSignature: str = None,
    sampleUtterances: List["SampleUtteranceTypeDef"] = None,
    dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
    fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
    slotPriorities: List["SlotPriorityTypeDef"] = None,
    intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
    intentClosingSetting: "IntentClosingSettingTypeDef" = None,
    inputContexts: List["InputContextTypeDef"] = None,
    outputContexts: List["OutputContextTypeDef"] = None,
    kendraConfiguration: "KendraConfigurationTypeDef" = None
) -> UpdateIntentResponseTypeDef:
    pass
```

### update_slot

Type annotations for `boto3.client("lexv2-models").update_slot` method.

[Client.update_slot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)

```python
def update_slot(
    self,
    slotId: str,
    slotName: str,
    slotTypeId: str,
    valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
    botId: str,
    botVersion: str,
    localeId: str,
    intentId: str,
    description: str = None,
    obfuscationSetting: "ObfuscationSettingTypeDef" = None
) -> UpdateSlotResponseTypeDef:
    pass
```

### update_slot_type

Type annotations for `boto3.client("lexv2-models").update_slot_type` method.

[Client.update_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)

```python
def update_slot_type(
    self,
    slotTypeId: str,
    slotTypeName: str,
    valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
    botId: str,
    botVersion: str,
    localeId: str,
    description: str = None,
    slotTypeValues: List["SlotTypeValueTypeDef"] = None,
    parentSlotTypeSignature: str = None
) -> UpdateSlotTypeResponseTypeDef:
    pass
```