# Structures for boto3 Textract module

> [Index](../index.md) > [Textract](./index.md) > Structures

Auto-generated documentation for [Textract](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract)
type annotations stubs module [mypy_boto3_textract](https://pypi.org/project/mypy-boto3-textract/).

- [Structures for boto3 Textract module](#structures-for-boto3-textract-module)
  - [AnalyzeDocumentResponseTypeDef](#analyzedocumentresponsetypedef)
  - [BlockTypeDef](#blocktypedef)
  - [BoundingBoxTypeDef](#boundingboxtypedef)
  - [DetectDocumentTextResponseTypeDef](#detectdocumenttextresponsetypedef)
  - [DocumentLocationTypeDef](#documentlocationtypedef)
  - [DocumentMetadataTypeDef](#documentmetadatatypedef)
  - [DocumentTypeDef](#documenttypedef)
  - [GeometryTypeDef](#geometrytypedef)
  - [GetDocumentAnalysisResponseTypeDef](#getdocumentanalysisresponsetypedef)
  - [GetDocumentTextDetectionResponseTypeDef](#getdocumenttextdetectionresponsetypedef)
  - [HumanLoopActivationOutputTypeDef](#humanloopactivationoutputtypedef)
  - [HumanLoopConfigTypeDef](#humanloopconfigtypedef)
  - [HumanLoopDataAttributesTypeDef](#humanloopdataattributestypedef)
  - [NotificationChannelTypeDef](#notificationchanneltypedef)
  - [OutputConfigTypeDef](#outputconfigtypedef)
  - [PointTypeDef](#pointtypedef)
  - [RelationshipTypeDef](#relationshiptypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3ObjectTypeDef](#s3objecttypedef)
  - [StartDocumentAnalysisResponseTypeDef](#startdocumentanalysisresponsetypedef)
  - [StartDocumentTextDetectionResponseTypeDef](#startdocumenttextdetectionresponsetypedef)
  - [WarningTypeDef](#warningtypedef)

## AnalyzeDocumentResponseTypeDef

```python
from mypy_boto3_textract.type_defs import AnalyzeDocumentResponseTypeDef
```




Optional fields:
- `DocumentMetadata`: `"DocumentMetadataTypeDef"`
- `Blocks`: `List["BlockTypeDef"]`
- `HumanLoopActivationOutput`: `"HumanLoopActivationOutputTypeDef"`
- `AnalyzeDocumentModelVersion`: `str`


## BlockTypeDef

```python
from mypy_boto3_textract.type_defs import BlockTypeDef
```




Optional fields:
- `BlockType`: `BlockType`
- `Confidence`: `float`
- `Text`: `str`
- `TextType`: `TextType`
- `RowIndex`: `int`
- `ColumnIndex`: `int`
- `RowSpan`: `int`
- `ColumnSpan`: `int`
- `Geometry`: `"GeometryTypeDef"`
- `Id`: `str`
- `Relationships`: `List["RelationshipTypeDef"]`
- `EntityTypes`: `List[EntityType]`
- `SelectionStatus`: `SelectionStatus`
- `Page`: `int`


## BoundingBoxTypeDef

```python
from mypy_boto3_textract.type_defs import BoundingBoxTypeDef
```




Optional fields:
- `Width`: `float`
- `Height`: `float`
- `Left`: `float`
- `Top`: `float`


## DetectDocumentTextResponseTypeDef

```python
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef
```




Optional fields:
- `DocumentMetadata`: `"DocumentMetadataTypeDef"`
- `Blocks`: `List["BlockTypeDef"]`
- `DetectDocumentTextModelVersion`: `str`


## DocumentLocationTypeDef

```python
from mypy_boto3_textract.type_defs import DocumentLocationTypeDef
```




Optional fields:
- `S3Object`: `"S3ObjectTypeDef"`


## DocumentMetadataTypeDef

```python
from mypy_boto3_textract.type_defs import DocumentMetadataTypeDef
```




Optional fields:
- `Pages`: `int`


## DocumentTypeDef

```python
from mypy_boto3_textract.type_defs import DocumentTypeDef
```




Optional fields:
- `Bytes`: `Union[bytes, IO[bytes]]`
- `S3Object`: `"S3ObjectTypeDef"`


## GeometryTypeDef

```python
from mypy_boto3_textract.type_defs import GeometryTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Polygon`: `List["PointTypeDef"]`


## GetDocumentAnalysisResponseTypeDef

```python
from mypy_boto3_textract.type_defs import GetDocumentAnalysisResponseTypeDef
```




Optional fields:
- `DocumentMetadata`: `"DocumentMetadataTypeDef"`
- `JobStatus`: `JobStatus`
- `NextToken`: `str`
- `Blocks`: `List["BlockTypeDef"]`
- `Warnings`: `List["WarningTypeDef"]`
- `StatusMessage`: `str`
- `AnalyzeDocumentModelVersion`: `str`


## GetDocumentTextDetectionResponseTypeDef

```python
from mypy_boto3_textract.type_defs import GetDocumentTextDetectionResponseTypeDef
```




Optional fields:
- `DocumentMetadata`: `"DocumentMetadataTypeDef"`
- `JobStatus`: `JobStatus`
- `NextToken`: `str`
- `Blocks`: `List["BlockTypeDef"]`
- `Warnings`: `List["WarningTypeDef"]`
- `StatusMessage`: `str`
- `DetectDocumentTextModelVersion`: `str`


## HumanLoopActivationOutputTypeDef

```python
from mypy_boto3_textract.type_defs import HumanLoopActivationOutputTypeDef
```




Optional fields:
- `HumanLoopArn`: `str`
- `HumanLoopActivationReasons`: `List[str]`
- `HumanLoopActivationConditionsEvaluationResults`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## HumanLoopConfigTypeDef

```python
from mypy_boto3_textract.type_defs import HumanLoopConfigTypeDef
```


Required fields:
- `HumanLoopName`: `str`
- `FlowDefinitionArn`: `str`



Optional fields:
- `DataAttributes`: `"HumanLoopDataAttributesTypeDef"`


## HumanLoopDataAttributesTypeDef

```python
from mypy_boto3_textract.type_defs import HumanLoopDataAttributesTypeDef
```




Optional fields:
- `ContentClassifiers`: `List[ContentClassifier]`


## NotificationChannelTypeDef

```python
from mypy_boto3_textract.type_defs import NotificationChannelTypeDef
```


Required fields:
- `SNSTopicArn`: `str`
- `RoleArn`: `str`




## OutputConfigTypeDef

```python
from mypy_boto3_textract.type_defs import OutputConfigTypeDef
```


Required fields:
- `S3Bucket`: `str`



Optional fields:
- `S3Prefix`: `str`


## PointTypeDef

```python
from mypy_boto3_textract.type_defs import PointTypeDef
```




Optional fields:
- `X`: `float`
- `Y`: `float`


## RelationshipTypeDef

```python
from mypy_boto3_textract.type_defs import RelationshipTypeDef
```




Optional fields:
- `Type`: `RelationshipType`
- `Ids`: `List[str]`


## ResponseMetadata

```python
from mypy_boto3_textract.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3ObjectTypeDef

```python
from mypy_boto3_textract.type_defs import S3ObjectTypeDef
```




Optional fields:
- `Bucket`: `str`
- `Name`: `str`
- `Version`: `str`


## StartDocumentAnalysisResponseTypeDef

```python
from mypy_boto3_textract.type_defs import StartDocumentAnalysisResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartDocumentTextDetectionResponseTypeDef

```python
from mypy_boto3_textract.type_defs import StartDocumentTextDetectionResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## WarningTypeDef

```python
from mypy_boto3_textract.type_defs import WarningTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `Pages`: `List[int]`

