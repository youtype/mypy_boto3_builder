# Structures for boto3 LookoutforVision module

> [Index](../index.md) > [LookoutforVision](./index.md) > Structures

Auto-generated documentation for [LookoutforVision](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision)
type annotations stubs module [mypy_boto3_lookoutvision](https://pypi.org/project/mypy-boto3-lookoutvision/).

- [Structures for boto3 LookoutforVision module](#structures-for-boto3-lookoutforvision-module)
  - [DatasetDescriptionTypeDef](#datasetdescriptiontypedef)
  - [DatasetGroundTruthManifestTypeDef](#datasetgroundtruthmanifesttypedef)
  - [DatasetImageStatsTypeDef](#datasetimagestatstypedef)
  - [DatasetMetadataTypeDef](#datasetmetadatatypedef)
  - [DetectAnomalyResultTypeDef](#detectanomalyresulttypedef)
  - [ImageSourceTypeDef](#imagesourcetypedef)
  - [InputS3ObjectTypeDef](#inputs3objecttypedef)
  - [ModelDescriptionTypeDef](#modeldescriptiontypedef)
  - [ModelMetadataTypeDef](#modelmetadatatypedef)
  - [ModelPerformanceTypeDef](#modelperformancetypedef)
  - [OutputConfigTypeDef](#outputconfigtypedef)
  - [OutputS3ObjectTypeDef](#outputs3objecttypedef)
  - [ProjectDescriptionTypeDef](#projectdescriptiontypedef)
  - [ProjectMetadataTypeDef](#projectmetadatatypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [TagTypeDef](#tagtypedef)
  - [CreateDatasetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateModelResponseTypeDef](#createmodelresponsetypedef)
  - [CreateProjectResponseTypeDef](#createprojectresponsetypedef)
  - [DatasetSourceTypeDef](#datasetsourcetypedef)
  - [DeleteModelResponseTypeDef](#deletemodelresponsetypedef)
  - [DeleteProjectResponseTypeDef](#deleteprojectresponsetypedef)
  - [DescribeDatasetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeModelResponseTypeDef](#describemodelresponsetypedef)
  - [DescribeProjectResponseTypeDef](#describeprojectresponsetypedef)
  - [DetectAnomaliesResponseTypeDef](#detectanomaliesresponsetypedef)
  - [ListDatasetEntriesResponseTypeDef](#listdatasetentriesresponsetypedef)
  - [ListModelsResponseTypeDef](#listmodelsresponsetypedef)
  - [ListProjectsResponseTypeDef](#listprojectsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [StartModelResponseTypeDef](#startmodelresponsetypedef)
  - [StopModelResponseTypeDef](#stopmodelresponsetypedef)
  - [UpdateDatasetEntriesResponseTypeDef](#updatedatasetentriesresponsetypedef)

## DatasetDescriptionTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DatasetDescriptionTypeDef
```




Optional fields:
- `ProjectName`: `str`
- `DatasetType`: `str`
- `CreationTimestamp`: `datetime`
- `LastUpdatedTimestamp`: `datetime`
- `Status`: `DatasetStatus`
- `StatusMessage`: `str`
- `ImageStats`: `"DatasetImageStatsTypeDef"`


## DatasetGroundTruthManifestTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DatasetGroundTruthManifestTypeDef
```




Optional fields:
- `S3Object`: `"InputS3ObjectTypeDef"`


## DatasetImageStatsTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DatasetImageStatsTypeDef
```




Optional fields:
- `Total`: `int`
- `Labeled`: `int`
- `Normal`: `int`
- `Anomaly`: `int`


## DatasetMetadataTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DatasetMetadataTypeDef
```




Optional fields:
- `DatasetType`: `str`
- `CreationTimestamp`: `datetime`
- `Status`: `DatasetStatus`
- `StatusMessage`: `str`


## DetectAnomalyResultTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DetectAnomalyResultTypeDef
```




Optional fields:
- `Source`: `"ImageSourceTypeDef"`
- `IsAnomalous`: `bool`
- `Confidence`: `float`


## ImageSourceTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ImageSourceTypeDef
```




Optional fields:
- `Type`: `str`


## InputS3ObjectTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import InputS3ObjectTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`



Optional fields:
- `VersionId`: `str`


## ModelDescriptionTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ModelDescriptionTypeDef
```




Optional fields:
- `ModelVersion`: `str`
- `ModelArn`: `str`
- `CreationTimestamp`: `datetime`
- `Description`: `str`
- `Status`: `ModelStatus`
- `StatusMessage`: `str`
- `Performance`: `"ModelPerformanceTypeDef"`
- `OutputConfig`: `"OutputConfigTypeDef"`
- `EvaluationManifest`: `"OutputS3ObjectTypeDef"`
- `EvaluationResult`: `"OutputS3ObjectTypeDef"`
- `EvaluationEndTimestamp`: `datetime`
- `KmsKeyId`: `str`


## ModelMetadataTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ModelMetadataTypeDef
```




Optional fields:
- `CreationTimestamp`: `datetime`
- `ModelVersion`: `str`
- `ModelArn`: `str`
- `Description`: `str`
- `Status`: `ModelStatus`
- `StatusMessage`: `str`
- `Performance`: `"ModelPerformanceTypeDef"`


## ModelPerformanceTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ModelPerformanceTypeDef
```




Optional fields:
- `F1Score`: `float`
- `Recall`: `float`
- `Precision`: `float`


## OutputConfigTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import OutputConfigTypeDef
```


Required fields:
- `S3Location`: `"S3LocationTypeDef"`




## OutputS3ObjectTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import OutputS3ObjectTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`




## ProjectDescriptionTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ProjectDescriptionTypeDef
```




Optional fields:
- `ProjectArn`: `str`
- `ProjectName`: `str`
- `CreationTimestamp`: `datetime`
- `Datasets`: `List["DatasetMetadataTypeDef"]`


## ProjectMetadataTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ProjectMetadataTypeDef
```




Optional fields:
- `ProjectArn`: `str`
- `ProjectName`: `str`
- `CreationTimestamp`: `datetime`


## S3LocationTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import S3LocationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Prefix`: `str`


## TagTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## CreateDatasetResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import CreateDatasetResponseTypeDef
```




Optional fields:
- `DatasetMetadata`: `"DatasetMetadataTypeDef"`


## CreateModelResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import CreateModelResponseTypeDef
```




Optional fields:
- `ModelMetadata`: `"ModelMetadataTypeDef"`


## CreateProjectResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import CreateProjectResponseTypeDef
```




Optional fields:
- `ProjectMetadata`: `"ProjectMetadataTypeDef"`


## DatasetSourceTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DatasetSourceTypeDef
```




Optional fields:
- `GroundTruthManifest`: `"DatasetGroundTruthManifestTypeDef"`


## DeleteModelResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DeleteModelResponseTypeDef
```




Optional fields:
- `ModelArn`: `str`


## DeleteProjectResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DeleteProjectResponseTypeDef
```




Optional fields:
- `ProjectArn`: `str`


## DescribeDatasetResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DescribeDatasetResponseTypeDef
```




Optional fields:
- `DatasetDescription`: `"DatasetDescriptionTypeDef"`


## DescribeModelResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DescribeModelResponseTypeDef
```




Optional fields:
- `ModelDescription`: `"ModelDescriptionTypeDef"`


## DescribeProjectResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DescribeProjectResponseTypeDef
```




Optional fields:
- `ProjectDescription`: `"ProjectDescriptionTypeDef"`


## DetectAnomaliesResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import DetectAnomaliesResponseTypeDef
```




Optional fields:
- `DetectAnomalyResult`: `"DetectAnomalyResultTypeDef"`


## ListDatasetEntriesResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ListDatasetEntriesResponseTypeDef
```




Optional fields:
- `DatasetEntries`: `List[str]`
- `NextToken`: `str`


## ListModelsResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ListModelsResponseTypeDef
```




Optional fields:
- `Models`: `List["ModelMetadataTypeDef"]`
- `NextToken`: `str`


## ListProjectsResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ListProjectsResponseTypeDef
```




Optional fields:
- `Projects`: `List["ProjectMetadataTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## StartModelResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import StartModelResponseTypeDef
```




Optional fields:
- `Status`: `ModelHostingStatus`


## StopModelResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import StopModelResponseTypeDef
```




Optional fields:
- `Status`: `ModelHostingStatus`


## UpdateDatasetEntriesResponseTypeDef

```python
from mypy_boto3_lookoutvision.type_defs import UpdateDatasetEntriesResponseTypeDef
```




Optional fields:
- `Status`: `DatasetStatus`

