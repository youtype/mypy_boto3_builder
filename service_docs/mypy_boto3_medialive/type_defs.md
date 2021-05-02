# Structures for boto3 MediaLive module

> [Index](../index.md) > [MediaLive](./index.md) > Structures

Auto-generated documentation for [MediaLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive)
type annotations stubs module [mypy_boto3_medialive](https://pypi.org/project/mypy-boto3-medialive/).

- [Structures for boto3 MediaLive module](#structures-for-boto3-medialive-module)
  - [AacSettingsTypeDef](#aacsettingstypedef)
  - [Ac3SettingsTypeDef](#ac3settingstypedef)
  - [AncillarySourceSettingsTypeDef](#ancillarysourcesettingstypedef)
  - [ArchiveCdnSettingsTypeDef](#archivecdnsettingstypedef)
  - [ArchiveContainerSettingsTypeDef](#archivecontainersettingstypedef)
  - [ArchiveGroupSettingsTypeDef](#archivegroupsettingstypedef)
  - [ArchiveOutputSettingsTypeDef](#archiveoutputsettingstypedef)
  - [ArchiveS3SettingsTypeDef](#archives3settingstypedef)
  - [AudioChannelMappingTypeDef](#audiochannelmappingtypedef)
  - [AudioCodecSettingsTypeDef](#audiocodecsettingstypedef)
  - [AudioDescriptionTypeDef](#audiodescriptiontypedef)
  - [AudioLanguageSelectionTypeDef](#audiolanguageselectiontypedef)
  - [AudioNormalizationSettingsTypeDef](#audionormalizationsettingstypedef)
  - [AudioOnlyHlsSettingsTypeDef](#audioonlyhlssettingstypedef)
  - [AudioPidSelectionTypeDef](#audiopidselectiontypedef)
  - [AudioSelectorSettingsTypeDef](#audioselectorsettingstypedef)
  - [AudioSelectorTypeDef](#audioselectortypedef)
  - [AudioSilenceFailoverSettingsTypeDef](#audiosilencefailoversettingstypedef)
  - [AudioTrackSelectionTypeDef](#audiotrackselectiontypedef)
  - [AudioTrackTypeDef](#audiotracktypedef)
  - [AutomaticInputFailoverSettingsTypeDef](#automaticinputfailoversettingstypedef)
  - [AvailBlankingTypeDef](#availblankingtypedef)
  - [AvailConfigurationTypeDef](#availconfigurationtypedef)
  - [AvailSettingsTypeDef](#availsettingstypedef)
  - [BatchFailedResultModelTypeDef](#batchfailedresultmodeltypedef)
  - [BatchScheduleActionCreateResultTypeDef](#batchscheduleactioncreateresulttypedef)
  - [BatchScheduleActionDeleteResultTypeDef](#batchscheduleactiondeleteresulttypedef)
  - [BatchSuccessfulResultModelTypeDef](#batchsuccessfulresultmodeltypedef)
  - [BlackoutSlateTypeDef](#blackoutslatetypedef)
  - [BurnInDestinationSettingsTypeDef](#burnindestinationsettingstypedef)
  - [CaptionDescriptionTypeDef](#captiondescriptiontypedef)
  - [CaptionDestinationSettingsTypeDef](#captiondestinationsettingstypedef)
  - [CaptionLanguageMappingTypeDef](#captionlanguagemappingtypedef)
  - [CaptionRectangleTypeDef](#captionrectangletypedef)
  - [CaptionSelectorSettingsTypeDef](#captionselectorsettingstypedef)
  - [CaptionSelectorTypeDef](#captionselectortypedef)
  - [CdiInputSpecificationTypeDef](#cdiinputspecificationtypedef)
  - [ChannelEgressEndpointTypeDef](#channelegressendpointtypedef)
  - [ChannelSummaryTypeDef](#channelsummarytypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [DvbNitSettingsTypeDef](#dvbnitsettingstypedef)
  - [DvbSdtSettingsTypeDef](#dvbsdtsettingstypedef)
  - [DvbSubDestinationSettingsTypeDef](#dvbsubdestinationsettingstypedef)
  - [DvbSubSourceSettingsTypeDef](#dvbsubsourcesettingstypedef)
  - [DvbTdtSettingsTypeDef](#dvbtdtsettingstypedef)
  - [Eac3SettingsTypeDef](#eac3settingstypedef)
  - [EbuTtDDestinationSettingsTypeDef](#ebuttddestinationsettingstypedef)
  - [EmbeddedSourceSettingsTypeDef](#embeddedsourcesettingstypedef)
  - [EncoderSettingsTypeDef](#encodersettingstypedef)
  - [FailoverConditionSettingsTypeDef](#failoverconditionsettingstypedef)
  - [FailoverConditionTypeDef](#failoverconditiontypedef)
  - [FeatureActivationsTypeDef](#featureactivationstypedef)
  - [FecOutputSettingsTypeDef](#fecoutputsettingstypedef)
  - [FixedModeScheduleActionStartSettingsTypeDef](#fixedmodescheduleactionstartsettingstypedef)
  - [Fmp4HlsSettingsTypeDef](#fmp4hlssettingstypedef)
  - [FollowModeScheduleActionStartSettingsTypeDef](#followmodescheduleactionstartsettingstypedef)
  - [FrameCaptureCdnSettingsTypeDef](#framecapturecdnsettingstypedef)
  - [FrameCaptureGroupSettingsTypeDef](#framecapturegroupsettingstypedef)
  - [FrameCaptureOutputSettingsTypeDef](#framecaptureoutputsettingstypedef)
  - [FrameCaptureS3SettingsTypeDef](#framecaptures3settingstypedef)
  - [FrameCaptureSettingsTypeDef](#framecapturesettingstypedef)
  - [GlobalConfigurationTypeDef](#globalconfigurationtypedef)
  - [H264ColorSpaceSettingsTypeDef](#h264colorspacesettingstypedef)
  - [H264FilterSettingsTypeDef](#h264filtersettingstypedef)
  - [H264SettingsTypeDef](#h264settingstypedef)
  - [H265ColorSpaceSettingsTypeDef](#h265colorspacesettingstypedef)
  - [H265FilterSettingsTypeDef](#h265filtersettingstypedef)
  - [H265SettingsTypeDef](#h265settingstypedef)
  - [Hdr10SettingsTypeDef](#hdr10settingstypedef)
  - [HlsAkamaiSettingsTypeDef](#hlsakamaisettingstypedef)
  - [HlsBasicPutSettingsTypeDef](#hlsbasicputsettingstypedef)
  - [HlsCdnSettingsTypeDef](#hlscdnsettingstypedef)
  - [HlsGroupSettingsTypeDef](#hlsgroupsettingstypedef)
  - [HlsId3SegmentTaggingScheduleActionSettingsTypeDef](#hlsid3segmenttaggingscheduleactionsettingstypedef)
  - [HlsInputSettingsTypeDef](#hlsinputsettingstypedef)
  - [HlsMediaStoreSettingsTypeDef](#hlsmediastoresettingstypedef)
  - [HlsOutputSettingsTypeDef](#hlsoutputsettingstypedef)
  - [HlsS3SettingsTypeDef](#hlss3settingstypedef)
  - [HlsSettingsTypeDef](#hlssettingstypedef)
  - [HlsTimedMetadataScheduleActionSettingsTypeDef](#hlstimedmetadatascheduleactionsettingstypedef)
  - [HlsWebdavSettingsTypeDef](#hlswebdavsettingstypedef)
  - [InputAttachmentTypeDef](#inputattachmenttypedef)
  - [InputChannelLevelTypeDef](#inputchannelleveltypedef)
  - [InputClippingSettingsTypeDef](#inputclippingsettingstypedef)
  - [InputDestinationTypeDef](#inputdestinationtypedef)
  - [InputDestinationVpcTypeDef](#inputdestinationvpctypedef)
  - [InputDeviceHdSettingsTypeDef](#inputdevicehdsettingstypedef)
  - [InputDeviceNetworkSettingsTypeDef](#inputdevicenetworksettingstypedef)
  - [InputDeviceSettingsTypeDef](#inputdevicesettingstypedef)
  - [InputDeviceSummaryTypeDef](#inputdevicesummarytypedef)
  - [InputDeviceUhdSettingsTypeDef](#inputdeviceuhdsettingstypedef)
  - [InputLocationTypeDef](#inputlocationtypedef)
  - [InputLossBehaviorTypeDef](#inputlossbehaviortypedef)
  - [InputLossFailoverSettingsTypeDef](#inputlossfailoversettingstypedef)
  - [InputPrepareScheduleActionSettingsTypeDef](#inputpreparescheduleactionsettingstypedef)
  - [InputSecurityGroupTypeDef](#inputsecuritygrouptypedef)
  - [InputSettingsTypeDef](#inputsettingstypedef)
  - [InputSourceTypeDef](#inputsourcetypedef)
  - [InputSpecificationTypeDef](#inputspecificationtypedef)
  - [InputSwitchScheduleActionSettingsTypeDef](#inputswitchscheduleactionsettingstypedef)
  - [InputTypeDef](#inputtypedef)
  - [InputWhitelistRuleTypeDef](#inputwhitelistruletypedef)
  - [KeyProviderSettingsTypeDef](#keyprovidersettingstypedef)
  - [M2tsSettingsTypeDef](#m2tssettingstypedef)
  - [M3u8SettingsTypeDef](#m3u8settingstypedef)
  - [MediaConnectFlowTypeDef](#mediaconnectflowtypedef)
  - [MediaPackageGroupSettingsTypeDef](#mediapackagegroupsettingstypedef)
  - [MediaPackageOutputDestinationSettingsTypeDef](#mediapackageoutputdestinationsettingstypedef)
  - [MotionGraphicsActivateScheduleActionSettingsTypeDef](#motiongraphicsactivatescheduleactionsettingstypedef)
  - [MotionGraphicsConfigurationTypeDef](#motiongraphicsconfigurationtypedef)
  - [MotionGraphicsSettingsTypeDef](#motiongraphicssettingstypedef)
  - [Mp2SettingsTypeDef](#mp2settingstypedef)
  - [Mpeg2FilterSettingsTypeDef](#mpeg2filtersettingstypedef)
  - [Mpeg2SettingsTypeDef](#mpeg2settingstypedef)
  - [MsSmoothGroupSettingsTypeDef](#mssmoothgroupsettingstypedef)
  - [MsSmoothOutputSettingsTypeDef](#mssmoothoutputsettingstypedef)
  - [MultiplexMediaConnectOutputDestinationSettingsTypeDef](#multiplexmediaconnectoutputdestinationsettingstypedef)
  - [MultiplexOutputDestinationTypeDef](#multiplexoutputdestinationtypedef)
  - [MultiplexOutputSettingsTypeDef](#multiplexoutputsettingstypedef)
  - [MultiplexProgramChannelDestinationSettingsTypeDef](#multiplexprogramchanneldestinationsettingstypedef)
  - [MultiplexProgramPacketIdentifiersMapTypeDef](#multiplexprogrampacketidentifiersmaptypedef)
  - [MultiplexProgramPipelineDetailTypeDef](#multiplexprogrampipelinedetailtypedef)
  - [MultiplexProgramServiceDescriptorTypeDef](#multiplexprogramservicedescriptortypedef)
  - [MultiplexProgramSettingsTypeDef](#multiplexprogramsettingstypedef)
  - [MultiplexProgramSummaryTypeDef](#multiplexprogramsummarytypedef)
  - [MultiplexProgramTypeDef](#multiplexprogramtypedef)
  - [MultiplexSettingsSummaryTypeDef](#multiplexsettingssummarytypedef)
  - [MultiplexSettingsTypeDef](#multiplexsettingstypedef)
  - [MultiplexStatmuxVideoSettingsTypeDef](#multiplexstatmuxvideosettingstypedef)
  - [MultiplexSummaryTypeDef](#multiplexsummarytypedef)
  - [MultiplexTypeDef](#multiplextypedef)
  - [MultiplexVideoSettingsTypeDef](#multiplexvideosettingstypedef)
  - [NetworkInputSettingsTypeDef](#networkinputsettingstypedef)
  - [NielsenConfigurationTypeDef](#nielsenconfigurationtypedef)
  - [OfferingTypeDef](#offeringtypedef)
  - [OutputDestinationSettingsTypeDef](#outputdestinationsettingstypedef)
  - [OutputDestinationTypeDef](#outputdestinationtypedef)
  - [OutputGroupSettingsTypeDef](#outputgroupsettingstypedef)
  - [OutputGroupTypeDef](#outputgrouptypedef)
  - [OutputLocationRefTypeDef](#outputlocationreftypedef)
  - [OutputSettingsTypeDef](#outputsettingstypedef)
  - [OutputTypeDef](#outputtypedef)
  - [PauseStateScheduleActionSettingsTypeDef](#pausestatescheduleactionsettingstypedef)
  - [PipelineDetailTypeDef](#pipelinedetailtypedef)
  - [PipelinePauseStateSettingsTypeDef](#pipelinepausestatesettingstypedef)
  - [RemixSettingsTypeDef](#remixsettingstypedef)
  - [ReservationResourceSpecificationTypeDef](#reservationresourcespecificationtypedef)
  - [ReservationTypeDef](#reservationtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RtmpGroupSettingsTypeDef](#rtmpgroupsettingstypedef)
  - [RtmpOutputSettingsTypeDef](#rtmpoutputsettingstypedef)
  - [ScheduleActionSettingsTypeDef](#scheduleactionsettingstypedef)
  - [ScheduleActionStartSettingsTypeDef](#scheduleactionstartsettingstypedef)
  - [ScheduleActionTypeDef](#scheduleactiontypedef)
  - [Scte20SourceSettingsTypeDef](#scte20sourcesettingstypedef)
  - [Scte27SourceSettingsTypeDef](#scte27sourcesettingstypedef)
  - [Scte35DeliveryRestrictionsTypeDef](#scte35deliveryrestrictionstypedef)
  - [Scte35DescriptorSettingsTypeDef](#scte35descriptorsettingstypedef)
  - [Scte35DescriptorTypeDef](#scte35descriptortypedef)
  - [Scte35ReturnToNetworkScheduleActionSettingsTypeDef](#scte35returntonetworkscheduleactionsettingstypedef)
  - [Scte35SegmentationDescriptorTypeDef](#scte35segmentationdescriptortypedef)
  - [Scte35SpliceInsertScheduleActionSettingsTypeDef](#scte35spliceinsertscheduleactionsettingstypedef)
  - [Scte35SpliceInsertTypeDef](#scte35spliceinserttypedef)
  - [Scte35TimeSignalAposTypeDef](#scte35timesignalapostypedef)
  - [Scte35TimeSignalScheduleActionSettingsTypeDef](#scte35timesignalscheduleactionsettingstypedef)
  - [StandardHlsSettingsTypeDef](#standardhlssettingstypedef)
  - [StartTimecodeTypeDef](#starttimecodetypedef)
  - [StaticImageActivateScheduleActionSettingsTypeDef](#staticimageactivatescheduleactionsettingstypedef)
  - [StaticImageDeactivateScheduleActionSettingsTypeDef](#staticimagedeactivatescheduleactionsettingstypedef)
  - [StaticKeySettingsTypeDef](#statickeysettingstypedef)
  - [StopTimecodeTypeDef](#stoptimecodetypedef)
  - [TeletextSourceSettingsTypeDef](#teletextsourcesettingstypedef)
  - [TemporalFilterSettingsTypeDef](#temporalfiltersettingstypedef)
  - [TimecodeConfigTypeDef](#timecodeconfigtypedef)
  - [TransferringInputDeviceSummaryTypeDef](#transferringinputdevicesummarytypedef)
  - [TtmlDestinationSettingsTypeDef](#ttmldestinationsettingstypedef)
  - [UdpContainerSettingsTypeDef](#udpcontainersettingstypedef)
  - [UdpGroupSettingsTypeDef](#udpgroupsettingstypedef)
  - [UdpOutputSettingsTypeDef](#udpoutputsettingstypedef)
  - [VideoBlackFailoverSettingsTypeDef](#videoblackfailoversettingstypedef)
  - [VideoCodecSettingsTypeDef](#videocodecsettingstypedef)
  - [VideoDescriptionTypeDef](#videodescriptiontypedef)
  - [VideoSelectorColorSpaceSettingsTypeDef](#videoselectorcolorspacesettingstypedef)
  - [VideoSelectorPidTypeDef](#videoselectorpidtypedef)
  - [VideoSelectorProgramIdTypeDef](#videoselectorprogramidtypedef)
  - [VideoSelectorSettingsTypeDef](#videoselectorsettingstypedef)
  - [VideoSelectorTypeDef](#videoselectortypedef)
  - [VpcOutputSettingsDescriptionTypeDef](#vpcoutputsettingsdescriptiontypedef)
  - [WavSettingsTypeDef](#wavsettingstypedef)
  - [BatchDeleteResponseTypeDef](#batchdeleteresponsetypedef)
  - [BatchScheduleActionCreateRequestTypeDef](#batchscheduleactioncreaterequesttypedef)
  - [BatchScheduleActionDeleteRequestTypeDef](#batchscheduleactiondeleterequesttypedef)
  - [BatchStartResponseTypeDef](#batchstartresponsetypedef)
  - [BatchStopResponseTypeDef](#batchstopresponsetypedef)
  - [BatchUpdateScheduleResponseTypeDef](#batchupdatescheduleresponsetypedef)
  - [CreateChannelResponseTypeDef](#createchannelresponsetypedef)
  - [CreateInputResponseTypeDef](#createinputresponsetypedef)
  - [CreateInputSecurityGroupResponseTypeDef](#createinputsecuritygroupresponsetypedef)
  - [CreateMultiplexProgramResponseTypeDef](#createmultiplexprogramresponsetypedef)
  - [CreateMultiplexResponseTypeDef](#createmultiplexresponsetypedef)
  - [CreatePartnerInputResponseTypeDef](#createpartnerinputresponsetypedef)
  - [DeleteChannelResponseTypeDef](#deletechannelresponsetypedef)
  - [DeleteMultiplexProgramResponseTypeDef](#deletemultiplexprogramresponsetypedef)
  - [DeleteMultiplexResponseTypeDef](#deletemultiplexresponsetypedef)
  - [DeleteReservationResponseTypeDef](#deletereservationresponsetypedef)
  - [DescribeChannelResponseTypeDef](#describechannelresponsetypedef)
  - [DescribeInputDeviceResponseTypeDef](#describeinputdeviceresponsetypedef)
  - [DescribeInputDeviceThumbnailResponseTypeDef](#describeinputdevicethumbnailresponsetypedef)
  - [DescribeInputResponseTypeDef](#describeinputresponsetypedef)
  - [DescribeInputSecurityGroupResponseTypeDef](#describeinputsecuritygroupresponsetypedef)
  - [DescribeMultiplexProgramResponseTypeDef](#describemultiplexprogramresponsetypedef)
  - [DescribeMultiplexResponseTypeDef](#describemultiplexresponsetypedef)
  - [DescribeOfferingResponseTypeDef](#describeofferingresponsetypedef)
  - [DescribeReservationResponseTypeDef](#describereservationresponsetypedef)
  - [DescribeScheduleResponseTypeDef](#describescheduleresponsetypedef)
  - [InputDestinationRequestTypeDef](#inputdestinationrequesttypedef)
  - [InputDeviceConfigurableSettingsTypeDef](#inputdeviceconfigurablesettingstypedef)
  - [InputDeviceRequestTypeDef](#inputdevicerequesttypedef)
  - [InputSourceRequestTypeDef](#inputsourcerequesttypedef)
  - [InputVpcRequestTypeDef](#inputvpcrequesttypedef)
  - [InputWhitelistRuleCidrTypeDef](#inputwhitelistrulecidrtypedef)
  - [ListChannelsResponseTypeDef](#listchannelsresponsetypedef)
  - [ListInputDeviceTransfersResponseTypeDef](#listinputdevicetransfersresponsetypedef)
  - [ListInputDevicesResponseTypeDef](#listinputdevicesresponsetypedef)
  - [ListInputSecurityGroupsResponseTypeDef](#listinputsecuritygroupsresponsetypedef)
  - [ListInputsResponseTypeDef](#listinputsresponsetypedef)
  - [ListMultiplexProgramsResponseTypeDef](#listmultiplexprogramsresponsetypedef)
  - [ListMultiplexesResponseTypeDef](#listmultiplexesresponsetypedef)
  - [ListOfferingsResponseTypeDef](#listofferingsresponsetypedef)
  - [ListReservationsResponseTypeDef](#listreservationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MediaConnectFlowRequestTypeDef](#mediaconnectflowrequesttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PurchaseOfferingResponseTypeDef](#purchaseofferingresponsetypedef)
  - [StartChannelResponseTypeDef](#startchannelresponsetypedef)
  - [StartMultiplexResponseTypeDef](#startmultiplexresponsetypedef)
  - [StopChannelResponseTypeDef](#stopchannelresponsetypedef)
  - [StopMultiplexResponseTypeDef](#stopmultiplexresponsetypedef)
  - [UpdateChannelClassResponseTypeDef](#updatechannelclassresponsetypedef)
  - [UpdateChannelResponseTypeDef](#updatechannelresponsetypedef)
  - [UpdateInputDeviceResponseTypeDef](#updateinputdeviceresponsetypedef)
  - [UpdateInputResponseTypeDef](#updateinputresponsetypedef)
  - [UpdateInputSecurityGroupResponseTypeDef](#updateinputsecuritygroupresponsetypedef)
  - [UpdateMultiplexProgramResponseTypeDef](#updatemultiplexprogramresponsetypedef)
  - [UpdateMultiplexResponseTypeDef](#updatemultiplexresponsetypedef)
  - [UpdateReservationResponseTypeDef](#updatereservationresponsetypedef)
  - [VpcOutputSettingsTypeDef](#vpcoutputsettingstypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AacSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AacSettingsTypeDef
```




Optional fields:
- `Bitrate`: `float`
- `CodingMode`: `AacCodingMode`
- `InputType`: `AacInputType`
- `Profile`: `AacProfile`
- `RateControlMode`: `AacRateControlMode`
- `RawFormat`: `AacRawFormat`
- `SampleRate`: `float`
- `Spec`: `AacSpec`
- `VbrQuality`: `AacVbrQuality`


## Ac3SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Ac3SettingsTypeDef
```




Optional fields:
- `Bitrate`: `float`
- `BitstreamMode`: `Ac3BitstreamMode`
- `CodingMode`: `Ac3CodingMode`
- `Dialnorm`: `int`
- `DrcProfile`: `Ac3DrcProfile`
- `LfeFilter`: `Ac3LfeFilter`
- `MetadataControl`: `Ac3MetadataControl`


## AncillarySourceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AncillarySourceSettingsTypeDef
```




Optional fields:
- `SourceAncillaryChannelNumber`: `int`


## ArchiveCdnSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ArchiveCdnSettingsTypeDef
```




Optional fields:
- `ArchiveS3Settings`: `"ArchiveS3SettingsTypeDef"`


## ArchiveContainerSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ArchiveContainerSettingsTypeDef
```




Optional fields:
- `M2tsSettings`: `"M2tsSettingsTypeDef"`
- `RawSettings`: `Dict[str, Any]`


## ArchiveGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ArchiveGroupSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`



Optional fields:
- `ArchiveCdnSettings`: `"ArchiveCdnSettingsTypeDef"`
- `RolloverInterval`: `int`


## ArchiveOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ArchiveOutputSettingsTypeDef
```


Required fields:
- `ContainerSettings`: `"ArchiveContainerSettingsTypeDef"`



Optional fields:
- `Extension`: `str`
- `NameModifier`: `str`


## ArchiveS3SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ArchiveS3SettingsTypeDef
```




Optional fields:
- `CannedAcl`: `S3CannedAcl`


## AudioChannelMappingTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioChannelMappingTypeDef
```


Required fields:
- `InputChannelLevels`: `List["InputChannelLevelTypeDef"]`
- `OutputChannel`: `int`




## AudioCodecSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioCodecSettingsTypeDef
```




Optional fields:
- `AacSettings`: `"AacSettingsTypeDef"`
- `Ac3Settings`: `"Ac3SettingsTypeDef"`
- `Eac3Settings`: `"Eac3SettingsTypeDef"`
- `Mp2Settings`: `"Mp2SettingsTypeDef"`
- `PassThroughSettings`: `Dict[str, Any]`
- `WavSettings`: `"WavSettingsTypeDef"`


## AudioDescriptionTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioDescriptionTypeDef
```


Required fields:
- `AudioSelectorName`: `str`
- `Name`: `str`



Optional fields:
- `AudioNormalizationSettings`: `"AudioNormalizationSettingsTypeDef"`
- `AudioType`: `AudioType`
- `AudioTypeControl`: `AudioDescriptionAudioTypeControl`
- `CodecSettings`: `"AudioCodecSettingsTypeDef"`
- `LanguageCode`: `str`
- `LanguageCodeControl`: `AudioDescriptionLanguageCodeControl`
- `RemixSettings`: `"RemixSettingsTypeDef"`
- `StreamName`: `str`


## AudioLanguageSelectionTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioLanguageSelectionTypeDef
```


Required fields:
- `LanguageCode`: `str`



Optional fields:
- `LanguageSelectionPolicy`: `AudioLanguageSelectionPolicy`


## AudioNormalizationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioNormalizationSettingsTypeDef
```




Optional fields:
- `Algorithm`: `AudioNormalizationAlgorithm`
- `AlgorithmControl`: `AudioNormalizationAlgorithmControl`
- `TargetLkfs`: `float`


## AudioOnlyHlsSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioOnlyHlsSettingsTypeDef
```




Optional fields:
- `AudioGroupId`: `str`
- `AudioOnlyImage`: `"InputLocationTypeDef"`
- `AudioTrackType`: `AudioOnlyHlsTrackType`
- `SegmentType`: `AudioOnlyHlsSegmentType`


## AudioPidSelectionTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioPidSelectionTypeDef
```


Required fields:
- `Pid`: `int`




## AudioSelectorSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioSelectorSettingsTypeDef
```




Optional fields:
- `AudioLanguageSelection`: `"AudioLanguageSelectionTypeDef"`
- `AudioPidSelection`: `"AudioPidSelectionTypeDef"`
- `AudioTrackSelection`: `"AudioTrackSelectionTypeDef"`


## AudioSelectorTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioSelectorTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `SelectorSettings`: `"AudioSelectorSettingsTypeDef"`


## AudioSilenceFailoverSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioSilenceFailoverSettingsTypeDef
```


Required fields:
- `AudioSelectorName`: `str`



Optional fields:
- `AudioSilenceThresholdMsec`: `int`


## AudioTrackSelectionTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioTrackSelectionTypeDef
```


Required fields:
- `Tracks`: `List["AudioTrackTypeDef"]`




## AudioTrackTypeDef

```python
from mypy_boto3_medialive.type_defs import AudioTrackTypeDef
```


Required fields:
- `Track`: `int`




## AutomaticInputFailoverSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AutomaticInputFailoverSettingsTypeDef
```


Required fields:
- `SecondaryInputId`: `str`



Optional fields:
- `ErrorClearTimeMsec`: `int`
- `FailoverConditions`: `List["FailoverConditionTypeDef"]`
- `InputPreference`: `InputPreference`


## AvailBlankingTypeDef

```python
from mypy_boto3_medialive.type_defs import AvailBlankingTypeDef
```




Optional fields:
- `AvailBlankingImage`: `"InputLocationTypeDef"`
- `State`: `AvailBlankingState`


## AvailConfigurationTypeDef

```python
from mypy_boto3_medialive.type_defs import AvailConfigurationTypeDef
```




Optional fields:
- `AvailSettings`: `"AvailSettingsTypeDef"`


## AvailSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import AvailSettingsTypeDef
```




Optional fields:
- `Scte35SpliceInsert`: `"Scte35SpliceInsertTypeDef"`
- `Scte35TimeSignalApos`: `"Scte35TimeSignalAposTypeDef"`


## BatchFailedResultModelTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchFailedResultModelTypeDef
```




Optional fields:
- `Arn`: `str`
- `Code`: `str`
- `Id`: `str`
- `Message`: `str`


## BatchScheduleActionCreateResultTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchScheduleActionCreateResultTypeDef
```


Required fields:
- `ScheduleActions`: `List["ScheduleActionTypeDef"]`




## BatchScheduleActionDeleteResultTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchScheduleActionDeleteResultTypeDef
```


Required fields:
- `ScheduleActions`: `List["ScheduleActionTypeDef"]`




## BatchSuccessfulResultModelTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchSuccessfulResultModelTypeDef
```




Optional fields:
- `Arn`: `str`
- `Id`: `str`
- `State`: `str`


## BlackoutSlateTypeDef

```python
from mypy_boto3_medialive.type_defs import BlackoutSlateTypeDef
```




Optional fields:
- `BlackoutSlateImage`: `"InputLocationTypeDef"`
- `NetworkEndBlackout`: `BlackoutSlateNetworkEndBlackout`
- `NetworkEndBlackoutImage`: `"InputLocationTypeDef"`
- `NetworkId`: `str`
- `State`: `BlackoutSlateState`


## BurnInDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import BurnInDestinationSettingsTypeDef
```




Optional fields:
- `Alignment`: `BurnInAlignment`
- `BackgroundColor`: `BurnInBackgroundColor`
- `BackgroundOpacity`: `int`
- `Font`: `"InputLocationTypeDef"`
- `FontColor`: `BurnInFontColor`
- `FontOpacity`: `int`
- `FontResolution`: `int`
- `FontSize`: `str`
- `OutlineColor`: `BurnInOutlineColor`
- `OutlineSize`: `int`
- `ShadowColor`: `BurnInShadowColor`
- `ShadowOpacity`: `int`
- `ShadowXOffset`: `int`
- `ShadowYOffset`: `int`
- `TeletextGridControl`: `BurnInTeletextGridControl`
- `XPosition`: `int`
- `YPosition`: `int`


## CaptionDescriptionTypeDef

```python
from mypy_boto3_medialive.type_defs import CaptionDescriptionTypeDef
```


Required fields:
- `CaptionSelectorName`: `str`
- `Name`: `str`



Optional fields:
- `DestinationSettings`: `"CaptionDestinationSettingsTypeDef"`
- `LanguageCode`: `str`
- `LanguageDescription`: `str`


## CaptionDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import CaptionDestinationSettingsTypeDef
```




Optional fields:
- `AribDestinationSettings`: `Dict[str, Any]`
- `BurnInDestinationSettings`: `"BurnInDestinationSettingsTypeDef"`
- `DvbSubDestinationSettings`: `"DvbSubDestinationSettingsTypeDef"`
- `EbuTtDDestinationSettings`: `"EbuTtDDestinationSettingsTypeDef"`
- `EmbeddedDestinationSettings`: `Dict[str, Any]`
- `EmbeddedPlusScte20DestinationSettings`: `Dict[str, Any]`
- `RtmpCaptionInfoDestinationSettings`: `Dict[str, Any]`
- `Scte20PlusEmbeddedDestinationSettings`: `Dict[str, Any]`
- `Scte27DestinationSettings`: `Dict[str, Any]`
- `SmpteTtDestinationSettings`: `Dict[str, Any]`
- `TeletextDestinationSettings`: `Dict[str, Any]`
- `TtmlDestinationSettings`: `"TtmlDestinationSettingsTypeDef"`
- `WebvttDestinationSettings`: `Dict[str, Any]`


## CaptionLanguageMappingTypeDef

```python
from mypy_boto3_medialive.type_defs import CaptionLanguageMappingTypeDef
```


Required fields:
- `CaptionChannel`: `int`
- `LanguageCode`: `str`
- `LanguageDescription`: `str`




## CaptionRectangleTypeDef

```python
from mypy_boto3_medialive.type_defs import CaptionRectangleTypeDef
```


Required fields:
- `Height`: `float`
- `LeftOffset`: `float`
- `TopOffset`: `float`
- `Width`: `float`




## CaptionSelectorSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import CaptionSelectorSettingsTypeDef
```




Optional fields:
- `AncillarySourceSettings`: `"AncillarySourceSettingsTypeDef"`
- `AribSourceSettings`: `Dict[str, Any]`
- `DvbSubSourceSettings`: `"DvbSubSourceSettingsTypeDef"`
- `EmbeddedSourceSettings`: `"EmbeddedSourceSettingsTypeDef"`
- `Scte20SourceSettings`: `"Scte20SourceSettingsTypeDef"`
- `Scte27SourceSettings`: `"Scte27SourceSettingsTypeDef"`
- `TeletextSourceSettings`: `"TeletextSourceSettingsTypeDef"`


## CaptionSelectorTypeDef

```python
from mypy_boto3_medialive.type_defs import CaptionSelectorTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `LanguageCode`: `str`
- `SelectorSettings`: `"CaptionSelectorSettingsTypeDef"`


## CdiInputSpecificationTypeDef

```python
from mypy_boto3_medialive.type_defs import CdiInputSpecificationTypeDef
```




Optional fields:
- `Resolution`: `CdiInputResolution`


## ChannelEgressEndpointTypeDef

```python
from mypy_boto3_medialive.type_defs import ChannelEgressEndpointTypeDef
```




Optional fields:
- `SourceIp`: `str`


## ChannelSummaryTypeDef

```python
from mypy_boto3_medialive.type_defs import ChannelSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `CdiInputSpecification`: `"CdiInputSpecificationTypeDef"`
- `ChannelClass`: `ChannelClass`
- `Destinations`: `List["OutputDestinationTypeDef"]`
- `EgressEndpoints`: `List["ChannelEgressEndpointTypeDef"]`
- `Id`: `str`
- `InputAttachments`: `List["InputAttachmentTypeDef"]`
- `InputSpecification`: `"InputSpecificationTypeDef"`
- `LogLevel`: `LogLevel`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `RoleArn`: `str`
- `State`: `ChannelState`
- `Tags`: `Dict[str, str]`
- `Vpc`: `"VpcOutputSettingsDescriptionTypeDef"`


## ChannelTypeDef

```python
from mypy_boto3_medialive.type_defs import ChannelTypeDef
```




Optional fields:
- `Arn`: `str`
- `CdiInputSpecification`: `"CdiInputSpecificationTypeDef"`
- `ChannelClass`: `ChannelClass`
- `Destinations`: `List["OutputDestinationTypeDef"]`
- `EgressEndpoints`: `List["ChannelEgressEndpointTypeDef"]`
- `EncoderSettings`: `"EncoderSettingsTypeDef"`
- `Id`: `str`
- `InputAttachments`: `List["InputAttachmentTypeDef"]`
- `InputSpecification`: `"InputSpecificationTypeDef"`
- `LogLevel`: `LogLevel`
- `Name`: `str`
- `PipelineDetails`: `List["PipelineDetailTypeDef"]`
- `PipelinesRunningCount`: `int`
- `RoleArn`: `str`
- `State`: `ChannelState`
- `Tags`: `Dict[str, str]`
- `Vpc`: `"VpcOutputSettingsDescriptionTypeDef"`


## DvbNitSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import DvbNitSettingsTypeDef
```


Required fields:
- `NetworkId`: `int`
- `NetworkName`: `str`



Optional fields:
- `RepInterval`: `int`


## DvbSdtSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import DvbSdtSettingsTypeDef
```




Optional fields:
- `OutputSdt`: `DvbSdtOutputSdt`
- `RepInterval`: `int`
- `ServiceName`: `str`
- `ServiceProviderName`: `str`


## DvbSubDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import DvbSubDestinationSettingsTypeDef
```




Optional fields:
- `Alignment`: `DvbSubDestinationAlignment`
- `BackgroundColor`: `DvbSubDestinationBackgroundColor`
- `BackgroundOpacity`: `int`
- `Font`: `"InputLocationTypeDef"`
- `FontColor`: `DvbSubDestinationFontColor`
- `FontOpacity`: `int`
- `FontResolution`: `int`
- `FontSize`: `str`
- `OutlineColor`: `DvbSubDestinationOutlineColor`
- `OutlineSize`: `int`
- `ShadowColor`: `DvbSubDestinationShadowColor`
- `ShadowOpacity`: `int`
- `ShadowXOffset`: `int`
- `ShadowYOffset`: `int`
- `TeletextGridControl`: `DvbSubDestinationTeletextGridControl`
- `XPosition`: `int`
- `YPosition`: `int`


## DvbSubSourceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import DvbSubSourceSettingsTypeDef
```




Optional fields:
- `Pid`: `int`


## DvbTdtSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import DvbTdtSettingsTypeDef
```




Optional fields:
- `RepInterval`: `int`


## Eac3SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Eac3SettingsTypeDef
```




Optional fields:
- `AttenuationControl`: `Eac3AttenuationControl`
- `Bitrate`: `float`
- `BitstreamMode`: `Eac3BitstreamMode`
- `CodingMode`: `Eac3CodingMode`
- `DcFilter`: `Eac3DcFilter`
- `Dialnorm`: `int`
- `DrcLine`: `Eac3DrcLine`
- `DrcRf`: `Eac3DrcRf`
- `LfeControl`: `Eac3LfeControl`
- `LfeFilter`: `Eac3LfeFilter`
- `LoRoCenterMixLevel`: `float`
- `LoRoSurroundMixLevel`: `float`
- `LtRtCenterMixLevel`: `float`
- `LtRtSurroundMixLevel`: `float`
- `MetadataControl`: `Eac3MetadataControl`
- `PassthroughControl`: `Eac3PassthroughControl`
- `PhaseControl`: `Eac3PhaseControl`
- `StereoDownmix`: `Eac3StereoDownmix`
- `SurroundExMode`: `Eac3SurroundExMode`
- `SurroundMode`: `Eac3SurroundMode`


## EbuTtDDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import EbuTtDDestinationSettingsTypeDef
```




Optional fields:
- `CopyrightHolder`: `str`
- `FillLineGap`: `EbuTtDFillLineGapControl`
- `FontFamily`: `str`
- `StyleControl`: `EbuTtDDestinationStyleControl`


## EmbeddedSourceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import EmbeddedSourceSettingsTypeDef
```




Optional fields:
- `Convert608To708`: `EmbeddedConvert608To708`
- `Scte20Detection`: `EmbeddedScte20Detection`
- `Source608ChannelNumber`: `int`
- `Source608TrackNumber`: `int`


## EncoderSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import EncoderSettingsTypeDef
```


Required fields:
- `AudioDescriptions`: `List["AudioDescriptionTypeDef"]`
- `OutputGroups`: `List["OutputGroupTypeDef"]`
- `TimecodeConfig`: `"TimecodeConfigTypeDef"`
- `VideoDescriptions`: `List["VideoDescriptionTypeDef"]`



Optional fields:
- `AvailBlanking`: `"AvailBlankingTypeDef"`
- `AvailConfiguration`: `"AvailConfigurationTypeDef"`
- `BlackoutSlate`: `"BlackoutSlateTypeDef"`
- `CaptionDescriptions`: `List["CaptionDescriptionTypeDef"]`
- `FeatureActivations`: `"FeatureActivationsTypeDef"`
- `GlobalConfiguration`: `"GlobalConfigurationTypeDef"`
- `MotionGraphicsConfiguration`: `"MotionGraphicsConfigurationTypeDef"`
- `NielsenConfiguration`: `"NielsenConfigurationTypeDef"`


## FailoverConditionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FailoverConditionSettingsTypeDef
```




Optional fields:
- `AudioSilenceSettings`: `"AudioSilenceFailoverSettingsTypeDef"`
- `InputLossSettings`: `"InputLossFailoverSettingsTypeDef"`
- `VideoBlackSettings`: `"VideoBlackFailoverSettingsTypeDef"`


## FailoverConditionTypeDef

```python
from mypy_boto3_medialive.type_defs import FailoverConditionTypeDef
```




Optional fields:
- `FailoverConditionSettings`: `"FailoverConditionSettingsTypeDef"`


## FeatureActivationsTypeDef

```python
from mypy_boto3_medialive.type_defs import FeatureActivationsTypeDef
```




Optional fields:
- `InputPrepareScheduleActions`: `FeatureActivationsInputPrepareScheduleActions`


## FecOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FecOutputSettingsTypeDef
```




Optional fields:
- `ColumnDepth`: `int`
- `IncludeFec`: `FecOutputIncludeFec`
- `RowLength`: `int`


## FixedModeScheduleActionStartSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FixedModeScheduleActionStartSettingsTypeDef
```


Required fields:
- `Time`: `str`




## Fmp4HlsSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Fmp4HlsSettingsTypeDef
```




Optional fields:
- `AudioRenditionSets`: `str`
- `NielsenId3Behavior`: `Fmp4NielsenId3Behavior`
- `TimedMetadataBehavior`: `Fmp4TimedMetadataBehavior`


## FollowModeScheduleActionStartSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FollowModeScheduleActionStartSettingsTypeDef
```


Required fields:
- `FollowPoint`: `FollowPoint`
- `ReferenceActionName`: `str`




## FrameCaptureCdnSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FrameCaptureCdnSettingsTypeDef
```




Optional fields:
- `FrameCaptureS3Settings`: `"FrameCaptureS3SettingsTypeDef"`


## FrameCaptureGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FrameCaptureGroupSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`



Optional fields:
- `FrameCaptureCdnSettings`: `"FrameCaptureCdnSettingsTypeDef"`


## FrameCaptureOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FrameCaptureOutputSettingsTypeDef
```




Optional fields:
- `NameModifier`: `str`


## FrameCaptureS3SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FrameCaptureS3SettingsTypeDef
```




Optional fields:
- `CannedAcl`: `S3CannedAcl`


## FrameCaptureSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import FrameCaptureSettingsTypeDef
```




Optional fields:
- `CaptureInterval`: `int`
- `CaptureIntervalUnits`: `FrameCaptureIntervalUnit`


## GlobalConfigurationTypeDef

```python
from mypy_boto3_medialive.type_defs import GlobalConfigurationTypeDef
```




Optional fields:
- `InitialAudioGain`: `int`
- `InputEndAction`: `GlobalConfigurationInputEndAction`
- `InputLossBehavior`: `"InputLossBehaviorTypeDef"`
- `OutputLockingMode`: `GlobalConfigurationOutputLockingMode`
- `OutputTimingSource`: `GlobalConfigurationOutputTimingSource`
- `SupportLowFramerateInputs`: `GlobalConfigurationLowFramerateInputs`


## H264ColorSpaceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import H264ColorSpaceSettingsTypeDef
```




Optional fields:
- `ColorSpacePassthroughSettings`: `Dict[str, Any]`
- `Rec601Settings`: `Dict[str, Any]`
- `Rec709Settings`: `Dict[str, Any]`


## H264FilterSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import H264FilterSettingsTypeDef
```




Optional fields:
- `TemporalFilterSettings`: `"TemporalFilterSettingsTypeDef"`


## H264SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import H264SettingsTypeDef
```




Optional fields:
- `AdaptiveQuantization`: `H264AdaptiveQuantization`
- `AfdSignaling`: `AfdSignaling`
- `Bitrate`: `int`
- `BufFillPct`: `int`
- `BufSize`: `int`
- `ColorMetadata`: `H264ColorMetadata`
- `ColorSpaceSettings`: `"H264ColorSpaceSettingsTypeDef"`
- `EntropyEncoding`: `H264EntropyEncoding`
- `FilterSettings`: `"H264FilterSettingsTypeDef"`
- `FixedAfd`: `FixedAfd`
- `FlickerAq`: `H264FlickerAq`
- `ForceFieldPictures`: `H264ForceFieldPictures`
- `FramerateControl`: `H264FramerateControl`
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`
- `GopBReference`: `H264GopBReference`
- `GopClosedCadence`: `int`
- `GopNumBFrames`: `int`
- `GopSize`: `float`
- `GopSizeUnits`: `H264GopSizeUnits`
- `Level`: `H264Level`
- `LookAheadRateControl`: `H264LookAheadRateControl`
- `MaxBitrate`: `int`
- `MinIInterval`: `int`
- `NumRefFrames`: `int`
- `ParControl`: `H264ParControl`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `Profile`: `H264Profile`
- `QualityLevel`: `H264QualityLevel`
- `QvbrQualityLevel`: `int`
- `RateControlMode`: `H264RateControlMode`
- `ScanType`: `H264ScanType`
- `SceneChangeDetect`: `H264SceneChangeDetect`
- `Slices`: `int`
- `Softness`: `int`
- `SpatialAq`: `H264SpatialAq`
- `SubgopLength`: `H264SubGopLength`
- `Syntax`: `H264Syntax`
- `TemporalAq`: `H264TemporalAq`
- `TimecodeInsertion`: `H264TimecodeInsertionBehavior`


## H265ColorSpaceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import H265ColorSpaceSettingsTypeDef
```




Optional fields:
- `ColorSpacePassthroughSettings`: `Dict[str, Any]`
- `Hdr10Settings`: `"Hdr10SettingsTypeDef"`
- `Rec601Settings`: `Dict[str, Any]`
- `Rec709Settings`: `Dict[str, Any]`


## H265FilterSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import H265FilterSettingsTypeDef
```




Optional fields:
- `TemporalFilterSettings`: `"TemporalFilterSettingsTypeDef"`


## H265SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import H265SettingsTypeDef
```


Required fields:
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`



Optional fields:
- `AdaptiveQuantization`: `H265AdaptiveQuantization`
- `AfdSignaling`: `AfdSignaling`
- `AlternativeTransferFunction`: `H265AlternativeTransferFunction`
- `Bitrate`: `int`
- `BufSize`: `int`
- `ColorMetadata`: `H265ColorMetadata`
- `ColorSpaceSettings`: `"H265ColorSpaceSettingsTypeDef"`
- `FilterSettings`: `"H265FilterSettingsTypeDef"`
- `FixedAfd`: `FixedAfd`
- `FlickerAq`: `H265FlickerAq`
- `GopClosedCadence`: `int`
- `GopSize`: `float`
- `GopSizeUnits`: `H265GopSizeUnits`
- `Level`: `H265Level`
- `LookAheadRateControl`: `H265LookAheadRateControl`
- `MaxBitrate`: `int`
- `MinIInterval`: `int`
- `ParDenominator`: `int`
- `ParNumerator`: `int`
- `Profile`: `H265Profile`
- `QvbrQualityLevel`: `int`
- `RateControlMode`: `H265RateControlMode`
- `ScanType`: `H265ScanType`
- `SceneChangeDetect`: `H265SceneChangeDetect`
- `Slices`: `int`
- `Tier`: `H265Tier`
- `TimecodeInsertion`: `H265TimecodeInsertionBehavior`


## Hdr10SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Hdr10SettingsTypeDef
```




Optional fields:
- `MaxCll`: `int`
- `MaxFall`: `int`


## HlsAkamaiSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsAkamaiSettingsTypeDef
```




Optional fields:
- `ConnectionRetryInterval`: `int`
- `FilecacheDuration`: `int`
- `HttpTransferMode`: `HlsAkamaiHttpTransferMode`
- `NumRetries`: `int`
- `RestartDelay`: `int`
- `Salt`: `str`
- `Token`: `str`


## HlsBasicPutSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsBasicPutSettingsTypeDef
```




Optional fields:
- `ConnectionRetryInterval`: `int`
- `FilecacheDuration`: `int`
- `NumRetries`: `int`
- `RestartDelay`: `int`


## HlsCdnSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsCdnSettingsTypeDef
```




Optional fields:
- `HlsAkamaiSettings`: `"HlsAkamaiSettingsTypeDef"`
- `HlsBasicPutSettings`: `"HlsBasicPutSettingsTypeDef"`
- `HlsMediaStoreSettings`: `"HlsMediaStoreSettingsTypeDef"`
- `HlsS3Settings`: `"HlsS3SettingsTypeDef"`
- `HlsWebdavSettings`: `"HlsWebdavSettingsTypeDef"`


## HlsGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsGroupSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`



Optional fields:
- `AdMarkers`: `List[HlsAdMarkers]`
- `BaseUrlContent`: `str`
- `BaseUrlContent1`: `str`
- `BaseUrlManifest`: `str`
- `BaseUrlManifest1`: `str`
- `CaptionLanguageMappings`: `List["CaptionLanguageMappingTypeDef"]`
- `CaptionLanguageSetting`: `HlsCaptionLanguageSetting`
- `ClientCache`: `HlsClientCache`
- `CodecSpecification`: `HlsCodecSpecification`
- `ConstantIv`: `str`
- `DirectoryStructure`: `HlsDirectoryStructure`
- `DiscontinuityTags`: `HlsDiscontinuityTags`
- `EncryptionType`: `HlsEncryptionType`
- `HlsCdnSettings`: `"HlsCdnSettingsTypeDef"`
- `HlsId3SegmentTagging`: `HlsId3SegmentTaggingState`
- `IFrameOnlyPlaylists`: `IFrameOnlyPlaylistType`
- `IncompleteSegmentBehavior`: `HlsIncompleteSegmentBehavior`
- `IndexNSegments`: `int`
- `InputLossAction`: `InputLossActionForHlsOut`
- `IvInManifest`: `HlsIvInManifest`
- `IvSource`: `HlsIvSource`
- `KeepSegments`: `int`
- `KeyFormat`: `str`
- `KeyFormatVersions`: `str`
- `KeyProviderSettings`: `"KeyProviderSettingsTypeDef"`
- `ManifestCompression`: `HlsManifestCompression`
- `ManifestDurationFormat`: `HlsManifestDurationFormat`
- `MinSegmentLength`: `int`
- `Mode`: `HlsMode`
- `OutputSelection`: `HlsOutputSelection`
- `ProgramDateTime`: `HlsProgramDateTime`
- `ProgramDateTimePeriod`: `int`
- `RedundantManifest`: `HlsRedundantManifest`
- `SegmentLength`: `int`
- `SegmentationMode`: `HlsSegmentationMode`
- `SegmentsPerSubdirectory`: `int`
- `StreamInfResolution`: `HlsStreamInfResolution`
- `TimedMetadataId3Frame`: `HlsTimedMetadataId3Frame`
- `TimedMetadataId3Period`: `int`
- `TimestampDeltaMilliseconds`: `int`
- `TsFileMode`: `HlsTsFileMode`


## HlsId3SegmentTaggingScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsId3SegmentTaggingScheduleActionSettingsTypeDef
```


Required fields:
- `Tag`: `str`




## HlsInputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsInputSettingsTypeDef
```




Optional fields:
- `Bandwidth`: `int`
- `BufferSegments`: `int`
- `Retries`: `int`
- `RetryInterval`: `int`


## HlsMediaStoreSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsMediaStoreSettingsTypeDef
```




Optional fields:
- `ConnectionRetryInterval`: `int`
- `FilecacheDuration`: `int`
- `MediaStoreStorageClass`: `HlsMediaStoreStorageClass`
- `NumRetries`: `int`
- `RestartDelay`: `int`


## HlsOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsOutputSettingsTypeDef
```


Required fields:
- `HlsSettings`: `"HlsSettingsTypeDef"`



Optional fields:
- `H265PackagingType`: `HlsH265PackagingType`
- `NameModifier`: `str`
- `SegmentModifier`: `str`


## HlsS3SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsS3SettingsTypeDef
```




Optional fields:
- `CannedAcl`: `S3CannedAcl`


## HlsSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsSettingsTypeDef
```




Optional fields:
- `AudioOnlyHlsSettings`: `"AudioOnlyHlsSettingsTypeDef"`
- `Fmp4HlsSettings`: `"Fmp4HlsSettingsTypeDef"`
- `FrameCaptureHlsSettings`: `Dict[str, Any]`
- `StandardHlsSettings`: `"StandardHlsSettingsTypeDef"`


## HlsTimedMetadataScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsTimedMetadataScheduleActionSettingsTypeDef
```


Required fields:
- `Id3`: `str`




## HlsWebdavSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import HlsWebdavSettingsTypeDef
```




Optional fields:
- `ConnectionRetryInterval`: `int`
- `FilecacheDuration`: `int`
- `HttpTransferMode`: `HlsWebdavHttpTransferMode`
- `NumRetries`: `int`
- `RestartDelay`: `int`


## InputAttachmentTypeDef

```python
from mypy_boto3_medialive.type_defs import InputAttachmentTypeDef
```




Optional fields:
- `AutomaticInputFailoverSettings`: `"AutomaticInputFailoverSettingsTypeDef"`
- `InputAttachmentName`: `str`
- `InputId`: `str`
- `InputSettings`: `"InputSettingsTypeDef"`


## InputChannelLevelTypeDef

```python
from mypy_boto3_medialive.type_defs import InputChannelLevelTypeDef
```


Required fields:
- `Gain`: `int`
- `InputChannel`: `int`




## InputClippingSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputClippingSettingsTypeDef
```


Required fields:
- `InputTimecodeSource`: `InputTimecodeSource`



Optional fields:
- `StartTimecode`: `"StartTimecodeTypeDef"`
- `StopTimecode`: `"StopTimecodeTypeDef"`


## InputDestinationTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDestinationTypeDef
```




Optional fields:
- `Ip`: `str`
- `Port`: `str`
- `Url`: `str`
- `Vpc`: `"InputDestinationVpcTypeDef"`


## InputDestinationVpcTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDestinationVpcTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `NetworkInterfaceId`: `str`


## InputDeviceHdSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceHdSettingsTypeDef
```




Optional fields:
- `ActiveInput`: `InputDeviceActiveInput`
- `ConfiguredInput`: `InputDeviceConfiguredInput`
- `DeviceState`: `InputDeviceState`
- `Framerate`: `float`
- `Height`: `int`
- `MaxBitrate`: `int`
- `ScanType`: `InputDeviceScanType`
- `Width`: `int`


## InputDeviceNetworkSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceNetworkSettingsTypeDef
```




Optional fields:
- `DnsAddresses`: `List[str]`
- `Gateway`: `str`
- `IpAddress`: `str`
- `IpScheme`: `InputDeviceIpScheme`
- `SubnetMask`: `str`


## InputDeviceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceSettingsTypeDef
```




Optional fields:
- `Id`: `str`


## InputDeviceSummaryTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `ConnectionState`: `InputDeviceConnectionState`
- `DeviceSettingsSyncState`: `DeviceSettingsSyncState`
- `DeviceUpdateStatus`: `DeviceUpdateStatus`
- `HdDeviceSettings`: `"InputDeviceHdSettingsTypeDef"`
- `Id`: `str`
- `MacAddress`: `str`
- `Name`: `str`
- `NetworkSettings`: `"InputDeviceNetworkSettingsTypeDef"`
- `SerialNumber`: `str`
- `Type`: `InputDeviceType`
- `UhdDeviceSettings`: `"InputDeviceUhdSettingsTypeDef"`


## InputDeviceUhdSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceUhdSettingsTypeDef
```




Optional fields:
- `ActiveInput`: `InputDeviceActiveInput`
- `ConfiguredInput`: `InputDeviceConfiguredInput`
- `DeviceState`: `InputDeviceState`
- `Framerate`: `float`
- `Height`: `int`
- `MaxBitrate`: `int`
- `ScanType`: `InputDeviceScanType`
- `Width`: `int`


## InputLocationTypeDef

```python
from mypy_boto3_medialive.type_defs import InputLocationTypeDef
```


Required fields:
- `Uri`: `str`



Optional fields:
- `PasswordParam`: `str`
- `Username`: `str`


## InputLossBehaviorTypeDef

```python
from mypy_boto3_medialive.type_defs import InputLossBehaviorTypeDef
```




Optional fields:
- `BlackFrameMsec`: `int`
- `InputLossImageColor`: `str`
- `InputLossImageSlate`: `"InputLocationTypeDef"`
- `InputLossImageType`: `InputLossImageType`
- `RepeatFrameMsec`: `int`


## InputLossFailoverSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputLossFailoverSettingsTypeDef
```




Optional fields:
- `InputLossThresholdMsec`: `int`


## InputPrepareScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputPrepareScheduleActionSettingsTypeDef
```




Optional fields:
- `InputAttachmentNameReference`: `str`
- `InputClippingSettings`: `"InputClippingSettingsTypeDef"`
- `UrlPath`: `List[str]`


## InputSecurityGroupTypeDef

```python
from mypy_boto3_medialive.type_defs import InputSecurityGroupTypeDef
```




Optional fields:
- `Arn`: `str`
- `Id`: `str`
- `Inputs`: `List[str]`
- `State`: `InputSecurityGroupState`
- `Tags`: `Dict[str, str]`
- `WhitelistRules`: `List["InputWhitelistRuleTypeDef"]`


## InputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputSettingsTypeDef
```




Optional fields:
- `AudioSelectors`: `List["AudioSelectorTypeDef"]`
- `CaptionSelectors`: `List["CaptionSelectorTypeDef"]`
- `DeblockFilter`: `InputDeblockFilter`
- `DenoiseFilter`: `InputDenoiseFilter`
- `FilterStrength`: `int`
- `InputFilter`: `InputFilter`
- `NetworkInputSettings`: `"NetworkInputSettingsTypeDef"`
- `Smpte2038DataPreference`: `Smpte2038DataPreference`
- `SourceEndBehavior`: `InputSourceEndBehavior`
- `VideoSelector`: `"VideoSelectorTypeDef"`


## InputSourceTypeDef

```python
from mypy_boto3_medialive.type_defs import InputSourceTypeDef
```




Optional fields:
- `PasswordParam`: `str`
- `Url`: `str`
- `Username`: `str`


## InputSpecificationTypeDef

```python
from mypy_boto3_medialive.type_defs import InputSpecificationTypeDef
```




Optional fields:
- `Codec`: `InputCodec`
- `MaximumBitrate`: `InputMaximumBitrate`
- `Resolution`: `InputResolution`


## InputSwitchScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputSwitchScheduleActionSettingsTypeDef
```


Required fields:
- `InputAttachmentNameReference`: `str`



Optional fields:
- `InputClippingSettings`: `"InputClippingSettingsTypeDef"`
- `UrlPath`: `List[str]`


## InputTypeDef

```python
from mypy_boto3_medialive.type_defs import InputTypeDef
```




Optional fields:
- `Arn`: `str`
- `AttachedChannels`: `List[str]`
- `Destinations`: `List["InputDestinationTypeDef"]`
- `Id`: `str`
- `InputClass`: `InputClass`
- `InputDevices`: `List["InputDeviceSettingsTypeDef"]`
- `InputPartnerIds`: `List[str]`
- `InputSourceType`: `InputSourceType`
- `MediaConnectFlows`: `List["MediaConnectFlowTypeDef"]`
- `Name`: `str`
- `RoleArn`: `str`
- `SecurityGroups`: `List[str]`
- `Sources`: `List["InputSourceTypeDef"]`
- `State`: `InputState`
- `Tags`: `Dict[str, str]`
- `Type`: `InputType`


## InputWhitelistRuleTypeDef

```python
from mypy_boto3_medialive.type_defs import InputWhitelistRuleTypeDef
```




Optional fields:
- `Cidr`: `str`


## KeyProviderSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import KeyProviderSettingsTypeDef
```




Optional fields:
- `StaticKeySettings`: `"StaticKeySettingsTypeDef"`


## M2tsSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import M2tsSettingsTypeDef
```




Optional fields:
- `AbsentInputAudioBehavior`: `M2tsAbsentInputAudioBehavior`
- `Arib`: `M2tsArib`
- `AribCaptionsPid`: `str`
- `AribCaptionsPidControl`: `M2tsAribCaptionsPidControl`
- `AudioBufferModel`: `M2tsAudioBufferModel`
- `AudioFramesPerPes`: `int`
- `AudioPids`: `str`
- `AudioStreamType`: `M2tsAudioStreamType`
- `Bitrate`: `int`
- `BufferModel`: `M2tsBufferModel`
- `CcDescriptor`: `M2tsCcDescriptor`
- `DvbNitSettings`: `"DvbNitSettingsTypeDef"`
- `DvbSdtSettings`: `"DvbSdtSettingsTypeDef"`
- `DvbSubPids`: `str`
- `DvbTdtSettings`: `"DvbTdtSettingsTypeDef"`
- `DvbTeletextPid`: `str`
- `Ebif`: `M2tsEbifControl`
- `EbpAudioInterval`: `M2tsAudioInterval`
- `EbpLookaheadMs`: `int`
- `EbpPlacement`: `M2tsEbpPlacement`
- `EcmPid`: `str`
- `EsRateInPes`: `M2tsEsRateInPes`
- `EtvPlatformPid`: `str`
- `EtvSignalPid`: `str`
- `FragmentTime`: `float`
- `Klv`: `M2tsKlv`
- `KlvDataPids`: `str`
- `NielsenId3Behavior`: `M2tsNielsenId3Behavior`
- `NullPacketBitrate`: `float`
- `PatInterval`: `int`
- `PcrControl`: `M2tsPcrControl`
- `PcrPeriod`: `int`
- `PcrPid`: `str`
- `PmtInterval`: `int`
- `PmtPid`: `str`
- `ProgramNum`: `int`
- `RateMode`: `M2tsRateMode`
- `Scte27Pids`: `str`
- `Scte35Control`: `M2tsScte35Control`
- `Scte35Pid`: `str`
- `SegmentationMarkers`: `M2tsSegmentationMarkers`
- `SegmentationStyle`: `M2tsSegmentationStyle`
- `SegmentationTime`: `float`
- `TimedMetadataBehavior`: `M2tsTimedMetadataBehavior`
- `TimedMetadataPid`: `str`
- `TransportStreamId`: `int`
- `VideoPid`: `str`


## M3u8SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import M3u8SettingsTypeDef
```




Optional fields:
- `AudioFramesPerPes`: `int`
- `AudioPids`: `str`
- `EcmPid`: `str`
- `NielsenId3Behavior`: `M3u8NielsenId3Behavior`
- `PatInterval`: `int`
- `PcrControl`: `M3u8PcrControl`
- `PcrPeriod`: `int`
- `PcrPid`: `str`
- `PmtInterval`: `int`
- `PmtPid`: `str`
- `ProgramNum`: `int`
- `Scte35Behavior`: `M3u8Scte35Behavior`
- `Scte35Pid`: `str`
- `TimedMetadataBehavior`: `M3u8TimedMetadataBehavior`
- `TimedMetadataPid`: `str`
- `TransportStreamId`: `int`
- `VideoPid`: `str`


## MediaConnectFlowTypeDef

```python
from mypy_boto3_medialive.type_defs import MediaConnectFlowTypeDef
```




Optional fields:
- `FlowArn`: `str`


## MediaPackageGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MediaPackageGroupSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`




## MediaPackageOutputDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MediaPackageOutputDestinationSettingsTypeDef
```




Optional fields:
- `ChannelId`: `str`


## MotionGraphicsActivateScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MotionGraphicsActivateScheduleActionSettingsTypeDef
```




Optional fields:
- `Duration`: `int`
- `PasswordParam`: `str`
- `Url`: `str`
- `Username`: `str`


## MotionGraphicsConfigurationTypeDef

```python
from mypy_boto3_medialive.type_defs import MotionGraphicsConfigurationTypeDef
```


Required fields:
- `MotionGraphicsSettings`: `"MotionGraphicsSettingsTypeDef"`



Optional fields:
- `MotionGraphicsInsertion`: `MotionGraphicsInsertion`


## MotionGraphicsSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MotionGraphicsSettingsTypeDef
```




Optional fields:
- `HtmlMotionGraphicsSettings`: `Dict[str, Any]`


## Mp2SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Mp2SettingsTypeDef
```




Optional fields:
- `Bitrate`: `float`
- `CodingMode`: `Mp2CodingMode`
- `SampleRate`: `float`


## Mpeg2FilterSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Mpeg2FilterSettingsTypeDef
```




Optional fields:
- `TemporalFilterSettings`: `"TemporalFilterSettingsTypeDef"`


## Mpeg2SettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Mpeg2SettingsTypeDef
```


Required fields:
- `FramerateDenominator`: `int`
- `FramerateNumerator`: `int`



Optional fields:
- `AdaptiveQuantization`: `Mpeg2AdaptiveQuantization`
- `AfdSignaling`: `AfdSignaling`
- `ColorMetadata`: `Mpeg2ColorMetadata`
- `ColorSpace`: `Mpeg2ColorSpace`
- `DisplayAspectRatio`: `Mpeg2DisplayRatio`
- `FilterSettings`: `"Mpeg2FilterSettingsTypeDef"`
- `FixedAfd`: `FixedAfd`
- `GopClosedCadence`: `int`
- `GopNumBFrames`: `int`
- `GopSize`: `float`
- `GopSizeUnits`: `Mpeg2GopSizeUnits`
- `ScanType`: `Mpeg2ScanType`
- `SubgopLength`: `Mpeg2SubGopLength`
- `TimecodeInsertion`: `Mpeg2TimecodeInsertionBehavior`


## MsSmoothGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MsSmoothGroupSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`



Optional fields:
- `AcquisitionPointId`: `str`
- `AudioOnlyTimecodeControl`: `SmoothGroupAudioOnlyTimecodeControl`
- `CertificateMode`: `SmoothGroupCertificateMode`
- `ConnectionRetryInterval`: `int`
- `EventId`: `str`
- `EventIdMode`: `SmoothGroupEventIdMode`
- `EventStopBehavior`: `SmoothGroupEventStopBehavior`
- `FilecacheDuration`: `int`
- `FragmentLength`: `int`
- `InputLossAction`: `InputLossActionForMsSmoothOut`
- `NumRetries`: `int`
- `RestartDelay`: `int`
- `SegmentationMode`: `SmoothGroupSegmentationMode`
- `SendDelayMs`: `int`
- `SparseTrackType`: `SmoothGroupSparseTrackType`
- `StreamManifestBehavior`: `SmoothGroupStreamManifestBehavior`
- `TimestampOffset`: `str`
- `TimestampOffsetMode`: `SmoothGroupTimestampOffsetMode`


## MsSmoothOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MsSmoothOutputSettingsTypeDef
```




Optional fields:
- `H265PackagingType`: `MsSmoothH265PackagingType`
- `NameModifier`: `str`


## MultiplexMediaConnectOutputDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexMediaConnectOutputDestinationSettingsTypeDef
```




Optional fields:
- `EntitlementArn`: `str`


## MultiplexOutputDestinationTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexOutputDestinationTypeDef
```




Optional fields:
- `MediaConnectSettings`: `"MultiplexMediaConnectOutputDestinationSettingsTypeDef"`


## MultiplexOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexOutputSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`




## MultiplexProgramChannelDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramChannelDestinationSettingsTypeDef
```




Optional fields:
- `MultiplexId`: `str`
- `ProgramName`: `str`


## MultiplexProgramPacketIdentifiersMapTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramPacketIdentifiersMapTypeDef
```




Optional fields:
- `AudioPids`: `List[int]`
- `DvbSubPids`: `List[int]`
- `DvbTeletextPid`: `int`
- `EtvPlatformPid`: `int`
- `EtvSignalPid`: `int`
- `KlvDataPids`: `List[int]`
- `PcrPid`: `int`
- `PmtPid`: `int`
- `PrivateMetadataPid`: `int`
- `Scte27Pids`: `List[int]`
- `Scte35Pid`: `int`
- `TimedMetadataPid`: `int`
- `VideoPid`: `int`


## MultiplexProgramPipelineDetailTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramPipelineDetailTypeDef
```




Optional fields:
- `ActiveChannelPipeline`: `str`
- `PipelineId`: `str`


## MultiplexProgramServiceDescriptorTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramServiceDescriptorTypeDef
```


Required fields:
- `ProviderName`: `str`
- `ServiceName`: `str`




## MultiplexProgramSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramSettingsTypeDef
```


Required fields:
- `ProgramNumber`: `int`



Optional fields:
- `PreferredChannelPipeline`: `PreferredChannelPipeline`
- `ServiceDescriptor`: `"MultiplexProgramServiceDescriptorTypeDef"`
- `VideoSettings`: `"MultiplexVideoSettingsTypeDef"`


## MultiplexProgramSummaryTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramSummaryTypeDef
```




Optional fields:
- `ChannelId`: `str`
- `ProgramName`: `str`


## MultiplexProgramTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexProgramTypeDef
```




Optional fields:
- `ChannelId`: `str`
- `MultiplexProgramSettings`: `"MultiplexProgramSettingsTypeDef"`
- `PacketIdentifiersMap`: `"MultiplexProgramPacketIdentifiersMapTypeDef"`
- `PipelineDetails`: `List["MultiplexProgramPipelineDetailTypeDef"]`
- `ProgramName`: `str`


## MultiplexSettingsSummaryTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexSettingsSummaryTypeDef
```




Optional fields:
- `TransportStreamBitrate`: `int`


## MultiplexSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexSettingsTypeDef
```


Required fields:
- `TransportStreamBitrate`: `int`
- `TransportStreamId`: `int`



Optional fields:
- `MaximumVideoBufferDelayMilliseconds`: `int`
- `TransportStreamReservedBitrate`: `int`


## MultiplexStatmuxVideoSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexStatmuxVideoSettingsTypeDef
```




Optional fields:
- `MaximumBitrate`: `int`
- `MinimumBitrate`: `int`
- `Priority`: `int`


## MultiplexSummaryTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `AvailabilityZones`: `List[str]`
- `Id`: `str`
- `MultiplexSettings`: `"MultiplexSettingsSummaryTypeDef"`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `ProgramCount`: `int`
- `State`: `MultiplexState`
- `Tags`: `Dict[str, str]`


## MultiplexTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexTypeDef
```




Optional fields:
- `Arn`: `str`
- `AvailabilityZones`: `List[str]`
- `Destinations`: `List["MultiplexOutputDestinationTypeDef"]`
- `Id`: `str`
- `MultiplexSettings`: `"MultiplexSettingsTypeDef"`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `ProgramCount`: `int`
- `State`: `MultiplexState`
- `Tags`: `Dict[str, str]`


## MultiplexVideoSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import MultiplexVideoSettingsTypeDef
```




Optional fields:
- `ConstantBitrate`: `int`
- `StatmuxSettings`: `"MultiplexStatmuxVideoSettingsTypeDef"`


## NetworkInputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import NetworkInputSettingsTypeDef
```




Optional fields:
- `HlsInputSettings`: `"HlsInputSettingsTypeDef"`
- `ServerValidation`: `NetworkInputServerValidation`


## NielsenConfigurationTypeDef

```python
from mypy_boto3_medialive.type_defs import NielsenConfigurationTypeDef
```




Optional fields:
- `DistributorId`: `str`
- `NielsenPcmToId3Tagging`: `NielsenPcmToId3TaggingState`


## OfferingTypeDef

```python
from mypy_boto3_medialive.type_defs import OfferingTypeDef
```




Optional fields:
- `Arn`: `str`
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `OfferingDurationUnits`
- `FixedPrice`: `float`
- `OfferingDescription`: `str`
- `OfferingId`: `str`
- `OfferingType`: `OfferingType`
- `Region`: `str`
- `ResourceSpecification`: `"ReservationResourceSpecificationTypeDef"`
- `UsagePrice`: `float`


## OutputDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputDestinationSettingsTypeDef
```




Optional fields:
- `PasswordParam`: `str`
- `StreamName`: `str`
- `Url`: `str`
- `Username`: `str`


## OutputDestinationTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputDestinationTypeDef
```




Optional fields:
- `Id`: `str`
- `MediaPackageSettings`: `List["MediaPackageOutputDestinationSettingsTypeDef"]`
- `MultiplexSettings`: `"MultiplexProgramChannelDestinationSettingsTypeDef"`
- `Settings`: `List["OutputDestinationSettingsTypeDef"]`


## OutputGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputGroupSettingsTypeDef
```




Optional fields:
- `ArchiveGroupSettings`: `"ArchiveGroupSettingsTypeDef"`
- `FrameCaptureGroupSettings`: `"FrameCaptureGroupSettingsTypeDef"`
- `HlsGroupSettings`: `"HlsGroupSettingsTypeDef"`
- `MediaPackageGroupSettings`: `"MediaPackageGroupSettingsTypeDef"`
- `MsSmoothGroupSettings`: `"MsSmoothGroupSettingsTypeDef"`
- `MultiplexGroupSettings`: `Dict[str, Any]`
- `RtmpGroupSettings`: `"RtmpGroupSettingsTypeDef"`
- `UdpGroupSettings`: `"UdpGroupSettingsTypeDef"`


## OutputGroupTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputGroupTypeDef
```


Required fields:
- `OutputGroupSettings`: `"OutputGroupSettingsTypeDef"`
- `Outputs`: `List["OutputTypeDef"]`



Optional fields:
- `Name`: `str`


## OutputLocationRefTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputLocationRefTypeDef
```




Optional fields:
- `DestinationRefId`: `str`


## OutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputSettingsTypeDef
```




Optional fields:
- `ArchiveOutputSettings`: `"ArchiveOutputSettingsTypeDef"`
- `FrameCaptureOutputSettings`: `"FrameCaptureOutputSettingsTypeDef"`
- `HlsOutputSettings`: `"HlsOutputSettingsTypeDef"`
- `MediaPackageOutputSettings`: `Dict[str, Any]`
- `MsSmoothOutputSettings`: `"MsSmoothOutputSettingsTypeDef"`
- `MultiplexOutputSettings`: `"MultiplexOutputSettingsTypeDef"`
- `RtmpOutputSettings`: `"RtmpOutputSettingsTypeDef"`
- `UdpOutputSettings`: `"UdpOutputSettingsTypeDef"`


## OutputTypeDef

```python
from mypy_boto3_medialive.type_defs import OutputTypeDef
```


Required fields:
- `OutputSettings`: `"OutputSettingsTypeDef"`



Optional fields:
- `AudioDescriptionNames`: `List[str]`
- `CaptionDescriptionNames`: `List[str]`
- `OutputName`: `str`
- `VideoDescriptionName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PauseStateScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import PauseStateScheduleActionSettingsTypeDef
```




Optional fields:
- `Pipelines`: `List["PipelinePauseStateSettingsTypeDef"]`


## PipelineDetailTypeDef

```python
from mypy_boto3_medialive.type_defs import PipelineDetailTypeDef
```




Optional fields:
- `ActiveInputAttachmentName`: `str`
- `ActiveInputSwitchActionName`: `str`
- `ActiveMotionGraphicsActionName`: `str`
- `ActiveMotionGraphicsUri`: `str`
- `PipelineId`: `str`


## PipelinePauseStateSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import PipelinePauseStateSettingsTypeDef
```


Required fields:
- `PipelineId`: `PipelineId`




## RemixSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import RemixSettingsTypeDef
```


Required fields:
- `ChannelMappings`: `List["AudioChannelMappingTypeDef"]`



Optional fields:
- `ChannelsIn`: `int`
- `ChannelsOut`: `int`


## ReservationResourceSpecificationTypeDef

```python
from mypy_boto3_medialive.type_defs import ReservationResourceSpecificationTypeDef
```




Optional fields:
- `ChannelClass`: `ChannelClass`
- `Codec`: `ReservationCodec`
- `MaximumBitrate`: `ReservationMaximumBitrate`
- `MaximumFramerate`: `ReservationMaximumFramerate`
- `Resolution`: `ReservationResolution`
- `ResourceType`: `ReservationResourceType`
- `SpecialFeature`: `ReservationSpecialFeature`
- `VideoQuality`: `ReservationVideoQuality`


## ReservationTypeDef

```python
from mypy_boto3_medialive.type_defs import ReservationTypeDef
```




Optional fields:
- `Arn`: `str`
- `Count`: `int`
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `OfferingDurationUnits`
- `End`: `str`
- `FixedPrice`: `float`
- `Name`: `str`
- `OfferingDescription`: `str`
- `OfferingId`: `str`
- `OfferingType`: `OfferingType`
- `Region`: `str`
- `ReservationId`: `str`
- `ResourceSpecification`: `"ReservationResourceSpecificationTypeDef"`
- `Start`: `str`
- `State`: `ReservationState`
- `Tags`: `Dict[str, str]`
- `UsagePrice`: `float`


## ResponseMetadata

```python
from mypy_boto3_medialive.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RtmpGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import RtmpGroupSettingsTypeDef
```




Optional fields:
- `AdMarkers`: `List[RtmpAdMarkers]`
- `AuthenticationScheme`: `AuthenticationScheme`
- `CacheFullBehavior`: `RtmpCacheFullBehavior`
- `CacheLength`: `int`
- `CaptionData`: `RtmpCaptionData`
- `InputLossAction`: `InputLossActionForRtmpOut`
- `RestartDelay`: `int`


## RtmpOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import RtmpOutputSettingsTypeDef
```


Required fields:
- `Destination`: `"OutputLocationRefTypeDef"`



Optional fields:
- `CertificateMode`: `RtmpOutputCertificateMode`
- `ConnectionRetryInterval`: `int`
- `NumRetries`: `int`


## ScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ScheduleActionSettingsTypeDef
```




Optional fields:
- `HlsId3SegmentTaggingSettings`: `"HlsId3SegmentTaggingScheduleActionSettingsTypeDef"`
- `HlsTimedMetadataSettings`: `"HlsTimedMetadataScheduleActionSettingsTypeDef"`
- `InputPrepareSettings`: `"InputPrepareScheduleActionSettingsTypeDef"`
- `InputSwitchSettings`: `"InputSwitchScheduleActionSettingsTypeDef"`
- `MotionGraphicsImageActivateSettings`: `"MotionGraphicsActivateScheduleActionSettingsTypeDef"`
- `MotionGraphicsImageDeactivateSettings`: `Dict[str, Any]`
- `PauseStateSettings`: `"PauseStateScheduleActionSettingsTypeDef"`
- `Scte35ReturnToNetworkSettings`: `"Scte35ReturnToNetworkScheduleActionSettingsTypeDef"`
- `Scte35SpliceInsertSettings`: `"Scte35SpliceInsertScheduleActionSettingsTypeDef"`
- `Scte35TimeSignalSettings`: `"Scte35TimeSignalScheduleActionSettingsTypeDef"`
- `StaticImageActivateSettings`: `"StaticImageActivateScheduleActionSettingsTypeDef"`
- `StaticImageDeactivateSettings`: `"StaticImageDeactivateScheduleActionSettingsTypeDef"`


## ScheduleActionStartSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import ScheduleActionStartSettingsTypeDef
```




Optional fields:
- `FixedModeScheduleActionStartSettings`: `"FixedModeScheduleActionStartSettingsTypeDef"`
- `FollowModeScheduleActionStartSettings`: `"FollowModeScheduleActionStartSettingsTypeDef"`
- `ImmediateModeScheduleActionStartSettings`: `Dict[str, Any]`


## ScheduleActionTypeDef

```python
from mypy_boto3_medialive.type_defs import ScheduleActionTypeDef
```


Required fields:
- `ActionName`: `str`
- `ScheduleActionSettings`: `"ScheduleActionSettingsTypeDef"`
- `ScheduleActionStartSettings`: `"ScheduleActionStartSettingsTypeDef"`




## Scte20SourceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte20SourceSettingsTypeDef
```




Optional fields:
- `Convert608To708`: `Scte20Convert608To708`
- `Source608ChannelNumber`: `int`


## Scte27SourceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte27SourceSettingsTypeDef
```




Optional fields:
- `Pid`: `int`


## Scte35DeliveryRestrictionsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35DeliveryRestrictionsTypeDef
```


Required fields:
- `ArchiveAllowedFlag`: `Scte35ArchiveAllowedFlag`
- `DeviceRestrictions`: `Scte35DeviceRestrictions`
- `NoRegionalBlackoutFlag`: `Scte35NoRegionalBlackoutFlag`
- `WebDeliveryAllowedFlag`: `Scte35WebDeliveryAllowedFlag`




## Scte35DescriptorSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35DescriptorSettingsTypeDef
```


Required fields:
- `SegmentationDescriptorScte35DescriptorSettings`: `"Scte35SegmentationDescriptorTypeDef"`




## Scte35DescriptorTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35DescriptorTypeDef
```


Required fields:
- `Scte35DescriptorSettings`: `"Scte35DescriptorSettingsTypeDef"`




## Scte35ReturnToNetworkScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35ReturnToNetworkScheduleActionSettingsTypeDef
```


Required fields:
- `SpliceEventId`: `int`




## Scte35SegmentationDescriptorTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35SegmentationDescriptorTypeDef
```


Required fields:
- `SegmentationCancelIndicator`: `Scte35SegmentationCancelIndicator`
- `SegmentationEventId`: `int`



Optional fields:
- `DeliveryRestrictions`: `"Scte35DeliveryRestrictionsTypeDef"`
- `SegmentNum`: `int`
- `SegmentationDuration`: `int`
- `SegmentationTypeId`: `int`
- `SegmentationUpid`: `str`
- `SegmentationUpidType`: `int`
- `SegmentsExpected`: `int`
- `SubSegmentNum`: `int`
- `SubSegmentsExpected`: `int`


## Scte35SpliceInsertScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35SpliceInsertScheduleActionSettingsTypeDef
```


Required fields:
- `SpliceEventId`: `int`



Optional fields:
- `Duration`: `int`


## Scte35SpliceInsertTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35SpliceInsertTypeDef
```




Optional fields:
- `AdAvailOffset`: `int`
- `NoRegionalBlackoutFlag`: `Scte35SpliceInsertNoRegionalBlackoutBehavior`
- `WebDeliveryAllowedFlag`: `Scte35SpliceInsertWebDeliveryAllowedBehavior`


## Scte35TimeSignalAposTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35TimeSignalAposTypeDef
```




Optional fields:
- `AdAvailOffset`: `int`
- `NoRegionalBlackoutFlag`: `Scte35AposNoRegionalBlackoutBehavior`
- `WebDeliveryAllowedFlag`: `Scte35AposWebDeliveryAllowedBehavior`


## Scte35TimeSignalScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import Scte35TimeSignalScheduleActionSettingsTypeDef
```


Required fields:
- `Scte35Descriptors`: `List["Scte35DescriptorTypeDef"]`




## StandardHlsSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import StandardHlsSettingsTypeDef
```


Required fields:
- `M3u8Settings`: `"M3u8SettingsTypeDef"`



Optional fields:
- `AudioRenditionSets`: `str`


## StartTimecodeTypeDef

```python
from mypy_boto3_medialive.type_defs import StartTimecodeTypeDef
```




Optional fields:
- `Timecode`: `str`


## StaticImageActivateScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import StaticImageActivateScheduleActionSettingsTypeDef
```


Required fields:
- `Image`: `"InputLocationTypeDef"`



Optional fields:
- `Duration`: `int`
- `FadeIn`: `int`
- `FadeOut`: `int`
- `Height`: `int`
- `ImageX`: `int`
- `ImageY`: `int`
- `Layer`: `int`
- `Opacity`: `int`
- `Width`: `int`


## StaticImageDeactivateScheduleActionSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import StaticImageDeactivateScheduleActionSettingsTypeDef
```




Optional fields:
- `FadeOut`: `int`
- `Layer`: `int`


## StaticKeySettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import StaticKeySettingsTypeDef
```


Required fields:
- `StaticKeyValue`: `str`



Optional fields:
- `KeyProviderServer`: `"InputLocationTypeDef"`


## StopTimecodeTypeDef

```python
from mypy_boto3_medialive.type_defs import StopTimecodeTypeDef
```




Optional fields:
- `LastFrameClippingBehavior`: `LastFrameClippingBehavior`
- `Timecode`: `str`


## TeletextSourceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import TeletextSourceSettingsTypeDef
```




Optional fields:
- `OutputRectangle`: `"CaptionRectangleTypeDef"`
- `PageNumber`: `str`


## TemporalFilterSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import TemporalFilterSettingsTypeDef
```




Optional fields:
- `PostFilterSharpening`: `TemporalFilterPostFilterSharpening`
- `Strength`: `TemporalFilterStrength`


## TimecodeConfigTypeDef

```python
from mypy_boto3_medialive.type_defs import TimecodeConfigTypeDef
```


Required fields:
- `Source`: `TimecodeConfigSource`



Optional fields:
- `SyncThreshold`: `int`


## TransferringInputDeviceSummaryTypeDef

```python
from mypy_boto3_medialive.type_defs import TransferringInputDeviceSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Message`: `str`
- `TargetCustomerId`: `str`
- `TransferType`: `InputDeviceTransferType`


## TtmlDestinationSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import TtmlDestinationSettingsTypeDef
```




Optional fields:
- `StyleControl`: `TtmlDestinationStyleControl`


## UdpContainerSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import UdpContainerSettingsTypeDef
```




Optional fields:
- `M2tsSettings`: `"M2tsSettingsTypeDef"`


## UdpGroupSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import UdpGroupSettingsTypeDef
```




Optional fields:
- `InputLossAction`: `InputLossActionForUdpOut`
- `TimedMetadataId3Frame`: `UdpTimedMetadataId3Frame`
- `TimedMetadataId3Period`: `int`


## UdpOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import UdpOutputSettingsTypeDef
```


Required fields:
- `ContainerSettings`: `"UdpContainerSettingsTypeDef"`
- `Destination`: `"OutputLocationRefTypeDef"`



Optional fields:
- `BufferMsec`: `int`
- `FecOutputSettings`: `"FecOutputSettingsTypeDef"`


## VideoBlackFailoverSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoBlackFailoverSettingsTypeDef
```




Optional fields:
- `BlackDetectThreshold`: `float`
- `VideoBlackThresholdMsec`: `int`


## VideoCodecSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoCodecSettingsTypeDef
```




Optional fields:
- `FrameCaptureSettings`: `"FrameCaptureSettingsTypeDef"`
- `H264Settings`: `"H264SettingsTypeDef"`
- `H265Settings`: `"H265SettingsTypeDef"`
- `Mpeg2Settings`: `"Mpeg2SettingsTypeDef"`


## VideoDescriptionTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoDescriptionTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CodecSettings`: `"VideoCodecSettingsTypeDef"`
- `Height`: `int`
- `RespondToAfd`: `VideoDescriptionRespondToAfd`
- `ScalingBehavior`: `VideoDescriptionScalingBehavior`
- `Sharpness`: `int`
- `Width`: `int`


## VideoSelectorColorSpaceSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoSelectorColorSpaceSettingsTypeDef
```




Optional fields:
- `Hdr10Settings`: `"Hdr10SettingsTypeDef"`


## VideoSelectorPidTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoSelectorPidTypeDef
```




Optional fields:
- `Pid`: `int`


## VideoSelectorProgramIdTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoSelectorProgramIdTypeDef
```




Optional fields:
- `ProgramId`: `int`


## VideoSelectorSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoSelectorSettingsTypeDef
```




Optional fields:
- `VideoSelectorPid`: `"VideoSelectorPidTypeDef"`
- `VideoSelectorProgramId`: `"VideoSelectorProgramIdTypeDef"`


## VideoSelectorTypeDef

```python
from mypy_boto3_medialive.type_defs import VideoSelectorTypeDef
```




Optional fields:
- `ColorSpace`: `VideoSelectorColorSpace`
- `ColorSpaceSettings`: `"VideoSelectorColorSpaceSettingsTypeDef"`
- `ColorSpaceUsage`: `VideoSelectorColorSpaceUsage`
- `SelectorSettings`: `"VideoSelectorSettingsTypeDef"`


## VpcOutputSettingsDescriptionTypeDef

```python
from mypy_boto3_medialive.type_defs import VpcOutputSettingsDescriptionTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `NetworkInterfaceIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`
- `SubnetIds`: `List[str]`


## WavSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import WavSettingsTypeDef
```




Optional fields:
- `BitDepth`: `float`
- `CodingMode`: `WavCodingMode`
- `SampleRate`: `float`


## BatchDeleteResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchDeleteResponseTypeDef
```




Optional fields:
- `Failed`: `List["BatchFailedResultModelTypeDef"]`
- `Successful`: `List["BatchSuccessfulResultModelTypeDef"]`


## BatchScheduleActionCreateRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchScheduleActionCreateRequestTypeDef
```


Required fields:
- `ScheduleActions`: `List["ScheduleActionTypeDef"]`




## BatchScheduleActionDeleteRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchScheduleActionDeleteRequestTypeDef
```


Required fields:
- `ActionNames`: `List[str]`




## BatchStartResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchStartResponseTypeDef
```




Optional fields:
- `Failed`: `List["BatchFailedResultModelTypeDef"]`
- `Successful`: `List["BatchSuccessfulResultModelTypeDef"]`


## BatchStopResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchStopResponseTypeDef
```




Optional fields:
- `Failed`: `List["BatchFailedResultModelTypeDef"]`
- `Successful`: `List["BatchSuccessfulResultModelTypeDef"]`


## BatchUpdateScheduleResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import BatchUpdateScheduleResponseTypeDef
```




Optional fields:
- `Creates`: `"BatchScheduleActionCreateResultTypeDef"`
- `Deletes`: `"BatchScheduleActionDeleteResultTypeDef"`


## CreateChannelResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import CreateChannelResponseTypeDef
```




Optional fields:
- `Channel`: `"ChannelTypeDef"`


## CreateInputResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import CreateInputResponseTypeDef
```




Optional fields:
- `Input`: `"InputTypeDef"`


## CreateInputSecurityGroupResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import CreateInputSecurityGroupResponseTypeDef
```




Optional fields:
- `SecurityGroup`: `"InputSecurityGroupTypeDef"`


## CreateMultiplexProgramResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import CreateMultiplexProgramResponseTypeDef
```




Optional fields:
- `MultiplexProgram`: `"MultiplexProgramTypeDef"`


## CreateMultiplexResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import CreateMultiplexResponseTypeDef
```




Optional fields:
- `Multiplex`: `"MultiplexTypeDef"`


## CreatePartnerInputResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import CreatePartnerInputResponseTypeDef
```




Optional fields:
- `Input`: `"InputTypeDef"`


## DeleteChannelResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DeleteChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CdiInputSpecification`: `"CdiInputSpecificationTypeDef"`
- `ChannelClass`: `ChannelClass`
- `Destinations`: `List["OutputDestinationTypeDef"]`
- `EgressEndpoints`: `List["ChannelEgressEndpointTypeDef"]`
- `EncoderSettings`: `"EncoderSettingsTypeDef"`
- `Id`: `str`
- `InputAttachments`: `List["InputAttachmentTypeDef"]`
- `InputSpecification`: `"InputSpecificationTypeDef"`
- `LogLevel`: `LogLevel`
- `Name`: `str`
- `PipelineDetails`: `List["PipelineDetailTypeDef"]`
- `PipelinesRunningCount`: `int`
- `RoleArn`: `str`
- `State`: `ChannelState`
- `Tags`: `Dict[str, str]`
- `Vpc`: `"VpcOutputSettingsDescriptionTypeDef"`


## DeleteMultiplexProgramResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DeleteMultiplexProgramResponseTypeDef
```




Optional fields:
- `ChannelId`: `str`
- `MultiplexProgramSettings`: `"MultiplexProgramSettingsTypeDef"`
- `PacketIdentifiersMap`: `"MultiplexProgramPacketIdentifiersMapTypeDef"`
- `PipelineDetails`: `List["MultiplexProgramPipelineDetailTypeDef"]`
- `ProgramName`: `str`


## DeleteMultiplexResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DeleteMultiplexResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AvailabilityZones`: `List[str]`
- `Destinations`: `List["MultiplexOutputDestinationTypeDef"]`
- `Id`: `str`
- `MultiplexSettings`: `"MultiplexSettingsTypeDef"`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `ProgramCount`: `int`
- `State`: `MultiplexState`
- `Tags`: `Dict[str, str]`


## DeleteReservationResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DeleteReservationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Count`: `int`
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `OfferingDurationUnits`
- `End`: `str`
- `FixedPrice`: `float`
- `Name`: `str`
- `OfferingDescription`: `str`
- `OfferingId`: `str`
- `OfferingType`: `OfferingType`
- `Region`: `str`
- `ReservationId`: `str`
- `ResourceSpecification`: `"ReservationResourceSpecificationTypeDef"`
- `Start`: `str`
- `State`: `ReservationState`
- `Tags`: `Dict[str, str]`
- `UsagePrice`: `float`


## DescribeChannelResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CdiInputSpecification`: `"CdiInputSpecificationTypeDef"`
- `ChannelClass`: `ChannelClass`
- `Destinations`: `List["OutputDestinationTypeDef"]`
- `EgressEndpoints`: `List["ChannelEgressEndpointTypeDef"]`
- `EncoderSettings`: `"EncoderSettingsTypeDef"`
- `Id`: `str`
- `InputAttachments`: `List["InputAttachmentTypeDef"]`
- `InputSpecification`: `"InputSpecificationTypeDef"`
- `LogLevel`: `LogLevel`
- `Name`: `str`
- `PipelineDetails`: `List["PipelineDetailTypeDef"]`
- `PipelinesRunningCount`: `int`
- `RoleArn`: `str`
- `State`: `ChannelState`
- `Tags`: `Dict[str, str]`
- `Vpc`: `"VpcOutputSettingsDescriptionTypeDef"`


## DescribeInputDeviceResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeInputDeviceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `ConnectionState`: `InputDeviceConnectionState`
- `DeviceSettingsSyncState`: `DeviceSettingsSyncState`
- `DeviceUpdateStatus`: `DeviceUpdateStatus`
- `HdDeviceSettings`: `"InputDeviceHdSettingsTypeDef"`
- `Id`: `str`
- `MacAddress`: `str`
- `Name`: `str`
- `NetworkSettings`: `"InputDeviceNetworkSettingsTypeDef"`
- `SerialNumber`: `str`
- `Type`: `InputDeviceType`
- `UhdDeviceSettings`: `"InputDeviceUhdSettingsTypeDef"`


## DescribeInputDeviceThumbnailResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeInputDeviceThumbnailResponseTypeDef
```




Optional fields:
- `Body`: `StreamingBody`
- `ContentType`: `ContentType`
- `ContentLength`: `int`
- `ETag`: `str`
- `LastModified`: `datetime`


## DescribeInputResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeInputResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AttachedChannels`: `List[str]`
- `Destinations`: `List["InputDestinationTypeDef"]`
- `Id`: `str`
- `InputClass`: `InputClass`
- `InputDevices`: `List["InputDeviceSettingsTypeDef"]`
- `InputPartnerIds`: `List[str]`
- `InputSourceType`: `InputSourceType`
- `MediaConnectFlows`: `List["MediaConnectFlowTypeDef"]`
- `Name`: `str`
- `RoleArn`: `str`
- `SecurityGroups`: `List[str]`
- `Sources`: `List["InputSourceTypeDef"]`
- `State`: `InputState`
- `Tags`: `Dict[str, str]`
- `Type`: `InputType`


## DescribeInputSecurityGroupResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeInputSecurityGroupResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Id`: `str`
- `Inputs`: `List[str]`
- `State`: `InputSecurityGroupState`
- `Tags`: `Dict[str, str]`
- `WhitelistRules`: `List["InputWhitelistRuleTypeDef"]`


## DescribeMultiplexProgramResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeMultiplexProgramResponseTypeDef
```




Optional fields:
- `ChannelId`: `str`
- `MultiplexProgramSettings`: `"MultiplexProgramSettingsTypeDef"`
- `PacketIdentifiersMap`: `"MultiplexProgramPacketIdentifiersMapTypeDef"`
- `PipelineDetails`: `List["MultiplexProgramPipelineDetailTypeDef"]`
- `ProgramName`: `str`


## DescribeMultiplexResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeMultiplexResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AvailabilityZones`: `List[str]`
- `Destinations`: `List["MultiplexOutputDestinationTypeDef"]`
- `Id`: `str`
- `MultiplexSettings`: `"MultiplexSettingsTypeDef"`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `ProgramCount`: `int`
- `State`: `MultiplexState`
- `Tags`: `Dict[str, str]`


## DescribeOfferingResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeOfferingResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `OfferingDurationUnits`
- `FixedPrice`: `float`
- `OfferingDescription`: `str`
- `OfferingId`: `str`
- `OfferingType`: `OfferingType`
- `Region`: `str`
- `ResourceSpecification`: `"ReservationResourceSpecificationTypeDef"`
- `UsagePrice`: `float`


## DescribeReservationResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeReservationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Count`: `int`
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `OfferingDurationUnits`
- `End`: `str`
- `FixedPrice`: `float`
- `Name`: `str`
- `OfferingDescription`: `str`
- `OfferingId`: `str`
- `OfferingType`: `OfferingType`
- `Region`: `str`
- `ReservationId`: `str`
- `ResourceSpecification`: `"ReservationResourceSpecificationTypeDef"`
- `Start`: `str`
- `State`: `ReservationState`
- `Tags`: `Dict[str, str]`
- `UsagePrice`: `float`


## DescribeScheduleResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import DescribeScheduleResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ScheduleActions`: `List["ScheduleActionTypeDef"]`


## InputDestinationRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDestinationRequestTypeDef
```




Optional fields:
- `StreamName`: `str`


## InputDeviceConfigurableSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceConfigurableSettingsTypeDef
```




Optional fields:
- `ConfiguredInput`: `InputDeviceConfiguredInput`
- `MaxBitrate`: `int`


## InputDeviceRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import InputDeviceRequestTypeDef
```




Optional fields:
- `Id`: `str`


## InputSourceRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import InputSourceRequestTypeDef
```




Optional fields:
- `PasswordParam`: `str`
- `Url`: `str`
- `Username`: `str`


## InputVpcRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import InputVpcRequestTypeDef
```


Required fields:
- `SubnetIds`: `List[str]`



Optional fields:
- `SecurityGroupIds`: `List[str]`


## InputWhitelistRuleCidrTypeDef

```python
from mypy_boto3_medialive.type_defs import InputWhitelistRuleCidrTypeDef
```




Optional fields:
- `Cidr`: `str`


## ListChannelsResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListChannelsResponseTypeDef
```




Optional fields:
- `Channels`: `List["ChannelSummaryTypeDef"]`
- `NextToken`: `str`


## ListInputDeviceTransfersResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListInputDeviceTransfersResponseTypeDef
```




Optional fields:
- `InputDeviceTransfers`: `List["TransferringInputDeviceSummaryTypeDef"]`
- `NextToken`: `str`


## ListInputDevicesResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListInputDevicesResponseTypeDef
```




Optional fields:
- `InputDevices`: `List["InputDeviceSummaryTypeDef"]`
- `NextToken`: `str`


## ListInputSecurityGroupsResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListInputSecurityGroupsResponseTypeDef
```




Optional fields:
- `InputSecurityGroups`: `List["InputSecurityGroupTypeDef"]`
- `NextToken`: `str`


## ListInputsResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListInputsResponseTypeDef
```




Optional fields:
- `Inputs`: `List["InputTypeDef"]`
- `NextToken`: `str`


## ListMultiplexProgramsResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListMultiplexProgramsResponseTypeDef
```




Optional fields:
- `MultiplexPrograms`: `List["MultiplexProgramSummaryTypeDef"]`
- `NextToken`: `str`


## ListMultiplexesResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListMultiplexesResponseTypeDef
```




Optional fields:
- `Multiplexes`: `List["MultiplexSummaryTypeDef"]`
- `NextToken`: `str`


## ListOfferingsResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListOfferingsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Offerings`: `List["OfferingTypeDef"]`


## ListReservationsResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListReservationsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Reservations`: `List["ReservationTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## MediaConnectFlowRequestTypeDef

```python
from mypy_boto3_medialive.type_defs import MediaConnectFlowRequestTypeDef
```




Optional fields:
- `FlowArn`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_medialive.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PurchaseOfferingResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import PurchaseOfferingResponseTypeDef
```




Optional fields:
- `Reservation`: `"ReservationTypeDef"`


## StartChannelResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import StartChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CdiInputSpecification`: `"CdiInputSpecificationTypeDef"`
- `ChannelClass`: `ChannelClass`
- `Destinations`: `List["OutputDestinationTypeDef"]`
- `EgressEndpoints`: `List["ChannelEgressEndpointTypeDef"]`
- `EncoderSettings`: `"EncoderSettingsTypeDef"`
- `Id`: `str`
- `InputAttachments`: `List["InputAttachmentTypeDef"]`
- `InputSpecification`: `"InputSpecificationTypeDef"`
- `LogLevel`: `LogLevel`
- `Name`: `str`
- `PipelineDetails`: `List["PipelineDetailTypeDef"]`
- `PipelinesRunningCount`: `int`
- `RoleArn`: `str`
- `State`: `ChannelState`
- `Tags`: `Dict[str, str]`
- `Vpc`: `"VpcOutputSettingsDescriptionTypeDef"`


## StartMultiplexResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import StartMultiplexResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AvailabilityZones`: `List[str]`
- `Destinations`: `List["MultiplexOutputDestinationTypeDef"]`
- `Id`: `str`
- `MultiplexSettings`: `"MultiplexSettingsTypeDef"`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `ProgramCount`: `int`
- `State`: `MultiplexState`
- `Tags`: `Dict[str, str]`


## StopChannelResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import StopChannelResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CdiInputSpecification`: `"CdiInputSpecificationTypeDef"`
- `ChannelClass`: `ChannelClass`
- `Destinations`: `List["OutputDestinationTypeDef"]`
- `EgressEndpoints`: `List["ChannelEgressEndpointTypeDef"]`
- `EncoderSettings`: `"EncoderSettingsTypeDef"`
- `Id`: `str`
- `InputAttachments`: `List["InputAttachmentTypeDef"]`
- `InputSpecification`: `"InputSpecificationTypeDef"`
- `LogLevel`: `LogLevel`
- `Name`: `str`
- `PipelineDetails`: `List["PipelineDetailTypeDef"]`
- `PipelinesRunningCount`: `int`
- `RoleArn`: `str`
- `State`: `ChannelState`
- `Tags`: `Dict[str, str]`
- `Vpc`: `"VpcOutputSettingsDescriptionTypeDef"`


## StopMultiplexResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import StopMultiplexResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AvailabilityZones`: `List[str]`
- `Destinations`: `List["MultiplexOutputDestinationTypeDef"]`
- `Id`: `str`
- `MultiplexSettings`: `"MultiplexSettingsTypeDef"`
- `Name`: `str`
- `PipelinesRunningCount`: `int`
- `ProgramCount`: `int`
- `State`: `MultiplexState`
- `Tags`: `Dict[str, str]`


## UpdateChannelClassResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateChannelClassResponseTypeDef
```




Optional fields:
- `Channel`: `"ChannelTypeDef"`


## UpdateChannelResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateChannelResponseTypeDef
```




Optional fields:
- `Channel`: `"ChannelTypeDef"`


## UpdateInputDeviceResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateInputDeviceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `ConnectionState`: `InputDeviceConnectionState`
- `DeviceSettingsSyncState`: `DeviceSettingsSyncState`
- `DeviceUpdateStatus`: `DeviceUpdateStatus`
- `HdDeviceSettings`: `"InputDeviceHdSettingsTypeDef"`
- `Id`: `str`
- `MacAddress`: `str`
- `Name`: `str`
- `NetworkSettings`: `"InputDeviceNetworkSettingsTypeDef"`
- `SerialNumber`: `str`
- `Type`: `InputDeviceType`
- `UhdDeviceSettings`: `"InputDeviceUhdSettingsTypeDef"`


## UpdateInputResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateInputResponseTypeDef
```




Optional fields:
- `Input`: `"InputTypeDef"`


## UpdateInputSecurityGroupResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateInputSecurityGroupResponseTypeDef
```




Optional fields:
- `SecurityGroup`: `"InputSecurityGroupTypeDef"`


## UpdateMultiplexProgramResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateMultiplexProgramResponseTypeDef
```




Optional fields:
- `MultiplexProgram`: `"MultiplexProgramTypeDef"`


## UpdateMultiplexResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateMultiplexResponseTypeDef
```




Optional fields:
- `Multiplex`: `"MultiplexTypeDef"`


## UpdateReservationResponseTypeDef

```python
from mypy_boto3_medialive.type_defs import UpdateReservationResponseTypeDef
```




Optional fields:
- `Reservation`: `"ReservationTypeDef"`


## VpcOutputSettingsTypeDef

```python
from mypy_boto3_medialive.type_defs import VpcOutputSettingsTypeDef
```


Required fields:
- `SubnetIds`: `List[str]`



Optional fields:
- `PublicAddressAllocationIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`


## WaiterConfigTypeDef

```python
from mypy_boto3_medialive.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

