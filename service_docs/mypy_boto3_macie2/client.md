# Macie2Client for boto3 Macie2 module

> [Index](../index.md) > [Macie2](./index.md) > Macie2Client

Auto-generated documentation for [Macie2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2)
type annotations stubs module [mypy_boto3_macie2](https://pypi.org/project/mypy-boto3-macie2/).

- [Macie2Client for boto3 Macie2 module](#macie2client-for-boto3-macie2-module)
  - [Macie2Client](#macie2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_invitation](#accept_invitation)
    - [batch_get_custom_data_identifiers](#batch_get_custom_data_identifiers)
    - [can_paginate](#can_paginate)
    - [create_classification_job](#create_classification_job)
    - [create_custom_data_identifier](#create_custom_data_identifier)
    - [create_findings_filter](#create_findings_filter)
    - [create_invitations](#create_invitations)
    - [create_member](#create_member)
    - [create_sample_findings](#create_sample_findings)
    - [decline_invitations](#decline_invitations)
    - [delete_custom_data_identifier](#delete_custom_data_identifier)
    - [delete_findings_filter](#delete_findings_filter)
    - [delete_invitations](#delete_invitations)
    - [delete_member](#delete_member)
    - [describe_buckets](#describe_buckets)
    - [describe_classification_job](#describe_classification_job)
    - [describe_organization_configuration](#describe_organization_configuration)
    - [disable_macie](#disable_macie)
    - [disable_organization_admin_account](#disable_organization_admin_account)
    - [disassociate_from_administrator_account](#disassociate_from_administrator_account)
    - [disassociate_from_master_account](#disassociate_from_master_account)
    - [disassociate_member](#disassociate_member)
    - [enable_macie](#enable_macie)
    - [enable_organization_admin_account](#enable_organization_admin_account)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_administrator_account](#get_administrator_account)
    - [get_bucket_statistics](#get_bucket_statistics)
    - [get_classification_export_configuration](#get_classification_export_configuration)
    - [get_custom_data_identifier](#get_custom_data_identifier)
    - [get_finding_statistics](#get_finding_statistics)
    - [get_findings](#get_findings)
    - [get_findings_filter](#get_findings_filter)
    - [get_findings_publication_configuration](#get_findings_publication_configuration)
    - [get_invitations_count](#get_invitations_count)
    - [get_macie_session](#get_macie_session)
    - [get_master_account](#get_master_account)
    - [get_member](#get_member)
    - [get_usage_statistics](#get_usage_statistics)
    - [get_usage_totals](#get_usage_totals)
    - [list_classification_jobs](#list_classification_jobs)
    - [list_custom_data_identifiers](#list_custom_data_identifiers)
    - [list_findings](#list_findings)
    - [list_findings_filters](#list_findings_filters)
    - [list_invitations](#list_invitations)
    - [list_members](#list_members)
    - [list_organization_admin_accounts](#list_organization_admin_accounts)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_classification_export_configuration](#put_classification_export_configuration)
    - [put_findings_publication_configuration](#put_findings_publication_configuration)
    - [tag_resource](#tag_resource)
    - [test_custom_data_identifier](#test_custom_data_identifier)
    - [untag_resource](#untag_resource)
    - [update_classification_job](#update_classification_job)
    - [update_findings_filter](#update_findings_filter)
    - [update_macie_session](#update_macie_session)
    - [update_member_session](#update_member_session)
    - [update_organization_configuration](#update_organization_configuration)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)

## Macie2Client

Type annotations for `boto3.client("macie2")`

Can be used directly:

```python
from mypy_boto3_macie2.client import Macie2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_macie2.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### accept_invitation

Type annotations for `boto3.client("macie2").accept_invitation` method.

[Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.accept_invitation)

```python
def accept_invitation(
    self,
    invitationId: str,
    administratorAccountId: str = None,
    masterAccount: str = None
) -> Dict[str, Any]:
    pass
```

### batch_get_custom_data_identifiers

Type annotations for `boto3.client("macie2").batch_get_custom_data_identifiers` method.

[Client.batch_get_custom_data_identifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.batch_get_custom_data_identifiers)

```python
def batch_get_custom_data_identifiers(
    self,
    ids: List[str] = None
) -> BatchGetCustomDataIdentifiersResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("macie2").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_classification_job

Type annotations for `boto3.client("macie2").create_classification_job` method.

[Client.create_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.create_classification_job)

```python
def create_classification_job(
    self,
    clientToken: str,
    jobType: JobType,
    name: str,
    s3JobDefinition: "S3JobDefinitionTypeDef",
    customDataIdentifierIds: List[str] = None,
    description: str = None,
    initialRun: bool = None,
    samplingPercentage: int = None,
    scheduleFrequency: "JobScheduleFrequencyTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateClassificationJobResponseTypeDef:
    pass
```

### create_custom_data_identifier

Type annotations for `boto3.client("macie2").create_custom_data_identifier` method.

[Client.create_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.create_custom_data_identifier)

```python
def create_custom_data_identifier(
    self,
    clientToken: str = None,
    description: str = None,
    ignoreWords: List[str] = None,
    keywords: List[str] = None,
    maximumMatchDistance: int = None,
    name: str = None,
    regex: str = None,
    tags: Dict[str, str] = None
) -> CreateCustomDataIdentifierResponseTypeDef:
    pass
```

### create_findings_filter

Type annotations for `boto3.client("macie2").create_findings_filter` method.

[Client.create_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.create_findings_filter)

```python
def create_findings_filter(
    self,
    action: FindingsFilterAction,
    findingCriteria: "FindingCriteriaTypeDef",
    name: str,
    clientToken: str = None,
    description: str = None,
    position: int = None,
    tags: Dict[str, str] = None
) -> CreateFindingsFilterResponseTypeDef:
    pass
```

### create_invitations

Type annotations for `boto3.client("macie2").create_invitations` method.

[Client.create_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.create_invitations)

```python
def create_invitations(
    self,
    accountIds: List[str],
    disableEmailNotification: bool = None,
    message: str = None
) -> CreateInvitationsResponseTypeDef:
    pass
```

### create_member

Type annotations for `boto3.client("macie2").create_member` method.

[Client.create_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.create_member)

```python
def create_member(
    self,
    account: AccountDetailTypeDef,
    tags: Dict[str, str] = None
) -> CreateMemberResponseTypeDef:
    pass
```

### create_sample_findings

Type annotations for `boto3.client("macie2").create_sample_findings` method.

[Client.create_sample_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.create_sample_findings)

```python
def create_sample_findings(
    self,
    findingTypes: List[FindingType] = None
) -> Dict[str, Any]:
    pass
```

### decline_invitations

Type annotations for `boto3.client("macie2").decline_invitations` method.

[Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.decline_invitations)

```python
def decline_invitations(
    self,
    accountIds: List[str]
) -> DeclineInvitationsResponseTypeDef:
    pass
```

### delete_custom_data_identifier

Type annotations for `boto3.client("macie2").delete_custom_data_identifier` method.

[Client.delete_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.delete_custom_data_identifier)

```python
def delete_custom_data_identifier(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### delete_findings_filter

Type annotations for `boto3.client("macie2").delete_findings_filter` method.

[Client.delete_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.delete_findings_filter)

```python
def delete_findings_filter(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### delete_invitations

Type annotations for `boto3.client("macie2").delete_invitations` method.

[Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.delete_invitations)

```python
def delete_invitations(
    self,
    accountIds: List[str]
) -> DeleteInvitationsResponseTypeDef:
    pass
```

### delete_member

Type annotations for `boto3.client("macie2").delete_member` method.

[Client.delete_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.delete_member)

```python
def delete_member(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### describe_buckets

Type annotations for `boto3.client("macie2").describe_buckets` method.

[Client.describe_buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.describe_buckets)

```python
def describe_buckets(
    self,
    criteria: Dict[str, BucketCriteriaAdditionalPropertiesTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None,
    sortCriteria: BucketSortCriteriaTypeDef = None
) -> DescribeBucketsResponseTypeDef:
    pass
```

### describe_classification_job

Type annotations for `boto3.client("macie2").describe_classification_job` method.

[Client.describe_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.describe_classification_job)

```python
def describe_classification_job(
    self,
    jobId: str
) -> DescribeClassificationJobResponseTypeDef:
    pass
```

### describe_organization_configuration

Type annotations for `boto3.client("macie2").describe_organization_configuration` method.

[Client.describe_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.describe_organization_configuration)

```python
def describe_organization_configuration(
    self
) -> DescribeOrganizationConfigurationResponseTypeDef:
    pass
```

### disable_macie

Type annotations for `boto3.client("macie2").disable_macie` method.

[Client.disable_macie documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.disable_macie)

```python
def disable_macie(
    self
) -> Dict[str, Any]:
    pass
```

### disable_organization_admin_account

Type annotations for `boto3.client("macie2").disable_organization_admin_account` method.

[Client.disable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.disable_organization_admin_account)

```python
def disable_organization_admin_account(
    self,
    adminAccountId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_from_administrator_account

Type annotations for `boto3.client("macie2").disassociate_from_administrator_account` method.

[Client.disassociate_from_administrator_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.disassociate_from_administrator_account)

```python
def disassociate_from_administrator_account(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_from_master_account

Type annotations for `boto3.client("macie2").disassociate_from_master_account` method.

[Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.disassociate_from_master_account)

```python
def disassociate_from_master_account(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_member

Type annotations for `boto3.client("macie2").disassociate_member` method.

[Client.disassociate_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.disassociate_member)

```python
def disassociate_member(
    self,
    id: str
) -> Dict[str, Any]:
    pass
```

### enable_macie

Type annotations for `boto3.client("macie2").enable_macie` method.

[Client.enable_macie documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.enable_macie)

```python
def enable_macie(
    self,
    clientToken: str = None,
    findingPublishingFrequency: FindingPublishingFrequency = None,
    status: MacieStatus = None
) -> Dict[str, Any]:
    pass
```

### enable_organization_admin_account

Type annotations for `boto3.client("macie2").enable_organization_admin_account` method.

[Client.enable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.enable_organization_admin_account)

```python
def enable_organization_admin_account(
    self,
    adminAccountId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("macie2").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_administrator_account

Type annotations for `boto3.client("macie2").get_administrator_account` method.

[Client.get_administrator_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_administrator_account)

```python
def get_administrator_account(
    self
) -> GetAdministratorAccountResponseTypeDef:
    pass
```

### get_bucket_statistics

Type annotations for `boto3.client("macie2").get_bucket_statistics` method.

[Client.get_bucket_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_bucket_statistics)

```python
def get_bucket_statistics(
    self,
    accountId: str = None
) -> GetBucketStatisticsResponseTypeDef:
    pass
```

### get_classification_export_configuration

Type annotations for `boto3.client("macie2").get_classification_export_configuration` method.

[Client.get_classification_export_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_classification_export_configuration)

```python
def get_classification_export_configuration(
    self
) -> GetClassificationExportConfigurationResponseTypeDef:
    pass
```

### get_custom_data_identifier

Type annotations for `boto3.client("macie2").get_custom_data_identifier` method.

[Client.get_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_custom_data_identifier)

```python
def get_custom_data_identifier(
    self,
    id: str
) -> GetCustomDataIdentifierResponseTypeDef:
    pass
```

### get_finding_statistics

Type annotations for `boto3.client("macie2").get_finding_statistics` method.

[Client.get_finding_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_finding_statistics)

```python
def get_finding_statistics(
    self,
    groupBy: GroupBy,
    findingCriteria: "FindingCriteriaTypeDef" = None,
    size: int = None,
    sortCriteria: FindingStatisticsSortCriteriaTypeDef = None
) -> GetFindingStatisticsResponseTypeDef:
    pass
```

### get_findings

Type annotations for `boto3.client("macie2").get_findings` method.

[Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_findings)

```python
def get_findings(
    self,
    findingIds: List[str],
    sortCriteria: SortCriteriaTypeDef = None
) -> GetFindingsResponseTypeDef:
    pass
```

### get_findings_filter

Type annotations for `boto3.client("macie2").get_findings_filter` method.

[Client.get_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_findings_filter)

```python
def get_findings_filter(
    self,
    id: str
) -> GetFindingsFilterResponseTypeDef:
    pass
```

### get_findings_publication_configuration

Type annotations for `boto3.client("macie2").get_findings_publication_configuration` method.

[Client.get_findings_publication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_findings_publication_configuration)

```python
def get_findings_publication_configuration(
    self
) -> GetFindingsPublicationConfigurationResponseTypeDef:
    pass
```

### get_invitations_count

Type annotations for `boto3.client("macie2").get_invitations_count` method.

[Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_invitations_count)

```python
def get_invitations_count(
    self
) -> GetInvitationsCountResponseTypeDef:
    pass
```

### get_macie_session

Type annotations for `boto3.client("macie2").get_macie_session` method.

[Client.get_macie_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_macie_session)

```python
def get_macie_session(
    self
) -> GetMacieSessionResponseTypeDef:
    pass
```

### get_master_account

Type annotations for `boto3.client("macie2").get_master_account` method.

[Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_master_account)

```python
def get_master_account(
    self
) -> GetMasterAccountResponseTypeDef:
    pass
```

### get_member

Type annotations for `boto3.client("macie2").get_member` method.

[Client.get_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_member)

```python
def get_member(
    self,
    id: str
) -> GetMemberResponseTypeDef:
    pass
```

### get_usage_statistics

Type annotations for `boto3.client("macie2").get_usage_statistics` method.

[Client.get_usage_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_usage_statistics)

```python
def get_usage_statistics(
    self,
    filterBy: List[UsageStatisticsFilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None,
    sortBy: UsageStatisticsSortByTypeDef = None,
    timeRange: TimeRange = None
) -> GetUsageStatisticsResponseTypeDef:
    pass
```

### get_usage_totals

Type annotations for `boto3.client("macie2").get_usage_totals` method.

[Client.get_usage_totals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.get_usage_totals)

```python
def get_usage_totals(
    self,
    timeRange: str = None
) -> GetUsageTotalsResponseTypeDef:
    pass
```

### list_classification_jobs

Type annotations for `boto3.client("macie2").list_classification_jobs` method.

[Client.list_classification_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_classification_jobs)

```python
def list_classification_jobs(
    self,
    filterCriteria: ListJobsFilterCriteriaTypeDef = None,
    maxResults: int = None,
    nextToken: str = None,
    sortCriteria: ListJobsSortCriteriaTypeDef = None
) -> ListClassificationJobsResponseTypeDef:
    pass
```

### list_custom_data_identifiers

Type annotations for `boto3.client("macie2").list_custom_data_identifiers` method.

[Client.list_custom_data_identifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_custom_data_identifiers)

```python
def list_custom_data_identifiers(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListCustomDataIdentifiersResponseTypeDef:
    pass
```

### list_findings

Type annotations for `boto3.client("macie2").list_findings` method.

[Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_findings)

```python
def list_findings(
    self,
    findingCriteria: "FindingCriteriaTypeDef" = None,
    maxResults: int = None,
    nextToken: str = None,
    sortCriteria: SortCriteriaTypeDef = None
) -> ListFindingsResponseTypeDef:
    pass
```

### list_findings_filters

Type annotations for `boto3.client("macie2").list_findings_filters` method.

[Client.list_findings_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_findings_filters)

```python
def list_findings_filters(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListFindingsFiltersResponseTypeDef:
    pass
```

### list_invitations

Type annotations for `boto3.client("macie2").list_invitations` method.

[Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_invitations)

```python
def list_invitations(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListInvitationsResponseTypeDef:
    pass
```

### list_members

Type annotations for `boto3.client("macie2").list_members` method.

[Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_members)

```python
def list_members(
    self,
    maxResults: int = None,
    nextToken: str = None,
    onlyAssociated: str = None
) -> ListMembersResponseTypeDef:
    pass
```

### list_organization_admin_accounts

Type annotations for `boto3.client("macie2").list_organization_admin_accounts` method.

[Client.list_organization_admin_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_organization_admin_accounts)

```python
def list_organization_admin_accounts(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListOrganizationAdminAccountsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("macie2").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_classification_export_configuration

Type annotations for `boto3.client("macie2").put_classification_export_configuration` method.

[Client.put_classification_export_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.put_classification_export_configuration)

```python
def put_classification_export_configuration(
    self,
    configuration: "ClassificationExportConfigurationTypeDef"
) -> PutClassificationExportConfigurationResponseTypeDef:
    pass
```

### put_findings_publication_configuration

Type annotations for `boto3.client("macie2").put_findings_publication_configuration` method.

[Client.put_findings_publication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.put_findings_publication_configuration)

```python
def put_findings_publication_configuration(
    self,
    clientToken: str = None,
    securityHubConfiguration: "SecurityHubConfigurationTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("macie2").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### test_custom_data_identifier

Type annotations for `boto3.client("macie2").test_custom_data_identifier` method.

[Client.test_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.test_custom_data_identifier)

```python
def test_custom_data_identifier(
    self,
    regex: str,
    sampleText: str,
    ignoreWords: List[str] = None,
    keywords: List[str] = None,
    maximumMatchDistance: int = None
) -> TestCustomDataIdentifierResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("macie2").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_classification_job

Type annotations for `boto3.client("macie2").update_classification_job` method.

[Client.update_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.update_classification_job)

```python
def update_classification_job(
    self,
    jobId: str,
    jobStatus: JobStatus
) -> Dict[str, Any]:
    pass
```

### update_findings_filter

Type annotations for `boto3.client("macie2").update_findings_filter` method.

[Client.update_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.update_findings_filter)

```python
def update_findings_filter(
    self,
    id: str,
    action: FindingsFilterAction = None,
    description: str = None,
    findingCriteria: "FindingCriteriaTypeDef" = None,
    name: str = None,
    position: int = None
) -> UpdateFindingsFilterResponseTypeDef:
    pass
```

### update_macie_session

Type annotations for `boto3.client("macie2").update_macie_session` method.

[Client.update_macie_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.update_macie_session)

```python
def update_macie_session(
    self,
    findingPublishingFrequency: FindingPublishingFrequency = None,
    status: MacieStatus = None
) -> Dict[str, Any]:
    pass
```

### update_member_session

Type annotations for `boto3.client("macie2").update_member_session` method.

[Client.update_member_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.update_member_session)

```python
def update_member_session(
    self,
    id: str,
    status: MacieStatus
) -> Dict[str, Any]:
    pass
```

### update_organization_configuration

Type annotations for `boto3.client("macie2").update_organization_configuration` method.

[Client.update_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Client.update_organization_configuration)

```python
def update_organization_configuration(
    self,
    autoEnable: bool
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.DescribeBuckets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.DescribeBuckets)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBucketsPaginatorName
) -> DescribeBucketsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.GetUsageStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.GetUsageStatistics)

```python
@overload
def get_paginator(
    self,
    operation_name: GetUsageStatisticsPaginatorName
) -> GetUsageStatisticsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListClassificationJobs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListClassificationJobsPaginatorName
) -> ListClassificationJobsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListCustomDataIdentifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListCustomDataIdentifiers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCustomDataIdentifiersPaginatorName
) -> ListCustomDataIdentifiersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListFindings)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFindingsPaginatorName
) -> ListFindingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListFindingsFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListFindingsFilters)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFindingsFiltersPaginatorName
) -> ListFindingsFiltersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListInvitations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInvitationsPaginatorName
) -> ListInvitationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListMembers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMembersPaginatorName
) -> ListMembersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("macie2").get_paginator` method.

[Paginator.ListOrganizationAdminAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html#Macie2.Paginator.ListOrganizationAdminAccounts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOrganizationAdminAccountsPaginatorName
) -> ListOrganizationAdminAccountsPaginator:
    pass
```