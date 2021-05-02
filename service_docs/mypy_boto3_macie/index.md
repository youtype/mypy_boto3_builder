# Type annotations for boto3 Macie module

> [Index](../index.md) > Macie

Auto-generated documentation for [Macie](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie)
type annotations stubs module [mypy_boto3_macie](https://pypi.org/project/mypy-boto3-macie/).

```bash
pip install mypy-boto3-macie
```

- [Type annotations for boto3 Macie module](#type-annotations-for-boto3-macie-module)
  - [MacieClient](#macieclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MacieClient

Type annotations for  `boto3.client("macie")` as [MacieClient](./client.md)

Can be used directly:

```python
from mypy_boto3_macie.client import MacieClient
```


MacieClient [exceptions](./client.md#exceptions)



### Methods
- [associate_member_account](./client.md#associate-member-account)
- [associate_s3_resources](./client.md#associate-s3-resources)
- [can_paginate](./client.md#can-paginate)
- [disassociate_member_account](./client.md#disassociate-member-account)
- [disassociate_s3_resources](./client.md#disassociate-s3-resources)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_member_accounts](./client.md#list-member-accounts)
- [list_s3_resources](./client.md#list-s3-resources)
- [update_s3_resources](./client.md#update-s3-resources)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalException](./client.md#internalexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [LimitExceededException](./client.md#limitexceededexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("macie").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_macie.paginators import ListMemberAccountsPaginator, ...
```

- [ListMemberAccountsPaginator](./paginators.md#listmemberaccountspaginator)
- [ListS3ResourcesPaginator](./paginators.md#lists3resourcespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_macie.literals import ListMemberAccountsPaginatorName, ...
```

- [ListMemberAccountsPaginatorName](./literals.md#listmemberaccountspaginatorname)
- [ListS3ResourcesPaginatorName](./literals.md#lists3resourcespaginatorname)
- [S3ContinuousClassificationType](./literals.md#s3continuousclassificationtype)
- [S3OneTimeClassificationType](./literals.md#s3onetimeclassificationtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_macie.type_defs import AssociateS3ResourcesResultTypeDef, ...
```

- [AssociateS3ResourcesResultTypeDef](./type_defs.md#associates3resourcesresulttypedef)
- [ClassificationTypeTypeDef](./type_defs.md#classificationtypetypedef)
- [ClassificationTypeUpdateTypeDef](./type_defs.md#classificationtypeupdatetypedef)
- [DisassociateS3ResourcesResultTypeDef](./type_defs.md#disassociates3resourcesresulttypedef)
- [FailedS3ResourceTypeDef](./type_defs.md#faileds3resourcetypedef)
- [ListMemberAccountsResultTypeDef](./type_defs.md#listmemberaccountsresulttypedef)
- [ListS3ResourcesResultTypeDef](./type_defs.md#lists3resourcesresulttypedef)
- [MemberAccountTypeDef](./type_defs.md#memberaccounttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [S3ResourceClassificationTypeDef](./type_defs.md#s3resourceclassificationtypedef)
- [S3ResourceClassificationUpdateTypeDef](./type_defs.md#s3resourceclassificationupdatetypedef)
- [S3ResourceTypeDef](./type_defs.md#s3resourcetypedef)
- [UpdateS3ResourcesResultTypeDef](./type_defs.md#updates3resourcesresulttypedef)
