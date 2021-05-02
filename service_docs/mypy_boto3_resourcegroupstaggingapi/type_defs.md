# Structures for boto3 ResourceGroupsTaggingAPI module

> [Index](../index.md) > [ResourceGroupsTaggingAPI](./index.md) > Structures

Auto-generated documentation for [ResourceGroupsTaggingAPI](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html#ResourceGroupsTaggingAPI)
type annotations stubs module [mypy_boto3_resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/).

- [Structures for boto3 ResourceGroupsTaggingAPI module](#structures-for-boto3-resourcegroupstaggingapi-module)
  - [ComplianceDetailsTypeDef](#compliancedetailstypedef)
  - [DescribeReportCreationOutputTypeDef](#describereportcreationoutputtypedef)
  - [FailureInfoTypeDef](#failureinfotypedef)
  - [GetComplianceSummaryOutputTypeDef](#getcompliancesummaryoutputtypedef)
  - [GetResourcesOutputTypeDef](#getresourcesoutputtypedef)
  - [GetTagKeysOutputTypeDef](#gettagkeysoutputtypedef)
  - [GetTagValuesOutputTypeDef](#gettagvaluesoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResourceTagMappingTypeDef](#resourcetagmappingtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SummaryTypeDef](#summarytypedef)
  - [TagFilterTypeDef](#tagfiltertypedef)
  - [TagResourcesOutputTypeDef](#tagresourcesoutputtypedef)
  - [TagTypeDef](#tagtypedef)
  - [UntagResourcesOutputTypeDef](#untagresourcesoutputtypedef)

## ComplianceDetailsTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef
```




Optional fields:
- `NoncompliantKeys`: `List[str]`
- `KeysWithNoncompliantValues`: `List[str]`
- `ComplianceStatus`: `bool`


## DescribeReportCreationOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import DescribeReportCreationOutputTypeDef
```




Optional fields:
- `Status`: `str`
- `S3Location`: `str`
- `ErrorMessage`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## FailureInfoTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import FailureInfoTypeDef
```




Optional fields:
- `StatusCode`: `int`
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## GetComplianceSummaryOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import GetComplianceSummaryOutputTypeDef
```




Optional fields:
- `SummaryList`: `List["SummaryTypeDef"]`
- `PaginationToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetResourcesOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import GetResourcesOutputTypeDef
```




Optional fields:
- `PaginationToken`: `str`
- `ResourceTagMappingList`: `List["ResourceTagMappingTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTagKeysOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import GetTagKeysOutputTypeDef
```




Optional fields:
- `PaginationToken`: `str`
- `TagKeys`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetTagValuesOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import GetTagValuesOutputTypeDef
```




Optional fields:
- `PaginationToken`: `str`
- `TagValues`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResourceTagMappingTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import ResourceTagMappingTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `Tags`: `List["TagTypeDef"]`
- `ComplianceDetails`: `"ComplianceDetailsTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SummaryTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import SummaryTypeDef
```




Optional fields:
- `LastUpdated`: `str`
- `TargetId`: `str`
- `TargetIdType`: `TargetIdType`
- `Region`: `str`
- `ResourceType`: `str`
- `NonCompliantResources`: `int`


## TagFilterTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import TagFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## TagResourcesOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import TagResourcesOutputTypeDef
```




Optional fields:
- `FailedResourcesMap`: `Dict[str, "FailureInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## TagTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UntagResourcesOutputTypeDef

```python
from mypy_boto3_resourcegroupstaggingapi.type_defs import UntagResourcesOutputTypeDef
```




Optional fields:
- `FailedResourcesMap`: `Dict[str, "FailureInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`

