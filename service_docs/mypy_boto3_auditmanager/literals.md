# Literals for boto3 AuditManager module

> [Index](../index.md) > [AuditManager](./index.md) > Literals

Auto-generated documentation for [AuditManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager)
type annotations stubs module [mypy_boto3_auditmanager](https://pypi.org/project/mypy-boto3-auditmanager/).

- [Literals for boto3 AuditManager module](#literals-for-boto3-auditmanager-module)
  - [AccountStatus](#accountstatus)
  - [ActionEnum](#actionenum)
  - [AssessmentReportDestinationType](#assessmentreportdestinationtype)
  - [AssessmentReportStatus](#assessmentreportstatus)
  - [AssessmentStatus](#assessmentstatus)
  - [ControlResponse](#controlresponse)
  - [ControlSetStatus](#controlsetstatus)
  - [ControlStatus](#controlstatus)
  - [ControlType](#controltype)
  - [DelegationStatus](#delegationstatus)
  - [FrameworkType](#frameworktype)
  - [KeywordInputType](#keywordinputtype)
  - [ObjectTypeEnum](#objecttypeenum)
  - [RoleType](#roletype)
  - [SettingAttribute](#settingattribute)
  - [SourceFrequency](#sourcefrequency)
  - [SourceSetUpOption](#sourcesetupoption)
  - [SourceType](#sourcetype)

## AccountStatus

```python
from mypy_boto3_auditmanager.literals import AccountStatus
```

Values:

- `ACTIVE`
- `INACTIVE`
- `PENDING_ACTIVATION`

## ActionEnum

```python
from mypy_boto3_auditmanager.literals import ActionEnum
```

Values:

- `ACTIVE`
- `CREATE`
- `DELETE`
- `IMPORT_EVIDENCE`
- `INACTIVE`
- `REVIEWED`
- `UNDER_REVIEW`
- `UPDATE_METADATA`

## AssessmentReportDestinationType

```python
from mypy_boto3_auditmanager.literals import AssessmentReportDestinationType
```

Values:

- `S3`

## AssessmentReportStatus

```python
from mypy_boto3_auditmanager.literals import AssessmentReportStatus
```

Values:

- `COMPLETE`
- `FAILED`
- `IN_PROGRESS`

## AssessmentStatus

```python
from mypy_boto3_auditmanager.literals import AssessmentStatus
```

Values:

- `ACTIVE`
- `INACTIVE`

## ControlResponse

```python
from mypy_boto3_auditmanager.literals import ControlResponse
```

Values:

- `AUTOMATE`
- `DEFER`
- `IGNORE`
- `MANUAL`

## ControlSetStatus

```python
from mypy_boto3_auditmanager.literals import ControlSetStatus
```

Values:

- `ACTIVE`
- `REVIEWED`
- `UNDER_REVIEW`

## ControlStatus

```python
from mypy_boto3_auditmanager.literals import ControlStatus
```

Values:

- `INACTIVE`
- `REVIEWED`
- `UNDER_REVIEW`

## ControlType

```python
from mypy_boto3_auditmanager.literals import ControlType
```

Values:

- `Custom`
- `Standard`

## DelegationStatus

```python
from mypy_boto3_auditmanager.literals import DelegationStatus
```

Values:

- `COMPLETE`
- `IN_PROGRESS`
- `UNDER_REVIEW`

## FrameworkType

```python
from mypy_boto3_auditmanager.literals import FrameworkType
```

Values:

- `Custom`
- `Standard`

## KeywordInputType

```python
from mypy_boto3_auditmanager.literals import KeywordInputType
```

Values:

- `SELECT_FROM_LIST`

## ObjectTypeEnum

```python
from mypy_boto3_auditmanager.literals import ObjectTypeEnum
```

Values:

- `ASSESSMENT`
- `ASSESSMENT_REPORT`
- `CONTROL`
- `CONTROL_SET`
- `DELEGATION`

## RoleType

```python
from mypy_boto3_auditmanager.literals import RoleType
```

Values:

- `PROCESS_OWNER`
- `RESOURCE_OWNER`

## SettingAttribute

```python
from mypy_boto3_auditmanager.literals import SettingAttribute
```

Values:

- `ALL`
- `DEFAULT_ASSESSMENT_REPORTS_DESTINATION`
- `DEFAULT_PROCESS_OWNERS`
- `IS_AWS_ORG_ENABLED`
- `SNS_TOPIC`

## SourceFrequency

```python
from mypy_boto3_auditmanager.literals import SourceFrequency
```

Values:

- `DAILY`
- `MONTHLY`
- `WEEKLY`

## SourceSetUpOption

```python
from mypy_boto3_auditmanager.literals import SourceSetUpOption
```

Values:

- `Procedural_Controls_Mapping`
- `System_Controls_Mapping`

## SourceType

```python
from mypy_boto3_auditmanager.literals import SourceType
```

Values:

- `AWS_API_Call`
- `AWS_Cloudtrail`
- `AWS_Config`
- `AWS_Security_Hub`
- `MANUAL`
