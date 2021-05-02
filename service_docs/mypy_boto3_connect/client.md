# ConnectClient for boto3 Connect module

> [Index](../index.md) > [Connect](./index.md) > ConnectClient

Auto-generated documentation for [Connect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect)
type annotations stubs module [mypy_boto3_connect](https://pypi.org/project/mypy-boto3-connect/).

- [ConnectClient for boto3 Connect module](#connectclient-for-boto3-connect-module)
  - [ConnectClient](#connectclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_approved_origin](#associate_approved_origin)
    - [associate_instance_storage_config](#associate_instance_storage_config)
    - [associate_lambda_function](#associate_lambda_function)
    - [associate_lex_bot](#associate_lex_bot)
    - [associate_queue_quick_connects](#associate_queue_quick_connects)
    - [associate_routing_profile_queues](#associate_routing_profile_queues)
    - [associate_security_key](#associate_security_key)
    - [can_paginate](#can_paginate)
    - [create_contact_flow](#create_contact_flow)
    - [create_instance](#create_instance)
    - [create_integration_association](#create_integration_association)
    - [create_queue](#create_queue)
    - [create_quick_connect](#create_quick_connect)
    - [create_routing_profile](#create_routing_profile)
    - [create_use_case](#create_use_case)
    - [create_user](#create_user)
    - [create_user_hierarchy_group](#create_user_hierarchy_group)
    - [delete_instance](#delete_instance)
    - [delete_integration_association](#delete_integration_association)
    - [delete_quick_connect](#delete_quick_connect)
    - [delete_use_case](#delete_use_case)
    - [delete_user](#delete_user)
    - [delete_user_hierarchy_group](#delete_user_hierarchy_group)
    - [describe_contact_flow](#describe_contact_flow)
    - [describe_hours_of_operation](#describe_hours_of_operation)
    - [describe_instance](#describe_instance)
    - [describe_instance_attribute](#describe_instance_attribute)
    - [describe_instance_storage_config](#describe_instance_storage_config)
    - [describe_queue](#describe_queue)
    - [describe_quick_connect](#describe_quick_connect)
    - [describe_routing_profile](#describe_routing_profile)
    - [describe_user](#describe_user)
    - [describe_user_hierarchy_group](#describe_user_hierarchy_group)
    - [describe_user_hierarchy_structure](#describe_user_hierarchy_structure)
    - [disassociate_approved_origin](#disassociate_approved_origin)
    - [disassociate_instance_storage_config](#disassociate_instance_storage_config)
    - [disassociate_lambda_function](#disassociate_lambda_function)
    - [disassociate_lex_bot](#disassociate_lex_bot)
    - [disassociate_queue_quick_connects](#disassociate_queue_quick_connects)
    - [disassociate_routing_profile_queues](#disassociate_routing_profile_queues)
    - [disassociate_security_key](#disassociate_security_key)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_contact_attributes](#get_contact_attributes)
    - [get_current_metric_data](#get_current_metric_data)
    - [get_federation_token](#get_federation_token)
    - [get_metric_data](#get_metric_data)
    - [list_approved_origins](#list_approved_origins)
    - [list_contact_flows](#list_contact_flows)
    - [list_hours_of_operations](#list_hours_of_operations)
    - [list_instance_attributes](#list_instance_attributes)
    - [list_instance_storage_configs](#list_instance_storage_configs)
    - [list_instances](#list_instances)
    - [list_integration_associations](#list_integration_associations)
    - [list_lambda_functions](#list_lambda_functions)
    - [list_lex_bots](#list_lex_bots)
    - [list_phone_numbers](#list_phone_numbers)
    - [list_prompts](#list_prompts)
    - [list_queue_quick_connects](#list_queue_quick_connects)
    - [list_queues](#list_queues)
    - [list_quick_connects](#list_quick_connects)
    - [list_routing_profile_queues](#list_routing_profile_queues)
    - [list_routing_profiles](#list_routing_profiles)
    - [list_security_keys](#list_security_keys)
    - [list_security_profiles](#list_security_profiles)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_use_cases](#list_use_cases)
    - [list_user_hierarchy_groups](#list_user_hierarchy_groups)
    - [list_users](#list_users)
    - [resume_contact_recording](#resume_contact_recording)
    - [start_chat_contact](#start_chat_contact)
    - [start_contact_recording](#start_contact_recording)
    - [start_outbound_voice_contact](#start_outbound_voice_contact)
    - [start_task_contact](#start_task_contact)
    - [stop_contact](#stop_contact)
    - [stop_contact_recording](#stop_contact_recording)
    - [suspend_contact_recording](#suspend_contact_recording)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_contact_attributes](#update_contact_attributes)
    - [update_contact_flow_content](#update_contact_flow_content)
    - [update_contact_flow_name](#update_contact_flow_name)
    - [update_instance_attribute](#update_instance_attribute)
    - [update_instance_storage_config](#update_instance_storage_config)
    - [update_queue_hours_of_operation](#update_queue_hours_of_operation)
    - [update_queue_max_contacts](#update_queue_max_contacts)
    - [update_queue_name](#update_queue_name)
    - [update_queue_outbound_caller_config](#update_queue_outbound_caller_config)
    - [update_queue_status](#update_queue_status)
    - [update_quick_connect_config](#update_quick_connect_config)
    - [update_quick_connect_name](#update_quick_connect_name)
    - [update_routing_profile_concurrency](#update_routing_profile_concurrency)
    - [update_routing_profile_default_outbound_queue](#update_routing_profile_default_outbound_queue)
    - [update_routing_profile_name](#update_routing_profile_name)
    - [update_routing_profile_queues](#update_routing_profile_queues)
    - [update_user_hierarchy](#update_user_hierarchy)
    - [update_user_hierarchy_group_name](#update_user_hierarchy_group_name)
    - [update_user_hierarchy_structure](#update_user_hierarchy_structure)
    - [update_user_identity_info](#update_user_identity_info)
    - [update_user_phone_config](#update_user_phone_config)
    - [update_user_routing_profile](#update_user_routing_profile)
    - [update_user_security_profiles](#update_user_security_profiles)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)
    - [get_paginator](#get_paginator-19)
    - [get_paginator](#get_paginator-20)
    - [get_paginator](#get_paginator-21)

## ConnectClient

Type annotations for `boto3.client("connect")`

Can be used directly:

```python
from mypy_boto3_connect.client import ConnectClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_connect.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ContactFlowNotPublishedException`
- `Exceptions.ContactNotFoundException`
- `Exceptions.DestinationNotAllowedException`
- `Exceptions.DuplicateResourceException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidContactFlowException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.OutboundContactNotPermittedException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.UserNotFoundException`


## Methods


### associate_approved_origin

Type annotations for `boto3.client("connect").associate_approved_origin` method.

[Client.associate_approved_origin documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_approved_origin)

```python
def associate_approved_origin(
    self,
    InstanceId: str,
    Origin: str
) -> None:
    pass
```

### associate_instance_storage_config

Type annotations for `boto3.client("connect").associate_instance_storage_config` method.

[Client.associate_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_instance_storage_config)

```python
def associate_instance_storage_config(
    self,
    InstanceId: str,
    ResourceType: InstanceStorageResourceType,
    StorageConfig: "InstanceStorageConfigTypeDef"
) -> AssociateInstanceStorageConfigResponseTypeDef:
    pass
```

### associate_lambda_function

Type annotations for `boto3.client("connect").associate_lambda_function` method.

[Client.associate_lambda_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_lambda_function)

```python
def associate_lambda_function(
    self,
    InstanceId: str,
    FunctionArn: str
) -> None:
    pass
```

### associate_lex_bot

Type annotations for `boto3.client("connect").associate_lex_bot` method.

[Client.associate_lex_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_lex_bot)

```python
def associate_lex_bot(
    self,
    InstanceId: str,
    LexBot: "LexBotTypeDef"
) -> None:
    pass
```

### associate_queue_quick_connects

Type annotations for `boto3.client("connect").associate_queue_quick_connects` method.

[Client.associate_queue_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_queue_quick_connects)

```python
def associate_queue_quick_connects(
    self,
    InstanceId: str,
    QueueId: str,
    QuickConnectIds: List[str]
) -> None:
    pass
```

### associate_routing_profile_queues

Type annotations for `boto3.client("connect").associate_routing_profile_queues` method.

[Client.associate_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_routing_profile_queues)

```python
def associate_routing_profile_queues(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    QueueConfigs: List[RoutingProfileQueueConfigTypeDef]
) -> None:
    pass
```

### associate_security_key

Type annotations for `boto3.client("connect").associate_security_key` method.

[Client.associate_security_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_security_key)

```python
def associate_security_key(
    self,
    InstanceId: str,
    Key: str
) -> AssociateSecurityKeyResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("connect").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_contact_flow

Type annotations for `boto3.client("connect").create_contact_flow` method.

[Client.create_contact_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_contact_flow)

```python
def create_contact_flow(
    self,
    InstanceId: str,
    Name: str,
    Type: ContactFlowType,
    Content: str,
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateContactFlowResponseTypeDef:
    pass
```

### create_instance

Type annotations for `boto3.client("connect").create_instance` method.

[Client.create_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_instance)

```python
def create_instance(
    self,
    IdentityManagementType: DirectoryType,
    InboundCallsEnabled: bool,
    OutboundCallsEnabled: bool,
    ClientToken: str = None,
    InstanceAlias: str = None,
    DirectoryId: str = None
) -> CreateInstanceResponseTypeDef:
    pass
```

### create_integration_association

Type annotations for `boto3.client("connect").create_integration_association` method.

[Client.create_integration_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_integration_association)

```python
def create_integration_association(
    self,
    InstanceId: str,
    IntegrationType: IntegrationType,
    IntegrationArn: str,
    SourceApplicationUrl: str,
    SourceApplicationName: str,
    SourceType: SourceType
) -> CreateIntegrationAssociationResponseTypeDef:
    pass
```

### create_queue

Type annotations for `boto3.client("connect").create_queue` method.

[Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_queue)

```python
def create_queue(
    self,
    InstanceId: str,
    Name: str,
    HoursOfOperationId: str,
    Description: str = None,
    OutboundCallerConfig: "OutboundCallerConfigTypeDef" = None,
    MaxContacts: int = None,
    QuickConnectIds: List[str] = None,
    Tags: Dict[str, str] = None
) -> CreateQueueResponseTypeDef:
    pass
```

### create_quick_connect

Type annotations for `boto3.client("connect").create_quick_connect` method.

[Client.create_quick_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_quick_connect)

```python
def create_quick_connect(
    self,
    InstanceId: str,
    Name: str,
    QuickConnectConfig: "QuickConnectConfigTypeDef",
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateQuickConnectResponseTypeDef:
    pass
```

### create_routing_profile

Type annotations for `boto3.client("connect").create_routing_profile` method.

[Client.create_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_routing_profile)

```python
def create_routing_profile(
    self,
    InstanceId: str,
    Name: str,
    Description: str,
    DefaultOutboundQueueId: str,
    MediaConcurrencies: List["MediaConcurrencyTypeDef"],
    QueueConfigs: List[RoutingProfileQueueConfigTypeDef] = None,
    Tags: Dict[str, str] = None
) -> CreateRoutingProfileResponseTypeDef:
    pass
```

### create_use_case

Type annotations for `boto3.client("connect").create_use_case` method.

[Client.create_use_case documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_use_case)

```python
def create_use_case(
    self,
    InstanceId: str,
    IntegrationAssociationId: str,
    UseCaseType: UseCaseType
) -> CreateUseCaseResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("connect").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_user)

```python
def create_user(
    self,
    Username: str,
    PhoneConfig: "UserPhoneConfigTypeDef",
    SecurityProfileIds: List[str],
    RoutingProfileId: str,
    InstanceId: str,
    Password: str = None,
    IdentityInfo: "UserIdentityInfoTypeDef" = None,
    DirectoryUserId: str = None,
    HierarchyGroupId: str = None,
    Tags: Dict[str, str] = None
) -> CreateUserResponseTypeDef:
    pass
```

### create_user_hierarchy_group

Type annotations for `boto3.client("connect").create_user_hierarchy_group` method.

[Client.create_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_user_hierarchy_group)

```python
def create_user_hierarchy_group(
    self,
    Name: str,
    InstanceId: str,
    ParentGroupId: str = None
) -> CreateUserHierarchyGroupResponseTypeDef:
    pass
```

### delete_instance

Type annotations for `boto3.client("connect").delete_instance` method.

[Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_instance)

```python
def delete_instance(
    self,
    InstanceId: str
) -> None:
    pass
```

### delete_integration_association

Type annotations for `boto3.client("connect").delete_integration_association` method.

[Client.delete_integration_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_integration_association)

```python
def delete_integration_association(
    self,
    InstanceId: str,
    IntegrationAssociationId: str
) -> None:
    pass
```

### delete_quick_connect

Type annotations for `boto3.client("connect").delete_quick_connect` method.

[Client.delete_quick_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_quick_connect)

```python
def delete_quick_connect(
    self,
    InstanceId: str,
    QuickConnectId: str
) -> None:
    pass
```

### delete_use_case

Type annotations for `boto3.client("connect").delete_use_case` method.

[Client.delete_use_case documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_use_case)

```python
def delete_use_case(
    self,
    InstanceId: str,
    IntegrationAssociationId: str,
    UseCaseId: str
) -> None:
    pass
```

### delete_user

Type annotations for `boto3.client("connect").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_user)

```python
def delete_user(
    self,
    InstanceId: str,
    UserId: str
) -> None:
    pass
```

### delete_user_hierarchy_group

Type annotations for `boto3.client("connect").delete_user_hierarchy_group` method.

[Client.delete_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_user_hierarchy_group)

```python
def delete_user_hierarchy_group(
    self,
    HierarchyGroupId: str,
    InstanceId: str
) -> None:
    pass
```

### describe_contact_flow

Type annotations for `boto3.client("connect").describe_contact_flow` method.

[Client.describe_contact_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_contact_flow)

```python
def describe_contact_flow(
    self,
    InstanceId: str,
    ContactFlowId: str
) -> DescribeContactFlowResponseTypeDef:
    pass
```

### describe_hours_of_operation

Type annotations for `boto3.client("connect").describe_hours_of_operation` method.

[Client.describe_hours_of_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_hours_of_operation)

```python
def describe_hours_of_operation(
    self,
    InstanceId: str,
    HoursOfOperationId: str
) -> DescribeHoursOfOperationResponseTypeDef:
    pass
```

### describe_instance

Type annotations for `boto3.client("connect").describe_instance` method.

[Client.describe_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_instance)

```python
def describe_instance(
    self,
    InstanceId: str
) -> DescribeInstanceResponseTypeDef:
    pass
```

### describe_instance_attribute

Type annotations for `boto3.client("connect").describe_instance_attribute` method.

[Client.describe_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_instance_attribute)

```python
def describe_instance_attribute(
    self,
    InstanceId: str,
    AttributeType: InstanceAttributeType
) -> DescribeInstanceAttributeResponseTypeDef:
    pass
```

### describe_instance_storage_config

Type annotations for `boto3.client("connect").describe_instance_storage_config` method.

[Client.describe_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_instance_storage_config)

```python
def describe_instance_storage_config(
    self,
    InstanceId: str,
    AssociationId: str,
    ResourceType: InstanceStorageResourceType
) -> DescribeInstanceStorageConfigResponseTypeDef:
    pass
```

### describe_queue

Type annotations for `boto3.client("connect").describe_queue` method.

[Client.describe_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_queue)

```python
def describe_queue(
    self,
    InstanceId: str,
    QueueId: str
) -> DescribeQueueResponseTypeDef:
    pass
```

### describe_quick_connect

Type annotations for `boto3.client("connect").describe_quick_connect` method.

[Client.describe_quick_connect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_quick_connect)

```python
def describe_quick_connect(
    self,
    InstanceId: str,
    QuickConnectId: str
) -> DescribeQuickConnectResponseTypeDef:
    pass
```

### describe_routing_profile

Type annotations for `boto3.client("connect").describe_routing_profile` method.

[Client.describe_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_routing_profile)

```python
def describe_routing_profile(
    self,
    InstanceId: str,
    RoutingProfileId: str
) -> DescribeRoutingProfileResponseTypeDef:
    pass
```

### describe_user

Type annotations for `boto3.client("connect").describe_user` method.

[Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_user)

```python
def describe_user(
    self,
    UserId: str,
    InstanceId: str
) -> DescribeUserResponseTypeDef:
    pass
```

### describe_user_hierarchy_group

Type annotations for `boto3.client("connect").describe_user_hierarchy_group` method.

[Client.describe_user_hierarchy_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_user_hierarchy_group)

```python
def describe_user_hierarchy_group(
    self,
    HierarchyGroupId: str,
    InstanceId: str
) -> DescribeUserHierarchyGroupResponseTypeDef:
    pass
```

### describe_user_hierarchy_structure

Type annotations for `boto3.client("connect").describe_user_hierarchy_structure` method.

[Client.describe_user_hierarchy_structure documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_user_hierarchy_structure)

```python
def describe_user_hierarchy_structure(
    self,
    InstanceId: str
) -> DescribeUserHierarchyStructureResponseTypeDef:
    pass
```

### disassociate_approved_origin

Type annotations for `boto3.client("connect").disassociate_approved_origin` method.

[Client.disassociate_approved_origin documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_approved_origin)

```python
def disassociate_approved_origin(
    self,
    InstanceId: str,
    Origin: str
) -> None:
    pass
```

### disassociate_instance_storage_config

Type annotations for `boto3.client("connect").disassociate_instance_storage_config` method.

[Client.disassociate_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_instance_storage_config)

```python
def disassociate_instance_storage_config(
    self,
    InstanceId: str,
    AssociationId: str,
    ResourceType: InstanceStorageResourceType
) -> None:
    pass
```

### disassociate_lambda_function

Type annotations for `boto3.client("connect").disassociate_lambda_function` method.

[Client.disassociate_lambda_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_lambda_function)

```python
def disassociate_lambda_function(
    self,
    InstanceId: str,
    FunctionArn: str
) -> None:
    pass
```

### disassociate_lex_bot

Type annotations for `boto3.client("connect").disassociate_lex_bot` method.

[Client.disassociate_lex_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_lex_bot)

```python
def disassociate_lex_bot(
    self,
    InstanceId: str,
    BotName: str,
    LexRegion: str
) -> None:
    pass
```

### disassociate_queue_quick_connects

Type annotations for `boto3.client("connect").disassociate_queue_quick_connects` method.

[Client.disassociate_queue_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_queue_quick_connects)

```python
def disassociate_queue_quick_connects(
    self,
    InstanceId: str,
    QueueId: str,
    QuickConnectIds: List[str]
) -> None:
    pass
```

### disassociate_routing_profile_queues

Type annotations for `boto3.client("connect").disassociate_routing_profile_queues` method.

[Client.disassociate_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_routing_profile_queues)

```python
def disassociate_routing_profile_queues(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    QueueReferences: List["RoutingProfileQueueReferenceTypeDef"]
) -> None:
    pass
```

### disassociate_security_key

Type annotations for `boto3.client("connect").disassociate_security_key` method.

[Client.disassociate_security_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_security_key)

```python
def disassociate_security_key(
    self,
    InstanceId: str,
    AssociationId: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("connect").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.generate_presigned_url)

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

### get_contact_attributes

Type annotations for `boto3.client("connect").get_contact_attributes` method.

[Client.get_contact_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_contact_attributes)

```python
def get_contact_attributes(
    self,
    InstanceId: str,
    InitialContactId: str
) -> GetContactAttributesResponseTypeDef:
    pass
```

### get_current_metric_data

Type annotations for `boto3.client("connect").get_current_metric_data` method.

[Client.get_current_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_current_metric_data)

```python
def get_current_metric_data(
    self,
    InstanceId: str,
    Filters: FiltersTypeDef,
    CurrentMetrics: List["CurrentMetricTypeDef"],
    Groupings: List[Grouping] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetCurrentMetricDataResponseTypeDef:
    pass
```

### get_federation_token

Type annotations for `boto3.client("connect").get_federation_token` method.

[Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_federation_token)

```python
def get_federation_token(
    self,
    InstanceId: str
) -> GetFederationTokenResponseTypeDef:
    pass
```

### get_metric_data

Type annotations for `boto3.client("connect").get_metric_data` method.

[Client.get_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_metric_data)

```python
def get_metric_data(
    self,
    InstanceId: str,
    StartTime: datetime,
    EndTime: datetime,
    Filters: FiltersTypeDef,
    HistoricalMetrics: List["HistoricalMetricTypeDef"],
    Groupings: List[Grouping] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetMetricDataResponseTypeDef:
    pass
```

### list_approved_origins

Type annotations for `boto3.client("connect").list_approved_origins` method.

[Client.list_approved_origins documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_approved_origins)

```python
def list_approved_origins(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListApprovedOriginsResponseTypeDef:
    pass
```

### list_contact_flows

Type annotations for `boto3.client("connect").list_contact_flows` method.

[Client.list_contact_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_contact_flows)

```python
def list_contact_flows(
    self,
    InstanceId: str,
    ContactFlowTypes: List[ContactFlowType] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListContactFlowsResponseTypeDef:
    pass
```

### list_hours_of_operations

Type annotations for `boto3.client("connect").list_hours_of_operations` method.

[Client.list_hours_of_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_hours_of_operations)

```python
def list_hours_of_operations(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHoursOfOperationsResponseTypeDef:
    pass
```

### list_instance_attributes

Type annotations for `boto3.client("connect").list_instance_attributes` method.

[Client.list_instance_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_instance_attributes)

```python
def list_instance_attributes(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListInstanceAttributesResponseTypeDef:
    pass
```

### list_instance_storage_configs

Type annotations for `boto3.client("connect").list_instance_storage_configs` method.

[Client.list_instance_storage_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_instance_storage_configs)

```python
def list_instance_storage_configs(
    self,
    InstanceId: str,
    ResourceType: InstanceStorageResourceType,
    NextToken: str = None,
    MaxResults: int = None
) -> ListInstanceStorageConfigsResponseTypeDef:
    pass
```

### list_instances

Type annotations for `boto3.client("connect").list_instances` method.

[Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_instances)

```python
def list_instances(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListInstancesResponseTypeDef:
    pass
```

### list_integration_associations

Type annotations for `boto3.client("connect").list_integration_associations` method.

[Client.list_integration_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_integration_associations)

```python
def list_integration_associations(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIntegrationAssociationsResponseTypeDef:
    pass
```

### list_lambda_functions

Type annotations for `boto3.client("connect").list_lambda_functions` method.

[Client.list_lambda_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_lambda_functions)

```python
def list_lambda_functions(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLambdaFunctionsResponseTypeDef:
    pass
```

### list_lex_bots

Type annotations for `boto3.client("connect").list_lex_bots` method.

[Client.list_lex_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_lex_bots)

```python
def list_lex_bots(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLexBotsResponseTypeDef:
    pass
```

### list_phone_numbers

Type annotations for `boto3.client("connect").list_phone_numbers` method.

[Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_phone_numbers)

```python
def list_phone_numbers(
    self,
    InstanceId: str,
    PhoneNumberTypes: List[PhoneNumberType] = None,
    PhoneNumberCountryCodes: List[PhoneNumberCountryCode] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPhoneNumbersResponseTypeDef:
    pass
```

### list_prompts

Type annotations for `boto3.client("connect").list_prompts` method.

[Client.list_prompts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_prompts)

```python
def list_prompts(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPromptsResponseTypeDef:
    pass
```

### list_queue_quick_connects

Type annotations for `boto3.client("connect").list_queue_quick_connects` method.

[Client.list_queue_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_queue_quick_connects)

```python
def list_queue_quick_connects(
    self,
    InstanceId: str,
    QueueId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListQueueQuickConnectsResponseTypeDef:
    pass
```

### list_queues

Type annotations for `boto3.client("connect").list_queues` method.

[Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_queues)

```python
def list_queues(
    self,
    InstanceId: str,
    QueueTypes: List[QueueType] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListQueuesResponseTypeDef:
    pass
```

### list_quick_connects

Type annotations for `boto3.client("connect").list_quick_connects` method.

[Client.list_quick_connects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_quick_connects)

```python
def list_quick_connects(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None,
    QuickConnectTypes: List[QuickConnectType] = None
) -> ListQuickConnectsResponseTypeDef:
    pass
```

### list_routing_profile_queues

Type annotations for `boto3.client("connect").list_routing_profile_queues` method.

[Client.list_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_routing_profile_queues)

```python
def list_routing_profile_queues(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRoutingProfileQueuesResponseTypeDef:
    pass
```

### list_routing_profiles

Type annotations for `boto3.client("connect").list_routing_profiles` method.

[Client.list_routing_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_routing_profiles)

```python
def list_routing_profiles(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRoutingProfilesResponseTypeDef:
    pass
```

### list_security_keys

Type annotations for `boto3.client("connect").list_security_keys` method.

[Client.list_security_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_security_keys)

```python
def list_security_keys(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSecurityKeysResponseTypeDef:
    pass
```

### list_security_profiles

Type annotations for `boto3.client("connect").list_security_profiles` method.

[Client.list_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_security_profiles)

```python
def list_security_profiles(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSecurityProfilesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("connect").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_use_cases

Type annotations for `boto3.client("connect").list_use_cases` method.

[Client.list_use_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_use_cases)

```python
def list_use_cases(
    self,
    InstanceId: str,
    IntegrationAssociationId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListUseCasesResponseTypeDef:
    pass
```

### list_user_hierarchy_groups

Type annotations for `boto3.client("connect").list_user_hierarchy_groups` method.

[Client.list_user_hierarchy_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_user_hierarchy_groups)

```python
def list_user_hierarchy_groups(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListUserHierarchyGroupsResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("connect").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_users)

```python
def list_users(
    self,
    InstanceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListUsersResponseTypeDef:
    pass
```

### resume_contact_recording

Type annotations for `boto3.client("connect").resume_contact_recording` method.

[Client.resume_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.resume_contact_recording)

```python
def resume_contact_recording(
    self,
    InstanceId: str,
    ContactId: str,
    InitialContactId: str
) -> Dict[str, Any]:
    pass
```

### start_chat_contact

Type annotations for `boto3.client("connect").start_chat_contact` method.

[Client.start_chat_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_chat_contact)

```python
def start_chat_contact(
    self,
    InstanceId: str,
    ContactFlowId: str,
    ParticipantDetails: ParticipantDetailsTypeDef,
    Attributes: Dict[str, str] = None,
    InitialMessage: ChatMessageTypeDef = None,
    ClientToken: str = None
) -> StartChatContactResponseTypeDef:
    pass
```

### start_contact_recording

Type annotations for `boto3.client("connect").start_contact_recording` method.

[Client.start_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_contact_recording)

```python
def start_contact_recording(
    self,
    InstanceId: str,
    ContactId: str,
    InitialContactId: str,
    VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef
) -> Dict[str, Any]:
    pass
```

### start_outbound_voice_contact

Type annotations for `boto3.client("connect").start_outbound_voice_contact` method.

[Client.start_outbound_voice_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_outbound_voice_contact)

```python
def start_outbound_voice_contact(
    self,
    DestinationPhoneNumber: str,
    ContactFlowId: str,
    InstanceId: str,
    ClientToken: str = None,
    SourcePhoneNumber: str = None,
    QueueId: str = None,
    Attributes: Dict[str, str] = None
) -> StartOutboundVoiceContactResponseTypeDef:
    pass
```

### start_task_contact

Type annotations for `boto3.client("connect").start_task_contact` method.

[Client.start_task_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_task_contact)

```python
def start_task_contact(
    self,
    InstanceId: str,
    ContactFlowId: str,
    Name: str,
    PreviousContactId: str = None,
    Attributes: Dict[str, str] = None,
    References: Dict[str, ReferenceTypeDef] = None,
    Description: str = None,
    ClientToken: str = None
) -> StartTaskContactResponseTypeDef:
    pass
```

### stop_contact

Type annotations for `boto3.client("connect").stop_contact` method.

[Client.stop_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.stop_contact)

```python
def stop_contact(
    self,
    ContactId: str,
    InstanceId: str
) -> Dict[str, Any]:
    pass
```

### stop_contact_recording

Type annotations for `boto3.client("connect").stop_contact_recording` method.

[Client.stop_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.stop_contact_recording)

```python
def stop_contact_recording(
    self,
    InstanceId: str,
    ContactId: str,
    InitialContactId: str
) -> Dict[str, Any]:
    pass
```

### suspend_contact_recording

Type annotations for `boto3.client("connect").suspend_contact_recording` method.

[Client.suspend_contact_recording documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.suspend_contact_recording)

```python
def suspend_contact_recording(
    self,
    InstanceId: str,
    ContactId: str,
    InitialContactId: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("connect").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("connect").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> None:
    pass
```

### update_contact_attributes

Type annotations for `boto3.client("connect").update_contact_attributes` method.

[Client.update_contact_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_attributes)

```python
def update_contact_attributes(
    self,
    InitialContactId: str,
    InstanceId: str,
    Attributes: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### update_contact_flow_content

Type annotations for `boto3.client("connect").update_contact_flow_content` method.

[Client.update_contact_flow_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_content)

```python
def update_contact_flow_content(
    self,
    InstanceId: str,
    ContactFlowId: str,
    Content: str
) -> None:
    pass
```

### update_contact_flow_name

Type annotations for `boto3.client("connect").update_contact_flow_name` method.

[Client.update_contact_flow_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_name)

```python
def update_contact_flow_name(
    self,
    InstanceId: str,
    ContactFlowId: str,
    Name: str = None,
    Description: str = None
) -> None:
    pass
```

### update_instance_attribute

Type annotations for `boto3.client("connect").update_instance_attribute` method.

[Client.update_instance_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_instance_attribute)

```python
def update_instance_attribute(
    self,
    InstanceId: str,
    AttributeType: InstanceAttributeType,
    Value: str
) -> None:
    pass
```

### update_instance_storage_config

Type annotations for `boto3.client("connect").update_instance_storage_config` method.

[Client.update_instance_storage_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_instance_storage_config)

```python
def update_instance_storage_config(
    self,
    InstanceId: str,
    AssociationId: str,
    ResourceType: InstanceStorageResourceType,
    StorageConfig: "InstanceStorageConfigTypeDef"
) -> None:
    pass
```

### update_queue_hours_of_operation

Type annotations for `boto3.client("connect").update_queue_hours_of_operation` method.

[Client.update_queue_hours_of_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_hours_of_operation)

```python
def update_queue_hours_of_operation(
    self,
    InstanceId: str,
    QueueId: str,
    HoursOfOperationId: str
) -> None:
    pass
```

### update_queue_max_contacts

Type annotations for `boto3.client("connect").update_queue_max_contacts` method.

[Client.update_queue_max_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_max_contacts)

```python
def update_queue_max_contacts(
    self,
    InstanceId: str,
    QueueId: str,
    MaxContacts: int = None
) -> None:
    pass
```

### update_queue_name

Type annotations for `boto3.client("connect").update_queue_name` method.

[Client.update_queue_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_name)

```python
def update_queue_name(
    self,
    InstanceId: str,
    QueueId: str,
    Name: str = None,
    Description: str = None
) -> None:
    pass
```

### update_queue_outbound_caller_config

Type annotations for `boto3.client("connect").update_queue_outbound_caller_config` method.

[Client.update_queue_outbound_caller_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_outbound_caller_config)

```python
def update_queue_outbound_caller_config(
    self,
    InstanceId: str,
    QueueId: str,
    OutboundCallerConfig: "OutboundCallerConfigTypeDef"
) -> None:
    pass
```

### update_queue_status

Type annotations for `boto3.client("connect").update_queue_status` method.

[Client.update_queue_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_status)

```python
def update_queue_status(
    self,
    InstanceId: str,
    QueueId: str,
    Status: QueueStatus
) -> None:
    pass
```

### update_quick_connect_config

Type annotations for `boto3.client("connect").update_quick_connect_config` method.

[Client.update_quick_connect_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_quick_connect_config)

```python
def update_quick_connect_config(
    self,
    InstanceId: str,
    QuickConnectId: str,
    QuickConnectConfig: "QuickConnectConfigTypeDef"
) -> None:
    pass
```

### update_quick_connect_name

Type annotations for `boto3.client("connect").update_quick_connect_name` method.

[Client.update_quick_connect_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_quick_connect_name)

```python
def update_quick_connect_name(
    self,
    InstanceId: str,
    QuickConnectId: str,
    Name: str = None,
    Description: str = None
) -> None:
    pass
```

### update_routing_profile_concurrency

Type annotations for `boto3.client("connect").update_routing_profile_concurrency` method.

[Client.update_routing_profile_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_concurrency)

```python
def update_routing_profile_concurrency(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    MediaConcurrencies: List["MediaConcurrencyTypeDef"]
) -> None:
    pass
```

### update_routing_profile_default_outbound_queue

Type annotations for `boto3.client("connect").update_routing_profile_default_outbound_queue` method.

[Client.update_routing_profile_default_outbound_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_default_outbound_queue)

```python
def update_routing_profile_default_outbound_queue(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    DefaultOutboundQueueId: str
) -> None:
    pass
```

### update_routing_profile_name

Type annotations for `boto3.client("connect").update_routing_profile_name` method.

[Client.update_routing_profile_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_name)

```python
def update_routing_profile_name(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    Name: str = None,
    Description: str = None
) -> None:
    pass
```

### update_routing_profile_queues

Type annotations for `boto3.client("connect").update_routing_profile_queues` method.

[Client.update_routing_profile_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_queues)

```python
def update_routing_profile_queues(
    self,
    InstanceId: str,
    RoutingProfileId: str,
    QueueConfigs: List[RoutingProfileQueueConfigTypeDef]
) -> None:
    pass
```

### update_user_hierarchy

Type annotations for `boto3.client("connect").update_user_hierarchy` method.

[Client.update_user_hierarchy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_hierarchy)

```python
def update_user_hierarchy(
    self,
    UserId: str,
    InstanceId: str,
    HierarchyGroupId: str = None
) -> None:
    pass
```

### update_user_hierarchy_group_name

Type annotations for `boto3.client("connect").update_user_hierarchy_group_name` method.

[Client.update_user_hierarchy_group_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_hierarchy_group_name)

```python
def update_user_hierarchy_group_name(
    self,
    Name: str,
    HierarchyGroupId: str,
    InstanceId: str
) -> None:
    pass
```

### update_user_hierarchy_structure

Type annotations for `boto3.client("connect").update_user_hierarchy_structure` method.

[Client.update_user_hierarchy_structure documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_hierarchy_structure)

```python
def update_user_hierarchy_structure(
    self,
    HierarchyStructure: HierarchyStructureUpdateTypeDef,
    InstanceId: str
) -> None:
    pass
```

### update_user_identity_info

Type annotations for `boto3.client("connect").update_user_identity_info` method.

[Client.update_user_identity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_identity_info)

```python
def update_user_identity_info(
    self,
    IdentityInfo: "UserIdentityInfoTypeDef",
    UserId: str,
    InstanceId: str
) -> None:
    pass
```

### update_user_phone_config

Type annotations for `boto3.client("connect").update_user_phone_config` method.

[Client.update_user_phone_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_phone_config)

```python
def update_user_phone_config(
    self,
    PhoneConfig: "UserPhoneConfigTypeDef",
    UserId: str,
    InstanceId: str
) -> None:
    pass
```

### update_user_routing_profile

Type annotations for `boto3.client("connect").update_user_routing_profile` method.

[Client.update_user_routing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_routing_profile)

```python
def update_user_routing_profile(
    self,
    RoutingProfileId: str,
    UserId: str,
    InstanceId: str
) -> None:
    pass
```

### update_user_security_profiles

Type annotations for `boto3.client("connect").update_user_security_profiles` method.

[Client.update_user_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_security_profiles)

```python
def update_user_security_profiles(
    self,
    SecurityProfileIds: List[str],
    UserId: str,
    InstanceId: str
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.GetMetricData)

```python
@overload
def get_paginator(
    self,
    operation_name: GetMetricDataPaginatorName
) -> GetMetricDataPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListApprovedOrigins documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins)

```python
@overload
def get_paginator(
    self,
    operation_name: ListApprovedOriginsPaginatorName
) -> ListApprovedOriginsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListContactFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactFlows)

```python
@overload
def get_paginator(
    self,
    operation_name: ListContactFlowsPaginatorName
) -> ListContactFlowsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListHoursOfOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListHoursOfOperationsPaginatorName
) -> ListHoursOfOperationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListInstanceAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInstanceAttributesPaginatorName
) -> ListInstanceAttributesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListInstanceStorageConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInstanceStorageConfigsPaginatorName
) -> ListInstanceStorageConfigsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInstancesPaginatorName
) -> ListInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListIntegrationAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListIntegrationAssociationsPaginatorName
) -> ListIntegrationAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListLambdaFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListLambdaFunctionsPaginatorName
) -> ListLambdaFunctionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListLexBots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLexBots)

```python
@overload
def get_paginator(
    self,
    operation_name: ListLexBotsPaginatorName
) -> ListLexBotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListPhoneNumbers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPhoneNumbersPaginatorName
) -> ListPhoneNumbersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListPrompts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPrompts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPromptsPaginatorName
) -> ListPromptsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListQueueQuickConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQueueQuickConnectsPaginatorName
) -> ListQueueQuickConnectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueues)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQueuesPaginatorName
) -> ListQueuesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListQuickConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQuickConnects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQuickConnectsPaginatorName
) -> ListQuickConnectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListRoutingProfileQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRoutingProfileQueuesPaginatorName
) -> ListRoutingProfileQueuesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListRoutingProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRoutingProfilesPaginatorName
) -> ListRoutingProfilesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListSecurityKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSecurityKeysPaginatorName
) -> ListSecurityKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSecurityProfilesPaginatorName
) -> ListSecurityProfilesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListUseCases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUseCases)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUseCasesPaginatorName
) -> ListUseCasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListUserHierarchyGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUserHierarchyGroupsPaginatorName
) -> ListUserHierarchyGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("connect").get_paginator` method.

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUsers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUsersPaginatorName
) -> ListUsersPaginator:
    pass
```