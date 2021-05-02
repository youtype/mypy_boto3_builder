# Type annotations for boto3 GuardDuty module

> [Index](../index.md) > GuardDuty

Auto-generated documentation for [GuardDuty](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty)
type annotations stubs module [mypy_boto3_guardduty](https://pypi.org/project/mypy-boto3-guardduty/).

```bash
pip install mypy-boto3-guardduty
```

- [Type annotations for boto3 GuardDuty module](#type-annotations-for-boto3-guardduty-module)
  - [GuardDutyClient](#guarddutyclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## GuardDutyClient

Type annotations for  `boto3.client("guardduty")` as [GuardDutyClient](./client.md)

Can be used directly:

```python
from mypy_boto3_guardduty.client import GuardDutyClient
```


GuardDutyClient [exceptions](./client.md#exceptions)



### Methods
- [accept_invitation](./client.md#accept-invitation)
- [archive_findings](./client.md#archive-findings)
- [can_paginate](./client.md#can-paginate)
- [create_detector](./client.md#create-detector)
- [create_filter](./client.md#create-filter)
- [create_ip_set](./client.md#create-ip-set)
- [create_members](./client.md#create-members)
- [create_publishing_destination](./client.md#create-publishing-destination)
- [create_sample_findings](./client.md#create-sample-findings)
- [create_threat_intel_set](./client.md#create-threat-intel-set)
- [decline_invitations](./client.md#decline-invitations)
- [delete_detector](./client.md#delete-detector)
- [delete_filter](./client.md#delete-filter)
- [delete_invitations](./client.md#delete-invitations)
- [delete_ip_set](./client.md#delete-ip-set)
- [delete_members](./client.md#delete-members)
- [delete_publishing_destination](./client.md#delete-publishing-destination)
- [delete_threat_intel_set](./client.md#delete-threat-intel-set)
- [describe_organization_configuration](./client.md#describe-organization-configuration)
- [describe_publishing_destination](./client.md#describe-publishing-destination)
- [disable_organization_admin_account](./client.md#disable-organization-admin-account)
- [disassociate_from_master_account](./client.md#disassociate-from-master-account)
- [disassociate_members](./client.md#disassociate-members)
- [enable_organization_admin_account](./client.md#enable-organization-admin-account)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_detector](./client.md#get-detector)
- [get_filter](./client.md#get-filter)
- [get_findings](./client.md#get-findings)
- [get_findings_statistics](./client.md#get-findings-statistics)
- [get_invitations_count](./client.md#get-invitations-count)
- [get_ip_set](./client.md#get-ip-set)
- [get_master_account](./client.md#get-master-account)
- [get_member_detectors](./client.md#get-member-detectors)
- [get_members](./client.md#get-members)
- [get_paginator](./client.md#get-paginator)
- [get_threat_intel_set](./client.md#get-threat-intel-set)
- [get_usage_statistics](./client.md#get-usage-statistics)
- [invite_members](./client.md#invite-members)
- [list_detectors](./client.md#list-detectors)
- [list_filters](./client.md#list-filters)
- [list_findings](./client.md#list-findings)
- [list_invitations](./client.md#list-invitations)
- [list_ip_sets](./client.md#list-ip-sets)
- [list_members](./client.md#list-members)
- [list_organization_admin_accounts](./client.md#list-organization-admin-accounts)
- [list_publishing_destinations](./client.md#list-publishing-destinations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_threat_intel_sets](./client.md#list-threat-intel-sets)
- [start_monitoring_members](./client.md#start-monitoring-members)
- [stop_monitoring_members](./client.md#stop-monitoring-members)
- [tag_resource](./client.md#tag-resource)
- [unarchive_findings](./client.md#unarchive-findings)
- [untag_resource](./client.md#untag-resource)
- [update_detector](./client.md#update-detector)
- [update_filter](./client.md#update-filter)
- [update_findings_feedback](./client.md#update-findings-feedback)
- [update_ip_set](./client.md#update-ip-set)
- [update_member_detectors](./client.md#update-member-detectors)
- [update_organization_configuration](./client.md#update-organization-configuration)
- [update_publishing_destination](./client.md#update-publishing-destination)
- [update_threat_intel_set](./client.md#update-threat-intel-set)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalServerErrorException](./client.md#internalservererrorexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("guardduty").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_guardduty.paginators import ListDetectorsPaginator, ...
```

- [ListDetectorsPaginator](./paginators.md#listdetectorspaginator)
- [ListFiltersPaginator](./paginators.md#listfilterspaginator)
- [ListFindingsPaginator](./paginators.md#listfindingspaginator)
- [ListIPSetsPaginator](./paginators.md#listipsetspaginator)
- [ListInvitationsPaginator](./paginators.md#listinvitationspaginator)
- [ListMembersPaginator](./paginators.md#listmemberspaginator)
- [ListOrganizationAdminAccountsPaginator](./paginators.md#listorganizationadminaccountspaginator)
- [ListThreatIntelSetsPaginator](./paginators.md#listthreatintelsetspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_guardduty.literals import AdminStatus, ...
```

- [AdminStatus](./literals.md#adminstatus)
- [DataSource](./literals.md#datasource)
- [DataSourceStatus](./literals.md#datasourcestatus)
- [DestinationType](./literals.md#destinationtype)
- [DetectorStatus](./literals.md#detectorstatus)
- [Feedback](./literals.md#feedback)
- [FilterAction](./literals.md#filteraction)
- [FindingPublishingFrequency](./literals.md#findingpublishingfrequency)
- [FindingStatisticType](./literals.md#findingstatistictype)
- [IpSetFormat](./literals.md#ipsetformat)
- [IpSetStatus](./literals.md#ipsetstatus)
- [ListDetectorsPaginatorName](./literals.md#listdetectorspaginatorname)
- [ListFiltersPaginatorName](./literals.md#listfilterspaginatorname)
- [ListFindingsPaginatorName](./literals.md#listfindingspaginatorname)
- [ListIPSetsPaginatorName](./literals.md#listipsetspaginatorname)
- [ListInvitationsPaginatorName](./literals.md#listinvitationspaginatorname)
- [ListMembersPaginatorName](./literals.md#listmemberspaginatorname)
- [ListOrganizationAdminAccountsPaginatorName](./literals.md#listorganizationadminaccountspaginatorname)
- [ListThreatIntelSetsPaginatorName](./literals.md#listthreatintelsetspaginatorname)
- [OrderBy](./literals.md#orderby)
- [PublishingStatus](./literals.md#publishingstatus)
- [ThreatIntelSetFormat](./literals.md#threatintelsetformat)
- [ThreatIntelSetStatus](./literals.md#threatintelsetstatus)
- [UsageStatisticType](./literals.md#usagestatistictype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_guardduty.type_defs import AccessControlListTypeDef, ...
```

- [AccessControlListTypeDef](./type_defs.md#accesscontrollisttypedef)
- [AccessKeyDetailsTypeDef](./type_defs.md#accesskeydetailstypedef)
- [AccountLevelPermissionsTypeDef](./type_defs.md#accountlevelpermissionstypedef)
- [ActionTypeDef](./type_defs.md#actiontypedef)
- [AdminAccountTypeDef](./type_defs.md#adminaccounttypedef)
- [AwsApiCallActionTypeDef](./type_defs.md#awsapicallactiontypedef)
- [BlockPublicAccessTypeDef](./type_defs.md#blockpublicaccesstypedef)
- [BucketLevelPermissionsTypeDef](./type_defs.md#bucketlevelpermissionstypedef)
- [BucketPolicyTypeDef](./type_defs.md#bucketpolicytypedef)
- [CityTypeDef](./type_defs.md#citytypedef)
- [CloudTrailConfigurationResultTypeDef](./type_defs.md#cloudtrailconfigurationresulttypedef)
- [ConditionTypeDef](./type_defs.md#conditiontypedef)
- [CountryTypeDef](./type_defs.md#countrytypedef)
- [DNSLogsConfigurationResultTypeDef](./type_defs.md#dnslogsconfigurationresulttypedef)
- [DataSourceConfigurationsResultTypeDef](./type_defs.md#datasourceconfigurationsresulttypedef)
- [DefaultServerSideEncryptionTypeDef](./type_defs.md#defaultserversideencryptiontypedef)
- [DestinationPropertiesTypeDef](./type_defs.md#destinationpropertiestypedef)
- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [DnsRequestActionTypeDef](./type_defs.md#dnsrequestactiontypedef)
- [DomainDetailsTypeDef](./type_defs.md#domaindetailstypedef)
- [EvidenceTypeDef](./type_defs.md#evidencetypedef)
- [FindingCriteriaTypeDef](./type_defs.md#findingcriteriatypedef)
- [FindingStatisticsTypeDef](./type_defs.md#findingstatisticstypedef)
- [FindingTypeDef](./type_defs.md#findingtypedef)
- [FlowLogsConfigurationResultTypeDef](./type_defs.md#flowlogsconfigurationresulttypedef)
- [GeoLocationTypeDef](./type_defs.md#geolocationtypedef)
- [IamInstanceProfileTypeDef](./type_defs.md#iaminstanceprofiletypedef)
- [InstanceDetailsTypeDef](./type_defs.md#instancedetailstypedef)
- [InvitationTypeDef](./type_defs.md#invitationtypedef)
- [LocalIpDetailsTypeDef](./type_defs.md#localipdetailstypedef)
- [LocalPortDetailsTypeDef](./type_defs.md#localportdetailstypedef)
- [MasterTypeDef](./type_defs.md#mastertypedef)
- [MemberDataSourceConfigurationTypeDef](./type_defs.md#memberdatasourceconfigurationtypedef)
- [MemberTypeDef](./type_defs.md#membertypedef)
- [NetworkConnectionActionTypeDef](./type_defs.md#networkconnectionactiontypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [OrganizationDataSourceConfigurationsResultTypeDef](./type_defs.md#organizationdatasourceconfigurationsresulttypedef)
- [OrganizationS3LogsConfigurationResultTypeDef](./type_defs.md#organizations3logsconfigurationresulttypedef)
- [OrganizationS3LogsConfigurationTypeDef](./type_defs.md#organizations3logsconfigurationtypedef)
- [OrganizationTypeDef](./type_defs.md#organizationtypedef)
- [OwnerTypeDef](./type_defs.md#ownertypedef)
- [PermissionConfigurationTypeDef](./type_defs.md#permissionconfigurationtypedef)
- [PortProbeActionTypeDef](./type_defs.md#portprobeactiontypedef)
- [PortProbeDetailTypeDef](./type_defs.md#portprobedetailtypedef)
- [PrivateIpAddressDetailsTypeDef](./type_defs.md#privateipaddressdetailstypedef)
- [ProductCodeTypeDef](./type_defs.md#productcodetypedef)
- [PublicAccessTypeDef](./type_defs.md#publicaccesstypedef)
- [RemoteIpDetailsTypeDef](./type_defs.md#remoteipdetailstypedef)
- [RemotePortDetailsTypeDef](./type_defs.md#remoteportdetailstypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [S3BucketDetailTypeDef](./type_defs.md#s3bucketdetailtypedef)
- [S3LogsConfigurationResultTypeDef](./type_defs.md#s3logsconfigurationresulttypedef)
- [S3LogsConfigurationTypeDef](./type_defs.md#s3logsconfigurationtypedef)
- [SecurityGroupTypeDef](./type_defs.md#securitygrouptypedef)
- [ServiceTypeDef](./type_defs.md#servicetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [ThreatIntelligenceDetailTypeDef](./type_defs.md#threatintelligencedetailtypedef)
- [TotalTypeDef](./type_defs.md#totaltypedef)
- [UnprocessedAccountTypeDef](./type_defs.md#unprocessedaccounttypedef)
- [UsageAccountResultTypeDef](./type_defs.md#usageaccountresulttypedef)
- [UsageDataSourceResultTypeDef](./type_defs.md#usagedatasourceresulttypedef)
- [UsageResourceResultTypeDef](./type_defs.md#usageresourceresulttypedef)
- [UsageStatisticsTypeDef](./type_defs.md#usagestatisticstypedef)
- [AccountDetailTypeDef](./type_defs.md#accountdetailtypedef)
- [CreateDetectorResponseTypeDef](./type_defs.md#createdetectorresponsetypedef)
- [CreateFilterResponseTypeDef](./type_defs.md#createfilterresponsetypedef)
- [CreateIPSetResponseTypeDef](./type_defs.md#createipsetresponsetypedef)
- [CreateMembersResponseTypeDef](./type_defs.md#createmembersresponsetypedef)
- [CreatePublishingDestinationResponseTypeDef](./type_defs.md#createpublishingdestinationresponsetypedef)
- [CreateThreatIntelSetResponseTypeDef](./type_defs.md#createthreatintelsetresponsetypedef)
- [DataSourceConfigurationsTypeDef](./type_defs.md#datasourceconfigurationstypedef)
- [DeclineInvitationsResponseTypeDef](./type_defs.md#declineinvitationsresponsetypedef)
- [DeleteInvitationsResponseTypeDef](./type_defs.md#deleteinvitationsresponsetypedef)
- [DeleteMembersResponseTypeDef](./type_defs.md#deletemembersresponsetypedef)
- [DescribeOrganizationConfigurationResponseTypeDef](./type_defs.md#describeorganizationconfigurationresponsetypedef)
- [DescribePublishingDestinationResponseTypeDef](./type_defs.md#describepublishingdestinationresponsetypedef)
- [DisassociateMembersResponseTypeDef](./type_defs.md#disassociatemembersresponsetypedef)
- [GetDetectorResponseTypeDef](./type_defs.md#getdetectorresponsetypedef)
- [GetFilterResponseTypeDef](./type_defs.md#getfilterresponsetypedef)
- [GetFindingsResponseTypeDef](./type_defs.md#getfindingsresponsetypedef)
- [GetFindingsStatisticsResponseTypeDef](./type_defs.md#getfindingsstatisticsresponsetypedef)
- [GetIPSetResponseTypeDef](./type_defs.md#getipsetresponsetypedef)
- [GetInvitationsCountResponseTypeDef](./type_defs.md#getinvitationscountresponsetypedef)
- [GetMasterAccountResponseTypeDef](./type_defs.md#getmasteraccountresponsetypedef)
- [GetMemberDetectorsResponseTypeDef](./type_defs.md#getmemberdetectorsresponsetypedef)
- [GetMembersResponseTypeDef](./type_defs.md#getmembersresponsetypedef)
- [GetThreatIntelSetResponseTypeDef](./type_defs.md#getthreatintelsetresponsetypedef)
- [GetUsageStatisticsResponseTypeDef](./type_defs.md#getusagestatisticsresponsetypedef)
- [InviteMembersResponseTypeDef](./type_defs.md#invitemembersresponsetypedef)
- [ListDetectorsResponseTypeDef](./type_defs.md#listdetectorsresponsetypedef)
- [ListFiltersResponseTypeDef](./type_defs.md#listfiltersresponsetypedef)
- [ListFindingsResponseTypeDef](./type_defs.md#listfindingsresponsetypedef)
- [ListIPSetsResponseTypeDef](./type_defs.md#listipsetsresponsetypedef)
- [ListInvitationsResponseTypeDef](./type_defs.md#listinvitationsresponsetypedef)
- [ListMembersResponseTypeDef](./type_defs.md#listmembersresponsetypedef)
- [ListOrganizationAdminAccountsResponseTypeDef](./type_defs.md#listorganizationadminaccountsresponsetypedef)
- [ListPublishingDestinationsResponseTypeDef](./type_defs.md#listpublishingdestinationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListThreatIntelSetsResponseTypeDef](./type_defs.md#listthreatintelsetsresponsetypedef)
- [OrganizationDataSourceConfigurationsTypeDef](./type_defs.md#organizationdatasourceconfigurationstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [SortCriteriaTypeDef](./type_defs.md#sortcriteriatypedef)
- [StartMonitoringMembersResponseTypeDef](./type_defs.md#startmonitoringmembersresponsetypedef)
- [StopMonitoringMembersResponseTypeDef](./type_defs.md#stopmonitoringmembersresponsetypedef)
- [UpdateFilterResponseTypeDef](./type_defs.md#updatefilterresponsetypedef)
- [UpdateMemberDetectorsResponseTypeDef](./type_defs.md#updatememberdetectorsresponsetypedef)
- [UsageCriteriaTypeDef](./type_defs.md#usagecriteriatypedef)
