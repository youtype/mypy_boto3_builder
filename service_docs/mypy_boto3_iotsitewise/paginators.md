# Paginators for boto3 IoTSiteWise module

> [Index](../index.md) > [IoTSiteWise](./index.md) > Paginators

Auto-generated documentation for [IoTSiteWise](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise)
type annotations stubs module [mypy_boto3_iotsitewise](https://pypi.org/project/mypy-boto3-iotsitewise/).

- [Paginators for boto3 IoTSiteWise module](#paginators-for-boto3-iotsitewise-module)
  - [GetAssetPropertyAggregatesPaginator](#getassetpropertyaggregatespaginator)
  - [GetAssetPropertyValueHistoryPaginator](#getassetpropertyvaluehistorypaginator)
  - [GetInterpolatedAssetPropertyValuesPaginator](#getinterpolatedassetpropertyvaluespaginator)
  - [ListAccessPoliciesPaginator](#listaccesspoliciespaginator)
  - [ListAssetModelsPaginator](#listassetmodelspaginator)
  - [ListAssetRelationshipsPaginator](#listassetrelationshipspaginator)
  - [ListAssetsPaginator](#listassetspaginator)
  - [ListAssociatedAssetsPaginator](#listassociatedassetspaginator)
  - [ListDashboardsPaginator](#listdashboardspaginator)
  - [ListGatewaysPaginator](#listgatewayspaginator)
  - [ListPortalsPaginator](#listportalspaginator)
  - [ListProjectAssetsPaginator](#listprojectassetspaginator)
  - [ListProjectsPaginator](#listprojectspaginator)

## GetAssetPropertyAggregatesPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("get_asset_property_aggregates")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import GetAssetPropertyAggregatesPaginator

def get_get_asset_property_aggregates_paginator() -> GetAssetPropertyAggregatesPaginator:
    return boto3.client("iotsitewise").get_paginator("get_asset_property_aggregates")
```

[Paginator.GetAssetPropertyAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)

```python
class GetAssetPropertyAggregatesPaginator(Boto3Paginator):
    def paginate(
        self,
        aggregateTypes: List[AggregateType],
        resolution: str,
        startDate: datetime,
        endDate: datetime,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        qualities: List[Quality] = None,
        timeOrdering: TimeOrdering = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAssetPropertyAggregatesResponseTypeDef]:
        pass
```
## GetAssetPropertyValueHistoryPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("get_asset_property_value_history")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import GetAssetPropertyValueHistoryPaginator

def get_get_asset_property_value_history_paginator() -> GetAssetPropertyValueHistoryPaginator:
    return boto3.client("iotsitewise").get_paginator("get_asset_property_value_history")
```

[Paginator.GetAssetPropertyValueHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)

```python
class GetAssetPropertyValueHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        startDate: datetime = None,
        endDate: datetime = None,
        qualities: List[Quality] = None,
        timeOrdering: TimeOrdering = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAssetPropertyValueHistoryResponseTypeDef]:
        pass
```
## GetInterpolatedAssetPropertyValuesPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("get_interpolated_asset_property_values")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import GetInterpolatedAssetPropertyValuesPaginator

def get_get_interpolated_asset_property_values_paginator() -> GetInterpolatedAssetPropertyValuesPaginator:
    return boto3.client("iotsitewise").get_paginator("get_interpolated_asset_property_values")
```

[Paginator.GetInterpolatedAssetPropertyValues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues)

```python
class GetInterpolatedAssetPropertyValuesPaginator(Boto3Paginator):
    def paginate(
        self,
        startTimeInSeconds: int,
        endTimeInSeconds: int,
        quality: Quality,
        intervalInSeconds: int,
        type: str,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        startTimeOffsetInNanos: int = None,
        endTimeOffsetInNanos: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInterpolatedAssetPropertyValuesResponseTypeDef]:
        pass
```
## ListAccessPoliciesPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_access_policies")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListAccessPoliciesPaginator

def get_list_access_policies_paginator() -> ListAccessPoliciesPaginator:
    return boto3.client("iotsitewise").get_paginator("list_access_policies")
```

[Paginator.ListAccessPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies)

```python
class ListAccessPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        identityType: IdentityType = None,
        identityId: str = None,
        resourceType: ResourceType = None,
        resourceId: str = None,
        iamArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessPoliciesResponseTypeDef]:
        pass
```
## ListAssetModelsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_asset_models")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListAssetModelsPaginator

def get_list_asset_models_paginator() -> ListAssetModelsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_asset_models")
```

[Paginator.ListAssetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels)

```python
class ListAssetModelsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetModelsResponseTypeDef]:
        pass
```
## ListAssetRelationshipsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_asset_relationships")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListAssetRelationshipsPaginator

def get_list_asset_relationships_paginator() -> ListAssetRelationshipsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_asset_relationships")
```

[Paginator.ListAssetRelationships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetRelationships)

```python
class ListAssetRelationshipsPaginator(Boto3Paginator):
    def paginate(
        self,
        assetId: str,
        traversalType: TraversalType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetRelationshipsResponseTypeDef]:
        pass
```
## ListAssetsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_assets")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListAssetsPaginator

def get_list_assets_paginator() -> ListAssetsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_assets")
```

[Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets)

```python
class ListAssetsPaginator(Boto3Paginator):
    def paginate(
        self,
        assetModelId: str = None,
        filter: ListAssetsFilter = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetsResponseTypeDef]:
        pass
```
## ListAssociatedAssetsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_associated_assets")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListAssociatedAssetsPaginator

def get_list_associated_assets_paginator() -> ListAssociatedAssetsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_associated_assets")
```

[Paginator.ListAssociatedAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets)

```python
class ListAssociatedAssetsPaginator(Boto3Paginator):
    def paginate(
        self,
        assetId: str,
        hierarchyId: str = None,
        traversalDirection: TraversalDirection = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedAssetsResponseTypeDef]:
        pass
```
## ListDashboardsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_dashboards")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListDashboardsPaginator

def get_list_dashboards_paginator() -> ListDashboardsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_dashboards")
```

[Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards)

```python
class ListDashboardsPaginator(Boto3Paginator):
    def paginate(
        self,
        projectId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsResponseTypeDef]:
        pass
```
## ListGatewaysPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_gateways")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListGatewaysPaginator

def get_list_gateways_paginator() -> ListGatewaysPaginator:
    return boto3.client("iotsitewise").get_paginator("list_gateways")
```

[Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways)

```python
class ListGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGatewaysResponseTypeDef]:
        pass
```
## ListPortalsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_portals")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListPortalsPaginator

def get_list_portals_paginator() -> ListPortalsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_portals")
```

[Paginator.ListPortals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals)

```python
class ListPortalsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPortalsResponseTypeDef]:
        pass
```
## ListProjectAssetsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_project_assets")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListProjectAssetsPaginator

def get_list_project_assets_paginator() -> ListProjectAssetsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_project_assets")
```

[Paginator.ListProjectAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets)

```python
class ListProjectAssetsPaginator(Boto3Paginator):
    def paginate(
        self,
        projectId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectAssetsResponseTypeDef]:
        pass
```
## ListProjectsPaginator

Type annotations for `boto3.client("iotsitewise").get_paginator("list_projects")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import ListProjectsPaginator

def get_list_projects_paginator() -> ListProjectsPaginator:
    return boto3.client("iotsitewise").get_paginator("list_projects")
```

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects)

```python
class ListProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        portalId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        pass
```