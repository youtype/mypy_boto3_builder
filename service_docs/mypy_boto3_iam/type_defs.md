# Structures for boto3 IAM module

> [Index](../index.md) > [IAM](./index.md) > Structures

Auto-generated documentation for [IAM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM)
type annotations stubs module [mypy_boto3_iam](https://pypi.org/project/mypy-boto3-iam/).

- [Structures for boto3 IAM module](#structures-for-boto3-iam-module)
  - [AccessDetailTypeDef](#accessdetailtypedef)
  - [AccessKeyLastUsedTypeDef](#accesskeylastusedtypedef)
  - [AccessKeyMetadataTypeDef](#accesskeymetadatatypedef)
  - [AccessKeyTypeDef](#accesskeytypedef)
  - [AttachedPermissionsBoundaryTypeDef](#attachedpermissionsboundarytypedef)
  - [AttachedPolicyTypeDef](#attachedpolicytypedef)
  - [ContextEntryTypeDef](#contextentrytypedef)
  - [CreateAccessKeyResponseTypeDef](#createaccesskeyresponsetypedef)
  - [CreateGroupResponseTypeDef](#creategroupresponsetypedef)
  - [CreateInstanceProfileResponseTypeDef](#createinstanceprofileresponsetypedef)
  - [CreateLoginProfileResponseTypeDef](#createloginprofileresponsetypedef)
  - [CreateOpenIDConnectProviderResponseTypeDef](#createopenidconnectproviderresponsetypedef)
  - [CreatePolicyResponseTypeDef](#createpolicyresponsetypedef)
  - [CreatePolicyVersionResponseTypeDef](#createpolicyversionresponsetypedef)
  - [CreateRoleResponseTypeDef](#createroleresponsetypedef)
  - [CreateSAMLProviderResponseTypeDef](#createsamlproviderresponsetypedef)
  - [CreateServiceLinkedRoleResponseTypeDef](#createservicelinkedroleresponsetypedef)
  - [CreateServiceSpecificCredentialResponseTypeDef](#createservicespecificcredentialresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [CreateVirtualMFADeviceResponseTypeDef](#createvirtualmfadeviceresponsetypedef)
  - [DeleteServiceLinkedRoleResponseTypeDef](#deleteservicelinkedroleresponsetypedef)
  - [DeletionTaskFailureReasonTypeTypeDef](#deletiontaskfailurereasontypetypedef)
  - [EntityDetailsTypeDef](#entitydetailstypedef)
  - [EntityInfoTypeDef](#entityinfotypedef)
  - [ErrorDetailsTypeDef](#errordetailstypedef)
  - [EvaluationResultTypeDef](#evaluationresulttypedef)
  - [GenerateCredentialReportResponseTypeDef](#generatecredentialreportresponsetypedef)
  - [GenerateOrganizationsAccessReportResponseTypeDef](#generateorganizationsaccessreportresponsetypedef)
  - [GenerateServiceLastAccessedDetailsResponseTypeDef](#generateservicelastaccesseddetailsresponsetypedef)
  - [GetAccessKeyLastUsedResponseTypeDef](#getaccesskeylastusedresponsetypedef)
  - [GetAccountAuthorizationDetailsResponseTypeDef](#getaccountauthorizationdetailsresponsetypedef)
  - [GetAccountPasswordPolicyResponseTypeDef](#getaccountpasswordpolicyresponsetypedef)
  - [GetAccountSummaryResponseTypeDef](#getaccountsummaryresponsetypedef)
  - [GetContextKeysForPolicyResponseTypeDef](#getcontextkeysforpolicyresponsetypedef)
  - [GetCredentialReportResponseTypeDef](#getcredentialreportresponsetypedef)
  - [GetGroupPolicyResponseTypeDef](#getgrouppolicyresponsetypedef)
  - [GetGroupResponseTypeDef](#getgroupresponsetypedef)
  - [GetInstanceProfileResponseTypeDef](#getinstanceprofileresponsetypedef)
  - [GetLoginProfileResponseTypeDef](#getloginprofileresponsetypedef)
  - [GetOpenIDConnectProviderResponseTypeDef](#getopenidconnectproviderresponsetypedef)
  - [GetOrganizationsAccessReportResponseTypeDef](#getorganizationsaccessreportresponsetypedef)
  - [GetPolicyResponseTypeDef](#getpolicyresponsetypedef)
  - [GetPolicyVersionResponseTypeDef](#getpolicyversionresponsetypedef)
  - [GetRolePolicyResponseTypeDef](#getrolepolicyresponsetypedef)
  - [GetRoleResponseTypeDef](#getroleresponsetypedef)
  - [GetSAMLProviderResponseTypeDef](#getsamlproviderresponsetypedef)
  - [GetSSHPublicKeyResponseTypeDef](#getsshpublickeyresponsetypedef)
  - [GetServerCertificateResponseTypeDef](#getservercertificateresponsetypedef)
  - [GetServiceLastAccessedDetailsResponseTypeDef](#getservicelastaccesseddetailsresponsetypedef)
  - [GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef](#getservicelastaccesseddetailswithentitiesresponsetypedef)
  - [GetServiceLinkedRoleDeletionStatusResponseTypeDef](#getservicelinkedroledeletionstatusresponsetypedef)
  - [GetUserPolicyResponseTypeDef](#getuserpolicyresponsetypedef)
  - [GetUserResponseTypeDef](#getuserresponsetypedef)
  - [GroupDetailTypeDef](#groupdetailtypedef)
  - [GroupTypeDef](#grouptypedef)
  - [InstanceProfileTypeDef](#instanceprofiletypedef)
  - [ListAccessKeysResponseTypeDef](#listaccesskeysresponsetypedef)
  - [ListAccountAliasesResponseTypeDef](#listaccountaliasesresponsetypedef)
  - [ListAttachedGroupPoliciesResponseTypeDef](#listattachedgrouppoliciesresponsetypedef)
  - [ListAttachedRolePoliciesResponseTypeDef](#listattachedrolepoliciesresponsetypedef)
  - [ListAttachedUserPoliciesResponseTypeDef](#listattacheduserpoliciesresponsetypedef)
  - [ListEntitiesForPolicyResponseTypeDef](#listentitiesforpolicyresponsetypedef)
  - [ListGroupPoliciesResponseTypeDef](#listgrouppoliciesresponsetypedef)
  - [ListGroupsForUserResponseTypeDef](#listgroupsforuserresponsetypedef)
  - [ListGroupsResponseTypeDef](#listgroupsresponsetypedef)
  - [ListInstanceProfileTagsResponseTypeDef](#listinstanceprofiletagsresponsetypedef)
  - [ListInstanceProfilesForRoleResponseTypeDef](#listinstanceprofilesforroleresponsetypedef)
  - [ListInstanceProfilesResponseTypeDef](#listinstanceprofilesresponsetypedef)
  - [ListMFADeviceTagsResponseTypeDef](#listmfadevicetagsresponsetypedef)
  - [ListMFADevicesResponseTypeDef](#listmfadevicesresponsetypedef)
  - [ListOpenIDConnectProviderTagsResponseTypeDef](#listopenidconnectprovidertagsresponsetypedef)
  - [ListOpenIDConnectProvidersResponseTypeDef](#listopenidconnectprovidersresponsetypedef)
  - [ListPoliciesGrantingServiceAccessEntryTypeDef](#listpoliciesgrantingserviceaccessentrytypedef)
  - [ListPoliciesGrantingServiceAccessResponseTypeDef](#listpoliciesgrantingserviceaccessresponsetypedef)
  - [ListPoliciesResponseTypeDef](#listpoliciesresponsetypedef)
  - [ListPolicyTagsResponseTypeDef](#listpolicytagsresponsetypedef)
  - [ListPolicyVersionsResponseTypeDef](#listpolicyversionsresponsetypedef)
  - [ListRolePoliciesResponseTypeDef](#listrolepoliciesresponsetypedef)
  - [ListRoleTagsResponseTypeDef](#listroletagsresponsetypedef)
  - [ListRolesResponseTypeDef](#listrolesresponsetypedef)
  - [ListSAMLProviderTagsResponseTypeDef](#listsamlprovidertagsresponsetypedef)
  - [ListSAMLProvidersResponseTypeDef](#listsamlprovidersresponsetypedef)
  - [ListSSHPublicKeysResponseTypeDef](#listsshpublickeysresponsetypedef)
  - [ListServerCertificateTagsResponseTypeDef](#listservercertificatetagsresponsetypedef)
  - [ListServerCertificatesResponseTypeDef](#listservercertificatesresponsetypedef)
  - [ListServiceSpecificCredentialsResponseTypeDef](#listservicespecificcredentialsresponsetypedef)
  - [ListSigningCertificatesResponseTypeDef](#listsigningcertificatesresponsetypedef)
  - [ListUserPoliciesResponseTypeDef](#listuserpoliciesresponsetypedef)
  - [ListUserTagsResponseTypeDef](#listusertagsresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [ListVirtualMFADevicesResponseTypeDef](#listvirtualmfadevicesresponsetypedef)
  - [LoginProfileTypeDef](#loginprofiletypedef)
  - [MFADeviceTypeDef](#mfadevicetypedef)
  - [ManagedPolicyDetailTypeDef](#managedpolicydetailtypedef)
  - [OpenIDConnectProviderListEntryTypeDef](#openidconnectproviderlistentrytypedef)
  - [OrganizationsDecisionDetailTypeDef](#organizationsdecisiondetailtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PasswordPolicyTypeDef](#passwordpolicytypedef)
  - [PermissionsBoundaryDecisionDetailTypeDef](#permissionsboundarydecisiondetailtypedef)
  - [PolicyDetailTypeDef](#policydetailtypedef)
  - [PolicyGrantingServiceAccessTypeDef](#policygrantingserviceaccesstypedef)
  - [PolicyGroupTypeDef](#policygrouptypedef)
  - [PolicyRoleTypeDef](#policyroletypedef)
  - [PolicyTypeDef](#policytypedef)
  - [PolicyUserTypeDef](#policyusertypedef)
  - [PolicyVersionTypeDef](#policyversiontypedef)
  - [PositionTypeDef](#positiontypedef)
  - [ResetServiceSpecificCredentialResponseTypeDef](#resetservicespecificcredentialresponsetypedef)
  - [ResourceSpecificResultTypeDef](#resourcespecificresulttypedef)
  - [RoleDetailTypeDef](#roledetailtypedef)
  - [RoleLastUsedTypeDef](#rolelastusedtypedef)
  - [RoleTypeDef](#roletypedef)
  - [RoleUsageTypeTypeDef](#roleusagetypetypedef)
  - [SAMLProviderListEntryTypeDef](#samlproviderlistentrytypedef)
  - [SSHPublicKeyMetadataTypeDef](#sshpublickeymetadatatypedef)
  - [SSHPublicKeyTypeDef](#sshpublickeytypedef)
  - [ServerCertificateMetadataTypeDef](#servercertificatemetadatatypedef)
  - [ServerCertificateTypeDef](#servercertificatetypedef)
  - [ServiceLastAccessedTypeDef](#servicelastaccessedtypedef)
  - [ServiceSpecificCredentialMetadataTypeDef](#servicespecificcredentialmetadatatypedef)
  - [ServiceSpecificCredentialTypeDef](#servicespecificcredentialtypedef)
  - [SigningCertificateTypeDef](#signingcertificatetypedef)
  - [SimulatePolicyResponseTypeDef](#simulatepolicyresponsetypedef)
  - [StatementTypeDef](#statementtypedef)
  - [TagTypeDef](#tagtypedef)
  - [TrackedActionLastAccessedTypeDef](#trackedactionlastaccessedtypedef)
  - [UpdateRoleDescriptionResponseTypeDef](#updateroledescriptionresponsetypedef)
  - [UpdateSAMLProviderResponseTypeDef](#updatesamlproviderresponsetypedef)
  - [UploadSSHPublicKeyResponseTypeDef](#uploadsshpublickeyresponsetypedef)
  - [UploadServerCertificateResponseTypeDef](#uploadservercertificateresponsetypedef)
  - [UploadSigningCertificateResponseTypeDef](#uploadsigningcertificateresponsetypedef)
  - [UserDetailTypeDef](#userdetailtypedef)
  - [UserTypeDef](#usertypedef)
  - [VirtualMFADeviceTypeDef](#virtualmfadevicetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccessDetailTypeDef

```python
from mypy_boto3_iam.type_defs import AccessDetailTypeDef
```


Required fields:
- `ServiceName`: `str`
- `ServiceNamespace`: `str`



Optional fields:
- `Region`: `str`
- `EntityPath`: `str`
- `LastAuthenticatedTime`: `datetime`
- `TotalAuthenticatedEntities`: `int`


## AccessKeyLastUsedTypeDef

```python
from mypy_boto3_iam.type_defs import AccessKeyLastUsedTypeDef
```


Required fields:
- `LastUsedDate`: `datetime`
- `ServiceName`: `str`
- `Region`: `str`




## AccessKeyMetadataTypeDef

```python
from mypy_boto3_iam.type_defs import AccessKeyMetadataTypeDef
```




Optional fields:
- `UserName`: `str`
- `AccessKeyId`: `str`
- `Status`: `statusType`
- `CreateDate`: `datetime`


## AccessKeyTypeDef

```python
from mypy_boto3_iam.type_defs import AccessKeyTypeDef
```


Required fields:
- `UserName`: `str`
- `AccessKeyId`: `str`
- `Status`: `statusType`
- `SecretAccessKey`: `str`



Optional fields:
- `CreateDate`: `datetime`


## AttachedPermissionsBoundaryTypeDef

```python
from mypy_boto3_iam.type_defs import AttachedPermissionsBoundaryTypeDef
```




Optional fields:
- `PermissionsBoundaryType`: `Literal['PermissionsBoundaryPolicy']`
- `PermissionsBoundaryArn`: `str`


## AttachedPolicyTypeDef

```python
from mypy_boto3_iam.type_defs import AttachedPolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `PolicyArn`: `str`


## ContextEntryTypeDef

```python
from mypy_boto3_iam.type_defs import ContextEntryTypeDef
```




Optional fields:
- `ContextKeyName`: `str`
- `ContextKeyValues`: `List[str]`
- `ContextKeyType`: `ContextKeyTypeEnum`


## CreateAccessKeyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateAccessKeyResponseTypeDef
```


Required fields:
- `AccessKey`: `"AccessKeyTypeDef"`




## CreateGroupResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateGroupResponseTypeDef
```


Required fields:
- `Group`: `"GroupTypeDef"`




## CreateInstanceProfileResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateInstanceProfileResponseTypeDef
```


Required fields:
- `InstanceProfile`: `"InstanceProfileTypeDef"`




## CreateLoginProfileResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateLoginProfileResponseTypeDef
```


Required fields:
- `LoginProfile`: `"LoginProfileTypeDef"`




## CreateOpenIDConnectProviderResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateOpenIDConnectProviderResponseTypeDef
```




Optional fields:
- `OpenIDConnectProviderArn`: `str`
- `Tags`: `List["TagTypeDef"]`


## CreatePolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreatePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`


## CreatePolicyVersionResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreatePolicyVersionResponseTypeDef
```




Optional fields:
- `PolicyVersion`: `"PolicyVersionTypeDef"`


## CreateRoleResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateRoleResponseTypeDef
```


Required fields:
- `Role`: `"RoleTypeDef"`




## CreateSAMLProviderResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateSAMLProviderResponseTypeDef
```




Optional fields:
- `SAMLProviderArn`: `str`
- `Tags`: `List["TagTypeDef"]`


## CreateServiceLinkedRoleResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateServiceLinkedRoleResponseTypeDef
```




Optional fields:
- `Role`: `"RoleTypeDef"`


## CreateServiceSpecificCredentialResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateServiceSpecificCredentialResponseTypeDef
```




Optional fields:
- `ServiceSpecificCredential`: `"ServiceSpecificCredentialTypeDef"`


## CreateUserResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## CreateVirtualMFADeviceResponseTypeDef

```python
from mypy_boto3_iam.type_defs import CreateVirtualMFADeviceResponseTypeDef
```


Required fields:
- `VirtualMFADevice`: `"VirtualMFADeviceTypeDef"`




## DeleteServiceLinkedRoleResponseTypeDef

```python
from mypy_boto3_iam.type_defs import DeleteServiceLinkedRoleResponseTypeDef
```


Required fields:
- `DeletionTaskId`: `str`




## DeletionTaskFailureReasonTypeTypeDef

```python
from mypy_boto3_iam.type_defs import DeletionTaskFailureReasonTypeTypeDef
```




Optional fields:
- `Reason`: `str`
- `RoleUsageList`: `List["RoleUsageTypeTypeDef"]`


## EntityDetailsTypeDef

```python
from mypy_boto3_iam.type_defs import EntityDetailsTypeDef
```


Required fields:
- `EntityInfo`: `"EntityInfoTypeDef"`



Optional fields:
- `LastAuthenticated`: `datetime`


## EntityInfoTypeDef

```python
from mypy_boto3_iam.type_defs import EntityInfoTypeDef
```


Required fields:
- `Arn`: `str`
- `Name`: `str`
- `Type`: `policyOwnerEntityType`
- `Id`: `str`



Optional fields:
- `Path`: `str`


## ErrorDetailsTypeDef

```python
from mypy_boto3_iam.type_defs import ErrorDetailsTypeDef
```


Required fields:
- `Message`: `str`
- `Code`: `str`




## EvaluationResultTypeDef

```python
from mypy_boto3_iam.type_defs import EvaluationResultTypeDef
```


Required fields:
- `EvalActionName`: `str`
- `EvalDecision`: `PolicyEvaluationDecisionType`



Optional fields:
- `EvalResourceName`: `str`
- `MatchedStatements`: `List["StatementTypeDef"]`
- `MissingContextValues`: `List[str]`
- `OrganizationsDecisionDetail`: `"OrganizationsDecisionDetailTypeDef"`
- `PermissionsBoundaryDecisionDetail`: `"PermissionsBoundaryDecisionDetailTypeDef"`
- `EvalDecisionDetails`: `Dict[str, PolicyEvaluationDecisionType]`
- `ResourceSpecificResults`: `List["ResourceSpecificResultTypeDef"]`


## GenerateCredentialReportResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GenerateCredentialReportResponseTypeDef
```




Optional fields:
- `State`: `ReportStateType`
- `Description`: `str`


## GenerateOrganizationsAccessReportResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GenerateOrganizationsAccessReportResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## GenerateServiceLastAccessedDetailsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GenerateServiceLastAccessedDetailsResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## GetAccessKeyLastUsedResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetAccessKeyLastUsedResponseTypeDef
```




Optional fields:
- `UserName`: `str`
- `AccessKeyLastUsed`: `"AccessKeyLastUsedTypeDef"`


## GetAccountAuthorizationDetailsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetAccountAuthorizationDetailsResponseTypeDef
```




Optional fields:
- `UserDetailList`: `List["UserDetailTypeDef"]`
- `GroupDetailList`: `List["GroupDetailTypeDef"]`
- `RoleDetailList`: `List["RoleDetailTypeDef"]`
- `Policies`: `List["ManagedPolicyDetailTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## GetAccountPasswordPolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetAccountPasswordPolicyResponseTypeDef
```


Required fields:
- `PasswordPolicy`: `"PasswordPolicyTypeDef"`




## GetAccountSummaryResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetAccountSummaryResponseTypeDef
```




Optional fields:
- `SummaryMap`: `Dict[summaryKeyType, int]`


## GetContextKeysForPolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetContextKeysForPolicyResponseTypeDef
```




Optional fields:
- `ContextKeyNames`: `List[str]`


## GetCredentialReportResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetCredentialReportResponseTypeDef
```




Optional fields:
- `Content`: `Union[bytes, IO[bytes]]`
- `ReportFormat`: `Literal['text/csv']`
- `GeneratedTime`: `datetime`


## GetGroupPolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetGroupPolicyResponseTypeDef
```


Required fields:
- `GroupName`: `str`
- `PolicyName`: `str`
- `PolicyDocument`: `str`




## GetGroupResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetGroupResponseTypeDef
```


Required fields:
- `Group`: `"GroupTypeDef"`
- `Users`: `List["UserTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## GetInstanceProfileResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetInstanceProfileResponseTypeDef
```


Required fields:
- `InstanceProfile`: `"InstanceProfileTypeDef"`




## GetLoginProfileResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetLoginProfileResponseTypeDef
```


Required fields:
- `LoginProfile`: `"LoginProfileTypeDef"`




## GetOpenIDConnectProviderResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetOpenIDConnectProviderResponseTypeDef
```




Optional fields:
- `Url`: `str`
- `ClientIDList`: `List[str]`
- `ThumbprintList`: `List[str]`
- `CreateDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## GetOrganizationsAccessReportResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetOrganizationsAccessReportResponseTypeDef
```


Required fields:
- `JobStatus`: `jobStatusType`
- `JobCreationDate`: `datetime`



Optional fields:
- `JobCompletionDate`: `datetime`
- `NumberOfServicesAccessible`: `int`
- `NumberOfServicesNotAccessed`: `int`
- `AccessDetails`: `List["AccessDetailTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`
- `ErrorDetails`: `"ErrorDetailsTypeDef"`


## GetPolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`


## GetPolicyVersionResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetPolicyVersionResponseTypeDef
```




Optional fields:
- `PolicyVersion`: `"PolicyVersionTypeDef"`


## GetRolePolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetRolePolicyResponseTypeDef
```


Required fields:
- `RoleName`: `str`
- `PolicyName`: `str`
- `PolicyDocument`: `str`




## GetRoleResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetRoleResponseTypeDef
```


Required fields:
- `Role`: `"RoleTypeDef"`




## GetSAMLProviderResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetSAMLProviderResponseTypeDef
```




Optional fields:
- `SAMLMetadataDocument`: `str`
- `CreateDate`: `datetime`
- `ValidUntil`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## GetSSHPublicKeyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetSSHPublicKeyResponseTypeDef
```




Optional fields:
- `SSHPublicKey`: `"SSHPublicKeyTypeDef"`


## GetServerCertificateResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetServerCertificateResponseTypeDef
```


Required fields:
- `ServerCertificate`: `"ServerCertificateTypeDef"`




## GetServiceLastAccessedDetailsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetServiceLastAccessedDetailsResponseTypeDef
```


Required fields:
- `JobStatus`: `jobStatusType`
- `JobCreationDate`: `datetime`
- `ServicesLastAccessed`: `List["ServiceLastAccessedTypeDef"]`
- `JobCompletionDate`: `datetime`



Optional fields:
- `JobType`: `AccessAdvisorUsageGranularityType`
- `IsTruncated`: `bool`
- `Marker`: `str`
- `Error`: `"ErrorDetailsTypeDef"`


## GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef
```


Required fields:
- `JobStatus`: `jobStatusType`
- `JobCreationDate`: `datetime`
- `JobCompletionDate`: `datetime`
- `EntityDetailsList`: `List["EntityDetailsTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`
- `Error`: `"ErrorDetailsTypeDef"`


## GetServiceLinkedRoleDeletionStatusResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetServiceLinkedRoleDeletionStatusResponseTypeDef
```


Required fields:
- `Status`: `DeletionTaskStatusType`



Optional fields:
- `Reason`: `"DeletionTaskFailureReasonTypeTypeDef"`


## GetUserPolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetUserPolicyResponseTypeDef
```


Required fields:
- `UserName`: `str`
- `PolicyName`: `str`
- `PolicyDocument`: `str`




## GetUserResponseTypeDef

```python
from mypy_boto3_iam.type_defs import GetUserResponseTypeDef
```


Required fields:
- `User`: `"UserTypeDef"`




## GroupDetailTypeDef

```python
from mypy_boto3_iam.type_defs import GroupDetailTypeDef
```




Optional fields:
- `Path`: `str`
- `GroupName`: `str`
- `GroupId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`
- `GroupPolicyList`: `List["PolicyDetailTypeDef"]`
- `AttachedManagedPolicies`: `List["AttachedPolicyTypeDef"]`


## GroupTypeDef

```python
from mypy_boto3_iam.type_defs import GroupTypeDef
```


Required fields:
- `Path`: `str`
- `GroupName`: `str`
- `GroupId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`




## InstanceProfileTypeDef

```python
from mypy_boto3_iam.type_defs import InstanceProfileTypeDef
```


Required fields:
- `Path`: `str`
- `InstanceProfileName`: `str`
- `InstanceProfileId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`
- `Roles`: `List["RoleTypeDef"]`



Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListAccessKeysResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListAccessKeysResponseTypeDef
```


Required fields:
- `AccessKeyMetadata`: `List["AccessKeyMetadataTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListAccountAliasesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListAccountAliasesResponseTypeDef
```


Required fields:
- `AccountAliases`: `List[str]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListAttachedGroupPoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListAttachedGroupPoliciesResponseTypeDef
```




Optional fields:
- `AttachedPolicies`: `List["AttachedPolicyTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListAttachedRolePoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListAttachedRolePoliciesResponseTypeDef
```




Optional fields:
- `AttachedPolicies`: `List["AttachedPolicyTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListAttachedUserPoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListAttachedUserPoliciesResponseTypeDef
```




Optional fields:
- `AttachedPolicies`: `List["AttachedPolicyTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListEntitiesForPolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListEntitiesForPolicyResponseTypeDef
```




Optional fields:
- `PolicyGroups`: `List["PolicyGroupTypeDef"]`
- `PolicyUsers`: `List["PolicyUserTypeDef"]`
- `PolicyRoles`: `List["PolicyRoleTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListGroupPoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListGroupPoliciesResponseTypeDef
```


Required fields:
- `PolicyNames`: `List[str]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListGroupsForUserResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListGroupsForUserResponseTypeDef
```


Required fields:
- `Groups`: `List["GroupTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListGroupsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListGroupsResponseTypeDef
```


Required fields:
- `Groups`: `List["GroupTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListInstanceProfileTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListInstanceProfileTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListInstanceProfilesForRoleResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListInstanceProfilesForRoleResponseTypeDef
```


Required fields:
- `InstanceProfiles`: `List["InstanceProfileTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListInstanceProfilesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListInstanceProfilesResponseTypeDef
```


Required fields:
- `InstanceProfiles`: `List["InstanceProfileTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListMFADeviceTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListMFADeviceTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListMFADevicesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListMFADevicesResponseTypeDef
```


Required fields:
- `MFADevices`: `List["MFADeviceTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListOpenIDConnectProviderTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListOpenIDConnectProviderTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListOpenIDConnectProvidersResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListOpenIDConnectProvidersResponseTypeDef
```




Optional fields:
- `OpenIDConnectProviderList`: `List["OpenIDConnectProviderListEntryTypeDef"]`


## ListPoliciesGrantingServiceAccessEntryTypeDef

```python
from mypy_boto3_iam.type_defs import ListPoliciesGrantingServiceAccessEntryTypeDef
```




Optional fields:
- `ServiceNamespace`: `str`
- `Policies`: `List["PolicyGrantingServiceAccessTypeDef"]`


## ListPoliciesGrantingServiceAccessResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListPoliciesGrantingServiceAccessResponseTypeDef
```


Required fields:
- `PoliciesGrantingServiceAccess`: `List["ListPoliciesGrantingServiceAccessEntryTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListPoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListPoliciesResponseTypeDef
```




Optional fields:
- `Policies`: `List["PolicyTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListPolicyTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListPolicyTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListPolicyVersionsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListPolicyVersionsResponseTypeDef
```




Optional fields:
- `Versions`: `List["PolicyVersionTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListRolePoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListRolePoliciesResponseTypeDef
```


Required fields:
- `PolicyNames`: `List[str]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListRoleTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListRoleTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListRolesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListRolesResponseTypeDef
```


Required fields:
- `Roles`: `List["RoleTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListSAMLProviderTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListSAMLProviderTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListSAMLProvidersResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListSAMLProvidersResponseTypeDef
```




Optional fields:
- `SAMLProviderList`: `List["SAMLProviderListEntryTypeDef"]`


## ListSSHPublicKeysResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListSSHPublicKeysResponseTypeDef
```




Optional fields:
- `SSHPublicKeys`: `List["SSHPublicKeyMetadataTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListServerCertificateTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListServerCertificateTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListServerCertificatesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListServerCertificatesResponseTypeDef
```


Required fields:
- `ServerCertificateMetadataList`: `List["ServerCertificateMetadataTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListServiceSpecificCredentialsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListServiceSpecificCredentialsResponseTypeDef
```




Optional fields:
- `ServiceSpecificCredentials`: `List["ServiceSpecificCredentialMetadataTypeDef"]`


## ListSigningCertificatesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListSigningCertificatesResponseTypeDef
```


Required fields:
- `Certificates`: `List["SigningCertificateTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListUserPoliciesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListUserPoliciesResponseTypeDef
```


Required fields:
- `PolicyNames`: `List[str]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListUserTagsResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListUserTagsResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListUsersResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListUsersResponseTypeDef
```


Required fields:
- `Users`: `List["UserTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## ListVirtualMFADevicesResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ListVirtualMFADevicesResponseTypeDef
```


Required fields:
- `VirtualMFADevices`: `List["VirtualMFADeviceTypeDef"]`



Optional fields:
- `IsTruncated`: `bool`
- `Marker`: `str`


## LoginProfileTypeDef

```python
from mypy_boto3_iam.type_defs import LoginProfileTypeDef
```


Required fields:
- `UserName`: `str`
- `CreateDate`: `datetime`



Optional fields:
- `PasswordResetRequired`: `bool`


## MFADeviceTypeDef

```python
from mypy_boto3_iam.type_defs import MFADeviceTypeDef
```


Required fields:
- `UserName`: `str`
- `SerialNumber`: `str`
- `EnableDate`: `datetime`




## ManagedPolicyDetailTypeDef

```python
from mypy_boto3_iam.type_defs import ManagedPolicyDetailTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `PolicyId`: `str`
- `Arn`: `str`
- `Path`: `str`
- `DefaultVersionId`: `str`
- `AttachmentCount`: `int`
- `PermissionsBoundaryUsageCount`: `int`
- `IsAttachable`: `bool`
- `Description`: `str`
- `CreateDate`: `datetime`
- `UpdateDate`: `datetime`
- `PolicyVersionList`: `List["PolicyVersionTypeDef"]`


## OpenIDConnectProviderListEntryTypeDef

```python
from mypy_boto3_iam.type_defs import OpenIDConnectProviderListEntryTypeDef
```




Optional fields:
- `Arn`: `str`


## OrganizationsDecisionDetailTypeDef

```python
from mypy_boto3_iam.type_defs import OrganizationsDecisionDetailTypeDef
```




Optional fields:
- `AllowedByOrganizations`: `bool`


## PaginatorConfigTypeDef

```python
from mypy_boto3_iam.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PasswordPolicyTypeDef

```python
from mypy_boto3_iam.type_defs import PasswordPolicyTypeDef
```




Optional fields:
- `MinimumPasswordLength`: `int`
- `RequireSymbols`: `bool`
- `RequireNumbers`: `bool`
- `RequireUppercaseCharacters`: `bool`
- `RequireLowercaseCharacters`: `bool`
- `AllowUsersToChangePassword`: `bool`
- `ExpirePasswords`: `bool`
- `MaxPasswordAge`: `int`
- `PasswordReusePrevention`: `int`
- `HardExpiry`: `bool`


## PermissionsBoundaryDecisionDetailTypeDef

```python
from mypy_boto3_iam.type_defs import PermissionsBoundaryDecisionDetailTypeDef
```




Optional fields:
- `AllowedByPermissionsBoundary`: `bool`


## PolicyDetailTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyDetailTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `PolicyDocument`: `str`


## PolicyGrantingServiceAccessTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyGrantingServiceAccessTypeDef
```


Required fields:
- `PolicyName`: `str`
- `PolicyType`: `policyType`



Optional fields:
- `PolicyArn`: `str`
- `EntityType`: `policyOwnerEntityType`
- `EntityName`: `str`


## PolicyGroupTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyGroupTypeDef
```




Optional fields:
- `GroupName`: `str`
- `GroupId`: `str`


## PolicyRoleTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyRoleTypeDef
```




Optional fields:
- `RoleName`: `str`
- `RoleId`: `str`


## PolicyTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `PolicyId`: `str`
- `Arn`: `str`
- `Path`: `str`
- `DefaultVersionId`: `str`
- `AttachmentCount`: `int`
- `PermissionsBoundaryUsageCount`: `int`
- `IsAttachable`: `bool`
- `Description`: `str`
- `CreateDate`: `datetime`
- `UpdateDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## PolicyUserTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyUserTypeDef
```




Optional fields:
- `UserName`: `str`
- `UserId`: `str`


## PolicyVersionTypeDef

```python
from mypy_boto3_iam.type_defs import PolicyVersionTypeDef
```




Optional fields:
- `Document`: `str`
- `VersionId`: `str`
- `IsDefaultVersion`: `bool`
- `CreateDate`: `datetime`


## PositionTypeDef

```python
from mypy_boto3_iam.type_defs import PositionTypeDef
```




Optional fields:
- `Line`: `int`
- `Column`: `int`


## ResetServiceSpecificCredentialResponseTypeDef

```python
from mypy_boto3_iam.type_defs import ResetServiceSpecificCredentialResponseTypeDef
```




Optional fields:
- `ServiceSpecificCredential`: `"ServiceSpecificCredentialTypeDef"`


## ResourceSpecificResultTypeDef

```python
from mypy_boto3_iam.type_defs import ResourceSpecificResultTypeDef
```


Required fields:
- `EvalResourceName`: `str`
- `EvalResourceDecision`: `PolicyEvaluationDecisionType`



Optional fields:
- `MatchedStatements`: `List["StatementTypeDef"]`
- `MissingContextValues`: `List[str]`
- `EvalDecisionDetails`: `Dict[str, PolicyEvaluationDecisionType]`
- `PermissionsBoundaryDecisionDetail`: `"PermissionsBoundaryDecisionDetailTypeDef"`


## RoleDetailTypeDef

```python
from mypy_boto3_iam.type_defs import RoleDetailTypeDef
```




Optional fields:
- `Path`: `str`
- `RoleName`: `str`
- `RoleId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`
- `AssumeRolePolicyDocument`: `str`
- `InstanceProfileList`: `List["InstanceProfileTypeDef"]`
- `RolePolicyList`: `List["PolicyDetailTypeDef"]`
- `AttachedManagedPolicies`: `List["AttachedPolicyTypeDef"]`
- `PermissionsBoundary`: `"AttachedPermissionsBoundaryTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `RoleLastUsed`: `"RoleLastUsedTypeDef"`


## RoleLastUsedTypeDef

```python
from mypy_boto3_iam.type_defs import RoleLastUsedTypeDef
```




Optional fields:
- `LastUsedDate`: `datetime`
- `Region`: `str`


## RoleTypeDef

```python
from mypy_boto3_iam.type_defs import RoleTypeDef
```


Required fields:
- `Path`: `str`
- `RoleName`: `str`
- `RoleId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`



Optional fields:
- `AssumeRolePolicyDocument`: `str`
- `Description`: `str`
- `MaxSessionDuration`: `int`
- `PermissionsBoundary`: `"AttachedPermissionsBoundaryTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `RoleLastUsed`: `"RoleLastUsedTypeDef"`


## RoleUsageTypeTypeDef

```python
from mypy_boto3_iam.type_defs import RoleUsageTypeTypeDef
```




Optional fields:
- `Region`: `str`
- `Resources`: `List[str]`


## SAMLProviderListEntryTypeDef

```python
from mypy_boto3_iam.type_defs import SAMLProviderListEntryTypeDef
```




Optional fields:
- `Arn`: `str`
- `ValidUntil`: `datetime`
- `CreateDate`: `datetime`


## SSHPublicKeyMetadataTypeDef

```python
from mypy_boto3_iam.type_defs import SSHPublicKeyMetadataTypeDef
```


Required fields:
- `UserName`: `str`
- `SSHPublicKeyId`: `str`
- `Status`: `statusType`
- `UploadDate`: `datetime`




## SSHPublicKeyTypeDef

```python
from mypy_boto3_iam.type_defs import SSHPublicKeyTypeDef
```


Required fields:
- `UserName`: `str`
- `SSHPublicKeyId`: `str`
- `Fingerprint`: `str`
- `SSHPublicKeyBody`: `str`
- `Status`: `statusType`



Optional fields:
- `UploadDate`: `datetime`


## ServerCertificateMetadataTypeDef

```python
from mypy_boto3_iam.type_defs import ServerCertificateMetadataTypeDef
```


Required fields:
- `Path`: `str`
- `ServerCertificateName`: `str`
- `ServerCertificateId`: `str`
- `Arn`: `str`



Optional fields:
- `UploadDate`: `datetime`
- `Expiration`: `datetime`


## ServerCertificateTypeDef

```python
from mypy_boto3_iam.type_defs import ServerCertificateTypeDef
```


Required fields:
- `ServerCertificateMetadata`: `"ServerCertificateMetadataTypeDef"`
- `CertificateBody`: `str`



Optional fields:
- `CertificateChain`: `str`
- `Tags`: `List["TagTypeDef"]`


## ServiceLastAccessedTypeDef

```python
from mypy_boto3_iam.type_defs import ServiceLastAccessedTypeDef
```


Required fields:
- `ServiceName`: `str`
- `ServiceNamespace`: `str`



Optional fields:
- `LastAuthenticated`: `datetime`
- `LastAuthenticatedEntity`: `str`
- `LastAuthenticatedRegion`: `str`
- `TotalAuthenticatedEntities`: `int`
- `TrackedActionsLastAccessed`: `List["TrackedActionLastAccessedTypeDef"]`


## ServiceSpecificCredentialMetadataTypeDef

```python
from mypy_boto3_iam.type_defs import ServiceSpecificCredentialMetadataTypeDef
```


Required fields:
- `UserName`: `str`
- `Status`: `statusType`
- `ServiceUserName`: `str`
- `CreateDate`: `datetime`
- `ServiceSpecificCredentialId`: `str`
- `ServiceName`: `str`




## ServiceSpecificCredentialTypeDef

```python
from mypy_boto3_iam.type_defs import ServiceSpecificCredentialTypeDef
```


Required fields:
- `CreateDate`: `datetime`
- `ServiceName`: `str`
- `ServiceUserName`: `str`
- `ServicePassword`: `str`
- `ServiceSpecificCredentialId`: `str`
- `UserName`: `str`
- `Status`: `statusType`




## SigningCertificateTypeDef

```python
from mypy_boto3_iam.type_defs import SigningCertificateTypeDef
```


Required fields:
- `UserName`: `str`
- `CertificateId`: `str`
- `CertificateBody`: `str`
- `Status`: `statusType`



Optional fields:
- `UploadDate`: `datetime`


## SimulatePolicyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import SimulatePolicyResponseTypeDef
```




Optional fields:
- `EvaluationResults`: `List["EvaluationResultTypeDef"]`
- `IsTruncated`: `bool`
- `Marker`: `str`


## StatementTypeDef

```python
from mypy_boto3_iam.type_defs import StatementTypeDef
```




Optional fields:
- `SourcePolicyId`: `str`
- `SourcePolicyType`: `PolicySourceType`
- `StartPosition`: `"PositionTypeDef"`
- `EndPosition`: `"PositionTypeDef"`


## TagTypeDef

```python
from mypy_boto3_iam.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TrackedActionLastAccessedTypeDef

```python
from mypy_boto3_iam.type_defs import TrackedActionLastAccessedTypeDef
```




Optional fields:
- `ActionName`: `str`
- `LastAccessedEntity`: `str`
- `LastAccessedTime`: `datetime`
- `LastAccessedRegion`: `str`


## UpdateRoleDescriptionResponseTypeDef

```python
from mypy_boto3_iam.type_defs import UpdateRoleDescriptionResponseTypeDef
```




Optional fields:
- `Role`: `"RoleTypeDef"`


## UpdateSAMLProviderResponseTypeDef

```python
from mypy_boto3_iam.type_defs import UpdateSAMLProviderResponseTypeDef
```




Optional fields:
- `SAMLProviderArn`: `str`


## UploadSSHPublicKeyResponseTypeDef

```python
from mypy_boto3_iam.type_defs import UploadSSHPublicKeyResponseTypeDef
```




Optional fields:
- `SSHPublicKey`: `"SSHPublicKeyTypeDef"`


## UploadServerCertificateResponseTypeDef

```python
from mypy_boto3_iam.type_defs import UploadServerCertificateResponseTypeDef
```




Optional fields:
- `ServerCertificateMetadata`: `"ServerCertificateMetadataTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## UploadSigningCertificateResponseTypeDef

```python
from mypy_boto3_iam.type_defs import UploadSigningCertificateResponseTypeDef
```


Required fields:
- `Certificate`: `"SigningCertificateTypeDef"`




## UserDetailTypeDef

```python
from mypy_boto3_iam.type_defs import UserDetailTypeDef
```




Optional fields:
- `Path`: `str`
- `UserName`: `str`
- `UserId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`
- `UserPolicyList`: `List["PolicyDetailTypeDef"]`
- `GroupList`: `List[str]`
- `AttachedManagedPolicies`: `List["AttachedPolicyTypeDef"]`
- `PermissionsBoundary`: `"AttachedPermissionsBoundaryTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## UserTypeDef

```python
from mypy_boto3_iam.type_defs import UserTypeDef
```


Required fields:
- `Path`: `str`
- `UserName`: `str`
- `UserId`: `str`
- `Arn`: `str`
- `CreateDate`: `datetime`



Optional fields:
- `PasswordLastUsed`: `datetime`
- `PermissionsBoundary`: `"AttachedPermissionsBoundaryTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## VirtualMFADeviceTypeDef

```python
from mypy_boto3_iam.type_defs import VirtualMFADeviceTypeDef
```


Required fields:
- `SerialNumber`: `str`



Optional fields:
- `Base32StringSeed`: `Union[bytes, IO[bytes]]`
- `QRCodePNG`: `Union[bytes, IO[bytes]]`
- `User`: `"UserTypeDef"`
- `EnableDate`: `datetime`
- `Tags`: `List["TagTypeDef"]`


## WaiterConfigTypeDef

```python
from mypy_boto3_iam.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

