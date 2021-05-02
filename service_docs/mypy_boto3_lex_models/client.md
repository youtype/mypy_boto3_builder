# LexModelBuildingServiceClient for boto3 LexModelBuildingService module

> [Index](../index.md) > [LexModelBuildingService](./index.md) > LexModelBuildingServiceClient

Auto-generated documentation for [LexModelBuildingService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService)
type annotations stubs module [mypy_boto3_lex_models](https://pypi.org/project/mypy-boto3-lex-models/).

- [LexModelBuildingServiceClient for boto3 LexModelBuildingService module](#lexmodelbuildingserviceclient-for-boto3-lexmodelbuildingservice-module)
  - [LexModelBuildingServiceClient](#lexmodelbuildingserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_bot_version](#create_bot_version)
    - [create_intent_version](#create_intent_version)
    - [create_slot_type_version](#create_slot_type_version)
    - [delete_bot](#delete_bot)
    - [delete_bot_alias](#delete_bot_alias)
    - [delete_bot_channel_association](#delete_bot_channel_association)
    - [delete_bot_version](#delete_bot_version)
    - [delete_intent](#delete_intent)
    - [delete_intent_version](#delete_intent_version)
    - [delete_slot_type](#delete_slot_type)
    - [delete_slot_type_version](#delete_slot_type_version)
    - [delete_utterances](#delete_utterances)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_bot](#get_bot)
    - [get_bot_alias](#get_bot_alias)
    - [get_bot_aliases](#get_bot_aliases)
    - [get_bot_channel_association](#get_bot_channel_association)
    - [get_bot_channel_associations](#get_bot_channel_associations)
    - [get_bot_versions](#get_bot_versions)
    - [get_bots](#get_bots)
    - [get_builtin_intent](#get_builtin_intent)
    - [get_builtin_intents](#get_builtin_intents)
    - [get_builtin_slot_types](#get_builtin_slot_types)
    - [get_export](#get_export)
    - [get_import](#get_import)
    - [get_intent](#get_intent)
    - [get_intent_versions](#get_intent_versions)
    - [get_intents](#get_intents)
    - [get_slot_type](#get_slot_type)
    - [get_slot_type_versions](#get_slot_type_versions)
    - [get_slot_types](#get_slot_types)
    - [get_utterances_view](#get_utterances_view)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_bot](#put_bot)
    - [put_bot_alias](#put_bot_alias)
    - [put_intent](#put_intent)
    - [put_slot_type](#put_slot_type)
    - [start_import](#start_import)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)

## LexModelBuildingServiceClient

Type annotations for `boto3.client("lex-models")`

Can be used directly:

```python
from mypy_boto3_lex_models.client import LexModelBuildingServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lex_models.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalFailureException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.PreconditionFailedException`
- `Exceptions.ResourceInUseException`


## Methods


### can_paginate

Type annotations for `boto3.client("lex-models").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_bot_version

Type annotations for `boto3.client("lex-models").create_bot_version` method.

[Client.create_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.create_bot_version)

```python
def create_bot_version(
    self,
    name: str,
    checksum: str = None
) -> CreateBotVersionResponseTypeDef:
    pass
```

### create_intent_version

Type annotations for `boto3.client("lex-models").create_intent_version` method.

[Client.create_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.create_intent_version)

```python
def create_intent_version(
    self,
    name: str,
    checksum: str = None
) -> CreateIntentVersionResponseTypeDef:
    pass
```

### create_slot_type_version

Type annotations for `boto3.client("lex-models").create_slot_type_version` method.

[Client.create_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.create_slot_type_version)

```python
def create_slot_type_version(
    self,
    name: str,
    checksum: str = None
) -> CreateSlotTypeVersionResponseTypeDef:
    pass
```

### delete_bot

Type annotations for `boto3.client("lex-models").delete_bot` method.

[Client.delete_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot)

```python
def delete_bot(
    self,
    name: str
) -> None:
    pass
```

### delete_bot_alias

Type annotations for `boto3.client("lex-models").delete_bot_alias` method.

[Client.delete_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_alias)

```python
def delete_bot_alias(
    self,
    name: str,
    botName: str
) -> None:
    pass
```

### delete_bot_channel_association

Type annotations for `boto3.client("lex-models").delete_bot_channel_association` method.

[Client.delete_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_channel_association)

```python
def delete_bot_channel_association(
    self,
    name: str,
    botName: str,
    botAlias: str
) -> None:
    pass
```

### delete_bot_version

Type annotations for `boto3.client("lex-models").delete_bot_version` method.

[Client.delete_bot_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_version)

```python
def delete_bot_version(
    self,
    name: str,
    version: str
) -> None:
    pass
```

### delete_intent

Type annotations for `boto3.client("lex-models").delete_intent` method.

[Client.delete_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent)

```python
def delete_intent(
    self,
    name: str
) -> None:
    pass
```

### delete_intent_version

Type annotations for `boto3.client("lex-models").delete_intent_version` method.

[Client.delete_intent_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent_version)

```python
def delete_intent_version(
    self,
    name: str,
    version: str
) -> None:
    pass
```

### delete_slot_type

Type annotations for `boto3.client("lex-models").delete_slot_type` method.

[Client.delete_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type)

```python
def delete_slot_type(
    self,
    name: str
) -> None:
    pass
```

### delete_slot_type_version

Type annotations for `boto3.client("lex-models").delete_slot_type_version` method.

[Client.delete_slot_type_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type_version)

```python
def delete_slot_type_version(
    self,
    name: str,
    version: str
) -> None:
    pass
```

### delete_utterances

Type annotations for `boto3.client("lex-models").delete_utterances` method.

[Client.delete_utterances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.delete_utterances)

```python
def delete_utterances(
    self,
    botName: str,
    userId: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lex-models").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.generate_presigned_url)

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

### get_bot

Type annotations for `boto3.client("lex-models").get_bot` method.

[Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot)

```python
def get_bot(
    self,
    name: str,
    versionOrAlias: str
) -> GetBotResponseTypeDef:
    pass
```

### get_bot_alias

Type annotations for `boto3.client("lex-models").get_bot_alias` method.

[Client.get_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_alias)

```python
def get_bot_alias(
    self,
    name: str,
    botName: str
) -> GetBotAliasResponseTypeDef:
    pass
```

### get_bot_aliases

Type annotations for `boto3.client("lex-models").get_bot_aliases` method.

[Client.get_bot_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_aliases)

```python
def get_bot_aliases(
    self,
    botName: str,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None
) -> GetBotAliasesResponseTypeDef:
    pass
```

### get_bot_channel_association

Type annotations for `boto3.client("lex-models").get_bot_channel_association` method.

[Client.get_bot_channel_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_association)

```python
def get_bot_channel_association(
    self,
    name: str,
    botName: str,
    botAlias: str
) -> GetBotChannelAssociationResponseTypeDef:
    pass
```

### get_bot_channel_associations

Type annotations for `boto3.client("lex-models").get_bot_channel_associations` method.

[Client.get_bot_channel_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_associations)

```python
def get_bot_channel_associations(
    self,
    botName: str,
    botAlias: str,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None
) -> GetBotChannelAssociationsResponseTypeDef:
    pass
```

### get_bot_versions

Type annotations for `boto3.client("lex-models").get_bot_versions` method.

[Client.get_bot_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_versions)

```python
def get_bot_versions(
    self,
    name: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetBotVersionsResponseTypeDef:
    pass
```

### get_bots

Type annotations for `boto3.client("lex-models").get_bots` method.

[Client.get_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_bots)

```python
def get_bots(
    self,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None
) -> GetBotsResponseTypeDef:
    pass
```

### get_builtin_intent

Type annotations for `boto3.client("lex-models").get_builtin_intent` method.

[Client.get_builtin_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intent)

```python
def get_builtin_intent(
    self,
    signature: str
) -> GetBuiltinIntentResponseTypeDef:
    pass
```

### get_builtin_intents

Type annotations for `boto3.client("lex-models").get_builtin_intents` method.

[Client.get_builtin_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intents)

```python
def get_builtin_intents(
    self,
    locale: Locale = None,
    signatureContains: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetBuiltinIntentsResponseTypeDef:
    pass
```

### get_builtin_slot_types

Type annotations for `boto3.client("lex-models").get_builtin_slot_types` method.

[Client.get_builtin_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_slot_types)

```python
def get_builtin_slot_types(
    self,
    locale: Locale = None,
    signatureContains: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetBuiltinSlotTypesResponseTypeDef:
    pass
```

### get_export

Type annotations for `boto3.client("lex-models").get_export` method.

[Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_export)

```python
def get_export(
    self,
    name: str,
    version: str,
    resourceType: ResourceType,
    exportType: ExportType
) -> GetExportResponseTypeDef:
    pass
```

### get_import

Type annotations for `boto3.client("lex-models").get_import` method.

[Client.get_import documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_import)

```python
def get_import(
    self,
    importId: str
) -> GetImportResponseTypeDef:
    pass
```

### get_intent

Type annotations for `boto3.client("lex-models").get_intent` method.

[Client.get_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent)

```python
def get_intent(
    self,
    name: str,
    version: str
) -> GetIntentResponseTypeDef:
    pass
```

### get_intent_versions

Type annotations for `boto3.client("lex-models").get_intent_versions` method.

[Client.get_intent_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent_versions)

```python
def get_intent_versions(
    self,
    name: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetIntentVersionsResponseTypeDef:
    pass
```

### get_intents

Type annotations for `boto3.client("lex-models").get_intents` method.

[Client.get_intents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_intents)

```python
def get_intents(
    self,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None
) -> GetIntentsResponseTypeDef:
    pass
```

### get_slot_type

Type annotations for `boto3.client("lex-models").get_slot_type` method.

[Client.get_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type)

```python
def get_slot_type(
    self,
    name: str,
    version: str
) -> GetSlotTypeResponseTypeDef:
    pass
```

### get_slot_type_versions

Type annotations for `boto3.client("lex-models").get_slot_type_versions` method.

[Client.get_slot_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type_versions)

```python
def get_slot_type_versions(
    self,
    name: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetSlotTypeVersionsResponseTypeDef:
    pass
```

### get_slot_types

Type annotations for `boto3.client("lex-models").get_slot_types` method.

[Client.get_slot_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_types)

```python
def get_slot_types(
    self,
    nextToken: str = None,
    maxResults: int = None,
    nameContains: str = None
) -> GetSlotTypesResponseTypeDef:
    pass
```

### get_utterances_view

Type annotations for `boto3.client("lex-models").get_utterances_view` method.

[Client.get_utterances_view documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.get_utterances_view)

```python
def get_utterances_view(
    self,
    botName: str,
    botVersions: List[str],
    statusType: StatusType
) -> GetUtterancesViewResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("lex-models").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_bot

Type annotations for `boto3.client("lex-models").put_bot` method.

[Client.put_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot)

```python
def put_bot(
    self,
    name: str,
    locale: Locale,
    childDirected: bool,
    description: str = None,
    intents: List["IntentTypeDef"] = None,
    enableModelImprovements: bool = None,
    nluIntentConfidenceThreshold: float = None,
    clarificationPrompt: "PromptTypeDef" = None,
    abortStatement: "StatementTypeDef" = None,
    idleSessionTTLInSeconds: int = None,
    voiceId: str = None,
    checksum: str = None,
    processBehavior: ProcessBehavior = None,
    detectSentiment: bool = None,
    createVersion: bool = None,
    tags: List["TagTypeDef"] = None
) -> PutBotResponseTypeDef:
    pass
```

### put_bot_alias

Type annotations for `boto3.client("lex-models").put_bot_alias` method.

[Client.put_bot_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot_alias)

```python
def put_bot_alias(
    self,
    name: str,
    botVersion: str,
    botName: str,
    description: str = None,
    checksum: str = None,
    conversationLogs: ConversationLogsRequestTypeDef = None,
    tags: List["TagTypeDef"] = None
) -> PutBotAliasResponseTypeDef:
    pass
```

### put_intent

Type annotations for `boto3.client("lex-models").put_intent` method.

[Client.put_intent documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.put_intent)

```python
def put_intent(
    self,
    name: str,
    description: str = None,
    slots: List["SlotTypeDef"] = None,
    sampleUtterances: List[str] = None,
    confirmationPrompt: "PromptTypeDef" = None,
    rejectionStatement: "StatementTypeDef" = None,
    followUpPrompt: "FollowUpPromptTypeDef" = None,
    conclusionStatement: "StatementTypeDef" = None,
    dialogCodeHook: "CodeHookTypeDef" = None,
    fulfillmentActivity: "FulfillmentActivityTypeDef" = None,
    parentIntentSignature: str = None,
    checksum: str = None,
    createVersion: bool = None,
    kendraConfiguration: "KendraConfigurationTypeDef" = None,
    inputContexts: List["InputContextTypeDef"] = None,
    outputContexts: List["OutputContextTypeDef"] = None
) -> PutIntentResponseTypeDef:
    pass
```

### put_slot_type

Type annotations for `boto3.client("lex-models").put_slot_type` method.

[Client.put_slot_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.put_slot_type)

```python
def put_slot_type(
    self,
    name: str,
    description: str = None,
    enumerationValues: List["EnumerationValueTypeDef"] = None,
    checksum: str = None,
    valueSelectionStrategy: SlotValueSelectionStrategy = None,
    createVersion: bool = None,
    parentSlotTypeSignature: str = None,
    slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"] = None
) -> PutSlotTypeResponseTypeDef:
    pass
```

### start_import

Type annotations for `boto3.client("lex-models").start_import` method.

[Client.start_import documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.start_import)

```python
def start_import(
    self,
    payload: Union[bytes, IO[bytes]],
    resourceType: ResourceType,
    mergeStrategy: MergeStrategy,
    tags: List["TagTypeDef"] = None
) -> StartImportResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("lex-models").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("lex-models").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBotAliasesPaginatorName
) -> GetBotAliasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBotChannelAssociationsPaginatorName
) -> GetBotChannelAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBotVersionsPaginatorName
) -> GetBotVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBotsPaginatorName
) -> GetBotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBuiltinIntentsPaginatorName
) -> GetBuiltinIntentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBuiltinSlotTypesPaginatorName
) -> GetBuiltinSlotTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetIntentVersionsPaginatorName
) -> GetIntentVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)

```python
@overload
def get_paginator(
    self,
    operation_name: GetIntentsPaginatorName
) -> GetIntentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSlotTypeVersionsPaginatorName
) -> GetSlotTypeVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lex-models").get_paginator` method.

[Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSlotTypesPaginatorName
) -> GetSlotTypesPaginator:
    pass
```