# Structures for boto3 GroundStation module

> [Index](../index.md) > [GroundStation](./index.md) > Structures

Auto-generated documentation for [GroundStation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation)
type annotations stubs module [mypy_boto3_groundstation](https://pypi.org/project/mypy-boto3-groundstation/).

- [Structures for boto3 GroundStation module](#structures-for-boto3-groundstation-module)
  - [AntennaDemodDecodeDetailsTypeDef](#antennademoddecodedetailstypedef)
  - [AntennaDownlinkConfigTypeDef](#antennadownlinkconfigtypedef)
  - [AntennaDownlinkDemodDecodeConfigTypeDef](#antennadownlinkdemoddecodeconfigtypedef)
  - [AntennaUplinkConfigTypeDef](#antennauplinkconfigtypedef)
  - [ConfigDetailsTypeDef](#configdetailstypedef)
  - [ConfigListItemTypeDef](#configlistitemtypedef)
  - [ConfigTypeDataTypeDef](#configtypedatatypedef)
  - [ContactDataTypeDef](#contactdatatypedef)
  - [DataflowDetailTypeDef](#dataflowdetailtypedef)
  - [DataflowEndpointConfigTypeDef](#dataflowendpointconfigtypedef)
  - [DataflowEndpointListItemTypeDef](#dataflowendpointlistitemtypedef)
  - [DataflowEndpointTypeDef](#dataflowendpointtypedef)
  - [DecodeConfigTypeDef](#decodeconfigtypedef)
  - [DemodulationConfigTypeDef](#demodulationconfigtypedef)
  - [DestinationTypeDef](#destinationtypedef)
  - [EirpTypeDef](#eirptypedef)
  - [ElevationTypeDef](#elevationtypedef)
  - [EndpointDetailsTypeDef](#endpointdetailstypedef)
  - [FrequencyBandwidthTypeDef](#frequencybandwidthtypedef)
  - [FrequencyTypeDef](#frequencytypedef)
  - [GroundStationDataTypeDef](#groundstationdatatypedef)
  - [MissionProfileListItemTypeDef](#missionprofilelistitemtypedef)
  - [S3RecordingConfigTypeDef](#s3recordingconfigtypedef)
  - [S3RecordingDetailsTypeDef](#s3recordingdetailstypedef)
  - [SatelliteListItemTypeDef](#satellitelistitemtypedef)
  - [SecurityDetailsTypeDef](#securitydetailstypedef)
  - [SocketAddressTypeDef](#socketaddresstypedef)
  - [SourceTypeDef](#sourcetypedef)
  - [SpectrumConfigTypeDef](#spectrumconfigtypedef)
  - [TrackingConfigTypeDef](#trackingconfigtypedef)
  - [UplinkEchoConfigTypeDef](#uplinkechoconfigtypedef)
  - [UplinkSpectrumConfigTypeDef](#uplinkspectrumconfigtypedef)
  - [ConfigIdResponseTypeDef](#configidresponsetypedef)
  - [ContactIdResponseTypeDef](#contactidresponsetypedef)
  - [DataflowEndpointGroupIdResponseTypeDef](#dataflowendpointgroupidresponsetypedef)
  - [DescribeContactResponseTypeDef](#describecontactresponsetypedef)
  - [GetConfigResponseTypeDef](#getconfigresponsetypedef)
  - [GetDataflowEndpointGroupResponseTypeDef](#getdataflowendpointgroupresponsetypedef)
  - [GetMinuteUsageResponseTypeDef](#getminuteusageresponsetypedef)
  - [GetMissionProfileResponseTypeDef](#getmissionprofileresponsetypedef)
  - [GetSatelliteResponseTypeDef](#getsatelliteresponsetypedef)
  - [ListConfigsResponseTypeDef](#listconfigsresponsetypedef)
  - [ListContactsResponseTypeDef](#listcontactsresponsetypedef)
  - [ListDataflowEndpointGroupsResponseTypeDef](#listdataflowendpointgroupsresponsetypedef)
  - [ListGroundStationsResponseTypeDef](#listgroundstationsresponsetypedef)
  - [ListMissionProfilesResponseTypeDef](#listmissionprofilesresponsetypedef)
  - [ListSatellitesResponseTypeDef](#listsatellitesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MissionProfileIdResponseTypeDef](#missionprofileidresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## AntennaDemodDecodeDetailsTypeDef

```python
from mypy_boto3_groundstation.type_defs import AntennaDemodDecodeDetailsTypeDef
```




Optional fields:
- `outputNode`: `str`


## AntennaDownlinkConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import AntennaDownlinkConfigTypeDef
```


Required fields:
- `spectrumConfig`: `"SpectrumConfigTypeDef"`




## AntennaDownlinkDemodDecodeConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import AntennaDownlinkDemodDecodeConfigTypeDef
```


Required fields:
- `decodeConfig`: `"DecodeConfigTypeDef"`
- `demodulationConfig`: `"DemodulationConfigTypeDef"`
- `spectrumConfig`: `"SpectrumConfigTypeDef"`




## AntennaUplinkConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import AntennaUplinkConfigTypeDef
```


Required fields:
- `spectrumConfig`: `"UplinkSpectrumConfigTypeDef"`
- `targetEirp`: `"EirpTypeDef"`



Optional fields:
- `transmitDisabled`: `bool`


## ConfigDetailsTypeDef

```python
from mypy_boto3_groundstation.type_defs import ConfigDetailsTypeDef
```




Optional fields:
- `antennaDemodDecodeDetails`: `"AntennaDemodDecodeDetailsTypeDef"`
- `endpointDetails`: `"EndpointDetailsTypeDef"`
- `s3RecordingDetails`: `"S3RecordingDetailsTypeDef"`


## ConfigListItemTypeDef

```python
from mypy_boto3_groundstation.type_defs import ConfigListItemTypeDef
```




Optional fields:
- `configArn`: `str`
- `configId`: `str`
- `configType`: `ConfigCapabilityType`
- `name`: `str`


## ConfigTypeDataTypeDef

```python
from mypy_boto3_groundstation.type_defs import ConfigTypeDataTypeDef
```




Optional fields:
- `antennaDownlinkConfig`: `"AntennaDownlinkConfigTypeDef"`
- `antennaDownlinkDemodDecodeConfig`: `"AntennaDownlinkDemodDecodeConfigTypeDef"`
- `antennaUplinkConfig`: `"AntennaUplinkConfigTypeDef"`
- `dataflowEndpointConfig`: `"DataflowEndpointConfigTypeDef"`
- `s3RecordingConfig`: `"S3RecordingConfigTypeDef"`
- `trackingConfig`: `"TrackingConfigTypeDef"`
- `uplinkEchoConfig`: `"UplinkEchoConfigTypeDef"`


## ContactDataTypeDef

```python
from mypy_boto3_groundstation.type_defs import ContactDataTypeDef
```




Optional fields:
- `contactId`: `str`
- `contactStatus`: `ContactStatus`
- `endTime`: `datetime`
- `errorMessage`: `str`
- `groundStation`: `str`
- `maximumElevation`: `"ElevationTypeDef"`
- `missionProfileArn`: `str`
- `postPassEndTime`: `datetime`
- `prePassStartTime`: `datetime`
- `region`: `str`
- `satelliteArn`: `str`
- `startTime`: `datetime`
- `tags`: `Dict[str, str]`


## DataflowDetailTypeDef

```python
from mypy_boto3_groundstation.type_defs import DataflowDetailTypeDef
```




Optional fields:
- `destination`: `"DestinationTypeDef"`
- `errorMessage`: `str`
- `source`: `"SourceTypeDef"`


## DataflowEndpointConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import DataflowEndpointConfigTypeDef
```


Required fields:
- `dataflowEndpointName`: `str`



Optional fields:
- `dataflowEndpointRegion`: `str`


## DataflowEndpointListItemTypeDef

```python
from mypy_boto3_groundstation.type_defs import DataflowEndpointListItemTypeDef
```




Optional fields:
- `dataflowEndpointGroupArn`: `str`
- `dataflowEndpointGroupId`: `str`


## DataflowEndpointTypeDef

```python
from mypy_boto3_groundstation.type_defs import DataflowEndpointTypeDef
```




Optional fields:
- `address`: `"SocketAddressTypeDef"`
- `mtu`: `int`
- `name`: `str`
- `status`: `EndpointStatus`


## DecodeConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import DecodeConfigTypeDef
```


Required fields:
- `unvalidatedJSON`: `str`




## DemodulationConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import DemodulationConfigTypeDef
```


Required fields:
- `unvalidatedJSON`: `str`




## DestinationTypeDef

```python
from mypy_boto3_groundstation.type_defs import DestinationTypeDef
```




Optional fields:
- `configDetails`: `"ConfigDetailsTypeDef"`
- `configId`: `str`
- `configType`: `ConfigCapabilityType`
- `dataflowDestinationRegion`: `str`


## EirpTypeDef

```python
from mypy_boto3_groundstation.type_defs import EirpTypeDef
```


Required fields:
- `units`: `EirpUnits`
- `value`: `float`




## ElevationTypeDef

```python
from mypy_boto3_groundstation.type_defs import ElevationTypeDef
```


Required fields:
- `unit`: `AngleUnits`
- `value`: `float`




## EndpointDetailsTypeDef

```python
from mypy_boto3_groundstation.type_defs import EndpointDetailsTypeDef
```




Optional fields:
- `endpoint`: `"DataflowEndpointTypeDef"`
- `securityDetails`: `"SecurityDetailsTypeDef"`


## FrequencyBandwidthTypeDef

```python
from mypy_boto3_groundstation.type_defs import FrequencyBandwidthTypeDef
```


Required fields:
- `units`: `BandwidthUnits`
- `value`: `float`




## FrequencyTypeDef

```python
from mypy_boto3_groundstation.type_defs import FrequencyTypeDef
```


Required fields:
- `units`: `FrequencyUnits`
- `value`: `float`




## GroundStationDataTypeDef

```python
from mypy_boto3_groundstation.type_defs import GroundStationDataTypeDef
```




Optional fields:
- `groundStationId`: `str`
- `groundStationName`: `str`
- `region`: `str`


## MissionProfileListItemTypeDef

```python
from mypy_boto3_groundstation.type_defs import MissionProfileListItemTypeDef
```




Optional fields:
- `missionProfileArn`: `str`
- `missionProfileId`: `str`
- `name`: `str`
- `region`: `str`


## S3RecordingConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import S3RecordingConfigTypeDef
```


Required fields:
- `bucketArn`: `str`
- `roleArn`: `str`



Optional fields:
- `prefix`: `str`


## S3RecordingDetailsTypeDef

```python
from mypy_boto3_groundstation.type_defs import S3RecordingDetailsTypeDef
```




Optional fields:
- `bucketArn`: `str`
- `keyTemplate`: `str`


## SatelliteListItemTypeDef

```python
from mypy_boto3_groundstation.type_defs import SatelliteListItemTypeDef
```




Optional fields:
- `groundStations`: `List[str]`
- `noradSatelliteID`: `int`
- `satelliteArn`: `str`
- `satelliteId`: `str`


## SecurityDetailsTypeDef

```python
from mypy_boto3_groundstation.type_defs import SecurityDetailsTypeDef
```


Required fields:
- `roleArn`: `str`
- `securityGroupIds`: `List[str]`
- `subnetIds`: `List[str]`




## SocketAddressTypeDef

```python
from mypy_boto3_groundstation.type_defs import SocketAddressTypeDef
```


Required fields:
- `name`: `str`
- `port`: `int`




## SourceTypeDef

```python
from mypy_boto3_groundstation.type_defs import SourceTypeDef
```




Optional fields:
- `configDetails`: `"ConfigDetailsTypeDef"`
- `configId`: `str`
- `configType`: `ConfigCapabilityType`
- `dataflowSourceRegion`: `str`


## SpectrumConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import SpectrumConfigTypeDef
```


Required fields:
- `bandwidth`: `"FrequencyBandwidthTypeDef"`
- `centerFrequency`: `"FrequencyTypeDef"`



Optional fields:
- `polarization`: `Polarization`


## TrackingConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import TrackingConfigTypeDef
```


Required fields:
- `autotrack`: `Criticality`




## UplinkEchoConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import UplinkEchoConfigTypeDef
```


Required fields:
- `antennaUplinkConfigArn`: `str`
- `enabled`: `bool`




## UplinkSpectrumConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import UplinkSpectrumConfigTypeDef
```


Required fields:
- `centerFrequency`: `"FrequencyTypeDef"`



Optional fields:
- `polarization`: `Polarization`


## ConfigIdResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ConfigIdResponseTypeDef
```




Optional fields:
- `configArn`: `str`
- `configId`: `str`
- `configType`: `ConfigCapabilityType`


## ContactIdResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ContactIdResponseTypeDef
```




Optional fields:
- `contactId`: `str`


## DataflowEndpointGroupIdResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import DataflowEndpointGroupIdResponseTypeDef
```




Optional fields:
- `dataflowEndpointGroupId`: `str`


## DescribeContactResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import DescribeContactResponseTypeDef
```




Optional fields:
- `contactId`: `str`
- `contactStatus`: `ContactStatus`
- `dataflowList`: `List["DataflowDetailTypeDef"]`
- `endTime`: `datetime`
- `errorMessage`: `str`
- `groundStation`: `str`
- `maximumElevation`: `"ElevationTypeDef"`
- `missionProfileArn`: `str`
- `postPassEndTime`: `datetime`
- `prePassStartTime`: `datetime`
- `region`: `str`
- `satelliteArn`: `str`
- `startTime`: `datetime`
- `tags`: `Dict[str, str]`


## GetConfigResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import GetConfigResponseTypeDef
```


Required fields:
- `configArn`: `str`
- `configData`: `"ConfigTypeDataTypeDef"`
- `configId`: `str`
- `name`: `str`



Optional fields:
- `configType`: `ConfigCapabilityType`
- `tags`: `Dict[str, str]`


## GetDataflowEndpointGroupResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import GetDataflowEndpointGroupResponseTypeDef
```




Optional fields:
- `dataflowEndpointGroupArn`: `str`
- `dataflowEndpointGroupId`: `str`
- `endpointsDetails`: `List["EndpointDetailsTypeDef"]`
- `tags`: `Dict[str, str]`


## GetMinuteUsageResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import GetMinuteUsageResponseTypeDef
```




Optional fields:
- `estimatedMinutesRemaining`: `int`
- `isReservedMinutesCustomer`: `bool`
- `totalReservedMinuteAllocation`: `int`
- `totalScheduledMinutes`: `int`
- `upcomingMinutesScheduled`: `int`


## GetMissionProfileResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import GetMissionProfileResponseTypeDef
```




Optional fields:
- `contactPostPassDurationSeconds`: `int`
- `contactPrePassDurationSeconds`: `int`
- `dataflowEdges`: `List[List[str]]`
- `minimumViableContactDurationSeconds`: `int`
- `missionProfileArn`: `str`
- `missionProfileId`: `str`
- `name`: `str`
- `region`: `str`
- `tags`: `Dict[str, str]`
- `trackingConfigArn`: `str`


## GetSatelliteResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import GetSatelliteResponseTypeDef
```




Optional fields:
- `groundStations`: `List[str]`
- `noradSatelliteID`: `int`
- `satelliteArn`: `str`
- `satelliteId`: `str`


## ListConfigsResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListConfigsResponseTypeDef
```




Optional fields:
- `configList`: `List["ConfigListItemTypeDef"]`
- `nextToken`: `str`


## ListContactsResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListContactsResponseTypeDef
```




Optional fields:
- `contactList`: `List["ContactDataTypeDef"]`
- `nextToken`: `str`


## ListDataflowEndpointGroupsResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListDataflowEndpointGroupsResponseTypeDef
```




Optional fields:
- `dataflowEndpointGroupList`: `List["DataflowEndpointListItemTypeDef"]`
- `nextToken`: `str`


## ListGroundStationsResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListGroundStationsResponseTypeDef
```




Optional fields:
- `groundStationList`: `List["GroundStationDataTypeDef"]`
- `nextToken`: `str`


## ListMissionProfilesResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListMissionProfilesResponseTypeDef
```




Optional fields:
- `missionProfileList`: `List["MissionProfileListItemTypeDef"]`
- `nextToken`: `str`


## ListSatellitesResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListSatellitesResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `satellites`: `List["SatelliteListItemTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## MissionProfileIdResponseTypeDef

```python
from mypy_boto3_groundstation.type_defs import MissionProfileIdResponseTypeDef
```




Optional fields:
- `missionProfileId`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_groundstation.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

