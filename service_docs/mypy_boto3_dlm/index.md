# Type annotations for boto3 DLM module

> [Index](../index.md) > DLM

Auto-generated documentation for [DLM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM)
type annotations stubs module [mypy_boto3_dlm](https://pypi.org/project/mypy-boto3-dlm/).

```bash
pip install mypy-boto3-dlm
```

- [Type annotations for boto3 DLM module](#type-annotations-for-boto3-dlm-module)
  - [DLMClient](#dlmclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## DLMClient

Type annotations for  `boto3.client("dlm")` as [DLMClient](./client.md)

Can be used directly:

```python
from mypy_boto3_dlm.client import DLMClient
```


DLMClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_lifecycle_policy](./client.md#create-lifecycle-policy)
- [delete_lifecycle_policy](./client.md#delete-lifecycle-policy)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_lifecycle_policies](./client.md#get-lifecycle-policies)
- [get_lifecycle_policy](./client.md#get-lifecycle-policy)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_lifecycle_policy](./client.md#update-lifecycle-policy)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dlm.literals import EventSourceValues, ...
```

- [EventSourceValues](./literals.md#eventsourcevalues)
- [EventTypeValues](./literals.md#eventtypevalues)
- [GettablePolicyStateValues](./literals.md#gettablepolicystatevalues)
- [IntervalUnitValues](./literals.md#intervalunitvalues)
- [LocationValues](./literals.md#locationvalues)
- [PolicyTypeValues](./literals.md#policytypevalues)
- [ResourceLocationValues](./literals.md#resourcelocationvalues)
- [ResourceTypeValues](./literals.md#resourcetypevalues)
- [RetentionIntervalUnitValues](./literals.md#retentionintervalunitvalues)
- [SettablePolicyStateValues](./literals.md#settablepolicystatevalues)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dlm.type_defs import ActionTypeDef, ...
```

- [ActionTypeDef](./type_defs.md#actiontypedef)
- [CreateLifecyclePolicyResponseTypeDef](./type_defs.md#createlifecyclepolicyresponsetypedef)
- [CreateRuleTypeDef](./type_defs.md#createruletypedef)
- [CrossRegionCopyActionTypeDef](./type_defs.md#crossregioncopyactiontypedef)
- [CrossRegionCopyRetainRuleTypeDef](./type_defs.md#crossregioncopyretainruletypedef)
- [CrossRegionCopyRuleTypeDef](./type_defs.md#crossregioncopyruletypedef)
- [EncryptionConfigurationTypeDef](./type_defs.md#encryptionconfigurationtypedef)
- [EventParametersTypeDef](./type_defs.md#eventparameterstypedef)
- [EventSourceTypeDef](./type_defs.md#eventsourcetypedef)
- [FastRestoreRuleTypeDef](./type_defs.md#fastrestoreruletypedef)
- [GetLifecyclePoliciesResponseTypeDef](./type_defs.md#getlifecyclepoliciesresponsetypedef)
- [GetLifecyclePolicyResponseTypeDef](./type_defs.md#getlifecyclepolicyresponsetypedef)
- [LifecyclePolicySummaryTypeDef](./type_defs.md#lifecyclepolicysummarytypedef)
- [LifecyclePolicyTypeDef](./type_defs.md#lifecyclepolicytypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ParametersTypeDef](./type_defs.md#parameterstypedef)
- [PolicyDetailsTypeDef](./type_defs.md#policydetailstypedef)
- [RetainRuleTypeDef](./type_defs.md#retainruletypedef)
- [ScheduleTypeDef](./type_defs.md#scheduletypedef)
- [ShareRuleTypeDef](./type_defs.md#shareruletypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
