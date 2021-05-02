# Type annotations for boto3 CodeStar module

> [Index](../index.md) > CodeStar

Auto-generated documentation for [CodeStar](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar)
type annotations stubs module [mypy_boto3_codestar](https://pypi.org/project/mypy-boto3-codestar/).

```bash
pip install mypy-boto3-codestar
```

- [Type annotations for boto3 CodeStar module](#type-annotations-for-boto3-codestar-module)
  - [CodeStarClient](#codestarclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeStarClient

Type annotations for  `boto3.client("codestar")` as [CodeStarClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codestar.client import CodeStarClient
```


CodeStarClient [exceptions](./client.md#exceptions)



### Methods
- [associate_team_member](./client.md#associate-team-member)
- [can_paginate](./client.md#can-paginate)
- [create_project](./client.md#create-project)
- [create_user_profile](./client.md#create-user-profile)
- [delete_project](./client.md#delete-project)
- [delete_user_profile](./client.md#delete-user-profile)
- [describe_project](./client.md#describe-project)
- [describe_user_profile](./client.md#describe-user-profile)
- [disassociate_team_member](./client.md#disassociate-team-member)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_projects](./client.md#list-projects)
- [list_resources](./client.md#list-resources)
- [list_tags_for_project](./client.md#list-tags-for-project)
- [list_team_members](./client.md#list-team-members)
- [list_user_profiles](./client.md#list-user-profiles)
- [tag_project](./client.md#tag-project)
- [untag_project](./client.md#untag-project)
- [update_project](./client.md#update-project)
- [update_team_member](./client.md#update-team-member)
- [update_user_profile](./client.md#update-user-profile)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidServiceRoleException](./client.md#invalidserviceroleexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ProjectAlreadyExistsException](./client.md#projectalreadyexistsexception)
- [ProjectConfigurationException](./client.md#projectconfigurationexception)
- [ProjectCreationFailedException](./client.md#projectcreationfailedexception)
- [ProjectNotFoundException](./client.md#projectnotfoundexception)
- [TeamMemberAlreadyAssociatedException](./client.md#teammemberalreadyassociatedexception)
- [TeamMemberNotFoundException](./client.md#teammembernotfoundexception)
- [UserProfileAlreadyExistsException](./client.md#userprofilealreadyexistsexception)
- [UserProfileNotFoundException](./client.md#userprofilenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codestar").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codestar.paginators import ListProjectsPaginator, ...
```

- [ListProjectsPaginator](./paginators.md#listprojectspaginator)
- [ListResourcesPaginator](./paginators.md#listresourcespaginator)
- [ListTeamMembersPaginator](./paginators.md#listteammemberspaginator)
- [ListUserProfilesPaginator](./paginators.md#listuserprofilespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codestar.literals import ListProjectsPaginatorName, ...
```

- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)
- [ListResourcesPaginatorName](./literals.md#listresourcespaginatorname)
- [ListTeamMembersPaginatorName](./literals.md#listteammemberspaginatorname)
- [ListUserProfilesPaginatorName](./literals.md#listuserprofilespaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codestar.type_defs import AssociateTeamMemberResultTypeDef, ...
```

- [AssociateTeamMemberResultTypeDef](./type_defs.md#associateteammemberresulttypedef)
- [CodeCommitCodeDestinationTypeDef](./type_defs.md#codecommitcodedestinationtypedef)
- [CodeDestinationTypeDef](./type_defs.md#codedestinationtypedef)
- [CodeSourceTypeDef](./type_defs.md#codesourcetypedef)
- [CodeTypeDef](./type_defs.md#codetypedef)
- [CreateProjectResultTypeDef](./type_defs.md#createprojectresulttypedef)
- [CreateUserProfileResultTypeDef](./type_defs.md#createuserprofileresulttypedef)
- [DeleteProjectResultTypeDef](./type_defs.md#deleteprojectresulttypedef)
- [DeleteUserProfileResultTypeDef](./type_defs.md#deleteuserprofileresulttypedef)
- [DescribeProjectResultTypeDef](./type_defs.md#describeprojectresulttypedef)
- [DescribeUserProfileResultTypeDef](./type_defs.md#describeuserprofileresulttypedef)
- [GitHubCodeDestinationTypeDef](./type_defs.md#githubcodedestinationtypedef)
- [ListProjectsResultTypeDef](./type_defs.md#listprojectsresulttypedef)
- [ListResourcesResultTypeDef](./type_defs.md#listresourcesresulttypedef)
- [ListTagsForProjectResultTypeDef](./type_defs.md#listtagsforprojectresulttypedef)
- [ListTeamMembersResultTypeDef](./type_defs.md#listteammembersresulttypedef)
- [ListUserProfilesResultTypeDef](./type_defs.md#listuserprofilesresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProjectStatusTypeDef](./type_defs.md#projectstatustypedef)
- [ProjectSummaryTypeDef](./type_defs.md#projectsummarytypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [TagProjectResultTypeDef](./type_defs.md#tagprojectresulttypedef)
- [TeamMemberTypeDef](./type_defs.md#teammembertypedef)
- [ToolchainSourceTypeDef](./type_defs.md#toolchainsourcetypedef)
- [ToolchainTypeDef](./type_defs.md#toolchaintypedef)
- [UpdateTeamMemberResultTypeDef](./type_defs.md#updateteammemberresulttypedef)
- [UpdateUserProfileResultTypeDef](./type_defs.md#updateuserprofileresulttypedef)
- [UserProfileSummaryTypeDef](./type_defs.md#userprofilesummarytypedef)
