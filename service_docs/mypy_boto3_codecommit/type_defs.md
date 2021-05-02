# Structures for boto3 CodeCommit module

> [Index](../index.md) > [CodeCommit](./index.md) > Structures

Auto-generated documentation for [CodeCommit](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit)
type annotations stubs module [mypy_boto3_codecommit](https://pypi.org/project/mypy-boto3-codecommit/).

- [Structures for boto3 CodeCommit module](#structures-for-boto3-codecommit-module)
  - [ApprovalRuleEventMetadataTypeDef](#approvalruleeventmetadatatypedef)
  - [ApprovalRuleOverriddenEventMetadataTypeDef](#approvalruleoverriddeneventmetadatatypedef)
  - [ApprovalRuleTemplateTypeDef](#approvalruletemplatetypedef)
  - [ApprovalRuleTypeDef](#approvalruletypedef)
  - [ApprovalStateChangedEventMetadataTypeDef](#approvalstatechangedeventmetadatatypedef)
  - [ApprovalTypeDef](#approvaltypedef)
  - [BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef](#batchassociateapprovalruletemplatewithrepositorieserrortypedef)
  - [BatchDescribeMergeConflictsErrorTypeDef](#batchdescribemergeconflictserrortypedef)
  - [BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef](#batchdisassociateapprovalruletemplatefromrepositorieserrortypedef)
  - [BatchGetCommitsErrorTypeDef](#batchgetcommitserrortypedef)
  - [BlobMetadataTypeDef](#blobmetadatatypedef)
  - [BranchInfoTypeDef](#branchinfotypedef)
  - [CommentTypeDef](#commenttypedef)
  - [CommentsForComparedCommitTypeDef](#commentsforcomparedcommittypedef)
  - [CommentsForPullRequestTypeDef](#commentsforpullrequesttypedef)
  - [CommitTypeDef](#committypedef)
  - [ConflictMetadataTypeDef](#conflictmetadatatypedef)
  - [ConflictTypeDef](#conflicttypedef)
  - [DeleteFileEntryTypeDef](#deletefileentrytypedef)
  - [DifferenceTypeDef](#differencetypedef)
  - [EvaluationTypeDef](#evaluationtypedef)
  - [FileMetadataTypeDef](#filemetadatatypedef)
  - [FileModesTypeDef](#filemodestypedef)
  - [FileSizesTypeDef](#filesizestypedef)
  - [FileTypeDef](#filetypedef)
  - [FolderTypeDef](#foldertypedef)
  - [IsBinaryFileTypeDef](#isbinaryfiletypedef)
  - [LocationTypeDef](#locationtypedef)
  - [MergeHunkDetailTypeDef](#mergehunkdetailtypedef)
  - [MergeHunkTypeDef](#mergehunktypedef)
  - [MergeMetadataTypeDef](#mergemetadatatypedef)
  - [MergeOperationsTypeDef](#mergeoperationstypedef)
  - [ObjectTypesTypeDef](#objecttypestypedef)
  - [OriginApprovalRuleTemplateTypeDef](#originapprovalruletemplatetypedef)
  - [PullRequestCreatedEventMetadataTypeDef](#pullrequestcreatedeventmetadatatypedef)
  - [PullRequestEventTypeDef](#pullrequesteventtypedef)
  - [PullRequestMergedStateChangedEventMetadataTypeDef](#pullrequestmergedstatechangedeventmetadatatypedef)
  - [PullRequestSourceReferenceUpdatedEventMetadataTypeDef](#pullrequestsourcereferenceupdatedeventmetadatatypedef)
  - [PullRequestStatusChangedEventMetadataTypeDef](#pullrequeststatuschangedeventmetadatatypedef)
  - [PullRequestTargetTypeDef](#pullrequesttargettypedef)
  - [PullRequestTypeDef](#pullrequesttypedef)
  - [ReactionForCommentTypeDef](#reactionforcommenttypedef)
  - [ReactionValueFormatsTypeDef](#reactionvalueformatstypedef)
  - [ReplaceContentEntryTypeDef](#replacecontententrytypedef)
  - [RepositoryMetadataTypeDef](#repositorymetadatatypedef)
  - [RepositoryNameIdPairTypeDef](#repositorynameidpairtypedef)
  - [RepositoryTriggerExecutionFailureTypeDef](#repositorytriggerexecutionfailuretypedef)
  - [RepositoryTriggerTypeDef](#repositorytriggertypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SetFileModeEntryTypeDef](#setfilemodeentrytypedef)
  - [SourceFileSpecifierTypeDef](#sourcefilespecifiertypedef)
  - [SubModuleTypeDef](#submoduletypedef)
  - [SymbolicLinkTypeDef](#symboliclinktypedef)
  - [UserInfoTypeDef](#userinfotypedef)
  - [BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef](#batchassociateapprovalruletemplatewithrepositoriesoutputtypedef)
  - [BatchDescribeMergeConflictsOutputTypeDef](#batchdescribemergeconflictsoutputtypedef)
  - [BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef](#batchdisassociateapprovalruletemplatefromrepositoriesoutputtypedef)
  - [BatchGetCommitsOutputTypeDef](#batchgetcommitsoutputtypedef)
  - [BatchGetRepositoriesOutputTypeDef](#batchgetrepositoriesoutputtypedef)
  - [ConflictResolutionTypeDef](#conflictresolutiontypedef)
  - [CreateApprovalRuleTemplateOutputTypeDef](#createapprovalruletemplateoutputtypedef)
  - [CreateCommitOutputTypeDef](#createcommitoutputtypedef)
  - [CreatePullRequestApprovalRuleOutputTypeDef](#createpullrequestapprovalruleoutputtypedef)
  - [CreatePullRequestOutputTypeDef](#createpullrequestoutputtypedef)
  - [CreateRepositoryOutputTypeDef](#createrepositoryoutputtypedef)
  - [CreateUnreferencedMergeCommitOutputTypeDef](#createunreferencedmergecommitoutputtypedef)
  - [DeleteApprovalRuleTemplateOutputTypeDef](#deleteapprovalruletemplateoutputtypedef)
  - [DeleteBranchOutputTypeDef](#deletebranchoutputtypedef)
  - [DeleteCommentContentOutputTypeDef](#deletecommentcontentoutputtypedef)
  - [DeleteFileOutputTypeDef](#deletefileoutputtypedef)
  - [DeletePullRequestApprovalRuleOutputTypeDef](#deletepullrequestapprovalruleoutputtypedef)
  - [DeleteRepositoryOutputTypeDef](#deleterepositoryoutputtypedef)
  - [DescribeMergeConflictsOutputTypeDef](#describemergeconflictsoutputtypedef)
  - [DescribePullRequestEventsOutputTypeDef](#describepullrequesteventsoutputtypedef)
  - [EvaluatePullRequestApprovalRulesOutputTypeDef](#evaluatepullrequestapprovalrulesoutputtypedef)
  - [GetApprovalRuleTemplateOutputTypeDef](#getapprovalruletemplateoutputtypedef)
  - [GetBlobOutputTypeDef](#getbloboutputtypedef)
  - [GetBranchOutputTypeDef](#getbranchoutputtypedef)
  - [GetCommentOutputTypeDef](#getcommentoutputtypedef)
  - [GetCommentReactionsOutputTypeDef](#getcommentreactionsoutputtypedef)
  - [GetCommentsForComparedCommitOutputTypeDef](#getcommentsforcomparedcommitoutputtypedef)
  - [GetCommentsForPullRequestOutputTypeDef](#getcommentsforpullrequestoutputtypedef)
  - [GetCommitOutputTypeDef](#getcommitoutputtypedef)
  - [GetDifferencesOutputTypeDef](#getdifferencesoutputtypedef)
  - [GetFileOutputTypeDef](#getfileoutputtypedef)
  - [GetFolderOutputTypeDef](#getfolderoutputtypedef)
  - [GetMergeCommitOutputTypeDef](#getmergecommitoutputtypedef)
  - [GetMergeConflictsOutputTypeDef](#getmergeconflictsoutputtypedef)
  - [GetMergeOptionsOutputTypeDef](#getmergeoptionsoutputtypedef)
  - [GetPullRequestApprovalStatesOutputTypeDef](#getpullrequestapprovalstatesoutputtypedef)
  - [GetPullRequestOutputTypeDef](#getpullrequestoutputtypedef)
  - [GetPullRequestOverrideStateOutputTypeDef](#getpullrequestoverridestateoutputtypedef)
  - [GetRepositoryOutputTypeDef](#getrepositoryoutputtypedef)
  - [GetRepositoryTriggersOutputTypeDef](#getrepositorytriggersoutputtypedef)
  - [ListApprovalRuleTemplatesOutputTypeDef](#listapprovalruletemplatesoutputtypedef)
  - [ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef](#listassociatedapprovalruletemplatesforrepositoryoutputtypedef)
  - [ListBranchesOutputTypeDef](#listbranchesoutputtypedef)
  - [ListPullRequestsOutputTypeDef](#listpullrequestsoutputtypedef)
  - [ListRepositoriesForApprovalRuleTemplateOutputTypeDef](#listrepositoriesforapprovalruletemplateoutputtypedef)
  - [ListRepositoriesOutputTypeDef](#listrepositoriesoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [MergeBranchesByFastForwardOutputTypeDef](#mergebranchesbyfastforwardoutputtypedef)
  - [MergeBranchesBySquashOutputTypeDef](#mergebranchesbysquashoutputtypedef)
  - [MergeBranchesByThreeWayOutputTypeDef](#mergebranchesbythreewayoutputtypedef)
  - [MergePullRequestByFastForwardOutputTypeDef](#mergepullrequestbyfastforwardoutputtypedef)
  - [MergePullRequestBySquashOutputTypeDef](#mergepullrequestbysquashoutputtypedef)
  - [MergePullRequestByThreeWayOutputTypeDef](#mergepullrequestbythreewayoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PostCommentForComparedCommitOutputTypeDef](#postcommentforcomparedcommitoutputtypedef)
  - [PostCommentForPullRequestOutputTypeDef](#postcommentforpullrequestoutputtypedef)
  - [PostCommentReplyOutputTypeDef](#postcommentreplyoutputtypedef)
  - [PutFileEntryTypeDef](#putfileentrytypedef)
  - [PutFileOutputTypeDef](#putfileoutputtypedef)
  - [PutRepositoryTriggersOutputTypeDef](#putrepositorytriggersoutputtypedef)
  - [TargetTypeDef](#targettypedef)
  - [TestRepositoryTriggersOutputTypeDef](#testrepositorytriggersoutputtypedef)
  - [UpdateApprovalRuleTemplateContentOutputTypeDef](#updateapprovalruletemplatecontentoutputtypedef)
  - [UpdateApprovalRuleTemplateDescriptionOutputTypeDef](#updateapprovalruletemplatedescriptionoutputtypedef)
  - [UpdateApprovalRuleTemplateNameOutputTypeDef](#updateapprovalruletemplatenameoutputtypedef)
  - [UpdateCommentOutputTypeDef](#updatecommentoutputtypedef)
  - [UpdatePullRequestApprovalRuleContentOutputTypeDef](#updatepullrequestapprovalrulecontentoutputtypedef)
  - [UpdatePullRequestDescriptionOutputTypeDef](#updatepullrequestdescriptionoutputtypedef)
  - [UpdatePullRequestStatusOutputTypeDef](#updatepullrequeststatusoutputtypedef)
  - [UpdatePullRequestTitleOutputTypeDef](#updatepullrequesttitleoutputtypedef)

## ApprovalRuleEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef
```




Optional fields:
- `approvalRuleName`: `str`
- `approvalRuleId`: `str`
- `approvalRuleContent`: `str`


## ApprovalRuleOverriddenEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import ApprovalRuleOverriddenEventMetadataTypeDef
```




Optional fields:
- `revisionId`: `str`
- `overrideStatus`: `OverrideStatus`


## ApprovalRuleTemplateTypeDef

```python
from mypy_boto3_codecommit.type_defs import ApprovalRuleTemplateTypeDef
```




Optional fields:
- `approvalRuleTemplateId`: `str`
- `approvalRuleTemplateName`: `str`
- `approvalRuleTemplateDescription`: `str`
- `approvalRuleTemplateContent`: `str`
- `ruleContentSha256`: `str`
- `lastModifiedDate`: `datetime`
- `creationDate`: `datetime`
- `lastModifiedUser`: `str`


## ApprovalRuleTypeDef

```python
from mypy_boto3_codecommit.type_defs import ApprovalRuleTypeDef
```




Optional fields:
- `approvalRuleId`: `str`
- `approvalRuleName`: `str`
- `approvalRuleContent`: `str`
- `ruleContentSha256`: `str`
- `lastModifiedDate`: `datetime`
- `creationDate`: `datetime`
- `lastModifiedUser`: `str`
- `originApprovalRuleTemplate`: `"OriginApprovalRuleTemplateTypeDef"`


## ApprovalStateChangedEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import ApprovalStateChangedEventMetadataTypeDef
```




Optional fields:
- `revisionId`: `str`
- `approvalStatus`: `ApprovalState`


## ApprovalTypeDef

```python
from mypy_boto3_codecommit.type_defs import ApprovalTypeDef
```




Optional fields:
- `userArn`: `str`
- `approvalState`: `ApprovalState`


## BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `errorCode`: `str`
- `errorMessage`: `str`


## BatchDescribeMergeConflictsErrorTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchDescribeMergeConflictsErrorTypeDef
```


Required fields:
- `filePath`: `str`
- `exceptionName`: `str`
- `message`: `str`




## BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `errorCode`: `str`
- `errorMessage`: `str`


## BatchGetCommitsErrorTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchGetCommitsErrorTypeDef
```




Optional fields:
- `commitId`: `str`
- `errorCode`: `str`
- `errorMessage`: `str`


## BlobMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import BlobMetadataTypeDef
```




Optional fields:
- `blobId`: `str`
- `path`: `str`
- `mode`: `str`


## BranchInfoTypeDef

```python
from mypy_boto3_codecommit.type_defs import BranchInfoTypeDef
```




Optional fields:
- `branchName`: `str`
- `commitId`: `str`


## CommentTypeDef

```python
from mypy_boto3_codecommit.type_defs import CommentTypeDef
```




Optional fields:
- `commentId`: `str`
- `content`: `str`
- `inReplyTo`: `str`
- `creationDate`: `datetime`
- `lastModifiedDate`: `datetime`
- `authorArn`: `str`
- `deleted`: `bool`
- `clientRequestToken`: `str`
- `callerReactions`: `List[str]`
- `reactionCounts`: `Dict[str, int]`


## CommentsForComparedCommitTypeDef

```python
from mypy_boto3_codecommit.type_defs import CommentsForComparedCommitTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `beforeCommitId`: `str`
- `afterCommitId`: `str`
- `beforeBlobId`: `str`
- `afterBlobId`: `str`
- `location`: `"LocationTypeDef"`
- `comments`: `List["CommentTypeDef"]`


## CommentsForPullRequestTypeDef

```python
from mypy_boto3_codecommit.type_defs import CommentsForPullRequestTypeDef
```




Optional fields:
- `pullRequestId`: `str`
- `repositoryName`: `str`
- `beforeCommitId`: `str`
- `afterCommitId`: `str`
- `beforeBlobId`: `str`
- `afterBlobId`: `str`
- `location`: `"LocationTypeDef"`
- `comments`: `List["CommentTypeDef"]`


## CommitTypeDef

```python
from mypy_boto3_codecommit.type_defs import CommitTypeDef
```




Optional fields:
- `commitId`: `str`
- `treeId`: `str`
- `parents`: `List[str]`
- `message`: `str`
- `author`: `"UserInfoTypeDef"`
- `committer`: `"UserInfoTypeDef"`
- `additionalData`: `str`


## ConflictMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import ConflictMetadataTypeDef
```




Optional fields:
- `filePath`: `str`
- `fileSizes`: `"FileSizesTypeDef"`
- `fileModes`: `"FileModesTypeDef"`
- `objectTypes`: `"ObjectTypesTypeDef"`
- `numberOfConflicts`: `int`
- `isBinaryFile`: `"IsBinaryFileTypeDef"`
- `contentConflict`: `bool`
- `fileModeConflict`: `bool`
- `objectTypeConflict`: `bool`
- `mergeOperations`: `"MergeOperationsTypeDef"`


## ConflictTypeDef

```python
from mypy_boto3_codecommit.type_defs import ConflictTypeDef
```




Optional fields:
- `conflictMetadata`: `"ConflictMetadataTypeDef"`
- `mergeHunks`: `List["MergeHunkTypeDef"]`


## DeleteFileEntryTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeleteFileEntryTypeDef
```


Required fields:
- `filePath`: `str`




## DifferenceTypeDef

```python
from mypy_boto3_codecommit.type_defs import DifferenceTypeDef
```




Optional fields:
- `beforeBlob`: `"BlobMetadataTypeDef"`
- `afterBlob`: `"BlobMetadataTypeDef"`
- `changeType`: `ChangeTypeEnum`


## EvaluationTypeDef

```python
from mypy_boto3_codecommit.type_defs import EvaluationTypeDef
```




Optional fields:
- `approved`: `bool`
- `overridden`: `bool`
- `approvalRulesSatisfied`: `List[str]`
- `approvalRulesNotSatisfied`: `List[str]`


## FileMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import FileMetadataTypeDef
```




Optional fields:
- `absolutePath`: `str`
- `blobId`: `str`
- `fileMode`: `FileModeTypeEnum`


## FileModesTypeDef

```python
from mypy_boto3_codecommit.type_defs import FileModesTypeDef
```




Optional fields:
- `source`: `FileModeTypeEnum`
- `destination`: `FileModeTypeEnum`
- `base`: `FileModeTypeEnum`


## FileSizesTypeDef

```python
from mypy_boto3_codecommit.type_defs import FileSizesTypeDef
```




Optional fields:
- `source`: `int`
- `destination`: `int`
- `base`: `int`


## FileTypeDef

```python
from mypy_boto3_codecommit.type_defs import FileTypeDef
```




Optional fields:
- `blobId`: `str`
- `absolutePath`: `str`
- `relativePath`: `str`
- `fileMode`: `FileModeTypeEnum`


## FolderTypeDef

```python
from mypy_boto3_codecommit.type_defs import FolderTypeDef
```




Optional fields:
- `treeId`: `str`
- `absolutePath`: `str`
- `relativePath`: `str`


## IsBinaryFileTypeDef

```python
from mypy_boto3_codecommit.type_defs import IsBinaryFileTypeDef
```




Optional fields:
- `source`: `bool`
- `destination`: `bool`
- `base`: `bool`


## LocationTypeDef

```python
from mypy_boto3_codecommit.type_defs import LocationTypeDef
```




Optional fields:
- `filePath`: `str`
- `filePosition`: `int`
- `relativeFileVersion`: `RelativeFileVersionEnum`


## MergeHunkDetailTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeHunkDetailTypeDef
```




Optional fields:
- `startLine`: `int`
- `endLine`: `int`
- `hunkContent`: `str`


## MergeHunkTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeHunkTypeDef
```




Optional fields:
- `isConflict`: `bool`
- `source`: `"MergeHunkDetailTypeDef"`
- `destination`: `"MergeHunkDetailTypeDef"`
- `base`: `"MergeHunkDetailTypeDef"`


## MergeMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeMetadataTypeDef
```




Optional fields:
- `isMerged`: `bool`
- `mergedBy`: `str`
- `mergeCommitId`: `str`
- `mergeOption`: `MergeOptionTypeEnum`


## MergeOperationsTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeOperationsTypeDef
```




Optional fields:
- `source`: `ChangeTypeEnum`
- `destination`: `ChangeTypeEnum`


## ObjectTypesTypeDef

```python
from mypy_boto3_codecommit.type_defs import ObjectTypesTypeDef
```




Optional fields:
- `source`: `ObjectTypeEnum`
- `destination`: `ObjectTypeEnum`
- `base`: `ObjectTypeEnum`


## OriginApprovalRuleTemplateTypeDef

```python
from mypy_boto3_codecommit.type_defs import OriginApprovalRuleTemplateTypeDef
```




Optional fields:
- `approvalRuleTemplateId`: `str`
- `approvalRuleTemplateName`: `str`


## PullRequestCreatedEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestCreatedEventMetadataTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `sourceCommitId`: `str`
- `destinationCommitId`: `str`
- `mergeBase`: `str`


## PullRequestEventTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestEventTypeDef
```




Optional fields:
- `pullRequestId`: `str`
- `eventDate`: `datetime`
- `pullRequestEventType`: `PullRequestEventType`
- `actorArn`: `str`
- `pullRequestCreatedEventMetadata`: `"PullRequestCreatedEventMetadataTypeDef"`
- `pullRequestStatusChangedEventMetadata`: `"PullRequestStatusChangedEventMetadataTypeDef"`
- `pullRequestSourceReferenceUpdatedEventMetadata`: `"PullRequestSourceReferenceUpdatedEventMetadataTypeDef"`
- `pullRequestMergedStateChangedEventMetadata`: `"PullRequestMergedStateChangedEventMetadataTypeDef"`
- `approvalRuleEventMetadata`: `"ApprovalRuleEventMetadataTypeDef"`
- `approvalStateChangedEventMetadata`: `"ApprovalStateChangedEventMetadataTypeDef"`
- `approvalRuleOverriddenEventMetadata`: `"ApprovalRuleOverriddenEventMetadataTypeDef"`


## PullRequestMergedStateChangedEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestMergedStateChangedEventMetadataTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `destinationReference`: `str`
- `mergeMetadata`: `"MergeMetadataTypeDef"`


## PullRequestSourceReferenceUpdatedEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestSourceReferenceUpdatedEventMetadataTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `beforeCommitId`: `str`
- `afterCommitId`: `str`
- `mergeBase`: `str`


## PullRequestStatusChangedEventMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestStatusChangedEventMetadataTypeDef
```




Optional fields:
- `pullRequestStatus`: `PullRequestStatusEnum`


## PullRequestTargetTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestTargetTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `sourceReference`: `str`
- `destinationReference`: `str`
- `destinationCommit`: `str`
- `sourceCommit`: `str`
- `mergeBase`: `str`
- `mergeMetadata`: `"MergeMetadataTypeDef"`


## PullRequestTypeDef

```python
from mypy_boto3_codecommit.type_defs import PullRequestTypeDef
```




Optional fields:
- `pullRequestId`: `str`
- `title`: `str`
- `description`: `str`
- `lastActivityDate`: `datetime`
- `creationDate`: `datetime`
- `pullRequestStatus`: `PullRequestStatusEnum`
- `authorArn`: `str`
- `pullRequestTargets`: `List["PullRequestTargetTypeDef"]`
- `clientRequestToken`: `str`
- `revisionId`: `str`
- `approvalRules`: `List["ApprovalRuleTypeDef"]`


## ReactionForCommentTypeDef

```python
from mypy_boto3_codecommit.type_defs import ReactionForCommentTypeDef
```




Optional fields:
- `reaction`: `"ReactionValueFormatsTypeDef"`
- `reactionUsers`: `List[str]`
- `reactionsFromDeletedUsersCount`: `int`


## ReactionValueFormatsTypeDef

```python
from mypy_boto3_codecommit.type_defs import ReactionValueFormatsTypeDef
```




Optional fields:
- `emoji`: `str`
- `shortCode`: `str`
- `unicode`: `str`


## ReplaceContentEntryTypeDef

```python
from mypy_boto3_codecommit.type_defs import ReplaceContentEntryTypeDef
```


Required fields:
- `filePath`: `str`
- `replacementType`: `ReplacementTypeEnum`



Optional fields:
- `content`: `Union[bytes, IO[bytes]]`
- `fileMode`: `FileModeTypeEnum`


## RepositoryMetadataTypeDef

```python
from mypy_boto3_codecommit.type_defs import RepositoryMetadataTypeDef
```




Optional fields:
- `accountId`: `str`
- `repositoryId`: `str`
- `repositoryName`: `str`
- `repositoryDescription`: `str`
- `defaultBranch`: `str`
- `lastModifiedDate`: `datetime`
- `creationDate`: `datetime`
- `cloneUrlHttp`: `str`
- `cloneUrlSsh`: `str`
- `Arn`: `str`


## RepositoryNameIdPairTypeDef

```python
from mypy_boto3_codecommit.type_defs import RepositoryNameIdPairTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `repositoryId`: `str`


## RepositoryTriggerExecutionFailureTypeDef

```python
from mypy_boto3_codecommit.type_defs import RepositoryTriggerExecutionFailureTypeDef
```




Optional fields:
- `trigger`: `str`
- `failureMessage`: `str`


## RepositoryTriggerTypeDef

```python
from mypy_boto3_codecommit.type_defs import RepositoryTriggerTypeDef
```


Required fields:
- `name`: `str`
- `destinationArn`: `str`
- `events`: `List[RepositoryTriggerEventEnum]`



Optional fields:
- `customData`: `str`
- `branches`: `List[str]`


## ResponseMetadata

```python
from mypy_boto3_codecommit.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SetFileModeEntryTypeDef

```python
from mypy_boto3_codecommit.type_defs import SetFileModeEntryTypeDef
```


Required fields:
- `filePath`: `str`
- `fileMode`: `FileModeTypeEnum`




## SourceFileSpecifierTypeDef

```python
from mypy_boto3_codecommit.type_defs import SourceFileSpecifierTypeDef
```


Required fields:
- `filePath`: `str`



Optional fields:
- `isMove`: `bool`


## SubModuleTypeDef

```python
from mypy_boto3_codecommit.type_defs import SubModuleTypeDef
```




Optional fields:
- `commitId`: `str`
- `absolutePath`: `str`
- `relativePath`: `str`


## SymbolicLinkTypeDef

```python
from mypy_boto3_codecommit.type_defs import SymbolicLinkTypeDef
```




Optional fields:
- `blobId`: `str`
- `absolutePath`: `str`
- `relativePath`: `str`
- `fileMode`: `FileModeTypeEnum`


## UserInfoTypeDef

```python
from mypy_boto3_codecommit.type_defs import UserInfoTypeDef
```




Optional fields:
- `name`: `str`
- `email`: `str`
- `date`: `str`


## BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef
```


Required fields:
- `associatedRepositoryNames`: `List[str]`
- `errors`: `List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"]`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchDescribeMergeConflictsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchDescribeMergeConflictsOutputTypeDef
```


Required fields:
- `conflicts`: `List["ConflictTypeDef"]`
- `destinationCommitId`: `str`
- `sourceCommitId`: `str`



Optional fields:
- `nextToken`: `str`
- `errors`: `List["BatchDescribeMergeConflictsErrorTypeDef"]`
- `baseCommitId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef
```


Required fields:
- `disassociatedRepositoryNames`: `List[str]`
- `errors`: `List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"]`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetCommitsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchGetCommitsOutputTypeDef
```




Optional fields:
- `commits`: `List["CommitTypeDef"]`
- `errors`: `List["BatchGetCommitsErrorTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetRepositoriesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import BatchGetRepositoriesOutputTypeDef
```




Optional fields:
- `repositories`: `List["RepositoryMetadataTypeDef"]`
- `repositoriesNotFound`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ConflictResolutionTypeDef

```python
from mypy_boto3_codecommit.type_defs import ConflictResolutionTypeDef
```




Optional fields:
- `replaceContents`: `List["ReplaceContentEntryTypeDef"]`
- `deleteFiles`: `List["DeleteFileEntryTypeDef"]`
- `setFileModes`: `List["SetFileModeEntryTypeDef"]`


## CreateApprovalRuleTemplateOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import CreateApprovalRuleTemplateOutputTypeDef
```


Required fields:
- `approvalRuleTemplate`: `"ApprovalRuleTemplateTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateCommitOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import CreateCommitOutputTypeDef
```




Optional fields:
- `commitId`: `str`
- `treeId`: `str`
- `filesAdded`: `List["FileMetadataTypeDef"]`
- `filesUpdated`: `List["FileMetadataTypeDef"]`
- `filesDeleted`: `List["FileMetadataTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePullRequestApprovalRuleOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import CreatePullRequestApprovalRuleOutputTypeDef
```


Required fields:
- `approvalRule`: `"ApprovalRuleTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePullRequestOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import CreatePullRequestOutputTypeDef
```


Required fields:
- `pullRequest`: `"PullRequestTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateRepositoryOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import CreateRepositoryOutputTypeDef
```




Optional fields:
- `repositoryMetadata`: `"RepositoryMetadataTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateUnreferencedMergeCommitOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import CreateUnreferencedMergeCommitOutputTypeDef
```




Optional fields:
- `commitId`: `str`
- `treeId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteApprovalRuleTemplateOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeleteApprovalRuleTemplateOutputTypeDef
```


Required fields:
- `approvalRuleTemplateId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteBranchOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeleteBranchOutputTypeDef
```




Optional fields:
- `deletedBranch`: `"BranchInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteCommentContentOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeleteCommentContentOutputTypeDef
```




Optional fields:
- `comment`: `"CommentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteFileOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeleteFileOutputTypeDef
```


Required fields:
- `commitId`: `str`
- `blobId`: `str`
- `treeId`: `str`
- `filePath`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeletePullRequestApprovalRuleOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeletePullRequestApprovalRuleOutputTypeDef
```


Required fields:
- `approvalRuleId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteRepositoryOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DeleteRepositoryOutputTypeDef
```




Optional fields:
- `repositoryId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeMergeConflictsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DescribeMergeConflictsOutputTypeDef
```


Required fields:
- `conflictMetadata`: `"ConflictMetadataTypeDef"`
- `mergeHunks`: `List["MergeHunkTypeDef"]`
- `destinationCommitId`: `str`
- `sourceCommitId`: `str`



Optional fields:
- `nextToken`: `str`
- `baseCommitId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePullRequestEventsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import DescribePullRequestEventsOutputTypeDef
```


Required fields:
- `pullRequestEvents`: `List["PullRequestEventTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## EvaluatePullRequestApprovalRulesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import EvaluatePullRequestApprovalRulesOutputTypeDef
```


Required fields:
- `evaluation`: `"EvaluationTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetApprovalRuleTemplateOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetApprovalRuleTemplateOutputTypeDef
```


Required fields:
- `approvalRuleTemplate`: `"ApprovalRuleTemplateTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBlobOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetBlobOutputTypeDef
```


Required fields:
- `content`: `Union[bytes, IO[bytes]]`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetBranchOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetBranchOutputTypeDef
```




Optional fields:
- `branch`: `"BranchInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetCommentOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetCommentOutputTypeDef
```




Optional fields:
- `comment`: `"CommentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetCommentReactionsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetCommentReactionsOutputTypeDef
```


Required fields:
- `reactionsForComment`: `List["ReactionForCommentTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetCommentsForComparedCommitOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetCommentsForComparedCommitOutputTypeDef
```




Optional fields:
- `commentsForComparedCommitData`: `List["CommentsForComparedCommitTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetCommentsForPullRequestOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetCommentsForPullRequestOutputTypeDef
```




Optional fields:
- `commentsForPullRequestData`: `List["CommentsForPullRequestTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetCommitOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetCommitOutputTypeDef
```


Required fields:
- `commit`: `"CommitTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDifferencesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetDifferencesOutputTypeDef
```




Optional fields:
- `differences`: `List["DifferenceTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetFileOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetFileOutputTypeDef
```


Required fields:
- `commitId`: `str`
- `blobId`: `str`
- `filePath`: `str`
- `fileMode`: `FileModeTypeEnum`
- `fileSize`: `int`
- `fileContent`: `Union[bytes, IO[bytes]]`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetFolderOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetFolderOutputTypeDef
```


Required fields:
- `commitId`: `str`
- `folderPath`: `str`



Optional fields:
- `treeId`: `str`
- `subFolders`: `List["FolderTypeDef"]`
- `files`: `List["FileTypeDef"]`
- `symbolicLinks`: `List["SymbolicLinkTypeDef"]`
- `subModules`: `List["SubModuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMergeCommitOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetMergeCommitOutputTypeDef
```




Optional fields:
- `sourceCommitId`: `str`
- `destinationCommitId`: `str`
- `baseCommitId`: `str`
- `mergedCommitId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMergeConflictsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetMergeConflictsOutputTypeDef
```


Required fields:
- `mergeable`: `bool`
- `destinationCommitId`: `str`
- `sourceCommitId`: `str`
- `conflictMetadataList`: `List["ConflictMetadataTypeDef"]`



Optional fields:
- `baseCommitId`: `str`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMergeOptionsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetMergeOptionsOutputTypeDef
```


Required fields:
- `mergeOptions`: `List[MergeOptionTypeEnum]`
- `sourceCommitId`: `str`
- `destinationCommitId`: `str`
- `baseCommitId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPullRequestApprovalStatesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetPullRequestApprovalStatesOutputTypeDef
```




Optional fields:
- `approvals`: `List["ApprovalTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPullRequestOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetPullRequestOutputTypeDef
```


Required fields:
- `pullRequest`: `"PullRequestTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## GetPullRequestOverrideStateOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetPullRequestOverrideStateOutputTypeDef
```




Optional fields:
- `overridden`: `bool`
- `overrider`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetRepositoryOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetRepositoryOutputTypeDef
```




Optional fields:
- `repositoryMetadata`: `"RepositoryMetadataTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetRepositoryTriggersOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import GetRepositoryTriggersOutputTypeDef
```




Optional fields:
- `configurationId`: `str`
- `triggers`: `List["RepositoryTriggerTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListApprovalRuleTemplatesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListApprovalRuleTemplatesOutputTypeDef
```




Optional fields:
- `approvalRuleTemplateNames`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef
```




Optional fields:
- `approvalRuleTemplateNames`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBranchesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListBranchesOutputTypeDef
```




Optional fields:
- `branches`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPullRequestsOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListPullRequestsOutputTypeDef
```


Required fields:
- `pullRequestIds`: `List[str]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRepositoriesForApprovalRuleTemplateOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListRepositoriesForApprovalRuleTemplateOutputTypeDef
```




Optional fields:
- `repositoryNames`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRepositoriesOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListRepositoriesOutputTypeDef
```




Optional fields:
- `repositories`: `List["RepositoryNameIdPairTypeDef"]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## MergeBranchesByFastForwardOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeBranchesByFastForwardOutputTypeDef
```




Optional fields:
- `commitId`: `str`
- `treeId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## MergeBranchesBySquashOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeBranchesBySquashOutputTypeDef
```




Optional fields:
- `commitId`: `str`
- `treeId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## MergeBranchesByThreeWayOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergeBranchesByThreeWayOutputTypeDef
```




Optional fields:
- `commitId`: `str`
- `treeId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## MergePullRequestByFastForwardOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergePullRequestByFastForwardOutputTypeDef
```




Optional fields:
- `pullRequest`: `"PullRequestTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## MergePullRequestBySquashOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergePullRequestBySquashOutputTypeDef
```




Optional fields:
- `pullRequest`: `"PullRequestTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## MergePullRequestByThreeWayOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import MergePullRequestByThreeWayOutputTypeDef
```




Optional fields:
- `pullRequest`: `"PullRequestTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codecommit.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PostCommentForComparedCommitOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import PostCommentForComparedCommitOutputTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `beforeCommitId`: `str`
- `afterCommitId`: `str`
- `beforeBlobId`: `str`
- `afterBlobId`: `str`
- `location`: `"LocationTypeDef"`
- `comment`: `"CommentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PostCommentForPullRequestOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import PostCommentForPullRequestOutputTypeDef
```




Optional fields:
- `repositoryName`: `str`
- `pullRequestId`: `str`
- `beforeCommitId`: `str`
- `afterCommitId`: `str`
- `beforeBlobId`: `str`
- `afterBlobId`: `str`
- `location`: `"LocationTypeDef"`
- `comment`: `"CommentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PostCommentReplyOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import PostCommentReplyOutputTypeDef
```




Optional fields:
- `comment`: `"CommentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PutFileEntryTypeDef

```python
from mypy_boto3_codecommit.type_defs import PutFileEntryTypeDef
```


Required fields:
- `filePath`: `str`



Optional fields:
- `fileMode`: `FileModeTypeEnum`
- `fileContent`: `Union[bytes, IO[bytes]]`
- `sourceFile`: `"SourceFileSpecifierTypeDef"`


## PutFileOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import PutFileOutputTypeDef
```


Required fields:
- `commitId`: `str`
- `blobId`: `str`
- `treeId`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## PutRepositoryTriggersOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import PutRepositoryTriggersOutputTypeDef
```




Optional fields:
- `configurationId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## TargetTypeDef

```python
from mypy_boto3_codecommit.type_defs import TargetTypeDef
```


Required fields:
- `repositoryName`: `str`
- `sourceReference`: `str`



Optional fields:
- `destinationReference`: `str`


## TestRepositoryTriggersOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import TestRepositoryTriggersOutputTypeDef
```




Optional fields:
- `successfulExecutions`: `List[str]`
- `failedExecutions`: `List["RepositoryTriggerExecutionFailureTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateApprovalRuleTemplateContentOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdateApprovalRuleTemplateContentOutputTypeDef
```


Required fields:
- `approvalRuleTemplate`: `"ApprovalRuleTemplateTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateApprovalRuleTemplateDescriptionOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdateApprovalRuleTemplateDescriptionOutputTypeDef
```


Required fields:
- `approvalRuleTemplate`: `"ApprovalRuleTemplateTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateApprovalRuleTemplateNameOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdateApprovalRuleTemplateNameOutputTypeDef
```


Required fields:
- `approvalRuleTemplate`: `"ApprovalRuleTemplateTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateCommentOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdateCommentOutputTypeDef
```




Optional fields:
- `comment`: `"CommentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdatePullRequestApprovalRuleContentOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdatePullRequestApprovalRuleContentOutputTypeDef
```


Required fields:
- `approvalRule`: `"ApprovalRuleTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdatePullRequestDescriptionOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdatePullRequestDescriptionOutputTypeDef
```


Required fields:
- `pullRequest`: `"PullRequestTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdatePullRequestStatusOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdatePullRequestStatusOutputTypeDef
```


Required fields:
- `pullRequest`: `"PullRequestTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdatePullRequestTitleOutputTypeDef

```python
from mypy_boto3_codecommit.type_defs import UpdatePullRequestTitleOutputTypeDef
```


Required fields:
- `pullRequest`: `"PullRequestTypeDef"`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`

