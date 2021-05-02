# Literals for boto3 GuardDuty module

> [Index](../index.md) > [GuardDuty](./index.md) > Literals

Auto-generated documentation for [GuardDuty](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty)
type annotations stubs module [mypy_boto3_guardduty](https://pypi.org/project/mypy-boto3-guardduty/).

- [Literals for boto3 GuardDuty module](#literals-for-boto3-guardduty-module)
  - [AdminStatus](#adminstatus)
  - [DataSource](#datasource)
  - [DataSourceStatus](#datasourcestatus)
  - [DestinationType](#destinationtype)
  - [DetectorStatus](#detectorstatus)
  - [Feedback](#feedback)
  - [FilterAction](#filteraction)
  - [FindingPublishingFrequency](#findingpublishingfrequency)
  - [FindingStatisticType](#findingstatistictype)
  - [IpSetFormat](#ipsetformat)
  - [IpSetStatus](#ipsetstatus)
  - [ListDetectorsPaginatorName](#listdetectorspaginatorname)
  - [ListFiltersPaginatorName](#listfilterspaginatorname)
  - [ListFindingsPaginatorName](#listfindingspaginatorname)
  - [ListIPSetsPaginatorName](#listipsetspaginatorname)
  - [ListInvitationsPaginatorName](#listinvitationspaginatorname)
  - [ListMembersPaginatorName](#listmemberspaginatorname)
  - [ListOrganizationAdminAccountsPaginatorName](#listorganizationadminaccountspaginatorname)
  - [ListThreatIntelSetsPaginatorName](#listthreatintelsetspaginatorname)
  - [OrderBy](#orderby)
  - [PublishingStatus](#publishingstatus)
  - [ThreatIntelSetFormat](#threatintelsetformat)
  - [ThreatIntelSetStatus](#threatintelsetstatus)
  - [UsageStatisticType](#usagestatistictype)

## AdminStatus

```python
from mypy_boto3_guardduty.literals import AdminStatus
```

Values:

- `DISABLE_IN_PROGRESS`
- `ENABLED`

## DataSource

```python
from mypy_boto3_guardduty.literals import DataSource
```

Values:

- `CLOUD_TRAIL`
- `DNS_LOGS`
- `FLOW_LOGS`
- `S3_LOGS`

## DataSourceStatus

```python
from mypy_boto3_guardduty.literals import DataSourceStatus
```

Values:

- `DISABLED`
- `ENABLED`

## DestinationType

```python
from mypy_boto3_guardduty.literals import DestinationType
```

Values:

- `S3`

## DetectorStatus

```python
from mypy_boto3_guardduty.literals import DetectorStatus
```

Values:

- `DISABLED`
- `ENABLED`

## Feedback

```python
from mypy_boto3_guardduty.literals import Feedback
```

Values:

- `NOT_USEFUL`
- `USEFUL`

## FilterAction

```python
from mypy_boto3_guardduty.literals import FilterAction
```

Values:

- `ARCHIVE`
- `NOOP`

## FindingPublishingFrequency

```python
from mypy_boto3_guardduty.literals import FindingPublishingFrequency
```

Values:

- `FIFTEEN_MINUTES`
- `ONE_HOUR`
- `SIX_HOURS`

## FindingStatisticType

```python
from mypy_boto3_guardduty.literals import FindingStatisticType
```

Values:

- `COUNT_BY_SEVERITY`

## IpSetFormat

```python
from mypy_boto3_guardduty.literals import IpSetFormat
```

Values:

- `ALIEN_VAULT`
- `FIRE_EYE`
- `OTX_CSV`
- `PROOF_POINT`
- `STIX`
- `TXT`

## IpSetStatus

```python
from mypy_boto3_guardduty.literals import IpSetStatus
```

Values:

- `ACTIVATING`
- `ACTIVE`
- `DEACTIVATING`
- `DELETE_PENDING`
- `DELETED`
- `ERROR`
- `INACTIVE`

## ListDetectorsPaginatorName

```python
from mypy_boto3_guardduty.literals import ListDetectorsPaginatorName
```

Values:

- `list_detectors`

## ListFiltersPaginatorName

```python
from mypy_boto3_guardduty.literals import ListFiltersPaginatorName
```

Values:

- `list_filters`

## ListFindingsPaginatorName

```python
from mypy_boto3_guardduty.literals import ListFindingsPaginatorName
```

Values:

- `list_findings`

## ListIPSetsPaginatorName

```python
from mypy_boto3_guardduty.literals import ListIPSetsPaginatorName
```

Values:

- `list_ip_sets`

## ListInvitationsPaginatorName

```python
from mypy_boto3_guardduty.literals import ListInvitationsPaginatorName
```

Values:

- `list_invitations`

## ListMembersPaginatorName

```python
from mypy_boto3_guardduty.literals import ListMembersPaginatorName
```

Values:

- `list_members`

## ListOrganizationAdminAccountsPaginatorName

```python
from mypy_boto3_guardduty.literals import ListOrganizationAdminAccountsPaginatorName
```

Values:

- `list_organization_admin_accounts`

## ListThreatIntelSetsPaginatorName

```python
from mypy_boto3_guardduty.literals import ListThreatIntelSetsPaginatorName
```

Values:

- `list_threat_intel_sets`

## OrderBy

```python
from mypy_boto3_guardduty.literals import OrderBy
```

Values:

- `ASC`
- `DESC`

## PublishingStatus

```python
from mypy_boto3_guardduty.literals import PublishingStatus
```

Values:

- `PENDING_VERIFICATION`
- `PUBLISHING`
- `STOPPED`
- `UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY`

## ThreatIntelSetFormat

```python
from mypy_boto3_guardduty.literals import ThreatIntelSetFormat
```

Values:

- `ALIEN_VAULT`
- `FIRE_EYE`
- `OTX_CSV`
- `PROOF_POINT`
- `STIX`
- `TXT`

## ThreatIntelSetStatus

```python
from mypy_boto3_guardduty.literals import ThreatIntelSetStatus
```

Values:

- `ACTIVATING`
- `ACTIVE`
- `DEACTIVATING`
- `DELETE_PENDING`
- `DELETED`
- `ERROR`
- `INACTIVE`

## UsageStatisticType

```python
from mypy_boto3_guardduty.literals import UsageStatisticType
```

Values:

- `SUM_BY_ACCOUNT`
- `SUM_BY_DATA_SOURCE`
- `SUM_BY_RESOURCE`
- `TOP_RESOURCES`
