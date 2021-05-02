# IAMClient for boto3 IAM module

> [Index](../index.md) > [IAM](./index.md) > IAMClient

Auto-generated documentation for [IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM)
type annotations stubs module [mypy_boto3_iam](https://pypi.org/project/mypy-boto3-iam/).

- [IAMClient for boto3 IAM module](#iamclient-for-boto3-iam-module)
  - [IAMClient](#iamclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_client_id_to_open_id_connect_provider](#add_client_id_to_open_id_connect_provider)
    - [add_role_to_instance_profile](#add_role_to_instance_profile)
    - [add_user_to_group](#add_user_to_group)
    - [attach_group_policy](#attach_group_policy)
    - [attach_role_policy](#attach_role_policy)
    - [attach_user_policy](#attach_user_policy)
    - [can_paginate](#can_paginate)
    - [change_password](#change_password)
    - [create_access_key](#create_access_key)
    - [create_account_alias](#create_account_alias)
    - [create_group](#create_group)
    - [create_instance_profile](#create_instance_profile)
    - [create_login_profile](#create_login_profile)
    - [create_open_id_connect_provider](#create_open_id_connect_provider)
    - [create_policy](#create_policy)
    - [create_policy_version](#create_policy_version)
    - [create_role](#create_role)
    - [create_saml_provider](#create_saml_provider)
    - [create_service_linked_role](#create_service_linked_role)
    - [create_service_specific_credential](#create_service_specific_credential)
    - [create_user](#create_user)
    - [create_virtual_mfa_device](#create_virtual_mfa_device)
    - [deactivate_mfa_device](#deactivate_mfa_device)
    - [delete_access_key](#delete_access_key)
    - [delete_account_alias](#delete_account_alias)
    - [delete_account_password_policy](#delete_account_password_policy)
    - [delete_group](#delete_group)
    - [delete_group_policy](#delete_group_policy)
    - [delete_instance_profile](#delete_instance_profile)
    - [delete_login_profile](#delete_login_profile)
    - [delete_open_id_connect_provider](#delete_open_id_connect_provider)
    - [delete_policy](#delete_policy)
    - [delete_policy_version](#delete_policy_version)
    - [delete_role](#delete_role)
    - [delete_role_permissions_boundary](#delete_role_permissions_boundary)
    - [delete_role_policy](#delete_role_policy)
    - [delete_saml_provider](#delete_saml_provider)
    - [delete_server_certificate](#delete_server_certificate)
    - [delete_service_linked_role](#delete_service_linked_role)
    - [delete_service_specific_credential](#delete_service_specific_credential)
    - [delete_signing_certificate](#delete_signing_certificate)
    - [delete_ssh_public_key](#delete_ssh_public_key)
    - [delete_user](#delete_user)
    - [delete_user_permissions_boundary](#delete_user_permissions_boundary)
    - [delete_user_policy](#delete_user_policy)
    - [delete_virtual_mfa_device](#delete_virtual_mfa_device)
    - [detach_group_policy](#detach_group_policy)
    - [detach_role_policy](#detach_role_policy)
    - [detach_user_policy](#detach_user_policy)
    - [enable_mfa_device](#enable_mfa_device)
    - [generate_credential_report](#generate_credential_report)
    - [generate_organizations_access_report](#generate_organizations_access_report)
    - [generate_presigned_url](#generate_presigned_url)
    - [generate_service_last_accessed_details](#generate_service_last_accessed_details)
    - [get_access_key_last_used](#get_access_key_last_used)
    - [get_account_authorization_details](#get_account_authorization_details)
    - [get_account_password_policy](#get_account_password_policy)
    - [get_account_summary](#get_account_summary)
    - [get_context_keys_for_custom_policy](#get_context_keys_for_custom_policy)
    - [get_context_keys_for_principal_policy](#get_context_keys_for_principal_policy)
    - [get_credential_report](#get_credential_report)
    - [get_group](#get_group)
    - [get_group_policy](#get_group_policy)
    - [get_instance_profile](#get_instance_profile)
    - [get_login_profile](#get_login_profile)
    - [get_open_id_connect_provider](#get_open_id_connect_provider)
    - [get_organizations_access_report](#get_organizations_access_report)
    - [get_policy](#get_policy)
    - [get_policy_version](#get_policy_version)
    - [get_role](#get_role)
    - [get_role_policy](#get_role_policy)
    - [get_saml_provider](#get_saml_provider)
    - [get_server_certificate](#get_server_certificate)
    - [get_service_last_accessed_details](#get_service_last_accessed_details)
    - [get_service_last_accessed_details_with_entities](#get_service_last_accessed_details_with_entities)
    - [get_service_linked_role_deletion_status](#get_service_linked_role_deletion_status)
    - [get_ssh_public_key](#get_ssh_public_key)
    - [get_user](#get_user)
    - [get_user_policy](#get_user_policy)
    - [list_access_keys](#list_access_keys)
    - [list_account_aliases](#list_account_aliases)
    - [list_attached_group_policies](#list_attached_group_policies)
    - [list_attached_role_policies](#list_attached_role_policies)
    - [list_attached_user_policies](#list_attached_user_policies)
    - [list_entities_for_policy](#list_entities_for_policy)
    - [list_group_policies](#list_group_policies)
    - [list_groups](#list_groups)
    - [list_groups_for_user](#list_groups_for_user)
    - [list_instance_profile_tags](#list_instance_profile_tags)
    - [list_instance_profiles](#list_instance_profiles)
    - [list_instance_profiles_for_role](#list_instance_profiles_for_role)
    - [list_mfa_device_tags](#list_mfa_device_tags)
    - [list_mfa_devices](#list_mfa_devices)
    - [list_open_id_connect_provider_tags](#list_open_id_connect_provider_tags)
    - [list_open_id_connect_providers](#list_open_id_connect_providers)
    - [list_policies](#list_policies)
    - [list_policies_granting_service_access](#list_policies_granting_service_access)
    - [list_policy_tags](#list_policy_tags)
    - [list_policy_versions](#list_policy_versions)
    - [list_role_policies](#list_role_policies)
    - [list_role_tags](#list_role_tags)
    - [list_roles](#list_roles)
    - [list_saml_provider_tags](#list_saml_provider_tags)
    - [list_saml_providers](#list_saml_providers)
    - [list_server_certificate_tags](#list_server_certificate_tags)
    - [list_server_certificates](#list_server_certificates)
    - [list_service_specific_credentials](#list_service_specific_credentials)
    - [list_signing_certificates](#list_signing_certificates)
    - [list_ssh_public_keys](#list_ssh_public_keys)
    - [list_user_policies](#list_user_policies)
    - [list_user_tags](#list_user_tags)
    - [list_users](#list_users)
    - [list_virtual_mfa_devices](#list_virtual_mfa_devices)
    - [put_group_policy](#put_group_policy)
    - [put_role_permissions_boundary](#put_role_permissions_boundary)
    - [put_role_policy](#put_role_policy)
    - [put_user_permissions_boundary](#put_user_permissions_boundary)
    - [put_user_policy](#put_user_policy)
    - [remove_client_id_from_open_id_connect_provider](#remove_client_id_from_open_id_connect_provider)
    - [remove_role_from_instance_profile](#remove_role_from_instance_profile)
    - [remove_user_from_group](#remove_user_from_group)
    - [reset_service_specific_credential](#reset_service_specific_credential)
    - [resync_mfa_device](#resync_mfa_device)
    - [set_default_policy_version](#set_default_policy_version)
    - [set_security_token_service_preferences](#set_security_token_service_preferences)
    - [simulate_custom_policy](#simulate_custom_policy)
    - [simulate_principal_policy](#simulate_principal_policy)
    - [tag_instance_profile](#tag_instance_profile)
    - [tag_mfa_device](#tag_mfa_device)
    - [tag_open_id_connect_provider](#tag_open_id_connect_provider)
    - [tag_policy](#tag_policy)
    - [tag_role](#tag_role)
    - [tag_saml_provider](#tag_saml_provider)
    - [tag_server_certificate](#tag_server_certificate)
    - [tag_user](#tag_user)
    - [untag_instance_profile](#untag_instance_profile)
    - [untag_mfa_device](#untag_mfa_device)
    - [untag_open_id_connect_provider](#untag_open_id_connect_provider)
    - [untag_policy](#untag_policy)
    - [untag_role](#untag_role)
    - [untag_saml_provider](#untag_saml_provider)
    - [untag_server_certificate](#untag_server_certificate)
    - [untag_user](#untag_user)
    - [update_access_key](#update_access_key)
    - [update_account_password_policy](#update_account_password_policy)
    - [update_assume_role_policy](#update_assume_role_policy)
    - [update_group](#update_group)
    - [update_login_profile](#update_login_profile)
    - [update_open_id_connect_provider_thumbprint](#update_open_id_connect_provider_thumbprint)
    - [update_role](#update_role)
    - [update_role_description](#update_role_description)
    - [update_saml_provider](#update_saml_provider)
    - [update_server_certificate](#update_server_certificate)
    - [update_service_specific_credential](#update_service_specific_credential)
    - [update_signing_certificate](#update_signing_certificate)
    - [update_ssh_public_key](#update_ssh_public_key)
    - [update_user](#update_user)
    - [upload_server_certificate](#upload_server_certificate)
    - [upload_signing_certificate](#upload_signing_certificate)
    - [upload_ssh_public_key](#upload_ssh_public_key)
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
    - [get_paginator](#get_paginator-22)
    - [get_paginator](#get_paginator-23)
    - [get_paginator](#get_paginator-24)
    - [get_paginator](#get_paginator-25)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)

## IAMClient

Type annotations for `boto3.client("iam")`

Can be used directly:

```python
from mypy_boto3_iam.client import IAMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iam.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.CredentialReportExpiredException`
- `Exceptions.CredentialReportNotPresentException`
- `Exceptions.CredentialReportNotReadyException`
- `Exceptions.DeleteConflictException`
- `Exceptions.DuplicateCertificateException`
- `Exceptions.DuplicateSSHPublicKeyException`
- `Exceptions.EntityAlreadyExistsException`
- `Exceptions.EntityTemporarilyUnmodifiableException`
- `Exceptions.InvalidAuthenticationCodeException`
- `Exceptions.InvalidCertificateException`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidPublicKeyException`
- `Exceptions.InvalidUserTypeException`
- `Exceptions.KeyPairMismatchException`
- `Exceptions.LimitExceededException`
- `Exceptions.MalformedCertificateException`
- `Exceptions.MalformedPolicyDocumentException`
- `Exceptions.NoSuchEntityException`
- `Exceptions.PasswordPolicyViolationException`
- `Exceptions.PolicyEvaluationException`
- `Exceptions.PolicyNotAttachableException`
- `Exceptions.ReportGenerationLimitExceededException`
- `Exceptions.ServiceFailureException`
- `Exceptions.ServiceNotSupportedException`
- `Exceptions.UnmodifiableEntityException`
- `Exceptions.UnrecognizedPublicKeyEncodingException`


## Methods


### add_client_id_to_open_id_connect_provider

Type annotations for `boto3.client("iam").add_client_id_to_open_id_connect_provider` method.

[Client.add_client_id_to_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.add_client_id_to_open_id_connect_provider)

```python
def add_client_id_to_open_id_connect_provider(
    self,
    OpenIDConnectProviderArn: str,
    ClientID: str
) -> None:
    pass
```

### add_role_to_instance_profile

Type annotations for `boto3.client("iam").add_role_to_instance_profile` method.

[Client.add_role_to_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.add_role_to_instance_profile)

```python
def add_role_to_instance_profile(
    self,
    InstanceProfileName: str,
    RoleName: str
) -> None:
    pass
```

### add_user_to_group

Type annotations for `boto3.client("iam").add_user_to_group` method.

[Client.add_user_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.add_user_to_group)

```python
def add_user_to_group(
    self,
    GroupName: str,
    UserName: str
) -> None:
    pass
```

### attach_group_policy

Type annotations for `boto3.client("iam").attach_group_policy` method.

[Client.attach_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_group_policy)

```python
def attach_group_policy(
    self,
    GroupName: str,
    PolicyArn: str
) -> None:
    pass
```

### attach_role_policy

Type annotations for `boto3.client("iam").attach_role_policy` method.

[Client.attach_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_role_policy)

```python
def attach_role_policy(
    self,
    RoleName: str,
    PolicyArn: str
) -> None:
    pass
```

### attach_user_policy

Type annotations for `boto3.client("iam").attach_user_policy` method.

[Client.attach_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.attach_user_policy)

```python
def attach_user_policy(
    self,
    UserName: str,
    PolicyArn: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("iam").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### change_password

Type annotations for `boto3.client("iam").change_password` method.

[Client.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.change_password)

```python
def change_password(
    self,
    OldPassword: str,
    NewPassword: str
) -> None:
    pass
```

### create_access_key

Type annotations for `boto3.client("iam").create_access_key` method.

[Client.create_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_access_key)

```python
def create_access_key(
    self,
    UserName: str = None
) -> CreateAccessKeyResponseTypeDef:
    pass
```

### create_account_alias

Type annotations for `boto3.client("iam").create_account_alias` method.

[Client.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_account_alias)

```python
def create_account_alias(
    self,
    AccountAlias: str
) -> None:
    pass
```

### create_group

Type annotations for `boto3.client("iam").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_group)

```python
def create_group(
    self,
    GroupName: str,
    Path: str = None
) -> CreateGroupResponseTypeDef:
    pass
```

### create_instance_profile

Type annotations for `boto3.client("iam").create_instance_profile` method.

[Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_instance_profile)

```python
def create_instance_profile(
    self,
    InstanceProfileName: str,
    Path: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateInstanceProfileResponseTypeDef:
    pass
```

### create_login_profile

Type annotations for `boto3.client("iam").create_login_profile` method.

[Client.create_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_login_profile)

```python
def create_login_profile(
    self,
    UserName: str,
    Password: str,
    PasswordResetRequired: bool = None
) -> CreateLoginProfileResponseTypeDef:
    pass
```

### create_open_id_connect_provider

Type annotations for `boto3.client("iam").create_open_id_connect_provider` method.

[Client.create_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_open_id_connect_provider)

```python
def create_open_id_connect_provider(
    self,
    Url: str,
    ThumbprintList: List[str],
    ClientIDList: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateOpenIDConnectProviderResponseTypeDef:
    pass
```

### create_policy

Type annotations for `boto3.client("iam").create_policy` method.

[Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_policy)

```python
def create_policy(
    self,
    PolicyName: str,
    PolicyDocument: str,
    Path: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePolicyResponseTypeDef:
    pass
```

### create_policy_version

Type annotations for `boto3.client("iam").create_policy_version` method.

[Client.create_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_policy_version)

```python
def create_policy_version(
    self,
    PolicyArn: str,
    PolicyDocument: str,
    SetAsDefault: bool = None
) -> CreatePolicyVersionResponseTypeDef:
    pass
```

### create_role

Type annotations for `boto3.client("iam").create_role` method.

[Client.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_role)

```python
def create_role(
    self,
    RoleName: str,
    AssumeRolePolicyDocument: str,
    Path: str = None,
    Description: str = None,
    MaxSessionDuration: int = None,
    PermissionsBoundary: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateRoleResponseTypeDef:
    pass
```

### create_saml_provider

Type annotations for `boto3.client("iam").create_saml_provider` method.

[Client.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_saml_provider)

```python
def create_saml_provider(
    self,
    SAMLMetadataDocument: str,
    Name: str,
    Tags: List["TagTypeDef"] = None
) -> CreateSAMLProviderResponseTypeDef:
    pass
```

### create_service_linked_role

Type annotations for `boto3.client("iam").create_service_linked_role` method.

[Client.create_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_service_linked_role)

```python
def create_service_linked_role(
    self,
    AWSServiceName: str,
    Description: str = None,
    CustomSuffix: str = None
) -> CreateServiceLinkedRoleResponseTypeDef:
    pass
```

### create_service_specific_credential

Type annotations for `boto3.client("iam").create_service_specific_credential` method.

[Client.create_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_service_specific_credential)

```python
def create_service_specific_credential(
    self,
    UserName: str,
    ServiceName: str
) -> CreateServiceSpecificCredentialResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("iam").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_user)

```python
def create_user(
    self,
    UserName: str,
    Path: str = None,
    PermissionsBoundary: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateUserResponseTypeDef:
    pass
```

### create_virtual_mfa_device

Type annotations for `boto3.client("iam").create_virtual_mfa_device` method.

[Client.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_virtual_mfa_device)

```python
def create_virtual_mfa_device(
    self,
    VirtualMFADeviceName: str,
    Path: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateVirtualMFADeviceResponseTypeDef:
    pass
```

### deactivate_mfa_device

Type annotations for `boto3.client("iam").deactivate_mfa_device` method.

[Client.deactivate_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.deactivate_mfa_device)

```python
def deactivate_mfa_device(
    self,
    UserName: str,
    SerialNumber: str
) -> None:
    pass
```

### delete_access_key

Type annotations for `boto3.client("iam").delete_access_key` method.

[Client.delete_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_access_key)

```python
def delete_access_key(
    self,
    AccessKeyId: str,
    UserName: str = None
) -> None:
    pass
```

### delete_account_alias

Type annotations for `boto3.client("iam").delete_account_alias` method.

[Client.delete_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_account_alias)

```python
def delete_account_alias(
    self,
    AccountAlias: str
) -> None:
    pass
```

### delete_account_password_policy

Type annotations for `boto3.client("iam").delete_account_password_policy` method.

[Client.delete_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_account_password_policy)

```python
def delete_account_password_policy(
    self
) -> None:
    pass
```

### delete_group

Type annotations for `boto3.client("iam").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_group)

```python
def delete_group(
    self,
    GroupName: str
) -> None:
    pass
```

### delete_group_policy

Type annotations for `boto3.client("iam").delete_group_policy` method.

[Client.delete_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_group_policy)

```python
def delete_group_policy(
    self,
    GroupName: str,
    PolicyName: str
) -> None:
    pass
```

### delete_instance_profile

Type annotations for `boto3.client("iam").delete_instance_profile` method.

[Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_instance_profile)

```python
def delete_instance_profile(
    self,
    InstanceProfileName: str
) -> None:
    pass
```

### delete_login_profile

Type annotations for `boto3.client("iam").delete_login_profile` method.

[Client.delete_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_login_profile)

```python
def delete_login_profile(
    self,
    UserName: str
) -> None:
    pass
```

### delete_open_id_connect_provider

Type annotations for `boto3.client("iam").delete_open_id_connect_provider` method.

[Client.delete_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_open_id_connect_provider)

```python
def delete_open_id_connect_provider(
    self,
    OpenIDConnectProviderArn: str
) -> None:
    pass
```

### delete_policy

Type annotations for `boto3.client("iam").delete_policy` method.

[Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_policy)

```python
def delete_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

### delete_policy_version

Type annotations for `boto3.client("iam").delete_policy_version` method.

[Client.delete_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_policy_version)

```python
def delete_policy_version(
    self,
    PolicyArn: str,
    VersionId: str
) -> None:
    pass
```

### delete_role

Type annotations for `boto3.client("iam").delete_role` method.

[Client.delete_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_role)

```python
def delete_role(
    self,
    RoleName: str
) -> None:
    pass
```

### delete_role_permissions_boundary

Type annotations for `boto3.client("iam").delete_role_permissions_boundary` method.

[Client.delete_role_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_role_permissions_boundary)

```python
def delete_role_permissions_boundary(
    self,
    RoleName: str
) -> None:
    pass
```

### delete_role_policy

Type annotations for `boto3.client("iam").delete_role_policy` method.

[Client.delete_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_role_policy)

```python
def delete_role_policy(
    self,
    RoleName: str,
    PolicyName: str
) -> None:
    pass
```

### delete_saml_provider

Type annotations for `boto3.client("iam").delete_saml_provider` method.

[Client.delete_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_saml_provider)

```python
def delete_saml_provider(
    self,
    SAMLProviderArn: str
) -> None:
    pass
```

### delete_server_certificate

Type annotations for `boto3.client("iam").delete_server_certificate` method.

[Client.delete_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_server_certificate)

```python
def delete_server_certificate(
    self,
    ServerCertificateName: str
) -> None:
    pass
```

### delete_service_linked_role

Type annotations for `boto3.client("iam").delete_service_linked_role` method.

[Client.delete_service_linked_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_service_linked_role)

```python
def delete_service_linked_role(
    self,
    RoleName: str
) -> DeleteServiceLinkedRoleResponseTypeDef:
    pass
```

### delete_service_specific_credential

Type annotations for `boto3.client("iam").delete_service_specific_credential` method.

[Client.delete_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_service_specific_credential)

```python
def delete_service_specific_credential(
    self,
    ServiceSpecificCredentialId: str,
    UserName: str = None
) -> None:
    pass
```

### delete_signing_certificate

Type annotations for `boto3.client("iam").delete_signing_certificate` method.

[Client.delete_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_signing_certificate)

```python
def delete_signing_certificate(
    self,
    CertificateId: str,
    UserName: str = None
) -> None:
    pass
```

### delete_ssh_public_key

Type annotations for `boto3.client("iam").delete_ssh_public_key` method.

[Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_ssh_public_key)

```python
def delete_ssh_public_key(
    self,
    UserName: str,
    SSHPublicKeyId: str
) -> None:
    pass
```

### delete_user

Type annotations for `boto3.client("iam").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_user)

```python
def delete_user(
    self,
    UserName: str
) -> None:
    pass
```

### delete_user_permissions_boundary

Type annotations for `boto3.client("iam").delete_user_permissions_boundary` method.

[Client.delete_user_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_user_permissions_boundary)

```python
def delete_user_permissions_boundary(
    self,
    UserName: str
) -> None:
    pass
```

### delete_user_policy

Type annotations for `boto3.client("iam").delete_user_policy` method.

[Client.delete_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_user_policy)

```python
def delete_user_policy(
    self,
    UserName: str,
    PolicyName: str
) -> None:
    pass
```

### delete_virtual_mfa_device

Type annotations for `boto3.client("iam").delete_virtual_mfa_device` method.

[Client.delete_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.delete_virtual_mfa_device)

```python
def delete_virtual_mfa_device(
    self,
    SerialNumber: str
) -> None:
    pass
```

### detach_group_policy

Type annotations for `boto3.client("iam").detach_group_policy` method.

[Client.detach_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.detach_group_policy)

```python
def detach_group_policy(
    self,
    GroupName: str,
    PolicyArn: str
) -> None:
    pass
```

### detach_role_policy

Type annotations for `boto3.client("iam").detach_role_policy` method.

[Client.detach_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.detach_role_policy)

```python
def detach_role_policy(
    self,
    RoleName: str,
    PolicyArn: str
) -> None:
    pass
```

### detach_user_policy

Type annotations for `boto3.client("iam").detach_user_policy` method.

[Client.detach_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.detach_user_policy)

```python
def detach_user_policy(
    self,
    UserName: str,
    PolicyArn: str
) -> None:
    pass
```

### enable_mfa_device

Type annotations for `boto3.client("iam").enable_mfa_device` method.

[Client.enable_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.enable_mfa_device)

```python
def enable_mfa_device(
    self,
    UserName: str,
    SerialNumber: str,
    AuthenticationCode1: str,
    AuthenticationCode2: str
) -> None:
    pass
```

### generate_credential_report

Type annotations for `boto3.client("iam").generate_credential_report` method.

[Client.generate_credential_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.generate_credential_report)

```python
def generate_credential_report(
    self
) -> GenerateCredentialReportResponseTypeDef:
    pass
```

### generate_organizations_access_report

Type annotations for `boto3.client("iam").generate_organizations_access_report` method.

[Client.generate_organizations_access_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.generate_organizations_access_report)

```python
def generate_organizations_access_report(
    self,
    EntityPath: str,
    OrganizationsPolicyId: str = None
) -> GenerateOrganizationsAccessReportResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iam").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.generate_presigned_url)

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

### generate_service_last_accessed_details

Type annotations for `boto3.client("iam").generate_service_last_accessed_details` method.

[Client.generate_service_last_accessed_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.generate_service_last_accessed_details)

```python
def generate_service_last_accessed_details(
    self,
    Arn: str,
    Granularity: AccessAdvisorUsageGranularityType = None
) -> GenerateServiceLastAccessedDetailsResponseTypeDef:
    pass
```

### get_access_key_last_used

Type annotations for `boto3.client("iam").get_access_key_last_used` method.

[Client.get_access_key_last_used documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_access_key_last_used)

```python
def get_access_key_last_used(
    self,
    AccessKeyId: str
) -> GetAccessKeyLastUsedResponseTypeDef:
    pass
```

### get_account_authorization_details

Type annotations for `boto3.client("iam").get_account_authorization_details` method.

[Client.get_account_authorization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_account_authorization_details)

```python
def get_account_authorization_details(
    self,
    Filter: List[EntityType] = None,
    MaxItems: int = None,
    Marker: str = None
) -> GetAccountAuthorizationDetailsResponseTypeDef:
    pass
```

### get_account_password_policy

Type annotations for `boto3.client("iam").get_account_password_policy` method.

[Client.get_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_account_password_policy)

```python
def get_account_password_policy(
    self
) -> GetAccountPasswordPolicyResponseTypeDef:
    pass
```

### get_account_summary

Type annotations for `boto3.client("iam").get_account_summary` method.

[Client.get_account_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_account_summary)

```python
def get_account_summary(
    self
) -> GetAccountSummaryResponseTypeDef:
    pass
```

### get_context_keys_for_custom_policy

Type annotations for `boto3.client("iam").get_context_keys_for_custom_policy` method.

[Client.get_context_keys_for_custom_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_context_keys_for_custom_policy)

```python
def get_context_keys_for_custom_policy(
    self,
    PolicyInputList: List[str]
) -> GetContextKeysForPolicyResponseTypeDef:
    pass
```

### get_context_keys_for_principal_policy

Type annotations for `boto3.client("iam").get_context_keys_for_principal_policy` method.

[Client.get_context_keys_for_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_context_keys_for_principal_policy)

```python
def get_context_keys_for_principal_policy(
    self,
    PolicySourceArn: str,
    PolicyInputList: List[str] = None
) -> GetContextKeysForPolicyResponseTypeDef:
    pass
```

### get_credential_report

Type annotations for `boto3.client("iam").get_credential_report` method.

[Client.get_credential_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_credential_report)

```python
def get_credential_report(
    self
) -> GetCredentialReportResponseTypeDef:
    pass
```

### get_group

Type annotations for `boto3.client("iam").get_group` method.

[Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_group)

```python
def get_group(
    self,
    GroupName: str,
    Marker: str = None,
    MaxItems: int = None
) -> GetGroupResponseTypeDef:
    pass
```

### get_group_policy

Type annotations for `boto3.client("iam").get_group_policy` method.

[Client.get_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_group_policy)

```python
def get_group_policy(
    self,
    GroupName: str,
    PolicyName: str
) -> GetGroupPolicyResponseTypeDef:
    pass
```

### get_instance_profile

Type annotations for `boto3.client("iam").get_instance_profile` method.

[Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_instance_profile)

```python
def get_instance_profile(
    self,
    InstanceProfileName: str
) -> GetInstanceProfileResponseTypeDef:
    pass
```

### get_login_profile

Type annotations for `boto3.client("iam").get_login_profile` method.

[Client.get_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_login_profile)

```python
def get_login_profile(
    self,
    UserName: str
) -> GetLoginProfileResponseTypeDef:
    pass
```

### get_open_id_connect_provider

Type annotations for `boto3.client("iam").get_open_id_connect_provider` method.

[Client.get_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_open_id_connect_provider)

```python
def get_open_id_connect_provider(
    self,
    OpenIDConnectProviderArn: str
) -> GetOpenIDConnectProviderResponseTypeDef:
    pass
```

### get_organizations_access_report

Type annotations for `boto3.client("iam").get_organizations_access_report` method.

[Client.get_organizations_access_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_organizations_access_report)

```python
def get_organizations_access_report(
    self,
    JobId: str,
    MaxItems: int = None,
    Marker: str = None,
    SortKey: sortKeyType = None
) -> GetOrganizationsAccessReportResponseTypeDef:
    pass
```

### get_policy

Type annotations for `boto3.client("iam").get_policy` method.

[Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_policy)

```python
def get_policy(
    self,
    PolicyArn: str
) -> GetPolicyResponseTypeDef:
    pass
```

### get_policy_version

Type annotations for `boto3.client("iam").get_policy_version` method.

[Client.get_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_policy_version)

```python
def get_policy_version(
    self,
    PolicyArn: str,
    VersionId: str
) -> GetPolicyVersionResponseTypeDef:
    pass
```

### get_role

Type annotations for `boto3.client("iam").get_role` method.

[Client.get_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_role)

```python
def get_role(
    self,
    RoleName: str
) -> GetRoleResponseTypeDef:
    pass
```

### get_role_policy

Type annotations for `boto3.client("iam").get_role_policy` method.

[Client.get_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_role_policy)

```python
def get_role_policy(
    self,
    RoleName: str,
    PolicyName: str
) -> GetRolePolicyResponseTypeDef:
    pass
```

### get_saml_provider

Type annotations for `boto3.client("iam").get_saml_provider` method.

[Client.get_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_saml_provider)

```python
def get_saml_provider(
    self,
    SAMLProviderArn: str
) -> GetSAMLProviderResponseTypeDef:
    pass
```

### get_server_certificate

Type annotations for `boto3.client("iam").get_server_certificate` method.

[Client.get_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_server_certificate)

```python
def get_server_certificate(
    self,
    ServerCertificateName: str
) -> GetServerCertificateResponseTypeDef:
    pass
```

### get_service_last_accessed_details

Type annotations for `boto3.client("iam").get_service_last_accessed_details` method.

[Client.get_service_last_accessed_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_service_last_accessed_details)

```python
def get_service_last_accessed_details(
    self,
    JobId: str,
    MaxItems: int = None,
    Marker: str = None
) -> GetServiceLastAccessedDetailsResponseTypeDef:
    pass
```

### get_service_last_accessed_details_with_entities

Type annotations for `boto3.client("iam").get_service_last_accessed_details_with_entities` method.

[Client.get_service_last_accessed_details_with_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_service_last_accessed_details_with_entities)

```python
def get_service_last_accessed_details_with_entities(
    self,
    JobId: str,
    ServiceNamespace: str,
    MaxItems: int = None,
    Marker: str = None
) -> GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef:
    pass
```

### get_service_linked_role_deletion_status

Type annotations for `boto3.client("iam").get_service_linked_role_deletion_status` method.

[Client.get_service_linked_role_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_service_linked_role_deletion_status)

```python
def get_service_linked_role_deletion_status(
    self,
    DeletionTaskId: str
) -> GetServiceLinkedRoleDeletionStatusResponseTypeDef:
    pass
```

### get_ssh_public_key

Type annotations for `boto3.client("iam").get_ssh_public_key` method.

[Client.get_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_ssh_public_key)

```python
def get_ssh_public_key(
    self,
    UserName: str,
    SSHPublicKeyId: str,
    Encoding: encodingType
) -> GetSSHPublicKeyResponseTypeDef:
    pass
```

### get_user

Type annotations for `boto3.client("iam").get_user` method.

[Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_user)

```python
def get_user(
    self,
    UserName: str = None
) -> GetUserResponseTypeDef:
    pass
```

### get_user_policy

Type annotations for `boto3.client("iam").get_user_policy` method.

[Client.get_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.get_user_policy)

```python
def get_user_policy(
    self,
    UserName: str,
    PolicyName: str
) -> GetUserPolicyResponseTypeDef:
    pass
```

### list_access_keys

Type annotations for `boto3.client("iam").list_access_keys` method.

[Client.list_access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_access_keys)

```python
def list_access_keys(
    self,
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListAccessKeysResponseTypeDef:
    pass
```

### list_account_aliases

Type annotations for `boto3.client("iam").list_account_aliases` method.

[Client.list_account_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_account_aliases)

```python
def list_account_aliases(
    self,
    Marker: str = None,
    MaxItems: int = None
) -> ListAccountAliasesResponseTypeDef:
    pass
```

### list_attached_group_policies

Type annotations for `boto3.client("iam").list_attached_group_policies` method.

[Client.list_attached_group_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_attached_group_policies)

```python
def list_attached_group_policies(
    self,
    GroupName: str,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListAttachedGroupPoliciesResponseTypeDef:
    pass
```

### list_attached_role_policies

Type annotations for `boto3.client("iam").list_attached_role_policies` method.

[Client.list_attached_role_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_attached_role_policies)

```python
def list_attached_role_policies(
    self,
    RoleName: str,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListAttachedRolePoliciesResponseTypeDef:
    pass
```

### list_attached_user_policies

Type annotations for `boto3.client("iam").list_attached_user_policies` method.

[Client.list_attached_user_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_attached_user_policies)

```python
def list_attached_user_policies(
    self,
    UserName: str,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListAttachedUserPoliciesResponseTypeDef:
    pass
```

### list_entities_for_policy

Type annotations for `boto3.client("iam").list_entities_for_policy` method.

[Client.list_entities_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_entities_for_policy)

```python
def list_entities_for_policy(
    self,
    PolicyArn: str,
    EntityFilter: EntityType = None,
    PathPrefix: str = None,
    PolicyUsageFilter: PolicyUsageType = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListEntitiesForPolicyResponseTypeDef:
    pass
```

### list_group_policies

Type annotations for `boto3.client("iam").list_group_policies` method.

[Client.list_group_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_group_policies)

```python
def list_group_policies(
    self,
    GroupName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListGroupPoliciesResponseTypeDef:
    pass
```

### list_groups

Type annotations for `boto3.client("iam").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_groups)

```python
def list_groups(
    self,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListGroupsResponseTypeDef:
    pass
```

### list_groups_for_user

Type annotations for `boto3.client("iam").list_groups_for_user` method.

[Client.list_groups_for_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_groups_for_user)

```python
def list_groups_for_user(
    self,
    UserName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListGroupsForUserResponseTypeDef:
    pass
```

### list_instance_profile_tags

Type annotations for `boto3.client("iam").list_instance_profile_tags` method.

[Client.list_instance_profile_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_instance_profile_tags)

```python
def list_instance_profile_tags(
    self,
    InstanceProfileName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListInstanceProfileTagsResponseTypeDef:
    pass
```

### list_instance_profiles

Type annotations for `boto3.client("iam").list_instance_profiles` method.

[Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_instance_profiles)

```python
def list_instance_profiles(
    self,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListInstanceProfilesResponseTypeDef:
    pass
```

### list_instance_profiles_for_role

Type annotations for `boto3.client("iam").list_instance_profiles_for_role` method.

[Client.list_instance_profiles_for_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_instance_profiles_for_role)

```python
def list_instance_profiles_for_role(
    self,
    RoleName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListInstanceProfilesForRoleResponseTypeDef:
    pass
```

### list_mfa_device_tags

Type annotations for `boto3.client("iam").list_mfa_device_tags` method.

[Client.list_mfa_device_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_mfa_device_tags)

```python
def list_mfa_device_tags(
    self,
    SerialNumber: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListMFADeviceTagsResponseTypeDef:
    pass
```

### list_mfa_devices

Type annotations for `boto3.client("iam").list_mfa_devices` method.

[Client.list_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_mfa_devices)

```python
def list_mfa_devices(
    self,
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListMFADevicesResponseTypeDef:
    pass
```

### list_open_id_connect_provider_tags

Type annotations for `boto3.client("iam").list_open_id_connect_provider_tags` method.

[Client.list_open_id_connect_provider_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_open_id_connect_provider_tags)

```python
def list_open_id_connect_provider_tags(
    self,
    OpenIDConnectProviderArn: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListOpenIDConnectProviderTagsResponseTypeDef:
    pass
```

### list_open_id_connect_providers

Type annotations for `boto3.client("iam").list_open_id_connect_providers` method.

[Client.list_open_id_connect_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_open_id_connect_providers)

```python
def list_open_id_connect_providers(
    self
) -> ListOpenIDConnectProvidersResponseTypeDef:
    pass
```

### list_policies

Type annotations for `boto3.client("iam").list_policies` method.

[Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_policies)

```python
def list_policies(
    self,
    Scope: policyScopeType = None,
    OnlyAttached: bool = None,
    PathPrefix: str = None,
    PolicyUsageFilter: PolicyUsageType = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListPoliciesResponseTypeDef:
    pass
```

### list_policies_granting_service_access

Type annotations for `boto3.client("iam").list_policies_granting_service_access` method.

[Client.list_policies_granting_service_access documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_policies_granting_service_access)

```python
def list_policies_granting_service_access(
    self,
    Arn: str,
    ServiceNamespaces: List[str],
    Marker: str = None
) -> ListPoliciesGrantingServiceAccessResponseTypeDef:
    pass
```

### list_policy_tags

Type annotations for `boto3.client("iam").list_policy_tags` method.

[Client.list_policy_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_policy_tags)

```python
def list_policy_tags(
    self,
    PolicyArn: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListPolicyTagsResponseTypeDef:
    pass
```

### list_policy_versions

Type annotations for `boto3.client("iam").list_policy_versions` method.

[Client.list_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_policy_versions)

```python
def list_policy_versions(
    self,
    PolicyArn: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListPolicyVersionsResponseTypeDef:
    pass
```

### list_role_policies

Type annotations for `boto3.client("iam").list_role_policies` method.

[Client.list_role_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_role_policies)

```python
def list_role_policies(
    self,
    RoleName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListRolePoliciesResponseTypeDef:
    pass
```

### list_role_tags

Type annotations for `boto3.client("iam").list_role_tags` method.

[Client.list_role_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_role_tags)

```python
def list_role_tags(
    self,
    RoleName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListRoleTagsResponseTypeDef:
    pass
```

### list_roles

Type annotations for `boto3.client("iam").list_roles` method.

[Client.list_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_roles)

```python
def list_roles(
    self,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListRolesResponseTypeDef:
    pass
```

### list_saml_provider_tags

Type annotations for `boto3.client("iam").list_saml_provider_tags` method.

[Client.list_saml_provider_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_saml_provider_tags)

```python
def list_saml_provider_tags(
    self,
    SAMLProviderArn: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListSAMLProviderTagsResponseTypeDef:
    pass
```

### list_saml_providers

Type annotations for `boto3.client("iam").list_saml_providers` method.

[Client.list_saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_saml_providers)

```python
def list_saml_providers(
    self
) -> ListSAMLProvidersResponseTypeDef:
    pass
```

### list_server_certificate_tags

Type annotations for `boto3.client("iam").list_server_certificate_tags` method.

[Client.list_server_certificate_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_server_certificate_tags)

```python
def list_server_certificate_tags(
    self,
    ServerCertificateName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListServerCertificateTagsResponseTypeDef:
    pass
```

### list_server_certificates

Type annotations for `boto3.client("iam").list_server_certificates` method.

[Client.list_server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_server_certificates)

```python
def list_server_certificates(
    self,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListServerCertificatesResponseTypeDef:
    pass
```

### list_service_specific_credentials

Type annotations for `boto3.client("iam").list_service_specific_credentials` method.

[Client.list_service_specific_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_service_specific_credentials)

```python
def list_service_specific_credentials(
    self,
    UserName: str = None,
    ServiceName: str = None
) -> ListServiceSpecificCredentialsResponseTypeDef:
    pass
```

### list_signing_certificates

Type annotations for `boto3.client("iam").list_signing_certificates` method.

[Client.list_signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_signing_certificates)

```python
def list_signing_certificates(
    self,
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListSigningCertificatesResponseTypeDef:
    pass
```

### list_ssh_public_keys

Type annotations for `boto3.client("iam").list_ssh_public_keys` method.

[Client.list_ssh_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_ssh_public_keys)

```python
def list_ssh_public_keys(
    self,
    UserName: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListSSHPublicKeysResponseTypeDef:
    pass
```

### list_user_policies

Type annotations for `boto3.client("iam").list_user_policies` method.

[Client.list_user_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_user_policies)

```python
def list_user_policies(
    self,
    UserName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListUserPoliciesResponseTypeDef:
    pass
```

### list_user_tags

Type annotations for `boto3.client("iam").list_user_tags` method.

[Client.list_user_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_user_tags)

```python
def list_user_tags(
    self,
    UserName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListUserTagsResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("iam").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_users)

```python
def list_users(
    self,
    PathPrefix: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListUsersResponseTypeDef:
    pass
```

### list_virtual_mfa_devices

Type annotations for `boto3.client("iam").list_virtual_mfa_devices` method.

[Client.list_virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_virtual_mfa_devices)

```python
def list_virtual_mfa_devices(
    self,
    AssignmentStatus: assignmentStatusType = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListVirtualMFADevicesResponseTypeDef:
    pass
```

### put_group_policy

Type annotations for `boto3.client("iam").put_group_policy` method.

[Client.put_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.put_group_policy)

```python
def put_group_policy(
    self,
    GroupName: str,
    PolicyName: str,
    PolicyDocument: str
) -> None:
    pass
```

### put_role_permissions_boundary

Type annotations for `boto3.client("iam").put_role_permissions_boundary` method.

[Client.put_role_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.put_role_permissions_boundary)

```python
def put_role_permissions_boundary(
    self,
    RoleName: str,
    PermissionsBoundary: str
) -> None:
    pass
```

### put_role_policy

Type annotations for `boto3.client("iam").put_role_policy` method.

[Client.put_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.put_role_policy)

```python
def put_role_policy(
    self,
    RoleName: str,
    PolicyName: str,
    PolicyDocument: str
) -> None:
    pass
```

### put_user_permissions_boundary

Type annotations for `boto3.client("iam").put_user_permissions_boundary` method.

[Client.put_user_permissions_boundary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.put_user_permissions_boundary)

```python
def put_user_permissions_boundary(
    self,
    UserName: str,
    PermissionsBoundary: str
) -> None:
    pass
```

### put_user_policy

Type annotations for `boto3.client("iam").put_user_policy` method.

[Client.put_user_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.put_user_policy)

```python
def put_user_policy(
    self,
    UserName: str,
    PolicyName: str,
    PolicyDocument: str
) -> None:
    pass
```

### remove_client_id_from_open_id_connect_provider

Type annotations for `boto3.client("iam").remove_client_id_from_open_id_connect_provider` method.

[Client.remove_client_id_from_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.remove_client_id_from_open_id_connect_provider)

```python
def remove_client_id_from_open_id_connect_provider(
    self,
    OpenIDConnectProviderArn: str,
    ClientID: str
) -> None:
    pass
```

### remove_role_from_instance_profile

Type annotations for `boto3.client("iam").remove_role_from_instance_profile` method.

[Client.remove_role_from_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.remove_role_from_instance_profile)

```python
def remove_role_from_instance_profile(
    self,
    InstanceProfileName: str,
    RoleName: str
) -> None:
    pass
```

### remove_user_from_group

Type annotations for `boto3.client("iam").remove_user_from_group` method.

[Client.remove_user_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.remove_user_from_group)

```python
def remove_user_from_group(
    self,
    GroupName: str,
    UserName: str
) -> None:
    pass
```

### reset_service_specific_credential

Type annotations for `boto3.client("iam").reset_service_specific_credential` method.

[Client.reset_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.reset_service_specific_credential)

```python
def reset_service_specific_credential(
    self,
    ServiceSpecificCredentialId: str,
    UserName: str = None
) -> ResetServiceSpecificCredentialResponseTypeDef:
    pass
```

### resync_mfa_device

Type annotations for `boto3.client("iam").resync_mfa_device` method.

[Client.resync_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.resync_mfa_device)

```python
def resync_mfa_device(
    self,
    UserName: str,
    SerialNumber: str,
    AuthenticationCode1: str,
    AuthenticationCode2: str
) -> None:
    pass
```

### set_default_policy_version

Type annotations for `boto3.client("iam").set_default_policy_version` method.

[Client.set_default_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.set_default_policy_version)

```python
def set_default_policy_version(
    self,
    PolicyArn: str,
    VersionId: str
) -> None:
    pass
```

### set_security_token_service_preferences

Type annotations for `boto3.client("iam").set_security_token_service_preferences` method.

[Client.set_security_token_service_preferences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.set_security_token_service_preferences)

```python
def set_security_token_service_preferences(
    self,
    GlobalEndpointTokenVersion: globalEndpointTokenVersion
) -> None:
    pass
```

### simulate_custom_policy

Type annotations for `boto3.client("iam").simulate_custom_policy` method.

[Client.simulate_custom_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.simulate_custom_policy)

```python
def simulate_custom_policy(
    self,
    PolicyInputList: List[str],
    ActionNames: List[str],
    PermissionsBoundaryPolicyInputList: List[str] = None,
    ResourceArns: List[str] = None,
    ResourcePolicy: str = None,
    ResourceOwner: str = None,
    CallerArn: str = None,
    ContextEntries: List[ContextEntryTypeDef] = None,
    ResourceHandlingOption: str = None,
    MaxItems: int = None,
    Marker: str = None
) -> SimulatePolicyResponseTypeDef:
    pass
```

### simulate_principal_policy

Type annotations for `boto3.client("iam").simulate_principal_policy` method.

[Client.simulate_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.simulate_principal_policy)

```python
def simulate_principal_policy(
    self,
    PolicySourceArn: str,
    ActionNames: List[str],
    PolicyInputList: List[str] = None,
    PermissionsBoundaryPolicyInputList: List[str] = None,
    ResourceArns: List[str] = None,
    ResourcePolicy: str = None,
    ResourceOwner: str = None,
    CallerArn: str = None,
    ContextEntries: List[ContextEntryTypeDef] = None,
    ResourceHandlingOption: str = None,
    MaxItems: int = None,
    Marker: str = None
) -> SimulatePolicyResponseTypeDef:
    pass
```

### tag_instance_profile

Type annotations for `boto3.client("iam").tag_instance_profile` method.

[Client.tag_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_instance_profile)

```python
def tag_instance_profile(
    self,
    InstanceProfileName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_mfa_device

Type annotations for `boto3.client("iam").tag_mfa_device` method.

[Client.tag_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_mfa_device)

```python
def tag_mfa_device(
    self,
    SerialNumber: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_open_id_connect_provider

Type annotations for `boto3.client("iam").tag_open_id_connect_provider` method.

[Client.tag_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_open_id_connect_provider)

```python
def tag_open_id_connect_provider(
    self,
    OpenIDConnectProviderArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_policy

Type annotations for `boto3.client("iam").tag_policy` method.

[Client.tag_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_policy)

```python
def tag_policy(
    self,
    PolicyArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_role

Type annotations for `boto3.client("iam").tag_role` method.

[Client.tag_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_role)

```python
def tag_role(
    self,
    RoleName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_saml_provider

Type annotations for `boto3.client("iam").tag_saml_provider` method.

[Client.tag_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_saml_provider)

```python
def tag_saml_provider(
    self,
    SAMLProviderArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_server_certificate

Type annotations for `boto3.client("iam").tag_server_certificate` method.

[Client.tag_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_server_certificate)

```python
def tag_server_certificate(
    self,
    ServerCertificateName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_user

Type annotations for `boto3.client("iam").tag_user` method.

[Client.tag_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.tag_user)

```python
def tag_user(
    self,
    UserName: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_instance_profile

Type annotations for `boto3.client("iam").untag_instance_profile` method.

[Client.untag_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_instance_profile)

```python
def untag_instance_profile(
    self,
    InstanceProfileName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_mfa_device

Type annotations for `boto3.client("iam").untag_mfa_device` method.

[Client.untag_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_mfa_device)

```python
def untag_mfa_device(
    self,
    SerialNumber: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_open_id_connect_provider

Type annotations for `boto3.client("iam").untag_open_id_connect_provider` method.

[Client.untag_open_id_connect_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_open_id_connect_provider)

```python
def untag_open_id_connect_provider(
    self,
    OpenIDConnectProviderArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_policy

Type annotations for `boto3.client("iam").untag_policy` method.

[Client.untag_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_policy)

```python
def untag_policy(
    self,
    PolicyArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_role

Type annotations for `boto3.client("iam").untag_role` method.

[Client.untag_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_role)

```python
def untag_role(
    self,
    RoleName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_saml_provider

Type annotations for `boto3.client("iam").untag_saml_provider` method.

[Client.untag_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_saml_provider)

```python
def untag_saml_provider(
    self,
    SAMLProviderArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_server_certificate

Type annotations for `boto3.client("iam").untag_server_certificate` method.

[Client.untag_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_server_certificate)

```python
def untag_server_certificate(
    self,
    ServerCertificateName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_user

Type annotations for `boto3.client("iam").untag_user` method.

[Client.untag_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.untag_user)

```python
def untag_user(
    self,
    UserName: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_access_key

Type annotations for `boto3.client("iam").update_access_key` method.

[Client.update_access_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_access_key)

```python
def update_access_key(
    self,
    AccessKeyId: str,
    Status: statusType,
    UserName: str = None
) -> None:
    pass
```

### update_account_password_policy

Type annotations for `boto3.client("iam").update_account_password_policy` method.

[Client.update_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_account_password_policy)

```python
def update_account_password_policy(
    self,
    MinimumPasswordLength: int = None,
    RequireSymbols: bool = None,
    RequireNumbers: bool = None,
    RequireUppercaseCharacters: bool = None,
    RequireLowercaseCharacters: bool = None,
    AllowUsersToChangePassword: bool = None,
    MaxPasswordAge: int = None,
    PasswordReusePrevention: int = None,
    HardExpiry: bool = None
) -> None:
    pass
```

### update_assume_role_policy

Type annotations for `boto3.client("iam").update_assume_role_policy` method.

[Client.update_assume_role_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_assume_role_policy)

```python
def update_assume_role_policy(
    self,
    RoleName: str,
    PolicyDocument: str
) -> None:
    pass
```

### update_group

Type annotations for `boto3.client("iam").update_group` method.

[Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_group)

```python
def update_group(
    self,
    GroupName: str,
    NewPath: str = None,
    NewGroupName: str = None
) -> None:
    pass
```

### update_login_profile

Type annotations for `boto3.client("iam").update_login_profile` method.

[Client.update_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_login_profile)

```python
def update_login_profile(
    self,
    UserName: str,
    Password: str = None,
    PasswordResetRequired: bool = None
) -> None:
    pass
```

### update_open_id_connect_provider_thumbprint

Type annotations for `boto3.client("iam").update_open_id_connect_provider_thumbprint` method.

[Client.update_open_id_connect_provider_thumbprint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_open_id_connect_provider_thumbprint)

```python
def update_open_id_connect_provider_thumbprint(
    self,
    OpenIDConnectProviderArn: str,
    ThumbprintList: List[str]
) -> None:
    pass
```

### update_role

Type annotations for `boto3.client("iam").update_role` method.

[Client.update_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_role)

```python
def update_role(
    self,
    RoleName: str,
    Description: str = None,
    MaxSessionDuration: int = None
) -> Dict[str, Any]:
    pass
```

### update_role_description

Type annotations for `boto3.client("iam").update_role_description` method.

[Client.update_role_description documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_role_description)

```python
def update_role_description(
    self,
    RoleName: str,
    Description: str
) -> UpdateRoleDescriptionResponseTypeDef:
    pass
```

### update_saml_provider

Type annotations for `boto3.client("iam").update_saml_provider` method.

[Client.update_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_saml_provider)

```python
def update_saml_provider(
    self,
    SAMLMetadataDocument: str,
    SAMLProviderArn: str
) -> UpdateSAMLProviderResponseTypeDef:
    pass
```

### update_server_certificate

Type annotations for `boto3.client("iam").update_server_certificate` method.

[Client.update_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_server_certificate)

```python
def update_server_certificate(
    self,
    ServerCertificateName: str,
    NewPath: str = None,
    NewServerCertificateName: str = None
) -> None:
    pass
```

### update_service_specific_credential

Type annotations for `boto3.client("iam").update_service_specific_credential` method.

[Client.update_service_specific_credential documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_service_specific_credential)

```python
def update_service_specific_credential(
    self,
    ServiceSpecificCredentialId: str,
    Status: statusType,
    UserName: str = None
) -> None:
    pass
```

### update_signing_certificate

Type annotations for `boto3.client("iam").update_signing_certificate` method.

[Client.update_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_signing_certificate)

```python
def update_signing_certificate(
    self,
    CertificateId: str,
    Status: statusType,
    UserName: str = None
) -> None:
    pass
```

### update_ssh_public_key

Type annotations for `boto3.client("iam").update_ssh_public_key` method.

[Client.update_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_ssh_public_key)

```python
def update_ssh_public_key(
    self,
    UserName: str,
    SSHPublicKeyId: str,
    Status: statusType
) -> None:
    pass
```

### update_user

Type annotations for `boto3.client("iam").update_user` method.

[Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_user)

```python
def update_user(
    self,
    UserName: str,
    NewPath: str = None,
    NewUserName: str = None
) -> None:
    pass
```

### upload_server_certificate

Type annotations for `boto3.client("iam").upload_server_certificate` method.

[Client.upload_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.upload_server_certificate)

```python
def upload_server_certificate(
    self,
    ServerCertificateName: str,
    CertificateBody: str,
    PrivateKey: str,
    Path: str = None,
    CertificateChain: str = None,
    Tags: List["TagTypeDef"] = None
) -> UploadServerCertificateResponseTypeDef:
    pass
```

### upload_signing_certificate

Type annotations for `boto3.client("iam").upload_signing_certificate` method.

[Client.upload_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.upload_signing_certificate)

```python
def upload_signing_certificate(
    self,
    CertificateBody: str,
    UserName: str = None
) -> UploadSigningCertificateResponseTypeDef:
    pass
```

### upload_ssh_public_key

Type annotations for `boto3.client("iam").upload_ssh_public_key` method.

[Client.upload_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.upload_ssh_public_key)

```python
def upload_ssh_public_key(
    self,
    UserName: str,
    SSHPublicKeyBody: str
) -> UploadSSHPublicKeyResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.GetAccountAuthorizationDetails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.GetAccountAuthorizationDetails)

```python
@overload
def get_paginator(
    self,
    operation_name: GetAccountAuthorizationDetailsPaginatorName
) -> GetAccountAuthorizationDetailsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.GetGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.GetGroup)

```python
@overload
def get_paginator(
    self,
    operation_name: GetGroupPaginatorName
) -> GetGroupPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListAccessKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAccessKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccessKeysPaginatorName
) -> ListAccessKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListAccountAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAccountAliases)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccountAliasesPaginatorName
) -> ListAccountAliasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListAttachedGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAttachedGroupPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAttachedGroupPoliciesPaginatorName
) -> ListAttachedGroupPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListAttachedRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAttachedRolePolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAttachedRolePoliciesPaginatorName
) -> ListAttachedRolePoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListAttachedUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListAttachedUserPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAttachedUserPoliciesPaginatorName
) -> ListAttachedUserPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListEntitiesForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListEntitiesForPolicy)

```python
@overload
def get_paginator(
    self,
    operation_name: ListEntitiesForPolicyPaginatorName
) -> ListEntitiesForPolicyPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListGroupPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListGroupPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGroupPoliciesPaginatorName
) -> ListGroupPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGroupsPaginatorName
) -> ListGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListGroupsForUser)

```python
@overload
def get_paginator(
    self,
    operation_name: ListGroupsForUserPaginatorName
) -> ListGroupsForUserPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListInstanceProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInstanceProfilesPaginatorName
) -> ListInstanceProfilesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListInstanceProfilesForRole documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListInstanceProfilesForRole)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInstanceProfilesForRolePaginatorName
) -> ListInstanceProfilesForRolePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListMFADevices)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMFADevicesPaginatorName
) -> ListMFADevicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPoliciesPaginatorName
) -> ListPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListPolicyVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListPolicyVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPolicyVersionsPaginatorName
) -> ListPolicyVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListRolePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListRolePolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRolePoliciesPaginatorName
) -> ListRolePoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListRoles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRolesPaginatorName
) -> ListRolesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListSSHPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListSSHPublicKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSSHPublicKeysPaginatorName
) -> ListSSHPublicKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListServerCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListServerCertificates)

```python
@overload
def get_paginator(
    self,
    operation_name: ListServerCertificatesPaginatorName
) -> ListServerCertificatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListSigningCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListSigningCertificates)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSigningCertificatesPaginatorName
) -> ListSigningCertificatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListUserPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListUserPolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUserPoliciesPaginatorName
) -> ListUserPoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListUsers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUsersPaginatorName
) -> ListUsersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.ListVirtualMFADevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.ListVirtualMFADevices)

```python
@overload
def get_paginator(
    self,
    operation_name: ListVirtualMFADevicesPaginatorName
) -> ListVirtualMFADevicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.SimulateCustomPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.SimulateCustomPolicy)

```python
@overload
def get_paginator(
    self,
    operation_name: SimulateCustomPolicyPaginatorName
) -> SimulateCustomPolicyPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("iam").get_paginator` method.

[Paginator.SimulatePrincipalPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Paginator.SimulatePrincipalPolicy)

```python
@overload
def get_paginator(
    self,
    operation_name: SimulatePrincipalPolicyPaginatorName
) -> SimulatePrincipalPolicyPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("iam").get_waiter` method.

[Waiter.InstanceProfileExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.InstanceProfileExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: InstanceProfileExistsWaiterName
) -> InstanceProfileExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iam").get_waiter` method.

[Waiter.PolicyExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.PolicyExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: PolicyExistsWaiterName
) -> PolicyExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iam").get_waiter` method.

[Waiter.RoleExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.RoleExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: RoleExistsWaiterName
) -> RoleExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("iam").get_waiter` method.

[Waiter.UserExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Waiter.UserExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: UserExistsWaiterName
) -> UserExistsWaiter:
    pass
```