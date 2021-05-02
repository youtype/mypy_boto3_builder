# Structures for boto3 CodeArtifact module

> [Index](../index.md) > [CodeArtifact](./index.md) > Structures

Auto-generated documentation for [CodeArtifact](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact)
type annotations stubs module [mypy_boto3_codeartifact](https://pypi.org/project/mypy-boto3-codeartifact/).

- [Structures for boto3 CodeArtifact module](#structures-for-boto3-codeartifact-module)
  - [AssetSummaryTypeDef](#assetsummarytypedef)
  - [DomainDescriptionTypeDef](#domaindescriptiontypedef)
  - [DomainSummaryTypeDef](#domainsummarytypedef)
  - [LicenseInfoTypeDef](#licenseinfotypedef)
  - [PackageDependencyTypeDef](#packagedependencytypedef)
  - [PackageSummaryTypeDef](#packagesummarytypedef)
  - [PackageVersionDescriptionTypeDef](#packageversiondescriptiontypedef)
  - [PackageVersionErrorTypeDef](#packageversionerrortypedef)
  - [PackageVersionSummaryTypeDef](#packageversionsummarytypedef)
  - [RepositoryDescriptionTypeDef](#repositorydescriptiontypedef)
  - [RepositoryExternalConnectionInfoTypeDef](#repositoryexternalconnectioninfotypedef)
  - [RepositorySummaryTypeDef](#repositorysummarytypedef)
  - [ResourcePolicyTypeDef](#resourcepolicytypedef)
  - [SuccessfulPackageVersionInfoTypeDef](#successfulpackageversioninfotypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpstreamRepositoryInfoTypeDef](#upstreamrepositoryinfotypedef)
  - [AssociateExternalConnectionResultTypeDef](#associateexternalconnectionresulttypedef)
  - [CopyPackageVersionsResultTypeDef](#copypackageversionsresulttypedef)
  - [CreateDomainResultTypeDef](#createdomainresulttypedef)
  - [CreateRepositoryResultTypeDef](#createrepositoryresulttypedef)
  - [DeleteDomainPermissionsPolicyResultTypeDef](#deletedomainpermissionspolicyresulttypedef)
  - [DeleteDomainResultTypeDef](#deletedomainresulttypedef)
  - [DeletePackageVersionsResultTypeDef](#deletepackageversionsresulttypedef)
  - [DeleteRepositoryPermissionsPolicyResultTypeDef](#deleterepositorypermissionspolicyresulttypedef)
  - [DeleteRepositoryResultTypeDef](#deleterepositoryresulttypedef)
  - [DescribeDomainResultTypeDef](#describedomainresulttypedef)
  - [DescribePackageVersionResultTypeDef](#describepackageversionresulttypedef)
  - [DescribeRepositoryResultTypeDef](#describerepositoryresulttypedef)
  - [DisassociateExternalConnectionResultTypeDef](#disassociateexternalconnectionresulttypedef)
  - [DisposePackageVersionsResultTypeDef](#disposepackageversionsresulttypedef)
  - [GetAuthorizationTokenResultTypeDef](#getauthorizationtokenresulttypedef)
  - [GetDomainPermissionsPolicyResultTypeDef](#getdomainpermissionspolicyresulttypedef)
  - [GetPackageVersionAssetResultTypeDef](#getpackageversionassetresulttypedef)
  - [GetPackageVersionReadmeResultTypeDef](#getpackageversionreadmeresulttypedef)
  - [GetRepositoryEndpointResultTypeDef](#getrepositoryendpointresulttypedef)
  - [GetRepositoryPermissionsPolicyResultTypeDef](#getrepositorypermissionspolicyresulttypedef)
  - [ListDomainsResultTypeDef](#listdomainsresulttypedef)
  - [ListPackageVersionAssetsResultTypeDef](#listpackageversionassetsresulttypedef)
  - [ListPackageVersionDependenciesResultTypeDef](#listpackageversiondependenciesresulttypedef)
  - [ListPackageVersionsResultTypeDef](#listpackageversionsresulttypedef)
  - [ListPackagesResultTypeDef](#listpackagesresulttypedef)
  - [ListRepositoriesInDomainResultTypeDef](#listrepositoriesindomainresulttypedef)
  - [ListRepositoriesResultTypeDef](#listrepositoriesresulttypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutDomainPermissionsPolicyResultTypeDef](#putdomainpermissionspolicyresulttypedef)
  - [PutRepositoryPermissionsPolicyResultTypeDef](#putrepositorypermissionspolicyresulttypedef)
  - [UpdatePackageVersionsStatusResultTypeDef](#updatepackageversionsstatusresulttypedef)
  - [UpdateRepositoryResultTypeDef](#updaterepositoryresulttypedef)
  - [UpstreamRepositoryTypeDef](#upstreamrepositorytypedef)

## AssetSummaryTypeDef

```python
from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `size`: `int`
- `hashes`: `Dict[HashAlgorithm, str]`


## DomainDescriptionTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DomainDescriptionTypeDef
```




Optional fields:
- `name`: `str`
- `owner`: `str`
- `arn`: `str`
- `status`: `DomainStatus`
- `createdTime`: `datetime`
- `encryptionKey`: `str`
- `repositoryCount`: `int`
- `assetSizeBytes`: `int`
- `s3BucketArn`: `str`


## DomainSummaryTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DomainSummaryTypeDef
```




Optional fields:
- `name`: `str`
- `owner`: `str`
- `arn`: `str`
- `status`: `DomainStatus`
- `createdTime`: `datetime`
- `encryptionKey`: `str`


## LicenseInfoTypeDef

```python
from mypy_boto3_codeartifact.type_defs import LicenseInfoTypeDef
```




Optional fields:
- `name`: `str`
- `url`: `str`


## PackageDependencyTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PackageDependencyTypeDef
```




Optional fields:
- `namespace`: `str`
- `package`: `str`
- `dependencyType`: `str`
- `versionRequirement`: `str`


## PackageSummaryTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PackageSummaryTypeDef
```




Optional fields:
- `format`: `PackageFormat`
- `namespace`: `str`
- `package`: `str`


## PackageVersionDescriptionTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PackageVersionDescriptionTypeDef
```




Optional fields:
- `format`: `PackageFormat`
- `namespace`: `str`
- `packageName`: `str`
- `displayName`: `str`
- `version`: `str`
- `summary`: `str`
- `homePage`: `str`
- `sourceCodeRepository`: `str`
- `publishedTime`: `datetime`
- `licenses`: `List["LicenseInfoTypeDef"]`
- `revision`: `str`
- `status`: `PackageVersionStatus`


## PackageVersionErrorTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PackageVersionErrorTypeDef
```




Optional fields:
- `errorCode`: `PackageVersionErrorCode`
- `errorMessage`: `str`


## PackageVersionSummaryTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PackageVersionSummaryTypeDef
```


Required fields:
- `version`: `str`
- `status`: `PackageVersionStatus`



Optional fields:
- `revision`: `str`


## RepositoryDescriptionTypeDef

```python
from mypy_boto3_codeartifact.type_defs import RepositoryDescriptionTypeDef
```




Optional fields:
- `name`: `str`
- `administratorAccount`: `str`
- `domainName`: `str`
- `domainOwner`: `str`
- `arn`: `str`
- `description`: `str`
- `upstreams`: `List["UpstreamRepositoryInfoTypeDef"]`
- `externalConnections`: `List["RepositoryExternalConnectionInfoTypeDef"]`


## RepositoryExternalConnectionInfoTypeDef

```python
from mypy_boto3_codeartifact.type_defs import RepositoryExternalConnectionInfoTypeDef
```




Optional fields:
- `externalConnectionName`: `str`
- `packageFormat`: `PackageFormat`
- `status`: `ExternalConnectionStatus`


## RepositorySummaryTypeDef

```python
from mypy_boto3_codeartifact.type_defs import RepositorySummaryTypeDef
```




Optional fields:
- `name`: `str`
- `administratorAccount`: `str`
- `domainName`: `str`
- `domainOwner`: `str`
- `arn`: `str`
- `description`: `str`


## ResourcePolicyTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ResourcePolicyTypeDef
```




Optional fields:
- `resourceArn`: `str`
- `revision`: `str`
- `document`: `str`


## SuccessfulPackageVersionInfoTypeDef

```python
from mypy_boto3_codeartifact.type_defs import SuccessfulPackageVersionInfoTypeDef
```




Optional fields:
- `revision`: `str`
- `status`: `PackageVersionStatus`


## TagTypeDef

```python
from mypy_boto3_codeartifact.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## UpstreamRepositoryInfoTypeDef

```python
from mypy_boto3_codeartifact.type_defs import UpstreamRepositoryInfoTypeDef
```




Optional fields:
- `repositoryName`: `str`


## AssociateExternalConnectionResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import AssociateExternalConnectionResultTypeDef
```




Optional fields:
- `repository`: `"RepositoryDescriptionTypeDef"`


## CopyPackageVersionsResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import CopyPackageVersionsResultTypeDef
```




Optional fields:
- `successfulVersions`: `Dict[str, "SuccessfulPackageVersionInfoTypeDef"]`
- `failedVersions`: `Dict[str, "PackageVersionErrorTypeDef"]`


## CreateDomainResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import CreateDomainResultTypeDef
```




Optional fields:
- `domain`: `"DomainDescriptionTypeDef"`


## CreateRepositoryResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import CreateRepositoryResultTypeDef
```




Optional fields:
- `repository`: `"RepositoryDescriptionTypeDef"`


## DeleteDomainPermissionsPolicyResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DeleteDomainPermissionsPolicyResultTypeDef
```




Optional fields:
- `policy`: `"ResourcePolicyTypeDef"`


## DeleteDomainResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DeleteDomainResultTypeDef
```




Optional fields:
- `domain`: `"DomainDescriptionTypeDef"`


## DeletePackageVersionsResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DeletePackageVersionsResultTypeDef
```




Optional fields:
- `successfulVersions`: `Dict[str, "SuccessfulPackageVersionInfoTypeDef"]`
- `failedVersions`: `Dict[str, "PackageVersionErrorTypeDef"]`


## DeleteRepositoryPermissionsPolicyResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DeleteRepositoryPermissionsPolicyResultTypeDef
```




Optional fields:
- `policy`: `"ResourcePolicyTypeDef"`


## DeleteRepositoryResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DeleteRepositoryResultTypeDef
```




Optional fields:
- `repository`: `"RepositoryDescriptionTypeDef"`


## DescribeDomainResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DescribeDomainResultTypeDef
```




Optional fields:
- `domain`: `"DomainDescriptionTypeDef"`


## DescribePackageVersionResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DescribePackageVersionResultTypeDef
```


Required fields:
- `packageVersion`: `"PackageVersionDescriptionTypeDef"`




## DescribeRepositoryResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DescribeRepositoryResultTypeDef
```




Optional fields:
- `repository`: `"RepositoryDescriptionTypeDef"`


## DisassociateExternalConnectionResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DisassociateExternalConnectionResultTypeDef
```




Optional fields:
- `repository`: `"RepositoryDescriptionTypeDef"`


## DisposePackageVersionsResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import DisposePackageVersionsResultTypeDef
```




Optional fields:
- `successfulVersions`: `Dict[str, "SuccessfulPackageVersionInfoTypeDef"]`
- `failedVersions`: `Dict[str, "PackageVersionErrorTypeDef"]`


## GetAuthorizationTokenResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import GetAuthorizationTokenResultTypeDef
```




Optional fields:
- `authorizationToken`: `str`
- `expiration`: `datetime`


## GetDomainPermissionsPolicyResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import GetDomainPermissionsPolicyResultTypeDef
```




Optional fields:
- `policy`: `"ResourcePolicyTypeDef"`


## GetPackageVersionAssetResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import GetPackageVersionAssetResultTypeDef
```




Optional fields:
- `asset`: `StreamingBody`
- `assetName`: `str`
- `packageVersion`: `str`
- `packageVersionRevision`: `str`


## GetPackageVersionReadmeResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import GetPackageVersionReadmeResultTypeDef
```




Optional fields:
- `format`: `PackageFormat`
- `namespace`: `str`
- `package`: `str`
- `version`: `str`
- `versionRevision`: `str`
- `readme`: `str`


## GetRepositoryEndpointResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import GetRepositoryEndpointResultTypeDef
```




Optional fields:
- `repositoryEndpoint`: `str`


## GetRepositoryPermissionsPolicyResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import GetRepositoryPermissionsPolicyResultTypeDef
```




Optional fields:
- `policy`: `"ResourcePolicyTypeDef"`


## ListDomainsResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListDomainsResultTypeDef
```




Optional fields:
- `domains`: `List["DomainSummaryTypeDef"]`
- `nextToken`: `str`


## ListPackageVersionAssetsResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListPackageVersionAssetsResultTypeDef
```




Optional fields:
- `format`: `PackageFormat`
- `namespace`: `str`
- `package`: `str`
- `version`: `str`
- `versionRevision`: `str`
- `nextToken`: `str`
- `assets`: `List["AssetSummaryTypeDef"]`


## ListPackageVersionDependenciesResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListPackageVersionDependenciesResultTypeDef
```




Optional fields:
- `format`: `PackageFormat`
- `namespace`: `str`
- `package`: `str`
- `version`: `str`
- `versionRevision`: `str`
- `nextToken`: `str`
- `dependencies`: `List["PackageDependencyTypeDef"]`


## ListPackageVersionsResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListPackageVersionsResultTypeDef
```




Optional fields:
- `defaultDisplayVersion`: `str`
- `format`: `PackageFormat`
- `namespace`: `str`
- `package`: `str`
- `versions`: `List["PackageVersionSummaryTypeDef"]`
- `nextToken`: `str`


## ListPackagesResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListPackagesResultTypeDef
```




Optional fields:
- `packages`: `List["PackageSummaryTypeDef"]`
- `nextToken`: `str`


## ListRepositoriesInDomainResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListRepositoriesInDomainResultTypeDef
```




Optional fields:
- `repositories`: `List["RepositorySummaryTypeDef"]`
- `nextToken`: `str`


## ListRepositoriesResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListRepositoriesResultTypeDef
```




Optional fields:
- `repositories`: `List["RepositorySummaryTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import ListTagsForResourceResultTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutDomainPermissionsPolicyResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PutDomainPermissionsPolicyResultTypeDef
```




Optional fields:
- `policy`: `"ResourcePolicyTypeDef"`


## PutRepositoryPermissionsPolicyResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import PutRepositoryPermissionsPolicyResultTypeDef
```




Optional fields:
- `policy`: `"ResourcePolicyTypeDef"`


## UpdatePackageVersionsStatusResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import UpdatePackageVersionsStatusResultTypeDef
```




Optional fields:
- `successfulVersions`: `Dict[str, "SuccessfulPackageVersionInfoTypeDef"]`
- `failedVersions`: `Dict[str, "PackageVersionErrorTypeDef"]`


## UpdateRepositoryResultTypeDef

```python
from mypy_boto3_codeartifact.type_defs import UpdateRepositoryResultTypeDef
```




Optional fields:
- `repository`: `"RepositoryDescriptionTypeDef"`


## UpstreamRepositoryTypeDef

```python
from mypy_boto3_codeartifact.type_defs import UpstreamRepositoryTypeDef
```


Required fields:
- `repositoryName`: `str`



