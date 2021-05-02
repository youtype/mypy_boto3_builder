# Literals for boto3 ApplicationDiscoveryService module

> [Index](../index.md) > [ApplicationDiscoveryService](./index.md) > Literals

Auto-generated documentation for [ApplicationDiscoveryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html#ApplicationDiscoveryService)
type annotations stubs module [mypy_boto3_discovery](https://pypi.org/project/mypy-boto3-discovery/).

- [Literals for boto3 ApplicationDiscoveryService module](#literals-for-boto3-applicationdiscoveryservice-module)
  - [AgentStatus](#agentstatus)
  - [BatchDeleteImportDataErrorCode](#batchdeleteimportdataerrorcode)
  - [ConfigurationItemType](#configurationitemtype)
  - [ContinuousExportStatus](#continuousexportstatus)
  - [DataSource](#datasource)
  - [DescribeAgentsPaginatorName](#describeagentspaginatorname)
  - [DescribeContinuousExportsPaginatorName](#describecontinuousexportspaginatorname)
  - [DescribeExportConfigurationsPaginatorName](#describeexportconfigurationspaginatorname)
  - [DescribeExportTasksPaginatorName](#describeexporttaskspaginatorname)
  - [DescribeTagsPaginatorName](#describetagspaginatorname)
  - [ExportDataFormat](#exportdataformat)
  - [ExportStatus](#exportstatus)
  - [ImportStatus](#importstatus)
  - [ImportTaskFilterName](#importtaskfiltername)
  - [ListConfigurationsPaginatorName](#listconfigurationspaginatorname)
  - [orderString](#orderstring)

## AgentStatus

```python
from mypy_boto3_discovery.literals import AgentStatus
```

Values:

- `BLACKLISTED`
- `HEALTHY`
- `RUNNING`
- `SHUTDOWN`
- `UNHEALTHY`
- `UNKNOWN`

## BatchDeleteImportDataErrorCode

```python
from mypy_boto3_discovery.literals import BatchDeleteImportDataErrorCode
```

Values:

- `INTERNAL_SERVER_ERROR`
- `NOT_FOUND`
- `OVER_LIMIT`

## ConfigurationItemType

```python
from mypy_boto3_discovery.literals import ConfigurationItemType
```

Values:

- `APPLICATION`
- `CONNECTION`
- `PROCESS`
- `SERVER`

## ContinuousExportStatus

```python
from mypy_boto3_discovery.literals import ContinuousExportStatus
```

Values:

- `ACTIVE`
- `ERROR`
- `INACTIVE`
- `START_FAILED`
- `START_IN_PROGRESS`
- `STOP_FAILED`
- `STOP_IN_PROGRESS`

## DataSource

```python
from mypy_boto3_discovery.literals import DataSource
```

Values:

- `AGENT`

## DescribeAgentsPaginatorName

```python
from mypy_boto3_discovery.literals import DescribeAgentsPaginatorName
```

Values:

- `describe_agents`

## DescribeContinuousExportsPaginatorName

```python
from mypy_boto3_discovery.literals import DescribeContinuousExportsPaginatorName
```

Values:

- `describe_continuous_exports`

## DescribeExportConfigurationsPaginatorName

```python
from mypy_boto3_discovery.literals import DescribeExportConfigurationsPaginatorName
```

Values:

- `describe_export_configurations`

## DescribeExportTasksPaginatorName

```python
from mypy_boto3_discovery.literals import DescribeExportTasksPaginatorName
```

Values:

- `describe_export_tasks`

## DescribeTagsPaginatorName

```python
from mypy_boto3_discovery.literals import DescribeTagsPaginatorName
```

Values:

- `describe_tags`

## ExportDataFormat

```python
from mypy_boto3_discovery.literals import ExportDataFormat
```

Values:

- `CSV`
- `GRAPHML`

## ExportStatus

```python
from mypy_boto3_discovery.literals import ExportStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`

## ImportStatus

```python
from mypy_boto3_discovery.literals import ImportStatus
```

Values:

- `DELETE_COMPLETE`
- `DELETE_FAILED`
- `DELETE_FAILED_LIMIT_EXCEEDED`
- `DELETE_IN_PROGRESS`
- `IMPORT_COMPLETE`
- `IMPORT_COMPLETE_WITH_ERRORS`
- `IMPORT_FAILED`
- `IMPORT_FAILED_RECORD_LIMIT_EXCEEDED`
- `IMPORT_FAILED_SERVER_LIMIT_EXCEEDED`
- `IMPORT_IN_PROGRESS`
- `INTERNAL_ERROR`

## ImportTaskFilterName

```python
from mypy_boto3_discovery.literals import ImportTaskFilterName
```

Values:

- `IMPORT_TASK_ID`
- `NAME`
- `STATUS`

## ListConfigurationsPaginatorName

```python
from mypy_boto3_discovery.literals import ListConfigurationsPaginatorName
```

Values:

- `list_configurations`

## orderString

```python
from mypy_boto3_discovery.literals import orderString
```

Values:

- `ASC`
- `DESC`
