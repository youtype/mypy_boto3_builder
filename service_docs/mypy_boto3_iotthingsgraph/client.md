# IoTThingsGraphClient for boto3 IoTThingsGraph module

> [Index](../index.md) > [IoTThingsGraph](./index.md) > IoTThingsGraphClient

Auto-generated documentation for [IoTThingsGraph](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph)
type annotations stubs module [mypy_boto3_iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/).

- [IoTThingsGraphClient for boto3 IoTThingsGraph module](#iotthingsgraphclient-for-boto3-iotthingsgraph-module)
  - [IoTThingsGraphClient](#iotthingsgraphclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_entity_to_thing](#associate_entity_to_thing)
    - [can_paginate](#can_paginate)
    - [create_flow_template](#create_flow_template)
    - [create_system_instance](#create_system_instance)
    - [create_system_template](#create_system_template)
    - [delete_flow_template](#delete_flow_template)
    - [delete_namespace](#delete_namespace)
    - [delete_system_instance](#delete_system_instance)
    - [delete_system_template](#delete_system_template)
    - [deploy_system_instance](#deploy_system_instance)
    - [deprecate_flow_template](#deprecate_flow_template)
    - [deprecate_system_template](#deprecate_system_template)
    - [describe_namespace](#describe_namespace)
    - [dissociate_entity_from_thing](#dissociate_entity_from_thing)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_entities](#get_entities)
    - [get_flow_template](#get_flow_template)
    - [get_flow_template_revisions](#get_flow_template_revisions)
    - [get_namespace_deletion_status](#get_namespace_deletion_status)
    - [get_system_instance](#get_system_instance)
    - [get_system_template](#get_system_template)
    - [get_system_template_revisions](#get_system_template_revisions)
    - [get_upload_status](#get_upload_status)
    - [list_flow_execution_messages](#list_flow_execution_messages)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [search_entities](#search_entities)
    - [search_flow_executions](#search_flow_executions)
    - [search_flow_templates](#search_flow_templates)
    - [search_system_instances](#search_system_instances)
    - [search_system_templates](#search_system_templates)
    - [search_things](#search_things)
    - [tag_resource](#tag_resource)
    - [undeploy_system_instance](#undeploy_system_instance)
    - [untag_resource](#untag_resource)
    - [update_flow_template](#update_flow_template)
    - [update_system_template](#update_system_template)
    - [upload_entity_definitions](#upload_entity_definitions)
    - [get_paginator](#get_paginator)

## IoTThingsGraphClient

Type annotations for `boto3.client("iotthingsgraph")`

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.client import IoTThingsGraphClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotthingsgraph.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`


## Methods


### associate_entity_to_thing

Type annotations for `boto3.client("iotthingsgraph").associate_entity_to_thing` method.

[Client.associate_entity_to_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.associate_entity_to_thing)

```python
def associate_entity_to_thing(
    self,
    thingName: str,
    entityId: str,
    namespaceVersion: int = None
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("iotthingsgraph").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_flow_template

Type annotations for `boto3.client("iotthingsgraph").create_flow_template` method.

[Client.create_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_flow_template)

```python
def create_flow_template(
    self,
    definition: "DefinitionDocumentTypeDef",
    compatibleNamespaceVersion: int = None
) -> CreateFlowTemplateResponseTypeDef:
    pass
```

### create_system_instance

Type annotations for `boto3.client("iotthingsgraph").create_system_instance` method.

[Client.create_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_instance)

```python
def create_system_instance(
    self,
    definition: "DefinitionDocumentTypeDef",
    target: DeploymentTarget,
    tags: List["TagTypeDef"] = None,
    greengrassGroupName: str = None,
    s3BucketName: str = None,
    metricsConfiguration: "MetricsConfigurationTypeDef" = None,
    flowActionsRoleArn: str = None
) -> CreateSystemInstanceResponseTypeDef:
    pass
```

### create_system_template

Type annotations for `boto3.client("iotthingsgraph").create_system_template` method.

[Client.create_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_template)

```python
def create_system_template(
    self,
    definition: "DefinitionDocumentTypeDef",
    compatibleNamespaceVersion: int = None
) -> CreateSystemTemplateResponseTypeDef:
    pass
```

### delete_flow_template

Type annotations for `boto3.client("iotthingsgraph").delete_flow_template` method.

[Client.delete_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_flow_template)

```python
def delete_flow_template(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### delete_namespace

Type annotations for `boto3.client("iotthingsgraph").delete_namespace` method.

[Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_namespace)

```python
def delete_namespace(
    self
) -> DeleteNamespaceResponseTypeDef:
    pass
```

### delete_system_instance

Type annotations for `boto3.client("iotthingsgraph").delete_system_instance` method.

[Client.delete_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_instance)

```python
def delete_system_instance(
    self,
    id: str = None
) -> Dict[str, Any]:
    pass
```

### delete_system_template

Type annotations for `boto3.client("iotthingsgraph").delete_system_template` method.

[Client.delete_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_template)

```python
def delete_system_template(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### deploy_system_instance

Type annotations for `boto3.client("iotthingsgraph").deploy_system_instance` method.

[Client.deploy_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deploy_system_instance)

```python
def deploy_system_instance(
    self,
    id: str = None
) -> DeploySystemInstanceResponseTypeDef:
    pass
```

### deprecate_flow_template

Type annotations for `boto3.client("iotthingsgraph").deprecate_flow_template` method.

[Client.deprecate_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_flow_template)

```python
def deprecate_flow_template(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### deprecate_system_template

Type annotations for `boto3.client("iotthingsgraph").deprecate_system_template` method.

[Client.deprecate_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_system_template)

```python
def deprecate_system_template(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### describe_namespace

Type annotations for `boto3.client("iotthingsgraph").describe_namespace` method.

[Client.describe_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.describe_namespace)

```python
def describe_namespace(
    self,
    namespaceName: str = None
) -> DescribeNamespaceResponseTypeDef:
    pass
```

### dissociate_entity_from_thing

Type annotations for `boto3.client("iotthingsgraph").dissociate_entity_from_thing` method.

[Client.dissociate_entity_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.dissociate_entity_from_thing)

```python
def dissociate_entity_from_thing(
    self,
    thingName: str,
    entityType: EntityType
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotthingsgraph").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.generate_presigned_url)

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

### get_entities

Type annotations for `boto3.client("iotthingsgraph").get_entities` method.

[Client.get_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_entities)

```python
def get_entities(
    self,
    ids: List[str],
    namespaceVersion: int = None
) -> GetEntitiesResponseTypeDef:
    pass
```

### get_flow_template

Type annotations for `boto3.client("iotthingsgraph").get_flow_template` method.

[Client.get_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template)

```python
def get_flow_template(
    self,
    id: str,
    revisionNumber: int = None
) -> GetFlowTemplateResponseTypeDef:
    pass
```

### get_flow_template_revisions

Type annotations for `boto3.client("iotthingsgraph").get_flow_template_revisions` method.

[Client.get_flow_template_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template_revisions)

```python
def get_flow_template_revisions(
    self,
    id: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetFlowTemplateRevisionsResponseTypeDef:
    pass
```

### get_namespace_deletion_status

Type annotations for `boto3.client("iotthingsgraph").get_namespace_deletion_status` method.

[Client.get_namespace_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_namespace_deletion_status)

```python
def get_namespace_deletion_status(
    self
) -> GetNamespaceDeletionStatusResponseTypeDef:
    pass
```

### get_system_instance

Type annotations for `boto3.client("iotthingsgraph").get_system_instance` method.

[Client.get_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_instance)

```python
def get_system_instance(
    self,
    id: str
) -> GetSystemInstanceResponseTypeDef:
    pass
```

### get_system_template

Type annotations for `boto3.client("iotthingsgraph").get_system_template` method.

[Client.get_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template)

```python
def get_system_template(
    self,
    id: str,
    revisionNumber: int = None
) -> GetSystemTemplateResponseTypeDef:
    pass
```

### get_system_template_revisions

Type annotations for `boto3.client("iotthingsgraph").get_system_template_revisions` method.

[Client.get_system_template_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template_revisions)

```python
def get_system_template_revisions(
    self,
    id: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetSystemTemplateRevisionsResponseTypeDef:
    pass
```

### get_upload_status

Type annotations for `boto3.client("iotthingsgraph").get_upload_status` method.

[Client.get_upload_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_upload_status)

```python
def get_upload_status(
    self,
    uploadId: str
) -> GetUploadStatusResponseTypeDef:
    pass
```

### list_flow_execution_messages

Type annotations for `boto3.client("iotthingsgraph").list_flow_execution_messages` method.

[Client.list_flow_execution_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_flow_execution_messages)

```python
def list_flow_execution_messages(
    self,
    flowExecutionId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListFlowExecutionMessagesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotthingsgraph").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### search_entities

Type annotations for `boto3.client("iotthingsgraph").search_entities` method.

[Client.search_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_entities)

```python
def search_entities(
    self,
    entityTypes: List[EntityType],
    filters: List[EntityFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None,
    namespaceVersion: int = None
) -> SearchEntitiesResponseTypeDef:
    pass
```

### search_flow_executions

Type annotations for `boto3.client("iotthingsgraph").search_flow_executions` method.

[Client.search_flow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_executions)

```python
def search_flow_executions(
    self,
    systemInstanceId: str,
    flowExecutionId: str = None,
    startTime: datetime = None,
    endTime: datetime = None,
    nextToken: str = None,
    maxResults: int = None
) -> SearchFlowExecutionsResponseTypeDef:
    pass
```

### search_flow_templates

Type annotations for `boto3.client("iotthingsgraph").search_flow_templates` method.

[Client.search_flow_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_templates)

```python
def search_flow_templates(
    self,
    filters: List[FlowTemplateFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> SearchFlowTemplatesResponseTypeDef:
    pass
```

### search_system_instances

Type annotations for `boto3.client("iotthingsgraph").search_system_instances` method.

[Client.search_system_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_instances)

```python
def search_system_instances(
    self,
    filters: List[SystemInstanceFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> SearchSystemInstancesResponseTypeDef:
    pass
```

### search_system_templates

Type annotations for `boto3.client("iotthingsgraph").search_system_templates` method.

[Client.search_system_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_templates)

```python
def search_system_templates(
    self,
    filters: List[SystemTemplateFilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> SearchSystemTemplatesResponseTypeDef:
    pass
```

### search_things

Type annotations for `boto3.client("iotthingsgraph").search_things` method.

[Client.search_things documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_things)

```python
def search_things(
    self,
    entityId: str,
    nextToken: str = None,
    maxResults: int = None,
    namespaceVersion: int = None
) -> SearchThingsResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotthingsgraph").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### undeploy_system_instance

Type annotations for `boto3.client("iotthingsgraph").undeploy_system_instance` method.

[Client.undeploy_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.undeploy_system_instance)

```python
def undeploy_system_instance(
    self,
    id: str = None
) -> UndeploySystemInstanceResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotthingsgraph").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_flow_template

Type annotations for `boto3.client("iotthingsgraph").update_flow_template` method.

[Client.update_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_flow_template)

```python
def update_flow_template(
    self,
    id: str,
    definition: "DefinitionDocumentTypeDef",
    compatibleNamespaceVersion: int = None
) -> UpdateFlowTemplateResponseTypeDef:
    pass
```

### update_system_template

Type annotations for `boto3.client("iotthingsgraph").update_system_template` method.

[Client.update_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_system_template)

```python
def update_system_template(
    self,
    id: str,
    definition: "DefinitionDocumentTypeDef",
    compatibleNamespaceVersion: int = None
) -> UpdateSystemTemplateResponseTypeDef:
    pass
```

### upload_entity_definitions

Type annotations for `boto3.client("iotthingsgraph").upload_entity_definitions` method.

[Client.upload_entity_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.upload_entity_definitions)

```python
def upload_entity_definitions(
    self,
    document: "DefinitionDocumentTypeDef" = None,
    syncWithPublicNamespace: bool = None,
    deprecateExistingEntities: bool = None
) -> UploadEntityDefinitionsResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("iotthingsgraph").get_paginator` method with overloads.

- `client.get_paginator("get_flow_template_revisions")` -> [GetFlowTemplateRevisionsPaginator](./paginators.md#getflowtemplaterevisionspaginator)
- `client.get_paginator("get_system_template_revisions")` -> [GetSystemTemplateRevisionsPaginator](./paginators.md#getsystemtemplaterevisionspaginator)
- `client.get_paginator("list_flow_execution_messages")` -> [ListFlowExecutionMessagesPaginator](./paginators.md#listflowexecutionmessagespaginator)
- `client.get_paginator("list_tags_for_resource")` -> [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- `client.get_paginator("search_entities")` -> [SearchEntitiesPaginator](./paginators.md#searchentitiespaginator)
- `client.get_paginator("search_flow_executions")` -> [SearchFlowExecutionsPaginator](./paginators.md#searchflowexecutionspaginator)
- `client.get_paginator("search_flow_templates")` -> [SearchFlowTemplatesPaginator](./paginators.md#searchflowtemplatespaginator)
- `client.get_paginator("search_system_instances")` -> [SearchSystemInstancesPaginator](./paginators.md#searchsysteminstancespaginator)
- `client.get_paginator("search_system_templates")` -> [SearchSystemTemplatesPaginator](./paginators.md#searchsystemtemplatespaginator)
- `client.get_paginator("search_things")` -> [SearchThingsPaginator](./paginators.md#searchthingspaginator)


