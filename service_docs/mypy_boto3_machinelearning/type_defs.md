# Structures for boto3 MachineLearning module

> [Index](../index.md) > [MachineLearning](./index.md) > Structures

Auto-generated documentation for [MachineLearning](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning)
type annotations stubs module [mypy_boto3_machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/).

- [Structures for boto3 MachineLearning module](#structures-for-boto3-machinelearning-module)
  - [BatchPredictionTypeDef](#batchpredictiontypedef)
  - [DataSourceTypeDef](#datasourcetypedef)
  - [EvaluationTypeDef](#evaluationtypedef)
  - [MLModelTypeDef](#mlmodeltypedef)
  - [PerformanceMetricsTypeDef](#performancemetricstypedef)
  - [PredictionTypeDef](#predictiontypedef)
  - [RDSDatabaseCredentialsTypeDef](#rdsdatabasecredentialstypedef)
  - [RDSDatabaseTypeDef](#rdsdatabasetypedef)
  - [RDSMetadataTypeDef](#rdsmetadatatypedef)
  - [RealtimeEndpointInfoTypeDef](#realtimeendpointinfotypedef)
  - [RedshiftDatabaseCredentialsTypeDef](#redshiftdatabasecredentialstypedef)
  - [RedshiftDatabaseTypeDef](#redshiftdatabasetypedef)
  - [RedshiftMetadataTypeDef](#redshiftmetadatatypedef)
  - [ResponseMetadata](#responsemetadata)
  - [TagTypeDef](#tagtypedef)
  - [AddTagsOutputTypeDef](#addtagsoutputtypedef)
  - [CreateBatchPredictionOutputTypeDef](#createbatchpredictionoutputtypedef)
  - [CreateDataSourceFromRDSOutputTypeDef](#createdatasourcefromrdsoutputtypedef)
  - [CreateDataSourceFromRedshiftOutputTypeDef](#createdatasourcefromredshiftoutputtypedef)
  - [CreateDataSourceFromS3OutputTypeDef](#createdatasourcefroms3outputtypedef)
  - [CreateEvaluationOutputTypeDef](#createevaluationoutputtypedef)
  - [CreateMLModelOutputTypeDef](#createmlmodeloutputtypedef)
  - [CreateRealtimeEndpointOutputTypeDef](#createrealtimeendpointoutputtypedef)
  - [DeleteBatchPredictionOutputTypeDef](#deletebatchpredictionoutputtypedef)
  - [DeleteDataSourceOutputTypeDef](#deletedatasourceoutputtypedef)
  - [DeleteEvaluationOutputTypeDef](#deleteevaluationoutputtypedef)
  - [DeleteMLModelOutputTypeDef](#deletemlmodeloutputtypedef)
  - [DeleteRealtimeEndpointOutputTypeDef](#deleterealtimeendpointoutputtypedef)
  - [DeleteTagsOutputTypeDef](#deletetagsoutputtypedef)
  - [DescribeBatchPredictionsOutputTypeDef](#describebatchpredictionsoutputtypedef)
  - [DescribeDataSourcesOutputTypeDef](#describedatasourcesoutputtypedef)
  - [DescribeEvaluationsOutputTypeDef](#describeevaluationsoutputtypedef)
  - [DescribeMLModelsOutputTypeDef](#describemlmodelsoutputtypedef)
  - [DescribeTagsOutputTypeDef](#describetagsoutputtypedef)
  - [GetBatchPredictionOutputTypeDef](#getbatchpredictionoutputtypedef)
  - [GetDataSourceOutputTypeDef](#getdatasourceoutputtypedef)
  - [GetEvaluationOutputTypeDef](#getevaluationoutputtypedef)
  - [GetMLModelOutputTypeDef](#getmlmodeloutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PredictOutputTypeDef](#predictoutputtypedef)
  - [RDSDataSpecTypeDef](#rdsdataspectypedef)
  - [RedshiftDataSpecTypeDef](#redshiftdataspectypedef)
  - [S3DataSpecTypeDef](#s3dataspectypedef)
  - [UpdateBatchPredictionOutputTypeDef](#updatebatchpredictionoutputtypedef)
  - [UpdateDataSourceOutputTypeDef](#updatedatasourceoutputtypedef)
  - [UpdateEvaluationOutputTypeDef](#updateevaluationoutputtypedef)
  - [UpdateMLModelOutputTypeDef](#updatemlmodeloutputtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## BatchPredictionTypeDef

```python
from mypy_boto3_machinelearning.type_defs import BatchPredictionTypeDef
```




Optional fields:
- `BatchPredictionId`: `str`
- `MLModelId`: `str`
- `BatchPredictionDataSourceId`: `str`
- `InputDataLocationS3`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Name`: `str`
- `Status`: `EntityStatus`
- `OutputUri`: `str`
- `Message`: `str`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`
- `TotalRecordCount`: `int`
- `InvalidRecordCount`: `int`


## DataSourceTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DataSourceTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `DataLocationS3`: `str`
- `DataRearrangement`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `DataSizeInBytes`: `int`
- `NumberOfFiles`: `int`
- `Name`: `str`
- `Status`: `EntityStatus`
- `Message`: `str`
- `RedshiftMetadata`: `"RedshiftMetadataTypeDef"`
- `RDSMetadata`: `"RDSMetadataTypeDef"`
- `RoleARN`: `str`
- `ComputeStatistics`: `bool`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`


## EvaluationTypeDef

```python
from mypy_boto3_machinelearning.type_defs import EvaluationTypeDef
```




Optional fields:
- `EvaluationId`: `str`
- `MLModelId`: `str`
- `EvaluationDataSourceId`: `str`
- `InputDataLocationS3`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Name`: `str`
- `Status`: `EntityStatus`
- `PerformanceMetrics`: `"PerformanceMetricsTypeDef"`
- `Message`: `str`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`


## MLModelTypeDef

```python
from mypy_boto3_machinelearning.type_defs import MLModelTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `TrainingDataSourceId`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Name`: `str`
- `Status`: `EntityStatus`
- `SizeInBytes`: `int`
- `EndpointInfo`: `"RealtimeEndpointInfoTypeDef"`
- `TrainingParameters`: `Dict[str, str]`
- `InputDataLocationS3`: `str`
- `Algorithm`: `Algorithm`
- `MLModelType`: `MLModelType`
- `ScoreThreshold`: `float`
- `ScoreThresholdLastUpdatedAt`: `datetime`
- `Message`: `str`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`


## PerformanceMetricsTypeDef

```python
from mypy_boto3_machinelearning.type_defs import PerformanceMetricsTypeDef
```




Optional fields:
- `Properties`: `Dict[str, str]`


## PredictionTypeDef

```python
from mypy_boto3_machinelearning.type_defs import PredictionTypeDef
```




Optional fields:
- `predictedLabel`: `str`
- `predictedValue`: `float`
- `predictedScores`: `Dict[str, float]`
- `details`: `Dict[DetailsAttributes, str]`


## RDSDatabaseCredentialsTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RDSDatabaseCredentialsTypeDef
```


Required fields:
- `Username`: `str`
- `Password`: `str`




## RDSDatabaseTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RDSDatabaseTypeDef
```


Required fields:
- `InstanceIdentifier`: `str`
- `DatabaseName`: `str`




## RDSMetadataTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RDSMetadataTypeDef
```




Optional fields:
- `Database`: `"RDSDatabaseTypeDef"`
- `DatabaseUserName`: `str`
- `SelectSqlQuery`: `str`
- `ResourceRole`: `str`
- `ServiceRole`: `str`
- `DataPipelineId`: `str`


## RealtimeEndpointInfoTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RealtimeEndpointInfoTypeDef
```




Optional fields:
- `PeakRequestsPerSecond`: `int`
- `CreatedAt`: `datetime`
- `EndpointUrl`: `str`
- `EndpointStatus`: `RealtimeEndpointStatus`


## RedshiftDatabaseCredentialsTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RedshiftDatabaseCredentialsTypeDef
```


Required fields:
- `Username`: `str`
- `Password`: `str`




## RedshiftDatabaseTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RedshiftDatabaseTypeDef
```


Required fields:
- `DatabaseName`: `str`
- `ClusterIdentifier`: `str`




## RedshiftMetadataTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RedshiftMetadataTypeDef
```




Optional fields:
- `RedshiftDatabase`: `"RedshiftDatabaseTypeDef"`
- `DatabaseUserName`: `str`
- `SelectSqlQuery`: `str`


## ResponseMetadata

```python
from mypy_boto3_machinelearning.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## TagTypeDef

```python
from mypy_boto3_machinelearning.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## AddTagsOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import AddTagsOutputTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ResourceType`: `TaggableResourceType`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateBatchPredictionOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateBatchPredictionOutputTypeDef
```




Optional fields:
- `BatchPredictionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDataSourceFromRDSOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateDataSourceFromRDSOutputTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDataSourceFromRedshiftOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateDataSourceFromRedshiftOutputTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDataSourceFromS3OutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateDataSourceFromS3OutputTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateEvaluationOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateEvaluationOutputTypeDef
```




Optional fields:
- `EvaluationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateMLModelOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateMLModelOutputTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateRealtimeEndpointOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import CreateRealtimeEndpointOutputTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `RealtimeEndpointInfo`: `"RealtimeEndpointInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteBatchPredictionOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DeleteBatchPredictionOutputTypeDef
```




Optional fields:
- `BatchPredictionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteDataSourceOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DeleteDataSourceOutputTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteEvaluationOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DeleteEvaluationOutputTypeDef
```




Optional fields:
- `EvaluationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteMLModelOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DeleteMLModelOutputTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteRealtimeEndpointOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DeleteRealtimeEndpointOutputTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `RealtimeEndpointInfo`: `"RealtimeEndpointInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteTagsOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DeleteTagsOutputTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ResourceType`: `TaggableResourceType`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeBatchPredictionsOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DescribeBatchPredictionsOutputTypeDef
```




Optional fields:
- `Results`: `List["BatchPredictionTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeDataSourcesOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DescribeDataSourcesOutputTypeDef
```




Optional fields:
- `Results`: `List["DataSourceTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeEvaluationsOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DescribeEvaluationsOutputTypeDef
```




Optional fields:
- `Results`: `List["EvaluationTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMLModelsOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DescribeMLModelsOutputTypeDef
```




Optional fields:
- `Results`: `List["MLModelTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTagsOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import DescribeTagsOutputTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `ResourceType`: `TaggableResourceType`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBatchPredictionOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import GetBatchPredictionOutputTypeDef
```




Optional fields:
- `BatchPredictionId`: `str`
- `MLModelId`: `str`
- `BatchPredictionDataSourceId`: `str`
- `InputDataLocationS3`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Name`: `str`
- `Status`: `EntityStatus`
- `OutputUri`: `str`
- `LogUri`: `str`
- `Message`: `str`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`
- `TotalRecordCount`: `int`
- `InvalidRecordCount`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDataSourceOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import GetDataSourceOutputTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `DataLocationS3`: `str`
- `DataRearrangement`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `DataSizeInBytes`: `int`
- `NumberOfFiles`: `int`
- `Name`: `str`
- `Status`: `EntityStatus`
- `LogUri`: `str`
- `Message`: `str`
- `RedshiftMetadata`: `"RedshiftMetadataTypeDef"`
- `RDSMetadata`: `"RDSMetadataTypeDef"`
- `RoleARN`: `str`
- `ComputeStatistics`: `bool`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`
- `DataSourceSchema`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetEvaluationOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import GetEvaluationOutputTypeDef
```




Optional fields:
- `EvaluationId`: `str`
- `MLModelId`: `str`
- `EvaluationDataSourceId`: `str`
- `InputDataLocationS3`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Name`: `str`
- `Status`: `EntityStatus`
- `PerformanceMetrics`: `"PerformanceMetricsTypeDef"`
- `LogUri`: `str`
- `Message`: `str`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMLModelOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import GetMLModelOutputTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `TrainingDataSourceId`: `str`
- `CreatedByIamUser`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Name`: `str`
- `Status`: `EntityStatus`
- `SizeInBytes`: `int`
- `EndpointInfo`: `"RealtimeEndpointInfoTypeDef"`
- `TrainingParameters`: `Dict[str, str]`
- `InputDataLocationS3`: `str`
- `MLModelType`: `MLModelType`
- `ScoreThreshold`: `float`
- `ScoreThresholdLastUpdatedAt`: `datetime`
- `LogUri`: `str`
- `Message`: `str`
- `ComputeTime`: `int`
- `FinishedAt`: `datetime`
- `StartedAt`: `datetime`
- `Recipe`: `str`
- `Schema`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_machinelearning.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PredictOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import PredictOutputTypeDef
```




Optional fields:
- `Prediction`: `"PredictionTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## RDSDataSpecTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RDSDataSpecTypeDef
```


Required fields:
- `DatabaseInformation`: `"RDSDatabaseTypeDef"`
- `SelectSqlQuery`: `str`
- `DatabaseCredentials`: `"RDSDatabaseCredentialsTypeDef"`
- `S3StagingLocation`: `str`
- `ResourceRole`: `str`
- `ServiceRole`: `str`
- `SubnetId`: `str`
- `SecurityGroupIds`: `List[str]`



Optional fields:
- `DataRearrangement`: `str`
- `DataSchema`: `str`
- `DataSchemaUri`: `str`


## RedshiftDataSpecTypeDef

```python
from mypy_boto3_machinelearning.type_defs import RedshiftDataSpecTypeDef
```


Required fields:
- `DatabaseInformation`: `"RedshiftDatabaseTypeDef"`
- `SelectSqlQuery`: `str`
- `DatabaseCredentials`: `"RedshiftDatabaseCredentialsTypeDef"`
- `S3StagingLocation`: `str`



Optional fields:
- `DataRearrangement`: `str`
- `DataSchema`: `str`
- `DataSchemaUri`: `str`


## S3DataSpecTypeDef

```python
from mypy_boto3_machinelearning.type_defs import S3DataSpecTypeDef
```


Required fields:
- `DataLocationS3`: `str`



Optional fields:
- `DataRearrangement`: `str`
- `DataSchema`: `str`
- `DataSchemaLocationS3`: `str`


## UpdateBatchPredictionOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import UpdateBatchPredictionOutputTypeDef
```




Optional fields:
- `BatchPredictionId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateDataSourceOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import UpdateDataSourceOutputTypeDef
```




Optional fields:
- `DataSourceId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateEvaluationOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import UpdateEvaluationOutputTypeDef
```




Optional fields:
- `EvaluationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateMLModelOutputTypeDef

```python
from mypy_boto3_machinelearning.type_defs import UpdateMLModelOutputTypeDef
```




Optional fields:
- `MLModelId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## WaiterConfigTypeDef

```python
from mypy_boto3_machinelearning.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

