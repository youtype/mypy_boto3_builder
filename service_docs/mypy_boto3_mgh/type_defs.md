# Structures for boto3 MigrationHub module

> [Index](../index.md) > [MigrationHub](./index.md) > Structures

Auto-generated documentation for [MigrationHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub)
type annotations stubs module [mypy_boto3_mgh](https://pypi.org/project/mypy-boto3-mgh/).

- [Structures for boto3 MigrationHub module](#structures-for-boto3-migrationhub-module)
  - [ApplicationStateTypeDef](#applicationstatetypedef)
  - [CreatedArtifactTypeDef](#createdartifacttypedef)
  - [DiscoveredResourceTypeDef](#discoveredresourcetypedef)
  - [MigrationTaskSummaryTypeDef](#migrationtasksummarytypedef)
  - [MigrationTaskTypeDef](#migrationtasktypedef)
  - [ProgressUpdateStreamSummaryTypeDef](#progressupdatestreamsummarytypedef)
  - [ResourceAttributeTypeDef](#resourceattributetypedef)
  - [TaskTypeDef](#tasktypedef)
  - [DescribeApplicationStateResultTypeDef](#describeapplicationstateresulttypedef)
  - [DescribeMigrationTaskResultTypeDef](#describemigrationtaskresulttypedef)
  - [ListApplicationStatesResultTypeDef](#listapplicationstatesresulttypedef)
  - [ListCreatedArtifactsResultTypeDef](#listcreatedartifactsresulttypedef)
  - [ListDiscoveredResourcesResultTypeDef](#listdiscoveredresourcesresulttypedef)
  - [ListMigrationTasksResultTypeDef](#listmigrationtasksresulttypedef)
  - [ListProgressUpdateStreamsResultTypeDef](#listprogressupdatestreamsresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## ApplicationStateTypeDef

```python
from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef
```




Optional fields:
- `ApplicationId`: `str`
- `ApplicationStatus`: `ApplicationStatus`
- `LastUpdatedTime`: `datetime`


## CreatedArtifactTypeDef

```python
from mypy_boto3_mgh.type_defs import CreatedArtifactTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Description`: `str`


## DiscoveredResourceTypeDef

```python
from mypy_boto3_mgh.type_defs import DiscoveredResourceTypeDef
```


Required fields:
- `ConfigurationId`: `str`



Optional fields:
- `Description`: `str`


## MigrationTaskSummaryTypeDef

```python
from mypy_boto3_mgh.type_defs import MigrationTaskSummaryTypeDef
```




Optional fields:
- `ProgressUpdateStream`: `str`
- `MigrationTaskName`: `str`
- `Status`: `Status`
- `ProgressPercent`: `int`
- `StatusDetail`: `str`
- `UpdateDateTime`: `datetime`


## MigrationTaskTypeDef

```python
from mypy_boto3_mgh.type_defs import MigrationTaskTypeDef
```




Optional fields:
- `ProgressUpdateStream`: `str`
- `MigrationTaskName`: `str`
- `Task`: `"TaskTypeDef"`
- `UpdateDateTime`: `datetime`
- `ResourceAttributeList`: `List["ResourceAttributeTypeDef"]`


## ProgressUpdateStreamSummaryTypeDef

```python
from mypy_boto3_mgh.type_defs import ProgressUpdateStreamSummaryTypeDef
```




Optional fields:
- `ProgressUpdateStreamName`: `str`


## ResourceAttributeTypeDef

```python
from mypy_boto3_mgh.type_defs import ResourceAttributeTypeDef
```


Required fields:
- `Type`: `ResourceAttributeType`
- `Value`: `str`




## TaskTypeDef

```python
from mypy_boto3_mgh.type_defs import TaskTypeDef
```


Required fields:
- `Status`: `Status`



Optional fields:
- `StatusDetail`: `str`
- `ProgressPercent`: `int`


## DescribeApplicationStateResultTypeDef

```python
from mypy_boto3_mgh.type_defs import DescribeApplicationStateResultTypeDef
```




Optional fields:
- `ApplicationStatus`: `ApplicationStatus`
- `LastUpdatedTime`: `datetime`


## DescribeMigrationTaskResultTypeDef

```python
from mypy_boto3_mgh.type_defs import DescribeMigrationTaskResultTypeDef
```




Optional fields:
- `MigrationTask`: `"MigrationTaskTypeDef"`


## ListApplicationStatesResultTypeDef

```python
from mypy_boto3_mgh.type_defs import ListApplicationStatesResultTypeDef
```




Optional fields:
- `ApplicationStateList`: `List["ApplicationStateTypeDef"]`
- `NextToken`: `str`


## ListCreatedArtifactsResultTypeDef

```python
from mypy_boto3_mgh.type_defs import ListCreatedArtifactsResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `CreatedArtifactList`: `List["CreatedArtifactTypeDef"]`


## ListDiscoveredResourcesResultTypeDef

```python
from mypy_boto3_mgh.type_defs import ListDiscoveredResourcesResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `DiscoveredResourceList`: `List["DiscoveredResourceTypeDef"]`


## ListMigrationTasksResultTypeDef

```python
from mypy_boto3_mgh.type_defs import ListMigrationTasksResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MigrationTaskSummaryList`: `List["MigrationTaskSummaryTypeDef"]`


## ListProgressUpdateStreamsResultTypeDef

```python
from mypy_boto3_mgh.type_defs import ListProgressUpdateStreamsResultTypeDef
```




Optional fields:
- `ProgressUpdateStreamSummaryList`: `List["ProgressUpdateStreamSummaryTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mgh.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

