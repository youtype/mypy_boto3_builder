# Paginators for boto3 DatabaseMigrationService module

> [Index](../index.md) > [DatabaseMigrationService](./index.md) > Paginators

Auto-generated documentation for [DatabaseMigrationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService)
type annotations stubs module [mypy_boto3_dms](https://pypi.org/project/mypy-boto3-dms/).

- [Paginators for boto3 DatabaseMigrationService module](#paginators-for-boto3-databasemigrationservice-module)
  - [DescribeCertificatesPaginator](#describecertificatespaginator)
  - [DescribeConnectionsPaginator](#describeconnectionspaginator)
  - [DescribeEndpointTypesPaginator](#describeendpointtypespaginator)
  - [DescribeEndpointsPaginator](#describeendpointspaginator)
  - [DescribeEventSubscriptionsPaginator](#describeeventsubscriptionspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeOrderableReplicationInstancesPaginator](#describeorderablereplicationinstancespaginator)
  - [DescribeReplicationInstancesPaginator](#describereplicationinstancespaginator)
  - [DescribeReplicationSubnetGroupsPaginator](#describereplicationsubnetgroupspaginator)
  - [DescribeReplicationTaskAssessmentResultsPaginator](#describereplicationtaskassessmentresultspaginator)
  - [DescribeReplicationTasksPaginator](#describereplicationtaskspaginator)
  - [DescribeSchemasPaginator](#describeschemaspaginator)
  - [DescribeTableStatisticsPaginator](#describetablestatisticspaginator)

## DescribeCertificatesPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_certificates")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeCertificatesPaginator

def get_describe_certificates_paginator() -> DescribeCertificatesPaginator:
    return boto3.client("dms").get_paginator("describe_certificates")
```

[Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)

```python
class DescribeCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCertificatesResponseTypeDef]:
        pass
```
## DescribeConnectionsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_connections")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeConnectionsPaginator

def get_describe_connections_paginator() -> DescribeConnectionsPaginator:
    return boto3.client("dms").get_paginator("describe_connections")
```

[Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)

```python
class DescribeConnectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConnectionsResponseTypeDef]:
        pass
```
## DescribeEndpointTypesPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_endpoint_types")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeEndpointTypesPaginator

def get_describe_endpoint_types_paginator() -> DescribeEndpointTypesPaginator:
    return boto3.client("dms").get_paginator("describe_endpoint_types")
```

[Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)

```python
class DescribeEndpointTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointTypesResponseTypeDef]:
        pass
```
## DescribeEndpointsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_endpoints")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeEndpointsPaginator

def get_describe_endpoints_paginator() -> DescribeEndpointsPaginator:
    return boto3.client("dms").get_paginator("describe_endpoints")
```

[Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)

```python
class DescribeEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointsResponseTypeDef]:
        pass
```
## DescribeEventSubscriptionsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_event_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeEventSubscriptionsPaginator

def get_describe_event_subscriptions_paginator() -> DescribeEventSubscriptionsPaginator:
    return boto3.client("dms").get_paginator("describe_event_subscriptions")
```

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)

```python
class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEventSubscriptionsResponseTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("dms").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal['replication-instance'] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        pass
```
## DescribeOrderableReplicationInstancesPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_orderable_replication_instances")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeOrderableReplicationInstancesPaginator

def get_describe_orderable_replication_instances_paginator() -> DescribeOrderableReplicationInstancesPaginator:
    return boto3.client("dms").get_paginator("describe_orderable_replication_instances")
```

[Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)

```python
class DescribeOrderableReplicationInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrderableReplicationInstancesResponseTypeDef]:
        pass
```
## DescribeReplicationInstancesPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_replication_instances")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeReplicationInstancesPaginator

def get_describe_replication_instances_paginator() -> DescribeReplicationInstancesPaginator:
    return boto3.client("dms").get_paginator("describe_replication_instances")
```

[Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)

```python
class DescribeReplicationInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationInstancesResponseTypeDef]:
        pass
```
## DescribeReplicationSubnetGroupsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_replication_subnet_groups")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeReplicationSubnetGroupsPaginator

def get_describe_replication_subnet_groups_paginator() -> DescribeReplicationSubnetGroupsPaginator:
    return boto3.client("dms").get_paginator("describe_replication_subnet_groups")
```

[Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)

```python
class DescribeReplicationSubnetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationSubnetGroupsResponseTypeDef]:
        pass
```
## DescribeReplicationTaskAssessmentResultsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_replication_task_assessment_results")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeReplicationTaskAssessmentResultsPaginator

def get_describe_replication_task_assessment_results_paginator() -> DescribeReplicationTaskAssessmentResultsPaginator:
    return boto3.client("dms").get_paginator("describe_replication_task_assessment_results")
```

[Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)

```python
class DescribeReplicationTaskAssessmentResultsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReplicationTaskArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationTaskAssessmentResultsResponseTypeDef]:
        pass
```
## DescribeReplicationTasksPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_replication_tasks")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeReplicationTasksPaginator

def get_describe_replication_tasks_paginator() -> DescribeReplicationTasksPaginator:
    return boto3.client("dms").get_paginator("describe_replication_tasks")
```

[Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)

```python
class DescribeReplicationTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        WithoutSettings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationTasksResponseTypeDef]:
        pass
```
## DescribeSchemasPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_schemas")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeSchemasPaginator

def get_describe_schemas_paginator() -> DescribeSchemasPaginator:
    return boto3.client("dms").get_paginator("describe_schemas")
```

[Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)

```python
class DescribeSchemasPaginator(Boto3Paginator):
    def paginate(
        self,
        EndpointArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSchemasResponseTypeDef]:
        pass
```
## DescribeTableStatisticsPaginator

Type annotations for `boto3.client("dms").get_paginator("describe_table_statistics")`.

Can be used directly:

```python
from mypy_boto3_dms.paginators import DescribeTableStatisticsPaginator

def get_describe_table_statistics_paginator() -> DescribeTableStatisticsPaginator:
    return boto3.client("dms").get_paginator("describe_table_statistics")
```

[Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)

```python
class DescribeTableStatisticsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTableStatisticsResponseTypeDef]:
        pass
```