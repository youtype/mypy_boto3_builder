# Type annotations for boto3 Macie2 module

> [Index](../index.md) > Macie2

Auto-generated documentation for [Macie2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2)
type annotations stubs module [mypy_boto3_macie2](https://pypi.org/project/mypy-boto3-macie2/).

```bash
pip install mypy-boto3-macie2
```

- [Type annotations for boto3 Macie2 module](#type-annotations-for-boto3-macie2-module)
  - [Macie2Client](#macie2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## Macie2Client

Type annotations for  `boto3.client("macie2")` as [Macie2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_macie2.client import Macie2Client
```


Macie2Client [exceptions](./client.md#exceptions)



### Methods
- [accept_invitation](./client.md#accept-invitation)
- [batch_get_custom_data_identifiers](./client.md#batch-get-custom-data-identifiers)
- [can_paginate](./client.md#can-paginate)
- [create_classification_job](./client.md#create-classification-job)
- [create_custom_data_identifier](./client.md#create-custom-data-identifier)
- [create_findings_filter](./client.md#create-findings-filter)
- [create_invitations](./client.md#create-invitations)
- [create_member](./client.md#create-member)
- [create_sample_findings](./client.md#create-sample-findings)
- [decline_invitations](./client.md#decline-invitations)
- [delete_custom_data_identifier](./client.md#delete-custom-data-identifier)
- [delete_findings_filter](./client.md#delete-findings-filter)
- [delete_invitations](./client.md#delete-invitations)
- [delete_member](./client.md#delete-member)
- [describe_buckets](./client.md#describe-buckets)
- [describe_classification_job](./client.md#describe-classification-job)
- [describe_organization_configuration](./client.md#describe-organization-configuration)
- [disable_macie](./client.md#disable-macie)
- [disable_organization_admin_account](./client.md#disable-organization-admin-account)
- [disassociate_from_administrator_account](./client.md#disassociate-from-administrator-account)
- [disassociate_from_master_account](./client.md#disassociate-from-master-account)
- [disassociate_member](./client.md#disassociate-member)
- [enable_macie](./client.md#enable-macie)
- [enable_organization_admin_account](./client.md#enable-organization-admin-account)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_administrator_account](./client.md#get-administrator-account)
- [get_bucket_statistics](./client.md#get-bucket-statistics)
- [get_classification_export_configuration](./client.md#get-classification-export-configuration)
- [get_custom_data_identifier](./client.md#get-custom-data-identifier)
- [get_finding_statistics](./client.md#get-finding-statistics)
- [get_findings](./client.md#get-findings)
- [get_findings_filter](./client.md#get-findings-filter)
- [get_findings_publication_configuration](./client.md#get-findings-publication-configuration)
- [get_invitations_count](./client.md#get-invitations-count)
- [get_macie_session](./client.md#get-macie-session)
- [get_master_account](./client.md#get-master-account)
- [get_member](./client.md#get-member)
- [get_paginator](./client.md#get-paginator)
- [get_usage_statistics](./client.md#get-usage-statistics)
- [get_usage_totals](./client.md#get-usage-totals)
- [list_classification_jobs](./client.md#list-classification-jobs)
- [list_custom_data_identifiers](./client.md#list-custom-data-identifiers)
- [list_findings](./client.md#list-findings)
- [list_findings_filters](./client.md#list-findings-filters)
- [list_invitations](./client.md#list-invitations)
- [list_members](./client.md#list-members)
- [list_organization_admin_accounts](./client.md#list-organization-admin-accounts)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_classification_export_configuration](./client.md#put-classification-export-configuration)
- [put_findings_publication_configuration](./client.md#put-findings-publication-configuration)
- [tag_resource](./client.md#tag-resource)
- [test_custom_data_identifier](./client.md#test-custom-data-identifier)
- [untag_resource](./client.md#untag-resource)
- [update_classification_job](./client.md#update-classification-job)
- [update_findings_filter](./client.md#update-findings-filter)
- [update_macie_session](./client.md#update-macie-session)
- [update_member_session](./client.md#update-member-session)
- [update_organization_configuration](./client.md#update-organization-configuration)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("macie2").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_macie2.paginators import DescribeBucketsPaginator, ...
```

- [DescribeBucketsPaginator](./paginators.md#describebucketspaginator)
- [GetUsageStatisticsPaginator](./paginators.md#getusagestatisticspaginator)
- [ListClassificationJobsPaginator](./paginators.md#listclassificationjobspaginator)
- [ListCustomDataIdentifiersPaginator](./paginators.md#listcustomdataidentifierspaginator)
- [ListFindingsPaginator](./paginators.md#listfindingspaginator)
- [ListFindingsFiltersPaginator](./paginators.md#listfindingsfilterspaginator)
- [ListInvitationsPaginator](./paginators.md#listinvitationspaginator)
- [ListMembersPaginator](./paginators.md#listmemberspaginator)
- [ListOrganizationAdminAccountsPaginator](./paginators.md#listorganizationadminaccountspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_macie2.literals import AdminStatus, ...
```

- [AdminStatus](./literals.md#adminstatus)
- [AllowsUnencryptedObjectUploads](./literals.md#allowsunencryptedobjectuploads)
- [Currency](./literals.md#currency)
- [DayOfWeek](./literals.md#dayofweek)
- [DescribeBucketsPaginatorName](./literals.md#describebucketspaginatorname)
- [EffectivePermission](./literals.md#effectivepermission)
- [EncryptionType](./literals.md#encryptiontype)
- [ErrorCode](./literals.md#errorcode)
- [FindingActionType](./literals.md#findingactiontype)
- [FindingCategory](./literals.md#findingcategory)
- [FindingPublishingFrequency](./literals.md#findingpublishingfrequency)
- [FindingStatisticsSortAttributeName](./literals.md#findingstatisticssortattributename)
- [FindingType](./literals.md#findingtype)
- [FindingsFilterAction](./literals.md#findingsfilteraction)
- [GetUsageStatisticsPaginatorName](./literals.md#getusagestatisticspaginatorname)
- [GroupBy](./literals.md#groupby)
- [IsDefinedInJob](./literals.md#isdefinedinjob)
- [IsMonitoredByJob](./literals.md#ismonitoredbyjob)
- [JobComparator](./literals.md#jobcomparator)
- [JobStatus](./literals.md#jobstatus)
- [JobType](./literals.md#jobtype)
- [LastRunErrorStatusCode](./literals.md#lastrunerrorstatuscode)
- [ListClassificationJobsPaginatorName](./literals.md#listclassificationjobspaginatorname)
- [ListCustomDataIdentifiersPaginatorName](./literals.md#listcustomdataidentifierspaginatorname)
- [ListFindingsFiltersPaginatorName](./literals.md#listfindingsfilterspaginatorname)
- [ListFindingsPaginatorName](./literals.md#listfindingspaginatorname)
- [ListInvitationsPaginatorName](./literals.md#listinvitationspaginatorname)
- [ListJobsFilterKey](./literals.md#listjobsfilterkey)
- [ListJobsSortAttributeName](./literals.md#listjobssortattributename)
- [ListMembersPaginatorName](./literals.md#listmemberspaginatorname)
- [ListOrganizationAdminAccountsPaginatorName](./literals.md#listorganizationadminaccountspaginatorname)
- [MacieStatus](./literals.md#maciestatus)
- [OrderBy](./literals.md#orderby)
- [RelationshipStatus](./literals.md#relationshipstatus)
- [ScopeFilterKey](./literals.md#scopefilterkey)
- [SensitiveDataItemCategory](./literals.md#sensitivedataitemcategory)
- [SeverityDescription](./literals.md#severitydescription)
- [SharedAccess](./literals.md#sharedaccess)
- [StorageClass](./literals.md#storageclass)
- [TagTarget](./literals.md#tagtarget)
- [TimeRange](./literals.md#timerange)
- [TypeType](./literals.md#typetype)
- [Unit](./literals.md#unit)
- [UsageStatisticsFilterComparator](./literals.md#usagestatisticsfiltercomparator)
- [UsageStatisticsFilterKey](./literals.md#usagestatisticsfilterkey)
- [UsageStatisticsSortKey](./literals.md#usagestatisticssortkey)
- [UsageType](./literals.md#usagetype)
- [UserIdentityType](./literals.md#useridentitytype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_macie2.type_defs import AccessControlListTypeDef, ...
```

- [AccessControlListTypeDef](./type_defs.md#accesscontrollisttypedef)
- [AccountDetailTypeDef](./type_defs.md#accountdetailtypedef)
- [AccountLevelPermissionsTypeDef](./type_defs.md#accountlevelpermissionstypedef)
- [AdminAccountTypeDef](./type_defs.md#adminaccounttypedef)
- [ApiCallDetailsTypeDef](./type_defs.md#apicalldetailstypedef)
- [AssumedRoleTypeDef](./type_defs.md#assumedroletypedef)
- [AwsAccountTypeDef](./type_defs.md#awsaccounttypedef)
- [AwsServiceTypeDef](./type_defs.md#awsservicetypedef)
- [BatchGetCustomDataIdentifierSummaryTypeDef](./type_defs.md#batchgetcustomdataidentifiersummarytypedef)
- [BatchGetCustomDataIdentifiersResponseTypeDef](./type_defs.md#batchgetcustomdataidentifiersresponsetypedef)
- [BlockPublicAccessTypeDef](./type_defs.md#blockpublicaccesstypedef)
- [BucketCountByEffectivePermissionTypeDef](./type_defs.md#bucketcountbyeffectivepermissiontypedef)
- [BucketCountByEncryptionTypeTypeDef](./type_defs.md#bucketcountbyencryptiontypetypedef)
- [BucketCountBySharedAccessTypeTypeDef](./type_defs.md#bucketcountbysharedaccesstypetypedef)
- [BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef](./type_defs.md#bucketcountpolicyallowsunencryptedobjectuploadstypedef)
- [BucketCriteriaAdditionalPropertiesTypeDef](./type_defs.md#bucketcriteriaadditionalpropertiestypedef)
- [BucketLevelPermissionsTypeDef](./type_defs.md#bucketlevelpermissionstypedef)
- [BucketMetadataTypeDef](./type_defs.md#bucketmetadatatypedef)
- [BucketPermissionConfigurationTypeDef](./type_defs.md#bucketpermissionconfigurationtypedef)
- [BucketPolicyTypeDef](./type_defs.md#bucketpolicytypedef)
- [BucketPublicAccessTypeDef](./type_defs.md#bucketpublicaccesstypedef)
- [BucketServerSideEncryptionTypeDef](./type_defs.md#bucketserversideencryptiontypedef)
- [BucketSortCriteriaTypeDef](./type_defs.md#bucketsortcriteriatypedef)
- [CellTypeDef](./type_defs.md#celltypedef)
- [ClassificationDetailsTypeDef](./type_defs.md#classificationdetailstypedef)
- [ClassificationExportConfigurationTypeDef](./type_defs.md#classificationexportconfigurationtypedef)
- [ClassificationResultStatusTypeDef](./type_defs.md#classificationresultstatustypedef)
- [ClassificationResultTypeDef](./type_defs.md#classificationresulttypedef)
- [CreateClassificationJobResponseTypeDef](./type_defs.md#createclassificationjobresponsetypedef)
- [CreateCustomDataIdentifierResponseTypeDef](./type_defs.md#createcustomdataidentifierresponsetypedef)
- [CreateFindingsFilterResponseTypeDef](./type_defs.md#createfindingsfilterresponsetypedef)
- [CreateInvitationsResponseTypeDef](./type_defs.md#createinvitationsresponsetypedef)
- [CreateMemberResponseTypeDef](./type_defs.md#creatememberresponsetypedef)
- [CriterionAdditionalPropertiesTypeDef](./type_defs.md#criterionadditionalpropertiestypedef)
- [CustomDataIdentifierSummaryTypeDef](./type_defs.md#customdataidentifiersummarytypedef)
- [CustomDataIdentifiersTypeDef](./type_defs.md#customdataidentifierstypedef)
- [CustomDetectionTypeDef](./type_defs.md#customdetectiontypedef)
- [DeclineInvitationsResponseTypeDef](./type_defs.md#declineinvitationsresponsetypedef)
- [DefaultDetectionTypeDef](./type_defs.md#defaultdetectiontypedef)
- [DeleteInvitationsResponseTypeDef](./type_defs.md#deleteinvitationsresponsetypedef)
- [DescribeBucketsResponseTypeDef](./type_defs.md#describebucketsresponsetypedef)
- [DescribeClassificationJobResponseTypeDef](./type_defs.md#describeclassificationjobresponsetypedef)
- [DescribeOrganizationConfigurationResponseTypeDef](./type_defs.md#describeorganizationconfigurationresponsetypedef)
- [DomainDetailsTypeDef](./type_defs.md#domaindetailstypedef)
- [FederatedUserTypeDef](./type_defs.md#federatedusertypedef)
- [FindingActionTypeDef](./type_defs.md#findingactiontypedef)
- [FindingActorTypeDef](./type_defs.md#findingactortypedef)
- [FindingCriteriaTypeDef](./type_defs.md#findingcriteriatypedef)
- [FindingStatisticsSortCriteriaTypeDef](./type_defs.md#findingstatisticssortcriteriatypedef)
- [FindingTypeDef](./type_defs.md#findingtypedef)
- [FindingsFilterListItemTypeDef](./type_defs.md#findingsfilterlistitemtypedef)
- [GetAdministratorAccountResponseTypeDef](./type_defs.md#getadministratoraccountresponsetypedef)
- [GetBucketStatisticsResponseTypeDef](./type_defs.md#getbucketstatisticsresponsetypedef)
- [GetClassificationExportConfigurationResponseTypeDef](./type_defs.md#getclassificationexportconfigurationresponsetypedef)
- [GetCustomDataIdentifierResponseTypeDef](./type_defs.md#getcustomdataidentifierresponsetypedef)
- [GetFindingStatisticsResponseTypeDef](./type_defs.md#getfindingstatisticsresponsetypedef)
- [GetFindingsFilterResponseTypeDef](./type_defs.md#getfindingsfilterresponsetypedef)
- [GetFindingsPublicationConfigurationResponseTypeDef](./type_defs.md#getfindingspublicationconfigurationresponsetypedef)
- [GetFindingsResponseTypeDef](./type_defs.md#getfindingsresponsetypedef)
- [GetInvitationsCountResponseTypeDef](./type_defs.md#getinvitationscountresponsetypedef)
- [GetMacieSessionResponseTypeDef](./type_defs.md#getmaciesessionresponsetypedef)
- [GetMasterAccountResponseTypeDef](./type_defs.md#getmasteraccountresponsetypedef)
- [GetMemberResponseTypeDef](./type_defs.md#getmemberresponsetypedef)
- [GetUsageStatisticsResponseTypeDef](./type_defs.md#getusagestatisticsresponsetypedef)
- [GetUsageTotalsResponseTypeDef](./type_defs.md#getusagetotalsresponsetypedef)
- [GroupCountTypeDef](./type_defs.md#groupcounttypedef)
- [IamUserTypeDef](./type_defs.md#iamusertypedef)
- [InvitationTypeDef](./type_defs.md#invitationtypedef)
- [IpAddressDetailsTypeDef](./type_defs.md#ipaddressdetailstypedef)
- [IpCityTypeDef](./type_defs.md#ipcitytypedef)
- [IpCountryTypeDef](./type_defs.md#ipcountrytypedef)
- [IpGeoLocationTypeDef](./type_defs.md#ipgeolocationtypedef)
- [IpOwnerTypeDef](./type_defs.md#ipownertypedef)
- [JobDetailsTypeDef](./type_defs.md#jobdetailstypedef)
- [JobScheduleFrequencyTypeDef](./type_defs.md#jobschedulefrequencytypedef)
- [JobScopeTermTypeDef](./type_defs.md#jobscopetermtypedef)
- [JobScopingBlockTypeDef](./type_defs.md#jobscopingblocktypedef)
- [JobSummaryTypeDef](./type_defs.md#jobsummarytypedef)
- [KeyValuePairTypeDef](./type_defs.md#keyvaluepairtypedef)
- [LastRunErrorStatusTypeDef](./type_defs.md#lastrunerrorstatustypedef)
- [ListClassificationJobsResponseTypeDef](./type_defs.md#listclassificationjobsresponsetypedef)
- [ListCustomDataIdentifiersResponseTypeDef](./type_defs.md#listcustomdataidentifiersresponsetypedef)
- [ListFindingsFiltersResponseTypeDef](./type_defs.md#listfindingsfiltersresponsetypedef)
- [ListFindingsResponseTypeDef](./type_defs.md#listfindingsresponsetypedef)
- [ListInvitationsResponseTypeDef](./type_defs.md#listinvitationsresponsetypedef)
- [ListJobsFilterCriteriaTypeDef](./type_defs.md#listjobsfiltercriteriatypedef)
- [ListJobsFilterTermTypeDef](./type_defs.md#listjobsfiltertermtypedef)
- [ListJobsSortCriteriaTypeDef](./type_defs.md#listjobssortcriteriatypedef)
- [ListMembersResponseTypeDef](./type_defs.md#listmembersresponsetypedef)
- [ListOrganizationAdminAccountsResponseTypeDef](./type_defs.md#listorganizationadminaccountsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MemberTypeDef](./type_defs.md#membertypedef)
- [MonthlyScheduleTypeDef](./type_defs.md#monthlyscheduletypedef)
- [ObjectCountByEncryptionTypeTypeDef](./type_defs.md#objectcountbyencryptiontypetypedef)
- [ObjectLevelStatisticsTypeDef](./type_defs.md#objectlevelstatisticstypedef)
- [OccurrencesTypeDef](./type_defs.md#occurrencestypedef)
- [PageTypeDef](./type_defs.md#pagetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PolicyDetailsTypeDef](./type_defs.md#policydetailstypedef)
- [PutClassificationExportConfigurationResponseTypeDef](./type_defs.md#putclassificationexportconfigurationresponsetypedef)
- [RangeTypeDef](./type_defs.md#rangetypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [ReplicationDetailsTypeDef](./type_defs.md#replicationdetailstypedef)
- [ResourcesAffectedTypeDef](./type_defs.md#resourcesaffectedtypedef)
- [S3BucketDefinitionForJobTypeDef](./type_defs.md#s3bucketdefinitionforjobtypedef)
- [S3BucketOwnerTypeDef](./type_defs.md#s3bucketownertypedef)
- [S3BucketTypeDef](./type_defs.md#s3buckettypedef)
- [S3DestinationTypeDef](./type_defs.md#s3destinationtypedef)
- [S3JobDefinitionTypeDef](./type_defs.md#s3jobdefinitiontypedef)
- [S3ObjectTypeDef](./type_defs.md#s3objecttypedef)
- [ScopingTypeDef](./type_defs.md#scopingtypedef)
- [SecurityHubConfigurationTypeDef](./type_defs.md#securityhubconfigurationtypedef)
- [SensitiveDataItemTypeDef](./type_defs.md#sensitivedataitemtypedef)
- [ServerSideEncryptionTypeDef](./type_defs.md#serversideencryptiontypedef)
- [ServiceLimitTypeDef](./type_defs.md#servicelimittypedef)
- [SessionContextAttributesTypeDef](./type_defs.md#sessioncontextattributestypedef)
- [SessionContextTypeDef](./type_defs.md#sessioncontexttypedef)
- [SessionIssuerTypeDef](./type_defs.md#sessionissuertypedef)
- [SeverityTypeDef](./type_defs.md#severitytypedef)
- [SimpleScopeTermTypeDef](./type_defs.md#simplescopetermtypedef)
- [SortCriteriaTypeDef](./type_defs.md#sortcriteriatypedef)
- [StatisticsTypeDef](./type_defs.md#statisticstypedef)
- [TagScopeTermTypeDef](./type_defs.md#tagscopetermtypedef)
- [TagValuePairTypeDef](./type_defs.md#tagvaluepairtypedef)
- [TestCustomDataIdentifierResponseTypeDef](./type_defs.md#testcustomdataidentifierresponsetypedef)
- [UnprocessedAccountTypeDef](./type_defs.md#unprocessedaccounttypedef)
- [UpdateFindingsFilterResponseTypeDef](./type_defs.md#updatefindingsfilterresponsetypedef)
- [UsageByAccountTypeDef](./type_defs.md#usagebyaccounttypedef)
- [UsageRecordTypeDef](./type_defs.md#usagerecordtypedef)
- [UsageStatisticsFilterTypeDef](./type_defs.md#usagestatisticsfiltertypedef)
- [UsageStatisticsSortByTypeDef](./type_defs.md#usagestatisticssortbytypedef)
- [UsageTotalTypeDef](./type_defs.md#usagetotaltypedef)
- [UserIdentityRootTypeDef](./type_defs.md#useridentityroottypedef)
- [UserIdentityTypeDef](./type_defs.md#useridentitytypedef)
- [UserPausedDetailsTypeDef](./type_defs.md#userpauseddetailstypedef)
- [WeeklyScheduleTypeDef](./type_defs.md#weeklyscheduletypedef)
