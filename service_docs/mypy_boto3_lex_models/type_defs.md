# Structures for boto3 LexModelBuildingService module

> [Index](../index.md) > [LexModelBuildingService](./index.md) > Structures

Auto-generated documentation for [LexModelBuildingService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService)
type annotations stubs module [mypy_boto3_lex_models](https://pypi.org/project/mypy-boto3-lex-models/).

- [Structures for boto3 LexModelBuildingService module](#structures-for-boto3-lexmodelbuildingservice-module)
  - [BotAliasMetadataTypeDef](#botaliasmetadatatypedef)
  - [BotChannelAssociationTypeDef](#botchannelassociationtypedef)
  - [BotMetadataTypeDef](#botmetadatatypedef)
  - [BuiltinIntentMetadataTypeDef](#builtinintentmetadatatypedef)
  - [BuiltinIntentSlotTypeDef](#builtinintentslottypedef)
  - [BuiltinSlotTypeMetadataTypeDef](#builtinslottypemetadatatypedef)
  - [CodeHookTypeDef](#codehooktypedef)
  - [ConversationLogsResponseTypeDef](#conversationlogsresponsetypedef)
  - [EnumerationValueTypeDef](#enumerationvaluetypedef)
  - [FollowUpPromptTypeDef](#followupprompttypedef)
  - [FulfillmentActivityTypeDef](#fulfillmentactivitytypedef)
  - [InputContextTypeDef](#inputcontexttypedef)
  - [IntentMetadataTypeDef](#intentmetadatatypedef)
  - [IntentTypeDef](#intenttypedef)
  - [KendraConfigurationTypeDef](#kendraconfigurationtypedef)
  - [LogSettingsRequestTypeDef](#logsettingsrequesttypedef)
  - [LogSettingsResponseTypeDef](#logsettingsresponsetypedef)
  - [MessageTypeDef](#messagetypedef)
  - [OutputContextTypeDef](#outputcontexttypedef)
  - [PromptTypeDef](#prompttypedef)
  - [SlotDefaultValueSpecTypeDef](#slotdefaultvaluespectypedef)
  - [SlotDefaultValueTypeDef](#slotdefaultvaluetypedef)
  - [SlotTypeConfigurationTypeDef](#slottypeconfigurationtypedef)
  - [SlotTypeDef](#slottypedef)
  - [SlotTypeMetadataTypeDef](#slottypemetadatatypedef)
  - [SlotTypeRegexConfigurationTypeDef](#slottyperegexconfigurationtypedef)
  - [StatementTypeDef](#statementtypedef)
  - [TagTypeDef](#tagtypedef)
  - [UtteranceDataTypeDef](#utterancedatatypedef)
  - [UtteranceListTypeDef](#utterancelisttypedef)
  - [ConversationLogsRequestTypeDef](#conversationlogsrequesttypedef)
  - [CreateBotVersionResponseTypeDef](#createbotversionresponsetypedef)
  - [CreateIntentVersionResponseTypeDef](#createintentversionresponsetypedef)
  - [CreateSlotTypeVersionResponseTypeDef](#createslottypeversionresponsetypedef)
  - [GetBotAliasResponseTypeDef](#getbotaliasresponsetypedef)
  - [GetBotAliasesResponseTypeDef](#getbotaliasesresponsetypedef)
  - [GetBotChannelAssociationResponseTypeDef](#getbotchannelassociationresponsetypedef)
  - [GetBotChannelAssociationsResponseTypeDef](#getbotchannelassociationsresponsetypedef)
  - [GetBotResponseTypeDef](#getbotresponsetypedef)
  - [GetBotVersionsResponseTypeDef](#getbotversionsresponsetypedef)
  - [GetBotsResponseTypeDef](#getbotsresponsetypedef)
  - [GetBuiltinIntentResponseTypeDef](#getbuiltinintentresponsetypedef)
  - [GetBuiltinIntentsResponseTypeDef](#getbuiltinintentsresponsetypedef)
  - [GetBuiltinSlotTypesResponseTypeDef](#getbuiltinslottypesresponsetypedef)
  - [GetExportResponseTypeDef](#getexportresponsetypedef)
  - [GetImportResponseTypeDef](#getimportresponsetypedef)
  - [GetIntentResponseTypeDef](#getintentresponsetypedef)
  - [GetIntentVersionsResponseTypeDef](#getintentversionsresponsetypedef)
  - [GetIntentsResponseTypeDef](#getintentsresponsetypedef)
  - [GetSlotTypeResponseTypeDef](#getslottyperesponsetypedef)
  - [GetSlotTypeVersionsResponseTypeDef](#getslottypeversionsresponsetypedef)
  - [GetSlotTypesResponseTypeDef](#getslottypesresponsetypedef)
  - [GetUtterancesViewResponseTypeDef](#getutterancesviewresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutBotAliasResponseTypeDef](#putbotaliasresponsetypedef)
  - [PutBotResponseTypeDef](#putbotresponsetypedef)
  - [PutIntentResponseTypeDef](#putintentresponsetypedef)
  - [PutSlotTypeResponseTypeDef](#putslottyperesponsetypedef)
  - [StartImportResponseTypeDef](#startimportresponsetypedef)

## BotAliasMetadataTypeDef

```python
from mypy_boto3_lex_models.type_defs import BotAliasMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botName`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `checksum`: `str`
- `conversationLogs`: `"ConversationLogsResponseTypeDef"`


## BotChannelAssociationTypeDef

```python
from mypy_boto3_lex_models.type_defs import BotChannelAssociationTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `botAlias`: `str`
- `botName`: `str`
- `createdDate`: `datetime`
- `type`: `ChannelType`
- `botConfiguration`: `Dict[str, str]`
- `status`: `ChannelStatus`
- `failureReason`: `str`


## BotMetadataTypeDef

```python
from mypy_boto3_lex_models.type_defs import BotMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `status`: `Status`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`


## BuiltinIntentMetadataTypeDef

```python
from mypy_boto3_lex_models.type_defs import BuiltinIntentMetadataTypeDef
```




Optional fields:
- `signature`: `str`
- `supportedLocales`: `List[Locale]`


## BuiltinIntentSlotTypeDef

```python
from mypy_boto3_lex_models.type_defs import BuiltinIntentSlotTypeDef
```




Optional fields:
- `name`: `str`


## BuiltinSlotTypeMetadataTypeDef

```python
from mypy_boto3_lex_models.type_defs import BuiltinSlotTypeMetadataTypeDef
```




Optional fields:
- `signature`: `str`
- `supportedLocales`: `List[Locale]`


## CodeHookTypeDef

```python
from mypy_boto3_lex_models.type_defs import CodeHookTypeDef
```


Required fields:
- `uri`: `str`
- `messageVersion`: `str`




## ConversationLogsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import ConversationLogsResponseTypeDef
```




Optional fields:
- `logSettings`: `List["LogSettingsResponseTypeDef"]`
- `iamRoleArn`: `str`


## EnumerationValueTypeDef

```python
from mypy_boto3_lex_models.type_defs import EnumerationValueTypeDef
```


Required fields:
- `value`: `str`



Optional fields:
- `synonyms`: `List[str]`


## FollowUpPromptTypeDef

```python
from mypy_boto3_lex_models.type_defs import FollowUpPromptTypeDef
```


Required fields:
- `prompt`: `"PromptTypeDef"`
- `rejectionStatement`: `"StatementTypeDef"`




## FulfillmentActivityTypeDef

```python
from mypy_boto3_lex_models.type_defs import FulfillmentActivityTypeDef
```


Required fields:
- `type`: `FulfillmentActivityType`



Optional fields:
- `codeHook`: `"CodeHookTypeDef"`


## InputContextTypeDef

```python
from mypy_boto3_lex_models.type_defs import InputContextTypeDef
```


Required fields:
- `name`: `str`




## IntentMetadataTypeDef

```python
from mypy_boto3_lex_models.type_defs import IntentMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`


## IntentTypeDef

```python
from mypy_boto3_lex_models.type_defs import IntentTypeDef
```


Required fields:
- `intentName`: `str`
- `intentVersion`: `str`




## KendraConfigurationTypeDef

```python
from mypy_boto3_lex_models.type_defs import KendraConfigurationTypeDef
```


Required fields:
- `kendraIndex`: `str`
- `role`: `str`



Optional fields:
- `queryFilterString`: `str`


## LogSettingsRequestTypeDef

```python
from mypy_boto3_lex_models.type_defs import LogSettingsRequestTypeDef
```


Required fields:
- `logType`: `LogType`
- `destination`: `Destination`
- `resourceArn`: `str`



Optional fields:
- `kmsKeyArn`: `str`


## LogSettingsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import LogSettingsResponseTypeDef
```




Optional fields:
- `logType`: `LogType`
- `destination`: `Destination`
- `kmsKeyArn`: `str`
- `resourceArn`: `str`
- `resourcePrefix`: `str`


## MessageTypeDef

```python
from mypy_boto3_lex_models.type_defs import MessageTypeDef
```


Required fields:
- `contentType`: `ContentType`
- `content`: `str`



Optional fields:
- `groupNumber`: `int`


## OutputContextTypeDef

```python
from mypy_boto3_lex_models.type_defs import OutputContextTypeDef
```


Required fields:
- `name`: `str`
- `timeToLiveInSeconds`: `int`
- `turnsToLive`: `int`




## PromptTypeDef

```python
from mypy_boto3_lex_models.type_defs import PromptTypeDef
```


Required fields:
- `messages`: `List["MessageTypeDef"]`
- `maxAttempts`: `int`



Optional fields:
- `responseCard`: `str`


## SlotDefaultValueSpecTypeDef

```python
from mypy_boto3_lex_models.type_defs import SlotDefaultValueSpecTypeDef
```


Required fields:
- `defaultValueList`: `List["SlotDefaultValueTypeDef"]`




## SlotDefaultValueTypeDef

```python
from mypy_boto3_lex_models.type_defs import SlotDefaultValueTypeDef
```


Required fields:
- `defaultValue`: `str`




## SlotTypeConfigurationTypeDef

```python
from mypy_boto3_lex_models.type_defs import SlotTypeConfigurationTypeDef
```




Optional fields:
- `regexConfiguration`: `"SlotTypeRegexConfigurationTypeDef"`


## SlotTypeDef

```python
from mypy_boto3_lex_models.type_defs import SlotTypeDef
```


Required fields:
- `name`: `str`
- `slotConstraint`: `SlotConstraint`



Optional fields:
- `description`: `str`
- `slotType`: `str`
- `slotTypeVersion`: `str`
- `valueElicitationPrompt`: `"PromptTypeDef"`
- `priority`: `int`
- `sampleUtterances`: `List[str]`
- `responseCard`: `str`
- `obfuscationSetting`: `ObfuscationSetting`
- `defaultValueSpec`: `"SlotDefaultValueSpecTypeDef"`


## SlotTypeMetadataTypeDef

```python
from mypy_boto3_lex_models.type_defs import SlotTypeMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`


## SlotTypeRegexConfigurationTypeDef

```python
from mypy_boto3_lex_models.type_defs import SlotTypeRegexConfigurationTypeDef
```


Required fields:
- `pattern`: `str`




## StatementTypeDef

```python
from mypy_boto3_lex_models.type_defs import StatementTypeDef
```


Required fields:
- `messages`: `List["MessageTypeDef"]`



Optional fields:
- `responseCard`: `str`


## TagTypeDef

```python
from mypy_boto3_lex_models.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## UtteranceDataTypeDef

```python
from mypy_boto3_lex_models.type_defs import UtteranceDataTypeDef
```




Optional fields:
- `utteranceString`: `str`
- `count`: `int`
- `distinctUsers`: `int`
- `firstUtteredDate`: `datetime`
- `lastUtteredDate`: `datetime`


## UtteranceListTypeDef

```python
from mypy_boto3_lex_models.type_defs import UtteranceListTypeDef
```




Optional fields:
- `botVersion`: `str`
- `utterances`: `List["UtteranceDataTypeDef"]`


## ConversationLogsRequestTypeDef

```python
from mypy_boto3_lex_models.type_defs import ConversationLogsRequestTypeDef
```


Required fields:
- `logSettings`: `List["LogSettingsRequestTypeDef"]`
- `iamRoleArn`: `str`




## CreateBotVersionResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import CreateBotVersionResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `intents`: `List["IntentTypeDef"]`
- `clarificationPrompt`: `"PromptTypeDef"`
- `abortStatement`: `"StatementTypeDef"`
- `status`: `Status`
- `failureReason`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `idleSessionTTLInSeconds`: `int`
- `voiceId`: `str`
- `checksum`: `str`
- `version`: `str`
- `locale`: `Locale`
- `childDirected`: `bool`
- `enableModelImprovements`: `bool`
- `detectSentiment`: `bool`


## CreateIntentVersionResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import CreateIntentVersionResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `slots`: `List["SlotTypeDef"]`
- `sampleUtterances`: `List[str]`
- `confirmationPrompt`: `"PromptTypeDef"`
- `rejectionStatement`: `"StatementTypeDef"`
- `followUpPrompt`: `"FollowUpPromptTypeDef"`
- `conclusionStatement`: `"StatementTypeDef"`
- `dialogCodeHook`: `"CodeHookTypeDef"`
- `fulfillmentActivity`: `"FulfillmentActivityTypeDef"`
- `parentIntentSignature`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`
- `checksum`: `str`
- `kendraConfiguration`: `"KendraConfigurationTypeDef"`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`


## CreateSlotTypeVersionResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import CreateSlotTypeVersionResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `enumerationValues`: `List["EnumerationValueTypeDef"]`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`
- `checksum`: `str`
- `valueSelectionStrategy`: `SlotValueSelectionStrategy`
- `parentSlotTypeSignature`: `str`
- `slotTypeConfigurations`: `List["SlotTypeConfigurationTypeDef"]`


## GetBotAliasResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotAliasResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botName`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `checksum`: `str`
- `conversationLogs`: `"ConversationLogsResponseTypeDef"`


## GetBotAliasesResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotAliasesResponseTypeDef
```




Optional fields:
- `BotAliases`: `List["BotAliasMetadataTypeDef"]`
- `nextToken`: `str`


## GetBotChannelAssociationResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotChannelAssociationResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `botAlias`: `str`
- `botName`: `str`
- `createdDate`: `datetime`
- `type`: `ChannelType`
- `botConfiguration`: `Dict[str, str]`
- `status`: `ChannelStatus`
- `failureReason`: `str`


## GetBotChannelAssociationsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotChannelAssociationsResponseTypeDef
```




Optional fields:
- `botChannelAssociations`: `List["BotChannelAssociationTypeDef"]`
- `nextToken`: `str`


## GetBotResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `intents`: `List["IntentTypeDef"]`
- `enableModelImprovements`: `bool`
- `nluIntentConfidenceThreshold`: `float`
- `clarificationPrompt`: `"PromptTypeDef"`
- `abortStatement`: `"StatementTypeDef"`
- `status`: `Status`
- `failureReason`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `idleSessionTTLInSeconds`: `int`
- `voiceId`: `str`
- `checksum`: `str`
- `version`: `str`
- `locale`: `Locale`
- `childDirected`: `bool`
- `detectSentiment`: `bool`


## GetBotVersionsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotVersionsResponseTypeDef
```




Optional fields:
- `bots`: `List["BotMetadataTypeDef"]`
- `nextToken`: `str`


## GetBotsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBotsResponseTypeDef
```




Optional fields:
- `bots`: `List["BotMetadataTypeDef"]`
- `nextToken`: `str`


## GetBuiltinIntentResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBuiltinIntentResponseTypeDef
```




Optional fields:
- `signature`: `str`
- `supportedLocales`: `List[Locale]`
- `slots`: `List["BuiltinIntentSlotTypeDef"]`


## GetBuiltinIntentsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBuiltinIntentsResponseTypeDef
```




Optional fields:
- `intents`: `List["BuiltinIntentMetadataTypeDef"]`
- `nextToken`: `str`


## GetBuiltinSlotTypesResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetBuiltinSlotTypesResponseTypeDef
```




Optional fields:
- `slotTypes`: `List["BuiltinSlotTypeMetadataTypeDef"]`
- `nextToken`: `str`


## GetExportResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetExportResponseTypeDef
```




Optional fields:
- `name`: `str`
- `version`: `str`
- `resourceType`: `ResourceType`
- `exportType`: `ExportType`
- `exportStatus`: `ExportStatus`
- `failureReason`: `str`
- `url`: `str`


## GetImportResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetImportResponseTypeDef
```




Optional fields:
- `name`: `str`
- `resourceType`: `ResourceType`
- `mergeStrategy`: `MergeStrategy`
- `importId`: `str`
- `importStatus`: `ImportStatus`
- `failureReason`: `List[str]`
- `createdDate`: `datetime`


## GetIntentResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetIntentResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `slots`: `List["SlotTypeDef"]`
- `sampleUtterances`: `List[str]`
- `confirmationPrompt`: `"PromptTypeDef"`
- `rejectionStatement`: `"StatementTypeDef"`
- `followUpPrompt`: `"FollowUpPromptTypeDef"`
- `conclusionStatement`: `"StatementTypeDef"`
- `dialogCodeHook`: `"CodeHookTypeDef"`
- `fulfillmentActivity`: `"FulfillmentActivityTypeDef"`
- `parentIntentSignature`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`
- `checksum`: `str`
- `kendraConfiguration`: `"KendraConfigurationTypeDef"`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`


## GetIntentVersionsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetIntentVersionsResponseTypeDef
```




Optional fields:
- `intents`: `List["IntentMetadataTypeDef"]`
- `nextToken`: `str`


## GetIntentsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetIntentsResponseTypeDef
```




Optional fields:
- `intents`: `List["IntentMetadataTypeDef"]`
- `nextToken`: `str`


## GetSlotTypeResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetSlotTypeResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `enumerationValues`: `List["EnumerationValueTypeDef"]`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`
- `checksum`: `str`
- `valueSelectionStrategy`: `SlotValueSelectionStrategy`
- `parentSlotTypeSignature`: `str`
- `slotTypeConfigurations`: `List["SlotTypeConfigurationTypeDef"]`


## GetSlotTypeVersionsResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetSlotTypeVersionsResponseTypeDef
```




Optional fields:
- `slotTypes`: `List["SlotTypeMetadataTypeDef"]`
- `nextToken`: `str`


## GetSlotTypesResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetSlotTypesResponseTypeDef
```




Optional fields:
- `slotTypes`: `List["SlotTypeMetadataTypeDef"]`
- `nextToken`: `str`


## GetUtterancesViewResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import GetUtterancesViewResponseTypeDef
```




Optional fields:
- `botName`: `str`
- `utterances`: `List["UtteranceListTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_lex_models.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutBotAliasResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import PutBotAliasResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botName`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `checksum`: `str`
- `conversationLogs`: `"ConversationLogsResponseTypeDef"`
- `tags`: `List["TagTypeDef"]`


## PutBotResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import PutBotResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `intents`: `List["IntentTypeDef"]`
- `enableModelImprovements`: `bool`
- `nluIntentConfidenceThreshold`: `float`
- `clarificationPrompt`: `"PromptTypeDef"`
- `abortStatement`: `"StatementTypeDef"`
- `status`: `Status`
- `failureReason`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `idleSessionTTLInSeconds`: `int`
- `voiceId`: `str`
- `checksum`: `str`
- `version`: `str`
- `locale`: `Locale`
- `childDirected`: `bool`
- `createVersion`: `bool`
- `detectSentiment`: `bool`
- `tags`: `List["TagTypeDef"]`


## PutIntentResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import PutIntentResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `slots`: `List["SlotTypeDef"]`
- `sampleUtterances`: `List[str]`
- `confirmationPrompt`: `"PromptTypeDef"`
- `rejectionStatement`: `"StatementTypeDef"`
- `followUpPrompt`: `"FollowUpPromptTypeDef"`
- `conclusionStatement`: `"StatementTypeDef"`
- `dialogCodeHook`: `"CodeHookTypeDef"`
- `fulfillmentActivity`: `"FulfillmentActivityTypeDef"`
- `parentIntentSignature`: `str`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`
- `checksum`: `str`
- `createVersion`: `bool`
- `kendraConfiguration`: `"KendraConfigurationTypeDef"`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`


## PutSlotTypeResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import PutSlotTypeResponseTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `enumerationValues`: `List["EnumerationValueTypeDef"]`
- `lastUpdatedDate`: `datetime`
- `createdDate`: `datetime`
- `version`: `str`
- `checksum`: `str`
- `valueSelectionStrategy`: `SlotValueSelectionStrategy`
- `createVersion`: `bool`
- `parentSlotTypeSignature`: `str`
- `slotTypeConfigurations`: `List["SlotTypeConfigurationTypeDef"]`


## StartImportResponseTypeDef

```python
from mypy_boto3_lex_models.type_defs import StartImportResponseTypeDef
```




Optional fields:
- `name`: `str`
- `resourceType`: `ResourceType`
- `mergeStrategy`: `MergeStrategy`
- `importId`: `str`
- `importStatus`: `ImportStatus`
- `tags`: `List["TagTypeDef"]`
- `createdDate`: `datetime`

