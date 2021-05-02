# Structures for boto3 DataPipeline module

> [Index](../index.md) > [DataPipeline](./index.md) > Structures

Auto-generated documentation for [DataPipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline)
type annotations stubs module [mypy_boto3_datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/).

- [Structures for boto3 DataPipeline module](#structures-for-boto3-datapipeline-module)
  - [FieldTypeDef](#fieldtypedef)
  - [OperatorTypeDef](#operatortypedef)
  - [ParameterAttributeTypeDef](#parameterattributetypedef)
  - [ParameterObjectTypeDef](#parameterobjecttypedef)
  - [ParameterValueTypeDef](#parametervaluetypedef)
  - [PipelineDescriptionTypeDef](#pipelinedescriptiontypedef)
  - [PipelineIdNameTypeDef](#pipelineidnametypedef)
  - [PipelineObjectTypeDef](#pipelineobjecttypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SelectorTypeDef](#selectortypedef)
  - [TagTypeDef](#tagtypedef)
  - [TaskObjectTypeDef](#taskobjecttypedef)
  - [ValidationErrorTypeDef](#validationerrortypedef)
  - [ValidationWarningTypeDef](#validationwarningtypedef)
  - [CreatePipelineOutputTypeDef](#createpipelineoutputtypedef)
  - [DescribeObjectsOutputTypeDef](#describeobjectsoutputtypedef)
  - [DescribePipelinesOutputTypeDef](#describepipelinesoutputtypedef)
  - [EvaluateExpressionOutputTypeDef](#evaluateexpressionoutputtypedef)
  - [GetPipelineDefinitionOutputTypeDef](#getpipelinedefinitionoutputtypedef)
  - [InstanceIdentityTypeDef](#instanceidentitytypedef)
  - [ListPipelinesOutputTypeDef](#listpipelinesoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PollForTaskOutputTypeDef](#pollfortaskoutputtypedef)
  - [PutPipelineDefinitionOutputTypeDef](#putpipelinedefinitionoutputtypedef)
  - [QueryObjectsOutputTypeDef](#queryobjectsoutputtypedef)
  - [QueryTypeDef](#querytypedef)
  - [ReportTaskProgressOutputTypeDef](#reporttaskprogressoutputtypedef)
  - [ReportTaskRunnerHeartbeatOutputTypeDef](#reporttaskrunnerheartbeatoutputtypedef)
  - [ValidatePipelineDefinitionOutputTypeDef](#validatepipelinedefinitionoutputtypedef)

## FieldTypeDef

```python
from mypy_boto3_datapipeline.type_defs import FieldTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `stringValue`: `str`
- `refValue`: `str`


## OperatorTypeDef

```python
from mypy_boto3_datapipeline.type_defs import OperatorTypeDef
```




Optional fields:
- `type`: `OperatorType`
- `values`: `List[str]`


## ParameterAttributeTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ParameterAttributeTypeDef
```


Required fields:
- `key`: `str`
- `stringValue`: `str`




## ParameterObjectTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ParameterObjectTypeDef
```


Required fields:
- `id`: `str`
- `attributes`: `List["ParameterAttributeTypeDef"]`




## ParameterValueTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ParameterValueTypeDef
```


Required fields:
- `id`: `str`
- `stringValue`: `str`




## PipelineDescriptionTypeDef

```python
from mypy_boto3_datapipeline.type_defs import PipelineDescriptionTypeDef
```


Required fields:
- `pipelineId`: `str`
- `name`: `str`
- `fields`: `List["FieldTypeDef"]`



Optional fields:
- `description`: `str`
- `tags`: `List["TagTypeDef"]`


## PipelineIdNameTypeDef

```python
from mypy_boto3_datapipeline.type_defs import PipelineIdNameTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`


## PipelineObjectTypeDef

```python
from mypy_boto3_datapipeline.type_defs import PipelineObjectTypeDef
```


Required fields:
- `id`: `str`
- `name`: `str`
- `fields`: `List["FieldTypeDef"]`




## ResponseMetadata

```python
from mypy_boto3_datapipeline.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SelectorTypeDef

```python
from mypy_boto3_datapipeline.type_defs import SelectorTypeDef
```




Optional fields:
- `fieldName`: `str`
- `operator`: `"OperatorTypeDef"`


## TagTypeDef

```python
from mypy_boto3_datapipeline.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## TaskObjectTypeDef

```python
from mypy_boto3_datapipeline.type_defs import TaskObjectTypeDef
```




Optional fields:
- `taskId`: `str`
- `pipelineId`: `str`
- `attemptId`: `str`
- `objects`: `Dict[str, "PipelineObjectTypeDef"]`


## ValidationErrorTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ValidationErrorTypeDef
```




Optional fields:
- `id`: `str`
- `errors`: `List[str]`


## ValidationWarningTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ValidationWarningTypeDef
```




Optional fields:
- `id`: `str`
- `warnings`: `List[str]`


## CreatePipelineOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import CreatePipelineOutputTypeDef
```


Required fields:
- `pipelineId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeObjectsOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import DescribeObjectsOutputTypeDef
```


Required fields:
- `pipelineObjects`: `List["PipelineObjectTypeDef"]`



Optional fields:
- `marker`: `str`
- `hasMoreResults`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePipelinesOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import DescribePipelinesOutputTypeDef
```


Required fields:
- `pipelineDescriptionList`: `List["PipelineDescriptionTypeDef"]`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## EvaluateExpressionOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import EvaluateExpressionOutputTypeDef
```


Required fields:
- `evaluatedExpression`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPipelineDefinitionOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import GetPipelineDefinitionOutputTypeDef
```




Optional fields:
- `pipelineObjects`: `List["PipelineObjectTypeDef"]`
- `parameterObjects`: `List["ParameterObjectTypeDef"]`
- `parameterValues`: `List["ParameterValueTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## InstanceIdentityTypeDef

```python
from mypy_boto3_datapipeline.type_defs import InstanceIdentityTypeDef
```




Optional fields:
- `document`: `str`
- `signature`: `str`


## ListPipelinesOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ListPipelinesOutputTypeDef
```


Required fields:
- `pipelineIdList`: `List["PipelineIdNameTypeDef"]`



Optional fields:
- `marker`: `str`
- `hasMoreResults`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_datapipeline.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PollForTaskOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import PollForTaskOutputTypeDef
```




Optional fields:
- `taskObject`: `"TaskObjectTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutPipelineDefinitionOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import PutPipelineDefinitionOutputTypeDef
```


Required fields:
- `errored`: `bool`



Optional fields:
- `validationErrors`: `List["ValidationErrorTypeDef"]`
- `validationWarnings`: `List["ValidationWarningTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## QueryObjectsOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import QueryObjectsOutputTypeDef
```




Optional fields:
- `ids`: `List[str]`
- `marker`: `str`
- `hasMoreResults`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## QueryTypeDef

```python
from mypy_boto3_datapipeline.type_defs import QueryTypeDef
```




Optional fields:
- `selectors`: `List["SelectorTypeDef"]`


## ReportTaskProgressOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ReportTaskProgressOutputTypeDef
```


Required fields:
- `canceled`: `bool`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ReportTaskRunnerHeartbeatOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ReportTaskRunnerHeartbeatOutputTypeDef
```


Required fields:
- `terminate`: `bool`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ValidatePipelineDefinitionOutputTypeDef

```python
from mypy_boto3_datapipeline.type_defs import ValidatePipelineDefinitionOutputTypeDef
```


Required fields:
- `errored`: `bool`



Optional fields:
- `validationErrors`: `List["ValidationErrorTypeDef"]`
- `validationWarnings`: `List["ValidationWarningTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`

