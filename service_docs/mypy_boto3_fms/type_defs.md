# Structures for boto3 FMS module

> [Index](../index.md) > [FMS](./index.md) > Structures

Auto-generated documentation for [FMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS)
type annotations stubs module [mypy_boto3_fms](https://pypi.org/project/mypy-boto3-fms/).

- [Structures for boto3 FMS module](#structures-for-boto3-fms-module)
  - [AppTypeDef](#apptypedef)
  - [AppsListDataSummaryTypeDef](#appslistdatasummarytypedef)
  - [AppsListDataTypeDef](#appslistdatatypedef)
  - [AwsEc2InstanceViolationTypeDef](#awsec2instanceviolationtypedef)
  - [AwsEc2NetworkInterfaceViolationTypeDef](#awsec2networkinterfaceviolationtypedef)
  - [AwsVPCSecurityGroupViolationTypeDef](#awsvpcsecuritygroupviolationtypedef)
  - [ComplianceViolatorTypeDef](#complianceviolatortypedef)
  - [DnsDuplicateRuleGroupViolationTypeDef](#dnsduplicaterulegroupviolationtypedef)
  - [DnsRuleGroupLimitExceededViolationTypeDef](#dnsrulegrouplimitexceededviolationtypedef)
  - [DnsRuleGroupPriorityConflictViolationTypeDef](#dnsrulegrouppriorityconflictviolationtypedef)
  - [EvaluationResultTypeDef](#evaluationresulttypedef)
  - [NetworkFirewallMissingExpectedRTViolationTypeDef](#networkfirewallmissingexpectedrtviolationtypedef)
  - [NetworkFirewallMissingFirewallViolationTypeDef](#networkfirewallmissingfirewallviolationtypedef)
  - [NetworkFirewallMissingSubnetViolationTypeDef](#networkfirewallmissingsubnetviolationtypedef)
  - [NetworkFirewallPolicyDescriptionTypeDef](#networkfirewallpolicydescriptiontypedef)
  - [NetworkFirewallPolicyModifiedViolationTypeDef](#networkfirewallpolicymodifiedviolationtypedef)
  - [PartialMatchTypeDef](#partialmatchtypedef)
  - [PolicyComplianceDetailTypeDef](#policycompliancedetailtypedef)
  - [PolicyComplianceStatusTypeDef](#policycompliancestatustypedef)
  - [PolicySummaryTypeDef](#policysummarytypedef)
  - [PolicyTypeDef](#policytypedef)
  - [ProtocolsListDataSummaryTypeDef](#protocolslistdatasummarytypedef)
  - [ProtocolsListDataTypeDef](#protocolslistdatatypedef)
  - [ResourceTagTypeDef](#resourcetagtypedef)
  - [ResourceViolationTypeDef](#resourceviolationtypedef)
  - [SecurityGroupRemediationActionTypeDef](#securitygroupremediationactiontypedef)
  - [SecurityGroupRuleDescriptionTypeDef](#securitygroupruledescriptiontypedef)
  - [SecurityServicePolicyDataTypeDef](#securityservicepolicydatatypedef)
  - [StatefulRuleGroupTypeDef](#statefulrulegrouptypedef)
  - [StatelessRuleGroupTypeDef](#statelessrulegrouptypedef)
  - [TagTypeDef](#tagtypedef)
  - [ViolationDetailTypeDef](#violationdetailtypedef)
  - [GetAdminAccountResponseTypeDef](#getadminaccountresponsetypedef)
  - [GetAppsListResponseTypeDef](#getappslistresponsetypedef)
  - [GetComplianceDetailResponseTypeDef](#getcompliancedetailresponsetypedef)
  - [GetNotificationChannelResponseTypeDef](#getnotificationchannelresponsetypedef)
  - [GetPolicyResponseTypeDef](#getpolicyresponsetypedef)
  - [GetProtectionStatusResponseTypeDef](#getprotectionstatusresponsetypedef)
  - [GetProtocolsListResponseTypeDef](#getprotocolslistresponsetypedef)
  - [GetViolationDetailsResponseTypeDef](#getviolationdetailsresponsetypedef)
  - [ListAppsListsResponseTypeDef](#listappslistsresponsetypedef)
  - [ListComplianceStatusResponseTypeDef](#listcompliancestatusresponsetypedef)
  - [ListMemberAccountsResponseTypeDef](#listmemberaccountsresponsetypedef)
  - [ListPoliciesResponseTypeDef](#listpoliciesresponsetypedef)
  - [ListProtocolsListsResponseTypeDef](#listprotocolslistsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutAppsListResponseTypeDef](#putappslistresponsetypedef)
  - [PutPolicyResponseTypeDef](#putpolicyresponsetypedef)
  - [PutProtocolsListResponseTypeDef](#putprotocolslistresponsetypedef)

## AppTypeDef

```python
from mypy_boto3_fms.type_defs import AppTypeDef
```


Required fields:
- `AppName`: `str`
- `Protocol`: `str`
- `Port`: `int`




## AppsListDataSummaryTypeDef

```python
from mypy_boto3_fms.type_defs import AppsListDataSummaryTypeDef
```




Optional fields:
- `ListArn`: `str`
- `ListId`: `str`
- `ListName`: `str`
- `AppsList`: `List["AppTypeDef"]`


## AppsListDataTypeDef

```python
from mypy_boto3_fms.type_defs import AppsListDataTypeDef
```


Required fields:
- `ListName`: `str`
- `AppsList`: `List["AppTypeDef"]`



Optional fields:
- `ListId`: `str`
- `ListUpdateToken`: `str`
- `CreateTime`: `datetime`
- `LastUpdateTime`: `datetime`
- `PreviousAppsList`: `Dict[str, List["AppTypeDef"]]`


## AwsEc2InstanceViolationTypeDef

```python
from mypy_boto3_fms.type_defs import AwsEc2InstanceViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `AwsEc2NetworkInterfaceViolations`: `List["AwsEc2NetworkInterfaceViolationTypeDef"]`


## AwsEc2NetworkInterfaceViolationTypeDef

```python
from mypy_boto3_fms.type_defs import AwsEc2NetworkInterfaceViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `ViolatingSecurityGroups`: `List[str]`


## AwsVPCSecurityGroupViolationTypeDef

```python
from mypy_boto3_fms.type_defs import AwsVPCSecurityGroupViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `ViolationTargetDescription`: `str`
- `PartialMatches`: `List["PartialMatchTypeDef"]`
- `PossibleSecurityGroupRemediationActions`: `List["SecurityGroupRemediationActionTypeDef"]`


## ComplianceViolatorTypeDef

```python
from mypy_boto3_fms.type_defs import ComplianceViolatorTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ViolationReason`: `ViolationReason`
- `ResourceType`: `str`


## DnsDuplicateRuleGroupViolationTypeDef

```python
from mypy_boto3_fms.type_defs import DnsDuplicateRuleGroupViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `ViolationTargetDescription`: `str`


## DnsRuleGroupLimitExceededViolationTypeDef

```python
from mypy_boto3_fms.type_defs import DnsRuleGroupLimitExceededViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `ViolationTargetDescription`: `str`
- `NumberOfRuleGroupsAlreadyAssociated`: `int`


## DnsRuleGroupPriorityConflictViolationTypeDef

```python
from mypy_boto3_fms.type_defs import DnsRuleGroupPriorityConflictViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `ViolationTargetDescription`: `str`
- `ConflictingPriority`: `int`
- `ConflictingPolicyId`: `str`
- `UnavailablePriorities`: `List[int]`


## EvaluationResultTypeDef

```python
from mypy_boto3_fms.type_defs import EvaluationResultTypeDef
```




Optional fields:
- `ComplianceStatus`: `PolicyComplianceStatusType`
- `ViolatorCount`: `int`
- `EvaluationLimitExceeded`: `bool`


## NetworkFirewallMissingExpectedRTViolationTypeDef

```python
from mypy_boto3_fms.type_defs import NetworkFirewallMissingExpectedRTViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `VPC`: `str`
- `AvailabilityZone`: `str`
- `CurrentRouteTable`: `str`
- `ExpectedRouteTable`: `str`


## NetworkFirewallMissingFirewallViolationTypeDef

```python
from mypy_boto3_fms.type_defs import NetworkFirewallMissingFirewallViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `VPC`: `str`
- `AvailabilityZone`: `str`
- `TargetViolationReason`: `str`


## NetworkFirewallMissingSubnetViolationTypeDef

```python
from mypy_boto3_fms.type_defs import NetworkFirewallMissingSubnetViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `VPC`: `str`
- `AvailabilityZone`: `str`
- `TargetViolationReason`: `str`


## NetworkFirewallPolicyDescriptionTypeDef

```python
from mypy_boto3_fms.type_defs import NetworkFirewallPolicyDescriptionTypeDef
```




Optional fields:
- `StatelessRuleGroups`: `List["StatelessRuleGroupTypeDef"]`
- `StatelessDefaultActions`: `List[str]`
- `StatelessFragmentDefaultActions`: `List[str]`
- `StatelessCustomActions`: `List[str]`
- `StatefulRuleGroups`: `List["StatefulRuleGroupTypeDef"]`


## NetworkFirewallPolicyModifiedViolationTypeDef

```python
from mypy_boto3_fms.type_defs import NetworkFirewallPolicyModifiedViolationTypeDef
```




Optional fields:
- `ViolationTarget`: `str`
- `CurrentPolicyDescription`: `"NetworkFirewallPolicyDescriptionTypeDef"`
- `ExpectedPolicyDescription`: `"NetworkFirewallPolicyDescriptionTypeDef"`


## PartialMatchTypeDef

```python
from mypy_boto3_fms.type_defs import PartialMatchTypeDef
```




Optional fields:
- `Reference`: `str`
- `TargetViolationReasons`: `List[str]`


## PolicyComplianceDetailTypeDef

```python
from mypy_boto3_fms.type_defs import PolicyComplianceDetailTypeDef
```




Optional fields:
- `PolicyOwner`: `str`
- `PolicyId`: `str`
- `MemberAccount`: `str`
- `Violators`: `List["ComplianceViolatorTypeDef"]`
- `EvaluationLimitExceeded`: `bool`
- `ExpiredAt`: `datetime`
- `IssueInfoMap`: `Dict[DependentServiceName, str]`


## PolicyComplianceStatusTypeDef

```python
from mypy_boto3_fms.type_defs import PolicyComplianceStatusTypeDef
```




Optional fields:
- `PolicyOwner`: `str`
- `PolicyId`: `str`
- `PolicyName`: `str`
- `MemberAccount`: `str`
- `EvaluationResults`: `List["EvaluationResultTypeDef"]`
- `LastUpdated`: `datetime`
- `IssueInfoMap`: `Dict[DependentServiceName, str]`


## PolicySummaryTypeDef

```python
from mypy_boto3_fms.type_defs import PolicySummaryTypeDef
```




Optional fields:
- `PolicyArn`: `str`
- `PolicyId`: `str`
- `PolicyName`: `str`
- `ResourceType`: `str`
- `SecurityServiceType`: `SecurityServiceType`
- `RemediationEnabled`: `bool`


## PolicyTypeDef

```python
from mypy_boto3_fms.type_defs import PolicyTypeDef
```


Required fields:
- `PolicyName`: `str`
- `SecurityServicePolicyData`: `"SecurityServicePolicyDataTypeDef"`
- `ResourceType`: `str`
- `ExcludeResourceTags`: `bool`
- `RemediationEnabled`: `bool`



Optional fields:
- `PolicyId`: `str`
- `PolicyUpdateToken`: `str`
- `ResourceTypeList`: `List[str]`
- `ResourceTags`: `List["ResourceTagTypeDef"]`
- `IncludeMap`: `Dict[CustomerPolicyScopeIdType, List[str]]`
- `ExcludeMap`: `Dict[CustomerPolicyScopeIdType, List[str]]`


## ProtocolsListDataSummaryTypeDef

```python
from mypy_boto3_fms.type_defs import ProtocolsListDataSummaryTypeDef
```




Optional fields:
- `ListArn`: `str`
- `ListId`: `str`
- `ListName`: `str`
- `ProtocolsList`: `List[str]`


## ProtocolsListDataTypeDef

```python
from mypy_boto3_fms.type_defs import ProtocolsListDataTypeDef
```


Required fields:
- `ListName`: `str`
- `ProtocolsList`: `List[str]`



Optional fields:
- `ListId`: `str`
- `ListUpdateToken`: `str`
- `CreateTime`: `datetime`
- `LastUpdateTime`: `datetime`
- `PreviousProtocolsList`: `Dict[str, List[str]]`


## ResourceTagTypeDef

```python
from mypy_boto3_fms.type_defs import ResourceTagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## ResourceViolationTypeDef

```python
from mypy_boto3_fms.type_defs import ResourceViolationTypeDef
```




Optional fields:
- `AwsVPCSecurityGroupViolation`: `"AwsVPCSecurityGroupViolationTypeDef"`
- `AwsEc2NetworkInterfaceViolation`: `"AwsEc2NetworkInterfaceViolationTypeDef"`
- `AwsEc2InstanceViolation`: `"AwsEc2InstanceViolationTypeDef"`
- `NetworkFirewallMissingFirewallViolation`: `"NetworkFirewallMissingFirewallViolationTypeDef"`
- `NetworkFirewallMissingSubnetViolation`: `"NetworkFirewallMissingSubnetViolationTypeDef"`
- `NetworkFirewallMissingExpectedRTViolation`: `"NetworkFirewallMissingExpectedRTViolationTypeDef"`
- `NetworkFirewallPolicyModifiedViolation`: `"NetworkFirewallPolicyModifiedViolationTypeDef"`
- `DnsRuleGroupPriorityConflictViolation`: `"DnsRuleGroupPriorityConflictViolationTypeDef"`
- `DnsDuplicateRuleGroupViolation`: `"DnsDuplicateRuleGroupViolationTypeDef"`
- `DnsRuleGroupLimitExceededViolation`: `"DnsRuleGroupLimitExceededViolationTypeDef"`


## SecurityGroupRemediationActionTypeDef

```python
from mypy_boto3_fms.type_defs import SecurityGroupRemediationActionTypeDef
```




Optional fields:
- `RemediationActionType`: `RemediationActionType`
- `Description`: `str`
- `RemediationResult`: `"SecurityGroupRuleDescriptionTypeDef"`
- `IsDefaultAction`: `bool`


## SecurityGroupRuleDescriptionTypeDef

```python
from mypy_boto3_fms.type_defs import SecurityGroupRuleDescriptionTypeDef
```




Optional fields:
- `IPV4Range`: `str`
- `IPV6Range`: `str`
- `PrefixListId`: `str`
- `Protocol`: `str`
- `FromPort`: `int`
- `ToPort`: `int`


## SecurityServicePolicyDataTypeDef

```python
from mypy_boto3_fms.type_defs import SecurityServicePolicyDataTypeDef
```


Required fields:
- `Type`: `SecurityServiceType`



Optional fields:
- `ManagedServiceData`: `str`


## StatefulRuleGroupTypeDef

```python
from mypy_boto3_fms.type_defs import StatefulRuleGroupTypeDef
```




Optional fields:
- `RuleGroupName`: `str`
- `ResourceId`: `str`


## StatelessRuleGroupTypeDef

```python
from mypy_boto3_fms.type_defs import StatelessRuleGroupTypeDef
```




Optional fields:
- `RuleGroupName`: `str`
- `ResourceId`: `str`
- `Priority`: `int`


## TagTypeDef

```python
from mypy_boto3_fms.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## ViolationDetailTypeDef

```python
from mypy_boto3_fms.type_defs import ViolationDetailTypeDef
```


Required fields:
- `PolicyId`: `str`
- `MemberAccount`: `str`
- `ResourceId`: `str`
- `ResourceType`: `str`
- `ResourceViolations`: `List["ResourceViolationTypeDef"]`



Optional fields:
- `ResourceTags`: `List["TagTypeDef"]`
- `ResourceDescription`: `str`


## GetAdminAccountResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetAdminAccountResponseTypeDef
```




Optional fields:
- `AdminAccount`: `str`
- `RoleStatus`: `AccountRoleStatus`


## GetAppsListResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetAppsListResponseTypeDef
```




Optional fields:
- `AppsList`: `"AppsListDataTypeDef"`
- `AppsListArn`: `str`


## GetComplianceDetailResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetComplianceDetailResponseTypeDef
```




Optional fields:
- `PolicyComplianceDetail`: `"PolicyComplianceDetailTypeDef"`


## GetNotificationChannelResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetNotificationChannelResponseTypeDef
```




Optional fields:
- `SnsTopicArn`: `str`
- `SnsRoleName`: `str`


## GetPolicyResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`
- `PolicyArn`: `str`


## GetProtectionStatusResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetProtectionStatusResponseTypeDef
```




Optional fields:
- `AdminAccountId`: `str`
- `ServiceType`: `SecurityServiceType`
- `Data`: `str`
- `NextToken`: `str`


## GetProtocolsListResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetProtocolsListResponseTypeDef
```




Optional fields:
- `ProtocolsList`: `"ProtocolsListDataTypeDef"`
- `ProtocolsListArn`: `str`


## GetViolationDetailsResponseTypeDef

```python
from mypy_boto3_fms.type_defs import GetViolationDetailsResponseTypeDef
```




Optional fields:
- `ViolationDetail`: `"ViolationDetailTypeDef"`


## ListAppsListsResponseTypeDef

```python
from mypy_boto3_fms.type_defs import ListAppsListsResponseTypeDef
```




Optional fields:
- `AppsLists`: `List["AppsListDataSummaryTypeDef"]`
- `NextToken`: `str`


## ListComplianceStatusResponseTypeDef

```python
from mypy_boto3_fms.type_defs import ListComplianceStatusResponseTypeDef
```




Optional fields:
- `PolicyComplianceStatusList`: `List["PolicyComplianceStatusTypeDef"]`
- `NextToken`: `str`


## ListMemberAccountsResponseTypeDef

```python
from mypy_boto3_fms.type_defs import ListMemberAccountsResponseTypeDef
```




Optional fields:
- `MemberAccounts`: `List[str]`
- `NextToken`: `str`


## ListPoliciesResponseTypeDef

```python
from mypy_boto3_fms.type_defs import ListPoliciesResponseTypeDef
```




Optional fields:
- `PolicyList`: `List["PolicySummaryTypeDef"]`
- `NextToken`: `str`


## ListProtocolsListsResponseTypeDef

```python
from mypy_boto3_fms.type_defs import ListProtocolsListsResponseTypeDef
```




Optional fields:
- `ProtocolsLists`: `List["ProtocolsListDataSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_fms.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `TagList`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_fms.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutAppsListResponseTypeDef

```python
from mypy_boto3_fms.type_defs import PutAppsListResponseTypeDef
```




Optional fields:
- `AppsList`: `"AppsListDataTypeDef"`
- `AppsListArn`: `str`


## PutPolicyResponseTypeDef

```python
from mypy_boto3_fms.type_defs import PutPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `"PolicyTypeDef"`
- `PolicyArn`: `str`


## PutProtocolsListResponseTypeDef

```python
from mypy_boto3_fms.type_defs import PutProtocolsListResponseTypeDef
```




Optional fields:
- `ProtocolsList`: `"ProtocolsListDataTypeDef"`
- `ProtocolsListArn`: `str`

