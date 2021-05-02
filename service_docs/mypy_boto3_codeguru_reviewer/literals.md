# Literals for boto3 CodeGuruReviewer module

> [Index](../index.md) > [CodeGuruReviewer](./index.md) > Literals

Auto-generated documentation for [CodeGuruReviewer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html#CodeGuruReviewer)
type annotations stubs module [mypy_boto3_codeguru_reviewer](https://pypi.org/project/mypy-boto3-codeguru-reviewer/).

- [Literals for boto3 CodeGuruReviewer module](#literals-for-boto3-codegurureviewer-module)
  - [EncryptionOption](#encryptionoption)
  - [JobState](#jobstate)
  - [ListRepositoryAssociationsPaginatorName](#listrepositoryassociationspaginatorname)
  - [ProviderType](#providertype)
  - [Reaction](#reaction)
  - [RepositoryAssociationState](#repositoryassociationstate)
  - [TypeType](#typetype)

## EncryptionOption

```python
from mypy_boto3_codeguru_reviewer.literals import EncryptionOption
```

Values:

- `AWS_OWNED_CMK`
- `CUSTOMER_MANAGED_CMK`

## JobState

```python
from mypy_boto3_codeguru_reviewer.literals import JobState
```

Values:

- `Completed`
- `Deleting`
- `Failed`
- `Pending`

## ListRepositoryAssociationsPaginatorName

```python
from mypy_boto3_codeguru_reviewer.literals import ListRepositoryAssociationsPaginatorName
```

Values:

- `list_repository_associations`

## ProviderType

```python
from mypy_boto3_codeguru_reviewer.literals import ProviderType
```

Values:

- `Bitbucket`
- `CodeCommit`
- `GitHub`
- `GitHubEnterpriseServer`

## Reaction

```python
from mypy_boto3_codeguru_reviewer.literals import Reaction
```

Values:

- `ThumbsDown`
- `ThumbsUp`

## RepositoryAssociationState

```python
from mypy_boto3_codeguru_reviewer.literals import RepositoryAssociationState
```

Values:

- `Associated`
- `Associating`
- `Disassociated`
- `Disassociating`
- `Failed`

## TypeType

```python
from mypy_boto3_codeguru_reviewer.literals import TypeType
```

Values:

- `PullRequest`
- `RepositoryAnalysis`
