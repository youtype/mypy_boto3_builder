# EKSClient for boto3 EKS module

> [Index](../index.md) > [EKS](./index.md) > EKSClient

Auto-generated documentation for [EKS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS)
type annotations stubs module [mypy_boto3_eks](https://pypi.org/project/mypy-boto3-eks/).

- [EKSClient for boto3 EKS module](#eksclient-for-boto3-eks-module)
  - [EKSClient](#eksclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_encryption_config](#associate_encryption_config)
    - [associate_identity_provider_config](#associate_identity_provider_config)
    - [can_paginate](#can_paginate)
    - [create_addon](#create_addon)
    - [create_cluster](#create_cluster)
    - [create_fargate_profile](#create_fargate_profile)
    - [create_nodegroup](#create_nodegroup)
    - [delete_addon](#delete_addon)
    - [delete_cluster](#delete_cluster)
    - [delete_fargate_profile](#delete_fargate_profile)
    - [delete_nodegroup](#delete_nodegroup)
    - [describe_addon](#describe_addon)
    - [describe_addon_versions](#describe_addon_versions)
    - [describe_cluster](#describe_cluster)
    - [describe_fargate_profile](#describe_fargate_profile)
    - [describe_identity_provider_config](#describe_identity_provider_config)
    - [describe_nodegroup](#describe_nodegroup)
    - [describe_update](#describe_update)
    - [disassociate_identity_provider_config](#disassociate_identity_provider_config)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_addons](#list_addons)
    - [list_clusters](#list_clusters)
    - [list_fargate_profiles](#list_fargate_profiles)
    - [list_identity_provider_configs](#list_identity_provider_configs)
    - [list_nodegroups](#list_nodegroups)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_updates](#list_updates)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_addon](#update_addon)
    - [update_cluster_config](#update_cluster_config)
    - [update_cluster_version](#update_cluster_version)
    - [update_nodegroup_config](#update_nodegroup_config)
    - [update_nodegroup_version](#update_nodegroup_version)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)
    - [get_waiter](#get_waiter-4)
    - [get_waiter](#get_waiter-5)

## EKSClient

Type annotations for `boto3.client("eks")`

Can be used directly:

```python
from mypy_boto3_eks.client import EKSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_eks.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ClientException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidRequestException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServerException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.UnsupportedAvailabilityZoneException`


## Methods


### associate_encryption_config

Type annotations for `boto3.client("eks").associate_encryption_config` method.

[Client.associate_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.associate_encryption_config)

```python
def associate_encryption_config(
    self,
    clusterName: str,
    encryptionConfig: List["EncryptionConfigTypeDef"],
    clientRequestToken: str = None
) -> AssociateEncryptionConfigResponseTypeDef:
    pass
```

### associate_identity_provider_config

Type annotations for `boto3.client("eks").associate_identity_provider_config` method.

[Client.associate_identity_provider_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.associate_identity_provider_config)

```python
def associate_identity_provider_config(
    self,
    clusterName: str,
    oidc: OidcIdentityProviderConfigRequestTypeDef,
    tags: Dict[str, str] = None,
    clientRequestToken: str = None
) -> AssociateIdentityProviderConfigResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("eks").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_addon

Type annotations for `boto3.client("eks").create_addon` method.

[Client.create_addon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_addon)

```python
def create_addon(
    self,
    clusterName: str,
    addonName: str,
    addonVersion: str = None,
    serviceAccountRoleArn: str = None,
    resolveConflicts: ResolveConflicts = None,
    clientRequestToken: str = None,
    tags: Dict[str, str] = None
) -> CreateAddonResponseTypeDef:
    pass
```

### create_cluster

Type annotations for `boto3.client("eks").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_cluster)

```python
def create_cluster(
    self,
    name: str,
    roleArn: str,
    resourcesVpcConfig: VpcConfigRequestTypeDef,
    version: str = None,
    kubernetesNetworkConfig: KubernetesNetworkConfigRequestTypeDef = None,
    logging: "LoggingTypeDef" = None,
    clientRequestToken: str = None,
    tags: Dict[str, str] = None,
    encryptionConfig: List["EncryptionConfigTypeDef"] = None
) -> CreateClusterResponseTypeDef:
    pass
```

### create_fargate_profile

Type annotations for `boto3.client("eks").create_fargate_profile` method.

[Client.create_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_fargate_profile)

```python
def create_fargate_profile(
    self,
    fargateProfileName: str,
    clusterName: str,
    podExecutionRoleArn: str,
    subnets: List[str] = None,
    selectors: List["FargateProfileSelectorTypeDef"] = None,
    clientRequestToken: str = None,
    tags: Dict[str, str] = None
) -> CreateFargateProfileResponseTypeDef:
    pass
```

### create_nodegroup

Type annotations for `boto3.client("eks").create_nodegroup` method.

[Client.create_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.create_nodegroup)

```python
def create_nodegroup(
    self,
    clusterName: str,
    nodegroupName: str,
    subnets: List[str],
    nodeRole: str,
    scalingConfig: "NodegroupScalingConfigTypeDef" = None,
    diskSize: int = None,
    instanceTypes: List[str] = None,
    amiType: AMITypes = None,
    remoteAccess: "RemoteAccessConfigTypeDef" = None,
    labels: Dict[str, str] = None,
    tags: Dict[str, str] = None,
    clientRequestToken: str = None,
    launchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
    capacityType: CapacityTypes = None,
    version: str = None,
    releaseVersion: str = None
) -> CreateNodegroupResponseTypeDef:
    pass
```

### delete_addon

Type annotations for `boto3.client("eks").delete_addon` method.

[Client.delete_addon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_addon)

```python
def delete_addon(
    self,
    clusterName: str,
    addonName: str
) -> DeleteAddonResponseTypeDef:
    pass
```

### delete_cluster

Type annotations for `boto3.client("eks").delete_cluster` method.

[Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_cluster)

```python
def delete_cluster(
    self,
    name: str
) -> DeleteClusterResponseTypeDef:
    pass
```

### delete_fargate_profile

Type annotations for `boto3.client("eks").delete_fargate_profile` method.

[Client.delete_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_fargate_profile)

```python
def delete_fargate_profile(
    self,
    clusterName: str,
    fargateProfileName: str
) -> DeleteFargateProfileResponseTypeDef:
    pass
```

### delete_nodegroup

Type annotations for `boto3.client("eks").delete_nodegroup` method.

[Client.delete_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.delete_nodegroup)

```python
def delete_nodegroup(
    self,
    clusterName: str,
    nodegroupName: str
) -> DeleteNodegroupResponseTypeDef:
    pass
```

### describe_addon

Type annotations for `boto3.client("eks").describe_addon` method.

[Client.describe_addon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_addon)

```python
def describe_addon(
    self,
    clusterName: str,
    addonName: str
) -> DescribeAddonResponseTypeDef:
    pass
```

### describe_addon_versions

Type annotations for `boto3.client("eks").describe_addon_versions` method.

[Client.describe_addon_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_addon_versions)

```python
def describe_addon_versions(
    self,
    kubernetesVersion: str = None,
    maxResults: int = None,
    nextToken: str = None,
    addonName: str = None
) -> DescribeAddonVersionsResponseTypeDef:
    pass
```

### describe_cluster

Type annotations for `boto3.client("eks").describe_cluster` method.

[Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_cluster)

```python
def describe_cluster(
    self,
    name: str
) -> DescribeClusterResponseTypeDef:
    pass
```

### describe_fargate_profile

Type annotations for `boto3.client("eks").describe_fargate_profile` method.

[Client.describe_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_fargate_profile)

```python
def describe_fargate_profile(
    self,
    clusterName: str,
    fargateProfileName: str
) -> DescribeFargateProfileResponseTypeDef:
    pass
```

### describe_identity_provider_config

Type annotations for `boto3.client("eks").describe_identity_provider_config` method.

[Client.describe_identity_provider_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_identity_provider_config)

```python
def describe_identity_provider_config(
    self,
    clusterName: str,
    identityProviderConfig: "IdentityProviderConfigTypeDef"
) -> DescribeIdentityProviderConfigResponseTypeDef:
    pass
```

### describe_nodegroup

Type annotations for `boto3.client("eks").describe_nodegroup` method.

[Client.describe_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_nodegroup)

```python
def describe_nodegroup(
    self,
    clusterName: str,
    nodegroupName: str
) -> DescribeNodegroupResponseTypeDef:
    pass
```

### describe_update

Type annotations for `boto3.client("eks").describe_update` method.

[Client.describe_update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.describe_update)

```python
def describe_update(
    self,
    name: str,
    updateId: str,
    nodegroupName: str = None,
    addonName: str = None
) -> DescribeUpdateResponseTypeDef:
    pass
```

### disassociate_identity_provider_config

Type annotations for `boto3.client("eks").disassociate_identity_provider_config` method.

[Client.disassociate_identity_provider_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.disassociate_identity_provider_config)

```python
def disassociate_identity_provider_config(
    self,
    clusterName: str,
    identityProviderConfig: "IdentityProviderConfigTypeDef",
    clientRequestToken: str = None
) -> DisassociateIdentityProviderConfigResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("eks").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.generate_presigned_url)

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

### list_addons

Type annotations for `boto3.client("eks").list_addons` method.

[Client.list_addons documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_addons)

```python
def list_addons(
    self,
    clusterName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListAddonsResponseTypeDef:
    pass
```

### list_clusters

Type annotations for `boto3.client("eks").list_clusters` method.

[Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_clusters)

```python
def list_clusters(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListClustersResponseTypeDef:
    pass
```

### list_fargate_profiles

Type annotations for `boto3.client("eks").list_fargate_profiles` method.

[Client.list_fargate_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_fargate_profiles)

```python
def list_fargate_profiles(
    self,
    clusterName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListFargateProfilesResponseTypeDef:
    pass
```

### list_identity_provider_configs

Type annotations for `boto3.client("eks").list_identity_provider_configs` method.

[Client.list_identity_provider_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_identity_provider_configs)

```python
def list_identity_provider_configs(
    self,
    clusterName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListIdentityProviderConfigsResponseTypeDef:
    pass
```

### list_nodegroups

Type annotations for `boto3.client("eks").list_nodegroups` method.

[Client.list_nodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_nodegroups)

```python
def list_nodegroups(
    self,
    clusterName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListNodegroupsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("eks").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_updates

Type annotations for `boto3.client("eks").list_updates` method.

[Client.list_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.list_updates)

```python
def list_updates(
    self,
    name: str,
    nodegroupName: str = None,
    addonName: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListUpdatesResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("eks").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("eks").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_addon

Type annotations for `boto3.client("eks").update_addon` method.

[Client.update_addon documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_addon)

```python
def update_addon(
    self,
    clusterName: str,
    addonName: str,
    addonVersion: str = None,
    serviceAccountRoleArn: str = None,
    resolveConflicts: ResolveConflicts = None,
    clientRequestToken: str = None
) -> UpdateAddonResponseTypeDef:
    pass
```

### update_cluster_config

Type annotations for `boto3.client("eks").update_cluster_config` method.

[Client.update_cluster_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_cluster_config)

```python
def update_cluster_config(
    self,
    name: str,
    resourcesVpcConfig: VpcConfigRequestTypeDef = None,
    logging: "LoggingTypeDef" = None,
    clientRequestToken: str = None
) -> UpdateClusterConfigResponseTypeDef:
    pass
```

### update_cluster_version

Type annotations for `boto3.client("eks").update_cluster_version` method.

[Client.update_cluster_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_cluster_version)

```python
def update_cluster_version(
    self,
    name: str,
    version: str,
    clientRequestToken: str = None
) -> UpdateClusterVersionResponseTypeDef:
    pass
```

### update_nodegroup_config

Type annotations for `boto3.client("eks").update_nodegroup_config` method.

[Client.update_nodegroup_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_nodegroup_config)

```python
def update_nodegroup_config(
    self,
    clusterName: str,
    nodegroupName: str,
    labels: UpdateLabelsPayloadTypeDef = None,
    scalingConfig: "NodegroupScalingConfigTypeDef" = None,
    clientRequestToken: str = None
) -> UpdateNodegroupConfigResponseTypeDef:
    pass
```

### update_nodegroup_version

Type annotations for `boto3.client("eks").update_nodegroup_version` method.

[Client.update_nodegroup_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client.update_nodegroup_version)

```python
def update_nodegroup_version(
    self,
    clusterName: str,
    nodegroupName: str,
    version: str = None,
    releaseVersion: str = None,
    launchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
    force: bool = None,
    clientRequestToken: str = None
) -> UpdateNodegroupVersionResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.DescribeAddonVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAddonVersionsPaginatorName
) -> DescribeAddonVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.ListAddons documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.ListAddons)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAddonsPaginatorName
) -> ListAddonsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.ListClusters)

```python
@overload
def get_paginator(
    self,
    operation_name: ListClustersPaginatorName
) -> ListClustersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.ListFargateProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFargateProfilesPaginatorName
) -> ListFargateProfilesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.ListIdentityProviderConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.ListIdentityProviderConfigs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListIdentityProviderConfigsPaginatorName
) -> ListIdentityProviderConfigsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.ListNodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.ListNodegroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListNodegroupsPaginatorName
) -> ListNodegroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("eks").get_paginator` method.

[Paginator.ListUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Paginator.ListUpdates)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUpdatesPaginatorName
) -> ListUpdatesPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("eks").get_waiter` method.

[Waiter.AddonActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.AddonActive)

```python
@overload
def get_waiter(
    self,
    waiter_name: AddonActiveWaiterName
) -> AddonActiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("eks").get_waiter` method.

[Waiter.AddonDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.AddonDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: AddonDeletedWaiterName
) -> AddonDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("eks").get_waiter` method.

[Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.ClusterActive)

```python
@overload
def get_waiter(
    self,
    waiter_name: ClusterActiveWaiterName
) -> ClusterActiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("eks").get_waiter` method.

[Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.ClusterDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: ClusterDeletedWaiterName
) -> ClusterDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("eks").get_waiter` method.

[Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.NodegroupActive)

```python
@overload
def get_waiter(
    self,
    waiter_name: NodegroupActiveWaiterName
) -> NodegroupActiveWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("eks").get_waiter` method.

[Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: NodegroupDeletedWaiterName
) -> NodegroupDeletedWaiter:
    pass
```