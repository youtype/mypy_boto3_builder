# Structures for boto3 LexModelsV2 module

> [Index](../index.md) > [LexModelsV2](./index.md) > Structures

Auto-generated documentation for [LexModelsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2)
type annotations stubs module [mypy_boto3_lexv2_models](https://pypi.org/project/mypy-boto3-lexv2-models/).

- [Structures for boto3 LexModelsV2 module](#structures-for-boto3-lexmodelsv2-module)
  - [AudioLogDestinationTypeDef](#audiologdestinationtypedef)
  - [AudioLogSettingTypeDef](#audiologsettingtypedef)
  - [BotAliasHistoryEventTypeDef](#botaliashistoryeventtypedef)
  - [BotAliasLocaleSettingsTypeDef](#botaliaslocalesettingstypedef)
  - [BotAliasSummaryTypeDef](#botaliassummarytypedef)
  - [BotLocaleHistoryEventTypeDef](#botlocalehistoryeventtypedef)
  - [BotLocaleSummaryTypeDef](#botlocalesummarytypedef)
  - [BotSummaryTypeDef](#botsummarytypedef)
  - [BotVersionLocaleDetailsTypeDef](#botversionlocaledetailstypedef)
  - [BotVersionSummaryTypeDef](#botversionsummarytypedef)
  - [BuiltInIntentSummaryTypeDef](#builtinintentsummarytypedef)
  - [BuiltInSlotTypeSummaryTypeDef](#builtinslottypesummarytypedef)
  - [ButtonTypeDef](#buttontypedef)
  - [CloudWatchLogGroupLogDestinationTypeDef](#cloudwatchloggrouplogdestinationtypedef)
  - [CodeHookSpecificationTypeDef](#codehookspecificationtypedef)
  - [ConversationLogSettingsTypeDef](#conversationlogsettingstypedef)
  - [CustomPayloadTypeDef](#custompayloadtypedef)
  - [DataPrivacyTypeDef](#dataprivacytypedef)
  - [DialogCodeHookSettingsTypeDef](#dialogcodehooksettingstypedef)
  - [FulfillmentCodeHookSettingsTypeDef](#fulfillmentcodehooksettingstypedef)
  - [ImageResponseCardTypeDef](#imageresponsecardtypedef)
  - [InputContextTypeDef](#inputcontexttypedef)
  - [IntentClosingSettingTypeDef](#intentclosingsettingtypedef)
  - [IntentConfirmationSettingTypeDef](#intentconfirmationsettingtypedef)
  - [IntentSummaryTypeDef](#intentsummarytypedef)
  - [KendraConfigurationTypeDef](#kendraconfigurationtypedef)
  - [LambdaCodeHookTypeDef](#lambdacodehooktypedef)
  - [MessageGroupTypeDef](#messagegrouptypedef)
  - [MessageTypeDef](#messagetypedef)
  - [ObfuscationSettingTypeDef](#obfuscationsettingtypedef)
  - [OutputContextTypeDef](#outputcontexttypedef)
  - [PlainTextMessageTypeDef](#plaintextmessagetypedef)
  - [PromptSpecificationTypeDef](#promptspecificationtypedef)
  - [ResponseSpecificationTypeDef](#responsespecificationtypedef)
  - [S3BucketLogDestinationTypeDef](#s3bucketlogdestinationtypedef)
  - [SSMLMessageTypeDef](#ssmlmessagetypedef)
  - [SampleUtteranceTypeDef](#sampleutterancetypedef)
  - [SampleValueTypeDef](#samplevaluetypedef)
  - [SentimentAnalysisSettingsTypeDef](#sentimentanalysissettingstypedef)
  - [SlotDefaultValueSpecificationTypeDef](#slotdefaultvaluespecificationtypedef)
  - [SlotDefaultValueTypeDef](#slotdefaultvaluetypedef)
  - [SlotPriorityTypeDef](#slotprioritytypedef)
  - [SlotSummaryTypeDef](#slotsummarytypedef)
  - [SlotTypeSummaryTypeDef](#slottypesummarytypedef)
  - [SlotTypeValueTypeDef](#slottypevaluetypedef)
  - [SlotValueElicitationSettingTypeDef](#slotvalueelicitationsettingtypedef)
  - [SlotValueRegexFilterTypeDef](#slotvalueregexfiltertypedef)
  - [SlotValueSelectionSettingTypeDef](#slotvalueselectionsettingtypedef)
  - [StillWaitingResponseSpecificationTypeDef](#stillwaitingresponsespecificationtypedef)
  - [TextLogDestinationTypeDef](#textlogdestinationtypedef)
  - [TextLogSettingTypeDef](#textlogsettingtypedef)
  - [VoiceSettingsTypeDef](#voicesettingstypedef)
  - [WaitAndContinueSpecificationTypeDef](#waitandcontinuespecificationtypedef)
  - [BotFilterTypeDef](#botfiltertypedef)
  - [BotLocaleFilterTypeDef](#botlocalefiltertypedef)
  - [BotLocaleSortByTypeDef](#botlocalesortbytypedef)
  - [BotSortByTypeDef](#botsortbytypedef)
  - [BotVersionSortByTypeDef](#botversionsortbytypedef)
  - [BuildBotLocaleResponseTypeDef](#buildbotlocaleresponsetypedef)
  - [BuiltInIntentSortByTypeDef](#builtinintentsortbytypedef)
  - [BuiltInSlotTypeSortByTypeDef](#builtinslottypesortbytypedef)
  - [CreateBotAliasResponseTypeDef](#createbotaliasresponsetypedef)
  - [CreateBotLocaleResponseTypeDef](#createbotlocaleresponsetypedef)
  - [CreateBotResponseTypeDef](#createbotresponsetypedef)
  - [CreateBotVersionResponseTypeDef](#createbotversionresponsetypedef)
  - [CreateIntentResponseTypeDef](#createintentresponsetypedef)
  - [CreateSlotResponseTypeDef](#createslotresponsetypedef)
  - [CreateSlotTypeResponseTypeDef](#createslottyperesponsetypedef)
  - [DeleteBotAliasResponseTypeDef](#deletebotaliasresponsetypedef)
  - [DeleteBotLocaleResponseTypeDef](#deletebotlocaleresponsetypedef)
  - [DeleteBotResponseTypeDef](#deletebotresponsetypedef)
  - [DeleteBotVersionResponseTypeDef](#deletebotversionresponsetypedef)
  - [DescribeBotAliasResponseTypeDef](#describebotaliasresponsetypedef)
  - [DescribeBotLocaleResponseTypeDef](#describebotlocaleresponsetypedef)
  - [DescribeBotResponseTypeDef](#describebotresponsetypedef)
  - [DescribeBotVersionResponseTypeDef](#describebotversionresponsetypedef)
  - [DescribeIntentResponseTypeDef](#describeintentresponsetypedef)
  - [DescribeSlotResponseTypeDef](#describeslotresponsetypedef)
  - [DescribeSlotTypeResponseTypeDef](#describeslottyperesponsetypedef)
  - [IntentFilterTypeDef](#intentfiltertypedef)
  - [IntentSortByTypeDef](#intentsortbytypedef)
  - [ListBotAliasesResponseTypeDef](#listbotaliasesresponsetypedef)
  - [ListBotLocalesResponseTypeDef](#listbotlocalesresponsetypedef)
  - [ListBotVersionsResponseTypeDef](#listbotversionsresponsetypedef)
  - [ListBotsResponseTypeDef](#listbotsresponsetypedef)
  - [ListBuiltInIntentsResponseTypeDef](#listbuiltinintentsresponsetypedef)
  - [ListBuiltInSlotTypesResponseTypeDef](#listbuiltinslottypesresponsetypedef)
  - [ListIntentsResponseTypeDef](#listintentsresponsetypedef)
  - [ListSlotTypesResponseTypeDef](#listslottypesresponsetypedef)
  - [ListSlotsResponseTypeDef](#listslotsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [SlotFilterTypeDef](#slotfiltertypedef)
  - [SlotSortByTypeDef](#slotsortbytypedef)
  - [SlotTypeFilterTypeDef](#slottypefiltertypedef)
  - [SlotTypeSortByTypeDef](#slottypesortbytypedef)
  - [UpdateBotAliasResponseTypeDef](#updatebotaliasresponsetypedef)
  - [UpdateBotLocaleResponseTypeDef](#updatebotlocaleresponsetypedef)
  - [UpdateBotResponseTypeDef](#updatebotresponsetypedef)
  - [UpdateIntentResponseTypeDef](#updateintentresponsetypedef)
  - [UpdateSlotResponseTypeDef](#updateslotresponsetypedef)
  - [UpdateSlotTypeResponseTypeDef](#updateslottyperesponsetypedef)

## AudioLogDestinationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import AudioLogDestinationTypeDef
```


Required fields:
- `s3Bucket`: `"S3BucketLogDestinationTypeDef"`




## AudioLogSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import AudioLogSettingTypeDef
```


Required fields:
- `enabled`: `bool`
- `destination`: `"AudioLogDestinationTypeDef"`




## BotAliasHistoryEventTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotAliasHistoryEventTypeDef
```




Optional fields:
- `botVersion`: `str`
- `startDate`: `datetime`
- `endDate`: `datetime`


## BotAliasLocaleSettingsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotAliasLocaleSettingsTypeDef
```


Required fields:
- `enabled`: `bool`



Optional fields:
- `codeHookSpecification`: `"CodeHookSpecificationTypeDef"`


## BotAliasSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotAliasSummaryTypeDef
```




Optional fields:
- `botAliasId`: `str`
- `botAliasName`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botAliasStatus`: `BotAliasStatus`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## BotLocaleHistoryEventTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotLocaleHistoryEventTypeDef
```


Required fields:
- `event`: `str`
- `eventDate`: `datetime`




## BotLocaleSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotLocaleSummaryTypeDef
```




Optional fields:
- `localeId`: `str`
- `localeName`: `str`
- `description`: `str`
- `botLocaleStatus`: `BotLocaleStatus`
- `lastUpdatedDateTime`: `datetime`
- `lastBuildSubmittedDateTime`: `datetime`


## BotSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotSummaryTypeDef
```




Optional fields:
- `botId`: `str`
- `botName`: `str`
- `description`: `str`
- `botStatus`: `BotStatus`
- `latestBotVersion`: `str`
- `lastUpdatedDateTime`: `datetime`


## BotVersionLocaleDetailsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotVersionLocaleDetailsTypeDef
```


Required fields:
- `sourceBotVersion`: `str`




## BotVersionSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotVersionSummaryTypeDef
```




Optional fields:
- `botName`: `str`
- `botVersion`: `str`
- `description`: `str`
- `botStatus`: `BotStatus`
- `creationDateTime`: `datetime`


## BuiltInIntentSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BuiltInIntentSummaryTypeDef
```




Optional fields:
- `intentSignature`: `str`
- `description`: `str`


## BuiltInSlotTypeSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BuiltInSlotTypeSummaryTypeDef
```




Optional fields:
- `slotTypeSignature`: `str`
- `description`: `str`


## ButtonTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ButtonTypeDef
```


Required fields:
- `text`: `str`
- `value`: `str`




## CloudWatchLogGroupLogDestinationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CloudWatchLogGroupLogDestinationTypeDef
```


Required fields:
- `cloudWatchLogGroupArn`: `str`
- `logPrefix`: `str`




## CodeHookSpecificationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CodeHookSpecificationTypeDef
```


Required fields:
- `lambdaCodeHook`: `"LambdaCodeHookTypeDef"`




## ConversationLogSettingsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ConversationLogSettingsTypeDef
```




Optional fields:
- `textLogSettings`: `List["TextLogSettingTypeDef"]`
- `audioLogSettings`: `List["AudioLogSettingTypeDef"]`


## CustomPayloadTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CustomPayloadTypeDef
```


Required fields:
- `value`: `str`




## DataPrivacyTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DataPrivacyTypeDef
```


Required fields:
- `childDirected`: `bool`




## DialogCodeHookSettingsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DialogCodeHookSettingsTypeDef
```


Required fields:
- `enabled`: `bool`




## FulfillmentCodeHookSettingsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import FulfillmentCodeHookSettingsTypeDef
```


Required fields:
- `enabled`: `bool`




## ImageResponseCardTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ImageResponseCardTypeDef
```


Required fields:
- `title`: `str`



Optional fields:
- `subtitle`: `str`
- `imageUrl`: `str`
- `buttons`: `List["ButtonTypeDef"]`


## InputContextTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import InputContextTypeDef
```


Required fields:
- `name`: `str`




## IntentClosingSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import IntentClosingSettingTypeDef
```


Required fields:
- `closingResponse`: `"ResponseSpecificationTypeDef"`




## IntentConfirmationSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import IntentConfirmationSettingTypeDef
```


Required fields:
- `promptSpecification`: `"PromptSpecificationTypeDef"`
- `declinationResponse`: `"ResponseSpecificationTypeDef"`




## IntentSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import IntentSummaryTypeDef
```




Optional fields:
- `intentId`: `str`
- `intentName`: `str`
- `description`: `str`
- `parentIntentSignature`: `str`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`
- `lastUpdatedDateTime`: `datetime`


## KendraConfigurationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import KendraConfigurationTypeDef
```


Required fields:
- `kendraIndex`: `str`



Optional fields:
- `queryFilterStringEnabled`: `bool`
- `queryFilterString`: `str`


## LambdaCodeHookTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import LambdaCodeHookTypeDef
```


Required fields:
- `lambdaARN`: `str`
- `codeHookInterfaceVersion`: `str`




## MessageGroupTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import MessageGroupTypeDef
```


Required fields:
- `message`: `"MessageTypeDef"`



Optional fields:
- `variations`: `List["MessageTypeDef"]`


## MessageTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import MessageTypeDef
```




Optional fields:
- `plainTextMessage`: `"PlainTextMessageTypeDef"`
- `customPayload`: `"CustomPayloadTypeDef"`
- `ssmlMessage`: `"SSMLMessageTypeDef"`
- `imageResponseCard`: `"ImageResponseCardTypeDef"`


## ObfuscationSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ObfuscationSettingTypeDef
```


Required fields:
- `obfuscationSettingType`: `ObfuscationSettingType`




## OutputContextTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import OutputContextTypeDef
```


Required fields:
- `name`: `str`
- `timeToLiveInSeconds`: `int`
- `turnsToLive`: `int`




## PlainTextMessageTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import PlainTextMessageTypeDef
```


Required fields:
- `value`: `str`




## PromptSpecificationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import PromptSpecificationTypeDef
```


Required fields:
- `messageGroups`: `List["MessageGroupTypeDef"]`
- `maxRetries`: `int`



Optional fields:
- `allowInterrupt`: `bool`


## ResponseSpecificationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ResponseSpecificationTypeDef
```


Required fields:
- `messageGroups`: `List["MessageGroupTypeDef"]`



Optional fields:
- `allowInterrupt`: `bool`


## S3BucketLogDestinationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import S3BucketLogDestinationTypeDef
```


Required fields:
- `s3BucketArn`: `str`
- `logPrefix`: `str`



Optional fields:
- `kmsKeyArn`: `str`


## SSMLMessageTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SSMLMessageTypeDef
```


Required fields:
- `value`: `str`




## SampleUtteranceTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SampleUtteranceTypeDef
```


Required fields:
- `utterance`: `str`




## SampleValueTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SampleValueTypeDef
```


Required fields:
- `value`: `str`




## SentimentAnalysisSettingsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SentimentAnalysisSettingsTypeDef
```


Required fields:
- `detectSentiment`: `bool`




## SlotDefaultValueSpecificationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotDefaultValueSpecificationTypeDef
```


Required fields:
- `defaultValueList`: `List["SlotDefaultValueTypeDef"]`




## SlotDefaultValueTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotDefaultValueTypeDef
```


Required fields:
- `defaultValue`: `str`




## SlotPriorityTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotPriorityTypeDef
```


Required fields:
- `priority`: `int`
- `slotId`: `str`




## SlotSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotSummaryTypeDef
```




Optional fields:
- `slotId`: `str`
- `slotName`: `str`
- `description`: `str`
- `slotConstraint`: `SlotConstraint`
- `slotTypeId`: `str`
- `valueElicitationPromptSpecification`: `"PromptSpecificationTypeDef"`
- `lastUpdatedDateTime`: `datetime`


## SlotTypeSummaryTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotTypeSummaryTypeDef
```




Optional fields:
- `slotTypeId`: `str`
- `slotTypeName`: `str`
- `description`: `str`
- `parentSlotTypeSignature`: `str`
- `lastUpdatedDateTime`: `datetime`


## SlotTypeValueTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotTypeValueTypeDef
```




Optional fields:
- `sampleValue`: `"SampleValueTypeDef"`
- `synonyms`: `List["SampleValueTypeDef"]`


## SlotValueElicitationSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotValueElicitationSettingTypeDef
```


Required fields:
- `slotConstraint`: `SlotConstraint`



Optional fields:
- `defaultValueSpecification`: `"SlotDefaultValueSpecificationTypeDef"`
- `promptSpecification`: `"PromptSpecificationTypeDef"`
- `sampleUtterances`: `List["SampleUtteranceTypeDef"]`
- `waitAndContinueSpecification`: `"WaitAndContinueSpecificationTypeDef"`


## SlotValueRegexFilterTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotValueRegexFilterTypeDef
```


Required fields:
- `pattern`: `str`




## SlotValueSelectionSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotValueSelectionSettingTypeDef
```


Required fields:
- `resolutionStrategy`: `SlotValueResolutionStrategy`



Optional fields:
- `regexFilter`: `"SlotValueRegexFilterTypeDef"`


## StillWaitingResponseSpecificationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import StillWaitingResponseSpecificationTypeDef
```


Required fields:
- `messageGroups`: `List["MessageGroupTypeDef"]`
- `frequencyInSeconds`: `int`
- `timeoutInSeconds`: `int`



Optional fields:
- `allowInterrupt`: `bool`


## TextLogDestinationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import TextLogDestinationTypeDef
```


Required fields:
- `cloudWatch`: `"CloudWatchLogGroupLogDestinationTypeDef"`




## TextLogSettingTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import TextLogSettingTypeDef
```


Required fields:
- `enabled`: `bool`
- `destination`: `"TextLogDestinationTypeDef"`




## VoiceSettingsTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import VoiceSettingsTypeDef
```


Required fields:
- `voiceId`: `str`




## WaitAndContinueSpecificationTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import WaitAndContinueSpecificationTypeDef
```


Required fields:
- `waitingResponse`: `"ResponseSpecificationTypeDef"`
- `continueResponse`: `"ResponseSpecificationTypeDef"`



Optional fields:
- `stillWaitingResponse`: `"StillWaitingResponseSpecificationTypeDef"`


## BotFilterTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotFilterTypeDef
```


Required fields:
- `name`: `BotFilterName`
- `values`: `List[str]`
- `operator`: `BotFilterOperator`




## BotLocaleFilterTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotLocaleFilterTypeDef
```


Required fields:
- `name`: `BotLocaleFilterName`
- `values`: `List[str]`
- `operator`: `BotLocaleFilterOperator`




## BotLocaleSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotLocaleSortByTypeDef
```


Required fields:
- `attribute`: `BotLocaleSortAttribute`
- `order`: `SortOrder`




## BotSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotSortByTypeDef
```


Required fields:
- `attribute`: `BotSortAttribute`
- `order`: `SortOrder`




## BotVersionSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BotVersionSortByTypeDef
```


Required fields:
- `attribute`: `BotVersionSortAttribute`
- `order`: `SortOrder`




## BuildBotLocaleResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BuildBotLocaleResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `botLocaleStatus`: `BotLocaleStatus`
- `lastBuildSubmittedDateTime`: `datetime`


## BuiltInIntentSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BuiltInIntentSortByTypeDef
```


Required fields:
- `attribute`: `BuiltInIntentSortAttribute`
- `order`: `SortOrder`




## BuiltInSlotTypeSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import BuiltInSlotTypeSortByTypeDef
```


Required fields:
- `attribute`: `BuiltInSlotTypeSortAttribute`
- `order`: `SortOrder`




## CreateBotAliasResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateBotAliasResponseTypeDef
```




Optional fields:
- `botAliasId`: `str`
- `botAliasName`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botAliasLocaleSettings`: `Dict[str, "BotAliasLocaleSettingsTypeDef"]`
- `conversationLogSettings`: `"ConversationLogSettingsTypeDef"`
- `sentimentAnalysisSettings`: `"SentimentAnalysisSettingsTypeDef"`
- `botAliasStatus`: `BotAliasStatus`
- `botId`: `str`
- `creationDateTime`: `datetime`
- `tags`: `Dict[str, str]`


## CreateBotLocaleResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateBotLocaleResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeName`: `str`
- `localeId`: `str`
- `description`: `str`
- `nluIntentConfidenceThreshold`: `float`
- `voiceSettings`: `"VoiceSettingsTypeDef"`
- `botLocaleStatus`: `BotLocaleStatus`
- `creationDateTime`: `datetime`


## CreateBotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateBotResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botName`: `str`
- `description`: `str`
- `roleArn`: `str`
- `dataPrivacy`: `"DataPrivacyTypeDef"`
- `idleSessionTTLInSeconds`: `int`
- `botStatus`: `BotStatus`
- `creationDateTime`: `datetime`
- `botTags`: `Dict[str, str]`
- `testBotAliasTags`: `Dict[str, str]`


## CreateBotVersionResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateBotVersionResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botVersionLocaleSpecification`: `Dict[str, "BotVersionLocaleDetailsTypeDef"]`
- `botStatus`: `BotStatus`
- `creationDateTime`: `datetime`


## CreateIntentResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateIntentResponseTypeDef
```




Optional fields:
- `intentId`: `str`
- `intentName`: `str`
- `description`: `str`
- `parentIntentSignature`: `str`
- `sampleUtterances`: `List["SampleUtteranceTypeDef"]`
- `dialogCodeHook`: `"DialogCodeHookSettingsTypeDef"`
- `fulfillmentCodeHook`: `"FulfillmentCodeHookSettingsTypeDef"`
- `intentConfirmationSetting`: `"IntentConfirmationSettingTypeDef"`
- `intentClosingSetting`: `"IntentClosingSettingTypeDef"`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`
- `kendraConfiguration`: `"KendraConfigurationTypeDef"`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `creationDateTime`: `datetime`


## CreateSlotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateSlotResponseTypeDef
```




Optional fields:
- `slotId`: `str`
- `slotName`: `str`
- `description`: `str`
- `slotTypeId`: `str`
- `valueElicitationSetting`: `"SlotValueElicitationSettingTypeDef"`
- `obfuscationSetting`: `"ObfuscationSettingTypeDef"`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `intentId`: `str`
- `creationDateTime`: `datetime`


## CreateSlotTypeResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import CreateSlotTypeResponseTypeDef
```




Optional fields:
- `slotTypeId`: `str`
- `slotTypeName`: `str`
- `description`: `str`
- `slotTypeValues`: `List["SlotTypeValueTypeDef"]`
- `valueSelectionSetting`: `"SlotValueSelectionSettingTypeDef"`
- `parentSlotTypeSignature`: `str`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `creationDateTime`: `datetime`


## DeleteBotAliasResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DeleteBotAliasResponseTypeDef
```




Optional fields:
- `botAliasId`: `str`
- `botId`: `str`
- `botAliasStatus`: `BotAliasStatus`


## DeleteBotLocaleResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DeleteBotLocaleResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `botLocaleStatus`: `BotLocaleStatus`


## DeleteBotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DeleteBotResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botStatus`: `BotStatus`


## DeleteBotVersionResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DeleteBotVersionResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `botStatus`: `BotStatus`


## DescribeBotAliasResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeBotAliasResponseTypeDef
```




Optional fields:
- `botAliasId`: `str`
- `botAliasName`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botAliasLocaleSettings`: `Dict[str, "BotAliasLocaleSettingsTypeDef"]`
- `conversationLogSettings`: `"ConversationLogSettingsTypeDef"`
- `sentimentAnalysisSettings`: `"SentimentAnalysisSettingsTypeDef"`
- `botAliasHistoryEvents`: `List["BotAliasHistoryEventTypeDef"]`
- `botAliasStatus`: `BotAliasStatus`
- `botId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## DescribeBotLocaleResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeBotLocaleResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `localeName`: `str`
- `description`: `str`
- `nluIntentConfidenceThreshold`: `float`
- `voiceSettings`: `"VoiceSettingsTypeDef"`
- `intentsCount`: `int`
- `slotTypesCount`: `int`
- `botLocaleStatus`: `BotLocaleStatus`
- `failureReasons`: `List[str]`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`
- `lastBuildSubmittedDateTime`: `datetime`
- `botLocaleHistoryEvents`: `List["BotLocaleHistoryEventTypeDef"]`


## DescribeBotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeBotResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botName`: `str`
- `description`: `str`
- `roleArn`: `str`
- `dataPrivacy`: `"DataPrivacyTypeDef"`
- `idleSessionTTLInSeconds`: `int`
- `botStatus`: `BotStatus`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## DescribeBotVersionResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeBotVersionResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botName`: `str`
- `botVersion`: `str`
- `description`: `str`
- `roleArn`: `str`
- `dataPrivacy`: `"DataPrivacyTypeDef"`
- `idleSessionTTLInSeconds`: `int`
- `botStatus`: `BotStatus`
- `failureReasons`: `List[str]`
- `creationDateTime`: `datetime`


## DescribeIntentResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeIntentResponseTypeDef
```




Optional fields:
- `intentId`: `str`
- `intentName`: `str`
- `description`: `str`
- `parentIntentSignature`: `str`
- `sampleUtterances`: `List["SampleUtteranceTypeDef"]`
- `dialogCodeHook`: `"DialogCodeHookSettingsTypeDef"`
- `fulfillmentCodeHook`: `"FulfillmentCodeHookSettingsTypeDef"`
- `slotPriorities`: `List["SlotPriorityTypeDef"]`
- `intentConfirmationSetting`: `"IntentConfirmationSettingTypeDef"`
- `intentClosingSetting`: `"IntentClosingSettingTypeDef"`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`
- `kendraConfiguration`: `"KendraConfigurationTypeDef"`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## DescribeSlotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeSlotResponseTypeDef
```




Optional fields:
- `slotId`: `str`
- `slotName`: `str`
- `description`: `str`
- `slotTypeId`: `str`
- `valueElicitationSetting`: `"SlotValueElicitationSettingTypeDef"`
- `obfuscationSetting`: `"ObfuscationSettingTypeDef"`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `intentId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## DescribeSlotTypeResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import DescribeSlotTypeResponseTypeDef
```




Optional fields:
- `slotTypeId`: `str`
- `slotTypeName`: `str`
- `description`: `str`
- `slotTypeValues`: `List["SlotTypeValueTypeDef"]`
- `valueSelectionSetting`: `"SlotValueSelectionSettingTypeDef"`
- `parentSlotTypeSignature`: `str`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## IntentFilterTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import IntentFilterTypeDef
```


Required fields:
- `name`: `IntentFilterName`
- `values`: `List[str]`
- `operator`: `IntentFilterOperator`




## IntentSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import IntentSortByTypeDef
```


Required fields:
- `attribute`: `IntentSortAttribute`
- `order`: `SortOrder`




## ListBotAliasesResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListBotAliasesResponseTypeDef
```




Optional fields:
- `botAliasSummaries`: `List["BotAliasSummaryTypeDef"]`
- `nextToken`: `str`
- `botId`: `str`


## ListBotLocalesResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListBotLocalesResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `nextToken`: `str`
- `botLocaleSummaries`: `List["BotLocaleSummaryTypeDef"]`


## ListBotVersionsResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListBotVersionsResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersionSummaries`: `List["BotVersionSummaryTypeDef"]`
- `nextToken`: `str`


## ListBotsResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListBotsResponseTypeDef
```




Optional fields:
- `botSummaries`: `List["BotSummaryTypeDef"]`
- `nextToken`: `str`


## ListBuiltInIntentsResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListBuiltInIntentsResponseTypeDef
```




Optional fields:
- `builtInIntentSummaries`: `List["BuiltInIntentSummaryTypeDef"]`
- `nextToken`: `str`
- `localeId`: `str`


## ListBuiltInSlotTypesResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListBuiltInSlotTypesResponseTypeDef
```




Optional fields:
- `builtInSlotTypeSummaries`: `List["BuiltInSlotTypeSummaryTypeDef"]`
- `nextToken`: `str`
- `localeId`: `str`


## ListIntentsResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListIntentsResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `intentSummaries`: `List["IntentSummaryTypeDef"]`
- `nextToken`: `str`


## ListSlotTypesResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListSlotTypesResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `slotTypeSummaries`: `List["SlotTypeSummaryTypeDef"]`
- `nextToken`: `str`


## ListSlotsResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListSlotsResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `intentId`: `str`
- `slotSummaries`: `List["SlotSummaryTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## SlotFilterTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotFilterTypeDef
```


Required fields:
- `name`: `SlotFilterName`
- `values`: `List[str]`
- `operator`: `SlotFilterOperator`




## SlotSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotSortByTypeDef
```


Required fields:
- `attribute`: `SlotSortAttribute`
- `order`: `SortOrder`




## SlotTypeFilterTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotTypeFilterTypeDef
```


Required fields:
- `name`: `SlotTypeFilterName`
- `values`: `List[str]`
- `operator`: `SlotTypeFilterOperator`




## SlotTypeSortByTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import SlotTypeSortByTypeDef
```


Required fields:
- `attribute`: `SlotTypeSortAttribute`
- `order`: `SortOrder`




## UpdateBotAliasResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import UpdateBotAliasResponseTypeDef
```




Optional fields:
- `botAliasId`: `str`
- `botAliasName`: `str`
- `description`: `str`
- `botVersion`: `str`
- `botAliasLocaleSettings`: `Dict[str, "BotAliasLocaleSettingsTypeDef"]`
- `conversationLogSettings`: `"ConversationLogSettingsTypeDef"`
- `sentimentAnalysisSettings`: `"SentimentAnalysisSettingsTypeDef"`
- `botAliasStatus`: `BotAliasStatus`
- `botId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## UpdateBotLocaleResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import UpdateBotLocaleResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `localeName`: `str`
- `description`: `str`
- `nluIntentConfidenceThreshold`: `float`
- `voiceSettings`: `"VoiceSettingsTypeDef"`
- `botLocaleStatus`: `BotLocaleStatus`
- `failureReasons`: `List[str]`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## UpdateBotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import UpdateBotResponseTypeDef
```




Optional fields:
- `botId`: `str`
- `botName`: `str`
- `description`: `str`
- `roleArn`: `str`
- `dataPrivacy`: `"DataPrivacyTypeDef"`
- `idleSessionTTLInSeconds`: `int`
- `botStatus`: `BotStatus`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## UpdateIntentResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import UpdateIntentResponseTypeDef
```




Optional fields:
- `intentId`: `str`
- `intentName`: `str`
- `description`: `str`
- `parentIntentSignature`: `str`
- `sampleUtterances`: `List["SampleUtteranceTypeDef"]`
- `dialogCodeHook`: `"DialogCodeHookSettingsTypeDef"`
- `fulfillmentCodeHook`: `"FulfillmentCodeHookSettingsTypeDef"`
- `slotPriorities`: `List["SlotPriorityTypeDef"]`
- `intentConfirmationSetting`: `"IntentConfirmationSettingTypeDef"`
- `intentClosingSetting`: `"IntentClosingSettingTypeDef"`
- `inputContexts`: `List["InputContextTypeDef"]`
- `outputContexts`: `List["OutputContextTypeDef"]`
- `kendraConfiguration`: `"KendraConfigurationTypeDef"`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## UpdateSlotResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import UpdateSlotResponseTypeDef
```




Optional fields:
- `slotId`: `str`
- `slotName`: `str`
- `description`: `str`
- `slotTypeId`: `str`
- `valueElicitationSetting`: `"SlotValueElicitationSettingTypeDef"`
- `obfuscationSetting`: `"ObfuscationSettingTypeDef"`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `intentId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`


## UpdateSlotTypeResponseTypeDef

```python
from mypy_boto3_lexv2_models.type_defs import UpdateSlotTypeResponseTypeDef
```




Optional fields:
- `slotTypeId`: `str`
- `slotTypeName`: `str`
- `description`: `str`
- `slotTypeValues`: `List["SlotTypeValueTypeDef"]`
- `valueSelectionSetting`: `"SlotValueSelectionSettingTypeDef"`
- `parentSlotTypeSignature`: `str`
- `botId`: `str`
- `botVersion`: `str`
- `localeId`: `str`
- `creationDateTime`: `datetime`
- `lastUpdatedDateTime`: `datetime`

