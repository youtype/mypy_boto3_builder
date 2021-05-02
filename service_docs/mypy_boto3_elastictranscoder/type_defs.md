# Structures for boto3 ElasticTranscoder module

> [Index](../index.md) > [ElasticTranscoder](./index.md) > Structures

Auto-generated documentation for [ElasticTranscoder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder)
type annotations stubs module [mypy_boto3_elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/).

- [Structures for boto3 ElasticTranscoder module](#structures-for-boto3-elastictranscoder-module)
  - [ArtworkTypeDef](#artworktypedef)
  - [AudioCodecOptionsTypeDef](#audiocodecoptionstypedef)
  - [AudioParametersTypeDef](#audioparameterstypedef)
  - [CaptionFormatTypeDef](#captionformattypedef)
  - [CaptionSourceTypeDef](#captionsourcetypedef)
  - [CaptionsTypeDef](#captionstypedef)
  - [ClipTypeDef](#cliptypedef)
  - [DetectedPropertiesTypeDef](#detectedpropertiestypedef)
  - [EncryptionTypeDef](#encryptiontypedef)
  - [HlsContentProtectionTypeDef](#hlscontentprotectiontypedef)
  - [InputCaptionsTypeDef](#inputcaptionstypedef)
  - [JobAlbumArtTypeDef](#jobalbumarttypedef)
  - [JobInputTypeDef](#jobinputtypedef)
  - [JobOutputTypeDef](#joboutputtypedef)
  - [JobTypeDef](#jobtypedef)
  - [JobWatermarkTypeDef](#jobwatermarktypedef)
  - [NotificationsTypeDef](#notificationstypedef)
  - [PermissionTypeDef](#permissiontypedef)
  - [PipelineOutputConfigTypeDef](#pipelineoutputconfigtypedef)
  - [PipelineTypeDef](#pipelinetypedef)
  - [PlayReadyDrmTypeDef](#playreadydrmtypedef)
  - [PlaylistTypeDef](#playlisttypedef)
  - [PresetTypeDef](#presettypedef)
  - [PresetWatermarkTypeDef](#presetwatermarktypedef)
  - [ResponseMetadata](#responsemetadata)
  - [ThumbnailsTypeDef](#thumbnailstypedef)
  - [TimeSpanTypeDef](#timespantypedef)
  - [TimingTypeDef](#timingtypedef)
  - [VideoParametersTypeDef](#videoparameterstypedef)
  - [WarningTypeDef](#warningtypedef)
  - [CreateJobOutputTypeDef](#createjoboutputtypedef)
  - [CreateJobPlaylistTypeDef](#createjobplaylisttypedef)
  - [CreateJobResponseTypeDef](#createjobresponsetypedef)
  - [CreatePipelineResponseTypeDef](#createpipelineresponsetypedef)
  - [CreatePresetResponseTypeDef](#createpresetresponsetypedef)
  - [ListJobsByPipelineResponseTypeDef](#listjobsbypipelineresponsetypedef)
  - [ListJobsByStatusResponseTypeDef](#listjobsbystatusresponsetypedef)
  - [ListPipelinesResponseTypeDef](#listpipelinesresponsetypedef)
  - [ListPresetsResponseTypeDef](#listpresetsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ReadJobResponseTypeDef](#readjobresponsetypedef)
  - [ReadPipelineResponseTypeDef](#readpipelineresponsetypedef)
  - [ReadPresetResponseTypeDef](#readpresetresponsetypedef)
  - [TestRoleResponseTypeDef](#testroleresponsetypedef)
  - [UpdatePipelineNotificationsResponseTypeDef](#updatepipelinenotificationsresponsetypedef)
  - [UpdatePipelineResponseTypeDef](#updatepipelineresponsetypedef)
  - [UpdatePipelineStatusResponseTypeDef](#updatepipelinestatusresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ArtworkTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ArtworkTypeDef
```




Optional fields:
- `InputKey`: `str`
- `MaxWidth`: `str`
- `MaxHeight`: `str`
- `SizingPolicy`: `str`
- `PaddingPolicy`: `str`
- `AlbumArtFormat`: `str`
- `Encryption`: `"EncryptionTypeDef"`


## AudioCodecOptionsTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import AudioCodecOptionsTypeDef
```




Optional fields:
- `Profile`: `str`
- `BitDepth`: `str`
- `BitOrder`: `str`
- `Signed`: `str`


## AudioParametersTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import AudioParametersTypeDef
```




Optional fields:
- `Codec`: `str`
- `SampleRate`: `str`
- `BitRate`: `str`
- `Channels`: `str`
- `AudioPackingMode`: `str`
- `CodecOptions`: `"AudioCodecOptionsTypeDef"`


## CaptionFormatTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CaptionFormatTypeDef
```




Optional fields:
- `Format`: `str`
- `Pattern`: `str`
- `Encryption`: `"EncryptionTypeDef"`


## CaptionSourceTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CaptionSourceTypeDef
```




Optional fields:
- `Key`: `str`
- `Language`: `str`
- `TimeOffset`: `str`
- `Label`: `str`
- `Encryption`: `"EncryptionTypeDef"`


## CaptionsTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CaptionsTypeDef
```




Optional fields:
- `MergePolicy`: `str`
- `CaptionSources`: `List["CaptionSourceTypeDef"]`
- `CaptionFormats`: `List["CaptionFormatTypeDef"]`


## ClipTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ClipTypeDef
```




Optional fields:
- `TimeSpan`: `"TimeSpanTypeDef"`


## DetectedPropertiesTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import DetectedPropertiesTypeDef
```




Optional fields:
- `Width`: `int`
- `Height`: `int`
- `FrameRate`: `str`
- `FileSize`: `int`
- `DurationMillis`: `int`


## EncryptionTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import EncryptionTypeDef
```




Optional fields:
- `Mode`: `str`
- `Key`: `str`
- `KeyMd5`: `str`
- `InitializationVector`: `str`


## HlsContentProtectionTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import HlsContentProtectionTypeDef
```




Optional fields:
- `Method`: `str`
- `Key`: `str`
- `KeyMd5`: `str`
- `InitializationVector`: `str`
- `LicenseAcquisitionUrl`: `str`
- `KeyStoragePolicy`: `str`


## InputCaptionsTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import InputCaptionsTypeDef
```




Optional fields:
- `MergePolicy`: `str`
- `CaptionSources`: `List["CaptionSourceTypeDef"]`


## JobAlbumArtTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import JobAlbumArtTypeDef
```




Optional fields:
- `MergePolicy`: `str`
- `Artwork`: `List["ArtworkTypeDef"]`


## JobInputTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import JobInputTypeDef
```




Optional fields:
- `Key`: `str`
- `FrameRate`: `str`
- `Resolution`: `str`
- `AspectRatio`: `str`
- `Interlaced`: `str`
- `Container`: `str`
- `Encryption`: `"EncryptionTypeDef"`
- `TimeSpan`: `"TimeSpanTypeDef"`
- `InputCaptions`: `"InputCaptionsTypeDef"`
- `DetectedProperties`: `"DetectedPropertiesTypeDef"`


## JobOutputTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import JobOutputTypeDef
```




Optional fields:
- `Id`: `str`
- `Key`: `str`
- `ThumbnailPattern`: `str`
- `ThumbnailEncryption`: `"EncryptionTypeDef"`
- `Rotate`: `str`
- `PresetId`: `str`
- `SegmentDuration`: `str`
- `Status`: `str`
- `StatusDetail`: `str`
- `Duration`: `int`
- `Width`: `int`
- `Height`: `int`
- `FrameRate`: `str`
- `FileSize`: `int`
- `DurationMillis`: `int`
- `Watermarks`: `List["JobWatermarkTypeDef"]`
- `AlbumArt`: `"JobAlbumArtTypeDef"`
- `Composition`: `List["ClipTypeDef"]`
- `Captions`: `"CaptionsTypeDef"`
- `Encryption`: `"EncryptionTypeDef"`
- `AppliedColorSpaceConversion`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## JobTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import JobTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `PipelineId`: `str`
- `Input`: `"JobInputTypeDef"`
- `Inputs`: `List["JobInputTypeDef"]`
- `Output`: `"JobOutputTypeDef"`
- `Outputs`: `List["JobOutputTypeDef"]`
- `OutputKeyPrefix`: `str`
- `Playlists`: `List["PlaylistTypeDef"]`
- `Status`: `str`
- `UserMetadata`: `Dict[str, str]`
- `Timing`: `"TimingTypeDef"`


## JobWatermarkTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import JobWatermarkTypeDef
```




Optional fields:
- `PresetWatermarkId`: `str`
- `InputKey`: `str`
- `Encryption`: `"EncryptionTypeDef"`


## NotificationsTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import NotificationsTypeDef
```




Optional fields:
- `Progressing`: `str`
- `Completed`: `str`
- `Warning`: `str`
- `Error`: `str`


## PermissionTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PermissionTypeDef
```




Optional fields:
- `GranteeType`: `str`
- `Grantee`: `str`
- `Access`: `List[str]`


## PipelineOutputConfigTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PipelineOutputConfigTypeDef
```




Optional fields:
- `Bucket`: `str`
- `StorageClass`: `str`
- `Permissions`: `List["PermissionTypeDef"]`


## PipelineTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PipelineTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Status`: `str`
- `InputBucket`: `str`
- `OutputBucket`: `str`
- `Role`: `str`
- `AwsKmsKeyArn`: `str`
- `Notifications`: `"NotificationsTypeDef"`
- `ContentConfig`: `"PipelineOutputConfigTypeDef"`
- `ThumbnailConfig`: `"PipelineOutputConfigTypeDef"`


## PlayReadyDrmTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PlayReadyDrmTypeDef
```




Optional fields:
- `Format`: `str`
- `Key`: `str`
- `KeyMd5`: `str`
- `KeyId`: `str`
- `InitializationVector`: `str`
- `LicenseAcquisitionUrl`: `str`


## PlaylistTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PlaylistTypeDef
```




Optional fields:
- `Name`: `str`
- `Format`: `str`
- `OutputKeys`: `List[str]`
- `HlsContentProtection`: `"HlsContentProtectionTypeDef"`
- `PlayReadyDrm`: `"PlayReadyDrmTypeDef"`
- `Status`: `str`
- `StatusDetail`: `str`


## PresetTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PresetTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Description`: `str`
- `Container`: `str`
- `Audio`: `"AudioParametersTypeDef"`
- `Video`: `"VideoParametersTypeDef"`
- `Thumbnails`: `"ThumbnailsTypeDef"`
- `Type`: `str`


## PresetWatermarkTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PresetWatermarkTypeDef
```




Optional fields:
- `Id`: `str`
- `MaxWidth`: `str`
- `MaxHeight`: `str`
- `SizingPolicy`: `str`
- `HorizontalAlign`: `str`
- `HorizontalOffset`: `str`
- `VerticalAlign`: `str`
- `VerticalOffset`: `str`
- `Opacity`: `str`
- `Target`: `str`


## ResponseMetadata

```python
from mypy_boto3_elastictranscoder.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## ThumbnailsTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ThumbnailsTypeDef
```




Optional fields:
- `Format`: `str`
- `Interval`: `str`
- `Resolution`: `str`
- `AspectRatio`: `str`
- `MaxWidth`: `str`
- `MaxHeight`: `str`
- `SizingPolicy`: `str`
- `PaddingPolicy`: `str`


## TimeSpanTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import TimeSpanTypeDef
```




Optional fields:
- `StartTime`: `str`
- `Duration`: `str`


## TimingTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import TimingTypeDef
```




Optional fields:
- `SubmitTimeMillis`: `int`
- `StartTimeMillis`: `int`
- `FinishTimeMillis`: `int`


## VideoParametersTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import VideoParametersTypeDef
```




Optional fields:
- `Codec`: `str`
- `CodecOptions`: `Dict[str, str]`
- `KeyframesMaxDist`: `str`
- `FixedGOP`: `str`
- `BitRate`: `str`
- `FrameRate`: `str`
- `MaxFrameRate`: `str`
- `Resolution`: `str`
- `AspectRatio`: `str`
- `MaxWidth`: `str`
- `MaxHeight`: `str`
- `DisplayAspectRatio`: `str`
- `SizingPolicy`: `str`
- `PaddingPolicy`: `str`
- `Watermarks`: `List["PresetWatermarkTypeDef"]`


## WarningTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import WarningTypeDef
```




Optional fields:
- `Code`: `str`
- `Message`: `str`


## CreateJobOutputTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CreateJobOutputTypeDef
```




Optional fields:
- `Key`: `str`
- `ThumbnailPattern`: `str`
- `ThumbnailEncryption`: `"EncryptionTypeDef"`
- `Rotate`: `str`
- `PresetId`: `str`
- `SegmentDuration`: `str`
- `Watermarks`: `List["JobWatermarkTypeDef"]`
- `AlbumArt`: `"JobAlbumArtTypeDef"`
- `Composition`: `List["ClipTypeDef"]`
- `Captions`: `"CaptionsTypeDef"`
- `Encryption`: `"EncryptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateJobPlaylistTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CreateJobPlaylistTypeDef
```




Optional fields:
- `Name`: `str`
- `Format`: `str`
- `OutputKeys`: `List[str]`
- `HlsContentProtection`: `"HlsContentProtectionTypeDef"`
- `PlayReadyDrm`: `"PlayReadyDrmTypeDef"`


## CreateJobResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CreateJobResponseTypeDef
```




Optional fields:
- `Job`: `"JobTypeDef"`


## CreatePipelineResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CreatePipelineResponseTypeDef
```




Optional fields:
- `Pipeline`: `"PipelineTypeDef"`
- `Warnings`: `List["WarningTypeDef"]`


## CreatePresetResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import CreatePresetResponseTypeDef
```




Optional fields:
- `Preset`: `"PresetTypeDef"`
- `Warning`: `str`


## ListJobsByPipelineResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ListJobsByPipelineResponseTypeDef
```




Optional fields:
- `Jobs`: `List["JobTypeDef"]`
- `NextPageToken`: `str`


## ListJobsByStatusResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ListJobsByStatusResponseTypeDef
```




Optional fields:
- `Jobs`: `List["JobTypeDef"]`
- `NextPageToken`: `str`


## ListPipelinesResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ListPipelinesResponseTypeDef
```




Optional fields:
- `Pipelines`: `List["PipelineTypeDef"]`
- `NextPageToken`: `str`


## ListPresetsResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ListPresetsResponseTypeDef
```




Optional fields:
- `Presets`: `List["PresetTypeDef"]`
- `NextPageToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ReadJobResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ReadJobResponseTypeDef
```




Optional fields:
- `Job`: `"JobTypeDef"`


## ReadPipelineResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ReadPipelineResponseTypeDef
```




Optional fields:
- `Pipeline`: `"PipelineTypeDef"`
- `Warnings`: `List["WarningTypeDef"]`


## ReadPresetResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import ReadPresetResponseTypeDef
```




Optional fields:
- `Preset`: `"PresetTypeDef"`


## TestRoleResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import TestRoleResponseTypeDef
```




Optional fields:
- `Success`: `str`
- `Messages`: `List[str]`


## UpdatePipelineNotificationsResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import UpdatePipelineNotificationsResponseTypeDef
```




Optional fields:
- `Pipeline`: `"PipelineTypeDef"`


## UpdatePipelineResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import UpdatePipelineResponseTypeDef
```




Optional fields:
- `Pipeline`: `"PipelineTypeDef"`
- `Warnings`: `List["WarningTypeDef"]`


## UpdatePipelineStatusResponseTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import UpdatePipelineStatusResponseTypeDef
```




Optional fields:
- `Pipeline`: `"PipelineTypeDef"`


## WaiterConfigTypeDef

```python
from mypy_boto3_elastictranscoder.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

