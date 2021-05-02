# Literals for boto3 CodeCommit module

> [Index](../index.md) > [CodeCommit](./index.md) > Literals

Auto-generated documentation for [CodeCommit](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit)
type annotations stubs module [mypy_boto3_codecommit](https://pypi.org/project/mypy-boto3-codecommit/).

- [Literals for boto3 CodeCommit module](#literals-for-boto3-codecommit-module)
  - [ApprovalState](#approvalstate)
  - [ChangeTypeEnum](#changetypeenum)
  - [ConflictDetailLevelTypeEnum](#conflictdetailleveltypeenum)
  - [ConflictResolutionStrategyTypeEnum](#conflictresolutionstrategytypeenum)
  - [DescribePullRequestEventsPaginatorName](#describepullrequesteventspaginatorname)
  - [FileModeTypeEnum](#filemodetypeenum)
  - [GetCommentsForComparedCommitPaginatorName](#getcommentsforcomparedcommitpaginatorname)
  - [GetCommentsForPullRequestPaginatorName](#getcommentsforpullrequestpaginatorname)
  - [GetDifferencesPaginatorName](#getdifferencespaginatorname)
  - [ListBranchesPaginatorName](#listbranchespaginatorname)
  - [ListPullRequestsPaginatorName](#listpullrequestspaginatorname)
  - [ListRepositoriesPaginatorName](#listrepositoriespaginatorname)
  - [MergeOptionTypeEnum](#mergeoptiontypeenum)
  - [ObjectTypeEnum](#objecttypeenum)
  - [OrderEnum](#orderenum)
  - [OverrideStatus](#overridestatus)
  - [PullRequestEventType](#pullrequesteventtype)
  - [PullRequestStatusEnum](#pullrequeststatusenum)
  - [RelativeFileVersionEnum](#relativefileversionenum)
  - [ReplacementTypeEnum](#replacementtypeenum)
  - [RepositoryTriggerEventEnum](#repositorytriggereventenum)
  - [SortByEnum](#sortbyenum)

## ApprovalState

```python
from mypy_boto3_codecommit.literals import ApprovalState
```

Values:

- `APPROVE`
- `REVOKE`

## ChangeTypeEnum

```python
from mypy_boto3_codecommit.literals import ChangeTypeEnum
```

Values:

- `A`
- `D`
- `M`

## ConflictDetailLevelTypeEnum

```python
from mypy_boto3_codecommit.literals import ConflictDetailLevelTypeEnum
```

Values:

- `FILE_LEVEL`
- `LINE_LEVEL`

## ConflictResolutionStrategyTypeEnum

```python
from mypy_boto3_codecommit.literals import ConflictResolutionStrategyTypeEnum
```

Values:

- `ACCEPT_DESTINATION`
- `ACCEPT_SOURCE`
- `AUTOMERGE`
- `NONE`

## DescribePullRequestEventsPaginatorName

```python
from mypy_boto3_codecommit.literals import DescribePullRequestEventsPaginatorName
```

Values:

- `describe_pull_request_events`

## FileModeTypeEnum

```python
from mypy_boto3_codecommit.literals import FileModeTypeEnum
```

Values:

- `EXECUTABLE`
- `NORMAL`
- `SYMLINK`

## GetCommentsForComparedCommitPaginatorName

```python
from mypy_boto3_codecommit.literals import GetCommentsForComparedCommitPaginatorName
```

Values:

- `get_comments_for_compared_commit`

## GetCommentsForPullRequestPaginatorName

```python
from mypy_boto3_codecommit.literals import GetCommentsForPullRequestPaginatorName
```

Values:

- `get_comments_for_pull_request`

## GetDifferencesPaginatorName

```python
from mypy_boto3_codecommit.literals import GetDifferencesPaginatorName
```

Values:

- `get_differences`

## ListBranchesPaginatorName

```python
from mypy_boto3_codecommit.literals import ListBranchesPaginatorName
```

Values:

- `list_branches`

## ListPullRequestsPaginatorName

```python
from mypy_boto3_codecommit.literals import ListPullRequestsPaginatorName
```

Values:

- `list_pull_requests`

## ListRepositoriesPaginatorName

```python
from mypy_boto3_codecommit.literals import ListRepositoriesPaginatorName
```

Values:

- `list_repositories`

## MergeOptionTypeEnum

```python
from mypy_boto3_codecommit.literals import MergeOptionTypeEnum
```

Values:

- `FAST_FORWARD_MERGE`
- `SQUASH_MERGE`
- `THREE_WAY_MERGE`

## ObjectTypeEnum

```python
from mypy_boto3_codecommit.literals import ObjectTypeEnum
```

Values:

- `DIRECTORY`
- `FILE`
- `GIT_LINK`
- `SYMBOLIC_LINK`

## OrderEnum

```python
from mypy_boto3_codecommit.literals import OrderEnum
```

Values:

- `ascending`
- `descending`

## OverrideStatus

```python
from mypy_boto3_codecommit.literals import OverrideStatus
```

Values:

- `OVERRIDE`
- `REVOKE`

## PullRequestEventType

```python
from mypy_boto3_codecommit.literals import PullRequestEventType
```

Values:

- `PULL_REQUEST_APPROVAL_RULE_CREATED`
- `PULL_REQUEST_APPROVAL_RULE_DELETED`
- `PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN`
- `PULL_REQUEST_APPROVAL_RULE_UPDATED`
- `PULL_REQUEST_APPROVAL_STATE_CHANGED`
- `PULL_REQUEST_CREATED`
- `PULL_REQUEST_MERGE_STATE_CHANGED`
- `PULL_REQUEST_SOURCE_REFERENCE_UPDATED`
- `PULL_REQUEST_STATUS_CHANGED`

## PullRequestStatusEnum

```python
from mypy_boto3_codecommit.literals import PullRequestStatusEnum
```

Values:

- `CLOSED`
- `OPEN`

## RelativeFileVersionEnum

```python
from mypy_boto3_codecommit.literals import RelativeFileVersionEnum
```

Values:

- `AFTER`
- `BEFORE`

## ReplacementTypeEnum

```python
from mypy_boto3_codecommit.literals import ReplacementTypeEnum
```

Values:

- `KEEP_BASE`
- `KEEP_DESTINATION`
- `KEEP_SOURCE`
- `USE_NEW_CONTENT`

## RepositoryTriggerEventEnum

```python
from mypy_boto3_codecommit.literals import RepositoryTriggerEventEnum
```

Values:

- `all`
- `createReference`
- `deleteReference`
- `updateReference`

## SortByEnum

```python
from mypy_boto3_codecommit.literals import SortByEnum
```

Values:

- `lastModifiedDate`
- `repositoryName`
