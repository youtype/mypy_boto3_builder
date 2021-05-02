# Literals for boto3 ServiceQuotas module

> [Index](../index.md) > [ServiceQuotas](./index.md) > Literals

Auto-generated documentation for [ServiceQuotas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas)
type annotations stubs module [mypy_boto3_service_quotas](https://pypi.org/project/mypy-boto3-service-quotas/).

- [Literals for boto3 ServiceQuotas module](#literals-for-boto3-servicequotas-module)
  - [ErrorCode](#errorcode)
  - [ListAWSDefaultServiceQuotasPaginatorName](#listawsdefaultservicequotaspaginatorname)
  - [ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName](#listrequestedservicequotachangehistorybyquotapaginatorname)
  - [ListRequestedServiceQuotaChangeHistoryPaginatorName](#listrequestedservicequotachangehistorypaginatorname)
  - [ListServiceQuotaIncreaseRequestsInTemplatePaginatorName](#listservicequotaincreaserequestsintemplatepaginatorname)
  - [ListServiceQuotasPaginatorName](#listservicequotaspaginatorname)
  - [ListServicesPaginatorName](#listservicespaginatorname)
  - [PeriodUnit](#periodunit)
  - [RequestStatus](#requeststatus)
  - [ServiceQuotaTemplateAssociationStatus](#servicequotatemplateassociationstatus)

## ErrorCode

```python
from mypy_boto3_service_quotas.literals import ErrorCode
```

Values:

- `DEPENDENCY_ACCESS_DENIED_ERROR`
- `DEPENDENCY_SERVICE_ERROR`
- `DEPENDENCY_THROTTLING_ERROR`
- `SERVICE_QUOTA_NOT_AVAILABLE_ERROR`

## ListAWSDefaultServiceQuotasPaginatorName

```python
from mypy_boto3_service_quotas.literals import ListAWSDefaultServiceQuotasPaginatorName
```

Values:

- `list_aws_default_service_quotas`

## ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName

```python
from mypy_boto3_service_quotas.literals import ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName
```

Values:

- `list_requested_service_quota_change_history_by_quota`

## ListRequestedServiceQuotaChangeHistoryPaginatorName

```python
from mypy_boto3_service_quotas.literals import ListRequestedServiceQuotaChangeHistoryPaginatorName
```

Values:

- `list_requested_service_quota_change_history`

## ListServiceQuotaIncreaseRequestsInTemplatePaginatorName

```python
from mypy_boto3_service_quotas.literals import ListServiceQuotaIncreaseRequestsInTemplatePaginatorName
```

Values:

- `list_service_quota_increase_requests_in_template`

## ListServiceQuotasPaginatorName

```python
from mypy_boto3_service_quotas.literals import ListServiceQuotasPaginatorName
```

Values:

- `list_service_quotas`

## ListServicesPaginatorName

```python
from mypy_boto3_service_quotas.literals import ListServicesPaginatorName
```

Values:

- `list_services`

## PeriodUnit

```python
from mypy_boto3_service_quotas.literals import PeriodUnit
```

Values:

- `DAY`
- `HOUR`
- `MICROSECOND`
- `MILLISECOND`
- `MINUTE`
- `SECOND`
- `WEEK`

## RequestStatus

```python
from mypy_boto3_service_quotas.literals import RequestStatus
```

Values:

- `APPROVED`
- `CASE_CLOSED`
- `CASE_OPENED`
- `DENIED`
- `PENDING`

## ServiceQuotaTemplateAssociationStatus

```python
from mypy_boto3_service_quotas.literals import ServiceQuotaTemplateAssociationStatus
```

Values:

- `ASSOCIATED`
- `DISASSOCIATED`
