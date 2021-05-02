# Structures for boto3 Outposts module

> [Index](../index.md) > [Outposts](./index.md) > Structures

Auto-generated documentation for [Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts)
type annotations stubs module [mypy_boto3_outposts](https://pypi.org/project/mypy-boto3-outposts/).

- [Structures for boto3 Outposts module](#structures-for-boto3-outposts-module)
  - [InstanceTypeItemTypeDef](#instancetypeitemtypedef)
  - [OutpostTypeDef](#outposttypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SiteTypeDef](#sitetypedef)
  - [CreateOutpostOutputTypeDef](#createoutpostoutputtypedef)
  - [GetOutpostInstanceTypesOutputTypeDef](#getoutpostinstancetypesoutputtypedef)
  - [GetOutpostOutputTypeDef](#getoutpostoutputtypedef)
  - [ListOutpostsOutputTypeDef](#listoutpostsoutputtypedef)
  - [ListSitesOutputTypeDef](#listsitesoutputtypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)

## InstanceTypeItemTypeDef

```python
from mypy_boto3_outposts.type_defs import InstanceTypeItemTypeDef
```




Optional fields:
- `InstanceType`: `str`


## OutpostTypeDef

```python
from mypy_boto3_outposts.type_defs import OutpostTypeDef
```




Optional fields:
- `OutpostId`: `str`
- `OwnerId`: `str`
- `OutpostArn`: `str`
- `SiteId`: `str`
- `Name`: `str`
- `Description`: `str`
- `LifeCycleStatus`: `str`
- `AvailabilityZone`: `str`
- `AvailabilityZoneId`: `str`
- `Tags`: `Dict[str, str]`


## ResponseMetadata

```python
from mypy_boto3_outposts.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SiteTypeDef

```python
from mypy_boto3_outposts.type_defs import SiteTypeDef
```




Optional fields:
- `SiteId`: `str`
- `AccountId`: `str`
- `Name`: `str`
- `Description`: `str`
- `Tags`: `Dict[str, str]`


## CreateOutpostOutputTypeDef

```python
from mypy_boto3_outposts.type_defs import CreateOutpostOutputTypeDef
```




Optional fields:
- `Outpost`: `"OutpostTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetOutpostInstanceTypesOutputTypeDef

```python
from mypy_boto3_outposts.type_defs import GetOutpostInstanceTypesOutputTypeDef
```




Optional fields:
- `InstanceTypes`: `List["InstanceTypeItemTypeDef"]`
- `NextToken`: `str`
- `OutpostId`: `str`
- `OutpostArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetOutpostOutputTypeDef

```python
from mypy_boto3_outposts.type_defs import GetOutpostOutputTypeDef
```




Optional fields:
- `Outpost`: `"OutpostTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListOutpostsOutputTypeDef

```python
from mypy_boto3_outposts.type_defs import ListOutpostsOutputTypeDef
```




Optional fields:
- `Outposts`: `List["OutpostTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSitesOutputTypeDef

```python
from mypy_boto3_outposts.type_defs import ListSitesOutputTypeDef
```




Optional fields:
- `Sites`: `List["SiteTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_outposts.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`

