# Structures for boto3 EMRContainers module

> [Index](../index.md) > [EMRContainers](./index.md) > Structures

Auto-generated documentation for [EMRContainers](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers)
type annotations stubs module [mypy_boto3_emr_containers](https://pypi.org/project/mypy-boto3-emr-containers/).

- [Structures for boto3 EMRContainers module](#structures-for-boto3-emrcontainers-module)
  - [CancelJobRunResponseTypeDef](#canceljobrunresponsetypedef)
  - [CloudWatchMonitoringConfigurationTypeDef](#cloudwatchmonitoringconfigurationtypedef)
  - [ConfigurationOverridesTypeDef](#configurationoverridestypedef)
  - [ConfigurationTypeDef](#configurationtypedef)
  - [ContainerInfoTypeDef](#containerinfotypedef)
  - [ContainerProviderTypeDef](#containerprovidertypedef)
  - [CreateManagedEndpointResponseTypeDef](#createmanagedendpointresponsetypedef)
  - [CreateVirtualClusterResponseTypeDef](#createvirtualclusterresponsetypedef)
  - [DeleteManagedEndpointResponseTypeDef](#deletemanagedendpointresponsetypedef)
  - [DeleteVirtualClusterResponseTypeDef](#deletevirtualclusterresponsetypedef)
  - [DescribeJobRunResponseTypeDef](#describejobrunresponsetypedef)
  - [DescribeManagedEndpointResponseTypeDef](#describemanagedendpointresponsetypedef)
  - [DescribeVirtualClusterResponseTypeDef](#describevirtualclusterresponsetypedef)
  - [EksInfoTypeDef](#eksinfotypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [JobDriverTypeDef](#jobdrivertypedef)
  - [JobRunTypeDef](#jobruntypedef)
  - [ListJobRunsResponseTypeDef](#listjobrunsresponsetypedef)
  - [ListManagedEndpointsResponseTypeDef](#listmanagedendpointsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListVirtualClustersResponseTypeDef](#listvirtualclustersresponsetypedef)
  - [MonitoringConfigurationTypeDef](#monitoringconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [S3MonitoringConfigurationTypeDef](#s3monitoringconfigurationtypedef)
  - [SparkSubmitJobDriverTypeDef](#sparksubmitjobdrivertypedef)
  - [StartJobRunResponseTypeDef](#startjobrunresponsetypedef)
  - [VirtualClusterTypeDef](#virtualclustertypedef)

## CancelJobRunResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import CancelJobRunResponseTypeDef
```




Optional fields:
- `id`: `str`
- `virtualClusterId`: `str`


## CloudWatchMonitoringConfigurationTypeDef

```python
from mypy_boto3_emr_containers.type_defs import CloudWatchMonitoringConfigurationTypeDef
```


Required fields:
- `logGroupName`: `str`



Optional fields:
- `logStreamNamePrefix`: `str`


## ConfigurationOverridesTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ConfigurationOverridesTypeDef
```




Optional fields:
- `applicationConfiguration`: `List[Dict[str, Any]]`
- `monitoringConfiguration`: `"MonitoringConfigurationTypeDef"`


## ConfigurationTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ConfigurationTypeDef
```


Required fields:
- `classification`: `str`



Optional fields:
- `properties`: `Dict[str, str]`
- `configurations`: `List[Dict[str, Any]]`


## ContainerInfoTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ContainerInfoTypeDef
```




Optional fields:
- `eksInfo`: `"EksInfoTypeDef"`


## ContainerProviderTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ContainerProviderTypeDef
```


Required fields:
- `type`: `Literal['EKS']`
- `id`: `str`



Optional fields:
- `info`: `"ContainerInfoTypeDef"`


## CreateManagedEndpointResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import CreateManagedEndpointResponseTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `arn`: `str`
- `virtualClusterId`: `str`


## CreateVirtualClusterResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import CreateVirtualClusterResponseTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `arn`: `str`


## DeleteManagedEndpointResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import DeleteManagedEndpointResponseTypeDef
```




Optional fields:
- `id`: `str`
- `virtualClusterId`: `str`


## DeleteVirtualClusterResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import DeleteVirtualClusterResponseTypeDef
```




Optional fields:
- `id`: `str`


## DescribeJobRunResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import DescribeJobRunResponseTypeDef
```




Optional fields:
- `jobRun`: `"JobRunTypeDef"`


## DescribeManagedEndpointResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import DescribeManagedEndpointResponseTypeDef
```




Optional fields:
- `endpoint`: `"EndpointTypeDef"`


## DescribeVirtualClusterResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import DescribeVirtualClusterResponseTypeDef
```




Optional fields:
- `virtualCluster`: `"VirtualClusterTypeDef"`


## EksInfoTypeDef

```python
from mypy_boto3_emr_containers.type_defs import EksInfoTypeDef
```




Optional fields:
- `namespace`: `str`


## EndpointTypeDef

```python
from mypy_boto3_emr_containers.type_defs import EndpointTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `arn`: `str`
- `virtualClusterId`: `str`
- `type`: `str`
- `state`: `EndpointState`
- `releaseLabel`: `str`
- `executionRoleArn`: `str`
- `certificateArn`: `str`
- `configurationOverrides`: `"ConfigurationOverridesTypeDef"`
- `serverUrl`: `str`
- `createdAt`: `datetime`
- `securityGroup`: `str`
- `subnetIds`: `List[str]`
- `tags`: `Dict[str, str]`


## JobDriverTypeDef

```python
from mypy_boto3_emr_containers.type_defs import JobDriverTypeDef
```




Optional fields:
- `sparkSubmitJobDriver`: `"SparkSubmitJobDriverTypeDef"`


## JobRunTypeDef

```python
from mypy_boto3_emr_containers.type_defs import JobRunTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `virtualClusterId`: `str`
- `arn`: `str`
- `state`: `JobRunState`
- `clientToken`: `str`
- `executionRoleArn`: `str`
- `releaseLabel`: `str`
- `configurationOverrides`: `"ConfigurationOverridesTypeDef"`
- `jobDriver`: `"JobDriverTypeDef"`
- `createdAt`: `datetime`
- `createdBy`: `str`
- `finishedAt`: `datetime`
- `stateDetails`: `str`
- `failureReason`: `FailureReason`
- `tags`: `Dict[str, str]`


## ListJobRunsResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ListJobRunsResponseTypeDef
```




Optional fields:
- `jobRuns`: `List["JobRunTypeDef"]`
- `nextToken`: `str`


## ListManagedEndpointsResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ListManagedEndpointsResponseTypeDef
```




Optional fields:
- `endpoints`: `List["EndpointTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListVirtualClustersResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import ListVirtualClustersResponseTypeDef
```




Optional fields:
- `virtualClusters`: `List["VirtualClusterTypeDef"]`
- `nextToken`: `str`


## MonitoringConfigurationTypeDef

```python
from mypy_boto3_emr_containers.type_defs import MonitoringConfigurationTypeDef
```




Optional fields:
- `persistentAppUI`: `PersistentAppUI`
- `cloudWatchMonitoringConfiguration`: `"CloudWatchMonitoringConfigurationTypeDef"`
- `s3MonitoringConfiguration`: `"S3MonitoringConfigurationTypeDef"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_emr_containers.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## S3MonitoringConfigurationTypeDef

```python
from mypy_boto3_emr_containers.type_defs import S3MonitoringConfigurationTypeDef
```


Required fields:
- `logUri`: `str`




## SparkSubmitJobDriverTypeDef

```python
from mypy_boto3_emr_containers.type_defs import SparkSubmitJobDriverTypeDef
```


Required fields:
- `entryPoint`: `str`



Optional fields:
- `entryPointArguments`: `List[str]`
- `sparkSubmitParameters`: `str`


## StartJobRunResponseTypeDef

```python
from mypy_boto3_emr_containers.type_defs import StartJobRunResponseTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `arn`: `str`
- `virtualClusterId`: `str`


## VirtualClusterTypeDef

```python
from mypy_boto3_emr_containers.type_defs import VirtualClusterTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `arn`: `str`
- `state`: `VirtualClusterState`
- `containerProvider`: `"ContainerProviderTypeDef"`
- `createdAt`: `datetime`
- `tags`: `Dict[str, str]`

