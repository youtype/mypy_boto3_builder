# Type annotations for boto3 ServiceQuotas module

> [Index](../index.md) > ServiceQuotas

Auto-generated documentation for [ServiceQuotas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas)
type annotations stubs module [mypy_boto3_service_quotas](https://pypi.org/project/mypy-boto3-service-quotas/).

```bash
pip install mypy-boto3-service-quotas
```

- [Type annotations for boto3 ServiceQuotas module](#type-annotations-for-boto3-servicequotas-module)
  - [ServiceQuotasClient](#servicequotasclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ServiceQuotasClient

Type annotations for  `boto3.client("service-quotas")` as [ServiceQuotasClient](./client.md)

Can be used directly:

```python
from mypy_boto3_service_quotas.client import ServiceQuotasClient
```


ServiceQuotasClient [exceptions](./client.md#exceptions)



### Methods
- [associate_service_quota_template](./client.md#associate-service-quota-template)
- [can_paginate](./client.md#can-paginate)
- [delete_service_quota_increase_request_from_template](./client.md#delete-service-quota-increase-request-from-template)
- [disassociate_service_quota_template](./client.md#disassociate-service-quota-template)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_association_for_service_quota_template](./client.md#get-association-for-service-quota-template)
- [get_aws_default_service_quota](./client.md#get-aws-default-service-quota)
- [get_paginator](./client.md#get-paginator)
- [get_requested_service_quota_change](./client.md#get-requested-service-quota-change)
- [get_service_quota](./client.md#get-service-quota)
- [get_service_quota_increase_request_from_template](./client.md#get-service-quota-increase-request-from-template)
- [list_aws_default_service_quotas](./client.md#list-aws-default-service-quotas)
- [list_requested_service_quota_change_history](./client.md#list-requested-service-quota-change-history)
- [list_requested_service_quota_change_history_by_quota](./client.md#list-requested-service-quota-change-history-by-quota)
- [list_service_quota_increase_requests_in_template](./client.md#list-service-quota-increase-requests-in-template)
- [list_service_quotas](./client.md#list-service-quotas)
- [list_services](./client.md#list-services)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_service_quota_increase_request_into_template](./client.md#put-service-quota-increase-request-into-template)
- [request_service_quota_increase](./client.md#request-service-quota-increase)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AWSServiceAccessNotEnabledException](./client.md#awsserviceaccessnotenabledexception)
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [DependencyAccessDeniedException](./client.md#dependencyaccessdeniedexception)
- [IllegalArgumentException](./client.md#illegalargumentexception)
- [InvalidPaginationTokenException](./client.md#invalidpaginationtokenexception)
- [InvalidResourceStateException](./client.md#invalidresourcestateexception)
- [NoAvailableOrganizationException](./client.md#noavailableorganizationexception)
- [NoSuchResourceException](./client.md#nosuchresourceexception)
- [OrganizationNotInAllFeaturesModeException](./client.md#organizationnotinallfeaturesmodeexception)
- [QuotaExceededException](./client.md#quotaexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ServiceException](./client.md#serviceexception)
- [ServiceQuotaTemplateNotInUseException](./client.md#servicequotatemplatenotinuseexception)
- [TagPolicyViolationException](./client.md#tagpolicyviolationexception)
- [TemplatesNotAvailableInRegionException](./client.md#templatesnotavailableinregionexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("service-quotas").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_service_quotas.paginators import ListAWSDefaultServiceQuotasPaginator, ...
```

- [ListAWSDefaultServiceQuotasPaginator](./paginators.md#listawsdefaultservicequotaspaginator)
- [ListRequestedServiceQuotaChangeHistoryPaginator](./paginators.md#listrequestedservicequotachangehistorypaginator)
- [ListRequestedServiceQuotaChangeHistoryByQuotaPaginator](./paginators.md#listrequestedservicequotachangehistorybyquotapaginator)
- [ListServiceQuotaIncreaseRequestsInTemplatePaginator](./paginators.md#listservicequotaincreaserequestsintemplatepaginator)
- [ListServiceQuotasPaginator](./paginators.md#listservicequotaspaginator)
- [ListServicesPaginator](./paginators.md#listservicespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_service_quotas.literals import ErrorCode, ...
```

- [ErrorCode](./literals.md#errorcode)
- [ListAWSDefaultServiceQuotasPaginatorName](./literals.md#listawsdefaultservicequotaspaginatorname)
- [ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName](./literals.md#listrequestedservicequotachangehistorybyquotapaginatorname)
- [ListRequestedServiceQuotaChangeHistoryPaginatorName](./literals.md#listrequestedservicequotachangehistorypaginatorname)
- [ListServiceQuotaIncreaseRequestsInTemplatePaginatorName](./literals.md#listservicequotaincreaserequestsintemplatepaginatorname)
- [ListServiceQuotasPaginatorName](./literals.md#listservicequotaspaginatorname)
- [ListServicesPaginatorName](./literals.md#listservicespaginatorname)
- [PeriodUnit](./literals.md#periodunit)
- [RequestStatus](./literals.md#requeststatus)
- [ServiceQuotaTemplateAssociationStatus](./literals.md#servicequotatemplateassociationstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_service_quotas.type_defs import ErrorReasonTypeDef, ...
```

- [ErrorReasonTypeDef](./type_defs.md#errorreasontypedef)
- [MetricInfoTypeDef](./type_defs.md#metricinfotypedef)
- [QuotaPeriodTypeDef](./type_defs.md#quotaperiodtypedef)
- [RequestedServiceQuotaChangeTypeDef](./type_defs.md#requestedservicequotachangetypedef)
- [ServiceInfoTypeDef](./type_defs.md#serviceinfotypedef)
- [ServiceQuotaIncreaseRequestInTemplateTypeDef](./type_defs.md#servicequotaincreaserequestintemplatetypedef)
- [ServiceQuotaTypeDef](./type_defs.md#servicequotatypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [GetAWSDefaultServiceQuotaResponseTypeDef](./type_defs.md#getawsdefaultservicequotaresponsetypedef)
- [GetAssociationForServiceQuotaTemplateResponseTypeDef](./type_defs.md#getassociationforservicequotatemplateresponsetypedef)
- [GetRequestedServiceQuotaChangeResponseTypeDef](./type_defs.md#getrequestedservicequotachangeresponsetypedef)
- [GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef](./type_defs.md#getservicequotaincreaserequestfromtemplateresponsetypedef)
- [GetServiceQuotaResponseTypeDef](./type_defs.md#getservicequotaresponsetypedef)
- [ListAWSDefaultServiceQuotasResponseTypeDef](./type_defs.md#listawsdefaultservicequotasresponsetypedef)
- [ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef](./type_defs.md#listrequestedservicequotachangehistorybyquotaresponsetypedef)
- [ListRequestedServiceQuotaChangeHistoryResponseTypeDef](./type_defs.md#listrequestedservicequotachangehistoryresponsetypedef)
- [ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef](./type_defs.md#listservicequotaincreaserequestsintemplateresponsetypedef)
- [ListServiceQuotasResponseTypeDef](./type_defs.md#listservicequotasresponsetypedef)
- [ListServicesResponseTypeDef](./type_defs.md#listservicesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef](./type_defs.md#putservicequotaincreaserequestintotemplateresponsetypedef)
- [RequestServiceQuotaIncreaseResponseTypeDef](./type_defs.md#requestservicequotaincreaseresponsetypedef)
