# GuardDutyClient for boto3 GuardDuty module

> [Index](../index.md) > [GuardDuty](./index.md) > GuardDutyClient

Auto-generated documentation for [GuardDuty](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty)
type annotations stubs module [mypy_boto3_guardduty](https://pypi.org/project/mypy-boto3-guardduty/).

- [GuardDutyClient for boto3 GuardDuty module](#guarddutyclient-for-boto3-guardduty-module)
  - [GuardDutyClient](#guarddutyclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_invitation](#accept_invitation)
    - [archive_findings](#archive_findings)
    - [can_paginate](#can_paginate)
    - [create_detector](#create_detector)
    - [create_filter](#create_filter)
    - [create_ip_set](#create_ip_set)
    - [create_members](#create_members)
    - [create_publishing_destination](#create_publishing_destination)
    - [create_sample_findings](#create_sample_findings)
    - [create_threat_intel_set](#create_threat_intel_set)
    - [decline_invitations](#decline_invitations)
    - [delete_detector](#delete_detector)
    - [delete_filter](#delete_filter)
    - [delete_invitations](#delete_invitations)
    - [delete_ip_set](#delete_ip_set)
    - [delete_members](#delete_members)
    - [delete_publishing_destination](#delete_publishing_destination)
    - [delete_threat_intel_set](#delete_threat_intel_set)
    - [describe_organization_configuration](#describe_organization_configuration)
    - [describe_publishing_destination](#describe_publishing_destination)
    - [disable_organization_admin_account](#disable_organization_admin_account)
    - [disassociate_from_master_account](#disassociate_from_master_account)
    - [disassociate_members](#disassociate_members)
    - [enable_organization_admin_account](#enable_organization_admin_account)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_detector](#get_detector)
    - [get_filter](#get_filter)
    - [get_findings](#get_findings)
    - [get_findings_statistics](#get_findings_statistics)
    - [get_invitations_count](#get_invitations_count)
    - [get_ip_set](#get_ip_set)
    - [get_master_account](#get_master_account)
    - [get_member_detectors](#get_member_detectors)
    - [get_members](#get_members)
    - [get_threat_intel_set](#get_threat_intel_set)
    - [get_usage_statistics](#get_usage_statistics)
    - [invite_members](#invite_members)
    - [list_detectors](#list_detectors)
    - [list_filters](#list_filters)
    - [list_findings](#list_findings)
    - [list_invitations](#list_invitations)
    - [list_ip_sets](#list_ip_sets)
    - [list_members](#list_members)
    - [list_organization_admin_accounts](#list_organization_admin_accounts)
    - [list_publishing_destinations](#list_publishing_destinations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_threat_intel_sets](#list_threat_intel_sets)
    - [start_monitoring_members](#start_monitoring_members)
    - [stop_monitoring_members](#stop_monitoring_members)
    - [tag_resource](#tag_resource)
    - [unarchive_findings](#unarchive_findings)
    - [untag_resource](#untag_resource)
    - [update_detector](#update_detector)
    - [update_filter](#update_filter)
    - [update_findings_feedback](#update_findings_feedback)
    - [update_ip_set](#update_ip_set)
    - [update_member_detectors](#update_member_detectors)
    - [update_organization_configuration](#update_organization_configuration)
    - [update_publishing_destination](#update_publishing_destination)
    - [update_threat_intel_set](#update_threat_intel_set)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)

## GuardDutyClient

Type annotations for `boto3.client("guardduty")`

Can be used directly:

```python
from mypy_boto3_guardduty.client import GuardDutyClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_guardduty.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerErrorException`


## Methods


### accept_invitation

Type annotations for `boto3.client("guardduty").accept_invitation` method.

[Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)

```python
def accept_invitation(
    self,
    DetectorId: str,
    MasterId: str,
    InvitationId: str
) -> Dict[str, Any]:
    pass
```

### archive_findings

Type annotations for `boto3.client("guardduty").archive_findings` method.

[Client.archive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.archive_findings)

```python
def archive_findings(
    self,
    DetectorId: str,
    FindingIds: List[str]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("guardduty").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_detector

Type annotations for `boto3.client("guardduty").create_detector` method.

[Client.create_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_detector)

```python
def create_detector(
    self,
    Enable: bool,
    ClientToken: str = None,
    FindingPublishingFrequency: FindingPublishingFrequency = None,
    DataSources: DataSourceConfigurationsTypeDef = None,
    Tags: Dict[str, str] = None
) -> CreateDetectorResponseTypeDef:
    pass
```

### create_filter

Type annotations for `boto3.client("guardduty").create_filter` method.

[Client.create_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_filter)

```python
def create_filter(
    self,
    DetectorId: str,
    Name: str,
    FindingCriteria: "FindingCriteriaTypeDef",
    Description: str = None,
    Action: FilterAction = None,
    Rank: int = None,
    ClientToken: str = None,
    Tags: Dict[str, str] = None
) -> CreateFilterResponseTypeDef:
    pass
```

### create_ip_set

Type annotations for `boto3.client("guardduty").create_ip_set` method.

[Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)

```python
def create_ip_set(
    self,
    DetectorId: str,
    Name: str,
    Format: IpSetFormat,
    Location: str,
    Activate: bool,
    ClientToken: str = None,
    Tags: Dict[str, str] = None
) -> CreateIPSetResponseTypeDef:
    pass
```

### create_members

Type annotations for `boto3.client("guardduty").create_members` method.

[Client.create_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_members)

```python
def create_members(
    self,
    DetectorId: str,
    AccountDetails: List[AccountDetailTypeDef]
) -> CreateMembersResponseTypeDef:
    pass
```

### create_publishing_destination

Type annotations for `boto3.client("guardduty").create_publishing_destination` method.

[Client.create_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)

```python
def create_publishing_destination(
    self,
    DetectorId: str,
    DestinationType: DestinationType,
    DestinationProperties: "DestinationPropertiesTypeDef",
    ClientToken: str = None
) -> CreatePublishingDestinationResponseTypeDef:
    pass
```

### create_sample_findings

Type annotations for `boto3.client("guardduty").create_sample_findings` method.

[Client.create_sample_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)

```python
def create_sample_findings(
    self,
    DetectorId: str,
    FindingTypes: List[str] = None
) -> Dict[str, Any]:
    pass
```

### create_threat_intel_set

Type annotations for `boto3.client("guardduty").create_threat_intel_set` method.

[Client.create_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)

```python
def create_threat_intel_set(
    self,
    DetectorId: str,
    Name: str,
    Format: ThreatIntelSetFormat,
    Location: str,
    Activate: bool,
    ClientToken: str = None,
    Tags: Dict[str, str] = None
) -> CreateThreatIntelSetResponseTypeDef:
    pass
```

### decline_invitations

Type annotations for `boto3.client("guardduty").decline_invitations` method.

[Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)

```python
def decline_invitations(
    self,
    AccountIds: List[str]
) -> DeclineInvitationsResponseTypeDef:
    pass
```

### delete_detector

Type annotations for `boto3.client("guardduty").delete_detector` method.

[Client.delete_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_detector)

```python
def delete_detector(
    self,
    DetectorId: str
) -> Dict[str, Any]:
    pass
```

### delete_filter

Type annotations for `boto3.client("guardduty").delete_filter` method.

[Client.delete_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_filter)

```python
def delete_filter(
    self,
    DetectorId: str,
    FilterName: str
) -> Dict[str, Any]:
    pass
```

### delete_invitations

Type annotations for `boto3.client("guardduty").delete_invitations` method.

[Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)

```python
def delete_invitations(
    self,
    AccountIds: List[str]
) -> DeleteInvitationsResponseTypeDef:
    pass
```

### delete_ip_set

Type annotations for `boto3.client("guardduty").delete_ip_set` method.

[Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)

```python
def delete_ip_set(
    self,
    DetectorId: str,
    IpSetId: str
) -> Dict[str, Any]:
    pass
```

### delete_members

Type annotations for `boto3.client("guardduty").delete_members` method.

[Client.delete_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_members)

```python
def delete_members(
    self,
    DetectorId: str,
    AccountIds: List[str]
) -> DeleteMembersResponseTypeDef:
    pass
```

### delete_publishing_destination

Type annotations for `boto3.client("guardduty").delete_publishing_destination` method.

[Client.delete_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)

```python
def delete_publishing_destination(
    self,
    DetectorId: str,
    DestinationId: str
) -> Dict[str, Any]:
    pass
```

### delete_threat_intel_set

Type annotations for `boto3.client("guardduty").delete_threat_intel_set` method.

[Client.delete_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)

```python
def delete_threat_intel_set(
    self,
    DetectorId: str,
    ThreatIntelSetId: str
) -> Dict[str, Any]:
    pass
```

### describe_organization_configuration

Type annotations for `boto3.client("guardduty").describe_organization_configuration` method.

[Client.describe_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.describe_organization_configuration)

```python
def describe_organization_configuration(
    self,
    DetectorId: str
) -> DescribeOrganizationConfigurationResponseTypeDef:
    pass
```

### describe_publishing_destination

Type annotations for `boto3.client("guardduty").describe_publishing_destination` method.

[Client.describe_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)

```python
def describe_publishing_destination(
    self,
    DetectorId: str,
    DestinationId: str
) -> DescribePublishingDestinationResponseTypeDef:
    pass
```

### disable_organization_admin_account

Type annotations for `boto3.client("guardduty").disable_organization_admin_account` method.

[Client.disable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disable_organization_admin_account)

```python
def disable_organization_admin_account(
    self,
    AdminAccountId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_from_master_account

Type annotations for `boto3.client("guardduty").disassociate_from_master_account` method.

[Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)

```python
def disassociate_from_master_account(
    self,
    DetectorId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_members

Type annotations for `boto3.client("guardduty").disassociate_members` method.

[Client.disassociate_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)

```python
def disassociate_members(
    self,
    DetectorId: str,
    AccountIds: List[str]
) -> DisassociateMembersResponseTypeDef:
    pass
```

### enable_organization_admin_account

Type annotations for `boto3.client("guardduty").enable_organization_admin_account` method.

[Client.enable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.enable_organization_admin_account)

```python
def enable_organization_admin_account(
    self,
    AdminAccountId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("guardduty").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)

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

### get_detector

Type annotations for `boto3.client("guardduty").get_detector` method.

[Client.get_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_detector)

```python
def get_detector(
    self,
    DetectorId: str
) -> GetDetectorResponseTypeDef:
    pass
```

### get_filter

Type annotations for `boto3.client("guardduty").get_filter` method.

[Client.get_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_filter)

```python
def get_filter(
    self,
    DetectorId: str,
    FilterName: str
) -> GetFilterResponseTypeDef:
    pass
```

### get_findings

Type annotations for `boto3.client("guardduty").get_findings` method.

[Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_findings)

```python
def get_findings(
    self,
    DetectorId: str,
    FindingIds: List[str],
    SortCriteria: SortCriteriaTypeDef = None
) -> GetFindingsResponseTypeDef:
    pass
```

### get_findings_statistics

Type annotations for `boto3.client("guardduty").get_findings_statistics` method.

[Client.get_findings_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)

```python
def get_findings_statistics(
    self,
    DetectorId: str,
    FindingStatisticTypes: List[FindingStatisticType],
    FindingCriteria: "FindingCriteriaTypeDef" = None
) -> GetFindingsStatisticsResponseTypeDef:
    pass
```

### get_invitations_count

Type annotations for `boto3.client("guardduty").get_invitations_count` method.

[Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)

```python
def get_invitations_count(
    self
) -> GetInvitationsCountResponseTypeDef:
    pass
```

### get_ip_set

Type annotations for `boto3.client("guardduty").get_ip_set` method.

[Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)

```python
def get_ip_set(
    self,
    DetectorId: str,
    IpSetId: str
) -> GetIPSetResponseTypeDef:
    pass
```

### get_master_account

Type annotations for `boto3.client("guardduty").get_master_account` method.

[Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_master_account)

```python
def get_master_account(
    self,
    DetectorId: str
) -> GetMasterAccountResponseTypeDef:
    pass
```

### get_member_detectors

Type annotations for `boto3.client("guardduty").get_member_detectors` method.

[Client.get_member_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_member_detectors)

```python
def get_member_detectors(
    self,
    DetectorId: str,
    AccountIds: List[str]
) -> GetMemberDetectorsResponseTypeDef:
    pass
```

### get_members

Type annotations for `boto3.client("guardduty").get_members` method.

[Client.get_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_members)

```python
def get_members(
    self,
    DetectorId: str,
    AccountIds: List[str]
) -> GetMembersResponseTypeDef:
    pass
```

### get_threat_intel_set

Type annotations for `boto3.client("guardduty").get_threat_intel_set` method.

[Client.get_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)

```python
def get_threat_intel_set(
    self,
    DetectorId: str,
    ThreatIntelSetId: str
) -> GetThreatIntelSetResponseTypeDef:
    pass
```

### get_usage_statistics

Type annotations for `boto3.client("guardduty").get_usage_statistics` method.

[Client.get_usage_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_usage_statistics)

```python
def get_usage_statistics(
    self,
    DetectorId: str,
    UsageStatisticType: UsageStatisticType,
    UsageCriteria: UsageCriteriaTypeDef,
    Unit: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetUsageStatisticsResponseTypeDef:
    pass
```

### invite_members

Type annotations for `boto3.client("guardduty").invite_members` method.

[Client.invite_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.invite_members)

```python
def invite_members(
    self,
    DetectorId: str,
    AccountIds: List[str],
    DisableEmailNotification: bool = None,
    Message: str = None
) -> InviteMembersResponseTypeDef:
    pass
```

### list_detectors

Type annotations for `boto3.client("guardduty").list_detectors` method.

[Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_detectors)

```python
def list_detectors(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDetectorsResponseTypeDef:
    pass
```

### list_filters

Type annotations for `boto3.client("guardduty").list_filters` method.

[Client.list_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_filters)

```python
def list_filters(
    self,
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFiltersResponseTypeDef:
    pass
```

### list_findings

Type annotations for `boto3.client("guardduty").list_findings` method.

[Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_findings)

```python
def list_findings(
    self,
    DetectorId: str,
    FindingCriteria: "FindingCriteriaTypeDef" = None,
    SortCriteria: SortCriteriaTypeDef = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFindingsResponseTypeDef:
    pass
```

### list_invitations

Type annotations for `boto3.client("guardduty").list_invitations` method.

[Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_invitations)

```python
def list_invitations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInvitationsResponseTypeDef:
    pass
```

### list_ip_sets

Type annotations for `boto3.client("guardduty").list_ip_sets` method.

[Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)

```python
def list_ip_sets(
    self,
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListIPSetsResponseTypeDef:
    pass
```

### list_members

Type annotations for `boto3.client("guardduty").list_members` method.

[Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_members)

```python
def list_members(
    self,
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None,
    OnlyAssociated: str = None
) -> ListMembersResponseTypeDef:
    pass
```

### list_organization_admin_accounts

Type annotations for `boto3.client("guardduty").list_organization_admin_accounts` method.

[Client.list_organization_admin_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_organization_admin_accounts)

```python
def list_organization_admin_accounts(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListOrganizationAdminAccountsResponseTypeDef:
    pass
```

### list_publishing_destinations

Type annotations for `boto3.client("guardduty").list_publishing_destinations` method.

[Client.list_publishing_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)

```python
def list_publishing_destinations(
    self,
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPublishingDestinationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("guardduty").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_threat_intel_sets

Type annotations for `boto3.client("guardduty").list_threat_intel_sets` method.

[Client.list_threat_intel_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)

```python
def list_threat_intel_sets(
    self,
    DetectorId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListThreatIntelSetsResponseTypeDef:
    pass
```

### start_monitoring_members

Type annotations for `boto3.client("guardduty").start_monitoring_members` method.

[Client.start_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)

```python
def start_monitoring_members(
    self,
    DetectorId: str,
    AccountIds: List[str]
) -> StartMonitoringMembersResponseTypeDef:
    pass
```

### stop_monitoring_members

Type annotations for `boto3.client("guardduty").stop_monitoring_members` method.

[Client.stop_monitoring_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)

```python
def stop_monitoring_members(
    self,
    DetectorId: str,
    AccountIds: List[str]
) -> StopMonitoringMembersResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("guardduty").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### unarchive_findings

Type annotations for `boto3.client("guardduty").unarchive_findings` method.

[Client.unarchive_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)

```python
def unarchive_findings(
    self,
    DetectorId: str,
    FindingIds: List[str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("guardduty").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_detector

Type annotations for `boto3.client("guardduty").update_detector` method.

[Client.update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_detector)

```python
def update_detector(
    self,
    DetectorId: str,
    Enable: bool = None,
    FindingPublishingFrequency: FindingPublishingFrequency = None,
    DataSources: DataSourceConfigurationsTypeDef = None
) -> Dict[str, Any]:
    pass
```

### update_filter

Type annotations for `boto3.client("guardduty").update_filter` method.

[Client.update_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_filter)

```python
def update_filter(
    self,
    DetectorId: str,
    FilterName: str,
    Description: str = None,
    Action: FilterAction = None,
    Rank: int = None,
    FindingCriteria: "FindingCriteriaTypeDef" = None
) -> UpdateFilterResponseTypeDef:
    pass
```

### update_findings_feedback

Type annotations for `boto3.client("guardduty").update_findings_feedback` method.

[Client.update_findings_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)

```python
def update_findings_feedback(
    self,
    DetectorId: str,
    FindingIds: List[str],
    Feedback: Feedback,
    Comments: str = None
) -> Dict[str, Any]:
    pass
```

### update_ip_set

Type annotations for `boto3.client("guardduty").update_ip_set` method.

[Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)

```python
def update_ip_set(
    self,
    DetectorId: str,
    IpSetId: str,
    Name: str = None,
    Location: str = None,
    Activate: bool = None
) -> Dict[str, Any]:
    pass
```

### update_member_detectors

Type annotations for `boto3.client("guardduty").update_member_detectors` method.

[Client.update_member_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_member_detectors)

```python
def update_member_detectors(
    self,
    DetectorId: str,
    AccountIds: List[str],
    DataSources: DataSourceConfigurationsTypeDef = None
) -> UpdateMemberDetectorsResponseTypeDef:
    pass
```

### update_organization_configuration

Type annotations for `boto3.client("guardduty").update_organization_configuration` method.

[Client.update_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_organization_configuration)

```python
def update_organization_configuration(
    self,
    DetectorId: str,
    AutoEnable: bool,
    DataSources: OrganizationDataSourceConfigurationsTypeDef = None
) -> Dict[str, Any]:
    pass
```

### update_publishing_destination

Type annotations for `boto3.client("guardduty").update_publishing_destination` method.

[Client.update_publishing_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)

```python
def update_publishing_destination(
    self,
    DetectorId: str,
    DestinationId: str,
    DestinationProperties: "DestinationPropertiesTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_threat_intel_set

Type annotations for `boto3.client("guardduty").update_threat_intel_set` method.

[Client.update_threat_intel_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)

```python
def update_threat_intel_set(
    self,
    DetectorId: str,
    ThreatIntelSetId: str,
    Name: str = None,
    Location: str = None,
    Activate: bool = None
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListDetectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDetectorsPaginatorName
) -> ListDetectorsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFiltersPaginatorName
) -> ListFiltersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFindingsPaginatorName
) -> ListFindingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListIPSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListIPSetsPaginatorName
) -> ListIPSetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInvitationsPaginatorName
) -> ListInvitationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMembersPaginatorName
) -> ListMembersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListOrganizationAdminAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListOrganizationAdminAccounts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOrganizationAdminAccountsPaginatorName
) -> ListOrganizationAdminAccountsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("guardduty").get_paginator` method.

[Paginator.ListThreatIntelSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListThreatIntelSetsPaginatorName
) -> ListThreatIntelSetsPaginator:
    pass
```