# TranslateClient for boto3 Translate module

> [Index](../index.md) > [Translate](./index.md) > TranslateClient

Auto-generated documentation for [Translate](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate)
type annotations stubs module [mypy_boto3_translate](https://pypi.org/project/mypy-boto3-translate/).

- [TranslateClient for boto3 Translate module](#translateclient-for-boto3-translate-module)
  - [TranslateClient](#translateclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_parallel_data](#create_parallel_data)
    - [delete_parallel_data](#delete_parallel_data)
    - [delete_terminology](#delete_terminology)
    - [describe_text_translation_job](#describe_text_translation_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_parallel_data](#get_parallel_data)
    - [get_terminology](#get_terminology)
    - [import_terminology](#import_terminology)
    - [list_parallel_data](#list_parallel_data)
    - [list_terminologies](#list_terminologies)
    - [list_text_translation_jobs](#list_text_translation_jobs)
    - [start_text_translation_job](#start_text_translation_job)
    - [stop_text_translation_job](#stop_text_translation_job)
    - [translate_text](#translate_text)
    - [update_parallel_data](#update_parallel_data)
    - [get_paginator](#get_paginator)

## TranslateClient

Type annotations for `boto3.client("translate")`

Can be used directly:

```python
from mypy_boto3_translate.client import TranslateClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_translate.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConflictException`
- `Exceptions.DetectedLanguageLowConfidenceException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidFilterException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TextSizeLimitExceededException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnsupportedLanguagePairException`


## Methods


### can_paginate

Type annotations for `boto3.client("translate").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_parallel_data

Type annotations for `boto3.client("translate").create_parallel_data` method.

[Client.create_parallel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.create_parallel_data)

```python
def create_parallel_data(
    self,
    Name: str,
    ParallelDataConfig: "ParallelDataConfigTypeDef",
    ClientToken: str,
    Description: str = None,
    EncryptionKey: "EncryptionKeyTypeDef" = None
) -> CreateParallelDataResponseTypeDef:
    pass
```

### delete_parallel_data

Type annotations for `boto3.client("translate").delete_parallel_data` method.

[Client.delete_parallel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.delete_parallel_data)

```python
def delete_parallel_data(
    self,
    Name: str
) -> DeleteParallelDataResponseTypeDef:
    pass
```

### delete_terminology

Type annotations for `boto3.client("translate").delete_terminology` method.

[Client.delete_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.delete_terminology)

```python
def delete_terminology(
    self,
    Name: str
) -> None:
    pass
```

### describe_text_translation_job

Type annotations for `boto3.client("translate").describe_text_translation_job` method.

[Client.describe_text_translation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.describe_text_translation_job)

```python
def describe_text_translation_job(
    self,
    JobId: str
) -> DescribeTextTranslationJobResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("translate").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.generate_presigned_url)

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

### get_parallel_data

Type annotations for `boto3.client("translate").get_parallel_data` method.

[Client.get_parallel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.get_parallel_data)

```python
def get_parallel_data(
    self,
    Name: str
) -> GetParallelDataResponseTypeDef:
    pass
```

### get_terminology

Type annotations for `boto3.client("translate").get_terminology` method.

[Client.get_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.get_terminology)

```python
def get_terminology(
    self,
    Name: str,
    TerminologyDataFormat: TerminologyDataFormat
) -> GetTerminologyResponseTypeDef:
    pass
```

### import_terminology

Type annotations for `boto3.client("translate").import_terminology` method.

[Client.import_terminology documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.import_terminology)

```python
def import_terminology(
    self,
    Name: str,
    MergeStrategy: MergeStrategy,
    TerminologyData: TerminologyDataTypeDef,
    Description: str = None,
    EncryptionKey: "EncryptionKeyTypeDef" = None
) -> ImportTerminologyResponseTypeDef:
    pass
```

### list_parallel_data

Type annotations for `boto3.client("translate").list_parallel_data` method.

[Client.list_parallel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.list_parallel_data)

```python
def list_parallel_data(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListParallelDataResponseTypeDef:
    pass
```

### list_terminologies

Type annotations for `boto3.client("translate").list_terminologies` method.

[Client.list_terminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.list_terminologies)

```python
def list_terminologies(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTerminologiesResponseTypeDef:
    pass
```

### list_text_translation_jobs

Type annotations for `boto3.client("translate").list_text_translation_jobs` method.

[Client.list_text_translation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.list_text_translation_jobs)

```python
def list_text_translation_jobs(
    self,
    Filter: TextTranslationJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTextTranslationJobsResponseTypeDef:
    pass
```

### start_text_translation_job

Type annotations for `boto3.client("translate").start_text_translation_job` method.

[Client.start_text_translation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.start_text_translation_job)

```python
def start_text_translation_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    SourceLanguageCode: str,
    TargetLanguageCodes: List[str],
    ClientToken: str,
    JobName: str = None,
    TerminologyNames: List[str] = None,
    ParallelDataNames: List[str] = None
) -> StartTextTranslationJobResponseTypeDef:
    pass
```

### stop_text_translation_job

Type annotations for `boto3.client("translate").stop_text_translation_job` method.

[Client.stop_text_translation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.stop_text_translation_job)

```python
def stop_text_translation_job(
    self,
    JobId: str
) -> StopTextTranslationJobResponseTypeDef:
    pass
```

### translate_text

Type annotations for `boto3.client("translate").translate_text` method.

[Client.translate_text documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.translate_text)

```python
def translate_text(
    self,
    Text: str,
    SourceLanguageCode: str,
    TargetLanguageCode: str,
    TerminologyNames: List[str] = None
) -> TranslateTextResponseTypeDef:
    pass
```

### update_parallel_data

Type annotations for `boto3.client("translate").update_parallel_data` method.

[Client.update_parallel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Client.update_parallel_data)

```python
def update_parallel_data(
    self,
    Name: str,
    ParallelDataConfig: "ParallelDataConfigTypeDef",
    ClientToken: str,
    Description: str = None
) -> UpdateParallelDataResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("translate").get_paginator` method.

[Paginator.ListTerminologies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate.Paginator.ListTerminologies)

```python
def get_paginator(
    self,
    operation_name: ListTerminologiesPaginatorName
) -> ListTerminologiesPaginator:
    pass
```