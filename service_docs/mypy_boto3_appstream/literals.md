# Literals for boto3 AppStream module

> [Index](../index.md) > [AppStream](./index.md) > Literals

Auto-generated documentation for [AppStream](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream)
type annotations stubs module [mypy_boto3_appstream](https://pypi.org/project/mypy-boto3-appstream/).

- [Literals for boto3 AppStream module](#literals-for-boto3-appstream-module)
  - [AccessEndpointType](#accessendpointtype)
  - [Action](#action)
  - [AuthenticationType](#authenticationtype)
  - [DescribeDirectoryConfigsPaginatorName](#describedirectoryconfigspaginatorname)
  - [DescribeFleetsPaginatorName](#describefleetspaginatorname)
  - [DescribeImageBuildersPaginatorName](#describeimagebuilderspaginatorname)
  - [DescribeImagesPaginatorName](#describeimagespaginatorname)
  - [DescribeSessionsPaginatorName](#describesessionspaginatorname)
  - [DescribeStacksPaginatorName](#describestackspaginatorname)
  - [DescribeUserStackAssociationsPaginatorName](#describeuserstackassociationspaginatorname)
  - [DescribeUsersPaginatorName](#describeuserspaginatorname)
  - [FleetAttribute](#fleetattribute)
  - [FleetErrorCode](#fleeterrorcode)
  - [FleetStartedWaiterName](#fleetstartedwaitername)
  - [FleetState](#fleetstate)
  - [FleetStoppedWaiterName](#fleetstoppedwaitername)
  - [FleetType](#fleettype)
  - [ImageBuilderState](#imagebuilderstate)
  - [ImageBuilderStateChangeReasonCode](#imagebuilderstatechangereasoncode)
  - [ImageState](#imagestate)
  - [ImageStateChangeReasonCode](#imagestatechangereasoncode)
  - [ListAssociatedFleetsPaginatorName](#listassociatedfleetspaginatorname)
  - [ListAssociatedStacksPaginatorName](#listassociatedstackspaginatorname)
  - [MessageAction](#messageaction)
  - [Permission](#permission)
  - [PlatformType](#platformtype)
  - [SessionConnectionState](#sessionconnectionstate)
  - [SessionState](#sessionstate)
  - [StackAttribute](#stackattribute)
  - [StackErrorCode](#stackerrorcode)
  - [StorageConnectorType](#storageconnectortype)
  - [StreamView](#streamview)
  - [UsageReportExecutionErrorCode](#usagereportexecutionerrorcode)
  - [UsageReportSchedule](#usagereportschedule)
  - [UserStackAssociationErrorCode](#userstackassociationerrorcode)
  - [VisibilityType](#visibilitytype)

## AccessEndpointType

```python
from mypy_boto3_appstream.literals import AccessEndpointType
```

Values:

- `STREAMING`

## Action

```python
from mypy_boto3_appstream.literals import Action
```

Values:

- `CLIPBOARD_COPY_FROM_LOCAL_DEVICE`
- `CLIPBOARD_COPY_TO_LOCAL_DEVICE`
- `DOMAIN_PASSWORD_SIGNIN`
- `DOMAIN_SMART_CARD_SIGNIN`
- `FILE_DOWNLOAD`
- `FILE_UPLOAD`
- `PRINTING_TO_LOCAL_DEVICE`

## AuthenticationType

```python
from mypy_boto3_appstream.literals import AuthenticationType
```

Values:

- `API`
- `SAML`
- `USERPOOL`

## DescribeDirectoryConfigsPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeDirectoryConfigsPaginatorName
```

Values:

- `describe_directory_configs`

## DescribeFleetsPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeFleetsPaginatorName
```

Values:

- `describe_fleets`

## DescribeImageBuildersPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeImageBuildersPaginatorName
```

Values:

- `describe_image_builders`

## DescribeImagesPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeImagesPaginatorName
```

Values:

- `describe_images`

## DescribeSessionsPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeSessionsPaginatorName
```

Values:

- `describe_sessions`

## DescribeStacksPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeStacksPaginatorName
```

Values:

- `describe_stacks`

## DescribeUserStackAssociationsPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeUserStackAssociationsPaginatorName
```

Values:

- `describe_user_stack_associations`

## DescribeUsersPaginatorName

```python
from mypy_boto3_appstream.literals import DescribeUsersPaginatorName
```

Values:

- `describe_users`

## FleetAttribute

```python
from mypy_boto3_appstream.literals import FleetAttribute
```

Values:

- `DOMAIN_JOIN_INFO`
- `IAM_ROLE_ARN`
- `VPC_CONFIGURATION`
- `VPC_CONFIGURATION_SECURITY_GROUP_IDS`

## FleetErrorCode

```python
from mypy_boto3_appstream.literals import FleetErrorCode
```

Values:

- `DOMAIN_JOIN_ERROR_ACCESS_DENIED`
- `DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED`
- `DOMAIN_JOIN_ERROR_FILE_NOT_FOUND`
- `DOMAIN_JOIN_ERROR_INVALID_PARAMETER`
- `DOMAIN_JOIN_ERROR_LOGON_FAILURE`
- `DOMAIN_JOIN_ERROR_MORE_DATA`
- `DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN`
- `DOMAIN_JOIN_ERROR_NOT_SUPPORTED`
- `DOMAIN_JOIN_INTERNAL_SERVICE_ERROR`
- `DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME`
- `DOMAIN_JOIN_NERR_PASSWORD_EXPIRED`
- `DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED`
- `FLEET_INSTANCE_PROVISIONING_FAILURE`
- `FLEET_STOPPED`
- `IAM_SERVICE_ROLE_IS_MISSING`
- `IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION`
- `IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION`
- `IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION`
- `IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION`
- `IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION`
- `IGW_NOT_ATTACHED`
- `IMAGE_NOT_FOUND`
- `INTERNAL_SERVICE_ERROR`
- `INVALID_SUBNET_CONFIGURATION`
- `MACHINE_ROLE_IS_MISSING`
- `NETWORK_INTERFACE_LIMIT_EXCEEDED`
- `SECURITY_GROUPS_NOT_FOUND`
- `STS_DISABLED_IN_REGION`
- `SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES`
- `SUBNET_NOT_FOUND`

## FleetStartedWaiterName

```python
from mypy_boto3_appstream.literals import FleetStartedWaiterName
```

Values:

- `fleet_started`

## FleetState

```python
from mypy_boto3_appstream.literals import FleetState
```

Values:

- `RUNNING`
- `STARTING`
- `STOPPED`
- `STOPPING`

## FleetStoppedWaiterName

```python
from mypy_boto3_appstream.literals import FleetStoppedWaiterName
```

Values:

- `fleet_stopped`

## FleetType

```python
from mypy_boto3_appstream.literals import FleetType
```

Values:

- `ALWAYS_ON`
- `ON_DEMAND`

## ImageBuilderState

```python
from mypy_boto3_appstream.literals import ImageBuilderState
```

Values:

- `DELETING`
- `FAILED`
- `PENDING`
- `PENDING_QUALIFICATION`
- `REBOOTING`
- `RUNNING`
- `SNAPSHOTTING`
- `STOPPED`
- `STOPPING`
- `UPDATING`
- `UPDATING_AGENT`

## ImageBuilderStateChangeReasonCode

```python
from mypy_boto3_appstream.literals import ImageBuilderStateChangeReasonCode
```

Values:

- `IMAGE_UNAVAILABLE`
- `INTERNAL_ERROR`

## ImageState

```python
from mypy_boto3_appstream.literals import ImageState
```

Values:

- `AVAILABLE`
- `COPYING`
- `CREATING`
- `DELETING`
- `FAILED`
- `IMPORTING`
- `PENDING`

## ImageStateChangeReasonCode

```python
from mypy_boto3_appstream.literals import ImageStateChangeReasonCode
```

Values:

- `IMAGE_BUILDER_NOT_AVAILABLE`
- `IMAGE_COPY_FAILURE`
- `INTERNAL_ERROR`

## ListAssociatedFleetsPaginatorName

```python
from mypy_boto3_appstream.literals import ListAssociatedFleetsPaginatorName
```

Values:

- `list_associated_fleets`

## ListAssociatedStacksPaginatorName

```python
from mypy_boto3_appstream.literals import ListAssociatedStacksPaginatorName
```

Values:

- `list_associated_stacks`

## MessageAction

```python
from mypy_boto3_appstream.literals import MessageAction
```

Values:

- `RESEND`
- `SUPPRESS`

## Permission

```python
from mypy_boto3_appstream.literals import Permission
```

Values:

- `DISABLED`
- `ENABLED`

## PlatformType

```python
from mypy_boto3_appstream.literals import PlatformType
```

Values:

- `WINDOWS`
- `WINDOWS_SERVER_2016`
- `WINDOWS_SERVER_2019`

## SessionConnectionState

```python
from mypy_boto3_appstream.literals import SessionConnectionState
```

Values:

- `CONNECTED`
- `NOT_CONNECTED`

## SessionState

```python
from mypy_boto3_appstream.literals import SessionState
```

Values:

- `ACTIVE`
- `EXPIRED`
- `PENDING`

## StackAttribute

```python
from mypy_boto3_appstream.literals import StackAttribute
```

Values:

- `ACCESS_ENDPOINTS`
- `EMBED_HOST_DOMAINS`
- `FEEDBACK_URL`
- `IAM_ROLE_ARN`
- `REDIRECT_URL`
- `STORAGE_CONNECTOR_GOOGLE_DRIVE`
- `STORAGE_CONNECTOR_HOMEFOLDERS`
- `STORAGE_CONNECTOR_ONE_DRIVE`
- `STORAGE_CONNECTORS`
- `THEME_NAME`
- `USER_SETTINGS`

## StackErrorCode

```python
from mypy_boto3_appstream.literals import StackErrorCode
```

Values:

- `INTERNAL_SERVICE_ERROR`
- `STORAGE_CONNECTOR_ERROR`

## StorageConnectorType

```python
from mypy_boto3_appstream.literals import StorageConnectorType
```

Values:

- `GOOGLE_DRIVE`
- `HOMEFOLDERS`
- `ONE_DRIVE`

## StreamView

```python
from mypy_boto3_appstream.literals import StreamView
```

Values:

- `APP`
- `DESKTOP`

## UsageReportExecutionErrorCode

```python
from mypy_boto3_appstream.literals import UsageReportExecutionErrorCode
```

Values:

- `ACCESS_DENIED`
- `INTERNAL_SERVICE_ERROR`
- `RESOURCE_NOT_FOUND`

## UsageReportSchedule

```python
from mypy_boto3_appstream.literals import UsageReportSchedule
```

Values:

- `DAILY`

## UserStackAssociationErrorCode

```python
from mypy_boto3_appstream.literals import UserStackAssociationErrorCode
```

Values:

- `DIRECTORY_NOT_FOUND`
- `INTERNAL_ERROR`
- `STACK_NOT_FOUND`
- `USER_NAME_NOT_FOUND`

## VisibilityType

```python
from mypy_boto3_appstream.literals import VisibilityType
```

Values:

- `PRIVATE`
- `PUBLIC`
- `SHARED`
