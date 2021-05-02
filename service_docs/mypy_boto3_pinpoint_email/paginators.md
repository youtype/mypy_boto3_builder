# Paginators for boto3 PinpointEmail module

> [Index](../index.md) > [PinpointEmail](./index.md) > Paginators

Auto-generated documentation for [PinpointEmail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail)
type annotations stubs module [mypy_boto3_pinpoint_email](https://pypi.org/project/mypy-boto3-pinpoint-email/).

- [Paginators for boto3 PinpointEmail module](#paginators-for-boto3-pinpointemail-module)
  - [GetDedicatedIpsPaginator](#getdedicatedipspaginator)
  - [ListConfigurationSetsPaginator](#listconfigurationsetspaginator)
  - [ListDedicatedIpPoolsPaginator](#listdedicatedippoolspaginator)
  - [ListDeliverabilityTestReportsPaginator](#listdeliverabilitytestreportspaginator)
  - [ListEmailIdentitiesPaginator](#listemailidentitiespaginator)

## GetDedicatedIpsPaginator

Type annotations for `boto3.client("pinpoint-email").get_paginator("get_dedicated_ips")`.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.paginators import GetDedicatedIpsPaginator

def get_get_dedicated_ips_paginator() -> GetDedicatedIpsPaginator:
    return boto3.client("pinpoint-email").get_paginator("get_dedicated_ips")
```

[Paginator.GetDedicatedIps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)

```python
class GetDedicatedIpsPaginator(Boto3Paginator):
    def paginate(
        self,
        PoolName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDedicatedIpsResponseTypeDef]:
        pass
```
## ListConfigurationSetsPaginator

Type annotations for `boto3.client("pinpoint-email").get_paginator("list_configuration_sets")`.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.paginators import ListConfigurationSetsPaginator

def get_list_configuration_sets_paginator() -> ListConfigurationSetsPaginator:
    return boto3.client("pinpoint-email").get_paginator("list_configuration_sets")
```

[Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)

```python
class ListConfigurationSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationSetsResponseTypeDef]:
        pass
```
## ListDedicatedIpPoolsPaginator

Type annotations for `boto3.client("pinpoint-email").get_paginator("list_dedicated_ip_pools")`.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.paginators import ListDedicatedIpPoolsPaginator

def get_list_dedicated_ip_pools_paginator() -> ListDedicatedIpPoolsPaginator:
    return boto3.client("pinpoint-email").get_paginator("list_dedicated_ip_pools")
```

[Paginator.ListDedicatedIpPools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)

```python
class ListDedicatedIpPoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDedicatedIpPoolsResponseTypeDef]:
        pass
```
## ListDeliverabilityTestReportsPaginator

Type annotations for `boto3.client("pinpoint-email").get_paginator("list_deliverability_test_reports")`.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.paginators import ListDeliverabilityTestReportsPaginator

def get_list_deliverability_test_reports_paginator() -> ListDeliverabilityTestReportsPaginator:
    return boto3.client("pinpoint-email").get_paginator("list_deliverability_test_reports")
```

[Paginator.ListDeliverabilityTestReports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)

```python
class ListDeliverabilityTestReportsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeliverabilityTestReportsResponseTypeDef]:
        pass
```
## ListEmailIdentitiesPaginator

Type annotations for `boto3.client("pinpoint-email").get_paginator("list_email_identities")`.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.paginators import ListEmailIdentitiesPaginator

def get_list_email_identities_paginator() -> ListEmailIdentitiesPaginator:
    return boto3.client("pinpoint-email").get_paginator("list_email_identities")
```

[Paginator.ListEmailIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)

```python
class ListEmailIdentitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEmailIdentitiesResponseTypeDef]:
        pass
```