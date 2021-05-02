# GreengrassClient for boto3 Greengrass module

> [Index](../index.md) > [Greengrass](./index.md) > GreengrassClient

Auto-generated documentation for [Greengrass](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass)
type annotations stubs module [mypy_boto3_greengrass](https://pypi.org/project/mypy-boto3-greengrass/).

- [GreengrassClient for boto3 Greengrass module](#greengrassclient-for-boto3-greengrass-module)
  - [GreengrassClient](#greengrassclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_role_to_group](#associate_role_to_group)
    - [associate_service_role_to_account](#associate_service_role_to_account)
    - [can_paginate](#can_paginate)
    - [create_connector_definition](#create_connector_definition)
    - [create_connector_definition_version](#create_connector_definition_version)
    - [create_core_definition](#create_core_definition)
    - [create_core_definition_version](#create_core_definition_version)
    - [create_deployment](#create_deployment)
    - [create_device_definition](#create_device_definition)
    - [create_device_definition_version](#create_device_definition_version)
    - [create_function_definition](#create_function_definition)
    - [create_function_definition_version](#create_function_definition_version)
    - [create_group](#create_group)
    - [create_group_certificate_authority](#create_group_certificate_authority)
    - [create_group_version](#create_group_version)
    - [create_logger_definition](#create_logger_definition)
    - [create_logger_definition_version](#create_logger_definition_version)
    - [create_resource_definition](#create_resource_definition)
    - [create_resource_definition_version](#create_resource_definition_version)
    - [create_software_update_job](#create_software_update_job)
    - [create_subscription_definition](#create_subscription_definition)
    - [create_subscription_definition_version](#create_subscription_definition_version)
    - [delete_connector_definition](#delete_connector_definition)
    - [delete_core_definition](#delete_core_definition)
    - [delete_device_definition](#delete_device_definition)
    - [delete_function_definition](#delete_function_definition)
    - [delete_group](#delete_group)
    - [delete_logger_definition](#delete_logger_definition)
    - [delete_resource_definition](#delete_resource_definition)
    - [delete_subscription_definition](#delete_subscription_definition)
    - [disassociate_role_from_group](#disassociate_role_from_group)
    - [disassociate_service_role_from_account](#disassociate_service_role_from_account)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_associated_role](#get_associated_role)
    - [get_bulk_deployment_status](#get_bulk_deployment_status)
    - [get_connectivity_info](#get_connectivity_info)
    - [get_connector_definition](#get_connector_definition)
    - [get_connector_definition_version](#get_connector_definition_version)
    - [get_core_definition](#get_core_definition)
    - [get_core_definition_version](#get_core_definition_version)
    - [get_deployment_status](#get_deployment_status)
    - [get_device_definition](#get_device_definition)
    - [get_device_definition_version](#get_device_definition_version)
    - [get_function_definition](#get_function_definition)
    - [get_function_definition_version](#get_function_definition_version)
    - [get_group](#get_group)
    - [get_group_certificate_authority](#get_group_certificate_authority)
    - [get_group_certificate_configuration](#get_group_certificate_configuration)
    - [get_group_version](#get_group_version)
    - [get_logger_definition](#get_logger_definition)
    - [get_logger_definition_version](#get_logger_definition_version)
    - [get_resource_definition](#get_resource_definition)
    - [get_resource_definition_version](#get_resource_definition_version)
    - [get_service_role_for_account](#get_service_role_for_account)
    - [get_subscription_definition](#get_subscription_definition)
    - [get_subscription_definition_version](#get_subscription_definition_version)
    - [get_thing_runtime_configuration](#get_thing_runtime_configuration)
    - [list_bulk_deployment_detailed_reports](#list_bulk_deployment_detailed_reports)
    - [list_bulk_deployments](#list_bulk_deployments)
    - [list_connector_definition_versions](#list_connector_definition_versions)
    - [list_connector_definitions](#list_connector_definitions)
    - [list_core_definition_versions](#list_core_definition_versions)
    - [list_core_definitions](#list_core_definitions)
    - [list_deployments](#list_deployments)
    - [list_device_definition_versions](#list_device_definition_versions)
    - [list_device_definitions](#list_device_definitions)
    - [list_function_definition_versions](#list_function_definition_versions)
    - [list_function_definitions](#list_function_definitions)
    - [list_group_certificate_authorities](#list_group_certificate_authorities)
    - [list_group_versions](#list_group_versions)
    - [list_groups](#list_groups)
    - [list_logger_definition_versions](#list_logger_definition_versions)
    - [list_logger_definitions](#list_logger_definitions)
    - [list_resource_definition_versions](#list_resource_definition_versions)
    - [list_resource_definitions](#list_resource_definitions)
    - [list_subscription_definition_versions](#list_subscription_definition_versions)
    - [list_subscription_definitions](#list_subscription_definitions)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [reset_deployments](#reset_deployments)
    - [start_bulk_deployment](#start_bulk_deployment)
    - [stop_bulk_deployment](#stop_bulk_deployment)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_connectivity_info](#update_connectivity_info)
    - [update_connector_definition](#update_connector_definition)
    - [update_core_definition](#update_core_definition)
    - [update_device_definition](#update_device_definition)
    - [update_function_definition](#update_function_definition)
    - [update_group](#update_group)
    - [update_group_certificate_configuration](#update_group_certificate_configuration)
    - [update_logger_definition](#update_logger_definition)
    - [update_resource_definition](#update_resource_definition)
    - [update_subscription_definition](#update_subscription_definition)
    - [update_thing_runtime_configuration](#update_thing_runtime_configuration)
    - [get_paginator](#get_paginator)

## GreengrassClient

Type annotations for `boto3.client("greengrass")`

Can be used directly:

```python
from mypy_boto3_greengrass.client import GreengrassClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_greengrass.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerErrorException`


## Methods


### associate_role_to_group

Type annotations for `boto3.client("greengrass").associate_role_to_group` method.

[Client.associate_role_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.associate_role_to_group)

```python
def associate_role_to_group(
    self,
    GroupId: str,
    RoleArn: str
) -> AssociateRoleToGroupResponseTypeDef:
    pass
```

### associate_service_role_to_account

Type annotations for `boto3.client("greengrass").associate_service_role_to_account` method.

[Client.associate_service_role_to_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.associate_service_role_to_account)

```python
def associate_service_role_to_account(
    self,
    RoleArn: str
) -> AssociateServiceRoleToAccountResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("greengrass").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_connector_definition

Type annotations for `boto3.client("greengrass").create_connector_definition` method.

[Client.create_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_connector_definition)

```python
def create_connector_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "ConnectorDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateConnectorDefinitionResponseTypeDef:
    pass
```

### create_connector_definition_version

Type annotations for `boto3.client("greengrass").create_connector_definition_version` method.

[Client.create_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_connector_definition_version)

```python
def create_connector_definition_version(
    self,
    ConnectorDefinitionId: str,
    AmznClientToken: str = None,
    Connectors: List["ConnectorTypeDef"] = None
) -> CreateConnectorDefinitionVersionResponseTypeDef:
    pass
```

### create_core_definition

Type annotations for `boto3.client("greengrass").create_core_definition` method.

[Client.create_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_core_definition)

```python
def create_core_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "CoreDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateCoreDefinitionResponseTypeDef:
    pass
```

### create_core_definition_version

Type annotations for `boto3.client("greengrass").create_core_definition_version` method.

[Client.create_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_core_definition_version)

```python
def create_core_definition_version(
    self,
    CoreDefinitionId: str,
    AmznClientToken: str = None,
    Cores: List["CoreTypeDef"] = None
) -> CreateCoreDefinitionVersionResponseTypeDef:
    pass
```

### create_deployment

Type annotations for `boto3.client("greengrass").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_deployment)

```python
def create_deployment(
    self,
    DeploymentType: DeploymentType,
    GroupId: str,
    AmznClientToken: str = None,
    DeploymentId: str = None,
    GroupVersionId: str = None
) -> CreateDeploymentResponseTypeDef:
    pass
```

### create_device_definition

Type annotations for `boto3.client("greengrass").create_device_definition` method.

[Client.create_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_device_definition)

```python
def create_device_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "DeviceDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateDeviceDefinitionResponseTypeDef:
    pass
```

### create_device_definition_version

Type annotations for `boto3.client("greengrass").create_device_definition_version` method.

[Client.create_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_device_definition_version)

```python
def create_device_definition_version(
    self,
    DeviceDefinitionId: str,
    AmznClientToken: str = None,
    Devices: List["DeviceTypeDef"] = None
) -> CreateDeviceDefinitionVersionResponseTypeDef:
    pass
```

### create_function_definition

Type annotations for `boto3.client("greengrass").create_function_definition` method.

[Client.create_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_function_definition)

```python
def create_function_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "FunctionDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateFunctionDefinitionResponseTypeDef:
    pass
```

### create_function_definition_version

Type annotations for `boto3.client("greengrass").create_function_definition_version` method.

[Client.create_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_function_definition_version)

```python
def create_function_definition_version(
    self,
    FunctionDefinitionId: str,
    AmznClientToken: str = None,
    DefaultConfig: "FunctionDefaultConfigTypeDef" = None,
    Functions: List["FunctionTypeDef"] = None
) -> CreateFunctionDefinitionVersionResponseTypeDef:
    pass
```

### create_group

Type annotations for `boto3.client("greengrass").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_group)

```python
def create_group(
    self,
    Name: str,
    AmznClientToken: str = None,
    InitialVersion: "GroupVersionTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateGroupResponseTypeDef:
    pass
```

### create_group_certificate_authority

Type annotations for `boto3.client("greengrass").create_group_certificate_authority` method.

[Client.create_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_group_certificate_authority)

```python
def create_group_certificate_authority(
    self,
    GroupId: str,
    AmznClientToken: str = None
) -> CreateGroupCertificateAuthorityResponseTypeDef:
    pass
```

### create_group_version

Type annotations for `boto3.client("greengrass").create_group_version` method.

[Client.create_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_group_version)

```python
def create_group_version(
    self,
    GroupId: str,
    AmznClientToken: str = None,
    ConnectorDefinitionVersionArn: str = None,
    CoreDefinitionVersionArn: str = None,
    DeviceDefinitionVersionArn: str = None,
    FunctionDefinitionVersionArn: str = None,
    LoggerDefinitionVersionArn: str = None,
    ResourceDefinitionVersionArn: str = None,
    SubscriptionDefinitionVersionArn: str = None
) -> CreateGroupVersionResponseTypeDef:
    pass
```

### create_logger_definition

Type annotations for `boto3.client("greengrass").create_logger_definition` method.

[Client.create_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_logger_definition)

```python
def create_logger_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "LoggerDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateLoggerDefinitionResponseTypeDef:
    pass
```

### create_logger_definition_version

Type annotations for `boto3.client("greengrass").create_logger_definition_version` method.

[Client.create_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_logger_definition_version)

```python
def create_logger_definition_version(
    self,
    LoggerDefinitionId: str,
    AmznClientToken: str = None,
    Loggers: List["LoggerTypeDef"] = None
) -> CreateLoggerDefinitionVersionResponseTypeDef:
    pass
```

### create_resource_definition

Type annotations for `boto3.client("greengrass").create_resource_definition` method.

[Client.create_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_resource_definition)

```python
def create_resource_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "ResourceDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateResourceDefinitionResponseTypeDef:
    pass
```

### create_resource_definition_version

Type annotations for `boto3.client("greengrass").create_resource_definition_version` method.

[Client.create_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_resource_definition_version)

```python
def create_resource_definition_version(
    self,
    ResourceDefinitionId: str,
    AmznClientToken: str = None,
    Resources: List["ResourceTypeDef"] = None
) -> CreateResourceDefinitionVersionResponseTypeDef:
    pass
```

### create_software_update_job

Type annotations for `boto3.client("greengrass").create_software_update_job` method.

[Client.create_software_update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_software_update_job)

```python
def create_software_update_job(
    self,
    S3UrlSignerRole: str,
    SoftwareToUpdate: SoftwareToUpdate,
    UpdateTargets: List[str],
    UpdateTargetsArchitecture: UpdateTargetsArchitecture,
    UpdateTargetsOperatingSystem: UpdateTargetsOperatingSystem,
    AmznClientToken: str = None,
    UpdateAgentLogLevel: UpdateAgentLogLevel = None
) -> CreateSoftwareUpdateJobResponseTypeDef:
    pass
```

### create_subscription_definition

Type annotations for `boto3.client("greengrass").create_subscription_definition` method.

[Client.create_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition)

```python
def create_subscription_definition(
    self,
    AmznClientToken: str = None,
    InitialVersion: "SubscriptionDefinitionVersionTypeDef" = None,
    Name: str = None,
    tags: Dict[str, str] = None
) -> CreateSubscriptionDefinitionResponseTypeDef:
    pass
```

### create_subscription_definition_version

Type annotations for `boto3.client("greengrass").create_subscription_definition_version` method.

[Client.create_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition_version)

```python
def create_subscription_definition_version(
    self,
    SubscriptionDefinitionId: str,
    AmznClientToken: str = None,
    Subscriptions: List["SubscriptionTypeDef"] = None
) -> CreateSubscriptionDefinitionVersionResponseTypeDef:
    pass
```

### delete_connector_definition

Type annotations for `boto3.client("greengrass").delete_connector_definition` method.

[Client.delete_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_connector_definition)

```python
def delete_connector_definition(
    self,
    ConnectorDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### delete_core_definition

Type annotations for `boto3.client("greengrass").delete_core_definition` method.

[Client.delete_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_core_definition)

```python
def delete_core_definition(
    self,
    CoreDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### delete_device_definition

Type annotations for `boto3.client("greengrass").delete_device_definition` method.

[Client.delete_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_device_definition)

```python
def delete_device_definition(
    self,
    DeviceDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### delete_function_definition

Type annotations for `boto3.client("greengrass").delete_function_definition` method.

[Client.delete_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_function_definition)

```python
def delete_function_definition(
    self,
    FunctionDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### delete_group

Type annotations for `boto3.client("greengrass").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_group)

```python
def delete_group(
    self,
    GroupId: str
) -> Dict[str, Any]:
    pass
```

### delete_logger_definition

Type annotations for `boto3.client("greengrass").delete_logger_definition` method.

[Client.delete_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_logger_definition)

```python
def delete_logger_definition(
    self,
    LoggerDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### delete_resource_definition

Type annotations for `boto3.client("greengrass").delete_resource_definition` method.

[Client.delete_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_resource_definition)

```python
def delete_resource_definition(
    self,
    ResourceDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### delete_subscription_definition

Type annotations for `boto3.client("greengrass").delete_subscription_definition` method.

[Client.delete_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.delete_subscription_definition)

```python
def delete_subscription_definition(
    self,
    SubscriptionDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_role_from_group

Type annotations for `boto3.client("greengrass").disassociate_role_from_group` method.

[Client.disassociate_role_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.disassociate_role_from_group)

```python
def disassociate_role_from_group(
    self,
    GroupId: str
) -> DisassociateRoleFromGroupResponseTypeDef:
    pass
```

### disassociate_service_role_from_account

Type annotations for `boto3.client("greengrass").disassociate_service_role_from_account` method.

[Client.disassociate_service_role_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.disassociate_service_role_from_account)

```python
def disassociate_service_role_from_account(
    self
) -> DisassociateServiceRoleFromAccountResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("greengrass").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.generate_presigned_url)

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

### get_associated_role

Type annotations for `boto3.client("greengrass").get_associated_role` method.

[Client.get_associated_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_associated_role)

```python
def get_associated_role(
    self,
    GroupId: str
) -> GetAssociatedRoleResponseTypeDef:
    pass
```

### get_bulk_deployment_status

Type annotations for `boto3.client("greengrass").get_bulk_deployment_status` method.

[Client.get_bulk_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_bulk_deployment_status)

```python
def get_bulk_deployment_status(
    self,
    BulkDeploymentId: str
) -> GetBulkDeploymentStatusResponseTypeDef:
    pass
```

### get_connectivity_info

Type annotations for `boto3.client("greengrass").get_connectivity_info` method.

[Client.get_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_connectivity_info)

```python
def get_connectivity_info(
    self,
    ThingName: str
) -> GetConnectivityInfoResponseTypeDef:
    pass
```

### get_connector_definition

Type annotations for `boto3.client("greengrass").get_connector_definition` method.

[Client.get_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_connector_definition)

```python
def get_connector_definition(
    self,
    ConnectorDefinitionId: str
) -> GetConnectorDefinitionResponseTypeDef:
    pass
```

### get_connector_definition_version

Type annotations for `boto3.client("greengrass").get_connector_definition_version` method.

[Client.get_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_connector_definition_version)

```python
def get_connector_definition_version(
    self,
    ConnectorDefinitionId: str,
    ConnectorDefinitionVersionId: str,
    NextToken: str = None
) -> GetConnectorDefinitionVersionResponseTypeDef:
    pass
```

### get_core_definition

Type annotations for `boto3.client("greengrass").get_core_definition` method.

[Client.get_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_core_definition)

```python
def get_core_definition(
    self,
    CoreDefinitionId: str
) -> GetCoreDefinitionResponseTypeDef:
    pass
```

### get_core_definition_version

Type annotations for `boto3.client("greengrass").get_core_definition_version` method.

[Client.get_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_core_definition_version)

```python
def get_core_definition_version(
    self,
    CoreDefinitionId: str,
    CoreDefinitionVersionId: str
) -> GetCoreDefinitionVersionResponseTypeDef:
    pass
```

### get_deployment_status

Type annotations for `boto3.client("greengrass").get_deployment_status` method.

[Client.get_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_deployment_status)

```python
def get_deployment_status(
    self,
    DeploymentId: str,
    GroupId: str
) -> GetDeploymentStatusResponseTypeDef:
    pass
```

### get_device_definition

Type annotations for `boto3.client("greengrass").get_device_definition` method.

[Client.get_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_device_definition)

```python
def get_device_definition(
    self,
    DeviceDefinitionId: str
) -> GetDeviceDefinitionResponseTypeDef:
    pass
```

### get_device_definition_version

Type annotations for `boto3.client("greengrass").get_device_definition_version` method.

[Client.get_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_device_definition_version)

```python
def get_device_definition_version(
    self,
    DeviceDefinitionId: str,
    DeviceDefinitionVersionId: str,
    NextToken: str = None
) -> GetDeviceDefinitionVersionResponseTypeDef:
    pass
```

### get_function_definition

Type annotations for `boto3.client("greengrass").get_function_definition` method.

[Client.get_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_function_definition)

```python
def get_function_definition(
    self,
    FunctionDefinitionId: str
) -> GetFunctionDefinitionResponseTypeDef:
    pass
```

### get_function_definition_version

Type annotations for `boto3.client("greengrass").get_function_definition_version` method.

[Client.get_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_function_definition_version)

```python
def get_function_definition_version(
    self,
    FunctionDefinitionId: str,
    FunctionDefinitionVersionId: str,
    NextToken: str = None
) -> GetFunctionDefinitionVersionResponseTypeDef:
    pass
```

### get_group

Type annotations for `boto3.client("greengrass").get_group` method.

[Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_group)

```python
def get_group(
    self,
    GroupId: str
) -> GetGroupResponseTypeDef:
    pass
```

### get_group_certificate_authority

Type annotations for `boto3.client("greengrass").get_group_certificate_authority` method.

[Client.get_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_authority)

```python
def get_group_certificate_authority(
    self,
    CertificateAuthorityId: str,
    GroupId: str
) -> GetGroupCertificateAuthorityResponseTypeDef:
    pass
```

### get_group_certificate_configuration

Type annotations for `boto3.client("greengrass").get_group_certificate_configuration` method.

[Client.get_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_configuration)

```python
def get_group_certificate_configuration(
    self,
    GroupId: str
) -> GetGroupCertificateConfigurationResponseTypeDef:
    pass
```

### get_group_version

Type annotations for `boto3.client("greengrass").get_group_version` method.

[Client.get_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_group_version)

```python
def get_group_version(
    self,
    GroupId: str,
    GroupVersionId: str
) -> GetGroupVersionResponseTypeDef:
    pass
```

### get_logger_definition

Type annotations for `boto3.client("greengrass").get_logger_definition` method.

[Client.get_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_logger_definition)

```python
def get_logger_definition(
    self,
    LoggerDefinitionId: str
) -> GetLoggerDefinitionResponseTypeDef:
    pass
```

### get_logger_definition_version

Type annotations for `boto3.client("greengrass").get_logger_definition_version` method.

[Client.get_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_logger_definition_version)

```python
def get_logger_definition_version(
    self,
    LoggerDefinitionId: str,
    LoggerDefinitionVersionId: str,
    NextToken: str = None
) -> GetLoggerDefinitionVersionResponseTypeDef:
    pass
```

### get_resource_definition

Type annotations for `boto3.client("greengrass").get_resource_definition` method.

[Client.get_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_resource_definition)

```python
def get_resource_definition(
    self,
    ResourceDefinitionId: str
) -> GetResourceDefinitionResponseTypeDef:
    pass
```

### get_resource_definition_version

Type annotations for `boto3.client("greengrass").get_resource_definition_version` method.

[Client.get_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_resource_definition_version)

```python
def get_resource_definition_version(
    self,
    ResourceDefinitionId: str,
    ResourceDefinitionVersionId: str
) -> GetResourceDefinitionVersionResponseTypeDef:
    pass
```

### get_service_role_for_account

Type annotations for `boto3.client("greengrass").get_service_role_for_account` method.

[Client.get_service_role_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_service_role_for_account)

```python
def get_service_role_for_account(
    self
) -> GetServiceRoleForAccountResponseTypeDef:
    pass
```

### get_subscription_definition

Type annotations for `boto3.client("greengrass").get_subscription_definition` method.

[Client.get_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition)

```python
def get_subscription_definition(
    self,
    SubscriptionDefinitionId: str
) -> GetSubscriptionDefinitionResponseTypeDef:
    pass
```

### get_subscription_definition_version

Type annotations for `boto3.client("greengrass").get_subscription_definition_version` method.

[Client.get_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition_version)

```python
def get_subscription_definition_version(
    self,
    SubscriptionDefinitionId: str,
    SubscriptionDefinitionVersionId: str,
    NextToken: str = None
) -> GetSubscriptionDefinitionVersionResponseTypeDef:
    pass
```

### get_thing_runtime_configuration

Type annotations for `boto3.client("greengrass").get_thing_runtime_configuration` method.

[Client.get_thing_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_thing_runtime_configuration)

```python
def get_thing_runtime_configuration(
    self,
    ThingName: str
) -> GetThingRuntimeConfigurationResponseTypeDef:
    pass
```

### list_bulk_deployment_detailed_reports

Type annotations for `boto3.client("greengrass").list_bulk_deployment_detailed_reports` method.

[Client.list_bulk_deployment_detailed_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployment_detailed_reports)

```python
def list_bulk_deployment_detailed_reports(
    self,
    BulkDeploymentId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListBulkDeploymentDetailedReportsResponseTypeDef:
    pass
```

### list_bulk_deployments

Type annotations for `boto3.client("greengrass").list_bulk_deployments` method.

[Client.list_bulk_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployments)

```python
def list_bulk_deployments(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListBulkDeploymentsResponseTypeDef:
    pass
```

### list_connector_definition_versions

Type annotations for `boto3.client("greengrass").list_connector_definition_versions` method.

[Client.list_connector_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_connector_definition_versions)

```python
def list_connector_definition_versions(
    self,
    ConnectorDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListConnectorDefinitionVersionsResponseTypeDef:
    pass
```

### list_connector_definitions

Type annotations for `boto3.client("greengrass").list_connector_definitions` method.

[Client.list_connector_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_connector_definitions)

```python
def list_connector_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListConnectorDefinitionsResponseTypeDef:
    pass
```

### list_core_definition_versions

Type annotations for `boto3.client("greengrass").list_core_definition_versions` method.

[Client.list_core_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_core_definition_versions)

```python
def list_core_definition_versions(
    self,
    CoreDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListCoreDefinitionVersionsResponseTypeDef:
    pass
```

### list_core_definitions

Type annotations for `boto3.client("greengrass").list_core_definitions` method.

[Client.list_core_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_core_definitions)

```python
def list_core_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListCoreDefinitionsResponseTypeDef:
    pass
```

### list_deployments

Type annotations for `boto3.client("greengrass").list_deployments` method.

[Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_deployments)

```python
def list_deployments(
    self,
    GroupId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListDeploymentsResponseTypeDef:
    pass
```

### list_device_definition_versions

Type annotations for `boto3.client("greengrass").list_device_definition_versions` method.

[Client.list_device_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_device_definition_versions)

```python
def list_device_definition_versions(
    self,
    DeviceDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListDeviceDefinitionVersionsResponseTypeDef:
    pass
```

### list_device_definitions

Type annotations for `boto3.client("greengrass").list_device_definitions` method.

[Client.list_device_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_device_definitions)

```python
def list_device_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListDeviceDefinitionsResponseTypeDef:
    pass
```

### list_function_definition_versions

Type annotations for `boto3.client("greengrass").list_function_definition_versions` method.

[Client.list_function_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_function_definition_versions)

```python
def list_function_definition_versions(
    self,
    FunctionDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListFunctionDefinitionVersionsResponseTypeDef:
    pass
```

### list_function_definitions

Type annotations for `boto3.client("greengrass").list_function_definitions` method.

[Client.list_function_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_function_definitions)

```python
def list_function_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListFunctionDefinitionsResponseTypeDef:
    pass
```

### list_group_certificate_authorities

Type annotations for `boto3.client("greengrass").list_group_certificate_authorities` method.

[Client.list_group_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_group_certificate_authorities)

```python
def list_group_certificate_authorities(
    self,
    GroupId: str
) -> ListGroupCertificateAuthoritiesResponseTypeDef:
    pass
```

### list_group_versions

Type annotations for `boto3.client("greengrass").list_group_versions` method.

[Client.list_group_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_group_versions)

```python
def list_group_versions(
    self,
    GroupId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListGroupVersionsResponseTypeDef:
    pass
```

### list_groups

Type annotations for `boto3.client("greengrass").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_groups)

```python
def list_groups(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListGroupsResponseTypeDef:
    pass
```

### list_logger_definition_versions

Type annotations for `boto3.client("greengrass").list_logger_definition_versions` method.

[Client.list_logger_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_logger_definition_versions)

```python
def list_logger_definition_versions(
    self,
    LoggerDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListLoggerDefinitionVersionsResponseTypeDef:
    pass
```

### list_logger_definitions

Type annotations for `boto3.client("greengrass").list_logger_definitions` method.

[Client.list_logger_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_logger_definitions)

```python
def list_logger_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListLoggerDefinitionsResponseTypeDef:
    pass
```

### list_resource_definition_versions

Type annotations for `boto3.client("greengrass").list_resource_definition_versions` method.

[Client.list_resource_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_resource_definition_versions)

```python
def list_resource_definition_versions(
    self,
    ResourceDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListResourceDefinitionVersionsResponseTypeDef:
    pass
```

### list_resource_definitions

Type annotations for `boto3.client("greengrass").list_resource_definitions` method.

[Client.list_resource_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_resource_definitions)

```python
def list_resource_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListResourceDefinitionsResponseTypeDef:
    pass
```

### list_subscription_definition_versions

Type annotations for `boto3.client("greengrass").list_subscription_definition_versions` method.

[Client.list_subscription_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_subscription_definition_versions)

```python
def list_subscription_definition_versions(
    self,
    SubscriptionDefinitionId: str,
    MaxResults: str = None,
    NextToken: str = None
) -> ListSubscriptionDefinitionVersionsResponseTypeDef:
    pass
```

### list_subscription_definitions

Type annotations for `boto3.client("greengrass").list_subscription_definitions` method.

[Client.list_subscription_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_subscription_definitions)

```python
def list_subscription_definitions(
    self,
    MaxResults: str = None,
    NextToken: str = None
) -> ListSubscriptionDefinitionsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("greengrass").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### reset_deployments

Type annotations for `boto3.client("greengrass").reset_deployments` method.

[Client.reset_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.reset_deployments)

```python
def reset_deployments(
    self,
    GroupId: str,
    AmznClientToken: str = None,
    Force: bool = None
) -> ResetDeploymentsResponseTypeDef:
    pass
```

### start_bulk_deployment

Type annotations for `boto3.client("greengrass").start_bulk_deployment` method.

[Client.start_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.start_bulk_deployment)

```python
def start_bulk_deployment(
    self,
    ExecutionRoleArn: str,
    InputFileUri: str,
    AmznClientToken: str = None,
    tags: Dict[str, str] = None
) -> StartBulkDeploymentResponseTypeDef:
    pass
```

### stop_bulk_deployment

Type annotations for `boto3.client("greengrass").stop_bulk_deployment` method.

[Client.stop_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.stop_bulk_deployment)

```python
def stop_bulk_deployment(
    self,
    BulkDeploymentId: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("greengrass").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    tags: Dict[str, str] = None
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("greengrass").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_connectivity_info

Type annotations for `boto3.client("greengrass").update_connectivity_info` method.

[Client.update_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_connectivity_info)

```python
def update_connectivity_info(
    self,
    ThingName: str,
    ConnectivityInfo: List["ConnectivityInfoTypeDef"] = None
) -> UpdateConnectivityInfoResponseTypeDef:
    pass
```

### update_connector_definition

Type annotations for `boto3.client("greengrass").update_connector_definition` method.

[Client.update_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_connector_definition)

```python
def update_connector_definition(
    self,
    ConnectorDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_core_definition

Type annotations for `boto3.client("greengrass").update_core_definition` method.

[Client.update_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_core_definition)

```python
def update_core_definition(
    self,
    CoreDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_device_definition

Type annotations for `boto3.client("greengrass").update_device_definition` method.

[Client.update_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_device_definition)

```python
def update_device_definition(
    self,
    DeviceDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_function_definition

Type annotations for `boto3.client("greengrass").update_function_definition` method.

[Client.update_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_function_definition)

```python
def update_function_definition(
    self,
    FunctionDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_group

Type annotations for `boto3.client("greengrass").update_group` method.

[Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_group)

```python
def update_group(
    self,
    GroupId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_group_certificate_configuration

Type annotations for `boto3.client("greengrass").update_group_certificate_configuration` method.

[Client.update_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_group_certificate_configuration)

```python
def update_group_certificate_configuration(
    self,
    GroupId: str,
    CertificateExpiryInMilliseconds: str = None
) -> UpdateGroupCertificateConfigurationResponseTypeDef:
    pass
```

### update_logger_definition

Type annotations for `boto3.client("greengrass").update_logger_definition` method.

[Client.update_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_logger_definition)

```python
def update_logger_definition(
    self,
    LoggerDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_resource_definition

Type annotations for `boto3.client("greengrass").update_resource_definition` method.

[Client.update_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_resource_definition)

```python
def update_resource_definition(
    self,
    ResourceDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_subscription_definition

Type annotations for `boto3.client("greengrass").update_subscription_definition` method.

[Client.update_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_subscription_definition)

```python
def update_subscription_definition(
    self,
    SubscriptionDefinitionId: str,
    Name: str = None
) -> Dict[str, Any]:
    pass
```

### update_thing_runtime_configuration

Type annotations for `boto3.client("greengrass").update_thing_runtime_configuration` method.

[Client.update_thing_runtime_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.update_thing_runtime_configuration)

```python
def update_thing_runtime_configuration(
    self,
    ThingName: str,
    TelemetryConfiguration: TelemetryConfigurationUpdateTypeDef = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("greengrass").get_paginator` method with overloads.

- `client.get_paginator("list_bulk_deployment_detailed_reports")` -> [ListBulkDeploymentDetailedReportsPaginator](./paginators.md#listbulkdeploymentdetailedreportspaginator)
- `client.get_paginator("list_bulk_deployments")` -> [ListBulkDeploymentsPaginator](./paginators.md#listbulkdeploymentspaginator)
- `client.get_paginator("list_connector_definition_versions")` -> [ListConnectorDefinitionVersionsPaginator](./paginators.md#listconnectordefinitionversionspaginator)
- `client.get_paginator("list_connector_definitions")` -> [ListConnectorDefinitionsPaginator](./paginators.md#listconnectordefinitionspaginator)
- `client.get_paginator("list_core_definition_versions")` -> [ListCoreDefinitionVersionsPaginator](./paginators.md#listcoredefinitionversionspaginator)
- `client.get_paginator("list_core_definitions")` -> [ListCoreDefinitionsPaginator](./paginators.md#listcoredefinitionspaginator)
- `client.get_paginator("list_deployments")` -> [ListDeploymentsPaginator](./paginators.md#listdeploymentspaginator)
- `client.get_paginator("list_device_definition_versions")` -> [ListDeviceDefinitionVersionsPaginator](./paginators.md#listdevicedefinitionversionspaginator)
- `client.get_paginator("list_device_definitions")` -> [ListDeviceDefinitionsPaginator](./paginators.md#listdevicedefinitionspaginator)
- `client.get_paginator("list_function_definition_versions")` -> [ListFunctionDefinitionVersionsPaginator](./paginators.md#listfunctiondefinitionversionspaginator)
- `client.get_paginator("list_function_definitions")` -> [ListFunctionDefinitionsPaginator](./paginators.md#listfunctiondefinitionspaginator)
- `client.get_paginator("list_group_versions")` -> [ListGroupVersionsPaginator](./paginators.md#listgroupversionspaginator)
- `client.get_paginator("list_groups")` -> [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- `client.get_paginator("list_logger_definition_versions")` -> [ListLoggerDefinitionVersionsPaginator](./paginators.md#listloggerdefinitionversionspaginator)
- `client.get_paginator("list_logger_definitions")` -> [ListLoggerDefinitionsPaginator](./paginators.md#listloggerdefinitionspaginator)
- `client.get_paginator("list_resource_definition_versions")` -> [ListResourceDefinitionVersionsPaginator](./paginators.md#listresourcedefinitionversionspaginator)
- `client.get_paginator("list_resource_definitions")` -> [ListResourceDefinitionsPaginator](./paginators.md#listresourcedefinitionspaginator)
- `client.get_paginator("list_subscription_definition_versions")` -> [ListSubscriptionDefinitionVersionsPaginator](./paginators.md#listsubscriptiondefinitionversionspaginator)
- `client.get_paginator("list_subscription_definitions")` -> [ListSubscriptionDefinitionsPaginator](./paginators.md#listsubscriptiondefinitionspaginator)


