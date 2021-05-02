# Structures for boto3 DAX module

> [Index](../index.md) > [DAX](./index.md) > Structures

Auto-generated documentation for [DAX](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX)
type annotations stubs module [mypy_boto3_dax](https://pypi.org/project/mypy-boto3-dax/).

- [Structures for boto3 DAX module](#structures-for-boto3-dax-module)
  - [ClusterTypeDef](#clustertypedef)
  - [CreateClusterResponseTypeDef](#createclusterresponsetypedef)
  - [CreateParameterGroupResponseTypeDef](#createparametergroupresponsetypedef)
  - [CreateSubnetGroupResponseTypeDef](#createsubnetgroupresponsetypedef)
  - [DecreaseReplicationFactorResponseTypeDef](#decreasereplicationfactorresponsetypedef)
  - [DeleteClusterResponseTypeDef](#deleteclusterresponsetypedef)
  - [DeleteParameterGroupResponseTypeDef](#deleteparametergroupresponsetypedef)
  - [DeleteSubnetGroupResponseTypeDef](#deletesubnetgroupresponsetypedef)
  - [DescribeClustersResponseTypeDef](#describeclustersresponsetypedef)
  - [DescribeDefaultParametersResponseTypeDef](#describedefaultparametersresponsetypedef)
  - [DescribeEventsResponseTypeDef](#describeeventsresponsetypedef)
  - [DescribeParameterGroupsResponseTypeDef](#describeparametergroupsresponsetypedef)
  - [DescribeParametersResponseTypeDef](#describeparametersresponsetypedef)
  - [DescribeSubnetGroupsResponseTypeDef](#describesubnetgroupsresponsetypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [EventTypeDef](#eventtypedef)
  - [IncreaseReplicationFactorResponseTypeDef](#increasereplicationfactorresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [NodeTypeDef](#nodetypedef)
  - [NodeTypeSpecificValueTypeDef](#nodetypespecificvaluetypedef)
  - [NotificationConfigurationTypeDef](#notificationconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParameterGroupStatusTypeDef](#parametergroupstatustypedef)
  - [ParameterGroupTypeDef](#parametergrouptypedef)
  - [ParameterNameValueTypeDef](#parameternamevaluetypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [RebootNodeResponseTypeDef](#rebootnoderesponsetypedef)
  - [SSEDescriptionTypeDef](#ssedescriptiontypedef)
  - [SSESpecificationTypeDef](#ssespecificationtypedef)
  - [SecurityGroupMembershipTypeDef](#securitygroupmembershiptypedef)
  - [SubnetGroupTypeDef](#subnetgrouptypedef)
  - [SubnetTypeDef](#subnettypedef)
  - [TagResourceResponseTypeDef](#tagresourceresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UntagResourceResponseTypeDef](#untagresourceresponsetypedef)
  - [UpdateClusterResponseTypeDef](#updateclusterresponsetypedef)
  - [UpdateParameterGroupResponseTypeDef](#updateparametergroupresponsetypedef)
  - [UpdateSubnetGroupResponseTypeDef](#updatesubnetgroupresponsetypedef)

## ClusterTypeDef

```python
from mypy_boto3_dax.type_defs import ClusterTypeDef
```




Optional fields:
- `ClusterName`: `str`
- `Description`: `str`
- `ClusterArn`: `str`
- `TotalNodes`: `int`
- `ActiveNodes`: `int`
- `NodeType`: `str`
- `Status`: `str`
- `ClusterDiscoveryEndpoint`: `"EndpointTypeDef"`
- `NodeIdsToRemove`: `List[str]`
- `Nodes`: `List["NodeTypeDef"]`
- `PreferredMaintenanceWindow`: `str`
- `NotificationConfiguration`: `"NotificationConfigurationTypeDef"`
- `SubnetGroup`: `str`
- `SecurityGroups`: `List["SecurityGroupMembershipTypeDef"]`
- `IamRoleArn`: `str`
- `ParameterGroup`: `"ParameterGroupStatusTypeDef"`
- `SSEDescription`: `"SSEDescriptionTypeDef"`


## CreateClusterResponseTypeDef

```python
from mypy_boto3_dax.type_defs import CreateClusterResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## CreateParameterGroupResponseTypeDef

```python
from mypy_boto3_dax.type_defs import CreateParameterGroupResponseTypeDef
```




Optional fields:
- `ParameterGroup`: `"ParameterGroupTypeDef"`


## CreateSubnetGroupResponseTypeDef

```python
from mypy_boto3_dax.type_defs import CreateSubnetGroupResponseTypeDef
```




Optional fields:
- `SubnetGroup`: `"SubnetGroupTypeDef"`


## DecreaseReplicationFactorResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DecreaseReplicationFactorResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## DeleteClusterResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DeleteClusterResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## DeleteParameterGroupResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DeleteParameterGroupResponseTypeDef
```




Optional fields:
- `DeletionMessage`: `str`


## DeleteSubnetGroupResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DeleteSubnetGroupResponseTypeDef
```




Optional fields:
- `DeletionMessage`: `str`


## DescribeClustersResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DescribeClustersResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Clusters`: `List["ClusterTypeDef"]`


## DescribeDefaultParametersResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DescribeDefaultParametersResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Parameters`: `List["ParameterTypeDef"]`


## DescribeEventsResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DescribeEventsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Events`: `List["EventTypeDef"]`


## DescribeParameterGroupsResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DescribeParameterGroupsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ParameterGroups`: `List["ParameterGroupTypeDef"]`


## DescribeParametersResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DescribeParametersResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Parameters`: `List["ParameterTypeDef"]`


## DescribeSubnetGroupsResponseTypeDef

```python
from mypy_boto3_dax.type_defs import DescribeSubnetGroupsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `SubnetGroups`: `List["SubnetGroupTypeDef"]`


## EndpointTypeDef

```python
from mypy_boto3_dax.type_defs import EndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Port`: `int`


## EventTypeDef

```python
from mypy_boto3_dax.type_defs import EventTypeDef
```




Optional fields:
- `SourceName`: `str`
- `SourceType`: `SourceType`
- `Message`: `str`
- `Date`: `datetime`


## IncreaseReplicationFactorResponseTypeDef

```python
from mypy_boto3_dax.type_defs import IncreaseReplicationFactorResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ListTagsResponseTypeDef

```python
from mypy_boto3_dax.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## NodeTypeDef

```python
from mypy_boto3_dax.type_defs import NodeTypeDef
```




Optional fields:
- `NodeId`: `str`
- `Endpoint`: `"EndpointTypeDef"`
- `NodeCreateTime`: `datetime`
- `AvailabilityZone`: `str`
- `NodeStatus`: `str`
- `ParameterGroupStatus`: `str`


## NodeTypeSpecificValueTypeDef

```python
from mypy_boto3_dax.type_defs import NodeTypeSpecificValueTypeDef
```




Optional fields:
- `NodeType`: `str`
- `Value`: `str`


## NotificationConfigurationTypeDef

```python
from mypy_boto3_dax.type_defs import NotificationConfigurationTypeDef
```




Optional fields:
- `TopicArn`: `str`
- `TopicStatus`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_dax.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParameterGroupStatusTypeDef

```python
from mypy_boto3_dax.type_defs import ParameterGroupStatusTypeDef
```




Optional fields:
- `ParameterGroupName`: `str`
- `ParameterApplyStatus`: `str`
- `NodeIdsToReboot`: `List[str]`


## ParameterGroupTypeDef

```python
from mypy_boto3_dax.type_defs import ParameterGroupTypeDef
```




Optional fields:
- `ParameterGroupName`: `str`
- `Description`: `str`


## ParameterNameValueTypeDef

```python
from mypy_boto3_dax.type_defs import ParameterNameValueTypeDef
```




Optional fields:
- `ParameterName`: `str`
- `ParameterValue`: `str`


## ParameterTypeDef

```python
from mypy_boto3_dax.type_defs import ParameterTypeDef
```




Optional fields:
- `ParameterName`: `str`
- `ParameterType`: `ParameterType`
- `ParameterValue`: `str`
- `NodeTypeSpecificValues`: `List["NodeTypeSpecificValueTypeDef"]`
- `Description`: `str`
- `Source`: `str`
- `DataType`: `str`
- `AllowedValues`: `str`
- `IsModifiable`: `IsModifiable`
- `ChangeType`: `ChangeType`


## RebootNodeResponseTypeDef

```python
from mypy_boto3_dax.type_defs import RebootNodeResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## SSEDescriptionTypeDef

```python
from mypy_boto3_dax.type_defs import SSEDescriptionTypeDef
```




Optional fields:
- `Status`: `SSEStatus`


## SSESpecificationTypeDef

```python
from mypy_boto3_dax.type_defs import SSESpecificationTypeDef
```


Required fields:
- `Enabled`: `bool`




## SecurityGroupMembershipTypeDef

```python
from mypy_boto3_dax.type_defs import SecurityGroupMembershipTypeDef
```




Optional fields:
- `SecurityGroupIdentifier`: `str`
- `Status`: `str`


## SubnetGroupTypeDef

```python
from mypy_boto3_dax.type_defs import SubnetGroupTypeDef
```




Optional fields:
- `SubnetGroupName`: `str`
- `Description`: `str`
- `VpcId`: `str`
- `Subnets`: `List["SubnetTypeDef"]`


## SubnetTypeDef

```python
from mypy_boto3_dax.type_defs import SubnetTypeDef
```




Optional fields:
- `SubnetIdentifier`: `str`
- `SubnetAvailabilityZone`: `str`


## TagResourceResponseTypeDef

```python
from mypy_boto3_dax.type_defs import TagResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_dax.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## UntagResourceResponseTypeDef

```python
from mypy_boto3_dax.type_defs import UntagResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## UpdateClusterResponseTypeDef

```python
from mypy_boto3_dax.type_defs import UpdateClusterResponseTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## UpdateParameterGroupResponseTypeDef

```python
from mypy_boto3_dax.type_defs import UpdateParameterGroupResponseTypeDef
```




Optional fields:
- `ParameterGroup`: `"ParameterGroupTypeDef"`


## UpdateSubnetGroupResponseTypeDef

```python
from mypy_boto3_dax.type_defs import UpdateSubnetGroupResponseTypeDef
```




Optional fields:
- `SubnetGroup`: `"SubnetGroupTypeDef"`

