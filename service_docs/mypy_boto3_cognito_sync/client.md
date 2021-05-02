# CognitoSyncClient for boto3 CognitoSync module

> [Index](../index.md) > [CognitoSync](./index.md) > CognitoSyncClient

Auto-generated documentation for [CognitoSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync)
type annotations stubs module [mypy_boto3_cognito_sync](https://pypi.org/project/mypy-boto3-cognito-sync/).

- [CognitoSyncClient for boto3 CognitoSync module](#cognitosyncclient-for-boto3-cognitosync-module)
  - [CognitoSyncClient](#cognitosyncclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [bulk_publish](#bulk_publish)
    - [can_paginate](#can_paginate)
    - [delete_dataset](#delete_dataset)
    - [describe_dataset](#describe_dataset)
    - [describe_identity_pool_usage](#describe_identity_pool_usage)
    - [describe_identity_usage](#describe_identity_usage)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_bulk_publish_details](#get_bulk_publish_details)
    - [get_cognito_events](#get_cognito_events)
    - [get_identity_pool_configuration](#get_identity_pool_configuration)
    - [list_datasets](#list_datasets)
    - [list_identity_pool_usage](#list_identity_pool_usage)
    - [list_records](#list_records)
    - [register_device](#register_device)
    - [set_cognito_events](#set_cognito_events)
    - [set_identity_pool_configuration](#set_identity_pool_configuration)
    - [subscribe_to_dataset](#subscribe_to_dataset)
    - [unsubscribe_from_dataset](#unsubscribe_from_dataset)
    - [update_records](#update_records)

## CognitoSyncClient

Type annotations for `boto3.client("cognito-sync")`

Can be used directly:

```python
from mypy_boto3_cognito_sync.client import CognitoSyncClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cognito_sync.client import Exceptions

def handle_error(exc: Exceptions.AlreadyStreamedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyStreamedException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.DuplicateRequestException`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidConfigurationException`
- `Exceptions.InvalidLambdaFunctionOutputException`
- `Exceptions.InvalidParameterException`
- `Exceptions.LambdaThrottledException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### bulk_publish

Type annotations for `boto3.client("cognito-sync").bulk_publish` method.

[Client.bulk_publish documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.bulk_publish)

```python
def bulk_publish(
    self,
    IdentityPoolId: str
) -> BulkPublishResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("cognito-sync").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_dataset

Type annotations for `boto3.client("cognito-sync").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.delete_dataset)

```python
def delete_dataset(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str
) -> DeleteDatasetResponseTypeDef:
    pass
```

### describe_dataset

Type annotations for `boto3.client("cognito-sync").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.describe_dataset)

```python
def describe_dataset(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_identity_pool_usage

Type annotations for `boto3.client("cognito-sync").describe_identity_pool_usage` method.

[Client.describe_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_pool_usage)

```python
def describe_identity_pool_usage(
    self,
    IdentityPoolId: str
) -> DescribeIdentityPoolUsageResponseTypeDef:
    pass
```

### describe_identity_usage

Type annotations for `boto3.client("cognito-sync").describe_identity_usage` method.

[Client.describe_identity_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_usage)

```python
def describe_identity_usage(
    self,
    IdentityPoolId: str,
    IdentityId: str
) -> DescribeIdentityUsageResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cognito-sync").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.generate_presigned_url)

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

### get_bulk_publish_details

Type annotations for `boto3.client("cognito-sync").get_bulk_publish_details` method.

[Client.get_bulk_publish_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.get_bulk_publish_details)

```python
def get_bulk_publish_details(
    self,
    IdentityPoolId: str
) -> GetBulkPublishDetailsResponseTypeDef:
    pass
```

### get_cognito_events

Type annotations for `boto3.client("cognito-sync").get_cognito_events` method.

[Client.get_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.get_cognito_events)

```python
def get_cognito_events(
    self,
    IdentityPoolId: str
) -> GetCognitoEventsResponseTypeDef:
    pass
```

### get_identity_pool_configuration

Type annotations for `boto3.client("cognito-sync").get_identity_pool_configuration` method.

[Client.get_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.get_identity_pool_configuration)

```python
def get_identity_pool_configuration(
    self,
    IdentityPoolId: str
) -> GetIdentityPoolConfigurationResponseTypeDef:
    pass
```

### list_datasets

Type annotations for `boto3.client("cognito-sync").list_datasets` method.

[Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.list_datasets)

```python
def list_datasets(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDatasetsResponseTypeDef:
    pass
```

### list_identity_pool_usage

Type annotations for `boto3.client("cognito-sync").list_identity_pool_usage` method.

[Client.list_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.list_identity_pool_usage)

```python
def list_identity_pool_usage(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListIdentityPoolUsageResponseTypeDef:
    pass
```

### list_records

Type annotations for `boto3.client("cognito-sync").list_records` method.

[Client.list_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.list_records)

```python
def list_records(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    LastSyncCount: int = None,
    NextToken: str = None,
    MaxResults: int = None,
    SyncSessionToken: str = None
) -> ListRecordsResponseTypeDef:
    pass
```

### register_device

Type annotations for `boto3.client("cognito-sync").register_device` method.

[Client.register_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.register_device)

```python
def register_device(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    Platform: Platform,
    Token: str
) -> RegisterDeviceResponseTypeDef:
    pass
```

### set_cognito_events

Type annotations for `boto3.client("cognito-sync").set_cognito_events` method.

[Client.set_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.set_cognito_events)

```python
def set_cognito_events(
    self,
    IdentityPoolId: str,
    Events: Dict[str, str]
) -> None:
    pass
```

### set_identity_pool_configuration

Type annotations for `boto3.client("cognito-sync").set_identity_pool_configuration` method.

[Client.set_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.set_identity_pool_configuration)

```python
def set_identity_pool_configuration(
    self,
    IdentityPoolId: str,
    PushSync: "PushSyncTypeDef" = None,
    CognitoStreams: "CognitoStreamsTypeDef" = None
) -> SetIdentityPoolConfigurationResponseTypeDef:
    pass
```

### subscribe_to_dataset

Type annotations for `boto3.client("cognito-sync").subscribe_to_dataset` method.

[Client.subscribe_to_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.subscribe_to_dataset)

```python
def subscribe_to_dataset(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    DeviceId: str
) -> Dict[str, Any]:
    pass
```

### unsubscribe_from_dataset

Type annotations for `boto3.client("cognito-sync").unsubscribe_from_dataset` method.

[Client.unsubscribe_from_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.unsubscribe_from_dataset)

```python
def unsubscribe_from_dataset(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    DeviceId: str
) -> Dict[str, Any]:
    pass
```

### update_records

Type annotations for `boto3.client("cognito-sync").update_records` method.

[Client.update_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client.update_records)

```python
def update_records(
    self,
    IdentityPoolId: str,
    IdentityId: str,
    DatasetName: str,
    SyncSessionToken: str,
    DeviceId: str = None,
    RecordPatches: List[RecordPatchTypeDef] = None,
    ClientContext: str = None
) -> UpdateRecordsResponseTypeDef:
    pass
```



