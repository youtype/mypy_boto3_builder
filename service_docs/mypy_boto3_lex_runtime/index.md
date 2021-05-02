# Type annotations for boto3 LexRuntimeService module

> [Index](../index.md) > LexRuntimeService

Auto-generated documentation for [LexRuntimeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService)
type annotations stubs module [mypy_boto3_lex_runtime](https://pypi.org/project/mypy-boto3-lex-runtime/).

```bash
pip install mypy-boto3-lex-runtime
```

- [Type annotations for boto3 LexRuntimeService module](#type-annotations-for-boto3-lexruntimeservice-module)
  - [LexRuntimeServiceClient](#lexruntimeserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## LexRuntimeServiceClient

Type annotations for  `boto3.client("lex-runtime")` as [LexRuntimeServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lex_runtime.client import LexRuntimeServiceClient
```


LexRuntimeServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_session](./client.md#delete-session)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_session](./client.md#get-session)
- [post_content](./client.md#post-content)
- [post_text](./client.md#post-text)
- [put_session](./client.md#put-session)




### Exceptions
- [BadGatewayException](./client.md#badgatewayexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [DependencyFailedException](./client.md#dependencyfailedexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [LoopDetectedException](./client.md#loopdetectedexception)
- [NotAcceptableException](./client.md#notacceptableexception)
- [NotFoundException](./client.md#notfoundexception)
- [RequestTimeoutException](./client.md#requesttimeoutexception)
- [UnsupportedMediaTypeException](./client.md#unsupportedmediatypeexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lex_runtime.literals import ConfirmationStatus, ...
```

- [ConfirmationStatus](./literals.md#confirmationstatus)
- [ContentType](./literals.md#contenttype)
- [DialogActionType](./literals.md#dialogactiontype)
- [DialogState](./literals.md#dialogstate)
- [FulfillmentState](./literals.md#fulfillmentstate)
- [MessageFormatType](./literals.md#messageformattype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef, ...
```

- [ActiveContextTimeToLiveTypeDef](./type_defs.md#activecontexttimetolivetypedef)
- [ActiveContextTypeDef](./type_defs.md#activecontexttypedef)
- [ButtonTypeDef](./type_defs.md#buttontypedef)
- [DialogActionTypeDef](./type_defs.md#dialogactiontypedef)
- [GenericAttachmentTypeDef](./type_defs.md#genericattachmenttypedef)
- [IntentConfidenceTypeDef](./type_defs.md#intentconfidencetypedef)
- [IntentSummaryTypeDef](./type_defs.md#intentsummarytypedef)
- [PredictedIntentTypeDef](./type_defs.md#predictedintenttypedef)
- [ResponseCardTypeDef](./type_defs.md#responsecardtypedef)
- [SentimentResponseTypeDef](./type_defs.md#sentimentresponsetypedef)
- [DeleteSessionResponseTypeDef](./type_defs.md#deletesessionresponsetypedef)
- [GetSessionResponseTypeDef](./type_defs.md#getsessionresponsetypedef)
- [PostContentResponseTypeDef](./type_defs.md#postcontentresponsetypedef)
- [PostTextResponseTypeDef](./type_defs.md#posttextresponsetypedef)
- [PutSessionResponseTypeDef](./type_defs.md#putsessionresponsetypedef)
