# Type annotations for boto3 Polly module

> [Index](../index.md) > Polly

Auto-generated documentation for [Polly](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly)
type annotations stubs module [mypy_boto3_polly](https://pypi.org/project/mypy-boto3-polly/).

```bash
pip install mypy-boto3-polly
```

- [Type annotations for boto3 Polly module](#type-annotations-for-boto3-polly-module)
  - [PollyClient](#pollyclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## PollyClient

Type annotations for  `boto3.client("polly")` as [PollyClient](./client.md)

Can be used directly:

```python
from mypy_boto3_polly.client import PollyClient
```


PollyClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_lexicon](./client.md#delete-lexicon)
- [describe_voices](./client.md#describe-voices)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_lexicon](./client.md#get-lexicon)
- [get_paginator](./client.md#get-paginator)
- [get_speech_synthesis_task](./client.md#get-speech-synthesis-task)
- [list_lexicons](./client.md#list-lexicons)
- [list_speech_synthesis_tasks](./client.md#list-speech-synthesis-tasks)
- [put_lexicon](./client.md#put-lexicon)
- [start_speech_synthesis_task](./client.md#start-speech-synthesis-task)
- [synthesize_speech](./client.md#synthesize-speech)




### Exceptions
- [ClientError](./client.md#clienterror)
- [EngineNotSupportedException](./client.md#enginenotsupportedexception)
- [InvalidLexiconException](./client.md#invalidlexiconexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidS3BucketException](./client.md#invalids3bucketexception)
- [InvalidS3KeyException](./client.md#invalids3keyexception)
- [InvalidSampleRateException](./client.md#invalidsamplerateexception)
- [InvalidSnsTopicArnException](./client.md#invalidsnstopicarnexception)
- [InvalidSsmlException](./client.md#invalidssmlexception)
- [InvalidTaskIdException](./client.md#invalidtaskidexception)
- [LanguageNotSupportedException](./client.md#languagenotsupportedexception)
- [LexiconNotFoundException](./client.md#lexiconnotfoundexception)
- [LexiconSizeExceededException](./client.md#lexiconsizeexceededexception)
- [MarksNotSupportedForFormatException](./client.md#marksnotsupportedforformatexception)
- [MaxLexemeLengthExceededException](./client.md#maxlexemelengthexceededexception)
- [MaxLexiconsNumberExceededException](./client.md#maxlexiconsnumberexceededexception)
- [ServiceFailureException](./client.md#servicefailureexception)
- [SsmlMarksNotSupportedForTextTypeException](./client.md#ssmlmarksnotsupportedfortexttypeexception)
- [SynthesisTaskNotFoundException](./client.md#synthesistasknotfoundexception)
- [TextLengthExceededException](./client.md#textlengthexceededexception)
- [UnsupportedPlsAlphabetException](./client.md#unsupportedplsalphabetexception)
- [UnsupportedPlsLanguageException](./client.md#unsupportedplslanguageexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("polly").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_polly.paginators import DescribeVoicesPaginator, ...
```

- [DescribeVoicesPaginator](./paginators.md#describevoicespaginator)
- [ListLexiconsPaginator](./paginators.md#listlexiconspaginator)
- [ListSpeechSynthesisTasksPaginator](./paginators.md#listspeechsynthesistaskspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_polly.literals import DescribeVoicesPaginatorName, ...
```

- [DescribeVoicesPaginatorName](./literals.md#describevoicespaginatorname)
- [Engine](./literals.md#engine)
- [Gender](./literals.md#gender)
- [LanguageCode](./literals.md#languagecode)
- [ListLexiconsPaginatorName](./literals.md#listlexiconspaginatorname)
- [ListSpeechSynthesisTasksPaginatorName](./literals.md#listspeechsynthesistaskspaginatorname)
- [OutputFormat](./literals.md#outputformat)
- [SpeechMarkType](./literals.md#speechmarktype)
- [TaskStatus](./literals.md#taskstatus)
- [TextType](./literals.md#texttype)
- [VoiceId](./literals.md#voiceid)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_polly.type_defs import DescribeVoicesOutputTypeDef, ...
```

- [DescribeVoicesOutputTypeDef](./type_defs.md#describevoicesoutputtypedef)
- [GetLexiconOutputTypeDef](./type_defs.md#getlexiconoutputtypedef)
- [GetSpeechSynthesisTaskOutputTypeDef](./type_defs.md#getspeechsynthesistaskoutputtypedef)
- [LexiconAttributesTypeDef](./type_defs.md#lexiconattributestypedef)
- [LexiconDescriptionTypeDef](./type_defs.md#lexicondescriptiontypedef)
- [LexiconTypeDef](./type_defs.md#lexicontypedef)
- [ListLexiconsOutputTypeDef](./type_defs.md#listlexiconsoutputtypedef)
- [ListSpeechSynthesisTasksOutputTypeDef](./type_defs.md#listspeechsynthesistasksoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [StartSpeechSynthesisTaskOutputTypeDef](./type_defs.md#startspeechsynthesistaskoutputtypedef)
- [SynthesisTaskTypeDef](./type_defs.md#synthesistasktypedef)
- [SynthesizeSpeechOutputTypeDef](./type_defs.md#synthesizespeechoutputtypedef)
- [VoiceTypeDef](./type_defs.md#voicetypedef)
