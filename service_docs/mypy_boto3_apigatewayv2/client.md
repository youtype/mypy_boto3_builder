# ApiGatewayV2Client for boto3 ApiGatewayV2 module

> [Index](../index.md) > [ApiGatewayV2](./index.md) > ApiGatewayV2Client

Auto-generated documentation for [ApiGatewayV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2)
type annotations stubs module [mypy_boto3_apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/).

- [ApiGatewayV2Client for boto3 ApiGatewayV2 module](#apigatewayv2client-for-boto3-apigatewayv2-module)
  - [ApiGatewayV2Client](#apigatewayv2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_api](#create_api)
    - [create_api_mapping](#create_api_mapping)
    - [create_authorizer](#create_authorizer)
    - [create_deployment](#create_deployment)
    - [create_domain_name](#create_domain_name)
    - [create_integration](#create_integration)
    - [create_integration_response](#create_integration_response)
    - [create_model](#create_model)
    - [create_route](#create_route)
    - [create_route_response](#create_route_response)
    - [create_stage](#create_stage)
    - [create_vpc_link](#create_vpc_link)
    - [delete_access_log_settings](#delete_access_log_settings)
    - [delete_api](#delete_api)
    - [delete_api_mapping](#delete_api_mapping)
    - [delete_authorizer](#delete_authorizer)
    - [delete_cors_configuration](#delete_cors_configuration)
    - [delete_deployment](#delete_deployment)
    - [delete_domain_name](#delete_domain_name)
    - [delete_integration](#delete_integration)
    - [delete_integration_response](#delete_integration_response)
    - [delete_model](#delete_model)
    - [delete_route](#delete_route)
    - [delete_route_request_parameter](#delete_route_request_parameter)
    - [delete_route_response](#delete_route_response)
    - [delete_route_settings](#delete_route_settings)
    - [delete_stage](#delete_stage)
    - [delete_vpc_link](#delete_vpc_link)
    - [export_api](#export_api)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_api](#get_api)
    - [get_api_mapping](#get_api_mapping)
    - [get_api_mappings](#get_api_mappings)
    - [get_apis](#get_apis)
    - [get_authorizer](#get_authorizer)
    - [get_authorizers](#get_authorizers)
    - [get_deployment](#get_deployment)
    - [get_deployments](#get_deployments)
    - [get_domain_name](#get_domain_name)
    - [get_domain_names](#get_domain_names)
    - [get_integration](#get_integration)
    - [get_integration_response](#get_integration_response)
    - [get_integration_responses](#get_integration_responses)
    - [get_integrations](#get_integrations)
    - [get_model](#get_model)
    - [get_model_template](#get_model_template)
    - [get_models](#get_models)
    - [get_route](#get_route)
    - [get_route_response](#get_route_response)
    - [get_route_responses](#get_route_responses)
    - [get_routes](#get_routes)
    - [get_stage](#get_stage)
    - [get_stages](#get_stages)
    - [get_tags](#get_tags)
    - [get_vpc_link](#get_vpc_link)
    - [get_vpc_links](#get_vpc_links)
    - [import_api](#import_api)
    - [reimport_api](#reimport_api)
    - [reset_authorizers_cache](#reset_authorizers_cache)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_api](#update_api)
    - [update_api_mapping](#update_api_mapping)
    - [update_authorizer](#update_authorizer)
    - [update_deployment](#update_deployment)
    - [update_domain_name](#update_domain_name)
    - [update_integration](#update_integration)
    - [update_integration_response](#update_integration_response)
    - [update_model](#update_model)
    - [update_route](#update_route)
    - [update_route_response](#update_route_response)
    - [update_stage](#update_stage)
    - [update_vpc_link](#update_vpc_link)
    - [get_paginator](#get_paginator)

## ApiGatewayV2Client

Type annotations for `boto3.client("apigatewayv2")`

Can be used directly:

```python
from mypy_boto3_apigatewayv2.client import ApiGatewayV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_apigatewayv2.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("apigatewayv2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_api

Type annotations for `boto3.client("apigatewayv2").create_api` method.

[Client.create_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api)

```python
def create_api(
    self,
    Name: str,
    ProtocolType: ProtocolType,
    ApiKeySelectionExpression: str = None,
    CorsConfiguration: "CorsTypeDef" = None,
    CredentialsArn: str = None,
    Description: str = None,
    DisableSchemaValidation: bool = None,
    DisableExecuteApiEndpoint: bool = None,
    RouteKey: str = None,
    RouteSelectionExpression: str = None,
    Tags: Dict[str, str] = None,
    Target: str = None,
    Version: str = None
) -> CreateApiResponseTypeDef:
    pass
```

### create_api_mapping

Type annotations for `boto3.client("apigatewayv2").create_api_mapping` method.

[Client.create_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api_mapping)

```python
def create_api_mapping(
    self,
    ApiId: str,
    DomainName: str,
    Stage: str,
    ApiMappingKey: str = None
) -> CreateApiMappingResponseTypeDef:
    pass
```

### create_authorizer

Type annotations for `boto3.client("apigatewayv2").create_authorizer` method.

[Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_authorizer)

```python
def create_authorizer(
    self,
    ApiId: str,
    AuthorizerType: AuthorizerType,
    IdentitySource: List[str],
    Name: str,
    AuthorizerCredentialsArn: str = None,
    AuthorizerPayloadFormatVersion: str = None,
    AuthorizerResultTtlInSeconds: int = None,
    AuthorizerUri: str = None,
    EnableSimpleResponses: bool = None,
    IdentityValidationExpression: str = None,
    JwtConfiguration: "JWTConfigurationTypeDef" = None
) -> CreateAuthorizerResponseTypeDef:
    pass
```

### create_deployment

Type annotations for `boto3.client("apigatewayv2").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_deployment)

```python
def create_deployment(
    self,
    ApiId: str,
    Description: str = None,
    StageName: str = None
) -> CreateDeploymentResponseTypeDef:
    pass
```

### create_domain_name

Type annotations for `boto3.client("apigatewayv2").create_domain_name` method.

[Client.create_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_domain_name)

```python
def create_domain_name(
    self,
    DomainName: str,
    DomainNameConfigurations: List["DomainNameConfigurationTypeDef"] = None,
    MutualTlsAuthentication: MutualTlsAuthenticationInputTypeDef = None,
    Tags: Dict[str, str] = None
) -> CreateDomainNameResponseTypeDef:
    pass
```

### create_integration

Type annotations for `boto3.client("apigatewayv2").create_integration` method.

[Client.create_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_integration)

```python
def create_integration(
    self,
    ApiId: str,
    IntegrationType: IntegrationType,
    ConnectionId: str = None,
    ConnectionType: ConnectionType = None,
    ContentHandlingStrategy: ContentHandlingStrategy = None,
    CredentialsArn: str = None,
    Description: str = None,
    IntegrationMethod: str = None,
    IntegrationSubtype: str = None,
    IntegrationUri: str = None,
    PassthroughBehavior: PassthroughBehavior = None,
    PayloadFormatVersion: str = None,
    RequestParameters: Dict[str, str] = None,
    RequestTemplates: Dict[str, str] = None,
    ResponseParameters: Dict[str, Dict[str, str]] = None,
    TemplateSelectionExpression: str = None,
    TimeoutInMillis: int = None,
    TlsConfig: TlsConfigInputTypeDef = None
) -> CreateIntegrationResultTypeDef:
    pass
```

### create_integration_response

Type annotations for `boto3.client("apigatewayv2").create_integration_response` method.

[Client.create_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_integration_response)

```python
def create_integration_response(
    self,
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseKey: str,
    ContentHandlingStrategy: ContentHandlingStrategy = None,
    ResponseParameters: Dict[str, str] = None,
    ResponseTemplates: Dict[str, str] = None,
    TemplateSelectionExpression: str = None
) -> CreateIntegrationResponseResponseTypeDef:
    pass
```

### create_model

Type annotations for `boto3.client("apigatewayv2").create_model` method.

[Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_model)

```python
def create_model(
    self,
    ApiId: str,
    Name: str,
    Schema: str,
    ContentType: str = None,
    Description: str = None
) -> CreateModelResponseTypeDef:
    pass
```

### create_route

Type annotations for `boto3.client("apigatewayv2").create_route` method.

[Client.create_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_route)

```python
def create_route(
    self,
    ApiId: str,
    RouteKey: str,
    ApiKeyRequired: bool = None,
    AuthorizationScopes: List[str] = None,
    AuthorizationType: AuthorizationType = None,
    AuthorizerId: str = None,
    ModelSelectionExpression: str = None,
    OperationName: str = None,
    RequestModels: Dict[str, str] = None,
    RequestParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
    RouteResponseSelectionExpression: str = None,
    Target: str = None
) -> CreateRouteResultTypeDef:
    pass
```

### create_route_response

Type annotations for `boto3.client("apigatewayv2").create_route_response` method.

[Client.create_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_route_response)

```python
def create_route_response(
    self,
    ApiId: str,
    RouteId: str,
    RouteResponseKey: str,
    ModelSelectionExpression: str = None,
    ResponseModels: Dict[str, str] = None,
    ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"] = None
) -> CreateRouteResponseResponseTypeDef:
    pass
```

### create_stage

Type annotations for `boto3.client("apigatewayv2").create_stage` method.

[Client.create_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_stage)

```python
def create_stage(
    self,
    ApiId: str,
    StageName: str,
    AccessLogSettings: "AccessLogSettingsTypeDef" = None,
    AutoDeploy: bool = None,
    ClientCertificateId: str = None,
    DefaultRouteSettings: "RouteSettingsTypeDef" = None,
    DeploymentId: str = None,
    Description: str = None,
    RouteSettings: Dict[str, "RouteSettingsTypeDef"] = None,
    StageVariables: Dict[str, str] = None,
    Tags: Dict[str, str] = None
) -> CreateStageResponseTypeDef:
    pass
```

### create_vpc_link

Type annotations for `boto3.client("apigatewayv2").create_vpc_link` method.

[Client.create_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_vpc_link)

```python
def create_vpc_link(
    self,
    Name: str,
    SubnetIds: List[str],
    SecurityGroupIds: List[str] = None,
    Tags: Dict[str, str] = None
) -> CreateVpcLinkResponseTypeDef:
    pass
```

### delete_access_log_settings

Type annotations for `boto3.client("apigatewayv2").delete_access_log_settings` method.

[Client.delete_access_log_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_access_log_settings)

```python
def delete_access_log_settings(
    self,
    ApiId: str,
    StageName: str
) -> None:
    pass
```

### delete_api

Type annotations for `boto3.client("apigatewayv2").delete_api` method.

[Client.delete_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_api)

```python
def delete_api(
    self,
    ApiId: str
) -> None:
    pass
```

### delete_api_mapping

Type annotations for `boto3.client("apigatewayv2").delete_api_mapping` method.

[Client.delete_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_api_mapping)

```python
def delete_api_mapping(
    self,
    ApiMappingId: str,
    DomainName: str
) -> None:
    pass
```

### delete_authorizer

Type annotations for `boto3.client("apigatewayv2").delete_authorizer` method.

[Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_authorizer)

```python
def delete_authorizer(
    self,
    ApiId: str,
    AuthorizerId: str
) -> None:
    pass
```

### delete_cors_configuration

Type annotations for `boto3.client("apigatewayv2").delete_cors_configuration` method.

[Client.delete_cors_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_cors_configuration)

```python
def delete_cors_configuration(
    self,
    ApiId: str
) -> None:
    pass
```

### delete_deployment

Type annotations for `boto3.client("apigatewayv2").delete_deployment` method.

[Client.delete_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_deployment)

```python
def delete_deployment(
    self,
    ApiId: str,
    DeploymentId: str
) -> None:
    pass
```

### delete_domain_name

Type annotations for `boto3.client("apigatewayv2").delete_domain_name` method.

[Client.delete_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_domain_name)

```python
def delete_domain_name(
    self,
    DomainName: str
) -> None:
    pass
```

### delete_integration

Type annotations for `boto3.client("apigatewayv2").delete_integration` method.

[Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_integration)

```python
def delete_integration(
    self,
    ApiId: str,
    IntegrationId: str
) -> None:
    pass
```

### delete_integration_response

Type annotations for `boto3.client("apigatewayv2").delete_integration_response` method.

[Client.delete_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_integration_response)

```python
def delete_integration_response(
    self,
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseId: str
) -> None:
    pass
```

### delete_model

Type annotations for `boto3.client("apigatewayv2").delete_model` method.

[Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_model)

```python
def delete_model(
    self,
    ApiId: str,
    ModelId: str
) -> None:
    pass
```

### delete_route

Type annotations for `boto3.client("apigatewayv2").delete_route` method.

[Client.delete_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route)

```python
def delete_route(
    self,
    ApiId: str,
    RouteId: str
) -> None:
    pass
```

### delete_route_request_parameter

Type annotations for `boto3.client("apigatewayv2").delete_route_request_parameter` method.

[Client.delete_route_request_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_request_parameter)

```python
def delete_route_request_parameter(
    self,
    ApiId: str,
    RequestParameterKey: str,
    RouteId: str
) -> None:
    pass
```

### delete_route_response

Type annotations for `boto3.client("apigatewayv2").delete_route_response` method.

[Client.delete_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_response)

```python
def delete_route_response(
    self,
    ApiId: str,
    RouteId: str,
    RouteResponseId: str
) -> None:
    pass
```

### delete_route_settings

Type annotations for `boto3.client("apigatewayv2").delete_route_settings` method.

[Client.delete_route_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_settings)

```python
def delete_route_settings(
    self,
    ApiId: str,
    RouteKey: str,
    StageName: str
) -> None:
    pass
```

### delete_stage

Type annotations for `boto3.client("apigatewayv2").delete_stage` method.

[Client.delete_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_stage)

```python
def delete_stage(
    self,
    ApiId: str,
    StageName: str
) -> None:
    pass
```

### delete_vpc_link

Type annotations for `boto3.client("apigatewayv2").delete_vpc_link` method.

[Client.delete_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_vpc_link)

```python
def delete_vpc_link(
    self,
    VpcLinkId: str
) -> Dict[str, Any]:
    pass
```

### export_api

Type annotations for `boto3.client("apigatewayv2").export_api` method.

[Client.export_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.export_api)

```python
def export_api(
    self,
    ApiId: str,
    OutputType: JSONYAMLType,
    Specification: Literal['OAS30'],
    ExportVersion: str = None,
    IncludeExtensions: bool = None,
    StageName: str = None
) -> ExportApiResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("apigatewayv2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.generate_presigned_url)

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

### get_api

Type annotations for `boto3.client("apigatewayv2").get_api` method.

[Client.get_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api)

```python
def get_api(
    self,
    ApiId: str
) -> GetApiResponseTypeDef:
    pass
```

### get_api_mapping

Type annotations for `boto3.client("apigatewayv2").get_api_mapping` method.

[Client.get_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api_mapping)

```python
def get_api_mapping(
    self,
    ApiMappingId: str,
    DomainName: str
) -> GetApiMappingResponseTypeDef:
    pass
```

### get_api_mappings

Type annotations for `boto3.client("apigatewayv2").get_api_mappings` method.

[Client.get_api_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api_mappings)

```python
def get_api_mappings(
    self,
    DomainName: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetApiMappingsResponseTypeDef:
    pass
```

### get_apis

Type annotations for `boto3.client("apigatewayv2").get_apis` method.

[Client.get_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_apis)

```python
def get_apis(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> GetApisResponseTypeDef:
    pass
```

### get_authorizer

Type annotations for `boto3.client("apigatewayv2").get_authorizer` method.

[Client.get_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_authorizer)

```python
def get_authorizer(
    self,
    ApiId: str,
    AuthorizerId: str
) -> GetAuthorizerResponseTypeDef:
    pass
```

### get_authorizers

Type annotations for `boto3.client("apigatewayv2").get_authorizers` method.

[Client.get_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_authorizers)

```python
def get_authorizers(
    self,
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetAuthorizersResponseTypeDef:
    pass
```

### get_deployment

Type annotations for `boto3.client("apigatewayv2").get_deployment` method.

[Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_deployment)

```python
def get_deployment(
    self,
    ApiId: str,
    DeploymentId: str
) -> GetDeploymentResponseTypeDef:
    pass
```

### get_deployments

Type annotations for `boto3.client("apigatewayv2").get_deployments` method.

[Client.get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_deployments)

```python
def get_deployments(
    self,
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetDeploymentsResponseTypeDef:
    pass
```

### get_domain_name

Type annotations for `boto3.client("apigatewayv2").get_domain_name` method.

[Client.get_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_domain_name)

```python
def get_domain_name(
    self,
    DomainName: str
) -> GetDomainNameResponseTypeDef:
    pass
```

### get_domain_names

Type annotations for `boto3.client("apigatewayv2").get_domain_names` method.

[Client.get_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_domain_names)

```python
def get_domain_names(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> GetDomainNamesResponseTypeDef:
    pass
```

### get_integration

Type annotations for `boto3.client("apigatewayv2").get_integration` method.

[Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration)

```python
def get_integration(
    self,
    ApiId: str,
    IntegrationId: str
) -> GetIntegrationResultTypeDef:
    pass
```

### get_integration_response

Type annotations for `boto3.client("apigatewayv2").get_integration_response` method.

[Client.get_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration_response)

```python
def get_integration_response(
    self,
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseId: str
) -> GetIntegrationResponseResponseTypeDef:
    pass
```

### get_integration_responses

Type annotations for `boto3.client("apigatewayv2").get_integration_responses` method.

[Client.get_integration_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration_responses)

```python
def get_integration_responses(
    self,
    ApiId: str,
    IntegrationId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetIntegrationResponsesResponseTypeDef:
    pass
```

### get_integrations

Type annotations for `boto3.client("apigatewayv2").get_integrations` method.

[Client.get_integrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integrations)

```python
def get_integrations(
    self,
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetIntegrationsResponseTypeDef:
    pass
```

### get_model

Type annotations for `boto3.client("apigatewayv2").get_model` method.

[Client.get_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_model)

```python
def get_model(
    self,
    ApiId: str,
    ModelId: str
) -> GetModelResponseTypeDef:
    pass
```

### get_model_template

Type annotations for `boto3.client("apigatewayv2").get_model_template` method.

[Client.get_model_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_model_template)

```python
def get_model_template(
    self,
    ApiId: str,
    ModelId: str
) -> GetModelTemplateResponseTypeDef:
    pass
```

### get_models

Type annotations for `boto3.client("apigatewayv2").get_models` method.

[Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_models)

```python
def get_models(
    self,
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetModelsResponseTypeDef:
    pass
```

### get_route

Type annotations for `boto3.client("apigatewayv2").get_route` method.

[Client.get_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route)

```python
def get_route(
    self,
    ApiId: str,
    RouteId: str
) -> GetRouteResultTypeDef:
    pass
```

### get_route_response

Type annotations for `boto3.client("apigatewayv2").get_route_response` method.

[Client.get_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route_response)

```python
def get_route_response(
    self,
    ApiId: str,
    RouteId: str,
    RouteResponseId: str
) -> GetRouteResponseResponseTypeDef:
    pass
```

### get_route_responses

Type annotations for `boto3.client("apigatewayv2").get_route_responses` method.

[Client.get_route_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route_responses)

```python
def get_route_responses(
    self,
    ApiId: str,
    RouteId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetRouteResponsesResponseTypeDef:
    pass
```

### get_routes

Type annotations for `boto3.client("apigatewayv2").get_routes` method.

[Client.get_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_routes)

```python
def get_routes(
    self,
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetRoutesResponseTypeDef:
    pass
```

### get_stage

Type annotations for `boto3.client("apigatewayv2").get_stage` method.

[Client.get_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_stage)

```python
def get_stage(
    self,
    ApiId: str,
    StageName: str
) -> GetStageResponseTypeDef:
    pass
```

### get_stages

Type annotations for `boto3.client("apigatewayv2").get_stages` method.

[Client.get_stages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_stages)

```python
def get_stages(
    self,
    ApiId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> GetStagesResponseTypeDef:
    pass
```

### get_tags

Type annotations for `boto3.client("apigatewayv2").get_tags` method.

[Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_tags)

```python
def get_tags(
    self,
    ResourceArn: str
) -> GetTagsResponseTypeDef:
    pass
```

### get_vpc_link

Type annotations for `boto3.client("apigatewayv2").get_vpc_link` method.

[Client.get_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_vpc_link)

```python
def get_vpc_link(
    self,
    VpcLinkId: str
) -> GetVpcLinkResponseTypeDef:
    pass
```

### get_vpc_links

Type annotations for `boto3.client("apigatewayv2").get_vpc_links` method.

[Client.get_vpc_links documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_vpc_links)

```python
def get_vpc_links(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> GetVpcLinksResponseTypeDef:
    pass
```

### import_api

Type annotations for `boto3.client("apigatewayv2").import_api` method.

[Client.import_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.import_api)

```python
def import_api(
    self,
    Body: str,
    Basepath: str = None,
    FailOnWarnings: bool = None
) -> ImportApiResponseTypeDef:
    pass
```

### reimport_api

Type annotations for `boto3.client("apigatewayv2").reimport_api` method.

[Client.reimport_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.reimport_api)

```python
def reimport_api(
    self,
    ApiId: str,
    Body: str,
    Basepath: str = None,
    FailOnWarnings: bool = None
) -> ReimportApiResponseTypeDef:
    pass
```

### reset_authorizers_cache

Type annotations for `boto3.client("apigatewayv2").reset_authorizers_cache` method.

[Client.reset_authorizers_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.reset_authorizers_cache)

```python
def reset_authorizers_cache(
    self,
    ApiId: str,
    StageName: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("apigatewayv2").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("apigatewayv2").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_api

Type annotations for `boto3.client("apigatewayv2").update_api` method.

[Client.update_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_api)

```python
def update_api(
    self,
    ApiId: str,
    ApiKeySelectionExpression: str = None,
    CorsConfiguration: "CorsTypeDef" = None,
    CredentialsArn: str = None,
    Description: str = None,
    DisableSchemaValidation: bool = None,
    DisableExecuteApiEndpoint: bool = None,
    Name: str = None,
    RouteKey: str = None,
    RouteSelectionExpression: str = None,
    Target: str = None,
    Version: str = None
) -> UpdateApiResponseTypeDef:
    pass
```

### update_api_mapping

Type annotations for `boto3.client("apigatewayv2").update_api_mapping` method.

[Client.update_api_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_api_mapping)

```python
def update_api_mapping(
    self,
    ApiId: str,
    ApiMappingId: str,
    DomainName: str,
    ApiMappingKey: str = None,
    Stage: str = None
) -> UpdateApiMappingResponseTypeDef:
    pass
```

### update_authorizer

Type annotations for `boto3.client("apigatewayv2").update_authorizer` method.

[Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_authorizer)

```python
def update_authorizer(
    self,
    ApiId: str,
    AuthorizerId: str,
    AuthorizerCredentialsArn: str = None,
    AuthorizerPayloadFormatVersion: str = None,
    AuthorizerResultTtlInSeconds: int = None,
    AuthorizerType: AuthorizerType = None,
    AuthorizerUri: str = None,
    EnableSimpleResponses: bool = None,
    IdentitySource: List[str] = None,
    IdentityValidationExpression: str = None,
    JwtConfiguration: "JWTConfigurationTypeDef" = None,
    Name: str = None
) -> UpdateAuthorizerResponseTypeDef:
    pass
```

### update_deployment

Type annotations for `boto3.client("apigatewayv2").update_deployment` method.

[Client.update_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_deployment)

```python
def update_deployment(
    self,
    ApiId: str,
    DeploymentId: str,
    Description: str = None
) -> UpdateDeploymentResponseTypeDef:
    pass
```

### update_domain_name

Type annotations for `boto3.client("apigatewayv2").update_domain_name` method.

[Client.update_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_domain_name)

```python
def update_domain_name(
    self,
    DomainName: str,
    DomainNameConfigurations: List["DomainNameConfigurationTypeDef"] = None,
    MutualTlsAuthentication: MutualTlsAuthenticationInputTypeDef = None
) -> UpdateDomainNameResponseTypeDef:
    pass
```

### update_integration

Type annotations for `boto3.client("apigatewayv2").update_integration` method.

[Client.update_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_integration)

```python
def update_integration(
    self,
    ApiId: str,
    IntegrationId: str,
    ConnectionId: str = None,
    ConnectionType: ConnectionType = None,
    ContentHandlingStrategy: ContentHandlingStrategy = None,
    CredentialsArn: str = None,
    Description: str = None,
    IntegrationMethod: str = None,
    IntegrationSubtype: str = None,
    IntegrationType: IntegrationType = None,
    IntegrationUri: str = None,
    PassthroughBehavior: PassthroughBehavior = None,
    PayloadFormatVersion: str = None,
    RequestParameters: Dict[str, str] = None,
    RequestTemplates: Dict[str, str] = None,
    ResponseParameters: Dict[str, Dict[str, str]] = None,
    TemplateSelectionExpression: str = None,
    TimeoutInMillis: int = None,
    TlsConfig: TlsConfigInputTypeDef = None
) -> UpdateIntegrationResultTypeDef:
    pass
```

### update_integration_response

Type annotations for `boto3.client("apigatewayv2").update_integration_response` method.

[Client.update_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_integration_response)

```python
def update_integration_response(
    self,
    ApiId: str,
    IntegrationId: str,
    IntegrationResponseId: str,
    ContentHandlingStrategy: ContentHandlingStrategy = None,
    IntegrationResponseKey: str = None,
    ResponseParameters: Dict[str, str] = None,
    ResponseTemplates: Dict[str, str] = None,
    TemplateSelectionExpression: str = None
) -> UpdateIntegrationResponseResponseTypeDef:
    pass
```

### update_model

Type annotations for `boto3.client("apigatewayv2").update_model` method.

[Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_model)

```python
def update_model(
    self,
    ApiId: str,
    ModelId: str,
    ContentType: str = None,
    Description: str = None,
    Name: str = None,
    Schema: str = None
) -> UpdateModelResponseTypeDef:
    pass
```

### update_route

Type annotations for `boto3.client("apigatewayv2").update_route` method.

[Client.update_route documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_route)

```python
def update_route(
    self,
    ApiId: str,
    RouteId: str,
    ApiKeyRequired: bool = None,
    AuthorizationScopes: List[str] = None,
    AuthorizationType: AuthorizationType = None,
    AuthorizerId: str = None,
    ModelSelectionExpression: str = None,
    OperationName: str = None,
    RequestModels: Dict[str, str] = None,
    RequestParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
    RouteKey: str = None,
    RouteResponseSelectionExpression: str = None,
    Target: str = None
) -> UpdateRouteResultTypeDef:
    pass
```

### update_route_response

Type annotations for `boto3.client("apigatewayv2").update_route_response` method.

[Client.update_route_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_route_response)

```python
def update_route_response(
    self,
    ApiId: str,
    RouteId: str,
    RouteResponseId: str,
    ModelSelectionExpression: str = None,
    ResponseModels: Dict[str, str] = None,
    ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
    RouteResponseKey: str = None
) -> UpdateRouteResponseResponseTypeDef:
    pass
```

### update_stage

Type annotations for `boto3.client("apigatewayv2").update_stage` method.

[Client.update_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_stage)

```python
def update_stage(
    self,
    ApiId: str,
    StageName: str,
    AccessLogSettings: "AccessLogSettingsTypeDef" = None,
    AutoDeploy: bool = None,
    ClientCertificateId: str = None,
    DefaultRouteSettings: "RouteSettingsTypeDef" = None,
    DeploymentId: str = None,
    Description: str = None,
    RouteSettings: Dict[str, "RouteSettingsTypeDef"] = None,
    StageVariables: Dict[str, str] = None
) -> UpdateStageResponseTypeDef:
    pass
```

### update_vpc_link

Type annotations for `boto3.client("apigatewayv2").update_vpc_link` method.

[Client.update_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_vpc_link)

```python
def update_vpc_link(
    self,
    VpcLinkId: str,
    Name: str = None
) -> UpdateVpcLinkResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("apigatewayv2").get_paginator` method with overloads.

- `client.get_paginator("get_apis")` -> [GetApisPaginator](./paginators.md#getapispaginator)
- `client.get_paginator("get_authorizers")` -> [GetAuthorizersPaginator](./paginators.md#getauthorizerspaginator)
- `client.get_paginator("get_deployments")` -> [GetDeploymentsPaginator](./paginators.md#getdeploymentspaginator)
- `client.get_paginator("get_domain_names")` -> [GetDomainNamesPaginator](./paginators.md#getdomainnamespaginator)
- `client.get_paginator("get_integration_responses")` -> [GetIntegrationResponsesPaginator](./paginators.md#getintegrationresponsespaginator)
- `client.get_paginator("get_integrations")` -> [GetIntegrationsPaginator](./paginators.md#getintegrationspaginator)
- `client.get_paginator("get_models")` -> [GetModelsPaginator](./paginators.md#getmodelspaginator)
- `client.get_paginator("get_route_responses")` -> [GetRouteResponsesPaginator](./paginators.md#getrouteresponsespaginator)
- `client.get_paginator("get_routes")` -> [GetRoutesPaginator](./paginators.md#getroutespaginator)
- `client.get_paginator("get_stages")` -> [GetStagesPaginator](./paginators.md#getstagespaginator)


