# Structures for boto3 ResourceGroups module

> [Index](../index.md) > [ResourceGroups](./index.md) > Structures

Auto-generated documentation for [ResourceGroups](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups)
type annotations stubs module [mypy_boto3_resource_groups](https://pypi.org/project/mypy-boto3-resource-groups/).

- [Structures for boto3 ResourceGroups module](#structures-for-boto3-resourcegroups-module)
  - [FailedResourceTypeDef](#failedresourcetypedef)
  - [GroupConfigurationItemTypeDef](#groupconfigurationitemtypedef)
  - [GroupConfigurationParameterTypeDef](#groupconfigurationparametertypedef)
  - [GroupConfigurationTypeDef](#groupconfigurationtypedef)
  - [GroupIdentifierTypeDef](#groupidentifiertypedef)
  - [GroupQueryTypeDef](#groupquerytypedef)
  - [GroupTypeDef](#grouptypedef)
  - [ListGroupResourcesItemTypeDef](#listgroupresourcesitemtypedef)
  - [PendingResourceTypeDef](#pendingresourcetypedef)
  - [QueryErrorTypeDef](#queryerrortypedef)
  - [ResourceIdentifierTypeDef](#resourceidentifiertypedef)
  - [ResourceQueryTypeDef](#resourcequerytypedef)
  - [ResourceStatusTypeDef](#resourcestatustypedef)
  - [ResponseMetadata](#responsemetadata)
  - [CreateGroupOutputTypeDef](#creategroupoutputtypedef)
  - [DeleteGroupOutputTypeDef](#deletegroupoutputtypedef)
  - [GetGroupConfigurationOutputTypeDef](#getgroupconfigurationoutputtypedef)
  - [GetGroupOutputTypeDef](#getgroupoutputtypedef)
  - [GetGroupQueryOutputTypeDef](#getgroupqueryoutputtypedef)
  - [GetTagsOutputTypeDef](#gettagsoutputtypedef)
  - [GroupFilterTypeDef](#groupfiltertypedef)
  - [GroupResourcesOutputTypeDef](#groupresourcesoutputtypedef)
  - [ListGroupResourcesOutputTypeDef](#listgroupresourcesoutputtypedef)
  - [ListGroupsOutputTypeDef](#listgroupsoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResourceFilterTypeDef](#resourcefiltertypedef)
  - [SearchResourcesOutputTypeDef](#searchresourcesoutputtypedef)
  - [TagOutputTypeDef](#tagoutputtypedef)
  - [UngroupResourcesOutputTypeDef](#ungroupresourcesoutputtypedef)
  - [UntagOutputTypeDef](#untagoutputtypedef)
  - [UpdateGroupOutputTypeDef](#updategroupoutputtypedef)
  - [UpdateGroupQueryOutputTypeDef](#updategroupqueryoutputtypedef)

## FailedResourceTypeDef

```python
from mypy_boto3_resource_groups.type_defs import FailedResourceTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ErrorMessage`: `str`
- `ErrorCode`: `str`


## GroupConfigurationItemTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupConfigurationItemTypeDef
```


Required fields:
- `Type`: `str`



Optional fields:
- `Parameters`: `List["GroupConfigurationParameterTypeDef"]`


## GroupConfigurationParameterTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupConfigurationParameterTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Values`: `List[str]`


## GroupConfigurationTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupConfigurationTypeDef
```




Optional fields:
- `Configuration`: `List["GroupConfigurationItemTypeDef"]`
- `ProposedConfiguration`: `List["GroupConfigurationItemTypeDef"]`
- `Status`: `GroupConfigurationStatus`
- `FailureReason`: `str`


## GroupIdentifierTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupIdentifierTypeDef
```




Optional fields:
- `GroupName`: `str`
- `GroupArn`: `str`


## GroupQueryTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupQueryTypeDef
```


Required fields:
- `GroupName`: `str`
- `ResourceQuery`: `"ResourceQueryTypeDef"`




## GroupTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupTypeDef
```


Required fields:
- `GroupArn`: `str`
- `Name`: `str`



Optional fields:
- `Description`: `str`


## ListGroupResourcesItemTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ListGroupResourcesItemTypeDef
```




Optional fields:
- `Identifier`: `"ResourceIdentifierTypeDef"`
- `Status`: `"ResourceStatusTypeDef"`


## PendingResourceTypeDef

```python
from mypy_boto3_resource_groups.type_defs import PendingResourceTypeDef
```




Optional fields:
- `ResourceArn`: `str`


## QueryErrorTypeDef

```python
from mypy_boto3_resource_groups.type_defs import QueryErrorTypeDef
```




Optional fields:
- `ErrorCode`: `QueryErrorCode`
- `Message`: `str`


## ResourceIdentifierTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ResourceIdentifierTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `ResourceType`: `str`


## ResourceQueryTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ResourceQueryTypeDef
```


Required fields:
- `Type`: `QueryType`
- `Query`: `str`




## ResourceStatusTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ResourceStatusTypeDef
```




Optional fields:
- `Name`: `ResourceStatusValue`


## ResponseMetadata

```python
from mypy_boto3_resource_groups.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## CreateGroupOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import CreateGroupOutputTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `ResourceQuery`: `"ResourceQueryTypeDef"`
- `Tags`: `Dict[str, str]`
- `GroupConfiguration`: `"GroupConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteGroupOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import DeleteGroupOutputTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetGroupConfigurationOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GetGroupConfigurationOutputTypeDef
```




Optional fields:
- `GroupConfiguration`: `"GroupConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetGroupOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GetGroupOutputTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetGroupQueryOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GetGroupQueryOutputTypeDef
```




Optional fields:
- `GroupQuery`: `"GroupQueryTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTagsOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GetTagsOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GroupFilterTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupFilterTypeDef
```


Required fields:
- `Name`: `GroupFilterName`
- `Values`: `List[str]`




## GroupResourcesOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import GroupResourcesOutputTypeDef
```




Optional fields:
- `Succeeded`: `List[str]`
- `Failed`: `List["FailedResourceTypeDef"]`
- `Pending`: `List["PendingResourceTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGroupResourcesOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ListGroupResourcesOutputTypeDef
```




Optional fields:
- `Resources`: `List["ListGroupResourcesItemTypeDef"]`
- `ResourceIdentifiers`: `List["ResourceIdentifierTypeDef"]`
- `NextToken`: `str`
- `QueryErrors`: `List["QueryErrorTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListGroupsOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ListGroupsOutputTypeDef
```




Optional fields:
- `GroupIdentifiers`: `List["GroupIdentifierTypeDef"]`
- `Groups`: `List["GroupTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_resource_groups.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResourceFilterTypeDef

```python
from mypy_boto3_resource_groups.type_defs import ResourceFilterTypeDef
```


Required fields:
- `Name`: `ResourceFilterName`
- `Values`: `List[str]`




## SearchResourcesOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import SearchResourcesOutputTypeDef
```




Optional fields:
- `ResourceIdentifiers`: `List["ResourceIdentifierTypeDef"]`
- `NextToken`: `str`
- `QueryErrors`: `List["QueryErrorTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## TagOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import TagOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UngroupResourcesOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import UngroupResourcesOutputTypeDef
```




Optional fields:
- `Succeeded`: `List[str]`
- `Failed`: `List["FailedResourceTypeDef"]`
- `Pending`: `List["PendingResourceTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UntagOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import UntagOutputTypeDef
```




Optional fields:
- `Arn`: `str`
- `Keys`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGroupOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import UpdateGroupOutputTypeDef
```




Optional fields:
- `Group`: `"GroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateGroupQueryOutputTypeDef

```python
from mypy_boto3_resource_groups.type_defs import UpdateGroupQueryOutputTypeDef
```




Optional fields:
- `GroupQuery`: `"GroupQueryTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`

