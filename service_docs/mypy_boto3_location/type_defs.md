# Structures for boto3 LocationService module

> [Index](../index.md) > [LocationService](./index.md) > Structures

Auto-generated documentation for [LocationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html#LocationService)
type annotations stubs module [mypy_boto3_location](https://pypi.org/project/mypy-boto3-location/).

- [Structures for boto3 LocationService module](#structures-for-boto3-locationservice-module)
  - [BatchDeleteGeofenceErrorTypeDef](#batchdeletegeofenceerrortypedef)
  - [BatchEvaluateGeofencesErrorTypeDef](#batchevaluategeofenceserrortypedef)
  - [BatchGetDevicePositionErrorTypeDef](#batchgetdevicepositionerrortypedef)
  - [BatchItemErrorTypeDef](#batchitemerrortypedef)
  - [BatchPutGeofenceErrorTypeDef](#batchputgeofenceerrortypedef)
  - [BatchPutGeofenceSuccessTypeDef](#batchputgeofencesuccesstypedef)
  - [BatchUpdateDevicePositionErrorTypeDef](#batchupdatedevicepositionerrortypedef)
  - [DataSourceConfigurationTypeDef](#datasourceconfigurationtypedef)
  - [DevicePositionTypeDef](#devicepositiontypedef)
  - [GeofenceGeometryTypeDef](#geofencegeometrytypedef)
  - [ListGeofenceCollectionsResponseEntryTypeDef](#listgeofencecollectionsresponseentrytypedef)
  - [ListGeofenceResponseEntryTypeDef](#listgeofenceresponseentrytypedef)
  - [ListMapsResponseEntryTypeDef](#listmapsresponseentrytypedef)
  - [ListPlaceIndexesResponseEntryTypeDef](#listplaceindexesresponseentrytypedef)
  - [ListTrackersResponseEntryTypeDef](#listtrackersresponseentrytypedef)
  - [MapConfigurationTypeDef](#mapconfigurationtypedef)
  - [PlaceGeometryTypeDef](#placegeometrytypedef)
  - [PlaceTypeDef](#placetypedef)
  - [SearchForPositionResultTypeDef](#searchforpositionresulttypedef)
  - [SearchForTextResultTypeDef](#searchfortextresulttypedef)
  - [SearchPlaceIndexForPositionSummaryTypeDef](#searchplaceindexforpositionsummarytypedef)
  - [SearchPlaceIndexForTextSummaryTypeDef](#searchplaceindexfortextsummarytypedef)
  - [BatchDeleteGeofenceResponseTypeDef](#batchdeletegeofenceresponsetypedef)
  - [BatchEvaluateGeofencesResponseTypeDef](#batchevaluategeofencesresponsetypedef)
  - [BatchGetDevicePositionResponseTypeDef](#batchgetdevicepositionresponsetypedef)
  - [BatchPutGeofenceRequestEntryTypeDef](#batchputgeofencerequestentrytypedef)
  - [BatchPutGeofenceResponseTypeDef](#batchputgeofenceresponsetypedef)
  - [BatchUpdateDevicePositionResponseTypeDef](#batchupdatedevicepositionresponsetypedef)
  - [CreateGeofenceCollectionResponseTypeDef](#creategeofencecollectionresponsetypedef)
  - [CreateMapResponseTypeDef](#createmapresponsetypedef)
  - [CreatePlaceIndexResponseTypeDef](#createplaceindexresponsetypedef)
  - [CreateTrackerResponseTypeDef](#createtrackerresponsetypedef)
  - [DescribeGeofenceCollectionResponseTypeDef](#describegeofencecollectionresponsetypedef)
  - [DescribeMapResponseTypeDef](#describemapresponsetypedef)
  - [DescribePlaceIndexResponseTypeDef](#describeplaceindexresponsetypedef)
  - [DescribeTrackerResponseTypeDef](#describetrackerresponsetypedef)
  - [DevicePositionUpdateTypeDef](#devicepositionupdatetypedef)
  - [GetDevicePositionHistoryResponseTypeDef](#getdevicepositionhistoryresponsetypedef)
  - [GetDevicePositionResponseTypeDef](#getdevicepositionresponsetypedef)
  - [GetGeofenceResponseTypeDef](#getgeofenceresponsetypedef)
  - [GetMapGlyphsResponseTypeDef](#getmapglyphsresponsetypedef)
  - [GetMapSpritesResponseTypeDef](#getmapspritesresponsetypedef)
  - [GetMapStyleDescriptorResponseTypeDef](#getmapstyledescriptorresponsetypedef)
  - [GetMapTileResponseTypeDef](#getmaptileresponsetypedef)
  - [ListGeofenceCollectionsResponseTypeDef](#listgeofencecollectionsresponsetypedef)
  - [ListGeofencesResponseTypeDef](#listgeofencesresponsetypedef)
  - [ListMapsResponseTypeDef](#listmapsresponsetypedef)
  - [ListPlaceIndexesResponseTypeDef](#listplaceindexesresponsetypedef)
  - [ListTrackerConsumersResponseTypeDef](#listtrackerconsumersresponsetypedef)
  - [ListTrackersResponseTypeDef](#listtrackersresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutGeofenceResponseTypeDef](#putgeofenceresponsetypedef)
  - [SearchPlaceIndexForPositionResponseTypeDef](#searchplaceindexforpositionresponsetypedef)
  - [SearchPlaceIndexForTextResponseTypeDef](#searchplaceindexfortextresponsetypedef)

## BatchDeleteGeofenceErrorTypeDef

```python
from mypy_boto3_location.type_defs import BatchDeleteGeofenceErrorTypeDef
```


Required fields:
- `Error`: `"BatchItemErrorTypeDef"`
- `GeofenceId`: `str`




## BatchEvaluateGeofencesErrorTypeDef

```python
from mypy_boto3_location.type_defs import BatchEvaluateGeofencesErrorTypeDef
```


Required fields:
- `DeviceId`: `str`
- `Error`: `"BatchItemErrorTypeDef"`
- `SampleTime`: `datetime`




## BatchGetDevicePositionErrorTypeDef

```python
from mypy_boto3_location.type_defs import BatchGetDevicePositionErrorTypeDef
```


Required fields:
- `DeviceId`: `str`
- `Error`: `"BatchItemErrorTypeDef"`




## BatchItemErrorTypeDef

```python
from mypy_boto3_location.type_defs import BatchItemErrorTypeDef
```




Optional fields:
- `Code`: `BatchItemErrorCode`
- `Message`: `str`


## BatchPutGeofenceErrorTypeDef

```python
from mypy_boto3_location.type_defs import BatchPutGeofenceErrorTypeDef
```


Required fields:
- `Error`: `"BatchItemErrorTypeDef"`
- `GeofenceId`: `str`




## BatchPutGeofenceSuccessTypeDef

```python
from mypy_boto3_location.type_defs import BatchPutGeofenceSuccessTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `GeofenceId`: `str`
- `UpdateTime`: `datetime`




## BatchUpdateDevicePositionErrorTypeDef

```python
from mypy_boto3_location.type_defs import BatchUpdateDevicePositionErrorTypeDef
```


Required fields:
- `DeviceId`: `str`
- `Error`: `"BatchItemErrorTypeDef"`
- `SampleTime`: `datetime`




## DataSourceConfigurationTypeDef

```python
from mypy_boto3_location.type_defs import DataSourceConfigurationTypeDef
```




Optional fields:
- `IntendedUse`: `IntendedUse`


## DevicePositionTypeDef

```python
from mypy_boto3_location.type_defs import DevicePositionTypeDef
```


Required fields:
- `Position`: `List[float]`
- `ReceivedTime`: `datetime`
- `SampleTime`: `datetime`



Optional fields:
- `DeviceId`: `str`


## GeofenceGeometryTypeDef

```python
from mypy_boto3_location.type_defs import GeofenceGeometryTypeDef
```




Optional fields:
- `Polygon`: `List[List[List[float]]]`


## ListGeofenceCollectionsResponseEntryTypeDef

```python
from mypy_boto3_location.type_defs import ListGeofenceCollectionsResponseEntryTypeDef
```


Required fields:
- `CollectionName`: `str`
- `CreateTime`: `datetime`
- `Description`: `str`
- `PricingPlan`: `PricingPlan`
- `UpdateTime`: `datetime`



Optional fields:
- `PricingPlanDataSource`: `str`


## ListGeofenceResponseEntryTypeDef

```python
from mypy_boto3_location.type_defs import ListGeofenceResponseEntryTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `GeofenceId`: `str`
- `Geometry`: `"GeofenceGeometryTypeDef"`
- `Status`: `str`
- `UpdateTime`: `datetime`




## ListMapsResponseEntryTypeDef

```python
from mypy_boto3_location.type_defs import ListMapsResponseEntryTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `DataSource`: `str`
- `Description`: `str`
- `MapName`: `str`
- `PricingPlan`: `PricingPlan`
- `UpdateTime`: `datetime`




## ListPlaceIndexesResponseEntryTypeDef

```python
from mypy_boto3_location.type_defs import ListPlaceIndexesResponseEntryTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `DataSource`: `str`
- `Description`: `str`
- `IndexName`: `str`
- `PricingPlan`: `PricingPlan`
- `UpdateTime`: `datetime`




## ListTrackersResponseEntryTypeDef

```python
from mypy_boto3_location.type_defs import ListTrackersResponseEntryTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `Description`: `str`
- `PricingPlan`: `PricingPlan`
- `TrackerName`: `str`
- `UpdateTime`: `datetime`



Optional fields:
- `PricingPlanDataSource`: `str`


## MapConfigurationTypeDef

```python
from mypy_boto3_location.type_defs import MapConfigurationTypeDef
```


Required fields:
- `Style`: `str`




## PlaceGeometryTypeDef

```python
from mypy_boto3_location.type_defs import PlaceGeometryTypeDef
```




Optional fields:
- `Point`: `List[float]`


## PlaceTypeDef

```python
from mypy_boto3_location.type_defs import PlaceTypeDef
```


Required fields:
- `Geometry`: `"PlaceGeometryTypeDef"`



Optional fields:
- `AddressNumber`: `str`
- `Country`: `str`
- `Label`: `str`
- `Municipality`: `str`
- `Neighborhood`: `str`
- `PostalCode`: `str`
- `Region`: `str`
- `Street`: `str`
- `SubRegion`: `str`


## SearchForPositionResultTypeDef

```python
from mypy_boto3_location.type_defs import SearchForPositionResultTypeDef
```


Required fields:
- `Place`: `"PlaceTypeDef"`




## SearchForTextResultTypeDef

```python
from mypy_boto3_location.type_defs import SearchForTextResultTypeDef
```


Required fields:
- `Place`: `"PlaceTypeDef"`




## SearchPlaceIndexForPositionSummaryTypeDef

```python
from mypy_boto3_location.type_defs import SearchPlaceIndexForPositionSummaryTypeDef
```


Required fields:
- `DataSource`: `str`
- `Position`: `List[float]`



Optional fields:
- `MaxResults`: `int`


## SearchPlaceIndexForTextSummaryTypeDef

```python
from mypy_boto3_location.type_defs import SearchPlaceIndexForTextSummaryTypeDef
```


Required fields:
- `DataSource`: `str`
- `Text`: `str`



Optional fields:
- `BiasPosition`: `List[float]`
- `FilterBBox`: `List[float]`
- `FilterCountries`: `List[str]`
- `MaxResults`: `int`
- `ResultBBox`: `List[float]`


## BatchDeleteGeofenceResponseTypeDef

```python
from mypy_boto3_location.type_defs import BatchDeleteGeofenceResponseTypeDef
```


Required fields:
- `Errors`: `List["BatchDeleteGeofenceErrorTypeDef"]`




## BatchEvaluateGeofencesResponseTypeDef

```python
from mypy_boto3_location.type_defs import BatchEvaluateGeofencesResponseTypeDef
```


Required fields:
- `Errors`: `List["BatchEvaluateGeofencesErrorTypeDef"]`




## BatchGetDevicePositionResponseTypeDef

```python
from mypy_boto3_location.type_defs import BatchGetDevicePositionResponseTypeDef
```


Required fields:
- `DevicePositions`: `List["DevicePositionTypeDef"]`
- `Errors`: `List["BatchGetDevicePositionErrorTypeDef"]`




## BatchPutGeofenceRequestEntryTypeDef

```python
from mypy_boto3_location.type_defs import BatchPutGeofenceRequestEntryTypeDef
```


Required fields:
- `GeofenceId`: `str`
- `Geometry`: `"GeofenceGeometryTypeDef"`




## BatchPutGeofenceResponseTypeDef

```python
from mypy_boto3_location.type_defs import BatchPutGeofenceResponseTypeDef
```


Required fields:
- `Errors`: `List["BatchPutGeofenceErrorTypeDef"]`
- `Successes`: `List["BatchPutGeofenceSuccessTypeDef"]`




## BatchUpdateDevicePositionResponseTypeDef

```python
from mypy_boto3_location.type_defs import BatchUpdateDevicePositionResponseTypeDef
```


Required fields:
- `Errors`: `List["BatchUpdateDevicePositionErrorTypeDef"]`




## CreateGeofenceCollectionResponseTypeDef

```python
from mypy_boto3_location.type_defs import CreateGeofenceCollectionResponseTypeDef
```


Required fields:
- `CollectionArn`: `str`
- `CollectionName`: `str`
- `CreateTime`: `datetime`




## CreateMapResponseTypeDef

```python
from mypy_boto3_location.type_defs import CreateMapResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `MapArn`: `str`
- `MapName`: `str`




## CreatePlaceIndexResponseTypeDef

```python
from mypy_boto3_location.type_defs import CreatePlaceIndexResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `IndexArn`: `str`
- `IndexName`: `str`




## CreateTrackerResponseTypeDef

```python
from mypy_boto3_location.type_defs import CreateTrackerResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `TrackerArn`: `str`
- `TrackerName`: `str`




## DescribeGeofenceCollectionResponseTypeDef

```python
from mypy_boto3_location.type_defs import DescribeGeofenceCollectionResponseTypeDef
```


Required fields:
- `CollectionArn`: `str`
- `CollectionName`: `str`
- `CreateTime`: `datetime`
- `Description`: `str`
- `PricingPlan`: `PricingPlan`
- `UpdateTime`: `datetime`



Optional fields:
- `PricingPlanDataSource`: `str`


## DescribeMapResponseTypeDef

```python
from mypy_boto3_location.type_defs import DescribeMapResponseTypeDef
```


Required fields:
- `Configuration`: `"MapConfigurationTypeDef"`
- `CreateTime`: `datetime`
- `DataSource`: `str`
- `Description`: `str`
- `MapArn`: `str`
- `MapName`: `str`
- `PricingPlan`: `PricingPlan`
- `UpdateTime`: `datetime`




## DescribePlaceIndexResponseTypeDef

```python
from mypy_boto3_location.type_defs import DescribePlaceIndexResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `DataSource`: `str`
- `DataSourceConfiguration`: `"DataSourceConfigurationTypeDef"`
- `Description`: `str`
- `IndexArn`: `str`
- `IndexName`: `str`
- `PricingPlan`: `PricingPlan`
- `UpdateTime`: `datetime`




## DescribeTrackerResponseTypeDef

```python
from mypy_boto3_location.type_defs import DescribeTrackerResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `Description`: `str`
- `PricingPlan`: `PricingPlan`
- `TrackerArn`: `str`
- `TrackerName`: `str`
- `UpdateTime`: `datetime`



Optional fields:
- `PricingPlanDataSource`: `str`


## DevicePositionUpdateTypeDef

```python
from mypy_boto3_location.type_defs import DevicePositionUpdateTypeDef
```


Required fields:
- `DeviceId`: `str`
- `Position`: `List[float]`
- `SampleTime`: `datetime`




## GetDevicePositionHistoryResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetDevicePositionHistoryResponseTypeDef
```


Required fields:
- `DevicePositions`: `List["DevicePositionTypeDef"]`



Optional fields:
- `NextToken`: `str`


## GetDevicePositionResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetDevicePositionResponseTypeDef
```


Required fields:
- `Position`: `List[float]`
- `ReceivedTime`: `datetime`
- `SampleTime`: `datetime`



Optional fields:
- `DeviceId`: `str`


## GetGeofenceResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetGeofenceResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `GeofenceId`: `str`
- `Geometry`: `"GeofenceGeometryTypeDef"`
- `Status`: `str`
- `UpdateTime`: `datetime`




## GetMapGlyphsResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetMapGlyphsResponseTypeDef
```




Optional fields:
- `Blob`: `Union[bytes, IO[bytes]]`
- `ContentType`: `str`


## GetMapSpritesResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetMapSpritesResponseTypeDef
```




Optional fields:
- `Blob`: `Union[bytes, IO[bytes]]`
- `ContentType`: `str`


## GetMapStyleDescriptorResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetMapStyleDescriptorResponseTypeDef
```




Optional fields:
- `Blob`: `Union[bytes, IO[bytes]]`
- `ContentType`: `str`


## GetMapTileResponseTypeDef

```python
from mypy_boto3_location.type_defs import GetMapTileResponseTypeDef
```




Optional fields:
- `Blob`: `Union[bytes, IO[bytes]]`
- `ContentType`: `str`


## ListGeofenceCollectionsResponseTypeDef

```python
from mypy_boto3_location.type_defs import ListGeofenceCollectionsResponseTypeDef
```


Required fields:
- `Entries`: `List["ListGeofenceCollectionsResponseEntryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListGeofencesResponseTypeDef

```python
from mypy_boto3_location.type_defs import ListGeofencesResponseTypeDef
```


Required fields:
- `Entries`: `List["ListGeofenceResponseEntryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListMapsResponseTypeDef

```python
from mypy_boto3_location.type_defs import ListMapsResponseTypeDef
```


Required fields:
- `Entries`: `List["ListMapsResponseEntryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListPlaceIndexesResponseTypeDef

```python
from mypy_boto3_location.type_defs import ListPlaceIndexesResponseTypeDef
```


Required fields:
- `Entries`: `List["ListPlaceIndexesResponseEntryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTrackerConsumersResponseTypeDef

```python
from mypy_boto3_location.type_defs import ListTrackerConsumersResponseTypeDef
```


Required fields:
- `ConsumerArns`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListTrackersResponseTypeDef

```python
from mypy_boto3_location.type_defs import ListTrackersResponseTypeDef
```


Required fields:
- `Entries`: `List["ListTrackersResponseEntryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_location.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutGeofenceResponseTypeDef

```python
from mypy_boto3_location.type_defs import PutGeofenceResponseTypeDef
```


Required fields:
- `CreateTime`: `datetime`
- `GeofenceId`: `str`
- `UpdateTime`: `datetime`




## SearchPlaceIndexForPositionResponseTypeDef

```python
from mypy_boto3_location.type_defs import SearchPlaceIndexForPositionResponseTypeDef
```


Required fields:
- `Results`: `List["SearchForPositionResultTypeDef"]`
- `Summary`: `"SearchPlaceIndexForPositionSummaryTypeDef"`




## SearchPlaceIndexForTextResponseTypeDef

```python
from mypy_boto3_location.type_defs import SearchPlaceIndexForTextResponseTypeDef
```


Required fields:
- `Results`: `List["SearchForTextResultTypeDef"]`
- `Summary`: `"SearchPlaceIndexForTextSummaryTypeDef"`



