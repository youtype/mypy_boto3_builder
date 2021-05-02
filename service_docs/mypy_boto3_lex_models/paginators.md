# Paginators for boto3 LexModelBuildingService module

> [Index](../index.md) > [LexModelBuildingService](./index.md) > Paginators

Auto-generated documentation for [LexModelBuildingService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService)
type annotations stubs module [mypy_boto3_lex_models](https://pypi.org/project/mypy-boto3-lex-models/).

- [Paginators for boto3 LexModelBuildingService module](#paginators-for-boto3-lexmodelbuildingservice-module)
  - [GetBotAliasesPaginator](#getbotaliasespaginator)
  - [GetBotChannelAssociationsPaginator](#getbotchannelassociationspaginator)
  - [GetBotVersionsPaginator](#getbotversionspaginator)
  - [GetBotsPaginator](#getbotspaginator)
  - [GetBuiltinIntentsPaginator](#getbuiltinintentspaginator)
  - [GetBuiltinSlotTypesPaginator](#getbuiltinslottypespaginator)
  - [GetIntentVersionsPaginator](#getintentversionspaginator)
  - [GetIntentsPaginator](#getintentspaginator)
  - [GetSlotTypeVersionsPaginator](#getslottypeversionspaginator)
  - [GetSlotTypesPaginator](#getslottypespaginator)

## GetBotAliasesPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_bot_aliases")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBotAliasesPaginator

def get_get_bot_aliases_paginator() -> GetBotAliasesPaginator:
    return boto3.client("lex-models").get_paginator("get_bot_aliases")
```

[Paginator.GetBotAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)

```python
class GetBotAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        botName: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotAliasesResponseTypeDef]:
        pass
```
## GetBotChannelAssociationsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_bot_channel_associations")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBotChannelAssociationsPaginator

def get_get_bot_channel_associations_paginator() -> GetBotChannelAssociationsPaginator:
    return boto3.client("lex-models").get_paginator("get_bot_channel_associations")
```

[Paginator.GetBotChannelAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)

```python
class GetBotChannelAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotChannelAssociationsResponseTypeDef]:
        pass
```
## GetBotVersionsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_bot_versions")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBotVersionsPaginator

def get_get_bot_versions_paginator() -> GetBotVersionsPaginator:
    return boto3.client("lex-models").get_paginator("get_bot_versions")
```

[Paginator.GetBotVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)

```python
class GetBotVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotVersionsResponseTypeDef]:
        pass
```
## GetBotsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_bots")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBotsPaginator

def get_get_bots_paginator() -> GetBotsPaginator:
    return boto3.client("lex-models").get_paginator("get_bots")
```

[Paginator.GetBots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)

```python
class GetBotsPaginator(Boto3Paginator):
    def paginate(
        self,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBotsResponseTypeDef]:
        pass
```
## GetBuiltinIntentsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_builtin_intents")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBuiltinIntentsPaginator

def get_get_builtin_intents_paginator() -> GetBuiltinIntentsPaginator:
    return boto3.client("lex-models").get_paginator("get_builtin_intents")
```

[Paginator.GetBuiltinIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)

```python
class GetBuiltinIntentsPaginator(Boto3Paginator):
    def paginate(
        self,
        locale: Locale = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBuiltinIntentsResponseTypeDef]:
        pass
```
## GetBuiltinSlotTypesPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_builtin_slot_types")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetBuiltinSlotTypesPaginator

def get_get_builtin_slot_types_paginator() -> GetBuiltinSlotTypesPaginator:
    return boto3.client("lex-models").get_paginator("get_builtin_slot_types")
```

[Paginator.GetBuiltinSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)

```python
class GetBuiltinSlotTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        locale: Locale = None,
        signatureContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBuiltinSlotTypesResponseTypeDef]:
        pass
```
## GetIntentVersionsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_intent_versions")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetIntentVersionsPaginator

def get_get_intent_versions_paginator() -> GetIntentVersionsPaginator:
    return boto3.client("lex-models").get_paginator("get_intent_versions")
```

[Paginator.GetIntentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)

```python
class GetIntentVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntentVersionsResponseTypeDef]:
        pass
```
## GetIntentsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_intents")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetIntentsPaginator

def get_get_intents_paginator() -> GetIntentsPaginator:
    return boto3.client("lex-models").get_paginator("get_intents")
```

[Paginator.GetIntents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)

```python
class GetIntentsPaginator(Boto3Paginator):
    def paginate(
        self,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntentsResponseTypeDef]:
        pass
```
## GetSlotTypeVersionsPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_slot_type_versions")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetSlotTypeVersionsPaginator

def get_get_slot_type_versions_paginator() -> GetSlotTypeVersionsPaginator:
    return boto3.client("lex-models").get_paginator("get_slot_type_versions")
```

[Paginator.GetSlotTypeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)

```python
class GetSlotTypeVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSlotTypeVersionsResponseTypeDef]:
        pass
```
## GetSlotTypesPaginator

Type annotations for `boto3.client("lex-models").get_paginator("get_slot_types")`.

Can be used directly:

```python
from mypy_boto3_lex_models.paginators import GetSlotTypesPaginator

def get_get_slot_types_paginator() -> GetSlotTypesPaginator:
    return boto3.client("lex-models").get_paginator("get_slot_types")
```

[Paginator.GetSlotTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)

```python
class GetSlotTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        nameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSlotTypesResponseTypeDef]:
        pass
```