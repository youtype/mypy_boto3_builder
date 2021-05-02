# Literals for boto3 Backup module

> [Index](../index.md) > [Backup](./index.md) > Literals

Auto-generated documentation for [Backup](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html#Backup)
type annotations stubs module [mypy_boto3_backup](https://pypi.org/project/mypy-boto3-backup/).

- [Literals for boto3 Backup module](#literals-for-boto3-backup-module)
  - [BackupJobState](#backupjobstate)
  - [BackupVaultEvent](#backupvaultevent)
  - [ConditionType](#conditiontype)
  - [CopyJobState](#copyjobstate)
  - [RecoveryPointStatus](#recoverypointstatus)
  - [RestoreJobStatus](#restorejobstatus)
  - [StorageClass](#storageclass)

## BackupJobState

```python
from mypy_boto3_backup.literals import BackupJobState
```

Values:

- `ABORTED`
- `ABORTING`
- `COMPLETED`
- `CREATED`
- `EXPIRED`
- `FAILED`
- `PENDING`
- `RUNNING`

## BackupVaultEvent

```python
from mypy_boto3_backup.literals import BackupVaultEvent
```

Values:

- `BACKUP_JOB_COMPLETED`
- `BACKUP_JOB_EXPIRED`
- `BACKUP_JOB_FAILED`
- `BACKUP_JOB_STARTED`
- `BACKUP_JOB_SUCCESSFUL`
- `BACKUP_PLAN_CREATED`
- `BACKUP_PLAN_MODIFIED`
- `COPY_JOB_FAILED`
- `COPY_JOB_STARTED`
- `COPY_JOB_SUCCESSFUL`
- `RECOVERY_POINT_MODIFIED`
- `RESTORE_JOB_COMPLETED`
- `RESTORE_JOB_FAILED`
- `RESTORE_JOB_STARTED`
- `RESTORE_JOB_SUCCESSFUL`

## ConditionType

```python
from mypy_boto3_backup.literals import ConditionType
```

Values:

- `STRINGEQUALS`

## CopyJobState

```python
from mypy_boto3_backup.literals import CopyJobState
```

Values:

- `COMPLETED`
- `CREATED`
- `FAILED`
- `RUNNING`

## RecoveryPointStatus

```python
from mypy_boto3_backup.literals import RecoveryPointStatus
```

Values:

- `COMPLETED`
- `DELETING`
- `EXPIRED`
- `PARTIAL`

## RestoreJobStatus

```python
from mypy_boto3_backup.literals import RestoreJobStatus
```

Values:

- `ABORTED`
- `COMPLETED`
- `FAILED`
- `PENDING`
- `RUNNING`

## StorageClass

```python
from mypy_boto3_backup.literals import StorageClass
```

Values:

- `COLD`
- `DELETED`
- `WARM`
