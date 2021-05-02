# ApplicationDiscoveryServiceClient for boto3 ApplicationDiscoveryService module

> [Index](../index.md) > [ApplicationDiscoveryService](./index.md) > ApplicationDiscoveryServiceClient

Auto-generated documentation for [ApplicationDiscoveryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService)
type annotations stubs module [mypy_boto3_discovery](https://pypi.org/project/mypy-boto3-discovery/).

- [ApplicationDiscoveryServiceClient for boto3 ApplicationDiscoveryService module](#applicationdiscoveryserviceclient-for-boto3-applicationdiscoveryservice-module)
  - [ApplicationDiscoveryServiceClient](#applicationdiscoveryserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_configuration_items_to_application](#associate_configuration_items_to_application)
    - [batch_delete_import_data](#batch_delete_import_data)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [create_tags](#create_tags)
    - [delete_applications](#delete_applications)
    - [delete_tags](#delete_tags)
    - [describe_agents](#describe_agents)
    - [describe_configurations](#describe_configurations)
    - [describe_continuous_exports](#describe_continuous_exports)
    - [describe_export_configurations](#describe_export_configurations)
    - [describe_export_tasks](#describe_export_tasks)
    - [describe_import_tasks](#describe_import_tasks)
    - [describe_tags](#describe_tags)
    - [disassociate_configuration_items_from_application](#disassociate_configuration_items_from_application)
    - [export_configurations](#export_configurations)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_discovery_summary](#get_discovery_summary)
    - [list_configurations](#list_configurations)
    - [list_server_neighbors](#list_server_neighbors)
    - [start_continuous_export](#start_continuous_export)
    - [start_data_collection_by_agent_ids](#start_data_collection_by_agent_ids)
    - [start_export_task](#start_export_task)
    - [start_import_task](#start_import_task)
    - [stop_continuous_export](#stop_continuous_export)
    - [stop_data_collection_by_agent_ids](#stop_data_collection_by_agent_ids)
    - [update_application](#update_application)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)

## ApplicationDiscoveryServiceClient

Type annotations for `boto3.client("discovery")`

Can be used directly:

```python
from mypy_boto3_discovery.client import ApplicationDiscoveryServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_discovery.client import Exceptions

def handle_error(exc: Exceptions.AuthorizationErrorException) -> None:
    ...
```


Exceptions:

- `Exceptions.AuthorizationErrorException`
- `Exceptions.ClientError`
- `Exceptions.ConflictErrorException`
- `Exceptions.HomeRegionNotSetException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServerInternalErrorException`


## Methods


### associate_configuration_items_to_application

Type annotations for `boto3.client("discovery").associate_configuration_items_to_application` method.

[Client.associate_configuration_items_to_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.associate_configuration_items_to_application)

```python
def associate_configuration_items_to_application(
    self,
    applicationConfigurationId: str,
    configurationIds: List[str]
) -> Dict[str, Any]:
    pass
```

### batch_delete_import_data

Type annotations for `boto3.client("discovery").batch_delete_import_data` method.

[Client.batch_delete_import_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.batch_delete_import_data)

```python
def batch_delete_import_data(
    self,
    importTaskIds: List[str]
) -> BatchDeleteImportDataResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("discovery").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("discovery").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_application)

```python
def create_application(
    self,
    name: str,
    description: str = None
) -> CreateApplicationResponseTypeDef:
    pass
```

### create_tags

Type annotations for `boto3.client("discovery").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.create_tags)

```python
def create_tags(
    self,
    configurationIds: List[str],
    tags: List[TagTypeDef]
) -> Dict[str, Any]:
    pass
```

### delete_applications

Type annotations for `boto3.client("discovery").delete_applications` method.

[Client.delete_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_applications)

```python
def delete_applications(
    self,
    configurationIds: List[str]
) -> Dict[str, Any]:
    pass
```

### delete_tags

Type annotations for `boto3.client("discovery").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.delete_tags)

```python
def delete_tags(
    self,
    configurationIds: List[str],
    tags: List[TagTypeDef] = None
) -> Dict[str, Any]:
    pass
```

### describe_agents

Type annotations for `boto3.client("discovery").describe_agents` method.

[Client.describe_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_agents)

```python
def describe_agents(
    self,
    agentIds: List[str] = None,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeAgentsResponseTypeDef:
    pass
```

### describe_configurations

Type annotations for `boto3.client("discovery").describe_configurations` method.

[Client.describe_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_configurations)

```python
def describe_configurations(
    self,
    configurationIds: List[str]
) -> DescribeConfigurationsResponseTypeDef:
    pass
```

### describe_continuous_exports

Type annotations for `boto3.client("discovery").describe_continuous_exports` method.

[Client.describe_continuous_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_continuous_exports)

```python
def describe_continuous_exports(
    self,
    exportIds: List[str] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeContinuousExportsResponseTypeDef:
    pass
```

### describe_export_configurations

Type annotations for `boto3.client("discovery").describe_export_configurations` method.

[Client.describe_export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_configurations)

```python
def describe_export_configurations(
    self,
    exportIds: List[str] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeExportConfigurationsResponseTypeDef:
    pass
```

### describe_export_tasks

Type annotations for `boto3.client("discovery").describe_export_tasks` method.

[Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_export_tasks)

```python
def describe_export_tasks(
    self,
    exportIds: List[str] = None,
    filters: List[ExportFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeExportTasksResponseTypeDef:
    pass
```

### describe_import_tasks

Type annotations for `boto3.client("discovery").describe_import_tasks` method.

[Client.describe_import_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_import_tasks)

```python
def describe_import_tasks(
    self,
    filters: List[ImportTaskFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeImportTasksResponseTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("discovery").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.describe_tags)

```python
def describe_tags(
    self,
    filters: List[TagFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeTagsResponseTypeDef:
    pass
```

### disassociate_configuration_items_from_application

Type annotations for `boto3.client("discovery").disassociate_configuration_items_from_application` method.

[Client.disassociate_configuration_items_from_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.disassociate_configuration_items_from_application)

```python
def disassociate_configuration_items_from_application(
    self,
    applicationConfigurationId: str,
    configurationIds: List[str]
) -> Dict[str, Any]:
    pass
```

### export_configurations

Type annotations for `boto3.client("discovery").export_configurations` method.

[Client.export_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.export_configurations)

```python
def export_configurations(
    self
) -> ExportConfigurationsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("discovery").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.generate_presigned_url)

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

### get_discovery_summary

Type annotations for `boto3.client("discovery").get_discovery_summary` method.

[Client.get_discovery_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.get_discovery_summary)

```python
def get_discovery_summary(
    self
) -> GetDiscoverySummaryResponseTypeDef:
    pass
```

### list_configurations

Type annotations for `boto3.client("discovery").list_configurations` method.

[Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_configurations)

```python
def list_configurations(
    self,
    configurationType: ConfigurationItemType,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None,
    orderBy: List[OrderByElementTypeDef] = None
) -> ListConfigurationsResponseTypeDef:
    pass
```

### list_server_neighbors

Type annotations for `boto3.client("discovery").list_server_neighbors` method.

[Client.list_server_neighbors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.list_server_neighbors)

```python
def list_server_neighbors(
    self,
    configurationId: str,
    portInformationNeeded: bool = None,
    neighborConfigurationIds: List[str] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListServerNeighborsResponseTypeDef:
    pass
```

### start_continuous_export

Type annotations for `boto3.client("discovery").start_continuous_export` method.

[Client.start_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_continuous_export)

```python
def start_continuous_export(
    self
) -> StartContinuousExportResponseTypeDef:
    pass
```

### start_data_collection_by_agent_ids

Type annotations for `boto3.client("discovery").start_data_collection_by_agent_ids` method.

[Client.start_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_data_collection_by_agent_ids)

```python
def start_data_collection_by_agent_ids(
    self,
    agentIds: List[str]
) -> StartDataCollectionByAgentIdsResponseTypeDef:
    pass
```

### start_export_task

Type annotations for `boto3.client("discovery").start_export_task` method.

[Client.start_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_export_task)

```python
def start_export_task(
    self,
    exportDataFormat: List[ExportDataFormat] = None,
    filters: List[ExportFilterTypeDef] = None,
    startTime: datetime = None,
    endTime: datetime = None
) -> StartExportTaskResponseTypeDef:
    pass
```

### start_import_task

Type annotations for `boto3.client("discovery").start_import_task` method.

[Client.start_import_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.start_import_task)

```python
def start_import_task(
    self,
    name: str,
    importUrl: str,
    clientRequestToken: str = None
) -> StartImportTaskResponseTypeDef:
    pass
```

### stop_continuous_export

Type annotations for `boto3.client("discovery").stop_continuous_export` method.

[Client.stop_continuous_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_continuous_export)

```python
def stop_continuous_export(
    self,
    exportId: str
) -> StopContinuousExportResponseTypeDef:
    pass
```

### stop_data_collection_by_agent_ids

Type annotations for `boto3.client("discovery").stop_data_collection_by_agent_ids` method.

[Client.stop_data_collection_by_agent_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.stop_data_collection_by_agent_ids)

```python
def stop_data_collection_by_agent_ids(
    self,
    agentIds: List[str]
) -> StopDataCollectionByAgentIdsResponseTypeDef:
    pass
```

### update_application

Type annotations for `boto3.client("discovery").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Client.update_application)

```python
def update_application(
    self,
    configurationId: str,
    name: str = None,
    description: str = None
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("discovery").get_paginator` method.

[Paginator.DescribeAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeAgents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAgentsPaginatorName
) -> DescribeAgentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("discovery").get_paginator` method.

[Paginator.DescribeContinuousExports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeContinuousExports)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeContinuousExportsPaginatorName
) -> DescribeContinuousExportsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("discovery").get_paginator` method.

[Paginator.DescribeExportConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeExportConfigurationsPaginatorName
) -> DescribeExportConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("discovery").get_paginator` method.

[Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeExportTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeExportTasksPaginatorName
) -> DescribeExportTasksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("discovery").get_paginator` method.

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.DescribeTags)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeTagsPaginatorName
) -> DescribeTagsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("discovery").get_paginator` method.

[Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService.Paginator.ListConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListConfigurationsPaginatorName
) -> ListConfigurationsPaginator:
    pass
```