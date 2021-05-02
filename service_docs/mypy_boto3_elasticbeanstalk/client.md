# ElasticBeanstalkClient for boto3 ElasticBeanstalk module

> [Index](../index.md) > [ElasticBeanstalk](./index.md) > ElasticBeanstalkClient

Auto-generated documentation for [ElasticBeanstalk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk)
type annotations stubs module [mypy_boto3_elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/).

- [ElasticBeanstalkClient for boto3 ElasticBeanstalk module](#elasticbeanstalkclient-for-boto3-elasticbeanstalk-module)
  - [ElasticBeanstalkClient](#elasticbeanstalkclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [abort_environment_update](#abort_environment_update)
    - [apply_environment_managed_action](#apply_environment_managed_action)
    - [associate_environment_operations_role](#associate_environment_operations_role)
    - [can_paginate](#can_paginate)
    - [check_dns_availability](#check_dns_availability)
    - [compose_environments](#compose_environments)
    - [create_application](#create_application)
    - [create_application_version](#create_application_version)
    - [create_configuration_template](#create_configuration_template)
    - [create_environment](#create_environment)
    - [create_platform_version](#create_platform_version)
    - [create_storage_location](#create_storage_location)
    - [delete_application](#delete_application)
    - [delete_application_version](#delete_application_version)
    - [delete_configuration_template](#delete_configuration_template)
    - [delete_environment_configuration](#delete_environment_configuration)
    - [delete_platform_version](#delete_platform_version)
    - [describe_account_attributes](#describe_account_attributes)
    - [describe_application_versions](#describe_application_versions)
    - [describe_applications](#describe_applications)
    - [describe_configuration_options](#describe_configuration_options)
    - [describe_configuration_settings](#describe_configuration_settings)
    - [describe_environment_health](#describe_environment_health)
    - [describe_environment_managed_action_history](#describe_environment_managed_action_history)
    - [describe_environment_managed_actions](#describe_environment_managed_actions)
    - [describe_environment_resources](#describe_environment_resources)
    - [describe_environments](#describe_environments)
    - [describe_events](#describe_events)
    - [describe_instances_health](#describe_instances_health)
    - [describe_platform_version](#describe_platform_version)
    - [disassociate_environment_operations_role](#disassociate_environment_operations_role)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_available_solution_stacks](#list_available_solution_stacks)
    - [list_platform_branches](#list_platform_branches)
    - [list_platform_versions](#list_platform_versions)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [rebuild_environment](#rebuild_environment)
    - [request_environment_info](#request_environment_info)
    - [restart_app_server](#restart_app_server)
    - [retrieve_environment_info](#retrieve_environment_info)
    - [swap_environment_cnames](#swap_environment_cnames)
    - [terminate_environment](#terminate_environment)
    - [update_application](#update_application)
    - [update_application_resource_lifecycle](#update_application_resource_lifecycle)
    - [update_application_version](#update_application_version)
    - [update_configuration_template](#update_configuration_template)
    - [update_environment](#update_environment)
    - [update_tags_for_resource](#update_tags_for_resource)
    - [validate_configuration_settings](#validate_configuration_settings)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)

## ElasticBeanstalkClient

Type annotations for `boto3.client("elasticbeanstalk")`

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.client import ElasticBeanstalkClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_elasticbeanstalk.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CodeBuildNotInServiceRegionException`
- `Exceptions.ElasticBeanstalkServiceException`
- `Exceptions.InsufficientPrivilegesException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ManagedActionInvalidStateException`
- `Exceptions.OperationInProgressException`
- `Exceptions.PlatformVersionStillReferencedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceTypeNotSupportedException`
- `Exceptions.S3LocationNotInServiceRegionException`
- `Exceptions.S3SubscriptionRequiredException`
- `Exceptions.SourceBundleDeletionException`
- `Exceptions.TooManyApplicationVersionsException`
- `Exceptions.TooManyApplicationsException`
- `Exceptions.TooManyBucketsException`
- `Exceptions.TooManyConfigurationTemplatesException`
- `Exceptions.TooManyEnvironmentsException`
- `Exceptions.TooManyPlatformsException`
- `Exceptions.TooManyTagsException`


## Methods


### abort_environment_update

Type annotations for `boto3.client("elasticbeanstalk").abort_environment_update` method.

[Client.abort_environment_update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.abort_environment_update)

```python
def abort_environment_update(
    self,
    EnvironmentId: str = None,
    EnvironmentName: str = None
) -> None:
    pass
```

### apply_environment_managed_action

Type annotations for `boto3.client("elasticbeanstalk").apply_environment_managed_action` method.

[Client.apply_environment_managed_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.apply_environment_managed_action)

```python
def apply_environment_managed_action(
    self,
    ActionId: str,
    EnvironmentName: str = None,
    EnvironmentId: str = None
) -> ApplyEnvironmentManagedActionResultTypeDef:
    pass
```

### associate_environment_operations_role

Type annotations for `boto3.client("elasticbeanstalk").associate_environment_operations_role` method.

[Client.associate_environment_operations_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.associate_environment_operations_role)

```python
def associate_environment_operations_role(
    self,
    EnvironmentName: str,
    OperationsRole: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("elasticbeanstalk").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### check_dns_availability

Type annotations for `boto3.client("elasticbeanstalk").check_dns_availability` method.

[Client.check_dns_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.check_dns_availability)

```python
def check_dns_availability(
    self,
    CNAMEPrefix: str
) -> CheckDNSAvailabilityResultMessageTypeDef:
    pass
```

### compose_environments

Type annotations for `boto3.client("elasticbeanstalk").compose_environments` method.

[Client.compose_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.compose_environments)

```python
def compose_environments(
    self,
    ApplicationName: str = None,
    GroupName: str = None,
    VersionLabels: List[str] = None
) -> EnvironmentDescriptionsMessageTypeDef:
    pass
```

### create_application

Type annotations for `boto3.client("elasticbeanstalk").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application)

```python
def create_application(
    self,
    ApplicationName: str,
    Description: str = None,
    ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> ApplicationDescriptionMessageTypeDef:
    pass
```

### create_application_version

Type annotations for `boto3.client("elasticbeanstalk").create_application_version` method.

[Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application_version)

```python
def create_application_version(
    self,
    ApplicationName: str,
    VersionLabel: str,
    Description: str = None,
    SourceBuildInformation: "SourceBuildInformationTypeDef" = None,
    SourceBundle: "S3LocationTypeDef" = None,
    BuildConfiguration: BuildConfigurationTypeDef = None,
    AutoCreateApplication: bool = None,
    Process: bool = None,
    Tags: List["TagTypeDef"] = None
) -> ApplicationVersionDescriptionMessageTypeDef:
    pass
```

### create_configuration_template

Type annotations for `boto3.client("elasticbeanstalk").create_configuration_template` method.

[Client.create_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_configuration_template)

```python
def create_configuration_template(
    self,
    ApplicationName: str,
    TemplateName: str,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    SourceConfiguration: SourceConfigurationTypeDef = None,
    EnvironmentId: str = None,
    Description: str = None,
    OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> "ConfigurationSettingsDescriptionTypeDef":
    pass
```

### create_environment

Type annotations for `boto3.client("elasticbeanstalk").create_environment` method.

[Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_environment)

```python
def create_environment(
    self,
    ApplicationName: str,
    EnvironmentName: str = None,
    GroupName: str = None,
    Description: str = None,
    CNAMEPrefix: str = None,
    Tier: "EnvironmentTierTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
    OptionsToRemove: List[OptionSpecificationTypeDef] = None,
    OperationsRole: str = None
) -> "EnvironmentDescriptionTypeDef":
    pass
```

### create_platform_version

Type annotations for `boto3.client("elasticbeanstalk").create_platform_version` method.

[Client.create_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_platform_version)

```python
def create_platform_version(
    self,
    PlatformName: str,
    PlatformVersion: str,
    PlatformDefinitionBundle: "S3LocationTypeDef",
    EnvironmentName: str = None,
    OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePlatformVersionResultTypeDef:
    pass
```

### create_storage_location

Type annotations for `boto3.client("elasticbeanstalk").create_storage_location` method.

[Client.create_storage_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_storage_location)

```python
def create_storage_location(
    self
) -> CreateStorageLocationResultMessageTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("elasticbeanstalk").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application)

```python
def delete_application(
    self,
    ApplicationName: str,
    TerminateEnvByForce: bool = None
) -> None:
    pass
```

### delete_application_version

Type annotations for `boto3.client("elasticbeanstalk").delete_application_version` method.

[Client.delete_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application_version)

```python
def delete_application_version(
    self,
    ApplicationName: str,
    VersionLabel: str,
    DeleteSourceBundle: bool = None
) -> None:
    pass
```

### delete_configuration_template

Type annotations for `boto3.client("elasticbeanstalk").delete_configuration_template` method.

[Client.delete_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_configuration_template)

```python
def delete_configuration_template(
    self,
    ApplicationName: str,
    TemplateName: str
) -> None:
    pass
```

### delete_environment_configuration

Type annotations for `boto3.client("elasticbeanstalk").delete_environment_configuration` method.

[Client.delete_environment_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_environment_configuration)

```python
def delete_environment_configuration(
    self,
    ApplicationName: str,
    EnvironmentName: str
) -> None:
    pass
```

### delete_platform_version

Type annotations for `boto3.client("elasticbeanstalk").delete_platform_version` method.

[Client.delete_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_platform_version)

```python
def delete_platform_version(
    self,
    PlatformArn: str = None
) -> DeletePlatformVersionResultTypeDef:
    pass
```

### describe_account_attributes

Type annotations for `boto3.client("elasticbeanstalk").describe_account_attributes` method.

[Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_account_attributes)

```python
def describe_account_attributes(
    self
) -> DescribeAccountAttributesResultTypeDef:
    pass
```

### describe_application_versions

Type annotations for `boto3.client("elasticbeanstalk").describe_application_versions` method.

[Client.describe_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_application_versions)

```python
def describe_application_versions(
    self,
    ApplicationName: str = None,
    VersionLabels: List[str] = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> ApplicationVersionDescriptionsMessageTypeDef:
    pass
```

### describe_applications

Type annotations for `boto3.client("elasticbeanstalk").describe_applications` method.

[Client.describe_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_applications)

```python
def describe_applications(
    self,
    ApplicationNames: List[str] = None
) -> ApplicationDescriptionsMessageTypeDef:
    pass
```

### describe_configuration_options

Type annotations for `boto3.client("elasticbeanstalk").describe_configuration_options` method.

[Client.describe_configuration_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_options)

```python
def describe_configuration_options(
    self,
    ApplicationName: str = None,
    TemplateName: str = None,
    EnvironmentName: str = None,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    Options: List[OptionSpecificationTypeDef] = None
) -> ConfigurationOptionsDescriptionTypeDef:
    pass
```

### describe_configuration_settings

Type annotations for `boto3.client("elasticbeanstalk").describe_configuration_settings` method.

[Client.describe_configuration_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_settings)

```python
def describe_configuration_settings(
    self,
    ApplicationName: str,
    TemplateName: str = None,
    EnvironmentName: str = None
) -> ConfigurationSettingsDescriptionsTypeDef:
    pass
```

### describe_environment_health

Type annotations for `boto3.client("elasticbeanstalk").describe_environment_health` method.

[Client.describe_environment_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_health)

```python
def describe_environment_health(
    self,
    EnvironmentName: str = None,
    EnvironmentId: str = None,
    AttributeNames: List[EnvironmentHealthAttribute] = None
) -> DescribeEnvironmentHealthResultTypeDef:
    pass
```

### describe_environment_managed_action_history

Type annotations for `boto3.client("elasticbeanstalk").describe_environment_managed_action_history` method.

[Client.describe_environment_managed_action_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_action_history)

```python
def describe_environment_managed_action_history(
    self,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    NextToken: str = None,
    MaxItems: int = None
) -> DescribeEnvironmentManagedActionHistoryResultTypeDef:
    pass
```

### describe_environment_managed_actions

Type annotations for `boto3.client("elasticbeanstalk").describe_environment_managed_actions` method.

[Client.describe_environment_managed_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_actions)

```python
def describe_environment_managed_actions(
    self,
    EnvironmentName: str = None,
    EnvironmentId: str = None,
    Status: ActionStatus = None
) -> DescribeEnvironmentManagedActionsResultTypeDef:
    pass
```

### describe_environment_resources

Type annotations for `boto3.client("elasticbeanstalk").describe_environment_resources` method.

[Client.describe_environment_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_resources)

```python
def describe_environment_resources(
    self,
    EnvironmentId: str = None,
    EnvironmentName: str = None
) -> EnvironmentResourceDescriptionsMessageTypeDef:
    pass
```

### describe_environments

Type annotations for `boto3.client("elasticbeanstalk").describe_environments` method.

[Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environments)

```python
def describe_environments(
    self,
    ApplicationName: str = None,
    VersionLabel: str = None,
    EnvironmentIds: List[str] = None,
    EnvironmentNames: List[str] = None,
    IncludeDeleted: bool = None,
    IncludedDeletedBackTo: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> EnvironmentDescriptionsMessageTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("elasticbeanstalk").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_events)

```python
def describe_events(
    self,
    ApplicationName: str = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    PlatformArn: str = None,
    RequestId: str = None,
    Severity: EventSeverity = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> EventDescriptionsMessageTypeDef:
    pass
```

### describe_instances_health

Type annotations for `boto3.client("elasticbeanstalk").describe_instances_health` method.

[Client.describe_instances_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_instances_health)

```python
def describe_instances_health(
    self,
    EnvironmentName: str = None,
    EnvironmentId: str = None,
    AttributeNames: List[InstancesHealthAttribute] = None,
    NextToken: str = None
) -> DescribeInstancesHealthResultTypeDef:
    pass
```

### describe_platform_version

Type annotations for `boto3.client("elasticbeanstalk").describe_platform_version` method.

[Client.describe_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_platform_version)

```python
def describe_platform_version(
    self,
    PlatformArn: str = None
) -> DescribePlatformVersionResultTypeDef:
    pass
```

### disassociate_environment_operations_role

Type annotations for `boto3.client("elasticbeanstalk").disassociate_environment_operations_role` method.

[Client.disassociate_environment_operations_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.disassociate_environment_operations_role)

```python
def disassociate_environment_operations_role(
    self,
    EnvironmentName: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("elasticbeanstalk").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.generate_presigned_url)

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

### list_available_solution_stacks

Type annotations for `boto3.client("elasticbeanstalk").list_available_solution_stacks` method.

[Client.list_available_solution_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_available_solution_stacks)

```python
def list_available_solution_stacks(
    self
) -> ListAvailableSolutionStacksResultMessageTypeDef:
    pass
```

### list_platform_branches

Type annotations for `boto3.client("elasticbeanstalk").list_platform_branches` method.

[Client.list_platform_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_branches)

```python
def list_platform_branches(
    self,
    Filters: List[SearchFilterTypeDef] = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> ListPlatformBranchesResultTypeDef:
    pass
```

### list_platform_versions

Type annotations for `boto3.client("elasticbeanstalk").list_platform_versions` method.

[Client.list_platform_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_versions)

```python
def list_platform_versions(
    self,
    Filters: List[PlatformFilterTypeDef] = None,
    MaxRecords: int = None,
    NextToken: str = None
) -> ListPlatformVersionsResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("elasticbeanstalk").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ResourceTagsDescriptionMessageTypeDef:
    pass
```

### rebuild_environment

Type annotations for `boto3.client("elasticbeanstalk").rebuild_environment` method.

[Client.rebuild_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.rebuild_environment)

```python
def rebuild_environment(
    self,
    EnvironmentId: str = None,
    EnvironmentName: str = None
) -> None:
    pass
```

### request_environment_info

Type annotations for `boto3.client("elasticbeanstalk").request_environment_info` method.

[Client.request_environment_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.request_environment_info)

```python
def request_environment_info(
    self,
    InfoType: EnvironmentInfoType,
    EnvironmentId: str = None,
    EnvironmentName: str = None
) -> None:
    pass
```

### restart_app_server

Type annotations for `boto3.client("elasticbeanstalk").restart_app_server` method.

[Client.restart_app_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.restart_app_server)

```python
def restart_app_server(
    self,
    EnvironmentId: str = None,
    EnvironmentName: str = None
) -> None:
    pass
```

### retrieve_environment_info

Type annotations for `boto3.client("elasticbeanstalk").retrieve_environment_info` method.

[Client.retrieve_environment_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.retrieve_environment_info)

```python
def retrieve_environment_info(
    self,
    InfoType: EnvironmentInfoType,
    EnvironmentId: str = None,
    EnvironmentName: str = None
) -> RetrieveEnvironmentInfoResultMessageTypeDef:
    pass
```

### swap_environment_cnames

Type annotations for `boto3.client("elasticbeanstalk").swap_environment_cnames` method.

[Client.swap_environment_cnames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.swap_environment_cnames)

```python
def swap_environment_cnames(
    self,
    SourceEnvironmentId: str = None,
    SourceEnvironmentName: str = None,
    DestinationEnvironmentId: str = None,
    DestinationEnvironmentName: str = None
) -> None:
    pass
```

### terminate_environment

Type annotations for `boto3.client("elasticbeanstalk").terminate_environment` method.

[Client.terminate_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.terminate_environment)

```python
def terminate_environment(
    self,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    TerminateResources: bool = None,
    ForceTerminate: bool = None
) -> "EnvironmentDescriptionTypeDef":
    pass
```

### update_application

Type annotations for `boto3.client("elasticbeanstalk").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application)

```python
def update_application(
    self,
    ApplicationName: str,
    Description: str = None
) -> ApplicationDescriptionMessageTypeDef:
    pass
```

### update_application_resource_lifecycle

Type annotations for `boto3.client("elasticbeanstalk").update_application_resource_lifecycle` method.

[Client.update_application_resource_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_resource_lifecycle)

```python
def update_application_resource_lifecycle(
    self,
    ApplicationName: str,
    ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef"
) -> ApplicationResourceLifecycleDescriptionMessageTypeDef:
    pass
```

### update_application_version

Type annotations for `boto3.client("elasticbeanstalk").update_application_version` method.

[Client.update_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_version)

```python
def update_application_version(
    self,
    ApplicationName: str,
    VersionLabel: str,
    Description: str = None
) -> ApplicationVersionDescriptionMessageTypeDef:
    pass
```

### update_configuration_template

Type annotations for `boto3.client("elasticbeanstalk").update_configuration_template` method.

[Client.update_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_configuration_template)

```python
def update_configuration_template(
    self,
    ApplicationName: str,
    TemplateName: str,
    Description: str = None,
    OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
    OptionsToRemove: List[OptionSpecificationTypeDef] = None
) -> "ConfigurationSettingsDescriptionTypeDef":
    pass
```

### update_environment

Type annotations for `boto3.client("elasticbeanstalk").update_environment` method.

[Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_environment)

```python
def update_environment(
    self,
    ApplicationName: str = None,
    EnvironmentId: str = None,
    EnvironmentName: str = None,
    GroupName: str = None,
    Description: str = None,
    Tier: "EnvironmentTierTypeDef" = None,
    VersionLabel: str = None,
    TemplateName: str = None,
    SolutionStackName: str = None,
    PlatformArn: str = None,
    OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
    OptionsToRemove: List[OptionSpecificationTypeDef] = None
) -> "EnvironmentDescriptionTypeDef":
    pass
```

### update_tags_for_resource

Type annotations for `boto3.client("elasticbeanstalk").update_tags_for_resource` method.

[Client.update_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_tags_for_resource)

```python
def update_tags_for_resource(
    self,
    ResourceArn: str,
    TagsToAdd: List["TagTypeDef"] = None,
    TagsToRemove: List[str] = None
) -> None:
    pass
```

### validate_configuration_settings

Type annotations for `boto3.client("elasticbeanstalk").validate_configuration_settings` method.

[Client.validate_configuration_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.validate_configuration_settings)

```python
def validate_configuration_settings(
    self,
    ApplicationName: str,
    OptionSettings: List["ConfigurationOptionSettingTypeDef"],
    TemplateName: str = None,
    EnvironmentName: str = None
) -> ConfigurationSettingsValidationMessagesTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator` method.

[Paginator.DescribeApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeApplicationVersionsPaginatorName
) -> DescribeApplicationVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator` method.

[Paginator.DescribeEnvironmentManagedActionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEnvironmentManagedActionHistoryPaginatorName
) -> DescribeEnvironmentManagedActionHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator` method.

[Paginator.DescribeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEnvironmentsPaginatorName
) -> DescribeEnvironmentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator` method.

[Paginator.ListPlatformVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPlatformVersionsPaginatorName
) -> ListPlatformVersionsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("elasticbeanstalk").get_waiter` method.

[Waiter.EnvironmentExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: EnvironmentExistsWaiterName
) -> EnvironmentExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("elasticbeanstalk").get_waiter` method.

[Waiter.EnvironmentTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated)

```python
@overload
def get_waiter(
    self,
    waiter_name: EnvironmentTerminatedWaiterName
) -> EnvironmentTerminatedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("elasticbeanstalk").get_waiter` method.

[Waiter.EnvironmentUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated)

```python
@overload
def get_waiter(
    self,
    waiter_name: EnvironmentUpdatedWaiterName
) -> EnvironmentUpdatedWaiter:
    pass
```