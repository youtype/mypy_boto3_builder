# Literals for boto3 APIGateway module

> [Index](../index.md) > [APIGateway](./index.md) > Literals

Auto-generated documentation for [APIGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway)
type annotations stubs module [mypy_boto3_apigateway](https://pypi.org/project/mypy-boto3-apigateway/).

- [Literals for boto3 APIGateway module](#literals-for-boto3-apigateway-module)
  - [ApiKeySourceType](#apikeysourcetype)
  - [ApiKeysFormat](#apikeysformat)
  - [AuthorizerType](#authorizertype)
  - [CacheClusterSize](#cacheclustersize)
  - [CacheClusterStatus](#cacheclusterstatus)
  - [ConnectionType](#connectiontype)
  - [ContentHandlingStrategy](#contenthandlingstrategy)
  - [DocumentationPartType](#documentationparttype)
  - [DomainNameStatus](#domainnamestatus)
  - [EndpointType](#endpointtype)
  - [GatewayResponseType](#gatewayresponsetype)
  - [GetApiKeysPaginatorName](#getapikeyspaginatorname)
  - [GetAuthorizersPaginatorName](#getauthorizerspaginatorname)
  - [GetBasePathMappingsPaginatorName](#getbasepathmappingspaginatorname)
  - [GetClientCertificatesPaginatorName](#getclientcertificatespaginatorname)
  - [GetDeploymentsPaginatorName](#getdeploymentspaginatorname)
  - [GetDocumentationPartsPaginatorName](#getdocumentationpartspaginatorname)
  - [GetDocumentationVersionsPaginatorName](#getdocumentationversionspaginatorname)
  - [GetDomainNamesPaginatorName](#getdomainnamespaginatorname)
  - [GetGatewayResponsesPaginatorName](#getgatewayresponsespaginatorname)
  - [GetModelsPaginatorName](#getmodelspaginatorname)
  - [GetRequestValidatorsPaginatorName](#getrequestvalidatorspaginatorname)
  - [GetResourcesPaginatorName](#getresourcespaginatorname)
  - [GetRestApisPaginatorName](#getrestapispaginatorname)
  - [GetSdkTypesPaginatorName](#getsdktypespaginatorname)
  - [GetUsagePaginatorName](#getusagepaginatorname)
  - [GetUsagePlanKeysPaginatorName](#getusageplankeyspaginatorname)
  - [GetUsagePlansPaginatorName](#getusageplanspaginatorname)
  - [GetVpcLinksPaginatorName](#getvpclinkspaginatorname)
  - [IntegrationType](#integrationtype)
  - [LocationStatusType](#locationstatustype)
  - [Op](#op)
  - [PutMode](#putmode)
  - [QuotaPeriodType](#quotaperiodtype)
  - [SecurityPolicy](#securitypolicy)
  - [UnauthorizedCacheControlHeaderStrategy](#unauthorizedcachecontrolheaderstrategy)
  - [VpcLinkStatus](#vpclinkstatus)

## ApiKeySourceType

```python
from mypy_boto3_apigateway.literals import ApiKeySourceType
```

Values:

- `AUTHORIZER`
- `HEADER`

## ApiKeysFormat

```python
from mypy_boto3_apigateway.literals import ApiKeysFormat
```

Values:

- `csv`

## AuthorizerType

```python
from mypy_boto3_apigateway.literals import AuthorizerType
```

Values:

- `COGNITO_USER_POOLS`
- `REQUEST`
- `TOKEN`

## CacheClusterSize

```python
from mypy_boto3_apigateway.literals import CacheClusterSize
```

Values:

- `0.5`
- `1.6`
- `118`
- `13.5`
- `237`
- `28.4`
- `58.2`
- `6.1`

## CacheClusterStatus

```python
from mypy_boto3_apigateway.literals import CacheClusterStatus
```

Values:

- `AVAILABLE`
- `CREATE_IN_PROGRESS`
- `DELETE_IN_PROGRESS`
- `FLUSH_IN_PROGRESS`
- `NOT_AVAILABLE`

## ConnectionType

```python
from mypy_boto3_apigateway.literals import ConnectionType
```

Values:

- `INTERNET`
- `VPC_LINK`

## ContentHandlingStrategy

```python
from mypy_boto3_apigateway.literals import ContentHandlingStrategy
```

Values:

- `CONVERT_TO_BINARY`
- `CONVERT_TO_TEXT`

## DocumentationPartType

```python
from mypy_boto3_apigateway.literals import DocumentationPartType
```

Values:

- `API`
- `AUTHORIZER`
- `METHOD`
- `MODEL`
- `PATH_PARAMETER`
- `QUERY_PARAMETER`
- `REQUEST_BODY`
- `REQUEST_HEADER`
- `RESOURCE`
- `RESPONSE`
- `RESPONSE_BODY`
- `RESPONSE_HEADER`

## DomainNameStatus

```python
from mypy_boto3_apigateway.literals import DomainNameStatus
```

Values:

- `AVAILABLE`
- `PENDING`
- `UPDATING`

## EndpointType

```python
from mypy_boto3_apigateway.literals import EndpointType
```

Values:

- `EDGE`
- `PRIVATE`
- `REGIONAL`

## GatewayResponseType

```python
from mypy_boto3_apigateway.literals import GatewayResponseType
```

Values:

- `ACCESS_DENIED`
- `API_CONFIGURATION_ERROR`
- `AUTHORIZER_CONFIGURATION_ERROR`
- `AUTHORIZER_FAILURE`
- `BAD_REQUEST_BODY`
- `BAD_REQUEST_PARAMETERS`
- `DEFAULT_4XX`
- `DEFAULT_5XX`
- `EXPIRED_TOKEN`
- `INTEGRATION_FAILURE`
- `INTEGRATION_TIMEOUT`
- `INVALID_API_KEY`
- `INVALID_SIGNATURE`
- `MISSING_AUTHENTICATION_TOKEN`
- `QUOTA_EXCEEDED`
- `REQUEST_TOO_LARGE`
- `RESOURCE_NOT_FOUND`
- `THROTTLED`
- `UNAUTHORIZED`
- `UNSUPPORTED_MEDIA_TYPE`

## GetApiKeysPaginatorName

```python
from mypy_boto3_apigateway.literals import GetApiKeysPaginatorName
```

Values:

- `get_api_keys`

## GetAuthorizersPaginatorName

```python
from mypy_boto3_apigateway.literals import GetAuthorizersPaginatorName
```

Values:

- `get_authorizers`

## GetBasePathMappingsPaginatorName

```python
from mypy_boto3_apigateway.literals import GetBasePathMappingsPaginatorName
```

Values:

- `get_base_path_mappings`

## GetClientCertificatesPaginatorName

```python
from mypy_boto3_apigateway.literals import GetClientCertificatesPaginatorName
```

Values:

- `get_client_certificates`

## GetDeploymentsPaginatorName

```python
from mypy_boto3_apigateway.literals import GetDeploymentsPaginatorName
```

Values:

- `get_deployments`

## GetDocumentationPartsPaginatorName

```python
from mypy_boto3_apigateway.literals import GetDocumentationPartsPaginatorName
```

Values:

- `get_documentation_parts`

## GetDocumentationVersionsPaginatorName

```python
from mypy_boto3_apigateway.literals import GetDocumentationVersionsPaginatorName
```

Values:

- `get_documentation_versions`

## GetDomainNamesPaginatorName

```python
from mypy_boto3_apigateway.literals import GetDomainNamesPaginatorName
```

Values:

- `get_domain_names`

## GetGatewayResponsesPaginatorName

```python
from mypy_boto3_apigateway.literals import GetGatewayResponsesPaginatorName
```

Values:

- `get_gateway_responses`

## GetModelsPaginatorName

```python
from mypy_boto3_apigateway.literals import GetModelsPaginatorName
```

Values:

- `get_models`

## GetRequestValidatorsPaginatorName

```python
from mypy_boto3_apigateway.literals import GetRequestValidatorsPaginatorName
```

Values:

- `get_request_validators`

## GetResourcesPaginatorName

```python
from mypy_boto3_apigateway.literals import GetResourcesPaginatorName
```

Values:

- `get_resources`

## GetRestApisPaginatorName

```python
from mypy_boto3_apigateway.literals import GetRestApisPaginatorName
```

Values:

- `get_rest_apis`

## GetSdkTypesPaginatorName

```python
from mypy_boto3_apigateway.literals import GetSdkTypesPaginatorName
```

Values:

- `get_sdk_types`

## GetUsagePaginatorName

```python
from mypy_boto3_apigateway.literals import GetUsagePaginatorName
```

Values:

- `get_usage`

## GetUsagePlanKeysPaginatorName

```python
from mypy_boto3_apigateway.literals import GetUsagePlanKeysPaginatorName
```

Values:

- `get_usage_plan_keys`

## GetUsagePlansPaginatorName

```python
from mypy_boto3_apigateway.literals import GetUsagePlansPaginatorName
```

Values:

- `get_usage_plans`

## GetVpcLinksPaginatorName

```python
from mypy_boto3_apigateway.literals import GetVpcLinksPaginatorName
```

Values:

- `get_vpc_links`

## IntegrationType

```python
from mypy_boto3_apigateway.literals import IntegrationType
```

Values:

- `AWS`
- `AWS_PROXY`
- `HTTP`
- `HTTP_PROXY`
- `MOCK`

## LocationStatusType

```python
from mypy_boto3_apigateway.literals import LocationStatusType
```

Values:

- `DOCUMENTED`
- `UNDOCUMENTED`

## Op

```python
from mypy_boto3_apigateway.literals import Op
```

Values:

- `add`
- `copy`
- `move`
- `remove`
- `replace`
- `test`

## PutMode

```python
from mypy_boto3_apigateway.literals import PutMode
```

Values:

- `merge`
- `overwrite`

## QuotaPeriodType

```python
from mypy_boto3_apigateway.literals import QuotaPeriodType
```

Values:

- `DAY`
- `MONTH`
- `WEEK`

## SecurityPolicy

```python
from mypy_boto3_apigateway.literals import SecurityPolicy
```

Values:

- `TLS_1_0`
- `TLS_1_2`

## UnauthorizedCacheControlHeaderStrategy

```python
from mypy_boto3_apigateway.literals import UnauthorizedCacheControlHeaderStrategy
```

Values:

- `FAIL_WITH_403`
- `SUCCEED_WITH_RESPONSE_HEADER`
- `SUCCEED_WITHOUT_RESPONSE_HEADER`

## VpcLinkStatus

```python
from mypy_boto3_apigateway.literals import VpcLinkStatus
```

Values:

- `AVAILABLE`
- `DELETING`
- `FAILED`
- `PENDING`
