# Structures for boto3 Organizations module

> [Index](../index.md) > [Organizations](./index.md) > Structures

Auto-generated documentation for [Organizations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations)
type annotations stubs module [mypy_boto3_organizations](https://pypi.org/project/mypy-boto3-organizations/).

- [Structures for boto3 Organizations module](#structures-for-boto3-organizations-module)
  - [AccountTypeDef](#accounttypedef)
  - [ChildTypeDef](#childtypedef)
  - [CreateAccountStatusTypeDef](#createaccountstatustypedef)
  - [DelegatedAdministratorTypeDef](#delegatedadministratortypedef)
  - [DelegatedServiceTypeDef](#delegatedservicetypedef)
  - [EffectivePolicyTypeDef](#effectivepolicytypedef)
  - [EnabledServicePrincipalTypeDef](#enabledserviceprincipaltypedef)
  - [HandshakePartyTypeDef](#handshakepartytypedef)
  - [HandshakeTypeDef](#handshaketypedef)
  - [OrganizationTypeDef](#organizationtypedef)
  - [OrganizationalUnitTypeDef](#organizationalunittypedef)
  - [ParentTypeDef](#parenttypedef)
  - [PolicySummaryTypeDef](#policysummarytypedef)
  - [PolicyTargetSummaryTypeDef](#policytargetsummarytypedef)
  - [PolicyTypeDef](#policytypedef)
  - [PolicyTypeSummaryTypeDef](#policytypesummarytypedef)
  - [RootTypeDef](#roottypedef)
  - [TagTypeDef](#tagtypedef)
  - [AcceptHandshakeResponseTypeDef](#accepthandshakeresponsetypedef)
  - [CancelHandshakeResponseTypeDef](#cancelhandshakeresponsetypedef)
  - [CreateAccountResponseTypeDef](#createaccountresponsetypedef)
  - [CreateGovCloudAccountResponseTypeDef](#creategovcloudaccountresponsetypedef)
  - [CreateOrganizationResponseTypeDef](#createorganizationresponsetypedef)
  - [CreateOrganizationalUnitResponseTypeDef](#createorganizationalunitresponsetypedef)
  - [CreatePolicyResponseTypeDef](#createpolicyresponsetypedef)
  - [DeclineHandshakeResponseTypeDef](#declinehandshakeresponsetypedef)
  - [DescribeAccountResponseTypeDef](#describeaccountresponsetypedef)
  - [DescribeCreateAccountStatusResponseTypeDef](#describecreateaccountstatusresponsetypedef)
  - [DescribeEffectivePolicyResponseTypeDef](#describeeffectivepolicyresponsetypedef)
  - [DescribeHandshakeResponseTypeDef](#describehandshakeresponsetypedef)
  - [DescribeOrganizationResponseTypeDef](#describeorganizationresponsetypedef)
  - [DescribeOrganizationalUnitResponseTypeDef](#describeorganizationalunitresponsetypedef)
  - [DescribePolicyResponseTypeDef](#describepolicyresponsetypedef)
  - [HandshakeResourceTypeDef](#handshakeresourcetypedef)
  - [DisablePolicyTypeResponseTypeDef](#disablepolicytyperesponsetypedef)
  - [EnableAllFeaturesResponseTypeDef](#enableallfeaturesresponsetypedef)
  - [EnablePolicyTypeResponseTypeDef](#enablepolicytyperesponsetypedef)
  - [HandshakeFilterTypeDef](#handshakefiltertypedef)
  - [InviteAccountToOrganizationResponseTypeDef](#inviteaccounttoorganizationresponsetypedef)
  - [ListAWSServiceAccessForOrganizationResponseTypeDef](#listawsserviceaccessfororganizationresponsetypedef)
  - [ListAccountsForParentResponseTypeDef](#listaccountsforparentresponsetypedef)
  - [ListAccountsResponseTypeDef](#listaccountsresponsetypedef)
  - [ListChildrenResponseTypeDef](#listchildrenresponsetypedef)
  - [ListCreateAccountStatusResponseTypeDef](#listcreateaccountstatusresponsetypedef)
  - [ListDelegatedAdministratorsResponseTypeDef](#listdelegatedadministratorsresponsetypedef)
  - [ListDelegatedServicesForAccountResponseTypeDef](#listdelegatedservicesforaccountresponsetypedef)
  - [ListHandshakesForAccountResponseTypeDef](#listhandshakesforaccountresponsetypedef)
  - [ListHandshakesForOrganizationResponseTypeDef](#listhandshakesfororganizationresponsetypedef)
  - [ListOrganizationalUnitsForParentResponseTypeDef](#listorganizationalunitsforparentresponsetypedef)
  - [ListParentsResponseTypeDef](#listparentsresponsetypedef)
  - [ListPoliciesForTargetResponseTypeDef](#listpoliciesfortargetresponsetypedef)
  - [ListPoliciesResponseTypeDef](#listpoliciesresponsetypedef)
  - [ListRootsResponseTypeDef](#listrootsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTargetsForPolicyResponseTypeDef](#listtargetsforpolicyresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateOrganizationalUnitResponseTypeDef](#updateorganizationalunitresponsetypedef)
  - [UpdatePolicyResponseTypeDef](#updatepolicyresponsetypedef)

## AccountTypeDef

```python
from mypy_boto3_organizations.type_defs import AccountTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Email`: `str`
- `Name`: `str`
- `Status`: `AccountStatus`
- `JoinedMethod`: `AccountJoinedMethod`
- `JoinedTimestamp`: `datetime`


## ChildTypeDef

```python
from mypy_boto3_organizations.type_defs import ChildTypeDef
```




Optional fields:
- `Id`: `str`
- `Type`: `ChildType`


## CreateAccountStatusTypeDef

```python
from mypy_boto3_organizations.type_defs import CreateAccountStatusTypeDef
```




Optional fields:
- `Id`: `str`
- `AccountName`: `str`
- `State`: `CreateAccountState`
- `RequestedTimestamp`: `datetime`
- `CompletedTimestamp`: `datetime`
- `AccountId`: `str`
- `GovCloudAccountId`: `str`
- `FailureReason`: `CreateAccountFailureReason`


## DelegatedAdministratorTypeDef

```python
from mypy_boto3_organizations.type_defs import DelegatedAdministratorTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Email`: `str`
- `Name`: `str`
- `Status`: `AccountStatus`
- `JoinedMethod`: `AccountJoinedMethod`
- `JoinedTimestamp`: `datetime`
- `DelegationEnabledDate`: `datetime`


## DelegatedServiceTypeDef

```python
from mypy_boto3_organizations.type_defs import DelegatedServiceTypeDef
```




Optional fields:
- `ServicePrincipal`: `str`
- `DelegationEnabledDate`: `datetime`


## EffectivePolicyTypeDef

```python
from mypy_boto3_organizations.type_defs import EffectivePolicyTypeDef
```




Optional fields:
- `PolicyContent`: `str`
- `LastUpdatedTimestamp`: `datetime`
- `TargetId`: `str`
- `PolicyType`: `EffectivePolicyType`


## EnabledServicePrincipalTypeDef

```python
from mypy_boto3_organizations.type_defs import EnabledServicePrincipalTypeDef
```




Optional fields:
- `ServicePrincipal`: `str`
- `DateEnabled`: `datetime`


## HandshakePartyTypeDef

```python
from mypy_boto3_organizations.type_defs import HandshakePartyTypeDef
```


Required fields:
- `Id`: `str`
- `Type`: `HandshakePartyType`




## HandshakeTypeDef

```python
from mypy_boto3_organizations.type_defs import HandshakeTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Parties`: `List["HandshakePartyTypeDef"]`
- `State`: `HandshakeState`
- `RequestedTimestamp`: `datetime`
- `ExpirationTimestamp`: `datetime`
- `Action`: `ActionType`
- `Resources`: `List[Dict[str, Any]]`


## OrganizationTypeDef

```python
from mypy_boto3_organizations.type_defs import OrganizationTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `FeatureSet`: `OrganizationFeatureSet`
- `MasterAccountArn`: `str`
- `MasterAccountId`: `str`
- `MasterAccountEmail`: `str`
- `AvailablePolicyTypes`: `List["PolicyTypeSummaryTypeDef"]`


## OrganizationalUnitTypeDef

```python
from mypy_boto3_organizations.type_defs import OrganizationalUnitTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## ParentTypeDef

```python
from mypy_boto3_organizations.type_defs import ParentTypeDef
```




Optional fields:
- `Id`: `str`
- `Type`: `ParentType`


## PolicySummaryTypeDef

```python
from mypy_boto3_organizations.type_defs import PolicySummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Description`: `str`
- `Type`: `PolicyType`
- `AwsManaged`: `bool`


## PolicyTargetSummaryTypeDef

```python
from mypy_boto3_organizations.type_defs import PolicyTargetSummaryTypeDef
```




Optional fields:
- `TargetId`: `str`
- `Arn`: `str`
- `Name`: `str`
- `Type`: `TargetType`


## PolicyTypeDef

```python
from mypy_boto3_organizations.type_defs import PolicyTypeDef
```




Optional fields:
- `PolicySummary`: `"PolicySummaryTypeDef"`
- `Content`: `str`


## PolicyTypeSummaryTypeDef

```python
from mypy_boto3_organizations.type_defs import PolicyTypeSummaryTypeDef
```




Optional fields:
- `Type`: `PolicyType`
- `Status`: `PolicyTypeStatus`


## RootTypeDef

```python
from mypy_boto3_organizations.type_defs import RootTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `PolicyTypes`: `List["PolicyTypeSummaryTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_organizations.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## AcceptHandshakeResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import AcceptHandshakeResponseTypeDef
```




Optional fields:
- `Handshake`: `"HandshakeTypeDef"`


## CancelHandshakeResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import CancelHandshakeResponseTypeDef
```




Optional fields:
- `Handshake`: `"HandshakeTypeDef"`


## CreateAccountResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import CreateAccountResponseTypeDef
```




Optional fields:
- `CreateAccountStatus`: `"CreateAccountStatusTypeDef"`


## CreateGovCloudAccountResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import CreateGovCloudAccountResponseTypeDef
```




Optional fields:
- `CreateAccountStatus`: `"CreateAccountStatusTypeDef"`


## CreateOrganizationResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import CreateOrganizationResponseTypeDef
```




Optional fields:
- `Organization`: `"OrganizationTypeDef"`


## CreateOrganizationalUnitResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import CreateOrganizationalUnitResponseTypeDef
```




Optional fields:
- `OrganizationalUnit`: `"OrganizationalUnitTypeDef"`


## CreatePolicyResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import CreatePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`


## DeclineHandshakeResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DeclineHandshakeResponseTypeDef
```




Optional fields:
- `Handshake`: `"HandshakeTypeDef"`


## DescribeAccountResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribeAccountResponseTypeDef
```




Optional fields:
- `Account`: `"AccountTypeDef"`


## DescribeCreateAccountStatusResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribeCreateAccountStatusResponseTypeDef
```




Optional fields:
- `CreateAccountStatus`: `"CreateAccountStatusTypeDef"`


## DescribeEffectivePolicyResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribeEffectivePolicyResponseTypeDef
```




Optional fields:
- `EffectivePolicy`: `"EffectivePolicyTypeDef"`


## DescribeHandshakeResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribeHandshakeResponseTypeDef
```




Optional fields:
- `Handshake`: `"HandshakeTypeDef"`


## DescribeOrganizationResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribeOrganizationResponseTypeDef
```




Optional fields:
- `Organization`: `"OrganizationTypeDef"`


## DescribeOrganizationalUnitResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribeOrganizationalUnitResponseTypeDef
```




Optional fields:
- `OrganizationalUnit`: `"OrganizationalUnitTypeDef"`


## DescribePolicyResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DescribePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`


## HandshakeResourceTypeDef

```python
from mypy_boto3_organizations.type_defs import HandshakeResourceTypeDef
```




Optional fields:
- `Value`: `str`
- `Type`: `HandshakeResourceType`
- `Resources`: `List[Dict[str, Any]]`


## DisablePolicyTypeResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import DisablePolicyTypeResponseTypeDef
```




Optional fields:
- `Root`: `"RootTypeDef"`


## EnableAllFeaturesResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import EnableAllFeaturesResponseTypeDef
```




Optional fields:
- `Handshake`: `"HandshakeTypeDef"`


## EnablePolicyTypeResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import EnablePolicyTypeResponseTypeDef
```




Optional fields:
- `Root`: `"RootTypeDef"`


## HandshakeFilterTypeDef

```python
from mypy_boto3_organizations.type_defs import HandshakeFilterTypeDef
```




Optional fields:
- `ActionType`: `ActionType`
- `ParentHandshakeId`: `str`


## InviteAccountToOrganizationResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import InviteAccountToOrganizationResponseTypeDef
```




Optional fields:
- `Handshake`: `"HandshakeTypeDef"`


## ListAWSServiceAccessForOrganizationResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListAWSServiceAccessForOrganizationResponseTypeDef
```




Optional fields:
- `EnabledServicePrincipals`: `List["EnabledServicePrincipalTypeDef"]`
- `NextToken`: `str`


## ListAccountsForParentResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListAccountsForParentResponseTypeDef
```




Optional fields:
- `Accounts`: `List["AccountTypeDef"]`
- `NextToken`: `str`


## ListAccountsResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListAccountsResponseTypeDef
```




Optional fields:
- `Accounts`: `List["AccountTypeDef"]`
- `NextToken`: `str`


## ListChildrenResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListChildrenResponseTypeDef
```




Optional fields:
- `Children`: `List["ChildTypeDef"]`
- `NextToken`: `str`


## ListCreateAccountStatusResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListCreateAccountStatusResponseTypeDef
```




Optional fields:
- `CreateAccountStatuses`: `List["CreateAccountStatusTypeDef"]`
- `NextToken`: `str`


## ListDelegatedAdministratorsResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListDelegatedAdministratorsResponseTypeDef
```




Optional fields:
- `DelegatedAdministrators`: `List["DelegatedAdministratorTypeDef"]`
- `NextToken`: `str`


## ListDelegatedServicesForAccountResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListDelegatedServicesForAccountResponseTypeDef
```




Optional fields:
- `DelegatedServices`: `List["DelegatedServiceTypeDef"]`
- `NextToken`: `str`


## ListHandshakesForAccountResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListHandshakesForAccountResponseTypeDef
```




Optional fields:
- `Handshakes`: `List["HandshakeTypeDef"]`
- `NextToken`: `str`


## ListHandshakesForOrganizationResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListHandshakesForOrganizationResponseTypeDef
```




Optional fields:
- `Handshakes`: `List["HandshakeTypeDef"]`
- `NextToken`: `str`


## ListOrganizationalUnitsForParentResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListOrganizationalUnitsForParentResponseTypeDef
```




Optional fields:
- `OrganizationalUnits`: `List["OrganizationalUnitTypeDef"]`
- `NextToken`: `str`


## ListParentsResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListParentsResponseTypeDef
```




Optional fields:
- `Parents`: `List["ParentTypeDef"]`
- `NextToken`: `str`


## ListPoliciesForTargetResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListPoliciesForTargetResponseTypeDef
```




Optional fields:
- `Policies`: `List["PolicySummaryTypeDef"]`
- `NextToken`: `str`


## ListPoliciesResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListPoliciesResponseTypeDef
```




Optional fields:
- `Policies`: `List["PolicySummaryTypeDef"]`
- `NextToken`: `str`


## ListRootsResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListRootsResponseTypeDef
```




Optional fields:
- `Roots`: `List["RootTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## ListTargetsForPolicyResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import ListTargetsForPolicyResponseTypeDef
```




Optional fields:
- `Targets`: `List["PolicyTargetSummaryTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_organizations.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateOrganizationalUnitResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import UpdateOrganizationalUnitResponseTypeDef
```




Optional fields:
- `OrganizationalUnit`: `"OrganizationalUnitTypeDef"`


## UpdatePolicyResponseTypeDef

```python
from mypy_boto3_organizations.type_defs import UpdatePolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`

