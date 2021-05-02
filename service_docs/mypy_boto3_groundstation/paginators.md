# Paginators for boto3 GroundStation module

> [Index](../index.md) > [GroundStation](./index.md) > Paginators

Auto-generated documentation for [GroundStation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation)
type annotations stubs module [mypy_boto3_groundstation](https://pypi.org/project/mypy-boto3-groundstation/).

- [Paginators for boto3 GroundStation module](#paginators-for-boto3-groundstation-module)
  - [ListConfigsPaginator](#listconfigspaginator)
  - [ListContactsPaginator](#listcontactspaginator)
  - [ListDataflowEndpointGroupsPaginator](#listdataflowendpointgroupspaginator)
  - [ListGroundStationsPaginator](#listgroundstationspaginator)
  - [ListMissionProfilesPaginator](#listmissionprofilespaginator)
  - [ListSatellitesPaginator](#listsatellitespaginator)

## ListConfigsPaginator

Type annotations for `boto3.client("groundstation").get_paginator("list_configs")`.

Can be used directly:

```python
from mypy_boto3_groundstation.paginators import ListConfigsPaginator

def get_list_configs_paginator() -> ListConfigsPaginator:
    return boto3.client("groundstation").get_paginator("list_configs")
```

[Paginator.ListConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)

```python
class ListConfigsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigsResponseTypeDef]:
        pass
```
## ListContactsPaginator

Type annotations for `boto3.client("groundstation").get_paginator("list_contacts")`.

Can be used directly:

```python
from mypy_boto3_groundstation.paginators import ListContactsPaginator

def get_list_contacts_paginator() -> ListContactsPaginator:
    return boto3.client("groundstation").get_paginator("list_contacts")
```

[Paginator.ListContacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)

```python
class ListContactsPaginator(Boto3Paginator):
    def paginate(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[ContactStatus],
        groundStation: str = None,
        missionProfileArn: str = None,
        satelliteArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContactsResponseTypeDef]:
        pass
```
## ListDataflowEndpointGroupsPaginator

Type annotations for `boto3.client("groundstation").get_paginator("list_dataflow_endpoint_groups")`.

Can be used directly:

```python
from mypy_boto3_groundstation.paginators import ListDataflowEndpointGroupsPaginator

def get_list_dataflow_endpoint_groups_paginator() -> ListDataflowEndpointGroupsPaginator:
    return boto3.client("groundstation").get_paginator("list_dataflow_endpoint_groups")
```

[Paginator.ListDataflowEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)

```python
class ListDataflowEndpointGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataflowEndpointGroupsResponseTypeDef]:
        pass
```
## ListGroundStationsPaginator

Type annotations for `boto3.client("groundstation").get_paginator("list_ground_stations")`.

Can be used directly:

```python
from mypy_boto3_groundstation.paginators import ListGroundStationsPaginator

def get_list_ground_stations_paginator() -> ListGroundStationsPaginator:
    return boto3.client("groundstation").get_paginator("list_ground_stations")
```

[Paginator.ListGroundStations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)

```python
class ListGroundStationsPaginator(Boto3Paginator):
    def paginate(
        self,
        satelliteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroundStationsResponseTypeDef]:
        pass
```
## ListMissionProfilesPaginator

Type annotations for `boto3.client("groundstation").get_paginator("list_mission_profiles")`.

Can be used directly:

```python
from mypy_boto3_groundstation.paginators import ListMissionProfilesPaginator

def get_list_mission_profiles_paginator() -> ListMissionProfilesPaginator:
    return boto3.client("groundstation").get_paginator("list_mission_profiles")
```

[Paginator.ListMissionProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)

```python
class ListMissionProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMissionProfilesResponseTypeDef]:
        pass
```
## ListSatellitesPaginator

Type annotations for `boto3.client("groundstation").get_paginator("list_satellites")`.

Can be used directly:

```python
from mypy_boto3_groundstation.paginators import ListSatellitesPaginator

def get_list_satellites_paginator() -> ListSatellitesPaginator:
    return boto3.client("groundstation").get_paginator("list_satellites")
```

[Paginator.ListSatellites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)

```python
class ListSatellitesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSatellitesResponseTypeDef]:
        pass
```