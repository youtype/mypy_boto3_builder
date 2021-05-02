# Type annotations for boto3 ForecastService module

> [Index](../index.md) > ForecastService

Auto-generated documentation for [ForecastService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService)
type annotations stubs module [mypy_boto3_forecast](https://pypi.org/project/mypy-boto3-forecast/).

```bash
pip install mypy-boto3-forecast
```

- [Type annotations for boto3 ForecastService module](#type-annotations-for-boto3-forecastservice-module)
  - [ForecastServiceClient](#forecastserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ForecastServiceClient

Type annotations for  `boto3.client("forecast")` as [ForecastServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_forecast.client import ForecastServiceClient
```


ForecastServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_dataset](./client.md#create-dataset)
- [create_dataset_group](./client.md#create-dataset-group)
- [create_dataset_import_job](./client.md#create-dataset-import-job)
- [create_forecast](./client.md#create-forecast)
- [create_forecast_export_job](./client.md#create-forecast-export-job)
- [create_predictor](./client.md#create-predictor)
- [create_predictor_backtest_export_job](./client.md#create-predictor-backtest-export-job)
- [delete_dataset](./client.md#delete-dataset)
- [delete_dataset_group](./client.md#delete-dataset-group)
- [delete_dataset_import_job](./client.md#delete-dataset-import-job)
- [delete_forecast](./client.md#delete-forecast)
- [delete_forecast_export_job](./client.md#delete-forecast-export-job)
- [delete_predictor](./client.md#delete-predictor)
- [delete_predictor_backtest_export_job](./client.md#delete-predictor-backtest-export-job)
- [delete_resource_tree](./client.md#delete-resource-tree)
- [describe_dataset](./client.md#describe-dataset)
- [describe_dataset_group](./client.md#describe-dataset-group)
- [describe_dataset_import_job](./client.md#describe-dataset-import-job)
- [describe_forecast](./client.md#describe-forecast)
- [describe_forecast_export_job](./client.md#describe-forecast-export-job)
- [describe_predictor](./client.md#describe-predictor)
- [describe_predictor_backtest_export_job](./client.md#describe-predictor-backtest-export-job)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_accuracy_metrics](./client.md#get-accuracy-metrics)
- [get_paginator](./client.md#get-paginator)
- [list_dataset_groups](./client.md#list-dataset-groups)
- [list_dataset_import_jobs](./client.md#list-dataset-import-jobs)
- [list_datasets](./client.md#list-datasets)
- [list_forecast_export_jobs](./client.md#list-forecast-export-jobs)
- [list_forecasts](./client.md#list-forecasts)
- [list_predictor_backtest_export_jobs](./client.md#list-predictor-backtest-export-jobs)
- [list_predictors](./client.md#list-predictors)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [stop_resource](./client.md#stop-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_dataset_group](./client.md#update-dataset-group)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidInputException](./client.md#invalidinputexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("forecast").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_forecast.paginators import ListDatasetGroupsPaginator, ...
```

- [ListDatasetGroupsPaginator](./paginators.md#listdatasetgroupspaginator)
- [ListDatasetImportJobsPaginator](./paginators.md#listdatasetimportjobspaginator)
- [ListDatasetsPaginator](./paginators.md#listdatasetspaginator)
- [ListForecastExportJobsPaginator](./paginators.md#listforecastexportjobspaginator)
- [ListForecastsPaginator](./paginators.md#listforecastspaginator)
- [ListPredictorBacktestExportJobsPaginator](./paginators.md#listpredictorbacktestexportjobspaginator)
- [ListPredictorsPaginator](./paginators.md#listpredictorspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_forecast.literals import AttributeType, ...
```

- [AttributeType](./literals.md#attributetype)
- [DatasetType](./literals.md#datasettype)
- [Domain](./literals.md#domain)
- [EvaluationType](./literals.md#evaluationtype)
- [FeaturizationMethodName](./literals.md#featurizationmethodname)
- [FilterConditionString](./literals.md#filterconditionstring)
- [ListDatasetGroupsPaginatorName](./literals.md#listdatasetgroupspaginatorname)
- [ListDatasetImportJobsPaginatorName](./literals.md#listdatasetimportjobspaginatorname)
- [ListDatasetsPaginatorName](./literals.md#listdatasetspaginatorname)
- [ListForecastExportJobsPaginatorName](./literals.md#listforecastexportjobspaginatorname)
- [ListForecastsPaginatorName](./literals.md#listforecastspaginatorname)
- [ListPredictorBacktestExportJobsPaginatorName](./literals.md#listpredictorbacktestexportjobspaginatorname)
- [ListPredictorsPaginatorName](./literals.md#listpredictorspaginatorname)
- [ScalingType](./literals.md#scalingtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_forecast.type_defs import CategoricalParameterRangeTypeDef, ...
```

- [CategoricalParameterRangeTypeDef](./type_defs.md#categoricalparameterrangetypedef)
- [ContinuousParameterRangeTypeDef](./type_defs.md#continuousparameterrangetypedef)
- [CreateDatasetGroupResponseTypeDef](./type_defs.md#createdatasetgroupresponsetypedef)
- [CreateDatasetImportJobResponseTypeDef](./type_defs.md#createdatasetimportjobresponsetypedef)
- [CreateDatasetResponseTypeDef](./type_defs.md#createdatasetresponsetypedef)
- [CreateForecastExportJobResponseTypeDef](./type_defs.md#createforecastexportjobresponsetypedef)
- [CreateForecastResponseTypeDef](./type_defs.md#createforecastresponsetypedef)
- [CreatePredictorBacktestExportJobResponseTypeDef](./type_defs.md#createpredictorbacktestexportjobresponsetypedef)
- [CreatePredictorResponseTypeDef](./type_defs.md#createpredictorresponsetypedef)
- [DataDestinationTypeDef](./type_defs.md#datadestinationtypedef)
- [DataSourceTypeDef](./type_defs.md#datasourcetypedef)
- [DatasetGroupSummaryTypeDef](./type_defs.md#datasetgroupsummarytypedef)
- [DatasetImportJobSummaryTypeDef](./type_defs.md#datasetimportjobsummarytypedef)
- [DatasetSummaryTypeDef](./type_defs.md#datasetsummarytypedef)
- [DescribeDatasetGroupResponseTypeDef](./type_defs.md#describedatasetgroupresponsetypedef)
- [DescribeDatasetImportJobResponseTypeDef](./type_defs.md#describedatasetimportjobresponsetypedef)
- [DescribeDatasetResponseTypeDef](./type_defs.md#describedatasetresponsetypedef)
- [DescribeForecastExportJobResponseTypeDef](./type_defs.md#describeforecastexportjobresponsetypedef)
- [DescribeForecastResponseTypeDef](./type_defs.md#describeforecastresponsetypedef)
- [DescribePredictorBacktestExportJobResponseTypeDef](./type_defs.md#describepredictorbacktestexportjobresponsetypedef)
- [DescribePredictorResponseTypeDef](./type_defs.md#describepredictorresponsetypedef)
- [EncryptionConfigTypeDef](./type_defs.md#encryptionconfigtypedef)
- [ErrorMetricTypeDef](./type_defs.md#errormetrictypedef)
- [EvaluationParametersTypeDef](./type_defs.md#evaluationparameterstypedef)
- [EvaluationResultTypeDef](./type_defs.md#evaluationresulttypedef)
- [FeaturizationConfigTypeDef](./type_defs.md#featurizationconfigtypedef)
- [FeaturizationMethodTypeDef](./type_defs.md#featurizationmethodtypedef)
- [FeaturizationTypeDef](./type_defs.md#featurizationtypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [ForecastExportJobSummaryTypeDef](./type_defs.md#forecastexportjobsummarytypedef)
- [ForecastSummaryTypeDef](./type_defs.md#forecastsummarytypedef)
- [GetAccuracyMetricsResponseTypeDef](./type_defs.md#getaccuracymetricsresponsetypedef)
- [HyperParameterTuningJobConfigTypeDef](./type_defs.md#hyperparametertuningjobconfigtypedef)
- [InputDataConfigTypeDef](./type_defs.md#inputdataconfigtypedef)
- [IntegerParameterRangeTypeDef](./type_defs.md#integerparameterrangetypedef)
- [ListDatasetGroupsResponseTypeDef](./type_defs.md#listdatasetgroupsresponsetypedef)
- [ListDatasetImportJobsResponseTypeDef](./type_defs.md#listdatasetimportjobsresponsetypedef)
- [ListDatasetsResponseTypeDef](./type_defs.md#listdatasetsresponsetypedef)
- [ListForecastExportJobsResponseTypeDef](./type_defs.md#listforecastexportjobsresponsetypedef)
- [ListForecastsResponseTypeDef](./type_defs.md#listforecastsresponsetypedef)
- [ListPredictorBacktestExportJobsResponseTypeDef](./type_defs.md#listpredictorbacktestexportjobsresponsetypedef)
- [ListPredictorsResponseTypeDef](./type_defs.md#listpredictorsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MetricsTypeDef](./type_defs.md#metricstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterRangesTypeDef](./type_defs.md#parameterrangestypedef)
- [PredictorBacktestExportJobSummaryTypeDef](./type_defs.md#predictorbacktestexportjobsummarytypedef)
- [PredictorExecutionDetailsTypeDef](./type_defs.md#predictorexecutiondetailstypedef)
- [PredictorExecutionTypeDef](./type_defs.md#predictorexecutiontypedef)
- [PredictorSummaryTypeDef](./type_defs.md#predictorsummarytypedef)
- [S3ConfigTypeDef](./type_defs.md#s3configtypedef)
- [SchemaAttributeTypeDef](./type_defs.md#schemaattributetypedef)
- [SchemaTypeDef](./type_defs.md#schematypedef)
- [StatisticsTypeDef](./type_defs.md#statisticstypedef)
- [SupplementaryFeatureTypeDef](./type_defs.md#supplementaryfeaturetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TestWindowSummaryTypeDef](./type_defs.md#testwindowsummarytypedef)
- [WeightedQuantileLossTypeDef](./type_defs.md#weightedquantilelosstypedef)
- [WindowSummaryTypeDef](./type_defs.md#windowsummarytypedef)
