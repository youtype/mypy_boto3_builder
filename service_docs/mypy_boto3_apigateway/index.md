# Type annotations for boto3 APIGateway module

> [Index](../index.md) > APIGateway

Auto-generated documentation for [APIGateway](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway)
type annotations stubs module [mypy_boto3_apigateway](https://pypi.org/project/mypy-boto3-apigateway/).

```bash
pip install mypy-boto3-apigateway
```

- [Type annotations for boto3 APIGateway module](#type-annotations-for-boto3-apigateway-module)
  - [APIGatewayClient](#apigatewayclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## APIGatewayClient

Type annotations for  `boto3.client("apigateway")` as [APIGatewayClient](./client.md)

Can be used directly:

```python
from mypy_boto3_apigateway.client import APIGatewayClient
```


APIGatewayClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_api_key](./client.md#create-api-key)
- [create_authorizer](./client.md#create-authorizer)
- [create_base_path_mapping](./client.md#create-base-path-mapping)
- [create_deployment](./client.md#create-deployment)
- [create_documentation_part](./client.md#create-documentation-part)
- [create_documentation_version](./client.md#create-documentation-version)
- [create_domain_name](./client.md#create-domain-name)
- [create_model](./client.md#create-model)
- [create_request_validator](./client.md#create-request-validator)
- [create_resource](./client.md#create-resource)
- [create_rest_api](./client.md#create-rest-api)
- [create_stage](./client.md#create-stage)
- [create_usage_plan](./client.md#create-usage-plan)
- [create_usage_plan_key](./client.md#create-usage-plan-key)
- [create_vpc_link](./client.md#create-vpc-link)
- [delete_api_key](./client.md#delete-api-key)
- [delete_authorizer](./client.md#delete-authorizer)
- [delete_base_path_mapping](./client.md#delete-base-path-mapping)
- [delete_client_certificate](./client.md#delete-client-certificate)
- [delete_deployment](./client.md#delete-deployment)
- [delete_documentation_part](./client.md#delete-documentation-part)
- [delete_documentation_version](./client.md#delete-documentation-version)
- [delete_domain_name](./client.md#delete-domain-name)
- [delete_gateway_response](./client.md#delete-gateway-response)
- [delete_integration](./client.md#delete-integration)
- [delete_integration_response](./client.md#delete-integration-response)
- [delete_method](./client.md#delete-method)
- [delete_method_response](./client.md#delete-method-response)
- [delete_model](./client.md#delete-model)
- [delete_request_validator](./client.md#delete-request-validator)
- [delete_resource](./client.md#delete-resource)
- [delete_rest_api](./client.md#delete-rest-api)
- [delete_stage](./client.md#delete-stage)
- [delete_usage_plan](./client.md#delete-usage-plan)
- [delete_usage_plan_key](./client.md#delete-usage-plan-key)
- [delete_vpc_link](./client.md#delete-vpc-link)
- [flush_stage_authorizers_cache](./client.md#flush-stage-authorizers-cache)
- [flush_stage_cache](./client.md#flush-stage-cache)
- [generate_client_certificate](./client.md#generate-client-certificate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account](./client.md#get-account)
- [get_api_key](./client.md#get-api-key)
- [get_api_keys](./client.md#get-api-keys)
- [get_authorizer](./client.md#get-authorizer)
- [get_authorizers](./client.md#get-authorizers)
- [get_base_path_mapping](./client.md#get-base-path-mapping)
- [get_base_path_mappings](./client.md#get-base-path-mappings)
- [get_client_certificate](./client.md#get-client-certificate)
- [get_client_certificates](./client.md#get-client-certificates)
- [get_deployment](./client.md#get-deployment)
- [get_deployments](./client.md#get-deployments)
- [get_documentation_part](./client.md#get-documentation-part)
- [get_documentation_parts](./client.md#get-documentation-parts)
- [get_documentation_version](./client.md#get-documentation-version)
- [get_documentation_versions](./client.md#get-documentation-versions)
- [get_domain_name](./client.md#get-domain-name)
- [get_domain_names](./client.md#get-domain-names)
- [get_export](./client.md#get-export)
- [get_gateway_response](./client.md#get-gateway-response)
- [get_gateway_responses](./client.md#get-gateway-responses)
- [get_integration](./client.md#get-integration)
- [get_integration_response](./client.md#get-integration-response)
- [get_method](./client.md#get-method)
- [get_method_response](./client.md#get-method-response)
- [get_model](./client.md#get-model)
- [get_model_template](./client.md#get-model-template)
- [get_models](./client.md#get-models)
- [get_paginator](./client.md#get-paginator)
- [get_request_validator](./client.md#get-request-validator)
- [get_request_validators](./client.md#get-request-validators)
- [get_resource](./client.md#get-resource)
- [get_resources](./client.md#get-resources)
- [get_rest_api](./client.md#get-rest-api)
- [get_rest_apis](./client.md#get-rest-apis)
- [get_sdk](./client.md#get-sdk)
- [get_sdk_type](./client.md#get-sdk-type)
- [get_sdk_types](./client.md#get-sdk-types)
- [get_stage](./client.md#get-stage)
- [get_stages](./client.md#get-stages)
- [get_tags](./client.md#get-tags)
- [get_usage](./client.md#get-usage)
- [get_usage_plan](./client.md#get-usage-plan)
- [get_usage_plan_key](./client.md#get-usage-plan-key)
- [get_usage_plan_keys](./client.md#get-usage-plan-keys)
- [get_usage_plans](./client.md#get-usage-plans)
- [get_vpc_link](./client.md#get-vpc-link)
- [get_vpc_links](./client.md#get-vpc-links)
- [import_api_keys](./client.md#import-api-keys)
- [import_documentation_parts](./client.md#import-documentation-parts)
- [import_rest_api](./client.md#import-rest-api)
- [put_gateway_response](./client.md#put-gateway-response)
- [put_integration](./client.md#put-integration)
- [put_integration_response](./client.md#put-integration-response)
- [put_method](./client.md#put-method)
- [put_method_response](./client.md#put-method-response)
- [put_rest_api](./client.md#put-rest-api)
- [tag_resource](./client.md#tag-resource)
- [test_invoke_authorizer](./client.md#test-invoke-authorizer)
- [test_invoke_method](./client.md#test-invoke-method)
- [untag_resource](./client.md#untag-resource)
- [update_account](./client.md#update-account)
- [update_api_key](./client.md#update-api-key)
- [update_authorizer](./client.md#update-authorizer)
- [update_base_path_mapping](./client.md#update-base-path-mapping)
- [update_client_certificate](./client.md#update-client-certificate)
- [update_deployment](./client.md#update-deployment)
- [update_documentation_part](./client.md#update-documentation-part)
- [update_documentation_version](./client.md#update-documentation-version)
- [update_domain_name](./client.md#update-domain-name)
- [update_gateway_response](./client.md#update-gateway-response)
- [update_integration](./client.md#update-integration)
- [update_integration_response](./client.md#update-integration-response)
- [update_method](./client.md#update-method)
- [update_method_response](./client.md#update-method-response)
- [update_model](./client.md#update-model)
- [update_request_validator](./client.md#update-request-validator)
- [update_resource](./client.md#update-resource)
- [update_rest_api](./client.md#update-rest-api)
- [update_stage](./client.md#update-stage)
- [update_usage](./client.md#update-usage)
- [update_usage_plan](./client.md#update-usage-plan)
- [update_vpc_link](./client.md#update-vpc-link)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("apigateway").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_apigateway.paginators import GetApiKeysPaginator, ...
```

- [GetApiKeysPaginator](./paginators.md#getapikeyspaginator)
- [GetAuthorizersPaginator](./paginators.md#getauthorizerspaginator)
- [GetBasePathMappingsPaginator](./paginators.md#getbasepathmappingspaginator)
- [GetClientCertificatesPaginator](./paginators.md#getclientcertificatespaginator)
- [GetDeploymentsPaginator](./paginators.md#getdeploymentspaginator)
- [GetDocumentationPartsPaginator](./paginators.md#getdocumentationpartspaginator)
- [GetDocumentationVersionsPaginator](./paginators.md#getdocumentationversionspaginator)
- [GetDomainNamesPaginator](./paginators.md#getdomainnamespaginator)
- [GetGatewayResponsesPaginator](./paginators.md#getgatewayresponsespaginator)
- [GetModelsPaginator](./paginators.md#getmodelspaginator)
- [GetRequestValidatorsPaginator](./paginators.md#getrequestvalidatorspaginator)
- [GetResourcesPaginator](./paginators.md#getresourcespaginator)
- [GetRestApisPaginator](./paginators.md#getrestapispaginator)
- [GetSdkTypesPaginator](./paginators.md#getsdktypespaginator)
- [GetUsagePaginator](./paginators.md#getusagepaginator)
- [GetUsagePlanKeysPaginator](./paginators.md#getusageplankeyspaginator)
- [GetUsagePlansPaginator](./paginators.md#getusageplanspaginator)
- [GetVpcLinksPaginator](./paginators.md#getvpclinkspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_apigateway.literals import ApiKeySourceType, ...
```

- [ApiKeySourceType](./literals.md#apikeysourcetype)
- [ApiKeysFormat](./literals.md#apikeysformat)
- [AuthorizerType](./literals.md#authorizertype)
- [CacheClusterSize](./literals.md#cacheclustersize)
- [CacheClusterStatus](./literals.md#cacheclusterstatus)
- [ConnectionType](./literals.md#connectiontype)
- [ContentHandlingStrategy](./literals.md#contenthandlingstrategy)
- [DocumentationPartType](./literals.md#documentationparttype)
- [DomainNameStatus](./literals.md#domainnamestatus)
- [EndpointType](./literals.md#endpointtype)
- [GatewayResponseType](./literals.md#gatewayresponsetype)
- [GetApiKeysPaginatorName](./literals.md#getapikeyspaginatorname)
- [GetAuthorizersPaginatorName](./literals.md#getauthorizerspaginatorname)
- [GetBasePathMappingsPaginatorName](./literals.md#getbasepathmappingspaginatorname)
- [GetClientCertificatesPaginatorName](./literals.md#getclientcertificatespaginatorname)
- [GetDeploymentsPaginatorName](./literals.md#getdeploymentspaginatorname)
- [GetDocumentationPartsPaginatorName](./literals.md#getdocumentationpartspaginatorname)
- [GetDocumentationVersionsPaginatorName](./literals.md#getdocumentationversionspaginatorname)
- [GetDomainNamesPaginatorName](./literals.md#getdomainnamespaginatorname)
- [GetGatewayResponsesPaginatorName](./literals.md#getgatewayresponsespaginatorname)
- [GetModelsPaginatorName](./literals.md#getmodelspaginatorname)
- [GetRequestValidatorsPaginatorName](./literals.md#getrequestvalidatorspaginatorname)
- [GetResourcesPaginatorName](./literals.md#getresourcespaginatorname)
- [GetRestApisPaginatorName](./literals.md#getrestapispaginatorname)
- [GetSdkTypesPaginatorName](./literals.md#getsdktypespaginatorname)
- [GetUsagePaginatorName](./literals.md#getusagepaginatorname)
- [GetUsagePlanKeysPaginatorName](./literals.md#getusageplankeyspaginatorname)
- [GetUsagePlansPaginatorName](./literals.md#getusageplanspaginatorname)
- [GetVpcLinksPaginatorName](./literals.md#getvpclinkspaginatorname)
- [IntegrationType](./literals.md#integrationtype)
- [LocationStatusType](./literals.md#locationstatustype)
- [Op](./literals.md#op)
- [PutMode](./literals.md#putmode)
- [QuotaPeriodType](./literals.md#quotaperiodtype)
- [SecurityPolicy](./literals.md#securitypolicy)
- [UnauthorizedCacheControlHeaderStrategy](./literals.md#unauthorizedcachecontrolheaderstrategy)
- [VpcLinkStatus](./literals.md#vpclinkstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef, ...
```

- [AccessLogSettingsTypeDef](./type_defs.md#accesslogsettingstypedef)
- [AccountTypeDef](./type_defs.md#accounttypedef)
- [ApiKeyIdsTypeDef](./type_defs.md#apikeyidstypedef)
- [ApiKeyTypeDef](./type_defs.md#apikeytypedef)
- [ApiKeysTypeDef](./type_defs.md#apikeystypedef)
- [ApiStageTypeDef](./type_defs.md#apistagetypedef)
- [AuthorizerTypeDef](./type_defs.md#authorizertypedef)
- [AuthorizersTypeDef](./type_defs.md#authorizerstypedef)
- [BasePathMappingTypeDef](./type_defs.md#basepathmappingtypedef)
- [BasePathMappingsTypeDef](./type_defs.md#basepathmappingstypedef)
- [CanarySettingsTypeDef](./type_defs.md#canarysettingstypedef)
- [ClientCertificateTypeDef](./type_defs.md#clientcertificatetypedef)
- [ClientCertificatesTypeDef](./type_defs.md#clientcertificatestypedef)
- [DeploymentCanarySettingsTypeDef](./type_defs.md#deploymentcanarysettingstypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DeploymentsTypeDef](./type_defs.md#deploymentstypedef)
- [DocumentationPartIdsTypeDef](./type_defs.md#documentationpartidstypedef)
- [DocumentationPartLocationTypeDef](./type_defs.md#documentationpartlocationtypedef)
- [DocumentationPartTypeDef](./type_defs.md#documentationparttypedef)
- [DocumentationPartsTypeDef](./type_defs.md#documentationpartstypedef)
- [DocumentationVersionTypeDef](./type_defs.md#documentationversiontypedef)
- [DocumentationVersionsTypeDef](./type_defs.md#documentationversionstypedef)
- [DomainNameTypeDef](./type_defs.md#domainnametypedef)
- [DomainNamesTypeDef](./type_defs.md#domainnamestypedef)
- [EndpointConfigurationTypeDef](./type_defs.md#endpointconfigurationtypedef)
- [ExportResponseTypeDef](./type_defs.md#exportresponsetypedef)
- [GatewayResponseTypeDef](./type_defs.md#gatewayresponsetypedef)
- [GatewayResponsesTypeDef](./type_defs.md#gatewayresponsestypedef)
- [IntegrationResponseTypeDef](./type_defs.md#integrationresponsetypedef)
- [IntegrationTypeDef](./type_defs.md#integrationtypedef)
- [MethodResponseTypeDef](./type_defs.md#methodresponsetypedef)
- [MethodSettingTypeDef](./type_defs.md#methodsettingtypedef)
- [MethodSnapshotTypeDef](./type_defs.md#methodsnapshottypedef)
- [MethodTypeDef](./type_defs.md#methodtypedef)
- [ModelTypeDef](./type_defs.md#modeltypedef)
- [ModelsTypeDef](./type_defs.md#modelstypedef)
- [MutualTlsAuthenticationInputTypeDef](./type_defs.md#mutualtlsauthenticationinputtypedef)
- [MutualTlsAuthenticationTypeDef](./type_defs.md#mutualtlsauthenticationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PatchOperationTypeDef](./type_defs.md#patchoperationtypedef)
- [QuotaSettingsTypeDef](./type_defs.md#quotasettingstypedef)
- [RequestValidatorTypeDef](./type_defs.md#requestvalidatortypedef)
- [RequestValidatorsTypeDef](./type_defs.md#requestvalidatorstypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [ResourcesTypeDef](./type_defs.md#resourcestypedef)
- [RestApiTypeDef](./type_defs.md#restapitypedef)
- [RestApisTypeDef](./type_defs.md#restapistypedef)
- [SdkConfigurationPropertyTypeDef](./type_defs.md#sdkconfigurationpropertytypedef)
- [SdkResponseTypeDef](./type_defs.md#sdkresponsetypedef)
- [SdkTypeTypeDef](./type_defs.md#sdktypetypedef)
- [SdkTypesTypeDef](./type_defs.md#sdktypestypedef)
- [StageKeyTypeDef](./type_defs.md#stagekeytypedef)
- [StageTypeDef](./type_defs.md#stagetypedef)
- [StagesTypeDef](./type_defs.md#stagestypedef)
- [TagsTypeDef](./type_defs.md#tagstypedef)
- [TemplateTypeDef](./type_defs.md#templatetypedef)
- [TestInvokeAuthorizerResponseTypeDef](./type_defs.md#testinvokeauthorizerresponsetypedef)
- [TestInvokeMethodResponseTypeDef](./type_defs.md#testinvokemethodresponsetypedef)
- [ThrottleSettingsTypeDef](./type_defs.md#throttlesettingstypedef)
- [TlsConfigTypeDef](./type_defs.md#tlsconfigtypedef)
- [UsagePlanKeyTypeDef](./type_defs.md#usageplankeytypedef)
- [UsagePlanKeysTypeDef](./type_defs.md#usageplankeystypedef)
- [UsagePlanTypeDef](./type_defs.md#usageplantypedef)
- [UsagePlansTypeDef](./type_defs.md#usageplanstypedef)
- [UsageTypeDef](./type_defs.md#usagetypedef)
- [VpcLinkTypeDef](./type_defs.md#vpclinktypedef)
- [VpcLinksTypeDef](./type_defs.md#vpclinkstypedef)
