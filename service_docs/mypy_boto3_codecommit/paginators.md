# Paginators for boto3 CodeCommit module

> [Index](../index.md) > [CodeCommit](./index.md) > Paginators

Auto-generated documentation for [CodeCommit](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit)
type annotations stubs module [mypy_boto3_codecommit](https://pypi.org/project/mypy-boto3-codecommit/).

- [Paginators for boto3 CodeCommit module](#paginators-for-boto3-codecommit-module)
  - [DescribePullRequestEventsPaginator](#describepullrequesteventspaginator)
  - [GetCommentsForComparedCommitPaginator](#getcommentsforcomparedcommitpaginator)
  - [GetCommentsForPullRequestPaginator](#getcommentsforpullrequestpaginator)
  - [GetDifferencesPaginator](#getdifferencespaginator)
  - [ListBranchesPaginator](#listbranchespaginator)
  - [ListPullRequestsPaginator](#listpullrequestspaginator)
  - [ListRepositoriesPaginator](#listrepositoriespaginator)

## DescribePullRequestEventsPaginator

Type annotations for `boto3.client("codecommit").get_paginator("describe_pull_request_events")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import DescribePullRequestEventsPaginator

def get_describe_pull_request_events_paginator() -> DescribePullRequestEventsPaginator:
    return boto3.client("codecommit").get_paginator("describe_pull_request_events")
```

[Paginator.DescribePullRequestEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)

```python
class DescribePullRequestEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        pullRequestId: str,
        pullRequestEventType: PullRequestEventType = None,
        actorArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePullRequestEventsOutputTypeDef]:
        pass
```
## GetCommentsForComparedCommitPaginator

Type annotations for `boto3.client("codecommit").get_paginator("get_comments_for_compared_commit")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import GetCommentsForComparedCommitPaginator

def get_get_comments_for_compared_commit_paginator() -> GetCommentsForComparedCommitPaginator:
    return boto3.client("codecommit").get_paginator("get_comments_for_compared_commit")
```

[Paginator.GetCommentsForComparedCommit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)

```python
class GetCommentsForComparedCommitPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        afterCommitId: str,
        beforeCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCommentsForComparedCommitOutputTypeDef]:
        pass
```
## GetCommentsForPullRequestPaginator

Type annotations for `boto3.client("codecommit").get_paginator("get_comments_for_pull_request")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import GetCommentsForPullRequestPaginator

def get_get_comments_for_pull_request_paginator() -> GetCommentsForPullRequestPaginator:
    return boto3.client("codecommit").get_paginator("get_comments_for_pull_request")
```

[Paginator.GetCommentsForPullRequest documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)

```python
class GetCommentsForPullRequestPaginator(Boto3Paginator):
    def paginate(
        self,
        pullRequestId: str,
        repositoryName: str = None,
        beforeCommitId: str = None,
        afterCommitId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCommentsForPullRequestOutputTypeDef]:
        pass
```
## GetDifferencesPaginator

Type annotations for `boto3.client("codecommit").get_paginator("get_differences")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import GetDifferencesPaginator

def get_get_differences_paginator() -> GetDifferencesPaginator:
    return boto3.client("codecommit").get_paginator("get_differences")
```

[Paginator.GetDifferences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)

```python
class GetDifferencesPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        afterCommitSpecifier: str,
        beforeCommitSpecifier: str = None,
        beforePath: str = None,
        afterPath: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDifferencesOutputTypeDef]:
        pass
```
## ListBranchesPaginator

Type annotations for `boto3.client("codecommit").get_paginator("list_branches")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import ListBranchesPaginator

def get_list_branches_paginator() -> ListBranchesPaginator:
    return boto3.client("codecommit").get_paginator("list_branches")
```

[Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)

```python
class ListBranchesPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBranchesOutputTypeDef]:
        pass
```
## ListPullRequestsPaginator

Type annotations for `boto3.client("codecommit").get_paginator("list_pull_requests")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import ListPullRequestsPaginator

def get_list_pull_requests_paginator() -> ListPullRequestsPaginator:
    return boto3.client("codecommit").get_paginator("list_pull_requests")
```

[Paginator.ListPullRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)

```python
class ListPullRequestsPaginator(Boto3Paginator):
    def paginate(
        self,
        repositoryName: str,
        authorArn: str = None,
        pullRequestStatus: PullRequestStatusEnum = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPullRequestsOutputTypeDef]:
        pass
```
## ListRepositoriesPaginator

Type annotations for `boto3.client("codecommit").get_paginator("list_repositories")`.

Can be used directly:

```python
from mypy_boto3_codecommit.paginators import ListRepositoriesPaginator

def get_list_repositories_paginator() -> ListRepositoriesPaginator:
    return boto3.client("codecommit").get_paginator("list_repositories")
```

[Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)

```python
class ListRepositoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        sortBy: SortByEnum = None,
        order: OrderEnum = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesOutputTypeDef]:
        pass
```