# Paginators for boto3 AmplifyBackend module

> [Index](../index.md) > [AmplifyBackend](./index.md) > Paginators

Auto-generated documentation for [AmplifyBackend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend)
type annotations stubs module [mypy_boto3_amplifybackend](https://pypi.org/project/mypy-boto3-amplifybackend/).

- [Paginators for boto3 AmplifyBackend module](#paginators-for-boto3-amplifybackend-module)
  - [ListBackendJobsPaginator](#listbackendjobspaginator)

## ListBackendJobsPaginator

Type annotations for `boto3.client("amplifybackend").get_paginator("list_backend_jobs")`.

Can be used directly:

```python
from mypy_boto3_amplifybackend.paginators import ListBackendJobsPaginator

def get_list_backend_jobs_paginator() -> ListBackendJobsPaginator:
    return boto3.client("amplifybackend").get_paginator("list_backend_jobs")
```

[Paginator.ListBackendJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Paginator.ListBackendJobs)

```python
class ListBackendJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        AppId: str,
        BackendEnvironmentName: str,
        JobId: str = None,
        Operation: str = None,
        Status: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBackendJobsResponseTypeDef]:
        pass
```