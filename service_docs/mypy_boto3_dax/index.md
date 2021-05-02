# Type annotations for boto3 DAX module

> [Index](../index.md) > DAX

Auto-generated documentation for [DAX](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html#DAX)
type annotations stubs module [mypy_boto3_dax](https://pypi.org/project/mypy-boto3-dax/).

```bash
pip install mypy-boto3-dax
```

- [Type annotations for boto3 DAX module](#type-annotations-for-boto3-dax-module)
  - [DAXClient](#daxclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DAXClient

Type annotations for  `boto3.client("dax")` as [DAXClient](./client.md)

Can be used directly:

```python
from mypy_boto3_dax.client import DAXClient
```


DAXClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_cluster](./client.md#create-cluster)
- [create_parameter_group](./client.md#create-parameter-group)
- [create_subnet_group](./client.md#create-subnet-group)
- [decrease_replication_factor](./client.md#decrease-replication-factor)
- [delete_cluster](./client.md#delete-cluster)
- [delete_parameter_group](./client.md#delete-parameter-group)
- [delete_subnet_group](./client.md#delete-subnet-group)
- [describe_clusters](./client.md#describe-clusters)
- [describe_default_parameters](./client.md#describe-default-parameters)
- [describe_events](./client.md#describe-events)
- [describe_parameter_groups](./client.md#describe-parameter-groups)
- [describe_parameters](./client.md#describe-parameters)
- [describe_subnet_groups](./client.md#describe-subnet-groups)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [increase_replication_factor](./client.md#increase-replication-factor)
- [list_tags](./client.md#list-tags)
- [reboot_node](./client.md#reboot-node)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_cluster](./client.md#update-cluster)
- [update_parameter_group](./client.md#update-parameter-group)
- [update_subnet_group](./client.md#update-subnet-group)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ClusterAlreadyExistsFault](./client.md#clusteralreadyexistsfault)
- [ClusterNotFoundFault](./client.md#clusternotfoundfault)
- [ClusterQuotaForCustomerExceededFault](./client.md#clusterquotaforcustomerexceededfault)
- [InsufficientClusterCapacityFault](./client.md#insufficientclustercapacityfault)
- [InvalidARNFault](./client.md#invalidarnfault)
- [InvalidClusterStateFault](./client.md#invalidclusterstatefault)
- [InvalidParameterCombinationException](./client.md#invalidparametercombinationexception)
- [InvalidParameterGroupStateFault](./client.md#invalidparametergroupstatefault)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidSubnet](./client.md#invalidsubnet)
- [InvalidVPCNetworkStateFault](./client.md#invalidvpcnetworkstatefault)
- [NodeNotFoundFault](./client.md#nodenotfoundfault)
- [NodeQuotaForClusterExceededFault](./client.md#nodequotaforclusterexceededfault)
- [NodeQuotaForCustomerExceededFault](./client.md#nodequotaforcustomerexceededfault)
- [ParameterGroupAlreadyExistsFault](./client.md#parametergroupalreadyexistsfault)
- [ParameterGroupNotFoundFault](./client.md#parametergroupnotfoundfault)
- [ParameterGroupQuotaExceededFault](./client.md#parametergroupquotaexceededfault)
- [ServiceLinkedRoleNotFoundFault](./client.md#servicelinkedrolenotfoundfault)
- [SubnetGroupAlreadyExistsFault](./client.md#subnetgroupalreadyexistsfault)
- [SubnetGroupInUseFault](./client.md#subnetgroupinusefault)
- [SubnetGroupNotFoundFault](./client.md#subnetgroupnotfoundfault)
- [SubnetGroupQuotaExceededFault](./client.md#subnetgroupquotaexceededfault)
- [SubnetInUse](./client.md#subnetinuse)
- [SubnetQuotaExceededFault](./client.md#subnetquotaexceededfault)
- [TagNotFoundFault](./client.md#tagnotfoundfault)
- [TagQuotaPerResourceExceeded](./client.md#tagquotaperresourceexceeded)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("dax").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_dax.paginators import DescribeClustersPaginator, ...
```

- [DescribeClustersPaginator](./paginators.md#describeclusterspaginator)
- [DescribeDefaultParametersPaginator](./paginators.md#describedefaultparameterspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeParameterGroupsPaginator](./paginators.md#describeparametergroupspaginator)
- [DescribeParametersPaginator](./paginators.md#describeparameterspaginator)
- [DescribeSubnetGroupsPaginator](./paginators.md#describesubnetgroupspaginator)
- [ListTagsPaginator](./paginators.md#listtagspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dax.literals import ChangeType, ...
```

- [ChangeType](./literals.md#changetype)
- [DescribeClustersPaginatorName](./literals.md#describeclusterspaginatorname)
- [DescribeDefaultParametersPaginatorName](./literals.md#describedefaultparameterspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [DescribeParameterGroupsPaginatorName](./literals.md#describeparametergroupspaginatorname)
- [DescribeParametersPaginatorName](./literals.md#describeparameterspaginatorname)
- [DescribeSubnetGroupsPaginatorName](./literals.md#describesubnetgroupspaginatorname)
- [IsModifiable](./literals.md#ismodifiable)
- [ListTagsPaginatorName](./literals.md#listtagspaginatorname)
- [ParameterType](./literals.md#parametertype)
- [SSEStatus](./literals.md#ssestatus)
- [SourceType](./literals.md#sourcetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_dax.type_defs import ClusterTypeDef, ...
```

- [ClusterTypeDef](./type_defs.md#clustertypedef)
- [CreateClusterResponseTypeDef](./type_defs.md#createclusterresponsetypedef)
- [CreateParameterGroupResponseTypeDef](./type_defs.md#createparametergroupresponsetypedef)
- [CreateSubnetGroupResponseTypeDef](./type_defs.md#createsubnetgroupresponsetypedef)
- [DecreaseReplicationFactorResponseTypeDef](./type_defs.md#decreasereplicationfactorresponsetypedef)
- [DeleteClusterResponseTypeDef](./type_defs.md#deleteclusterresponsetypedef)
- [DeleteParameterGroupResponseTypeDef](./type_defs.md#deleteparametergroupresponsetypedef)
- [DeleteSubnetGroupResponseTypeDef](./type_defs.md#deletesubnetgroupresponsetypedef)
- [DescribeClustersResponseTypeDef](./type_defs.md#describeclustersresponsetypedef)
- [DescribeDefaultParametersResponseTypeDef](./type_defs.md#describedefaultparametersresponsetypedef)
- [DescribeEventsResponseTypeDef](./type_defs.md#describeeventsresponsetypedef)
- [DescribeParameterGroupsResponseTypeDef](./type_defs.md#describeparametergroupsresponsetypedef)
- [DescribeParametersResponseTypeDef](./type_defs.md#describeparametersresponsetypedef)
- [DescribeSubnetGroupsResponseTypeDef](./type_defs.md#describesubnetgroupsresponsetypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [IncreaseReplicationFactorResponseTypeDef](./type_defs.md#increasereplicationfactorresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [NodeTypeDef](./type_defs.md#nodetypedef)
- [NodeTypeSpecificValueTypeDef](./type_defs.md#nodetypespecificvaluetypedef)
- [NotificationConfigurationTypeDef](./type_defs.md#notificationconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterGroupStatusTypeDef](./type_defs.md#parametergroupstatustypedef)
- [ParameterGroupTypeDef](./type_defs.md#parametergrouptypedef)
- [ParameterNameValueTypeDef](./type_defs.md#parameternamevaluetypedef)
- [ParameterTypeDef](./type_defs.md#parametertypedef)
- [RebootNodeResponseTypeDef](./type_defs.md#rebootnoderesponsetypedef)
- [SSEDescriptionTypeDef](./type_defs.md#ssedescriptiontypedef)
- [SSESpecificationTypeDef](./type_defs.md#ssespecificationtypedef)
- [SecurityGroupMembershipTypeDef](./type_defs.md#securitygroupmembershiptypedef)
- [SubnetGroupTypeDef](./type_defs.md#subnetgrouptypedef)
- [SubnetTypeDef](./type_defs.md#subnettypedef)
- [TagResourceResponseTypeDef](./type_defs.md#tagresourceresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UntagResourceResponseTypeDef](./type_defs.md#untagresourceresponsetypedef)
- [UpdateClusterResponseTypeDef](./type_defs.md#updateclusterresponsetypedef)
- [UpdateParameterGroupResponseTypeDef](./type_defs.md#updateparametergroupresponsetypedef)
- [UpdateSubnetGroupResponseTypeDef](./type_defs.md#updatesubnetgroupresponsetypedef)
