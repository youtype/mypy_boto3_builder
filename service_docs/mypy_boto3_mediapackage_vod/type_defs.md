# Structures for boto3 MediaPackageVod module

> [Index](../index.md) > [MediaPackageVod](./index.md) > Structures

Auto-generated documentation for [MediaPackageVod](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html#MediaPackageVod)
type annotations stubs module [mypy_boto3_mediapackage_vod](https://pypi.org/project/mypy-boto3-mediapackage-vod/).

- [Structures for boto3 MediaPackageVod module](#structures-for-boto3-mediapackagevod-module)
  - [AssetShallowTypeDef](#assetshallowtypedef)
  - [AuthorizationTypeDef](#authorizationtypedef)
  - [CmafEncryptionTypeDef](#cmafencryptiontypedef)
  - [CmafPackageTypeDef](#cmafpackagetypedef)
  - [DashEncryptionTypeDef](#dashencryptiontypedef)
  - [DashManifestTypeDef](#dashmanifesttypedef)
  - [DashPackageTypeDef](#dashpackagetypedef)
  - [EgressAccessLogsTypeDef](#egressaccesslogstypedef)
  - [EgressEndpointTypeDef](#egressendpointtypedef)
  - [HlsEncryptionTypeDef](#hlsencryptiontypedef)
  - [HlsManifestTypeDef](#hlsmanifesttypedef)
  - [HlsPackageTypeDef](#hlspackagetypedef)
  - [MssEncryptionTypeDef](#mssencryptiontypedef)
  - [MssManifestTypeDef](#mssmanifesttypedef)
  - [MssPackageTypeDef](#msspackagetypedef)
  - [PackagingConfigurationTypeDef](#packagingconfigurationtypedef)
  - [PackagingGroupTypeDef](#packaginggrouptypedef)
  - [SpekeKeyProviderTypeDef](#spekekeyprovidertypedef)
  - [StreamSelectionTypeDef](#streamselectiontypedef)
  - [ConfigureLogsResponseTypeDef](#configurelogsresponsetypedef)
  - [CreateAssetResponseTypeDef](#createassetresponsetypedef)
  - [CreatePackagingConfigurationResponseTypeDef](#createpackagingconfigurationresponsetypedef)
  - [CreatePackagingGroupResponseTypeDef](#createpackaginggroupresponsetypedef)
  - [DescribeAssetResponseTypeDef](#describeassetresponsetypedef)
  - [DescribePackagingConfigurationResponseTypeDef](#describepackagingconfigurationresponsetypedef)
  - [DescribePackagingGroupResponseTypeDef](#describepackaginggroupresponsetypedef)
  - [ListAssetsResponseTypeDef](#listassetsresponsetypedef)
  - [ListPackagingConfigurationsResponseTypeDef](#listpackagingconfigurationsresponsetypedef)
  - [ListPackagingGroupsResponseTypeDef](#listpackaginggroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdatePackagingGroupResponseTypeDef](#updatepackaginggroupresponsetypedef)

## AssetShallowTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedAt`: `str`
- `Id`: `str`
- `PackagingGroupId`: `str`
- `ResourceId`: `str`
- `SourceArn`: `str`
- `SourceRoleArn`: `str`
- `Tags`: `Dict[str, str]`


## AuthorizationTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import AuthorizationTypeDef
```


Required fields:
- `CdnIdentifierSecret`: `str`
- `SecretsRoleArn`: `str`




## CmafEncryptionTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import CmafEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`




## CmafPackageTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import CmafPackageTypeDef
```


Required fields:
- `HlsManifests`: `List["HlsManifestTypeDef"]`



Optional fields:
- `Encryption`: `"CmafEncryptionTypeDef"`
- `IncludeEncoderConfigurationInSegments`: `bool`
- `SegmentDurationSeconds`: `int`


## DashEncryptionTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import DashEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`




## DashManifestTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import DashManifestTypeDef
```




Optional fields:
- `ManifestLayout`: `ManifestLayout`
- `ManifestName`: `str`
- `MinBufferTimeSeconds`: `int`
- `Profile`: `Profile`
- `StreamSelection`: `"StreamSelectionTypeDef"`


## DashPackageTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import DashPackageTypeDef
```


Required fields:
- `DashManifests`: `List["DashManifestTypeDef"]`



Optional fields:
- `Encryption`: `"DashEncryptionTypeDef"`
- `IncludeEncoderConfigurationInSegments`: `bool`
- `PeriodTriggers`: `List[__PeriodTriggersElement]`
- `SegmentDurationSeconds`: `int`
- `SegmentTemplateFormat`: `SegmentTemplateFormat`


## EgressAccessLogsTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import EgressAccessLogsTypeDef
```




Optional fields:
- `LogGroupName`: `str`


## EgressEndpointTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import EgressEndpointTypeDef
```




Optional fields:
- `PackagingConfigurationId`: `str`
- `Url`: `str`


## HlsEncryptionTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import HlsEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`



Optional fields:
- `ConstantInitializationVector`: `str`
- `EncryptionMethod`: `EncryptionMethod`


## HlsManifestTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import HlsManifestTypeDef
```




Optional fields:
- `AdMarkers`: `AdMarkers`
- `IncludeIframeOnlyStream`: `bool`
- `ManifestName`: `str`
- `ProgramDateTimeIntervalSeconds`: `int`
- `RepeatExtXKey`: `bool`
- `StreamSelection`: `"StreamSelectionTypeDef"`


## HlsPackageTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import HlsPackageTypeDef
```


Required fields:
- `HlsManifests`: `List["HlsManifestTypeDef"]`



Optional fields:
- `Encryption`: `"HlsEncryptionTypeDef"`
- `SegmentDurationSeconds`: `int`
- `UseAudioRenditionGroup`: `bool`


## MssEncryptionTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import MssEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`




## MssManifestTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import MssManifestTypeDef
```




Optional fields:
- `ManifestName`: `str`
- `StreamSelection`: `"StreamSelectionTypeDef"`


## MssPackageTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import MssPackageTypeDef
```


Required fields:
- `MssManifests`: `List["MssManifestTypeDef"]`



Optional fields:
- `Encryption`: `"MssEncryptionTypeDef"`
- `SegmentDurationSeconds`: `int`


## PackagingConfigurationTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import PackagingConfigurationTypeDef
```




Optional fields:
- `Arn`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `PackagingGroupId`: `str`
- `Tags`: `Dict[str, str]`


## PackagingGroupTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import PackagingGroupTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `DomainName`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `Id`: `str`
- `Tags`: `Dict[str, str]`


## SpekeKeyProviderTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import SpekeKeyProviderTypeDef
```


Required fields:
- `RoleArn`: `str`
- `SystemIds`: `List[str]`
- `Url`: `str`




## StreamSelectionTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import StreamSelectionTypeDef
```




Optional fields:
- `MaxVideoBitsPerSecond`: `int`
- `MinVideoBitsPerSecond`: `int`
- `StreamOrder`: `StreamOrder`


## ConfigureLogsResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import ConfigureLogsResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `DomainName`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `Id`: `str`
- `Tags`: `Dict[str, str]`


## CreateAssetResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import CreateAssetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedAt`: `str`
- `EgressEndpoints`: `List["EgressEndpointTypeDef"]`
- `Id`: `str`
- `PackagingGroupId`: `str`
- `ResourceId`: `str`
- `SourceArn`: `str`
- `SourceRoleArn`: `str`
- `Tags`: `Dict[str, str]`


## CreatePackagingConfigurationResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import CreatePackagingConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `PackagingGroupId`: `str`
- `Tags`: `Dict[str, str]`


## CreatePackagingGroupResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import CreatePackagingGroupResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `DomainName`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `Id`: `str`
- `Tags`: `Dict[str, str]`


## DescribeAssetResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import DescribeAssetResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedAt`: `str`
- `EgressEndpoints`: `List["EgressEndpointTypeDef"]`
- `Id`: `str`
- `PackagingGroupId`: `str`
- `ResourceId`: `str`
- `SourceArn`: `str`
- `SourceRoleArn`: `str`
- `Tags`: `Dict[str, str]`


## DescribePackagingConfigurationResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import DescribePackagingConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `PackagingGroupId`: `str`
- `Tags`: `Dict[str, str]`


## DescribePackagingGroupResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import DescribePackagingGroupResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `DomainName`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `Id`: `str`
- `Tags`: `Dict[str, str]`


## ListAssetsResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import ListAssetsResponseTypeDef
```




Optional fields:
- `Assets`: `List["AssetShallowTypeDef"]`
- `NextToken`: `str`


## ListPackagingConfigurationsResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import ListPackagingConfigurationsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `PackagingConfigurations`: `List["PackagingConfigurationTypeDef"]`


## ListPackagingGroupsResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import ListPackagingGroupsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `PackagingGroups`: `List["PackagingGroupTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdatePackagingGroupResponseTypeDef

```python
from mypy_boto3_mediapackage_vod.type_defs import UpdatePackagingGroupResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `DomainName`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `Id`: `str`
- `Tags`: `Dict[str, str]`

