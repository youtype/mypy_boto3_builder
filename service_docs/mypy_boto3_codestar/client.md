# CodeStarClient for boto3 CodeStar module

> [Index](../index.md) > [CodeStar](./index.md) > CodeStarClient

Auto-generated documentation for [CodeStar](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar)
type annotations stubs module [mypy_boto3_codestar](https://pypi.org/project/mypy-boto3-codestar/).

- [CodeStarClient for boto3 CodeStar module](#codestarclient-for-boto3-codestar-module)
  - [CodeStarClient](#codestarclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_team_member](#associate_team_member)
    - [can_paginate](#can_paginate)
    - [create_project](#create_project)
    - [create_user_profile](#create_user_profile)
    - [delete_project](#delete_project)
    - [delete_user_profile](#delete_user_profile)
    - [describe_project](#describe_project)
    - [describe_user_profile](#describe_user_profile)
    - [disassociate_team_member](#disassociate_team_member)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_projects](#list_projects)
    - [list_resources](#list_resources)
    - [list_tags_for_project](#list_tags_for_project)
    - [list_team_members](#list_team_members)
    - [list_user_profiles](#list_user_profiles)
    - [tag_project](#tag_project)
    - [untag_project](#untag_project)
    - [update_project](#update_project)
    - [update_team_member](#update_team_member)
    - [update_user_profile](#update_user_profile)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)

## CodeStarClient

Type annotations for `boto3.client("codestar")`

Can be used directly:

```python
from mypy_boto3_codestar.client import CodeStarClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codestar.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidServiceRoleException`
- `Exceptions.LimitExceededException`
- `Exceptions.ProjectAlreadyExistsException`
- `Exceptions.ProjectConfigurationException`
- `Exceptions.ProjectCreationFailedException`
- `Exceptions.ProjectNotFoundException`
- `Exceptions.TeamMemberAlreadyAssociatedException`
- `Exceptions.TeamMemberNotFoundException`
- `Exceptions.UserProfileAlreadyExistsException`
- `Exceptions.UserProfileNotFoundException`
- `Exceptions.ValidationException`


## Methods


### associate_team_member

Type annotations for `boto3.client("codestar").associate_team_member` method.

[Client.associate_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.associate_team_member)

```python
def associate_team_member(
    self,
    projectId: str,
    userArn: str,
    projectRole: str,
    clientRequestToken: str = None,
    remoteAccessAllowed: bool = None
) -> AssociateTeamMemberResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codestar").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_project

Type annotations for `boto3.client("codestar").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.create_project)

```python
def create_project(
    self,
    name: str,
    id: str,
    description: str = None,
    clientRequestToken: str = None,
    sourceCode: List[CodeTypeDef] = None,
    toolchain: ToolchainTypeDef = None,
    tags: Dict[str, str] = None
) -> CreateProjectResultTypeDef:
    pass
```

### create_user_profile

Type annotations for `boto3.client("codestar").create_user_profile` method.

[Client.create_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.create_user_profile)

```python
def create_user_profile(
    self,
    userArn: str,
    displayName: str,
    emailAddress: str,
    sshPublicKey: str = None
) -> CreateUserProfileResultTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("codestar").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.delete_project)

```python
def delete_project(
    self,
    id: str,
    clientRequestToken: str = None,
    deleteStack: bool = None
) -> DeleteProjectResultTypeDef:
    pass
```

### delete_user_profile

Type annotations for `boto3.client("codestar").delete_user_profile` method.

[Client.delete_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.delete_user_profile)

```python
def delete_user_profile(
    self,
    userArn: str
) -> DeleteUserProfileResultTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("codestar").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.describe_project)

```python
def describe_project(
    self,
    id: str
) -> DescribeProjectResultTypeDef:
    pass
```

### describe_user_profile

Type annotations for `boto3.client("codestar").describe_user_profile` method.

[Client.describe_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.describe_user_profile)

```python
def describe_user_profile(
    self,
    userArn: str
) -> DescribeUserProfileResultTypeDef:
    pass
```

### disassociate_team_member

Type annotations for `boto3.client("codestar").disassociate_team_member` method.

[Client.disassociate_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.disassociate_team_member)

```python
def disassociate_team_member(
    self,
    projectId: str,
    userArn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codestar").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.generate_presigned_url)

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

### list_projects

Type annotations for `boto3.client("codestar").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.list_projects)

```python
def list_projects(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListProjectsResultTypeDef:
    pass
```

### list_resources

Type annotations for `boto3.client("codestar").list_resources` method.

[Client.list_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.list_resources)

```python
def list_resources(
    self,
    projectId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListResourcesResultTypeDef:
    pass
```

### list_tags_for_project

Type annotations for `boto3.client("codestar").list_tags_for_project` method.

[Client.list_tags_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.list_tags_for_project)

```python
def list_tags_for_project(
    self,
    id: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListTagsForProjectResultTypeDef:
    pass
```

### list_team_members

Type annotations for `boto3.client("codestar").list_team_members` method.

[Client.list_team_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.list_team_members)

```python
def list_team_members(
    self,
    projectId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListTeamMembersResultTypeDef:
    pass
```

### list_user_profiles

Type annotations for `boto3.client("codestar").list_user_profiles` method.

[Client.list_user_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.list_user_profiles)

```python
def list_user_profiles(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListUserProfilesResultTypeDef:
    pass
```

### tag_project

Type annotations for `boto3.client("codestar").tag_project` method.

[Client.tag_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.tag_project)

```python
def tag_project(
    self,
    id: str,
    tags: Dict[str, str]
) -> TagProjectResultTypeDef:
    pass
```

### untag_project

Type annotations for `boto3.client("codestar").untag_project` method.

[Client.untag_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.untag_project)

```python
def untag_project(
    self,
    id: str,
    tags: List[str]
) -> Dict[str, Any]:
    pass
```

### update_project

Type annotations for `boto3.client("codestar").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.update_project)

```python
def update_project(
    self,
    id: str,
    name: str = None,
    description: str = None
) -> Dict[str, Any]:
    pass
```

### update_team_member

Type annotations for `boto3.client("codestar").update_team_member` method.

[Client.update_team_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.update_team_member)

```python
def update_team_member(
    self,
    projectId: str,
    userArn: str,
    projectRole: str = None,
    remoteAccessAllowed: bool = None
) -> UpdateTeamMemberResultTypeDef:
    pass
```

### update_user_profile

Type annotations for `boto3.client("codestar").update_user_profile` method.

[Client.update_user_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Client.update_user_profile)

```python
def update_user_profile(
    self,
    userArn: str,
    displayName: str = None,
    emailAddress: str = None,
    sshPublicKey: str = None
) -> UpdateUserProfileResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("codestar").get_paginator` method.

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Paginator.ListProjects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListProjectsPaginatorName
) -> ListProjectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codestar").get_paginator` method.

[Paginator.ListResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Paginator.ListResources)

```python
@overload
def get_paginator(
    self,
    operation_name: ListResourcesPaginatorName
) -> ListResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codestar").get_paginator` method.

[Paginator.ListTeamMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTeamMembersPaginatorName
) -> ListTeamMembersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codestar").get_paginator` method.

[Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUserProfilesPaginatorName
) -> ListUserProfilesPaginator:
    pass
```