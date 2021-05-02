# Structures for boto3 ServiceDiscovery module

> [Index](../index.md) > [ServiceDiscovery](./index.md) > Structures

Auto-generated documentation for [ServiceDiscovery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery)
type annotations stubs module [mypy_boto3_servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/).

- [Structures for boto3 ServiceDiscovery module](#structures-for-boto3-servicediscovery-module)
  - [CreateHttpNamespaceResponseTypeDef](#createhttpnamespaceresponsetypedef)
  - [CreatePrivateDnsNamespaceResponseTypeDef](#createprivatednsnamespaceresponsetypedef)
  - [CreatePublicDnsNamespaceResponseTypeDef](#createpublicdnsnamespaceresponsetypedef)
  - [CreateServiceResponseTypeDef](#createserviceresponsetypedef)
  - [DeleteNamespaceResponseTypeDef](#deletenamespaceresponsetypedef)
  - [DeregisterInstanceResponseTypeDef](#deregisterinstanceresponsetypedef)
  - [DiscoverInstancesResponseTypeDef](#discoverinstancesresponsetypedef)
  - [DnsConfigChangeTypeDef](#dnsconfigchangetypedef)
  - [DnsConfigTypeDef](#dnsconfigtypedef)
  - [DnsPropertiesTypeDef](#dnspropertiestypedef)
  - [DnsRecordTypeDef](#dnsrecordtypedef)
  - [GetInstanceResponseTypeDef](#getinstanceresponsetypedef)
  - [GetInstancesHealthStatusResponseTypeDef](#getinstanceshealthstatusresponsetypedef)
  - [GetNamespaceResponseTypeDef](#getnamespaceresponsetypedef)
  - [GetOperationResponseTypeDef](#getoperationresponsetypedef)
  - [GetServiceResponseTypeDef](#getserviceresponsetypedef)
  - [HealthCheckConfigTypeDef](#healthcheckconfigtypedef)
  - [HealthCheckCustomConfigTypeDef](#healthcheckcustomconfigtypedef)
  - [HttpInstanceSummaryTypeDef](#httpinstancesummarytypedef)
  - [HttpPropertiesTypeDef](#httppropertiestypedef)
  - [InstanceSummaryTypeDef](#instancesummarytypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [ListInstancesResponseTypeDef](#listinstancesresponsetypedef)
  - [ListNamespacesResponseTypeDef](#listnamespacesresponsetypedef)
  - [ListOperationsResponseTypeDef](#listoperationsresponsetypedef)
  - [ListServicesResponseTypeDef](#listservicesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [NamespaceFilterTypeDef](#namespacefiltertypedef)
  - [NamespacePropertiesTypeDef](#namespacepropertiestypedef)
  - [NamespaceSummaryTypeDef](#namespacesummarytypedef)
  - [NamespaceTypeDef](#namespacetypedef)
  - [OperationFilterTypeDef](#operationfiltertypedef)
  - [OperationSummaryTypeDef](#operationsummarytypedef)
  - [OperationTypeDef](#operationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RegisterInstanceResponseTypeDef](#registerinstanceresponsetypedef)
  - [ServiceChangeTypeDef](#servicechangetypedef)
  - [ServiceFilterTypeDef](#servicefiltertypedef)
  - [ServiceSummaryTypeDef](#servicesummarytypedef)
  - [ServiceTypeDef](#servicetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateServiceResponseTypeDef](#updateserviceresponsetypedef)

## CreateHttpNamespaceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import CreateHttpNamespaceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`


## CreatePrivateDnsNamespaceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import CreatePrivateDnsNamespaceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`


## CreatePublicDnsNamespaceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import CreatePublicDnsNamespaceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`


## CreateServiceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import CreateServiceResponseTypeDef
```




Optional fields:
- `Service`: `"ServiceTypeDef"`


## DeleteNamespaceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DeleteNamespaceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`


## DeregisterInstanceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DeregisterInstanceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`


## DiscoverInstancesResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DiscoverInstancesResponseTypeDef
```




Optional fields:
- `Instances`: `List["HttpInstanceSummaryTypeDef"]`


## DnsConfigChangeTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DnsConfigChangeTypeDef
```


Required fields:
- `DnsRecords`: `List["DnsRecordTypeDef"]`




## DnsConfigTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DnsConfigTypeDef
```


Required fields:
- `DnsRecords`: `List["DnsRecordTypeDef"]`



Optional fields:
- `NamespaceId`: `str`
- `RoutingPolicy`: `RoutingPolicy`


## DnsPropertiesTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DnsPropertiesTypeDef
```




Optional fields:
- `HostedZoneId`: `str`


## DnsRecordTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import DnsRecordTypeDef
```


Required fields:
- `Type`: `RecordType`
- `TTL`: `int`




## GetInstanceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import GetInstanceResponseTypeDef
```




Optional fields:
- `Instance`: `"InstanceTypeDef"`


## GetInstancesHealthStatusResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import GetInstancesHealthStatusResponseTypeDef
```




Optional fields:
- `Status`: `Dict[str, HealthStatus]`
- `NextToken`: `str`


## GetNamespaceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import GetNamespaceResponseTypeDef
```




Optional fields:
- `Namespace`: `"NamespaceTypeDef"`


## GetOperationResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import GetOperationResponseTypeDef
```




Optional fields:
- `Operation`: `"OperationTypeDef"`


## GetServiceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import GetServiceResponseTypeDef
```




Optional fields:
- `Service`: `"ServiceTypeDef"`


## HealthCheckConfigTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import HealthCheckConfigTypeDef
```


Required fields:
- `Type`: `HealthCheckType`



Optional fields:
- `ResourcePath`: `str`
- `FailureThreshold`: `int`


## HealthCheckCustomConfigTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import HealthCheckCustomConfigTypeDef
```




Optional fields:
- `FailureThreshold`: `int`


## HttpInstanceSummaryTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import HttpInstanceSummaryTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `NamespaceName`: `str`
- `ServiceName`: `str`
- `HealthStatus`: `HealthStatus`
- `Attributes`: `Dict[str, str]`


## HttpPropertiesTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import HttpPropertiesTypeDef
```




Optional fields:
- `HttpName`: `str`


## InstanceSummaryTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import InstanceSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Attributes`: `Dict[str, str]`


## InstanceTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import InstanceTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `CreatorRequestId`: `str`
- `Attributes`: `Dict[str, str]`


## ListInstancesResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ListInstancesResponseTypeDef
```




Optional fields:
- `Instances`: `List["InstanceSummaryTypeDef"]`
- `NextToken`: `str`


## ListNamespacesResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ListNamespacesResponseTypeDef
```




Optional fields:
- `Namespaces`: `List["NamespaceSummaryTypeDef"]`
- `NextToken`: `str`


## ListOperationsResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ListOperationsResponseTypeDef
```




Optional fields:
- `Operations`: `List["OperationSummaryTypeDef"]`
- `NextToken`: `str`


## ListServicesResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ListServicesResponseTypeDef
```




Optional fields:
- `Services`: `List["ServiceSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## NamespaceFilterTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import NamespaceFilterTypeDef
```


Required fields:
- `Name`: `Literal['TYPE']`
- `Values`: `List[str]`



Optional fields:
- `Condition`: `FilterCondition`


## NamespacePropertiesTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import NamespacePropertiesTypeDef
```




Optional fields:
- `DnsProperties`: `"DnsPropertiesTypeDef"`
- `HttpProperties`: `"HttpPropertiesTypeDef"`


## NamespaceSummaryTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import NamespaceSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Type`: `NamespaceType`
- `Description`: `str`
- `ServiceCount`: `int`
- `Properties`: `"NamespacePropertiesTypeDef"`
- `CreateDate`: `datetime`


## NamespaceTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import NamespaceTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Type`: `NamespaceType`
- `Description`: `str`
- `ServiceCount`: `int`
- `Properties`: `"NamespacePropertiesTypeDef"`
- `CreateDate`: `datetime`
- `CreatorRequestId`: `str`


## OperationFilterTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import OperationFilterTypeDef
```


Required fields:
- `Name`: `OperationFilterName`
- `Values`: `List[str]`



Optional fields:
- `Condition`: `FilterCondition`


## OperationSummaryTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import OperationSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Status`: `OperationStatus`


## OperationTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import OperationTypeDef
```




Optional fields:
- `Id`: `str`
- `Type`: `OperationType`
- `Status`: `OperationStatus`
- `ErrorMessage`: `str`
- `ErrorCode`: `str`
- `CreateDate`: `datetime`
- `UpdateDate`: `datetime`
- `Targets`: `Dict[OperationTargetType, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RegisterInstanceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import RegisterInstanceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`


## ServiceChangeTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ServiceChangeTypeDef
```




Optional fields:
- `Description`: `str`
- `DnsConfig`: `"DnsConfigChangeTypeDef"`
- `HealthCheckConfig`: `"HealthCheckConfigTypeDef"`


## ServiceFilterTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ServiceFilterTypeDef
```


Required fields:
- `Name`: `Literal['NAMESPACE_ID']`
- `Values`: `List[str]`



Optional fields:
- `Condition`: `FilterCondition`


## ServiceSummaryTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ServiceSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Type`: `ServiceType`
- `Description`: `str`
- `InstanceCount`: `int`
- `DnsConfig`: `"DnsConfigTypeDef"`
- `HealthCheckConfig`: `"HealthCheckConfigTypeDef"`
- `HealthCheckCustomConfig`: `"HealthCheckCustomConfigTypeDef"`
- `CreateDate`: `datetime`


## ServiceTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import ServiceTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `NamespaceId`: `str`
- `Description`: `str`
- `InstanceCount`: `int`
- `DnsConfig`: `"DnsConfigTypeDef"`
- `Type`: `ServiceType`
- `HealthCheckConfig`: `"HealthCheckConfigTypeDef"`
- `HealthCheckCustomConfig`: `"HealthCheckCustomConfigTypeDef"`
- `CreateDate`: `datetime`
- `CreatorRequestId`: `str`


## TagTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UpdateServiceResponseTypeDef

```python
from mypy_boto3_servicediscovery.type_defs import UpdateServiceResponseTypeDef
```




Optional fields:
- `OperationId`: `str`

