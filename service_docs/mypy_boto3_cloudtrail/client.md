# CloudTrailClient for boto3 CloudTrail module

> [Index](../index.md) > [CloudTrail](./index.md) > CloudTrailClient

Auto-generated documentation for [CloudTrail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail)
type annotations stubs module [mypy_boto3_cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/).

- [CloudTrailClient for boto3 CloudTrail module](#cloudtrailclient-for-boto3-cloudtrail-module)
  - [CloudTrailClient](#cloudtrailclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags](#add_tags)
    - [can_paginate](#can_paginate)
    - [create_trail](#create_trail)
    - [delete_trail](#delete_trail)
    - [describe_trails](#describe_trails)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_event_selectors](#get_event_selectors)
    - [get_insight_selectors](#get_insight_selectors)
    - [get_trail](#get_trail)
    - [get_trail_status](#get_trail_status)
    - [list_public_keys](#list_public_keys)
    - [list_tags](#list_tags)
    - [list_trails](#list_trails)
    - [lookup_events](#lookup_events)
    - [put_event_selectors](#put_event_selectors)
    - [put_insight_selectors](#put_insight_selectors)
    - [remove_tags](#remove_tags)
    - [start_logging](#start_logging)
    - [stop_logging](#stop_logging)
    - [update_trail](#update_trail)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)

## CloudTrailClient

Type annotations for `boto3.client("cloudtrail")`

Can be used directly:

```python
from mypy_boto3_cloudtrail.client import CloudTrailClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudtrail.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CloudTrailARNInvalidException`
- `Exceptions.CloudTrailAccessNotEnabledException`
- `Exceptions.CloudTrailInvalidClientTokenIdException`
- `Exceptions.CloudWatchLogsDeliveryUnavailableException`
- `Exceptions.ConflictException`
- `Exceptions.InsightNotEnabledException`
- `Exceptions.InsufficientDependencyServiceAccessPermissionException`
- `Exceptions.InsufficientEncryptionPolicyException`
- `Exceptions.InsufficientS3BucketPolicyException`
- `Exceptions.InsufficientSnsTopicPolicyException`
- `Exceptions.InvalidCloudWatchLogsLogGroupArnException`
- `Exceptions.InvalidCloudWatchLogsRoleArnException`
- `Exceptions.InvalidEventCategoryException`
- `Exceptions.InvalidEventSelectorsException`
- `Exceptions.InvalidHomeRegionException`
- `Exceptions.InvalidInsightSelectorsException`
- `Exceptions.InvalidKmsKeyIdException`
- `Exceptions.InvalidLookupAttributesException`
- `Exceptions.InvalidMaxResultsException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterCombinationException`
- `Exceptions.InvalidS3BucketNameException`
- `Exceptions.InvalidS3PrefixException`
- `Exceptions.InvalidSnsTopicNameException`
- `Exceptions.InvalidTagParameterException`
- `Exceptions.InvalidTimeRangeException`
- `Exceptions.InvalidTokenException`
- `Exceptions.InvalidTrailNameException`
- `Exceptions.KmsException`
- `Exceptions.KmsKeyDisabledException`
- `Exceptions.KmsKeyNotFoundException`
- `Exceptions.MaximumNumberOfTrailsExceededException`
- `Exceptions.NotOrganizationMasterAccountException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.OrganizationNotInAllFeaturesModeException`
- `Exceptions.OrganizationsNotInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceTypeNotSupportedException`
- `Exceptions.S3BucketDoesNotExistException`
- `Exceptions.TagsLimitExceededException`
- `Exceptions.TrailAlreadyExistsException`
- `Exceptions.TrailNotFoundException`
- `Exceptions.TrailNotProvidedException`
- `Exceptions.UnsupportedOperationException`


## Methods


### add_tags

Type annotations for `boto3.client("cloudtrail").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.add_tags)

```python
def add_tags(
    self,
    ResourceId: str,
    TagsList: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("cloudtrail").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_trail

Type annotations for `boto3.client("cloudtrail").create_trail` method.

[Client.create_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.create_trail)

```python
def create_trail(
    self,
    Name: str,
    S3BucketName: str,
    S3KeyPrefix: str = None,
    SnsTopicName: str = None,
    IncludeGlobalServiceEvents: bool = None,
    IsMultiRegionTrail: bool = None,
    EnableLogFileValidation: bool = None,
    CloudWatchLogsLogGroupArn: str = None,
    CloudWatchLogsRoleArn: str = None,
    KmsKeyId: str = None,
    IsOrganizationTrail: bool = None,
    TagsList: List["TagTypeDef"] = None
) -> CreateTrailResponseTypeDef:
    pass
```

### delete_trail

Type annotations for `boto3.client("cloudtrail").delete_trail` method.

[Client.delete_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.delete_trail)

```python
def delete_trail(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### describe_trails

Type annotations for `boto3.client("cloudtrail").describe_trails` method.

[Client.describe_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.describe_trails)

```python
def describe_trails(
    self,
    trailNameList: List[str] = None,
    includeShadowTrails: bool = None
) -> DescribeTrailsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudtrail").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_event_selectors

Type annotations for `boto3.client("cloudtrail").get_event_selectors` method.

[Client.get_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.get_event_selectors)

```python
def get_event_selectors(
    self,
    TrailName: str
) -> GetEventSelectorsResponseTypeDef:
    pass
```

### get_insight_selectors

Type annotations for `boto3.client("cloudtrail").get_insight_selectors` method.

[Client.get_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.get_insight_selectors)

```python
def get_insight_selectors(
    self,
    TrailName: str
) -> GetInsightSelectorsResponseTypeDef:
    pass
```

### get_trail

Type annotations for `boto3.client("cloudtrail").get_trail` method.

[Client.get_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.get_trail)

```python
def get_trail(
    self,
    Name: str
) -> GetTrailResponseTypeDef:
    pass
```

### get_trail_status

Type annotations for `boto3.client("cloudtrail").get_trail_status` method.

[Client.get_trail_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.get_trail_status)

```python
def get_trail_status(
    self,
    Name: str
) -> GetTrailStatusResponseTypeDef:
    pass
```

### list_public_keys

Type annotations for `boto3.client("cloudtrail").list_public_keys` method.

[Client.list_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.list_public_keys)

```python
def list_public_keys(
    self,
    StartTime: datetime = None,
    EndTime: datetime = None,
    NextToken: str = None
) -> ListPublicKeysResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("cloudtrail").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.list_tags)

```python
def list_tags(
    self,
    ResourceIdList: List[str],
    NextToken: str = None
) -> ListTagsResponseTypeDef:
    pass
```

### list_trails

Type annotations for `boto3.client("cloudtrail").list_trails` method.

[Client.list_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.list_trails)

```python
def list_trails(
    self,
    NextToken: str = None
) -> ListTrailsResponseTypeDef:
    pass
```

### lookup_events

Type annotations for `boto3.client("cloudtrail").lookup_events` method.

[Client.lookup_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events)

```python
def lookup_events(
    self,
    LookupAttributes: List[LookupAttributeTypeDef] = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    EventCategory: EventCategory = None,
    MaxResults: int = None,
    NextToken: str = None
) -> LookupEventsResponseTypeDef:
    pass
```

### put_event_selectors

Type annotations for `boto3.client("cloudtrail").put_event_selectors` method.

[Client.put_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.put_event_selectors)

```python
def put_event_selectors(
    self,
    TrailName: str,
    EventSelectors: List["EventSelectorTypeDef"] = None,
    AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"] = None
) -> PutEventSelectorsResponseTypeDef:
    pass
```

### put_insight_selectors

Type annotations for `boto3.client("cloudtrail").put_insight_selectors` method.

[Client.put_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.put_insight_selectors)

```python
def put_insight_selectors(
    self,
    TrailName: str,
    InsightSelectors: List["InsightSelectorTypeDef"]
) -> PutInsightSelectorsResponseTypeDef:
    pass
```

### remove_tags

Type annotations for `boto3.client("cloudtrail").remove_tags` method.

[Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.remove_tags)

```python
def remove_tags(
    self,
    ResourceId: str,
    TagsList: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### start_logging

Type annotations for `boto3.client("cloudtrail").start_logging` method.

[Client.start_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.start_logging)

```python
def start_logging(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### stop_logging

Type annotations for `boto3.client("cloudtrail").stop_logging` method.

[Client.stop_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.stop_logging)

```python
def stop_logging(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### update_trail

Type annotations for `boto3.client("cloudtrail").update_trail` method.

[Client.update_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.update_trail)

```python
def update_trail(
    self,
    Name: str,
    S3BucketName: str = None,
    S3KeyPrefix: str = None,
    SnsTopicName: str = None,
    IncludeGlobalServiceEvents: bool = None,
    IsMultiRegionTrail: bool = None,
    EnableLogFileValidation: bool = None,
    CloudWatchLogsLogGroupArn: str = None,
    CloudWatchLogsRoleArn: str = None,
    KmsKeyId: str = None,
    IsOrganizationTrail: bool = None
) -> UpdateTrailResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudtrail").get_paginator` method.

[Paginator.ListPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPublicKeysPaginatorName
) -> ListPublicKeysPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudtrail").get_paginator` method.

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsPaginatorName
) -> ListTagsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudtrail").get_paginator` method.

[Paginator.ListTrails documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTrailsPaginatorName
) -> ListTrailsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudtrail").get_paginator` method.

[Paginator.LookupEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: LookupEventsPaginatorName
) -> LookupEventsPaginator:
    pass
```