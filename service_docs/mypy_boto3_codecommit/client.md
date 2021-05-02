# CodeCommitClient for boto3 CodeCommit module

> [Index](../index.md) > [CodeCommit](./index.md) > CodeCommitClient

Auto-generated documentation for [CodeCommit](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit)
type annotations stubs module [mypy_boto3_codecommit](https://pypi.org/project/mypy-boto3-codecommit/).

- [CodeCommitClient for boto3 CodeCommit module](#codecommitclient-for-boto3-codecommit-module)
  - [CodeCommitClient](#codecommitclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_approval_rule_template_with_repository](#associate_approval_rule_template_with_repository)
    - [batch_associate_approval_rule_template_with_repositories](#batch_associate_approval_rule_template_with_repositories)
    - [batch_describe_merge_conflicts](#batch_describe_merge_conflicts)
    - [batch_disassociate_approval_rule_template_from_repositories](#batch_disassociate_approval_rule_template_from_repositories)
    - [batch_get_commits](#batch_get_commits)
    - [batch_get_repositories](#batch_get_repositories)
    - [can_paginate](#can_paginate)
    - [create_approval_rule_template](#create_approval_rule_template)
    - [create_branch](#create_branch)
    - [create_commit](#create_commit)
    - [create_pull_request](#create_pull_request)
    - [create_pull_request_approval_rule](#create_pull_request_approval_rule)
    - [create_repository](#create_repository)
    - [create_unreferenced_merge_commit](#create_unreferenced_merge_commit)
    - [delete_approval_rule_template](#delete_approval_rule_template)
    - [delete_branch](#delete_branch)
    - [delete_comment_content](#delete_comment_content)
    - [delete_file](#delete_file)
    - [delete_pull_request_approval_rule](#delete_pull_request_approval_rule)
    - [delete_repository](#delete_repository)
    - [describe_merge_conflicts](#describe_merge_conflicts)
    - [describe_pull_request_events](#describe_pull_request_events)
    - [disassociate_approval_rule_template_from_repository](#disassociate_approval_rule_template_from_repository)
    - [evaluate_pull_request_approval_rules](#evaluate_pull_request_approval_rules)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_approval_rule_template](#get_approval_rule_template)
    - [get_blob](#get_blob)
    - [get_branch](#get_branch)
    - [get_comment](#get_comment)
    - [get_comment_reactions](#get_comment_reactions)
    - [get_comments_for_compared_commit](#get_comments_for_compared_commit)
    - [get_comments_for_pull_request](#get_comments_for_pull_request)
    - [get_commit](#get_commit)
    - [get_differences](#get_differences)
    - [get_file](#get_file)
    - [get_folder](#get_folder)
    - [get_merge_commit](#get_merge_commit)
    - [get_merge_conflicts](#get_merge_conflicts)
    - [get_merge_options](#get_merge_options)
    - [get_pull_request](#get_pull_request)
    - [get_pull_request_approval_states](#get_pull_request_approval_states)
    - [get_pull_request_override_state](#get_pull_request_override_state)
    - [get_repository](#get_repository)
    - [get_repository_triggers](#get_repository_triggers)
    - [list_approval_rule_templates](#list_approval_rule_templates)
    - [list_associated_approval_rule_templates_for_repository](#list_associated_approval_rule_templates_for_repository)
    - [list_branches](#list_branches)
    - [list_pull_requests](#list_pull_requests)
    - [list_repositories](#list_repositories)
    - [list_repositories_for_approval_rule_template](#list_repositories_for_approval_rule_template)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [merge_branches_by_fast_forward](#merge_branches_by_fast_forward)
    - [merge_branches_by_squash](#merge_branches_by_squash)
    - [merge_branches_by_three_way](#merge_branches_by_three_way)
    - [merge_pull_request_by_fast_forward](#merge_pull_request_by_fast_forward)
    - [merge_pull_request_by_squash](#merge_pull_request_by_squash)
    - [merge_pull_request_by_three_way](#merge_pull_request_by_three_way)
    - [override_pull_request_approval_rules](#override_pull_request_approval_rules)
    - [post_comment_for_compared_commit](#post_comment_for_compared_commit)
    - [post_comment_for_pull_request](#post_comment_for_pull_request)
    - [post_comment_reply](#post_comment_reply)
    - [put_comment_reaction](#put_comment_reaction)
    - [put_file](#put_file)
    - [put_repository_triggers](#put_repository_triggers)
    - [tag_resource](#tag_resource)
    - [test_repository_triggers](#test_repository_triggers)
    - [untag_resource](#untag_resource)
    - [update_approval_rule_template_content](#update_approval_rule_template_content)
    - [update_approval_rule_template_description](#update_approval_rule_template_description)
    - [update_approval_rule_template_name](#update_approval_rule_template_name)
    - [update_comment](#update_comment)
    - [update_default_branch](#update_default_branch)
    - [update_pull_request_approval_rule_content](#update_pull_request_approval_rule_content)
    - [update_pull_request_approval_state](#update_pull_request_approval_state)
    - [update_pull_request_description](#update_pull_request_description)
    - [update_pull_request_status](#update_pull_request_status)
    - [update_pull_request_title](#update_pull_request_title)
    - [update_repository_description](#update_repository_description)
    - [update_repository_name](#update_repository_name)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## CodeCommitClient

Type annotations for `boto3.client("codecommit")`

Can be used directly:

```python
from mypy_boto3_codecommit.client import CodeCommitClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codecommit.client import Exceptions

def handle_error(exc: Exceptions.ActorDoesNotExistException) -> None:
    ...
```


Exceptions:

- `Exceptions.ActorDoesNotExistException`
- `Exceptions.ApprovalRuleContentRequiredException`
- `Exceptions.ApprovalRuleDoesNotExistException`
- `Exceptions.ApprovalRuleNameAlreadyExistsException`
- `Exceptions.ApprovalRuleNameRequiredException`
- `Exceptions.ApprovalRuleTemplateContentRequiredException`
- `Exceptions.ApprovalRuleTemplateDoesNotExistException`
- `Exceptions.ApprovalRuleTemplateInUseException`
- `Exceptions.ApprovalRuleTemplateNameAlreadyExistsException`
- `Exceptions.ApprovalRuleTemplateNameRequiredException`
- `Exceptions.ApprovalStateRequiredException`
- `Exceptions.AuthorDoesNotExistException`
- `Exceptions.BeforeCommitIdAndAfterCommitIdAreSameException`
- `Exceptions.BlobIdDoesNotExistException`
- `Exceptions.BlobIdRequiredException`
- `Exceptions.BranchDoesNotExistException`
- `Exceptions.BranchNameExistsException`
- `Exceptions.BranchNameIsTagNameException`
- `Exceptions.BranchNameRequiredException`
- `Exceptions.CannotDeleteApprovalRuleFromTemplateException`
- `Exceptions.CannotModifyApprovalRuleFromTemplateException`
- `Exceptions.ClientError`
- `Exceptions.ClientRequestTokenRequiredException`
- `Exceptions.CommentContentRequiredException`
- `Exceptions.CommentContentSizeLimitExceededException`
- `Exceptions.CommentDeletedException`
- `Exceptions.CommentDoesNotExistException`
- `Exceptions.CommentIdRequiredException`
- `Exceptions.CommentNotCreatedByCallerException`
- `Exceptions.CommitDoesNotExistException`
- `Exceptions.CommitIdDoesNotExistException`
- `Exceptions.CommitIdRequiredException`
- `Exceptions.CommitIdsLimitExceededException`
- `Exceptions.CommitIdsListRequiredException`
- `Exceptions.CommitMessageLengthExceededException`
- `Exceptions.CommitRequiredException`
- `Exceptions.ConcurrentReferenceUpdateException`
- `Exceptions.DefaultBranchCannotBeDeletedException`
- `Exceptions.DirectoryNameConflictsWithFileNameException`
- `Exceptions.EncryptionIntegrityChecksFailedException`
- `Exceptions.EncryptionKeyAccessDeniedException`
- `Exceptions.EncryptionKeyDisabledException`
- `Exceptions.EncryptionKeyNotFoundException`
- `Exceptions.EncryptionKeyUnavailableException`
- `Exceptions.FileContentAndSourceFileSpecifiedException`
- `Exceptions.FileContentRequiredException`
- `Exceptions.FileContentSizeLimitExceededException`
- `Exceptions.FileDoesNotExistException`
- `Exceptions.FileEntryRequiredException`
- `Exceptions.FileModeRequiredException`
- `Exceptions.FileNameConflictsWithDirectoryNameException`
- `Exceptions.FilePathConflictsWithSubmodulePathException`
- `Exceptions.FileTooLargeException`
- `Exceptions.FolderContentSizeLimitExceededException`
- `Exceptions.FolderDoesNotExistException`
- `Exceptions.IdempotencyParameterMismatchException`
- `Exceptions.InvalidActorArnException`
- `Exceptions.InvalidApprovalRuleContentException`
- `Exceptions.InvalidApprovalRuleNameException`
- `Exceptions.InvalidApprovalRuleTemplateContentException`
- `Exceptions.InvalidApprovalRuleTemplateDescriptionException`
- `Exceptions.InvalidApprovalRuleTemplateNameException`
- `Exceptions.InvalidApprovalStateException`
- `Exceptions.InvalidAuthorArnException`
- `Exceptions.InvalidBlobIdException`
- `Exceptions.InvalidBranchNameException`
- `Exceptions.InvalidClientRequestTokenException`
- `Exceptions.InvalidCommentIdException`
- `Exceptions.InvalidCommitException`
- `Exceptions.InvalidCommitIdException`
- `Exceptions.InvalidConflictDetailLevelException`
- `Exceptions.InvalidConflictResolutionException`
- `Exceptions.InvalidConflictResolutionStrategyException`
- `Exceptions.InvalidContinuationTokenException`
- `Exceptions.InvalidDeletionParameterException`
- `Exceptions.InvalidDescriptionException`
- `Exceptions.InvalidDestinationCommitSpecifierException`
- `Exceptions.InvalidEmailException`
- `Exceptions.InvalidFileLocationException`
- `Exceptions.InvalidFileModeException`
- `Exceptions.InvalidFilePositionException`
- `Exceptions.InvalidMaxConflictFilesException`
- `Exceptions.InvalidMaxMergeHunksException`
- `Exceptions.InvalidMaxResultsException`
- `Exceptions.InvalidMergeOptionException`
- `Exceptions.InvalidOrderException`
- `Exceptions.InvalidOverrideStatusException`
- `Exceptions.InvalidParentCommitIdException`
- `Exceptions.InvalidPathException`
- `Exceptions.InvalidPullRequestEventTypeException`
- `Exceptions.InvalidPullRequestIdException`
- `Exceptions.InvalidPullRequestStatusException`
- `Exceptions.InvalidPullRequestStatusUpdateException`
- `Exceptions.InvalidReactionUserArnException`
- `Exceptions.InvalidReactionValueException`
- `Exceptions.InvalidReferenceNameException`
- `Exceptions.InvalidRelativeFileVersionEnumException`
- `Exceptions.InvalidReplacementContentException`
- `Exceptions.InvalidReplacementTypeException`
- `Exceptions.InvalidRepositoryDescriptionException`
- `Exceptions.InvalidRepositoryNameException`
- `Exceptions.InvalidRepositoryTriggerBranchNameException`
- `Exceptions.InvalidRepositoryTriggerCustomDataException`
- `Exceptions.InvalidRepositoryTriggerDestinationArnException`
- `Exceptions.InvalidRepositoryTriggerEventsException`
- `Exceptions.InvalidRepositoryTriggerNameException`
- `Exceptions.InvalidRepositoryTriggerRegionException`
- `Exceptions.InvalidResourceArnException`
- `Exceptions.InvalidRevisionIdException`
- `Exceptions.InvalidRuleContentSha256Exception`
- `Exceptions.InvalidSortByException`
- `Exceptions.InvalidSourceCommitSpecifierException`
- `Exceptions.InvalidSystemTagUsageException`
- `Exceptions.InvalidTagKeysListException`
- `Exceptions.InvalidTagsMapException`
- `Exceptions.InvalidTargetBranchException`
- `Exceptions.InvalidTargetException`
- `Exceptions.InvalidTargetsException`
- `Exceptions.InvalidTitleException`
- `Exceptions.ManualMergeRequiredException`
- `Exceptions.MaximumBranchesExceededException`
- `Exceptions.MaximumConflictResolutionEntriesExceededException`
- `Exceptions.MaximumFileContentToLoadExceededException`
- `Exceptions.MaximumFileEntriesExceededException`
- `Exceptions.MaximumItemsToCompareExceededException`
- `Exceptions.MaximumNumberOfApprovalsExceededException`
- `Exceptions.MaximumOpenPullRequestsExceededException`
- `Exceptions.MaximumRepositoryNamesExceededException`
- `Exceptions.MaximumRepositoryTriggersExceededException`
- `Exceptions.MaximumRuleTemplatesAssociatedWithRepositoryException`
- `Exceptions.MergeOptionRequiredException`
- `Exceptions.MultipleConflictResolutionEntriesException`
- `Exceptions.MultipleRepositoriesInPullRequestException`
- `Exceptions.NameLengthExceededException`
- `Exceptions.NoChangeException`
- `Exceptions.NumberOfRuleTemplatesExceededException`
- `Exceptions.NumberOfRulesExceededException`
- `Exceptions.OverrideAlreadySetException`
- `Exceptions.OverrideStatusRequiredException`
- `Exceptions.ParentCommitDoesNotExistException`
- `Exceptions.ParentCommitIdOutdatedException`
- `Exceptions.ParentCommitIdRequiredException`
- `Exceptions.PathDoesNotExistException`
- `Exceptions.PathRequiredException`
- `Exceptions.PullRequestAlreadyClosedException`
- `Exceptions.PullRequestApprovalRulesNotSatisfiedException`
- `Exceptions.PullRequestCannotBeApprovedByAuthorException`
- `Exceptions.PullRequestDoesNotExistException`
- `Exceptions.PullRequestIdRequiredException`
- `Exceptions.PullRequestStatusRequiredException`
- `Exceptions.PutFileEntryConflictException`
- `Exceptions.ReactionLimitExceededException`
- `Exceptions.ReactionValueRequiredException`
- `Exceptions.ReferenceDoesNotExistException`
- `Exceptions.ReferenceNameRequiredException`
- `Exceptions.ReferenceTypeNotSupportedException`
- `Exceptions.ReplacementContentRequiredException`
- `Exceptions.ReplacementTypeRequiredException`
- `Exceptions.RepositoryDoesNotExistException`
- `Exceptions.RepositoryLimitExceededException`
- `Exceptions.RepositoryNameExistsException`
- `Exceptions.RepositoryNameRequiredException`
- `Exceptions.RepositoryNamesRequiredException`
- `Exceptions.RepositoryNotAssociatedWithPullRequestException`
- `Exceptions.RepositoryTriggerBranchNameListRequiredException`
- `Exceptions.RepositoryTriggerDestinationArnRequiredException`
- `Exceptions.RepositoryTriggerEventsListRequiredException`
- `Exceptions.RepositoryTriggerNameRequiredException`
- `Exceptions.RepositoryTriggersListRequiredException`
- `Exceptions.ResourceArnRequiredException`
- `Exceptions.RestrictedSourceFileException`
- `Exceptions.RevisionIdRequiredException`
- `Exceptions.RevisionNotCurrentException`
- `Exceptions.SameFileContentException`
- `Exceptions.SamePathRequestException`
- `Exceptions.SourceAndDestinationAreSameException`
- `Exceptions.SourceFileOrContentRequiredException`
- `Exceptions.TagKeysListRequiredException`
- `Exceptions.TagPolicyException`
- `Exceptions.TagsMapRequiredException`
- `Exceptions.TargetRequiredException`
- `Exceptions.TargetsRequiredException`
- `Exceptions.TipOfSourceReferenceIsDifferentException`
- `Exceptions.TipsDivergenceExceededException`
- `Exceptions.TitleRequiredException`
- `Exceptions.TooManyTagsException`


## Methods


### associate_approval_rule_template_with_repository

Type annotations for `boto3.client("codecommit").associate_approval_rule_template_with_repository` method.

[Client.associate_approval_rule_template_with_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.associate_approval_rule_template_with_repository)

```python
def associate_approval_rule_template_with_repository(
    self,
    approvalRuleTemplateName: str,
    repositoryName: str
) -> None:
    pass
```

### batch_associate_approval_rule_template_with_repositories

Type annotations for `boto3.client("codecommit").batch_associate_approval_rule_template_with_repositories` method.

[Client.batch_associate_approval_rule_template_with_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.batch_associate_approval_rule_template_with_repositories)

```python
def batch_associate_approval_rule_template_with_repositories(
    self,
    approvalRuleTemplateName: str,
    repositoryNames: List[str]
) -> BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef:
    pass
```

### batch_describe_merge_conflicts

Type annotations for `boto3.client("codecommit").batch_describe_merge_conflicts` method.

[Client.batch_describe_merge_conflicts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.batch_describe_merge_conflicts)

```python
def batch_describe_merge_conflicts(
    self,
    repositoryName: str,
    destinationCommitSpecifier: str,
    sourceCommitSpecifier: str,
    mergeOption: MergeOptionTypeEnum,
    maxMergeHunks: int = None,
    maxConflictFiles: int = None,
    filePaths: List[str] = None,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    nextToken: str = None
) -> BatchDescribeMergeConflictsOutputTypeDef:
    pass
```

### batch_disassociate_approval_rule_template_from_repositories

Type annotations for `boto3.client("codecommit").batch_disassociate_approval_rule_template_from_repositories` method.

[Client.batch_disassociate_approval_rule_template_from_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.batch_disassociate_approval_rule_template_from_repositories)

```python
def batch_disassociate_approval_rule_template_from_repositories(
    self,
    approvalRuleTemplateName: str,
    repositoryNames: List[str]
) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef:
    pass
```

### batch_get_commits

Type annotations for `boto3.client("codecommit").batch_get_commits` method.

[Client.batch_get_commits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.batch_get_commits)

```python
def batch_get_commits(
    self,
    commitIds: List[str],
    repositoryName: str
) -> BatchGetCommitsOutputTypeDef:
    pass
```

### batch_get_repositories

Type annotations for `boto3.client("codecommit").batch_get_repositories` method.

[Client.batch_get_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.batch_get_repositories)

```python
def batch_get_repositories(
    self,
    repositoryNames: List[str]
) -> BatchGetRepositoriesOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codecommit").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_approval_rule_template

Type annotations for `boto3.client("codecommit").create_approval_rule_template` method.

[Client.create_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_approval_rule_template)

```python
def create_approval_rule_template(
    self,
    approvalRuleTemplateName: str,
    approvalRuleTemplateContent: str,
    approvalRuleTemplateDescription: str = None
) -> CreateApprovalRuleTemplateOutputTypeDef:
    pass
```

### create_branch

Type annotations for `boto3.client("codecommit").create_branch` method.

[Client.create_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_branch)

```python
def create_branch(
    self,
    repositoryName: str,
    branchName: str,
    commitId: str
) -> None:
    pass
```

### create_commit

Type annotations for `boto3.client("codecommit").create_commit` method.

[Client.create_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_commit)

```python
def create_commit(
    self,
    repositoryName: str,
    branchName: str,
    parentCommitId: str = None,
    authorName: str = None,
    email: str = None,
    commitMessage: str = None,
    keepEmptyFolders: bool = None,
    putFiles: List[PutFileEntryTypeDef] = None,
    deleteFiles: List["DeleteFileEntryTypeDef"] = None,
    setFileModes: List["SetFileModeEntryTypeDef"] = None
) -> CreateCommitOutputTypeDef:
    pass
```

### create_pull_request

Type annotations for `boto3.client("codecommit").create_pull_request` method.

[Client.create_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_pull_request)

```python
def create_pull_request(
    self,
    title: str,
    targets: List[TargetTypeDef],
    description: str = None,
    clientRequestToken: str = None
) -> CreatePullRequestOutputTypeDef:
    pass
```

### create_pull_request_approval_rule

Type annotations for `boto3.client("codecommit").create_pull_request_approval_rule` method.

[Client.create_pull_request_approval_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_pull_request_approval_rule)

```python
def create_pull_request_approval_rule(
    self,
    pullRequestId: str,
    approvalRuleName: str,
    approvalRuleContent: str
) -> CreatePullRequestApprovalRuleOutputTypeDef:
    pass
```

### create_repository

Type annotations for `boto3.client("codecommit").create_repository` method.

[Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_repository)

```python
def create_repository(
    self,
    repositoryName: str,
    repositoryDescription: str = None,
    tags: Dict[str, str] = None
) -> CreateRepositoryOutputTypeDef:
    pass
```

### create_unreferenced_merge_commit

Type annotations for `boto3.client("codecommit").create_unreferenced_merge_commit` method.

[Client.create_unreferenced_merge_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.create_unreferenced_merge_commit)

```python
def create_unreferenced_merge_commit(
    self,
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    mergeOption: MergeOptionTypeEnum,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    authorName: str = None,
    email: str = None,
    commitMessage: str = None,
    keepEmptyFolders: bool = None,
    conflictResolution: ConflictResolutionTypeDef = None
) -> CreateUnreferencedMergeCommitOutputTypeDef:
    pass
```

### delete_approval_rule_template

Type annotations for `boto3.client("codecommit").delete_approval_rule_template` method.

[Client.delete_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.delete_approval_rule_template)

```python
def delete_approval_rule_template(
    self,
    approvalRuleTemplateName: str
) -> DeleteApprovalRuleTemplateOutputTypeDef:
    pass
```

### delete_branch

Type annotations for `boto3.client("codecommit").delete_branch` method.

[Client.delete_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.delete_branch)

```python
def delete_branch(
    self,
    repositoryName: str,
    branchName: str
) -> DeleteBranchOutputTypeDef:
    pass
```

### delete_comment_content

Type annotations for `boto3.client("codecommit").delete_comment_content` method.

[Client.delete_comment_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.delete_comment_content)

```python
def delete_comment_content(
    self,
    commentId: str
) -> DeleteCommentContentOutputTypeDef:
    pass
```

### delete_file

Type annotations for `boto3.client("codecommit").delete_file` method.

[Client.delete_file documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.delete_file)

```python
def delete_file(
    self,
    repositoryName: str,
    branchName: str,
    filePath: str,
    parentCommitId: str,
    keepEmptyFolders: bool = None,
    commitMessage: str = None,
    name: str = None,
    email: str = None
) -> DeleteFileOutputTypeDef:
    pass
```

### delete_pull_request_approval_rule

Type annotations for `boto3.client("codecommit").delete_pull_request_approval_rule` method.

[Client.delete_pull_request_approval_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.delete_pull_request_approval_rule)

```python
def delete_pull_request_approval_rule(
    self,
    pullRequestId: str,
    approvalRuleName: str
) -> DeletePullRequestApprovalRuleOutputTypeDef:
    pass
```

### delete_repository

Type annotations for `boto3.client("codecommit").delete_repository` method.

[Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.delete_repository)

```python
def delete_repository(
    self,
    repositoryName: str
) -> DeleteRepositoryOutputTypeDef:
    pass
```

### describe_merge_conflicts

Type annotations for `boto3.client("codecommit").describe_merge_conflicts` method.

[Client.describe_merge_conflicts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.describe_merge_conflicts)

```python
def describe_merge_conflicts(
    self,
    repositoryName: str,
    destinationCommitSpecifier: str,
    sourceCommitSpecifier: str,
    mergeOption: MergeOptionTypeEnum,
    filePath: str,
    maxMergeHunks: int = None,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    nextToken: str = None
) -> DescribeMergeConflictsOutputTypeDef:
    pass
```

### describe_pull_request_events

Type annotations for `boto3.client("codecommit").describe_pull_request_events` method.

[Client.describe_pull_request_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.describe_pull_request_events)

```python
def describe_pull_request_events(
    self,
    pullRequestId: str,
    pullRequestEventType: PullRequestEventType = None,
    actorArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribePullRequestEventsOutputTypeDef:
    pass
```

### disassociate_approval_rule_template_from_repository

Type annotations for `boto3.client("codecommit").disassociate_approval_rule_template_from_repository` method.

[Client.disassociate_approval_rule_template_from_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.disassociate_approval_rule_template_from_repository)

```python
def disassociate_approval_rule_template_from_repository(
    self,
    approvalRuleTemplateName: str,
    repositoryName: str
) -> None:
    pass
```

### evaluate_pull_request_approval_rules

Type annotations for `boto3.client("codecommit").evaluate_pull_request_approval_rules` method.

[Client.evaluate_pull_request_approval_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.evaluate_pull_request_approval_rules)

```python
def evaluate_pull_request_approval_rules(
    self,
    pullRequestId: str,
    revisionId: str
) -> EvaluatePullRequestApprovalRulesOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codecommit").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.generate_presigned_url)

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

### get_approval_rule_template

Type annotations for `boto3.client("codecommit").get_approval_rule_template` method.

[Client.get_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_approval_rule_template)

```python
def get_approval_rule_template(
    self,
    approvalRuleTemplateName: str
) -> GetApprovalRuleTemplateOutputTypeDef:
    pass
```

### get_blob

Type annotations for `boto3.client("codecommit").get_blob` method.

[Client.get_blob documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_blob)

```python
def get_blob(
    self,
    repositoryName: str,
    blobId: str
) -> GetBlobOutputTypeDef:
    pass
```

### get_branch

Type annotations for `boto3.client("codecommit").get_branch` method.

[Client.get_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_branch)

```python
def get_branch(
    self,
    repositoryName: str = None,
    branchName: str = None
) -> GetBranchOutputTypeDef:
    pass
```

### get_comment

Type annotations for `boto3.client("codecommit").get_comment` method.

[Client.get_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_comment)

```python
def get_comment(
    self,
    commentId: str
) -> GetCommentOutputTypeDef:
    pass
```

### get_comment_reactions

Type annotations for `boto3.client("codecommit").get_comment_reactions` method.

[Client.get_comment_reactions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_comment_reactions)

```python
def get_comment_reactions(
    self,
    commentId: str,
    reactionUserArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetCommentReactionsOutputTypeDef:
    pass
```

### get_comments_for_compared_commit

Type annotations for `boto3.client("codecommit").get_comments_for_compared_commit` method.

[Client.get_comments_for_compared_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_compared_commit)

```python
def get_comments_for_compared_commit(
    self,
    repositoryName: str,
    afterCommitId: str,
    beforeCommitId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetCommentsForComparedCommitOutputTypeDef:
    pass
```

### get_comments_for_pull_request

Type annotations for `boto3.client("codecommit").get_comments_for_pull_request` method.

[Client.get_comments_for_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_comments_for_pull_request)

```python
def get_comments_for_pull_request(
    self,
    pullRequestId: str,
    repositoryName: str = None,
    beforeCommitId: str = None,
    afterCommitId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetCommentsForPullRequestOutputTypeDef:
    pass
```

### get_commit

Type annotations for `boto3.client("codecommit").get_commit` method.

[Client.get_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_commit)

```python
def get_commit(
    self,
    repositoryName: str,
    commitId: str
) -> GetCommitOutputTypeDef:
    pass
```

### get_differences

Type annotations for `boto3.client("codecommit").get_differences` method.

[Client.get_differences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_differences)

```python
def get_differences(
    self,
    repositoryName: str,
    afterCommitSpecifier: str,
    beforeCommitSpecifier: str = None,
    beforePath: str = None,
    afterPath: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetDifferencesOutputTypeDef:
    pass
```

### get_file

Type annotations for `boto3.client("codecommit").get_file` method.

[Client.get_file documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_file)

```python
def get_file(
    self,
    repositoryName: str,
    filePath: str,
    commitSpecifier: str = None
) -> GetFileOutputTypeDef:
    pass
```

### get_folder

Type annotations for `boto3.client("codecommit").get_folder` method.

[Client.get_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_folder)

```python
def get_folder(
    self,
    repositoryName: str,
    folderPath: str,
    commitSpecifier: str = None
) -> GetFolderOutputTypeDef:
    pass
```

### get_merge_commit

Type annotations for `boto3.client("codecommit").get_merge_commit` method.

[Client.get_merge_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_merge_commit)

```python
def get_merge_commit(
    self,
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None
) -> GetMergeCommitOutputTypeDef:
    pass
```

### get_merge_conflicts

Type annotations for `boto3.client("codecommit").get_merge_conflicts` method.

[Client.get_merge_conflicts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_merge_conflicts)

```python
def get_merge_conflicts(
    self,
    repositoryName: str,
    destinationCommitSpecifier: str,
    sourceCommitSpecifier: str,
    mergeOption: MergeOptionTypeEnum,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    maxConflictFiles: int = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    nextToken: str = None
) -> GetMergeConflictsOutputTypeDef:
    pass
```

### get_merge_options

Type annotations for `boto3.client("codecommit").get_merge_options` method.

[Client.get_merge_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_merge_options)

```python
def get_merge_options(
    self,
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None
) -> GetMergeOptionsOutputTypeDef:
    pass
```

### get_pull_request

Type annotations for `boto3.client("codecommit").get_pull_request` method.

[Client.get_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_pull_request)

```python
def get_pull_request(
    self,
    pullRequestId: str
) -> GetPullRequestOutputTypeDef:
    pass
```

### get_pull_request_approval_states

Type annotations for `boto3.client("codecommit").get_pull_request_approval_states` method.

[Client.get_pull_request_approval_states documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_approval_states)

```python
def get_pull_request_approval_states(
    self,
    pullRequestId: str,
    revisionId: str
) -> GetPullRequestApprovalStatesOutputTypeDef:
    pass
```

### get_pull_request_override_state

Type annotations for `boto3.client("codecommit").get_pull_request_override_state` method.

[Client.get_pull_request_override_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_pull_request_override_state)

```python
def get_pull_request_override_state(
    self,
    pullRequestId: str,
    revisionId: str
) -> GetPullRequestOverrideStateOutputTypeDef:
    pass
```

### get_repository

Type annotations for `boto3.client("codecommit").get_repository` method.

[Client.get_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_repository)

```python
def get_repository(
    self,
    repositoryName: str
) -> GetRepositoryOutputTypeDef:
    pass
```

### get_repository_triggers

Type annotations for `boto3.client("codecommit").get_repository_triggers` method.

[Client.get_repository_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_repository_triggers)

```python
def get_repository_triggers(
    self,
    repositoryName: str
) -> GetRepositoryTriggersOutputTypeDef:
    pass
```

### list_approval_rule_templates

Type annotations for `boto3.client("codecommit").list_approval_rule_templates` method.

[Client.list_approval_rule_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_approval_rule_templates)

```python
def list_approval_rule_templates(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListApprovalRuleTemplatesOutputTypeDef:
    pass
```

### list_associated_approval_rule_templates_for_repository

Type annotations for `boto3.client("codecommit").list_associated_approval_rule_templates_for_repository` method.

[Client.list_associated_approval_rule_templates_for_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_associated_approval_rule_templates_for_repository)

```python
def list_associated_approval_rule_templates_for_repository(
    self,
    repositoryName: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef:
    pass
```

### list_branches

Type annotations for `boto3.client("codecommit").list_branches` method.

[Client.list_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_branches)

```python
def list_branches(
    self,
    repositoryName: str,
    nextToken: str = None
) -> ListBranchesOutputTypeDef:
    pass
```

### list_pull_requests

Type annotations for `boto3.client("codecommit").list_pull_requests` method.

[Client.list_pull_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_pull_requests)

```python
def list_pull_requests(
    self,
    repositoryName: str,
    authorArn: str = None,
    pullRequestStatus: PullRequestStatusEnum = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListPullRequestsOutputTypeDef:
    pass
```

### list_repositories

Type annotations for `boto3.client("codecommit").list_repositories` method.

[Client.list_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_repositories)

```python
def list_repositories(
    self,
    nextToken: str = None,
    sortBy: SortByEnum = None,
    order: OrderEnum = None
) -> ListRepositoriesOutputTypeDef:
    pass
```

### list_repositories_for_approval_rule_template

Type annotations for `boto3.client("codecommit").list_repositories_for_approval_rule_template` method.

[Client.list_repositories_for_approval_rule_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_repositories_for_approval_rule_template)

```python
def list_repositories_for_approval_rule_template(
    self,
    approvalRuleTemplateName: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListRepositoriesForApprovalRuleTemplateOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codecommit").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str,
    nextToken: str = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### merge_branches_by_fast_forward

Type annotations for `boto3.client("codecommit").merge_branches_by_fast_forward` method.

[Client.merge_branches_by_fast_forward documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_fast_forward)

```python
def merge_branches_by_fast_forward(
    self,
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    targetBranch: str = None
) -> MergeBranchesByFastForwardOutputTypeDef:
    pass
```

### merge_branches_by_squash

Type annotations for `boto3.client("codecommit").merge_branches_by_squash` method.

[Client.merge_branches_by_squash documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_squash)

```python
def merge_branches_by_squash(
    self,
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    targetBranch: str = None,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    authorName: str = None,
    email: str = None,
    commitMessage: str = None,
    keepEmptyFolders: bool = None,
    conflictResolution: ConflictResolutionTypeDef = None
) -> MergeBranchesBySquashOutputTypeDef:
    pass
```

### merge_branches_by_three_way

Type annotations for `boto3.client("codecommit").merge_branches_by_three_way` method.

[Client.merge_branches_by_three_way documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.merge_branches_by_three_way)

```python
def merge_branches_by_three_way(
    self,
    repositoryName: str,
    sourceCommitSpecifier: str,
    destinationCommitSpecifier: str,
    targetBranch: str = None,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    authorName: str = None,
    email: str = None,
    commitMessage: str = None,
    keepEmptyFolders: bool = None,
    conflictResolution: ConflictResolutionTypeDef = None
) -> MergeBranchesByThreeWayOutputTypeDef:
    pass
```

### merge_pull_request_by_fast_forward

Type annotations for `boto3.client("codecommit").merge_pull_request_by_fast_forward` method.

[Client.merge_pull_request_by_fast_forward documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_fast_forward)

```python
def merge_pull_request_by_fast_forward(
    self,
    pullRequestId: str,
    repositoryName: str,
    sourceCommitId: str = None
) -> MergePullRequestByFastForwardOutputTypeDef:
    pass
```

### merge_pull_request_by_squash

Type annotations for `boto3.client("codecommit").merge_pull_request_by_squash` method.

[Client.merge_pull_request_by_squash documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_squash)

```python
def merge_pull_request_by_squash(
    self,
    pullRequestId: str,
    repositoryName: str,
    sourceCommitId: str = None,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    commitMessage: str = None,
    authorName: str = None,
    email: str = None,
    keepEmptyFolders: bool = None,
    conflictResolution: ConflictResolutionTypeDef = None
) -> MergePullRequestBySquashOutputTypeDef:
    pass
```

### merge_pull_request_by_three_way

Type annotations for `boto3.client("codecommit").merge_pull_request_by_three_way` method.

[Client.merge_pull_request_by_three_way documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.merge_pull_request_by_three_way)

```python
def merge_pull_request_by_three_way(
    self,
    pullRequestId: str,
    repositoryName: str,
    sourceCommitId: str = None,
    conflictDetailLevel: ConflictDetailLevelTypeEnum = None,
    conflictResolutionStrategy: ConflictResolutionStrategyTypeEnum = None,
    commitMessage: str = None,
    authorName: str = None,
    email: str = None,
    keepEmptyFolders: bool = None,
    conflictResolution: ConflictResolutionTypeDef = None
) -> MergePullRequestByThreeWayOutputTypeDef:
    pass
```

### override_pull_request_approval_rules

Type annotations for `boto3.client("codecommit").override_pull_request_approval_rules` method.

[Client.override_pull_request_approval_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.override_pull_request_approval_rules)

```python
def override_pull_request_approval_rules(
    self,
    pullRequestId: str,
    revisionId: str,
    overrideStatus: OverrideStatus
) -> None:
    pass
```

### post_comment_for_compared_commit

Type annotations for `boto3.client("codecommit").post_comment_for_compared_commit` method.

[Client.post_comment_for_compared_commit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_compared_commit)

```python
def post_comment_for_compared_commit(
    self,
    repositoryName: str,
    afterCommitId: str,
    content: str,
    beforeCommitId: str = None,
    location: "LocationTypeDef" = None,
    clientRequestToken: str = None
) -> PostCommentForComparedCommitOutputTypeDef:
    pass
```

### post_comment_for_pull_request

Type annotations for `boto3.client("codecommit").post_comment_for_pull_request` method.

[Client.post_comment_for_pull_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.post_comment_for_pull_request)

```python
def post_comment_for_pull_request(
    self,
    pullRequestId: str,
    repositoryName: str,
    beforeCommitId: str,
    afterCommitId: str,
    content: str,
    location: "LocationTypeDef" = None,
    clientRequestToken: str = None
) -> PostCommentForPullRequestOutputTypeDef:
    pass
```

### post_comment_reply

Type annotations for `boto3.client("codecommit").post_comment_reply` method.

[Client.post_comment_reply documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.post_comment_reply)

```python
def post_comment_reply(
    self,
    inReplyTo: str,
    content: str,
    clientRequestToken: str = None
) -> PostCommentReplyOutputTypeDef:
    pass
```

### put_comment_reaction

Type annotations for `boto3.client("codecommit").put_comment_reaction` method.

[Client.put_comment_reaction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.put_comment_reaction)

```python
def put_comment_reaction(
    self,
    commentId: str,
    reactionValue: str
) -> None:
    pass
```

### put_file

Type annotations for `boto3.client("codecommit").put_file` method.

[Client.put_file documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.put_file)

```python
def put_file(
    self,
    repositoryName: str,
    branchName: str,
    fileContent: Union[bytes, IO[bytes]],
    filePath: str,
    fileMode: FileModeTypeEnum = None,
    parentCommitId: str = None,
    commitMessage: str = None,
    name: str = None,
    email: str = None
) -> PutFileOutputTypeDef:
    pass
```

### put_repository_triggers

Type annotations for `boto3.client("codecommit").put_repository_triggers` method.

[Client.put_repository_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.put_repository_triggers)

```python
def put_repository_triggers(
    self,
    repositoryName: str,
    triggers: List["RepositoryTriggerTypeDef"]
) -> PutRepositoryTriggersOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("codecommit").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> None:
    pass
```

### test_repository_triggers

Type annotations for `boto3.client("codecommit").test_repository_triggers` method.

[Client.test_repository_triggers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.test_repository_triggers)

```python
def test_repository_triggers(
    self,
    repositoryName: str,
    triggers: List["RepositoryTriggerTypeDef"]
) -> TestRepositoryTriggersOutputTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("codecommit").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> None:
    pass
```

### update_approval_rule_template_content

Type annotations for `boto3.client("codecommit").update_approval_rule_template_content` method.

[Client.update_approval_rule_template_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_content)

```python
def update_approval_rule_template_content(
    self,
    approvalRuleTemplateName: str,
    newRuleContent: str,
    existingRuleContentSha256: str = None
) -> UpdateApprovalRuleTemplateContentOutputTypeDef:
    pass
```

### update_approval_rule_template_description

Type annotations for `boto3.client("codecommit").update_approval_rule_template_description` method.

[Client.update_approval_rule_template_description documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_description)

```python
def update_approval_rule_template_description(
    self,
    approvalRuleTemplateName: str,
    approvalRuleTemplateDescription: str
) -> UpdateApprovalRuleTemplateDescriptionOutputTypeDef:
    pass
```

### update_approval_rule_template_name

Type annotations for `boto3.client("codecommit").update_approval_rule_template_name` method.

[Client.update_approval_rule_template_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_approval_rule_template_name)

```python
def update_approval_rule_template_name(
    self,
    oldApprovalRuleTemplateName: str,
    newApprovalRuleTemplateName: str
) -> UpdateApprovalRuleTemplateNameOutputTypeDef:
    pass
```

### update_comment

Type annotations for `boto3.client("codecommit").update_comment` method.

[Client.update_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_comment)

```python
def update_comment(
    self,
    commentId: str,
    content: str
) -> UpdateCommentOutputTypeDef:
    pass
```

### update_default_branch

Type annotations for `boto3.client("codecommit").update_default_branch` method.

[Client.update_default_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_default_branch)

```python
def update_default_branch(
    self,
    repositoryName: str,
    defaultBranchName: str
) -> None:
    pass
```

### update_pull_request_approval_rule_content

Type annotations for `boto3.client("codecommit").update_pull_request_approval_rule_content` method.

[Client.update_pull_request_approval_rule_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_rule_content)

```python
def update_pull_request_approval_rule_content(
    self,
    pullRequestId: str,
    approvalRuleName: str,
    newRuleContent: str,
    existingRuleContentSha256: str = None
) -> UpdatePullRequestApprovalRuleContentOutputTypeDef:
    pass
```

### update_pull_request_approval_state

Type annotations for `boto3.client("codecommit").update_pull_request_approval_state` method.

[Client.update_pull_request_approval_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_approval_state)

```python
def update_pull_request_approval_state(
    self,
    pullRequestId: str,
    revisionId: str,
    approvalState: ApprovalState
) -> None:
    pass
```

### update_pull_request_description

Type annotations for `boto3.client("codecommit").update_pull_request_description` method.

[Client.update_pull_request_description documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_description)

```python
def update_pull_request_description(
    self,
    pullRequestId: str,
    description: str
) -> UpdatePullRequestDescriptionOutputTypeDef:
    pass
```

### update_pull_request_status

Type annotations for `boto3.client("codecommit").update_pull_request_status` method.

[Client.update_pull_request_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_status)

```python
def update_pull_request_status(
    self,
    pullRequestId: str,
    pullRequestStatus: PullRequestStatusEnum
) -> UpdatePullRequestStatusOutputTypeDef:
    pass
```

### update_pull_request_title

Type annotations for `boto3.client("codecommit").update_pull_request_title` method.

[Client.update_pull_request_title documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_pull_request_title)

```python
def update_pull_request_title(
    self,
    pullRequestId: str,
    title: str
) -> UpdatePullRequestTitleOutputTypeDef:
    pass
```

### update_repository_description

Type annotations for `boto3.client("codecommit").update_repository_description` method.

[Client.update_repository_description documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_repository_description)

```python
def update_repository_description(
    self,
    repositoryName: str,
    repositoryDescription: str = None
) -> None:
    pass
```

### update_repository_name

Type annotations for `boto3.client("codecommit").update_repository_name` method.

[Client.update_repository_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.update_repository_name)

```python
def update_repository_name(
    self,
    oldName: str,
    newName: str
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.DescribePullRequestEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.DescribePullRequestEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePullRequestEventsPaginatorName
) -> DescribePullRequestEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.GetCommentsForComparedCommit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForComparedCommit)

```python
@overload
def get_paginator(
    self,
    operation_name: GetCommentsForComparedCommitPaginatorName
) -> GetCommentsForComparedCommitPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.GetCommentsForPullRequest documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.GetCommentsForPullRequest)

```python
@overload
def get_paginator(
    self,
    operation_name: GetCommentsForPullRequestPaginatorName
) -> GetCommentsForPullRequestPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.GetDifferences documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.GetDifferences)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDifferencesPaginatorName
) -> GetDifferencesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.ListBranches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.ListBranches)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBranchesPaginatorName
) -> ListBranchesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.ListPullRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.ListPullRequests)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPullRequestsPaginatorName
) -> ListPullRequestsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codecommit").get_paginator` method.

[Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Paginator.ListRepositories)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRepositoriesPaginatorName
) -> ListRepositoriesPaginator:
    pass
```