# Literals for boto3 TranscribeService module

> [Index](../index.md) > [TranscribeService](./index.md) > Literals

Auto-generated documentation for [TranscribeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService)
type annotations stubs module [mypy_boto3_transcribe](https://pypi.org/project/mypy-boto3-transcribe/).

- [Literals for boto3 TranscribeService module](#literals-for-boto3-transcribeservice-module)
  - [BaseModelName](#basemodelname)
  - [CLMLanguageCode](#clmlanguagecode)
  - [LanguageCode](#languagecode)
  - [MediaFormat](#mediaformat)
  - [ModelStatus](#modelstatus)
  - [OutputLocationType](#outputlocationtype)
  - [RedactionOutput](#redactionoutput)
  - [RedactionType](#redactiontype)
  - [Specialty](#specialty)
  - [TranscriptionJobStatus](#transcriptionjobstatus)
  - [TypeType](#typetype)
  - [VocabularyFilterMethod](#vocabularyfiltermethod)
  - [VocabularyState](#vocabularystate)

## BaseModelName

```python
from mypy_boto3_transcribe.literals import BaseModelName
```

Values:

- `NarrowBand`
- `WideBand`

## CLMLanguageCode

```python
from mypy_boto3_transcribe.literals import CLMLanguageCode
```

Values:

- `en-AU`
- `en-GB`
- `en-US`
- `es-US`
- `hi-IN`

## LanguageCode

```python
from mypy_boto3_transcribe.literals import LanguageCode
```

Values:

- `af-ZA`
- `ar-AE`
- `ar-SA`
- `cy-GB`
- `da-DK`
- `de-CH`
- `de-DE`
- `en-AB`
- `en-AU`
- `en-GB`
- `en-IE`
- `en-IN`
- `en-US`
- `en-WL`
- `es-ES`
- `es-US`
- `fa-IR`
- `fr-CA`
- `fr-FR`
- `ga-IE`
- `gd-GB`
- `he-IL`
- `hi-IN`
- `id-ID`
- `it-IT`
- `ja-JP`
- `ko-KR`
- `ms-MY`
- `nl-NL`
- `pt-BR`
- `pt-PT`
- `ru-RU`
- `ta-IN`
- `te-IN`
- `tr-TR`
- `zh-CN`

## MediaFormat

```python
from mypy_boto3_transcribe.literals import MediaFormat
```

Values:

- `amr`
- `flac`
- `mp3`
- `mp4`
- `ogg`
- `wav`
- `webm`

## ModelStatus

```python
from mypy_boto3_transcribe.literals import ModelStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`

## OutputLocationType

```python
from mypy_boto3_transcribe.literals import OutputLocationType
```

Values:

- `CUSTOMER_BUCKET`
- `SERVICE_BUCKET`

## RedactionOutput

```python
from mypy_boto3_transcribe.literals import RedactionOutput
```

Values:

- `redacted`
- `redacted_and_unredacted`

## RedactionType

```python
from mypy_boto3_transcribe.literals import RedactionType
```

Values:

- `PII`

## Specialty

```python
from mypy_boto3_transcribe.literals import Specialty
```

Values:

- `PRIMARYCARE`

## TranscriptionJobStatus

```python
from mypy_boto3_transcribe.literals import TranscriptionJobStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`
- `QUEUED`

## TypeType

```python
from mypy_boto3_transcribe.literals import TypeType
```

Values:

- `CONVERSATION`
- `DICTATION`

## VocabularyFilterMethod

```python
from mypy_boto3_transcribe.literals import VocabularyFilterMethod
```

Values:

- `mask`
- `remove`
- `tag`

## VocabularyState

```python
from mypy_boto3_transcribe.literals import VocabularyState
```

Values:

- `FAILED`
- `PENDING`
- `READY`
