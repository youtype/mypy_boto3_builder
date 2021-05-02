# AppConfigClient for boto3 AppConfig module

> [Index](../index.md) > [AppConfig](./index.md) > AppConfigClient

Auto-generated documentation for [AppConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig)
type annotations stubs module [mypy_boto3_appconfig](https://pypi.org/project/mypy-boto3-appconfig/).

- [AppConfigClient for boto3 AppConfig module](#appconfigclient-for-boto3-appconfig-module)
  - [AppConfigClient](#appconfigclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [create_configuration_profile](#create_configuration_profile)
    - [create_deployment_strategy](#create_deployment_strategy)
    - [create_environment](#create_environment)
    - [create_hosted_configuration_version](#create_hosted_configuration_version)
    - [delete_application](#delete_application)
    - [delete_configuration_profile](#delete_configuration_profile)
    - [delete_deployment_strategy](#delete_deployment_strategy)
    - [delete_environment](#delete_environment)
    - [delete_hosted_configuration_version](#delete_hosted_configuration_version)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_application](#get_application)
    - [get_configuration](#get_configuration)
    - [get_configuration_profile](#get_configuration_profile)
    - [get_deployment](#get_deployment)
    - [get_deployment_strategy](#get_deployment_strategy)
    - [get_environment](#get_environment)
    - [get_hosted_configuration_version](#get_hosted_configuration_version)
    - [list_applications](#list_applications)
    - [list_configuration_profiles](#list_configuration_profiles)
    - [list_deployment_strategies](#list_deployment_strategies)
    - [list_deployments](#list_deployments)
    - [list_environments](#list_environments)
    - [list_hosted_configuration_versions](#list_hosted_configuration_versions)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_deployment](#start_deployment)
    - [stop_deployment](#stop_deployment)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_application](#update_application)
    - [update_configuration_profile](#update_configuration_profile)
    - [update_deployment_strategy](#update_deployment_strategy)
    - [update_environment](#update_environment)
    - [validate_configuration](#validate_configuration)

## AppConfigClient

Type annotations for `boto3.client("appconfig")`

Can be used directly:

```python
from mypy_boto3_appconfig.client import AppConfigClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_appconfig.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.PayloadTooLargeException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`


## Methods


### can_paginate

Type annotations for `boto3.client("appconfig").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("appconfig").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_application)

```python
def create_application(
    self,
    Name: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> "ApplicationTypeDef":
    pass
```

### create_configuration_profile

Type annotations for `boto3.client("appconfig").create_configuration_profile` method.

[Client.create_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)

```python
def create_configuration_profile(
    self,
    ApplicationId: str,
    Name: str,
    LocationUri: str,
    Description: str = None,
    RetrievalRoleArn: str = None,
    Validators: List["ValidatorTypeDef"] = None,
    Tags: Dict[str, str] = None
) -> ConfigurationProfileTypeDef:
    pass
```

### create_deployment_strategy

Type annotations for `boto3.client("appconfig").create_deployment_strategy` method.

[Client.create_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)

```python
def create_deployment_strategy(
    self,
    Name: str,
    DeploymentDurationInMinutes: int,
    GrowthFactor: float,
    ReplicateTo: ReplicateTo,
    Description: str = None,
    FinalBakeTimeInMinutes: int = None,
    GrowthType: GrowthType = None,
    Tags: Dict[str, str] = None
) -> "DeploymentStrategyTypeDef":
    pass
```

### create_environment

Type annotations for `boto3.client("appconfig").create_environment` method.

[Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_environment)

```python
def create_environment(
    self,
    ApplicationId: str,
    Name: str,
    Description: str = None,
    Monitors: List["MonitorTypeDef"] = None,
    Tags: Dict[str, str] = None
) -> "EnvironmentTypeDef":
    pass
```

### create_hosted_configuration_version

Type annotations for `boto3.client("appconfig").create_hosted_configuration_version` method.

[Client.create_hosted_configuration_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.create_hosted_configuration_version)

```python
def create_hosted_configuration_version(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str,
    Content: Union[bytes, IO[bytes]],
    ContentType: str,
    Description: str = None,
    LatestVersionNumber: int = None
) -> HostedConfigurationVersionTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("appconfig").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_application)

```python
def delete_application(
    self,
    ApplicationId: str
) -> None:
    pass
```

### delete_configuration_profile

Type annotations for `boto3.client("appconfig").delete_configuration_profile` method.

[Client.delete_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)

```python
def delete_configuration_profile(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str
) -> None:
    pass
```

### delete_deployment_strategy

Type annotations for `boto3.client("appconfig").delete_deployment_strategy` method.

[Client.delete_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)

```python
def delete_deployment_strategy(
    self,
    DeploymentStrategyId: str
) -> None:
    pass
```

### delete_environment

Type annotations for `boto3.client("appconfig").delete_environment` method.

[Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_environment)

```python
def delete_environment(
    self,
    ApplicationId: str,
    EnvironmentId: str
) -> None:
    pass
```

### delete_hosted_configuration_version

Type annotations for `boto3.client("appconfig").delete_hosted_configuration_version` method.

[Client.delete_hosted_configuration_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.delete_hosted_configuration_version)

```python
def delete_hosted_configuration_version(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str,
    VersionNumber: int
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("appconfig").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)

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

### get_application

Type annotations for `boto3.client("appconfig").get_application` method.

[Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_application)

```python
def get_application(
    self,
    ApplicationId: str
) -> "ApplicationTypeDef":
    pass
```

### get_configuration

Type annotations for `boto3.client("appconfig").get_configuration` method.

[Client.get_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_configuration)

```python
def get_configuration(
    self,
    Application: str,
    Environment: str,
    Configuration: str,
    ClientId: str,
    ClientConfigurationVersion: str = None
) -> ConfigurationTypeDef:
    pass
```

### get_configuration_profile

Type annotations for `boto3.client("appconfig").get_configuration_profile` method.

[Client.get_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)

```python
def get_configuration_profile(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str
) -> ConfigurationProfileTypeDef:
    pass
```

### get_deployment

Type annotations for `boto3.client("appconfig").get_deployment` method.

[Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_deployment)

```python
def get_deployment(
    self,
    ApplicationId: str,
    EnvironmentId: str,
    DeploymentNumber: int
) -> DeploymentTypeDef:
    pass
```

### get_deployment_strategy

Type annotations for `boto3.client("appconfig").get_deployment_strategy` method.

[Client.get_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)

```python
def get_deployment_strategy(
    self,
    DeploymentStrategyId: str
) -> "DeploymentStrategyTypeDef":
    pass
```

### get_environment

Type annotations for `boto3.client("appconfig").get_environment` method.

[Client.get_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_environment)

```python
def get_environment(
    self,
    ApplicationId: str,
    EnvironmentId: str
) -> "EnvironmentTypeDef":
    pass
```

### get_hosted_configuration_version

Type annotations for `boto3.client("appconfig").get_hosted_configuration_version` method.

[Client.get_hosted_configuration_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.get_hosted_configuration_version)

```python
def get_hosted_configuration_version(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str,
    VersionNumber: int
) -> HostedConfigurationVersionTypeDef:
    pass
```

### list_applications

Type annotations for `boto3.client("appconfig").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_applications)

```python
def list_applications(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ApplicationsTypeDef:
    pass
```

### list_configuration_profiles

Type annotations for `boto3.client("appconfig").list_configuration_profiles` method.

[Client.list_configuration_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)

```python
def list_configuration_profiles(
    self,
    ApplicationId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ConfigurationProfilesTypeDef:
    pass
```

### list_deployment_strategies

Type annotations for `boto3.client("appconfig").list_deployment_strategies` method.

[Client.list_deployment_strategies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)

```python
def list_deployment_strategies(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> DeploymentStrategiesTypeDef:
    pass
```

### list_deployments

Type annotations for `boto3.client("appconfig").list_deployments` method.

[Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_deployments)

```python
def list_deployments(
    self,
    ApplicationId: str,
    EnvironmentId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DeploymentsTypeDef:
    pass
```

### list_environments

Type annotations for `boto3.client("appconfig").list_environments` method.

[Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_environments)

```python
def list_environments(
    self,
    ApplicationId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> EnvironmentsTypeDef:
    pass
```

### list_hosted_configuration_versions

Type annotations for `boto3.client("appconfig").list_hosted_configuration_versions` method.

[Client.list_hosted_configuration_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_hosted_configuration_versions)

```python
def list_hosted_configuration_versions(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> HostedConfigurationVersionsTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("appconfig").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ResourceTagsTypeDef:
    pass
```

### start_deployment

Type annotations for `boto3.client("appconfig").start_deployment` method.

[Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.start_deployment)

```python
def start_deployment(
    self,
    ApplicationId: str,
    EnvironmentId: str,
    DeploymentStrategyId: str,
    ConfigurationProfileId: str,
    ConfigurationVersion: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> DeploymentTypeDef:
    pass
```

### stop_deployment

Type annotations for `boto3.client("appconfig").stop_deployment` method.

[Client.stop_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.stop_deployment)

```python
def stop_deployment(
    self,
    ApplicationId: str,
    EnvironmentId: str,
    DeploymentNumber: int
) -> DeploymentTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("appconfig").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("appconfig").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_application

Type annotations for `boto3.client("appconfig").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_application)

```python
def update_application(
    self,
    ApplicationId: str,
    Name: str = None,
    Description: str = None
) -> "ApplicationTypeDef":
    pass
```

### update_configuration_profile

Type annotations for `boto3.client("appconfig").update_configuration_profile` method.

[Client.update_configuration_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)

```python
def update_configuration_profile(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str,
    Name: str = None,
    Description: str = None,
    RetrievalRoleArn: str = None,
    Validators: List["ValidatorTypeDef"] = None
) -> ConfigurationProfileTypeDef:
    pass
```

### update_deployment_strategy

Type annotations for `boto3.client("appconfig").update_deployment_strategy` method.

[Client.update_deployment_strategy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)

```python
def update_deployment_strategy(
    self,
    DeploymentStrategyId: str,
    Description: str = None,
    DeploymentDurationInMinutes: int = None,
    FinalBakeTimeInMinutes: int = None,
    GrowthFactor: float = None,
    GrowthType: GrowthType = None
) -> "DeploymentStrategyTypeDef":
    pass
```

### update_environment

Type annotations for `boto3.client("appconfig").update_environment` method.

[Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.update_environment)

```python
def update_environment(
    self,
    ApplicationId: str,
    EnvironmentId: str,
    Name: str = None,
    Description: str = None,
    Monitors: List["MonitorTypeDef"] = None
) -> "EnvironmentTypeDef":
    pass
```

### validate_configuration

Type annotations for `boto3.client("appconfig").validate_configuration` method.

[Client.validate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig.Client.validate_configuration)

```python
def validate_configuration(
    self,
    ApplicationId: str,
    ConfigurationProfileId: str,
    ConfigurationVersion: str
) -> None:
    pass
```



