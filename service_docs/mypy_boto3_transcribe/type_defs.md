# Structures for boto3 TranscribeService module

> [Index](../index.md) > [TranscribeService](./index.md) > Structures

Auto-generated documentation for [TranscribeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService)
type annotations stubs module [mypy_boto3_transcribe](https://pypi.org/project/mypy-boto3-transcribe/).

- [Structures for boto3 TranscribeService module](#structures-for-boto3-transcribeservice-module)
  - [ContentRedactionTypeDef](#contentredactiontypedef)
  - [InputDataConfigTypeDef](#inputdataconfigtypedef)
  - [JobExecutionSettingsTypeDef](#jobexecutionsettingstypedef)
  - [LanguageModelTypeDef](#languagemodeltypedef)
  - [MediaTypeDef](#mediatypedef)
  - [MedicalTranscriptTypeDef](#medicaltranscripttypedef)
  - [MedicalTranscriptionJobSummaryTypeDef](#medicaltranscriptionjobsummarytypedef)
  - [MedicalTranscriptionJobTypeDef](#medicaltranscriptionjobtypedef)
  - [MedicalTranscriptionSettingTypeDef](#medicaltranscriptionsettingtypedef)
  - [ModelSettingsTypeDef](#modelsettingstypedef)
  - [SettingsTypeDef](#settingstypedef)
  - [TranscriptTypeDef](#transcripttypedef)
  - [TranscriptionJobSummaryTypeDef](#transcriptionjobsummarytypedef)
  - [TranscriptionJobTypeDef](#transcriptionjobtypedef)
  - [VocabularyFilterInfoTypeDef](#vocabularyfilterinfotypedef)
  - [VocabularyInfoTypeDef](#vocabularyinfotypedef)
  - [CreateLanguageModelResponseTypeDef](#createlanguagemodelresponsetypedef)
  - [CreateMedicalVocabularyResponseTypeDef](#createmedicalvocabularyresponsetypedef)
  - [CreateVocabularyFilterResponseTypeDef](#createvocabularyfilterresponsetypedef)
  - [CreateVocabularyResponseTypeDef](#createvocabularyresponsetypedef)
  - [DescribeLanguageModelResponseTypeDef](#describelanguagemodelresponsetypedef)
  - [GetMedicalTranscriptionJobResponseTypeDef](#getmedicaltranscriptionjobresponsetypedef)
  - [GetMedicalVocabularyResponseTypeDef](#getmedicalvocabularyresponsetypedef)
  - [GetTranscriptionJobResponseTypeDef](#gettranscriptionjobresponsetypedef)
  - [GetVocabularyFilterResponseTypeDef](#getvocabularyfilterresponsetypedef)
  - [GetVocabularyResponseTypeDef](#getvocabularyresponsetypedef)
  - [ListLanguageModelsResponseTypeDef](#listlanguagemodelsresponsetypedef)
  - [ListMedicalTranscriptionJobsResponseTypeDef](#listmedicaltranscriptionjobsresponsetypedef)
  - [ListMedicalVocabulariesResponseTypeDef](#listmedicalvocabulariesresponsetypedef)
  - [ListTranscriptionJobsResponseTypeDef](#listtranscriptionjobsresponsetypedef)
  - [ListVocabulariesResponseTypeDef](#listvocabulariesresponsetypedef)
  - [ListVocabularyFiltersResponseTypeDef](#listvocabularyfiltersresponsetypedef)
  - [StartMedicalTranscriptionJobResponseTypeDef](#startmedicaltranscriptionjobresponsetypedef)
  - [StartTranscriptionJobResponseTypeDef](#starttranscriptionjobresponsetypedef)
  - [UpdateMedicalVocabularyResponseTypeDef](#updatemedicalvocabularyresponsetypedef)
  - [UpdateVocabularyFilterResponseTypeDef](#updatevocabularyfilterresponsetypedef)
  - [UpdateVocabularyResponseTypeDef](#updatevocabularyresponsetypedef)

## ContentRedactionTypeDef

```python
from mypy_boto3_transcribe.type_defs import ContentRedactionTypeDef
```


Required fields:
- `RedactionType`: `RedactionType`
- `RedactionOutput`: `RedactionOutput`




## InputDataConfigTypeDef

```python
from mypy_boto3_transcribe.type_defs import InputDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`
- `DataAccessRoleArn`: `str`



Optional fields:
- `TuningDataS3Uri`: `str`


## JobExecutionSettingsTypeDef

```python
from mypy_boto3_transcribe.type_defs import JobExecutionSettingsTypeDef
```




Optional fields:
- `AllowDeferredExecution`: `bool`
- `DataAccessRoleArn`: `str`


## LanguageModelTypeDef

```python
from mypy_boto3_transcribe.type_defs import LanguageModelTypeDef
```




Optional fields:
- `ModelName`: `str`
- `CreateTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LanguageCode`: `CLMLanguageCode`
- `BaseModelName`: `BaseModelName`
- `ModelStatus`: `ModelStatus`
- `UpgradeAvailability`: `bool`
- `FailureReason`: `str`
- `InputDataConfig`: `"InputDataConfigTypeDef"`


## MediaTypeDef

```python
from mypy_boto3_transcribe.type_defs import MediaTypeDef
```




Optional fields:
- `MediaFileUri`: `str`


## MedicalTranscriptTypeDef

```python
from mypy_boto3_transcribe.type_defs import MedicalTranscriptTypeDef
```




Optional fields:
- `TranscriptFileUri`: `str`


## MedicalTranscriptionJobSummaryTypeDef

```python
from mypy_boto3_transcribe.type_defs import MedicalTranscriptionJobSummaryTypeDef
```




Optional fields:
- `MedicalTranscriptionJobName`: `str`
- `CreationTime`: `datetime`
- `StartTime`: `datetime`
- `CompletionTime`: `datetime`
- `LanguageCode`: `LanguageCode`
- `TranscriptionJobStatus`: `TranscriptionJobStatus`
- `FailureReason`: `str`
- `OutputLocationType`: `OutputLocationType`
- `Specialty`: `Specialty`
- `Type`: `TypeType`


## MedicalTranscriptionJobTypeDef

```python
from mypy_boto3_transcribe.type_defs import MedicalTranscriptionJobTypeDef
```




Optional fields:
- `MedicalTranscriptionJobName`: `str`
- `TranscriptionJobStatus`: `TranscriptionJobStatus`
- `LanguageCode`: `LanguageCode`
- `MediaSampleRateHertz`: `int`
- `MediaFormat`: `MediaFormat`
- `Media`: `"MediaTypeDef"`
- `Transcript`: `"MedicalTranscriptTypeDef"`
- `StartTime`: `datetime`
- `CreationTime`: `datetime`
- `CompletionTime`: `datetime`
- `FailureReason`: `str`
- `Settings`: `"MedicalTranscriptionSettingTypeDef"`
- `Specialty`: `Specialty`
- `Type`: `TypeType`


## MedicalTranscriptionSettingTypeDef

```python
from mypy_boto3_transcribe.type_defs import MedicalTranscriptionSettingTypeDef
```




Optional fields:
- `ShowSpeakerLabels`: `bool`
- `MaxSpeakerLabels`: `int`
- `ChannelIdentification`: `bool`
- `ShowAlternatives`: `bool`
- `MaxAlternatives`: `int`
- `VocabularyName`: `str`


## ModelSettingsTypeDef

```python
from mypy_boto3_transcribe.type_defs import ModelSettingsTypeDef
```




Optional fields:
- `LanguageModelName`: `str`


## SettingsTypeDef

```python
from mypy_boto3_transcribe.type_defs import SettingsTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `ShowSpeakerLabels`: `bool`
- `MaxSpeakerLabels`: `int`
- `ChannelIdentification`: `bool`
- `ShowAlternatives`: `bool`
- `MaxAlternatives`: `int`
- `VocabularyFilterName`: `str`
- `VocabularyFilterMethod`: `VocabularyFilterMethod`


## TranscriptTypeDef

```python
from mypy_boto3_transcribe.type_defs import TranscriptTypeDef
```




Optional fields:
- `TranscriptFileUri`: `str`
- `RedactedTranscriptFileUri`: `str`


## TranscriptionJobSummaryTypeDef

```python
from mypy_boto3_transcribe.type_defs import TranscriptionJobSummaryTypeDef
```




Optional fields:
- `TranscriptionJobName`: `str`
- `CreationTime`: `datetime`
- `StartTime`: `datetime`
- `CompletionTime`: `datetime`
- `LanguageCode`: `LanguageCode`
- `TranscriptionJobStatus`: `TranscriptionJobStatus`
- `FailureReason`: `str`
- `OutputLocationType`: `OutputLocationType`
- `ContentRedaction`: `"ContentRedactionTypeDef"`
- `ModelSettings`: `"ModelSettingsTypeDef"`
- `IdentifyLanguage`: `bool`
- `IdentifiedLanguageScore`: `float`


## TranscriptionJobTypeDef

```python
from mypy_boto3_transcribe.type_defs import TranscriptionJobTypeDef
```




Optional fields:
- `TranscriptionJobName`: `str`
- `TranscriptionJobStatus`: `TranscriptionJobStatus`
- `LanguageCode`: `LanguageCode`
- `MediaSampleRateHertz`: `int`
- `MediaFormat`: `MediaFormat`
- `Media`: `"MediaTypeDef"`
- `Transcript`: `"TranscriptTypeDef"`
- `StartTime`: `datetime`
- `CreationTime`: `datetime`
- `CompletionTime`: `datetime`
- `FailureReason`: `str`
- `Settings`: `"SettingsTypeDef"`
- `ModelSettings`: `"ModelSettingsTypeDef"`
- `JobExecutionSettings`: `"JobExecutionSettingsTypeDef"`
- `ContentRedaction`: `"ContentRedactionTypeDef"`
- `IdentifyLanguage`: `bool`
- `LanguageOptions`: `List[LanguageCode]`
- `IdentifiedLanguageScore`: `float`


## VocabularyFilterInfoTypeDef

```python
from mypy_boto3_transcribe.type_defs import VocabularyFilterInfoTypeDef
```




Optional fields:
- `VocabularyFilterName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`


## VocabularyInfoTypeDef

```python
from mypy_boto3_transcribe.type_defs import VocabularyInfoTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`
- `VocabularyState`: `VocabularyState`


## CreateLanguageModelResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import CreateLanguageModelResponseTypeDef
```




Optional fields:
- `LanguageCode`: `CLMLanguageCode`
- `BaseModelName`: `BaseModelName`
- `ModelName`: `str`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `ModelStatus`: `ModelStatus`


## CreateMedicalVocabularyResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import CreateMedicalVocabularyResponseTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `VocabularyState`: `VocabularyState`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`


## CreateVocabularyFilterResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import CreateVocabularyFilterResponseTypeDef
```




Optional fields:
- `VocabularyFilterName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`


## CreateVocabularyResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import CreateVocabularyResponseTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `VocabularyState`: `VocabularyState`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`


## DescribeLanguageModelResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import DescribeLanguageModelResponseTypeDef
```




Optional fields:
- `LanguageModel`: `"LanguageModelTypeDef"`


## GetMedicalTranscriptionJobResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import GetMedicalTranscriptionJobResponseTypeDef
```




Optional fields:
- `MedicalTranscriptionJob`: `"MedicalTranscriptionJobTypeDef"`


## GetMedicalVocabularyResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import GetMedicalVocabularyResponseTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `VocabularyState`: `VocabularyState`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`
- `DownloadUri`: `str`


## GetTranscriptionJobResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import GetTranscriptionJobResponseTypeDef
```




Optional fields:
- `TranscriptionJob`: `"TranscriptionJobTypeDef"`


## GetVocabularyFilterResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import GetVocabularyFilterResponseTypeDef
```




Optional fields:
- `VocabularyFilterName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`
- `DownloadUri`: `str`


## GetVocabularyResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import GetVocabularyResponseTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `VocabularyState`: `VocabularyState`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`
- `DownloadUri`: `str`


## ListLanguageModelsResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import ListLanguageModelsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Models`: `List["LanguageModelTypeDef"]`


## ListMedicalTranscriptionJobsResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import ListMedicalTranscriptionJobsResponseTypeDef
```




Optional fields:
- `Status`: `TranscriptionJobStatus`
- `NextToken`: `str`
- `MedicalTranscriptionJobSummaries`: `List["MedicalTranscriptionJobSummaryTypeDef"]`


## ListMedicalVocabulariesResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import ListMedicalVocabulariesResponseTypeDef
```




Optional fields:
- `Status`: `VocabularyState`
- `NextToken`: `str`
- `Vocabularies`: `List["VocabularyInfoTypeDef"]`


## ListTranscriptionJobsResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import ListTranscriptionJobsResponseTypeDef
```




Optional fields:
- `Status`: `TranscriptionJobStatus`
- `NextToken`: `str`
- `TranscriptionJobSummaries`: `List["TranscriptionJobSummaryTypeDef"]`


## ListVocabulariesResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import ListVocabulariesResponseTypeDef
```




Optional fields:
- `Status`: `VocabularyState`
- `NextToken`: `str`
- `Vocabularies`: `List["VocabularyInfoTypeDef"]`


## ListVocabularyFiltersResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import ListVocabularyFiltersResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `VocabularyFilters`: `List["VocabularyFilterInfoTypeDef"]`


## StartMedicalTranscriptionJobResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import StartMedicalTranscriptionJobResponseTypeDef
```




Optional fields:
- `MedicalTranscriptionJob`: `"MedicalTranscriptionJobTypeDef"`


## StartTranscriptionJobResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import StartTranscriptionJobResponseTypeDef
```




Optional fields:
- `TranscriptionJob`: `"TranscriptionJobTypeDef"`


## UpdateMedicalVocabularyResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import UpdateMedicalVocabularyResponseTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`
- `VocabularyState`: `VocabularyState`


## UpdateVocabularyFilterResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import UpdateVocabularyFilterResponseTypeDef
```




Optional fields:
- `VocabularyFilterName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`


## UpdateVocabularyResponseTypeDef

```python
from mypy_boto3_transcribe.type_defs import UpdateVocabularyResponseTypeDef
```




Optional fields:
- `VocabularyName`: `str`
- `LanguageCode`: `LanguageCode`
- `LastModifiedTime`: `datetime`
- `VocabularyState`: `VocabularyState`

