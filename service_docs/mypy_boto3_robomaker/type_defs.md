# Structures for boto3 RoboMaker module

> [Index](../index.md) > [RoboMaker](./index.md) > Structures

Auto-generated documentation for [RoboMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker)
type annotations stubs module [mypy_boto3_robomaker](https://pypi.org/project/mypy-boto3-robomaker/).

- [Structures for boto3 RoboMaker module](#structures-for-boto3-robomaker-module)
  - [BatchDeleteWorldsResponseTypeDef](#batchdeleteworldsresponsetypedef)
  - [BatchDescribeSimulationJobResponseTypeDef](#batchdescribesimulationjobresponsetypedef)
  - [BatchPolicyTypeDef](#batchpolicytypedef)
  - [ComputeResponseTypeDef](#computeresponsetypedef)
  - [ComputeTypeDef](#computetypedef)
  - [CreateDeploymentJobResponseTypeDef](#createdeploymentjobresponsetypedef)
  - [CreateFleetResponseTypeDef](#createfleetresponsetypedef)
  - [CreateRobotApplicationResponseTypeDef](#createrobotapplicationresponsetypedef)
  - [CreateRobotApplicationVersionResponseTypeDef](#createrobotapplicationversionresponsetypedef)
  - [CreateRobotResponseTypeDef](#createrobotresponsetypedef)
  - [CreateSimulationApplicationResponseTypeDef](#createsimulationapplicationresponsetypedef)
  - [CreateSimulationApplicationVersionResponseTypeDef](#createsimulationapplicationversionresponsetypedef)
  - [CreateSimulationJobResponseTypeDef](#createsimulationjobresponsetypedef)
  - [CreateWorldExportJobResponseTypeDef](#createworldexportjobresponsetypedef)
  - [CreateWorldGenerationJobResponseTypeDef](#createworldgenerationjobresponsetypedef)
  - [CreateWorldTemplateResponseTypeDef](#createworldtemplateresponsetypedef)
  - [DataSourceConfigTypeDef](#datasourceconfigtypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [DeploymentApplicationConfigTypeDef](#deploymentapplicationconfigtypedef)
  - [DeploymentConfigTypeDef](#deploymentconfigtypedef)
  - [DeploymentJobTypeDef](#deploymentjobtypedef)
  - [DeploymentLaunchConfigTypeDef](#deploymentlaunchconfigtypedef)
  - [DeregisterRobotResponseTypeDef](#deregisterrobotresponsetypedef)
  - [DescribeDeploymentJobResponseTypeDef](#describedeploymentjobresponsetypedef)
  - [DescribeFleetResponseTypeDef](#describefleetresponsetypedef)
  - [DescribeRobotApplicationResponseTypeDef](#describerobotapplicationresponsetypedef)
  - [DescribeRobotResponseTypeDef](#describerobotresponsetypedef)
  - [DescribeSimulationApplicationResponseTypeDef](#describesimulationapplicationresponsetypedef)
  - [DescribeSimulationJobBatchResponseTypeDef](#describesimulationjobbatchresponsetypedef)
  - [DescribeSimulationJobResponseTypeDef](#describesimulationjobresponsetypedef)
  - [DescribeWorldExportJobResponseTypeDef](#describeworldexportjobresponsetypedef)
  - [DescribeWorldGenerationJobResponseTypeDef](#describeworldgenerationjobresponsetypedef)
  - [DescribeWorldResponseTypeDef](#describeworldresponsetypedef)
  - [DescribeWorldTemplateResponseTypeDef](#describeworldtemplateresponsetypedef)
  - [FailedCreateSimulationJobRequestTypeDef](#failedcreatesimulationjobrequesttypedef)
  - [FailureSummaryTypeDef](#failuresummarytypedef)
  - [FilterTypeDef](#filtertypedef)
  - [FinishedWorldsSummaryTypeDef](#finishedworldssummarytypedef)
  - [FleetTypeDef](#fleettypedef)
  - [GetWorldTemplateBodyResponseTypeDef](#getworldtemplatebodyresponsetypedef)
  - [LaunchConfigTypeDef](#launchconfigtypedef)
  - [ListDeploymentJobsResponseTypeDef](#listdeploymentjobsresponsetypedef)
  - [ListFleetsResponseTypeDef](#listfleetsresponsetypedef)
  - [ListRobotApplicationsResponseTypeDef](#listrobotapplicationsresponsetypedef)
  - [ListRobotsResponseTypeDef](#listrobotsresponsetypedef)
  - [ListSimulationApplicationsResponseTypeDef](#listsimulationapplicationsresponsetypedef)
  - [ListSimulationJobBatchesResponseTypeDef](#listsimulationjobbatchesresponsetypedef)
  - [ListSimulationJobsResponseTypeDef](#listsimulationjobsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListWorldExportJobsResponseTypeDef](#listworldexportjobsresponsetypedef)
  - [ListWorldGenerationJobsResponseTypeDef](#listworldgenerationjobsresponsetypedef)
  - [ListWorldTemplatesResponseTypeDef](#listworldtemplatesresponsetypedef)
  - [ListWorldsResponseTypeDef](#listworldsresponsetypedef)
  - [LoggingConfigTypeDef](#loggingconfigtypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [OutputLocationTypeDef](#outputlocationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PortForwardingConfigTypeDef](#portforwardingconfigtypedef)
  - [PortMappingTypeDef](#portmappingtypedef)
  - [ProgressDetailTypeDef](#progressdetailtypedef)
  - [RegisterRobotResponseTypeDef](#registerrobotresponsetypedef)
  - [RenderingEngineTypeDef](#renderingenginetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RobotApplicationConfigTypeDef](#robotapplicationconfigtypedef)
  - [RobotApplicationSummaryTypeDef](#robotapplicationsummarytypedef)
  - [RobotDeploymentTypeDef](#robotdeploymenttypedef)
  - [RobotSoftwareSuiteTypeDef](#robotsoftwaresuitetypedef)
  - [RobotTypeDef](#robottypedef)
  - [S3KeyOutputTypeDef](#s3keyoutputtypedef)
  - [S3ObjectTypeDef](#s3objecttypedef)
  - [SimulationApplicationConfigTypeDef](#simulationapplicationconfigtypedef)
  - [SimulationApplicationSummaryTypeDef](#simulationapplicationsummarytypedef)
  - [SimulationJobBatchSummaryTypeDef](#simulationjobbatchsummarytypedef)
  - [SimulationJobRequestTypeDef](#simulationjobrequesttypedef)
  - [SimulationJobSummaryTypeDef](#simulationjobsummarytypedef)
  - [SimulationJobTypeDef](#simulationjobtypedef)
  - [SimulationSoftwareSuiteTypeDef](#simulationsoftwaresuitetypedef)
  - [SourceConfigTypeDef](#sourceconfigtypedef)
  - [SourceTypeDef](#sourcetypedef)
  - [StartSimulationJobBatchResponseTypeDef](#startsimulationjobbatchresponsetypedef)
  - [SyncDeploymentJobResponseTypeDef](#syncdeploymentjobresponsetypedef)
  - [TemplateLocationTypeDef](#templatelocationtypedef)
  - [TemplateSummaryTypeDef](#templatesummarytypedef)
  - [ToolTypeDef](#tooltypedef)
  - [UpdateRobotApplicationResponseTypeDef](#updaterobotapplicationresponsetypedef)
  - [UpdateSimulationApplicationResponseTypeDef](#updatesimulationapplicationresponsetypedef)
  - [UpdateWorldTemplateResponseTypeDef](#updateworldtemplateresponsetypedef)
  - [UploadConfigurationTypeDef](#uploadconfigurationtypedef)
  - [VPCConfigResponseTypeDef](#vpcconfigresponsetypedef)
  - [VPCConfigTypeDef](#vpcconfigtypedef)
  - [WorldConfigTypeDef](#worldconfigtypedef)
  - [WorldCountTypeDef](#worldcounttypedef)
  - [WorldExportJobSummaryTypeDef](#worldexportjobsummarytypedef)
  - [WorldFailureTypeDef](#worldfailuretypedef)
  - [WorldGenerationJobSummaryTypeDef](#worldgenerationjobsummarytypedef)
  - [WorldSummaryTypeDef](#worldsummarytypedef)

## BatchDeleteWorldsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsResponseTypeDef
```




Optional fields:
- `unprocessedWorlds`: `List[str]`


## BatchDescribeSimulationJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import BatchDescribeSimulationJobResponseTypeDef
```




Optional fields:
- `jobs`: `List["SimulationJobTypeDef"]`
- `unprocessedJobs`: `List[str]`


## BatchPolicyTypeDef

```python
from mypy_boto3_robomaker.type_defs import BatchPolicyTypeDef
```




Optional fields:
- `timeoutInSeconds`: `int`
- `maxConcurrency`: `int`


## ComputeResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ComputeResponseTypeDef
```




Optional fields:
- `simulationUnitLimit`: `int`


## ComputeTypeDef

```python
from mypy_boto3_robomaker.type_defs import ComputeTypeDef
```




Optional fields:
- `simulationUnitLimit`: `int`


## CreateDeploymentJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateDeploymentJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `fleet`: `str`
- `status`: `DeploymentStatus`
- `deploymentApplicationConfigs`: `List["DeploymentApplicationConfigTypeDef"]`
- `failureReason`: `str`
- `failureCode`: `DeploymentJobErrorCode`
- `createdAt`: `datetime`
- `deploymentConfig`: `"DeploymentConfigTypeDef"`
- `tags`: `Dict[str, str]`


## CreateFleetResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateFleetResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `createdAt`: `datetime`
- `tags`: `Dict[str, str]`


## CreateRobotApplicationResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateRobotApplicationResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `lastUpdatedAt`: `datetime`
- `revisionId`: `str`
- `tags`: `Dict[str, str]`


## CreateRobotApplicationVersionResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateRobotApplicationVersionResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `lastUpdatedAt`: `datetime`
- `revisionId`: `str`


## CreateRobotResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateRobotResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `createdAt`: `datetime`
- `greengrassGroupId`: `str`
- `architecture`: `Architecture`
- `tags`: `Dict[str, str]`


## CreateSimulationApplicationResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateSimulationApplicationResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `simulationSoftwareSuite`: `"SimulationSoftwareSuiteTypeDef"`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `renderingEngine`: `"RenderingEngineTypeDef"`
- `lastUpdatedAt`: `datetime`
- `revisionId`: `str`
- `tags`: `Dict[str, str]`


## CreateSimulationApplicationVersionResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateSimulationApplicationVersionResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `simulationSoftwareSuite`: `"SimulationSoftwareSuiteTypeDef"`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `renderingEngine`: `"RenderingEngineTypeDef"`
- `lastUpdatedAt`: `datetime`
- `revisionId`: `str`


## CreateSimulationJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateSimulationJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `SimulationJobStatus`
- `lastStartedAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `failureBehavior`: `FailureBehavior`
- `failureCode`: `SimulationJobErrorCode`
- `clientRequestToken`: `str`
- `outputLocation`: `"OutputLocationTypeDef"`
- `loggingConfig`: `"LoggingConfigTypeDef"`
- `maxJobDurationInSeconds`: `int`
- `simulationTimeMillis`: `int`
- `iamRole`: `str`
- `robotApplications`: `List["RobotApplicationConfigTypeDef"]`
- `simulationApplications`: `List["SimulationApplicationConfigTypeDef"]`
- `dataSources`: `List["DataSourceTypeDef"]`
- `tags`: `Dict[str, str]`
- `vpcConfig`: `"VPCConfigResponseTypeDef"`
- `compute`: `"ComputeResponseTypeDef"`


## CreateWorldExportJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateWorldExportJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `WorldExportJobStatus`
- `createdAt`: `datetime`
- `failureCode`: `WorldExportJobErrorCode`
- `clientRequestToken`: `str`
- `outputLocation`: `"OutputLocationTypeDef"`
- `iamRole`: `str`
- `tags`: `Dict[str, str]`


## CreateWorldGenerationJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateWorldGenerationJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `WorldGenerationJobStatus`
- `createdAt`: `datetime`
- `failureCode`: `WorldGenerationJobErrorCode`
- `clientRequestToken`: `str`
- `template`: `str`
- `worldCount`: `"WorldCountTypeDef"`
- `tags`: `Dict[str, str]`
- `worldTags`: `Dict[str, str]`


## CreateWorldTemplateResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import CreateWorldTemplateResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `clientRequestToken`: `str`
- `createdAt`: `datetime`
- `name`: `str`
- `tags`: `Dict[str, str]`


## DataSourceConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import DataSourceConfigTypeDef
```


Required fields:
- `name`: `str`
- `s3Bucket`: `str`
- `s3Keys`: `List[str]`




## DataSourceTypeDef

```python
from mypy_boto3_robomaker.type_defs import DataSourceTypeDef
```




Optional fields:
- `name`: `str`
- `s3Bucket`: `str`
- `s3Keys`: `List["S3KeyOutputTypeDef"]`


## DeploymentApplicationConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import DeploymentApplicationConfigTypeDef
```


Required fields:
- `application`: `str`
- `applicationVersion`: `str`
- `launchConfig`: `"DeploymentLaunchConfigTypeDef"`




## DeploymentConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import DeploymentConfigTypeDef
```




Optional fields:
- `concurrentDeploymentPercentage`: `int`
- `failureThresholdPercentage`: `int`
- `robotDeploymentTimeoutInSeconds`: `int`
- `downloadConditionFile`: `"S3ObjectTypeDef"`


## DeploymentJobTypeDef

```python
from mypy_boto3_robomaker.type_defs import DeploymentJobTypeDef
```




Optional fields:
- `arn`: `str`
- `fleet`: `str`
- `status`: `DeploymentStatus`
- `deploymentApplicationConfigs`: `List["DeploymentApplicationConfigTypeDef"]`
- `deploymentConfig`: `"DeploymentConfigTypeDef"`
- `failureReason`: `str`
- `failureCode`: `DeploymentJobErrorCode`
- `createdAt`: `datetime`


## DeploymentLaunchConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import DeploymentLaunchConfigTypeDef
```


Required fields:
- `packageName`: `str`
- `launchFile`: `str`



Optional fields:
- `preLaunchFile`: `str`
- `postLaunchFile`: `str`
- `environmentVariables`: `Dict[str, str]`


## DeregisterRobotResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DeregisterRobotResponseTypeDef
```




Optional fields:
- `fleet`: `str`
- `robot`: `str`


## DescribeDeploymentJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeDeploymentJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `fleet`: `str`
- `status`: `DeploymentStatus`
- `deploymentConfig`: `"DeploymentConfigTypeDef"`
- `deploymentApplicationConfigs`: `List["DeploymentApplicationConfigTypeDef"]`
- `failureReason`: `str`
- `failureCode`: `DeploymentJobErrorCode`
- `createdAt`: `datetime`
- `robotDeploymentSummary`: `List["RobotDeploymentTypeDef"]`
- `tags`: `Dict[str, str]`


## DescribeFleetResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeFleetResponseTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `robots`: `List["RobotTypeDef"]`
- `createdAt`: `datetime`
- `lastDeploymentStatus`: `DeploymentStatus`
- `lastDeploymentJob`: `str`
- `lastDeploymentTime`: `datetime`
- `tags`: `Dict[str, str]`


## DescribeRobotApplicationResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeRobotApplicationResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `revisionId`: `str`
- `lastUpdatedAt`: `datetime`
- `tags`: `Dict[str, str]`


## DescribeRobotResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeRobotResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `fleetArn`: `str`
- `status`: `RobotStatus`
- `greengrassGroupId`: `str`
- `createdAt`: `datetime`
- `architecture`: `Architecture`
- `lastDeploymentJob`: `str`
- `lastDeploymentTime`: `datetime`
- `tags`: `Dict[str, str]`


## DescribeSimulationApplicationResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeSimulationApplicationResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `simulationSoftwareSuite`: `"SimulationSoftwareSuiteTypeDef"`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `renderingEngine`: `"RenderingEngineTypeDef"`
- `revisionId`: `str`
- `lastUpdatedAt`: `datetime`
- `tags`: `Dict[str, str]`


## DescribeSimulationJobBatchResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeSimulationJobBatchResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `SimulationJobBatchStatus`
- `lastUpdatedAt`: `datetime`
- `createdAt`: `datetime`
- `clientRequestToken`: `str`
- `batchPolicy`: `"BatchPolicyTypeDef"`
- `failureCode`: `Literal['InternalServiceError']`
- `failureReason`: `str`
- `failedRequests`: `List["FailedCreateSimulationJobRequestTypeDef"]`
- `pendingRequests`: `List["SimulationJobRequestTypeDef"]`
- `createdRequests`: `List["SimulationJobSummaryTypeDef"]`
- `tags`: `Dict[str, str]`


## DescribeSimulationJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeSimulationJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `status`: `SimulationJobStatus`
- `lastStartedAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `failureBehavior`: `FailureBehavior`
- `failureCode`: `SimulationJobErrorCode`
- `failureReason`: `str`
- `clientRequestToken`: `str`
- `outputLocation`: `"OutputLocationTypeDef"`
- `loggingConfig`: `"LoggingConfigTypeDef"`
- `maxJobDurationInSeconds`: `int`
- `simulationTimeMillis`: `int`
- `iamRole`: `str`
- `robotApplications`: `List["RobotApplicationConfigTypeDef"]`
- `simulationApplications`: `List["SimulationApplicationConfigTypeDef"]`
- `dataSources`: `List["DataSourceTypeDef"]`
- `tags`: `Dict[str, str]`
- `vpcConfig`: `"VPCConfigResponseTypeDef"`
- `networkInterface`: `"NetworkInterfaceTypeDef"`
- `compute`: `"ComputeResponseTypeDef"`


## DescribeWorldExportJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeWorldExportJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `WorldExportJobStatus`
- `createdAt`: `datetime`
- `failureCode`: `WorldExportJobErrorCode`
- `failureReason`: `str`
- `clientRequestToken`: `str`
- `worlds`: `List[str]`
- `outputLocation`: `"OutputLocationTypeDef"`
- `iamRole`: `str`
- `tags`: `Dict[str, str]`


## DescribeWorldGenerationJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeWorldGenerationJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `WorldGenerationJobStatus`
- `createdAt`: `datetime`
- `failureCode`: `WorldGenerationJobErrorCode`
- `failureReason`: `str`
- `clientRequestToken`: `str`
- `template`: `str`
- `worldCount`: `"WorldCountTypeDef"`
- `finishedWorldsSummary`: `"FinishedWorldsSummaryTypeDef"`
- `tags`: `Dict[str, str]`
- `worldTags`: `Dict[str, str]`


## DescribeWorldResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeWorldResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `generationJob`: `str`
- `template`: `str`
- `createdAt`: `datetime`
- `tags`: `Dict[str, str]`


## DescribeWorldTemplateResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import DescribeWorldTemplateResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `clientRequestToken`: `str`
- `name`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `tags`: `Dict[str, str]`


## FailedCreateSimulationJobRequestTypeDef

```python
from mypy_boto3_robomaker.type_defs import FailedCreateSimulationJobRequestTypeDef
```




Optional fields:
- `request`: `"SimulationJobRequestTypeDef"`
- `failureReason`: `str`
- `failureCode`: `SimulationJobErrorCode`
- `failedAt`: `datetime`


## FailureSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import FailureSummaryTypeDef
```




Optional fields:
- `totalFailureCount`: `int`
- `failures`: `List["WorldFailureTypeDef"]`


## FilterTypeDef

```python
from mypy_boto3_robomaker.type_defs import FilterTypeDef
```




Optional fields:
- `name`: `str`
- `values`: `List[str]`


## FinishedWorldsSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import FinishedWorldsSummaryTypeDef
```




Optional fields:
- `finishedCount`: `int`
- `succeededWorlds`: `List[str]`
- `failureSummary`: `"FailureSummaryTypeDef"`


## FleetTypeDef

```python
from mypy_boto3_robomaker.type_defs import FleetTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `lastDeploymentStatus`: `DeploymentStatus`
- `lastDeploymentJob`: `str`
- `lastDeploymentTime`: `datetime`


## GetWorldTemplateBodyResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import GetWorldTemplateBodyResponseTypeDef
```




Optional fields:
- `templateBody`: `str`


## LaunchConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import LaunchConfigTypeDef
```


Required fields:
- `packageName`: `str`
- `launchFile`: `str`



Optional fields:
- `environmentVariables`: `Dict[str, str]`
- `portForwardingConfig`: `"PortForwardingConfigTypeDef"`
- `streamUI`: `bool`


## ListDeploymentJobsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListDeploymentJobsResponseTypeDef
```




Optional fields:
- `deploymentJobs`: `List["DeploymentJobTypeDef"]`
- `nextToken`: `str`


## ListFleetsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListFleetsResponseTypeDef
```




Optional fields:
- `fleetDetails`: `List["FleetTypeDef"]`
- `nextToken`: `str`


## ListRobotApplicationsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListRobotApplicationsResponseTypeDef
```




Optional fields:
- `robotApplicationSummaries`: `List["RobotApplicationSummaryTypeDef"]`
- `nextToken`: `str`


## ListRobotsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListRobotsResponseTypeDef
```




Optional fields:
- `robots`: `List["RobotTypeDef"]`
- `nextToken`: `str`


## ListSimulationApplicationsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListSimulationApplicationsResponseTypeDef
```




Optional fields:
- `simulationApplicationSummaries`: `List["SimulationApplicationSummaryTypeDef"]`
- `nextToken`: `str`


## ListSimulationJobBatchesResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListSimulationJobBatchesResponseTypeDef
```




Optional fields:
- `simulationJobBatchSummaries`: `List["SimulationJobBatchSummaryTypeDef"]`
- `nextToken`: `str`


## ListSimulationJobsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListSimulationJobsResponseTypeDef
```


Required fields:
- `simulationJobSummaries`: `List["SimulationJobSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListWorldExportJobsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListWorldExportJobsResponseTypeDef
```


Required fields:
- `worldExportJobSummaries`: `List["WorldExportJobSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListWorldGenerationJobsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListWorldGenerationJobsResponseTypeDef
```


Required fields:
- `worldGenerationJobSummaries`: `List["WorldGenerationJobSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListWorldTemplatesResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListWorldTemplatesResponseTypeDef
```




Optional fields:
- `templateSummaries`: `List["TemplateSummaryTypeDef"]`
- `nextToken`: `str`


## ListWorldsResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import ListWorldsResponseTypeDef
```




Optional fields:
- `worldSummaries`: `List["WorldSummaryTypeDef"]`
- `nextToken`: `str`


## LoggingConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import LoggingConfigTypeDef
```


Required fields:
- `recordAllRosTopics`: `bool`




## NetworkInterfaceTypeDef

```python
from mypy_boto3_robomaker.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `networkInterfaceId`: `str`
- `privateIpAddress`: `str`
- `publicIpAddress`: `str`


## OutputLocationTypeDef

```python
from mypy_boto3_robomaker.type_defs import OutputLocationTypeDef
```




Optional fields:
- `s3Bucket`: `str`
- `s3Prefix`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PortForwardingConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import PortForwardingConfigTypeDef
```




Optional fields:
- `portMappings`: `List["PortMappingTypeDef"]`


## PortMappingTypeDef

```python
from mypy_boto3_robomaker.type_defs import PortMappingTypeDef
```


Required fields:
- `jobPort`: `int`
- `applicationPort`: `int`



Optional fields:
- `enableOnPublicIp`: `bool`


## ProgressDetailTypeDef

```python
from mypy_boto3_robomaker.type_defs import ProgressDetailTypeDef
```




Optional fields:
- `currentProgress`: `RobotDeploymentStep`
- `percentDone`: `float`
- `estimatedTimeRemainingSeconds`: `int`
- `targetResource`: `str`


## RegisterRobotResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import RegisterRobotResponseTypeDef
```




Optional fields:
- `fleet`: `str`
- `robot`: `str`


## RenderingEngineTypeDef

```python
from mypy_boto3_robomaker.type_defs import RenderingEngineTypeDef
```




Optional fields:
- `name`: `Literal['OGRE']`
- `version`: `str`


## ResponseMetadata

```python
from mypy_boto3_robomaker.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RobotApplicationConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import RobotApplicationConfigTypeDef
```


Required fields:
- `application`: `str`
- `launchConfig`: `"LaunchConfigTypeDef"`



Optional fields:
- `applicationVersion`: `str`
- `uploadConfigurations`: `List["UploadConfigurationTypeDef"]`
- `useDefaultUploadConfigurations`: `bool`
- `tools`: `List["ToolTypeDef"]`
- `useDefaultTools`: `bool`


## RobotApplicationSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import RobotApplicationSummaryTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `version`: `str`
- `lastUpdatedAt`: `datetime`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`


## RobotDeploymentTypeDef

```python
from mypy_boto3_robomaker.type_defs import RobotDeploymentTypeDef
```




Optional fields:
- `arn`: `str`
- `deploymentStartTime`: `datetime`
- `deploymentFinishTime`: `datetime`
- `status`: `RobotStatus`
- `progressDetail`: `"ProgressDetailTypeDef"`
- `failureReason`: `str`
- `failureCode`: `DeploymentJobErrorCode`


## RobotSoftwareSuiteTypeDef

```python
from mypy_boto3_robomaker.type_defs import RobotSoftwareSuiteTypeDef
```




Optional fields:
- `name`: `RobotSoftwareSuiteType`
- `version`: `RobotSoftwareSuiteVersionType`


## RobotTypeDef

```python
from mypy_boto3_robomaker.type_defs import RobotTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `fleetArn`: `str`
- `status`: `RobotStatus`
- `greenGrassGroupId`: `str`
- `createdAt`: `datetime`
- `architecture`: `Architecture`
- `lastDeploymentJob`: `str`
- `lastDeploymentTime`: `datetime`


## S3KeyOutputTypeDef

```python
from mypy_boto3_robomaker.type_defs import S3KeyOutputTypeDef
```




Optional fields:
- `s3Key`: `str`
- `etag`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## S3ObjectTypeDef

```python
from mypy_boto3_robomaker.type_defs import S3ObjectTypeDef
```


Required fields:
- `bucket`: `str`
- `key`: `str`



Optional fields:
- `etag`: `str`


## SimulationApplicationConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationApplicationConfigTypeDef
```


Required fields:
- `application`: `str`
- `launchConfig`: `"LaunchConfigTypeDef"`



Optional fields:
- `applicationVersion`: `str`
- `uploadConfigurations`: `List["UploadConfigurationTypeDef"]`
- `worldConfigs`: `List["WorldConfigTypeDef"]`
- `useDefaultUploadConfigurations`: `bool`
- `tools`: `List["ToolTypeDef"]`
- `useDefaultTools`: `bool`


## SimulationApplicationSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationApplicationSummaryTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `version`: `str`
- `lastUpdatedAt`: `datetime`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `simulationSoftwareSuite`: `"SimulationSoftwareSuiteTypeDef"`


## SimulationJobBatchSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationJobBatchSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `lastUpdatedAt`: `datetime`
- `createdAt`: `datetime`
- `status`: `SimulationJobBatchStatus`
- `failedRequestCount`: `int`
- `pendingRequestCount`: `int`
- `createdRequestCount`: `int`


## SimulationJobRequestTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationJobRequestTypeDef
```


Required fields:
- `maxJobDurationInSeconds`: `int`



Optional fields:
- `outputLocation`: `"OutputLocationTypeDef"`
- `loggingConfig`: `"LoggingConfigTypeDef"`
- `iamRole`: `str`
- `failureBehavior`: `FailureBehavior`
- `useDefaultApplications`: `bool`
- `robotApplications`: `List["RobotApplicationConfigTypeDef"]`
- `simulationApplications`: `List["SimulationApplicationConfigTypeDef"]`
- `dataSources`: `List["DataSourceConfigTypeDef"]`
- `vpcConfig`: `"VPCConfigTypeDef"`
- `compute`: `"ComputeTypeDef"`
- `tags`: `Dict[str, str]`


## SimulationJobSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationJobSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `lastUpdatedAt`: `datetime`
- `name`: `str`
- `status`: `SimulationJobStatus`
- `simulationApplicationNames`: `List[str]`
- `robotApplicationNames`: `List[str]`
- `dataSourceNames`: `List[str]`


## SimulationJobTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationJobTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `status`: `SimulationJobStatus`
- `lastStartedAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `failureBehavior`: `FailureBehavior`
- `failureCode`: `SimulationJobErrorCode`
- `failureReason`: `str`
- `clientRequestToken`: `str`
- `outputLocation`: `"OutputLocationTypeDef"`
- `loggingConfig`: `"LoggingConfigTypeDef"`
- `maxJobDurationInSeconds`: `int`
- `simulationTimeMillis`: `int`
- `iamRole`: `str`
- `robotApplications`: `List["RobotApplicationConfigTypeDef"]`
- `simulationApplications`: `List["SimulationApplicationConfigTypeDef"]`
- `dataSources`: `List["DataSourceTypeDef"]`
- `tags`: `Dict[str, str]`
- `vpcConfig`: `"VPCConfigResponseTypeDef"`
- `networkInterface`: `"NetworkInterfaceTypeDef"`
- `compute`: `"ComputeResponseTypeDef"`


## SimulationSoftwareSuiteTypeDef

```python
from mypy_boto3_robomaker.type_defs import SimulationSoftwareSuiteTypeDef
```




Optional fields:
- `name`: `SimulationSoftwareSuiteType`
- `version`: `str`


## SourceConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import SourceConfigTypeDef
```




Optional fields:
- `s3Bucket`: `str`
- `s3Key`: `str`
- `architecture`: `Architecture`


## SourceTypeDef

```python
from mypy_boto3_robomaker.type_defs import SourceTypeDef
```




Optional fields:
- `s3Bucket`: `str`
- `s3Key`: `str`
- `etag`: `str`
- `architecture`: `Architecture`


## StartSimulationJobBatchResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import StartSimulationJobBatchResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `SimulationJobBatchStatus`
- `createdAt`: `datetime`
- `clientRequestToken`: `str`
- `batchPolicy`: `"BatchPolicyTypeDef"`
- `failureCode`: `Literal['InternalServiceError']`
- `failureReason`: `str`
- `failedRequests`: `List["FailedCreateSimulationJobRequestTypeDef"]`
- `pendingRequests`: `List["SimulationJobRequestTypeDef"]`
- `createdRequests`: `List["SimulationJobSummaryTypeDef"]`
- `tags`: `Dict[str, str]`


## SyncDeploymentJobResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import SyncDeploymentJobResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `fleet`: `str`
- `status`: `DeploymentStatus`
- `deploymentConfig`: `"DeploymentConfigTypeDef"`
- `deploymentApplicationConfigs`: `List["DeploymentApplicationConfigTypeDef"]`
- `failureReason`: `str`
- `failureCode`: `DeploymentJobErrorCode`
- `createdAt`: `datetime`


## TemplateLocationTypeDef

```python
from mypy_boto3_robomaker.type_defs import TemplateLocationTypeDef
```


Required fields:
- `s3Bucket`: `str`
- `s3Key`: `str`




## TemplateSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import TemplateSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `name`: `str`


## ToolTypeDef

```python
from mypy_boto3_robomaker.type_defs import ToolTypeDef
```


Required fields:
- `name`: `str`
- `command`: `str`



Optional fields:
- `streamUI`: `bool`
- `streamOutputToCloudWatch`: `bool`
- `exitBehavior`: `ExitBehavior`


## UpdateRobotApplicationResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import UpdateRobotApplicationResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `lastUpdatedAt`: `datetime`
- `revisionId`: `str`


## UpdateSimulationApplicationResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import UpdateSimulationApplicationResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `sources`: `List["SourceTypeDef"]`
- `simulationSoftwareSuite`: `"SimulationSoftwareSuiteTypeDef"`
- `robotSoftwareSuite`: `"RobotSoftwareSuiteTypeDef"`
- `renderingEngine`: `"RenderingEngineTypeDef"`
- `lastUpdatedAt`: `datetime`
- `revisionId`: `str`


## UpdateWorldTemplateResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import UpdateWorldTemplateResponseTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`


## UploadConfigurationTypeDef

```python
from mypy_boto3_robomaker.type_defs import UploadConfigurationTypeDef
```


Required fields:
- `name`: `str`
- `path`: `str`
- `uploadBehavior`: `UploadBehavior`




## VPCConfigResponseTypeDef

```python
from mypy_boto3_robomaker.type_defs import VPCConfigResponseTypeDef
```




Optional fields:
- `subnets`: `List[str]`
- `securityGroups`: `List[str]`
- `vpcId`: `str`
- `assignPublicIp`: `bool`


## VPCConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import VPCConfigTypeDef
```


Required fields:
- `subnets`: `List[str]`



Optional fields:
- `securityGroups`: `List[str]`
- `assignPublicIp`: `bool`


## WorldConfigTypeDef

```python
from mypy_boto3_robomaker.type_defs import WorldConfigTypeDef
```




Optional fields:
- `world`: `str`


## WorldCountTypeDef

```python
from mypy_boto3_robomaker.type_defs import WorldCountTypeDef
```




Optional fields:
- `floorplanCount`: `int`
- `interiorCountPerFloorplan`: `int`


## WorldExportJobSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import WorldExportJobSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `WorldExportJobStatus`
- `createdAt`: `datetime`
- `worlds`: `List[str]`


## WorldFailureTypeDef

```python
from mypy_boto3_robomaker.type_defs import WorldFailureTypeDef
```




Optional fields:
- `failureCode`: `WorldGenerationJobErrorCode`
- `sampleFailureReason`: `str`
- `failureCount`: `int`


## WorldGenerationJobSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import WorldGenerationJobSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `template`: `str`
- `createdAt`: `datetime`
- `status`: `WorldGenerationJobStatus`
- `worldCount`: `"WorldCountTypeDef"`
- `succeededWorldCount`: `int`
- `failedWorldCount`: `int`


## WorldSummaryTypeDef

```python
from mypy_boto3_robomaker.type_defs import WorldSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `generationJob`: `str`
- `template`: `str`

