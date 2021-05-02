# Literals for boto3 Rekognition module

> [Index](../index.md) > [Rekognition](./index.md) > Literals

Auto-generated documentation for [Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition)
type annotations stubs module [mypy_boto3_rekognition](https://pypi.org/project/mypy-boto3-rekognition/).

- [Literals for boto3 Rekognition module](#literals-for-boto3-rekognition-module)
  - [Attribute](#attribute)
  - [BodyPart](#bodypart)
  - [CelebrityRecognitionSortBy](#celebrityrecognitionsortby)
  - [ContentClassifier](#contentclassifier)
  - [ContentModerationSortBy](#contentmoderationsortby)
  - [DescribeProjectVersionsPaginatorName](#describeprojectversionspaginatorname)
  - [DescribeProjectsPaginatorName](#describeprojectspaginatorname)
  - [EmotionName](#emotionname)
  - [FaceAttributes](#faceattributes)
  - [FaceSearchSortBy](#facesearchsortby)
  - [GenderType](#gendertype)
  - [LabelDetectionSortBy](#labeldetectionsortby)
  - [LandmarkType](#landmarktype)
  - [ListCollectionsPaginatorName](#listcollectionspaginatorname)
  - [ListFacesPaginatorName](#listfacespaginatorname)
  - [ListStreamProcessorsPaginatorName](#liststreamprocessorspaginatorname)
  - [OrientationCorrection](#orientationcorrection)
  - [PersonTrackingSortBy](#persontrackingsortby)
  - [ProjectStatus](#projectstatus)
  - [ProjectVersionRunningWaiterName](#projectversionrunningwaitername)
  - [ProjectVersionStatus](#projectversionstatus)
  - [ProjectVersionTrainingCompletedWaiterName](#projectversiontrainingcompletedwaitername)
  - [ProtectiveEquipmentType](#protectiveequipmenttype)
  - [QualityFilter](#qualityfilter)
  - [Reason](#reason)
  - [SegmentType](#segmenttype)
  - [StreamProcessorStatus](#streamprocessorstatus)
  - [TechnicalCueType](#technicalcuetype)
  - [TextTypes](#texttypes)
  - [VideoJobStatus](#videojobstatus)

## Attribute

```python
from mypy_boto3_rekognition.literals import Attribute
```

Values:

- `ALL`
- `DEFAULT`

## BodyPart

```python
from mypy_boto3_rekognition.literals import BodyPart
```

Values:

- `FACE`
- `HEAD`
- `LEFT_HAND`
- `RIGHT_HAND`

## CelebrityRecognitionSortBy

```python
from mypy_boto3_rekognition.literals import CelebrityRecognitionSortBy
```

Values:

- `ID`
- `TIMESTAMP`

## ContentClassifier

```python
from mypy_boto3_rekognition.literals import ContentClassifier
```

Values:

- `FreeOfAdultContent`
- `FreeOfPersonallyIdentifiableInformation`

## ContentModerationSortBy

```python
from mypy_boto3_rekognition.literals import ContentModerationSortBy
```

Values:

- `NAME`
- `TIMESTAMP`

## DescribeProjectVersionsPaginatorName

```python
from mypy_boto3_rekognition.literals import DescribeProjectVersionsPaginatorName
```

Values:

- `describe_project_versions`

## DescribeProjectsPaginatorName

```python
from mypy_boto3_rekognition.literals import DescribeProjectsPaginatorName
```

Values:

- `describe_projects`

## EmotionName

```python
from mypy_boto3_rekognition.literals import EmotionName
```

Values:

- `ANGRY`
- `CALM`
- `CONFUSED`
- `DISGUSTED`
- `FEAR`
- `HAPPY`
- `SAD`
- `SURPRISED`
- `UNKNOWN`

## FaceAttributes

```python
from mypy_boto3_rekognition.literals import FaceAttributes
```

Values:

- `ALL`
- `DEFAULT`

## FaceSearchSortBy

```python
from mypy_boto3_rekognition.literals import FaceSearchSortBy
```

Values:

- `INDEX`
- `TIMESTAMP`

## GenderType

```python
from mypy_boto3_rekognition.literals import GenderType
```

Values:

- `Female`
- `Male`

## LabelDetectionSortBy

```python
from mypy_boto3_rekognition.literals import LabelDetectionSortBy
```

Values:

- `NAME`
- `TIMESTAMP`

## LandmarkType

```python
from mypy_boto3_rekognition.literals import LandmarkType
```

Values:

- `chinBottom`
- `eyeLeft`
- `eyeRight`
- `leftEyeBrowLeft`
- `leftEyeBrowRight`
- `leftEyeBrowUp`
- `leftEyeDown`
- `leftEyeLeft`
- `leftEyeRight`
- `leftEyeUp`
- `leftPupil`
- `midJawlineLeft`
- `midJawlineRight`
- `mouthDown`
- `mouthLeft`
- `mouthRight`
- `mouthUp`
- `nose`
- `noseLeft`
- `noseRight`
- `rightEyeBrowLeft`
- `rightEyeBrowRight`
- `rightEyeBrowUp`
- `rightEyeDown`
- `rightEyeLeft`
- `rightEyeRight`
- `rightEyeUp`
- `rightPupil`
- `upperJawlineLeft`
- `upperJawlineRight`

## ListCollectionsPaginatorName

```python
from mypy_boto3_rekognition.literals import ListCollectionsPaginatorName
```

Values:

- `list_collections`

## ListFacesPaginatorName

```python
from mypy_boto3_rekognition.literals import ListFacesPaginatorName
```

Values:

- `list_faces`

## ListStreamProcessorsPaginatorName

```python
from mypy_boto3_rekognition.literals import ListStreamProcessorsPaginatorName
```

Values:

- `list_stream_processors`

## OrientationCorrection

```python
from mypy_boto3_rekognition.literals import OrientationCorrection
```

Values:

- `ROTATE_0`
- `ROTATE_180`
- `ROTATE_270`
- `ROTATE_90`

## PersonTrackingSortBy

```python
from mypy_boto3_rekognition.literals import PersonTrackingSortBy
```

Values:

- `INDEX`
- `TIMESTAMP`

## ProjectStatus

```python
from mypy_boto3_rekognition.literals import ProjectStatus
```

Values:

- `CREATED`
- `CREATING`
- `DELETING`

## ProjectVersionRunningWaiterName

```python
from mypy_boto3_rekognition.literals import ProjectVersionRunningWaiterName
```

Values:

- `project_version_running`

## ProjectVersionStatus

```python
from mypy_boto3_rekognition.literals import ProjectVersionStatus
```

Values:

- `DELETING`
- `FAILED`
- `RUNNING`
- `STARTING`
- `STOPPED`
- `STOPPING`
- `TRAINING_COMPLETED`
- `TRAINING_FAILED`
- `TRAINING_IN_PROGRESS`

## ProjectVersionTrainingCompletedWaiterName

```python
from mypy_boto3_rekognition.literals import ProjectVersionTrainingCompletedWaiterName
```

Values:

- `project_version_training_completed`

## ProtectiveEquipmentType

```python
from mypy_boto3_rekognition.literals import ProtectiveEquipmentType
```

Values:

- `FACE_COVER`
- `HAND_COVER`
- `HEAD_COVER`

## QualityFilter

```python
from mypy_boto3_rekognition.literals import QualityFilter
```

Values:

- `AUTO`
- `HIGH`
- `LOW`
- `MEDIUM`
- `NONE`

## Reason

```python
from mypy_boto3_rekognition.literals import Reason
```

Values:

- `EXCEEDS_MAX_FACES`
- `EXTREME_POSE`
- `LOW_BRIGHTNESS`
- `LOW_CONFIDENCE`
- `LOW_FACE_QUALITY`
- `LOW_SHARPNESS`
- `SMALL_BOUNDING_BOX`

## SegmentType

```python
from mypy_boto3_rekognition.literals import SegmentType
```

Values:

- `SHOT`
- `TECHNICAL_CUE`

## StreamProcessorStatus

```python
from mypy_boto3_rekognition.literals import StreamProcessorStatus
```

Values:

- `FAILED`
- `RUNNING`
- `STARTING`
- `STOPPED`
- `STOPPING`

## TechnicalCueType

```python
from mypy_boto3_rekognition.literals import TechnicalCueType
```

Values:

- `BlackFrames`
- `ColorBars`
- `EndCredits`

## TextTypes

```python
from mypy_boto3_rekognition.literals import TextTypes
```

Values:

- `LINE`
- `WORD`

## VideoJobStatus

```python
from mypy_boto3_rekognition.literals import VideoJobStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SUCCEEDED`
