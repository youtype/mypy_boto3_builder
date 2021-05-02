# Structures for boto3 mgn module

> [Index](../index.md) > [mgn](./index.md) > Structures

Auto-generated documentation for [mgn](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn)
type annotations stubs module [mypy_boto3_mgn](https://pypi.org/project/mypy-boto3-mgn/).

- [Structures for boto3 mgn module](#structures-for-boto3-mgn-module)
  - [CPUTypeDef](#cputypedef)
  - [DataReplicationErrorTypeDef](#datareplicationerrortypedef)
  - [DataReplicationInfoReplicatedDiskTypeDef](#datareplicationinforeplicateddisktypedef)
  - [DataReplicationInfoTypeDef](#datareplicationinfotypedef)
  - [DataReplicationInitiationStepTypeDef](#datareplicationinitiationsteptypedef)
  - [DataReplicationInitiationTypeDef](#datareplicationinitiationtypedef)
  - [DiskTypeDef](#disktypedef)
  - [IdentificationHintsTypeDef](#identificationhintstypedef)
  - [JobLogEventDataTypeDef](#joblogeventdatatypedef)
  - [JobLogTypeDef](#joblogtypedef)
  - [JobTypeDef](#jobtypedef)
  - [LaunchedInstanceTypeDef](#launchedinstancetypedef)
  - [LicensingTypeDef](#licensingtypedef)
  - [LifeCycleLastCutoverFinalizedTypeDef](#lifecyclelastcutoverfinalizedtypedef)
  - [LifeCycleLastCutoverInitiatedTypeDef](#lifecyclelastcutoverinitiatedtypedef)
  - [LifeCycleLastCutoverRevertedTypeDef](#lifecyclelastcutoverrevertedtypedef)
  - [LifeCycleLastCutoverTypeDef](#lifecyclelastcutovertypedef)
  - [LifeCycleLastTestFinalizedTypeDef](#lifecyclelasttestfinalizedtypedef)
  - [LifeCycleLastTestInitiatedTypeDef](#lifecyclelasttestinitiatedtypedef)
  - [LifeCycleLastTestRevertedTypeDef](#lifecyclelasttestrevertedtypedef)
  - [LifeCycleLastTestTypeDef](#lifecyclelasttesttypedef)
  - [LifeCycleTypeDef](#lifecycletypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [OSTypeDef](#ostypedef)
  - [ParticipatingServerTypeDef](#participatingservertypedef)
  - [ReplicationConfigurationReplicatedDiskTypeDef](#replicationconfigurationreplicateddisktypedef)
  - [ReplicationConfigurationTemplateTypeDef](#replicationconfigurationtemplatetypedef)
  - [SourcePropertiesTypeDef](#sourcepropertiestypedef)
  - [SourceServerTypeDef](#sourceservertypedef)
  - [ChangeServerLifeCycleStateSourceServerLifecycleTypeDef](#changeserverlifecyclestatesourceserverlifecycletypedef)
  - [DescribeJobLogItemsResponseTypeDef](#describejoblogitemsresponsetypedef)
  - [DescribeJobsRequestFiltersTypeDef](#describejobsrequestfilterstypedef)
  - [DescribeJobsResponseTypeDef](#describejobsresponsetypedef)
  - [DescribeReplicationConfigurationTemplatesResponseTypeDef](#describereplicationconfigurationtemplatesresponsetypedef)
  - [DescribeSourceServersRequestFiltersTypeDef](#describesourceserversrequestfilterstypedef)
  - [DescribeSourceServersResponseTypeDef](#describesourceserversresponsetypedef)
  - [LaunchConfigurationTypeDef](#launchconfigurationtypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ReplicationConfigurationTypeDef](#replicationconfigurationtypedef)
  - [StartCutoverResponseTypeDef](#startcutoverresponsetypedef)
  - [StartTestResponseTypeDef](#starttestresponsetypedef)
  - [TerminateTargetInstancesResponseTypeDef](#terminatetargetinstancesresponsetypedef)

## CPUTypeDef

```python
from mypy_boto3_mgn.type_defs import CPUTypeDef
```




Optional fields:
- `cores`: `int`
- `modelName`: `str`


## DataReplicationErrorTypeDef

```python
from mypy_boto3_mgn.type_defs import DataReplicationErrorTypeDef
```




Optional fields:
- `error`: `DataReplicationErrorString`
- `rawError`: `str`


## DataReplicationInfoReplicatedDiskTypeDef

```python
from mypy_boto3_mgn.type_defs import DataReplicationInfoReplicatedDiskTypeDef
```




Optional fields:
- `backloggedStorageBytes`: `int`
- `deviceName`: `str`
- `replicatedStorageBytes`: `int`
- `rescannedStorageBytes`: `int`
- `totalStorageBytes`: `int`


## DataReplicationInfoTypeDef

```python
from mypy_boto3_mgn.type_defs import DataReplicationInfoTypeDef
```




Optional fields:
- `dataReplicationError`: `"DataReplicationErrorTypeDef"`
- `dataReplicationInitiation`: `"DataReplicationInitiationTypeDef"`
- `dataReplicationState`: `DataReplicationState`
- `etaDateTime`: `str`
- `lagDuration`: `str`
- `replicatedDisks`: `List["DataReplicationInfoReplicatedDiskTypeDef"]`


## DataReplicationInitiationStepTypeDef

```python
from mypy_boto3_mgn.type_defs import DataReplicationInitiationStepTypeDef
```




Optional fields:
- `name`: `DataReplicationInitiationStepName`
- `status`: `DataReplicationInitiationStepStatus`


## DataReplicationInitiationTypeDef

```python
from mypy_boto3_mgn.type_defs import DataReplicationInitiationTypeDef
```




Optional fields:
- `nextAttemptDateTime`: `str`
- `startDateTime`: `str`
- `steps`: `List["DataReplicationInitiationStepTypeDef"]`


## DiskTypeDef

```python
from mypy_boto3_mgn.type_defs import DiskTypeDef
```




Optional fields:
- `bytes`: `int`
- `deviceName`: `str`


## IdentificationHintsTypeDef

```python
from mypy_boto3_mgn.type_defs import IdentificationHintsTypeDef
```




Optional fields:
- `awsInstanceID`: `str`
- `fqdn`: `str`
- `hostname`: `str`
- `vmWareUuid`: `str`


## JobLogEventDataTypeDef

```python
from mypy_boto3_mgn.type_defs import JobLogEventDataTypeDef
```




Optional fields:
- `conversionServerID`: `str`
- `rawError`: `str`
- `sourceServerID`: `str`
- `targetInstanceID`: `str`


## JobLogTypeDef

```python
from mypy_boto3_mgn.type_defs import JobLogTypeDef
```




Optional fields:
- `event`: `JobLogEvent`
- `eventData`: `"JobLogEventDataTypeDef"`
- `logDateTime`: `str`


## JobTypeDef

```python
from mypy_boto3_mgn.type_defs import JobTypeDef
```


Required fields:
- `jobID`: `str`



Optional fields:
- `arn`: `str`
- `creationDateTime`: `str`
- `endDateTime`: `str`
- `initiatedBy`: `InitiatedBy`
- `participatingServers`: `List["ParticipatingServerTypeDef"]`
- `status`: `JobStatus`
- `tags`: `Dict[str, str]`
- `type`: `JobType`


## LaunchedInstanceTypeDef

```python
from mypy_boto3_mgn.type_defs import LaunchedInstanceTypeDef
```




Optional fields:
- `ec2InstanceID`: `str`
- `firstBoot`: `FirstBoot`
- `jobID`: `str`


## LicensingTypeDef

```python
from mypy_boto3_mgn.type_defs import LicensingTypeDef
```




Optional fields:
- `osByol`: `bool`


## LifeCycleLastCutoverFinalizedTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastCutoverFinalizedTypeDef
```




Optional fields:
- `apiCallDateTime`: `str`


## LifeCycleLastCutoverInitiatedTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastCutoverInitiatedTypeDef
```




Optional fields:
- `apiCallDateTime`: `str`
- `jobID`: `str`


## LifeCycleLastCutoverRevertedTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastCutoverRevertedTypeDef
```




Optional fields:
- `apiCallDateTime`: `str`


## LifeCycleLastCutoverTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastCutoverTypeDef
```




Optional fields:
- `finalized`: `"LifeCycleLastCutoverFinalizedTypeDef"`
- `initiated`: `"LifeCycleLastCutoverInitiatedTypeDef"`
- `reverted`: `"LifeCycleLastCutoverRevertedTypeDef"`


## LifeCycleLastTestFinalizedTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastTestFinalizedTypeDef
```




Optional fields:
- `apiCallDateTime`: `str`


## LifeCycleLastTestInitiatedTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastTestInitiatedTypeDef
```




Optional fields:
- `apiCallDateTime`: `str`
- `jobID`: `str`


## LifeCycleLastTestRevertedTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastTestRevertedTypeDef
```




Optional fields:
- `apiCallDateTime`: `str`


## LifeCycleLastTestTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleLastTestTypeDef
```




Optional fields:
- `finalized`: `"LifeCycleLastTestFinalizedTypeDef"`
- `initiated`: `"LifeCycleLastTestInitiatedTypeDef"`
- `reverted`: `"LifeCycleLastTestRevertedTypeDef"`


## LifeCycleTypeDef

```python
from mypy_boto3_mgn.type_defs import LifeCycleTypeDef
```




Optional fields:
- `addedToServiceDateTime`: `str`
- `elapsedReplicationDuration`: `str`
- `firstByteDateTime`: `str`
- `lastCutover`: `"LifeCycleLastCutoverTypeDef"`
- `lastSeenByServiceDateTime`: `str`
- `lastTest`: `"LifeCycleLastTestTypeDef"`
- `state`: `LifeCycleState`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_mgn.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `ips`: `List[str]`
- `isPrimary`: `bool`
- `macAddress`: `str`


## OSTypeDef

```python
from mypy_boto3_mgn.type_defs import OSTypeDef
```




Optional fields:
- `fullString`: `str`


## ParticipatingServerTypeDef

```python
from mypy_boto3_mgn.type_defs import ParticipatingServerTypeDef
```




Optional fields:
- `launchStatus`: `LaunchStatus`
- `sourceServerID`: `str`


## ReplicationConfigurationReplicatedDiskTypeDef

```python
from mypy_boto3_mgn.type_defs import ReplicationConfigurationReplicatedDiskTypeDef
```




Optional fields:
- `deviceName`: `str`
- `iops`: `int`
- `isBootDisk`: `bool`
- `stagingDiskType`: `ReplicationConfigurationReplicatedDiskStagingDiskType`


## ReplicationConfigurationTemplateTypeDef

```python
from mypy_boto3_mgn.type_defs import ReplicationConfigurationTemplateTypeDef
```


Required fields:
- `replicationConfigurationTemplateID`: `str`



Optional fields:
- `arn`: `str`
- `associateDefaultSecurityGroup`: `bool`
- `bandwidthThrottling`: `int`
- `createPublicIP`: `bool`
- `dataPlaneRouting`: `ReplicationConfigurationDataPlaneRouting`
- `defaultLargeStagingDiskType`: `ReplicationConfigurationDefaultLargeStagingDiskType`
- `ebsEncryption`: `ReplicationConfigurationEbsEncryption`
- `ebsEncryptionKeyArn`: `str`
- `replicationServerInstanceType`: `str`
- `replicationServersSecurityGroupsIDs`: `List[str]`
- `stagingAreaSubnetId`: `str`
- `stagingAreaTags`: `Dict[str, str]`
- `tags`: `Dict[str, str]`
- `useDedicatedReplicationServer`: `bool`


## SourcePropertiesTypeDef

```python
from mypy_boto3_mgn.type_defs import SourcePropertiesTypeDef
```




Optional fields:
- `cpus`: `List["CPUTypeDef"]`
- `disks`: `List["DiskTypeDef"]`
- `identificationHints`: `"IdentificationHintsTypeDef"`
- `lastUpdatedDateTime`: `str`
- `networkInterfaces`: `List["NetworkInterfaceTypeDef"]`
- `os`: `"OSTypeDef"`
- `ramBytes`: `int`
- `recommendedInstanceType`: `str`


## SourceServerTypeDef

```python
from mypy_boto3_mgn.type_defs import SourceServerTypeDef
```




Optional fields:
- `arn`: `str`
- `dataReplicationInfo`: `"DataReplicationInfoTypeDef"`
- `isArchived`: `bool`
- `launchedInstance`: `"LaunchedInstanceTypeDef"`
- `lifeCycle`: `"LifeCycleTypeDef"`
- `sourceProperties`: `"SourcePropertiesTypeDef"`
- `sourceServerID`: `str`
- `tags`: `Dict[str, str]`


## ChangeServerLifeCycleStateSourceServerLifecycleTypeDef

```python
from mypy_boto3_mgn.type_defs import ChangeServerLifeCycleStateSourceServerLifecycleTypeDef
```


Required fields:
- `state`: `ChangeServerLifeCycleStateSourceServerLifecycleState`




## DescribeJobLogItemsResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import DescribeJobLogItemsResponseTypeDef
```




Optional fields:
- `items`: `List["JobLogTypeDef"]`
- `nextToken`: `str`


## DescribeJobsRequestFiltersTypeDef

```python
from mypy_boto3_mgn.type_defs import DescribeJobsRequestFiltersTypeDef
```




Optional fields:
- `fromDate`: `str`
- `jobIDs`: `List[str]`
- `toDate`: `str`


## DescribeJobsResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import DescribeJobsResponseTypeDef
```




Optional fields:
- `items`: `List["JobTypeDef"]`
- `nextToken`: `str`


## DescribeReplicationConfigurationTemplatesResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import DescribeReplicationConfigurationTemplatesResponseTypeDef
```




Optional fields:
- `items`: `List["ReplicationConfigurationTemplateTypeDef"]`
- `nextToken`: `str`


## DescribeSourceServersRequestFiltersTypeDef

```python
from mypy_boto3_mgn.type_defs import DescribeSourceServersRequestFiltersTypeDef
```




Optional fields:
- `isArchived`: `bool`
- `sourceServerIDs`: `List[str]`


## DescribeSourceServersResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import DescribeSourceServersResponseTypeDef
```




Optional fields:
- `items`: `List["SourceServerTypeDef"]`
- `nextToken`: `str`


## LaunchConfigurationTypeDef

```python
from mypy_boto3_mgn.type_defs import LaunchConfigurationTypeDef
```




Optional fields:
- `copyPrivateIp`: `bool`
- `copyTags`: `bool`
- `ec2LaunchTemplateID`: `str`
- `launchDisposition`: `LaunchDisposition`
- `licensing`: `"LicensingTypeDef"`
- `name`: `str`
- `sourceServerID`: `str`
- `targetInstanceTypeRightSizingMethod`: `TargetInstanceTypeRightSizingMethod`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mgn.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ReplicationConfigurationTypeDef

```python
from mypy_boto3_mgn.type_defs import ReplicationConfigurationTypeDef
```




Optional fields:
- `associateDefaultSecurityGroup`: `bool`
- `bandwidthThrottling`: `int`
- `createPublicIP`: `bool`
- `dataPlaneRouting`: `ReplicationConfigurationDataPlaneRouting`
- `defaultLargeStagingDiskType`: `ReplicationConfigurationDefaultLargeStagingDiskType`
- `ebsEncryption`: `ReplicationConfigurationEbsEncryption`
- `ebsEncryptionKeyArn`: `str`
- `name`: `str`
- `replicatedDisks`: `List["ReplicationConfigurationReplicatedDiskTypeDef"]`
- `replicationServerInstanceType`: `str`
- `replicationServersSecurityGroupsIDs`: `List[str]`
- `sourceServerID`: `str`
- `stagingAreaSubnetId`: `str`
- `stagingAreaTags`: `Dict[str, str]`
- `useDedicatedReplicationServer`: `bool`


## StartCutoverResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import StartCutoverResponseTypeDef
```




Optional fields:
- `job`: `"JobTypeDef"`


## StartTestResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import StartTestResponseTypeDef
```




Optional fields:
- `job`: `"JobTypeDef"`


## TerminateTargetInstancesResponseTypeDef

```python
from mypy_boto3_mgn.type_defs import TerminateTargetInstancesResponseTypeDef
```




Optional fields:
- `job`: `"JobTypeDef"`

