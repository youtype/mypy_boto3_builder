# Literals for boto3 Appflow module

> [Index](../index.md) > [Appflow](./index.md) > Literals

Auto-generated documentation for [Appflow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow)
type annotations stubs module [mypy_boto3_appflow](https://pypi.org/project/mypy-boto3-appflow/).

- [Literals for boto3 Appflow module](#literals-for-boto3-appflow-module)
  - [AggregationType](#aggregationtype)
  - [AmplitudeConnectorOperator](#amplitudeconnectoroperator)
  - [ConnectionMode](#connectionmode)
  - [ConnectorType](#connectortype)
  - [DataPullMode](#datapullmode)
  - [DatadogConnectorOperator](#datadogconnectoroperator)
  - [DynatraceConnectorOperator](#dynatraceconnectoroperator)
  - [ExecutionStatus](#executionstatus)
  - [FileType](#filetype)
  - [FlowStatus](#flowstatus)
  - [GoogleAnalyticsConnectorOperator](#googleanalyticsconnectoroperator)
  - [InforNexusConnectorOperator](#infornexusconnectoroperator)
  - [MarketoConnectorOperator](#marketoconnectoroperator)
  - [Operator](#operator)
  - [OperatorPropertiesKeys](#operatorpropertieskeys)
  - [PrefixFormat](#prefixformat)
  - [PrefixType](#prefixtype)
  - [S3ConnectorOperator](#s3connectoroperator)
  - [SalesforceConnectorOperator](#salesforceconnectoroperator)
  - [ScheduleFrequencyType](#schedulefrequencytype)
  - [ServiceNowConnectorOperator](#servicenowconnectoroperator)
  - [SingularConnectorOperator](#singularconnectoroperator)
  - [SlackConnectorOperator](#slackconnectoroperator)
  - [TaskType](#tasktype)
  - [TrendmicroConnectorOperator](#trendmicroconnectoroperator)
  - [TriggerType](#triggertype)
  - [VeevaConnectorOperator](#veevaconnectoroperator)
  - [WriteOperationType](#writeoperationtype)
  - [ZendeskConnectorOperator](#zendeskconnectoroperator)

## AggregationType

```python
from mypy_boto3_appflow.literals import AggregationType
```

Values:

- `None`
- `SingleFile`

## AmplitudeConnectorOperator

```python
from mypy_boto3_appflow.literals import AmplitudeConnectorOperator
```

Values:

- `BETWEEN`

## ConnectionMode

```python
from mypy_boto3_appflow.literals import ConnectionMode
```

Values:

- `Private`
- `Public`

## ConnectorType

```python
from mypy_boto3_appflow.literals import ConnectorType
```

Values:

- `Amplitude`
- `CustomerProfiles`
- `Datadog`
- `Dynatrace`
- `EventBridge`
- `Googleanalytics`
- `Honeycode`
- `Infornexus`
- `LookoutMetrics`
- `Marketo`
- `Redshift`
- `S3`
- `Salesforce`
- `Servicenow`
- `Singular`
- `Slack`
- `Snowflake`
- `Trendmicro`
- `Upsolver`
- `Veeva`
- `Zendesk`

## DataPullMode

```python
from mypy_boto3_appflow.literals import DataPullMode
```

Values:

- `Complete`
- `Incremental`

## DatadogConnectorOperator

```python
from mypy_boto3_appflow.literals import DatadogConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## DynatraceConnectorOperator

```python
from mypy_boto3_appflow.literals import DynatraceConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## ExecutionStatus

```python
from mypy_boto3_appflow.literals import ExecutionStatus
```

Values:

- `Error`
- `InProgress`
- `Successful`

## FileType

```python
from mypy_boto3_appflow.literals import FileType
```

Values:

- `CSV`
- `JSON`
- `PARQUET`

## FlowStatus

```python
from mypy_boto3_appflow.literals import FlowStatus
```

Values:

- `Active`
- `Deleted`
- `Deprecated`
- `Draft`
- `Errored`
- `Suspended`

## GoogleAnalyticsConnectorOperator

```python
from mypy_boto3_appflow.literals import GoogleAnalyticsConnectorOperator
```

Values:

- `BETWEEN`
- `PROJECTION`

## InforNexusConnectorOperator

```python
from mypy_boto3_appflow.literals import InforNexusConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## MarketoConnectorOperator

```python
from mypy_boto3_appflow.literals import MarketoConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `GREATER_THAN`
- `LESS_THAN`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## Operator

```python
from mypy_boto3_appflow.literals import Operator
```

Values:

- `ADDITION`
- `BETWEEN`
- `CONTAINS`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## OperatorPropertiesKeys

```python
from mypy_boto3_appflow.literals import OperatorPropertiesKeys
```

Values:

- `CONCAT_FORMAT`
- `DATA_TYPE`
- `DESTINATION_DATA_TYPE`
- `LOWER_BOUND`
- `MASK_LENGTH`
- `MASK_VALUE`
- `MATH_OPERATION_FIELDS_ORDER`
- `SOURCE_DATA_TYPE`
- `SUBFIELD_CATEGORY_MAP`
- `TRUNCATE_LENGTH`
- `UPPER_BOUND`
- `VALIDATION_ACTION`
- `VALUE`
- `VALUES`

## PrefixFormat

```python
from mypy_boto3_appflow.literals import PrefixFormat
```

Values:

- `DAY`
- `HOUR`
- `MINUTE`
- `MONTH`
- `YEAR`

## PrefixType

```python
from mypy_boto3_appflow.literals import PrefixType
```

Values:

- `FILENAME`
- `PATH`
- `PATH_AND_FILENAME`

## S3ConnectorOperator

```python
from mypy_boto3_appflow.literals import S3ConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## SalesforceConnectorOperator

```python
from mypy_boto3_appflow.literals import SalesforceConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `CONTAINS`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## ScheduleFrequencyType

```python
from mypy_boto3_appflow.literals import ScheduleFrequencyType
```

Values:

- `BYMINUTE`
- `DAILY`
- `HOURLY`
- `MONTHLY`
- `ONCE`
- `WEEKLY`

## ServiceNowConnectorOperator

```python
from mypy_boto3_appflow.literals import ServiceNowConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `CONTAINS`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## SingularConnectorOperator

```python
from mypy_boto3_appflow.literals import SingularConnectorOperator
```

Values:

- `ADDITION`
- `DIVISION`
- `EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## SlackConnectorOperator

```python
from mypy_boto3_appflow.literals import SlackConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## TaskType

```python
from mypy_boto3_appflow.literals import TaskType
```

Values:

- `Arithmetic`
- `Filter`
- `Map`
- `Mask`
- `Merge`
- `Truncate`
- `Validate`

## TrendmicroConnectorOperator

```python
from mypy_boto3_appflow.literals import TrendmicroConnectorOperator
```

Values:

- `ADDITION`
- `DIVISION`
- `EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## TriggerType

```python
from mypy_boto3_appflow.literals import TriggerType
```

Values:

- `Event`
- `OnDemand`
- `Scheduled`

## VeevaConnectorOperator

```python
from mypy_boto3_appflow.literals import VeevaConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `CONTAINS`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## WriteOperationType

```python
from mypy_boto3_appflow.literals import WriteOperationType
```

Values:

- `INSERT`
- `UPDATE`
- `UPSERT`

## ZendeskConnectorOperator

```python
from mypy_boto3_appflow.literals import ZendeskConnectorOperator
```

Values:

- `ADDITION`
- `DIVISION`
- `GREATER_THAN`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`
