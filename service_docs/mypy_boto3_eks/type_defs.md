# Structures for boto3 EKS module

> [Index](../index.md) > [EKS](./index.md) > Structures

Auto-generated documentation for [EKS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS)
type annotations stubs module [mypy_boto3_eks](https://pypi.org/project/mypy-boto3-eks/).

- [Structures for boto3 EKS module](#structures-for-boto3-eks-module)
  - [AddonHealthTypeDef](#addonhealthtypedef)
  - [AddonInfoTypeDef](#addoninfotypedef)
  - [AddonIssueTypeDef](#addonissuetypedef)
  - [AddonTypeDef](#addontypedef)
  - [AddonVersionInfoTypeDef](#addonversioninfotypedef)
  - [AssociateEncryptionConfigResponseTypeDef](#associateencryptionconfigresponsetypedef)
  - [AssociateIdentityProviderConfigResponseTypeDef](#associateidentityproviderconfigresponsetypedef)
  - [AutoScalingGroupTypeDef](#autoscalinggrouptypedef)
  - [CertificateTypeDef](#certificatetypedef)
  - [ClusterTypeDef](#clustertypedef)
  - [CompatibilityTypeDef](#compatibilitytypedef)
  - [CreateAddonResponseTypeDef](#createaddonresponsetypedef)
  - [CreateClusterResponseTypeDef](#createclusterresponsetypedef)
  - [CreateFargateProfileResponseTypeDef](#createfargateprofileresponsetypedef)
  - [CreateNodegroupResponseTypeDef](#createnodegroupresponsetypedef)
  - [DeleteAddonResponseTypeDef](#deleteaddonresponsetypedef)
  - [DeleteClusterResponseTypeDef](#deleteclusterresponsetypedef)
  - [DeleteFargateProfileResponseTypeDef](#deletefargateprofileresponsetypedef)
  - [DeleteNodegroupResponseTypeDef](#deletenodegroupresponsetypedef)
  - [DescribeAddonResponseTypeDef](#describeaddonresponsetypedef)
  - [DescribeAddonVersionsResponseTypeDef](#describeaddonversionsresponsetypedef)
  - [DescribeClusterResponseTypeDef](#describeclusterresponsetypedef)
  - [DescribeFargateProfileResponseTypeDef](#describefargateprofileresponsetypedef)
  - [DescribeIdentityProviderConfigResponseTypeDef](#describeidentityproviderconfigresponsetypedef)
  - [DescribeNodegroupResponseTypeDef](#describenodegroupresponsetypedef)
  - [DescribeUpdateResponseTypeDef](#describeupdateresponsetypedef)
  - [DisassociateIdentityProviderConfigResponseTypeDef](#disassociateidentityproviderconfigresponsetypedef)
  - [EncryptionConfigTypeDef](#encryptionconfigtypedef)
  - [ErrorDetailTypeDef](#errordetailtypedef)
  - [FargateProfileSelectorTypeDef](#fargateprofileselectortypedef)
  - [FargateProfileTypeDef](#fargateprofiletypedef)
  - [IdentityProviderConfigResponseTypeDef](#identityproviderconfigresponsetypedef)
  - [IdentityProviderConfigTypeDef](#identityproviderconfigtypedef)
  - [IdentityTypeDef](#identitytypedef)
  - [IssueTypeDef](#issuetypedef)
  - [KubernetesNetworkConfigRequestTypeDef](#kubernetesnetworkconfigrequesttypedef)
  - [KubernetesNetworkConfigResponseTypeDef](#kubernetesnetworkconfigresponsetypedef)
  - [LaunchTemplateSpecificationTypeDef](#launchtemplatespecificationtypedef)
  - [ListAddonsResponseTypeDef](#listaddonsresponsetypedef)
  - [ListClustersResponseTypeDef](#listclustersresponsetypedef)
  - [ListFargateProfilesResponseTypeDef](#listfargateprofilesresponsetypedef)
  - [ListIdentityProviderConfigsResponseTypeDef](#listidentityproviderconfigsresponsetypedef)
  - [ListNodegroupsResponseTypeDef](#listnodegroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListUpdatesResponseTypeDef](#listupdatesresponsetypedef)
  - [LogSetupTypeDef](#logsetuptypedef)
  - [LoggingTypeDef](#loggingtypedef)
  - [NodegroupHealthTypeDef](#nodegrouphealthtypedef)
  - [NodegroupResourcesTypeDef](#nodegroupresourcestypedef)
  - [NodegroupScalingConfigTypeDef](#nodegroupscalingconfigtypedef)
  - [NodegroupTypeDef](#nodegrouptypedef)
  - [OIDCTypeDef](#oidctypedef)
  - [OidcIdentityProviderConfigRequestTypeDef](#oidcidentityproviderconfigrequesttypedef)
  - [OidcIdentityProviderConfigTypeDef](#oidcidentityproviderconfigtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProviderTypeDef](#providertypedef)
  - [RemoteAccessConfigTypeDef](#remoteaccessconfigtypedef)
  - [UpdateAddonResponseTypeDef](#updateaddonresponsetypedef)
  - [UpdateClusterConfigResponseTypeDef](#updateclusterconfigresponsetypedef)
  - [UpdateClusterVersionResponseTypeDef](#updateclusterversionresponsetypedef)
  - [UpdateLabelsPayloadTypeDef](#updatelabelspayloadtypedef)
  - [UpdateNodegroupConfigResponseTypeDef](#updatenodegroupconfigresponsetypedef)
  - [UpdateNodegroupVersionResponseTypeDef](#updatenodegroupversionresponsetypedef)
  - [UpdateParamTypeDef](#updateparamtypedef)
  - [UpdateTypeDef](#updatetypedef)
  - [VpcConfigRequestTypeDef](#vpcconfigrequesttypedef)
  - [VpcConfigResponseTypeDef](#vpcconfigresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AddonHealthTypeDef

```python
from mypy_boto3_eks.type_defs import AddonHealthTypeDef
```




Optional fields:
- `issues`: `List["AddonIssueTypeDef"]`


## AddonInfoTypeDef

```python
from mypy_boto3_eks.type_defs import AddonInfoTypeDef
```




Optional fields:
- `addonName`: `str`
- `type`: `str`
- `addonVersions`: `List["AddonVersionInfoTypeDef"]`


## AddonIssueTypeDef

```python
from mypy_boto3_eks.type_defs import AddonIssueTypeDef
```




Optional fields:
- `code`: `AddonIssueCode`
- `message`: `str`
- `resourceIds`: `List[str]`


## AddonTypeDef

```python
from mypy_boto3_eks.type_defs import AddonTypeDef
```




Optional fields:
- `addonName`: `str`
- `clusterName`: `str`
- `status`: `AddonStatus`
- `addonVersion`: `str`
- `health`: `"AddonHealthTypeDef"`
- `addonArn`: `str`
- `createdAt`: `datetime`
- `modifiedAt`: `datetime`
- `serviceAccountRoleArn`: `str`
- `tags`: `Dict[str, str]`


## AddonVersionInfoTypeDef

```python
from mypy_boto3_eks.type_defs import AddonVersionInfoTypeDef
```




Optional fields:
- `addonVersion`: `str`
- `architecture`: `List[str]`
- `compatibilities`: `List["CompatibilityTypeDef"]`


## AssociateEncryptionConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import AssociateEncryptionConfigResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## AssociateIdentityProviderConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import AssociateIdentityProviderConfigResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`
- `tags`: `Dict[str, str]`


## AutoScalingGroupTypeDef

```python
from mypy_boto3_eks.type_defs import AutoScalingGroupTypeDef
```




Optional fields:
- `name`: `str`


## CertificateTypeDef

```python
from mypy_boto3_eks.type_defs import CertificateTypeDef
```




Optional fields:
- `data`: `str`


## ClusterTypeDef

```python
from mypy_boto3_eks.type_defs import ClusterTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `version`: `str`
- `endpoint`: `str`
- `roleArn`: `str`
- `resourcesVpcConfig`: `"VpcConfigResponseTypeDef"`
- `kubernetesNetworkConfig`: `"KubernetesNetworkConfigResponseTypeDef"`
- `logging`: `"LoggingTypeDef"`
- `identity`: `"IdentityTypeDef"`
- `status`: `ClusterStatus`
- `certificateAuthority`: `"CertificateTypeDef"`
- `clientRequestToken`: `str`
- `platformVersion`: `str`
- `tags`: `Dict[str, str]`
- `encryptionConfig`: `List["EncryptionConfigTypeDef"]`


## CompatibilityTypeDef

```python
from mypy_boto3_eks.type_defs import CompatibilityTypeDef
```




Optional fields:
- `clusterVersion`: `str`
- `platformVersions`: `List[str]`
- `defaultVersion`: `bool`


## CreateAddonResponseTypeDef

```python
from mypy_boto3_eks.type_defs import CreateAddonResponseTypeDef
```




Optional fields:
- `addon`: `"AddonTypeDef"`


## CreateClusterResponseTypeDef

```python
from mypy_boto3_eks.type_defs import CreateClusterResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## CreateFargateProfileResponseTypeDef

```python
from mypy_boto3_eks.type_defs import CreateFargateProfileResponseTypeDef
```




Optional fields:
- `fargateProfile`: `"FargateProfileTypeDef"`


## CreateNodegroupResponseTypeDef

```python
from mypy_boto3_eks.type_defs import CreateNodegroupResponseTypeDef
```




Optional fields:
- `nodegroup`: `"NodegroupTypeDef"`


## DeleteAddonResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DeleteAddonResponseTypeDef
```




Optional fields:
- `addon`: `"AddonTypeDef"`


## DeleteClusterResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DeleteClusterResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## DeleteFargateProfileResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DeleteFargateProfileResponseTypeDef
```




Optional fields:
- `fargateProfile`: `"FargateProfileTypeDef"`


## DeleteNodegroupResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DeleteNodegroupResponseTypeDef
```




Optional fields:
- `nodegroup`: `"NodegroupTypeDef"`


## DescribeAddonResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeAddonResponseTypeDef
```




Optional fields:
- `addon`: `"AddonTypeDef"`


## DescribeAddonVersionsResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeAddonVersionsResponseTypeDef
```




Optional fields:
- `addons`: `List["AddonInfoTypeDef"]`
- `nextToken`: `str`


## DescribeClusterResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeClusterResponseTypeDef
```




Optional fields:
- `cluster`: `"ClusterTypeDef"`


## DescribeFargateProfileResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeFargateProfileResponseTypeDef
```




Optional fields:
- `fargateProfile`: `"FargateProfileTypeDef"`


## DescribeIdentityProviderConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeIdentityProviderConfigResponseTypeDef
```




Optional fields:
- `identityProviderConfig`: `"IdentityProviderConfigResponseTypeDef"`


## DescribeNodegroupResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeNodegroupResponseTypeDef
```




Optional fields:
- `nodegroup`: `"NodegroupTypeDef"`


## DescribeUpdateResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DescribeUpdateResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## DisassociateIdentityProviderConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import DisassociateIdentityProviderConfigResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## EncryptionConfigTypeDef

```python
from mypy_boto3_eks.type_defs import EncryptionConfigTypeDef
```




Optional fields:
- `resources`: `List[str]`
- `provider`: `"ProviderTypeDef"`


## ErrorDetailTypeDef

```python
from mypy_boto3_eks.type_defs import ErrorDetailTypeDef
```




Optional fields:
- `errorCode`: `ErrorCode`
- `errorMessage`: `str`
- `resourceIds`: `List[str]`


## FargateProfileSelectorTypeDef

```python
from mypy_boto3_eks.type_defs import FargateProfileSelectorTypeDef
```




Optional fields:
- `namespace`: `str`
- `labels`: `Dict[str, str]`


## FargateProfileTypeDef

```python
from mypy_boto3_eks.type_defs import FargateProfileTypeDef
```




Optional fields:
- `fargateProfileName`: `str`
- `fargateProfileArn`: `str`
- `clusterName`: `str`
- `createdAt`: `datetime`
- `podExecutionRoleArn`: `str`
- `subnets`: `List[str]`
- `selectors`: `List["FargateProfileSelectorTypeDef"]`
- `status`: `FargateProfileStatus`
- `tags`: `Dict[str, str]`


## IdentityProviderConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import IdentityProviderConfigResponseTypeDef
```




Optional fields:
- `oidc`: `"OidcIdentityProviderConfigTypeDef"`


## IdentityProviderConfigTypeDef

```python
from mypy_boto3_eks.type_defs import IdentityProviderConfigTypeDef
```


Required fields:
- `type`: `str`
- `name`: `str`




## IdentityTypeDef

```python
from mypy_boto3_eks.type_defs import IdentityTypeDef
```




Optional fields:
- `oidc`: `"OIDCTypeDef"`


## IssueTypeDef

```python
from mypy_boto3_eks.type_defs import IssueTypeDef
```




Optional fields:
- `code`: `NodegroupIssueCode`
- `message`: `str`
- `resourceIds`: `List[str]`


## KubernetesNetworkConfigRequestTypeDef

```python
from mypy_boto3_eks.type_defs import KubernetesNetworkConfigRequestTypeDef
```




Optional fields:
- `serviceIpv4Cidr`: `str`


## KubernetesNetworkConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import KubernetesNetworkConfigResponseTypeDef
```




Optional fields:
- `serviceIpv4Cidr`: `str`


## LaunchTemplateSpecificationTypeDef

```python
from mypy_boto3_eks.type_defs import LaunchTemplateSpecificationTypeDef
```




Optional fields:
- `name`: `str`
- `version`: `str`
- `id`: `str`


## ListAddonsResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListAddonsResponseTypeDef
```




Optional fields:
- `addons`: `List[str]`
- `nextToken`: `str`


## ListClustersResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListClustersResponseTypeDef
```




Optional fields:
- `clusters`: `List[str]`
- `nextToken`: `str`


## ListFargateProfilesResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListFargateProfilesResponseTypeDef
```




Optional fields:
- `fargateProfileNames`: `List[str]`
- `nextToken`: `str`


## ListIdentityProviderConfigsResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListIdentityProviderConfigsResponseTypeDef
```




Optional fields:
- `identityProviderConfigs`: `List["IdentityProviderConfigTypeDef"]`
- `nextToken`: `str`


## ListNodegroupsResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListNodegroupsResponseTypeDef
```




Optional fields:
- `nodegroups`: `List[str]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListUpdatesResponseTypeDef

```python
from mypy_boto3_eks.type_defs import ListUpdatesResponseTypeDef
```




Optional fields:
- `updateIds`: `List[str]`
- `nextToken`: `str`


## LogSetupTypeDef

```python
from mypy_boto3_eks.type_defs import LogSetupTypeDef
```




Optional fields:
- `types`: `List[LogType]`
- `enabled`: `bool`


## LoggingTypeDef

```python
from mypy_boto3_eks.type_defs import LoggingTypeDef
```




Optional fields:
- `clusterLogging`: `List["LogSetupTypeDef"]`


## NodegroupHealthTypeDef

```python
from mypy_boto3_eks.type_defs import NodegroupHealthTypeDef
```




Optional fields:
- `issues`: `List["IssueTypeDef"]`


## NodegroupResourcesTypeDef

```python
from mypy_boto3_eks.type_defs import NodegroupResourcesTypeDef
```




Optional fields:
- `autoScalingGroups`: `List["AutoScalingGroupTypeDef"]`
- `remoteAccessSecurityGroup`: `str`


## NodegroupScalingConfigTypeDef

```python
from mypy_boto3_eks.type_defs import NodegroupScalingConfigTypeDef
```




Optional fields:
- `minSize`: `int`
- `maxSize`: `int`
- `desiredSize`: `int`


## NodegroupTypeDef

```python
from mypy_boto3_eks.type_defs import NodegroupTypeDef
```




Optional fields:
- `nodegroupName`: `str`
- `nodegroupArn`: `str`
- `clusterName`: `str`
- `version`: `str`
- `releaseVersion`: `str`
- `createdAt`: `datetime`
- `modifiedAt`: `datetime`
- `status`: `NodegroupStatus`
- `capacityType`: `CapacityTypes`
- `scalingConfig`: `"NodegroupScalingConfigTypeDef"`
- `instanceTypes`: `List[str]`
- `subnets`: `List[str]`
- `remoteAccess`: `"RemoteAccessConfigTypeDef"`
- `amiType`: `AMITypes`
- `nodeRole`: `str`
- `labels`: `Dict[str, str]`
- `resources`: `"NodegroupResourcesTypeDef"`
- `diskSize`: `int`
- `health`: `"NodegroupHealthTypeDef"`
- `launchTemplate`: `"LaunchTemplateSpecificationTypeDef"`
- `tags`: `Dict[str, str]`


## OIDCTypeDef

```python
from mypy_boto3_eks.type_defs import OIDCTypeDef
```




Optional fields:
- `issuer`: `str`


## OidcIdentityProviderConfigRequestTypeDef

```python
from mypy_boto3_eks.type_defs import OidcIdentityProviderConfigRequestTypeDef
```


Required fields:
- `identityProviderConfigName`: `str`
- `issuerUrl`: `str`
- `clientId`: `str`



Optional fields:
- `usernameClaim`: `str`
- `usernamePrefix`: `str`
- `groupsClaim`: `str`
- `groupsPrefix`: `str`
- `requiredClaims`: `Dict[str, str]`


## OidcIdentityProviderConfigTypeDef

```python
from mypy_boto3_eks.type_defs import OidcIdentityProviderConfigTypeDef
```




Optional fields:
- `identityProviderConfigName`: `str`
- `identityProviderConfigArn`: `str`
- `clusterName`: `str`
- `issuerUrl`: `str`
- `clientId`: `str`
- `usernameClaim`: `str`
- `usernamePrefix`: `str`
- `groupsClaim`: `str`
- `groupsPrefix`: `str`
- `requiredClaims`: `Dict[str, str]`
- `tags`: `Dict[str, str]`
- `status`: `configStatus`


## PaginatorConfigTypeDef

```python
from mypy_boto3_eks.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProviderTypeDef

```python
from mypy_boto3_eks.type_defs import ProviderTypeDef
```




Optional fields:
- `keyArn`: `str`


## RemoteAccessConfigTypeDef

```python
from mypy_boto3_eks.type_defs import RemoteAccessConfigTypeDef
```




Optional fields:
- `ec2SshKey`: `str`
- `sourceSecurityGroups`: `List[str]`


## UpdateAddonResponseTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateAddonResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## UpdateClusterConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateClusterConfigResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## UpdateClusterVersionResponseTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateClusterVersionResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## UpdateLabelsPayloadTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateLabelsPayloadTypeDef
```




Optional fields:
- `addOrUpdateLabels`: `Dict[str, str]`
- `removeLabels`: `List[str]`


## UpdateNodegroupConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateNodegroupConfigResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## UpdateNodegroupVersionResponseTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateNodegroupVersionResponseTypeDef
```




Optional fields:
- `update`: `"UpdateTypeDef"`


## UpdateParamTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateParamTypeDef
```




Optional fields:
- `type`: `UpdateParamType`
- `value`: `str`


## UpdateTypeDef

```python
from mypy_boto3_eks.type_defs import UpdateTypeDef
```




Optional fields:
- `id`: `str`
- `status`: `UpdateStatus`
- `type`: `UpdateType`
- `params`: `List["UpdateParamTypeDef"]`
- `createdAt`: `datetime`
- `errors`: `List["ErrorDetailTypeDef"]`


## VpcConfigRequestTypeDef

```python
from mypy_boto3_eks.type_defs import VpcConfigRequestTypeDef
```




Optional fields:
- `subnetIds`: `List[str]`
- `securityGroupIds`: `List[str]`
- `endpointPublicAccess`: `bool`
- `endpointPrivateAccess`: `bool`
- `publicAccessCidrs`: `List[str]`


## VpcConfigResponseTypeDef

```python
from mypy_boto3_eks.type_defs import VpcConfigResponseTypeDef
```




Optional fields:
- `subnetIds`: `List[str]`
- `securityGroupIds`: `List[str]`
- `clusterSecurityGroupId`: `str`
- `vpcId`: `str`
- `endpointPublicAccess`: `bool`
- `endpointPrivateAccess`: `bool`
- `publicAccessCidrs`: `List[str]`


## WaiterConfigTypeDef

```python
from mypy_boto3_eks.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

