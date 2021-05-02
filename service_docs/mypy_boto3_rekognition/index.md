# Type annotations for boto3 Rekognition module

> [Index](../index.md) > Rekognition

Auto-generated documentation for [Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition)
type annotations stubs module [mypy_boto3_rekognition](https://pypi.org/project/mypy-boto3-rekognition/).

```bash
pip install mypy-boto3-rekognition
```

- [Type annotations for boto3 Rekognition module](#type-annotations-for-boto3-rekognition-module)
  - [RekognitionClient](#rekognitionclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## RekognitionClient

Type annotations for  `boto3.client("rekognition")` as [RekognitionClient](./client.md)

Can be used directly:

```python
from mypy_boto3_rekognition.client import RekognitionClient
```


RekognitionClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [compare_faces](./client.md#compare-faces)
- [create_collection](./client.md#create-collection)
- [create_project](./client.md#create-project)
- [create_project_version](./client.md#create-project-version)
- [create_stream_processor](./client.md#create-stream-processor)
- [delete_collection](./client.md#delete-collection)
- [delete_faces](./client.md#delete-faces)
- [delete_project](./client.md#delete-project)
- [delete_project_version](./client.md#delete-project-version)
- [delete_stream_processor](./client.md#delete-stream-processor)
- [describe_collection](./client.md#describe-collection)
- [describe_project_versions](./client.md#describe-project-versions)
- [describe_projects](./client.md#describe-projects)
- [describe_stream_processor](./client.md#describe-stream-processor)
- [detect_custom_labels](./client.md#detect-custom-labels)
- [detect_faces](./client.md#detect-faces)
- [detect_labels](./client.md#detect-labels)
- [detect_moderation_labels](./client.md#detect-moderation-labels)
- [detect_protective_equipment](./client.md#detect-protective-equipment)
- [detect_text](./client.md#detect-text)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_celebrity_info](./client.md#get-celebrity-info)
- [get_celebrity_recognition](./client.md#get-celebrity-recognition)
- [get_content_moderation](./client.md#get-content-moderation)
- [get_face_detection](./client.md#get-face-detection)
- [get_face_search](./client.md#get-face-search)
- [get_label_detection](./client.md#get-label-detection)
- [get_paginator](./client.md#get-paginator)
- [get_person_tracking](./client.md#get-person-tracking)
- [get_segment_detection](./client.md#get-segment-detection)
- [get_text_detection](./client.md#get-text-detection)
- [get_waiter](./client.md#get-waiter)
- [index_faces](./client.md#index-faces)
- [list_collections](./client.md#list-collections)
- [list_faces](./client.md#list-faces)
- [list_stream_processors](./client.md#list-stream-processors)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [recognize_celebrities](./client.md#recognize-celebrities)
- [search_faces](./client.md#search-faces)
- [search_faces_by_image](./client.md#search-faces-by-image)
- [start_celebrity_recognition](./client.md#start-celebrity-recognition)
- [start_content_moderation](./client.md#start-content-moderation)
- [start_face_detection](./client.md#start-face-detection)
- [start_face_search](./client.md#start-face-search)
- [start_label_detection](./client.md#start-label-detection)
- [start_person_tracking](./client.md#start-person-tracking)
- [start_project_version](./client.md#start-project-version)
- [start_segment_detection](./client.md#start-segment-detection)
- [start_stream_processor](./client.md#start-stream-processor)
- [start_text_detection](./client.md#start-text-detection)
- [stop_project_version](./client.md#stop-project-version)
- [stop_stream_processor](./client.md#stop-stream-processor)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [HumanLoopQuotaExceededException](./client.md#humanloopquotaexceededexception)
- [IdempotentParameterMismatchException](./client.md#idempotentparametermismatchexception)
- [ImageTooLargeException](./client.md#imagetoolargeexception)
- [InternalServerError](./client.md#internalservererror)
- [InvalidImageFormatException](./client.md#invalidimageformatexception)
- [InvalidPaginationTokenException](./client.md#invalidpaginationtokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidS3ObjectException](./client.md#invalids3objectexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ProvisionedThroughputExceededException](./client.md#provisionedthroughputexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceNotReadyException](./client.md#resourcenotreadyexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [VideoTooLargeException](./client.md#videotoolargeexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("rekognition").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_rekognition.paginators import DescribeProjectVersionsPaginator, ...
```

- [DescribeProjectVersionsPaginator](./paginators.md#describeprojectversionspaginator)
- [DescribeProjectsPaginator](./paginators.md#describeprojectspaginator)
- [ListCollectionsPaginator](./paginators.md#listcollectionspaginator)
- [ListFacesPaginator](./paginators.md#listfacespaginator)
- [ListStreamProcessorsPaginator](./paginators.md#liststreamprocessorspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("rekognition").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_rekognition.waiters import ProjectVersionRunningWaiter, ...
```

- [ProjectVersionRunningWaiter](./waiters.md#projectversionrunningwaiter)
- [ProjectVersionTrainingCompletedWaiter](./waiters.md#projectversiontrainingcompletedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_rekognition.literals import Attribute, ...
```

- [Attribute](./literals.md#attribute)
- [BodyPart](./literals.md#bodypart)
- [CelebrityRecognitionSortBy](./literals.md#celebrityrecognitionsortby)
- [ContentClassifier](./literals.md#contentclassifier)
- [ContentModerationSortBy](./literals.md#contentmoderationsortby)
- [DescribeProjectVersionsPaginatorName](./literals.md#describeprojectversionspaginatorname)
- [DescribeProjectsPaginatorName](./literals.md#describeprojectspaginatorname)
- [EmotionName](./literals.md#emotionname)
- [FaceAttributes](./literals.md#faceattributes)
- [FaceSearchSortBy](./literals.md#facesearchsortby)
- [GenderType](./literals.md#gendertype)
- [LabelDetectionSortBy](./literals.md#labeldetectionsortby)
- [LandmarkType](./literals.md#landmarktype)
- [ListCollectionsPaginatorName](./literals.md#listcollectionspaginatorname)
- [ListFacesPaginatorName](./literals.md#listfacespaginatorname)
- [ListStreamProcessorsPaginatorName](./literals.md#liststreamprocessorspaginatorname)
- [OrientationCorrection](./literals.md#orientationcorrection)
- [PersonTrackingSortBy](./literals.md#persontrackingsortby)
- [ProjectStatus](./literals.md#projectstatus)
- [ProjectVersionRunningWaiterName](./literals.md#projectversionrunningwaitername)
- [ProjectVersionStatus](./literals.md#projectversionstatus)
- [ProjectVersionTrainingCompletedWaiterName](./literals.md#projectversiontrainingcompletedwaitername)
- [ProtectiveEquipmentType](./literals.md#protectiveequipmenttype)
- [QualityFilter](./literals.md#qualityfilter)
- [Reason](./literals.md#reason)
- [SegmentType](./literals.md#segmenttype)
- [StreamProcessorStatus](./literals.md#streamprocessorstatus)
- [TechnicalCueType](./literals.md#technicalcuetype)
- [TextTypes](./literals.md#texttypes)
- [VideoJobStatus](./literals.md#videojobstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef, ...
```

- [AgeRangeTypeDef](./type_defs.md#agerangetypedef)
- [AssetTypeDef](./type_defs.md#assettypedef)
- [AudioMetadataTypeDef](./type_defs.md#audiometadatatypedef)
- [BeardTypeDef](./type_defs.md#beardtypedef)
- [BoundingBoxTypeDef](./type_defs.md#boundingboxtypedef)
- [CelebrityDetailTypeDef](./type_defs.md#celebritydetailtypedef)
- [CelebrityRecognitionTypeDef](./type_defs.md#celebrityrecognitiontypedef)
- [CelebrityTypeDef](./type_defs.md#celebritytypedef)
- [CompareFacesMatchTypeDef](./type_defs.md#comparefacesmatchtypedef)
- [ComparedFaceTypeDef](./type_defs.md#comparedfacetypedef)
- [ComparedSourceImageFaceTypeDef](./type_defs.md#comparedsourceimagefacetypedef)
- [ContentModerationDetectionTypeDef](./type_defs.md#contentmoderationdetectiontypedef)
- [CoversBodyPartTypeDef](./type_defs.md#coversbodyparttypedef)
- [CustomLabelTypeDef](./type_defs.md#customlabeltypedef)
- [DetectionFilterTypeDef](./type_defs.md#detectionfiltertypedef)
- [EmotionTypeDef](./type_defs.md#emotiontypedef)
- [EquipmentDetectionTypeDef](./type_defs.md#equipmentdetectiontypedef)
- [EvaluationResultTypeDef](./type_defs.md#evaluationresulttypedef)
- [EyeOpenTypeDef](./type_defs.md#eyeopentypedef)
- [EyeglassesTypeDef](./type_defs.md#eyeglassestypedef)
- [FaceDetailTypeDef](./type_defs.md#facedetailtypedef)
- [FaceDetectionTypeDef](./type_defs.md#facedetectiontypedef)
- [FaceMatchTypeDef](./type_defs.md#facematchtypedef)
- [FaceRecordTypeDef](./type_defs.md#facerecordtypedef)
- [FaceSearchSettingsTypeDef](./type_defs.md#facesearchsettingstypedef)
- [FaceTypeDef](./type_defs.md#facetypedef)
- [GenderTypeDef](./type_defs.md#gendertypedef)
- [GeometryTypeDef](./type_defs.md#geometrytypedef)
- [GroundTruthManifestTypeDef](./type_defs.md#groundtruthmanifesttypedef)
- [HumanLoopActivationOutputTypeDef](./type_defs.md#humanloopactivationoutputtypedef)
- [HumanLoopDataAttributesTypeDef](./type_defs.md#humanloopdataattributestypedef)
- [ImageQualityTypeDef](./type_defs.md#imagequalitytypedef)
- [InstanceTypeDef](./type_defs.md#instancetypedef)
- [KinesisDataStreamTypeDef](./type_defs.md#kinesisdatastreamtypedef)
- [KinesisVideoStreamTypeDef](./type_defs.md#kinesisvideostreamtypedef)
- [LabelDetectionTypeDef](./type_defs.md#labeldetectiontypedef)
- [LabelTypeDef](./type_defs.md#labeltypedef)
- [LandmarkTypeDef](./type_defs.md#landmarktypedef)
- [ModerationLabelTypeDef](./type_defs.md#moderationlabeltypedef)
- [MouthOpenTypeDef](./type_defs.md#mouthopentypedef)
- [MustacheTypeDef](./type_defs.md#mustachetypedef)
- [OutputConfigTypeDef](./type_defs.md#outputconfigtypedef)
- [ParentTypeDef](./type_defs.md#parenttypedef)
- [PersonDetailTypeDef](./type_defs.md#persondetailtypedef)
- [PersonDetectionTypeDef](./type_defs.md#persondetectiontypedef)
- [PersonMatchTypeDef](./type_defs.md#personmatchtypedef)
- [PointTypeDef](./type_defs.md#pointtypedef)
- [PoseTypeDef](./type_defs.md#posetypedef)
- [ProjectDescriptionTypeDef](./type_defs.md#projectdescriptiontypedef)
- [ProjectVersionDescriptionTypeDef](./type_defs.md#projectversiondescriptiontypedef)
- [ProtectiveEquipmentBodyPartTypeDef](./type_defs.md#protectiveequipmentbodyparttypedef)
- [ProtectiveEquipmentPersonTypeDef](./type_defs.md#protectiveequipmentpersontypedef)
- [ProtectiveEquipmentSummaryTypeDef](./type_defs.md#protectiveequipmentsummarytypedef)
- [RegionOfInterestTypeDef](./type_defs.md#regionofinteresttypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3ObjectTypeDef](./type_defs.md#s3objecttypedef)
- [SegmentDetectionTypeDef](./type_defs.md#segmentdetectiontypedef)
- [SegmentTypeInfoTypeDef](./type_defs.md#segmenttypeinfotypedef)
- [ShotSegmentTypeDef](./type_defs.md#shotsegmenttypedef)
- [SmileTypeDef](./type_defs.md#smiletypedef)
- [StartShotDetectionFilterTypeDef](./type_defs.md#startshotdetectionfiltertypedef)
- [StartTechnicalCueDetectionFilterTypeDef](./type_defs.md#starttechnicalcuedetectionfiltertypedef)
- [StreamProcessorInputTypeDef](./type_defs.md#streamprocessorinputtypedef)
- [StreamProcessorOutputTypeDef](./type_defs.md#streamprocessoroutputtypedef)
- [StreamProcessorSettingsTypeDef](./type_defs.md#streamprocessorsettingstypedef)
- [StreamProcessorTypeDef](./type_defs.md#streamprocessortypedef)
- [SummaryTypeDef](./type_defs.md#summarytypedef)
- [SunglassesTypeDef](./type_defs.md#sunglassestypedef)
- [TechnicalCueSegmentTypeDef](./type_defs.md#technicalcuesegmenttypedef)
- [TestingDataResultTypeDef](./type_defs.md#testingdataresulttypedef)
- [TestingDataTypeDef](./type_defs.md#testingdatatypedef)
- [TextDetectionResultTypeDef](./type_defs.md#textdetectionresulttypedef)
- [TextDetectionTypeDef](./type_defs.md#textdetectiontypedef)
- [TrainingDataResultTypeDef](./type_defs.md#trainingdataresulttypedef)
- [TrainingDataTypeDef](./type_defs.md#trainingdatatypedef)
- [UnindexedFaceTypeDef](./type_defs.md#unindexedfacetypedef)
- [ValidationDataTypeDef](./type_defs.md#validationdatatypedef)
- [VideoMetadataTypeDef](./type_defs.md#videometadatatypedef)
- [CompareFacesResponseTypeDef](./type_defs.md#comparefacesresponsetypedef)
- [CreateCollectionResponseTypeDef](./type_defs.md#createcollectionresponsetypedef)
- [CreateProjectResponseTypeDef](./type_defs.md#createprojectresponsetypedef)
- [CreateProjectVersionResponseTypeDef](./type_defs.md#createprojectversionresponsetypedef)
- [CreateStreamProcessorResponseTypeDef](./type_defs.md#createstreamprocessorresponsetypedef)
- [DeleteCollectionResponseTypeDef](./type_defs.md#deletecollectionresponsetypedef)
- [DeleteFacesResponseTypeDef](./type_defs.md#deletefacesresponsetypedef)
- [DeleteProjectResponseTypeDef](./type_defs.md#deleteprojectresponsetypedef)
- [DeleteProjectVersionResponseTypeDef](./type_defs.md#deleteprojectversionresponsetypedef)
- [DescribeCollectionResponseTypeDef](./type_defs.md#describecollectionresponsetypedef)
- [DescribeProjectVersionsResponseTypeDef](./type_defs.md#describeprojectversionsresponsetypedef)
- [DescribeProjectsResponseTypeDef](./type_defs.md#describeprojectsresponsetypedef)
- [DescribeStreamProcessorResponseTypeDef](./type_defs.md#describestreamprocessorresponsetypedef)
- [DetectCustomLabelsResponseTypeDef](./type_defs.md#detectcustomlabelsresponsetypedef)
- [DetectFacesResponseTypeDef](./type_defs.md#detectfacesresponsetypedef)
- [DetectLabelsResponseTypeDef](./type_defs.md#detectlabelsresponsetypedef)
- [DetectModerationLabelsResponseTypeDef](./type_defs.md#detectmoderationlabelsresponsetypedef)
- [DetectProtectiveEquipmentResponseTypeDef](./type_defs.md#detectprotectiveequipmentresponsetypedef)
- [DetectTextFiltersTypeDef](./type_defs.md#detecttextfilterstypedef)
- [DetectTextResponseTypeDef](./type_defs.md#detecttextresponsetypedef)
- [GetCelebrityInfoResponseTypeDef](./type_defs.md#getcelebrityinforesponsetypedef)
- [GetCelebrityRecognitionResponseTypeDef](./type_defs.md#getcelebrityrecognitionresponsetypedef)
- [GetContentModerationResponseTypeDef](./type_defs.md#getcontentmoderationresponsetypedef)
- [GetFaceDetectionResponseTypeDef](./type_defs.md#getfacedetectionresponsetypedef)
- [GetFaceSearchResponseTypeDef](./type_defs.md#getfacesearchresponsetypedef)
- [GetLabelDetectionResponseTypeDef](./type_defs.md#getlabeldetectionresponsetypedef)
- [GetPersonTrackingResponseTypeDef](./type_defs.md#getpersontrackingresponsetypedef)
- [GetSegmentDetectionResponseTypeDef](./type_defs.md#getsegmentdetectionresponsetypedef)
- [GetTextDetectionResponseTypeDef](./type_defs.md#gettextdetectionresponsetypedef)
- [HumanLoopConfigTypeDef](./type_defs.md#humanloopconfigtypedef)
- [ImageTypeDef](./type_defs.md#imagetypedef)
- [IndexFacesResponseTypeDef](./type_defs.md#indexfacesresponsetypedef)
- [ListCollectionsResponseTypeDef](./type_defs.md#listcollectionsresponsetypedef)
- [ListFacesResponseTypeDef](./type_defs.md#listfacesresponsetypedef)
- [ListStreamProcessorsResponseTypeDef](./type_defs.md#liststreamprocessorsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NotificationChannelTypeDef](./type_defs.md#notificationchanneltypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProtectiveEquipmentSummarizationAttributesTypeDef](./type_defs.md#protectiveequipmentsummarizationattributestypedef)
- [RecognizeCelebritiesResponseTypeDef](./type_defs.md#recognizecelebritiesresponsetypedef)
- [SearchFacesByImageResponseTypeDef](./type_defs.md#searchfacesbyimageresponsetypedef)
- [SearchFacesResponseTypeDef](./type_defs.md#searchfacesresponsetypedef)
- [StartCelebrityRecognitionResponseTypeDef](./type_defs.md#startcelebrityrecognitionresponsetypedef)
- [StartContentModerationResponseTypeDef](./type_defs.md#startcontentmoderationresponsetypedef)
- [StartFaceDetectionResponseTypeDef](./type_defs.md#startfacedetectionresponsetypedef)
- [StartFaceSearchResponseTypeDef](./type_defs.md#startfacesearchresponsetypedef)
- [StartLabelDetectionResponseTypeDef](./type_defs.md#startlabeldetectionresponsetypedef)
- [StartPersonTrackingResponseTypeDef](./type_defs.md#startpersontrackingresponsetypedef)
- [StartProjectVersionResponseTypeDef](./type_defs.md#startprojectversionresponsetypedef)
- [StartSegmentDetectionFiltersTypeDef](./type_defs.md#startsegmentdetectionfilterstypedef)
- [StartSegmentDetectionResponseTypeDef](./type_defs.md#startsegmentdetectionresponsetypedef)
- [StartTextDetectionFiltersTypeDef](./type_defs.md#starttextdetectionfilterstypedef)
- [StartTextDetectionResponseTypeDef](./type_defs.md#starttextdetectionresponsetypedef)
- [StopProjectVersionResponseTypeDef](./type_defs.md#stopprojectversionresponsetypedef)
- [VideoTypeDef](./type_defs.md#videotypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
