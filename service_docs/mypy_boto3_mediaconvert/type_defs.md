# Structures for boto3 MediaConvert module

> [Index](../index.md) > [MediaConvert](./index.md) > Structures

Auto-generated documentation for [MediaConvert](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html#MediaConvert)
type annotations stubs module [mypy_boto3_mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert/).

- [Structures for boto3 MediaConvert module](#structures-for-boto3-mediaconvert-module)
  - [AacSettingsTypeDef](#aacsettingstypedef)
  - [Ac3SettingsTypeDef](#ac3settingstypedef)
  - [AccelerationSettingsTypeDef](#accelerationsettingstypedef)
  - [AiffSettingsTypeDef](#aiffsettingstypedef)
  - [AncillarySourceSettingsTypeDef](#ancillarysourcesettingstypedef)
  - [AudioChannelTaggingSettingsTypeDef](#audiochanneltaggingsettingstypedef)
  - [AudioCodecSettingsTypeDef](#audiocodecsettingstypedef)
  - [AudioDescriptionTypeDef](#audiodescriptiontypedef)
  - [AudioNormalizationSettingsTypeDef](#audionormalizationsettingstypedef)
  - [AudioSelectorGroupTypeDef](#audioselectorgrouptypedef)
  - [AudioSelectorTypeDef](#audioselectortypedef)
  - [AutomatedAbrSettingsTypeDef](#automatedabrsettingstypedef)
  - [AutomatedEncodingSettingsTypeDef](#automatedencodingsettingstypedef)
  - [Av1QvbrSettingsTypeDef](#av1qvbrsettingstypedef)
  - [Av1SettingsTypeDef](#av1settingstypedef)
  - [AvailBlankingTypeDef](#availblankingtypedef)
  - [AvcIntraSettingsTypeDef](#avcintrasettingstypedef)
  - [AvcIntraUhdSettingsTypeDef](#avcintrauhdsettingstypedef)
  - [BurninDestinationSettingsTypeDef](#burnindestinationsettingstypedef)
  - [CaptionDescriptionPresetTypeDef](#captiondescriptionpresettypedef)
  - [CaptionDescriptionTypeDef](#captiondescriptiontypedef)
  - [CaptionDestinationSettingsTypeDef](#captiondestinationsettingstypedef)
  - [CaptionSelectorTypeDef](#captionselectortypedef)
  - [CaptionSourceFramerateTypeDef](#captionsourceframeratetypedef)
  - [CaptionSourceSettingsTypeDef](#captionsourcesettingstypedef)
  - [ChannelMappingTypeDef](#channelmappingtypedef)
  - [CmafAdditionalManifestTypeDef](#cmafadditionalmanifesttypedef)
  - [CmafEncryptionSettingsTypeDef](#cmafencryptionsettingstypedef)
  - [CmafGroupSettingsTypeDef](#cmafgroupsettingstypedef)
  - [CmfcSettingsTypeDef](#cmfcsettingstypedef)
  - [ColorCorrectorTypeDef](#colorcorrectortypedef)
  - [ContainerSettingsTypeDef](#containersettingstypedef)
  - [DashAdditionalManifestTypeDef](#dashadditionalmanifesttypedef)
  - [DashIsoEncryptionSettingsTypeDef](#dashisoencryptionsettingstypedef)
  - [DashIsoGroupSettingsTypeDef](#dashisogroupsettingstypedef)
  - [DeinterlacerTypeDef](#deinterlacertypedef)
  - [DestinationSettingsTypeDef](#destinationsettingstypedef)
  - [DolbyVisionLevel6MetadataTypeDef](#dolbyvisionlevel6metadatatypedef)
  - [DolbyVisionTypeDef](#dolbyvisiontypedef)
  - [DvbNitSettingsTypeDef](#dvbnitsettingstypedef)
  - [DvbSdtSettingsTypeDef](#dvbsdtsettingstypedef)
  - [DvbSubDestinationSettingsTypeDef](#dvbsubdestinationsettingstypedef)
  - [DvbSubSourceSettingsTypeDef](#dvbsubsourcesettingstypedef)
  - [DvbTdtSettingsTypeDef](#dvbtdtsettingstypedef)
  - [Eac3AtmosSettingsTypeDef](#eac3atmossettingstypedef)
  - [Eac3SettingsTypeDef](#eac3settingstypedef)
  - [EmbeddedDestinationSettingsTypeDef](#embeddeddestinationsettingstypedef)
  - [EmbeddedSourceSettingsTypeDef](#embeddedsourcesettingstypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [EsamManifestConfirmConditionNotificationTypeDef](#esammanifestconfirmconditionnotificationtypedef)
  - [EsamSettingsTypeDef](#esamsettingstypedef)
  - [EsamSignalProcessingNotificationTypeDef](#esamsignalprocessingnotificationtypedef)
  - [F4vSettingsTypeDef](#f4vsettingstypedef)
  - [FileGroupSettingsTypeDef](#filegroupsettingstypedef)
  - [FileSourceSettingsTypeDef](#filesourcesettingstypedef)
  - [FrameCaptureSettingsTypeDef](#framecapturesettingstypedef)
  - [H264QvbrSettingsTypeDef](#h264qvbrsettingstypedef)
  - [H264SettingsTypeDef](#h264settingstypedef)
  - [H265QvbrSettingsTypeDef](#h265qvbrsettingstypedef)
  - [H265SettingsTypeDef](#h265settingstypedef)
  - [Hdr10MetadataTypeDef](#hdr10metadatatypedef)
  - [HlsAdditionalManifestTypeDef](#hlsadditionalmanifesttypedef)
  - [HlsCaptionLanguageMappingTypeDef](#hlscaptionlanguagemappingtypedef)
  - [HlsEncryptionSettingsTypeDef](#hlsencryptionsettingstypedef)
  - [HlsGroupSettingsTypeDef](#hlsgroupsettingstypedef)
  - [HlsSettingsTypeDef](#hlssettingstypedef)
  - [HopDestinationTypeDef](#hopdestinationtypedef)
  - [Id3InsertionTypeDef](#id3insertiontypedef)
  - [ImageInserterTypeDef](#imageinsertertypedef)
  - [ImscDestinationSettingsTypeDef](#imscdestinationsettingstypedef)
  - [InputClippingTypeDef](#inputclippingtypedef)
  - [InputDecryptionSettingsTypeDef](#inputdecryptionsettingstypedef)
  - [InputTemplateTypeDef](#inputtemplatetypedef)
  - [InputTypeDef](#inputtypedef)
  - [InsertableImageTypeDef](#insertableimagetypedef)
  - [JobMessagesTypeDef](#jobmessagestypedef)
  - [JobSettingsTypeDef](#jobsettingstypedef)
  - [JobTemplateSettingsTypeDef](#jobtemplatesettingstypedef)
  - [JobTemplateTypeDef](#jobtemplatetypedef)
  - [JobTypeDef](#jobtypedef)
  - [M2tsScte35EsamTypeDef](#m2tsscte35esamtypedef)
  - [M2tsSettingsTypeDef](#m2tssettingstypedef)
  - [M3u8SettingsTypeDef](#m3u8settingstypedef)
  - [MotionImageInserterTypeDef](#motionimageinsertertypedef)
  - [MotionImageInsertionFramerateTypeDef](#motionimageinsertionframeratetypedef)
  - [MotionImageInsertionOffsetTypeDef](#motionimageinsertionoffsettypedef)
  - [MovSettingsTypeDef](#movsettingstypedef)
  - [Mp2SettingsTypeDef](#mp2settingstypedef)
  - [Mp3SettingsTypeDef](#mp3settingstypedef)
  - [Mp4SettingsTypeDef](#mp4settingstypedef)
  - [MpdSettingsTypeDef](#mpdsettingstypedef)
  - [Mpeg2SettingsTypeDef](#mpeg2settingstypedef)
  - [MsSmoothAdditionalManifestTypeDef](#mssmoothadditionalmanifesttypedef)
  - [MsSmoothEncryptionSettingsTypeDef](#mssmoothencryptionsettingstypedef)
  - [MsSmoothGroupSettingsTypeDef](#mssmoothgroupsettingstypedef)
  - [MxfSettingsTypeDef](#mxfsettingstypedef)
  - [NexGuardFileMarkerSettingsTypeDef](#nexguardfilemarkersettingstypedef)
  - [NielsenConfigurationTypeDef](#nielsenconfigurationtypedef)
  - [NielsenNonLinearWatermarkSettingsTypeDef](#nielsennonlinearwatermarksettingstypedef)
  - [NoiseReducerFilterSettingsTypeDef](#noisereducerfiltersettingstypedef)
  - [NoiseReducerSpatialFilterSettingsTypeDef](#noisereducerspatialfiltersettingstypedef)
  - [NoiseReducerTemporalFilterSettingsTypeDef](#noisereducertemporalfiltersettingstypedef)
  - [NoiseReducerTypeDef](#noisereducertypedef)
  - [OpusSettingsTypeDef](#opussettingstypedef)
  - [OutputChannelMappingTypeDef](#outputchannelmappingtypedef)
  - [OutputDetailTypeDef](#outputdetailtypedef)
  - [OutputGroupDetailTypeDef](#outputgroupdetailtypedef)
  - [OutputGroupSettingsTypeDef](#outputgroupsettingstypedef)
  - [OutputGroupTypeDef](#outputgrouptypedef)
  - [OutputSettingsTypeDef](#outputsettingstypedef)
  - [OutputTypeDef](#outputtypedef)
  - [PartnerWatermarkingTypeDef](#partnerwatermarkingtypedef)
  - [PresetSettingsTypeDef](#presetsettingstypedef)
  - [PresetTypeDef](#presettypedef)
  - [ProresSettingsTypeDef](#proressettingstypedef)
  - [QueueTransitionTypeDef](#queuetransitiontypedef)
  - [QueueTypeDef](#queuetypedef)
  - [RectangleTypeDef](#rectangletypedef)
  - [RemixSettingsTypeDef](#remixsettingstypedef)
  - [ReservationPlanTypeDef](#reservationplantypedef)
  - [ResourceTagsTypeDef](#resourcetagstypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3DestinationAccessControlTypeDef](#s3destinationaccesscontroltypedef)
  - [S3DestinationSettingsTypeDef](#s3destinationsettingstypedef)
  - [S3EncryptionSettingsTypeDef](#s3encryptionsettingstypedef)
  - [SccDestinationSettingsTypeDef](#sccdestinationsettingstypedef)
  - [SpekeKeyProviderCmafTypeDef](#spekekeyprovidercmaftypedef)
  - [SpekeKeyProviderTypeDef](#spekekeyprovidertypedef)
  - [StaticKeyProviderTypeDef](#statickeyprovidertypedef)
  - [TeletextDestinationSettingsTypeDef](#teletextdestinationsettingstypedef)
  - [TeletextSourceSettingsTypeDef](#teletextsourcesettingstypedef)
  - [TimecodeBurninTypeDef](#timecodeburnintypedef)
  - [TimecodeConfigTypeDef](#timecodeconfigtypedef)
  - [TimedMetadataInsertionTypeDef](#timedmetadatainsertiontypedef)
  - [TimingTypeDef](#timingtypedef)
  - [TrackSourceSettingsTypeDef](#tracksourcesettingstypedef)
  - [TtmlDestinationSettingsTypeDef](#ttmldestinationsettingstypedef)
  - [Vc3SettingsTypeDef](#vc3settingstypedef)
  - [VideoCodecSettingsTypeDef](#videocodecsettingstypedef)
  - [VideoDescriptionTypeDef](#videodescriptiontypedef)
  - [VideoDetailTypeDef](#videodetailtypedef)
  - [VideoPreprocessorTypeDef](#videopreprocessortypedef)
  - [VideoSelectorTypeDef](#videoselectortypedef)
  - [VorbisSettingsTypeDef](#vorbissettingstypedef)
  - [Vp8SettingsTypeDef](#vp8settingstypedef)
  - [Vp9SettingsTypeDef](#vp9settingstypedef)
  - [WavSettingsTypeDef](#wavsettingstypedef)
  - [WebvttDestinationSettingsTypeDef](#webvttdestinationsettingstypedef)
  - [CreateJobResponseTypeDef](#createjobresponsetypedef)
  - [CreateJobTemplateResponseTypeDef](#createjobtemplateresponsetypedef)
  - [CreatePresetResponseTypeDef](#createpresetresponsetypedef)
  - [CreateQueueResponseTypeDef](#createqueueresponsetypedef)
  - [DescribeEndpointsResponseTypeDef](#describeendpointsresponsetypedef)
  - [GetJobResponseTypeDef](#getjobresponsetypedef)
  - [GetJobTemplateResponseTypeDef](#getjobtemplateresponsetypedef)
  - [GetPresetResponseTypeDef](#getpresetresponsetypedef)
  - [GetQueueResponseTypeDef](#getqueueresponsetypedef)
  - [ListJobTemplatesResponseTypeDef](#listjobtemplatesresponsetypedef)
  - [ListJobsResponseTypeDef](#listjobsresponsetypedef)
  - [ListPresetsResponseTypeDef](#listpresetsresponsetypedef)
  - [ListQueuesResponseTypeDef](#listqueuesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ReservationPlanSettingsTypeDef](#reservationplansettingstypedef)
  - [UpdateJobTemplateResponseTypeDef](#updatejobtemplateresponsetypedef)
  - [UpdatePresetResponseTypeDef](#updatepresetresponsetypedef)
  - [UpdateQueueResponseTypeDef](#updatequeueresponsetypedef)

## AacSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AacSettingsTypeDef
```




Optional fields:
- `AudioDescriptionBroadcasterMix`: `AacAudioDescriptionBroadcasterMix`
- `Bitrate`: `int`
- `CodecProfile`: `AacCodecProfile`
- `CodingMode`: `AacCodingMode`
- `RateControlMode`: `AacRateControlMode`
- `RawFormat`: `AacRawFormat`
- `SampleRate`: `int`
- `Specification`: `AacSpecification`
- `VbrQuality`: `AacVbrQuality`


## Ac3SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Ac3SettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `BitstreamMode`: `Ac3BitstreamMode`
- `CodingMode`: `Ac3CodingMode`
- `Dialnorm`: `int`
- `DynamicRangeCompressionLine`: `Ac3DynamicRangeCompressionLine`
- `DynamicRangeCompressionProfile`: `Ac3DynamicRangeCompressionProfile`
- `DynamicRangeCompressionRf`: `Ac3DynamicRangeCompressionRf`
- `LfeFilter`: `Ac3LfeFilter`
- `MetadataControl`: `Ac3MetadataControl`
- `SampleRate`: `int`


## AccelerationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AccelerationSettingsTypeDef
```


Required fields:
- `Mode`: `AccelerationMode`




## AiffSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AiffSettingsTypeDef
```




Optional fields:
- `BitDepth`: `int`
- `Channels`: `int`
- `SampleRate`: `int`


## AncillarySourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AncillarySourceSettingsTypeDef
```




Optional fields:
- `Convert608To708`: `AncillaryConvert608To708`
- `SourceAncillaryChannelNumber`: `int`
- `TerminateCaptions`: `AncillaryTerminateCaptions`


## AudioChannelTaggingSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AudioChannelTaggingSettingsTypeDef
```




Optional fields:
- `ChannelTag`: `AudioChannelTag`


## AudioCodecSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AudioCodecSettingsTypeDef
```




Optional fields:
- `AacSettings`: `"AacSettingsTypeDef"`
- `Ac3Settings`: `"Ac3SettingsTypeDef"`
- `AiffSettings`: `"AiffSettingsTypeDef"`
- `Codec`: `AudioCodec`
- `Eac3AtmosSettings`: `"Eac3AtmosSettingsTypeDef"`
- `Eac3Settings`: `"Eac3SettingsTypeDef"`
- `Mp2Settings`: `"Mp2SettingsTypeDef"`
- `Mp3Settings`: `"Mp3SettingsTypeDef"`
- `OpusSettings`: `"OpusSettingsTypeDef"`
- `VorbisSettings`: `"VorbisSettingsTypeDef"`
- `WavSettings`: `"WavSettingsTypeDef"`


## AudioDescriptionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AudioDescriptionTypeDef
```




Optional fields:
- `AudioChannelTaggingSettings`: `"AudioChannelTaggingSettingsTypeDef"`
- `AudioNormalizationSettings`: `"AudioNormalizationSettingsTypeDef"`
- `AudioSourceName`: `str`
- `AudioType`: `int`
- `AudioTypeControl`: `AudioTypeControl`
- `CodecSettings`: `"AudioCodecSettingsTypeDef"`
- `CustomLanguageCode`: `str`
- `LanguageCode`: `LanguageCode`
- `LanguageCodeControl`: `AudioLanguageCodeControl`
- `RemixSettings`: `"RemixSettingsTypeDef"`
- `StreamName`: `str`


## AudioNormalizationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AudioNormalizationSettingsTypeDef
```




Optional fields:
- `Algorithm`: `AudioNormalizationAlgorithm`
- `AlgorithmControl`: `AudioNormalizationAlgorithmControl`
- `CorrectionGateLevel`: `int`
- `LoudnessLogging`: `AudioNormalizationLoudnessLogging`
- `PeakCalculation`: `AudioNormalizationPeakCalculation`
- `TargetLkfs`: `float`


## AudioSelectorGroupTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AudioSelectorGroupTypeDef
```




Optional fields:
- `AudioSelectorNames`: `List[str]`


## AudioSelectorTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AudioSelectorTypeDef
```




Optional fields:
- `CustomLanguageCode`: `str`
- `DefaultSelection`: `AudioDefaultSelection`
- `ExternalAudioFileInput`: `str`
- `LanguageCode`: `LanguageCode`
- `Offset`: `int`
- `Pids`: `List[int]`
- `ProgramSelection`: `int`
- `RemixSettings`: `"RemixSettingsTypeDef"`
- `SelectorType`: `AudioSelectorType`
- `Tracks`: `List[int]`


## AutomatedAbrSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AutomatedAbrSettingsTypeDef
```




Optional fields:
- `MaxAbrBitrate`: `int`
- `MaxRenditions`: `int`
- `MinAbrBitrate`: `int`


## AutomatedEncodingSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AutomatedEncodingSettingsTypeDef
```




Optional fields:
- `AbrSettings`: `"AutomatedAbrSettingsTypeDef"`


## Av1QvbrSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Av1QvbrSettingsTypeDef
```




Optional fields:
- `QvbrQualityLevel`: `int`
- `QvbrQualityLevelFineTune`: `float`


## Av1SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Av1SettingsTypeDef
```




Optional fields:
- `AdaptiveQuantization`: `Av1AdaptiveQuantization`
- `FramerateControl`: `Av1FramerateControl`
- `FramerateConversionAlgorithm`: `Av1FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopSize`: `float`
- `MaxBitrate`: `int`
- `NumberBFramesBetweenReferenceFrames`: `int`
- `QvbrSettings`: `"Av1QvbrSettingsTypeDef"`
- `RateControlMode`: `Av1RateControlMode`
- `Slices`: `int`
- `SpatialAdaptiveQuantization`: `Av1SpatialAdaptiveQuantization`


## AvailBlankingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AvailBlankingTypeDef
```




Optional fields:
- `AvailBlankingImage`: `str`


## AvcIntraSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AvcIntraSettingsTypeDef
```




Optional fields:
- `AvcIntraClass`: `AvcIntraClass`
- `AvcIntraUhdSettings`: `"AvcIntraUhdSettingsTypeDef"`
- `FramerateControl`: `AvcIntraFramerateControl`
- `FramerateConversionAlgorithm`: `AvcIntraFramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `InterlaceMode`: `AvcIntraInterlaceMode`
- `ScanTypeConversionMode`: `AvcIntraScanTypeConversionMode`
- `SlowPal`: `AvcIntraSlowPal`
- `Telecine`: `AvcIntraTelecine`


## AvcIntraUhdSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import AvcIntraUhdSettingsTypeDef
```




Optional fields:
- `QualityTuningLevel`: `AvcIntraUhdQualityTuningLevel`


## BurninDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import BurninDestinationSettingsTypeDef
```




Optional fields:
- `Alignment`: `BurninSubtitleAlignment`
- `BackgroundColor`: `BurninSubtitleBackgroundColor`
- `BackgroundOpacity`: `int`
- `FontColor`: `BurninSubtitleFontColor`
- `FontOpacity`: `int`
- `FontResolution`: `int`
- `FontScript`: `FontScript`
- `FontSize`: `int`
- `OutlineColor`: `BurninSubtitleOutlineColor`
- `OutlineSize`: `int`
- `ShadowColor`: `BurninSubtitleShadowColor`
- `ShadowOpacity`: `int`
- `ShadowXOffset`: `int`
- `ShadowYOffset`: `int`
- `TeletextSpacing`: `BurninSubtitleTeletextSpacing`
- `XPosition`: `int`
- `YPosition`: `int`


## CaptionDescriptionPresetTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CaptionDescriptionPresetTypeDef
```




Optional fields:
- `CustomLanguageCode`: `str`
- `DestinationSettings`: `"CaptionDestinationSettingsTypeDef"`
- `LanguageCode`: `LanguageCode`
- `LanguageDescription`: `str`


## CaptionDescriptionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CaptionDescriptionTypeDef
```




Optional fields:
- `CaptionSelectorName`: `str`
- `CustomLanguageCode`: `str`
- `DestinationSettings`: `"CaptionDestinationSettingsTypeDef"`
- `LanguageCode`: `LanguageCode`
- `LanguageDescription`: `str`


## CaptionDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CaptionDestinationSettingsTypeDef
```




Optional fields:
- `BurninDestinationSettings`: `"BurninDestinationSettingsTypeDef"`
- `DestinationType`: `CaptionDestinationType`
- `DvbSubDestinationSettings`: `"DvbSubDestinationSettingsTypeDef"`
- `EmbeddedDestinationSettings`: `"EmbeddedDestinationSettingsTypeDef"`
- `ImscDestinationSettings`: `"ImscDestinationSettingsTypeDef"`
- `SccDestinationSettings`: `"SccDestinationSettingsTypeDef"`
- `TeletextDestinationSettings`: `"TeletextDestinationSettingsTypeDef"`
- `TtmlDestinationSettings`: `"TtmlDestinationSettingsTypeDef"`
- `WebvttDestinationSettings`: `"WebvttDestinationSettingsTypeDef"`


## CaptionSelectorTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CaptionSelectorTypeDef
```




Optional fields:
- `CustomLanguageCode`: `str`
- `LanguageCode`: `LanguageCode`
- `SourceSettings`: `"CaptionSourceSettingsTypeDef"`


## CaptionSourceFramerateTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CaptionSourceFramerateTypeDef
```




Optional fields:
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`


## CaptionSourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CaptionSourceSettingsTypeDef
```




Optional fields:
- `AncillarySourceSettings`: `"AncillarySourceSettingsTypeDef"`
- `DvbSubSourceSettings`: `"DvbSubSourceSettingsTypeDef"`
- `EmbeddedSourceSettings`: `"EmbeddedSourceSettingsTypeDef"`
- `FileSourceSettings`: `"FileSourceSettingsTypeDef"`
- `SourceType`: `CaptionSourceType`
- `TeletextSourceSettings`: `"TeletextSourceSettingsTypeDef"`
- `TrackSourceSettings`: `"TrackSourceSettingsTypeDef"`


## ChannelMappingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ChannelMappingTypeDef
```




Optional fields:
- `OutputChannels`: `List["OutputChannelMappingTypeDef"]`


## CmafAdditionalManifestTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CmafAdditionalManifestTypeDef
```




Optional fields:
- `ManifestNameModifier`: `str`
- `SelectedOutputs`: `List[str]`


## CmafEncryptionSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CmafEncryptionSettingsTypeDef
```




Optional fields:
- `ConstantInitializationVector`: `str`
- `EncryptionMethod`: `CmafEncryptionType`
- `InitializationVectorInManifest`: `CmafInitializationVectorInManifest`
- `SpekeKeyProvider`: `"SpekeKeyProviderCmafTypeDef"`
- `StaticKeyProvider`: `"StaticKeyProviderTypeDef"`
- `Type`: `CmafKeyProviderType`


## CmafGroupSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CmafGroupSettingsTypeDef
```




Optional fields:
- `AdditionalManifests`: `List["CmafAdditionalManifestTypeDef"]`
- `BaseUrl`: `str`
- `ClientCache`: `CmafClientCache`
- `CodecSpecification`: `CmafCodecSpecification`
- `Destination`: `str`
- `DestinationSettings`: `"DestinationSettingsTypeDef"`
- `Encryption`: `"CmafEncryptionSettingsTypeDef"`
- `FragmentLength`: `int`
- `ManifestCompression`: `CmafManifestCompression`
- `ManifestDurationFormat`: `CmafManifestDurationFormat`
- `MinBufferTime`: `int`
- `MinFinalSegmentLength`: `float`
- `MpdProfile`: `CmafMpdProfile`
- `PtsOffsetHandlingForBFrames`: `CmafPtsOffsetHandlingForBFrames`
- `SegmentControl`: `CmafSegmentControl`
- `SegmentLength`: `int`
- `StreamInfResolution`: `CmafStreamInfResolution`
- `WriteDashManifest`: `CmafWriteDASHManifest`
- `WriteHlsManifest`: `CmafWriteHLSManifest`
- `WriteSegmentTimelineInRepresentation`: `CmafWriteSegmentTimelineInRepresentation`


## CmfcSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CmfcSettingsTypeDef
```




Optional fields:
- `AudioDuration`: `CmfcAudioDuration`
- `AudioGroupId`: `str`
- `AudioRenditionSets`: `str`
- `AudioTrackType`: `CmfcAudioTrackType`
- `DescriptiveVideoServiceFlag`: `CmfcDescriptiveVideoServiceFlag`
- `IFrameOnlyManifest`: `CmfcIFrameOnlyManifest`
- `Scte35Esam`: `CmfcScte35Esam`
- `Scte35Source`: `CmfcScte35Source`


## ColorCorrectorTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ColorCorrectorTypeDef
```




Optional fields:
- `Brightness`: `int`
- `ColorSpaceConversion`: `ColorSpaceConversion`
- `Contrast`: `int`
- `Hdr10Metadata`: `"Hdr10MetadataTypeDef"`
- `Hue`: `int`
- `Saturation`: `int`


## ContainerSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ContainerSettingsTypeDef
```




Optional fields:
- `CmfcSettings`: `"CmfcSettingsTypeDef"`
- `Container`: `ContainerType`
- `F4vSettings`: `"F4vSettingsTypeDef"`
- `M2tsSettings`: `"M2tsSettingsTypeDef"`
- `M3u8Settings`: `"M3u8SettingsTypeDef"`
- `MovSettings`: `"MovSettingsTypeDef"`
- `Mp4Settings`: `"Mp4SettingsTypeDef"`
- `MpdSettings`: `"MpdSettingsTypeDef"`
- `MxfSettings`: `"MxfSettingsTypeDef"`


## DashAdditionalManifestTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DashAdditionalManifestTypeDef
```




Optional fields:
- `ManifestNameModifier`: `str`
- `SelectedOutputs`: `List[str]`


## DashIsoEncryptionSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DashIsoEncryptionSettingsTypeDef
```




Optional fields:
- `PlaybackDeviceCompatibility`: `DashIsoPlaybackDeviceCompatibility`
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`


## DashIsoGroupSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DashIsoGroupSettingsTypeDef
```




Optional fields:
- `AdditionalManifests`: `List["DashAdditionalManifestTypeDef"]`
- `AudioChannelConfigSchemeIdUri`: `DashIsoGroupAudioChannelConfigSchemeIdUri`
- `BaseUrl`: `str`
- `Destination`: `str`
- `DestinationSettings`: `"DestinationSettingsTypeDef"`
- `Encryption`: `"DashIsoEncryptionSettingsTypeDef"`
- `FragmentLength`: `int`
- `HbbtvCompliance`: `DashIsoHbbtvCompliance`
- `MinBufferTime`: `int`
- `MinFinalSegmentLength`: `float`
- `MpdProfile`: `DashIsoMpdProfile`
- `PtsOffsetHandlingForBFrames`: `DashIsoPtsOffsetHandlingForBFrames`
- `SegmentControl`: `DashIsoSegmentControl`
- `SegmentLength`: `int`
- `WriteSegmentTimelineInRepresentation`: `DashIsoWriteSegmentTimelineInRepresentation`


## DeinterlacerTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DeinterlacerTypeDef
```




Optional fields:
- `Algorithm`: `DeinterlaceAlgorithm`
- `Control`: `DeinterlacerControl`
- `Mode`: `DeinterlacerMode`


## DestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DestinationSettingsTypeDef
```




Optional fields:
- `S3Settings`: `"S3DestinationSettingsTypeDef"`


## DolbyVisionLevel6MetadataTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DolbyVisionLevel6MetadataTypeDef
```




Optional fields:
- `MaxCll`: `int`
- `MaxFall`: `int`


## DolbyVisionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DolbyVisionTypeDef
```




Optional fields:
- `L6Metadata`: `"DolbyVisionLevel6MetadataTypeDef"`
- `L6Mode`: `DolbyVisionLevel6Mode`
- `Profile`: `DolbyVisionProfile`


## DvbNitSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DvbNitSettingsTypeDef
```




Optional fields:
- `NetworkId`: `int`
- `NetworkName`: `str`
- `NitInterval`: `int`


## DvbSdtSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DvbSdtSettingsTypeDef
```




Optional fields:
- `OutputSdt`: `OutputSdt`
- `SdtInterval`: `int`
- `ServiceName`: `str`
- `ServiceProviderName`: `str`


## DvbSubDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DvbSubDestinationSettingsTypeDef
```




Optional fields:
- `Alignment`: `DvbSubtitleAlignment`
- `BackgroundColor`: `DvbSubtitleBackgroundColor`
- `BackgroundOpacity`: `int`
- `FontColor`: `DvbSubtitleFontColor`
- `FontOpacity`: `int`
- `FontResolution`: `int`
- `FontScript`: `FontScript`
- `FontSize`: `int`
- `OutlineColor`: `DvbSubtitleOutlineColor`
- `OutlineSize`: `int`
- `ShadowColor`: `DvbSubtitleShadowColor`
- `ShadowOpacity`: `int`
- `ShadowXOffset`: `int`
- `ShadowYOffset`: `int`
- `SubtitlingType`: `DvbSubtitlingType`
- `TeletextSpacing`: `DvbSubtitleTeletextSpacing`
- `XPosition`: `int`
- `YPosition`: `int`


## DvbSubSourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DvbSubSourceSettingsTypeDef
```




Optional fields:
- `Pid`: `int`


## DvbTdtSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DvbTdtSettingsTypeDef
```




Optional fields:
- `TdtInterval`: `int`


## Eac3AtmosSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Eac3AtmosSettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `BitstreamMode`: `Eac3AtmosBitstreamMode`
- `CodingMode`: `Eac3AtmosCodingMode`
- `DialogueIntelligence`: `Eac3AtmosDialogueIntelligence`
- `DynamicRangeCompressionLine`: `Eac3AtmosDynamicRangeCompressionLine`
- `DynamicRangeCompressionRf`: `Eac3AtmosDynamicRangeCompressionRf`
- `LoRoCenterMixLevel`: `float`
- `LoRoSurroundMixLevel`: `float`
- `LtRtCenterMixLevel`: `float`
- `LtRtSurroundMixLevel`: `float`
- `MeteringMode`: `Eac3AtmosMeteringMode`
- `SampleRate`: `int`
- `SpeechThreshold`: `int`
- `StereoDownmix`: `Eac3AtmosStereoDownmix`
- `SurroundExMode`: `Eac3AtmosSurroundExMode`


## Eac3SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Eac3SettingsTypeDef
```




Optional fields:
- `AttenuationControl`: `Eac3AttenuationControl`
- `Bitrate`: `int`
- `BitstreamMode`: `Eac3BitstreamMode`
- `CodingMode`: `Eac3CodingMode`
- `DcFilter`: `Eac3DcFilter`
- `Dialnorm`: `int`
- `DynamicRangeCompressionLine`: `Eac3DynamicRangeCompressionLine`
- `DynamicRangeCompressionRf`: `Eac3DynamicRangeCompressionRf`
- `LfeControl`: `Eac3LfeControl`
- `LfeFilter`: `Eac3LfeFilter`
- `LoRoCenterMixLevel`: `float`
- `LoRoSurroundMixLevel`: `float`
- `LtRtCenterMixLevel`: `float`
- `LtRtSurroundMixLevel`: `float`
- `MetadataControl`: `Eac3MetadataControl`
- `PassthroughControl`: `Eac3PassthroughControl`
- `PhaseControl`: `Eac3PhaseControl`
- `SampleRate`: `int`
- `StereoDownmix`: `Eac3StereoDownmix`
- `SurroundExMode`: `Eac3SurroundExMode`
- `SurroundMode`: `Eac3SurroundMode`


## EmbeddedDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import EmbeddedDestinationSettingsTypeDef
```




Optional fields:
- `Destination608ChannelNumber`: `int`
- `Destination708ServiceNumber`: `int`


## EmbeddedSourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import EmbeddedSourceSettingsTypeDef
```




Optional fields:
- `Convert608To708`: `EmbeddedConvert608To708`
- `Source608ChannelNumber`: `int`
- `Source608TrackNumber`: `int`
- `TerminateCaptions`: `EmbeddedTerminateCaptions`


## EndpointTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import EndpointTypeDef
```




Optional fields:
- `Url`: `str`


## EsamManifestConfirmConditionNotificationTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import EsamManifestConfirmConditionNotificationTypeDef
```




Optional fields:
- `MccXml`: `str`


## EsamSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import EsamSettingsTypeDef
```




Optional fields:
- `ManifestConfirmConditionNotification`: `"EsamManifestConfirmConditionNotificationTypeDef"`
- `ResponseSignalPreroll`: `int`
- `SignalProcessingNotification`: `"EsamSignalProcessingNotificationTypeDef"`


## EsamSignalProcessingNotificationTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import EsamSignalProcessingNotificationTypeDef
```




Optional fields:
- `SccXml`: `str`


## F4vSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import F4vSettingsTypeDef
```




Optional fields:
- `MoovPlacement`: `F4vMoovPlacement`


## FileGroupSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import FileGroupSettingsTypeDef
```




Optional fields:
- `Destination`: `str`
- `DestinationSettings`: `"DestinationSettingsTypeDef"`


## FileSourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import FileSourceSettingsTypeDef
```




Optional fields:
- `Convert608To708`: `FileSourceConvert608To708`
- `Framerate`: `"CaptionSourceFramerateTypeDef"`
- `SourceFile`: `str`
- `TimeDelta`: `int`


## FrameCaptureSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import FrameCaptureSettingsTypeDef
```




Optional fields:
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `MaxCaptures`: `int`
- `Quality`: `int`


## H264QvbrSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import H264QvbrSettingsTypeDef
```




Optional fields:
- `MaxAverageBitrate`: `int`
- `QvbrQualityLevel`: `int`
- `QvbrQualityLevelFineTune`: `float`


## H264SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import H264SettingsTypeDef
```




Optional fields:
- `AdaptiveQuantization`: `H264AdaptiveQuantization`
- `Bitrate`: `int`
- `CodecLevel`: `H264CodecLevel`
- `CodecProfile`: `H264CodecProfile`
- `DynamicSubGop`: `H264DynamicSubGop`
- `EntropyEncoding`: `H264EntropyEncoding`
- `FieldEncoding`: `H264FieldEncoding`
- `FlickerAdaptiveQuantization`: `H264FlickerAdaptiveQuantization`
- `FramerateControl`: `H264FramerateControl`
- `FramerateConversionAlgorithm`: `H264FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopBReference`: `H264GopBReference`
- `GopClosedCadence`: `int`
- `GopSize`: `float`
- `GopSizeUnits`: `H264GopSizeUnits`
- `HrdBufferInitialFillPercentage`: `int`
- `HrdBufferSize`: `int`
- `InterlaceMode`: `H264InterlaceMode`
- `MaxBitrate`: `int`
- `MinIInterval`: `int`
- `NumberBFramesBetweenReferenceFrames`: `int`
- `NumberReferenceFrames`: `int`
- `ParControl`: `H264ParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `QualityTuningLevel`: `H264QualityTuningLevel`
- `QvbrSettings`: `"H264QvbrSettingsTypeDef"`
- `RateControlMode`: `H264RateControlMode`
- `RepeatPps`: `H264RepeatPps`
- `ScanTypeConversionMode`: `H264ScanTypeConversionMode`
- `SceneChangeDetect`: `H264SceneChangeDetect`
- `Slices`: `int`
- `SlowPal`: `H264SlowPal`
- `Softness`: `int`
- `SpatialAdaptiveQuantization`: `H264SpatialAdaptiveQuantization`
- `Syntax`: `H264Syntax`
- `Telecine`: `H264Telecine`
- `TemporalAdaptiveQuantization`: `H264TemporalAdaptiveQuantization`
- `UnregisteredSeiTimecode`: `H264UnregisteredSeiTimecode`


## H265QvbrSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import H265QvbrSettingsTypeDef
```




Optional fields:
- `MaxAverageBitrate`: `int`
- `QvbrQualityLevel`: `int`
- `QvbrQualityLevelFineTune`: `float`


## H265SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import H265SettingsTypeDef
```




Optional fields:
- `AdaptiveQuantization`: `H265AdaptiveQuantization`
- `AlternateTransferFunctionSei`: `H265AlternateTransferFunctionSei`
- `Bitrate`: `int`
- `CodecLevel`: `H265CodecLevel`
- `CodecProfile`: `H265CodecProfile`
- `DynamicSubGop`: `H265DynamicSubGop`
- `FlickerAdaptiveQuantization`: `H265FlickerAdaptiveQuantization`
- `FramerateControl`: `H265FramerateControl`
- `FramerateConversionAlgorithm`: `H265FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopBReference`: `H265GopBReference`
- `GopClosedCadence`: `int`
- `GopSize`: `float`
- `GopSizeUnits`: `H265GopSizeUnits`
- `HrdBufferInitialFillPercentage`: `int`
- `HrdBufferSize`: `int`
- `InterlaceMode`: `H265InterlaceMode`
- `MaxBitrate`: `int`
- `MinIInterval`: `int`
- `NumberBFramesBetweenReferenceFrames`: `int`
- `NumberReferenceFrames`: `int`
- `ParControl`: `H265ParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `QualityTuningLevel`: `H265QualityTuningLevel`
- `QvbrSettings`: `"H265QvbrSettingsTypeDef"`
- `RateControlMode`: `H265RateControlMode`
- `SampleAdaptiveOffsetFilterMode`: `H265SampleAdaptiveOffsetFilterMode`
- `ScanTypeConversionMode`: `H265ScanTypeConversionMode`
- `SceneChangeDetect`: `H265SceneChangeDetect`
- `Slices`: `int`
- `SlowPal`: `H265SlowPal`
- `SpatialAdaptiveQuantization`: `H265SpatialAdaptiveQuantization`
- `Telecine`: `H265Telecine`
- `TemporalAdaptiveQuantization`: `H265TemporalAdaptiveQuantization`
- `TemporalIds`: `H265TemporalIds`
- `Tiles`: `H265Tiles`
- `UnregisteredSeiTimecode`: `H265UnregisteredSeiTimecode`
- `WriteMp4PackagingType`: `H265WriteMp4PackagingType`


## Hdr10MetadataTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Hdr10MetadataTypeDef
```




Optional fields:
- `BluePrimaryX`: `int`
- `BluePrimaryY`: `int`
- `GreenPrimaryX`: `int`
- `GreenPrimaryY`: `int`
- `MaxContentLightLevel`: `int`
- `MaxFrameAverageLightLevel`: `int`
- `MaxLuminance`: `int`
- `MinLuminance`: `int`
- `RedPrimaryX`: `int`
- `RedPrimaryY`: `int`
- `WhitePointX`: `int`
- `WhitePointY`: `int`


## HlsAdditionalManifestTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import HlsAdditionalManifestTypeDef
```




Optional fields:
- `ManifestNameModifier`: `str`
- `SelectedOutputs`: `List[str]`


## HlsCaptionLanguageMappingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import HlsCaptionLanguageMappingTypeDef
```




Optional fields:
- `CaptionChannel`: `int`
- `CustomLanguageCode`: `str`
- `LanguageCode`: `LanguageCode`
- `LanguageDescription`: `str`


## HlsEncryptionSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import HlsEncryptionSettingsTypeDef
```




Optional fields:
- `ConstantInitializationVector`: `str`
- `EncryptionMethod`: `HlsEncryptionType`
- `InitializationVectorInManifest`: `HlsInitializationVectorInManifest`
- `OfflineEncrypted`: `HlsOfflineEncrypted`
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`
- `StaticKeyProvider`: `"StaticKeyProviderTypeDef"`
- `Type`: `HlsKeyProviderType`


## HlsGroupSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import HlsGroupSettingsTypeDef
```




Optional fields:
- `AdMarkers`: `List[HlsAdMarkers]`
- `AdditionalManifests`: `List["HlsAdditionalManifestTypeDef"]`
- `AudioOnlyHeader`: `HlsAudioOnlyHeader`
- `BaseUrl`: `str`
- `CaptionLanguageMappings`: `List["HlsCaptionLanguageMappingTypeDef"]`
- `CaptionLanguageSetting`: `HlsCaptionLanguageSetting`
- `ClientCache`: `HlsClientCache`
- `CodecSpecification`: `HlsCodecSpecification`
- `Destination`: `str`
- `DestinationSettings`: `"DestinationSettingsTypeDef"`
- `DirectoryStructure`: `HlsDirectoryStructure`
- `Encryption`: `"HlsEncryptionSettingsTypeDef"`
- `ManifestCompression`: `HlsManifestCompression`
- `ManifestDurationFormat`: `HlsManifestDurationFormat`
- `MinFinalSegmentLength`: `float`
- `MinSegmentLength`: `int`
- `OutputSelection`: `HlsOutputSelection`
- `ProgramDateTime`: `HlsProgramDateTime`
- `ProgramDateTimePeriod`: `int`
- `SegmentControl`: `HlsSegmentControl`
- `SegmentLength`: `int`
- `SegmentsPerSubdirectory`: `int`
- `StreamInfResolution`: `HlsStreamInfResolution`
- `TimedMetadataId3Frame`: `HlsTimedMetadataId3Frame`
- `TimedMetadataId3Period`: `int`
- `TimestampDeltaMilliseconds`: `int`


## HlsSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import HlsSettingsTypeDef
```




Optional fields:
- `AudioGroupId`: `str`
- `AudioOnlyContainer`: `HlsAudioOnlyContainer`
- `AudioRenditionSets`: `str`
- `AudioTrackType`: `HlsAudioTrackType`
- `DescriptiveVideoServiceFlag`: `HlsDescriptiveVideoServiceFlag`
- `IFrameOnlyManifest`: `HlsIFrameOnlyManifest`
- `SegmentModifier`: `str`


## HopDestinationTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import HopDestinationTypeDef
```




Optional fields:
- `Priority`: `int`
- `Queue`: `str`
- `WaitMinutes`: `int`


## Id3InsertionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Id3InsertionTypeDef
```




Optional fields:
- `Id3`: `str`
- `Timecode`: `str`


## ImageInserterTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ImageInserterTypeDef
```




Optional fields:
- `InsertableImages`: `List["InsertableImageTypeDef"]`


## ImscDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ImscDestinationSettingsTypeDef
```




Optional fields:
- `StylePassthrough`: `ImscStylePassthrough`


## InputClippingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import InputClippingTypeDef
```




Optional fields:
- `EndTimecode`: `str`
- `StartTimecode`: `str`


## InputDecryptionSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import InputDecryptionSettingsTypeDef
```




Optional fields:
- `DecryptionMode`: `DecryptionMode`
- `EncryptedDecryptionKey`: `str`
- `InitializationVector`: `str`
- `KmsKeyRegion`: `str`


## InputTemplateTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import InputTemplateTypeDef
```




Optional fields:
- `AudioSelectorGroups`: `Dict[str, "AudioSelectorGroupTypeDef"]`
- `AudioSelectors`: `Dict[str, "AudioSelectorTypeDef"]`
- `CaptionSelectors`: `Dict[str, "CaptionSelectorTypeDef"]`
- `Crop`: `"RectangleTypeDef"`
- `DeblockFilter`: `InputDeblockFilter`
- `DenoiseFilter`: `InputDenoiseFilter`
- `FilterEnable`: `InputFilterEnable`
- `FilterStrength`: `int`
- `ImageInserter`: `"ImageInserterTypeDef"`
- `InputClippings`: `List["InputClippingTypeDef"]`
- `InputScanType`: `InputScanType`
- `Position`: `"RectangleTypeDef"`
- `ProgramNumber`: `int`
- `PsiControl`: `InputPsiControl`
- `TimecodeSource`: `InputTimecodeSource`
- `TimecodeStart`: `str`
- `VideoSelector`: `"VideoSelectorTypeDef"`


## InputTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import InputTypeDef
```




Optional fields:
- `AudioSelectorGroups`: `Dict[str, "AudioSelectorGroupTypeDef"]`
- `AudioSelectors`: `Dict[str, "AudioSelectorTypeDef"]`
- `CaptionSelectors`: `Dict[str, "CaptionSelectorTypeDef"]`
- `Crop`: `"RectangleTypeDef"`
- `DeblockFilter`: `InputDeblockFilter`
- `DecryptionSettings`: `"InputDecryptionSettingsTypeDef"`
- `DenoiseFilter`: `InputDenoiseFilter`
- `FileInput`: `str`
- `FilterEnable`: `InputFilterEnable`
- `FilterStrength`: `int`
- `ImageInserter`: `"ImageInserterTypeDef"`
- `InputClippings`: `List["InputClippingTypeDef"]`
- `InputScanType`: `InputScanType`
- `Position`: `"RectangleTypeDef"`
- `ProgramNumber`: `int`
- `PsiControl`: `InputPsiControl`
- `SupplementalImps`: `List[str]`
- `TimecodeSource`: `InputTimecodeSource`
- `TimecodeStart`: `str`
- `VideoSelector`: `"VideoSelectorTypeDef"`


## InsertableImageTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import InsertableImageTypeDef
```




Optional fields:
- `Duration`: `int`
- `FadeIn`: `int`
- `FadeOut`: `int`
- `Height`: `int`
- `ImageInserterInput`: `str`
- `ImageX`: `int`
- `ImageY`: `int`
- `Layer`: `int`
- `Opacity`: `int`
- `StartTime`: `str`
- `Width`: `int`


## JobMessagesTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import JobMessagesTypeDef
```




Optional fields:
- `Info`: `List[str]`
- `Warning`: `List[str]`


## JobSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import JobSettingsTypeDef
```




Optional fields:
- `AdAvailOffset`: `int`
- `AvailBlanking`: `"AvailBlankingTypeDef"`
- `Esam`: `"EsamSettingsTypeDef"`
- `Inputs`: `List["InputTypeDef"]`
- `MotionImageInserter`: `"MotionImageInserterTypeDef"`
- `NielsenConfiguration`: `"NielsenConfigurationTypeDef"`
- `NielsenNonLinearWatermark`: `"NielsenNonLinearWatermarkSettingsTypeDef"`
- `OutputGroups`: `List["OutputGroupTypeDef"]`
- `TimecodeConfig`: `"TimecodeConfigTypeDef"`
- `TimedMetadataInsertion`: `"TimedMetadataInsertionTypeDef"`


## JobTemplateSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import JobTemplateSettingsTypeDef
```




Optional fields:
- `AdAvailOffset`: `int`
- `AvailBlanking`: `"AvailBlankingTypeDef"`
- `Esam`: `"EsamSettingsTypeDef"`
- `Inputs`: `List["InputTemplateTypeDef"]`
- `MotionImageInserter`: `"MotionImageInserterTypeDef"`
- `NielsenConfiguration`: `"NielsenConfigurationTypeDef"`
- `NielsenNonLinearWatermark`: `"NielsenNonLinearWatermarkSettingsTypeDef"`
- `OutputGroups`: `List["OutputGroupTypeDef"]`
- `TimecodeConfig`: `"TimecodeConfigTypeDef"`
- `TimedMetadataInsertion`: `"TimedMetadataInsertionTypeDef"`


## JobTemplateTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import JobTemplateTypeDef
```


Required fields:
- `Name`: `str`
- `Settings`: `"JobTemplateSettingsTypeDef"`



Optional fields:
- `AccelerationSettings`: `"AccelerationSettingsTypeDef"`
- `Arn`: `str`
- `Category`: `str`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `HopDestinations`: `List["HopDestinationTypeDef"]`
- `LastUpdated`: `datetime`
- `Priority`: `int`
- `Queue`: `str`
- `StatusUpdateInterval`: `StatusUpdateInterval`
- `Type`: `TypeType`


## JobTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import JobTypeDef
```


Required fields:
- `Role`: `str`
- `Settings`: `"JobSettingsTypeDef"`



Optional fields:
- `AccelerationSettings`: `"AccelerationSettingsTypeDef"`
- `AccelerationStatus`: `AccelerationStatus`
- `Arn`: `str`
- `BillingTagsSource`: `BillingTagsSource`
- `CreatedAt`: `datetime`
- `CurrentPhase`: `JobPhase`
- `ErrorCode`: `int`
- `ErrorMessage`: `str`
- `HopDestinations`: `List["HopDestinationTypeDef"]`
- `Id`: `str`
- `JobPercentComplete`: `int`
- `JobTemplate`: `str`
- `Messages`: `"JobMessagesTypeDef"`
- `OutputGroupDetails`: `List["OutputGroupDetailTypeDef"]`
- `Priority`: `int`
- `Queue`: `str`
- `QueueTransitions`: `List["QueueTransitionTypeDef"]`
- `RetryCount`: `int`
- `SimulateReservedQueue`: `SimulateReservedQueue`
- `Status`: `JobStatus`
- `StatusUpdateInterval`: `StatusUpdateInterval`
- `Timing`: `"TimingTypeDef"`
- `UserMetadata`: `Dict[str, str]`


## M2tsScte35EsamTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import M2tsScte35EsamTypeDef
```




Optional fields:
- `Scte35EsamPid`: `int`


## M2tsSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import M2tsSettingsTypeDef
```




Optional fields:
- `AudioBufferModel`: `M2tsAudioBufferModel`
- `AudioDuration`: `M2tsAudioDuration`
- `AudioFramesPerPes`: `int`
- `AudioPids`: `List[int]`
- `Bitrate`: `int`
- `BufferModel`: `M2tsBufferModel`
- `DvbNitSettings`: `"DvbNitSettingsTypeDef"`
- `DvbSdtSettings`: `"DvbSdtSettingsTypeDef"`
- `DvbSubPids`: `List[int]`
- `DvbTdtSettings`: `"DvbTdtSettingsTypeDef"`
- `DvbTeletextPid`: `int`
- `EbpAudioInterval`: `M2tsEbpAudioInterval`
- `EbpPlacement`: `M2tsEbpPlacement`
- `EsRateInPes`: `M2tsEsRateInPes`
- `ForceTsVideoEbpOrder`: `M2tsForceTsVideoEbpOrder`
- `FragmentTime`: `float`
- `MaxPcrInterval`: `int`
- `MinEbpInterval`: `int`
- `NielsenId3`: `M2tsNielsenId3`
- `NullPacketBitrate`: `float`
- `PatInterval`: `int`
- `PcrControl`: `M2tsPcrControl`
- `PcrPid`: `int`
- `PmtInterval`: `int`
- `PmtPid`: `int`
- `PrivateMetadataPid`: `int`
- `ProgramNumber`: `int`
- `RateMode`: `M2tsRateMode`
- `Scte35Esam`: `"M2tsScte35EsamTypeDef"`
- `Scte35Pid`: `int`
- `Scte35Source`: `M2tsScte35Source`
- `SegmentationMarkers`: `M2tsSegmentationMarkers`
- `SegmentationStyle`: `M2tsSegmentationStyle`
- `SegmentationTime`: `float`
- `TimedMetadataPid`: `int`
- `TransportStreamId`: `int`
- `VideoPid`: `int`


## M3u8SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import M3u8SettingsTypeDef
```




Optional fields:
- `AudioDuration`: `M3u8AudioDuration`
- `AudioFramesPerPes`: `int`
- `AudioPids`: `List[int]`
- `NielsenId3`: `M3u8NielsenId3`
- `PatInterval`: `int`
- `PcrControl`: `M3u8PcrControl`
- `PcrPid`: `int`
- `PmtInterval`: `int`
- `PmtPid`: `int`
- `PrivateMetadataPid`: `int`
- `ProgramNumber`: `int`
- `Scte35Pid`: `int`
- `Scte35Source`: `M3u8Scte35Source`
- `TimedMetadata`: `TimedMetadata`
- `TimedMetadataPid`: `int`
- `TransportStreamId`: `int`
- `VideoPid`: `int`


## MotionImageInserterTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MotionImageInserterTypeDef
```




Optional fields:
- `Framerate`: `"MotionImageInsertionFramerateTypeDef"`
- `Input`: `str`
- `InsertionMode`: `MotionImageInsertionMode`
- `Offset`: `"MotionImageInsertionOffsetTypeDef"`
- `Playback`: `MotionImagePlayback`
- `StartTime`: `str`


## MotionImageInsertionFramerateTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MotionImageInsertionFramerateTypeDef
```




Optional fields:
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`


## MotionImageInsertionOffsetTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MotionImageInsertionOffsetTypeDef
```




Optional fields:
- `ImageX`: `int`
- `ImageY`: `int`


## MovSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MovSettingsTypeDef
```




Optional fields:
- `ClapAtom`: `MovClapAtom`
- `CslgAtom`: `MovCslgAtom`
- `Mpeg2FourCCControl`: `MovMpeg2FourCCControl`
- `PaddingControl`: `MovPaddingControl`
- `Reference`: `MovReference`


## Mp2SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Mp2SettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `Channels`: `int`
- `SampleRate`: `int`


## Mp3SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Mp3SettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `Channels`: `int`
- `RateControlMode`: `Mp3RateControlMode`
- `SampleRate`: `int`
- `VbrQuality`: `int`


## Mp4SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Mp4SettingsTypeDef
```




Optional fields:
- `AudioDuration`: `CmfcAudioDuration`
- `CslgAtom`: `Mp4CslgAtom`
- `CttsVersion`: `int`
- `FreeSpaceBox`: `Mp4FreeSpaceBox`
- `MoovPlacement`: `Mp4MoovPlacement`
- `Mp4MajorBrand`: `str`


## MpdSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MpdSettingsTypeDef
```




Optional fields:
- `AccessibilityCaptionHints`: `MpdAccessibilityCaptionHints`
- `AudioDuration`: `MpdAudioDuration`
- `CaptionContainerType`: `MpdCaptionContainerType`
- `Scte35Esam`: `MpdScte35Esam`
- `Scte35Source`: `MpdScte35Source`


## Mpeg2SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Mpeg2SettingsTypeDef
```




Optional fields:
- `AdaptiveQuantization`: `Mpeg2AdaptiveQuantization`
- `Bitrate`: `int`
- `CodecLevel`: `Mpeg2CodecLevel`
- `CodecProfile`: `Mpeg2CodecProfile`
- `DynamicSubGop`: `Mpeg2DynamicSubGop`
- `FramerateControl`: `Mpeg2FramerateControl`
- `FramerateConversionAlgorithm`: `Mpeg2FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopClosedCadence`: `int`
- `GopSize`: `float`
- `GopSizeUnits`: `Mpeg2GopSizeUnits`
- `HrdBufferInitialFillPercentage`: `int`
- `HrdBufferSize`: `int`
- `InterlaceMode`: `Mpeg2InterlaceMode`
- `IntraDcPrecision`: `Mpeg2IntraDcPrecision`
- `MaxBitrate`: `int`
- `MinIInterval`: `int`
- `NumberBFramesBetweenReferenceFrames`: `int`
- `ParControl`: `Mpeg2ParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `QualityTuningLevel`: `Mpeg2QualityTuningLevel`
- `RateControlMode`: `Mpeg2RateControlMode`
- `ScanTypeConversionMode`: `Mpeg2ScanTypeConversionMode`
- `SceneChangeDetect`: `Mpeg2SceneChangeDetect`
- `SlowPal`: `Mpeg2SlowPal`
- `Softness`: `int`
- `SpatialAdaptiveQuantization`: `Mpeg2SpatialAdaptiveQuantization`
- `Syntax`: `Mpeg2Syntax`
- `Telecine`: `Mpeg2Telecine`
- `TemporalAdaptiveQuantization`: `Mpeg2TemporalAdaptiveQuantization`


## MsSmoothAdditionalManifestTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MsSmoothAdditionalManifestTypeDef
```




Optional fields:
- `ManifestNameModifier`: `str`
- `SelectedOutputs`: `List[str]`


## MsSmoothEncryptionSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MsSmoothEncryptionSettingsTypeDef
```




Optional fields:
- `SpekeKeyProvider`: `"SpekeKeyProviderTypeDef"`


## MsSmoothGroupSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MsSmoothGroupSettingsTypeDef
```




Optional fields:
- `AdditionalManifests`: `List["MsSmoothAdditionalManifestTypeDef"]`
- `AudioDeduplication`: `MsSmoothAudioDeduplication`
- `Destination`: `str`
- `DestinationSettings`: `"DestinationSettingsTypeDef"`
- `Encryption`: `"MsSmoothEncryptionSettingsTypeDef"`
- `FragmentLength`: `int`
- `ManifestEncoding`: `MsSmoothManifestEncoding`


## MxfSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import MxfSettingsTypeDef
```




Optional fields:
- `AfdSignaling`: `MxfAfdSignaling`
- `Profile`: `MxfProfile`


## NexGuardFileMarkerSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NexGuardFileMarkerSettingsTypeDef
```




Optional fields:
- `License`: `str`
- `Payload`: `int`
- `Preset`: `str`
- `Strength`: `WatermarkingStrength`


## NielsenConfigurationTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NielsenConfigurationTypeDef
```




Optional fields:
- `BreakoutCode`: `int`
- `DistributorId`: `str`


## NielsenNonLinearWatermarkSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NielsenNonLinearWatermarkSettingsTypeDef
```




Optional fields:
- `ActiveWatermarkProcess`: `NielsenActiveWatermarkProcessType`
- `AdiFilename`: `str`
- `AssetId`: `str`
- `AssetName`: `str`
- `CbetSourceId`: `str`
- `EpisodeId`: `str`
- `MetadataDestination`: `str`
- `SourceId`: `int`
- `SourceWatermarkStatus`: `NielsenSourceWatermarkStatusType`
- `TicServerUrl`: `str`
- `UniqueTicPerAudioTrack`: `NielsenUniqueTicPerAudioTrackType`


## NoiseReducerFilterSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NoiseReducerFilterSettingsTypeDef
```




Optional fields:
- `Strength`: `int`


## NoiseReducerSpatialFilterSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NoiseReducerSpatialFilterSettingsTypeDef
```




Optional fields:
- `PostFilterSharpenStrength`: `int`
- `Speed`: `int`
- `Strength`: `int`


## NoiseReducerTemporalFilterSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NoiseReducerTemporalFilterSettingsTypeDef
```




Optional fields:
- `AggressiveMode`: `int`
- `PostTemporalSharpening`: `NoiseFilterPostTemporalSharpening`
- `Speed`: `int`
- `Strength`: `int`


## NoiseReducerTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import NoiseReducerTypeDef
```




Optional fields:
- `Filter`: `NoiseReducerFilter`
- `FilterSettings`: `"NoiseReducerFilterSettingsTypeDef"`
- `SpatialFilterSettings`: `"NoiseReducerSpatialFilterSettingsTypeDef"`
- `TemporalFilterSettings`: `"NoiseReducerTemporalFilterSettingsTypeDef"`


## OpusSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OpusSettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `Channels`: `int`
- `SampleRate`: `int`


## OutputChannelMappingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputChannelMappingTypeDef
```




Optional fields:
- `InputChannels`: `List[int]`
- `InputChannelsFineTune`: `List[float]`


## OutputDetailTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputDetailTypeDef
```




Optional fields:
- `DurationInMs`: `int`
- `VideoDetails`: `"VideoDetailTypeDef"`


## OutputGroupDetailTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputGroupDetailTypeDef
```




Optional fields:
- `OutputDetails`: `List["OutputDetailTypeDef"]`


## OutputGroupSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputGroupSettingsTypeDef
```




Optional fields:
- `CmafGroupSettings`: `"CmafGroupSettingsTypeDef"`
- `DashIsoGroupSettings`: `"DashIsoGroupSettingsTypeDef"`
- `FileGroupSettings`: `"FileGroupSettingsTypeDef"`
- `HlsGroupSettings`: `"HlsGroupSettingsTypeDef"`
- `MsSmoothGroupSettings`: `"MsSmoothGroupSettingsTypeDef"`
- `Type`: `OutputGroupType`


## OutputGroupTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputGroupTypeDef
```




Optional fields:
- `AutomatedEncodingSettings`: `"AutomatedEncodingSettingsTypeDef"`
- `CustomName`: `str`
- `Name`: `str`
- `OutputGroupSettings`: `"OutputGroupSettingsTypeDef"`
- `Outputs`: `List["OutputTypeDef"]`


## OutputSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputSettingsTypeDef
```




Optional fields:
- `HlsSettings`: `"HlsSettingsTypeDef"`


## OutputTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import OutputTypeDef
```




Optional fields:
- `AudioDescriptions`: `List["AudioDescriptionTypeDef"]`
- `CaptionDescriptions`: `List["CaptionDescriptionTypeDef"]`
- `ContainerSettings`: `"ContainerSettingsTypeDef"`
- `Extension`: `str`
- `NameModifier`: `str`
- `OutputSettings`: `"OutputSettingsTypeDef"`
- `Preset`: `str`
- `VideoDescription`: `"VideoDescriptionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PartnerWatermarkingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import PartnerWatermarkingTypeDef
```




Optional fields:
- `NexguardFileMarkerSettings`: `"NexGuardFileMarkerSettingsTypeDef"`


## PresetSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import PresetSettingsTypeDef
```




Optional fields:
- `AudioDescriptions`: `List["AudioDescriptionTypeDef"]`
- `CaptionDescriptions`: `List["CaptionDescriptionPresetTypeDef"]`
- `ContainerSettings`: `"ContainerSettingsTypeDef"`
- `VideoDescription`: `"VideoDescriptionTypeDef"`


## PresetTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import PresetTypeDef
```


Required fields:
- `Name`: `str`
- `Settings`: `"PresetSettingsTypeDef"`



Optional fields:
- `Arn`: `str`
- `Category`: `str`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `LastUpdated`: `datetime`
- `Type`: `TypeType`


## ProresSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ProresSettingsTypeDef
```




Optional fields:
- `CodecProfile`: `ProresCodecProfile`
- `FramerateControl`: `ProresFramerateControl`
- `FramerateConversionAlgorithm`: `ProresFramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `InterlaceMode`: `ProresInterlaceMode`
- `ParControl`: `ProresParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `ScanTypeConversionMode`: `ProresScanTypeConversionMode`
- `SlowPal`: `ProresSlowPal`
- `Telecine`: `ProresTelecine`


## QueueTransitionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import QueueTransitionTypeDef
```




Optional fields:
- `DestinationQueue`: `str`
- `SourceQueue`: `str`
- `Timestamp`: `datetime`


## QueueTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import QueueTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Arn`: `str`
- `CreatedAt`: `datetime`
- `Description`: `str`
- `LastUpdated`: `datetime`
- `PricingPlan`: `PricingPlan`
- `ProgressingJobsCount`: `int`
- `ReservationPlan`: `"ReservationPlanTypeDef"`
- `Status`: `QueueStatus`
- `SubmittedJobsCount`: `int`
- `Type`: `TypeType`


## RectangleTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import RectangleTypeDef
```




Optional fields:
- `Height`: `int`
- `Width`: `int`
- `X`: `int`
- `Y`: `int`


## RemixSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import RemixSettingsTypeDef
```




Optional fields:
- `ChannelMapping`: `"ChannelMappingTypeDef"`
- `ChannelsIn`: `int`
- `ChannelsOut`: `int`


## ReservationPlanTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ReservationPlanTypeDef
```




Optional fields:
- `Commitment`: `Commitment`
- `ExpiresAt`: `datetime`
- `PurchasedAt`: `datetime`
- `RenewalType`: `RenewalType`
- `ReservedSlots`: `int`
- `Status`: `ReservationPlanStatus`


## ResourceTagsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ResourceTagsTypeDef
```




Optional fields:
- `Arn`: `str`
- `Tags`: `Dict[str, str]`


## ResponseMetadata

```python
from mypy_boto3_mediaconvert.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3DestinationAccessControlTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import S3DestinationAccessControlTypeDef
```




Optional fields:
- `CannedAcl`: `S3ObjectCannedAcl`


## S3DestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import S3DestinationSettingsTypeDef
```




Optional fields:
- `AccessControl`: `"S3DestinationAccessControlTypeDef"`
- `Encryption`: `"S3EncryptionSettingsTypeDef"`


## S3EncryptionSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import S3EncryptionSettingsTypeDef
```




Optional fields:
- `EncryptionType`: `S3ServerSideEncryptionType`
- `KmsKeyArn`: `str`


## SccDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import SccDestinationSettingsTypeDef
```




Optional fields:
- `Framerate`: `SccDestinationFramerate`


## SpekeKeyProviderCmafTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import SpekeKeyProviderCmafTypeDef
```




Optional fields:
- `CertificateArn`: `str`
- `DashSignaledSystemIds`: `List[str]`
- `HlsSignaledSystemIds`: `List[str]`
- `ResourceId`: `str`
- `Url`: `str`


## SpekeKeyProviderTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import SpekeKeyProviderTypeDef
```




Optional fields:
- `CertificateArn`: `str`
- `ResourceId`: `str`
- `SystemIds`: `List[str]`
- `Url`: `str`


## StaticKeyProviderTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import StaticKeyProviderTypeDef
```




Optional fields:
- `KeyFormat`: `str`
- `KeyFormatVersions`: `str`
- `StaticKeyValue`: `str`
- `Url`: `str`


## TeletextDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TeletextDestinationSettingsTypeDef
```




Optional fields:
- `PageNumber`: `str`
- `PageTypes`: `List[TeletextPageType]`


## TeletextSourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TeletextSourceSettingsTypeDef
```




Optional fields:
- `PageNumber`: `str`


## TimecodeBurninTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TimecodeBurninTypeDef
```




Optional fields:
- `FontSize`: `int`
- `Position`: `TimecodeBurninPosition`
- `Prefix`: `str`


## TimecodeConfigTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TimecodeConfigTypeDef
```




Optional fields:
- `Anchor`: `str`
- `Source`: `TimecodeSource`
- `Start`: `str`
- `TimestampOffset`: `str`


## TimedMetadataInsertionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TimedMetadataInsertionTypeDef
```




Optional fields:
- `Id3Insertions`: `List["Id3InsertionTypeDef"]`


## TimingTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TimingTypeDef
```




Optional fields:
- `FinishTime`: `datetime`
- `StartTime`: `datetime`
- `SubmitTime`: `datetime`


## TrackSourceSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TrackSourceSettingsTypeDef
```




Optional fields:
- `TrackNumber`: `int`


## TtmlDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import TtmlDestinationSettingsTypeDef
```




Optional fields:
- `StylePassthrough`: `TtmlStylePassthrough`


## Vc3SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Vc3SettingsTypeDef
```




Optional fields:
- `FramerateControl`: `Vc3FramerateControl`
- `FramerateConversionAlgorithm`: `Vc3FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `InterlaceMode`: `Vc3InterlaceMode`
- `ScanTypeConversionMode`: `Vc3ScanTypeConversionMode`
- `SlowPal`: `Vc3SlowPal`
- `Telecine`: `Vc3Telecine`
- `Vc3Class`: `Vc3Class`


## VideoCodecSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import VideoCodecSettingsTypeDef
```




Optional fields:
- `Av1Settings`: `"Av1SettingsTypeDef"`
- `AvcIntraSettings`: `"AvcIntraSettingsTypeDef"`
- `Codec`: `VideoCodec`
- `FrameCaptureSettings`: `"FrameCaptureSettingsTypeDef"`
- `H264Settings`: `"H264SettingsTypeDef"`
- `H265Settings`: `"H265SettingsTypeDef"`
- `Mpeg2Settings`: `"Mpeg2SettingsTypeDef"`
- `ProresSettings`: `"ProresSettingsTypeDef"`
- `Vc3Settings`: `"Vc3SettingsTypeDef"`
- `Vp8Settings`: `"Vp8SettingsTypeDef"`
- `Vp9Settings`: `"Vp9SettingsTypeDef"`


## VideoDescriptionTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import VideoDescriptionTypeDef
```




Optional fields:
- `AfdSignaling`: `AfdSignaling`
- `AntiAlias`: `AntiAlias`
- `CodecSettings`: `"VideoCodecSettingsTypeDef"`
- `ColorMetadata`: `ColorMetadata`
- `Crop`: `"RectangleTypeDef"`
- `DropFrameTimecode`: `DropFrameTimecode`
- `FixedAfd`: `int`
- `Height`: `int`
- `Position`: `"RectangleTypeDef"`
- `RespondToAfd`: `RespondToAfd`
- `ScalingBehavior`: `ScalingBehavior`
- `Sharpness`: `int`
- `TimecodeInsertion`: `VideoTimecodeInsertion`
- `VideoPreprocessors`: `"VideoPreprocessorTypeDef"`
- `Width`: `int`


## VideoDetailTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import VideoDetailTypeDef
```




Optional fields:
- `HeightInPx`: `int`
- `WidthInPx`: `int`


## VideoPreprocessorTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import VideoPreprocessorTypeDef
```




Optional fields:
- `ColorCorrector`: `"ColorCorrectorTypeDef"`
- `Deinterlacer`: `"DeinterlacerTypeDef"`
- `DolbyVision`: `"DolbyVisionTypeDef"`
- `ImageInserter`: `"ImageInserterTypeDef"`
- `NoiseReducer`: `"NoiseReducerTypeDef"`
- `PartnerWatermarking`: `"PartnerWatermarkingTypeDef"`
- `TimecodeBurnin`: `"TimecodeBurninTypeDef"`


## VideoSelectorTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import VideoSelectorTypeDef
```




Optional fields:
- `AlphaBehavior`: `AlphaBehavior`
- `ColorSpace`: `ColorSpace`
- `ColorSpaceUsage`: `ColorSpaceUsage`
- `Hdr10Metadata`: `"Hdr10MetadataTypeDef"`
- `Pid`: `int`
- `ProgramNumber`: `int`
- `Rotate`: `InputRotate`


## VorbisSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import VorbisSettingsTypeDef
```




Optional fields:
- `Channels`: `int`
- `SampleRate`: `int`
- `VbrQuality`: `int`


## Vp8SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Vp8SettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `FramerateControl`: `Vp8FramerateControl`
- `FramerateConversionAlgorithm`: `Vp8FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopSize`: `float`
- `HrdBufferSize`: `int`
- `MaxBitrate`: `int`
- `ParControl`: `Vp8ParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `QualityTuningLevel`: `Vp8QualityTuningLevel`
- `RateControlMode`: `Vp8RateControlMode`


## Vp9SettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import Vp9SettingsTypeDef
```




Optional fields:
- `Bitrate`: `int`
- `FramerateControl`: `Vp9FramerateControl`
- `FramerateConversionAlgorithm`: `Vp9FramerateConversionAlgorithm`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopSize`: `float`
- `HrdBufferSize`: `int`
- `MaxBitrate`: `int`
- `ParControl`: `Vp9ParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `QualityTuningLevel`: `Vp9QualityTuningLevel`
- `RateControlMode`: `Vp9RateControlMode`


## WavSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import WavSettingsTypeDef
```




Optional fields:
- `BitDepth`: `int`
- `Channels`: `int`
- `Format`: `WavFormat`
- `SampleRate`: `int`


## WebvttDestinationSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import WebvttDestinationSettingsTypeDef
```




Optional fields:
- `StylePassthrough`: `WebvttStylePassthrough`


## CreateJobResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CreateJobResponseTypeDef
```




Optional fields:
- `Job`: `"JobTypeDef"`


## CreateJobTemplateResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CreateJobTemplateResponseTypeDef
```




Optional fields:
- `JobTemplate`: `"JobTemplateTypeDef"`


## CreatePresetResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CreatePresetResponseTypeDef
```




Optional fields:
- `Preset`: `"PresetTypeDef"`


## CreateQueueResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import CreateQueueResponseTypeDef
```




Optional fields:
- `Queue`: `"QueueTypeDef"`


## DescribeEndpointsResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import DescribeEndpointsResponseTypeDef
```




Optional fields:
- `Endpoints`: `List["EndpointTypeDef"]`
- `NextToken`: `str`


## GetJobResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import GetJobResponseTypeDef
```




Optional fields:
- `Job`: `"JobTypeDef"`


## GetJobTemplateResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import GetJobTemplateResponseTypeDef
```




Optional fields:
- `JobTemplate`: `"JobTemplateTypeDef"`


## GetPresetResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import GetPresetResponseTypeDef
```




Optional fields:
- `Preset`: `"PresetTypeDef"`


## GetQueueResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import GetQueueResponseTypeDef
```




Optional fields:
- `Queue`: `"QueueTypeDef"`


## ListJobTemplatesResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ListJobTemplatesResponseTypeDef
```




Optional fields:
- `JobTemplates`: `List["JobTemplateTypeDef"]`
- `NextToken`: `str`


## ListJobsResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ListJobsResponseTypeDef
```




Optional fields:
- `Jobs`: `List["JobTypeDef"]`
- `NextToken`: `str`


## ListPresetsResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ListPresetsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Presets`: `List["PresetTypeDef"]`


## ListQueuesResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ListQueuesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Queues`: `List["QueueTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `ResourceTags`: `"ResourceTagsTypeDef"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ReservationPlanSettingsTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import ReservationPlanSettingsTypeDef
```


Required fields:
- `Commitment`: `Commitment`
- `RenewalType`: `RenewalType`
- `ReservedSlots`: `int`




## UpdateJobTemplateResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import UpdateJobTemplateResponseTypeDef
```




Optional fields:
- `JobTemplate`: `"JobTemplateTypeDef"`


## UpdatePresetResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import UpdatePresetResponseTypeDef
```




Optional fields:
- `Preset`: `"PresetTypeDef"`


## UpdateQueueResponseTypeDef

```python
from mypy_boto3_mediaconvert.type_defs import UpdateQueueResponseTypeDef
```




Optional fields:
- `Queue`: `"QueueTypeDef"`

