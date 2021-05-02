# SignerClient for boto3 Signer module

> [Index](../index.md) > [Signer](./index.md) > SignerClient

Auto-generated documentation for [Signer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer)
type annotations stubs module [mypy_boto3_signer](https://pypi.org/project/mypy-boto3-signer/).

- [SignerClient for boto3 Signer module](#signerclient-for-boto3-signer-module)
  - [SignerClient](#signerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_profile_permission](#add_profile_permission)
    - [can_paginate](#can_paginate)
    - [cancel_signing_profile](#cancel_signing_profile)
    - [describe_signing_job](#describe_signing_job)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_signing_platform](#get_signing_platform)
    - [get_signing_profile](#get_signing_profile)
    - [list_profile_permissions](#list_profile_permissions)
    - [list_signing_jobs](#list_signing_jobs)
    - [list_signing_platforms](#list_signing_platforms)
    - [list_signing_profiles](#list_signing_profiles)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_signing_profile](#put_signing_profile)
    - [remove_profile_permission](#remove_profile_permission)
    - [revoke_signature](#revoke_signature)
    - [revoke_signing_profile](#revoke_signing_profile)
    - [start_signing_job](#start_signing_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## SignerClient

Type annotations for `boto3.client("signer")`

Can be used directly:

```python
from mypy_boto3_signer.client import SignerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_signer.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceLimitExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.ValidationException`


## Methods


### add_profile_permission

Type annotations for `boto3.client("signer").add_profile_permission` method.

[Client.add_profile_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.add_profile_permission)

```python
def add_profile_permission(
    self,
    profileName: str,
    action: str,
    principal: str,
    statementId: str,
    profileVersion: str = None,
    revisionId: str = None
) -> AddProfilePermissionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("signer").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_signing_profile

Type annotations for `boto3.client("signer").cancel_signing_profile` method.

[Client.cancel_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.cancel_signing_profile)

```python
def cancel_signing_profile(
    self,
    profileName: str
) -> None:
    pass
```

### describe_signing_job

Type annotations for `boto3.client("signer").describe_signing_job` method.

[Client.describe_signing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.describe_signing_job)

```python
def describe_signing_job(
    self,
    jobId: str
) -> DescribeSigningJobResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("signer").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.generate_presigned_url)

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

### get_signing_platform

Type annotations for `boto3.client("signer").get_signing_platform` method.

[Client.get_signing_platform documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.get_signing_platform)

```python
def get_signing_platform(
    self,
    platformId: str
) -> GetSigningPlatformResponseTypeDef:
    pass
```

### get_signing_profile

Type annotations for `boto3.client("signer").get_signing_profile` method.

[Client.get_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.get_signing_profile)

```python
def get_signing_profile(
    self,
    profileName: str,
    profileOwner: str = None
) -> GetSigningProfileResponseTypeDef:
    pass
```

### list_profile_permissions

Type annotations for `boto3.client("signer").list_profile_permissions` method.

[Client.list_profile_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.list_profile_permissions)

```python
def list_profile_permissions(
    self,
    profileName: str,
    nextToken: str = None
) -> ListProfilePermissionsResponseTypeDef:
    pass
```

### list_signing_jobs

Type annotations for `boto3.client("signer").list_signing_jobs` method.

[Client.list_signing_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.list_signing_jobs)

```python
def list_signing_jobs(
    self,
    status: SigningStatus = None,
    platformId: str = None,
    requestedBy: str = None,
    maxResults: int = None,
    nextToken: str = None,
    isRevoked: bool = None,
    signatureExpiresBefore: datetime = None,
    signatureExpiresAfter: datetime = None,
    jobInvoker: str = None
) -> ListSigningJobsResponseTypeDef:
    pass
```

### list_signing_platforms

Type annotations for `boto3.client("signer").list_signing_platforms` method.

[Client.list_signing_platforms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.list_signing_platforms)

```python
def list_signing_platforms(
    self,
    category: str = None,
    partner: str = None,
    target: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListSigningPlatformsResponseTypeDef:
    pass
```

### list_signing_profiles

Type annotations for `boto3.client("signer").list_signing_profiles` method.

[Client.list_signing_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.list_signing_profiles)

```python
def list_signing_profiles(
    self,
    includeCanceled: bool = None,
    maxResults: int = None,
    nextToken: str = None,
    platformId: str = None,
    statuses: List[SigningProfileStatus] = None
) -> ListSigningProfilesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("signer").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_signing_profile

Type annotations for `boto3.client("signer").put_signing_profile` method.

[Client.put_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.put_signing_profile)

```python
def put_signing_profile(
    self,
    profileName: str,
    platformId: str,
    signingMaterial: "SigningMaterialTypeDef" = None,
    signatureValidityPeriod: "SignatureValidityPeriodTypeDef" = None,
    overrides: "SigningPlatformOverridesTypeDef" = None,
    signingParameters: Dict[str, str] = None,
    tags: Dict[str, str] = None
) -> PutSigningProfileResponseTypeDef:
    pass
```

### remove_profile_permission

Type annotations for `boto3.client("signer").remove_profile_permission` method.

[Client.remove_profile_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.remove_profile_permission)

```python
def remove_profile_permission(
    self,
    profileName: str,
    revisionId: str,
    statementId: str
) -> RemoveProfilePermissionResponseTypeDef:
    pass
```

### revoke_signature

Type annotations for `boto3.client("signer").revoke_signature` method.

[Client.revoke_signature documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.revoke_signature)

```python
def revoke_signature(
    self,
    jobId: str,
    reason: str,
    jobOwner: str = None
) -> None:
    pass
```

### revoke_signing_profile

Type annotations for `boto3.client("signer").revoke_signing_profile` method.

[Client.revoke_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.revoke_signing_profile)

```python
def revoke_signing_profile(
    self,
    profileName: str,
    profileVersion: str,
    reason: str,
    effectiveTime: datetime
) -> None:
    pass
```

### start_signing_job

Type annotations for `boto3.client("signer").start_signing_job` method.

[Client.start_signing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.start_signing_job)

```python
def start_signing_job(
    self,
    source: "SourceTypeDef",
    destination: DestinationTypeDef,
    profileName: str,
    clientRequestToken: str,
    profileOwner: str = None
) -> StartSigningJobResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("signer").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("signer").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("signer").get_paginator` method with overloads.

- `client.get_paginator("list_signing_jobs")` -> [ListSigningJobsPaginator](./paginators.md#listsigningjobspaginator)
- `client.get_paginator("list_signing_platforms")` -> [ListSigningPlatformsPaginator](./paginators.md#listsigningplatformspaginator)
- `client.get_paginator("list_signing_profiles")` -> [ListSigningProfilesPaginator](./paginators.md#listsigningprofilespaginator)




### get_waiter

Type annotations for `boto3.client("signer").get_waiter` method with overloads.

- `client.get_waiter("successful_signing_job")` -> [SuccessfulSigningJobWaiter](./waiters.md#successfulsigningjobwaiter)
