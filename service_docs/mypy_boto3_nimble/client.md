# NimbleStudioClient for boto3 NimbleStudio module

> [Index](../index.md) > [NimbleStudio](./index.md) > NimbleStudioClient

Auto-generated documentation for [NimbleStudio](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio)
type annotations stubs module [mypy_boto3_nimble](https://pypi.org/project/mypy-boto3-nimble/).

- [NimbleStudioClient for boto3 NimbleStudio module](#nimblestudioclient-for-boto3-nimblestudio-module)
  - [NimbleStudioClient](#nimblestudioclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_eulas](#accept_eulas)
    - [can_paginate](#can_paginate)
    - [create_launch_profile](#create_launch_profile)
    - [create_streaming_image](#create_streaming_image)
    - [create_streaming_session](#create_streaming_session)
    - [create_streaming_session_stream](#create_streaming_session_stream)
    - [create_studio](#create_studio)
    - [create_studio_component](#create_studio_component)
    - [delete_launch_profile](#delete_launch_profile)
    - [delete_launch_profile_member](#delete_launch_profile_member)
    - [delete_streaming_image](#delete_streaming_image)
    - [delete_streaming_session](#delete_streaming_session)
    - [delete_studio](#delete_studio)
    - [delete_studio_component](#delete_studio_component)
    - [delete_studio_member](#delete_studio_member)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_eula](#get_eula)
    - [get_launch_profile](#get_launch_profile)
    - [get_launch_profile_details](#get_launch_profile_details)
    - [get_launch_profile_initialization](#get_launch_profile_initialization)
    - [get_launch_profile_member](#get_launch_profile_member)
    - [get_streaming_image](#get_streaming_image)
    - [get_streaming_session](#get_streaming_session)
    - [get_streaming_session_stream](#get_streaming_session_stream)
    - [get_studio](#get_studio)
    - [get_studio_component](#get_studio_component)
    - [get_studio_member](#get_studio_member)
    - [list_eula_acceptances](#list_eula_acceptances)
    - [list_eulas](#list_eulas)
    - [list_launch_profile_members](#list_launch_profile_members)
    - [list_launch_profiles](#list_launch_profiles)
    - [list_streaming_images](#list_streaming_images)
    - [list_streaming_sessions](#list_streaming_sessions)
    - [list_studio_components](#list_studio_components)
    - [list_studio_members](#list_studio_members)
    - [list_studios](#list_studios)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_launch_profile_members](#put_launch_profile_members)
    - [put_studio_members](#put_studio_members)
    - [start_studio_sso_configuration_repair](#start_studio_sso_configuration_repair)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_launch_profile](#update_launch_profile)
    - [update_launch_profile_member](#update_launch_profile_member)
    - [update_streaming_image](#update_streaming_image)
    - [update_studio](#update_studio)
    - [update_studio_component](#update_studio_component)
    - [get_paginator](#get_paginator)

## NimbleStudioClient

Type annotations for `boto3.client("nimble")`

Can be used directly:

```python
from mypy_boto3_nimble.client import NimbleStudioClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_nimble.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### accept_eulas

Type annotations for `boto3.client("nimble").accept_eulas` method.

[Client.accept_eulas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.accept_eulas)

```python
def accept_eulas(
    self,
    studioId: str,
    clientToken: str = None,
    eulaIds: List[str] = None
) -> AcceptEulasResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("nimble").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_launch_profile

Type annotations for `boto3.client("nimble").create_launch_profile` method.

[Client.create_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_launch_profile)

```python
def create_launch_profile(
    self,
    ec2SubnetIds: List[str],
    launchProfileProtocolVersions: List[str],
    name: str,
    streamConfiguration: StreamConfigurationCreateTypeDef,
    studioComponentIds: List[str],
    studioId: str,
    clientToken: str = None,
    description: str = None,
    tags: Dict[str, str] = None
) -> CreateLaunchProfileResponseTypeDef:
    pass
```

### create_streaming_image

Type annotations for `boto3.client("nimble").create_streaming_image` method.

[Client.create_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_streaming_image)

```python
def create_streaming_image(
    self,
    ec2ImageId: str,
    name: str,
    studioId: str,
    clientToken: str = None,
    description: str = None,
    tags: Dict[str, str] = None
) -> CreateStreamingImageResponseTypeDef:
    pass
```

### create_streaming_session

Type annotations for `boto3.client("nimble").create_streaming_session` method.

[Client.create_streaming_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session)

```python
def create_streaming_session(
    self,
    studioId: str,
    clientToken: str = None,
    ec2InstanceType: StreamingInstanceType = None,
    launchProfileId: str = None,
    streamingImageId: str = None,
    tags: Dict[str, str] = None
) -> CreateStreamingSessionResponseTypeDef:
    pass
```

### create_streaming_session_stream

Type annotations for `boto3.client("nimble").create_streaming_session_stream` method.

[Client.create_streaming_session_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session_stream)

```python
def create_streaming_session_stream(
    self,
    sessionId: str,
    studioId: str,
    clientToken: str = None,
    expirationInSeconds: int = None
) -> CreateStreamingSessionStreamResponseTypeDef:
    pass
```

### create_studio

Type annotations for `boto3.client("nimble").create_studio` method.

[Client.create_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_studio)

```python
def create_studio(
    self,
    adminRoleArn: str,
    displayName: str,
    studioName: str,
    userRoleArn: str,
    clientToken: str = None,
    studioEncryptionConfiguration: "StudioEncryptionConfigurationTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateStudioResponseTypeDef:
    pass
```

### create_studio_component

Type annotations for `boto3.client("nimble").create_studio_component` method.

[Client.create_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.create_studio_component)

```python
def create_studio_component(
    self,
    name: str,
    studioId: str,
    type: StudioComponentType,
    clientToken: str = None,
    configuration: "StudioComponentConfigurationTypeDef" = None,
    description: str = None,
    ec2SecurityGroupIds: List[str] = None,
    initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
    scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
    subtype: StudioComponentSubtype = None,
    tags: Dict[str, str] = None
) -> CreateStudioComponentResponseTypeDef:
    pass
```

### delete_launch_profile

Type annotations for `boto3.client("nimble").delete_launch_profile` method.

[Client.delete_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile)

```python
def delete_launch_profile(
    self,
    launchProfileId: str,
    studioId: str,
    clientToken: str = None
) -> DeleteLaunchProfileResponseTypeDef:
    pass
```

### delete_launch_profile_member

Type annotations for `boto3.client("nimble").delete_launch_profile_member` method.

[Client.delete_launch_profile_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile_member)

```python
def delete_launch_profile_member(
    self,
    launchProfileId: str,
    principalId: str,
    studioId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### delete_streaming_image

Type annotations for `boto3.client("nimble").delete_streaming_image` method.

[Client.delete_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_image)

```python
def delete_streaming_image(
    self,
    streamingImageId: str,
    studioId: str,
    clientToken: str = None
) -> DeleteStreamingImageResponseTypeDef:
    pass
```

### delete_streaming_session

Type annotations for `boto3.client("nimble").delete_streaming_session` method.

[Client.delete_streaming_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_session)

```python
def delete_streaming_session(
    self,
    sessionId: str,
    studioId: str,
    clientToken: str = None
) -> DeleteStreamingSessionResponseTypeDef:
    pass
```

### delete_studio

Type annotations for `boto3.client("nimble").delete_studio` method.

[Client.delete_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_studio)

```python
def delete_studio(
    self,
    studioId: str,
    clientToken: str = None
) -> DeleteStudioResponseTypeDef:
    pass
```

### delete_studio_component

Type annotations for `boto3.client("nimble").delete_studio_component` method.

[Client.delete_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_studio_component)

```python
def delete_studio_component(
    self,
    studioComponentId: str,
    studioId: str,
    clientToken: str = None
) -> DeleteStudioComponentResponseTypeDef:
    pass
```

### delete_studio_member

Type annotations for `boto3.client("nimble").delete_studio_member` method.

[Client.delete_studio_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.delete_studio_member)

```python
def delete_studio_member(
    self,
    principalId: str,
    studioId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("nimble").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.generate_presigned_url)

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

### get_eula

Type annotations for `boto3.client("nimble").get_eula` method.

[Client.get_eula documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_eula)

```python
def get_eula(
    self,
    eulaId: str
) -> GetEulaResponseTypeDef:
    pass
```

### get_launch_profile

Type annotations for `boto3.client("nimble").get_launch_profile` method.

[Client.get_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile)

```python
def get_launch_profile(
    self,
    launchProfileId: str,
    studioId: str
) -> GetLaunchProfileResponseTypeDef:
    pass
```

### get_launch_profile_details

Type annotations for `boto3.client("nimble").get_launch_profile_details` method.

[Client.get_launch_profile_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_details)

```python
def get_launch_profile_details(
    self,
    launchProfileId: str,
    studioId: str
) -> GetLaunchProfileDetailsResponseTypeDef:
    pass
```

### get_launch_profile_initialization

Type annotations for `boto3.client("nimble").get_launch_profile_initialization` method.

[Client.get_launch_profile_initialization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_initialization)

```python
def get_launch_profile_initialization(
    self,
    launchProfileId: str,
    launchProfileProtocolVersions: List[str],
    launchPurpose: str,
    platform: str,
    studioId: str
) -> GetLaunchProfileInitializationResponseTypeDef:
    pass
```

### get_launch_profile_member

Type annotations for `boto3.client("nimble").get_launch_profile_member` method.

[Client.get_launch_profile_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_member)

```python
def get_launch_profile_member(
    self,
    launchProfileId: str,
    principalId: str,
    studioId: str
) -> GetLaunchProfileMemberResponseTypeDef:
    pass
```

### get_streaming_image

Type annotations for `boto3.client("nimble").get_streaming_image` method.

[Client.get_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_image)

```python
def get_streaming_image(
    self,
    streamingImageId: str,
    studioId: str
) -> GetStreamingImageResponseTypeDef:
    pass
```

### get_streaming_session

Type annotations for `boto3.client("nimble").get_streaming_session` method.

[Client.get_streaming_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session)

```python
def get_streaming_session(
    self,
    sessionId: str,
    studioId: str
) -> GetStreamingSessionResponseTypeDef:
    pass
```

### get_streaming_session_stream

Type annotations for `boto3.client("nimble").get_streaming_session_stream` method.

[Client.get_streaming_session_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_stream)

```python
def get_streaming_session_stream(
    self,
    sessionId: str,
    streamId: str,
    studioId: str
) -> GetStreamingSessionStreamResponseTypeDef:
    pass
```

### get_studio

Type annotations for `boto3.client("nimble").get_studio` method.

[Client.get_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_studio)

```python
def get_studio(
    self,
    studioId: str
) -> GetStudioResponseTypeDef:
    pass
```

### get_studio_component

Type annotations for `boto3.client("nimble").get_studio_component` method.

[Client.get_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_studio_component)

```python
def get_studio_component(
    self,
    studioComponentId: str,
    studioId: str
) -> GetStudioComponentResponseTypeDef:
    pass
```

### get_studio_member

Type annotations for `boto3.client("nimble").get_studio_member` method.

[Client.get_studio_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.get_studio_member)

```python
def get_studio_member(
    self,
    principalId: str,
    studioId: str
) -> GetStudioMemberResponseTypeDef:
    pass
```

### list_eula_acceptances

Type annotations for `boto3.client("nimble").list_eula_acceptances` method.

[Client.list_eula_acceptances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_eula_acceptances)

```python
def list_eula_acceptances(
    self,
    studioId: str,
    eulaIds: List[str] = None,
    nextToken: str = None
) -> ListEulaAcceptancesResponseTypeDef:
    pass
```

### list_eulas

Type annotations for `boto3.client("nimble").list_eulas` method.

[Client.list_eulas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_eulas)

```python
def list_eulas(
    self,
    eulaIds: List[str] = None,
    nextToken: str = None
) -> ListEulasResponseTypeDef:
    pass
```

### list_launch_profile_members

Type annotations for `boto3.client("nimble").list_launch_profile_members` method.

[Client.list_launch_profile_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_launch_profile_members)

```python
def list_launch_profile_members(
    self,
    launchProfileId: str,
    studioId: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListLaunchProfileMembersResponseTypeDef:
    pass
```

### list_launch_profiles

Type annotations for `boto3.client("nimble").list_launch_profiles` method.

[Client.list_launch_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_launch_profiles)

```python
def list_launch_profiles(
    self,
    studioId: str,
    maxResults: int = None,
    nextToken: str = None,
    principalId: str = None,
    states: List[str] = None
) -> ListLaunchProfilesResponseTypeDef:
    pass
```

### list_streaming_images

Type annotations for `boto3.client("nimble").list_streaming_images` method.

[Client.list_streaming_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_streaming_images)

```python
def list_streaming_images(
    self,
    studioId: str,
    nextToken: str = None,
    owner: str = None
) -> ListStreamingImagesResponseTypeDef:
    pass
```

### list_streaming_sessions

Type annotations for `boto3.client("nimble").list_streaming_sessions` method.

[Client.list_streaming_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_streaming_sessions)

```python
def list_streaming_sessions(
    self,
    studioId: str,
    createdBy: str = None,
    nextToken: str = None,
    sessionIds: str = None
) -> ListStreamingSessionsResponseTypeDef:
    pass
```

### list_studio_components

Type annotations for `boto3.client("nimble").list_studio_components` method.

[Client.list_studio_components documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_studio_components)

```python
def list_studio_components(
    self,
    studioId: str,
    maxResults: int = None,
    nextToken: str = None,
    states: List[str] = None,
    types: List[str] = None
) -> ListStudioComponentsResponseTypeDef:
    pass
```

### list_studio_members

Type annotations for `boto3.client("nimble").list_studio_members` method.

[Client.list_studio_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_studio_members)

```python
def list_studio_members(
    self,
    studioId: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListStudioMembersResponseTypeDef:
    pass
```

### list_studios

Type annotations for `boto3.client("nimble").list_studios` method.

[Client.list_studios documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_studios)

```python
def list_studios(
    self,
    nextToken: str = None
) -> ListStudiosResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("nimble").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_launch_profile_members

Type annotations for `boto3.client("nimble").put_launch_profile_members` method.

[Client.put_launch_profile_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.put_launch_profile_members)

```python
def put_launch_profile_members(
    self,
    identityStoreId: str,
    launchProfileId: str,
    members: List[NewLaunchProfileMemberTypeDef],
    studioId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### put_studio_members

Type annotations for `boto3.client("nimble").put_studio_members` method.

[Client.put_studio_members documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.put_studio_members)

```python
def put_studio_members(
    self,
    identityStoreId: str,
    members: List[NewStudioMemberTypeDef],
    studioId: str,
    clientToken: str = None
) -> Dict[str, Any]:
    pass
```

### start_studio_sso_configuration_repair

Type annotations for `boto3.client("nimble").start_studio_sso_configuration_repair` method.

[Client.start_studio_sso_configuration_repair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.start_studio_sso_configuration_repair)

```python
def start_studio_sso_configuration_repair(
    self,
    studioId: str,
    clientToken: str = None
) -> StartStudioSSOConfigurationRepairResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("nimble").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str] = None
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("nimble").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_launch_profile

Type annotations for `boto3.client("nimble").update_launch_profile` method.

[Client.update_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile)

```python
def update_launch_profile(
    self,
    launchProfileId: str,
    studioId: str,
    clientToken: str = None,
    description: str = None,
    launchProfileProtocolVersions: List[str] = None,
    name: str = None,
    streamConfiguration: StreamConfigurationCreateTypeDef = None,
    studioComponentIds: List[str] = None
) -> UpdateLaunchProfileResponseTypeDef:
    pass
```

### update_launch_profile_member

Type annotations for `boto3.client("nimble").update_launch_profile_member` method.

[Client.update_launch_profile_member documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile_member)

```python
def update_launch_profile_member(
    self,
    launchProfileId: str,
    persona: Literal['USER'],
    principalId: str,
    studioId: str,
    clientToken: str = None
) -> UpdateLaunchProfileMemberResponseTypeDef:
    pass
```

### update_streaming_image

Type annotations for `boto3.client("nimble").update_streaming_image` method.

[Client.update_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_streaming_image)

```python
def update_streaming_image(
    self,
    streamingImageId: str,
    studioId: str,
    clientToken: str = None,
    description: str = None,
    name: str = None
) -> UpdateStreamingImageResponseTypeDef:
    pass
```

### update_studio

Type annotations for `boto3.client("nimble").update_studio` method.

[Client.update_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_studio)

```python
def update_studio(
    self,
    studioId: str,
    adminRoleArn: str = None,
    clientToken: str = None,
    displayName: str = None,
    userRoleArn: str = None
) -> UpdateStudioResponseTypeDef:
    pass
```

### update_studio_component

Type annotations for `boto3.client("nimble").update_studio_component` method.

[Client.update_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Client.update_studio_component)

```python
def update_studio_component(
    self,
    studioComponentId: str,
    studioId: str,
    clientToken: str = None,
    configuration: "StudioComponentConfigurationTypeDef" = None,
    description: str = None,
    ec2SecurityGroupIds: List[str] = None,
    initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
    name: str = None,
    scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
    subtype: StudioComponentSubtype = None,
    type: StudioComponentType = None
) -> UpdateStudioComponentResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("nimble").get_paginator` method with overloads.

- `client.get_paginator("list_eula_acceptances")` -> [ListEulaAcceptancesPaginator](./paginators.md#listeulaacceptancespaginator)
- `client.get_paginator("list_eulas")` -> [ListEulasPaginator](./paginators.md#listeulaspaginator)
- `client.get_paginator("list_launch_profile_members")` -> [ListLaunchProfileMembersPaginator](./paginators.md#listlaunchprofilememberspaginator)
- `client.get_paginator("list_launch_profiles")` -> [ListLaunchProfilesPaginator](./paginators.md#listlaunchprofilespaginator)
- `client.get_paginator("list_streaming_images")` -> [ListStreamingImagesPaginator](./paginators.md#liststreamingimagespaginator)
- `client.get_paginator("list_streaming_sessions")` -> [ListStreamingSessionsPaginator](./paginators.md#liststreamingsessionspaginator)
- `client.get_paginator("list_studio_components")` -> [ListStudioComponentsPaginator](./paginators.md#liststudiocomponentspaginator)
- `client.get_paginator("list_studio_members")` -> [ListStudioMembersPaginator](./paginators.md#liststudiomemberspaginator)
- `client.get_paginator("list_studios")` -> [ListStudiosPaginator](./paginators.md#liststudiospaginator)


