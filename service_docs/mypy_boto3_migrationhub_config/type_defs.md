# Structures for boto3 MigrationHubConfig module

> [Index](../index.md) > [MigrationHubConfig](./index.md) > Structures

Auto-generated documentation for [MigrationHubConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig)
type annotations stubs module [mypy_boto3_migrationhub_config](https://pypi.org/project/mypy-boto3-migrationhub-config/).

- [Structures for boto3 MigrationHubConfig module](#structures-for-boto3-migrationhubconfig-module)
  - [HomeRegionControlTypeDef](#homeregioncontroltypedef)
  - [TargetTypeDef](#targettypedef)
  - [CreateHomeRegionControlResultTypeDef](#createhomeregioncontrolresulttypedef)
  - [DescribeHomeRegionControlsResultTypeDef](#describehomeregioncontrolsresulttypedef)
  - [GetHomeRegionResultTypeDef](#gethomeregionresulttypedef)

## HomeRegionControlTypeDef

```python
from mypy_boto3_migrationhub_config.type_defs import HomeRegionControlTypeDef
```




Optional fields:
- `ControlId`: `str`
- `HomeRegion`: `str`
- `Target`: `"TargetTypeDef"`
- `RequestedTime`: `datetime`


## TargetTypeDef

```python
from mypy_boto3_migrationhub_config.type_defs import TargetTypeDef
```


Required fields:
- `Type`: `TargetType`



Optional fields:
- `Id`: `str`


## CreateHomeRegionControlResultTypeDef

```python
from mypy_boto3_migrationhub_config.type_defs import CreateHomeRegionControlResultTypeDef
```




Optional fields:
- `HomeRegionControl`: `"HomeRegionControlTypeDef"`


## DescribeHomeRegionControlsResultTypeDef

```python
from mypy_boto3_migrationhub_config.type_defs import DescribeHomeRegionControlsResultTypeDef
```




Optional fields:
- `HomeRegionControls`: `List["HomeRegionControlTypeDef"]`
- `NextToken`: `str`


## GetHomeRegionResultTypeDef

```python
from mypy_boto3_migrationhub_config.type_defs import GetHomeRegionResultTypeDef
```




Optional fields:
- `HomeRegion`: `str`

