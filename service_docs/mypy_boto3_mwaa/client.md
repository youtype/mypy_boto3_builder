# MWAAClient for boto3 MWAA module

> [Index](../index.md) > [MWAA](./index.md) > MWAAClient

Auto-generated documentation for [MWAA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA)
type annotations stubs module [mypy_boto3_mwaa](https://pypi.org/project/mypy-boto3-mwaa/).

- [MWAAClient for boto3 MWAA module](#mwaaclient-for-boto3-mwaa-module)
  - [MWAAClient](#mwaaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_cli_token](#create_cli_token)
    - [create_environment](#create_environment)
    - [create_web_login_token](#create_web_login_token)
    - [delete_environment](#delete_environment)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_environment](#get_environment)
    - [list_environments](#list_environments)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [publish_metrics](#publish_metrics)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_environment](#update_environment)
    - [get_paginator](#get_paginator)

## MWAAClient

Type annotations for `boto3.client("mwaa")`

Can be used directly:

```python
from mypy_boto3_mwaa.client import MWAAClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mwaa.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("mwaa").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_cli_token

Type annotations for `boto3.client("mwaa").create_cli_token` method.

[Client.create_cli_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_cli_token)

```python
def create_cli_token(
    self,
    Name: str
) -> CreateCliTokenResponseTypeDef:
    pass
```

### create_environment

Type annotations for `boto3.client("mwaa").create_environment` method.

[Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_environment)

```python
def create_environment(
    self,
    DagS3Path: str,
    ExecutionRoleArn: str,
    Name: str,
    NetworkConfiguration: "NetworkConfigurationTypeDef",
    SourceBucketArn: str,
    AirflowConfigurationOptions: Dict[str, str] = None,
    AirflowVersion: str = None,
    EnvironmentClass: str = None,
    KmsKey: str = None,
    LoggingConfiguration: LoggingConfigurationInputTypeDef = None,
    MaxWorkers: int = None,
    MinWorkers: int = None,
    PluginsS3ObjectVersion: str = None,
    PluginsS3Path: str = None,
    RequirementsS3ObjectVersion: str = None,
    RequirementsS3Path: str = None,
    Tags: Dict[str, str] = None,
    WebserverAccessMode: WebserverAccessMode = None,
    WeeklyMaintenanceWindowStart: str = None
) -> CreateEnvironmentOutputTypeDef:
    pass
```

### create_web_login_token

Type annotations for `boto3.client("mwaa").create_web_login_token` method.

[Client.create_web_login_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_web_login_token)

```python
def create_web_login_token(
    self,
    Name: str
) -> CreateWebLoginTokenResponseTypeDef:
    pass
```

### delete_environment

Type annotations for `boto3.client("mwaa").delete_environment` method.

[Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.delete_environment)

```python
def delete_environment(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mwaa").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.generate_presigned_url)

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

### get_environment

Type annotations for `boto3.client("mwaa").get_environment` method.

[Client.get_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.get_environment)

```python
def get_environment(
    self,
    Name: str
) -> GetEnvironmentOutputTypeDef:
    pass
```

### list_environments

Type annotations for `boto3.client("mwaa").list_environments` method.

[Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.list_environments)

```python
def list_environments(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListEnvironmentsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mwaa").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### publish_metrics

Type annotations for `boto3.client("mwaa").publish_metrics` method.

[Client.publish_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.publish_metrics)

```python
def publish_metrics(
    self,
    EnvironmentName: str,
    MetricData: List[MetricDatumTypeDef]
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("mwaa").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("mwaa").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_environment

Type annotations for `boto3.client("mwaa").update_environment` method.

[Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.update_environment)

```python
def update_environment(
    self,
    Name: str,
    AirflowConfigurationOptions: Dict[str, str] = None,
    AirflowVersion: str = None,
    DagS3Path: str = None,
    EnvironmentClass: str = None,
    ExecutionRoleArn: str = None,
    LoggingConfiguration: LoggingConfigurationInputTypeDef = None,
    MaxWorkers: int = None,
    MinWorkers: int = None,
    NetworkConfiguration: UpdateNetworkConfigurationInputTypeDef = None,
    PluginsS3ObjectVersion: str = None,
    PluginsS3Path: str = None,
    RequirementsS3ObjectVersion: str = None,
    RequirementsS3Path: str = None,
    SourceBucketArn: str = None,
    WebserverAccessMode: WebserverAccessMode = None,
    WeeklyMaintenanceWindowStart: str = None
) -> UpdateEnvironmentOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mwaa").get_paginator` method with overloads.

- `client.get_paginator("list_environments")` -> [ListEnvironmentsPaginator](./paginators.md#listenvironmentspaginator)


