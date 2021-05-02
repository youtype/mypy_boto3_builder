# Literals for boto3 NimbleStudio module

> [Index](../index.md) > [NimbleStudio](./index.md) > Literals

Auto-generated documentation for [NimbleStudio](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio)
type annotations stubs module [mypy_boto3_nimble](https://pypi.org/project/mypy-boto3-nimble/).

- [Literals for boto3 NimbleStudio module](#literals-for-boto3-nimblestudio-module)
  - [LaunchProfilePersona](#launchprofilepersona)
  - [LaunchProfilePlatform](#launchprofileplatform)
  - [LaunchProfileState](#launchprofilestate)
  - [LaunchProfileStatusCode](#launchprofilestatuscode)
  - [ListEulaAcceptancesPaginatorName](#listeulaacceptancespaginatorname)
  - [ListEulasPaginatorName](#listeulaspaginatorname)
  - [ListLaunchProfileMembersPaginatorName](#listlaunchprofilememberspaginatorname)
  - [ListLaunchProfilesPaginatorName](#listlaunchprofilespaginatorname)
  - [ListStreamingImagesPaginatorName](#liststreamingimagespaginatorname)
  - [ListStreamingSessionsPaginatorName](#liststreamingsessionspaginatorname)
  - [ListStudioComponentsPaginatorName](#liststudiocomponentspaginatorname)
  - [ListStudioMembersPaginatorName](#liststudiomemberspaginatorname)
  - [ListStudiosPaginatorName](#liststudiospaginatorname)
  - [StreamingClipboardMode](#streamingclipboardmode)
  - [StreamingImageEncryptionConfigurationKeyType](#streamingimageencryptionconfigurationkeytype)
  - [StreamingImageState](#streamingimagestate)
  - [StreamingImageStatusCode](#streamingimagestatuscode)
  - [StreamingInstanceType](#streaminginstancetype)
  - [StreamingSessionState](#streamingsessionstate)
  - [StreamingSessionStatusCode](#streamingsessionstatuscode)
  - [StreamingSessionStreamState](#streamingsessionstreamstate)
  - [StreamingSessionStreamStatusCode](#streamingsessionstreamstatuscode)
  - [StudioComponentInitializationScriptRunContext](#studiocomponentinitializationscriptruncontext)
  - [StudioComponentState](#studiocomponentstate)
  - [StudioComponentStatusCode](#studiocomponentstatuscode)
  - [StudioComponentSubtype](#studiocomponentsubtype)
  - [StudioComponentType](#studiocomponenttype)
  - [StudioEncryptionConfigurationKeyType](#studioencryptionconfigurationkeytype)
  - [StudioPersona](#studiopersona)
  - [StudioState](#studiostate)
  - [StudioStatusCode](#studiostatuscode)

## LaunchProfilePersona

```python
from mypy_boto3_nimble.literals import LaunchProfilePersona
```

Values:

- `USER`

## LaunchProfilePlatform

```python
from mypy_boto3_nimble.literals import LaunchProfilePlatform
```

Values:

- `LINUX`
- `WINDOWS`

## LaunchProfileState

```python
from mypy_boto3_nimble.literals import LaunchProfileState
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETED`
- `READY`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## LaunchProfileStatusCode

```python
from mypy_boto3_nimble.literals import LaunchProfileStatusCode
```

Values:

- `ENCRYPTION_KEY_ACCESS_DENIED`
- `ENCRYPTION_KEY_NOT_FOUND`
- `INTERNAL_ERROR`
- `INVALID_SUBNETS_PROVIDED`
- `LAUNCH_PROFILE_CREATE_IN_PROGRESS`
- `LAUNCH_PROFILE_CREATED`
- `LAUNCH_PROFILE_DELETE_IN_PROGRESS`
- `LAUNCH_PROFILE_DELETED`
- `LAUNCH_PROFILE_UPDATE_IN_PROGRESS`
- `LAUNCH_PROFILE_UPDATED`
- `LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED`
- `STREAMING_IMAGE_NOT_FOUND`
- `STREAMING_IMAGE_NOT_READY`

## ListEulaAcceptancesPaginatorName

```python
from mypy_boto3_nimble.literals import ListEulaAcceptancesPaginatorName
```

Values:

- `list_eula_acceptances`

## ListEulasPaginatorName

```python
from mypy_boto3_nimble.literals import ListEulasPaginatorName
```

Values:

- `list_eulas`

## ListLaunchProfileMembersPaginatorName

```python
from mypy_boto3_nimble.literals import ListLaunchProfileMembersPaginatorName
```

Values:

- `list_launch_profile_members`

## ListLaunchProfilesPaginatorName

```python
from mypy_boto3_nimble.literals import ListLaunchProfilesPaginatorName
```

Values:

- `list_launch_profiles`

## ListStreamingImagesPaginatorName

```python
from mypy_boto3_nimble.literals import ListStreamingImagesPaginatorName
```

Values:

- `list_streaming_images`

## ListStreamingSessionsPaginatorName

```python
from mypy_boto3_nimble.literals import ListStreamingSessionsPaginatorName
```

Values:

- `list_streaming_sessions`

## ListStudioComponentsPaginatorName

```python
from mypy_boto3_nimble.literals import ListStudioComponentsPaginatorName
```

Values:

- `list_studio_components`

## ListStudioMembersPaginatorName

```python
from mypy_boto3_nimble.literals import ListStudioMembersPaginatorName
```

Values:

- `list_studio_members`

## ListStudiosPaginatorName

```python
from mypy_boto3_nimble.literals import ListStudiosPaginatorName
```

Values:

- `list_studios`

## StreamingClipboardMode

```python
from mypy_boto3_nimble.literals import StreamingClipboardMode
```

Values:

- `DISABLED`
- `ENABLED`

## StreamingImageEncryptionConfigurationKeyType

```python
from mypy_boto3_nimble.literals import StreamingImageEncryptionConfigurationKeyType
```

Values:

- `CUSTOMER_MANAGED_KEY`

## StreamingImageState

```python
from mypy_boto3_nimble.literals import StreamingImageState
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETED`
- `READY`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## StreamingImageStatusCode

```python
from mypy_boto3_nimble.literals import StreamingImageStatusCode
```

Values:

- `INTERNAL_ERROR`
- `STREAMING_IMAGE_CREATE_IN_PROGRESS`
- `STREAMING_IMAGE_DELETE_IN_PROGRESS`
- `STREAMING_IMAGE_DELETED`
- `STREAMING_IMAGE_READY`
- `STREAMING_IMAGE_UPDATE_IN_PROGRESS`

## StreamingInstanceType

```python
from mypy_boto3_nimble.literals import StreamingInstanceType
```

Values:

- `g4dn.12xlarge`
- `g4dn.16xlarge`
- `g4dn.2xlarge`
- `g4dn.4xlarge`
- `g4dn.8xlarge`
- `g4dn.xlarge`

## StreamingSessionState

```python
from mypy_boto3_nimble.literals import StreamingSessionState
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETED`
- `READY`

## StreamingSessionStatusCode

```python
from mypy_boto3_nimble.literals import StreamingSessionStatusCode
```

Values:

- `ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR`
- `DECRYPT_STREAMING_IMAGE_ERROR`
- `INITIALIZATION_SCRIPT_ERROR`
- `INSUFFICIENT_CAPACITY`
- `INTERNAL_ERROR`
- `NETWORK_CONNECTION_ERROR`
- `NETWORK_INTERFACE_ERROR`
- `STREAMING_SESSION_CREATE_IN_PROGRESS`
- `STREAMING_SESSION_DELETE_IN_PROGRESS`
- `STREAMING_SESSION_DELETED`
- `STREAMING_SESSION_READY`

## StreamingSessionStreamState

```python
from mypy_boto3_nimble.literals import StreamingSessionStreamState
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETED`
- `READY`

## StreamingSessionStreamStatusCode

```python
from mypy_boto3_nimble.literals import StreamingSessionStreamStatusCode
```

Values:

- `INTERNAL_ERROR`
- `NETWORK_CONNECTION_ERROR`
- `STREAM_CREATE_IN_PROGRESS`
- `STREAM_DELETE_IN_PROGRESS`
- `STREAM_DELETED`
- `STREAM_READY`

## StudioComponentInitializationScriptRunContext

```python
from mypy_boto3_nimble.literals import StudioComponentInitializationScriptRunContext
```

Values:

- `SYSTEM_INITIALIZATION`
- `USER_INITIALIZATION`

## StudioComponentState

```python
from mypy_boto3_nimble.literals import StudioComponentState
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETED`
- `READY`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## StudioComponentStatusCode

```python
from mypy_boto3_nimble.literals import StudioComponentStatusCode
```

Values:

- `ACTIVE_DIRECTORY_ALREADY_EXISTS`
- `ENCRYPTION_KEY_ACCESS_DENIED`
- `ENCRYPTION_KEY_NOT_FOUND`
- `INTERNAL_ERROR`
- `STUDIO_COMPONENT_CREATE_IN_PROGRESS`
- `STUDIO_COMPONENT_CREATED`
- `STUDIO_COMPONENT_DELETE_IN_PROGRESS`
- `STUDIO_COMPONENT_DELETED`
- `STUDIO_COMPONENT_UPDATE_IN_PROGRESS`
- `STUDIO_COMPONENT_UPDATED`

## StudioComponentSubtype

```python
from mypy_boto3_nimble.literals import StudioComponentSubtype
```

Values:

- `AMAZON_FSX_FOR_LUSTRE`
- `AMAZON_FSX_FOR_WINDOWS`
- `AWS_MANAGED_MICROSOFT_AD`
- `CUSTOM`

## StudioComponentType

```python
from mypy_boto3_nimble.literals import StudioComponentType
```

Values:

- `ACTIVE_DIRECTORY`
- `COMPUTE_FARM`
- `CUSTOM`
- `LICENSE_SERVICE`
- `SHARED_FILE_SYSTEM`

## StudioEncryptionConfigurationKeyType

```python
from mypy_boto3_nimble.literals import StudioEncryptionConfigurationKeyType
```

Values:

- `AWS_OWNED_KEY`
- `CUSTOMER_MANAGED_KEY`

## StudioPersona

```python
from mypy_boto3_nimble.literals import StudioPersona
```

Values:

- `ADMINISTRATOR`

## StudioState

```python
from mypy_boto3_nimble.literals import StudioState
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETED`
- `READY`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`

## StudioStatusCode

```python
from mypy_boto3_nimble.literals import StudioStatusCode
```

Values:

- `AWS_SSO_ACCESS_DENIED`
- `AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS`
- `AWS_SSO_CONFIGURATION_REPAIRED`
- `AWS_SSO_NOT_ENABLED`
- `ENCRYPTION_KEY_ACCESS_DENIED`
- `ENCRYPTION_KEY_NOT_FOUND`
- `INTERNAL_ERROR`
- `ROLE_COULD_NOT_BE_ASSUMED`
- `ROLE_NOT_OWNED_BY_STUDIO_OWNER`
- `STUDIO_CREATE_IN_PROGRESS`
- `STUDIO_CREATED`
- `STUDIO_DELETE_IN_PROGRESS`
- `STUDIO_DELETED`
- `STUDIO_UPDATE_IN_PROGRESS`
- `STUDIO_UPDATED`
- `STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED`
- `STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED`
- `STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED`
