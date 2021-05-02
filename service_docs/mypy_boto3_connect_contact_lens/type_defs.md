# Structures for boto3 ConnectContactLens module

> [Index](../index.md) > [ConnectContactLens](./index.md) > Structures

Auto-generated documentation for [ConnectContactLens](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html#ConnectContactLens)
type annotations stubs module [mypy_boto3_connect_contact_lens](https://pypi.org/project/mypy-boto3-connect-contact-lens/).

- [Structures for boto3 ConnectContactLens module](#structures-for-boto3-connectcontactlens-module)
  - [CategoriesTypeDef](#categoriestypedef)
  - [CategoryDetailsTypeDef](#categorydetailstypedef)
  - [CharacterOffsetsTypeDef](#characteroffsetstypedef)
  - [IssueDetectedTypeDef](#issuedetectedtypedef)
  - [PointOfInterestTypeDef](#pointofinteresttypedef)
  - [RealtimeContactAnalysisSegmentTypeDef](#realtimecontactanalysissegmenttypedef)
  - [TranscriptTypeDef](#transcripttypedef)
  - [ListRealtimeContactAnalysisSegmentsResponseTypeDef](#listrealtimecontactanalysissegmentsresponsetypedef)

## CategoriesTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import CategoriesTypeDef
```


Required fields:
- `MatchedCategories`: `List[str]`
- `MatchedDetails`: `Dict[str, "CategoryDetailsTypeDef"]`




## CategoryDetailsTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import CategoryDetailsTypeDef
```


Required fields:
- `PointsOfInterest`: `List["PointOfInterestTypeDef"]`




## CharacterOffsetsTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import CharacterOffsetsTypeDef
```


Required fields:
- `BeginOffsetChar`: `int`
- `EndOffsetChar`: `int`




## IssueDetectedTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import IssueDetectedTypeDef
```


Required fields:
- `CharacterOffsets`: `"CharacterOffsetsTypeDef"`




## PointOfInterestTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import PointOfInterestTypeDef
```


Required fields:
- `BeginOffsetMillis`: `int`
- `EndOffsetMillis`: `int`




## RealtimeContactAnalysisSegmentTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import RealtimeContactAnalysisSegmentTypeDef
```




Optional fields:
- `Transcript`: `"TranscriptTypeDef"`
- `Categories`: `"CategoriesTypeDef"`


## TranscriptTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import TranscriptTypeDef
```


Required fields:
- `Id`: `str`
- `ParticipantId`: `str`
- `ParticipantRole`: `str`
- `Content`: `str`
- `BeginOffsetMillis`: `int`
- `EndOffsetMillis`: `int`
- `Sentiment`: `SentimentValue`



Optional fields:
- `IssuesDetected`: `List["IssueDetectedTypeDef"]`


## ListRealtimeContactAnalysisSegmentsResponseTypeDef

```python
from mypy_boto3_connect_contact_lens.type_defs import ListRealtimeContactAnalysisSegmentsResponseTypeDef
```


Required fields:
- `Segments`: `List["RealtimeContactAnalysisSegmentTypeDef"]`



Optional fields:
- `NextToken`: `str`

