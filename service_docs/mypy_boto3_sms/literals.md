# Literals for boto3 SMS module

> [Index](../index.md) > [SMS](./index.md) > Literals

Auto-generated documentation for [SMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS)
type annotations stubs module [mypy_boto3_sms](https://pypi.org/project/mypy-boto3-sms/).

- [Literals for boto3 SMS module](#literals-for-boto3-sms-module)
  - [AppLaunchConfigurationStatus](#applaunchconfigurationstatus)
  - [AppLaunchStatus](#applaunchstatus)
  - [AppReplicationConfigurationStatus](#appreplicationconfigurationstatus)
  - [AppReplicationStatus](#appreplicationstatus)
  - [AppStatus](#appstatus)
  - [AppValidationStrategy](#appvalidationstrategy)
  - [ConnectorCapability](#connectorcapability)
  - [ConnectorStatus](#connectorstatus)
  - [GetConnectorsPaginatorName](#getconnectorspaginatorname)
  - [GetReplicationJobsPaginatorName](#getreplicationjobspaginatorname)
  - [GetReplicationRunsPaginatorName](#getreplicationrunspaginatorname)
  - [GetServersPaginatorName](#getserverspaginatorname)
  - [LicenseType](#licensetype)
  - [ListAppsPaginatorName](#listappspaginatorname)
  - [OutputFormat](#outputformat)
  - [ReplicationJobState](#replicationjobstate)
  - [ReplicationRunState](#replicationrunstate)
  - [ReplicationRunType](#replicationruntype)
  - [ScriptType](#scripttype)
  - [ServerCatalogStatus](#servercatalogstatus)
  - [ServerType](#servertype)
  - [ServerValidationStrategy](#servervalidationstrategy)
  - [ValidationStatus](#validationstatus)
  - [VmManagerType](#vmmanagertype)

## AppLaunchConfigurationStatus

```python
from mypy_boto3_sms.literals import AppLaunchConfigurationStatus
```

Values:

- `CONFIGURED`
- `NOT_CONFIGURED`

## AppLaunchStatus

```python
from mypy_boto3_sms.literals import AppLaunchStatus
```

Values:

- `CONFIGURATION_IN_PROGRESS`
- `CONFIGURATION_INVALID`
- `DELTA_LAUNCH_FAILED`
- `DELTA_LAUNCH_IN_PROGRESS`
- `LAUNCH_FAILED`
- `LAUNCH_IN_PROGRESS`
- `LAUNCH_PENDING`
- `LAUNCHED`
- `PARTIALLY_LAUNCHED`
- `READY_FOR_CONFIGURATION`
- `READY_FOR_LAUNCH`
- `TERMINATE_FAILED`
- `TERMINATE_IN_PROGRESS`
- `TERMINATED`
- `VALIDATION_IN_PROGRESS`

## AppReplicationConfigurationStatus

```python
from mypy_boto3_sms.literals import AppReplicationConfigurationStatus
```

Values:

- `CONFIGURED`
- `NOT_CONFIGURED`

## AppReplicationStatus

```python
from mypy_boto3_sms.literals import AppReplicationStatus
```

Values:

- `CONFIGURATION_IN_PROGRESS`
- `CONFIGURATION_INVALID`
- `DELTA_REPLICATED`
- `DELTA_REPLICATION_FAILED`
- `DELTA_REPLICATION_IN_PROGRESS`
- `PARTIALLY_REPLICATED`
- `READY_FOR_CONFIGURATION`
- `READY_FOR_REPLICATION`
- `REPLICATED`
- `REPLICATION_FAILED`
- `REPLICATION_IN_PROGRESS`
- `REPLICATION_PENDING`
- `REPLICATION_STOP_FAILED`
- `REPLICATION_STOPPED`
- `REPLICATION_STOPPING`
- `VALIDATION_IN_PROGRESS`

## AppStatus

```python
from mypy_boto3_sms.literals import AppStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETE_FAILED`
- `DELETED`
- `DELETING`
- `UPDATING`

## AppValidationStrategy

```python
from mypy_boto3_sms.literals import AppValidationStrategy
```

Values:

- `SSM`

## ConnectorCapability

```python
from mypy_boto3_sms.literals import ConnectorCapability
```

Values:

- `HYPERV-MANAGER`
- `SCVMM`
- `SMS_OPTIMIZED`
- `SNAPSHOT_BATCHING`
- `VSPHERE`

## ConnectorStatus

```python
from mypy_boto3_sms.literals import ConnectorStatus
```

Values:

- `HEALTHY`
- `UNHEALTHY`

## GetConnectorsPaginatorName

```python
from mypy_boto3_sms.literals import GetConnectorsPaginatorName
```

Values:

- `get_connectors`

## GetReplicationJobsPaginatorName

```python
from mypy_boto3_sms.literals import GetReplicationJobsPaginatorName
```

Values:

- `get_replication_jobs`

## GetReplicationRunsPaginatorName

```python
from mypy_boto3_sms.literals import GetReplicationRunsPaginatorName
```

Values:

- `get_replication_runs`

## GetServersPaginatorName

```python
from mypy_boto3_sms.literals import GetServersPaginatorName
```

Values:

- `get_servers`

## LicenseType

```python
from mypy_boto3_sms.literals import LicenseType
```

Values:

- `AWS`
- `BYOL`

## ListAppsPaginatorName

```python
from mypy_boto3_sms.literals import ListAppsPaginatorName
```

Values:

- `list_apps`

## OutputFormat

```python
from mypy_boto3_sms.literals import OutputFormat
```

Values:

- `JSON`
- `YAML`

## ReplicationJobState

```python
from mypy_boto3_sms.literals import ReplicationJobState
```

Values:

- `ACTIVE`
- `COMPLETED`
- `DELETED`
- `DELETING`
- `FAILED`
- `FAILING`
- `PAUSED_ON_FAILURE`
- `PENDING`

## ReplicationRunState

```python
from mypy_boto3_sms.literals import ReplicationRunState
```

Values:

- `ACTIVE`
- `COMPLETED`
- `DELETED`
- `DELETING`
- `FAILED`
- `MISSED`
- `PENDING`

## ReplicationRunType

```python
from mypy_boto3_sms.literals import ReplicationRunType
```

Values:

- `AUTOMATIC`
- `ON_DEMAND`

## ScriptType

```python
from mypy_boto3_sms.literals import ScriptType
```

Values:

- `POWERSHELL_SCRIPT`
- `SHELL_SCRIPT`

## ServerCatalogStatus

```python
from mypy_boto3_sms.literals import ServerCatalogStatus
```

Values:

- `AVAILABLE`
- `DELETED`
- `EXPIRED`
- `IMPORTING`
- `NOT_IMPORTED`

## ServerType

```python
from mypy_boto3_sms.literals import ServerType
```

Values:

- `VIRTUAL_MACHINE`

## ServerValidationStrategy

```python
from mypy_boto3_sms.literals import ServerValidationStrategy
```

Values:

- `USERDATA`

## ValidationStatus

```python
from mypy_boto3_sms.literals import ValidationStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `PENDING`
- `READY_FOR_VALIDATION`
- `SUCCEEDED`

## VmManagerType

```python
from mypy_boto3_sms.literals import VmManagerType
```

Values:

- `HYPERV-MANAGER`
- `SCVMM`
- `VSPHERE`
