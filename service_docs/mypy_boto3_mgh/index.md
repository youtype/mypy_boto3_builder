# Type annotations for boto3 MigrationHub module

> [Index](../index.md) > MigrationHub

Auto-generated documentation for [MigrationHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html#MigrationHub)
type annotations stubs module [mypy_boto3_mgh](https://pypi.org/project/mypy-boto3-mgh/).

```bash
pip install mypy-boto3-mgh
```

- [Type annotations for boto3 MigrationHub module](#type-annotations-for-boto3-migrationhub-module)
  - [MigrationHubClient](#migrationhubclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MigrationHubClient

Type annotations for  `boto3.client("mgh")` as [MigrationHubClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mgh.client import MigrationHubClient
```


MigrationHubClient [exceptions](./client.md#exceptions)



### Methods
- [associate_created_artifact](./client.md#associate-created-artifact)
- [associate_discovered_resource](./client.md#associate-discovered-resource)
- [can_paginate](./client.md#can-paginate)
- [create_progress_update_stream](./client.md#create-progress-update-stream)
- [delete_progress_update_stream](./client.md#delete-progress-update-stream)
- [describe_application_state](./client.md#describe-application-state)
- [describe_migration_task](./client.md#describe-migration-task)
- [disassociate_created_artifact](./client.md#disassociate-created-artifact)
- [disassociate_discovered_resource](./client.md#disassociate-discovered-resource)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [import_migration_task](./client.md#import-migration-task)
- [list_application_states](./client.md#list-application-states)
- [list_created_artifacts](./client.md#list-created-artifacts)
- [list_discovered_resources](./client.md#list-discovered-resources)
- [list_migration_tasks](./client.md#list-migration-tasks)
- [list_progress_update_streams](./client.md#list-progress-update-streams)
- [notify_application_state](./client.md#notify-application-state)
- [notify_migration_task_state](./client.md#notify-migration-task-state)
- [put_resource_attributes](./client.md#put-resource-attributes)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [DryRunOperation](./client.md#dryrunoperation)
- [HomeRegionNotSetException](./client.md#homeregionnotsetexception)
- [InternalServerError](./client.md#internalservererror)
- [InvalidInputException](./client.md#invalidinputexception)
- [PolicyErrorException](./client.md#policyerrorexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)
- [UnauthorizedOperation](./client.md#unauthorizedoperation)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mgh").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mgh.paginators import ListApplicationStatesPaginator, ...
```

- [ListApplicationStatesPaginator](./paginators.md#listapplicationstatespaginator)
- [ListCreatedArtifactsPaginator](./paginators.md#listcreatedartifactspaginator)
- [ListDiscoveredResourcesPaginator](./paginators.md#listdiscoveredresourcespaginator)
- [ListMigrationTasksPaginator](./paginators.md#listmigrationtaskspaginator)
- [ListProgressUpdateStreamsPaginator](./paginators.md#listprogressupdatestreamspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mgh.literals import ApplicationStatus, ...
```

- [ApplicationStatus](./literals.md#applicationstatus)
- [ListApplicationStatesPaginatorName](./literals.md#listapplicationstatespaginatorname)
- [ListCreatedArtifactsPaginatorName](./literals.md#listcreatedartifactspaginatorname)
- [ListDiscoveredResourcesPaginatorName](./literals.md#listdiscoveredresourcespaginatorname)
- [ListMigrationTasksPaginatorName](./literals.md#listmigrationtaskspaginatorname)
- [ListProgressUpdateStreamsPaginatorName](./literals.md#listprogressupdatestreamspaginatorname)
- [ResourceAttributeType](./literals.md#resourceattributetype)
- [Status](./literals.md#status)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef, ...
```

- [ApplicationStateTypeDef](./type_defs.md#applicationstatetypedef)
- [CreatedArtifactTypeDef](./type_defs.md#createdartifacttypedef)
- [DescribeApplicationStateResultTypeDef](./type_defs.md#describeapplicationstateresulttypedef)
- [DescribeMigrationTaskResultTypeDef](./type_defs.md#describemigrationtaskresulttypedef)
- [DiscoveredResourceTypeDef](./type_defs.md#discoveredresourcetypedef)
- [ListApplicationStatesResultTypeDef](./type_defs.md#listapplicationstatesresulttypedef)
- [ListCreatedArtifactsResultTypeDef](./type_defs.md#listcreatedartifactsresulttypedef)
- [ListDiscoveredResourcesResultTypeDef](./type_defs.md#listdiscoveredresourcesresulttypedef)
- [ListMigrationTasksResultTypeDef](./type_defs.md#listmigrationtasksresulttypedef)
- [ListProgressUpdateStreamsResultTypeDef](./type_defs.md#listprogressupdatestreamsresulttypedef)
- [MigrationTaskSummaryTypeDef](./type_defs.md#migrationtasksummarytypedef)
- [MigrationTaskTypeDef](./type_defs.md#migrationtasktypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProgressUpdateStreamSummaryTypeDef](./type_defs.md#progressupdatestreamsummarytypedef)
- [ResourceAttributeTypeDef](./type_defs.md#resourceattributetypedef)
- [TaskTypeDef](./type_defs.md#tasktypedef)
