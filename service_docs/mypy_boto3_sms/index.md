# Type annotations for boto3 SMS module

> [Index](../index.md) > SMS

Auto-generated documentation for [SMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS)
type annotations stubs module [mypy_boto3_sms](https://pypi.org/project/mypy-boto3-sms/).

```bash
pip install mypy-boto3-sms
```

- [Type annotations for boto3 SMS module](#type-annotations-for-boto3-sms-module)
  - [SMSClient](#smsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SMSClient

Type annotations for  `boto3.client("sms")` as [SMSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sms.client import SMSClient
```


SMSClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_app](./client.md#create-app)
- [create_replication_job](./client.md#create-replication-job)
- [delete_app](./client.md#delete-app)
- [delete_app_launch_configuration](./client.md#delete-app-launch-configuration)
- [delete_app_replication_configuration](./client.md#delete-app-replication-configuration)
- [delete_app_validation_configuration](./client.md#delete-app-validation-configuration)
- [delete_replication_job](./client.md#delete-replication-job)
- [delete_server_catalog](./client.md#delete-server-catalog)
- [disassociate_connector](./client.md#disassociate-connector)
- [generate_change_set](./client.md#generate-change-set)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [generate_template](./client.md#generate-template)
- [get_app](./client.md#get-app)
- [get_app_launch_configuration](./client.md#get-app-launch-configuration)
- [get_app_replication_configuration](./client.md#get-app-replication-configuration)
- [get_app_validation_configuration](./client.md#get-app-validation-configuration)
- [get_app_validation_output](./client.md#get-app-validation-output)
- [get_connectors](./client.md#get-connectors)
- [get_paginator](./client.md#get-paginator)
- [get_replication_jobs](./client.md#get-replication-jobs)
- [get_replication_runs](./client.md#get-replication-runs)
- [get_servers](./client.md#get-servers)
- [import_app_catalog](./client.md#import-app-catalog)
- [import_server_catalog](./client.md#import-server-catalog)
- [launch_app](./client.md#launch-app)
- [list_apps](./client.md#list-apps)
- [notify_app_validation_output](./client.md#notify-app-validation-output)
- [put_app_launch_configuration](./client.md#put-app-launch-configuration)
- [put_app_replication_configuration](./client.md#put-app-replication-configuration)
- [put_app_validation_configuration](./client.md#put-app-validation-configuration)
- [start_app_replication](./client.md#start-app-replication)
- [start_on_demand_app_replication](./client.md#start-on-demand-app-replication)
- [start_on_demand_replication_run](./client.md#start-on-demand-replication-run)
- [stop_app_replication](./client.md#stop-app-replication)
- [terminate_app](./client.md#terminate-app)
- [update_app](./client.md#update-app)
- [update_replication_job](./client.md#update-replication-job)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DryRunOperationException](./client.md#dryrunoperationexception)
- [InternalError](./client.md#internalerror)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [MissingRequiredParameterException](./client.md#missingrequiredparameterexception)
- [NoConnectorsAvailableException](./client.md#noconnectorsavailableexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [ReplicationJobAlreadyExistsException](./client.md#replicationjobalreadyexistsexception)
- [ReplicationJobNotFoundException](./client.md#replicationjobnotfoundexception)
- [ReplicationRunLimitExceededException](./client.md#replicationrunlimitexceededexception)
- [ServerCannotBeReplicatedException](./client.md#servercannotbereplicatedexception)
- [TemporarilyUnavailableException](./client.md#temporarilyunavailableexception)
- [UnauthorizedOperationException](./client.md#unauthorizedoperationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sms").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sms.paginators import GetConnectorsPaginator, ...
```

- [GetConnectorsPaginator](./paginators.md#getconnectorspaginator)
- [GetReplicationJobsPaginator](./paginators.md#getreplicationjobspaginator)
- [GetReplicationRunsPaginator](./paginators.md#getreplicationrunspaginator)
- [GetServersPaginator](./paginators.md#getserverspaginator)
- [ListAppsPaginator](./paginators.md#listappspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sms.literals import AppLaunchConfigurationStatus, ...
```

- [AppLaunchConfigurationStatus](./literals.md#applaunchconfigurationstatus)
- [AppLaunchStatus](./literals.md#applaunchstatus)
- [AppReplicationConfigurationStatus](./literals.md#appreplicationconfigurationstatus)
- [AppReplicationStatus](./literals.md#appreplicationstatus)
- [AppStatus](./literals.md#appstatus)
- [AppValidationStrategy](./literals.md#appvalidationstrategy)
- [ConnectorCapability](./literals.md#connectorcapability)
- [ConnectorStatus](./literals.md#connectorstatus)
- [GetConnectorsPaginatorName](./literals.md#getconnectorspaginatorname)
- [GetReplicationJobsPaginatorName](./literals.md#getreplicationjobspaginatorname)
- [GetReplicationRunsPaginatorName](./literals.md#getreplicationrunspaginatorname)
- [GetServersPaginatorName](./literals.md#getserverspaginatorname)
- [LicenseType](./literals.md#licensetype)
- [ListAppsPaginatorName](./literals.md#listappspaginatorname)
- [OutputFormat](./literals.md#outputformat)
- [ReplicationJobState](./literals.md#replicationjobstate)
- [ReplicationRunState](./literals.md#replicationrunstate)
- [ReplicationRunType](./literals.md#replicationruntype)
- [ScriptType](./literals.md#scripttype)
- [ServerCatalogStatus](./literals.md#servercatalogstatus)
- [ServerType](./literals.md#servertype)
- [ServerValidationStrategy](./literals.md#servervalidationstrategy)
- [ValidationStatus](./literals.md#validationstatus)
- [VmManagerType](./literals.md#vmmanagertype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sms.type_defs import AppSummaryTypeDef, ...
```

- [AppSummaryTypeDef](./type_defs.md#appsummarytypedef)
- [AppValidationConfigurationTypeDef](./type_defs.md#appvalidationconfigurationtypedef)
- [AppValidationOutputTypeDef](./type_defs.md#appvalidationoutputtypedef)
- [ConnectorTypeDef](./type_defs.md#connectortypedef)
- [CreateAppResponseTypeDef](./type_defs.md#createappresponsetypedef)
- [CreateReplicationJobResponseTypeDef](./type_defs.md#createreplicationjobresponsetypedef)
- [GenerateChangeSetResponseTypeDef](./type_defs.md#generatechangesetresponsetypedef)
- [GenerateTemplateResponseTypeDef](./type_defs.md#generatetemplateresponsetypedef)
- [GetAppLaunchConfigurationResponseTypeDef](./type_defs.md#getapplaunchconfigurationresponsetypedef)
- [GetAppReplicationConfigurationResponseTypeDef](./type_defs.md#getappreplicationconfigurationresponsetypedef)
- [GetAppResponseTypeDef](./type_defs.md#getappresponsetypedef)
- [GetAppValidationConfigurationResponseTypeDef](./type_defs.md#getappvalidationconfigurationresponsetypedef)
- [GetAppValidationOutputResponseTypeDef](./type_defs.md#getappvalidationoutputresponsetypedef)
- [GetConnectorsResponseTypeDef](./type_defs.md#getconnectorsresponsetypedef)
- [GetReplicationJobsResponseTypeDef](./type_defs.md#getreplicationjobsresponsetypedef)
- [GetReplicationRunsResponseTypeDef](./type_defs.md#getreplicationrunsresponsetypedef)
- [GetServersResponseTypeDef](./type_defs.md#getserversresponsetypedef)
- [LaunchDetailsTypeDef](./type_defs.md#launchdetailstypedef)
- [ListAppsResponseTypeDef](./type_defs.md#listappsresponsetypedef)
- [NotificationContextTypeDef](./type_defs.md#notificationcontexttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ReplicationJobTypeDef](./type_defs.md#replicationjobtypedef)
- [ReplicationRunStageDetailsTypeDef](./type_defs.md#replicationrunstagedetailstypedef)
- [ReplicationRunTypeDef](./type_defs.md#replicationruntypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [SSMOutputTypeDef](./type_defs.md#ssmoutputtypedef)
- [SSMValidationParametersTypeDef](./type_defs.md#ssmvalidationparameterstypedef)
- [ServerGroupLaunchConfigurationTypeDef](./type_defs.md#servergrouplaunchconfigurationtypedef)
- [ServerGroupReplicationConfigurationTypeDef](./type_defs.md#servergroupreplicationconfigurationtypedef)
- [ServerGroupTypeDef](./type_defs.md#servergrouptypedef)
- [ServerGroupValidationConfigurationTypeDef](./type_defs.md#servergroupvalidationconfigurationtypedef)
- [ServerLaunchConfigurationTypeDef](./type_defs.md#serverlaunchconfigurationtypedef)
- [ServerReplicationConfigurationTypeDef](./type_defs.md#serverreplicationconfigurationtypedef)
- [ServerReplicationParametersTypeDef](./type_defs.md#serverreplicationparameterstypedef)
- [ServerTypeDef](./type_defs.md#servertypedef)
- [ServerValidationConfigurationTypeDef](./type_defs.md#servervalidationconfigurationtypedef)
- [ServerValidationOutputTypeDef](./type_defs.md#servervalidationoutputtypedef)
- [SourceTypeDef](./type_defs.md#sourcetypedef)
- [StartOnDemandReplicationRunResponseTypeDef](./type_defs.md#startondemandreplicationrunresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateAppResponseTypeDef](./type_defs.md#updateappresponsetypedef)
- [UserDataTypeDef](./type_defs.md#userdatatypedef)
- [UserDataValidationParametersTypeDef](./type_defs.md#userdatavalidationparameterstypedef)
- [ValidationOutputTypeDef](./type_defs.md#validationoutputtypedef)
- [VmServerAddressTypeDef](./type_defs.md#vmserveraddresstypedef)
- [VmServerTypeDef](./type_defs.md#vmservertypedef)
