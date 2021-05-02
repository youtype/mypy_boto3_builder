# Literals for boto3 Organizations module

> [Index](../index.md) > [Organizations](./index.md) > Literals

Auto-generated documentation for [Organizations](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations)
type annotations stubs module [mypy_boto3_organizations](https://pypi.org/project/mypy-boto3-organizations/).

- [Literals for boto3 Organizations module](#literals-for-boto3-organizations-module)
  - [AccountJoinedMethod](#accountjoinedmethod)
  - [AccountStatus](#accountstatus)
  - [ActionType](#actiontype)
  - [ChildType](#childtype)
  - [CreateAccountFailureReason](#createaccountfailurereason)
  - [CreateAccountState](#createaccountstate)
  - [EffectivePolicyType](#effectivepolicytype)
  - [HandshakePartyType](#handshakepartytype)
  - [HandshakeState](#handshakestate)
  - [IAMUserAccessToBilling](#iamuseraccesstobilling)
  - [ListAWSServiceAccessForOrganizationPaginatorName](#listawsserviceaccessfororganizationpaginatorname)
  - [ListAccountsForParentPaginatorName](#listaccountsforparentpaginatorname)
  - [ListAccountsPaginatorName](#listaccountspaginatorname)
  - [ListChildrenPaginatorName](#listchildrenpaginatorname)
  - [ListCreateAccountStatusPaginatorName](#listcreateaccountstatuspaginatorname)
  - [ListDelegatedAdministratorsPaginatorName](#listdelegatedadministratorspaginatorname)
  - [ListDelegatedServicesForAccountPaginatorName](#listdelegatedservicesforaccountpaginatorname)
  - [ListHandshakesForAccountPaginatorName](#listhandshakesforaccountpaginatorname)
  - [ListHandshakesForOrganizationPaginatorName](#listhandshakesfororganizationpaginatorname)
  - [ListOrganizationalUnitsForParentPaginatorName](#listorganizationalunitsforparentpaginatorname)
  - [ListParentsPaginatorName](#listparentspaginatorname)
  - [ListPoliciesForTargetPaginatorName](#listpoliciesfortargetpaginatorname)
  - [ListPoliciesPaginatorName](#listpoliciespaginatorname)
  - [ListRootsPaginatorName](#listrootspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListTargetsForPolicyPaginatorName](#listtargetsforpolicypaginatorname)
  - [OrganizationFeatureSet](#organizationfeatureset)
  - [ParentType](#parenttype)
  - [PolicyType](#policytype)
  - [PolicyTypeStatus](#policytypestatus)
  - [TargetType](#targettype)

## AccountJoinedMethod

```python
from mypy_boto3_organizations.literals import AccountJoinedMethod
```

Values:

- `CREATED`
- `INVITED`

## AccountStatus

```python
from mypy_boto3_organizations.literals import AccountStatus
```

Values:

- `ACTIVE`
- `SUSPENDED`

## ActionType

```python
from mypy_boto3_organizations.literals import ActionType
```

Values:

- `ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE`
- `APPROVE_ALL_FEATURES`
- `ENABLE_ALL_FEATURES`
- `INVITE`

## ChildType

```python
from mypy_boto3_organizations.literals import ChildType
```

Values:

- `ACCOUNT`
- `ORGANIZATIONAL_UNIT`

## CreateAccountFailureReason

```python
from mypy_boto3_organizations.literals import CreateAccountFailureReason
```

Values:

- `ACCOUNT_LIMIT_EXCEEDED`
- `CONCURRENT_ACCOUNT_MODIFICATION`
- `EMAIL_ALREADY_EXISTS`
- `FAILED_BUSINESS_VALIDATION`
- `GOVCLOUD_ACCOUNT_ALREADY_EXISTS`
- `INTERNAL_FAILURE`
- `INVALID_ADDRESS`
- `INVALID_EMAIL`
- `INVALID_IDENTITY_FOR_BUSINESS_VALIDATION`
- `MISSING_BUSINESS_VALIDATION`
- `MISSING_PAYMENT_INSTRUMENT`
- `PENDING_BUSINESS_VALIDATION`
- `UNKNOWN_BUSINESS_VALIDATION`

## CreateAccountState

```python
from mypy_boto3_organizations.literals import CreateAccountState
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`

## EffectivePolicyType

```python
from mypy_boto3_organizations.literals import EffectivePolicyType
```

Values:

- `AISERVICES_OPT_OUT_POLICY`
- `BACKUP_POLICY`
- `TAG_POLICY`

## HandshakePartyType

```python
from mypy_boto3_organizations.literals import HandshakePartyType
```

Values:

- `ACCOUNT`
- `EMAIL`
- `ORGANIZATION`

## HandshakeState

```python
from mypy_boto3_organizations.literals import HandshakeState
```

Values:

- `ACCEPTED`
- `CANCELED`
- `DECLINED`
- `EXPIRED`
- `OPEN`
- `REQUESTED`

## IAMUserAccessToBilling

```python
from mypy_boto3_organizations.literals import IAMUserAccessToBilling
```

Values:

- `ALLOW`
- `DENY`

## ListAWSServiceAccessForOrganizationPaginatorName

```python
from mypy_boto3_organizations.literals import ListAWSServiceAccessForOrganizationPaginatorName
```

Values:

- `list_aws_service_access_for_organization`

## ListAccountsForParentPaginatorName

```python
from mypy_boto3_organizations.literals import ListAccountsForParentPaginatorName
```

Values:

- `list_accounts_for_parent`

## ListAccountsPaginatorName

```python
from mypy_boto3_organizations.literals import ListAccountsPaginatorName
```

Values:

- `list_accounts`

## ListChildrenPaginatorName

```python
from mypy_boto3_organizations.literals import ListChildrenPaginatorName
```

Values:

- `list_children`

## ListCreateAccountStatusPaginatorName

```python
from mypy_boto3_organizations.literals import ListCreateAccountStatusPaginatorName
```

Values:

- `list_create_account_status`

## ListDelegatedAdministratorsPaginatorName

```python
from mypy_boto3_organizations.literals import ListDelegatedAdministratorsPaginatorName
```

Values:

- `list_delegated_administrators`

## ListDelegatedServicesForAccountPaginatorName

```python
from mypy_boto3_organizations.literals import ListDelegatedServicesForAccountPaginatorName
```

Values:

- `list_delegated_services_for_account`

## ListHandshakesForAccountPaginatorName

```python
from mypy_boto3_organizations.literals import ListHandshakesForAccountPaginatorName
```

Values:

- `list_handshakes_for_account`

## ListHandshakesForOrganizationPaginatorName

```python
from mypy_boto3_organizations.literals import ListHandshakesForOrganizationPaginatorName
```

Values:

- `list_handshakes_for_organization`

## ListOrganizationalUnitsForParentPaginatorName

```python
from mypy_boto3_organizations.literals import ListOrganizationalUnitsForParentPaginatorName
```

Values:

- `list_organizational_units_for_parent`

## ListParentsPaginatorName

```python
from mypy_boto3_organizations.literals import ListParentsPaginatorName
```

Values:

- `list_parents`

## ListPoliciesForTargetPaginatorName

```python
from mypy_boto3_organizations.literals import ListPoliciesForTargetPaginatorName
```

Values:

- `list_policies_for_target`

## ListPoliciesPaginatorName

```python
from mypy_boto3_organizations.literals import ListPoliciesPaginatorName
```

Values:

- `list_policies`

## ListRootsPaginatorName

```python
from mypy_boto3_organizations.literals import ListRootsPaginatorName
```

Values:

- `list_roots`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_organizations.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListTargetsForPolicyPaginatorName

```python
from mypy_boto3_organizations.literals import ListTargetsForPolicyPaginatorName
```

Values:

- `list_targets_for_policy`

## OrganizationFeatureSet

```python
from mypy_boto3_organizations.literals import OrganizationFeatureSet
```

Values:

- `ALL`
- `CONSOLIDATED_BILLING`

## ParentType

```python
from mypy_boto3_organizations.literals import ParentType
```

Values:

- `ORGANIZATIONAL_UNIT`
- `ROOT`

## PolicyType

```python
from mypy_boto3_organizations.literals import PolicyType
```

Values:

- `AISERVICES_OPT_OUT_POLICY`
- `BACKUP_POLICY`
- `SERVICE_CONTROL_POLICY`
- `TAG_POLICY`

## PolicyTypeStatus

```python
from mypy_boto3_organizations.literals import PolicyTypeStatus
```

Values:

- `ENABLED`
- `PENDING_DISABLE`
- `PENDING_ENABLE`

## TargetType

```python
from mypy_boto3_organizations.literals import TargetType
```

Values:

- `ACCOUNT`
- `ORGANIZATIONAL_UNIT`
- `ROOT`
