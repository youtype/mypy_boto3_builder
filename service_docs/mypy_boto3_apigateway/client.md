# APIGatewayClient for boto3 APIGateway module

> [Index](../index.md) > [APIGateway](./index.md) > APIGatewayClient

Auto-generated documentation for [APIGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway)
type annotations stubs module [mypy_boto3_apigateway](https://pypi.org/project/mypy-boto3-apigateway/).

- [APIGatewayClient for boto3 APIGateway module](#apigatewayclient-for-boto3-apigateway-module)
  - [APIGatewayClient](#apigatewayclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_api_key](#create_api_key)
    - [create_authorizer](#create_authorizer)
    - [create_base_path_mapping](#create_base_path_mapping)
    - [create_deployment](#create_deployment)
    - [create_documentation_part](#create_documentation_part)
    - [create_documentation_version](#create_documentation_version)
    - [create_domain_name](#create_domain_name)
    - [create_model](#create_model)
    - [create_request_validator](#create_request_validator)
    - [create_resource](#create_resource)
    - [create_rest_api](#create_rest_api)
    - [create_stage](#create_stage)
    - [create_usage_plan](#create_usage_plan)
    - [create_usage_plan_key](#create_usage_plan_key)
    - [create_vpc_link](#create_vpc_link)
    - [delete_api_key](#delete_api_key)
    - [delete_authorizer](#delete_authorizer)
    - [delete_base_path_mapping](#delete_base_path_mapping)
    - [delete_client_certificate](#delete_client_certificate)
    - [delete_deployment](#delete_deployment)
    - [delete_documentation_part](#delete_documentation_part)
    - [delete_documentation_version](#delete_documentation_version)
    - [delete_domain_name](#delete_domain_name)
    - [delete_gateway_response](#delete_gateway_response)
    - [delete_integration](#delete_integration)
    - [delete_integration_response](#delete_integration_response)
    - [delete_method](#delete_method)
    - [delete_method_response](#delete_method_response)
    - [delete_model](#delete_model)
    - [delete_request_validator](#delete_request_validator)
    - [delete_resource](#delete_resource)
    - [delete_rest_api](#delete_rest_api)
    - [delete_stage](#delete_stage)
    - [delete_usage_plan](#delete_usage_plan)
    - [delete_usage_plan_key](#delete_usage_plan_key)
    - [delete_vpc_link](#delete_vpc_link)
    - [flush_stage_authorizers_cache](#flush_stage_authorizers_cache)
    - [flush_stage_cache](#flush_stage_cache)
    - [generate_client_certificate](#generate_client_certificate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account](#get_account)
    - [get_api_key](#get_api_key)
    - [get_api_keys](#get_api_keys)
    - [get_authorizer](#get_authorizer)
    - [get_authorizers](#get_authorizers)
    - [get_base_path_mapping](#get_base_path_mapping)
    - [get_base_path_mappings](#get_base_path_mappings)
    - [get_client_certificate](#get_client_certificate)
    - [get_client_certificates](#get_client_certificates)
    - [get_deployment](#get_deployment)
    - [get_deployments](#get_deployments)
    - [get_documentation_part](#get_documentation_part)
    - [get_documentation_parts](#get_documentation_parts)
    - [get_documentation_version](#get_documentation_version)
    - [get_documentation_versions](#get_documentation_versions)
    - [get_domain_name](#get_domain_name)
    - [get_domain_names](#get_domain_names)
    - [get_export](#get_export)
    - [get_gateway_response](#get_gateway_response)
    - [get_gateway_responses](#get_gateway_responses)
    - [get_integration](#get_integration)
    - [get_integration_response](#get_integration_response)
    - [get_method](#get_method)
    - [get_method_response](#get_method_response)
    - [get_model](#get_model)
    - [get_model_template](#get_model_template)
    - [get_models](#get_models)
    - [get_request_validator](#get_request_validator)
    - [get_request_validators](#get_request_validators)
    - [get_resource](#get_resource)
    - [get_resources](#get_resources)
    - [get_rest_api](#get_rest_api)
    - [get_rest_apis](#get_rest_apis)
    - [get_sdk](#get_sdk)
    - [get_sdk_type](#get_sdk_type)
    - [get_sdk_types](#get_sdk_types)
    - [get_stage](#get_stage)
    - [get_stages](#get_stages)
    - [get_tags](#get_tags)
    - [get_usage](#get_usage)
    - [get_usage_plan](#get_usage_plan)
    - [get_usage_plan_key](#get_usage_plan_key)
    - [get_usage_plan_keys](#get_usage_plan_keys)
    - [get_usage_plans](#get_usage_plans)
    - [get_vpc_link](#get_vpc_link)
    - [get_vpc_links](#get_vpc_links)
    - [import_api_keys](#import_api_keys)
    - [import_documentation_parts](#import_documentation_parts)
    - [import_rest_api](#import_rest_api)
    - [put_gateway_response](#put_gateway_response)
    - [put_integration](#put_integration)
    - [put_integration_response](#put_integration_response)
    - [put_method](#put_method)
    - [put_method_response](#put_method_response)
    - [put_rest_api](#put_rest_api)
    - [tag_resource](#tag_resource)
    - [test_invoke_authorizer](#test_invoke_authorizer)
    - [test_invoke_method](#test_invoke_method)
    - [untag_resource](#untag_resource)
    - [update_account](#update_account)
    - [update_api_key](#update_api_key)
    - [update_authorizer](#update_authorizer)
    - [update_base_path_mapping](#update_base_path_mapping)
    - [update_client_certificate](#update_client_certificate)
    - [update_deployment](#update_deployment)
    - [update_documentation_part](#update_documentation_part)
    - [update_documentation_version](#update_documentation_version)
    - [update_domain_name](#update_domain_name)
    - [update_gateway_response](#update_gateway_response)
    - [update_integration](#update_integration)
    - [update_integration_response](#update_integration_response)
    - [update_method](#update_method)
    - [update_method_response](#update_method_response)
    - [update_model](#update_model)
    - [update_request_validator](#update_request_validator)
    - [update_resource](#update_resource)
    - [update_rest_api](#update_rest_api)
    - [update_stage](#update_stage)
    - [update_usage](#update_usage)
    - [update_usage_plan](#update_usage_plan)
    - [update_vpc_link](#update_vpc_link)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)

## APIGatewayClient

Type annotations for `boto3.client("apigateway")`

Can be used directly:

```python
from mypy_boto3_apigateway.client import APIGatewayClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_apigateway.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("apigateway").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_api_key

Type annotations for `boto3.client("apigateway").create_api_key` method.

[Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_api_key)

```python
def create_api_key(
    self,
    name: str = None,
    description: str = None,
    enabled: bool = None,
    generateDistinctId: bool = None,
    value: str = None,
    stageKeys: List[StageKeyTypeDef] = None,
    customerId: str = None,
    tags: Dict[str, str] = None
) -> "ApiKeyTypeDef":
    pass
```

### create_authorizer

Type annotations for `boto3.client("apigateway").create_authorizer` method.

[Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_authorizer)

```python
def create_authorizer(
    self,
    restApiId: str,
    name: str,
    type: AuthorizerType,
    providerARNs: List[str] = None,
    authType: str = None,
    authorizerUri: str = None,
    authorizerCredentials: str = None,
    identitySource: str = None,
    identityValidationExpression: str = None,
    authorizerResultTtlInSeconds: int = None
) -> "AuthorizerTypeDef":
    pass
```

### create_base_path_mapping

Type annotations for `boto3.client("apigateway").create_base_path_mapping` method.

[Client.create_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_base_path_mapping)

```python
def create_base_path_mapping(
    self,
    domainName: str,
    restApiId: str,
    basePath: str = None,
    stage: str = None
) -> "BasePathMappingTypeDef":
    pass
```

### create_deployment

Type annotations for `boto3.client("apigateway").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_deployment)

```python
def create_deployment(
    self,
    restApiId: str,
    stageName: str = None,
    stageDescription: str = None,
    description: str = None,
    cacheClusterEnabled: bool = None,
    cacheClusterSize: CacheClusterSize = None,
    variables: Dict[str, str] = None,
    canarySettings: DeploymentCanarySettingsTypeDef = None,
    tracingEnabled: bool = None
) -> "DeploymentTypeDef":
    pass
```

### create_documentation_part

Type annotations for `boto3.client("apigateway").create_documentation_part` method.

[Client.create_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_documentation_part)

```python
def create_documentation_part(
    self,
    restApiId: str,
    location: "DocumentationPartLocationTypeDef",
    properties: str
) -> "DocumentationPartTypeDef":
    pass
```

### create_documentation_version

Type annotations for `boto3.client("apigateway").create_documentation_version` method.

[Client.create_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_documentation_version)

```python
def create_documentation_version(
    self,
    restApiId: str,
    documentationVersion: str,
    stageName: str = None,
    description: str = None
) -> "DocumentationVersionTypeDef":
    pass
```

### create_domain_name

Type annotations for `boto3.client("apigateway").create_domain_name` method.

[Client.create_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_domain_name)

```python
def create_domain_name(
    self,
    domainName: str,
    certificateName: str = None,
    certificateBody: str = None,
    certificatePrivateKey: str = None,
    certificateChain: str = None,
    certificateArn: str = None,
    regionalCertificateName: str = None,
    regionalCertificateArn: str = None,
    endpointConfiguration: "EndpointConfigurationTypeDef" = None,
    tags: Dict[str, str] = None,
    securityPolicy: SecurityPolicy = None,
    mutualTlsAuthentication: MutualTlsAuthenticationInputTypeDef = None
) -> "DomainNameTypeDef":
    pass
```

### create_model

Type annotations for `boto3.client("apigateway").create_model` method.

[Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_model)

```python
def create_model(
    self,
    restApiId: str,
    name: str,
    contentType: str,
    description: str = None,
    schema: str = None
) -> "ModelTypeDef":
    pass
```

### create_request_validator

Type annotations for `boto3.client("apigateway").create_request_validator` method.

[Client.create_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_request_validator)

```python
def create_request_validator(
    self,
    restApiId: str,
    name: str = None,
    validateRequestBody: bool = None,
    validateRequestParameters: bool = None
) -> "RequestValidatorTypeDef":
    pass
```

### create_resource

Type annotations for `boto3.client("apigateway").create_resource` method.

[Client.create_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_resource)

```python
def create_resource(
    self,
    restApiId: str,
    parentId: str,
    pathPart: str
) -> "ResourceTypeDef":
    pass
```

### create_rest_api

Type annotations for `boto3.client("apigateway").create_rest_api` method.

[Client.create_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_rest_api)

```python
def create_rest_api(
    self,
    name: str,
    description: str = None,
    version: str = None,
    cloneFrom: str = None,
    binaryMediaTypes: List[str] = None,
    minimumCompressionSize: int = None,
    apiKeySource: ApiKeySourceType = None,
    endpointConfiguration: "EndpointConfigurationTypeDef" = None,
    policy: str = None,
    tags: Dict[str, str] = None,
    disableExecuteApiEndpoint: bool = None
) -> "RestApiTypeDef":
    pass
```

### create_stage

Type annotations for `boto3.client("apigateway").create_stage` method.

[Client.create_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_stage)

```python
def create_stage(
    self,
    restApiId: str,
    stageName: str,
    deploymentId: str,
    description: str = None,
    cacheClusterEnabled: bool = None,
    cacheClusterSize: CacheClusterSize = None,
    variables: Dict[str, str] = None,
    documentationVersion: str = None,
    canarySettings: "CanarySettingsTypeDef" = None,
    tracingEnabled: bool = None,
    tags: Dict[str, str] = None
) -> "StageTypeDef":
    pass
```

### create_usage_plan

Type annotations for `boto3.client("apigateway").create_usage_plan` method.

[Client.create_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_usage_plan)

```python
def create_usage_plan(
    self,
    name: str,
    description: str = None,
    apiStages: List["ApiStageTypeDef"] = None,
    throttle: "ThrottleSettingsTypeDef" = None,
    quota: "QuotaSettingsTypeDef" = None,
    tags: Dict[str, str] = None
) -> "UsagePlanTypeDef":
    pass
```

### create_usage_plan_key

Type annotations for `boto3.client("apigateway").create_usage_plan_key` method.

[Client.create_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_usage_plan_key)

```python
def create_usage_plan_key(
    self,
    usagePlanId: str,
    keyId: str,
    keyType: str
) -> "UsagePlanKeyTypeDef":
    pass
```

### create_vpc_link

Type annotations for `boto3.client("apigateway").create_vpc_link` method.

[Client.create_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_vpc_link)

```python
def create_vpc_link(
    self,
    name: str,
    targetArns: List[str],
    description: str = None,
    tags: Dict[str, str] = None
) -> "VpcLinkTypeDef":
    pass
```

### delete_api_key

Type annotations for `boto3.client("apigateway").delete_api_key` method.

[Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_api_key)

```python
def delete_api_key(
    self,
    apiKey: str
) -> None:
    pass
```

### delete_authorizer

Type annotations for `boto3.client("apigateway").delete_authorizer` method.

[Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_authorizer)

```python
def delete_authorizer(
    self,
    restApiId: str,
    authorizerId: str
) -> None:
    pass
```

### delete_base_path_mapping

Type annotations for `boto3.client("apigateway").delete_base_path_mapping` method.

[Client.delete_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_base_path_mapping)

```python
def delete_base_path_mapping(
    self,
    domainName: str,
    basePath: str
) -> None:
    pass
```

### delete_client_certificate

Type annotations for `boto3.client("apigateway").delete_client_certificate` method.

[Client.delete_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_client_certificate)

```python
def delete_client_certificate(
    self,
    clientCertificateId: str
) -> None:
    pass
```

### delete_deployment

Type annotations for `boto3.client("apigateway").delete_deployment` method.

[Client.delete_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_deployment)

```python
def delete_deployment(
    self,
    restApiId: str,
    deploymentId: str
) -> None:
    pass
```

### delete_documentation_part

Type annotations for `boto3.client("apigateway").delete_documentation_part` method.

[Client.delete_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_documentation_part)

```python
def delete_documentation_part(
    self,
    restApiId: str,
    documentationPartId: str
) -> None:
    pass
```

### delete_documentation_version

Type annotations for `boto3.client("apigateway").delete_documentation_version` method.

[Client.delete_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_documentation_version)

```python
def delete_documentation_version(
    self,
    restApiId: str,
    documentationVersion: str
) -> None:
    pass
```

### delete_domain_name

Type annotations for `boto3.client("apigateway").delete_domain_name` method.

[Client.delete_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_domain_name)

```python
def delete_domain_name(
    self,
    domainName: str
) -> None:
    pass
```

### delete_gateway_response

Type annotations for `boto3.client("apigateway").delete_gateway_response` method.

[Client.delete_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_gateway_response)

```python
def delete_gateway_response(
    self,
    restApiId: str,
    responseType: GatewayResponseType
) -> None:
    pass
```

### delete_integration

Type annotations for `boto3.client("apigateway").delete_integration` method.

[Client.delete_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_integration)

```python
def delete_integration(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str
) -> None:
    pass
```

### delete_integration_response

Type annotations for `boto3.client("apigateway").delete_integration_response` method.

[Client.delete_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_integration_response)

```python
def delete_integration_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str
) -> None:
    pass
```

### delete_method

Type annotations for `boto3.client("apigateway").delete_method` method.

[Client.delete_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_method)

```python
def delete_method(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str
) -> None:
    pass
```

### delete_method_response

Type annotations for `boto3.client("apigateway").delete_method_response` method.

[Client.delete_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_method_response)

```python
def delete_method_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str
) -> None:
    pass
```

### delete_model

Type annotations for `boto3.client("apigateway").delete_model` method.

[Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_model)

```python
def delete_model(
    self,
    restApiId: str,
    modelName: str
) -> None:
    pass
```

### delete_request_validator

Type annotations for `boto3.client("apigateway").delete_request_validator` method.

[Client.delete_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_request_validator)

```python
def delete_request_validator(
    self,
    restApiId: str,
    requestValidatorId: str
) -> None:
    pass
```

### delete_resource

Type annotations for `boto3.client("apigateway").delete_resource` method.

[Client.delete_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_resource)

```python
def delete_resource(
    self,
    restApiId: str,
    resourceId: str
) -> None:
    pass
```

### delete_rest_api

Type annotations for `boto3.client("apigateway").delete_rest_api` method.

[Client.delete_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_rest_api)

```python
def delete_rest_api(
    self,
    restApiId: str
) -> None:
    pass
```

### delete_stage

Type annotations for `boto3.client("apigateway").delete_stage` method.

[Client.delete_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_stage)

```python
def delete_stage(
    self,
    restApiId: str,
    stageName: str
) -> None:
    pass
```

### delete_usage_plan

Type annotations for `boto3.client("apigateway").delete_usage_plan` method.

[Client.delete_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan)

```python
def delete_usage_plan(
    self,
    usagePlanId: str
) -> None:
    pass
```

### delete_usage_plan_key

Type annotations for `boto3.client("apigateway").delete_usage_plan_key` method.

[Client.delete_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan_key)

```python
def delete_usage_plan_key(
    self,
    usagePlanId: str,
    keyId: str
) -> None:
    pass
```

### delete_vpc_link

Type annotations for `boto3.client("apigateway").delete_vpc_link` method.

[Client.delete_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.delete_vpc_link)

```python
def delete_vpc_link(
    self,
    vpcLinkId: str
) -> None:
    pass
```

### flush_stage_authorizers_cache

Type annotations for `boto3.client("apigateway").flush_stage_authorizers_cache` method.

[Client.flush_stage_authorizers_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.flush_stage_authorizers_cache)

```python
def flush_stage_authorizers_cache(
    self,
    restApiId: str,
    stageName: str
) -> None:
    pass
```

### flush_stage_cache

Type annotations for `boto3.client("apigateway").flush_stage_cache` method.

[Client.flush_stage_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.flush_stage_cache)

```python
def flush_stage_cache(
    self,
    restApiId: str,
    stageName: str
) -> None:
    pass
```

### generate_client_certificate

Type annotations for `boto3.client("apigateway").generate_client_certificate` method.

[Client.generate_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.generate_client_certificate)

```python
def generate_client_certificate(
    self,
    description: str = None,
    tags: Dict[str, str] = None
) -> "ClientCertificateTypeDef":
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("apigateway").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.generate_presigned_url)

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

### get_account

Type annotations for `boto3.client("apigateway").get_account` method.

[Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_account)

```python
def get_account(
    self
) -> AccountTypeDef:
    pass
```

### get_api_key

Type annotations for `boto3.client("apigateway").get_api_key` method.

[Client.get_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_api_key)

```python
def get_api_key(
    self,
    apiKey: str,
    includeValue: bool = None
) -> "ApiKeyTypeDef":
    pass
```

### get_api_keys

Type annotations for `boto3.client("apigateway").get_api_keys` method.

[Client.get_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_api_keys)

```python
def get_api_keys(
    self,
    position: str = None,
    limit: int = None,
    nameQuery: str = None,
    customerId: str = None,
    includeValues: bool = None
) -> ApiKeysTypeDef:
    pass
```

### get_authorizer

Type annotations for `boto3.client("apigateway").get_authorizer` method.

[Client.get_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_authorizer)

```python
def get_authorizer(
    self,
    restApiId: str,
    authorizerId: str
) -> "AuthorizerTypeDef":
    pass
```

### get_authorizers

Type annotations for `boto3.client("apigateway").get_authorizers` method.

[Client.get_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_authorizers)

```python
def get_authorizers(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None
) -> AuthorizersTypeDef:
    pass
```

### get_base_path_mapping

Type annotations for `boto3.client("apigateway").get_base_path_mapping` method.

[Client.get_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_base_path_mapping)

```python
def get_base_path_mapping(
    self,
    domainName: str,
    basePath: str
) -> "BasePathMappingTypeDef":
    pass
```

### get_base_path_mappings

Type annotations for `boto3.client("apigateway").get_base_path_mappings` method.

[Client.get_base_path_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_base_path_mappings)

```python
def get_base_path_mappings(
    self,
    domainName: str,
    position: str = None,
    limit: int = None
) -> BasePathMappingsTypeDef:
    pass
```

### get_client_certificate

Type annotations for `boto3.client("apigateway").get_client_certificate` method.

[Client.get_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_client_certificate)

```python
def get_client_certificate(
    self,
    clientCertificateId: str
) -> "ClientCertificateTypeDef":
    pass
```

### get_client_certificates

Type annotations for `boto3.client("apigateway").get_client_certificates` method.

[Client.get_client_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_client_certificates)

```python
def get_client_certificates(
    self,
    position: str = None,
    limit: int = None
) -> ClientCertificatesTypeDef:
    pass
```

### get_deployment

Type annotations for `boto3.client("apigateway").get_deployment` method.

[Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_deployment)

```python
def get_deployment(
    self,
    restApiId: str,
    deploymentId: str,
    embed: List[str] = None
) -> "DeploymentTypeDef":
    pass
```

### get_deployments

Type annotations for `boto3.client("apigateway").get_deployments` method.

[Client.get_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_deployments)

```python
def get_deployments(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None
) -> DeploymentsTypeDef:
    pass
```

### get_documentation_part

Type annotations for `boto3.client("apigateway").get_documentation_part` method.

[Client.get_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_documentation_part)

```python
def get_documentation_part(
    self,
    restApiId: str,
    documentationPartId: str
) -> "DocumentationPartTypeDef":
    pass
```

### get_documentation_parts

Type annotations for `boto3.client("apigateway").get_documentation_parts` method.

[Client.get_documentation_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_documentation_parts)

```python
def get_documentation_parts(
    self,
    restApiId: str,
    type: DocumentationPartType = None,
    nameQuery: str = None,
    path: str = None,
    position: str = None,
    limit: int = None,
    locationStatus: LocationStatusType = None
) -> DocumentationPartsTypeDef:
    pass
```

### get_documentation_version

Type annotations for `boto3.client("apigateway").get_documentation_version` method.

[Client.get_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_documentation_version)

```python
def get_documentation_version(
    self,
    restApiId: str,
    documentationVersion: str
) -> "DocumentationVersionTypeDef":
    pass
```

### get_documentation_versions

Type annotations for `boto3.client("apigateway").get_documentation_versions` method.

[Client.get_documentation_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_documentation_versions)

```python
def get_documentation_versions(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None
) -> DocumentationVersionsTypeDef:
    pass
```

### get_domain_name

Type annotations for `boto3.client("apigateway").get_domain_name` method.

[Client.get_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_domain_name)

```python
def get_domain_name(
    self,
    domainName: str
) -> "DomainNameTypeDef":
    pass
```

### get_domain_names

Type annotations for `boto3.client("apigateway").get_domain_names` method.

[Client.get_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_domain_names)

```python
def get_domain_names(
    self,
    position: str = None,
    limit: int = None
) -> DomainNamesTypeDef:
    pass
```

### get_export

Type annotations for `boto3.client("apigateway").get_export` method.

[Client.get_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_export)

```python
def get_export(
    self,
    restApiId: str,
    stageName: str,
    exportType: str,
    parameters: Dict[str, str] = None,
    accepts: str = None
) -> ExportResponseTypeDef:
    pass
```

### get_gateway_response

Type annotations for `boto3.client("apigateway").get_gateway_response` method.

[Client.get_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_gateway_response)

```python
def get_gateway_response(
    self,
    restApiId: str,
    responseType: GatewayResponseType
) -> "GatewayResponseTypeDef":
    pass
```

### get_gateway_responses

Type annotations for `boto3.client("apigateway").get_gateway_responses` method.

[Client.get_gateway_responses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_gateway_responses)

```python
def get_gateway_responses(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None
) -> GatewayResponsesTypeDef:
    pass
```

### get_integration

Type annotations for `boto3.client("apigateway").get_integration` method.

[Client.get_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_integration)

```python
def get_integration(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str
) -> "IntegrationTypeDef":
    pass
```

### get_integration_response

Type annotations for `boto3.client("apigateway").get_integration_response` method.

[Client.get_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_integration_response)

```python
def get_integration_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str
) -> "IntegrationResponseTypeDef":
    pass
```

### get_method

Type annotations for `boto3.client("apigateway").get_method` method.

[Client.get_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_method)

```python
def get_method(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str
) -> "MethodTypeDef":
    pass
```

### get_method_response

Type annotations for `boto3.client("apigateway").get_method_response` method.

[Client.get_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_method_response)

```python
def get_method_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str
) -> "MethodResponseTypeDef":
    pass
```

### get_model

Type annotations for `boto3.client("apigateway").get_model` method.

[Client.get_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_model)

```python
def get_model(
    self,
    restApiId: str,
    modelName: str,
    flatten: bool = None
) -> "ModelTypeDef":
    pass
```

### get_model_template

Type annotations for `boto3.client("apigateway").get_model_template` method.

[Client.get_model_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_model_template)

```python
def get_model_template(
    self,
    restApiId: str,
    modelName: str
) -> TemplateTypeDef:
    pass
```

### get_models

Type annotations for `boto3.client("apigateway").get_models` method.

[Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_models)

```python
def get_models(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None
) -> ModelsTypeDef:
    pass
```

### get_request_validator

Type annotations for `boto3.client("apigateway").get_request_validator` method.

[Client.get_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_request_validator)

```python
def get_request_validator(
    self,
    restApiId: str,
    requestValidatorId: str
) -> "RequestValidatorTypeDef":
    pass
```

### get_request_validators

Type annotations for `boto3.client("apigateway").get_request_validators` method.

[Client.get_request_validators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_request_validators)

```python
def get_request_validators(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None
) -> RequestValidatorsTypeDef:
    pass
```

### get_resource

Type annotations for `boto3.client("apigateway").get_resource` method.

[Client.get_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_resource)

```python
def get_resource(
    self,
    restApiId: str,
    resourceId: str,
    embed: List[str] = None
) -> "ResourceTypeDef":
    pass
```

### get_resources

Type annotations for `boto3.client("apigateway").get_resources` method.

[Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_resources)

```python
def get_resources(
    self,
    restApiId: str,
    position: str = None,
    limit: int = None,
    embed: List[str] = None
) -> ResourcesTypeDef:
    pass
```

### get_rest_api

Type annotations for `boto3.client("apigateway").get_rest_api` method.

[Client.get_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_rest_api)

```python
def get_rest_api(
    self,
    restApiId: str
) -> "RestApiTypeDef":
    pass
```

### get_rest_apis

Type annotations for `boto3.client("apigateway").get_rest_apis` method.

[Client.get_rest_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_rest_apis)

```python
def get_rest_apis(
    self,
    position: str = None,
    limit: int = None
) -> RestApisTypeDef:
    pass
```

### get_sdk

Type annotations for `boto3.client("apigateway").get_sdk` method.

[Client.get_sdk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_sdk)

```python
def get_sdk(
    self,
    restApiId: str,
    stageName: str,
    sdkType: str,
    parameters: Dict[str, str] = None
) -> SdkResponseTypeDef:
    pass
```

### get_sdk_type

Type annotations for `boto3.client("apigateway").get_sdk_type` method.

[Client.get_sdk_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_sdk_type)

```python
def get_sdk_type(
    self,
    id: str
) -> "SdkTypeTypeDef":
    pass
```

### get_sdk_types

Type annotations for `boto3.client("apigateway").get_sdk_types` method.

[Client.get_sdk_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_sdk_types)

```python
def get_sdk_types(
    self,
    position: str = None,
    limit: int = None
) -> SdkTypesTypeDef:
    pass
```

### get_stage

Type annotations for `boto3.client("apigateway").get_stage` method.

[Client.get_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_stage)

```python
def get_stage(
    self,
    restApiId: str,
    stageName: str
) -> "StageTypeDef":
    pass
```

### get_stages

Type annotations for `boto3.client("apigateway").get_stages` method.

[Client.get_stages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_stages)

```python
def get_stages(
    self,
    restApiId: str,
    deploymentId: str = None
) -> StagesTypeDef:
    pass
```

### get_tags

Type annotations for `boto3.client("apigateway").get_tags` method.

[Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_tags)

```python
def get_tags(
    self,
    resourceArn: str,
    position: str = None,
    limit: int = None
) -> TagsTypeDef:
    pass
```

### get_usage

Type annotations for `boto3.client("apigateway").get_usage` method.

[Client.get_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_usage)

```python
def get_usage(
    self,
    usagePlanId: str,
    startDate: str,
    endDate: str,
    keyId: str = None,
    position: str = None,
    limit: int = None
) -> UsageTypeDef:
    pass
```

### get_usage_plan

Type annotations for `boto3.client("apigateway").get_usage_plan` method.

[Client.get_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_usage_plan)

```python
def get_usage_plan(
    self,
    usagePlanId: str
) -> "UsagePlanTypeDef":
    pass
```

### get_usage_plan_key

Type annotations for `boto3.client("apigateway").get_usage_plan_key` method.

[Client.get_usage_plan_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_key)

```python
def get_usage_plan_key(
    self,
    usagePlanId: str,
    keyId: str
) -> "UsagePlanKeyTypeDef":
    pass
```

### get_usage_plan_keys

Type annotations for `boto3.client("apigateway").get_usage_plan_keys` method.

[Client.get_usage_plan_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_keys)

```python
def get_usage_plan_keys(
    self,
    usagePlanId: str,
    position: str = None,
    limit: int = None,
    nameQuery: str = None
) -> UsagePlanKeysTypeDef:
    pass
```

### get_usage_plans

Type annotations for `boto3.client("apigateway").get_usage_plans` method.

[Client.get_usage_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_usage_plans)

```python
def get_usage_plans(
    self,
    position: str = None,
    keyId: str = None,
    limit: int = None
) -> UsagePlansTypeDef:
    pass
```

### get_vpc_link

Type annotations for `boto3.client("apigateway").get_vpc_link` method.

[Client.get_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_vpc_link)

```python
def get_vpc_link(
    self,
    vpcLinkId: str
) -> "VpcLinkTypeDef":
    pass
```

### get_vpc_links

Type annotations for `boto3.client("apigateway").get_vpc_links` method.

[Client.get_vpc_links documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.get_vpc_links)

```python
def get_vpc_links(
    self,
    position: str = None,
    limit: int = None
) -> VpcLinksTypeDef:
    pass
```

### import_api_keys

Type annotations for `boto3.client("apigateway").import_api_keys` method.

[Client.import_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.import_api_keys)

```python
def import_api_keys(
    self,
    body: Union[bytes, IO[bytes]],
    format: ApiKeysFormat,
    failOnWarnings: bool = None
) -> ApiKeyIdsTypeDef:
    pass
```

### import_documentation_parts

Type annotations for `boto3.client("apigateway").import_documentation_parts` method.

[Client.import_documentation_parts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.import_documentation_parts)

```python
def import_documentation_parts(
    self,
    restApiId: str,
    body: Union[bytes, IO[bytes]],
    mode: PutMode = None,
    failOnWarnings: bool = None
) -> DocumentationPartIdsTypeDef:
    pass
```

### import_rest_api

Type annotations for `boto3.client("apigateway").import_rest_api` method.

[Client.import_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.import_rest_api)

```python
def import_rest_api(
    self,
    body: Union[bytes, IO[bytes]],
    failOnWarnings: bool = None,
    parameters: Dict[str, str] = None
) -> "RestApiTypeDef":
    pass
```

### put_gateway_response

Type annotations for `boto3.client("apigateway").put_gateway_response` method.

[Client.put_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.put_gateway_response)

```python
def put_gateway_response(
    self,
    restApiId: str,
    responseType: GatewayResponseType,
    statusCode: str = None,
    responseParameters: Dict[str, str] = None,
    responseTemplates: Dict[str, str] = None
) -> "GatewayResponseTypeDef":
    pass
```

### put_integration

Type annotations for `boto3.client("apigateway").put_integration` method.

[Client.put_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.put_integration)

```python
def put_integration(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    type: IntegrationType,
    integrationHttpMethod: str = None,
    uri: str = None,
    connectionType: ConnectionType = None,
    connectionId: str = None,
    credentials: str = None,
    requestParameters: Dict[str, str] = None,
    requestTemplates: Dict[str, str] = None,
    passthroughBehavior: str = None,
    cacheNamespace: str = None,
    cacheKeyParameters: List[str] = None,
    contentHandling: ContentHandlingStrategy = None,
    timeoutInMillis: int = None,
    tlsConfig: "TlsConfigTypeDef" = None
) -> "IntegrationTypeDef":
    pass
```

### put_integration_response

Type annotations for `boto3.client("apigateway").put_integration_response` method.

[Client.put_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.put_integration_response)

```python
def put_integration_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    selectionPattern: str = None,
    responseParameters: Dict[str, str] = None,
    responseTemplates: Dict[str, str] = None,
    contentHandling: ContentHandlingStrategy = None
) -> "IntegrationResponseTypeDef":
    pass
```

### put_method

Type annotations for `boto3.client("apigateway").put_method` method.

[Client.put_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.put_method)

```python
def put_method(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    authorizationType: str,
    authorizerId: str = None,
    apiKeyRequired: bool = None,
    operationName: str = None,
    requestParameters: Dict[str, bool] = None,
    requestModels: Dict[str, str] = None,
    requestValidatorId: str = None,
    authorizationScopes: List[str] = None
) -> "MethodTypeDef":
    pass
```

### put_method_response

Type annotations for `boto3.client("apigateway").put_method_response` method.

[Client.put_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.put_method_response)

```python
def put_method_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    responseParameters: Dict[str, bool] = None,
    responseModels: Dict[str, str] = None
) -> "MethodResponseTypeDef":
    pass
```

### put_rest_api

Type annotations for `boto3.client("apigateway").put_rest_api` method.

[Client.put_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.put_rest_api)

```python
def put_rest_api(
    self,
    restApiId: str,
    body: Union[bytes, IO[bytes]],
    mode: PutMode = None,
    failOnWarnings: bool = None,
    parameters: Dict[str, str] = None
) -> "RestApiTypeDef":
    pass
```

### tag_resource

Type annotations for `boto3.client("apigateway").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> None:
    pass
```

### test_invoke_authorizer

Type annotations for `boto3.client("apigateway").test_invoke_authorizer` method.

[Client.test_invoke_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.test_invoke_authorizer)

```python
def test_invoke_authorizer(
    self,
    restApiId: str,
    authorizerId: str,
    headers: Dict[str, str] = None,
    multiValueHeaders: Dict[str, List[str]] = None,
    pathWithQueryString: str = None,
    body: str = None,
    stageVariables: Dict[str, str] = None,
    additionalContext: Dict[str, str] = None
) -> TestInvokeAuthorizerResponseTypeDef:
    pass
```

### test_invoke_method

Type annotations for `boto3.client("apigateway").test_invoke_method` method.

[Client.test_invoke_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.test_invoke_method)

```python
def test_invoke_method(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    pathWithQueryString: str = None,
    body: str = None,
    headers: Dict[str, str] = None,
    multiValueHeaders: Dict[str, List[str]] = None,
    clientCertificateId: str = None,
    stageVariables: Dict[str, str] = None
) -> TestInvokeMethodResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("apigateway").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> None:
    pass
```

### update_account

Type annotations for `boto3.client("apigateway").update_account` method.

[Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_account)

```python
def update_account(
    self,
    patchOperations: List[PatchOperationTypeDef] = None
) -> AccountTypeDef:
    pass
```

### update_api_key

Type annotations for `boto3.client("apigateway").update_api_key` method.

[Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_api_key)

```python
def update_api_key(
    self,
    apiKey: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "ApiKeyTypeDef":
    pass
```

### update_authorizer

Type annotations for `boto3.client("apigateway").update_authorizer` method.

[Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_authorizer)

```python
def update_authorizer(
    self,
    restApiId: str,
    authorizerId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "AuthorizerTypeDef":
    pass
```

### update_base_path_mapping

Type annotations for `boto3.client("apigateway").update_base_path_mapping` method.

[Client.update_base_path_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_base_path_mapping)

```python
def update_base_path_mapping(
    self,
    domainName: str,
    basePath: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "BasePathMappingTypeDef":
    pass
```

### update_client_certificate

Type annotations for `boto3.client("apigateway").update_client_certificate` method.

[Client.update_client_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_client_certificate)

```python
def update_client_certificate(
    self,
    clientCertificateId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "ClientCertificateTypeDef":
    pass
```

### update_deployment

Type annotations for `boto3.client("apigateway").update_deployment` method.

[Client.update_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_deployment)

```python
def update_deployment(
    self,
    restApiId: str,
    deploymentId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "DeploymentTypeDef":
    pass
```

### update_documentation_part

Type annotations for `boto3.client("apigateway").update_documentation_part` method.

[Client.update_documentation_part documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_documentation_part)

```python
def update_documentation_part(
    self,
    restApiId: str,
    documentationPartId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "DocumentationPartTypeDef":
    pass
```

### update_documentation_version

Type annotations for `boto3.client("apigateway").update_documentation_version` method.

[Client.update_documentation_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_documentation_version)

```python
def update_documentation_version(
    self,
    restApiId: str,
    documentationVersion: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "DocumentationVersionTypeDef":
    pass
```

### update_domain_name

Type annotations for `boto3.client("apigateway").update_domain_name` method.

[Client.update_domain_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_domain_name)

```python
def update_domain_name(
    self,
    domainName: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "DomainNameTypeDef":
    pass
```

### update_gateway_response

Type annotations for `boto3.client("apigateway").update_gateway_response` method.

[Client.update_gateway_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_gateway_response)

```python
def update_gateway_response(
    self,
    restApiId: str,
    responseType: GatewayResponseType,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "GatewayResponseTypeDef":
    pass
```

### update_integration

Type annotations for `boto3.client("apigateway").update_integration` method.

[Client.update_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_integration)

```python
def update_integration(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "IntegrationTypeDef":
    pass
```

### update_integration_response

Type annotations for `boto3.client("apigateway").update_integration_response` method.

[Client.update_integration_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_integration_response)

```python
def update_integration_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "IntegrationResponseTypeDef":
    pass
```

### update_method

Type annotations for `boto3.client("apigateway").update_method` method.

[Client.update_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_method)

```python
def update_method(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "MethodTypeDef":
    pass
```

### update_method_response

Type annotations for `boto3.client("apigateway").update_method_response` method.

[Client.update_method_response documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_method_response)

```python
def update_method_response(
    self,
    restApiId: str,
    resourceId: str,
    httpMethod: str,
    statusCode: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "MethodResponseTypeDef":
    pass
```

### update_model

Type annotations for `boto3.client("apigateway").update_model` method.

[Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_model)

```python
def update_model(
    self,
    restApiId: str,
    modelName: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "ModelTypeDef":
    pass
```

### update_request_validator

Type annotations for `boto3.client("apigateway").update_request_validator` method.

[Client.update_request_validator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_request_validator)

```python
def update_request_validator(
    self,
    restApiId: str,
    requestValidatorId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "RequestValidatorTypeDef":
    pass
```

### update_resource

Type annotations for `boto3.client("apigateway").update_resource` method.

[Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_resource)

```python
def update_resource(
    self,
    restApiId: str,
    resourceId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "ResourceTypeDef":
    pass
```

### update_rest_api

Type annotations for `boto3.client("apigateway").update_rest_api` method.

[Client.update_rest_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_rest_api)

```python
def update_rest_api(
    self,
    restApiId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "RestApiTypeDef":
    pass
```

### update_stage

Type annotations for `boto3.client("apigateway").update_stage` method.

[Client.update_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_stage)

```python
def update_stage(
    self,
    restApiId: str,
    stageName: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "StageTypeDef":
    pass
```

### update_usage

Type annotations for `boto3.client("apigateway").update_usage` method.

[Client.update_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_usage)

```python
def update_usage(
    self,
    usagePlanId: str,
    keyId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> UsageTypeDef:
    pass
```

### update_usage_plan

Type annotations for `boto3.client("apigateway").update_usage_plan` method.

[Client.update_usage_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_usage_plan)

```python
def update_usage_plan(
    self,
    usagePlanId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "UsagePlanTypeDef":
    pass
```

### update_vpc_link

Type annotations for `boto3.client("apigateway").update_vpc_link` method.

[Client.update_vpc_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.update_vpc_link)

```python
def update_vpc_link(
    self,
    vpcLinkId: str,
    patchOperations: List[PatchOperationTypeDef] = None
) -> "VpcLinkTypeDef":
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: GetApiKeysPaginatorName
) -> GetApiKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)

```python
@overload
def get_paginator(
    self,
    operation_name: GetAuthorizersPaginatorName
) -> GetAuthorizersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetBasePathMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBasePathMappingsPaginatorName
) -> GetBasePathMappingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)

```python
@overload
def get_paginator(
    self,
    operation_name: GetClientCertificatesPaginatorName
) -> GetClientCertificatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDeploymentsPaginatorName
) -> GetDeploymentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetDocumentationParts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDocumentationPartsPaginatorName
) -> GetDocumentationPartsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetDocumentationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDocumentationVersionsPaginatorName
) -> GetDocumentationVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDomainNamesPaginatorName
) -> GetDomainNamesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetGatewayResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)

```python
@overload
def get_paginator(
    self,
    operation_name: GetGatewayResponsesPaginatorName
) -> GetGatewayResponsesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetModels)

```python
@overload
def get_paginator(
    self,
    operation_name: GetModelsPaginatorName
) -> GetModelsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetRequestValidators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRequestValidatorsPaginatorName
) -> GetRequestValidatorsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetResources)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourcesPaginatorName
) -> GetResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetRestApis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRestApisPaginatorName
) -> GetRestApisPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetSdkTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSdkTypesPaginatorName
) -> GetSdkTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetUsage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)

```python
@overload
def get_paginator(
    self,
    operation_name: GetUsagePaginatorName
) -> GetUsagePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetUsagePlanKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: GetUsagePlanKeysPaginatorName
) -> GetUsagePlanKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetUsagePlans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)

```python
@overload
def get_paginator(
    self,
    operation_name: GetUsagePlansPaginatorName
) -> GetUsagePlansPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("apigateway").get_paginator` method.

[Paginator.GetVpcLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)

```python
@overload
def get_paginator(
    self,
    operation_name: GetVpcLinksPaginatorName
) -> GetVpcLinksPaginator:
    pass
```