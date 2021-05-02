# Paginators for boto3 OpsWorks module

> [Index](../index.md) > [OpsWorks](./index.md) > Paginators

Auto-generated documentation for [OpsWorks](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks)
type annotations stubs module [mypy_boto3_opsworks](https://pypi.org/project/mypy-boto3-opsworks/).

- [Paginators for boto3 OpsWorks module](#paginators-for-boto3-opsworks-module)
  - [DescribeEcsClustersPaginator](#describeecsclusterspaginator)

## DescribeEcsClustersPaginator

Type annotations for `boto3.client("opsworks").get_paginator("describe_ecs_clusters")`.

Can be used directly:

```python
from mypy_boto3_opsworks.paginators import DescribeEcsClustersPaginator

def get_describe_ecs_clusters_paginator() -> DescribeEcsClustersPaginator:
    return boto3.client("opsworks").get_paginator("describe_ecs_clusters")
```

[Paginator.DescribeEcsClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)

```python
class DescribeEcsClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEcsClustersResultTypeDef]:
        pass
```