# Structures for boto3 AppMesh module

> [Index](../index.md) > [AppMesh](./index.md) > Structures

Auto-generated documentation for [AppMesh](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh)
type annotations stubs module [mypy_boto3_appmesh](https://pypi.org/project/mypy-boto3-appmesh/).

- [Structures for boto3 AppMesh module](#structures-for-boto3-appmesh-module)
  - [AccessLogTypeDef](#accesslogtypedef)
  - [AwsCloudMapInstanceAttributeTypeDef](#awscloudmapinstanceattributetypedef)
  - [AwsCloudMapServiceDiscoveryTypeDef](#awscloudmapservicediscoverytypedef)
  - [BackendDefaultsTypeDef](#backenddefaultstypedef)
  - [BackendTypeDef](#backendtypedef)
  - [ClientPolicyTlsTypeDef](#clientpolicytlstypedef)
  - [ClientPolicyTypeDef](#clientpolicytypedef)
  - [ClientTlsCertificateTypeDef](#clienttlscertificatetypedef)
  - [DnsServiceDiscoveryTypeDef](#dnsservicediscoverytypedef)
  - [DurationTypeDef](#durationtypedef)
  - [EgressFilterTypeDef](#egressfiltertypedef)
  - [FileAccessLogTypeDef](#fileaccesslogtypedef)
  - [GatewayRouteDataTypeDef](#gatewayroutedatatypedef)
  - [GatewayRouteRefTypeDef](#gatewayroutereftypedef)
  - [GatewayRouteSpecTypeDef](#gatewayroutespectypedef)
  - [GatewayRouteStatusTypeDef](#gatewayroutestatustypedef)
  - [GatewayRouteTargetTypeDef](#gatewayroutetargettypedef)
  - [GatewayRouteVirtualServiceTypeDef](#gatewayroutevirtualservicetypedef)
  - [GrpcGatewayRouteActionTypeDef](#grpcgatewayrouteactiontypedef)
  - [GrpcGatewayRouteMatchTypeDef](#grpcgatewayroutematchtypedef)
  - [GrpcGatewayRouteTypeDef](#grpcgatewayroutetypedef)
  - [GrpcRetryPolicyTypeDef](#grpcretrypolicytypedef)
  - [GrpcRouteActionTypeDef](#grpcrouteactiontypedef)
  - [GrpcRouteMatchTypeDef](#grpcroutematchtypedef)
  - [GrpcRouteMetadataMatchMethodTypeDef](#grpcroutemetadatamatchmethodtypedef)
  - [GrpcRouteMetadataTypeDef](#grpcroutemetadatatypedef)
  - [GrpcRouteTypeDef](#grpcroutetypedef)
  - [GrpcTimeoutTypeDef](#grpctimeouttypedef)
  - [HeaderMatchMethodTypeDef](#headermatchmethodtypedef)
  - [HealthCheckPolicyTypeDef](#healthcheckpolicytypedef)
  - [HttpGatewayRouteActionTypeDef](#httpgatewayrouteactiontypedef)
  - [HttpGatewayRouteMatchTypeDef](#httpgatewayroutematchtypedef)
  - [HttpGatewayRouteTypeDef](#httpgatewayroutetypedef)
  - [HttpRetryPolicyTypeDef](#httpretrypolicytypedef)
  - [HttpRouteActionTypeDef](#httprouteactiontypedef)
  - [HttpRouteHeaderTypeDef](#httprouteheadertypedef)
  - [HttpRouteMatchTypeDef](#httproutematchtypedef)
  - [HttpRouteTypeDef](#httproutetypedef)
  - [HttpTimeoutTypeDef](#httptimeouttypedef)
  - [ListenerTimeoutTypeDef](#listenertimeouttypedef)
  - [ListenerTlsAcmCertificateTypeDef](#listenertlsacmcertificatetypedef)
  - [ListenerTlsCertificateTypeDef](#listenertlscertificatetypedef)
  - [ListenerTlsFileCertificateTypeDef](#listenertlsfilecertificatetypedef)
  - [ListenerTlsSdsCertificateTypeDef](#listenertlssdscertificatetypedef)
  - [ListenerTlsTypeDef](#listenertlstypedef)
  - [ListenerTlsValidationContextTrustTypeDef](#listenertlsvalidationcontexttrusttypedef)
  - [ListenerTlsValidationContextTypeDef](#listenertlsvalidationcontexttypedef)
  - [ListenerTypeDef](#listenertypedef)
  - [LoggingTypeDef](#loggingtypedef)
  - [MatchRangeTypeDef](#matchrangetypedef)
  - [MeshDataTypeDef](#meshdatatypedef)
  - [MeshRefTypeDef](#meshreftypedef)
  - [MeshSpecTypeDef](#meshspectypedef)
  - [MeshStatusTypeDef](#meshstatustypedef)
  - [OutlierDetectionTypeDef](#outlierdetectiontypedef)
  - [PortMappingTypeDef](#portmappingtypedef)
  - [ResourceMetadataTypeDef](#resourcemetadatatypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RouteDataTypeDef](#routedatatypedef)
  - [RouteRefTypeDef](#routereftypedef)
  - [RouteSpecTypeDef](#routespectypedef)
  - [RouteStatusTypeDef](#routestatustypedef)
  - [ServiceDiscoveryTypeDef](#servicediscoverytypedef)
  - [SubjectAlternativeNameMatchersTypeDef](#subjectalternativenamematcherstypedef)
  - [SubjectAlternativeNamesTypeDef](#subjectalternativenamestypedef)
  - [TagRefTypeDef](#tagreftypedef)
  - [TcpRouteActionTypeDef](#tcprouteactiontypedef)
  - [TcpRouteTypeDef](#tcproutetypedef)
  - [TcpTimeoutTypeDef](#tcptimeouttypedef)
  - [TlsValidationContextAcmTrustTypeDef](#tlsvalidationcontextacmtrusttypedef)
  - [TlsValidationContextFileTrustTypeDef](#tlsvalidationcontextfiletrusttypedef)
  - [TlsValidationContextSdsTrustTypeDef](#tlsvalidationcontextsdstrusttypedef)
  - [TlsValidationContextTrustTypeDef](#tlsvalidationcontexttrusttypedef)
  - [TlsValidationContextTypeDef](#tlsvalidationcontexttypedef)
  - [VirtualGatewayAccessLogTypeDef](#virtualgatewayaccesslogtypedef)
  - [VirtualGatewayBackendDefaultsTypeDef](#virtualgatewaybackenddefaultstypedef)
  - [VirtualGatewayClientPolicyTlsTypeDef](#virtualgatewayclientpolicytlstypedef)
  - [VirtualGatewayClientPolicyTypeDef](#virtualgatewayclientpolicytypedef)
  - [VirtualGatewayClientTlsCertificateTypeDef](#virtualgatewayclienttlscertificatetypedef)
  - [VirtualGatewayConnectionPoolTypeDef](#virtualgatewayconnectionpooltypedef)
  - [VirtualGatewayDataTypeDef](#virtualgatewaydatatypedef)
  - [VirtualGatewayFileAccessLogTypeDef](#virtualgatewayfileaccesslogtypedef)
  - [VirtualGatewayGrpcConnectionPoolTypeDef](#virtualgatewaygrpcconnectionpooltypedef)
  - [VirtualGatewayHealthCheckPolicyTypeDef](#virtualgatewayhealthcheckpolicytypedef)
  - [VirtualGatewayHttp2ConnectionPoolTypeDef](#virtualgatewayhttp2connectionpooltypedef)
  - [VirtualGatewayHttpConnectionPoolTypeDef](#virtualgatewayhttpconnectionpooltypedef)
  - [VirtualGatewayListenerTlsAcmCertificateTypeDef](#virtualgatewaylistenertlsacmcertificatetypedef)
  - [VirtualGatewayListenerTlsCertificateTypeDef](#virtualgatewaylistenertlscertificatetypedef)
  - [VirtualGatewayListenerTlsFileCertificateTypeDef](#virtualgatewaylistenertlsfilecertificatetypedef)
  - [VirtualGatewayListenerTlsSdsCertificateTypeDef](#virtualgatewaylistenertlssdscertificatetypedef)
  - [VirtualGatewayListenerTlsTypeDef](#virtualgatewaylistenertlstypedef)
  - [VirtualGatewayListenerTlsValidationContextTrustTypeDef](#virtualgatewaylistenertlsvalidationcontexttrusttypedef)
  - [VirtualGatewayListenerTlsValidationContextTypeDef](#virtualgatewaylistenertlsvalidationcontexttypedef)
  - [VirtualGatewayListenerTypeDef](#virtualgatewaylistenertypedef)
  - [VirtualGatewayLoggingTypeDef](#virtualgatewayloggingtypedef)
  - [VirtualGatewayPortMappingTypeDef](#virtualgatewayportmappingtypedef)
  - [VirtualGatewayRefTypeDef](#virtualgatewayreftypedef)
  - [VirtualGatewaySpecTypeDef](#virtualgatewayspectypedef)
  - [VirtualGatewayStatusTypeDef](#virtualgatewaystatustypedef)
  - [VirtualGatewayTlsValidationContextAcmTrustTypeDef](#virtualgatewaytlsvalidationcontextacmtrusttypedef)
  - [VirtualGatewayTlsValidationContextFileTrustTypeDef](#virtualgatewaytlsvalidationcontextfiletrusttypedef)
  - [VirtualGatewayTlsValidationContextSdsTrustTypeDef](#virtualgatewaytlsvalidationcontextsdstrusttypedef)
  - [VirtualGatewayTlsValidationContextTrustTypeDef](#virtualgatewaytlsvalidationcontexttrusttypedef)
  - [VirtualGatewayTlsValidationContextTypeDef](#virtualgatewaytlsvalidationcontexttypedef)
  - [VirtualNodeConnectionPoolTypeDef](#virtualnodeconnectionpooltypedef)
  - [VirtualNodeDataTypeDef](#virtualnodedatatypedef)
  - [VirtualNodeGrpcConnectionPoolTypeDef](#virtualnodegrpcconnectionpooltypedef)
  - [VirtualNodeHttp2ConnectionPoolTypeDef](#virtualnodehttp2connectionpooltypedef)
  - [VirtualNodeHttpConnectionPoolTypeDef](#virtualnodehttpconnectionpooltypedef)
  - [VirtualNodeRefTypeDef](#virtualnodereftypedef)
  - [VirtualNodeServiceProviderTypeDef](#virtualnodeserviceprovidertypedef)
  - [VirtualNodeSpecTypeDef](#virtualnodespectypedef)
  - [VirtualNodeStatusTypeDef](#virtualnodestatustypedef)
  - [VirtualNodeTcpConnectionPoolTypeDef](#virtualnodetcpconnectionpooltypedef)
  - [VirtualRouterDataTypeDef](#virtualrouterdatatypedef)
  - [VirtualRouterListenerTypeDef](#virtualrouterlistenertypedef)
  - [VirtualRouterRefTypeDef](#virtualrouterreftypedef)
  - [VirtualRouterServiceProviderTypeDef](#virtualrouterserviceprovidertypedef)
  - [VirtualRouterSpecTypeDef](#virtualrouterspectypedef)
  - [VirtualRouterStatusTypeDef](#virtualrouterstatustypedef)
  - [VirtualServiceBackendTypeDef](#virtualservicebackendtypedef)
  - [VirtualServiceDataTypeDef](#virtualservicedatatypedef)
  - [VirtualServiceProviderTypeDef](#virtualserviceprovidertypedef)
  - [VirtualServiceRefTypeDef](#virtualservicereftypedef)
  - [VirtualServiceSpecTypeDef](#virtualservicespectypedef)
  - [VirtualServiceStatusTypeDef](#virtualservicestatustypedef)
  - [WeightedTargetTypeDef](#weightedtargettypedef)
  - [CreateGatewayRouteOutputTypeDef](#creategatewayrouteoutputtypedef)
  - [CreateMeshOutputTypeDef](#createmeshoutputtypedef)
  - [CreateRouteOutputTypeDef](#createrouteoutputtypedef)
  - [CreateVirtualGatewayOutputTypeDef](#createvirtualgatewayoutputtypedef)
  - [CreateVirtualNodeOutputTypeDef](#createvirtualnodeoutputtypedef)
  - [CreateVirtualRouterOutputTypeDef](#createvirtualrouteroutputtypedef)
  - [CreateVirtualServiceOutputTypeDef](#createvirtualserviceoutputtypedef)
  - [DeleteGatewayRouteOutputTypeDef](#deletegatewayrouteoutputtypedef)
  - [DeleteMeshOutputTypeDef](#deletemeshoutputtypedef)
  - [DeleteRouteOutputTypeDef](#deleterouteoutputtypedef)
  - [DeleteVirtualGatewayOutputTypeDef](#deletevirtualgatewayoutputtypedef)
  - [DeleteVirtualNodeOutputTypeDef](#deletevirtualnodeoutputtypedef)
  - [DeleteVirtualRouterOutputTypeDef](#deletevirtualrouteroutputtypedef)
  - [DeleteVirtualServiceOutputTypeDef](#deletevirtualserviceoutputtypedef)
  - [DescribeGatewayRouteOutputTypeDef](#describegatewayrouteoutputtypedef)
  - [DescribeMeshOutputTypeDef](#describemeshoutputtypedef)
  - [DescribeRouteOutputTypeDef](#describerouteoutputtypedef)
  - [DescribeVirtualGatewayOutputTypeDef](#describevirtualgatewayoutputtypedef)
  - [DescribeVirtualNodeOutputTypeDef](#describevirtualnodeoutputtypedef)
  - [DescribeVirtualRouterOutputTypeDef](#describevirtualrouteroutputtypedef)
  - [DescribeVirtualServiceOutputTypeDef](#describevirtualserviceoutputtypedef)
  - [ListGatewayRoutesOutputTypeDef](#listgatewayroutesoutputtypedef)
  - [ListMeshesOutputTypeDef](#listmeshesoutputtypedef)
  - [ListRoutesOutputTypeDef](#listroutesoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ListVirtualGatewaysOutputTypeDef](#listvirtualgatewaysoutputtypedef)
  - [ListVirtualNodesOutputTypeDef](#listvirtualnodesoutputtypedef)
  - [ListVirtualRoutersOutputTypeDef](#listvirtualroutersoutputtypedef)
  - [ListVirtualServicesOutputTypeDef](#listvirtualservicesoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateGatewayRouteOutputTypeDef](#updategatewayrouteoutputtypedef)
  - [UpdateMeshOutputTypeDef](#updatemeshoutputtypedef)
  - [UpdateRouteOutputTypeDef](#updaterouteoutputtypedef)
  - [UpdateVirtualGatewayOutputTypeDef](#updatevirtualgatewayoutputtypedef)
  - [UpdateVirtualNodeOutputTypeDef](#updatevirtualnodeoutputtypedef)
  - [UpdateVirtualRouterOutputTypeDef](#updatevirtualrouteroutputtypedef)
  - [UpdateVirtualServiceOutputTypeDef](#updatevirtualserviceoutputtypedef)

## AccessLogTypeDef

```python
from mypy_boto3_appmesh.type_defs import AccessLogTypeDef
```




Optional fields:
- `file`: `"FileAccessLogTypeDef"`


## AwsCloudMapInstanceAttributeTypeDef

```python
from mypy_boto3_appmesh.type_defs import AwsCloudMapInstanceAttributeTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## AwsCloudMapServiceDiscoveryTypeDef

```python
from mypy_boto3_appmesh.type_defs import AwsCloudMapServiceDiscoveryTypeDef
```


Required fields:
- `namespaceName`: `str`
- `serviceName`: `str`



Optional fields:
- `attributes`: `List["AwsCloudMapInstanceAttributeTypeDef"]`


## BackendDefaultsTypeDef

```python
from mypy_boto3_appmesh.type_defs import BackendDefaultsTypeDef
```




Optional fields:
- `clientPolicy`: `"ClientPolicyTypeDef"`


## BackendTypeDef

```python
from mypy_boto3_appmesh.type_defs import BackendTypeDef
```




Optional fields:
- `virtualService`: `"VirtualServiceBackendTypeDef"`


## ClientPolicyTlsTypeDef

```python
from mypy_boto3_appmesh.type_defs import ClientPolicyTlsTypeDef
```


Required fields:
- `validation`: `"TlsValidationContextTypeDef"`



Optional fields:
- `certificate`: `"ClientTlsCertificateTypeDef"`
- `enforce`: `bool`
- `ports`: `List[int]`


## ClientPolicyTypeDef

```python
from mypy_boto3_appmesh.type_defs import ClientPolicyTypeDef
```




Optional fields:
- `tls`: `"ClientPolicyTlsTypeDef"`


## ClientTlsCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import ClientTlsCertificateTypeDef
```




Optional fields:
- `file`: `"ListenerTlsFileCertificateTypeDef"`
- `sds`: `"ListenerTlsSdsCertificateTypeDef"`


## DnsServiceDiscoveryTypeDef

```python
from mypy_boto3_appmesh.type_defs import DnsServiceDiscoveryTypeDef
```


Required fields:
- `hostname`: `str`




## DurationTypeDef

```python
from mypy_boto3_appmesh.type_defs import DurationTypeDef
```




Optional fields:
- `unit`: `DurationUnit`
- `value`: `int`


## EgressFilterTypeDef

```python
from mypy_boto3_appmesh.type_defs import EgressFilterTypeDef
```


Required fields:
- `type`: `EgressFilterType`




## FileAccessLogTypeDef

```python
from mypy_boto3_appmesh.type_defs import FileAccessLogTypeDef
```


Required fields:
- `path`: `str`




## GatewayRouteDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import GatewayRouteDataTypeDef
```


Required fields:
- `gatewayRouteName`: `str`
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `spec`: `"GatewayRouteSpecTypeDef"`
- `status`: `"GatewayRouteStatusTypeDef"`
- `virtualGatewayName`: `str`




## GatewayRouteRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import GatewayRouteRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `gatewayRouteName`: `str`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `version`: `int`
- `virtualGatewayName`: `str`




## GatewayRouteSpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import GatewayRouteSpecTypeDef
```




Optional fields:
- `grpcRoute`: `"GrpcGatewayRouteTypeDef"`
- `http2Route`: `"HttpGatewayRouteTypeDef"`
- `httpRoute`: `"HttpGatewayRouteTypeDef"`


## GatewayRouteStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import GatewayRouteStatusTypeDef
```


Required fields:
- `status`: `GatewayRouteStatusCode`




## GatewayRouteTargetTypeDef

```python
from mypy_boto3_appmesh.type_defs import GatewayRouteTargetTypeDef
```


Required fields:
- `virtualService`: `"GatewayRouteVirtualServiceTypeDef"`




## GatewayRouteVirtualServiceTypeDef

```python
from mypy_boto3_appmesh.type_defs import GatewayRouteVirtualServiceTypeDef
```


Required fields:
- `virtualServiceName`: `str`




## GrpcGatewayRouteActionTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcGatewayRouteActionTypeDef
```


Required fields:
- `target`: `"GatewayRouteTargetTypeDef"`




## GrpcGatewayRouteMatchTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcGatewayRouteMatchTypeDef
```




Optional fields:
- `serviceName`: `str`


## GrpcGatewayRouteTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcGatewayRouteTypeDef
```


Required fields:
- `action`: `"GrpcGatewayRouteActionTypeDef"`
- `match`: `"GrpcGatewayRouteMatchTypeDef"`




## GrpcRetryPolicyTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcRetryPolicyTypeDef
```


Required fields:
- `maxRetries`: `int`
- `perRetryTimeout`: `"DurationTypeDef"`



Optional fields:
- `grpcRetryEvents`: `List[GrpcRetryPolicyEvent]`
- `httpRetryEvents`: `List[str]`
- `tcpRetryEvents`: `List[TcpRetryPolicyEvent]`


## GrpcRouteActionTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcRouteActionTypeDef
```


Required fields:
- `weightedTargets`: `List["WeightedTargetTypeDef"]`




## GrpcRouteMatchTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcRouteMatchTypeDef
```




Optional fields:
- `metadata`: `List["GrpcRouteMetadataTypeDef"]`
- `methodName`: `str`
- `serviceName`: `str`


## GrpcRouteMetadataMatchMethodTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcRouteMetadataMatchMethodTypeDef
```




Optional fields:
- `exact`: `str`
- `prefix`: `str`
- `range`: `"MatchRangeTypeDef"`
- `regex`: `str`
- `suffix`: `str`


## GrpcRouteMetadataTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcRouteMetadataTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `invert`: `bool`
- `match`: `"GrpcRouteMetadataMatchMethodTypeDef"`


## GrpcRouteTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcRouteTypeDef
```


Required fields:
- `action`: `"GrpcRouteActionTypeDef"`
- `match`: `"GrpcRouteMatchTypeDef"`



Optional fields:
- `retryPolicy`: `"GrpcRetryPolicyTypeDef"`
- `timeout`: `"GrpcTimeoutTypeDef"`


## GrpcTimeoutTypeDef

```python
from mypy_boto3_appmesh.type_defs import GrpcTimeoutTypeDef
```




Optional fields:
- `idle`: `"DurationTypeDef"`
- `perRequest`: `"DurationTypeDef"`


## HeaderMatchMethodTypeDef

```python
from mypy_boto3_appmesh.type_defs import HeaderMatchMethodTypeDef
```




Optional fields:
- `exact`: `str`
- `prefix`: `str`
- `range`: `"MatchRangeTypeDef"`
- `regex`: `str`
- `suffix`: `str`


## HealthCheckPolicyTypeDef

```python
from mypy_boto3_appmesh.type_defs import HealthCheckPolicyTypeDef
```


Required fields:
- `healthyThreshold`: `int`
- `intervalMillis`: `int`
- `protocol`: `PortProtocol`
- `timeoutMillis`: `int`
- `unhealthyThreshold`: `int`



Optional fields:
- `path`: `str`
- `port`: `int`


## HttpGatewayRouteActionTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpGatewayRouteActionTypeDef
```


Required fields:
- `target`: `"GatewayRouteTargetTypeDef"`




## HttpGatewayRouteMatchTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpGatewayRouteMatchTypeDef
```


Required fields:
- `prefix`: `str`




## HttpGatewayRouteTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpGatewayRouteTypeDef
```


Required fields:
- `action`: `"HttpGatewayRouteActionTypeDef"`
- `match`: `"HttpGatewayRouteMatchTypeDef"`




## HttpRetryPolicyTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpRetryPolicyTypeDef
```


Required fields:
- `maxRetries`: `int`
- `perRetryTimeout`: `"DurationTypeDef"`



Optional fields:
- `httpRetryEvents`: `List[str]`
- `tcpRetryEvents`: `List[TcpRetryPolicyEvent]`


## HttpRouteActionTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpRouteActionTypeDef
```


Required fields:
- `weightedTargets`: `List["WeightedTargetTypeDef"]`




## HttpRouteHeaderTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpRouteHeaderTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `invert`: `bool`
- `match`: `"HeaderMatchMethodTypeDef"`


## HttpRouteMatchTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpRouteMatchTypeDef
```


Required fields:
- `prefix`: `str`



Optional fields:
- `headers`: `List["HttpRouteHeaderTypeDef"]`
- `method`: `HttpMethod`
- `scheme`: `HttpScheme`


## HttpRouteTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpRouteTypeDef
```


Required fields:
- `action`: `"HttpRouteActionTypeDef"`
- `match`: `"HttpRouteMatchTypeDef"`



Optional fields:
- `retryPolicy`: `"HttpRetryPolicyTypeDef"`
- `timeout`: `"HttpTimeoutTypeDef"`


## HttpTimeoutTypeDef

```python
from mypy_boto3_appmesh.type_defs import HttpTimeoutTypeDef
```




Optional fields:
- `idle`: `"DurationTypeDef"`
- `perRequest`: `"DurationTypeDef"`


## ListenerTimeoutTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTimeoutTypeDef
```




Optional fields:
- `grpc`: `"GrpcTimeoutTypeDef"`
- `http`: `"HttpTimeoutTypeDef"`
- `http2`: `"HttpTimeoutTypeDef"`
- `tcp`: `"TcpTimeoutTypeDef"`


## ListenerTlsAcmCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsAcmCertificateTypeDef
```


Required fields:
- `certificateArn`: `str`




## ListenerTlsCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsCertificateTypeDef
```




Optional fields:
- `acm`: `"ListenerTlsAcmCertificateTypeDef"`
- `file`: `"ListenerTlsFileCertificateTypeDef"`
- `sds`: `"ListenerTlsSdsCertificateTypeDef"`


## ListenerTlsFileCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsFileCertificateTypeDef
```


Required fields:
- `certificateChain`: `str`
- `privateKey`: `str`




## ListenerTlsSdsCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsSdsCertificateTypeDef
```


Required fields:
- `secretName`: `str`




## ListenerTlsTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsTypeDef
```


Required fields:
- `certificate`: `"ListenerTlsCertificateTypeDef"`
- `mode`: `ListenerTlsMode`



Optional fields:
- `validation`: `"ListenerTlsValidationContextTypeDef"`


## ListenerTlsValidationContextTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsValidationContextTrustTypeDef
```




Optional fields:
- `file`: `"TlsValidationContextFileTrustTypeDef"`
- `sds`: `"TlsValidationContextSdsTrustTypeDef"`


## ListenerTlsValidationContextTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTlsValidationContextTypeDef
```


Required fields:
- `trust`: `"ListenerTlsValidationContextTrustTypeDef"`



Optional fields:
- `subjectAlternativeNames`: `"SubjectAlternativeNamesTypeDef"`


## ListenerTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListenerTypeDef
```


Required fields:
- `portMapping`: `"PortMappingTypeDef"`



Optional fields:
- `connectionPool`: `"VirtualNodeConnectionPoolTypeDef"`
- `healthCheck`: `"HealthCheckPolicyTypeDef"`
- `outlierDetection`: `"OutlierDetectionTypeDef"`
- `timeout`: `"ListenerTimeoutTypeDef"`
- `tls`: `"ListenerTlsTypeDef"`


## LoggingTypeDef

```python
from mypy_boto3_appmesh.type_defs import LoggingTypeDef
```




Optional fields:
- `accessLog`: `"AccessLogTypeDef"`


## MatchRangeTypeDef

```python
from mypy_boto3_appmesh.type_defs import MatchRangeTypeDef
```


Required fields:
- `end`: `int`
- `start`: `int`




## MeshDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import MeshDataTypeDef
```


Required fields:
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `spec`: `"MeshSpecTypeDef"`
- `status`: `"MeshStatusTypeDef"`




## MeshRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import MeshRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `version`: `int`




## MeshSpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import MeshSpecTypeDef
```




Optional fields:
- `egressFilter`: `"EgressFilterTypeDef"`


## MeshStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import MeshStatusTypeDef
```




Optional fields:
- `status`: `MeshStatusCode`


## OutlierDetectionTypeDef

```python
from mypy_boto3_appmesh.type_defs import OutlierDetectionTypeDef
```


Required fields:
- `baseEjectionDuration`: `"DurationTypeDef"`
- `interval`: `"DurationTypeDef"`
- `maxEjectionPercent`: `int`
- `maxServerErrors`: `int`




## PortMappingTypeDef

```python
from mypy_boto3_appmesh.type_defs import PortMappingTypeDef
```


Required fields:
- `port`: `int`
- `protocol`: `PortProtocol`




## ResourceMetadataTypeDef

```python
from mypy_boto3_appmesh.type_defs import ResourceMetadataTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `uid`: `str`
- `version`: `int`




## ResponseMetadata

```python
from mypy_boto3_appmesh.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RouteDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import RouteDataTypeDef
```


Required fields:
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `routeName`: `str`
- `spec`: `"RouteSpecTypeDef"`
- `status`: `"RouteStatusTypeDef"`
- `virtualRouterName`: `str`




## RouteRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import RouteRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `routeName`: `str`
- `version`: `int`
- `virtualRouterName`: `str`




## RouteSpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import RouteSpecTypeDef
```




Optional fields:
- `grpcRoute`: `"GrpcRouteTypeDef"`
- `http2Route`: `"HttpRouteTypeDef"`
- `httpRoute`: `"HttpRouteTypeDef"`
- `priority`: `int`
- `tcpRoute`: `"TcpRouteTypeDef"`


## RouteStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import RouteStatusTypeDef
```


Required fields:
- `status`: `RouteStatusCode`




## ServiceDiscoveryTypeDef

```python
from mypy_boto3_appmesh.type_defs import ServiceDiscoveryTypeDef
```




Optional fields:
- `awsCloudMap`: `"AwsCloudMapServiceDiscoveryTypeDef"`
- `dns`: `"DnsServiceDiscoveryTypeDef"`


## SubjectAlternativeNameMatchersTypeDef

```python
from mypy_boto3_appmesh.type_defs import SubjectAlternativeNameMatchersTypeDef
```


Required fields:
- `exact`: `List[str]`




## SubjectAlternativeNamesTypeDef

```python
from mypy_boto3_appmesh.type_defs import SubjectAlternativeNamesTypeDef
```


Required fields:
- `match`: `"SubjectAlternativeNameMatchersTypeDef"`




## TagRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import TagRefTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## TcpRouteActionTypeDef

```python
from mypy_boto3_appmesh.type_defs import TcpRouteActionTypeDef
```


Required fields:
- `weightedTargets`: `List["WeightedTargetTypeDef"]`




## TcpRouteTypeDef

```python
from mypy_boto3_appmesh.type_defs import TcpRouteTypeDef
```


Required fields:
- `action`: `"TcpRouteActionTypeDef"`



Optional fields:
- `timeout`: `"TcpTimeoutTypeDef"`


## TcpTimeoutTypeDef

```python
from mypy_boto3_appmesh.type_defs import TcpTimeoutTypeDef
```




Optional fields:
- `idle`: `"DurationTypeDef"`


## TlsValidationContextAcmTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import TlsValidationContextAcmTrustTypeDef
```


Required fields:
- `certificateAuthorityArns`: `List[str]`




## TlsValidationContextFileTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import TlsValidationContextFileTrustTypeDef
```


Required fields:
- `certificateChain`: `str`




## TlsValidationContextSdsTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import TlsValidationContextSdsTrustTypeDef
```


Required fields:
- `secretName`: `str`




## TlsValidationContextTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import TlsValidationContextTrustTypeDef
```




Optional fields:
- `acm`: `"TlsValidationContextAcmTrustTypeDef"`
- `file`: `"TlsValidationContextFileTrustTypeDef"`
- `sds`: `"TlsValidationContextSdsTrustTypeDef"`


## TlsValidationContextTypeDef

```python
from mypy_boto3_appmesh.type_defs import TlsValidationContextTypeDef
```


Required fields:
- `trust`: `"TlsValidationContextTrustTypeDef"`



Optional fields:
- `subjectAlternativeNames`: `"SubjectAlternativeNamesTypeDef"`


## VirtualGatewayAccessLogTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayAccessLogTypeDef
```




Optional fields:
- `file`: `"VirtualGatewayFileAccessLogTypeDef"`


## VirtualGatewayBackendDefaultsTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayBackendDefaultsTypeDef
```




Optional fields:
- `clientPolicy`: `"VirtualGatewayClientPolicyTypeDef"`


## VirtualGatewayClientPolicyTlsTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayClientPolicyTlsTypeDef
```


Required fields:
- `validation`: `"VirtualGatewayTlsValidationContextTypeDef"`



Optional fields:
- `certificate`: `"VirtualGatewayClientTlsCertificateTypeDef"`
- `enforce`: `bool`
- `ports`: `List[int]`


## VirtualGatewayClientPolicyTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayClientPolicyTypeDef
```




Optional fields:
- `tls`: `"VirtualGatewayClientPolicyTlsTypeDef"`


## VirtualGatewayClientTlsCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayClientTlsCertificateTypeDef
```




Optional fields:
- `file`: `"VirtualGatewayListenerTlsFileCertificateTypeDef"`
- `sds`: `"VirtualGatewayListenerTlsSdsCertificateTypeDef"`


## VirtualGatewayConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayConnectionPoolTypeDef
```




Optional fields:
- `grpc`: `"VirtualGatewayGrpcConnectionPoolTypeDef"`
- `http`: `"VirtualGatewayHttpConnectionPoolTypeDef"`
- `http2`: `"VirtualGatewayHttp2ConnectionPoolTypeDef"`


## VirtualGatewayDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayDataTypeDef
```


Required fields:
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `spec`: `"VirtualGatewaySpecTypeDef"`
- `status`: `"VirtualGatewayStatusTypeDef"`
- `virtualGatewayName`: `str`




## VirtualGatewayFileAccessLogTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayFileAccessLogTypeDef
```


Required fields:
- `path`: `str`




## VirtualGatewayGrpcConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayGrpcConnectionPoolTypeDef
```


Required fields:
- `maxRequests`: `int`




## VirtualGatewayHealthCheckPolicyTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayHealthCheckPolicyTypeDef
```


Required fields:
- `healthyThreshold`: `int`
- `intervalMillis`: `int`
- `protocol`: `VirtualGatewayPortProtocol`
- `timeoutMillis`: `int`
- `unhealthyThreshold`: `int`



Optional fields:
- `path`: `str`
- `port`: `int`


## VirtualGatewayHttp2ConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayHttp2ConnectionPoolTypeDef
```


Required fields:
- `maxRequests`: `int`




## VirtualGatewayHttpConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayHttpConnectionPoolTypeDef
```


Required fields:
- `maxConnections`: `int`



Optional fields:
- `maxPendingRequests`: `int`


## VirtualGatewayListenerTlsAcmCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsAcmCertificateTypeDef
```


Required fields:
- `certificateArn`: `str`




## VirtualGatewayListenerTlsCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsCertificateTypeDef
```




Optional fields:
- `acm`: `"VirtualGatewayListenerTlsAcmCertificateTypeDef"`
- `file`: `"VirtualGatewayListenerTlsFileCertificateTypeDef"`
- `sds`: `"VirtualGatewayListenerTlsSdsCertificateTypeDef"`


## VirtualGatewayListenerTlsFileCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsFileCertificateTypeDef
```


Required fields:
- `certificateChain`: `str`
- `privateKey`: `str`




## VirtualGatewayListenerTlsSdsCertificateTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsSdsCertificateTypeDef
```


Required fields:
- `secretName`: `str`




## VirtualGatewayListenerTlsTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsTypeDef
```


Required fields:
- `certificate`: `"VirtualGatewayListenerTlsCertificateTypeDef"`
- `mode`: `VirtualGatewayListenerTlsMode`



Optional fields:
- `validation`: `"VirtualGatewayListenerTlsValidationContextTypeDef"`


## VirtualGatewayListenerTlsValidationContextTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsValidationContextTrustTypeDef
```




Optional fields:
- `file`: `"VirtualGatewayTlsValidationContextFileTrustTypeDef"`
- `sds`: `"VirtualGatewayTlsValidationContextSdsTrustTypeDef"`


## VirtualGatewayListenerTlsValidationContextTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTlsValidationContextTypeDef
```


Required fields:
- `trust`: `"VirtualGatewayListenerTlsValidationContextTrustTypeDef"`



Optional fields:
- `subjectAlternativeNames`: `"SubjectAlternativeNamesTypeDef"`


## VirtualGatewayListenerTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayListenerTypeDef
```


Required fields:
- `portMapping`: `"VirtualGatewayPortMappingTypeDef"`



Optional fields:
- `connectionPool`: `"VirtualGatewayConnectionPoolTypeDef"`
- `healthCheck`: `"VirtualGatewayHealthCheckPolicyTypeDef"`
- `tls`: `"VirtualGatewayListenerTlsTypeDef"`


## VirtualGatewayLoggingTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayLoggingTypeDef
```




Optional fields:
- `accessLog`: `"VirtualGatewayAccessLogTypeDef"`


## VirtualGatewayPortMappingTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayPortMappingTypeDef
```


Required fields:
- `port`: `int`
- `protocol`: `VirtualGatewayPortProtocol`




## VirtualGatewayRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `version`: `int`
- `virtualGatewayName`: `str`




## VirtualGatewaySpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewaySpecTypeDef
```


Required fields:
- `listeners`: `List["VirtualGatewayListenerTypeDef"]`



Optional fields:
- `backendDefaults`: `"VirtualGatewayBackendDefaultsTypeDef"`
- `logging`: `"VirtualGatewayLoggingTypeDef"`


## VirtualGatewayStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayStatusTypeDef
```


Required fields:
- `status`: `VirtualGatewayStatusCode`




## VirtualGatewayTlsValidationContextAcmTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayTlsValidationContextAcmTrustTypeDef
```


Required fields:
- `certificateAuthorityArns`: `List[str]`




## VirtualGatewayTlsValidationContextFileTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayTlsValidationContextFileTrustTypeDef
```


Required fields:
- `certificateChain`: `str`




## VirtualGatewayTlsValidationContextSdsTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayTlsValidationContextSdsTrustTypeDef
```


Required fields:
- `secretName`: `str`




## VirtualGatewayTlsValidationContextTrustTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayTlsValidationContextTrustTypeDef
```




Optional fields:
- `acm`: `"VirtualGatewayTlsValidationContextAcmTrustTypeDef"`
- `file`: `"VirtualGatewayTlsValidationContextFileTrustTypeDef"`
- `sds`: `"VirtualGatewayTlsValidationContextSdsTrustTypeDef"`


## VirtualGatewayTlsValidationContextTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualGatewayTlsValidationContextTypeDef
```


Required fields:
- `trust`: `"VirtualGatewayTlsValidationContextTrustTypeDef"`



Optional fields:
- `subjectAlternativeNames`: `"SubjectAlternativeNamesTypeDef"`


## VirtualNodeConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeConnectionPoolTypeDef
```




Optional fields:
- `grpc`: `"VirtualNodeGrpcConnectionPoolTypeDef"`
- `http`: `"VirtualNodeHttpConnectionPoolTypeDef"`
- `http2`: `"VirtualNodeHttp2ConnectionPoolTypeDef"`
- `tcp`: `"VirtualNodeTcpConnectionPoolTypeDef"`


## VirtualNodeDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeDataTypeDef
```


Required fields:
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `spec`: `"VirtualNodeSpecTypeDef"`
- `status`: `"VirtualNodeStatusTypeDef"`
- `virtualNodeName`: `str`




## VirtualNodeGrpcConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeGrpcConnectionPoolTypeDef
```


Required fields:
- `maxRequests`: `int`




## VirtualNodeHttp2ConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeHttp2ConnectionPoolTypeDef
```


Required fields:
- `maxRequests`: `int`




## VirtualNodeHttpConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeHttpConnectionPoolTypeDef
```


Required fields:
- `maxConnections`: `int`



Optional fields:
- `maxPendingRequests`: `int`


## VirtualNodeRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `version`: `int`
- `virtualNodeName`: `str`




## VirtualNodeServiceProviderTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeServiceProviderTypeDef
```


Required fields:
- `virtualNodeName`: `str`




## VirtualNodeSpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeSpecTypeDef
```




Optional fields:
- `backendDefaults`: `"BackendDefaultsTypeDef"`
- `backends`: `List["BackendTypeDef"]`
- `listeners`: `List["ListenerTypeDef"]`
- `logging`: `"LoggingTypeDef"`
- `serviceDiscovery`: `"ServiceDiscoveryTypeDef"`


## VirtualNodeStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeStatusTypeDef
```


Required fields:
- `status`: `VirtualNodeStatusCode`




## VirtualNodeTcpConnectionPoolTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualNodeTcpConnectionPoolTypeDef
```


Required fields:
- `maxConnections`: `int`




## VirtualRouterDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualRouterDataTypeDef
```


Required fields:
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `spec`: `"VirtualRouterSpecTypeDef"`
- `status`: `"VirtualRouterStatusTypeDef"`
- `virtualRouterName`: `str`




## VirtualRouterListenerTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualRouterListenerTypeDef
```


Required fields:
- `portMapping`: `"PortMappingTypeDef"`




## VirtualRouterRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualRouterRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `version`: `int`
- `virtualRouterName`: `str`




## VirtualRouterServiceProviderTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualRouterServiceProviderTypeDef
```


Required fields:
- `virtualRouterName`: `str`




## VirtualRouterSpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualRouterSpecTypeDef
```




Optional fields:
- `listeners`: `List["VirtualRouterListenerTypeDef"]`


## VirtualRouterStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualRouterStatusTypeDef
```


Required fields:
- `status`: `VirtualRouterStatusCode`




## VirtualServiceBackendTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualServiceBackendTypeDef
```


Required fields:
- `virtualServiceName`: `str`



Optional fields:
- `clientPolicy`: `"ClientPolicyTypeDef"`


## VirtualServiceDataTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualServiceDataTypeDef
```


Required fields:
- `meshName`: `str`
- `metadata`: `"ResourceMetadataTypeDef"`
- `spec`: `"VirtualServiceSpecTypeDef"`
- `status`: `"VirtualServiceStatusTypeDef"`
- `virtualServiceName`: `str`




## VirtualServiceProviderTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualServiceProviderTypeDef
```




Optional fields:
- `virtualNode`: `"VirtualNodeServiceProviderTypeDef"`
- `virtualRouter`: `"VirtualRouterServiceProviderTypeDef"`


## VirtualServiceRefTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualServiceRefTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `meshName`: `str`
- `meshOwner`: `str`
- `resourceOwner`: `str`
- `version`: `int`
- `virtualServiceName`: `str`




## VirtualServiceSpecTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualServiceSpecTypeDef
```




Optional fields:
- `provider`: `"VirtualServiceProviderTypeDef"`


## VirtualServiceStatusTypeDef

```python
from mypy_boto3_appmesh.type_defs import VirtualServiceStatusTypeDef
```


Required fields:
- `status`: `VirtualServiceStatusCode`




## WeightedTargetTypeDef

```python
from mypy_boto3_appmesh.type_defs import WeightedTargetTypeDef
```


Required fields:
- `virtualNode`: `str`
- `weight`: `int`




## CreateGatewayRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateGatewayRouteOutputTypeDef
```


Required fields:
- `gatewayRoute`: `"GatewayRouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateMeshOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateMeshOutputTypeDef
```


Required fields:
- `mesh`: `"MeshDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateRouteOutputTypeDef
```


Required fields:
- `route`: `"RouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateVirtualGatewayOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateVirtualGatewayOutputTypeDef
```


Required fields:
- `virtualGateway`: `"VirtualGatewayDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateVirtualNodeOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateVirtualNodeOutputTypeDef
```


Required fields:
- `virtualNode`: `"VirtualNodeDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateVirtualRouterOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateVirtualRouterOutputTypeDef
```


Required fields:
- `virtualRouter`: `"VirtualRouterDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateVirtualServiceOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import CreateVirtualServiceOutputTypeDef
```


Required fields:
- `virtualService`: `"VirtualServiceDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteGatewayRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteGatewayRouteOutputTypeDef
```


Required fields:
- `gatewayRoute`: `"GatewayRouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteMeshOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteMeshOutputTypeDef
```


Required fields:
- `mesh`: `"MeshDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteRouteOutputTypeDef
```


Required fields:
- `route`: `"RouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteVirtualGatewayOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteVirtualGatewayOutputTypeDef
```


Required fields:
- `virtualGateway`: `"VirtualGatewayDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteVirtualNodeOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteVirtualNodeOutputTypeDef
```


Required fields:
- `virtualNode`: `"VirtualNodeDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteVirtualRouterOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteVirtualRouterOutputTypeDef
```


Required fields:
- `virtualRouter`: `"VirtualRouterDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteVirtualServiceOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DeleteVirtualServiceOutputTypeDef
```


Required fields:
- `virtualService`: `"VirtualServiceDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeGatewayRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeGatewayRouteOutputTypeDef
```


Required fields:
- `gatewayRoute`: `"GatewayRouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMeshOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeMeshOutputTypeDef
```


Required fields:
- `mesh`: `"MeshDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeRouteOutputTypeDef
```


Required fields:
- `route`: `"RouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVirtualGatewayOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeVirtualGatewayOutputTypeDef
```


Required fields:
- `virtualGateway`: `"VirtualGatewayDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVirtualNodeOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeVirtualNodeOutputTypeDef
```


Required fields:
- `virtualNode`: `"VirtualNodeDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVirtualRouterOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeVirtualRouterOutputTypeDef
```


Required fields:
- `virtualRouter`: `"VirtualRouterDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeVirtualServiceOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import DescribeVirtualServiceOutputTypeDef
```


Required fields:
- `virtualService`: `"VirtualServiceDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGatewayRoutesOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListGatewayRoutesOutputTypeDef
```


Required fields:
- `gatewayRoutes`: `List["GatewayRouteRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMeshesOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListMeshesOutputTypeDef
```


Required fields:
- `meshes`: `List["MeshRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRoutesOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListRoutesOutputTypeDef
```


Required fields:
- `routes`: `List["RouteRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListTagsForResourceOutputTypeDef
```


Required fields:
- `tags`: `List["TagRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVirtualGatewaysOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListVirtualGatewaysOutputTypeDef
```


Required fields:
- `virtualGateways`: `List["VirtualGatewayRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVirtualNodesOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListVirtualNodesOutputTypeDef
```


Required fields:
- `virtualNodes`: `List["VirtualNodeRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVirtualRoutersOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListVirtualRoutersOutputTypeDef
```


Required fields:
- `virtualRouters`: `List["VirtualRouterRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListVirtualServicesOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import ListVirtualServicesOutputTypeDef
```


Required fields:
- `virtualServices`: `List["VirtualServiceRefTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_appmesh.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateGatewayRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateGatewayRouteOutputTypeDef
```


Required fields:
- `gatewayRoute`: `"GatewayRouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateMeshOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateMeshOutputTypeDef
```


Required fields:
- `mesh`: `"MeshDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateRouteOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateRouteOutputTypeDef
```


Required fields:
- `route`: `"RouteDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateVirtualGatewayOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateVirtualGatewayOutputTypeDef
```


Required fields:
- `virtualGateway`: `"VirtualGatewayDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateVirtualNodeOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateVirtualNodeOutputTypeDef
```


Required fields:
- `virtualNode`: `"VirtualNodeDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateVirtualRouterOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateVirtualRouterOutputTypeDef
```


Required fields:
- `virtualRouter`: `"VirtualRouterDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateVirtualServiceOutputTypeDef

```python
from mypy_boto3_appmesh.type_defs import UpdateVirtualServiceOutputTypeDef
```


Required fields:
- `virtualService`: `"VirtualServiceDataTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`

