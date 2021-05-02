# Type annotations for boto3 ApiGatewayV2 module

> [Index](../index.md) > ApiGatewayV2

Auto-generated documentation for [ApiGatewayV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html#ApiGatewayV2)
type annotations stubs module [mypy_boto3_apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/).

```bash
pip install mypy-boto3-apigatewayv2
```

- [Type annotations for boto3 ApiGatewayV2 module](#type-annotations-for-boto3-apigatewayv2-module)
  - [ApiGatewayV2Client](#apigatewayv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ApiGatewayV2Client

Type annotations for  `boto3.client("apigatewayv2")` as [ApiGatewayV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_apigatewayv2.client import ApiGatewayV2Client
```


ApiGatewayV2Client [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_api](./client.md#create-api)
- [create_api_mapping](./client.md#create-api-mapping)
- [create_authorizer](./client.md#create-authorizer)
- [create_deployment](./client.md#create-deployment)
- [create_domain_name](./client.md#create-domain-name)
- [create_integration](./client.md#create-integration)
- [create_integration_response](./client.md#create-integration-response)
- [create_model](./client.md#create-model)
- [create_route](./client.md#create-route)
- [create_route_response](./client.md#create-route-response)
- [create_stage](./client.md#create-stage)
- [create_vpc_link](./client.md#create-vpc-link)
- [delete_access_log_settings](./client.md#delete-access-log-settings)
- [delete_api](./client.md#delete-api)
- [delete_api_mapping](./client.md#delete-api-mapping)
- [delete_authorizer](./client.md#delete-authorizer)
- [delete_cors_configuration](./client.md#delete-cors-configuration)
- [delete_deployment](./client.md#delete-deployment)
- [delete_domain_name](./client.md#delete-domain-name)
- [delete_integration](./client.md#delete-integration)
- [delete_integration_response](./client.md#delete-integration-response)
- [delete_model](./client.md#delete-model)
- [delete_route](./client.md#delete-route)
- [delete_route_request_parameter](./client.md#delete-route-request-parameter)
- [delete_route_response](./client.md#delete-route-response)
- [delete_route_settings](./client.md#delete-route-settings)
- [delete_stage](./client.md#delete-stage)
- [delete_vpc_link](./client.md#delete-vpc-link)
- [export_api](./client.md#export-api)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_api](./client.md#get-api)
- [get_api_mapping](./client.md#get-api-mapping)
- [get_api_mappings](./client.md#get-api-mappings)
- [get_apis](./client.md#get-apis)
- [get_authorizer](./client.md#get-authorizer)
- [get_authorizers](./client.md#get-authorizers)
- [get_deployment](./client.md#get-deployment)
- [get_deployments](./client.md#get-deployments)
- [get_domain_name](./client.md#get-domain-name)
- [get_domain_names](./client.md#get-domain-names)
- [get_integration](./client.md#get-integration)
- [get_integration_response](./client.md#get-integration-response)
- [get_integration_responses](./client.md#get-integration-responses)
- [get_integrations](./client.md#get-integrations)
- [get_model](./client.md#get-model)
- [get_model_template](./client.md#get-model-template)
- [get_models](./client.md#get-models)
- [get_paginator](./client.md#get-paginator)
- [get_route](./client.md#get-route)
- [get_route_response](./client.md#get-route-response)
- [get_route_responses](./client.md#get-route-responses)
- [get_routes](./client.md#get-routes)
- [get_stage](./client.md#get-stage)
- [get_stages](./client.md#get-stages)
- [get_tags](./client.md#get-tags)
- [get_vpc_link](./client.md#get-vpc-link)
- [get_vpc_links](./client.md#get-vpc-links)
- [import_api](./client.md#import-api)
- [reimport_api](./client.md#reimport-api)
- [reset_authorizers_cache](./client.md#reset-authorizers-cache)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_api](./client.md#update-api)
- [update_api_mapping](./client.md#update-api-mapping)
- [update_authorizer](./client.md#update-authorizer)
- [update_deployment](./client.md#update-deployment)
- [update_domain_name](./client.md#update-domain-name)
- [update_integration](./client.md#update-integration)
- [update_integration_response](./client.md#update-integration-response)
- [update_model](./client.md#update-model)
- [update_route](./client.md#update-route)
- [update_route_response](./client.md#update-route-response)
- [update_stage](./client.md#update-stage)
- [update_vpc_link](./client.md#update-vpc-link)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("apigatewayv2").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.paginators import GetApisPaginator, ...
```

- [GetApisPaginator](./paginators.md#getapispaginator)
- [GetAuthorizersPaginator](./paginators.md#getauthorizerspaginator)
- [GetDeploymentsPaginator](./paginators.md#getdeploymentspaginator)
- [GetDomainNamesPaginator](./paginators.md#getdomainnamespaginator)
- [GetIntegrationResponsesPaginator](./paginators.md#getintegrationresponsespaginator)
- [GetIntegrationsPaginator](./paginators.md#getintegrationspaginator)
- [GetModelsPaginator](./paginators.md#getmodelspaginator)
- [GetRouteResponsesPaginator](./paginators.md#getrouteresponsespaginator)
- [GetRoutesPaginator](./paginators.md#getroutespaginator)
- [GetStagesPaginator](./paginators.md#getstagespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.literals import AuthorizationType, ...
```

- [AuthorizationType](./literals.md#authorizationtype)
- [AuthorizerType](./literals.md#authorizertype)
- [ConnectionType](./literals.md#connectiontype)
- [ContentHandlingStrategy](./literals.md#contenthandlingstrategy)
- [DeploymentStatus](./literals.md#deploymentstatus)
- [DomainNameStatus](./literals.md#domainnamestatus)
- [EndpointType](./literals.md#endpointtype)
- [GetApisPaginatorName](./literals.md#getapispaginatorname)
- [GetAuthorizersPaginatorName](./literals.md#getauthorizerspaginatorname)
- [GetDeploymentsPaginatorName](./literals.md#getdeploymentspaginatorname)
- [GetDomainNamesPaginatorName](./literals.md#getdomainnamespaginatorname)
- [GetIntegrationResponsesPaginatorName](./literals.md#getintegrationresponsespaginatorname)
- [GetIntegrationsPaginatorName](./literals.md#getintegrationspaginatorname)
- [GetModelsPaginatorName](./literals.md#getmodelspaginatorname)
- [GetRouteResponsesPaginatorName](./literals.md#getrouteresponsespaginatorname)
- [GetRoutesPaginatorName](./literals.md#getroutespaginatorname)
- [GetStagesPaginatorName](./literals.md#getstagespaginatorname)
- [IntegrationType](./literals.md#integrationtype)
- [LoggingLevel](./literals.md#logginglevel)
- [PassthroughBehavior](./literals.md#passthroughbehavior)
- [ProtocolType](./literals.md#protocoltype)
- [SecurityPolicy](./literals.md#securitypolicy)
- [VpcLinkStatus](./literals.md#vpclinkstatus)
- [VpcLinkVersion](./literals.md#vpclinkversion)
- [__string](./literals.md#--string)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_apigatewayv2.type_defs import AccessLogSettingsTypeDef, ...
```

- [AccessLogSettingsTypeDef](./type_defs.md#accesslogsettingstypedef)
- [ApiMappingTypeDef](./type_defs.md#apimappingtypedef)
- [ApiTypeDef](./type_defs.md#apitypedef)
- [AuthorizerTypeDef](./type_defs.md#authorizertypedef)
- [CorsTypeDef](./type_defs.md#corstypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DomainNameConfigurationTypeDef](./type_defs.md#domainnameconfigurationtypedef)
- [DomainNameTypeDef](./type_defs.md#domainnametypedef)
- [IntegrationResponseTypeDef](./type_defs.md#integrationresponsetypedef)
- [IntegrationTypeDef](./type_defs.md#integrationtypedef)
- [JWTConfigurationTypeDef](./type_defs.md#jwtconfigurationtypedef)
- [ModelTypeDef](./type_defs.md#modeltypedef)
- [MutualTlsAuthenticationTypeDef](./type_defs.md#mutualtlsauthenticationtypedef)
- [ParameterConstraintsTypeDef](./type_defs.md#parameterconstraintstypedef)
- [RouteResponseTypeDef](./type_defs.md#routeresponsetypedef)
- [RouteSettingsTypeDef](./type_defs.md#routesettingstypedef)
- [RouteTypeDef](./type_defs.md#routetypedef)
- [StageTypeDef](./type_defs.md#stagetypedef)
- [TlsConfigTypeDef](./type_defs.md#tlsconfigtypedef)
- [VpcLinkTypeDef](./type_defs.md#vpclinktypedef)
- [CreateApiMappingResponseTypeDef](./type_defs.md#createapimappingresponsetypedef)
- [CreateApiResponseTypeDef](./type_defs.md#createapiresponsetypedef)
- [CreateAuthorizerResponseTypeDef](./type_defs.md#createauthorizerresponsetypedef)
- [CreateDeploymentResponseTypeDef](./type_defs.md#createdeploymentresponsetypedef)
- [CreateDomainNameResponseTypeDef](./type_defs.md#createdomainnameresponsetypedef)
- [CreateIntegrationResponseResponseTypeDef](./type_defs.md#createintegrationresponseresponsetypedef)
- [CreateIntegrationResultTypeDef](./type_defs.md#createintegrationresulttypedef)
- [CreateModelResponseTypeDef](./type_defs.md#createmodelresponsetypedef)
- [CreateRouteResponseResponseTypeDef](./type_defs.md#createrouteresponseresponsetypedef)
- [CreateRouteResultTypeDef](./type_defs.md#createrouteresulttypedef)
- [CreateStageResponseTypeDef](./type_defs.md#createstageresponsetypedef)
- [CreateVpcLinkResponseTypeDef](./type_defs.md#createvpclinkresponsetypedef)
- [ExportApiResponseTypeDef](./type_defs.md#exportapiresponsetypedef)
- [GetApiMappingResponseTypeDef](./type_defs.md#getapimappingresponsetypedef)
- [GetApiMappingsResponseTypeDef](./type_defs.md#getapimappingsresponsetypedef)
- [GetApiResponseTypeDef](./type_defs.md#getapiresponsetypedef)
- [GetApisResponseTypeDef](./type_defs.md#getapisresponsetypedef)
- [GetAuthorizerResponseTypeDef](./type_defs.md#getauthorizerresponsetypedef)
- [GetAuthorizersResponseTypeDef](./type_defs.md#getauthorizersresponsetypedef)
- [GetDeploymentResponseTypeDef](./type_defs.md#getdeploymentresponsetypedef)
- [GetDeploymentsResponseTypeDef](./type_defs.md#getdeploymentsresponsetypedef)
- [GetDomainNameResponseTypeDef](./type_defs.md#getdomainnameresponsetypedef)
- [GetDomainNamesResponseTypeDef](./type_defs.md#getdomainnamesresponsetypedef)
- [GetIntegrationResponseResponseTypeDef](./type_defs.md#getintegrationresponseresponsetypedef)
- [GetIntegrationResponsesResponseTypeDef](./type_defs.md#getintegrationresponsesresponsetypedef)
- [GetIntegrationResultTypeDef](./type_defs.md#getintegrationresulttypedef)
- [GetIntegrationsResponseTypeDef](./type_defs.md#getintegrationsresponsetypedef)
- [GetModelResponseTypeDef](./type_defs.md#getmodelresponsetypedef)
- [GetModelTemplateResponseTypeDef](./type_defs.md#getmodeltemplateresponsetypedef)
- [GetModelsResponseTypeDef](./type_defs.md#getmodelsresponsetypedef)
- [GetRouteResponseResponseTypeDef](./type_defs.md#getrouteresponseresponsetypedef)
- [GetRouteResponsesResponseTypeDef](./type_defs.md#getrouteresponsesresponsetypedef)
- [GetRouteResultTypeDef](./type_defs.md#getrouteresulttypedef)
- [GetRoutesResponseTypeDef](./type_defs.md#getroutesresponsetypedef)
- [GetStageResponseTypeDef](./type_defs.md#getstageresponsetypedef)
- [GetStagesResponseTypeDef](./type_defs.md#getstagesresponsetypedef)
- [GetTagsResponseTypeDef](./type_defs.md#gettagsresponsetypedef)
- [GetVpcLinkResponseTypeDef](./type_defs.md#getvpclinkresponsetypedef)
- [GetVpcLinksResponseTypeDef](./type_defs.md#getvpclinksresponsetypedef)
- [ImportApiResponseTypeDef](./type_defs.md#importapiresponsetypedef)
- [MutualTlsAuthenticationInputTypeDef](./type_defs.md#mutualtlsauthenticationinputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ReimportApiResponseTypeDef](./type_defs.md#reimportapiresponsetypedef)
- [TlsConfigInputTypeDef](./type_defs.md#tlsconfiginputtypedef)
- [UpdateApiMappingResponseTypeDef](./type_defs.md#updateapimappingresponsetypedef)
- [UpdateApiResponseTypeDef](./type_defs.md#updateapiresponsetypedef)
- [UpdateAuthorizerResponseTypeDef](./type_defs.md#updateauthorizerresponsetypedef)
- [UpdateDeploymentResponseTypeDef](./type_defs.md#updatedeploymentresponsetypedef)
- [UpdateDomainNameResponseTypeDef](./type_defs.md#updatedomainnameresponsetypedef)
- [UpdateIntegrationResponseResponseTypeDef](./type_defs.md#updateintegrationresponseresponsetypedef)
- [UpdateIntegrationResultTypeDef](./type_defs.md#updateintegrationresulttypedef)
- [UpdateModelResponseTypeDef](./type_defs.md#updatemodelresponsetypedef)
- [UpdateRouteResponseResponseTypeDef](./type_defs.md#updaterouteresponseresponsetypedef)
- [UpdateRouteResultTypeDef](./type_defs.md#updaterouteresulttypedef)
- [UpdateStageResponseTypeDef](./type_defs.md#updatestageresponsetypedef)
- [UpdateVpcLinkResponseTypeDef](./type_defs.md#updatevpclinkresponsetypedef)
