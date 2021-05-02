# Type annotations for boto3 ServerlessApplicationRepository module

> [Index](../index.md) > ServerlessApplicationRepository

Auto-generated documentation for [ServerlessApplicationRepository](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository)
type annotations stubs module [mypy_boto3_serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo/).

```bash
pip install mypy-boto3-serverlessrepo
```

- [Type annotations for boto3 ServerlessApplicationRepository module](#type-annotations-for-boto3-serverlessapplicationrepository-module)
  - [ServerlessApplicationRepositoryClient](#serverlessapplicationrepositoryclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ServerlessApplicationRepositoryClient

Type annotations for  `boto3.client("serverlessrepo")` as [ServerlessApplicationRepositoryClient](./client.md)

Can be used directly:

```python
from mypy_boto3_serverlessrepo.client import ServerlessApplicationRepositoryClient
```


ServerlessApplicationRepositoryClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [create_application_version](./client.md#create-application-version)
- [create_cloud_formation_change_set](./client.md#create-cloud-formation-change-set)
- [create_cloud_formation_template](./client.md#create-cloud-formation-template)
- [delete_application](./client.md#delete-application)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_application](./client.md#get-application)
- [get_application_policy](./client.md#get-application-policy)
- [get_cloud_formation_template](./client.md#get-cloud-formation-template)
- [get_paginator](./client.md#get-paginator)
- [list_application_dependencies](./client.md#list-application-dependencies)
- [list_application_versions](./client.md#list-application-versions)
- [list_applications](./client.md#list-applications)
- [put_application_policy](./client.md#put-application-policy)
- [unshare_application](./client.md#unshare-application)
- [update_application](./client.md#update-application)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("serverlessrepo").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_serverlessrepo.paginators import ListApplicationDependenciesPaginator, ...
```

- [ListApplicationDependenciesPaginator](./paginators.md#listapplicationdependenciespaginator)
- [ListApplicationVersionsPaginator](./paginators.md#listapplicationversionspaginator)
- [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_serverlessrepo.literals import Capability, ...
```

- [Capability](./literals.md#capability)
- [ListApplicationDependenciesPaginatorName](./literals.md#listapplicationdependenciespaginatorname)
- [ListApplicationVersionsPaginatorName](./literals.md#listapplicationversionspaginatorname)
- [ListApplicationsPaginatorName](./literals.md#listapplicationspaginatorname)
- [Status](./literals.md#status)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_serverlessrepo.type_defs import ApplicationDependencySummaryTypeDef, ...
```

- [ApplicationDependencySummaryTypeDef](./type_defs.md#applicationdependencysummarytypedef)
- [ApplicationPolicyStatementTypeDef](./type_defs.md#applicationpolicystatementtypedef)
- [ApplicationSummaryTypeDef](./type_defs.md#applicationsummarytypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [CreateApplicationVersionResponseTypeDef](./type_defs.md#createapplicationversionresponsetypedef)
- [CreateCloudFormationChangeSetResponseTypeDef](./type_defs.md#createcloudformationchangesetresponsetypedef)
- [CreateCloudFormationTemplateResponseTypeDef](./type_defs.md#createcloudformationtemplateresponsetypedef)
- [GetApplicationPolicyResponseTypeDef](./type_defs.md#getapplicationpolicyresponsetypedef)
- [GetApplicationResponseTypeDef](./type_defs.md#getapplicationresponsetypedef)
- [GetCloudFormationTemplateResponseTypeDef](./type_defs.md#getcloudformationtemplateresponsetypedef)
- [ListApplicationDependenciesResponseTypeDef](./type_defs.md#listapplicationdependenciesresponsetypedef)
- [ListApplicationVersionsResponseTypeDef](./type_defs.md#listapplicationversionsresponsetypedef)
- [ListApplicationsResponseTypeDef](./type_defs.md#listapplicationsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterDefinitionTypeDef](./type_defs.md#parameterdefinitiontypedef)
- [ParameterValueTypeDef](./type_defs.md#parametervaluetypedef)
- [PutApplicationPolicyResponseTypeDef](./type_defs.md#putapplicationpolicyresponsetypedef)
- [RollbackConfigurationTypeDef](./type_defs.md#rollbackconfigurationtypedef)
- [RollbackTriggerTypeDef](./type_defs.md#rollbacktriggertypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateApplicationResponseTypeDef](./type_defs.md#updateapplicationresponsetypedef)
- [VersionSummaryTypeDef](./type_defs.md#versionsummarytypedef)
- [VersionTypeDef](./type_defs.md#versiontypedef)
