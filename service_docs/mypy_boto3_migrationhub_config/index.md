# Type annotations for boto3 MigrationHubConfig module

> [Index](../index.md) > MigrationHubConfig

Auto-generated documentation for [MigrationHubConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html#MigrationHubConfig)
type annotations stubs module [mypy_boto3_migrationhub_config](https://pypi.org/project/mypy-boto3-migrationhub-config/).

```bash
pip install mypy-boto3-migrationhub-config
```

- [Type annotations for boto3 MigrationHubConfig module](#type-annotations-for-boto3-migrationhubconfig-module)
  - [MigrationHubConfigClient](#migrationhubconfigclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## MigrationHubConfigClient

Type annotations for  `boto3.client("migrationhub-config")` as [MigrationHubConfigClient](./client.md)

Can be used directly:

```python
from mypy_boto3_migrationhub_config.client import MigrationHubConfigClient
```


MigrationHubConfigClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_home_region_control](./client.md#create-home-region-control)
- [describe_home_region_controls](./client.md#describe-home-region-controls)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_home_region](./client.md#get-home-region)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [DryRunOperation](./client.md#dryrunoperation)
- [InternalServerError](./client.md#internalservererror)
- [InvalidInputException](./client.md#invalidinputexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_migrationhub_config.literals import TargetType, ...
```

- [TargetType](./literals.md#targettype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_migrationhub_config.type_defs import CreateHomeRegionControlResultTypeDef, ...
```

- [CreateHomeRegionControlResultTypeDef](./type_defs.md#createhomeregioncontrolresulttypedef)
- [DescribeHomeRegionControlsResultTypeDef](./type_defs.md#describehomeregioncontrolsresulttypedef)
- [GetHomeRegionResultTypeDef](./type_defs.md#gethomeregionresulttypedef)
- [HomeRegionControlTypeDef](./type_defs.md#homeregioncontroltypedef)
- [TargetTypeDef](./type_defs.md#targettypedef)
