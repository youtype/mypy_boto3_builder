# Paginators for boto3 Route53 module

> [Index](../index.md) > [Route53](./index.md) > Paginators

Auto-generated documentation for [Route53](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53)
type annotations stubs module [mypy_boto3_route53](https://pypi.org/project/mypy-boto3-route53/).

- [Paginators for boto3 Route53 module](#paginators-for-boto3-route53-module)
  - [ListHealthChecksPaginator](#listhealthcheckspaginator)
  - [ListHostedZonesPaginator](#listhostedzonespaginator)
  - [ListQueryLoggingConfigsPaginator](#listqueryloggingconfigspaginator)
  - [ListResourceRecordSetsPaginator](#listresourcerecordsetspaginator)
  - [ListVPCAssociationAuthorizationsPaginator](#listvpcassociationauthorizationspaginator)

## ListHealthChecksPaginator

Type annotations for `boto3.client("route53").get_paginator("list_health_checks")`.

Can be used directly:

```python
from mypy_boto3_route53.paginators import ListHealthChecksPaginator

def get_list_health_checks_paginator() -> ListHealthChecksPaginator:
    return boto3.client("route53").get_paginator("list_health_checks")
```

[Paginator.ListHealthChecks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListHealthChecks)

```python
class ListHealthChecksPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHealthChecksResponseTypeDef]:
        pass
```
## ListHostedZonesPaginator

Type annotations for `boto3.client("route53").get_paginator("list_hosted_zones")`.

Can be used directly:

```python
from mypy_boto3_route53.paginators import ListHostedZonesPaginator

def get_list_hosted_zones_paginator() -> ListHostedZonesPaginator:
    return boto3.client("route53").get_paginator("list_hosted_zones")
```

[Paginator.ListHostedZones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListHostedZones)

```python
class ListHostedZonesPaginator(Boto3Paginator):
    def paginate(
        self,
        DelegationSetId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHostedZonesResponseTypeDef]:
        pass
```
## ListQueryLoggingConfigsPaginator

Type annotations for `boto3.client("route53").get_paginator("list_query_logging_configs")`.

Can be used directly:

```python
from mypy_boto3_route53.paginators import ListQueryLoggingConfigsPaginator

def get_list_query_logging_configs_paginator() -> ListQueryLoggingConfigsPaginator:
    return boto3.client("route53").get_paginator("list_query_logging_configs")
```

[Paginator.ListQueryLoggingConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)

```python
class ListQueryLoggingConfigsPaginator(Boto3Paginator):
    def paginate(
        self,
        HostedZoneId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueryLoggingConfigsResponseTypeDef]:
        pass
```
## ListResourceRecordSetsPaginator

Type annotations for `boto3.client("route53").get_paginator("list_resource_record_sets")`.

Can be used directly:

```python
from mypy_boto3_route53.paginators import ListResourceRecordSetsPaginator

def get_list_resource_record_sets_paginator() -> ListResourceRecordSetsPaginator:
    return boto3.client("route53").get_paginator("list_resource_record_sets")
```

[Paginator.ListResourceRecordSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)

```python
class ListResourceRecordSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        HostedZoneId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceRecordSetsResponseTypeDef]:
        pass
```
## ListVPCAssociationAuthorizationsPaginator

Type annotations for `boto3.client("route53").get_paginator("list_vpc_association_authorizations")`.

Can be used directly:

```python
from mypy_boto3_route53.paginators import ListVPCAssociationAuthorizationsPaginator

def get_list_vpc_association_authorizations_paginator() -> ListVPCAssociationAuthorizationsPaginator:
    return boto3.client("route53").get_paginator("list_vpc_association_authorizations")
```

[Paginator.ListVPCAssociationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)

```python
class ListVPCAssociationAuthorizationsPaginator(Boto3Paginator):
    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVPCAssociationAuthorizationsResponseTypeDef]:
        pass
```