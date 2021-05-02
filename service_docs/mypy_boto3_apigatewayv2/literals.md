# Literals for boto3 ApiGatewayV2 module

> [Index](../index.md) > [ApiGatewayV2](./index.md) > Literals

Auto-generated documentation for [ApiGatewayV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2)
type annotations stubs module [mypy_boto3_apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/).

- [Literals for boto3 ApiGatewayV2 module](#literals-for-boto3-apigatewayv2-module)
  - [AuthorizationType](#authorizationtype)
  - [AuthorizerType](#authorizertype)
  - [ConnectionType](#connectiontype)
  - [ContentHandlingStrategy](#contenthandlingstrategy)
  - [DeploymentStatus](#deploymentstatus)
  - [DomainNameStatus](#domainnamestatus)
  - [EndpointType](#endpointtype)
  - [GetApisPaginatorName](#getapispaginatorname)
  - [GetAuthorizersPaginatorName](#getauthorizerspaginatorname)
  - [GetDeploymentsPaginatorName](#getdeploymentspaginatorname)
  - [GetDomainNamesPaginatorName](#getdomainnamespaginatorname)
  - [GetIntegrationResponsesPaginatorName](#getintegrationresponsespaginatorname)
  - [GetIntegrationsPaginatorName](#getintegrationspaginatorname)
  - [GetModelsPaginatorName](#getmodelspaginatorname)
  - [GetRouteResponsesPaginatorName](#getrouteresponsespaginatorname)
  - [GetRoutesPaginatorName](#getroutespaginatorname)
  - [GetStagesPaginatorName](#getstagespaginatorname)
  - [IntegrationType](#integrationtype)
  - [JSONYAMLType](#jsonyamltype)
  - [LoggingLevel](#logginglevel)
  - [OAS30Type](#oas30type)
  - [PassthroughBehavior](#passthroughbehavior)
  - [ProtocolType](#protocoltype)
  - [SecurityPolicy](#securitypolicy)
  - [VpcLinkStatus](#vpclinkstatus)
  - [VpcLinkVersion](#vpclinkversion)

## AuthorizationType

```python
from mypy_boto3_apigatewayv2.literals import AuthorizationType
```

Values:

- `AWS_IAM`
- `CUSTOM`
- `JWT`
- `NONE`

## AuthorizerType

```python
from mypy_boto3_apigatewayv2.literals import AuthorizerType
```

Values:

- `JWT`
- `REQUEST`

## ConnectionType

```python
from mypy_boto3_apigatewayv2.literals import ConnectionType
```

Values:

- `INTERNET`
- `VPC_LINK`

## ContentHandlingStrategy

```python
from mypy_boto3_apigatewayv2.literals import ContentHandlingStrategy
```

Values:

- `CONVERT_TO_BINARY`
- `CONVERT_TO_TEXT`

## DeploymentStatus

```python
from mypy_boto3_apigatewayv2.literals import DeploymentStatus
```

Values:

- `DEPLOYED`
- `FAILED`
- `PENDING`

## DomainNameStatus

```python
from mypy_boto3_apigatewayv2.literals import DomainNameStatus
```

Values:

- `AVAILABLE`
- `UPDATING`

## EndpointType

```python
from mypy_boto3_apigatewayv2.literals import EndpointType
```

Values:

- `EDGE`
- `REGIONAL`

## GetApisPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetApisPaginatorName
```

Values:

- `get_apis`

## GetAuthorizersPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetAuthorizersPaginatorName
```

Values:

- `get_authorizers`

## GetDeploymentsPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetDeploymentsPaginatorName
```

Values:

- `get_deployments`

## GetDomainNamesPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetDomainNamesPaginatorName
```

Values:

- `get_domain_names`

## GetIntegrationResponsesPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetIntegrationResponsesPaginatorName
```

Values:

- `get_integration_responses`

## GetIntegrationsPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetIntegrationsPaginatorName
```

Values:

- `get_integrations`

## GetModelsPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetModelsPaginatorName
```

Values:

- `get_models`

## GetRouteResponsesPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetRouteResponsesPaginatorName
```

Values:

- `get_route_responses`

## GetRoutesPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetRoutesPaginatorName
```

Values:

- `get_routes`

## GetStagesPaginatorName

```python
from mypy_boto3_apigatewayv2.literals import GetStagesPaginatorName
```

Values:

- `get_stages`

## IntegrationType

```python
from mypy_boto3_apigatewayv2.literals import IntegrationType
```

Values:

- `AWS`
- `AWS_PROXY`
- `HTTP`
- `HTTP_PROXY`
- `MOCK`

## JSONYAMLType

```python
from mypy_boto3_apigatewayv2.literals import JSONYAMLType
```

Values:

- `JSON`
- `YAML`

## LoggingLevel

```python
from mypy_boto3_apigatewayv2.literals import LoggingLevel
```

Values:

- `ERROR`
- `INFO`
- `OFF`

## OAS30Type

```python
from mypy_boto3_apigatewayv2.literals import OAS30Type
```

Values:

- `OAS30`

## PassthroughBehavior

```python
from mypy_boto3_apigatewayv2.literals import PassthroughBehavior
```

Values:

- `NEVER`
- `WHEN_NO_MATCH`
- `WHEN_NO_TEMPLATES`

## ProtocolType

```python
from mypy_boto3_apigatewayv2.literals import ProtocolType
```

Values:

- `HTTP`
- `WEBSOCKET`

## SecurityPolicy

```python
from mypy_boto3_apigatewayv2.literals import SecurityPolicy
```

Values:

- `TLS_1_0`
- `TLS_1_2`

## VpcLinkStatus

```python
from mypy_boto3_apigatewayv2.literals import VpcLinkStatus
```

Values:

- `AVAILABLE`
- `DELETING`
- `FAILED`
- `INACTIVE`
- `PENDING`

## VpcLinkVersion

```python
from mypy_boto3_apigatewayv2.literals import VpcLinkVersion
```

Values:

- `V2`
