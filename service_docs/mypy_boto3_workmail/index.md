# Type annotations for boto3 WorkMail module

> [Index](../index.md) > WorkMail

Auto-generated documentation for [WorkMail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail)
type annotations stubs module [mypy_boto3_workmail](https://pypi.org/project/mypy-boto3-workmail/).

```bash
pip install mypy-boto3-workmail
```

- [Type annotations for boto3 WorkMail module](#type-annotations-for-boto3-workmail-module)
  - [WorkMailClient](#workmailclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## WorkMailClient

Type annotations for  `boto3.client("workmail")` as [WorkMailClient](./client.md)

Can be used directly:

```python
from mypy_boto3_workmail.client import WorkMailClient
```


WorkMailClient [exceptions](./client.md#exceptions)



### Methods
- [associate_delegate_to_resource](./client.md#associate-delegate-to-resource)
- [associate_member_to_group](./client.md#associate-member-to-group)
- [can_paginate](./client.md#can-paginate)
- [cancel_mailbox_export_job](./client.md#cancel-mailbox-export-job)
- [create_alias](./client.md#create-alias)
- [create_group](./client.md#create-group)
- [create_mobile_device_access_rule](./client.md#create-mobile-device-access-rule)
- [create_organization](./client.md#create-organization)
- [create_resource](./client.md#create-resource)
- [create_user](./client.md#create-user)
- [delete_access_control_rule](./client.md#delete-access-control-rule)
- [delete_alias](./client.md#delete-alias)
- [delete_group](./client.md#delete-group)
- [delete_mailbox_permissions](./client.md#delete-mailbox-permissions)
- [delete_mobile_device_access_rule](./client.md#delete-mobile-device-access-rule)
- [delete_organization](./client.md#delete-organization)
- [delete_resource](./client.md#delete-resource)
- [delete_retention_policy](./client.md#delete-retention-policy)
- [delete_user](./client.md#delete-user)
- [deregister_from_work_mail](./client.md#deregister-from-work-mail)
- [describe_group](./client.md#describe-group)
- [describe_mailbox_export_job](./client.md#describe-mailbox-export-job)
- [describe_organization](./client.md#describe-organization)
- [describe_resource](./client.md#describe-resource)
- [describe_user](./client.md#describe-user)
- [disassociate_delegate_from_resource](./client.md#disassociate-delegate-from-resource)
- [disassociate_member_from_group](./client.md#disassociate-member-from-group)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_access_control_effect](./client.md#get-access-control-effect)
- [get_default_retention_policy](./client.md#get-default-retention-policy)
- [get_mailbox_details](./client.md#get-mailbox-details)
- [get_mobile_device_access_effect](./client.md#get-mobile-device-access-effect)
- [get_paginator](./client.md#get-paginator)
- [list_access_control_rules](./client.md#list-access-control-rules)
- [list_aliases](./client.md#list-aliases)
- [list_group_members](./client.md#list-group-members)
- [list_groups](./client.md#list-groups)
- [list_mailbox_export_jobs](./client.md#list-mailbox-export-jobs)
- [list_mailbox_permissions](./client.md#list-mailbox-permissions)
- [list_mobile_device_access_rules](./client.md#list-mobile-device-access-rules)
- [list_organizations](./client.md#list-organizations)
- [list_resource_delegates](./client.md#list-resource-delegates)
- [list_resources](./client.md#list-resources)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_users](./client.md#list-users)
- [put_access_control_rule](./client.md#put-access-control-rule)
- [put_mailbox_permissions](./client.md#put-mailbox-permissions)
- [put_retention_policy](./client.md#put-retention-policy)
- [register_to_work_mail](./client.md#register-to-work-mail)
- [reset_password](./client.md#reset-password)
- [start_mailbox_export_job](./client.md#start-mailbox-export-job)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_mailbox_quota](./client.md#update-mailbox-quota)
- [update_mobile_device_access_rule](./client.md#update-mobile-device-access-rule)
- [update_primary_email_address](./client.md#update-primary-email-address)
- [update_resource](./client.md#update-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DirectoryInUseException](./client.md#directoryinuseexception)
- [DirectoryServiceAuthenticationFailedException](./client.md#directoryserviceauthenticationfailedexception)
- [DirectoryUnavailableException](./client.md#directoryunavailableexception)
- [EmailAddressInUseException](./client.md#emailaddressinuseexception)
- [EntityAlreadyRegisteredException](./client.md#entityalreadyregisteredexception)
- [EntityNotFoundException](./client.md#entitynotfoundexception)
- [EntityStateException](./client.md#entitystateexception)
- [InvalidConfigurationException](./client.md#invalidconfigurationexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidPasswordException](./client.md#invalidpasswordexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MailDomainNotFoundException](./client.md#maildomainnotfoundexception)
- [MailDomainStateException](./client.md#maildomainstateexception)
- [NameAvailabilityException](./client.md#nameavailabilityexception)
- [OrganizationNotFoundException](./client.md#organizationnotfoundexception)
- [OrganizationStateException](./client.md#organizationstateexception)
- [ReservedNameException](./client.md#reservednameexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("workmail").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_workmail.paginators import ListAliasesPaginator, ...
```

- [ListAliasesPaginator](./paginators.md#listaliasespaginator)
- [ListGroupMembersPaginator](./paginators.md#listgroupmemberspaginator)
- [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- [ListMailboxPermissionsPaginator](./paginators.md#listmailboxpermissionspaginator)
- [ListOrganizationsPaginator](./paginators.md#listorganizationspaginator)
- [ListResourceDelegatesPaginator](./paginators.md#listresourcedelegatespaginator)
- [ListResourcesPaginator](./paginators.md#listresourcespaginator)
- [ListUsersPaginator](./paginators.md#listuserspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workmail.literals import AccessControlRuleEffect, ...
```

- [AccessControlRuleEffect](./literals.md#accesscontrolruleeffect)
- [EntityState](./literals.md#entitystate)
- [FolderName](./literals.md#foldername)
- [ListAliasesPaginatorName](./literals.md#listaliasespaginatorname)
- [ListGroupMembersPaginatorName](./literals.md#listgroupmemberspaginatorname)
- [ListGroupsPaginatorName](./literals.md#listgroupspaginatorname)
- [ListMailboxPermissionsPaginatorName](./literals.md#listmailboxpermissionspaginatorname)
- [ListOrganizationsPaginatorName](./literals.md#listorganizationspaginatorname)
- [ListResourceDelegatesPaginatorName](./literals.md#listresourcedelegatespaginatorname)
- [ListResourcesPaginatorName](./literals.md#listresourcespaginatorname)
- [ListUsersPaginatorName](./literals.md#listuserspaginatorname)
- [MailboxExportJobState](./literals.md#mailboxexportjobstate)
- [MemberType](./literals.md#membertype)
- [MobileDeviceAccessRuleEffect](./literals.md#mobiledeviceaccessruleeffect)
- [PermissionType](./literals.md#permissiontype)
- [ResourceType](./literals.md#resourcetype)
- [RetentionAction](./literals.md#retentionaction)
- [UserRole](./literals.md#userrole)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef, ...
```

- [AccessControlRuleTypeDef](./type_defs.md#accesscontrolruletypedef)
- [BookingOptionsTypeDef](./type_defs.md#bookingoptionstypedef)
- [DelegateTypeDef](./type_defs.md#delegatetypedef)
- [FolderConfigurationTypeDef](./type_defs.md#folderconfigurationtypedef)
- [GroupTypeDef](./type_defs.md#grouptypedef)
- [MailboxExportJobTypeDef](./type_defs.md#mailboxexportjobtypedef)
- [MemberTypeDef](./type_defs.md#membertypedef)
- [MobileDeviceAccessMatchedRuleTypeDef](./type_defs.md#mobiledeviceaccessmatchedruletypedef)
- [MobileDeviceAccessRuleTypeDef](./type_defs.md#mobiledeviceaccessruletypedef)
- [OrganizationSummaryTypeDef](./type_defs.md#organizationsummarytypedef)
- [PermissionTypeDef](./type_defs.md#permissiontypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
- [CreateGroupResponseTypeDef](./type_defs.md#creategroupresponsetypedef)
- [CreateMobileDeviceAccessRuleResponseTypeDef](./type_defs.md#createmobiledeviceaccessruleresponsetypedef)
- [CreateOrganizationResponseTypeDef](./type_defs.md#createorganizationresponsetypedef)
- [CreateResourceResponseTypeDef](./type_defs.md#createresourceresponsetypedef)
- [CreateUserResponseTypeDef](./type_defs.md#createuserresponsetypedef)
- [DeleteOrganizationResponseTypeDef](./type_defs.md#deleteorganizationresponsetypedef)
- [DescribeGroupResponseTypeDef](./type_defs.md#describegroupresponsetypedef)
- [DescribeMailboxExportJobResponseTypeDef](./type_defs.md#describemailboxexportjobresponsetypedef)
- [DescribeOrganizationResponseTypeDef](./type_defs.md#describeorganizationresponsetypedef)
- [DescribeResourceResponseTypeDef](./type_defs.md#describeresourceresponsetypedef)
- [DescribeUserResponseTypeDef](./type_defs.md#describeuserresponsetypedef)
- [DomainTypeDef](./type_defs.md#domaintypedef)
- [GetAccessControlEffectResponseTypeDef](./type_defs.md#getaccesscontroleffectresponsetypedef)
- [GetDefaultRetentionPolicyResponseTypeDef](./type_defs.md#getdefaultretentionpolicyresponsetypedef)
- [GetMailboxDetailsResponseTypeDef](./type_defs.md#getmailboxdetailsresponsetypedef)
- [GetMobileDeviceAccessEffectResponseTypeDef](./type_defs.md#getmobiledeviceaccesseffectresponsetypedef)
- [ListAccessControlRulesResponseTypeDef](./type_defs.md#listaccesscontrolrulesresponsetypedef)
- [ListAliasesResponseTypeDef](./type_defs.md#listaliasesresponsetypedef)
- [ListGroupMembersResponseTypeDef](./type_defs.md#listgroupmembersresponsetypedef)
- [ListGroupsResponseTypeDef](./type_defs.md#listgroupsresponsetypedef)
- [ListMailboxExportJobsResponseTypeDef](./type_defs.md#listmailboxexportjobsresponsetypedef)
- [ListMailboxPermissionsResponseTypeDef](./type_defs.md#listmailboxpermissionsresponsetypedef)
- [ListMobileDeviceAccessRulesResponseTypeDef](./type_defs.md#listmobiledeviceaccessrulesresponsetypedef)
- [ListOrganizationsResponseTypeDef](./type_defs.md#listorganizationsresponsetypedef)
- [ListResourceDelegatesResponseTypeDef](./type_defs.md#listresourcedelegatesresponsetypedef)
- [ListResourcesResponseTypeDef](./type_defs.md#listresourcesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListUsersResponseTypeDef](./type_defs.md#listusersresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartMailboxExportJobResponseTypeDef](./type_defs.md#startmailboxexportjobresponsetypedef)
