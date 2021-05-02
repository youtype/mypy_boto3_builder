# GroundStationClient for boto3 GroundStation module

> [Index](../index.md) > [GroundStation](./index.md) > GroundStationClient

Auto-generated documentation for [GroundStation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation)
type annotations stubs module [mypy_boto3_groundstation](https://pypi.org/project/mypy-boto3-groundstation/).

- [GroundStationClient for boto3 GroundStation module](#groundstationclient-for-boto3-groundstation-module)
  - [GroundStationClient](#groundstationclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_contact](#cancel_contact)
    - [create_config](#create_config)
    - [create_dataflow_endpoint_group](#create_dataflow_endpoint_group)
    - [create_mission_profile](#create_mission_profile)
    - [delete_config](#delete_config)
    - [delete_dataflow_endpoint_group](#delete_dataflow_endpoint_group)
    - [delete_mission_profile](#delete_mission_profile)
    - [describe_contact](#describe_contact)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_config](#get_config)
    - [get_dataflow_endpoint_group](#get_dataflow_endpoint_group)
    - [get_minute_usage](#get_minute_usage)
    - [get_mission_profile](#get_mission_profile)
    - [get_satellite](#get_satellite)
    - [list_configs](#list_configs)
    - [list_contacts](#list_contacts)
    - [list_dataflow_endpoint_groups](#list_dataflow_endpoint_groups)
    - [list_ground_stations](#list_ground_stations)
    - [list_mission_profiles](#list_mission_profiles)
    - [list_satellites](#list_satellites)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [reserve_contact](#reserve_contact)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_config](#update_config)
    - [update_mission_profile](#update_mission_profile)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)

## GroundStationClient

Type annotations for `boto3.client("groundstation")`

Can be used directly:

```python
from mypy_boto3_groundstation.client import GroundStationClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_groundstation.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DependencyException`
- `Exceptions.InvalidParameterException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("groundstation").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_contact

Type annotations for `boto3.client("groundstation").cancel_contact` method.

[Client.cancel_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.cancel_contact)

```python
def cancel_contact(
    self,
    contactId: str
) -> ContactIdResponseTypeDef:
    pass
```

### create_config

Type annotations for `boto3.client("groundstation").create_config` method.

[Client.create_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.create_config)

```python
def create_config(
    self,
    configData: "ConfigTypeDataTypeDef",
    name: str,
    tags: Dict[str, str] = None
) -> ConfigIdResponseTypeDef:
    pass
```

### create_dataflow_endpoint_group

Type annotations for `boto3.client("groundstation").create_dataflow_endpoint_group` method.

[Client.create_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.create_dataflow_endpoint_group)

```python
def create_dataflow_endpoint_group(
    self,
    endpointDetails: List["EndpointDetailsTypeDef"],
    tags: Dict[str, str] = None
) -> DataflowEndpointGroupIdResponseTypeDef:
    pass
```

### create_mission_profile

Type annotations for `boto3.client("groundstation").create_mission_profile` method.

[Client.create_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.create_mission_profile)

```python
def create_mission_profile(
    self,
    dataflowEdges: List[List[str]],
    minimumViableContactDurationSeconds: int,
    name: str,
    trackingConfigArn: str,
    contactPostPassDurationSeconds: int = None,
    contactPrePassDurationSeconds: int = None,
    tags: Dict[str, str] = None
) -> MissionProfileIdResponseTypeDef:
    pass
```

### delete_config

Type annotations for `boto3.client("groundstation").delete_config` method.

[Client.delete_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.delete_config)

```python
def delete_config(
    self,
    configId: str,
    configType: ConfigCapabilityType
) -> ConfigIdResponseTypeDef:
    pass
```

### delete_dataflow_endpoint_group

Type annotations for `boto3.client("groundstation").delete_dataflow_endpoint_group` method.

[Client.delete_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.delete_dataflow_endpoint_group)

```python
def delete_dataflow_endpoint_group(
    self,
    dataflowEndpointGroupId: str
) -> DataflowEndpointGroupIdResponseTypeDef:
    pass
```

### delete_mission_profile

Type annotations for `boto3.client("groundstation").delete_mission_profile` method.

[Client.delete_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.delete_mission_profile)

```python
def delete_mission_profile(
    self,
    missionProfileId: str
) -> MissionProfileIdResponseTypeDef:
    pass
```

### describe_contact

Type annotations for `boto3.client("groundstation").describe_contact` method.

[Client.describe_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.describe_contact)

```python
def describe_contact(
    self,
    contactId: str
) -> DescribeContactResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("groundstation").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_config

Type annotations for `boto3.client("groundstation").get_config` method.

[Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.get_config)

```python
def get_config(
    self,
    configId: str,
    configType: ConfigCapabilityType
) -> GetConfigResponseTypeDef:
    pass
```

### get_dataflow_endpoint_group

Type annotations for `boto3.client("groundstation").get_dataflow_endpoint_group` method.

[Client.get_dataflow_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.get_dataflow_endpoint_group)

```python
def get_dataflow_endpoint_group(
    self,
    dataflowEndpointGroupId: str
) -> GetDataflowEndpointGroupResponseTypeDef:
    pass
```

### get_minute_usage

Type annotations for `boto3.client("groundstation").get_minute_usage` method.

[Client.get_minute_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.get_minute_usage)

```python
def get_minute_usage(
    self,
    month: int,
    year: int
) -> GetMinuteUsageResponseTypeDef:
    pass
```

### get_mission_profile

Type annotations for `boto3.client("groundstation").get_mission_profile` method.

[Client.get_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.get_mission_profile)

```python
def get_mission_profile(
    self,
    missionProfileId: str
) -> GetMissionProfileResponseTypeDef:
    pass
```

### get_satellite

Type annotations for `boto3.client("groundstation").get_satellite` method.

[Client.get_satellite documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.get_satellite)

```python
def get_satellite(
    self,
    satelliteId: str
) -> GetSatelliteResponseTypeDef:
    pass
```

### list_configs

Type annotations for `boto3.client("groundstation").list_configs` method.

[Client.list_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_configs)

```python
def list_configs(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListConfigsResponseTypeDef:
    pass
```

### list_contacts

Type annotations for `boto3.client("groundstation").list_contacts` method.

[Client.list_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_contacts)

```python
def list_contacts(
    self,
    endTime: datetime,
    startTime: datetime,
    statusList: List[ContactStatus],
    groundStation: str = None,
    maxResults: int = None,
    missionProfileArn: str = None,
    nextToken: str = None,
    satelliteArn: str = None
) -> ListContactsResponseTypeDef:
    pass
```

### list_dataflow_endpoint_groups

Type annotations for `boto3.client("groundstation").list_dataflow_endpoint_groups` method.

[Client.list_dataflow_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_dataflow_endpoint_groups)

```python
def list_dataflow_endpoint_groups(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListDataflowEndpointGroupsResponseTypeDef:
    pass
```

### list_ground_stations

Type annotations for `boto3.client("groundstation").list_ground_stations` method.

[Client.list_ground_stations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_ground_stations)

```python
def list_ground_stations(
    self,
    maxResults: int = None,
    nextToken: str = None,
    satelliteId: str = None
) -> ListGroundStationsResponseTypeDef:
    pass
```

### list_mission_profiles

Type annotations for `boto3.client("groundstation").list_mission_profiles` method.

[Client.list_mission_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_mission_profiles)

```python
def list_mission_profiles(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListMissionProfilesResponseTypeDef:
    pass
```

### list_satellites

Type annotations for `boto3.client("groundstation").list_satellites` method.

[Client.list_satellites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_satellites)

```python
def list_satellites(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListSatellitesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("groundstation").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### reserve_contact

Type annotations for `boto3.client("groundstation").reserve_contact` method.

[Client.reserve_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.reserve_contact)

```python
def reserve_contact(
    self,
    endTime: datetime,
    groundStation: str,
    missionProfileArn: str,
    satelliteArn: str,
    startTime: datetime,
    tags: Dict[str, str] = None
) -> ContactIdResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("groundstation").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("groundstation").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_config

Type annotations for `boto3.client("groundstation").update_config` method.

[Client.update_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.update_config)

```python
def update_config(
    self,
    configData: "ConfigTypeDataTypeDef",
    configId: str,
    configType: ConfigCapabilityType,
    name: str
) -> ConfigIdResponseTypeDef:
    pass
```

### update_mission_profile

Type annotations for `boto3.client("groundstation").update_mission_profile` method.

[Client.update_mission_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Client.update_mission_profile)

```python
def update_mission_profile(
    self,
    missionProfileId: str,
    contactPostPassDurationSeconds: int = None,
    contactPrePassDurationSeconds: int = None,
    dataflowEdges: List[List[str]] = None,
    minimumViableContactDurationSeconds: int = None,
    name: str = None,
    trackingConfigArn: str = None
) -> MissionProfileIdResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("groundstation").get_paginator` method.

[Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListConfigsPaginatorName
) -> ListConfigsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("groundstation").get_paginator` method.

[Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListContactsPaginatorName
) -> ListContactsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("groundstation").get_paginator` method.

[Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDataflowEndpointGroupsPaginatorName
) -> ListDataflowEndpointGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("groundstation").get_paginator` method.

[Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGroundStationsPaginatorName
) -> ListGroundStationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("groundstation").get_paginator` method.

[Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMissionProfilesPaginatorName
) -> ListMissionProfilesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("groundstation").get_paginator` method.

[Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSatellitesPaginatorName
) -> ListSatellitesPaginator:
    pass
```