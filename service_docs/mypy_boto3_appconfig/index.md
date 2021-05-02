# Type annotations for boto3 AppConfig module

> [Index](../index.md) > AppConfig

Auto-generated documentation for [AppConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig)
type annotations stubs module [mypy_boto3_appconfig](https://pypi.org/project/mypy-boto3-appconfig/).

```bash
pip install mypy-boto3-appconfig
```

- [Type annotations for boto3 AppConfig module](#type-annotations-for-boto3-appconfig-module)
  - [AppConfigClient](#appconfigclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## AppConfigClient

Type annotations for  `boto3.client("appconfig")` as [AppConfigClient](./client.md)

Can be used directly:

```python
from mypy_boto3_appconfig.client import AppConfigClient
```


AppConfigClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [create_configuration_profile](./client.md#create-configuration-profile)
- [create_deployment_strategy](./client.md#create-deployment-strategy)
- [create_environment](./client.md#create-environment)
- [create_hosted_configuration_version](./client.md#create-hosted-configuration-version)
- [delete_application](./client.md#delete-application)
- [delete_configuration_profile](./client.md#delete-configuration-profile)
- [delete_deployment_strategy](./client.md#delete-deployment-strategy)
- [delete_environment](./client.md#delete-environment)
- [delete_hosted_configuration_version](./client.md#delete-hosted-configuration-version)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_application](./client.md#get-application)
- [get_configuration](./client.md#get-configuration)
- [get_configuration_profile](./client.md#get-configuration-profile)
- [get_deployment](./client.md#get-deployment)
- [get_deployment_strategy](./client.md#get-deployment-strategy)
- [get_environment](./client.md#get-environment)
- [get_hosted_configuration_version](./client.md#get-hosted-configuration-version)
- [list_applications](./client.md#list-applications)
- [list_configuration_profiles](./client.md#list-configuration-profiles)
- [list_deployment_strategies](./client.md#list-deployment-strategies)
- [list_deployments](./client.md#list-deployments)
- [list_environments](./client.md#list-environments)
- [list_hosted_configuration_versions](./client.md#list-hosted-configuration-versions)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_deployment](./client.md#start-deployment)
- [stop_deployment](./client.md#stop-deployment)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)
- [update_configuration_profile](./client.md#update-configuration-profile)
- [update_deployment_strategy](./client.md#update-deployment-strategy)
- [update_environment](./client.md#update-environment)
- [validate_configuration](./client.md#validate-configuration)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [PayloadTooLargeException](./client.md#payloadtoolargeexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appconfig.literals import DeploymentEventType, ...
```

- [DeploymentEventType](./literals.md#deploymenteventtype)
- [DeploymentState](./literals.md#deploymentstate)
- [EnvironmentState](./literals.md#environmentstate)
- [GrowthType](./literals.md#growthtype)
- [ReplicateTo](./literals.md#replicateto)
- [TriggeredBy](./literals.md#triggeredby)
- [ValidatorType](./literals.md#validatortype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appconfig.type_defs import ApplicationTypeDef, ...
```

- [ApplicationTypeDef](./type_defs.md#applicationtypedef)
- [ConfigurationProfileSummaryTypeDef](./type_defs.md#configurationprofilesummarytypedef)
- [DeploymentEventTypeDef](./type_defs.md#deploymenteventtypedef)
- [DeploymentStrategyTypeDef](./type_defs.md#deploymentstrategytypedef)
- [DeploymentSummaryTypeDef](./type_defs.md#deploymentsummarytypedef)
- [EnvironmentTypeDef](./type_defs.md#environmenttypedef)
- [HostedConfigurationVersionSummaryTypeDef](./type_defs.md#hostedconfigurationversionsummarytypedef)
- [MonitorTypeDef](./type_defs.md#monitortypedef)
- [ValidatorTypeDef](./type_defs.md#validatortypedef)
- [ApplicationsTypeDef](./type_defs.md#applicationstypedef)
- [ConfigurationProfileTypeDef](./type_defs.md#configurationprofiletypedef)
- [ConfigurationProfilesTypeDef](./type_defs.md#configurationprofilestypedef)
- [ConfigurationTypeDef](./type_defs.md#configurationtypedef)
- [DeploymentStrategiesTypeDef](./type_defs.md#deploymentstrategiestypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DeploymentsTypeDef](./type_defs.md#deploymentstypedef)
- [EnvironmentsTypeDef](./type_defs.md#environmentstypedef)
- [HostedConfigurationVersionTypeDef](./type_defs.md#hostedconfigurationversiontypedef)
- [HostedConfigurationVersionsTypeDef](./type_defs.md#hostedconfigurationversionstypedef)
- [ResourceTagsTypeDef](./type_defs.md#resourcetagstypedef)
