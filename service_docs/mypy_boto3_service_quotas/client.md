# ServiceQuotasClient for boto3 ServiceQuotas module

> [Index](../index.md) > [ServiceQuotas](./index.md) > ServiceQuotasClient

Auto-generated documentation for [ServiceQuotas](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas)
type annotations stubs module [mypy_boto3_service_quotas](https://pypi.org/project/mypy-boto3-service-quotas/).

- [ServiceQuotasClient for boto3 ServiceQuotas module](#servicequotasclient-for-boto3-servicequotas-module)
  - [ServiceQuotasClient](#servicequotasclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_service_quota_template](#associate_service_quota_template)
    - [can_paginate](#can_paginate)
    - [delete_service_quota_increase_request_from_template](#delete_service_quota_increase_request_from_template)
    - [disassociate_service_quota_template](#disassociate_service_quota_template)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_association_for_service_quota_template](#get_association_for_service_quota_template)
    - [get_aws_default_service_quota](#get_aws_default_service_quota)
    - [get_requested_service_quota_change](#get_requested_service_quota_change)
    - [get_service_quota](#get_service_quota)
    - [get_service_quota_increase_request_from_template](#get_service_quota_increase_request_from_template)
    - [list_aws_default_service_quotas](#list_aws_default_service_quotas)
    - [list_requested_service_quota_change_history](#list_requested_service_quota_change_history)
    - [list_requested_service_quota_change_history_by_quota](#list_requested_service_quota_change_history_by_quota)
    - [list_service_quota_increase_requests_in_template](#list_service_quota_increase_requests_in_template)
    - [list_service_quotas](#list_service_quotas)
    - [list_services](#list_services)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_service_quota_increase_request_into_template](#put_service_quota_increase_request_into_template)
    - [request_service_quota_increase](#request_service_quota_increase)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)

## ServiceQuotasClient

Type annotations for `boto3.client("service-quotas")`

Can be used directly:

```python
from mypy_boto3_service_quotas.client import ServiceQuotasClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_service_quotas.client import Exceptions

def handle_error(exc: Exceptions.AWSServiceAccessNotEnabledException) -> None:
    ...
```


Exceptions:

- `Exceptions.AWSServiceAccessNotEnabledException`
- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.DependencyAccessDeniedException`
- `Exceptions.IllegalArgumentException`
- `Exceptions.InvalidPaginationTokenException`
- `Exceptions.InvalidResourceStateException`
- `Exceptions.NoAvailableOrganizationException`
- `Exceptions.NoSuchResourceException`
- `Exceptions.OrganizationNotInAllFeaturesModeException`
- `Exceptions.QuotaExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ServiceException`
- `Exceptions.ServiceQuotaTemplateNotInUseException`
- `Exceptions.TagPolicyViolationException`
- `Exceptions.TemplatesNotAvailableInRegionException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.TooManyTagsException`


## Methods


### associate_service_quota_template

Type annotations for `boto3.client("service-quotas").associate_service_quota_template` method.

[Client.associate_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.associate_service_quota_template)

```python
def associate_service_quota_template(
    self
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("service-quotas").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_service_quota_increase_request_from_template

Type annotations for `boto3.client("service-quotas").delete_service_quota_increase_request_from_template` method.

[Client.delete_service_quota_increase_request_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.delete_service_quota_increase_request_from_template)

```python
def delete_service_quota_increase_request_from_template(
    self,
    ServiceCode: str,
    QuotaCode: str,
    AwsRegion: str
) -> Dict[str, Any]:
    pass
```

### disassociate_service_quota_template

Type annotations for `boto3.client("service-quotas").disassociate_service_quota_template` method.

[Client.disassociate_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.disassociate_service_quota_template)

```python
def disassociate_service_quota_template(
    self
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("service-quotas").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.generate_presigned_url)

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

### get_association_for_service_quota_template

Type annotations for `boto3.client("service-quotas").get_association_for_service_quota_template` method.

[Client.get_association_for_service_quota_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.get_association_for_service_quota_template)

```python
def get_association_for_service_quota_template(
    self
) -> GetAssociationForServiceQuotaTemplateResponseTypeDef:
    pass
```

### get_aws_default_service_quota

Type annotations for `boto3.client("service-quotas").get_aws_default_service_quota` method.

[Client.get_aws_default_service_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.get_aws_default_service_quota)

```python
def get_aws_default_service_quota(
    self,
    ServiceCode: str,
    QuotaCode: str
) -> GetAWSDefaultServiceQuotaResponseTypeDef:
    pass
```

### get_requested_service_quota_change

Type annotations for `boto3.client("service-quotas").get_requested_service_quota_change` method.

[Client.get_requested_service_quota_change documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.get_requested_service_quota_change)

```python
def get_requested_service_quota_change(
    self,
    RequestId: str
) -> GetRequestedServiceQuotaChangeResponseTypeDef:
    pass
```

### get_service_quota

Type annotations for `boto3.client("service-quotas").get_service_quota` method.

[Client.get_service_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota)

```python
def get_service_quota(
    self,
    ServiceCode: str,
    QuotaCode: str
) -> GetServiceQuotaResponseTypeDef:
    pass
```

### get_service_quota_increase_request_from_template

Type annotations for `boto3.client("service-quotas").get_service_quota_increase_request_from_template` method.

[Client.get_service_quota_increase_request_from_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota_increase_request_from_template)

```python
def get_service_quota_increase_request_from_template(
    self,
    ServiceCode: str,
    QuotaCode: str,
    AwsRegion: str
) -> GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
    pass
```

### list_aws_default_service_quotas

Type annotations for `boto3.client("service-quotas").list_aws_default_service_quotas` method.

[Client.list_aws_default_service_quotas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_aws_default_service_quotas)

```python
def list_aws_default_service_quotas(
    self,
    ServiceCode: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAWSDefaultServiceQuotasResponseTypeDef:
    pass
```

### list_requested_service_quota_change_history

Type annotations for `boto3.client("service-quotas").list_requested_service_quota_change_history` method.

[Client.list_requested_service_quota_change_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history)

```python
def list_requested_service_quota_change_history(
    self,
    ServiceCode: str = None,
    Status: RequestStatus = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRequestedServiceQuotaChangeHistoryResponseTypeDef:
    pass
```

### list_requested_service_quota_change_history_by_quota

Type annotations for `boto3.client("service-quotas").list_requested_service_quota_change_history_by_quota` method.

[Client.list_requested_service_quota_change_history_by_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history_by_quota)

```python
def list_requested_service_quota_change_history_by_quota(
    self,
    ServiceCode: str,
    QuotaCode: str,
    Status: RequestStatus = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
    pass
```

### list_service_quota_increase_requests_in_template

Type annotations for `boto3.client("service-quotas").list_service_quota_increase_requests_in_template` method.

[Client.list_service_quota_increase_requests_in_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quota_increase_requests_in_template)

```python
def list_service_quota_increase_requests_in_template(
    self,
    ServiceCode: str = None,
    AwsRegion: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
    pass
```

### list_service_quotas

Type annotations for `boto3.client("service-quotas").list_service_quotas` method.

[Client.list_service_quotas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quotas)

```python
def list_service_quotas(
    self,
    ServiceCode: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListServiceQuotasResponseTypeDef:
    pass
```

### list_services

Type annotations for `boto3.client("service-quotas").list_services` method.

[Client.list_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_services)

```python
def list_services(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListServicesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("service-quotas").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_service_quota_increase_request_into_template

Type annotations for `boto3.client("service-quotas").put_service_quota_increase_request_into_template` method.

[Client.put_service_quota_increase_request_into_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.put_service_quota_increase_request_into_template)

```python
def put_service_quota_increase_request_into_template(
    self,
    QuotaCode: str,
    ServiceCode: str,
    AwsRegion: str,
    DesiredValue: float
) -> PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
    pass
```

### request_service_quota_increase

Type annotations for `boto3.client("service-quotas").request_service_quota_increase` method.

[Client.request_service_quota_increase documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.request_service_quota_increase)

```python
def request_service_quota_increase(
    self,
    ServiceCode: str,
    QuotaCode: str,
    DesiredValue: float
) -> RequestServiceQuotaIncreaseResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("service-quotas").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("service-quotas").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html#ServiceQuotas.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("service-quotas").get_paginator` method with overloads.

- `client.get_paginator("list_aws_default_service_quotas")` -> [ListAWSDefaultServiceQuotasPaginator](./paginators.md#listawsdefaultservicequotaspaginator)
- `client.get_paginator("list_requested_service_quota_change_history")` -> [ListRequestedServiceQuotaChangeHistoryPaginator](./paginators.md#listrequestedservicequotachangehistorypaginator)
- `client.get_paginator("list_requested_service_quota_change_history_by_quota")` -> [ListRequestedServiceQuotaChangeHistoryByQuotaPaginator](./paginators.md#listrequestedservicequotachangehistorybyquotapaginator)
- `client.get_paginator("list_service_quota_increase_requests_in_template")` -> [ListServiceQuotaIncreaseRequestsInTemplatePaginator](./paginators.md#listservicequotaincreaserequestsintemplatepaginator)
- `client.get_paginator("list_service_quotas")` -> [ListServiceQuotasPaginator](./paginators.md#listservicequotaspaginator)
- `client.get_paginator("list_services")` -> [ListServicesPaginator](./paginators.md#listservicespaginator)


