# Type annotations for boto3 FMS module

> [Index](../index.md) > FMS

Auto-generated documentation for [FMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS)
type annotations stubs module [mypy_boto3_fms](https://pypi.org/project/mypy-boto3-fms/).

```bash
pip install mypy-boto3-fms
```

- [Type annotations for boto3 FMS module](#type-annotations-for-boto3-fms-module)
  - [FMSClient](#fmsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## FMSClient

Type annotations for  `boto3.client("fms")` as [FMSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_fms.client import FMSClient
```


FMSClient [exceptions](./client.md#exceptions)



### Methods
- [associate_admin_account](./client.md#associate-admin-account)
- [can_paginate](./client.md#can-paginate)
- [delete_apps_list](./client.md#delete-apps-list)
- [delete_notification_channel](./client.md#delete-notification-channel)
- [delete_policy](./client.md#delete-policy)
- [delete_protocols_list](./client.md#delete-protocols-list)
- [disassociate_admin_account](./client.md#disassociate-admin-account)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_admin_account](./client.md#get-admin-account)
- [get_apps_list](./client.md#get-apps-list)
- [get_compliance_detail](./client.md#get-compliance-detail)
- [get_notification_channel](./client.md#get-notification-channel)
- [get_paginator](./client.md#get-paginator)
- [get_policy](./client.md#get-policy)
- [get_protection_status](./client.md#get-protection-status)
- [get_protocols_list](./client.md#get-protocols-list)
- [get_violation_details](./client.md#get-violation-details)
- [list_apps_lists](./client.md#list-apps-lists)
- [list_compliance_status](./client.md#list-compliance-status)
- [list_member_accounts](./client.md#list-member-accounts)
- [list_policies](./client.md#list-policies)
- [list_protocols_lists](./client.md#list-protocols-lists)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_apps_list](./client.md#put-apps-list)
- [put_notification_channel](./client.md#put-notification-channel)
- [put_policy](./client.md#put-policy)
- [put_protocols_list](./client.md#put-protocols-list)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidTypeException](./client.md#invalidtypeexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("fms").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_fms.paginators import ListComplianceStatusPaginator, ...
```

- [ListComplianceStatusPaginator](./paginators.md#listcompliancestatuspaginator)
- [ListMemberAccountsPaginator](./paginators.md#listmemberaccountspaginator)
- [ListPoliciesPaginator](./paginators.md#listpoliciespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_fms.literals import AccountRoleStatus, ...
```

- [AccountRoleStatus](./literals.md#accountrolestatus)
- [CustomerPolicyScopeIdType](./literals.md#customerpolicyscopeidtype)
- [DependentServiceName](./literals.md#dependentservicename)
- [ListComplianceStatusPaginatorName](./literals.md#listcompliancestatuspaginatorname)
- [ListMemberAccountsPaginatorName](./literals.md#listmemberaccountspaginatorname)
- [ListPoliciesPaginatorName](./literals.md#listpoliciespaginatorname)
- [PolicyComplianceStatusType](./literals.md#policycompliancestatustype)
- [RemediationActionType](./literals.md#remediationactiontype)
- [SecurityServiceType](./literals.md#securityservicetype)
- [ViolationReason](./literals.md#violationreason)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_fms.type_defs import AppTypeDef, ...
```

- [AppTypeDef](./type_defs.md#apptypedef)
- [AppsListDataSummaryTypeDef](./type_defs.md#appslistdatasummarytypedef)
- [AppsListDataTypeDef](./type_defs.md#appslistdatatypedef)
- [AwsEc2InstanceViolationTypeDef](./type_defs.md#awsec2instanceviolationtypedef)
- [AwsEc2NetworkInterfaceViolationTypeDef](./type_defs.md#awsec2networkinterfaceviolationtypedef)
- [AwsVPCSecurityGroupViolationTypeDef](./type_defs.md#awsvpcsecuritygroupviolationtypedef)
- [ComplianceViolatorTypeDef](./type_defs.md#complianceviolatortypedef)
- [DnsDuplicateRuleGroupViolationTypeDef](./type_defs.md#dnsduplicaterulegroupviolationtypedef)
- [DnsRuleGroupLimitExceededViolationTypeDef](./type_defs.md#dnsrulegrouplimitexceededviolationtypedef)
- [DnsRuleGroupPriorityConflictViolationTypeDef](./type_defs.md#dnsrulegrouppriorityconflictviolationtypedef)
- [EvaluationResultTypeDef](./type_defs.md#evaluationresulttypedef)
- [GetAdminAccountResponseTypeDef](./type_defs.md#getadminaccountresponsetypedef)
- [GetAppsListResponseTypeDef](./type_defs.md#getappslistresponsetypedef)
- [GetComplianceDetailResponseTypeDef](./type_defs.md#getcompliancedetailresponsetypedef)
- [GetNotificationChannelResponseTypeDef](./type_defs.md#getnotificationchannelresponsetypedef)
- [GetPolicyResponseTypeDef](./type_defs.md#getpolicyresponsetypedef)
- [GetProtectionStatusResponseTypeDef](./type_defs.md#getprotectionstatusresponsetypedef)
- [GetProtocolsListResponseTypeDef](./type_defs.md#getprotocolslistresponsetypedef)
- [GetViolationDetailsResponseTypeDef](./type_defs.md#getviolationdetailsresponsetypedef)
- [ListAppsListsResponseTypeDef](./type_defs.md#listappslistsresponsetypedef)
- [ListComplianceStatusResponseTypeDef](./type_defs.md#listcompliancestatusresponsetypedef)
- [ListMemberAccountsResponseTypeDef](./type_defs.md#listmemberaccountsresponsetypedef)
- [ListPoliciesResponseTypeDef](./type_defs.md#listpoliciesresponsetypedef)
- [ListProtocolsListsResponseTypeDef](./type_defs.md#listprotocolslistsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NetworkFirewallMissingExpectedRTViolationTypeDef](./type_defs.md#networkfirewallmissingexpectedrtviolationtypedef)
- [NetworkFirewallMissingFirewallViolationTypeDef](./type_defs.md#networkfirewallmissingfirewallviolationtypedef)
- [NetworkFirewallMissingSubnetViolationTypeDef](./type_defs.md#networkfirewallmissingsubnetviolationtypedef)
- [NetworkFirewallPolicyDescriptionTypeDef](./type_defs.md#networkfirewallpolicydescriptiontypedef)
- [NetworkFirewallPolicyModifiedViolationTypeDef](./type_defs.md#networkfirewallpolicymodifiedviolationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PartialMatchTypeDef](./type_defs.md#partialmatchtypedef)
- [PolicyComplianceDetailTypeDef](./type_defs.md#policycompliancedetailtypedef)
- [PolicyComplianceStatusTypeDef](./type_defs.md#policycompliancestatustypedef)
- [PolicySummaryTypeDef](./type_defs.md#policysummarytypedef)
- [PolicyTypeDef](./type_defs.md#policytypedef)
- [ProtocolsListDataSummaryTypeDef](./type_defs.md#protocolslistdatasummarytypedef)
- [ProtocolsListDataTypeDef](./type_defs.md#protocolslistdatatypedef)
- [PutAppsListResponseTypeDef](./type_defs.md#putappslistresponsetypedef)
- [PutPolicyResponseTypeDef](./type_defs.md#putpolicyresponsetypedef)
- [PutProtocolsListResponseTypeDef](./type_defs.md#putprotocolslistresponsetypedef)
- [ResourceTagTypeDef](./type_defs.md#resourcetagtypedef)
- [ResourceViolationTypeDef](./type_defs.md#resourceviolationtypedef)
- [SecurityGroupRemediationActionTypeDef](./type_defs.md#securitygroupremediationactiontypedef)
- [SecurityGroupRuleDescriptionTypeDef](./type_defs.md#securitygroupruledescriptiontypedef)
- [SecurityServicePolicyDataTypeDef](./type_defs.md#securityservicepolicydatatypedef)
- [StatefulRuleGroupTypeDef](./type_defs.md#statefulrulegrouptypedef)
- [StatelessRuleGroupTypeDef](./type_defs.md#statelessrulegrouptypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [ViolationDetailTypeDef](./type_defs.md#violationdetailtypedef)
