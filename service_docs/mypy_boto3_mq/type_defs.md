# Structures for boto3 MQ module

> [Index](../index.md) > [MQ](./index.md) > Structures

Auto-generated documentation for [MQ](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ)
type annotations stubs module [mypy_boto3_mq](https://pypi.org/project/mypy-boto3-mq/).

- [Structures for boto3 MQ module](#structures-for-boto3-mq-module)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [BrokerEngineTypeTypeDef](#brokerenginetypetypedef)
  - [BrokerInstanceOptionTypeDef](#brokerinstanceoptiontypedef)
  - [BrokerInstanceTypeDef](#brokerinstancetypedef)
  - [BrokerSummaryTypeDef](#brokersummarytypedef)
  - [ConfigurationIdTypeDef](#configurationidtypedef)
  - [ConfigurationRevisionTypeDef](#configurationrevisiontypedef)
  - [ConfigurationTypeDef](#configurationtypedef)
  - [ConfigurationsTypeDef](#configurationstypedef)
  - [EncryptionOptionsTypeDef](#encryptionoptionstypedef)
  - [EngineVersionTypeDef](#engineversiontypedef)
  - [LdapServerMetadataOutputTypeDef](#ldapservermetadataoutputtypedef)
  - [LogsSummaryTypeDef](#logssummarytypedef)
  - [LogsTypeDef](#logstypedef)
  - [PendingLogsTypeDef](#pendinglogstypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SanitizationWarningTypeDef](#sanitizationwarningtypedef)
  - [UserPendingChangesTypeDef](#userpendingchangestypedef)
  - [UserSummaryTypeDef](#usersummarytypedef)
  - [WeeklyStartTimeTypeDef](#weeklystarttimetypedef)
  - [CreateBrokerResponseTypeDef](#createbrokerresponsetypedef)
  - [CreateConfigurationResponseTypeDef](#createconfigurationresponsetypedef)
  - [DeleteBrokerResponseTypeDef](#deletebrokerresponsetypedef)
  - [DescribeBrokerEngineTypesResponseTypeDef](#describebrokerenginetypesresponsetypedef)
  - [DescribeBrokerInstanceOptionsResponseTypeDef](#describebrokerinstanceoptionsresponsetypedef)
  - [DescribeBrokerResponseTypeDef](#describebrokerresponsetypedef)
  - [DescribeConfigurationResponseTypeDef](#describeconfigurationresponsetypedef)
  - [DescribeConfigurationRevisionResponseTypeDef](#describeconfigurationrevisionresponsetypedef)
  - [DescribeUserResponseTypeDef](#describeuserresponsetypedef)
  - [LdapServerMetadataInputTypeDef](#ldapservermetadatainputtypedef)
  - [ListBrokersResponseTypeDef](#listbrokersresponsetypedef)
  - [ListConfigurationRevisionsResponseTypeDef](#listconfigurationrevisionsresponsetypedef)
  - [ListConfigurationsResponseTypeDef](#listconfigurationsresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateBrokerResponseTypeDef](#updatebrokerresponsetypedef)
  - [UpdateConfigurationResponseTypeDef](#updateconfigurationresponsetypedef)
  - [UserTypeDef](#usertypedef)

## AvailabilityZoneTypeDef

```python
from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `Name`: `str`


## BrokerEngineTypeTypeDef

```python
from mypy_boto3_mq.type_defs import BrokerEngineTypeTypeDef
```




Optional fields:
- `EngineType`: `EngineType`
- `EngineVersions`: `List["EngineVersionTypeDef"]`


## BrokerInstanceOptionTypeDef

```python
from mypy_boto3_mq.type_defs import BrokerInstanceOptionTypeDef
```




Optional fields:
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`
- `EngineType`: `EngineType`
- `HostInstanceType`: `str`
- `StorageType`: `BrokerStorageType`
- `SupportedDeploymentModes`: `List[DeploymentMode]`
- `SupportedEngineVersions`: `List[str]`


## BrokerInstanceTypeDef

```python
from mypy_boto3_mq.type_defs import BrokerInstanceTypeDef
```




Optional fields:
- `ConsoleURL`: `str`
- `Endpoints`: `List[str]`
- `IpAddress`: `str`


## BrokerSummaryTypeDef

```python
from mypy_boto3_mq.type_defs import BrokerSummaryTypeDef
```




Optional fields:
- `BrokerArn`: `str`
- `BrokerId`: `str`
- `BrokerName`: `str`
- `BrokerState`: `BrokerState`
- `Created`: `datetime`
- `DeploymentMode`: `DeploymentMode`
- `EngineType`: `EngineType`
- `HostInstanceType`: `str`


## ConfigurationIdTypeDef

```python
from mypy_boto3_mq.type_defs import ConfigurationIdTypeDef
```




Optional fields:
- `Id`: `str`
- `Revision`: `int`


## ConfigurationRevisionTypeDef

```python
from mypy_boto3_mq.type_defs import ConfigurationRevisionTypeDef
```




Optional fields:
- `Created`: `datetime`
- `Description`: `str`
- `Revision`: `int`


## ConfigurationTypeDef

```python
from mypy_boto3_mq.type_defs import ConfigurationTypeDef
```




Optional fields:
- `Arn`: `str`
- `AuthenticationStrategy`: `AuthenticationStrategy`
- `Created`: `datetime`
- `Description`: `str`
- `EngineType`: `EngineType`
- `EngineVersion`: `str`
- `Id`: `str`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`
- `Tags`: `Dict[str, str]`


## ConfigurationsTypeDef

```python
from mypy_boto3_mq.type_defs import ConfigurationsTypeDef
```




Optional fields:
- `Current`: `"ConfigurationIdTypeDef"`
- `History`: `List["ConfigurationIdTypeDef"]`
- `Pending`: `"ConfigurationIdTypeDef"`


## EncryptionOptionsTypeDef

```python
from mypy_boto3_mq.type_defs import EncryptionOptionsTypeDef
```


Required fields:
- `UseAwsOwnedKey`: `bool`



Optional fields:
- `KmsKeyId`: `str`


## EngineVersionTypeDef

```python
from mypy_boto3_mq.type_defs import EngineVersionTypeDef
```




Optional fields:
- `Name`: `str`


## LdapServerMetadataOutputTypeDef

```python
from mypy_boto3_mq.type_defs import LdapServerMetadataOutputTypeDef
```




Optional fields:
- `Hosts`: `List[str]`
- `RoleBase`: `str`
- `RoleName`: `str`
- `RoleSearchMatching`: `str`
- `RoleSearchSubtree`: `bool`
- `ServiceAccountUsername`: `str`
- `UserBase`: `str`
- `UserRoleName`: `str`
- `UserSearchMatching`: `str`
- `UserSearchSubtree`: `bool`
- `ResponseMetadata`: `"ResponseMetadata"`


## LogsSummaryTypeDef

```python
from mypy_boto3_mq.type_defs import LogsSummaryTypeDef
```




Optional fields:
- `Audit`: `bool`
- `AuditLogGroup`: `str`
- `General`: `bool`
- `GeneralLogGroup`: `str`
- `Pending`: `"PendingLogsTypeDef"`


## LogsTypeDef

```python
from mypy_boto3_mq.type_defs import LogsTypeDef
```




Optional fields:
- `Audit`: `bool`
- `General`: `bool`


## PendingLogsTypeDef

```python
from mypy_boto3_mq.type_defs import PendingLogsTypeDef
```




Optional fields:
- `Audit`: `bool`
- `General`: `bool`


## ResponseMetadata

```python
from mypy_boto3_mq.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SanitizationWarningTypeDef

```python
from mypy_boto3_mq.type_defs import SanitizationWarningTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `ElementName`: `str`
- `Reason`: `SanitizationWarningReason`


## UserPendingChangesTypeDef

```python
from mypy_boto3_mq.type_defs import UserPendingChangesTypeDef
```




Optional fields:
- `ConsoleAccess`: `bool`
- `Groups`: `List[str]`
- `PendingChange`: `ChangeType`


## UserSummaryTypeDef

```python
from mypy_boto3_mq.type_defs import UserSummaryTypeDef
```




Optional fields:
- `PendingChange`: `ChangeType`
- `Username`: `str`


## WeeklyStartTimeTypeDef

```python
from mypy_boto3_mq.type_defs import WeeklyStartTimeTypeDef
```




Optional fields:
- `DayOfWeek`: `DayOfWeek`
- `TimeOfDay`: `str`
- `TimeZone`: `str`


## CreateBrokerResponseTypeDef

```python
from mypy_boto3_mq.type_defs import CreateBrokerResponseTypeDef
```




Optional fields:
- `BrokerArn`: `str`
- `BrokerId`: `str`


## CreateConfigurationResponseTypeDef

```python
from mypy_boto3_mq.type_defs import CreateConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AuthenticationStrategy`: `AuthenticationStrategy`
- `Created`: `datetime`
- `Id`: `str`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`


## DeleteBrokerResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DeleteBrokerResponseTypeDef
```




Optional fields:
- `BrokerId`: `str`


## DescribeBrokerEngineTypesResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DescribeBrokerEngineTypesResponseTypeDef
```




Optional fields:
- `BrokerEngineTypes`: `List["BrokerEngineTypeTypeDef"]`
- `MaxResults`: `int`
- `NextToken`: `str`


## DescribeBrokerInstanceOptionsResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DescribeBrokerInstanceOptionsResponseTypeDef
```




Optional fields:
- `BrokerInstanceOptions`: `List["BrokerInstanceOptionTypeDef"]`
- `MaxResults`: `int`
- `NextToken`: `str`


## DescribeBrokerResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DescribeBrokerResponseTypeDef
```




Optional fields:
- `AuthenticationStrategy`: `AuthenticationStrategy`
- `AutoMinorVersionUpgrade`: `bool`
- `BrokerArn`: `str`
- `BrokerId`: `str`
- `BrokerInstances`: `List["BrokerInstanceTypeDef"]`
- `BrokerName`: `str`
- `BrokerState`: `BrokerState`
- `Configurations`: `"ConfigurationsTypeDef"`
- `Created`: `datetime`
- `DeploymentMode`: `DeploymentMode`
- `EncryptionOptions`: `"EncryptionOptionsTypeDef"`
- `EngineType`: `EngineType`
- `EngineVersion`: `str`
- `HostInstanceType`: `str`
- `LdapServerMetadata`: `"LdapServerMetadataOutputTypeDef"`
- `Logs`: `"LogsSummaryTypeDef"`
- `MaintenanceWindowStartTime`: `"WeeklyStartTimeTypeDef"`
- `PendingAuthenticationStrategy`: `AuthenticationStrategy`
- `PendingEngineVersion`: `str`
- `PendingHostInstanceType`: `str`
- `PendingLdapServerMetadata`: `"LdapServerMetadataOutputTypeDef"`
- `PendingSecurityGroups`: `List[str]`
- `PubliclyAccessible`: `bool`
- `SecurityGroups`: `List[str]`
- `StorageType`: `BrokerStorageType`
- `SubnetIds`: `List[str]`
- `Tags`: `Dict[str, str]`
- `Users`: `List["UserSummaryTypeDef"]`


## DescribeConfigurationResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DescribeConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `AuthenticationStrategy`: `AuthenticationStrategy`
- `Created`: `datetime`
- `Description`: `str`
- `EngineType`: `EngineType`
- `EngineVersion`: `str`
- `Id`: `str`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`
- `Tags`: `Dict[str, str]`


## DescribeConfigurationRevisionResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DescribeConfigurationRevisionResponseTypeDef
```




Optional fields:
- `ConfigurationId`: `str`
- `Created`: `datetime`
- `Data`: `str`
- `Description`: `str`


## DescribeUserResponseTypeDef

```python
from mypy_boto3_mq.type_defs import DescribeUserResponseTypeDef
```




Optional fields:
- `BrokerId`: `str`
- `ConsoleAccess`: `bool`
- `Groups`: `List[str]`
- `Pending`: `"UserPendingChangesTypeDef"`
- `Username`: `str`


## LdapServerMetadataInputTypeDef

```python
from mypy_boto3_mq.type_defs import LdapServerMetadataInputTypeDef
```




Optional fields:
- `Hosts`: `List[str]`
- `RoleBase`: `str`
- `RoleName`: `str`
- `RoleSearchMatching`: `str`
- `RoleSearchSubtree`: `bool`
- `ServiceAccountPassword`: `str`
- `ServiceAccountUsername`: `str`
- `UserBase`: `str`
- `UserRoleName`: `str`
- `UserSearchMatching`: `str`
- `UserSearchSubtree`: `bool`


## ListBrokersResponseTypeDef

```python
from mypy_boto3_mq.type_defs import ListBrokersResponseTypeDef
```




Optional fields:
- `BrokerSummaries`: `List["BrokerSummaryTypeDef"]`
- `NextToken`: `str`


## ListConfigurationRevisionsResponseTypeDef

```python
from mypy_boto3_mq.type_defs import ListConfigurationRevisionsResponseTypeDef
```




Optional fields:
- `ConfigurationId`: `str`
- `MaxResults`: `int`
- `NextToken`: `str`
- `Revisions`: `List["ConfigurationRevisionTypeDef"]`


## ListConfigurationsResponseTypeDef

```python
from mypy_boto3_mq.type_defs import ListConfigurationsResponseTypeDef
```




Optional fields:
- `Configurations`: `List["ConfigurationTypeDef"]`
- `MaxResults`: `int`
- `NextToken`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_mq.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListUsersResponseTypeDef

```python
from mypy_boto3_mq.type_defs import ListUsersResponseTypeDef
```




Optional fields:
- `BrokerId`: `str`
- `MaxResults`: `int`
- `NextToken`: `str`
- `Users`: `List["UserSummaryTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mq.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateBrokerResponseTypeDef

```python
from mypy_boto3_mq.type_defs import UpdateBrokerResponseTypeDef
```




Optional fields:
- `AuthenticationStrategy`: `AuthenticationStrategy`
- `AutoMinorVersionUpgrade`: `bool`
- `BrokerId`: `str`
- `Configuration`: `"ConfigurationIdTypeDef"`
- `EngineVersion`: `str`
- `HostInstanceType`: `str`
- `LdapServerMetadata`: `"LdapServerMetadataOutputTypeDef"`
- `Logs`: `"LogsTypeDef"`
- `SecurityGroups`: `List[str]`


## UpdateConfigurationResponseTypeDef

```python
from mypy_boto3_mq.type_defs import UpdateConfigurationResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Created`: `datetime`
- `Id`: `str`
- `LatestRevision`: `"ConfigurationRevisionTypeDef"`
- `Name`: `str`
- `Warnings`: `List["SanitizationWarningTypeDef"]`


## UserTypeDef

```python
from mypy_boto3_mq.type_defs import UserTypeDef
```




Optional fields:
- `ConsoleAccess`: `bool`
- `Groups`: `List[str]`
- `Password`: `str`
- `Username`: `str`

