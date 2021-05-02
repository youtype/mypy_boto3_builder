# Type annotations for boto3 LexModelBuildingService module

> [Index](../index.md) > LexModelBuildingService

Auto-generated documentation for [LexModelBuildingService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService)
type annotations stubs module [mypy_boto3_lex_models](https://pypi.org/project/mypy-boto3-lex-models/).

```bash
pip install mypy-boto3-lex-models
```

- [Type annotations for boto3 LexModelBuildingService module](#type-annotations-for-boto3-lexmodelbuildingservice-module)
  - [LexModelBuildingServiceClient](#lexmodelbuildingserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## LexModelBuildingServiceClient

Type annotations for  `boto3.client("lex-models")` as [LexModelBuildingServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lex_models.client import LexModelBuildingServiceClient
```


LexModelBuildingServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_bot_version](./client.md#create-bot-version)
- [create_intent_version](./client.md#create-intent-version)
- [create_slot_type_version](./client.md#create-slot-type-version)
- [delete_bot](./client.md#delete-bot)
- [delete_bot_alias](./client.md#delete-bot-alias)
- [delete_bot_channel_association](./client.md#delete-bot-channel-association)
- [delete_bot_version](./client.md#delete-bot-version)
- [delete_intent](./client.md#delete-intent)
- [delete_intent_version](./client.md#delete-intent-version)
- [delete_slot_type](./client.md#delete-slot-type)
- [delete_slot_type_version](./client.md#delete-slot-type-version)
- [delete_utterances](./client.md#delete-utterances)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_bot](./client.md#get-bot)
- [get_bot_alias](./client.md#get-bot-alias)
- [get_bot_aliases](./client.md#get-bot-aliases)
- [get_bot_channel_association](./client.md#get-bot-channel-association)
- [get_bot_channel_associations](./client.md#get-bot-channel-associations)
- [get_bot_versions](./client.md#get-bot-versions)
- [get_bots](./client.md#get-bots)
- [get_builtin_intent](./client.md#get-builtin-intent)
- [get_builtin_intents](./client.md#get-builtin-intents)
- [get_builtin_slot_types](./client.md#get-builtin-slot-types)
- [get_export](./client.md#get-export)
- [get_import](./client.md#get-import)
- [get_intent](./client.md#get-intent)
- [get_intent_versions](./client.md#get-intent-versions)
- [get_intents](./client.md#get-intents)
- [get_paginator](./client.md#get-paginator)
- [get_slot_type](./client.md#get-slot-type)
- [get_slot_type_versions](./client.md#get-slot-type-versions)
- [get_slot_types](./client.md#get-slot-types)
- [get_utterances_view](./client.md#get-utterances-view)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_bot](./client.md#put-bot)
- [put_bot_alias](./client.md#put-bot-alias)
- [put_intent](./client.md#put-intent)
- [put_slot_type](./client.md#put-slot-type)
- [start_import](./client.md#start-import)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [PreconditionFailedException](./client.md#preconditionfailedexception)
- [ResourceInUseException](./client.md#resourceinuseexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("lex-models").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBotAliasesPaginator, ...
```

- [GetBotAliasesPaginator](./paginators.md#getbotaliasespaginator)
- [GetBotChannelAssociationsPaginator](./paginators.md#getbotchannelassociationspaginator)
- [GetBotVersionsPaginator](./paginators.md#getbotversionspaginator)
- [GetBotsPaginator](./paginators.md#getbotspaginator)
- [GetBuiltinIntentsPaginator](./paginators.md#getbuiltinintentspaginator)
- [GetBuiltinSlotTypesPaginator](./paginators.md#getbuiltinslottypespaginator)
- [GetIntentVersionsPaginator](./paginators.md#getintentversionspaginator)
- [GetIntentsPaginator](./paginators.md#getintentspaginator)
- [GetSlotTypeVersionsPaginator](./paginators.md#getslottypeversionspaginator)
- [GetSlotTypesPaginator](./paginators.md#getslottypespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lex_models.literals import ChannelStatus, ...
```

- [ChannelStatus](./literals.md#channelstatus)
- [ChannelType](./literals.md#channeltype)
- [ContentType](./literals.md#contenttype)
- [Destination](./literals.md#destination)
- [ExportStatus](./literals.md#exportstatus)
- [ExportType](./literals.md#exporttype)
- [FulfillmentActivityType](./literals.md#fulfillmentactivitytype)
- [GetBotAliasesPaginatorName](./literals.md#getbotaliasespaginatorname)
- [GetBotChannelAssociationsPaginatorName](./literals.md#getbotchannelassociationspaginatorname)
- [GetBotVersionsPaginatorName](./literals.md#getbotversionspaginatorname)
- [GetBotsPaginatorName](./literals.md#getbotspaginatorname)
- [GetBuiltinIntentsPaginatorName](./literals.md#getbuiltinintentspaginatorname)
- [GetBuiltinSlotTypesPaginatorName](./literals.md#getbuiltinslottypespaginatorname)
- [GetIntentVersionsPaginatorName](./literals.md#getintentversionspaginatorname)
- [GetIntentsPaginatorName](./literals.md#getintentspaginatorname)
- [GetSlotTypeVersionsPaginatorName](./literals.md#getslottypeversionspaginatorname)
- [GetSlotTypesPaginatorName](./literals.md#getslottypespaginatorname)
- [ImportStatus](./literals.md#importstatus)
- [Locale](./literals.md#locale)
- [LogType](./literals.md#logtype)
- [MergeStrategy](./literals.md#mergestrategy)
- [ObfuscationSetting](./literals.md#obfuscationsetting)
- [ProcessBehavior](./literals.md#processbehavior)
- [ResourceType](./literals.md#resourcetype)
- [SlotConstraint](./literals.md#slotconstraint)
- [SlotValueSelectionStrategy](./literals.md#slotvalueselectionstrategy)
- [Status](./literals.md#status)
- [StatusType](./literals.md#statustype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lex_models.type_defs import BotAliasMetadataTypeDef, ...
```

- [BotAliasMetadataTypeDef](./type_defs.md#botaliasmetadatatypedef)
- [BotChannelAssociationTypeDef](./type_defs.md#botchannelassociationtypedef)
- [BotMetadataTypeDef](./type_defs.md#botmetadatatypedef)
- [BuiltinIntentMetadataTypeDef](./type_defs.md#builtinintentmetadatatypedef)
- [BuiltinIntentSlotTypeDef](./type_defs.md#builtinintentslottypedef)
- [BuiltinSlotTypeMetadataTypeDef](./type_defs.md#builtinslottypemetadatatypedef)
- [CodeHookTypeDef](./type_defs.md#codehooktypedef)
- [ConversationLogsResponseTypeDef](./type_defs.md#conversationlogsresponsetypedef)
- [EnumerationValueTypeDef](./type_defs.md#enumerationvaluetypedef)
- [FollowUpPromptTypeDef](./type_defs.md#followupprompttypedef)
- [FulfillmentActivityTypeDef](./type_defs.md#fulfillmentactivitytypedef)
- [InputContextTypeDef](./type_defs.md#inputcontexttypedef)
- [IntentMetadataTypeDef](./type_defs.md#intentmetadatatypedef)
- [IntentTypeDef](./type_defs.md#intenttypedef)
- [KendraConfigurationTypeDef](./type_defs.md#kendraconfigurationtypedef)
- [LogSettingsRequestTypeDef](./type_defs.md#logsettingsrequesttypedef)
- [LogSettingsResponseTypeDef](./type_defs.md#logsettingsresponsetypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [OutputContextTypeDef](./type_defs.md#outputcontexttypedef)
- [PromptTypeDef](./type_defs.md#prompttypedef)
- [SlotDefaultValueSpecTypeDef](./type_defs.md#slotdefaultvaluespectypedef)
- [SlotDefaultValueTypeDef](./type_defs.md#slotdefaultvaluetypedef)
- [SlotTypeConfigurationTypeDef](./type_defs.md#slottypeconfigurationtypedef)
- [SlotTypeDef](./type_defs.md#slottypedef)
- [SlotTypeMetadataTypeDef](./type_defs.md#slottypemetadatatypedef)
- [SlotTypeRegexConfigurationTypeDef](./type_defs.md#slottyperegexconfigurationtypedef)
- [StatementTypeDef](./type_defs.md#statementtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UtteranceDataTypeDef](./type_defs.md#utterancedatatypedef)
- [UtteranceListTypeDef](./type_defs.md#utterancelisttypedef)
- [ConversationLogsRequestTypeDef](./type_defs.md#conversationlogsrequesttypedef)
- [CreateBotVersionResponseTypeDef](./type_defs.md#createbotversionresponsetypedef)
- [CreateIntentVersionResponseTypeDef](./type_defs.md#createintentversionresponsetypedef)
- [CreateSlotTypeVersionResponseTypeDef](./type_defs.md#createslottypeversionresponsetypedef)
- [GetBotAliasResponseTypeDef](./type_defs.md#getbotaliasresponsetypedef)
- [GetBotAliasesResponseTypeDef](./type_defs.md#getbotaliasesresponsetypedef)
- [GetBotChannelAssociationResponseTypeDef](./type_defs.md#getbotchannelassociationresponsetypedef)
- [GetBotChannelAssociationsResponseTypeDef](./type_defs.md#getbotchannelassociationsresponsetypedef)
- [GetBotResponseTypeDef](./type_defs.md#getbotresponsetypedef)
- [GetBotVersionsResponseTypeDef](./type_defs.md#getbotversionsresponsetypedef)
- [GetBotsResponseTypeDef](./type_defs.md#getbotsresponsetypedef)
- [GetBuiltinIntentResponseTypeDef](./type_defs.md#getbuiltinintentresponsetypedef)
- [GetBuiltinIntentsResponseTypeDef](./type_defs.md#getbuiltinintentsresponsetypedef)
- [GetBuiltinSlotTypesResponseTypeDef](./type_defs.md#getbuiltinslottypesresponsetypedef)
- [GetExportResponseTypeDef](./type_defs.md#getexportresponsetypedef)
- [GetImportResponseTypeDef](./type_defs.md#getimportresponsetypedef)
- [GetIntentResponseTypeDef](./type_defs.md#getintentresponsetypedef)
- [GetIntentVersionsResponseTypeDef](./type_defs.md#getintentversionsresponsetypedef)
- [GetIntentsResponseTypeDef](./type_defs.md#getintentsresponsetypedef)
- [GetSlotTypeResponseTypeDef](./type_defs.md#getslottyperesponsetypedef)
- [GetSlotTypeVersionsResponseTypeDef](./type_defs.md#getslottypeversionsresponsetypedef)
- [GetSlotTypesResponseTypeDef](./type_defs.md#getslottypesresponsetypedef)
- [GetUtterancesViewResponseTypeDef](./type_defs.md#getutterancesviewresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutBotAliasResponseTypeDef](./type_defs.md#putbotaliasresponsetypedef)
- [PutBotResponseTypeDef](./type_defs.md#putbotresponsetypedef)
- [PutIntentResponseTypeDef](./type_defs.md#putintentresponsetypedef)
- [PutSlotTypeResponseTypeDef](./type_defs.md#putslottyperesponsetypedef)
- [StartImportResponseTypeDef](./type_defs.md#startimportresponsetypedef)
