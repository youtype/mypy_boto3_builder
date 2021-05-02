# Structures for boto3 Macie2 module

> [Index](../index.md) > [Macie2](./index.md) > Structures

Auto-generated documentation for [Macie2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2)
type annotations stubs module [mypy_boto3_macie2](https://pypi.org/project/mypy-boto3-macie2/).

- [Structures for boto3 Macie2 module](#structures-for-boto3-macie2-module)
  - [AccessControlListTypeDef](#accesscontrollisttypedef)
  - [AccountLevelPermissionsTypeDef](#accountlevelpermissionstypedef)
  - [AdminAccountTypeDef](#adminaccounttypedef)
  - [ApiCallDetailsTypeDef](#apicalldetailstypedef)
  - [AssumedRoleTypeDef](#assumedroletypedef)
  - [AwsAccountTypeDef](#awsaccounttypedef)
  - [AwsServiceTypeDef](#awsservicetypedef)
  - [BatchGetCustomDataIdentifierSummaryTypeDef](#batchgetcustomdataidentifiersummarytypedef)
  - [BlockPublicAccessTypeDef](#blockpublicaccesstypedef)
  - [BucketCountByEffectivePermissionTypeDef](#bucketcountbyeffectivepermissiontypedef)
  - [BucketCountByEncryptionTypeTypeDef](#bucketcountbyencryptiontypetypedef)
  - [BucketCountBySharedAccessTypeTypeDef](#bucketcountbysharedaccesstypetypedef)
  - [BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef](#bucketcountpolicyallowsunencryptedobjectuploadstypedef)
  - [BucketLevelPermissionsTypeDef](#bucketlevelpermissionstypedef)
  - [BucketMetadataTypeDef](#bucketmetadatatypedef)
  - [BucketPermissionConfigurationTypeDef](#bucketpermissionconfigurationtypedef)
  - [BucketPolicyTypeDef](#bucketpolicytypedef)
  - [BucketPublicAccessTypeDef](#bucketpublicaccesstypedef)
  - [BucketServerSideEncryptionTypeDef](#bucketserversideencryptiontypedef)
  - [CellTypeDef](#celltypedef)
  - [ClassificationDetailsTypeDef](#classificationdetailstypedef)
  - [ClassificationExportConfigurationTypeDef](#classificationexportconfigurationtypedef)
  - [ClassificationResultStatusTypeDef](#classificationresultstatustypedef)
  - [ClassificationResultTypeDef](#classificationresulttypedef)
  - [CriterionAdditionalPropertiesTypeDef](#criterionadditionalpropertiestypedef)
  - [CustomDataIdentifierSummaryTypeDef](#customdataidentifiersummarytypedef)
  - [CustomDataIdentifiersTypeDef](#customdataidentifierstypedef)
  - [CustomDetectionTypeDef](#customdetectiontypedef)
  - [DefaultDetectionTypeDef](#defaultdetectiontypedef)
  - [DomainDetailsTypeDef](#domaindetailstypedef)
  - [FederatedUserTypeDef](#federatedusertypedef)
  - [FindingActionTypeDef](#findingactiontypedef)
  - [FindingActorTypeDef](#findingactortypedef)
  - [FindingCriteriaTypeDef](#findingcriteriatypedef)
  - [FindingTypeDef](#findingtypedef)
  - [FindingsFilterListItemTypeDef](#findingsfilterlistitemtypedef)
  - [GroupCountTypeDef](#groupcounttypedef)
  - [IamUserTypeDef](#iamusertypedef)
  - [InvitationTypeDef](#invitationtypedef)
  - [IpAddressDetailsTypeDef](#ipaddressdetailstypedef)
  - [IpCityTypeDef](#ipcitytypedef)
  - [IpCountryTypeDef](#ipcountrytypedef)
  - [IpGeoLocationTypeDef](#ipgeolocationtypedef)
  - [IpOwnerTypeDef](#ipownertypedef)
  - [JobDetailsTypeDef](#jobdetailstypedef)
  - [JobScheduleFrequencyTypeDef](#jobschedulefrequencytypedef)
  - [JobScopeTermTypeDef](#jobscopetermtypedef)
  - [JobScopingBlockTypeDef](#jobscopingblocktypedef)
  - [JobSummaryTypeDef](#jobsummarytypedef)
  - [KeyValuePairTypeDef](#keyvaluepairtypedef)
  - [LastRunErrorStatusTypeDef](#lastrunerrorstatustypedef)
  - [ListJobsFilterTermTypeDef](#listjobsfiltertermtypedef)
  - [MemberTypeDef](#membertypedef)
  - [MonthlyScheduleTypeDef](#monthlyscheduletypedef)
  - [ObjectCountByEncryptionTypeTypeDef](#objectcountbyencryptiontypetypedef)
  - [ObjectLevelStatisticsTypeDef](#objectlevelstatisticstypedef)
  - [OccurrencesTypeDef](#occurrencestypedef)
  - [PageTypeDef](#pagetypedef)
  - [PolicyDetailsTypeDef](#policydetailstypedef)
  - [RangeTypeDef](#rangetypedef)
  - [RecordTypeDef](#recordtypedef)
  - [ReplicationDetailsTypeDef](#replicationdetailstypedef)
  - [ResourcesAffectedTypeDef](#resourcesaffectedtypedef)
  - [S3BucketDefinitionForJobTypeDef](#s3bucketdefinitionforjobtypedef)
  - [S3BucketOwnerTypeDef](#s3bucketownertypedef)
  - [S3BucketTypeDef](#s3buckettypedef)
  - [S3DestinationTypeDef](#s3destinationtypedef)
  - [S3JobDefinitionTypeDef](#s3jobdefinitiontypedef)
  - [S3ObjectTypeDef](#s3objecttypedef)
  - [ScopingTypeDef](#scopingtypedef)
  - [SecurityHubConfigurationTypeDef](#securityhubconfigurationtypedef)
  - [SensitiveDataItemTypeDef](#sensitivedataitemtypedef)
  - [ServerSideEncryptionTypeDef](#serversideencryptiontypedef)
  - [ServiceLimitTypeDef](#servicelimittypedef)
  - [SessionContextAttributesTypeDef](#sessioncontextattributestypedef)
  - [SessionContextTypeDef](#sessioncontexttypedef)
  - [SessionIssuerTypeDef](#sessionissuertypedef)
  - [SeverityTypeDef](#severitytypedef)
  - [SimpleScopeTermTypeDef](#simplescopetermtypedef)
  - [StatisticsTypeDef](#statisticstypedef)
  - [TagScopeTermTypeDef](#tagscopetermtypedef)
  - [TagValuePairTypeDef](#tagvaluepairtypedef)
  - [UnprocessedAccountTypeDef](#unprocessedaccounttypedef)
  - [UsageByAccountTypeDef](#usagebyaccounttypedef)
  - [UsageRecordTypeDef](#usagerecordtypedef)
  - [UsageTotalTypeDef](#usagetotaltypedef)
  - [UserIdentityRootTypeDef](#useridentityroottypedef)
  - [UserIdentityTypeDef](#useridentitytypedef)
  - [UserPausedDetailsTypeDef](#userpauseddetailstypedef)
  - [WeeklyScheduleTypeDef](#weeklyscheduletypedef)
  - [AccountDetailTypeDef](#accountdetailtypedef)
  - [BatchGetCustomDataIdentifiersResponseTypeDef](#batchgetcustomdataidentifiersresponsetypedef)
  - [BucketCriteriaAdditionalPropertiesTypeDef](#bucketcriteriaadditionalpropertiestypedef)
  - [BucketSortCriteriaTypeDef](#bucketsortcriteriatypedef)
  - [CreateClassificationJobResponseTypeDef](#createclassificationjobresponsetypedef)
  - [CreateCustomDataIdentifierResponseTypeDef](#createcustomdataidentifierresponsetypedef)
  - [CreateFindingsFilterResponseTypeDef](#createfindingsfilterresponsetypedef)
  - [CreateInvitationsResponseTypeDef](#createinvitationsresponsetypedef)
  - [CreateMemberResponseTypeDef](#creatememberresponsetypedef)
  - [DeclineInvitationsResponseTypeDef](#declineinvitationsresponsetypedef)
  - [DeleteInvitationsResponseTypeDef](#deleteinvitationsresponsetypedef)
  - [DescribeBucketsResponseTypeDef](#describebucketsresponsetypedef)
  - [DescribeClassificationJobResponseTypeDef](#describeclassificationjobresponsetypedef)
  - [DescribeOrganizationConfigurationResponseTypeDef](#describeorganizationconfigurationresponsetypedef)
  - [FindingStatisticsSortCriteriaTypeDef](#findingstatisticssortcriteriatypedef)
  - [GetAdministratorAccountResponseTypeDef](#getadministratoraccountresponsetypedef)
  - [GetBucketStatisticsResponseTypeDef](#getbucketstatisticsresponsetypedef)
  - [GetClassificationExportConfigurationResponseTypeDef](#getclassificationexportconfigurationresponsetypedef)
  - [GetCustomDataIdentifierResponseTypeDef](#getcustomdataidentifierresponsetypedef)
  - [GetFindingStatisticsResponseTypeDef](#getfindingstatisticsresponsetypedef)
  - [GetFindingsFilterResponseTypeDef](#getfindingsfilterresponsetypedef)
  - [GetFindingsPublicationConfigurationResponseTypeDef](#getfindingspublicationconfigurationresponsetypedef)
  - [GetFindingsResponseTypeDef](#getfindingsresponsetypedef)
  - [GetInvitationsCountResponseTypeDef](#getinvitationscountresponsetypedef)
  - [GetMacieSessionResponseTypeDef](#getmaciesessionresponsetypedef)
  - [GetMasterAccountResponseTypeDef](#getmasteraccountresponsetypedef)
  - [GetMemberResponseTypeDef](#getmemberresponsetypedef)
  - [GetUsageStatisticsResponseTypeDef](#getusagestatisticsresponsetypedef)
  - [GetUsageTotalsResponseTypeDef](#getusagetotalsresponsetypedef)
  - [ListClassificationJobsResponseTypeDef](#listclassificationjobsresponsetypedef)
  - [ListCustomDataIdentifiersResponseTypeDef](#listcustomdataidentifiersresponsetypedef)
  - [ListFindingsFiltersResponseTypeDef](#listfindingsfiltersresponsetypedef)
  - [ListFindingsResponseTypeDef](#listfindingsresponsetypedef)
  - [ListInvitationsResponseTypeDef](#listinvitationsresponsetypedef)
  - [ListJobsFilterCriteriaTypeDef](#listjobsfiltercriteriatypedef)
  - [ListJobsSortCriteriaTypeDef](#listjobssortcriteriatypedef)
  - [ListMembersResponseTypeDef](#listmembersresponsetypedef)
  - [ListOrganizationAdminAccountsResponseTypeDef](#listorganizationadminaccountsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutClassificationExportConfigurationResponseTypeDef](#putclassificationexportconfigurationresponsetypedef)
  - [SortCriteriaTypeDef](#sortcriteriatypedef)
  - [TestCustomDataIdentifierResponseTypeDef](#testcustomdataidentifierresponsetypedef)
  - [UpdateFindingsFilterResponseTypeDef](#updatefindingsfilterresponsetypedef)
  - [UsageStatisticsFilterTypeDef](#usagestatisticsfiltertypedef)
  - [UsageStatisticsSortByTypeDef](#usagestatisticssortbytypedef)

## AccessControlListTypeDef

```python
from mypy_boto3_macie2.type_defs import AccessControlListTypeDef
```




Optional fields:
- `allowsPublicReadAccess`: `bool`
- `allowsPublicWriteAccess`: `bool`


## AccountLevelPermissionsTypeDef

```python
from mypy_boto3_macie2.type_defs import AccountLevelPermissionsTypeDef
```




Optional fields:
- `blockPublicAccess`: `"BlockPublicAccessTypeDef"`


## AdminAccountTypeDef

```python
from mypy_boto3_macie2.type_defs import AdminAccountTypeDef
```




Optional fields:
- `accountId`: `str`
- `status`: `AdminStatus`


## ApiCallDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import ApiCallDetailsTypeDef
```




Optional fields:
- `api`: `str`
- `apiServiceName`: `str`
- `firstSeen`: `datetime`
- `lastSeen`: `datetime`


## AssumedRoleTypeDef

```python
from mypy_boto3_macie2.type_defs import AssumedRoleTypeDef
```




Optional fields:
- `accessKeyId`: `str`
- `accountId`: `str`
- `arn`: `str`
- `principalId`: `str`
- `sessionContext`: `"SessionContextTypeDef"`


## AwsAccountTypeDef

```python
from mypy_boto3_macie2.type_defs import AwsAccountTypeDef
```




Optional fields:
- `accountId`: `str`
- `principalId`: `str`


## AwsServiceTypeDef

```python
from mypy_boto3_macie2.type_defs import AwsServiceTypeDef
```




Optional fields:
- `invokedBy`: `str`


## BatchGetCustomDataIdentifierSummaryTypeDef

```python
from mypy_boto3_macie2.type_defs import BatchGetCustomDataIdentifierSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `deleted`: `bool`
- `description`: `str`
- `id`: `str`
- `name`: `str`


## BlockPublicAccessTypeDef

```python
from mypy_boto3_macie2.type_defs import BlockPublicAccessTypeDef
```




Optional fields:
- `blockPublicAcls`: `bool`
- `blockPublicPolicy`: `bool`
- `ignorePublicAcls`: `bool`
- `restrictPublicBuckets`: `bool`


## BucketCountByEffectivePermissionTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketCountByEffectivePermissionTypeDef
```




Optional fields:
- `publiclyAccessible`: `int`
- `publiclyReadable`: `int`
- `publiclyWritable`: `int`
- `unknown`: `int`


## BucketCountByEncryptionTypeTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketCountByEncryptionTypeTypeDef
```




Optional fields:
- `kmsManaged`: `int`
- `s3Managed`: `int`
- `unencrypted`: `int`
- `unknown`: `int`


## BucketCountBySharedAccessTypeTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketCountBySharedAccessTypeTypeDef
```




Optional fields:
- `external`: `int`
- `internal`: `int`
- `notShared`: `int`
- `unknown`: `int`


## BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef
```




Optional fields:
- `allowsUnencryptedObjectUploads`: `int`
- `deniesUnencryptedObjectUploads`: `int`
- `unknown`: `int`


## BucketLevelPermissionsTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketLevelPermissionsTypeDef
```




Optional fields:
- `accessControlList`: `"AccessControlListTypeDef"`
- `blockPublicAccess`: `"BlockPublicAccessTypeDef"`
- `bucketPolicy`: `"BucketPolicyTypeDef"`


## BucketMetadataTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketMetadataTypeDef
```




Optional fields:
- `accountId`: `str`
- `allowsUnencryptedObjectUploads`: `AllowsUnencryptedObjectUploads`
- `bucketArn`: `str`
- `bucketCreatedAt`: `datetime`
- `bucketName`: `str`
- `classifiableObjectCount`: `int`
- `classifiableSizeInBytes`: `int`
- `jobDetails`: `"JobDetailsTypeDef"`
- `lastUpdated`: `datetime`
- `objectCount`: `int`
- `objectCountByEncryptionType`: `"ObjectCountByEncryptionTypeTypeDef"`
- `publicAccess`: `"BucketPublicAccessTypeDef"`
- `region`: `str`
- `replicationDetails`: `"ReplicationDetailsTypeDef"`
- `serverSideEncryption`: `"BucketServerSideEncryptionTypeDef"`
- `sharedAccess`: `SharedAccess`
- `sizeInBytes`: `int`
- `sizeInBytesCompressed`: `int`
- `tags`: `List["KeyValuePairTypeDef"]`
- `unclassifiableObjectCount`: `"ObjectLevelStatisticsTypeDef"`
- `unclassifiableObjectSizeInBytes`: `"ObjectLevelStatisticsTypeDef"`
- `versioning`: `bool`


## BucketPermissionConfigurationTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketPermissionConfigurationTypeDef
```




Optional fields:
- `accountLevelPermissions`: `"AccountLevelPermissionsTypeDef"`
- `bucketLevelPermissions`: `"BucketLevelPermissionsTypeDef"`


## BucketPolicyTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketPolicyTypeDef
```




Optional fields:
- `allowsPublicReadAccess`: `bool`
- `allowsPublicWriteAccess`: `bool`


## BucketPublicAccessTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketPublicAccessTypeDef
```




Optional fields:
- `effectivePermission`: `EffectivePermission`
- `permissionConfiguration`: `"BucketPermissionConfigurationTypeDef"`


## BucketServerSideEncryptionTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketServerSideEncryptionTypeDef
```




Optional fields:
- `kmsMasterKeyId`: `str`
- `type`: `TypeType`


## CellTypeDef

```python
from mypy_boto3_macie2.type_defs import CellTypeDef
```




Optional fields:
- `cellReference`: `str`
- `column`: `int`
- `columnName`: `str`
- `row`: `int`


## ClassificationDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import ClassificationDetailsTypeDef
```




Optional fields:
- `detailedResultsLocation`: `str`
- `jobArn`: `str`
- `jobId`: `str`
- `result`: `"ClassificationResultTypeDef"`


## ClassificationExportConfigurationTypeDef

```python
from mypy_boto3_macie2.type_defs import ClassificationExportConfigurationTypeDef
```




Optional fields:
- `s3Destination`: `"S3DestinationTypeDef"`


## ClassificationResultStatusTypeDef

```python
from mypy_boto3_macie2.type_defs import ClassificationResultStatusTypeDef
```




Optional fields:
- `code`: `str`
- `reason`: `str`


## ClassificationResultTypeDef

```python
from mypy_boto3_macie2.type_defs import ClassificationResultTypeDef
```




Optional fields:
- `additionalOccurrences`: `bool`
- `customDataIdentifiers`: `"CustomDataIdentifiersTypeDef"`
- `mimeType`: `str`
- `sensitiveData`: `List["SensitiveDataItemTypeDef"]`
- `sizeClassified`: `int`
- `status`: `"ClassificationResultStatusTypeDef"`


## CriterionAdditionalPropertiesTypeDef

```python
from mypy_boto3_macie2.type_defs import CriterionAdditionalPropertiesTypeDef
```




Optional fields:
- `eq`: `List[str]`
- `eqExactMatch`: `List[str]`
- `gt`: `int`
- `gte`: `int`
- `lt`: `int`
- `lte`: `int`
- `neq`: `List[str]`


## CustomDataIdentifierSummaryTypeDef

```python
from mypy_boto3_macie2.type_defs import CustomDataIdentifierSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `description`: `str`
- `id`: `str`
- `name`: `str`


## CustomDataIdentifiersTypeDef

```python
from mypy_boto3_macie2.type_defs import CustomDataIdentifiersTypeDef
```




Optional fields:
- `detections`: `List["CustomDetectionTypeDef"]`
- `totalCount`: `int`


## CustomDetectionTypeDef

```python
from mypy_boto3_macie2.type_defs import CustomDetectionTypeDef
```




Optional fields:
- `arn`: `str`
- `count`: `int`
- `name`: `str`
- `occurrences`: `"OccurrencesTypeDef"`


## DefaultDetectionTypeDef

```python
from mypy_boto3_macie2.type_defs import DefaultDetectionTypeDef
```




Optional fields:
- `count`: `int`
- `occurrences`: `"OccurrencesTypeDef"`
- `type`: `str`


## DomainDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import DomainDetailsTypeDef
```




Optional fields:
- `domainName`: `str`


## FederatedUserTypeDef

```python
from mypy_boto3_macie2.type_defs import FederatedUserTypeDef
```




Optional fields:
- `accessKeyId`: `str`
- `accountId`: `str`
- `arn`: `str`
- `principalId`: `str`
- `sessionContext`: `"SessionContextTypeDef"`


## FindingActionTypeDef

```python
from mypy_boto3_macie2.type_defs import FindingActionTypeDef
```




Optional fields:
- `actionType`: `FindingActionType`
- `apiCallDetails`: `"ApiCallDetailsTypeDef"`


## FindingActorTypeDef

```python
from mypy_boto3_macie2.type_defs import FindingActorTypeDef
```




Optional fields:
- `domainDetails`: `"DomainDetailsTypeDef"`
- `ipAddressDetails`: `"IpAddressDetailsTypeDef"`
- `userIdentity`: `"UserIdentityTypeDef"`


## FindingCriteriaTypeDef

```python
from mypy_boto3_macie2.type_defs import FindingCriteriaTypeDef
```




Optional fields:
- `criterion`: `Dict[str, "CriterionAdditionalPropertiesTypeDef"]`


## FindingTypeDef

```python
from mypy_boto3_macie2.type_defs import FindingTypeDef
```




Optional fields:
- `accountId`: `str`
- `archived`: `bool`
- `category`: `FindingCategory`
- `classificationDetails`: `"ClassificationDetailsTypeDef"`
- `count`: `int`
- `createdAt`: `datetime`
- `description`: `str`
- `id`: `str`
- `partition`: `str`
- `policyDetails`: `"PolicyDetailsTypeDef"`
- `region`: `str`
- `resourcesAffected`: `"ResourcesAffectedTypeDef"`
- `sample`: `bool`
- `schemaVersion`: `str`
- `severity`: `"SeverityTypeDef"`
- `title`: `str`
- `type`: `FindingType`
- `updatedAt`: `datetime`


## FindingsFilterListItemTypeDef

```python
from mypy_boto3_macie2.type_defs import FindingsFilterListItemTypeDef
```




Optional fields:
- `action`: `FindingsFilterAction`
- `arn`: `str`
- `id`: `str`
- `name`: `str`
- `tags`: `Dict[str, str]`


## GroupCountTypeDef

```python
from mypy_boto3_macie2.type_defs import GroupCountTypeDef
```




Optional fields:
- `count`: `int`
- `groupKey`: `str`


## IamUserTypeDef

```python
from mypy_boto3_macie2.type_defs import IamUserTypeDef
```




Optional fields:
- `accountId`: `str`
- `arn`: `str`
- `principalId`: `str`
- `userName`: `str`


## InvitationTypeDef

```python
from mypy_boto3_macie2.type_defs import InvitationTypeDef
```




Optional fields:
- `accountId`: `str`
- `invitationId`: `str`
- `invitedAt`: `datetime`
- `relationshipStatus`: `RelationshipStatus`


## IpAddressDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import IpAddressDetailsTypeDef
```




Optional fields:
- `ipAddressV4`: `str`
- `ipCity`: `"IpCityTypeDef"`
- `ipCountry`: `"IpCountryTypeDef"`
- `ipGeoLocation`: `"IpGeoLocationTypeDef"`
- `ipOwner`: `"IpOwnerTypeDef"`


## IpCityTypeDef

```python
from mypy_boto3_macie2.type_defs import IpCityTypeDef
```




Optional fields:
- `name`: `str`


## IpCountryTypeDef

```python
from mypy_boto3_macie2.type_defs import IpCountryTypeDef
```




Optional fields:
- `code`: `str`
- `name`: `str`


## IpGeoLocationTypeDef

```python
from mypy_boto3_macie2.type_defs import IpGeoLocationTypeDef
```




Optional fields:
- `lat`: `float`
- `lon`: `float`


## IpOwnerTypeDef

```python
from mypy_boto3_macie2.type_defs import IpOwnerTypeDef
```




Optional fields:
- `asn`: `str`
- `asnOrg`: `str`
- `isp`: `str`
- `org`: `str`


## JobDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import JobDetailsTypeDef
```




Optional fields:
- `isDefinedInJob`: `IsDefinedInJob`
- `isMonitoredByJob`: `IsMonitoredByJob`
- `lastJobId`: `str`
- `lastJobRunTime`: `datetime`


## JobScheduleFrequencyTypeDef

```python
from mypy_boto3_macie2.type_defs import JobScheduleFrequencyTypeDef
```




Optional fields:
- `dailySchedule`: `Dict[str, Any]`
- `monthlySchedule`: `"MonthlyScheduleTypeDef"`
- `weeklySchedule`: `"WeeklyScheduleTypeDef"`


## JobScopeTermTypeDef

```python
from mypy_boto3_macie2.type_defs import JobScopeTermTypeDef
```




Optional fields:
- `simpleScopeTerm`: `"SimpleScopeTermTypeDef"`
- `tagScopeTerm`: `"TagScopeTermTypeDef"`


## JobScopingBlockTypeDef

```python
from mypy_boto3_macie2.type_defs import JobScopingBlockTypeDef
```




Optional fields:
- `and`: `List["JobScopeTermTypeDef"]`


## JobSummaryTypeDef

```python
from mypy_boto3_macie2.type_defs import JobSummaryTypeDef
```




Optional fields:
- `bucketDefinitions`: `List["S3BucketDefinitionForJobTypeDef"]`
- `createdAt`: `datetime`
- `jobId`: `str`
- `jobStatus`: `JobStatus`
- `jobType`: `JobType`
- `lastRunErrorStatus`: `"LastRunErrorStatusTypeDef"`
- `name`: `str`
- `userPausedDetails`: `"UserPausedDetailsTypeDef"`


## KeyValuePairTypeDef

```python
from mypy_boto3_macie2.type_defs import KeyValuePairTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## LastRunErrorStatusTypeDef

```python
from mypy_boto3_macie2.type_defs import LastRunErrorStatusTypeDef
```




Optional fields:
- `code`: `LastRunErrorStatusCode`


## ListJobsFilterTermTypeDef

```python
from mypy_boto3_macie2.type_defs import ListJobsFilterTermTypeDef
```




Optional fields:
- `comparator`: `JobComparator`
- `key`: `ListJobsFilterKey`
- `values`: `List[str]`


## MemberTypeDef

```python
from mypy_boto3_macie2.type_defs import MemberTypeDef
```




Optional fields:
- `accountId`: `str`
- `administratorAccountId`: `str`
- `arn`: `str`
- `email`: `str`
- `invitedAt`: `datetime`
- `masterAccountId`: `str`
- `relationshipStatus`: `RelationshipStatus`
- `tags`: `Dict[str, str]`
- `updatedAt`: `datetime`


## MonthlyScheduleTypeDef

```python
from mypy_boto3_macie2.type_defs import MonthlyScheduleTypeDef
```




Optional fields:
- `dayOfMonth`: `int`


## ObjectCountByEncryptionTypeTypeDef

```python
from mypy_boto3_macie2.type_defs import ObjectCountByEncryptionTypeTypeDef
```




Optional fields:
- `customerManaged`: `int`
- `kmsManaged`: `int`
- `s3Managed`: `int`
- `unencrypted`: `int`
- `unknown`: `int`


## ObjectLevelStatisticsTypeDef

```python
from mypy_boto3_macie2.type_defs import ObjectLevelStatisticsTypeDef
```




Optional fields:
- `fileType`: `int`
- `storageClass`: `int`
- `total`: `int`


## OccurrencesTypeDef

```python
from mypy_boto3_macie2.type_defs import OccurrencesTypeDef
```




Optional fields:
- `cells`: `List["CellTypeDef"]`
- `lineRanges`: `List["RangeTypeDef"]`
- `offsetRanges`: `List["RangeTypeDef"]`
- `pages`: `List["PageTypeDef"]`
- `records`: `List["RecordTypeDef"]`


## PageTypeDef

```python
from mypy_boto3_macie2.type_defs import PageTypeDef
```




Optional fields:
- `lineRange`: `"RangeTypeDef"`
- `offsetRange`: `"RangeTypeDef"`
- `pageNumber`: `int`


## PolicyDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import PolicyDetailsTypeDef
```




Optional fields:
- `action`: `"FindingActionTypeDef"`
- `actor`: `"FindingActorTypeDef"`


## RangeTypeDef

```python
from mypy_boto3_macie2.type_defs import RangeTypeDef
```




Optional fields:
- `end`: `int`
- `start`: `int`
- `startColumn`: `int`


## RecordTypeDef

```python
from mypy_boto3_macie2.type_defs import RecordTypeDef
```




Optional fields:
- `jsonPath`: `str`
- `recordIndex`: `int`


## ReplicationDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import ReplicationDetailsTypeDef
```




Optional fields:
- `replicated`: `bool`
- `replicatedExternally`: `bool`
- `replicationAccounts`: `List[str]`


## ResourcesAffectedTypeDef

```python
from mypy_boto3_macie2.type_defs import ResourcesAffectedTypeDef
```




Optional fields:
- `s3Bucket`: `"S3BucketTypeDef"`
- `s3Object`: `"S3ObjectTypeDef"`


## S3BucketDefinitionForJobTypeDef

```python
from mypy_boto3_macie2.type_defs import S3BucketDefinitionForJobTypeDef
```


Required fields:
- `accountId`: `str`
- `buckets`: `List[str]`




## S3BucketOwnerTypeDef

```python
from mypy_boto3_macie2.type_defs import S3BucketOwnerTypeDef
```




Optional fields:
- `displayName`: `str`
- `id`: `str`


## S3BucketTypeDef

```python
from mypy_boto3_macie2.type_defs import S3BucketTypeDef
```




Optional fields:
- `allowsUnencryptedObjectUploads`: `AllowsUnencryptedObjectUploads`
- `arn`: `str`
- `createdAt`: `datetime`
- `defaultServerSideEncryption`: `"ServerSideEncryptionTypeDef"`
- `name`: `str`
- `owner`: `"S3BucketOwnerTypeDef"`
- `publicAccess`: `"BucketPublicAccessTypeDef"`
- `tags`: `List["KeyValuePairTypeDef"]`


## S3DestinationTypeDef

```python
from mypy_boto3_macie2.type_defs import S3DestinationTypeDef
```


Required fields:
- `bucketName`: `str`
- `kmsKeyArn`: `str`



Optional fields:
- `keyPrefix`: `str`


## S3JobDefinitionTypeDef

```python
from mypy_boto3_macie2.type_defs import S3JobDefinitionTypeDef
```




Optional fields:
- `bucketDefinitions`: `List["S3BucketDefinitionForJobTypeDef"]`
- `scoping`: `"ScopingTypeDef"`


## S3ObjectTypeDef

```python
from mypy_boto3_macie2.type_defs import S3ObjectTypeDef
```




Optional fields:
- `bucketArn`: `str`
- `eTag`: `str`
- `extension`: `str`
- `key`: `str`
- `lastModified`: `datetime`
- `path`: `str`
- `publicAccess`: `bool`
- `serverSideEncryption`: `"ServerSideEncryptionTypeDef"`
- `size`: `int`
- `storageClass`: `StorageClass`
- `tags`: `List["KeyValuePairTypeDef"]`
- `versionId`: `str`


## ScopingTypeDef

```python
from mypy_boto3_macie2.type_defs import ScopingTypeDef
```




Optional fields:
- `excludes`: `"JobScopingBlockTypeDef"`
- `includes`: `"JobScopingBlockTypeDef"`


## SecurityHubConfigurationTypeDef

```python
from mypy_boto3_macie2.type_defs import SecurityHubConfigurationTypeDef
```


Required fields:
- `publishClassificationFindings`: `bool`
- `publishPolicyFindings`: `bool`




## SensitiveDataItemTypeDef

```python
from mypy_boto3_macie2.type_defs import SensitiveDataItemTypeDef
```




Optional fields:
- `category`: `SensitiveDataItemCategory`
- `detections`: `List["DefaultDetectionTypeDef"]`
- `totalCount`: `int`


## ServerSideEncryptionTypeDef

```python
from mypy_boto3_macie2.type_defs import ServerSideEncryptionTypeDef
```




Optional fields:
- `encryptionType`: `EncryptionType`
- `kmsMasterKeyId`: `str`


## ServiceLimitTypeDef

```python
from mypy_boto3_macie2.type_defs import ServiceLimitTypeDef
```




Optional fields:
- `isServiceLimited`: `bool`
- `unit`: `Unit`
- `value`: `int`


## SessionContextAttributesTypeDef

```python
from mypy_boto3_macie2.type_defs import SessionContextAttributesTypeDef
```




Optional fields:
- `creationDate`: `datetime`
- `mfaAuthenticated`: `bool`


## SessionContextTypeDef

```python
from mypy_boto3_macie2.type_defs import SessionContextTypeDef
```




Optional fields:
- `attributes`: `"SessionContextAttributesTypeDef"`
- `sessionIssuer`: `"SessionIssuerTypeDef"`


## SessionIssuerTypeDef

```python
from mypy_boto3_macie2.type_defs import SessionIssuerTypeDef
```




Optional fields:
- `accountId`: `str`
- `arn`: `str`
- `principalId`: `str`
- `type`: `str`
- `userName`: `str`


## SeverityTypeDef

```python
from mypy_boto3_macie2.type_defs import SeverityTypeDef
```




Optional fields:
- `description`: `SeverityDescription`
- `score`: `int`


## SimpleScopeTermTypeDef

```python
from mypy_boto3_macie2.type_defs import SimpleScopeTermTypeDef
```




Optional fields:
- `comparator`: `JobComparator`
- `key`: `ScopeFilterKey`
- `values`: `List[str]`


## StatisticsTypeDef

```python
from mypy_boto3_macie2.type_defs import StatisticsTypeDef
```




Optional fields:
- `approximateNumberOfObjectsToProcess`: `float`
- `numberOfRuns`: `float`


## TagScopeTermTypeDef

```python
from mypy_boto3_macie2.type_defs import TagScopeTermTypeDef
```




Optional fields:
- `comparator`: `JobComparator`
- `key`: `str`
- `tagValues`: `List["TagValuePairTypeDef"]`
- `target`: `TagTarget`


## TagValuePairTypeDef

```python
from mypy_boto3_macie2.type_defs import TagValuePairTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## UnprocessedAccountTypeDef

```python
from mypy_boto3_macie2.type_defs import UnprocessedAccountTypeDef
```




Optional fields:
- `accountId`: `str`
- `errorCode`: `ErrorCode`
- `errorMessage`: `str`


## UsageByAccountTypeDef

```python
from mypy_boto3_macie2.type_defs import UsageByAccountTypeDef
```




Optional fields:
- `currency`: `Currency`
- `estimatedCost`: `str`
- `serviceLimit`: `"ServiceLimitTypeDef"`
- `type`: `UsageType`


## UsageRecordTypeDef

```python
from mypy_boto3_macie2.type_defs import UsageRecordTypeDef
```




Optional fields:
- `accountId`: `str`
- `freeTrialStartDate`: `datetime`
- `usage`: `List["UsageByAccountTypeDef"]`


## UsageTotalTypeDef

```python
from mypy_boto3_macie2.type_defs import UsageTotalTypeDef
```




Optional fields:
- `currency`: `Currency`
- `estimatedCost`: `str`
- `type`: `UsageType`


## UserIdentityRootTypeDef

```python
from mypy_boto3_macie2.type_defs import UserIdentityRootTypeDef
```




Optional fields:
- `accountId`: `str`
- `arn`: `str`
- `principalId`: `str`


## UserIdentityTypeDef

```python
from mypy_boto3_macie2.type_defs import UserIdentityTypeDef
```




Optional fields:
- `assumedRole`: `"AssumedRoleTypeDef"`
- `awsAccount`: `"AwsAccountTypeDef"`
- `awsService`: `"AwsServiceTypeDef"`
- `federatedUser`: `"FederatedUserTypeDef"`
- `iamUser`: `"IamUserTypeDef"`
- `root`: `"UserIdentityRootTypeDef"`
- `type`: `UserIdentityType`


## UserPausedDetailsTypeDef

```python
from mypy_boto3_macie2.type_defs import UserPausedDetailsTypeDef
```




Optional fields:
- `jobExpiresAt`: `datetime`
- `jobImminentExpirationHealthEventArn`: `str`
- `jobPausedAt`: `datetime`


## WeeklyScheduleTypeDef

```python
from mypy_boto3_macie2.type_defs import WeeklyScheduleTypeDef
```




Optional fields:
- `dayOfWeek`: `DayOfWeek`


## AccountDetailTypeDef

```python
from mypy_boto3_macie2.type_defs import AccountDetailTypeDef
```


Required fields:
- `accountId`: `str`
- `email`: `str`




## BatchGetCustomDataIdentifiersResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import BatchGetCustomDataIdentifiersResponseTypeDef
```




Optional fields:
- `customDataIdentifiers`: `List["BatchGetCustomDataIdentifierSummaryTypeDef"]`
- `notFoundIdentifierIds`: `List[str]`


## BucketCriteriaAdditionalPropertiesTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketCriteriaAdditionalPropertiesTypeDef
```




Optional fields:
- `eq`: `List[str]`
- `gt`: `int`
- `gte`: `int`
- `lt`: `int`
- `lte`: `int`
- `neq`: `List[str]`
- `prefix`: `str`


## BucketSortCriteriaTypeDef

```python
from mypy_boto3_macie2.type_defs import BucketSortCriteriaTypeDef
```




Optional fields:
- `attributeName`: `str`
- `orderBy`: `OrderBy`


## CreateClassificationJobResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import CreateClassificationJobResponseTypeDef
```




Optional fields:
- `jobArn`: `str`
- `jobId`: `str`


## CreateCustomDataIdentifierResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import CreateCustomDataIdentifierResponseTypeDef
```




Optional fields:
- `customDataIdentifierId`: `str`


## CreateFindingsFilterResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import CreateFindingsFilterResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `id`: `str`


## CreateInvitationsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import CreateInvitationsResponseTypeDef
```




Optional fields:
- `unprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`


## CreateMemberResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import CreateMemberResponseTypeDef
```




Optional fields:
- `arn`: `str`


## DeclineInvitationsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import DeclineInvitationsResponseTypeDef
```




Optional fields:
- `unprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`


## DeleteInvitationsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import DeleteInvitationsResponseTypeDef
```




Optional fields:
- `unprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`


## DescribeBucketsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import DescribeBucketsResponseTypeDef
```




Optional fields:
- `buckets`: `List["BucketMetadataTypeDef"]`
- `nextToken`: `str`


## DescribeClassificationJobResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import DescribeClassificationJobResponseTypeDef
```




Optional fields:
- `clientToken`: `str`
- `createdAt`: `datetime`
- `customDataIdentifierIds`: `List[str]`
- `description`: `str`
- `initialRun`: `bool`
- `jobArn`: `str`
- `jobId`: `str`
- `jobStatus`: `JobStatus`
- `jobType`: `JobType`
- `lastRunErrorStatus`: `"LastRunErrorStatusTypeDef"`
- `lastRunTime`: `datetime`
- `name`: `str`
- `s3JobDefinition`: `"S3JobDefinitionTypeDef"`
- `samplingPercentage`: `int`
- `scheduleFrequency`: `"JobScheduleFrequencyTypeDef"`
- `statistics`: `"StatisticsTypeDef"`
- `tags`: `Dict[str, str]`
- `userPausedDetails`: `"UserPausedDetailsTypeDef"`


## DescribeOrganizationConfigurationResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import DescribeOrganizationConfigurationResponseTypeDef
```




Optional fields:
- `autoEnable`: `bool`
- `maxAccountLimitReached`: `bool`


## FindingStatisticsSortCriteriaTypeDef

```python
from mypy_boto3_macie2.type_defs import FindingStatisticsSortCriteriaTypeDef
```




Optional fields:
- `attributeName`: `FindingStatisticsSortAttributeName`
- `orderBy`: `OrderBy`


## GetAdministratorAccountResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetAdministratorAccountResponseTypeDef
```




Optional fields:
- `administrator`: `"InvitationTypeDef"`


## GetBucketStatisticsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetBucketStatisticsResponseTypeDef
```




Optional fields:
- `bucketCount`: `int`
- `bucketCountByEffectivePermission`: `"BucketCountByEffectivePermissionTypeDef"`
- `bucketCountByEncryptionType`: `"BucketCountByEncryptionTypeTypeDef"`
- `bucketCountByObjectEncryptionRequirement`: `"BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef"`
- `bucketCountBySharedAccessType`: `"BucketCountBySharedAccessTypeTypeDef"`
- `classifiableObjectCount`: `int`
- `classifiableSizeInBytes`: `int`
- `lastUpdated`: `datetime`
- `objectCount`: `int`
- `sizeInBytes`: `int`
- `sizeInBytesCompressed`: `int`
- `unclassifiableObjectCount`: `"ObjectLevelStatisticsTypeDef"`
- `unclassifiableObjectSizeInBytes`: `"ObjectLevelStatisticsTypeDef"`


## GetClassificationExportConfigurationResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetClassificationExportConfigurationResponseTypeDef
```




Optional fields:
- `configuration`: `"ClassificationExportConfigurationTypeDef"`


## GetCustomDataIdentifierResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetCustomDataIdentifierResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `deleted`: `bool`
- `description`: `str`
- `id`: `str`
- `ignoreWords`: `List[str]`
- `keywords`: `List[str]`
- `maximumMatchDistance`: `int`
- `name`: `str`
- `regex`: `str`
- `tags`: `Dict[str, str]`


## GetFindingStatisticsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetFindingStatisticsResponseTypeDef
```




Optional fields:
- `countsByGroup`: `List["GroupCountTypeDef"]`


## GetFindingsFilterResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetFindingsFilterResponseTypeDef
```




Optional fields:
- `action`: `FindingsFilterAction`
- `arn`: `str`
- `description`: `str`
- `findingCriteria`: `"FindingCriteriaTypeDef"`
- `id`: `str`
- `name`: `str`
- `position`: `int`
- `tags`: `Dict[str, str]`


## GetFindingsPublicationConfigurationResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetFindingsPublicationConfigurationResponseTypeDef
```




Optional fields:
- `securityHubConfiguration`: `"SecurityHubConfigurationTypeDef"`


## GetFindingsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetFindingsResponseTypeDef
```




Optional fields:
- `findings`: `List["FindingTypeDef"]`


## GetInvitationsCountResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetInvitationsCountResponseTypeDef
```




Optional fields:
- `invitationsCount`: `int`


## GetMacieSessionResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetMacieSessionResponseTypeDef
```




Optional fields:
- `createdAt`: `datetime`
- `findingPublishingFrequency`: `FindingPublishingFrequency`
- `serviceRole`: `str`
- `status`: `MacieStatus`
- `updatedAt`: `datetime`


## GetMasterAccountResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetMasterAccountResponseTypeDef
```




Optional fields:
- `master`: `"InvitationTypeDef"`


## GetMemberResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetMemberResponseTypeDef
```




Optional fields:
- `accountId`: `str`
- `administratorAccountId`: `str`
- `arn`: `str`
- `email`: `str`
- `invitedAt`: `datetime`
- `masterAccountId`: `str`
- `relationshipStatus`: `RelationshipStatus`
- `tags`: `Dict[str, str]`
- `updatedAt`: `datetime`


## GetUsageStatisticsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetUsageStatisticsResponseTypeDef
```




Optional fields:
- `nextToken`: `str`
- `records`: `List["UsageRecordTypeDef"]`
- `timeRange`: `TimeRange`


## GetUsageTotalsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import GetUsageTotalsResponseTypeDef
```




Optional fields:
- `timeRange`: `TimeRange`
- `usageTotals`: `List["UsageTotalTypeDef"]`


## ListClassificationJobsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListClassificationJobsResponseTypeDef
```




Optional fields:
- `items`: `List["JobSummaryTypeDef"]`
- `nextToken`: `str`


## ListCustomDataIdentifiersResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListCustomDataIdentifiersResponseTypeDef
```




Optional fields:
- `items`: `List["CustomDataIdentifierSummaryTypeDef"]`
- `nextToken`: `str`


## ListFindingsFiltersResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListFindingsFiltersResponseTypeDef
```




Optional fields:
- `findingsFilterListItems`: `List["FindingsFilterListItemTypeDef"]`
- `nextToken`: `str`


## ListFindingsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListFindingsResponseTypeDef
```




Optional fields:
- `findingIds`: `List[str]`
- `nextToken`: `str`


## ListInvitationsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListInvitationsResponseTypeDef
```




Optional fields:
- `invitations`: `List["InvitationTypeDef"]`
- `nextToken`: `str`


## ListJobsFilterCriteriaTypeDef

```python
from mypy_boto3_macie2.type_defs import ListJobsFilterCriteriaTypeDef
```




Optional fields:
- `excludes`: `List["ListJobsFilterTermTypeDef"]`
- `includes`: `List["ListJobsFilterTermTypeDef"]`


## ListJobsSortCriteriaTypeDef

```python
from mypy_boto3_macie2.type_defs import ListJobsSortCriteriaTypeDef
```




Optional fields:
- `attributeName`: `ListJobsSortAttributeName`
- `orderBy`: `OrderBy`


## ListMembersResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListMembersResponseTypeDef
```




Optional fields:
- `members`: `List["MemberTypeDef"]`
- `nextToken`: `str`


## ListOrganizationAdminAccountsResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListOrganizationAdminAccountsResponseTypeDef
```




Optional fields:
- `adminAccounts`: `List["AdminAccountTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_macie2.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutClassificationExportConfigurationResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import PutClassificationExportConfigurationResponseTypeDef
```




Optional fields:
- `configuration`: `"ClassificationExportConfigurationTypeDef"`


## SortCriteriaTypeDef

```python
from mypy_boto3_macie2.type_defs import SortCriteriaTypeDef
```




Optional fields:
- `attributeName`: `str`
- `orderBy`: `OrderBy`


## TestCustomDataIdentifierResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import TestCustomDataIdentifierResponseTypeDef
```




Optional fields:
- `matchCount`: `int`


## UpdateFindingsFilterResponseTypeDef

```python
from mypy_boto3_macie2.type_defs import UpdateFindingsFilterResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `id`: `str`


## UsageStatisticsFilterTypeDef

```python
from mypy_boto3_macie2.type_defs import UsageStatisticsFilterTypeDef
```




Optional fields:
- `comparator`: `UsageStatisticsFilterComparator`
- `key`: `UsageStatisticsFilterKey`
- `values`: `List[str]`


## UsageStatisticsSortByTypeDef

```python
from mypy_boto3_macie2.type_defs import UsageStatisticsSortByTypeDef
```




Optional fields:
- `key`: `UsageStatisticsSortKey`
- `orderBy`: `OrderBy`

