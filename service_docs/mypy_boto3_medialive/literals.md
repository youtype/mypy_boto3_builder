# Literals for boto3 MediaLive module

> [Index](../index.md) > [MediaLive](./index.md) > Literals

Auto-generated documentation for [MediaLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive)
type annotations stubs module [mypy_boto3_medialive](https://pypi.org/project/mypy-boto3-medialive/).

- [Literals for boto3 MediaLive module](#literals-for-boto3-medialive-module)
  - [AacCodingMode](#aaccodingmode)
  - [AacInputType](#aacinputtype)
  - [AacProfile](#aacprofile)
  - [AacRateControlMode](#aacratecontrolmode)
  - [AacRawFormat](#aacrawformat)
  - [AacSpec](#aacspec)
  - [AacVbrQuality](#aacvbrquality)
  - [Ac3BitstreamMode](#ac3bitstreammode)
  - [Ac3CodingMode](#ac3codingmode)
  - [Ac3DrcProfile](#ac3drcprofile)
  - [Ac3LfeFilter](#ac3lfefilter)
  - [Ac3MetadataControl](#ac3metadatacontrol)
  - [AcceptHeader](#acceptheader)
  - [AfdSignaling](#afdsignaling)
  - [AudioDescriptionAudioTypeControl](#audiodescriptionaudiotypecontrol)
  - [AudioDescriptionLanguageCodeControl](#audiodescriptionlanguagecodecontrol)
  - [AudioLanguageSelectionPolicy](#audiolanguageselectionpolicy)
  - [AudioNormalizationAlgorithm](#audionormalizationalgorithm)
  - [AudioNormalizationAlgorithmControl](#audionormalizationalgorithmcontrol)
  - [AudioOnlyHlsSegmentType](#audioonlyhlssegmenttype)
  - [AudioOnlyHlsTrackType](#audioonlyhlstracktype)
  - [AudioType](#audiotype)
  - [AuthenticationScheme](#authenticationscheme)
  - [AvailBlankingState](#availblankingstate)
  - [BlackoutSlateNetworkEndBlackout](#blackoutslatenetworkendblackout)
  - [BlackoutSlateState](#blackoutslatestate)
  - [BurnInAlignment](#burninalignment)
  - [BurnInBackgroundColor](#burninbackgroundcolor)
  - [BurnInFontColor](#burninfontcolor)
  - [BurnInOutlineColor](#burninoutlinecolor)
  - [BurnInShadowColor](#burninshadowcolor)
  - [BurnInTeletextGridControl](#burninteletextgridcontrol)
  - [CdiInputResolution](#cdiinputresolution)
  - [ChannelClass](#channelclass)
  - [ChannelCreatedWaiterName](#channelcreatedwaitername)
  - [ChannelDeletedWaiterName](#channeldeletedwaitername)
  - [ChannelRunningWaiterName](#channelrunningwaitername)
  - [ChannelState](#channelstate)
  - [ChannelStoppedWaiterName](#channelstoppedwaitername)
  - [ContentType](#contenttype)
  - [DescribeSchedulePaginatorName](#describeschedulepaginatorname)
  - [DeviceSettingsSyncState](#devicesettingssyncstate)
  - [DeviceUpdateStatus](#deviceupdatestatus)
  - [DvbSdtOutputSdt](#dvbsdtoutputsdt)
  - [DvbSubDestinationAlignment](#dvbsubdestinationalignment)
  - [DvbSubDestinationBackgroundColor](#dvbsubdestinationbackgroundcolor)
  - [DvbSubDestinationFontColor](#dvbsubdestinationfontcolor)
  - [DvbSubDestinationOutlineColor](#dvbsubdestinationoutlinecolor)
  - [DvbSubDestinationShadowColor](#dvbsubdestinationshadowcolor)
  - [DvbSubDestinationTeletextGridControl](#dvbsubdestinationteletextgridcontrol)
  - [Eac3AttenuationControl](#eac3attenuationcontrol)
  - [Eac3BitstreamMode](#eac3bitstreammode)
  - [Eac3CodingMode](#eac3codingmode)
  - [Eac3DcFilter](#eac3dcfilter)
  - [Eac3DrcLine](#eac3drcline)
  - [Eac3DrcRf](#eac3drcrf)
  - [Eac3LfeControl](#eac3lfecontrol)
  - [Eac3LfeFilter](#eac3lfefilter)
  - [Eac3MetadataControl](#eac3metadatacontrol)
  - [Eac3PassthroughControl](#eac3passthroughcontrol)
  - [Eac3PhaseControl](#eac3phasecontrol)
  - [Eac3StereoDownmix](#eac3stereodownmix)
  - [Eac3SurroundExMode](#eac3surroundexmode)
  - [Eac3SurroundMode](#eac3surroundmode)
  - [EbuTtDDestinationStyleControl](#ebuttddestinationstylecontrol)
  - [EbuTtDFillLineGapControl](#ebuttdfilllinegapcontrol)
  - [EmbeddedConvert608To708](#embeddedconvert608to708)
  - [EmbeddedScte20Detection](#embeddedscte20detection)
  - [FeatureActivationsInputPrepareScheduleActions](#featureactivationsinputpreparescheduleactions)
  - [FecOutputIncludeFec](#fecoutputincludefec)
  - [FixedAfd](#fixedafd)
  - [Fmp4NielsenId3Behavior](#fmp4nielsenid3behavior)
  - [Fmp4TimedMetadataBehavior](#fmp4timedmetadatabehavior)
  - [FollowPoint](#followpoint)
  - [FrameCaptureIntervalUnit](#framecaptureintervalunit)
  - [GlobalConfigurationInputEndAction](#globalconfigurationinputendaction)
  - [GlobalConfigurationLowFramerateInputs](#globalconfigurationlowframerateinputs)
  - [GlobalConfigurationOutputLockingMode](#globalconfigurationoutputlockingmode)
  - [GlobalConfigurationOutputTimingSource](#globalconfigurationoutputtimingsource)
  - [H264AdaptiveQuantization](#h264adaptivequantization)
  - [H264ColorMetadata](#h264colormetadata)
  - [H264EntropyEncoding](#h264entropyencoding)
  - [H264FlickerAq](#h264flickeraq)
  - [H264ForceFieldPictures](#h264forcefieldpictures)
  - [H264FramerateControl](#h264frameratecontrol)
  - [H264GopBReference](#h264gopbreference)
  - [H264GopSizeUnits](#h264gopsizeunits)
  - [H264Level](#h264level)
  - [H264LookAheadRateControl](#h264lookaheadratecontrol)
  - [H264ParControl](#h264parcontrol)
  - [H264Profile](#h264profile)
  - [H264QualityLevel](#h264qualitylevel)
  - [H264RateControlMode](#h264ratecontrolmode)
  - [H264ScanType](#h264scantype)
  - [H264SceneChangeDetect](#h264scenechangedetect)
  - [H264SpatialAq](#h264spatialaq)
  - [H264SubGopLength](#h264subgoplength)
  - [H264Syntax](#h264syntax)
  - [H264TemporalAq](#h264temporalaq)
  - [H264TimecodeInsertionBehavior](#h264timecodeinsertionbehavior)
  - [H265AdaptiveQuantization](#h265adaptivequantization)
  - [H265AlternativeTransferFunction](#h265alternativetransferfunction)
  - [H265ColorMetadata](#h265colormetadata)
  - [H265FlickerAq](#h265flickeraq)
  - [H265GopSizeUnits](#h265gopsizeunits)
  - [H265Level](#h265level)
  - [H265LookAheadRateControl](#h265lookaheadratecontrol)
  - [H265Profile](#h265profile)
  - [H265RateControlMode](#h265ratecontrolmode)
  - [H265ScanType](#h265scantype)
  - [H265SceneChangeDetect](#h265scenechangedetect)
  - [H265Tier](#h265tier)
  - [H265TimecodeInsertionBehavior](#h265timecodeinsertionbehavior)
  - [HlsAdMarkers](#hlsadmarkers)
  - [HlsAkamaiHttpTransferMode](#hlsakamaihttptransfermode)
  - [HlsCaptionLanguageSetting](#hlscaptionlanguagesetting)
  - [HlsClientCache](#hlsclientcache)
  - [HlsCodecSpecification](#hlscodecspecification)
  - [HlsDirectoryStructure](#hlsdirectorystructure)
  - [HlsDiscontinuityTags](#hlsdiscontinuitytags)
  - [HlsEncryptionType](#hlsencryptiontype)
  - [HlsH265PackagingType](#hlsh265packagingtype)
  - [HlsId3SegmentTaggingState](#hlsid3segmenttaggingstate)
  - [HlsIncompleteSegmentBehavior](#hlsincompletesegmentbehavior)
  - [HlsIvInManifest](#hlsivinmanifest)
  - [HlsIvSource](#hlsivsource)
  - [HlsManifestCompression](#hlsmanifestcompression)
  - [HlsManifestDurationFormat](#hlsmanifestdurationformat)
  - [HlsMediaStoreStorageClass](#hlsmediastorestorageclass)
  - [HlsMode](#hlsmode)
  - [HlsOutputSelection](#hlsoutputselection)
  - [HlsProgramDateTime](#hlsprogramdatetime)
  - [HlsRedundantManifest](#hlsredundantmanifest)
  - [HlsSegmentationMode](#hlssegmentationmode)
  - [HlsStreamInfResolution](#hlsstreaminfresolution)
  - [HlsTimedMetadataId3Frame](#hlstimedmetadataid3frame)
  - [HlsTsFileMode](#hlstsfilemode)
  - [HlsWebdavHttpTransferMode](#hlswebdavhttptransfermode)
  - [IFrameOnlyPlaylistType](#iframeonlyplaylisttype)
  - [InputAttachedWaiterName](#inputattachedwaitername)
  - [InputClass](#inputclass)
  - [InputCodec](#inputcodec)
  - [InputDeblockFilter](#inputdeblockfilter)
  - [InputDeletedWaiterName](#inputdeletedwaitername)
  - [InputDenoiseFilter](#inputdenoisefilter)
  - [InputDetachedWaiterName](#inputdetachedwaitername)
  - [InputDeviceActiveInput](#inputdeviceactiveinput)
  - [InputDeviceConfiguredInput](#inputdeviceconfiguredinput)
  - [InputDeviceConnectionState](#inputdeviceconnectionstate)
  - [InputDeviceIpScheme](#inputdeviceipscheme)
  - [InputDeviceScanType](#inputdevicescantype)
  - [InputDeviceState](#inputdevicestate)
  - [InputDeviceTransferType](#inputdevicetransfertype)
  - [InputDeviceType](#inputdevicetype)
  - [InputFilter](#inputfilter)
  - [InputLossActionForHlsOut](#inputlossactionforhlsout)
  - [InputLossActionForMsSmoothOut](#inputlossactionformssmoothout)
  - [InputLossActionForRtmpOut](#inputlossactionforrtmpout)
  - [InputLossActionForUdpOut](#inputlossactionforudpout)
  - [InputLossImageType](#inputlossimagetype)
  - [InputMaximumBitrate](#inputmaximumbitrate)
  - [InputPreference](#inputpreference)
  - [InputResolution](#inputresolution)
  - [InputSecurityGroupState](#inputsecuritygroupstate)
  - [InputSourceEndBehavior](#inputsourceendbehavior)
  - [InputSourceType](#inputsourcetype)
  - [InputState](#inputstate)
  - [InputTimecodeSource](#inputtimecodesource)
  - [InputType](#inputtype)
  - [LastFrameClippingBehavior](#lastframeclippingbehavior)
  - [ListChannelsPaginatorName](#listchannelspaginatorname)
  - [ListInputDeviceTransfersPaginatorName](#listinputdevicetransferspaginatorname)
  - [ListInputDevicesPaginatorName](#listinputdevicespaginatorname)
  - [ListInputSecurityGroupsPaginatorName](#listinputsecuritygroupspaginatorname)
  - [ListInputsPaginatorName](#listinputspaginatorname)
  - [ListMultiplexProgramsPaginatorName](#listmultiplexprogramspaginatorname)
  - [ListMultiplexesPaginatorName](#listmultiplexespaginatorname)
  - [ListOfferingsPaginatorName](#listofferingspaginatorname)
  - [ListReservationsPaginatorName](#listreservationspaginatorname)
  - [LogLevel](#loglevel)
  - [M2tsAbsentInputAudioBehavior](#m2tsabsentinputaudiobehavior)
  - [M2tsArib](#m2tsarib)
  - [M2tsAribCaptionsPidControl](#m2tsaribcaptionspidcontrol)
  - [M2tsAudioBufferModel](#m2tsaudiobuffermodel)
  - [M2tsAudioInterval](#m2tsaudiointerval)
  - [M2tsAudioStreamType](#m2tsaudiostreamtype)
  - [M2tsBufferModel](#m2tsbuffermodel)
  - [M2tsCcDescriptor](#m2tsccdescriptor)
  - [M2tsEbifControl](#m2tsebifcontrol)
  - [M2tsEbpPlacement](#m2tsebpplacement)
  - [M2tsEsRateInPes](#m2tsesrateinpes)
  - [M2tsKlv](#m2tsklv)
  - [M2tsNielsenId3Behavior](#m2tsnielsenid3behavior)
  - [M2tsPcrControl](#m2tspcrcontrol)
  - [M2tsRateMode](#m2tsratemode)
  - [M2tsScte35Control](#m2tsscte35control)
  - [M2tsSegmentationMarkers](#m2tssegmentationmarkers)
  - [M2tsSegmentationStyle](#m2tssegmentationstyle)
  - [M2tsTimedMetadataBehavior](#m2tstimedmetadatabehavior)
  - [M3u8NielsenId3Behavior](#m3u8nielsenid3behavior)
  - [M3u8PcrControl](#m3u8pcrcontrol)
  - [M3u8Scte35Behavior](#m3u8scte35behavior)
  - [M3u8TimedMetadataBehavior](#m3u8timedmetadatabehavior)
  - [MotionGraphicsInsertion](#motiongraphicsinsertion)
  - [Mp2CodingMode](#mp2codingmode)
  - [Mpeg2AdaptiveQuantization](#mpeg2adaptivequantization)
  - [Mpeg2ColorMetadata](#mpeg2colormetadata)
  - [Mpeg2ColorSpace](#mpeg2colorspace)
  - [Mpeg2DisplayRatio](#mpeg2displayratio)
  - [Mpeg2GopSizeUnits](#mpeg2gopsizeunits)
  - [Mpeg2ScanType](#mpeg2scantype)
  - [Mpeg2SubGopLength](#mpeg2subgoplength)
  - [Mpeg2TimecodeInsertionBehavior](#mpeg2timecodeinsertionbehavior)
  - [MsSmoothH265PackagingType](#mssmoothh265packagingtype)
  - [MultiplexCreatedWaiterName](#multiplexcreatedwaitername)
  - [MultiplexDeletedWaiterName](#multiplexdeletedwaitername)
  - [MultiplexRunningWaiterName](#multiplexrunningwaitername)
  - [MultiplexState](#multiplexstate)
  - [MultiplexStoppedWaiterName](#multiplexstoppedwaitername)
  - [NetworkInputServerValidation](#networkinputservervalidation)
  - [NielsenPcmToId3TaggingState](#nielsenpcmtoid3taggingstate)
  - [OfferingDurationUnits](#offeringdurationunits)
  - [OfferingType](#offeringtype)
  - [PipelineId](#pipelineid)
  - [PreferredChannelPipeline](#preferredchannelpipeline)
  - [ReservationCodec](#reservationcodec)
  - [ReservationMaximumBitrate](#reservationmaximumbitrate)
  - [ReservationMaximumFramerate](#reservationmaximumframerate)
  - [ReservationResolution](#reservationresolution)
  - [ReservationResourceType](#reservationresourcetype)
  - [ReservationSpecialFeature](#reservationspecialfeature)
  - [ReservationState](#reservationstate)
  - [ReservationVideoQuality](#reservationvideoquality)
  - [RtmpAdMarkers](#rtmpadmarkers)
  - [RtmpCacheFullBehavior](#rtmpcachefullbehavior)
  - [RtmpCaptionData](#rtmpcaptiondata)
  - [RtmpOutputCertificateMode](#rtmpoutputcertificatemode)
  - [S3CannedAcl](#s3cannedacl)
  - [Scte20Convert608To708](#scte20convert608to708)
  - [Scte35AposNoRegionalBlackoutBehavior](#scte35aposnoregionalblackoutbehavior)
  - [Scte35AposWebDeliveryAllowedBehavior](#scte35aposwebdeliveryallowedbehavior)
  - [Scte35ArchiveAllowedFlag](#scte35archiveallowedflag)
  - [Scte35DeviceRestrictions](#scte35devicerestrictions)
  - [Scte35NoRegionalBlackoutFlag](#scte35noregionalblackoutflag)
  - [Scte35SegmentationCancelIndicator](#scte35segmentationcancelindicator)
  - [Scte35SpliceInsertNoRegionalBlackoutBehavior](#scte35spliceinsertnoregionalblackoutbehavior)
  - [Scte35SpliceInsertWebDeliveryAllowedBehavior](#scte35spliceinsertwebdeliveryallowedbehavior)
  - [Scte35WebDeliveryAllowedFlag](#scte35webdeliveryallowedflag)
  - [SmoothGroupAudioOnlyTimecodeControl](#smoothgroupaudioonlytimecodecontrol)
  - [SmoothGroupCertificateMode](#smoothgroupcertificatemode)
  - [SmoothGroupEventIdMode](#smoothgroupeventidmode)
  - [SmoothGroupEventStopBehavior](#smoothgroupeventstopbehavior)
  - [SmoothGroupSegmentationMode](#smoothgroupsegmentationmode)
  - [SmoothGroupSparseTrackType](#smoothgroupsparsetracktype)
  - [SmoothGroupStreamManifestBehavior](#smoothgroupstreammanifestbehavior)
  - [SmoothGroupTimestampOffsetMode](#smoothgrouptimestampoffsetmode)
  - [Smpte2038DataPreference](#smpte2038datapreference)
  - [TemporalFilterPostFilterSharpening](#temporalfilterpostfiltersharpening)
  - [TemporalFilterStrength](#temporalfilterstrength)
  - [TimecodeConfigSource](#timecodeconfigsource)
  - [TtmlDestinationStyleControl](#ttmldestinationstylecontrol)
  - [UdpTimedMetadataId3Frame](#udptimedmetadataid3frame)
  - [VideoDescriptionRespondToAfd](#videodescriptionrespondtoafd)
  - [VideoDescriptionScalingBehavior](#videodescriptionscalingbehavior)
  - [VideoSelectorColorSpace](#videoselectorcolorspace)
  - [VideoSelectorColorSpaceUsage](#videoselectorcolorspaceusage)
  - [WavCodingMode](#wavcodingmode)

## AacCodingMode

```python
from mypy_boto3_medialive.literals import AacCodingMode
```

Values:

- `AD_RECEIVER_MIX`
- `CODING_MODE_1_0`
- `CODING_MODE_1_1`
- `CODING_MODE_2_0`
- `CODING_MODE_5_1`

## AacInputType

```python
from mypy_boto3_medialive.literals import AacInputType
```

Values:

- `BROADCASTER_MIXED_AD`
- `NORMAL`

## AacProfile

```python
from mypy_boto3_medialive.literals import AacProfile
```

Values:

- `HEV1`
- `HEV2`
- `LC`

## AacRateControlMode

```python
from mypy_boto3_medialive.literals import AacRateControlMode
```

Values:

- `CBR`
- `VBR`

## AacRawFormat

```python
from mypy_boto3_medialive.literals import AacRawFormat
```

Values:

- `LATM_LOAS`
- `NONE`

## AacSpec

```python
from mypy_boto3_medialive.literals import AacSpec
```

Values:

- `MPEG2`
- `MPEG4`

## AacVbrQuality

```python
from mypy_boto3_medialive.literals import AacVbrQuality
```

Values:

- `HIGH`
- `LOW`
- `MEDIUM_HIGH`
- `MEDIUM_LOW`

## Ac3BitstreamMode

```python
from mypy_boto3_medialive.literals import Ac3BitstreamMode
```

Values:

- `COMMENTARY`
- `COMPLETE_MAIN`
- `DIALOGUE`
- `EMERGENCY`
- `HEARING_IMPAIRED`
- `MUSIC_AND_EFFECTS`
- `VISUALLY_IMPAIRED`
- `VOICE_OVER`

## Ac3CodingMode

```python
from mypy_boto3_medialive.literals import Ac3CodingMode
```

Values:

- `CODING_MODE_1_0`
- `CODING_MODE_1_1`
- `CODING_MODE_2_0`
- `CODING_MODE_3_2_LFE`

## Ac3DrcProfile

```python
from mypy_boto3_medialive.literals import Ac3DrcProfile
```

Values:

- `FILM_STANDARD`
- `NONE`

## Ac3LfeFilter

```python
from mypy_boto3_medialive.literals import Ac3LfeFilter
```

Values:

- `DISABLED`
- `ENABLED`

## Ac3MetadataControl

```python
from mypy_boto3_medialive.literals import Ac3MetadataControl
```

Values:

- `FOLLOW_INPUT`
- `USE_CONFIGURED`

## AcceptHeader

```python
from mypy_boto3_medialive.literals import AcceptHeader
```

Values:

- `image/jpeg`

## AfdSignaling

```python
from mypy_boto3_medialive.literals import AfdSignaling
```

Values:

- `AUTO`
- `FIXED`
- `NONE`

## AudioDescriptionAudioTypeControl

```python
from mypy_boto3_medialive.literals import AudioDescriptionAudioTypeControl
```

Values:

- `FOLLOW_INPUT`
- `USE_CONFIGURED`

## AudioDescriptionLanguageCodeControl

```python
from mypy_boto3_medialive.literals import AudioDescriptionLanguageCodeControl
```

Values:

- `FOLLOW_INPUT`
- `USE_CONFIGURED`

## AudioLanguageSelectionPolicy

```python
from mypy_boto3_medialive.literals import AudioLanguageSelectionPolicy
```

Values:

- `LOOSE`
- `STRICT`

## AudioNormalizationAlgorithm

```python
from mypy_boto3_medialive.literals import AudioNormalizationAlgorithm
```

Values:

- `ITU_1770_1`
- `ITU_1770_2`

## AudioNormalizationAlgorithmControl

```python
from mypy_boto3_medialive.literals import AudioNormalizationAlgorithmControl
```

Values:

- `CORRECT_AUDIO`

## AudioOnlyHlsSegmentType

```python
from mypy_boto3_medialive.literals import AudioOnlyHlsSegmentType
```

Values:

- `AAC`
- `FMP4`

## AudioOnlyHlsTrackType

```python
from mypy_boto3_medialive.literals import AudioOnlyHlsTrackType
```

Values:

- `ALTERNATE_AUDIO_AUTO_SELECT`
- `ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT`
- `ALTERNATE_AUDIO_NOT_AUTO_SELECT`
- `AUDIO_ONLY_VARIANT_STREAM`

## AudioType

```python
from mypy_boto3_medialive.literals import AudioType
```

Values:

- `CLEAN_EFFECTS`
- `HEARING_IMPAIRED`
- `UNDEFINED`
- `VISUAL_IMPAIRED_COMMENTARY`

## AuthenticationScheme

```python
from mypy_boto3_medialive.literals import AuthenticationScheme
```

Values:

- `AKAMAI`
- `COMMON`

## AvailBlankingState

```python
from mypy_boto3_medialive.literals import AvailBlankingState
```

Values:

- `DISABLED`
- `ENABLED`

## BlackoutSlateNetworkEndBlackout

```python
from mypy_boto3_medialive.literals import BlackoutSlateNetworkEndBlackout
```

Values:

- `DISABLED`
- `ENABLED`

## BlackoutSlateState

```python
from mypy_boto3_medialive.literals import BlackoutSlateState
```

Values:

- `DISABLED`
- `ENABLED`

## BurnInAlignment

```python
from mypy_boto3_medialive.literals import BurnInAlignment
```

Values:

- `CENTERED`
- `LEFT`
- `SMART`

## BurnInBackgroundColor

```python
from mypy_boto3_medialive.literals import BurnInBackgroundColor
```

Values:

- `BLACK`
- `NONE`
- `WHITE`

## BurnInFontColor

```python
from mypy_boto3_medialive.literals import BurnInFontColor
```

Values:

- `BLACK`
- `BLUE`
- `GREEN`
- `RED`
- `WHITE`
- `YELLOW`

## BurnInOutlineColor

```python
from mypy_boto3_medialive.literals import BurnInOutlineColor
```

Values:

- `BLACK`
- `BLUE`
- `GREEN`
- `RED`
- `WHITE`
- `YELLOW`

## BurnInShadowColor

```python
from mypy_boto3_medialive.literals import BurnInShadowColor
```

Values:

- `BLACK`
- `NONE`
- `WHITE`

## BurnInTeletextGridControl

```python
from mypy_boto3_medialive.literals import BurnInTeletextGridControl
```

Values:

- `FIXED`
- `SCALED`

## CdiInputResolution

```python
from mypy_boto3_medialive.literals import CdiInputResolution
```

Values:

- `FHD`
- `HD`
- `SD`
- `UHD`

## ChannelClass

```python
from mypy_boto3_medialive.literals import ChannelClass
```

Values:

- `SINGLE_PIPELINE`
- `STANDARD`

## ChannelCreatedWaiterName

```python
from mypy_boto3_medialive.literals import ChannelCreatedWaiterName
```

Values:

- `channel_created`

## ChannelDeletedWaiterName

```python
from mypy_boto3_medialive.literals import ChannelDeletedWaiterName
```

Values:

- `channel_deleted`

## ChannelRunningWaiterName

```python
from mypy_boto3_medialive.literals import ChannelRunningWaiterName
```

Values:

- `channel_running`

## ChannelState

```python
from mypy_boto3_medialive.literals import ChannelState
```

Values:

- `CREATE_FAILED`
- `CREATING`
- `DELETED`
- `DELETING`
- `IDLE`
- `RECOVERING`
- `RUNNING`
- `STARTING`
- `STOPPING`
- `UPDATE_FAILED`
- `UPDATING`

## ChannelStoppedWaiterName

```python
from mypy_boto3_medialive.literals import ChannelStoppedWaiterName
```

Values:

- `channel_stopped`

## ContentType

```python
from mypy_boto3_medialive.literals import ContentType
```

Values:

- `image/jpeg`

## DescribeSchedulePaginatorName

```python
from mypy_boto3_medialive.literals import DescribeSchedulePaginatorName
```

Values:

- `describe_schedule`

## DeviceSettingsSyncState

```python
from mypy_boto3_medialive.literals import DeviceSettingsSyncState
```

Values:

- `SYNCED`
- `SYNCING`

## DeviceUpdateStatus

```python
from mypy_boto3_medialive.literals import DeviceUpdateStatus
```

Values:

- `NOT_UP_TO_DATE`
- `UP_TO_DATE`

## DvbSdtOutputSdt

```python
from mypy_boto3_medialive.literals import DvbSdtOutputSdt
```

Values:

- `SDT_FOLLOW`
- `SDT_FOLLOW_IF_PRESENT`
- `SDT_MANUAL`
- `SDT_NONE`

## DvbSubDestinationAlignment

```python
from mypy_boto3_medialive.literals import DvbSubDestinationAlignment
```

Values:

- `CENTERED`
- `LEFT`
- `SMART`

## DvbSubDestinationBackgroundColor

```python
from mypy_boto3_medialive.literals import DvbSubDestinationBackgroundColor
```

Values:

- `BLACK`
- `NONE`
- `WHITE`

## DvbSubDestinationFontColor

```python
from mypy_boto3_medialive.literals import DvbSubDestinationFontColor
```

Values:

- `BLACK`
- `BLUE`
- `GREEN`
- `RED`
- `WHITE`
- `YELLOW`

## DvbSubDestinationOutlineColor

```python
from mypy_boto3_medialive.literals import DvbSubDestinationOutlineColor
```

Values:

- `BLACK`
- `BLUE`
- `GREEN`
- `RED`
- `WHITE`
- `YELLOW`

## DvbSubDestinationShadowColor

```python
from mypy_boto3_medialive.literals import DvbSubDestinationShadowColor
```

Values:

- `BLACK`
- `NONE`
- `WHITE`

## DvbSubDestinationTeletextGridControl

```python
from mypy_boto3_medialive.literals import DvbSubDestinationTeletextGridControl
```

Values:

- `FIXED`
- `SCALED`

## Eac3AttenuationControl

```python
from mypy_boto3_medialive.literals import Eac3AttenuationControl
```

Values:

- `ATTENUATE_3_DB`
- `NONE`

## Eac3BitstreamMode

```python
from mypy_boto3_medialive.literals import Eac3BitstreamMode
```

Values:

- `COMMENTARY`
- `COMPLETE_MAIN`
- `EMERGENCY`
- `HEARING_IMPAIRED`
- `VISUALLY_IMPAIRED`

## Eac3CodingMode

```python
from mypy_boto3_medialive.literals import Eac3CodingMode
```

Values:

- `CODING_MODE_1_0`
- `CODING_MODE_2_0`
- `CODING_MODE_3_2`

## Eac3DcFilter

```python
from mypy_boto3_medialive.literals import Eac3DcFilter
```

Values:

- `DISABLED`
- `ENABLED`

## Eac3DrcLine

```python
from mypy_boto3_medialive.literals import Eac3DrcLine
```

Values:

- `FILM_LIGHT`
- `FILM_STANDARD`
- `MUSIC_LIGHT`
- `MUSIC_STANDARD`
- `NONE`
- `SPEECH`

## Eac3DrcRf

```python
from mypy_boto3_medialive.literals import Eac3DrcRf
```

Values:

- `FILM_LIGHT`
- `FILM_STANDARD`
- `MUSIC_LIGHT`
- `MUSIC_STANDARD`
- `NONE`
- `SPEECH`

## Eac3LfeControl

```python
from mypy_boto3_medialive.literals import Eac3LfeControl
```

Values:

- `LFE`
- `NO_LFE`

## Eac3LfeFilter

```python
from mypy_boto3_medialive.literals import Eac3LfeFilter
```

Values:

- `DISABLED`
- `ENABLED`

## Eac3MetadataControl

```python
from mypy_boto3_medialive.literals import Eac3MetadataControl
```

Values:

- `FOLLOW_INPUT`
- `USE_CONFIGURED`

## Eac3PassthroughControl

```python
from mypy_boto3_medialive.literals import Eac3PassthroughControl
```

Values:

- `NO_PASSTHROUGH`
- `WHEN_POSSIBLE`

## Eac3PhaseControl

```python
from mypy_boto3_medialive.literals import Eac3PhaseControl
```

Values:

- `NO_SHIFT`
- `SHIFT_90_DEGREES`

## Eac3StereoDownmix

```python
from mypy_boto3_medialive.literals import Eac3StereoDownmix
```

Values:

- `DPL2`
- `LO_RO`
- `LT_RT`
- `NOT_INDICATED`

## Eac3SurroundExMode

```python
from mypy_boto3_medialive.literals import Eac3SurroundExMode
```

Values:

- `DISABLED`
- `ENABLED`
- `NOT_INDICATED`

## Eac3SurroundMode

```python
from mypy_boto3_medialive.literals import Eac3SurroundMode
```

Values:

- `DISABLED`
- `ENABLED`
- `NOT_INDICATED`

## EbuTtDDestinationStyleControl

```python
from mypy_boto3_medialive.literals import EbuTtDDestinationStyleControl
```

Values:

- `EXCLUDE`
- `INCLUDE`

## EbuTtDFillLineGapControl

```python
from mypy_boto3_medialive.literals import EbuTtDFillLineGapControl
```

Values:

- `DISABLED`
- `ENABLED`

## EmbeddedConvert608To708

```python
from mypy_boto3_medialive.literals import EmbeddedConvert608To708
```

Values:

- `DISABLED`
- `UPCONVERT`

## EmbeddedScte20Detection

```python
from mypy_boto3_medialive.literals import EmbeddedScte20Detection
```

Values:

- `AUTO`
- `OFF`

## FeatureActivationsInputPrepareScheduleActions

```python
from mypy_boto3_medialive.literals import FeatureActivationsInputPrepareScheduleActions
```

Values:

- `DISABLED`
- `ENABLED`

## FecOutputIncludeFec

```python
from mypy_boto3_medialive.literals import FecOutputIncludeFec
```

Values:

- `COLUMN`
- `COLUMN_AND_ROW`

## FixedAfd

```python
from mypy_boto3_medialive.literals import FixedAfd
```

Values:

- `AFD_0000`
- `AFD_0010`
- `AFD_0011`
- `AFD_0100`
- `AFD_1000`
- `AFD_1001`
- `AFD_1010`
- `AFD_1011`
- `AFD_1101`
- `AFD_1110`
- `AFD_1111`

## Fmp4NielsenId3Behavior

```python
from mypy_boto3_medialive.literals import Fmp4NielsenId3Behavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## Fmp4TimedMetadataBehavior

```python
from mypy_boto3_medialive.literals import Fmp4TimedMetadataBehavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## FollowPoint

```python
from mypy_boto3_medialive.literals import FollowPoint
```

Values:

- `END`
- `START`

## FrameCaptureIntervalUnit

```python
from mypy_boto3_medialive.literals import FrameCaptureIntervalUnit
```

Values:

- `MILLISECONDS`
- `SECONDS`

## GlobalConfigurationInputEndAction

```python
from mypy_boto3_medialive.literals import GlobalConfigurationInputEndAction
```

Values:

- `NONE`
- `SWITCH_AND_LOOP_INPUTS`

## GlobalConfigurationLowFramerateInputs

```python
from mypy_boto3_medialive.literals import GlobalConfigurationLowFramerateInputs
```

Values:

- `DISABLED`
- `ENABLED`

## GlobalConfigurationOutputLockingMode

```python
from mypy_boto3_medialive.literals import GlobalConfigurationOutputLockingMode
```

Values:

- `EPOCH_LOCKING`
- `PIPELINE_LOCKING`

## GlobalConfigurationOutputTimingSource

```python
from mypy_boto3_medialive.literals import GlobalConfigurationOutputTimingSource
```

Values:

- `INPUT_CLOCK`
- `SYSTEM_CLOCK`

## H264AdaptiveQuantization

```python
from mypy_boto3_medialive.literals import H264AdaptiveQuantization
```

Values:

- `HIGH`
- `HIGHER`
- `LOW`
- `MAX`
- `MEDIUM`
- `OFF`

## H264ColorMetadata

```python
from mypy_boto3_medialive.literals import H264ColorMetadata
```

Values:

- `IGNORE`
- `INSERT`

## H264EntropyEncoding

```python
from mypy_boto3_medialive.literals import H264EntropyEncoding
```

Values:

- `CABAC`
- `CAVLC`

## H264FlickerAq

```python
from mypy_boto3_medialive.literals import H264FlickerAq
```

Values:

- `DISABLED`
- `ENABLED`

## H264ForceFieldPictures

```python
from mypy_boto3_medialive.literals import H264ForceFieldPictures
```

Values:

- `DISABLED`
- `ENABLED`

## H264FramerateControl

```python
from mypy_boto3_medialive.literals import H264FramerateControl
```

Values:

- `INITIALIZE_FROM_SOURCE`
- `SPECIFIED`

## H264GopBReference

```python
from mypy_boto3_medialive.literals import H264GopBReference
```

Values:

- `DISABLED`
- `ENABLED`

## H264GopSizeUnits

```python
from mypy_boto3_medialive.literals import H264GopSizeUnits
```

Values:

- `FRAMES`
- `SECONDS`

## H264Level

```python
from mypy_boto3_medialive.literals import H264Level
```

Values:

- `H264_LEVEL_1`
- `H264_LEVEL_1_1`
- `H264_LEVEL_1_2`
- `H264_LEVEL_1_3`
- `H264_LEVEL_2`
- `H264_LEVEL_2_1`
- `H264_LEVEL_2_2`
- `H264_LEVEL_3`
- `H264_LEVEL_3_1`
- `H264_LEVEL_3_2`
- `H264_LEVEL_4`
- `H264_LEVEL_4_1`
- `H264_LEVEL_4_2`
- `H264_LEVEL_5`
- `H264_LEVEL_5_1`
- `H264_LEVEL_5_2`
- `H264_LEVEL_AUTO`

## H264LookAheadRateControl

```python
from mypy_boto3_medialive.literals import H264LookAheadRateControl
```

Values:

- `HIGH`
- `LOW`
- `MEDIUM`

## H264ParControl

```python
from mypy_boto3_medialive.literals import H264ParControl
```

Values:

- `INITIALIZE_FROM_SOURCE`
- `SPECIFIED`

## H264Profile

```python
from mypy_boto3_medialive.literals import H264Profile
```

Values:

- `BASELINE`
- `HIGH`
- `HIGH_10BIT`
- `HIGH_422`
- `HIGH_422_10BIT`
- `MAIN`

## H264QualityLevel

```python
from mypy_boto3_medialive.literals import H264QualityLevel
```

Values:

- `ENHANCED_QUALITY`
- `STANDARD_QUALITY`

## H264RateControlMode

```python
from mypy_boto3_medialive.literals import H264RateControlMode
```

Values:

- `CBR`
- `MULTIPLEX`
- `QVBR`
- `VBR`

## H264ScanType

```python
from mypy_boto3_medialive.literals import H264ScanType
```

Values:

- `INTERLACED`
- `PROGRESSIVE`

## H264SceneChangeDetect

```python
from mypy_boto3_medialive.literals import H264SceneChangeDetect
```

Values:

- `DISABLED`
- `ENABLED`

## H264SpatialAq

```python
from mypy_boto3_medialive.literals import H264SpatialAq
```

Values:

- `DISABLED`
- `ENABLED`

## H264SubGopLength

```python
from mypy_boto3_medialive.literals import H264SubGopLength
```

Values:

- `DYNAMIC`
- `FIXED`

## H264Syntax

```python
from mypy_boto3_medialive.literals import H264Syntax
```

Values:

- `DEFAULT`
- `RP2027`

## H264TemporalAq

```python
from mypy_boto3_medialive.literals import H264TemporalAq
```

Values:

- `DISABLED`
- `ENABLED`

## H264TimecodeInsertionBehavior

```python
from mypy_boto3_medialive.literals import H264TimecodeInsertionBehavior
```

Values:

- `DISABLED`
- `PIC_TIMING_SEI`

## H265AdaptiveQuantization

```python
from mypy_boto3_medialive.literals import H265AdaptiveQuantization
```

Values:

- `HIGH`
- `HIGHER`
- `LOW`
- `MAX`
- `MEDIUM`
- `OFF`

## H265AlternativeTransferFunction

```python
from mypy_boto3_medialive.literals import H265AlternativeTransferFunction
```

Values:

- `INSERT`
- `OMIT`

## H265ColorMetadata

```python
from mypy_boto3_medialive.literals import H265ColorMetadata
```

Values:

- `IGNORE`
- `INSERT`

## H265FlickerAq

```python
from mypy_boto3_medialive.literals import H265FlickerAq
```

Values:

- `DISABLED`
- `ENABLED`

## H265GopSizeUnits

```python
from mypy_boto3_medialive.literals import H265GopSizeUnits
```

Values:

- `FRAMES`
- `SECONDS`

## H265Level

```python
from mypy_boto3_medialive.literals import H265Level
```

Values:

- `H265_LEVEL_1`
- `H265_LEVEL_2`
- `H265_LEVEL_2_1`
- `H265_LEVEL_3`
- `H265_LEVEL_3_1`
- `H265_LEVEL_4`
- `H265_LEVEL_4_1`
- `H265_LEVEL_5`
- `H265_LEVEL_5_1`
- `H265_LEVEL_5_2`
- `H265_LEVEL_6`
- `H265_LEVEL_6_1`
- `H265_LEVEL_6_2`
- `H265_LEVEL_AUTO`

## H265LookAheadRateControl

```python
from mypy_boto3_medialive.literals import H265LookAheadRateControl
```

Values:

- `HIGH`
- `LOW`
- `MEDIUM`

## H265Profile

```python
from mypy_boto3_medialive.literals import H265Profile
```

Values:

- `MAIN`
- `MAIN_10BIT`

## H265RateControlMode

```python
from mypy_boto3_medialive.literals import H265RateControlMode
```

Values:

- `CBR`
- `MULTIPLEX`
- `QVBR`

## H265ScanType

```python
from mypy_boto3_medialive.literals import H265ScanType
```

Values:

- `INTERLACED`
- `PROGRESSIVE`

## H265SceneChangeDetect

```python
from mypy_boto3_medialive.literals import H265SceneChangeDetect
```

Values:

- `DISABLED`
- `ENABLED`

## H265Tier

```python
from mypy_boto3_medialive.literals import H265Tier
```

Values:

- `HIGH`
- `MAIN`

## H265TimecodeInsertionBehavior

```python
from mypy_boto3_medialive.literals import H265TimecodeInsertionBehavior
```

Values:

- `DISABLED`
- `PIC_TIMING_SEI`

## HlsAdMarkers

```python
from mypy_boto3_medialive.literals import HlsAdMarkers
```

Values:

- `ADOBE`
- `ELEMENTAL`
- `ELEMENTAL_SCTE35`

## HlsAkamaiHttpTransferMode

```python
from mypy_boto3_medialive.literals import HlsAkamaiHttpTransferMode
```

Values:

- `CHUNKED`
- `NON_CHUNKED`

## HlsCaptionLanguageSetting

```python
from mypy_boto3_medialive.literals import HlsCaptionLanguageSetting
```

Values:

- `INSERT`
- `NONE`
- `OMIT`

## HlsClientCache

```python
from mypy_boto3_medialive.literals import HlsClientCache
```

Values:

- `DISABLED`
- `ENABLED`

## HlsCodecSpecification

```python
from mypy_boto3_medialive.literals import HlsCodecSpecification
```

Values:

- `RFC_4281`
- `RFC_6381`

## HlsDirectoryStructure

```python
from mypy_boto3_medialive.literals import HlsDirectoryStructure
```

Values:

- `SINGLE_DIRECTORY`
- `SUBDIRECTORY_PER_STREAM`

## HlsDiscontinuityTags

```python
from mypy_boto3_medialive.literals import HlsDiscontinuityTags
```

Values:

- `INSERT`
- `NEVER_INSERT`

## HlsEncryptionType

```python
from mypy_boto3_medialive.literals import HlsEncryptionType
```

Values:

- `AES128`
- `SAMPLE_AES`

## HlsH265PackagingType

```python
from mypy_boto3_medialive.literals import HlsH265PackagingType
```

Values:

- `HEV1`
- `HVC1`

## HlsId3SegmentTaggingState

```python
from mypy_boto3_medialive.literals import HlsId3SegmentTaggingState
```

Values:

- `DISABLED`
- `ENABLED`

## HlsIncompleteSegmentBehavior

```python
from mypy_boto3_medialive.literals import HlsIncompleteSegmentBehavior
```

Values:

- `AUTO`
- `SUPPRESS`

## HlsIvInManifest

```python
from mypy_boto3_medialive.literals import HlsIvInManifest
```

Values:

- `EXCLUDE`
- `INCLUDE`

## HlsIvSource

```python
from mypy_boto3_medialive.literals import HlsIvSource
```

Values:

- `EXPLICIT`
- `FOLLOWS_SEGMENT_NUMBER`

## HlsManifestCompression

```python
from mypy_boto3_medialive.literals import HlsManifestCompression
```

Values:

- `GZIP`
- `NONE`

## HlsManifestDurationFormat

```python
from mypy_boto3_medialive.literals import HlsManifestDurationFormat
```

Values:

- `FLOATING_POINT`
- `INTEGER`

## HlsMediaStoreStorageClass

```python
from mypy_boto3_medialive.literals import HlsMediaStoreStorageClass
```

Values:

- `TEMPORAL`

## HlsMode

```python
from mypy_boto3_medialive.literals import HlsMode
```

Values:

- `LIVE`
- `VOD`

## HlsOutputSelection

```python
from mypy_boto3_medialive.literals import HlsOutputSelection
```

Values:

- `MANIFESTS_AND_SEGMENTS`
- `SEGMENTS_ONLY`
- `VARIANT_MANIFESTS_AND_SEGMENTS`

## HlsProgramDateTime

```python
from mypy_boto3_medialive.literals import HlsProgramDateTime
```

Values:

- `EXCLUDE`
- `INCLUDE`

## HlsRedundantManifest

```python
from mypy_boto3_medialive.literals import HlsRedundantManifest
```

Values:

- `DISABLED`
- `ENABLED`

## HlsSegmentationMode

```python
from mypy_boto3_medialive.literals import HlsSegmentationMode
```

Values:

- `USE_INPUT_SEGMENTATION`
- `USE_SEGMENT_DURATION`

## HlsStreamInfResolution

```python
from mypy_boto3_medialive.literals import HlsStreamInfResolution
```

Values:

- `EXCLUDE`
- `INCLUDE`

## HlsTimedMetadataId3Frame

```python
from mypy_boto3_medialive.literals import HlsTimedMetadataId3Frame
```

Values:

- `NONE`
- `PRIV`
- `TDRL`

## HlsTsFileMode

```python
from mypy_boto3_medialive.literals import HlsTsFileMode
```

Values:

- `SEGMENTED_FILES`
- `SINGLE_FILE`

## HlsWebdavHttpTransferMode

```python
from mypy_boto3_medialive.literals import HlsWebdavHttpTransferMode
```

Values:

- `CHUNKED`
- `NON_CHUNKED`

## IFrameOnlyPlaylistType

```python
from mypy_boto3_medialive.literals import IFrameOnlyPlaylistType
```

Values:

- `DISABLED`
- `STANDARD`

## InputAttachedWaiterName

```python
from mypy_boto3_medialive.literals import InputAttachedWaiterName
```

Values:

- `input_attached`

## InputClass

```python
from mypy_boto3_medialive.literals import InputClass
```

Values:

- `SINGLE_PIPELINE`
- `STANDARD`

## InputCodec

```python
from mypy_boto3_medialive.literals import InputCodec
```

Values:

- `AVC`
- `HEVC`
- `MPEG2`

## InputDeblockFilter

```python
from mypy_boto3_medialive.literals import InputDeblockFilter
```

Values:

- `DISABLED`
- `ENABLED`

## InputDeletedWaiterName

```python
from mypy_boto3_medialive.literals import InputDeletedWaiterName
```

Values:

- `input_deleted`

## InputDenoiseFilter

```python
from mypy_boto3_medialive.literals import InputDenoiseFilter
```

Values:

- `DISABLED`
- `ENABLED`

## InputDetachedWaiterName

```python
from mypy_boto3_medialive.literals import InputDetachedWaiterName
```

Values:

- `input_detached`

## InputDeviceActiveInput

```python
from mypy_boto3_medialive.literals import InputDeviceActiveInput
```

Values:

- `HDMI`
- `SDI`

## InputDeviceConfiguredInput

```python
from mypy_boto3_medialive.literals import InputDeviceConfiguredInput
```

Values:

- `AUTO`
- `HDMI`
- `SDI`

## InputDeviceConnectionState

```python
from mypy_boto3_medialive.literals import InputDeviceConnectionState
```

Values:

- `CONNECTED`
- `DISCONNECTED`

## InputDeviceIpScheme

```python
from mypy_boto3_medialive.literals import InputDeviceIpScheme
```

Values:

- `DHCP`
- `STATIC`

## InputDeviceScanType

```python
from mypy_boto3_medialive.literals import InputDeviceScanType
```

Values:

- `INTERLACED`
- `PROGRESSIVE`

## InputDeviceState

```python
from mypy_boto3_medialive.literals import InputDeviceState
```

Values:

- `IDLE`
- `STREAMING`

## InputDeviceTransferType

```python
from mypy_boto3_medialive.literals import InputDeviceTransferType
```

Values:

- `INCOMING`
- `OUTGOING`

## InputDeviceType

```python
from mypy_boto3_medialive.literals import InputDeviceType
```

Values:

- `HD`

## InputFilter

```python
from mypy_boto3_medialive.literals import InputFilter
```

Values:

- `AUTO`
- `DISABLED`
- `FORCED`

## InputLossActionForHlsOut

```python
from mypy_boto3_medialive.literals import InputLossActionForHlsOut
```

Values:

- `EMIT_OUTPUT`
- `PAUSE_OUTPUT`

## InputLossActionForMsSmoothOut

```python
from mypy_boto3_medialive.literals import InputLossActionForMsSmoothOut
```

Values:

- `EMIT_OUTPUT`
- `PAUSE_OUTPUT`

## InputLossActionForRtmpOut

```python
from mypy_boto3_medialive.literals import InputLossActionForRtmpOut
```

Values:

- `EMIT_OUTPUT`
- `PAUSE_OUTPUT`

## InputLossActionForUdpOut

```python
from mypy_boto3_medialive.literals import InputLossActionForUdpOut
```

Values:

- `DROP_PROGRAM`
- `DROP_TS`
- `EMIT_PROGRAM`

## InputLossImageType

```python
from mypy_boto3_medialive.literals import InputLossImageType
```

Values:

- `COLOR`
- `SLATE`

## InputMaximumBitrate

```python
from mypy_boto3_medialive.literals import InputMaximumBitrate
```

Values:

- `MAX_10_MBPS`
- `MAX_20_MBPS`
- `MAX_50_MBPS`

## InputPreference

```python
from mypy_boto3_medialive.literals import InputPreference
```

Values:

- `EQUAL_INPUT_PREFERENCE`
- `PRIMARY_INPUT_PREFERRED`

## InputResolution

```python
from mypy_boto3_medialive.literals import InputResolution
```

Values:

- `HD`
- `SD`
- `UHD`

## InputSecurityGroupState

```python
from mypy_boto3_medialive.literals import InputSecurityGroupState
```

Values:

- `DELETED`
- `IDLE`
- `IN_USE`
- `UPDATING`

## InputSourceEndBehavior

```python
from mypy_boto3_medialive.literals import InputSourceEndBehavior
```

Values:

- `CONTINUE`
- `LOOP`

## InputSourceType

```python
from mypy_boto3_medialive.literals import InputSourceType
```

Values:

- `DYNAMIC`
- `STATIC`

## InputState

```python
from mypy_boto3_medialive.literals import InputState
```

Values:

- `ATTACHED`
- `CREATING`
- `DELETED`
- `DELETING`
- `DETACHED`

## InputTimecodeSource

```python
from mypy_boto3_medialive.literals import InputTimecodeSource
```

Values:

- `EMBEDDED`
- `ZEROBASED`

## InputType

```python
from mypy_boto3_medialive.literals import InputType
```

Values:

- `AWS_CDI`
- `INPUT_DEVICE`
- `MEDIACONNECT`
- `MP4_FILE`
- `RTMP_PULL`
- `RTMP_PUSH`
- `RTP_PUSH`
- `UDP_PUSH`
- `URL_PULL`

## LastFrameClippingBehavior

```python
from mypy_boto3_medialive.literals import LastFrameClippingBehavior
```

Values:

- `EXCLUDE_LAST_FRAME`
- `INCLUDE_LAST_FRAME`

## ListChannelsPaginatorName

```python
from mypy_boto3_medialive.literals import ListChannelsPaginatorName
```

Values:

- `list_channels`

## ListInputDeviceTransfersPaginatorName

```python
from mypy_boto3_medialive.literals import ListInputDeviceTransfersPaginatorName
```

Values:

- `list_input_device_transfers`

## ListInputDevicesPaginatorName

```python
from mypy_boto3_medialive.literals import ListInputDevicesPaginatorName
```

Values:

- `list_input_devices`

## ListInputSecurityGroupsPaginatorName

```python
from mypy_boto3_medialive.literals import ListInputSecurityGroupsPaginatorName
```

Values:

- `list_input_security_groups`

## ListInputsPaginatorName

```python
from mypy_boto3_medialive.literals import ListInputsPaginatorName
```

Values:

- `list_inputs`

## ListMultiplexProgramsPaginatorName

```python
from mypy_boto3_medialive.literals import ListMultiplexProgramsPaginatorName
```

Values:

- `list_multiplex_programs`

## ListMultiplexesPaginatorName

```python
from mypy_boto3_medialive.literals import ListMultiplexesPaginatorName
```

Values:

- `list_multiplexes`

## ListOfferingsPaginatorName

```python
from mypy_boto3_medialive.literals import ListOfferingsPaginatorName
```

Values:

- `list_offerings`

## ListReservationsPaginatorName

```python
from mypy_boto3_medialive.literals import ListReservationsPaginatorName
```

Values:

- `list_reservations`

## LogLevel

```python
from mypy_boto3_medialive.literals import LogLevel
```

Values:

- `DEBUG`
- `DISABLED`
- `ERROR`
- `INFO`
- `WARNING`

## M2tsAbsentInputAudioBehavior

```python
from mypy_boto3_medialive.literals import M2tsAbsentInputAudioBehavior
```

Values:

- `DROP`
- `ENCODE_SILENCE`

## M2tsArib

```python
from mypy_boto3_medialive.literals import M2tsArib
```

Values:

- `DISABLED`
- `ENABLED`

## M2tsAribCaptionsPidControl

```python
from mypy_boto3_medialive.literals import M2tsAribCaptionsPidControl
```

Values:

- `AUTO`
- `USE_CONFIGURED`

## M2tsAudioBufferModel

```python
from mypy_boto3_medialive.literals import M2tsAudioBufferModel
```

Values:

- `ATSC`
- `DVB`

## M2tsAudioInterval

```python
from mypy_boto3_medialive.literals import M2tsAudioInterval
```

Values:

- `VIDEO_AND_FIXED_INTERVALS`
- `VIDEO_INTERVAL`

## M2tsAudioStreamType

```python
from mypy_boto3_medialive.literals import M2tsAudioStreamType
```

Values:

- `ATSC`
- `DVB`

## M2tsBufferModel

```python
from mypy_boto3_medialive.literals import M2tsBufferModel
```

Values:

- `MULTIPLEX`
- `NONE`

## M2tsCcDescriptor

```python
from mypy_boto3_medialive.literals import M2tsCcDescriptor
```

Values:

- `DISABLED`
- `ENABLED`

## M2tsEbifControl

```python
from mypy_boto3_medialive.literals import M2tsEbifControl
```

Values:

- `NONE`
- `PASSTHROUGH`

## M2tsEbpPlacement

```python
from mypy_boto3_medialive.literals import M2tsEbpPlacement
```

Values:

- `VIDEO_AND_AUDIO_PIDS`
- `VIDEO_PID`

## M2tsEsRateInPes

```python
from mypy_boto3_medialive.literals import M2tsEsRateInPes
```

Values:

- `EXCLUDE`
- `INCLUDE`

## M2tsKlv

```python
from mypy_boto3_medialive.literals import M2tsKlv
```

Values:

- `NONE`
- `PASSTHROUGH`

## M2tsNielsenId3Behavior

```python
from mypy_boto3_medialive.literals import M2tsNielsenId3Behavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## M2tsPcrControl

```python
from mypy_boto3_medialive.literals import M2tsPcrControl
```

Values:

- `CONFIGURED_PCR_PERIOD`
- `PCR_EVERY_PES_PACKET`

## M2tsRateMode

```python
from mypy_boto3_medialive.literals import M2tsRateMode
```

Values:

- `CBR`
- `VBR`

## M2tsScte35Control

```python
from mypy_boto3_medialive.literals import M2tsScte35Control
```

Values:

- `NONE`
- `PASSTHROUGH`

## M2tsSegmentationMarkers

```python
from mypy_boto3_medialive.literals import M2tsSegmentationMarkers
```

Values:

- `EBP`
- `EBP_LEGACY`
- `NONE`
- `PSI_SEGSTART`
- `RAI_ADAPT`
- `RAI_SEGSTART`

## M2tsSegmentationStyle

```python
from mypy_boto3_medialive.literals import M2tsSegmentationStyle
```

Values:

- `MAINTAIN_CADENCE`
- `RESET_CADENCE`

## M2tsTimedMetadataBehavior

```python
from mypy_boto3_medialive.literals import M2tsTimedMetadataBehavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## M3u8NielsenId3Behavior

```python
from mypy_boto3_medialive.literals import M3u8NielsenId3Behavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## M3u8PcrControl

```python
from mypy_boto3_medialive.literals import M3u8PcrControl
```

Values:

- `CONFIGURED_PCR_PERIOD`
- `PCR_EVERY_PES_PACKET`

## M3u8Scte35Behavior

```python
from mypy_boto3_medialive.literals import M3u8Scte35Behavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## M3u8TimedMetadataBehavior

```python
from mypy_boto3_medialive.literals import M3u8TimedMetadataBehavior
```

Values:

- `NO_PASSTHROUGH`
- `PASSTHROUGH`

## MotionGraphicsInsertion

```python
from mypy_boto3_medialive.literals import MotionGraphicsInsertion
```

Values:

- `DISABLED`
- `ENABLED`

## Mp2CodingMode

```python
from mypy_boto3_medialive.literals import Mp2CodingMode
```

Values:

- `CODING_MODE_1_0`
- `CODING_MODE_2_0`

## Mpeg2AdaptiveQuantization

```python
from mypy_boto3_medialive.literals import Mpeg2AdaptiveQuantization
```

Values:

- `AUTO`
- `HIGH`
- `LOW`
- `MEDIUM`
- `OFF`

## Mpeg2ColorMetadata

```python
from mypy_boto3_medialive.literals import Mpeg2ColorMetadata
```

Values:

- `IGNORE`
- `INSERT`

## Mpeg2ColorSpace

```python
from mypy_boto3_medialive.literals import Mpeg2ColorSpace
```

Values:

- `AUTO`
- `PASSTHROUGH`

## Mpeg2DisplayRatio

```python
from mypy_boto3_medialive.literals import Mpeg2DisplayRatio
```

Values:

- `DISPLAYRATIO16X9`
- `DISPLAYRATIO4X3`

## Mpeg2GopSizeUnits

```python
from mypy_boto3_medialive.literals import Mpeg2GopSizeUnits
```

Values:

- `FRAMES`
- `SECONDS`

## Mpeg2ScanType

```python
from mypy_boto3_medialive.literals import Mpeg2ScanType
```

Values:

- `INTERLACED`
- `PROGRESSIVE`

## Mpeg2SubGopLength

```python
from mypy_boto3_medialive.literals import Mpeg2SubGopLength
```

Values:

- `DYNAMIC`
- `FIXED`

## Mpeg2TimecodeInsertionBehavior

```python
from mypy_boto3_medialive.literals import Mpeg2TimecodeInsertionBehavior
```

Values:

- `DISABLED`
- `GOP_TIMECODE`

## MsSmoothH265PackagingType

```python
from mypy_boto3_medialive.literals import MsSmoothH265PackagingType
```

Values:

- `HEV1`
- `HVC1`

## MultiplexCreatedWaiterName

```python
from mypy_boto3_medialive.literals import MultiplexCreatedWaiterName
```

Values:

- `multiplex_created`

## MultiplexDeletedWaiterName

```python
from mypy_boto3_medialive.literals import MultiplexDeletedWaiterName
```

Values:

- `multiplex_deleted`

## MultiplexRunningWaiterName

```python
from mypy_boto3_medialive.literals import MultiplexRunningWaiterName
```

Values:

- `multiplex_running`

## MultiplexState

```python
from mypy_boto3_medialive.literals import MultiplexState
```

Values:

- `CREATE_FAILED`
- `CREATING`
- `DELETED`
- `DELETING`
- `IDLE`
- `RECOVERING`
- `RUNNING`
- `STARTING`
- `STOPPING`

## MultiplexStoppedWaiterName

```python
from mypy_boto3_medialive.literals import MultiplexStoppedWaiterName
```

Values:

- `multiplex_stopped`

## NetworkInputServerValidation

```python
from mypy_boto3_medialive.literals import NetworkInputServerValidation
```

Values:

- `CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME`
- `CHECK_CRYPTOGRAPHY_ONLY`

## NielsenPcmToId3TaggingState

```python
from mypy_boto3_medialive.literals import NielsenPcmToId3TaggingState
```

Values:

- `DISABLED`
- `ENABLED`

## OfferingDurationUnits

```python
from mypy_boto3_medialive.literals import OfferingDurationUnits
```

Values:

- `MONTHS`

## OfferingType

```python
from mypy_boto3_medialive.literals import OfferingType
```

Values:

- `NO_UPFRONT`

## PipelineId

```python
from mypy_boto3_medialive.literals import PipelineId
```

Values:

- `PIPELINE_0`
- `PIPELINE_1`

## PreferredChannelPipeline

```python
from mypy_boto3_medialive.literals import PreferredChannelPipeline
```

Values:

- `CURRENTLY_ACTIVE`
- `PIPELINE_0`
- `PIPELINE_1`

## ReservationCodec

```python
from mypy_boto3_medialive.literals import ReservationCodec
```

Values:

- `AUDIO`
- `AVC`
- `HEVC`
- `LINK`
- `MPEG2`

## ReservationMaximumBitrate

```python
from mypy_boto3_medialive.literals import ReservationMaximumBitrate
```

Values:

- `MAX_10_MBPS`
- `MAX_20_MBPS`
- `MAX_50_MBPS`

## ReservationMaximumFramerate

```python
from mypy_boto3_medialive.literals import ReservationMaximumFramerate
```

Values:

- `MAX_30_FPS`
- `MAX_60_FPS`

## ReservationResolution

```python
from mypy_boto3_medialive.literals import ReservationResolution
```

Values:

- `FHD`
- `HD`
- `SD`
- `UHD`

## ReservationResourceType

```python
from mypy_boto3_medialive.literals import ReservationResourceType
```

Values:

- `CHANNEL`
- `INPUT`
- `MULTIPLEX`
- `OUTPUT`

## ReservationSpecialFeature

```python
from mypy_boto3_medialive.literals import ReservationSpecialFeature
```

Values:

- `ADVANCED_AUDIO`
- `AUDIO_NORMALIZATION`

## ReservationState

```python
from mypy_boto3_medialive.literals import ReservationState
```

Values:

- `ACTIVE`
- `CANCELED`
- `DELETED`
- `EXPIRED`

## ReservationVideoQuality

```python
from mypy_boto3_medialive.literals import ReservationVideoQuality
```

Values:

- `ENHANCED`
- `PREMIUM`
- `STANDARD`

## RtmpAdMarkers

```python
from mypy_boto3_medialive.literals import RtmpAdMarkers
```

Values:

- `ON_CUE_POINT_SCTE35`

## RtmpCacheFullBehavior

```python
from mypy_boto3_medialive.literals import RtmpCacheFullBehavior
```

Values:

- `DISCONNECT_IMMEDIATELY`
- `WAIT_FOR_SERVER`

## RtmpCaptionData

```python
from mypy_boto3_medialive.literals import RtmpCaptionData
```

Values:

- `ALL`
- `FIELD1_608`
- `FIELD1_AND_FIELD2_608`

## RtmpOutputCertificateMode

```python
from mypy_boto3_medialive.literals import RtmpOutputCertificateMode
```

Values:

- `SELF_SIGNED`
- `VERIFY_AUTHENTICITY`

## S3CannedAcl

```python
from mypy_boto3_medialive.literals import S3CannedAcl
```

Values:

- `AUTHENTICATED_READ`
- `BUCKET_OWNER_FULL_CONTROL`
- `BUCKET_OWNER_READ`
- `PUBLIC_READ`

## Scte20Convert608To708

```python
from mypy_boto3_medialive.literals import Scte20Convert608To708
```

Values:

- `DISABLED`
- `UPCONVERT`

## Scte35AposNoRegionalBlackoutBehavior

```python
from mypy_boto3_medialive.literals import Scte35AposNoRegionalBlackoutBehavior
```

Values:

- `FOLLOW`
- `IGNORE`

## Scte35AposWebDeliveryAllowedBehavior

```python
from mypy_boto3_medialive.literals import Scte35AposWebDeliveryAllowedBehavior
```

Values:

- `FOLLOW`
- `IGNORE`

## Scte35ArchiveAllowedFlag

```python
from mypy_boto3_medialive.literals import Scte35ArchiveAllowedFlag
```

Values:

- `ARCHIVE_ALLOWED`
- `ARCHIVE_NOT_ALLOWED`

## Scte35DeviceRestrictions

```python
from mypy_boto3_medialive.literals import Scte35DeviceRestrictions
```

Values:

- `NONE`
- `RESTRICT_GROUP0`
- `RESTRICT_GROUP1`
- `RESTRICT_GROUP2`

## Scte35NoRegionalBlackoutFlag

```python
from mypy_boto3_medialive.literals import Scte35NoRegionalBlackoutFlag
```

Values:

- `NO_REGIONAL_BLACKOUT`
- `REGIONAL_BLACKOUT`

## Scte35SegmentationCancelIndicator

```python
from mypy_boto3_medialive.literals import Scte35SegmentationCancelIndicator
```

Values:

- `SEGMENTATION_EVENT_CANCELED`
- `SEGMENTATION_EVENT_NOT_CANCELED`

## Scte35SpliceInsertNoRegionalBlackoutBehavior

```python
from mypy_boto3_medialive.literals import Scte35SpliceInsertNoRegionalBlackoutBehavior
```

Values:

- `FOLLOW`
- `IGNORE`

## Scte35SpliceInsertWebDeliveryAllowedBehavior

```python
from mypy_boto3_medialive.literals import Scte35SpliceInsertWebDeliveryAllowedBehavior
```

Values:

- `FOLLOW`
- `IGNORE`

## Scte35WebDeliveryAllowedFlag

```python
from mypy_boto3_medialive.literals import Scte35WebDeliveryAllowedFlag
```

Values:

- `WEB_DELIVERY_ALLOWED`
- `WEB_DELIVERY_NOT_ALLOWED`

## SmoothGroupAudioOnlyTimecodeControl

```python
from mypy_boto3_medialive.literals import SmoothGroupAudioOnlyTimecodeControl
```

Values:

- `PASSTHROUGH`
- `USE_CONFIGURED_CLOCK`

## SmoothGroupCertificateMode

```python
from mypy_boto3_medialive.literals import SmoothGroupCertificateMode
```

Values:

- `SELF_SIGNED`
- `VERIFY_AUTHENTICITY`

## SmoothGroupEventIdMode

```python
from mypy_boto3_medialive.literals import SmoothGroupEventIdMode
```

Values:

- `NO_EVENT_ID`
- `USE_CONFIGURED`
- `USE_TIMESTAMP`

## SmoothGroupEventStopBehavior

```python
from mypy_boto3_medialive.literals import SmoothGroupEventStopBehavior
```

Values:

- `NONE`
- `SEND_EOS`

## SmoothGroupSegmentationMode

```python
from mypy_boto3_medialive.literals import SmoothGroupSegmentationMode
```

Values:

- `USE_INPUT_SEGMENTATION`
- `USE_SEGMENT_DURATION`

## SmoothGroupSparseTrackType

```python
from mypy_boto3_medialive.literals import SmoothGroupSparseTrackType
```

Values:

- `NONE`
- `SCTE_35`
- `SCTE_35_WITHOUT_SEGMENTATION`

## SmoothGroupStreamManifestBehavior

```python
from mypy_boto3_medialive.literals import SmoothGroupStreamManifestBehavior
```

Values:

- `DO_NOT_SEND`
- `SEND`

## SmoothGroupTimestampOffsetMode

```python
from mypy_boto3_medialive.literals import SmoothGroupTimestampOffsetMode
```

Values:

- `USE_CONFIGURED_OFFSET`
- `USE_EVENT_START_DATE`

## Smpte2038DataPreference

```python
from mypy_boto3_medialive.literals import Smpte2038DataPreference
```

Values:

- `IGNORE`
- `PREFER`

## TemporalFilterPostFilterSharpening

```python
from mypy_boto3_medialive.literals import TemporalFilterPostFilterSharpening
```

Values:

- `AUTO`
- `DISABLED`
- `ENABLED`

## TemporalFilterStrength

```python
from mypy_boto3_medialive.literals import TemporalFilterStrength
```

Values:

- `AUTO`
- `STRENGTH_1`
- `STRENGTH_10`
- `STRENGTH_11`
- `STRENGTH_12`
- `STRENGTH_13`
- `STRENGTH_14`
- `STRENGTH_15`
- `STRENGTH_16`
- `STRENGTH_2`
- `STRENGTH_3`
- `STRENGTH_4`
- `STRENGTH_5`
- `STRENGTH_6`
- `STRENGTH_7`
- `STRENGTH_8`
- `STRENGTH_9`

## TimecodeConfigSource

```python
from mypy_boto3_medialive.literals import TimecodeConfigSource
```

Values:

- `EMBEDDED`
- `SYSTEMCLOCK`
- `ZEROBASED`

## TtmlDestinationStyleControl

```python
from mypy_boto3_medialive.literals import TtmlDestinationStyleControl
```

Values:

- `PASSTHROUGH`
- `USE_CONFIGURED`

## UdpTimedMetadataId3Frame

```python
from mypy_boto3_medialive.literals import UdpTimedMetadataId3Frame
```

Values:

- `NONE`
- `PRIV`
- `TDRL`

## VideoDescriptionRespondToAfd

```python
from mypy_boto3_medialive.literals import VideoDescriptionRespondToAfd
```

Values:

- `NONE`
- `PASSTHROUGH`
- `RESPOND`

## VideoDescriptionScalingBehavior

```python
from mypy_boto3_medialive.literals import VideoDescriptionScalingBehavior
```

Values:

- `DEFAULT`
- `STRETCH_TO_OUTPUT`

## VideoSelectorColorSpace

```python
from mypy_boto3_medialive.literals import VideoSelectorColorSpace
```

Values:

- `FOLLOW`
- `HDR10`
- `HLG_2020`
- `REC_601`
- `REC_709`

## VideoSelectorColorSpaceUsage

```python
from mypy_boto3_medialive.literals import VideoSelectorColorSpaceUsage
```

Values:

- `FALLBACK`
- `FORCE`

## WavCodingMode

```python
from mypy_boto3_medialive.literals import WavCodingMode
```

Values:

- `CODING_MODE_1_0`
- `CODING_MODE_2_0`
- `CODING_MODE_4_0`
- `CODING_MODE_8_0`
