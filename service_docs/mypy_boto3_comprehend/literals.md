# Literals for boto3 Comprehend module

> [Index](../index.md) > [Comprehend](./index.md) > Literals

Auto-generated documentation for [Comprehend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend)
type annotations stubs module [mypy_boto3_comprehend](https://pypi.org/project/mypy-boto3-comprehend/).

- [Literals for boto3 Comprehend module](#literals-for-boto3-comprehend-module)
  - [DocumentClassifierDataFormat](#documentclassifierdataformat)
  - [DocumentClassifierMode](#documentclassifiermode)
  - [EndpointStatus](#endpointstatus)
  - [EntityRecognizerDataFormat](#entityrecognizerdataformat)
  - [EntityType](#entitytype)
  - [InputFormat](#inputformat)
  - [JobStatus](#jobstatus)
  - [LanguageCode](#languagecode)
  - [ListDocumentClassificationJobsPaginatorName](#listdocumentclassificationjobspaginatorname)
  - [ListDocumentClassifiersPaginatorName](#listdocumentclassifierspaginatorname)
  - [ListDominantLanguageDetectionJobsPaginatorName](#listdominantlanguagedetectionjobspaginatorname)
  - [ListEntitiesDetectionJobsPaginatorName](#listentitiesdetectionjobspaginatorname)
  - [ListEntityRecognizersPaginatorName](#listentityrecognizerspaginatorname)
  - [ListKeyPhrasesDetectionJobsPaginatorName](#listkeyphrasesdetectionjobspaginatorname)
  - [ListSentimentDetectionJobsPaginatorName](#listsentimentdetectionjobspaginatorname)
  - [ListTopicsDetectionJobsPaginatorName](#listtopicsdetectionjobspaginatorname)
  - [ModelStatus](#modelstatus)
  - [PartOfSpeechTagType](#partofspeechtagtype)
  - [PiiEntitiesDetectionMaskMode](#piientitiesdetectionmaskmode)
  - [PiiEntitiesDetectionMode](#piientitiesdetectionmode)
  - [PiiEntityType](#piientitytype)
  - [SentimentType](#sentimenttype)
  - [SyntaxLanguageCode](#syntaxlanguagecode)

## DocumentClassifierDataFormat

```python
from mypy_boto3_comprehend.literals import DocumentClassifierDataFormat
```

Values:

- `AUGMENTED_MANIFEST`
- `COMPREHEND_CSV`

## DocumentClassifierMode

```python
from mypy_boto3_comprehend.literals import DocumentClassifierMode
```

Values:

- `MULTI_CLASS`
- `MULTI_LABEL`

## EndpointStatus

```python
from mypy_boto3_comprehend.literals import EndpointStatus
```

Values:

- `CREATING`
- `DELETING`
- `FAILED`
- `IN_SERVICE`
- `UPDATING`

## EntityRecognizerDataFormat

```python
from mypy_boto3_comprehend.literals import EntityRecognizerDataFormat
```

Values:

- `AUGMENTED_MANIFEST`
- `COMPREHEND_CSV`

## EntityType

```python
from mypy_boto3_comprehend.literals import EntityType
```

Values:

- `COMMERCIAL_ITEM`
- `DATE`
- `EVENT`
- `LOCATION`
- `ORGANIZATION`
- `OTHER`
- `PERSON`
- `QUANTITY`
- `TITLE`

## InputFormat

```python
from mypy_boto3_comprehend.literals import InputFormat
```

Values:

- `ONE_DOC_PER_FILE`
- `ONE_DOC_PER_LINE`

## JobStatus

```python
from mypy_boto3_comprehend.literals import JobStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`
- `STOP_REQUESTED`
- `STOPPED`
- `SUBMITTED`

## LanguageCode

```python
from mypy_boto3_comprehend.literals import LanguageCode
```

Values:

- `ar`
- `de`
- `en`
- `es`
- `fr`
- `hi`
- `it`
- `ja`
- `ko`
- `pt`
- `zh`
- `zh-TW`

## ListDocumentClassificationJobsPaginatorName

```python
from mypy_boto3_comprehend.literals import ListDocumentClassificationJobsPaginatorName
```

Values:

- `list_document_classification_jobs`

## ListDocumentClassifiersPaginatorName

```python
from mypy_boto3_comprehend.literals import ListDocumentClassifiersPaginatorName
```

Values:

- `list_document_classifiers`

## ListDominantLanguageDetectionJobsPaginatorName

```python
from mypy_boto3_comprehend.literals import ListDominantLanguageDetectionJobsPaginatorName
```

Values:

- `list_dominant_language_detection_jobs`

## ListEntitiesDetectionJobsPaginatorName

```python
from mypy_boto3_comprehend.literals import ListEntitiesDetectionJobsPaginatorName
```

Values:

- `list_entities_detection_jobs`

## ListEntityRecognizersPaginatorName

```python
from mypy_boto3_comprehend.literals import ListEntityRecognizersPaginatorName
```

Values:

- `list_entity_recognizers`

## ListKeyPhrasesDetectionJobsPaginatorName

```python
from mypy_boto3_comprehend.literals import ListKeyPhrasesDetectionJobsPaginatorName
```

Values:

- `list_key_phrases_detection_jobs`

## ListSentimentDetectionJobsPaginatorName

```python
from mypy_boto3_comprehend.literals import ListSentimentDetectionJobsPaginatorName
```

Values:

- `list_sentiment_detection_jobs`

## ListTopicsDetectionJobsPaginatorName

```python
from mypy_boto3_comprehend.literals import ListTopicsDetectionJobsPaginatorName
```

Values:

- `list_topics_detection_jobs`

## ModelStatus

```python
from mypy_boto3_comprehend.literals import ModelStatus
```

Values:

- `DELETING`
- `IN_ERROR`
- `STOP_REQUESTED`
- `STOPPED`
- `SUBMITTED`
- `TRAINED`
- `TRAINING`

## PartOfSpeechTagType

```python
from mypy_boto3_comprehend.literals import PartOfSpeechTagType
```

Values:

- `ADJ`
- `ADP`
- `ADV`
- `AUX`
- `CCONJ`
- `CONJ`
- `DET`
- `INTJ`
- `NOUN`
- `NUM`
- `O`
- `PART`
- `PRON`
- `PROPN`
- `PUNCT`
- `SCONJ`
- `SYM`
- `VERB`

## PiiEntitiesDetectionMaskMode

```python
from mypy_boto3_comprehend.literals import PiiEntitiesDetectionMaskMode
```

Values:

- `MASK`
- `REPLACE_WITH_PII_ENTITY_TYPE`

## PiiEntitiesDetectionMode

```python
from mypy_boto3_comprehend.literals import PiiEntitiesDetectionMode
```

Values:

- `ONLY_OFFSETS`
- `ONLY_REDACTION`

## PiiEntityType

```python
from mypy_boto3_comprehend.literals import PiiEntityType
```

Values:

- `ADDRESS`
- `AGE`
- `ALL`
- `AWS_ACCESS_KEY`
- `AWS_SECRET_KEY`
- `BANK_ACCOUNT_NUMBER`
- `BANK_ROUTING`
- `CREDIT_DEBIT_CVV`
- `CREDIT_DEBIT_EXPIRY`
- `CREDIT_DEBIT_NUMBER`
- `DATE_TIME`
- `DRIVER_ID`
- `EMAIL`
- `IP_ADDRESS`
- `MAC_ADDRESS`
- `NAME`
- `PASSPORT_NUMBER`
- `PASSWORD`
- `PHONE`
- `PIN`
- `SSN`
- `URL`
- `USERNAME`

## SentimentType

```python
from mypy_boto3_comprehend.literals import SentimentType
```

Values:

- `MIXED`
- `NEGATIVE`
- `NEUTRAL`
- `POSITIVE`

## SyntaxLanguageCode

```python
from mypy_boto3_comprehend.literals import SyntaxLanguageCode
```

Values:

- `de`
- `en`
- `es`
- `fr`
- `it`
- `pt`
