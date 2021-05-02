# Structures for boto3 AppSync module

> [Index](../index.md) > [AppSync](./index.md) > Structures

Auto-generated documentation for [AppSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync)
type annotations stubs module [mypy_boto3_appsync](https://pypi.org/project/mypy-boto3-appsync/).

- [Structures for boto3 AppSync module](#structures-for-boto3-appsync-module)
  - [AdditionalAuthenticationProviderTypeDef](#additionalauthenticationprovidertypedef)
  - [ApiCacheTypeDef](#apicachetypedef)
  - [ApiKeyTypeDef](#apikeytypedef)
  - [AuthorizationConfigTypeDef](#authorizationconfigtypedef)
  - [AwsIamConfigTypeDef](#awsiamconfigtypedef)
  - [CachingConfigTypeDef](#cachingconfigtypedef)
  - [CognitoUserPoolConfigTypeDef](#cognitouserpoolconfigtypedef)
  - [CreateApiCacheResponseTypeDef](#createapicacheresponsetypedef)
  - [CreateApiKeyResponseTypeDef](#createapikeyresponsetypedef)
  - [CreateDataSourceResponseTypeDef](#createdatasourceresponsetypedef)
  - [CreateFunctionResponseTypeDef](#createfunctionresponsetypedef)
  - [CreateGraphqlApiResponseTypeDef](#creategraphqlapiresponsetypedef)
  - [CreateResolverResponseTypeDef](#createresolverresponsetypedef)
  - [CreateTypeResponseTypeDef](#createtyperesponsetypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [DeltaSyncConfigTypeDef](#deltasyncconfigtypedef)
  - [DynamodbDataSourceConfigTypeDef](#dynamodbdatasourceconfigtypedef)
  - [ElasticsearchDataSourceConfigTypeDef](#elasticsearchdatasourceconfigtypedef)
  - [FunctionConfigurationTypeDef](#functionconfigurationtypedef)
  - [GetApiCacheResponseTypeDef](#getapicacheresponsetypedef)
  - [GetDataSourceResponseTypeDef](#getdatasourceresponsetypedef)
  - [GetFunctionResponseTypeDef](#getfunctionresponsetypedef)
  - [GetGraphqlApiResponseTypeDef](#getgraphqlapiresponsetypedef)
  - [GetIntrospectionSchemaResponseTypeDef](#getintrospectionschemaresponsetypedef)
  - [GetResolverResponseTypeDef](#getresolverresponsetypedef)
  - [GetSchemaCreationStatusResponseTypeDef](#getschemacreationstatusresponsetypedef)
  - [GetTypeResponseTypeDef](#gettyperesponsetypedef)
  - [GraphqlApiTypeDef](#graphqlapitypedef)
  - [HttpDataSourceConfigTypeDef](#httpdatasourceconfigtypedef)
  - [LambdaConflictHandlerConfigTypeDef](#lambdaconflicthandlerconfigtypedef)
  - [LambdaDataSourceConfigTypeDef](#lambdadatasourceconfigtypedef)
  - [ListApiKeysResponseTypeDef](#listapikeysresponsetypedef)
  - [ListDataSourcesResponseTypeDef](#listdatasourcesresponsetypedef)
  - [ListFunctionsResponseTypeDef](#listfunctionsresponsetypedef)
  - [ListGraphqlApisResponseTypeDef](#listgraphqlapisresponsetypedef)
  - [ListResolversByFunctionResponseTypeDef](#listresolversbyfunctionresponsetypedef)
  - [ListResolversResponseTypeDef](#listresolversresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTypesResponseTypeDef](#listtypesresponsetypedef)
  - [LogConfigTypeDef](#logconfigtypedef)
  - [OpenIDConnectConfigTypeDef](#openidconnectconfigtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PipelineConfigTypeDef](#pipelineconfigtypedef)
  - [RdsHttpEndpointConfigTypeDef](#rdshttpendpointconfigtypedef)
  - [RelationalDatabaseDataSourceConfigTypeDef](#relationaldatabasedatasourceconfigtypedef)
  - [ResolverTypeDef](#resolvertypedef)
  - [StartSchemaCreationResponseTypeDef](#startschemacreationresponsetypedef)
  - [SyncConfigTypeDef](#syncconfigtypedef)
  - [TypeTypeDef](#typetypedef)
  - [UpdateApiCacheResponseTypeDef](#updateapicacheresponsetypedef)
  - [UpdateApiKeyResponseTypeDef](#updateapikeyresponsetypedef)
  - [UpdateDataSourceResponseTypeDef](#updatedatasourceresponsetypedef)
  - [UpdateFunctionResponseTypeDef](#updatefunctionresponsetypedef)
  - [UpdateGraphqlApiResponseTypeDef](#updategraphqlapiresponsetypedef)
  - [UpdateResolverResponseTypeDef](#updateresolverresponsetypedef)
  - [UpdateTypeResponseTypeDef](#updatetyperesponsetypedef)
  - [UserPoolConfigTypeDef](#userpoolconfigtypedef)

## AdditionalAuthenticationProviderTypeDef

```python
from mypy_boto3_appsync.type_defs import AdditionalAuthenticationProviderTypeDef
```




Optional fields:
- `authenticationType`: `AuthenticationType`
- `openIDConnectConfig`: `"OpenIDConnectConfigTypeDef"`
- `userPoolConfig`: `"CognitoUserPoolConfigTypeDef"`


## ApiCacheTypeDef

```python
from mypy_boto3_appsync.type_defs import ApiCacheTypeDef
```




Optional fields:
- `ttl`: `int`
- `apiCachingBehavior`: `ApiCachingBehavior`
- `transitEncryptionEnabled`: `bool`
- `atRestEncryptionEnabled`: `bool`
- `type`: `ApiCacheType`
- `status`: `ApiCacheStatus`


## ApiKeyTypeDef

```python
from mypy_boto3_appsync.type_defs import ApiKeyTypeDef
```




Optional fields:
- `id`: `str`
- `description`: `str`
- `expires`: `int`
- `deletes`: `int`


## AuthorizationConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import AuthorizationConfigTypeDef
```


Required fields:
- `authorizationType`: `Literal['AWS_IAM']`



Optional fields:
- `awsIamConfig`: `"AwsIamConfigTypeDef"`


## AwsIamConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import AwsIamConfigTypeDef
```




Optional fields:
- `signingRegion`: `str`
- `signingServiceName`: `str`


## CachingConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import CachingConfigTypeDef
```




Optional fields:
- `ttl`: `int`
- `cachingKeys`: `List[str]`


## CognitoUserPoolConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import CognitoUserPoolConfigTypeDef
```


Required fields:
- `userPoolId`: `str`
- `awsRegion`: `str`



Optional fields:
- `appIdClientRegex`: `str`


## CreateApiCacheResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateApiCacheResponseTypeDef
```




Optional fields:
- `apiCache`: `"ApiCacheTypeDef"`


## CreateApiKeyResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateApiKeyResponseTypeDef
```




Optional fields:
- `apiKey`: `"ApiKeyTypeDef"`


## CreateDataSourceResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateDataSourceResponseTypeDef
```




Optional fields:
- `dataSource`: `"DataSourceTypeDef"`


## CreateFunctionResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateFunctionResponseTypeDef
```




Optional fields:
- `functionConfiguration`: `"FunctionConfigurationTypeDef"`


## CreateGraphqlApiResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateGraphqlApiResponseTypeDef
```




Optional fields:
- `graphqlApi`: `"GraphqlApiTypeDef"`


## CreateResolverResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateResolverResponseTypeDef
```




Optional fields:
- `resolver`: `"ResolverTypeDef"`


## CreateTypeResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import CreateTypeResponseTypeDef
```




Optional fields:
- `type`: `"TypeTypeDef"`


## DataSourceTypeDef

```python
from mypy_boto3_appsync.type_defs import DataSourceTypeDef
```




Optional fields:
- `dataSourceArn`: `str`
- `name`: `str`
- `description`: `str`
- `type`: `DataSourceType`
- `serviceRoleArn`: `str`
- `dynamodbConfig`: `"DynamodbDataSourceConfigTypeDef"`
- `lambdaConfig`: `"LambdaDataSourceConfigTypeDef"`
- `elasticsearchConfig`: `"ElasticsearchDataSourceConfigTypeDef"`
- `httpConfig`: `"HttpDataSourceConfigTypeDef"`
- `relationalDatabaseConfig`: `"RelationalDatabaseDataSourceConfigTypeDef"`


## DeltaSyncConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import DeltaSyncConfigTypeDef
```




Optional fields:
- `baseTableTTL`: `int`
- `deltaSyncTableName`: `str`
- `deltaSyncTableTTL`: `int`


## DynamodbDataSourceConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import DynamodbDataSourceConfigTypeDef
```


Required fields:
- `tableName`: `str`
- `awsRegion`: `str`



Optional fields:
- `useCallerCredentials`: `bool`
- `deltaSyncConfig`: `"DeltaSyncConfigTypeDef"`
- `versioned`: `bool`


## ElasticsearchDataSourceConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import ElasticsearchDataSourceConfigTypeDef
```


Required fields:
- `endpoint`: `str`
- `awsRegion`: `str`




## FunctionConfigurationTypeDef

```python
from mypy_boto3_appsync.type_defs import FunctionConfigurationTypeDef
```




Optional fields:
- `functionId`: `str`
- `functionArn`: `str`
- `name`: `str`
- `description`: `str`
- `dataSourceName`: `str`
- `requestMappingTemplate`: `str`
- `responseMappingTemplate`: `str`
- `functionVersion`: `str`
- `syncConfig`: `"SyncConfigTypeDef"`


## GetApiCacheResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetApiCacheResponseTypeDef
```




Optional fields:
- `apiCache`: `"ApiCacheTypeDef"`


## GetDataSourceResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetDataSourceResponseTypeDef
```




Optional fields:
- `dataSource`: `"DataSourceTypeDef"`


## GetFunctionResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetFunctionResponseTypeDef
```




Optional fields:
- `functionConfiguration`: `"FunctionConfigurationTypeDef"`


## GetGraphqlApiResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetGraphqlApiResponseTypeDef
```




Optional fields:
- `graphqlApi`: `"GraphqlApiTypeDef"`


## GetIntrospectionSchemaResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetIntrospectionSchemaResponseTypeDef
```




Optional fields:
- `schema`: `Union[bytes, IO[bytes]]`


## GetResolverResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetResolverResponseTypeDef
```




Optional fields:
- `resolver`: `"ResolverTypeDef"`


## GetSchemaCreationStatusResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetSchemaCreationStatusResponseTypeDef
```




Optional fields:
- `status`: `SchemaStatus`
- `details`: `str`


## GetTypeResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import GetTypeResponseTypeDef
```




Optional fields:
- `type`: `"TypeTypeDef"`


## GraphqlApiTypeDef

```python
from mypy_boto3_appsync.type_defs import GraphqlApiTypeDef
```




Optional fields:
- `name`: `str`
- `apiId`: `str`
- `authenticationType`: `AuthenticationType`
- `logConfig`: `"LogConfigTypeDef"`
- `userPoolConfig`: `"UserPoolConfigTypeDef"`
- `openIDConnectConfig`: `"OpenIDConnectConfigTypeDef"`
- `arn`: `str`
- `uris`: `Dict[str, str]`
- `tags`: `Dict[str, str]`
- `additionalAuthenticationProviders`: `List["AdditionalAuthenticationProviderTypeDef"]`
- `xrayEnabled`: `bool`
- `wafWebAclArn`: `str`


## HttpDataSourceConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import HttpDataSourceConfigTypeDef
```




Optional fields:
- `endpoint`: `str`
- `authorizationConfig`: `"AuthorizationConfigTypeDef"`


## LambdaConflictHandlerConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import LambdaConflictHandlerConfigTypeDef
```




Optional fields:
- `lambdaConflictHandlerArn`: `str`


## LambdaDataSourceConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import LambdaDataSourceConfigTypeDef
```


Required fields:
- `lambdaFunctionArn`: `str`




## ListApiKeysResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListApiKeysResponseTypeDef
```




Optional fields:
- `apiKeys`: `List["ApiKeyTypeDef"]`
- `nextToken`: `str`


## ListDataSourcesResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListDataSourcesResponseTypeDef
```




Optional fields:
- `dataSources`: `List["DataSourceTypeDef"]`
- `nextToken`: `str`


## ListFunctionsResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListFunctionsResponseTypeDef
```




Optional fields:
- `functions`: `List["FunctionConfigurationTypeDef"]`
- `nextToken`: `str`


## ListGraphqlApisResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListGraphqlApisResponseTypeDef
```




Optional fields:
- `graphqlApis`: `List["GraphqlApiTypeDef"]`
- `nextToken`: `str`


## ListResolversByFunctionResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListResolversByFunctionResponseTypeDef
```




Optional fields:
- `resolvers`: `List["ResolverTypeDef"]`
- `nextToken`: `str`


## ListResolversResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListResolversResponseTypeDef
```




Optional fields:
- `resolvers`: `List["ResolverTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListTypesResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import ListTypesResponseTypeDef
```




Optional fields:
- `types`: `List["TypeTypeDef"]`
- `nextToken`: `str`


## LogConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import LogConfigTypeDef
```


Required fields:
- `fieldLogLevel`: `FieldLogLevel`
- `cloudWatchLogsRoleArn`: `str`



Optional fields:
- `excludeVerboseContent`: `bool`


## OpenIDConnectConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import OpenIDConnectConfigTypeDef
```


Required fields:
- `issuer`: `str`



Optional fields:
- `clientId`: `str`
- `iatTTL`: `int`
- `authTTL`: `int`


## PaginatorConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PipelineConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import PipelineConfigTypeDef
```




Optional fields:
- `functions`: `List[str]`


## RdsHttpEndpointConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import RdsHttpEndpointConfigTypeDef
```




Optional fields:
- `awsRegion`: `str`
- `dbClusterIdentifier`: `str`
- `databaseName`: `str`
- `schema`: `str`
- `awsSecretStoreArn`: `str`


## RelationalDatabaseDataSourceConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import RelationalDatabaseDataSourceConfigTypeDef
```




Optional fields:
- `relationalDatabaseSourceType`: `Literal['RDS_HTTP_ENDPOINT']`
- `rdsHttpEndpointConfig`: `"RdsHttpEndpointConfigTypeDef"`


## ResolverTypeDef

```python
from mypy_boto3_appsync.type_defs import ResolverTypeDef
```




Optional fields:
- `typeName`: `str`
- `fieldName`: `str`
- `dataSourceName`: `str`
- `resolverArn`: `str`
- `requestMappingTemplate`: `str`
- `responseMappingTemplate`: `str`
- `kind`: `ResolverKind`
- `pipelineConfig`: `"PipelineConfigTypeDef"`
- `syncConfig`: `"SyncConfigTypeDef"`
- `cachingConfig`: `"CachingConfigTypeDef"`


## StartSchemaCreationResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import StartSchemaCreationResponseTypeDef
```




Optional fields:
- `status`: `SchemaStatus`


## SyncConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import SyncConfigTypeDef
```




Optional fields:
- `conflictHandler`: `ConflictHandlerType`
- `conflictDetection`: `ConflictDetectionType`
- `lambdaConflictHandlerConfig`: `"LambdaConflictHandlerConfigTypeDef"`


## TypeTypeDef

```python
from mypy_boto3_appsync.type_defs import TypeTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `arn`: `str`
- `definition`: `str`
- `format`: `TypeDefinitionFormat`


## UpdateApiCacheResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateApiCacheResponseTypeDef
```




Optional fields:
- `apiCache`: `"ApiCacheTypeDef"`


## UpdateApiKeyResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateApiKeyResponseTypeDef
```




Optional fields:
- `apiKey`: `"ApiKeyTypeDef"`


## UpdateDataSourceResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateDataSourceResponseTypeDef
```




Optional fields:
- `dataSource`: `"DataSourceTypeDef"`


## UpdateFunctionResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateFunctionResponseTypeDef
```




Optional fields:
- `functionConfiguration`: `"FunctionConfigurationTypeDef"`


## UpdateGraphqlApiResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateGraphqlApiResponseTypeDef
```




Optional fields:
- `graphqlApi`: `"GraphqlApiTypeDef"`


## UpdateResolverResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateResolverResponseTypeDef
```




Optional fields:
- `resolver`: `"ResolverTypeDef"`


## UpdateTypeResponseTypeDef

```python
from mypy_boto3_appsync.type_defs import UpdateTypeResponseTypeDef
```




Optional fields:
- `type`: `"TypeTypeDef"`


## UserPoolConfigTypeDef

```python
from mypy_boto3_appsync.type_defs import UserPoolConfigTypeDef
```


Required fields:
- `userPoolId`: `str`
- `awsRegion`: `str`
- `defaultAction`: `DefaultAction`



Optional fields:
- `appIdClientRegex`: `str`

