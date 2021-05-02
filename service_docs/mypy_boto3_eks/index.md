# Type annotations for boto3 EKS module

> [Index](../index.md) > EKS

Auto-generated documentation for [EKS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS)
type annotations stubs module [mypy_boto3_eks](https://pypi.org/project/mypy-boto3-eks/).

```bash
pip install mypy-boto3-eks
```

- [Type annotations for boto3 EKS module](#type-annotations-for-boto3-eks-module)
  - [EKSClient](#eksclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## EKSClient

Type annotations for  `boto3.client("eks")` as [EKSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_eks.client import EKSClient
```


EKSClient [exceptions](./client.md#exceptions)



### Methods
- [associate_encryption_config](./client.md#associate-encryption-config)
- [associate_identity_provider_config](./client.md#associate-identity-provider-config)
- [can_paginate](./client.md#can-paginate)
- [create_addon](./client.md#create-addon)
- [create_cluster](./client.md#create-cluster)
- [create_fargate_profile](./client.md#create-fargate-profile)
- [create_nodegroup](./client.md#create-nodegroup)
- [delete_addon](./client.md#delete-addon)
- [delete_cluster](./client.md#delete-cluster)
- [delete_fargate_profile](./client.md#delete-fargate-profile)
- [delete_nodegroup](./client.md#delete-nodegroup)
- [describe_addon](./client.md#describe-addon)
- [describe_addon_versions](./client.md#describe-addon-versions)
- [describe_cluster](./client.md#describe-cluster)
- [describe_fargate_profile](./client.md#describe-fargate-profile)
- [describe_identity_provider_config](./client.md#describe-identity-provider-config)
- [describe_nodegroup](./client.md#describe-nodegroup)
- [describe_update](./client.md#describe-update)
- [disassociate_identity_provider_config](./client.md#disassociate-identity-provider-config)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_addons](./client.md#list-addons)
- [list_clusters](./client.md#list-clusters)
- [list_fargate_profiles](./client.md#list-fargate-profiles)
- [list_identity_provider_configs](./client.md#list-identity-provider-configs)
- [list_nodegroups](./client.md#list-nodegroups)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_updates](./client.md#list-updates)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_addon](./client.md#update-addon)
- [update_cluster_config](./client.md#update-cluster-config)
- [update_cluster_version](./client.md#update-cluster-version)
- [update_nodegroup_config](./client.md#update-nodegroup-config)
- [update_nodegroup_version](./client.md#update-nodegroup-version)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ClientException](./client.md#clientexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [NotFoundException](./client.md#notfoundexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceLimitExceededException](./client.md#resourcelimitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServerException](./client.md#serverexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [UnsupportedAvailabilityZoneException](./client.md#unsupportedavailabilityzoneexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("eks").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_eks.paginators import DescribeAddonVersionsPaginator, ...
```

- [DescribeAddonVersionsPaginator](./paginators.md#describeaddonversionspaginator)
- [ListAddonsPaginator](./paginators.md#listaddonspaginator)
- [ListClustersPaginator](./paginators.md#listclusterspaginator)
- [ListFargateProfilesPaginator](./paginators.md#listfargateprofilespaginator)
- [ListIdentityProviderConfigsPaginator](./paginators.md#listidentityproviderconfigspaginator)
- [ListNodegroupsPaginator](./paginators.md#listnodegroupspaginator)
- [ListUpdatesPaginator](./paginators.md#listupdatespaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("eks").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_eks.waiters import AddonActiveWaiter, ...
```

- [AddonActiveWaiter](./waiters.md#addonactivewaiter)
- [AddonDeletedWaiter](./waiters.md#addondeletedwaiter)
- [ClusterActiveWaiter](./waiters.md#clusteractivewaiter)
- [ClusterDeletedWaiter](./waiters.md#clusterdeletedwaiter)
- [NodegroupActiveWaiter](./waiters.md#nodegroupactivewaiter)
- [NodegroupDeletedWaiter](./waiters.md#nodegroupdeletedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_eks.literals import AMITypes, ...
```

- [AMITypes](./literals.md#amitypes)
- [AddonActiveWaiterName](./literals.md#addonactivewaitername)
- [AddonDeletedWaiterName](./literals.md#addondeletedwaitername)
- [AddonIssueCode](./literals.md#addonissuecode)
- [AddonStatus](./literals.md#addonstatus)
- [CapacityTypes](./literals.md#capacitytypes)
- [ClusterActiveWaiterName](./literals.md#clusteractivewaitername)
- [ClusterDeletedWaiterName](./literals.md#clusterdeletedwaitername)
- [ClusterStatus](./literals.md#clusterstatus)
- [DescribeAddonVersionsPaginatorName](./literals.md#describeaddonversionspaginatorname)
- [ErrorCode](./literals.md#errorcode)
- [FargateProfileStatus](./literals.md#fargateprofilestatus)
- [ListAddonsPaginatorName](./literals.md#listaddonspaginatorname)
- [ListClustersPaginatorName](./literals.md#listclusterspaginatorname)
- [ListFargateProfilesPaginatorName](./literals.md#listfargateprofilespaginatorname)
- [ListIdentityProviderConfigsPaginatorName](./literals.md#listidentityproviderconfigspaginatorname)
- [ListNodegroupsPaginatorName](./literals.md#listnodegroupspaginatorname)
- [ListUpdatesPaginatorName](./literals.md#listupdatespaginatorname)
- [LogType](./literals.md#logtype)
- [NodegroupActiveWaiterName](./literals.md#nodegroupactivewaitername)
- [NodegroupDeletedWaiterName](./literals.md#nodegroupdeletedwaitername)
- [NodegroupIssueCode](./literals.md#nodegroupissuecode)
- [NodegroupStatus](./literals.md#nodegroupstatus)
- [ResolveConflicts](./literals.md#resolveconflicts)
- [UpdateParamType](./literals.md#updateparamtype)
- [UpdateStatus](./literals.md#updatestatus)
- [UpdateType](./literals.md#updatetype)
- [configStatus](./literals.md#configstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_eks.type_defs import AddonHealthTypeDef, ...
```

- [AddonHealthTypeDef](./type_defs.md#addonhealthtypedef)
- [AddonInfoTypeDef](./type_defs.md#addoninfotypedef)
- [AddonIssueTypeDef](./type_defs.md#addonissuetypedef)
- [AddonTypeDef](./type_defs.md#addontypedef)
- [AddonVersionInfoTypeDef](./type_defs.md#addonversioninfotypedef)
- [AutoScalingGroupTypeDef](./type_defs.md#autoscalinggrouptypedef)
- [CertificateTypeDef](./type_defs.md#certificatetypedef)
- [ClusterTypeDef](./type_defs.md#clustertypedef)
- [CompatibilityTypeDef](./type_defs.md#compatibilitytypedef)
- [EncryptionConfigTypeDef](./type_defs.md#encryptionconfigtypedef)
- [ErrorDetailTypeDef](./type_defs.md#errordetailtypedef)
- [FargateProfileSelectorTypeDef](./type_defs.md#fargateprofileselectortypedef)
- [FargateProfileTypeDef](./type_defs.md#fargateprofiletypedef)
- [IdentityProviderConfigResponseTypeDef](./type_defs.md#identityproviderconfigresponsetypedef)
- [IdentityProviderConfigTypeDef](./type_defs.md#identityproviderconfigtypedef)
- [IdentityTypeDef](./type_defs.md#identitytypedef)
- [IssueTypeDef](./type_defs.md#issuetypedef)
- [KubernetesNetworkConfigResponseTypeDef](./type_defs.md#kubernetesnetworkconfigresponsetypedef)
- [LaunchTemplateSpecificationTypeDef](./type_defs.md#launchtemplatespecificationtypedef)
- [LogSetupTypeDef](./type_defs.md#logsetuptypedef)
- [LoggingTypeDef](./type_defs.md#loggingtypedef)
- [NodegroupHealthTypeDef](./type_defs.md#nodegrouphealthtypedef)
- [NodegroupResourcesTypeDef](./type_defs.md#nodegroupresourcestypedef)
- [NodegroupScalingConfigTypeDef](./type_defs.md#nodegroupscalingconfigtypedef)
- [NodegroupTypeDef](./type_defs.md#nodegrouptypedef)
- [OIDCTypeDef](./type_defs.md#oidctypedef)
- [OidcIdentityProviderConfigTypeDef](./type_defs.md#oidcidentityproviderconfigtypedef)
- [ProviderTypeDef](./type_defs.md#providertypedef)
- [RemoteAccessConfigTypeDef](./type_defs.md#remoteaccessconfigtypedef)
- [UpdateParamTypeDef](./type_defs.md#updateparamtypedef)
- [UpdateTypeDef](./type_defs.md#updatetypedef)
- [VpcConfigResponseTypeDef](./type_defs.md#vpcconfigresponsetypedef)
- [AssociateEncryptionConfigResponseTypeDef](./type_defs.md#associateencryptionconfigresponsetypedef)
- [AssociateIdentityProviderConfigResponseTypeDef](./type_defs.md#associateidentityproviderconfigresponsetypedef)
- [CreateAddonResponseTypeDef](./type_defs.md#createaddonresponsetypedef)
- [CreateClusterResponseTypeDef](./type_defs.md#createclusterresponsetypedef)
- [CreateFargateProfileResponseTypeDef](./type_defs.md#createfargateprofileresponsetypedef)
- [CreateNodegroupResponseTypeDef](./type_defs.md#createnodegroupresponsetypedef)
- [DeleteAddonResponseTypeDef](./type_defs.md#deleteaddonresponsetypedef)
- [DeleteClusterResponseTypeDef](./type_defs.md#deleteclusterresponsetypedef)
- [DeleteFargateProfileResponseTypeDef](./type_defs.md#deletefargateprofileresponsetypedef)
- [DeleteNodegroupResponseTypeDef](./type_defs.md#deletenodegroupresponsetypedef)
- [DescribeAddonResponseTypeDef](./type_defs.md#describeaddonresponsetypedef)
- [DescribeAddonVersionsResponseTypeDef](./type_defs.md#describeaddonversionsresponsetypedef)
- [DescribeClusterResponseTypeDef](./type_defs.md#describeclusterresponsetypedef)
- [DescribeFargateProfileResponseTypeDef](./type_defs.md#describefargateprofileresponsetypedef)
- [DescribeIdentityProviderConfigResponseTypeDef](./type_defs.md#describeidentityproviderconfigresponsetypedef)
- [DescribeNodegroupResponseTypeDef](./type_defs.md#describenodegroupresponsetypedef)
- [DescribeUpdateResponseTypeDef](./type_defs.md#describeupdateresponsetypedef)
- [DisassociateIdentityProviderConfigResponseTypeDef](./type_defs.md#disassociateidentityproviderconfigresponsetypedef)
- [KubernetesNetworkConfigRequestTypeDef](./type_defs.md#kubernetesnetworkconfigrequesttypedef)
- [ListAddonsResponseTypeDef](./type_defs.md#listaddonsresponsetypedef)
- [ListClustersResponseTypeDef](./type_defs.md#listclustersresponsetypedef)
- [ListFargateProfilesResponseTypeDef](./type_defs.md#listfargateprofilesresponsetypedef)
- [ListIdentityProviderConfigsResponseTypeDef](./type_defs.md#listidentityproviderconfigsresponsetypedef)
- [ListNodegroupsResponseTypeDef](./type_defs.md#listnodegroupsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListUpdatesResponseTypeDef](./type_defs.md#listupdatesresponsetypedef)
- [OidcIdentityProviderConfigRequestTypeDef](./type_defs.md#oidcidentityproviderconfigrequesttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateAddonResponseTypeDef](./type_defs.md#updateaddonresponsetypedef)
- [UpdateClusterConfigResponseTypeDef](./type_defs.md#updateclusterconfigresponsetypedef)
- [UpdateClusterVersionResponseTypeDef](./type_defs.md#updateclusterversionresponsetypedef)
- [UpdateLabelsPayloadTypeDef](./type_defs.md#updatelabelspayloadtypedef)
- [UpdateNodegroupConfigResponseTypeDef](./type_defs.md#updatenodegroupconfigresponsetypedef)
- [UpdateNodegroupVersionResponseTypeDef](./type_defs.md#updatenodegroupversionresponsetypedef)
- [VpcConfigRequestTypeDef](./type_defs.md#vpcconfigrequesttypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
