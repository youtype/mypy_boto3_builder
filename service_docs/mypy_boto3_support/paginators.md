# Paginators for boto3 Support module

> [Index](../index.md) > [Support](./index.md) > Paginators

Auto-generated documentation for [Support](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support)
type annotations stubs module [mypy_boto3_support](https://pypi.org/project/mypy-boto3-support/).

- [Paginators for boto3 Support module](#paginators-for-boto3-support-module)
  - [DescribeCasesPaginator](#describecasespaginator)
  - [DescribeCommunicationsPaginator](#describecommunicationspaginator)

## DescribeCasesPaginator

Type annotations for `boto3.client("support").get_paginator("describe_cases")`.

Can be used directly:

```python
from mypy_boto3_support.paginators import DescribeCasesPaginator

def get_describe_cases_paginator() -> DescribeCasesPaginator:
    return boto3.client("support").get_paginator("describe_cases")
```

[Paginator.DescribeCases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Paginator.DescribeCases)

```python
class DescribeCasesPaginator(Boto3Paginator):
    def paginate(
        self,
        caseIdList: List[str] = None,
        displayId: str = None,
        afterTime: str = None,
        beforeTime: str = None,
        includeResolvedCases: bool = None,
        language: str = None,
        includeCommunications: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCasesResponseTypeDef]:
        pass
```
## DescribeCommunicationsPaginator

Type annotations for `boto3.client("support").get_paginator("describe_communications")`.

Can be used directly:

```python
from mypy_boto3_support.paginators import DescribeCommunicationsPaginator

def get_describe_communications_paginator() -> DescribeCommunicationsPaginator:
    return boto3.client("support").get_paginator("describe_communications")
```

[Paginator.DescribeCommunications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html#Support.Paginator.DescribeCommunications)

```python
class DescribeCommunicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        caseId: str,
        beforeTime: str = None,
        afterTime: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCommunicationsResponseTypeDef]:
        pass
```