# Literals for boto3 CodeArtifact module

> [Index](../index.md) > [CodeArtifact](./index.md) > Literals

Auto-generated documentation for [CodeArtifact](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact)
type annotations stubs module [mypy_boto3_codeartifact](https://pypi.org/project/mypy-boto3-codeartifact/).

- [Literals for boto3 CodeArtifact module](#literals-for-boto3-codeartifact-module)
  - [DomainStatus](#domainstatus)
  - [ExternalConnectionStatus](#externalconnectionstatus)
  - [HashAlgorithm](#hashalgorithm)
  - [ListDomainsPaginatorName](#listdomainspaginatorname)
  - [ListPackageVersionAssetsPaginatorName](#listpackageversionassetspaginatorname)
  - [ListPackageVersionsPaginatorName](#listpackageversionspaginatorname)
  - [ListPackagesPaginatorName](#listpackagespaginatorname)
  - [ListRepositoriesInDomainPaginatorName](#listrepositoriesindomainpaginatorname)
  - [ListRepositoriesPaginatorName](#listrepositoriespaginatorname)
  - [PackageFormat](#packageformat)
  - [PackageVersionErrorCode](#packageversionerrorcode)
  - [PackageVersionSortType](#packageversionsorttype)
  - [PackageVersionStatus](#packageversionstatus)

## DomainStatus

```python
from mypy_boto3_codeartifact.literals import DomainStatus
```

Values:

- `Active`
- `Deleted`

## ExternalConnectionStatus

```python
from mypy_boto3_codeartifact.literals import ExternalConnectionStatus
```

Values:

- `Available`

## HashAlgorithm

```python
from mypy_boto3_codeartifact.literals import HashAlgorithm
```

Values:

- `MD5`
- `SHA-1`
- `SHA-256`
- `SHA-512`

## ListDomainsPaginatorName

```python
from mypy_boto3_codeartifact.literals import ListDomainsPaginatorName
```

Values:

- `list_domains`

## ListPackageVersionAssetsPaginatorName

```python
from mypy_boto3_codeartifact.literals import ListPackageVersionAssetsPaginatorName
```

Values:

- `list_package_version_assets`

## ListPackageVersionsPaginatorName

```python
from mypy_boto3_codeartifact.literals import ListPackageVersionsPaginatorName
```

Values:

- `list_package_versions`

## ListPackagesPaginatorName

```python
from mypy_boto3_codeartifact.literals import ListPackagesPaginatorName
```

Values:

- `list_packages`

## ListRepositoriesInDomainPaginatorName

```python
from mypy_boto3_codeartifact.literals import ListRepositoriesInDomainPaginatorName
```

Values:

- `list_repositories_in_domain`

## ListRepositoriesPaginatorName

```python
from mypy_boto3_codeartifact.literals import ListRepositoriesPaginatorName
```

Values:

- `list_repositories`

## PackageFormat

```python
from mypy_boto3_codeartifact.literals import PackageFormat
```

Values:

- `maven`
- `npm`
- `nuget`
- `pypi`

## PackageVersionErrorCode

```python
from mypy_boto3_codeartifact.literals import PackageVersionErrorCode
```

Values:

- `ALREADY_EXISTS`
- `MISMATCHED_REVISION`
- `MISMATCHED_STATUS`
- `NOT_ALLOWED`
- `NOT_FOUND`
- `SKIPPED`

## PackageVersionSortType

```python
from mypy_boto3_codeartifact.literals import PackageVersionSortType
```

Values:

- `PUBLISHED_TIME`

## PackageVersionStatus

```python
from mypy_boto3_codeartifact.literals import PackageVersionStatus
```

Values:

- `Archived`
- `Deleted`
- `Disposed`
- `Published`
- `Unfinished`
- `Unlisted`
