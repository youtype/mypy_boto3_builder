# Structures for boto3 IoT1ClickProjects module

> [Index](../index.md) > [IoT1ClickProjects](./index.md) > Structures

Auto-generated documentation for [IoT1ClickProjects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects)
type annotations stubs module [mypy_boto3_iot1click_projects](https://pypi.org/project/mypy-boto3-iot1click-projects/).

- [Structures for boto3 IoT1ClickProjects module](#structures-for-boto3-iot1clickprojects-module)
  - [DescribePlacementResponseTypeDef](#describeplacementresponsetypedef)
  - [DescribeProjectResponseTypeDef](#describeprojectresponsetypedef)
  - [DeviceTemplateTypeDef](#devicetemplatetypedef)
  - [GetDevicesInPlacementResponseTypeDef](#getdevicesinplacementresponsetypedef)
  - [ListPlacementsResponseTypeDef](#listplacementsresponsetypedef)
  - [ListProjectsResponseTypeDef](#listprojectsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PlacementDescriptionTypeDef](#placementdescriptiontypedef)
  - [PlacementSummaryTypeDef](#placementsummarytypedef)
  - [PlacementTemplateTypeDef](#placementtemplatetypedef)
  - [ProjectDescriptionTypeDef](#projectdescriptiontypedef)
  - [ProjectSummaryTypeDef](#projectsummarytypedef)

## DescribePlacementResponseTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import DescribePlacementResponseTypeDef
```


Required fields:
- `placement`: `"PlacementDescriptionTypeDef"`




## DescribeProjectResponseTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import DescribeProjectResponseTypeDef
```


Required fields:
- `project`: `"ProjectDescriptionTypeDef"`




## DeviceTemplateTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import DeviceTemplateTypeDef
```




Optional fields:
- `deviceType`: `str`
- `callbackOverrides`: `Dict[str, str]`


## GetDevicesInPlacementResponseTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import GetDevicesInPlacementResponseTypeDef
```


Required fields:
- `devices`: `Dict[str, str]`




## ListPlacementsResponseTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import ListPlacementsResponseTypeDef
```


Required fields:
- `placements`: `List["PlacementSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListProjectsResponseTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import ListProjectsResponseTypeDef
```


Required fields:
- `projects`: `List["ProjectSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PlacementDescriptionTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import PlacementDescriptionTypeDef
```


Required fields:
- `projectName`: `str`
- `placementName`: `str`
- `attributes`: `Dict[str, str]`
- `createdDate`: `datetime`
- `updatedDate`: `datetime`




## PlacementSummaryTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import PlacementSummaryTypeDef
```


Required fields:
- `projectName`: `str`
- `placementName`: `str`
- `createdDate`: `datetime`
- `updatedDate`: `datetime`




## PlacementTemplateTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import PlacementTemplateTypeDef
```




Optional fields:
- `defaultAttributes`: `Dict[str, str]`
- `deviceTemplates`: `Dict[str, "DeviceTemplateTypeDef"]`


## ProjectDescriptionTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import ProjectDescriptionTypeDef
```


Required fields:
- `projectName`: `str`
- `createdDate`: `datetime`
- `updatedDate`: `datetime`



Optional fields:
- `arn`: `str`
- `description`: `str`
- `placementTemplate`: `"PlacementTemplateTypeDef"`
- `tags`: `Dict[str, str]`


## ProjectSummaryTypeDef

```python
from mypy_boto3_iot1click_projects.type_defs import ProjectSummaryTypeDef
```


Required fields:
- `projectName`: `str`
- `createdDate`: `datetime`
- `updatedDate`: `datetime`



Optional fields:
- `arn`: `str`
- `tags`: `Dict[str, str]`

