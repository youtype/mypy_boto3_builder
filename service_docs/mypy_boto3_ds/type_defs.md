# Structures for boto3 DirectoryService module

> [Index](../index.md) > [DirectoryService](./index.md) > Structures

Auto-generated documentation for [DirectoryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService)
type annotations stubs module [mypy_boto3_ds](https://pypi.org/project/mypy-boto3-ds/).

- [Structures for boto3 DirectoryService module](#structures-for-boto3-directoryservice-module)
  - [AcceptSharedDirectoryResultTypeDef](#acceptshareddirectoryresulttypedef)
  - [AttributeTypeDef](#attributetypedef)
  - [CertificateInfoTypeDef](#certificateinfotypedef)
  - [CertificateTypeDef](#certificatetypedef)
  - [ClientCertAuthSettingsTypeDef](#clientcertauthsettingstypedef)
  - [ComputerTypeDef](#computertypedef)
  - [ConditionalForwarderTypeDef](#conditionalforwardertypedef)
  - [ConnectDirectoryResultTypeDef](#connectdirectoryresulttypedef)
  - [CreateAliasResultTypeDef](#createaliasresulttypedef)
  - [CreateComputerResultTypeDef](#createcomputerresulttypedef)
  - [CreateDirectoryResultTypeDef](#createdirectoryresulttypedef)
  - [CreateMicrosoftADResultTypeDef](#createmicrosoftadresulttypedef)
  - [CreateSnapshotResultTypeDef](#createsnapshotresulttypedef)
  - [CreateTrustResultTypeDef](#createtrustresulttypedef)
  - [DeleteDirectoryResultTypeDef](#deletedirectoryresulttypedef)
  - [DeleteSnapshotResultTypeDef](#deletesnapshotresulttypedef)
  - [DeleteTrustResultTypeDef](#deletetrustresulttypedef)
  - [DescribeCertificateResultTypeDef](#describecertificateresulttypedef)
  - [DescribeConditionalForwardersResultTypeDef](#describeconditionalforwardersresulttypedef)
  - [DescribeDirectoriesResultTypeDef](#describedirectoriesresulttypedef)
  - [DescribeDomainControllersResultTypeDef](#describedomaincontrollersresulttypedef)
  - [DescribeEventTopicsResultTypeDef](#describeeventtopicsresulttypedef)
  - [DescribeLDAPSSettingsResultTypeDef](#describeldapssettingsresulttypedef)
  - [DescribeRegionsResultTypeDef](#describeregionsresulttypedef)
  - [DescribeSharedDirectoriesResultTypeDef](#describeshareddirectoriesresulttypedef)
  - [DescribeSnapshotsResultTypeDef](#describesnapshotsresulttypedef)
  - [DescribeTrustsResultTypeDef](#describetrustsresulttypedef)
  - [DirectoryConnectSettingsDescriptionTypeDef](#directoryconnectsettingsdescriptiontypedef)
  - [DirectoryConnectSettingsTypeDef](#directoryconnectsettingstypedef)
  - [DirectoryDescriptionTypeDef](#directorydescriptiontypedef)
  - [DirectoryLimitsTypeDef](#directorylimitstypedef)
  - [DirectoryVpcSettingsDescriptionTypeDef](#directoryvpcsettingsdescriptiontypedef)
  - [DirectoryVpcSettingsTypeDef](#directoryvpcsettingstypedef)
  - [DomainControllerTypeDef](#domaincontrollertypedef)
  - [EventTopicTypeDef](#eventtopictypedef)
  - [GetDirectoryLimitsResultTypeDef](#getdirectorylimitsresulttypedef)
  - [GetSnapshotLimitsResultTypeDef](#getsnapshotlimitsresulttypedef)
  - [IpRouteInfoTypeDef](#iprouteinfotypedef)
  - [IpRouteTypeDef](#iproutetypedef)
  - [LDAPSSettingInfoTypeDef](#ldapssettinginfotypedef)
  - [ListCertificatesResultTypeDef](#listcertificatesresulttypedef)
  - [ListIpRoutesResultTypeDef](#listiproutesresulttypedef)
  - [ListLogSubscriptionsResultTypeDef](#listlogsubscriptionsresulttypedef)
  - [ListSchemaExtensionsResultTypeDef](#listschemaextensionsresulttypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [LogSubscriptionTypeDef](#logsubscriptiontypedef)
  - [OwnerDirectoryDescriptionTypeDef](#ownerdirectorydescriptiontypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RadiusSettingsTypeDef](#radiussettingstypedef)
  - [RegionDescriptionTypeDef](#regiondescriptiontypedef)
  - [RegionsInfoTypeDef](#regionsinfotypedef)
  - [RegisterCertificateResultTypeDef](#registercertificateresulttypedef)
  - [RejectSharedDirectoryResultTypeDef](#rejectshareddirectoryresulttypedef)
  - [SchemaExtensionInfoTypeDef](#schemaextensioninfotypedef)
  - [ShareDirectoryResultTypeDef](#sharedirectoryresulttypedef)
  - [ShareTargetTypeDef](#sharetargettypedef)
  - [SharedDirectoryTypeDef](#shareddirectorytypedef)
  - [SnapshotLimitsTypeDef](#snapshotlimitstypedef)
  - [SnapshotTypeDef](#snapshottypedef)
  - [StartSchemaExtensionResultTypeDef](#startschemaextensionresulttypedef)
  - [TagTypeDef](#tagtypedef)
  - [TrustTypeDef](#trusttypedef)
  - [UnshareDirectoryResultTypeDef](#unsharedirectoryresulttypedef)
  - [UnshareTargetTypeDef](#unsharetargettypedef)
  - [UpdateTrustResultTypeDef](#updatetrustresulttypedef)
  - [VerifyTrustResultTypeDef](#verifytrustresulttypedef)

## AcceptSharedDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import AcceptSharedDirectoryResultTypeDef
```




Optional fields:
- `SharedDirectory`: `"SharedDirectoryTypeDef"`


## AttributeTypeDef

```python
from mypy_boto3_ds.type_defs import AttributeTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## CertificateInfoTypeDef

```python
from mypy_boto3_ds.type_defs import CertificateInfoTypeDef
```




Optional fields:
- `CertificateId`: `str`
- `CommonName`: `str`
- `State`: `CertificateState`
- `ExpiryDateTime`: `datetime`
- `Type`: `CertificateType`


## CertificateTypeDef

```python
from mypy_boto3_ds.type_defs import CertificateTypeDef
```




Optional fields:
- `CertificateId`: `str`
- `State`: `CertificateState`
- `StateReason`: `str`
- `CommonName`: `str`
- `RegisteredDateTime`: `datetime`
- `ExpiryDateTime`: `datetime`
- `Type`: `CertificateType`
- `ClientCertAuthSettings`: `"ClientCertAuthSettingsTypeDef"`


## ClientCertAuthSettingsTypeDef

```python
from mypy_boto3_ds.type_defs import ClientCertAuthSettingsTypeDef
```




Optional fields:
- `OCSPUrl`: `str`


## ComputerTypeDef

```python
from mypy_boto3_ds.type_defs import ComputerTypeDef
```




Optional fields:
- `ComputerId`: `str`
- `ComputerName`: `str`
- `ComputerAttributes`: `List["AttributeTypeDef"]`


## ConditionalForwarderTypeDef

```python
from mypy_boto3_ds.type_defs import ConditionalForwarderTypeDef
```




Optional fields:
- `RemoteDomainName`: `str`
- `DnsIpAddrs`: `List[str]`
- `ReplicationScope`: `Literal['Domain']`


## ConnectDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import ConnectDirectoryResultTypeDef
```




Optional fields:
- `DirectoryId`: `str`


## CreateAliasResultTypeDef

```python
from mypy_boto3_ds.type_defs import CreateAliasResultTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `Alias`: `str`


## CreateComputerResultTypeDef

```python
from mypy_boto3_ds.type_defs import CreateComputerResultTypeDef
```




Optional fields:
- `Computer`: `"ComputerTypeDef"`


## CreateDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import CreateDirectoryResultTypeDef
```




Optional fields:
- `DirectoryId`: `str`


## CreateMicrosoftADResultTypeDef

```python
from mypy_boto3_ds.type_defs import CreateMicrosoftADResultTypeDef
```




Optional fields:
- `DirectoryId`: `str`


## CreateSnapshotResultTypeDef

```python
from mypy_boto3_ds.type_defs import CreateSnapshotResultTypeDef
```




Optional fields:
- `SnapshotId`: `str`


## CreateTrustResultTypeDef

```python
from mypy_boto3_ds.type_defs import CreateTrustResultTypeDef
```




Optional fields:
- `TrustId`: `str`


## DeleteDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import DeleteDirectoryResultTypeDef
```




Optional fields:
- `DirectoryId`: `str`


## DeleteSnapshotResultTypeDef

```python
from mypy_boto3_ds.type_defs import DeleteSnapshotResultTypeDef
```




Optional fields:
- `SnapshotId`: `str`


## DeleteTrustResultTypeDef

```python
from mypy_boto3_ds.type_defs import DeleteTrustResultTypeDef
```




Optional fields:
- `TrustId`: `str`


## DescribeCertificateResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeCertificateResultTypeDef
```




Optional fields:
- `Certificate`: `"CertificateTypeDef"`


## DescribeConditionalForwardersResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeConditionalForwardersResultTypeDef
```




Optional fields:
- `ConditionalForwarders`: `List["ConditionalForwarderTypeDef"]`


## DescribeDirectoriesResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeDirectoriesResultTypeDef
```




Optional fields:
- `DirectoryDescriptions`: `List["DirectoryDescriptionTypeDef"]`
- `NextToken`: `str`


## DescribeDomainControllersResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeDomainControllersResultTypeDef
```




Optional fields:
- `DomainControllers`: `List["DomainControllerTypeDef"]`
- `NextToken`: `str`


## DescribeEventTopicsResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeEventTopicsResultTypeDef
```




Optional fields:
- `EventTopics`: `List["EventTopicTypeDef"]`


## DescribeLDAPSSettingsResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeLDAPSSettingsResultTypeDef
```




Optional fields:
- `LDAPSSettingsInfo`: `List["LDAPSSettingInfoTypeDef"]`
- `NextToken`: `str`


## DescribeRegionsResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeRegionsResultTypeDef
```




Optional fields:
- `RegionsDescription`: `List["RegionDescriptionTypeDef"]`
- `NextToken`: `str`


## DescribeSharedDirectoriesResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeSharedDirectoriesResultTypeDef
```




Optional fields:
- `SharedDirectories`: `List["SharedDirectoryTypeDef"]`
- `NextToken`: `str`


## DescribeSnapshotsResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeSnapshotsResultTypeDef
```




Optional fields:
- `Snapshots`: `List["SnapshotTypeDef"]`
- `NextToken`: `str`


## DescribeTrustsResultTypeDef

```python
from mypy_boto3_ds.type_defs import DescribeTrustsResultTypeDef
```




Optional fields:
- `Trusts`: `List["TrustTypeDef"]`
- `NextToken`: `str`


## DirectoryConnectSettingsDescriptionTypeDef

```python
from mypy_boto3_ds.type_defs import DirectoryConnectSettingsDescriptionTypeDef
```




Optional fields:
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `CustomerUserName`: `str`
- `SecurityGroupId`: `str`
- `AvailabilityZones`: `List[str]`
- `ConnectIps`: `List[str]`


## DirectoryConnectSettingsTypeDef

```python
from mypy_boto3_ds.type_defs import DirectoryConnectSettingsTypeDef
```


Required fields:
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `CustomerDnsIps`: `List[str]`
- `CustomerUserName`: `str`




## DirectoryDescriptionTypeDef

```python
from mypy_boto3_ds.type_defs import DirectoryDescriptionTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `Name`: `str`
- `ShortName`: `str`
- `Size`: `DirectorySize`
- `Edition`: `DirectoryEdition`
- `Alias`: `str`
- `AccessUrl`: `str`
- `Description`: `str`
- `DnsIpAddrs`: `List[str]`
- `Stage`: `DirectoryStage`
- `ShareStatus`: `ShareStatus`
- `ShareMethod`: `ShareMethod`
- `ShareNotes`: `str`
- `LaunchTime`: `datetime`
- `StageLastUpdatedDateTime`: `datetime`
- `Type`: `DirectoryType`
- `VpcSettings`: `"DirectoryVpcSettingsDescriptionTypeDef"`
- `ConnectSettings`: `"DirectoryConnectSettingsDescriptionTypeDef"`
- `RadiusSettings`: `"RadiusSettingsTypeDef"`
- `RadiusStatus`: `RadiusStatus`
- `StageReason`: `str`
- `SsoEnabled`: `bool`
- `DesiredNumberOfDomainControllers`: `int`
- `OwnerDirectoryDescription`: `"OwnerDirectoryDescriptionTypeDef"`
- `RegionsInfo`: `"RegionsInfoTypeDef"`


## DirectoryLimitsTypeDef

```python
from mypy_boto3_ds.type_defs import DirectoryLimitsTypeDef
```




Optional fields:
- `CloudOnlyDirectoriesLimit`: `int`
- `CloudOnlyDirectoriesCurrentCount`: `int`
- `CloudOnlyDirectoriesLimitReached`: `bool`
- `CloudOnlyMicrosoftADLimit`: `int`
- `CloudOnlyMicrosoftADCurrentCount`: `int`
- `CloudOnlyMicrosoftADLimitReached`: `bool`
- `ConnectedDirectoriesLimit`: `int`
- `ConnectedDirectoriesCurrentCount`: `int`
- `ConnectedDirectoriesLimitReached`: `bool`


## DirectoryVpcSettingsDescriptionTypeDef

```python
from mypy_boto3_ds.type_defs import DirectoryVpcSettingsDescriptionTypeDef
```




Optional fields:
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `SecurityGroupId`: `str`
- `AvailabilityZones`: `List[str]`


## DirectoryVpcSettingsTypeDef

```python
from mypy_boto3_ds.type_defs import DirectoryVpcSettingsTypeDef
```


Required fields:
- `VpcId`: `str`
- `SubnetIds`: `List[str]`




## DomainControllerTypeDef

```python
from mypy_boto3_ds.type_defs import DomainControllerTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `DomainControllerId`: `str`
- `DnsIpAddr`: `str`
- `VpcId`: `str`
- `SubnetId`: `str`
- `AvailabilityZone`: `str`
- `Status`: `DomainControllerStatus`
- `StatusReason`: `str`
- `LaunchTime`: `datetime`
- `StatusLastUpdatedDateTime`: `datetime`


## EventTopicTypeDef

```python
from mypy_boto3_ds.type_defs import EventTopicTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `TopicName`: `str`
- `TopicArn`: `str`
- `CreatedDateTime`: `datetime`
- `Status`: `TopicStatus`


## GetDirectoryLimitsResultTypeDef

```python
from mypy_boto3_ds.type_defs import GetDirectoryLimitsResultTypeDef
```




Optional fields:
- `DirectoryLimits`: `"DirectoryLimitsTypeDef"`


## GetSnapshotLimitsResultTypeDef

```python
from mypy_boto3_ds.type_defs import GetSnapshotLimitsResultTypeDef
```




Optional fields:
- `SnapshotLimits`: `"SnapshotLimitsTypeDef"`


## IpRouteInfoTypeDef

```python
from mypy_boto3_ds.type_defs import IpRouteInfoTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `CidrIp`: `str`
- `IpRouteStatusMsg`: `IpRouteStatusMsg`
- `AddedDateTime`: `datetime`
- `IpRouteStatusReason`: `str`
- `Description`: `str`


## IpRouteTypeDef

```python
from mypy_boto3_ds.type_defs import IpRouteTypeDef
```




Optional fields:
- `CidrIp`: `str`
- `Description`: `str`


## LDAPSSettingInfoTypeDef

```python
from mypy_boto3_ds.type_defs import LDAPSSettingInfoTypeDef
```




Optional fields:
- `LDAPSStatus`: `LDAPSStatus`
- `LDAPSStatusReason`: `str`
- `LastUpdatedDateTime`: `datetime`


## ListCertificatesResultTypeDef

```python
from mypy_boto3_ds.type_defs import ListCertificatesResultTypeDef
```




Optional fields:
- `NextToken`: `str`
- `CertificatesInfo`: `List["CertificateInfoTypeDef"]`


## ListIpRoutesResultTypeDef

```python
from mypy_boto3_ds.type_defs import ListIpRoutesResultTypeDef
```




Optional fields:
- `IpRoutesInfo`: `List["IpRouteInfoTypeDef"]`
- `NextToken`: `str`


## ListLogSubscriptionsResultTypeDef

```python
from mypy_boto3_ds.type_defs import ListLogSubscriptionsResultTypeDef
```




Optional fields:
- `LogSubscriptions`: `List["LogSubscriptionTypeDef"]`
- `NextToken`: `str`


## ListSchemaExtensionsResultTypeDef

```python
from mypy_boto3_ds.type_defs import ListSchemaExtensionsResultTypeDef
```




Optional fields:
- `SchemaExtensionsInfo`: `List["SchemaExtensionInfoTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_ds.type_defs import ListTagsForResourceResultTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## LogSubscriptionTypeDef

```python
from mypy_boto3_ds.type_defs import LogSubscriptionTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `LogGroupName`: `str`
- `SubscriptionCreatedDateTime`: `datetime`


## OwnerDirectoryDescriptionTypeDef

```python
from mypy_boto3_ds.type_defs import OwnerDirectoryDescriptionTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `AccountId`: `str`
- `DnsIpAddrs`: `List[str]`
- `VpcSettings`: `"DirectoryVpcSettingsDescriptionTypeDef"`
- `RadiusSettings`: `"RadiusSettingsTypeDef"`
- `RadiusStatus`: `RadiusStatus`


## PaginatorConfigTypeDef

```python
from mypy_boto3_ds.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RadiusSettingsTypeDef

```python
from mypy_boto3_ds.type_defs import RadiusSettingsTypeDef
```




Optional fields:
- `RadiusServers`: `List[str]`
- `RadiusPort`: `int`
- `RadiusTimeout`: `int`
- `RadiusRetries`: `int`
- `SharedSecret`: `str`
- `AuthenticationProtocol`: `RadiusAuthenticationProtocol`
- `DisplayLabel`: `str`
- `UseSameUsername`: `bool`


## RegionDescriptionTypeDef

```python
from mypy_boto3_ds.type_defs import RegionDescriptionTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `RegionName`: `str`
- `RegionType`: `RegionType`
- `Status`: `DirectoryStage`
- `VpcSettings`: `"DirectoryVpcSettingsTypeDef"`
- `DesiredNumberOfDomainControllers`: `int`
- `LaunchTime`: `datetime`
- `StatusLastUpdatedDateTime`: `datetime`
- `LastUpdatedDateTime`: `datetime`


## RegionsInfoTypeDef

```python
from mypy_boto3_ds.type_defs import RegionsInfoTypeDef
```




Optional fields:
- `PrimaryRegion`: `str`
- `AdditionalRegions`: `List[str]`


## RegisterCertificateResultTypeDef

```python
from mypy_boto3_ds.type_defs import RegisterCertificateResultTypeDef
```




Optional fields:
- `CertificateId`: `str`


## RejectSharedDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import RejectSharedDirectoryResultTypeDef
```




Optional fields:
- `SharedDirectoryId`: `str`


## SchemaExtensionInfoTypeDef

```python
from mypy_boto3_ds.type_defs import SchemaExtensionInfoTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `SchemaExtensionId`: `str`
- `Description`: `str`
- `SchemaExtensionStatus`: `SchemaExtensionStatus`
- `SchemaExtensionStatusReason`: `str`
- `StartDateTime`: `datetime`
- `EndDateTime`: `datetime`


## ShareDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import ShareDirectoryResultTypeDef
```




Optional fields:
- `SharedDirectoryId`: `str`


## ShareTargetTypeDef

```python
from mypy_boto3_ds.type_defs import ShareTargetTypeDef
```


Required fields:
- `Id`: `str`
- `Type`: `Literal['ACCOUNT']`




## SharedDirectoryTypeDef

```python
from mypy_boto3_ds.type_defs import SharedDirectoryTypeDef
```




Optional fields:
- `OwnerAccountId`: `str`
- `OwnerDirectoryId`: `str`
- `ShareMethod`: `ShareMethod`
- `SharedAccountId`: `str`
- `SharedDirectoryId`: `str`
- `ShareStatus`: `ShareStatus`
- `ShareNotes`: `str`
- `CreatedDateTime`: `datetime`
- `LastUpdatedDateTime`: `datetime`


## SnapshotLimitsTypeDef

```python
from mypy_boto3_ds.type_defs import SnapshotLimitsTypeDef
```




Optional fields:
- `ManualSnapshotsLimit`: `int`
- `ManualSnapshotsCurrentCount`: `int`
- `ManualSnapshotsLimitReached`: `bool`


## SnapshotTypeDef

```python
from mypy_boto3_ds.type_defs import SnapshotTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `SnapshotId`: `str`
- `Type`: `SnapshotType`
- `Name`: `str`
- `Status`: `SnapshotStatus`
- `StartTime`: `datetime`


## StartSchemaExtensionResultTypeDef

```python
from mypy_boto3_ds.type_defs import StartSchemaExtensionResultTypeDef
```




Optional fields:
- `SchemaExtensionId`: `str`


## TagTypeDef

```python
from mypy_boto3_ds.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TrustTypeDef

```python
from mypy_boto3_ds.type_defs import TrustTypeDef
```




Optional fields:
- `DirectoryId`: `str`
- `TrustId`: `str`
- `RemoteDomainName`: `str`
- `TrustType`: `TrustType`
- `TrustDirection`: `TrustDirection`
- `TrustState`: `TrustState`
- `CreatedDateTime`: `datetime`
- `LastUpdatedDateTime`: `datetime`
- `StateLastUpdatedDateTime`: `datetime`
- `TrustStateReason`: `str`
- `SelectiveAuth`: `SelectiveAuth`


## UnshareDirectoryResultTypeDef

```python
from mypy_boto3_ds.type_defs import UnshareDirectoryResultTypeDef
```




Optional fields:
- `SharedDirectoryId`: `str`


## UnshareTargetTypeDef

```python
from mypy_boto3_ds.type_defs import UnshareTargetTypeDef
```


Required fields:
- `Id`: `str`
- `Type`: `Literal['ACCOUNT']`




## UpdateTrustResultTypeDef

```python
from mypy_boto3_ds.type_defs import UpdateTrustResultTypeDef
```




Optional fields:
- `RequestId`: `str`
- `TrustId`: `str`


## VerifyTrustResultTypeDef

```python
from mypy_boto3_ds.type_defs import VerifyTrustResultTypeDef
```




Optional fields:
- `TrustId`: `str`

