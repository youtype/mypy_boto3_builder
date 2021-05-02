# Literals for boto3 DataExchange module

> [Index](../index.md) > [DataExchange](./index.md) > Literals

Auto-generated documentation for [DataExchange](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange)
type annotations stubs module [mypy_boto3_dataexchange](https://pypi.org/project/mypy-boto3-dataexchange/).

- [Literals for boto3 DataExchange module](#literals-for-boto3-dataexchange-module)
  - [AssetType](#assettype)
  - [Code](#code)
  - [JobErrorLimitName](#joberrorlimitname)
  - [JobErrorResourceTypes](#joberrorresourcetypes)
  - [ListDataSetRevisionsPaginatorName](#listdatasetrevisionspaginatorname)
  - [ListDataSetsPaginatorName](#listdatasetspaginatorname)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [ListRevisionAssetsPaginatorName](#listrevisionassetspaginatorname)
  - [Origin](#origin)
  - [ServerSideEncryptionTypes](#serversideencryptiontypes)
  - [State](#state)
  - [TypeType](#typetype)

## AssetType

```python
from mypy_boto3_dataexchange.literals import AssetType
```

Values:

- `S3_SNAPSHOT`

## Code

```python
from mypy_boto3_dataexchange.literals import Code
```

Values:

- `ACCESS_DENIED_EXCEPTION`
- `INTERNAL_SERVER_EXCEPTION`
- `MALWARE_DETECTED`
- `MALWARE_SCAN_ENCRYPTED_FILE`
- `RESOURCE_NOT_FOUND_EXCEPTION`
- `SERVICE_QUOTA_EXCEEDED_EXCEPTION`
- `VALIDATION_EXCEPTION`

## JobErrorLimitName

```python
from mypy_boto3_dataexchange.literals import JobErrorLimitName
```

Values:

- `Asset size in GB`
- `Assets per revision`

## JobErrorResourceTypes

```python
from mypy_boto3_dataexchange.literals import JobErrorResourceTypes
```

Values:

- `ASSET`
- `REVISION`

## ListDataSetRevisionsPaginatorName

```python
from mypy_boto3_dataexchange.literals import ListDataSetRevisionsPaginatorName
```

Values:

- `list_data_set_revisions`

## ListDataSetsPaginatorName

```python
from mypy_boto3_dataexchange.literals import ListDataSetsPaginatorName
```

Values:

- `list_data_sets`

## ListJobsPaginatorName

```python
from mypy_boto3_dataexchange.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## ListRevisionAssetsPaginatorName

```python
from mypy_boto3_dataexchange.literals import ListRevisionAssetsPaginatorName
```

Values:

- `list_revision_assets`

## Origin

```python
from mypy_boto3_dataexchange.literals import Origin
```

Values:

- `ENTITLED`
- `OWNED`

## ServerSideEncryptionTypes

```python
from mypy_boto3_dataexchange.literals import ServerSideEncryptionTypes
```

Values:

- `AES256`
- `aws:kms`

## State

```python
from mypy_boto3_dataexchange.literals import State
```

Values:

- `CANCELLED`
- `COMPLETED`
- `ERROR`
- `IN_PROGRESS`
- `TIMED_OUT`
- `WAITING`

## TypeType

```python
from mypy_boto3_dataexchange.literals import TypeType
```

Values:

- `EXPORT_ASSET_TO_SIGNED_URL`
- `EXPORT_ASSETS_TO_S3`
- `EXPORT_REVISIONS_TO_S3`
- `IMPORT_ASSET_FROM_SIGNED_URL`
- `IMPORT_ASSETS_FROM_S3`
