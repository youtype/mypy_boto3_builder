# Type annotations for boto3 mgn module

> [Index](../index.md) > mgn

Auto-generated documentation for [mgn](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn)
type annotations stubs module [mypy_boto3_mgn](https://pypi.org/project/mypy-boto3-mgn/).

```bash
pip install mypy-boto3-mgn
```

- [Type annotations for boto3 mgn module](#type-annotations-for-boto3-mgn-module)
  - [mgnClient](#mgnclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## mgnClient

Type annotations for  `boto3.client("mgn")` as [mgnClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mgn.client import mgnClient
```


mgnClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [change_server_life_cycle_state](./client.md#change-server-life-cycle-state)
- [create_replication_configuration_template](./client.md#create-replication-configuration-template)
- [delete_job](./client.md#delete-job)
- [delete_replication_configuration_template](./client.md#delete-replication-configuration-template)
- [delete_source_server](./client.md#delete-source-server)
- [describe_job_log_items](./client.md#describe-job-log-items)
- [describe_jobs](./client.md#describe-jobs)
- [describe_replication_configuration_templates](./client.md#describe-replication-configuration-templates)
- [describe_source_servers](./client.md#describe-source-servers)
- [disconnect_from_service](./client.md#disconnect-from-service)
- [finalize_cutover](./client.md#finalize-cutover)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_launch_configuration](./client.md#get-launch-configuration)
- [get_paginator](./client.md#get-paginator)
- [get_replication_configuration](./client.md#get-replication-configuration)
- [initialize_service](./client.md#initialize-service)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [mark_as_archived](./client.md#mark-as-archived)
- [retry_data_replication](./client.md#retry-data-replication)
- [start_cutover](./client.md#start-cutover)
- [start_test](./client.md#start-test)
- [tag_resource](./client.md#tag-resource)
- [terminate_target_instances](./client.md#terminate-target-instances)
- [untag_resource](./client.md#untag-resource)
- [update_launch_configuration](./client.md#update-launch-configuration)
- [update_replication_configuration](./client.md#update-replication-configuration)
- [update_replication_configuration_template](./client.md#update-replication-configuration-template)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)
- [UninitializedAccountException](./client.md#uninitializedaccountexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mgn").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mgn.paginators import DescribeJobLogItemsPaginator, ...
```

- [DescribeJobLogItemsPaginator](./paginators.md#describejoblogitemspaginator)
- [DescribeJobsPaginator](./paginators.md#describejobspaginator)
- [DescribeReplicationConfigurationTemplatesPaginator](./paginators.md#describereplicationconfigurationtemplatespaginator)
- [DescribeSourceServersPaginator](./paginators.md#describesourceserverspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mgn.literals import ChangeServerLifeCycleStateSourceServerLifecycleState, ...
```

- [ChangeServerLifeCycleStateSourceServerLifecycleState](./literals.md#changeserverlifecyclestatesourceserverlifecyclestate)
- [DataReplicationErrorString](./literals.md#datareplicationerrorstring)
- [DataReplicationInitiationStepName](./literals.md#datareplicationinitiationstepname)
- [DataReplicationInitiationStepStatus](./literals.md#datareplicationinitiationstepstatus)
- [DataReplicationState](./literals.md#datareplicationstate)
- [DescribeJobLogItemsPaginatorName](./literals.md#describejoblogitemspaginatorname)
- [DescribeJobsPaginatorName](./literals.md#describejobspaginatorname)
- [DescribeReplicationConfigurationTemplatesPaginatorName](./literals.md#describereplicationconfigurationtemplatespaginatorname)
- [DescribeSourceServersPaginatorName](./literals.md#describesourceserverspaginatorname)
- [FirstBoot](./literals.md#firstboot)
- [InitiatedBy](./literals.md#initiatedby)
- [JobLogEvent](./literals.md#joblogevent)
- [JobStatus](./literals.md#jobstatus)
- [JobType](./literals.md#jobtype)
- [LaunchDisposition](./literals.md#launchdisposition)
- [LaunchStatus](./literals.md#launchstatus)
- [LifeCycleState](./literals.md#lifecyclestate)
- [ReplicationConfigurationDataPlaneRouting](./literals.md#replicationconfigurationdataplanerouting)
- [ReplicationConfigurationDefaultLargeStagingDiskType](./literals.md#replicationconfigurationdefaultlargestagingdisktype)
- [ReplicationConfigurationEbsEncryption](./literals.md#replicationconfigurationebsencryption)
- [ReplicationConfigurationReplicatedDiskStagingDiskType](./literals.md#replicationconfigurationreplicateddiskstagingdisktype)
- [TargetInstanceTypeRightSizingMethod](./literals.md#targetinstancetyperightsizingmethod)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mgn.type_defs import CPUTypeDef, ...
```

- [CPUTypeDef](./type_defs.md#cputypedef)
- [ChangeServerLifeCycleStateSourceServerLifecycleTypeDef](./type_defs.md#changeserverlifecyclestatesourceserverlifecycletypedef)
- [DataReplicationErrorTypeDef](./type_defs.md#datareplicationerrortypedef)
- [DataReplicationInfoReplicatedDiskTypeDef](./type_defs.md#datareplicationinforeplicateddisktypedef)
- [DataReplicationInfoTypeDef](./type_defs.md#datareplicationinfotypedef)
- [DataReplicationInitiationStepTypeDef](./type_defs.md#datareplicationinitiationsteptypedef)
- [DataReplicationInitiationTypeDef](./type_defs.md#datareplicationinitiationtypedef)
- [DescribeJobLogItemsResponseTypeDef](./type_defs.md#describejoblogitemsresponsetypedef)
- [DescribeJobsRequestFiltersTypeDef](./type_defs.md#describejobsrequestfilterstypedef)
- [DescribeJobsResponseTypeDef](./type_defs.md#describejobsresponsetypedef)
- [DescribeReplicationConfigurationTemplatesResponseTypeDef](./type_defs.md#describereplicationconfigurationtemplatesresponsetypedef)
- [DescribeSourceServersRequestFiltersTypeDef](./type_defs.md#describesourceserversrequestfilterstypedef)
- [DescribeSourceServersResponseTypeDef](./type_defs.md#describesourceserversresponsetypedef)
- [DiskTypeDef](./type_defs.md#disktypedef)
- [IdentificationHintsTypeDef](./type_defs.md#identificationhintstypedef)
- [JobLogEventDataTypeDef](./type_defs.md#joblogeventdatatypedef)
- [JobLogTypeDef](./type_defs.md#joblogtypedef)
- [JobTypeDef](./type_defs.md#jobtypedef)
- [LaunchConfigurationTypeDef](./type_defs.md#launchconfigurationtypedef)
- [LaunchedInstanceTypeDef](./type_defs.md#launchedinstancetypedef)
- [LicensingTypeDef](./type_defs.md#licensingtypedef)
- [LifeCycleLastCutoverFinalizedTypeDef](./type_defs.md#lifecyclelastcutoverfinalizedtypedef)
- [LifeCycleLastCutoverInitiatedTypeDef](./type_defs.md#lifecyclelastcutoverinitiatedtypedef)
- [LifeCycleLastCutoverRevertedTypeDef](./type_defs.md#lifecyclelastcutoverrevertedtypedef)
- [LifeCycleLastCutoverTypeDef](./type_defs.md#lifecyclelastcutovertypedef)
- [LifeCycleLastTestFinalizedTypeDef](./type_defs.md#lifecyclelasttestfinalizedtypedef)
- [LifeCycleLastTestInitiatedTypeDef](./type_defs.md#lifecyclelasttestinitiatedtypedef)
- [LifeCycleLastTestRevertedTypeDef](./type_defs.md#lifecyclelasttestrevertedtypedef)
- [LifeCycleLastTestTypeDef](./type_defs.md#lifecyclelasttesttypedef)
- [LifeCycleTypeDef](./type_defs.md#lifecycletypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [OSTypeDef](./type_defs.md#ostypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParticipatingServerTypeDef](./type_defs.md#participatingservertypedef)
- [ReplicationConfigurationReplicatedDiskTypeDef](./type_defs.md#replicationconfigurationreplicateddisktypedef)
- [ReplicationConfigurationTemplateTypeDef](./type_defs.md#replicationconfigurationtemplatetypedef)
- [ReplicationConfigurationTypeDef](./type_defs.md#replicationconfigurationtypedef)
- [SourcePropertiesTypeDef](./type_defs.md#sourcepropertiestypedef)
- [SourceServerTypeDef](./type_defs.md#sourceservertypedef)
- [StartCutoverResponseTypeDef](./type_defs.md#startcutoverresponsetypedef)
- [StartTestResponseTypeDef](./type_defs.md#starttestresponsetypedef)
- [TerminateTargetInstancesResponseTypeDef](./type_defs.md#terminatetargetinstancesresponsetypedef)
