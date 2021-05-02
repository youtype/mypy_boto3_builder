# Paginators for boto3 Polly module

> [Index](../index.md) > [Polly](./index.md) > Paginators

Auto-generated documentation for [Polly](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly)
type annotations stubs module [mypy_boto3_polly](https://pypi.org/project/mypy-boto3-polly/).

- [Paginators for boto3 Polly module](#paginators-for-boto3-polly-module)
  - [DescribeVoicesPaginator](#describevoicespaginator)
  - [ListLexiconsPaginator](#listlexiconspaginator)
  - [ListSpeechSynthesisTasksPaginator](#listspeechsynthesistaskspaginator)

## DescribeVoicesPaginator

Type annotations for `boto3.client("polly").get_paginator("describe_voices")`.

Can be used directly:

```python
from mypy_boto3_polly.paginators import DescribeVoicesPaginator

def get_describe_voices_paginator() -> DescribeVoicesPaginator:
    return boto3.client("polly").get_paginator("describe_voices")
```

[Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Paginator.DescribeVoices)

```python
class DescribeVoicesPaginator(Boto3Paginator):
    def paginate(
        self,
        Engine: Engine = None,
        LanguageCode: LanguageCode = None,
        IncludeAdditionalLanguageCodes: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVoicesOutputTypeDef]:
        pass
```
## ListLexiconsPaginator

Type annotations for `boto3.client("polly").get_paginator("list_lexicons")`.

Can be used directly:

```python
from mypy_boto3_polly.paginators import ListLexiconsPaginator

def get_list_lexicons_paginator() -> ListLexiconsPaginator:
    return boto3.client("polly").get_paginator("list_lexicons")
```

[Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Paginator.ListLexicons)

```python
class ListLexiconsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLexiconsOutputTypeDef]:
        pass
```
## ListSpeechSynthesisTasksPaginator

Type annotations for `boto3.client("polly").get_paginator("list_speech_synthesis_tasks")`.

Can be used directly:

```python
from mypy_boto3_polly.paginators import ListSpeechSynthesisTasksPaginator

def get_list_speech_synthesis_tasks_paginator() -> ListSpeechSynthesisTasksPaginator:
    return boto3.client("polly").get_paginator("list_speech_synthesis_tasks")
```

[Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)

```python
class ListSpeechSynthesisTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        Status: TaskStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpeechSynthesisTasksOutputTypeDef]:
        pass
```