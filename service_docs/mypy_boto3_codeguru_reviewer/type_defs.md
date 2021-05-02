# Structures for boto3 CodeGuruReviewer module

> [Index](../index.md) > [CodeGuruReviewer](./index.md) > Structures

Auto-generated documentation for [CodeGuruReviewer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer)
type annotations stubs module [mypy_boto3_codeguru_reviewer](https://pypi.org/project/mypy-boto3-codeguru-reviewer/).

- [Structures for boto3 CodeGuruReviewer module](#structures-for-boto3-codegurureviewer-module)
  - [CodeCommitRepositoryTypeDef](#codecommitrepositorytypedef)
  - [CodeReviewSummaryTypeDef](#codereviewsummarytypedef)
  - [CodeReviewTypeDef](#codereviewtypedef)
  - [CommitDiffSourceCodeTypeTypeDef](#commitdiffsourcecodetypetypedef)
  - [KMSKeyDetailsTypeDef](#kmskeydetailstypedef)
  - [MetricsSummaryTypeDef](#metricssummarytypedef)
  - [MetricsTypeDef](#metricstypedef)
  - [RecommendationFeedbackSummaryTypeDef](#recommendationfeedbacksummarytypedef)
  - [RecommendationFeedbackTypeDef](#recommendationfeedbacktypedef)
  - [RecommendationSummaryTypeDef](#recommendationsummarytypedef)
  - [RepositoryAnalysisTypeDef](#repositoryanalysistypedef)
  - [RepositoryAssociationSummaryTypeDef](#repositoryassociationsummarytypedef)
  - [RepositoryAssociationTypeDef](#repositoryassociationtypedef)
  - [RepositoryHeadSourceCodeTypeTypeDef](#repositoryheadsourcecodetypetypedef)
  - [SourceCodeTypeTypeDef](#sourcecodetypetypedef)
  - [ThirdPartySourceRepositoryTypeDef](#thirdpartysourcerepositorytypedef)
  - [AssociateRepositoryResponseTypeDef](#associaterepositoryresponsetypedef)
  - [CodeReviewTypeTypeDef](#codereviewtypetypedef)
  - [CreateCodeReviewResponseTypeDef](#createcodereviewresponsetypedef)
  - [DescribeCodeReviewResponseTypeDef](#describecodereviewresponsetypedef)
  - [DescribeRecommendationFeedbackResponseTypeDef](#describerecommendationfeedbackresponsetypedef)
  - [DescribeRepositoryAssociationResponseTypeDef](#describerepositoryassociationresponsetypedef)
  - [DisassociateRepositoryResponseTypeDef](#disassociaterepositoryresponsetypedef)
  - [ListCodeReviewsResponseTypeDef](#listcodereviewsresponsetypedef)
  - [ListRecommendationFeedbackResponseTypeDef](#listrecommendationfeedbackresponsetypedef)
  - [ListRecommendationsResponseTypeDef](#listrecommendationsresponsetypedef)
  - [ListRepositoryAssociationsResponseTypeDef](#listrepositoryassociationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RepositoryTypeDef](#repositorytypedef)

## CodeCommitRepositoryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import CodeCommitRepositoryTypeDef
```


Required fields:
- `Name`: `str`




## CodeReviewSummaryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import CodeReviewSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `CodeReviewArn`: `str`
- `RepositoryName`: `str`
- `Owner`: `str`
- `ProviderType`: `ProviderType`
- `State`: `JobState`
- `CreatedTimeStamp`: `datetime`
- `LastUpdatedTimeStamp`: `datetime`
- `Type`: `TypeType`
- `PullRequestId`: `str`
- `MetricsSummary`: `"MetricsSummaryTypeDef"`


## CodeReviewTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import CodeReviewTypeDef
```




Optional fields:
- `Name`: `str`
- `CodeReviewArn`: `str`
- `RepositoryName`: `str`
- `Owner`: `str`
- `ProviderType`: `ProviderType`
- `State`: `JobState`
- `StateReason`: `str`
- `CreatedTimeStamp`: `datetime`
- `LastUpdatedTimeStamp`: `datetime`
- `Type`: `TypeType`
- `PullRequestId`: `str`
- `SourceCodeType`: `"SourceCodeTypeTypeDef"`
- `AssociationArn`: `str`
- `Metrics`: `"MetricsTypeDef"`


## CommitDiffSourceCodeTypeTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import CommitDiffSourceCodeTypeTypeDef
```




Optional fields:
- `SourceCommit`: `str`
- `DestinationCommit`: `str`


## KMSKeyDetailsTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import KMSKeyDetailsTypeDef
```




Optional fields:
- `KMSKeyId`: `str`
- `EncryptionOption`: `EncryptionOption`


## MetricsSummaryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import MetricsSummaryTypeDef
```




Optional fields:
- `MeteredLinesOfCodeCount`: `int`
- `FindingsCount`: `int`


## MetricsTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import MetricsTypeDef
```




Optional fields:
- `MeteredLinesOfCodeCount`: `int`
- `FindingsCount`: `int`


## RecommendationFeedbackSummaryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RecommendationFeedbackSummaryTypeDef
```




Optional fields:
- `RecommendationId`: `str`
- `Reactions`: `List[Reaction]`
- `UserId`: `str`


## RecommendationFeedbackTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RecommendationFeedbackTypeDef
```




Optional fields:
- `CodeReviewArn`: `str`
- `RecommendationId`: `str`
- `Reactions`: `List[Reaction]`
- `UserId`: `str`
- `CreatedTimeStamp`: `datetime`
- `LastUpdatedTimeStamp`: `datetime`


## RecommendationSummaryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RecommendationSummaryTypeDef
```




Optional fields:
- `FilePath`: `str`
- `RecommendationId`: `str`
- `StartLine`: `int`
- `EndLine`: `int`
- `Description`: `str`


## RepositoryAnalysisTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RepositoryAnalysisTypeDef
```


Required fields:
- `RepositoryHead`: `"RepositoryHeadSourceCodeTypeTypeDef"`




## RepositoryAssociationSummaryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RepositoryAssociationSummaryTypeDef
```




Optional fields:
- `AssociationArn`: `str`
- `ConnectionArn`: `str`
- `LastUpdatedTimeStamp`: `datetime`
- `AssociationId`: `str`
- `Name`: `str`
- `Owner`: `str`
- `ProviderType`: `ProviderType`
- `State`: `RepositoryAssociationState`


## RepositoryAssociationTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RepositoryAssociationTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `AssociationArn`: `str`
- `ConnectionArn`: `str`
- `Name`: `str`
- `Owner`: `str`
- `ProviderType`: `ProviderType`
- `State`: `RepositoryAssociationState`
- `StateReason`: `str`
- `LastUpdatedTimeStamp`: `datetime`
- `CreatedTimeStamp`: `datetime`
- `KMSKeyDetails`: `"KMSKeyDetailsTypeDef"`


## RepositoryHeadSourceCodeTypeTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RepositoryHeadSourceCodeTypeTypeDef
```


Required fields:
- `BranchName`: `str`




## SourceCodeTypeTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import SourceCodeTypeTypeDef
```




Optional fields:
- `CommitDiff`: `"CommitDiffSourceCodeTypeTypeDef"`
- `RepositoryHead`: `"RepositoryHeadSourceCodeTypeTypeDef"`


## ThirdPartySourceRepositoryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import ThirdPartySourceRepositoryTypeDef
```


Required fields:
- `Name`: `str`
- `ConnectionArn`: `str`
- `Owner`: `str`




## AssociateRepositoryResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import AssociateRepositoryResponseTypeDef
```




Optional fields:
- `RepositoryAssociation`: `"RepositoryAssociationTypeDef"`
- `Tags`: `Dict[str, str]`


## CodeReviewTypeTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import CodeReviewTypeTypeDef
```


Required fields:
- `RepositoryAnalysis`: `"RepositoryAnalysisTypeDef"`




## CreateCodeReviewResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import CreateCodeReviewResponseTypeDef
```




Optional fields:
- `CodeReview`: `"CodeReviewTypeDef"`


## DescribeCodeReviewResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import DescribeCodeReviewResponseTypeDef
```




Optional fields:
- `CodeReview`: `"CodeReviewTypeDef"`


## DescribeRecommendationFeedbackResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import DescribeRecommendationFeedbackResponseTypeDef
```




Optional fields:
- `RecommendationFeedback`: `"RecommendationFeedbackTypeDef"`


## DescribeRepositoryAssociationResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import DescribeRepositoryAssociationResponseTypeDef
```




Optional fields:
- `RepositoryAssociation`: `"RepositoryAssociationTypeDef"`
- `Tags`: `Dict[str, str]`


## DisassociateRepositoryResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import DisassociateRepositoryResponseTypeDef
```




Optional fields:
- `RepositoryAssociation`: `"RepositoryAssociationTypeDef"`
- `Tags`: `Dict[str, str]`


## ListCodeReviewsResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import ListCodeReviewsResponseTypeDef
```




Optional fields:
- `CodeReviewSummaries`: `List["CodeReviewSummaryTypeDef"]`
- `NextToken`: `str`


## ListRecommendationFeedbackResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import ListRecommendationFeedbackResponseTypeDef
```




Optional fields:
- `RecommendationFeedbackSummaries`: `List["RecommendationFeedbackSummaryTypeDef"]`
- `NextToken`: `str`


## ListRecommendationsResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import ListRecommendationsResponseTypeDef
```




Optional fields:
- `RecommendationSummaries`: `List["RecommendationSummaryTypeDef"]`
- `NextToken`: `str`


## ListRepositoryAssociationsResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import ListRepositoryAssociationsResponseTypeDef
```




Optional fields:
- `RepositoryAssociationSummaries`: `List["RepositoryAssociationSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RepositoryTypeDef

```python
from mypy_boto3_codeguru_reviewer.type_defs import RepositoryTypeDef
```




Optional fields:
- `CodeCommit`: `"CodeCommitRepositoryTypeDef"`
- `Bitbucket`: `"ThirdPartySourceRepositoryTypeDef"`
- `GitHubEnterpriseServer`: `"ThirdPartySourceRepositoryTypeDef"`

