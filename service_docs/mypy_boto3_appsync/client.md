# AppSyncClient for boto3 AppSync module

> [Index](../index.md) > [AppSync](./index.md) > AppSyncClient

Auto-generated documentation for [AppSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync)
type annotations stubs module [mypy_boto3_appsync](https://pypi.org/project/mypy-boto3-appsync/).

- [AppSyncClient for boto3 AppSync module](#appsyncclient-for-boto3-appsync-module)
  - [AppSyncClient](#appsyncclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_api_cache](#create_api_cache)
    - [create_api_key](#create_api_key)
    - [create_data_source](#create_data_source)
    - [create_function](#create_function)
    - [create_graphql_api](#create_graphql_api)
    - [create_resolver](#create_resolver)
    - [create_type](#create_type)
    - [delete_api_cache](#delete_api_cache)
    - [delete_api_key](#delete_api_key)
    - [delete_data_source](#delete_data_source)
    - [delete_function](#delete_function)
    - [delete_graphql_api](#delete_graphql_api)
    - [delete_resolver](#delete_resolver)
    - [delete_type](#delete_type)
    - [flush_api_cache](#flush_api_cache)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_api_cache](#get_api_cache)
    - [get_data_source](#get_data_source)
    - [get_function](#get_function)
    - [get_graphql_api](#get_graphql_api)
    - [get_introspection_schema](#get_introspection_schema)
    - [get_resolver](#get_resolver)
    - [get_schema_creation_status](#get_schema_creation_status)
    - [get_type](#get_type)
    - [list_api_keys](#list_api_keys)
    - [list_data_sources](#list_data_sources)
    - [list_functions](#list_functions)
    - [list_graphql_apis](#list_graphql_apis)
    - [list_resolvers](#list_resolvers)
    - [list_resolvers_by_function](#list_resolvers_by_function)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_types](#list_types)
    - [start_schema_creation](#start_schema_creation)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_api_cache](#update_api_cache)
    - [update_api_key](#update_api_key)
    - [update_data_source](#update_data_source)
    - [update_function](#update_function)
    - [update_graphql_api](#update_graphql_api)
    - [update_resolver](#update_resolver)
    - [update_type](#update_type)
    - [get_paginator](#get_paginator)

## AppSyncClient

Type annotations for `boto3.client("appsync")`

Can be used directly:

```python
from mypy_boto3_appsync.client import AppSyncClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_appsync.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ApiKeyLimitExceededException`
- `Exceptions.ApiKeyValidityOutOfBoundsException`
- `Exceptions.ApiLimitExceededException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.GraphQLSchemaException`
- `Exceptions.InternalFailureException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("appsync").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_api_cache

Type annotations for `boto3.client("appsync").create_api_cache` method.

[Client.create_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_api_cache)

```python
def create_api_cache(
    self,
    apiId: str,
    ttl: int,
    apiCachingBehavior: ApiCachingBehavior,
    type: ApiCacheType,
    transitEncryptionEnabled: bool = None,
    atRestEncryptionEnabled: bool = None
) -> CreateApiCacheResponseTypeDef:
    pass
```

### create_api_key

Type annotations for `boto3.client("appsync").create_api_key` method.

[Client.create_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_api_key)

```python
def create_api_key(
    self,
    apiId: str,
    description: str = None,
    expires: int = None
) -> CreateApiKeyResponseTypeDef:
    pass
```

### create_data_source

Type annotations for `boto3.client("appsync").create_data_source` method.

[Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_data_source)

```python
def create_data_source(
    self,
    apiId: str,
    name: str,
    type: DataSourceType,
    description: str = None,
    serviceRoleArn: str = None,
    dynamodbConfig: "DynamodbDataSourceConfigTypeDef" = None,
    lambdaConfig: "LambdaDataSourceConfigTypeDef" = None,
    elasticsearchConfig: "ElasticsearchDataSourceConfigTypeDef" = None,
    httpConfig: "HttpDataSourceConfigTypeDef" = None,
    relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None
) -> CreateDataSourceResponseTypeDef:
    pass
```

### create_function

Type annotations for `boto3.client("appsync").create_function` method.

[Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_function)

```python
def create_function(
    self,
    apiId: str,
    name: str,
    dataSourceName: str,
    functionVersion: str,
    description: str = None,
    requestMappingTemplate: str = None,
    responseMappingTemplate: str = None,
    syncConfig: "SyncConfigTypeDef" = None
) -> CreateFunctionResponseTypeDef:
    pass
```

### create_graphql_api

Type annotations for `boto3.client("appsync").create_graphql_api` method.

[Client.create_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_graphql_api)

```python
def create_graphql_api(
    self,
    name: str,
    authenticationType: AuthenticationType,
    logConfig: "LogConfigTypeDef" = None,
    userPoolConfig: "UserPoolConfigTypeDef" = None,
    openIDConnectConfig: "OpenIDConnectConfigTypeDef" = None,
    tags: Dict[str, str] = None,
    additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"] = None,
    xrayEnabled: bool = None
) -> CreateGraphqlApiResponseTypeDef:
    pass
```

### create_resolver

Type annotations for `boto3.client("appsync").create_resolver` method.

[Client.create_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_resolver)

```python
def create_resolver(
    self,
    apiId: str,
    typeName: str,
    fieldName: str,
    dataSourceName: str = None,
    requestMappingTemplate: str = None,
    responseMappingTemplate: str = None,
    kind: ResolverKind = None,
    pipelineConfig: "PipelineConfigTypeDef" = None,
    syncConfig: "SyncConfigTypeDef" = None,
    cachingConfig: "CachingConfigTypeDef" = None
) -> CreateResolverResponseTypeDef:
    pass
```

### create_type

Type annotations for `boto3.client("appsync").create_type` method.

[Client.create_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.create_type)

```python
def create_type(
    self,
    apiId: str,
    definition: str,
    format: TypeDefinitionFormat
) -> CreateTypeResponseTypeDef:
    pass
```

### delete_api_cache

Type annotations for `boto3.client("appsync").delete_api_cache` method.

[Client.delete_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_api_cache)

```python
def delete_api_cache(
    self,
    apiId: str
) -> Dict[str, Any]:
    pass
```

### delete_api_key

Type annotations for `boto3.client("appsync").delete_api_key` method.

[Client.delete_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_api_key)

```python
def delete_api_key(
    self,
    apiId: str,
    id: str
) -> Dict[str, Any]:
    pass
```

### delete_data_source

Type annotations for `boto3.client("appsync").delete_data_source` method.

[Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_data_source)

```python
def delete_data_source(
    self,
    apiId: str,
    name: str
) -> Dict[str, Any]:
    pass
```

### delete_function

Type annotations for `boto3.client("appsync").delete_function` method.

[Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_function)

```python
def delete_function(
    self,
    apiId: str,
    functionId: str
) -> Dict[str, Any]:
    pass
```

### delete_graphql_api

Type annotations for `boto3.client("appsync").delete_graphql_api` method.

[Client.delete_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_graphql_api)

```python
def delete_graphql_api(
    self,
    apiId: str
) -> Dict[str, Any]:
    pass
```

### delete_resolver

Type annotations for `boto3.client("appsync").delete_resolver` method.

[Client.delete_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_resolver)

```python
def delete_resolver(
    self,
    apiId: str,
    typeName: str,
    fieldName: str
) -> Dict[str, Any]:
    pass
```

### delete_type

Type annotations for `boto3.client("appsync").delete_type` method.

[Client.delete_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.delete_type)

```python
def delete_type(
    self,
    apiId: str,
    typeName: str
) -> Dict[str, Any]:
    pass
```

### flush_api_cache

Type annotations for `boto3.client("appsync").flush_api_cache` method.

[Client.flush_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.flush_api_cache)

```python
def flush_api_cache(
    self,
    apiId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("appsync").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.generate_presigned_url)

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

### get_api_cache

Type annotations for `boto3.client("appsync").get_api_cache` method.

[Client.get_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_api_cache)

```python
def get_api_cache(
    self,
    apiId: str
) -> GetApiCacheResponseTypeDef:
    pass
```

### get_data_source

Type annotations for `boto3.client("appsync").get_data_source` method.

[Client.get_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_data_source)

```python
def get_data_source(
    self,
    apiId: str,
    name: str
) -> GetDataSourceResponseTypeDef:
    pass
```

### get_function

Type annotations for `boto3.client("appsync").get_function` method.

[Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_function)

```python
def get_function(
    self,
    apiId: str,
    functionId: str
) -> GetFunctionResponseTypeDef:
    pass
```

### get_graphql_api

Type annotations for `boto3.client("appsync").get_graphql_api` method.

[Client.get_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_graphql_api)

```python
def get_graphql_api(
    self,
    apiId: str
) -> GetGraphqlApiResponseTypeDef:
    pass
```

### get_introspection_schema

Type annotations for `boto3.client("appsync").get_introspection_schema` method.

[Client.get_introspection_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_introspection_schema)

```python
def get_introspection_schema(
    self,
    apiId: str,
    format: OutputType,
    includeDirectives: bool = None
) -> GetIntrospectionSchemaResponseTypeDef:
    pass
```

### get_resolver

Type annotations for `boto3.client("appsync").get_resolver` method.

[Client.get_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_resolver)

```python
def get_resolver(
    self,
    apiId: str,
    typeName: str,
    fieldName: str
) -> GetResolverResponseTypeDef:
    pass
```

### get_schema_creation_status

Type annotations for `boto3.client("appsync").get_schema_creation_status` method.

[Client.get_schema_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_schema_creation_status)

```python
def get_schema_creation_status(
    self,
    apiId: str
) -> GetSchemaCreationStatusResponseTypeDef:
    pass
```

### get_type

Type annotations for `boto3.client("appsync").get_type` method.

[Client.get_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.get_type)

```python
def get_type(
    self,
    apiId: str,
    typeName: str,
    format: TypeDefinitionFormat
) -> GetTypeResponseTypeDef:
    pass
```

### list_api_keys

Type annotations for `boto3.client("appsync").list_api_keys` method.

[Client.list_api_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_api_keys)

```python
def list_api_keys(
    self,
    apiId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListApiKeysResponseTypeDef:
    pass
```

### list_data_sources

Type annotations for `boto3.client("appsync").list_data_sources` method.

[Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_data_sources)

```python
def list_data_sources(
    self,
    apiId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListDataSourcesResponseTypeDef:
    pass
```

### list_functions

Type annotations for `boto3.client("appsync").list_functions` method.

[Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_functions)

```python
def list_functions(
    self,
    apiId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListFunctionsResponseTypeDef:
    pass
```

### list_graphql_apis

Type annotations for `boto3.client("appsync").list_graphql_apis` method.

[Client.list_graphql_apis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_graphql_apis)

```python
def list_graphql_apis(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListGraphqlApisResponseTypeDef:
    pass
```

### list_resolvers

Type annotations for `boto3.client("appsync").list_resolvers` method.

[Client.list_resolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_resolvers)

```python
def list_resolvers(
    self,
    apiId: str,
    typeName: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListResolversResponseTypeDef:
    pass
```

### list_resolvers_by_function

Type annotations for `boto3.client("appsync").list_resolvers_by_function` method.

[Client.list_resolvers_by_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_resolvers_by_function)

```python
def list_resolvers_by_function(
    self,
    apiId: str,
    functionId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListResolversByFunctionResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("appsync").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_types

Type annotations for `boto3.client("appsync").list_types` method.

[Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.list_types)

```python
def list_types(
    self,
    apiId: str,
    format: TypeDefinitionFormat,
    nextToken: str = None,
    maxResults: int = None
) -> ListTypesResponseTypeDef:
    pass
```

### start_schema_creation

Type annotations for `boto3.client("appsync").start_schema_creation` method.

[Client.start_schema_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.start_schema_creation)

```python
def start_schema_creation(
    self,
    apiId: str,
    definition: Union[bytes, IO[bytes]]
) -> StartSchemaCreationResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("appsync").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("appsync").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_api_cache

Type annotations for `boto3.client("appsync").update_api_cache` method.

[Client.update_api_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_api_cache)

```python
def update_api_cache(
    self,
    apiId: str,
    ttl: int,
    apiCachingBehavior: ApiCachingBehavior,
    type: ApiCacheType
) -> UpdateApiCacheResponseTypeDef:
    pass
```

### update_api_key

Type annotations for `boto3.client("appsync").update_api_key` method.

[Client.update_api_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_api_key)

```python
def update_api_key(
    self,
    apiId: str,
    id: str,
    description: str = None,
    expires: int = None
) -> UpdateApiKeyResponseTypeDef:
    pass
```

### update_data_source

Type annotations for `boto3.client("appsync").update_data_source` method.

[Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_data_source)

```python
def update_data_source(
    self,
    apiId: str,
    name: str,
    type: DataSourceType,
    description: str = None,
    serviceRoleArn: str = None,
    dynamodbConfig: "DynamodbDataSourceConfigTypeDef" = None,
    lambdaConfig: "LambdaDataSourceConfigTypeDef" = None,
    elasticsearchConfig: "ElasticsearchDataSourceConfigTypeDef" = None,
    httpConfig: "HttpDataSourceConfigTypeDef" = None,
    relationalDatabaseConfig: "RelationalDatabaseDataSourceConfigTypeDef" = None
) -> UpdateDataSourceResponseTypeDef:
    pass
```

### update_function

Type annotations for `boto3.client("appsync").update_function` method.

[Client.update_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_function)

```python
def update_function(
    self,
    apiId: str,
    name: str,
    functionId: str,
    dataSourceName: str,
    functionVersion: str,
    description: str = None,
    requestMappingTemplate: str = None,
    responseMappingTemplate: str = None,
    syncConfig: "SyncConfigTypeDef" = None
) -> UpdateFunctionResponseTypeDef:
    pass
```

### update_graphql_api

Type annotations for `boto3.client("appsync").update_graphql_api` method.

[Client.update_graphql_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_graphql_api)

```python
def update_graphql_api(
    self,
    apiId: str,
    name: str,
    logConfig: "LogConfigTypeDef" = None,
    authenticationType: AuthenticationType = None,
    userPoolConfig: "UserPoolConfigTypeDef" = None,
    openIDConnectConfig: "OpenIDConnectConfigTypeDef" = None,
    additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"] = None,
    xrayEnabled: bool = None
) -> UpdateGraphqlApiResponseTypeDef:
    pass
```

### update_resolver

Type annotations for `boto3.client("appsync").update_resolver` method.

[Client.update_resolver documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_resolver)

```python
def update_resolver(
    self,
    apiId: str,
    typeName: str,
    fieldName: str,
    dataSourceName: str = None,
    requestMappingTemplate: str = None,
    responseMappingTemplate: str = None,
    kind: ResolverKind = None,
    pipelineConfig: "PipelineConfigTypeDef" = None,
    syncConfig: "SyncConfigTypeDef" = None,
    cachingConfig: "CachingConfigTypeDef" = None
) -> UpdateResolverResponseTypeDef:
    pass
```

### update_type

Type annotations for `boto3.client("appsync").update_type` method.

[Client.update_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client.update_type)

```python
def update_type(
    self,
    apiId: str,
    typeName: str,
    format: TypeDefinitionFormat,
    definition: str = None
) -> UpdateTypeResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("appsync").get_paginator` method with overloads.

- `client.get_paginator("list_api_keys")` -> [ListApiKeysPaginator](./paginators.md#listapikeyspaginator)
- `client.get_paginator("list_data_sources")` -> [ListDataSourcesPaginator](./paginators.md#listdatasourcespaginator)
- `client.get_paginator("list_functions")` -> [ListFunctionsPaginator](./paginators.md#listfunctionspaginator)
- `client.get_paginator("list_graphql_apis")` -> [ListGraphqlApisPaginator](./paginators.md#listgraphqlapispaginator)
- `client.get_paginator("list_resolvers")` -> [ListResolversPaginator](./paginators.md#listresolverspaginator)
- `client.get_paginator("list_resolvers_by_function")` -> [ListResolversByFunctionPaginator](./paginators.md#listresolversbyfunctionpaginator)
- `client.get_paginator("list_types")` -> [ListTypesPaginator](./paginators.md#listtypespaginator)


