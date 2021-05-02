# Literals for boto3 ElasticsearchService module

> [Index](../index.md) > [ElasticsearchService](./index.md) > Literals

Auto-generated documentation for [ElasticsearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService)
type annotations stubs module [mypy_boto3_es](https://pypi.org/project/mypy-boto3-es/).

- [Literals for boto3 ElasticsearchService module](#literals-for-boto3-elasticsearchservice-module)
  - [AutoTuneDesiredState](#autotunedesiredstate)
  - [AutoTuneState](#autotunestate)
  - [AutoTuneType](#autotunetype)
  - [DeploymentStatus](#deploymentstatus)
  - [DescribePackagesFilterName](#describepackagesfiltername)
  - [DescribeReservedElasticsearchInstanceOfferingsPaginatorName](#describereservedelasticsearchinstanceofferingspaginatorname)
  - [DescribeReservedElasticsearchInstancesPaginatorName](#describereservedelasticsearchinstancespaginatorname)
  - [DomainPackageStatus](#domainpackagestatus)
  - [ESPartitionInstanceType](#espartitioninstancetype)
  - [ESWarmPartitionInstanceType](#eswarmpartitioninstancetype)
  - [GetUpgradeHistoryPaginatorName](#getupgradehistorypaginatorname)
  - [InboundCrossClusterSearchConnectionStatusCode](#inboundcrossclustersearchconnectionstatuscode)
  - [ListElasticsearchInstanceTypesPaginatorName](#listelasticsearchinstancetypespaginatorname)
  - [ListElasticsearchVersionsPaginatorName](#listelasticsearchversionspaginatorname)
  - [LogType](#logtype)
  - [OptionState](#optionstate)
  - [OutboundCrossClusterSearchConnectionStatusCode](#outboundcrossclustersearchconnectionstatuscode)
  - [PackageStatus](#packagestatus)
  - [PackageType](#packagetype)
  - [ReservedElasticsearchInstancePaymentOption](#reservedelasticsearchinstancepaymentoption)
  - [RollbackOnDisable](#rollbackondisable)
  - [ScheduledAutoTuneActionType](#scheduledautotuneactiontype)
  - [ScheduledAutoTuneSeverityType](#scheduledautotuneseveritytype)
  - [TLSSecurityPolicy](#tlssecuritypolicy)
  - [TimeUnit](#timeunit)
  - [UpgradeStatus](#upgradestatus)
  - [UpgradeStep](#upgradestep)
  - [VolumeType](#volumetype)

## AutoTuneDesiredState

```python
from mypy_boto3_es.literals import AutoTuneDesiredState
```

Values:

- `DISABLED`
- `ENABLED`

## AutoTuneState

```python
from mypy_boto3_es.literals import AutoTuneState
```

Values:

- `DISABLE_IN_PROGRESS`
- `DISABLED`
- `DISABLED_AND_ROLLBACK_COMPLETE`
- `DISABLED_AND_ROLLBACK_ERROR`
- `DISABLED_AND_ROLLBACK_IN_PROGRESS`
- `DISABLED_AND_ROLLBACK_SCHEDULED`
- `ENABLE_IN_PROGRESS`
- `ENABLED`
- `ERROR`

## AutoTuneType

```python
from mypy_boto3_es.literals import AutoTuneType
```

Values:

- `SCHEDULED_ACTION`

## DeploymentStatus

```python
from mypy_boto3_es.literals import DeploymentStatus
```

Values:

- `COMPLETED`
- `ELIGIBLE`
- `IN_PROGRESS`
- `NOT_ELIGIBLE`
- `PENDING_UPDATE`

## DescribePackagesFilterName

```python
from mypy_boto3_es.literals import DescribePackagesFilterName
```

Values:

- `PackageID`
- `PackageName`
- `PackageStatus`

## DescribeReservedElasticsearchInstanceOfferingsPaginatorName

```python
from mypy_boto3_es.literals import DescribeReservedElasticsearchInstanceOfferingsPaginatorName
```

Values:

- `describe_reserved_elasticsearch_instance_offerings`

## DescribeReservedElasticsearchInstancesPaginatorName

```python
from mypy_boto3_es.literals import DescribeReservedElasticsearchInstancesPaginatorName
```

Values:

- `describe_reserved_elasticsearch_instances`

## DomainPackageStatus

```python
from mypy_boto3_es.literals import DomainPackageStatus
```

Values:

- `ACTIVE`
- `ASSOCIATING`
- `ASSOCIATION_FAILED`
- `DISSOCIATING`
- `DISSOCIATION_FAILED`

## ESPartitionInstanceType

```python
from mypy_boto3_es.literals import ESPartitionInstanceType
```

Values:

- `c4.2xlarge.elasticsearch`
- `c4.4xlarge.elasticsearch`
- `c4.8xlarge.elasticsearch`
- `c4.large.elasticsearch`
- `c4.xlarge.elasticsearch`
- `c5.18xlarge.elasticsearch`
- `c5.2xlarge.elasticsearch`
- `c5.4xlarge.elasticsearch`
- `c5.9xlarge.elasticsearch`
- `c5.large.elasticsearch`
- `c5.xlarge.elasticsearch`
- `d2.2xlarge.elasticsearch`
- `d2.4xlarge.elasticsearch`
- `d2.8xlarge.elasticsearch`
- `d2.xlarge.elasticsearch`
- `i2.2xlarge.elasticsearch`
- `i2.xlarge.elasticsearch`
- `i3.16xlarge.elasticsearch`
- `i3.2xlarge.elasticsearch`
- `i3.4xlarge.elasticsearch`
- `i3.8xlarge.elasticsearch`
- `i3.large.elasticsearch`
- `i3.xlarge.elasticsearch`
- `m3.2xlarge.elasticsearch`
- `m3.large.elasticsearch`
- `m3.medium.elasticsearch`
- `m3.xlarge.elasticsearch`
- `m4.10xlarge.elasticsearch`
- `m4.2xlarge.elasticsearch`
- `m4.4xlarge.elasticsearch`
- `m4.large.elasticsearch`
- `m4.xlarge.elasticsearch`
- `m5.12xlarge.elasticsearch`
- `m5.2xlarge.elasticsearch`
- `m5.4xlarge.elasticsearch`
- `m5.large.elasticsearch`
- `m5.xlarge.elasticsearch`
- `r3.2xlarge.elasticsearch`
- `r3.4xlarge.elasticsearch`
- `r3.8xlarge.elasticsearch`
- `r3.large.elasticsearch`
- `r3.xlarge.elasticsearch`
- `r4.16xlarge.elasticsearch`
- `r4.2xlarge.elasticsearch`
- `r4.4xlarge.elasticsearch`
- `r4.8xlarge.elasticsearch`
- `r4.large.elasticsearch`
- `r4.xlarge.elasticsearch`
- `r5.12xlarge.elasticsearch`
- `r5.2xlarge.elasticsearch`
- `r5.4xlarge.elasticsearch`
- `r5.large.elasticsearch`
- `r5.xlarge.elasticsearch`
- `t2.medium.elasticsearch`
- `t2.micro.elasticsearch`
- `t2.small.elasticsearch`
- `ultrawarm1.large.elasticsearch`
- `ultrawarm1.medium.elasticsearch`

## ESWarmPartitionInstanceType

```python
from mypy_boto3_es.literals import ESWarmPartitionInstanceType
```

Values:

- `ultrawarm1.large.elasticsearch`
- `ultrawarm1.medium.elasticsearch`

## GetUpgradeHistoryPaginatorName

```python
from mypy_boto3_es.literals import GetUpgradeHistoryPaginatorName
```

Values:

- `get_upgrade_history`

## InboundCrossClusterSearchConnectionStatusCode

```python
from mypy_boto3_es.literals import InboundCrossClusterSearchConnectionStatusCode
```

Values:

- `APPROVED`
- `DELETED`
- `DELETING`
- `PENDING_ACCEPTANCE`
- `REJECTED`
- `REJECTING`

## ListElasticsearchInstanceTypesPaginatorName

```python
from mypy_boto3_es.literals import ListElasticsearchInstanceTypesPaginatorName
```

Values:

- `list_elasticsearch_instance_types`

## ListElasticsearchVersionsPaginatorName

```python
from mypy_boto3_es.literals import ListElasticsearchVersionsPaginatorName
```

Values:

- `list_elasticsearch_versions`

## LogType

```python
from mypy_boto3_es.literals import LogType
```

Values:

- `AUDIT_LOGS`
- `ES_APPLICATION_LOGS`
- `INDEX_SLOW_LOGS`
- `SEARCH_SLOW_LOGS`

## OptionState

```python
from mypy_boto3_es.literals import OptionState
```

Values:

- `Active`
- `Processing`
- `RequiresIndexDocuments`

## OutboundCrossClusterSearchConnectionStatusCode

```python
from mypy_boto3_es.literals import OutboundCrossClusterSearchConnectionStatusCode
```

Values:

- `ACTIVE`
- `DELETED`
- `DELETING`
- `PENDING_ACCEPTANCE`
- `PROVISIONING`
- `REJECTED`
- `VALIDATING`
- `VALIDATION_FAILED`

## PackageStatus

```python
from mypy_boto3_es.literals import PackageStatus
```

Values:

- `AVAILABLE`
- `COPY_FAILED`
- `COPYING`
- `DELETE_FAILED`
- `DELETED`
- `DELETING`
- `VALIDATING`
- `VALIDATION_FAILED`

## PackageType

```python
from mypy_boto3_es.literals import PackageType
```

Values:

- `TXT-DICTIONARY`

## ReservedElasticsearchInstancePaymentOption

```python
from mypy_boto3_es.literals import ReservedElasticsearchInstancePaymentOption
```

Values:

- `ALL_UPFRONT`
- `NO_UPFRONT`
- `PARTIAL_UPFRONT`

## RollbackOnDisable

```python
from mypy_boto3_es.literals import RollbackOnDisable
```

Values:

- `DEFAULT_ROLLBACK`
- `NO_ROLLBACK`

## ScheduledAutoTuneActionType

```python
from mypy_boto3_es.literals import ScheduledAutoTuneActionType
```

Values:

- `JVM_HEAP_SIZE_TUNING`
- `JVM_YOUNG_GEN_TUNING`

## ScheduledAutoTuneSeverityType

```python
from mypy_boto3_es.literals import ScheduledAutoTuneSeverityType
```

Values:

- `HIGH`
- `LOW`
- `MEDIUM`

## TLSSecurityPolicy

```python
from mypy_boto3_es.literals import TLSSecurityPolicy
```

Values:

- `Policy-Min-TLS-1-0-2019-07`
- `Policy-Min-TLS-1-2-2019-07`

## TimeUnit

```python
from mypy_boto3_es.literals import TimeUnit
```

Values:

- `HOURS`

## UpgradeStatus

```python
from mypy_boto3_es.literals import UpgradeStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `SUCCEEDED_WITH_ISSUES`

## UpgradeStep

```python
from mypy_boto3_es.literals import UpgradeStep
```

Values:

- `PRE_UPGRADE_CHECK`
- `SNAPSHOT`
- `UPGRADE`

## VolumeType

```python
from mypy_boto3_es.literals import VolumeType
```

Values:

- `gp2`
- `io1`
- `standard`
