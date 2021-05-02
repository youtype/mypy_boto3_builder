# Structures for boto3 SageMaker module

> [Index](../index.md) > [SageMaker](./index.md) > Structures

Auto-generated documentation for [SageMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker)
type annotations stubs module [mypy_boto3_sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/).

- [Structures for boto3 SageMaker module](#structures-for-boto3-sagemaker-module)
  - [ActionSourceTypeDef](#actionsourcetypedef)
  - [ActionSummaryTypeDef](#actionsummarytypedef)
  - [AddAssociationResponseTypeDef](#addassociationresponsetypedef)
  - [AddTagsOutputTypeDef](#addtagsoutputtypedef)
  - [AgentVersionTypeDef](#agentversiontypedef)
  - [AlarmTypeDef](#alarmtypedef)
  - [AlgorithmSpecificationTypeDef](#algorithmspecificationtypedef)
  - [AlgorithmStatusDetailsTypeDef](#algorithmstatusdetailstypedef)
  - [AlgorithmStatusItemTypeDef](#algorithmstatusitemtypedef)
  - [AlgorithmSummaryTypeDef](#algorithmsummarytypedef)
  - [AlgorithmValidationProfileTypeDef](#algorithmvalidationprofiletypedef)
  - [AlgorithmValidationSpecificationTypeDef](#algorithmvalidationspecificationtypedef)
  - [AnnotationConsolidationConfigTypeDef](#annotationconsolidationconfigtypedef)
  - [AppDetailsTypeDef](#appdetailstypedef)
  - [AppImageConfigDetailsTypeDef](#appimageconfigdetailstypedef)
  - [AppSpecificationTypeDef](#appspecificationtypedef)
  - [ArtifactSourceTypeDef](#artifactsourcetypedef)
  - [ArtifactSourceTypeTypeDef](#artifactsourcetypetypedef)
  - [ArtifactSummaryTypeDef](#artifactsummarytypedef)
  - [AssociateTrialComponentResponseTypeDef](#associatetrialcomponentresponsetypedef)
  - [AssociationSummaryTypeDef](#associationsummarytypedef)
  - [AthenaDatasetDefinitionTypeDef](#athenadatasetdefinitiontypedef)
  - [AutoMLCandidateStepTypeDef](#automlcandidatesteptypedef)
  - [AutoMLCandidateTypeDef](#automlcandidatetypedef)
  - [AutoMLChannelTypeDef](#automlchanneltypedef)
  - [AutoMLContainerDefinitionTypeDef](#automlcontainerdefinitiontypedef)
  - [AutoMLDataSourceTypeDef](#automldatasourcetypedef)
  - [AutoMLJobArtifactsTypeDef](#automljobartifactstypedef)
  - [AutoMLJobCompletionCriteriaTypeDef](#automljobcompletioncriteriatypedef)
  - [AutoMLJobConfigTypeDef](#automljobconfigtypedef)
  - [AutoMLJobObjectiveTypeDef](#automljobobjectivetypedef)
  - [AutoMLJobSummaryTypeDef](#automljobsummarytypedef)
  - [AutoMLOutputDataConfigTypeDef](#automloutputdataconfigtypedef)
  - [AutoMLPartialFailureReasonTypeDef](#automlpartialfailurereasontypedef)
  - [AutoMLS3DataSourceTypeDef](#automls3datasourcetypedef)
  - [AutoMLSecurityConfigTypeDef](#automlsecurityconfigtypedef)
  - [AutoRollbackConfigTypeDef](#autorollbackconfigtypedef)
  - [BiasTypeDef](#biastypedef)
  - [BlueGreenUpdatePolicyTypeDef](#bluegreenupdatepolicytypedef)
  - [CacheHitResultTypeDef](#cachehitresulttypedef)
  - [CandidateArtifactLocationsTypeDef](#candidateartifactlocationstypedef)
  - [CandidatePropertiesTypeDef](#candidatepropertiestypedef)
  - [CapacitySizeTypeDef](#capacitysizetypedef)
  - [CaptureContentTypeHeaderTypeDef](#capturecontenttypeheadertypedef)
  - [CaptureOptionTypeDef](#captureoptiontypedef)
  - [CategoricalParameterRangeSpecificationTypeDef](#categoricalparameterrangespecificationtypedef)
  - [CategoricalParameterRangeTypeDef](#categoricalparameterrangetypedef)
  - [ChannelSpecificationTypeDef](#channelspecificationtypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [CheckpointConfigTypeDef](#checkpointconfigtypedef)
  - [CodeRepositorySummaryTypeDef](#coderepositorysummarytypedef)
  - [CognitoConfigTypeDef](#cognitoconfigtypedef)
  - [CognitoMemberDefinitionTypeDef](#cognitomemberdefinitiontypedef)
  - [CollectionConfigurationTypeDef](#collectionconfigurationtypedef)
  - [CompilationJobSummaryTypeDef](#compilationjobsummarytypedef)
  - [ConditionStepMetadataTypeDef](#conditionstepmetadatatypedef)
  - [ContainerDefinitionTypeDef](#containerdefinitiontypedef)
  - [ContextSourceTypeDef](#contextsourcetypedef)
  - [ContextSummaryTypeDef](#contextsummarytypedef)
  - [ContinuousParameterRangeSpecificationTypeDef](#continuousparameterrangespecificationtypedef)
  - [ContinuousParameterRangeTypeDef](#continuousparameterrangetypedef)
  - [CreateActionResponseTypeDef](#createactionresponsetypedef)
  - [CreateAlgorithmOutputTypeDef](#createalgorithmoutputtypedef)
  - [CreateAppImageConfigResponseTypeDef](#createappimageconfigresponsetypedef)
  - [CreateAppResponseTypeDef](#createappresponsetypedef)
  - [CreateArtifactResponseTypeDef](#createartifactresponsetypedef)
  - [CreateAutoMLJobResponseTypeDef](#createautomljobresponsetypedef)
  - [CreateCodeRepositoryOutputTypeDef](#createcoderepositoryoutputtypedef)
  - [CreateCompilationJobResponseTypeDef](#createcompilationjobresponsetypedef)
  - [CreateContextResponseTypeDef](#createcontextresponsetypedef)
  - [CreateDataQualityJobDefinitionResponseTypeDef](#createdataqualityjobdefinitionresponsetypedef)
  - [CreateDomainResponseTypeDef](#createdomainresponsetypedef)
  - [CreateEndpointConfigOutputTypeDef](#createendpointconfigoutputtypedef)
  - [CreateEndpointOutputTypeDef](#createendpointoutputtypedef)
  - [CreateExperimentResponseTypeDef](#createexperimentresponsetypedef)
  - [CreateFeatureGroupResponseTypeDef](#createfeaturegroupresponsetypedef)
  - [CreateFlowDefinitionResponseTypeDef](#createflowdefinitionresponsetypedef)
  - [CreateHumanTaskUiResponseTypeDef](#createhumantaskuiresponsetypedef)
  - [CreateHyperParameterTuningJobResponseTypeDef](#createhyperparametertuningjobresponsetypedef)
  - [CreateImageResponseTypeDef](#createimageresponsetypedef)
  - [CreateImageVersionResponseTypeDef](#createimageversionresponsetypedef)
  - [CreateLabelingJobResponseTypeDef](#createlabelingjobresponsetypedef)
  - [CreateModelBiasJobDefinitionResponseTypeDef](#createmodelbiasjobdefinitionresponsetypedef)
  - [CreateModelExplainabilityJobDefinitionResponseTypeDef](#createmodelexplainabilityjobdefinitionresponsetypedef)
  - [CreateModelOutputTypeDef](#createmodeloutputtypedef)
  - [CreateModelPackageGroupOutputTypeDef](#createmodelpackagegroupoutputtypedef)
  - [CreateModelPackageOutputTypeDef](#createmodelpackageoutputtypedef)
  - [CreateModelQualityJobDefinitionResponseTypeDef](#createmodelqualityjobdefinitionresponsetypedef)
  - [CreateMonitoringScheduleResponseTypeDef](#createmonitoringscheduleresponsetypedef)
  - [CreateNotebookInstanceLifecycleConfigOutputTypeDef](#createnotebookinstancelifecycleconfigoutputtypedef)
  - [CreateNotebookInstanceOutputTypeDef](#createnotebookinstanceoutputtypedef)
  - [CreatePipelineResponseTypeDef](#createpipelineresponsetypedef)
  - [CreatePresignedDomainUrlResponseTypeDef](#createpresigneddomainurlresponsetypedef)
  - [CreatePresignedNotebookInstanceUrlOutputTypeDef](#createpresignednotebookinstanceurloutputtypedef)
  - [CreateProcessingJobResponseTypeDef](#createprocessingjobresponsetypedef)
  - [CreateProjectOutputTypeDef](#createprojectoutputtypedef)
  - [CreateTrainingJobResponseTypeDef](#createtrainingjobresponsetypedef)
  - [CreateTransformJobResponseTypeDef](#createtransformjobresponsetypedef)
  - [CreateTrialComponentResponseTypeDef](#createtrialcomponentresponsetypedef)
  - [CreateTrialResponseTypeDef](#createtrialresponsetypedef)
  - [CreateUserProfileResponseTypeDef](#createuserprofileresponsetypedef)
  - [CreateWorkforceResponseTypeDef](#createworkforceresponsetypedef)
  - [CreateWorkteamResponseTypeDef](#createworkteamresponsetypedef)
  - [CustomImageTypeDef](#customimagetypedef)
  - [DataCaptureConfigSummaryTypeDef](#datacaptureconfigsummarytypedef)
  - [DataCaptureConfigTypeDef](#datacaptureconfigtypedef)
  - [DataCatalogConfigTypeDef](#datacatalogconfigtypedef)
  - [DataProcessingTypeDef](#dataprocessingtypedef)
  - [DataQualityAppSpecificationTypeDef](#dataqualityappspecificationtypedef)
  - [DataQualityBaselineConfigTypeDef](#dataqualitybaselineconfigtypedef)
  - [DataQualityJobInputTypeDef](#dataqualityjobinputtypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [DatasetDefinitionTypeDef](#datasetdefinitiontypedef)
  - [DebugHookConfigTypeDef](#debughookconfigtypedef)
  - [DebugRuleConfigurationTypeDef](#debugruleconfigurationtypedef)
  - [DebugRuleEvaluationStatusTypeDef](#debugruleevaluationstatustypedef)
  - [DeleteActionResponseTypeDef](#deleteactionresponsetypedef)
  - [DeleteArtifactResponseTypeDef](#deleteartifactresponsetypedef)
  - [DeleteAssociationResponseTypeDef](#deleteassociationresponsetypedef)
  - [DeleteContextResponseTypeDef](#deletecontextresponsetypedef)
  - [DeleteExperimentResponseTypeDef](#deleteexperimentresponsetypedef)
  - [DeletePipelineResponseTypeDef](#deletepipelineresponsetypedef)
  - [DeleteTrialComponentResponseTypeDef](#deletetrialcomponentresponsetypedef)
  - [DeleteTrialResponseTypeDef](#deletetrialresponsetypedef)
  - [DeleteWorkteamResponseTypeDef](#deleteworkteamresponsetypedef)
  - [DeployedImageTypeDef](#deployedimagetypedef)
  - [DeploymentConfigTypeDef](#deploymentconfigtypedef)
  - [DescribeActionResponseTypeDef](#describeactionresponsetypedef)
  - [DescribeAlgorithmOutputTypeDef](#describealgorithmoutputtypedef)
  - [DescribeAppImageConfigResponseTypeDef](#describeappimageconfigresponsetypedef)
  - [DescribeAppResponseTypeDef](#describeappresponsetypedef)
  - [DescribeArtifactResponseTypeDef](#describeartifactresponsetypedef)
  - [DescribeAutoMLJobResponseTypeDef](#describeautomljobresponsetypedef)
  - [DescribeCodeRepositoryOutputTypeDef](#describecoderepositoryoutputtypedef)
  - [DescribeCompilationJobResponseTypeDef](#describecompilationjobresponsetypedef)
  - [DescribeContextResponseTypeDef](#describecontextresponsetypedef)
  - [DescribeDataQualityJobDefinitionResponseTypeDef](#describedataqualityjobdefinitionresponsetypedef)
  - [DescribeDeviceFleetResponseTypeDef](#describedevicefleetresponsetypedef)
  - [DescribeDeviceResponseTypeDef](#describedeviceresponsetypedef)
  - [DescribeDomainResponseTypeDef](#describedomainresponsetypedef)
  - [DescribeEdgePackagingJobResponseTypeDef](#describeedgepackagingjobresponsetypedef)
  - [DescribeEndpointConfigOutputTypeDef](#describeendpointconfigoutputtypedef)
  - [DescribeEndpointOutputTypeDef](#describeendpointoutputtypedef)
  - [DescribeExperimentResponseTypeDef](#describeexperimentresponsetypedef)
  - [DescribeFeatureGroupResponseTypeDef](#describefeaturegroupresponsetypedef)
  - [DescribeFlowDefinitionResponseTypeDef](#describeflowdefinitionresponsetypedef)
  - [DescribeHumanTaskUiResponseTypeDef](#describehumantaskuiresponsetypedef)
  - [DescribeHyperParameterTuningJobResponseTypeDef](#describehyperparametertuningjobresponsetypedef)
  - [DescribeImageResponseTypeDef](#describeimageresponsetypedef)
  - [DescribeImageVersionResponseTypeDef](#describeimageversionresponsetypedef)
  - [DescribeLabelingJobResponseTypeDef](#describelabelingjobresponsetypedef)
  - [DescribeModelBiasJobDefinitionResponseTypeDef](#describemodelbiasjobdefinitionresponsetypedef)
  - [DescribeModelExplainabilityJobDefinitionResponseTypeDef](#describemodelexplainabilityjobdefinitionresponsetypedef)
  - [DescribeModelOutputTypeDef](#describemodeloutputtypedef)
  - [DescribeModelPackageGroupOutputTypeDef](#describemodelpackagegroupoutputtypedef)
  - [DescribeModelPackageOutputTypeDef](#describemodelpackageoutputtypedef)
  - [DescribeModelQualityJobDefinitionResponseTypeDef](#describemodelqualityjobdefinitionresponsetypedef)
  - [DescribeMonitoringScheduleResponseTypeDef](#describemonitoringscheduleresponsetypedef)
  - [DescribeNotebookInstanceLifecycleConfigOutputTypeDef](#describenotebookinstancelifecycleconfigoutputtypedef)
  - [DescribeNotebookInstanceOutputTypeDef](#describenotebookinstanceoutputtypedef)
  - [DescribePipelineDefinitionForExecutionResponseTypeDef](#describepipelinedefinitionforexecutionresponsetypedef)
  - [DescribePipelineExecutionResponseTypeDef](#describepipelineexecutionresponsetypedef)
  - [DescribePipelineResponseTypeDef](#describepipelineresponsetypedef)
  - [DescribeProcessingJobResponseTypeDef](#describeprocessingjobresponsetypedef)
  - [DescribeProjectOutputTypeDef](#describeprojectoutputtypedef)
  - [DescribeSubscribedWorkteamResponseTypeDef](#describesubscribedworkteamresponsetypedef)
  - [DescribeTrainingJobResponseTypeDef](#describetrainingjobresponsetypedef)
  - [DescribeTransformJobResponseTypeDef](#describetransformjobresponsetypedef)
  - [DescribeTrialComponentResponseTypeDef](#describetrialcomponentresponsetypedef)
  - [DescribeTrialResponseTypeDef](#describetrialresponsetypedef)
  - [DescribeUserProfileResponseTypeDef](#describeuserprofileresponsetypedef)
  - [DescribeWorkforceResponseTypeDef](#describeworkforceresponsetypedef)
  - [DescribeWorkteamResponseTypeDef](#describeworkteamresponsetypedef)
  - [DesiredWeightAndCapacityTypeDef](#desiredweightandcapacitytypedef)
  - [DeviceFleetSummaryTypeDef](#devicefleetsummarytypedef)
  - [DeviceStatsTypeDef](#devicestatstypedef)
  - [DeviceSummaryTypeDef](#devicesummarytypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [DisassociateTrialComponentResponseTypeDef](#disassociatetrialcomponentresponsetypedef)
  - [DomainDetailsTypeDef](#domaindetailstypedef)
  - [EdgeModelStatTypeDef](#edgemodelstattypedef)
  - [EdgeModelSummaryTypeDef](#edgemodelsummarytypedef)
  - [EdgeModelTypeDef](#edgemodeltypedef)
  - [EdgeOutputConfigTypeDef](#edgeoutputconfigtypedef)
  - [EdgePackagingJobSummaryTypeDef](#edgepackagingjobsummarytypedef)
  - [EndpointConfigSummaryTypeDef](#endpointconfigsummarytypedef)
  - [EndpointInputTypeDef](#endpointinputtypedef)
  - [EndpointSummaryTypeDef](#endpointsummarytypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [ExperimentConfigTypeDef](#experimentconfigtypedef)
  - [ExperimentSourceTypeDef](#experimentsourcetypedef)
  - [ExperimentSummaryTypeDef](#experimentsummarytypedef)
  - [ExperimentTypeDef](#experimenttypedef)
  - [ExplainabilityTypeDef](#explainabilitytypedef)
  - [FeatureDefinitionTypeDef](#featuredefinitiontypedef)
  - [FeatureGroupSummaryTypeDef](#featuregroupsummarytypedef)
  - [FeatureGroupTypeDef](#featuregrouptypedef)
  - [FileSystemConfigTypeDef](#filesystemconfigtypedef)
  - [FileSystemDataSourceTypeDef](#filesystemdatasourcetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [FinalAutoMLJobObjectiveMetricTypeDef](#finalautomljobobjectivemetrictypedef)
  - [FinalHyperParameterTuningJobObjectiveMetricTypeDef](#finalhyperparametertuningjobobjectivemetrictypedef)
  - [FlowDefinitionOutputConfigTypeDef](#flowdefinitionoutputconfigtypedef)
  - [FlowDefinitionSummaryTypeDef](#flowdefinitionsummarytypedef)
  - [GetDeviceFleetReportResponseTypeDef](#getdevicefleetreportresponsetypedef)
  - [GetModelPackageGroupPolicyOutputTypeDef](#getmodelpackagegrouppolicyoutputtypedef)
  - [GetSagemakerServicecatalogPortfolioStatusOutputTypeDef](#getsagemakerservicecatalogportfoliostatusoutputtypedef)
  - [GetSearchSuggestionsResponseTypeDef](#getsearchsuggestionsresponsetypedef)
  - [GitConfigForUpdateTypeDef](#gitconfigforupdatetypedef)
  - [GitConfigTypeDef](#gitconfigtypedef)
  - [HumanLoopActivationConditionsConfigTypeDef](#humanloopactivationconditionsconfigtypedef)
  - [HumanLoopActivationConfigTypeDef](#humanloopactivationconfigtypedef)
  - [HumanLoopConfigTypeDef](#humanloopconfigtypedef)
  - [HumanLoopRequestSourceTypeDef](#humanlooprequestsourcetypedef)
  - [HumanTaskConfigTypeDef](#humantaskconfigtypedef)
  - [HumanTaskUiSummaryTypeDef](#humantaskuisummarytypedef)
  - [HyperParameterAlgorithmSpecificationTypeDef](#hyperparameteralgorithmspecificationtypedef)
  - [HyperParameterSpecificationTypeDef](#hyperparameterspecificationtypedef)
  - [HyperParameterTrainingJobDefinitionTypeDef](#hyperparametertrainingjobdefinitiontypedef)
  - [HyperParameterTrainingJobSummaryTypeDef](#hyperparametertrainingjobsummarytypedef)
  - [HyperParameterTuningJobConfigTypeDef](#hyperparametertuningjobconfigtypedef)
  - [HyperParameterTuningJobObjectiveTypeDef](#hyperparametertuningjobobjectivetypedef)
  - [HyperParameterTuningJobSummaryTypeDef](#hyperparametertuningjobsummarytypedef)
  - [HyperParameterTuningJobWarmStartConfigTypeDef](#hyperparametertuningjobwarmstartconfigtypedef)
  - [ImageConfigTypeDef](#imageconfigtypedef)
  - [ImageTypeDef](#imagetypedef)
  - [ImageVersionTypeDef](#imageversiontypedef)
  - [InferenceExecutionConfigTypeDef](#inferenceexecutionconfigtypedef)
  - [InferenceSpecificationTypeDef](#inferencespecificationtypedef)
  - [InputConfigTypeDef](#inputconfigtypedef)
  - [IntegerParameterRangeSpecificationTypeDef](#integerparameterrangespecificationtypedef)
  - [IntegerParameterRangeTypeDef](#integerparameterrangetypedef)
  - [JupyterServerAppSettingsTypeDef](#jupyterserverappsettingstypedef)
  - [KernelGatewayAppSettingsTypeDef](#kernelgatewayappsettingstypedef)
  - [KernelGatewayImageConfigTypeDef](#kernelgatewayimageconfigtypedef)
  - [KernelSpecTypeDef](#kernelspectypedef)
  - [LabelCountersForWorkteamTypeDef](#labelcountersforworkteamtypedef)
  - [LabelCountersTypeDef](#labelcounterstypedef)
  - [LabelingJobAlgorithmsConfigTypeDef](#labelingjobalgorithmsconfigtypedef)
  - [LabelingJobDataAttributesTypeDef](#labelingjobdataattributestypedef)
  - [LabelingJobDataSourceTypeDef](#labelingjobdatasourcetypedef)
  - [LabelingJobForWorkteamSummaryTypeDef](#labelingjobforworkteamsummarytypedef)
  - [LabelingJobInputConfigTypeDef](#labelingjobinputconfigtypedef)
  - [LabelingJobOutputConfigTypeDef](#labelingjoboutputconfigtypedef)
  - [LabelingJobOutputTypeDef](#labelingjoboutputtypedef)
  - [LabelingJobResourceConfigTypeDef](#labelingjobresourceconfigtypedef)
  - [LabelingJobS3DataSourceTypeDef](#labelingjobs3datasourcetypedef)
  - [LabelingJobSnsDataSourceTypeDef](#labelingjobsnsdatasourcetypedef)
  - [LabelingJobStoppingConditionsTypeDef](#labelingjobstoppingconditionstypedef)
  - [LabelingJobSummaryTypeDef](#labelingjobsummarytypedef)
  - [ListActionsResponseTypeDef](#listactionsresponsetypedef)
  - [ListAlgorithmsOutputTypeDef](#listalgorithmsoutputtypedef)
  - [ListAppImageConfigsResponseTypeDef](#listappimageconfigsresponsetypedef)
  - [ListAppsResponseTypeDef](#listappsresponsetypedef)
  - [ListArtifactsResponseTypeDef](#listartifactsresponsetypedef)
  - [ListAssociationsResponseTypeDef](#listassociationsresponsetypedef)
  - [ListAutoMLJobsResponseTypeDef](#listautomljobsresponsetypedef)
  - [ListCandidatesForAutoMLJobResponseTypeDef](#listcandidatesforautomljobresponsetypedef)
  - [ListCodeRepositoriesOutputTypeDef](#listcoderepositoriesoutputtypedef)
  - [ListCompilationJobsResponseTypeDef](#listcompilationjobsresponsetypedef)
  - [ListContextsResponseTypeDef](#listcontextsresponsetypedef)
  - [ListDataQualityJobDefinitionsResponseTypeDef](#listdataqualityjobdefinitionsresponsetypedef)
  - [ListDeviceFleetsResponseTypeDef](#listdevicefleetsresponsetypedef)
  - [ListDevicesResponseTypeDef](#listdevicesresponsetypedef)
  - [ListDomainsResponseTypeDef](#listdomainsresponsetypedef)
  - [ListEdgePackagingJobsResponseTypeDef](#listedgepackagingjobsresponsetypedef)
  - [ListEndpointConfigsOutputTypeDef](#listendpointconfigsoutputtypedef)
  - [ListEndpointsOutputTypeDef](#listendpointsoutputtypedef)
  - [ListExperimentsResponseTypeDef](#listexperimentsresponsetypedef)
  - [ListFeatureGroupsResponseTypeDef](#listfeaturegroupsresponsetypedef)
  - [ListFlowDefinitionsResponseTypeDef](#listflowdefinitionsresponsetypedef)
  - [ListHumanTaskUisResponseTypeDef](#listhumantaskuisresponsetypedef)
  - [ListHyperParameterTuningJobsResponseTypeDef](#listhyperparametertuningjobsresponsetypedef)
  - [ListImageVersionsResponseTypeDef](#listimageversionsresponsetypedef)
  - [ListImagesResponseTypeDef](#listimagesresponsetypedef)
  - [ListLabelingJobsForWorkteamResponseTypeDef](#listlabelingjobsforworkteamresponsetypedef)
  - [ListLabelingJobsResponseTypeDef](#listlabelingjobsresponsetypedef)
  - [ListModelBiasJobDefinitionsResponseTypeDef](#listmodelbiasjobdefinitionsresponsetypedef)
  - [ListModelExplainabilityJobDefinitionsResponseTypeDef](#listmodelexplainabilityjobdefinitionsresponsetypedef)
  - [ListModelPackageGroupsOutputTypeDef](#listmodelpackagegroupsoutputtypedef)
  - [ListModelPackagesOutputTypeDef](#listmodelpackagesoutputtypedef)
  - [ListModelQualityJobDefinitionsResponseTypeDef](#listmodelqualityjobdefinitionsresponsetypedef)
  - [ListModelsOutputTypeDef](#listmodelsoutputtypedef)
  - [ListMonitoringExecutionsResponseTypeDef](#listmonitoringexecutionsresponsetypedef)
  - [ListMonitoringSchedulesResponseTypeDef](#listmonitoringschedulesresponsetypedef)
  - [ListNotebookInstanceLifecycleConfigsOutputTypeDef](#listnotebookinstancelifecycleconfigsoutputtypedef)
  - [ListNotebookInstancesOutputTypeDef](#listnotebookinstancesoutputtypedef)
  - [ListPipelineExecutionStepsResponseTypeDef](#listpipelineexecutionstepsresponsetypedef)
  - [ListPipelineExecutionsResponseTypeDef](#listpipelineexecutionsresponsetypedef)
  - [ListPipelineParametersForExecutionResponseTypeDef](#listpipelineparametersforexecutionresponsetypedef)
  - [ListPipelinesResponseTypeDef](#listpipelinesresponsetypedef)
  - [ListProcessingJobsResponseTypeDef](#listprocessingjobsresponsetypedef)
  - [ListProjectsOutputTypeDef](#listprojectsoutputtypedef)
  - [ListSubscribedWorkteamsResponseTypeDef](#listsubscribedworkteamsresponsetypedef)
  - [ListTagsOutputTypeDef](#listtagsoutputtypedef)
  - [ListTrainingJobsForHyperParameterTuningJobResponseTypeDef](#listtrainingjobsforhyperparametertuningjobresponsetypedef)
  - [ListTrainingJobsResponseTypeDef](#listtrainingjobsresponsetypedef)
  - [ListTransformJobsResponseTypeDef](#listtransformjobsresponsetypedef)
  - [ListTrialComponentsResponseTypeDef](#listtrialcomponentsresponsetypedef)
  - [ListTrialsResponseTypeDef](#listtrialsresponsetypedef)
  - [ListUserProfilesResponseTypeDef](#listuserprofilesresponsetypedef)
  - [ListWorkforcesResponseTypeDef](#listworkforcesresponsetypedef)
  - [ListWorkteamsResponseTypeDef](#listworkteamsresponsetypedef)
  - [MemberDefinitionTypeDef](#memberdefinitiontypedef)
  - [MetadataPropertiesTypeDef](#metadatapropertiestypedef)
  - [MetricDataTypeDef](#metricdatatypedef)
  - [MetricDefinitionTypeDef](#metricdefinitiontypedef)
  - [MetricsSourceTypeDef](#metricssourcetypedef)
  - [ModelArtifactsTypeDef](#modelartifactstypedef)
  - [ModelBiasAppSpecificationTypeDef](#modelbiasappspecificationtypedef)
  - [ModelBiasBaselineConfigTypeDef](#modelbiasbaselineconfigtypedef)
  - [ModelBiasJobInputTypeDef](#modelbiasjobinputtypedef)
  - [ModelClientConfigTypeDef](#modelclientconfigtypedef)
  - [ModelDataQualityTypeDef](#modeldataqualitytypedef)
  - [ModelDigestsTypeDef](#modeldigeststypedef)
  - [ModelExplainabilityAppSpecificationTypeDef](#modelexplainabilityappspecificationtypedef)
  - [ModelExplainabilityBaselineConfigTypeDef](#modelexplainabilitybaselineconfigtypedef)
  - [ModelExplainabilityJobInputTypeDef](#modelexplainabilityjobinputtypedef)
  - [ModelMetricsTypeDef](#modelmetricstypedef)
  - [ModelPackageContainerDefinitionTypeDef](#modelpackagecontainerdefinitiontypedef)
  - [ModelPackageGroupSummaryTypeDef](#modelpackagegroupsummarytypedef)
  - [ModelPackageGroupTypeDef](#modelpackagegrouptypedef)
  - [ModelPackageStatusDetailsTypeDef](#modelpackagestatusdetailstypedef)
  - [ModelPackageStatusItemTypeDef](#modelpackagestatusitemtypedef)
  - [ModelPackageSummaryTypeDef](#modelpackagesummarytypedef)
  - [ModelPackageTypeDef](#modelpackagetypedef)
  - [ModelPackageValidationProfileTypeDef](#modelpackagevalidationprofiletypedef)
  - [ModelPackageValidationSpecificationTypeDef](#modelpackagevalidationspecificationtypedef)
  - [ModelQualityAppSpecificationTypeDef](#modelqualityappspecificationtypedef)
  - [ModelQualityBaselineConfigTypeDef](#modelqualitybaselineconfigtypedef)
  - [ModelQualityJobInputTypeDef](#modelqualityjobinputtypedef)
  - [ModelQualityTypeDef](#modelqualitytypedef)
  - [ModelStepMetadataTypeDef](#modelstepmetadatatypedef)
  - [ModelSummaryTypeDef](#modelsummarytypedef)
  - [MonitoringAppSpecificationTypeDef](#monitoringappspecificationtypedef)
  - [MonitoringBaselineConfigTypeDef](#monitoringbaselineconfigtypedef)
  - [MonitoringClusterConfigTypeDef](#monitoringclusterconfigtypedef)
  - [MonitoringConstraintsResourceTypeDef](#monitoringconstraintsresourcetypedef)
  - [MonitoringExecutionSummaryTypeDef](#monitoringexecutionsummarytypedef)
  - [MonitoringGroundTruthS3InputTypeDef](#monitoringgroundtruths3inputtypedef)
  - [MonitoringInputTypeDef](#monitoringinputtypedef)
  - [MonitoringJobDefinitionSummaryTypeDef](#monitoringjobdefinitionsummarytypedef)
  - [MonitoringJobDefinitionTypeDef](#monitoringjobdefinitiontypedef)
  - [MonitoringNetworkConfigTypeDef](#monitoringnetworkconfigtypedef)
  - [MonitoringOutputConfigTypeDef](#monitoringoutputconfigtypedef)
  - [MonitoringOutputTypeDef](#monitoringoutputtypedef)
  - [MonitoringResourcesTypeDef](#monitoringresourcestypedef)
  - [MonitoringS3OutputTypeDef](#monitorings3outputtypedef)
  - [MonitoringScheduleConfigTypeDef](#monitoringscheduleconfigtypedef)
  - [MonitoringScheduleSummaryTypeDef](#monitoringschedulesummarytypedef)
  - [MonitoringScheduleTypeDef](#monitoringscheduletypedef)
  - [MonitoringStatisticsResourceTypeDef](#monitoringstatisticsresourcetypedef)
  - [MonitoringStoppingConditionTypeDef](#monitoringstoppingconditiontypedef)
  - [MultiModelConfigTypeDef](#multimodelconfigtypedef)
  - [NestedFiltersTypeDef](#nestedfilterstypedef)
  - [NetworkConfigTypeDef](#networkconfigtypedef)
  - [NotebookInstanceLifecycleConfigSummaryTypeDef](#notebookinstancelifecycleconfigsummarytypedef)
  - [NotebookInstanceLifecycleHookTypeDef](#notebookinstancelifecyclehooktypedef)
  - [NotebookInstanceSummaryTypeDef](#notebookinstancesummarytypedef)
  - [NotificationConfigurationTypeDef](#notificationconfigurationtypedef)
  - [ObjectiveStatusCountersTypeDef](#objectivestatuscounterstypedef)
  - [OfflineStoreConfigTypeDef](#offlinestoreconfigtypedef)
  - [OfflineStoreStatusTypeDef](#offlinestorestatustypedef)
  - [OidcConfigForResponseTypeDef](#oidcconfigforresponsetypedef)
  - [OidcConfigTypeDef](#oidcconfigtypedef)
  - [OidcMemberDefinitionTypeDef](#oidcmemberdefinitiontypedef)
  - [OnlineStoreConfigTypeDef](#onlinestoreconfigtypedef)
  - [OnlineStoreSecurityConfigTypeDef](#onlinestoresecurityconfigtypedef)
  - [OutputConfigTypeDef](#outputconfigtypedef)
  - [OutputDataConfigTypeDef](#outputdataconfigtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParameterRangeTypeDef](#parameterrangetypedef)
  - [ParameterRangesTypeDef](#parameterrangestypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [ParentHyperParameterTuningJobTypeDef](#parenthyperparametertuningjobtypedef)
  - [ParentTypeDef](#parenttypedef)
  - [PipelineExecutionStepMetadataTypeDef](#pipelineexecutionstepmetadatatypedef)
  - [PipelineExecutionStepTypeDef](#pipelineexecutionsteptypedef)
  - [PipelineExecutionSummaryTypeDef](#pipelineexecutionsummarytypedef)
  - [PipelineExecutionTypeDef](#pipelineexecutiontypedef)
  - [PipelineSummaryTypeDef](#pipelinesummarytypedef)
  - [PipelineTypeDef](#pipelinetypedef)
  - [ProcessingClusterConfigTypeDef](#processingclusterconfigtypedef)
  - [ProcessingFeatureStoreOutputTypeDef](#processingfeaturestoreoutputtypedef)
  - [ProcessingInputTypeDef](#processinginputtypedef)
  - [ProcessingJobStepMetadataTypeDef](#processingjobstepmetadatatypedef)
  - [ProcessingJobSummaryTypeDef](#processingjobsummarytypedef)
  - [ProcessingJobTypeDef](#processingjobtypedef)
  - [ProcessingOutputConfigTypeDef](#processingoutputconfigtypedef)
  - [ProcessingOutputTypeDef](#processingoutputtypedef)
  - [ProcessingResourcesTypeDef](#processingresourcestypedef)
  - [ProcessingS3InputTypeDef](#processings3inputtypedef)
  - [ProcessingS3OutputTypeDef](#processings3outputtypedef)
  - [ProcessingStoppingConditionTypeDef](#processingstoppingconditiontypedef)
  - [ProductionVariantCoreDumpConfigTypeDef](#productionvariantcoredumpconfigtypedef)
  - [ProductionVariantSummaryTypeDef](#productionvariantsummarytypedef)
  - [ProductionVariantTypeDef](#productionvarianttypedef)
  - [ProfilerConfigForUpdateTypeDef](#profilerconfigforupdatetypedef)
  - [ProfilerConfigTypeDef](#profilerconfigtypedef)
  - [ProfilerRuleConfigurationTypeDef](#profilerruleconfigurationtypedef)
  - [ProfilerRuleEvaluationStatusTypeDef](#profilerruleevaluationstatustypedef)
  - [ProjectSummaryTypeDef](#projectsummarytypedef)
  - [PropertyNameQueryTypeDef](#propertynamequerytypedef)
  - [PropertyNameSuggestionTypeDef](#propertynamesuggestiontypedef)
  - [ProvisioningParameterTypeDef](#provisioningparametertypedef)
  - [PublicWorkforceTaskPriceTypeDef](#publicworkforcetaskpricetypedef)
  - [PutModelPackageGroupPolicyOutputTypeDef](#putmodelpackagegrouppolicyoutputtypedef)
  - [RedshiftDatasetDefinitionTypeDef](#redshiftdatasetdefinitiontypedef)
  - [RegisterModelStepMetadataTypeDef](#registermodelstepmetadatatypedef)
  - [RenderUiTemplateResponseTypeDef](#renderuitemplateresponsetypedef)
  - [RenderableTaskTypeDef](#renderabletasktypedef)
  - [RenderingErrorTypeDef](#renderingerrortypedef)
  - [RepositoryAuthConfigTypeDef](#repositoryauthconfigtypedef)
  - [ResolvedAttributesTypeDef](#resolvedattributestypedef)
  - [ResourceConfigTypeDef](#resourceconfigtypedef)
  - [ResourceLimitsTypeDef](#resourcelimitstypedef)
  - [ResourceSpecTypeDef](#resourcespectypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RetentionPolicyTypeDef](#retentionpolicytypedef)
  - [S3DataSourceTypeDef](#s3datasourcetypedef)
  - [S3StorageConfigTypeDef](#s3storageconfigtypedef)
  - [ScheduleConfigTypeDef](#scheduleconfigtypedef)
  - [SearchExpressionTypeDef](#searchexpressiontypedef)
  - [SearchRecordTypeDef](#searchrecordtypedef)
  - [SearchResponseTypeDef](#searchresponsetypedef)
  - [SecondaryStatusTransitionTypeDef](#secondarystatustransitiontypedef)
  - [ServiceCatalogProvisionedProductDetailsTypeDef](#servicecatalogprovisionedproductdetailstypedef)
  - [ServiceCatalogProvisioningDetailsTypeDef](#servicecatalogprovisioningdetailstypedef)
  - [SharingSettingsTypeDef](#sharingsettingstypedef)
  - [ShuffleConfigTypeDef](#shuffleconfigtypedef)
  - [SourceAlgorithmSpecificationTypeDef](#sourcealgorithmspecificationtypedef)
  - [SourceAlgorithmTypeDef](#sourcealgorithmtypedef)
  - [SourceIpConfigTypeDef](#sourceipconfigtypedef)
  - [StartPipelineExecutionResponseTypeDef](#startpipelineexecutionresponsetypedef)
  - [StopPipelineExecutionResponseTypeDef](#stoppipelineexecutionresponsetypedef)
  - [StoppingConditionTypeDef](#stoppingconditiontypedef)
  - [SubscribedWorkteamTypeDef](#subscribedworkteamtypedef)
  - [SuggestionQueryTypeDef](#suggestionquerytypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetPlatformTypeDef](#targetplatformtypedef)
  - [TensorBoardAppSettingsTypeDef](#tensorboardappsettingstypedef)
  - [TensorBoardOutputConfigTypeDef](#tensorboardoutputconfigtypedef)
  - [TrafficRoutingConfigTypeDef](#trafficroutingconfigtypedef)
  - [TrainingJobDefinitionTypeDef](#trainingjobdefinitiontypedef)
  - [TrainingJobStatusCountersTypeDef](#trainingjobstatuscounterstypedef)
  - [TrainingJobStepMetadataTypeDef](#trainingjobstepmetadatatypedef)
  - [TrainingJobSummaryTypeDef](#trainingjobsummarytypedef)
  - [TrainingJobTypeDef](#trainingjobtypedef)
  - [TrainingSpecificationTypeDef](#trainingspecificationtypedef)
  - [TransformDataSourceTypeDef](#transformdatasourcetypedef)
  - [TransformInputTypeDef](#transforminputtypedef)
  - [TransformJobDefinitionTypeDef](#transformjobdefinitiontypedef)
  - [TransformJobStepMetadataTypeDef](#transformjobstepmetadatatypedef)
  - [TransformJobSummaryTypeDef](#transformjobsummarytypedef)
  - [TransformJobTypeDef](#transformjobtypedef)
  - [TransformOutputTypeDef](#transformoutputtypedef)
  - [TransformResourcesTypeDef](#transformresourcestypedef)
  - [TransformS3DataSourceTypeDef](#transforms3datasourcetypedef)
  - [TrialComponentArtifactTypeDef](#trialcomponentartifacttypedef)
  - [TrialComponentMetricSummaryTypeDef](#trialcomponentmetricsummarytypedef)
  - [TrialComponentParameterValueTypeDef](#trialcomponentparametervaluetypedef)
  - [TrialComponentSimpleSummaryTypeDef](#trialcomponentsimplesummarytypedef)
  - [TrialComponentSourceDetailTypeDef](#trialcomponentsourcedetailtypedef)
  - [TrialComponentSourceTypeDef](#trialcomponentsourcetypedef)
  - [TrialComponentStatusTypeDef](#trialcomponentstatustypedef)
  - [TrialComponentSummaryTypeDef](#trialcomponentsummarytypedef)
  - [TrialComponentTypeDef](#trialcomponenttypedef)
  - [TrialSourceTypeDef](#trialsourcetypedef)
  - [TrialSummaryTypeDef](#trialsummarytypedef)
  - [TrialTypeDef](#trialtypedef)
  - [TuningJobCompletionCriteriaTypeDef](#tuningjobcompletioncriteriatypedef)
  - [USDTypeDef](#usdtypedef)
  - [UiConfigTypeDef](#uiconfigtypedef)
  - [UiTemplateInfoTypeDef](#uitemplateinfotypedef)
  - [UiTemplateTypeDef](#uitemplatetypedef)
  - [UpdateActionResponseTypeDef](#updateactionresponsetypedef)
  - [UpdateAppImageConfigResponseTypeDef](#updateappimageconfigresponsetypedef)
  - [UpdateArtifactResponseTypeDef](#updateartifactresponsetypedef)
  - [UpdateCodeRepositoryOutputTypeDef](#updatecoderepositoryoutputtypedef)
  - [UpdateContextResponseTypeDef](#updatecontextresponsetypedef)
  - [UpdateDomainResponseTypeDef](#updatedomainresponsetypedef)
  - [UpdateEndpointOutputTypeDef](#updateendpointoutputtypedef)
  - [UpdateEndpointWeightsAndCapacitiesOutputTypeDef](#updateendpointweightsandcapacitiesoutputtypedef)
  - [UpdateExperimentResponseTypeDef](#updateexperimentresponsetypedef)
  - [UpdateImageResponseTypeDef](#updateimageresponsetypedef)
  - [UpdateModelPackageOutputTypeDef](#updatemodelpackageoutputtypedef)
  - [UpdateMonitoringScheduleResponseTypeDef](#updatemonitoringscheduleresponsetypedef)
  - [UpdatePipelineExecutionResponseTypeDef](#updatepipelineexecutionresponsetypedef)
  - [UpdatePipelineResponseTypeDef](#updatepipelineresponsetypedef)
  - [UpdateTrainingJobResponseTypeDef](#updatetrainingjobresponsetypedef)
  - [UpdateTrialComponentResponseTypeDef](#updatetrialcomponentresponsetypedef)
  - [UpdateTrialResponseTypeDef](#updatetrialresponsetypedef)
  - [UpdateUserProfileResponseTypeDef](#updateuserprofileresponsetypedef)
  - [UpdateWorkforceResponseTypeDef](#updateworkforceresponsetypedef)
  - [UpdateWorkteamResponseTypeDef](#updateworkteamresponsetypedef)
  - [UserContextTypeDef](#usercontexttypedef)
  - [UserProfileDetailsTypeDef](#userprofiledetailstypedef)
  - [UserSettingsTypeDef](#usersettingstypedef)
  - [VariantPropertyTypeDef](#variantpropertytypedef)
  - [VpcConfigTypeDef](#vpcconfigtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)
  - [WorkforceTypeDef](#workforcetypedef)
  - [WorkteamTypeDef](#workteamtypedef)

## ActionSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ActionSourceTypeDef
```


Required fields:
- `SourceUri`: `str`



Optional fields:
- `SourceType`: `str`
- `SourceId`: `str`


## ActionSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ActionSummaryTypeDef
```




Optional fields:
- `ActionArn`: `str`
- `ActionName`: `str`
- `Source`: `"ActionSourceTypeDef"`
- `ActionType`: `str`
- `Status`: `ActionStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## AddAssociationResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AddAssociationResponseTypeDef
```




Optional fields:
- `SourceArn`: `str`
- `DestinationArn`: `str`


## AddTagsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AddTagsOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## AgentVersionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AgentVersionTypeDef
```


Required fields:
- `Version`: `str`
- `AgentCount`: `int`




## AlarmTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlarmTypeDef
```




Optional fields:
- `AlarmName`: `str`


## AlgorithmSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlgorithmSpecificationTypeDef
```


Required fields:
- `TrainingInputMode`: `TrainingInputMode`



Optional fields:
- `TrainingImage`: `str`
- `AlgorithmName`: `str`
- `MetricDefinitions`: `List["MetricDefinitionTypeDef"]`
- `EnableSageMakerMetricsTimeSeries`: `bool`


## AlgorithmStatusDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlgorithmStatusDetailsTypeDef
```




Optional fields:
- `ValidationStatuses`: `List["AlgorithmStatusItemTypeDef"]`
- `ImageScanStatuses`: `List["AlgorithmStatusItemTypeDef"]`


## AlgorithmStatusItemTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlgorithmStatusItemTypeDef
```


Required fields:
- `Name`: `str`
- `Status`: `DetailedAlgorithmStatus`



Optional fields:
- `FailureReason`: `str`


## AlgorithmSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlgorithmSummaryTypeDef
```


Required fields:
- `AlgorithmName`: `str`
- `AlgorithmArn`: `str`
- `CreationTime`: `datetime`
- `AlgorithmStatus`: `AlgorithmStatus`



Optional fields:
- `AlgorithmDescription`: `str`


## AlgorithmValidationProfileTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlgorithmValidationProfileTypeDef
```


Required fields:
- `ProfileName`: `str`
- `TrainingJobDefinition`: `"TrainingJobDefinitionTypeDef"`



Optional fields:
- `TransformJobDefinition`: `"TransformJobDefinitionTypeDef"`


## AlgorithmValidationSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AlgorithmValidationSpecificationTypeDef
```


Required fields:
- `ValidationRole`: `str`
- `ValidationProfiles`: `List["AlgorithmValidationProfileTypeDef"]`




## AnnotationConsolidationConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AnnotationConsolidationConfigTypeDef
```


Required fields:
- `AnnotationConsolidationLambdaArn`: `str`




## AppDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AppDetailsTypeDef
```




Optional fields:
- `DomainId`: `str`
- `UserProfileName`: `str`
- `AppType`: `AppType`
- `AppName`: `str`
- `Status`: `AppStatus`
- `CreationTime`: `datetime`


## AppImageConfigDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AppImageConfigDetailsTypeDef
```




Optional fields:
- `AppImageConfigArn`: `str`
- `AppImageConfigName`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `KernelGatewayImageConfig`: `"KernelGatewayImageConfigTypeDef"`


## AppSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AppSpecificationTypeDef
```


Required fields:
- `ImageUri`: `str`



Optional fields:
- `ContainerEntrypoint`: `List[str]`
- `ContainerArguments`: `List[str]`


## ArtifactSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ArtifactSourceTypeDef
```


Required fields:
- `SourceUri`: `str`



Optional fields:
- `SourceTypes`: `List["ArtifactSourceTypeTypeDef"]`


## ArtifactSourceTypeTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ArtifactSourceTypeTypeDef
```


Required fields:
- `SourceIdType`: `ArtifactSourceIdType`
- `Value`: `str`




## ArtifactSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ArtifactSummaryTypeDef
```




Optional fields:
- `ArtifactArn`: `str`
- `ArtifactName`: `str`
- `Source`: `"ArtifactSourceTypeDef"`
- `ArtifactType`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## AssociateTrialComponentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AssociateTrialComponentResponseTypeDef
```




Optional fields:
- `TrialComponentArn`: `str`
- `TrialArn`: `str`


## AssociationSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AssociationSummaryTypeDef
```




Optional fields:
- `SourceArn`: `str`
- `DestinationArn`: `str`
- `SourceType`: `str`
- `DestinationType`: `str`
- `AssociationType`: `AssociationEdgeType`
- `SourceName`: `str`
- `DestinationName`: `str`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`


## AthenaDatasetDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AthenaDatasetDefinitionTypeDef
```


Required fields:
- `Catalog`: `str`
- `Database`: `str`
- `QueryString`: `str`
- `OutputS3Uri`: `str`
- `OutputFormat`: `AthenaResultFormat`



Optional fields:
- `WorkGroup`: `str`
- `KmsKeyId`: `str`
- `OutputCompression`: `AthenaResultCompressionType`


## AutoMLCandidateStepTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLCandidateStepTypeDef
```


Required fields:
- `CandidateStepType`: `CandidateStepType`
- `CandidateStepArn`: `str`
- `CandidateStepName`: `str`




## AutoMLCandidateTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLCandidateTypeDef
```


Required fields:
- `CandidateName`: `str`
- `ObjectiveStatus`: `ObjectiveStatus`
- `CandidateSteps`: `List["AutoMLCandidateStepTypeDef"]`
- `CandidateStatus`: `CandidateStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `FinalAutoMLJobObjectiveMetric`: `"FinalAutoMLJobObjectiveMetricTypeDef"`
- `InferenceContainers`: `List["AutoMLContainerDefinitionTypeDef"]`
- `EndTime`: `datetime`
- `FailureReason`: `str`
- `CandidateProperties`: `"CandidatePropertiesTypeDef"`


## AutoMLChannelTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLChannelTypeDef
```


Required fields:
- `DataSource`: `"AutoMLDataSourceTypeDef"`
- `TargetAttributeName`: `str`



Optional fields:
- `CompressionType`: `CompressionType`


## AutoMLContainerDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLContainerDefinitionTypeDef
```


Required fields:
- `Image`: `str`
- `ModelDataUrl`: `str`



Optional fields:
- `Environment`: `Dict[str, str]`


## AutoMLDataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLDataSourceTypeDef
```


Required fields:
- `S3DataSource`: `"AutoMLS3DataSourceTypeDef"`




## AutoMLJobArtifactsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLJobArtifactsTypeDef
```




Optional fields:
- `CandidateDefinitionNotebookLocation`: `str`
- `DataExplorationNotebookLocation`: `str`


## AutoMLJobCompletionCriteriaTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLJobCompletionCriteriaTypeDef
```




Optional fields:
- `MaxCandidates`: `int`
- `MaxRuntimePerTrainingJobInSeconds`: `int`
- `MaxAutoMLJobRuntimeInSeconds`: `int`


## AutoMLJobConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLJobConfigTypeDef
```




Optional fields:
- `CompletionCriteria`: `"AutoMLJobCompletionCriteriaTypeDef"`
- `SecurityConfig`: `"AutoMLSecurityConfigTypeDef"`


## AutoMLJobObjectiveTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLJobObjectiveTypeDef
```


Required fields:
- `MetricName`: `AutoMLMetricEnum`




## AutoMLJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLJobSummaryTypeDef
```


Required fields:
- `AutoMLJobName`: `str`
- `AutoMLJobArn`: `str`
- `AutoMLJobStatus`: `AutoMLJobStatus`
- `AutoMLJobSecondaryStatus`: `AutoMLJobSecondaryStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `EndTime`: `datetime`
- `FailureReason`: `str`
- `PartialFailureReasons`: `List["AutoMLPartialFailureReasonTypeDef"]`


## AutoMLOutputDataConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLOutputDataConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `KmsKeyId`: `str`


## AutoMLPartialFailureReasonTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLPartialFailureReasonTypeDef
```




Optional fields:
- `PartialFailureMessage`: `str`


## AutoMLS3DataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLS3DataSourceTypeDef
```


Required fields:
- `S3DataType`: `AutoMLS3DataType`
- `S3Uri`: `str`




## AutoMLSecurityConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoMLSecurityConfigTypeDef
```




Optional fields:
- `VolumeKmsKeyId`: `str`
- `EnableInterContainerTrafficEncryption`: `bool`
- `VpcConfig`: `"VpcConfigTypeDef"`


## AutoRollbackConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import AutoRollbackConfigTypeDef
```




Optional fields:
- `Alarms`: `List["AlarmTypeDef"]`


## BiasTypeDef

```python
from mypy_boto3_sagemaker.type_defs import BiasTypeDef
```




Optional fields:
- `Report`: `"MetricsSourceTypeDef"`


## BlueGreenUpdatePolicyTypeDef

```python
from mypy_boto3_sagemaker.type_defs import BlueGreenUpdatePolicyTypeDef
```


Required fields:
- `TrafficRoutingConfiguration`: `"TrafficRoutingConfigTypeDef"`



Optional fields:
- `TerminationWaitInSeconds`: `int`
- `MaximumExecutionTimeoutInSeconds`: `int`


## CacheHitResultTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CacheHitResultTypeDef
```




Optional fields:
- `SourcePipelineExecutionArn`: `str`


## CandidateArtifactLocationsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CandidateArtifactLocationsTypeDef
```


Required fields:
- `Explainability`: `str`




## CandidatePropertiesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CandidatePropertiesTypeDef
```




Optional fields:
- `CandidateArtifactLocations`: `"CandidateArtifactLocationsTypeDef"`


## CapacitySizeTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CapacitySizeTypeDef
```


Required fields:
- `Type`: `CapacitySizeType`
- `Value`: `int`




## CaptureContentTypeHeaderTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CaptureContentTypeHeaderTypeDef
```




Optional fields:
- `CsvContentTypes`: `List[str]`
- `JsonContentTypes`: `List[str]`


## CaptureOptionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CaptureOptionTypeDef
```


Required fields:
- `CaptureMode`: `CaptureMode`




## CategoricalParameterRangeSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CategoricalParameterRangeSpecificationTypeDef
```


Required fields:
- `Values`: `List[str]`




## CategoricalParameterRangeTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CategoricalParameterRangeTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[str]`




## ChannelSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ChannelSpecificationTypeDef
```


Required fields:
- `Name`: `str`
- `SupportedContentTypes`: `List[str]`
- `SupportedInputModes`: `List[TrainingInputMode]`



Optional fields:
- `Description`: `str`
- `IsRequired`: `bool`
- `SupportedCompressionTypes`: `List[CompressionType]`


## ChannelTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ChannelTypeDef
```


Required fields:
- `ChannelName`: `str`
- `DataSource`: `"DataSourceTypeDef"`



Optional fields:
- `ContentType`: `str`
- `CompressionType`: `CompressionType`
- `RecordWrapperType`: `RecordWrapper`
- `InputMode`: `TrainingInputMode`
- `ShuffleConfig`: `"ShuffleConfigTypeDef"`


## CheckpointConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CheckpointConfigTypeDef
```


Required fields:
- `S3Uri`: `str`



Optional fields:
- `LocalPath`: `str`


## CodeRepositorySummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CodeRepositorySummaryTypeDef
```


Required fields:
- `CodeRepositoryName`: `str`
- `CodeRepositoryArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `GitConfig`: `"GitConfigTypeDef"`


## CognitoConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CognitoConfigTypeDef
```


Required fields:
- `UserPool`: `str`
- `ClientId`: `str`




## CognitoMemberDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CognitoMemberDefinitionTypeDef
```


Required fields:
- `UserPool`: `str`
- `UserGroup`: `str`
- `ClientId`: `str`




## CollectionConfigurationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CollectionConfigurationTypeDef
```




Optional fields:
- `CollectionName`: `str`
- `CollectionParameters`: `Dict[str, str]`


## CompilationJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CompilationJobSummaryTypeDef
```


Required fields:
- `CompilationJobName`: `str`
- `CompilationJobArn`: `str`
- `CreationTime`: `datetime`
- `CompilationJobStatus`: `CompilationJobStatus`



Optional fields:
- `CompilationStartTime`: `datetime`
- `CompilationEndTime`: `datetime`
- `CompilationTargetDevice`: `TargetDevice`
- `CompilationTargetPlatformOs`: `TargetPlatformOs`
- `CompilationTargetPlatformArch`: `TargetPlatformArch`
- `CompilationTargetPlatformAccelerator`: `TargetPlatformAccelerator`
- `LastModifiedTime`: `datetime`


## ConditionStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ConditionStepMetadataTypeDef
```




Optional fields:
- `Outcome`: `ConditionOutcome`


## ContainerDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ContainerDefinitionTypeDef
```




Optional fields:
- `ContainerHostname`: `str`
- `Image`: `str`
- `ImageConfig`: `"ImageConfigTypeDef"`
- `Mode`: `ContainerMode`
- `ModelDataUrl`: `str`
- `Environment`: `Dict[str, str]`
- `ModelPackageName`: `str`
- `MultiModelConfig`: `"MultiModelConfigTypeDef"`


## ContextSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ContextSourceTypeDef
```


Required fields:
- `SourceUri`: `str`



Optional fields:
- `SourceType`: `str`
- `SourceId`: `str`


## ContextSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ContextSummaryTypeDef
```




Optional fields:
- `ContextArn`: `str`
- `ContextName`: `str`
- `Source`: `"ContextSourceTypeDef"`
- `ContextType`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## ContinuousParameterRangeSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ContinuousParameterRangeSpecificationTypeDef
```


Required fields:
- `MinValue`: `str`
- `MaxValue`: `str`




## ContinuousParameterRangeTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ContinuousParameterRangeTypeDef
```


Required fields:
- `Name`: `str`
- `MinValue`: `str`
- `MaxValue`: `str`



Optional fields:
- `ScalingType`: `HyperParameterScalingType`


## CreateActionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateActionResponseTypeDef
```




Optional fields:
- `ActionArn`: `str`


## CreateAlgorithmOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateAlgorithmOutputTypeDef
```


Required fields:
- `AlgorithmArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateAppImageConfigResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateAppImageConfigResponseTypeDef
```




Optional fields:
- `AppImageConfigArn`: `str`


## CreateAppResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateAppResponseTypeDef
```




Optional fields:
- `AppArn`: `str`


## CreateArtifactResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateArtifactResponseTypeDef
```




Optional fields:
- `ArtifactArn`: `str`


## CreateAutoMLJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateAutoMLJobResponseTypeDef
```


Required fields:
- `AutoMLJobArn`: `str`




## CreateCodeRepositoryOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateCodeRepositoryOutputTypeDef
```


Required fields:
- `CodeRepositoryArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateCompilationJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateCompilationJobResponseTypeDef
```


Required fields:
- `CompilationJobArn`: `str`




## CreateContextResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateContextResponseTypeDef
```




Optional fields:
- `ContextArn`: `str`


## CreateDataQualityJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateDataQualityJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`




## CreateDomainResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateDomainResponseTypeDef
```




Optional fields:
- `DomainArn`: `str`
- `Url`: `str`


## CreateEndpointConfigOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateEndpointConfigOutputTypeDef
```


Required fields:
- `EndpointConfigArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateEndpointOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateEndpointOutputTypeDef
```


Required fields:
- `EndpointArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateExperimentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateExperimentResponseTypeDef
```




Optional fields:
- `ExperimentArn`: `str`


## CreateFeatureGroupResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateFeatureGroupResponseTypeDef
```


Required fields:
- `FeatureGroupArn`: `str`




## CreateFlowDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateFlowDefinitionResponseTypeDef
```


Required fields:
- `FlowDefinitionArn`: `str`




## CreateHumanTaskUiResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateHumanTaskUiResponseTypeDef
```


Required fields:
- `HumanTaskUiArn`: `str`




## CreateHyperParameterTuningJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateHyperParameterTuningJobResponseTypeDef
```


Required fields:
- `HyperParameterTuningJobArn`: `str`




## CreateImageResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateImageResponseTypeDef
```




Optional fields:
- `ImageArn`: `str`


## CreateImageVersionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateImageVersionResponseTypeDef
```




Optional fields:
- `ImageVersionArn`: `str`


## CreateLabelingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateLabelingJobResponseTypeDef
```


Required fields:
- `LabelingJobArn`: `str`




## CreateModelBiasJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateModelBiasJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`




## CreateModelExplainabilityJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateModelExplainabilityJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`




## CreateModelOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateModelOutputTypeDef
```


Required fields:
- `ModelArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateModelPackageGroupOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateModelPackageGroupOutputTypeDef
```


Required fields:
- `ModelPackageGroupArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateModelPackageOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateModelPackageOutputTypeDef
```


Required fields:
- `ModelPackageArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateModelQualityJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateModelQualityJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`




## CreateMonitoringScheduleResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateMonitoringScheduleResponseTypeDef
```


Required fields:
- `MonitoringScheduleArn`: `str`




## CreateNotebookInstanceLifecycleConfigOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateNotebookInstanceLifecycleConfigOutputTypeDef
```




Optional fields:
- `NotebookInstanceLifecycleConfigArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateNotebookInstanceOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateNotebookInstanceOutputTypeDef
```




Optional fields:
- `NotebookInstanceArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePipelineResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreatePipelineResponseTypeDef
```




Optional fields:
- `PipelineArn`: `str`


## CreatePresignedDomainUrlResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreatePresignedDomainUrlResponseTypeDef
```




Optional fields:
- `AuthorizedUrl`: `str`


## CreatePresignedNotebookInstanceUrlOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreatePresignedNotebookInstanceUrlOutputTypeDef
```




Optional fields:
- `AuthorizedUrl`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateProcessingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateProcessingJobResponseTypeDef
```


Required fields:
- `ProcessingJobArn`: `str`




## CreateProjectOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateProjectOutputTypeDef
```


Required fields:
- `ProjectArn`: `str`
- `ProjectId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateTrainingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateTrainingJobResponseTypeDef
```


Required fields:
- `TrainingJobArn`: `str`




## CreateTransformJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateTransformJobResponseTypeDef
```


Required fields:
- `TransformJobArn`: `str`




## CreateTrialComponentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateTrialComponentResponseTypeDef
```




Optional fields:
- `TrialComponentArn`: `str`


## CreateTrialResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateTrialResponseTypeDef
```




Optional fields:
- `TrialArn`: `str`


## CreateUserProfileResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateUserProfileResponseTypeDef
```




Optional fields:
- `UserProfileArn`: `str`


## CreateWorkforceResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateWorkforceResponseTypeDef
```


Required fields:
- `WorkforceArn`: `str`




## CreateWorkteamResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CreateWorkteamResponseTypeDef
```




Optional fields:
- `WorkteamArn`: `str`


## CustomImageTypeDef

```python
from mypy_boto3_sagemaker.type_defs import CustomImageTypeDef
```


Required fields:
- `ImageName`: `str`
- `AppImageConfigName`: `str`



Optional fields:
- `ImageVersionNumber`: `int`


## DataCaptureConfigSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataCaptureConfigSummaryTypeDef
```


Required fields:
- `EnableCapture`: `bool`
- `CaptureStatus`: `CaptureStatus`
- `CurrentSamplingPercentage`: `int`
- `DestinationS3Uri`: `str`
- `KmsKeyId`: `str`




## DataCaptureConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataCaptureConfigTypeDef
```


Required fields:
- `InitialSamplingPercentage`: `int`
- `DestinationS3Uri`: `str`
- `CaptureOptions`: `List["CaptureOptionTypeDef"]`



Optional fields:
- `EnableCapture`: `bool`
- `KmsKeyId`: `str`
- `CaptureContentTypeHeader`: `"CaptureContentTypeHeaderTypeDef"`


## DataCatalogConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataCatalogConfigTypeDef
```


Required fields:
- `TableName`: `str`
- `Catalog`: `str`
- `Database`: `str`




## DataProcessingTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataProcessingTypeDef
```




Optional fields:
- `InputFilter`: `str`
- `OutputFilter`: `str`
- `JoinSource`: `JoinSource`


## DataQualityAppSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataQualityAppSpecificationTypeDef
```


Required fields:
- `ImageUri`: `str`



Optional fields:
- `ContainerEntrypoint`: `List[str]`
- `ContainerArguments`: `List[str]`
- `RecordPreprocessorSourceUri`: `str`
- `PostAnalyticsProcessorSourceUri`: `str`
- `Environment`: `Dict[str, str]`


## DataQualityBaselineConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataQualityBaselineConfigTypeDef
```




Optional fields:
- `BaseliningJobName`: `str`
- `ConstraintsResource`: `"MonitoringConstraintsResourceTypeDef"`
- `StatisticsResource`: `"MonitoringStatisticsResourceTypeDef"`


## DataQualityJobInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataQualityJobInputTypeDef
```


Required fields:
- `EndpointInput`: `"EndpointInputTypeDef"`




## DataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DataSourceTypeDef
```




Optional fields:
- `S3DataSource`: `"S3DataSourceTypeDef"`
- `FileSystemDataSource`: `"FileSystemDataSourceTypeDef"`


## DatasetDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DatasetDefinitionTypeDef
```




Optional fields:
- `AthenaDatasetDefinition`: `"AthenaDatasetDefinitionTypeDef"`
- `RedshiftDatasetDefinition`: `"RedshiftDatasetDefinitionTypeDef"`
- `LocalPath`: `str`
- `DataDistributionType`: `DataDistributionType`
- `InputMode`: `InputMode`


## DebugHookConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DebugHookConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `LocalPath`: `str`
- `HookParameters`: `Dict[str, str]`
- `CollectionConfigurations`: `List["CollectionConfigurationTypeDef"]`


## DebugRuleConfigurationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DebugRuleConfigurationTypeDef
```


Required fields:
- `RuleConfigurationName`: `str`
- `RuleEvaluatorImage`: `str`



Optional fields:
- `LocalPath`: `str`
- `S3OutputPath`: `str`
- `InstanceType`: `ProcessingInstanceType`
- `VolumeSizeInGB`: `int`
- `RuleParameters`: `Dict[str, str]`


## DebugRuleEvaluationStatusTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DebugRuleEvaluationStatusTypeDef
```




Optional fields:
- `RuleConfigurationName`: `str`
- `RuleEvaluationJobArn`: `str`
- `RuleEvaluationStatus`: `RuleEvaluationStatus`
- `StatusDetails`: `str`
- `LastModifiedTime`: `datetime`


## DeleteActionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteActionResponseTypeDef
```




Optional fields:
- `ActionArn`: `str`


## DeleteArtifactResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteArtifactResponseTypeDef
```




Optional fields:
- `ArtifactArn`: `str`


## DeleteAssociationResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteAssociationResponseTypeDef
```




Optional fields:
- `SourceArn`: `str`
- `DestinationArn`: `str`


## DeleteContextResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteContextResponseTypeDef
```




Optional fields:
- `ContextArn`: `str`


## DeleteExperimentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteExperimentResponseTypeDef
```




Optional fields:
- `ExperimentArn`: `str`


## DeletePipelineResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeletePipelineResponseTypeDef
```




Optional fields:
- `PipelineArn`: `str`


## DeleteTrialComponentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteTrialComponentResponseTypeDef
```




Optional fields:
- `TrialComponentArn`: `str`


## DeleteTrialResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteTrialResponseTypeDef
```




Optional fields:
- `TrialArn`: `str`


## DeleteWorkteamResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeleteWorkteamResponseTypeDef
```


Required fields:
- `Success`: `bool`




## DeployedImageTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeployedImageTypeDef
```




Optional fields:
- `SpecifiedImage`: `str`
- `ResolvedImage`: `str`
- `ResolutionTime`: `datetime`


## DeploymentConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeploymentConfigTypeDef
```


Required fields:
- `BlueGreenUpdatePolicy`: `"BlueGreenUpdatePolicyTypeDef"`



Optional fields:
- `AutoRollbackConfiguration`: `"AutoRollbackConfigTypeDef"`


## DescribeActionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeActionResponseTypeDef
```




Optional fields:
- `ActionName`: `str`
- `ActionArn`: `str`
- `Source`: `"ActionSourceTypeDef"`
- `ActionType`: `str`
- `Description`: `str`
- `Status`: `ActionStatus`
- `Properties`: `Dict[str, str]`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`


## DescribeAlgorithmOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeAlgorithmOutputTypeDef
```


Required fields:
- `AlgorithmName`: `str`
- `AlgorithmArn`: `str`
- `CreationTime`: `datetime`
- `TrainingSpecification`: `"TrainingSpecificationTypeDef"`
- `AlgorithmStatus`: `AlgorithmStatus`
- `AlgorithmStatusDetails`: `"AlgorithmStatusDetailsTypeDef"`



Optional fields:
- `AlgorithmDescription`: `str`
- `InferenceSpecification`: `"InferenceSpecificationTypeDef"`
- `ValidationSpecification`: `"AlgorithmValidationSpecificationTypeDef"`
- `ProductId`: `str`
- `CertifyForMarketplace`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAppImageConfigResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeAppImageConfigResponseTypeDef
```




Optional fields:
- `AppImageConfigArn`: `str`
- `AppImageConfigName`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `KernelGatewayImageConfig`: `"KernelGatewayImageConfigTypeDef"`


## DescribeAppResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeAppResponseTypeDef
```




Optional fields:
- `AppArn`: `str`
- `AppType`: `AppType`
- `AppName`: `str`
- `DomainId`: `str`
- `UserProfileName`: `str`
- `Status`: `AppStatus`
- `LastHealthCheckTimestamp`: `datetime`
- `LastUserActivityTimestamp`: `datetime`
- `CreationTime`: `datetime`
- `FailureReason`: `str`
- `ResourceSpec`: `"ResourceSpecTypeDef"`


## DescribeArtifactResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeArtifactResponseTypeDef
```




Optional fields:
- `ArtifactName`: `str`
- `ArtifactArn`: `str`
- `Source`: `"ArtifactSourceTypeDef"`
- `ArtifactType`: `str`
- `Properties`: `Dict[str, str]`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`


## DescribeAutoMLJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeAutoMLJobResponseTypeDef
```


Required fields:
- `AutoMLJobName`: `str`
- `AutoMLJobArn`: `str`
- `InputDataConfig`: `List["AutoMLChannelTypeDef"]`
- `OutputDataConfig`: `"AutoMLOutputDataConfigTypeDef"`
- `RoleArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `AutoMLJobStatus`: `AutoMLJobStatus`
- `AutoMLJobSecondaryStatus`: `AutoMLJobSecondaryStatus`



Optional fields:
- `AutoMLJobObjective`: `"AutoMLJobObjectiveTypeDef"`
- `ProblemType`: `ProblemType`
- `AutoMLJobConfig`: `"AutoMLJobConfigTypeDef"`
- `EndTime`: `datetime`
- `FailureReason`: `str`
- `PartialFailureReasons`: `List["AutoMLPartialFailureReasonTypeDef"]`
- `BestCandidate`: `"AutoMLCandidateTypeDef"`
- `GenerateCandidateDefinitionsOnly`: `bool`
- `AutoMLJobArtifacts`: `"AutoMLJobArtifactsTypeDef"`
- `ResolvedAttributes`: `"ResolvedAttributesTypeDef"`


## DescribeCodeRepositoryOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeCodeRepositoryOutputTypeDef
```


Required fields:
- `CodeRepositoryName`: `str`
- `CodeRepositoryArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `GitConfig`: `"GitConfigTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeCompilationJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeCompilationJobResponseTypeDef
```


Required fields:
- `CompilationJobName`: `str`
- `CompilationJobArn`: `str`
- `CompilationJobStatus`: `CompilationJobStatus`
- `StoppingCondition`: `"StoppingConditionTypeDef"`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`
- `ModelArtifacts`: `"ModelArtifactsTypeDef"`
- `RoleArn`: `str`
- `InputConfig`: `"InputConfigTypeDef"`
- `OutputConfig`: `"OutputConfigTypeDef"`



Optional fields:
- `CompilationStartTime`: `datetime`
- `CompilationEndTime`: `datetime`
- `ModelDigests`: `"ModelDigestsTypeDef"`


## DescribeContextResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeContextResponseTypeDef
```




Optional fields:
- `ContextName`: `str`
- `ContextArn`: `str`
- `Source`: `"ContextSourceTypeDef"`
- `ContextType`: `str`
- `Description`: `str`
- `Properties`: `Dict[str, str]`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`


## DescribeDataQualityJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeDataQualityJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`
- `JobDefinitionName`: `str`
- `CreationTime`: `datetime`
- `DataQualityAppSpecification`: `"DataQualityAppSpecificationTypeDef"`
- `DataQualityJobInput`: `"DataQualityJobInputTypeDef"`
- `DataQualityJobOutputConfig`: `"MonitoringOutputConfigTypeDef"`
- `JobResources`: `"MonitoringResourcesTypeDef"`
- `RoleArn`: `str`



Optional fields:
- `DataQualityBaselineConfig`: `"DataQualityBaselineConfigTypeDef"`
- `NetworkConfig`: `"MonitoringNetworkConfigTypeDef"`
- `StoppingCondition`: `"MonitoringStoppingConditionTypeDef"`


## DescribeDeviceFleetResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeDeviceFleetResponseTypeDef
```


Required fields:
- `DeviceFleetName`: `str`
- `DeviceFleetArn`: `str`
- `OutputConfig`: `"EdgeOutputConfigTypeDef"`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `Description`: `str`
- `RoleArn`: `str`
- `IotRoleAlias`: `str`


## DescribeDeviceResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeDeviceResponseTypeDef
```


Required fields:
- `DeviceName`: `str`
- `DeviceFleetName`: `str`
- `RegistrationTime`: `datetime`



Optional fields:
- `DeviceArn`: `str`
- `Description`: `str`
- `IotThingName`: `str`
- `LatestHeartbeat`: `datetime`
- `Models`: `List["EdgeModelTypeDef"]`
- `MaxModels`: `int`
- `NextToken`: `str`


## DescribeDomainResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeDomainResponseTypeDef
```




Optional fields:
- `DomainArn`: `str`
- `DomainId`: `str`
- `DomainName`: `str`
- `HomeEfsFileSystemId`: `str`
- `SingleSignOnManagedApplicationInstanceId`: `str`
- `Status`: `DomainStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`
- `AuthMode`: `AuthMode`
- `DefaultUserSettings`: `"UserSettingsTypeDef"`
- `AppNetworkAccessType`: `AppNetworkAccessType`
- `HomeEfsFileSystemKmsKeyId`: `str`
- `SubnetIds`: `List[str]`
- `Url`: `str`
- `VpcId`: `str`
- `KmsKeyId`: `str`


## DescribeEdgePackagingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeEdgePackagingJobResponseTypeDef
```


Required fields:
- `EdgePackagingJobArn`: `str`
- `EdgePackagingJobName`: `str`
- `EdgePackagingJobStatus`: `EdgePackagingJobStatus`



Optional fields:
- `CompilationJobName`: `str`
- `ModelName`: `str`
- `ModelVersion`: `str`
- `RoleArn`: `str`
- `OutputConfig`: `"EdgeOutputConfigTypeDef"`
- `ResourceKey`: `str`
- `EdgePackagingJobStatusMessage`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `ModelArtifact`: `str`
- `ModelSignature`: `str`


## DescribeEndpointConfigOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeEndpointConfigOutputTypeDef
```


Required fields:
- `EndpointConfigName`: `str`
- `EndpointConfigArn`: `str`
- `ProductionVariants`: `List["ProductionVariantTypeDef"]`
- `CreationTime`: `datetime`



Optional fields:
- `DataCaptureConfig`: `"DataCaptureConfigTypeDef"`
- `KmsKeyId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeEndpointOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeEndpointOutputTypeDef
```


Required fields:
- `EndpointName`: `str`
- `EndpointArn`: `str`
- `EndpointConfigName`: `str`
- `EndpointStatus`: `EndpointStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `ProductionVariants`: `List["ProductionVariantSummaryTypeDef"]`
- `DataCaptureConfig`: `"DataCaptureConfigSummaryTypeDef"`
- `FailureReason`: `str`
- `LastDeploymentConfig`: `"DeploymentConfigTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeExperimentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeExperimentResponseTypeDef
```




Optional fields:
- `ExperimentName`: `str`
- `ExperimentArn`: `str`
- `DisplayName`: `str`
- `Source`: `"ExperimentSourceTypeDef"`
- `Description`: `str`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`


## DescribeFeatureGroupResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeFeatureGroupResponseTypeDef
```


Required fields:
- `FeatureGroupArn`: `str`
- `FeatureGroupName`: `str`
- `RecordIdentifierFeatureName`: `str`
- `EventTimeFeatureName`: `str`
- `FeatureDefinitions`: `List["FeatureDefinitionTypeDef"]`
- `CreationTime`: `datetime`
- `NextToken`: `str`



Optional fields:
- `OnlineStoreConfig`: `"OnlineStoreConfigTypeDef"`
- `OfflineStoreConfig`: `"OfflineStoreConfigTypeDef"`
- `RoleArn`: `str`
- `FeatureGroupStatus`: `FeatureGroupStatus`
- `OfflineStoreStatus`: `"OfflineStoreStatusTypeDef"`
- `FailureReason`: `str`
- `Description`: `str`


## DescribeFlowDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeFlowDefinitionResponseTypeDef
```


Required fields:
- `FlowDefinitionArn`: `str`
- `FlowDefinitionName`: `str`
- `FlowDefinitionStatus`: `FlowDefinitionStatus`
- `CreationTime`: `datetime`
- `HumanLoopConfig`: `"HumanLoopConfigTypeDef"`
- `OutputConfig`: `"FlowDefinitionOutputConfigTypeDef"`
- `RoleArn`: `str`



Optional fields:
- `HumanLoopRequestSource`: `"HumanLoopRequestSourceTypeDef"`
- `HumanLoopActivationConfig`: `"HumanLoopActivationConfigTypeDef"`
- `FailureReason`: `str`


## DescribeHumanTaskUiResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeHumanTaskUiResponseTypeDef
```


Required fields:
- `HumanTaskUiArn`: `str`
- `HumanTaskUiName`: `str`
- `CreationTime`: `datetime`
- `UiTemplate`: `"UiTemplateInfoTypeDef"`



Optional fields:
- `HumanTaskUiStatus`: `HumanTaskUiStatus`


## DescribeHyperParameterTuningJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeHyperParameterTuningJobResponseTypeDef
```


Required fields:
- `HyperParameterTuningJobName`: `str`
- `HyperParameterTuningJobArn`: `str`
- `HyperParameterTuningJobConfig`: `"HyperParameterTuningJobConfigTypeDef"`
- `HyperParameterTuningJobStatus`: `HyperParameterTuningJobStatus`
- `CreationTime`: `datetime`
- `TrainingJobStatusCounters`: `"TrainingJobStatusCountersTypeDef"`
- `ObjectiveStatusCounters`: `"ObjectiveStatusCountersTypeDef"`



Optional fields:
- `TrainingJobDefinition`: `"HyperParameterTrainingJobDefinitionTypeDef"`
- `TrainingJobDefinitions`: `List["HyperParameterTrainingJobDefinitionTypeDef"]`
- `HyperParameterTuningEndTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `BestTrainingJob`: `"HyperParameterTrainingJobSummaryTypeDef"`
- `OverallBestTrainingJob`: `"HyperParameterTrainingJobSummaryTypeDef"`
- `WarmStartConfig`: `"HyperParameterTuningJobWarmStartConfigTypeDef"`
- `FailureReason`: `str`


## DescribeImageResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeImageResponseTypeDef
```




Optional fields:
- `CreationTime`: `datetime`
- `Description`: `str`
- `DisplayName`: `str`
- `FailureReason`: `str`
- `ImageArn`: `str`
- `ImageName`: `str`
- `ImageStatus`: `ImageStatus`
- `LastModifiedTime`: `datetime`
- `RoleArn`: `str`


## DescribeImageVersionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeImageVersionResponseTypeDef
```




Optional fields:
- `BaseImage`: `str`
- `ContainerImage`: `str`
- `CreationTime`: `datetime`
- `FailureReason`: `str`
- `ImageArn`: `str`
- `ImageVersionArn`: `str`
- `ImageVersionStatus`: `ImageVersionStatus`
- `LastModifiedTime`: `datetime`
- `Version`: `int`


## DescribeLabelingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeLabelingJobResponseTypeDef
```


Required fields:
- `LabelingJobStatus`: `LabelingJobStatus`
- `LabelCounters`: `"LabelCountersTypeDef"`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `JobReferenceCode`: `str`
- `LabelingJobName`: `str`
- `LabelingJobArn`: `str`
- `InputConfig`: `"LabelingJobInputConfigTypeDef"`
- `OutputConfig`: `"LabelingJobOutputConfigTypeDef"`
- `RoleArn`: `str`
- `HumanTaskConfig`: `"HumanTaskConfigTypeDef"`



Optional fields:
- `FailureReason`: `str`
- `LabelAttributeName`: `str`
- `LabelCategoryConfigS3Uri`: `str`
- `StoppingConditions`: `"LabelingJobStoppingConditionsTypeDef"`
- `LabelingJobAlgorithmsConfig`: `"LabelingJobAlgorithmsConfigTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `LabelingJobOutput`: `"LabelingJobOutputTypeDef"`


## DescribeModelBiasJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeModelBiasJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`
- `JobDefinitionName`: `str`
- `CreationTime`: `datetime`
- `ModelBiasAppSpecification`: `"ModelBiasAppSpecificationTypeDef"`
- `ModelBiasJobInput`: `"ModelBiasJobInputTypeDef"`
- `ModelBiasJobOutputConfig`: `"MonitoringOutputConfigTypeDef"`
- `JobResources`: `"MonitoringResourcesTypeDef"`
- `RoleArn`: `str`



Optional fields:
- `ModelBiasBaselineConfig`: `"ModelBiasBaselineConfigTypeDef"`
- `NetworkConfig`: `"MonitoringNetworkConfigTypeDef"`
- `StoppingCondition`: `"MonitoringStoppingConditionTypeDef"`


## DescribeModelExplainabilityJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeModelExplainabilityJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`
- `JobDefinitionName`: `str`
- `CreationTime`: `datetime`
- `ModelExplainabilityAppSpecification`: `"ModelExplainabilityAppSpecificationTypeDef"`
- `ModelExplainabilityJobInput`: `"ModelExplainabilityJobInputTypeDef"`
- `ModelExplainabilityJobOutputConfig`: `"MonitoringOutputConfigTypeDef"`
- `JobResources`: `"MonitoringResourcesTypeDef"`
- `RoleArn`: `str`



Optional fields:
- `ModelExplainabilityBaselineConfig`: `"ModelExplainabilityBaselineConfigTypeDef"`
- `NetworkConfig`: `"MonitoringNetworkConfigTypeDef"`
- `StoppingCondition`: `"MonitoringStoppingConditionTypeDef"`


## DescribeModelOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeModelOutputTypeDef
```


Required fields:
- `ModelName`: `str`
- `ExecutionRoleArn`: `str`
- `CreationTime`: `datetime`
- `ModelArn`: `str`



Optional fields:
- `PrimaryContainer`: `"ContainerDefinitionTypeDef"`
- `Containers`: `List["ContainerDefinitionTypeDef"]`
- `InferenceExecutionConfig`: `"InferenceExecutionConfigTypeDef"`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `EnableNetworkIsolation`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeModelPackageGroupOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeModelPackageGroupOutputTypeDef
```


Required fields:
- `ModelPackageGroupName`: `str`
- `ModelPackageGroupArn`: `str`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `ModelPackageGroupStatus`: `ModelPackageGroupStatus`



Optional fields:
- `ModelPackageGroupDescription`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeModelPackageOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeModelPackageOutputTypeDef
```


Required fields:
- `ModelPackageName`: `str`
- `ModelPackageArn`: `str`
- `CreationTime`: `datetime`
- `ModelPackageStatus`: `ModelPackageStatus`
- `ModelPackageStatusDetails`: `"ModelPackageStatusDetailsTypeDef"`



Optional fields:
- `ModelPackageGroupName`: `str`
- `ModelPackageVersion`: `int`
- `ModelPackageDescription`: `str`
- `InferenceSpecification`: `"InferenceSpecificationTypeDef"`
- `SourceAlgorithmSpecification`: `"SourceAlgorithmSpecificationTypeDef"`
- `ValidationSpecification`: `"ModelPackageValidationSpecificationTypeDef"`
- `CertifyForMarketplace`: `bool`
- `ModelApprovalStatus`: `ModelApprovalStatus`
- `CreatedBy`: `"UserContextTypeDef"`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`
- `ModelMetrics`: `"ModelMetricsTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `ApprovalDescription`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeModelQualityJobDefinitionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeModelQualityJobDefinitionResponseTypeDef
```


Required fields:
- `JobDefinitionArn`: `str`
- `JobDefinitionName`: `str`
- `CreationTime`: `datetime`
- `ModelQualityAppSpecification`: `"ModelQualityAppSpecificationTypeDef"`
- `ModelQualityJobInput`: `"ModelQualityJobInputTypeDef"`
- `ModelQualityJobOutputConfig`: `"MonitoringOutputConfigTypeDef"`
- `JobResources`: `"MonitoringResourcesTypeDef"`
- `RoleArn`: `str`



Optional fields:
- `ModelQualityBaselineConfig`: `"ModelQualityBaselineConfigTypeDef"`
- `NetworkConfig`: `"MonitoringNetworkConfigTypeDef"`
- `StoppingCondition`: `"MonitoringStoppingConditionTypeDef"`


## DescribeMonitoringScheduleResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeMonitoringScheduleResponseTypeDef
```


Required fields:
- `MonitoringScheduleArn`: `str`
- `MonitoringScheduleName`: `str`
- `MonitoringScheduleStatus`: `ScheduleStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `MonitoringScheduleConfig`: `"MonitoringScheduleConfigTypeDef"`



Optional fields:
- `MonitoringType`: `MonitoringType`
- `FailureReason`: `str`
- `EndpointName`: `str`
- `LastMonitoringExecutionSummary`: `"MonitoringExecutionSummaryTypeDef"`


## DescribeNotebookInstanceLifecycleConfigOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeNotebookInstanceLifecycleConfigOutputTypeDef
```




Optional fields:
- `NotebookInstanceLifecycleConfigArn`: `str`
- `NotebookInstanceLifecycleConfigName`: `str`
- `OnCreate`: `List["NotebookInstanceLifecycleHookTypeDef"]`
- `OnStart`: `List["NotebookInstanceLifecycleHookTypeDef"]`
- `LastModifiedTime`: `datetime`
- `CreationTime`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeNotebookInstanceOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeNotebookInstanceOutputTypeDef
```




Optional fields:
- `NotebookInstanceArn`: `str`
- `NotebookInstanceName`: `str`
- `NotebookInstanceStatus`: `NotebookInstanceStatus`
- `FailureReason`: `str`
- `Url`: `str`
- `InstanceType`: `InstanceType`
- `SubnetId`: `str`
- `SecurityGroups`: `List[str]`
- `RoleArn`: `str`
- `KmsKeyId`: `str`
- `NetworkInterfaceId`: `str`
- `LastModifiedTime`: `datetime`
- `CreationTime`: `datetime`
- `NotebookInstanceLifecycleConfigName`: `str`
- `DirectInternetAccess`: `DirectInternetAccess`
- `VolumeSizeInGB`: `int`
- `AcceleratorTypes`: `List[NotebookInstanceAcceleratorType]`
- `DefaultCodeRepository`: `str`
- `AdditionalCodeRepositories`: `List[str]`
- `RootAccess`: `RootAccess`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePipelineDefinitionForExecutionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribePipelineDefinitionForExecutionResponseTypeDef
```




Optional fields:
- `PipelineDefinition`: `str`
- `CreationTime`: `datetime`


## DescribePipelineExecutionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribePipelineExecutionResponseTypeDef
```




Optional fields:
- `PipelineArn`: `str`
- `PipelineExecutionArn`: `str`
- `PipelineExecutionDisplayName`: `str`
- `PipelineExecutionStatus`: `PipelineExecutionStatus`
- `PipelineExecutionDescription`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedBy`: `"UserContextTypeDef"`


## DescribePipelineResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribePipelineResponseTypeDef
```




Optional fields:
- `PipelineArn`: `str`
- `PipelineName`: `str`
- `PipelineDisplayName`: `str`
- `PipelineDefinition`: `str`
- `PipelineDescription`: `str`
- `RoleArn`: `str`
- `PipelineStatus`: `Literal['Active']`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastRunTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedBy`: `"UserContextTypeDef"`


## DescribeProcessingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeProcessingJobResponseTypeDef
```


Required fields:
- `ProcessingJobName`: `str`
- `ProcessingResources`: `"ProcessingResourcesTypeDef"`
- `AppSpecification`: `"AppSpecificationTypeDef"`
- `ProcessingJobArn`: `str`
- `ProcessingJobStatus`: `ProcessingJobStatus`
- `CreationTime`: `datetime`



Optional fields:
- `ProcessingInputs`: `List["ProcessingInputTypeDef"]`
- `ProcessingOutputConfig`: `"ProcessingOutputConfigTypeDef"`
- `StoppingCondition`: `"ProcessingStoppingConditionTypeDef"`
- `Environment`: `Dict[str, str]`
- `NetworkConfig`: `"NetworkConfigTypeDef"`
- `RoleArn`: `str`
- `ExperimentConfig`: `"ExperimentConfigTypeDef"`
- `ExitMessage`: `str`
- `FailureReason`: `str`
- `ProcessingEndTime`: `datetime`
- `ProcessingStartTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `MonitoringScheduleArn`: `str`
- `AutoMLJobArn`: `str`
- `TrainingJobArn`: `str`


## DescribeProjectOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeProjectOutputTypeDef
```


Required fields:
- `ProjectArn`: `str`
- `ProjectName`: `str`
- `ProjectId`: `str`
- `ServiceCatalogProvisioningDetails`: `"ServiceCatalogProvisioningDetailsTypeDef"`
- `ProjectStatus`: `ProjectStatus`
- `CreationTime`: `datetime`



Optional fields:
- `ProjectDescription`: `str`
- `ServiceCatalogProvisionedProductDetails`: `"ServiceCatalogProvisionedProductDetailsTypeDef"`
- `CreatedBy`: `"UserContextTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSubscribedWorkteamResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeSubscribedWorkteamResponseTypeDef
```


Required fields:
- `SubscribedWorkteam`: `"SubscribedWorkteamTypeDef"`




## DescribeTrainingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeTrainingJobResponseTypeDef
```


Required fields:
- `TrainingJobName`: `str`
- `TrainingJobArn`: `str`
- `ModelArtifacts`: `"ModelArtifactsTypeDef"`
- `TrainingJobStatus`: `TrainingJobStatus`
- `SecondaryStatus`: `SecondaryStatus`
- `AlgorithmSpecification`: `"AlgorithmSpecificationTypeDef"`
- `ResourceConfig`: `"ResourceConfigTypeDef"`
- `StoppingCondition`: `"StoppingConditionTypeDef"`
- `CreationTime`: `datetime`



Optional fields:
- `TuningJobArn`: `str`
- `LabelingJobArn`: `str`
- `AutoMLJobArn`: `str`
- `FailureReason`: `str`
- `HyperParameters`: `Dict[str, str]`
- `RoleArn`: `str`
- `InputDataConfig`: `List["ChannelTypeDef"]`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `TrainingStartTime`: `datetime`
- `TrainingEndTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `SecondaryStatusTransitions`: `List["SecondaryStatusTransitionTypeDef"]`
- `FinalMetricDataList`: `List["MetricDataTypeDef"]`
- `EnableNetworkIsolation`: `bool`
- `EnableInterContainerTrafficEncryption`: `bool`
- `EnableManagedSpotTraining`: `bool`
- `CheckpointConfig`: `"CheckpointConfigTypeDef"`
- `TrainingTimeInSeconds`: `int`
- `BillableTimeInSeconds`: `int`
- `DebugHookConfig`: `"DebugHookConfigTypeDef"`
- `ExperimentConfig`: `"ExperimentConfigTypeDef"`
- `DebugRuleConfigurations`: `List["DebugRuleConfigurationTypeDef"]`
- `TensorBoardOutputConfig`: `"TensorBoardOutputConfigTypeDef"`
- `DebugRuleEvaluationStatuses`: `List["DebugRuleEvaluationStatusTypeDef"]`
- `ProfilerConfig`: `"ProfilerConfigTypeDef"`
- `ProfilerRuleConfigurations`: `List["ProfilerRuleConfigurationTypeDef"]`
- `ProfilerRuleEvaluationStatuses`: `List["ProfilerRuleEvaluationStatusTypeDef"]`
- `ProfilingStatus`: `ProfilingStatus`
- `Environment`: `Dict[str, str]`


## DescribeTransformJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeTransformJobResponseTypeDef
```


Required fields:
- `TransformJobName`: `str`
- `TransformJobArn`: `str`
- `TransformJobStatus`: `TransformJobStatus`
- `ModelName`: `str`
- `TransformInput`: `"TransformInputTypeDef"`
- `TransformResources`: `"TransformResourcesTypeDef"`
- `CreationTime`: `datetime`



Optional fields:
- `FailureReason`: `str`
- `MaxConcurrentTransforms`: `int`
- `ModelClientConfig`: `"ModelClientConfigTypeDef"`
- `MaxPayloadInMB`: `int`
- `BatchStrategy`: `BatchStrategy`
- `Environment`: `Dict[str, str]`
- `TransformOutput`: `"TransformOutputTypeDef"`
- `TransformStartTime`: `datetime`
- `TransformEndTime`: `datetime`
- `LabelingJobArn`: `str`
- `AutoMLJobArn`: `str`
- `DataProcessing`: `"DataProcessingTypeDef"`
- `ExperimentConfig`: `"ExperimentConfigTypeDef"`


## DescribeTrialComponentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeTrialComponentResponseTypeDef
```




Optional fields:
- `TrialComponentName`: `str`
- `TrialComponentArn`: `str`
- `DisplayName`: `str`
- `Source`: `"TrialComponentSourceTypeDef"`
- `Status`: `"TrialComponentStatusTypeDef"`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `Parameters`: `Dict[str, "TrialComponentParameterValueTypeDef"]`
- `InputArtifacts`: `Dict[str, "TrialComponentArtifactTypeDef"]`
- `OutputArtifacts`: `Dict[str, "TrialComponentArtifactTypeDef"]`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`
- `Metrics`: `List["TrialComponentMetricSummaryTypeDef"]`


## DescribeTrialResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeTrialResponseTypeDef
```




Optional fields:
- `TrialName`: `str`
- `TrialArn`: `str`
- `DisplayName`: `str`
- `ExperimentName`: `str`
- `Source`: `"TrialSourceTypeDef"`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`


## DescribeUserProfileResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeUserProfileResponseTypeDef
```




Optional fields:
- `DomainId`: `str`
- `UserProfileArn`: `str`
- `UserProfileName`: `str`
- `HomeEfsFileSystemUid`: `str`
- `Status`: `UserProfileStatus`
- `LastModifiedTime`: `datetime`
- `CreationTime`: `datetime`
- `FailureReason`: `str`
- `SingleSignOnUserIdentifier`: `str`
- `SingleSignOnUserValue`: `str`
- `UserSettings`: `"UserSettingsTypeDef"`


## DescribeWorkforceResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeWorkforceResponseTypeDef
```


Required fields:
- `Workforce`: `"WorkforceTypeDef"`




## DescribeWorkteamResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DescribeWorkteamResponseTypeDef
```


Required fields:
- `Workteam`: `"WorkteamTypeDef"`




## DesiredWeightAndCapacityTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DesiredWeightAndCapacityTypeDef
```


Required fields:
- `VariantName`: `str`



Optional fields:
- `DesiredWeight`: `float`
- `DesiredInstanceCount`: `int`


## DeviceFleetSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeviceFleetSummaryTypeDef
```


Required fields:
- `DeviceFleetArn`: `str`
- `DeviceFleetName`: `str`



Optional fields:
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## DeviceStatsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeviceStatsTypeDef
```


Required fields:
- `ConnectedDeviceCount`: `int`
- `RegisteredDeviceCount`: `int`




## DeviceSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeviceSummaryTypeDef
```


Required fields:
- `DeviceName`: `str`
- `DeviceArn`: `str`



Optional fields:
- `Description`: `str`
- `DeviceFleetName`: `str`
- `IotThingName`: `str`
- `RegistrationTime`: `datetime`
- `LatestHeartbeat`: `datetime`
- `Models`: `List["EdgeModelSummaryTypeDef"]`


## DeviceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DeviceTypeDef
```


Required fields:
- `DeviceName`: `str`



Optional fields:
- `Description`: `str`
- `IotThingName`: `str`


## DisassociateTrialComponentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DisassociateTrialComponentResponseTypeDef
```




Optional fields:
- `TrialComponentArn`: `str`
- `TrialArn`: `str`


## DomainDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import DomainDetailsTypeDef
```




Optional fields:
- `DomainArn`: `str`
- `DomainId`: `str`
- `DomainName`: `str`
- `Status`: `DomainStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `Url`: `str`


## EdgeModelStatTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EdgeModelStatTypeDef
```


Required fields:
- `ModelName`: `str`
- `ModelVersion`: `str`
- `OfflineDeviceCount`: `int`
- `ConnectedDeviceCount`: `int`
- `ActiveDeviceCount`: `int`
- `SamplingDeviceCount`: `int`




## EdgeModelSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EdgeModelSummaryTypeDef
```


Required fields:
- `ModelName`: `str`
- `ModelVersion`: `str`




## EdgeModelTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EdgeModelTypeDef
```


Required fields:
- `ModelName`: `str`
- `ModelVersion`: `str`



Optional fields:
- `LatestSampleTime`: `datetime`
- `LatestInference`: `datetime`


## EdgeOutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EdgeOutputConfigTypeDef
```


Required fields:
- `S3OutputLocation`: `str`



Optional fields:
- `KmsKeyId`: `str`


## EdgePackagingJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EdgePackagingJobSummaryTypeDef
```


Required fields:
- `EdgePackagingJobArn`: `str`
- `EdgePackagingJobName`: `str`
- `EdgePackagingJobStatus`: `EdgePackagingJobStatus`



Optional fields:
- `CompilationJobName`: `str`
- `ModelName`: `str`
- `ModelVersion`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## EndpointConfigSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EndpointConfigSummaryTypeDef
```


Required fields:
- `EndpointConfigName`: `str`
- `EndpointConfigArn`: `str`
- `CreationTime`: `datetime`




## EndpointInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EndpointInputTypeDef
```


Required fields:
- `EndpointName`: `str`
- `LocalPath`: `str`



Optional fields:
- `S3InputMode`: `ProcessingS3InputMode`
- `S3DataDistributionType`: `ProcessingS3DataDistributionType`
- `FeaturesAttribute`: `str`
- `InferenceAttribute`: `str`
- `ProbabilityAttribute`: `str`
- `ProbabilityThresholdAttribute`: `float`
- `StartTimeOffset`: `str`
- `EndTimeOffset`: `str`


## EndpointSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EndpointSummaryTypeDef
```


Required fields:
- `EndpointName`: `str`
- `EndpointArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `EndpointStatus`: `EndpointStatus`




## EndpointTypeDef

```python
from mypy_boto3_sagemaker.type_defs import EndpointTypeDef
```


Required fields:
- `EndpointName`: `str`
- `EndpointArn`: `str`
- `EndpointConfigName`: `str`
- `EndpointStatus`: `EndpointStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`



Optional fields:
- `ProductionVariants`: `List["ProductionVariantSummaryTypeDef"]`
- `DataCaptureConfig`: `"DataCaptureConfigSummaryTypeDef"`
- `FailureReason`: `str`
- `MonitoringSchedules`: `List["MonitoringScheduleTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## ExperimentConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ExperimentConfigTypeDef
```




Optional fields:
- `ExperimentName`: `str`
- `TrialName`: `str`
- `TrialComponentDisplayName`: `str`


## ExperimentSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ExperimentSourceTypeDef
```


Required fields:
- `SourceArn`: `str`



Optional fields:
- `SourceType`: `str`


## ExperimentSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ExperimentSummaryTypeDef
```




Optional fields:
- `ExperimentArn`: `str`
- `ExperimentName`: `str`
- `DisplayName`: `str`
- `ExperimentSource`: `"ExperimentSourceTypeDef"`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## ExperimentTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ExperimentTypeDef
```




Optional fields:
- `ExperimentName`: `str`
- `ExperimentArn`: `str`
- `DisplayName`: `str`
- `Source`: `"ExperimentSourceTypeDef"`
- `Description`: `str`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## ExplainabilityTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ExplainabilityTypeDef
```




Optional fields:
- `Report`: `"MetricsSourceTypeDef"`


## FeatureDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FeatureDefinitionTypeDef
```




Optional fields:
- `FeatureName`: `str`
- `FeatureType`: `FeatureType`


## FeatureGroupSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FeatureGroupSummaryTypeDef
```


Required fields:
- `FeatureGroupName`: `str`
- `FeatureGroupArn`: `str`
- `CreationTime`: `datetime`



Optional fields:
- `FeatureGroupStatus`: `FeatureGroupStatus`
- `OfflineStoreStatus`: `"OfflineStoreStatusTypeDef"`


## FeatureGroupTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FeatureGroupTypeDef
```




Optional fields:
- `FeatureGroupArn`: `str`
- `FeatureGroupName`: `str`
- `RecordIdentifierFeatureName`: `str`
- `EventTimeFeatureName`: `str`
- `FeatureDefinitions`: `List["FeatureDefinitionTypeDef"]`
- `CreationTime`: `datetime`
- `OnlineStoreConfig`: `"OnlineStoreConfigTypeDef"`
- `OfflineStoreConfig`: `"OfflineStoreConfigTypeDef"`
- `RoleArn`: `str`
- `FeatureGroupStatus`: `FeatureGroupStatus`
- `OfflineStoreStatus`: `"OfflineStoreStatusTypeDef"`
- `FailureReason`: `str`
- `Description`: `str`
- `Tags`: `List["TagTypeDef"]`


## FileSystemConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FileSystemConfigTypeDef
```




Optional fields:
- `MountPath`: `str`
- `DefaultUid`: `int`
- `DefaultGid`: `int`


## FileSystemDataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FileSystemDataSourceTypeDef
```


Required fields:
- `FileSystemId`: `str`
- `FileSystemAccessMode`: `FileSystemAccessMode`
- `FileSystemType`: `FileSystemType`
- `DirectoryPath`: `str`




## FilterTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FilterTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Operator`: `Operator`
- `Value`: `str`


## FinalAutoMLJobObjectiveMetricTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FinalAutoMLJobObjectiveMetricTypeDef
```


Required fields:
- `MetricName`: `AutoMLMetricEnum`
- `Value`: `float`



Optional fields:
- `Type`: `AutoMLJobObjectiveType`


## FinalHyperParameterTuningJobObjectiveMetricTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FinalHyperParameterTuningJobObjectiveMetricTypeDef
```


Required fields:
- `MetricName`: `str`
- `Value`: `float`



Optional fields:
- `Type`: `HyperParameterTuningJobObjectiveType`


## FlowDefinitionOutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FlowDefinitionOutputConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `KmsKeyId`: `str`


## FlowDefinitionSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import FlowDefinitionSummaryTypeDef
```


Required fields:
- `FlowDefinitionName`: `str`
- `FlowDefinitionArn`: `str`
- `FlowDefinitionStatus`: `FlowDefinitionStatus`
- `CreationTime`: `datetime`



Optional fields:
- `FailureReason`: `str`


## GetDeviceFleetReportResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import GetDeviceFleetReportResponseTypeDef
```


Required fields:
- `DeviceFleetArn`: `str`
- `DeviceFleetName`: `str`



Optional fields:
- `OutputConfig`: `"EdgeOutputConfigTypeDef"`
- `Description`: `str`
- `ReportGenerated`: `datetime`
- `DeviceStats`: `"DeviceStatsTypeDef"`
- `AgentVersions`: `List["AgentVersionTypeDef"]`
- `ModelStats`: `List["EdgeModelStatTypeDef"]`


## GetModelPackageGroupPolicyOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import GetModelPackageGroupPolicyOutputTypeDef
```


Required fields:
- `ResourcePolicy`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetSagemakerServicecatalogPortfolioStatusOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import GetSagemakerServicecatalogPortfolioStatusOutputTypeDef
```




Optional fields:
- `Status`: `SagemakerServicecatalogStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetSearchSuggestionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import GetSearchSuggestionsResponseTypeDef
```




Optional fields:
- `PropertyNameSuggestions`: `List["PropertyNameSuggestionTypeDef"]`


## GitConfigForUpdateTypeDef

```python
from mypy_boto3_sagemaker.type_defs import GitConfigForUpdateTypeDef
```




Optional fields:
- `SecretArn`: `str`


## GitConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import GitConfigTypeDef
```


Required fields:
- `RepositoryUrl`: `str`



Optional fields:
- `Branch`: `str`
- `SecretArn`: `str`


## HumanLoopActivationConditionsConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HumanLoopActivationConditionsConfigTypeDef
```


Required fields:
- `HumanLoopActivationConditions`: `str`




## HumanLoopActivationConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HumanLoopActivationConfigTypeDef
```


Required fields:
- `HumanLoopActivationConditionsConfig`: `"HumanLoopActivationConditionsConfigTypeDef"`




## HumanLoopConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HumanLoopConfigTypeDef
```


Required fields:
- `WorkteamArn`: `str`
- `HumanTaskUiArn`: `str`
- `TaskTitle`: `str`
- `TaskDescription`: `str`
- `TaskCount`: `int`



Optional fields:
- `TaskAvailabilityLifetimeInSeconds`: `int`
- `TaskTimeLimitInSeconds`: `int`
- `TaskKeywords`: `List[str]`
- `PublicWorkforceTaskPrice`: `"PublicWorkforceTaskPriceTypeDef"`


## HumanLoopRequestSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HumanLoopRequestSourceTypeDef
```


Required fields:
- `AwsManagedHumanLoopRequestSource`: `AwsManagedHumanLoopRequestSource`




## HumanTaskConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HumanTaskConfigTypeDef
```


Required fields:
- `WorkteamArn`: `str`
- `UiConfig`: `"UiConfigTypeDef"`
- `PreHumanTaskLambdaArn`: `str`
- `TaskTitle`: `str`
- `TaskDescription`: `str`
- `NumberOfHumanWorkersPerDataObject`: `int`
- `TaskTimeLimitInSeconds`: `int`
- `AnnotationConsolidationConfig`: `"AnnotationConsolidationConfigTypeDef"`



Optional fields:
- `TaskKeywords`: `List[str]`
- `TaskAvailabilityLifetimeInSeconds`: `int`
- `MaxConcurrentTaskCount`: `int`
- `PublicWorkforceTaskPrice`: `"PublicWorkforceTaskPriceTypeDef"`


## HumanTaskUiSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HumanTaskUiSummaryTypeDef
```


Required fields:
- `HumanTaskUiName`: `str`
- `HumanTaskUiArn`: `str`
- `CreationTime`: `datetime`




## HyperParameterAlgorithmSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterAlgorithmSpecificationTypeDef
```


Required fields:
- `TrainingInputMode`: `TrainingInputMode`



Optional fields:
- `TrainingImage`: `str`
- `AlgorithmName`: `str`
- `MetricDefinitions`: `List["MetricDefinitionTypeDef"]`


## HyperParameterSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterSpecificationTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `ParameterType`



Optional fields:
- `Description`: `str`
- `Range`: `"ParameterRangeTypeDef"`
- `IsTunable`: `bool`
- `IsRequired`: `bool`
- `DefaultValue`: `str`


## HyperParameterTrainingJobDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterTrainingJobDefinitionTypeDef
```


Required fields:
- `AlgorithmSpecification`: `"HyperParameterAlgorithmSpecificationTypeDef"`
- `RoleArn`: `str`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `ResourceConfig`: `"ResourceConfigTypeDef"`
- `StoppingCondition`: `"StoppingConditionTypeDef"`



Optional fields:
- `DefinitionName`: `str`
- `TuningObjective`: `"HyperParameterTuningJobObjectiveTypeDef"`
- `HyperParameterRanges`: `"ParameterRangesTypeDef"`
- `StaticHyperParameters`: `Dict[str, str]`
- `InputDataConfig`: `List["ChannelTypeDef"]`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `EnableNetworkIsolation`: `bool`
- `EnableInterContainerTrafficEncryption`: `bool`
- `EnableManagedSpotTraining`: `bool`
- `CheckpointConfig`: `"CheckpointConfigTypeDef"`


## HyperParameterTrainingJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterTrainingJobSummaryTypeDef
```


Required fields:
- `TrainingJobName`: `str`
- `TrainingJobArn`: `str`
- `CreationTime`: `datetime`
- `TrainingJobStatus`: `TrainingJobStatus`
- `TunedHyperParameters`: `Dict[str, str]`



Optional fields:
- `TrainingJobDefinitionName`: `str`
- `TuningJobName`: `str`
- `TrainingStartTime`: `datetime`
- `TrainingEndTime`: `datetime`
- `FailureReason`: `str`
- `FinalHyperParameterTuningJobObjectiveMetric`: `"FinalHyperParameterTuningJobObjectiveMetricTypeDef"`
- `ObjectiveStatus`: `ObjectiveStatus`


## HyperParameterTuningJobConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterTuningJobConfigTypeDef
```


Required fields:
- `Strategy`: `HyperParameterTuningJobStrategyType`
- `ResourceLimits`: `"ResourceLimitsTypeDef"`



Optional fields:
- `HyperParameterTuningJobObjective`: `"HyperParameterTuningJobObjectiveTypeDef"`
- `ParameterRanges`: `"ParameterRangesTypeDef"`
- `TrainingJobEarlyStoppingType`: `TrainingJobEarlyStoppingType`
- `TuningJobCompletionCriteria`: `"TuningJobCompletionCriteriaTypeDef"`


## HyperParameterTuningJobObjectiveTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterTuningJobObjectiveTypeDef
```


Required fields:
- `Type`: `HyperParameterTuningJobObjectiveType`
- `MetricName`: `str`




## HyperParameterTuningJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterTuningJobSummaryTypeDef
```


Required fields:
- `HyperParameterTuningJobName`: `str`
- `HyperParameterTuningJobArn`: `str`
- `HyperParameterTuningJobStatus`: `HyperParameterTuningJobStatus`
- `Strategy`: `HyperParameterTuningJobStrategyType`
- `CreationTime`: `datetime`
- `TrainingJobStatusCounters`: `"TrainingJobStatusCountersTypeDef"`
- `ObjectiveStatusCounters`: `"ObjectiveStatusCountersTypeDef"`



Optional fields:
- `HyperParameterTuningEndTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `ResourceLimits`: `"ResourceLimitsTypeDef"`


## HyperParameterTuningJobWarmStartConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import HyperParameterTuningJobWarmStartConfigTypeDef
```


Required fields:
- `ParentHyperParameterTuningJobs`: `List["ParentHyperParameterTuningJobTypeDef"]`
- `WarmStartType`: `HyperParameterTuningJobWarmStartType`




## ImageConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ImageConfigTypeDef
```


Required fields:
- `RepositoryAccessMode`: `RepositoryAccessMode`



Optional fields:
- `RepositoryAuthConfig`: `"RepositoryAuthConfigTypeDef"`


## ImageTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ImageTypeDef
```


Required fields:
- `CreationTime`: `datetime`
- `ImageArn`: `str`
- `ImageName`: `str`
- `ImageStatus`: `ImageStatus`
- `LastModifiedTime`: `datetime`



Optional fields:
- `Description`: `str`
- `DisplayName`: `str`
- `FailureReason`: `str`


## ImageVersionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ImageVersionTypeDef
```


Required fields:
- `CreationTime`: `datetime`
- `ImageArn`: `str`
- `ImageVersionArn`: `str`
- `ImageVersionStatus`: `ImageVersionStatus`
- `LastModifiedTime`: `datetime`
- `Version`: `int`



Optional fields:
- `FailureReason`: `str`


## InferenceExecutionConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import InferenceExecutionConfigTypeDef
```


Required fields:
- `Mode`: `InferenceExecutionMode`




## InferenceSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import InferenceSpecificationTypeDef
```


Required fields:
- `Containers`: `List["ModelPackageContainerDefinitionTypeDef"]`
- `SupportedContentTypes`: `List[str]`
- `SupportedResponseMIMETypes`: `List[str]`



Optional fields:
- `SupportedTransformInstanceTypes`: `List[TransformInstanceType]`
- `SupportedRealtimeInferenceInstanceTypes`: `List[ProductionVariantInstanceType]`


## InputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import InputConfigTypeDef
```


Required fields:
- `S3Uri`: `str`
- `DataInputConfig`: `str`
- `Framework`: `Framework`



Optional fields:
- `FrameworkVersion`: `str`


## IntegerParameterRangeSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import IntegerParameterRangeSpecificationTypeDef
```


Required fields:
- `MinValue`: `str`
- `MaxValue`: `str`




## IntegerParameterRangeTypeDef

```python
from mypy_boto3_sagemaker.type_defs import IntegerParameterRangeTypeDef
```


Required fields:
- `Name`: `str`
- `MinValue`: `str`
- `MaxValue`: `str`



Optional fields:
- `ScalingType`: `HyperParameterScalingType`


## JupyterServerAppSettingsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import JupyterServerAppSettingsTypeDef
```




Optional fields:
- `DefaultResourceSpec`: `"ResourceSpecTypeDef"`


## KernelGatewayAppSettingsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import KernelGatewayAppSettingsTypeDef
```




Optional fields:
- `DefaultResourceSpec`: `"ResourceSpecTypeDef"`
- `CustomImages`: `List["CustomImageTypeDef"]`


## KernelGatewayImageConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import KernelGatewayImageConfigTypeDef
```


Required fields:
- `KernelSpecs`: `List["KernelSpecTypeDef"]`



Optional fields:
- `FileSystemConfig`: `"FileSystemConfigTypeDef"`


## KernelSpecTypeDef

```python
from mypy_boto3_sagemaker.type_defs import KernelSpecTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `DisplayName`: `str`


## LabelCountersForWorkteamTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelCountersForWorkteamTypeDef
```




Optional fields:
- `HumanLabeled`: `int`
- `PendingHuman`: `int`
- `Total`: `int`


## LabelCountersTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelCountersTypeDef
```




Optional fields:
- `TotalLabeled`: `int`
- `HumanLabeled`: `int`
- `MachineLabeled`: `int`
- `FailedNonRetryableError`: `int`
- `Unlabeled`: `int`


## LabelingJobAlgorithmsConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobAlgorithmsConfigTypeDef
```


Required fields:
- `LabelingJobAlgorithmSpecificationArn`: `str`



Optional fields:
- `InitialActiveLearningModelArn`: `str`
- `LabelingJobResourceConfig`: `"LabelingJobResourceConfigTypeDef"`


## LabelingJobDataAttributesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobDataAttributesTypeDef
```




Optional fields:
- `ContentClassifiers`: `List[ContentClassifier]`


## LabelingJobDataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobDataSourceTypeDef
```




Optional fields:
- `S3DataSource`: `"LabelingJobS3DataSourceTypeDef"`
- `SnsDataSource`: `"LabelingJobSnsDataSourceTypeDef"`


## LabelingJobForWorkteamSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobForWorkteamSummaryTypeDef
```


Required fields:
- `JobReferenceCode`: `str`
- `WorkRequesterAccountId`: `str`
- `CreationTime`: `datetime`



Optional fields:
- `LabelingJobName`: `str`
- `LabelCounters`: `"LabelCountersForWorkteamTypeDef"`
- `NumberOfHumanWorkersPerDataObject`: `int`


## LabelingJobInputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobInputConfigTypeDef
```


Required fields:
- `DataSource`: `"LabelingJobDataSourceTypeDef"`



Optional fields:
- `DataAttributes`: `"LabelingJobDataAttributesTypeDef"`


## LabelingJobOutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobOutputConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `KmsKeyId`: `str`
- `SnsTopicArn`: `str`


## LabelingJobOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobOutputTypeDef
```


Required fields:
- `OutputDatasetS3Uri`: `str`



Optional fields:
- `FinalActiveLearningModelArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## LabelingJobResourceConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobResourceConfigTypeDef
```




Optional fields:
- `VolumeKmsKeyId`: `str`


## LabelingJobS3DataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobS3DataSourceTypeDef
```


Required fields:
- `ManifestS3Uri`: `str`




## LabelingJobSnsDataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobSnsDataSourceTypeDef
```


Required fields:
- `SnsTopicArn`: `str`




## LabelingJobStoppingConditionsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobStoppingConditionsTypeDef
```




Optional fields:
- `MaxHumanLabeledObjectCount`: `int`
- `MaxPercentageOfInputDatasetLabeled`: `int`


## LabelingJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import LabelingJobSummaryTypeDef
```


Required fields:
- `LabelingJobName`: `str`
- `LabelingJobArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LabelingJobStatus`: `LabelingJobStatus`
- `LabelCounters`: `"LabelCountersTypeDef"`
- `WorkteamArn`: `str`
- `PreHumanTaskLambdaArn`: `str`



Optional fields:
- `AnnotationConsolidationLambdaArn`: `str`
- `FailureReason`: `str`
- `LabelingJobOutput`: `"LabelingJobOutputTypeDef"`
- `InputConfig`: `"LabelingJobInputConfigTypeDef"`


## ListActionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListActionsResponseTypeDef
```




Optional fields:
- `ActionSummaries`: `List["ActionSummaryTypeDef"]`
- `NextToken`: `str`


## ListAlgorithmsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListAlgorithmsOutputTypeDef
```


Required fields:
- `AlgorithmSummaryList`: `List["AlgorithmSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListAppImageConfigsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListAppImageConfigsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `AppImageConfigs`: `List["AppImageConfigDetailsTypeDef"]`


## ListAppsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListAppsResponseTypeDef
```




Optional fields:
- `Apps`: `List["AppDetailsTypeDef"]`
- `NextToken`: `str`


## ListArtifactsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListArtifactsResponseTypeDef
```




Optional fields:
- `ArtifactSummaries`: `List["ArtifactSummaryTypeDef"]`
- `NextToken`: `str`


## ListAssociationsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListAssociationsResponseTypeDef
```




Optional fields:
- `AssociationSummaries`: `List["AssociationSummaryTypeDef"]`
- `NextToken`: `str`


## ListAutoMLJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListAutoMLJobsResponseTypeDef
```


Required fields:
- `AutoMLJobSummaries`: `List["AutoMLJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListCandidatesForAutoMLJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListCandidatesForAutoMLJobResponseTypeDef
```


Required fields:
- `Candidates`: `List["AutoMLCandidateTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListCodeRepositoriesOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListCodeRepositoriesOutputTypeDef
```


Required fields:
- `CodeRepositorySummaryList`: `List["CodeRepositorySummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListCompilationJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListCompilationJobsResponseTypeDef
```


Required fields:
- `CompilationJobSummaries`: `List["CompilationJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListContextsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListContextsResponseTypeDef
```




Optional fields:
- `ContextSummaries`: `List["ContextSummaryTypeDef"]`
- `NextToken`: `str`


## ListDataQualityJobDefinitionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListDataQualityJobDefinitionsResponseTypeDef
```


Required fields:
- `JobDefinitionSummaries`: `List["MonitoringJobDefinitionSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListDeviceFleetsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListDeviceFleetsResponseTypeDef
```


Required fields:
- `DeviceFleetSummaries`: `List["DeviceFleetSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListDevicesResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListDevicesResponseTypeDef
```


Required fields:
- `DeviceSummaries`: `List["DeviceSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListDomainsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListDomainsResponseTypeDef
```




Optional fields:
- `Domains`: `List["DomainDetailsTypeDef"]`
- `NextToken`: `str`


## ListEdgePackagingJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListEdgePackagingJobsResponseTypeDef
```


Required fields:
- `EdgePackagingJobSummaries`: `List["EdgePackagingJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListEndpointConfigsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListEndpointConfigsOutputTypeDef
```


Required fields:
- `EndpointConfigs`: `List["EndpointConfigSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListEndpointsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListEndpointsOutputTypeDef
```


Required fields:
- `Endpoints`: `List["EndpointSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListExperimentsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListExperimentsResponseTypeDef
```




Optional fields:
- `ExperimentSummaries`: `List["ExperimentSummaryTypeDef"]`
- `NextToken`: `str`


## ListFeatureGroupsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListFeatureGroupsResponseTypeDef
```


Required fields:
- `FeatureGroupSummaries`: `List["FeatureGroupSummaryTypeDef"]`
- `NextToken`: `str`




## ListFlowDefinitionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListFlowDefinitionsResponseTypeDef
```


Required fields:
- `FlowDefinitionSummaries`: `List["FlowDefinitionSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListHumanTaskUisResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListHumanTaskUisResponseTypeDef
```


Required fields:
- `HumanTaskUiSummaries`: `List["HumanTaskUiSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListHyperParameterTuningJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListHyperParameterTuningJobsResponseTypeDef
```


Required fields:
- `HyperParameterTuningJobSummaries`: `List["HyperParameterTuningJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListImageVersionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListImageVersionsResponseTypeDef
```




Optional fields:
- `ImageVersions`: `List["ImageVersionTypeDef"]`
- `NextToken`: `str`


## ListImagesResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListImagesResponseTypeDef
```




Optional fields:
- `Images`: `List["ImageTypeDef"]`
- `NextToken`: `str`


## ListLabelingJobsForWorkteamResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListLabelingJobsForWorkteamResponseTypeDef
```


Required fields:
- `LabelingJobSummaryList`: `List["LabelingJobForWorkteamSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListLabelingJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListLabelingJobsResponseTypeDef
```




Optional fields:
- `LabelingJobSummaryList`: `List["LabelingJobSummaryTypeDef"]`
- `NextToken`: `str`


## ListModelBiasJobDefinitionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListModelBiasJobDefinitionsResponseTypeDef
```


Required fields:
- `JobDefinitionSummaries`: `List["MonitoringJobDefinitionSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListModelExplainabilityJobDefinitionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListModelExplainabilityJobDefinitionsResponseTypeDef
```


Required fields:
- `JobDefinitionSummaries`: `List["MonitoringJobDefinitionSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListModelPackageGroupsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListModelPackageGroupsOutputTypeDef
```


Required fields:
- `ModelPackageGroupSummaryList`: `List["ModelPackageGroupSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListModelPackagesOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListModelPackagesOutputTypeDef
```


Required fields:
- `ModelPackageSummaryList`: `List["ModelPackageSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListModelQualityJobDefinitionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListModelQualityJobDefinitionsResponseTypeDef
```


Required fields:
- `JobDefinitionSummaries`: `List["MonitoringJobDefinitionSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListModelsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListModelsOutputTypeDef
```


Required fields:
- `Models`: `List["ModelSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMonitoringExecutionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListMonitoringExecutionsResponseTypeDef
```


Required fields:
- `MonitoringExecutionSummaries`: `List["MonitoringExecutionSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListMonitoringSchedulesResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListMonitoringSchedulesResponseTypeDef
```


Required fields:
- `MonitoringScheduleSummaries`: `List["MonitoringScheduleSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListNotebookInstanceLifecycleConfigsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListNotebookInstanceLifecycleConfigsOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NotebookInstanceLifecycleConfigs`: `List["NotebookInstanceLifecycleConfigSummaryTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListNotebookInstancesOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListNotebookInstancesOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NotebookInstances`: `List["NotebookInstanceSummaryTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPipelineExecutionStepsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListPipelineExecutionStepsResponseTypeDef
```




Optional fields:
- `PipelineExecutionSteps`: `List["PipelineExecutionStepTypeDef"]`
- `NextToken`: `str`


## ListPipelineExecutionsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListPipelineExecutionsResponseTypeDef
```




Optional fields:
- `PipelineExecutionSummaries`: `List["PipelineExecutionSummaryTypeDef"]`
- `NextToken`: `str`


## ListPipelineParametersForExecutionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListPipelineParametersForExecutionResponseTypeDef
```




Optional fields:
- `PipelineParameters`: `List["ParameterTypeDef"]`
- `NextToken`: `str`


## ListPipelinesResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListPipelinesResponseTypeDef
```




Optional fields:
- `PipelineSummaries`: `List["PipelineSummaryTypeDef"]`
- `NextToken`: `str`


## ListProcessingJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListProcessingJobsResponseTypeDef
```


Required fields:
- `ProcessingJobSummaries`: `List["ProcessingJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListProjectsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListProjectsOutputTypeDef
```


Required fields:
- `ProjectSummaryList`: `List["ProjectSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSubscribedWorkteamsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListSubscribedWorkteamsResponseTypeDef
```


Required fields:
- `SubscribedWorkteams`: `List["SubscribedWorkteamTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTagsOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListTagsOutputTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTrainingJobsForHyperParameterTuningJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListTrainingJobsForHyperParameterTuningJobResponseTypeDef
```


Required fields:
- `TrainingJobSummaries`: `List["HyperParameterTrainingJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTrainingJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListTrainingJobsResponseTypeDef
```


Required fields:
- `TrainingJobSummaries`: `List["TrainingJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTransformJobsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListTransformJobsResponseTypeDef
```


Required fields:
- `TransformJobSummaries`: `List["TransformJobSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTrialComponentsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListTrialComponentsResponseTypeDef
```




Optional fields:
- `TrialComponentSummaries`: `List["TrialComponentSummaryTypeDef"]`
- `NextToken`: `str`


## ListTrialsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListTrialsResponseTypeDef
```




Optional fields:
- `TrialSummaries`: `List["TrialSummaryTypeDef"]`
- `NextToken`: `str`


## ListUserProfilesResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListUserProfilesResponseTypeDef
```




Optional fields:
- `UserProfiles`: `List["UserProfileDetailsTypeDef"]`
- `NextToken`: `str`


## ListWorkforcesResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListWorkforcesResponseTypeDef
```


Required fields:
- `Workforces`: `List["WorkforceTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListWorkteamsResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ListWorkteamsResponseTypeDef
```


Required fields:
- `Workteams`: `List["WorkteamTypeDef"]`



Optional fields:
- `NextToken`: `str`


## MemberDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MemberDefinitionTypeDef
```




Optional fields:
- `CognitoMemberDefinition`: `"CognitoMemberDefinitionTypeDef"`
- `OidcMemberDefinition`: `"OidcMemberDefinitionTypeDef"`


## MetadataPropertiesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MetadataPropertiesTypeDef
```




Optional fields:
- `CommitId`: `str`
- `Repository`: `str`
- `GeneratedBy`: `str`
- `ProjectId`: `str`


## MetricDataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MetricDataTypeDef
```




Optional fields:
- `MetricName`: `str`
- `Value`: `float`
- `Timestamp`: `datetime`


## MetricDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MetricDefinitionTypeDef
```


Required fields:
- `Name`: `str`
- `Regex`: `str`




## MetricsSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MetricsSourceTypeDef
```


Required fields:
- `ContentType`: `str`
- `S3Uri`: `str`



Optional fields:
- `ContentDigest`: `str`


## ModelArtifactsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelArtifactsTypeDef
```


Required fields:
- `S3ModelArtifacts`: `str`




## ModelBiasAppSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelBiasAppSpecificationTypeDef
```


Required fields:
- `ImageUri`: `str`
- `ConfigUri`: `str`



Optional fields:
- `Environment`: `Dict[str, str]`


## ModelBiasBaselineConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelBiasBaselineConfigTypeDef
```




Optional fields:
- `BaseliningJobName`: `str`
- `ConstraintsResource`: `"MonitoringConstraintsResourceTypeDef"`


## ModelBiasJobInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelBiasJobInputTypeDef
```


Required fields:
- `EndpointInput`: `"EndpointInputTypeDef"`
- `GroundTruthS3Input`: `"MonitoringGroundTruthS3InputTypeDef"`




## ModelClientConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelClientConfigTypeDef
```




Optional fields:
- `InvocationsTimeoutInSeconds`: `int`
- `InvocationsMaxRetries`: `int`


## ModelDataQualityTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelDataQualityTypeDef
```




Optional fields:
- `Statistics`: `"MetricsSourceTypeDef"`
- `Constraints`: `"MetricsSourceTypeDef"`


## ModelDigestsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelDigestsTypeDef
```




Optional fields:
- `ArtifactDigest`: `str`


## ModelExplainabilityAppSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelExplainabilityAppSpecificationTypeDef
```


Required fields:
- `ImageUri`: `str`
- `ConfigUri`: `str`



Optional fields:
- `Environment`: `Dict[str, str]`


## ModelExplainabilityBaselineConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelExplainabilityBaselineConfigTypeDef
```




Optional fields:
- `BaseliningJobName`: `str`
- `ConstraintsResource`: `"MonitoringConstraintsResourceTypeDef"`


## ModelExplainabilityJobInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelExplainabilityJobInputTypeDef
```


Required fields:
- `EndpointInput`: `"EndpointInputTypeDef"`




## ModelMetricsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelMetricsTypeDef
```




Optional fields:
- `ModelQuality`: `"ModelQualityTypeDef"`
- `ModelDataQuality`: `"ModelDataQualityTypeDef"`
- `Bias`: `"BiasTypeDef"`
- `Explainability`: `"ExplainabilityTypeDef"`


## ModelPackageContainerDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageContainerDefinitionTypeDef
```


Required fields:
- `Image`: `str`



Optional fields:
- `ContainerHostname`: `str`
- `ImageDigest`: `str`
- `ModelDataUrl`: `str`
- `ProductId`: `str`


## ModelPackageGroupSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageGroupSummaryTypeDef
```


Required fields:
- `ModelPackageGroupName`: `str`
- `ModelPackageGroupArn`: `str`
- `CreationTime`: `datetime`
- `ModelPackageGroupStatus`: `ModelPackageGroupStatus`



Optional fields:
- `ModelPackageGroupDescription`: `str`


## ModelPackageGroupTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageGroupTypeDef
```




Optional fields:
- `ModelPackageGroupName`: `str`
- `ModelPackageGroupArn`: `str`
- `ModelPackageGroupDescription`: `str`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `ModelPackageGroupStatus`: `ModelPackageGroupStatus`
- `Tags`: `List["TagTypeDef"]`


## ModelPackageStatusDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageStatusDetailsTypeDef
```


Required fields:
- `ValidationStatuses`: `List["ModelPackageStatusItemTypeDef"]`



Optional fields:
- `ImageScanStatuses`: `List["ModelPackageStatusItemTypeDef"]`


## ModelPackageStatusItemTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageStatusItemTypeDef
```


Required fields:
- `Name`: `str`
- `Status`: `DetailedModelPackageStatus`



Optional fields:
- `FailureReason`: `str`


## ModelPackageSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageSummaryTypeDef
```


Required fields:
- `ModelPackageName`: `str`
- `ModelPackageArn`: `str`
- `CreationTime`: `datetime`
- `ModelPackageStatus`: `ModelPackageStatus`



Optional fields:
- `ModelPackageGroupName`: `str`
- `ModelPackageVersion`: `int`
- `ModelPackageDescription`: `str`
- `ModelApprovalStatus`: `ModelApprovalStatus`


## ModelPackageTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageTypeDef
```




Optional fields:
- `ModelPackageName`: `str`
- `ModelPackageGroupName`: `str`
- `ModelPackageVersion`: `int`
- `ModelPackageArn`: `str`
- `ModelPackageDescription`: `str`
- `CreationTime`: `datetime`
- `InferenceSpecification`: `"InferenceSpecificationTypeDef"`
- `SourceAlgorithmSpecification`: `"SourceAlgorithmSpecificationTypeDef"`
- `ValidationSpecification`: `"ModelPackageValidationSpecificationTypeDef"`
- `ModelPackageStatus`: `ModelPackageStatus`
- `ModelPackageStatusDetails`: `"ModelPackageStatusDetailsTypeDef"`
- `CertifyForMarketplace`: `bool`
- `ModelApprovalStatus`: `ModelApprovalStatus`
- `CreatedBy`: `"UserContextTypeDef"`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`
- `ModelMetrics`: `"ModelMetricsTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `ApprovalDescription`: `str`
- `Tags`: `List["TagTypeDef"]`


## ModelPackageValidationProfileTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageValidationProfileTypeDef
```


Required fields:
- `ProfileName`: `str`
- `TransformJobDefinition`: `"TransformJobDefinitionTypeDef"`




## ModelPackageValidationSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelPackageValidationSpecificationTypeDef
```


Required fields:
- `ValidationRole`: `str`
- `ValidationProfiles`: `List["ModelPackageValidationProfileTypeDef"]`




## ModelQualityAppSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelQualityAppSpecificationTypeDef
```


Required fields:
- `ImageUri`: `str`



Optional fields:
- `ContainerEntrypoint`: `List[str]`
- `ContainerArguments`: `List[str]`
- `RecordPreprocessorSourceUri`: `str`
- `PostAnalyticsProcessorSourceUri`: `str`
- `ProblemType`: `MonitoringProblemType`
- `Environment`: `Dict[str, str]`


## ModelQualityBaselineConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelQualityBaselineConfigTypeDef
```




Optional fields:
- `BaseliningJobName`: `str`
- `ConstraintsResource`: `"MonitoringConstraintsResourceTypeDef"`


## ModelQualityJobInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelQualityJobInputTypeDef
```


Required fields:
- `EndpointInput`: `"EndpointInputTypeDef"`
- `GroundTruthS3Input`: `"MonitoringGroundTruthS3InputTypeDef"`




## ModelQualityTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelQualityTypeDef
```




Optional fields:
- `Statistics`: `"MetricsSourceTypeDef"`
- `Constraints`: `"MetricsSourceTypeDef"`


## ModelStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelStepMetadataTypeDef
```




Optional fields:
- `Arn`: `str`


## ModelSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ModelSummaryTypeDef
```


Required fields:
- `ModelName`: `str`
- `ModelArn`: `str`
- `CreationTime`: `datetime`




## MonitoringAppSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringAppSpecificationTypeDef
```


Required fields:
- `ImageUri`: `str`



Optional fields:
- `ContainerEntrypoint`: `List[str]`
- `ContainerArguments`: `List[str]`
- `RecordPreprocessorSourceUri`: `str`
- `PostAnalyticsProcessorSourceUri`: `str`


## MonitoringBaselineConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringBaselineConfigTypeDef
```




Optional fields:
- `BaseliningJobName`: `str`
- `ConstraintsResource`: `"MonitoringConstraintsResourceTypeDef"`
- `StatisticsResource`: `"MonitoringStatisticsResourceTypeDef"`


## MonitoringClusterConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringClusterConfigTypeDef
```


Required fields:
- `InstanceCount`: `int`
- `InstanceType`: `ProcessingInstanceType`
- `VolumeSizeInGB`: `int`



Optional fields:
- `VolumeKmsKeyId`: `str`


## MonitoringConstraintsResourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringConstraintsResourceTypeDef
```




Optional fields:
- `S3Uri`: `str`


## MonitoringExecutionSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringExecutionSummaryTypeDef
```


Required fields:
- `MonitoringScheduleName`: `str`
- `ScheduledTime`: `datetime`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `MonitoringExecutionStatus`: `ExecutionStatus`



Optional fields:
- `ProcessingJobArn`: `str`
- `EndpointName`: `str`
- `FailureReason`: `str`
- `MonitoringJobDefinitionName`: `str`
- `MonitoringType`: `MonitoringType`


## MonitoringGroundTruthS3InputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringGroundTruthS3InputTypeDef
```




Optional fields:
- `S3Uri`: `str`


## MonitoringInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringInputTypeDef
```


Required fields:
- `EndpointInput`: `"EndpointInputTypeDef"`




## MonitoringJobDefinitionSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringJobDefinitionSummaryTypeDef
```


Required fields:
- `MonitoringJobDefinitionName`: `str`
- `MonitoringJobDefinitionArn`: `str`
- `CreationTime`: `datetime`
- `EndpointName`: `str`




## MonitoringJobDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringJobDefinitionTypeDef
```


Required fields:
- `MonitoringInputs`: `List["MonitoringInputTypeDef"]`
- `MonitoringOutputConfig`: `"MonitoringOutputConfigTypeDef"`
- `MonitoringResources`: `"MonitoringResourcesTypeDef"`
- `MonitoringAppSpecification`: `"MonitoringAppSpecificationTypeDef"`
- `RoleArn`: `str`



Optional fields:
- `BaselineConfig`: `"MonitoringBaselineConfigTypeDef"`
- `StoppingCondition`: `"MonitoringStoppingConditionTypeDef"`
- `Environment`: `Dict[str, str]`
- `NetworkConfig`: `"NetworkConfigTypeDef"`


## MonitoringNetworkConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringNetworkConfigTypeDef
```




Optional fields:
- `EnableInterContainerTrafficEncryption`: `bool`
- `EnableNetworkIsolation`: `bool`
- `VpcConfig`: `"VpcConfigTypeDef"`


## MonitoringOutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringOutputConfigTypeDef
```


Required fields:
- `MonitoringOutputs`: `List["MonitoringOutputTypeDef"]`



Optional fields:
- `KmsKeyId`: `str`


## MonitoringOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringOutputTypeDef
```


Required fields:
- `S3Output`: `"MonitoringS3OutputTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## MonitoringResourcesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringResourcesTypeDef
```


Required fields:
- `ClusterConfig`: `"MonitoringClusterConfigTypeDef"`




## MonitoringS3OutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringS3OutputTypeDef
```


Required fields:
- `S3Uri`: `str`
- `LocalPath`: `str`



Optional fields:
- `S3UploadMode`: `ProcessingS3UploadMode`
- `ResponseMetadata`: `"ResponseMetadata"`


## MonitoringScheduleConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringScheduleConfigTypeDef
```




Optional fields:
- `ScheduleConfig`: `"ScheduleConfigTypeDef"`
- `MonitoringJobDefinition`: `"MonitoringJobDefinitionTypeDef"`
- `MonitoringJobDefinitionName`: `str`
- `MonitoringType`: `MonitoringType`


## MonitoringScheduleSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringScheduleSummaryTypeDef
```


Required fields:
- `MonitoringScheduleName`: `str`
- `MonitoringScheduleArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `MonitoringScheduleStatus`: `ScheduleStatus`



Optional fields:
- `EndpointName`: `str`
- `MonitoringJobDefinitionName`: `str`
- `MonitoringType`: `MonitoringType`


## MonitoringScheduleTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringScheduleTypeDef
```




Optional fields:
- `MonitoringScheduleArn`: `str`
- `MonitoringScheduleName`: `str`
- `MonitoringScheduleStatus`: `ScheduleStatus`
- `MonitoringType`: `MonitoringType`
- `FailureReason`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `MonitoringScheduleConfig`: `"MonitoringScheduleConfigTypeDef"`
- `EndpointName`: `str`
- `LastMonitoringExecutionSummary`: `"MonitoringExecutionSummaryTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## MonitoringStatisticsResourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringStatisticsResourceTypeDef
```




Optional fields:
- `S3Uri`: `str`


## MonitoringStoppingConditionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MonitoringStoppingConditionTypeDef
```


Required fields:
- `MaxRuntimeInSeconds`: `int`




## MultiModelConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import MultiModelConfigTypeDef
```




Optional fields:
- `ModelCacheSetting`: `ModelCacheSetting`


## NestedFiltersTypeDef

```python
from mypy_boto3_sagemaker.type_defs import NestedFiltersTypeDef
```


Required fields:
- `NestedPropertyName`: `str`
- `Filters`: `List["FilterTypeDef"]`




## NetworkConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import NetworkConfigTypeDef
```




Optional fields:
- `EnableInterContainerTrafficEncryption`: `bool`
- `EnableNetworkIsolation`: `bool`
- `VpcConfig`: `"VpcConfigTypeDef"`


## NotebookInstanceLifecycleConfigSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import NotebookInstanceLifecycleConfigSummaryTypeDef
```


Required fields:
- `NotebookInstanceLifecycleConfigName`: `str`
- `NotebookInstanceLifecycleConfigArn`: `str`



Optional fields:
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## NotebookInstanceLifecycleHookTypeDef

```python
from mypy_boto3_sagemaker.type_defs import NotebookInstanceLifecycleHookTypeDef
```




Optional fields:
- `Content`: `str`


## NotebookInstanceSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import NotebookInstanceSummaryTypeDef
```


Required fields:
- `NotebookInstanceName`: `str`
- `NotebookInstanceArn`: `str`



Optional fields:
- `NotebookInstanceStatus`: `NotebookInstanceStatus`
- `Url`: `str`
- `InstanceType`: `InstanceType`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `NotebookInstanceLifecycleConfigName`: `str`
- `DefaultCodeRepository`: `str`
- `AdditionalCodeRepositories`: `List[str]`


## NotificationConfigurationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import NotificationConfigurationTypeDef
```




Optional fields:
- `NotificationTopicArn`: `str`


## ObjectiveStatusCountersTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ObjectiveStatusCountersTypeDef
```




Optional fields:
- `Succeeded`: `int`
- `Pending`: `int`
- `Failed`: `int`


## OfflineStoreConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OfflineStoreConfigTypeDef
```


Required fields:
- `S3StorageConfig`: `"S3StorageConfigTypeDef"`



Optional fields:
- `DisableGlueTableCreation`: `bool`
- `DataCatalogConfig`: `"DataCatalogConfigTypeDef"`


## OfflineStoreStatusTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OfflineStoreStatusTypeDef
```


Required fields:
- `Status`: `OfflineStoreStatusValue`



Optional fields:
- `BlockedReason`: `str`


## OidcConfigForResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OidcConfigForResponseTypeDef
```




Optional fields:
- `ClientId`: `str`
- `Issuer`: `str`
- `AuthorizationEndpoint`: `str`
- `TokenEndpoint`: `str`
- `UserInfoEndpoint`: `str`
- `LogoutEndpoint`: `str`
- `JwksUri`: `str`


## OidcConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OidcConfigTypeDef
```


Required fields:
- `ClientId`: `str`
- `ClientSecret`: `str`
- `Issuer`: `str`
- `AuthorizationEndpoint`: `str`
- `TokenEndpoint`: `str`
- `UserInfoEndpoint`: `str`
- `LogoutEndpoint`: `str`
- `JwksUri`: `str`




## OidcMemberDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OidcMemberDefinitionTypeDef
```


Required fields:
- `Groups`: `List[str]`




## OnlineStoreConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OnlineStoreConfigTypeDef
```




Optional fields:
- `SecurityConfig`: `"OnlineStoreSecurityConfigTypeDef"`
- `EnableOnlineStore`: `bool`


## OnlineStoreSecurityConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OnlineStoreSecurityConfigTypeDef
```




Optional fields:
- `KmsKeyId`: `str`


## OutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OutputConfigTypeDef
```


Required fields:
- `S3OutputLocation`: `str`



Optional fields:
- `TargetDevice`: `TargetDevice`
- `TargetPlatform`: `"TargetPlatformTypeDef"`
- `CompilerOptions`: `str`
- `KmsKeyId`: `str`


## OutputDataConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import OutputDataConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `KmsKeyId`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParameterRangeTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ParameterRangeTypeDef
```




Optional fields:
- `IntegerParameterRangeSpecification`: `"IntegerParameterRangeSpecificationTypeDef"`
- `ContinuousParameterRangeSpecification`: `"ContinuousParameterRangeSpecificationTypeDef"`
- `CategoricalParameterRangeSpecification`: `"CategoricalParameterRangeSpecificationTypeDef"`


## ParameterRangesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ParameterRangesTypeDef
```




Optional fields:
- `IntegerParameterRanges`: `List["IntegerParameterRangeTypeDef"]`
- `ContinuousParameterRanges`: `List["ContinuousParameterRangeTypeDef"]`
- `CategoricalParameterRanges`: `List["CategoricalParameterRangeTypeDef"]`


## ParameterTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## ParentHyperParameterTuningJobTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ParentHyperParameterTuningJobTypeDef
```




Optional fields:
- `HyperParameterTuningJobName`: `str`


## ParentTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ParentTypeDef
```




Optional fields:
- `TrialName`: `str`
- `ExperimentName`: `str`


## PipelineExecutionStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PipelineExecutionStepMetadataTypeDef
```




Optional fields:
- `TrainingJob`: `"TrainingJobStepMetadataTypeDef"`
- `ProcessingJob`: `"ProcessingJobStepMetadataTypeDef"`
- `TransformJob`: `"TransformJobStepMetadataTypeDef"`
- `Model`: `"ModelStepMetadataTypeDef"`
- `RegisterModel`: `"RegisterModelStepMetadataTypeDef"`
- `Condition`: `"ConditionStepMetadataTypeDef"`


## PipelineExecutionStepTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PipelineExecutionStepTypeDef
```




Optional fields:
- `StepName`: `str`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `StepStatus`: `StepStatus`
- `CacheHitResult`: `"CacheHitResultTypeDef"`
- `FailureReason`: `str`
- `Metadata`: `"PipelineExecutionStepMetadataTypeDef"`


## PipelineExecutionSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PipelineExecutionSummaryTypeDef
```




Optional fields:
- `PipelineExecutionArn`: `str`
- `StartTime`: `datetime`
- `PipelineExecutionStatus`: `PipelineExecutionStatus`
- `PipelineExecutionDescription`: `str`
- `PipelineExecutionDisplayName`: `str`


## PipelineExecutionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PipelineExecutionTypeDef
```




Optional fields:
- `PipelineArn`: `str`
- `PipelineExecutionArn`: `str`
- `PipelineExecutionDisplayName`: `str`
- `PipelineExecutionStatus`: `PipelineExecutionStatus`
- `PipelineExecutionDescription`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `PipelineParameters`: `List["ParameterTypeDef"]`


## PipelineSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PipelineSummaryTypeDef
```




Optional fields:
- `PipelineArn`: `str`
- `PipelineName`: `str`
- `PipelineDisplayName`: `str`
- `PipelineDescription`: `str`
- `RoleArn`: `str`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastExecutionTime`: `datetime`


## PipelineTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PipelineTypeDef
```




Optional fields:
- `PipelineArn`: `str`
- `PipelineName`: `str`
- `PipelineDisplayName`: `str`
- `PipelineDescription`: `str`
- `RoleArn`: `str`
- `PipelineStatus`: `Literal['Active']`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastRunTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## ProcessingClusterConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingClusterConfigTypeDef
```


Required fields:
- `InstanceCount`: `int`
- `InstanceType`: `ProcessingInstanceType`
- `VolumeSizeInGB`: `int`



Optional fields:
- `VolumeKmsKeyId`: `str`


## ProcessingFeatureStoreOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingFeatureStoreOutputTypeDef
```


Required fields:
- `FeatureGroupName`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ProcessingInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingInputTypeDef
```


Required fields:
- `InputName`: `str`



Optional fields:
- `AppManaged`: `bool`
- `S3Input`: `"ProcessingS3InputTypeDef"`
- `DatasetDefinition`: `"DatasetDefinitionTypeDef"`


## ProcessingJobStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingJobStepMetadataTypeDef
```




Optional fields:
- `Arn`: `str`


## ProcessingJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingJobSummaryTypeDef
```


Required fields:
- `ProcessingJobName`: `str`
- `ProcessingJobArn`: `str`
- `CreationTime`: `datetime`
- `ProcessingJobStatus`: `ProcessingJobStatus`



Optional fields:
- `ProcessingEndTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`
- `ExitMessage`: `str`


## ProcessingJobTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingJobTypeDef
```




Optional fields:
- `ProcessingInputs`: `List["ProcessingInputTypeDef"]`
- `ProcessingOutputConfig`: `"ProcessingOutputConfigTypeDef"`
- `ProcessingJobName`: `str`
- `ProcessingResources`: `"ProcessingResourcesTypeDef"`
- `StoppingCondition`: `"ProcessingStoppingConditionTypeDef"`
- `AppSpecification`: `"AppSpecificationTypeDef"`
- `Environment`: `Dict[str, str]`
- `NetworkConfig`: `"NetworkConfigTypeDef"`
- `RoleArn`: `str`
- `ExperimentConfig`: `"ExperimentConfigTypeDef"`
- `ProcessingJobArn`: `str`
- `ProcessingJobStatus`: `ProcessingJobStatus`
- `ExitMessage`: `str`
- `FailureReason`: `str`
- `ProcessingEndTime`: `datetime`
- `ProcessingStartTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `CreationTime`: `datetime`
- `MonitoringScheduleArn`: `str`
- `AutoMLJobArn`: `str`
- `TrainingJobArn`: `str`
- `Tags`: `List["TagTypeDef"]`


## ProcessingOutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingOutputConfigTypeDef
```


Required fields:
- `Outputs`: `List["ProcessingOutputTypeDef"]`



Optional fields:
- `KmsKeyId`: `str`


## ProcessingOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingOutputTypeDef
```


Required fields:
- `OutputName`: `str`



Optional fields:
- `S3Output`: `"ProcessingS3OutputTypeDef"`
- `FeatureStoreOutput`: `"ProcessingFeatureStoreOutputTypeDef"`
- `AppManaged`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## ProcessingResourcesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingResourcesTypeDef
```


Required fields:
- `ClusterConfig`: `"ProcessingClusterConfigTypeDef"`




## ProcessingS3InputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingS3InputTypeDef
```


Required fields:
- `S3Uri`: `str`
- `S3DataType`: `ProcessingS3DataType`



Optional fields:
- `LocalPath`: `str`
- `S3InputMode`: `ProcessingS3InputMode`
- `S3DataDistributionType`: `ProcessingS3DataDistributionType`
- `S3CompressionType`: `ProcessingS3CompressionType`


## ProcessingS3OutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingS3OutputTypeDef
```


Required fields:
- `S3Uri`: `str`
- `LocalPath`: `str`
- `S3UploadMode`: `ProcessingS3UploadMode`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## ProcessingStoppingConditionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProcessingStoppingConditionTypeDef
```


Required fields:
- `MaxRuntimeInSeconds`: `int`




## ProductionVariantCoreDumpConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProductionVariantCoreDumpConfigTypeDef
```


Required fields:
- `DestinationS3Uri`: `str`



Optional fields:
- `KmsKeyId`: `str`


## ProductionVariantSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProductionVariantSummaryTypeDef
```


Required fields:
- `VariantName`: `str`



Optional fields:
- `DeployedImages`: `List["DeployedImageTypeDef"]`
- `CurrentWeight`: `float`
- `DesiredWeight`: `float`
- `CurrentInstanceCount`: `int`
- `DesiredInstanceCount`: `int`


## ProductionVariantTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProductionVariantTypeDef
```


Required fields:
- `VariantName`: `str`
- `ModelName`: `str`
- `InitialInstanceCount`: `int`
- `InstanceType`: `ProductionVariantInstanceType`



Optional fields:
- `InitialVariantWeight`: `float`
- `AcceleratorType`: `ProductionVariantAcceleratorType`
- `CoreDumpConfig`: `"ProductionVariantCoreDumpConfigTypeDef"`


## ProfilerConfigForUpdateTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProfilerConfigForUpdateTypeDef
```




Optional fields:
- `S3OutputPath`: `str`
- `ProfilingIntervalInMilliseconds`: `int`
- `ProfilingParameters`: `Dict[str, str]`
- `DisableProfiler`: `bool`


## ProfilerConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProfilerConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `ProfilingIntervalInMilliseconds`: `int`
- `ProfilingParameters`: `Dict[str, str]`


## ProfilerRuleConfigurationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProfilerRuleConfigurationTypeDef
```


Required fields:
- `RuleConfigurationName`: `str`
- `RuleEvaluatorImage`: `str`



Optional fields:
- `LocalPath`: `str`
- `S3OutputPath`: `str`
- `InstanceType`: `ProcessingInstanceType`
- `VolumeSizeInGB`: `int`
- `RuleParameters`: `Dict[str, str]`


## ProfilerRuleEvaluationStatusTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProfilerRuleEvaluationStatusTypeDef
```




Optional fields:
- `RuleConfigurationName`: `str`
- `RuleEvaluationJobArn`: `str`
- `RuleEvaluationStatus`: `RuleEvaluationStatus`
- `StatusDetails`: `str`
- `LastModifiedTime`: `datetime`


## ProjectSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProjectSummaryTypeDef
```


Required fields:
- `ProjectName`: `str`
- `ProjectArn`: `str`
- `ProjectId`: `str`
- `CreationTime`: `datetime`
- `ProjectStatus`: `ProjectStatus`



Optional fields:
- `ProjectDescription`: `str`


## PropertyNameQueryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PropertyNameQueryTypeDef
```


Required fields:
- `PropertyNameHint`: `str`




## PropertyNameSuggestionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PropertyNameSuggestionTypeDef
```




Optional fields:
- `PropertyName`: `str`


## ProvisioningParameterTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ProvisioningParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## PublicWorkforceTaskPriceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PublicWorkforceTaskPriceTypeDef
```




Optional fields:
- `AmountInUsd`: `"USDTypeDef"`


## PutModelPackageGroupPolicyOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import PutModelPackageGroupPolicyOutputTypeDef
```


Required fields:
- `ModelPackageGroupArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## RedshiftDatasetDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RedshiftDatasetDefinitionTypeDef
```


Required fields:
- `ClusterId`: `str`
- `Database`: `str`
- `DbUser`: `str`
- `QueryString`: `str`
- `ClusterRoleArn`: `str`
- `OutputS3Uri`: `str`
- `OutputFormat`: `RedshiftResultFormat`



Optional fields:
- `KmsKeyId`: `str`
- `OutputCompression`: `RedshiftResultCompressionType`


## RegisterModelStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RegisterModelStepMetadataTypeDef
```




Optional fields:
- `Arn`: `str`


## RenderUiTemplateResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RenderUiTemplateResponseTypeDef
```


Required fields:
- `RenderedContent`: `str`
- `Errors`: `List["RenderingErrorTypeDef"]`




## RenderableTaskTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RenderableTaskTypeDef
```


Required fields:
- `Input`: `str`




## RenderingErrorTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RenderingErrorTypeDef
```


Required fields:
- `Code`: `str`
- `Message`: `str`




## RepositoryAuthConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RepositoryAuthConfigTypeDef
```


Required fields:
- `RepositoryCredentialsProviderArn`: `str`




## ResolvedAttributesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ResolvedAttributesTypeDef
```




Optional fields:
- `AutoMLJobObjective`: `"AutoMLJobObjectiveTypeDef"`
- `ProblemType`: `ProblemType`
- `CompletionCriteria`: `"AutoMLJobCompletionCriteriaTypeDef"`


## ResourceConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ResourceConfigTypeDef
```


Required fields:
- `InstanceType`: `TrainingInstanceType`
- `InstanceCount`: `int`
- `VolumeSizeInGB`: `int`



Optional fields:
- `VolumeKmsKeyId`: `str`


## ResourceLimitsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ResourceLimitsTypeDef
```


Required fields:
- `MaxNumberOfTrainingJobs`: `int`
- `MaxParallelTrainingJobs`: `int`




## ResourceSpecTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ResourceSpecTypeDef
```




Optional fields:
- `SageMakerImageArn`: `str`
- `SageMakerImageVersionArn`: `str`
- `InstanceType`: `AppInstanceType`


## ResponseMetadata

```python
from mypy_boto3_sagemaker.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RetentionPolicyTypeDef

```python
from mypy_boto3_sagemaker.type_defs import RetentionPolicyTypeDef
```




Optional fields:
- `HomeEfsFileSystem`: `RetentionType`


## S3DataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import S3DataSourceTypeDef
```


Required fields:
- `S3DataType`: `S3DataType`
- `S3Uri`: `str`



Optional fields:
- `S3DataDistributionType`: `S3DataDistribution`
- `AttributeNames`: `List[str]`


## S3StorageConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import S3StorageConfigTypeDef
```


Required fields:
- `S3Uri`: `str`



Optional fields:
- `KmsKeyId`: `str`
- `ResolvedOutputS3Uri`: `str`


## ScheduleConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ScheduleConfigTypeDef
```


Required fields:
- `ScheduleExpression`: `str`




## SearchExpressionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SearchExpressionTypeDef
```




Optional fields:
- `Filters`: `List["FilterTypeDef"]`
- `NestedFilters`: `List["NestedFiltersTypeDef"]`
- `SubExpressions`: `List[Dict[str, Any]]`
- `Operator`: `BooleanOperator`


## SearchRecordTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SearchRecordTypeDef
```




Optional fields:
- `TrainingJob`: `"TrainingJobTypeDef"`
- `Experiment`: `"ExperimentTypeDef"`
- `Trial`: `"TrialTypeDef"`
- `TrialComponent`: `"TrialComponentTypeDef"`
- `Endpoint`: `"EndpointTypeDef"`
- `ModelPackage`: `"ModelPackageTypeDef"`
- `ModelPackageGroup`: `"ModelPackageGroupTypeDef"`
- `Pipeline`: `"PipelineTypeDef"`
- `PipelineExecution`: `"PipelineExecutionTypeDef"`
- `FeatureGroup`: `"FeatureGroupTypeDef"`


## SearchResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SearchResponseTypeDef
```




Optional fields:
- `Results`: `List["SearchRecordTypeDef"]`
- `NextToken`: `str`


## SecondaryStatusTransitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SecondaryStatusTransitionTypeDef
```


Required fields:
- `Status`: `SecondaryStatus`
- `StartTime`: `datetime`



Optional fields:
- `EndTime`: `datetime`
- `StatusMessage`: `str`


## ServiceCatalogProvisionedProductDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ServiceCatalogProvisionedProductDetailsTypeDef
```




Optional fields:
- `ProvisionedProductId`: `str`
- `ProvisionedProductStatusMessage`: `str`


## ServiceCatalogProvisioningDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ServiceCatalogProvisioningDetailsTypeDef
```


Required fields:
- `ProductId`: `str`
- `ProvisioningArtifactId`: `str`



Optional fields:
- `PathId`: `str`
- `ProvisioningParameters`: `List["ProvisioningParameterTypeDef"]`


## SharingSettingsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SharingSettingsTypeDef
```




Optional fields:
- `NotebookOutputOption`: `NotebookOutputOption`
- `S3OutputPath`: `str`
- `S3KmsKeyId`: `str`


## ShuffleConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import ShuffleConfigTypeDef
```


Required fields:
- `Seed`: `int`




## SourceAlgorithmSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SourceAlgorithmSpecificationTypeDef
```


Required fields:
- `SourceAlgorithms`: `List["SourceAlgorithmTypeDef"]`




## SourceAlgorithmTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SourceAlgorithmTypeDef
```


Required fields:
- `AlgorithmName`: `str`



Optional fields:
- `ModelDataUrl`: `str`


## SourceIpConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SourceIpConfigTypeDef
```


Required fields:
- `Cidrs`: `List[str]`




## StartPipelineExecutionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import StartPipelineExecutionResponseTypeDef
```




Optional fields:
- `PipelineExecutionArn`: `str`


## StopPipelineExecutionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import StopPipelineExecutionResponseTypeDef
```




Optional fields:
- `PipelineExecutionArn`: `str`


## StoppingConditionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import StoppingConditionTypeDef
```




Optional fields:
- `MaxRuntimeInSeconds`: `int`
- `MaxWaitTimeInSeconds`: `int`


## SubscribedWorkteamTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SubscribedWorkteamTypeDef
```


Required fields:
- `WorkteamArn`: `str`



Optional fields:
- `MarketplaceTitle`: `str`
- `SellerName`: `str`
- `MarketplaceDescription`: `str`
- `ListingId`: `str`


## SuggestionQueryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import SuggestionQueryTypeDef
```




Optional fields:
- `PropertyNameQuery`: `"PropertyNameQueryTypeDef"`


## TagTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TargetPlatformTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TargetPlatformTypeDef
```


Required fields:
- `Os`: `TargetPlatformOs`
- `Arch`: `TargetPlatformArch`



Optional fields:
- `Accelerator`: `TargetPlatformAccelerator`


## TensorBoardAppSettingsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TensorBoardAppSettingsTypeDef
```




Optional fields:
- `DefaultResourceSpec`: `"ResourceSpecTypeDef"`


## TensorBoardOutputConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TensorBoardOutputConfigTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `LocalPath`: `str`


## TrafficRoutingConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrafficRoutingConfigTypeDef
```


Required fields:
- `Type`: `TrafficRoutingConfigType`
- `WaitIntervalInSeconds`: `int`



Optional fields:
- `CanarySize`: `"CapacitySizeTypeDef"`


## TrainingJobDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrainingJobDefinitionTypeDef
```


Required fields:
- `TrainingInputMode`: `TrainingInputMode`
- `InputDataConfig`: `List["ChannelTypeDef"]`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `ResourceConfig`: `"ResourceConfigTypeDef"`
- `StoppingCondition`: `"StoppingConditionTypeDef"`



Optional fields:
- `HyperParameters`: `Dict[str, str]`


## TrainingJobStatusCountersTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrainingJobStatusCountersTypeDef
```




Optional fields:
- `Completed`: `int`
- `InProgress`: `int`
- `RetryableError`: `int`
- `NonRetryableError`: `int`
- `Stopped`: `int`


## TrainingJobStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrainingJobStepMetadataTypeDef
```




Optional fields:
- `Arn`: `str`


## TrainingJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrainingJobSummaryTypeDef
```


Required fields:
- `TrainingJobName`: `str`
- `TrainingJobArn`: `str`
- `CreationTime`: `datetime`
- `TrainingJobStatus`: `TrainingJobStatus`



Optional fields:
- `TrainingEndTime`: `datetime`
- `LastModifiedTime`: `datetime`


## TrainingJobTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrainingJobTypeDef
```




Optional fields:
- `TrainingJobName`: `str`
- `TrainingJobArn`: `str`
- `TuningJobArn`: `str`
- `LabelingJobArn`: `str`
- `AutoMLJobArn`: `str`
- `ModelArtifacts`: `"ModelArtifactsTypeDef"`
- `TrainingJobStatus`: `TrainingJobStatus`
- `SecondaryStatus`: `SecondaryStatus`
- `FailureReason`: `str`
- `HyperParameters`: `Dict[str, str]`
- `AlgorithmSpecification`: `"AlgorithmSpecificationTypeDef"`
- `RoleArn`: `str`
- `InputDataConfig`: `List["ChannelTypeDef"]`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `ResourceConfig`: `"ResourceConfigTypeDef"`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `StoppingCondition`: `"StoppingConditionTypeDef"`
- `CreationTime`: `datetime`
- `TrainingStartTime`: `datetime`
- `TrainingEndTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `SecondaryStatusTransitions`: `List["SecondaryStatusTransitionTypeDef"]`
- `FinalMetricDataList`: `List["MetricDataTypeDef"]`
- `EnableNetworkIsolation`: `bool`
- `EnableInterContainerTrafficEncryption`: `bool`
- `EnableManagedSpotTraining`: `bool`
- `CheckpointConfig`: `"CheckpointConfigTypeDef"`
- `TrainingTimeInSeconds`: `int`
- `BillableTimeInSeconds`: `int`
- `DebugHookConfig`: `"DebugHookConfigTypeDef"`
- `ExperimentConfig`: `"ExperimentConfigTypeDef"`
- `DebugRuleConfigurations`: `List["DebugRuleConfigurationTypeDef"]`
- `TensorBoardOutputConfig`: `"TensorBoardOutputConfigTypeDef"`
- `DebugRuleEvaluationStatuses`: `List["DebugRuleEvaluationStatusTypeDef"]`
- `Environment`: `Dict[str, str]`
- `Tags`: `List["TagTypeDef"]`


## TrainingSpecificationTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrainingSpecificationTypeDef
```


Required fields:
- `TrainingImage`: `str`
- `SupportedTrainingInstanceTypes`: `List[TrainingInstanceType]`
- `TrainingChannels`: `List["ChannelSpecificationTypeDef"]`



Optional fields:
- `TrainingImageDigest`: `str`
- `SupportedHyperParameters`: `List["HyperParameterSpecificationTypeDef"]`
- `SupportsDistributedTraining`: `bool`
- `MetricDefinitions`: `List["MetricDefinitionTypeDef"]`
- `SupportedTuningJobObjectiveMetrics`: `List["HyperParameterTuningJobObjectiveTypeDef"]`


## TransformDataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformDataSourceTypeDef
```


Required fields:
- `S3DataSource`: `"TransformS3DataSourceTypeDef"`




## TransformInputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformInputTypeDef
```


Required fields:
- `DataSource`: `"TransformDataSourceTypeDef"`



Optional fields:
- `ContentType`: `str`
- `CompressionType`: `CompressionType`
- `SplitType`: `SplitType`


## TransformJobDefinitionTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformJobDefinitionTypeDef
```


Required fields:
- `TransformInput`: `"TransformInputTypeDef"`
- `TransformOutput`: `"TransformOutputTypeDef"`
- `TransformResources`: `"TransformResourcesTypeDef"`



Optional fields:
- `MaxConcurrentTransforms`: `int`
- `MaxPayloadInMB`: `int`
- `BatchStrategy`: `BatchStrategy`
- `Environment`: `Dict[str, str]`


## TransformJobStepMetadataTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformJobStepMetadataTypeDef
```




Optional fields:
- `Arn`: `str`


## TransformJobSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformJobSummaryTypeDef
```


Required fields:
- `TransformJobName`: `str`
- `TransformJobArn`: `str`
- `CreationTime`: `datetime`
- `TransformJobStatus`: `TransformJobStatus`



Optional fields:
- `TransformEndTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `FailureReason`: `str`


## TransformJobTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformJobTypeDef
```




Optional fields:
- `TransformJobName`: `str`
- `TransformJobArn`: `str`
- `TransformJobStatus`: `TransformJobStatus`
- `FailureReason`: `str`
- `ModelName`: `str`
- `MaxConcurrentTransforms`: `int`
- `ModelClientConfig`: `"ModelClientConfigTypeDef"`
- `MaxPayloadInMB`: `int`
- `BatchStrategy`: `BatchStrategy`
- `Environment`: `Dict[str, str]`
- `TransformInput`: `"TransformInputTypeDef"`
- `TransformOutput`: `"TransformOutputTypeDef"`
- `TransformResources`: `"TransformResourcesTypeDef"`
- `CreationTime`: `datetime`
- `TransformStartTime`: `datetime`
- `TransformEndTime`: `datetime`
- `LabelingJobArn`: `str`
- `AutoMLJobArn`: `str`
- `DataProcessing`: `"DataProcessingTypeDef"`
- `ExperimentConfig`: `"ExperimentConfigTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## TransformOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformOutputTypeDef
```


Required fields:
- `S3OutputPath`: `str`



Optional fields:
- `Accept`: `str`
- `AssembleWith`: `AssemblyType`
- `KmsKeyId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## TransformResourcesTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformResourcesTypeDef
```


Required fields:
- `InstanceType`: `TransformInstanceType`
- `InstanceCount`: `int`



Optional fields:
- `VolumeKmsKeyId`: `str`


## TransformS3DataSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TransformS3DataSourceTypeDef
```


Required fields:
- `S3DataType`: `S3DataType`
- `S3Uri`: `str`




## TrialComponentArtifactTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentArtifactTypeDef
```


Required fields:
- `Value`: `str`



Optional fields:
- `MediaType`: `str`


## TrialComponentMetricSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentMetricSummaryTypeDef
```




Optional fields:
- `MetricName`: `str`
- `SourceArn`: `str`
- `TimeStamp`: `datetime`
- `Max`: `float`
- `Min`: `float`
- `Last`: `float`
- `Count`: `int`
- `Avg`: `float`
- `StdDev`: `float`


## TrialComponentParameterValueTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentParameterValueTypeDef
```




Optional fields:
- `StringValue`: `str`
- `NumberValue`: `float`


## TrialComponentSimpleSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentSimpleSummaryTypeDef
```




Optional fields:
- `TrialComponentName`: `str`
- `TrialComponentArn`: `str`
- `TrialComponentSource`: `"TrialComponentSourceTypeDef"`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`


## TrialComponentSourceDetailTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentSourceDetailTypeDef
```




Optional fields:
- `SourceArn`: `str`
- `TrainingJob`: `"TrainingJobTypeDef"`
- `ProcessingJob`: `"ProcessingJobTypeDef"`
- `TransformJob`: `"TransformJobTypeDef"`


## TrialComponentSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentSourceTypeDef
```


Required fields:
- `SourceArn`: `str`



Optional fields:
- `SourceType`: `str`


## TrialComponentStatusTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentStatusTypeDef
```




Optional fields:
- `PrimaryStatus`: `TrialComponentPrimaryStatus`
- `Message`: `str`


## TrialComponentSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentSummaryTypeDef
```




Optional fields:
- `TrialComponentName`: `str`
- `TrialComponentArn`: `str`
- `DisplayName`: `str`
- `TrialComponentSource`: `"TrialComponentSourceTypeDef"`
- `Status`: `"TrialComponentStatusTypeDef"`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`


## TrialComponentTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialComponentTypeDef
```




Optional fields:
- `TrialComponentName`: `str`
- `DisplayName`: `str`
- `TrialComponentArn`: `str`
- `Source`: `"TrialComponentSourceTypeDef"`
- `Status`: `"TrialComponentStatusTypeDef"`
- `StartTime`: `datetime`
- `EndTime`: `datetime`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `Parameters`: `Dict[str, "TrialComponentParameterValueTypeDef"]`
- `InputArtifacts`: `Dict[str, "TrialComponentArtifactTypeDef"]`
- `OutputArtifacts`: `Dict[str, "TrialComponentArtifactTypeDef"]`
- `Metrics`: `List["TrialComponentMetricSummaryTypeDef"]`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`
- `SourceDetail`: `"TrialComponentSourceDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `Parents`: `List["ParentTypeDef"]`


## TrialSourceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialSourceTypeDef
```


Required fields:
- `SourceArn`: `str`



Optional fields:
- `SourceType`: `str`


## TrialSummaryTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialSummaryTypeDef
```




Optional fields:
- `TrialArn`: `str`
- `TrialName`: `str`
- `DisplayName`: `str`
- `TrialSource`: `"TrialSourceTypeDef"`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## TrialTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TrialTypeDef
```




Optional fields:
- `TrialName`: `str`
- `TrialArn`: `str`
- `DisplayName`: `str`
- `ExperimentName`: `str`
- `Source`: `"TrialSourceTypeDef"`
- `CreationTime`: `datetime`
- `CreatedBy`: `"UserContextTypeDef"`
- `LastModifiedTime`: `datetime`
- `LastModifiedBy`: `"UserContextTypeDef"`
- `MetadataProperties`: `"MetadataPropertiesTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `TrialComponentSummaries`: `List["TrialComponentSimpleSummaryTypeDef"]`


## TuningJobCompletionCriteriaTypeDef

```python
from mypy_boto3_sagemaker.type_defs import TuningJobCompletionCriteriaTypeDef
```


Required fields:
- `TargetObjectiveMetricValue`: `float`




## USDTypeDef

```python
from mypy_boto3_sagemaker.type_defs import USDTypeDef
```




Optional fields:
- `Dollars`: `int`
- `Cents`: `int`
- `TenthFractionsOfACent`: `int`


## UiConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UiConfigTypeDef
```




Optional fields:
- `UiTemplateS3Uri`: `str`
- `HumanTaskUiArn`: `str`


## UiTemplateInfoTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UiTemplateInfoTypeDef
```




Optional fields:
- `Url`: `str`
- `ContentSha256`: `str`


## UiTemplateTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UiTemplateTypeDef
```


Required fields:
- `Content`: `str`




## UpdateActionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateActionResponseTypeDef
```




Optional fields:
- `ActionArn`: `str`


## UpdateAppImageConfigResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateAppImageConfigResponseTypeDef
```




Optional fields:
- `AppImageConfigArn`: `str`


## UpdateArtifactResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateArtifactResponseTypeDef
```




Optional fields:
- `ArtifactArn`: `str`


## UpdateCodeRepositoryOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateCodeRepositoryOutputTypeDef
```


Required fields:
- `CodeRepositoryArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateContextResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateContextResponseTypeDef
```




Optional fields:
- `ContextArn`: `str`


## UpdateDomainResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateDomainResponseTypeDef
```




Optional fields:
- `DomainArn`: `str`


## UpdateEndpointOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateEndpointOutputTypeDef
```


Required fields:
- `EndpointArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateEndpointWeightsAndCapacitiesOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateEndpointWeightsAndCapacitiesOutputTypeDef
```


Required fields:
- `EndpointArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateExperimentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateExperimentResponseTypeDef
```




Optional fields:
- `ExperimentArn`: `str`


## UpdateImageResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateImageResponseTypeDef
```




Optional fields:
- `ImageArn`: `str`


## UpdateModelPackageOutputTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateModelPackageOutputTypeDef
```


Required fields:
- `ModelPackageArn`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateMonitoringScheduleResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateMonitoringScheduleResponseTypeDef
```


Required fields:
- `MonitoringScheduleArn`: `str`




## UpdatePipelineExecutionResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdatePipelineExecutionResponseTypeDef
```




Optional fields:
- `PipelineExecutionArn`: `str`


## UpdatePipelineResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdatePipelineResponseTypeDef
```




Optional fields:
- `PipelineArn`: `str`


## UpdateTrainingJobResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateTrainingJobResponseTypeDef
```


Required fields:
- `TrainingJobArn`: `str`




## UpdateTrialComponentResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateTrialComponentResponseTypeDef
```




Optional fields:
- `TrialComponentArn`: `str`


## UpdateTrialResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateTrialResponseTypeDef
```




Optional fields:
- `TrialArn`: `str`


## UpdateUserProfileResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateUserProfileResponseTypeDef
```




Optional fields:
- `UserProfileArn`: `str`


## UpdateWorkforceResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateWorkforceResponseTypeDef
```


Required fields:
- `Workforce`: `"WorkforceTypeDef"`




## UpdateWorkteamResponseTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UpdateWorkteamResponseTypeDef
```


Required fields:
- `Workteam`: `"WorkteamTypeDef"`




## UserContextTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UserContextTypeDef
```




Optional fields:
- `UserProfileArn`: `str`
- `UserProfileName`: `str`
- `DomainId`: `str`


## UserProfileDetailsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UserProfileDetailsTypeDef
```




Optional fields:
- `DomainId`: `str`
- `UserProfileName`: `str`
- `Status`: `UserProfileStatus`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## UserSettingsTypeDef

```python
from mypy_boto3_sagemaker.type_defs import UserSettingsTypeDef
```




Optional fields:
- `ExecutionRole`: `str`
- `SecurityGroups`: `List[str]`
- `SharingSettings`: `"SharingSettingsTypeDef"`
- `JupyterServerAppSettings`: `"JupyterServerAppSettingsTypeDef"`
- `KernelGatewayAppSettings`: `"KernelGatewayAppSettingsTypeDef"`
- `TensorBoardAppSettings`: `"TensorBoardAppSettingsTypeDef"`


## VariantPropertyTypeDef

```python
from mypy_boto3_sagemaker.type_defs import VariantPropertyTypeDef
```


Required fields:
- `VariantPropertyType`: `VariantPropertyType`




## VpcConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import VpcConfigTypeDef
```


Required fields:
- `SecurityGroupIds`: `List[str]`
- `Subnets`: `List[str]`




## WaiterConfigTypeDef

```python
from mypy_boto3_sagemaker.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`


## WorkforceTypeDef

```python
from mypy_boto3_sagemaker.type_defs import WorkforceTypeDef
```


Required fields:
- `WorkforceName`: `str`
- `WorkforceArn`: `str`



Optional fields:
- `LastUpdatedDate`: `datetime`
- `SourceIpConfig`: `"SourceIpConfigTypeDef"`
- `SubDomain`: `str`
- `CognitoConfig`: `"CognitoConfigTypeDef"`
- `OidcConfig`: `"OidcConfigForResponseTypeDef"`
- `CreateDate`: `datetime`


## WorkteamTypeDef

```python
from mypy_boto3_sagemaker.type_defs import WorkteamTypeDef
```


Required fields:
- `WorkteamName`: `str`
- `MemberDefinitions`: `List["MemberDefinitionTypeDef"]`
- `WorkteamArn`: `str`
- `Description`: `str`



Optional fields:
- `WorkforceArn`: `str`
- `ProductListingIds`: `List[str]`
- `SubDomain`: `str`
- `CreateDate`: `datetime`
- `LastUpdatedDate`: `datetime`
- `NotificationConfiguration`: `"NotificationConfigurationTypeDef"`

