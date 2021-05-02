# Paginators for boto3 APIGateway module

> [Index](../index.md) > [APIGateway](./index.md) > Paginators

Auto-generated documentation for [APIGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway)
type annotations stubs module [mypy_boto3_apigateway](https://pypi.org/project/mypy-boto3-apigateway/).

- [Paginators for boto3 APIGateway module](#paginators-for-boto3-apigateway-module)
  - [GetApiKeysPaginator](#getapikeyspaginator)
  - [GetAuthorizersPaginator](#getauthorizerspaginator)
  - [GetBasePathMappingsPaginator](#getbasepathmappingspaginator)
  - [GetClientCertificatesPaginator](#getclientcertificatespaginator)
  - [GetDeploymentsPaginator](#getdeploymentspaginator)
  - [GetDocumentationPartsPaginator](#getdocumentationpartspaginator)
  - [GetDocumentationVersionsPaginator](#getdocumentationversionspaginator)
  - [GetDomainNamesPaginator](#getdomainnamespaginator)
  - [GetGatewayResponsesPaginator](#getgatewayresponsespaginator)
  - [GetModelsPaginator](#getmodelspaginator)
  - [GetRequestValidatorsPaginator](#getrequestvalidatorspaginator)
  - [GetResourcesPaginator](#getresourcespaginator)
  - [GetRestApisPaginator](#getrestapispaginator)
  - [GetSdkTypesPaginator](#getsdktypespaginator)
  - [GetUsagePaginator](#getusagepaginator)
  - [GetUsagePlanKeysPaginator](#getusageplankeyspaginator)
  - [GetUsagePlansPaginator](#getusageplanspaginator)
  - [GetVpcLinksPaginator](#getvpclinkspaginator)

## GetApiKeysPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_api_keys")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetApiKeysPaginator

def get_get_api_keys_paginator() -> GetApiKeysPaginator:
    return boto3.client("apigateway").get_paginator("get_api_keys")
```

[Paginator.GetApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)

```python
class GetApiKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ApiKeysTypeDef]:
        pass
```
## GetAuthorizersPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_authorizers")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetAuthorizersPaginator

def get_get_authorizers_paginator() -> GetAuthorizersPaginator:
    return boto3.client("apigateway").get_paginator("get_authorizers")
```

[Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)

```python
class GetAuthorizersPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AuthorizersTypeDef]:
        pass
```
## GetBasePathMappingsPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_base_path_mappings")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetBasePathMappingsPaginator

def get_get_base_path_mappings_paginator() -> GetBasePathMappingsPaginator:
    return boto3.client("apigateway").get_paginator("get_base_path_mappings")
```

[Paginator.GetBasePathMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)

```python
class GetBasePathMappingsPaginator(Boto3Paginator):
    def paginate(
        self,
        domainName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[BasePathMappingsTypeDef]:
        pass
```
## GetClientCertificatesPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_client_certificates")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetClientCertificatesPaginator

def get_get_client_certificates_paginator() -> GetClientCertificatesPaginator:
    return boto3.client("apigateway").get_paginator("get_client_certificates")
```

[Paginator.GetClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)

```python
class GetClientCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClientCertificatesTypeDef]:
        pass
```
## GetDeploymentsPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_deployments")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetDeploymentsPaginator

def get_get_deployments_paginator() -> GetDeploymentsPaginator:
    return boto3.client("apigateway").get_paginator("get_deployments")
```

[Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)

```python
class GetDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DeploymentsTypeDef]:
        pass
```
## GetDocumentationPartsPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_documentation_parts")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetDocumentationPartsPaginator

def get_get_documentation_parts_paginator() -> GetDocumentationPartsPaginator:
    return boto3.client("apigateway").get_paginator("get_documentation_parts")
```

[Paginator.GetDocumentationParts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)

```python
class GetDocumentationPartsPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        type: DocumentationPartType = None,
        nameQuery: str = None,
        path: str = None,
        locationStatus: LocationStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DocumentationPartsTypeDef]:
        pass
```
## GetDocumentationVersionsPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_documentation_versions")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetDocumentationVersionsPaginator

def get_get_documentation_versions_paginator() -> GetDocumentationVersionsPaginator:
    return boto3.client("apigateway").get_paginator("get_documentation_versions")
```

[Paginator.GetDocumentationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)

```python
class GetDocumentationVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DocumentationVersionsTypeDef]:
        pass
```
## GetDomainNamesPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_domain_names")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetDomainNamesPaginator

def get_get_domain_names_paginator() -> GetDomainNamesPaginator:
    return boto3.client("apigateway").get_paginator("get_domain_names")
```

[Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)

```python
class GetDomainNamesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DomainNamesTypeDef]:
        pass
```
## GetGatewayResponsesPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_gateway_responses")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetGatewayResponsesPaginator

def get_get_gateway_responses_paginator() -> GetGatewayResponsesPaginator:
    return boto3.client("apigateway").get_paginator("get_gateway_responses")
```

[Paginator.GetGatewayResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)

```python
class GetGatewayResponsesPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GatewayResponsesTypeDef]:
        pass
```
## GetModelsPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_models")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetModelsPaginator

def get_get_models_paginator() -> GetModelsPaginator:
    return boto3.client("apigateway").get_paginator("get_models")
```

[Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetModels)

```python
class GetModelsPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ModelsTypeDef]:
        pass
```
## GetRequestValidatorsPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_request_validators")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetRequestValidatorsPaginator

def get_get_request_validators_paginator() -> GetRequestValidatorsPaginator:
    return boto3.client("apigateway").get_paginator("get_request_validators")
```

[Paginator.GetRequestValidators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)

```python
class GetRequestValidatorsPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[RequestValidatorsTypeDef]:
        pass
```
## GetResourcesPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_resources")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetResourcesPaginator

def get_get_resources_paginator() -> GetResourcesPaginator:
    return boto3.client("apigateway").get_paginator("get_resources")
```

[Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetResources)

```python
class GetResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        restApiId: str,
        embed: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ResourcesTypeDef]:
        pass
```
## GetRestApisPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_rest_apis")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetRestApisPaginator

def get_get_rest_apis_paginator() -> GetRestApisPaginator:
    return boto3.client("apigateway").get_paginator("get_rest_apis")
```

[Paginator.GetRestApis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)

```python
class GetRestApisPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[RestApisTypeDef]:
        pass
```
## GetSdkTypesPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_sdk_types")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetSdkTypesPaginator

def get_get_sdk_types_paginator() -> GetSdkTypesPaginator:
    return boto3.client("apigateway").get_paginator("get_sdk_types")
```

[Paginator.GetSdkTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)

```python
class GetSdkTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SdkTypesTypeDef]:
        pass
```
## GetUsagePaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_usage")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetUsagePaginator

def get_get_usage_paginator() -> GetUsagePaginator:
    return boto3.client("apigateway").get_paginator("get_usage")
```

[Paginator.GetUsage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)

```python
class GetUsagePaginator(Boto3Paginator):
    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UsageTypeDef]:
        pass
```
## GetUsagePlanKeysPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_usage_plan_keys")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetUsagePlanKeysPaginator

def get_get_usage_plan_keys_paginator() -> GetUsagePlanKeysPaginator:
    return boto3.client("apigateway").get_paginator("get_usage_plan_keys")
```

[Paginator.GetUsagePlanKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)

```python
class GetUsagePlanKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        usagePlanId: str,
        nameQuery: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UsagePlanKeysTypeDef]:
        pass
```
## GetUsagePlansPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_usage_plans")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetUsagePlansPaginator

def get_get_usage_plans_paginator() -> GetUsagePlansPaginator:
    return boto3.client("apigateway").get_paginator("get_usage_plans")
```

[Paginator.GetUsagePlans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)

```python
class GetUsagePlansPaginator(Boto3Paginator):
    def paginate(
        self,
        keyId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UsagePlansTypeDef]:
        pass
```
## GetVpcLinksPaginator

Type annotations for `boto3.client("apigateway").get_paginator("get_vpc_links")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetVpcLinksPaginator

def get_get_vpc_links_paginator() -> GetVpcLinksPaginator:
    return boto3.client("apigateway").get_paginator("get_vpc_links")
```

[Paginator.GetVpcLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)

```python
class GetVpcLinksPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[VpcLinksTypeDef]:
        pass
```