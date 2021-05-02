# Type annotations for boto3 IAM module

> [Index](../index.md) > IAM

Auto-generated documentation for [IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM)
type annotations stubs module [mypy_boto3_iam](https://pypi.org/project/mypy-boto3-iam/).

```bash
pip install mypy-boto3-iam
```

- [Type annotations for boto3 IAM module](#type-annotations-for-boto3-iam-module)
  - [IAMClient](#iamclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [IAMServiceResource](#iamserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## IAMClient

Type annotations for  `boto3.client("iam")` as [IAMClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iam.client import IAMClient
```


IAMClient [exceptions](./client.md#exceptions)



### Methods
- [add_client_id_to_open_id_connect_provider](./client.md#add-client-id-to-open-id-connect-provider)
- [add_role_to_instance_profile](./client.md#add-role-to-instance-profile)
- [add_user_to_group](./client.md#add-user-to-group)
- [attach_group_policy](./client.md#attach-group-policy)
- [attach_role_policy](./client.md#attach-role-policy)
- [attach_user_policy](./client.md#attach-user-policy)
- [can_paginate](./client.md#can-paginate)
- [change_password](./client.md#change-password)
- [create_access_key](./client.md#create-access-key)
- [create_account_alias](./client.md#create-account-alias)
- [create_group](./client.md#create-group)
- [create_instance_profile](./client.md#create-instance-profile)
- [create_login_profile](./client.md#create-login-profile)
- [create_open_id_connect_provider](./client.md#create-open-id-connect-provider)
- [create_policy](./client.md#create-policy)
- [create_policy_version](./client.md#create-policy-version)
- [create_role](./client.md#create-role)
- [create_saml_provider](./client.md#create-saml-provider)
- [create_service_linked_role](./client.md#create-service-linked-role)
- [create_service_specific_credential](./client.md#create-service-specific-credential)
- [create_user](./client.md#create-user)
- [create_virtual_mfa_device](./client.md#create-virtual-mfa-device)
- [deactivate_mfa_device](./client.md#deactivate-mfa-device)
- [delete_access_key](./client.md#delete-access-key)
- [delete_account_alias](./client.md#delete-account-alias)
- [delete_account_password_policy](./client.md#delete-account-password-policy)
- [delete_group](./client.md#delete-group)
- [delete_group_policy](./client.md#delete-group-policy)
- [delete_instance_profile](./client.md#delete-instance-profile)
- [delete_login_profile](./client.md#delete-login-profile)
- [delete_open_id_connect_provider](./client.md#delete-open-id-connect-provider)
- [delete_policy](./client.md#delete-policy)
- [delete_policy_version](./client.md#delete-policy-version)
- [delete_role](./client.md#delete-role)
- [delete_role_permissions_boundary](./client.md#delete-role-permissions-boundary)
- [delete_role_policy](./client.md#delete-role-policy)
- [delete_saml_provider](./client.md#delete-saml-provider)
- [delete_server_certificate](./client.md#delete-server-certificate)
- [delete_service_linked_role](./client.md#delete-service-linked-role)
- [delete_service_specific_credential](./client.md#delete-service-specific-credential)
- [delete_signing_certificate](./client.md#delete-signing-certificate)
- [delete_ssh_public_key](./client.md#delete-ssh-public-key)
- [delete_user](./client.md#delete-user)
- [delete_user_permissions_boundary](./client.md#delete-user-permissions-boundary)
- [delete_user_policy](./client.md#delete-user-policy)
- [delete_virtual_mfa_device](./client.md#delete-virtual-mfa-device)
- [detach_group_policy](./client.md#detach-group-policy)
- [detach_role_policy](./client.md#detach-role-policy)
- [detach_user_policy](./client.md#detach-user-policy)
- [enable_mfa_device](./client.md#enable-mfa-device)
- [generate_credential_report](./client.md#generate-credential-report)
- [generate_organizations_access_report](./client.md#generate-organizations-access-report)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [generate_service_last_accessed_details](./client.md#generate-service-last-accessed-details)
- [get_access_key_last_used](./client.md#get-access-key-last-used)
- [get_account_authorization_details](./client.md#get-account-authorization-details)
- [get_account_password_policy](./client.md#get-account-password-policy)
- [get_account_summary](./client.md#get-account-summary)
- [get_context_keys_for_custom_policy](./client.md#get-context-keys-for-custom-policy)
- [get_context_keys_for_principal_policy](./client.md#get-context-keys-for-principal-policy)
- [get_credential_report](./client.md#get-credential-report)
- [get_group](./client.md#get-group)
- [get_group_policy](./client.md#get-group-policy)
- [get_instance_profile](./client.md#get-instance-profile)
- [get_login_profile](./client.md#get-login-profile)
- [get_open_id_connect_provider](./client.md#get-open-id-connect-provider)
- [get_organizations_access_report](./client.md#get-organizations-access-report)
- [get_paginator](./client.md#get-paginator)
- [get_policy](./client.md#get-policy)
- [get_policy_version](./client.md#get-policy-version)
- [get_role](./client.md#get-role)
- [get_role_policy](./client.md#get-role-policy)
- [get_saml_provider](./client.md#get-saml-provider)
- [get_server_certificate](./client.md#get-server-certificate)
- [get_service_last_accessed_details](./client.md#get-service-last-accessed-details)
- [get_service_last_accessed_details_with_entities](./client.md#get-service-last-accessed-details-with-entities)
- [get_service_linked_role_deletion_status](./client.md#get-service-linked-role-deletion-status)
- [get_ssh_public_key](./client.md#get-ssh-public-key)
- [get_user](./client.md#get-user)
- [get_user_policy](./client.md#get-user-policy)
- [get_waiter](./client.md#get-waiter)
- [list_access_keys](./client.md#list-access-keys)
- [list_account_aliases](./client.md#list-account-aliases)
- [list_attached_group_policies](./client.md#list-attached-group-policies)
- [list_attached_role_policies](./client.md#list-attached-role-policies)
- [list_attached_user_policies](./client.md#list-attached-user-policies)
- [list_entities_for_policy](./client.md#list-entities-for-policy)
- [list_group_policies](./client.md#list-group-policies)
- [list_groups](./client.md#list-groups)
- [list_groups_for_user](./client.md#list-groups-for-user)
- [list_instance_profile_tags](./client.md#list-instance-profile-tags)
- [list_instance_profiles](./client.md#list-instance-profiles)
- [list_instance_profiles_for_role](./client.md#list-instance-profiles-for-role)
- [list_mfa_device_tags](./client.md#list-mfa-device-tags)
- [list_mfa_devices](./client.md#list-mfa-devices)
- [list_open_id_connect_provider_tags](./client.md#list-open-id-connect-provider-tags)
- [list_open_id_connect_providers](./client.md#list-open-id-connect-providers)
- [list_policies](./client.md#list-policies)
- [list_policies_granting_service_access](./client.md#list-policies-granting-service-access)
- [list_policy_tags](./client.md#list-policy-tags)
- [list_policy_versions](./client.md#list-policy-versions)
- [list_role_policies](./client.md#list-role-policies)
- [list_role_tags](./client.md#list-role-tags)
- [list_roles](./client.md#list-roles)
- [list_saml_provider_tags](./client.md#list-saml-provider-tags)
- [list_saml_providers](./client.md#list-saml-providers)
- [list_server_certificate_tags](./client.md#list-server-certificate-tags)
- [list_server_certificates](./client.md#list-server-certificates)
- [list_service_specific_credentials](./client.md#list-service-specific-credentials)
- [list_signing_certificates](./client.md#list-signing-certificates)
- [list_ssh_public_keys](./client.md#list-ssh-public-keys)
- [list_user_policies](./client.md#list-user-policies)
- [list_user_tags](./client.md#list-user-tags)
- [list_users](./client.md#list-users)
- [list_virtual_mfa_devices](./client.md#list-virtual-mfa-devices)
- [put_group_policy](./client.md#put-group-policy)
- [put_role_permissions_boundary](./client.md#put-role-permissions-boundary)
- [put_role_policy](./client.md#put-role-policy)
- [put_user_permissions_boundary](./client.md#put-user-permissions-boundary)
- [put_user_policy](./client.md#put-user-policy)
- [remove_client_id_from_open_id_connect_provider](./client.md#remove-client-id-from-open-id-connect-provider)
- [remove_role_from_instance_profile](./client.md#remove-role-from-instance-profile)
- [remove_user_from_group](./client.md#remove-user-from-group)
- [reset_service_specific_credential](./client.md#reset-service-specific-credential)
- [resync_mfa_device](./client.md#resync-mfa-device)
- [set_default_policy_version](./client.md#set-default-policy-version)
- [set_security_token_service_preferences](./client.md#set-security-token-service-preferences)
- [simulate_custom_policy](./client.md#simulate-custom-policy)
- [simulate_principal_policy](./client.md#simulate-principal-policy)
- [tag_instance_profile](./client.md#tag-instance-profile)
- [tag_mfa_device](./client.md#tag-mfa-device)
- [tag_open_id_connect_provider](./client.md#tag-open-id-connect-provider)
- [tag_policy](./client.md#tag-policy)
- [tag_role](./client.md#tag-role)
- [tag_saml_provider](./client.md#tag-saml-provider)
- [tag_server_certificate](./client.md#tag-server-certificate)
- [tag_user](./client.md#tag-user)
- [untag_instance_profile](./client.md#untag-instance-profile)
- [untag_mfa_device](./client.md#untag-mfa-device)
- [untag_open_id_connect_provider](./client.md#untag-open-id-connect-provider)
- [untag_policy](./client.md#untag-policy)
- [untag_role](./client.md#untag-role)
- [untag_saml_provider](./client.md#untag-saml-provider)
- [untag_server_certificate](./client.md#untag-server-certificate)
- [untag_user](./client.md#untag-user)
- [update_access_key](./client.md#update-access-key)
- [update_account_password_policy](./client.md#update-account-password-policy)
- [update_assume_role_policy](./client.md#update-assume-role-policy)
- [update_group](./client.md#update-group)
- [update_login_profile](./client.md#update-login-profile)
- [update_open_id_connect_provider_thumbprint](./client.md#update-open-id-connect-provider-thumbprint)
- [update_role](./client.md#update-role)
- [update_role_description](./client.md#update-role-description)
- [update_saml_provider](./client.md#update-saml-provider)
- [update_server_certificate](./client.md#update-server-certificate)
- [update_service_specific_credential](./client.md#update-service-specific-credential)
- [update_signing_certificate](./client.md#update-signing-certificate)
- [update_ssh_public_key](./client.md#update-ssh-public-key)
- [update_user](./client.md#update-user)
- [upload_server_certificate](./client.md#upload-server-certificate)
- [upload_signing_certificate](./client.md#upload-signing-certificate)
- [upload_ssh_public_key](./client.md#upload-ssh-public-key)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [CredentialReportExpiredException](./client.md#credentialreportexpiredexception)
- [CredentialReportNotPresentException](./client.md#credentialreportnotpresentexception)
- [CredentialReportNotReadyException](./client.md#credentialreportnotreadyexception)
- [DeleteConflictException](./client.md#deleteconflictexception)
- [DuplicateCertificateException](./client.md#duplicatecertificateexception)
- [DuplicateSSHPublicKeyException](./client.md#duplicatesshpublickeyexception)
- [EntityAlreadyExistsException](./client.md#entityalreadyexistsexception)
- [EntityTemporarilyUnmodifiableException](./client.md#entitytemporarilyunmodifiableexception)
- [InvalidAuthenticationCodeException](./client.md#invalidauthenticationcodeexception)
- [InvalidCertificateException](./client.md#invalidcertificateexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [InvalidPublicKeyException](./client.md#invalidpublickeyexception)
- [InvalidUserTypeException](./client.md#invalidusertypeexception)
- [KeyPairMismatchException](./client.md#keypairmismatchexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MalformedCertificateException](./client.md#malformedcertificateexception)
- [MalformedPolicyDocumentException](./client.md#malformedpolicydocumentexception)
- [NoSuchEntityException](./client.md#nosuchentityexception)
- [PasswordPolicyViolationException](./client.md#passwordpolicyviolationexception)
- [PolicyEvaluationException](./client.md#policyevaluationexception)
- [PolicyNotAttachableException](./client.md#policynotattachableexception)
- [ReportGenerationLimitExceededException](./client.md#reportgenerationlimitexceededexception)
- [ServiceFailureException](./client.md#servicefailureexception)
- [ServiceNotSupportedException](./client.md#servicenotsupportedexception)
- [UnmodifiableEntityException](./client.md#unmodifiableentityexception)
- [UnrecognizedPublicKeyEncodingException](./client.md#unrecognizedpublickeyencodingexception)




## IAMServiceResource

Type annotations for  `boto3.resource("iam")` as [IAMServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_iam.service_resource import IAMServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("iam").*`.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceGroupsCollection, ...
```

- [ServiceResourceGroupsCollection](./service_resource.md#iamserviceresource.groups)
- [ServiceResourceInstanceProfilesCollection](./service_resource.md#iamserviceresource.instance-profiles)
- [ServiceResourcePoliciesCollection](./service_resource.md#iamserviceresource.policies)
- [ServiceResourceRolesCollection](./service_resource.md#iamserviceresource.roles)
- [ServiceResourceSamlProvidersCollection](./service_resource.md#iamserviceresource.saml-providers)
- [ServiceResourceServerCertificatesCollection](./service_resource.md#iamserviceresource.server-certificates)
- [ServiceResourceUsersCollection](./service_resource.md#iamserviceresource.users)
- [ServiceResourceVirtualMfaDevicesCollection](./service_resource.md#iamserviceresource.virtual-mfa-devices)




### Resources

Type annotations for additional resources from `boto3.resource("iam").*`.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import AccessKey, ...
```

- [AccessKey](./service_resource.md#accesskey)
- [AccessKeyPair](./service_resource.md#accesskeypair)
- [AccountPasswordPolicy](./service_resource.md#accountpasswordpolicy)
- [AccountSummary](./service_resource.md#accountsummary)
- [AssumeRolePolicy](./service_resource.md#assumerolepolicy)
- [CurrentUser](./service_resource.md#currentuser)
- [Group](./service_resource.md#group)
- [GroupPolicy](./service_resource.md#grouppolicy)
- [InstanceProfile](./service_resource.md#instanceprofile)
- [LoginProfile](./service_resource.md#loginprofile)
- [MfaDevice](./service_resource.md#mfadevice)
- [Policy](./service_resource.md#policy)
- [PolicyVersion](./service_resource.md#policyversion)
- [Role](./service_resource.md#role)
- [RolePolicy](./service_resource.md#rolepolicy)
- [SamlProvider](./service_resource.md#samlprovider)
- [ServerCertificate](./service_resource.md#servercertificate)
- [SigningCertificate](./service_resource.md#signingcertificate)
- [User](./service_resource.md#user)
- [UserPolicy](./service_resource.md#userpolicy)
- [VirtualMfaDevice](./service_resource.md#virtualmfadevice)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iam").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iam.paginators import GetAccountAuthorizationDetailsPaginator, ...
```

- [GetAccountAuthorizationDetailsPaginator](./paginators.md#getaccountauthorizationdetailspaginator)
- [GetGroupPaginator](./paginators.md#getgrouppaginator)
- [ListAccessKeysPaginator](./paginators.md#listaccesskeyspaginator)
- [ListAccountAliasesPaginator](./paginators.md#listaccountaliasespaginator)
- [ListAttachedGroupPoliciesPaginator](./paginators.md#listattachedgrouppoliciespaginator)
- [ListAttachedRolePoliciesPaginator](./paginators.md#listattachedrolepoliciespaginator)
- [ListAttachedUserPoliciesPaginator](./paginators.md#listattacheduserpoliciespaginator)
- [ListEntitiesForPolicyPaginator](./paginators.md#listentitiesforpolicypaginator)
- [ListGroupPoliciesPaginator](./paginators.md#listgrouppoliciespaginator)
- [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- [ListGroupsForUserPaginator](./paginators.md#listgroupsforuserpaginator)
- [ListInstanceProfilesPaginator](./paginators.md#listinstanceprofilespaginator)
- [ListInstanceProfilesForRolePaginator](./paginators.md#listinstanceprofilesforrolepaginator)
- [ListMFADevicesPaginator](./paginators.md#listmfadevicespaginator)
- [ListPoliciesPaginator](./paginators.md#listpoliciespaginator)
- [ListPolicyVersionsPaginator](./paginators.md#listpolicyversionspaginator)
- [ListRolePoliciesPaginator](./paginators.md#listrolepoliciespaginator)
- [ListRolesPaginator](./paginators.md#listrolespaginator)
- [ListSSHPublicKeysPaginator](./paginators.md#listsshpublickeyspaginator)
- [ListServerCertificatesPaginator](./paginators.md#listservercertificatespaginator)
- [ListSigningCertificatesPaginator](./paginators.md#listsigningcertificatespaginator)
- [ListUserPoliciesPaginator](./paginators.md#listuserpoliciespaginator)
- [ListUsersPaginator](./paginators.md#listuserspaginator)
- [ListVirtualMFADevicesPaginator](./paginators.md#listvirtualmfadevicespaginator)
- [SimulateCustomPolicyPaginator](./paginators.md#simulatecustompolicypaginator)
- [SimulatePrincipalPolicyPaginator](./paginators.md#simulateprincipalpolicypaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("iam").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_iam.waiters import InstanceProfileExistsWaiter, ...
```

- [InstanceProfileExistsWaiter](./waiters.md#instanceprofileexistswaiter)
- [PolicyExistsWaiter](./waiters.md#policyexistswaiter)
- [RoleExistsWaiter](./waiters.md#roleexistswaiter)
- [UserExistsWaiter](./waiters.md#userexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iam.literals import AccessAdvisorUsageGranularityType, ...
```

- [AccessAdvisorUsageGranularityType](./literals.md#accessadvisorusagegranularitytype)
- [ContextKeyTypeEnum](./literals.md#contextkeytypeenum)
- [DeletionTaskStatusType](./literals.md#deletiontaskstatustype)
- [EntityType](./literals.md#entitytype)
- [GetAccountAuthorizationDetailsPaginatorName](./literals.md#getaccountauthorizationdetailspaginatorname)
- [GetGroupPaginatorName](./literals.md#getgrouppaginatorname)
- [InstanceProfileExistsWaiterName](./literals.md#instanceprofileexistswaitername)
- [ListAccessKeysPaginatorName](./literals.md#listaccesskeyspaginatorname)
- [ListAccountAliasesPaginatorName](./literals.md#listaccountaliasespaginatorname)
- [ListAttachedGroupPoliciesPaginatorName](./literals.md#listattachedgrouppoliciespaginatorname)
- [ListAttachedRolePoliciesPaginatorName](./literals.md#listattachedrolepoliciespaginatorname)
- [ListAttachedUserPoliciesPaginatorName](./literals.md#listattacheduserpoliciespaginatorname)
- [ListEntitiesForPolicyPaginatorName](./literals.md#listentitiesforpolicypaginatorname)
- [ListGroupPoliciesPaginatorName](./literals.md#listgrouppoliciespaginatorname)
- [ListGroupsForUserPaginatorName](./literals.md#listgroupsforuserpaginatorname)
- [ListGroupsPaginatorName](./literals.md#listgroupspaginatorname)
- [ListInstanceProfilesForRolePaginatorName](./literals.md#listinstanceprofilesforrolepaginatorname)
- [ListInstanceProfilesPaginatorName](./literals.md#listinstanceprofilespaginatorname)
- [ListMFADevicesPaginatorName](./literals.md#listmfadevicespaginatorname)
- [ListPoliciesPaginatorName](./literals.md#listpoliciespaginatorname)
- [ListPolicyVersionsPaginatorName](./literals.md#listpolicyversionspaginatorname)
- [ListRolePoliciesPaginatorName](./literals.md#listrolepoliciespaginatorname)
- [ListRolesPaginatorName](./literals.md#listrolespaginatorname)
- [ListSSHPublicKeysPaginatorName](./literals.md#listsshpublickeyspaginatorname)
- [ListServerCertificatesPaginatorName](./literals.md#listservercertificatespaginatorname)
- [ListSigningCertificatesPaginatorName](./literals.md#listsigningcertificatespaginatorname)
- [ListUserPoliciesPaginatorName](./literals.md#listuserpoliciespaginatorname)
- [ListUsersPaginatorName](./literals.md#listuserspaginatorname)
- [ListVirtualMFADevicesPaginatorName](./literals.md#listvirtualmfadevicespaginatorname)
- [PermissionsBoundaryAttachmentType](./literals.md#permissionsboundaryattachmenttype)
- [PolicyEvaluationDecisionType](./literals.md#policyevaluationdecisiontype)
- [PolicyExistsWaiterName](./literals.md#policyexistswaitername)
- [PolicySourceType](./literals.md#policysourcetype)
- [PolicyUsageType](./literals.md#policyusagetype)
- [ReportFormatType](./literals.md#reportformattype)
- [ReportStateType](./literals.md#reportstatetype)
- [RoleExistsWaiterName](./literals.md#roleexistswaitername)
- [SimulateCustomPolicyPaginatorName](./literals.md#simulatecustompolicypaginatorname)
- [SimulatePrincipalPolicyPaginatorName](./literals.md#simulateprincipalpolicypaginatorname)
- [UserExistsWaiterName](./literals.md#userexistswaitername)
- [assignmentStatusType](./literals.md#assignmentstatustype)
- [encodingType](./literals.md#encodingtype)
- [globalEndpointTokenVersion](./literals.md#globalendpointtokenversion)
- [jobStatusType](./literals.md#jobstatustype)
- [policyOwnerEntityType](./literals.md#policyownerentitytype)
- [policyScopeType](./literals.md#policyscopetype)
- [policyType](./literals.md#policytype)
- [sortKeyType](./literals.md#sortkeytype)
- [statusType](./literals.md#statustype)
- [summaryKeyType](./literals.md#summarykeytype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iam.type_defs import AccessDetailTypeDef, ...
```

- [AccessDetailTypeDef](./type_defs.md#accessdetailtypedef)
- [AccessKeyLastUsedTypeDef](./type_defs.md#accesskeylastusedtypedef)
- [AccessKeyMetadataTypeDef](./type_defs.md#accesskeymetadatatypedef)
- [AccessKeyTypeDef](./type_defs.md#accesskeytypedef)
- [AttachedPermissionsBoundaryTypeDef](./type_defs.md#attachedpermissionsboundarytypedef)
- [AttachedPolicyTypeDef](./type_defs.md#attachedpolicytypedef)
- [DeletionTaskFailureReasonTypeTypeDef](./type_defs.md#deletiontaskfailurereasontypetypedef)
- [EntityDetailsTypeDef](./type_defs.md#entitydetailstypedef)
- [EntityInfoTypeDef](./type_defs.md#entityinfotypedef)
- [ErrorDetailsTypeDef](./type_defs.md#errordetailstypedef)
- [EvaluationResultTypeDef](./type_defs.md#evaluationresulttypedef)
- [GroupDetailTypeDef](./type_defs.md#groupdetailtypedef)
- [GroupTypeDef](./type_defs.md#grouptypedef)
- [InstanceProfileTypeDef](./type_defs.md#instanceprofiletypedef)
- [ListPoliciesGrantingServiceAccessEntryTypeDef](./type_defs.md#listpoliciesgrantingserviceaccessentrytypedef)
- [LoginProfileTypeDef](./type_defs.md#loginprofiletypedef)
- [MFADeviceTypeDef](./type_defs.md#mfadevicetypedef)
- [ManagedPolicyDetailTypeDef](./type_defs.md#managedpolicydetailtypedef)
- [OpenIDConnectProviderListEntryTypeDef](./type_defs.md#openidconnectproviderlistentrytypedef)
- [OrganizationsDecisionDetailTypeDef](./type_defs.md#organizationsdecisiondetailtypedef)
- [PasswordPolicyTypeDef](./type_defs.md#passwordpolicytypedef)
- [PermissionsBoundaryDecisionDetailTypeDef](./type_defs.md#permissionsboundarydecisiondetailtypedef)
- [PolicyDetailTypeDef](./type_defs.md#policydetailtypedef)
- [PolicyGrantingServiceAccessTypeDef](./type_defs.md#policygrantingserviceaccesstypedef)
- [PolicyGroupTypeDef](./type_defs.md#policygrouptypedef)
- [PolicyRoleTypeDef](./type_defs.md#policyroletypedef)
- [PolicyTypeDef](./type_defs.md#policytypedef)
- [PolicyUserTypeDef](./type_defs.md#policyusertypedef)
- [PolicyVersionTypeDef](./type_defs.md#policyversiontypedef)
- [PositionTypeDef](./type_defs.md#positiontypedef)
- [ResourceSpecificResultTypeDef](./type_defs.md#resourcespecificresulttypedef)
- [RoleDetailTypeDef](./type_defs.md#roledetailtypedef)
- [RoleLastUsedTypeDef](./type_defs.md#rolelastusedtypedef)
- [RoleTypeDef](./type_defs.md#roletypedef)
- [RoleUsageTypeTypeDef](./type_defs.md#roleusagetypetypedef)
- [SAMLProviderListEntryTypeDef](./type_defs.md#samlproviderlistentrytypedef)
- [SSHPublicKeyMetadataTypeDef](./type_defs.md#sshpublickeymetadatatypedef)
- [SSHPublicKeyTypeDef](./type_defs.md#sshpublickeytypedef)
- [ServerCertificateMetadataTypeDef](./type_defs.md#servercertificatemetadatatypedef)
- [ServerCertificateTypeDef](./type_defs.md#servercertificatetypedef)
- [ServiceLastAccessedTypeDef](./type_defs.md#servicelastaccessedtypedef)
- [ServiceSpecificCredentialMetadataTypeDef](./type_defs.md#servicespecificcredentialmetadatatypedef)
- [ServiceSpecificCredentialTypeDef](./type_defs.md#servicespecificcredentialtypedef)
- [SigningCertificateTypeDef](./type_defs.md#signingcertificatetypedef)
- [StatementTypeDef](./type_defs.md#statementtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TrackedActionLastAccessedTypeDef](./type_defs.md#trackedactionlastaccessedtypedef)
- [UserDetailTypeDef](./type_defs.md#userdetailtypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
- [VirtualMFADeviceTypeDef](./type_defs.md#virtualmfadevicetypedef)
- [ContextEntryTypeDef](./type_defs.md#contextentrytypedef)
- [CreateAccessKeyResponseTypeDef](./type_defs.md#createaccesskeyresponsetypedef)
- [CreateGroupResponseTypeDef](./type_defs.md#creategroupresponsetypedef)
- [CreateInstanceProfileResponseTypeDef](./type_defs.md#createinstanceprofileresponsetypedef)
- [CreateLoginProfileResponseTypeDef](./type_defs.md#createloginprofileresponsetypedef)
- [CreateOpenIDConnectProviderResponseTypeDef](./type_defs.md#createopenidconnectproviderresponsetypedef)
- [CreatePolicyResponseTypeDef](./type_defs.md#createpolicyresponsetypedef)
- [CreatePolicyVersionResponseTypeDef](./type_defs.md#createpolicyversionresponsetypedef)
- [CreateRoleResponseTypeDef](./type_defs.md#createroleresponsetypedef)
- [CreateSAMLProviderResponseTypeDef](./type_defs.md#createsamlproviderresponsetypedef)
- [CreateServiceLinkedRoleResponseTypeDef](./type_defs.md#createservicelinkedroleresponsetypedef)
- [CreateServiceSpecificCredentialResponseTypeDef](./type_defs.md#createservicespecificcredentialresponsetypedef)
- [CreateUserResponseTypeDef](./type_defs.md#createuserresponsetypedef)
- [CreateVirtualMFADeviceResponseTypeDef](./type_defs.md#createvirtualmfadeviceresponsetypedef)
- [DeleteServiceLinkedRoleResponseTypeDef](./type_defs.md#deleteservicelinkedroleresponsetypedef)
- [GenerateCredentialReportResponseTypeDef](./type_defs.md#generatecredentialreportresponsetypedef)
- [GenerateOrganizationsAccessReportResponseTypeDef](./type_defs.md#generateorganizationsaccessreportresponsetypedef)
- [GenerateServiceLastAccessedDetailsResponseTypeDef](./type_defs.md#generateservicelastaccesseddetailsresponsetypedef)
- [GetAccessKeyLastUsedResponseTypeDef](./type_defs.md#getaccesskeylastusedresponsetypedef)
- [GetAccountAuthorizationDetailsResponseTypeDef](./type_defs.md#getaccountauthorizationdetailsresponsetypedef)
- [GetAccountPasswordPolicyResponseTypeDef](./type_defs.md#getaccountpasswordpolicyresponsetypedef)
- [GetAccountSummaryResponseTypeDef](./type_defs.md#getaccountsummaryresponsetypedef)
- [GetContextKeysForPolicyResponseTypeDef](./type_defs.md#getcontextkeysforpolicyresponsetypedef)
- [GetCredentialReportResponseTypeDef](./type_defs.md#getcredentialreportresponsetypedef)
- [GetGroupPolicyResponseTypeDef](./type_defs.md#getgrouppolicyresponsetypedef)
- [GetGroupResponseTypeDef](./type_defs.md#getgroupresponsetypedef)
- [GetInstanceProfileResponseTypeDef](./type_defs.md#getinstanceprofileresponsetypedef)
- [GetLoginProfileResponseTypeDef](./type_defs.md#getloginprofileresponsetypedef)
- [GetOpenIDConnectProviderResponseTypeDef](./type_defs.md#getopenidconnectproviderresponsetypedef)
- [GetOrganizationsAccessReportResponseTypeDef](./type_defs.md#getorganizationsaccessreportresponsetypedef)
- [GetPolicyResponseTypeDef](./type_defs.md#getpolicyresponsetypedef)
- [GetPolicyVersionResponseTypeDef](./type_defs.md#getpolicyversionresponsetypedef)
- [GetRolePolicyResponseTypeDef](./type_defs.md#getrolepolicyresponsetypedef)
- [GetRoleResponseTypeDef](./type_defs.md#getroleresponsetypedef)
- [GetSAMLProviderResponseTypeDef](./type_defs.md#getsamlproviderresponsetypedef)
- [GetSSHPublicKeyResponseTypeDef](./type_defs.md#getsshpublickeyresponsetypedef)
- [GetServerCertificateResponseTypeDef](./type_defs.md#getservercertificateresponsetypedef)
- [GetServiceLastAccessedDetailsResponseTypeDef](./type_defs.md#getservicelastaccesseddetailsresponsetypedef)
- [GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef](./type_defs.md#getservicelastaccesseddetailswithentitiesresponsetypedef)
- [GetServiceLinkedRoleDeletionStatusResponseTypeDef](./type_defs.md#getservicelinkedroledeletionstatusresponsetypedef)
- [GetUserPolicyResponseTypeDef](./type_defs.md#getuserpolicyresponsetypedef)
- [GetUserResponseTypeDef](./type_defs.md#getuserresponsetypedef)
- [ListAccessKeysResponseTypeDef](./type_defs.md#listaccesskeysresponsetypedef)
- [ListAccountAliasesResponseTypeDef](./type_defs.md#listaccountaliasesresponsetypedef)
- [ListAttachedGroupPoliciesResponseTypeDef](./type_defs.md#listattachedgrouppoliciesresponsetypedef)
- [ListAttachedRolePoliciesResponseTypeDef](./type_defs.md#listattachedrolepoliciesresponsetypedef)
- [ListAttachedUserPoliciesResponseTypeDef](./type_defs.md#listattacheduserpoliciesresponsetypedef)
- [ListEntitiesForPolicyResponseTypeDef](./type_defs.md#listentitiesforpolicyresponsetypedef)
- [ListGroupPoliciesResponseTypeDef](./type_defs.md#listgrouppoliciesresponsetypedef)
- [ListGroupsForUserResponseTypeDef](./type_defs.md#listgroupsforuserresponsetypedef)
- [ListGroupsResponseTypeDef](./type_defs.md#listgroupsresponsetypedef)
- [ListInstanceProfileTagsResponseTypeDef](./type_defs.md#listinstanceprofiletagsresponsetypedef)
- [ListInstanceProfilesForRoleResponseTypeDef](./type_defs.md#listinstanceprofilesforroleresponsetypedef)
- [ListInstanceProfilesResponseTypeDef](./type_defs.md#listinstanceprofilesresponsetypedef)
- [ListMFADeviceTagsResponseTypeDef](./type_defs.md#listmfadevicetagsresponsetypedef)
- [ListMFADevicesResponseTypeDef](./type_defs.md#listmfadevicesresponsetypedef)
- [ListOpenIDConnectProviderTagsResponseTypeDef](./type_defs.md#listopenidconnectprovidertagsresponsetypedef)
- [ListOpenIDConnectProvidersResponseTypeDef](./type_defs.md#listopenidconnectprovidersresponsetypedef)
- [ListPoliciesGrantingServiceAccessResponseTypeDef](./type_defs.md#listpoliciesgrantingserviceaccessresponsetypedef)
- [ListPoliciesResponseTypeDef](./type_defs.md#listpoliciesresponsetypedef)
- [ListPolicyTagsResponseTypeDef](./type_defs.md#listpolicytagsresponsetypedef)
- [ListPolicyVersionsResponseTypeDef](./type_defs.md#listpolicyversionsresponsetypedef)
- [ListRolePoliciesResponseTypeDef](./type_defs.md#listrolepoliciesresponsetypedef)
- [ListRoleTagsResponseTypeDef](./type_defs.md#listroletagsresponsetypedef)
- [ListRolesResponseTypeDef](./type_defs.md#listrolesresponsetypedef)
- [ListSAMLProviderTagsResponseTypeDef](./type_defs.md#listsamlprovidertagsresponsetypedef)
- [ListSAMLProvidersResponseTypeDef](./type_defs.md#listsamlprovidersresponsetypedef)
- [ListSSHPublicKeysResponseTypeDef](./type_defs.md#listsshpublickeysresponsetypedef)
- [ListServerCertificateTagsResponseTypeDef](./type_defs.md#listservercertificatetagsresponsetypedef)
- [ListServerCertificatesResponseTypeDef](./type_defs.md#listservercertificatesresponsetypedef)
- [ListServiceSpecificCredentialsResponseTypeDef](./type_defs.md#listservicespecificcredentialsresponsetypedef)
- [ListSigningCertificatesResponseTypeDef](./type_defs.md#listsigningcertificatesresponsetypedef)
- [ListUserPoliciesResponseTypeDef](./type_defs.md#listuserpoliciesresponsetypedef)
- [ListUserTagsResponseTypeDef](./type_defs.md#listusertagsresponsetypedef)
- [ListUsersResponseTypeDef](./type_defs.md#listusersresponsetypedef)
- [ListVirtualMFADevicesResponseTypeDef](./type_defs.md#listvirtualmfadevicesresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResetServiceSpecificCredentialResponseTypeDef](./type_defs.md#resetservicespecificcredentialresponsetypedef)
- [SimulatePolicyResponseTypeDef](./type_defs.md#simulatepolicyresponsetypedef)
- [UpdateRoleDescriptionResponseTypeDef](./type_defs.md#updateroledescriptionresponsetypedef)
- [UpdateSAMLProviderResponseTypeDef](./type_defs.md#updatesamlproviderresponsetypedef)
- [UploadSSHPublicKeyResponseTypeDef](./type_defs.md#uploadsshpublickeyresponsetypedef)
- [UploadServerCertificateResponseTypeDef](./type_defs.md#uploadservercertificateresponsetypedef)
- [UploadSigningCertificateResponseTypeDef](./type_defs.md#uploadsigningcertificateresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
