# Literals for boto3 Glue module

> [Index](../index.md) > [Glue](./index.md) > Literals

Auto-generated documentation for [Glue](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue)
type annotations stubs module [mypy_boto3_glue](https://pypi.org/project/mypy-boto3-glue/).

- [Literals for boto3 Glue module](#literals-for-boto3-glue-module)
  - [BackfillErrorCode](#backfillerrorcode)
  - [CatalogEncryptionMode](#catalogencryptionmode)
  - [CloudWatchEncryptionMode](#cloudwatchencryptionmode)
  - [ColumnStatisticsType](#columnstatisticstype)
  - [Comparator](#comparator)
  - [Compatibility](#compatibility)
  - [ConnectionPropertyKey](#connectionpropertykey)
  - [ConnectionType](#connectiontype)
  - [CrawlState](#crawlstate)
  - [CrawlerLineageSettings](#crawlerlineagesettings)
  - [CrawlerState](#crawlerstate)
  - [CsvHeaderOption](#csvheaderoption)
  - [DataFormat](#dataformat)
  - [DeleteBehavior](#deletebehavior)
  - [EnableHybridValues](#enablehybridvalues)
  - [ExistCondition](#existcondition)
  - [GetClassifiersPaginatorName](#getclassifierspaginatorname)
  - [GetConnectionsPaginatorName](#getconnectionspaginatorname)
  - [GetCrawlerMetricsPaginatorName](#getcrawlermetricspaginatorname)
  - [GetCrawlersPaginatorName](#getcrawlerspaginatorname)
  - [GetDatabasesPaginatorName](#getdatabasespaginatorname)
  - [GetDevEndpointsPaginatorName](#getdevendpointspaginatorname)
  - [GetJobRunsPaginatorName](#getjobrunspaginatorname)
  - [GetJobsPaginatorName](#getjobspaginatorname)
  - [GetPartitionIndexesPaginatorName](#getpartitionindexespaginatorname)
  - [GetPartitionsPaginatorName](#getpartitionspaginatorname)
  - [GetResourcePoliciesPaginatorName](#getresourcepoliciespaginatorname)
  - [GetSecurityConfigurationsPaginatorName](#getsecurityconfigurationspaginatorname)
  - [GetTableVersionsPaginatorName](#gettableversionspaginatorname)
  - [GetTablesPaginatorName](#gettablespaginatorname)
  - [GetTriggersPaginatorName](#gettriggerspaginatorname)
  - [GetUserDefinedFunctionsPaginatorName](#getuserdefinedfunctionspaginatorname)
  - [JobBookmarksEncryptionMode](#jobbookmarksencryptionmode)
  - [JobRunState](#jobrunstate)
  - [Language](#language)
  - [LastCrawlStatus](#lastcrawlstatus)
  - [ListRegistriesPaginatorName](#listregistriespaginatorname)
  - [ListSchemaVersionsPaginatorName](#listschemaversionspaginatorname)
  - [ListSchemasPaginatorName](#listschemaspaginatorname)
  - [Logical](#logical)
  - [LogicalOperator](#logicaloperator)
  - [MLUserDataEncryptionModeString](#mluserdataencryptionmodestring)
  - [NodeType](#nodetype)
  - [PartitionIndexStatus](#partitionindexstatus)
  - [Permission](#permission)
  - [PrincipalType](#principaltype)
  - [RecrawlBehavior](#recrawlbehavior)
  - [RegistryStatus](#registrystatus)
  - [ResourceShareType](#resourcesharetype)
  - [ResourceType](#resourcetype)
  - [S3EncryptionMode](#s3encryptionmode)
  - [ScheduleState](#schedulestate)
  - [SchemaDiffType](#schemadifftype)
  - [SchemaStatus](#schemastatus)
  - [SchemaVersionStatus](#schemaversionstatus)
  - [Sort](#sort)
  - [SortDirectionType](#sortdirectiontype)
  - [TaskRunSortColumnType](#taskrunsortcolumntype)
  - [TaskStatusType](#taskstatustype)
  - [TaskType](#tasktype)
  - [TransformSortColumnType](#transformsortcolumntype)
  - [TransformStatusType](#transformstatustype)
  - [TransformType](#transformtype)
  - [TriggerState](#triggerstate)
  - [TriggerType](#triggertype)
  - [UpdateBehavior](#updatebehavior)
  - [WorkerType](#workertype)
  - [WorkflowRunStatus](#workflowrunstatus)

## BackfillErrorCode

```python
from mypy_boto3_glue.literals import BackfillErrorCode
```

Values:

- `ENCRYPTED_PARTITION_ERROR`
- `INTERNAL_ERROR`
- `INVALID_PARTITION_TYPE_DATA_ERROR`
- `MISSING_PARTITION_VALUE_ERROR`
- `UNSUPPORTED_PARTITION_CHARACTER_ERROR`

## CatalogEncryptionMode

```python
from mypy_boto3_glue.literals import CatalogEncryptionMode
```

Values:

- `DISABLED`
- `SSE-KMS`

## CloudWatchEncryptionMode

```python
from mypy_boto3_glue.literals import CloudWatchEncryptionMode
```

Values:

- `DISABLED`
- `SSE-KMS`

## ColumnStatisticsType

```python
from mypy_boto3_glue.literals import ColumnStatisticsType
```

Values:

- `BINARY`
- `BOOLEAN`
- `DATE`
- `DECIMAL`
- `DOUBLE`
- `LONG`
- `STRING`

## Comparator

```python
from mypy_boto3_glue.literals import Comparator
```

Values:

- `EQUALS`
- `GREATER_THAN`
- `GREATER_THAN_EQUALS`
- `LESS_THAN`
- `LESS_THAN_EQUALS`

## Compatibility

```python
from mypy_boto3_glue.literals import Compatibility
```

Values:

- `BACKWARD`
- `BACKWARD_ALL`
- `DISABLED`
- `FORWARD`
- `FORWARD_ALL`
- `FULL`
- `FULL_ALL`
- `NONE`

## ConnectionPropertyKey

```python
from mypy_boto3_glue.literals import ConnectionPropertyKey
```

Values:

- `CONFIG_FILES`
- `CONNECTION_URL`
- `CONNECTOR_CLASS_NAME`
- `CONNECTOR_TYPE`
- `CONNECTOR_URL`
- `CUSTOM_JDBC_CERT`
- `CUSTOM_JDBC_CERT_STRING`
- `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD`
- `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD`
- `ENCRYPTED_PASSWORD`
- `HOST`
- `INSTANCE_ID`
- `JDBC_CONNECTION_URL`
- `JDBC_DRIVER_CLASS_NAME`
- `JDBC_DRIVER_JAR_URI`
- `JDBC_ENFORCE_SSL`
- `JDBC_ENGINE`
- `JDBC_ENGINE_VERSION`
- `KAFKA_BOOTSTRAP_SERVERS`
- `KAFKA_CLIENT_KEY_PASSWORD`
- `KAFKA_CLIENT_KEYSTORE`
- `KAFKA_CLIENT_KEYSTORE_PASSWORD`
- `KAFKA_CUSTOM_CERT`
- `KAFKA_SKIP_CUSTOM_CERT_VALIDATION`
- `KAFKA_SSL_ENABLED`
- `PASSWORD`
- `PORT`
- `SECRET_ID`
- `SKIP_CUSTOM_JDBC_CERT_VALIDATION`
- `USERNAME`

## ConnectionType

```python
from mypy_boto3_glue.literals import ConnectionType
```

Values:

- `CUSTOM`
- `JDBC`
- `KAFKA`
- `MARKETPLACE`
- `MONGODB`
- `NETWORK`
- `SFTP`

## CrawlState

```python
from mypy_boto3_glue.literals import CrawlState
```

Values:

- `CANCELLED`
- `CANCELLING`
- `FAILED`
- `RUNNING`
- `SUCCEEDED`

## CrawlerLineageSettings

```python
from mypy_boto3_glue.literals import CrawlerLineageSettings
```

Values:

- `DISABLE`
- `ENABLE`

## CrawlerState

```python
from mypy_boto3_glue.literals import CrawlerState
```

Values:

- `READY`
- `RUNNING`
- `STOPPING`

## CsvHeaderOption

```python
from mypy_boto3_glue.literals import CsvHeaderOption
```

Values:

- `ABSENT`
- `PRESENT`
- `UNKNOWN`

## DataFormat

```python
from mypy_boto3_glue.literals import DataFormat
```

Values:

- `AVRO`

## DeleteBehavior

```python
from mypy_boto3_glue.literals import DeleteBehavior
```

Values:

- `DELETE_FROM_DATABASE`
- `DEPRECATE_IN_DATABASE`
- `LOG`

## EnableHybridValues

```python
from mypy_boto3_glue.literals import EnableHybridValues
```

Values:

- `FALSE`
- `TRUE`

## ExistCondition

```python
from mypy_boto3_glue.literals import ExistCondition
```

Values:

- `MUST_EXIST`
- `NONE`
- `NOT_EXIST`

## GetClassifiersPaginatorName

```python
from mypy_boto3_glue.literals import GetClassifiersPaginatorName
```

Values:

- `get_classifiers`

## GetConnectionsPaginatorName

```python
from mypy_boto3_glue.literals import GetConnectionsPaginatorName
```

Values:

- `get_connections`

## GetCrawlerMetricsPaginatorName

```python
from mypy_boto3_glue.literals import GetCrawlerMetricsPaginatorName
```

Values:

- `get_crawler_metrics`

## GetCrawlersPaginatorName

```python
from mypy_boto3_glue.literals import GetCrawlersPaginatorName
```

Values:

- `get_crawlers`

## GetDatabasesPaginatorName

```python
from mypy_boto3_glue.literals import GetDatabasesPaginatorName
```

Values:

- `get_databases`

## GetDevEndpointsPaginatorName

```python
from mypy_boto3_glue.literals import GetDevEndpointsPaginatorName
```

Values:

- `get_dev_endpoints`

## GetJobRunsPaginatorName

```python
from mypy_boto3_glue.literals import GetJobRunsPaginatorName
```

Values:

- `get_job_runs`

## GetJobsPaginatorName

```python
from mypy_boto3_glue.literals import GetJobsPaginatorName
```

Values:

- `get_jobs`

## GetPartitionIndexesPaginatorName

```python
from mypy_boto3_glue.literals import GetPartitionIndexesPaginatorName
```

Values:

- `get_partition_indexes`

## GetPartitionsPaginatorName

```python
from mypy_boto3_glue.literals import GetPartitionsPaginatorName
```

Values:

- `get_partitions`

## GetResourcePoliciesPaginatorName

```python
from mypy_boto3_glue.literals import GetResourcePoliciesPaginatorName
```

Values:

- `get_resource_policies`

## GetSecurityConfigurationsPaginatorName

```python
from mypy_boto3_glue.literals import GetSecurityConfigurationsPaginatorName
```

Values:

- `get_security_configurations`

## GetTableVersionsPaginatorName

```python
from mypy_boto3_glue.literals import GetTableVersionsPaginatorName
```

Values:

- `get_table_versions`

## GetTablesPaginatorName

```python
from mypy_boto3_glue.literals import GetTablesPaginatorName
```

Values:

- `get_tables`

## GetTriggersPaginatorName

```python
from mypy_boto3_glue.literals import GetTriggersPaginatorName
```

Values:

- `get_triggers`

## GetUserDefinedFunctionsPaginatorName

```python
from mypy_boto3_glue.literals import GetUserDefinedFunctionsPaginatorName
```

Values:

- `get_user_defined_functions`

## JobBookmarksEncryptionMode

```python
from mypy_boto3_glue.literals import JobBookmarksEncryptionMode
```

Values:

- `CSE-KMS`
- `DISABLED`

## JobRunState

```python
from mypy_boto3_glue.literals import JobRunState
```

Values:

- `FAILED`
- `RUNNING`
- `STARTING`
- `STOPPED`
- `STOPPING`
- `SUCCEEDED`
- `TIMEOUT`

## Language

```python
from mypy_boto3_glue.literals import Language
```

Values:

- `PYTHON`
- `SCALA`

## LastCrawlStatus

```python
from mypy_boto3_glue.literals import LastCrawlStatus
```

Values:

- `CANCELLED`
- `FAILED`
- `SUCCEEDED`

## ListRegistriesPaginatorName

```python
from mypy_boto3_glue.literals import ListRegistriesPaginatorName
```

Values:

- `list_registries`

## ListSchemaVersionsPaginatorName

```python
from mypy_boto3_glue.literals import ListSchemaVersionsPaginatorName
```

Values:

- `list_schema_versions`

## ListSchemasPaginatorName

```python
from mypy_boto3_glue.literals import ListSchemasPaginatorName
```

Values:

- `list_schemas`

## Logical

```python
from mypy_boto3_glue.literals import Logical
```

Values:

- `AND`
- `ANY`

## LogicalOperator

```python
from mypy_boto3_glue.literals import LogicalOperator
```

Values:

- `EQUALS`

## MLUserDataEncryptionModeString

```python
from mypy_boto3_glue.literals import MLUserDataEncryptionModeString
```

Values:

- `DISABLED`
- `SSE-KMS`

## NodeType

```python
from mypy_boto3_glue.literals import NodeType
```

Values:

- `CRAWLER`
- `JOB`
- `TRIGGER`

## PartitionIndexStatus

```python
from mypy_boto3_glue.literals import PartitionIndexStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`

## Permission

```python
from mypy_boto3_glue.literals import Permission
```

Values:

- `ALL`
- `ALTER`
- `CREATE_DATABASE`
- `CREATE_TABLE`
- `DATA_LOCATION_ACCESS`
- `DELETE`
- `DROP`
- `INSERT`
- `SELECT`

## PrincipalType

```python
from mypy_boto3_glue.literals import PrincipalType
```

Values:

- `GROUP`
- `ROLE`
- `USER`

## RecrawlBehavior

```python
from mypy_boto3_glue.literals import RecrawlBehavior
```

Values:

- `CRAWL_EVERYTHING`
- `CRAWL_NEW_FOLDERS_ONLY`

## RegistryStatus

```python
from mypy_boto3_glue.literals import RegistryStatus
```

Values:

- `AVAILABLE`
- `DELETING`

## ResourceShareType

```python
from mypy_boto3_glue.literals import ResourceShareType
```

Values:

- `ALL`
- `FOREIGN`

## ResourceType

```python
from mypy_boto3_glue.literals import ResourceType
```

Values:

- `ARCHIVE`
- `FILE`
- `JAR`

## S3EncryptionMode

```python
from mypy_boto3_glue.literals import S3EncryptionMode
```

Values:

- `DISABLED`
- `SSE-KMS`
- `SSE-S3`

## ScheduleState

```python
from mypy_boto3_glue.literals import ScheduleState
```

Values:

- `NOT_SCHEDULED`
- `SCHEDULED`
- `TRANSITIONING`

## SchemaDiffType

```python
from mypy_boto3_glue.literals import SchemaDiffType
```

Values:

- `SYNTAX_DIFF`

## SchemaStatus

```python
from mypy_boto3_glue.literals import SchemaStatus
```

Values:

- `AVAILABLE`
- `DELETING`
- `PENDING`

## SchemaVersionStatus

```python
from mypy_boto3_glue.literals import SchemaVersionStatus
```

Values:

- `AVAILABLE`
- `DELETING`
- `FAILURE`
- `PENDING`

## Sort

```python
from mypy_boto3_glue.literals import Sort
```

Values:

- `ASC`
- `DESC`

## SortDirectionType

```python
from mypy_boto3_glue.literals import SortDirectionType
```

Values:

- `ASCENDING`
- `DESCENDING`

## TaskRunSortColumnType

```python
from mypy_boto3_glue.literals import TaskRunSortColumnType
```

Values:

- `STARTED`
- `STATUS`
- `TASK_RUN_TYPE`

## TaskStatusType

```python
from mypy_boto3_glue.literals import TaskStatusType
```

Values:

- `FAILED`
- `RUNNING`
- `STARTING`
- `STOPPED`
- `STOPPING`
- `SUCCEEDED`
- `TIMEOUT`

## TaskType

```python
from mypy_boto3_glue.literals import TaskType
```

Values:

- `EVALUATION`
- `EXPORT_LABELS`
- `FIND_MATCHES`
- `IMPORT_LABELS`
- `LABELING_SET_GENERATION`

## TransformSortColumnType

```python
from mypy_boto3_glue.literals import TransformSortColumnType
```

Values:

- `CREATED`
- `LAST_MODIFIED`
- `NAME`
- `STATUS`
- `TRANSFORM_TYPE`

## TransformStatusType

```python
from mypy_boto3_glue.literals import TransformStatusType
```

Values:

- `DELETING`
- `NOT_READY`
- `READY`

## TransformType

```python
from mypy_boto3_glue.literals import TransformType
```

Values:

- `FIND_MATCHES`

## TriggerState

```python
from mypy_boto3_glue.literals import TriggerState
```

Values:

- `ACTIVATED`
- `ACTIVATING`
- `CREATED`
- `CREATING`
- `DEACTIVATED`
- `DEACTIVATING`
- `DELETING`
- `UPDATING`

## TriggerType

```python
from mypy_boto3_glue.literals import TriggerType
```

Values:

- `CONDITIONAL`
- `ON_DEMAND`
- `SCHEDULED`

## UpdateBehavior

```python
from mypy_boto3_glue.literals import UpdateBehavior
```

Values:

- `LOG`
- `UPDATE_IN_DATABASE`

## WorkerType

```python
from mypy_boto3_glue.literals import WorkerType
```

Values:

- `G.1X`
- `G.2X`
- `Standard`

## WorkflowRunStatus

```python
from mypy_boto3_glue.literals import WorkflowRunStatus
```

Values:

- `COMPLETED`
- `ERROR`
- `RUNNING`
- `STOPPED`
- `STOPPING`
