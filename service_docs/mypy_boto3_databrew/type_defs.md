# Structures for boto3 GlueDataBrew module

> [Index](../index.md) > [GlueDataBrew](./index.md) > Structures

Auto-generated documentation for [GlueDataBrew](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew)
type annotations stubs module [mypy_boto3_databrew](https://pypi.org/project/mypy-boto3-databrew/).

- [Structures for boto3 GlueDataBrew module](#structures-for-boto3-gluedatabrew-module)
  - [BatchDeleteRecipeVersionResponseTypeDef](#batchdeleterecipeversionresponsetypedef)
  - [ConditionExpressionTypeDef](#conditionexpressiontypedef)
  - [CreateDatasetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateProfileJobResponseTypeDef](#createprofilejobresponsetypedef)
  - [CreateProjectResponseTypeDef](#createprojectresponsetypedef)
  - [CreateRecipeJobResponseTypeDef](#createrecipejobresponsetypedef)
  - [CreateRecipeResponseTypeDef](#createreciperesponsetypedef)
  - [CreateScheduleResponseTypeDef](#createscheduleresponsetypedef)
  - [CsvOptionsTypeDef](#csvoptionstypedef)
  - [CsvOutputOptionsTypeDef](#csvoutputoptionstypedef)
  - [DataCatalogInputDefinitionTypeDef](#datacataloginputdefinitiontypedef)
  - [DatabaseInputDefinitionTypeDef](#databaseinputdefinitiontypedef)
  - [DatasetParameterTypeDef](#datasetparametertypedef)
  - [DatasetTypeDef](#datasettypedef)
  - [DatetimeOptionsTypeDef](#datetimeoptionstypedef)
  - [DeleteDatasetResponseTypeDef](#deletedatasetresponsetypedef)
  - [DeleteJobResponseTypeDef](#deletejobresponsetypedef)
  - [DeleteProjectResponseTypeDef](#deleteprojectresponsetypedef)
  - [DeleteRecipeVersionResponseTypeDef](#deleterecipeversionresponsetypedef)
  - [DeleteScheduleResponseTypeDef](#deletescheduleresponsetypedef)
  - [DescribeDatasetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeJobResponseTypeDef](#describejobresponsetypedef)
  - [DescribeJobRunResponseTypeDef](#describejobrunresponsetypedef)
  - [DescribeProjectResponseTypeDef](#describeprojectresponsetypedef)
  - [DescribeRecipeResponseTypeDef](#describereciperesponsetypedef)
  - [DescribeScheduleResponseTypeDef](#describescheduleresponsetypedef)
  - [ExcelOptionsTypeDef](#exceloptionstypedef)
  - [FilesLimitTypeDef](#fileslimittypedef)
  - [FilterExpressionTypeDef](#filterexpressiontypedef)
  - [FormatOptionsTypeDef](#formatoptionstypedef)
  - [InputTypeDef](#inputtypedef)
  - [JobRunTypeDef](#jobruntypedef)
  - [JobSampleTypeDef](#jobsampletypedef)
  - [JobTypeDef](#jobtypedef)
  - [JsonOptionsTypeDef](#jsonoptionstypedef)
  - [ListDatasetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListJobRunsResponseTypeDef](#listjobrunsresponsetypedef)
  - [ListJobsResponseTypeDef](#listjobsresponsetypedef)
  - [ListProjectsResponseTypeDef](#listprojectsresponsetypedef)
  - [ListRecipeVersionsResponseTypeDef](#listrecipeversionsresponsetypedef)
  - [ListRecipesResponseTypeDef](#listrecipesresponsetypedef)
  - [ListSchedulesResponseTypeDef](#listschedulesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [OutputFormatOptionsTypeDef](#outputformatoptionstypedef)
  - [OutputTypeDef](#outputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PathOptionsTypeDef](#pathoptionstypedef)
  - [ProjectTypeDef](#projecttypedef)
  - [PublishRecipeResponseTypeDef](#publishreciperesponsetypedef)
  - [RecipeActionTypeDef](#recipeactiontypedef)
  - [RecipeReferenceTypeDef](#recipereferencetypedef)
  - [RecipeStepTypeDef](#recipesteptypedef)
  - [RecipeTypeDef](#recipetypedef)
  - [RecipeVersionErrorDetailTypeDef](#recipeversionerrordetailtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [SampleTypeDef](#sampletypedef)
  - [ScheduleTypeDef](#scheduletypedef)
  - [SendProjectSessionActionResponseTypeDef](#sendprojectsessionactionresponsetypedef)
  - [StartJobRunResponseTypeDef](#startjobrunresponsetypedef)
  - [StartProjectSessionResponseTypeDef](#startprojectsessionresponsetypedef)
  - [StopJobRunResponseTypeDef](#stopjobrunresponsetypedef)
  - [UpdateDatasetResponseTypeDef](#updatedatasetresponsetypedef)
  - [UpdateProfileJobResponseTypeDef](#updateprofilejobresponsetypedef)
  - [UpdateProjectResponseTypeDef](#updateprojectresponsetypedef)
  - [UpdateRecipeJobResponseTypeDef](#updaterecipejobresponsetypedef)
  - [UpdateRecipeResponseTypeDef](#updatereciperesponsetypedef)
  - [UpdateScheduleResponseTypeDef](#updatescheduleresponsetypedef)
  - [ViewFrameTypeDef](#viewframetypedef)

## BatchDeleteRecipeVersionResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import BatchDeleteRecipeVersionResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Errors`: `List["RecipeVersionErrorDetailTypeDef"]`


## ConditionExpressionTypeDef

```python
from mypy_boto3_databrew.type_defs import ConditionExpressionTypeDef
```


Required fields:
- `Condition`: `str`
- `TargetColumn`: `str`



Optional fields:
- `Value`: `str`


## CreateDatasetResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import CreateDatasetResponseTypeDef
```


Required fields:
- `Name`: `str`




## CreateProfileJobResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import CreateProfileJobResponseTypeDef
```


Required fields:
- `Name`: `str`




## CreateProjectResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import CreateProjectResponseTypeDef
```


Required fields:
- `Name`: `str`




## CreateRecipeJobResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import CreateRecipeJobResponseTypeDef
```


Required fields:
- `Name`: `str`




## CreateRecipeResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import CreateRecipeResponseTypeDef
```


Required fields:
- `Name`: `str`




## CreateScheduleResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import CreateScheduleResponseTypeDef
```


Required fields:
- `Name`: `str`




## CsvOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import CsvOptionsTypeDef
```




Optional fields:
- `Delimiter`: `str`
- `HeaderRow`: `bool`


## CsvOutputOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import CsvOutputOptionsTypeDef
```




Optional fields:
- `Delimiter`: `str`


## DataCatalogInputDefinitionTypeDef

```python
from mypy_boto3_databrew.type_defs import DataCatalogInputDefinitionTypeDef
```


Required fields:
- `DatabaseName`: `str`
- `TableName`: `str`



Optional fields:
- `CatalogId`: `str`
- `TempDirectory`: `"S3LocationTypeDef"`


## DatabaseInputDefinitionTypeDef

```python
from mypy_boto3_databrew.type_defs import DatabaseInputDefinitionTypeDef
```


Required fields:
- `GlueConnectionName`: `str`
- `DatabaseTableName`: `str`



Optional fields:
- `TempDirectory`: `"S3LocationTypeDef"`


## DatasetParameterTypeDef

```python
from mypy_boto3_databrew.type_defs import DatasetParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `ParameterType`



Optional fields:
- `DatetimeOptions`: `"DatetimeOptionsTypeDef"`
- `CreateColumn`: `bool`
- `Filter`: `"FilterExpressionTypeDef"`


## DatasetTypeDef

```python
from mypy_boto3_databrew.type_defs import DatasetTypeDef
```


Required fields:
- `Name`: `str`
- `Input`: `"InputTypeDef"`



Optional fields:
- `AccountId`: `str`
- `CreatedBy`: `str`
- `CreateDate`: `datetime`
- `Format`: `InputFormat`
- `FormatOptions`: `"FormatOptionsTypeDef"`
- `LastModifiedDate`: `datetime`
- `LastModifiedBy`: `str`
- `Source`: `Source`
- `PathOptions`: `"PathOptionsTypeDef"`
- `Tags`: `Dict[str, str]`
- `ResourceArn`: `str`


## DatetimeOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import DatetimeOptionsTypeDef
```


Required fields:
- `Format`: `str`



Optional fields:
- `TimezoneOffset`: `str`
- `LocaleCode`: `str`


## DeleteDatasetResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DeleteDatasetResponseTypeDef
```


Required fields:
- `Name`: `str`




## DeleteJobResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DeleteJobResponseTypeDef
```


Required fields:
- `Name`: `str`




## DeleteProjectResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DeleteProjectResponseTypeDef
```


Required fields:
- `Name`: `str`




## DeleteRecipeVersionResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DeleteRecipeVersionResponseTypeDef
```


Required fields:
- `Name`: `str`
- `RecipeVersion`: `str`




## DeleteScheduleResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DeleteScheduleResponseTypeDef
```


Required fields:
- `Name`: `str`




## DescribeDatasetResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DescribeDatasetResponseTypeDef
```


Required fields:
- `Name`: `str`
- `Input`: `"InputTypeDef"`



Optional fields:
- `CreatedBy`: `str`
- `CreateDate`: `datetime`
- `Format`: `InputFormat`
- `FormatOptions`: `"FormatOptionsTypeDef"`
- `LastModifiedDate`: `datetime`
- `LastModifiedBy`: `str`
- `Source`: `Source`
- `PathOptions`: `"PathOptionsTypeDef"`
- `Tags`: `Dict[str, str]`
- `ResourceArn`: `str`


## DescribeJobResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DescribeJobResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CreateDate`: `datetime`
- `CreatedBy`: `str`
- `DatasetName`: `str`
- `EncryptionKeyArn`: `str`
- `EncryptionMode`: `EncryptionMode`
- `Type`: `JobType`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `datetime`
- `LogSubscription`: `LogSubscription`
- `MaxCapacity`: `int`
- `MaxRetries`: `int`
- `Outputs`: `List["OutputTypeDef"]`
- `ProjectName`: `str`
- `RecipeReference`: `"RecipeReferenceTypeDef"`
- `ResourceArn`: `str`
- `RoleArn`: `str`
- `Tags`: `Dict[str, str]`
- `Timeout`: `int`
- `JobSample`: `"JobSampleTypeDef"`


## DescribeJobRunResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DescribeJobRunResponseTypeDef
```


Required fields:
- `JobName`: `str`



Optional fields:
- `Attempt`: `int`
- `CompletedOn`: `datetime`
- `DatasetName`: `str`
- `ErrorMessage`: `str`
- `ExecutionTime`: `int`
- `RunId`: `str`
- `State`: `JobRunState`
- `LogSubscription`: `LogSubscription`
- `LogGroupName`: `str`
- `Outputs`: `List["OutputTypeDef"]`
- `RecipeReference`: `"RecipeReferenceTypeDef"`
- `StartedBy`: `str`
- `StartedOn`: `datetime`
- `JobSample`: `"JobSampleTypeDef"`


## DescribeProjectResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DescribeProjectResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CreateDate`: `datetime`
- `CreatedBy`: `str`
- `DatasetName`: `str`
- `LastModifiedDate`: `datetime`
- `LastModifiedBy`: `str`
- `RecipeName`: `str`
- `ResourceArn`: `str`
- `Sample`: `"SampleTypeDef"`
- `RoleArn`: `str`
- `Tags`: `Dict[str, str]`
- `SessionStatus`: `SessionStatus`
- `OpenedBy`: `str`
- `OpenDate`: `datetime`


## DescribeRecipeResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DescribeRecipeResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CreatedBy`: `str`
- `CreateDate`: `datetime`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `datetime`
- `ProjectName`: `str`
- `PublishedBy`: `str`
- `PublishedDate`: `datetime`
- `Description`: `str`
- `Steps`: `List["RecipeStepTypeDef"]`
- `Tags`: `Dict[str, str]`
- `ResourceArn`: `str`
- `RecipeVersion`: `str`


## DescribeScheduleResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import DescribeScheduleResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CreateDate`: `datetime`
- `CreatedBy`: `str`
- `JobNames`: `List[str]`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `datetime`
- `ResourceArn`: `str`
- `CronExpression`: `str`
- `Tags`: `Dict[str, str]`


## ExcelOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import ExcelOptionsTypeDef
```




Optional fields:
- `SheetNames`: `List[str]`
- `SheetIndexes`: `List[int]`
- `HeaderRow`: `bool`


## FilesLimitTypeDef

```python
from mypy_boto3_databrew.type_defs import FilesLimitTypeDef
```


Required fields:
- `MaxFiles`: `int`



Optional fields:
- `OrderedBy`: `Literal['LAST_MODIFIED_DATE']`
- `Order`: `Order`


## FilterExpressionTypeDef

```python
from mypy_boto3_databrew.type_defs import FilterExpressionTypeDef
```


Required fields:
- `Expression`: `str`
- `ValuesMap`: `Dict[str, str]`




## FormatOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import FormatOptionsTypeDef
```




Optional fields:
- `Json`: `"JsonOptionsTypeDef"`
- `Excel`: `"ExcelOptionsTypeDef"`
- `Csv`: `"CsvOptionsTypeDef"`


## InputTypeDef

```python
from mypy_boto3_databrew.type_defs import InputTypeDef
```




Optional fields:
- `S3InputDefinition`: `"S3LocationTypeDef"`
- `DataCatalogInputDefinition`: `"DataCatalogInputDefinitionTypeDef"`
- `DatabaseInputDefinition`: `"DatabaseInputDefinitionTypeDef"`


## JobRunTypeDef

```python
from mypy_boto3_databrew.type_defs import JobRunTypeDef
```




Optional fields:
- `Attempt`: `int`
- `CompletedOn`: `datetime`
- `DatasetName`: `str`
- `ErrorMessage`: `str`
- `ExecutionTime`: `int`
- `JobName`: `str`
- `RunId`: `str`
- `State`: `JobRunState`
- `LogSubscription`: `LogSubscription`
- `LogGroupName`: `str`
- `Outputs`: `List["OutputTypeDef"]`
- `RecipeReference`: `"RecipeReferenceTypeDef"`
- `StartedBy`: `str`
- `StartedOn`: `datetime`
- `JobSample`: `"JobSampleTypeDef"`


## JobSampleTypeDef

```python
from mypy_boto3_databrew.type_defs import JobSampleTypeDef
```




Optional fields:
- `Mode`: `SampleMode`
- `Size`: `int`


## JobTypeDef

```python
from mypy_boto3_databrew.type_defs import JobTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `AccountId`: `str`
- `CreatedBy`: `str`
- `CreateDate`: `datetime`
- `DatasetName`: `str`
- `EncryptionKeyArn`: `str`
- `EncryptionMode`: `EncryptionMode`
- `Type`: `JobType`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `datetime`
- `LogSubscription`: `LogSubscription`
- `MaxCapacity`: `int`
- `MaxRetries`: `int`
- `Outputs`: `List["OutputTypeDef"]`
- `ProjectName`: `str`
- `RecipeReference`: `"RecipeReferenceTypeDef"`
- `ResourceArn`: `str`
- `RoleArn`: `str`
- `Timeout`: `int`
- `Tags`: `Dict[str, str]`
- `JobSample`: `"JobSampleTypeDef"`


## JsonOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import JsonOptionsTypeDef
```




Optional fields:
- `MultiLine`: `bool`


## ListDatasetsResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListDatasetsResponseTypeDef
```


Required fields:
- `Datasets`: `List["DatasetTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListJobRunsResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListJobRunsResponseTypeDef
```


Required fields:
- `JobRuns`: `List["JobRunTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListJobsResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListJobsResponseTypeDef
```


Required fields:
- `Jobs`: `List["JobTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListProjectsResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListProjectsResponseTypeDef
```


Required fields:
- `Projects`: `List["ProjectTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListRecipeVersionsResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListRecipeVersionsResponseTypeDef
```


Required fields:
- `Recipes`: `List["RecipeTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListRecipesResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListRecipesResponseTypeDef
```


Required fields:
- `Recipes`: `List["RecipeTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListSchedulesResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListSchedulesResponseTypeDef
```


Required fields:
- `Schedules`: `List["ScheduleTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## OutputFormatOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import OutputFormatOptionsTypeDef
```




Optional fields:
- `Csv`: `"CsvOutputOptionsTypeDef"`


## OutputTypeDef

```python
from mypy_boto3_databrew.type_defs import OutputTypeDef
```


Required fields:
- `Location`: `"S3LocationTypeDef"`



Optional fields:
- `CompressionFormat`: `CompressionFormat`
- `Format`: `OutputFormat`
- `PartitionColumns`: `List[str]`
- `Overwrite`: `bool`
- `FormatOptions`: `"OutputFormatOptionsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_databrew.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PathOptionsTypeDef

```python
from mypy_boto3_databrew.type_defs import PathOptionsTypeDef
```




Optional fields:
- `LastModifiedDateCondition`: `"FilterExpressionTypeDef"`
- `FilesLimit`: `"FilesLimitTypeDef"`
- `Parameters`: `Dict[str, "DatasetParameterTypeDef"]`


## ProjectTypeDef

```python
from mypy_boto3_databrew.type_defs import ProjectTypeDef
```


Required fields:
- `Name`: `str`
- `RecipeName`: `str`



Optional fields:
- `AccountId`: `str`
- `CreateDate`: `datetime`
- `CreatedBy`: `str`
- `DatasetName`: `str`
- `LastModifiedDate`: `datetime`
- `LastModifiedBy`: `str`
- `ResourceArn`: `str`
- `Sample`: `"SampleTypeDef"`
- `Tags`: `Dict[str, str]`
- `RoleArn`: `str`
- `OpenedBy`: `str`
- `OpenDate`: `datetime`


## PublishRecipeResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import PublishRecipeResponseTypeDef
```


Required fields:
- `Name`: `str`




## RecipeActionTypeDef

```python
from mypy_boto3_databrew.type_defs import RecipeActionTypeDef
```


Required fields:
- `Operation`: `str`



Optional fields:
- `Parameters`: `Dict[str, str]`


## RecipeReferenceTypeDef

```python
from mypy_boto3_databrew.type_defs import RecipeReferenceTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `RecipeVersion`: `str`


## RecipeStepTypeDef

```python
from mypy_boto3_databrew.type_defs import RecipeStepTypeDef
```


Required fields:
- `Action`: `"RecipeActionTypeDef"`



Optional fields:
- `ConditionExpressions`: `List["ConditionExpressionTypeDef"]`


## RecipeTypeDef

```python
from mypy_boto3_databrew.type_defs import RecipeTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `CreatedBy`: `str`
- `CreateDate`: `datetime`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `datetime`
- `ProjectName`: `str`
- `PublishedBy`: `str`
- `PublishedDate`: `datetime`
- `Description`: `str`
- `ResourceArn`: `str`
- `Steps`: `List["RecipeStepTypeDef"]`
- `Tags`: `Dict[str, str]`
- `RecipeVersion`: `str`


## RecipeVersionErrorDetailTypeDef

```python
from mypy_boto3_databrew.type_defs import RecipeVersionErrorDetailTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `ErrorMessage`: `str`
- `RecipeVersion`: `str`


## ResponseMetadata

```python
from mypy_boto3_databrew.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3LocationTypeDef

```python
from mypy_boto3_databrew.type_defs import S3LocationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Key`: `str`


## SampleTypeDef

```python
from mypy_boto3_databrew.type_defs import SampleTypeDef
```


Required fields:
- `Type`: `SampleType`



Optional fields:
- `Size`: `int`


## ScheduleTypeDef

```python
from mypy_boto3_databrew.type_defs import ScheduleTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `AccountId`: `str`
- `CreatedBy`: `str`
- `CreateDate`: `datetime`
- `JobNames`: `List[str]`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `datetime`
- `ResourceArn`: `str`
- `CronExpression`: `str`
- `Tags`: `Dict[str, str]`


## SendProjectSessionActionResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import SendProjectSessionActionResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Result`: `str`
- `ActionId`: `int`


## StartJobRunResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import StartJobRunResponseTypeDef
```


Required fields:
- `RunId`: `str`




## StartProjectSessionResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import StartProjectSessionResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `ClientSessionId`: `str`


## StopJobRunResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import StopJobRunResponseTypeDef
```


Required fields:
- `RunId`: `str`




## UpdateDatasetResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import UpdateDatasetResponseTypeDef
```


Required fields:
- `Name`: `str`




## UpdateProfileJobResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import UpdateProfileJobResponseTypeDef
```


Required fields:
- `Name`: `str`




## UpdateProjectResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import UpdateProjectResponseTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `LastModifiedDate`: `datetime`


## UpdateRecipeJobResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import UpdateRecipeJobResponseTypeDef
```


Required fields:
- `Name`: `str`




## UpdateRecipeResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import UpdateRecipeResponseTypeDef
```


Required fields:
- `Name`: `str`




## UpdateScheduleResponseTypeDef

```python
from mypy_boto3_databrew.type_defs import UpdateScheduleResponseTypeDef
```


Required fields:
- `Name`: `str`




## ViewFrameTypeDef

```python
from mypy_boto3_databrew.type_defs import ViewFrameTypeDef
```


Required fields:
- `StartColumnIndex`: `int`



Optional fields:
- `ColumnRange`: `int`
- `HiddenColumns`: `List[str]`

