# Structures for boto3 ServiceQuotas module

> [Index](../index.md) > [ServiceQuotas](./index.md) > Structures

Auto-generated documentation for [ServiceQuotas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas)
type annotations stubs module [mypy_boto3_service_quotas](https://pypi.org/project/mypy-boto3-service-quotas/).

- [Structures for boto3 ServiceQuotas module](#structures-for-boto3-servicequotas-module)
  - [ErrorReasonTypeDef](#errorreasontypedef)
  - [MetricInfoTypeDef](#metricinfotypedef)
  - [QuotaPeriodTypeDef](#quotaperiodtypedef)
  - [RequestedServiceQuotaChangeTypeDef](#requestedservicequotachangetypedef)
  - [ServiceInfoTypeDef](#serviceinfotypedef)
  - [ServiceQuotaIncreaseRequestInTemplateTypeDef](#servicequotaincreaserequestintemplatetypedef)
  - [ServiceQuotaTypeDef](#servicequotatypedef)
  - [TagTypeDef](#tagtypedef)
  - [GetAWSDefaultServiceQuotaResponseTypeDef](#getawsdefaultservicequotaresponsetypedef)
  - [GetAssociationForServiceQuotaTemplateResponseTypeDef](#getassociationforservicequotatemplateresponsetypedef)
  - [GetRequestedServiceQuotaChangeResponseTypeDef](#getrequestedservicequotachangeresponsetypedef)
  - [GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef](#getservicequotaincreaserequestfromtemplateresponsetypedef)
  - [GetServiceQuotaResponseTypeDef](#getservicequotaresponsetypedef)
  - [ListAWSDefaultServiceQuotasResponseTypeDef](#listawsdefaultservicequotasresponsetypedef)
  - [ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef](#listrequestedservicequotachangehistorybyquotaresponsetypedef)
  - [ListRequestedServiceQuotaChangeHistoryResponseTypeDef](#listrequestedservicequotachangehistoryresponsetypedef)
  - [ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef](#listservicequotaincreaserequestsintemplateresponsetypedef)
  - [ListServiceQuotasResponseTypeDef](#listservicequotasresponsetypedef)
  - [ListServicesResponseTypeDef](#listservicesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef](#putservicequotaincreaserequestintotemplateresponsetypedef)
  - [RequestServiceQuotaIncreaseResponseTypeDef](#requestservicequotaincreaseresponsetypedef)

## ErrorReasonTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ErrorReasonTypeDef
```




Optional fields:
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## MetricInfoTypeDef

```python
from mypy_boto3_service_quotas.type_defs import MetricInfoTypeDef
```




Optional fields:
- `MetricNamespace`: `str`
- `MetricName`: `str`
- `MetricDimensions`: `Dict[str, str]`
- `MetricStatisticRecommendation`: `str`


## QuotaPeriodTypeDef

```python
from mypy_boto3_service_quotas.type_defs import QuotaPeriodTypeDef
```




Optional fields:
- `PeriodValue`: `int`
- `PeriodUnit`: `PeriodUnit`


## RequestedServiceQuotaChangeTypeDef

```python
from mypy_boto3_service_quotas.type_defs import RequestedServiceQuotaChangeTypeDef
```




Optional fields:
- `Id`: `str`
- `CaseId`: `str`
- `ServiceCode`: `str`
- `ServiceName`: `str`
- `QuotaCode`: `str`
- `QuotaName`: `str`
- `DesiredValue`: `float`
- `Status`: `RequestStatus`
- `Created`: `datetime`
- `LastUpdated`: `datetime`
- `Requester`: `str`
- `QuotaArn`: `str`
- `GlobalQuota`: `bool`
- `Unit`: `str`


## ServiceInfoTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ServiceInfoTypeDef
```




Optional fields:
- `ServiceCode`: `str`
- `ServiceName`: `str`


## ServiceQuotaIncreaseRequestInTemplateTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ServiceQuotaIncreaseRequestInTemplateTypeDef
```




Optional fields:
- `ServiceCode`: `str`
- `ServiceName`: `str`
- `QuotaCode`: `str`
- `QuotaName`: `str`
- `DesiredValue`: `float`
- `AwsRegion`: `str`
- `Unit`: `str`
- `GlobalQuota`: `bool`


## ServiceQuotaTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ServiceQuotaTypeDef
```




Optional fields:
- `ServiceCode`: `str`
- `ServiceName`: `str`
- `QuotaArn`: `str`
- `QuotaCode`: `str`
- `QuotaName`: `str`
- `Value`: `float`
- `Unit`: `str`
- `Adjustable`: `bool`
- `GlobalQuota`: `bool`
- `UsageMetric`: `"MetricInfoTypeDef"`
- `Period`: `"QuotaPeriodTypeDef"`
- `ErrorReason`: `"ErrorReasonTypeDef"`


## TagTypeDef

```python
from mypy_boto3_service_quotas.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## GetAWSDefaultServiceQuotaResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import GetAWSDefaultServiceQuotaResponseTypeDef
```




Optional fields:
- `Quota`: `"ServiceQuotaTypeDef"`


## GetAssociationForServiceQuotaTemplateResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import GetAssociationForServiceQuotaTemplateResponseTypeDef
```




Optional fields:
- `ServiceQuotaTemplateAssociationStatus`: `ServiceQuotaTemplateAssociationStatus`


## GetRequestedServiceQuotaChangeResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import GetRequestedServiceQuotaChangeResponseTypeDef
```




Optional fields:
- `RequestedQuota`: `"RequestedServiceQuotaChangeTypeDef"`


## GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef
```




Optional fields:
- `ServiceQuotaIncreaseRequestInTemplate`: `"ServiceQuotaIncreaseRequestInTemplateTypeDef"`


## GetServiceQuotaResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import GetServiceQuotaResponseTypeDef
```




Optional fields:
- `Quota`: `"ServiceQuotaTypeDef"`


## ListAWSDefaultServiceQuotasResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListAWSDefaultServiceQuotasResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Quotas`: `List["ServiceQuotaTypeDef"]`


## ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `RequestedQuotas`: `List["RequestedServiceQuotaChangeTypeDef"]`


## ListRequestedServiceQuotaChangeHistoryResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListRequestedServiceQuotaChangeHistoryResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `RequestedQuotas`: `List["RequestedServiceQuotaChangeTypeDef"]`


## ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef
```




Optional fields:
- `ServiceQuotaIncreaseRequestInTemplateList`: `List["ServiceQuotaIncreaseRequestInTemplateTypeDef"]`
- `NextToken`: `str`


## ListServiceQuotasResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListServiceQuotasResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Quotas`: `List["ServiceQuotaTypeDef"]`


## ListServicesResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListServicesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Services`: `List["ServiceInfoTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_service_quotas.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef
```




Optional fields:
- `ServiceQuotaIncreaseRequestInTemplate`: `"ServiceQuotaIncreaseRequestInTemplateTypeDef"`


## RequestServiceQuotaIncreaseResponseTypeDef

```python
from mypy_boto3_service_quotas.type_defs import RequestServiceQuotaIncreaseResponseTypeDef
```




Optional fields:
- `RequestedQuota`: `"RequestedServiceQuotaChangeTypeDef"`

