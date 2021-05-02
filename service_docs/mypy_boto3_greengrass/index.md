# Type annotations for boto3 Greengrass module

> [Index](../index.md) > Greengrass

Auto-generated documentation for [Greengrass](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass)
type annotations stubs module [mypy_boto3_greengrass](https://pypi.org/project/mypy-boto3-greengrass/).

```bash
pip install mypy-boto3-greengrass
```

- [Type annotations for boto3 Greengrass module](#type-annotations-for-boto3-greengrass-module)
  - [GreengrassClient](#greengrassclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## GreengrassClient

Type annotations for  `boto3.client("greengrass")` as [GreengrassClient](./client.md)

Can be used directly:

```python
from mypy_boto3_greengrass.client import GreengrassClient
```


GreengrassClient [exceptions](./client.md#exceptions)



### Methods
- [associate_role_to_group](./client.md#associate-role-to-group)
- [associate_service_role_to_account](./client.md#associate-service-role-to-account)
- [can_paginate](./client.md#can-paginate)
- [create_connector_definition](./client.md#create-connector-definition)
- [create_connector_definition_version](./client.md#create-connector-definition-version)
- [create_core_definition](./client.md#create-core-definition)
- [create_core_definition_version](./client.md#create-core-definition-version)
- [create_deployment](./client.md#create-deployment)
- [create_device_definition](./client.md#create-device-definition)
- [create_device_definition_version](./client.md#create-device-definition-version)
- [create_function_definition](./client.md#create-function-definition)
- [create_function_definition_version](./client.md#create-function-definition-version)
- [create_group](./client.md#create-group)
- [create_group_certificate_authority](./client.md#create-group-certificate-authority)
- [create_group_version](./client.md#create-group-version)
- [create_logger_definition](./client.md#create-logger-definition)
- [create_logger_definition_version](./client.md#create-logger-definition-version)
- [create_resource_definition](./client.md#create-resource-definition)
- [create_resource_definition_version](./client.md#create-resource-definition-version)
- [create_software_update_job](./client.md#create-software-update-job)
- [create_subscription_definition](./client.md#create-subscription-definition)
- [create_subscription_definition_version](./client.md#create-subscription-definition-version)
- [delete_connector_definition](./client.md#delete-connector-definition)
- [delete_core_definition](./client.md#delete-core-definition)
- [delete_device_definition](./client.md#delete-device-definition)
- [delete_function_definition](./client.md#delete-function-definition)
- [delete_group](./client.md#delete-group)
- [delete_logger_definition](./client.md#delete-logger-definition)
- [delete_resource_definition](./client.md#delete-resource-definition)
- [delete_subscription_definition](./client.md#delete-subscription-definition)
- [disassociate_role_from_group](./client.md#disassociate-role-from-group)
- [disassociate_service_role_from_account](./client.md#disassociate-service-role-from-account)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_associated_role](./client.md#get-associated-role)
- [get_bulk_deployment_status](./client.md#get-bulk-deployment-status)
- [get_connectivity_info](./client.md#get-connectivity-info)
- [get_connector_definition](./client.md#get-connector-definition)
- [get_connector_definition_version](./client.md#get-connector-definition-version)
- [get_core_definition](./client.md#get-core-definition)
- [get_core_definition_version](./client.md#get-core-definition-version)
- [get_deployment_status](./client.md#get-deployment-status)
- [get_device_definition](./client.md#get-device-definition)
- [get_device_definition_version](./client.md#get-device-definition-version)
- [get_function_definition](./client.md#get-function-definition)
- [get_function_definition_version](./client.md#get-function-definition-version)
- [get_group](./client.md#get-group)
- [get_group_certificate_authority](./client.md#get-group-certificate-authority)
- [get_group_certificate_configuration](./client.md#get-group-certificate-configuration)
- [get_group_version](./client.md#get-group-version)
- [get_logger_definition](./client.md#get-logger-definition)
- [get_logger_definition_version](./client.md#get-logger-definition-version)
- [get_paginator](./client.md#get-paginator)
- [get_resource_definition](./client.md#get-resource-definition)
- [get_resource_definition_version](./client.md#get-resource-definition-version)
- [get_service_role_for_account](./client.md#get-service-role-for-account)
- [get_subscription_definition](./client.md#get-subscription-definition)
- [get_subscription_definition_version](./client.md#get-subscription-definition-version)
- [get_thing_runtime_configuration](./client.md#get-thing-runtime-configuration)
- [list_bulk_deployment_detailed_reports](./client.md#list-bulk-deployment-detailed-reports)
- [list_bulk_deployments](./client.md#list-bulk-deployments)
- [list_connector_definition_versions](./client.md#list-connector-definition-versions)
- [list_connector_definitions](./client.md#list-connector-definitions)
- [list_core_definition_versions](./client.md#list-core-definition-versions)
- [list_core_definitions](./client.md#list-core-definitions)
- [list_deployments](./client.md#list-deployments)
- [list_device_definition_versions](./client.md#list-device-definition-versions)
- [list_device_definitions](./client.md#list-device-definitions)
- [list_function_definition_versions](./client.md#list-function-definition-versions)
- [list_function_definitions](./client.md#list-function-definitions)
- [list_group_certificate_authorities](./client.md#list-group-certificate-authorities)
- [list_group_versions](./client.md#list-group-versions)
- [list_groups](./client.md#list-groups)
- [list_logger_definition_versions](./client.md#list-logger-definition-versions)
- [list_logger_definitions](./client.md#list-logger-definitions)
- [list_resource_definition_versions](./client.md#list-resource-definition-versions)
- [list_resource_definitions](./client.md#list-resource-definitions)
- [list_subscription_definition_versions](./client.md#list-subscription-definition-versions)
- [list_subscription_definitions](./client.md#list-subscription-definitions)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [reset_deployments](./client.md#reset-deployments)
- [start_bulk_deployment](./client.md#start-bulk-deployment)
- [stop_bulk_deployment](./client.md#stop-bulk-deployment)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_connectivity_info](./client.md#update-connectivity-info)
- [update_connector_definition](./client.md#update-connector-definition)
- [update_core_definition](./client.md#update-core-definition)
- [update_device_definition](./client.md#update-device-definition)
- [update_function_definition](./client.md#update-function-definition)
- [update_group](./client.md#update-group)
- [update_group_certificate_configuration](./client.md#update-group-certificate-configuration)
- [update_logger_definition](./client.md#update-logger-definition)
- [update_resource_definition](./client.md#update-resource-definition)
- [update_subscription_definition](./client.md#update-subscription-definition)
- [update_thing_runtime_configuration](./client.md#update-thing-runtime-configuration)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalServerErrorException](./client.md#internalservererrorexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("greengrass").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListBulkDeploymentDetailedReportsPaginator, ...
```

- [ListBulkDeploymentDetailedReportsPaginator](./paginators.md#listbulkdeploymentdetailedreportspaginator)
- [ListBulkDeploymentsPaginator](./paginators.md#listbulkdeploymentspaginator)
- [ListConnectorDefinitionVersionsPaginator](./paginators.md#listconnectordefinitionversionspaginator)
- [ListConnectorDefinitionsPaginator](./paginators.md#listconnectordefinitionspaginator)
- [ListCoreDefinitionVersionsPaginator](./paginators.md#listcoredefinitionversionspaginator)
- [ListCoreDefinitionsPaginator](./paginators.md#listcoredefinitionspaginator)
- [ListDeploymentsPaginator](./paginators.md#listdeploymentspaginator)
- [ListDeviceDefinitionVersionsPaginator](./paginators.md#listdevicedefinitionversionspaginator)
- [ListDeviceDefinitionsPaginator](./paginators.md#listdevicedefinitionspaginator)
- [ListFunctionDefinitionVersionsPaginator](./paginators.md#listfunctiondefinitionversionspaginator)
- [ListFunctionDefinitionsPaginator](./paginators.md#listfunctiondefinitionspaginator)
- [ListGroupVersionsPaginator](./paginators.md#listgroupversionspaginator)
- [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- [ListLoggerDefinitionVersionsPaginator](./paginators.md#listloggerdefinitionversionspaginator)
- [ListLoggerDefinitionsPaginator](./paginators.md#listloggerdefinitionspaginator)
- [ListResourceDefinitionVersionsPaginator](./paginators.md#listresourcedefinitionversionspaginator)
- [ListResourceDefinitionsPaginator](./paginators.md#listresourcedefinitionspaginator)
- [ListSubscriptionDefinitionVersionsPaginator](./paginators.md#listsubscriptiondefinitionversionspaginator)
- [ListSubscriptionDefinitionsPaginator](./paginators.md#listsubscriptiondefinitionspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_greengrass.literals import BulkDeploymentStatus, ...
```

- [BulkDeploymentStatus](./literals.md#bulkdeploymentstatus)
- [ConfigurationSyncStatus](./literals.md#configurationsyncstatus)
- [DeploymentType](./literals.md#deploymenttype)
- [EncodingType](./literals.md#encodingtype)
- [FunctionIsolationMode](./literals.md#functionisolationmode)
- [ListBulkDeploymentDetailedReportsPaginatorName](./literals.md#listbulkdeploymentdetailedreportspaginatorname)
- [ListBulkDeploymentsPaginatorName](./literals.md#listbulkdeploymentspaginatorname)
- [ListConnectorDefinitionVersionsPaginatorName](./literals.md#listconnectordefinitionversionspaginatorname)
- [ListConnectorDefinitionsPaginatorName](./literals.md#listconnectordefinitionspaginatorname)
- [ListCoreDefinitionVersionsPaginatorName](./literals.md#listcoredefinitionversionspaginatorname)
- [ListCoreDefinitionsPaginatorName](./literals.md#listcoredefinitionspaginatorname)
- [ListDeploymentsPaginatorName](./literals.md#listdeploymentspaginatorname)
- [ListDeviceDefinitionVersionsPaginatorName](./literals.md#listdevicedefinitionversionspaginatorname)
- [ListDeviceDefinitionsPaginatorName](./literals.md#listdevicedefinitionspaginatorname)
- [ListFunctionDefinitionVersionsPaginatorName](./literals.md#listfunctiondefinitionversionspaginatorname)
- [ListFunctionDefinitionsPaginatorName](./literals.md#listfunctiondefinitionspaginatorname)
- [ListGroupVersionsPaginatorName](./literals.md#listgroupversionspaginatorname)
- [ListGroupsPaginatorName](./literals.md#listgroupspaginatorname)
- [ListLoggerDefinitionVersionsPaginatorName](./literals.md#listloggerdefinitionversionspaginatorname)
- [ListLoggerDefinitionsPaginatorName](./literals.md#listloggerdefinitionspaginatorname)
- [ListResourceDefinitionVersionsPaginatorName](./literals.md#listresourcedefinitionversionspaginatorname)
- [ListResourceDefinitionsPaginatorName](./literals.md#listresourcedefinitionspaginatorname)
- [ListSubscriptionDefinitionVersionsPaginatorName](./literals.md#listsubscriptiondefinitionversionspaginatorname)
- [ListSubscriptionDefinitionsPaginatorName](./literals.md#listsubscriptiondefinitionspaginatorname)
- [LoggerComponent](./literals.md#loggercomponent)
- [LoggerLevel](./literals.md#loggerlevel)
- [LoggerType](./literals.md#loggertype)
- [Permission](./literals.md#permission)
- [SoftwareToUpdate](./literals.md#softwaretoupdate)
- [Telemetry](./literals.md#telemetry)
- [UpdateAgentLogLevel](./literals.md#updateagentloglevel)
- [UpdateTargetsArchitecture](./literals.md#updatetargetsarchitecture)
- [UpdateTargetsOperatingSystem](./literals.md#updatetargetsoperatingsystem)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_greengrass.type_defs import AssociateRoleToGroupResponseTypeDef, ...
```

- [AssociateRoleToGroupResponseTypeDef](./type_defs.md#associateroletogroupresponsetypedef)
- [AssociateServiceRoleToAccountResponseTypeDef](./type_defs.md#associateserviceroletoaccountresponsetypedef)
- [BulkDeploymentMetricsTypeDef](./type_defs.md#bulkdeploymentmetricstypedef)
- [BulkDeploymentResultTypeDef](./type_defs.md#bulkdeploymentresulttypedef)
- [BulkDeploymentTypeDef](./type_defs.md#bulkdeploymenttypedef)
- [ConnectivityInfoTypeDef](./type_defs.md#connectivityinfotypedef)
- [ConnectorDefinitionVersionTypeDef](./type_defs.md#connectordefinitionversiontypedef)
- [ConnectorTypeDef](./type_defs.md#connectortypedef)
- [CoreDefinitionVersionTypeDef](./type_defs.md#coredefinitionversiontypedef)
- [CoreTypeDef](./type_defs.md#coretypedef)
- [CreateConnectorDefinitionResponseTypeDef](./type_defs.md#createconnectordefinitionresponsetypedef)
- [CreateConnectorDefinitionVersionResponseTypeDef](./type_defs.md#createconnectordefinitionversionresponsetypedef)
- [CreateCoreDefinitionResponseTypeDef](./type_defs.md#createcoredefinitionresponsetypedef)
- [CreateCoreDefinitionVersionResponseTypeDef](./type_defs.md#createcoredefinitionversionresponsetypedef)
- [CreateDeploymentResponseTypeDef](./type_defs.md#createdeploymentresponsetypedef)
- [CreateDeviceDefinitionResponseTypeDef](./type_defs.md#createdevicedefinitionresponsetypedef)
- [CreateDeviceDefinitionVersionResponseTypeDef](./type_defs.md#createdevicedefinitionversionresponsetypedef)
- [CreateFunctionDefinitionResponseTypeDef](./type_defs.md#createfunctiondefinitionresponsetypedef)
- [CreateFunctionDefinitionVersionResponseTypeDef](./type_defs.md#createfunctiondefinitionversionresponsetypedef)
- [CreateGroupCertificateAuthorityResponseTypeDef](./type_defs.md#creategroupcertificateauthorityresponsetypedef)
- [CreateGroupResponseTypeDef](./type_defs.md#creategroupresponsetypedef)
- [CreateGroupVersionResponseTypeDef](./type_defs.md#creategroupversionresponsetypedef)
- [CreateLoggerDefinitionResponseTypeDef](./type_defs.md#createloggerdefinitionresponsetypedef)
- [CreateLoggerDefinitionVersionResponseTypeDef](./type_defs.md#createloggerdefinitionversionresponsetypedef)
- [CreateResourceDefinitionResponseTypeDef](./type_defs.md#createresourcedefinitionresponsetypedef)
- [CreateResourceDefinitionVersionResponseTypeDef](./type_defs.md#createresourcedefinitionversionresponsetypedef)
- [CreateSoftwareUpdateJobResponseTypeDef](./type_defs.md#createsoftwareupdatejobresponsetypedef)
- [CreateSubscriptionDefinitionResponseTypeDef](./type_defs.md#createsubscriptiondefinitionresponsetypedef)
- [CreateSubscriptionDefinitionVersionResponseTypeDef](./type_defs.md#createsubscriptiondefinitionversionresponsetypedef)
- [DefinitionInformationTypeDef](./type_defs.md#definitioninformationtypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DeviceDefinitionVersionTypeDef](./type_defs.md#devicedefinitionversiontypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [DisassociateRoleFromGroupResponseTypeDef](./type_defs.md#disassociaterolefromgroupresponsetypedef)
- [DisassociateServiceRoleFromAccountResponseTypeDef](./type_defs.md#disassociateservicerolefromaccountresponsetypedef)
- [ErrorDetailTypeDef](./type_defs.md#errordetailtypedef)
- [FunctionConfigurationEnvironmentTypeDef](./type_defs.md#functionconfigurationenvironmenttypedef)
- [FunctionConfigurationTypeDef](./type_defs.md#functionconfigurationtypedef)
- [FunctionDefaultConfigTypeDef](./type_defs.md#functiondefaultconfigtypedef)
- [FunctionDefaultExecutionConfigTypeDef](./type_defs.md#functiondefaultexecutionconfigtypedef)
- [FunctionDefinitionVersionTypeDef](./type_defs.md#functiondefinitionversiontypedef)
- [FunctionExecutionConfigTypeDef](./type_defs.md#functionexecutionconfigtypedef)
- [FunctionRunAsConfigTypeDef](./type_defs.md#functionrunasconfigtypedef)
- [FunctionTypeDef](./type_defs.md#functiontypedef)
- [GetAssociatedRoleResponseTypeDef](./type_defs.md#getassociatedroleresponsetypedef)
- [GetBulkDeploymentStatusResponseTypeDef](./type_defs.md#getbulkdeploymentstatusresponsetypedef)
- [GetConnectivityInfoResponseTypeDef](./type_defs.md#getconnectivityinforesponsetypedef)
- [GetConnectorDefinitionResponseTypeDef](./type_defs.md#getconnectordefinitionresponsetypedef)
- [GetConnectorDefinitionVersionResponseTypeDef](./type_defs.md#getconnectordefinitionversionresponsetypedef)
- [GetCoreDefinitionResponseTypeDef](./type_defs.md#getcoredefinitionresponsetypedef)
- [GetCoreDefinitionVersionResponseTypeDef](./type_defs.md#getcoredefinitionversionresponsetypedef)
- [GetDeploymentStatusResponseTypeDef](./type_defs.md#getdeploymentstatusresponsetypedef)
- [GetDeviceDefinitionResponseTypeDef](./type_defs.md#getdevicedefinitionresponsetypedef)
- [GetDeviceDefinitionVersionResponseTypeDef](./type_defs.md#getdevicedefinitionversionresponsetypedef)
- [GetFunctionDefinitionResponseTypeDef](./type_defs.md#getfunctiondefinitionresponsetypedef)
- [GetFunctionDefinitionVersionResponseTypeDef](./type_defs.md#getfunctiondefinitionversionresponsetypedef)
- [GetGroupCertificateAuthorityResponseTypeDef](./type_defs.md#getgroupcertificateauthorityresponsetypedef)
- [GetGroupCertificateConfigurationResponseTypeDef](./type_defs.md#getgroupcertificateconfigurationresponsetypedef)
- [GetGroupResponseTypeDef](./type_defs.md#getgroupresponsetypedef)
- [GetGroupVersionResponseTypeDef](./type_defs.md#getgroupversionresponsetypedef)
- [GetLoggerDefinitionResponseTypeDef](./type_defs.md#getloggerdefinitionresponsetypedef)
- [GetLoggerDefinitionVersionResponseTypeDef](./type_defs.md#getloggerdefinitionversionresponsetypedef)
- [GetResourceDefinitionResponseTypeDef](./type_defs.md#getresourcedefinitionresponsetypedef)
- [GetResourceDefinitionVersionResponseTypeDef](./type_defs.md#getresourcedefinitionversionresponsetypedef)
- [GetServiceRoleForAccountResponseTypeDef](./type_defs.md#getserviceroleforaccountresponsetypedef)
- [GetSubscriptionDefinitionResponseTypeDef](./type_defs.md#getsubscriptiondefinitionresponsetypedef)
- [GetSubscriptionDefinitionVersionResponseTypeDef](./type_defs.md#getsubscriptiondefinitionversionresponsetypedef)
- [GetThingRuntimeConfigurationResponseTypeDef](./type_defs.md#getthingruntimeconfigurationresponsetypedef)
- [GroupCertificateAuthorityPropertiesTypeDef](./type_defs.md#groupcertificateauthoritypropertiestypedef)
- [GroupInformationTypeDef](./type_defs.md#groupinformationtypedef)
- [GroupOwnerSettingTypeDef](./type_defs.md#groupownersettingtypedef)
- [GroupVersionTypeDef](./type_defs.md#groupversiontypedef)
- [ListBulkDeploymentDetailedReportsResponseTypeDef](./type_defs.md#listbulkdeploymentdetailedreportsresponsetypedef)
- [ListBulkDeploymentsResponseTypeDef](./type_defs.md#listbulkdeploymentsresponsetypedef)
- [ListConnectorDefinitionVersionsResponseTypeDef](./type_defs.md#listconnectordefinitionversionsresponsetypedef)
- [ListConnectorDefinitionsResponseTypeDef](./type_defs.md#listconnectordefinitionsresponsetypedef)
- [ListCoreDefinitionVersionsResponseTypeDef](./type_defs.md#listcoredefinitionversionsresponsetypedef)
- [ListCoreDefinitionsResponseTypeDef](./type_defs.md#listcoredefinitionsresponsetypedef)
- [ListDeploymentsResponseTypeDef](./type_defs.md#listdeploymentsresponsetypedef)
- [ListDeviceDefinitionVersionsResponseTypeDef](./type_defs.md#listdevicedefinitionversionsresponsetypedef)
- [ListDeviceDefinitionsResponseTypeDef](./type_defs.md#listdevicedefinitionsresponsetypedef)
- [ListFunctionDefinitionVersionsResponseTypeDef](./type_defs.md#listfunctiondefinitionversionsresponsetypedef)
- [ListFunctionDefinitionsResponseTypeDef](./type_defs.md#listfunctiondefinitionsresponsetypedef)
- [ListGroupCertificateAuthoritiesResponseTypeDef](./type_defs.md#listgroupcertificateauthoritiesresponsetypedef)
- [ListGroupVersionsResponseTypeDef](./type_defs.md#listgroupversionsresponsetypedef)
- [ListGroupsResponseTypeDef](./type_defs.md#listgroupsresponsetypedef)
- [ListLoggerDefinitionVersionsResponseTypeDef](./type_defs.md#listloggerdefinitionversionsresponsetypedef)
- [ListLoggerDefinitionsResponseTypeDef](./type_defs.md#listloggerdefinitionsresponsetypedef)
- [ListResourceDefinitionVersionsResponseTypeDef](./type_defs.md#listresourcedefinitionversionsresponsetypedef)
- [ListResourceDefinitionsResponseTypeDef](./type_defs.md#listresourcedefinitionsresponsetypedef)
- [ListSubscriptionDefinitionVersionsResponseTypeDef](./type_defs.md#listsubscriptiondefinitionversionsresponsetypedef)
- [ListSubscriptionDefinitionsResponseTypeDef](./type_defs.md#listsubscriptiondefinitionsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [LocalDeviceResourceDataTypeDef](./type_defs.md#localdeviceresourcedatatypedef)
- [LocalVolumeResourceDataTypeDef](./type_defs.md#localvolumeresourcedatatypedef)
- [LoggerDefinitionVersionTypeDef](./type_defs.md#loggerdefinitionversiontypedef)
- [LoggerTypeDef](./type_defs.md#loggertypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResetDeploymentsResponseTypeDef](./type_defs.md#resetdeploymentsresponsetypedef)
- [ResourceAccessPolicyTypeDef](./type_defs.md#resourceaccesspolicytypedef)
- [ResourceDataContainerTypeDef](./type_defs.md#resourcedatacontainertypedef)
- [ResourceDefinitionVersionTypeDef](./type_defs.md#resourcedefinitionversiontypedef)
- [ResourceDownloadOwnerSettingTypeDef](./type_defs.md#resourcedownloadownersettingtypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [RuntimeConfigurationTypeDef](./type_defs.md#runtimeconfigurationtypedef)
- [S3MachineLearningModelResourceDataTypeDef](./type_defs.md#s3machinelearningmodelresourcedatatypedef)
- [SageMakerMachineLearningModelResourceDataTypeDef](./type_defs.md#sagemakermachinelearningmodelresourcedatatypedef)
- [SecretsManagerSecretResourceDataTypeDef](./type_defs.md#secretsmanagersecretresourcedatatypedef)
- [StartBulkDeploymentResponseTypeDef](./type_defs.md#startbulkdeploymentresponsetypedef)
- [SubscriptionDefinitionVersionTypeDef](./type_defs.md#subscriptiondefinitionversiontypedef)
- [SubscriptionTypeDef](./type_defs.md#subscriptiontypedef)
- [TelemetryConfigurationTypeDef](./type_defs.md#telemetryconfigurationtypedef)
- [TelemetryConfigurationUpdateTypeDef](./type_defs.md#telemetryconfigurationupdatetypedef)
- [UpdateConnectivityInfoResponseTypeDef](./type_defs.md#updateconnectivityinforesponsetypedef)
- [UpdateGroupCertificateConfigurationResponseTypeDef](./type_defs.md#updategroupcertificateconfigurationresponsetypedef)
- [VersionInformationTypeDef](./type_defs.md#versioninformationtypedef)
