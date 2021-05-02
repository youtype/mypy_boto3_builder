# Structures for boto3 Translate module

> [Index](../index.md) > [Translate](./index.md) > Structures

Auto-generated documentation for [Translate](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate)
type annotations stubs module [mypy_boto3_translate](https://pypi.org/project/mypy-boto3-translate/).

- [Structures for boto3 Translate module](#structures-for-boto3-translate-module)
  - [AppliedTerminologyTypeDef](#appliedterminologytypedef)
  - [EncryptionKeyTypeDef](#encryptionkeytypedef)
  - [InputDataConfigTypeDef](#inputdataconfigtypedef)
  - [JobDetailsTypeDef](#jobdetailstypedef)
  - [OutputDataConfigTypeDef](#outputdataconfigtypedef)
  - [ParallelDataConfigTypeDef](#paralleldataconfigtypedef)
  - [ParallelDataDataLocationTypeDef](#paralleldatadatalocationtypedef)
  - [ParallelDataPropertiesTypeDef](#paralleldatapropertiestypedef)
  - [TermTypeDef](#termtypedef)
  - [TerminologyDataLocationTypeDef](#terminologydatalocationtypedef)
  - [TerminologyPropertiesTypeDef](#terminologypropertiestypedef)
  - [TextTranslationJobPropertiesTypeDef](#texttranslationjobpropertiestypedef)
  - [CreateParallelDataResponseTypeDef](#createparalleldataresponsetypedef)
  - [DeleteParallelDataResponseTypeDef](#deleteparalleldataresponsetypedef)
  - [DescribeTextTranslationJobResponseTypeDef](#describetexttranslationjobresponsetypedef)
  - [GetParallelDataResponseTypeDef](#getparalleldataresponsetypedef)
  - [GetTerminologyResponseTypeDef](#getterminologyresponsetypedef)
  - [ImportTerminologyResponseTypeDef](#importterminologyresponsetypedef)
  - [ListParallelDataResponseTypeDef](#listparalleldataresponsetypedef)
  - [ListTerminologiesResponseTypeDef](#listterminologiesresponsetypedef)
  - [ListTextTranslationJobsResponseTypeDef](#listtexttranslationjobsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [StartTextTranslationJobResponseTypeDef](#starttexttranslationjobresponsetypedef)
  - [StopTextTranslationJobResponseTypeDef](#stoptexttranslationjobresponsetypedef)
  - [TerminologyDataTypeDef](#terminologydatatypedef)
  - [TextTranslationJobFilterTypeDef](#texttranslationjobfiltertypedef)
  - [TranslateTextResponseTypeDef](#translatetextresponsetypedef)
  - [UpdateParallelDataResponseTypeDef](#updateparalleldataresponsetypedef)

## AppliedTerminologyTypeDef

```python
from mypy_boto3_translate.type_defs import AppliedTerminologyTypeDef
```




Optional fields:
- `Name`: `str`
- `Terms`: `List["TermTypeDef"]`


## EncryptionKeyTypeDef

```python
from mypy_boto3_translate.type_defs import EncryptionKeyTypeDef
```


Required fields:
- `Type`: `EncryptionKeyType`
- `Id`: `str`




## InputDataConfigTypeDef

```python
from mypy_boto3_translate.type_defs import InputDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`
- `ContentType`: `str`




## JobDetailsTypeDef

```python
from mypy_boto3_translate.type_defs import JobDetailsTypeDef
```




Optional fields:
- `TranslatedDocumentsCount`: `int`
- `DocumentsWithErrorsCount`: `int`
- `InputDocumentsCount`: `int`


## OutputDataConfigTypeDef

```python
from mypy_boto3_translate.type_defs import OutputDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`




## ParallelDataConfigTypeDef

```python
from mypy_boto3_translate.type_defs import ParallelDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`
- `Format`: `ParallelDataFormat`




## ParallelDataDataLocationTypeDef

```python
from mypy_boto3_translate.type_defs import ParallelDataDataLocationTypeDef
```


Required fields:
- `RepositoryType`: `str`
- `Location`: `str`




## ParallelDataPropertiesTypeDef

```python
from mypy_boto3_translate.type_defs import ParallelDataPropertiesTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `Description`: `str`
- `Status`: `ParallelDataStatus`
- `SourceLanguageCode`: `str`
- `TargetLanguageCodes`: `List[str]`
- `ParallelDataConfig`: `"ParallelDataConfigTypeDef"`
- `Message`: `str`
- `ImportedDataSize`: `int`
- `ImportedRecordCount`: `int`
- `FailedRecordCount`: `int`
- `SkippedRecordCount`: `int`
- `EncryptionKey`: `"EncryptionKeyTypeDef"`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `LatestUpdateAttemptStatus`: `ParallelDataStatus`
- `LatestUpdateAttemptAt`: `datetime`


## TermTypeDef

```python
from mypy_boto3_translate.type_defs import TermTypeDef
```




Optional fields:
- `SourceText`: `str`
- `TargetText`: `str`


## TerminologyDataLocationTypeDef

```python
from mypy_boto3_translate.type_defs import TerminologyDataLocationTypeDef
```


Required fields:
- `RepositoryType`: `str`
- `Location`: `str`




## TerminologyPropertiesTypeDef

```python
from mypy_boto3_translate.type_defs import TerminologyPropertiesTypeDef
```




Optional fields:
- `Name`: `str`
- `Description`: `str`
- `Arn`: `str`
- `SourceLanguageCode`: `str`
- `TargetLanguageCodes`: `List[str]`
- `EncryptionKey`: `"EncryptionKeyTypeDef"`
- `SizeBytes`: `int`
- `TermCount`: `int`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`


## TextTranslationJobPropertiesTypeDef

```python
from mypy_boto3_translate.type_defs import TextTranslationJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `JobDetails`: `"JobDetailsTypeDef"`
- `SourceLanguageCode`: `str`
- `TargetLanguageCodes`: `List[str]`
- `TerminologyNames`: `List[str]`
- `ParallelDataNames`: `List[str]`
- `Message`: `str`
- `SubmittedTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `DataAccessRoleArn`: `str`


## CreateParallelDataResponseTypeDef

```python
from mypy_boto3_translate.type_defs import CreateParallelDataResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Status`: `ParallelDataStatus`


## DeleteParallelDataResponseTypeDef

```python
from mypy_boto3_translate.type_defs import DeleteParallelDataResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Status`: `ParallelDataStatus`


## DescribeTextTranslationJobResponseTypeDef

```python
from mypy_boto3_translate.type_defs import DescribeTextTranslationJobResponseTypeDef
```




Optional fields:
- `TextTranslationJobProperties`: `"TextTranslationJobPropertiesTypeDef"`


## GetParallelDataResponseTypeDef

```python
from mypy_boto3_translate.type_defs import GetParallelDataResponseTypeDef
```




Optional fields:
- `ParallelDataProperties`: `"ParallelDataPropertiesTypeDef"`
- `DataLocation`: `"ParallelDataDataLocationTypeDef"`
- `AuxiliaryDataLocation`: `"ParallelDataDataLocationTypeDef"`
- `LatestUpdateAttemptAuxiliaryDataLocation`: `"ParallelDataDataLocationTypeDef"`


## GetTerminologyResponseTypeDef

```python
from mypy_boto3_translate.type_defs import GetTerminologyResponseTypeDef
```




Optional fields:
- `TerminologyProperties`: `"TerminologyPropertiesTypeDef"`
- `TerminologyDataLocation`: `"TerminologyDataLocationTypeDef"`


## ImportTerminologyResponseTypeDef

```python
from mypy_boto3_translate.type_defs import ImportTerminologyResponseTypeDef
```




Optional fields:
- `TerminologyProperties`: `"TerminologyPropertiesTypeDef"`


## ListParallelDataResponseTypeDef

```python
from mypy_boto3_translate.type_defs import ListParallelDataResponseTypeDef
```




Optional fields:
- `ParallelDataPropertiesList`: `List["ParallelDataPropertiesTypeDef"]`
- `NextToken`: `str`


## ListTerminologiesResponseTypeDef

```python
from mypy_boto3_translate.type_defs import ListTerminologiesResponseTypeDef
```




Optional fields:
- `TerminologyPropertiesList`: `List["TerminologyPropertiesTypeDef"]`
- `NextToken`: `str`


## ListTextTranslationJobsResponseTypeDef

```python
from mypy_boto3_translate.type_defs import ListTextTranslationJobsResponseTypeDef
```




Optional fields:
- `TextTranslationJobPropertiesList`: `List["TextTranslationJobPropertiesTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_translate.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## StartTextTranslationJobResponseTypeDef

```python
from mypy_boto3_translate.type_defs import StartTextTranslationJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopTextTranslationJobResponseTypeDef

```python
from mypy_boto3_translate.type_defs import StopTextTranslationJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## TerminologyDataTypeDef

```python
from mypy_boto3_translate.type_defs import TerminologyDataTypeDef
```


Required fields:
- `File`: `Union[bytes, IO[bytes]]`
- `Format`: `TerminologyDataFormat`




## TextTranslationJobFilterTypeDef

```python
from mypy_boto3_translate.type_defs import TextTranslationJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmittedBeforeTime`: `datetime`
- `SubmittedAfterTime`: `datetime`


## TranslateTextResponseTypeDef

```python
from mypy_boto3_translate.type_defs import TranslateTextResponseTypeDef
```


Required fields:
- `TranslatedText`: `str`
- `SourceLanguageCode`: `str`
- `TargetLanguageCode`: `str`



Optional fields:
- `AppliedTerminologies`: `List["AppliedTerminologyTypeDef"]`


## UpdateParallelDataResponseTypeDef

```python
from mypy_boto3_translate.type_defs import UpdateParallelDataResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Status`: `ParallelDataStatus`
- `LatestUpdateAttemptStatus`: `ParallelDataStatus`
- `LatestUpdateAttemptAt`: `datetime`

