# Literals for boto3 ServiceDiscovery module

> [Index](../index.md) > [ServiceDiscovery](./index.md) > Literals

Auto-generated documentation for [ServiceDiscovery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html#ServiceDiscovery)
type annotations stubs module [mypy_boto3_servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/).

- [Literals for boto3 ServiceDiscovery module](#literals-for-boto3-servicediscovery-module)
  - [CustomHealthStatus](#customhealthstatus)
  - [FilterCondition](#filtercondition)
  - [HealthCheckType](#healthchecktype)
  - [HealthStatus](#healthstatus)
  - [HealthStatusFilter](#healthstatusfilter)
  - [ListInstancesPaginatorName](#listinstancespaginatorname)
  - [ListNamespacesPaginatorName](#listnamespacespaginatorname)
  - [ListOperationsPaginatorName](#listoperationspaginatorname)
  - [ListServicesPaginatorName](#listservicespaginatorname)
  - [NamespaceFilterName](#namespacefiltername)
  - [NamespaceType](#namespacetype)
  - [OperationFilterName](#operationfiltername)
  - [OperationStatus](#operationstatus)
  - [OperationTargetType](#operationtargettype)
  - [OperationType](#operationtype)
  - [RecordType](#recordtype)
  - [RoutingPolicy](#routingpolicy)
  - [ServiceFilterName](#servicefiltername)
  - [ServiceType](#servicetype)
  - [ServiceTypeOption](#servicetypeoption)

## CustomHealthStatus

```python
from mypy_boto3_servicediscovery.literals import CustomHealthStatus
```

Values:

- `HEALTHY`
- `UNHEALTHY`

## FilterCondition

```python
from mypy_boto3_servicediscovery.literals import FilterCondition
```

Values:

- `BETWEEN`
- `EQ`
- `IN`

## HealthCheckType

```python
from mypy_boto3_servicediscovery.literals import HealthCheckType
```

Values:

- `HTTP`
- `HTTPS`
- `TCP`

## HealthStatus

```python
from mypy_boto3_servicediscovery.literals import HealthStatus
```

Values:

- `HEALTHY`
- `UNHEALTHY`
- `UNKNOWN`

## HealthStatusFilter

```python
from mypy_boto3_servicediscovery.literals import HealthStatusFilter
```

Values:

- `ALL`
- `HEALTHY`
- `UNHEALTHY`

## ListInstancesPaginatorName

```python
from mypy_boto3_servicediscovery.literals import ListInstancesPaginatorName
```

Values:

- `list_instances`

## ListNamespacesPaginatorName

```python
from mypy_boto3_servicediscovery.literals import ListNamespacesPaginatorName
```

Values:

- `list_namespaces`

## ListOperationsPaginatorName

```python
from mypy_boto3_servicediscovery.literals import ListOperationsPaginatorName
```

Values:

- `list_operations`

## ListServicesPaginatorName

```python
from mypy_boto3_servicediscovery.literals import ListServicesPaginatorName
```

Values:

- `list_services`

## NamespaceFilterName

```python
from mypy_boto3_servicediscovery.literals import NamespaceFilterName
```

Values:

- `TYPE`

## NamespaceType

```python
from mypy_boto3_servicediscovery.literals import NamespaceType
```

Values:

- `DNS_PRIVATE`
- `DNS_PUBLIC`
- `HTTP`

## OperationFilterName

```python
from mypy_boto3_servicediscovery.literals import OperationFilterName
```

Values:

- `NAMESPACE_ID`
- `SERVICE_ID`
- `STATUS`
- `TYPE`
- `UPDATE_DATE`

## OperationStatus

```python
from mypy_boto3_servicediscovery.literals import OperationStatus
```

Values:

- `FAIL`
- `PENDING`
- `SUBMITTED`
- `SUCCESS`

## OperationTargetType

```python
from mypy_boto3_servicediscovery.literals import OperationTargetType
```

Values:

- `INSTANCE`
- `NAMESPACE`
- `SERVICE`

## OperationType

```python
from mypy_boto3_servicediscovery.literals import OperationType
```

Values:

- `CREATE_NAMESPACE`
- `DELETE_NAMESPACE`
- `DEREGISTER_INSTANCE`
- `REGISTER_INSTANCE`
- `UPDATE_SERVICE`

## RecordType

```python
from mypy_boto3_servicediscovery.literals import RecordType
```

Values:

- `A`
- `AAAA`
- `CNAME`
- `SRV`

## RoutingPolicy

```python
from mypy_boto3_servicediscovery.literals import RoutingPolicy
```

Values:

- `MULTIVALUE`
- `WEIGHTED`

## ServiceFilterName

```python
from mypy_boto3_servicediscovery.literals import ServiceFilterName
```

Values:

- `NAMESPACE_ID`

## ServiceType

```python
from mypy_boto3_servicediscovery.literals import ServiceType
```

Values:

- `DNS`
- `DNS_HTTP`
- `HTTP`

## ServiceTypeOption

```python
from mypy_boto3_servicediscovery.literals import ServiceTypeOption
```

Values:

- `HTTP`
