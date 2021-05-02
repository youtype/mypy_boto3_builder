# Paginators for boto3 ElasticBeanstalk module

> [Index](../index.md) > [ElasticBeanstalk](./index.md) > Paginators

Auto-generated documentation for [ElasticBeanstalk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk)
type annotations stubs module [mypy_boto3_elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/).

- [Paginators for boto3 ElasticBeanstalk module](#paginators-for-boto3-elasticbeanstalk-module)
  - [DescribeApplicationVersionsPaginator](#describeapplicationversionspaginator)
  - [DescribeEnvironmentManagedActionHistoryPaginator](#describeenvironmentmanagedactionhistorypaginator)
  - [DescribeEnvironmentsPaginator](#describeenvironmentspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [ListPlatformVersionsPaginator](#listplatformversionspaginator)

## DescribeApplicationVersionsPaginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator("describe_application_versions")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.paginators import DescribeApplicationVersionsPaginator

def get_describe_application_versions_paginator() -> DescribeApplicationVersionsPaginator:
    return boto3.client("elasticbeanstalk").get_paginator("describe_application_versions")
```

[Paginator.DescribeApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)

```python
class DescribeApplicationVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ApplicationVersionDescriptionsMessageTypeDef]:
        pass
```
## DescribeEnvironmentManagedActionHistoryPaginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator("describe_environment_managed_action_history")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.paginators import DescribeEnvironmentManagedActionHistoryPaginator

def get_describe_environment_managed_action_history_paginator() -> DescribeEnvironmentManagedActionHistoryPaginator:
    return boto3.client("elasticbeanstalk").get_paginator("describe_environment_managed_action_history")
```

[Paginator.DescribeEnvironmentManagedActionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)

```python
class DescribeEnvironmentManagedActionHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEnvironmentManagedActionHistoryResultTypeDef]:
        pass
```
## DescribeEnvironmentsPaginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator("describe_environments")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.paginators import DescribeEnvironmentsPaginator

def get_describe_environments_paginator() -> DescribeEnvironmentsPaginator:
    return boto3.client("elasticbeanstalk").get_paginator("describe_environments")
```

[Paginator.DescribeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)

```python
class DescribeEnvironmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EnvironmentDescriptionsMessageTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("elasticbeanstalk").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: EventSeverity = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventDescriptionsMessageTypeDef]:
        pass
```
## ListPlatformVersionsPaginator

Type annotations for `boto3.client("elasticbeanstalk").get_paginator("list_platform_versions")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.paginators import ListPlatformVersionsPaginator

def get_list_platform_versions_paginator() -> ListPlatformVersionsPaginator:
    return boto3.client("elasticbeanstalk").get_paginator("list_platform_versions")
```

[Paginator.ListPlatformVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)

```python
class ListPlatformVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[PlatformFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlatformVersionsResultTypeDef]:
        pass
```