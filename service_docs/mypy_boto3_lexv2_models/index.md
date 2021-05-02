# Type annotations for boto3 LexModelsV2 module

> [Index](../index.md) > LexModelsV2

Auto-generated documentation for [LexModelsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2)
type annotations stubs module [mypy_boto3_lexv2_models](https://pypi.org/project/mypy-boto3-lexv2-models/).

```bash
pip install mypy-boto3-lexv2-models
```

- [Type annotations for boto3 LexModelsV2 module](#type-annotations-for-boto3-lexmodelsv2-module)
  - [LexModelsV2Client](#lexmodelsv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## LexModelsV2Client

Type annotations for  `boto3.client("lexv2-models")` as [LexModelsV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_lexv2_models.client import LexModelsV2Client
```


LexModelsV2Client [exceptions](./client.md#exceptions)



### Methods
- [build_bot_locale](./client.md#build-bot-locale)
- [can_paginate](./client.md#can-paginate)
- [create_bot](./client.md#create-bot)
- [create_bot_alias](./client.md#create-bot-alias)
- [create_bot_locale](./client.md#create-bot-locale)
- [create_bot_version](./client.md#create-bot-version)
- [create_intent](./client.md#create-intent)
- [create_slot](./client.md#create-slot)
- [create_slot_type](./client.md#create-slot-type)
- [delete_bot](./client.md#delete-bot)
- [delete_bot_alias](./client.md#delete-bot-alias)
- [delete_bot_locale](./client.md#delete-bot-locale)
- [delete_bot_version](./client.md#delete-bot-version)
- [delete_intent](./client.md#delete-intent)
- [delete_slot](./client.md#delete-slot)
- [delete_slot_type](./client.md#delete-slot-type)
- [describe_bot](./client.md#describe-bot)
- [describe_bot_alias](./client.md#describe-bot-alias)
- [describe_bot_locale](./client.md#describe-bot-locale)
- [describe_bot_version](./client.md#describe-bot-version)
- [describe_intent](./client.md#describe-intent)
- [describe_slot](./client.md#describe-slot)
- [describe_slot_type](./client.md#describe-slot-type)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_bot_aliases](./client.md#list-bot-aliases)
- [list_bot_locales](./client.md#list-bot-locales)
- [list_bot_versions](./client.md#list-bot-versions)
- [list_bots](./client.md#list-bots)
- [list_built_in_intents](./client.md#list-built-in-intents)
- [list_built_in_slot_types](./client.md#list-built-in-slot-types)
- [list_intents](./client.md#list-intents)
- [list_slot_types](./client.md#list-slot-types)
- [list_slots](./client.md#list-slots)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_bot](./client.md#update-bot)
- [update_bot_alias](./client.md#update-bot-alias)
- [update_bot_locale](./client.md#update-bot-locale)
- [update_intent](./client.md#update-intent)
- [update_slot](./client.md#update-slot)
- [update_slot_type](./client.md#update-slot-type)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [PreconditionFailedException](./client.md#preconditionfailedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lexv2_models.literals import BotAliasStatus, ...
```

- [BotAliasStatus](./literals.md#botaliasstatus)
- [BotFilterName](./literals.md#botfiltername)
- [BotFilterOperator](./literals.md#botfilteroperator)
- [BotLocaleFilterName](./literals.md#botlocalefiltername)
- [BotLocaleFilterOperator](./literals.md#botlocalefilteroperator)
- [BotLocaleSortAttribute](./literals.md#botlocalesortattribute)
- [BotLocaleStatus](./literals.md#botlocalestatus)
- [BotSortAttribute](./literals.md#botsortattribute)
- [BotStatus](./literals.md#botstatus)
- [BotVersionSortAttribute](./literals.md#botversionsortattribute)
- [BuiltInIntentSortAttribute](./literals.md#builtinintentsortattribute)
- [BuiltInSlotTypeSortAttribute](./literals.md#builtinslottypesortattribute)
- [IntentFilterName](./literals.md#intentfiltername)
- [IntentFilterOperator](./literals.md#intentfilteroperator)
- [IntentSortAttribute](./literals.md#intentsortattribute)
- [ObfuscationSettingType](./literals.md#obfuscationsettingtype)
- [SlotConstraint](./literals.md#slotconstraint)
- [SlotFilterName](./literals.md#slotfiltername)
- [SlotFilterOperator](./literals.md#slotfilteroperator)
- [SlotSortAttribute](./literals.md#slotsortattribute)
- [SlotTypeFilterName](./literals.md#slottypefiltername)
- [SlotTypeFilterOperator](./literals.md#slottypefilteroperator)
- [SlotTypeSortAttribute](./literals.md#slottypesortattribute)
- [SlotValueResolutionStrategy](./literals.md#slotvalueresolutionstrategy)
- [SortOrder](./literals.md#sortorder)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lexv2_models.type_defs import AudioLogDestinationTypeDef, ...
```

- [AudioLogDestinationTypeDef](./type_defs.md#audiologdestinationtypedef)
- [AudioLogSettingTypeDef](./type_defs.md#audiologsettingtypedef)
- [BotAliasHistoryEventTypeDef](./type_defs.md#botaliashistoryeventtypedef)
- [BotAliasLocaleSettingsTypeDef](./type_defs.md#botaliaslocalesettingstypedef)
- [BotAliasSummaryTypeDef](./type_defs.md#botaliassummarytypedef)
- [BotLocaleHistoryEventTypeDef](./type_defs.md#botlocalehistoryeventtypedef)
- [BotLocaleSummaryTypeDef](./type_defs.md#botlocalesummarytypedef)
- [BotSummaryTypeDef](./type_defs.md#botsummarytypedef)
- [BotVersionLocaleDetailsTypeDef](./type_defs.md#botversionlocaledetailstypedef)
- [BotVersionSummaryTypeDef](./type_defs.md#botversionsummarytypedef)
- [BuiltInIntentSummaryTypeDef](./type_defs.md#builtinintentsummarytypedef)
- [BuiltInSlotTypeSummaryTypeDef](./type_defs.md#builtinslottypesummarytypedef)
- [ButtonTypeDef](./type_defs.md#buttontypedef)
- [CloudWatchLogGroupLogDestinationTypeDef](./type_defs.md#cloudwatchloggrouplogdestinationtypedef)
- [CodeHookSpecificationTypeDef](./type_defs.md#codehookspecificationtypedef)
- [ConversationLogSettingsTypeDef](./type_defs.md#conversationlogsettingstypedef)
- [CustomPayloadTypeDef](./type_defs.md#custompayloadtypedef)
- [DataPrivacyTypeDef](./type_defs.md#dataprivacytypedef)
- [DialogCodeHookSettingsTypeDef](./type_defs.md#dialogcodehooksettingstypedef)
- [FulfillmentCodeHookSettingsTypeDef](./type_defs.md#fulfillmentcodehooksettingstypedef)
- [ImageResponseCardTypeDef](./type_defs.md#imageresponsecardtypedef)
- [InputContextTypeDef](./type_defs.md#inputcontexttypedef)
- [IntentClosingSettingTypeDef](./type_defs.md#intentclosingsettingtypedef)
- [IntentConfirmationSettingTypeDef](./type_defs.md#intentconfirmationsettingtypedef)
- [IntentSummaryTypeDef](./type_defs.md#intentsummarytypedef)
- [KendraConfigurationTypeDef](./type_defs.md#kendraconfigurationtypedef)
- [LambdaCodeHookTypeDef](./type_defs.md#lambdacodehooktypedef)
- [MessageGroupTypeDef](./type_defs.md#messagegrouptypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [ObfuscationSettingTypeDef](./type_defs.md#obfuscationsettingtypedef)
- [OutputContextTypeDef](./type_defs.md#outputcontexttypedef)
- [PlainTextMessageTypeDef](./type_defs.md#plaintextmessagetypedef)
- [PromptSpecificationTypeDef](./type_defs.md#promptspecificationtypedef)
- [ResponseSpecificationTypeDef](./type_defs.md#responsespecificationtypedef)
- [S3BucketLogDestinationTypeDef](./type_defs.md#s3bucketlogdestinationtypedef)
- [SSMLMessageTypeDef](./type_defs.md#ssmlmessagetypedef)
- [SampleUtteranceTypeDef](./type_defs.md#sampleutterancetypedef)
- [SampleValueTypeDef](./type_defs.md#samplevaluetypedef)
- [SentimentAnalysisSettingsTypeDef](./type_defs.md#sentimentanalysissettingstypedef)
- [SlotDefaultValueSpecificationTypeDef](./type_defs.md#slotdefaultvaluespecificationtypedef)
- [SlotDefaultValueTypeDef](./type_defs.md#slotdefaultvaluetypedef)
- [SlotPriorityTypeDef](./type_defs.md#slotprioritytypedef)
- [SlotSummaryTypeDef](./type_defs.md#slotsummarytypedef)
- [SlotTypeSummaryTypeDef](./type_defs.md#slottypesummarytypedef)
- [SlotTypeValueTypeDef](./type_defs.md#slottypevaluetypedef)
- [SlotValueElicitationSettingTypeDef](./type_defs.md#slotvalueelicitationsettingtypedef)
- [SlotValueRegexFilterTypeDef](./type_defs.md#slotvalueregexfiltertypedef)
- [SlotValueSelectionSettingTypeDef](./type_defs.md#slotvalueselectionsettingtypedef)
- [StillWaitingResponseSpecificationTypeDef](./type_defs.md#stillwaitingresponsespecificationtypedef)
- [TextLogDestinationTypeDef](./type_defs.md#textlogdestinationtypedef)
- [TextLogSettingTypeDef](./type_defs.md#textlogsettingtypedef)
- [VoiceSettingsTypeDef](./type_defs.md#voicesettingstypedef)
- [WaitAndContinueSpecificationTypeDef](./type_defs.md#waitandcontinuespecificationtypedef)
- [BotFilterTypeDef](./type_defs.md#botfiltertypedef)
- [BotLocaleFilterTypeDef](./type_defs.md#botlocalefiltertypedef)
- [BotLocaleSortByTypeDef](./type_defs.md#botlocalesortbytypedef)
- [BotSortByTypeDef](./type_defs.md#botsortbytypedef)
- [BotVersionSortByTypeDef](./type_defs.md#botversionsortbytypedef)
- [BuildBotLocaleResponseTypeDef](./type_defs.md#buildbotlocaleresponsetypedef)
- [BuiltInIntentSortByTypeDef](./type_defs.md#builtinintentsortbytypedef)
- [BuiltInSlotTypeSortByTypeDef](./type_defs.md#builtinslottypesortbytypedef)
- [CreateBotAliasResponseTypeDef](./type_defs.md#createbotaliasresponsetypedef)
- [CreateBotLocaleResponseTypeDef](./type_defs.md#createbotlocaleresponsetypedef)
- [CreateBotResponseTypeDef](./type_defs.md#createbotresponsetypedef)
- [CreateBotVersionResponseTypeDef](./type_defs.md#createbotversionresponsetypedef)
- [CreateIntentResponseTypeDef](./type_defs.md#createintentresponsetypedef)
- [CreateSlotResponseTypeDef](./type_defs.md#createslotresponsetypedef)
- [CreateSlotTypeResponseTypeDef](./type_defs.md#createslottyperesponsetypedef)
- [DeleteBotAliasResponseTypeDef](./type_defs.md#deletebotaliasresponsetypedef)
- [DeleteBotLocaleResponseTypeDef](./type_defs.md#deletebotlocaleresponsetypedef)
- [DeleteBotResponseTypeDef](./type_defs.md#deletebotresponsetypedef)
- [DeleteBotVersionResponseTypeDef](./type_defs.md#deletebotversionresponsetypedef)
- [DescribeBotAliasResponseTypeDef](./type_defs.md#describebotaliasresponsetypedef)
- [DescribeBotLocaleResponseTypeDef](./type_defs.md#describebotlocaleresponsetypedef)
- [DescribeBotResponseTypeDef](./type_defs.md#describebotresponsetypedef)
- [DescribeBotVersionResponseTypeDef](./type_defs.md#describebotversionresponsetypedef)
- [DescribeIntentResponseTypeDef](./type_defs.md#describeintentresponsetypedef)
- [DescribeSlotResponseTypeDef](./type_defs.md#describeslotresponsetypedef)
- [DescribeSlotTypeResponseTypeDef](./type_defs.md#describeslottyperesponsetypedef)
- [IntentFilterTypeDef](./type_defs.md#intentfiltertypedef)
- [IntentSortByTypeDef](./type_defs.md#intentsortbytypedef)
- [ListBotAliasesResponseTypeDef](./type_defs.md#listbotaliasesresponsetypedef)
- [ListBotLocalesResponseTypeDef](./type_defs.md#listbotlocalesresponsetypedef)
- [ListBotVersionsResponseTypeDef](./type_defs.md#listbotversionsresponsetypedef)
- [ListBotsResponseTypeDef](./type_defs.md#listbotsresponsetypedef)
- [ListBuiltInIntentsResponseTypeDef](./type_defs.md#listbuiltinintentsresponsetypedef)
- [ListBuiltInSlotTypesResponseTypeDef](./type_defs.md#listbuiltinslottypesresponsetypedef)
- [ListIntentsResponseTypeDef](./type_defs.md#listintentsresponsetypedef)
- [ListSlotTypesResponseTypeDef](./type_defs.md#listslottypesresponsetypedef)
- [ListSlotsResponseTypeDef](./type_defs.md#listslotsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [SlotFilterTypeDef](./type_defs.md#slotfiltertypedef)
- [SlotSortByTypeDef](./type_defs.md#slotsortbytypedef)
- [SlotTypeFilterTypeDef](./type_defs.md#slottypefiltertypedef)
- [SlotTypeSortByTypeDef](./type_defs.md#slottypesortbytypedef)
- [UpdateBotAliasResponseTypeDef](./type_defs.md#updatebotaliasresponsetypedef)
- [UpdateBotLocaleResponseTypeDef](./type_defs.md#updatebotlocaleresponsetypedef)
- [UpdateBotResponseTypeDef](./type_defs.md#updatebotresponsetypedef)
- [UpdateIntentResponseTypeDef](./type_defs.md#updateintentresponsetypedef)
- [UpdateSlotResponseTypeDef](./type_defs.md#updateslotresponsetypedef)
- [UpdateSlotTypeResponseTypeDef](./type_defs.md#updateslottyperesponsetypedef)
