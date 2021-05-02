# Structures for boto3 LexRuntimeService module

> [Index](../index.md) > [LexRuntimeService](./index.md) > Structures

Auto-generated documentation for [LexRuntimeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService)
type annotations stubs module [mypy_boto3_lex_runtime](https://pypi.org/project/mypy-boto3-lex-runtime/).

- [Structures for boto3 LexRuntimeService module](#structures-for-boto3-lexruntimeservice-module)
  - [ActiveContextTimeToLiveTypeDef](#activecontexttimetolivetypedef)
  - [ActiveContextTypeDef](#activecontexttypedef)
  - [ButtonTypeDef](#buttontypedef)
  - [DialogActionTypeDef](#dialogactiontypedef)
  - [GenericAttachmentTypeDef](#genericattachmenttypedef)
  - [IntentConfidenceTypeDef](#intentconfidencetypedef)
  - [IntentSummaryTypeDef](#intentsummarytypedef)
  - [PredictedIntentTypeDef](#predictedintenttypedef)
  - [ResponseCardTypeDef](#responsecardtypedef)
  - [SentimentResponseTypeDef](#sentimentresponsetypedef)
  - [DeleteSessionResponseTypeDef](#deletesessionresponsetypedef)
  - [GetSessionResponseTypeDef](#getsessionresponsetypedef)
  - [PostContentResponseTypeDef](#postcontentresponsetypedef)
  - [PostTextResponseTypeDef](#posttextresponsetypedef)
  - [PutSessionResponseTypeDef](#putsessionresponsetypedef)

## ActiveContextTimeToLiveTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef
```




Optional fields:
- `timeToLiveInSeconds`: `int`
- `turnsToLive`: `int`


## ActiveContextTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import ActiveContextTypeDef
```


Required fields:
- `name`: `str`
- `timeToLive`: `"ActiveContextTimeToLiveTypeDef"`
- `parameters`: `Dict[str, str]`




## ButtonTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import ButtonTypeDef
```


Required fields:
- `text`: `str`
- `value`: `str`




## DialogActionTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import DialogActionTypeDef
```


Required fields:
- `type`: `DialogActionType`



Optional fields:
- `intentName`: `str`
- `slots`: `Dict[str, str]`
- `slotToElicit`: `str`
- `fulfillmentState`: `FulfillmentState`
- `message`: `str`
- `messageFormat`: `MessageFormatType`


## GenericAttachmentTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import GenericAttachmentTypeDef
```




Optional fields:
- `title`: `str`
- `subTitle`: `str`
- `attachmentLinkUrl`: `str`
- `imageUrl`: `str`
- `buttons`: `List["ButtonTypeDef"]`


## IntentConfidenceTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import IntentConfidenceTypeDef
```




Optional fields:
- `score`: `float`


## IntentSummaryTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import IntentSummaryTypeDef
```


Required fields:
- `dialogActionType`: `DialogActionType`



Optional fields:
- `intentName`: `str`
- `checkpointLabel`: `str`
- `slots`: `Dict[str, str]`
- `confirmationStatus`: `ConfirmationStatus`
- `fulfillmentState`: `FulfillmentState`
- `slotToElicit`: `str`


## PredictedIntentTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import PredictedIntentTypeDef
```




Optional fields:
- `intentName`: `str`
- `nluIntentConfidence`: `"IntentConfidenceTypeDef"`
- `slots`: `Dict[str, str]`


## ResponseCardTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import ResponseCardTypeDef
```




Optional fields:
- `version`: `str`
- `contentType`: `ContentType`
- `genericAttachments`: `List["GenericAttachmentTypeDef"]`


## SentimentResponseTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import SentimentResponseTypeDef
```




Optional fields:
- `sentimentLabel`: `str`
- `sentimentScore`: `str`


## DeleteSessionResponseTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import DeleteSessionResponseTypeDef
```




Optional fields:
- `botName`: `str`
- `botAlias`: `str`
- `userId`: `str`
- `sessionId`: `str`


## GetSessionResponseTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import GetSessionResponseTypeDef
```




Optional fields:
- `recentIntentSummaryView`: `List["IntentSummaryTypeDef"]`
- `sessionAttributes`: `Dict[str, str]`
- `sessionId`: `str`
- `dialogAction`: `"DialogActionTypeDef"`
- `activeContexts`: `List["ActiveContextTypeDef"]`


## PostContentResponseTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import PostContentResponseTypeDef
```




Optional fields:
- `contentType`: `str`
- `intentName`: `str`
- `nluIntentConfidence`: `str`
- `alternativeIntents`: `str`
- `slots`: `str`
- `sessionAttributes`: `str`
- `sentimentResponse`: `str`
- `message`: `str`
- `encodedMessage`: `str`
- `messageFormat`: `MessageFormatType`
- `dialogState`: `DialogState`
- `slotToElicit`: `str`
- `inputTranscript`: `str`
- `encodedInputTranscript`: `str`
- `audioStream`: `StreamingBody`
- `botVersion`: `str`
- `sessionId`: `str`
- `activeContexts`: `str`


## PostTextResponseTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import PostTextResponseTypeDef
```




Optional fields:
- `intentName`: `str`
- `nluIntentConfidence`: `"IntentConfidenceTypeDef"`
- `alternativeIntents`: `List["PredictedIntentTypeDef"]`
- `slots`: `Dict[str, str]`
- `sessionAttributes`: `Dict[str, str]`
- `message`: `str`
- `sentimentResponse`: `"SentimentResponseTypeDef"`
- `messageFormat`: `MessageFormatType`
- `dialogState`: `DialogState`
- `slotToElicit`: `str`
- `responseCard`: `"ResponseCardTypeDef"`
- `sessionId`: `str`
- `botVersion`: `str`
- `activeContexts`: `List["ActiveContextTypeDef"]`


## PutSessionResponseTypeDef

```python
from mypy_boto3_lex_runtime.type_defs import PutSessionResponseTypeDef
```




Optional fields:
- `contentType`: `str`
- `intentName`: `str`
- `slots`: `str`
- `sessionAttributes`: `str`
- `message`: `str`
- `encodedMessage`: `str`
- `messageFormat`: `MessageFormatType`
- `dialogState`: `DialogState`
- `slotToElicit`: `str`
- `audioStream`: `StreamingBody`
- `sessionId`: `str`
- `activeContexts`: `str`

