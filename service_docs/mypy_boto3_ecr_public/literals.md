# Literals for boto3 ECRPublic module

> [Index](../index.md) > [ECRPublic](./index.md) > Literals

Auto-generated documentation for [ECRPublic](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html#ECRPublic)
type annotations stubs module [mypy_boto3_ecr_public](https://pypi.org/project/mypy-boto3-ecr-public/).

- [Literals for boto3 ECRPublic module](#literals-for-boto3-ecrpublic-module)
  - [DescribeImageTagsPaginatorName](#describeimagetagspaginatorname)
  - [DescribeImagesPaginatorName](#describeimagespaginatorname)
  - [DescribeRegistriesPaginatorName](#describeregistriespaginatorname)
  - [DescribeRepositoriesPaginatorName](#describerepositoriespaginatorname)
  - [ImageFailureCode](#imagefailurecode)
  - [LayerAvailability](#layeravailability)
  - [LayerFailureCode](#layerfailurecode)
  - [RegistryAliasStatus](#registryaliasstatus)

## DescribeImageTagsPaginatorName

```python
from mypy_boto3_ecr_public.literals import DescribeImageTagsPaginatorName
```

Values:

- `describe_image_tags`

## DescribeImagesPaginatorName

```python
from mypy_boto3_ecr_public.literals import DescribeImagesPaginatorName
```

Values:

- `describe_images`

## DescribeRegistriesPaginatorName

```python
from mypy_boto3_ecr_public.literals import DescribeRegistriesPaginatorName
```

Values:

- `describe_registries`

## DescribeRepositoriesPaginatorName

```python
from mypy_boto3_ecr_public.literals import DescribeRepositoriesPaginatorName
```

Values:

- `describe_repositories`

## ImageFailureCode

```python
from mypy_boto3_ecr_public.literals import ImageFailureCode
```

Values:

- `ImageNotFound`
- `ImageReferencedByManifestList`
- `ImageTagDoesNotMatchDigest`
- `InvalidImageDigest`
- `InvalidImageTag`
- `KmsError`
- `MissingDigestAndTag`

## LayerAvailability

```python
from mypy_boto3_ecr_public.literals import LayerAvailability
```

Values:

- `AVAILABLE`
- `UNAVAILABLE`

## LayerFailureCode

```python
from mypy_boto3_ecr_public.literals import LayerFailureCode
```

Values:

- `InvalidLayerDigest`
- `MissingLayerDigest`

## RegistryAliasStatus

```python
from mypy_boto3_ecr_public.literals import RegistryAliasStatus
```

Values:

- `ACTIVE`
- `PENDING`
- `REJECTED`
