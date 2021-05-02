# Literals for boto3 EKS module

> [Index](../index.md) > [EKS](./index.md) > Literals

Auto-generated documentation for [EKS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS)
type annotations stubs module [mypy_boto3_eks](https://pypi.org/project/mypy-boto3-eks/).

- [Literals for boto3 EKS module](#literals-for-boto3-eks-module)
  - [AMITypes](#amitypes)
  - [AddonActiveWaiterName](#addonactivewaitername)
  - [AddonDeletedWaiterName](#addondeletedwaitername)
  - [AddonIssueCode](#addonissuecode)
  - [AddonStatus](#addonstatus)
  - [CapacityTypes](#capacitytypes)
  - [ClusterActiveWaiterName](#clusteractivewaitername)
  - [ClusterDeletedWaiterName](#clusterdeletedwaitername)
  - [ClusterStatus](#clusterstatus)
  - [DescribeAddonVersionsPaginatorName](#describeaddonversionspaginatorname)
  - [ErrorCode](#errorcode)
  - [FargateProfileStatus](#fargateprofilestatus)
  - [ListAddonsPaginatorName](#listaddonspaginatorname)
  - [ListClustersPaginatorName](#listclusterspaginatorname)
  - [ListFargateProfilesPaginatorName](#listfargateprofilespaginatorname)
  - [ListIdentityProviderConfigsPaginatorName](#listidentityproviderconfigspaginatorname)
  - [ListNodegroupsPaginatorName](#listnodegroupspaginatorname)
  - [ListUpdatesPaginatorName](#listupdatespaginatorname)
  - [LogType](#logtype)
  - [NodegroupActiveWaiterName](#nodegroupactivewaitername)
  - [NodegroupDeletedWaiterName](#nodegroupdeletedwaitername)
  - [NodegroupIssueCode](#nodegroupissuecode)
  - [NodegroupStatus](#nodegroupstatus)
  - [ResolveConflicts](#resolveconflicts)
  - [UpdateParamType](#updateparamtype)
  - [UpdateStatus](#updatestatus)
  - [UpdateType](#updatetype)
  - [configStatus](#configstatus)

## AMITypes

```python
from mypy_boto3_eks.literals import AMITypes
```

Values:

- `AL2_ARM_64`
- `AL2_x86_64`
- `AL2_x86_64_GPU`
- `CUSTOM`

## AddonActiveWaiterName

```python
from mypy_boto3_eks.literals import AddonActiveWaiterName
```

Values:

- `addon_active`

## AddonDeletedWaiterName

```python
from mypy_boto3_eks.literals import AddonDeletedWaiterName
```

Values:

- `addon_deleted`

## AddonIssueCode

```python
from mypy_boto3_eks.literals import AddonIssueCode
```

Values:

- `AccessDenied`
- `AdmissionRequestDenied`
- `ClusterUnreachable`
- `ConfigurationConflict`
- `InsufficientNumberOfReplicas`
- `InternalFailure`

## AddonStatus

```python
from mypy_boto3_eks.literals import AddonStatus
```

Values:

- `ACTIVE`
- `CREATE_FAILED`
- `CREATING`
- `DEGRADED`
- `DELETE_FAILED`
- `DELETING`
- `UPDATING`

## CapacityTypes

```python
from mypy_boto3_eks.literals import CapacityTypes
```

Values:

- `ON_DEMAND`
- `SPOT`

## ClusterActiveWaiterName

```python
from mypy_boto3_eks.literals import ClusterActiveWaiterName
```

Values:

- `cluster_active`

## ClusterDeletedWaiterName

```python
from mypy_boto3_eks.literals import ClusterDeletedWaiterName
```

Values:

- `cluster_deleted`

## ClusterStatus

```python
from mypy_boto3_eks.literals import ClusterStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `UPDATING`

## DescribeAddonVersionsPaginatorName

```python
from mypy_boto3_eks.literals import DescribeAddonVersionsPaginatorName
```

Values:

- `describe_addon_versions`

## ErrorCode

```python
from mypy_boto3_eks.literals import ErrorCode
```

Values:

- `AccessDenied`
- `AdmissionRequestDenied`
- `ClusterUnreachable`
- `ConfigurationConflict`
- `EniLimitReached`
- `InsufficientFreeAddresses`
- `InsufficientNumberOfReplicas`
- `IpNotAvailable`
- `NodeCreationFailure`
- `OperationNotPermitted`
- `PodEvictionFailure`
- `SecurityGroupNotFound`
- `SubnetNotFound`
- `Unknown`
- `VpcIdNotFound`

## FargateProfileStatus

```python
from mypy_boto3_eks.literals import FargateProfileStatus
```

Values:

- `ACTIVE`
- `CREATE_FAILED`
- `CREATING`
- `DELETE_FAILED`
- `DELETING`

## ListAddonsPaginatorName

```python
from mypy_boto3_eks.literals import ListAddonsPaginatorName
```

Values:

- `list_addons`

## ListClustersPaginatorName

```python
from mypy_boto3_eks.literals import ListClustersPaginatorName
```

Values:

- `list_clusters`

## ListFargateProfilesPaginatorName

```python
from mypy_boto3_eks.literals import ListFargateProfilesPaginatorName
```

Values:

- `list_fargate_profiles`

## ListIdentityProviderConfigsPaginatorName

```python
from mypy_boto3_eks.literals import ListIdentityProviderConfigsPaginatorName
```

Values:

- `list_identity_provider_configs`

## ListNodegroupsPaginatorName

```python
from mypy_boto3_eks.literals import ListNodegroupsPaginatorName
```

Values:

- `list_nodegroups`

## ListUpdatesPaginatorName

```python
from mypy_boto3_eks.literals import ListUpdatesPaginatorName
```

Values:

- `list_updates`

## LogType

```python
from mypy_boto3_eks.literals import LogType
```

Values:

- `api`
- `audit`
- `authenticator`
- `controllerManager`
- `scheduler`

## NodegroupActiveWaiterName

```python
from mypy_boto3_eks.literals import NodegroupActiveWaiterName
```

Values:

- `nodegroup_active`

## NodegroupDeletedWaiterName

```python
from mypy_boto3_eks.literals import NodegroupDeletedWaiterName
```

Values:

- `nodegroup_deleted`

## NodegroupIssueCode

```python
from mypy_boto3_eks.literals import NodegroupIssueCode
```

Values:

- `AccessDenied`
- `AsgInstanceLaunchFailures`
- `AutoScalingGroupInvalidConfiguration`
- `AutoScalingGroupNotFound`
- `ClusterUnreachable`
- `Ec2LaunchTemplateNotFound`
- `Ec2LaunchTemplateVersionMismatch`
- `Ec2SecurityGroupDeletionFailure`
- `Ec2SecurityGroupNotFound`
- `Ec2SubnetInvalidConfiguration`
- `Ec2SubnetNotFound`
- `IamInstanceProfileNotFound`
- `IamLimitExceeded`
- `IamNodeRoleNotFound`
- `InstanceLimitExceeded`
- `InsufficientFreeAddresses`
- `InternalFailure`
- `NodeCreationFailure`

## NodegroupStatus

```python
from mypy_boto3_eks.literals import NodegroupStatus
```

Values:

- `ACTIVE`
- `CREATE_FAILED`
- `CREATING`
- `DEGRADED`
- `DELETE_FAILED`
- `DELETING`
- `UPDATING`

## ResolveConflicts

```python
from mypy_boto3_eks.literals import ResolveConflicts
```

Values:

- `NONE`
- `OVERWRITE`

## UpdateParamType

```python
from mypy_boto3_eks.literals import UpdateParamType
```

Values:

- `AddonVersion`
- `ClusterLogging`
- `DesiredSize`
- `EncryptionConfig`
- `EndpointPrivateAccess`
- `EndpointPublicAccess`
- `IdentityProviderConfig`
- `LabelsToAdd`
- `LabelsToRemove`
- `LaunchTemplateName`
- `LaunchTemplateVersion`
- `MaxSize`
- `MinSize`
- `PlatformVersion`
- `PublicAccessCidrs`
- `ReleaseVersion`
- `ResolveConflicts`
- `ServiceAccountRoleArn`
- `Version`

## UpdateStatus

```python
from mypy_boto3_eks.literals import UpdateStatus
```

Values:

- `Cancelled`
- `Failed`
- `InProgress`
- `Successful`

## UpdateType

```python
from mypy_boto3_eks.literals import UpdateType
```

Values:

- `AddonUpdate`
- `AssociateEncryptionConfig`
- `AssociateIdentityProviderConfig`
- `ConfigUpdate`
- `DisassociateIdentityProviderConfig`
- `EndpointAccessUpdate`
- `LoggingUpdate`
- `VersionUpdate`

## configStatus

```python
from mypy_boto3_eks.literals import configStatus
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
