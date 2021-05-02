# Type annotations for boto3 MachineLearning module

> [Index](../index.md) > MachineLearning

Auto-generated documentation for [MachineLearning](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning)
type annotations stubs module [mypy_boto3_machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/).

```bash
pip install mypy-boto3-machinelearning
```

- [Type annotations for boto3 MachineLearning module](#type-annotations-for-boto3-machinelearning-module)
  - [MachineLearningClient](#machinelearningclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## MachineLearningClient

Type annotations for  `boto3.client("machinelearning")` as [MachineLearningClient](./client.md)

Can be used directly:

```python
from mypy_boto3_machinelearning.client import MachineLearningClient
```


MachineLearningClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags](./client.md#add-tags)
- [can_paginate](./client.md#can-paginate)
- [create_batch_prediction](./client.md#create-batch-prediction)
- [create_data_source_from_rds](./client.md#create-data-source-from-rds)
- [create_data_source_from_redshift](./client.md#create-data-source-from-redshift)
- [create_data_source_from_s3](./client.md#create-data-source-from-s3)
- [create_evaluation](./client.md#create-evaluation)
- [create_ml_model](./client.md#create-ml-model)
- [create_realtime_endpoint](./client.md#create-realtime-endpoint)
- [delete_batch_prediction](./client.md#delete-batch-prediction)
- [delete_data_source](./client.md#delete-data-source)
- [delete_evaluation](./client.md#delete-evaluation)
- [delete_ml_model](./client.md#delete-ml-model)
- [delete_realtime_endpoint](./client.md#delete-realtime-endpoint)
- [delete_tags](./client.md#delete-tags)
- [describe_batch_predictions](./client.md#describe-batch-predictions)
- [describe_data_sources](./client.md#describe-data-sources)
- [describe_evaluations](./client.md#describe-evaluations)
- [describe_ml_models](./client.md#describe-ml-models)
- [describe_tags](./client.md#describe-tags)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_batch_prediction](./client.md#get-batch-prediction)
- [get_data_source](./client.md#get-data-source)
- [get_evaluation](./client.md#get-evaluation)
- [get_ml_model](./client.md#get-ml-model)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [predict](./client.md#predict)
- [update_batch_prediction](./client.md#update-batch-prediction)
- [update_data_source](./client.md#update-data-source)
- [update_evaluation](./client.md#update-evaluation)
- [update_ml_model](./client.md#update-ml-model)




### Exceptions
- [ClientError](./client.md#clienterror)
- [IdempotentParameterMismatchException](./client.md#idempotentparametermismatchexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [InvalidTagException](./client.md#invalidtagexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [PredictorNotMountedException](./client.md#predictornotmountedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TagLimitExceededException](./client.md#taglimitexceededexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("machinelearning").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.paginators import DescribeBatchPredictionsPaginator, ...
```

- [DescribeBatchPredictionsPaginator](./paginators.md#describebatchpredictionspaginator)
- [DescribeDataSourcesPaginator](./paginators.md#describedatasourcespaginator)
- [DescribeEvaluationsPaginator](./paginators.md#describeevaluationspaginator)
- [DescribeMLModelsPaginator](./paginators.md#describemlmodelspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("machinelearning").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.waiters import BatchPredictionAvailableWaiter, ...
```

- [BatchPredictionAvailableWaiter](./waiters.md#batchpredictionavailablewaiter)
- [DataSourceAvailableWaiter](./waiters.md#datasourceavailablewaiter)
- [EvaluationAvailableWaiter](./waiters.md#evaluationavailablewaiter)
- [MLModelAvailableWaiter](./waiters.md#mlmodelavailablewaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_machinelearning.literals import Algorithm, ...
```

- [Algorithm](./literals.md#algorithm)
- [BatchPredictionAvailableWaiterName](./literals.md#batchpredictionavailablewaitername)
- [BatchPredictionFilterVariable](./literals.md#batchpredictionfiltervariable)
- [DataSourceAvailableWaiterName](./literals.md#datasourceavailablewaitername)
- [DataSourceFilterVariable](./literals.md#datasourcefiltervariable)
- [DescribeBatchPredictionsPaginatorName](./literals.md#describebatchpredictionspaginatorname)
- [DescribeDataSourcesPaginatorName](./literals.md#describedatasourcespaginatorname)
- [DescribeEvaluationsPaginatorName](./literals.md#describeevaluationspaginatorname)
- [DescribeMLModelsPaginatorName](./literals.md#describemlmodelspaginatorname)
- [DetailsAttributes](./literals.md#detailsattributes)
- [EntityStatus](./literals.md#entitystatus)
- [EvaluationAvailableWaiterName](./literals.md#evaluationavailablewaitername)
- [EvaluationFilterVariable](./literals.md#evaluationfiltervariable)
- [MLModelAvailableWaiterName](./literals.md#mlmodelavailablewaitername)
- [MLModelFilterVariable](./literals.md#mlmodelfiltervariable)
- [MLModelType](./literals.md#mlmodeltype)
- [RealtimeEndpointStatus](./literals.md#realtimeendpointstatus)
- [SortOrder](./literals.md#sortorder)
- [TaggableResourceType](./literals.md#taggableresourcetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_machinelearning.type_defs import BatchPredictionTypeDef, ...
```

- [BatchPredictionTypeDef](./type_defs.md#batchpredictiontypedef)
- [DataSourceTypeDef](./type_defs.md#datasourcetypedef)
- [EvaluationTypeDef](./type_defs.md#evaluationtypedef)
- [MLModelTypeDef](./type_defs.md#mlmodeltypedef)
- [PerformanceMetricsTypeDef](./type_defs.md#performancemetricstypedef)
- [PredictionTypeDef](./type_defs.md#predictiontypedef)
- [RDSDatabaseCredentialsTypeDef](./type_defs.md#rdsdatabasecredentialstypedef)
- [RDSDatabaseTypeDef](./type_defs.md#rdsdatabasetypedef)
- [RDSMetadataTypeDef](./type_defs.md#rdsmetadatatypedef)
- [RealtimeEndpointInfoTypeDef](./type_defs.md#realtimeendpointinfotypedef)
- [RedshiftDatabaseCredentialsTypeDef](./type_defs.md#redshiftdatabasecredentialstypedef)
- [RedshiftDatabaseTypeDef](./type_defs.md#redshiftdatabasetypedef)
- [RedshiftMetadataTypeDef](./type_defs.md#redshiftmetadatatypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [AddTagsOutputTypeDef](./type_defs.md#addtagsoutputtypedef)
- [CreateBatchPredictionOutputTypeDef](./type_defs.md#createbatchpredictionoutputtypedef)
- [CreateDataSourceFromRDSOutputTypeDef](./type_defs.md#createdatasourcefromrdsoutputtypedef)
- [CreateDataSourceFromRedshiftOutputTypeDef](./type_defs.md#createdatasourcefromredshiftoutputtypedef)
- [CreateDataSourceFromS3OutputTypeDef](./type_defs.md#createdatasourcefroms3outputtypedef)
- [CreateEvaluationOutputTypeDef](./type_defs.md#createevaluationoutputtypedef)
- [CreateMLModelOutputTypeDef](./type_defs.md#createmlmodeloutputtypedef)
- [CreateRealtimeEndpointOutputTypeDef](./type_defs.md#createrealtimeendpointoutputtypedef)
- [DeleteBatchPredictionOutputTypeDef](./type_defs.md#deletebatchpredictionoutputtypedef)
- [DeleteDataSourceOutputTypeDef](./type_defs.md#deletedatasourceoutputtypedef)
- [DeleteEvaluationOutputTypeDef](./type_defs.md#deleteevaluationoutputtypedef)
- [DeleteMLModelOutputTypeDef](./type_defs.md#deletemlmodeloutputtypedef)
- [DeleteRealtimeEndpointOutputTypeDef](./type_defs.md#deleterealtimeendpointoutputtypedef)
- [DeleteTagsOutputTypeDef](./type_defs.md#deletetagsoutputtypedef)
- [DescribeBatchPredictionsOutputTypeDef](./type_defs.md#describebatchpredictionsoutputtypedef)
- [DescribeDataSourcesOutputTypeDef](./type_defs.md#describedatasourcesoutputtypedef)
- [DescribeEvaluationsOutputTypeDef](./type_defs.md#describeevaluationsoutputtypedef)
- [DescribeMLModelsOutputTypeDef](./type_defs.md#describemlmodelsoutputtypedef)
- [DescribeTagsOutputTypeDef](./type_defs.md#describetagsoutputtypedef)
- [GetBatchPredictionOutputTypeDef](./type_defs.md#getbatchpredictionoutputtypedef)
- [GetDataSourceOutputTypeDef](./type_defs.md#getdatasourceoutputtypedef)
- [GetEvaluationOutputTypeDef](./type_defs.md#getevaluationoutputtypedef)
- [GetMLModelOutputTypeDef](./type_defs.md#getmlmodeloutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PredictOutputTypeDef](./type_defs.md#predictoutputtypedef)
- [RDSDataSpecTypeDef](./type_defs.md#rdsdataspectypedef)
- [RedshiftDataSpecTypeDef](./type_defs.md#redshiftdataspectypedef)
- [S3DataSpecTypeDef](./type_defs.md#s3dataspectypedef)
- [UpdateBatchPredictionOutputTypeDef](./type_defs.md#updatebatchpredictionoutputtypedef)
- [UpdateDataSourceOutputTypeDef](./type_defs.md#updatedatasourceoutputtypedef)
- [UpdateEvaluationOutputTypeDef](./type_defs.md#updateevaluationoutputtypedef)
- [UpdateMLModelOutputTypeDef](./type_defs.md#updatemlmodeloutputtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
