# Type annotations for boto3 DataPipeline module

> [Index](../index.md) > DataPipeline

Auto-generated documentation for [DataPipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline)
type annotations stubs module [mypy_boto3_datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/).

```bash
pip install mypy-boto3-datapipeline
```

- [Type annotations for boto3 DataPipeline module](#type-annotations-for-boto3-datapipeline-module)
  - [DataPipelineClient](#datapipelineclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DataPipelineClient

Type annotations for  `boto3.client("datapipeline")` as [DataPipelineClient](./client.md)

Can be used directly:

```python
from mypy_boto3_datapipeline.client import DataPipelineClient
```


DataPipelineClient [exceptions](./client.md#exceptions)



### Methods
- [activate_pipeline](./client.md#activate-pipeline)
- [add_tags](./client.md#add-tags)
- [can_paginate](./client.md#can-paginate)
- [create_pipeline](./client.md#create-pipeline)
- [deactivate_pipeline](./client.md#deactivate-pipeline)
- [delete_pipeline](./client.md#delete-pipeline)
- [describe_objects](./client.md#describe-objects)
- [describe_pipelines](./client.md#describe-pipelines)
- [evaluate_expression](./client.md#evaluate-expression)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_pipeline_definition](./client.md#get-pipeline-definition)
- [list_pipelines](./client.md#list-pipelines)
- [poll_for_task](./client.md#poll-for-task)
- [put_pipeline_definition](./client.md#put-pipeline-definition)
- [query_objects](./client.md#query-objects)
- [remove_tags](./client.md#remove-tags)
- [report_task_progress](./client.md#report-task-progress)
- [report_task_runner_heartbeat](./client.md#report-task-runner-heartbeat)
- [set_status](./client.md#set-status)
- [set_task_status](./client.md#set-task-status)
- [validate_pipeline_definition](./client.md#validate-pipeline-definition)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServiceError](./client.md#internalserviceerror)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [PipelineDeletedException](./client.md#pipelinedeletedexception)
- [PipelineNotFoundException](./client.md#pipelinenotfoundexception)
- [TaskNotFoundException](./client.md#tasknotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("datapipeline").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_datapipeline.paginators import DescribeObjectsPaginator, ...
```

- [DescribeObjectsPaginator](./paginators.md#describeobjectspaginator)
- [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)
- [QueryObjectsPaginator](./paginators.md#queryobjectspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_datapipeline.literals import DescribeObjectsPaginatorName, ...
```

- [DescribeObjectsPaginatorName](./literals.md#describeobjectspaginatorname)
- [ListPipelinesPaginatorName](./literals.md#listpipelinespaginatorname)
- [OperatorType](./literals.md#operatortype)
- [QueryObjectsPaginatorName](./literals.md#queryobjectspaginatorname)
- [TaskStatus](./literals.md#taskstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_datapipeline.type_defs import FieldTypeDef, ...
```

- [FieldTypeDef](./type_defs.md#fieldtypedef)
- [OperatorTypeDef](./type_defs.md#operatortypedef)
- [ParameterAttributeTypeDef](./type_defs.md#parameterattributetypedef)
- [ParameterObjectTypeDef](./type_defs.md#parameterobjecttypedef)
- [ParameterValueTypeDef](./type_defs.md#parametervaluetypedef)
- [PipelineDescriptionTypeDef](./type_defs.md#pipelinedescriptiontypedef)
- [PipelineIdNameTypeDef](./type_defs.md#pipelineidnametypedef)
- [PipelineObjectTypeDef](./type_defs.md#pipelineobjecttypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SelectorTypeDef](./type_defs.md#selectortypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TaskObjectTypeDef](./type_defs.md#taskobjecttypedef)
- [ValidationErrorTypeDef](./type_defs.md#validationerrortypedef)
- [ValidationWarningTypeDef](./type_defs.md#validationwarningtypedef)
- [CreatePipelineOutputTypeDef](./type_defs.md#createpipelineoutputtypedef)
- [DescribeObjectsOutputTypeDef](./type_defs.md#describeobjectsoutputtypedef)
- [DescribePipelinesOutputTypeDef](./type_defs.md#describepipelinesoutputtypedef)
- [EvaluateExpressionOutputTypeDef](./type_defs.md#evaluateexpressionoutputtypedef)
- [GetPipelineDefinitionOutputTypeDef](./type_defs.md#getpipelinedefinitionoutputtypedef)
- [InstanceIdentityTypeDef](./type_defs.md#instanceidentitytypedef)
- [ListPipelinesOutputTypeDef](./type_defs.md#listpipelinesoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PollForTaskOutputTypeDef](./type_defs.md#pollfortaskoutputtypedef)
- [PutPipelineDefinitionOutputTypeDef](./type_defs.md#putpipelinedefinitionoutputtypedef)
- [QueryObjectsOutputTypeDef](./type_defs.md#queryobjectsoutputtypedef)
- [QueryTypeDef](./type_defs.md#querytypedef)
- [ReportTaskProgressOutputTypeDef](./type_defs.md#reporttaskprogressoutputtypedef)
- [ReportTaskRunnerHeartbeatOutputTypeDef](./type_defs.md#reporttaskrunnerheartbeatoutputtypedef)
- [ValidatePipelineDefinitionOutputTypeDef](./type_defs.md#validatepipelinedefinitionoutputtypedef)
