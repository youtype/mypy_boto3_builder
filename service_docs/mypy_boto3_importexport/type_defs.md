# Structures for boto3 ImportExport module

> [Index](../index.md) > [ImportExport](./index.md) > Structures

Auto-generated documentation for [ImportExport](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport)
type annotations stubs module [mypy_boto3_importexport](https://pypi.org/project/mypy-boto3-importexport/).

- [Structures for boto3 ImportExport module](#structures-for-boto3-importexport-module)
  - [ArtifactTypeDef](#artifacttypedef)
  - [CancelJobOutputTypeDef](#canceljoboutputtypedef)
  - [CreateJobOutputTypeDef](#createjoboutputtypedef)
  - [GetShippingLabelOutputTypeDef](#getshippinglabeloutputtypedef)
  - [GetStatusOutputTypeDef](#getstatusoutputtypedef)
  - [JobTypeDef](#jobtypedef)
  - [ListJobsOutputTypeDef](#listjobsoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [UpdateJobOutputTypeDef](#updatejoboutputtypedef)

## ArtifactTypeDef

```python
from mypy_boto3_importexport.type_defs import ArtifactTypeDef
```




Optional fields:
- `Description`: `str`
- `URL`: `str`


## CancelJobOutputTypeDef

```python
from mypy_boto3_importexport.type_defs import CancelJobOutputTypeDef
```




Optional fields:
- `Success`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateJobOutputTypeDef

```python
from mypy_boto3_importexport.type_defs import CreateJobOutputTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobType`: `JobType`
- `Signature`: `str`
- `SignatureFileContents`: `str`
- `WarningMessage`: `str`
- `ArtifactList`: `List["ArtifactTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetShippingLabelOutputTypeDef

```python
from mypy_boto3_importexport.type_defs import GetShippingLabelOutputTypeDef
```




Optional fields:
- `ShippingLabelURL`: `str`
- `Warning`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetStatusOutputTypeDef

```python
from mypy_boto3_importexport.type_defs import GetStatusOutputTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobType`: `JobType`
- `LocationCode`: `str`
- `LocationMessage`: `str`
- `ProgressCode`: `str`
- `ProgressMessage`: `str`
- `Carrier`: `str`
- `TrackingNumber`: `str`
- `LogBucket`: `str`
- `LogKey`: `str`
- `ErrorCount`: `int`
- `Signature`: `str`
- `SignatureFileContents`: `str`
- `CurrentManifest`: `str`
- `CreationDate`: `datetime`
- `ArtifactList`: `List["ArtifactTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## JobTypeDef

```python
from mypy_boto3_importexport.type_defs import JobTypeDef
```




Optional fields:
- `JobId`: `str`
- `CreationDate`: `datetime`
- `IsCanceled`: `bool`
- `JobType`: `JobType`


## ListJobsOutputTypeDef

```python
from mypy_boto3_importexport.type_defs import ListJobsOutputTypeDef
```




Optional fields:
- `Jobs`: `List["JobTypeDef"]`
- `IsTruncated`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_importexport.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResponseMetadata

```python
from mypy_boto3_importexport.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## UpdateJobOutputTypeDef

```python
from mypy_boto3_importexport.type_defs import UpdateJobOutputTypeDef
```




Optional fields:
- `Success`: `bool`
- `WarningMessage`: `str`
- `ArtifactList`: `List["ArtifactTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`

