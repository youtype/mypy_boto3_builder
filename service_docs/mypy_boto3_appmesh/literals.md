# Literals for boto3 AppMesh module

> [Index](../index.md) > [AppMesh](./index.md) > Literals

Auto-generated documentation for [AppMesh](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh)
type annotations stubs module [mypy_boto3_appmesh](https://pypi.org/project/mypy-boto3-appmesh/).

- [Literals for boto3 AppMesh module](#literals-for-boto3-appmesh-module)
  - [DurationUnit](#durationunit)
  - [EgressFilterType](#egressfiltertype)
  - [GatewayRouteStatusCode](#gatewayroutestatuscode)
  - [GrpcRetryPolicyEvent](#grpcretrypolicyevent)
  - [HttpMethod](#httpmethod)
  - [HttpScheme](#httpscheme)
  - [ListGatewayRoutesPaginatorName](#listgatewayroutespaginatorname)
  - [ListMeshesPaginatorName](#listmeshespaginatorname)
  - [ListRoutesPaginatorName](#listroutespaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListVirtualGatewaysPaginatorName](#listvirtualgatewayspaginatorname)
  - [ListVirtualNodesPaginatorName](#listvirtualnodespaginatorname)
  - [ListVirtualRoutersPaginatorName](#listvirtualrouterspaginatorname)
  - [ListVirtualServicesPaginatorName](#listvirtualservicespaginatorname)
  - [ListenerTlsMode](#listenertlsmode)
  - [MeshStatusCode](#meshstatuscode)
  - [PortProtocol](#portprotocol)
  - [RouteStatusCode](#routestatuscode)
  - [TcpRetryPolicyEvent](#tcpretrypolicyevent)
  - [VirtualGatewayListenerTlsMode](#virtualgatewaylistenertlsmode)
  - [VirtualGatewayPortProtocol](#virtualgatewayportprotocol)
  - [VirtualGatewayStatusCode](#virtualgatewaystatuscode)
  - [VirtualNodeStatusCode](#virtualnodestatuscode)
  - [VirtualRouterStatusCode](#virtualrouterstatuscode)
  - [VirtualServiceStatusCode](#virtualservicestatuscode)

## DurationUnit

```python
from mypy_boto3_appmesh.literals import DurationUnit
```

Values:

- `ms`
- `s`

## EgressFilterType

```python
from mypy_boto3_appmesh.literals import EgressFilterType
```

Values:

- `ALLOW_ALL`
- `DROP_ALL`

## GatewayRouteStatusCode

```python
from mypy_boto3_appmesh.literals import GatewayRouteStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## GrpcRetryPolicyEvent

```python
from mypy_boto3_appmesh.literals import GrpcRetryPolicyEvent
```

Values:

- `cancelled`
- `deadline-exceeded`
- `internal`
- `resource-exhausted`
- `unavailable`

## HttpMethod

```python
from mypy_boto3_appmesh.literals import HttpMethod
```

Values:

- `CONNECT`
- `DELETE`
- `GET`
- `HEAD`
- `OPTIONS`
- `PATCH`
- `POST`
- `PUT`
- `TRACE`

## HttpScheme

```python
from mypy_boto3_appmesh.literals import HttpScheme
```

Values:

- `http`
- `https`

## ListGatewayRoutesPaginatorName

```python
from mypy_boto3_appmesh.literals import ListGatewayRoutesPaginatorName
```

Values:

- `list_gateway_routes`

## ListMeshesPaginatorName

```python
from mypy_boto3_appmesh.literals import ListMeshesPaginatorName
```

Values:

- `list_meshes`

## ListRoutesPaginatorName

```python
from mypy_boto3_appmesh.literals import ListRoutesPaginatorName
```

Values:

- `list_routes`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_appmesh.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListVirtualGatewaysPaginatorName

```python
from mypy_boto3_appmesh.literals import ListVirtualGatewaysPaginatorName
```

Values:

- `list_virtual_gateways`

## ListVirtualNodesPaginatorName

```python
from mypy_boto3_appmesh.literals import ListVirtualNodesPaginatorName
```

Values:

- `list_virtual_nodes`

## ListVirtualRoutersPaginatorName

```python
from mypy_boto3_appmesh.literals import ListVirtualRoutersPaginatorName
```

Values:

- `list_virtual_routers`

## ListVirtualServicesPaginatorName

```python
from mypy_boto3_appmesh.literals import ListVirtualServicesPaginatorName
```

Values:

- `list_virtual_services`

## ListenerTlsMode

```python
from mypy_boto3_appmesh.literals import ListenerTlsMode
```

Values:

- `DISABLED`
- `PERMISSIVE`
- `STRICT`

## MeshStatusCode

```python
from mypy_boto3_appmesh.literals import MeshStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## PortProtocol

```python
from mypy_boto3_appmesh.literals import PortProtocol
```

Values:

- `grpc`
- `http`
- `http2`
- `tcp`

## RouteStatusCode

```python
from mypy_boto3_appmesh.literals import RouteStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## TcpRetryPolicyEvent

```python
from mypy_boto3_appmesh.literals import TcpRetryPolicyEvent
```

Values:

- `connection-error`

## VirtualGatewayListenerTlsMode

```python
from mypy_boto3_appmesh.literals import VirtualGatewayListenerTlsMode
```

Values:

- `DISABLED`
- `PERMISSIVE`
- `STRICT`

## VirtualGatewayPortProtocol

```python
from mypy_boto3_appmesh.literals import VirtualGatewayPortProtocol
```

Values:

- `grpc`
- `http`
- `http2`

## VirtualGatewayStatusCode

```python
from mypy_boto3_appmesh.literals import VirtualGatewayStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## VirtualNodeStatusCode

```python
from mypy_boto3_appmesh.literals import VirtualNodeStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## VirtualRouterStatusCode

```python
from mypy_boto3_appmesh.literals import VirtualRouterStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## VirtualServiceStatusCode

```python
from mypy_boto3_appmesh.literals import VirtualServiceStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `INACTIVE`
