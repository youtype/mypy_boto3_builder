# Structures for boto3 Macie module

> [Index](../index.md) > [Macie](./index.md) > Structures

Auto-generated documentation for [Macie](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie)
type annotations stubs module [mypy_boto3_macie](https://pypi.org/project/mypy-boto3-macie/).

- [Structures for boto3 Macie module](#structures-for-boto3-macie-module)
  - [ClassificationTypeTypeDef](#classificationtypetypedef)
  - [ClassificationTypeUpdateTypeDef](#classificationtypeupdatetypedef)
  - [FailedS3ResourceTypeDef](#faileds3resourcetypedef)
  - [MemberAccountTypeDef](#memberaccounttypedef)
  - [S3ResourceClassificationTypeDef](#s3resourceclassificationtypedef)
  - [S3ResourceTypeDef](#s3resourcetypedef)
  - [AssociateS3ResourcesResultTypeDef](#associates3resourcesresulttypedef)
  - [DisassociateS3ResourcesResultTypeDef](#disassociates3resourcesresulttypedef)
  - [ListMemberAccountsResultTypeDef](#listmemberaccountsresulttypedef)
  - [ListS3ResourcesResultTypeDef](#lists3resourcesresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [S3ResourceClassificationUpdateTypeDef](#s3resourceclassificationupdatetypedef)
  - [UpdateS3ResourcesResultTypeDef](#updates3resourcesresulttypedef)

## ClassificationTypeTypeDef

```python
from mypy_boto3_macie.type_defs import ClassificationTypeTypeDef
```


Required fields:
- `oneTime`: `S3OneTimeClassificationType`
- `continuous`: `S3ContinuousClassificationType`




## ClassificationTypeUpdateTypeDef

```python
from mypy_boto3_macie.type_defs import ClassificationTypeUpdateTypeDef
```




Optional fields:
- `oneTime`: `S3OneTimeClassificationType`
- `continuous`: `S3ContinuousClassificationType`


## FailedS3ResourceTypeDef

```python
from mypy_boto3_macie.type_defs import FailedS3ResourceTypeDef
```




Optional fields:
- `failedItem`: `"S3ResourceTypeDef"`
- `errorCode`: `str`
- `errorMessage`: `str`


## MemberAccountTypeDef

```python
from mypy_boto3_macie.type_defs import MemberAccountTypeDef
```




Optional fields:
- `accountId`: `str`


## S3ResourceClassificationTypeDef

```python
from mypy_boto3_macie.type_defs import S3ResourceClassificationTypeDef
```


Required fields:
- `bucketName`: `str`
- `classificationType`: `"ClassificationTypeTypeDef"`



Optional fields:
- `prefix`: `str`


## S3ResourceTypeDef

```python
from mypy_boto3_macie.type_defs import S3ResourceTypeDef
```


Required fields:
- `bucketName`: `str`



Optional fields:
- `prefix`: `str`


## AssociateS3ResourcesResultTypeDef

```python
from mypy_boto3_macie.type_defs import AssociateS3ResourcesResultTypeDef
```




Optional fields:
- `failedS3Resources`: `List["FailedS3ResourceTypeDef"]`


## DisassociateS3ResourcesResultTypeDef

```python
from mypy_boto3_macie.type_defs import DisassociateS3ResourcesResultTypeDef
```




Optional fields:
- `failedS3Resources`: `List["FailedS3ResourceTypeDef"]`


## ListMemberAccountsResultTypeDef

```python
from mypy_boto3_macie.type_defs import ListMemberAccountsResultTypeDef
```




Optional fields:
- `memberAccounts`: `List["MemberAccountTypeDef"]`
- `nextToken`: `str`


## ListS3ResourcesResultTypeDef

```python
from mypy_boto3_macie.type_defs import ListS3ResourcesResultTypeDef
```




Optional fields:
- `s3Resources`: `List["S3ResourceClassificationTypeDef"]`
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_macie.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## S3ResourceClassificationUpdateTypeDef

```python
from mypy_boto3_macie.type_defs import S3ResourceClassificationUpdateTypeDef
```


Required fields:
- `bucketName`: `str`
- `classificationTypeUpdate`: `"ClassificationTypeUpdateTypeDef"`



Optional fields:
- `prefix`: `str`


## UpdateS3ResourcesResultTypeDef

```python
from mypy_boto3_macie.type_defs import UpdateS3ResourcesResultTypeDef
```




Optional fields:
- `failedS3Resources`: `List["FailedS3ResourceTypeDef"]`

