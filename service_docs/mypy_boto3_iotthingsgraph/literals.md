# Literals for boto3 IoTThingsGraph module

> [Index](../index.md) > [IoTThingsGraph](./index.md) > Literals

Auto-generated documentation for [IoTThingsGraph](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph)
type annotations stubs module [mypy_boto3_iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/).

- [Literals for boto3 IoTThingsGraph module](#literals-for-boto3-iotthingsgraph-module)
  - [DefinitionLanguage](#definitionlanguage)
  - [DeploymentTarget](#deploymenttarget)
  - [EntityFilterName](#entityfiltername)
  - [EntityType](#entitytype)
  - [FlowExecutionEventType](#flowexecutioneventtype)
  - [FlowExecutionStatus](#flowexecutionstatus)
  - [FlowTemplateFilterName](#flowtemplatefiltername)
  - [GetFlowTemplateRevisionsPaginatorName](#getflowtemplaterevisionspaginatorname)
  - [GetSystemTemplateRevisionsPaginatorName](#getsystemtemplaterevisionspaginatorname)
  - [ListFlowExecutionMessagesPaginatorName](#listflowexecutionmessagespaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [NamespaceDeletionStatus](#namespacedeletionstatus)
  - [NamespaceDeletionStatusErrorCodes](#namespacedeletionstatuserrorcodes)
  - [SearchEntitiesPaginatorName](#searchentitiespaginatorname)
  - [SearchFlowExecutionsPaginatorName](#searchflowexecutionspaginatorname)
  - [SearchFlowTemplatesPaginatorName](#searchflowtemplatespaginatorname)
  - [SearchSystemInstancesPaginatorName](#searchsysteminstancespaginatorname)
  - [SearchSystemTemplatesPaginatorName](#searchsystemtemplatespaginatorname)
  - [SearchThingsPaginatorName](#searchthingspaginatorname)
  - [SystemInstanceDeploymentStatus](#systeminstancedeploymentstatus)
  - [SystemInstanceFilterName](#systeminstancefiltername)
  - [SystemTemplateFilterName](#systemtemplatefiltername)
  - [UploadStatus](#uploadstatus)

## DefinitionLanguage

```python
from mypy_boto3_iotthingsgraph.literals import DefinitionLanguage
```

Values:

- `GRAPHQL`

## DeploymentTarget

```python
from mypy_boto3_iotthingsgraph.literals import DeploymentTarget
```

Values:

- `CLOUD`
- `GREENGRASS`

## EntityFilterName

```python
from mypy_boto3_iotthingsgraph.literals import EntityFilterName
```

Values:

- `NAME`
- `NAMESPACE`
- `REFERENCED_ENTITY_ID`
- `SEMANTIC_TYPE_PATH`

## EntityType

```python
from mypy_boto3_iotthingsgraph.literals import EntityType
```

Values:

- `ACTION`
- `CAPABILITY`
- `DEVICE`
- `DEVICE_MODEL`
- `ENUM`
- `EVENT`
- `MAPPING`
- `PROPERTY`
- `SERVICE`
- `STATE`

## FlowExecutionEventType

```python
from mypy_boto3_iotthingsgraph.literals import FlowExecutionEventType
```

Values:

- `ACKNOWLEDGE_TASK_MESSAGE`
- `ACTIVITY_FAILED`
- `ACTIVITY_SCHEDULED`
- `ACTIVITY_STARTED`
- `ACTIVITY_SUCCEEDED`
- `EXECUTION_ABORTED`
- `EXECUTION_FAILED`
- `EXECUTION_STARTED`
- `EXECUTION_SUCCEEDED`
- `SCHEDULE_NEXT_READY_STEPS_TASK`
- `START_FLOW_EXECUTION_TASK`
- `STEP_FAILED`
- `STEP_STARTED`
- `STEP_SUCCEEDED`
- `THING_ACTION_TASK`
- `THING_ACTION_TASK_FAILED`
- `THING_ACTION_TASK_SUCCEEDED`

## FlowExecutionStatus

```python
from mypy_boto3_iotthingsgraph.literals import FlowExecutionStatus
```

Values:

- `ABORTED`
- `FAILED`
- `RUNNING`
- `SUCCEEDED`

## FlowTemplateFilterName

```python
from mypy_boto3_iotthingsgraph.literals import FlowTemplateFilterName
```

Values:

- `DEVICE_MODEL_ID`

## GetFlowTemplateRevisionsPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import GetFlowTemplateRevisionsPaginatorName
```

Values:

- `get_flow_template_revisions`

## GetSystemTemplateRevisionsPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import GetSystemTemplateRevisionsPaginatorName
```

Values:

- `get_system_template_revisions`

## ListFlowExecutionMessagesPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import ListFlowExecutionMessagesPaginatorName
```

Values:

- `list_flow_execution_messages`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## NamespaceDeletionStatus

```python
from mypy_boto3_iotthingsgraph.literals import NamespaceDeletionStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`

## NamespaceDeletionStatusErrorCodes

```python
from mypy_boto3_iotthingsgraph.literals import NamespaceDeletionStatusErrorCodes
```

Values:

- `VALIDATION_FAILED`

## SearchEntitiesPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import SearchEntitiesPaginatorName
```

Values:

- `search_entities`

## SearchFlowExecutionsPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import SearchFlowExecutionsPaginatorName
```

Values:

- `search_flow_executions`

## SearchFlowTemplatesPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import SearchFlowTemplatesPaginatorName
```

Values:

- `search_flow_templates`

## SearchSystemInstancesPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import SearchSystemInstancesPaginatorName
```

Values:

- `search_system_instances`

## SearchSystemTemplatesPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import SearchSystemTemplatesPaginatorName
```

Values:

- `search_system_templates`

## SearchThingsPaginatorName

```python
from mypy_boto3_iotthingsgraph.literals import SearchThingsPaginatorName
```

Values:

- `search_things`

## SystemInstanceDeploymentStatus

```python
from mypy_boto3_iotthingsgraph.literals import SystemInstanceDeploymentStatus
```

Values:

- `BOOTSTRAP`
- `DELETED_IN_TARGET`
- `DEPLOY_IN_PROGRESS`
- `DEPLOYED_IN_TARGET`
- `FAILED`
- `NOT_DEPLOYED`
- `PENDING_DELETE`
- `UNDEPLOY_IN_PROGRESS`

## SystemInstanceFilterName

```python
from mypy_boto3_iotthingsgraph.literals import SystemInstanceFilterName
```

Values:

- `GREENGRASS_GROUP_NAME`
- `STATUS`
- `SYSTEM_TEMPLATE_ID`

## SystemTemplateFilterName

```python
from mypy_boto3_iotthingsgraph.literals import SystemTemplateFilterName
```

Values:

- `FLOW_TEMPLATE_ID`

## UploadStatus

```python
from mypy_boto3_iotthingsgraph.literals import UploadStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`
