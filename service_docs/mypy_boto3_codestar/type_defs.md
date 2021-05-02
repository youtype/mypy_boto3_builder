# Structures for boto3 CodeStar module

> [Index](../index.md) > [CodeStar](./index.md) > Structures

Auto-generated documentation for [CodeStar](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar)
type annotations stubs module [mypy_boto3_codestar](https://pypi.org/project/mypy-boto3-codestar/).

- [Structures for boto3 CodeStar module](#structures-for-boto3-codestar-module)
  - [AssociateTeamMemberResultTypeDef](#associateteammemberresulttypedef)
  - [CodeCommitCodeDestinationTypeDef](#codecommitcodedestinationtypedef)
  - [CodeDestinationTypeDef](#codedestinationtypedef)
  - [CodeSourceTypeDef](#codesourcetypedef)
  - [CodeTypeDef](#codetypedef)
  - [CreateProjectResultTypeDef](#createprojectresulttypedef)
  - [CreateUserProfileResultTypeDef](#createuserprofileresulttypedef)
  - [DeleteProjectResultTypeDef](#deleteprojectresulttypedef)
  - [DeleteUserProfileResultTypeDef](#deleteuserprofileresulttypedef)
  - [DescribeProjectResultTypeDef](#describeprojectresulttypedef)
  - [DescribeUserProfileResultTypeDef](#describeuserprofileresulttypedef)
  - [GitHubCodeDestinationTypeDef](#githubcodedestinationtypedef)
  - [ListProjectsResultTypeDef](#listprojectsresulttypedef)
  - [ListResourcesResultTypeDef](#listresourcesresulttypedef)
  - [ListTagsForProjectResultTypeDef](#listtagsforprojectresulttypedef)
  - [ListTeamMembersResultTypeDef](#listteammembersresulttypedef)
  - [ListUserProfilesResultTypeDef](#listuserprofilesresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProjectStatusTypeDef](#projectstatustypedef)
  - [ProjectSummaryTypeDef](#projectsummarytypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [TagProjectResultTypeDef](#tagprojectresulttypedef)
  - [TeamMemberTypeDef](#teammembertypedef)
  - [ToolchainSourceTypeDef](#toolchainsourcetypedef)
  - [ToolchainTypeDef](#toolchaintypedef)
  - [UpdateTeamMemberResultTypeDef](#updateteammemberresulttypedef)
  - [UpdateUserProfileResultTypeDef](#updateuserprofileresulttypedef)
  - [UserProfileSummaryTypeDef](#userprofilesummarytypedef)

## AssociateTeamMemberResultTypeDef

```python
from mypy_boto3_codestar.type_defs import AssociateTeamMemberResultTypeDef
```




Optional fields:
- `clientRequestToken`: `str`


## CodeCommitCodeDestinationTypeDef

```python
from mypy_boto3_codestar.type_defs import CodeCommitCodeDestinationTypeDef
```


Required fields:
- `name`: `str`




## CodeDestinationTypeDef

```python
from mypy_boto3_codestar.type_defs import CodeDestinationTypeDef
```




Optional fields:
- `codeCommit`: `"CodeCommitCodeDestinationTypeDef"`
- `gitHub`: `"GitHubCodeDestinationTypeDef"`


## CodeSourceTypeDef

```python
from mypy_boto3_codestar.type_defs import CodeSourceTypeDef
```


Required fields:
- `s3`: `"S3LocationTypeDef"`




## CodeTypeDef

```python
from mypy_boto3_codestar.type_defs import CodeTypeDef
```


Required fields:
- `source`: `"CodeSourceTypeDef"`
- `destination`: `"CodeDestinationTypeDef"`




## CreateProjectResultTypeDef

```python
from mypy_boto3_codestar.type_defs import CreateProjectResultTypeDef
```


Required fields:
- `id`: `str`
- `arn`: `str`



Optional fields:
- `clientRequestToken`: `str`
- `projectTemplateId`: `str`


## CreateUserProfileResultTypeDef

```python
from mypy_boto3_codestar.type_defs import CreateUserProfileResultTypeDef
```


Required fields:
- `userArn`: `str`



Optional fields:
- `displayName`: `str`
- `emailAddress`: `str`
- `sshPublicKey`: `str`
- `createdTimestamp`: `datetime`
- `lastModifiedTimestamp`: `datetime`


## DeleteProjectResultTypeDef

```python
from mypy_boto3_codestar.type_defs import DeleteProjectResultTypeDef
```




Optional fields:
- `stackId`: `str`
- `projectArn`: `str`


## DeleteUserProfileResultTypeDef

```python
from mypy_boto3_codestar.type_defs import DeleteUserProfileResultTypeDef
```


Required fields:
- `userArn`: `str`




## DescribeProjectResultTypeDef

```python
from mypy_boto3_codestar.type_defs import DescribeProjectResultTypeDef
```




Optional fields:
- `name`: `str`
- `id`: `str`
- `arn`: `str`
- `description`: `str`
- `clientRequestToken`: `str`
- `createdTimeStamp`: `datetime`
- `stackId`: `str`
- `projectTemplateId`: `str`
- `status`: `"ProjectStatusTypeDef"`


## DescribeUserProfileResultTypeDef

```python
from mypy_boto3_codestar.type_defs import DescribeUserProfileResultTypeDef
```


Required fields:
- `userArn`: `str`
- `createdTimestamp`: `datetime`
- `lastModifiedTimestamp`: `datetime`



Optional fields:
- `displayName`: `str`
- `emailAddress`: `str`
- `sshPublicKey`: `str`


## GitHubCodeDestinationTypeDef

```python
from mypy_boto3_codestar.type_defs import GitHubCodeDestinationTypeDef
```


Required fields:
- `name`: `str`
- `type`: `str`
- `owner`: `str`
- `privateRepository`: `bool`
- `issuesEnabled`: `bool`
- `token`: `str`



Optional fields:
- `description`: `str`


## ListProjectsResultTypeDef

```python
from mypy_boto3_codestar.type_defs import ListProjectsResultTypeDef
```


Required fields:
- `projects`: `List["ProjectSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListResourcesResultTypeDef

```python
from mypy_boto3_codestar.type_defs import ListResourcesResultTypeDef
```




Optional fields:
- `resources`: `List["ResourceTypeDef"]`
- `nextToken`: `str`


## ListTagsForProjectResultTypeDef

```python
from mypy_boto3_codestar.type_defs import ListTagsForProjectResultTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`
- `nextToken`: `str`


## ListTeamMembersResultTypeDef

```python
from mypy_boto3_codestar.type_defs import ListTeamMembersResultTypeDef
```


Required fields:
- `teamMembers`: `List["TeamMemberTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListUserProfilesResultTypeDef

```python
from mypy_boto3_codestar.type_defs import ListUserProfilesResultTypeDef
```


Required fields:
- `userProfiles`: `List["UserProfileSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codestar.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProjectStatusTypeDef

```python
from mypy_boto3_codestar.type_defs import ProjectStatusTypeDef
```


Required fields:
- `state`: `str`



Optional fields:
- `reason`: `str`


## ProjectSummaryTypeDef

```python
from mypy_boto3_codestar.type_defs import ProjectSummaryTypeDef
```




Optional fields:
- `projectId`: `str`
- `projectArn`: `str`


## ResourceTypeDef

```python
from mypy_boto3_codestar.type_defs import ResourceTypeDef
```


Required fields:
- `id`: `str`




## S3LocationTypeDef

```python
from mypy_boto3_codestar.type_defs import S3LocationTypeDef
```




Optional fields:
- `bucketName`: `str`
- `bucketKey`: `str`


## TagProjectResultTypeDef

```python
from mypy_boto3_codestar.type_defs import TagProjectResultTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## TeamMemberTypeDef

```python
from mypy_boto3_codestar.type_defs import TeamMemberTypeDef
```


Required fields:
- `userArn`: `str`
- `projectRole`: `str`



Optional fields:
- `remoteAccessAllowed`: `bool`


## ToolchainSourceTypeDef

```python
from mypy_boto3_codestar.type_defs import ToolchainSourceTypeDef
```


Required fields:
- `s3`: `"S3LocationTypeDef"`




## ToolchainTypeDef

```python
from mypy_boto3_codestar.type_defs import ToolchainTypeDef
```


Required fields:
- `source`: `"ToolchainSourceTypeDef"`



Optional fields:
- `roleArn`: `str`
- `stackParameters`: `Dict[str, str]`


## UpdateTeamMemberResultTypeDef

```python
from mypy_boto3_codestar.type_defs import UpdateTeamMemberResultTypeDef
```




Optional fields:
- `userArn`: `str`
- `projectRole`: `str`
- `remoteAccessAllowed`: `bool`


## UpdateUserProfileResultTypeDef

```python
from mypy_boto3_codestar.type_defs import UpdateUserProfileResultTypeDef
```


Required fields:
- `userArn`: `str`



Optional fields:
- `displayName`: `str`
- `emailAddress`: `str`
- `sshPublicKey`: `str`
- `createdTimestamp`: `datetime`
- `lastModifiedTimestamp`: `datetime`


## UserProfileSummaryTypeDef

```python
from mypy_boto3_codestar.type_defs import UserProfileSummaryTypeDef
```




Optional fields:
- `userArn`: `str`
- `displayName`: `str`
- `emailAddress`: `str`
- `sshPublicKey`: `str`

