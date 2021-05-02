# Literals for boto3 MediaPackage module

> [Index](../index.md) > [MediaPackage](./index.md) > Literals

Auto-generated documentation for [MediaPackage](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html#MediaPackage)
type annotations stubs module [mypy_boto3_mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/).

- [Literals for boto3 MediaPackage module](#literals-for-boto3-mediapackage-module)
  - [AdMarkers](#admarkers)
  - [AdsOnDeliveryRestrictions](#adsondeliveryrestrictions)
  - [EncryptionMethod](#encryptionmethod)
  - [ListChannelsPaginatorName](#listchannelspaginatorname)
  - [ListHarvestJobsPaginatorName](#listharvestjobspaginatorname)
  - [ListOriginEndpointsPaginatorName](#listoriginendpointspaginatorname)
  - [ManifestLayout](#manifestlayout)
  - [Origination](#origination)
  - [PlaylistType](#playlisttype)
  - [PresetSpeke20Audio](#presetspeke20audio)
  - [PresetSpeke20Video](#presetspeke20video)
  - [Profile](#profile)
  - [SegmentTemplateFormat](#segmenttemplateformat)
  - [Status](#status)
  - [StreamOrder](#streamorder)
  - [UtcTiming](#utctiming)
  - [__AdTriggersElement](#__adtriggerselement)
  - [__PeriodTriggersElement](#__periodtriggerselement)

## AdMarkers

```python
from mypy_boto3_mediapackage.literals import AdMarkers
```

Values:

- `DATERANGE`
- `NONE`
- `PASSTHROUGH`
- `SCTE35_ENHANCED`

## AdsOnDeliveryRestrictions

```python
from mypy_boto3_mediapackage.literals import AdsOnDeliveryRestrictions
```

Values:

- `BOTH`
- `NONE`
- `RESTRICTED`
- `UNRESTRICTED`

## EncryptionMethod

```python
from mypy_boto3_mediapackage.literals import EncryptionMethod
```

Values:

- `AES_128`
- `SAMPLE_AES`

## ListChannelsPaginatorName

```python
from mypy_boto3_mediapackage.literals import ListChannelsPaginatorName
```

Values:

- `list_channels`

## ListHarvestJobsPaginatorName

```python
from mypy_boto3_mediapackage.literals import ListHarvestJobsPaginatorName
```

Values:

- `list_harvest_jobs`

## ListOriginEndpointsPaginatorName

```python
from mypy_boto3_mediapackage.literals import ListOriginEndpointsPaginatorName
```

Values:

- `list_origin_endpoints`

## ManifestLayout

```python
from mypy_boto3_mediapackage.literals import ManifestLayout
```

Values:

- `COMPACT`
- `FULL`

## Origination

```python
from mypy_boto3_mediapackage.literals import Origination
```

Values:

- `ALLOW`
- `DENY`

## PlaylistType

```python
from mypy_boto3_mediapackage.literals import PlaylistType
```

Values:

- `EVENT`
- `NONE`
- `VOD`

## PresetSpeke20Audio

```python
from mypy_boto3_mediapackage.literals import PresetSpeke20Audio
```

Values:

- `PRESET-AUDIO-1`

## PresetSpeke20Video

```python
from mypy_boto3_mediapackage.literals import PresetSpeke20Video
```

Values:

- `PRESET-VIDEO-1`

## Profile

```python
from mypy_boto3_mediapackage.literals import Profile
```

Values:

- `HBBTV_1_5`
- `NONE`

## SegmentTemplateFormat

```python
from mypy_boto3_mediapackage.literals import SegmentTemplateFormat
```

Values:

- `NUMBER_WITH_DURATION`
- `NUMBER_WITH_TIMELINE`
- `TIME_WITH_TIMELINE`

## Status

```python
from mypy_boto3_mediapackage.literals import Status
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`

## StreamOrder

```python
from mypy_boto3_mediapackage.literals import StreamOrder
```

Values:

- `ORIGINAL`
- `VIDEO_BITRATE_ASCENDING`
- `VIDEO_BITRATE_DESCENDING`

## UtcTiming

```python
from mypy_boto3_mediapackage.literals import UtcTiming
```

Values:

- `HTTP-HEAD`
- `HTTP-ISO`
- `NONE`

## __AdTriggersElement

```python
from mypy_boto3_mediapackage.literals import __AdTriggersElement
```

Values:

- `BREAK`
- `DISTRIBUTOR_ADVERTISEMENT`
- `DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY`
- `DISTRIBUTOR_PLACEMENT_OPPORTUNITY`
- `PROVIDER_ADVERTISEMENT`
- `PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY`
- `PROVIDER_PLACEMENT_OPPORTUNITY`
- `SPLICE_INSERT`

## __PeriodTriggersElement

```python
from mypy_boto3_mediapackage.literals import __PeriodTriggersElement
```

Values:

- `ADS`
