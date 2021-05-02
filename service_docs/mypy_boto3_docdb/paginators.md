# Paginators for boto3 DocDB module

> [Index](../index.md) > [DocDB](./index.md) > Paginators

Auto-generated documentation for [DocDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB)
type annotations stubs module [mypy_boto3_docdb](https://pypi.org/project/mypy-boto3-docdb/).

- [Paginators for boto3 DocDB module](#paginators-for-boto3-docdb-module)
  - [DescribeCertificatesPaginator](#describecertificatespaginator)
  - [DescribeDBClusterParameterGroupsPaginator](#describedbclusterparametergroupspaginator)
  - [DescribeDBClusterParametersPaginator](#describedbclusterparameterspaginator)
  - [DescribeDBClusterSnapshotsPaginator](#describedbclustersnapshotspaginator)
  - [DescribeDBClustersPaginator](#describedbclusterspaginator)
  - [DescribeDBEngineVersionsPaginator](#describedbengineversionspaginator)
  - [DescribeDBInstancesPaginator](#describedbinstancespaginator)
  - [DescribeDBSubnetGroupsPaginator](#describedbsubnetgroupspaginator)
  - [DescribeEventSubscriptionsPaginator](#describeeventsubscriptionspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeOrderableDBInstanceOptionsPaginator](#describeorderabledbinstanceoptionspaginator)
  - [DescribePendingMaintenanceActionsPaginator](#describependingmaintenanceactionspaginator)

## DescribeCertificatesPaginator

Type annotations for `boto3.client("docdb").get_paginator("describe_certificates")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeCertificatesPaginator

def get_describe_certificates_paginator() -> DescribeCertificatesPaginator:
    return boto3.client("docdb").get_paginator("describe_certificates")
```

[Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeCertificates)

```python
class DescribeCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CertificateMessageTypeDef]:
        pass
```
## DescribeDBClusterParameterGroupsPaginator

Type annotations for `boto3.client("docdb").get_paginator("describe_db_cluster_parameter_groups")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBClusterParameterGroupsPaginator

def get_describe_db_cluster_parameter_groups_paginator() -> DescribeDBClusterParameterGroupsPaginator:
    return boto3.client("docdb").get_paginator("describe_db_cluster_parameter_groups")
```

[Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterParameterGroups)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_db_cluster_parameters")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBClusterParametersPaginator

def get_describe_db_cluster_parameters_paginator() -> DescribeDBClusterParametersPaginator:
    return boto3.client("docdb").get_paginator("describe_db_cluster_parameters")
```

[Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterParameters)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_db_cluster_snapshots")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBClusterSnapshotsPaginator

def get_describe_db_cluster_snapshots_paginator() -> DescribeDBClusterSnapshotsPaginator:
    return boto3.client("docdb").get_paginator("describe_db_cluster_snapshots")
```

[Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusterSnapshots)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_db_clusters")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBClustersPaginator

def get_describe_db_clusters_paginator() -> DescribeDBClustersPaginator:
    return boto3.client("docdb").get_paginator("describe_db_clusters")
```

[Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_db_engine_versions")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBEngineVersionsPaginator

def get_describe_db_engine_versions_paginator() -> DescribeDBEngineVersionsPaginator:
    return boto3.client("docdb").get_paginator("describe_db_engine_versions")
```

[Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_db_instances")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBInstancesPaginator

def get_describe_db_instances_paginator() -> DescribeDBInstancesPaginator:
    return boto3.client("docdb").get_paginator("describe_db_instances")
```

[Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances)

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
## DescribeDBSubnetGroupsPaginator

Type annotations for `boto3.client("docdb").get_paginator("describe_db_subnet_groups")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeDBSubnetGroupsPaginator

def get_describe_db_subnet_groups_paginator() -> DescribeDBSubnetGroupsPaginator:
    return boto3.client("docdb").get_paginator("describe_db_subnet_groups")
```

[Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups)

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
## DescribeEventSubscriptionsPaginator

Type annotations for `boto3.client("docdb").get_paginator("describe_event_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeEventSubscriptionsPaginator

def get_describe_event_subscriptions_paginator() -> DescribeEventSubscriptionsPaginator:
    return boto3.client("docdb").get_paginator("describe_event_subscriptions")
```

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeEventSubscriptions)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("docdb").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeEvents)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_orderable_db_instance_options")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribeOrderableDBInstanceOptionsPaginator

def get_describe_orderable_db_instance_options_paginator() -> DescribeOrderableDBInstanceOptionsPaginator:
    return boto3.client("docdb").get_paginator("describe_orderable_db_instance_options")
```

[Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)

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

Type annotations for `boto3.client("docdb").get_paginator("describe_pending_maintenance_actions")`.

Can be used directly:

```python
from mypy_boto3_docdb.paginators import DescribePendingMaintenanceActionsPaginator

def get_describe_pending_maintenance_actions_paginator() -> DescribePendingMaintenanceActionsPaginator:
    return boto3.client("docdb").get_paginator("describe_pending_maintenance_actions")
```

[Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Paginator.DescribePendingMaintenanceActions)

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