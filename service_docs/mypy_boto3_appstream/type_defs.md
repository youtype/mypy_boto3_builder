# Structures for boto3 AppStream module

> [Index](../index.md) > [AppStream](./index.md) > Structures

Auto-generated documentation for [AppStream](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream)
type annotations stubs module [mypy_boto3_appstream](https://pypi.org/project/mypy-boto3-appstream/).

- [Structures for boto3 AppStream module](#structures-for-boto3-appstream-module)
  - [AccessEndpointTypeDef](#accessendpointtypedef)
  - [ApplicationSettingsResponseTypeDef](#applicationsettingsresponsetypedef)
  - [ApplicationSettingsTypeDef](#applicationsettingstypedef)
  - [ApplicationTypeDef](#applicationtypedef)
  - [BatchAssociateUserStackResultTypeDef](#batchassociateuserstackresulttypedef)
  - [BatchDisassociateUserStackResultTypeDef](#batchdisassociateuserstackresulttypedef)
  - [ComputeCapacityStatusTypeDef](#computecapacitystatustypedef)
  - [ComputeCapacityTypeDef](#computecapacitytypedef)
  - [CopyImageResponseTypeDef](#copyimageresponsetypedef)
  - [CreateDirectoryConfigResultTypeDef](#createdirectoryconfigresulttypedef)
  - [CreateFleetResultTypeDef](#createfleetresulttypedef)
  - [CreateImageBuilderResultTypeDef](#createimagebuilderresulttypedef)
  - [CreateImageBuilderStreamingURLResultTypeDef](#createimagebuilderstreamingurlresulttypedef)
  - [CreateStackResultTypeDef](#createstackresulttypedef)
  - [CreateStreamingURLResultTypeDef](#createstreamingurlresulttypedef)
  - [CreateUpdatedImageResultTypeDef](#createupdatedimageresulttypedef)
  - [CreateUsageReportSubscriptionResultTypeDef](#createusagereportsubscriptionresulttypedef)
  - [DeleteImageBuilderResultTypeDef](#deleteimagebuilderresulttypedef)
  - [DeleteImageResultTypeDef](#deleteimageresulttypedef)
  - [DescribeDirectoryConfigsResultTypeDef](#describedirectoryconfigsresulttypedef)
  - [DescribeFleetsResultTypeDef](#describefleetsresulttypedef)
  - [DescribeImageBuildersResultTypeDef](#describeimagebuildersresulttypedef)
  - [DescribeImagePermissionsResultTypeDef](#describeimagepermissionsresulttypedef)
  - [DescribeImagesResultTypeDef](#describeimagesresulttypedef)
  - [DescribeSessionsResultTypeDef](#describesessionsresulttypedef)
  - [DescribeStacksResultTypeDef](#describestacksresulttypedef)
  - [DescribeUsageReportSubscriptionsResultTypeDef](#describeusagereportsubscriptionsresulttypedef)
  - [DescribeUserStackAssociationsResultTypeDef](#describeuserstackassociationsresulttypedef)
  - [DescribeUsersResultTypeDef](#describeusersresulttypedef)
  - [DirectoryConfigTypeDef](#directoryconfigtypedef)
  - [DomainJoinInfoTypeDef](#domainjoininfotypedef)
  - [FleetErrorTypeDef](#fleeterrortypedef)
  - [FleetTypeDef](#fleettypedef)
  - [ImageBuilderStateChangeReasonTypeDef](#imagebuilderstatechangereasontypedef)
  - [ImageBuilderTypeDef](#imagebuildertypedef)
  - [ImagePermissionsTypeDef](#imagepermissionstypedef)
  - [ImageStateChangeReasonTypeDef](#imagestatechangereasontypedef)
  - [ImageTypeDef](#imagetypedef)
  - [LastReportGenerationExecutionErrorTypeDef](#lastreportgenerationexecutionerrortypedef)
  - [ListAssociatedFleetsResultTypeDef](#listassociatedfleetsresulttypedef)
  - [ListAssociatedStacksResultTypeDef](#listassociatedstacksresulttypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [NetworkAccessConfigurationTypeDef](#networkaccessconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResourceErrorTypeDef](#resourceerrortypedef)
  - [ServiceAccountCredentialsTypeDef](#serviceaccountcredentialstypedef)
  - [SessionTypeDef](#sessiontypedef)
  - [SharedImagePermissionsTypeDef](#sharedimagepermissionstypedef)
  - [StackErrorTypeDef](#stackerrortypedef)
  - [StackTypeDef](#stacktypedef)
  - [StartImageBuilderResultTypeDef](#startimagebuilderresulttypedef)
  - [StopImageBuilderResultTypeDef](#stopimagebuilderresulttypedef)
  - [StorageConnectorTypeDef](#storageconnectortypedef)
  - [UpdateDirectoryConfigResultTypeDef](#updatedirectoryconfigresulttypedef)
  - [UpdateFleetResultTypeDef](#updatefleetresulttypedef)
  - [UpdateStackResultTypeDef](#updatestackresulttypedef)
  - [UsageReportSubscriptionTypeDef](#usagereportsubscriptiontypedef)
  - [UserSettingTypeDef](#usersettingtypedef)
  - [UserStackAssociationErrorTypeDef](#userstackassociationerrortypedef)
  - [UserStackAssociationTypeDef](#userstackassociationtypedef)
  - [UserTypeDef](#usertypedef)
  - [VpcConfigTypeDef](#vpcconfigtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccessEndpointTypeDef

```python
from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef
```


Required fields:
- `EndpointType`: `Literal['STREAMING']`



Optional fields:
- `VpceId`: `str`


## ApplicationSettingsResponseTypeDef

```python
from mypy_boto3_appstream.type_defs import ApplicationSettingsResponseTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `SettingsGroup`: `str`
- `S3BucketName`: `str`


## ApplicationSettingsTypeDef

```python
from mypy_boto3_appstream.type_defs import ApplicationSettingsTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `SettingsGroup`: `str`


## ApplicationTypeDef

```python
from mypy_boto3_appstream.type_defs import ApplicationTypeDef
```




Optional fields:
- `Name`: `str`
- `DisplayName`: `str`
- `IconURL`: `str`
- `LaunchPath`: `str`
- `LaunchParameters`: `str`
- `Enabled`: `bool`
- `Metadata`: `Dict[str, str]`


## BatchAssociateUserStackResultTypeDef

```python
from mypy_boto3_appstream.type_defs import BatchAssociateUserStackResultTypeDef
```




Optional fields:
- `errors`: `List["UserStackAssociationErrorTypeDef"]`


## BatchDisassociateUserStackResultTypeDef

```python
from mypy_boto3_appstream.type_defs import BatchDisassociateUserStackResultTypeDef
```




Optional fields:
- `errors`: `List["UserStackAssociationErrorTypeDef"]`


## ComputeCapacityStatusTypeDef

```python
from mypy_boto3_appstream.type_defs import ComputeCapacityStatusTypeDef
```


Required fields:
- `Desired`: `int`



Optional fields:
- `Running`: `int`
- `InUse`: `int`
- `Available`: `int`


## ComputeCapacityTypeDef

```python
from mypy_boto3_appstream.type_defs import ComputeCapacityTypeDef
```


Required fields:
- `DesiredInstances`: `int`




## CopyImageResponseTypeDef

```python
from mypy_boto3_appstream.type_defs import CopyImageResponseTypeDef
```




Optional fields:
- `DestinationImageName`: `str`


## CreateDirectoryConfigResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateDirectoryConfigResultTypeDef
```




Optional fields:
- `DirectoryConfig`: `"DirectoryConfigTypeDef"`


## CreateFleetResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateFleetResultTypeDef
```




Optional fields:
- `Fleet`: `"FleetTypeDef"`


## CreateImageBuilderResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateImageBuilderResultTypeDef
```




Optional fields:
- `ImageBuilder`: `"ImageBuilderTypeDef"`


## CreateImageBuilderStreamingURLResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateImageBuilderStreamingURLResultTypeDef
```




Optional fields:
- `StreamingURL`: `str`
- `Expires`: `datetime`


## CreateStackResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateStackResultTypeDef
```




Optional fields:
- `Stack`: `"StackTypeDef"`


## CreateStreamingURLResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateStreamingURLResultTypeDef
```




Optional fields:
- `StreamingURL`: `str`
- `Expires`: `datetime`


## CreateUpdatedImageResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateUpdatedImageResultTypeDef
```




Optional fields:
- `image`: `"ImageTypeDef"`
- `canUpdateImage`: `bool`


## CreateUsageReportSubscriptionResultTypeDef

```python
from mypy_boto3_appstream.type_defs import CreateUsageReportSubscriptionResultTypeDef
```




Optional fields:
- `S3BucketName`: `str`
- `Schedule`: `Literal['DAILY']`


## DeleteImageBuilderResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DeleteImageBuilderResultTypeDef
```




Optional fields:
- `ImageBuilder`: `"ImageBuilderTypeDef"`


## DeleteImageResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DeleteImageResultTypeDef
```




Optional fields:
- `Image`: `"ImageTypeDef"`


## DescribeDirectoryConfigsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeDirectoryConfigsResultTypeDef
```




Optional fields:
- `DirectoryConfigs`: `List["DirectoryConfigTypeDef"]`
- `NextToken`: `str`


## DescribeFleetsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeFleetsResultTypeDef
```




Optional fields:
- `Fleets`: `List["FleetTypeDef"]`
- `NextToken`: `str`


## DescribeImageBuildersResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeImageBuildersResultTypeDef
```




Optional fields:
- `ImageBuilders`: `List["ImageBuilderTypeDef"]`
- `NextToken`: `str`


## DescribeImagePermissionsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeImagePermissionsResultTypeDef
```




Optional fields:
- `Name`: `str`
- `SharedImagePermissionsList`: `List["SharedImagePermissionsTypeDef"]`
- `NextToken`: `str`


## DescribeImagesResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeImagesResultTypeDef
```




Optional fields:
- `Images`: `List["ImageTypeDef"]`
- `NextToken`: `str`


## DescribeSessionsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeSessionsResultTypeDef
```




Optional fields:
- `Sessions`: `List["SessionTypeDef"]`
- `NextToken`: `str`


## DescribeStacksResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeStacksResultTypeDef
```




Optional fields:
- `Stacks`: `List["StackTypeDef"]`
- `NextToken`: `str`


## DescribeUsageReportSubscriptionsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeUsageReportSubscriptionsResultTypeDef
```




Optional fields:
- `UsageReportSubscriptions`: `List["UsageReportSubscriptionTypeDef"]`
- `NextToken`: `str`


## DescribeUserStackAssociationsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeUserStackAssociationsResultTypeDef
```




Optional fields:
- `UserStackAssociations`: `List["UserStackAssociationTypeDef"]`
- `NextToken`: `str`


## DescribeUsersResultTypeDef

```python
from mypy_boto3_appstream.type_defs import DescribeUsersResultTypeDef
```




Optional fields:
- `Users`: `List["UserTypeDef"]`
- `NextToken`: `str`


## DirectoryConfigTypeDef

```python
from mypy_boto3_appstream.type_defs import DirectoryConfigTypeDef
```


Required fields:
- `DirectoryName`: `str`



Optional fields:
- `OrganizationalUnitDistinguishedNames`: `List[str]`
- `ServiceAccountCredentials`: `"ServiceAccountCredentialsTypeDef"`
- `CreatedTime`: `datetime`


## DomainJoinInfoTypeDef

```python
from mypy_boto3_appstream.type_defs import DomainJoinInfoTypeDef
```




Optional fields:
- `DirectoryName`: `str`
- `OrganizationalUnitDistinguishedName`: `str`


## FleetErrorTypeDef

```python
from mypy_boto3_appstream.type_defs import FleetErrorTypeDef
```




Optional fields:
- `ErrorCode`: `FleetErrorCode`
- `ErrorMessage`: `str`


## FleetTypeDef

```python
from mypy_boto3_appstream.type_defs import FleetTypeDef
```


Required fields:
- `Arn`: `str`
- `Name`: `str`
- `InstanceType`: `str`
- `ComputeCapacityStatus`: `"ComputeCapacityStatusTypeDef"`
- `State`: `FleetState`



Optional fields:
- `DisplayName`: `str`
- `Description`: `str`
- `ImageName`: `str`
- `ImageArn`: `str`
- `FleetType`: `FleetType`
- `MaxUserDurationInSeconds`: `int`
- `DisconnectTimeoutInSeconds`: `int`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `CreatedTime`: `datetime`
- `FleetErrors`: `List["FleetErrorTypeDef"]`
- `EnableDefaultInternetAccess`: `bool`
- `DomainJoinInfo`: `"DomainJoinInfoTypeDef"`
- `IdleDisconnectTimeoutInSeconds`: `int`
- `IamRoleArn`: `str`
- `StreamView`: `StreamView`


## ImageBuilderStateChangeReasonTypeDef

```python
from mypy_boto3_appstream.type_defs import ImageBuilderStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `ImageBuilderStateChangeReasonCode`
- `Message`: `str`


## ImageBuilderTypeDef

```python
from mypy_boto3_appstream.type_defs import ImageBuilderTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Arn`: `str`
- `ImageArn`: `str`
- `Description`: `str`
- `DisplayName`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `InstanceType`: `str`
- `Platform`: `PlatformType`
- `IamRoleArn`: `str`
- `State`: `ImageBuilderState`
- `StateChangeReason`: `"ImageBuilderStateChangeReasonTypeDef"`
- `CreatedTime`: `datetime`
- `EnableDefaultInternetAccess`: `bool`
- `DomainJoinInfo`: `"DomainJoinInfoTypeDef"`
- `NetworkAccessConfiguration`: `"NetworkAccessConfigurationTypeDef"`
- `ImageBuilderErrors`: `List["ResourceErrorTypeDef"]`
- `AppstreamAgentVersion`: `str`
- `AccessEndpoints`: `List["AccessEndpointTypeDef"]`


## ImagePermissionsTypeDef

```python
from mypy_boto3_appstream.type_defs import ImagePermissionsTypeDef
```




Optional fields:
- `allowFleet`: `bool`
- `allowImageBuilder`: `bool`


## ImageStateChangeReasonTypeDef

```python
from mypy_boto3_appstream.type_defs import ImageStateChangeReasonTypeDef
```




Optional fields:
- `Code`: `ImageStateChangeReasonCode`
- `Message`: `str`


## ImageTypeDef

```python
from mypy_boto3_appstream.type_defs import ImageTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Arn`: `str`
- `BaseImageArn`: `str`
- `DisplayName`: `str`
- `State`: `ImageState`
- `Visibility`: `VisibilityType`
- `ImageBuilderSupported`: `bool`
- `ImageBuilderName`: `str`
- `Platform`: `PlatformType`
- `Description`: `str`
- `StateChangeReason`: `"ImageStateChangeReasonTypeDef"`
- `Applications`: `List["ApplicationTypeDef"]`
- `CreatedTime`: `datetime`
- `PublicBaseImageReleasedDate`: `datetime`
- `AppstreamAgentVersion`: `str`
- `ImagePermissions`: `"ImagePermissionsTypeDef"`
- `ImageErrors`: `List["ResourceErrorTypeDef"]`


## LastReportGenerationExecutionErrorTypeDef

```python
from mypy_boto3_appstream.type_defs import LastReportGenerationExecutionErrorTypeDef
```




Optional fields:
- `ErrorCode`: `UsageReportExecutionErrorCode`
- `ErrorMessage`: `str`


## ListAssociatedFleetsResultTypeDef

```python
from mypy_boto3_appstream.type_defs import ListAssociatedFleetsResultTypeDef
```




Optional fields:
- `Names`: `List[str]`
- `NextToken`: `str`


## ListAssociatedStacksResultTypeDef

```python
from mypy_boto3_appstream.type_defs import ListAssociatedStacksResultTypeDef
```




Optional fields:
- `Names`: `List[str]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_appstream.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## NetworkAccessConfigurationTypeDef

```python
from mypy_boto3_appstream.type_defs import NetworkAccessConfigurationTypeDef
```




Optional fields:
- `EniPrivateIpAddress`: `str`
- `EniId`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_appstream.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResourceErrorTypeDef

```python
from mypy_boto3_appstream.type_defs import ResourceErrorTypeDef
```




Optional fields:
- `ErrorCode`: `FleetErrorCode`
- `ErrorMessage`: `str`
- `ErrorTimestamp`: `datetime`


## ServiceAccountCredentialsTypeDef

```python
from mypy_boto3_appstream.type_defs import ServiceAccountCredentialsTypeDef
```


Required fields:
- `AccountName`: `str`
- `AccountPassword`: `str`




## SessionTypeDef

```python
from mypy_boto3_appstream.type_defs import SessionTypeDef
```


Required fields:
- `Id`: `str`
- `UserId`: `str`
- `StackName`: `str`
- `FleetName`: `str`
- `State`: `SessionState`



Optional fields:
- `ConnectionState`: `SessionConnectionState`
- `StartTime`: `datetime`
- `MaxExpirationTime`: `datetime`
- `AuthenticationType`: `AuthenticationType`
- `NetworkAccessConfiguration`: `"NetworkAccessConfigurationTypeDef"`


## SharedImagePermissionsTypeDef

```python
from mypy_boto3_appstream.type_defs import SharedImagePermissionsTypeDef
```


Required fields:
- `sharedAccountId`: `str`
- `imagePermissions`: `"ImagePermissionsTypeDef"`




## StackErrorTypeDef

```python
from mypy_boto3_appstream.type_defs import StackErrorTypeDef
```




Optional fields:
- `ErrorCode`: `StackErrorCode`
- `ErrorMessage`: `str`


## StackTypeDef

```python
from mypy_boto3_appstream.type_defs import StackTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Arn`: `str`
- `Description`: `str`
- `DisplayName`: `str`
- `CreatedTime`: `datetime`
- `StorageConnectors`: `List["StorageConnectorTypeDef"]`
- `RedirectURL`: `str`
- `FeedbackURL`: `str`
- `StackErrors`: `List["StackErrorTypeDef"]`
- `UserSettings`: `List["UserSettingTypeDef"]`
- `ApplicationSettings`: `"ApplicationSettingsResponseTypeDef"`
- `AccessEndpoints`: `List["AccessEndpointTypeDef"]`
- `EmbedHostDomains`: `List[str]`


## StartImageBuilderResultTypeDef

```python
from mypy_boto3_appstream.type_defs import StartImageBuilderResultTypeDef
```




Optional fields:
- `ImageBuilder`: `"ImageBuilderTypeDef"`


## StopImageBuilderResultTypeDef

```python
from mypy_boto3_appstream.type_defs import StopImageBuilderResultTypeDef
```




Optional fields:
- `ImageBuilder`: `"ImageBuilderTypeDef"`


## StorageConnectorTypeDef

```python
from mypy_boto3_appstream.type_defs import StorageConnectorTypeDef
```


Required fields:
- `ConnectorType`: `StorageConnectorType`



Optional fields:
- `ResourceIdentifier`: `str`
- `Domains`: `List[str]`


## UpdateDirectoryConfigResultTypeDef

```python
from mypy_boto3_appstream.type_defs import UpdateDirectoryConfigResultTypeDef
```




Optional fields:
- `DirectoryConfig`: `"DirectoryConfigTypeDef"`


## UpdateFleetResultTypeDef

```python
from mypy_boto3_appstream.type_defs import UpdateFleetResultTypeDef
```




Optional fields:
- `Fleet`: `"FleetTypeDef"`


## UpdateStackResultTypeDef

```python
from mypy_boto3_appstream.type_defs import UpdateStackResultTypeDef
```




Optional fields:
- `Stack`: `"StackTypeDef"`


## UsageReportSubscriptionTypeDef

```python
from mypy_boto3_appstream.type_defs import UsageReportSubscriptionTypeDef
```




Optional fields:
- `S3BucketName`: `str`
- `Schedule`: `Literal['DAILY']`
- `LastGeneratedReportDate`: `datetime`
- `SubscriptionErrors`: `List["LastReportGenerationExecutionErrorTypeDef"]`


## UserSettingTypeDef

```python
from mypy_boto3_appstream.type_defs import UserSettingTypeDef
```


Required fields:
- `Action`: `Action`
- `Permission`: `Permission`




## UserStackAssociationErrorTypeDef

```python
from mypy_boto3_appstream.type_defs import UserStackAssociationErrorTypeDef
```




Optional fields:
- `UserStackAssociation`: `"UserStackAssociationTypeDef"`
- `ErrorCode`: `UserStackAssociationErrorCode`
- `ErrorMessage`: `str`


## UserStackAssociationTypeDef

```python
from mypy_boto3_appstream.type_defs import UserStackAssociationTypeDef
```


Required fields:
- `StackName`: `str`
- `UserName`: `str`
- `AuthenticationType`: `AuthenticationType`



Optional fields:
- `SendEmailNotification`: `bool`


## UserTypeDef

```python
from mypy_boto3_appstream.type_defs import UserTypeDef
```


Required fields:
- `AuthenticationType`: `AuthenticationType`



Optional fields:
- `Arn`: `str`
- `UserName`: `str`
- `Enabled`: `bool`
- `Status`: `str`
- `FirstName`: `str`
- `LastName`: `str`
- `CreatedTime`: `datetime`


## VpcConfigTypeDef

```python
from mypy_boto3_appstream.type_defs import VpcConfigTypeDef
```




Optional fields:
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`


## WaiterConfigTypeDef

```python
from mypy_boto3_appstream.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

