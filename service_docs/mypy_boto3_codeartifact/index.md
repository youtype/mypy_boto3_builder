# Type annotations for boto3 CodeArtifact module

> [Index](../index.md) > CodeArtifact

Auto-generated documentation for [CodeArtifact](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact)
type annotations stubs module [mypy_boto3_codeartifact](https://pypi.org/project/mypy-boto3-codeartifact/).

```bash
pip install mypy-boto3-codeartifact
```

- [Type annotations for boto3 CodeArtifact module](#type-annotations-for-boto3-codeartifact-module)
  - [CodeArtifactClient](#codeartifactclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeArtifactClient

Type annotations for  `boto3.client("codeartifact")` as [CodeArtifactClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codeartifact.client import CodeArtifactClient
```


CodeArtifactClient [exceptions](./client.md#exceptions)



### Methods
- [associate_external_connection](./client.md#associate-external-connection)
- [can_paginate](./client.md#can-paginate)
- [copy_package_versions](./client.md#copy-package-versions)
- [create_domain](./client.md#create-domain)
- [create_repository](./client.md#create-repository)
- [delete_domain](./client.md#delete-domain)
- [delete_domain_permissions_policy](./client.md#delete-domain-permissions-policy)
- [delete_package_versions](./client.md#delete-package-versions)
- [delete_repository](./client.md#delete-repository)
- [delete_repository_permissions_policy](./client.md#delete-repository-permissions-policy)
- [describe_domain](./client.md#describe-domain)
- [describe_package_version](./client.md#describe-package-version)
- [describe_repository](./client.md#describe-repository)
- [disassociate_external_connection](./client.md#disassociate-external-connection)
- [dispose_package_versions](./client.md#dispose-package-versions)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_authorization_token](./client.md#get-authorization-token)
- [get_domain_permissions_policy](./client.md#get-domain-permissions-policy)
- [get_package_version_asset](./client.md#get-package-version-asset)
- [get_package_version_readme](./client.md#get-package-version-readme)
- [get_paginator](./client.md#get-paginator)
- [get_repository_endpoint](./client.md#get-repository-endpoint)
- [get_repository_permissions_policy](./client.md#get-repository-permissions-policy)
- [list_domains](./client.md#list-domains)
- [list_package_version_assets](./client.md#list-package-version-assets)
- [list_package_version_dependencies](./client.md#list-package-version-dependencies)
- [list_package_versions](./client.md#list-package-versions)
- [list_packages](./client.md#list-packages)
- [list_repositories](./client.md#list-repositories)
- [list_repositories_in_domain](./client.md#list-repositories-in-domain)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_domain_permissions_policy](./client.md#put-domain-permissions-policy)
- [put_repository_permissions_policy](./client.md#put-repository-permissions-policy)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_package_versions_status](./client.md#update-package-versions-status)
- [update_repository](./client.md#update-repository)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codeartifact").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codeartifact.paginators import ListDomainsPaginator, ...
```

- [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- [ListPackageVersionAssetsPaginator](./paginators.md#listpackageversionassetspaginator)
- [ListPackageVersionsPaginator](./paginators.md#listpackageversionspaginator)
- [ListPackagesPaginator](./paginators.md#listpackagespaginator)
- [ListRepositoriesPaginator](./paginators.md#listrepositoriespaginator)
- [ListRepositoriesInDomainPaginator](./paginators.md#listrepositoriesindomainpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codeartifact.literals import DomainStatus, ...
```

- [DomainStatus](./literals.md#domainstatus)
- [ExternalConnectionStatus](./literals.md#externalconnectionstatus)
- [HashAlgorithm](./literals.md#hashalgorithm)
- [ListDomainsPaginatorName](./literals.md#listdomainspaginatorname)
- [ListPackageVersionAssetsPaginatorName](./literals.md#listpackageversionassetspaginatorname)
- [ListPackageVersionsPaginatorName](./literals.md#listpackageversionspaginatorname)
- [ListPackagesPaginatorName](./literals.md#listpackagespaginatorname)
- [ListRepositoriesInDomainPaginatorName](./literals.md#listrepositoriesindomainpaginatorname)
- [ListRepositoriesPaginatorName](./literals.md#listrepositoriespaginatorname)
- [PackageFormat](./literals.md#packageformat)
- [PackageVersionErrorCode](./literals.md#packageversionerrorcode)
- [PackageVersionSortType](./literals.md#packageversionsorttype)
- [PackageVersionStatus](./literals.md#packageversionstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef, ...
```

- [AssetSummaryTypeDef](./type_defs.md#assetsummarytypedef)
- [DomainDescriptionTypeDef](./type_defs.md#domaindescriptiontypedef)
- [DomainSummaryTypeDef](./type_defs.md#domainsummarytypedef)
- [LicenseInfoTypeDef](./type_defs.md#licenseinfotypedef)
- [PackageDependencyTypeDef](./type_defs.md#packagedependencytypedef)
- [PackageSummaryTypeDef](./type_defs.md#packagesummarytypedef)
- [PackageVersionDescriptionTypeDef](./type_defs.md#packageversiondescriptiontypedef)
- [PackageVersionErrorTypeDef](./type_defs.md#packageversionerrortypedef)
- [PackageVersionSummaryTypeDef](./type_defs.md#packageversionsummarytypedef)
- [RepositoryDescriptionTypeDef](./type_defs.md#repositorydescriptiontypedef)
- [RepositoryExternalConnectionInfoTypeDef](./type_defs.md#repositoryexternalconnectioninfotypedef)
- [RepositorySummaryTypeDef](./type_defs.md#repositorysummarytypedef)
- [ResourcePolicyTypeDef](./type_defs.md#resourcepolicytypedef)
- [SuccessfulPackageVersionInfoTypeDef](./type_defs.md#successfulpackageversioninfotypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpstreamRepositoryInfoTypeDef](./type_defs.md#upstreamrepositoryinfotypedef)
- [AssociateExternalConnectionResultTypeDef](./type_defs.md#associateexternalconnectionresulttypedef)
- [CopyPackageVersionsResultTypeDef](./type_defs.md#copypackageversionsresulttypedef)
- [CreateDomainResultTypeDef](./type_defs.md#createdomainresulttypedef)
- [CreateRepositoryResultTypeDef](./type_defs.md#createrepositoryresulttypedef)
- [DeleteDomainPermissionsPolicyResultTypeDef](./type_defs.md#deletedomainpermissionspolicyresulttypedef)
- [DeleteDomainResultTypeDef](./type_defs.md#deletedomainresulttypedef)
- [DeletePackageVersionsResultTypeDef](./type_defs.md#deletepackageversionsresulttypedef)
- [DeleteRepositoryPermissionsPolicyResultTypeDef](./type_defs.md#deleterepositorypermissionspolicyresulttypedef)
- [DeleteRepositoryResultTypeDef](./type_defs.md#deleterepositoryresulttypedef)
- [DescribeDomainResultTypeDef](./type_defs.md#describedomainresulttypedef)
- [DescribePackageVersionResultTypeDef](./type_defs.md#describepackageversionresulttypedef)
- [DescribeRepositoryResultTypeDef](./type_defs.md#describerepositoryresulttypedef)
- [DisassociateExternalConnectionResultTypeDef](./type_defs.md#disassociateexternalconnectionresulttypedef)
- [DisposePackageVersionsResultTypeDef](./type_defs.md#disposepackageversionsresulttypedef)
- [GetAuthorizationTokenResultTypeDef](./type_defs.md#getauthorizationtokenresulttypedef)
- [GetDomainPermissionsPolicyResultTypeDef](./type_defs.md#getdomainpermissionspolicyresulttypedef)
- [GetPackageVersionAssetResultTypeDef](./type_defs.md#getpackageversionassetresulttypedef)
- [GetPackageVersionReadmeResultTypeDef](./type_defs.md#getpackageversionreadmeresulttypedef)
- [GetRepositoryEndpointResultTypeDef](./type_defs.md#getrepositoryendpointresulttypedef)
- [GetRepositoryPermissionsPolicyResultTypeDef](./type_defs.md#getrepositorypermissionspolicyresulttypedef)
- [ListDomainsResultTypeDef](./type_defs.md#listdomainsresulttypedef)
- [ListPackageVersionAssetsResultTypeDef](./type_defs.md#listpackageversionassetsresulttypedef)
- [ListPackageVersionDependenciesResultTypeDef](./type_defs.md#listpackageversiondependenciesresulttypedef)
- [ListPackageVersionsResultTypeDef](./type_defs.md#listpackageversionsresulttypedef)
- [ListPackagesResultTypeDef](./type_defs.md#listpackagesresulttypedef)
- [ListRepositoriesInDomainResultTypeDef](./type_defs.md#listrepositoriesindomainresulttypedef)
- [ListRepositoriesResultTypeDef](./type_defs.md#listrepositoriesresulttypedef)
- [ListTagsForResourceResultTypeDef](./type_defs.md#listtagsforresourceresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutDomainPermissionsPolicyResultTypeDef](./type_defs.md#putdomainpermissionspolicyresulttypedef)
- [PutRepositoryPermissionsPolicyResultTypeDef](./type_defs.md#putrepositorypermissionspolicyresulttypedef)
- [UpdatePackageVersionsStatusResultTypeDef](./type_defs.md#updatepackageversionsstatusresulttypedef)
- [UpdateRepositoryResultTypeDef](./type_defs.md#updaterepositoryresulttypedef)
- [UpstreamRepositoryTypeDef](./type_defs.md#upstreamrepositorytypedef)
