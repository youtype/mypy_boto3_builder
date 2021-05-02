# Literals for boto3 Macie2 module

> [Index](../index.md) > [Macie2](./index.md) > Literals

Auto-generated documentation for [Macie2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2)
type annotations stubs module [mypy_boto3_macie2](https://pypi.org/project/mypy-boto3-macie2/).

- [Literals for boto3 Macie2 module](#literals-for-boto3-macie2-module)
  - [AdminStatus](#adminstatus)
  - [AllowsUnencryptedObjectUploads](#allowsunencryptedobjectuploads)
  - [Currency](#currency)
  - [DayOfWeek](#dayofweek)
  - [DescribeBucketsPaginatorName](#describebucketspaginatorname)
  - [EffectivePermission](#effectivepermission)
  - [EncryptionType](#encryptiontype)
  - [ErrorCode](#errorcode)
  - [FindingActionType](#findingactiontype)
  - [FindingCategory](#findingcategory)
  - [FindingPublishingFrequency](#findingpublishingfrequency)
  - [FindingStatisticsSortAttributeName](#findingstatisticssortattributename)
  - [FindingType](#findingtype)
  - [FindingsFilterAction](#findingsfilteraction)
  - [GetUsageStatisticsPaginatorName](#getusagestatisticspaginatorname)
  - [GroupBy](#groupby)
  - [IsDefinedInJob](#isdefinedinjob)
  - [IsMonitoredByJob](#ismonitoredbyjob)
  - [JobComparator](#jobcomparator)
  - [JobStatus](#jobstatus)
  - [JobType](#jobtype)
  - [LastRunErrorStatusCode](#lastrunerrorstatuscode)
  - [ListClassificationJobsPaginatorName](#listclassificationjobspaginatorname)
  - [ListCustomDataIdentifiersPaginatorName](#listcustomdataidentifierspaginatorname)
  - [ListFindingsFiltersPaginatorName](#listfindingsfilterspaginatorname)
  - [ListFindingsPaginatorName](#listfindingspaginatorname)
  - [ListInvitationsPaginatorName](#listinvitationspaginatorname)
  - [ListJobsFilterKey](#listjobsfilterkey)
  - [ListJobsSortAttributeName](#listjobssortattributename)
  - [ListMembersPaginatorName](#listmemberspaginatorname)
  - [ListOrganizationAdminAccountsPaginatorName](#listorganizationadminaccountspaginatorname)
  - [MacieStatus](#maciestatus)
  - [OrderBy](#orderby)
  - [RelationshipStatus](#relationshipstatus)
  - [ScopeFilterKey](#scopefilterkey)
  - [SensitiveDataItemCategory](#sensitivedataitemcategory)
  - [SeverityDescription](#severitydescription)
  - [SharedAccess](#sharedaccess)
  - [StorageClass](#storageclass)
  - [TagTarget](#tagtarget)
  - [TimeRange](#timerange)
  - [TypeType](#typetype)
  - [Unit](#unit)
  - [UsageStatisticsFilterComparator](#usagestatisticsfiltercomparator)
  - [UsageStatisticsFilterKey](#usagestatisticsfilterkey)
  - [UsageStatisticsSortKey](#usagestatisticssortkey)
  - [UsageType](#usagetype)
  - [UserIdentityType](#useridentitytype)

## AdminStatus

```python
from mypy_boto3_macie2.literals import AdminStatus
```

Values:

- `DISABLING_IN_PROGRESS`
- `ENABLED`

## AllowsUnencryptedObjectUploads

```python
from mypy_boto3_macie2.literals import AllowsUnencryptedObjectUploads
```

Values:

- `FALSE`
- `TRUE`
- `UNKNOWN`

## Currency

```python
from mypy_boto3_macie2.literals import Currency
```

Values:

- `USD`

## DayOfWeek

```python
from mypy_boto3_macie2.literals import DayOfWeek
```

Values:

- `FRIDAY`
- `MONDAY`
- `SATURDAY`
- `SUNDAY`
- `THURSDAY`
- `TUESDAY`
- `WEDNESDAY`

## DescribeBucketsPaginatorName

```python
from mypy_boto3_macie2.literals import DescribeBucketsPaginatorName
```

Values:

- `describe_buckets`

## EffectivePermission

```python
from mypy_boto3_macie2.literals import EffectivePermission
```

Values:

- `NOT_PUBLIC`
- `PUBLIC`
- `UNKNOWN`

## EncryptionType

```python
from mypy_boto3_macie2.literals import EncryptionType
```

Values:

- `AES256`
- `aws:kms`
- `NONE`
- `UNKNOWN`

## ErrorCode

```python
from mypy_boto3_macie2.literals import ErrorCode
```

Values:

- `ClientError`
- `InternalError`

## FindingActionType

```python
from mypy_boto3_macie2.literals import FindingActionType
```

Values:

- `AWS_API_CALL`

## FindingCategory

```python
from mypy_boto3_macie2.literals import FindingCategory
```

Values:

- `CLASSIFICATION`
- `POLICY`

## FindingPublishingFrequency

```python
from mypy_boto3_macie2.literals import FindingPublishingFrequency
```

Values:

- `FIFTEEN_MINUTES`
- `ONE_HOUR`
- `SIX_HOURS`

## FindingStatisticsSortAttributeName

```python
from mypy_boto3_macie2.literals import FindingStatisticsSortAttributeName
```

Values:

- `count`
- `groupKey`

## FindingType

```python
from mypy_boto3_macie2.literals import FindingType
```

Values:

- `Policy:IAMUser/S3BlockPublicAccessDisabled`
- `Policy:IAMUser/S3BucketEncryptionDisabled`
- `Policy:IAMUser/S3BucketPublic`
- `Policy:IAMUser/S3BucketReplicatedExternally`
- `Policy:IAMUser/S3BucketSharedExternally`
- `SensitiveData:S3Object/Credentials`
- `SensitiveData:S3Object/CustomIdentifier`
- `SensitiveData:S3Object/Financial`
- `SensitiveData:S3Object/Multiple`
- `SensitiveData:S3Object/Personal`

## FindingsFilterAction

```python
from mypy_boto3_macie2.literals import FindingsFilterAction
```

Values:

- `ARCHIVE`
- `NOOP`

## GetUsageStatisticsPaginatorName

```python
from mypy_boto3_macie2.literals import GetUsageStatisticsPaginatorName
```

Values:

- `get_usage_statistics`

## GroupBy

```python
from mypy_boto3_macie2.literals import GroupBy
```

Values:

- `classificationDetails.jobId`
- `resourcesAffected.s3Bucket.name`
- `severity.description`
- `type`

## IsDefinedInJob

```python
from mypy_boto3_macie2.literals import IsDefinedInJob
```

Values:

- `FALSE`
- `TRUE`
- `UNKNOWN`

## IsMonitoredByJob

```python
from mypy_boto3_macie2.literals import IsMonitoredByJob
```

Values:

- `FALSE`
- `TRUE`
- `UNKNOWN`

## JobComparator

```python
from mypy_boto3_macie2.literals import JobComparator
```

Values:

- `CONTAINS`
- `EQ`
- `GT`
- `GTE`
- `LT`
- `LTE`
- `NE`
- `STARTS_WITH`

## JobStatus

```python
from mypy_boto3_macie2.literals import JobStatus
```

Values:

- `CANCELLED`
- `COMPLETE`
- `IDLE`
- `PAUSED`
- `RUNNING`
- `USER_PAUSED`

## JobType

```python
from mypy_boto3_macie2.literals import JobType
```

Values:

- `ONE_TIME`
- `SCHEDULED`

## LastRunErrorStatusCode

```python
from mypy_boto3_macie2.literals import LastRunErrorStatusCode
```

Values:

- `ERROR`
- `NONE`

## ListClassificationJobsPaginatorName

```python
from mypy_boto3_macie2.literals import ListClassificationJobsPaginatorName
```

Values:

- `list_classification_jobs`

## ListCustomDataIdentifiersPaginatorName

```python
from mypy_boto3_macie2.literals import ListCustomDataIdentifiersPaginatorName
```

Values:

- `list_custom_data_identifiers`

## ListFindingsFiltersPaginatorName

```python
from mypy_boto3_macie2.literals import ListFindingsFiltersPaginatorName
```

Values:

- `list_findings_filters`

## ListFindingsPaginatorName

```python
from mypy_boto3_macie2.literals import ListFindingsPaginatorName
```

Values:

- `list_findings`

## ListInvitationsPaginatorName

```python
from mypy_boto3_macie2.literals import ListInvitationsPaginatorName
```

Values:

- `list_invitations`

## ListJobsFilterKey

```python
from mypy_boto3_macie2.literals import ListJobsFilterKey
```

Values:

- `createdAt`
- `jobStatus`
- `jobType`
- `name`

## ListJobsSortAttributeName

```python
from mypy_boto3_macie2.literals import ListJobsSortAttributeName
```

Values:

- `createdAt`
- `jobStatus`
- `jobType`
- `name`

## ListMembersPaginatorName

```python
from mypy_boto3_macie2.literals import ListMembersPaginatorName
```

Values:

- `list_members`

## ListOrganizationAdminAccountsPaginatorName

```python
from mypy_boto3_macie2.literals import ListOrganizationAdminAccountsPaginatorName
```

Values:

- `list_organization_admin_accounts`

## MacieStatus

```python
from mypy_boto3_macie2.literals import MacieStatus
```

Values:

- `ENABLED`
- `PAUSED`

## OrderBy

```python
from mypy_boto3_macie2.literals import OrderBy
```

Values:

- `ASC`
- `DESC`

## RelationshipStatus

```python
from mypy_boto3_macie2.literals import RelationshipStatus
```

Values:

- `AccountSuspended`
- `Created`
- `EmailVerificationFailed`
- `EmailVerificationInProgress`
- `Enabled`
- `Invited`
- `Paused`
- `RegionDisabled`
- `Removed`
- `Resigned`

## ScopeFilterKey

```python
from mypy_boto3_macie2.literals import ScopeFilterKey
```

Values:

- `BUCKET_CREATION_DATE`
- `OBJECT_EXTENSION`
- `OBJECT_KEY`
- `OBJECT_LAST_MODIFIED_DATE`
- `OBJECT_SIZE`
- `TAG`

## SensitiveDataItemCategory

```python
from mypy_boto3_macie2.literals import SensitiveDataItemCategory
```

Values:

- `CREDENTIALS`
- `CUSTOM_IDENTIFIER`
- `FINANCIAL_INFORMATION`
- `PERSONAL_INFORMATION`

## SeverityDescription

```python
from mypy_boto3_macie2.literals import SeverityDescription
```

Values:

- `High`
- `Low`
- `Medium`

## SharedAccess

```python
from mypy_boto3_macie2.literals import SharedAccess
```

Values:

- `EXTERNAL`
- `INTERNAL`
- `NOT_SHARED`
- `UNKNOWN`

## StorageClass

```python
from mypy_boto3_macie2.literals import StorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `REDUCED_REDUNDANCY`
- `STANDARD`
- `STANDARD_IA`

## TagTarget

```python
from mypy_boto3_macie2.literals import TagTarget
```

Values:

- `S3_OBJECT`

## TimeRange

```python
from mypy_boto3_macie2.literals import TimeRange
```

Values:

- `MONTH_TO_DATE`
- `PAST_30_DAYS`

## TypeType

```python
from mypy_boto3_macie2.literals import TypeType
```

Values:

- `AES256`
- `aws:kms`
- `NONE`

## Unit

```python
from mypy_boto3_macie2.literals import Unit
```

Values:

- `TERABYTES`

## UsageStatisticsFilterComparator

```python
from mypy_boto3_macie2.literals import UsageStatisticsFilterComparator
```

Values:

- `CONTAINS`
- `EQ`
- `GT`
- `GTE`
- `LT`
- `LTE`
- `NE`

## UsageStatisticsFilterKey

```python
from mypy_boto3_macie2.literals import UsageStatisticsFilterKey
```

Values:

- `accountId`
- `freeTrialStartDate`
- `serviceLimit`
- `total`

## UsageStatisticsSortKey

```python
from mypy_boto3_macie2.literals import UsageStatisticsSortKey
```

Values:

- `accountId`
- `freeTrialStartDate`
- `serviceLimitValue`
- `total`

## UsageType

```python
from mypy_boto3_macie2.literals import UsageType
```

Values:

- `DATA_INVENTORY_EVALUATION`
- `SENSITIVE_DATA_DISCOVERY`

## UserIdentityType

```python
from mypy_boto3_macie2.literals import UserIdentityType
```

Values:

- `AssumedRole`
- `AWSAccount`
- `AWSService`
- `FederatedUser`
- `IAMUser`
- `Root`
