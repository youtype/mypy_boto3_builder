# Type annotations for boto3 AppMesh module

> [Index](../index.md) > AppMesh

Auto-generated documentation for [AppMesh](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh)
type annotations stubs module [mypy_boto3_appmesh](https://pypi.org/project/mypy-boto3-appmesh/).

```bash
pip install mypy-boto3-appmesh
```

- [Type annotations for boto3 AppMesh module](#type-annotations-for-boto3-appmesh-module)
  - [AppMeshClient](#appmeshclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AppMeshClient

Type annotations for  `boto3.client("appmesh")` as [AppMeshClient](./client.md)

Can be used directly:

```python
from mypy_boto3_appmesh.client import AppMeshClient
```


AppMeshClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_gateway_route](./client.md#create-gateway-route)
- [create_mesh](./client.md#create-mesh)
- [create_route](./client.md#create-route)
- [create_virtual_gateway](./client.md#create-virtual-gateway)
- [create_virtual_node](./client.md#create-virtual-node)
- [create_virtual_router](./client.md#create-virtual-router)
- [create_virtual_service](./client.md#create-virtual-service)
- [delete_gateway_route](./client.md#delete-gateway-route)
- [delete_mesh](./client.md#delete-mesh)
- [delete_route](./client.md#delete-route)
- [delete_virtual_gateway](./client.md#delete-virtual-gateway)
- [delete_virtual_node](./client.md#delete-virtual-node)
- [delete_virtual_router](./client.md#delete-virtual-router)
- [delete_virtual_service](./client.md#delete-virtual-service)
- [describe_gateway_route](./client.md#describe-gateway-route)
- [describe_mesh](./client.md#describe-mesh)
- [describe_route](./client.md#describe-route)
- [describe_virtual_gateway](./client.md#describe-virtual-gateway)
- [describe_virtual_node](./client.md#describe-virtual-node)
- [describe_virtual_router](./client.md#describe-virtual-router)
- [describe_virtual_service](./client.md#describe-virtual-service)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_gateway_routes](./client.md#list-gateway-routes)
- [list_meshes](./client.md#list-meshes)
- [list_routes](./client.md#list-routes)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_virtual_gateways](./client.md#list-virtual-gateways)
- [list_virtual_nodes](./client.md#list-virtual-nodes)
- [list_virtual_routers](./client.md#list-virtual-routers)
- [list_virtual_services](./client.md#list-virtual-services)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_gateway_route](./client.md#update-gateway-route)
- [update_mesh](./client.md#update-mesh)
- [update_route](./client.md#update-route)
- [update_virtual_gateway](./client.md#update-virtual-gateway)
- [update_virtual_node](./client.md#update-virtual-node)
- [update_virtual_router](./client.md#update-virtual-router)
- [update_virtual_service](./client.md#update-virtual-service)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("appmesh").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListGatewayRoutesPaginator, ...
```

- [ListGatewayRoutesPaginator](./paginators.md#listgatewayroutespaginator)
- [ListMeshesPaginator](./paginators.md#listmeshespaginator)
- [ListRoutesPaginator](./paginators.md#listroutespaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- [ListVirtualGatewaysPaginator](./paginators.md#listvirtualgatewayspaginator)
- [ListVirtualNodesPaginator](./paginators.md#listvirtualnodespaginator)
- [ListVirtualRoutersPaginator](./paginators.md#listvirtualrouterspaginator)
- [ListVirtualServicesPaginator](./paginators.md#listvirtualservicespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appmesh.literals import DurationUnit, ...
```

- [DurationUnit](./literals.md#durationunit)
- [EgressFilterType](./literals.md#egressfiltertype)
- [GatewayRouteStatusCode](./literals.md#gatewayroutestatuscode)
- [GrpcRetryPolicyEvent](./literals.md#grpcretrypolicyevent)
- [HttpMethod](./literals.md#httpmethod)
- [HttpScheme](./literals.md#httpscheme)
- [ListGatewayRoutesPaginatorName](./literals.md#listgatewayroutespaginatorname)
- [ListMeshesPaginatorName](./literals.md#listmeshespaginatorname)
- [ListRoutesPaginatorName](./literals.md#listroutespaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [ListVirtualGatewaysPaginatorName](./literals.md#listvirtualgatewayspaginatorname)
- [ListVirtualNodesPaginatorName](./literals.md#listvirtualnodespaginatorname)
- [ListVirtualRoutersPaginatorName](./literals.md#listvirtualrouterspaginatorname)
- [ListVirtualServicesPaginatorName](./literals.md#listvirtualservicespaginatorname)
- [ListenerTlsMode](./literals.md#listenertlsmode)
- [MeshStatusCode](./literals.md#meshstatuscode)
- [PortProtocol](./literals.md#portprotocol)
- [RouteStatusCode](./literals.md#routestatuscode)
- [TcpRetryPolicyEvent](./literals.md#tcpretrypolicyevent)
- [VirtualGatewayListenerTlsMode](./literals.md#virtualgatewaylistenertlsmode)
- [VirtualGatewayPortProtocol](./literals.md#virtualgatewayportprotocol)
- [VirtualGatewayStatusCode](./literals.md#virtualgatewaystatuscode)
- [VirtualNodeStatusCode](./literals.md#virtualnodestatuscode)
- [VirtualRouterStatusCode](./literals.md#virtualrouterstatuscode)
- [VirtualServiceStatusCode](./literals.md#virtualservicestatuscode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appmesh.type_defs import AccessLogTypeDef, ...
```

- [AccessLogTypeDef](./type_defs.md#accesslogtypedef)
- [AwsCloudMapInstanceAttributeTypeDef](./type_defs.md#awscloudmapinstanceattributetypedef)
- [AwsCloudMapServiceDiscoveryTypeDef](./type_defs.md#awscloudmapservicediscoverytypedef)
- [BackendDefaultsTypeDef](./type_defs.md#backenddefaultstypedef)
- [BackendTypeDef](./type_defs.md#backendtypedef)
- [ClientPolicyTlsTypeDef](./type_defs.md#clientpolicytlstypedef)
- [ClientPolicyTypeDef](./type_defs.md#clientpolicytypedef)
- [ClientTlsCertificateTypeDef](./type_defs.md#clienttlscertificatetypedef)
- [DnsServiceDiscoveryTypeDef](./type_defs.md#dnsservicediscoverytypedef)
- [DurationTypeDef](./type_defs.md#durationtypedef)
- [EgressFilterTypeDef](./type_defs.md#egressfiltertypedef)
- [FileAccessLogTypeDef](./type_defs.md#fileaccesslogtypedef)
- [GatewayRouteDataTypeDef](./type_defs.md#gatewayroutedatatypedef)
- [GatewayRouteRefTypeDef](./type_defs.md#gatewayroutereftypedef)
- [GatewayRouteSpecTypeDef](./type_defs.md#gatewayroutespectypedef)
- [GatewayRouteStatusTypeDef](./type_defs.md#gatewayroutestatustypedef)
- [GatewayRouteTargetTypeDef](./type_defs.md#gatewayroutetargettypedef)
- [GatewayRouteVirtualServiceTypeDef](./type_defs.md#gatewayroutevirtualservicetypedef)
- [GrpcGatewayRouteActionTypeDef](./type_defs.md#grpcgatewayrouteactiontypedef)
- [GrpcGatewayRouteMatchTypeDef](./type_defs.md#grpcgatewayroutematchtypedef)
- [GrpcGatewayRouteTypeDef](./type_defs.md#grpcgatewayroutetypedef)
- [GrpcRetryPolicyTypeDef](./type_defs.md#grpcretrypolicytypedef)
- [GrpcRouteActionTypeDef](./type_defs.md#grpcrouteactiontypedef)
- [GrpcRouteMatchTypeDef](./type_defs.md#grpcroutematchtypedef)
- [GrpcRouteMetadataMatchMethodTypeDef](./type_defs.md#grpcroutemetadatamatchmethodtypedef)
- [GrpcRouteMetadataTypeDef](./type_defs.md#grpcroutemetadatatypedef)
- [GrpcRouteTypeDef](./type_defs.md#grpcroutetypedef)
- [GrpcTimeoutTypeDef](./type_defs.md#grpctimeouttypedef)
- [HeaderMatchMethodTypeDef](./type_defs.md#headermatchmethodtypedef)
- [HealthCheckPolicyTypeDef](./type_defs.md#healthcheckpolicytypedef)
- [HttpGatewayRouteActionTypeDef](./type_defs.md#httpgatewayrouteactiontypedef)
- [HttpGatewayRouteMatchTypeDef](./type_defs.md#httpgatewayroutematchtypedef)
- [HttpGatewayRouteTypeDef](./type_defs.md#httpgatewayroutetypedef)
- [HttpRetryPolicyTypeDef](./type_defs.md#httpretrypolicytypedef)
- [HttpRouteActionTypeDef](./type_defs.md#httprouteactiontypedef)
- [HttpRouteHeaderTypeDef](./type_defs.md#httprouteheadertypedef)
- [HttpRouteMatchTypeDef](./type_defs.md#httproutematchtypedef)
- [HttpRouteTypeDef](./type_defs.md#httproutetypedef)
- [HttpTimeoutTypeDef](./type_defs.md#httptimeouttypedef)
- [ListenerTimeoutTypeDef](./type_defs.md#listenertimeouttypedef)
- [ListenerTlsAcmCertificateTypeDef](./type_defs.md#listenertlsacmcertificatetypedef)
- [ListenerTlsCertificateTypeDef](./type_defs.md#listenertlscertificatetypedef)
- [ListenerTlsFileCertificateTypeDef](./type_defs.md#listenertlsfilecertificatetypedef)
- [ListenerTlsSdsCertificateTypeDef](./type_defs.md#listenertlssdscertificatetypedef)
- [ListenerTlsTypeDef](./type_defs.md#listenertlstypedef)
- [ListenerTlsValidationContextTrustTypeDef](./type_defs.md#listenertlsvalidationcontexttrusttypedef)
- [ListenerTlsValidationContextTypeDef](./type_defs.md#listenertlsvalidationcontexttypedef)
- [ListenerTypeDef](./type_defs.md#listenertypedef)
- [LoggingTypeDef](./type_defs.md#loggingtypedef)
- [MatchRangeTypeDef](./type_defs.md#matchrangetypedef)
- [MeshDataTypeDef](./type_defs.md#meshdatatypedef)
- [MeshRefTypeDef](./type_defs.md#meshreftypedef)
- [MeshSpecTypeDef](./type_defs.md#meshspectypedef)
- [MeshStatusTypeDef](./type_defs.md#meshstatustypedef)
- [OutlierDetectionTypeDef](./type_defs.md#outlierdetectiontypedef)
- [PortMappingTypeDef](./type_defs.md#portmappingtypedef)
- [ResourceMetadataTypeDef](./type_defs.md#resourcemetadatatypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RouteDataTypeDef](./type_defs.md#routedatatypedef)
- [RouteRefTypeDef](./type_defs.md#routereftypedef)
- [RouteSpecTypeDef](./type_defs.md#routespectypedef)
- [RouteStatusTypeDef](./type_defs.md#routestatustypedef)
- [ServiceDiscoveryTypeDef](./type_defs.md#servicediscoverytypedef)
- [SubjectAlternativeNameMatchersTypeDef](./type_defs.md#subjectalternativenamematcherstypedef)
- [SubjectAlternativeNamesTypeDef](./type_defs.md#subjectalternativenamestypedef)
- [TagRefTypeDef](./type_defs.md#tagreftypedef)
- [TcpRouteActionTypeDef](./type_defs.md#tcprouteactiontypedef)
- [TcpRouteTypeDef](./type_defs.md#tcproutetypedef)
- [TcpTimeoutTypeDef](./type_defs.md#tcptimeouttypedef)
- [TlsValidationContextAcmTrustTypeDef](./type_defs.md#tlsvalidationcontextacmtrusttypedef)
- [TlsValidationContextFileTrustTypeDef](./type_defs.md#tlsvalidationcontextfiletrusttypedef)
- [TlsValidationContextSdsTrustTypeDef](./type_defs.md#tlsvalidationcontextsdstrusttypedef)
- [TlsValidationContextTrustTypeDef](./type_defs.md#tlsvalidationcontexttrusttypedef)
- [TlsValidationContextTypeDef](./type_defs.md#tlsvalidationcontexttypedef)
- [VirtualGatewayAccessLogTypeDef](./type_defs.md#virtualgatewayaccesslogtypedef)
- [VirtualGatewayBackendDefaultsTypeDef](./type_defs.md#virtualgatewaybackenddefaultstypedef)
- [VirtualGatewayClientPolicyTlsTypeDef](./type_defs.md#virtualgatewayclientpolicytlstypedef)
- [VirtualGatewayClientPolicyTypeDef](./type_defs.md#virtualgatewayclientpolicytypedef)
- [VirtualGatewayClientTlsCertificateTypeDef](./type_defs.md#virtualgatewayclienttlscertificatetypedef)
- [VirtualGatewayConnectionPoolTypeDef](./type_defs.md#virtualgatewayconnectionpooltypedef)
- [VirtualGatewayDataTypeDef](./type_defs.md#virtualgatewaydatatypedef)
- [VirtualGatewayFileAccessLogTypeDef](./type_defs.md#virtualgatewayfileaccesslogtypedef)
- [VirtualGatewayGrpcConnectionPoolTypeDef](./type_defs.md#virtualgatewaygrpcconnectionpooltypedef)
- [VirtualGatewayHealthCheckPolicyTypeDef](./type_defs.md#virtualgatewayhealthcheckpolicytypedef)
- [VirtualGatewayHttp2ConnectionPoolTypeDef](./type_defs.md#virtualgatewayhttp2connectionpooltypedef)
- [VirtualGatewayHttpConnectionPoolTypeDef](./type_defs.md#virtualgatewayhttpconnectionpooltypedef)
- [VirtualGatewayListenerTlsAcmCertificateTypeDef](./type_defs.md#virtualgatewaylistenertlsacmcertificatetypedef)
- [VirtualGatewayListenerTlsCertificateTypeDef](./type_defs.md#virtualgatewaylistenertlscertificatetypedef)
- [VirtualGatewayListenerTlsFileCertificateTypeDef](./type_defs.md#virtualgatewaylistenertlsfilecertificatetypedef)
- [VirtualGatewayListenerTlsSdsCertificateTypeDef](./type_defs.md#virtualgatewaylistenertlssdscertificatetypedef)
- [VirtualGatewayListenerTlsTypeDef](./type_defs.md#virtualgatewaylistenertlstypedef)
- [VirtualGatewayListenerTlsValidationContextTrustTypeDef](./type_defs.md#virtualgatewaylistenertlsvalidationcontexttrusttypedef)
- [VirtualGatewayListenerTlsValidationContextTypeDef](./type_defs.md#virtualgatewaylistenertlsvalidationcontexttypedef)
- [VirtualGatewayListenerTypeDef](./type_defs.md#virtualgatewaylistenertypedef)
- [VirtualGatewayLoggingTypeDef](./type_defs.md#virtualgatewayloggingtypedef)
- [VirtualGatewayPortMappingTypeDef](./type_defs.md#virtualgatewayportmappingtypedef)
- [VirtualGatewayRefTypeDef](./type_defs.md#virtualgatewayreftypedef)
- [VirtualGatewaySpecTypeDef](./type_defs.md#virtualgatewayspectypedef)
- [VirtualGatewayStatusTypeDef](./type_defs.md#virtualgatewaystatustypedef)
- [VirtualGatewayTlsValidationContextAcmTrustTypeDef](./type_defs.md#virtualgatewaytlsvalidationcontextacmtrusttypedef)
- [VirtualGatewayTlsValidationContextFileTrustTypeDef](./type_defs.md#virtualgatewaytlsvalidationcontextfiletrusttypedef)
- [VirtualGatewayTlsValidationContextSdsTrustTypeDef](./type_defs.md#virtualgatewaytlsvalidationcontextsdstrusttypedef)
- [VirtualGatewayTlsValidationContextTrustTypeDef](./type_defs.md#virtualgatewaytlsvalidationcontexttrusttypedef)
- [VirtualGatewayTlsValidationContextTypeDef](./type_defs.md#virtualgatewaytlsvalidationcontexttypedef)
- [VirtualNodeConnectionPoolTypeDef](./type_defs.md#virtualnodeconnectionpooltypedef)
- [VirtualNodeDataTypeDef](./type_defs.md#virtualnodedatatypedef)
- [VirtualNodeGrpcConnectionPoolTypeDef](./type_defs.md#virtualnodegrpcconnectionpooltypedef)
- [VirtualNodeHttp2ConnectionPoolTypeDef](./type_defs.md#virtualnodehttp2connectionpooltypedef)
- [VirtualNodeHttpConnectionPoolTypeDef](./type_defs.md#virtualnodehttpconnectionpooltypedef)
- [VirtualNodeRefTypeDef](./type_defs.md#virtualnodereftypedef)
- [VirtualNodeServiceProviderTypeDef](./type_defs.md#virtualnodeserviceprovidertypedef)
- [VirtualNodeSpecTypeDef](./type_defs.md#virtualnodespectypedef)
- [VirtualNodeStatusTypeDef](./type_defs.md#virtualnodestatustypedef)
- [VirtualNodeTcpConnectionPoolTypeDef](./type_defs.md#virtualnodetcpconnectionpooltypedef)
- [VirtualRouterDataTypeDef](./type_defs.md#virtualrouterdatatypedef)
- [VirtualRouterListenerTypeDef](./type_defs.md#virtualrouterlistenertypedef)
- [VirtualRouterRefTypeDef](./type_defs.md#virtualrouterreftypedef)
- [VirtualRouterServiceProviderTypeDef](./type_defs.md#virtualrouterserviceprovidertypedef)
- [VirtualRouterSpecTypeDef](./type_defs.md#virtualrouterspectypedef)
- [VirtualRouterStatusTypeDef](./type_defs.md#virtualrouterstatustypedef)
- [VirtualServiceBackendTypeDef](./type_defs.md#virtualservicebackendtypedef)
- [VirtualServiceDataTypeDef](./type_defs.md#virtualservicedatatypedef)
- [VirtualServiceProviderTypeDef](./type_defs.md#virtualserviceprovidertypedef)
- [VirtualServiceRefTypeDef](./type_defs.md#virtualservicereftypedef)
- [VirtualServiceSpecTypeDef](./type_defs.md#virtualservicespectypedef)
- [VirtualServiceStatusTypeDef](./type_defs.md#virtualservicestatustypedef)
- [WeightedTargetTypeDef](./type_defs.md#weightedtargettypedef)
- [CreateGatewayRouteOutputTypeDef](./type_defs.md#creategatewayrouteoutputtypedef)
- [CreateMeshOutputTypeDef](./type_defs.md#createmeshoutputtypedef)
- [CreateRouteOutputTypeDef](./type_defs.md#createrouteoutputtypedef)
- [CreateVirtualGatewayOutputTypeDef](./type_defs.md#createvirtualgatewayoutputtypedef)
- [CreateVirtualNodeOutputTypeDef](./type_defs.md#createvirtualnodeoutputtypedef)
- [CreateVirtualRouterOutputTypeDef](./type_defs.md#createvirtualrouteroutputtypedef)
- [CreateVirtualServiceOutputTypeDef](./type_defs.md#createvirtualserviceoutputtypedef)
- [DeleteGatewayRouteOutputTypeDef](./type_defs.md#deletegatewayrouteoutputtypedef)
- [DeleteMeshOutputTypeDef](./type_defs.md#deletemeshoutputtypedef)
- [DeleteRouteOutputTypeDef](./type_defs.md#deleterouteoutputtypedef)
- [DeleteVirtualGatewayOutputTypeDef](./type_defs.md#deletevirtualgatewayoutputtypedef)
- [DeleteVirtualNodeOutputTypeDef](./type_defs.md#deletevirtualnodeoutputtypedef)
- [DeleteVirtualRouterOutputTypeDef](./type_defs.md#deletevirtualrouteroutputtypedef)
- [DeleteVirtualServiceOutputTypeDef](./type_defs.md#deletevirtualserviceoutputtypedef)
- [DescribeGatewayRouteOutputTypeDef](./type_defs.md#describegatewayrouteoutputtypedef)
- [DescribeMeshOutputTypeDef](./type_defs.md#describemeshoutputtypedef)
- [DescribeRouteOutputTypeDef](./type_defs.md#describerouteoutputtypedef)
- [DescribeVirtualGatewayOutputTypeDef](./type_defs.md#describevirtualgatewayoutputtypedef)
- [DescribeVirtualNodeOutputTypeDef](./type_defs.md#describevirtualnodeoutputtypedef)
- [DescribeVirtualRouterOutputTypeDef](./type_defs.md#describevirtualrouteroutputtypedef)
- [DescribeVirtualServiceOutputTypeDef](./type_defs.md#describevirtualserviceoutputtypedef)
- [ListGatewayRoutesOutputTypeDef](./type_defs.md#listgatewayroutesoutputtypedef)
- [ListMeshesOutputTypeDef](./type_defs.md#listmeshesoutputtypedef)
- [ListRoutesOutputTypeDef](./type_defs.md#listroutesoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ListVirtualGatewaysOutputTypeDef](./type_defs.md#listvirtualgatewaysoutputtypedef)
- [ListVirtualNodesOutputTypeDef](./type_defs.md#listvirtualnodesoutputtypedef)
- [ListVirtualRoutersOutputTypeDef](./type_defs.md#listvirtualroutersoutputtypedef)
- [ListVirtualServicesOutputTypeDef](./type_defs.md#listvirtualservicesoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateGatewayRouteOutputTypeDef](./type_defs.md#updategatewayrouteoutputtypedef)
- [UpdateMeshOutputTypeDef](./type_defs.md#updatemeshoutputtypedef)
- [UpdateRouteOutputTypeDef](./type_defs.md#updaterouteoutputtypedef)
- [UpdateVirtualGatewayOutputTypeDef](./type_defs.md#updatevirtualgatewayoutputtypedef)
- [UpdateVirtualNodeOutputTypeDef](./type_defs.md#updatevirtualnodeoutputtypedef)
- [UpdateVirtualRouterOutputTypeDef](./type_defs.md#updatevirtualrouteroutputtypedef)
- [UpdateVirtualServiceOutputTypeDef](./type_defs.md#updatevirtualserviceoutputtypedef)
