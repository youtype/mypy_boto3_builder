# Literals for boto3 SageMaker module

> [Index](../index.md) > [SageMaker](./index.md) > Literals

Auto-generated documentation for [SageMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker)
type annotations stubs module [mypy_boto3_sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/).

- [Literals for boto3 SageMaker module](#literals-for-boto3-sagemaker-module)
  - [ActionStatus](#actionstatus)
  - [AlgorithmSortBy](#algorithmsortby)
  - [AlgorithmStatus](#algorithmstatus)
  - [AppImageConfigSortKey](#appimageconfigsortkey)
  - [AppInstanceType](#appinstancetype)
  - [AppNetworkAccessType](#appnetworkaccesstype)
  - [AppSortKey](#appsortkey)
  - [AppStatus](#appstatus)
  - [AppType](#apptype)
  - [ArtifactSourceIdType](#artifactsourceidtype)
  - [AssemblyType](#assemblytype)
  - [AssociationEdgeType](#associationedgetype)
  - [AthenaResultCompressionType](#athenaresultcompressiontype)
  - [AthenaResultFormat](#athenaresultformat)
  - [AuthMode](#authmode)
  - [AutoMLJobObjectiveType](#automljobobjectivetype)
  - [AutoMLJobSecondaryStatus](#automljobsecondarystatus)
  - [AutoMLJobStatus](#automljobstatus)
  - [AutoMLMetricEnum](#automlmetricenum)
  - [AutoMLS3DataType](#automls3datatype)
  - [AutoMLSortBy](#automlsortby)
  - [AutoMLSortOrder](#automlsortorder)
  - [AwsManagedHumanLoopRequestSource](#awsmanagedhumanlooprequestsource)
  - [BatchStrategy](#batchstrategy)
  - [CandidateSortBy](#candidatesortby)
  - [CandidateStatus](#candidatestatus)
  - [CandidateStepType](#candidatesteptype)
  - [CapacitySizeType](#capacitysizetype)
  - [CaptureMode](#capturemode)
  - [CaptureStatus](#capturestatus)
  - [CodeRepositorySortBy](#coderepositorysortby)
  - [CodeRepositorySortOrder](#coderepositorysortorder)
  - [CompilationJobStatus](#compilationjobstatus)
  - [CompressionType](#compressiontype)
  - [ConditionOutcome](#conditionoutcome)
  - [ContainerMode](#containermode)
  - [ContentClassifier](#contentclassifier)
  - [DataDistributionType](#datadistributiontype)
  - [DetailedAlgorithmStatus](#detailedalgorithmstatus)
  - [DetailedModelPackageStatus](#detailedmodelpackagestatus)
  - [DirectInternetAccess](#directinternetaccess)
  - [DomainStatus](#domainstatus)
  - [EdgePackagingJobStatus](#edgepackagingjobstatus)
  - [EndpointConfigSortKey](#endpointconfigsortkey)
  - [EndpointDeletedWaiterName](#endpointdeletedwaitername)
  - [EndpointInServiceWaiterName](#endpointinservicewaitername)
  - [EndpointSortKey](#endpointsortkey)
  - [EndpointStatus](#endpointstatus)
  - [ExecutionStatus](#executionstatus)
  - [FeatureGroupSortBy](#featuregroupsortby)
  - [FeatureGroupSortOrder](#featuregroupsortorder)
  - [FeatureGroupStatus](#featuregroupstatus)
  - [FeatureType](#featuretype)
  - [FileSystemAccessMode](#filesystemaccessmode)
  - [FileSystemType](#filesystemtype)
  - [FlowDefinitionStatus](#flowdefinitionstatus)
  - [Framework](#framework)
  - [HumanTaskUiStatus](#humantaskuistatus)
  - [HyperParameterScalingType](#hyperparameterscalingtype)
  - [HyperParameterTuningJobObjectiveType](#hyperparametertuningjobobjectivetype)
  - [HyperParameterTuningJobSortByOptions](#hyperparametertuningjobsortbyoptions)
  - [HyperParameterTuningJobStatus](#hyperparametertuningjobstatus)
  - [HyperParameterTuningJobStrategyType](#hyperparametertuningjobstrategytype)
  - [HyperParameterTuningJobWarmStartType](#hyperparametertuningjobwarmstarttype)
  - [ImageSortBy](#imagesortby)
  - [ImageSortOrder](#imagesortorder)
  - [ImageStatus](#imagestatus)
  - [ImageVersionSortBy](#imageversionsortby)
  - [ImageVersionSortOrder](#imageversionsortorder)
  - [ImageVersionStatus](#imageversionstatus)
  - [InferenceExecutionMode](#inferenceexecutionmode)
  - [InputMode](#inputmode)
  - [InstanceType](#instancetype)
  - [JoinSource](#joinsource)
  - [LabelingJobStatus](#labelingjobstatus)
  - [ListActionsPaginatorName](#listactionspaginatorname)
  - [ListAlgorithmsPaginatorName](#listalgorithmspaginatorname)
  - [ListAppImageConfigsPaginatorName](#listappimageconfigspaginatorname)
  - [ListAppsPaginatorName](#listappspaginatorname)
  - [ListArtifactsPaginatorName](#listartifactspaginatorname)
  - [ListAssociationsPaginatorName](#listassociationspaginatorname)
  - [ListAutoMLJobsPaginatorName](#listautomljobspaginatorname)
  - [ListCandidatesForAutoMLJobPaginatorName](#listcandidatesforautomljobpaginatorname)
  - [ListCodeRepositoriesPaginatorName](#listcoderepositoriespaginatorname)
  - [ListCompilationJobsPaginatorName](#listcompilationjobspaginatorname)
  - [ListCompilationJobsSortBy](#listcompilationjobssortby)
  - [ListContextsPaginatorName](#listcontextspaginatorname)
  - [ListDataQualityJobDefinitionsPaginatorName](#listdataqualityjobdefinitionspaginatorname)
  - [ListDeviceFleetsPaginatorName](#listdevicefleetspaginatorname)
  - [ListDeviceFleetsSortBy](#listdevicefleetssortby)
  - [ListDevicesPaginatorName](#listdevicespaginatorname)
  - [ListDomainsPaginatorName](#listdomainspaginatorname)
  - [ListEdgePackagingJobsPaginatorName](#listedgepackagingjobspaginatorname)
  - [ListEdgePackagingJobsSortBy](#listedgepackagingjobssortby)
  - [ListEndpointConfigsPaginatorName](#listendpointconfigspaginatorname)
  - [ListEndpointsPaginatorName](#listendpointspaginatorname)
  - [ListExperimentsPaginatorName](#listexperimentspaginatorname)
  - [ListFeatureGroupsPaginatorName](#listfeaturegroupspaginatorname)
  - [ListFlowDefinitionsPaginatorName](#listflowdefinitionspaginatorname)
  - [ListHumanTaskUisPaginatorName](#listhumantaskuispaginatorname)
  - [ListHyperParameterTuningJobsPaginatorName](#listhyperparametertuningjobspaginatorname)
  - [ListImageVersionsPaginatorName](#listimageversionspaginatorname)
  - [ListImagesPaginatorName](#listimagespaginatorname)
  - [ListLabelingJobsForWorkteamPaginatorName](#listlabelingjobsforworkteampaginatorname)
  - [ListLabelingJobsForWorkteamSortByOptions](#listlabelingjobsforworkteamsortbyoptions)
  - [ListLabelingJobsPaginatorName](#listlabelingjobspaginatorname)
  - [ListModelBiasJobDefinitionsPaginatorName](#listmodelbiasjobdefinitionspaginatorname)
  - [ListModelExplainabilityJobDefinitionsPaginatorName](#listmodelexplainabilityjobdefinitionspaginatorname)
  - [ListModelPackageGroupsPaginatorName](#listmodelpackagegroupspaginatorname)
  - [ListModelPackagesPaginatorName](#listmodelpackagespaginatorname)
  - [ListModelQualityJobDefinitionsPaginatorName](#listmodelqualityjobdefinitionspaginatorname)
  - [ListModelsPaginatorName](#listmodelspaginatorname)
  - [ListMonitoringExecutionsPaginatorName](#listmonitoringexecutionspaginatorname)
  - [ListMonitoringSchedulesPaginatorName](#listmonitoringschedulespaginatorname)
  - [ListNotebookInstanceLifecycleConfigsPaginatorName](#listnotebookinstancelifecycleconfigspaginatorname)
  - [ListNotebookInstancesPaginatorName](#listnotebookinstancespaginatorname)
  - [ListPipelineExecutionStepsPaginatorName](#listpipelineexecutionstepspaginatorname)
  - [ListPipelineExecutionsPaginatorName](#listpipelineexecutionspaginatorname)
  - [ListPipelineParametersForExecutionPaginatorName](#listpipelineparametersforexecutionpaginatorname)
  - [ListPipelinesPaginatorName](#listpipelinespaginatorname)
  - [ListProcessingJobsPaginatorName](#listprocessingjobspaginatorname)
  - [ListSubscribedWorkteamsPaginatorName](#listsubscribedworkteamspaginatorname)
  - [ListTagsPaginatorName](#listtagspaginatorname)
  - [ListTrainingJobsForHyperParameterTuningJobPaginatorName](#listtrainingjobsforhyperparametertuningjobpaginatorname)
  - [ListTrainingJobsPaginatorName](#listtrainingjobspaginatorname)
  - [ListTransformJobsPaginatorName](#listtransformjobspaginatorname)
  - [ListTrialComponentsPaginatorName](#listtrialcomponentspaginatorname)
  - [ListTrialsPaginatorName](#listtrialspaginatorname)
  - [ListUserProfilesPaginatorName](#listuserprofilespaginatorname)
  - [ListWorkforcesPaginatorName](#listworkforcespaginatorname)
  - [ListWorkforcesSortByOptions](#listworkforcessortbyoptions)
  - [ListWorkteamsPaginatorName](#listworkteamspaginatorname)
  - [ListWorkteamsSortByOptions](#listworkteamssortbyoptions)
  - [ModelApprovalStatus](#modelapprovalstatus)
  - [ModelCacheSetting](#modelcachesetting)
  - [ModelPackageGroupSortBy](#modelpackagegroupsortby)
  - [ModelPackageGroupStatus](#modelpackagegroupstatus)
  - [ModelPackageSortBy](#modelpackagesortby)
  - [ModelPackageStatus](#modelpackagestatus)
  - [ModelPackageType](#modelpackagetype)
  - [ModelSortKey](#modelsortkey)
  - [MonitoringExecutionSortKey](#monitoringexecutionsortkey)
  - [MonitoringJobDefinitionSortKey](#monitoringjobdefinitionsortkey)
  - [MonitoringProblemType](#monitoringproblemtype)
  - [MonitoringScheduleSortKey](#monitoringschedulesortkey)
  - [MonitoringType](#monitoringtype)
  - [NotebookInstanceAcceleratorType](#notebookinstanceacceleratortype)
  - [NotebookInstanceDeletedWaiterName](#notebookinstancedeletedwaitername)
  - [NotebookInstanceInServiceWaiterName](#notebookinstanceinservicewaitername)
  - [NotebookInstanceLifecycleConfigSortKey](#notebookinstancelifecycleconfigsortkey)
  - [NotebookInstanceLifecycleConfigSortOrder](#notebookinstancelifecycleconfigsortorder)
  - [NotebookInstanceSortKey](#notebookinstancesortkey)
  - [NotebookInstanceSortOrder](#notebookinstancesortorder)
  - [NotebookInstanceStatus](#notebookinstancestatus)
  - [NotebookInstanceStoppedWaiterName](#notebookinstancestoppedwaitername)
  - [NotebookOutputOption](#notebookoutputoption)
  - [ObjectiveStatus](#objectivestatus)
  - [OfflineStoreStatusValue](#offlinestorestatusvalue)
  - [OrderKey](#orderkey)
  - [ParameterType](#parametertype)
  - [PipelineExecutionStatus](#pipelineexecutionstatus)
  - [PipelineStatus](#pipelinestatus)
  - [ProblemType](#problemtype)
  - [ProcessingInstanceType](#processinginstancetype)
  - [ProcessingJobCompletedOrStoppedWaiterName](#processingjobcompletedorstoppedwaitername)
  - [ProcessingJobStatus](#processingjobstatus)
  - [ProcessingS3CompressionType](#processings3compressiontype)
  - [ProcessingS3DataDistributionType](#processings3datadistributiontype)
  - [ProcessingS3DataType](#processings3datatype)
  - [ProcessingS3InputMode](#processings3inputmode)
  - [ProcessingS3UploadMode](#processings3uploadmode)
  - [ProductionVariantAcceleratorType](#productionvariantacceleratortype)
  - [ProductionVariantInstanceType](#productionvariantinstancetype)
  - [ProfilingStatus](#profilingstatus)
  - [ProjectSortBy](#projectsortby)
  - [ProjectSortOrder](#projectsortorder)
  - [ProjectStatus](#projectstatus)
  - [RecordWrapper](#recordwrapper)
  - [RedshiftResultCompressionType](#redshiftresultcompressiontype)
  - [RedshiftResultFormat](#redshiftresultformat)
  - [RepositoryAccessMode](#repositoryaccessmode)
  - [ResourceType](#resourcetype)
  - [RetentionType](#retentiontype)
  - [RootAccess](#rootaccess)
  - [RuleEvaluationStatus](#ruleevaluationstatus)
  - [S3DataDistribution](#s3datadistribution)
  - [S3DataType](#s3datatype)
  - [SagemakerServicecatalogStatus](#sagemakerservicecatalogstatus)
  - [ScheduleStatus](#schedulestatus)
  - [SearchPaginatorName](#searchpaginatorname)
  - [SearchSortOrder](#searchsortorder)
  - [SecondaryStatus](#secondarystatus)
  - [SortActionsBy](#sortactionsby)
  - [SortArtifactsBy](#sortartifactsby)
  - [SortAssociationsBy](#sortassociationsby)
  - [SortBy](#sortby)
  - [SortContextsBy](#sortcontextsby)
  - [SortExperimentsBy](#sortexperimentsby)
  - [SortOrder](#sortorder)
  - [SortPipelineExecutionsBy](#sortpipelineexecutionsby)
  - [SortPipelinesBy](#sortpipelinesby)
  - [SortTrialComponentsBy](#sorttrialcomponentsby)
  - [SortTrialsBy](#sorttrialsby)
  - [SplitType](#splittype)
  - [StepStatus](#stepstatus)
  - [TargetDevice](#targetdevice)
  - [TargetPlatformAccelerator](#targetplatformaccelerator)
  - [TargetPlatformArch](#targetplatformarch)
  - [TargetPlatformOs](#targetplatformos)
  - [TrafficRoutingConfigType](#trafficroutingconfigtype)
  - [TrainingInputMode](#traininginputmode)
  - [TrainingInstanceType](#traininginstancetype)
  - [TrainingJobCompletedOrStoppedWaiterName](#trainingjobcompletedorstoppedwaitername)
  - [TrainingJobEarlyStoppingType](#trainingjobearlystoppingtype)
  - [TrainingJobSortByOptions](#trainingjobsortbyoptions)
  - [TrainingJobStatus](#trainingjobstatus)
  - [TransformInstanceType](#transforminstancetype)
  - [TransformJobCompletedOrStoppedWaiterName](#transformjobcompletedorstoppedwaitername)
  - [TransformJobStatus](#transformjobstatus)
  - [TrialComponentPrimaryStatus](#trialcomponentprimarystatus)
  - [UserProfileSortKey](#userprofilesortkey)
  - [UserProfileStatus](#userprofilestatus)
  - [VariantPropertyType](#variantpropertytype)

## ActionStatus

```python
from mypy_boto3_sagemaker.literals import ActionStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`
- `Unknown`

## AlgorithmSortBy

```python
from mypy_boto3_sagemaker.literals import AlgorithmSortBy
```

Values:

- `CreationTime`
- `Name`

## AlgorithmStatus

```python
from mypy_boto3_sagemaker.literals import AlgorithmStatus
```

Values:

- `Completed`
- `Deleting`
- `Failed`
- `InProgress`
- `Pending`

## AppImageConfigSortKey

```python
from mypy_boto3_sagemaker.literals import AppImageConfigSortKey
```

Values:

- `CreationTime`
- `LastModifiedTime`
- `Name`

## AppInstanceType

```python
from mypy_boto3_sagemaker.literals import AppInstanceType
```

Values:

- `ml.c5.12xlarge`
- `ml.c5.18xlarge`
- `ml.c5.24xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.large`
- `ml.c5.xlarge`
- `ml.g4dn.12xlarge`
- `ml.g4dn.16xlarge`
- `ml.g4dn.2xlarge`
- `ml.g4dn.4xlarge`
- `ml.g4dn.8xlarge`
- `ml.g4dn.xlarge`
- `ml.m5.12xlarge`
- `ml.m5.16xlarge`
- `ml.m5.24xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.8xlarge`
- `ml.m5.large`
- `ml.m5.xlarge`
- `ml.p3.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`
- `ml.t3.2xlarge`
- `ml.t3.large`
- `ml.t3.medium`
- `ml.t3.micro`
- `ml.t3.small`
- `ml.t3.xlarge`
- `system`

## AppNetworkAccessType

```python
from mypy_boto3_sagemaker.literals import AppNetworkAccessType
```

Values:

- `PublicInternetOnly`
- `VpcOnly`

## AppSortKey

```python
from mypy_boto3_sagemaker.literals import AppSortKey
```

Values:

- `CreationTime`

## AppStatus

```python
from mypy_boto3_sagemaker.literals import AppStatus
```

Values:

- `Deleted`
- `Deleting`
- `Failed`
- `InService`
- `Pending`

## AppType

```python
from mypy_boto3_sagemaker.literals import AppType
```

Values:

- `JupyterServer`
- `KernelGateway`
- `TensorBoard`

## ArtifactSourceIdType

```python
from mypy_boto3_sagemaker.literals import ArtifactSourceIdType
```

Values:

- `Custom`
- `MD5Hash`
- `S3ETag`
- `S3Version`

## AssemblyType

```python
from mypy_boto3_sagemaker.literals import AssemblyType
```

Values:

- `Line`
- `None`

## AssociationEdgeType

```python
from mypy_boto3_sagemaker.literals import AssociationEdgeType
```

Values:

- `AssociatedWith`
- `ContributedTo`
- `DerivedFrom`
- `Produced`

## AthenaResultCompressionType

```python
from mypy_boto3_sagemaker.literals import AthenaResultCompressionType
```

Values:

- `GZIP`
- `SNAPPY`
- `ZLIB`

## AthenaResultFormat

```python
from mypy_boto3_sagemaker.literals import AthenaResultFormat
```

Values:

- `AVRO`
- `JSON`
- `ORC`
- `PARQUET`
- `TEXTFILE`

## AuthMode

```python
from mypy_boto3_sagemaker.literals import AuthMode
```

Values:

- `IAM`
- `SSO`

## AutoMLJobObjectiveType

```python
from mypy_boto3_sagemaker.literals import AutoMLJobObjectiveType
```

Values:

- `Maximize`
- `Minimize`

## AutoMLJobSecondaryStatus

```python
from mypy_boto3_sagemaker.literals import AutoMLJobSecondaryStatus
```

Values:

- `AnalyzingData`
- `CandidateDefinitionsGenerated`
- `Completed`
- `ExplainabilityError`
- `Failed`
- `FeatureEngineering`
- `GeneratingExplainabilityReport`
- `MaxAutoMLJobRuntimeReached`
- `MaxCandidatesReached`
- `ModelTuning`
- `Starting`
- `Stopped`
- `Stopping`

## AutoMLJobStatus

```python
from mypy_boto3_sagemaker.literals import AutoMLJobStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## AutoMLMetricEnum

```python
from mypy_boto3_sagemaker.literals import AutoMLMetricEnum
```

Values:

- `Accuracy`
- `AUC`
- `F1`
- `F1macro`
- `MSE`

## AutoMLS3DataType

```python
from mypy_boto3_sagemaker.literals import AutoMLS3DataType
```

Values:

- `ManifestFile`
- `S3Prefix`

## AutoMLSortBy

```python
from mypy_boto3_sagemaker.literals import AutoMLSortBy
```

Values:

- `CreationTime`
- `Name`
- `Status`

## AutoMLSortOrder

```python
from mypy_boto3_sagemaker.literals import AutoMLSortOrder
```

Values:

- `Ascending`
- `Descending`

## AwsManagedHumanLoopRequestSource

```python
from mypy_boto3_sagemaker.literals import AwsManagedHumanLoopRequestSource
```

Values:

- `AWS/Rekognition/DetectModerationLabels/Image/V3`
- `AWS/Textract/AnalyzeDocument/Forms/V1`

## BatchStrategy

```python
from mypy_boto3_sagemaker.literals import BatchStrategy
```

Values:

- `MultiRecord`
- `SingleRecord`

## CandidateSortBy

```python
from mypy_boto3_sagemaker.literals import CandidateSortBy
```

Values:

- `CreationTime`
- `FinalObjectiveMetricValue`
- `Status`

## CandidateStatus

```python
from mypy_boto3_sagemaker.literals import CandidateStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## CandidateStepType

```python
from mypy_boto3_sagemaker.literals import CandidateStepType
```

Values:

- `AWS::SageMaker::ProcessingJob`
- `AWS::SageMaker::TrainingJob`
- `AWS::SageMaker::TransformJob`

## CapacitySizeType

```python
from mypy_boto3_sagemaker.literals import CapacitySizeType
```

Values:

- `CAPACITY_PERCENT`
- `INSTANCE_COUNT`

## CaptureMode

```python
from mypy_boto3_sagemaker.literals import CaptureMode
```

Values:

- `Input`
- `Output`

## CaptureStatus

```python
from mypy_boto3_sagemaker.literals import CaptureStatus
```

Values:

- `Started`
- `Stopped`

## CodeRepositorySortBy

```python
from mypy_boto3_sagemaker.literals import CodeRepositorySortBy
```

Values:

- `CreationTime`
- `LastModifiedTime`
- `Name`

## CodeRepositorySortOrder

```python
from mypy_boto3_sagemaker.literals import CodeRepositorySortOrder
```

Values:

- `Ascending`
- `Descending`

## CompilationJobStatus

```python
from mypy_boto3_sagemaker.literals import CompilationJobStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `INPROGRESS`
- `STARTING`
- `STOPPED`
- `STOPPING`

## CompressionType

```python
from mypy_boto3_sagemaker.literals import CompressionType
```

Values:

- `Gzip`
- `None`

## ConditionOutcome

```python
from mypy_boto3_sagemaker.literals import ConditionOutcome
```

Values:

- `False`
- `True`

## ContainerMode

```python
from mypy_boto3_sagemaker.literals import ContainerMode
```

Values:

- `MultiModel`
- `SingleModel`

## ContentClassifier

```python
from mypy_boto3_sagemaker.literals import ContentClassifier
```

Values:

- `FreeOfAdultContent`
- `FreeOfPersonallyIdentifiableInformation`

## DataDistributionType

```python
from mypy_boto3_sagemaker.literals import DataDistributionType
```

Values:

- `FullyReplicated`
- `ShardedByS3Key`

## DetailedAlgorithmStatus

```python
from mypy_boto3_sagemaker.literals import DetailedAlgorithmStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `NotStarted`

## DetailedModelPackageStatus

```python
from mypy_boto3_sagemaker.literals import DetailedModelPackageStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `NotStarted`

## DirectInternetAccess

```python
from mypy_boto3_sagemaker.literals import DirectInternetAccess
```

Values:

- `Disabled`
- `Enabled`

## DomainStatus

```python
from mypy_boto3_sagemaker.literals import DomainStatus
```

Values:

- `Delete_Failed`
- `Deleting`
- `Failed`
- `InService`
- `Pending`
- `Update_Failed`
- `Updating`

## EdgePackagingJobStatus

```python
from mypy_boto3_sagemaker.literals import EdgePackagingJobStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `INPROGRESS`
- `STARTING`
- `STOPPED`
- `STOPPING`

## EndpointConfigSortKey

```python
from mypy_boto3_sagemaker.literals import EndpointConfigSortKey
```

Values:

- `CreationTime`
- `Name`

## EndpointDeletedWaiterName

```python
from mypy_boto3_sagemaker.literals import EndpointDeletedWaiterName
```

Values:

- `endpoint_deleted`

## EndpointInServiceWaiterName

```python
from mypy_boto3_sagemaker.literals import EndpointInServiceWaiterName
```

Values:

- `endpoint_in_service`

## EndpointSortKey

```python
from mypy_boto3_sagemaker.literals import EndpointSortKey
```

Values:

- `CreationTime`
- `Name`
- `Status`

## EndpointStatus

```python
from mypy_boto3_sagemaker.literals import EndpointStatus
```

Values:

- `Creating`
- `Deleting`
- `Failed`
- `InService`
- `OutOfService`
- `RollingBack`
- `SystemUpdating`
- `Updating`

## ExecutionStatus

```python
from mypy_boto3_sagemaker.literals import ExecutionStatus
```

Values:

- `Completed`
- `CompletedWithViolations`
- `Failed`
- `InProgress`
- `Pending`
- `Stopped`
- `Stopping`

## FeatureGroupSortBy

```python
from mypy_boto3_sagemaker.literals import FeatureGroupSortBy
```

Values:

- `CreationTime`
- `FeatureGroupStatus`
- `Name`
- `OfflineStoreStatus`

## FeatureGroupSortOrder

```python
from mypy_boto3_sagemaker.literals import FeatureGroupSortOrder
```

Values:

- `Ascending`
- `Descending`

## FeatureGroupStatus

```python
from mypy_boto3_sagemaker.literals import FeatureGroupStatus
```

Values:

- `Created`
- `CreateFailed`
- `Creating`
- `DeleteFailed`
- `Deleting`

## FeatureType

```python
from mypy_boto3_sagemaker.literals import FeatureType
```

Values:

- `Fractional`
- `Integral`
- `String`

## FileSystemAccessMode

```python
from mypy_boto3_sagemaker.literals import FileSystemAccessMode
```

Values:

- `ro`
- `rw`

## FileSystemType

```python
from mypy_boto3_sagemaker.literals import FileSystemType
```

Values:

- `EFS`
- `FSxLustre`

## FlowDefinitionStatus

```python
from mypy_boto3_sagemaker.literals import FlowDefinitionStatus
```

Values:

- `Active`
- `Deleting`
- `Failed`
- `Initializing`

## Framework

```python
from mypy_boto3_sagemaker.literals import Framework
```

Values:

- `DARKNET`
- `KERAS`
- `MXNET`
- `ONNX`
- `PYTORCH`
- `SKLEARN`
- `TENSORFLOW`
- `TFLITE`
- `XGBOOST`

## HumanTaskUiStatus

```python
from mypy_boto3_sagemaker.literals import HumanTaskUiStatus
```

Values:

- `Active`
- `Deleting`

## HyperParameterScalingType

```python
from mypy_boto3_sagemaker.literals import HyperParameterScalingType
```

Values:

- `Auto`
- `Linear`
- `Logarithmic`
- `ReverseLogarithmic`

## HyperParameterTuningJobObjectiveType

```python
from mypy_boto3_sagemaker.literals import HyperParameterTuningJobObjectiveType
```

Values:

- `Maximize`
- `Minimize`

## HyperParameterTuningJobSortByOptions

```python
from mypy_boto3_sagemaker.literals import HyperParameterTuningJobSortByOptions
```

Values:

- `CreationTime`
- `Name`
- `Status`

## HyperParameterTuningJobStatus

```python
from mypy_boto3_sagemaker.literals import HyperParameterTuningJobStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## HyperParameterTuningJobStrategyType

```python
from mypy_boto3_sagemaker.literals import HyperParameterTuningJobStrategyType
```

Values:

- `Bayesian`
- `Random`

## HyperParameterTuningJobWarmStartType

```python
from mypy_boto3_sagemaker.literals import HyperParameterTuningJobWarmStartType
```

Values:

- `IdenticalDataAndAlgorithm`
- `TransferLearning`

## ImageSortBy

```python
from mypy_boto3_sagemaker.literals import ImageSortBy
```

Values:

- `CREATION_TIME`
- `IMAGE_NAME`
- `LAST_MODIFIED_TIME`

## ImageSortOrder

```python
from mypy_boto3_sagemaker.literals import ImageSortOrder
```

Values:

- `ASCENDING`
- `DESCENDING`

## ImageStatus

```python
from mypy_boto3_sagemaker.literals import ImageStatus
```

Values:

- `CREATE_FAILED`
- `CREATED`
- `CREATING`
- `DELETE_FAILED`
- `DELETING`
- `UPDATE_FAILED`
- `UPDATING`

## ImageVersionSortBy

```python
from mypy_boto3_sagemaker.literals import ImageVersionSortBy
```

Values:

- `CREATION_TIME`
- `LAST_MODIFIED_TIME`
- `VERSION`

## ImageVersionSortOrder

```python
from mypy_boto3_sagemaker.literals import ImageVersionSortOrder
```

Values:

- `ASCENDING`
- `DESCENDING`

## ImageVersionStatus

```python
from mypy_boto3_sagemaker.literals import ImageVersionStatus
```

Values:

- `CREATE_FAILED`
- `CREATED`
- `CREATING`
- `DELETE_FAILED`
- `DELETING`

## InferenceExecutionMode

```python
from mypy_boto3_sagemaker.literals import InferenceExecutionMode
```

Values:

- `Direct`
- `Serial`

## InputMode

```python
from mypy_boto3_sagemaker.literals import InputMode
```

Values:

- `File`
- `Pipe`

## InstanceType

```python
from mypy_boto3_sagemaker.literals import InstanceType
```

Values:

- `ml.c4.2xlarge`
- `ml.c4.4xlarge`
- `ml.c4.8xlarge`
- `ml.c4.xlarge`
- `ml.c5.18xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.xlarge`
- `ml.c5d.18xlarge`
- `ml.c5d.2xlarge`
- `ml.c5d.4xlarge`
- `ml.c5d.9xlarge`
- `ml.c5d.xlarge`
- `ml.m4.10xlarge`
- `ml.m4.16xlarge`
- `ml.m4.2xlarge`
- `ml.m4.4xlarge`
- `ml.m4.xlarge`
- `ml.m5.12xlarge`
- `ml.m5.24xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.xlarge`
- `ml.p2.16xlarge`
- `ml.p2.8xlarge`
- `ml.p2.xlarge`
- `ml.p3.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`
- `ml.t2.2xlarge`
- `ml.t2.large`
- `ml.t2.medium`
- `ml.t2.xlarge`
- `ml.t3.2xlarge`
- `ml.t3.large`
- `ml.t3.medium`
- `ml.t3.xlarge`

## JoinSource

```python
from mypy_boto3_sagemaker.literals import JoinSource
```

Values:

- `Input`
- `None`

## LabelingJobStatus

```python
from mypy_boto3_sagemaker.literals import LabelingJobStatus
```

Values:

- `Completed`
- `Failed`
- `Initializing`
- `InProgress`
- `Stopped`
- `Stopping`

## ListActionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListActionsPaginatorName
```

Values:

- `list_actions`

## ListAlgorithmsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListAlgorithmsPaginatorName
```

Values:

- `list_algorithms`

## ListAppImageConfigsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListAppImageConfigsPaginatorName
```

Values:

- `list_app_image_configs`

## ListAppsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListAppsPaginatorName
```

Values:

- `list_apps`

## ListArtifactsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListArtifactsPaginatorName
```

Values:

- `list_artifacts`

## ListAssociationsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListAssociationsPaginatorName
```

Values:

- `list_associations`

## ListAutoMLJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListAutoMLJobsPaginatorName
```

Values:

- `list_auto_ml_jobs`

## ListCandidatesForAutoMLJobPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListCandidatesForAutoMLJobPaginatorName
```

Values:

- `list_candidates_for_auto_ml_job`

## ListCodeRepositoriesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListCodeRepositoriesPaginatorName
```

Values:

- `list_code_repositories`

## ListCompilationJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListCompilationJobsPaginatorName
```

Values:

- `list_compilation_jobs`

## ListCompilationJobsSortBy

```python
from mypy_boto3_sagemaker.literals import ListCompilationJobsSortBy
```

Values:

- `CreationTime`
- `Name`
- `Status`

## ListContextsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListContextsPaginatorName
```

Values:

- `list_contexts`

## ListDataQualityJobDefinitionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListDataQualityJobDefinitionsPaginatorName
```

Values:

- `list_data_quality_job_definitions`

## ListDeviceFleetsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListDeviceFleetsPaginatorName
```

Values:

- `list_device_fleets`

## ListDeviceFleetsSortBy

```python
from mypy_boto3_sagemaker.literals import ListDeviceFleetsSortBy
```

Values:

- `CREATION_TIME`
- `LAST_MODIFIED_TIME`
- `NAME`

## ListDevicesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListDevicesPaginatorName
```

Values:

- `list_devices`

## ListDomainsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListDomainsPaginatorName
```

Values:

- `list_domains`

## ListEdgePackagingJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListEdgePackagingJobsPaginatorName
```

Values:

- `list_edge_packaging_jobs`

## ListEdgePackagingJobsSortBy

```python
from mypy_boto3_sagemaker.literals import ListEdgePackagingJobsSortBy
```

Values:

- `CREATION_TIME`
- `LAST_MODIFIED_TIME`
- `MODEL_NAME`
- `NAME`
- `STATUS`

## ListEndpointConfigsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListEndpointConfigsPaginatorName
```

Values:

- `list_endpoint_configs`

## ListEndpointsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListEndpointsPaginatorName
```

Values:

- `list_endpoints`

## ListExperimentsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListExperimentsPaginatorName
```

Values:

- `list_experiments`

## ListFeatureGroupsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListFeatureGroupsPaginatorName
```

Values:

- `list_feature_groups`

## ListFlowDefinitionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListFlowDefinitionsPaginatorName
```

Values:

- `list_flow_definitions`

## ListHumanTaskUisPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListHumanTaskUisPaginatorName
```

Values:

- `list_human_task_uis`

## ListHyperParameterTuningJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListHyperParameterTuningJobsPaginatorName
```

Values:

- `list_hyper_parameter_tuning_jobs`

## ListImageVersionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListImageVersionsPaginatorName
```

Values:

- `list_image_versions`

## ListImagesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListImagesPaginatorName
```

Values:

- `list_images`

## ListLabelingJobsForWorkteamPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListLabelingJobsForWorkteamPaginatorName
```

Values:

- `list_labeling_jobs_for_workteam`

## ListLabelingJobsForWorkteamSortByOptions

```python
from mypy_boto3_sagemaker.literals import ListLabelingJobsForWorkteamSortByOptions
```

Values:

- `CreationTime`

## ListLabelingJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListLabelingJobsPaginatorName
```

Values:

- `list_labeling_jobs`

## ListModelBiasJobDefinitionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListModelBiasJobDefinitionsPaginatorName
```

Values:

- `list_model_bias_job_definitions`

## ListModelExplainabilityJobDefinitionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListModelExplainabilityJobDefinitionsPaginatorName
```

Values:

- `list_model_explainability_job_definitions`

## ListModelPackageGroupsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListModelPackageGroupsPaginatorName
```

Values:

- `list_model_package_groups`

## ListModelPackagesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListModelPackagesPaginatorName
```

Values:

- `list_model_packages`

## ListModelQualityJobDefinitionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListModelQualityJobDefinitionsPaginatorName
```

Values:

- `list_model_quality_job_definitions`

## ListModelsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListModelsPaginatorName
```

Values:

- `list_models`

## ListMonitoringExecutionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListMonitoringExecutionsPaginatorName
```

Values:

- `list_monitoring_executions`

## ListMonitoringSchedulesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListMonitoringSchedulesPaginatorName
```

Values:

- `list_monitoring_schedules`

## ListNotebookInstanceLifecycleConfigsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListNotebookInstanceLifecycleConfigsPaginatorName
```

Values:

- `list_notebook_instance_lifecycle_configs`

## ListNotebookInstancesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListNotebookInstancesPaginatorName
```

Values:

- `list_notebook_instances`

## ListPipelineExecutionStepsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListPipelineExecutionStepsPaginatorName
```

Values:

- `list_pipeline_execution_steps`

## ListPipelineExecutionsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListPipelineExecutionsPaginatorName
```

Values:

- `list_pipeline_executions`

## ListPipelineParametersForExecutionPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListPipelineParametersForExecutionPaginatorName
```

Values:

- `list_pipeline_parameters_for_execution`

## ListPipelinesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListPipelinesPaginatorName
```

Values:

- `list_pipelines`

## ListProcessingJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListProcessingJobsPaginatorName
```

Values:

- `list_processing_jobs`

## ListSubscribedWorkteamsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListSubscribedWorkteamsPaginatorName
```

Values:

- `list_subscribed_workteams`

## ListTagsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListTagsPaginatorName
```

Values:

- `list_tags`

## ListTrainingJobsForHyperParameterTuningJobPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListTrainingJobsForHyperParameterTuningJobPaginatorName
```

Values:

- `list_training_jobs_for_hyper_parameter_tuning_job`

## ListTrainingJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListTrainingJobsPaginatorName
```

Values:

- `list_training_jobs`

## ListTransformJobsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListTransformJobsPaginatorName
```

Values:

- `list_transform_jobs`

## ListTrialComponentsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListTrialComponentsPaginatorName
```

Values:

- `list_trial_components`

## ListTrialsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListTrialsPaginatorName
```

Values:

- `list_trials`

## ListUserProfilesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListUserProfilesPaginatorName
```

Values:

- `list_user_profiles`

## ListWorkforcesPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListWorkforcesPaginatorName
```

Values:

- `list_workforces`

## ListWorkforcesSortByOptions

```python
from mypy_boto3_sagemaker.literals import ListWorkforcesSortByOptions
```

Values:

- `CreateDate`
- `Name`

## ListWorkteamsPaginatorName

```python
from mypy_boto3_sagemaker.literals import ListWorkteamsPaginatorName
```

Values:

- `list_workteams`

## ListWorkteamsSortByOptions

```python
from mypy_boto3_sagemaker.literals import ListWorkteamsSortByOptions
```

Values:

- `CreateDate`
- `Name`

## ModelApprovalStatus

```python
from mypy_boto3_sagemaker.literals import ModelApprovalStatus
```

Values:

- `Approved`
- `PendingManualApproval`
- `Rejected`

## ModelCacheSetting

```python
from mypy_boto3_sagemaker.literals import ModelCacheSetting
```

Values:

- `Disabled`
- `Enabled`

## ModelPackageGroupSortBy

```python
from mypy_boto3_sagemaker.literals import ModelPackageGroupSortBy
```

Values:

- `CreationTime`
- `Name`

## ModelPackageGroupStatus

```python
from mypy_boto3_sagemaker.literals import ModelPackageGroupStatus
```

Values:

- `Completed`
- `DeleteFailed`
- `Deleting`
- `Failed`
- `InProgress`
- `Pending`

## ModelPackageSortBy

```python
from mypy_boto3_sagemaker.literals import ModelPackageSortBy
```

Values:

- `CreationTime`
- `Name`

## ModelPackageStatus

```python
from mypy_boto3_sagemaker.literals import ModelPackageStatus
```

Values:

- `Completed`
- `Deleting`
- `Failed`
- `InProgress`
- `Pending`

## ModelPackageType

```python
from mypy_boto3_sagemaker.literals import ModelPackageType
```

Values:

- `Both`
- `Unversioned`
- `Versioned`

## ModelSortKey

```python
from mypy_boto3_sagemaker.literals import ModelSortKey
```

Values:

- `CreationTime`
- `Name`

## MonitoringExecutionSortKey

```python
from mypy_boto3_sagemaker.literals import MonitoringExecutionSortKey
```

Values:

- `CreationTime`
- `ScheduledTime`
- `Status`

## MonitoringJobDefinitionSortKey

```python
from mypy_boto3_sagemaker.literals import MonitoringJobDefinitionSortKey
```

Values:

- `CreationTime`
- `Name`

## MonitoringProblemType

```python
from mypy_boto3_sagemaker.literals import MonitoringProblemType
```

Values:

- `BinaryClassification`
- `MulticlassClassification`
- `Regression`

## MonitoringScheduleSortKey

```python
from mypy_boto3_sagemaker.literals import MonitoringScheduleSortKey
```

Values:

- `CreationTime`
- `Name`
- `Status`

## MonitoringType

```python
from mypy_boto3_sagemaker.literals import MonitoringType
```

Values:

- `DataQuality`
- `ModelBias`
- `ModelExplainability`
- `ModelQuality`

## NotebookInstanceAcceleratorType

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceAcceleratorType
```

Values:

- `ml.eia1.large`
- `ml.eia1.medium`
- `ml.eia1.xlarge`
- `ml.eia2.large`
- `ml.eia2.medium`
- `ml.eia2.xlarge`

## NotebookInstanceDeletedWaiterName

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceDeletedWaiterName
```

Values:

- `notebook_instance_deleted`

## NotebookInstanceInServiceWaiterName

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceInServiceWaiterName
```

Values:

- `notebook_instance_in_service`

## NotebookInstanceLifecycleConfigSortKey

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceLifecycleConfigSortKey
```

Values:

- `CreationTime`
- `LastModifiedTime`
- `Name`

## NotebookInstanceLifecycleConfigSortOrder

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceLifecycleConfigSortOrder
```

Values:

- `Ascending`
- `Descending`

## NotebookInstanceSortKey

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceSortKey
```

Values:

- `CreationTime`
- `Name`
- `Status`

## NotebookInstanceSortOrder

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceSortOrder
```

Values:

- `Ascending`
- `Descending`

## NotebookInstanceStatus

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceStatus
```

Values:

- `Deleting`
- `Failed`
- `InService`
- `Pending`
- `Stopped`
- `Stopping`
- `Updating`

## NotebookInstanceStoppedWaiterName

```python
from mypy_boto3_sagemaker.literals import NotebookInstanceStoppedWaiterName
```

Values:

- `notebook_instance_stopped`

## NotebookOutputOption

```python
from mypy_boto3_sagemaker.literals import NotebookOutputOption
```

Values:

- `Allowed`
- `Disabled`

## ObjectiveStatus

```python
from mypy_boto3_sagemaker.literals import ObjectiveStatus
```

Values:

- `Failed`
- `Pending`
- `Succeeded`

## OfflineStoreStatusValue

```python
from mypy_boto3_sagemaker.literals import OfflineStoreStatusValue
```

Values:

- `Active`
- `Blocked`
- `Disabled`

## OrderKey

```python
from mypy_boto3_sagemaker.literals import OrderKey
```

Values:

- `Ascending`
- `Descending`

## ParameterType

```python
from mypy_boto3_sagemaker.literals import ParameterType
```

Values:

- `Categorical`
- `Continuous`
- `FreeText`
- `Integer`

## PipelineExecutionStatus

```python
from mypy_boto3_sagemaker.literals import PipelineExecutionStatus
```

Values:

- `Executing`
- `Failed`
- `Stopped`
- `Stopping`
- `Succeeded`

## PipelineStatus

```python
from mypy_boto3_sagemaker.literals import PipelineStatus
```

Values:

- `Active`

## ProblemType

```python
from mypy_boto3_sagemaker.literals import ProblemType
```

Values:

- `BinaryClassification`
- `MulticlassClassification`
- `Regression`

## ProcessingInstanceType

```python
from mypy_boto3_sagemaker.literals import ProcessingInstanceType
```

Values:

- `ml.c4.2xlarge`
- `ml.c4.4xlarge`
- `ml.c4.8xlarge`
- `ml.c4.xlarge`
- `ml.c5.18xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.xlarge`
- `ml.m4.10xlarge`
- `ml.m4.16xlarge`
- `ml.m4.2xlarge`
- `ml.m4.4xlarge`
- `ml.m4.xlarge`
- `ml.m5.12xlarge`
- `ml.m5.24xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.large`
- `ml.m5.xlarge`
- `ml.p2.16xlarge`
- `ml.p2.8xlarge`
- `ml.p2.xlarge`
- `ml.p3.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`
- `ml.r5.12xlarge`
- `ml.r5.16xlarge`
- `ml.r5.24xlarge`
- `ml.r5.2xlarge`
- `ml.r5.4xlarge`
- `ml.r5.8xlarge`
- `ml.r5.large`
- `ml.r5.xlarge`
- `ml.t3.2xlarge`
- `ml.t3.large`
- `ml.t3.medium`
- `ml.t3.xlarge`

## ProcessingJobCompletedOrStoppedWaiterName

```python
from mypy_boto3_sagemaker.literals import ProcessingJobCompletedOrStoppedWaiterName
```

Values:

- `processing_job_completed_or_stopped`

## ProcessingJobStatus

```python
from mypy_boto3_sagemaker.literals import ProcessingJobStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## ProcessingS3CompressionType

```python
from mypy_boto3_sagemaker.literals import ProcessingS3CompressionType
```

Values:

- `Gzip`
- `None`

## ProcessingS3DataDistributionType

```python
from mypy_boto3_sagemaker.literals import ProcessingS3DataDistributionType
```

Values:

- `FullyReplicated`
- `ShardedByS3Key`

## ProcessingS3DataType

```python
from mypy_boto3_sagemaker.literals import ProcessingS3DataType
```

Values:

- `ManifestFile`
- `S3Prefix`

## ProcessingS3InputMode

```python
from mypy_boto3_sagemaker.literals import ProcessingS3InputMode
```

Values:

- `File`
- `Pipe`

## ProcessingS3UploadMode

```python
from mypy_boto3_sagemaker.literals import ProcessingS3UploadMode
```

Values:

- `Continuous`
- `EndOfJob`

## ProductionVariantAcceleratorType

```python
from mypy_boto3_sagemaker.literals import ProductionVariantAcceleratorType
```

Values:

- `ml.eia1.large`
- `ml.eia1.medium`
- `ml.eia1.xlarge`
- `ml.eia2.large`
- `ml.eia2.medium`
- `ml.eia2.xlarge`

## ProductionVariantInstanceType

```python
from mypy_boto3_sagemaker.literals import ProductionVariantInstanceType
```

Values:

- `ml.c4.2xlarge`
- `ml.c4.4xlarge`
- `ml.c4.8xlarge`
- `ml.c4.large`
- `ml.c4.xlarge`
- `ml.c5.18xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.large`
- `ml.c5.xlarge`
- `ml.c5d.18xlarge`
- `ml.c5d.2xlarge`
- `ml.c5d.4xlarge`
- `ml.c5d.9xlarge`
- `ml.c5d.large`
- `ml.c5d.xlarge`
- `ml.g4dn.12xlarge`
- `ml.g4dn.16xlarge`
- `ml.g4dn.2xlarge`
- `ml.g4dn.4xlarge`
- `ml.g4dn.8xlarge`
- `ml.g4dn.xlarge`
- `ml.inf1.24xlarge`
- `ml.inf1.2xlarge`
- `ml.inf1.6xlarge`
- `ml.inf1.xlarge`
- `ml.m4.10xlarge`
- `ml.m4.16xlarge`
- `ml.m4.2xlarge`
- `ml.m4.4xlarge`
- `ml.m4.xlarge`
- `ml.m5.12xlarge`
- `ml.m5.24xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.large`
- `ml.m5.xlarge`
- `ml.m5d.12xlarge`
- `ml.m5d.24xlarge`
- `ml.m5d.2xlarge`
- `ml.m5d.4xlarge`
- `ml.m5d.large`
- `ml.m5d.xlarge`
- `ml.p2.16xlarge`
- `ml.p2.8xlarge`
- `ml.p2.xlarge`
- `ml.p3.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`
- `ml.r5.12xlarge`
- `ml.r5.24xlarge`
- `ml.r5.2xlarge`
- `ml.r5.4xlarge`
- `ml.r5.large`
- `ml.r5.xlarge`
- `ml.r5d.12xlarge`
- `ml.r5d.24xlarge`
- `ml.r5d.2xlarge`
- `ml.r5d.4xlarge`
- `ml.r5d.large`
- `ml.r5d.xlarge`
- `ml.t2.2xlarge`
- `ml.t2.large`
- `ml.t2.medium`
- `ml.t2.xlarge`

## ProfilingStatus

```python
from mypy_boto3_sagemaker.literals import ProfilingStatus
```

Values:

- `Disabled`
- `Enabled`

## ProjectSortBy

```python
from mypy_boto3_sagemaker.literals import ProjectSortBy
```

Values:

- `CreationTime`
- `Name`

## ProjectSortOrder

```python
from mypy_boto3_sagemaker.literals import ProjectSortOrder
```

Values:

- `Ascending`
- `Descending`

## ProjectStatus

```python
from mypy_boto3_sagemaker.literals import ProjectStatus
```

Values:

- `CreateCompleted`
- `CreateFailed`
- `CreateInProgress`
- `DeleteCompleted`
- `DeleteFailed`
- `DeleteInProgress`
- `Pending`

## RecordWrapper

```python
from mypy_boto3_sagemaker.literals import RecordWrapper
```

Values:

- `None`
- `RecordIO`

## RedshiftResultCompressionType

```python
from mypy_boto3_sagemaker.literals import RedshiftResultCompressionType
```

Values:

- `BZIP2`
- `GZIP`
- `None`
- `SNAPPY`
- `ZSTD`

## RedshiftResultFormat

```python
from mypy_boto3_sagemaker.literals import RedshiftResultFormat
```

Values:

- `CSV`
- `PARQUET`

## RepositoryAccessMode

```python
from mypy_boto3_sagemaker.literals import RepositoryAccessMode
```

Values:

- `Platform`
- `Vpc`

## ResourceType

```python
from mypy_boto3_sagemaker.literals import ResourceType
```

Values:

- `Endpoint`
- `Experiment`
- `ExperimentTrial`
- `ExperimentTrialComponent`
- `FeatureGroup`
- `ModelPackage`
- `ModelPackageGroup`
- `Pipeline`
- `PipelineExecution`
- `TrainingJob`

## RetentionType

```python
from mypy_boto3_sagemaker.literals import RetentionType
```

Values:

- `Delete`
- `Retain`

## RootAccess

```python
from mypy_boto3_sagemaker.literals import RootAccess
```

Values:

- `Disabled`
- `Enabled`

## RuleEvaluationStatus

```python
from mypy_boto3_sagemaker.literals import RuleEvaluationStatus
```

Values:

- `Error`
- `InProgress`
- `IssuesFound`
- `NoIssuesFound`
- `Stopped`
- `Stopping`

## S3DataDistribution

```python
from mypy_boto3_sagemaker.literals import S3DataDistribution
```

Values:

- `FullyReplicated`
- `ShardedByS3Key`

## S3DataType

```python
from mypy_boto3_sagemaker.literals import S3DataType
```

Values:

- `AugmentedManifestFile`
- `ManifestFile`
- `S3Prefix`

## SagemakerServicecatalogStatus

```python
from mypy_boto3_sagemaker.literals import SagemakerServicecatalogStatus
```

Values:

- `Disabled`
- `Enabled`

## ScheduleStatus

```python
from mypy_boto3_sagemaker.literals import ScheduleStatus
```

Values:

- `Failed`
- `Pending`
- `Scheduled`
- `Stopped`

## SearchPaginatorName

```python
from mypy_boto3_sagemaker.literals import SearchPaginatorName
```

Values:

- `search`

## SearchSortOrder

```python
from mypy_boto3_sagemaker.literals import SearchSortOrder
```

Values:

- `Ascending`
- `Descending`

## SecondaryStatus

```python
from mypy_boto3_sagemaker.literals import SecondaryStatus
```

Values:

- `Completed`
- `Downloading`
- `DownloadingTrainingImage`
- `Failed`
- `Interrupted`
- `LaunchingMLInstances`
- `MaxRuntimeExceeded`
- `MaxWaitTimeExceeded`
- `PreparingTrainingStack`
- `Starting`
- `Stopped`
- `Stopping`
- `Training`
- `Updating`
- `Uploading`

## SortActionsBy

```python
from mypy_boto3_sagemaker.literals import SortActionsBy
```

Values:

- `CreationTime`
- `Name`

## SortArtifactsBy

```python
from mypy_boto3_sagemaker.literals import SortArtifactsBy
```

Values:

- `CreationTime`

## SortAssociationsBy

```python
from mypy_boto3_sagemaker.literals import SortAssociationsBy
```

Values:

- `CreationTime`
- `DestinationArn`
- `DestinationType`
- `SourceArn`
- `SourceType`

## SortBy

```python
from mypy_boto3_sagemaker.literals import SortBy
```

Values:

- `CreationTime`
- `Name`
- `Status`

## SortContextsBy

```python
from mypy_boto3_sagemaker.literals import SortContextsBy
```

Values:

- `CreationTime`
- `Name`

## SortExperimentsBy

```python
from mypy_boto3_sagemaker.literals import SortExperimentsBy
```

Values:

- `CreationTime`
- `Name`

## SortOrder

```python
from mypy_boto3_sagemaker.literals import SortOrder
```

Values:

- `Ascending`
- `Descending`

## SortPipelineExecutionsBy

```python
from mypy_boto3_sagemaker.literals import SortPipelineExecutionsBy
```

Values:

- `CreationTime`
- `PipelineExecutionArn`

## SortPipelinesBy

```python
from mypy_boto3_sagemaker.literals import SortPipelinesBy
```

Values:

- `CreationTime`
- `Name`

## SortTrialComponentsBy

```python
from mypy_boto3_sagemaker.literals import SortTrialComponentsBy
```

Values:

- `CreationTime`
- `Name`

## SortTrialsBy

```python
from mypy_boto3_sagemaker.literals import SortTrialsBy
```

Values:

- `CreationTime`
- `Name`

## SplitType

```python
from mypy_boto3_sagemaker.literals import SplitType
```

Values:

- `Line`
- `None`
- `RecordIO`
- `TFRecord`

## StepStatus

```python
from mypy_boto3_sagemaker.literals import StepStatus
```

Values:

- `Executing`
- `Failed`
- `Starting`
- `Stopped`
- `Stopping`
- `Succeeded`

## TargetDevice

```python
from mypy_boto3_sagemaker.literals import TargetDevice
```

Values:

- `aisage`
- `amba_cv22`
- `coreml`
- `deeplens`
- `imx8qm`
- `jacinto_tda4vm`
- `jetson_nano`
- `jetson_tx1`
- `jetson_tx2`
- `jetson_xavier`
- `lambda`
- `ml_c4`
- `ml_c5`
- `ml_eia2`
- `ml_g4dn`
- `ml_inf1`
- `ml_m4`
- `ml_m5`
- `ml_p2`
- `ml_p3`
- `qcs603`
- `qcs605`
- `rasp3b`
- `rk3288`
- `rk3399`
- `sbe_c`
- `sitara_am57x`
- `x86_win32`
- `x86_win64`

## TargetPlatformAccelerator

```python
from mypy_boto3_sagemaker.literals import TargetPlatformAccelerator
```

Values:

- `INTEL_GRAPHICS`
- `MALI`
- `NVIDIA`

## TargetPlatformArch

```python
from mypy_boto3_sagemaker.literals import TargetPlatformArch
```

Values:

- `ARM64`
- `ARM_EABI`
- `ARM_EABIHF`
- `X86`
- `X86_64`

## TargetPlatformOs

```python
from mypy_boto3_sagemaker.literals import TargetPlatformOs
```

Values:

- `ANDROID`
- `LINUX`

## TrafficRoutingConfigType

```python
from mypy_boto3_sagemaker.literals import TrafficRoutingConfigType
```

Values:

- `ALL_AT_ONCE`
- `CANARY`

## TrainingInputMode

```python
from mypy_boto3_sagemaker.literals import TrainingInputMode
```

Values:

- `File`
- `Pipe`

## TrainingInstanceType

```python
from mypy_boto3_sagemaker.literals import TrainingInstanceType
```

Values:

- `ml.c4.2xlarge`
- `ml.c4.4xlarge`
- `ml.c4.8xlarge`
- `ml.c4.xlarge`
- `ml.c5.18xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.xlarge`
- `ml.c5n.18xlarge`
- `ml.c5n.2xlarge`
- `ml.c5n.4xlarge`
- `ml.c5n.9xlarge`
- `ml.c5n.xlarge`
- `ml.g4dn.12xlarge`
- `ml.g4dn.16xlarge`
- `ml.g4dn.2xlarge`
- `ml.g4dn.4xlarge`
- `ml.g4dn.8xlarge`
- `ml.g4dn.xlarge`
- `ml.m4.10xlarge`
- `ml.m4.16xlarge`
- `ml.m4.2xlarge`
- `ml.m4.4xlarge`
- `ml.m4.xlarge`
- `ml.m5.12xlarge`
- `ml.m5.24xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.large`
- `ml.m5.xlarge`
- `ml.p2.16xlarge`
- `ml.p2.8xlarge`
- `ml.p2.xlarge`
- `ml.p3.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`
- `ml.p3dn.24xlarge`
- `ml.p4d.24xlarge`

## TrainingJobCompletedOrStoppedWaiterName

```python
from mypy_boto3_sagemaker.literals import TrainingJobCompletedOrStoppedWaiterName
```

Values:

- `training_job_completed_or_stopped`

## TrainingJobEarlyStoppingType

```python
from mypy_boto3_sagemaker.literals import TrainingJobEarlyStoppingType
```

Values:

- `Auto`
- `Off`

## TrainingJobSortByOptions

```python
from mypy_boto3_sagemaker.literals import TrainingJobSortByOptions
```

Values:

- `CreationTime`
- `FinalObjectiveMetricValue`
- `Name`
- `Status`

## TrainingJobStatus

```python
from mypy_boto3_sagemaker.literals import TrainingJobStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## TransformInstanceType

```python
from mypy_boto3_sagemaker.literals import TransformInstanceType
```

Values:

- `ml.c4.2xlarge`
- `ml.c4.4xlarge`
- `ml.c4.8xlarge`
- `ml.c4.xlarge`
- `ml.c5.18xlarge`
- `ml.c5.2xlarge`
- `ml.c5.4xlarge`
- `ml.c5.9xlarge`
- `ml.c5.xlarge`
- `ml.m4.10xlarge`
- `ml.m4.16xlarge`
- `ml.m4.2xlarge`
- `ml.m4.4xlarge`
- `ml.m4.xlarge`
- `ml.m5.12xlarge`
- `ml.m5.24xlarge`
- `ml.m5.2xlarge`
- `ml.m5.4xlarge`
- `ml.m5.large`
- `ml.m5.xlarge`
- `ml.p2.16xlarge`
- `ml.p2.8xlarge`
- `ml.p2.xlarge`
- `ml.p3.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.8xlarge`

## TransformJobCompletedOrStoppedWaiterName

```python
from mypy_boto3_sagemaker.literals import TransformJobCompletedOrStoppedWaiterName
```

Values:

- `transform_job_completed_or_stopped`

## TransformJobStatus

```python
from mypy_boto3_sagemaker.literals import TransformJobStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## TrialComponentPrimaryStatus

```python
from mypy_boto3_sagemaker.literals import TrialComponentPrimaryStatus
```

Values:

- `Completed`
- `Failed`
- `InProgress`
- `Stopped`
- `Stopping`

## UserProfileSortKey

```python
from mypy_boto3_sagemaker.literals import UserProfileSortKey
```

Values:

- `CreationTime`
- `LastModifiedTime`

## UserProfileStatus

```python
from mypy_boto3_sagemaker.literals import UserProfileStatus
```

Values:

- `Delete_Failed`
- `Deleting`
- `Failed`
- `InService`
- `Pending`
- `Update_Failed`
- `Updating`

## VariantPropertyType

```python
from mypy_boto3_sagemaker.literals import VariantPropertyType
```

Values:

- `DataCaptureConfig`
- `DesiredInstanceCount`
- `DesiredWeight`
