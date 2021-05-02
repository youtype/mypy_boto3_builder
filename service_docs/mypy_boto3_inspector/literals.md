# Literals for boto3 Inspector module

> [Index](../index.md) > [Inspector](./index.md) > Literals

Auto-generated documentation for [Inspector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector)
type annotations stubs module [mypy_boto3_inspector](https://pypi.org/project/mypy-boto3-inspector/).

- [Literals for boto3 Inspector module](#literals-for-boto3-inspector-module)
  - [AgentHealth](#agenthealth)
  - [AgentHealthCode](#agenthealthcode)
  - [AssessmentRunNotificationSnsStatusCode](#assessmentrunnotificationsnsstatuscode)
  - [AssessmentRunState](#assessmentrunstate)
  - [AssetType](#assettype)
  - [FailedItemErrorCode](#faileditemerrorcode)
  - [InspectorEvent](#inspectorevent)
  - [ListAssessmentRunAgentsPaginatorName](#listassessmentrunagentspaginatorname)
  - [ListAssessmentRunsPaginatorName](#listassessmentrunspaginatorname)
  - [ListAssessmentTargetsPaginatorName](#listassessmenttargetspaginatorname)
  - [ListAssessmentTemplatesPaginatorName](#listassessmenttemplatespaginatorname)
  - [ListEventSubscriptionsPaginatorName](#listeventsubscriptionspaginatorname)
  - [ListExclusionsPaginatorName](#listexclusionspaginatorname)
  - [ListFindingsPaginatorName](#listfindingspaginatorname)
  - [ListRulesPackagesPaginatorName](#listrulespackagespaginatorname)
  - [Locale](#locale)
  - [PreviewAgentsPaginatorName](#previewagentspaginatorname)
  - [PreviewStatus](#previewstatus)
  - [ReportFileFormat](#reportfileformat)
  - [ReportStatus](#reportstatus)
  - [ReportType](#reporttype)
  - [ScopeType](#scopetype)
  - [Severity](#severity)
  - [StopAction](#stopaction)

## AgentHealth

```python
from mypy_boto3_inspector.literals import AgentHealth
```

Values:

- `HEALTHY`
- `UNHEALTHY`
- `UNKNOWN`

## AgentHealthCode

```python
from mypy_boto3_inspector.literals import AgentHealthCode
```

Values:

- `IDLE`
- `RUNNING`
- `SHUTDOWN`
- `THROTTLED`
- `UNHEALTHY`
- `UNKNOWN`

## AssessmentRunNotificationSnsStatusCode

```python
from mypy_boto3_inspector.literals import AssessmentRunNotificationSnsStatusCode
```

Values:

- `ACCESS_DENIED`
- `INTERNAL_ERROR`
- `SUCCESS`
- `TOPIC_DOES_NOT_EXIST`

## AssessmentRunState

```python
from mypy_boto3_inspector.literals import AssessmentRunState
```

Values:

- `CANCELED`
- `COLLECTING_DATA`
- `COMPLETED`
- `COMPLETED_WITH_ERRORS`
- `CREATED`
- `DATA_COLLECTED`
- `ERROR`
- `EVALUATING_RULES`
- `FAILED`
- `START_DATA_COLLECTION_IN_PROGRESS`
- `START_DATA_COLLECTION_PENDING`
- `START_EVALUATING_RULES_PENDING`
- `STOP_DATA_COLLECTION_PENDING`

## AssetType

```python
from mypy_boto3_inspector.literals import AssetType
```

Values:

- `ec2-instance`

## FailedItemErrorCode

```python
from mypy_boto3_inspector.literals import FailedItemErrorCode
```

Values:

- `ACCESS_DENIED`
- `DUPLICATE_ARN`
- `INTERNAL_ERROR`
- `INVALID_ARN`
- `ITEM_DOES_NOT_EXIST`
- `LIMIT_EXCEEDED`

## InspectorEvent

```python
from mypy_boto3_inspector.literals import InspectorEvent
```

Values:

- `ASSESSMENT_RUN_COMPLETED`
- `ASSESSMENT_RUN_STARTED`
- `ASSESSMENT_RUN_STATE_CHANGED`
- `FINDING_REPORTED`
- `OTHER`

## ListAssessmentRunAgentsPaginatorName

```python
from mypy_boto3_inspector.literals import ListAssessmentRunAgentsPaginatorName
```

Values:

- `list_assessment_run_agents`

## ListAssessmentRunsPaginatorName

```python
from mypy_boto3_inspector.literals import ListAssessmentRunsPaginatorName
```

Values:

- `list_assessment_runs`

## ListAssessmentTargetsPaginatorName

```python
from mypy_boto3_inspector.literals import ListAssessmentTargetsPaginatorName
```

Values:

- `list_assessment_targets`

## ListAssessmentTemplatesPaginatorName

```python
from mypy_boto3_inspector.literals import ListAssessmentTemplatesPaginatorName
```

Values:

- `list_assessment_templates`

## ListEventSubscriptionsPaginatorName

```python
from mypy_boto3_inspector.literals import ListEventSubscriptionsPaginatorName
```

Values:

- `list_event_subscriptions`

## ListExclusionsPaginatorName

```python
from mypy_boto3_inspector.literals import ListExclusionsPaginatorName
```

Values:

- `list_exclusions`

## ListFindingsPaginatorName

```python
from mypy_boto3_inspector.literals import ListFindingsPaginatorName
```

Values:

- `list_findings`

## ListRulesPackagesPaginatorName

```python
from mypy_boto3_inspector.literals import ListRulesPackagesPaginatorName
```

Values:

- `list_rules_packages`

## Locale

```python
from mypy_boto3_inspector.literals import Locale
```

Values:

- `EN_US`

## PreviewAgentsPaginatorName

```python
from mypy_boto3_inspector.literals import PreviewAgentsPaginatorName
```

Values:

- `preview_agents`

## PreviewStatus

```python
from mypy_boto3_inspector.literals import PreviewStatus
```

Values:

- `COMPLETED`
- `WORK_IN_PROGRESS`

## ReportFileFormat

```python
from mypy_boto3_inspector.literals import ReportFileFormat
```

Values:

- `HTML`
- `PDF`

## ReportStatus

```python
from mypy_boto3_inspector.literals import ReportStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `WORK_IN_PROGRESS`

## ReportType

```python
from mypy_boto3_inspector.literals import ReportType
```

Values:

- `FINDING`
- `FULL`

## ScopeType

```python
from mypy_boto3_inspector.literals import ScopeType
```

Values:

- `INSTANCE_ID`
- `RULES_PACKAGE_ARN`

## Severity

```python
from mypy_boto3_inspector.literals import Severity
```

Values:

- `High`
- `Informational`
- `Low`
- `Medium`
- `Undefined`

## StopAction

```python
from mypy_boto3_inspector.literals import StopAction
```

Values:

- `SKIP_EVALUATION`
- `START_EVALUATION`
