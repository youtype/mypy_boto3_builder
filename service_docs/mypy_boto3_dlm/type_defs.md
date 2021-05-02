# Structures for boto3 DLM module

> [Index](../index.md) > [DLM](./index.md) > Structures

Auto-generated documentation for [DLM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM)
type annotations stubs module [mypy_boto3_dlm](https://pypi.org/project/mypy-boto3-dlm/).

- [Structures for boto3 DLM module](#structures-for-boto3-dlm-module)
  - [ActionTypeDef](#actiontypedef)
  - [CreateLifecyclePolicyResponseTypeDef](#createlifecyclepolicyresponsetypedef)
  - [CreateRuleTypeDef](#createruletypedef)
  - [CrossRegionCopyActionTypeDef](#crossregioncopyactiontypedef)
  - [CrossRegionCopyRetainRuleTypeDef](#crossregioncopyretainruletypedef)
  - [CrossRegionCopyRuleTypeDef](#crossregioncopyruletypedef)
  - [EncryptionConfigurationTypeDef](#encryptionconfigurationtypedef)
  - [EventParametersTypeDef](#eventparameterstypedef)
  - [EventSourceTypeDef](#eventsourcetypedef)
  - [FastRestoreRuleTypeDef](#fastrestoreruletypedef)
  - [GetLifecyclePoliciesResponseTypeDef](#getlifecyclepoliciesresponsetypedef)
  - [GetLifecyclePolicyResponseTypeDef](#getlifecyclepolicyresponsetypedef)
  - [LifecyclePolicySummaryTypeDef](#lifecyclepolicysummarytypedef)
  - [LifecyclePolicyTypeDef](#lifecyclepolicytypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ParametersTypeDef](#parameterstypedef)
  - [PolicyDetailsTypeDef](#policydetailstypedef)
  - [RetainRuleTypeDef](#retainruletypedef)
  - [ScheduleTypeDef](#scheduletypedef)
  - [ShareRuleTypeDef](#shareruletypedef)
  - [TagTypeDef](#tagtypedef)

## ActionTypeDef

```python
from mypy_boto3_dlm.type_defs import ActionTypeDef
```


Required fields:
- `Name`: `str`
- `CrossRegionCopy`: `List["CrossRegionCopyActionTypeDef"]`




## CreateLifecyclePolicyResponseTypeDef

```python
from mypy_boto3_dlm.type_defs import CreateLifecyclePolicyResponseTypeDef
```




Optional fields:
- `PolicyId`: `str`


## CreateRuleTypeDef

```python
from mypy_boto3_dlm.type_defs import CreateRuleTypeDef
```




Optional fields:
- `Location`: `LocationValues`
- `Interval`: `int`
- `IntervalUnit`: `Literal['HOURS']`
- `Times`: `List[str]`
- `CronExpression`: `str`


## CrossRegionCopyActionTypeDef

```python
from mypy_boto3_dlm.type_defs import CrossRegionCopyActionTypeDef
```


Required fields:
- `Target`: `str`
- `EncryptionConfiguration`: `"EncryptionConfigurationTypeDef"`



Optional fields:
- `RetainRule`: `"CrossRegionCopyRetainRuleTypeDef"`


## CrossRegionCopyRetainRuleTypeDef

```python
from mypy_boto3_dlm.type_defs import CrossRegionCopyRetainRuleTypeDef
```




Optional fields:
- `Interval`: `int`
- `IntervalUnit`: `RetentionIntervalUnitValues`


## CrossRegionCopyRuleTypeDef

```python
from mypy_boto3_dlm.type_defs import CrossRegionCopyRuleTypeDef
```


Required fields:
- `Encrypted`: `bool`



Optional fields:
- `TargetRegion`: `str`
- `Target`: `str`
- `CmkArn`: `str`
- `CopyTags`: `bool`
- `RetainRule`: `"CrossRegionCopyRetainRuleTypeDef"`


## EncryptionConfigurationTypeDef

```python
from mypy_boto3_dlm.type_defs import EncryptionConfigurationTypeDef
```


Required fields:
- `Encrypted`: `bool`



Optional fields:
- `CmkArn`: `str`


## EventParametersTypeDef

```python
from mypy_boto3_dlm.type_defs import EventParametersTypeDef
```


Required fields:
- `EventType`: `Literal['shareSnapshot']`
- `SnapshotOwner`: `List[str]`
- `DescriptionRegex`: `str`




## EventSourceTypeDef

```python
from mypy_boto3_dlm.type_defs import EventSourceTypeDef
```


Required fields:
- `Type`: `Literal['MANAGED_CWE']`



Optional fields:
- `Parameters`: `"EventParametersTypeDef"`


## FastRestoreRuleTypeDef

```python
from mypy_boto3_dlm.type_defs import FastRestoreRuleTypeDef
```


Required fields:
- `AvailabilityZones`: `List[str]`



Optional fields:
- `Count`: `int`
- `Interval`: `int`
- `IntervalUnit`: `RetentionIntervalUnitValues`


## GetLifecyclePoliciesResponseTypeDef

```python
from mypy_boto3_dlm.type_defs import GetLifecyclePoliciesResponseTypeDef
```




Optional fields:
- `Policies`: `List["LifecyclePolicySummaryTypeDef"]`


## GetLifecyclePolicyResponseTypeDef

```python
from mypy_boto3_dlm.type_defs import GetLifecyclePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"LifecyclePolicyTypeDef"`


## LifecyclePolicySummaryTypeDef

```python
from mypy_boto3_dlm.type_defs import LifecyclePolicySummaryTypeDef
```




Optional fields:
- `PolicyId`: `str`
- `Description`: `str`
- `State`: `GettablePolicyStateValues`
- `Tags`: `Dict[str, str]`
- `PolicyType`: `PolicyTypeValues`


## LifecyclePolicyTypeDef

```python
from mypy_boto3_dlm.type_defs import LifecyclePolicyTypeDef
```




Optional fields:
- `PolicyId`: `str`
- `Description`: `str`
- `State`: `GettablePolicyStateValues`
- `StatusMessage`: `str`
- `ExecutionRoleArn`: `str`
- `DateCreated`: `datetime`
- `DateModified`: `datetime`
- `PolicyDetails`: `"PolicyDetailsTypeDef"`
- `Tags`: `Dict[str, str]`
- `PolicyArn`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_dlm.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ParametersTypeDef

```python
from mypy_boto3_dlm.type_defs import ParametersTypeDef
```




Optional fields:
- `ExcludeBootVolume`: `bool`
- `NoReboot`: `bool`


## PolicyDetailsTypeDef

```python
from mypy_boto3_dlm.type_defs import PolicyDetailsTypeDef
```




Optional fields:
- `PolicyType`: `PolicyTypeValues`
- `ResourceTypes`: `List[ResourceTypeValues]`
- `ResourceLocations`: `List[ResourceLocationValues]`
- `TargetTags`: `List["TagTypeDef"]`
- `Schedules`: `List["ScheduleTypeDef"]`
- `Parameters`: `"ParametersTypeDef"`
- `EventSource`: `"EventSourceTypeDef"`
- `Actions`: `List["ActionTypeDef"]`


## RetainRuleTypeDef

```python
from mypy_boto3_dlm.type_defs import RetainRuleTypeDef
```




Optional fields:
- `Count`: `int`
- `Interval`: `int`
- `IntervalUnit`: `RetentionIntervalUnitValues`


## ScheduleTypeDef

```python
from mypy_boto3_dlm.type_defs import ScheduleTypeDef
```




Optional fields:
- `Name`: `str`
- `CopyTags`: `bool`
- `TagsToAdd`: `List["TagTypeDef"]`
- `VariableTags`: `List["TagTypeDef"]`
- `CreateRule`: `"CreateRuleTypeDef"`
- `RetainRule`: `"RetainRuleTypeDef"`
- `FastRestoreRule`: `"FastRestoreRuleTypeDef"`
- `CrossRegionCopyRules`: `List["CrossRegionCopyRuleTypeDef"]`
- `ShareRules`: `List["ShareRuleTypeDef"]`


## ShareRuleTypeDef

```python
from mypy_boto3_dlm.type_defs import ShareRuleTypeDef
```


Required fields:
- `TargetAccounts`: `List[str]`



Optional fields:
- `UnshareInterval`: `int`
- `UnshareIntervalUnit`: `RetentionIntervalUnitValues`


## TagTypeDef

```python
from mypy_boto3_dlm.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`



