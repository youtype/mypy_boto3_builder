# Literals for boto3 SecurityHub module

> [Index](../index.md) > [SecurityHub](./index.md) > Literals

Auto-generated documentation for [SecurityHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html#SecurityHub)
type annotations stubs module [mypy_boto3_securityhub](https://pypi.org/project/mypy-boto3-securityhub/).

- [Literals for boto3 SecurityHub module](#literals-for-boto3-securityhub-module)
  - [AdminStatus](#adminstatus)
  - [AwsIamAccessKeyStatus](#awsiamaccesskeystatus)
  - [ComplianceStatus](#compliancestatus)
  - [ControlStatus](#controlstatus)
  - [DateRangeUnit](#daterangeunit)
  - [GetEnabledStandardsPaginatorName](#getenabledstandardspaginatorname)
  - [GetFindingsPaginatorName](#getfindingspaginatorname)
  - [GetInsightsPaginatorName](#getinsightspaginatorname)
  - [IntegrationType](#integrationtype)
  - [ListEnabledProductsForImportPaginatorName](#listenabledproductsforimportpaginatorname)
  - [ListInvitationsPaginatorName](#listinvitationspaginatorname)
  - [ListMembersPaginatorName](#listmemberspaginatorname)
  - [MalwareState](#malwarestate)
  - [MalwareType](#malwaretype)
  - [MapFilterComparison](#mapfiltercomparison)
  - [NetworkDirection](#networkdirection)
  - [Partition](#partition)
  - [RecordState](#recordstate)
  - [SeverityLabel](#severitylabel)
  - [SeverityRating](#severityrating)
  - [SortOrder](#sortorder)
  - [StandardsStatus](#standardsstatus)
  - [StringFilterComparison](#stringfiltercomparison)
  - [ThreatIntelIndicatorCategory](#threatintelindicatorcategory)
  - [ThreatIntelIndicatorType](#threatintelindicatortype)
  - [VerificationState](#verificationstate)
  - [WorkflowState](#workflowstate)
  - [WorkflowStatus](#workflowstatus)

## AdminStatus

```python
from mypy_boto3_securityhub.literals import AdminStatus
```

Values:

- `DISABLE_IN_PROGRESS`
- `ENABLED`

## AwsIamAccessKeyStatus

```python
from mypy_boto3_securityhub.literals import AwsIamAccessKeyStatus
```

Values:

- `Active`
- `Inactive`

## ComplianceStatus

```python
from mypy_boto3_securityhub.literals import ComplianceStatus
```

Values:

- `FAILED`
- `NOT_AVAILABLE`
- `PASSED`
- `WARNING`

## ControlStatus

```python
from mypy_boto3_securityhub.literals import ControlStatus
```

Values:

- `DISABLED`
- `ENABLED`

## DateRangeUnit

```python
from mypy_boto3_securityhub.literals import DateRangeUnit
```

Values:

- `DAYS`

## GetEnabledStandardsPaginatorName

```python
from mypy_boto3_securityhub.literals import GetEnabledStandardsPaginatorName
```

Values:

- `get_enabled_standards`

## GetFindingsPaginatorName

```python
from mypy_boto3_securityhub.literals import GetFindingsPaginatorName
```

Values:

- `get_findings`

## GetInsightsPaginatorName

```python
from mypy_boto3_securityhub.literals import GetInsightsPaginatorName
```

Values:

- `get_insights`

## IntegrationType

```python
from mypy_boto3_securityhub.literals import IntegrationType
```

Values:

- `RECEIVE_FINDINGS_FROM_SECURITY_HUB`
- `SEND_FINDINGS_TO_SECURITY_HUB`
- `UPDATE_FINDINGS_IN_SECURITY_HUB`

## ListEnabledProductsForImportPaginatorName

```python
from mypy_boto3_securityhub.literals import ListEnabledProductsForImportPaginatorName
```

Values:

- `list_enabled_products_for_import`

## ListInvitationsPaginatorName

```python
from mypy_boto3_securityhub.literals import ListInvitationsPaginatorName
```

Values:

- `list_invitations`

## ListMembersPaginatorName

```python
from mypy_boto3_securityhub.literals import ListMembersPaginatorName
```

Values:

- `list_members`

## MalwareState

```python
from mypy_boto3_securityhub.literals import MalwareState
```

Values:

- `OBSERVED`
- `REMOVAL_FAILED`
- `REMOVED`

## MalwareType

```python
from mypy_boto3_securityhub.literals import MalwareType
```

Values:

- `ADWARE`
- `BLENDED_THREAT`
- `BOTNET_AGENT`
- `COIN_MINER`
- `EXPLOIT_KIT`
- `KEYLOGGER`
- `MACRO`
- `POTENTIALLY_UNWANTED`
- `RANSOMWARE`
- `REMOTE_ACCESS`
- `ROOTKIT`
- `SPYWARE`
- `TROJAN`
- `VIRUS`
- `WORM`

## MapFilterComparison

```python
from mypy_boto3_securityhub.literals import MapFilterComparison
```

Values:

- `EQUALS`
- `NOT_EQUALS`

## NetworkDirection

```python
from mypy_boto3_securityhub.literals import NetworkDirection
```

Values:

- `IN`
- `OUT`

## Partition

```python
from mypy_boto3_securityhub.literals import Partition
```

Values:

- `aws`
- `aws-cn`
- `aws-us-gov`

## RecordState

```python
from mypy_boto3_securityhub.literals import RecordState
```

Values:

- `ACTIVE`
- `ARCHIVED`

## SeverityLabel

```python
from mypy_boto3_securityhub.literals import SeverityLabel
```

Values:

- `CRITICAL`
- `HIGH`
- `INFORMATIONAL`
- `LOW`
- `MEDIUM`

## SeverityRating

```python
from mypy_boto3_securityhub.literals import SeverityRating
```

Values:

- `CRITICAL`
- `HIGH`
- `LOW`
- `MEDIUM`

## SortOrder

```python
from mypy_boto3_securityhub.literals import SortOrder
```

Values:

- `asc`
- `desc`

## StandardsStatus

```python
from mypy_boto3_securityhub.literals import StandardsStatus
```

Values:

- `DELETING`
- `FAILED`
- `INCOMPLETE`
- `PENDING`
- `READY`

## StringFilterComparison

```python
from mypy_boto3_securityhub.literals import StringFilterComparison
```

Values:

- `EQUALS`
- `NOT_EQUALS`
- `PREFIX`
- `PREFIX_NOT_EQUALS`

## ThreatIntelIndicatorCategory

```python
from mypy_boto3_securityhub.literals import ThreatIntelIndicatorCategory
```

Values:

- `BACKDOOR`
- `CARD_STEALER`
- `COMMAND_AND_CONTROL`
- `DROP_SITE`
- `EXPLOIT_SITE`
- `KEYLOGGER`

## ThreatIntelIndicatorType

```python
from mypy_boto3_securityhub.literals import ThreatIntelIndicatorType
```

Values:

- `DOMAIN`
- `EMAIL_ADDRESS`
- `HASH_MD5`
- `HASH_SHA1`
- `HASH_SHA256`
- `HASH_SHA512`
- `IPV4_ADDRESS`
- `IPV6_ADDRESS`
- `MUTEX`
- `PROCESS`
- `URL`

## VerificationState

```python
from mypy_boto3_securityhub.literals import VerificationState
```

Values:

- `BENIGN_POSITIVE`
- `FALSE_POSITIVE`
- `TRUE_POSITIVE`
- `UNKNOWN`

## WorkflowState

```python
from mypy_boto3_securityhub.literals import WorkflowState
```

Values:

- `ASSIGNED`
- `DEFERRED`
- `IN_PROGRESS`
- `NEW`
- `RESOLVED`

## WorkflowStatus

```python
from mypy_boto3_securityhub.literals import WorkflowStatus
```

Values:

- `NEW`
- `NOTIFIED`
- `RESOLVED`
- `SUPPRESSED`
