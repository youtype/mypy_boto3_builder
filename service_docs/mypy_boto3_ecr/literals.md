# Literals for boto3 ECR module

> [Index](../index.md) > [ECR](./index.md) > Literals

Auto-generated documentation for [ECR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR)
type annotations stubs module [mypy_boto3_ecr](https://pypi.org/project/mypy-boto3-ecr/).

- [Literals for boto3 ECR module](#literals-for-boto3-ecr-module)
  - [DescribeImageScanFindingsPaginatorName](#describeimagescanfindingspaginatorname)
  - [DescribeImagesPaginatorName](#describeimagespaginatorname)
  - [DescribeRepositoriesPaginatorName](#describerepositoriespaginatorname)
  - [EncryptionType](#encryptiontype)
  - [FindingSeverity](#findingseverity)
  - [GetLifecyclePolicyPreviewPaginatorName](#getlifecyclepolicypreviewpaginatorname)
  - [ImageActionType](#imageactiontype)
  - [ImageFailureCode](#imagefailurecode)
  - [ImageScanCompleteWaiterName](#imagescancompletewaitername)
  - [ImageTagMutability](#imagetagmutability)
  - [LayerAvailability](#layeravailability)
  - [LayerFailureCode](#layerfailurecode)
  - [LifecyclePolicyPreviewCompleteWaiterName](#lifecyclepolicypreviewcompletewaitername)
  - [LifecyclePolicyPreviewStatus](#lifecyclepolicypreviewstatus)
  - [ListImagesPaginatorName](#listimagespaginatorname)
  - [ScanStatus](#scanstatus)
  - [TagStatus](#tagstatus)

## DescribeImageScanFindingsPaginatorName

```python
from mypy_boto3_ecr.literals import DescribeImageScanFindingsPaginatorName
```

Values:

- `describe_image_scan_findings`

## DescribeImagesPaginatorName

```python
from mypy_boto3_ecr.literals import DescribeImagesPaginatorName
```

Values:

- `describe_images`

## DescribeRepositoriesPaginatorName

```python
from mypy_boto3_ecr.literals import DescribeRepositoriesPaginatorName
```

Values:

- `describe_repositories`

## EncryptionType

```python
from mypy_boto3_ecr.literals import EncryptionType
```

Values:

- `AES256`
- `KMS`

## FindingSeverity

```python
from mypy_boto3_ecr.literals import FindingSeverity
```

Values:

- `CRITICAL`
- `HIGH`
- `INFORMATIONAL`
- `LOW`
- `MEDIUM`
- `UNDEFINED`

## GetLifecyclePolicyPreviewPaginatorName

```python
from mypy_boto3_ecr.literals import GetLifecyclePolicyPreviewPaginatorName
```

Values:

- `get_lifecycle_policy_preview`

## ImageActionType

```python
from mypy_boto3_ecr.literals import ImageActionType
```

Values:

- `EXPIRE`

## ImageFailureCode

```python
from mypy_boto3_ecr.literals import ImageFailureCode
```

Values:

- `ImageNotFound`
- `ImageReferencedByManifestList`
- `ImageTagDoesNotMatchDigest`
- `InvalidImageDigest`
- `InvalidImageTag`
- `KmsError`
- `MissingDigestAndTag`

## ImageScanCompleteWaiterName

```python
from mypy_boto3_ecr.literals import ImageScanCompleteWaiterName
```

Values:

- `image_scan_complete`

## ImageTagMutability

```python
from mypy_boto3_ecr.literals import ImageTagMutability
```

Values:

- `IMMUTABLE`
- `MUTABLE`

## LayerAvailability

```python
from mypy_boto3_ecr.literals import LayerAvailability
```

Values:

- `AVAILABLE`
- `UNAVAILABLE`

## LayerFailureCode

```python
from mypy_boto3_ecr.literals import LayerFailureCode
```

Values:

- `InvalidLayerDigest`
- `MissingLayerDigest`

## LifecyclePolicyPreviewCompleteWaiterName

```python
from mypy_boto3_ecr.literals import LifecyclePolicyPreviewCompleteWaiterName
```

Values:

- `lifecycle_policy_preview_complete`

## LifecyclePolicyPreviewStatus

```python
from mypy_boto3_ecr.literals import LifecyclePolicyPreviewStatus
```

Values:

- `COMPLETE`
- `EXPIRED`
- `FAILED`
- `IN_PROGRESS`

## ListImagesPaginatorName

```python
from mypy_boto3_ecr.literals import ListImagesPaginatorName
```

Values:

- `list_images`

## ScanStatus

```python
from mypy_boto3_ecr.literals import ScanStatus
```

Values:

- `COMPLETE`
- `FAILED`
- `IN_PROGRESS`

## TagStatus

```python
from mypy_boto3_ecr.literals import TagStatus
```

Values:

- `ANY`
- `TAGGED`
- `UNTAGGED`
