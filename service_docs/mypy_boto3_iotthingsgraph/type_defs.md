# Structures for boto3 IoTThingsGraph module

> [Index](../index.md) > [IoTThingsGraph](./index.md) > Structures

Auto-generated documentation for [IoTThingsGraph](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph)
type annotations stubs module [mypy_boto3_iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/).

- [Structures for boto3 IoTThingsGraph module](#structures-for-boto3-iotthingsgraph-module)
  - [DefinitionDocumentTypeDef](#definitiondocumenttypedef)
  - [DependencyRevisionTypeDef](#dependencyrevisiontypedef)
  - [EntityDescriptionTypeDef](#entitydescriptiontypedef)
  - [FlowExecutionMessageTypeDef](#flowexecutionmessagetypedef)
  - [FlowExecutionSummaryTypeDef](#flowexecutionsummarytypedef)
  - [FlowTemplateDescriptionTypeDef](#flowtemplatedescriptiontypedef)
  - [FlowTemplateSummaryTypeDef](#flowtemplatesummarytypedef)
  - [MetricsConfigurationTypeDef](#metricsconfigurationtypedef)
  - [SystemInstanceDescriptionTypeDef](#systeminstancedescriptiontypedef)
  - [SystemInstanceSummaryTypeDef](#systeminstancesummarytypedef)
  - [SystemTemplateDescriptionTypeDef](#systemtemplatedescriptiontypedef)
  - [SystemTemplateSummaryTypeDef](#systemtemplatesummarytypedef)
  - [TagTypeDef](#tagtypedef)
  - [ThingTypeDef](#thingtypedef)
  - [CreateFlowTemplateResponseTypeDef](#createflowtemplateresponsetypedef)
  - [CreateSystemInstanceResponseTypeDef](#createsysteminstanceresponsetypedef)
  - [CreateSystemTemplateResponseTypeDef](#createsystemtemplateresponsetypedef)
  - [DeleteNamespaceResponseTypeDef](#deletenamespaceresponsetypedef)
  - [DeploySystemInstanceResponseTypeDef](#deploysysteminstanceresponsetypedef)
  - [DescribeNamespaceResponseTypeDef](#describenamespaceresponsetypedef)
  - [EntityFilterTypeDef](#entityfiltertypedef)
  - [FlowTemplateFilterTypeDef](#flowtemplatefiltertypedef)
  - [GetEntitiesResponseTypeDef](#getentitiesresponsetypedef)
  - [GetFlowTemplateResponseTypeDef](#getflowtemplateresponsetypedef)
  - [GetFlowTemplateRevisionsResponseTypeDef](#getflowtemplaterevisionsresponsetypedef)
  - [GetNamespaceDeletionStatusResponseTypeDef](#getnamespacedeletionstatusresponsetypedef)
  - [GetSystemInstanceResponseTypeDef](#getsysteminstanceresponsetypedef)
  - [GetSystemTemplateResponseTypeDef](#getsystemtemplateresponsetypedef)
  - [GetSystemTemplateRevisionsResponseTypeDef](#getsystemtemplaterevisionsresponsetypedef)
  - [GetUploadStatusResponseTypeDef](#getuploadstatusresponsetypedef)
  - [ListFlowExecutionMessagesResponseTypeDef](#listflowexecutionmessagesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [SearchEntitiesResponseTypeDef](#searchentitiesresponsetypedef)
  - [SearchFlowExecutionsResponseTypeDef](#searchflowexecutionsresponsetypedef)
  - [SearchFlowTemplatesResponseTypeDef](#searchflowtemplatesresponsetypedef)
  - [SearchSystemInstancesResponseTypeDef](#searchsysteminstancesresponsetypedef)
  - [SearchSystemTemplatesResponseTypeDef](#searchsystemtemplatesresponsetypedef)
  - [SearchThingsResponseTypeDef](#searchthingsresponsetypedef)
  - [SystemInstanceFilterTypeDef](#systeminstancefiltertypedef)
  - [SystemTemplateFilterTypeDef](#systemtemplatefiltertypedef)
  - [UndeploySystemInstanceResponseTypeDef](#undeploysysteminstanceresponsetypedef)
  - [UpdateFlowTemplateResponseTypeDef](#updateflowtemplateresponsetypedef)
  - [UpdateSystemTemplateResponseTypeDef](#updatesystemtemplateresponsetypedef)
  - [UploadEntityDefinitionsResponseTypeDef](#uploadentitydefinitionsresponsetypedef)

## DefinitionDocumentTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import DefinitionDocumentTypeDef
```


Required fields:
- `language`: `DefinitionLanguage`
- `text`: `str`




## DependencyRevisionTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import DependencyRevisionTypeDef
```




Optional fields:
- `id`: `str`
- `revisionNumber`: `int`


## EntityDescriptionTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import EntityDescriptionTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `type`: `EntityType`
- `createdAt`: `datetime`
- `definition`: `"DefinitionDocumentTypeDef"`


## FlowExecutionMessageTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import FlowExecutionMessageTypeDef
```




Optional fields:
- `messageId`: `str`
- `eventType`: `FlowExecutionEventType`
- `timestamp`: `datetime`
- `payload`: `str`


## FlowExecutionSummaryTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import FlowExecutionSummaryTypeDef
```




Optional fields:
- `flowExecutionId`: `str`
- `status`: `FlowExecutionStatus`
- `systemInstanceId`: `str`
- `flowTemplateId`: `str`
- `createdAt`: `datetime`
- `updatedAt`: `datetime`


## FlowTemplateDescriptionTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import FlowTemplateDescriptionTypeDef
```




Optional fields:
- `summary`: `"FlowTemplateSummaryTypeDef"`
- `definition`: `"DefinitionDocumentTypeDef"`
- `validatedNamespaceVersion`: `int`


## FlowTemplateSummaryTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import FlowTemplateSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `revisionNumber`: `int`
- `createdAt`: `datetime`


## MetricsConfigurationTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import MetricsConfigurationTypeDef
```




Optional fields:
- `cloudMetricEnabled`: `bool`
- `metricRuleRoleArn`: `str`


## SystemInstanceDescriptionTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SystemInstanceDescriptionTypeDef
```




Optional fields:
- `summary`: `"SystemInstanceSummaryTypeDef"`
- `definition`: `"DefinitionDocumentTypeDef"`
- `s3BucketName`: `str`
- `metricsConfiguration`: `"MetricsConfigurationTypeDef"`
- `validatedNamespaceVersion`: `int`
- `validatedDependencyRevisions`: `List["DependencyRevisionTypeDef"]`
- `flowActionsRoleArn`: `str`


## SystemInstanceSummaryTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SystemInstanceSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `status`: `SystemInstanceDeploymentStatus`
- `target`: `DeploymentTarget`
- `greengrassGroupName`: `str`
- `createdAt`: `datetime`
- `updatedAt`: `datetime`
- `greengrassGroupId`: `str`
- `greengrassGroupVersionId`: `str`


## SystemTemplateDescriptionTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SystemTemplateDescriptionTypeDef
```




Optional fields:
- `summary`: `"SystemTemplateSummaryTypeDef"`
- `definition`: `"DefinitionDocumentTypeDef"`
- `validatedNamespaceVersion`: `int`


## SystemTemplateSummaryTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SystemTemplateSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `revisionNumber`: `int`
- `createdAt`: `datetime`


## TagTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## ThingTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import ThingTypeDef
```




Optional fields:
- `thingArn`: `str`
- `thingName`: `str`


## CreateFlowTemplateResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import CreateFlowTemplateResponseTypeDef
```




Optional fields:
- `summary`: `"FlowTemplateSummaryTypeDef"`


## CreateSystemInstanceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import CreateSystemInstanceResponseTypeDef
```




Optional fields:
- `summary`: `"SystemInstanceSummaryTypeDef"`


## CreateSystemTemplateResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import CreateSystemTemplateResponseTypeDef
```




Optional fields:
- `summary`: `"SystemTemplateSummaryTypeDef"`


## DeleteNamespaceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import DeleteNamespaceResponseTypeDef
```




Optional fields:
- `namespaceArn`: `str`
- `namespaceName`: `str`


## DeploySystemInstanceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import DeploySystemInstanceResponseTypeDef
```


Required fields:
- `summary`: `"SystemInstanceSummaryTypeDef"`



Optional fields:
- `greengrassDeploymentId`: `str`


## DescribeNamespaceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import DescribeNamespaceResponseTypeDef
```




Optional fields:
- `namespaceArn`: `str`
- `namespaceName`: `str`
- `trackingNamespaceName`: `str`
- `trackingNamespaceVersion`: `int`
- `namespaceVersion`: `int`


## EntityFilterTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import EntityFilterTypeDef
```




Optional fields:
- `name`: `EntityFilterName`
- `value`: `List[str]`


## FlowTemplateFilterTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import FlowTemplateFilterTypeDef
```


Required fields:
- `name`: `FlowTemplateFilterName`
- `value`: `List[str]`




## GetEntitiesResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetEntitiesResponseTypeDef
```




Optional fields:
- `descriptions`: `List["EntityDescriptionTypeDef"]`


## GetFlowTemplateResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetFlowTemplateResponseTypeDef
```




Optional fields:
- `description`: `"FlowTemplateDescriptionTypeDef"`


## GetFlowTemplateRevisionsResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetFlowTemplateRevisionsResponseTypeDef
```




Optional fields:
- `summaries`: `List["FlowTemplateSummaryTypeDef"]`
- `nextToken`: `str`


## GetNamespaceDeletionStatusResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetNamespaceDeletionStatusResponseTypeDef
```




Optional fields:
- `namespaceArn`: `str`
- `namespaceName`: `str`
- `status`: `NamespaceDeletionStatus`
- `errorCode`: `NamespaceDeletionStatusErrorCodes`
- `errorMessage`: `str`


## GetSystemInstanceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetSystemInstanceResponseTypeDef
```




Optional fields:
- `description`: `"SystemInstanceDescriptionTypeDef"`


## GetSystemTemplateResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetSystemTemplateResponseTypeDef
```




Optional fields:
- `description`: `"SystemTemplateDescriptionTypeDef"`


## GetSystemTemplateRevisionsResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetSystemTemplateRevisionsResponseTypeDef
```




Optional fields:
- `summaries`: `List["SystemTemplateSummaryTypeDef"]`
- `nextToken`: `str`


## GetUploadStatusResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import GetUploadStatusResponseTypeDef
```


Required fields:
- `uploadId`: `str`
- `uploadStatus`: `UploadStatus`
- `createdDate`: `datetime`



Optional fields:
- `namespaceArn`: `str`
- `namespaceName`: `str`
- `namespaceVersion`: `int`
- `failureReason`: `List[str]`


## ListFlowExecutionMessagesResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import ListFlowExecutionMessagesResponseTypeDef
```




Optional fields:
- `messages`: `List["FlowExecutionMessageTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## SearchEntitiesResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SearchEntitiesResponseTypeDef
```




Optional fields:
- `descriptions`: `List["EntityDescriptionTypeDef"]`
- `nextToken`: `str`


## SearchFlowExecutionsResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SearchFlowExecutionsResponseTypeDef
```




Optional fields:
- `summaries`: `List["FlowExecutionSummaryTypeDef"]`
- `nextToken`: `str`


## SearchFlowTemplatesResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SearchFlowTemplatesResponseTypeDef
```




Optional fields:
- `summaries`: `List["FlowTemplateSummaryTypeDef"]`
- `nextToken`: `str`


## SearchSystemInstancesResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SearchSystemInstancesResponseTypeDef
```




Optional fields:
- `summaries`: `List["SystemInstanceSummaryTypeDef"]`
- `nextToken`: `str`


## SearchSystemTemplatesResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SearchSystemTemplatesResponseTypeDef
```




Optional fields:
- `summaries`: `List["SystemTemplateSummaryTypeDef"]`
- `nextToken`: `str`


## SearchThingsResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SearchThingsResponseTypeDef
```




Optional fields:
- `things`: `List["ThingTypeDef"]`
- `nextToken`: `str`


## SystemInstanceFilterTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SystemInstanceFilterTypeDef
```




Optional fields:
- `name`: `SystemInstanceFilterName`
- `value`: `List[str]`


## SystemTemplateFilterTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import SystemTemplateFilterTypeDef
```


Required fields:
- `name`: `SystemTemplateFilterName`
- `value`: `List[str]`




## UndeploySystemInstanceResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import UndeploySystemInstanceResponseTypeDef
```




Optional fields:
- `summary`: `"SystemInstanceSummaryTypeDef"`


## UpdateFlowTemplateResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import UpdateFlowTemplateResponseTypeDef
```




Optional fields:
- `summary`: `"FlowTemplateSummaryTypeDef"`


## UpdateSystemTemplateResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import UpdateSystemTemplateResponseTypeDef
```




Optional fields:
- `summary`: `"SystemTemplateSummaryTypeDef"`


## UploadEntityDefinitionsResponseTypeDef

```python
from mypy_boto3_iotthingsgraph.type_defs import UploadEntityDefinitionsResponseTypeDef
```


Required fields:
- `uploadId`: `str`



