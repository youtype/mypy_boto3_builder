# Type annotations for boto3 AugmentedAIRuntime module

> [Index](../index.md) > AugmentedAIRuntime

Auto-generated documentation for [AugmentedAIRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime)
type annotations stubs module [mypy_boto3_sagemaker_a2i_runtime](https://pypi.org/project/mypy-boto3-sagemaker-a2i-runtime/).

```bash
pip install mypy-boto3-sagemaker-a2i-runtime
```

- [Type annotations for boto3 AugmentedAIRuntime module](#type-annotations-for-boto3-augmentedairuntime-module)
  - [AugmentedAIRuntimeClient](#augmentedairuntimeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AugmentedAIRuntimeClient

Type annotations for  `boto3.client("sagemaker-a2i-runtime")` as [AugmentedAIRuntimeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient
```


AugmentedAIRuntimeClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_human_loop](./client.md#delete-human-loop)
- [describe_human_loop](./client.md#describe-human-loop)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_human_loops](./client.md#list-human-loops)
- [start_human_loop](./client.md#start-human-loop)
- [stop_human_loop](./client.md#stop-human-loop)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sagemaker-a2i-runtime").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.paginators import ListHumanLoopsPaginator, ...
```

- [ListHumanLoopsPaginator](./paginators.md#listhumanloopspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.literals import ContentClassifier, ...
```

- [ContentClassifier](./literals.md#contentclassifier)
- [HumanLoopStatus](./literals.md#humanloopstatus)
- [ListHumanLoopsPaginatorName](./literals.md#listhumanloopspaginatorname)
- [SortOrder](./literals.md#sortorder)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopOutputTypeDef, ...
```

- [HumanLoopOutputTypeDef](./type_defs.md#humanloopoutputtypedef)
- [HumanLoopSummaryTypeDef](./type_defs.md#humanloopsummarytypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [DescribeHumanLoopResponseTypeDef](./type_defs.md#describehumanloopresponsetypedef)
- [HumanLoopDataAttributesTypeDef](./type_defs.md#humanloopdataattributestypedef)
- [HumanLoopInputTypeDef](./type_defs.md#humanloopinputtypedef)
- [ListHumanLoopsResponseTypeDef](./type_defs.md#listhumanloopsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartHumanLoopResponseTypeDef](./type_defs.md#starthumanloopresponsetypedef)
