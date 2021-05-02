# Literals for boto3 Signer module

> [Index](../index.md) > [Signer](./index.md) > Literals

Auto-generated documentation for [Signer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer)
type annotations stubs module [mypy_boto3_signer](https://pypi.org/project/mypy-boto3-signer/).

- [Literals for boto3 Signer module](#literals-for-boto3-signer-module)
  - [Category](#category)
  - [EncryptionAlgorithm](#encryptionalgorithm)
  - [HashAlgorithm](#hashalgorithm)
  - [ImageFormat](#imageformat)
  - [ListSigningJobsPaginatorName](#listsigningjobspaginatorname)
  - [ListSigningPlatformsPaginatorName](#listsigningplatformspaginatorname)
  - [ListSigningProfilesPaginatorName](#listsigningprofilespaginatorname)
  - [SigningProfileStatus](#signingprofilestatus)
  - [SigningStatus](#signingstatus)
  - [SuccessfulSigningJobWaiterName](#successfulsigningjobwaitername)
  - [ValidityType](#validitytype)

## Category

```python
from mypy_boto3_signer.literals import Category
```

Values:

- `AWSIoT`

## EncryptionAlgorithm

```python
from mypy_boto3_signer.literals import EncryptionAlgorithm
```

Values:

- `ECDSA`
- `RSA`

## HashAlgorithm

```python
from mypy_boto3_signer.literals import HashAlgorithm
```

Values:

- `SHA1`
- `SHA256`

## ImageFormat

```python
from mypy_boto3_signer.literals import ImageFormat
```

Values:

- `JSON`
- `JSONDetached`
- `JSONEmbedded`

## ListSigningJobsPaginatorName

```python
from mypy_boto3_signer.literals import ListSigningJobsPaginatorName
```

Values:

- `list_signing_jobs`

## ListSigningPlatformsPaginatorName

```python
from mypy_boto3_signer.literals import ListSigningPlatformsPaginatorName
```

Values:

- `list_signing_platforms`

## ListSigningProfilesPaginatorName

```python
from mypy_boto3_signer.literals import ListSigningProfilesPaginatorName
```

Values:

- `list_signing_profiles`

## SigningProfileStatus

```python
from mypy_boto3_signer.literals import SigningProfileStatus
```

Values:

- `Active`
- `Canceled`
- `Revoked`

## SigningStatus

```python
from mypy_boto3_signer.literals import SigningStatus
```

Values:

- `Failed`
- `InProgress`
- `Succeeded`

## SuccessfulSigningJobWaiterName

```python
from mypy_boto3_signer.literals import SuccessfulSigningJobWaiterName
```

Values:

- `successful_signing_job`

## ValidityType

```python
from mypy_boto3_signer.literals import ValidityType
```

Values:

- `DAYS`
- `MONTHS`
- `YEARS`
