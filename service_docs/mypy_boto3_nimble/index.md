# Type annotations for boto3 NimbleStudio module

> [Index](../index.md) > NimbleStudio

Auto-generated documentation for [NimbleStudio](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio)
type annotations stubs module [mypy_boto3_nimble](https://pypi.org/project/mypy-boto3-nimble/).

```bash
pip install mypy-boto3-nimble
```

- [Type annotations for boto3 NimbleStudio module](#type-annotations-for-boto3-nimblestudio-module)
  - [NimbleStudioClient](#nimblestudioclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## NimbleStudioClient

Type annotations for  `boto3.client("nimble")` as [NimbleStudioClient](./client.md)

Can be used directly:

```python
from mypy_boto3_nimble.client import NimbleStudioClient
```


NimbleStudioClient [exceptions](./client.md#exceptions)



### Methods
- [accept_eulas](./client.md#accept-eulas)
- [can_paginate](./client.md#can-paginate)
- [create_launch_profile](./client.md#create-launch-profile)
- [create_streaming_image](./client.md#create-streaming-image)
- [create_streaming_session](./client.md#create-streaming-session)
- [create_streaming_session_stream](./client.md#create-streaming-session-stream)
- [create_studio](./client.md#create-studio)
- [create_studio_component](./client.md#create-studio-component)
- [delete_launch_profile](./client.md#delete-launch-profile)
- [delete_launch_profile_member](./client.md#delete-launch-profile-member)
- [delete_streaming_image](./client.md#delete-streaming-image)
- [delete_streaming_session](./client.md#delete-streaming-session)
- [delete_studio](./client.md#delete-studio)
- [delete_studio_component](./client.md#delete-studio-component)
- [delete_studio_member](./client.md#delete-studio-member)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_eula](./client.md#get-eula)
- [get_launch_profile](./client.md#get-launch-profile)
- [get_launch_profile_details](./client.md#get-launch-profile-details)
- [get_launch_profile_initialization](./client.md#get-launch-profile-initialization)
- [get_launch_profile_member](./client.md#get-launch-profile-member)
- [get_paginator](./client.md#get-paginator)
- [get_streaming_image](./client.md#get-streaming-image)
- [get_streaming_session](./client.md#get-streaming-session)
- [get_streaming_session_stream](./client.md#get-streaming-session-stream)
- [get_studio](./client.md#get-studio)
- [get_studio_component](./client.md#get-studio-component)
- [get_studio_member](./client.md#get-studio-member)
- [list_eula_acceptances](./client.md#list-eula-acceptances)
- [list_eulas](./client.md#list-eulas)
- [list_launch_profile_members](./client.md#list-launch-profile-members)
- [list_launch_profiles](./client.md#list-launch-profiles)
- [list_streaming_images](./client.md#list-streaming-images)
- [list_streaming_sessions](./client.md#list-streaming-sessions)
- [list_studio_components](./client.md#list-studio-components)
- [list_studio_members](./client.md#list-studio-members)
- [list_studios](./client.md#list-studios)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_launch_profile_members](./client.md#put-launch-profile-members)
- [put_studio_members](./client.md#put-studio-members)
- [start_studio_sso_configuration_repair](./client.md#start-studio-sso-configuration-repair)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_launch_profile](./client.md#update-launch-profile)
- [update_launch_profile_member](./client.md#update-launch-profile-member)
- [update_streaming_image](./client.md#update-streaming-image)
- [update_studio](./client.md#update-studio)
- [update_studio_component](./client.md#update-studio-component)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("nimble").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_nimble.paginators import ListEulaAcceptancesPaginator, ...
```

- [ListEulaAcceptancesPaginator](./paginators.md#listeulaacceptancespaginator)
- [ListEulasPaginator](./paginators.md#listeulaspaginator)
- [ListLaunchProfileMembersPaginator](./paginators.md#listlaunchprofilememberspaginator)
- [ListLaunchProfilesPaginator](./paginators.md#listlaunchprofilespaginator)
- [ListStreamingImagesPaginator](./paginators.md#liststreamingimagespaginator)
- [ListStreamingSessionsPaginator](./paginators.md#liststreamingsessionspaginator)
- [ListStudioComponentsPaginator](./paginators.md#liststudiocomponentspaginator)
- [ListStudioMembersPaginator](./paginators.md#liststudiomemberspaginator)
- [ListStudiosPaginator](./paginators.md#liststudiospaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_nimble.literals import LaunchProfilePersona, ...
```

- [LaunchProfilePersona](./literals.md#launchprofilepersona)
- [LaunchProfilePlatform](./literals.md#launchprofileplatform)
- [LaunchProfileState](./literals.md#launchprofilestate)
- [LaunchProfileStatusCode](./literals.md#launchprofilestatuscode)
- [ListEulaAcceptancesPaginatorName](./literals.md#listeulaacceptancespaginatorname)
- [ListEulasPaginatorName](./literals.md#listeulaspaginatorname)
- [ListLaunchProfileMembersPaginatorName](./literals.md#listlaunchprofilememberspaginatorname)
- [ListLaunchProfilesPaginatorName](./literals.md#listlaunchprofilespaginatorname)
- [ListStreamingImagesPaginatorName](./literals.md#liststreamingimagespaginatorname)
- [ListStreamingSessionsPaginatorName](./literals.md#liststreamingsessionspaginatorname)
- [ListStudioComponentsPaginatorName](./literals.md#liststudiocomponentspaginatorname)
- [ListStudioMembersPaginatorName](./literals.md#liststudiomemberspaginatorname)
- [ListStudiosPaginatorName](./literals.md#liststudiospaginatorname)
- [StreamingClipboardMode](./literals.md#streamingclipboardmode)
- [StreamingImageEncryptionConfigurationKeyType](./literals.md#streamingimageencryptionconfigurationkeytype)
- [StreamingImageState](./literals.md#streamingimagestate)
- [StreamingImageStatusCode](./literals.md#streamingimagestatuscode)
- [StreamingInstanceType](./literals.md#streaminginstancetype)
- [StreamingSessionState](./literals.md#streamingsessionstate)
- [StreamingSessionStatusCode](./literals.md#streamingsessionstatuscode)
- [StreamingSessionStreamState](./literals.md#streamingsessionstreamstate)
- [StreamingSessionStreamStatusCode](./literals.md#streamingsessionstreamstatuscode)
- [StudioComponentInitializationScriptRunContext](./literals.md#studiocomponentinitializationscriptruncontext)
- [StudioComponentState](./literals.md#studiocomponentstate)
- [StudioComponentStatusCode](./literals.md#studiocomponentstatuscode)
- [StudioComponentSubtype](./literals.md#studiocomponentsubtype)
- [StudioComponentType](./literals.md#studiocomponenttype)
- [StudioEncryptionConfigurationKeyType](./literals.md#studioencryptionconfigurationkeytype)
- [StudioPersona](./literals.md#studiopersona)
- [StudioState](./literals.md#studiostate)
- [StudioStatusCode](./literals.md#studiostatuscode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_nimble.type_defs import AcceptEulasResponseTypeDef, ...
```

- [AcceptEulasResponseTypeDef](./type_defs.md#accepteulasresponsetypedef)
- [ActiveDirectoryComputerAttributeTypeDef](./type_defs.md#activedirectorycomputerattributetypedef)
- [ActiveDirectoryConfigurationTypeDef](./type_defs.md#activedirectoryconfigurationtypedef)
- [ComputeFarmConfigurationTypeDef](./type_defs.md#computefarmconfigurationtypedef)
- [CreateLaunchProfileResponseTypeDef](./type_defs.md#createlaunchprofileresponsetypedef)
- [CreateStreamingImageResponseTypeDef](./type_defs.md#createstreamingimageresponsetypedef)
- [CreateStreamingSessionResponseTypeDef](./type_defs.md#createstreamingsessionresponsetypedef)
- [CreateStreamingSessionStreamResponseTypeDef](./type_defs.md#createstreamingsessionstreamresponsetypedef)
- [CreateStudioComponentResponseTypeDef](./type_defs.md#createstudiocomponentresponsetypedef)
- [CreateStudioResponseTypeDef](./type_defs.md#createstudioresponsetypedef)
- [DeleteLaunchProfileResponseTypeDef](./type_defs.md#deletelaunchprofileresponsetypedef)
- [DeleteStreamingImageResponseTypeDef](./type_defs.md#deletestreamingimageresponsetypedef)
- [DeleteStreamingSessionResponseTypeDef](./type_defs.md#deletestreamingsessionresponsetypedef)
- [DeleteStudioComponentResponseTypeDef](./type_defs.md#deletestudiocomponentresponsetypedef)
- [DeleteStudioResponseTypeDef](./type_defs.md#deletestudioresponsetypedef)
- [EulaAcceptanceTypeDef](./type_defs.md#eulaacceptancetypedef)
- [EulaTypeDef](./type_defs.md#eulatypedef)
- [GetEulaResponseTypeDef](./type_defs.md#geteularesponsetypedef)
- [GetLaunchProfileDetailsResponseTypeDef](./type_defs.md#getlaunchprofiledetailsresponsetypedef)
- [GetLaunchProfileInitializationResponseTypeDef](./type_defs.md#getlaunchprofileinitializationresponsetypedef)
- [GetLaunchProfileMemberResponseTypeDef](./type_defs.md#getlaunchprofilememberresponsetypedef)
- [GetLaunchProfileResponseTypeDef](./type_defs.md#getlaunchprofileresponsetypedef)
- [GetStreamingImageResponseTypeDef](./type_defs.md#getstreamingimageresponsetypedef)
- [GetStreamingSessionResponseTypeDef](./type_defs.md#getstreamingsessionresponsetypedef)
- [GetStreamingSessionStreamResponseTypeDef](./type_defs.md#getstreamingsessionstreamresponsetypedef)
- [GetStudioComponentResponseTypeDef](./type_defs.md#getstudiocomponentresponsetypedef)
- [GetStudioMemberResponseTypeDef](./type_defs.md#getstudiomemberresponsetypedef)
- [GetStudioResponseTypeDef](./type_defs.md#getstudioresponsetypedef)
- [LaunchProfileInitializationActiveDirectoryTypeDef](./type_defs.md#launchprofileinitializationactivedirectorytypedef)
- [LaunchProfileInitializationScriptTypeDef](./type_defs.md#launchprofileinitializationscripttypedef)
- [LaunchProfileInitializationTypeDef](./type_defs.md#launchprofileinitializationtypedef)
- [LaunchProfileMembershipTypeDef](./type_defs.md#launchprofilemembershiptypedef)
- [LaunchProfileTypeDef](./type_defs.md#launchprofiletypedef)
- [LicenseServiceConfigurationTypeDef](./type_defs.md#licenseserviceconfigurationtypedef)
- [ListEulaAcceptancesResponseTypeDef](./type_defs.md#listeulaacceptancesresponsetypedef)
- [ListEulasResponseTypeDef](./type_defs.md#listeulasresponsetypedef)
- [ListLaunchProfileMembersResponseTypeDef](./type_defs.md#listlaunchprofilemembersresponsetypedef)
- [ListLaunchProfilesResponseTypeDef](./type_defs.md#listlaunchprofilesresponsetypedef)
- [ListStreamingImagesResponseTypeDef](./type_defs.md#liststreamingimagesresponsetypedef)
- [ListStreamingSessionsResponseTypeDef](./type_defs.md#liststreamingsessionsresponsetypedef)
- [ListStudioComponentsResponseTypeDef](./type_defs.md#liststudiocomponentsresponsetypedef)
- [ListStudioMembersResponseTypeDef](./type_defs.md#liststudiomembersresponsetypedef)
- [ListStudiosResponseTypeDef](./type_defs.md#liststudiosresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NewLaunchProfileMemberTypeDef](./type_defs.md#newlaunchprofilemembertypedef)
- [NewStudioMemberTypeDef](./type_defs.md#newstudiomembertypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ScriptParameterKeyValueTypeDef](./type_defs.md#scriptparameterkeyvaluetypedef)
- [SharedFileSystemConfigurationTypeDef](./type_defs.md#sharedfilesystemconfigurationtypedef)
- [StartStudioSSOConfigurationRepairResponseTypeDef](./type_defs.md#startstudiossoconfigurationrepairresponsetypedef)
- [StreamConfigurationCreateTypeDef](./type_defs.md#streamconfigurationcreatetypedef)
- [StreamConfigurationTypeDef](./type_defs.md#streamconfigurationtypedef)
- [StreamingImageEncryptionConfigurationTypeDef](./type_defs.md#streamingimageencryptionconfigurationtypedef)
- [StreamingImageTypeDef](./type_defs.md#streamingimagetypedef)
- [StreamingSessionStreamTypeDef](./type_defs.md#streamingsessionstreamtypedef)
- [StreamingSessionTypeDef](./type_defs.md#streamingsessiontypedef)
- [StudioComponentConfigurationTypeDef](./type_defs.md#studiocomponentconfigurationtypedef)
- [StudioComponentInitializationScriptTypeDef](./type_defs.md#studiocomponentinitializationscripttypedef)
- [StudioComponentSummaryTypeDef](./type_defs.md#studiocomponentsummarytypedef)
- [StudioComponentTypeDef](./type_defs.md#studiocomponenttypedef)
- [StudioEncryptionConfigurationTypeDef](./type_defs.md#studioencryptionconfigurationtypedef)
- [StudioMembershipTypeDef](./type_defs.md#studiomembershiptypedef)
- [StudioTypeDef](./type_defs.md#studiotypedef)
- [UpdateLaunchProfileMemberResponseTypeDef](./type_defs.md#updatelaunchprofilememberresponsetypedef)
- [UpdateLaunchProfileResponseTypeDef](./type_defs.md#updatelaunchprofileresponsetypedef)
- [UpdateStreamingImageResponseTypeDef](./type_defs.md#updatestreamingimageresponsetypedef)
- [UpdateStudioComponentResponseTypeDef](./type_defs.md#updatestudiocomponentresponsetypedef)
- [UpdateStudioResponseTypeDef](./type_defs.md#updatestudioresponsetypedef)
