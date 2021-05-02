# Type annotations for boto3 RoboMaker module

> [Index](../index.md) > RoboMaker

Auto-generated documentation for [RoboMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker)
type annotations stubs module [mypy_boto3_robomaker](https://pypi.org/project/mypy-boto3-robomaker/).

```bash
pip install mypy-boto3-robomaker
```

- [Type annotations for boto3 RoboMaker module](#type-annotations-for-boto3-robomaker-module)
  - [RoboMakerClient](#robomakerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## RoboMakerClient

Type annotations for  `boto3.client("robomaker")` as [RoboMakerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_robomaker.client import RoboMakerClient
```


RoboMakerClient [exceptions](./client.md#exceptions)



### Methods
- [batch_delete_worlds](./client.md#batch-delete-worlds)
- [batch_describe_simulation_job](./client.md#batch-describe-simulation-job)
- [can_paginate](./client.md#can-paginate)
- [cancel_deployment_job](./client.md#cancel-deployment-job)
- [cancel_simulation_job](./client.md#cancel-simulation-job)
- [cancel_simulation_job_batch](./client.md#cancel-simulation-job-batch)
- [cancel_world_export_job](./client.md#cancel-world-export-job)
- [cancel_world_generation_job](./client.md#cancel-world-generation-job)
- [create_deployment_job](./client.md#create-deployment-job)
- [create_fleet](./client.md#create-fleet)
- [create_robot](./client.md#create-robot)
- [create_robot_application](./client.md#create-robot-application)
- [create_robot_application_version](./client.md#create-robot-application-version)
- [create_simulation_application](./client.md#create-simulation-application)
- [create_simulation_application_version](./client.md#create-simulation-application-version)
- [create_simulation_job](./client.md#create-simulation-job)
- [create_world_export_job](./client.md#create-world-export-job)
- [create_world_generation_job](./client.md#create-world-generation-job)
- [create_world_template](./client.md#create-world-template)
- [delete_fleet](./client.md#delete-fleet)
- [delete_robot](./client.md#delete-robot)
- [delete_robot_application](./client.md#delete-robot-application)
- [delete_simulation_application](./client.md#delete-simulation-application)
- [delete_world_template](./client.md#delete-world-template)
- [deregister_robot](./client.md#deregister-robot)
- [describe_deployment_job](./client.md#describe-deployment-job)
- [describe_fleet](./client.md#describe-fleet)
- [describe_robot](./client.md#describe-robot)
- [describe_robot_application](./client.md#describe-robot-application)
- [describe_simulation_application](./client.md#describe-simulation-application)
- [describe_simulation_job](./client.md#describe-simulation-job)
- [describe_simulation_job_batch](./client.md#describe-simulation-job-batch)
- [describe_world](./client.md#describe-world)
- [describe_world_export_job](./client.md#describe-world-export-job)
- [describe_world_generation_job](./client.md#describe-world-generation-job)
- [describe_world_template](./client.md#describe-world-template)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_world_template_body](./client.md#get-world-template-body)
- [list_deployment_jobs](./client.md#list-deployment-jobs)
- [list_fleets](./client.md#list-fleets)
- [list_robot_applications](./client.md#list-robot-applications)
- [list_robots](./client.md#list-robots)
- [list_simulation_applications](./client.md#list-simulation-applications)
- [list_simulation_job_batches](./client.md#list-simulation-job-batches)
- [list_simulation_jobs](./client.md#list-simulation-jobs)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_world_export_jobs](./client.md#list-world-export-jobs)
- [list_world_generation_jobs](./client.md#list-world-generation-jobs)
- [list_world_templates](./client.md#list-world-templates)
- [list_worlds](./client.md#list-worlds)
- [register_robot](./client.md#register-robot)
- [restart_simulation_job](./client.md#restart-simulation-job)
- [start_simulation_job_batch](./client.md#start-simulation-job-batch)
- [sync_deployment_job](./client.md#sync-deployment-job)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_robot_application](./client.md#update-robot-application)
- [update_simulation_application](./client.md#update-simulation-application)
- [update_world_template](./client.md#update-world-template)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentDeploymentException](./client.md#concurrentdeploymentexception)
- [IdempotentParameterMismatchException](./client.md#idempotentparametermismatchexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("robomaker").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_robomaker.paginators import ListDeploymentJobsPaginator, ...
```

- [ListDeploymentJobsPaginator](./paginators.md#listdeploymentjobspaginator)
- [ListFleetsPaginator](./paginators.md#listfleetspaginator)
- [ListRobotApplicationsPaginator](./paginators.md#listrobotapplicationspaginator)
- [ListRobotsPaginator](./paginators.md#listrobotspaginator)
- [ListSimulationApplicationsPaginator](./paginators.md#listsimulationapplicationspaginator)
- [ListSimulationJobBatchesPaginator](./paginators.md#listsimulationjobbatchespaginator)
- [ListSimulationJobsPaginator](./paginators.md#listsimulationjobspaginator)
- [ListWorldExportJobsPaginator](./paginators.md#listworldexportjobspaginator)
- [ListWorldGenerationJobsPaginator](./paginators.md#listworldgenerationjobspaginator)
- [ListWorldTemplatesPaginator](./paginators.md#listworldtemplatespaginator)
- [ListWorldsPaginator](./paginators.md#listworldspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_robomaker.literals import Architecture, ...
```

- [Architecture](./literals.md#architecture)
- [DeploymentJobErrorCode](./literals.md#deploymentjoberrorcode)
- [DeploymentStatus](./literals.md#deploymentstatus)
- [ExitBehavior](./literals.md#exitbehavior)
- [FailureBehavior](./literals.md#failurebehavior)
- [ListDeploymentJobsPaginatorName](./literals.md#listdeploymentjobspaginatorname)
- [ListFleetsPaginatorName](./literals.md#listfleetspaginatorname)
- [ListRobotApplicationsPaginatorName](./literals.md#listrobotapplicationspaginatorname)
- [ListRobotsPaginatorName](./literals.md#listrobotspaginatorname)
- [ListSimulationApplicationsPaginatorName](./literals.md#listsimulationapplicationspaginatorname)
- [ListSimulationJobBatchesPaginatorName](./literals.md#listsimulationjobbatchespaginatorname)
- [ListSimulationJobsPaginatorName](./literals.md#listsimulationjobspaginatorname)
- [ListWorldExportJobsPaginatorName](./literals.md#listworldexportjobspaginatorname)
- [ListWorldGenerationJobsPaginatorName](./literals.md#listworldgenerationjobspaginatorname)
- [ListWorldTemplatesPaginatorName](./literals.md#listworldtemplatespaginatorname)
- [ListWorldsPaginatorName](./literals.md#listworldspaginatorname)
- [RenderingEngineType](./literals.md#renderingenginetype)
- [RobotDeploymentStep](./literals.md#robotdeploymentstep)
- [RobotSoftwareSuiteType](./literals.md#robotsoftwaresuitetype)
- [RobotSoftwareSuiteVersionType](./literals.md#robotsoftwaresuiteversiontype)
- [RobotStatus](./literals.md#robotstatus)
- [SimulationJobBatchErrorCode](./literals.md#simulationjobbatcherrorcode)
- [SimulationJobBatchStatus](./literals.md#simulationjobbatchstatus)
- [SimulationJobErrorCode](./literals.md#simulationjoberrorcode)
- [SimulationJobStatus](./literals.md#simulationjobstatus)
- [SimulationSoftwareSuiteType](./literals.md#simulationsoftwaresuitetype)
- [UploadBehavior](./literals.md#uploadbehavior)
- [WorldExportJobErrorCode](./literals.md#worldexportjoberrorcode)
- [WorldExportJobStatus](./literals.md#worldexportjobstatus)
- [WorldGenerationJobErrorCode](./literals.md#worldgenerationjoberrorcode)
- [WorldGenerationJobStatus](./literals.md#worldgenerationjobstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsResponseTypeDef, ...
```

- [BatchDeleteWorldsResponseTypeDef](./type_defs.md#batchdeleteworldsresponsetypedef)
- [BatchDescribeSimulationJobResponseTypeDef](./type_defs.md#batchdescribesimulationjobresponsetypedef)
- [BatchPolicyTypeDef](./type_defs.md#batchpolicytypedef)
- [ComputeResponseTypeDef](./type_defs.md#computeresponsetypedef)
- [ComputeTypeDef](./type_defs.md#computetypedef)
- [CreateDeploymentJobResponseTypeDef](./type_defs.md#createdeploymentjobresponsetypedef)
- [CreateFleetResponseTypeDef](./type_defs.md#createfleetresponsetypedef)
- [CreateRobotApplicationResponseTypeDef](./type_defs.md#createrobotapplicationresponsetypedef)
- [CreateRobotApplicationVersionResponseTypeDef](./type_defs.md#createrobotapplicationversionresponsetypedef)
- [CreateRobotResponseTypeDef](./type_defs.md#createrobotresponsetypedef)
- [CreateSimulationApplicationResponseTypeDef](./type_defs.md#createsimulationapplicationresponsetypedef)
- [CreateSimulationApplicationVersionResponseTypeDef](./type_defs.md#createsimulationapplicationversionresponsetypedef)
- [CreateSimulationJobResponseTypeDef](./type_defs.md#createsimulationjobresponsetypedef)
- [CreateWorldExportJobResponseTypeDef](./type_defs.md#createworldexportjobresponsetypedef)
- [CreateWorldGenerationJobResponseTypeDef](./type_defs.md#createworldgenerationjobresponsetypedef)
- [CreateWorldTemplateResponseTypeDef](./type_defs.md#createworldtemplateresponsetypedef)
- [DataSourceConfigTypeDef](./type_defs.md#datasourceconfigtypedef)
- [DataSourceTypeDef](./type_defs.md#datasourcetypedef)
- [DeploymentApplicationConfigTypeDef](./type_defs.md#deploymentapplicationconfigtypedef)
- [DeploymentConfigTypeDef](./type_defs.md#deploymentconfigtypedef)
- [DeploymentJobTypeDef](./type_defs.md#deploymentjobtypedef)
- [DeploymentLaunchConfigTypeDef](./type_defs.md#deploymentlaunchconfigtypedef)
- [DeregisterRobotResponseTypeDef](./type_defs.md#deregisterrobotresponsetypedef)
- [DescribeDeploymentJobResponseTypeDef](./type_defs.md#describedeploymentjobresponsetypedef)
- [DescribeFleetResponseTypeDef](./type_defs.md#describefleetresponsetypedef)
- [DescribeRobotApplicationResponseTypeDef](./type_defs.md#describerobotapplicationresponsetypedef)
- [DescribeRobotResponseTypeDef](./type_defs.md#describerobotresponsetypedef)
- [DescribeSimulationApplicationResponseTypeDef](./type_defs.md#describesimulationapplicationresponsetypedef)
- [DescribeSimulationJobBatchResponseTypeDef](./type_defs.md#describesimulationjobbatchresponsetypedef)
- [DescribeSimulationJobResponseTypeDef](./type_defs.md#describesimulationjobresponsetypedef)
- [DescribeWorldExportJobResponseTypeDef](./type_defs.md#describeworldexportjobresponsetypedef)
- [DescribeWorldGenerationJobResponseTypeDef](./type_defs.md#describeworldgenerationjobresponsetypedef)
- [DescribeWorldResponseTypeDef](./type_defs.md#describeworldresponsetypedef)
- [DescribeWorldTemplateResponseTypeDef](./type_defs.md#describeworldtemplateresponsetypedef)
- [FailedCreateSimulationJobRequestTypeDef](./type_defs.md#failedcreatesimulationjobrequesttypedef)
- [FailureSummaryTypeDef](./type_defs.md#failuresummarytypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [FinishedWorldsSummaryTypeDef](./type_defs.md#finishedworldssummarytypedef)
- [FleetTypeDef](./type_defs.md#fleettypedef)
- [GetWorldTemplateBodyResponseTypeDef](./type_defs.md#getworldtemplatebodyresponsetypedef)
- [LaunchConfigTypeDef](./type_defs.md#launchconfigtypedef)
- [ListDeploymentJobsResponseTypeDef](./type_defs.md#listdeploymentjobsresponsetypedef)
- [ListFleetsResponseTypeDef](./type_defs.md#listfleetsresponsetypedef)
- [ListRobotApplicationsResponseTypeDef](./type_defs.md#listrobotapplicationsresponsetypedef)
- [ListRobotsResponseTypeDef](./type_defs.md#listrobotsresponsetypedef)
- [ListSimulationApplicationsResponseTypeDef](./type_defs.md#listsimulationapplicationsresponsetypedef)
- [ListSimulationJobBatchesResponseTypeDef](./type_defs.md#listsimulationjobbatchesresponsetypedef)
- [ListSimulationJobsResponseTypeDef](./type_defs.md#listsimulationjobsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListWorldExportJobsResponseTypeDef](./type_defs.md#listworldexportjobsresponsetypedef)
- [ListWorldGenerationJobsResponseTypeDef](./type_defs.md#listworldgenerationjobsresponsetypedef)
- [ListWorldTemplatesResponseTypeDef](./type_defs.md#listworldtemplatesresponsetypedef)
- [ListWorldsResponseTypeDef](./type_defs.md#listworldsresponsetypedef)
- [LoggingConfigTypeDef](./type_defs.md#loggingconfigtypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [OutputLocationTypeDef](./type_defs.md#outputlocationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PortForwardingConfigTypeDef](./type_defs.md#portforwardingconfigtypedef)
- [PortMappingTypeDef](./type_defs.md#portmappingtypedef)
- [ProgressDetailTypeDef](./type_defs.md#progressdetailtypedef)
- [RegisterRobotResponseTypeDef](./type_defs.md#registerrobotresponsetypedef)
- [RenderingEngineTypeDef](./type_defs.md#renderingenginetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RobotApplicationConfigTypeDef](./type_defs.md#robotapplicationconfigtypedef)
- [RobotApplicationSummaryTypeDef](./type_defs.md#robotapplicationsummarytypedef)
- [RobotDeploymentTypeDef](./type_defs.md#robotdeploymenttypedef)
- [RobotSoftwareSuiteTypeDef](./type_defs.md#robotsoftwaresuitetypedef)
- [RobotTypeDef](./type_defs.md#robottypedef)
- [S3KeyOutputTypeDef](./type_defs.md#s3keyoutputtypedef)
- [S3ObjectTypeDef](./type_defs.md#s3objecttypedef)
- [SimulationApplicationConfigTypeDef](./type_defs.md#simulationapplicationconfigtypedef)
- [SimulationApplicationSummaryTypeDef](./type_defs.md#simulationapplicationsummarytypedef)
- [SimulationJobBatchSummaryTypeDef](./type_defs.md#simulationjobbatchsummarytypedef)
- [SimulationJobRequestTypeDef](./type_defs.md#simulationjobrequesttypedef)
- [SimulationJobSummaryTypeDef](./type_defs.md#simulationjobsummarytypedef)
- [SimulationJobTypeDef](./type_defs.md#simulationjobtypedef)
- [SimulationSoftwareSuiteTypeDef](./type_defs.md#simulationsoftwaresuitetypedef)
- [SourceConfigTypeDef](./type_defs.md#sourceconfigtypedef)
- [SourceTypeDef](./type_defs.md#sourcetypedef)
- [StartSimulationJobBatchResponseTypeDef](./type_defs.md#startsimulationjobbatchresponsetypedef)
- [SyncDeploymentJobResponseTypeDef](./type_defs.md#syncdeploymentjobresponsetypedef)
- [TemplateLocationTypeDef](./type_defs.md#templatelocationtypedef)
- [TemplateSummaryTypeDef](./type_defs.md#templatesummarytypedef)
- [ToolTypeDef](./type_defs.md#tooltypedef)
- [UpdateRobotApplicationResponseTypeDef](./type_defs.md#updaterobotapplicationresponsetypedef)
- [UpdateSimulationApplicationResponseTypeDef](./type_defs.md#updatesimulationapplicationresponsetypedef)
- [UpdateWorldTemplateResponseTypeDef](./type_defs.md#updateworldtemplateresponsetypedef)
- [UploadConfigurationTypeDef](./type_defs.md#uploadconfigurationtypedef)
- [VPCConfigResponseTypeDef](./type_defs.md#vpcconfigresponsetypedef)
- [VPCConfigTypeDef](./type_defs.md#vpcconfigtypedef)
- [WorldConfigTypeDef](./type_defs.md#worldconfigtypedef)
- [WorldCountTypeDef](./type_defs.md#worldcounttypedef)
- [WorldExportJobSummaryTypeDef](./type_defs.md#worldexportjobsummarytypedef)
- [WorldFailureTypeDef](./type_defs.md#worldfailuretypedef)
- [WorldGenerationJobSummaryTypeDef](./type_defs.md#worldgenerationjobsummarytypedef)
- [WorldSummaryTypeDef](./type_defs.md#worldsummarytypedef)
