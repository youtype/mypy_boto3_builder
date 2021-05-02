# Structures for boto3 Batch module

> [Index](../index.md) > [Batch](./index.md) > Structures

Auto-generated documentation for [Batch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch)
type annotations stubs module [mypy_boto3_batch](https://pypi.org/project/mypy-boto3-batch/).

- [Structures for boto3 Batch module](#structures-for-boto3-batch-module)
  - [ArrayPropertiesDetailTypeDef](#arraypropertiesdetailtypedef)
  - [ArrayPropertiesSummaryTypeDef](#arraypropertiessummarytypedef)
  - [AttemptContainerDetailTypeDef](#attemptcontainerdetailtypedef)
  - [AttemptDetailTypeDef](#attemptdetailtypedef)
  - [ComputeEnvironmentDetailTypeDef](#computeenvironmentdetailtypedef)
  - [ComputeEnvironmentOrderTypeDef](#computeenvironmentordertypedef)
  - [ComputeResourceTypeDef](#computeresourcetypedef)
  - [ContainerDetailTypeDef](#containerdetailtypedef)
  - [ContainerOverridesTypeDef](#containeroverridestypedef)
  - [ContainerPropertiesTypeDef](#containerpropertiestypedef)
  - [ContainerSummaryTypeDef](#containersummarytypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [EFSAuthorizationConfigTypeDef](#efsauthorizationconfigtypedef)
  - [EFSVolumeConfigurationTypeDef](#efsvolumeconfigurationtypedef)
  - [Ec2ConfigurationTypeDef](#ec2configurationtypedef)
  - [EvaluateOnExitTypeDef](#evaluateonexittypedef)
  - [FargatePlatformConfigurationTypeDef](#fargateplatformconfigurationtypedef)
  - [HostTypeDef](#hosttypedef)
  - [JobDefinitionTypeDef](#jobdefinitiontypedef)
  - [JobDependencyTypeDef](#jobdependencytypedef)
  - [JobDetailTypeDef](#jobdetailtypedef)
  - [JobQueueDetailTypeDef](#jobqueuedetailtypedef)
  - [JobSummaryTypeDef](#jobsummarytypedef)
  - [JobTimeoutTypeDef](#jobtimeouttypedef)
  - [KeyValuePairTypeDef](#keyvaluepairtypedef)
  - [LaunchTemplateSpecificationTypeDef](#launchtemplatespecificationtypedef)
  - [LinuxParametersTypeDef](#linuxparameterstypedef)
  - [LogConfigurationTypeDef](#logconfigurationtypedef)
  - [MountPointTypeDef](#mountpointtypedef)
  - [NetworkConfigurationTypeDef](#networkconfigurationtypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [NodeDetailsTypeDef](#nodedetailstypedef)
  - [NodePropertiesSummaryTypeDef](#nodepropertiessummarytypedef)
  - [NodePropertiesTypeDef](#nodepropertiestypedef)
  - [NodePropertyOverrideTypeDef](#nodepropertyoverridetypedef)
  - [NodeRangePropertyTypeDef](#noderangepropertytypedef)
  - [ResourceRequirementTypeDef](#resourcerequirementtypedef)
  - [RetryStrategyTypeDef](#retrystrategytypedef)
  - [SecretTypeDef](#secrettypedef)
  - [TmpfsTypeDef](#tmpfstypedef)
  - [UlimitTypeDef](#ulimittypedef)
  - [VolumeTypeDef](#volumetypedef)
  - [ArrayPropertiesTypeDef](#arraypropertiestypedef)
  - [ComputeResourceUpdateTypeDef](#computeresourceupdatetypedef)
  - [CreateComputeEnvironmentResponseTypeDef](#createcomputeenvironmentresponsetypedef)
  - [CreateJobQueueResponseTypeDef](#createjobqueueresponsetypedef)
  - [DescribeComputeEnvironmentsResponseTypeDef](#describecomputeenvironmentsresponsetypedef)
  - [DescribeJobDefinitionsResponseTypeDef](#describejobdefinitionsresponsetypedef)
  - [DescribeJobQueuesResponseTypeDef](#describejobqueuesresponsetypedef)
  - [DescribeJobsResponseTypeDef](#describejobsresponsetypedef)
  - [ListJobsResponseTypeDef](#listjobsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [NodeOverridesTypeDef](#nodeoverridestypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RegisterJobDefinitionResponseTypeDef](#registerjobdefinitionresponsetypedef)
  - [SubmitJobResponseTypeDef](#submitjobresponsetypedef)
  - [UpdateComputeEnvironmentResponseTypeDef](#updatecomputeenvironmentresponsetypedef)
  - [UpdateJobQueueResponseTypeDef](#updatejobqueueresponsetypedef)

## ArrayPropertiesDetailTypeDef

```python
from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef
```




Optional fields:
- `statusSummary`: `Dict[str, int]`
- `size`: `int`
- `index`: `int`


## ArrayPropertiesSummaryTypeDef

```python
from mypy_boto3_batch.type_defs import ArrayPropertiesSummaryTypeDef
```




Optional fields:
- `size`: `int`
- `index`: `int`


## AttemptContainerDetailTypeDef

```python
from mypy_boto3_batch.type_defs import AttemptContainerDetailTypeDef
```




Optional fields:
- `containerInstanceArn`: `str`
- `taskArn`: `str`
- `exitCode`: `int`
- `reason`: `str`
- `logStreamName`: `str`
- `networkInterfaces`: `List["NetworkInterfaceTypeDef"]`


## AttemptDetailTypeDef

```python
from mypy_boto3_batch.type_defs import AttemptDetailTypeDef
```




Optional fields:
- `container`: `"AttemptContainerDetailTypeDef"`
- `startedAt`: `int`
- `stoppedAt`: `int`
- `statusReason`: `str`


## ComputeEnvironmentDetailTypeDef

```python
from mypy_boto3_batch.type_defs import ComputeEnvironmentDetailTypeDef
```


Required fields:
- `computeEnvironmentName`: `str`
- `computeEnvironmentArn`: `str`
- `ecsClusterArn`: `str`



Optional fields:
- `tags`: `Dict[str, str]`
- `type`: `CEType`
- `state`: `CEState`
- `status`: `CEStatus`
- `statusReason`: `str`
- `computeResources`: `"ComputeResourceTypeDef"`
- `serviceRole`: `str`


## ComputeEnvironmentOrderTypeDef

```python
from mypy_boto3_batch.type_defs import ComputeEnvironmentOrderTypeDef
```


Required fields:
- `order`: `int`
- `computeEnvironment`: `str`




## ComputeResourceTypeDef

```python
from mypy_boto3_batch.type_defs import ComputeResourceTypeDef
```


Required fields:
- `type`: `CRType`
- `maxvCpus`: `int`
- `subnets`: `List[str]`



Optional fields:
- `allocationStrategy`: `CRAllocationStrategy`
- `minvCpus`: `int`
- `desiredvCpus`: `int`
- `instanceTypes`: `List[str]`
- `imageId`: `str`
- `securityGroupIds`: `List[str]`
- `ec2KeyPair`: `str`
- `instanceRole`: `str`
- `tags`: `Dict[str, str]`
- `placementGroup`: `str`
- `bidPercentage`: `int`
- `spotIamFleetRole`: `str`
- `launchTemplate`: `"LaunchTemplateSpecificationTypeDef"`
- `ec2Configuration`: `List["Ec2ConfigurationTypeDef"]`


## ContainerDetailTypeDef

```python
from mypy_boto3_batch.type_defs import ContainerDetailTypeDef
```




Optional fields:
- `image`: `str`
- `vcpus`: `int`
- `memory`: `int`
- `command`: `List[str]`
- `jobRoleArn`: `str`
- `executionRoleArn`: `str`
- `volumes`: `List["VolumeTypeDef"]`
- `environment`: `List["KeyValuePairTypeDef"]`
- `mountPoints`: `List["MountPointTypeDef"]`
- `readonlyRootFilesystem`: `bool`
- `ulimits`: `List["UlimitTypeDef"]`
- `privileged`: `bool`
- `user`: `str`
- `exitCode`: `int`
- `reason`: `str`
- `containerInstanceArn`: `str`
- `taskArn`: `str`
- `logStreamName`: `str`
- `instanceType`: `str`
- `networkInterfaces`: `List["NetworkInterfaceTypeDef"]`
- `resourceRequirements`: `List["ResourceRequirementTypeDef"]`
- `linuxParameters`: `"LinuxParametersTypeDef"`
- `logConfiguration`: `"LogConfigurationTypeDef"`
- `secrets`: `List["SecretTypeDef"]`
- `networkConfiguration`: `"NetworkConfigurationTypeDef"`
- `fargatePlatformConfiguration`: `"FargatePlatformConfigurationTypeDef"`


## ContainerOverridesTypeDef

```python
from mypy_boto3_batch.type_defs import ContainerOverridesTypeDef
```




Optional fields:
- `vcpus`: `int`
- `memory`: `int`
- `command`: `List[str]`
- `instanceType`: `str`
- `environment`: `List["KeyValuePairTypeDef"]`
- `resourceRequirements`: `List["ResourceRequirementTypeDef"]`


## ContainerPropertiesTypeDef

```python
from mypy_boto3_batch.type_defs import ContainerPropertiesTypeDef
```




Optional fields:
- `image`: `str`
- `vcpus`: `int`
- `memory`: `int`
- `command`: `List[str]`
- `jobRoleArn`: `str`
- `executionRoleArn`: `str`
- `volumes`: `List["VolumeTypeDef"]`
- `environment`: `List["KeyValuePairTypeDef"]`
- `mountPoints`: `List["MountPointTypeDef"]`
- `readonlyRootFilesystem`: `bool`
- `privileged`: `bool`
- `ulimits`: `List["UlimitTypeDef"]`
- `user`: `str`
- `instanceType`: `str`
- `resourceRequirements`: `List["ResourceRequirementTypeDef"]`
- `linuxParameters`: `"LinuxParametersTypeDef"`
- `logConfiguration`: `"LogConfigurationTypeDef"`
- `secrets`: `List["SecretTypeDef"]`
- `networkConfiguration`: `"NetworkConfigurationTypeDef"`
- `fargatePlatformConfiguration`: `"FargatePlatformConfigurationTypeDef"`


## ContainerSummaryTypeDef

```python
from mypy_boto3_batch.type_defs import ContainerSummaryTypeDef
```




Optional fields:
- `exitCode`: `int`
- `reason`: `str`


## DeviceTypeDef

```python
from mypy_boto3_batch.type_defs import DeviceTypeDef
```


Required fields:
- `hostPath`: `str`



Optional fields:
- `containerPath`: `str`
- `permissions`: `List[DeviceCgroupPermission]`


## EFSAuthorizationConfigTypeDef

```python
from mypy_boto3_batch.type_defs import EFSAuthorizationConfigTypeDef
```




Optional fields:
- `accessPointId`: `str`
- `iam`: `EFSAuthorizationConfigIAM`


## EFSVolumeConfigurationTypeDef

```python
from mypy_boto3_batch.type_defs import EFSVolumeConfigurationTypeDef
```


Required fields:
- `fileSystemId`: `str`



Optional fields:
- `rootDirectory`: `str`
- `transitEncryption`: `EFSTransitEncryption`
- `transitEncryptionPort`: `int`
- `authorizationConfig`: `"EFSAuthorizationConfigTypeDef"`


## Ec2ConfigurationTypeDef

```python
from mypy_boto3_batch.type_defs import Ec2ConfigurationTypeDef
```


Required fields:
- `imageType`: `str`



Optional fields:
- `imageIdOverride`: `str`


## EvaluateOnExitTypeDef

```python
from mypy_boto3_batch.type_defs import EvaluateOnExitTypeDef
```


Required fields:
- `action`: `RetryAction`



Optional fields:
- `onStatusReason`: `str`
- `onReason`: `str`
- `onExitCode`: `str`


## FargatePlatformConfigurationTypeDef

```python
from mypy_boto3_batch.type_defs import FargatePlatformConfigurationTypeDef
```




Optional fields:
- `platformVersion`: `str`


## HostTypeDef

```python
from mypy_boto3_batch.type_defs import HostTypeDef
```




Optional fields:
- `sourcePath`: `str`


## JobDefinitionTypeDef

```python
from mypy_boto3_batch.type_defs import JobDefinitionTypeDef
```


Required fields:
- `jobDefinitionName`: `str`
- `jobDefinitionArn`: `str`
- `revision`: `int`
- `type`: `str`



Optional fields:
- `status`: `str`
- `parameters`: `Dict[str, str]`
- `retryStrategy`: `"RetryStrategyTypeDef"`
- `containerProperties`: `"ContainerPropertiesTypeDef"`
- `timeout`: `"JobTimeoutTypeDef"`
- `nodeProperties`: `"NodePropertiesTypeDef"`
- `tags`: `Dict[str, str]`
- `propagateTags`: `bool`
- `platformCapabilities`: `List[PlatformCapability]`


## JobDependencyTypeDef

```python
from mypy_boto3_batch.type_defs import JobDependencyTypeDef
```




Optional fields:
- `jobId`: `str`
- `type`: `ArrayJobDependency`


## JobDetailTypeDef

```python
from mypy_boto3_batch.type_defs import JobDetailTypeDef
```


Required fields:
- `jobName`: `str`
- `jobId`: `str`
- `jobQueue`: `str`
- `status`: `JobStatus`
- `startedAt`: `int`
- `jobDefinition`: `str`



Optional fields:
- `jobArn`: `str`
- `attempts`: `List["AttemptDetailTypeDef"]`
- `statusReason`: `str`
- `createdAt`: `int`
- `retryStrategy`: `"RetryStrategyTypeDef"`
- `stoppedAt`: `int`
- `dependsOn`: `List["JobDependencyTypeDef"]`
- `parameters`: `Dict[str, str]`
- `container`: `"ContainerDetailTypeDef"`
- `nodeDetails`: `"NodeDetailsTypeDef"`
- `nodeProperties`: `"NodePropertiesTypeDef"`
- `arrayProperties`: `"ArrayPropertiesDetailTypeDef"`
- `timeout`: `"JobTimeoutTypeDef"`
- `tags`: `Dict[str, str]`
- `propagateTags`: `bool`
- `platformCapabilities`: `List[PlatformCapability]`


## JobQueueDetailTypeDef

```python
from mypy_boto3_batch.type_defs import JobQueueDetailTypeDef
```


Required fields:
- `jobQueueName`: `str`
- `jobQueueArn`: `str`
- `state`: `JQState`
- `priority`: `int`
- `computeEnvironmentOrder`: `List["ComputeEnvironmentOrderTypeDef"]`



Optional fields:
- `status`: `JQStatus`
- `statusReason`: `str`
- `tags`: `Dict[str, str]`


## JobSummaryTypeDef

```python
from mypy_boto3_batch.type_defs import JobSummaryTypeDef
```


Required fields:
- `jobId`: `str`
- `jobName`: `str`



Optional fields:
- `jobArn`: `str`
- `createdAt`: `int`
- `status`: `JobStatus`
- `statusReason`: `str`
- `startedAt`: `int`
- `stoppedAt`: `int`
- `container`: `"ContainerSummaryTypeDef"`
- `arrayProperties`: `"ArrayPropertiesSummaryTypeDef"`
- `nodeProperties`: `"NodePropertiesSummaryTypeDef"`


## JobTimeoutTypeDef

```python
from mypy_boto3_batch.type_defs import JobTimeoutTypeDef
```




Optional fields:
- `attemptDurationSeconds`: `int`


## KeyValuePairTypeDef

```python
from mypy_boto3_batch.type_defs import KeyValuePairTypeDef
```




Optional fields:
- `name`: `str`
- `value`: `str`


## LaunchTemplateSpecificationTypeDef

```python
from mypy_boto3_batch.type_defs import LaunchTemplateSpecificationTypeDef
```




Optional fields:
- `launchTemplateId`: `str`
- `launchTemplateName`: `str`
- `version`: `str`


## LinuxParametersTypeDef

```python
from mypy_boto3_batch.type_defs import LinuxParametersTypeDef
```




Optional fields:
- `devices`: `List["DeviceTypeDef"]`
- `initProcessEnabled`: `bool`
- `sharedMemorySize`: `int`
- `tmpfs`: `List["TmpfsTypeDef"]`
- `maxSwap`: `int`
- `swappiness`: `int`


## LogConfigurationTypeDef

```python
from mypy_boto3_batch.type_defs import LogConfigurationTypeDef
```


Required fields:
- `logDriver`: `LogDriver`



Optional fields:
- `options`: `Dict[str, str]`
- `secretOptions`: `List["SecretTypeDef"]`


## MountPointTypeDef

```python
from mypy_boto3_batch.type_defs import MountPointTypeDef
```




Optional fields:
- `containerPath`: `str`
- `readOnly`: `bool`
- `sourceVolume`: `str`


## NetworkConfigurationTypeDef

```python
from mypy_boto3_batch.type_defs import NetworkConfigurationTypeDef
```




Optional fields:
- `assignPublicIp`: `AssignPublicIp`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_batch.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `attachmentId`: `str`
- `ipv6Address`: `str`
- `privateIpv4Address`: `str`


## NodeDetailsTypeDef

```python
from mypy_boto3_batch.type_defs import NodeDetailsTypeDef
```




Optional fields:
- `nodeIndex`: `int`
- `isMainNode`: `bool`


## NodePropertiesSummaryTypeDef

```python
from mypy_boto3_batch.type_defs import NodePropertiesSummaryTypeDef
```




Optional fields:
- `isMainNode`: `bool`
- `numNodes`: `int`
- `nodeIndex`: `int`


## NodePropertiesTypeDef

```python
from mypy_boto3_batch.type_defs import NodePropertiesTypeDef
```


Required fields:
- `numNodes`: `int`
- `mainNode`: `int`
- `nodeRangeProperties`: `List["NodeRangePropertyTypeDef"]`




## NodePropertyOverrideTypeDef

```python
from mypy_boto3_batch.type_defs import NodePropertyOverrideTypeDef
```


Required fields:
- `targetNodes`: `str`



Optional fields:
- `containerOverrides`: `"ContainerOverridesTypeDef"`


## NodeRangePropertyTypeDef

```python
from mypy_boto3_batch.type_defs import NodeRangePropertyTypeDef
```


Required fields:
- `targetNodes`: `str`



Optional fields:
- `container`: `"ContainerPropertiesTypeDef"`


## ResourceRequirementTypeDef

```python
from mypy_boto3_batch.type_defs import ResourceRequirementTypeDef
```


Required fields:
- `value`: `str`
- `type`: `ResourceType`




## RetryStrategyTypeDef

```python
from mypy_boto3_batch.type_defs import RetryStrategyTypeDef
```




Optional fields:
- `attempts`: `int`
- `evaluateOnExit`: `List["EvaluateOnExitTypeDef"]`


## SecretTypeDef

```python
from mypy_boto3_batch.type_defs import SecretTypeDef
```


Required fields:
- `name`: `str`
- `valueFrom`: `str`




## TmpfsTypeDef

```python
from mypy_boto3_batch.type_defs import TmpfsTypeDef
```


Required fields:
- `containerPath`: `str`
- `size`: `int`



Optional fields:
- `mountOptions`: `List[str]`


## UlimitTypeDef

```python
from mypy_boto3_batch.type_defs import UlimitTypeDef
```


Required fields:
- `hardLimit`: `int`
- `name`: `str`
- `softLimit`: `int`




## VolumeTypeDef

```python
from mypy_boto3_batch.type_defs import VolumeTypeDef
```




Optional fields:
- `host`: `"HostTypeDef"`
- `name`: `str`
- `efsVolumeConfiguration`: `"EFSVolumeConfigurationTypeDef"`


## ArrayPropertiesTypeDef

```python
from mypy_boto3_batch.type_defs import ArrayPropertiesTypeDef
```




Optional fields:
- `size`: `int`


## ComputeResourceUpdateTypeDef

```python
from mypy_boto3_batch.type_defs import ComputeResourceUpdateTypeDef
```




Optional fields:
- `minvCpus`: `int`
- `maxvCpus`: `int`
- `desiredvCpus`: `int`
- `subnets`: `List[str]`
- `securityGroupIds`: `List[str]`


## CreateComputeEnvironmentResponseTypeDef

```python
from mypy_boto3_batch.type_defs import CreateComputeEnvironmentResponseTypeDef
```




Optional fields:
- `computeEnvironmentName`: `str`
- `computeEnvironmentArn`: `str`


## CreateJobQueueResponseTypeDef

```python
from mypy_boto3_batch.type_defs import CreateJobQueueResponseTypeDef
```


Required fields:
- `jobQueueName`: `str`
- `jobQueueArn`: `str`




## DescribeComputeEnvironmentsResponseTypeDef

```python
from mypy_boto3_batch.type_defs import DescribeComputeEnvironmentsResponseTypeDef
```




Optional fields:
- `computeEnvironments`: `List["ComputeEnvironmentDetailTypeDef"]`
- `nextToken`: `str`


## DescribeJobDefinitionsResponseTypeDef

```python
from mypy_boto3_batch.type_defs import DescribeJobDefinitionsResponseTypeDef
```




Optional fields:
- `jobDefinitions`: `List["JobDefinitionTypeDef"]`
- `nextToken`: `str`


## DescribeJobQueuesResponseTypeDef

```python
from mypy_boto3_batch.type_defs import DescribeJobQueuesResponseTypeDef
```




Optional fields:
- `jobQueues`: `List["JobQueueDetailTypeDef"]`
- `nextToken`: `str`


## DescribeJobsResponseTypeDef

```python
from mypy_boto3_batch.type_defs import DescribeJobsResponseTypeDef
```




Optional fields:
- `jobs`: `List["JobDetailTypeDef"]`


## ListJobsResponseTypeDef

```python
from mypy_boto3_batch.type_defs import ListJobsResponseTypeDef
```


Required fields:
- `jobSummaryList`: `List["JobSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_batch.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## NodeOverridesTypeDef

```python
from mypy_boto3_batch.type_defs import NodeOverridesTypeDef
```




Optional fields:
- `numNodes`: `int`
- `nodePropertyOverrides`: `List["NodePropertyOverrideTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_batch.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RegisterJobDefinitionResponseTypeDef

```python
from mypy_boto3_batch.type_defs import RegisterJobDefinitionResponseTypeDef
```


Required fields:
- `jobDefinitionName`: `str`
- `jobDefinitionArn`: `str`
- `revision`: `int`




## SubmitJobResponseTypeDef

```python
from mypy_boto3_batch.type_defs import SubmitJobResponseTypeDef
```


Required fields:
- `jobName`: `str`
- `jobId`: `str`



Optional fields:
- `jobArn`: `str`


## UpdateComputeEnvironmentResponseTypeDef

```python
from mypy_boto3_batch.type_defs import UpdateComputeEnvironmentResponseTypeDef
```




Optional fields:
- `computeEnvironmentName`: `str`
- `computeEnvironmentArn`: `str`


## UpdateJobQueueResponseTypeDef

```python
from mypy_boto3_batch.type_defs import UpdateJobQueueResponseTypeDef
```




Optional fields:
- `jobQueueName`: `str`
- `jobQueueArn`: `str`

