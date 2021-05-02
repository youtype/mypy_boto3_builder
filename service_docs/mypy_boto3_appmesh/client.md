# AppMeshClient for boto3 AppMesh module

> [Index](../index.md) > [AppMesh](./index.md) > AppMeshClient

Auto-generated documentation for [AppMesh](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh)
type annotations stubs module [mypy_boto3_appmesh](https://pypi.org/project/mypy-boto3-appmesh/).

- [AppMeshClient for boto3 AppMesh module](#appmeshclient-for-boto3-appmesh-module)
  - [AppMeshClient](#appmeshclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_gateway_route](#create_gateway_route)
    - [create_mesh](#create_mesh)
    - [create_route](#create_route)
    - [create_virtual_gateway](#create_virtual_gateway)
    - [create_virtual_node](#create_virtual_node)
    - [create_virtual_router](#create_virtual_router)
    - [create_virtual_service](#create_virtual_service)
    - [delete_gateway_route](#delete_gateway_route)
    - [delete_mesh](#delete_mesh)
    - [delete_route](#delete_route)
    - [delete_virtual_gateway](#delete_virtual_gateway)
    - [delete_virtual_node](#delete_virtual_node)
    - [delete_virtual_router](#delete_virtual_router)
    - [delete_virtual_service](#delete_virtual_service)
    - [describe_gateway_route](#describe_gateway_route)
    - [describe_mesh](#describe_mesh)
    - [describe_route](#describe_route)
    - [describe_virtual_gateway](#describe_virtual_gateway)
    - [describe_virtual_node](#describe_virtual_node)
    - [describe_virtual_router](#describe_virtual_router)
    - [describe_virtual_service](#describe_virtual_service)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_gateway_routes](#list_gateway_routes)
    - [list_meshes](#list_meshes)
    - [list_routes](#list_routes)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_virtual_gateways](#list_virtual_gateways)
    - [list_virtual_nodes](#list_virtual_nodes)
    - [list_virtual_routers](#list_virtual_routers)
    - [list_virtual_services](#list_virtual_services)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_gateway_route](#update_gateway_route)
    - [update_mesh](#update_mesh)
    - [update_route](#update_route)
    - [update_virtual_gateway](#update_virtual_gateway)
    - [update_virtual_node](#update_virtual_node)
    - [update_virtual_router](#update_virtual_router)
    - [update_virtual_service](#update_virtual_service)
    - [get_paginator](#get_paginator)

## AppMeshClient

Type annotations for `boto3.client("appmesh")`

Can be used directly:

```python
from mypy_boto3_appmesh.client import AppMeshClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_appmesh.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.TooManyTagsException`


## Methods


### can_paginate

Type annotations for `boto3.client("appmesh").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_gateway_route

Type annotations for `boto3.client("appmesh").create_gateway_route` method.

[Client.create_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_gateway_route)

```python
def create_gateway_route(
    self,
    gatewayRouteName: str,
    meshName: str,
    spec: "GatewayRouteSpecTypeDef",
    virtualGatewayName: str,
    clientToken: str = None,
    meshOwner: str = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateGatewayRouteOutputTypeDef:
    pass
```

### create_mesh

Type annotations for `boto3.client("appmesh").create_mesh` method.

[Client.create_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_mesh)

```python
def create_mesh(
    self,
    meshName: str,
    clientToken: str = None,
    spec: "MeshSpecTypeDef" = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateMeshOutputTypeDef:
    pass
```

### create_route

Type annotations for `boto3.client("appmesh").create_route` method.

[Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_route)

```python
def create_route(
    self,
    meshName: str,
    routeName: str,
    spec: "RouteSpecTypeDef",
    virtualRouterName: str,
    clientToken: str = None,
    meshOwner: str = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateRouteOutputTypeDef:
    pass
```

### create_virtual_gateway

Type annotations for `boto3.client("appmesh").create_virtual_gateway` method.

[Client.create_virtual_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_virtual_gateway)

```python
def create_virtual_gateway(
    self,
    meshName: str,
    spec: "VirtualGatewaySpecTypeDef",
    virtualGatewayName: str,
    clientToken: str = None,
    meshOwner: str = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateVirtualGatewayOutputTypeDef:
    pass
```

### create_virtual_node

Type annotations for `boto3.client("appmesh").create_virtual_node` method.

[Client.create_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_virtual_node)

```python
def create_virtual_node(
    self,
    meshName: str,
    spec: "VirtualNodeSpecTypeDef",
    virtualNodeName: str,
    clientToken: str = None,
    meshOwner: str = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateVirtualNodeOutputTypeDef:
    pass
```

### create_virtual_router

Type annotations for `boto3.client("appmesh").create_virtual_router` method.

[Client.create_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_virtual_router)

```python
def create_virtual_router(
    self,
    meshName: str,
    spec: "VirtualRouterSpecTypeDef",
    virtualRouterName: str,
    clientToken: str = None,
    meshOwner: str = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateVirtualRouterOutputTypeDef:
    pass
```

### create_virtual_service

Type annotations for `boto3.client("appmesh").create_virtual_service` method.

[Client.create_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.create_virtual_service)

```python
def create_virtual_service(
    self,
    meshName: str,
    spec: "VirtualServiceSpecTypeDef",
    virtualServiceName: str,
    clientToken: str = None,
    meshOwner: str = None,
    tags: List["TagRefTypeDef"] = None
) -> CreateVirtualServiceOutputTypeDef:
    pass
```

### delete_gateway_route

Type annotations for `boto3.client("appmesh").delete_gateway_route` method.

[Client.delete_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_gateway_route)

```python
def delete_gateway_route(
    self,
    gatewayRouteName: str,
    meshName: str,
    virtualGatewayName: str,
    meshOwner: str = None
) -> DeleteGatewayRouteOutputTypeDef:
    pass
```

### delete_mesh

Type annotations for `boto3.client("appmesh").delete_mesh` method.

[Client.delete_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_mesh)

```python
def delete_mesh(
    self,
    meshName: str
) -> DeleteMeshOutputTypeDef:
    pass
```

### delete_route

Type annotations for `boto3.client("appmesh").delete_route` method.

[Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_route)

```python
def delete_route(
    self,
    meshName: str,
    routeName: str,
    virtualRouterName: str,
    meshOwner: str = None
) -> DeleteRouteOutputTypeDef:
    pass
```

### delete_virtual_gateway

Type annotations for `boto3.client("appmesh").delete_virtual_gateway` method.

[Client.delete_virtual_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_virtual_gateway)

```python
def delete_virtual_gateway(
    self,
    meshName: str,
    virtualGatewayName: str,
    meshOwner: str = None
) -> DeleteVirtualGatewayOutputTypeDef:
    pass
```

### delete_virtual_node

Type annotations for `boto3.client("appmesh").delete_virtual_node` method.

[Client.delete_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_virtual_node)

```python
def delete_virtual_node(
    self,
    meshName: str,
    virtualNodeName: str,
    meshOwner: str = None
) -> DeleteVirtualNodeOutputTypeDef:
    pass
```

### delete_virtual_router

Type annotations for `boto3.client("appmesh").delete_virtual_router` method.

[Client.delete_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_virtual_router)

```python
def delete_virtual_router(
    self,
    meshName: str,
    virtualRouterName: str,
    meshOwner: str = None
) -> DeleteVirtualRouterOutputTypeDef:
    pass
```

### delete_virtual_service

Type annotations for `boto3.client("appmesh").delete_virtual_service` method.

[Client.delete_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.delete_virtual_service)

```python
def delete_virtual_service(
    self,
    meshName: str,
    virtualServiceName: str,
    meshOwner: str = None
) -> DeleteVirtualServiceOutputTypeDef:
    pass
```

### describe_gateway_route

Type annotations for `boto3.client("appmesh").describe_gateway_route` method.

[Client.describe_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_gateway_route)

```python
def describe_gateway_route(
    self,
    gatewayRouteName: str,
    meshName: str,
    virtualGatewayName: str,
    meshOwner: str = None
) -> DescribeGatewayRouteOutputTypeDef:
    pass
```

### describe_mesh

Type annotations for `boto3.client("appmesh").describe_mesh` method.

[Client.describe_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_mesh)

```python
def describe_mesh(
    self,
    meshName: str,
    meshOwner: str = None
) -> DescribeMeshOutputTypeDef:
    pass
```

### describe_route

Type annotations for `boto3.client("appmesh").describe_route` method.

[Client.describe_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_route)

```python
def describe_route(
    self,
    meshName: str,
    routeName: str,
    virtualRouterName: str,
    meshOwner: str = None
) -> DescribeRouteOutputTypeDef:
    pass
```

### describe_virtual_gateway

Type annotations for `boto3.client("appmesh").describe_virtual_gateway` method.

[Client.describe_virtual_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_virtual_gateway)

```python
def describe_virtual_gateway(
    self,
    meshName: str,
    virtualGatewayName: str,
    meshOwner: str = None
) -> DescribeVirtualGatewayOutputTypeDef:
    pass
```

### describe_virtual_node

Type annotations for `boto3.client("appmesh").describe_virtual_node` method.

[Client.describe_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_virtual_node)

```python
def describe_virtual_node(
    self,
    meshName: str,
    virtualNodeName: str,
    meshOwner: str = None
) -> DescribeVirtualNodeOutputTypeDef:
    pass
```

### describe_virtual_router

Type annotations for `boto3.client("appmesh").describe_virtual_router` method.

[Client.describe_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_virtual_router)

```python
def describe_virtual_router(
    self,
    meshName: str,
    virtualRouterName: str,
    meshOwner: str = None
) -> DescribeVirtualRouterOutputTypeDef:
    pass
```

### describe_virtual_service

Type annotations for `boto3.client("appmesh").describe_virtual_service` method.

[Client.describe_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.describe_virtual_service)

```python
def describe_virtual_service(
    self,
    meshName: str,
    virtualServiceName: str,
    meshOwner: str = None
) -> DescribeVirtualServiceOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("appmesh").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.generate_presigned_url)

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

### list_gateway_routes

Type annotations for `boto3.client("appmesh").list_gateway_routes` method.

[Client.list_gateway_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_gateway_routes)

```python
def list_gateway_routes(
    self,
    meshName: str,
    virtualGatewayName: str,
    limit: int = None,
    meshOwner: str = None,
    nextToken: str = None
) -> ListGatewayRoutesOutputTypeDef:
    pass
```

### list_meshes

Type annotations for `boto3.client("appmesh").list_meshes` method.

[Client.list_meshes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_meshes)

```python
def list_meshes(
    self,
    limit: int = None,
    nextToken: str = None
) -> ListMeshesOutputTypeDef:
    pass
```

### list_routes

Type annotations for `boto3.client("appmesh").list_routes` method.

[Client.list_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_routes)

```python
def list_routes(
    self,
    meshName: str,
    virtualRouterName: str,
    limit: int = None,
    meshOwner: str = None,
    nextToken: str = None
) -> ListRoutesOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("appmesh").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str,
    limit: int = None,
    nextToken: str = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_virtual_gateways

Type annotations for `boto3.client("appmesh").list_virtual_gateways` method.

[Client.list_virtual_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_virtual_gateways)

```python
def list_virtual_gateways(
    self,
    meshName: str,
    limit: int = None,
    meshOwner: str = None,
    nextToken: str = None
) -> ListVirtualGatewaysOutputTypeDef:
    pass
```

### list_virtual_nodes

Type annotations for `boto3.client("appmesh").list_virtual_nodes` method.

[Client.list_virtual_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_virtual_nodes)

```python
def list_virtual_nodes(
    self,
    meshName: str,
    limit: int = None,
    meshOwner: str = None,
    nextToken: str = None
) -> ListVirtualNodesOutputTypeDef:
    pass
```

### list_virtual_routers

Type annotations for `boto3.client("appmesh").list_virtual_routers` method.

[Client.list_virtual_routers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_virtual_routers)

```python
def list_virtual_routers(
    self,
    meshName: str,
    limit: int = None,
    meshOwner: str = None,
    nextToken: str = None
) -> ListVirtualRoutersOutputTypeDef:
    pass
```

### list_virtual_services

Type annotations for `boto3.client("appmesh").list_virtual_services` method.

[Client.list_virtual_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.list_virtual_services)

```python
def list_virtual_services(
    self,
    meshName: str,
    limit: int = None,
    meshOwner: str = None,
    nextToken: str = None
) -> ListVirtualServicesOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("appmesh").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagRefTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("appmesh").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_gateway_route

Type annotations for `boto3.client("appmesh").update_gateway_route` method.

[Client.update_gateway_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_gateway_route)

```python
def update_gateway_route(
    self,
    gatewayRouteName: str,
    meshName: str,
    spec: "GatewayRouteSpecTypeDef",
    virtualGatewayName: str,
    clientToken: str = None,
    meshOwner: str = None
) -> UpdateGatewayRouteOutputTypeDef:
    pass
```

### update_mesh

Type annotations for `boto3.client("appmesh").update_mesh` method.

[Client.update_mesh documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_mesh)

```python
def update_mesh(
    self,
    meshName: str,
    clientToken: str = None,
    spec: "MeshSpecTypeDef" = None
) -> UpdateMeshOutputTypeDef:
    pass
```

### update_route

Type annotations for `boto3.client("appmesh").update_route` method.

[Client.update_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_route)

```python
def update_route(
    self,
    meshName: str,
    routeName: str,
    spec: "RouteSpecTypeDef",
    virtualRouterName: str,
    clientToken: str = None,
    meshOwner: str = None
) -> UpdateRouteOutputTypeDef:
    pass
```

### update_virtual_gateway

Type annotations for `boto3.client("appmesh").update_virtual_gateway` method.

[Client.update_virtual_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_virtual_gateway)

```python
def update_virtual_gateway(
    self,
    meshName: str,
    spec: "VirtualGatewaySpecTypeDef",
    virtualGatewayName: str,
    clientToken: str = None,
    meshOwner: str = None
) -> UpdateVirtualGatewayOutputTypeDef:
    pass
```

### update_virtual_node

Type annotations for `boto3.client("appmesh").update_virtual_node` method.

[Client.update_virtual_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_virtual_node)

```python
def update_virtual_node(
    self,
    meshName: str,
    spec: "VirtualNodeSpecTypeDef",
    virtualNodeName: str,
    clientToken: str = None,
    meshOwner: str = None
) -> UpdateVirtualNodeOutputTypeDef:
    pass
```

### update_virtual_router

Type annotations for `boto3.client("appmesh").update_virtual_router` method.

[Client.update_virtual_router documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_virtual_router)

```python
def update_virtual_router(
    self,
    meshName: str,
    spec: "VirtualRouterSpecTypeDef",
    virtualRouterName: str,
    clientToken: str = None,
    meshOwner: str = None
) -> UpdateVirtualRouterOutputTypeDef:
    pass
```

### update_virtual_service

Type annotations for `boto3.client("appmesh").update_virtual_service` method.

[Client.update_virtual_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Client.update_virtual_service)

```python
def update_virtual_service(
    self,
    meshName: str,
    spec: "VirtualServiceSpecTypeDef",
    virtualServiceName: str,
    clientToken: str = None,
    meshOwner: str = None
) -> UpdateVirtualServiceOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("appmesh").get_paginator` method with overloads.

- `client.get_paginator("list_gateway_routes")` -> [ListGatewayRoutesPaginator](./paginators.md#listgatewayroutespaginator)
- `client.get_paginator("list_meshes")` -> [ListMeshesPaginator](./paginators.md#listmeshespaginator)
- `client.get_paginator("list_routes")` -> [ListRoutesPaginator](./paginators.md#listroutespaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- `client.get_paginator("list_virtual_gateways")` -> [ListVirtualGatewaysPaginator](./paginators.md#listvirtualgatewayspaginator)
- `client.get_paginator("list_virtual_nodes")` -> [ListVirtualNodesPaginator](./paginators.md#listvirtualnodespaginator)
- `client.get_paginator("list_virtual_routers")` -> [ListVirtualRoutersPaginator](./paginators.md#listvirtualrouterspaginator)
- `client.get_paginator("list_virtual_services")` -> [ListVirtualServicesPaginator](./paginators.md#listvirtualservicespaginator)


