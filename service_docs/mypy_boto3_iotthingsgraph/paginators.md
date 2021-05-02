# Paginators for boto3 IoTThingsGraph module

> [Index](../index.md) > [IoTThingsGraph](./index.md) > Paginators

Auto-generated documentation for [IoTThingsGraph](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph)
type annotations stubs module [mypy_boto3_iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/).

- [Paginators for boto3 IoTThingsGraph module](#paginators-for-boto3-iotthingsgraph-module)
  - [GetFlowTemplateRevisionsPaginator](#getflowtemplaterevisionspaginator)
  - [GetSystemTemplateRevisionsPaginator](#getsystemtemplaterevisionspaginator)
  - [ListFlowExecutionMessagesPaginator](#listflowexecutionmessagespaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [SearchEntitiesPaginator](#searchentitiespaginator)
  - [SearchFlowExecutionsPaginator](#searchflowexecutionspaginator)
  - [SearchFlowTemplatesPaginator](#searchflowtemplatespaginator)
  - [SearchSystemInstancesPaginator](#searchsysteminstancespaginator)
  - [SearchSystemTemplatesPaginator](#searchsystemtemplatespaginator)
  - [SearchThingsPaginator](#searchthingspaginator)

## GetFlowTemplateRevisionsPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("get_flow_template_revisions")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import GetFlowTemplateRevisionsPaginator

def get_get_flow_template_revisions_paginator() -> GetFlowTemplateRevisionsPaginator:
    return boto3.client("iotthingsgraph").get_paginator("get_flow_template_revisions")
```

[Paginator.GetFlowTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)

```python
class GetFlowTemplateRevisionsPaginator(Boto3Paginator):
    def paginate(
        self,
        id: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetFlowTemplateRevisionsResponseTypeDef]:
        pass
```
## GetSystemTemplateRevisionsPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("get_system_template_revisions")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import GetSystemTemplateRevisionsPaginator

def get_get_system_template_revisions_paginator() -> GetSystemTemplateRevisionsPaginator:
    return boto3.client("iotthingsgraph").get_paginator("get_system_template_revisions")
```

[Paginator.GetSystemTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)

```python
class GetSystemTemplateRevisionsPaginator(Boto3Paginator):
    def paginate(
        self,
        id: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSystemTemplateRevisionsResponseTypeDef]:
        pass
```
## ListFlowExecutionMessagesPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("list_flow_execution_messages")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import ListFlowExecutionMessagesPaginator

def get_list_flow_execution_messages_paginator() -> ListFlowExecutionMessagesPaginator:
    return boto3.client("iotthingsgraph").get_paginator("list_flow_execution_messages")
```

[Paginator.ListFlowExecutionMessages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)

```python
class ListFlowExecutionMessagesPaginator(Boto3Paginator):
    def paginate(
        self,
        flowExecutionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFlowExecutionMessagesResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("iotthingsgraph").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```
## SearchEntitiesPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("search_entities")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import SearchEntitiesPaginator

def get_search_entities_paginator() -> SearchEntitiesPaginator:
    return boto3.client("iotthingsgraph").get_paginator("search_entities")
```

[Paginator.SearchEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)

```python
class SearchEntitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        entityTypes: List[EntityType],
        filters: List[EntityFilterTypeDef] = None,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchEntitiesResponseTypeDef]:
        pass
```
## SearchFlowExecutionsPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("search_flow_executions")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import SearchFlowExecutionsPaginator

def get_search_flow_executions_paginator() -> SearchFlowExecutionsPaginator:
    return boto3.client("iotthingsgraph").get_paginator("search_flow_executions")
```

[Paginator.SearchFlowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)

```python
class SearchFlowExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchFlowExecutionsResponseTypeDef]:
        pass
```
## SearchFlowTemplatesPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("search_flow_templates")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import SearchFlowTemplatesPaginator

def get_search_flow_templates_paginator() -> SearchFlowTemplatesPaginator:
    return boto3.client("iotthingsgraph").get_paginator("search_flow_templates")
```

[Paginator.SearchFlowTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)

```python
class SearchFlowTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        filters: List[FlowTemplateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchFlowTemplatesResponseTypeDef]:
        pass
```
## SearchSystemInstancesPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("search_system_instances")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import SearchSystemInstancesPaginator

def get_search_system_instances_paginator() -> SearchSystemInstancesPaginator:
    return boto3.client("iotthingsgraph").get_paginator("search_system_instances")
```

[Paginator.SearchSystemInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)

```python
class SearchSystemInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        filters: List[SystemInstanceFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSystemInstancesResponseTypeDef]:
        pass
```
## SearchSystemTemplatesPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("search_system_templates")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import SearchSystemTemplatesPaginator

def get_search_system_templates_paginator() -> SearchSystemTemplatesPaginator:
    return boto3.client("iotthingsgraph").get_paginator("search_system_templates")
```

[Paginator.SearchSystemTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)

```python
class SearchSystemTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        filters: List[SystemTemplateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSystemTemplatesResponseTypeDef]:
        pass
```
## SearchThingsPaginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator("search_things")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import SearchThingsPaginator

def get_search_things_paginator() -> SearchThingsPaginator:
    return boto3.client("iotthingsgraph").get_paginator("search_things")
```

[Paginator.SearchThings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)

```python
class SearchThingsPaginator(Boto3Paginator):
    def paginate(
        self,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchThingsResponseTypeDef]:
        pass
```