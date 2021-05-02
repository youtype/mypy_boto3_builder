# Structures for boto3 GuardDuty module

> [Index](../index.md) > [GuardDuty](./index.md) > Structures

Auto-generated documentation for [GuardDuty](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty)
type annotations stubs module [mypy_boto3_guardduty](https://pypi.org/project/mypy-boto3-guardduty/).

- [Structures for boto3 GuardDuty module](#structures-for-boto3-guardduty-module)
  - [AccessControlListTypeDef](#accesscontrollisttypedef)
  - [AccessKeyDetailsTypeDef](#accesskeydetailstypedef)
  - [AccountDetailTypeDef](#accountdetailtypedef)
  - [AccountLevelPermissionsTypeDef](#accountlevelpermissionstypedef)
  - [ActionTypeDef](#actiontypedef)
  - [AdminAccountTypeDef](#adminaccounttypedef)
  - [AwsApiCallActionTypeDef](#awsapicallactiontypedef)
  - [BlockPublicAccessTypeDef](#blockpublicaccesstypedef)
  - [BucketLevelPermissionsTypeDef](#bucketlevelpermissionstypedef)
  - [BucketPolicyTypeDef](#bucketpolicytypedef)
  - [CityTypeDef](#citytypedef)
  - [CloudTrailConfigurationResultTypeDef](#cloudtrailconfigurationresulttypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [CountryTypeDef](#countrytypedef)
  - [CreateDetectorResponseTypeDef](#createdetectorresponsetypedef)
  - [CreateFilterResponseTypeDef](#createfilterresponsetypedef)
  - [CreateIPSetResponseTypeDef](#createipsetresponsetypedef)
  - [CreateMembersResponseTypeDef](#createmembersresponsetypedef)
  - [CreatePublishingDestinationResponseTypeDef](#createpublishingdestinationresponsetypedef)
  - [CreateThreatIntelSetResponseTypeDef](#createthreatintelsetresponsetypedef)
  - [DNSLogsConfigurationResultTypeDef](#dnslogsconfigurationresulttypedef)
  - [DataSourceConfigurationsResultTypeDef](#datasourceconfigurationsresulttypedef)
  - [DataSourceConfigurationsTypeDef](#datasourceconfigurationstypedef)
  - [DeclineInvitationsResponseTypeDef](#declineinvitationsresponsetypedef)
  - [DefaultServerSideEncryptionTypeDef](#defaultserversideencryptiontypedef)
  - [DeleteInvitationsResponseTypeDef](#deleteinvitationsresponsetypedef)
  - [DeleteMembersResponseTypeDef](#deletemembersresponsetypedef)
  - [DescribeOrganizationConfigurationResponseTypeDef](#describeorganizationconfigurationresponsetypedef)
  - [DescribePublishingDestinationResponseTypeDef](#describepublishingdestinationresponsetypedef)
  - [DestinationPropertiesTypeDef](#destinationpropertiestypedef)
  - [DestinationTypeDef](#destinationtypedef)
  - [DisassociateMembersResponseTypeDef](#disassociatemembersresponsetypedef)
  - [DnsRequestActionTypeDef](#dnsrequestactiontypedef)
  - [DomainDetailsTypeDef](#domaindetailstypedef)
  - [EvidenceTypeDef](#evidencetypedef)
  - [FindingCriteriaTypeDef](#findingcriteriatypedef)
  - [FindingStatisticsTypeDef](#findingstatisticstypedef)
  - [FindingTypeDef](#findingtypedef)
  - [FlowLogsConfigurationResultTypeDef](#flowlogsconfigurationresulttypedef)
  - [GeoLocationTypeDef](#geolocationtypedef)
  - [GetDetectorResponseTypeDef](#getdetectorresponsetypedef)
  - [GetFilterResponseTypeDef](#getfilterresponsetypedef)
  - [GetFindingsResponseTypeDef](#getfindingsresponsetypedef)
  - [GetFindingsStatisticsResponseTypeDef](#getfindingsstatisticsresponsetypedef)
  - [GetIPSetResponseTypeDef](#getipsetresponsetypedef)
  - [GetInvitationsCountResponseTypeDef](#getinvitationscountresponsetypedef)
  - [GetMasterAccountResponseTypeDef](#getmasteraccountresponsetypedef)
  - [GetMemberDetectorsResponseTypeDef](#getmemberdetectorsresponsetypedef)
  - [GetMembersResponseTypeDef](#getmembersresponsetypedef)
  - [GetThreatIntelSetResponseTypeDef](#getthreatintelsetresponsetypedef)
  - [GetUsageStatisticsResponseTypeDef](#getusagestatisticsresponsetypedef)
  - [IamInstanceProfileTypeDef](#iaminstanceprofiletypedef)
  - [InstanceDetailsTypeDef](#instancedetailstypedef)
  - [InvitationTypeDef](#invitationtypedef)
  - [InviteMembersResponseTypeDef](#invitemembersresponsetypedef)
  - [ListDetectorsResponseTypeDef](#listdetectorsresponsetypedef)
  - [ListFiltersResponseTypeDef](#listfiltersresponsetypedef)
  - [ListFindingsResponseTypeDef](#listfindingsresponsetypedef)
  - [ListIPSetsResponseTypeDef](#listipsetsresponsetypedef)
  - [ListInvitationsResponseTypeDef](#listinvitationsresponsetypedef)
  - [ListMembersResponseTypeDef](#listmembersresponsetypedef)
  - [ListOrganizationAdminAccountsResponseTypeDef](#listorganizationadminaccountsresponsetypedef)
  - [ListPublishingDestinationsResponseTypeDef](#listpublishingdestinationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListThreatIntelSetsResponseTypeDef](#listthreatintelsetsresponsetypedef)
  - [LocalIpDetailsTypeDef](#localipdetailstypedef)
  - [LocalPortDetailsTypeDef](#localportdetailstypedef)
  - [MasterTypeDef](#mastertypedef)
  - [MemberDataSourceConfigurationTypeDef](#memberdatasourceconfigurationtypedef)
  - [MemberTypeDef](#membertypedef)
  - [NetworkConnectionActionTypeDef](#networkconnectionactiontypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [OrganizationDataSourceConfigurationsResultTypeDef](#organizationdatasourceconfigurationsresulttypedef)
  - [OrganizationDataSourceConfigurationsTypeDef](#organizationdatasourceconfigurationstypedef)
  - [OrganizationS3LogsConfigurationResultTypeDef](#organizations3logsconfigurationresulttypedef)
  - [OrganizationS3LogsConfigurationTypeDef](#organizations3logsconfigurationtypedef)
  - [OrganizationTypeDef](#organizationtypedef)
  - [OwnerTypeDef](#ownertypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PermissionConfigurationTypeDef](#permissionconfigurationtypedef)
  - [PortProbeActionTypeDef](#portprobeactiontypedef)
  - [PortProbeDetailTypeDef](#portprobedetailtypedef)
  - [PrivateIpAddressDetailsTypeDef](#privateipaddressdetailstypedef)
  - [ProductCodeTypeDef](#productcodetypedef)
  - [PublicAccessTypeDef](#publicaccesstypedef)
  - [RemoteIpDetailsTypeDef](#remoteipdetailstypedef)
  - [RemotePortDetailsTypeDef](#remoteportdetailstypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [S3BucketDetailTypeDef](#s3bucketdetailtypedef)
  - [S3LogsConfigurationResultTypeDef](#s3logsconfigurationresulttypedef)
  - [S3LogsConfigurationTypeDef](#s3logsconfigurationtypedef)
  - [SecurityGroupTypeDef](#securitygrouptypedef)
  - [ServiceTypeDef](#servicetypedef)
  - [SortCriteriaTypeDef](#sortcriteriatypedef)
  - [StartMonitoringMembersResponseTypeDef](#startmonitoringmembersresponsetypedef)
  - [StopMonitoringMembersResponseTypeDef](#stopmonitoringmembersresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [ThreatIntelligenceDetailTypeDef](#threatintelligencedetailtypedef)
  - [TotalTypeDef](#totaltypedef)
  - [UnprocessedAccountTypeDef](#unprocessedaccounttypedef)
  - [UpdateFilterResponseTypeDef](#updatefilterresponsetypedef)
  - [UpdateMemberDetectorsResponseTypeDef](#updatememberdetectorsresponsetypedef)
  - [UsageAccountResultTypeDef](#usageaccountresulttypedef)
  - [UsageCriteriaTypeDef](#usagecriteriatypedef)
  - [UsageDataSourceResultTypeDef](#usagedatasourceresulttypedef)
  - [UsageResourceResultTypeDef](#usageresourceresulttypedef)
  - [UsageStatisticsTypeDef](#usagestatisticstypedef)

## AccessControlListTypeDef

```python
from mypy_boto3_guardduty.type_defs import AccessControlListTypeDef
```




Optional fields:
- `AllowsPublicReadAccess`: `bool`
- `AllowsPublicWriteAccess`: `bool`


## AccessKeyDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import AccessKeyDetailsTypeDef
```




Optional fields:
- `AccessKeyId`: `str`
- `PrincipalId`: `str`
- `UserName`: `str`
- `UserType`: `str`


## AccountDetailTypeDef

```python
from mypy_boto3_guardduty.type_defs import AccountDetailTypeDef
```


Required fields:
- `AccountId`: `str`
- `Email`: `str`




## AccountLevelPermissionsTypeDef

```python
from mypy_boto3_guardduty.type_defs import AccountLevelPermissionsTypeDef
```




Optional fields:
- `BlockPublicAccess`: `"BlockPublicAccessTypeDef"`


## ActionTypeDef

```python
from mypy_boto3_guardduty.type_defs import ActionTypeDef
```




Optional fields:
- `ActionType`: `str`
- `AwsApiCallAction`: `"AwsApiCallActionTypeDef"`
- `DnsRequestAction`: `"DnsRequestActionTypeDef"`
- `NetworkConnectionAction`: `"NetworkConnectionActionTypeDef"`
- `PortProbeAction`: `"PortProbeActionTypeDef"`


## AdminAccountTypeDef

```python
from mypy_boto3_guardduty.type_defs import AdminAccountTypeDef
```




Optional fields:
- `AdminAccountId`: `str`
- `AdminStatus`: `AdminStatus`


## AwsApiCallActionTypeDef

```python
from mypy_boto3_guardduty.type_defs import AwsApiCallActionTypeDef
```




Optional fields:
- `Api`: `str`
- `CallerType`: `str`
- `DomainDetails`: `"DomainDetailsTypeDef"`
- `ErrorCode`: `str`
- `RemoteIpDetails`: `"RemoteIpDetailsTypeDef"`
- `ServiceName`: `str`


## BlockPublicAccessTypeDef

```python
from mypy_boto3_guardduty.type_defs import BlockPublicAccessTypeDef
```




Optional fields:
- `IgnorePublicAcls`: `bool`
- `RestrictPublicBuckets`: `bool`
- `BlockPublicAcls`: `bool`
- `BlockPublicPolicy`: `bool`


## BucketLevelPermissionsTypeDef

```python
from mypy_boto3_guardduty.type_defs import BucketLevelPermissionsTypeDef
```




Optional fields:
- `AccessControlList`: `"AccessControlListTypeDef"`
- `BucketPolicy`: `"BucketPolicyTypeDef"`
- `BlockPublicAccess`: `"BlockPublicAccessTypeDef"`


## BucketPolicyTypeDef

```python
from mypy_boto3_guardduty.type_defs import BucketPolicyTypeDef
```




Optional fields:
- `AllowsPublicReadAccess`: `bool`
- `AllowsPublicWriteAccess`: `bool`


## CityTypeDef

```python
from mypy_boto3_guardduty.type_defs import CityTypeDef
```




Optional fields:
- `CityName`: `str`


## CloudTrailConfigurationResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import CloudTrailConfigurationResultTypeDef
```


Required fields:
- `Status`: `DataSourceStatus`




## ConditionTypeDef

```python
from mypy_boto3_guardduty.type_defs import ConditionTypeDef
```




Optional fields:
- `Eq`: `List[str]`
- `Neq`: `List[str]`
- `Gt`: `int`
- `Gte`: `int`
- `Lt`: `int`
- `Lte`: `int`
- `Equals`: `List[str]`
- `NotEquals`: `List[str]`
- `GreaterThan`: `int`
- `GreaterThanOrEqual`: `int`
- `LessThan`: `int`
- `LessThanOrEqual`: `int`


## CountryTypeDef

```python
from mypy_boto3_guardduty.type_defs import CountryTypeDef
```




Optional fields:
- `CountryCode`: `str`
- `CountryName`: `str`


## CreateDetectorResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import CreateDetectorResponseTypeDef
```




Optional fields:
- `DetectorId`: `str`


## CreateFilterResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import CreateFilterResponseTypeDef
```


Required fields:
- `Name`: `str`




## CreateIPSetResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import CreateIPSetResponseTypeDef
```


Required fields:
- `IpSetId`: `str`




## CreateMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import CreateMembersResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## CreatePublishingDestinationResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import CreatePublishingDestinationResponseTypeDef
```


Required fields:
- `DestinationId`: `str`




## CreateThreatIntelSetResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import CreateThreatIntelSetResponseTypeDef
```


Required fields:
- `ThreatIntelSetId`: `str`




## DNSLogsConfigurationResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import DNSLogsConfigurationResultTypeDef
```


Required fields:
- `Status`: `DataSourceStatus`




## DataSourceConfigurationsResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import DataSourceConfigurationsResultTypeDef
```


Required fields:
- `CloudTrail`: `"CloudTrailConfigurationResultTypeDef"`
- `DNSLogs`: `"DNSLogsConfigurationResultTypeDef"`
- `FlowLogs`: `"FlowLogsConfigurationResultTypeDef"`
- `S3Logs`: `"S3LogsConfigurationResultTypeDef"`




## DataSourceConfigurationsTypeDef

```python
from mypy_boto3_guardduty.type_defs import DataSourceConfigurationsTypeDef
```




Optional fields:
- `S3Logs`: `"S3LogsConfigurationTypeDef"`


## DeclineInvitationsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import DeclineInvitationsResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## DefaultServerSideEncryptionTypeDef

```python
from mypy_boto3_guardduty.type_defs import DefaultServerSideEncryptionTypeDef
```




Optional fields:
- `EncryptionType`: `str`
- `KmsMasterKeyArn`: `str`


## DeleteInvitationsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import DeleteInvitationsResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## DeleteMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import DeleteMembersResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## DescribeOrganizationConfigurationResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import DescribeOrganizationConfigurationResponseTypeDef
```


Required fields:
- `AutoEnable`: `bool`
- `MemberAccountLimitReached`: `bool`



Optional fields:
- `DataSources`: `"OrganizationDataSourceConfigurationsResultTypeDef"`


## DescribePublishingDestinationResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import DescribePublishingDestinationResponseTypeDef
```


Required fields:
- `DestinationId`: `str`
- `DestinationType`: `Literal['S3']`
- `Status`: `PublishingStatus`
- `PublishingFailureStartTimestamp`: `int`
- `DestinationProperties`: `"DestinationPropertiesTypeDef"`




## DestinationPropertiesTypeDef

```python
from mypy_boto3_guardduty.type_defs import DestinationPropertiesTypeDef
```




Optional fields:
- `DestinationArn`: `str`
- `KmsKeyArn`: `str`


## DestinationTypeDef

```python
from mypy_boto3_guardduty.type_defs import DestinationTypeDef
```


Required fields:
- `DestinationId`: `str`
- `DestinationType`: `Literal['S3']`
- `Status`: `PublishingStatus`




## DisassociateMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import DisassociateMembersResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## DnsRequestActionTypeDef

```python
from mypy_boto3_guardduty.type_defs import DnsRequestActionTypeDef
```




Optional fields:
- `Domain`: `str`


## DomainDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import DomainDetailsTypeDef
```




Optional fields:
- `Domain`: `str`


## EvidenceTypeDef

```python
from mypy_boto3_guardduty.type_defs import EvidenceTypeDef
```




Optional fields:
- `ThreatIntelligenceDetails`: `List["ThreatIntelligenceDetailTypeDef"]`


## FindingCriteriaTypeDef

```python
from mypy_boto3_guardduty.type_defs import FindingCriteriaTypeDef
```




Optional fields:
- `Criterion`: `Dict[str, "ConditionTypeDef"]`


## FindingStatisticsTypeDef

```python
from mypy_boto3_guardduty.type_defs import FindingStatisticsTypeDef
```




Optional fields:
- `CountBySeverity`: `Dict[str, int]`


## FindingTypeDef

```python
from mypy_boto3_guardduty.type_defs import FindingTypeDef
```


Required fields:
- `AccountId`: `str`
- `Arn`: `str`
- `CreatedAt`: `str`
- `Id`: `str`
- `Region`: `str`
- `Resource`: `"ResourceTypeDef"`
- `SchemaVersion`: `str`
- `Severity`: `float`
- `Type`: `str`
- `UpdatedAt`: `str`



Optional fields:
- `Confidence`: `float`
- `Description`: `str`
- `Partition`: `str`
- `Service`: `"ServiceTypeDef"`
- `Title`: `str`


## FlowLogsConfigurationResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import FlowLogsConfigurationResultTypeDef
```


Required fields:
- `Status`: `DataSourceStatus`




## GeoLocationTypeDef

```python
from mypy_boto3_guardduty.type_defs import GeoLocationTypeDef
```




Optional fields:
- `Lat`: `float`
- `Lon`: `float`


## GetDetectorResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetDetectorResponseTypeDef
```


Required fields:
- `ServiceRole`: `str`
- `Status`: `DetectorStatus`



Optional fields:
- `CreatedAt`: `str`
- `FindingPublishingFrequency`: `FindingPublishingFrequency`
- `UpdatedAt`: `str`
- `DataSources`: `"DataSourceConfigurationsResultTypeDef"`
- `Tags`: `Dict[str, str]`


## GetFilterResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetFilterResponseTypeDef
```


Required fields:
- `Name`: `str`
- `Action`: `FilterAction`
- `FindingCriteria`: `"FindingCriteriaTypeDef"`



Optional fields:
- `Description`: `str`
- `Rank`: `int`
- `Tags`: `Dict[str, str]`


## GetFindingsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetFindingsResponseTypeDef
```


Required fields:
- `Findings`: `List["FindingTypeDef"]`




## GetFindingsStatisticsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetFindingsStatisticsResponseTypeDef
```


Required fields:
- `FindingStatistics`: `"FindingStatisticsTypeDef"`




## GetIPSetResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetIPSetResponseTypeDef
```


Required fields:
- `Name`: `str`
- `Format`: `IpSetFormat`
- `Location`: `str`
- `Status`: `IpSetStatus`



Optional fields:
- `Tags`: `Dict[str, str]`


## GetInvitationsCountResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetInvitationsCountResponseTypeDef
```




Optional fields:
- `InvitationsCount`: `int`


## GetMasterAccountResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetMasterAccountResponseTypeDef
```


Required fields:
- `Master`: `"MasterTypeDef"`




## GetMemberDetectorsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetMemberDetectorsResponseTypeDef
```


Required fields:
- `MemberDataSourceConfigurations`: `List["MemberDataSourceConfigurationTypeDef"]`
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## GetMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetMembersResponseTypeDef
```


Required fields:
- `Members`: `List["MemberTypeDef"]`
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## GetThreatIntelSetResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetThreatIntelSetResponseTypeDef
```


Required fields:
- `Name`: `str`
- `Format`: `ThreatIntelSetFormat`
- `Location`: `str`
- `Status`: `ThreatIntelSetStatus`



Optional fields:
- `Tags`: `Dict[str, str]`


## GetUsageStatisticsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import GetUsageStatisticsResponseTypeDef
```




Optional fields:
- `UsageStatistics`: `"UsageStatisticsTypeDef"`
- `NextToken`: `str`


## IamInstanceProfileTypeDef

```python
from mypy_boto3_guardduty.type_defs import IamInstanceProfileTypeDef
```




Optional fields:
- `Arn`: `str`
- `Id`: `str`


## InstanceDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import InstanceDetailsTypeDef
```




Optional fields:
- `AvailabilityZone`: `str`
- `IamInstanceProfile`: `"IamInstanceProfileTypeDef"`
- `ImageDescription`: `str`
- `ImageId`: `str`
- `InstanceId`: `str`
- `InstanceState`: `str`
- `InstanceType`: `str`
- `OutpostArn`: `str`
- `LaunchTime`: `str`
- `NetworkInterfaces`: `List["NetworkInterfaceTypeDef"]`
- `Platform`: `str`
- `ProductCodes`: `List["ProductCodeTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## InvitationTypeDef

```python
from mypy_boto3_guardduty.type_defs import InvitationTypeDef
```




Optional fields:
- `AccountId`: `str`
- `InvitationId`: `str`
- `RelationshipStatus`: `str`
- `InvitedAt`: `str`


## InviteMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import InviteMembersResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## ListDetectorsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListDetectorsResponseTypeDef
```


Required fields:
- `DetectorIds`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListFiltersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListFiltersResponseTypeDef
```


Required fields:
- `FilterNames`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListFindingsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListFindingsResponseTypeDef
```


Required fields:
- `FindingIds`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListIPSetsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListIPSetsResponseTypeDef
```


Required fields:
- `IpSetIds`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListInvitationsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListInvitationsResponseTypeDef
```




Optional fields:
- `Invitations`: `List["InvitationTypeDef"]`
- `NextToken`: `str`


## ListMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListMembersResponseTypeDef
```




Optional fields:
- `Members`: `List["MemberTypeDef"]`
- `NextToken`: `str`


## ListOrganizationAdminAccountsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListOrganizationAdminAccountsResponseTypeDef
```




Optional fields:
- `AdminAccounts`: `List["AdminAccountTypeDef"]`
- `NextToken`: `str`


## ListPublishingDestinationsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListPublishingDestinationsResponseTypeDef
```


Required fields:
- `Destinations`: `List["DestinationTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListThreatIntelSetsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import ListThreatIntelSetsResponseTypeDef
```


Required fields:
- `ThreatIntelSetIds`: `List[str]`



Optional fields:
- `NextToken`: `str`


## LocalIpDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import LocalIpDetailsTypeDef
```




Optional fields:
- `IpAddressV4`: `str`


## LocalPortDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import LocalPortDetailsTypeDef
```




Optional fields:
- `Port`: `int`
- `PortName`: `str`


## MasterTypeDef

```python
from mypy_boto3_guardduty.type_defs import MasterTypeDef
```




Optional fields:
- `AccountId`: `str`
- `InvitationId`: `str`
- `RelationshipStatus`: `str`
- `InvitedAt`: `str`


## MemberDataSourceConfigurationTypeDef

```python
from mypy_boto3_guardduty.type_defs import MemberDataSourceConfigurationTypeDef
```


Required fields:
- `AccountId`: `str`
- `DataSources`: `"DataSourceConfigurationsResultTypeDef"`




## MemberTypeDef

```python
from mypy_boto3_guardduty.type_defs import MemberTypeDef
```


Required fields:
- `AccountId`: `str`
- `MasterId`: `str`
- `Email`: `str`
- `RelationshipStatus`: `str`
- `UpdatedAt`: `str`



Optional fields:
- `DetectorId`: `str`
- `InvitedAt`: `str`


## NetworkConnectionActionTypeDef

```python
from mypy_boto3_guardduty.type_defs import NetworkConnectionActionTypeDef
```




Optional fields:
- `Blocked`: `bool`
- `ConnectionDirection`: `str`
- `LocalPortDetails`: `"LocalPortDetailsTypeDef"`
- `Protocol`: `str`
- `LocalIpDetails`: `"LocalIpDetailsTypeDef"`
- `RemoteIpDetails`: `"RemoteIpDetailsTypeDef"`
- `RemotePortDetails`: `"RemotePortDetailsTypeDef"`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_guardduty.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `Ipv6Addresses`: `List[str]`
- `NetworkInterfaceId`: `str`
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`
- `PrivateIpAddresses`: `List["PrivateIpAddressDetailsTypeDef"]`
- `PublicDnsName`: `str`
- `PublicIp`: `str`
- `SecurityGroups`: `List["SecurityGroupTypeDef"]`
- `SubnetId`: `str`
- `VpcId`: `str`


## OrganizationDataSourceConfigurationsResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import OrganizationDataSourceConfigurationsResultTypeDef
```


Required fields:
- `S3Logs`: `"OrganizationS3LogsConfigurationResultTypeDef"`




## OrganizationDataSourceConfigurationsTypeDef

```python
from mypy_boto3_guardduty.type_defs import OrganizationDataSourceConfigurationsTypeDef
```




Optional fields:
- `S3Logs`: `"OrganizationS3LogsConfigurationTypeDef"`


## OrganizationS3LogsConfigurationResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import OrganizationS3LogsConfigurationResultTypeDef
```


Required fields:
- `AutoEnable`: `bool`




## OrganizationS3LogsConfigurationTypeDef

```python
from mypy_boto3_guardduty.type_defs import OrganizationS3LogsConfigurationTypeDef
```


Required fields:
- `AutoEnable`: `bool`




## OrganizationTypeDef

```python
from mypy_boto3_guardduty.type_defs import OrganizationTypeDef
```




Optional fields:
- `Asn`: `str`
- `AsnOrg`: `str`
- `Isp`: `str`
- `Org`: `str`


## OwnerTypeDef

```python
from mypy_boto3_guardduty.type_defs import OwnerTypeDef
```




Optional fields:
- `Id`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_guardduty.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PermissionConfigurationTypeDef

```python
from mypy_boto3_guardduty.type_defs import PermissionConfigurationTypeDef
```




Optional fields:
- `BucketLevelPermissions`: `"BucketLevelPermissionsTypeDef"`
- `AccountLevelPermissions`: `"AccountLevelPermissionsTypeDef"`


## PortProbeActionTypeDef

```python
from mypy_boto3_guardduty.type_defs import PortProbeActionTypeDef
```




Optional fields:
- `Blocked`: `bool`
- `PortProbeDetails`: `List["PortProbeDetailTypeDef"]`


## PortProbeDetailTypeDef

```python
from mypy_boto3_guardduty.type_defs import PortProbeDetailTypeDef
```




Optional fields:
- `LocalPortDetails`: `"LocalPortDetailsTypeDef"`
- `LocalIpDetails`: `"LocalIpDetailsTypeDef"`
- `RemoteIpDetails`: `"RemoteIpDetailsTypeDef"`


## PrivateIpAddressDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import PrivateIpAddressDetailsTypeDef
```




Optional fields:
- `PrivateDnsName`: `str`
- `PrivateIpAddress`: `str`


## ProductCodeTypeDef

```python
from mypy_boto3_guardduty.type_defs import ProductCodeTypeDef
```




Optional fields:
- `Code`: `str`
- `ProductType`: `str`


## PublicAccessTypeDef

```python
from mypy_boto3_guardduty.type_defs import PublicAccessTypeDef
```




Optional fields:
- `PermissionConfiguration`: `"PermissionConfigurationTypeDef"`
- `EffectivePermission`: `str`


## RemoteIpDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import RemoteIpDetailsTypeDef
```




Optional fields:
- `City`: `"CityTypeDef"`
- `Country`: `"CountryTypeDef"`
- `GeoLocation`: `"GeoLocationTypeDef"`
- `IpAddressV4`: `str`
- `Organization`: `"OrganizationTypeDef"`


## RemotePortDetailsTypeDef

```python
from mypy_boto3_guardduty.type_defs import RemotePortDetailsTypeDef
```




Optional fields:
- `Port`: `int`
- `PortName`: `str`


## ResourceTypeDef

```python
from mypy_boto3_guardduty.type_defs import ResourceTypeDef
```




Optional fields:
- `AccessKeyDetails`: `"AccessKeyDetailsTypeDef"`
- `S3BucketDetails`: `List["S3BucketDetailTypeDef"]`
- `InstanceDetails`: `"InstanceDetailsTypeDef"`
- `ResourceType`: `str`


## S3BucketDetailTypeDef

```python
from mypy_boto3_guardduty.type_defs import S3BucketDetailTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Type`: `str`
- `CreatedAt`: `datetime`
- `Owner`: `"OwnerTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `DefaultServerSideEncryption`: `"DefaultServerSideEncryptionTypeDef"`
- `PublicAccess`: `"PublicAccessTypeDef"`


## S3LogsConfigurationResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import S3LogsConfigurationResultTypeDef
```


Required fields:
- `Status`: `DataSourceStatus`




## S3LogsConfigurationTypeDef

```python
from mypy_boto3_guardduty.type_defs import S3LogsConfigurationTypeDef
```


Required fields:
- `Enable`: `bool`




## SecurityGroupTypeDef

```python
from mypy_boto3_guardduty.type_defs import SecurityGroupTypeDef
```




Optional fields:
- `GroupId`: `str`
- `GroupName`: `str`


## ServiceTypeDef

```python
from mypy_boto3_guardduty.type_defs import ServiceTypeDef
```




Optional fields:
- `Action`: `"ActionTypeDef"`
- `Evidence`: `"EvidenceTypeDef"`
- `Archived`: `bool`
- `Count`: `int`
- `DetectorId`: `str`
- `EventFirstSeen`: `str`
- `EventLastSeen`: `str`
- `ResourceRole`: `str`
- `ServiceName`: `str`
- `UserFeedback`: `str`


## SortCriteriaTypeDef

```python
from mypy_boto3_guardduty.type_defs import SortCriteriaTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `OrderBy`: `OrderBy`


## StartMonitoringMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import StartMonitoringMembersResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## StopMonitoringMembersResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import StopMonitoringMembersResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## TagTypeDef

```python
from mypy_boto3_guardduty.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## ThreatIntelligenceDetailTypeDef

```python
from mypy_boto3_guardduty.type_defs import ThreatIntelligenceDetailTypeDef
```




Optional fields:
- `ThreatListName`: `str`
- `ThreatNames`: `List[str]`


## TotalTypeDef

```python
from mypy_boto3_guardduty.type_defs import TotalTypeDef
```




Optional fields:
- `Amount`: `str`
- `Unit`: `str`


## UnprocessedAccountTypeDef

```python
from mypy_boto3_guardduty.type_defs import UnprocessedAccountTypeDef
```


Required fields:
- `AccountId`: `str`
- `Result`: `str`




## UpdateFilterResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import UpdateFilterResponseTypeDef
```


Required fields:
- `Name`: `str`




## UpdateMemberDetectorsResponseTypeDef

```python
from mypy_boto3_guardduty.type_defs import UpdateMemberDetectorsResponseTypeDef
```


Required fields:
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`




## UsageAccountResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import UsageAccountResultTypeDef
```




Optional fields:
- `AccountId`: `str`
- `Total`: `"TotalTypeDef"`


## UsageCriteriaTypeDef

```python
from mypy_boto3_guardduty.type_defs import UsageCriteriaTypeDef
```


Required fields:
- `DataSources`: `List[DataSource]`



Optional fields:
- `AccountIds`: `List[str]`
- `Resources`: `List[str]`


## UsageDataSourceResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import UsageDataSourceResultTypeDef
```




Optional fields:
- `DataSource`: `DataSource`
- `Total`: `"TotalTypeDef"`


## UsageResourceResultTypeDef

```python
from mypy_boto3_guardduty.type_defs import UsageResourceResultTypeDef
```




Optional fields:
- `Resource`: `str`
- `Total`: `"TotalTypeDef"`


## UsageStatisticsTypeDef

```python
from mypy_boto3_guardduty.type_defs import UsageStatisticsTypeDef
```




Optional fields:
- `SumByAccount`: `List["UsageAccountResultTypeDef"]`
- `SumByDataSource`: `List["UsageDataSourceResultTypeDef"]`
- `SumByResource`: `List["UsageResourceResultTypeDef"]`
- `TopResources`: `List["UsageResourceResultTypeDef"]`

