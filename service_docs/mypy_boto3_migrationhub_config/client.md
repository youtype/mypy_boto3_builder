# MigrationHubConfigClient for boto3 MigrationHubConfig module

> [Index](../index.md) > [MigrationHubConfig](./index.md) > MigrationHubConfigClient

Auto-generated documentation for [MigrationHubConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig)
type annotations stubs module [mypy_boto3_migrationhub_config](https://pypi.org/project/mypy-boto3-migrationhub-config/).

- [MigrationHubConfigClient for boto3 MigrationHubConfig module](#migrationhubconfigclient-for-boto3-migrationhubconfig-module)
  - [MigrationHubConfigClient](#migrationhubconfigclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_home_region_control](#create_home_region_control)
    - [describe_home_region_controls](#describe_home_region_controls)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_home_region](#get_home_region)

## MigrationHubConfigClient

Type annotations for `boto3.client("migrationhub-config")`

Can be used directly:

```python
from mypy_boto3_migrationhub_config.client import MigrationHubConfigClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_migrationhub_config.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.DryRunOperation`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidInputException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("migrationhub-config").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_home_region_control

Type annotations for `boto3.client("migrationhub-config").create_home_region_control` method.

[Client.create_home_region_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client.create_home_region_control)

```python
def create_home_region_control(
    self,
    HomeRegion: str,
    Target: "TargetTypeDef",
    DryRun: bool = None
) -> CreateHomeRegionControlResultTypeDef:
    pass
```

### describe_home_region_controls

Type annotations for `boto3.client("migrationhub-config").describe_home_region_controls` method.

[Client.describe_home_region_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client.describe_home_region_controls)

```python
def describe_home_region_controls(
    self,
    ControlId: str = None,
    HomeRegion: str = None,
    Target: "TargetTypeDef" = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeHomeRegionControlsResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("migrationhub-config").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_home_region

Type annotations for `boto3.client("migrationhub-config").get_home_region` method.

[Client.get_home_region documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig.Client.get_home_region)

```python
def get_home_region(
    self
) -> GetHomeRegionResultTypeDef:
    pass
```