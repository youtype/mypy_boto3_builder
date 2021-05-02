# PersonalizeEventsClient for boto3 PersonalizeEvents module

> [Index](../index.md) > [PersonalizeEvents](./index.md) > PersonalizeEventsClient

Auto-generated documentation for [PersonalizeEvents](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents)
type annotations stubs module [mypy_boto3_personalize_events](https://pypi.org/project/mypy-boto3-personalize-events/).

- [PersonalizeEventsClient for boto3 PersonalizeEvents module](#personalizeeventsclient-for-boto3-personalizeevents-module)
  - [PersonalizeEventsClient](#personalizeeventsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [put_events](#put_events)
    - [put_items](#put_items)
    - [put_users](#put_users)

## PersonalizeEventsClient

Type annotations for `boto3.client("personalize-events")`

Can be used directly:

```python
from mypy_boto3_personalize_events.client import PersonalizeEventsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_personalize_events.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("personalize-events").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("personalize-events").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.generate_presigned_url)

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

### put_events

Type annotations for `boto3.client("personalize-events").put_events` method.

[Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_events)

```python
def put_events(
    self,
    trackingId: str,
    sessionId: str,
    eventList: List[EventTypeDef],
    userId: str = None
) -> None:
    pass
```

### put_items

Type annotations for `boto3.client("personalize-events").put_items` method.

[Client.put_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_items)

```python
def put_items(
    self,
    datasetArn: str,
    items: List[ItemTypeDef]
) -> None:
    pass
```

### put_users

Type annotations for `boto3.client("personalize-events").put_users` method.

[Client.put_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_users)

```python
def put_users(
    self,
    datasetArn: str,
    users: List[UserTypeDef]
) -> None:
    pass
```



