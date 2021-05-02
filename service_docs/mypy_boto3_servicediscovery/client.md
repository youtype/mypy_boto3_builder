# ServiceDiscoveryClient for boto3 ServiceDiscovery module

> [Index](../index.md) > [ServiceDiscovery](./index.md) > ServiceDiscoveryClient

Auto-generated documentation for [ServiceDiscovery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery)
type annotations stubs module [mypy_boto3_servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/).

- [ServiceDiscoveryClient for boto3 ServiceDiscovery module](#servicediscoveryclient-for-boto3-servicediscovery-module)
  - [ServiceDiscoveryClient](#servicediscoveryclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_http_namespace](#create_http_namespace)
    - [create_private_dns_namespace](#create_private_dns_namespace)
    - [create_public_dns_namespace](#create_public_dns_namespace)
    - [create_service](#create_service)
    - [delete_namespace](#delete_namespace)
    - [delete_service](#delete_service)
    - [deregister_instance](#deregister_instance)
    - [discover_instances](#discover_instances)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_instance](#get_instance)
    - [get_instances_health_status](#get_instances_health_status)
    - [get_namespace](#get_namespace)
    - [get_operation](#get_operation)
    - [get_service](#get_service)
    - [list_instances](#list_instances)
    - [list_namespaces](#list_namespaces)
    - [list_operations](#list_operations)
    - [list_services](#list_services)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [register_instance](#register_instance)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_instance_custom_health_status](#update_instance_custom_health_status)
    - [update_service](#update_service)
    - [get_paginator](#get_paginator)

## ServiceDiscoveryClient

Type annotations for `boto3.client("servicediscovery")`

Can be used directly:

```python
from mypy_boto3_servicediscovery.client import ServiceDiscoveryClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_servicediscovery.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CustomHealthNotFound`
- `Exceptions.DuplicateRequest`
- `Exceptions.InstanceNotFound`
- `Exceptions.InvalidInput`
- `Exceptions.NamespaceAlreadyExists`
- `Exceptions.NamespaceNotFound`
- `Exceptions.OperationNotFound`
- `Exceptions.RequestLimitExceeded`
- `Exceptions.ResourceInUse`
- `Exceptions.ResourceLimitExceeded`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceAlreadyExists`
- `Exceptions.ServiceNotFound`
- `Exceptions.TooManyTagsException`


## Methods


### can_paginate

Type annotations for `boto3.client("servicediscovery").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_http_namespace

Type annotations for `boto3.client("servicediscovery").create_http_namespace` method.

[Client.create_http_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_http_namespace)

```python
def create_http_namespace(
    self,
    Name: str,
    CreatorRequestId: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateHttpNamespaceResponseTypeDef:
    pass
```

### create_private_dns_namespace

Type annotations for `boto3.client("servicediscovery").create_private_dns_namespace` method.

[Client.create_private_dns_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_private_dns_namespace)

```python
def create_private_dns_namespace(
    self,
    Name: str,
    Vpc: str,
    CreatorRequestId: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePrivateDnsNamespaceResponseTypeDef:
    pass
```

### create_public_dns_namespace

Type annotations for `boto3.client("servicediscovery").create_public_dns_namespace` method.

[Client.create_public_dns_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_public_dns_namespace)

```python
def create_public_dns_namespace(
    self,
    Name: str,
    CreatorRequestId: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePublicDnsNamespaceResponseTypeDef:
    pass
```

### create_service

Type annotations for `boto3.client("servicediscovery").create_service` method.

[Client.create_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_service)

```python
def create_service(
    self,
    Name: str,
    NamespaceId: str = None,
    CreatorRequestId: str = None,
    Description: str = None,
    DnsConfig: "DnsConfigTypeDef" = None,
    HealthCheckConfig: "HealthCheckConfigTypeDef" = None,
    HealthCheckCustomConfig: "HealthCheckCustomConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    Type: Literal['HTTP'] = None
) -> CreateServiceResponseTypeDef:
    pass
```

### delete_namespace

Type annotations for `boto3.client("servicediscovery").delete_namespace` method.

[Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_namespace)

```python
def delete_namespace(
    self,
    Id: str
) -> DeleteNamespaceResponseTypeDef:
    pass
```

### delete_service

Type annotations for `boto3.client("servicediscovery").delete_service` method.

[Client.delete_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_service)

```python
def delete_service(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### deregister_instance

Type annotations for `boto3.client("servicediscovery").deregister_instance` method.

[Client.deregister_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.deregister_instance)

```python
def deregister_instance(
    self,
    ServiceId: str,
    InstanceId: str
) -> DeregisterInstanceResponseTypeDef:
    pass
```

### discover_instances

Type annotations for `boto3.client("servicediscovery").discover_instances` method.

[Client.discover_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.discover_instances)

```python
def discover_instances(
    self,
    NamespaceName: str,
    ServiceName: str,
    MaxResults: int = None,
    QueryParameters: Dict[str, str] = None,
    OptionalParameters: Dict[str, str] = None,
    HealthStatus: HealthStatusFilter = None
) -> DiscoverInstancesResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("servicediscovery").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.generate_presigned_url)

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

### get_instance

Type annotations for `boto3.client("servicediscovery").get_instance` method.

[Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instance)

```python
def get_instance(
    self,
    ServiceId: str,
    InstanceId: str
) -> GetInstanceResponseTypeDef:
    pass
```

### get_instances_health_status

Type annotations for `boto3.client("servicediscovery").get_instances_health_status` method.

[Client.get_instances_health_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instances_health_status)

```python
def get_instances_health_status(
    self,
    ServiceId: str,
    Instances: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetInstancesHealthStatusResponseTypeDef:
    pass
```

### get_namespace

Type annotations for `boto3.client("servicediscovery").get_namespace` method.

[Client.get_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_namespace)

```python
def get_namespace(
    self,
    Id: str
) -> GetNamespaceResponseTypeDef:
    pass
```

### get_operation

Type annotations for `boto3.client("servicediscovery").get_operation` method.

[Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_operation)

```python
def get_operation(
    self,
    OperationId: str
) -> GetOperationResponseTypeDef:
    pass
```

### get_service

Type annotations for `boto3.client("servicediscovery").get_service` method.

[Client.get_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_service)

```python
def get_service(
    self,
    Id: str
) -> GetServiceResponseTypeDef:
    pass
```

### list_instances

Type annotations for `boto3.client("servicediscovery").list_instances` method.

[Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_instances)

```python
def list_instances(
    self,
    ServiceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListInstancesResponseTypeDef:
    pass
```

### list_namespaces

Type annotations for `boto3.client("servicediscovery").list_namespaces` method.

[Client.list_namespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_namespaces)

```python
def list_namespaces(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[NamespaceFilterTypeDef] = None
) -> ListNamespacesResponseTypeDef:
    pass
```

### list_operations

Type annotations for `boto3.client("servicediscovery").list_operations` method.

[Client.list_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_operations)

```python
def list_operations(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[OperationFilterTypeDef] = None
) -> ListOperationsResponseTypeDef:
    pass
```

### list_services

Type annotations for `boto3.client("servicediscovery").list_services` method.

[Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_services)

```python
def list_services(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[ServiceFilterTypeDef] = None
) -> ListServicesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("servicediscovery").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### register_instance

Type annotations for `boto3.client("servicediscovery").register_instance` method.

[Client.register_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.register_instance)

```python
def register_instance(
    self,
    ServiceId: str,
    InstanceId: str,
    Attributes: Dict[str, str],
    CreatorRequestId: str = None
) -> RegisterInstanceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("servicediscovery").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("servicediscovery").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_instance_custom_health_status

Type annotations for `boto3.client("servicediscovery").update_instance_custom_health_status` method.

[Client.update_instance_custom_health_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_instance_custom_health_status)

```python
def update_instance_custom_health_status(
    self,
    ServiceId: str,
    InstanceId: str,
    Status: CustomHealthStatus
) -> None:
    pass
```

### update_service

Type annotations for `boto3.client("servicediscovery").update_service` method.

[Client.update_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_service)

```python
def update_service(
    self,
    Id: str,
    Service: ServiceChangeTypeDef
) -> UpdateServiceResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("servicediscovery").get_paginator` method with overloads.

- `client.get_paginator("list_instances")` -> [ListInstancesPaginator](./paginators.md#listinstancespaginator)
- `client.get_paginator("list_namespaces")` -> [ListNamespacesPaginator](./paginators.md#listnamespacespaginator)
- `client.get_paginator("list_operations")` -> [ListOperationsPaginator](./paginators.md#listoperationspaginator)
- `client.get_paginator("list_services")` -> [ListServicesPaginator](./paginators.md#listservicespaginator)


