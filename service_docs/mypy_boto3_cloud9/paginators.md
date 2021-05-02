# Paginators for boto3 Cloud9 module

> [Index](../index.md) > [Cloud9](./index.md) > Paginators

Auto-generated documentation for [Cloud9](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9)
type annotations stubs module [mypy_boto3_cloud9](https://pypi.org/project/mypy-boto3-cloud9/).

- [Paginators for boto3 Cloud9 module](#paginators-for-boto3-cloud9-module)
  - [DescribeEnvironmentMembershipsPaginator](#describeenvironmentmembershipspaginator)
  - [ListEnvironmentsPaginator](#listenvironmentspaginator)

## DescribeEnvironmentMembershipsPaginator

Type annotations for `boto3.client("cloud9").get_paginator("describe_environment_memberships")`.

Can be used directly:

```python
from mypy_boto3_cloud9.paginators import DescribeEnvironmentMembershipsPaginator

def get_describe_environment_memberships_paginator() -> DescribeEnvironmentMembershipsPaginator:
    return boto3.client("cloud9").get_paginator("describe_environment_memberships")
```

[Paginator.DescribeEnvironmentMemberships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)

```python
class DescribeEnvironmentMembershipsPaginator(Boto3Paginator):
    def paginate(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Permissions] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEnvironmentMembershipsResultTypeDef]:
        pass
```
## ListEnvironmentsPaginator

Type annotations for `boto3.client("cloud9").get_paginator("list_environments")`.

Can be used directly:

```python
from mypy_boto3_cloud9.paginators import ListEnvironmentsPaginator

def get_list_environments_paginator() -> ListEnvironmentsPaginator:
    return boto3.client("cloud9").get_paginator("list_environments")
```

[Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)

```python
class ListEnvironmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsResultTypeDef]:
        pass
```