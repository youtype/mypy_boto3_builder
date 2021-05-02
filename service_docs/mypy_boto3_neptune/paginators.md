# Paginators for boto3 Neptune module

> [Index](../index.md) > [Neptune](./index.md) > Paginators

Auto-generated documentation for [Neptune](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune)
type annotations stubs module [mypy_boto3_neptune](https://pypi.org/project/mypy-boto3-neptune/).

- [Paginators for boto3 Neptune module](#paginators-for-boto3-neptune-module)
  - [DescribeDBClusterEndpointsPaginator](#describedbclusterendpointspaginator)
  - [DescribeDBClusterParameterGroupsPaginator](#describedbclusterparametergroupspaginator)
  - [DescribeDBClusterParametersPaginator](#describedbclusterparameterspaginator)
  - [DescribeDBClusterSnapshotsPaginator](#describedbclustersnapshotspaginator)
  - [DescribeDBClustersPaginator](#describedbclusterspaginator)
  - [DescribeDBEngineVersionsPaginator](#describedbengineversionspaginator)
  - [DescribeDBInstancesPaginator](#describedbinstancespaginator)
  - [DescribeDBParameterGroupsPaginator](#describedbparametergroupspaginator)
  - [DescribeDBParametersPaginator](#describedbparameterspaginator)
  - [DescribeDBSubnetGroupsPaginator](#describedbsubnetgroupspaginator)
  - [DescribeEngineDefaultParametersPaginator](#describeenginedefaultparameterspaginator)
  - [DescribeEventSubscriptionsPaginator](#describeeventsubscriptionspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeOrderableDBInstanceOptionsPaginator](#describeorderabledbinstanceoptionspaginator)
  - [DescribePendingMaintenanceActionsPaginator](#describependingmaintenanceactionspaginator)

## DescribeDBClusterEndpointsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_cluster_endpoints")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBClusterEndpointsPaginator

def get_describe_db_cluster_endpoints_paginator() -> DescribeDBClusterEndpointsPaginator:
    return boto3.client("neptune").get_paginator("describe_db_cluster_endpoints")
```

[Paginator.DescribeDBClusterEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterEndpoints)

```python
class DescribeDBClusterEndpointsPaginator(Boto3Paginator):
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterEndpointMessageTypeDef]:
        pass
```
## DescribeDBClusterParameterGroupsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_cluster_parameter_groups")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBClusterParameterGroupsPaginator

def get_describe_db_cluster_parameter_groups_paginator() -> DescribeDBClusterParameterGroupsPaginator:
    return boto3.client("neptune").get_paginator("describe_db_cluster_parameter_groups")
```

[Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups)

```python
class DescribeDBClusterParameterGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterParameterGroupsMessageTypeDef]:
        pass
```
## DescribeDBClusterParametersPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_cluster_parameters")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBClusterParametersPaginator

def get_describe_db_cluster_parameters_paginator() -> DescribeDBClusterParametersPaginator:
    return boto3.client("neptune").get_paginator("describe_db_cluster_parameters")
```

[Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters)

```python
class DescribeDBClusterParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterParameterGroupDetailsTypeDef]:
        pass
```
## DescribeDBClusterSnapshotsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_cluster_snapshots")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBClusterSnapshotsPaginator

def get_describe_db_cluster_snapshots_paginator() -> DescribeDBClusterSnapshotsPaginator:
    return boto3.client("neptune").get_paginator("describe_db_cluster_snapshots")
```

[Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots)

```python
class DescribeDBClusterSnapshotsPaginator(Boto3Paginator):
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterSnapshotMessageTypeDef]:
        pass
```
## DescribeDBClustersPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_clusters")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBClustersPaginator

def get_describe_db_clusters_paginator() -> DescribeDBClustersPaginator:
    return boto3.client("neptune").get_paginator("describe_db_clusters")
```

[Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters)

```python
class DescribeDBClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterMessageTypeDef]:
        pass
```
## DescribeDBEngineVersionsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_engine_versions")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBEngineVersionsPaginator

def get_describe_db_engine_versions_paginator() -> DescribeDBEngineVersionsPaginator:
    return boto3.client("neptune").get_paginator("describe_db_engine_versions")
```

[Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions)

```python
class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBEngineVersionMessageTypeDef]:
        pass
```
## DescribeDBInstancesPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_instances")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBInstancesPaginator

def get_describe_db_instances_paginator() -> DescribeDBInstancesPaginator:
    return boto3.client("neptune").get_paginator("describe_db_instances")
```

[Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances)

```python
class DescribeDBInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBInstanceMessageTypeDef]:
        pass
```
## DescribeDBParameterGroupsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_parameter_groups")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBParameterGroupsPaginator

def get_describe_db_parameter_groups_paginator() -> DescribeDBParameterGroupsPaginator:
    return boto3.client("neptune").get_paginator("describe_db_parameter_groups")
```

[Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups)

```python
class DescribeDBParameterGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBParameterGroupsMessageTypeDef]:
        pass
```
## DescribeDBParametersPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_parameters")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBParametersPaginator

def get_describe_db_parameters_paginator() -> DescribeDBParametersPaginator:
    return boto3.client("neptune").get_paginator("describe_db_parameters")
```

[Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters)

```python
class DescribeDBParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBParameterGroupDetailsTypeDef]:
        pass
```
## DescribeDBSubnetGroupsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_db_subnet_groups")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeDBSubnetGroupsPaginator

def get_describe_db_subnet_groups_paginator() -> DescribeDBSubnetGroupsPaginator:
    return boto3.client("neptune").get_paginator("describe_db_subnet_groups")
```

[Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups)

```python
class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBSubnetGroupMessageTypeDef]:
        pass
```
## DescribeEngineDefaultParametersPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_engine_default_parameters")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeEngineDefaultParametersPaginator

def get_describe_engine_default_parameters_paginator() -> DescribeEngineDefaultParametersPaginator:
    return boto3.client("neptune").get_paginator("describe_engine_default_parameters")
```

[Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters)

```python
class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEngineDefaultParametersResultTypeDef]:
        pass
```
## DescribeEventSubscriptionsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_event_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeEventSubscriptionsPaginator

def get_describe_event_subscriptions_paginator() -> DescribeEventSubscriptionsPaginator:
    return boto3.client("neptune").get_paginator("describe_event_subscriptions")
```

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions)

```python
class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventSubscriptionsMessageTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("neptune").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: SourceType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventsMessageTypeDef]:
        pass
```
## DescribeOrderableDBInstanceOptionsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_orderable_db_instance_options")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribeOrderableDBInstanceOptionsPaginator

def get_describe_orderable_db_instance_options_paginator() -> DescribeOrderableDBInstanceOptionsPaginator:
    return boto3.client("neptune").get_paginator("describe_orderable_db_instance_options")
```

[Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)

```python
class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[OrderableDBInstanceOptionsMessageTypeDef]:
        pass
```
## DescribePendingMaintenanceActionsPaginator

Type annotations for `boto3.client("neptune").get_paginator("describe_pending_maintenance_actions")`.

Can be used directly:

```python
from mypy_boto3_neptune.paginators import DescribePendingMaintenanceActionsPaginator

def get_describe_pending_maintenance_actions_paginator() -> DescribePendingMaintenanceActionsPaginator:
    return boto3.client("neptune").get_paginator("describe_pending_maintenance_actions")
```

[Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions)

```python
class DescribePendingMaintenanceActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[PendingMaintenanceActionsMessageTypeDef]:
        pass
```