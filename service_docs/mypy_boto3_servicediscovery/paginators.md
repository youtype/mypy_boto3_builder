# Paginators for boto3 ServiceDiscovery module

> [Index](../index.md) > [ServiceDiscovery](./index.md) > Paginators

Auto-generated documentation for [ServiceDiscovery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery)
type annotations stubs module [mypy_boto3_servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/).

- [Paginators for boto3 ServiceDiscovery module](#paginators-for-boto3-servicediscovery-module)
  - [ListInstancesPaginator](#listinstancespaginator)
  - [ListNamespacesPaginator](#listnamespacespaginator)
  - [ListOperationsPaginator](#listoperationspaginator)
  - [ListServicesPaginator](#listservicespaginator)

## ListInstancesPaginator

Type annotations for `boto3.client("servicediscovery").get_paginator("list_instances")`.

Can be used directly:

```python
from mypy_boto3_servicediscovery.paginators import ListInstancesPaginator

def get_list_instances_paginator() -> ListInstancesPaginator:
    return boto3.client("servicediscovery").get_paginator("list_instances")
```

[Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)

```python
class ListInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        pass
```
## ListNamespacesPaginator

Type annotations for `boto3.client("servicediscovery").get_paginator("list_namespaces")`.

Can be used directly:

```python
from mypy_boto3_servicediscovery.paginators import ListNamespacesPaginator

def get_list_namespaces_paginator() -> ListNamespacesPaginator:
    return boto3.client("servicediscovery").get_paginator("list_namespaces")
```

[Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)

```python
class ListNamespacesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[NamespaceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        pass
```
## ListOperationsPaginator

Type annotations for `boto3.client("servicediscovery").get_paginator("list_operations")`.

Can be used directly:

```python
from mypy_boto3_servicediscovery.paginators import ListOperationsPaginator

def get_list_operations_paginator() -> ListOperationsPaginator:
    return boto3.client("servicediscovery").get_paginator("list_operations")
```

[Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)

```python
class ListOperationsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[OperationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOperationsResponseTypeDef]:
        pass
```
## ListServicesPaginator

Type annotations for `boto3.client("servicediscovery").get_paginator("list_services")`.

Can be used directly:

```python
from mypy_boto3_servicediscovery.paginators import ListServicesPaginator

def get_list_services_paginator() -> ListServicesPaginator:
    return boto3.client("servicediscovery").get_paginator("list_services")
```

[Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)

```python
class ListServicesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ServiceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        pass
```