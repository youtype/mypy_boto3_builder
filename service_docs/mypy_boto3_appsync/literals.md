# Literals for boto3 AppSync module

> [Index](../index.md) > [AppSync](./index.md) > Literals

Auto-generated documentation for [AppSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync)
type annotations stubs module [mypy_boto3_appsync](https://pypi.org/project/mypy-boto3-appsync/).

- [Literals for boto3 AppSync module](#literals-for-boto3-appsync-module)
  - [ApiCacheStatus](#apicachestatus)
  - [ApiCacheType](#apicachetype)
  - [ApiCachingBehavior](#apicachingbehavior)
  - [AuthenticationType](#authenticationtype)
  - [AuthorizationType](#authorizationtype)
  - [ConflictDetectionType](#conflictdetectiontype)
  - [ConflictHandlerType](#conflicthandlertype)
  - [DataSourceType](#datasourcetype)
  - [DefaultAction](#defaultaction)
  - [FieldLogLevel](#fieldloglevel)
  - [ListApiKeysPaginatorName](#listapikeyspaginatorname)
  - [ListDataSourcesPaginatorName](#listdatasourcespaginatorname)
  - [ListFunctionsPaginatorName](#listfunctionspaginatorname)
  - [ListGraphqlApisPaginatorName](#listgraphqlapispaginatorname)
  - [ListResolversByFunctionPaginatorName](#listresolversbyfunctionpaginatorname)
  - [ListResolversPaginatorName](#listresolverspaginatorname)
  - [ListTypesPaginatorName](#listtypespaginatorname)
  - [OutputType](#outputtype)
  - [RelationalDatabaseSourceType](#relationaldatabasesourcetype)
  - [ResolverKind](#resolverkind)
  - [SchemaStatus](#schemastatus)
  - [TypeDefinitionFormat](#typedefinitionformat)

## ApiCacheStatus

```python
from mypy_boto3_appsync.literals import ApiCacheStatus
```

Values:

- `AVAILABLE`
- `CREATING`
- `DELETING`
- `FAILED`
- `MODIFYING`

## ApiCacheType

```python
from mypy_boto3_appsync.literals import ApiCacheType
```

Values:

- `LARGE`
- `LARGE_12X`
- `LARGE_2X`
- `LARGE_4X`
- `LARGE_8X`
- `MEDIUM`
- `R4_2XLARGE`
- `R4_4XLARGE`
- `R4_8XLARGE`
- `R4_LARGE`
- `R4_XLARGE`
- `SMALL`
- `T2_MEDIUM`
- `T2_SMALL`
- `XLARGE`

## ApiCachingBehavior

```python
from mypy_boto3_appsync.literals import ApiCachingBehavior
```

Values:

- `FULL_REQUEST_CACHING`
- `PER_RESOLVER_CACHING`

## AuthenticationType

```python
from mypy_boto3_appsync.literals import AuthenticationType
```

Values:

- `AMAZON_COGNITO_USER_POOLS`
- `API_KEY`
- `AWS_IAM`
- `OPENID_CONNECT`

## AuthorizationType

```python
from mypy_boto3_appsync.literals import AuthorizationType
```

Values:

- `AWS_IAM`

## ConflictDetectionType

```python
from mypy_boto3_appsync.literals import ConflictDetectionType
```

Values:

- `NONE`
- `VERSION`

## ConflictHandlerType

```python
from mypy_boto3_appsync.literals import ConflictHandlerType
```

Values:

- `AUTOMERGE`
- `LAMBDA`
- `NONE`
- `OPTIMISTIC_CONCURRENCY`

## DataSourceType

```python
from mypy_boto3_appsync.literals import DataSourceType
```

Values:

- `AMAZON_DYNAMODB`
- `AMAZON_ELASTICSEARCH`
- `AWS_LAMBDA`
- `HTTP`
- `NONE`
- `RELATIONAL_DATABASE`

## DefaultAction

```python
from mypy_boto3_appsync.literals import DefaultAction
```

Values:

- `ALLOW`
- `DENY`

## FieldLogLevel

```python
from mypy_boto3_appsync.literals import FieldLogLevel
```

Values:

- `ALL`
- `ERROR`
- `NONE`

## ListApiKeysPaginatorName

```python
from mypy_boto3_appsync.literals import ListApiKeysPaginatorName
```

Values:

- `list_api_keys`

## ListDataSourcesPaginatorName

```python
from mypy_boto3_appsync.literals import ListDataSourcesPaginatorName
```

Values:

- `list_data_sources`

## ListFunctionsPaginatorName

```python
from mypy_boto3_appsync.literals import ListFunctionsPaginatorName
```

Values:

- `list_functions`

## ListGraphqlApisPaginatorName

```python
from mypy_boto3_appsync.literals import ListGraphqlApisPaginatorName
```

Values:

- `list_graphql_apis`

## ListResolversByFunctionPaginatorName

```python
from mypy_boto3_appsync.literals import ListResolversByFunctionPaginatorName
```

Values:

- `list_resolvers_by_function`

## ListResolversPaginatorName

```python
from mypy_boto3_appsync.literals import ListResolversPaginatorName
```

Values:

- `list_resolvers`

## ListTypesPaginatorName

```python
from mypy_boto3_appsync.literals import ListTypesPaginatorName
```

Values:

- `list_types`

## OutputType

```python
from mypy_boto3_appsync.literals import OutputType
```

Values:

- `JSON`
- `SDL`

## RelationalDatabaseSourceType

```python
from mypy_boto3_appsync.literals import RelationalDatabaseSourceType
```

Values:

- `RDS_HTTP_ENDPOINT`

## ResolverKind

```python
from mypy_boto3_appsync.literals import ResolverKind
```

Values:

- `PIPELINE`
- `UNIT`

## SchemaStatus

```python
from mypy_boto3_appsync.literals import SchemaStatus
```

Values:

- `ACTIVE`
- `DELETING`
- `FAILED`
- `NOT_APPLICABLE`
- `PROCESSING`
- `SUCCESS`

## TypeDefinitionFormat

```python
from mypy_boto3_appsync.literals import TypeDefinitionFormat
```

Values:

- `JSON`
- `SDL`
