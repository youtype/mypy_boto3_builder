# Type annotations for boto3 ServiceDiscovery module

> [Index](../index.md) > ServiceDiscovery

Auto-generated documentation for [ServiceDiscovery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery)
type annotations stubs module [mypy_boto3_servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/).

```bash
pip install mypy-boto3-servicediscovery
```

- [Type annotations for boto3 ServiceDiscovery module](#type-annotations-for-boto3-servicediscovery-module)
  - [ServiceDiscoveryClient](#servicediscoveryclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ServiceDiscoveryClient

Type annotations for  `boto3.client("servicediscovery")` as [ServiceDiscoveryClient](./client.md)

Can be used directly:

```python
from mypy_boto3_servicediscovery.client import ServiceDiscoveryClient
```


ServiceDiscoveryClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_http_namespace](./client.md#create-http-namespace)
- [create_private_dns_namespace](./client.md#create-private-dns-namespace)
- [create_public_dns_namespace](./client.md#create-public-dns-namespace)
- [create_service](./client.md#create-service)
- [delete_namespace](./client.md#delete-namespace)
- [delete_service](./client.md#delete-service)
- [deregister_instance](./client.md#deregister-instance)
- [discover_instances](./client.md#discover-instances)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_instance](./client.md#get-instance)
- [get_instances_health_status](./client.md#get-instances-health-status)
- [get_namespace](./client.md#get-namespace)
- [get_operation](./client.md#get-operation)
- [get_paginator](./client.md#get-paginator)
- [get_service](./client.md#get-service)
- [list_instances](./client.md#list-instances)
- [list_namespaces](./client.md#list-namespaces)
- [list_operations](./client.md#list-operations)
- [list_services](./client.md#list-services)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [register_instance](./client.md#register-instance)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_instance_custom_health_status](./client.md#update-instance-custom-health-status)
- [update_service](./client.md#update-service)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CustomHealthNotFound](./client.md#customhealthnotfound)
- [DuplicateRequest](./client.md#duplicaterequest)
- [InstanceNotFound](./client.md#instancenotfound)
- [InvalidInput](./client.md#invalidinput)
- [NamespaceAlreadyExists](./client.md#namespacealreadyexists)
- [NamespaceNotFound](./client.md#namespacenotfound)
- [OperationNotFound](./client.md#operationnotfound)
- [RequestLimitExceeded](./client.md#requestlimitexceeded)
- [ResourceInUse](./client.md#resourceinuse)
- [ResourceLimitExceeded](./client.md#resourcelimitexceeded)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceAlreadyExists](./client.md#servicealreadyexists)
- [ServiceNotFound](./client.md#servicenotfound)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("servicediscovery").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_servicediscovery.paginators import ListInstancesPaginator, ...
```

- [ListInstancesPaginator](./paginators.md#listinstancespaginator)
- [ListNamespacesPaginator](./paginators.md#listnamespacespaginator)
- [ListOperationsPaginator](./paginators.md#listoperationspaginator)
- [ListServicesPaginator](./paginators.md#listservicespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_servicediscovery.literals import CustomHealthStatus, ...
```

- [CustomHealthStatus](./literals.md#customhealthstatus)
- [FilterCondition](./literals.md#filtercondition)
- [HealthCheckType](./literals.md#healthchecktype)
- [HealthStatus](./literals.md#healthstatus)
- [HealthStatusFilter](./literals.md#healthstatusfilter)
- [ListInstancesPaginatorName](./literals.md#listinstancespaginatorname)
- [ListNamespacesPaginatorName](./literals.md#listnamespacespaginatorname)
- [ListOperationsPaginatorName](./literals.md#listoperationspaginatorname)
- [ListServicesPaginatorName](./literals.md#listservicespaginatorname)
- [NamespaceFilterName](./literals.md#namespacefiltername)
- [NamespaceType](./literals.md#namespacetype)
- [OperationFilterName](./literals.md#operationfiltername)
- [OperationStatus](./literals.md#operationstatus)
- [OperationTargetType](./literals.md#operationtargettype)
- [OperationType](./literals.md#operationtype)
- [RecordType](./literals.md#recordtype)
- [RoutingPolicy](./literals.md#routingpolicy)
- [ServiceFilterName](./literals.md#servicefiltername)
- [ServiceType](./literals.md#servicetype)
- [ServiceTypeOption](./literals.md#servicetypeoption)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_servicediscovery.type_defs import DnsConfigChangeTypeDef, ...
```

- [DnsConfigChangeTypeDef](./type_defs.md#dnsconfigchangetypedef)
- [DnsConfigTypeDef](./type_defs.md#dnsconfigtypedef)
- [DnsPropertiesTypeDef](./type_defs.md#dnspropertiestypedef)
- [DnsRecordTypeDef](./type_defs.md#dnsrecordtypedef)
- [HealthCheckConfigTypeDef](./type_defs.md#healthcheckconfigtypedef)
- [HealthCheckCustomConfigTypeDef](./type_defs.md#healthcheckcustomconfigtypedef)
- [HttpInstanceSummaryTypeDef](./type_defs.md#httpinstancesummarytypedef)
- [HttpPropertiesTypeDef](./type_defs.md#httppropertiestypedef)
- [InstanceSummaryTypeDef](./type_defs.md#instancesummarytypedef)
- [InstanceTypeDef](./type_defs.md#instancetypedef)
- [NamespacePropertiesTypeDef](./type_defs.md#namespacepropertiestypedef)
- [NamespaceSummaryTypeDef](./type_defs.md#namespacesummarytypedef)
- [NamespaceTypeDef](./type_defs.md#namespacetypedef)
- [OperationSummaryTypeDef](./type_defs.md#operationsummarytypedef)
- [OperationTypeDef](./type_defs.md#operationtypedef)
- [ServiceSummaryTypeDef](./type_defs.md#servicesummarytypedef)
- [ServiceTypeDef](./type_defs.md#servicetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CreateHttpNamespaceResponseTypeDef](./type_defs.md#createhttpnamespaceresponsetypedef)
- [CreatePrivateDnsNamespaceResponseTypeDef](./type_defs.md#createprivatednsnamespaceresponsetypedef)
- [CreatePublicDnsNamespaceResponseTypeDef](./type_defs.md#createpublicdnsnamespaceresponsetypedef)
- [CreateServiceResponseTypeDef](./type_defs.md#createserviceresponsetypedef)
- [DeleteNamespaceResponseTypeDef](./type_defs.md#deletenamespaceresponsetypedef)
- [DeregisterInstanceResponseTypeDef](./type_defs.md#deregisterinstanceresponsetypedef)
- [DiscoverInstancesResponseTypeDef](./type_defs.md#discoverinstancesresponsetypedef)
- [GetInstanceResponseTypeDef](./type_defs.md#getinstanceresponsetypedef)
- [GetInstancesHealthStatusResponseTypeDef](./type_defs.md#getinstanceshealthstatusresponsetypedef)
- [GetNamespaceResponseTypeDef](./type_defs.md#getnamespaceresponsetypedef)
- [GetOperationResponseTypeDef](./type_defs.md#getoperationresponsetypedef)
- [GetServiceResponseTypeDef](./type_defs.md#getserviceresponsetypedef)
- [ListInstancesResponseTypeDef](./type_defs.md#listinstancesresponsetypedef)
- [ListNamespacesResponseTypeDef](./type_defs.md#listnamespacesresponsetypedef)
- [ListOperationsResponseTypeDef](./type_defs.md#listoperationsresponsetypedef)
- [ListServicesResponseTypeDef](./type_defs.md#listservicesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NamespaceFilterTypeDef](./type_defs.md#namespacefiltertypedef)
- [OperationFilterTypeDef](./type_defs.md#operationfiltertypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RegisterInstanceResponseTypeDef](./type_defs.md#registerinstanceresponsetypedef)
- [ServiceChangeTypeDef](./type_defs.md#servicechangetypedef)
- [ServiceFilterTypeDef](./type_defs.md#servicefiltertypedef)
- [UpdateServiceResponseTypeDef](./type_defs.md#updateserviceresponsetypedef)
