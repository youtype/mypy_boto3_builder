# CodeGuruReviewerClient for boto3 CodeGuruReviewer module

> [Index](../index.md) > [CodeGuruReviewer](./index.md) > CodeGuruReviewerClient

Auto-generated documentation for [CodeGuruReviewer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer)
type annotations stubs module [mypy_boto3_codeguru_reviewer](https://pypi.org/project/mypy-boto3-codeguru-reviewer/).

- [CodeGuruReviewerClient for boto3 CodeGuruReviewer module](#codegurureviewerclient-for-boto3-codegurureviewer-module)
  - [CodeGuruReviewerClient](#codegurureviewerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_repository](#associate_repository)
    - [can_paginate](#can_paginate)
    - [create_code_review](#create_code_review)
    - [describe_code_review](#describe_code_review)
    - [describe_recommendation_feedback](#describe_recommendation_feedback)
    - [describe_repository_association](#describe_repository_association)
    - [disassociate_repository](#disassociate_repository)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_code_reviews](#list_code_reviews)
    - [list_recommendation_feedback](#list_recommendation_feedback)
    - [list_recommendations](#list_recommendations)
    - [list_repository_associations](#list_repository_associations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_recommendation_feedback](#put_recommendation_feedback)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)

## CodeGuruReviewerClient

Type annotations for `boto3.client("codeguru-reviewer")`

Can be used directly:

```python
from mypy_boto3_codeguru_reviewer.client import CodeGuruReviewerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codeguru_reviewer.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### associate_repository

Type annotations for `boto3.client("codeguru-reviewer").associate_repository` method.

[Client.associate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)

```python
def associate_repository(
    self,
    Repository: RepositoryTypeDef,
    ClientRequestToken: str = None,
    Tags: Dict[str, str] = None,
    KMSKeyDetails: "KMSKeyDetailsTypeDef" = None
) -> AssociateRepositoryResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codeguru-reviewer").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_code_review

Type annotations for `boto3.client("codeguru-reviewer").create_code_review` method.

[Client.create_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.create_code_review)

```python
def create_code_review(
    self,
    Name: str,
    RepositoryAssociationArn: str,
    Type: CodeReviewTypeTypeDef,
    ClientRequestToken: str = None
) -> CreateCodeReviewResponseTypeDef:
    pass
```

### describe_code_review

Type annotations for `boto3.client("codeguru-reviewer").describe_code_review` method.

[Client.describe_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_code_review)

```python
def describe_code_review(
    self,
    CodeReviewArn: str
) -> DescribeCodeReviewResponseTypeDef:
    pass
```

### describe_recommendation_feedback

Type annotations for `boto3.client("codeguru-reviewer").describe_recommendation_feedback` method.

[Client.describe_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_recommendation_feedback)

```python
def describe_recommendation_feedback(
    self,
    CodeReviewArn: str,
    RecommendationId: str,
    UserId: str = None
) -> DescribeRecommendationFeedbackResponseTypeDef:
    pass
```

### describe_repository_association

Type annotations for `boto3.client("codeguru-reviewer").describe_repository_association` method.

[Client.describe_repository_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)

```python
def describe_repository_association(
    self,
    AssociationArn: str
) -> DescribeRepositoryAssociationResponseTypeDef:
    pass
```

### disassociate_repository

Type annotations for `boto3.client("codeguru-reviewer").disassociate_repository` method.

[Client.disassociate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)

```python
def disassociate_repository(
    self,
    AssociationArn: str
) -> DisassociateRepositoryResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codeguru-reviewer").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)

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

### list_code_reviews

Type annotations for `boto3.client("codeguru-reviewer").list_code_reviews` method.

[Client.list_code_reviews documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_code_reviews)

```python
def list_code_reviews(
    self,
    Type: TypeType,
    ProviderTypes: List[ProviderType] = None,
    States: List[JobState] = None,
    RepositoryNames: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCodeReviewsResponseTypeDef:
    pass
```

### list_recommendation_feedback

Type annotations for `boto3.client("codeguru-reviewer").list_recommendation_feedback` method.

[Client.list_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendation_feedback)

```python
def list_recommendation_feedback(
    self,
    CodeReviewArn: str,
    NextToken: str = None,
    MaxResults: int = None,
    UserIds: List[str] = None,
    RecommendationIds: List[str] = None
) -> ListRecommendationFeedbackResponseTypeDef:
    pass
```

### list_recommendations

Type annotations for `boto3.client("codeguru-reviewer").list_recommendations` method.

[Client.list_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendations)

```python
def list_recommendations(
    self,
    CodeReviewArn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListRecommendationsResponseTypeDef:
    pass
```

### list_repository_associations

Type annotations for `boto3.client("codeguru-reviewer").list_repository_associations` method.

[Client.list_repository_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)

```python
def list_repository_associations(
    self,
    ProviderTypes: List[ProviderType] = None,
    States: List[RepositoryAssociationState] = None,
    Names: List[str] = None,
    Owners: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRepositoryAssociationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codeguru-reviewer").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_recommendation_feedback

Type annotations for `boto3.client("codeguru-reviewer").put_recommendation_feedback` method.

[Client.put_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.put_recommendation_feedback)

```python
def put_recommendation_feedback(
    self,
    CodeReviewArn: str,
    RecommendationId: str,
    Reactions: List[Reaction]
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("codeguru-reviewer").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("codeguru-reviewer").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("codeguru-reviewer").get_paginator` method with overloads.

- `client.get_paginator("list_repository_associations")` -> [ListRepositoryAssociationsPaginator](./paginators.md#listrepositoryassociationspaginator)


