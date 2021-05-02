# CodeArtifactClient for boto3 CodeArtifact module

> [Index](../index.md) > [CodeArtifact](./index.md) > CodeArtifactClient

Auto-generated documentation for [CodeArtifact](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact)
type annotations stubs module [mypy_boto3_codeartifact](https://pypi.org/project/mypy-boto3-codeartifact/).

- [CodeArtifactClient for boto3 CodeArtifact module](#codeartifactclient-for-boto3-codeartifact-module)
  - [CodeArtifactClient](#codeartifactclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_external_connection](#associate_external_connection)
    - [can_paginate](#can_paginate)
    - [copy_package_versions](#copy_package_versions)
    - [create_domain](#create_domain)
    - [create_repository](#create_repository)
    - [delete_domain](#delete_domain)
    - [delete_domain_permissions_policy](#delete_domain_permissions_policy)
    - [delete_package_versions](#delete_package_versions)
    - [delete_repository](#delete_repository)
    - [delete_repository_permissions_policy](#delete_repository_permissions_policy)
    - [describe_domain](#describe_domain)
    - [describe_package_version](#describe_package_version)
    - [describe_repository](#describe_repository)
    - [disassociate_external_connection](#disassociate_external_connection)
    - [dispose_package_versions](#dispose_package_versions)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_authorization_token](#get_authorization_token)
    - [get_domain_permissions_policy](#get_domain_permissions_policy)
    - [get_package_version_asset](#get_package_version_asset)
    - [get_package_version_readme](#get_package_version_readme)
    - [get_repository_endpoint](#get_repository_endpoint)
    - [get_repository_permissions_policy](#get_repository_permissions_policy)
    - [list_domains](#list_domains)
    - [list_package_version_assets](#list_package_version_assets)
    - [list_package_version_dependencies](#list_package_version_dependencies)
    - [list_package_versions](#list_package_versions)
    - [list_packages](#list_packages)
    - [list_repositories](#list_repositories)
    - [list_repositories_in_domain](#list_repositories_in_domain)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_domain_permissions_policy](#put_domain_permissions_policy)
    - [put_repository_permissions_policy](#put_repository_permissions_policy)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_package_versions_status](#update_package_versions_status)
    - [update_repository](#update_repository)
    - [get_paginator](#get_paginator)

## CodeArtifactClient

Type annotations for `boto3.client("codeartifact")`

Can be used directly:

```python
from mypy_boto3_codeartifact.client import CodeArtifactClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codeartifact.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### associate_external_connection

Type annotations for `boto3.client("codeartifact").associate_external_connection` method.

[Client.associate_external_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.associate_external_connection)

```python
def associate_external_connection(
    self,
    domain: str,
    repository: str,
    externalConnection: str,
    domainOwner: str = None
) -> AssociateExternalConnectionResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codeartifact").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### copy_package_versions

Type annotations for `boto3.client("codeartifact").copy_package_versions` method.

[Client.copy_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.copy_package_versions)

```python
def copy_package_versions(
    self,
    domain: str,
    sourceRepository: str,
    destinationRepository: str,
    format: PackageFormat,
    package: str,
    domainOwner: str = None,
    namespace: str = None,
    versions: List[str] = None,
    versionRevisions: Dict[str, str] = None,
    allowOverwrite: bool = None,
    includeFromUpstream: bool = None
) -> CopyPackageVersionsResultTypeDef:
    pass
```

### create_domain

Type annotations for `boto3.client("codeartifact").create_domain` method.

[Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.create_domain)

```python
def create_domain(
    self,
    domain: str,
    encryptionKey: str = None,
    tags: List["TagTypeDef"] = None
) -> CreateDomainResultTypeDef:
    pass
```

### create_repository

Type annotations for `boto3.client("codeartifact").create_repository` method.

[Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.create_repository)

```python
def create_repository(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None,
    description: str = None,
    upstreams: List[UpstreamRepositoryTypeDef] = None,
    tags: List["TagTypeDef"] = None
) -> CreateRepositoryResultTypeDef:
    pass
```

### delete_domain

Type annotations for `boto3.client("codeartifact").delete_domain` method.

[Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.delete_domain)

```python
def delete_domain(
    self,
    domain: str,
    domainOwner: str = None
) -> DeleteDomainResultTypeDef:
    pass
```

### delete_domain_permissions_policy

Type annotations for `boto3.client("codeartifact").delete_domain_permissions_policy` method.

[Client.delete_domain_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.delete_domain_permissions_policy)

```python
def delete_domain_permissions_policy(
    self,
    domain: str,
    domainOwner: str = None,
    policyRevision: str = None
) -> DeleteDomainPermissionsPolicyResultTypeDef:
    pass
```

### delete_package_versions

Type annotations for `boto3.client("codeartifact").delete_package_versions` method.

[Client.delete_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.delete_package_versions)

```python
def delete_package_versions(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    versions: List[str],
    domainOwner: str = None,
    namespace: str = None,
    expectedStatus: PackageVersionStatus = None
) -> DeletePackageVersionsResultTypeDef:
    pass
```

### delete_repository

Type annotations for `boto3.client("codeartifact").delete_repository` method.

[Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.delete_repository)

```python
def delete_repository(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None
) -> DeleteRepositoryResultTypeDef:
    pass
```

### delete_repository_permissions_policy

Type annotations for `boto3.client("codeartifact").delete_repository_permissions_policy` method.

[Client.delete_repository_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.delete_repository_permissions_policy)

```python
def delete_repository_permissions_policy(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None,
    policyRevision: str = None
) -> DeleteRepositoryPermissionsPolicyResultTypeDef:
    pass
```

### describe_domain

Type annotations for `boto3.client("codeartifact").describe_domain` method.

[Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.describe_domain)

```python
def describe_domain(
    self,
    domain: str,
    domainOwner: str = None
) -> DescribeDomainResultTypeDef:
    pass
```

### describe_package_version

Type annotations for `boto3.client("codeartifact").describe_package_version` method.

[Client.describe_package_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.describe_package_version)

```python
def describe_package_version(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    packageVersion: str,
    domainOwner: str = None,
    namespace: str = None
) -> DescribePackageVersionResultTypeDef:
    pass
```

### describe_repository

Type annotations for `boto3.client("codeartifact").describe_repository` method.

[Client.describe_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.describe_repository)

```python
def describe_repository(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None
) -> DescribeRepositoryResultTypeDef:
    pass
```

### disassociate_external_connection

Type annotations for `boto3.client("codeartifact").disassociate_external_connection` method.

[Client.disassociate_external_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.disassociate_external_connection)

```python
def disassociate_external_connection(
    self,
    domain: str,
    repository: str,
    externalConnection: str,
    domainOwner: str = None
) -> DisassociateExternalConnectionResultTypeDef:
    pass
```

### dispose_package_versions

Type annotations for `boto3.client("codeartifact").dispose_package_versions` method.

[Client.dispose_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.dispose_package_versions)

```python
def dispose_package_versions(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    versions: List[str],
    domainOwner: str = None,
    namespace: str = None,
    versionRevisions: Dict[str, str] = None,
    expectedStatus: PackageVersionStatus = None
) -> DisposePackageVersionsResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codeartifact").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_authorization_token

Type annotations for `boto3.client("codeartifact").get_authorization_token` method.

[Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_authorization_token)

```python
def get_authorization_token(
    self,
    domain: str,
    domainOwner: str = None,
    durationSeconds: int = None
) -> GetAuthorizationTokenResultTypeDef:
    pass
```

### get_domain_permissions_policy

Type annotations for `boto3.client("codeartifact").get_domain_permissions_policy` method.

[Client.get_domain_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_domain_permissions_policy)

```python
def get_domain_permissions_policy(
    self,
    domain: str,
    domainOwner: str = None
) -> GetDomainPermissionsPolicyResultTypeDef:
    pass
```

### get_package_version_asset

Type annotations for `boto3.client("codeartifact").get_package_version_asset` method.

[Client.get_package_version_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_package_version_asset)

```python
def get_package_version_asset(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    packageVersion: str,
    asset: str,
    domainOwner: str = None,
    namespace: str = None,
    packageVersionRevision: str = None
) -> GetPackageVersionAssetResultTypeDef:
    pass
```

### get_package_version_readme

Type annotations for `boto3.client("codeartifact").get_package_version_readme` method.

[Client.get_package_version_readme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_package_version_readme)

```python
def get_package_version_readme(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    packageVersion: str,
    domainOwner: str = None,
    namespace: str = None
) -> GetPackageVersionReadmeResultTypeDef:
    pass
```

### get_repository_endpoint

Type annotations for `boto3.client("codeartifact").get_repository_endpoint` method.

[Client.get_repository_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_repository_endpoint)

```python
def get_repository_endpoint(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    domainOwner: str = None
) -> GetRepositoryEndpointResultTypeDef:
    pass
```

### get_repository_permissions_policy

Type annotations for `boto3.client("codeartifact").get_repository_permissions_policy` method.

[Client.get_repository_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.get_repository_permissions_policy)

```python
def get_repository_permissions_policy(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None
) -> GetRepositoryPermissionsPolicyResultTypeDef:
    pass
```

### list_domains

Type annotations for `boto3.client("codeartifact").list_domains` method.

[Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_domains)

```python
def list_domains(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListDomainsResultTypeDef:
    pass
```

### list_package_version_assets

Type annotations for `boto3.client("codeartifact").list_package_version_assets` method.

[Client.list_package_version_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_package_version_assets)

```python
def list_package_version_assets(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    packageVersion: str,
    domainOwner: str = None,
    namespace: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListPackageVersionAssetsResultTypeDef:
    pass
```

### list_package_version_dependencies

Type annotations for `boto3.client("codeartifact").list_package_version_dependencies` method.

[Client.list_package_version_dependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_package_version_dependencies)

```python
def list_package_version_dependencies(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    packageVersion: str,
    domainOwner: str = None,
    namespace: str = None,
    nextToken: str = None
) -> ListPackageVersionDependenciesResultTypeDef:
    pass
```

### list_package_versions

Type annotations for `boto3.client("codeartifact").list_package_versions` method.

[Client.list_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_package_versions)

```python
def list_package_versions(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    domainOwner: str = None,
    namespace: str = None,
    status: PackageVersionStatus = None,
    sortBy: Literal['PUBLISHED_TIME'] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListPackageVersionsResultTypeDef:
    pass
```

### list_packages

Type annotations for `boto3.client("codeartifact").list_packages` method.

[Client.list_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_packages)

```python
def list_packages(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None,
    format: PackageFormat = None,
    namespace: str = None,
    packagePrefix: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListPackagesResultTypeDef:
    pass
```

### list_repositories

Type annotations for `boto3.client("codeartifact").list_repositories` method.

[Client.list_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_repositories)

```python
def list_repositories(
    self,
    repositoryPrefix: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListRepositoriesResultTypeDef:
    pass
```

### list_repositories_in_domain

Type annotations for `boto3.client("codeartifact").list_repositories_in_domain` method.

[Client.list_repositories_in_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_repositories_in_domain)

```python
def list_repositories_in_domain(
    self,
    domain: str,
    domainOwner: str = None,
    administratorAccount: str = None,
    repositoryPrefix: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListRepositoriesInDomainResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codeartifact").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResultTypeDef:
    pass
```

### put_domain_permissions_policy

Type annotations for `boto3.client("codeartifact").put_domain_permissions_policy` method.

[Client.put_domain_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.put_domain_permissions_policy)

```python
def put_domain_permissions_policy(
    self,
    domain: str,
    policyDocument: str,
    domainOwner: str = None,
    policyRevision: str = None
) -> PutDomainPermissionsPolicyResultTypeDef:
    pass
```

### put_repository_permissions_policy

Type annotations for `boto3.client("codeartifact").put_repository_permissions_policy` method.

[Client.put_repository_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.put_repository_permissions_policy)

```python
def put_repository_permissions_policy(
    self,
    domain: str,
    repository: str,
    policyDocument: str,
    domainOwner: str = None,
    policyRevision: str = None
) -> PutRepositoryPermissionsPolicyResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("codeartifact").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("codeartifact").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_package_versions_status

Type annotations for `boto3.client("codeartifact").update_package_versions_status` method.

[Client.update_package_versions_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.update_package_versions_status)

```python
def update_package_versions_status(
    self,
    domain: str,
    repository: str,
    format: PackageFormat,
    package: str,
    versions: List[str],
    targetStatus: PackageVersionStatus,
    domainOwner: str = None,
    namespace: str = None,
    versionRevisions: Dict[str, str] = None,
    expectedStatus: PackageVersionStatus = None
) -> UpdatePackageVersionsStatusResultTypeDef:
    pass
```

### update_repository

Type annotations for `boto3.client("codeartifact").update_repository` method.

[Client.update_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client.update_repository)

```python
def update_repository(
    self,
    domain: str,
    repository: str,
    domainOwner: str = None,
    description: str = None,
    upstreams: List[UpstreamRepositoryTypeDef] = None
) -> UpdateRepositoryResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("codeartifact").get_paginator` method with overloads.

- `client.get_paginator("list_domains")` -> [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- `client.get_paginator("list_package_version_assets")` -> [ListPackageVersionAssetsPaginator](./paginators.md#listpackageversionassetspaginator)
- `client.get_paginator("list_package_versions")` -> [ListPackageVersionsPaginator](./paginators.md#listpackageversionspaginator)
- `client.get_paginator("list_packages")` -> [ListPackagesPaginator](./paginators.md#listpackagespaginator)
- `client.get_paginator("list_repositories")` -> [ListRepositoriesPaginator](./paginators.md#listrepositoriespaginator)
- `client.get_paginator("list_repositories_in_domain")` -> [ListRepositoriesInDomainPaginator](./paginators.md#listrepositoriesindomainpaginator)


