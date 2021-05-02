# TranscribeServiceClient for boto3 TranscribeService module

> [Index](../index.md) > [TranscribeService](./index.md) > TranscribeServiceClient

Auto-generated documentation for [TranscribeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService)
type annotations stubs module [mypy_boto3_transcribe](https://pypi.org/project/mypy-boto3-transcribe/).

- [TranscribeServiceClient for boto3 TranscribeService module](#transcribeserviceclient-for-boto3-transcribeservice-module)
  - [TranscribeServiceClient](#transcribeserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_language_model](#create_language_model)
    - [create_medical_vocabulary](#create_medical_vocabulary)
    - [create_vocabulary](#create_vocabulary)
    - [create_vocabulary_filter](#create_vocabulary_filter)
    - [delete_language_model](#delete_language_model)
    - [delete_medical_transcription_job](#delete_medical_transcription_job)
    - [delete_medical_vocabulary](#delete_medical_vocabulary)
    - [delete_transcription_job](#delete_transcription_job)
    - [delete_vocabulary](#delete_vocabulary)
    - [delete_vocabulary_filter](#delete_vocabulary_filter)
    - [describe_language_model](#describe_language_model)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_medical_transcription_job](#get_medical_transcription_job)
    - [get_medical_vocabulary](#get_medical_vocabulary)
    - [get_transcription_job](#get_transcription_job)
    - [get_vocabulary](#get_vocabulary)
    - [get_vocabulary_filter](#get_vocabulary_filter)
    - [list_language_models](#list_language_models)
    - [list_medical_transcription_jobs](#list_medical_transcription_jobs)
    - [list_medical_vocabularies](#list_medical_vocabularies)
    - [list_transcription_jobs](#list_transcription_jobs)
    - [list_vocabularies](#list_vocabularies)
    - [list_vocabulary_filters](#list_vocabulary_filters)
    - [start_medical_transcription_job](#start_medical_transcription_job)
    - [start_transcription_job](#start_transcription_job)
    - [update_medical_vocabulary](#update_medical_vocabulary)
    - [update_vocabulary](#update_vocabulary)
    - [update_vocabulary_filter](#update_vocabulary_filter)

## TranscribeServiceClient

Type annotations for `boto3.client("transcribe")`

Can be used directly:

```python
from mypy_boto3_transcribe.client import TranscribeServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_transcribe.client import Exceptions

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


## Methods


### can_paginate

Type annotations for `boto3.client("transcribe").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_language_model

Type annotations for `boto3.client("transcribe").create_language_model` method.

[Client.create_language_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_language_model)

```python
def create_language_model(
    self,
    LanguageCode: CLMLanguageCode,
    BaseModelName: BaseModelName,
    ModelName: str,
    InputDataConfig: "InputDataConfigTypeDef"
) -> CreateLanguageModelResponseTypeDef:
    pass
```

### create_medical_vocabulary

Type annotations for `boto3.client("transcribe").create_medical_vocabulary` method.

[Client.create_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_medical_vocabulary)

```python
def create_medical_vocabulary(
    self,
    VocabularyName: str,
    LanguageCode: LanguageCode,
    VocabularyFileUri: str
) -> CreateMedicalVocabularyResponseTypeDef:
    pass
```

### create_vocabulary

Type annotations for `boto3.client("transcribe").create_vocabulary` method.

[Client.create_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary)

```python
def create_vocabulary(
    self,
    VocabularyName: str,
    LanguageCode: LanguageCode,
    Phrases: List[str] = None,
    VocabularyFileUri: str = None
) -> CreateVocabularyResponseTypeDef:
    pass
```

### create_vocabulary_filter

Type annotations for `boto3.client("transcribe").create_vocabulary_filter` method.

[Client.create_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary_filter)

```python
def create_vocabulary_filter(
    self,
    VocabularyFilterName: str,
    LanguageCode: LanguageCode,
    Words: List[str] = None,
    VocabularyFilterFileUri: str = None
) -> CreateVocabularyFilterResponseTypeDef:
    pass
```

### delete_language_model

Type annotations for `boto3.client("transcribe").delete_language_model` method.

[Client.delete_language_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_language_model)

```python
def delete_language_model(
    self,
    ModelName: str
) -> None:
    pass
```

### delete_medical_transcription_job

Type annotations for `boto3.client("transcribe").delete_medical_transcription_job` method.

[Client.delete_medical_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_medical_transcription_job)

```python
def delete_medical_transcription_job(
    self,
    MedicalTranscriptionJobName: str
) -> None:
    pass
```

### delete_medical_vocabulary

Type annotations for `boto3.client("transcribe").delete_medical_vocabulary` method.

[Client.delete_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_medical_vocabulary)

```python
def delete_medical_vocabulary(
    self,
    VocabularyName: str
) -> None:
    pass
```

### delete_transcription_job

Type annotations for `boto3.client("transcribe").delete_transcription_job` method.

[Client.delete_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_transcription_job)

```python
def delete_transcription_job(
    self,
    TranscriptionJobName: str
) -> None:
    pass
```

### delete_vocabulary

Type annotations for `boto3.client("transcribe").delete_vocabulary` method.

[Client.delete_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary)

```python
def delete_vocabulary(
    self,
    VocabularyName: str
) -> None:
    pass
```

### delete_vocabulary_filter

Type annotations for `boto3.client("transcribe").delete_vocabulary_filter` method.

[Client.delete_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary_filter)

```python
def delete_vocabulary_filter(
    self,
    VocabularyFilterName: str
) -> None:
    pass
```

### describe_language_model

Type annotations for `boto3.client("transcribe").describe_language_model` method.

[Client.describe_language_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.describe_language_model)

```python
def describe_language_model(
    self,
    ModelName: str
) -> DescribeLanguageModelResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("transcribe").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.generate_presigned_url)

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

### get_medical_transcription_job

Type annotations for `boto3.client("transcribe").get_medical_transcription_job` method.

[Client.get_medical_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_medical_transcription_job)

```python
def get_medical_transcription_job(
    self,
    MedicalTranscriptionJobName: str
) -> GetMedicalTranscriptionJobResponseTypeDef:
    pass
```

### get_medical_vocabulary

Type annotations for `boto3.client("transcribe").get_medical_vocabulary` method.

[Client.get_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_medical_vocabulary)

```python
def get_medical_vocabulary(
    self,
    VocabularyName: str
) -> GetMedicalVocabularyResponseTypeDef:
    pass
```

### get_transcription_job

Type annotations for `boto3.client("transcribe").get_transcription_job` method.

[Client.get_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job)

```python
def get_transcription_job(
    self,
    TranscriptionJobName: str
) -> GetTranscriptionJobResponseTypeDef:
    pass
```

### get_vocabulary

Type annotations for `boto3.client("transcribe").get_vocabulary` method.

[Client.get_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary)

```python
def get_vocabulary(
    self,
    VocabularyName: str
) -> GetVocabularyResponseTypeDef:
    pass
```

### get_vocabulary_filter

Type annotations for `boto3.client("transcribe").get_vocabulary_filter` method.

[Client.get_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary_filter)

```python
def get_vocabulary_filter(
    self,
    VocabularyFilterName: str
) -> GetVocabularyFilterResponseTypeDef:
    pass
```

### list_language_models

Type annotations for `boto3.client("transcribe").list_language_models` method.

[Client.list_language_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_language_models)

```python
def list_language_models(
    self,
    StatusEquals: ModelStatus = None,
    NameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLanguageModelsResponseTypeDef:
    pass
```

### list_medical_transcription_jobs

Type annotations for `boto3.client("transcribe").list_medical_transcription_jobs` method.

[Client.list_medical_transcription_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_medical_transcription_jobs)

```python
def list_medical_transcription_jobs(
    self,
    Status: TranscriptionJobStatus = None,
    JobNameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMedicalTranscriptionJobsResponseTypeDef:
    pass
```

### list_medical_vocabularies

Type annotations for `boto3.client("transcribe").list_medical_vocabularies` method.

[Client.list_medical_vocabularies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_medical_vocabularies)

```python
def list_medical_vocabularies(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    StateEquals: VocabularyState = None,
    NameContains: str = None
) -> ListMedicalVocabulariesResponseTypeDef:
    pass
```

### list_transcription_jobs

Type annotations for `boto3.client("transcribe").list_transcription_jobs` method.

[Client.list_transcription_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_transcription_jobs)

```python
def list_transcription_jobs(
    self,
    Status: TranscriptionJobStatus = None,
    JobNameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTranscriptionJobsResponseTypeDef:
    pass
```

### list_vocabularies

Type annotations for `boto3.client("transcribe").list_vocabularies` method.

[Client.list_vocabularies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_vocabularies)

```python
def list_vocabularies(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    StateEquals: VocabularyState = None,
    NameContains: str = None
) -> ListVocabulariesResponseTypeDef:
    pass
```

### list_vocabulary_filters

Type annotations for `boto3.client("transcribe").list_vocabulary_filters` method.

[Client.list_vocabulary_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_vocabulary_filters)

```python
def list_vocabulary_filters(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None
) -> ListVocabularyFiltersResponseTypeDef:
    pass
```

### start_medical_transcription_job

Type annotations for `boto3.client("transcribe").start_medical_transcription_job` method.

[Client.start_medical_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_medical_transcription_job)

```python
def start_medical_transcription_job(
    self,
    MedicalTranscriptionJobName: str,
    LanguageCode: LanguageCode,
    Media: "MediaTypeDef",
    OutputBucketName: str,
    Specialty: Literal['PRIMARYCARE'],
    Type: TypeType,
    MediaSampleRateHertz: int = None,
    MediaFormat: MediaFormat = None,
    OutputKey: str = None,
    OutputEncryptionKMSKeyId: str = None,
    Settings: "MedicalTranscriptionSettingTypeDef" = None
) -> StartMedicalTranscriptionJobResponseTypeDef:
    pass
```

### start_transcription_job

Type annotations for `boto3.client("transcribe").start_transcription_job` method.

[Client.start_transcription_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job)

```python
def start_transcription_job(
    self,
    TranscriptionJobName: str,
    Media: "MediaTypeDef",
    LanguageCode: LanguageCode = None,
    MediaSampleRateHertz: int = None,
    MediaFormat: MediaFormat = None,
    OutputBucketName: str = None,
    OutputKey: str = None,
    OutputEncryptionKMSKeyId: str = None,
    Settings: "SettingsTypeDef" = None,
    ModelSettings: "ModelSettingsTypeDef" = None,
    JobExecutionSettings: "JobExecutionSettingsTypeDef" = None,
    ContentRedaction: "ContentRedactionTypeDef" = None,
    IdentifyLanguage: bool = None,
    LanguageOptions: List[LanguageCode] = None
) -> StartTranscriptionJobResponseTypeDef:
    pass
```

### update_medical_vocabulary

Type annotations for `boto3.client("transcribe").update_medical_vocabulary` method.

[Client.update_medical_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_medical_vocabulary)

```python
def update_medical_vocabulary(
    self,
    VocabularyName: str,
    LanguageCode: LanguageCode,
    VocabularyFileUri: str = None
) -> UpdateMedicalVocabularyResponseTypeDef:
    pass
```

### update_vocabulary

Type annotations for `boto3.client("transcribe").update_vocabulary` method.

[Client.update_vocabulary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary)

```python
def update_vocabulary(
    self,
    VocabularyName: str,
    LanguageCode: LanguageCode,
    Phrases: List[str] = None,
    VocabularyFileUri: str = None
) -> UpdateVocabularyResponseTypeDef:
    pass
```

### update_vocabulary_filter

Type annotations for `boto3.client("transcribe").update_vocabulary_filter` method.

[Client.update_vocabulary_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary_filter)

```python
def update_vocabulary_filter(
    self,
    VocabularyFilterName: str,
    Words: List[str] = None,
    VocabularyFilterFileUri: str = None
) -> UpdateVocabularyFilterResponseTypeDef:
    pass
```



