# Paginators for boto3 Signer module

> [Index](../index.md) > [Signer](./index.md) > Paginators

Auto-generated documentation for [Signer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer)
type annotations stubs module [mypy_boto3_signer](https://pypi.org/project/mypy-boto3-signer/).

- [Paginators for boto3 Signer module](#paginators-for-boto3-signer-module)
  - [ListSigningJobsPaginator](#listsigningjobspaginator)
  - [ListSigningPlatformsPaginator](#listsigningplatformspaginator)
  - [ListSigningProfilesPaginator](#listsigningprofilespaginator)

## ListSigningJobsPaginator

Type annotations for `boto3.client("signer").get_paginator("list_signing_jobs")`.

Can be used directly:

```python
from mypy_boto3_signer.paginators import ListSigningJobsPaginator

def get_list_signing_jobs_paginator() -> ListSigningJobsPaginator:
    return boto3.client("signer").get_paginator("list_signing_jobs")
```

[Paginator.ListSigningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Paginator.ListSigningJobs)

```python
class ListSigningJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        status: SigningStatus = None,
        platformId: str = None,
        requestedBy: str = None,
        isRevoked: bool = None,
        signatureExpiresBefore: datetime = None,
        signatureExpiresAfter: datetime = None,
        jobInvoker: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningJobsResponseTypeDef]:
        pass
```
## ListSigningPlatformsPaginator

Type annotations for `boto3.client("signer").get_paginator("list_signing_platforms")`.

Can be used directly:

```python
from mypy_boto3_signer.paginators import ListSigningPlatformsPaginator

def get_list_signing_platforms_paginator() -> ListSigningPlatformsPaginator:
    return boto3.client("signer").get_paginator("list_signing_platforms")
```

[Paginator.ListSigningPlatforms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)

```python
class ListSigningPlatformsPaginator(Boto3Paginator):
    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningPlatformsResponseTypeDef]:
        pass
```
## ListSigningProfilesPaginator

Type annotations for `boto3.client("signer").get_paginator("list_signing_profiles")`.

Can be used directly:

```python
from mypy_boto3_signer.paginators import ListSigningProfilesPaginator

def get_list_signing_profiles_paginator() -> ListSigningProfilesPaginator:
    return boto3.client("signer").get_paginator("list_signing_profiles")
```

[Paginator.ListSigningProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)

```python
class ListSigningProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        includeCanceled: bool = None,
        platformId: str = None,
        statuses: List[SigningProfileStatus] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSigningProfilesResponseTypeDef]:
        pass
```