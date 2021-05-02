# Literals for boto3 GroundStation module

> [Index](../index.md) > [GroundStation](./index.md) > Literals

Auto-generated documentation for [GroundStation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation)
type annotations stubs module [mypy_boto3_groundstation](https://pypi.org/project/mypy-boto3-groundstation/).

- [Literals for boto3 GroundStation module](#literals-for-boto3-groundstation-module)
  - [AngleUnits](#angleunits)
  - [BandwidthUnits](#bandwidthunits)
  - [ConfigCapabilityType](#configcapabilitytype)
  - [ContactStatus](#contactstatus)
  - [Criticality](#criticality)
  - [EirpUnits](#eirpunits)
  - [EndpointStatus](#endpointstatus)
  - [FrequencyUnits](#frequencyunits)
  - [ListConfigsPaginatorName](#listconfigspaginatorname)
  - [ListContactsPaginatorName](#listcontactspaginatorname)
  - [ListDataflowEndpointGroupsPaginatorName](#listdataflowendpointgroupspaginatorname)
  - [ListGroundStationsPaginatorName](#listgroundstationspaginatorname)
  - [ListMissionProfilesPaginatorName](#listmissionprofilespaginatorname)
  - [ListSatellitesPaginatorName](#listsatellitespaginatorname)
  - [Polarization](#polarization)

## AngleUnits

```python
from mypy_boto3_groundstation.literals import AngleUnits
```

Values:

- `DEGREE_ANGLE`
- `RADIAN`

## BandwidthUnits

```python
from mypy_boto3_groundstation.literals import BandwidthUnits
```

Values:

- `GHz`
- `kHz`
- `MHz`

## ConfigCapabilityType

```python
from mypy_boto3_groundstation.literals import ConfigCapabilityType
```

Values:

- `antenna-downlink`
- `antenna-downlink-demod-decode`
- `antenna-uplink`
- `dataflow-endpoint`
- `s3-recording`
- `tracking`
- `uplink-echo`

## ContactStatus

```python
from mypy_boto3_groundstation.literals import ContactStatus
```

Values:

- `AVAILABLE`
- `AWS_CANCELLED`
- `AWS_FAILED`
- `CANCELLED`
- `CANCELLING`
- `COMPLETED`
- `FAILED`
- `FAILED_TO_SCHEDULE`
- `PASS`
- `POSTPASS`
- `PREPASS`
- `SCHEDULED`
- `SCHEDULING`

## Criticality

```python
from mypy_boto3_groundstation.literals import Criticality
```

Values:

- `PREFERRED`
- `REMOVED`
- `REQUIRED`

## EirpUnits

```python
from mypy_boto3_groundstation.literals import EirpUnits
```

Values:

- `dBW`

## EndpointStatus

```python
from mypy_boto3_groundstation.literals import EndpointStatus
```

Values:

- `created`
- `creating`
- `deleted`
- `deleting`
- `failed`

## FrequencyUnits

```python
from mypy_boto3_groundstation.literals import FrequencyUnits
```

Values:

- `GHz`
- `kHz`
- `MHz`

## ListConfigsPaginatorName

```python
from mypy_boto3_groundstation.literals import ListConfigsPaginatorName
```

Values:

- `list_configs`

## ListContactsPaginatorName

```python
from mypy_boto3_groundstation.literals import ListContactsPaginatorName
```

Values:

- `list_contacts`

## ListDataflowEndpointGroupsPaginatorName

```python
from mypy_boto3_groundstation.literals import ListDataflowEndpointGroupsPaginatorName
```

Values:

- `list_dataflow_endpoint_groups`

## ListGroundStationsPaginatorName

```python
from mypy_boto3_groundstation.literals import ListGroundStationsPaginatorName
```

Values:

- `list_ground_stations`

## ListMissionProfilesPaginatorName

```python
from mypy_boto3_groundstation.literals import ListMissionProfilesPaginatorName
```

Values:

- `list_mission_profiles`

## ListSatellitesPaginatorName

```python
from mypy_boto3_groundstation.literals import ListSatellitesPaginatorName
```

Values:

- `list_satellites`

## Polarization

```python
from mypy_boto3_groundstation.literals import Polarization
```

Values:

- `LEFT_HAND`
- `NONE`
- `RIGHT_HAND`
