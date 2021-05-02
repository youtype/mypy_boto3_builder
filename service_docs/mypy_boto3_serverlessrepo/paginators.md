# Paginators for boto3 ServerlessApplicationRepository module

> [Index](../index.md) > [ServerlessApplicationRepository](./index.md) > Paginators

Auto-generated documentation for [ServerlessApplicationRepository](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository)
type annotations stubs module [mypy_boto3_serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo/).

- [Paginators for boto3 ServerlessApplicationRepository module](#paginators-for-boto3-serverlessapplicationrepository-module)
  - [ListApplicationDependenciesPaginator](#listapplicationdependenciespaginator)
  - [ListApplicationVersionsPaginator](#listapplicationversionspaginator)
  - [ListApplicationsPaginator](#listapplicationspaginator)

## ListApplicationDependenciesPaginator

Type annotations for `boto3.client("serverlessrepo").get_paginator("list_application_dependencies")`.

Can be used directly:

```python
from mypy_boto3_serverlessrepo.paginators import ListApplicationDependenciesPaginator

def get_list_application_dependencies_paginator() -> ListApplicationDependenciesPaginator:
    return boto3.client("serverlessrepo").get_paginator("list_application_dependencies")
```

[Paginator.ListApplicationDependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)

```python
class ListApplicationDependenciesPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationId: str,
        SemanticVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationDependenciesResponseTypeDef]:
        pass
```
## ListApplicationVersionsPaginator

Type annotations for `boto3.client("serverlessrepo").get_paginator("list_application_versions")`.

Can be used directly:

```python
from mypy_boto3_serverlessrepo.paginators import ListApplicationVersionsPaginator

def get_list_application_versions_paginator() -> ListApplicationVersionsPaginator:
    return boto3.client("serverlessrepo").get_paginator("list_application_versions")
```

[Paginator.ListApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)

```python
class ListApplicationVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationVersionsResponseTypeDef]:
        pass
```
## ListApplicationsPaginator

Type annotations for `boto3.client("serverlessrepo").get_paginator("list_applications")`.

Can be used directly:

```python
from mypy_boto3_serverlessrepo.paginators import ListApplicationsPaginator

def get_list_applications_paginator() -> ListApplicationsPaginator:
    return boto3.client("serverlessrepo").get_paginator("list_applications")
```

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)

```python
class ListApplicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        pass
```