# Paginators for boto3 ApiGatewayV2 module

> [Index](../index.md) > [ApiGatewayV2](./index.md) > Paginators

Auto-generated documentation for [ApiGatewayV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2)
type annotations stubs module [mypy_boto3_apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/).

- [Paginators for boto3 ApiGatewayV2 module](#paginators-for-boto3-apigatewayv2-module)
  - [GetApisPaginator](#getapispaginator)
  - [GetAuthorizersPaginator](#getauthorizerspaginator)
  - [GetDeploymentsPaginator](#getdeploymentspaginator)
  - [GetDomainNamesPaginator](#getdomainnamespaginator)
  - [GetIntegrationResponsesPaginator](#getintegrationresponsespaginator)
  - [GetIntegrationsPaginator](#getintegrationspaginator)
  - [GetModelsPaginator](#getmodelspaginator)
  - [GetRouteResponsesPaginator](#getrouteresponsespaginator)
  - [GetRoutesPaginator](#getroutespaginator)
  - [GetStagesPaginator](#getstagespaginator)

## GetApisPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_apis")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetApisPaginator

def get_get_apis_paginator() -> GetApisPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_apis")
```

[Paginator.GetApis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis)

```python
class GetApisPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetApisResponseTypeDef]:
        pass
```
## GetAuthorizersPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_authorizers")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetAuthorizersPaginator

def get_get_authorizers_paginator() -> GetAuthorizersPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_authorizers")
```

[Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers)

```python
class GetAuthorizersPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAuthorizersResponseTypeDef]:
        pass
```
## GetDeploymentsPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_deployments")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetDeploymentsPaginator

def get_get_deployments_paginator() -> GetDeploymentsPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_deployments")
```

[Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments)

```python
class GetDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDeploymentsResponseTypeDef]:
        pass
```
## GetDomainNamesPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_domain_names")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetDomainNamesPaginator

def get_get_domain_names_paginator() -> GetDomainNamesPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_domain_names")
```

[Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames)

```python
class GetDomainNamesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDomainNamesResponseTypeDef]:
        pass
```
## GetIntegrationResponsesPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_integration_responses")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetIntegrationResponsesPaginator

def get_get_integration_responses_paginator() -> GetIntegrationResponsesPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_integration_responses")
```

[Paginator.GetIntegrationResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses)

```python
class GetIntegrationResponsesPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        IntegrationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntegrationResponsesResponseTypeDef]:
        pass
```
## GetIntegrationsPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_integrations")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetIntegrationsPaginator

def get_get_integrations_paginator() -> GetIntegrationsPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_integrations")
```

[Paginator.GetIntegrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations)

```python
class GetIntegrationsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIntegrationsResponseTypeDef]:
        pass
```
## GetModelsPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_models")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetModelsPaginator

def get_get_models_paginator() -> GetModelsPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_models")
```

[Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels)

```python
class GetModelsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetModelsResponseTypeDef]:
        pass
```
## GetRouteResponsesPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_route_responses")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetRouteResponsesPaginator

def get_get_route_responses_paginator() -> GetRouteResponsesPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_route_responses")
```

[Paginator.GetRouteResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses)

```python
class GetRouteResponsesPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        RouteId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRouteResponsesResponseTypeDef]:
        pass
```
## GetRoutesPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_routes")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetRoutesPaginator

def get_get_routes_paginator() -> GetRoutesPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_routes")
```

[Paginator.GetRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes)

```python
class GetRoutesPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRoutesResponseTypeDef]:
        pass
```
## GetStagesPaginator

Type annotations for `boto3.client("apigatewayv2").get_paginator("get_stages")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetStagesPaginator

def get_get_stages_paginator() -> GetStagesPaginator:
    return boto3.client("apigatewayv2").get_paginator("get_stages")
```

[Paginator.GetStages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages)

```python
class GetStagesPaginator(Boto3Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetStagesResponseTypeDef]:
        pass
```