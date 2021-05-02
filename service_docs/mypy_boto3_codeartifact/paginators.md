# Paginators for boto3 CodeArtifact module

> [Index](../index.md) > [CodeArtifact](./index.md) > Paginators

Auto-generated documentation for [CodeArtifact](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact)
type annotations stubs module [mypy_boto3_codeartifact](https://pypi.org/project/mypy-boto3-codeartifact/).

- [Paginators for boto3 CodeArtifact module](#paginators-for-boto3-codeartifact-module)
  - [ListDomainsPaginator](#listdomainspaginator)
  - [ListPackageVersionAssetsPaginator](#listpackageversionassetspaginator)
  - [ListPackageVersionsPaginator](#listpackageversionspaginator)
  - [ListPackagesPaginator](#listpackagespaginator)
  - [ListRepositoriesPaginator](#listrepositoriespaginator)
  - [ListRepositoriesInDomainPaginator](#listrepositoriesindomainpaginator)

## ListDomainsPaginator

Type annotations for `boto3.client("codeartifact").get_paginator("list_domains")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListDomainsPaginator

def get_list_domains_paginator() -> ListDomainsPaginator:
    return boto3.client("codeartifact").get_paginator("list_domains")
```

[Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains)

```python
class ListDomainsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResultTypeDef]:
        pass
```
## ListPackageVersionAssetsPaginator

Type annotations for `boto3.client("codeartifact").get_paginator("list_package_version_assets")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListPackageVersionAssetsPaginator

def get_list_package_version_assets_paginator() -> ListPackageVersionAssetsPaginator:
    return boto3.client("codeartifact").get_paginator("list_package_version_assets")
```

[Paginator.ListPackageVersionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets)

```python
class ListPackageVersionAssetsPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        repository: str,
        format: PackageFormat,
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackageVersionAssetsResultTypeDef]:
        pass
```
## ListPackageVersionsPaginator

Type annotations for `boto3.client("codeartifact").get_paginator("list_package_versions")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListPackageVersionsPaginator

def get_list_package_versions_paginator() -> ListPackageVersionsPaginator:
    return boto3.client("codeartifact").get_paginator("list_package_versions")
```

[Paginator.ListPackageVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions)

```python
class ListPackageVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        repository: str,
        format: PackageFormat,
        package: str,
        domainOwner: str = None,
        namespace: str = None,
        status: PackageVersionStatus = None,
        sortBy: Literal['PUBLISHED_TIME'] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackageVersionsResultTypeDef]:
        pass
```
## ListPackagesPaginator

Type annotations for `boto3.client("codeartifact").get_paginator("list_packages")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListPackagesPaginator

def get_list_packages_paginator() -> ListPackagesPaginator:
    return boto3.client("codeartifact").get_paginator("list_packages")
```

[Paginator.ListPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages)

```python
class ListPackagesPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        repository: str,
        domainOwner: str = None,
        format: PackageFormat = None,
        namespace: str = None,
        packagePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagesResultTypeDef]:
        pass
```
## ListRepositoriesPaginator

Type annotations for `boto3.client("codeartifact").get_paginator("list_repositories")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListRepositoriesPaginator

def get_list_repositories_paginator() -> ListRepositoriesPaginator:
    return boto3.client("codeartifact").get_paginator("list_repositories")
```

[Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories)

```python
class ListRepositoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesResultTypeDef]:
        pass
```
## ListRepositoriesInDomainPaginator

Type annotations for `boto3.client("codeartifact").get_paginator("list_repositories_in_domain")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListRepositoriesInDomainPaginator

def get_list_repositories_in_domain_paginator() -> ListRepositoriesInDomainPaginator:
    return boto3.client("codeartifact").get_paginator("list_repositories_in_domain")
```

[Paginator.ListRepositoriesInDomain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain)

```python
class ListRepositoriesInDomainPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        domainOwner: str = None,
        administratorAccount: str = None,
        repositoryPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesInDomainResultTypeDef]:
        pass
```