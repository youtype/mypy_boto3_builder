# Structures for boto3 SMS module

> [Index](../index.md) > [SMS](./index.md) > Structures

Auto-generated documentation for [SMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS)
type annotations stubs module [mypy_boto3_sms](https://pypi.org/project/mypy-boto3-sms/).

- [Structures for boto3 SMS module](#structures-for-boto3-sms-module)
  - [AppSummaryTypeDef](#appsummarytypedef)
  - [AppValidationConfigurationTypeDef](#appvalidationconfigurationtypedef)
  - [AppValidationOutputTypeDef](#appvalidationoutputtypedef)
  - [ConnectorTypeDef](#connectortypedef)
  - [CreateAppResponseTypeDef](#createappresponsetypedef)
  - [CreateReplicationJobResponseTypeDef](#createreplicationjobresponsetypedef)
  - [GenerateChangeSetResponseTypeDef](#generatechangesetresponsetypedef)
  - [GenerateTemplateResponseTypeDef](#generatetemplateresponsetypedef)
  - [GetAppLaunchConfigurationResponseTypeDef](#getapplaunchconfigurationresponsetypedef)
  - [GetAppReplicationConfigurationResponseTypeDef](#getappreplicationconfigurationresponsetypedef)
  - [GetAppResponseTypeDef](#getappresponsetypedef)
  - [GetAppValidationConfigurationResponseTypeDef](#getappvalidationconfigurationresponsetypedef)
  - [GetAppValidationOutputResponseTypeDef](#getappvalidationoutputresponsetypedef)
  - [GetConnectorsResponseTypeDef](#getconnectorsresponsetypedef)
  - [GetReplicationJobsResponseTypeDef](#getreplicationjobsresponsetypedef)
  - [GetReplicationRunsResponseTypeDef](#getreplicationrunsresponsetypedef)
  - [GetServersResponseTypeDef](#getserversresponsetypedef)
  - [LaunchDetailsTypeDef](#launchdetailstypedef)
  - [ListAppsResponseTypeDef](#listappsresponsetypedef)
  - [NotificationContextTypeDef](#notificationcontexttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ReplicationJobTypeDef](#replicationjobtypedef)
  - [ReplicationRunStageDetailsTypeDef](#replicationrunstagedetailstypedef)
  - [ReplicationRunTypeDef](#replicationruntypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3LocationTypeDef](#s3locationtypedef)
  - [SSMOutputTypeDef](#ssmoutputtypedef)
  - [SSMValidationParametersTypeDef](#ssmvalidationparameterstypedef)
  - [ServerGroupLaunchConfigurationTypeDef](#servergrouplaunchconfigurationtypedef)
  - [ServerGroupReplicationConfigurationTypeDef](#servergroupreplicationconfigurationtypedef)
  - [ServerGroupTypeDef](#servergrouptypedef)
  - [ServerGroupValidationConfigurationTypeDef](#servergroupvalidationconfigurationtypedef)
  - [ServerLaunchConfigurationTypeDef](#serverlaunchconfigurationtypedef)
  - [ServerReplicationConfigurationTypeDef](#serverreplicationconfigurationtypedef)
  - [ServerReplicationParametersTypeDef](#serverreplicationparameterstypedef)
  - [ServerTypeDef](#servertypedef)
  - [ServerValidationConfigurationTypeDef](#servervalidationconfigurationtypedef)
  - [ServerValidationOutputTypeDef](#servervalidationoutputtypedef)
  - [SourceTypeDef](#sourcetypedef)
  - [StartOnDemandReplicationRunResponseTypeDef](#startondemandreplicationrunresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateAppResponseTypeDef](#updateappresponsetypedef)
  - [UserDataTypeDef](#userdatatypedef)
  - [UserDataValidationParametersTypeDef](#userdatavalidationparameterstypedef)
  - [ValidationOutputTypeDef](#validationoutputtypedef)
  - [VmServerAddressTypeDef](#vmserveraddresstypedef)
  - [VmServerTypeDef](#vmservertypedef)

## AppSummaryTypeDef

```python
from mypy_boto3_sms.type_defs import AppSummaryTypeDef
```




Optional fields:
- `appId`: `str`
- `importedAppId`: `str`
- `name`: `str`
- `description`: `str`
- `status`: `AppStatus`
- `statusMessage`: `str`
- `replicationConfigurationStatus`: `AppReplicationConfigurationStatus`
- `replicationStatus`: `AppReplicationStatus`
- `replicationStatusMessage`: `str`
- `latestReplicationTime`: `datetime`
- `launchConfigurationStatus`: `AppLaunchConfigurationStatus`
- `launchStatus`: `AppLaunchStatus`
- `launchStatusMessage`: `str`
- `launchDetails`: `"LaunchDetailsTypeDef"`
- `creationTime`: `datetime`
- `lastModified`: `datetime`
- `roleName`: `str`
- `totalServerGroups`: `int`
- `totalServers`: `int`


## AppValidationConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import AppValidationConfigurationTypeDef
```




Optional fields:
- `validationId`: `str`
- `name`: `str`
- `appValidationStrategy`: `Literal['SSM']`
- `ssmValidationParameters`: `"SSMValidationParametersTypeDef"`


## AppValidationOutputTypeDef

```python
from mypy_boto3_sms.type_defs import AppValidationOutputTypeDef
```




Optional fields:
- `ssmOutput`: `"SSMOutputTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ConnectorTypeDef

```python
from mypy_boto3_sms.type_defs import ConnectorTypeDef
```




Optional fields:
- `connectorId`: `str`
- `version`: `str`
- `status`: `ConnectorStatus`
- `capabilityList`: `List[ConnectorCapability]`
- `vmManagerName`: `str`
- `vmManagerType`: `VmManagerType`
- `vmManagerId`: `str`
- `ipAddress`: `str`
- `macAddress`: `str`
- `associatedOn`: `datetime`


## CreateAppResponseTypeDef

```python
from mypy_boto3_sms.type_defs import CreateAppResponseTypeDef
```




Optional fields:
- `appSummary`: `"AppSummaryTypeDef"`
- `serverGroups`: `List["ServerGroupTypeDef"]`
- `tags`: `List["TagTypeDef"]`


## CreateReplicationJobResponseTypeDef

```python
from mypy_boto3_sms.type_defs import CreateReplicationJobResponseTypeDef
```




Optional fields:
- `replicationJobId`: `str`


## GenerateChangeSetResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GenerateChangeSetResponseTypeDef
```




Optional fields:
- `s3Location`: `"S3LocationTypeDef"`


## GenerateTemplateResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GenerateTemplateResponseTypeDef
```




Optional fields:
- `s3Location`: `"S3LocationTypeDef"`


## GetAppLaunchConfigurationResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetAppLaunchConfigurationResponseTypeDef
```




Optional fields:
- `appId`: `str`
- `roleName`: `str`
- `autoLaunch`: `bool`
- `serverGroupLaunchConfigurations`: `List["ServerGroupLaunchConfigurationTypeDef"]`


## GetAppReplicationConfigurationResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetAppReplicationConfigurationResponseTypeDef
```




Optional fields:
- `serverGroupReplicationConfigurations`: `List["ServerGroupReplicationConfigurationTypeDef"]`


## GetAppResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetAppResponseTypeDef
```




Optional fields:
- `appSummary`: `"AppSummaryTypeDef"`
- `serverGroups`: `List["ServerGroupTypeDef"]`
- `tags`: `List["TagTypeDef"]`


## GetAppValidationConfigurationResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetAppValidationConfigurationResponseTypeDef
```




Optional fields:
- `appValidationConfigurations`: `List["AppValidationConfigurationTypeDef"]`
- `serverGroupValidationConfigurations`: `List["ServerGroupValidationConfigurationTypeDef"]`


## GetAppValidationOutputResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetAppValidationOutputResponseTypeDef
```




Optional fields:
- `validationOutputList`: `List["ValidationOutputTypeDef"]`


## GetConnectorsResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetConnectorsResponseTypeDef
```




Optional fields:
- `connectorList`: `List["ConnectorTypeDef"]`
- `nextToken`: `str`


## GetReplicationJobsResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetReplicationJobsResponseTypeDef
```




Optional fields:
- `replicationJobList`: `List["ReplicationJobTypeDef"]`
- `nextToken`: `str`


## GetReplicationRunsResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetReplicationRunsResponseTypeDef
```




Optional fields:
- `replicationJob`: `"ReplicationJobTypeDef"`
- `replicationRunList`: `List["ReplicationRunTypeDef"]`
- `nextToken`: `str`


## GetServersResponseTypeDef

```python
from mypy_boto3_sms.type_defs import GetServersResponseTypeDef
```




Optional fields:
- `lastModifiedOn`: `datetime`
- `serverCatalogStatus`: `ServerCatalogStatus`
- `serverList`: `List["ServerTypeDef"]`
- `nextToken`: `str`


## LaunchDetailsTypeDef

```python
from mypy_boto3_sms.type_defs import LaunchDetailsTypeDef
```




Optional fields:
- `latestLaunchTime`: `datetime`
- `stackName`: `str`
- `stackId`: `str`


## ListAppsResponseTypeDef

```python
from mypy_boto3_sms.type_defs import ListAppsResponseTypeDef
```




Optional fields:
- `apps`: `List["AppSummaryTypeDef"]`
- `nextToken`: `str`


## NotificationContextTypeDef

```python
from mypy_boto3_sms.type_defs import NotificationContextTypeDef
```




Optional fields:
- `validationId`: `str`
- `status`: `ValidationStatus`
- `statusMessage`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sms.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ReplicationJobTypeDef

```python
from mypy_boto3_sms.type_defs import ReplicationJobTypeDef
```




Optional fields:
- `replicationJobId`: `str`
- `serverId`: `str`
- `serverType`: `Literal['VIRTUAL_MACHINE']`
- `vmServer`: `"VmServerTypeDef"`
- `seedReplicationTime`: `datetime`
- `frequency`: `int`
- `runOnce`: `bool`
- `nextReplicationRunStartTime`: `datetime`
- `licenseType`: `LicenseType`
- `roleName`: `str`
- `latestAmiId`: `str`
- `state`: `ReplicationJobState`
- `statusMessage`: `str`
- `description`: `str`
- `numberOfRecentAmisToKeep`: `int`
- `encrypted`: `bool`
- `kmsKeyId`: `str`
- `replicationRunList`: `List["ReplicationRunTypeDef"]`


## ReplicationRunStageDetailsTypeDef

```python
from mypy_boto3_sms.type_defs import ReplicationRunStageDetailsTypeDef
```




Optional fields:
- `stage`: `str`
- `stageProgress`: `str`


## ReplicationRunTypeDef

```python
from mypy_boto3_sms.type_defs import ReplicationRunTypeDef
```




Optional fields:
- `replicationRunId`: `str`
- `state`: `ReplicationRunState`
- `type`: `ReplicationRunType`
- `stageDetails`: `"ReplicationRunStageDetailsTypeDef"`
- `statusMessage`: `str`
- `amiId`: `str`
- `scheduledStartTime`: `datetime`
- `completedTime`: `datetime`
- `description`: `str`
- `encrypted`: `bool`
- `kmsKeyId`: `str`


## ResponseMetadata

```python
from mypy_boto3_sms.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3LocationTypeDef

```python
from mypy_boto3_sms.type_defs import S3LocationTypeDef
```




Optional fields:
- `bucket`: `str`
- `key`: `str`


## SSMOutputTypeDef

```python
from mypy_boto3_sms.type_defs import SSMOutputTypeDef
```




Optional fields:
- `s3Location`: `"S3LocationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SSMValidationParametersTypeDef

```python
from mypy_boto3_sms.type_defs import SSMValidationParametersTypeDef
```




Optional fields:
- `source`: `"SourceTypeDef"`
- `instanceId`: `str`
- `scriptType`: `ScriptType`
- `command`: `str`
- `executionTimeoutSeconds`: `int`
- `outputS3BucketName`: `str`


## ServerGroupLaunchConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import ServerGroupLaunchConfigurationTypeDef
```




Optional fields:
- `serverGroupId`: `str`
- `launchOrder`: `int`
- `serverLaunchConfigurations`: `List["ServerLaunchConfigurationTypeDef"]`


## ServerGroupReplicationConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import ServerGroupReplicationConfigurationTypeDef
```




Optional fields:
- `serverGroupId`: `str`
- `serverReplicationConfigurations`: `List["ServerReplicationConfigurationTypeDef"]`


## ServerGroupTypeDef

```python
from mypy_boto3_sms.type_defs import ServerGroupTypeDef
```




Optional fields:
- `serverGroupId`: `str`
- `name`: `str`
- `serverList`: `List["ServerTypeDef"]`


## ServerGroupValidationConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import ServerGroupValidationConfigurationTypeDef
```




Optional fields:
- `serverGroupId`: `str`
- `serverValidationConfigurations`: `List["ServerValidationConfigurationTypeDef"]`


## ServerLaunchConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import ServerLaunchConfigurationTypeDef
```




Optional fields:
- `server`: `"ServerTypeDef"`
- `logicalId`: `str`
- `vpc`: `str`
- `subnet`: `str`
- `securityGroup`: `str`
- `ec2KeyName`: `str`
- `userData`: `"UserDataTypeDef"`
- `instanceType`: `str`
- `associatePublicIpAddress`: `bool`
- `iamInstanceProfileName`: `str`
- `configureScript`: `"S3LocationTypeDef"`
- `configureScriptType`: `ScriptType`


## ServerReplicationConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import ServerReplicationConfigurationTypeDef
```




Optional fields:
- `server`: `"ServerTypeDef"`
- `serverReplicationParameters`: `"ServerReplicationParametersTypeDef"`


## ServerReplicationParametersTypeDef

```python
from mypy_boto3_sms.type_defs import ServerReplicationParametersTypeDef
```




Optional fields:
- `seedTime`: `datetime`
- `frequency`: `int`
- `runOnce`: `bool`
- `licenseType`: `LicenseType`
- `numberOfRecentAmisToKeep`: `int`
- `encrypted`: `bool`
- `kmsKeyId`: `str`


## ServerTypeDef

```python
from mypy_boto3_sms.type_defs import ServerTypeDef
```




Optional fields:
- `serverId`: `str`
- `serverType`: `Literal['VIRTUAL_MACHINE']`
- `vmServer`: `"VmServerTypeDef"`
- `replicationJobId`: `str`
- `replicationJobTerminated`: `bool`


## ServerValidationConfigurationTypeDef

```python
from mypy_boto3_sms.type_defs import ServerValidationConfigurationTypeDef
```




Optional fields:
- `server`: `"ServerTypeDef"`
- `validationId`: `str`
- `name`: `str`
- `serverValidationStrategy`: `Literal['USERDATA']`
- `userDataValidationParameters`: `"UserDataValidationParametersTypeDef"`


## ServerValidationOutputTypeDef

```python
from mypy_boto3_sms.type_defs import ServerValidationOutputTypeDef
```




Optional fields:
- `server`: `"ServerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## SourceTypeDef

```python
from mypy_boto3_sms.type_defs import SourceTypeDef
```




Optional fields:
- `s3Location`: `"S3LocationTypeDef"`


## StartOnDemandReplicationRunResponseTypeDef

```python
from mypy_boto3_sms.type_defs import StartOnDemandReplicationRunResponseTypeDef
```




Optional fields:
- `replicationRunId`: `str`


## TagTypeDef

```python
from mypy_boto3_sms.type_defs import TagTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## UpdateAppResponseTypeDef

```python
from mypy_boto3_sms.type_defs import UpdateAppResponseTypeDef
```




Optional fields:
- `appSummary`: `"AppSummaryTypeDef"`
- `serverGroups`: `List["ServerGroupTypeDef"]`
- `tags`: `List["TagTypeDef"]`


## UserDataTypeDef

```python
from mypy_boto3_sms.type_defs import UserDataTypeDef
```




Optional fields:
- `s3Location`: `"S3LocationTypeDef"`


## UserDataValidationParametersTypeDef

```python
from mypy_boto3_sms.type_defs import UserDataValidationParametersTypeDef
```




Optional fields:
- `source`: `"SourceTypeDef"`
- `scriptType`: `ScriptType`


## ValidationOutputTypeDef

```python
from mypy_boto3_sms.type_defs import ValidationOutputTypeDef
```




Optional fields:
- `validationId`: `str`
- `name`: `str`
- `status`: `ValidationStatus`
- `statusMessage`: `str`
- `latestValidationTime`: `datetime`
- `appValidationOutput`: `"AppValidationOutputTypeDef"`
- `serverValidationOutput`: `"ServerValidationOutputTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## VmServerAddressTypeDef

```python
from mypy_boto3_sms.type_defs import VmServerAddressTypeDef
```




Optional fields:
- `vmManagerId`: `str`
- `vmId`: `str`


## VmServerTypeDef

```python
from mypy_boto3_sms.type_defs import VmServerTypeDef
```




Optional fields:
- `vmServerAddress`: `"VmServerAddressTypeDef"`
- `vmName`: `str`
- `vmManagerName`: `str`
- `vmManagerType`: `VmManagerType`
- `vmPath`: `str`

