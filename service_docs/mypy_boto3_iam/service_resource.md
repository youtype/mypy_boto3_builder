# IAMServiceResource for boto3 IAM module

> [Index](../index.md) > [IAM](./index.md) > IAMServiceResource

Auto-generated documentation for [IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM)
type annotations stubs module [mypy_boto3_iam](https://pypi.org/project/mypy-boto3-iam/).

- [IAMServiceResource for boto3 IAM module](#iamserviceresource-for-boto3-iam-module)
  - [IAMServiceResource](#iamserviceresource)
  - [Methods](#methods)
    - [IAMServiceResource.AccessKey](#iamserviceresourceaccesskey)
    - [IAMServiceResource.AccessKeyPair](#iamserviceresourceaccesskeypair)
    - [IAMServiceResource.AccountPasswordPolicy](#iamserviceresourceaccountpasswordpolicy)
    - [IAMServiceResource.AccountSummary](#iamserviceresourceaccountsummary)
    - [IAMServiceResource.AssumeRolePolicy](#iamserviceresourceassumerolepolicy)
    - [IAMServiceResource.CurrentUser](#iamserviceresourcecurrentuser)
    - [IAMServiceResource.Group](#iamserviceresourcegroup)
    - [IAMServiceResource.GroupPolicy](#iamserviceresourcegrouppolicy)
    - [IAMServiceResource.InstanceProfile](#iamserviceresourceinstanceprofile)
    - [IAMServiceResource.LoginProfile](#iamserviceresourceloginprofile)
    - [IAMServiceResource.MfaDevice](#iamserviceresourcemfadevice)
    - [IAMServiceResource.Policy](#iamserviceresourcepolicy)
    - [IAMServiceResource.PolicyVersion](#iamserviceresourcepolicyversion)
    - [IAMServiceResource.Role](#iamserviceresourcerole)
    - [IAMServiceResource.RolePolicy](#iamserviceresourcerolepolicy)
    - [IAMServiceResource.SamlProvider](#iamserviceresourcesamlprovider)
    - [IAMServiceResource.ServerCertificate](#iamserviceresourceservercertificate)
    - [IAMServiceResource.SigningCertificate](#iamserviceresourcesigningcertificate)
    - [IAMServiceResource.User](#iamserviceresourceuser)
    - [IAMServiceResource.UserPolicy](#iamserviceresourceuserpolicy)
    - [IAMServiceResource.VirtualMfaDevice](#iamserviceresourcevirtualmfadevice)
    - [IAMServiceResource.change_password](#iamserviceresourcechange_password)
    - [IAMServiceResource.create_account_alias](#iamserviceresourcecreate_account_alias)
    - [IAMServiceResource.create_account_password_policy](#iamserviceresourcecreate_account_password_policy)
    - [IAMServiceResource.create_group](#iamserviceresourcecreate_group)
    - [IAMServiceResource.create_instance_profile](#iamserviceresourcecreate_instance_profile)
    - [IAMServiceResource.create_policy](#iamserviceresourcecreate_policy)
    - [IAMServiceResource.create_role](#iamserviceresourcecreate_role)
    - [IAMServiceResource.create_saml_provider](#iamserviceresourcecreate_saml_provider)
    - [IAMServiceResource.create_server_certificate](#iamserviceresourcecreate_server_certificate)
    - [IAMServiceResource.create_signing_certificate](#iamserviceresourcecreate_signing_certificate)
    - [IAMServiceResource.create_user](#iamserviceresourcecreate_user)
    - [IAMServiceResource.create_virtual_mfa_device](#iamserviceresourcecreate_virtual_mfa_device)
    - [IAMServiceResource.get_available_subresources](#iamserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [IAMServiceResource.groups](#iamserviceresourcegroups)
    - [IAMServiceResource.instance_profiles](#iamserviceresourceinstance_profiles)
    - [IAMServiceResource.policies](#iamserviceresourcepolicies)
    - [IAMServiceResource.roles](#iamserviceresourceroles)
    - [IAMServiceResource.saml_providers](#iamserviceresourcesaml_providers)
    - [IAMServiceResource.server_certificates](#iamserviceresourceserver_certificates)
    - [IAMServiceResource.users](#iamserviceresourceusers)
    - [IAMServiceResource.virtual_mfa_devices](#iamserviceresourcevirtual_mfa_devices)
  - [AccessKey](#accesskey)
    - [AccessKey attributes](#accesskey-attributes)
    - [AccessKey methods](#accesskey-methods)
  - [AccessKeyPair](#accesskeypair)
    - [AccessKeyPair attributes](#accesskeypair-attributes)
    - [AccessKeyPair methods](#accesskeypair-methods)
  - [AccountPasswordPolicy](#accountpasswordpolicy)
    - [AccountPasswordPolicy attributes](#accountpasswordpolicy-attributes)
    - [AccountPasswordPolicy methods](#accountpasswordpolicy-methods)
  - [AccountSummary](#accountsummary)
    - [AccountSummary attributes](#accountsummary-attributes)
    - [AccountSummary methods](#accountsummary-methods)
  - [AssumeRolePolicy](#assumerolepolicy)
    - [AssumeRolePolicy attributes](#assumerolepolicy-attributes)
    - [AssumeRolePolicy methods](#assumerolepolicy-methods)
  - [CurrentUser](#currentuser)
    - [CurrentUser attributes](#currentuser-attributes)
    - [CurrentUser methods](#currentuser-methods)
    - [CurrentUser collections](#currentuser-collections)
  - [Group](#group)
    - [Group attributes](#group-attributes)
    - [Group methods](#group-methods)
    - [Group collections](#group-collections)
  - [GroupPolicy](#grouppolicy)
    - [GroupPolicy attributes](#grouppolicy-attributes)
    - [GroupPolicy methods](#grouppolicy-methods)
  - [InstanceProfile](#instanceprofile)
    - [InstanceProfile attributes](#instanceprofile-attributes)
    - [InstanceProfile methods](#instanceprofile-methods)
  - [LoginProfile](#loginprofile)
    - [LoginProfile attributes](#loginprofile-attributes)
    - [LoginProfile methods](#loginprofile-methods)
  - [MfaDevice](#mfadevice)
    - [MfaDevice attributes](#mfadevice-attributes)
    - [MfaDevice methods](#mfadevice-methods)
  - [Policy](#policy)
    - [Policy attributes](#policy-attributes)
    - [Policy methods](#policy-methods)
    - [Policy collections](#policy-collections)
  - [PolicyVersion](#policyversion)
    - [PolicyVersion attributes](#policyversion-attributes)
    - [PolicyVersion methods](#policyversion-methods)
  - [Role](#role)
    - [Role attributes](#role-attributes)
    - [Role methods](#role-methods)
    - [Role collections](#role-collections)
  - [RolePolicy](#rolepolicy)
    - [RolePolicy attributes](#rolepolicy-attributes)
    - [RolePolicy methods](#rolepolicy-methods)
  - [SamlProvider](#samlprovider)
    - [SamlProvider attributes](#samlprovider-attributes)
    - [SamlProvider methods](#samlprovider-methods)
  - [ServerCertificate](#servercertificate)
    - [ServerCertificate attributes](#servercertificate-attributes)
    - [ServerCertificate methods](#servercertificate-methods)
  - [SigningCertificate](#signingcertificate)
    - [SigningCertificate attributes](#signingcertificate-attributes)
    - [SigningCertificate methods](#signingcertificate-methods)
  - [User](#user)
    - [User attributes](#user-attributes)
    - [User methods](#user-methods)
    - [User collections](#user-collections)
  - [UserPolicy](#userpolicy)
    - [UserPolicy attributes](#userpolicy-attributes)
    - [UserPolicy methods](#userpolicy-methods)
  - [VirtualMfaDevice](#virtualmfadevice)
    - [VirtualMfaDevice attributes](#virtualmfadevice-attributes)
    - [VirtualMfaDevice methods](#virtualmfadevice-methods)

## IAMServiceResource

Type annotations for `boto3.resource("iam")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import IAMServiceResource
```



## Methods

### IAMServiceResource.AccessKey

Type annotations for `boto3.resource("iam").AccessKey` method.

[ServiceResource.AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKey)

Definition:

```python
def AccessKey(
    self,
    user_name: str,
    id: str
) -> _AccessKey:
    pass
```

### IAMServiceResource.AccessKeyPair

Type annotations for `boto3.resource("iam").AccessKeyPair` method.

[ServiceResource.AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)

Definition:

```python
def AccessKeyPair(
    self,
    user_name: str,
    id: str,
    secret: str
) -> _AccessKeyPair:
    pass
```

### IAMServiceResource.AccountPasswordPolicy

Type annotations for `boto3.resource("iam").AccountPasswordPolicy` method.

[ServiceResource.AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)

Definition:

```python
def AccountPasswordPolicy(
    self
) -> _AccountPasswordPolicy:
    pass
```

### IAMServiceResource.AccountSummary

Type annotations for `boto3.resource("iam").AccountSummary` method.

[ServiceResource.AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountSummary)

Definition:

```python
def AccountSummary(
    self
) -> _AccountSummary:
    pass
```

### IAMServiceResource.AssumeRolePolicy

Type annotations for `boto3.resource("iam").AssumeRolePolicy` method.

[ServiceResource.AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)

Definition:

```python
def AssumeRolePolicy(
    self,
    role_name: str
) -> _AssumeRolePolicy:
    pass
```

### IAMServiceResource.CurrentUser

Type annotations for `boto3.resource("iam").CurrentUser` method.

[ServiceResource.CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.CurrentUser)

Definition:

```python
def CurrentUser(
    self
) -> _CurrentUser:
    pass
```

### IAMServiceResource.Group

Type annotations for `boto3.resource("iam").Group` method.

[ServiceResource.Group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Group)

Definition:

```python
def Group(
    self,
    name: str
) -> _Group:
    pass
```

### IAMServiceResource.GroupPolicy

Type annotations for `boto3.resource("iam").GroupPolicy` method.

[ServiceResource.GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)

Definition:

```python
def GroupPolicy(
    self,
    group_name: str,
    name: str
) -> _GroupPolicy:
    pass
```

### IAMServiceResource.InstanceProfile

Type annotations for `boto3.resource("iam").InstanceProfile` method.

[ServiceResource.InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)

Definition:

```python
def InstanceProfile(
    self,
    name: str
) -> _InstanceProfile:
    pass
```

### IAMServiceResource.LoginProfile

Type annotations for `boto3.resource("iam").LoginProfile` method.

[ServiceResource.LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.LoginProfile)

Definition:

```python
def LoginProfile(
    self,
    user_name: str
) -> _LoginProfile:
    pass
```

### IAMServiceResource.MfaDevice

Type annotations for `boto3.resource("iam").MfaDevice` method.

[ServiceResource.MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.MfaDevice)

Definition:

```python
def MfaDevice(
    self,
    user_name: str,
    serial_number: str
) -> _MfaDevice:
    pass
```

### IAMServiceResource.Policy

Type annotations for `boto3.resource("iam").Policy` method.

[ServiceResource.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Policy)

Definition:

```python
def Policy(
    self,
    policy_arn: str
) -> _Policy:
    pass
```

### IAMServiceResource.PolicyVersion

Type annotations for `boto3.resource("iam").PolicyVersion` method.

[ServiceResource.PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)

Definition:

```python
def PolicyVersion(
    self,
    arn: str,
    version_id: str
) -> _PolicyVersion:
    pass
```

### IAMServiceResource.Role

Type annotations for `boto3.resource("iam").Role` method.

[ServiceResource.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Role)

Definition:

```python
def Role(
    self,
    name: str
) -> _Role:
    pass
```

### IAMServiceResource.RolePolicy

Type annotations for `boto3.resource("iam").RolePolicy` method.

[ServiceResource.RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.RolePolicy)

Definition:

```python
def RolePolicy(
    self,
    role_name: str,
    name: str
) -> _RolePolicy:
    pass
```

### IAMServiceResource.SamlProvider

Type annotations for `boto3.resource("iam").SamlProvider` method.

[ServiceResource.SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SamlProvider)

Definition:

```python
def SamlProvider(
    self,
    arn: str
) -> _SamlProvider:
    pass
```

### IAMServiceResource.ServerCertificate

Type annotations for `boto3.resource("iam").ServerCertificate` method.

[ServiceResource.ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)

Definition:

```python
def ServerCertificate(
    self,
    name: str
) -> _ServerCertificate:
    pass
```

### IAMServiceResource.SigningCertificate

Type annotations for `boto3.resource("iam").SigningCertificate` method.

[ServiceResource.SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)

Definition:

```python
def SigningCertificate(
    self,
    user_name: str,
    id: str
) -> _SigningCertificate:
    pass
```

### IAMServiceResource.User

Type annotations for `boto3.resource("iam").User` method.

[ServiceResource.User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.User)

Definition:

```python
def User(
    self,
    name: str
) -> _User:
    pass
```

### IAMServiceResource.UserPolicy

Type annotations for `boto3.resource("iam").UserPolicy` method.

[ServiceResource.UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.UserPolicy)

Definition:

```python
def UserPolicy(
    self,
    user_name: str,
    name: str
) -> _UserPolicy:
    pass
```

### IAMServiceResource.VirtualMfaDevice

Type annotations for `boto3.resource("iam").VirtualMfaDevice` method.

[ServiceResource.VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)

Definition:

```python
def VirtualMfaDevice(
    self,
    serial_number: str
) -> _VirtualMfaDevice:
    pass
```

### IAMServiceResource.change_password

Type annotations for `boto3.resource("iam").change_password` method.

[ServiceResource.change_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.change_password)

Definition:

```python
def change_password(
    self,
    OldPassword: str,
    NewPassword: str
) -> None:
    pass
```

### IAMServiceResource.create_account_alias

Type annotations for `boto3.resource("iam").create_account_alias` method.

[ServiceResource.create_account_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_account_alias)

Definition:

```python
def create_account_alias(
    self,
    AccountAlias: str
) -> None:
    pass
```

### IAMServiceResource.create_account_password_policy

Type annotations for `boto3.resource("iam").create_account_password_policy` method.

[ServiceResource.create_account_password_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)

Definition:

```python
def create_account_password_policy(
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
) -> _AccountPasswordPolicy:
    pass
```

### IAMServiceResource.create_group

Type annotations for `boto3.resource("iam").create_group` method.

[ServiceResource.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_group)

Definition:

```python
def create_group(
    self,
    GroupName: str,
    Path: str = None
) -> _Group:
    pass
```

### IAMServiceResource.create_instance_profile

Type annotations for `boto3.resource("iam").create_instance_profile` method.

[ServiceResource.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)

Definition:

```python
def create_instance_profile(
    self,
    InstanceProfileName: str,
    Path: str = None,
    Tags: List["TagTypeDef"] = None
) -> _InstanceProfile:
    pass
```

### IAMServiceResource.create_policy

Type annotations for `boto3.resource("iam").create_policy` method.

[ServiceResource.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_policy)

Definition:

```python
def create_policy(
    self,
    PolicyName: str,
    PolicyDocument: str,
    Path: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> _Policy:
    pass
```

### IAMServiceResource.create_role

Type annotations for `boto3.resource("iam").create_role` method.

[ServiceResource.create_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_role)

Definition:

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
) -> _Role:
    pass
```

### IAMServiceResource.create_saml_provider

Type annotations for `boto3.resource("iam").create_saml_provider` method.

[ServiceResource.create_saml_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)

Definition:

```python
def create_saml_provider(
    self,
    SAMLMetadataDocument: str,
    Name: str,
    Tags: List["TagTypeDef"] = None
) -> _SamlProvider:
    pass
```

### IAMServiceResource.create_server_certificate

Type annotations for `boto3.resource("iam").create_server_certificate` method.

[ServiceResource.create_server_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)

Definition:

```python
def create_server_certificate(
    self,
    ServerCertificateName: str,
    CertificateBody: str,
    PrivateKey: str,
    Path: str = None,
    CertificateChain: str = None,
    Tags: List["TagTypeDef"] = None
) -> _ServerCertificate:
    pass
```

### IAMServiceResource.create_signing_certificate

Type annotations for `boto3.resource("iam").create_signing_certificate` method.

[ServiceResource.create_signing_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)

Definition:

```python
def create_signing_certificate(
    self,
    CertificateBody: str,
    UserName: str = None
) -> _SigningCertificate:
    pass
```

### IAMServiceResource.create_user

Type annotations for `boto3.resource("iam").create_user` method.

[ServiceResource.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_user)

Definition:

```python
def create_user(
    self,
    UserName: str,
    Path: str = None,
    PermissionsBoundary: str = None,
    Tags: List["TagTypeDef"] = None
) -> _User:
    pass
```

### IAMServiceResource.create_virtual_mfa_device

Type annotations for `boto3.resource("iam").create_virtual_mfa_device` method.

[ServiceResource.create_virtual_mfa_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)

Definition:

```python
def create_virtual_mfa_device(
    self,
    VirtualMFADeviceName: str,
    Path: str = None,
    Tags: List["TagTypeDef"] = None
) -> _VirtualMfaDevice:
    pass
```

### IAMServiceResource.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### IAMServiceResource.groups

Type annotations for `boto3.resource("iam").groups` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceGroupsCollection,

def get_collection() -> ServiceResourceGroupsCollection:
    return boto3.resource("iam").groups(
        ...
    )
```

[ServiceResource.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)

Definition:

```python
class ServiceResourceGroupsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourceGroupsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceGroupsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceGroupsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Group"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Group"]:
        pass
```

### IAMServiceResource.instance_profiles

Type annotations for `boto3.resource("iam").instance_profiles` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceInstanceProfilesCollection,

def get_collection() -> ServiceResourceInstanceProfilesCollection:
    return boto3.resource("iam").instance_profiles(
        ...
    )
```

[ServiceResource.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)

Definition:

```python
class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["InstanceProfile"]:
        pass
```

### IAMServiceResource.policies

Type annotations for `boto3.resource("iam").policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourcePoliciesCollection,

def get_collection() -> ServiceResourcePoliciesCollection:
    return boto3.resource("iam").policies(
        ...
    )
```

[ServiceResource.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)

Definition:

```python
class ServiceResourcePoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Scope: policyScopeType = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Policy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Policy"]:
        pass
```

### IAMServiceResource.roles

Type annotations for `boto3.resource("iam").roles` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceRolesCollection,

def get_collection() -> ServiceResourceRolesCollection:
    return boto3.resource("iam").roles(
        ...
    )
```

[ServiceResource.roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)

Definition:

```python
class ServiceResourceRolesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceRolesCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourceRolesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceRolesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceRolesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Role"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Role"]:
        pass
```

### IAMServiceResource.saml_providers

Type annotations for `boto3.resource("iam").saml_providers` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceSamlProvidersCollection,

def get_collection() -> ServiceResourceSamlProvidersCollection:
    return boto3.resource("iam").saml_providers(
        ...
    )
```

[ServiceResource.saml_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)

Definition:

```python
class ServiceResourceSamlProvidersCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceSamlProvidersCollection":
        pass

    def filter(  # type: ignore
        self
    ) -> "ServiceResourceSamlProvidersCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceSamlProvidersCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceSamlProvidersCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["SamlProvider"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["SamlProvider"]:
        pass
```

### IAMServiceResource.server_certificates

Type annotations for `boto3.resource("iam").server_certificates` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceServerCertificatesCollection,

def get_collection() -> ServiceResourceServerCertificatesCollection:
    return boto3.resource("iam").server_certificates(
        ...
    )
```

[ServiceResource.server_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)

Definition:

```python
class ServiceResourceServerCertificatesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["ServerCertificate"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["ServerCertificate"]:
        pass
```

### IAMServiceResource.users

Type annotations for `boto3.resource("iam").users` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceUsersCollection,

def get_collection() -> ServiceResourceUsersCollection:
    return boto3.resource("iam").users(
        ...
    )
```

[ServiceResource.users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)

Definition:

```python
class ServiceResourceUsersCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceUsersCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourceUsersCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceUsersCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceUsersCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["User"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["User"]:
        pass
```

### IAMServiceResource.virtual_mfa_devices

Type annotations for `boto3.resource("iam").virtual_mfa_devices` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServiceResourceVirtualMfaDevicesCollection,

def get_collection() -> ServiceResourceVirtualMfaDevicesCollection:
    return boto3.resource("iam").virtual_mfa_devices(
        ...
    )
```

[ServiceResource.virtual_mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)

Definition:

```python
class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self,
        AssignmentStatus: assignmentStatusType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["VirtualMfaDevice"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["VirtualMfaDevice"]:
        pass
```




## AccessKey

Type annotations for `boto3.resource("iam").AccessKey` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import AccessKey

def get_resource() -> AccessKey:
    return boto3.resource("iam").AccessKey(...)
```

[AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKey)


### AccessKey attributes


- `access_key_id`: `str`

- `status`: `str`

- `create_date`: `datetime`

- `user_name`: `str`

- `id`: `str`




### AccessKey methods


#### AccessKey.User

Type annotations for `boto3.resource("iam").User` method.

[AccessKey.User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.User)

```python
def User(
    self
) -> _User:
    pass
```

#### AccessKey.activate

Type annotations for `boto3.resource("iam").activate` method.

[AccessKey.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.activate)

```python
def activate(
    self,
    Status: statusType
) -> None:
    pass
```

#### AccessKey.deactivate

Type annotations for `boto3.resource("iam").deactivate` method.

[AccessKey.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.deactivate)

```python
def deactivate(
    self,
    Status: statusType
) -> None:
    pass
```

#### AccessKey.delete

Type annotations for `boto3.resource("iam").delete` method.

[AccessKey.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### AccessKey.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[AccessKey.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```






## AccessKeyPair

Type annotations for `boto3.resource("iam").AccessKeyPair` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import AccessKeyPair

def get_resource() -> AccessKeyPair:
    return boto3.resource("iam").AccessKeyPair(...)
```

[AccessKeyPair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)


### AccessKeyPair attributes


- `access_key_id`: `str`

- `status`: `str`

- `secret_access_key`: `str`

- `create_date`: `datetime`

- `user_name`: `str`

- `id`: `str`

- `secret`: `str`




### AccessKeyPair methods


#### AccessKeyPair.activate

Type annotations for `boto3.resource("iam").activate` method.

[AccessKeyPair.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.activate)

```python
def activate(
    self,
    Status: statusType
) -> None:
    pass
```

#### AccessKeyPair.deactivate

Type annotations for `boto3.resource("iam").deactivate` method.

[AccessKeyPair.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.deactivate)

```python
def deactivate(
    self,
    Status: statusType
) -> None:
    pass
```

#### AccessKeyPair.delete

Type annotations for `boto3.resource("iam").delete` method.

[AccessKeyPair.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### AccessKeyPair.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[AccessKeyPair.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```






## AccountPasswordPolicy

Type annotations for `boto3.resource("iam").AccountPasswordPolicy` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import AccountPasswordPolicy

def get_resource() -> AccountPasswordPolicy:
    return boto3.resource("iam").AccountPasswordPolicy(...)
```

[AccountPasswordPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)


### AccountPasswordPolicy attributes


- `minimum_password_length`: `int`

- `require_symbols`: `bool`

- `require_numbers`: `bool`

- `require_uppercase_characters`: `bool`

- `require_lowercase_characters`: `bool`

- `allow_users_to_change_password`: `bool`

- `expire_passwords`: `bool`

- `max_password_age`: `int`

- `password_reuse_prevention`: `int`

- `hard_expiry`: `bool`




### AccountPasswordPolicy methods


#### AccountPasswordPolicy.delete

Type annotations for `boto3.resource("iam").delete` method.

[AccountPasswordPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### AccountPasswordPolicy.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[AccountPasswordPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### AccountPasswordPolicy.load

Type annotations for `boto3.resource("iam").load` method.

[AccountPasswordPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.load)

```python
def load(
    self
) -> None:
    pass
```

#### AccountPasswordPolicy.reload

Type annotations for `boto3.resource("iam").reload` method.

[AccountPasswordPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### AccountPasswordPolicy.update

Type annotations for `boto3.resource("iam").update` method.

[AccountPasswordPolicy.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.update)

```python
def update(
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






## AccountSummary

Type annotations for `boto3.resource("iam").AccountSummary` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import AccountSummary

def get_resource() -> AccountSummary:
    return boto3.resource("iam").AccountSummary(...)
```

[AccountSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountSummary)


### AccountSummary attributes


- `summary_map`: `Dict[str, Any]`




### AccountSummary methods


#### AccountSummary.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[AccountSummary.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountSummary.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### AccountSummary.load

Type annotations for `boto3.resource("iam").load` method.

[AccountSummary.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountSummary.load)

```python
def load(
    self
) -> None:
    pass
```

#### AccountSummary.reload

Type annotations for `boto3.resource("iam").reload` method.

[AccountSummary.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountSummary.reload)

```python
def reload(
    self
) -> None:
    pass
```






## AssumeRolePolicy

Type annotations for `boto3.resource("iam").AssumeRolePolicy` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import AssumeRolePolicy

def get_resource() -> AssumeRolePolicy:
    return boto3.resource("iam").AssumeRolePolicy(...)
```

[AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)


### AssumeRolePolicy attributes


- `role_name`: `str`




### AssumeRolePolicy methods


#### AssumeRolePolicy.Role

Type annotations for `boto3.resource("iam").Role` method.

[AssumeRolePolicy.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AssumeRolePolicy.Role)

```python
def Role(
    self
) -> _Role:
    pass
```

#### AssumeRolePolicy.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[AssumeRolePolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AssumeRolePolicy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### AssumeRolePolicy.update

Type annotations for `boto3.resource("iam").update` method.

[AssumeRolePolicy.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AssumeRolePolicy.update)

```python
def update(
    self,
    PolicyDocument: str
) -> None:
    pass
```






## CurrentUser

Type annotations for `boto3.resource("iam").CurrentUser` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import CurrentUser

def get_resource() -> CurrentUser:
    return boto3.resource("iam").CurrentUser(...)
```

[CurrentUser documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.CurrentUser)


### CurrentUser attributes


- `path`: `str`

- `user_name`: `str`

- `user_id`: `str`

- `arn`: `str`

- `create_date`: `datetime`

- `password_last_used`: `datetime`

- `permissions_boundary`: `Dict[str, Any]`

- `tags`: `List[Any]`

- `user`: `"User"`

- `access_keys`: `CurrentUserAccessKeysCollection`

- `mfa_devices`: `CurrentUserMfaDevicesCollection`

- `signing_certificates`: `CurrentUserSigningCertificatesCollection`




### CurrentUser methods


#### CurrentUser.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[CurrentUser.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### CurrentUser.load

Type annotations for `boto3.resource("iam").load` method.

[CurrentUser.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.load)

```python
def load(
    self
) -> None:
    pass
```

#### CurrentUser.reload

Type annotations for `boto3.resource("iam").reload` method.

[CurrentUser.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.reload)

```python
def reload(
    self
) -> None:
    pass
```




### CurrentUser collections


#### CurrentUser.access_keys

Type annotations for `boto3.resource("iam").CurrentUser(...).access_keys` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import CurrentUserAccessKeysCollection,

def get_collection() -> CurrentUserAccessKeysCollection:
    resource = boto3.resource("iam").CurrentUser(...)
    return resource.access_keys
```

[CurrentUser.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.access_keys)

```python
class CurrentUserAccessKeysCollection(ResourceCollection):
    def all(
        self
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self,
        UserName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["AccessKey"]:
        pass
```

#### CurrentUser.mfa_devices

Type annotations for `boto3.resource("iam").CurrentUser(...).mfa_devices` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import CurrentUserMfaDevicesCollection,

def get_collection() -> CurrentUserMfaDevicesCollection:
    resource = boto3.resource("iam").CurrentUser(...)
    return resource.mfa_devices
```

[CurrentUser.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.mfa_devices)

```python
class CurrentUserMfaDevicesCollection(ResourceCollection):
    def all(
        self
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self,
        UserName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["MfaDevice"]:
        pass
```

#### CurrentUser.signing_certificates

Type annotations for `boto3.resource("iam").CurrentUser(...).signing_certificates` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import CurrentUserSigningCertificatesCollection,

def get_collection() -> CurrentUserSigningCertificatesCollection:
    resource = boto3.resource("iam").CurrentUser(...)
    return resource.signing_certificates
```

[CurrentUser.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.signing_certificates)

```python
class CurrentUserSigningCertificatesCollection(ResourceCollection):
    def all(
        self
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self,
        UserName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["SigningCertificate"]:
        pass
```




## Group

Type annotations for `boto3.resource("iam").Group` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import Group

def get_resource() -> Group:
    return boto3.resource("iam").Group(...)
```

[Group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Group)


### Group attributes


- `path`: `str`

- `group_name`: `str`

- `group_id`: `str`

- `arn`: `str`

- `create_date`: `datetime`

- `name`: `str`

- `attached_policies`: `GroupAttachedPoliciesCollection`

- `policies`: `GroupPoliciesCollection`

- `users`: `GroupUsersCollection`




### Group methods


#### Group.Policy

Type annotations for `boto3.resource("iam").Policy` method.

[Group.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.Policy)

```python
def Policy(
    self,
    name: str
) -> _GroupPolicy:
    pass
```

#### Group.add_user

Type annotations for `boto3.resource("iam").add_user` method.

[Group.add_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.add_user)

```python
def add_user(
    self,
    UserName: str
) -> None:
    pass
```

#### Group.attach_policy

Type annotations for `boto3.resource("iam").attach_policy` method.

[Group.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.attach_policy)

```python
def attach_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

#### Group.create

Type annotations for `boto3.resource("iam").create` method.

[Group.create documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.create)

```python
def create(
    self,
    Path: str = None
) -> _Group:
    pass
```

#### Group.create_policy

Type annotations for `boto3.resource("iam").create_policy` method.

[Group.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.create_policy)

```python
def create_policy(
    self,
    PolicyName: str,
    PolicyDocument: str
) -> _GroupPolicy:
    pass
```

#### Group.delete

Type annotations for `boto3.resource("iam").delete` method.

[Group.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Group.detach_policy

Type annotations for `boto3.resource("iam").detach_policy` method.

[Group.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.detach_policy)

```python
def detach_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

#### Group.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[Group.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Group.load

Type annotations for `boto3.resource("iam").load` method.

[Group.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.load)

```python
def load(
    self
) -> None:
    pass
```

#### Group.reload

Type annotations for `boto3.resource("iam").reload` method.

[Group.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Group.remove_user

Type annotations for `boto3.resource("iam").remove_user` method.

[Group.remove_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.remove_user)

```python
def remove_user(
    self,
    UserName: str
) -> None:
    pass
```

#### Group.update

Type annotations for `boto3.resource("iam").update` method.

[Group.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.update)

```python
def update(
    self,
    NewPath: str = None,
    NewGroupName: str = None
) -> _Group:
    pass
```




### Group collections


#### Group.attached_policies

Type annotations for `boto3.resource("iam").Group(...).attached_policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import GroupAttachedPoliciesCollection,

def get_collection() -> GroupAttachedPoliciesCollection:
    resource = boto3.resource("iam").Group(...)
    return resource.attached_policies
```

[Group.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.attached_policies)

```python
class GroupAttachedPoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Policy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Policy"]:
        pass
```

#### Group.policies

Type annotations for `boto3.resource("iam").Group(...).policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import GroupPoliciesCollection,

def get_collection() -> GroupPoliciesCollection:
    resource = boto3.resource("iam").Group(...)
    return resource.policies
```

[Group.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.policies)

```python
class GroupPoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "GroupPoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "GroupPoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "GroupPoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "GroupPoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["GroupPolicy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["GroupPolicy"]:
        pass
```

#### Group.users

Type annotations for `boto3.resource("iam").Group(...).users` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import GroupUsersCollection,

def get_collection() -> GroupUsersCollection:
    resource = boto3.resource("iam").Group(...)
    return resource.users
```

[Group.users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.users)

```python
class GroupUsersCollection(ResourceCollection):
    def all(
        self
    ) -> "GroupUsersCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "GroupUsersCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "GroupUsersCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "GroupUsersCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["User"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["User"]:
        pass
```




## GroupPolicy

Type annotations for `boto3.resource("iam").GroupPolicy` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import GroupPolicy

def get_resource() -> GroupPolicy:
    return boto3.resource("iam").GroupPolicy(...)
```

[GroupPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)


### GroupPolicy attributes


- `policy_name`: `str`

- `policy_document`: `str`

- `group_name`: `str`

- `name`: `str`




### GroupPolicy methods


#### GroupPolicy.Group

Type annotations for `boto3.resource("iam").Group` method.

[GroupPolicy.Group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.Group)

```python
def Group(
    self
) -> _Group:
    pass
```

#### GroupPolicy.delete

Type annotations for `boto3.resource("iam").delete` method.

[GroupPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### GroupPolicy.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[GroupPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### GroupPolicy.load

Type annotations for `boto3.resource("iam").load` method.

[GroupPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.load)

```python
def load(
    self
) -> None:
    pass
```

#### GroupPolicy.put

Type annotations for `boto3.resource("iam").put` method.

[GroupPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.put)

```python
def put(
    self,
    PolicyDocument: str
) -> None:
    pass
```

#### GroupPolicy.reload

Type annotations for `boto3.resource("iam").reload` method.

[GroupPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.reload)

```python
def reload(
    self
) -> None:
    pass
```






## InstanceProfile

Type annotations for `boto3.resource("iam").InstanceProfile` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import InstanceProfile

def get_resource() -> InstanceProfile:
    return boto3.resource("iam").InstanceProfile(...)
```

[InstanceProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)


### InstanceProfile attributes


- `path`: `str`

- `instance_profile_name`: `str`

- `instance_profile_id`: `str`

- `arn`: `str`

- `create_date`: `datetime`

- `roles_attribute`: `List[Any]`

- `tags`: `List[Any]`

- `name`: `str`

- `roles`: `"Role"`




### InstanceProfile methods


#### InstanceProfile.add_role

Type annotations for `boto3.resource("iam").add_role` method.

[InstanceProfile.add_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.add_role)

```python
def add_role(
    self,
    RoleName: str
) -> None:
    pass
```

#### InstanceProfile.delete

Type annotations for `boto3.resource("iam").delete` method.

[InstanceProfile.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### InstanceProfile.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[InstanceProfile.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### InstanceProfile.load

Type annotations for `boto3.resource("iam").load` method.

[InstanceProfile.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.load)

```python
def load(
    self
) -> None:
    pass
```

#### InstanceProfile.reload

Type annotations for `boto3.resource("iam").reload` method.

[InstanceProfile.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### InstanceProfile.remove_role

Type annotations for `boto3.resource("iam").remove_role` method.

[InstanceProfile.remove_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.remove_role)

```python
def remove_role(
    self,
    RoleName: str
) -> None:
    pass
```






## LoginProfile

Type annotations for `boto3.resource("iam").LoginProfile` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import LoginProfile

def get_resource() -> LoginProfile:
    return boto3.resource("iam").LoginProfile(...)
```

[LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.LoginProfile)


### LoginProfile attributes


- `create_date`: `datetime`

- `password_reset_required`: `bool`

- `user_name`: `str`




### LoginProfile methods


#### LoginProfile.User

Type annotations for `boto3.resource("iam").User` method.

[LoginProfile.User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.User)

```python
def User(
    self
) -> _User:
    pass
```

#### LoginProfile.create

Type annotations for `boto3.resource("iam").create` method.

[LoginProfile.create documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.create)

```python
def create(
    self,
    Password: str,
    PasswordResetRequired: bool = None
) -> _LoginProfile:
    pass
```

#### LoginProfile.delete

Type annotations for `boto3.resource("iam").delete` method.

[LoginProfile.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### LoginProfile.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[LoginProfile.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### LoginProfile.load

Type annotations for `boto3.resource("iam").load` method.

[LoginProfile.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.load)

```python
def load(
    self
) -> None:
    pass
```

#### LoginProfile.reload

Type annotations for `boto3.resource("iam").reload` method.

[LoginProfile.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### LoginProfile.update

Type annotations for `boto3.resource("iam").update` method.

[LoginProfile.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.update)

```python
def update(
    self,
    Password: str = None,
    PasswordResetRequired: bool = None
) -> None:
    pass
```






## MfaDevice

Type annotations for `boto3.resource("iam").MfaDevice` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import MfaDevice

def get_resource() -> MfaDevice:
    return boto3.resource("iam").MfaDevice(...)
```

[MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.MfaDevice)


### MfaDevice attributes


- `enable_date`: `datetime`

- `user_name`: `str`

- `serial_number`: `str`




### MfaDevice methods


#### MfaDevice.User

Type annotations for `boto3.resource("iam").User` method.

[MfaDevice.User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.User)

```python
def User(
    self
) -> _User:
    pass
```

#### MfaDevice.associate

Type annotations for `boto3.resource("iam").associate` method.

[MfaDevice.associate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.associate)

```python
def associate(
    self,
    AuthenticationCode1: str,
    AuthenticationCode2: str
) -> None:
    pass
```

#### MfaDevice.disassociate

Type annotations for `boto3.resource("iam").disassociate` method.

[MfaDevice.disassociate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.disassociate)

```python
def disassociate(
    self
) -> None:
    pass
```

#### MfaDevice.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[MfaDevice.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### MfaDevice.resync

Type annotations for `boto3.resource("iam").resync` method.

[MfaDevice.resync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.resync)

```python
def resync(
    self,
    AuthenticationCode1: str,
    AuthenticationCode2: str
) -> None:
    pass
```






## Policy

Type annotations for `boto3.resource("iam").Policy` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import Policy

def get_resource() -> Policy:
    return boto3.resource("iam").Policy(...)
```

[Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Policy)


### Policy attributes


- `policy_name`: `str`

- `policy_id`: `str`

- `path`: `str`

- `default_version_id`: `str`

- `attachment_count`: `int`

- `permissions_boundary_usage_count`: `int`

- `is_attachable`: `bool`

- `description`: `str`

- `create_date`: `datetime`

- `update_date`: `datetime`

- `tags`: `List[Any]`

- `arn`: `str`

- `default_version`: `"PolicyVersion"`

- `attached_groups`: `PolicyAttachedGroupsCollection`

- `attached_roles`: `PolicyAttachedRolesCollection`

- `attached_users`: `PolicyAttachedUsersCollection`

- `versions`: `PolicyVersionsCollection`




### Policy methods


#### Policy.attach_group

Type annotations for `boto3.resource("iam").attach_group` method.

[Policy.attach_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attach_group)

```python
def attach_group(
    self,
    GroupName: str
) -> None:
    pass
```

#### Policy.attach_role

Type annotations for `boto3.resource("iam").attach_role` method.

[Policy.attach_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attach_role)

```python
def attach_role(
    self,
    RoleName: str
) -> None:
    pass
```

#### Policy.attach_user

Type annotations for `boto3.resource("iam").attach_user` method.

[Policy.attach_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attach_user)

```python
def attach_user(
    self,
    UserName: str
) -> None:
    pass
```

#### Policy.create_version

Type annotations for `boto3.resource("iam").create_version` method.

[Policy.create_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.create_version)

```python
def create_version(
    self,
    PolicyDocument: str,
    SetAsDefault: bool = None
) -> _PolicyVersion:
    pass
```

#### Policy.delete

Type annotations for `boto3.resource("iam").delete` method.

[Policy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Policy.detach_group

Type annotations for `boto3.resource("iam").detach_group` method.

[Policy.detach_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.detach_group)

```python
def detach_group(
    self,
    GroupName: str
) -> None:
    pass
```

#### Policy.detach_role

Type annotations for `boto3.resource("iam").detach_role` method.

[Policy.detach_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.detach_role)

```python
def detach_role(
    self,
    RoleName: str
) -> None:
    pass
```

#### Policy.detach_user

Type annotations for `boto3.resource("iam").detach_user` method.

[Policy.detach_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.detach_user)

```python
def detach_user(
    self,
    UserName: str
) -> None:
    pass
```

#### Policy.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[Policy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Policy.load

Type annotations for `boto3.resource("iam").load` method.

[Policy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.load)

```python
def load(
    self
) -> None:
    pass
```

#### Policy.reload

Type annotations for `boto3.resource("iam").reload` method.

[Policy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.reload)

```python
def reload(
    self
) -> None:
    pass
```




### Policy collections


#### Policy.attached_groups

Type annotations for `boto3.resource("iam").Policy(...).attached_groups` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import PolicyAttachedGroupsCollection,

def get_collection() -> PolicyAttachedGroupsCollection:
    resource = boto3.resource("iam").Policy(...)
    return resource.attached_groups
```

[Policy.attached_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attached_groups)

```python
class PolicyAttachedGroupsCollection(ResourceCollection):
    def all(
        self
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Group"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Group"]:
        pass
```

#### Policy.attached_roles

Type annotations for `boto3.resource("iam").Policy(...).attached_roles` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import PolicyAttachedRolesCollection,

def get_collection() -> PolicyAttachedRolesCollection:
    resource = boto3.resource("iam").Policy(...)
    return resource.attached_roles
```

[Policy.attached_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attached_roles)

```python
class PolicyAttachedRolesCollection(ResourceCollection):
    def all(
        self
    ) -> "PolicyAttachedRolesCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "PolicyAttachedRolesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "PolicyAttachedRolesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "PolicyAttachedRolesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Role"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Role"]:
        pass
```

#### Policy.attached_users

Type annotations for `boto3.resource("iam").Policy(...).attached_users` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import PolicyAttachedUsersCollection,

def get_collection() -> PolicyAttachedUsersCollection:
    resource = boto3.resource("iam").Policy(...)
    return resource.attached_users
```

[Policy.attached_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attached_users)

```python
class PolicyAttachedUsersCollection(ResourceCollection):
    def all(
        self
    ) -> "PolicyAttachedUsersCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "PolicyAttachedUsersCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "PolicyAttachedUsersCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "PolicyAttachedUsersCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["User"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["User"]:
        pass
```

#### Policy.versions

Type annotations for `boto3.resource("iam").Policy(...).versions` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import PolicyVersionsCollection,

def get_collection() -> PolicyVersionsCollection:
    resource = boto3.resource("iam").Policy(...)
    return resource.versions
```

[Policy.versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.versions)

```python
class PolicyVersionsCollection(ResourceCollection):
    def all(
        self
    ) -> "PolicyVersionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "PolicyVersionsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "PolicyVersionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "PolicyVersionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["PolicyVersion"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["PolicyVersion"]:
        pass
```




## PolicyVersion

Type annotations for `boto3.resource("iam").PolicyVersion` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import PolicyVersion

def get_resource() -> PolicyVersion:
    return boto3.resource("iam").PolicyVersion(...)
```

[PolicyVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)


### PolicyVersion attributes


- `document`: `str`

- `is_default_version`: `bool`

- `create_date`: `datetime`

- `arn`: `str`

- `version_id`: `str`




### PolicyVersion methods


#### PolicyVersion.delete

Type annotations for `boto3.resource("iam").delete` method.

[PolicyVersion.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### PolicyVersion.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[PolicyVersion.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### PolicyVersion.load

Type annotations for `boto3.resource("iam").load` method.

[PolicyVersion.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.load)

```python
def load(
    self
) -> None:
    pass
```

#### PolicyVersion.reload

Type annotations for `boto3.resource("iam").reload` method.

[PolicyVersion.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### PolicyVersion.set_as_default

Type annotations for `boto3.resource("iam").set_as_default` method.

[PolicyVersion.set_as_default documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.set_as_default)

```python
def set_as_default(
    self
) -> None:
    pass
```






## Role

Type annotations for `boto3.resource("iam").Role` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import Role

def get_resource() -> Role:
    return boto3.resource("iam").Role(...)
```

[Role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Role)


### Role attributes


- `path`: `str`

- `role_name`: `str`

- `role_id`: `str`

- `arn`: `str`

- `create_date`: `datetime`

- `assume_role_policy_document`: `str`

- `description`: `str`

- `max_session_duration`: `int`

- `permissions_boundary`: `Dict[str, Any]`

- `tags`: `List[Any]`

- `role_last_used`: `Dict[str, Any]`

- `name`: `str`

- `attached_policies`: `RoleAttachedPoliciesCollection`

- `instance_profiles`: `RoleInstanceProfilesCollection`

- `policies`: `RolePoliciesCollection`




### Role methods


#### Role.AssumeRolePolicy

Type annotations for `boto3.resource("iam").AssumeRolePolicy` method.

[Role.AssumeRolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.AssumeRolePolicy)

```python
def AssumeRolePolicy(
    self
) -> _AssumeRolePolicy:
    pass
```

#### Role.Policy

Type annotations for `boto3.resource("iam").Policy` method.

[Role.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.Policy)

```python
def Policy(
    self,
    name: str
) -> _RolePolicy:
    pass
```

#### Role.attach_policy

Type annotations for `boto3.resource("iam").attach_policy` method.

[Role.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.attach_policy)

```python
def attach_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

#### Role.delete

Type annotations for `boto3.resource("iam").delete` method.

[Role.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Role.detach_policy

Type annotations for `boto3.resource("iam").detach_policy` method.

[Role.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.detach_policy)

```python
def detach_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

#### Role.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[Role.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Role.load

Type annotations for `boto3.resource("iam").load` method.

[Role.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.load)

```python
def load(
    self
) -> None:
    pass
```

#### Role.reload

Type annotations for `boto3.resource("iam").reload` method.

[Role.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.reload)

```python
def reload(
    self
) -> None:
    pass
```




### Role collections


#### Role.attached_policies

Type annotations for `boto3.resource("iam").Role(...).attached_policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import RoleAttachedPoliciesCollection,

def get_collection() -> RoleAttachedPoliciesCollection:
    resource = boto3.resource("iam").Role(...)
    return resource.attached_policies
```

[Role.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.attached_policies)

```python
class RoleAttachedPoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Policy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Policy"]:
        pass
```

#### Role.instance_profiles

Type annotations for `boto3.resource("iam").Role(...).instance_profiles` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import RoleInstanceProfilesCollection,

def get_collection() -> RoleInstanceProfilesCollection:
    resource = boto3.resource("iam").Role(...)
    return resource.instance_profiles
```

[Role.instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.instance_profiles)

```python
class RoleInstanceProfilesCollection(ResourceCollection):
    def all(
        self
    ) -> "RoleInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "RoleInstanceProfilesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "RoleInstanceProfilesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "RoleInstanceProfilesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["InstanceProfile"]:
        pass
```

#### Role.policies

Type annotations for `boto3.resource("iam").Role(...).policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import RolePoliciesCollection,

def get_collection() -> RolePoliciesCollection:
    resource = boto3.resource("iam").Role(...)
    return resource.policies
```

[Role.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.policies)

```python
class RolePoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "RolePoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "RolePoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "RolePoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "RolePoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["RolePolicy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["RolePolicy"]:
        pass
```




## RolePolicy

Type annotations for `boto3.resource("iam").RolePolicy` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import RolePolicy

def get_resource() -> RolePolicy:
    return boto3.resource("iam").RolePolicy(...)
```

[RolePolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.RolePolicy)


### RolePolicy attributes


- `policy_name`: `str`

- `policy_document`: `str`

- `role_name`: `str`

- `name`: `str`




### RolePolicy methods


#### RolePolicy.Role

Type annotations for `boto3.resource("iam").Role` method.

[RolePolicy.Role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.Role)

```python
def Role(
    self
) -> _Role:
    pass
```

#### RolePolicy.delete

Type annotations for `boto3.resource("iam").delete` method.

[RolePolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### RolePolicy.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[RolePolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### RolePolicy.load

Type annotations for `boto3.resource("iam").load` method.

[RolePolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.load)

```python
def load(
    self
) -> None:
    pass
```

#### RolePolicy.put

Type annotations for `boto3.resource("iam").put` method.

[RolePolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.put)

```python
def put(
    self,
    PolicyDocument: str
) -> None:
    pass
```

#### RolePolicy.reload

Type annotations for `boto3.resource("iam").reload` method.

[RolePolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.reload)

```python
def reload(
    self
) -> None:
    pass
```






## SamlProvider

Type annotations for `boto3.resource("iam").SamlProvider` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import SamlProvider

def get_resource() -> SamlProvider:
    return boto3.resource("iam").SamlProvider(...)
```

[SamlProvider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SamlProvider)


### SamlProvider attributes


- `saml_metadata_document`: `str`

- `create_date`: `datetime`

- `valid_until`: `datetime`

- `tags`: `List[Any]`

- `arn`: `str`




### SamlProvider methods


#### SamlProvider.delete

Type annotations for `boto3.resource("iam").delete` method.

[SamlProvider.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### SamlProvider.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[SamlProvider.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### SamlProvider.load

Type annotations for `boto3.resource("iam").load` method.

[SamlProvider.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.load)

```python
def load(
    self
) -> None:
    pass
```

#### SamlProvider.reload

Type annotations for `boto3.resource("iam").reload` method.

[SamlProvider.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### SamlProvider.update

Type annotations for `boto3.resource("iam").update` method.

[SamlProvider.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.update)

```python
def update(
    self,
    SAMLMetadataDocument: str
) -> UpdateSAMLProviderResponseTypeDef:
    pass
```






## ServerCertificate

Type annotations for `boto3.resource("iam").ServerCertificate` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import ServerCertificate

def get_resource() -> ServerCertificate:
    return boto3.resource("iam").ServerCertificate(...)
```

[ServerCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)


### ServerCertificate attributes


- `server_certificate_metadata`: `Dict[str, Any]`

- `certificate_body`: `str`

- `certificate_chain`: `str`

- `tags`: `List[Any]`

- `name`: `str`




### ServerCertificate methods


#### ServerCertificate.delete

Type annotations for `boto3.resource("iam").delete` method.

[ServerCertificate.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### ServerCertificate.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[ServerCertificate.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### ServerCertificate.load

Type annotations for `boto3.resource("iam").load` method.

[ServerCertificate.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.load)

```python
def load(
    self
) -> None:
    pass
```

#### ServerCertificate.reload

Type annotations for `boto3.resource("iam").reload` method.

[ServerCertificate.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### ServerCertificate.update

Type annotations for `boto3.resource("iam").update` method.

[ServerCertificate.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.update)

```python
def update(
    self,
    NewPath: str = None,
    NewServerCertificateName: str = None
) -> _ServerCertificate:
    pass
```






## SigningCertificate

Type annotations for `boto3.resource("iam").SigningCertificate` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import SigningCertificate

def get_resource() -> SigningCertificate:
    return boto3.resource("iam").SigningCertificate(...)
```

[SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)


### SigningCertificate attributes


- `certificate_id`: `str`

- `certificate_body`: `str`

- `status`: `str`

- `upload_date`: `datetime`

- `user_name`: `str`

- `id`: `str`




### SigningCertificate methods


#### SigningCertificate.User

Type annotations for `boto3.resource("iam").User` method.

[SigningCertificate.User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.User)

```python
def User(
    self
) -> _User:
    pass
```

#### SigningCertificate.activate

Type annotations for `boto3.resource("iam").activate` method.

[SigningCertificate.activate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.activate)

```python
def activate(
    self,
    Status: statusType
) -> None:
    pass
```

#### SigningCertificate.deactivate

Type annotations for `boto3.resource("iam").deactivate` method.

[SigningCertificate.deactivate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.deactivate)

```python
def deactivate(
    self,
    Status: statusType
) -> None:
    pass
```

#### SigningCertificate.delete

Type annotations for `boto3.resource("iam").delete` method.

[SigningCertificate.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### SigningCertificate.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[SigningCertificate.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```






## User

Type annotations for `boto3.resource("iam").User` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import User

def get_resource() -> User:
    return boto3.resource("iam").User(...)
```

[User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.User)


### User attributes


- `path`: `str`

- `user_name`: `str`

- `user_id`: `str`

- `arn`: `str`

- `create_date`: `datetime`

- `password_last_used`: `datetime`

- `permissions_boundary`: `Dict[str, Any]`

- `tags`: `List[Any]`

- `name`: `str`

- `access_keys`: `UserAccessKeysCollection`

- `attached_policies`: `UserAttachedPoliciesCollection`

- `groups`: `UserGroupsCollection`

- `mfa_devices`: `UserMfaDevicesCollection`

- `policies`: `UserPoliciesCollection`

- `signing_certificates`: `UserSigningCertificatesCollection`




### User methods


#### User.AccessKey

Type annotations for `boto3.resource("iam").AccessKey` method.

[User.AccessKey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.AccessKey)

```python
def AccessKey(
    self,
    id: str
) -> _AccessKey:
    pass
```

#### User.LoginProfile

Type annotations for `boto3.resource("iam").LoginProfile` method.

[User.LoginProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.LoginProfile)

```python
def LoginProfile(
    self
) -> _LoginProfile:
    pass
```

#### User.MfaDevice

Type annotations for `boto3.resource("iam").MfaDevice` method.

[User.MfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.MfaDevice)

```python
def MfaDevice(
    self,
    serial_number: str
) -> _MfaDevice:
    pass
```

#### User.Policy

Type annotations for `boto3.resource("iam").Policy` method.

[User.Policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.Policy)

```python
def Policy(
    self,
    name: str
) -> _UserPolicy:
    pass
```

#### User.SigningCertificate

Type annotations for `boto3.resource("iam").SigningCertificate` method.

[User.SigningCertificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.SigningCertificate)

```python
def SigningCertificate(
    self,
    id: str
) -> _SigningCertificate:
    pass
```

#### User.add_group

Type annotations for `boto3.resource("iam").add_group` method.

[User.add_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.add_group)

```python
def add_group(
    self,
    GroupName: str
) -> None:
    pass
```

#### User.attach_policy

Type annotations for `boto3.resource("iam").attach_policy` method.

[User.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.attach_policy)

```python
def attach_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

#### User.create

Type annotations for `boto3.resource("iam").create` method.

[User.create documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create)

```python
def create(
    self,
    Path: str = None,
    PermissionsBoundary: str = None,
    Tags: List["TagTypeDef"] = None
) -> _User:
    pass
```

#### User.create_access_key_pair

Type annotations for `boto3.resource("iam").create_access_key_pair` method.

[User.create_access_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create_access_key_pair)

```python
def create_access_key_pair(
    self
) -> _AccessKeyPair:
    pass
```

#### User.create_login_profile

Type annotations for `boto3.resource("iam").create_login_profile` method.

[User.create_login_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create_login_profile)

```python
def create_login_profile(
    self,
    Password: str,
    PasswordResetRequired: bool = None
) -> _LoginProfile:
    pass
```

#### User.create_policy

Type annotations for `boto3.resource("iam").create_policy` method.

[User.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create_policy)

```python
def create_policy(
    self,
    PolicyName: str,
    PolicyDocument: str
) -> _UserPolicy:
    pass
```

#### User.delete

Type annotations for `boto3.resource("iam").delete` method.

[User.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### User.detach_policy

Type annotations for `boto3.resource("iam").detach_policy` method.

[User.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.detach_policy)

```python
def detach_policy(
    self,
    PolicyArn: str
) -> None:
    pass
```

#### User.enable_mfa

Type annotations for `boto3.resource("iam").enable_mfa` method.

[User.enable_mfa documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.enable_mfa)

```python
def enable_mfa(
    self,
    SerialNumber: str,
    AuthenticationCode1: str,
    AuthenticationCode2: str
) -> _MfaDevice:
    pass
```

#### User.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[User.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### User.load

Type annotations for `boto3.resource("iam").load` method.

[User.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.load)

```python
def load(
    self
) -> None:
    pass
```

#### User.reload

Type annotations for `boto3.resource("iam").reload` method.

[User.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### User.remove_group

Type annotations for `boto3.resource("iam").remove_group` method.

[User.remove_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.remove_group)

```python
def remove_group(
    self,
    GroupName: str
) -> None:
    pass
```

#### User.update

Type annotations for `boto3.resource("iam").update` method.

[User.update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.update)

```python
def update(
    self,
    NewPath: str = None,
    NewUserName: str = None
) -> _User:
    pass
```




### User collections


#### User.access_keys

Type annotations for `boto3.resource("iam").User(...).access_keys` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserAccessKeysCollection,

def get_collection() -> UserAccessKeysCollection:
    resource = boto3.resource("iam").User(...)
    return resource.access_keys
```

[User.access_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.access_keys)

```python
class UserAccessKeysCollection(ResourceCollection):
    def all(
        self
    ) -> "UserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self,
        UserName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "UserAccessKeysCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "UserAccessKeysCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "UserAccessKeysCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["AccessKey"]:
        pass
```

#### User.attached_policies

Type annotations for `boto3.resource("iam").User(...).attached_policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserAttachedPoliciesCollection,

def get_collection() -> UserAttachedPoliciesCollection:
    resource = boto3.resource("iam").User(...)
    return resource.attached_policies
```

[User.attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.attached_policies)

```python
class UserAttachedPoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "UserAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        PathPrefix: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "UserAttachedPoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "UserAttachedPoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "UserAttachedPoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Policy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Policy"]:
        pass
```

#### User.groups

Type annotations for `boto3.resource("iam").User(...).groups` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserGroupsCollection,

def get_collection() -> UserGroupsCollection:
    resource = boto3.resource("iam").User(...)
    return resource.groups
```

[User.groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.groups)

```python
class UserGroupsCollection(ResourceCollection):
    def all(
        self
    ) -> "UserGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "UserGroupsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "UserGroupsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "UserGroupsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Group"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Group"]:
        pass
```

#### User.mfa_devices

Type annotations for `boto3.resource("iam").User(...).mfa_devices` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserMfaDevicesCollection,

def get_collection() -> UserMfaDevicesCollection:
    resource = boto3.resource("iam").User(...)
    return resource.mfa_devices
```

[User.mfa_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.mfa_devices)

```python
class UserMfaDevicesCollection(ResourceCollection):
    def all(
        self
    ) -> "UserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self,
        UserName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "UserMfaDevicesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "UserMfaDevicesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "UserMfaDevicesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["MfaDevice"]:
        pass
```

#### User.policies

Type annotations for `boto3.resource("iam").User(...).policies` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserPoliciesCollection,

def get_collection() -> UserPoliciesCollection:
    resource = boto3.resource("iam").User(...)
    return resource.policies
```

[User.policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.policies)

```python
class UserPoliciesCollection(ResourceCollection):
    def all(
        self
    ) -> "UserPoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Marker: str = None,
        MaxItems: int = None
    ) -> "UserPoliciesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "UserPoliciesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "UserPoliciesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["UserPolicy"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["UserPolicy"]:
        pass
```

#### User.signing_certificates

Type annotations for `boto3.resource("iam").User(...).signing_certificates` collection.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserSigningCertificatesCollection,

def get_collection() -> UserSigningCertificatesCollection:
    resource = boto3.resource("iam").User(...)
    return resource.signing_certificates
```

[User.signing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.signing_certificates)

```python
class UserSigningCertificatesCollection(ResourceCollection):
    def all(
        self
    ) -> "UserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self,
        UserName: str = None,
        Marker: str = None,
        MaxItems: int = None
    ) -> "UserSigningCertificatesCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "UserSigningCertificatesCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "UserSigningCertificatesCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["SigningCertificate"]:
        pass
```




## UserPolicy

Type annotations for `boto3.resource("iam").UserPolicy` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import UserPolicy

def get_resource() -> UserPolicy:
    return boto3.resource("iam").UserPolicy(...)
```

[UserPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.UserPolicy)


### UserPolicy attributes


- `policy_name`: `str`

- `policy_document`: `str`

- `user_name`: `str`

- `name`: `str`




### UserPolicy methods


#### UserPolicy.User

Type annotations for `boto3.resource("iam").User` method.

[UserPolicy.User documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.User)

```python
def User(
    self
) -> _User:
    pass
```

#### UserPolicy.delete

Type annotations for `boto3.resource("iam").delete` method.

[UserPolicy.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### UserPolicy.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[UserPolicy.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### UserPolicy.load

Type annotations for `boto3.resource("iam").load` method.

[UserPolicy.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.load)

```python
def load(
    self
) -> None:
    pass
```

#### UserPolicy.put

Type annotations for `boto3.resource("iam").put` method.

[UserPolicy.put documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.put)

```python
def put(
    self,
    PolicyDocument: str
) -> None:
    pass
```

#### UserPolicy.reload

Type annotations for `boto3.resource("iam").reload` method.

[UserPolicy.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.reload)

```python
def reload(
    self
) -> None:
    pass
```






## VirtualMfaDevice

Type annotations for `boto3.resource("iam").VirtualMfaDevice` class.

Can be used directly:

```python
from mypy_boto3_iam.service_resource import VirtualMfaDevice

def get_resource() -> VirtualMfaDevice:
    return boto3.resource("iam").VirtualMfaDevice(...)
```

[VirtualMfaDevice documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)


### VirtualMfaDevice attributes


- `base32_string_seed`: `bytes`

- `qr_code_png`: `bytes`

- `user_attribute`: `Dict[str, Any]`

- `enable_date`: `datetime`

- `tags`: `List[Any]`

- `serial_number`: `str`

- `user`: `"User"`




### VirtualMfaDevice methods


#### VirtualMfaDevice.delete

Type annotations for `boto3.resource("iam").delete` method.

[VirtualMfaDevice.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.VirtualMfaDevice.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### VirtualMfaDevice.get_available_subresources

Type annotations for `boto3.resource("iam").get_available_subresources` method.

[VirtualMfaDevice.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.VirtualMfaDevice.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




