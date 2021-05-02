# Paginators for boto3 Redshift module

> [Index](../index.md) > [Redshift](./index.md) > Paginators

Auto-generated documentation for [Redshift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift)
type annotations stubs module [mypy_boto3_redshift](https://pypi.org/project/mypy-boto3-redshift/).

- [Paginators for boto3 Redshift module](#paginators-for-boto3-redshift-module)
  - [DescribeClusterDbRevisionsPaginator](#describeclusterdbrevisionspaginator)
  - [DescribeClusterParameterGroupsPaginator](#describeclusterparametergroupspaginator)
  - [DescribeClusterParametersPaginator](#describeclusterparameterspaginator)
  - [DescribeClusterSecurityGroupsPaginator](#describeclustersecuritygroupspaginator)
  - [DescribeClusterSnapshotsPaginator](#describeclustersnapshotspaginator)
  - [DescribeClusterSubnetGroupsPaginator](#describeclustersubnetgroupspaginator)
  - [DescribeClusterTracksPaginator](#describeclustertrackspaginator)
  - [DescribeClusterVersionsPaginator](#describeclusterversionspaginator)
  - [DescribeClustersPaginator](#describeclusterspaginator)
  - [DescribeDefaultClusterParametersPaginator](#describedefaultclusterparameterspaginator)
  - [DescribeEndpointAccessPaginator](#describeendpointaccesspaginator)
  - [DescribeEndpointAuthorizationPaginator](#describeendpointauthorizationpaginator)
  - [DescribeEventSubscriptionsPaginator](#describeeventsubscriptionspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeHsmClientCertificatesPaginator](#describehsmclientcertificatespaginator)
  - [DescribeHsmConfigurationsPaginator](#describehsmconfigurationspaginator)
  - [DescribeNodeConfigurationOptionsPaginator](#describenodeconfigurationoptionspaginator)
  - [DescribeOrderableClusterOptionsPaginator](#describeorderableclusteroptionspaginator)
  - [DescribeReservedNodeOfferingsPaginator](#describereservednodeofferingspaginator)
  - [DescribeReservedNodesPaginator](#describereservednodespaginator)
  - [DescribeScheduledActionsPaginator](#describescheduledactionspaginator)
  - [DescribeSnapshotCopyGrantsPaginator](#describesnapshotcopygrantspaginator)
  - [DescribeSnapshotSchedulesPaginator](#describesnapshotschedulespaginator)
  - [DescribeTableRestoreStatusPaginator](#describetablerestorestatuspaginator)
  - [DescribeTagsPaginator](#describetagspaginator)
  - [DescribeUsageLimitsPaginator](#describeusagelimitspaginator)
  - [GetReservedNodeExchangeOfferingsPaginator](#getreservednodeexchangeofferingspaginator)

## DescribeClusterDbRevisionsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_db_revisions")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterDbRevisionsPaginator

def get_describe_cluster_db_revisions_paginator() -> DescribeClusterDbRevisionsPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_db_revisions")
```

[Paginator.DescribeClusterDbRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)

```python
class DescribeClusterDbRevisionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterDbRevisionsMessageTypeDef]:
        pass
```
## DescribeClusterParameterGroupsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_parameter_groups")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterParameterGroupsPaginator

def get_describe_cluster_parameter_groups_paginator() -> DescribeClusterParameterGroupsPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_parameter_groups")
```

[Paginator.DescribeClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)

```python
class DescribeClusterParameterGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ParameterGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterParameterGroupsMessageTypeDef]:
        pass
```
## DescribeClusterParametersPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_parameters")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterParametersPaginator

def get_describe_cluster_parameters_paginator() -> DescribeClusterParametersPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_parameters")
```

[Paginator.DescribeClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)

```python
class DescribeClusterParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterParameterGroupDetailsTypeDef]:
        pass
```
## DescribeClusterSecurityGroupsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_security_groups")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterSecurityGroupsPaginator

def get_describe_cluster_security_groups_paginator() -> DescribeClusterSecurityGroupsPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_security_groups")
```

[Paginator.DescribeClusterSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)

```python
class DescribeClusterSecurityGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterSecurityGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterSecurityGroupMessageTypeDef]:
        pass
```
## DescribeClusterSnapshotsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_snapshots")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterSnapshotsPaginator

def get_describe_cluster_snapshots_paginator() -> DescribeClusterSnapshotsPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_snapshots")
```

[Paginator.DescribeClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)

```python
class DescribeClusterSnapshotsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SnapshotMessageTypeDef]:
        pass
```
## DescribeClusterSubnetGroupsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_subnet_groups")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterSubnetGroupsPaginator

def get_describe_cluster_subnet_groups_paginator() -> DescribeClusterSubnetGroupsPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_subnet_groups")
```

[Paginator.DescribeClusterSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)

```python
class DescribeClusterSubnetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterSubnetGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterSubnetGroupMessageTypeDef]:
        pass
```
## DescribeClusterTracksPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_tracks")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterTracksPaginator

def get_describe_cluster_tracks_paginator() -> DescribeClusterTracksPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_tracks")
```

[Paginator.DescribeClusterTracks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)

```python
class DescribeClusterTracksPaginator(Boto3Paginator):
    def paginate(
        self,
        MaintenanceTrackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TrackListMessageTypeDef]:
        pass
```
## DescribeClusterVersionsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_cluster_versions")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClusterVersionsPaginator

def get_describe_cluster_versions_paginator() -> DescribeClusterVersionsPaginator:
    return boto3.client("redshift").get_paginator("describe_cluster_versions")
```

[Paginator.DescribeClusterVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)

```python
class DescribeClusterVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterVersionsMessageTypeDef]:
        pass
```
## DescribeClustersPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_clusters")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeClustersPaginator

def get_describe_clusters_paginator() -> DescribeClustersPaginator:
    return boto3.client("redshift").get_paginator("describe_clusters")
```

[Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)

```python
class DescribeClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClustersMessageTypeDef]:
        pass
```
## DescribeDefaultClusterParametersPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_default_cluster_parameters")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeDefaultClusterParametersPaginator

def get_describe_default_cluster_parameters_paginator() -> DescribeDefaultClusterParametersPaginator:
    return boto3.client("redshift").get_paginator("describe_default_cluster_parameters")
```

[Paginator.DescribeDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)

```python
class DescribeDefaultClusterParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        ParameterGroupFamily: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDefaultClusterParametersResultTypeDef]:
        pass
```
## DescribeEndpointAccessPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_endpoint_access")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeEndpointAccessPaginator

def get_describe_endpoint_access_paginator() -> DescribeEndpointAccessPaginator:
    return boto3.client("redshift").get_paginator("describe_endpoint_access")
```

[Paginator.DescribeEndpointAccess documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAccess)

```python
class DescribeEndpointAccessPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        ResourceOwner: str = None,
        EndpointName: str = None,
        VpcId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EndpointAccessListTypeDef]:
        pass
```
## DescribeEndpointAuthorizationPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_endpoint_authorization")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeEndpointAuthorizationPaginator

def get_describe_endpoint_authorization_paginator() -> DescribeEndpointAuthorizationPaginator:
    return boto3.client("redshift").get_paginator("describe_endpoint_authorization")
```

[Paginator.DescribeEndpointAuthorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAuthorization)

```python
class DescribeEndpointAuthorizationPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        Account: str = None,
        Grantee: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EndpointAuthorizationListTypeDef]:
        pass
```
## DescribeEventSubscriptionsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_event_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeEventSubscriptionsPaginator

def get_describe_event_subscriptions_paginator() -> DescribeEventSubscriptionsPaginator:
    return boto3.client("redshift").get_paginator("describe_event_subscriptions")
```

[Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)

```python
class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        SubscriptionName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventSubscriptionsMessageTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("redshift").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: SourceType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventsMessageTypeDef]:
        pass
```
## DescribeHsmClientCertificatesPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_hsm_client_certificates")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeHsmClientCertificatesPaginator

def get_describe_hsm_client_certificates_paginator() -> DescribeHsmClientCertificatesPaginator:
    return boto3.client("redshift").get_paginator("describe_hsm_client_certificates")
```

[Paginator.DescribeHsmClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)

```python
class DescribeHsmClientCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        HsmClientCertificateIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HsmClientCertificateMessageTypeDef]:
        pass
```
## DescribeHsmConfigurationsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_hsm_configurations")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeHsmConfigurationsPaginator

def get_describe_hsm_configurations_paginator() -> DescribeHsmConfigurationsPaginator:
    return boto3.client("redshift").get_paginator("describe_hsm_configurations")
```

[Paginator.DescribeHsmConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)

```python
class DescribeHsmConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        HsmConfigurationIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HsmConfigurationMessageTypeDef]:
        pass
```
## DescribeNodeConfigurationOptionsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_node_configuration_options")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeNodeConfigurationOptionsPaginator

def get_describe_node_configuration_options_paginator() -> DescribeNodeConfigurationOptionsPaginator:
    return boto3.client("redshift").get_paginator("describe_node_configuration_options")
```

[Paginator.DescribeNodeConfigurationOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)

```python
class DescribeNodeConfigurationOptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ActionType: ActionType,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[NodeConfigurationOptionsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[NodeConfigurationOptionsMessageTypeDef]:
        pass
```
## DescribeOrderableClusterOptionsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_orderable_cluster_options")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeOrderableClusterOptionsPaginator

def get_describe_orderable_cluster_options_paginator() -> DescribeOrderableClusterOptionsPaginator:
    return boto3.client("redshift").get_paginator("describe_orderable_cluster_options")
```

[Paginator.DescribeOrderableClusterOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)

```python
class DescribeOrderableClusterOptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[OrderableClusterOptionsMessageTypeDef]:
        pass
```
## DescribeReservedNodeOfferingsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_reserved_node_offerings")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeReservedNodeOfferingsPaginator

def get_describe_reserved_node_offerings_paginator() -> DescribeReservedNodeOfferingsPaginator:
    return boto3.client("redshift").get_paginator("describe_reserved_node_offerings")
```

[Paginator.DescribeReservedNodeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)

```python
class DescribeReservedNodeOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedNodeOfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedNodeOfferingsMessageTypeDef]:
        pass
```
## DescribeReservedNodesPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_reserved_nodes")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeReservedNodesPaginator

def get_describe_reserved_nodes_paginator() -> DescribeReservedNodesPaginator:
    return boto3.client("redshift").get_paginator("describe_reserved_nodes")
```

[Paginator.DescribeReservedNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)

```python
class DescribeReservedNodesPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedNodeId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedNodesMessageTypeDef]:
        pass
```
## DescribeScheduledActionsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_scheduled_actions")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeScheduledActionsPaginator

def get_describe_scheduled_actions_paginator() -> DescribeScheduledActionsPaginator:
    return boto3.client("redshift").get_paginator("describe_scheduled_actions")
```

[Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)

```python
class DescribeScheduledActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ScheduledActionName: str = None,
        TargetActionType: ScheduledActionTypeValues = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Active: bool = None,
        Filters: List[ScheduledActionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ScheduledActionsMessageTypeDef]:
        pass
```
## DescribeSnapshotCopyGrantsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_snapshot_copy_grants")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeSnapshotCopyGrantsPaginator

def get_describe_snapshot_copy_grants_paginator() -> DescribeSnapshotCopyGrantsPaginator:
    return boto3.client("redshift").get_paginator("describe_snapshot_copy_grants")
```

[Paginator.DescribeSnapshotCopyGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)

```python
class DescribeSnapshotCopyGrantsPaginator(Boto3Paginator):
    def paginate(
        self,
        SnapshotCopyGrantName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SnapshotCopyGrantMessageTypeDef]:
        pass
```
## DescribeSnapshotSchedulesPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_snapshot_schedules")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeSnapshotSchedulesPaginator

def get_describe_snapshot_schedules_paginator() -> DescribeSnapshotSchedulesPaginator:
    return boto3.client("redshift").get_paginator("describe_snapshot_schedules")
```

[Paginator.DescribeSnapshotSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)

```python
class DescribeSnapshotSchedulesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotSchedulesOutputMessageTypeDef]:
        pass
```
## DescribeTableRestoreStatusPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_table_restore_status")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeTableRestoreStatusPaginator

def get_describe_table_restore_status_paginator() -> DescribeTableRestoreStatusPaginator:
    return boto3.client("redshift").get_paginator("describe_table_restore_status")
```

[Paginator.DescribeTableRestoreStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)

```python
class DescribeTableRestoreStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TableRestoreStatusMessageTypeDef]:
        pass
```
## DescribeTagsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_tags")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeTagsPaginator

def get_describe_tags_paginator() -> DescribeTagsPaginator:
    return boto3.client("redshift").get_paginator("describe_tags")
```

[Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeTags)

```python
class DescribeTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TaggedResourceListMessageTypeDef]:
        pass
```
## DescribeUsageLimitsPaginator

Type annotations for `boto3.client("redshift").get_paginator("describe_usage_limits")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import DescribeUsageLimitsPaginator

def get_describe_usage_limits_paginator() -> DescribeUsageLimitsPaginator:
    return boto3.client("redshift").get_paginator("describe_usage_limits")
```

[Paginator.DescribeUsageLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)

```python
class DescribeUsageLimitsPaginator(Boto3Paginator):
    def paginate(
        self,
        UsageLimitId: str = None,
        ClusterIdentifier: str = None,
        FeatureType: UsageLimitFeatureType = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UsageLimitListTypeDef]:
        pass
```
## GetReservedNodeExchangeOfferingsPaginator

Type annotations for `boto3.client("redshift").get_paginator("get_reserved_node_exchange_offerings")`.

Can be used directly:

```python
from mypy_boto3_redshift.paginators import GetReservedNodeExchangeOfferingsPaginator

def get_get_reserved_node_exchange_offerings_paginator() -> GetReservedNodeExchangeOfferingsPaginator:
    return boto3.client("redshift").get_paginator("get_reserved_node_exchange_offerings")
```

[Paginator.GetReservedNodeExchangeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)

```python
class GetReservedNodeExchangeOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedNodeId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReservedNodeExchangeOfferingsOutputMessageTypeDef]:
        pass
```