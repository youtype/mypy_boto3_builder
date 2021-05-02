# RoboMakerClient for boto3 RoboMaker module

> [Index](../index.md) > [RoboMaker](./index.md) > RoboMakerClient

Auto-generated documentation for [RoboMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker)
type annotations stubs module [mypy_boto3_robomaker](https://pypi.org/project/mypy-boto3-robomaker/).

- [RoboMakerClient for boto3 RoboMaker module](#robomakerclient-for-boto3-robomaker-module)
  - [RoboMakerClient](#robomakerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_delete_worlds](#batch_delete_worlds)
    - [batch_describe_simulation_job](#batch_describe_simulation_job)
    - [can_paginate](#can_paginate)
    - [cancel_deployment_job](#cancel_deployment_job)
    - [cancel_simulation_job](#cancel_simulation_job)
    - [cancel_simulation_job_batch](#cancel_simulation_job_batch)
    - [cancel_world_export_job](#cancel_world_export_job)
    - [cancel_world_generation_job](#cancel_world_generation_job)
    - [create_deployment_job](#create_deployment_job)
    - [create_fleet](#create_fleet)
    - [create_robot](#create_robot)
    - [create_robot_application](#create_robot_application)
    - [create_robot_application_version](#create_robot_application_version)
    - [create_simulation_application](#create_simulation_application)
    - [create_simulation_application_version](#create_simulation_application_version)
    - [create_simulation_job](#create_simulation_job)
    - [create_world_export_job](#create_world_export_job)
    - [create_world_generation_job](#create_world_generation_job)
    - [create_world_template](#create_world_template)
    - [delete_fleet](#delete_fleet)
    - [delete_robot](#delete_robot)
    - [delete_robot_application](#delete_robot_application)
    - [delete_simulation_application](#delete_simulation_application)
    - [delete_world_template](#delete_world_template)
    - [deregister_robot](#deregister_robot)
    - [describe_deployment_job](#describe_deployment_job)
    - [describe_fleet](#describe_fleet)
    - [describe_robot](#describe_robot)
    - [describe_robot_application](#describe_robot_application)
    - [describe_simulation_application](#describe_simulation_application)
    - [describe_simulation_job](#describe_simulation_job)
    - [describe_simulation_job_batch](#describe_simulation_job_batch)
    - [describe_world](#describe_world)
    - [describe_world_export_job](#describe_world_export_job)
    - [describe_world_generation_job](#describe_world_generation_job)
    - [describe_world_template](#describe_world_template)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_world_template_body](#get_world_template_body)
    - [list_deployment_jobs](#list_deployment_jobs)
    - [list_fleets](#list_fleets)
    - [list_robot_applications](#list_robot_applications)
    - [list_robots](#list_robots)
    - [list_simulation_applications](#list_simulation_applications)
    - [list_simulation_job_batches](#list_simulation_job_batches)
    - [list_simulation_jobs](#list_simulation_jobs)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_world_export_jobs](#list_world_export_jobs)
    - [list_world_generation_jobs](#list_world_generation_jobs)
    - [list_world_templates](#list_world_templates)
    - [list_worlds](#list_worlds)
    - [register_robot](#register_robot)
    - [restart_simulation_job](#restart_simulation_job)
    - [start_simulation_job_batch](#start_simulation_job_batch)
    - [sync_deployment_job](#sync_deployment_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_robot_application](#update_robot_application)
    - [update_simulation_application](#update_simulation_application)
    - [update_world_template](#update_world_template)
    - [get_paginator](#get_paginator)

## RoboMakerClient

Type annotations for `boto3.client("robomaker")`

Can be used directly:

```python
from mypy_boto3_robomaker.client import RoboMakerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_robomaker.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentDeploymentException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidParameterException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`


## Methods


### batch_delete_worlds

Type annotations for `boto3.client("robomaker").batch_delete_worlds` method.

[Client.batch_delete_worlds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.batch_delete_worlds)

```python
def batch_delete_worlds(
    self,
    worlds: List[str]
) -> BatchDeleteWorldsResponseTypeDef:
    pass
```

### batch_describe_simulation_job

Type annotations for `boto3.client("robomaker").batch_describe_simulation_job` method.

[Client.batch_describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.batch_describe_simulation_job)

```python
def batch_describe_simulation_job(
    self,
    jobs: List[str]
) -> BatchDescribeSimulationJobResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("robomaker").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_deployment_job

Type annotations for `boto3.client("robomaker").cancel_deployment_job` method.

[Client.cancel_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_deployment_job)

```python
def cancel_deployment_job(
    self,
    job: str
) -> Dict[str, Any]:
    pass
```

### cancel_simulation_job

Type annotations for `boto3.client("robomaker").cancel_simulation_job` method.

[Client.cancel_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job)

```python
def cancel_simulation_job(
    self,
    job: str
) -> Dict[str, Any]:
    pass
```

### cancel_simulation_job_batch

Type annotations for `boto3.client("robomaker").cancel_simulation_job_batch` method.

[Client.cancel_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job_batch)

```python
def cancel_simulation_job_batch(
    self,
    batch: str
) -> Dict[str, Any]:
    pass
```

### cancel_world_export_job

Type annotations for `boto3.client("robomaker").cancel_world_export_job` method.

[Client.cancel_world_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_world_export_job)

```python
def cancel_world_export_job(
    self,
    job: str
) -> Dict[str, Any]:
    pass
```

### cancel_world_generation_job

Type annotations for `boto3.client("robomaker").cancel_world_generation_job` method.

[Client.cancel_world_generation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.cancel_world_generation_job)

```python
def cancel_world_generation_job(
    self,
    job: str
) -> Dict[str, Any]:
    pass
```

### create_deployment_job

Type annotations for `boto3.client("robomaker").create_deployment_job` method.

[Client.create_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_deployment_job)

```python
def create_deployment_job(
    self,
    clientRequestToken: str,
    fleet: str,
    deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"],
    deploymentConfig: "DeploymentConfigTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateDeploymentJobResponseTypeDef:
    pass
```

### create_fleet

Type annotations for `boto3.client("robomaker").create_fleet` method.

[Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_fleet)

```python
def create_fleet(
    self,
    name: str,
    tags: Dict[str, str] = None
) -> CreateFleetResponseTypeDef:
    pass
```

### create_robot

Type annotations for `boto3.client("robomaker").create_robot` method.

[Client.create_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_robot)

```python
def create_robot(
    self,
    name: str,
    architecture: Architecture,
    greengrassGroupId: str,
    tags: Dict[str, str] = None
) -> CreateRobotResponseTypeDef:
    pass
```

### create_robot_application

Type annotations for `boto3.client("robomaker").create_robot_application` method.

[Client.create_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_robot_application)

```python
def create_robot_application(
    self,
    name: str,
    sources: List[SourceConfigTypeDef],
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
    tags: Dict[str, str] = None
) -> CreateRobotApplicationResponseTypeDef:
    pass
```

### create_robot_application_version

Type annotations for `boto3.client("robomaker").create_robot_application_version` method.

[Client.create_robot_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_robot_application_version)

```python
def create_robot_application_version(
    self,
    application: str,
    currentRevisionId: str = None
) -> CreateRobotApplicationVersionResponseTypeDef:
    pass
```

### create_simulation_application

Type annotations for `boto3.client("robomaker").create_simulation_application` method.

[Client.create_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application)

```python
def create_simulation_application(
    self,
    name: str,
    sources: List[SourceConfigTypeDef],
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef",
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
    renderingEngine: "RenderingEngineTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateSimulationApplicationResponseTypeDef:
    pass
```

### create_simulation_application_version

Type annotations for `boto3.client("robomaker").create_simulation_application_version` method.

[Client.create_simulation_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application_version)

```python
def create_simulation_application_version(
    self,
    application: str,
    currentRevisionId: str = None
) -> CreateSimulationApplicationVersionResponseTypeDef:
    pass
```

### create_simulation_job

Type annotations for `boto3.client("robomaker").create_simulation_job` method.

[Client.create_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_simulation_job)

```python
def create_simulation_job(
    self,
    maxJobDurationInSeconds: int,
    iamRole: str,
    clientRequestToken: str = None,
    outputLocation: "OutputLocationTypeDef" = None,
    loggingConfig: "LoggingConfigTypeDef" = None,
    failureBehavior: FailureBehavior = None,
    robotApplications: List["RobotApplicationConfigTypeDef"] = None,
    simulationApplications: List["SimulationApplicationConfigTypeDef"] = None,
    dataSources: List["DataSourceConfigTypeDef"] = None,
    tags: Dict[str, str] = None,
    vpcConfig: "VPCConfigTypeDef" = None,
    compute: "ComputeTypeDef" = None
) -> CreateSimulationJobResponseTypeDef:
    pass
```

### create_world_export_job

Type annotations for `boto3.client("robomaker").create_world_export_job` method.

[Client.create_world_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_world_export_job)

```python
def create_world_export_job(
    self,
    worlds: List[str],
    outputLocation: "OutputLocationTypeDef",
    iamRole: str,
    clientRequestToken: str = None,
    tags: Dict[str, str] = None
) -> CreateWorldExportJobResponseTypeDef:
    pass
```

### create_world_generation_job

Type annotations for `boto3.client("robomaker").create_world_generation_job` method.

[Client.create_world_generation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_world_generation_job)

```python
def create_world_generation_job(
    self,
    template: str,
    worldCount: "WorldCountTypeDef",
    clientRequestToken: str = None,
    tags: Dict[str, str] = None,
    worldTags: Dict[str, str] = None
) -> CreateWorldGenerationJobResponseTypeDef:
    pass
```

### create_world_template

Type annotations for `boto3.client("robomaker").create_world_template` method.

[Client.create_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.create_world_template)

```python
def create_world_template(
    self,
    clientRequestToken: str = None,
    name: str = None,
    templateBody: str = None,
    templateLocation: TemplateLocationTypeDef = None,
    tags: Dict[str, str] = None
) -> CreateWorldTemplateResponseTypeDef:
    pass
```

### delete_fleet

Type annotations for `boto3.client("robomaker").delete_fleet` method.

[Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_fleet)

```python
def delete_fleet(
    self,
    fleet: str
) -> Dict[str, Any]:
    pass
```

### delete_robot

Type annotations for `boto3.client("robomaker").delete_robot` method.

[Client.delete_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_robot)

```python
def delete_robot(
    self,
    robot: str
) -> Dict[str, Any]:
    pass
```

### delete_robot_application

Type annotations for `boto3.client("robomaker").delete_robot_application` method.

[Client.delete_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_robot_application)

```python
def delete_robot_application(
    self,
    application: str,
    applicationVersion: str = None
) -> Dict[str, Any]:
    pass
```

### delete_simulation_application

Type annotations for `boto3.client("robomaker").delete_simulation_application` method.

[Client.delete_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_simulation_application)

```python
def delete_simulation_application(
    self,
    application: str,
    applicationVersion: str = None
) -> Dict[str, Any]:
    pass
```

### delete_world_template

Type annotations for `boto3.client("robomaker").delete_world_template` method.

[Client.delete_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.delete_world_template)

```python
def delete_world_template(
    self,
    template: str
) -> Dict[str, Any]:
    pass
```

### deregister_robot

Type annotations for `boto3.client("robomaker").deregister_robot` method.

[Client.deregister_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.deregister_robot)

```python
def deregister_robot(
    self,
    fleet: str,
    robot: str
) -> DeregisterRobotResponseTypeDef:
    pass
```

### describe_deployment_job

Type annotations for `boto3.client("robomaker").describe_deployment_job` method.

[Client.describe_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_deployment_job)

```python
def describe_deployment_job(
    self,
    job: str
) -> DescribeDeploymentJobResponseTypeDef:
    pass
```

### describe_fleet

Type annotations for `boto3.client("robomaker").describe_fleet` method.

[Client.describe_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_fleet)

```python
def describe_fleet(
    self,
    fleet: str
) -> DescribeFleetResponseTypeDef:
    pass
```

### describe_robot

Type annotations for `boto3.client("robomaker").describe_robot` method.

[Client.describe_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_robot)

```python
def describe_robot(
    self,
    robot: str
) -> DescribeRobotResponseTypeDef:
    pass
```

### describe_robot_application

Type annotations for `boto3.client("robomaker").describe_robot_application` method.

[Client.describe_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application)

```python
def describe_robot_application(
    self,
    application: str,
    applicationVersion: str = None
) -> DescribeRobotApplicationResponseTypeDef:
    pass
```

### describe_simulation_application

Type annotations for `boto3.client("robomaker").describe_simulation_application` method.

[Client.describe_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application)

```python
def describe_simulation_application(
    self,
    application: str,
    applicationVersion: str = None
) -> DescribeSimulationApplicationResponseTypeDef:
    pass
```

### describe_simulation_job

Type annotations for `boto3.client("robomaker").describe_simulation_job` method.

[Client.describe_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job)

```python
def describe_simulation_job(
    self,
    job: str
) -> DescribeSimulationJobResponseTypeDef:
    pass
```

### describe_simulation_job_batch

Type annotations for `boto3.client("robomaker").describe_simulation_job_batch` method.

[Client.describe_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job_batch)

```python
def describe_simulation_job_batch(
    self,
    batch: str
) -> DescribeSimulationJobBatchResponseTypeDef:
    pass
```

### describe_world

Type annotations for `boto3.client("robomaker").describe_world` method.

[Client.describe_world documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world)

```python
def describe_world(
    self,
    world: str
) -> DescribeWorldResponseTypeDef:
    pass
```

### describe_world_export_job

Type annotations for `boto3.client("robomaker").describe_world_export_job` method.

[Client.describe_world_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world_export_job)

```python
def describe_world_export_job(
    self,
    job: str
) -> DescribeWorldExportJobResponseTypeDef:
    pass
```

### describe_world_generation_job

Type annotations for `boto3.client("robomaker").describe_world_generation_job` method.

[Client.describe_world_generation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world_generation_job)

```python
def describe_world_generation_job(
    self,
    job: str
) -> DescribeWorldGenerationJobResponseTypeDef:
    pass
```

### describe_world_template

Type annotations for `boto3.client("robomaker").describe_world_template` method.

[Client.describe_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.describe_world_template)

```python
def describe_world_template(
    self,
    template: str
) -> DescribeWorldTemplateResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("robomaker").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.generate_presigned_url)

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

### get_world_template_body

Type annotations for `boto3.client("robomaker").get_world_template_body` method.

[Client.get_world_template_body documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.get_world_template_body)

```python
def get_world_template_body(
    self,
    template: str = None,
    generationJob: str = None
) -> GetWorldTemplateBodyResponseTypeDef:
    pass
```

### list_deployment_jobs

Type annotations for `boto3.client("robomaker").list_deployment_jobs` method.

[Client.list_deployment_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_deployment_jobs)

```python
def list_deployment_jobs(
    self,
    filters: List[FilterTypeDef] = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListDeploymentJobsResponseTypeDef:
    pass
```

### list_fleets

Type annotations for `boto3.client("robomaker").list_fleets` method.

[Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_fleets)

```python
def list_fleets(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListFleetsResponseTypeDef:
    pass
```

### list_robot_applications

Type annotations for `boto3.client("robomaker").list_robot_applications` method.

[Client.list_robot_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_robot_applications)

```python
def list_robot_applications(
    self,
    versionQualifier: str = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListRobotApplicationsResponseTypeDef:
    pass
```

### list_robots

Type annotations for `boto3.client("robomaker").list_robots` method.

[Client.list_robots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_robots)

```python
def list_robots(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListRobotsResponseTypeDef:
    pass
```

### list_simulation_applications

Type annotations for `boto3.client("robomaker").list_simulation_applications` method.

[Client.list_simulation_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_simulation_applications)

```python
def list_simulation_applications(
    self,
    versionQualifier: str = None,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListSimulationApplicationsResponseTypeDef:
    pass
```

### list_simulation_job_batches

Type annotations for `boto3.client("robomaker").list_simulation_job_batches` method.

[Client.list_simulation_job_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_simulation_job_batches)

```python
def list_simulation_job_batches(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListSimulationJobBatchesResponseTypeDef:
    pass
```

### list_simulation_jobs

Type annotations for `boto3.client("robomaker").list_simulation_jobs` method.

[Client.list_simulation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_simulation_jobs)

```python
def list_simulation_jobs(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListSimulationJobsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("robomaker").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_world_export_jobs

Type annotations for `boto3.client("robomaker").list_world_export_jobs` method.

[Client.list_world_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_world_export_jobs)

```python
def list_world_export_jobs(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListWorldExportJobsResponseTypeDef:
    pass
```

### list_world_generation_jobs

Type annotations for `boto3.client("robomaker").list_world_generation_jobs` method.

[Client.list_world_generation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_world_generation_jobs)

```python
def list_world_generation_jobs(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListWorldGenerationJobsResponseTypeDef:
    pass
```

### list_world_templates

Type annotations for `boto3.client("robomaker").list_world_templates` method.

[Client.list_world_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_world_templates)

```python
def list_world_templates(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListWorldTemplatesResponseTypeDef:
    pass
```

### list_worlds

Type annotations for `boto3.client("robomaker").list_worlds` method.

[Client.list_worlds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.list_worlds)

```python
def list_worlds(
    self,
    nextToken: str = None,
    maxResults: int = None,
    filters: List[FilterTypeDef] = None
) -> ListWorldsResponseTypeDef:
    pass
```

### register_robot

Type annotations for `boto3.client("robomaker").register_robot` method.

[Client.register_robot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.register_robot)

```python
def register_robot(
    self,
    fleet: str,
    robot: str
) -> RegisterRobotResponseTypeDef:
    pass
```

### restart_simulation_job

Type annotations for `boto3.client("robomaker").restart_simulation_job` method.

[Client.restart_simulation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.restart_simulation_job)

```python
def restart_simulation_job(
    self,
    job: str
) -> Dict[str, Any]:
    pass
```

### start_simulation_job_batch

Type annotations for `boto3.client("robomaker").start_simulation_job_batch` method.

[Client.start_simulation_job_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.start_simulation_job_batch)

```python
def start_simulation_job_batch(
    self,
    createSimulationJobRequests: List["SimulationJobRequestTypeDef"],
    clientRequestToken: str = None,
    batchPolicy: "BatchPolicyTypeDef" = None,
    tags: Dict[str, str] = None
) -> StartSimulationJobBatchResponseTypeDef:
    pass
```

### sync_deployment_job

Type annotations for `boto3.client("robomaker").sync_deployment_job` method.

[Client.sync_deployment_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.sync_deployment_job)

```python
def sync_deployment_job(
    self,
    clientRequestToken: str,
    fleet: str
) -> SyncDeploymentJobResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("robomaker").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("robomaker").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_robot_application

Type annotations for `boto3.client("robomaker").update_robot_application` method.

[Client.update_robot_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.update_robot_application)

```python
def update_robot_application(
    self,
    application: str,
    sources: List[SourceConfigTypeDef],
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
    currentRevisionId: str = None
) -> UpdateRobotApplicationResponseTypeDef:
    pass
```

### update_simulation_application

Type annotations for `boto3.client("robomaker").update_simulation_application` method.

[Client.update_simulation_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.update_simulation_application)

```python
def update_simulation_application(
    self,
    application: str,
    sources: List[SourceConfigTypeDef],
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef",
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
    renderingEngine: "RenderingEngineTypeDef" = None,
    currentRevisionId: str = None
) -> UpdateSimulationApplicationResponseTypeDef:
    pass
```

### update_world_template

Type annotations for `boto3.client("robomaker").update_world_template` method.

[Client.update_world_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker.Client.update_world_template)

```python
def update_world_template(
    self,
    template: str,
    name: str = None,
    templateBody: str = None,
    templateLocation: TemplateLocationTypeDef = None
) -> UpdateWorldTemplateResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("robomaker").get_paginator` method with overloads.

- `client.get_paginator("list_deployment_jobs")` -> [ListDeploymentJobsPaginator](./paginators.md#listdeploymentjobspaginator)
- `client.get_paginator("list_fleets")` -> [ListFleetsPaginator](./paginators.md#listfleetspaginator)
- `client.get_paginator("list_robot_applications")` -> [ListRobotApplicationsPaginator](./paginators.md#listrobotapplicationspaginator)
- `client.get_paginator("list_robots")` -> [ListRobotsPaginator](./paginators.md#listrobotspaginator)
- `client.get_paginator("list_simulation_applications")` -> [ListSimulationApplicationsPaginator](./paginators.md#listsimulationapplicationspaginator)
- `client.get_paginator("list_simulation_job_batches")` -> [ListSimulationJobBatchesPaginator](./paginators.md#listsimulationjobbatchespaginator)
- `client.get_paginator("list_simulation_jobs")` -> [ListSimulationJobsPaginator](./paginators.md#listsimulationjobspaginator)
- `client.get_paginator("list_world_export_jobs")` -> [ListWorldExportJobsPaginator](./paginators.md#listworldexportjobspaginator)
- `client.get_paginator("list_world_generation_jobs")` -> [ListWorldGenerationJobsPaginator](./paginators.md#listworldgenerationjobspaginator)
- `client.get_paginator("list_world_templates")` -> [ListWorldTemplatesPaginator](./paginators.md#listworldtemplatespaginator)
- `client.get_paginator("list_worlds")` -> [ListWorldsPaginator](./paginators.md#listworldspaginator)


