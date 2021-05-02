# Type annotations for boto3 Textract module

> [Index](../index.md) > Textract

Auto-generated documentation for [Textract](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract)
type annotations stubs module [mypy_boto3_textract](https://pypi.org/project/mypy-boto3-textract/).

```bash
pip install mypy-boto3-textract
```

- [Type annotations for boto3 Textract module](#type-annotations-for-boto3-textract-module)
  - [TextractClient](#textractclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## TextractClient

Type annotations for  `boto3.client("textract")` as [TextractClient](./client.md)

Can be used directly:

```python
from mypy_boto3_textract.client import TextractClient
```


TextractClient [exceptions](./client.md#exceptions)



### Methods
- [analyze_document](./client.md#analyze-document)
- [can_paginate](./client.md#can-paginate)
- [detect_document_text](./client.md#detect-document-text)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_document_analysis](./client.md#get-document-analysis)
- [get_document_text_detection](./client.md#get-document-text-detection)
- [start_document_analysis](./client.md#start-document-analysis)
- [start_document_text_detection](./client.md#start-document-text-detection)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BadDocumentException](./client.md#baddocumentexception)
- [ClientError](./client.md#clienterror)
- [DocumentTooLargeException](./client.md#documenttoolargeexception)
- [HumanLoopQuotaExceededException](./client.md#humanloopquotaexceededexception)
- [IdempotentParameterMismatchException](./client.md#idempotentparametermismatchexception)
- [InternalServerError](./client.md#internalservererror)
- [InvalidJobIdException](./client.md#invalidjobidexception)
- [InvalidKMSKeyException](./client.md#invalidkmskeyexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidS3ObjectException](./client.md#invalids3objectexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ProvisionedThroughputExceededException](./client.md#provisionedthroughputexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [UnsupportedDocumentException](./client.md#unsupporteddocumentexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_textract.literals import BlockType, ...
```

- [BlockType](./literals.md#blocktype)
- [ContentClassifier](./literals.md#contentclassifier)
- [EntityType](./literals.md#entitytype)
- [FeatureType](./literals.md#featuretype)
- [JobStatus](./literals.md#jobstatus)
- [RelationshipType](./literals.md#relationshiptype)
- [SelectionStatus](./literals.md#selectionstatus)
- [TextType](./literals.md#texttype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_textract.type_defs import AnalyzeDocumentResponseTypeDef, ...
```

- [AnalyzeDocumentResponseTypeDef](./type_defs.md#analyzedocumentresponsetypedef)
- [BlockTypeDef](./type_defs.md#blocktypedef)
- [BoundingBoxTypeDef](./type_defs.md#boundingboxtypedef)
- [DetectDocumentTextResponseTypeDef](./type_defs.md#detectdocumenttextresponsetypedef)
- [DocumentLocationTypeDef](./type_defs.md#documentlocationtypedef)
- [DocumentMetadataTypeDef](./type_defs.md#documentmetadatatypedef)
- [DocumentTypeDef](./type_defs.md#documenttypedef)
- [GeometryTypeDef](./type_defs.md#geometrytypedef)
- [GetDocumentAnalysisResponseTypeDef](./type_defs.md#getdocumentanalysisresponsetypedef)
- [GetDocumentTextDetectionResponseTypeDef](./type_defs.md#getdocumenttextdetectionresponsetypedef)
- [HumanLoopActivationOutputTypeDef](./type_defs.md#humanloopactivationoutputtypedef)
- [HumanLoopConfigTypeDef](./type_defs.md#humanloopconfigtypedef)
- [HumanLoopDataAttributesTypeDef](./type_defs.md#humanloopdataattributestypedef)
- [NotificationChannelTypeDef](./type_defs.md#notificationchanneltypedef)
- [OutputConfigTypeDef](./type_defs.md#outputconfigtypedef)
- [PointTypeDef](./type_defs.md#pointtypedef)
- [RelationshipTypeDef](./type_defs.md#relationshiptypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3ObjectTypeDef](./type_defs.md#s3objecttypedef)
- [StartDocumentAnalysisResponseTypeDef](./type_defs.md#startdocumentanalysisresponsetypedef)
- [StartDocumentTextDetectionResponseTypeDef](./type_defs.md#startdocumenttextdetectionresponsetypedef)
- [WarningTypeDef](./type_defs.md#warningtypedef)
