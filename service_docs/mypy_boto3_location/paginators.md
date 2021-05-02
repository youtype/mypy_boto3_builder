# Paginators for boto3 LocationService module

> [Index](../index.md) > [LocationService](./index.md) > Paginators

Auto-generated documentation for [LocationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService)
type annotations stubs module [mypy_boto3_location](https://pypi.org/project/mypy-boto3-location/).

- [Paginators for boto3 LocationService module](#paginators-for-boto3-locationservice-module)
  - [GetDevicePositionHistoryPaginator](#getdevicepositionhistorypaginator)
  - [ListGeofenceCollectionsPaginator](#listgeofencecollectionspaginator)
  - [ListGeofencesPaginator](#listgeofencespaginator)
  - [ListMapsPaginator](#listmapspaginator)
  - [ListPlaceIndexesPaginator](#listplaceindexespaginator)
  - [ListTrackerConsumersPaginator](#listtrackerconsumerspaginator)
  - [ListTrackersPaginator](#listtrackerspaginator)

## GetDevicePositionHistoryPaginator

Type annotations for `boto3.client("location").get_paginator("get_device_position_history")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import GetDevicePositionHistoryPaginator

def get_get_device_position_history_paginator() -> GetDevicePositionHistoryPaginator:
    return boto3.client("location").get_paginator("get_device_position_history")
```

[Paginator.GetDevicePositionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)

```python
class GetDevicePositionHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        DeviceId: str,
        TrackerName: str,
        EndTimeExclusive: datetime = None,
        StartTimeInclusive: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDevicePositionHistoryResponseTypeDef]:
        pass
```
## ListGeofenceCollectionsPaginator

Type annotations for `boto3.client("location").get_paginator("list_geofence_collections")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import ListGeofenceCollectionsPaginator

def get_list_geofence_collections_paginator() -> ListGeofenceCollectionsPaginator:
    return boto3.client("location").get_paginator("list_geofence_collections")
```

[Paginator.ListGeofenceCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)

```python
class ListGeofenceCollectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeofenceCollectionsResponseTypeDef]:
        pass
```
## ListGeofencesPaginator

Type annotations for `boto3.client("location").get_paginator("list_geofences")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import ListGeofencesPaginator

def get_list_geofences_paginator() -> ListGeofencesPaginator:
    return boto3.client("location").get_paginator("list_geofences")
```

[Paginator.ListGeofences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListGeofences)

```python
class ListGeofencesPaginator(Boto3Paginator):
    def paginate(
        self,
        CollectionName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGeofencesResponseTypeDef]:
        pass
```
## ListMapsPaginator

Type annotations for `boto3.client("location").get_paginator("list_maps")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import ListMapsPaginator

def get_list_maps_paginator() -> ListMapsPaginator:
    return boto3.client("location").get_paginator("list_maps")
```

[Paginator.ListMaps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListMaps)

```python
class ListMapsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMapsResponseTypeDef]:
        pass
```
## ListPlaceIndexesPaginator

Type annotations for `boto3.client("location").get_paginator("list_place_indexes")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import ListPlaceIndexesPaginator

def get_list_place_indexes_paginator() -> ListPlaceIndexesPaginator:
    return boto3.client("location").get_paginator("list_place_indexes")
```

[Paginator.ListPlaceIndexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)

```python
class ListPlaceIndexesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlaceIndexesResponseTypeDef]:
        pass
```
## ListTrackerConsumersPaginator

Type annotations for `boto3.client("location").get_paginator("list_tracker_consumers")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import ListTrackerConsumersPaginator

def get_list_tracker_consumers_paginator() -> ListTrackerConsumersPaginator:
    return boto3.client("location").get_paginator("list_tracker_consumers")
```

[Paginator.ListTrackerConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)

```python
class ListTrackerConsumersPaginator(Boto3Paginator):
    def paginate(
        self,
        TrackerName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrackerConsumersResponseTypeDef]:
        pass
```
## ListTrackersPaginator

Type annotations for `boto3.client("location").get_paginator("list_trackers")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import ListTrackersPaginator

def get_list_trackers_paginator() -> ListTrackersPaginator:
    return boto3.client("location").get_paginator("list_trackers")
```

[Paginator.ListTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListTrackers)

```python
class ListTrackersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTrackersResponseTypeDef]:
        pass
```