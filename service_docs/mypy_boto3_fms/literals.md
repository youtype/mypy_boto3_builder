# Literals for boto3 FMS module

> [Index](../index.md) > [FMS](./index.md) > Literals

Auto-generated documentation for [FMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS)
type annotations stubs module [mypy_boto3_fms](https://pypi.org/project/mypy-boto3-fms/).

- [Literals for boto3 FMS module](#literals-for-boto3-fms-module)
  - [AccountRoleStatus](#accountrolestatus)
  - [CustomerPolicyScopeIdType](#customerpolicyscopeidtype)
  - [DependentServiceName](#dependentservicename)
  - [ListComplianceStatusPaginatorName](#listcompliancestatuspaginatorname)
  - [ListMemberAccountsPaginatorName](#listmemberaccountspaginatorname)
  - [ListPoliciesPaginatorName](#listpoliciespaginatorname)
  - [PolicyComplianceStatusType](#policycompliancestatustype)
  - [RemediationActionType](#remediationactiontype)
  - [SecurityServiceType](#securityservicetype)
  - [ViolationReason](#violationreason)

## AccountRoleStatus

```python
from mypy_boto3_fms.literals import AccountRoleStatus
```

Values:

- `CREATING`
- `DELETED`
- `DELETING`
- `PENDING_DELETION`
- `READY`

## CustomerPolicyScopeIdType

```python
from mypy_boto3_fms.literals import CustomerPolicyScopeIdType
```

Values:

- `ACCOUNT`
- `ORG_UNIT`

## DependentServiceName

```python
from mypy_boto3_fms.literals import DependentServiceName
```

Values:

- `AWSCONFIG`
- `AWSSHIELD_ADVANCED`
- `AWSVPC`
- `AWSWAF`

## ListComplianceStatusPaginatorName

```python
from mypy_boto3_fms.literals import ListComplianceStatusPaginatorName
```

Values:

- `list_compliance_status`

## ListMemberAccountsPaginatorName

```python
from mypy_boto3_fms.literals import ListMemberAccountsPaginatorName
```

Values:

- `list_member_accounts`

## ListPoliciesPaginatorName

```python
from mypy_boto3_fms.literals import ListPoliciesPaginatorName
```

Values:

- `list_policies`

## PolicyComplianceStatusType

```python
from mypy_boto3_fms.literals import PolicyComplianceStatusType
```

Values:

- `COMPLIANT`
- `NON_COMPLIANT`

## RemediationActionType

```python
from mypy_boto3_fms.literals import RemediationActionType
```

Values:

- `MODIFY`
- `REMOVE`

## SecurityServiceType

```python
from mypy_boto3_fms.literals import SecurityServiceType
```

Values:

- `DNS_FIREWALL`
- `NETWORK_FIREWALL`
- `SECURITY_GROUPS_COMMON`
- `SECURITY_GROUPS_CONTENT_AUDIT`
- `SECURITY_GROUPS_USAGE_AUDIT`
- `SHIELD_ADVANCED`
- `WAF`
- `WAFV2`

## ViolationReason

```python
from mypy_boto3_fms.literals import ViolationReason
```

Values:

- `FMS_CREATED_SECURITY_GROUP_EDITED`
- `MISSING_EXPECTED_ROUTE_TABLE`
- `MISSING_FIREWALL`
- `MISSING_FIREWALL_SUBNET_IN_AZ`
- `NETWORK_FIREWALL_POLICY_MODIFIED`
- `RESOURCE_INCORRECT_WEB_ACL`
- `RESOURCE_MISSING_DNS_FIREWALL`
- `RESOURCE_MISSING_SECURITY_GROUP`
- `RESOURCE_MISSING_SHIELD_PROTECTION`
- `RESOURCE_MISSING_WEB_ACL`
- `RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION`
- `RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP`
- `SECURITY_GROUP_REDUNDANT`
- `SECURITY_GROUP_UNUSED`
- `WEB_ACL_MISSING_RULE_GROUP`
