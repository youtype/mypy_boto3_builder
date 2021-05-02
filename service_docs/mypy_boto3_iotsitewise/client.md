# IoTSiteWiseClient for boto3 IoTSiteWise module

> [Index](../index.md) > [IoTSiteWise](./index.md) > IoTSiteWiseClient

Auto-generated documentation for [IoTSiteWise](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise)
type annotations stubs module [mypy_boto3_iotsitewise](https://pypi.org/project/mypy-boto3-iotsitewise/).

- [IoTSiteWiseClient for boto3 IoTSiteWise module](#iotsitewiseclient-for-boto3-iotsitewise-module)
  - [IoTSiteWiseClient](#iotsitewiseclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_assets](#associate_assets)
    - [batch_associate_project_assets](#batch_associate_project_assets)
    - [batch_disassociate_project_assets](#batch_disassociate_project_assets)
    - [batch_put_asset_property_value](#batch_put_asset_property_value)
    - [can_paginate](#can_paginate)
    - [create_access_policy](#create_access_policy)
    - [create_asset](#create_asset)
    - [create_asset_model](#create_asset_model)
    - [create_dashboard](#create_dashboard)
    - [create_gateway](#create_gateway)
    - [create_portal](#create_portal)
    - [create_project](#create_project)
    - [delete_access_policy](#delete_access_policy)
    - [delete_asset](#delete_asset)
    - [delete_asset_model](#delete_asset_model)
    - [delete_dashboard](#delete_dashboard)
    - [delete_gateway](#delete_gateway)
    - [delete_portal](#delete_portal)
    - [delete_project](#delete_project)
    - [describe_access_policy](#describe_access_policy)
    - [describe_asset](#describe_asset)
    - [describe_asset_model](#describe_asset_model)
    - [describe_asset_property](#describe_asset_property)
    - [describe_dashboard](#describe_dashboard)
    - [describe_default_encryption_configuration](#describe_default_encryption_configuration)
    - [describe_gateway](#describe_gateway)
    - [describe_gateway_capability_configuration](#describe_gateway_capability_configuration)
    - [describe_logging_options](#describe_logging_options)
    - [describe_portal](#describe_portal)
    - [describe_project](#describe_project)
    - [disassociate_assets](#disassociate_assets)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_asset_property_aggregates](#get_asset_property_aggregates)
    - [get_asset_property_value](#get_asset_property_value)
    - [get_asset_property_value_history](#get_asset_property_value_history)
    - [get_interpolated_asset_property_values](#get_interpolated_asset_property_values)
    - [list_access_policies](#list_access_policies)
    - [list_asset_models](#list_asset_models)
    - [list_asset_relationships](#list_asset_relationships)
    - [list_assets](#list_assets)
    - [list_associated_assets](#list_associated_assets)
    - [list_dashboards](#list_dashboards)
    - [list_gateways](#list_gateways)
    - [list_portals](#list_portals)
    - [list_project_assets](#list_project_assets)
    - [list_projects](#list_projects)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_default_encryption_configuration](#put_default_encryption_configuration)
    - [put_logging_options](#put_logging_options)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_access_policy](#update_access_policy)
    - [update_asset](#update_asset)
    - [update_asset_model](#update_asset_model)
    - [update_asset_property](#update_asset_property)
    - [update_dashboard](#update_dashboard)
    - [update_gateway](#update_gateway)
    - [update_gateway_capability_configuration](#update_gateway_capability_configuration)
    - [update_portal](#update_portal)
    - [update_project](#update_project)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)
    - [get_waiter](#get_waiter-4)
    - [get_waiter](#get_waiter-5)

## IoTSiteWiseClient

Type annotations for `boto3.client("iotsitewise")`

Can be used directly:

```python
from mypy_boto3_iotsitewise.client import IoTSiteWiseClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotsitewise.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictingOperationException`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnauthorizedException`


## Methods


### associate_assets

Type annotations for `boto3.client("iotsitewise").associate_assets` method.

[Client.associate_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.associate_assets)

```python
def associate_assets(
    self,
    assetId: str,
    hierarchyId: str,
    childAssetId: str,
    clientToken: str = None
) -> None:
    pass
```

### batch_associate_project_assets

Type annotations for `boto3.client("iotsitewise").batch_associate_project_assets` method.

[Client.batch_associate_project_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_associate_project_assets)

```python
def batch_associate_project_assets(
    self,
    projectId: str,
    assetIds: List[str],
    clientToken: str = None
) -> BatchAssociateProjectAssetsResponseTypeDef:
    pass
```

### batch_disassociate_project_assets

Type annotations for `boto3.client("iotsitewise").batch_disassociate_project_assets` method.

[Client.batch_disassociate_project_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_disassociate_project_assets)

```python
def batch_disassociate_project_assets(
    self,
    projectId: str,
    assetIds: List[str],
    clientToken: str = None
) -> BatchDisassociateProjectAssetsResponseTypeDef:
    pass
```

### batch_put_asset_property_value

Type annotations for `boto3.client("iotsitewise").batch_put_asset_property_value` method.

[Client.batch_put_asset_property_value documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_put_asset_property_value)

```python
def batch_put_asset_property_value(
    self,
    entries: List[PutAssetPropertyValueEntryTypeDef]
) -> BatchPutAssetPropertyValueResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("iotsitewise").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_access_policy

Type annotations for `boto3.client("iotsitewise").create_access_policy` method.

[Client.create_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_access_policy)

```python
def create_access_policy(
    self,
    accessPolicyIdentity: "IdentityTypeDef",
    accessPolicyResource: "ResourceTypeDef",
    accessPolicyPermission: Permission,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateAccessPolicyResponseTypeDef:
    pass
```

### create_asset

Type annotations for `boto3.client("iotsitewise").create_asset` method.

[Client.create_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset)

```python
def create_asset(
    self,
    assetName: str,
    assetModelId: str,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateAssetResponseTypeDef:
    pass
```

### create_asset_model

Type annotations for `boto3.client("iotsitewise").create_asset_model` method.

[Client.create_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset_model)

```python
def create_asset_model(
    self,
    assetModelName: str,
    assetModelDescription: str = None,
    assetModelProperties: List["AssetModelPropertyDefinitionTypeDef"] = None,
    assetModelHierarchies: List[AssetModelHierarchyDefinitionTypeDef] = None,
    assetModelCompositeModels: List[AssetModelCompositeModelDefinitionTypeDef] = None,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateAssetModelResponseTypeDef:
    pass
```

### create_dashboard

Type annotations for `boto3.client("iotsitewise").create_dashboard` method.

[Client.create_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_dashboard)

```python
def create_dashboard(
    self,
    projectId: str,
    dashboardName: str,
    dashboardDefinition: str,
    dashboardDescription: str = None,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateDashboardResponseTypeDef:
    pass
```

### create_gateway

Type annotations for `boto3.client("iotsitewise").create_gateway` method.

[Client.create_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_gateway)

```python
def create_gateway(
    self,
    gatewayName: str,
    gatewayPlatform: "GatewayPlatformTypeDef",
    tags: Dict[str, str] = None
) -> CreateGatewayResponseTypeDef:
    pass
```

### create_portal

Type annotations for `boto3.client("iotsitewise").create_portal` method.

[Client.create_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_portal)

```python
def create_portal(
    self,
    portalName: str,
    portalContactEmail: str,
    roleArn: str,
    portalDescription: str = None,
    clientToken: str = None,
    portalLogoImageFile: "ImageFileTypeDef" = None,
    tags: Dict[str, str] = None,
    portalAuthMode: AuthMode = None
) -> CreatePortalResponseTypeDef:
    pass
```

### create_project

Type annotations for `boto3.client("iotsitewise").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_project)

```python
def create_project(
    self,
    portalId: str,
    projectName: str,
    projectDescription: str = None,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateProjectResponseTypeDef:
    pass
```

### delete_access_policy

Type annotations for `boto3.client("iotsitewise").delete_access_policy` method.

[Client.delete_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_access_policy)

```python
def delete_access_policy(
    self,
    accessPolicyId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### delete_asset

Type annotations for `boto3.client("iotsitewise").delete_asset` method.

[Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_asset)

```python
def delete_asset(
    self,
    assetId: str,
    clientToken: str = None
) -> DeleteAssetResponseTypeDef:
    pass
```

### delete_asset_model

Type annotations for `boto3.client("iotsitewise").delete_asset_model` method.

[Client.delete_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_asset_model)

```python
def delete_asset_model(
    self,
    assetModelId: str,
    clientToken: str = None
) -> DeleteAssetModelResponseTypeDef:
    pass
```

### delete_dashboard

Type annotations for `boto3.client("iotsitewise").delete_dashboard` method.

[Client.delete_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_dashboard)

```python
def delete_dashboard(
    self,
    dashboardId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### delete_gateway

Type annotations for `boto3.client("iotsitewise").delete_gateway` method.

[Client.delete_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_gateway)

```python
def delete_gateway(
    self,
    gatewayId: str
) -> None:
    pass
```

### delete_portal

Type annotations for `boto3.client("iotsitewise").delete_portal` method.

[Client.delete_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_portal)

```python
def delete_portal(
    self,
    portalId: str,
    clientToken: str = None
) -> DeletePortalResponseTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("iotsitewise").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_project)

```python
def delete_project(
    self,
    projectId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### describe_access_policy

Type annotations for `boto3.client("iotsitewise").describe_access_policy` method.

[Client.describe_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_access_policy)

```python
def describe_access_policy(
    self,
    accessPolicyId: str
) -> DescribeAccessPolicyResponseTypeDef:
    pass
```

### describe_asset

Type annotations for `boto3.client("iotsitewise").describe_asset` method.

[Client.describe_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset)

```python
def describe_asset(
    self,
    assetId: str
) -> DescribeAssetResponseTypeDef:
    pass
```

### describe_asset_model

Type annotations for `boto3.client("iotsitewise").describe_asset_model` method.

[Client.describe_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset_model)

```python
def describe_asset_model(
    self,
    assetModelId: str
) -> DescribeAssetModelResponseTypeDef:
    pass
```

### describe_asset_property

Type annotations for `boto3.client("iotsitewise").describe_asset_property` method.

[Client.describe_asset_property documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset_property)

```python
def describe_asset_property(
    self,
    assetId: str,
    propertyId: str
) -> DescribeAssetPropertyResponseTypeDef:
    pass
```

### describe_dashboard

Type annotations for `boto3.client("iotsitewise").describe_dashboard` method.

[Client.describe_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_dashboard)

```python
def describe_dashboard(
    self,
    dashboardId: str
) -> DescribeDashboardResponseTypeDef:
    pass
```

### describe_default_encryption_configuration

Type annotations for `boto3.client("iotsitewise").describe_default_encryption_configuration` method.

[Client.describe_default_encryption_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_default_encryption_configuration)

```python
def describe_default_encryption_configuration(
    self
) -> DescribeDefaultEncryptionConfigurationResponseTypeDef:
    pass
```

### describe_gateway

Type annotations for `boto3.client("iotsitewise").describe_gateway` method.

[Client.describe_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_gateway)

```python
def describe_gateway(
    self,
    gatewayId: str
) -> DescribeGatewayResponseTypeDef:
    pass
```

### describe_gateway_capability_configuration

Type annotations for `boto3.client("iotsitewise").describe_gateway_capability_configuration` method.

[Client.describe_gateway_capability_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_gateway_capability_configuration)

```python
def describe_gateway_capability_configuration(
    self,
    gatewayId: str,
    capabilityNamespace: str
) -> DescribeGatewayCapabilityConfigurationResponseTypeDef:
    pass
```

### describe_logging_options

Type annotations for `boto3.client("iotsitewise").describe_logging_options` method.

[Client.describe_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_logging_options)

```python
def describe_logging_options(
    self
) -> DescribeLoggingOptionsResponseTypeDef:
    pass
```

### describe_portal

Type annotations for `boto3.client("iotsitewise").describe_portal` method.

[Client.describe_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_portal)

```python
def describe_portal(
    self,
    portalId: str
) -> DescribePortalResponseTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("iotsitewise").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_project)

```python
def describe_project(
    self,
    projectId: str
) -> DescribeProjectResponseTypeDef:
    pass
```

### disassociate_assets

Type annotations for `boto3.client("iotsitewise").disassociate_assets` method.

[Client.disassociate_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.disassociate_assets)

```python
def disassociate_assets(
    self,
    assetId: str,
    hierarchyId: str,
    childAssetId: str,
    clientToken: str = None
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotsitewise").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.generate_presigned_url)

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

### get_asset_property_aggregates

Type annotations for `boto3.client("iotsitewise").get_asset_property_aggregates` method.

[Client.get_asset_property_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_aggregates)

```python
def get_asset_property_aggregates(
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
    nextToken: str = None,
    maxResults: int = None
) -> GetAssetPropertyAggregatesResponseTypeDef:
    pass
```

### get_asset_property_value

Type annotations for `boto3.client("iotsitewise").get_asset_property_value` method.

[Client.get_asset_property_value documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_value)

```python
def get_asset_property_value(
    self,
    assetId: str = None,
    propertyId: str = None,
    propertyAlias: str = None
) -> GetAssetPropertyValueResponseTypeDef:
    pass
```

### get_asset_property_value_history

Type annotations for `boto3.client("iotsitewise").get_asset_property_value_history` method.

[Client.get_asset_property_value_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_value_history)

```python
def get_asset_property_value_history(
    self,
    assetId: str = None,
    propertyId: str = None,
    propertyAlias: str = None,
    startDate: datetime = None,
    endDate: datetime = None,
    qualities: List[Quality] = None,
    timeOrdering: TimeOrdering = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetAssetPropertyValueHistoryResponseTypeDef:
    pass
```

### get_interpolated_asset_property_values

Type annotations for `boto3.client("iotsitewise").get_interpolated_asset_property_values` method.

[Client.get_interpolated_asset_property_values documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.get_interpolated_asset_property_values)

```python
def get_interpolated_asset_property_values(
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
    nextToken: str = None,
    maxResults: int = None
) -> GetInterpolatedAssetPropertyValuesResponseTypeDef:
    pass
```

### list_access_policies

Type annotations for `boto3.client("iotsitewise").list_access_policies` method.

[Client.list_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_access_policies)

```python
def list_access_policies(
    self,
    identityType: IdentityType = None,
    identityId: str = None,
    resourceType: ResourceType = None,
    resourceId: str = None,
    iamArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAccessPoliciesResponseTypeDef:
    pass
```

### list_asset_models

Type annotations for `boto3.client("iotsitewise").list_asset_models` method.

[Client.list_asset_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_asset_models)

```python
def list_asset_models(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssetModelsResponseTypeDef:
    pass
```

### list_asset_relationships

Type annotations for `boto3.client("iotsitewise").list_asset_relationships` method.

[Client.list_asset_relationships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_asset_relationships)

```python
def list_asset_relationships(
    self,
    assetId: str,
    traversalType: TraversalType,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssetRelationshipsResponseTypeDef:
    pass
```

### list_assets

Type annotations for `boto3.client("iotsitewise").list_assets` method.

[Client.list_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_assets)

```python
def list_assets(
    self,
    nextToken: str = None,
    maxResults: int = None,
    assetModelId: str = None,
    filter: ListAssetsFilter = None
) -> ListAssetsResponseTypeDef:
    pass
```

### list_associated_assets

Type annotations for `boto3.client("iotsitewise").list_associated_assets` method.

[Client.list_associated_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_associated_assets)

```python
def list_associated_assets(
    self,
    assetId: str,
    hierarchyId: str = None,
    traversalDirection: TraversalDirection = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssociatedAssetsResponseTypeDef:
    pass
```

### list_dashboards

Type annotations for `boto3.client("iotsitewise").list_dashboards` method.

[Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_dashboards)

```python
def list_dashboards(
    self,
    projectId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListDashboardsResponseTypeDef:
    pass
```

### list_gateways

Type annotations for `boto3.client("iotsitewise").list_gateways` method.

[Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_gateways)

```python
def list_gateways(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListGatewaysResponseTypeDef:
    pass
```

### list_portals

Type annotations for `boto3.client("iotsitewise").list_portals` method.

[Client.list_portals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_portals)

```python
def list_portals(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListPortalsResponseTypeDef:
    pass
```

### list_project_assets

Type annotations for `boto3.client("iotsitewise").list_project_assets` method.

[Client.list_project_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_project_assets)

```python
def list_project_assets(
    self,
    projectId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListProjectAssetsResponseTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("iotsitewise").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_projects)

```python
def list_projects(
    self,
    portalId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListProjectsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotsitewise").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_default_encryption_configuration

Type annotations for `boto3.client("iotsitewise").put_default_encryption_configuration` method.

[Client.put_default_encryption_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.put_default_encryption_configuration)

```python
def put_default_encryption_configuration(
    self,
    encryptionType: EncryptionType,
    kmsKeyId: str = None
) -> PutDefaultEncryptionConfigurationResponseTypeDef:
    pass
```

### put_logging_options

Type annotations for `boto3.client("iotsitewise").put_logging_options` method.

[Client.put_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.put_logging_options)

```python
def put_logging_options(
    self,
    loggingOptions: "LoggingOptionsTypeDef"
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotsitewise").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotsitewise").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_access_policy

Type annotations for `boto3.client("iotsitewise").update_access_policy` method.

[Client.update_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_access_policy)

```python
def update_access_policy(
    self,
    accessPolicyId: str,
    accessPolicyIdentity: "IdentityTypeDef",
    accessPolicyResource: "ResourceTypeDef",
    accessPolicyPermission: Permission,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### update_asset

Type annotations for `boto3.client("iotsitewise").update_asset` method.

[Client.update_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset)

```python
def update_asset(
    self,
    assetId: str,
    assetName: str,
    clientToken: str = None
) -> UpdateAssetResponseTypeDef:
    pass
```

### update_asset_model

Type annotations for `boto3.client("iotsitewise").update_asset_model` method.

[Client.update_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset_model)

```python
def update_asset_model(
    self,
    assetModelId: str,
    assetModelName: str,
    assetModelDescription: str = None,
    assetModelProperties: List["AssetModelPropertyTypeDef"] = None,
    assetModelHierarchies: List["AssetModelHierarchyTypeDef"] = None,
    assetModelCompositeModels: List["AssetModelCompositeModelTypeDef"] = None,
    clientToken: str = None
) -> UpdateAssetModelResponseTypeDef:
    pass
```

### update_asset_property

Type annotations for `boto3.client("iotsitewise").update_asset_property` method.

[Client.update_asset_property documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset_property)

```python
def update_asset_property(
    self,
    assetId: str,
    propertyId: str,
    propertyAlias: str = None,
    propertyNotificationState: PropertyNotificationState = None,
    clientToken: str = None
) -> None:
    pass
```

### update_dashboard

Type annotations for `boto3.client("iotsitewise").update_dashboard` method.

[Client.update_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_dashboard)

```python
def update_dashboard(
    self,
    dashboardId: str,
    dashboardName: str,
    dashboardDefinition: str,
    dashboardDescription: str = None,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### update_gateway

Type annotations for `boto3.client("iotsitewise").update_gateway` method.

[Client.update_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_gateway)

```python
def update_gateway(
    self,
    gatewayId: str,
    gatewayName: str
) -> None:
    pass
```

### update_gateway_capability_configuration

Type annotations for `boto3.client("iotsitewise").update_gateway_capability_configuration` method.

[Client.update_gateway_capability_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_gateway_capability_configuration)

```python
def update_gateway_capability_configuration(
    self,
    gatewayId: str,
    capabilityNamespace: str,
    capabilityConfiguration: str
) -> UpdateGatewayCapabilityConfigurationResponseTypeDef:
    pass
```

### update_portal

Type annotations for `boto3.client("iotsitewise").update_portal` method.

[Client.update_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_portal)

```python
def update_portal(
    self,
    portalId: str,
    portalName: str,
    portalContactEmail: str,
    roleArn: str,
    portalDescription: str = None,
    portalLogoImage: ImageTypeDef = None,
    clientToken: str = None
) -> UpdatePortalResponseTypeDef:
    pass
```

### update_project

Type annotations for `boto3.client("iotsitewise").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.update_project)

```python
def update_project(
    self,
    projectId: str,
    projectName: str,
    projectDescription: str = None,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.GetAssetPropertyAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)

```python
@overload
def get_paginator(
    self,
    operation_name: GetAssetPropertyAggregatesPaginatorName
) -> GetAssetPropertyAggregatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.GetAssetPropertyValueHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetAssetPropertyValueHistoryPaginatorName
) -> GetAssetPropertyValueHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.GetInterpolatedAssetPropertyValues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues)

```python
@overload
def get_paginator(
    self,
    operation_name: GetInterpolatedAssetPropertyValuesPaginatorName
) -> GetInterpolatedAssetPropertyValuesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListAccessPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccessPoliciesPaginatorName
) -> ListAccessPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListAssetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssetModelsPaginatorName
) -> ListAssetModelsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListAssetRelationships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetRelationships)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssetRelationshipsPaginatorName
) -> ListAssetRelationshipsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssetsPaginatorName
) -> ListAssetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListAssociatedAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssociatedAssetsPaginatorName
) -> ListAssociatedAssetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDashboardsPaginatorName
) -> ListDashboardsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGatewaysPaginatorName
) -> ListGatewaysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListPortals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPortalsPaginatorName
) -> ListPortalsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListProjectAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListProjectAssetsPaginatorName
) -> ListProjectAssetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iotsitewise").get_paginator` method.

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListProjectsPaginatorName
) -> ListProjectsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("iotsitewise").get_waiter` method.

[Waiter.AssetActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetActive)

```python
@overload
def get_waiter(
    self,
    waiter_name: AssetActiveWaiterName
) -> AssetActiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iotsitewise").get_waiter` method.

[Waiter.AssetModelActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelActive)

```python
@overload
def get_waiter(
    self,
    waiter_name: AssetModelActiveWaiterName
) -> AssetModelActiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iotsitewise").get_waiter` method.

[Waiter.AssetModelNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: AssetModelNotExistsWaiterName
) -> AssetModelNotExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iotsitewise").get_waiter` method.

[Waiter.AssetNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: AssetNotExistsWaiterName
) -> AssetNotExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iotsitewise").get_waiter` method.

[Waiter.PortalActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalActive)

```python
@overload
def get_waiter(
    self,
    waiter_name: PortalActiveWaiterName
) -> PortalActiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iotsitewise").get_waiter` method.

[Waiter.PortalNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalNotExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: PortalNotExistsWaiterName
) -> PortalNotExistsWaiter:
    pass
```