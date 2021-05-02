# Paginators for boto3 CodeGuruReviewer module

> [Index](../index.md) > [CodeGuruReviewer](./index.md) > Paginators

Auto-generated documentation for [CodeGuruReviewer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer)
type annotations stubs module [mypy_boto3_codeguru_reviewer](https://pypi.org/project/mypy-boto3-codeguru-reviewer/).

- [Paginators for boto3 CodeGuruReviewer module](#paginators-for-boto3-codegurureviewer-module)
  - [ListRepositoryAssociationsPaginator](#listrepositoryassociationspaginator)

## ListRepositoryAssociationsPaginator

Type annotations for `boto3.client("codeguru-reviewer").get_paginator("list_repository_associations")`.

Can be used directly:

```python
from mypy_boto3_codeguru_reviewer.paginators import ListRepositoryAssociationsPaginator

def get_list_repository_associations_paginator() -> ListRepositoryAssociationsPaginator:
    return boto3.client("codeguru-reviewer").get_paginator("list_repository_associations")
```

[Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)

```python
class ListRepositoryAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        ProviderTypes: List[ProviderType] = None,
        States: List[RepositoryAssociationState] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoryAssociationsResponseTypeDef]:
        pass
```