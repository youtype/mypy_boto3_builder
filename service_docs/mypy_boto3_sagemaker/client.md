# SageMakerClient for boto3 SageMaker module

> [Index](../index.md) > [SageMaker](./index.md) > SageMakerClient

Auto-generated documentation for [SageMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker)
type annotations stubs module [mypy_boto3_sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/).

- [SageMakerClient for boto3 SageMaker module](#sagemakerclient-for-boto3-sagemaker-module)
  - [SageMakerClient](#sagemakerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_association](#add_association)
    - [add_tags](#add_tags)
    - [associate_trial_component](#associate_trial_component)
    - [can_paginate](#can_paginate)
    - [create_action](#create_action)
    - [create_algorithm](#create_algorithm)
    - [create_app](#create_app)
    - [create_app_image_config](#create_app_image_config)
    - [create_artifact](#create_artifact)
    - [create_auto_ml_job](#create_auto_ml_job)
    - [create_code_repository](#create_code_repository)
    - [create_compilation_job](#create_compilation_job)
    - [create_context](#create_context)
    - [create_data_quality_job_definition](#create_data_quality_job_definition)
    - [create_device_fleet](#create_device_fleet)
    - [create_domain](#create_domain)
    - [create_edge_packaging_job](#create_edge_packaging_job)
    - [create_endpoint](#create_endpoint)
    - [create_endpoint_config](#create_endpoint_config)
    - [create_experiment](#create_experiment)
    - [create_feature_group](#create_feature_group)
    - [create_flow_definition](#create_flow_definition)
    - [create_human_task_ui](#create_human_task_ui)
    - [create_hyper_parameter_tuning_job](#create_hyper_parameter_tuning_job)
    - [create_image](#create_image)
    - [create_image_version](#create_image_version)
    - [create_labeling_job](#create_labeling_job)
    - [create_model](#create_model)
    - [create_model_bias_job_definition](#create_model_bias_job_definition)
    - [create_model_explainability_job_definition](#create_model_explainability_job_definition)
    - [create_model_package](#create_model_package)
    - [create_model_package_group](#create_model_package_group)
    - [create_model_quality_job_definition](#create_model_quality_job_definition)
    - [create_monitoring_schedule](#create_monitoring_schedule)
    - [create_notebook_instance](#create_notebook_instance)
    - [create_notebook_instance_lifecycle_config](#create_notebook_instance_lifecycle_config)
    - [create_pipeline](#create_pipeline)
    - [create_presigned_domain_url](#create_presigned_domain_url)
    - [create_presigned_notebook_instance_url](#create_presigned_notebook_instance_url)
    - [create_processing_job](#create_processing_job)
    - [create_project](#create_project)
    - [create_training_job](#create_training_job)
    - [create_transform_job](#create_transform_job)
    - [create_trial](#create_trial)
    - [create_trial_component](#create_trial_component)
    - [create_user_profile](#create_user_profile)
    - [create_workforce](#create_workforce)
    - [create_workteam](#create_workteam)
    - [delete_action](#delete_action)
    - [delete_algorithm](#delete_algorithm)
    - [delete_app](#delete_app)
    - [delete_app_image_config](#delete_app_image_config)
    - [delete_artifact](#delete_artifact)
    - [delete_association](#delete_association)
    - [delete_code_repository](#delete_code_repository)
    - [delete_context](#delete_context)
    - [delete_data_quality_job_definition](#delete_data_quality_job_definition)
    - [delete_device_fleet](#delete_device_fleet)
    - [delete_domain](#delete_domain)
    - [delete_endpoint](#delete_endpoint)
    - [delete_endpoint_config](#delete_endpoint_config)
    - [delete_experiment](#delete_experiment)
    - [delete_feature_group](#delete_feature_group)
    - [delete_flow_definition](#delete_flow_definition)
    - [delete_human_task_ui](#delete_human_task_ui)
    - [delete_image](#delete_image)
    - [delete_image_version](#delete_image_version)
    - [delete_model](#delete_model)
    - [delete_model_bias_job_definition](#delete_model_bias_job_definition)
    - [delete_model_explainability_job_definition](#delete_model_explainability_job_definition)
    - [delete_model_package](#delete_model_package)
    - [delete_model_package_group](#delete_model_package_group)
    - [delete_model_package_group_policy](#delete_model_package_group_policy)
    - [delete_model_quality_job_definition](#delete_model_quality_job_definition)
    - [delete_monitoring_schedule](#delete_monitoring_schedule)
    - [delete_notebook_instance](#delete_notebook_instance)
    - [delete_notebook_instance_lifecycle_config](#delete_notebook_instance_lifecycle_config)
    - [delete_pipeline](#delete_pipeline)
    - [delete_project](#delete_project)
    - [delete_tags](#delete_tags)
    - [delete_trial](#delete_trial)
    - [delete_trial_component](#delete_trial_component)
    - [delete_user_profile](#delete_user_profile)
    - [delete_workforce](#delete_workforce)
    - [delete_workteam](#delete_workteam)
    - [deregister_devices](#deregister_devices)
    - [describe_action](#describe_action)
    - [describe_algorithm](#describe_algorithm)
    - [describe_app](#describe_app)
    - [describe_app_image_config](#describe_app_image_config)
    - [describe_artifact](#describe_artifact)
    - [describe_auto_ml_job](#describe_auto_ml_job)
    - [describe_code_repository](#describe_code_repository)
    - [describe_compilation_job](#describe_compilation_job)
    - [describe_context](#describe_context)
    - [describe_data_quality_job_definition](#describe_data_quality_job_definition)
    - [describe_device](#describe_device)
    - [describe_device_fleet](#describe_device_fleet)
    - [describe_domain](#describe_domain)
    - [describe_edge_packaging_job](#describe_edge_packaging_job)
    - [describe_endpoint](#describe_endpoint)
    - [describe_endpoint_config](#describe_endpoint_config)
    - [describe_experiment](#describe_experiment)
    - [describe_feature_group](#describe_feature_group)
    - [describe_flow_definition](#describe_flow_definition)
    - [describe_human_task_ui](#describe_human_task_ui)
    - [describe_hyper_parameter_tuning_job](#describe_hyper_parameter_tuning_job)
    - [describe_image](#describe_image)
    - [describe_image_version](#describe_image_version)
    - [describe_labeling_job](#describe_labeling_job)
    - [describe_model](#describe_model)
    - [describe_model_bias_job_definition](#describe_model_bias_job_definition)
    - [describe_model_explainability_job_definition](#describe_model_explainability_job_definition)
    - [describe_model_package](#describe_model_package)
    - [describe_model_package_group](#describe_model_package_group)
    - [describe_model_quality_job_definition](#describe_model_quality_job_definition)
    - [describe_monitoring_schedule](#describe_monitoring_schedule)
    - [describe_notebook_instance](#describe_notebook_instance)
    - [describe_notebook_instance_lifecycle_config](#describe_notebook_instance_lifecycle_config)
    - [describe_pipeline](#describe_pipeline)
    - [describe_pipeline_definition_for_execution](#describe_pipeline_definition_for_execution)
    - [describe_pipeline_execution](#describe_pipeline_execution)
    - [describe_processing_job](#describe_processing_job)
    - [describe_project](#describe_project)
    - [describe_subscribed_workteam](#describe_subscribed_workteam)
    - [describe_training_job](#describe_training_job)
    - [describe_transform_job](#describe_transform_job)
    - [describe_trial](#describe_trial)
    - [describe_trial_component](#describe_trial_component)
    - [describe_user_profile](#describe_user_profile)
    - [describe_workforce](#describe_workforce)
    - [describe_workteam](#describe_workteam)
    - [disable_sagemaker_servicecatalog_portfolio](#disable_sagemaker_servicecatalog_portfolio)
    - [disassociate_trial_component](#disassociate_trial_component)
    - [enable_sagemaker_servicecatalog_portfolio](#enable_sagemaker_servicecatalog_portfolio)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_device_fleet_report](#get_device_fleet_report)
    - [get_model_package_group_policy](#get_model_package_group_policy)
    - [get_sagemaker_servicecatalog_portfolio_status](#get_sagemaker_servicecatalog_portfolio_status)
    - [get_search_suggestions](#get_search_suggestions)
    - [list_actions](#list_actions)
    - [list_algorithms](#list_algorithms)
    - [list_app_image_configs](#list_app_image_configs)
    - [list_apps](#list_apps)
    - [list_artifacts](#list_artifacts)
    - [list_associations](#list_associations)
    - [list_auto_ml_jobs](#list_auto_ml_jobs)
    - [list_candidates_for_auto_ml_job](#list_candidates_for_auto_ml_job)
    - [list_code_repositories](#list_code_repositories)
    - [list_compilation_jobs](#list_compilation_jobs)
    - [list_contexts](#list_contexts)
    - [list_data_quality_job_definitions](#list_data_quality_job_definitions)
    - [list_device_fleets](#list_device_fleets)
    - [list_devices](#list_devices)
    - [list_domains](#list_domains)
    - [list_edge_packaging_jobs](#list_edge_packaging_jobs)
    - [list_endpoint_configs](#list_endpoint_configs)
    - [list_endpoints](#list_endpoints)
    - [list_experiments](#list_experiments)
    - [list_feature_groups](#list_feature_groups)
    - [list_flow_definitions](#list_flow_definitions)
    - [list_human_task_uis](#list_human_task_uis)
    - [list_hyper_parameter_tuning_jobs](#list_hyper_parameter_tuning_jobs)
    - [list_image_versions](#list_image_versions)
    - [list_images](#list_images)
    - [list_labeling_jobs](#list_labeling_jobs)
    - [list_labeling_jobs_for_workteam](#list_labeling_jobs_for_workteam)
    - [list_model_bias_job_definitions](#list_model_bias_job_definitions)
    - [list_model_explainability_job_definitions](#list_model_explainability_job_definitions)
    - [list_model_package_groups](#list_model_package_groups)
    - [list_model_packages](#list_model_packages)
    - [list_model_quality_job_definitions](#list_model_quality_job_definitions)
    - [list_models](#list_models)
    - [list_monitoring_executions](#list_monitoring_executions)
    - [list_monitoring_schedules](#list_monitoring_schedules)
    - [list_notebook_instance_lifecycle_configs](#list_notebook_instance_lifecycle_configs)
    - [list_notebook_instances](#list_notebook_instances)
    - [list_pipeline_execution_steps](#list_pipeline_execution_steps)
    - [list_pipeline_executions](#list_pipeline_executions)
    - [list_pipeline_parameters_for_execution](#list_pipeline_parameters_for_execution)
    - [list_pipelines](#list_pipelines)
    - [list_processing_jobs](#list_processing_jobs)
    - [list_projects](#list_projects)
    - [list_subscribed_workteams](#list_subscribed_workteams)
    - [list_tags](#list_tags)
    - [list_training_jobs](#list_training_jobs)
    - [list_training_jobs_for_hyper_parameter_tuning_job](#list_training_jobs_for_hyper_parameter_tuning_job)
    - [list_transform_jobs](#list_transform_jobs)
    - [list_trial_components](#list_trial_components)
    - [list_trials](#list_trials)
    - [list_user_profiles](#list_user_profiles)
    - [list_workforces](#list_workforces)
    - [list_workteams](#list_workteams)
    - [put_model_package_group_policy](#put_model_package_group_policy)
    - [register_devices](#register_devices)
    - [render_ui_template](#render_ui_template)
    - [search](#search)
    - [start_monitoring_schedule](#start_monitoring_schedule)
    - [start_notebook_instance](#start_notebook_instance)
    - [start_pipeline_execution](#start_pipeline_execution)
    - [stop_auto_ml_job](#stop_auto_ml_job)
    - [stop_compilation_job](#stop_compilation_job)
    - [stop_edge_packaging_job](#stop_edge_packaging_job)
    - [stop_hyper_parameter_tuning_job](#stop_hyper_parameter_tuning_job)
    - [stop_labeling_job](#stop_labeling_job)
    - [stop_monitoring_schedule](#stop_monitoring_schedule)
    - [stop_notebook_instance](#stop_notebook_instance)
    - [stop_pipeline_execution](#stop_pipeline_execution)
    - [stop_processing_job](#stop_processing_job)
    - [stop_training_job](#stop_training_job)
    - [stop_transform_job](#stop_transform_job)
    - [update_action](#update_action)
    - [update_app_image_config](#update_app_image_config)
    - [update_artifact](#update_artifact)
    - [update_code_repository](#update_code_repository)
    - [update_context](#update_context)
    - [update_device_fleet](#update_device_fleet)
    - [update_devices](#update_devices)
    - [update_domain](#update_domain)
    - [update_endpoint](#update_endpoint)
    - [update_endpoint_weights_and_capacities](#update_endpoint_weights_and_capacities)
    - [update_experiment](#update_experiment)
    - [update_image](#update_image)
    - [update_model_package](#update_model_package)
    - [update_monitoring_schedule](#update_monitoring_schedule)
    - [update_notebook_instance](#update_notebook_instance)
    - [update_notebook_instance_lifecycle_config](#update_notebook_instance_lifecycle_config)
    - [update_pipeline](#update_pipeline)
    - [update_pipeline_execution](#update_pipeline_execution)
    - [update_training_job](#update_training_job)
    - [update_trial](#update_trial)
    - [update_trial_component](#update_trial_component)
    - [update_user_profile](#update_user_profile)
    - [update_workforce](#update_workforce)
    - [update_workteam](#update_workteam)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## SageMakerClient

Type annotations for `boto3.client("sagemaker")`

Can be used directly:

```python
from mypy_boto3_sagemaker.client import SageMakerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sagemaker.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ResourceInUse`
- `Exceptions.ResourceLimitExceeded`
- `Exceptions.ResourceNotFound`


## Methods


### add_association

Type annotations for `boto3.client("sagemaker").add_association` method.

[Client.add_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.add_association)

```python
def add_association(
    self,
    SourceArn: str,
    DestinationArn: str,
    AssociationType: AssociationEdgeType = None
) -> AddAssociationResponseTypeDef:
    pass
```

### add_tags

Type annotations for `boto3.client("sagemaker").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.add_tags)

```python
def add_tags(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> AddTagsOutputTypeDef:
    pass
```

### associate_trial_component

Type annotations for `boto3.client("sagemaker").associate_trial_component` method.

[Client.associate_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)

```python
def associate_trial_component(
    self,
    TrialComponentName: str,
    TrialName: str
) -> AssociateTrialComponentResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("sagemaker").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_action

Type annotations for `boto3.client("sagemaker").create_action` method.

[Client.create_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_action)

```python
def create_action(
    self,
    ActionName: str,
    Source: "ActionSourceTypeDef",
    ActionType: str,
    Description: str = None,
    Status: ActionStatus = None,
    Properties: Dict[str, str] = None,
    MetadataProperties: "MetadataPropertiesTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateActionResponseTypeDef:
    pass
```

### create_algorithm

Type annotations for `boto3.client("sagemaker").create_algorithm` method.

[Client.create_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)

```python
def create_algorithm(
    self,
    AlgorithmName: str,
    TrainingSpecification: "TrainingSpecificationTypeDef",
    AlgorithmDescription: str = None,
    InferenceSpecification: "InferenceSpecificationTypeDef" = None,
    ValidationSpecification: "AlgorithmValidationSpecificationTypeDef" = None,
    CertifyForMarketplace: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAlgorithmOutputTypeDef:
    pass
```

### create_app

Type annotations for `boto3.client("sagemaker").create_app` method.

[Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app)

```python
def create_app(
    self,
    DomainId: str,
    UserProfileName: str,
    AppType: AppType,
    AppName: str,
    Tags: List["TagTypeDef"] = None,
    ResourceSpec: "ResourceSpecTypeDef" = None
) -> CreateAppResponseTypeDef:
    pass
```

### create_app_image_config

Type annotations for `boto3.client("sagemaker").create_app_image_config` method.

[Client.create_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config)

```python
def create_app_image_config(
    self,
    AppImageConfigName: str,
    Tags: List["TagTypeDef"] = None,
    KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None
) -> CreateAppImageConfigResponseTypeDef:
    pass
```

### create_artifact

Type annotations for `boto3.client("sagemaker").create_artifact` method.

[Client.create_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_artifact)

```python
def create_artifact(
    self,
    Source: "ArtifactSourceTypeDef",
    ArtifactType: str,
    ArtifactName: str = None,
    Properties: Dict[str, str] = None,
    MetadataProperties: "MetadataPropertiesTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateArtifactResponseTypeDef:
    pass
```

### create_auto_ml_job

Type annotations for `boto3.client("sagemaker").create_auto_ml_job` method.

[Client.create_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)

```python
def create_auto_ml_job(
    self,
    AutoMLJobName: str,
    InputDataConfig: List["AutoMLChannelTypeDef"],
    OutputDataConfig: "AutoMLOutputDataConfigTypeDef",
    RoleArn: str,
    ProblemType: ProblemType = None,
    AutoMLJobObjective: "AutoMLJobObjectiveTypeDef" = None,
    AutoMLJobConfig: "AutoMLJobConfigTypeDef" = None,
    GenerateCandidateDefinitionsOnly: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAutoMLJobResponseTypeDef:
    pass
```

### create_code_repository

Type annotations for `boto3.client("sagemaker").create_code_repository` method.

[Client.create_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)

```python
def create_code_repository(
    self,
    CodeRepositoryName: str,
    GitConfig: "GitConfigTypeDef",
    Tags: List["TagTypeDef"] = None
) -> CreateCodeRepositoryOutputTypeDef:
    pass
```

### create_compilation_job

Type annotations for `boto3.client("sagemaker").create_compilation_job` method.

[Client.create_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)

```python
def create_compilation_job(
    self,
    CompilationJobName: str,
    RoleArn: str,
    InputConfig: "InputConfigTypeDef",
    OutputConfig: "OutputConfigTypeDef",
    StoppingCondition: "StoppingConditionTypeDef",
    Tags: List["TagTypeDef"] = None
) -> CreateCompilationJobResponseTypeDef:
    pass
```

### create_context

Type annotations for `boto3.client("sagemaker").create_context` method.

[Client.create_context documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_context)

```python
def create_context(
    self,
    ContextName: str,
    Source: "ContextSourceTypeDef",
    ContextType: str,
    Description: str = None,
    Properties: Dict[str, str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateContextResponseTypeDef:
    pass
```

### create_data_quality_job_definition

Type annotations for `boto3.client("sagemaker").create_data_quality_job_definition` method.

[Client.create_data_quality_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_data_quality_job_definition)

```python
def create_data_quality_job_definition(
    self,
    JobDefinitionName: str,
    DataQualityAppSpecification: "DataQualityAppSpecificationTypeDef",
    DataQualityJobInput: "DataQualityJobInputTypeDef",
    DataQualityJobOutputConfig: "MonitoringOutputConfigTypeDef",
    JobResources: "MonitoringResourcesTypeDef",
    RoleArn: str,
    DataQualityBaselineConfig: "DataQualityBaselineConfigTypeDef" = None,
    NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
    StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDataQualityJobDefinitionResponseTypeDef:
    pass
```

### create_device_fleet

Type annotations for `boto3.client("sagemaker").create_device_fleet` method.

[Client.create_device_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_device_fleet)

```python
def create_device_fleet(
    self,
    DeviceFleetName: str,
    OutputConfig: "EdgeOutputConfigTypeDef",
    RoleArn: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> None:
    pass
```

### create_domain

Type annotations for `boto3.client("sagemaker").create_domain` method.

[Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_domain)

```python
def create_domain(
    self,
    DomainName: str,
    AuthMode: AuthMode,
    DefaultUserSettings: "UserSettingsTypeDef",
    SubnetIds: List[str],
    VpcId: str,
    Tags: List["TagTypeDef"] = None,
    AppNetworkAccessType: AppNetworkAccessType = None,
    HomeEfsFileSystemKmsKeyId: str = None,
    KmsKeyId: str = None
) -> CreateDomainResponseTypeDef:
    pass
```

### create_edge_packaging_job

Type annotations for `boto3.client("sagemaker").create_edge_packaging_job` method.

[Client.create_edge_packaging_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_edge_packaging_job)

```python
def create_edge_packaging_job(
    self,
    EdgePackagingJobName: str,
    CompilationJobName: str,
    ModelName: str,
    ModelVersion: str,
    RoleArn: str,
    OutputConfig: "EdgeOutputConfigTypeDef",
    ResourceKey: str = None,
    Tags: List["TagTypeDef"] = None
) -> None:
    pass
```

### create_endpoint

Type annotations for `boto3.client("sagemaker").create_endpoint` method.

[Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)

```python
def create_endpoint(
    self,
    EndpointName: str,
    EndpointConfigName: str,
    Tags: List["TagTypeDef"] = None
) -> CreateEndpointOutputTypeDef:
    pass
```

### create_endpoint_config

Type annotations for `boto3.client("sagemaker").create_endpoint_config` method.

[Client.create_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)

```python
def create_endpoint_config(
    self,
    EndpointConfigName: str,
    ProductionVariants: List["ProductionVariantTypeDef"],
    DataCaptureConfig: "DataCaptureConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    KmsKeyId: str = None
) -> CreateEndpointConfigOutputTypeDef:
    pass
```

### create_experiment

Type annotations for `boto3.client("sagemaker").create_experiment` method.

[Client.create_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_experiment)

```python
def create_experiment(
    self,
    ExperimentName: str,
    DisplayName: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateExperimentResponseTypeDef:
    pass
```

### create_feature_group

Type annotations for `boto3.client("sagemaker").create_feature_group` method.

[Client.create_feature_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_feature_group)

```python
def create_feature_group(
    self,
    FeatureGroupName: str,
    RecordIdentifierFeatureName: str,
    EventTimeFeatureName: str,
    FeatureDefinitions: List["FeatureDefinitionTypeDef"],
    OnlineStoreConfig: "OnlineStoreConfigTypeDef" = None,
    OfflineStoreConfig: "OfflineStoreConfigTypeDef" = None,
    RoleArn: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateFeatureGroupResponseTypeDef:
    pass
```

### create_flow_definition

Type annotations for `boto3.client("sagemaker").create_flow_definition` method.

[Client.create_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)

```python
def create_flow_definition(
    self,
    FlowDefinitionName: str,
    HumanLoopConfig: "HumanLoopConfigTypeDef",
    OutputConfig: "FlowDefinitionOutputConfigTypeDef",
    RoleArn: str,
    HumanLoopRequestSource: "HumanLoopRequestSourceTypeDef" = None,
    HumanLoopActivationConfig: "HumanLoopActivationConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateFlowDefinitionResponseTypeDef:
    pass
```

### create_human_task_ui

Type annotations for `boto3.client("sagemaker").create_human_task_ui` method.

[Client.create_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)

```python
def create_human_task_ui(
    self,
    HumanTaskUiName: str,
    UiTemplate: UiTemplateTypeDef,
    Tags: List["TagTypeDef"] = None
) -> CreateHumanTaskUiResponseTypeDef:
    pass
```

### create_hyper_parameter_tuning_job

Type annotations for `boto3.client("sagemaker").create_hyper_parameter_tuning_job` method.

[Client.create_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)

```python
def create_hyper_parameter_tuning_job(
    self,
    HyperParameterTuningJobName: str,
    HyperParameterTuningJobConfig: "HyperParameterTuningJobConfigTypeDef",
    TrainingJobDefinition: "HyperParameterTrainingJobDefinitionTypeDef" = None,
    TrainingJobDefinitions: List["HyperParameterTrainingJobDefinitionTypeDef"] = None,
    WarmStartConfig: "HyperParameterTuningJobWarmStartConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateHyperParameterTuningJobResponseTypeDef:
    pass
```

### create_image

Type annotations for `boto3.client("sagemaker").create_image` method.

[Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image)

```python
def create_image(
    self,
    ImageName: str,
    RoleArn: str,
    Description: str = None,
    DisplayName: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateImageResponseTypeDef:
    pass
```

### create_image_version

Type annotations for `boto3.client("sagemaker").create_image_version` method.

[Client.create_image_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image_version)

```python
def create_image_version(
    self,
    BaseImage: str,
    ClientToken: str,
    ImageName: str
) -> CreateImageVersionResponseTypeDef:
    pass
```

### create_labeling_job

Type annotations for `boto3.client("sagemaker").create_labeling_job` method.

[Client.create_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)

```python
def create_labeling_job(
    self,
    LabelingJobName: str,
    LabelAttributeName: str,
    InputConfig: "LabelingJobInputConfigTypeDef",
    OutputConfig: "LabelingJobOutputConfigTypeDef",
    RoleArn: str,
    HumanTaskConfig: "HumanTaskConfigTypeDef",
    LabelCategoryConfigS3Uri: str = None,
    StoppingConditions: "LabelingJobStoppingConditionsTypeDef" = None,
    LabelingJobAlgorithmsConfig: "LabelingJobAlgorithmsConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateLabelingJobResponseTypeDef:
    pass
```

### create_model

Type annotations for `boto3.client("sagemaker").create_model` method.

[Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model)

```python
def create_model(
    self,
    ModelName: str,
    ExecutionRoleArn: str,
    PrimaryContainer: "ContainerDefinitionTypeDef" = None,
    Containers: List["ContainerDefinitionTypeDef"] = None,
    InferenceExecutionConfig: "InferenceExecutionConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    EnableNetworkIsolation: bool = None
) -> CreateModelOutputTypeDef:
    pass
```

### create_model_bias_job_definition

Type annotations for `boto3.client("sagemaker").create_model_bias_job_definition` method.

[Client.create_model_bias_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_bias_job_definition)

```python
def create_model_bias_job_definition(
    self,
    JobDefinitionName: str,
    ModelBiasAppSpecification: "ModelBiasAppSpecificationTypeDef",
    ModelBiasJobInput: "ModelBiasJobInputTypeDef",
    ModelBiasJobOutputConfig: "MonitoringOutputConfigTypeDef",
    JobResources: "MonitoringResourcesTypeDef",
    RoleArn: str,
    ModelBiasBaselineConfig: "ModelBiasBaselineConfigTypeDef" = None,
    NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
    StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateModelBiasJobDefinitionResponseTypeDef:
    pass
```

### create_model_explainability_job_definition

Type annotations for `boto3.client("sagemaker").create_model_explainability_job_definition` method.

[Client.create_model_explainability_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_explainability_job_definition)

```python
def create_model_explainability_job_definition(
    self,
    JobDefinitionName: str,
    ModelExplainabilityAppSpecification: "ModelExplainabilityAppSpecificationTypeDef",
    ModelExplainabilityJobInput: "ModelExplainabilityJobInputTypeDef",
    ModelExplainabilityJobOutputConfig: "MonitoringOutputConfigTypeDef",
    JobResources: "MonitoringResourcesTypeDef",
    RoleArn: str,
    ModelExplainabilityBaselineConfig: "ModelExplainabilityBaselineConfigTypeDef" = None,
    NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
    StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateModelExplainabilityJobDefinitionResponseTypeDef:
    pass
```

### create_model_package

Type annotations for `boto3.client("sagemaker").create_model_package` method.

[Client.create_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_package)

```python
def create_model_package(
    self,
    ModelPackageName: str = None,
    ModelPackageGroupName: str = None,
    ModelPackageDescription: str = None,
    InferenceSpecification: "InferenceSpecificationTypeDef" = None,
    ValidationSpecification: "ModelPackageValidationSpecificationTypeDef" = None,
    SourceAlgorithmSpecification: "SourceAlgorithmSpecificationTypeDef" = None,
    CertifyForMarketplace: bool = None,
    Tags: List["TagTypeDef"] = None,
    ModelApprovalStatus: ModelApprovalStatus = None,
    MetadataProperties: "MetadataPropertiesTypeDef" = None,
    ModelMetrics: "ModelMetricsTypeDef" = None,
    ClientToken: str = None
) -> CreateModelPackageOutputTypeDef:
    pass
```

### create_model_package_group

Type annotations for `boto3.client("sagemaker").create_model_package_group` method.

[Client.create_model_package_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_package_group)

```python
def create_model_package_group(
    self,
    ModelPackageGroupName: str,
    ModelPackageGroupDescription: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateModelPackageGroupOutputTypeDef:
    pass
```

### create_model_quality_job_definition

Type annotations for `boto3.client("sagemaker").create_model_quality_job_definition` method.

[Client.create_model_quality_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model_quality_job_definition)

```python
def create_model_quality_job_definition(
    self,
    JobDefinitionName: str,
    ModelQualityAppSpecification: "ModelQualityAppSpecificationTypeDef",
    ModelQualityJobInput: "ModelQualityJobInputTypeDef",
    ModelQualityJobOutputConfig: "MonitoringOutputConfigTypeDef",
    JobResources: "MonitoringResourcesTypeDef",
    RoleArn: str,
    ModelQualityBaselineConfig: "ModelQualityBaselineConfigTypeDef" = None,
    NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
    StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateModelQualityJobDefinitionResponseTypeDef:
    pass
```

### create_monitoring_schedule

Type annotations for `boto3.client("sagemaker").create_monitoring_schedule` method.

[Client.create_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)

```python
def create_monitoring_schedule(
    self,
    MonitoringScheduleName: str,
    MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef",
    Tags: List["TagTypeDef"] = None
) -> CreateMonitoringScheduleResponseTypeDef:
    pass
```

### create_notebook_instance

Type annotations for `boto3.client("sagemaker").create_notebook_instance` method.

[Client.create_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)

```python
def create_notebook_instance(
    self,
    NotebookInstanceName: str,
    InstanceType: InstanceType,
    RoleArn: str,
    SubnetId: str = None,
    SecurityGroupIds: List[str] = None,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None,
    LifecycleConfigName: str = None,
    DirectInternetAccess: DirectInternetAccess = None,
    VolumeSizeInGB: int = None,
    AcceleratorTypes: List[NotebookInstanceAcceleratorType] = None,
    DefaultCodeRepository: str = None,
    AdditionalCodeRepositories: List[str] = None,
    RootAccess: RootAccess = None
) -> CreateNotebookInstanceOutputTypeDef:
    pass
```

### create_notebook_instance_lifecycle_config

Type annotations for `boto3.client("sagemaker").create_notebook_instance_lifecycle_config` method.

[Client.create_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)

```python
def create_notebook_instance_lifecycle_config(
    self,
    NotebookInstanceLifecycleConfigName: str,
    OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
    OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None
) -> CreateNotebookInstanceLifecycleConfigOutputTypeDef:
    pass
```

### create_pipeline

Type annotations for `boto3.client("sagemaker").create_pipeline` method.

[Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_pipeline)

```python
def create_pipeline(
    self,
    PipelineName: str,
    PipelineDefinition: str,
    ClientRequestToken: str,
    RoleArn: str,
    PipelineDisplayName: str = None,
    PipelineDescription: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreatePipelineResponseTypeDef:
    pass
```

### create_presigned_domain_url

Type annotations for `boto3.client("sagemaker").create_presigned_domain_url` method.

[Client.create_presigned_domain_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)

```python
def create_presigned_domain_url(
    self,
    DomainId: str,
    UserProfileName: str,
    SessionExpirationDurationInSeconds: int = None,
    ExpiresInSeconds: int = None
) -> CreatePresignedDomainUrlResponseTypeDef:
    pass
```

### create_presigned_notebook_instance_url

Type annotations for `boto3.client("sagemaker").create_presigned_notebook_instance_url` method.

[Client.create_presigned_notebook_instance_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)

```python
def create_presigned_notebook_instance_url(
    self,
    NotebookInstanceName: str,
    SessionExpirationDurationInSeconds: int = None
) -> CreatePresignedNotebookInstanceUrlOutputTypeDef:
    pass
```

### create_processing_job

Type annotations for `boto3.client("sagemaker").create_processing_job` method.

[Client.create_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)

```python
def create_processing_job(
    self,
    ProcessingJobName: str,
    ProcessingResources: "ProcessingResourcesTypeDef",
    AppSpecification: "AppSpecificationTypeDef",
    RoleArn: str,
    ProcessingInputs: List["ProcessingInputTypeDef"] = None,
    ProcessingOutputConfig: "ProcessingOutputConfigTypeDef" = None,
    StoppingCondition: "ProcessingStoppingConditionTypeDef" = None,
    Environment: Dict[str, str] = None,
    NetworkConfig: "NetworkConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    ExperimentConfig: "ExperimentConfigTypeDef" = None
) -> CreateProcessingJobResponseTypeDef:
    pass
```

### create_project

Type annotations for `boto3.client("sagemaker").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_project)

```python
def create_project(
    self,
    ProjectName: str,
    ServiceCatalogProvisioningDetails: "ServiceCatalogProvisioningDetailsTypeDef",
    ProjectDescription: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateProjectOutputTypeDef:
    pass
```

### create_training_job

Type annotations for `boto3.client("sagemaker").create_training_job` method.

[Client.create_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_training_job)

```python
def create_training_job(
    self,
    TrainingJobName: str,
    AlgorithmSpecification: "AlgorithmSpecificationTypeDef",
    RoleArn: str,
    OutputDataConfig: "OutputDataConfigTypeDef",
    ResourceConfig: "ResourceConfigTypeDef",
    StoppingCondition: "StoppingConditionTypeDef",
    HyperParameters: Dict[str, str] = None,
    InputDataConfig: List["ChannelTypeDef"] = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    EnableNetworkIsolation: bool = None,
    EnableInterContainerTrafficEncryption: bool = None,
    EnableManagedSpotTraining: bool = None,
    CheckpointConfig: "CheckpointConfigTypeDef" = None,
    DebugHookConfig: "DebugHookConfigTypeDef" = None,
    DebugRuleConfigurations: List["DebugRuleConfigurationTypeDef"] = None,
    TensorBoardOutputConfig: "TensorBoardOutputConfigTypeDef" = None,
    ExperimentConfig: "ExperimentConfigTypeDef" = None,
    ProfilerConfig: "ProfilerConfigTypeDef" = None,
    ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"] = None,
    Environment: Dict[str, str] = None
) -> CreateTrainingJobResponseTypeDef:
    pass
```

### create_transform_job

Type annotations for `boto3.client("sagemaker").create_transform_job` method.

[Client.create_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)

```python
def create_transform_job(
    self,
    TransformJobName: str,
    ModelName: str,
    TransformInput: "TransformInputTypeDef",
    TransformOutput: "TransformOutputTypeDef",
    TransformResources: "TransformResourcesTypeDef",
    MaxConcurrentTransforms: int = None,
    ModelClientConfig: "ModelClientConfigTypeDef" = None,
    MaxPayloadInMB: int = None,
    BatchStrategy: BatchStrategy = None,
    Environment: Dict[str, str] = None,
    DataProcessing: "DataProcessingTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    ExperimentConfig: "ExperimentConfigTypeDef" = None
) -> CreateTransformJobResponseTypeDef:
    pass
```

### create_trial

Type annotations for `boto3.client("sagemaker").create_trial` method.

[Client.create_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_trial)

```python
def create_trial(
    self,
    TrialName: str,
    ExperimentName: str,
    DisplayName: str = None,
    MetadataProperties: "MetadataPropertiesTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTrialResponseTypeDef:
    pass
```

### create_trial_component

Type annotations for `boto3.client("sagemaker").create_trial_component` method.

[Client.create_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)

```python
def create_trial_component(
    self,
    TrialComponentName: str,
    DisplayName: str = None,
    Status: "TrialComponentStatusTypeDef" = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
    InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
    OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
    MetadataProperties: "MetadataPropertiesTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTrialComponentResponseTypeDef:
    pass
```

### create_user_profile

Type annotations for `boto3.client("sagemaker").create_user_profile` method.

[Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)

```python
def create_user_profile(
    self,
    DomainId: str,
    UserProfileName: str,
    SingleSignOnUserIdentifier: str = None,
    SingleSignOnUserValue: str = None,
    Tags: List["TagTypeDef"] = None,
    UserSettings: "UserSettingsTypeDef" = None
) -> CreateUserProfileResponseTypeDef:
    pass
```

### create_workforce

Type annotations for `boto3.client("sagemaker").create_workforce` method.

[Client.create_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_workforce)

```python
def create_workforce(
    self,
    WorkforceName: str,
    CognitoConfig: "CognitoConfigTypeDef" = None,
    OidcConfig: OidcConfigTypeDef = None,
    SourceIpConfig: "SourceIpConfigTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateWorkforceResponseTypeDef:
    pass
```

### create_workteam

Type annotations for `boto3.client("sagemaker").create_workteam` method.

[Client.create_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_workteam)

```python
def create_workteam(
    self,
    WorkteamName: str,
    MemberDefinitions: List["MemberDefinitionTypeDef"],
    Description: str,
    WorkforceName: str = None,
    NotificationConfiguration: "NotificationConfigurationTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateWorkteamResponseTypeDef:
    pass
```

### delete_action

Type annotations for `boto3.client("sagemaker").delete_action` method.

[Client.delete_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_action)

```python
def delete_action(
    self,
    ActionName: str
) -> DeleteActionResponseTypeDef:
    pass
```

### delete_algorithm

Type annotations for `boto3.client("sagemaker").delete_algorithm` method.

[Client.delete_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)

```python
def delete_algorithm(
    self,
    AlgorithmName: str
) -> None:
    pass
```

### delete_app

Type annotations for `boto3.client("sagemaker").delete_app` method.

[Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app)

```python
def delete_app(
    self,
    DomainId: str,
    UserProfileName: str,
    AppType: AppType,
    AppName: str
) -> None:
    pass
```

### delete_app_image_config

Type annotations for `boto3.client("sagemaker").delete_app_image_config` method.

[Client.delete_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config)

```python
def delete_app_image_config(
    self,
    AppImageConfigName: str
) -> None:
    pass
```

### delete_artifact

Type annotations for `boto3.client("sagemaker").delete_artifact` method.

[Client.delete_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_artifact)

```python
def delete_artifact(
    self,
    ArtifactArn: str = None,
    Source: "ArtifactSourceTypeDef" = None
) -> DeleteArtifactResponseTypeDef:
    pass
```

### delete_association

Type annotations for `boto3.client("sagemaker").delete_association` method.

[Client.delete_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_association)

```python
def delete_association(
    self,
    SourceArn: str,
    DestinationArn: str
) -> DeleteAssociationResponseTypeDef:
    pass
```

### delete_code_repository

Type annotations for `boto3.client("sagemaker").delete_code_repository` method.

[Client.delete_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)

```python
def delete_code_repository(
    self,
    CodeRepositoryName: str
) -> None:
    pass
```

### delete_context

Type annotations for `boto3.client("sagemaker").delete_context` method.

[Client.delete_context documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_context)

```python
def delete_context(
    self,
    ContextName: str
) -> DeleteContextResponseTypeDef:
    pass
```

### delete_data_quality_job_definition

Type annotations for `boto3.client("sagemaker").delete_data_quality_job_definition` method.

[Client.delete_data_quality_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_data_quality_job_definition)

```python
def delete_data_quality_job_definition(
    self,
    JobDefinitionName: str
) -> None:
    pass
```

### delete_device_fleet

Type annotations for `boto3.client("sagemaker").delete_device_fleet` method.

[Client.delete_device_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_device_fleet)

```python
def delete_device_fleet(
    self,
    DeviceFleetName: str
) -> None:
    pass
```

### delete_domain

Type annotations for `boto3.client("sagemaker").delete_domain` method.

[Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_domain)

```python
def delete_domain(
    self,
    DomainId: str,
    RetentionPolicy: RetentionPolicyTypeDef = None
) -> None:
    pass
```

### delete_endpoint

Type annotations for `boto3.client("sagemaker").delete_endpoint` method.

[Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)

```python
def delete_endpoint(
    self,
    EndpointName: str
) -> None:
    pass
```

### delete_endpoint_config

Type annotations for `boto3.client("sagemaker").delete_endpoint_config` method.

[Client.delete_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)

```python
def delete_endpoint_config(
    self,
    EndpointConfigName: str
) -> None:
    pass
```

### delete_experiment

Type annotations for `boto3.client("sagemaker").delete_experiment` method.

[Client.delete_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)

```python
def delete_experiment(
    self,
    ExperimentName: str
) -> DeleteExperimentResponseTypeDef:
    pass
```

### delete_feature_group

Type annotations for `boto3.client("sagemaker").delete_feature_group` method.

[Client.delete_feature_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_feature_group)

```python
def delete_feature_group(
    self,
    FeatureGroupName: str
) -> None:
    pass
```

### delete_flow_definition

Type annotations for `boto3.client("sagemaker").delete_flow_definition` method.

[Client.delete_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)

```python
def delete_flow_definition(
    self,
    FlowDefinitionName: str
) -> Dict[str, Any]:
    pass
```

### delete_human_task_ui

Type annotations for `boto3.client("sagemaker").delete_human_task_ui` method.

[Client.delete_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_human_task_ui)

```python
def delete_human_task_ui(
    self,
    HumanTaskUiName: str
) -> Dict[str, Any]:
    pass
```

### delete_image

Type annotations for `boto3.client("sagemaker").delete_image` method.

[Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_image)

```python
def delete_image(
    self,
    ImageName: str
) -> Dict[str, Any]:
    pass
```

### delete_image_version

Type annotations for `boto3.client("sagemaker").delete_image_version` method.

[Client.delete_image_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_image_version)

```python
def delete_image_version(
    self,
    ImageName: str,
    Version: int
) -> Dict[str, Any]:
    pass
```

### delete_model

Type annotations for `boto3.client("sagemaker").delete_model` method.

[Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model)

```python
def delete_model(
    self,
    ModelName: str
) -> None:
    pass
```

### delete_model_bias_job_definition

Type annotations for `boto3.client("sagemaker").delete_model_bias_job_definition` method.

[Client.delete_model_bias_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_bias_job_definition)

```python
def delete_model_bias_job_definition(
    self,
    JobDefinitionName: str
) -> None:
    pass
```

### delete_model_explainability_job_definition

Type annotations for `boto3.client("sagemaker").delete_model_explainability_job_definition` method.

[Client.delete_model_explainability_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_explainability_job_definition)

```python
def delete_model_explainability_job_definition(
    self,
    JobDefinitionName: str
) -> None:
    pass
```

### delete_model_package

Type annotations for `boto3.client("sagemaker").delete_model_package` method.

[Client.delete_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)

```python
def delete_model_package(
    self,
    ModelPackageName: str
) -> None:
    pass
```

### delete_model_package_group

Type annotations for `boto3.client("sagemaker").delete_model_package_group` method.

[Client.delete_model_package_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group)

```python
def delete_model_package_group(
    self,
    ModelPackageGroupName: str
) -> None:
    pass
```

### delete_model_package_group_policy

Type annotations for `boto3.client("sagemaker").delete_model_package_group_policy` method.

[Client.delete_model_package_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group_policy)

```python
def delete_model_package_group_policy(
    self,
    ModelPackageGroupName: str
) -> None:
    pass
```

### delete_model_quality_job_definition

Type annotations for `boto3.client("sagemaker").delete_model_quality_job_definition` method.

[Client.delete_model_quality_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_model_quality_job_definition)

```python
def delete_model_quality_job_definition(
    self,
    JobDefinitionName: str
) -> None:
    pass
```

### delete_monitoring_schedule

Type annotations for `boto3.client("sagemaker").delete_monitoring_schedule` method.

[Client.delete_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)

```python
def delete_monitoring_schedule(
    self,
    MonitoringScheduleName: str
) -> None:
    pass
```

### delete_notebook_instance

Type annotations for `boto3.client("sagemaker").delete_notebook_instance` method.

[Client.delete_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)

```python
def delete_notebook_instance(
    self,
    NotebookInstanceName: str
) -> None:
    pass
```

### delete_notebook_instance_lifecycle_config

Type annotations for `boto3.client("sagemaker").delete_notebook_instance_lifecycle_config` method.

[Client.delete_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)

```python
def delete_notebook_instance_lifecycle_config(
    self,
    NotebookInstanceLifecycleConfigName: str
) -> None:
    pass
```

### delete_pipeline

Type annotations for `boto3.client("sagemaker").delete_pipeline` method.

[Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_pipeline)

```python
def delete_pipeline(
    self,
    PipelineName: str,
    ClientRequestToken: str
) -> DeletePipelineResponseTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("sagemaker").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_project)

```python
def delete_project(
    self,
    ProjectName: str
) -> None:
    pass
```

### delete_tags

Type annotations for `boto3.client("sagemaker").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_tags)

```python
def delete_tags(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### delete_trial

Type annotations for `boto3.client("sagemaker").delete_trial` method.

[Client.delete_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_trial)

```python
def delete_trial(
    self,
    TrialName: str
) -> DeleteTrialResponseTypeDef:
    pass
```

### delete_trial_component

Type annotations for `boto3.client("sagemaker").delete_trial_component` method.

[Client.delete_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)

```python
def delete_trial_component(
    self,
    TrialComponentName: str
) -> DeleteTrialComponentResponseTypeDef:
    pass
```

### delete_user_profile

Type annotations for `boto3.client("sagemaker").delete_user_profile` method.

[Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)

```python
def delete_user_profile(
    self,
    DomainId: str,
    UserProfileName: str
) -> None:
    pass
```

### delete_workforce

Type annotations for `boto3.client("sagemaker").delete_workforce` method.

[Client.delete_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_workforce)

```python
def delete_workforce(
    self,
    WorkforceName: str
) -> Dict[str, Any]:
    pass
```

### delete_workteam

Type annotations for `boto3.client("sagemaker").delete_workteam` method.

[Client.delete_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)

```python
def delete_workteam(
    self,
    WorkteamName: str
) -> DeleteWorkteamResponseTypeDef:
    pass
```

### deregister_devices

Type annotations for `boto3.client("sagemaker").deregister_devices` method.

[Client.deregister_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.deregister_devices)

```python
def deregister_devices(
    self,
    DeviceFleetName: str,
    DeviceNames: List[str]
) -> None:
    pass
```

### describe_action

Type annotations for `boto3.client("sagemaker").describe_action` method.

[Client.describe_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_action)

```python
def describe_action(
    self,
    ActionName: str
) -> DescribeActionResponseTypeDef:
    pass
```

### describe_algorithm

Type annotations for `boto3.client("sagemaker").describe_algorithm` method.

[Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)

```python
def describe_algorithm(
    self,
    AlgorithmName: str
) -> DescribeAlgorithmOutputTypeDef:
    pass
```

### describe_app

Type annotations for `boto3.client("sagemaker").describe_app` method.

[Client.describe_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_app)

```python
def describe_app(
    self,
    DomainId: str,
    UserProfileName: str,
    AppType: AppType,
    AppName: str
) -> DescribeAppResponseTypeDef:
    pass
```

### describe_app_image_config

Type annotations for `boto3.client("sagemaker").describe_app_image_config` method.

[Client.describe_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_app_image_config)

```python
def describe_app_image_config(
    self,
    AppImageConfigName: str
) -> DescribeAppImageConfigResponseTypeDef:
    pass
```

### describe_artifact

Type annotations for `boto3.client("sagemaker").describe_artifact` method.

[Client.describe_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_artifact)

```python
def describe_artifact(
    self,
    ArtifactArn: str
) -> DescribeArtifactResponseTypeDef:
    pass
```

### describe_auto_ml_job

Type annotations for `boto3.client("sagemaker").describe_auto_ml_job` method.

[Client.describe_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)

```python
def describe_auto_ml_job(
    self,
    AutoMLJobName: str
) -> DescribeAutoMLJobResponseTypeDef:
    pass
```

### describe_code_repository

Type annotations for `boto3.client("sagemaker").describe_code_repository` method.

[Client.describe_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)

```python
def describe_code_repository(
    self,
    CodeRepositoryName: str
) -> DescribeCodeRepositoryOutputTypeDef:
    pass
```

### describe_compilation_job

Type annotations for `boto3.client("sagemaker").describe_compilation_job` method.

[Client.describe_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)

```python
def describe_compilation_job(
    self,
    CompilationJobName: str
) -> DescribeCompilationJobResponseTypeDef:
    pass
```

### describe_context

Type annotations for `boto3.client("sagemaker").describe_context` method.

[Client.describe_context documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_context)

```python
def describe_context(
    self,
    ContextName: str
) -> DescribeContextResponseTypeDef:
    pass
```

### describe_data_quality_job_definition

Type annotations for `boto3.client("sagemaker").describe_data_quality_job_definition` method.

[Client.describe_data_quality_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_data_quality_job_definition)

```python
def describe_data_quality_job_definition(
    self,
    JobDefinitionName: str
) -> DescribeDataQualityJobDefinitionResponseTypeDef:
    pass
```

### describe_device

Type annotations for `boto3.client("sagemaker").describe_device` method.

[Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_device)

```python
def describe_device(
    self,
    DeviceName: str,
    DeviceFleetName: str,
    NextToken: str = None
) -> DescribeDeviceResponseTypeDef:
    pass
```

### describe_device_fleet

Type annotations for `boto3.client("sagemaker").describe_device_fleet` method.

[Client.describe_device_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_device_fleet)

```python
def describe_device_fleet(
    self,
    DeviceFleetName: str
) -> DescribeDeviceFleetResponseTypeDef:
    pass
```

### describe_domain

Type annotations for `boto3.client("sagemaker").describe_domain` method.

[Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_domain)

```python
def describe_domain(
    self,
    DomainId: str
) -> DescribeDomainResponseTypeDef:
    pass
```

### describe_edge_packaging_job

Type annotations for `boto3.client("sagemaker").describe_edge_packaging_job` method.

[Client.describe_edge_packaging_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_edge_packaging_job)

```python
def describe_edge_packaging_job(
    self,
    EdgePackagingJobName: str
) -> DescribeEdgePackagingJobResponseTypeDef:
    pass
```

### describe_endpoint

Type annotations for `boto3.client("sagemaker").describe_endpoint` method.

[Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)

```python
def describe_endpoint(
    self,
    EndpointName: str
) -> DescribeEndpointOutputTypeDef:
    pass
```

### describe_endpoint_config

Type annotations for `boto3.client("sagemaker").describe_endpoint_config` method.

[Client.describe_endpoint_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)

```python
def describe_endpoint_config(
    self,
    EndpointConfigName: str
) -> DescribeEndpointConfigOutputTypeDef:
    pass
```

### describe_experiment

Type annotations for `boto3.client("sagemaker").describe_experiment` method.

[Client.describe_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)

```python
def describe_experiment(
    self,
    ExperimentName: str
) -> DescribeExperimentResponseTypeDef:
    pass
```

### describe_feature_group

Type annotations for `boto3.client("sagemaker").describe_feature_group` method.

[Client.describe_feature_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_feature_group)

```python
def describe_feature_group(
    self,
    FeatureGroupName: str,
    NextToken: str = None
) -> DescribeFeatureGroupResponseTypeDef:
    pass
```

### describe_flow_definition

Type annotations for `boto3.client("sagemaker").describe_flow_definition` method.

[Client.describe_flow_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)

```python
def describe_flow_definition(
    self,
    FlowDefinitionName: str
) -> DescribeFlowDefinitionResponseTypeDef:
    pass
```

### describe_human_task_ui

Type annotations for `boto3.client("sagemaker").describe_human_task_ui` method.

[Client.describe_human_task_ui documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)

```python
def describe_human_task_ui(
    self,
    HumanTaskUiName: str
) -> DescribeHumanTaskUiResponseTypeDef:
    pass
```

### describe_hyper_parameter_tuning_job

Type annotations for `boto3.client("sagemaker").describe_hyper_parameter_tuning_job` method.

[Client.describe_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)

```python
def describe_hyper_parameter_tuning_job(
    self,
    HyperParameterTuningJobName: str
) -> DescribeHyperParameterTuningJobResponseTypeDef:
    pass
```

### describe_image

Type annotations for `boto3.client("sagemaker").describe_image` method.

[Client.describe_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_image)

```python
def describe_image(
    self,
    ImageName: str
) -> DescribeImageResponseTypeDef:
    pass
```

### describe_image_version

Type annotations for `boto3.client("sagemaker").describe_image_version` method.

[Client.describe_image_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_image_version)

```python
def describe_image_version(
    self,
    ImageName: str,
    Version: int = None
) -> DescribeImageVersionResponseTypeDef:
    pass
```

### describe_labeling_job

Type annotations for `boto3.client("sagemaker").describe_labeling_job` method.

[Client.describe_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)

```python
def describe_labeling_job(
    self,
    LabelingJobName: str
) -> DescribeLabelingJobResponseTypeDef:
    pass
```

### describe_model

Type annotations for `boto3.client("sagemaker").describe_model` method.

[Client.describe_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model)

```python
def describe_model(
    self,
    ModelName: str
) -> DescribeModelOutputTypeDef:
    pass
```

### describe_model_bias_job_definition

Type annotations for `boto3.client("sagemaker").describe_model_bias_job_definition` method.

[Client.describe_model_bias_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_bias_job_definition)

```python
def describe_model_bias_job_definition(
    self,
    JobDefinitionName: str
) -> DescribeModelBiasJobDefinitionResponseTypeDef:
    pass
```

### describe_model_explainability_job_definition

Type annotations for `boto3.client("sagemaker").describe_model_explainability_job_definition` method.

[Client.describe_model_explainability_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_explainability_job_definition)

```python
def describe_model_explainability_job_definition(
    self,
    JobDefinitionName: str
) -> DescribeModelExplainabilityJobDefinitionResponseTypeDef:
    pass
```

### describe_model_package

Type annotations for `boto3.client("sagemaker").describe_model_package` method.

[Client.describe_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)

```python
def describe_model_package(
    self,
    ModelPackageName: str
) -> DescribeModelPackageOutputTypeDef:
    pass
```

### describe_model_package_group

Type annotations for `boto3.client("sagemaker").describe_model_package_group` method.

[Client.describe_model_package_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_package_group)

```python
def describe_model_package_group(
    self,
    ModelPackageGroupName: str
) -> DescribeModelPackageGroupOutputTypeDef:
    pass
```

### describe_model_quality_job_definition

Type annotations for `boto3.client("sagemaker").describe_model_quality_job_definition` method.

[Client.describe_model_quality_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_model_quality_job_definition)

```python
def describe_model_quality_job_definition(
    self,
    JobDefinitionName: str
) -> DescribeModelQualityJobDefinitionResponseTypeDef:
    pass
```

### describe_monitoring_schedule

Type annotations for `boto3.client("sagemaker").describe_monitoring_schedule` method.

[Client.describe_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)

```python
def describe_monitoring_schedule(
    self,
    MonitoringScheduleName: str
) -> DescribeMonitoringScheduleResponseTypeDef:
    pass
```

### describe_notebook_instance

Type annotations for `boto3.client("sagemaker").describe_notebook_instance` method.

[Client.describe_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)

```python
def describe_notebook_instance(
    self,
    NotebookInstanceName: str
) -> DescribeNotebookInstanceOutputTypeDef:
    pass
```

### describe_notebook_instance_lifecycle_config

Type annotations for `boto3.client("sagemaker").describe_notebook_instance_lifecycle_config` method.

[Client.describe_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)

```python
def describe_notebook_instance_lifecycle_config(
    self,
    NotebookInstanceLifecycleConfigName: str
) -> DescribeNotebookInstanceLifecycleConfigOutputTypeDef:
    pass
```

### describe_pipeline

Type annotations for `boto3.client("sagemaker").describe_pipeline` method.

[Client.describe_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline)

```python
def describe_pipeline(
    self,
    PipelineName: str
) -> DescribePipelineResponseTypeDef:
    pass
```

### describe_pipeline_definition_for_execution

Type annotations for `boto3.client("sagemaker").describe_pipeline_definition_for_execution` method.

[Client.describe_pipeline_definition_for_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_definition_for_execution)

```python
def describe_pipeline_definition_for_execution(
    self,
    PipelineExecutionArn: str
) -> DescribePipelineDefinitionForExecutionResponseTypeDef:
    pass
```

### describe_pipeline_execution

Type annotations for `boto3.client("sagemaker").describe_pipeline_execution` method.

[Client.describe_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_execution)

```python
def describe_pipeline_execution(
    self,
    PipelineExecutionArn: str
) -> DescribePipelineExecutionResponseTypeDef:
    pass
```

### describe_processing_job

Type annotations for `boto3.client("sagemaker").describe_processing_job` method.

[Client.describe_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)

```python
def describe_processing_job(
    self,
    ProcessingJobName: str
) -> DescribeProcessingJobResponseTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("sagemaker").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_project)

```python
def describe_project(
    self,
    ProjectName: str
) -> DescribeProjectOutputTypeDef:
    pass
```

### describe_subscribed_workteam

Type annotations for `boto3.client("sagemaker").describe_subscribed_workteam` method.

[Client.describe_subscribed_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)

```python
def describe_subscribed_workteam(
    self,
    WorkteamArn: str
) -> DescribeSubscribedWorkteamResponseTypeDef:
    pass
```

### describe_training_job

Type annotations for `boto3.client("sagemaker").describe_training_job` method.

[Client.describe_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)

```python
def describe_training_job(
    self,
    TrainingJobName: str
) -> DescribeTrainingJobResponseTypeDef:
    pass
```

### describe_transform_job

Type annotations for `boto3.client("sagemaker").describe_transform_job` method.

[Client.describe_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)

```python
def describe_transform_job(
    self,
    TransformJobName: str
) -> DescribeTransformJobResponseTypeDef:
    pass
```

### describe_trial

Type annotations for `boto3.client("sagemaker").describe_trial` method.

[Client.describe_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_trial)

```python
def describe_trial(
    self,
    TrialName: str
) -> DescribeTrialResponseTypeDef:
    pass
```

### describe_trial_component

Type annotations for `boto3.client("sagemaker").describe_trial_component` method.

[Client.describe_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)

```python
def describe_trial_component(
    self,
    TrialComponentName: str
) -> DescribeTrialComponentResponseTypeDef:
    pass
```

### describe_user_profile

Type annotations for `boto3.client("sagemaker").describe_user_profile` method.

[Client.describe_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)

```python
def describe_user_profile(
    self,
    DomainId: str,
    UserProfileName: str
) -> DescribeUserProfileResponseTypeDef:
    pass
```

### describe_workforce

Type annotations for `boto3.client("sagemaker").describe_workforce` method.

[Client.describe_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)

```python
def describe_workforce(
    self,
    WorkforceName: str
) -> DescribeWorkforceResponseTypeDef:
    pass
```

### describe_workteam

Type annotations for `boto3.client("sagemaker").describe_workteam` method.

[Client.describe_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)

```python
def describe_workteam(
    self,
    WorkteamName: str
) -> DescribeWorkteamResponseTypeDef:
    pass
```

### disable_sagemaker_servicecatalog_portfolio

Type annotations for `boto3.client("sagemaker").disable_sagemaker_servicecatalog_portfolio` method.

[Client.disable_sagemaker_servicecatalog_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.disable_sagemaker_servicecatalog_portfolio)

```python
def disable_sagemaker_servicecatalog_portfolio(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_trial_component

Type annotations for `boto3.client("sagemaker").disassociate_trial_component` method.

[Client.disassociate_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)

```python
def disassociate_trial_component(
    self,
    TrialComponentName: str,
    TrialName: str
) -> DisassociateTrialComponentResponseTypeDef:
    pass
```

### enable_sagemaker_servicecatalog_portfolio

Type annotations for `boto3.client("sagemaker").enable_sagemaker_servicecatalog_portfolio` method.

[Client.enable_sagemaker_servicecatalog_portfolio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.enable_sagemaker_servicecatalog_portfolio)

```python
def enable_sagemaker_servicecatalog_portfolio(
    self
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sagemaker").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)

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

### get_device_fleet_report

Type annotations for `boto3.client("sagemaker").get_device_fleet_report` method.

[Client.get_device_fleet_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_device_fleet_report)

```python
def get_device_fleet_report(
    self,
    DeviceFleetName: str
) -> GetDeviceFleetReportResponseTypeDef:
    pass
```

### get_model_package_group_policy

Type annotations for `boto3.client("sagemaker").get_model_package_group_policy` method.

[Client.get_model_package_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_model_package_group_policy)

```python
def get_model_package_group_policy(
    self,
    ModelPackageGroupName: str
) -> GetModelPackageGroupPolicyOutputTypeDef:
    pass
```

### get_sagemaker_servicecatalog_portfolio_status

Type annotations for `boto3.client("sagemaker").get_sagemaker_servicecatalog_portfolio_status` method.

[Client.get_sagemaker_servicecatalog_portfolio_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_sagemaker_servicecatalog_portfolio_status)

```python
def get_sagemaker_servicecatalog_portfolio_status(
    self
) -> GetSagemakerServicecatalogPortfolioStatusOutputTypeDef:
    pass
```

### get_search_suggestions

Type annotations for `boto3.client("sagemaker").get_search_suggestions` method.

[Client.get_search_suggestions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)

```python
def get_search_suggestions(
    self,
    Resource: ResourceType,
    SuggestionQuery: SuggestionQueryTypeDef = None
) -> GetSearchSuggestionsResponseTypeDef:
    pass
```

### list_actions

Type annotations for `boto3.client("sagemaker").list_actions` method.

[Client.list_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_actions)

```python
def list_actions(
    self,
    SourceUri: str = None,
    ActionType: str = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortActionsBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListActionsResponseTypeDef:
    pass
```

### list_algorithms

Type annotations for `boto3.client("sagemaker").list_algorithms` method.

[Client.list_algorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)

```python
def list_algorithms(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: AlgorithmSortBy = None,
    SortOrder: SortOrder = None
) -> ListAlgorithmsOutputTypeDef:
    pass
```

### list_app_image_configs

Type annotations for `boto3.client("sagemaker").list_app_image_configs` method.

[Client.list_app_image_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_app_image_configs)

```python
def list_app_image_configs(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    ModifiedTimeBefore: datetime = None,
    ModifiedTimeAfter: datetime = None,
    SortBy: AppImageConfigSortKey = None,
    SortOrder: SortOrder = None
) -> ListAppImageConfigsResponseTypeDef:
    pass
```

### list_apps

Type annotations for `boto3.client("sagemaker").list_apps` method.

[Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_apps)

```python
def list_apps(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    SortOrder: SortOrder = None,
    SortBy: Literal['CreationTime'] = None,
    DomainIdEquals: str = None,
    UserProfileNameEquals: str = None
) -> ListAppsResponseTypeDef:
    pass
```

### list_artifacts

Type annotations for `boto3.client("sagemaker").list_artifacts` method.

[Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_artifacts)

```python
def list_artifacts(
    self,
    SourceUri: str = None,
    ArtifactType: str = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: Literal['CreationTime'] = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListArtifactsResponseTypeDef:
    pass
```

### list_associations

Type annotations for `boto3.client("sagemaker").list_associations` method.

[Client.list_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_associations)

```python
def list_associations(
    self,
    SourceArn: str = None,
    DestinationArn: str = None,
    SourceType: str = None,
    DestinationType: str = None,
    AssociationType: AssociationEdgeType = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortAssociationsBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAssociationsResponseTypeDef:
    pass
```

### list_auto_ml_jobs

Type annotations for `boto3.client("sagemaker").list_auto_ml_jobs` method.

[Client.list_auto_ml_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)

```python
def list_auto_ml_jobs(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: AutoMLJobStatus = None,
    SortOrder: AutoMLSortOrder = None,
    SortBy: AutoMLSortBy = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAutoMLJobsResponseTypeDef:
    pass
```

### list_candidates_for_auto_ml_job

Type annotations for `boto3.client("sagemaker").list_candidates_for_auto_ml_job` method.

[Client.list_candidates_for_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)

```python
def list_candidates_for_auto_ml_job(
    self,
    AutoMLJobName: str,
    StatusEquals: CandidateStatus = None,
    CandidateNameEquals: str = None,
    SortOrder: AutoMLSortOrder = None,
    SortBy: CandidateSortBy = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCandidatesForAutoMLJobResponseTypeDef:
    pass
```

### list_code_repositories

Type annotations for `boto3.client("sagemaker").list_code_repositories` method.

[Client.list_code_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)

```python
def list_code_repositories(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: CodeRepositorySortBy = None,
    SortOrder: CodeRepositorySortOrder = None
) -> ListCodeRepositoriesOutputTypeDef:
    pass
```

### list_compilation_jobs

Type annotations for `boto3.client("sagemaker").list_compilation_jobs` method.

[Client.list_compilation_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)

```python
def list_compilation_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: CompilationJobStatus = None,
    SortBy: ListCompilationJobsSortBy = None,
    SortOrder: SortOrder = None
) -> ListCompilationJobsResponseTypeDef:
    pass
```

### list_contexts

Type annotations for `boto3.client("sagemaker").list_contexts` method.

[Client.list_contexts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_contexts)

```python
def list_contexts(
    self,
    SourceUri: str = None,
    ContextType: str = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortContextsBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListContextsResponseTypeDef:
    pass
```

### list_data_quality_job_definitions

Type annotations for `boto3.client("sagemaker").list_data_quality_job_definitions` method.

[Client.list_data_quality_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_data_quality_job_definitions)

```python
def list_data_quality_job_definitions(
    self,
    EndpointName: str = None,
    SortBy: MonitoringJobDefinitionSortKey = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None
) -> ListDataQualityJobDefinitionsResponseTypeDef:
    pass
```

### list_device_fleets

Type annotations for `boto3.client("sagemaker").list_device_fleets` method.

[Client.list_device_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_device_fleets)

```python
def list_device_fleets(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    SortBy: ListDeviceFleetsSortBy = None,
    SortOrder: SortOrder = None
) -> ListDeviceFleetsResponseTypeDef:
    pass
```

### list_devices

Type annotations for `boto3.client("sagemaker").list_devices` method.

[Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_devices)

```python
def list_devices(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    LatestHeartbeatAfter: datetime = None,
    ModelName: str = None,
    DeviceFleetName: str = None
) -> ListDevicesResponseTypeDef:
    pass
```

### list_domains

Type annotations for `boto3.client("sagemaker").list_domains` method.

[Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_domains)

```python
def list_domains(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDomainsResponseTypeDef:
    pass
```

### list_edge_packaging_jobs

Type annotations for `boto3.client("sagemaker").list_edge_packaging_jobs` method.

[Client.list_edge_packaging_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_edge_packaging_jobs)

```python
def list_edge_packaging_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    ModelNameContains: str = None,
    StatusEquals: EdgePackagingJobStatus = None,
    SortBy: ListEdgePackagingJobsSortBy = None,
    SortOrder: SortOrder = None
) -> ListEdgePackagingJobsResponseTypeDef:
    pass
```

### list_endpoint_configs

Type annotations for `boto3.client("sagemaker").list_endpoint_configs` method.

[Client.list_endpoint_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)

```python
def list_endpoint_configs(
    self,
    SortBy: EndpointConfigSortKey = None,
    SortOrder: OrderKey = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None
) -> ListEndpointConfigsOutputTypeDef:
    pass
```

### list_endpoints

Type annotations for `boto3.client("sagemaker").list_endpoints` method.

[Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)

```python
def list_endpoints(
    self,
    SortBy: EndpointSortKey = None,
    SortOrder: OrderKey = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    StatusEquals: EndpointStatus = None
) -> ListEndpointsOutputTypeDef:
    pass
```

### list_experiments

Type annotations for `boto3.client("sagemaker").list_experiments` method.

[Client.list_experiments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_experiments)

```python
def list_experiments(
    self,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortExperimentsBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListExperimentsResponseTypeDef:
    pass
```

### list_feature_groups

Type annotations for `boto3.client("sagemaker").list_feature_groups` method.

[Client.list_feature_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_feature_groups)

```python
def list_feature_groups(
    self,
    NameContains: str = None,
    FeatureGroupStatusEquals: FeatureGroupStatus = None,
    OfflineStoreStatusEquals: OfflineStoreStatusValue = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    SortOrder: FeatureGroupSortOrder = None,
    SortBy: FeatureGroupSortBy = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFeatureGroupsResponseTypeDef:
    pass
```

### list_flow_definitions

Type annotations for `boto3.client("sagemaker").list_flow_definitions` method.

[Client.list_flow_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)

```python
def list_flow_definitions(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFlowDefinitionsResponseTypeDef:
    pass
```

### list_human_task_uis

Type annotations for `boto3.client("sagemaker").list_human_task_uis` method.

[Client.list_human_task_uis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)

```python
def list_human_task_uis(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHumanTaskUisResponseTypeDef:
    pass
```

### list_hyper_parameter_tuning_jobs

Type annotations for `boto3.client("sagemaker").list_hyper_parameter_tuning_jobs` method.

[Client.list_hyper_parameter_tuning_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)

```python
def list_hyper_parameter_tuning_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: HyperParameterTuningJobSortByOptions = None,
    SortOrder: SortOrder = None,
    NameContains: str = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    StatusEquals: HyperParameterTuningJobStatus = None
) -> ListHyperParameterTuningJobsResponseTypeDef:
    pass
```

### list_image_versions

Type annotations for `boto3.client("sagemaker").list_image_versions` method.

[Client.list_image_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_image_versions)

```python
def list_image_versions(
    self,
    ImageName: str,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: ImageVersionSortBy = None,
    SortOrder: ImageVersionSortOrder = None
) -> ListImageVersionsResponseTypeDef:
    pass
```

### list_images

Type annotations for `boto3.client("sagemaker").list_images` method.

[Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_images)

```python
def list_images(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: ImageSortBy = None,
    SortOrder: ImageSortOrder = None
) -> ListImagesResponseTypeDef:
    pass
```

### list_labeling_jobs

Type annotations for `boto3.client("sagemaker").list_labeling_jobs` method.

[Client.list_labeling_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)

```python
def list_labeling_jobs(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    MaxResults: int = None,
    NextToken: str = None,
    NameContains: str = None,
    SortBy: SortBy = None,
    SortOrder: SortOrder = None,
    StatusEquals: LabelingJobStatus = None
) -> ListLabelingJobsResponseTypeDef:
    pass
```

### list_labeling_jobs_for_workteam

Type annotations for `boto3.client("sagemaker").list_labeling_jobs_for_workteam` method.

[Client.list_labeling_jobs_for_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)

```python
def list_labeling_jobs_for_workteam(
    self,
    WorkteamArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    JobReferenceCodeContains: str = None,
    SortBy: Literal['CreationTime'] = None,
    SortOrder: SortOrder = None
) -> ListLabelingJobsForWorkteamResponseTypeDef:
    pass
```

### list_model_bias_job_definitions

Type annotations for `boto3.client("sagemaker").list_model_bias_job_definitions` method.

[Client.list_model_bias_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_bias_job_definitions)

```python
def list_model_bias_job_definitions(
    self,
    EndpointName: str = None,
    SortBy: MonitoringJobDefinitionSortKey = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None
) -> ListModelBiasJobDefinitionsResponseTypeDef:
    pass
```

### list_model_explainability_job_definitions

Type annotations for `boto3.client("sagemaker").list_model_explainability_job_definitions` method.

[Client.list_model_explainability_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_explainability_job_definitions)

```python
def list_model_explainability_job_definitions(
    self,
    EndpointName: str = None,
    SortBy: MonitoringJobDefinitionSortKey = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None
) -> ListModelExplainabilityJobDefinitionsResponseTypeDef:
    pass
```

### list_model_package_groups

Type annotations for `boto3.client("sagemaker").list_model_package_groups` method.

[Client.list_model_package_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_package_groups)

```python
def list_model_package_groups(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: ModelPackageGroupSortBy = None,
    SortOrder: SortOrder = None
) -> ListModelPackageGroupsOutputTypeDef:
    pass
```

### list_model_packages

Type annotations for `boto3.client("sagemaker").list_model_packages` method.

[Client.list_model_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)

```python
def list_model_packages(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    ModelApprovalStatus: ModelApprovalStatus = None,
    ModelPackageGroupName: str = None,
    ModelPackageType: ModelPackageType = None,
    NextToken: str = None,
    SortBy: ModelPackageSortBy = None,
    SortOrder: SortOrder = None
) -> ListModelPackagesOutputTypeDef:
    pass
```

### list_model_quality_job_definitions

Type annotations for `boto3.client("sagemaker").list_model_quality_job_definitions` method.

[Client.list_model_quality_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_model_quality_job_definitions)

```python
def list_model_quality_job_definitions(
    self,
    EndpointName: str = None,
    SortBy: MonitoringJobDefinitionSortKey = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None
) -> ListModelQualityJobDefinitionsResponseTypeDef:
    pass
```

### list_models

Type annotations for `boto3.client("sagemaker").list_models` method.

[Client.list_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_models)

```python
def list_models(
    self,
    SortBy: ModelSortKey = None,
    SortOrder: OrderKey = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None
) -> ListModelsOutputTypeDef:
    pass
```

### list_monitoring_executions

Type annotations for `boto3.client("sagemaker").list_monitoring_executions` method.

[Client.list_monitoring_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)

```python
def list_monitoring_executions(
    self,
    MonitoringScheduleName: str = None,
    EndpointName: str = None,
    SortBy: MonitoringExecutionSortKey = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None,
    ScheduledTimeBefore: datetime = None,
    ScheduledTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    StatusEquals: ExecutionStatus = None,
    MonitoringJobDefinitionName: str = None,
    MonitoringTypeEquals: MonitoringType = None
) -> ListMonitoringExecutionsResponseTypeDef:
    pass
```

### list_monitoring_schedules

Type annotations for `boto3.client("sagemaker").list_monitoring_schedules` method.

[Client.list_monitoring_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)

```python
def list_monitoring_schedules(
    self,
    EndpointName: str = None,
    SortBy: MonitoringScheduleSortKey = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    StatusEquals: ScheduleStatus = None,
    MonitoringJobDefinitionName: str = None,
    MonitoringTypeEquals: MonitoringType = None
) -> ListMonitoringSchedulesResponseTypeDef:
    pass
```

### list_notebook_instance_lifecycle_configs

Type annotations for `boto3.client("sagemaker").list_notebook_instance_lifecycle_configs` method.

[Client.list_notebook_instance_lifecycle_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)

```python
def list_notebook_instance_lifecycle_configs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: NotebookInstanceLifecycleConfigSortKey = None,
    SortOrder: NotebookInstanceLifecycleConfigSortOrder = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None
) -> ListNotebookInstanceLifecycleConfigsOutputTypeDef:
    pass
```

### list_notebook_instances

Type annotations for `boto3.client("sagemaker").list_notebook_instances` method.

[Client.list_notebook_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)

```python
def list_notebook_instances(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: NotebookInstanceSortKey = None,
    SortOrder: NotebookInstanceSortOrder = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    StatusEquals: NotebookInstanceStatus = None,
    NotebookInstanceLifecycleConfigNameContains: str = None,
    DefaultCodeRepositoryContains: str = None,
    AdditionalCodeRepositoryEquals: str = None
) -> ListNotebookInstancesOutputTypeDef:
    pass
```

### list_pipeline_execution_steps

Type annotations for `boto3.client("sagemaker").list_pipeline_execution_steps` method.

[Client.list_pipeline_execution_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_execution_steps)

```python
def list_pipeline_execution_steps(
    self,
    PipelineExecutionArn: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    SortOrder: SortOrder = None
) -> ListPipelineExecutionStepsResponseTypeDef:
    pass
```

### list_pipeline_executions

Type annotations for `boto3.client("sagemaker").list_pipeline_executions` method.

[Client.list_pipeline_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_executions)

```python
def list_pipeline_executions(
    self,
    PipelineName: str,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortPipelineExecutionsBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPipelineExecutionsResponseTypeDef:
    pass
```

### list_pipeline_parameters_for_execution

Type annotations for `boto3.client("sagemaker").list_pipeline_parameters_for_execution` method.

[Client.list_pipeline_parameters_for_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_parameters_for_execution)

```python
def list_pipeline_parameters_for_execution(
    self,
    PipelineExecutionArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPipelineParametersForExecutionResponseTypeDef:
    pass
```

### list_pipelines

Type annotations for `boto3.client("sagemaker").list_pipelines` method.

[Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_pipelines)

```python
def list_pipelines(
    self,
    PipelineNamePrefix: str = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortPipelinesBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPipelinesResponseTypeDef:
    pass
```

### list_processing_jobs

Type annotations for `boto3.client("sagemaker").list_processing_jobs` method.

[Client.list_processing_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)

```python
def list_processing_jobs(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: ProcessingJobStatus = None,
    SortBy: SortBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProcessingJobsResponseTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("sagemaker").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_projects)

```python
def list_projects(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: ProjectSortBy = None,
    SortOrder: ProjectSortOrder = None
) -> ListProjectsOutputTypeDef:
    pass
```

### list_subscribed_workteams

Type annotations for `boto3.client("sagemaker").list_subscribed_workteams` method.

[Client.list_subscribed_workteams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)

```python
def list_subscribed_workteams(
    self,
    NameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSubscribedWorkteamsResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("sagemaker").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_tags)

```python
def list_tags(
    self,
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsOutputTypeDef:
    pass
```

### list_training_jobs

Type annotations for `boto3.client("sagemaker").list_training_jobs` method.

[Client.list_training_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)

```python
def list_training_jobs(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: TrainingJobStatus = None,
    SortBy: SortBy = None,
    SortOrder: SortOrder = None
) -> ListTrainingJobsResponseTypeDef:
    pass
```

### list_training_jobs_for_hyper_parameter_tuning_job

Type annotations for `boto3.client("sagemaker").list_training_jobs_for_hyper_parameter_tuning_job` method.

[Client.list_training_jobs_for_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)

```python
def list_training_jobs_for_hyper_parameter_tuning_job(
    self,
    HyperParameterTuningJobName: str,
    NextToken: str = None,
    MaxResults: int = None,
    StatusEquals: TrainingJobStatus = None,
    SortBy: TrainingJobSortByOptions = None,
    SortOrder: SortOrder = None
) -> ListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
    pass
```

### list_transform_jobs

Type annotations for `boto3.client("sagemaker").list_transform_jobs` method.

[Client.list_transform_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)

```python
def list_transform_jobs(
    self,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: TransformJobStatus = None,
    SortBy: SortBy = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTransformJobsResponseTypeDef:
    pass
```

### list_trial_components

Type annotations for `boto3.client("sagemaker").list_trial_components` method.

[Client.list_trial_components documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)

```python
def list_trial_components(
    self,
    ExperimentName: str = None,
    TrialName: str = None,
    SourceArn: str = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortTrialComponentsBy = None,
    SortOrder: SortOrder = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTrialComponentsResponseTypeDef:
    pass
```

### list_trials

Type annotations for `boto3.client("sagemaker").list_trials` method.

[Client.list_trials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_trials)

```python
def list_trials(
    self,
    ExperimentName: str = None,
    TrialComponentName: str = None,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    SortBy: SortTrialsBy = None,
    SortOrder: SortOrder = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTrialsResponseTypeDef:
    pass
```

### list_user_profiles

Type annotations for `boto3.client("sagemaker").list_user_profiles` method.

[Client.list_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)

```python
def list_user_profiles(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    SortOrder: SortOrder = None,
    SortBy: UserProfileSortKey = None,
    DomainIdEquals: str = None,
    UserProfileNameContains: str = None
) -> ListUserProfilesResponseTypeDef:
    pass
```

### list_workforces

Type annotations for `boto3.client("sagemaker").list_workforces` method.

[Client.list_workforces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_workforces)

```python
def list_workforces(
    self,
    SortBy: ListWorkforcesSortByOptions = None,
    SortOrder: SortOrder = None,
    NameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkforcesResponseTypeDef:
    pass
```

### list_workteams

Type annotations for `boto3.client("sagemaker").list_workteams` method.

[Client.list_workteams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.list_workteams)

```python
def list_workteams(
    self,
    SortBy: ListWorkteamsSortByOptions = None,
    SortOrder: SortOrder = None,
    NameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkteamsResponseTypeDef:
    pass
```

### put_model_package_group_policy

Type annotations for `boto3.client("sagemaker").put_model_package_group_policy` method.

[Client.put_model_package_group_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.put_model_package_group_policy)

```python
def put_model_package_group_policy(
    self,
    ModelPackageGroupName: str,
    ResourcePolicy: str
) -> PutModelPackageGroupPolicyOutputTypeDef:
    pass
```

### register_devices

Type annotations for `boto3.client("sagemaker").register_devices` method.

[Client.register_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.register_devices)

```python
def register_devices(
    self,
    DeviceFleetName: str,
    Devices: List[DeviceTypeDef],
    Tags: List["TagTypeDef"] = None
) -> None:
    pass
```

### render_ui_template

Type annotations for `boto3.client("sagemaker").render_ui_template` method.

[Client.render_ui_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)

```python
def render_ui_template(
    self,
    Task: RenderableTaskTypeDef,
    RoleArn: str,
    UiTemplate: UiTemplateTypeDef = None,
    HumanTaskUiArn: str = None
) -> RenderUiTemplateResponseTypeDef:
    pass
```

### search

Type annotations for `boto3.client("sagemaker").search` method.

[Client.search documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.search)

```python
def search(
    self,
    Resource: ResourceType,
    SearchExpression: Dict[str, Any] = None,
    SortBy: str = None,
    SortOrder: SearchSortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> SearchResponseTypeDef:
    pass
```

### start_monitoring_schedule

Type annotations for `boto3.client("sagemaker").start_monitoring_schedule` method.

[Client.start_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)

```python
def start_monitoring_schedule(
    self,
    MonitoringScheduleName: str
) -> None:
    pass
```

### start_notebook_instance

Type annotations for `boto3.client("sagemaker").start_notebook_instance` method.

[Client.start_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)

```python
def start_notebook_instance(
    self,
    NotebookInstanceName: str
) -> None:
    pass
```

### start_pipeline_execution

Type annotations for `boto3.client("sagemaker").start_pipeline_execution` method.

[Client.start_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.start_pipeline_execution)

```python
def start_pipeline_execution(
    self,
    PipelineName: str,
    ClientRequestToken: str,
    PipelineExecutionDisplayName: str = None,
    PipelineParameters: List["ParameterTypeDef"] = None,
    PipelineExecutionDescription: str = None
) -> StartPipelineExecutionResponseTypeDef:
    pass
```

### stop_auto_ml_job

Type annotations for `boto3.client("sagemaker").stop_auto_ml_job` method.

[Client.stop_auto_ml_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)

```python
def stop_auto_ml_job(
    self,
    AutoMLJobName: str
) -> None:
    pass
```

### stop_compilation_job

Type annotations for `boto3.client("sagemaker").stop_compilation_job` method.

[Client.stop_compilation_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)

```python
def stop_compilation_job(
    self,
    CompilationJobName: str
) -> None:
    pass
```

### stop_edge_packaging_job

Type annotations for `boto3.client("sagemaker").stop_edge_packaging_job` method.

[Client.stop_edge_packaging_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_edge_packaging_job)

```python
def stop_edge_packaging_job(
    self,
    EdgePackagingJobName: str
) -> None:
    pass
```

### stop_hyper_parameter_tuning_job

Type annotations for `boto3.client("sagemaker").stop_hyper_parameter_tuning_job` method.

[Client.stop_hyper_parameter_tuning_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)

```python
def stop_hyper_parameter_tuning_job(
    self,
    HyperParameterTuningJobName: str
) -> None:
    pass
```

### stop_labeling_job

Type annotations for `boto3.client("sagemaker").stop_labeling_job` method.

[Client.stop_labeling_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)

```python
def stop_labeling_job(
    self,
    LabelingJobName: str
) -> None:
    pass
```

### stop_monitoring_schedule

Type annotations for `boto3.client("sagemaker").stop_monitoring_schedule` method.

[Client.stop_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)

```python
def stop_monitoring_schedule(
    self,
    MonitoringScheduleName: str
) -> None:
    pass
```

### stop_notebook_instance

Type annotations for `boto3.client("sagemaker").stop_notebook_instance` method.

[Client.stop_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)

```python
def stop_notebook_instance(
    self,
    NotebookInstanceName: str
) -> None:
    pass
```

### stop_pipeline_execution

Type annotations for `boto3.client("sagemaker").stop_pipeline_execution` method.

[Client.stop_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_pipeline_execution)

```python
def stop_pipeline_execution(
    self,
    PipelineExecutionArn: str,
    ClientRequestToken: str
) -> StopPipelineExecutionResponseTypeDef:
    pass
```

### stop_processing_job

Type annotations for `boto3.client("sagemaker").stop_processing_job` method.

[Client.stop_processing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)

```python
def stop_processing_job(
    self,
    ProcessingJobName: str
) -> None:
    pass
```

### stop_training_job

Type annotations for `boto3.client("sagemaker").stop_training_job` method.

[Client.stop_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)

```python
def stop_training_job(
    self,
    TrainingJobName: str
) -> None:
    pass
```

### stop_transform_job

Type annotations for `boto3.client("sagemaker").stop_transform_job` method.

[Client.stop_transform_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)

```python
def stop_transform_job(
    self,
    TransformJobName: str
) -> None:
    pass
```

### update_action

Type annotations for `boto3.client("sagemaker").update_action` method.

[Client.update_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_action)

```python
def update_action(
    self,
    ActionName: str,
    Description: str = None,
    Status: ActionStatus = None,
    Properties: Dict[str, str] = None,
    PropertiesToRemove: List[str] = None
) -> UpdateActionResponseTypeDef:
    pass
```

### update_app_image_config

Type annotations for `boto3.client("sagemaker").update_app_image_config` method.

[Client.update_app_image_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_app_image_config)

```python
def update_app_image_config(
    self,
    AppImageConfigName: str,
    KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None
) -> UpdateAppImageConfigResponseTypeDef:
    pass
```

### update_artifact

Type annotations for `boto3.client("sagemaker").update_artifact` method.

[Client.update_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_artifact)

```python
def update_artifact(
    self,
    ArtifactArn: str,
    ArtifactName: str = None,
    Properties: Dict[str, str] = None,
    PropertiesToRemove: List[str] = None
) -> UpdateArtifactResponseTypeDef:
    pass
```

### update_code_repository

Type annotations for `boto3.client("sagemaker").update_code_repository` method.

[Client.update_code_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)

```python
def update_code_repository(
    self,
    CodeRepositoryName: str,
    GitConfig: GitConfigForUpdateTypeDef = None
) -> UpdateCodeRepositoryOutputTypeDef:
    pass
```

### update_context

Type annotations for `boto3.client("sagemaker").update_context` method.

[Client.update_context documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_context)

```python
def update_context(
    self,
    ContextName: str,
    Description: str = None,
    Properties: Dict[str, str] = None,
    PropertiesToRemove: List[str] = None
) -> UpdateContextResponseTypeDef:
    pass
```

### update_device_fleet

Type annotations for `boto3.client("sagemaker").update_device_fleet` method.

[Client.update_device_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_device_fleet)

```python
def update_device_fleet(
    self,
    DeviceFleetName: str,
    OutputConfig: "EdgeOutputConfigTypeDef",
    RoleArn: str = None,
    Description: str = None
) -> None:
    pass
```

### update_devices

Type annotations for `boto3.client("sagemaker").update_devices` method.

[Client.update_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_devices)

```python
def update_devices(
    self,
    DeviceFleetName: str,
    Devices: List[DeviceTypeDef]
) -> None:
    pass
```

### update_domain

Type annotations for `boto3.client("sagemaker").update_domain` method.

[Client.update_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_domain)

```python
def update_domain(
    self,
    DomainId: str,
    DefaultUserSettings: "UserSettingsTypeDef" = None
) -> UpdateDomainResponseTypeDef:
    pass
```

### update_endpoint

Type annotations for `boto3.client("sagemaker").update_endpoint` method.

[Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)

```python
def update_endpoint(
    self,
    EndpointName: str,
    EndpointConfigName: str,
    RetainAllVariantProperties: bool = None,
    ExcludeRetainedVariantProperties: List[VariantPropertyTypeDef] = None,
    DeploymentConfig: "DeploymentConfigTypeDef" = None
) -> UpdateEndpointOutputTypeDef:
    pass
```

### update_endpoint_weights_and_capacities

Type annotations for `boto3.client("sagemaker").update_endpoint_weights_and_capacities` method.

[Client.update_endpoint_weights_and_capacities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)

```python
def update_endpoint_weights_and_capacities(
    self,
    EndpointName: str,
    DesiredWeightsAndCapacities: List[DesiredWeightAndCapacityTypeDef]
) -> UpdateEndpointWeightsAndCapacitiesOutputTypeDef:
    pass
```

### update_experiment

Type annotations for `boto3.client("sagemaker").update_experiment` method.

[Client.update_experiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_experiment)

```python
def update_experiment(
    self,
    ExperimentName: str,
    DisplayName: str = None,
    Description: str = None
) -> UpdateExperimentResponseTypeDef:
    pass
```

### update_image

Type annotations for `boto3.client("sagemaker").update_image` method.

[Client.update_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_image)

```python
def update_image(
    self,
    ImageName: str,
    DeleteProperties: List[str] = None,
    Description: str = None,
    DisplayName: str = None,
    RoleArn: str = None
) -> UpdateImageResponseTypeDef:
    pass
```

### update_model_package

Type annotations for `boto3.client("sagemaker").update_model_package` method.

[Client.update_model_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_model_package)

```python
def update_model_package(
    self,
    ModelPackageArn: str,
    ModelApprovalStatus: ModelApprovalStatus,
    ApprovalDescription: str = None
) -> UpdateModelPackageOutputTypeDef:
    pass
```

### update_monitoring_schedule

Type annotations for `boto3.client("sagemaker").update_monitoring_schedule` method.

[Client.update_monitoring_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)

```python
def update_monitoring_schedule(
    self,
    MonitoringScheduleName: str,
    MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef"
) -> UpdateMonitoringScheduleResponseTypeDef:
    pass
```

### update_notebook_instance

Type annotations for `boto3.client("sagemaker").update_notebook_instance` method.

[Client.update_notebook_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)

```python
def update_notebook_instance(
    self,
    NotebookInstanceName: str,
    InstanceType: InstanceType = None,
    RoleArn: str = None,
    LifecycleConfigName: str = None,
    DisassociateLifecycleConfig: bool = None,
    VolumeSizeInGB: int = None,
    DefaultCodeRepository: str = None,
    AdditionalCodeRepositories: List[str] = None,
    AcceleratorTypes: List[NotebookInstanceAcceleratorType] = None,
    DisassociateAcceleratorTypes: bool = None,
    DisassociateDefaultCodeRepository: bool = None,
    DisassociateAdditionalCodeRepositories: bool = None,
    RootAccess: RootAccess = None
) -> Dict[str, Any]:
    pass
```

### update_notebook_instance_lifecycle_config

Type annotations for `boto3.client("sagemaker").update_notebook_instance_lifecycle_config` method.

[Client.update_notebook_instance_lifecycle_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)

```python
def update_notebook_instance_lifecycle_config(
    self,
    NotebookInstanceLifecycleConfigName: str,
    OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
    OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### update_pipeline

Type annotations for `boto3.client("sagemaker").update_pipeline` method.

[Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_pipeline)

```python
def update_pipeline(
    self,
    PipelineName: str,
    PipelineDisplayName: str = None,
    PipelineDefinition: str = None,
    PipelineDescription: str = None,
    RoleArn: str = None
) -> UpdatePipelineResponseTypeDef:
    pass
```

### update_pipeline_execution

Type annotations for `boto3.client("sagemaker").update_pipeline_execution` method.

[Client.update_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_pipeline_execution)

```python
def update_pipeline_execution(
    self,
    PipelineExecutionArn: str,
    PipelineExecutionDescription: str = None,
    PipelineExecutionDisplayName: str = None
) -> UpdatePipelineExecutionResponseTypeDef:
    pass
```

### update_training_job

Type annotations for `boto3.client("sagemaker").update_training_job` method.

[Client.update_training_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_training_job)

```python
def update_training_job(
    self,
    TrainingJobName: str,
    ProfilerConfig: ProfilerConfigForUpdateTypeDef = None,
    ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"] = None
) -> UpdateTrainingJobResponseTypeDef:
    pass
```

### update_trial

Type annotations for `boto3.client("sagemaker").update_trial` method.

[Client.update_trial documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_trial)

```python
def update_trial(
    self,
    TrialName: str,
    DisplayName: str = None
) -> UpdateTrialResponseTypeDef:
    pass
```

### update_trial_component

Type annotations for `boto3.client("sagemaker").update_trial_component` method.

[Client.update_trial_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)

```python
def update_trial_component(
    self,
    TrialComponentName: str,
    DisplayName: str = None,
    Status: "TrialComponentStatusTypeDef" = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
    ParametersToRemove: List[str] = None,
    InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
    InputArtifactsToRemove: List[str] = None,
    OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
    OutputArtifactsToRemove: List[str] = None
) -> UpdateTrialComponentResponseTypeDef:
    pass
```

### update_user_profile

Type annotations for `boto3.client("sagemaker").update_user_profile` method.

[Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)

```python
def update_user_profile(
    self,
    DomainId: str,
    UserProfileName: str,
    UserSettings: "UserSettingsTypeDef" = None
) -> UpdateUserProfileResponseTypeDef:
    pass
```

### update_workforce

Type annotations for `boto3.client("sagemaker").update_workforce` method.

[Client.update_workforce documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_workforce)

```python
def update_workforce(
    self,
    WorkforceName: str,
    SourceIpConfig: "SourceIpConfigTypeDef" = None,
    OidcConfig: OidcConfigTypeDef = None
) -> UpdateWorkforceResponseTypeDef:
    pass
```

### update_workteam

Type annotations for `boto3.client("sagemaker").update_workteam` method.

[Client.update_workteam documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_workteam)

```python
def update_workteam(
    self,
    WorkteamName: str,
    MemberDefinitions: List["MemberDefinitionTypeDef"] = None,
    Description: str = None,
    NotificationConfiguration: "NotificationConfigurationTypeDef" = None
) -> UpdateWorkteamResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("sagemaker").get_paginator` method with overloads.

- `client.get_paginator("list_actions")` -> [ListActionsPaginator](./paginators.md#listactionspaginator)
- `client.get_paginator("list_algorithms")` -> [ListAlgorithmsPaginator](./paginators.md#listalgorithmspaginator)
- `client.get_paginator("list_app_image_configs")` -> [ListAppImageConfigsPaginator](./paginators.md#listappimageconfigspaginator)
- `client.get_paginator("list_apps")` -> [ListAppsPaginator](./paginators.md#listappspaginator)
- `client.get_paginator("list_artifacts")` -> [ListArtifactsPaginator](./paginators.md#listartifactspaginator)
- `client.get_paginator("list_associations")` -> [ListAssociationsPaginator](./paginators.md#listassociationspaginator)
- `client.get_paginator("list_auto_ml_jobs")` -> [ListAutoMLJobsPaginator](./paginators.md#listautomljobspaginator)
- `client.get_paginator("list_candidates_for_auto_ml_job")` -> [ListCandidatesForAutoMLJobPaginator](./paginators.md#listcandidatesforautomljobpaginator)
- `client.get_paginator("list_code_repositories")` -> [ListCodeRepositoriesPaginator](./paginators.md#listcoderepositoriespaginator)
- `client.get_paginator("list_compilation_jobs")` -> [ListCompilationJobsPaginator](./paginators.md#listcompilationjobspaginator)
- `client.get_paginator("list_contexts")` -> [ListContextsPaginator](./paginators.md#listcontextspaginator)
- `client.get_paginator("list_data_quality_job_definitions")` -> [ListDataQualityJobDefinitionsPaginator](./paginators.md#listdataqualityjobdefinitionspaginator)
- `client.get_paginator("list_device_fleets")` -> [ListDeviceFleetsPaginator](./paginators.md#listdevicefleetspaginator)
- `client.get_paginator("list_devices")` -> [ListDevicesPaginator](./paginators.md#listdevicespaginator)
- `client.get_paginator("list_domains")` -> [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- `client.get_paginator("list_edge_packaging_jobs")` -> [ListEdgePackagingJobsPaginator](./paginators.md#listedgepackagingjobspaginator)
- `client.get_paginator("list_endpoint_configs")` -> [ListEndpointConfigsPaginator](./paginators.md#listendpointconfigspaginator)
- `client.get_paginator("list_endpoints")` -> [ListEndpointsPaginator](./paginators.md#listendpointspaginator)
- `client.get_paginator("list_experiments")` -> [ListExperimentsPaginator](./paginators.md#listexperimentspaginator)
- `client.get_paginator("list_feature_groups")` -> [ListFeatureGroupsPaginator](./paginators.md#listfeaturegroupspaginator)
- `client.get_paginator("list_flow_definitions")` -> [ListFlowDefinitionsPaginator](./paginators.md#listflowdefinitionspaginator)
- `client.get_paginator("list_human_task_uis")` -> [ListHumanTaskUisPaginator](./paginators.md#listhumantaskuispaginator)
- `client.get_paginator("list_hyper_parameter_tuning_jobs")` -> [ListHyperParameterTuningJobsPaginator](./paginators.md#listhyperparametertuningjobspaginator)
- `client.get_paginator("list_image_versions")` -> [ListImageVersionsPaginator](./paginators.md#listimageversionspaginator)
- `client.get_paginator("list_images")` -> [ListImagesPaginator](./paginators.md#listimagespaginator)
- `client.get_paginator("list_labeling_jobs")` -> [ListLabelingJobsPaginator](./paginators.md#listlabelingjobspaginator)
- `client.get_paginator("list_labeling_jobs_for_workteam")` -> [ListLabelingJobsForWorkteamPaginator](./paginators.md#listlabelingjobsforworkteampaginator)
- `client.get_paginator("list_model_bias_job_definitions")` -> [ListModelBiasJobDefinitionsPaginator](./paginators.md#listmodelbiasjobdefinitionspaginator)
- `client.get_paginator("list_model_explainability_job_definitions")` -> [ListModelExplainabilityJobDefinitionsPaginator](./paginators.md#listmodelexplainabilityjobdefinitionspaginator)
- `client.get_paginator("list_model_package_groups")` -> [ListModelPackageGroupsPaginator](./paginators.md#listmodelpackagegroupspaginator)
- `client.get_paginator("list_model_packages")` -> [ListModelPackagesPaginator](./paginators.md#listmodelpackagespaginator)
- `client.get_paginator("list_model_quality_job_definitions")` -> [ListModelQualityJobDefinitionsPaginator](./paginators.md#listmodelqualityjobdefinitionspaginator)
- `client.get_paginator("list_models")` -> [ListModelsPaginator](./paginators.md#listmodelspaginator)
- `client.get_paginator("list_monitoring_executions")` -> [ListMonitoringExecutionsPaginator](./paginators.md#listmonitoringexecutionspaginator)
- `client.get_paginator("list_monitoring_schedules")` -> [ListMonitoringSchedulesPaginator](./paginators.md#listmonitoringschedulespaginator)
- `client.get_paginator("list_notebook_instance_lifecycle_configs")` -> [ListNotebookInstanceLifecycleConfigsPaginator](./paginators.md#listnotebookinstancelifecycleconfigspaginator)
- `client.get_paginator("list_notebook_instances")` -> [ListNotebookInstancesPaginator](./paginators.md#listnotebookinstancespaginator)
- `client.get_paginator("list_pipeline_execution_steps")` -> [ListPipelineExecutionStepsPaginator](./paginators.md#listpipelineexecutionstepspaginator)
- `client.get_paginator("list_pipeline_executions")` -> [ListPipelineExecutionsPaginator](./paginators.md#listpipelineexecutionspaginator)
- `client.get_paginator("list_pipeline_parameters_for_execution")` -> [ListPipelineParametersForExecutionPaginator](./paginators.md#listpipelineparametersforexecutionpaginator)
- `client.get_paginator("list_pipelines")` -> [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)
- `client.get_paginator("list_processing_jobs")` -> [ListProcessingJobsPaginator](./paginators.md#listprocessingjobspaginator)
- `client.get_paginator("list_subscribed_workteams")` -> [ListSubscribedWorkteamsPaginator](./paginators.md#listsubscribedworkteamspaginator)
- `client.get_paginator("list_tags")` -> [ListTagsPaginator](./paginators.md#listtagspaginator)
- `client.get_paginator("list_training_jobs")` -> [ListTrainingJobsPaginator](./paginators.md#listtrainingjobspaginator)
- `client.get_paginator("list_training_jobs_for_hyper_parameter_tuning_job")` -> [ListTrainingJobsForHyperParameterTuningJobPaginator](./paginators.md#listtrainingjobsforhyperparametertuningjobpaginator)
- `client.get_paginator("list_transform_jobs")` -> [ListTransformJobsPaginator](./paginators.md#listtransformjobspaginator)
- `client.get_paginator("list_trial_components")` -> [ListTrialComponentsPaginator](./paginators.md#listtrialcomponentspaginator)
- `client.get_paginator("list_trials")` -> [ListTrialsPaginator](./paginators.md#listtrialspaginator)
- `client.get_paginator("list_user_profiles")` -> [ListUserProfilesPaginator](./paginators.md#listuserprofilespaginator)
- `client.get_paginator("list_workforces")` -> [ListWorkforcesPaginator](./paginators.md#listworkforcespaginator)
- `client.get_paginator("list_workteams")` -> [ListWorkteamsPaginator](./paginators.md#listworkteamspaginator)
- `client.get_paginator("search")` -> [SearchPaginator](./paginators.md#searchpaginator)




### get_waiter

Type annotations for `boto3.client("sagemaker").get_waiter` method with overloads.

- `client.get_waiter("endpoint_deleted")` -> [EndpointDeletedWaiter](./waiters.md#endpointdeletedwaiter)
- `client.get_waiter("endpoint_in_service")` -> [EndpointInServiceWaiter](./waiters.md#endpointinservicewaiter)
- `client.get_waiter("notebook_instance_deleted")` -> [NotebookInstanceDeletedWaiter](./waiters.md#notebookinstancedeletedwaiter)
- `client.get_waiter("notebook_instance_in_service")` -> [NotebookInstanceInServiceWaiter](./waiters.md#notebookinstanceinservicewaiter)
- `client.get_waiter("notebook_instance_stopped")` -> [NotebookInstanceStoppedWaiter](./waiters.md#notebookinstancestoppedwaiter)
- `client.get_waiter("processing_job_completed_or_stopped")` -> [ProcessingJobCompletedOrStoppedWaiter](./waiters.md#processingjobcompletedorstoppedwaiter)
- `client.get_waiter("training_job_completed_or_stopped")` -> [TrainingJobCompletedOrStoppedWaiter](./waiters.md#trainingjobcompletedorstoppedwaiter)
- `client.get_waiter("transform_job_completed_or_stopped")` -> [TransformJobCompletedOrStoppedWaiter](./waiters.md#transformjobcompletedorstoppedwaiter)
