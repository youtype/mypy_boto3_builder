# Structures for boto3 Rekognition module

> [Index](../index.md) > [Rekognition](./index.md) > Structures

Auto-generated documentation for [Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition)
type annotations stubs module [mypy_boto3_rekognition](https://pypi.org/project/mypy-boto3-rekognition/).

- [Structures for boto3 Rekognition module](#structures-for-boto3-rekognition-module)
  - [AgeRangeTypeDef](#agerangetypedef)
  - [AssetTypeDef](#assettypedef)
  - [AudioMetadataTypeDef](#audiometadatatypedef)
  - [BeardTypeDef](#beardtypedef)
  - [BoundingBoxTypeDef](#boundingboxtypedef)
  - [CelebrityDetailTypeDef](#celebritydetailtypedef)
  - [CelebrityRecognitionTypeDef](#celebrityrecognitiontypedef)
  - [CelebrityTypeDef](#celebritytypedef)
  - [CompareFacesMatchTypeDef](#comparefacesmatchtypedef)
  - [ComparedFaceTypeDef](#comparedfacetypedef)
  - [ComparedSourceImageFaceTypeDef](#comparedsourceimagefacetypedef)
  - [ContentModerationDetectionTypeDef](#contentmoderationdetectiontypedef)
  - [CoversBodyPartTypeDef](#coversbodyparttypedef)
  - [CustomLabelTypeDef](#customlabeltypedef)
  - [DetectionFilterTypeDef](#detectionfiltertypedef)
  - [EmotionTypeDef](#emotiontypedef)
  - [EquipmentDetectionTypeDef](#equipmentdetectiontypedef)
  - [EvaluationResultTypeDef](#evaluationresulttypedef)
  - [EyeOpenTypeDef](#eyeopentypedef)
  - [EyeglassesTypeDef](#eyeglassestypedef)
  - [FaceDetailTypeDef](#facedetailtypedef)
  - [FaceDetectionTypeDef](#facedetectiontypedef)
  - [FaceMatchTypeDef](#facematchtypedef)
  - [FaceRecordTypeDef](#facerecordtypedef)
  - [FaceSearchSettingsTypeDef](#facesearchsettingstypedef)
  - [FaceTypeDef](#facetypedef)
  - [GenderTypeDef](#gendertypedef)
  - [GeometryTypeDef](#geometrytypedef)
  - [GroundTruthManifestTypeDef](#groundtruthmanifesttypedef)
  - [HumanLoopActivationOutputTypeDef](#humanloopactivationoutputtypedef)
  - [HumanLoopDataAttributesTypeDef](#humanloopdataattributestypedef)
  - [ImageQualityTypeDef](#imagequalitytypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [KinesisDataStreamTypeDef](#kinesisdatastreamtypedef)
  - [KinesisVideoStreamTypeDef](#kinesisvideostreamtypedef)
  - [LabelDetectionTypeDef](#labeldetectiontypedef)
  - [LabelTypeDef](#labeltypedef)
  - [LandmarkTypeDef](#landmarktypedef)
  - [ModerationLabelTypeDef](#moderationlabeltypedef)
  - [MouthOpenTypeDef](#mouthopentypedef)
  - [MustacheTypeDef](#mustachetypedef)
  - [OutputConfigTypeDef](#outputconfigtypedef)
  - [ParentTypeDef](#parenttypedef)
  - [PersonDetailTypeDef](#persondetailtypedef)
  - [PersonDetectionTypeDef](#persondetectiontypedef)
  - [PersonMatchTypeDef](#personmatchtypedef)
  - [PointTypeDef](#pointtypedef)
  - [PoseTypeDef](#posetypedef)
  - [ProjectDescriptionTypeDef](#projectdescriptiontypedef)
  - [ProjectVersionDescriptionTypeDef](#projectversiondescriptiontypedef)
  - [ProtectiveEquipmentBodyPartTypeDef](#protectiveequipmentbodyparttypedef)
  - [ProtectiveEquipmentPersonTypeDef](#protectiveequipmentpersontypedef)
  - [ProtectiveEquipmentSummaryTypeDef](#protectiveequipmentsummarytypedef)
  - [RegionOfInterestTypeDef](#regionofinteresttypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3ObjectTypeDef](#s3objecttypedef)
  - [SegmentDetectionTypeDef](#segmentdetectiontypedef)
  - [SegmentTypeInfoTypeDef](#segmenttypeinfotypedef)
  - [ShotSegmentTypeDef](#shotsegmenttypedef)
  - [SmileTypeDef](#smiletypedef)
  - [StartShotDetectionFilterTypeDef](#startshotdetectionfiltertypedef)
  - [StartTechnicalCueDetectionFilterTypeDef](#starttechnicalcuedetectionfiltertypedef)
  - [StreamProcessorInputTypeDef](#streamprocessorinputtypedef)
  - [StreamProcessorOutputTypeDef](#streamprocessoroutputtypedef)
  - [StreamProcessorSettingsTypeDef](#streamprocessorsettingstypedef)
  - [StreamProcessorTypeDef](#streamprocessortypedef)
  - [SummaryTypeDef](#summarytypedef)
  - [SunglassesTypeDef](#sunglassestypedef)
  - [TechnicalCueSegmentTypeDef](#technicalcuesegmenttypedef)
  - [TestingDataResultTypeDef](#testingdataresulttypedef)
  - [TestingDataTypeDef](#testingdatatypedef)
  - [TextDetectionResultTypeDef](#textdetectionresulttypedef)
  - [TextDetectionTypeDef](#textdetectiontypedef)
  - [TrainingDataResultTypeDef](#trainingdataresulttypedef)
  - [TrainingDataTypeDef](#trainingdatatypedef)
  - [UnindexedFaceTypeDef](#unindexedfacetypedef)
  - [ValidationDataTypeDef](#validationdatatypedef)
  - [VideoMetadataTypeDef](#videometadatatypedef)
  - [CompareFacesResponseTypeDef](#comparefacesresponsetypedef)
  - [CreateCollectionResponseTypeDef](#createcollectionresponsetypedef)
  - [CreateProjectResponseTypeDef](#createprojectresponsetypedef)
  - [CreateProjectVersionResponseTypeDef](#createprojectversionresponsetypedef)
  - [CreateStreamProcessorResponseTypeDef](#createstreamprocessorresponsetypedef)
  - [DeleteCollectionResponseTypeDef](#deletecollectionresponsetypedef)
  - [DeleteFacesResponseTypeDef](#deletefacesresponsetypedef)
  - [DeleteProjectResponseTypeDef](#deleteprojectresponsetypedef)
  - [DeleteProjectVersionResponseTypeDef](#deleteprojectversionresponsetypedef)
  - [DescribeCollectionResponseTypeDef](#describecollectionresponsetypedef)
  - [DescribeProjectVersionsResponseTypeDef](#describeprojectversionsresponsetypedef)
  - [DescribeProjectsResponseTypeDef](#describeprojectsresponsetypedef)
  - [DescribeStreamProcessorResponseTypeDef](#describestreamprocessorresponsetypedef)
  - [DetectCustomLabelsResponseTypeDef](#detectcustomlabelsresponsetypedef)
  - [DetectFacesResponseTypeDef](#detectfacesresponsetypedef)
  - [DetectLabelsResponseTypeDef](#detectlabelsresponsetypedef)
  - [DetectModerationLabelsResponseTypeDef](#detectmoderationlabelsresponsetypedef)
  - [DetectProtectiveEquipmentResponseTypeDef](#detectprotectiveequipmentresponsetypedef)
  - [DetectTextFiltersTypeDef](#detecttextfilterstypedef)
  - [DetectTextResponseTypeDef](#detecttextresponsetypedef)
  - [GetCelebrityInfoResponseTypeDef](#getcelebrityinforesponsetypedef)
  - [GetCelebrityRecognitionResponseTypeDef](#getcelebrityrecognitionresponsetypedef)
  - [GetContentModerationResponseTypeDef](#getcontentmoderationresponsetypedef)
  - [GetFaceDetectionResponseTypeDef](#getfacedetectionresponsetypedef)
  - [GetFaceSearchResponseTypeDef](#getfacesearchresponsetypedef)
  - [GetLabelDetectionResponseTypeDef](#getlabeldetectionresponsetypedef)
  - [GetPersonTrackingResponseTypeDef](#getpersontrackingresponsetypedef)
  - [GetSegmentDetectionResponseTypeDef](#getsegmentdetectionresponsetypedef)
  - [GetTextDetectionResponseTypeDef](#gettextdetectionresponsetypedef)
  - [HumanLoopConfigTypeDef](#humanloopconfigtypedef)
  - [ImageTypeDef](#imagetypedef)
  - [IndexFacesResponseTypeDef](#indexfacesresponsetypedef)
  - [ListCollectionsResponseTypeDef](#listcollectionsresponsetypedef)
  - [ListFacesResponseTypeDef](#listfacesresponsetypedef)
  - [ListStreamProcessorsResponseTypeDef](#liststreamprocessorsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [NotificationChannelTypeDef](#notificationchanneltypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProtectiveEquipmentSummarizationAttributesTypeDef](#protectiveequipmentsummarizationattributestypedef)
  - [RecognizeCelebritiesResponseTypeDef](#recognizecelebritiesresponsetypedef)
  - [SearchFacesByImageResponseTypeDef](#searchfacesbyimageresponsetypedef)
  - [SearchFacesResponseTypeDef](#searchfacesresponsetypedef)
  - [StartCelebrityRecognitionResponseTypeDef](#startcelebrityrecognitionresponsetypedef)
  - [StartContentModerationResponseTypeDef](#startcontentmoderationresponsetypedef)
  - [StartFaceDetectionResponseTypeDef](#startfacedetectionresponsetypedef)
  - [StartFaceSearchResponseTypeDef](#startfacesearchresponsetypedef)
  - [StartLabelDetectionResponseTypeDef](#startlabeldetectionresponsetypedef)
  - [StartPersonTrackingResponseTypeDef](#startpersontrackingresponsetypedef)
  - [StartProjectVersionResponseTypeDef](#startprojectversionresponsetypedef)
  - [StartSegmentDetectionFiltersTypeDef](#startsegmentdetectionfilterstypedef)
  - [StartSegmentDetectionResponseTypeDef](#startsegmentdetectionresponsetypedef)
  - [StartTextDetectionFiltersTypeDef](#starttextdetectionfilterstypedef)
  - [StartTextDetectionResponseTypeDef](#starttextdetectionresponsetypedef)
  - [StopProjectVersionResponseTypeDef](#stopprojectversionresponsetypedef)
  - [VideoTypeDef](#videotypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AgeRangeTypeDef

```python
from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef
```




Optional fields:
- `Low`: `int`
- `High`: `int`


## AssetTypeDef

```python
from mypy_boto3_rekognition.type_defs import AssetTypeDef
```




Optional fields:
- `GroundTruthManifest`: `"GroundTruthManifestTypeDef"`


## AudioMetadataTypeDef

```python
from mypy_boto3_rekognition.type_defs import AudioMetadataTypeDef
```




Optional fields:
- `Codec`: `str`
- `DurationMillis`: `int`
- `SampleRate`: `int`
- `NumberOfChannels`: `int`


## BeardTypeDef

```python
from mypy_boto3_rekognition.type_defs import BeardTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## BoundingBoxTypeDef

```python
from mypy_boto3_rekognition.type_defs import BoundingBoxTypeDef
```




Optional fields:
- `Width`: `float`
- `Height`: `float`
- `Left`: `float`
- `Top`: `float`


## CelebrityDetailTypeDef

```python
from mypy_boto3_rekognition.type_defs import CelebrityDetailTypeDef
```




Optional fields:
- `Urls`: `List[str]`
- `Name`: `str`
- `Id`: `str`
- `Confidence`: `float`
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Face`: `"FaceDetailTypeDef"`


## CelebrityRecognitionTypeDef

```python
from mypy_boto3_rekognition.type_defs import CelebrityRecognitionTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `Celebrity`: `"CelebrityDetailTypeDef"`


## CelebrityTypeDef

```python
from mypy_boto3_rekognition.type_defs import CelebrityTypeDef
```




Optional fields:
- `Urls`: `List[str]`
- `Name`: `str`
- `Id`: `str`
- `Face`: `"ComparedFaceTypeDef"`
- `MatchConfidence`: `float`


## CompareFacesMatchTypeDef

```python
from mypy_boto3_rekognition.type_defs import CompareFacesMatchTypeDef
```




Optional fields:
- `Similarity`: `float`
- `Face`: `"ComparedFaceTypeDef"`


## ComparedFaceTypeDef

```python
from mypy_boto3_rekognition.type_defs import ComparedFaceTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Confidence`: `float`
- `Landmarks`: `List["LandmarkTypeDef"]`
- `Pose`: `"PoseTypeDef"`
- `Quality`: `"ImageQualityTypeDef"`


## ComparedSourceImageFaceTypeDef

```python
from mypy_boto3_rekognition.type_defs import ComparedSourceImageFaceTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Confidence`: `float`


## ContentModerationDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import ContentModerationDetectionTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `ModerationLabel`: `"ModerationLabelTypeDef"`


## CoversBodyPartTypeDef

```python
from mypy_boto3_rekognition.type_defs import CoversBodyPartTypeDef
```




Optional fields:
- `Confidence`: `float`
- `Value`: `bool`


## CustomLabelTypeDef

```python
from mypy_boto3_rekognition.type_defs import CustomLabelTypeDef
```




Optional fields:
- `Name`: `str`
- `Confidence`: `float`
- `Geometry`: `"GeometryTypeDef"`


## DetectionFilterTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectionFilterTypeDef
```




Optional fields:
- `MinConfidence`: `float`
- `MinBoundingBoxHeight`: `float`
- `MinBoundingBoxWidth`: `float`


## EmotionTypeDef

```python
from mypy_boto3_rekognition.type_defs import EmotionTypeDef
```




Optional fields:
- `Type`: `EmotionName`
- `Confidence`: `float`


## EquipmentDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import EquipmentDetectionTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Confidence`: `float`
- `Type`: `ProtectiveEquipmentType`
- `CoversBodyPart`: `"CoversBodyPartTypeDef"`


## EvaluationResultTypeDef

```python
from mypy_boto3_rekognition.type_defs import EvaluationResultTypeDef
```




Optional fields:
- `F1Score`: `float`
- `Summary`: `"SummaryTypeDef"`


## EyeOpenTypeDef

```python
from mypy_boto3_rekognition.type_defs import EyeOpenTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## EyeglassesTypeDef

```python
from mypy_boto3_rekognition.type_defs import EyeglassesTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## FaceDetailTypeDef

```python
from mypy_boto3_rekognition.type_defs import FaceDetailTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `AgeRange`: `"AgeRangeTypeDef"`
- `Smile`: `"SmileTypeDef"`
- `Eyeglasses`: `"EyeglassesTypeDef"`
- `Sunglasses`: `"SunglassesTypeDef"`
- `Gender`: `"GenderTypeDef"`
- `Beard`: `"BeardTypeDef"`
- `Mustache`: `"MustacheTypeDef"`
- `EyesOpen`: `"EyeOpenTypeDef"`
- `MouthOpen`: `"MouthOpenTypeDef"`
- `Emotions`: `List["EmotionTypeDef"]`
- `Landmarks`: `List["LandmarkTypeDef"]`
- `Pose`: `"PoseTypeDef"`
- `Quality`: `"ImageQualityTypeDef"`
- `Confidence`: `float`


## FaceDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import FaceDetectionTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `Face`: `"FaceDetailTypeDef"`


## FaceMatchTypeDef

```python
from mypy_boto3_rekognition.type_defs import FaceMatchTypeDef
```




Optional fields:
- `Similarity`: `float`
- `Face`: `"FaceTypeDef"`


## FaceRecordTypeDef

```python
from mypy_boto3_rekognition.type_defs import FaceRecordTypeDef
```




Optional fields:
- `Face`: `"FaceTypeDef"`
- `FaceDetail`: `"FaceDetailTypeDef"`


## FaceSearchSettingsTypeDef

```python
from mypy_boto3_rekognition.type_defs import FaceSearchSettingsTypeDef
```




Optional fields:
- `CollectionId`: `str`
- `FaceMatchThreshold`: `float`


## FaceTypeDef

```python
from mypy_boto3_rekognition.type_defs import FaceTypeDef
```




Optional fields:
- `FaceId`: `str`
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `ImageId`: `str`
- `ExternalImageId`: `str`
- `Confidence`: `float`


## GenderTypeDef

```python
from mypy_boto3_rekognition.type_defs import GenderTypeDef
```




Optional fields:
- `Value`: `GenderType`
- `Confidence`: `float`


## GeometryTypeDef

```python
from mypy_boto3_rekognition.type_defs import GeometryTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Polygon`: `List["PointTypeDef"]`


## GroundTruthManifestTypeDef

```python
from mypy_boto3_rekognition.type_defs import GroundTruthManifestTypeDef
```




Optional fields:
- `S3Object`: `"S3ObjectTypeDef"`


## HumanLoopActivationOutputTypeDef

```python
from mypy_boto3_rekognition.type_defs import HumanLoopActivationOutputTypeDef
```




Optional fields:
- `HumanLoopArn`: `str`
- `HumanLoopActivationReasons`: `List[str]`
- `HumanLoopActivationConditionsEvaluationResults`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## HumanLoopDataAttributesTypeDef

```python
from mypy_boto3_rekognition.type_defs import HumanLoopDataAttributesTypeDef
```




Optional fields:
- `ContentClassifiers`: `List[ContentClassifier]`


## ImageQualityTypeDef

```python
from mypy_boto3_rekognition.type_defs import ImageQualityTypeDef
```




Optional fields:
- `Brightness`: `float`
- `Sharpness`: `float`


## InstanceTypeDef

```python
from mypy_boto3_rekognition.type_defs import InstanceTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Confidence`: `float`


## KinesisDataStreamTypeDef

```python
from mypy_boto3_rekognition.type_defs import KinesisDataStreamTypeDef
```




Optional fields:
- `Arn`: `str`


## KinesisVideoStreamTypeDef

```python
from mypy_boto3_rekognition.type_defs import KinesisVideoStreamTypeDef
```




Optional fields:
- `Arn`: `str`


## LabelDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import LabelDetectionTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `Label`: `"LabelTypeDef"`


## LabelTypeDef

```python
from mypy_boto3_rekognition.type_defs import LabelTypeDef
```




Optional fields:
- `Name`: `str`
- `Confidence`: `float`
- `Instances`: `List["InstanceTypeDef"]`
- `Parents`: `List["ParentTypeDef"]`


## LandmarkTypeDef

```python
from mypy_boto3_rekognition.type_defs import LandmarkTypeDef
```




Optional fields:
- `Type`: `LandmarkType`
- `X`: `float`
- `Y`: `float`


## ModerationLabelTypeDef

```python
from mypy_boto3_rekognition.type_defs import ModerationLabelTypeDef
```




Optional fields:
- `Confidence`: `float`
- `Name`: `str`
- `ParentName`: `str`


## MouthOpenTypeDef

```python
from mypy_boto3_rekognition.type_defs import MouthOpenTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## MustacheTypeDef

```python
from mypy_boto3_rekognition.type_defs import MustacheTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## OutputConfigTypeDef

```python
from mypy_boto3_rekognition.type_defs import OutputConfigTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3KeyPrefix`: `str`


## ParentTypeDef

```python
from mypy_boto3_rekognition.type_defs import ParentTypeDef
```




Optional fields:
- `Name`: `str`


## PersonDetailTypeDef

```python
from mypy_boto3_rekognition.type_defs import PersonDetailTypeDef
```




Optional fields:
- `Index`: `int`
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Face`: `"FaceDetailTypeDef"`


## PersonDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import PersonDetectionTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `Person`: `"PersonDetailTypeDef"`


## PersonMatchTypeDef

```python
from mypy_boto3_rekognition.type_defs import PersonMatchTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `Person`: `"PersonDetailTypeDef"`
- `FaceMatches`: `List["FaceMatchTypeDef"]`


## PointTypeDef

```python
from mypy_boto3_rekognition.type_defs import PointTypeDef
```




Optional fields:
- `X`: `float`
- `Y`: `float`


## PoseTypeDef

```python
from mypy_boto3_rekognition.type_defs import PoseTypeDef
```




Optional fields:
- `Roll`: `float`
- `Yaw`: `float`
- `Pitch`: `float`


## ProjectDescriptionTypeDef

```python
from mypy_boto3_rekognition.type_defs import ProjectDescriptionTypeDef
```




Optional fields:
- `ProjectArn`: `str`
- `CreationTimestamp`: `datetime`
- `Status`: `ProjectStatus`


## ProjectVersionDescriptionTypeDef

```python
from mypy_boto3_rekognition.type_defs import ProjectVersionDescriptionTypeDef
```




Optional fields:
- `ProjectVersionArn`: `str`
- `CreationTimestamp`: `datetime`
- `MinInferenceUnits`: `int`
- `Status`: `ProjectVersionStatus`
- `StatusMessage`: `str`
- `BillableTrainingTimeInSeconds`: `int`
- `TrainingEndTimestamp`: `datetime`
- `OutputConfig`: `"OutputConfigTypeDef"`
- `TrainingDataResult`: `"TrainingDataResultTypeDef"`
- `TestingDataResult`: `"TestingDataResultTypeDef"`
- `EvaluationResult`: `"EvaluationResultTypeDef"`
- `ManifestSummary`: `"GroundTruthManifestTypeDef"`


## ProtectiveEquipmentBodyPartTypeDef

```python
from mypy_boto3_rekognition.type_defs import ProtectiveEquipmentBodyPartTypeDef
```




Optional fields:
- `Name`: `BodyPart`
- `Confidence`: `float`
- `EquipmentDetections`: `List["EquipmentDetectionTypeDef"]`


## ProtectiveEquipmentPersonTypeDef

```python
from mypy_boto3_rekognition.type_defs import ProtectiveEquipmentPersonTypeDef
```




Optional fields:
- `BodyParts`: `List["ProtectiveEquipmentBodyPartTypeDef"]`
- `BoundingBox`: `"BoundingBoxTypeDef"`
- `Confidence`: `float`
- `Id`: `int`


## ProtectiveEquipmentSummaryTypeDef

```python
from mypy_boto3_rekognition.type_defs import ProtectiveEquipmentSummaryTypeDef
```




Optional fields:
- `PersonsWithRequiredEquipment`: `List[int]`
- `PersonsWithoutRequiredEquipment`: `List[int]`
- `PersonsIndeterminate`: `List[int]`


## RegionOfInterestTypeDef

```python
from mypy_boto3_rekognition.type_defs import RegionOfInterestTypeDef
```




Optional fields:
- `BoundingBox`: `"BoundingBoxTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_rekognition.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3ObjectTypeDef

```python
from mypy_boto3_rekognition.type_defs import S3ObjectTypeDef
```




Optional fields:
- `Bucket`: `str`
- `Name`: `str`
- `Version`: `str`


## SegmentDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import SegmentDetectionTypeDef
```




Optional fields:
- `Type`: `SegmentType`
- `StartTimestampMillis`: `int`
- `EndTimestampMillis`: `int`
- `DurationMillis`: `int`
- `StartTimecodeSMPTE`: `str`
- `EndTimecodeSMPTE`: `str`
- `DurationSMPTE`: `str`
- `TechnicalCueSegment`: `"TechnicalCueSegmentTypeDef"`
- `ShotSegment`: `"ShotSegmentTypeDef"`


## SegmentTypeInfoTypeDef

```python
from mypy_boto3_rekognition.type_defs import SegmentTypeInfoTypeDef
```




Optional fields:
- `Type`: `SegmentType`
- `ModelVersion`: `str`


## ShotSegmentTypeDef

```python
from mypy_boto3_rekognition.type_defs import ShotSegmentTypeDef
```




Optional fields:
- `Index`: `int`
- `Confidence`: `float`


## SmileTypeDef

```python
from mypy_boto3_rekognition.type_defs import SmileTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## StartShotDetectionFilterTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartShotDetectionFilterTypeDef
```




Optional fields:
- `MinSegmentConfidence`: `float`


## StartTechnicalCueDetectionFilterTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartTechnicalCueDetectionFilterTypeDef
```




Optional fields:
- `MinSegmentConfidence`: `float`


## StreamProcessorInputTypeDef

```python
from mypy_boto3_rekognition.type_defs import StreamProcessorInputTypeDef
```




Optional fields:
- `KinesisVideoStream`: `"KinesisVideoStreamTypeDef"`


## StreamProcessorOutputTypeDef

```python
from mypy_boto3_rekognition.type_defs import StreamProcessorOutputTypeDef
```




Optional fields:
- `KinesisDataStream`: `"KinesisDataStreamTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StreamProcessorSettingsTypeDef

```python
from mypy_boto3_rekognition.type_defs import StreamProcessorSettingsTypeDef
```




Optional fields:
- `FaceSearch`: `"FaceSearchSettingsTypeDef"`


## StreamProcessorTypeDef

```python
from mypy_boto3_rekognition.type_defs import StreamProcessorTypeDef
```




Optional fields:
- `Name`: `str`
- `Status`: `StreamProcessorStatus`


## SummaryTypeDef

```python
from mypy_boto3_rekognition.type_defs import SummaryTypeDef
```




Optional fields:
- `S3Object`: `"S3ObjectTypeDef"`


## SunglassesTypeDef

```python
from mypy_boto3_rekognition.type_defs import SunglassesTypeDef
```




Optional fields:
- `Value`: `bool`
- `Confidence`: `float`


## TechnicalCueSegmentTypeDef

```python
from mypy_boto3_rekognition.type_defs import TechnicalCueSegmentTypeDef
```




Optional fields:
- `Type`: `TechnicalCueType`
- `Confidence`: `float`


## TestingDataResultTypeDef

```python
from mypy_boto3_rekognition.type_defs import TestingDataResultTypeDef
```




Optional fields:
- `Input`: `"TestingDataTypeDef"`
- `Output`: `"TestingDataTypeDef"`
- `Validation`: `"ValidationDataTypeDef"`


## TestingDataTypeDef

```python
from mypy_boto3_rekognition.type_defs import TestingDataTypeDef
```




Optional fields:
- `Assets`: `List["AssetTypeDef"]`
- `AutoCreate`: `bool`


## TextDetectionResultTypeDef

```python
from mypy_boto3_rekognition.type_defs import TextDetectionResultTypeDef
```




Optional fields:
- `Timestamp`: `int`
- `TextDetection`: `"TextDetectionTypeDef"`


## TextDetectionTypeDef

```python
from mypy_boto3_rekognition.type_defs import TextDetectionTypeDef
```




Optional fields:
- `DetectedText`: `str`
- `Type`: `TextTypes`
- `Id`: `int`
- `ParentId`: `int`
- `Confidence`: `float`
- `Geometry`: `"GeometryTypeDef"`


## TrainingDataResultTypeDef

```python
from mypy_boto3_rekognition.type_defs import TrainingDataResultTypeDef
```




Optional fields:
- `Input`: `"TrainingDataTypeDef"`
- `Output`: `"TrainingDataTypeDef"`
- `Validation`: `"ValidationDataTypeDef"`


## TrainingDataTypeDef

```python
from mypy_boto3_rekognition.type_defs import TrainingDataTypeDef
```




Optional fields:
- `Assets`: `List["AssetTypeDef"]`


## UnindexedFaceTypeDef

```python
from mypy_boto3_rekognition.type_defs import UnindexedFaceTypeDef
```




Optional fields:
- `Reasons`: `List[Reason]`
- `FaceDetail`: `"FaceDetailTypeDef"`


## ValidationDataTypeDef

```python
from mypy_boto3_rekognition.type_defs import ValidationDataTypeDef
```




Optional fields:
- `Assets`: `List["AssetTypeDef"]`


## VideoMetadataTypeDef

```python
from mypy_boto3_rekognition.type_defs import VideoMetadataTypeDef
```




Optional fields:
- `Codec`: `str`
- `DurationMillis`: `int`
- `Format`: `str`
- `FrameRate`: `float`
- `FrameHeight`: `int`
- `FrameWidth`: `int`


## CompareFacesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import CompareFacesResponseTypeDef
```




Optional fields:
- `SourceImageFace`: `"ComparedSourceImageFaceTypeDef"`
- `FaceMatches`: `List["CompareFacesMatchTypeDef"]`
- `UnmatchedFaces`: `List["ComparedFaceTypeDef"]`
- `SourceImageOrientationCorrection`: `OrientationCorrection`
- `TargetImageOrientationCorrection`: `OrientationCorrection`


## CreateCollectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import CreateCollectionResponseTypeDef
```




Optional fields:
- `StatusCode`: `int`
- `CollectionArn`: `str`
- `FaceModelVersion`: `str`


## CreateProjectResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import CreateProjectResponseTypeDef
```




Optional fields:
- `ProjectArn`: `str`


## CreateProjectVersionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import CreateProjectVersionResponseTypeDef
```




Optional fields:
- `ProjectVersionArn`: `str`


## CreateStreamProcessorResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import CreateStreamProcessorResponseTypeDef
```




Optional fields:
- `StreamProcessorArn`: `str`


## DeleteCollectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DeleteCollectionResponseTypeDef
```




Optional fields:
- `StatusCode`: `int`


## DeleteFacesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DeleteFacesResponseTypeDef
```




Optional fields:
- `DeletedFaces`: `List[str]`


## DeleteProjectResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DeleteProjectResponseTypeDef
```




Optional fields:
- `Status`: `ProjectStatus`


## DeleteProjectVersionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DeleteProjectVersionResponseTypeDef
```




Optional fields:
- `Status`: `ProjectVersionStatus`


## DescribeCollectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DescribeCollectionResponseTypeDef
```




Optional fields:
- `FaceCount`: `int`
- `FaceModelVersion`: `str`
- `CollectionARN`: `str`
- `CreationTimestamp`: `datetime`


## DescribeProjectVersionsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DescribeProjectVersionsResponseTypeDef
```




Optional fields:
- `ProjectVersionDescriptions`: `List["ProjectVersionDescriptionTypeDef"]`
- `NextToken`: `str`


## DescribeProjectsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DescribeProjectsResponseTypeDef
```




Optional fields:
- `ProjectDescriptions`: `List["ProjectDescriptionTypeDef"]`
- `NextToken`: `str`


## DescribeStreamProcessorResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DescribeStreamProcessorResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `StreamProcessorArn`: `str`
- `Status`: `StreamProcessorStatus`
- `StatusMessage`: `str`
- `CreationTimestamp`: `datetime`
- `LastUpdateTimestamp`: `datetime`
- `Input`: `"StreamProcessorInputTypeDef"`
- `Output`: `"StreamProcessorOutputTypeDef"`
- `RoleArn`: `str`
- `Settings`: `"StreamProcessorSettingsTypeDef"`


## DetectCustomLabelsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectCustomLabelsResponseTypeDef
```




Optional fields:
- `CustomLabels`: `List["CustomLabelTypeDef"]`


## DetectFacesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectFacesResponseTypeDef
```




Optional fields:
- `FaceDetails`: `List["FaceDetailTypeDef"]`
- `OrientationCorrection`: `OrientationCorrection`


## DetectLabelsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectLabelsResponseTypeDef
```




Optional fields:
- `Labels`: `List["LabelTypeDef"]`
- `OrientationCorrection`: `OrientationCorrection`
- `LabelModelVersion`: `str`


## DetectModerationLabelsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectModerationLabelsResponseTypeDef
```




Optional fields:
- `ModerationLabels`: `List["ModerationLabelTypeDef"]`
- `ModerationModelVersion`: `str`
- `HumanLoopActivationOutput`: `"HumanLoopActivationOutputTypeDef"`


## DetectProtectiveEquipmentResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectProtectiveEquipmentResponseTypeDef
```




Optional fields:
- `ProtectiveEquipmentModelVersion`: `str`
- `Persons`: `List["ProtectiveEquipmentPersonTypeDef"]`
- `Summary`: `"ProtectiveEquipmentSummaryTypeDef"`


## DetectTextFiltersTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectTextFiltersTypeDef
```




Optional fields:
- `WordFilter`: `"DetectionFilterTypeDef"`
- `RegionsOfInterest`: `List["RegionOfInterestTypeDef"]`


## DetectTextResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import DetectTextResponseTypeDef
```




Optional fields:
- `TextDetections`: `List["TextDetectionTypeDef"]`
- `TextModelVersion`: `str`


## GetCelebrityInfoResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetCelebrityInfoResponseTypeDef
```




Optional fields:
- `Urls`: `List[str]`
- `Name`: `str`


## GetCelebrityRecognitionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetCelebrityRecognitionResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `NextToken`: `str`
- `Celebrities`: `List["CelebrityRecognitionTypeDef"]`


## GetContentModerationResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetContentModerationResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `ModerationLabels`: `List["ContentModerationDetectionTypeDef"]`
- `NextToken`: `str`
- `ModerationModelVersion`: `str`


## GetFaceDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetFaceDetectionResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `NextToken`: `str`
- `Faces`: `List["FaceDetectionTypeDef"]`


## GetFaceSearchResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetFaceSearchResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `NextToken`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `Persons`: `List["PersonMatchTypeDef"]`


## GetLabelDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetLabelDetectionResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `NextToken`: `str`
- `Labels`: `List["LabelDetectionTypeDef"]`
- `LabelModelVersion`: `str`


## GetPersonTrackingResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetPersonTrackingResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `NextToken`: `str`
- `Persons`: `List["PersonDetectionTypeDef"]`


## GetSegmentDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetSegmentDetectionResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `List["VideoMetadataTypeDef"]`
- `AudioMetadata`: `List["AudioMetadataTypeDef"]`
- `NextToken`: `str`
- `Segments`: `List["SegmentDetectionTypeDef"]`
- `SelectedSegmentTypes`: `List["SegmentTypeInfoTypeDef"]`


## GetTextDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import GetTextDetectionResponseTypeDef
```




Optional fields:
- `JobStatus`: `VideoJobStatus`
- `StatusMessage`: `str`
- `VideoMetadata`: `"VideoMetadataTypeDef"`
- `TextDetections`: `List["TextDetectionResultTypeDef"]`
- `NextToken`: `str`
- `TextModelVersion`: `str`


## HumanLoopConfigTypeDef

```python
from mypy_boto3_rekognition.type_defs import HumanLoopConfigTypeDef
```


Required fields:
- `HumanLoopName`: `str`
- `FlowDefinitionArn`: `str`



Optional fields:
- `DataAttributes`: `"HumanLoopDataAttributesTypeDef"`


## ImageTypeDef

```python
from mypy_boto3_rekognition.type_defs import ImageTypeDef
```




Optional fields:
- `Bytes`: `Union[bytes, IO[bytes]]`
- `S3Object`: `"S3ObjectTypeDef"`


## IndexFacesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import IndexFacesResponseTypeDef
```




Optional fields:
- `FaceRecords`: `List["FaceRecordTypeDef"]`
- `OrientationCorrection`: `OrientationCorrection`
- `FaceModelVersion`: `str`
- `UnindexedFaces`: `List["UnindexedFaceTypeDef"]`


## ListCollectionsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import ListCollectionsResponseTypeDef
```




Optional fields:
- `CollectionIds`: `List[str]`
- `NextToken`: `str`
- `FaceModelVersions`: `List[str]`


## ListFacesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import ListFacesResponseTypeDef
```




Optional fields:
- `Faces`: `List["FaceTypeDef"]`
- `NextToken`: `str`
- `FaceModelVersion`: `str`


## ListStreamProcessorsResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import ListStreamProcessorsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `StreamProcessors`: `List["StreamProcessorTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## NotificationChannelTypeDef

```python
from mypy_boto3_rekognition.type_defs import NotificationChannelTypeDef
```


Required fields:
- `SNSTopicArn`: `str`
- `RoleArn`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_rekognition.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProtectiveEquipmentSummarizationAttributesTypeDef

```python
from mypy_boto3_rekognition.type_defs import ProtectiveEquipmentSummarizationAttributesTypeDef
```


Required fields:
- `MinConfidence`: `float`
- `RequiredEquipmentTypes`: `List[ProtectiveEquipmentType]`




## RecognizeCelebritiesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import RecognizeCelebritiesResponseTypeDef
```




Optional fields:
- `CelebrityFaces`: `List["CelebrityTypeDef"]`
- `UnrecognizedFaces`: `List["ComparedFaceTypeDef"]`
- `OrientationCorrection`: `OrientationCorrection`


## SearchFacesByImageResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import SearchFacesByImageResponseTypeDef
```




Optional fields:
- `SearchedFaceBoundingBox`: `"BoundingBoxTypeDef"`
- `SearchedFaceConfidence`: `float`
- `FaceMatches`: `List["FaceMatchTypeDef"]`
- `FaceModelVersion`: `str`


## SearchFacesResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import SearchFacesResponseTypeDef
```




Optional fields:
- `SearchedFaceId`: `str`
- `FaceMatches`: `List["FaceMatchTypeDef"]`
- `FaceModelVersion`: `str`


## StartCelebrityRecognitionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartCelebrityRecognitionResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartContentModerationResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartContentModerationResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartFaceDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartFaceDetectionResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartFaceSearchResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartFaceSearchResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartLabelDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartLabelDetectionResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartPersonTrackingResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartPersonTrackingResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartProjectVersionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartProjectVersionResponseTypeDef
```




Optional fields:
- `Status`: `ProjectVersionStatus`


## StartSegmentDetectionFiltersTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartSegmentDetectionFiltersTypeDef
```




Optional fields:
- `TechnicalCueFilter`: `"StartTechnicalCueDetectionFilterTypeDef"`
- `ShotFilter`: `"StartShotDetectionFilterTypeDef"`


## StartSegmentDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartSegmentDetectionResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartTextDetectionFiltersTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartTextDetectionFiltersTypeDef
```




Optional fields:
- `WordFilter`: `"DetectionFilterTypeDef"`
- `RegionsOfInterest`: `List["RegionOfInterestTypeDef"]`


## StartTextDetectionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StartTextDetectionResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StopProjectVersionResponseTypeDef

```python
from mypy_boto3_rekognition.type_defs import StopProjectVersionResponseTypeDef
```




Optional fields:
- `Status`: `ProjectVersionStatus`


## VideoTypeDef

```python
from mypy_boto3_rekognition.type_defs import VideoTypeDef
```




Optional fields:
- `S3Object`: `"S3ObjectTypeDef"`


## WaiterConfigTypeDef

```python
from mypy_boto3_rekognition.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

