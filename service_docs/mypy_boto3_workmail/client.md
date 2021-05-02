# WorkMailClient for boto3 WorkMail module

> [Index](../index.md) > [WorkMail](./index.md) > WorkMailClient

Auto-generated documentation for [WorkMail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail)
type annotations stubs module [mypy_boto3_workmail](https://pypi.org/project/mypy-boto3-workmail/).

- [WorkMailClient for boto3 WorkMail module](#workmailclient-for-boto3-workmail-module)
  - [WorkMailClient](#workmailclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_delegate_to_resource](#associate_delegate_to_resource)
    - [associate_member_to_group](#associate_member_to_group)
    - [can_paginate](#can_paginate)
    - [cancel_mailbox_export_job](#cancel_mailbox_export_job)
    - [create_alias](#create_alias)
    - [create_group](#create_group)
    - [create_mobile_device_access_rule](#create_mobile_device_access_rule)
    - [create_organization](#create_organization)
    - [create_resource](#create_resource)
    - [create_user](#create_user)
    - [delete_access_control_rule](#delete_access_control_rule)
    - [delete_alias](#delete_alias)
    - [delete_group](#delete_group)
    - [delete_mailbox_permissions](#delete_mailbox_permissions)
    - [delete_mobile_device_access_rule](#delete_mobile_device_access_rule)
    - [delete_organization](#delete_organization)
    - [delete_resource](#delete_resource)
    - [delete_retention_policy](#delete_retention_policy)
    - [delete_user](#delete_user)
    - [deregister_from_work_mail](#deregister_from_work_mail)
    - [describe_group](#describe_group)
    - [describe_mailbox_export_job](#describe_mailbox_export_job)
    - [describe_organization](#describe_organization)
    - [describe_resource](#describe_resource)
    - [describe_user](#describe_user)
    - [disassociate_delegate_from_resource](#disassociate_delegate_from_resource)
    - [disassociate_member_from_group](#disassociate_member_from_group)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_access_control_effect](#get_access_control_effect)
    - [get_default_retention_policy](#get_default_retention_policy)
    - [get_mailbox_details](#get_mailbox_details)
    - [get_mobile_device_access_effect](#get_mobile_device_access_effect)
    - [list_access_control_rules](#list_access_control_rules)
    - [list_aliases](#list_aliases)
    - [list_group_members](#list_group_members)
    - [list_groups](#list_groups)
    - [list_mailbox_export_jobs](#list_mailbox_export_jobs)
    - [list_mailbox_permissions](#list_mailbox_permissions)
    - [list_mobile_device_access_rules](#list_mobile_device_access_rules)
    - [list_organizations](#list_organizations)
    - [list_resource_delegates](#list_resource_delegates)
    - [list_resources](#list_resources)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_users](#list_users)
    - [put_access_control_rule](#put_access_control_rule)
    - [put_mailbox_permissions](#put_mailbox_permissions)
    - [put_retention_policy](#put_retention_policy)
    - [register_to_work_mail](#register_to_work_mail)
    - [reset_password](#reset_password)
    - [start_mailbox_export_job](#start_mailbox_export_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_mailbox_quota](#update_mailbox_quota)
    - [update_mobile_device_access_rule](#update_mobile_device_access_rule)
    - [update_primary_email_address](#update_primary_email_address)
    - [update_resource](#update_resource)
    - [get_paginator](#get_paginator)

## WorkMailClient

Type annotations for `boto3.client("workmail")`

Can be used directly:

```python
from mypy_boto3_workmail.client import WorkMailClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_workmail.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DirectoryInUseException`
- `Exceptions.DirectoryServiceAuthenticationFailedException`
- `Exceptions.DirectoryUnavailableException`
- `Exceptions.EmailAddressInUseException`
- `Exceptions.EntityAlreadyRegisteredException`
- `Exceptions.EntityNotFoundException`
- `Exceptions.EntityStateException`
- `Exceptions.InvalidConfigurationException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidPasswordException`
- `Exceptions.LimitExceededException`
- `Exceptions.MailDomainNotFoundException`
- `Exceptions.MailDomainStateException`
- `Exceptions.NameAvailabilityException`
- `Exceptions.OrganizationNotFoundException`
- `Exceptions.OrganizationStateException`
- `Exceptions.ReservedNameException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnsupportedOperationException`


## Methods


### associate_delegate_to_resource

Type annotations for `boto3.client("workmail").associate_delegate_to_resource` method.

[Client.associate_delegate_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.associate_delegate_to_resource)

```python
def associate_delegate_to_resource(
    self,
    OrganizationId: str,
    ResourceId: str,
    EntityId: str
) -> Dict[str, Any]:
    pass
```

### associate_member_to_group

Type annotations for `boto3.client("workmail").associate_member_to_group` method.

[Client.associate_member_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.associate_member_to_group)

```python
def associate_member_to_group(
    self,
    OrganizationId: str,
    GroupId: str,
    MemberId: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("workmail").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_mailbox_export_job

Type annotations for `boto3.client("workmail").cancel_mailbox_export_job` method.

[Client.cancel_mailbox_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.cancel_mailbox_export_job)

```python
def cancel_mailbox_export_job(
    self,
    ClientToken: str,
    JobId: str,
    OrganizationId: str
) -> Dict[str, Any]:
    pass
```

### create_alias

Type annotations for `boto3.client("workmail").create_alias` method.

[Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.create_alias)

```python
def create_alias(
    self,
    OrganizationId: str,
    EntityId: str,
    Alias: str
) -> Dict[str, Any]:
    pass
```

### create_group

Type annotations for `boto3.client("workmail").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.create_group)

```python
def create_group(
    self,
    OrganizationId: str,
    Name: str
) -> CreateGroupResponseTypeDef:
    pass
```

### create_mobile_device_access_rule

Type annotations for `boto3.client("workmail").create_mobile_device_access_rule` method.

[Client.create_mobile_device_access_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.create_mobile_device_access_rule)

```python
def create_mobile_device_access_rule(
    self,
    OrganizationId: str,
    Name: str,
    Effect: MobileDeviceAccessRuleEffect,
    ClientToken: str = None,
    Description: str = None,
    DeviceTypes: List[str] = None,
    NotDeviceTypes: List[str] = None,
    DeviceModels: List[str] = None,
    NotDeviceModels: List[str] = None,
    DeviceOperatingSystems: List[str] = None,
    NotDeviceOperatingSystems: List[str] = None,
    DeviceUserAgents: List[str] = None,
    NotDeviceUserAgents: List[str] = None
) -> CreateMobileDeviceAccessRuleResponseTypeDef:
    pass
```

### create_organization

Type annotations for `boto3.client("workmail").create_organization` method.

[Client.create_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.create_organization)

```python
def create_organization(
    self,
    Alias: str,
    DirectoryId: str = None,
    ClientToken: str = None,
    Domains: List[DomainTypeDef] = None,
    KmsKeyArn: str = None,
    EnableInteroperability: bool = None
) -> CreateOrganizationResponseTypeDef:
    pass
```

### create_resource

Type annotations for `boto3.client("workmail").create_resource` method.

[Client.create_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.create_resource)

```python
def create_resource(
    self,
    OrganizationId: str,
    Name: str,
    Type: ResourceType
) -> CreateResourceResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("workmail").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.create_user)

```python
def create_user(
    self,
    OrganizationId: str,
    Name: str,
    DisplayName: str,
    Password: str
) -> CreateUserResponseTypeDef:
    pass
```

### delete_access_control_rule

Type annotations for `boto3.client("workmail").delete_access_control_rule` method.

[Client.delete_access_control_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_access_control_rule)

```python
def delete_access_control_rule(
    self,
    OrganizationId: str,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_alias

Type annotations for `boto3.client("workmail").delete_alias` method.

[Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_alias)

```python
def delete_alias(
    self,
    OrganizationId: str,
    EntityId: str,
    Alias: str
) -> Dict[str, Any]:
    pass
```

### delete_group

Type annotations for `boto3.client("workmail").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_group)

```python
def delete_group(
    self,
    OrganizationId: str,
    GroupId: str
) -> Dict[str, Any]:
    pass
```

### delete_mailbox_permissions

Type annotations for `boto3.client("workmail").delete_mailbox_permissions` method.

[Client.delete_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_mailbox_permissions)

```python
def delete_mailbox_permissions(
    self,
    OrganizationId: str,
    EntityId: str,
    GranteeId: str
) -> Dict[str, Any]:
    pass
```

### delete_mobile_device_access_rule

Type annotations for `boto3.client("workmail").delete_mobile_device_access_rule` method.

[Client.delete_mobile_device_access_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_mobile_device_access_rule)

```python
def delete_mobile_device_access_rule(
    self,
    OrganizationId: str,
    MobileDeviceAccessRuleId: str
) -> Dict[str, Any]:
    pass
```

### delete_organization

Type annotations for `boto3.client("workmail").delete_organization` method.

[Client.delete_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_organization)

```python
def delete_organization(
    self,
    OrganizationId: str,
    DeleteDirectory: bool,
    ClientToken: str = None
) -> DeleteOrganizationResponseTypeDef:
    pass
```

### delete_resource

Type annotations for `boto3.client("workmail").delete_resource` method.

[Client.delete_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_resource)

```python
def delete_resource(
    self,
    OrganizationId: str,
    ResourceId: str
) -> Dict[str, Any]:
    pass
```

### delete_retention_policy

Type annotations for `boto3.client("workmail").delete_retention_policy` method.

[Client.delete_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_retention_policy)

```python
def delete_retention_policy(
    self,
    OrganizationId: str,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_user

Type annotations for `boto3.client("workmail").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.delete_user)

```python
def delete_user(
    self,
    OrganizationId: str,
    UserId: str
) -> Dict[str, Any]:
    pass
```

### deregister_from_work_mail

Type annotations for `boto3.client("workmail").deregister_from_work_mail` method.

[Client.deregister_from_work_mail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.deregister_from_work_mail)

```python
def deregister_from_work_mail(
    self,
    OrganizationId: str,
    EntityId: str
) -> Dict[str, Any]:
    pass
```

### describe_group

Type annotations for `boto3.client("workmail").describe_group` method.

[Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.describe_group)

```python
def describe_group(
    self,
    OrganizationId: str,
    GroupId: str
) -> DescribeGroupResponseTypeDef:
    pass
```

### describe_mailbox_export_job

Type annotations for `boto3.client("workmail").describe_mailbox_export_job` method.

[Client.describe_mailbox_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.describe_mailbox_export_job)

```python
def describe_mailbox_export_job(
    self,
    JobId: str,
    OrganizationId: str
) -> DescribeMailboxExportJobResponseTypeDef:
    pass
```

### describe_organization

Type annotations for `boto3.client("workmail").describe_organization` method.

[Client.describe_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.describe_organization)

```python
def describe_organization(
    self,
    OrganizationId: str
) -> DescribeOrganizationResponseTypeDef:
    pass
```

### describe_resource

Type annotations for `boto3.client("workmail").describe_resource` method.

[Client.describe_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.describe_resource)

```python
def describe_resource(
    self,
    OrganizationId: str,
    ResourceId: str
) -> DescribeResourceResponseTypeDef:
    pass
```

### describe_user

Type annotations for `boto3.client("workmail").describe_user` method.

[Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.describe_user)

```python
def describe_user(
    self,
    OrganizationId: str,
    UserId: str
) -> DescribeUserResponseTypeDef:
    pass
```

### disassociate_delegate_from_resource

Type annotations for `boto3.client("workmail").disassociate_delegate_from_resource` method.

[Client.disassociate_delegate_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.disassociate_delegate_from_resource)

```python
def disassociate_delegate_from_resource(
    self,
    OrganizationId: str,
    ResourceId: str,
    EntityId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_member_from_group

Type annotations for `boto3.client("workmail").disassociate_member_from_group` method.

[Client.disassociate_member_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.disassociate_member_from_group)

```python
def disassociate_member_from_group(
    self,
    OrganizationId: str,
    GroupId: str,
    MemberId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("workmail").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.generate_presigned_url)

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

### get_access_control_effect

Type annotations for `boto3.client("workmail").get_access_control_effect` method.

[Client.get_access_control_effect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.get_access_control_effect)

```python
def get_access_control_effect(
    self,
    OrganizationId: str,
    IpAddress: str,
    Action: str,
    UserId: str
) -> GetAccessControlEffectResponseTypeDef:
    pass
```

### get_default_retention_policy

Type annotations for `boto3.client("workmail").get_default_retention_policy` method.

[Client.get_default_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.get_default_retention_policy)

```python
def get_default_retention_policy(
    self,
    OrganizationId: str
) -> GetDefaultRetentionPolicyResponseTypeDef:
    pass
```

### get_mailbox_details

Type annotations for `boto3.client("workmail").get_mailbox_details` method.

[Client.get_mailbox_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.get_mailbox_details)

```python
def get_mailbox_details(
    self,
    OrganizationId: str,
    UserId: str
) -> GetMailboxDetailsResponseTypeDef:
    pass
```

### get_mobile_device_access_effect

Type annotations for `boto3.client("workmail").get_mobile_device_access_effect` method.

[Client.get_mobile_device_access_effect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.get_mobile_device_access_effect)

```python
def get_mobile_device_access_effect(
    self,
    OrganizationId: str,
    DeviceType: str = None,
    DeviceModel: str = None,
    DeviceOperatingSystem: str = None,
    DeviceUserAgent: str = None
) -> GetMobileDeviceAccessEffectResponseTypeDef:
    pass
```

### list_access_control_rules

Type annotations for `boto3.client("workmail").list_access_control_rules` method.

[Client.list_access_control_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_access_control_rules)

```python
def list_access_control_rules(
    self,
    OrganizationId: str
) -> ListAccessControlRulesResponseTypeDef:
    pass
```

### list_aliases

Type annotations for `boto3.client("workmail").list_aliases` method.

[Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_aliases)

```python
def list_aliases(
    self,
    OrganizationId: str,
    EntityId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAliasesResponseTypeDef:
    pass
```

### list_group_members

Type annotations for `boto3.client("workmail").list_group_members` method.

[Client.list_group_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_group_members)

```python
def list_group_members(
    self,
    OrganizationId: str,
    GroupId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListGroupMembersResponseTypeDef:
    pass
```

### list_groups

Type annotations for `boto3.client("workmail").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_groups)

```python
def list_groups(
    self,
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListGroupsResponseTypeDef:
    pass
```

### list_mailbox_export_jobs

Type annotations for `boto3.client("workmail").list_mailbox_export_jobs` method.

[Client.list_mailbox_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_mailbox_export_jobs)

```python
def list_mailbox_export_jobs(
    self,
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMailboxExportJobsResponseTypeDef:
    pass
```

### list_mailbox_permissions

Type annotations for `boto3.client("workmail").list_mailbox_permissions` method.

[Client.list_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_mailbox_permissions)

```python
def list_mailbox_permissions(
    self,
    OrganizationId: str,
    EntityId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMailboxPermissionsResponseTypeDef:
    pass
```

### list_mobile_device_access_rules

Type annotations for `boto3.client("workmail").list_mobile_device_access_rules` method.

[Client.list_mobile_device_access_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_mobile_device_access_rules)

```python
def list_mobile_device_access_rules(
    self,
    OrganizationId: str
) -> ListMobileDeviceAccessRulesResponseTypeDef:
    pass
```

### list_organizations

Type annotations for `boto3.client("workmail").list_organizations` method.

[Client.list_organizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_organizations)

```python
def list_organizations(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListOrganizationsResponseTypeDef:
    pass
```

### list_resource_delegates

Type annotations for `boto3.client("workmail").list_resource_delegates` method.

[Client.list_resource_delegates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_resource_delegates)

```python
def list_resource_delegates(
    self,
    OrganizationId: str,
    ResourceId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListResourceDelegatesResponseTypeDef:
    pass
```

### list_resources

Type annotations for `boto3.client("workmail").list_resources` method.

[Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_resources)

```python
def list_resources(
    self,
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListResourcesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("workmail").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("workmail").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.list_users)

```python
def list_users(
    self,
    OrganizationId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListUsersResponseTypeDef:
    pass
```

### put_access_control_rule

Type annotations for `boto3.client("workmail").put_access_control_rule` method.

[Client.put_access_control_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.put_access_control_rule)

```python
def put_access_control_rule(
    self,
    Name: str,
    Effect: AccessControlRuleEffect,
    Description: str,
    OrganizationId: str,
    IpRanges: List[str] = None,
    NotIpRanges: List[str] = None,
    Actions: List[str] = None,
    NotActions: List[str] = None,
    UserIds: List[str] = None,
    NotUserIds: List[str] = None
) -> Dict[str, Any]:
    pass
```

### put_mailbox_permissions

Type annotations for `boto3.client("workmail").put_mailbox_permissions` method.

[Client.put_mailbox_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.put_mailbox_permissions)

```python
def put_mailbox_permissions(
    self,
    OrganizationId: str,
    EntityId: str,
    GranteeId: str,
    PermissionValues: List[PermissionType]
) -> Dict[str, Any]:
    pass
```

### put_retention_policy

Type annotations for `boto3.client("workmail").put_retention_policy` method.

[Client.put_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.put_retention_policy)

```python
def put_retention_policy(
    self,
    OrganizationId: str,
    Name: str,
    FolderConfigurations: List["FolderConfigurationTypeDef"],
    Id: str = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### register_to_work_mail

Type annotations for `boto3.client("workmail").register_to_work_mail` method.

[Client.register_to_work_mail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.register_to_work_mail)

```python
def register_to_work_mail(
    self,
    OrganizationId: str,
    EntityId: str,
    Email: str
) -> Dict[str, Any]:
    pass
```

### reset_password

Type annotations for `boto3.client("workmail").reset_password` method.

[Client.reset_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.reset_password)

```python
def reset_password(
    self,
    OrganizationId: str,
    UserId: str,
    Password: str
) -> Dict[str, Any]:
    pass
```

### start_mailbox_export_job

Type annotations for `boto3.client("workmail").start_mailbox_export_job` method.

[Client.start_mailbox_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.start_mailbox_export_job)

```python
def start_mailbox_export_job(
    self,
    ClientToken: str,
    OrganizationId: str,
    EntityId: str,
    RoleArn: str,
    KmsKeyArn: str,
    S3BucketName: str,
    S3Prefix: str,
    Description: str = None
) -> StartMailboxExportJobResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("workmail").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("workmail").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_mailbox_quota

Type annotations for `boto3.client("workmail").update_mailbox_quota` method.

[Client.update_mailbox_quota documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.update_mailbox_quota)

```python
def update_mailbox_quota(
    self,
    OrganizationId: str,
    UserId: str,
    MailboxQuota: int
) -> Dict[str, Any]:
    pass
```

### update_mobile_device_access_rule

Type annotations for `boto3.client("workmail").update_mobile_device_access_rule` method.

[Client.update_mobile_device_access_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.update_mobile_device_access_rule)

```python
def update_mobile_device_access_rule(
    self,
    OrganizationId: str,
    MobileDeviceAccessRuleId: str,
    Name: str,
    Effect: MobileDeviceAccessRuleEffect,
    Description: str = None,
    DeviceTypes: List[str] = None,
    NotDeviceTypes: List[str] = None,
    DeviceModels: List[str] = None,
    NotDeviceModels: List[str] = None,
    DeviceOperatingSystems: List[str] = None,
    NotDeviceOperatingSystems: List[str] = None,
    DeviceUserAgents: List[str] = None,
    NotDeviceUserAgents: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_primary_email_address

Type annotations for `boto3.client("workmail").update_primary_email_address` method.

[Client.update_primary_email_address documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.update_primary_email_address)

```python
def update_primary_email_address(
    self,
    OrganizationId: str,
    EntityId: str,
    Email: str
) -> Dict[str, Any]:
    pass
```

### update_resource

Type annotations for `boto3.client("workmail").update_resource` method.

[Client.update_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Client.update_resource)

```python
def update_resource(
    self,
    OrganizationId: str,
    ResourceId: str,
    Name: str = None,
    BookingOptions: "BookingOptionsTypeDef" = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("workmail").get_paginator` method with overloads.

- `client.get_paginator("list_aliases")` -> [ListAliasesPaginator](./paginators.md#listaliasespaginator)
- `client.get_paginator("list_group_members")` -> [ListGroupMembersPaginator](./paginators.md#listgroupmemberspaginator)
- `client.get_paginator("list_groups")` -> [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- `client.get_paginator("list_mailbox_permissions")` -> [ListMailboxPermissionsPaginator](./paginators.md#listmailboxpermissionspaginator)
- `client.get_paginator("list_organizations")` -> [ListOrganizationsPaginator](./paginators.md#listorganizationspaginator)
- `client.get_paginator("list_resource_delegates")` -> [ListResourceDelegatesPaginator](./paginators.md#listresourcedelegatespaginator)
- `client.get_paginator("list_resources")` -> [ListResourcesPaginator](./paginators.md#listresourcespaginator)
- `client.get_paginator("list_users")` -> [ListUsersPaginator](./paginators.md#listuserspaginator)


