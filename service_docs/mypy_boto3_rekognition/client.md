# RekognitionClient for boto3 Rekognition module

> [Index](../index.md) > [Rekognition](./index.md) > RekognitionClient

Auto-generated documentation for [Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition)
type annotations stubs module [mypy_boto3_rekognition](https://pypi.org/project/mypy-boto3-rekognition/).

- [RekognitionClient for boto3 Rekognition module](#rekognitionclient-for-boto3-rekognition-module)
  - [RekognitionClient](#rekognitionclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [compare_faces](#compare_faces)
    - [create_collection](#create_collection)
    - [create_project](#create_project)
    - [create_project_version](#create_project_version)
    - [create_stream_processor](#create_stream_processor)
    - [delete_collection](#delete_collection)
    - [delete_faces](#delete_faces)
    - [delete_project](#delete_project)
    - [delete_project_version](#delete_project_version)
    - [delete_stream_processor](#delete_stream_processor)
    - [describe_collection](#describe_collection)
    - [describe_project_versions](#describe_project_versions)
    - [describe_projects](#describe_projects)
    - [describe_stream_processor](#describe_stream_processor)
    - [detect_custom_labels](#detect_custom_labels)
    - [detect_faces](#detect_faces)
    - [detect_labels](#detect_labels)
    - [detect_moderation_labels](#detect_moderation_labels)
    - [detect_protective_equipment](#detect_protective_equipment)
    - [detect_text](#detect_text)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_celebrity_info](#get_celebrity_info)
    - [get_celebrity_recognition](#get_celebrity_recognition)
    - [get_content_moderation](#get_content_moderation)
    - [get_face_detection](#get_face_detection)
    - [get_face_search](#get_face_search)
    - [get_label_detection](#get_label_detection)
    - [get_person_tracking](#get_person_tracking)
    - [get_segment_detection](#get_segment_detection)
    - [get_text_detection](#get_text_detection)
    - [index_faces](#index_faces)
    - [list_collections](#list_collections)
    - [list_faces](#list_faces)
    - [list_stream_processors](#list_stream_processors)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [recognize_celebrities](#recognize_celebrities)
    - [search_faces](#search_faces)
    - [search_faces_by_image](#search_faces_by_image)
    - [start_celebrity_recognition](#start_celebrity_recognition)
    - [start_content_moderation](#start_content_moderation)
    - [start_face_detection](#start_face_detection)
    - [start_face_search](#start_face_search)
    - [start_label_detection](#start_label_detection)
    - [start_person_tracking](#start_person_tracking)
    - [start_project_version](#start_project_version)
    - [start_segment_detection](#start_segment_detection)
    - [start_stream_processor](#start_stream_processor)
    - [start_text_detection](#start_text_detection)
    - [stop_project_version](#stop_project_version)
    - [stop_stream_processor](#stop_stream_processor)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)

## RekognitionClient

Type annotations for `boto3.client("rekognition")`

Can be used directly:

```python
from mypy_boto3_rekognition.client import RekognitionClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_rekognition.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.HumanLoopQuotaExceededException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.ImageTooLargeException`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidImageFormatException`
- `Exceptions.InvalidPaginationTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidS3ObjectException`
- `Exceptions.LimitExceededException`
- `Exceptions.ProvisionedThroughputExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceNotReadyException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.VideoTooLargeException`


## Methods


### can_paginate

Type annotations for `boto3.client("rekognition").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### compare_faces

Type annotations for `boto3.client("rekognition").compare_faces` method.

[Client.compare_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.compare_faces)

```python
def compare_faces(
    self,
    SourceImage: ImageTypeDef,
    TargetImage: ImageTypeDef,
    SimilarityThreshold: float = None,
    QualityFilter: QualityFilter = None
) -> CompareFacesResponseTypeDef:
    pass
```

### create_collection

Type annotations for `boto3.client("rekognition").create_collection` method.

[Client.create_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_collection)

```python
def create_collection(
    self,
    CollectionId: str,
    Tags: Dict[str, str] = None
) -> CreateCollectionResponseTypeDef:
    pass
```

### create_project

Type annotations for `boto3.client("rekognition").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_project)

```python
def create_project(
    self,
    ProjectName: str
) -> CreateProjectResponseTypeDef:
    pass
```

### create_project_version

Type annotations for `boto3.client("rekognition").create_project_version` method.

[Client.create_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_project_version)

```python
def create_project_version(
    self,
    ProjectArn: str,
    VersionName: str,
    OutputConfig: "OutputConfigTypeDef",
    TrainingData: "TrainingDataTypeDef",
    TestingData: "TestingDataTypeDef",
    Tags: Dict[str, str] = None
) -> CreateProjectVersionResponseTypeDef:
    pass
```

### create_stream_processor

Type annotations for `boto3.client("rekognition").create_stream_processor` method.

[Client.create_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)

```python
def create_stream_processor(
    self,
    Input: "StreamProcessorInputTypeDef",
    Output: "StreamProcessorOutputTypeDef",
    Name: str,
    Settings: "StreamProcessorSettingsTypeDef",
    RoleArn: str,
    Tags: Dict[str, str] = None
) -> CreateStreamProcessorResponseTypeDef:
    pass
```

### delete_collection

Type annotations for `boto3.client("rekognition").delete_collection` method.

[Client.delete_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_collection)

```python
def delete_collection(
    self,
    CollectionId: str
) -> DeleteCollectionResponseTypeDef:
    pass
```

### delete_faces

Type annotations for `boto3.client("rekognition").delete_faces` method.

[Client.delete_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_faces)

```python
def delete_faces(
    self,
    CollectionId: str,
    FaceIds: List[str]
) -> DeleteFacesResponseTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("rekognition").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_project)

```python
def delete_project(
    self,
    ProjectArn: str
) -> DeleteProjectResponseTypeDef:
    pass
```

### delete_project_version

Type annotations for `boto3.client("rekognition").delete_project_version` method.

[Client.delete_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_project_version)

```python
def delete_project_version(
    self,
    ProjectVersionArn: str
) -> DeleteProjectVersionResponseTypeDef:
    pass
```

### delete_stream_processor

Type annotations for `boto3.client("rekognition").delete_stream_processor` method.

[Client.delete_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)

```python
def delete_stream_processor(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### describe_collection

Type annotations for `boto3.client("rekognition").describe_collection` method.

[Client.describe_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_collection)

```python
def describe_collection(
    self,
    CollectionId: str
) -> DescribeCollectionResponseTypeDef:
    pass
```

### describe_project_versions

Type annotations for `boto3.client("rekognition").describe_project_versions` method.

[Client.describe_project_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)

```python
def describe_project_versions(
    self,
    ProjectArn: str,
    VersionNames: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeProjectVersionsResponseTypeDef:
    pass
```

### describe_projects

Type annotations for `boto3.client("rekognition").describe_projects` method.

[Client.describe_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_projects)

```python
def describe_projects(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeProjectsResponseTypeDef:
    pass
```

### describe_stream_processor

Type annotations for `boto3.client("rekognition").describe_stream_processor` method.

[Client.describe_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)

```python
def describe_stream_processor(
    self,
    Name: str
) -> DescribeStreamProcessorResponseTypeDef:
    pass
```

### detect_custom_labels

Type annotations for `boto3.client("rekognition").detect_custom_labels` method.

[Client.detect_custom_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)

```python
def detect_custom_labels(
    self,
    ProjectVersionArn: str,
    Image: ImageTypeDef,
    MaxResults: int = None,
    MinConfidence: float = None
) -> DetectCustomLabelsResponseTypeDef:
    pass
```

### detect_faces

Type annotations for `boto3.client("rekognition").detect_faces` method.

[Client.detect_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces)

```python
def detect_faces(
    self,
    Image: ImageTypeDef,
    Attributes: List[Attribute] = None
) -> DetectFacesResponseTypeDef:
    pass
```

### detect_labels

Type annotations for `boto3.client("rekognition").detect_labels` method.

[Client.detect_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels)

```python
def detect_labels(
    self,
    Image: ImageTypeDef,
    MaxLabels: int = None,
    MinConfidence: float = None
) -> DetectLabelsResponseTypeDef:
    pass
```

### detect_moderation_labels

Type annotations for `boto3.client("rekognition").detect_moderation_labels` method.

[Client.detect_moderation_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)

```python
def detect_moderation_labels(
    self,
    Image: ImageTypeDef,
    MinConfidence: float = None,
    HumanLoopConfig: HumanLoopConfigTypeDef = None
) -> DetectModerationLabelsResponseTypeDef:
    pass
```

### detect_protective_equipment

Type annotations for `boto3.client("rekognition").detect_protective_equipment` method.

[Client.detect_protective_equipment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_protective_equipment)

```python
def detect_protective_equipment(
    self,
    Image: ImageTypeDef,
    SummarizationAttributes: ProtectiveEquipmentSummarizationAttributesTypeDef = None
) -> DetectProtectiveEquipmentResponseTypeDef:
    pass
```

### detect_text

Type annotations for `boto3.client("rekognition").detect_text` method.

[Client.detect_text documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_text)

```python
def detect_text(
    self,
    Image: ImageTypeDef,
    Filters: DetectTextFiltersTypeDef = None
) -> DetectTextResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("rekognition").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_celebrity_info

Type annotations for `boto3.client("rekognition").get_celebrity_info` method.

[Client.get_celebrity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)

```python
def get_celebrity_info(
    self,
    Id: str
) -> GetCelebrityInfoResponseTypeDef:
    pass
```

### get_celebrity_recognition

Type annotations for `boto3.client("rekognition").get_celebrity_recognition` method.

[Client.get_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)

```python
def get_celebrity_recognition(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: CelebrityRecognitionSortBy = None
) -> GetCelebrityRecognitionResponseTypeDef:
    pass
```

### get_content_moderation

Type annotations for `boto3.client("rekognition").get_content_moderation` method.

[Client.get_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)

```python
def get_content_moderation(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: ContentModerationSortBy = None
) -> GetContentModerationResponseTypeDef:
    pass
```

### get_face_detection

Type annotations for `boto3.client("rekognition").get_face_detection` method.

[Client.get_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_face_detection)

```python
def get_face_detection(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetFaceDetectionResponseTypeDef:
    pass
```

### get_face_search

Type annotations for `boto3.client("rekognition").get_face_search` method.

[Client.get_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_face_search)

```python
def get_face_search(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: FaceSearchSortBy = None
) -> GetFaceSearchResponseTypeDef:
    pass
```

### get_label_detection

Type annotations for `boto3.client("rekognition").get_label_detection` method.

[Client.get_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_label_detection)

```python
def get_label_detection(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: LabelDetectionSortBy = None
) -> GetLabelDetectionResponseTypeDef:
    pass
```

### get_person_tracking

Type annotations for `boto3.client("rekognition").get_person_tracking` method.

[Client.get_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)

```python
def get_person_tracking(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None,
    SortBy: PersonTrackingSortBy = None
) -> GetPersonTrackingResponseTypeDef:
    pass
```

### get_segment_detection

Type annotations for `boto3.client("rekognition").get_segment_detection` method.

[Client.get_segment_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_segment_detection)

```python
def get_segment_detection(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetSegmentDetectionResponseTypeDef:
    pass
```

### get_text_detection

Type annotations for `boto3.client("rekognition").get_text_detection` method.

[Client.get_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_text_detection)

```python
def get_text_detection(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetTextDetectionResponseTypeDef:
    pass
```

### index_faces

Type annotations for `boto3.client("rekognition").index_faces` method.

[Client.index_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.index_faces)

```python
def index_faces(
    self,
    CollectionId: str,
    Image: ImageTypeDef,
    ExternalImageId: str = None,
    DetectionAttributes: List[Attribute] = None,
    MaxFaces: int = None,
    QualityFilter: QualityFilter = None
) -> IndexFacesResponseTypeDef:
    pass
```

### list_collections

Type annotations for `boto3.client("rekognition").list_collections` method.

[Client.list_collections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_collections)

```python
def list_collections(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListCollectionsResponseTypeDef:
    pass
```

### list_faces

Type annotations for `boto3.client("rekognition").list_faces` method.

[Client.list_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_faces)

```python
def list_faces(
    self,
    CollectionId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListFacesResponseTypeDef:
    pass
```

### list_stream_processors

Type annotations for `boto3.client("rekognition").list_stream_processors` method.

[Client.list_stream_processors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)

```python
def list_stream_processors(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListStreamProcessorsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("rekognition").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### recognize_celebrities

Type annotations for `boto3.client("rekognition").recognize_celebrities` method.

[Client.recognize_celebrities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)

```python
def recognize_celebrities(
    self,
    Image: ImageTypeDef
) -> RecognizeCelebritiesResponseTypeDef:
    pass
```

### search_faces

Type annotations for `boto3.client("rekognition").search_faces` method.

[Client.search_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.search_faces)

```python
def search_faces(
    self,
    CollectionId: str,
    FaceId: str,
    MaxFaces: int = None,
    FaceMatchThreshold: float = None
) -> SearchFacesResponseTypeDef:
    pass
```

### search_faces_by_image

Type annotations for `boto3.client("rekognition").search_faces_by_image` method.

[Client.search_faces_by_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)

```python
def search_faces_by_image(
    self,
    CollectionId: str,
    Image: ImageTypeDef,
    MaxFaces: int = None,
    FaceMatchThreshold: float = None,
    QualityFilter: QualityFilter = None
) -> SearchFacesByImageResponseTypeDef:
    pass
```

### start_celebrity_recognition

Type annotations for `boto3.client("rekognition").start_celebrity_recognition` method.

[Client.start_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)

```python
def start_celebrity_recognition(
    self,
    Video: VideoTypeDef,
    ClientRequestToken: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None
) -> StartCelebrityRecognitionResponseTypeDef:
    pass
```

### start_content_moderation

Type annotations for `boto3.client("rekognition").start_content_moderation` method.

[Client.start_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)

```python
def start_content_moderation(
    self,
    Video: VideoTypeDef,
    MinConfidence: float = None,
    ClientRequestToken: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None
) -> StartContentModerationResponseTypeDef:
    pass
```

### start_face_detection

Type annotations for `boto3.client("rekognition").start_face_detection` method.

[Client.start_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_face_detection)

```python
def start_face_detection(
    self,
    Video: VideoTypeDef,
    ClientRequestToken: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    FaceAttributes: FaceAttributes = None,
    JobTag: str = None
) -> StartFaceDetectionResponseTypeDef:
    pass
```

### start_face_search

Type annotations for `boto3.client("rekognition").start_face_search` method.

[Client.start_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_face_search)

```python
def start_face_search(
    self,
    Video: VideoTypeDef,
    CollectionId: str,
    ClientRequestToken: str = None,
    FaceMatchThreshold: float = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None
) -> StartFaceSearchResponseTypeDef:
    pass
```

### start_label_detection

Type annotations for `boto3.client("rekognition").start_label_detection` method.

[Client.start_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_label_detection)

```python
def start_label_detection(
    self,
    Video: VideoTypeDef,
    ClientRequestToken: str = None,
    MinConfidence: float = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None
) -> StartLabelDetectionResponseTypeDef:
    pass
```

### start_person_tracking

Type annotations for `boto3.client("rekognition").start_person_tracking` method.

[Client.start_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)

```python
def start_person_tracking(
    self,
    Video: VideoTypeDef,
    ClientRequestToken: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None
) -> StartPersonTrackingResponseTypeDef:
    pass
```

### start_project_version

Type annotations for `boto3.client("rekognition").start_project_version` method.

[Client.start_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_project_version)

```python
def start_project_version(
    self,
    ProjectVersionArn: str,
    MinInferenceUnits: int
) -> StartProjectVersionResponseTypeDef:
    pass
```

### start_segment_detection

Type annotations for `boto3.client("rekognition").start_segment_detection` method.

[Client.start_segment_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_segment_detection)

```python
def start_segment_detection(
    self,
    Video: VideoTypeDef,
    SegmentTypes: List[SegmentType],
    ClientRequestToken: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None,
    Filters: StartSegmentDetectionFiltersTypeDef = None
) -> StartSegmentDetectionResponseTypeDef:
    pass
```

### start_stream_processor

Type annotations for `boto3.client("rekognition").start_stream_processor` method.

[Client.start_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)

```python
def start_stream_processor(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### start_text_detection

Type annotations for `boto3.client("rekognition").start_text_detection` method.

[Client.start_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_text_detection)

```python
def start_text_detection(
    self,
    Video: VideoTypeDef,
    ClientRequestToken: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    JobTag: str = None,
    Filters: StartTextDetectionFiltersTypeDef = None
) -> StartTextDetectionResponseTypeDef:
    pass
```

### stop_project_version

Type annotations for `boto3.client("rekognition").stop_project_version` method.

[Client.stop_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.stop_project_version)

```python
def stop_project_version(
    self,
    ProjectVersionArn: str
) -> StopProjectVersionResponseTypeDef:
    pass
```

### stop_stream_processor

Type annotations for `boto3.client("rekognition").stop_stream_processor` method.

[Client.stop_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)

```python
def stop_stream_processor(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("rekognition").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("rekognition").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("rekognition").get_paginator` method.

[Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeProjectVersionsPaginatorName
) -> DescribeProjectVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("rekognition").get_paginator` method.

[Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeProjectsPaginatorName
) -> DescribeProjectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("rekognition").get_paginator` method.

[Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCollectionsPaginatorName
) -> ListCollectionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("rekognition").get_paginator` method.

[Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)

```python
@overload
def get_paginator(
    self,
    operation_name: ListFacesPaginatorName
) -> ListFacesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("rekognition").get_paginator` method.

[Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStreamProcessorsPaginatorName
) -> ListStreamProcessorsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("rekognition").get_waiter` method.

[Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)

```python
@overload
def get_waiter(
    self,
    waiter_name: ProjectVersionRunningWaiterName
) -> ProjectVersionRunningWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("rekognition").get_waiter` method.

[Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: ProjectVersionTrainingCompletedWaiterName
) -> ProjectVersionTrainingCompletedWaiter:
    pass
```