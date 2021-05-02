# Literals for boto3 Glacier module

> [Index](../index.md) > [Glacier](./index.md) > Literals

Auto-generated documentation for [Glacier](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier)
type annotations stubs module [mypy_boto3_glacier](https://pypi.org/project/mypy-boto3-glacier/).

- [Literals for boto3 Glacier module](#literals-for-boto3-glacier-module)
  - [ActionCode](#actioncode)
  - [CannedACL](#cannedacl)
  - [EncryptionType](#encryptiontype)
  - [ExpressionType](#expressiontype)
  - [FileHeaderInfo](#fileheaderinfo)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [ListMultipartUploadsPaginatorName](#listmultipartuploadspaginatorname)
  - [ListPartsPaginatorName](#listpartspaginatorname)
  - [ListVaultsPaginatorName](#listvaultspaginatorname)
  - [Permission](#permission)
  - [QuoteFields](#quotefields)
  - [StatusCode](#statuscode)
  - [StorageClass](#storageclass)
  - [TypeType](#typetype)
  - [VaultExistsWaiterName](#vaultexistswaitername)
  - [VaultNotExistsWaiterName](#vaultnotexistswaitername)

## ActionCode

```python
from mypy_boto3_glacier.literals import ActionCode
```

Values:

- `ArchiveRetrieval`
- `InventoryRetrieval`
- `Select`

## CannedACL

```python
from mypy_boto3_glacier.literals import CannedACL
```

Values:

- `authenticated-read`
- `aws-exec-read`
- `bucket-owner-full-control`
- `bucket-owner-read`
- `private`
- `public-read`
- `public-read-write`

## EncryptionType

```python
from mypy_boto3_glacier.literals import EncryptionType
```

Values:

- `AES256`
- `aws:kms`

## ExpressionType

```python
from mypy_boto3_glacier.literals import ExpressionType
```

Values:

- `SQL`

## FileHeaderInfo

```python
from mypy_boto3_glacier.literals import FileHeaderInfo
```

Values:

- `IGNORE`
- `NONE`
- `USE`

## ListJobsPaginatorName

```python
from mypy_boto3_glacier.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## ListMultipartUploadsPaginatorName

```python
from mypy_boto3_glacier.literals import ListMultipartUploadsPaginatorName
```

Values:

- `list_multipart_uploads`

## ListPartsPaginatorName

```python
from mypy_boto3_glacier.literals import ListPartsPaginatorName
```

Values:

- `list_parts`

## ListVaultsPaginatorName

```python
from mypy_boto3_glacier.literals import ListVaultsPaginatorName
```

Values:

- `list_vaults`

## Permission

```python
from mypy_boto3_glacier.literals import Permission
```

Values:

- `FULL_CONTROL`
- `READ`
- `READ_ACP`
- `WRITE`
- `WRITE_ACP`

## QuoteFields

```python
from mypy_boto3_glacier.literals import QuoteFields
```

Values:

- `ALWAYS`
- `ASNEEDED`

## StatusCode

```python
from mypy_boto3_glacier.literals import StatusCode
```

Values:

- `Failed`
- `InProgress`
- `Succeeded`

## StorageClass

```python
from mypy_boto3_glacier.literals import StorageClass
```

Values:

- `REDUCED_REDUNDANCY`
- `STANDARD`
- `STANDARD_IA`

## TypeType

```python
from mypy_boto3_glacier.literals import TypeType
```

Values:

- `AmazonCustomerByEmail`
- `CanonicalUser`
- `Group`

## VaultExistsWaiterName

```python
from mypy_boto3_glacier.literals import VaultExistsWaiterName
```

Values:

- `vault_exists`

## VaultNotExistsWaiterName

```python
from mypy_boto3_glacier.literals import VaultNotExistsWaiterName
```

Values:

- `vault_not_exists`
