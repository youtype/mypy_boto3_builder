# DAXClient for boto3 DAX module

> [Index](../index.md) > [DAX](./index.md) > DAXClient

Auto-generated documentation for [DAX](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX)
type annotations stubs module [mypy_boto3_dax](https://pypi.org/project/mypy-boto3-dax/).

- [DAXClient for boto3 DAX module](#daxclient-for-boto3-dax-module)
  - [DAXClient](#daxclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_cluster](#create_cluster)
    - [create_parameter_group](#create_parameter_group)
    - [create_subnet_group](#create_subnet_group)
    - [decrease_replication_factor](#decrease_replication_factor)
    - [delete_cluster](#delete_cluster)
    - [delete_parameter_group](#delete_parameter_group)
    - [delete_subnet_group](#delete_subnet_group)
    - [describe_clusters](#describe_clusters)
    - [describe_default_parameters](#describe_default_parameters)
    - [describe_events](#describe_events)
    - [describe_parameter_groups](#describe_parameter_groups)
    - [describe_parameters](#describe_parameters)
    - [describe_subnet_groups](#describe_subnet_groups)
    - [generate_presigned_url](#generate_presigned_url)
    - [increase_replication_factor](#increase_replication_factor)
    - [list_tags](#list_tags)
    - [reboot_node](#reboot_node)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_cluster](#update_cluster)
    - [update_parameter_group](#update_parameter_group)
    - [update_subnet_group](#update_subnet_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## DAXClient

Type annotations for `boto3.client("dax")`

Can be used directly:

```python
from mypy_boto3_dax.client import DAXClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_dax.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ClusterAlreadyExistsFault`
- `Exceptions.ClusterNotFoundFault`
- `Exceptions.ClusterQuotaForCustomerExceededFault`
- `Exceptions.InsufficientClusterCapacityFault`
- `Exceptions.InvalidARNFault`
- `Exceptions.InvalidClusterStateFault`
- `Exceptions.InvalidParameterCombinationException`
- `Exceptions.InvalidParameterGroupStateFault`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidSubnet`
- `Exceptions.InvalidVPCNetworkStateFault`
- `Exceptions.NodeNotFoundFault`
- `Exceptions.NodeQuotaForClusterExceededFault`
- `Exceptions.NodeQuotaForCustomerExceededFault`
- `Exceptions.ParameterGroupAlreadyExistsFault`
- `Exceptions.ParameterGroupNotFoundFault`
- `Exceptions.ParameterGroupQuotaExceededFault`
- `Exceptions.ServiceLinkedRoleNotFoundFault`
- `Exceptions.SubnetGroupAlreadyExistsFault`
- `Exceptions.SubnetGroupInUseFault`
- `Exceptions.SubnetGroupNotFoundFault`
- `Exceptions.SubnetGroupQuotaExceededFault`
- `Exceptions.SubnetInUse`
- `Exceptions.SubnetQuotaExceededFault`
- `Exceptions.TagNotFoundFault`
- `Exceptions.TagQuotaPerResourceExceeded`


## Methods


### can_paginate

Type annotations for `boto3.client("dax").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_cluster

Type annotations for `boto3.client("dax").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.create_cluster)

```python
def create_cluster(
    self,
    ClusterName: str,
    NodeType: str,
    ReplicationFactor: int,
    IamRoleArn: str,
    Description: str = None,
    AvailabilityZones: List[str] = None,
    SubnetGroupName: str = None,
    SecurityGroupIds: List[str] = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    ParameterGroupName: str = None,
    Tags: List["TagTypeDef"] = None,
    SSESpecification: SSESpecificationTypeDef = None
) -> CreateClusterResponseTypeDef:
    pass
```

### create_parameter_group

Type annotations for `boto3.client("dax").create_parameter_group` method.

[Client.create_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.create_parameter_group)

```python
def create_parameter_group(
    self,
    ParameterGroupName: str,
    Description: str = None
) -> CreateParameterGroupResponseTypeDef:
    pass
```

### create_subnet_group

Type annotations for `boto3.client("dax").create_subnet_group` method.

[Client.create_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.create_subnet_group)

```python
def create_subnet_group(
    self,
    SubnetGroupName: str,
    SubnetIds: List[str],
    Description: str = None
) -> CreateSubnetGroupResponseTypeDef:
    pass
```

### decrease_replication_factor

Type annotations for `boto3.client("dax").decrease_replication_factor` method.

[Client.decrease_replication_factor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.decrease_replication_factor)

```python
def decrease_replication_factor(
    self,
    ClusterName: str,
    NewReplicationFactor: int,
    AvailabilityZones: List[str] = None,
    NodeIdsToRemove: List[str] = None
) -> DecreaseReplicationFactorResponseTypeDef:
    pass
```

### delete_cluster

Type annotations for `boto3.client("dax").delete_cluster` method.

[Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.delete_cluster)

```python
def delete_cluster(
    self,
    ClusterName: str
) -> DeleteClusterResponseTypeDef:
    pass
```

### delete_parameter_group

Type annotations for `boto3.client("dax").delete_parameter_group` method.

[Client.delete_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.delete_parameter_group)

```python
def delete_parameter_group(
    self,
    ParameterGroupName: str
) -> DeleteParameterGroupResponseTypeDef:
    pass
```

### delete_subnet_group

Type annotations for `boto3.client("dax").delete_subnet_group` method.

[Client.delete_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.delete_subnet_group)

```python
def delete_subnet_group(
    self,
    SubnetGroupName: str
) -> DeleteSubnetGroupResponseTypeDef:
    pass
```

### describe_clusters

Type annotations for `boto3.client("dax").describe_clusters` method.

[Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.describe_clusters)

```python
def describe_clusters(
    self,
    ClusterNames: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeClustersResponseTypeDef:
    pass
```

### describe_default_parameters

Type annotations for `boto3.client("dax").describe_default_parameters` method.

[Client.describe_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.describe_default_parameters)

```python
def describe_default_parameters(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeDefaultParametersResponseTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("dax").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.describe_events)

```python
def describe_events(
    self,
    SourceName: str = None,
    SourceType: SourceType = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Duration: int = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeEventsResponseTypeDef:
    pass
```

### describe_parameter_groups

Type annotations for `boto3.client("dax").describe_parameter_groups` method.

[Client.describe_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.describe_parameter_groups)

```python
def describe_parameter_groups(
    self,
    ParameterGroupNames: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeParameterGroupsResponseTypeDef:
    pass
```

### describe_parameters

Type annotations for `boto3.client("dax").describe_parameters` method.

[Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.describe_parameters)

```python
def describe_parameters(
    self,
    ParameterGroupName: str,
    Source: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeParametersResponseTypeDef:
    pass
```

### describe_subnet_groups

Type annotations for `boto3.client("dax").describe_subnet_groups` method.

[Client.describe_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.describe_subnet_groups)

```python
def describe_subnet_groups(
    self,
    SubnetGroupNames: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeSubnetGroupsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("dax").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### increase_replication_factor

Type annotations for `boto3.client("dax").increase_replication_factor` method.

[Client.increase_replication_factor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.increase_replication_factor)

```python
def increase_replication_factor(
    self,
    ClusterName: str,
    NewReplicationFactor: int,
    AvailabilityZones: List[str] = None
) -> IncreaseReplicationFactorResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("dax").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.list_tags)

```python
def list_tags(
    self,
    ResourceName: str,
    NextToken: str = None
) -> ListTagsResponseTypeDef:
    pass
```

### reboot_node

Type annotations for `boto3.client("dax").reboot_node` method.

[Client.reboot_node documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.reboot_node)

```python
def reboot_node(
    self,
    ClusterName: str,
    NodeId: str
) -> RebootNodeResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("dax").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceName: str,
    Tags: List["TagTypeDef"]
) -> TagResourceResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("dax").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceName: str,
    TagKeys: List[str]
) -> UntagResourceResponseTypeDef:
    pass
```

### update_cluster

Type annotations for `boto3.client("dax").update_cluster` method.

[Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.update_cluster)

```python
def update_cluster(
    self,
    ClusterName: str,
    Description: str = None,
    PreferredMaintenanceWindow: str = None,
    NotificationTopicArn: str = None,
    NotificationTopicStatus: str = None,
    ParameterGroupName: str = None,
    SecurityGroupIds: List[str] = None
) -> UpdateClusterResponseTypeDef:
    pass
```

### update_parameter_group

Type annotations for `boto3.client("dax").update_parameter_group` method.

[Client.update_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.update_parameter_group)

```python
def update_parameter_group(
    self,
    ParameterGroupName: str,
    ParameterNameValues: List[ParameterNameValueTypeDef]
) -> UpdateParameterGroupResponseTypeDef:
    pass
```

### update_subnet_group

Type annotations for `boto3.client("dax").update_subnet_group` method.

[Client.update_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Client.update_subnet_group)

```python
def update_subnet_group(
    self,
    SubnetGroupName: str,
    Description: str = None,
    SubnetIds: List[str] = None
) -> UpdateSubnetGroupResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeClustersPaginatorName
) -> DescribeClustersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.DescribeDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDefaultParametersPaginatorName
) -> DescribeDefaultParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.DescribeParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeParameterGroupsPaginatorName
) -> DescribeParameterGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeParametersPaginatorName
) -> DescribeParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.DescribeSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSubnetGroupsPaginatorName
) -> DescribeSubnetGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("dax").get_paginator` method.

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX.Paginator.ListTags)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsPaginatorName
) -> ListTagsPaginator:
    pass
```