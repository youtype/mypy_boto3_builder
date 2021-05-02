# Paginators for boto3 Glue module

> [Index](../index.md) > [Glue](./index.md) > Paginators

Auto-generated documentation for [Glue](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue)
type annotations stubs module [mypy_boto3_glue](https://pypi.org/project/mypy-boto3-glue/).

- [Paginators for boto3 Glue module](#paginators-for-boto3-glue-module)
  - [GetClassifiersPaginator](#getclassifierspaginator)
  - [GetConnectionsPaginator](#getconnectionspaginator)
  - [GetCrawlerMetricsPaginator](#getcrawlermetricspaginator)
  - [GetCrawlersPaginator](#getcrawlerspaginator)
  - [GetDatabasesPaginator](#getdatabasespaginator)
  - [GetDevEndpointsPaginator](#getdevendpointspaginator)
  - [GetJobRunsPaginator](#getjobrunspaginator)
  - [GetJobsPaginator](#getjobspaginator)
  - [GetPartitionIndexesPaginator](#getpartitionindexespaginator)
  - [GetPartitionsPaginator](#getpartitionspaginator)
  - [GetResourcePoliciesPaginator](#getresourcepoliciespaginator)
  - [GetSecurityConfigurationsPaginator](#getsecurityconfigurationspaginator)
  - [GetTableVersionsPaginator](#gettableversionspaginator)
  - [GetTablesPaginator](#gettablespaginator)
  - [GetTriggersPaginator](#gettriggerspaginator)
  - [GetUserDefinedFunctionsPaginator](#getuserdefinedfunctionspaginator)
  - [ListRegistriesPaginator](#listregistriespaginator)
  - [ListSchemaVersionsPaginator](#listschemaversionspaginator)
  - [ListSchemasPaginator](#listschemaspaginator)

## GetClassifiersPaginator

Type annotations for `boto3.client("glue").get_paginator("get_classifiers")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetClassifiersPaginator

def get_get_classifiers_paginator() -> GetClassifiersPaginator:
    return boto3.client("glue").get_paginator("get_classifiers")
```

[Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetClassifiers)

```python
class GetClassifiersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetClassifiersResponseTypeDef]:
        pass
```
## GetConnectionsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_connections")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetConnectionsPaginator

def get_get_connections_paginator() -> GetConnectionsPaginator:
    return boto3.client("glue").get_paginator("get_connections")
```

[Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetConnections)

```python
class GetConnectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        CatalogId: str = None,
        Filter: GetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectionsResponseTypeDef]:
        pass
```
## GetCrawlerMetricsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_crawler_metrics")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetCrawlerMetricsPaginator

def get_get_crawler_metrics_paginator() -> GetCrawlerMetricsPaginator:
    return boto3.client("glue").get_paginator("get_crawler_metrics")
```

[Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)

```python
class GetCrawlerMetricsPaginator(Boto3Paginator):
    def paginate(
        self,
        CrawlerNameList: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCrawlerMetricsResponseTypeDef]:
        pass
```
## GetCrawlersPaginator

Type annotations for `boto3.client("glue").get_paginator("get_crawlers")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetCrawlersPaginator

def get_get_crawlers_paginator() -> GetCrawlersPaginator:
    return boto3.client("glue").get_paginator("get_crawlers")
```

[Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetCrawlers)

```python
class GetCrawlersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCrawlersResponseTypeDef]:
        pass
```
## GetDatabasesPaginator

Type annotations for `boto3.client("glue").get_paginator("get_databases")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetDatabasesPaginator

def get_get_databases_paginator() -> GetDatabasesPaginator:
    return boto3.client("glue").get_paginator("get_databases")
```

[Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetDatabases)

```python
class GetDatabasesPaginator(Boto3Paginator):
    def paginate(
        self,
        CatalogId: str = None,
        ResourceShareType: ResourceShareType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDatabasesResponseTypeDef]:
        pass
```
## GetDevEndpointsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_dev_endpoints")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetDevEndpointsPaginator

def get_get_dev_endpoints_paginator() -> GetDevEndpointsPaginator:
    return boto3.client("glue").get_paginator("get_dev_endpoints")
```

[Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)

```python
class GetDevEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDevEndpointsResponseTypeDef]:
        pass
```
## GetJobRunsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_job_runs")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetJobRunsPaginator

def get_get_job_runs_paginator() -> GetJobRunsPaginator:
    return boto3.client("glue").get_paginator("get_job_runs")
```

[Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetJobRuns)

```python
class GetJobRunsPaginator(Boto3Paginator):
    def paginate(
        self,
        JobName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetJobRunsResponseTypeDef]:
        pass
```
## GetJobsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_jobs")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetJobsPaginator

def get_get_jobs_paginator() -> GetJobsPaginator:
    return boto3.client("glue").get_paginator("get_jobs")
```

[Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetJobs)

```python
class GetJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetJobsResponseTypeDef]:
        pass
```
## GetPartitionIndexesPaginator

Type annotations for `boto3.client("glue").get_paginator("get_partition_indexes")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetPartitionIndexesPaginator

def get_get_partition_indexes_paginator() -> GetPartitionIndexesPaginator:
    return boto3.client("glue").get_paginator("get_partition_indexes")
```

[Paginator.GetPartitionIndexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetPartitionIndexes)

```python
class GetPartitionIndexesPaginator(Boto3Paginator):
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetPartitionIndexesResponseTypeDef]:
        pass
```
## GetPartitionsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_partitions")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetPartitionsPaginator

def get_get_partitions_paginator() -> GetPartitionsPaginator:
    return boto3.client("glue").get_paginator("get_partitions")
```

[Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetPartitions)

```python
class GetPartitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        Segment: SegmentTypeDef = None,
        ExcludeColumnSchema: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetPartitionsResponseTypeDef]:
        pass
```
## GetResourcePoliciesPaginator

Type annotations for `boto3.client("glue").get_paginator("get_resource_policies")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetResourcePoliciesPaginator

def get_get_resource_policies_paginator() -> GetResourcePoliciesPaginator:
    return boto3.client("glue").get_paginator("get_resource_policies")
```

[Paginator.GetResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetResourcePolicies)

```python
class GetResourcePoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourcePoliciesResponseTypeDef]:
        pass
```
## GetSecurityConfigurationsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_security_configurations")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetSecurityConfigurationsPaginator

def get_get_security_configurations_paginator() -> GetSecurityConfigurationsPaginator:
    return boto3.client("glue").get_paginator("get_security_configurations")
```

[Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)

```python
class GetSecurityConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSecurityConfigurationsResponseTypeDef]:
        pass
```
## GetTableVersionsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_table_versions")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetTableVersionsPaginator

def get_get_table_versions_paginator() -> GetTableVersionsPaginator:
    return boto3.client("glue").get_paginator("get_table_versions")
```

[Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetTableVersions)

```python
class GetTableVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTableVersionsResponseTypeDef]:
        pass
```
## GetTablesPaginator

Type annotations for `boto3.client("glue").get_paginator("get_tables")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetTablesPaginator

def get_get_tables_paginator() -> GetTablesPaginator:
    return boto3.client("glue").get_paginator("get_tables")
```

[Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetTables)

```python
class GetTablesPaginator(Boto3Paginator):
    def paginate(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTablesResponseTypeDef]:
        pass
```
## GetTriggersPaginator

Type annotations for `boto3.client("glue").get_paginator("get_triggers")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetTriggersPaginator

def get_get_triggers_paginator() -> GetTriggersPaginator:
    return boto3.client("glue").get_paginator("get_triggers")
```

[Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetTriggers)

```python
class GetTriggersPaginator(Boto3Paginator):
    def paginate(
        self,
        DependentJobName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTriggersResponseTypeDef]:
        pass
```
## GetUserDefinedFunctionsPaginator

Type annotations for `boto3.client("glue").get_paginator("get_user_defined_functions")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import GetUserDefinedFunctionsPaginator

def get_get_user_defined_functions_paginator() -> GetUserDefinedFunctionsPaginator:
    return boto3.client("glue").get_paginator("get_user_defined_functions")
```

[Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)

```python
class GetUserDefinedFunctionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Pattern: str,
        CatalogId: str = None,
        DatabaseName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetUserDefinedFunctionsResponseTypeDef]:
        pass
```
## ListRegistriesPaginator

Type annotations for `boto3.client("glue").get_paginator("list_registries")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import ListRegistriesPaginator

def get_list_registries_paginator() -> ListRegistriesPaginator:
    return boto3.client("glue").get_paginator("list_registries")
```

[Paginator.ListRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.ListRegistries)

```python
class ListRegistriesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRegistriesResponseTypeDef]:
        pass
```
## ListSchemaVersionsPaginator

Type annotations for `boto3.client("glue").get_paginator("list_schema_versions")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import ListSchemaVersionsPaginator

def get_list_schema_versions_paginator() -> ListSchemaVersionsPaginator:
    return boto3.client("glue").get_paginator("list_schema_versions")
```

[Paginator.ListSchemaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.ListSchemaVersions)

```python
class ListSchemaVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        SchemaId: "SchemaIdTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemaVersionsResponseTypeDef]:
        pass
```
## ListSchemasPaginator

Type annotations for `boto3.client("glue").get_paginator("list_schemas")`.

Can be used directly:

```python
from mypy_boto3_glue.paginators import ListSchemasPaginator

def get_list_schemas_paginator() -> ListSchemasPaginator:
    return boto3.client("glue").get_paginator("list_schemas")
```

[Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Paginator.ListSchemas)

```python
class ListSchemasPaginator(Boto3Paginator):
    def paginate(
        self,
        RegistryId: RegistryIdTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasResponseTypeDef]:
        pass
```