# Literals for boto3 DatabaseMigrationService module

> [Index](../index.md) > [DatabaseMigrationService](./index.md) > Literals

Auto-generated documentation for [DatabaseMigrationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService)
type annotations stubs module [mypy_boto3_dms](https://pypi.org/project/mypy-boto3-dms/).

- [Literals for boto3 DatabaseMigrationService module](#literals-for-boto3-databasemigrationservice-module)
  - [AuthMechanismValue](#authmechanismvalue)
  - [AuthTypeValue](#authtypevalue)
  - [CharLengthSemantics](#charlengthsemantics)
  - [CompressionTypeValue](#compressiontypevalue)
  - [DataFormatValue](#dataformatvalue)
  - [DatePartitionDelimiterValue](#datepartitiondelimitervalue)
  - [DatePartitionSequenceValue](#datepartitionsequencevalue)
  - [DescribeCertificatesPaginatorName](#describecertificatespaginatorname)
  - [DescribeConnectionsPaginatorName](#describeconnectionspaginatorname)
  - [DescribeEndpointTypesPaginatorName](#describeendpointtypespaginatorname)
  - [DescribeEndpointsPaginatorName](#describeendpointspaginatorname)
  - [DescribeEventSubscriptionsPaginatorName](#describeeventsubscriptionspaginatorname)
  - [DescribeEventsPaginatorName](#describeeventspaginatorname)
  - [DescribeOrderableReplicationInstancesPaginatorName](#describeorderablereplicationinstancespaginatorname)
  - [DescribeReplicationInstancesPaginatorName](#describereplicationinstancespaginatorname)
  - [DescribeReplicationSubnetGroupsPaginatorName](#describereplicationsubnetgroupspaginatorname)
  - [DescribeReplicationTaskAssessmentResultsPaginatorName](#describereplicationtaskassessmentresultspaginatorname)
  - [DescribeReplicationTasksPaginatorName](#describereplicationtaskspaginatorname)
  - [DescribeSchemasPaginatorName](#describeschemaspaginatorname)
  - [DescribeTableStatisticsPaginatorName](#describetablestatisticspaginatorname)
  - [DmsSslModeValue](#dmssslmodevalue)
  - [EncodingTypeValue](#encodingtypevalue)
  - [EncryptionModeValue](#encryptionmodevalue)
  - [EndpointDeletedWaiterName](#endpointdeletedwaitername)
  - [EndpointSettingTypeValue](#endpointsettingtypevalue)
  - [KafkaSecurityProtocol](#kafkasecurityprotocol)
  - [MessageFormatValue](#messageformatvalue)
  - [MigrationTypeValue](#migrationtypevalue)
  - [NestingLevelValue](#nestinglevelvalue)
  - [ParquetVersionValue](#parquetversionvalue)
  - [RefreshSchemasStatusTypeValue](#refreshschemasstatustypevalue)
  - [ReleaseStatusValues](#releasestatusvalues)
  - [ReloadOptionValue](#reloadoptionvalue)
  - [ReplicationEndpointTypeValue](#replicationendpointtypevalue)
  - [ReplicationInstanceAvailableWaiterName](#replicationinstanceavailablewaitername)
  - [ReplicationInstanceDeletedWaiterName](#replicationinstancedeletedwaitername)
  - [ReplicationTaskDeletedWaiterName](#replicationtaskdeletedwaitername)
  - [ReplicationTaskReadyWaiterName](#replicationtaskreadywaitername)
  - [ReplicationTaskRunningWaiterName](#replicationtaskrunningwaitername)
  - [ReplicationTaskStoppedWaiterName](#replicationtaskstoppedwaitername)
  - [SafeguardPolicy](#safeguardpolicy)
  - [SourceType](#sourcetype)
  - [StartReplicationTaskTypeValue](#startreplicationtasktypevalue)
  - [TargetDbType](#targetdbtype)
  - [TestConnectionSucceedsWaiterName](#testconnectionsucceedswaitername)

## AuthMechanismValue

```python
from mypy_boto3_dms.literals import AuthMechanismValue
```

Values:

- `default`
- `mongodb_cr`
- `scram_sha_1`

## AuthTypeValue

```python
from mypy_boto3_dms.literals import AuthTypeValue
```

Values:

- `no`
- `password`

## CharLengthSemantics

```python
from mypy_boto3_dms.literals import CharLengthSemantics
```

Values:

- `byte`
- `char`
- `default`

## CompressionTypeValue

```python
from mypy_boto3_dms.literals import CompressionTypeValue
```

Values:

- `gzip`
- `none`

## DataFormatValue

```python
from mypy_boto3_dms.literals import DataFormatValue
```

Values:

- `csv`
- `parquet`

## DatePartitionDelimiterValue

```python
from mypy_boto3_dms.literals import DatePartitionDelimiterValue
```

Values:

- `DASH`
- `NONE`
- `SLASH`
- `UNDERSCORE`

## DatePartitionSequenceValue

```python
from mypy_boto3_dms.literals import DatePartitionSequenceValue
```

Values:

- `DDMMYYYY`
- `MMYYYYDD`
- `YYYYMM`
- `YYYYMMDD`
- `YYYYMMDDHH`

## DescribeCertificatesPaginatorName

```python
from mypy_boto3_dms.literals import DescribeCertificatesPaginatorName
```

Values:

- `describe_certificates`

## DescribeConnectionsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeConnectionsPaginatorName
```

Values:

- `describe_connections`

## DescribeEndpointTypesPaginatorName

```python
from mypy_boto3_dms.literals import DescribeEndpointTypesPaginatorName
```

Values:

- `describe_endpoint_types`

## DescribeEndpointsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeEndpointsPaginatorName
```

Values:

- `describe_endpoints`

## DescribeEventSubscriptionsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeEventSubscriptionsPaginatorName
```

Values:

- `describe_event_subscriptions`

## DescribeEventsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeEventsPaginatorName
```

Values:

- `describe_events`

## DescribeOrderableReplicationInstancesPaginatorName

```python
from mypy_boto3_dms.literals import DescribeOrderableReplicationInstancesPaginatorName
```

Values:

- `describe_orderable_replication_instances`

## DescribeReplicationInstancesPaginatorName

```python
from mypy_boto3_dms.literals import DescribeReplicationInstancesPaginatorName
```

Values:

- `describe_replication_instances`

## DescribeReplicationSubnetGroupsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeReplicationSubnetGroupsPaginatorName
```

Values:

- `describe_replication_subnet_groups`

## DescribeReplicationTaskAssessmentResultsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeReplicationTaskAssessmentResultsPaginatorName
```

Values:

- `describe_replication_task_assessment_results`

## DescribeReplicationTasksPaginatorName

```python
from mypy_boto3_dms.literals import DescribeReplicationTasksPaginatorName
```

Values:

- `describe_replication_tasks`

## DescribeSchemasPaginatorName

```python
from mypy_boto3_dms.literals import DescribeSchemasPaginatorName
```

Values:

- `describe_schemas`

## DescribeTableStatisticsPaginatorName

```python
from mypy_boto3_dms.literals import DescribeTableStatisticsPaginatorName
```

Values:

- `describe_table_statistics`

## DmsSslModeValue

```python
from mypy_boto3_dms.literals import DmsSslModeValue
```

Values:

- `none`
- `require`
- `verify-ca`
- `verify-full`

## EncodingTypeValue

```python
from mypy_boto3_dms.literals import EncodingTypeValue
```

Values:

- `plain`
- `plain-dictionary`
- `rle-dictionary`

## EncryptionModeValue

```python
from mypy_boto3_dms.literals import EncryptionModeValue
```

Values:

- `sse-kms`
- `sse-s3`

## EndpointDeletedWaiterName

```python
from mypy_boto3_dms.literals import EndpointDeletedWaiterName
```

Values:

- `endpoint_deleted`

## EndpointSettingTypeValue

```python
from mypy_boto3_dms.literals import EndpointSettingTypeValue
```

Values:

- `boolean`
- `enum`
- `integer`
- `string`

## KafkaSecurityProtocol

```python
from mypy_boto3_dms.literals import KafkaSecurityProtocol
```

Values:

- `plaintext`
- `sasl-ssl`
- `ssl-authentication`
- `ssl-encryption`

## MessageFormatValue

```python
from mypy_boto3_dms.literals import MessageFormatValue
```

Values:

- `json`
- `json-unformatted`

## MigrationTypeValue

```python
from mypy_boto3_dms.literals import MigrationTypeValue
```

Values:

- `cdc`
- `full-load`
- `full-load-and-cdc`

## NestingLevelValue

```python
from mypy_boto3_dms.literals import NestingLevelValue
```

Values:

- `none`
- `one`

## ParquetVersionValue

```python
from mypy_boto3_dms.literals import ParquetVersionValue
```

Values:

- `parquet-1-0`
- `parquet-2-0`

## RefreshSchemasStatusTypeValue

```python
from mypy_boto3_dms.literals import RefreshSchemasStatusTypeValue
```

Values:

- `failed`
- `refreshing`
- `successful`

## ReleaseStatusValues

```python
from mypy_boto3_dms.literals import ReleaseStatusValues
```

Values:

- `beta`

## ReloadOptionValue

```python
from mypy_boto3_dms.literals import ReloadOptionValue
```

Values:

- `data-reload`
- `validate-only`

## ReplicationEndpointTypeValue

```python
from mypy_boto3_dms.literals import ReplicationEndpointTypeValue
```

Values:

- `source`
- `target`

## ReplicationInstanceAvailableWaiterName

```python
from mypy_boto3_dms.literals import ReplicationInstanceAvailableWaiterName
```

Values:

- `replication_instance_available`

## ReplicationInstanceDeletedWaiterName

```python
from mypy_boto3_dms.literals import ReplicationInstanceDeletedWaiterName
```

Values:

- `replication_instance_deleted`

## ReplicationTaskDeletedWaiterName

```python
from mypy_boto3_dms.literals import ReplicationTaskDeletedWaiterName
```

Values:

- `replication_task_deleted`

## ReplicationTaskReadyWaiterName

```python
from mypy_boto3_dms.literals import ReplicationTaskReadyWaiterName
```

Values:

- `replication_task_ready`

## ReplicationTaskRunningWaiterName

```python
from mypy_boto3_dms.literals import ReplicationTaskRunningWaiterName
```

Values:

- `replication_task_running`

## ReplicationTaskStoppedWaiterName

```python
from mypy_boto3_dms.literals import ReplicationTaskStoppedWaiterName
```

Values:

- `replication_task_stopped`

## SafeguardPolicy

```python
from mypy_boto3_dms.literals import SafeguardPolicy
```

Values:

- `exclusive-automatic-truncation`
- `rely-on-sql-server-replication-agent`
- `shared-automatic-truncation`

## SourceType

```python
from mypy_boto3_dms.literals import SourceType
```

Values:

- `replication-instance`

## StartReplicationTaskTypeValue

```python
from mypy_boto3_dms.literals import StartReplicationTaskTypeValue
```

Values:

- `reload-target`
- `resume-processing`
- `start-replication`

## TargetDbType

```python
from mypy_boto3_dms.literals import TargetDbType
```

Values:

- `multiple-databases`
- `specific-database`

## TestConnectionSucceedsWaiterName

```python
from mypy_boto3_dms.literals import TestConnectionSucceedsWaiterName
```

Values:

- `test_connection_succeeds`
