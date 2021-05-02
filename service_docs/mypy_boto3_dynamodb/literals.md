# Literals for boto3 DynamoDB module

> [Index](../index.md) > [DynamoDB](./index.md) > Literals

Auto-generated documentation for [DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB)
type annotations stubs module [mypy_boto3_dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/).

- [Literals for boto3 DynamoDB module](#literals-for-boto3-dynamodb-module)
  - [AttributeAction](#attributeaction)
  - [BackupStatus](#backupstatus)
  - [BackupType](#backuptype)
  - [BackupTypeFilter](#backuptypefilter)
  - [BatchStatementErrorCodeEnum](#batchstatementerrorcodeenum)
  - [BillingMode](#billingmode)
  - [ComparisonOperator](#comparisonoperator)
  - [ConditionalOperator](#conditionaloperator)
  - [ContinuousBackupsStatus](#continuousbackupsstatus)
  - [ContributorInsightsAction](#contributorinsightsaction)
  - [ContributorInsightsStatus](#contributorinsightsstatus)
  - [DestinationStatus](#destinationstatus)
  - [ExportFormat](#exportformat)
  - [ExportStatus](#exportstatus)
  - [GlobalTableStatus](#globaltablestatus)
  - [IndexStatus](#indexstatus)
  - [KeyType](#keytype)
  - [ListBackupsPaginatorName](#listbackupspaginatorname)
  - [ListTablesPaginatorName](#listtablespaginatorname)
  - [ListTagsOfResourcePaginatorName](#listtagsofresourcepaginatorname)
  - [PointInTimeRecoveryStatus](#pointintimerecoverystatus)
  - [ProjectionType](#projectiontype)
  - [QueryPaginatorName](#querypaginatorname)
  - [ReplicaStatus](#replicastatus)
  - [ReturnConsumedCapacity](#returnconsumedcapacity)
  - [ReturnItemCollectionMetrics](#returnitemcollectionmetrics)
  - [ReturnValue](#returnvalue)
  - [ReturnValuesOnConditionCheckFailure](#returnvaluesonconditioncheckfailure)
  - [S3SseAlgorithm](#s3ssealgorithm)
  - [SSEStatus](#ssestatus)
  - [SSEType](#ssetype)
  - [ScalarAttributeType](#scalarattributetype)
  - [ScanPaginatorName](#scanpaginatorname)
  - [Select](#select)
  - [StreamViewType](#streamviewtype)
  - [TableExistsWaiterName](#tableexistswaitername)
  - [TableNotExistsWaiterName](#tablenotexistswaitername)
  - [TableStatus](#tablestatus)
  - [TimeToLiveStatus](#timetolivestatus)

## AttributeAction

```python
from mypy_boto3_dynamodb.literals import AttributeAction
```

Values:

- `ADD`
- `DELETE`
- `PUT`

## BackupStatus

```python
from mypy_boto3_dynamodb.literals import BackupStatus
```

Values:

- `AVAILABLE`
- `CREATING`
- `DELETED`

## BackupType

```python
from mypy_boto3_dynamodb.literals import BackupType
```

Values:

- `AWS_BACKUP`
- `SYSTEM`
- `USER`

## BackupTypeFilter

```python
from mypy_boto3_dynamodb.literals import BackupTypeFilter
```

Values:

- `ALL`
- `AWS_BACKUP`
- `SYSTEM`
- `USER`

## BatchStatementErrorCodeEnum

```python
from mypy_boto3_dynamodb.literals import BatchStatementErrorCodeEnum
```

Values:

- `AccessDenied`
- `ConditionalCheckFailed`
- `DuplicateItem`
- `InternalServerError`
- `ItemCollectionSizeLimitExceeded`
- `ProvisionedThroughputExceeded`
- `RequestLimitExceeded`
- `ResourceNotFound`
- `ThrottlingError`
- `TransactionConflict`
- `ValidationError`

## BillingMode

```python
from mypy_boto3_dynamodb.literals import BillingMode
```

Values:

- `PAY_PER_REQUEST`
- `PROVISIONED`

## ComparisonOperator

```python
from mypy_boto3_dynamodb.literals import ComparisonOperator
```

Values:

- `BEGINS_WITH`
- `BETWEEN`
- `CONTAINS`
- `EQ`
- `GE`
- `GT`
- `IN`
- `LE`
- `LT`
- `NE`
- `NOT_CONTAINS`
- `NOT_NULL`
- `NULL`

## ConditionalOperator

```python
from mypy_boto3_dynamodb.literals import ConditionalOperator
```

Values:

- `AND`
- `OR`

## ContinuousBackupsStatus

```python
from mypy_boto3_dynamodb.literals import ContinuousBackupsStatus
```

Values:

- `DISABLED`
- `ENABLED`

## ContributorInsightsAction

```python
from mypy_boto3_dynamodb.literals import ContributorInsightsAction
```

Values:

- `DISABLE`
- `ENABLE`

## ContributorInsightsStatus

```python
from mypy_boto3_dynamodb.literals import ContributorInsightsStatus
```

Values:

- `DISABLED`
- `DISABLING`
- `ENABLED`
- `ENABLING`
- `FAILED`

## DestinationStatus

```python
from mypy_boto3_dynamodb.literals import DestinationStatus
```

Values:

- `ACTIVE`
- `DISABLED`
- `DISABLING`
- `ENABLE_FAILED`
- `ENABLING`

## ExportFormat

```python
from mypy_boto3_dynamodb.literals import ExportFormat
```

Values:

- `DYNAMODB_JSON`
- `ION`

## ExportStatus

```python
from mypy_boto3_dynamodb.literals import ExportStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`

## GlobalTableStatus

```python
from mypy_boto3_dynamodb.literals import GlobalTableStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `UPDATING`

## IndexStatus

```python
from mypy_boto3_dynamodb.literals import IndexStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `UPDATING`

## KeyType

```python
from mypy_boto3_dynamodb.literals import KeyType
```

Values:

- `HASH`
- `RANGE`

## ListBackupsPaginatorName

```python
from mypy_boto3_dynamodb.literals import ListBackupsPaginatorName
```

Values:

- `list_backups`

## ListTablesPaginatorName

```python
from mypy_boto3_dynamodb.literals import ListTablesPaginatorName
```

Values:

- `list_tables`

## ListTagsOfResourcePaginatorName

```python
from mypy_boto3_dynamodb.literals import ListTagsOfResourcePaginatorName
```

Values:

- `list_tags_of_resource`

## PointInTimeRecoveryStatus

```python
from mypy_boto3_dynamodb.literals import PointInTimeRecoveryStatus
```

Values:

- `DISABLED`
- `ENABLED`

## ProjectionType

```python
from mypy_boto3_dynamodb.literals import ProjectionType
```

Values:

- `ALL`
- `INCLUDE`
- `KEYS_ONLY`

## QueryPaginatorName

```python
from mypy_boto3_dynamodb.literals import QueryPaginatorName
```

Values:

- `query`

## ReplicaStatus

```python
from mypy_boto3_dynamodb.literals import ReplicaStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `CREATION_FAILED`
- `DELETING`
- `INACCESSIBLE_ENCRYPTION_CREDENTIALS`
- `REGION_DISABLED`
- `UPDATING`

## ReturnConsumedCapacity

```python
from mypy_boto3_dynamodb.literals import ReturnConsumedCapacity
```

Values:

- `INDEXES`
- `NONE`
- `TOTAL`

## ReturnItemCollectionMetrics

```python
from mypy_boto3_dynamodb.literals import ReturnItemCollectionMetrics
```

Values:

- `NONE`
- `SIZE`

## ReturnValue

```python
from mypy_boto3_dynamodb.literals import ReturnValue
```

Values:

- `ALL_NEW`
- `ALL_OLD`
- `NONE`
- `UPDATED_NEW`
- `UPDATED_OLD`

## ReturnValuesOnConditionCheckFailure

```python
from mypy_boto3_dynamodb.literals import ReturnValuesOnConditionCheckFailure
```

Values:

- `ALL_OLD`
- `NONE`

## S3SseAlgorithm

```python
from mypy_boto3_dynamodb.literals import S3SseAlgorithm
```

Values:

- `AES256`
- `KMS`

## SSEStatus

```python
from mypy_boto3_dynamodb.literals import SSEStatus
```

Values:

- `DISABLED`
- `DISABLING`
- `ENABLED`
- `ENABLING`
- `UPDATING`

## SSEType

```python
from mypy_boto3_dynamodb.literals import SSEType
```

Values:

- `AES256`
- `KMS`

## ScalarAttributeType

```python
from mypy_boto3_dynamodb.literals import ScalarAttributeType
```

Values:

- `B`
- `N`
- `S`

## ScanPaginatorName

```python
from mypy_boto3_dynamodb.literals import ScanPaginatorName
```

Values:

- `scan`

## Select

```python
from mypy_boto3_dynamodb.literals import Select
```

Values:

- `ALL_ATTRIBUTES`
- `ALL_PROJECTED_ATTRIBUTES`
- `COUNT`
- `SPECIFIC_ATTRIBUTES`

## StreamViewType

```python
from mypy_boto3_dynamodb.literals import StreamViewType
```

Values:

- `KEYS_ONLY`
- `NEW_AND_OLD_IMAGES`
- `NEW_IMAGE`
- `OLD_IMAGE`

## TableExistsWaiterName

```python
from mypy_boto3_dynamodb.literals import TableExistsWaiterName
```

Values:

- `table_exists`

## TableNotExistsWaiterName

```python
from mypy_boto3_dynamodb.literals import TableNotExistsWaiterName
```

Values:

- `table_not_exists`

## TableStatus

```python
from mypy_boto3_dynamodb.literals import TableStatus
```

Values:

- `ACTIVE`
- `ARCHIVED`
- `ARCHIVING`
- `CREATING`
- `DELETING`
- `INACCESSIBLE_ENCRYPTION_CREDENTIALS`
- `UPDATING`

## TimeToLiveStatus

```python
from mypy_boto3_dynamodb.literals import TimeToLiveStatus
```

Values:

- `DISABLED`
- `DISABLING`
- `ENABLED`
- `ENABLING`
