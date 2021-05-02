# Paginators for boto3 CloudFormation module

> [Index](../index.md) > [CloudFormation](./index.md) > Paginators

Auto-generated documentation for [CloudFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
type annotations stubs module [mypy_boto3_cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/).

- [Paginators for boto3 CloudFormation module](#paginators-for-boto3-cloudformation-module)
  - [DescribeAccountLimitsPaginator](#describeaccountlimitspaginator)
  - [DescribeChangeSetPaginator](#describechangesetpaginator)
  - [DescribeStackEventsPaginator](#describestackeventspaginator)
  - [DescribeStacksPaginator](#describestackspaginator)
  - [ListChangeSetsPaginator](#listchangesetspaginator)
  - [ListExportsPaginator](#listexportspaginator)
  - [ListImportsPaginator](#listimportspaginator)
  - [ListStackInstancesPaginator](#liststackinstancespaginator)
  - [ListStackResourcesPaginator](#liststackresourcespaginator)
  - [ListStackSetOperationResultsPaginator](#liststacksetoperationresultspaginator)
  - [ListStackSetOperationsPaginator](#liststacksetoperationspaginator)
  - [ListStackSetsPaginator](#liststacksetspaginator)
  - [ListStacksPaginator](#liststackspaginator)

## DescribeAccountLimitsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("describe_account_limits")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import DescribeAccountLimitsPaginator

def get_describe_account_limits_paginator() -> DescribeAccountLimitsPaginator:
    return boto3.client("cloudformation").get_paginator("describe_account_limits")
```

[Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)

```python
class DescribeAccountLimitsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        pass
```
## DescribeChangeSetPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("describe_change_set")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import DescribeChangeSetPaginator

def get_describe_change_set_paginator() -> DescribeChangeSetPaginator:
    return boto3.client("cloudformation").get_paginator("describe_change_set")
```

[Paginator.DescribeChangeSet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)

```python
class DescribeChangeSetPaginator(Boto3Paginator):
    def paginate(
        self,
        ChangeSetName: str,
        StackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeChangeSetOutputTypeDef]:
        pass
```
## DescribeStackEventsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("describe_stack_events")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import DescribeStackEventsPaginator

def get_describe_stack_events_paginator() -> DescribeStackEventsPaginator:
    return boto3.client("cloudformation").get_paginator("describe_stack_events")
```

[Paginator.DescribeStackEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)

```python
class DescribeStackEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStackEventsOutputTypeDef]:
        pass
```
## DescribeStacksPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("describe_stacks")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import DescribeStacksPaginator

def get_describe_stacks_paginator() -> DescribeStacksPaginator:
    return boto3.client("cloudformation").get_paginator("describe_stacks")
```

[Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)

```python
class DescribeStacksPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStacksOutputTypeDef]:
        pass
```
## ListChangeSetsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_change_sets")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListChangeSetsPaginator

def get_list_change_sets_paginator() -> ListChangeSetsPaginator:
    return boto3.client("cloudformation").get_paginator("list_change_sets")
```

[Paginator.ListChangeSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)

```python
class ListChangeSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChangeSetsOutputTypeDef]:
        pass
```
## ListExportsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_exports")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListExportsPaginator

def get_list_exports_paginator() -> ListExportsPaginator:
    return boto3.client("cloudformation").get_paginator("list_exports")
```

[Paginator.ListExports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)

```python
class ListExportsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExportsOutputTypeDef]:
        pass
```
## ListImportsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_imports")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListImportsPaginator

def get_list_imports_paginator() -> ListImportsPaginator:
    return boto3.client("cloudformation").get_paginator("list_imports")
```

[Paginator.ListImports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)

```python
class ListImportsPaginator(Boto3Paginator):
    def paginate(
        self,
        ExportName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImportsOutputTypeDef]:
        pass
```
## ListStackInstancesPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_stack_instances")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListStackInstancesPaginator

def get_list_stack_instances_paginator() -> ListStackInstancesPaginator:
    return boto3.client("cloudformation").get_paginator("list_stack_instances")
```

[Paginator.ListStackInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)

```python
class ListStackInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        StackSetName: str,
        Filters: List[StackInstanceFilterTypeDef] = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        CallAs: CallAs = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackInstancesOutputTypeDef]:
        pass
```
## ListStackResourcesPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_stack_resources")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListStackResourcesPaginator

def get_list_stack_resources_paginator() -> ListStackResourcesPaginator:
    return boto3.client("cloudformation").get_paginator("list_stack_resources")
```

[Paginator.ListStackResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)

```python
class ListStackResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackResourcesOutputTypeDef]:
        pass
```
## ListStackSetOperationResultsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_stack_set_operation_results")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListStackSetOperationResultsPaginator

def get_list_stack_set_operation_results_paginator() -> ListStackSetOperationResultsPaginator:
    return boto3.client("cloudformation").get_paginator("list_stack_set_operation_results")
```

[Paginator.ListStackSetOperationResults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)

```python
class ListStackSetOperationResultsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackSetName: str,
        OperationId: str,
        CallAs: CallAs = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetOperationResultsOutputTypeDef]:
        pass
```
## ListStackSetOperationsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_stack_set_operations")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListStackSetOperationsPaginator

def get_list_stack_set_operations_paginator() -> ListStackSetOperationsPaginator:
    return boto3.client("cloudformation").get_paginator("list_stack_set_operations")
```

[Paginator.ListStackSetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)

```python
class ListStackSetOperationsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackSetName: str,
        CallAs: CallAs = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetOperationsOutputTypeDef]:
        pass
```
## ListStackSetsPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_stack_sets")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListStackSetsPaginator

def get_list_stack_sets_paginator() -> ListStackSetsPaginator:
    return boto3.client("cloudformation").get_paginator("list_stack_sets")
```

[Paginator.ListStackSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)

```python
class ListStackSetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Status: StackSetStatus = None,
        CallAs: CallAs = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetsOutputTypeDef]:
        pass
```
## ListStacksPaginator

Type annotations for `boto3.client("cloudformation").get_paginator("list_stacks")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import ListStacksPaginator

def get_list_stacks_paginator() -> ListStacksPaginator:
    return boto3.client("cloudformation").get_paginator("list_stacks")
```

[Paginator.ListStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)

```python
class ListStacksPaginator(Boto3Paginator):
    def paginate(
        self,
        StackStatusFilter: List[StackStatus] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStacksOutputTypeDef]:
        pass
```