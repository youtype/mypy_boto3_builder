# Type annotations for boto3 AppSync module

> [Index](../index.md) > AppSync

Auto-generated documentation for [AppSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync)
type annotations stubs module [mypy_boto3_appsync](https://pypi.org/project/mypy-boto3-appsync/).

```bash
pip install mypy-boto3-appsync
```

- [Type annotations for boto3 AppSync module](#type-annotations-for-boto3-appsync-module)
  - [AppSyncClient](#appsyncclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AppSyncClient

Type annotations for  `boto3.client("appsync")` as [AppSyncClient](./client.md)

Can be used directly:

```python
from mypy_boto3_appsync.client import AppSyncClient
```


AppSyncClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_api_cache](./client.md#create-api-cache)
- [create_api_key](./client.md#create-api-key)
- [create_data_source](./client.md#create-data-source)
- [create_function](./client.md#create-function)
- [create_graphql_api](./client.md#create-graphql-api)
- [create_resolver](./client.md#create-resolver)
- [create_type](./client.md#create-type)
- [delete_api_cache](./client.md#delete-api-cache)
- [delete_api_key](./client.md#delete-api-key)
- [delete_data_source](./client.md#delete-data-source)
- [delete_function](./client.md#delete-function)
- [delete_graphql_api](./client.md#delete-graphql-api)
- [delete_resolver](./client.md#delete-resolver)
- [delete_type](./client.md#delete-type)
- [flush_api_cache](./client.md#flush-api-cache)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_api_cache](./client.md#get-api-cache)
- [get_data_source](./client.md#get-data-source)
- [get_function](./client.md#get-function)
- [get_graphql_api](./client.md#get-graphql-api)
- [get_introspection_schema](./client.md#get-introspection-schema)
- [get_paginator](./client.md#get-paginator)
- [get_resolver](./client.md#get-resolver)
- [get_schema_creation_status](./client.md#get-schema-creation-status)
- [get_type](./client.md#get-type)
- [list_api_keys](./client.md#list-api-keys)
- [list_data_sources](./client.md#list-data-sources)
- [list_functions](./client.md#list-functions)
- [list_graphql_apis](./client.md#list-graphql-apis)
- [list_resolvers](./client.md#list-resolvers)
- [list_resolvers_by_function](./client.md#list-resolvers-by-function)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_types](./client.md#list-types)
- [start_schema_creation](./client.md#start-schema-creation)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_api_cache](./client.md#update-api-cache)
- [update_api_key](./client.md#update-api-key)
- [update_data_source](./client.md#update-data-source)
- [update_function](./client.md#update-function)
- [update_graphql_api](./client.md#update-graphql-api)
- [update_resolver](./client.md#update-resolver)
- [update_type](./client.md#update-type)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ApiKeyLimitExceededException](./client.md#apikeylimitexceededexception)
- [ApiKeyValidityOutOfBoundsException](./client.md#apikeyvalidityoutofboundsexception)
- [ApiLimitExceededException](./client.md#apilimitexceededexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [GraphQLSchemaException](./client.md#graphqlschemaexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("appsync").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListApiKeysPaginator, ...
```

- [ListApiKeysPaginator](./paginators.md#listapikeyspaginator)
- [ListDataSourcesPaginator](./paginators.md#listdatasourcespaginator)
- [ListFunctionsPaginator](./paginators.md#listfunctionspaginator)
- [ListGraphqlApisPaginator](./paginators.md#listgraphqlapispaginator)
- [ListResolversPaginator](./paginators.md#listresolverspaginator)
- [ListResolversByFunctionPaginator](./paginators.md#listresolversbyfunctionpaginator)
- [ListTypesPaginator](./paginators.md#listtypespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appsync.literals import ApiCacheStatus, ...
```

- [ApiCacheStatus](./literals.md#apicachestatus)
- [ApiCacheType](./literals.md#apicachetype)
- [ApiCachingBehavior](./literals.md#apicachingbehavior)
- [AuthenticationType](./literals.md#authenticationtype)
- [AuthorizationType](./literals.md#authorizationtype)
- [ConflictDetectionType](./literals.md#conflictdetectiontype)
- [ConflictHandlerType](./literals.md#conflicthandlertype)
- [DataSourceType](./literals.md#datasourcetype)
- [DefaultAction](./literals.md#defaultaction)
- [FieldLogLevel](./literals.md#fieldloglevel)
- [ListApiKeysPaginatorName](./literals.md#listapikeyspaginatorname)
- [ListDataSourcesPaginatorName](./literals.md#listdatasourcespaginatorname)
- [ListFunctionsPaginatorName](./literals.md#listfunctionspaginatorname)
- [ListGraphqlApisPaginatorName](./literals.md#listgraphqlapispaginatorname)
- [ListResolversByFunctionPaginatorName](./literals.md#listresolversbyfunctionpaginatorname)
- [ListResolversPaginatorName](./literals.md#listresolverspaginatorname)
- [ListTypesPaginatorName](./literals.md#listtypespaginatorname)
- [OutputType](./literals.md#outputtype)
- [RelationalDatabaseSourceType](./literals.md#relationaldatabasesourcetype)
- [ResolverKind](./literals.md#resolverkind)
- [SchemaStatus](./literals.md#schemastatus)
- [TypeDefinitionFormat](./literals.md#typedefinitionformat)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appsync.type_defs import AdditionalAuthenticationProviderTypeDef, ...
```

- [AdditionalAuthenticationProviderTypeDef](./type_defs.md#additionalauthenticationprovidertypedef)
- [ApiCacheTypeDef](./type_defs.md#apicachetypedef)
- [ApiKeyTypeDef](./type_defs.md#apikeytypedef)
- [AuthorizationConfigTypeDef](./type_defs.md#authorizationconfigtypedef)
- [AwsIamConfigTypeDef](./type_defs.md#awsiamconfigtypedef)
- [CachingConfigTypeDef](./type_defs.md#cachingconfigtypedef)
- [CognitoUserPoolConfigTypeDef](./type_defs.md#cognitouserpoolconfigtypedef)
- [CreateApiCacheResponseTypeDef](./type_defs.md#createapicacheresponsetypedef)
- [CreateApiKeyResponseTypeDef](./type_defs.md#createapikeyresponsetypedef)
- [CreateDataSourceResponseTypeDef](./type_defs.md#createdatasourceresponsetypedef)
- [CreateFunctionResponseTypeDef](./type_defs.md#createfunctionresponsetypedef)
- [CreateGraphqlApiResponseTypeDef](./type_defs.md#creategraphqlapiresponsetypedef)
- [CreateResolverResponseTypeDef](./type_defs.md#createresolverresponsetypedef)
- [CreateTypeResponseTypeDef](./type_defs.md#createtyperesponsetypedef)
- [DataSourceTypeDef](./type_defs.md#datasourcetypedef)
- [DeltaSyncConfigTypeDef](./type_defs.md#deltasyncconfigtypedef)
- [DynamodbDataSourceConfigTypeDef](./type_defs.md#dynamodbdatasourceconfigtypedef)
- [ElasticsearchDataSourceConfigTypeDef](./type_defs.md#elasticsearchdatasourceconfigtypedef)
- [FunctionConfigurationTypeDef](./type_defs.md#functionconfigurationtypedef)
- [GetApiCacheResponseTypeDef](./type_defs.md#getapicacheresponsetypedef)
- [GetDataSourceResponseTypeDef](./type_defs.md#getdatasourceresponsetypedef)
- [GetFunctionResponseTypeDef](./type_defs.md#getfunctionresponsetypedef)
- [GetGraphqlApiResponseTypeDef](./type_defs.md#getgraphqlapiresponsetypedef)
- [GetIntrospectionSchemaResponseTypeDef](./type_defs.md#getintrospectionschemaresponsetypedef)
- [GetResolverResponseTypeDef](./type_defs.md#getresolverresponsetypedef)
- [GetSchemaCreationStatusResponseTypeDef](./type_defs.md#getschemacreationstatusresponsetypedef)
- [GetTypeResponseTypeDef](./type_defs.md#gettyperesponsetypedef)
- [GraphqlApiTypeDef](./type_defs.md#graphqlapitypedef)
- [HttpDataSourceConfigTypeDef](./type_defs.md#httpdatasourceconfigtypedef)
- [LambdaConflictHandlerConfigTypeDef](./type_defs.md#lambdaconflicthandlerconfigtypedef)
- [LambdaDataSourceConfigTypeDef](./type_defs.md#lambdadatasourceconfigtypedef)
- [ListApiKeysResponseTypeDef](./type_defs.md#listapikeysresponsetypedef)
- [ListDataSourcesResponseTypeDef](./type_defs.md#listdatasourcesresponsetypedef)
- [ListFunctionsResponseTypeDef](./type_defs.md#listfunctionsresponsetypedef)
- [ListGraphqlApisResponseTypeDef](./type_defs.md#listgraphqlapisresponsetypedef)
- [ListResolversByFunctionResponseTypeDef](./type_defs.md#listresolversbyfunctionresponsetypedef)
- [ListResolversResponseTypeDef](./type_defs.md#listresolversresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTypesResponseTypeDef](./type_defs.md#listtypesresponsetypedef)
- [LogConfigTypeDef](./type_defs.md#logconfigtypedef)
- [OpenIDConnectConfigTypeDef](./type_defs.md#openidconnectconfigtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PipelineConfigTypeDef](./type_defs.md#pipelineconfigtypedef)
- [RdsHttpEndpointConfigTypeDef](./type_defs.md#rdshttpendpointconfigtypedef)
- [RelationalDatabaseDataSourceConfigTypeDef](./type_defs.md#relationaldatabasedatasourceconfigtypedef)
- [ResolverTypeDef](./type_defs.md#resolvertypedef)
- [StartSchemaCreationResponseTypeDef](./type_defs.md#startschemacreationresponsetypedef)
- [SyncConfigTypeDef](./type_defs.md#syncconfigtypedef)
- [TypeTypeDef](./type_defs.md#typetypedef)
- [UpdateApiCacheResponseTypeDef](./type_defs.md#updateapicacheresponsetypedef)
- [UpdateApiKeyResponseTypeDef](./type_defs.md#updateapikeyresponsetypedef)
- [UpdateDataSourceResponseTypeDef](./type_defs.md#updatedatasourceresponsetypedef)
- [UpdateFunctionResponseTypeDef](./type_defs.md#updatefunctionresponsetypedef)
- [UpdateGraphqlApiResponseTypeDef](./type_defs.md#updategraphqlapiresponsetypedef)
- [UpdateResolverResponseTypeDef](./type_defs.md#updateresolverresponsetypedef)
- [UpdateTypeResponseTypeDef](./type_defs.md#updatetyperesponsetypedef)
- [UserPoolConfigTypeDef](./type_defs.md#userpoolconfigtypedef)
