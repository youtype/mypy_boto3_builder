# Type annotations for boto3 LexRuntimeV2 module

> [Index](../index.md) > LexRuntimeV2

Auto-generated documentation for [LexRuntimeV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2)
type annotations stubs module [mypy_boto3_lexv2_runtime](https://pypi.org/project/mypy-boto3-lexv2-runtime/).

```bash
pip install mypy-boto3-lexv2-runtime
```

- [Type annotations for boto3 LexRuntimeV2 module](#type-annotations-for-boto3-lexruntimev2-module)
  - [LexRuntimeV2Client](#lexruntimev2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## LexRuntimeV2Client

Type annotations for  `boto3.client("lexv2-runtime")` as [LexRuntimeV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_lexv2_runtime.client import LexRuntimeV2Client
```


LexRuntimeV2Client [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_session](./client.md#delete-session)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_session](./client.md#get-session)
- [put_session](./client.md#put-session)
- [recognize_text](./client.md#recognize-text)
- [recognize_utterance](./client.md#recognize-utterance)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BadGatewayException](./client.md#badgatewayexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [DependencyFailedException](./client.md#dependencyfailedexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lexv2_runtime.literals import ConfirmationState, ...
```

- [ConfirmationState](./literals.md#confirmationstate)
- [DialogActionType](./literals.md#dialogactiontype)
- [IntentState](./literals.md#intentstate)
- [MessageContentType](./literals.md#messagecontenttype)
- [SentimentType](./literals.md#sentimenttype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lexv2_runtime.type_defs import ActiveContextTimeToLiveTypeDef, ...
```

- [ActiveContextTimeToLiveTypeDef](./type_defs.md#activecontexttimetolivetypedef)
- [ActiveContextTypeDef](./type_defs.md#activecontexttypedef)
- [ButtonTypeDef](./type_defs.md#buttontypedef)
- [ConfidenceScoreTypeDef](./type_defs.md#confidencescoretypedef)
- [DialogActionTypeDef](./type_defs.md#dialogactiontypedef)
- [ImageResponseCardTypeDef](./type_defs.md#imageresponsecardtypedef)
- [IntentTypeDef](./type_defs.md#intenttypedef)
- [InterpretationTypeDef](./type_defs.md#interpretationtypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [SentimentResponseTypeDef](./type_defs.md#sentimentresponsetypedef)
- [SentimentScoreTypeDef](./type_defs.md#sentimentscoretypedef)
- [SessionStateTypeDef](./type_defs.md#sessionstatetypedef)
- [SlotTypeDef](./type_defs.md#slottypedef)
- [ValueTypeDef](./type_defs.md#valuetypedef)
- [DeleteSessionResponseTypeDef](./type_defs.md#deletesessionresponsetypedef)
- [GetSessionResponseTypeDef](./type_defs.md#getsessionresponsetypedef)
- [PutSessionResponseTypeDef](./type_defs.md#putsessionresponsetypedef)
- [RecognizeTextResponseTypeDef](./type_defs.md#recognizetextresponsetypedef)
- [RecognizeUtteranceResponseTypeDef](./type_defs.md#recognizeutteranceresponsetypedef)
