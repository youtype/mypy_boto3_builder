# LocationServiceClient for boto3 LocationService module

> [Index](../index.md) > [LocationService](./index.md) > LocationServiceClient

Auto-generated documentation for [LocationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService)
type annotations stubs module [mypy_boto3_location](https://pypi.org/project/mypy-boto3-location/).

- [LocationServiceClient for boto3 LocationService module](#locationserviceclient-for-boto3-locationservice-module)
  - [LocationServiceClient](#locationserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_tracker_consumer](#associate_tracker_consumer)
    - [batch_delete_geofence](#batch_delete_geofence)
    - [batch_evaluate_geofences](#batch_evaluate_geofences)
    - [batch_get_device_position](#batch_get_device_position)
    - [batch_put_geofence](#batch_put_geofence)
    - [batch_update_device_position](#batch_update_device_position)
    - [can_paginate](#can_paginate)
    - [create_geofence_collection](#create_geofence_collection)
    - [create_map](#create_map)
    - [create_place_index](#create_place_index)
    - [create_tracker](#create_tracker)
    - [delete_geofence_collection](#delete_geofence_collection)
    - [delete_map](#delete_map)
    - [delete_place_index](#delete_place_index)
    - [delete_tracker](#delete_tracker)
    - [describe_geofence_collection](#describe_geofence_collection)
    - [describe_map](#describe_map)
    - [describe_place_index](#describe_place_index)
    - [describe_tracker](#describe_tracker)
    - [disassociate_tracker_consumer](#disassociate_tracker_consumer)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_device_position](#get_device_position)
    - [get_device_position_history](#get_device_position_history)
    - [get_geofence](#get_geofence)
    - [get_map_glyphs](#get_map_glyphs)
    - [get_map_sprites](#get_map_sprites)
    - [get_map_style_descriptor](#get_map_style_descriptor)
    - [get_map_tile](#get_map_tile)
    - [list_geofence_collections](#list_geofence_collections)
    - [list_geofences](#list_geofences)
    - [list_maps](#list_maps)
    - [list_place_indexes](#list_place_indexes)
    - [list_tracker_consumers](#list_tracker_consumers)
    - [list_trackers](#list_trackers)
    - [put_geofence](#put_geofence)
    - [search_place_index_for_position](#search_place_index_for_position)
    - [search_place_index_for_text](#search_place_index_for_text)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## LocationServiceClient

Type annotations for `boto3.client("location")`

Can be used directly:

```python
from mypy_boto3_location.client import LocationServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_location.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### associate_tracker_consumer

Type annotations for `boto3.client("location").associate_tracker_consumer` method.

[Client.associate_tracker_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.associate_tracker_consumer)

```python
def associate_tracker_consumer(
    self,
    ConsumerArn: str,
    TrackerName: str
) -> Dict[str, Any]:
    pass
```

### batch_delete_geofence

Type annotations for `boto3.client("location").batch_delete_geofence` method.

[Client.batch_delete_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.batch_delete_geofence)

```python
def batch_delete_geofence(
    self,
    CollectionName: str,
    GeofenceIds: List[str]
) -> BatchDeleteGeofenceResponseTypeDef:
    pass
```

### batch_evaluate_geofences

Type annotations for `boto3.client("location").batch_evaluate_geofences` method.

[Client.batch_evaluate_geofences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.batch_evaluate_geofences)

```python
def batch_evaluate_geofences(
    self,
    CollectionName: str,
    DevicePositionUpdates: List[DevicePositionUpdateTypeDef]
) -> BatchEvaluateGeofencesResponseTypeDef:
    pass
```

### batch_get_device_position

Type annotations for `boto3.client("location").batch_get_device_position` method.

[Client.batch_get_device_position documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.batch_get_device_position)

```python
def batch_get_device_position(
    self,
    DeviceIds: List[str],
    TrackerName: str
) -> BatchGetDevicePositionResponseTypeDef:
    pass
```

### batch_put_geofence

Type annotations for `boto3.client("location").batch_put_geofence` method.

[Client.batch_put_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.batch_put_geofence)

```python
def batch_put_geofence(
    self,
    CollectionName: str,
    Entries: List[BatchPutGeofenceRequestEntryTypeDef]
) -> BatchPutGeofenceResponseTypeDef:
    pass
```

### batch_update_device_position

Type annotations for `boto3.client("location").batch_update_device_position` method.

[Client.batch_update_device_position documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.batch_update_device_position)

```python
def batch_update_device_position(
    self,
    TrackerName: str,
    Updates: List[DevicePositionUpdateTypeDef]
) -> BatchUpdateDevicePositionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("location").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_geofence_collection

Type annotations for `boto3.client("location").create_geofence_collection` method.

[Client.create_geofence_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.create_geofence_collection)

```python
def create_geofence_collection(
    self,
    CollectionName: str,
    PricingPlan: PricingPlan,
    Description: str = None,
    PricingPlanDataSource: str = None
) -> CreateGeofenceCollectionResponseTypeDef:
    pass
```

### create_map

Type annotations for `boto3.client("location").create_map` method.

[Client.create_map documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.create_map)

```python
def create_map(
    self,
    Configuration: "MapConfigurationTypeDef",
    MapName: str,
    PricingPlan: PricingPlan,
    Description: str = None
) -> CreateMapResponseTypeDef:
    pass
```

### create_place_index

Type annotations for `boto3.client("location").create_place_index` method.

[Client.create_place_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.create_place_index)

```python
def create_place_index(
    self,
    DataSource: str,
    IndexName: str,
    PricingPlan: PricingPlan,
    DataSourceConfiguration: "DataSourceConfigurationTypeDef" = None,
    Description: str = None
) -> CreatePlaceIndexResponseTypeDef:
    pass
```

### create_tracker

Type annotations for `boto3.client("location").create_tracker` method.

[Client.create_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.create_tracker)

```python
def create_tracker(
    self,
    PricingPlan: PricingPlan,
    TrackerName: str,
    Description: str = None,
    PricingPlanDataSource: str = None
) -> CreateTrackerResponseTypeDef:
    pass
```

### delete_geofence_collection

Type annotations for `boto3.client("location").delete_geofence_collection` method.

[Client.delete_geofence_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.delete_geofence_collection)

```python
def delete_geofence_collection(
    self,
    CollectionName: str
) -> Dict[str, Any]:
    pass
```

### delete_map

Type annotations for `boto3.client("location").delete_map` method.

[Client.delete_map documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.delete_map)

```python
def delete_map(
    self,
    MapName: str
) -> Dict[str, Any]:
    pass
```

### delete_place_index

Type annotations for `boto3.client("location").delete_place_index` method.

[Client.delete_place_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.delete_place_index)

```python
def delete_place_index(
    self,
    IndexName: str
) -> Dict[str, Any]:
    pass
```

### delete_tracker

Type annotations for `boto3.client("location").delete_tracker` method.

[Client.delete_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.delete_tracker)

```python
def delete_tracker(
    self,
    TrackerName: str
) -> Dict[str, Any]:
    pass
```

### describe_geofence_collection

Type annotations for `boto3.client("location").describe_geofence_collection` method.

[Client.describe_geofence_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.describe_geofence_collection)

```python
def describe_geofence_collection(
    self,
    CollectionName: str
) -> DescribeGeofenceCollectionResponseTypeDef:
    pass
```

### describe_map

Type annotations for `boto3.client("location").describe_map` method.

[Client.describe_map documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.describe_map)

```python
def describe_map(
    self,
    MapName: str
) -> DescribeMapResponseTypeDef:
    pass
```

### describe_place_index

Type annotations for `boto3.client("location").describe_place_index` method.

[Client.describe_place_index documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.describe_place_index)

```python
def describe_place_index(
    self,
    IndexName: str
) -> DescribePlaceIndexResponseTypeDef:
    pass
```

### describe_tracker

Type annotations for `boto3.client("location").describe_tracker` method.

[Client.describe_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.describe_tracker)

```python
def describe_tracker(
    self,
    TrackerName: str
) -> DescribeTrackerResponseTypeDef:
    pass
```

### disassociate_tracker_consumer

Type annotations for `boto3.client("location").disassociate_tracker_consumer` method.

[Client.disassociate_tracker_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.disassociate_tracker_consumer)

```python
def disassociate_tracker_consumer(
    self,
    ConsumerArn: str,
    TrackerName: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("location").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.generate_presigned_url)

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

### get_device_position

Type annotations for `boto3.client("location").get_device_position` method.

[Client.get_device_position documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_device_position)

```python
def get_device_position(
    self,
    DeviceId: str,
    TrackerName: str
) -> GetDevicePositionResponseTypeDef:
    pass
```

### get_device_position_history

Type annotations for `boto3.client("location").get_device_position_history` method.

[Client.get_device_position_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_device_position_history)

```python
def get_device_position_history(
    self,
    DeviceId: str,
    TrackerName: str,
    EndTimeExclusive: datetime = None,
    NextToken: str = None,
    StartTimeInclusive: datetime = None
) -> GetDevicePositionHistoryResponseTypeDef:
    pass
```

### get_geofence

Type annotations for `boto3.client("location").get_geofence` method.

[Client.get_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_geofence)

```python
def get_geofence(
    self,
    CollectionName: str,
    GeofenceId: str
) -> GetGeofenceResponseTypeDef:
    pass
```

### get_map_glyphs

Type annotations for `boto3.client("location").get_map_glyphs` method.

[Client.get_map_glyphs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_map_glyphs)

```python
def get_map_glyphs(
    self,
    FontStack: str,
    FontUnicodeRange: str,
    MapName: str
) -> GetMapGlyphsResponseTypeDef:
    pass
```

### get_map_sprites

Type annotations for `boto3.client("location").get_map_sprites` method.

[Client.get_map_sprites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_map_sprites)

```python
def get_map_sprites(
    self,
    FileName: str,
    MapName: str
) -> GetMapSpritesResponseTypeDef:
    pass
```

### get_map_style_descriptor

Type annotations for `boto3.client("location").get_map_style_descriptor` method.

[Client.get_map_style_descriptor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_map_style_descriptor)

```python
def get_map_style_descriptor(
    self,
    MapName: str
) -> GetMapStyleDescriptorResponseTypeDef:
    pass
```

### get_map_tile

Type annotations for `boto3.client("location").get_map_tile` method.

[Client.get_map_tile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.get_map_tile)

```python
def get_map_tile(
    self,
    MapName: str,
    X: str,
    Y: str,
    Z: str
) -> GetMapTileResponseTypeDef:
    pass
```

### list_geofence_collections

Type annotations for `boto3.client("location").list_geofence_collections` method.

[Client.list_geofence_collections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.list_geofence_collections)

```python
def list_geofence_collections(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListGeofenceCollectionsResponseTypeDef:
    pass
```

### list_geofences

Type annotations for `boto3.client("location").list_geofences` method.

[Client.list_geofences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.list_geofences)

```python
def list_geofences(
    self,
    CollectionName: str,
    NextToken: str = None
) -> ListGeofencesResponseTypeDef:
    pass
```

### list_maps

Type annotations for `boto3.client("location").list_maps` method.

[Client.list_maps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.list_maps)

```python
def list_maps(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListMapsResponseTypeDef:
    pass
```

### list_place_indexes

Type annotations for `boto3.client("location").list_place_indexes` method.

[Client.list_place_indexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.list_place_indexes)

```python
def list_place_indexes(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPlaceIndexesResponseTypeDef:
    pass
```

### list_tracker_consumers

Type annotations for `boto3.client("location").list_tracker_consumers` method.

[Client.list_tracker_consumers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.list_tracker_consumers)

```python
def list_tracker_consumers(
    self,
    TrackerName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTrackerConsumersResponseTypeDef:
    pass
```

### list_trackers

Type annotations for `boto3.client("location").list_trackers` method.

[Client.list_trackers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.list_trackers)

```python
def list_trackers(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTrackersResponseTypeDef:
    pass
```

### put_geofence

Type annotations for `boto3.client("location").put_geofence` method.

[Client.put_geofence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.put_geofence)

```python
def put_geofence(
    self,
    CollectionName: str,
    GeofenceId: str,
    Geometry: "GeofenceGeometryTypeDef"
) -> PutGeofenceResponseTypeDef:
    pass
```

### search_place_index_for_position

Type annotations for `boto3.client("location").search_place_index_for_position` method.

[Client.search_place_index_for_position documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.search_place_index_for_position)

```python
def search_place_index_for_position(
    self,
    IndexName: str,
    Position: List[float],
    MaxResults: int = None
) -> SearchPlaceIndexForPositionResponseTypeDef:
    pass
```

### search_place_index_for_text

Type annotations for `boto3.client("location").search_place_index_for_text` method.

[Client.search_place_index_for_text documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Client.search_place_index_for_text)

```python
def search_place_index_for_text(
    self,
    IndexName: str,
    Text: str,
    BiasPosition: List[float] = None,
    FilterBBox: List[float] = None,
    FilterCountries: List[str] = None,
    MaxResults: int = None
) -> SearchPlaceIndexForTextResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.GetDevicePositionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDevicePositionHistoryPaginatorName
) -> GetDevicePositionHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.ListGeofenceCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGeofenceCollectionsPaginatorName
) -> ListGeofenceCollectionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.ListGeofences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListGeofences)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGeofencesPaginatorName
) -> ListGeofencesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.ListMaps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListMaps)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMapsPaginatorName
) -> ListMapsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.ListPlaceIndexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPlaceIndexesPaginatorName
) -> ListPlaceIndexesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.ListTrackerConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTrackerConsumersPaginatorName
) -> ListTrackerConsumersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("location").get_paginator` method.

[Paginator.ListTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService.Paginator.ListTrackers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTrackersPaginatorName
) -> ListTrackersPaginator:
    pass
```