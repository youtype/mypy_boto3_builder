# Paginators for boto3 AppMesh module

> [Index](../index.md) > [AppMesh](./index.md) > Paginators

Auto-generated documentation for [AppMesh](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh)
type annotations stubs module [mypy_boto3_appmesh](https://pypi.org/project/mypy-boto3-appmesh/).

- [Paginators for boto3 AppMesh module](#paginators-for-boto3-appmesh-module)
  - [ListGatewayRoutesPaginator](#listgatewayroutespaginator)
  - [ListMeshesPaginator](#listmeshespaginator)
  - [ListRoutesPaginator](#listroutespaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [ListVirtualGatewaysPaginator](#listvirtualgatewayspaginator)
  - [ListVirtualNodesPaginator](#listvirtualnodespaginator)
  - [ListVirtualRoutersPaginator](#listvirtualrouterspaginator)
  - [ListVirtualServicesPaginator](#listvirtualservicespaginator)

## ListGatewayRoutesPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_gateway_routes")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListGatewayRoutesPaginator

def get_list_gateway_routes_paginator() -> ListGatewayRoutesPaginator:
    return boto3.client("appmesh").get_paginator("list_gateway_routes")
```

[Paginator.ListGatewayRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListGatewayRoutes)

```python
class ListGatewayRoutesPaginator(Boto3Paginator):
    def paginate(
        self,
        meshName: str,
        virtualGatewayName: str,
        meshOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGatewayRoutesOutputTypeDef]:
        pass
```
## ListMeshesPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_meshes")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListMeshesPaginator

def get_list_meshes_paginator() -> ListMeshesPaginator:
    return boto3.client("appmesh").get_paginator("list_meshes")
```

[Paginator.ListMeshes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListMeshes)

```python
class ListMeshesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMeshesOutputTypeDef]:
        pass
```
## ListRoutesPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_routes")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListRoutesPaginator

def get_list_routes_paginator() -> ListRoutesPaginator:
    return boto3.client("appmesh").get_paginator("list_routes")
```

[Paginator.ListRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListRoutes)

```python
class ListRoutesPaginator(Boto3Paginator):
    def paginate(
        self,
        meshName: str,
        virtualRouterName: str,
        meshOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutesOutputTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("appmesh").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        pass
```
## ListVirtualGatewaysPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_virtual_gateways")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListVirtualGatewaysPaginator

def get_list_virtual_gateways_paginator() -> ListVirtualGatewaysPaginator:
    return boto3.client("appmesh").get_paginator("list_virtual_gateways")
```

[Paginator.ListVirtualGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualGateways)

```python
class ListVirtualGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        meshName: str,
        meshOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualGatewaysOutputTypeDef]:
        pass
```
## ListVirtualNodesPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_virtual_nodes")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListVirtualNodesPaginator

def get_list_virtual_nodes_paginator() -> ListVirtualNodesPaginator:
    return boto3.client("appmesh").get_paginator("list_virtual_nodes")
```

[Paginator.ListVirtualNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualNodes)

```python
class ListVirtualNodesPaginator(Boto3Paginator):
    def paginate(
        self,
        meshName: str,
        meshOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualNodesOutputTypeDef]:
        pass
```
## ListVirtualRoutersPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_virtual_routers")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListVirtualRoutersPaginator

def get_list_virtual_routers_paginator() -> ListVirtualRoutersPaginator:
    return boto3.client("appmesh").get_paginator("list_virtual_routers")
```

[Paginator.ListVirtualRouters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualRouters)

```python
class ListVirtualRoutersPaginator(Boto3Paginator):
    def paginate(
        self,
        meshName: str,
        meshOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualRoutersOutputTypeDef]:
        pass
```
## ListVirtualServicesPaginator

Type annotations for `boto3.client("appmesh").get_paginator("list_virtual_services")`.

Can be used directly:

```python
from mypy_boto3_appmesh.paginators import ListVirtualServicesPaginator

def get_list_virtual_services_paginator() -> ListVirtualServicesPaginator:
    return boto3.client("appmesh").get_paginator("list_virtual_services")
```

[Paginator.ListVirtualServices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html#AppMesh.Paginator.ListVirtualServices)

```python
class ListVirtualServicesPaginator(Boto3Paginator):
    def paginate(
        self,
        meshName: str,
        meshOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualServicesOutputTypeDef]:
        pass
```