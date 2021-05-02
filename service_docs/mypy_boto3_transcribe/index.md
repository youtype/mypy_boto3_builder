# Type annotations for boto3 TranscribeService module

> [Index](../index.md) > TranscribeService

Auto-generated documentation for [TranscribeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService)
type annotations stubs module [mypy_boto3_transcribe](https://pypi.org/project/mypy-boto3-transcribe/).

```bash
pip install mypy-boto3-transcribe
```

- [Type annotations for boto3 TranscribeService module](#type-annotations-for-boto3-transcribeservice-module)
  - [TranscribeServiceClient](#transcribeserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## TranscribeServiceClient

Type annotations for  `boto3.client("transcribe")` as [TranscribeServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_transcribe.client import TranscribeServiceClient
```


TranscribeServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_language_model](./client.md#create-language-model)
- [create_medical_vocabulary](./client.md#create-medical-vocabulary)
- [create_vocabulary](./client.md#create-vocabulary)
- [create_vocabulary_filter](./client.md#create-vocabulary-filter)
- [delete_language_model](./client.md#delete-language-model)
- [delete_medical_transcription_job](./client.md#delete-medical-transcription-job)
- [delete_medical_vocabulary](./client.md#delete-medical-vocabulary)
- [delete_transcription_job](./client.md#delete-transcription-job)
- [delete_vocabulary](./client.md#delete-vocabulary)
- [delete_vocabulary_filter](./client.md#delete-vocabulary-filter)
- [describe_language_model](./client.md#describe-language-model)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_medical_transcription_job](./client.md#get-medical-transcription-job)
- [get_medical_vocabulary](./client.md#get-medical-vocabulary)
- [get_transcription_job](./client.md#get-transcription-job)
- [get_vocabulary](./client.md#get-vocabulary)
- [get_vocabulary_filter](./client.md#get-vocabulary-filter)
- [list_language_models](./client.md#list-language-models)
- [list_medical_transcription_jobs](./client.md#list-medical-transcription-jobs)
- [list_medical_vocabularies](./client.md#list-medical-vocabularies)
- [list_transcription_jobs](./client.md#list-transcription-jobs)
- [list_vocabularies](./client.md#list-vocabularies)
- [list_vocabulary_filters](./client.md#list-vocabulary-filters)
- [start_medical_transcription_job](./client.md#start-medical-transcription-job)
- [start_transcription_job](./client.md#start-transcription-job)
- [update_medical_vocabulary](./client.md#update-medical-vocabulary)
- [update_vocabulary](./client.md#update-vocabulary)
- [update_vocabulary_filter](./client.md#update-vocabulary-filter)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_transcribe.literals import BaseModelName, ...
```

- [BaseModelName](./literals.md#basemodelname)
- [CLMLanguageCode](./literals.md#clmlanguagecode)
- [LanguageCode](./literals.md#languagecode)
- [MediaFormat](./literals.md#mediaformat)
- [ModelStatus](./literals.md#modelstatus)
- [OutputLocationType](./literals.md#outputlocationtype)
- [RedactionOutput](./literals.md#redactionoutput)
- [RedactionType](./literals.md#redactiontype)
- [Specialty](./literals.md#specialty)
- [TranscriptionJobStatus](./literals.md#transcriptionjobstatus)
- [TypeType](./literals.md#typetype)
- [VocabularyFilterMethod](./literals.md#vocabularyfiltermethod)
- [VocabularyState](./literals.md#vocabularystate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_transcribe.type_defs import ContentRedactionTypeDef, ...
```

- [ContentRedactionTypeDef](./type_defs.md#contentredactiontypedef)
- [CreateLanguageModelResponseTypeDef](./type_defs.md#createlanguagemodelresponsetypedef)
- [CreateMedicalVocabularyResponseTypeDef](./type_defs.md#createmedicalvocabularyresponsetypedef)
- [CreateVocabularyFilterResponseTypeDef](./type_defs.md#createvocabularyfilterresponsetypedef)
- [CreateVocabularyResponseTypeDef](./type_defs.md#createvocabularyresponsetypedef)
- [DescribeLanguageModelResponseTypeDef](./type_defs.md#describelanguagemodelresponsetypedef)
- [GetMedicalTranscriptionJobResponseTypeDef](./type_defs.md#getmedicaltranscriptionjobresponsetypedef)
- [GetMedicalVocabularyResponseTypeDef](./type_defs.md#getmedicalvocabularyresponsetypedef)
- [GetTranscriptionJobResponseTypeDef](./type_defs.md#gettranscriptionjobresponsetypedef)
- [GetVocabularyFilterResponseTypeDef](./type_defs.md#getvocabularyfilterresponsetypedef)
- [GetVocabularyResponseTypeDef](./type_defs.md#getvocabularyresponsetypedef)
- [InputDataConfigTypeDef](./type_defs.md#inputdataconfigtypedef)
- [JobExecutionSettingsTypeDef](./type_defs.md#jobexecutionsettingstypedef)
- [LanguageModelTypeDef](./type_defs.md#languagemodeltypedef)
- [ListLanguageModelsResponseTypeDef](./type_defs.md#listlanguagemodelsresponsetypedef)
- [ListMedicalTranscriptionJobsResponseTypeDef](./type_defs.md#listmedicaltranscriptionjobsresponsetypedef)
- [ListMedicalVocabulariesResponseTypeDef](./type_defs.md#listmedicalvocabulariesresponsetypedef)
- [ListTranscriptionJobsResponseTypeDef](./type_defs.md#listtranscriptionjobsresponsetypedef)
- [ListVocabulariesResponseTypeDef](./type_defs.md#listvocabulariesresponsetypedef)
- [ListVocabularyFiltersResponseTypeDef](./type_defs.md#listvocabularyfiltersresponsetypedef)
- [MediaTypeDef](./type_defs.md#mediatypedef)
- [MedicalTranscriptTypeDef](./type_defs.md#medicaltranscripttypedef)
- [MedicalTranscriptionJobSummaryTypeDef](./type_defs.md#medicaltranscriptionjobsummarytypedef)
- [MedicalTranscriptionJobTypeDef](./type_defs.md#medicaltranscriptionjobtypedef)
- [MedicalTranscriptionSettingTypeDef](./type_defs.md#medicaltranscriptionsettingtypedef)
- [ModelSettingsTypeDef](./type_defs.md#modelsettingstypedef)
- [SettingsTypeDef](./type_defs.md#settingstypedef)
- [StartMedicalTranscriptionJobResponseTypeDef](./type_defs.md#startmedicaltranscriptionjobresponsetypedef)
- [StartTranscriptionJobResponseTypeDef](./type_defs.md#starttranscriptionjobresponsetypedef)
- [TranscriptTypeDef](./type_defs.md#transcripttypedef)
- [TranscriptionJobSummaryTypeDef](./type_defs.md#transcriptionjobsummarytypedef)
- [TranscriptionJobTypeDef](./type_defs.md#transcriptionjobtypedef)
- [UpdateMedicalVocabularyResponseTypeDef](./type_defs.md#updatemedicalvocabularyresponsetypedef)
- [UpdateVocabularyFilterResponseTypeDef](./type_defs.md#updatevocabularyfilterresponsetypedef)
- [UpdateVocabularyResponseTypeDef](./type_defs.md#updatevocabularyresponsetypedef)
- [VocabularyFilterInfoTypeDef](./type_defs.md#vocabularyfilterinfotypedef)
- [VocabularyInfoTypeDef](./type_defs.md#vocabularyinfotypedef)
