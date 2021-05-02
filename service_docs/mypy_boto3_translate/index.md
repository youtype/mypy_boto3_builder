# Type annotations for boto3 Translate module

> [Index](../index.md) > Translate

Auto-generated documentation for [Translate](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#Translate)
type annotations stubs module [mypy_boto3_translate](https://pypi.org/project/mypy-boto3-translate/).

```bash
pip install mypy-boto3-translate
```

- [Type annotations for boto3 Translate module](#type-annotations-for-boto3-translate-module)
  - [TranslateClient](#translateclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## TranslateClient

Type annotations for  `boto3.client("translate")` as [TranslateClient](./client.md)

Can be used directly:

```python
from mypy_boto3_translate.client import TranslateClient
```


TranslateClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_parallel_data](./client.md#create-parallel-data)
- [delete_parallel_data](./client.md#delete-parallel-data)
- [delete_terminology](./client.md#delete-terminology)
- [describe_text_translation_job](./client.md#describe-text-translation-job)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_parallel_data](./client.md#get-parallel-data)
- [get_terminology](./client.md#get-terminology)
- [import_terminology](./client.md#import-terminology)
- [list_parallel_data](./client.md#list-parallel-data)
- [list_terminologies](./client.md#list-terminologies)
- [list_text_translation_jobs](./client.md#list-text-translation-jobs)
- [start_text_translation_job](./client.md#start-text-translation-job)
- [stop_text_translation_job](./client.md#stop-text-translation-job)
- [translate_text](./client.md#translate-text)
- [update_parallel_data](./client.md#update-parallel-data)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConflictException](./client.md#conflictexception)
- [DetectedLanguageLowConfidenceException](./client.md#detectedlanguagelowconfidenceexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidFilterException](./client.md#invalidfilterexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TextSizeLimitExceededException](./client.md#textsizelimitexceededexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnsupportedLanguagePairException](./client.md#unsupportedlanguagepairexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("translate").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_translate.paginators import ListTerminologiesPaginator, ...
```

- [ListTerminologiesPaginator](./paginators.md#listterminologiespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_translate.literals import EncryptionKeyType, ...
```

- [EncryptionKeyType](./literals.md#encryptionkeytype)
- [JobStatus](./literals.md#jobstatus)
- [ListTerminologiesPaginatorName](./literals.md#listterminologiespaginatorname)
- [MergeStrategy](./literals.md#mergestrategy)
- [ParallelDataFormat](./literals.md#paralleldataformat)
- [ParallelDataStatus](./literals.md#paralleldatastatus)
- [TerminologyDataFormat](./literals.md#terminologydataformat)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_translate.type_defs import AppliedTerminologyTypeDef, ...
```

- [AppliedTerminologyTypeDef](./type_defs.md#appliedterminologytypedef)
- [CreateParallelDataResponseTypeDef](./type_defs.md#createparalleldataresponsetypedef)
- [DeleteParallelDataResponseTypeDef](./type_defs.md#deleteparalleldataresponsetypedef)
- [DescribeTextTranslationJobResponseTypeDef](./type_defs.md#describetexttranslationjobresponsetypedef)
- [EncryptionKeyTypeDef](./type_defs.md#encryptionkeytypedef)
- [GetParallelDataResponseTypeDef](./type_defs.md#getparalleldataresponsetypedef)
- [GetTerminologyResponseTypeDef](./type_defs.md#getterminologyresponsetypedef)
- [ImportTerminologyResponseTypeDef](./type_defs.md#importterminologyresponsetypedef)
- [InputDataConfigTypeDef](./type_defs.md#inputdataconfigtypedef)
- [JobDetailsTypeDef](./type_defs.md#jobdetailstypedef)
- [ListParallelDataResponseTypeDef](./type_defs.md#listparalleldataresponsetypedef)
- [ListTerminologiesResponseTypeDef](./type_defs.md#listterminologiesresponsetypedef)
- [ListTextTranslationJobsResponseTypeDef](./type_defs.md#listtexttranslationjobsresponsetypedef)
- [OutputDataConfigTypeDef](./type_defs.md#outputdataconfigtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParallelDataConfigTypeDef](./type_defs.md#paralleldataconfigtypedef)
- [ParallelDataDataLocationTypeDef](./type_defs.md#paralleldatadatalocationtypedef)
- [ParallelDataPropertiesTypeDef](./type_defs.md#paralleldatapropertiestypedef)
- [StartTextTranslationJobResponseTypeDef](./type_defs.md#starttexttranslationjobresponsetypedef)
- [StopTextTranslationJobResponseTypeDef](./type_defs.md#stoptexttranslationjobresponsetypedef)
- [TermTypeDef](./type_defs.md#termtypedef)
- [TerminologyDataLocationTypeDef](./type_defs.md#terminologydatalocationtypedef)
- [TerminologyDataTypeDef](./type_defs.md#terminologydatatypedef)
- [TerminologyPropertiesTypeDef](./type_defs.md#terminologypropertiestypedef)
- [TextTranslationJobFilterTypeDef](./type_defs.md#texttranslationjobfiltertypedef)
- [TextTranslationJobPropertiesTypeDef](./type_defs.md#texttranslationjobpropertiestypedef)
- [TranslateTextResponseTypeDef](./type_defs.md#translatetextresponsetypedef)
- [UpdateParallelDataResponseTypeDef](./type_defs.md#updateparalleldataresponsetypedef)
