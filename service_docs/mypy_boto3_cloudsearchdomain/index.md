# Type annotations for boto3 CloudSearchDomain module

> [Index](../index.md) > CloudSearchDomain

Auto-generated documentation for [CloudSearchDomain](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html#CloudSearchDomain)
type annotations stubs module [mypy_boto3_cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain/).

```bash
pip install mypy-boto3-cloudsearchdomain
```

- [Type annotations for boto3 CloudSearchDomain module](#type-annotations-for-boto3-cloudsearchdomain-module)
  - [CloudSearchDomainClient](#cloudsearchdomainclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudSearchDomainClient

Type annotations for  `boto3.client("cloudsearchdomain")` as [CloudSearchDomainClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudsearchdomain.client import CloudSearchDomainClient
```


CloudSearchDomainClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [search](./client.md#search)
- [suggest](./client.md#suggest)
- [upload_documents](./client.md#upload-documents)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DocumentServiceException](./client.md#documentserviceexception)
- [SearchException](./client.md#searchexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudsearchdomain.literals import ContentType, ...
```

- [ContentType](./literals.md#contenttype)
- [QueryParser](./literals.md#queryparser)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef, ...
```

- [BucketInfoTypeDef](./type_defs.md#bucketinfotypedef)
- [BucketTypeDef](./type_defs.md#buckettypedef)
- [DocumentServiceWarningTypeDef](./type_defs.md#documentservicewarningtypedef)
- [FieldStatsTypeDef](./type_defs.md#fieldstatstypedef)
- [HitTypeDef](./type_defs.md#hittypedef)
- [HitsTypeDef](./type_defs.md#hitstypedef)
- [SearchStatusTypeDef](./type_defs.md#searchstatustypedef)
- [SuggestModelTypeDef](./type_defs.md#suggestmodeltypedef)
- [SuggestStatusTypeDef](./type_defs.md#suggeststatustypedef)
- [SuggestionMatchTypeDef](./type_defs.md#suggestionmatchtypedef)
- [SearchResponseTypeDef](./type_defs.md#searchresponsetypedef)
- [SuggestResponseTypeDef](./type_defs.md#suggestresponsetypedef)
- [UploadDocumentsResponseTypeDef](./type_defs.md#uploaddocumentsresponsetypedef)
