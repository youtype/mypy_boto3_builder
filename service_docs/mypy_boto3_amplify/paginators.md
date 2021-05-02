# Paginators for boto3 Amplify module

> [Index](../index.md) > [Amplify](./index.md) > Paginators

Auto-generated documentation for [Amplify](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify)
type annotations stubs module [mypy_boto3_amplify](https://pypi.org/project/mypy-boto3-amplify/).

- [Paginators for boto3 Amplify module](#paginators-for-boto3-amplify-module)
  - [ListAppsPaginator](#listappspaginator)
  - [ListBranchesPaginator](#listbranchespaginator)
  - [ListDomainAssociationsPaginator](#listdomainassociationspaginator)
  - [ListJobsPaginator](#listjobspaginator)

## ListAppsPaginator

Type annotations for `boto3.client("amplify").get_paginator("list_apps")`.

Can be used directly:

```python
from mypy_boto3_amplify.paginators import ListAppsPaginator

def get_list_apps_paginator() -> ListAppsPaginator:
    return boto3.client("amplify").get_paginator("list_apps")
```

[Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Paginator.ListApps)

```python
class ListAppsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppsResultTypeDef]:
        pass
```
## ListBranchesPaginator

Type annotations for `boto3.client("amplify").get_paginator("list_branches")`.

Can be used directly:

```python
from mypy_boto3_amplify.paginators import ListBranchesPaginator

def get_list_branches_paginator() -> ListBranchesPaginator:
    return boto3.client("amplify").get_paginator("list_branches")
```

[Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Paginator.ListBranches)

```python
class ListBranchesPaginator(Boto3Paginator):
    def paginate(
        self,
        appId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBranchesResultTypeDef]:
        pass
```
## ListDomainAssociationsPaginator

Type annotations for `boto3.client("amplify").get_paginator("list_domain_associations")`.

Can be used directly:

```python
from mypy_boto3_amplify.paginators import ListDomainAssociationsPaginator

def get_list_domain_associations_paginator() -> ListDomainAssociationsPaginator:
    return boto3.client("amplify").get_paginator("list_domain_associations")
```

[Paginator.ListDomainAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Paginator.ListDomainAssociations)

```python
class ListDomainAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        appId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainAssociationsResultTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("amplify").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_amplify.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("amplify").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        appId: str,
        branchName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResultTypeDef]:
        pass
```