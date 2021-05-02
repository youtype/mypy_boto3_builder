# PollyClient for boto3 Polly module

> [Index](../index.md) > [Polly](./index.md) > PollyClient

Auto-generated documentation for [Polly](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly)
type annotations stubs module [mypy_boto3_polly](https://pypi.org/project/mypy-boto3-polly/).

- [PollyClient for boto3 Polly module](#pollyclient-for-boto3-polly-module)
  - [PollyClient](#pollyclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_lexicon](#delete_lexicon)
    - [describe_voices](#describe_voices)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_lexicon](#get_lexicon)
    - [get_speech_synthesis_task](#get_speech_synthesis_task)
    - [list_lexicons](#list_lexicons)
    - [list_speech_synthesis_tasks](#list_speech_synthesis_tasks)
    - [put_lexicon](#put_lexicon)
    - [start_speech_synthesis_task](#start_speech_synthesis_task)
    - [synthesize_speech](#synthesize_speech)
    - [get_paginator](#get_paginator)

## PollyClient

Type annotations for `boto3.client("polly")`

Can be used directly:

```python
from mypy_boto3_polly.client import PollyClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_polly.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.EngineNotSupportedException`
- `Exceptions.InvalidLexiconException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidS3BucketException`
- `Exceptions.InvalidS3KeyException`
- `Exceptions.InvalidSampleRateException`
- `Exceptions.InvalidSnsTopicArnException`
- `Exceptions.InvalidSsmlException`
- `Exceptions.InvalidTaskIdException`
- `Exceptions.LanguageNotSupportedException`
- `Exceptions.LexiconNotFoundException`
- `Exceptions.LexiconSizeExceededException`
- `Exceptions.MarksNotSupportedForFormatException`
- `Exceptions.MaxLexemeLengthExceededException`
- `Exceptions.MaxLexiconsNumberExceededException`
- `Exceptions.ServiceFailureException`
- `Exceptions.SsmlMarksNotSupportedForTextTypeException`
- `Exceptions.SynthesisTaskNotFoundException`
- `Exceptions.TextLengthExceededException`
- `Exceptions.UnsupportedPlsAlphabetException`
- `Exceptions.UnsupportedPlsLanguageException`


## Methods


### can_paginate

Type annotations for `boto3.client("polly").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_lexicon

Type annotations for `boto3.client("polly").delete_lexicon` method.

[Client.delete_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.delete_lexicon)

```python
def delete_lexicon(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### describe_voices

Type annotations for `boto3.client("polly").describe_voices` method.

[Client.describe_voices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.describe_voices)

```python
def describe_voices(
    self,
    Engine: Engine = None,
    LanguageCode: LanguageCode = None,
    IncludeAdditionalLanguageCodes: bool = None,
    NextToken: str = None
) -> DescribeVoicesOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("polly").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.generate_presigned_url)

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

### get_lexicon

Type annotations for `boto3.client("polly").get_lexicon` method.

[Client.get_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.get_lexicon)

```python
def get_lexicon(
    self,
    Name: str
) -> GetLexiconOutputTypeDef:
    pass
```

### get_speech_synthesis_task

Type annotations for `boto3.client("polly").get_speech_synthesis_task` method.

[Client.get_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.get_speech_synthesis_task)

```python
def get_speech_synthesis_task(
    self,
    TaskId: str
) -> GetSpeechSynthesisTaskOutputTypeDef:
    pass
```

### list_lexicons

Type annotations for `boto3.client("polly").list_lexicons` method.

[Client.list_lexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.list_lexicons)

```python
def list_lexicons(
    self,
    NextToken: str = None
) -> ListLexiconsOutputTypeDef:
    pass
```

### list_speech_synthesis_tasks

Type annotations for `boto3.client("polly").list_speech_synthesis_tasks` method.

[Client.list_speech_synthesis_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.list_speech_synthesis_tasks)

```python
def list_speech_synthesis_tasks(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    Status: TaskStatus = None
) -> ListSpeechSynthesisTasksOutputTypeDef:
    pass
```

### put_lexicon

Type annotations for `boto3.client("polly").put_lexicon` method.

[Client.put_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.put_lexicon)

```python
def put_lexicon(
    self,
    Name: str,
    Content: str
) -> Dict[str, Any]:
    pass
```

### start_speech_synthesis_task

Type annotations for `boto3.client("polly").start_speech_synthesis_task` method.

[Client.start_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.start_speech_synthesis_task)

```python
def start_speech_synthesis_task(
    self,
    OutputFormat: OutputFormat,
    OutputS3BucketName: str,
    Text: str,
    VoiceId: VoiceId,
    Engine: Engine = None,
    LanguageCode: LanguageCode = None,
    LexiconNames: List[str] = None,
    OutputS3KeyPrefix: str = None,
    SampleRate: str = None,
    SnsTopicArn: str = None,
    SpeechMarkTypes: List[SpeechMarkType] = None,
    TextType: TextType = None
) -> StartSpeechSynthesisTaskOutputTypeDef:
    pass
```

### synthesize_speech

Type annotations for `boto3.client("polly").synthesize_speech` method.

[Client.synthesize_speech documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.synthesize_speech)

```python
def synthesize_speech(
    self,
    OutputFormat: OutputFormat,
    Text: str,
    VoiceId: VoiceId,
    Engine: Engine = None,
    LanguageCode: LanguageCode = None,
    LexiconNames: List[str] = None,
    SampleRate: str = None,
    SpeechMarkTypes: List[SpeechMarkType] = None,
    TextType: TextType = None
) -> SynthesizeSpeechOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("polly").get_paginator` method with overloads.

- `client.get_paginator("describe_voices")` -> [DescribeVoicesPaginator](./paginators.md#describevoicespaginator)
- `client.get_paginator("list_lexicons")` -> [ListLexiconsPaginator](./paginators.md#listlexiconspaginator)
- `client.get_paginator("list_speech_synthesis_tasks")` -> [ListSpeechSynthesisTasksPaginator](./paginators.md#listspeechsynthesistaskspaginator)


