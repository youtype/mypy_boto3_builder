# ConnectContactLensClient for boto3 ConnectContactLens module

> [Index](../index.md) > [ConnectContactLens](./index.md) > ConnectContactLensClient

Auto-generated documentation for [ConnectContactLens](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html#ConnectContactLens)
type annotations stubs module [mypy_boto3_connect_contact_lens](https://pypi.org/project/mypy-boto3-connect-contact-lens/).

- [ConnectContactLensClient for boto3 ConnectContactLens module](#connectcontactlensclient-for-boto3-connectcontactlens-module)
  - [ConnectContactLensClient](#connectcontactlensclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_realtime_contact_analysis_segments](#list_realtime_contact_analysis_segments)

## ConnectContactLensClient

Type annotations for `boto3.client("connect-contact-lens")`

Can be used directly:

```python
from mypy_boto3_connect_contact_lens.client import ConnectContactLensClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_connect_contact_lens.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("connect-contact-lens").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html#ConnectContactLens.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("connect-contact-lens").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html#ConnectContactLens.Client.generate_presigned_url)

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

### list_realtime_contact_analysis_segments

Type annotations for `boto3.client("connect-contact-lens").list_realtime_contact_analysis_segments` method.

[Client.list_realtime_contact_analysis_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html#ConnectContactLens.Client.list_realtime_contact_analysis_segments)

```python
def list_realtime_contact_analysis_segments(
    self,
    InstanceId: str,
    ContactId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRealtimeContactAnalysisSegmentsResponseTypeDef:
    pass
```