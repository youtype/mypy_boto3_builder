# Literals for boto3 QLDB module

> [Index](../index.md) > [QLDB](./index.md) > Literals

Auto-generated documentation for [QLDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB)
type annotations stubs module [mypy_boto3_qldb](https://pypi.org/project/mypy-boto3-qldb/).

- [Literals for boto3 QLDB module](#literals-for-boto3-qldb-module)
  - [ErrorCause](#errorcause)
  - [ExportStatus](#exportstatus)
  - [LedgerState](#ledgerstate)
  - [PermissionsMode](#permissionsmode)
  - [S3ObjectEncryptionType](#s3objectencryptiontype)
  - [StreamStatus](#streamstatus)

## ErrorCause

```python
from mypy_boto3_qldb.literals import ErrorCause
```

Values:

- `IAM_PERMISSION_REVOKED`
- `KINESIS_STREAM_NOT_FOUND`

## ExportStatus

```python
from mypy_boto3_qldb.literals import ExportStatus
```

Values:

- `CANCELLED`
- `COMPLETED`
- `IN_PROGRESS`

## LedgerState

```python
from mypy_boto3_qldb.literals import LedgerState
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETED`
- `DELETING`

## PermissionsMode

```python
from mypy_boto3_qldb.literals import PermissionsMode
```

Values:

- `ALLOW_ALL`

## S3ObjectEncryptionType

```python
from mypy_boto3_qldb.literals import S3ObjectEncryptionType
```

Values:

- `NO_ENCRYPTION`
- `SSE_KMS`
- `SSE_S3`

## StreamStatus

```python
from mypy_boto3_qldb.literals import StreamStatus
```

Values:

- `ACTIVE`
- `CANCELED`
- `COMPLETED`
- `FAILED`
- `IMPAIRED`
