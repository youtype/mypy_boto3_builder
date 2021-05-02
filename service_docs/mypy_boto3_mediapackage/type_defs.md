# Structures for boto3 MediaPackage module

> [Index](../index.md) > [MediaPackage](./index.md) > Structures

Auto-generated documentation for [MediaPackage](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage)
type annotations stubs module [mypy_boto3_mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/).

- [Structures for boto3 MediaPackage module](#structures-for-boto3-mediapackage-module)
  - [AuthorizationTypeDef](#authorizationtypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [CmafEncryptionTypeDef](#cmafencryptiontypedef)
  - [CmafPackageCreateOrUpdateParametersTypeDef](#cmafpackagecreateorupdateparameterstypedef)
  - [CmafPackageTypeDef](#cmafpackagetypedef)
  - [ConfigureLogsResponseTypeDef](#configurelogsresponsetypedef)
  - [CreateChannelResponseTypeDef](#createchannelresponsetypedef)
  - [CreateHarvestJobResponseTypeDef](#createharvestjobresponsetypedef)
  - [CreateOriginEndpointResponseTypeDef](#createoriginendpointresponsetypedef)
  - [DashEncryptionTypeDef](#dashencryptiontypedef)
  - [DashPackageTypeDef](#dashpackagetypedef)
  - [DescribeChannelResponseTypeDef](#describechannelresponsetypedef)
  - [DescribeHarvestJobResponseTypeDef](#describeharvestjobresponsetypedef)
  - [DescribeOriginEndpointResponseTypeDef](#describeoriginendpointresponsetypedef)
  - [EgressAccessLogsTypeDef](#egressaccesslogstypedef)
  - [EncryptionContractConfigurationTypeDef](#encryptioncontractconfigurationtypedef)
  - [HarvestJobTypeDef](#harvestjobtypedef)
  - [HlsEncryptionTypeDef](#hlsencryptiontypedef)
  - [HlsIngestTypeDef](#hlsingesttypedef)
  - [HlsManifestCreateOrUpdateParametersTypeDef](#hlsmanifestcreateorupdateparameterstypedef)
  - [HlsManifestTypeDef](#hlsmanifesttypedef)
  - [HlsPackageTypeDef](#hlspackagetypedef)
  - [IngestEndpointTypeDef](#ingestendpointtypedef)
  - [IngressAccessLogsTypeDef](#ingressaccesslogstypedef)
  - [ListChannelsResponseTypeDef](#listchannelsresponsetypedef)
  - [ListHarvestJobsResponseTypeDef](#listharvestjobsresponsetypedef)
  - [ListOriginEndpointsResponseTypeDef](#listoriginendpointsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MssEncryptionTypeDef](#mssencryptiontypedef)
  - [MssPackageTypeDef](#msspackagetypedef)
  - [OriginEndpointTypeDef](#originendpointtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RotateChannelCredentialsResponseTypeDef](#rotatechannelcredentialsresponsetypedef)
  - [RotateIngestEndpointCredentialsResponseTypeDef](#rotateingestendpointcredentialsresponsetypedef)
  - [S3DestinationTypeDef](#s3destinationtypedef)
  - [SpekeKeyProviderTypeDef](#spekekeyprovidertypedef)
  - [StreamSelectionTypeDef](#streamselectiontypedef)
  - [UpdateChannelResponseTypeDef](#updatechannelresponsetypedef)
  - [UpdateOriginEndpointResponseTypeDef](#updateoriginendpointresponsetypedef)

## AuthorizationTypeDef

```python
from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef
```


Required fields:
- `CdnIdentifierSecret`: `str`
- `SecretsRoleArn`: `str`




## ChannelTypeDef

```python
from mypy_boto3_mediapackage.type_defs import ChannelTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## CmafEncryptionTypeDef

```python
from mypy_boto3_mediapackage.type_defs import CmafEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`



Optional fields:
- `ConstantInitializationVector`: `str`
- `KeyRotationIntervalSeconds`: `int`


## CmafPackageCreateOrUpdateParametersTypeDef

```python
from mypy_boto3_mediapackage.type_defs import CmafPackageCreateOrUpdateParametersTypeDef
```




Optional fields:
- `Encryption`: `"CmafEncryptionTypeDef"`
- `HlsManifests`: `List["HlsManifestCreateOrUpdateParametersTypeDef"]`
- `SegmentDurationSeconds`: `int`
- `SegmentPrefix`: `str`
- `StreamSelection`: `"StreamSelectionTypeDef"`


## CmafPackageTypeDef

```python
from mypy_boto3_mediapackage.type_defs import CmafPackageTypeDef
```




Optional fields:
- `Encryption`: `"CmafEncryptionTypeDef"`
- `HlsManifests`: `List["HlsManifestTypeDef"]`
- `SegmentDurationSeconds`: `int`
- `SegmentPrefix`: `str`
- `StreamSelection`: `"StreamSelectionTypeDef"`


## ConfigureLogsResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import ConfigureLogsResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## CreateChannelResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import CreateChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## CreateHarvestJobResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import CreateHarvestJobResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `ChannelId`: `str`
- `CreatedAt`: `str`
- `EndTime`: `str`
- `Id`: `str`
- `OriginEndpointId`: `str`
- `S3Destination`: `"S3DestinationTypeDef"`
- `StartTime`: `str`
- `Status`: `Status`


## CreateOriginEndpointResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import CreateOriginEndpointResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `ChannelId`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `Description`: `str`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `ManifestName`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `Origination`: `Origination`
- `StartoverWindowSeconds`: `int`
- `Tags`: `Dict[str, str]`
- `TimeDelaySeconds`: `int`
- `Url`: `str`
- `Whitelist`: `List[str]`


## DashEncryptionTypeDef

```python
from mypy_boto3_mediapackage.type_defs import DashEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`



Optional fields:
- `KeyRotationIntervalSeconds`: `int`


## DashPackageTypeDef

```python
from mypy_boto3_mediapackage.type_defs import DashPackageTypeDef
```




Optional fields:
- `AdTriggers`: `List[__AdTriggersElement]`
- `AdsOnDeliveryRestrictions`: `AdsOnDeliveryRestrictions`
- `Encryption`: `"DashEncryptionTypeDef"`
- `ManifestLayout`: `ManifestLayout`
- `ManifestWindowSeconds`: `int`
- `MinBufferTimeSeconds`: `int`
- `MinUpdatePeriodSeconds`: `int`
- `PeriodTriggers`: `List[Literal['ADS']]`
- `Profile`: `Profile`
- `SegmentDurationSeconds`: `int`
- `SegmentTemplateFormat`: `SegmentTemplateFormat`
- `StreamSelection`: `"StreamSelectionTypeDef"`
- `SuggestedPresentationDelaySeconds`: `int`
- `UtcTiming`: `UtcTiming`
- `UtcTimingUri`: `str`


## DescribeChannelResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import DescribeChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## DescribeHarvestJobResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import DescribeHarvestJobResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `ChannelId`: `str`
- `CreatedAt`: `str`
- `EndTime`: `str`
- `Id`: `str`
- `OriginEndpointId`: `str`
- `S3Destination`: `"S3DestinationTypeDef"`
- `StartTime`: `str`
- `Status`: `Status`


## DescribeOriginEndpointResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import DescribeOriginEndpointResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `ChannelId`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `Description`: `str`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `ManifestName`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `Origination`: `Origination`
- `StartoverWindowSeconds`: `int`
- `Tags`: `Dict[str, str]`
- `TimeDelaySeconds`: `int`
- `Url`: `str`
- `Whitelist`: `List[str]`


## EgressAccessLogsTypeDef

```python
from mypy_boto3_mediapackage.type_defs import EgressAccessLogsTypeDef
```




Optional fields:
- `LogGroupName`: `str`


## EncryptionContractConfigurationTypeDef

```python
from mypy_boto3_mediapackage.type_defs import EncryptionContractConfigurationTypeDef
```


Required fields:
- `PresetSpeke20Audio`: `Literal['PRESET-AUDIO-1']`
- `PresetSpeke20Video`: `Literal['PRESET-VIDEO-1']`




## HarvestJobTypeDef

```python
from mypy_boto3_mediapackage.type_defs import HarvestJobTypeDef
```




Optional fields:
- `Arn`: `str`
- `ChannelId`: `str`
- `CreatedAt`: `str`
- `EndTime`: `str`
- `Id`: `str`
- `OriginEndpointId`: `str`
- `S3Destination`: `"S3DestinationTypeDef"`
- `StartTime`: `str`
- `Status`: `Status`


## HlsEncryptionTypeDef

```python
from mypy_boto3_mediapackage.type_defs import HlsEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`



Optional fields:
- `ConstantInitializationVector`: `str`
- `EncryptionMethod`: `EncryptionMethod`
- `KeyRotationIntervalSeconds`: `int`
- `RepeatExtXKey`: `bool`


## HlsIngestTypeDef

```python
from mypy_boto3_mediapackage.type_defs import HlsIngestTypeDef
```




Optional fields:
- `IngestEndpoints`: `List["IngestEndpointTypeDef"]`


## HlsManifestCreateOrUpdateParametersTypeDef

```python
from mypy_boto3_mediapackage.type_defs import HlsManifestCreateOrUpdateParametersTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `AdMarkers`: `AdMarkers`
- `AdTriggers`: `List[__AdTriggersElement]`
- `AdsOnDeliveryRestrictions`: `AdsOnDeliveryRestrictions`
- `IncludeIframeOnlyStream`: `bool`
- `ManifestName`: `str`
- `PlaylistType`: `PlaylistType`
- `PlaylistWindowSeconds`: `int`
- `ProgramDateTimeIntervalSeconds`: `int`


## HlsManifestTypeDef

```python
from mypy_boto3_mediapackage.type_defs import HlsManifestTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `AdMarkers`: `AdMarkers`
- `IncludeIframeOnlyStream`: `bool`
- `ManifestName`: `str`
- `PlaylistType`: `PlaylistType`
- `PlaylistWindowSeconds`: `int`
- `ProgramDateTimeIntervalSeconds`: `int`
- `Url`: `str`


## HlsPackageTypeDef

```python
from mypy_boto3_mediapackage.type_defs import HlsPackageTypeDef
```




Optional fields:
- `AdMarkers`: `AdMarkers`
- `AdTriggers`: `List[__AdTriggersElement]`
- `AdsOnDeliveryRestrictions`: `AdsOnDeliveryRestrictions`
- `Encryption`: `"HlsEncryptionTypeDef"`
- `IncludeIframeOnlyStream`: `bool`
- `PlaylistType`: `PlaylistType`
- `PlaylistWindowSeconds`: `int`
- `ProgramDateTimeIntervalSeconds`: `int`
- `SegmentDurationSeconds`: `int`
- `StreamSelection`: `"StreamSelectionTypeDef"`
- `UseAudioRenditionGroup`: `bool`


## IngestEndpointTypeDef

```python
from mypy_boto3_mediapackage.type_defs import IngestEndpointTypeDef
```




Optional fields:
- `Id`: `str`
- `Password`: `str`
- `Url`: `str`
- `Username`: `str`


## IngressAccessLogsTypeDef

```python
from mypy_boto3_mediapackage.type_defs import IngressAccessLogsTypeDef
```




Optional fields:
- `LogGroupName`: `str`


## ListChannelsResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import ListChannelsResponseTypeDef
```




Optional fields:
- `Channels`: `List["ChannelTypeDef"]`
- `NextToken`: `str`


## ListHarvestJobsResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import ListHarvestJobsResponseTypeDef
```




Optional fields:
- `HarvestJobs`: `List["HarvestJobTypeDef"]`
- `NextToken`: `str`


## ListOriginEndpointsResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import ListOriginEndpointsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `OriginEndpoints`: `List["OriginEndpointTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## MssEncryptionTypeDef

```python
from mypy_boto3_mediapackage.type_defs import MssEncryptionTypeDef
```


Required fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`




## MssPackageTypeDef

```python
from mypy_boto3_mediapackage.type_defs import MssPackageTypeDef
```




Optional fields:
- `Encryption`: `"MssEncryptionTypeDef"`
- `ManifestWindowSeconds`: `int`
- `SegmentDurationSeconds`: `int`
- `StreamSelection`: `"StreamSelectionTypeDef"`


## OriginEndpointTypeDef

```python
from mypy_boto3_mediapackage.type_defs import OriginEndpointTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `ChannelId`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `Description`: `str`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `ManifestName`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `Origination`: `Origination`
- `StartoverWindowSeconds`: `int`
- `Tags`: `Dict[str, str]`
- `TimeDelaySeconds`: `int`
- `Url`: `str`
- `Whitelist`: `List[str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mediapackage.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RotateChannelCredentialsResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import RotateChannelCredentialsResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## RotateIngestEndpointCredentialsResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import RotateIngestEndpointCredentialsResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## S3DestinationTypeDef

```python
from mypy_boto3_mediapackage.type_defs import S3DestinationTypeDef
```


Required fields:
- `BucketName`: `str`
- `ManifestKey`: `str`
- `RoleArn`: `str`




## SpekeKeyProviderTypeDef

```python
from mypy_boto3_mediapackage.type_defs import SpekeKeyProviderTypeDef
```


Required fields:
- `ResourceId`: `str`
- `RoleArn`: `str`
- `SystemIds`: `List[str]`
- `Url`: `str`



Optional fields:
- `CertificateArn`: `str`
- `EncryptionContractConfiguration`: `"EncryptionContractConfigurationTypeDef"`


## StreamSelectionTypeDef

```python
from mypy_boto3_mediapackage.type_defs import StreamSelectionTypeDef
```




Optional fields:
- `MaxVideoBitsPerSecond`: `int`
- `MinVideoBitsPerSecond`: `int`
- `StreamOrder`: `StreamOrder`


## UpdateChannelResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import UpdateChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `EgressAccessLogs`: `"EgressAccessLogsTypeDef"`
- `HlsIngest`: `"HlsIngestTypeDef"`
- `Id`: `str`
- `IngressAccessLogs`: `"IngressAccessLogsTypeDef"`
- `Tags`: `Dict[str, str]`


## UpdateOriginEndpointResponseTypeDef

```python
from mypy_boto3_mediapackage.type_defs import UpdateOriginEndpointResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Authorization`: `"AuthorizationTypeDef"`
- `ChannelId`: `str`
- `CmafPackage`: `"CmafPackageTypeDef"`
- `DashPackage`: `"DashPackageTypeDef"`
- `Description`: `str`
- `HlsPackage`: `"HlsPackageTypeDef"`
- `Id`: `str`
- `ManifestName`: `str`
- `MssPackage`: `"MssPackageTypeDef"`
- `Origination`: `Origination`
- `StartoverWindowSeconds`: `int`
- `Tags`: `Dict[str, str]`
- `TimeDelaySeconds`: `int`
- `Url`: `str`
- `Whitelist`: `List[str]`

