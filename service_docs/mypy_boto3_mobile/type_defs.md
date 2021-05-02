# Structures for boto3 Mobile module

> [Index](../index.md) > [Mobile](./index.md) > Structures

Auto-generated documentation for [Mobile](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile)
type annotations stubs module [mypy_boto3_mobile](https://pypi.org/project/mypy-boto3-mobile/).

- [Structures for boto3 Mobile module](#structures-for-boto3-mobile-module)
  - [BundleDetailsTypeDef](#bundledetailstypedef)
  - [CreateProjectResultTypeDef](#createprojectresulttypedef)
  - [DeleteProjectResultTypeDef](#deleteprojectresulttypedef)
  - [DescribeBundleResultTypeDef](#describebundleresulttypedef)
  - [DescribeProjectResultTypeDef](#describeprojectresulttypedef)
  - [ExportBundleResultTypeDef](#exportbundleresulttypedef)
  - [ExportProjectResultTypeDef](#exportprojectresulttypedef)
  - [ListBundlesResultTypeDef](#listbundlesresulttypedef)
  - [ListProjectsResultTypeDef](#listprojectsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProjectDetailsTypeDef](#projectdetailstypedef)
  - [ProjectSummaryTypeDef](#projectsummarytypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [UpdateProjectResultTypeDef](#updateprojectresulttypedef)

## BundleDetailsTypeDef

```python
from mypy_boto3_mobile.type_defs import BundleDetailsTypeDef
```




Optional fields:
- `bundleId`: `str`
- `title`: `str`
- `version`: `str`
- `description`: `str`
- `iconUrl`: `str`
- `availablePlatforms`: `List[Platform]`


## CreateProjectResultTypeDef

```python
from mypy_boto3_mobile.type_defs import CreateProjectResultTypeDef
```




Optional fields:
- `details`: `"ProjectDetailsTypeDef"`


## DeleteProjectResultTypeDef

```python
from mypy_boto3_mobile.type_defs import DeleteProjectResultTypeDef
```




Optional fields:
- `deletedResources`: `List["ResourceTypeDef"]`
- `orphanedResources`: `List["ResourceTypeDef"]`


## DescribeBundleResultTypeDef

```python
from mypy_boto3_mobile.type_defs import DescribeBundleResultTypeDef
```




Optional fields:
- `details`: `"BundleDetailsTypeDef"`


## DescribeProjectResultTypeDef

```python
from mypy_boto3_mobile.type_defs import DescribeProjectResultTypeDef
```




Optional fields:
- `details`: `"ProjectDetailsTypeDef"`


## ExportBundleResultTypeDef

```python
from mypy_boto3_mobile.type_defs import ExportBundleResultTypeDef
```




Optional fields:
- `downloadUrl`: `str`


## ExportProjectResultTypeDef

```python
from mypy_boto3_mobile.type_defs import ExportProjectResultTypeDef
```




Optional fields:
- `downloadUrl`: `str`
- `shareUrl`: `str`
- `snapshotId`: `str`


## ListBundlesResultTypeDef

```python
from mypy_boto3_mobile.type_defs import ListBundlesResultTypeDef
```




Optional fields:
- `bundleList`: `List["BundleDetailsTypeDef"]`
- `nextToken`: `str`


## ListProjectsResultTypeDef

```python
from mypy_boto3_mobile.type_defs import ListProjectsResultTypeDef
```




Optional fields:
- `projects`: `List["ProjectSummaryTypeDef"]`
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mobile.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProjectDetailsTypeDef

```python
from mypy_boto3_mobile.type_defs import ProjectDetailsTypeDef
```




Optional fields:
- `name`: `str`
- `projectId`: `str`
- `region`: `str`
- `state`: `ProjectState`
- `createdDate`: `datetime`
- `lastUpdatedDate`: `datetime`
- `consoleUrl`: `str`
- `resources`: `List["ResourceTypeDef"]`


## ProjectSummaryTypeDef

```python
from mypy_boto3_mobile.type_defs import ProjectSummaryTypeDef
```




Optional fields:
- `name`: `str`
- `projectId`: `str`


## ResourceTypeDef

```python
from mypy_boto3_mobile.type_defs import ResourceTypeDef
```




Optional fields:
- `type`: `str`
- `name`: `str`
- `arn`: `str`
- `feature`: `str`
- `attributes`: `Dict[str, str]`


## UpdateProjectResultTypeDef

```python
from mypy_boto3_mobile.type_defs import UpdateProjectResultTypeDef
```




Optional fields:
- `details`: `"ProjectDetailsTypeDef"`

