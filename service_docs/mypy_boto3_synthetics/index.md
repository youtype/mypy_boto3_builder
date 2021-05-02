# Type annotations for boto3 Synthetics module

> [Index](../index.md) > Synthetics

Auto-generated documentation for [Synthetics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html#Synthetics)
type annotations stubs module [mypy_boto3_synthetics](https://pypi.org/project/mypy-boto3-synthetics/).

```bash
pip install mypy-boto3-synthetics
```

- [Type annotations for boto3 Synthetics module](#type-annotations-for-boto3-synthetics-module)
  - [SyntheticsClient](#syntheticsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## SyntheticsClient

Type annotations for  `boto3.client("synthetics")` as [SyntheticsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_synthetics.client import SyntheticsClient
```


SyntheticsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_canary](./client.md#create-canary)
- [delete_canary](./client.md#delete-canary)
- [describe_canaries](./client.md#describe-canaries)
- [describe_canaries_last_run](./client.md#describe-canaries-last-run)
- [describe_runtime_versions](./client.md#describe-runtime-versions)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_canary](./client.md#get-canary)
- [get_canary_runs](./client.md#get-canary-runs)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_canary](./client.md#start-canary)
- [stop_canary](./client.md#stop-canary)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_canary](./client.md#update-canary)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_synthetics.literals import CanaryRunState, ...
```

- [CanaryRunState](./literals.md#canaryrunstate)
- [CanaryRunStateReasonCode](./literals.md#canaryrunstatereasoncode)
- [CanaryState](./literals.md#canarystate)
- [CanaryStateReasonCode](./literals.md#canarystatereasoncode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_synthetics.type_defs import CanaryCodeInputTypeDef, ...
```

- [CanaryCodeInputTypeDef](./type_defs.md#canarycodeinputtypedef)
- [CanaryCodeOutputTypeDef](./type_defs.md#canarycodeoutputtypedef)
- [CanaryLastRunTypeDef](./type_defs.md#canarylastruntypedef)
- [CanaryRunConfigInputTypeDef](./type_defs.md#canaryrunconfiginputtypedef)
- [CanaryRunConfigOutputTypeDef](./type_defs.md#canaryrunconfigoutputtypedef)
- [CanaryRunStatusTypeDef](./type_defs.md#canaryrunstatustypedef)
- [CanaryRunTimelineTypeDef](./type_defs.md#canaryruntimelinetypedef)
- [CanaryRunTypeDef](./type_defs.md#canaryruntypedef)
- [CanaryScheduleInputTypeDef](./type_defs.md#canaryscheduleinputtypedef)
- [CanaryScheduleOutputTypeDef](./type_defs.md#canaryscheduleoutputtypedef)
- [CanaryStatusTypeDef](./type_defs.md#canarystatustypedef)
- [CanaryTimelineTypeDef](./type_defs.md#canarytimelinetypedef)
- [CanaryTypeDef](./type_defs.md#canarytypedef)
- [CreateCanaryResponseTypeDef](./type_defs.md#createcanaryresponsetypedef)
- [DescribeCanariesLastRunResponseTypeDef](./type_defs.md#describecanarieslastrunresponsetypedef)
- [DescribeCanariesResponseTypeDef](./type_defs.md#describecanariesresponsetypedef)
- [DescribeRuntimeVersionsResponseTypeDef](./type_defs.md#describeruntimeversionsresponsetypedef)
- [GetCanaryResponseTypeDef](./type_defs.md#getcanaryresponsetypedef)
- [GetCanaryRunsResponseTypeDef](./type_defs.md#getcanaryrunsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RuntimeVersionTypeDef](./type_defs.md#runtimeversiontypedef)
- [VpcConfigInputTypeDef](./type_defs.md#vpcconfiginputtypedef)
- [VpcConfigOutputTypeDef](./type_defs.md#vpcconfigoutputtypedef)
