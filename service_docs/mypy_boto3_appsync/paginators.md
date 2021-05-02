# Paginators for boto3 AppSync module

> [Index](../index.md) > [AppSync](./index.md) > Paginators

Auto-generated documentation for [AppSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync)
type annotations stubs module [mypy_boto3_appsync](https://pypi.org/project/mypy-boto3-appsync/).

- [Paginators for boto3 AppSync module](#paginators-for-boto3-appsync-module)
  - [ListApiKeysPaginator](#listapikeyspaginator)
  - [ListDataSourcesPaginator](#listdatasourcespaginator)
  - [ListFunctionsPaginator](#listfunctionspaginator)
  - [ListGraphqlApisPaginator](#listgraphqlapispaginator)
  - [ListResolversPaginator](#listresolverspaginator)
  - [ListResolversByFunctionPaginator](#listresolversbyfunctionpaginator)
  - [ListTypesPaginator](#listtypespaginator)

## ListApiKeysPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_api_keys")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListApiKeysPaginator

def get_list_api_keys_paginator() -> ListApiKeysPaginator:
    return boto3.client("appsync").get_paginator("list_api_keys")
```

[Paginator.ListApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListApiKeys)

```python
class ListApiKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        apiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApiKeysResponseTypeDef]:
        pass
```
## ListDataSourcesPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_data_sources")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListDataSourcesPaginator

def get_list_data_sources_paginator() -> ListDataSourcesPaginator:
    return boto3.client("appsync").get_paginator("list_data_sources")
```

[Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListDataSources)

```python
class ListDataSourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        apiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        pass
```
## ListFunctionsPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_functions")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListFunctionsPaginator

def get_list_functions_paginator() -> ListFunctionsPaginator:
    return boto3.client("appsync").get_paginator("list_functions")
```

[Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListFunctions)

```python
class ListFunctionsPaginator(Boto3Paginator):
    def paginate(
        self,
        apiId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionsResponseTypeDef]:
        pass
```
## ListGraphqlApisPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_graphql_apis")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListGraphqlApisPaginator

def get_list_graphql_apis_paginator() -> ListGraphqlApisPaginator:
    return boto3.client("appsync").get_paginator("list_graphql_apis")
```

[Paginator.ListGraphqlApis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListGraphqlApis)

```python
class ListGraphqlApisPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGraphqlApisResponseTypeDef]:
        pass
```
## ListResolversPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_resolvers")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListResolversPaginator

def get_list_resolvers_paginator() -> ListResolversPaginator:
    return boto3.client("appsync").get_paginator("list_resolvers")
```

[Paginator.ListResolvers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListResolvers)

```python
class ListResolversPaginator(Boto3Paginator):
    def paginate(
        self,
        apiId: str,
        typeName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolversResponseTypeDef]:
        pass
```
## ListResolversByFunctionPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_resolvers_by_function")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListResolversByFunctionPaginator

def get_list_resolvers_by_function_paginator() -> ListResolversByFunctionPaginator:
    return boto3.client("appsync").get_paginator("list_resolvers_by_function")
```

[Paginator.ListResolversByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListResolversByFunction)

```python
class ListResolversByFunctionPaginator(Boto3Paginator):
    def paginate(
        self,
        apiId: str,
        functionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResolversByFunctionResponseTypeDef]:
        pass
```
## ListTypesPaginator

Type annotations for `boto3.client("appsync").get_paginator("list_types")`.

Can be used directly:

```python
from mypy_boto3_appsync.paginators import ListTypesPaginator

def get_list_types_paginator() -> ListTypesPaginator:
    return boto3.client("appsync").get_paginator("list_types")
```

[Paginator.ListTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Paginator.ListTypes)

```python
class ListTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        apiId: str,
        format: TypeDefinitionFormat,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTypesResponseTypeDef]:
        pass
```