# Literals for boto3 IoTSiteWise module

> [Index](../index.md) > [IoTSiteWise](./index.md) > Literals

Auto-generated documentation for [IoTSiteWise](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise)
type annotations stubs module [mypy_boto3_iotsitewise](https://pypi.org/project/mypy-boto3-iotsitewise/).

- [Literals for boto3 IoTSiteWise module](#literals-for-boto3-iotsitewise-module)
  - [AggregateType](#aggregatetype)
  - [AssetActiveWaiterName](#assetactivewaitername)
  - [AssetErrorCode](#asseterrorcode)
  - [AssetModelActiveWaiterName](#assetmodelactivewaitername)
  - [AssetModelNotExistsWaiterName](#assetmodelnotexistswaitername)
  - [AssetModelState](#assetmodelstate)
  - [AssetNotExistsWaiterName](#assetnotexistswaitername)
  - [AssetRelationshipType](#assetrelationshiptype)
  - [AssetState](#assetstate)
  - [AuthMode](#authmode)
  - [BatchPutAssetPropertyValueErrorCode](#batchputassetpropertyvalueerrorcode)
  - [CapabilitySyncStatus](#capabilitysyncstatus)
  - [ConfigurationState](#configurationstate)
  - [EncryptionType](#encryptiontype)
  - [ErrorCode](#errorcode)
  - [GetAssetPropertyAggregatesPaginatorName](#getassetpropertyaggregatespaginatorname)
  - [GetAssetPropertyValueHistoryPaginatorName](#getassetpropertyvaluehistorypaginatorname)
  - [GetInterpolatedAssetPropertyValuesPaginatorName](#getinterpolatedassetpropertyvaluespaginatorname)
  - [IdentityType](#identitytype)
  - [ImageFileType](#imagefiletype)
  - [ListAccessPoliciesPaginatorName](#listaccesspoliciespaginatorname)
  - [ListAssetModelsPaginatorName](#listassetmodelspaginatorname)
  - [ListAssetRelationshipsPaginatorName](#listassetrelationshipspaginatorname)
  - [ListAssetsFilter](#listassetsfilter)
  - [ListAssetsPaginatorName](#listassetspaginatorname)
  - [ListAssociatedAssetsPaginatorName](#listassociatedassetspaginatorname)
  - [ListDashboardsPaginatorName](#listdashboardspaginatorname)
  - [ListGatewaysPaginatorName](#listgatewayspaginatorname)
  - [ListPortalsPaginatorName](#listportalspaginatorname)
  - [ListProjectAssetsPaginatorName](#listprojectassetspaginatorname)
  - [ListProjectsPaginatorName](#listprojectspaginatorname)
  - [LoggingLevel](#logginglevel)
  - [MonitorErrorCode](#monitorerrorcode)
  - [Permission](#permission)
  - [PortalActiveWaiterName](#portalactivewaitername)
  - [PortalNotExistsWaiterName](#portalnotexistswaitername)
  - [PortalState](#portalstate)
  - [PropertyDataType](#propertydatatype)
  - [PropertyNotificationState](#propertynotificationstate)
  - [Quality](#quality)
  - [ResourceType](#resourcetype)
  - [TimeOrdering](#timeordering)
  - [TraversalDirection](#traversaldirection)
  - [TraversalType](#traversaltype)

## AggregateType

```python
from mypy_boto3_iotsitewise.literals import AggregateType
```

Values:

- `AVERAGE`
- `COUNT`
- `MAXIMUM`
- `MINIMUM`
- `STANDARD_DEVIATION`
- `SUM`

## AssetActiveWaiterName

```python
from mypy_boto3_iotsitewise.literals import AssetActiveWaiterName
```

Values:

- `asset_active`

## AssetErrorCode

```python
from mypy_boto3_iotsitewise.literals import AssetErrorCode
```

Values:

- `INTERNAL_FAILURE`

## AssetModelActiveWaiterName

```python
from mypy_boto3_iotsitewise.literals import AssetModelActiveWaiterName
```

Values:

- `asset_model_active`

## AssetModelNotExistsWaiterName

```python
from mypy_boto3_iotsitewise.literals import AssetModelNotExistsWaiterName
```

Values:

- `asset_model_not_exists`

## AssetModelState

```python
from mypy_boto3_iotsitewise.literals import AssetModelState
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `PROPAGATING`
- `UPDATING`

## AssetNotExistsWaiterName

```python
from mypy_boto3_iotsitewise.literals import AssetNotExistsWaiterName
```

Values:

- `asset_not_exists`

## AssetRelationshipType

```python
from mypy_boto3_iotsitewise.literals import AssetRelationshipType
```

Values:

- `HIERARCHY`

## AssetState

```python
from mypy_boto3_iotsitewise.literals import AssetState
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## AuthMode

```python
from mypy_boto3_iotsitewise.literals import AuthMode
```

Values:

- `IAM`
- `SSO`

## BatchPutAssetPropertyValueErrorCode

```python
from mypy_boto3_iotsitewise.literals import BatchPutAssetPropertyValueErrorCode
```

Values:

- `AccessDeniedException`
- `ConflictingOperationException`
- `InternalFailureException`
- `InvalidRequestException`
- `LimitExceededException`
- `ResourceNotFoundException`
- `ServiceUnavailableException`
- `ThrottlingException`
- `TimestampOutOfRangeException`

## CapabilitySyncStatus

```python
from mypy_boto3_iotsitewise.literals import CapabilitySyncStatus
```

Values:

- `IN_SYNC`
- `OUT_OF_SYNC`
- `SYNC_FAILED`

## ConfigurationState

```python
from mypy_boto3_iotsitewise.literals import ConfigurationState
```

Values:

- `ACTIVE`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## EncryptionType

```python
from mypy_boto3_iotsitewise.literals import EncryptionType
```

Values:

- `KMS_BASED_ENCRYPTION`
- `SITEWISE_DEFAULT_ENCRYPTION`

## ErrorCode

```python
from mypy_boto3_iotsitewise.literals import ErrorCode
```

Values:

- `INTERNAL_FAILURE`
- `VALIDATION_ERROR`

## GetAssetPropertyAggregatesPaginatorName

```python
from mypy_boto3_iotsitewise.literals import GetAssetPropertyAggregatesPaginatorName
```

Values:

- `get_asset_property_aggregates`

## GetAssetPropertyValueHistoryPaginatorName

```python
from mypy_boto3_iotsitewise.literals import GetAssetPropertyValueHistoryPaginatorName
```

Values:

- `get_asset_property_value_history`

## GetInterpolatedAssetPropertyValuesPaginatorName

```python
from mypy_boto3_iotsitewise.literals import GetInterpolatedAssetPropertyValuesPaginatorName
```

Values:

- `get_interpolated_asset_property_values`

## IdentityType

```python
from mypy_boto3_iotsitewise.literals import IdentityType
```

Values:

- `GROUP`
- `IAM`
- `USER`

## ImageFileType

```python
from mypy_boto3_iotsitewise.literals import ImageFileType
```

Values:

- `PNG`

## ListAccessPoliciesPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListAccessPoliciesPaginatorName
```

Values:

- `list_access_policies`

## ListAssetModelsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListAssetModelsPaginatorName
```

Values:

- `list_asset_models`

## ListAssetRelationshipsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListAssetRelationshipsPaginatorName
```

Values:

- `list_asset_relationships`

## ListAssetsFilter

```python
from mypy_boto3_iotsitewise.literals import ListAssetsFilter
```

Values:

- `ALL`
- `TOP_LEVEL`

## ListAssetsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListAssetsPaginatorName
```

Values:

- `list_assets`

## ListAssociatedAssetsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListAssociatedAssetsPaginatorName
```

Values:

- `list_associated_assets`

## ListDashboardsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListDashboardsPaginatorName
```

Values:

- `list_dashboards`

## ListGatewaysPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListGatewaysPaginatorName
```

Values:

- `list_gateways`

## ListPortalsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListPortalsPaginatorName
```

Values:

- `list_portals`

## ListProjectAssetsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListProjectAssetsPaginatorName
```

Values:

- `list_project_assets`

## ListProjectsPaginatorName

```python
from mypy_boto3_iotsitewise.literals import ListProjectsPaginatorName
```

Values:

- `list_projects`

## LoggingLevel

```python
from mypy_boto3_iotsitewise.literals import LoggingLevel
```

Values:

- `ERROR`
- `INFO`
- `OFF`

## MonitorErrorCode

```python
from mypy_boto3_iotsitewise.literals import MonitorErrorCode
```

Values:

- `INTERNAL_FAILURE`
- `LIMIT_EXCEEDED`
- `VALIDATION_ERROR`

## Permission

```python
from mypy_boto3_iotsitewise.literals import Permission
```

Values:

- `ADMINISTRATOR`
- `VIEWER`

## PortalActiveWaiterName

```python
from mypy_boto3_iotsitewise.literals import PortalActiveWaiterName
```

Values:

- `portal_active`

## PortalNotExistsWaiterName

```python
from mypy_boto3_iotsitewise.literals import PortalNotExistsWaiterName
```

Values:

- `portal_not_exists`

## PortalState

```python
from mypy_boto3_iotsitewise.literals import PortalState
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## PropertyDataType

```python
from mypy_boto3_iotsitewise.literals import PropertyDataType
```

Values:

- `BOOLEAN`
- `DOUBLE`
- `INTEGER`
- `STRING`
- `STRUCT`

## PropertyNotificationState

```python
from mypy_boto3_iotsitewise.literals import PropertyNotificationState
```

Values:

- `DISABLED`
- `ENABLED`

## Quality

```python
from mypy_boto3_iotsitewise.literals import Quality
```

Values:

- `BAD`
- `GOOD`
- `UNCERTAIN`

## ResourceType

```python
from mypy_boto3_iotsitewise.literals import ResourceType
```

Values:

- `PORTAL`
- `PROJECT`

## TimeOrdering

```python
from mypy_boto3_iotsitewise.literals import TimeOrdering
```

Values:

- `ASCENDING`
- `DESCENDING`

## TraversalDirection

```python
from mypy_boto3_iotsitewise.literals import TraversalDirection
```

Values:

- `CHILD`
- `PARENT`

## TraversalType

```python
from mypy_boto3_iotsitewise.literals import TraversalType
```

Values:

- `PATH_TO_ROOT`
