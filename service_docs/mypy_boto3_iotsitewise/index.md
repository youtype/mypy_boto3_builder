# Type annotations for boto3 IoTSiteWise module

> [Index](../index.md) > IoTSiteWise

Auto-generated documentation for [IoTSiteWise](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise)
type annotations stubs module [mypy_boto3_iotsitewise](https://pypi.org/project/mypy-boto3-iotsitewise/).

```bash
pip install mypy-boto3-iotsitewise
```

- [Type annotations for boto3 IoTSiteWise module](#type-annotations-for-boto3-iotsitewise-module)
  - [IoTSiteWiseClient](#iotsitewiseclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTSiteWiseClient

Type annotations for  `boto3.client("iotsitewise")` as [IoTSiteWiseClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotsitewise.client import IoTSiteWiseClient
```


IoTSiteWiseClient [exceptions](./client.md#exceptions)



### Methods
- [associate_assets](./client.md#associate-assets)
- [batch_associate_project_assets](./client.md#batch-associate-project-assets)
- [batch_disassociate_project_assets](./client.md#batch-disassociate-project-assets)
- [batch_put_asset_property_value](./client.md#batch-put-asset-property-value)
- [can_paginate](./client.md#can-paginate)
- [create_access_policy](./client.md#create-access-policy)
- [create_asset](./client.md#create-asset)
- [create_asset_model](./client.md#create-asset-model)
- [create_dashboard](./client.md#create-dashboard)
- [create_gateway](./client.md#create-gateway)
- [create_portal](./client.md#create-portal)
- [create_project](./client.md#create-project)
- [delete_access_policy](./client.md#delete-access-policy)
- [delete_asset](./client.md#delete-asset)
- [delete_asset_model](./client.md#delete-asset-model)
- [delete_dashboard](./client.md#delete-dashboard)
- [delete_gateway](./client.md#delete-gateway)
- [delete_portal](./client.md#delete-portal)
- [delete_project](./client.md#delete-project)
- [describe_access_policy](./client.md#describe-access-policy)
- [describe_asset](./client.md#describe-asset)
- [describe_asset_model](./client.md#describe-asset-model)
- [describe_asset_property](./client.md#describe-asset-property)
- [describe_dashboard](./client.md#describe-dashboard)
- [describe_default_encryption_configuration](./client.md#describe-default-encryption-configuration)
- [describe_gateway](./client.md#describe-gateway)
- [describe_gateway_capability_configuration](./client.md#describe-gateway-capability-configuration)
- [describe_logging_options](./client.md#describe-logging-options)
- [describe_portal](./client.md#describe-portal)
- [describe_project](./client.md#describe-project)
- [disassociate_assets](./client.md#disassociate-assets)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_asset_property_aggregates](./client.md#get-asset-property-aggregates)
- [get_asset_property_value](./client.md#get-asset-property-value)
- [get_asset_property_value_history](./client.md#get-asset-property-value-history)
- [get_interpolated_asset_property_values](./client.md#get-interpolated-asset-property-values)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_access_policies](./client.md#list-access-policies)
- [list_asset_models](./client.md#list-asset-models)
- [list_asset_relationships](./client.md#list-asset-relationships)
- [list_assets](./client.md#list-assets)
- [list_associated_assets](./client.md#list-associated-assets)
- [list_dashboards](./client.md#list-dashboards)
- [list_gateways](./client.md#list-gateways)
- [list_portals](./client.md#list-portals)
- [list_project_assets](./client.md#list-project-assets)
- [list_projects](./client.md#list-projects)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_default_encryption_configuration](./client.md#put-default-encryption-configuration)
- [put_logging_options](./client.md#put-logging-options)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_access_policy](./client.md#update-access-policy)
- [update_asset](./client.md#update-asset)
- [update_asset_model](./client.md#update-asset-model)
- [update_asset_property](./client.md#update-asset-property)
- [update_dashboard](./client.md#update-dashboard)
- [update_gateway](./client.md#update-gateway)
- [update_gateway_capability_configuration](./client.md#update-gateway-capability-configuration)
- [update_portal](./client.md#update-portal)
- [update_project](./client.md#update-project)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictingOperationException](./client.md#conflictingoperationexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iotsitewise").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.paginators import GetAssetPropertyAggregatesPaginator, ...
```

- [GetAssetPropertyAggregatesPaginator](./paginators.md#getassetpropertyaggregatespaginator)
- [GetAssetPropertyValueHistoryPaginator](./paginators.md#getassetpropertyvaluehistorypaginator)
- [GetInterpolatedAssetPropertyValuesPaginator](./paginators.md#getinterpolatedassetpropertyvaluespaginator)
- [ListAccessPoliciesPaginator](./paginators.md#listaccesspoliciespaginator)
- [ListAssetModelsPaginator](./paginators.md#listassetmodelspaginator)
- [ListAssetRelationshipsPaginator](./paginators.md#listassetrelationshipspaginator)
- [ListAssetsPaginator](./paginators.md#listassetspaginator)
- [ListAssociatedAssetsPaginator](./paginators.md#listassociatedassetspaginator)
- [ListDashboardsPaginator](./paginators.md#listdashboardspaginator)
- [ListGatewaysPaginator](./paginators.md#listgatewayspaginator)
- [ListPortalsPaginator](./paginators.md#listportalspaginator)
- [ListProjectAssetsPaginator](./paginators.md#listprojectassetspaginator)
- [ListProjectsPaginator](./paginators.md#listprojectspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("iotsitewise").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_iotsitewise.waiters import AssetActiveWaiter, ...
```

- [AssetActiveWaiter](./waiters.md#assetactivewaiter)
- [AssetModelActiveWaiter](./waiters.md#assetmodelactivewaiter)
- [AssetModelNotExistsWaiter](./waiters.md#assetmodelnotexistswaiter)
- [AssetNotExistsWaiter](./waiters.md#assetnotexistswaiter)
- [PortalActiveWaiter](./waiters.md#portalactivewaiter)
- [PortalNotExistsWaiter](./waiters.md#portalnotexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotsitewise.literals import AggregateType, ...
```

- [AggregateType](./literals.md#aggregatetype)
- [AssetActiveWaiterName](./literals.md#assetactivewaitername)
- [AssetErrorCode](./literals.md#asseterrorcode)
- [AssetModelActiveWaiterName](./literals.md#assetmodelactivewaitername)
- [AssetModelNotExistsWaiterName](./literals.md#assetmodelnotexistswaitername)
- [AssetModelState](./literals.md#assetmodelstate)
- [AssetNotExistsWaiterName](./literals.md#assetnotexistswaitername)
- [AssetRelationshipType](./literals.md#assetrelationshiptype)
- [AssetState](./literals.md#assetstate)
- [AuthMode](./literals.md#authmode)
- [BatchPutAssetPropertyValueErrorCode](./literals.md#batchputassetpropertyvalueerrorcode)
- [CapabilitySyncStatus](./literals.md#capabilitysyncstatus)
- [ConfigurationState](./literals.md#configurationstate)
- [EncryptionType](./literals.md#encryptiontype)
- [ErrorCode](./literals.md#errorcode)
- [GetAssetPropertyAggregatesPaginatorName](./literals.md#getassetpropertyaggregatespaginatorname)
- [GetAssetPropertyValueHistoryPaginatorName](./literals.md#getassetpropertyvaluehistorypaginatorname)
- [GetInterpolatedAssetPropertyValuesPaginatorName](./literals.md#getinterpolatedassetpropertyvaluespaginatorname)
- [IdentityType](./literals.md#identitytype)
- [ImageFileType](./literals.md#imagefiletype)
- [ListAccessPoliciesPaginatorName](./literals.md#listaccesspoliciespaginatorname)
- [ListAssetModelsPaginatorName](./literals.md#listassetmodelspaginatorname)
- [ListAssetRelationshipsPaginatorName](./literals.md#listassetrelationshipspaginatorname)
- [ListAssetsFilter](./literals.md#listassetsfilter)
- [ListAssetsPaginatorName](./literals.md#listassetspaginatorname)
- [ListAssociatedAssetsPaginatorName](./literals.md#listassociatedassetspaginatorname)
- [ListDashboardsPaginatorName](./literals.md#listdashboardspaginatorname)
- [ListGatewaysPaginatorName](./literals.md#listgatewayspaginatorname)
- [ListPortalsPaginatorName](./literals.md#listportalspaginatorname)
- [ListProjectAssetsPaginatorName](./literals.md#listprojectassetspaginatorname)
- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)
- [LoggingLevel](./literals.md#logginglevel)
- [MonitorErrorCode](./literals.md#monitorerrorcode)
- [Permission](./literals.md#permission)
- [PortalActiveWaiterName](./literals.md#portalactivewaitername)
- [PortalNotExistsWaiterName](./literals.md#portalnotexistswaitername)
- [PortalState](./literals.md#portalstate)
- [PropertyDataType](./literals.md#propertydatatype)
- [PropertyNotificationState](./literals.md#propertynotificationstate)
- [Quality](./literals.md#quality)
- [ResourceType](./literals.md#resourcetype)
- [TimeOrdering](./literals.md#timeordering)
- [TraversalDirection](./literals.md#traversaldirection)
- [TraversalType](./literals.md#traversaltype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotsitewise.type_defs import AccessPolicySummaryTypeDef, ...
```

- [AccessPolicySummaryTypeDef](./type_defs.md#accesspolicysummarytypedef)
- [AggregatedValueTypeDef](./type_defs.md#aggregatedvaluetypedef)
- [AggregatesTypeDef](./type_defs.md#aggregatestypedef)
- [AssetCompositeModelTypeDef](./type_defs.md#assetcompositemodeltypedef)
- [AssetErrorDetailsTypeDef](./type_defs.md#asseterrordetailstypedef)
- [AssetHierarchyInfoTypeDef](./type_defs.md#assethierarchyinfotypedef)
- [AssetHierarchyTypeDef](./type_defs.md#assethierarchytypedef)
- [AssetModelCompositeModelDefinitionTypeDef](./type_defs.md#assetmodelcompositemodeldefinitiontypedef)
- [AssetModelCompositeModelTypeDef](./type_defs.md#assetmodelcompositemodeltypedef)
- [AssetModelHierarchyDefinitionTypeDef](./type_defs.md#assetmodelhierarchydefinitiontypedef)
- [AssetModelHierarchyTypeDef](./type_defs.md#assetmodelhierarchytypedef)
- [AssetModelPropertyDefinitionTypeDef](./type_defs.md#assetmodelpropertydefinitiontypedef)
- [AssetModelPropertyTypeDef](./type_defs.md#assetmodelpropertytypedef)
- [AssetModelStatusTypeDef](./type_defs.md#assetmodelstatustypedef)
- [AssetModelSummaryTypeDef](./type_defs.md#assetmodelsummarytypedef)
- [AssetPropertyTypeDef](./type_defs.md#assetpropertytypedef)
- [AssetPropertyValueTypeDef](./type_defs.md#assetpropertyvaluetypedef)
- [AssetRelationshipSummaryTypeDef](./type_defs.md#assetrelationshipsummarytypedef)
- [AssetStatusTypeDef](./type_defs.md#assetstatustypedef)
- [AssetSummaryTypeDef](./type_defs.md#assetsummarytypedef)
- [AssociatedAssetsSummaryTypeDef](./type_defs.md#associatedassetssummarytypedef)
- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [BatchAssociateProjectAssetsResponseTypeDef](./type_defs.md#batchassociateprojectassetsresponsetypedef)
- [BatchDisassociateProjectAssetsResponseTypeDef](./type_defs.md#batchdisassociateprojectassetsresponsetypedef)
- [BatchPutAssetPropertyErrorEntryTypeDef](./type_defs.md#batchputassetpropertyerrorentrytypedef)
- [BatchPutAssetPropertyErrorTypeDef](./type_defs.md#batchputassetpropertyerrortypedef)
- [BatchPutAssetPropertyValueResponseTypeDef](./type_defs.md#batchputassetpropertyvalueresponsetypedef)
- [CompositeModelPropertyTypeDef](./type_defs.md#compositemodelpropertytypedef)
- [ConfigurationErrorDetailsTypeDef](./type_defs.md#configurationerrordetailstypedef)
- [ConfigurationStatusTypeDef](./type_defs.md#configurationstatustypedef)
- [CreateAccessPolicyResponseTypeDef](./type_defs.md#createaccesspolicyresponsetypedef)
- [CreateAssetModelResponseTypeDef](./type_defs.md#createassetmodelresponsetypedef)
- [CreateAssetResponseTypeDef](./type_defs.md#createassetresponsetypedef)
- [CreateDashboardResponseTypeDef](./type_defs.md#createdashboardresponsetypedef)
- [CreateGatewayResponseTypeDef](./type_defs.md#creategatewayresponsetypedef)
- [CreatePortalResponseTypeDef](./type_defs.md#createportalresponsetypedef)
- [CreateProjectResponseTypeDef](./type_defs.md#createprojectresponsetypedef)
- [DashboardSummaryTypeDef](./type_defs.md#dashboardsummarytypedef)
- [DeleteAssetModelResponseTypeDef](./type_defs.md#deleteassetmodelresponsetypedef)
- [DeleteAssetResponseTypeDef](./type_defs.md#deleteassetresponsetypedef)
- [DeletePortalResponseTypeDef](./type_defs.md#deleteportalresponsetypedef)
- [DescribeAccessPolicyResponseTypeDef](./type_defs.md#describeaccesspolicyresponsetypedef)
- [DescribeAssetModelResponseTypeDef](./type_defs.md#describeassetmodelresponsetypedef)
- [DescribeAssetPropertyResponseTypeDef](./type_defs.md#describeassetpropertyresponsetypedef)
- [DescribeAssetResponseTypeDef](./type_defs.md#describeassetresponsetypedef)
- [DescribeDashboardResponseTypeDef](./type_defs.md#describedashboardresponsetypedef)
- [DescribeDefaultEncryptionConfigurationResponseTypeDef](./type_defs.md#describedefaultencryptionconfigurationresponsetypedef)
- [DescribeGatewayCapabilityConfigurationResponseTypeDef](./type_defs.md#describegatewaycapabilityconfigurationresponsetypedef)
- [DescribeGatewayResponseTypeDef](./type_defs.md#describegatewayresponsetypedef)
- [DescribeLoggingOptionsResponseTypeDef](./type_defs.md#describeloggingoptionsresponsetypedef)
- [DescribePortalResponseTypeDef](./type_defs.md#describeportalresponsetypedef)
- [DescribeProjectResponseTypeDef](./type_defs.md#describeprojectresponsetypedef)
- [ErrorDetailsTypeDef](./type_defs.md#errordetailstypedef)
- [ExpressionVariableTypeDef](./type_defs.md#expressionvariabletypedef)
- [GatewayCapabilitySummaryTypeDef](./type_defs.md#gatewaycapabilitysummarytypedef)
- [GatewayPlatformTypeDef](./type_defs.md#gatewayplatformtypedef)
- [GatewaySummaryTypeDef](./type_defs.md#gatewaysummarytypedef)
- [GetAssetPropertyAggregatesResponseTypeDef](./type_defs.md#getassetpropertyaggregatesresponsetypedef)
- [GetAssetPropertyValueHistoryResponseTypeDef](./type_defs.md#getassetpropertyvaluehistoryresponsetypedef)
- [GetAssetPropertyValueResponseTypeDef](./type_defs.md#getassetpropertyvalueresponsetypedef)
- [GetInterpolatedAssetPropertyValuesResponseTypeDef](./type_defs.md#getinterpolatedassetpropertyvaluesresponsetypedef)
- [GreengrassTypeDef](./type_defs.md#greengrasstypedef)
- [GroupIdentityTypeDef](./type_defs.md#groupidentitytypedef)
- [IAMRoleIdentityTypeDef](./type_defs.md#iamroleidentitytypedef)
- [IAMUserIdentityTypeDef](./type_defs.md#iamuseridentitytypedef)
- [IdentityTypeDef](./type_defs.md#identitytypedef)
- [ImageFileTypeDef](./type_defs.md#imagefiletypedef)
- [ImageLocationTypeDef](./type_defs.md#imagelocationtypedef)
- [ImageTypeDef](./type_defs.md#imagetypedef)
- [InterpolatedAssetPropertyValueTypeDef](./type_defs.md#interpolatedassetpropertyvaluetypedef)
- [ListAccessPoliciesResponseTypeDef](./type_defs.md#listaccesspoliciesresponsetypedef)
- [ListAssetModelsResponseTypeDef](./type_defs.md#listassetmodelsresponsetypedef)
- [ListAssetRelationshipsResponseTypeDef](./type_defs.md#listassetrelationshipsresponsetypedef)
- [ListAssetsResponseTypeDef](./type_defs.md#listassetsresponsetypedef)
- [ListAssociatedAssetsResponseTypeDef](./type_defs.md#listassociatedassetsresponsetypedef)
- [ListDashboardsResponseTypeDef](./type_defs.md#listdashboardsresponsetypedef)
- [ListGatewaysResponseTypeDef](./type_defs.md#listgatewaysresponsetypedef)
- [ListPortalsResponseTypeDef](./type_defs.md#listportalsresponsetypedef)
- [ListProjectAssetsResponseTypeDef](./type_defs.md#listprojectassetsresponsetypedef)
- [ListProjectsResponseTypeDef](./type_defs.md#listprojectsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [LoggingOptionsTypeDef](./type_defs.md#loggingoptionstypedef)
- [MetricTypeDef](./type_defs.md#metrictypedef)
- [MetricWindowTypeDef](./type_defs.md#metricwindowtypedef)
- [MonitorErrorDetailsTypeDef](./type_defs.md#monitorerrordetailstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PortalResourceTypeDef](./type_defs.md#portalresourcetypedef)
- [PortalStatusTypeDef](./type_defs.md#portalstatustypedef)
- [PortalSummaryTypeDef](./type_defs.md#portalsummarytypedef)
- [ProjectResourceTypeDef](./type_defs.md#projectresourcetypedef)
- [ProjectSummaryTypeDef](./type_defs.md#projectsummarytypedef)
- [PropertyNotificationTypeDef](./type_defs.md#propertynotificationtypedef)
- [PropertyTypeDef](./type_defs.md#propertytypedef)
- [PropertyTypeTypeDef](./type_defs.md#propertytypetypedef)
- [PutAssetPropertyValueEntryTypeDef](./type_defs.md#putassetpropertyvalueentrytypedef)
- [PutDefaultEncryptionConfigurationResponseTypeDef](./type_defs.md#putdefaultencryptionconfigurationresponsetypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [TimeInNanosTypeDef](./type_defs.md#timeinnanostypedef)
- [TransformTypeDef](./type_defs.md#transformtypedef)
- [TumblingWindowTypeDef](./type_defs.md#tumblingwindowtypedef)
- [UpdateAssetModelResponseTypeDef](./type_defs.md#updateassetmodelresponsetypedef)
- [UpdateAssetResponseTypeDef](./type_defs.md#updateassetresponsetypedef)
- [UpdateGatewayCapabilityConfigurationResponseTypeDef](./type_defs.md#updategatewaycapabilityconfigurationresponsetypedef)
- [UpdatePortalResponseTypeDef](./type_defs.md#updateportalresponsetypedef)
- [UserIdentityTypeDef](./type_defs.md#useridentitytypedef)
- [VariableValueTypeDef](./type_defs.md#variablevaluetypedef)
- [VariantTypeDef](./type_defs.md#varianttypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
