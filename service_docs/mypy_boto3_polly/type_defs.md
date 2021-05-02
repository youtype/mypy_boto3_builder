# Structures for boto3 Polly module

> [Index](../index.md) > [Polly](./index.md) > Structures

Auto-generated documentation for [Polly](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly)
type annotations stubs module [mypy_boto3_polly](https://pypi.org/project/mypy-boto3-polly/).

- [Structures for boto3 Polly module](#structures-for-boto3-polly-module)
  - [DescribeVoicesOutputTypeDef](#describevoicesoutputtypedef)
  - [GetLexiconOutputTypeDef](#getlexiconoutputtypedef)
  - [GetSpeechSynthesisTaskOutputTypeDef](#getspeechsynthesistaskoutputtypedef)
  - [LexiconAttributesTypeDef](#lexiconattributestypedef)
  - [LexiconDescriptionTypeDef](#lexicondescriptiontypedef)
  - [LexiconTypeDef](#lexicontypedef)
  - [ListLexiconsOutputTypeDef](#listlexiconsoutputtypedef)
  - [ListSpeechSynthesisTasksOutputTypeDef](#listspeechsynthesistasksoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [StartSpeechSynthesisTaskOutputTypeDef](#startspeechsynthesistaskoutputtypedef)
  - [SynthesisTaskTypeDef](#synthesistasktypedef)
  - [SynthesizeSpeechOutputTypeDef](#synthesizespeechoutputtypedef)
  - [VoiceTypeDef](#voicetypedef)

## DescribeVoicesOutputTypeDef

```python
from mypy_boto3_polly.type_defs import DescribeVoicesOutputTypeDef
```




Optional fields:
- `Voices`: `List["VoiceTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetLexiconOutputTypeDef

```python
from mypy_boto3_polly.type_defs import GetLexiconOutputTypeDef
```




Optional fields:
- `Lexicon`: `"LexiconTypeDef"`
- `LexiconAttributes`: `"LexiconAttributesTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetSpeechSynthesisTaskOutputTypeDef

```python
from mypy_boto3_polly.type_defs import GetSpeechSynthesisTaskOutputTypeDef
```




Optional fields:
- `SynthesisTask`: `"SynthesisTaskTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## LexiconAttributesTypeDef

```python
from mypy_boto3_polly.type_defs import LexiconAttributesTypeDef
```




Optional fields:
- `Alphabet`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModified`: `datetime`
- `LexiconArn`: `str`
- `LexemesCount`: `int`
- `Size`: `int`


## LexiconDescriptionTypeDef

```python
from mypy_boto3_polly.type_defs import LexiconDescriptionTypeDef
```




Optional fields:
- `Name`: `str`
- `Attributes`: `"LexiconAttributesTypeDef"`


## LexiconTypeDef

```python
from mypy_boto3_polly.type_defs import LexiconTypeDef
```




Optional fields:
- `Content`: `str`
- `Name`: `str`


## ListLexiconsOutputTypeDef

```python
from mypy_boto3_polly.type_defs import ListLexiconsOutputTypeDef
```




Optional fields:
- `Lexicons`: `List["LexiconDescriptionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSpeechSynthesisTasksOutputTypeDef

```python
from mypy_boto3_polly.type_defs import ListSpeechSynthesisTasksOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `SynthesisTasks`: `List["SynthesisTaskTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_polly.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResponseMetadata

```python
from mypy_boto3_polly.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## StartSpeechSynthesisTaskOutputTypeDef

```python
from mypy_boto3_polly.type_defs import StartSpeechSynthesisTaskOutputTypeDef
```




Optional fields:
- `SynthesisTask`: `"SynthesisTaskTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SynthesisTaskTypeDef

```python
from mypy_boto3_polly.type_defs import SynthesisTaskTypeDef
```




Optional fields:
- `Engine`: `Engine`
- `TaskId`: `str`
- `TaskStatus`: `TaskStatus`
- `TaskStatusReason`: `str`
- `OutputUri`: `str`
- `CreationTime`: `datetime`
- `RequestCharacters`: `int`
- `SnsTopicArn`: `str`
- `LexiconNames`: `List[str]`
- `OutputFormat`: `OutputFormat`
- `SampleRate`: `str`
- `SpeechMarkTypes`: `List[SpeechMarkType]`
- `TextType`: `TextType`
- `VoiceId`: `VoiceId`
- `LanguageCode`: `LanguageCode`


## SynthesizeSpeechOutputTypeDef

```python
from mypy_boto3_polly.type_defs import SynthesizeSpeechOutputTypeDef
```




Optional fields:
- `AudioStream`: `StreamingBody`
- `ContentType`: `str`
- `RequestCharacters`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## VoiceTypeDef

```python
from mypy_boto3_polly.type_defs import VoiceTypeDef
```




Optional fields:
- `Gender`: `Gender`
- `Id`: `VoiceId`
- `LanguageCode`: `LanguageCode`
- `LanguageName`: `str`
- `Name`: `str`
- `AdditionalLanguageCodes`: `List[LanguageCode]`
- `SupportedEngines`: `List[Engine]`

