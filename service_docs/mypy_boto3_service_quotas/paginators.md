# Paginators for boto3 ServiceQuotas module

> [Index](../index.md) > [ServiceQuotas](./index.md) > Paginators

Auto-generated documentation for [ServiceQuotas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas)
type annotations stubs module [mypy_boto3_service_quotas](https://pypi.org/project/mypy-boto3-service-quotas/).

- [Paginators for boto3 ServiceQuotas module](#paginators-for-boto3-servicequotas-module)
  - [ListAWSDefaultServiceQuotasPaginator](#listawsdefaultservicequotaspaginator)
  - [ListRequestedServiceQuotaChangeHistoryPaginator](#listrequestedservicequotachangehistorypaginator)
  - [ListRequestedServiceQuotaChangeHistoryByQuotaPaginator](#listrequestedservicequotachangehistorybyquotapaginator)
  - [ListServiceQuotaIncreaseRequestsInTemplatePaginator](#listservicequotaincreaserequestsintemplatepaginator)
  - [ListServiceQuotasPaginator](#listservicequotaspaginator)
  - [ListServicesPaginator](#listservicespaginator)

## ListAWSDefaultServiceQuotasPaginator

Type annotations for `boto3.client("service-quotas").get_paginator("list_aws_default_service_quotas")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListAWSDefaultServiceQuotasPaginator

def get_list_aws_default_service_quotas_paginator() -> ListAWSDefaultServiceQuotasPaginator:
    return boto3.client("service-quotas").get_paginator("list_aws_default_service_quotas")
```

[Paginator.ListAWSDefaultServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)

```python
class ListAWSDefaultServiceQuotasPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAWSDefaultServiceQuotasResponseTypeDef]:
        pass
```
## ListRequestedServiceQuotaChangeHistoryPaginator

Type annotations for `boto3.client("service-quotas").get_paginator("list_requested_service_quota_change_history")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListRequestedServiceQuotaChangeHistoryPaginator

def get_list_requested_service_quota_change_history_paginator() -> ListRequestedServiceQuotaChangeHistoryPaginator:
    return boto3.client("service-quotas").get_paginator("list_requested_service_quota_change_history")
```

[Paginator.ListRequestedServiceQuotaChangeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)

```python
class ListRequestedServiceQuotaChangeHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str = None,
        Status: RequestStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRequestedServiceQuotaChangeHistoryResponseTypeDef]:
        pass
```
## ListRequestedServiceQuotaChangeHistoryByQuotaPaginator

Type annotations for `boto3.client("service-quotas").get_paginator("list_requested_service_quota_change_history_by_quota")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListRequestedServiceQuotaChangeHistoryByQuotaPaginator

def get_list_requested_service_quota_change_history_by_quota_paginator() -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
    return boto3.client("service-quotas").get_paginator("list_requested_service_quota_change_history_by_quota")
```

[Paginator.ListRequestedServiceQuotaChangeHistoryByQuota documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)

```python
class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: RequestStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef]:
        pass
```
## ListServiceQuotaIncreaseRequestsInTemplatePaginator

Type annotations for `boto3.client("service-quotas").get_paginator("list_service_quota_increase_requests_in_template")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListServiceQuotaIncreaseRequestsInTemplatePaginator

def get_list_service_quota_increase_requests_in_template_paginator() -> ListServiceQuotaIncreaseRequestsInTemplatePaginator:
    return boto3.client("service-quotas").get_paginator("list_service_quota_increase_requests_in_template")
```

[Paginator.ListServiceQuotaIncreaseRequestsInTemplate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)

```python
class ListServiceQuotaIncreaseRequestsInTemplatePaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef]:
        pass
```
## ListServiceQuotasPaginator

Type annotations for `boto3.client("service-quotas").get_paginator("list_service_quotas")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListServiceQuotasPaginator

def get_list_service_quotas_paginator() -> ListServiceQuotasPaginator:
    return boto3.client("service-quotas").get_paginator("list_service_quotas")
```

[Paginator.ListServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)

```python
class ListServiceQuotasPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceCode: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceQuotasResponseTypeDef]:
        pass
```
## ListServicesPaginator

Type annotations for `boto3.client("service-quotas").get_paginator("list_services")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListServicesPaginator

def get_list_services_paginator() -> ListServicesPaginator:
    return boto3.client("service-quotas").get_paginator("list_services")
```

[Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)

```python
class ListServicesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        pass
```