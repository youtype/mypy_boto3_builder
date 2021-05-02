# Structures for boto3 Connect module

> [Index](../index.md) > [Connect](./index.md) > Structures

Auto-generated documentation for [Connect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect)
type annotations stubs module [mypy_boto3_connect](https://pypi.org/project/mypy-boto3-connect/).

- [Structures for boto3 Connect module](#structures-for-boto3-connect-module)
  - [AssociateInstanceStorageConfigResponseTypeDef](#associateinstancestorageconfigresponsetypedef)
  - [AssociateSecurityKeyResponseTypeDef](#associatesecuritykeyresponsetypedef)
  - [AttributeTypeDef](#attributetypedef)
  - [ChatMessageTypeDef](#chatmessagetypedef)
  - [ContactFlowSummaryTypeDef](#contactflowsummarytypedef)
  - [ContactFlowTypeDef](#contactflowtypedef)
  - [CreateContactFlowResponseTypeDef](#createcontactflowresponsetypedef)
  - [CreateInstanceResponseTypeDef](#createinstanceresponsetypedef)
  - [CreateIntegrationAssociationResponseTypeDef](#createintegrationassociationresponsetypedef)
  - [CreateQueueResponseTypeDef](#createqueueresponsetypedef)
  - [CreateQuickConnectResponseTypeDef](#createquickconnectresponsetypedef)
  - [CreateRoutingProfileResponseTypeDef](#createroutingprofileresponsetypedef)
  - [CreateUseCaseResponseTypeDef](#createusecaseresponsetypedef)
  - [CreateUserHierarchyGroupResponseTypeDef](#createuserhierarchygroupresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [CredentialsTypeDef](#credentialstypedef)
  - [CurrentMetricDataTypeDef](#currentmetricdatatypedef)
  - [CurrentMetricResultTypeDef](#currentmetricresulttypedef)
  - [CurrentMetricTypeDef](#currentmetrictypedef)
  - [DescribeContactFlowResponseTypeDef](#describecontactflowresponsetypedef)
  - [DescribeHoursOfOperationResponseTypeDef](#describehoursofoperationresponsetypedef)
  - [DescribeInstanceAttributeResponseTypeDef](#describeinstanceattributeresponsetypedef)
  - [DescribeInstanceResponseTypeDef](#describeinstanceresponsetypedef)
  - [DescribeInstanceStorageConfigResponseTypeDef](#describeinstancestorageconfigresponsetypedef)
  - [DescribeQueueResponseTypeDef](#describequeueresponsetypedef)
  - [DescribeQuickConnectResponseTypeDef](#describequickconnectresponsetypedef)
  - [DescribeRoutingProfileResponseTypeDef](#describeroutingprofileresponsetypedef)
  - [DescribeUserHierarchyGroupResponseTypeDef](#describeuserhierarchygroupresponsetypedef)
  - [DescribeUserHierarchyStructureResponseTypeDef](#describeuserhierarchystructureresponsetypedef)
  - [DescribeUserResponseTypeDef](#describeuserresponsetypedef)
  - [DimensionsTypeDef](#dimensionstypedef)
  - [EncryptionConfigTypeDef](#encryptionconfigtypedef)
  - [FiltersTypeDef](#filterstypedef)
  - [GetContactAttributesResponseTypeDef](#getcontactattributesresponsetypedef)
  - [GetCurrentMetricDataResponseTypeDef](#getcurrentmetricdataresponsetypedef)
  - [GetFederationTokenResponseTypeDef](#getfederationtokenresponsetypedef)
  - [GetMetricDataResponseTypeDef](#getmetricdataresponsetypedef)
  - [HierarchyGroupSummaryTypeDef](#hierarchygroupsummarytypedef)
  - [HierarchyGroupTypeDef](#hierarchygrouptypedef)
  - [HierarchyLevelTypeDef](#hierarchyleveltypedef)
  - [HierarchyLevelUpdateTypeDef](#hierarchylevelupdatetypedef)
  - [HierarchyPathTypeDef](#hierarchypathtypedef)
  - [HierarchyStructureTypeDef](#hierarchystructuretypedef)
  - [HierarchyStructureUpdateTypeDef](#hierarchystructureupdatetypedef)
  - [HistoricalMetricDataTypeDef](#historicalmetricdatatypedef)
  - [HistoricalMetricResultTypeDef](#historicalmetricresulttypedef)
  - [HistoricalMetricTypeDef](#historicalmetrictypedef)
  - [HoursOfOperationConfigTypeDef](#hoursofoperationconfigtypedef)
  - [HoursOfOperationSummaryTypeDef](#hoursofoperationsummarytypedef)
  - [HoursOfOperationTimeSliceTypeDef](#hoursofoperationtimeslicetypedef)
  - [HoursOfOperationTypeDef](#hoursofoperationtypedef)
  - [InstanceStatusReasonTypeDef](#instancestatusreasontypedef)
  - [InstanceStorageConfigTypeDef](#instancestorageconfigtypedef)
  - [InstanceSummaryTypeDef](#instancesummarytypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [IntegrationAssociationSummaryTypeDef](#integrationassociationsummarytypedef)
  - [KinesisFirehoseConfigTypeDef](#kinesisfirehoseconfigtypedef)
  - [KinesisStreamConfigTypeDef](#kinesisstreamconfigtypedef)
  - [KinesisVideoStreamConfigTypeDef](#kinesisvideostreamconfigtypedef)
  - [LexBotTypeDef](#lexbottypedef)
  - [ListApprovedOriginsResponseTypeDef](#listapprovedoriginsresponsetypedef)
  - [ListContactFlowsResponseTypeDef](#listcontactflowsresponsetypedef)
  - [ListHoursOfOperationsResponseTypeDef](#listhoursofoperationsresponsetypedef)
  - [ListInstanceAttributesResponseTypeDef](#listinstanceattributesresponsetypedef)
  - [ListInstanceStorageConfigsResponseTypeDef](#listinstancestorageconfigsresponsetypedef)
  - [ListInstancesResponseTypeDef](#listinstancesresponsetypedef)
  - [ListIntegrationAssociationsResponseTypeDef](#listintegrationassociationsresponsetypedef)
  - [ListLambdaFunctionsResponseTypeDef](#listlambdafunctionsresponsetypedef)
  - [ListLexBotsResponseTypeDef](#listlexbotsresponsetypedef)
  - [ListPhoneNumbersResponseTypeDef](#listphonenumbersresponsetypedef)
  - [ListPromptsResponseTypeDef](#listpromptsresponsetypedef)
  - [ListQueueQuickConnectsResponseTypeDef](#listqueuequickconnectsresponsetypedef)
  - [ListQueuesResponseTypeDef](#listqueuesresponsetypedef)
  - [ListQuickConnectsResponseTypeDef](#listquickconnectsresponsetypedef)
  - [ListRoutingProfileQueuesResponseTypeDef](#listroutingprofilequeuesresponsetypedef)
  - [ListRoutingProfilesResponseTypeDef](#listroutingprofilesresponsetypedef)
  - [ListSecurityKeysResponseTypeDef](#listsecuritykeysresponsetypedef)
  - [ListSecurityProfilesResponseTypeDef](#listsecurityprofilesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListUseCasesResponseTypeDef](#listusecasesresponsetypedef)
  - [ListUserHierarchyGroupsResponseTypeDef](#listuserhierarchygroupsresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [MediaConcurrencyTypeDef](#mediaconcurrencytypedef)
  - [OutboundCallerConfigTypeDef](#outboundcallerconfigtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParticipantDetailsTypeDef](#participantdetailstypedef)
  - [PhoneNumberQuickConnectConfigTypeDef](#phonenumberquickconnectconfigtypedef)
  - [PhoneNumberSummaryTypeDef](#phonenumbersummarytypedef)
  - [PromptSummaryTypeDef](#promptsummarytypedef)
  - [QueueQuickConnectConfigTypeDef](#queuequickconnectconfigtypedef)
  - [QueueReferenceTypeDef](#queuereferencetypedef)
  - [QueueSummaryTypeDef](#queuesummarytypedef)
  - [QueueTypeDef](#queuetypedef)
  - [QuickConnectConfigTypeDef](#quickconnectconfigtypedef)
  - [QuickConnectSummaryTypeDef](#quickconnectsummarytypedef)
  - [QuickConnectTypeDef](#quickconnecttypedef)
  - [ReferenceTypeDef](#referencetypedef)
  - [RoutingProfileQueueConfigSummaryTypeDef](#routingprofilequeueconfigsummarytypedef)
  - [RoutingProfileQueueConfigTypeDef](#routingprofilequeueconfigtypedef)
  - [RoutingProfileQueueReferenceTypeDef](#routingprofilequeuereferencetypedef)
  - [RoutingProfileSummaryTypeDef](#routingprofilesummarytypedef)
  - [RoutingProfileTypeDef](#routingprofiletypedef)
  - [S3ConfigTypeDef](#s3configtypedef)
  - [SecurityKeyTypeDef](#securitykeytypedef)
  - [SecurityProfileSummaryTypeDef](#securityprofilesummarytypedef)
  - [StartChatContactResponseTypeDef](#startchatcontactresponsetypedef)
  - [StartOutboundVoiceContactResponseTypeDef](#startoutboundvoicecontactresponsetypedef)
  - [StartTaskContactResponseTypeDef](#starttaskcontactresponsetypedef)
  - [ThresholdTypeDef](#thresholdtypedef)
  - [UseCaseTypeDef](#usecasetypedef)
  - [UserIdentityInfoTypeDef](#useridentityinfotypedef)
  - [UserPhoneConfigTypeDef](#userphoneconfigtypedef)
  - [UserQuickConnectConfigTypeDef](#userquickconnectconfigtypedef)
  - [UserSummaryTypeDef](#usersummarytypedef)
  - [UserTypeDef](#usertypedef)
  - [VoiceRecordingConfigurationTypeDef](#voicerecordingconfigurationtypedef)

## AssociateInstanceStorageConfigResponseTypeDef

```python
from mypy_boto3_connect.type_defs import AssociateInstanceStorageConfigResponseTypeDef
```




Optional fields:
- `AssociationId`: `str`


## AssociateSecurityKeyResponseTypeDef

```python
from mypy_boto3_connect.type_defs import AssociateSecurityKeyResponseTypeDef
```




Optional fields:
- `AssociationId`: `str`


## AttributeTypeDef

```python
from mypy_boto3_connect.type_defs import AttributeTypeDef
```




Optional fields:
- `AttributeType`: `InstanceAttributeType`
- `Value`: `str`


## ChatMessageTypeDef

```python
from mypy_boto3_connect.type_defs import ChatMessageTypeDef
```


Required fields:
- `ContentType`: `str`
- `Content`: `str`




## ContactFlowSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import ContactFlowSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `ContactFlowType`: `ContactFlowType`


## ContactFlowTypeDef

```python
from mypy_boto3_connect.type_defs import ContactFlowTypeDef
```




Optional fields:
- `Arn`: `str`
- `Id`: `str`
- `Name`: `str`
- `Type`: `ContactFlowType`
- `Description`: `str`
- `Content`: `str`
- `Tags`: `Dict[str, str]`


## CreateContactFlowResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateContactFlowResponseTypeDef
```




Optional fields:
- `ContactFlowId`: `str`
- `ContactFlowArn`: `str`


## CreateInstanceResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateInstanceResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`


## CreateIntegrationAssociationResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateIntegrationAssociationResponseTypeDef
```




Optional fields:
- `IntegrationAssociationId`: `str`
- `IntegrationAssociationArn`: `str`


## CreateQueueResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateQueueResponseTypeDef
```




Optional fields:
- `QueueArn`: `str`
- `QueueId`: `str`


## CreateQuickConnectResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateQuickConnectResponseTypeDef
```




Optional fields:
- `QuickConnectARN`: `str`
- `QuickConnectId`: `str`


## CreateRoutingProfileResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateRoutingProfileResponseTypeDef
```




Optional fields:
- `RoutingProfileArn`: `str`
- `RoutingProfileId`: `str`


## CreateUseCaseResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateUseCaseResponseTypeDef
```




Optional fields:
- `UseCaseId`: `str`
- `UseCaseArn`: `str`


## CreateUserHierarchyGroupResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateUserHierarchyGroupResponseTypeDef
```




Optional fields:
- `HierarchyGroupId`: `str`
- `HierarchyGroupArn`: `str`


## CreateUserResponseTypeDef

```python
from mypy_boto3_connect.type_defs import CreateUserResponseTypeDef
```




Optional fields:
- `UserId`: `str`
- `UserArn`: `str`


## CredentialsTypeDef

```python
from mypy_boto3_connect.type_defs import CredentialsTypeDef
```




Optional fields:
- `AccessToken`: `str`
- `AccessTokenExpiration`: `datetime`
- `RefreshToken`: `str`
- `RefreshTokenExpiration`: `datetime`


## CurrentMetricDataTypeDef

```python
from mypy_boto3_connect.type_defs import CurrentMetricDataTypeDef
```




Optional fields:
- `Metric`: `"CurrentMetricTypeDef"`
- `Value`: `float`


## CurrentMetricResultTypeDef

```python
from mypy_boto3_connect.type_defs import CurrentMetricResultTypeDef
```




Optional fields:
- `Dimensions`: `"DimensionsTypeDef"`
- `Collections`: `List["CurrentMetricDataTypeDef"]`


## CurrentMetricTypeDef

```python
from mypy_boto3_connect.type_defs import CurrentMetricTypeDef
```




Optional fields:
- `Name`: `CurrentMetricName`
- `Unit`: `Unit`


## DescribeContactFlowResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeContactFlowResponseTypeDef
```




Optional fields:
- `ContactFlow`: `"ContactFlowTypeDef"`


## DescribeHoursOfOperationResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeHoursOfOperationResponseTypeDef
```




Optional fields:
- `HoursOfOperation`: `"HoursOfOperationTypeDef"`


## DescribeInstanceAttributeResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeInstanceAttributeResponseTypeDef
```




Optional fields:
- `Attribute`: `"AttributeTypeDef"`


## DescribeInstanceResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeInstanceResponseTypeDef
```




Optional fields:
- `Instance`: `"InstanceTypeDef"`


## DescribeInstanceStorageConfigResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeInstanceStorageConfigResponseTypeDef
```




Optional fields:
- `StorageConfig`: `"InstanceStorageConfigTypeDef"`


## DescribeQueueResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeQueueResponseTypeDef
```




Optional fields:
- `Queue`: `"QueueTypeDef"`


## DescribeQuickConnectResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeQuickConnectResponseTypeDef
```




Optional fields:
- `QuickConnect`: `"QuickConnectTypeDef"`


## DescribeRoutingProfileResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeRoutingProfileResponseTypeDef
```




Optional fields:
- `RoutingProfile`: `"RoutingProfileTypeDef"`


## DescribeUserHierarchyGroupResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeUserHierarchyGroupResponseTypeDef
```




Optional fields:
- `HierarchyGroup`: `"HierarchyGroupTypeDef"`


## DescribeUserHierarchyStructureResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeUserHierarchyStructureResponseTypeDef
```




Optional fields:
- `HierarchyStructure`: `"HierarchyStructureTypeDef"`


## DescribeUserResponseTypeDef

```python
from mypy_boto3_connect.type_defs import DescribeUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## DimensionsTypeDef

```python
from mypy_boto3_connect.type_defs import DimensionsTypeDef
```




Optional fields:
- `Queue`: `"QueueReferenceTypeDef"`
- `Channel`: `Channel`


## EncryptionConfigTypeDef

```python
from mypy_boto3_connect.type_defs import EncryptionConfigTypeDef
```


Required fields:
- `EncryptionType`: `Literal['KMS']`
- `KeyId`: `str`




## FiltersTypeDef

```python
from mypy_boto3_connect.type_defs import FiltersTypeDef
```




Optional fields:
- `Queues`: `List[str]`
- `Channels`: `List[Channel]`


## GetContactAttributesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import GetContactAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`


## GetCurrentMetricDataResponseTypeDef

```python
from mypy_boto3_connect.type_defs import GetCurrentMetricDataResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MetricResults`: `List["CurrentMetricResultTypeDef"]`
- `DataSnapshotTime`: `datetime`


## GetFederationTokenResponseTypeDef

```python
from mypy_boto3_connect.type_defs import GetFederationTokenResponseTypeDef
```




Optional fields:
- `Credentials`: `"CredentialsTypeDef"`


## GetMetricDataResponseTypeDef

```python
from mypy_boto3_connect.type_defs import GetMetricDataResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MetricResults`: `List["HistoricalMetricResultTypeDef"]`


## HierarchyGroupSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyGroupSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## HierarchyGroupTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyGroupTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `LevelId`: `str`
- `HierarchyPath`: `"HierarchyPathTypeDef"`


## HierarchyLevelTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyLevelTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## HierarchyLevelUpdateTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyLevelUpdateTypeDef
```


Required fields:
- `Name`: `str`




## HierarchyPathTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyPathTypeDef
```




Optional fields:
- `LevelOne`: `"HierarchyGroupSummaryTypeDef"`
- `LevelTwo`: `"HierarchyGroupSummaryTypeDef"`
- `LevelThree`: `"HierarchyGroupSummaryTypeDef"`
- `LevelFour`: `"HierarchyGroupSummaryTypeDef"`
- `LevelFive`: `"HierarchyGroupSummaryTypeDef"`


## HierarchyStructureTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyStructureTypeDef
```




Optional fields:
- `LevelOne`: `"HierarchyLevelTypeDef"`
- `LevelTwo`: `"HierarchyLevelTypeDef"`
- `LevelThree`: `"HierarchyLevelTypeDef"`
- `LevelFour`: `"HierarchyLevelTypeDef"`
- `LevelFive`: `"HierarchyLevelTypeDef"`


## HierarchyStructureUpdateTypeDef

```python
from mypy_boto3_connect.type_defs import HierarchyStructureUpdateTypeDef
```




Optional fields:
- `LevelOne`: `"HierarchyLevelUpdateTypeDef"`
- `LevelTwo`: `"HierarchyLevelUpdateTypeDef"`
- `LevelThree`: `"HierarchyLevelUpdateTypeDef"`
- `LevelFour`: `"HierarchyLevelUpdateTypeDef"`
- `LevelFive`: `"HierarchyLevelUpdateTypeDef"`


## HistoricalMetricDataTypeDef

```python
from mypy_boto3_connect.type_defs import HistoricalMetricDataTypeDef
```




Optional fields:
- `Metric`: `"HistoricalMetricTypeDef"`
- `Value`: `float`


## HistoricalMetricResultTypeDef

```python
from mypy_boto3_connect.type_defs import HistoricalMetricResultTypeDef
```




Optional fields:
- `Dimensions`: `"DimensionsTypeDef"`
- `Collections`: `List["HistoricalMetricDataTypeDef"]`


## HistoricalMetricTypeDef

```python
from mypy_boto3_connect.type_defs import HistoricalMetricTypeDef
```




Optional fields:
- `Name`: `HistoricalMetricName`
- `Threshold`: `"ThresholdTypeDef"`
- `Statistic`: `Statistic`
- `Unit`: `Unit`


## HoursOfOperationConfigTypeDef

```python
from mypy_boto3_connect.type_defs import HoursOfOperationConfigTypeDef
```




Optional fields:
- `Day`: `HoursOfOperationDays`
- `StartTime`: `"HoursOfOperationTimeSliceTypeDef"`
- `EndTime`: `"HoursOfOperationTimeSliceTypeDef"`


## HoursOfOperationSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import HoursOfOperationSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## HoursOfOperationTimeSliceTypeDef

```python
from mypy_boto3_connect.type_defs import HoursOfOperationTimeSliceTypeDef
```




Optional fields:
- `Hours`: `int`
- `Minutes`: `int`


## HoursOfOperationTypeDef

```python
from mypy_boto3_connect.type_defs import HoursOfOperationTypeDef
```




Optional fields:
- `HoursOfOperationId`: `str`
- `HoursOfOperationArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `TimeZone`: `str`
- `Config`: `List["HoursOfOperationConfigTypeDef"]`
- `Tags`: `Dict[str, str]`


## InstanceStatusReasonTypeDef

```python
from mypy_boto3_connect.type_defs import InstanceStatusReasonTypeDef
```




Optional fields:
- `Message`: `str`


## InstanceStorageConfigTypeDef

```python
from mypy_boto3_connect.type_defs import InstanceStorageConfigTypeDef
```


Required fields:
- `StorageType`: `StorageType`



Optional fields:
- `AssociationId`: `str`
- `S3Config`: `"S3ConfigTypeDef"`
- `KinesisVideoStreamConfig`: `"KinesisVideoStreamConfigTypeDef"`
- `KinesisStreamConfig`: `"KinesisStreamConfigTypeDef"`
- `KinesisFirehoseConfig`: `"KinesisFirehoseConfigTypeDef"`


## InstanceSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import InstanceSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `IdentityManagementType`: `DirectoryType`
- `InstanceAlias`: `str`
- `CreatedTime`: `datetime`
- `ServiceRole`: `str`
- `InstanceStatus`: `InstanceStatus`
- `InboundCallsEnabled`: `bool`
- `OutboundCallsEnabled`: `bool`


## InstanceTypeDef

```python
from mypy_boto3_connect.type_defs import InstanceTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `IdentityManagementType`: `DirectoryType`
- `InstanceAlias`: `str`
- `CreatedTime`: `datetime`
- `ServiceRole`: `str`
- `InstanceStatus`: `InstanceStatus`
- `StatusReason`: `"InstanceStatusReasonTypeDef"`
- `InboundCallsEnabled`: `bool`
- `OutboundCallsEnabled`: `bool`


## IntegrationAssociationSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import IntegrationAssociationSummaryTypeDef
```




Optional fields:
- `IntegrationAssociationId`: `str`
- `IntegrationAssociationArn`: `str`
- `InstanceId`: `str`
- `IntegrationType`: `Literal['EVENT']`
- `IntegrationArn`: `str`
- `SourceApplicationUrl`: `str`
- `SourceApplicationName`: `str`
- `SourceType`: `SourceType`


## KinesisFirehoseConfigTypeDef

```python
from mypy_boto3_connect.type_defs import KinesisFirehoseConfigTypeDef
```


Required fields:
- `FirehoseArn`: `str`




## KinesisStreamConfigTypeDef

```python
from mypy_boto3_connect.type_defs import KinesisStreamConfigTypeDef
```


Required fields:
- `StreamArn`: `str`




## KinesisVideoStreamConfigTypeDef

```python
from mypy_boto3_connect.type_defs import KinesisVideoStreamConfigTypeDef
```


Required fields:
- `Prefix`: `str`
- `RetentionPeriodHours`: `int`
- `EncryptionConfig`: `"EncryptionConfigTypeDef"`




## LexBotTypeDef

```python
from mypy_boto3_connect.type_defs import LexBotTypeDef
```




Optional fields:
- `Name`: `str`
- `LexRegion`: `str`


## ListApprovedOriginsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListApprovedOriginsResponseTypeDef
```




Optional fields:
- `Origins`: `List[str]`
- `NextToken`: `str`


## ListContactFlowsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListContactFlowsResponseTypeDef
```




Optional fields:
- `ContactFlowSummaryList`: `List["ContactFlowSummaryTypeDef"]`
- `NextToken`: `str`


## ListHoursOfOperationsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListHoursOfOperationsResponseTypeDef
```




Optional fields:
- `HoursOfOperationSummaryList`: `List["HoursOfOperationSummaryTypeDef"]`
- `NextToken`: `str`


## ListInstanceAttributesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListInstanceAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeTypeDef"]`
- `NextToken`: `str`


## ListInstanceStorageConfigsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListInstanceStorageConfigsResponseTypeDef
```




Optional fields:
- `StorageConfigs`: `List["InstanceStorageConfigTypeDef"]`
- `NextToken`: `str`


## ListInstancesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListInstancesResponseTypeDef
```




Optional fields:
- `InstanceSummaryList`: `List["InstanceSummaryTypeDef"]`
- `NextToken`: `str`


## ListIntegrationAssociationsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListIntegrationAssociationsResponseTypeDef
```




Optional fields:
- `IntegrationAssociationSummaryList`: `List["IntegrationAssociationSummaryTypeDef"]`
- `NextToken`: `str`


## ListLambdaFunctionsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListLambdaFunctionsResponseTypeDef
```




Optional fields:
- `LambdaFunctions`: `List[str]`
- `NextToken`: `str`


## ListLexBotsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListLexBotsResponseTypeDef
```




Optional fields:
- `LexBots`: `List["LexBotTypeDef"]`
- `NextToken`: `str`


## ListPhoneNumbersResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListPhoneNumbersResponseTypeDef
```




Optional fields:
- `PhoneNumberSummaryList`: `List["PhoneNumberSummaryTypeDef"]`
- `NextToken`: `str`


## ListPromptsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListPromptsResponseTypeDef
```




Optional fields:
- `PromptSummaryList`: `List["PromptSummaryTypeDef"]`
- `NextToken`: `str`


## ListQueueQuickConnectsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListQueueQuickConnectsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `QuickConnectSummaryList`: `List["QuickConnectSummaryTypeDef"]`


## ListQueuesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListQueuesResponseTypeDef
```




Optional fields:
- `QueueSummaryList`: `List["QueueSummaryTypeDef"]`
- `NextToken`: `str`


## ListQuickConnectsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListQuickConnectsResponseTypeDef
```




Optional fields:
- `QuickConnectSummaryList`: `List["QuickConnectSummaryTypeDef"]`
- `NextToken`: `str`


## ListRoutingProfileQueuesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListRoutingProfileQueuesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `RoutingProfileQueueConfigSummaryList`: `List["RoutingProfileQueueConfigSummaryTypeDef"]`


## ListRoutingProfilesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListRoutingProfilesResponseTypeDef
```




Optional fields:
- `RoutingProfileSummaryList`: `List["RoutingProfileSummaryTypeDef"]`
- `NextToken`: `str`


## ListSecurityKeysResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListSecurityKeysResponseTypeDef
```




Optional fields:
- `SecurityKeys`: `List["SecurityKeyTypeDef"]`
- `NextToken`: `str`


## ListSecurityProfilesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListSecurityProfilesResponseTypeDef
```




Optional fields:
- `SecurityProfileSummaryList`: `List["SecurityProfileSummaryTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListUseCasesResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListUseCasesResponseTypeDef
```




Optional fields:
- `UseCaseSummaryList`: `List["UseCaseTypeDef"]`
- `NextToken`: `str`


## ListUserHierarchyGroupsResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListUserHierarchyGroupsResponseTypeDef
```




Optional fields:
- `UserHierarchyGroupSummaryList`: `List["HierarchyGroupSummaryTypeDef"]`
- `NextToken`: `str`


## ListUsersResponseTypeDef

```python
from mypy_boto3_connect.type_defs import ListUsersResponseTypeDef
```




Optional fields:
- `UserSummaryList`: `List["UserSummaryTypeDef"]`
- `NextToken`: `str`


## MediaConcurrencyTypeDef

```python
from mypy_boto3_connect.type_defs import MediaConcurrencyTypeDef
```


Required fields:
- `Channel`: `Channel`
- `Concurrency`: `int`




## OutboundCallerConfigTypeDef

```python
from mypy_boto3_connect.type_defs import OutboundCallerConfigTypeDef
```




Optional fields:
- `OutboundCallerIdName`: `str`
- `OutboundCallerIdNumberId`: `str`
- `OutboundFlowId`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_connect.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParticipantDetailsTypeDef

```python
from mypy_boto3_connect.type_defs import ParticipantDetailsTypeDef
```


Required fields:
- `DisplayName`: `str`




## PhoneNumberQuickConnectConfigTypeDef

```python
from mypy_boto3_connect.type_defs import PhoneNumberQuickConnectConfigTypeDef
```


Required fields:
- `PhoneNumber`: `str`




## PhoneNumberSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import PhoneNumberSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `PhoneNumber`: `str`
- `PhoneNumberType`: `PhoneNumberType`
- `PhoneNumberCountryCode`: `PhoneNumberCountryCode`


## PromptSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import PromptSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## QueueQuickConnectConfigTypeDef

```python
from mypy_boto3_connect.type_defs import QueueQuickConnectConfigTypeDef
```


Required fields:
- `QueueId`: `str`
- `ContactFlowId`: `str`




## QueueReferenceTypeDef

```python
from mypy_boto3_connect.type_defs import QueueReferenceTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`


## QueueSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import QueueSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `QueueType`: `QueueType`


## QueueTypeDef

```python
from mypy_boto3_connect.type_defs import QueueTypeDef
```




Optional fields:
- `Name`: `str`
- `QueueArn`: `str`
- `QueueId`: `str`
- `Description`: `str`
- `OutboundCallerConfig`: `"OutboundCallerConfigTypeDef"`
- `HoursOfOperationId`: `str`
- `MaxContacts`: `int`
- `Status`: `QueueStatus`
- `Tags`: `Dict[str, str]`


## QuickConnectConfigTypeDef

```python
from mypy_boto3_connect.type_defs import QuickConnectConfigTypeDef
```


Required fields:
- `QuickConnectType`: `QuickConnectType`



Optional fields:
- `UserConfig`: `"UserQuickConnectConfigTypeDef"`
- `QueueConfig`: `"QueueQuickConnectConfigTypeDef"`
- `PhoneConfig`: `"PhoneNumberQuickConnectConfigTypeDef"`


## QuickConnectSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import QuickConnectSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`
- `QuickConnectType`: `QuickConnectType`


## QuickConnectTypeDef

```python
from mypy_boto3_connect.type_defs import QuickConnectTypeDef
```




Optional fields:
- `QuickConnectARN`: `str`
- `QuickConnectId`: `str`
- `Name`: `str`
- `Description`: `str`
- `QuickConnectConfig`: `"QuickConnectConfigTypeDef"`
- `Tags`: `Dict[str, str]`


## ReferenceTypeDef

```python
from mypy_boto3_connect.type_defs import ReferenceTypeDef
```


Required fields:
- `Value`: `str`
- `Type`: `Literal['URL']`




## RoutingProfileQueueConfigSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import RoutingProfileQueueConfigSummaryTypeDef
```


Required fields:
- `QueueId`: `str`
- `QueueArn`: `str`
- `QueueName`: `str`
- `Priority`: `int`
- `Delay`: `int`
- `Channel`: `Channel`




## RoutingProfileQueueConfigTypeDef

```python
from mypy_boto3_connect.type_defs import RoutingProfileQueueConfigTypeDef
```


Required fields:
- `QueueReference`: `"RoutingProfileQueueReferenceTypeDef"`
- `Priority`: `int`
- `Delay`: `int`




## RoutingProfileQueueReferenceTypeDef

```python
from mypy_boto3_connect.type_defs import RoutingProfileQueueReferenceTypeDef
```


Required fields:
- `QueueId`: `str`
- `Channel`: `Channel`




## RoutingProfileSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import RoutingProfileSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## RoutingProfileTypeDef

```python
from mypy_boto3_connect.type_defs import RoutingProfileTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `Name`: `str`
- `RoutingProfileArn`: `str`
- `RoutingProfileId`: `str`
- `Description`: `str`
- `MediaConcurrencies`: `List["MediaConcurrencyTypeDef"]`
- `DefaultOutboundQueueId`: `str`
- `Tags`: `Dict[str, str]`


## S3ConfigTypeDef

```python
from mypy_boto3_connect.type_defs import S3ConfigTypeDef
```


Required fields:
- `BucketName`: `str`
- `BucketPrefix`: `str`



Optional fields:
- `EncryptionConfig`: `"EncryptionConfigTypeDef"`


## SecurityKeyTypeDef

```python
from mypy_boto3_connect.type_defs import SecurityKeyTypeDef
```




Optional fields:
- `AssociationId`: `str`
- `Key`: `str`
- `CreationTime`: `datetime`


## SecurityProfileSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import SecurityProfileSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Name`: `str`


## StartChatContactResponseTypeDef

```python
from mypy_boto3_connect.type_defs import StartChatContactResponseTypeDef
```




Optional fields:
- `ContactId`: `str`
- `ParticipantId`: `str`
- `ParticipantToken`: `str`


## StartOutboundVoiceContactResponseTypeDef

```python
from mypy_boto3_connect.type_defs import StartOutboundVoiceContactResponseTypeDef
```




Optional fields:
- `ContactId`: `str`


## StartTaskContactResponseTypeDef

```python
from mypy_boto3_connect.type_defs import StartTaskContactResponseTypeDef
```




Optional fields:
- `ContactId`: `str`


## ThresholdTypeDef

```python
from mypy_boto3_connect.type_defs import ThresholdTypeDef
```




Optional fields:
- `Comparison`: `Literal['LT']`
- `ThresholdValue`: `float`


## UseCaseTypeDef

```python
from mypy_boto3_connect.type_defs import UseCaseTypeDef
```




Optional fields:
- `UseCaseId`: `str`
- `UseCaseArn`: `str`
- `UseCaseType`: `Literal['RULES_EVALUATION']`


## UserIdentityInfoTypeDef

```python
from mypy_boto3_connect.type_defs import UserIdentityInfoTypeDef
```




Optional fields:
- `FirstName`: `str`
- `LastName`: `str`
- `Email`: `str`


## UserPhoneConfigTypeDef

```python
from mypy_boto3_connect.type_defs import UserPhoneConfigTypeDef
```


Required fields:
- `PhoneType`: `PhoneType`



Optional fields:
- `AutoAccept`: `bool`
- `AfterContactWorkTimeLimit`: `int`
- `DeskPhoneNumber`: `str`


## UserQuickConnectConfigTypeDef

```python
from mypy_boto3_connect.type_defs import UserQuickConnectConfigTypeDef
```


Required fields:
- `UserId`: `str`
- `ContactFlowId`: `str`




## UserSummaryTypeDef

```python
from mypy_boto3_connect.type_defs import UserSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Username`: `str`


## UserTypeDef

```python
from mypy_boto3_connect.type_defs import UserTypeDef
```




Optional fields:
- `Id`: `str`
- `Arn`: `str`
- `Username`: `str`
- `IdentityInfo`: `"UserIdentityInfoTypeDef"`
- `PhoneConfig`: `"UserPhoneConfigTypeDef"`
- `DirectoryUserId`: `str`
- `SecurityProfileIds`: `List[str]`
- `RoutingProfileId`: `str`
- `HierarchyGroupId`: `str`
- `Tags`: `Dict[str, str]`


## VoiceRecordingConfigurationTypeDef

```python
from mypy_boto3_connect.type_defs import VoiceRecordingConfigurationTypeDef
```




Optional fields:
- `VoiceRecordingTrack`: `VoiceRecordingTrack`

