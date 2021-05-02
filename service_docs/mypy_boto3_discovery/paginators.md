# Paginators for boto3 ApplicationDiscoveryService module

> [Index](../index.md) > [ApplicationDiscoveryService](./index.md) > Paginators

Auto-generated documentation for [ApplicationDiscoveryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService)
type annotations stubs module [mypy_boto3_discovery](https://pypi.org/project/mypy-boto3-discovery/).

- [Paginators for boto3 ApplicationDiscoveryService module](#paginators-for-boto3-applicationdiscoveryservice-module)
  - [DescribeAgentsPaginator](#describeagentspaginator)
  - [DescribeContinuousExportsPaginator](#describecontinuousexportspaginator)
  - [DescribeExportConfigurationsPaginator](#describeexportconfigurationspaginator)
  - [DescribeExportTasksPaginator](#describeexporttaskspaginator)
  - [DescribeTagsPaginator](#describetagspaginator)
  - [ListConfigurationsPaginator](#listconfigurationspaginator)

## DescribeAgentsPaginator

Type annotations for `boto3.client("discovery").get_paginator("describe_agents")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import DescribeAgentsPaginator

def get_describe_agents_paginator() -> DescribeAgentsPaginator:
    return boto3.client("discovery").get_paginator("describe_agents")
```

[Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)

```python
class DescribeAgentsPaginator(Boto3Paginator):
    def paginate(
        self,
        agentIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAgentsResponseTypeDef]:
        pass
```
## DescribeContinuousExportsPaginator

Type annotations for `boto3.client("discovery").get_paginator("describe_continuous_exports")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import DescribeContinuousExportsPaginator

def get_describe_continuous_exports_paginator() -> DescribeContinuousExportsPaginator:
    return boto3.client("discovery").get_paginator("describe_continuous_exports")
```

[Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)

```python
class DescribeContinuousExportsPaginator(Boto3Paginator):
    def paginate(
        self,
        exportIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeContinuousExportsResponseTypeDef]:
        pass
```
## DescribeExportConfigurationsPaginator

Type annotations for `boto3.client("discovery").get_paginator("describe_export_configurations")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import DescribeExportConfigurationsPaginator

def get_describe_export_configurations_paginator() -> DescribeExportConfigurationsPaginator:
    return boto3.client("discovery").get_paginator("describe_export_configurations")
```

[Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)

```python
class DescribeExportConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        exportIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportConfigurationsResponseTypeDef]:
        pass
```
## DescribeExportTasksPaginator

Type annotations for `boto3.client("discovery").get_paginator("describe_export_tasks")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import DescribeExportTasksPaginator

def get_describe_export_tasks_paginator() -> DescribeExportTasksPaginator:
    return boto3.client("discovery").get_paginator("describe_export_tasks")
```

[Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)

```python
class DescribeExportTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        exportIds: List[str] = None,
        filters: List[ExportFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportTasksResponseTypeDef]:
        pass
```
## DescribeTagsPaginator

Type annotations for `boto3.client("discovery").get_paginator("describe_tags")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import DescribeTagsPaginator

def get_describe_tags_paginator() -> DescribeTagsPaginator:
    return boto3.client("discovery").get_paginator("describe_tags")
```

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)

```python
class DescribeTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        filters: List[TagFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTagsResponseTypeDef]:
        pass
```
## ListConfigurationsPaginator

Type annotations for `boto3.client("discovery").get_paginator("list_configurations")`.

Can be used directly:

```python
from mypy_boto3_discovery.paginators import ListConfigurationsPaginator

def get_list_configurations_paginator() -> ListConfigurationsPaginator:
    return boto3.client("discovery").get_paginator("list_configurations")
```

[Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)

```python
class ListConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        configurationType: ConfigurationItemType,
        filters: List[FilterTypeDef] = None,
        orderBy: List[OrderByElementTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationsResponseTypeDef]:
        pass
```