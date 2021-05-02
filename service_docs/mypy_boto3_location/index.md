# Type annotations for boto3 LocationService module

> [Index](../index.md) > LocationService

Auto-generated documentation for [LocationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService)
type annotations stubs module [mypy_boto3_location](https://pypi.org/project/mypy-boto3-location/).

```bash
pip install mypy-boto3-location
```

- [Type annotations for boto3 LocationService module](#type-annotations-for-boto3-locationservice-module)
  - [LocationServiceClient](#locationserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## LocationServiceClient

Type annotations for  `boto3.client("location")` as [LocationServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_location.client import LocationServiceClient
```


LocationServiceClient [exceptions](./client.md#exceptions)



### Methods
- [associate_tracker_consumer](./client.md#associate-tracker-consumer)
- [batch_delete_geofence](./client.md#batch-delete-geofence)
- [batch_evaluate_geofences](./client.md#batch-evaluate-geofences)
- [batch_get_device_position](./client.md#batch-get-device-position)
- [batch_put_geofence](./client.md#batch-put-geofence)
- [batch_update_device_position](./client.md#batch-update-device-position)
- [can_paginate](./client.md#can-paginate)
- [create_geofence_collection](./client.md#create-geofence-collection)
- [create_map](./client.md#create-map)
- [create_place_index](./client.md#create-place-index)
- [create_tracker](./client.md#create-tracker)
- [delete_geofence_collection](./client.md#delete-geofence-collection)
- [delete_map](./client.md#delete-map)
- [delete_place_index](./client.md#delete-place-index)
- [delete_tracker](./client.md#delete-tracker)
- [describe_geofence_collection](./client.md#describe-geofence-collection)
- [describe_map](./client.md#describe-map)
- [describe_place_index](./client.md#describe-place-index)
- [describe_tracker](./client.md#describe-tracker)
- [disassociate_tracker_consumer](./client.md#disassociate-tracker-consumer)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_device_position](./client.md#get-device-position)
- [get_device_position_history](./client.md#get-device-position-history)
- [get_geofence](./client.md#get-geofence)
- [get_map_glyphs](./client.md#get-map-glyphs)
- [get_map_sprites](./client.md#get-map-sprites)
- [get_map_style_descriptor](./client.md#get-map-style-descriptor)
- [get_map_tile](./client.md#get-map-tile)
- [get_paginator](./client.md#get-paginator)
- [list_geofence_collections](./client.md#list-geofence-collections)
- [list_geofences](./client.md#list-geofences)
- [list_maps](./client.md#list-maps)
- [list_place_indexes](./client.md#list-place-indexes)
- [list_tracker_consumers](./client.md#list-tracker-consumers)
- [list_trackers](./client.md#list-trackers)
- [put_geofence](./client.md#put-geofence)
- [search_place_index_for_position](./client.md#search-place-index-for-position)
- [search_place_index_for_text](./client.md#search-place-index-for-text)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("location").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_location.paginators import GetDevicePositionHistoryPaginator, ...
```

- [GetDevicePositionHistoryPaginator](./paginators.md#getdevicepositionhistorypaginator)
- [ListGeofenceCollectionsPaginator](./paginators.md#listgeofencecollectionspaginator)
- [ListGeofencesPaginator](./paginators.md#listgeofencespaginator)
- [ListMapsPaginator](./paginators.md#listmapspaginator)
- [ListPlaceIndexesPaginator](./paginators.md#listplaceindexespaginator)
- [ListTrackerConsumersPaginator](./paginators.md#listtrackerconsumerspaginator)
- [ListTrackersPaginator](./paginators.md#listtrackerspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_location.literals import BatchItemErrorCode, ...
```

- [BatchItemErrorCode](./literals.md#batchitemerrorcode)
- [GetDevicePositionHistoryPaginatorName](./literals.md#getdevicepositionhistorypaginatorname)
- [IntendedUse](./literals.md#intendeduse)
- [ListGeofenceCollectionsPaginatorName](./literals.md#listgeofencecollectionspaginatorname)
- [ListGeofencesPaginatorName](./literals.md#listgeofencespaginatorname)
- [ListMapsPaginatorName](./literals.md#listmapspaginatorname)
- [ListPlaceIndexesPaginatorName](./literals.md#listplaceindexespaginatorname)
- [ListTrackerConsumersPaginatorName](./literals.md#listtrackerconsumerspaginatorname)
- [ListTrackersPaginatorName](./literals.md#listtrackerspaginatorname)
- [PricingPlan](./literals.md#pricingplan)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_location.type_defs import BatchDeleteGeofenceErrorTypeDef, ...
```

- [BatchDeleteGeofenceErrorTypeDef](./type_defs.md#batchdeletegeofenceerrortypedef)
- [BatchEvaluateGeofencesErrorTypeDef](./type_defs.md#batchevaluategeofenceserrortypedef)
- [BatchGetDevicePositionErrorTypeDef](./type_defs.md#batchgetdevicepositionerrortypedef)
- [BatchItemErrorTypeDef](./type_defs.md#batchitemerrortypedef)
- [BatchPutGeofenceErrorTypeDef](./type_defs.md#batchputgeofenceerrortypedef)
- [BatchPutGeofenceSuccessTypeDef](./type_defs.md#batchputgeofencesuccesstypedef)
- [BatchUpdateDevicePositionErrorTypeDef](./type_defs.md#batchupdatedevicepositionerrortypedef)
- [DataSourceConfigurationTypeDef](./type_defs.md#datasourceconfigurationtypedef)
- [DevicePositionTypeDef](./type_defs.md#devicepositiontypedef)
- [GeofenceGeometryTypeDef](./type_defs.md#geofencegeometrytypedef)
- [ListGeofenceCollectionsResponseEntryTypeDef](./type_defs.md#listgeofencecollectionsresponseentrytypedef)
- [ListGeofenceResponseEntryTypeDef](./type_defs.md#listgeofenceresponseentrytypedef)
- [ListMapsResponseEntryTypeDef](./type_defs.md#listmapsresponseentrytypedef)
- [ListPlaceIndexesResponseEntryTypeDef](./type_defs.md#listplaceindexesresponseentrytypedef)
- [ListTrackersResponseEntryTypeDef](./type_defs.md#listtrackersresponseentrytypedef)
- [MapConfigurationTypeDef](./type_defs.md#mapconfigurationtypedef)
- [PlaceGeometryTypeDef](./type_defs.md#placegeometrytypedef)
- [PlaceTypeDef](./type_defs.md#placetypedef)
- [SearchForPositionResultTypeDef](./type_defs.md#searchforpositionresulttypedef)
- [SearchForTextResultTypeDef](./type_defs.md#searchfortextresulttypedef)
- [SearchPlaceIndexForPositionSummaryTypeDef](./type_defs.md#searchplaceindexforpositionsummarytypedef)
- [SearchPlaceIndexForTextSummaryTypeDef](./type_defs.md#searchplaceindexfortextsummarytypedef)
- [BatchDeleteGeofenceResponseTypeDef](./type_defs.md#batchdeletegeofenceresponsetypedef)
- [BatchEvaluateGeofencesResponseTypeDef](./type_defs.md#batchevaluategeofencesresponsetypedef)
- [BatchGetDevicePositionResponseTypeDef](./type_defs.md#batchgetdevicepositionresponsetypedef)
- [BatchPutGeofenceRequestEntryTypeDef](./type_defs.md#batchputgeofencerequestentrytypedef)
- [BatchPutGeofenceResponseTypeDef](./type_defs.md#batchputgeofenceresponsetypedef)
- [BatchUpdateDevicePositionResponseTypeDef](./type_defs.md#batchupdatedevicepositionresponsetypedef)
- [CreateGeofenceCollectionResponseTypeDef](./type_defs.md#creategeofencecollectionresponsetypedef)
- [CreateMapResponseTypeDef](./type_defs.md#createmapresponsetypedef)
- [CreatePlaceIndexResponseTypeDef](./type_defs.md#createplaceindexresponsetypedef)
- [CreateTrackerResponseTypeDef](./type_defs.md#createtrackerresponsetypedef)
- [DescribeGeofenceCollectionResponseTypeDef](./type_defs.md#describegeofencecollectionresponsetypedef)
- [DescribeMapResponseTypeDef](./type_defs.md#describemapresponsetypedef)
- [DescribePlaceIndexResponseTypeDef](./type_defs.md#describeplaceindexresponsetypedef)
- [DescribeTrackerResponseTypeDef](./type_defs.md#describetrackerresponsetypedef)
- [DevicePositionUpdateTypeDef](./type_defs.md#devicepositionupdatetypedef)
- [GetDevicePositionHistoryResponseTypeDef](./type_defs.md#getdevicepositionhistoryresponsetypedef)
- [GetDevicePositionResponseTypeDef](./type_defs.md#getdevicepositionresponsetypedef)
- [GetGeofenceResponseTypeDef](./type_defs.md#getgeofenceresponsetypedef)
- [GetMapGlyphsResponseTypeDef](./type_defs.md#getmapglyphsresponsetypedef)
- [GetMapSpritesResponseTypeDef](./type_defs.md#getmapspritesresponsetypedef)
- [GetMapStyleDescriptorResponseTypeDef](./type_defs.md#getmapstyledescriptorresponsetypedef)
- [GetMapTileResponseTypeDef](./type_defs.md#getmaptileresponsetypedef)
- [ListGeofenceCollectionsResponseTypeDef](./type_defs.md#listgeofencecollectionsresponsetypedef)
- [ListGeofencesResponseTypeDef](./type_defs.md#listgeofencesresponsetypedef)
- [ListMapsResponseTypeDef](./type_defs.md#listmapsresponsetypedef)
- [ListPlaceIndexesResponseTypeDef](./type_defs.md#listplaceindexesresponsetypedef)
- [ListTrackerConsumersResponseTypeDef](./type_defs.md#listtrackerconsumersresponsetypedef)
- [ListTrackersResponseTypeDef](./type_defs.md#listtrackersresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutGeofenceResponseTypeDef](./type_defs.md#putgeofenceresponsetypedef)
- [SearchPlaceIndexForPositionResponseTypeDef](./type_defs.md#searchplaceindexforpositionresponsetypedef)
- [SearchPlaceIndexForTextResponseTypeDef](./type_defs.md#searchplaceindexfortextresponsetypedef)
