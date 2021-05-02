# Type annotations for boto3 ElasticBeanstalk module

> [Index](../index.md) > ElasticBeanstalk

Auto-generated documentation for [ElasticBeanstalk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk)
type annotations stubs module [mypy_boto3_elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/).

```bash
pip install mypy-boto3-elasticbeanstalk
```

- [Type annotations for boto3 ElasticBeanstalk module](#type-annotations-for-boto3-elasticbeanstalk-module)
  - [ElasticBeanstalkClient](#elasticbeanstalkclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ElasticBeanstalkClient

Type annotations for  `boto3.client("elasticbeanstalk")` as [ElasticBeanstalkClient](./client.md)

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.client import ElasticBeanstalkClient
```


ElasticBeanstalkClient [exceptions](./client.md#exceptions)



### Methods
- [abort_environment_update](./client.md#abort-environment-update)
- [apply_environment_managed_action](./client.md#apply-environment-managed-action)
- [associate_environment_operations_role](./client.md#associate-environment-operations-role)
- [can_paginate](./client.md#can-paginate)
- [check_dns_availability](./client.md#check-dns-availability)
- [compose_environments](./client.md#compose-environments)
- [create_application](./client.md#create-application)
- [create_application_version](./client.md#create-application-version)
- [create_configuration_template](./client.md#create-configuration-template)
- [create_environment](./client.md#create-environment)
- [create_platform_version](./client.md#create-platform-version)
- [create_storage_location](./client.md#create-storage-location)
- [delete_application](./client.md#delete-application)
- [delete_application_version](./client.md#delete-application-version)
- [delete_configuration_template](./client.md#delete-configuration-template)
- [delete_environment_configuration](./client.md#delete-environment-configuration)
- [delete_platform_version](./client.md#delete-platform-version)
- [describe_account_attributes](./client.md#describe-account-attributes)
- [describe_application_versions](./client.md#describe-application-versions)
- [describe_applications](./client.md#describe-applications)
- [describe_configuration_options](./client.md#describe-configuration-options)
- [describe_configuration_settings](./client.md#describe-configuration-settings)
- [describe_environment_health](./client.md#describe-environment-health)
- [describe_environment_managed_action_history](./client.md#describe-environment-managed-action-history)
- [describe_environment_managed_actions](./client.md#describe-environment-managed-actions)
- [describe_environment_resources](./client.md#describe-environment-resources)
- [describe_environments](./client.md#describe-environments)
- [describe_events](./client.md#describe-events)
- [describe_instances_health](./client.md#describe-instances-health)
- [describe_platform_version](./client.md#describe-platform-version)
- [disassociate_environment_operations_role](./client.md#disassociate-environment-operations-role)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_available_solution_stacks](./client.md#list-available-solution-stacks)
- [list_platform_branches](./client.md#list-platform-branches)
- [list_platform_versions](./client.md#list-platform-versions)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [rebuild_environment](./client.md#rebuild-environment)
- [request_environment_info](./client.md#request-environment-info)
- [restart_app_server](./client.md#restart-app-server)
- [retrieve_environment_info](./client.md#retrieve-environment-info)
- [swap_environment_cnames](./client.md#swap-environment-cnames)
- [terminate_environment](./client.md#terminate-environment)
- [update_application](./client.md#update-application)
- [update_application_resource_lifecycle](./client.md#update-application-resource-lifecycle)
- [update_application_version](./client.md#update-application-version)
- [update_configuration_template](./client.md#update-configuration-template)
- [update_environment](./client.md#update-environment)
- [update_tags_for_resource](./client.md#update-tags-for-resource)
- [validate_configuration_settings](./client.md#validate-configuration-settings)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CodeBuildNotInServiceRegionException](./client.md#codebuildnotinserviceregionexception)
- [ElasticBeanstalkServiceException](./client.md#elasticbeanstalkserviceexception)
- [InsufficientPrivilegesException](./client.md#insufficientprivilegesexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ManagedActionInvalidStateException](./client.md#managedactioninvalidstateexception)
- [OperationInProgressException](./client.md#operationinprogressexception)
- [PlatformVersionStillReferencedException](./client.md#platformversionstillreferencedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceTypeNotSupportedException](./client.md#resourcetypenotsupportedexception)
- [S3LocationNotInServiceRegionException](./client.md#s3locationnotinserviceregionexception)
- [S3SubscriptionRequiredException](./client.md#s3subscriptionrequiredexception)
- [SourceBundleDeletionException](./client.md#sourcebundledeletionexception)
- [TooManyApplicationVersionsException](./client.md#toomanyapplicationversionsexception)
- [TooManyApplicationsException](./client.md#toomanyapplicationsexception)
- [TooManyBucketsException](./client.md#toomanybucketsexception)
- [TooManyConfigurationTemplatesException](./client.md#toomanyconfigurationtemplatesexception)
- [TooManyEnvironmentsException](./client.md#toomanyenvironmentsexception)
- [TooManyPlatformsException](./client.md#toomanyplatformsexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("elasticbeanstalk").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.paginators import DescribeApplicationVersionsPaginator, ...
```

- [DescribeApplicationVersionsPaginator](./paginators.md#describeapplicationversionspaginator)
- [DescribeEnvironmentManagedActionHistoryPaginator](./paginators.md#describeenvironmentmanagedactionhistorypaginator)
- [DescribeEnvironmentsPaginator](./paginators.md#describeenvironmentspaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [ListPlatformVersionsPaginator](./paginators.md#listplatformversionspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("elasticbeanstalk").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.waiters import EnvironmentExistsWaiter, ...
```

- [EnvironmentExistsWaiter](./waiters.md#environmentexistswaiter)
- [EnvironmentTerminatedWaiter](./waiters.md#environmentterminatedwaiter)
- [EnvironmentUpdatedWaiter](./waiters.md#environmentupdatedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.literals import ActionHistoryStatus, ...
```

- [ActionHistoryStatus](./literals.md#actionhistorystatus)
- [ActionStatus](./literals.md#actionstatus)
- [ActionType](./literals.md#actiontype)
- [ApplicationVersionStatus](./literals.md#applicationversionstatus)
- [ComputeType](./literals.md#computetype)
- [ConfigurationDeploymentStatus](./literals.md#configurationdeploymentstatus)
- [ConfigurationOptionValueType](./literals.md#configurationoptionvaluetype)
- [DescribeApplicationVersionsPaginatorName](./literals.md#describeapplicationversionspaginatorname)
- [DescribeEnvironmentManagedActionHistoryPaginatorName](./literals.md#describeenvironmentmanagedactionhistorypaginatorname)
- [DescribeEnvironmentsPaginatorName](./literals.md#describeenvironmentspaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [EnvironmentExistsWaiterName](./literals.md#environmentexistswaitername)
- [EnvironmentHealth](./literals.md#environmenthealth)
- [EnvironmentHealthAttribute](./literals.md#environmenthealthattribute)
- [EnvironmentHealthStatus](./literals.md#environmenthealthstatus)
- [EnvironmentInfoType](./literals.md#environmentinfotype)
- [EnvironmentStatus](./literals.md#environmentstatus)
- [EnvironmentTerminatedWaiterName](./literals.md#environmentterminatedwaitername)
- [EnvironmentUpdatedWaiterName](./literals.md#environmentupdatedwaitername)
- [EventSeverity](./literals.md#eventseverity)
- [FailureType](./literals.md#failuretype)
- [InstancesHealthAttribute](./literals.md#instanceshealthattribute)
- [ListPlatformVersionsPaginatorName](./literals.md#listplatformversionspaginatorname)
- [PlatformStatus](./literals.md#platformstatus)
- [SourceRepository](./literals.md#sourcerepository)
- [SourceType](./literals.md#sourcetype)
- [ValidationSeverity](./literals.md#validationseverity)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.type_defs import ApplicationDescriptionMessageTypeDef, ...
```

- [ApplicationDescriptionMessageTypeDef](./type_defs.md#applicationdescriptionmessagetypedef)
- [ApplicationDescriptionTypeDef](./type_defs.md#applicationdescriptiontypedef)
- [ApplicationDescriptionsMessageTypeDef](./type_defs.md#applicationdescriptionsmessagetypedef)
- [ApplicationMetricsTypeDef](./type_defs.md#applicationmetricstypedef)
- [ApplicationResourceLifecycleConfigTypeDef](./type_defs.md#applicationresourcelifecycleconfigtypedef)
- [ApplicationResourceLifecycleDescriptionMessageTypeDef](./type_defs.md#applicationresourcelifecycledescriptionmessagetypedef)
- [ApplicationVersionDescriptionMessageTypeDef](./type_defs.md#applicationversiondescriptionmessagetypedef)
- [ApplicationVersionDescriptionTypeDef](./type_defs.md#applicationversiondescriptiontypedef)
- [ApplicationVersionDescriptionsMessageTypeDef](./type_defs.md#applicationversiondescriptionsmessagetypedef)
- [ApplicationVersionLifecycleConfigTypeDef](./type_defs.md#applicationversionlifecycleconfigtypedef)
- [ApplyEnvironmentManagedActionResultTypeDef](./type_defs.md#applyenvironmentmanagedactionresulttypedef)
- [AutoScalingGroupTypeDef](./type_defs.md#autoscalinggrouptypedef)
- [BuildConfigurationTypeDef](./type_defs.md#buildconfigurationtypedef)
- [BuilderTypeDef](./type_defs.md#buildertypedef)
- [CPUUtilizationTypeDef](./type_defs.md#cpuutilizationtypedef)
- [CheckDNSAvailabilityResultMessageTypeDef](./type_defs.md#checkdnsavailabilityresultmessagetypedef)
- [ConfigurationOptionDescriptionTypeDef](./type_defs.md#configurationoptiondescriptiontypedef)
- [ConfigurationOptionSettingTypeDef](./type_defs.md#configurationoptionsettingtypedef)
- [ConfigurationOptionsDescriptionTypeDef](./type_defs.md#configurationoptionsdescriptiontypedef)
- [ConfigurationSettingsDescriptionTypeDef](./type_defs.md#configurationsettingsdescriptiontypedef)
- [ConfigurationSettingsDescriptionsTypeDef](./type_defs.md#configurationsettingsdescriptionstypedef)
- [ConfigurationSettingsValidationMessagesTypeDef](./type_defs.md#configurationsettingsvalidationmessagestypedef)
- [CreatePlatformVersionResultTypeDef](./type_defs.md#createplatformversionresulttypedef)
- [CreateStorageLocationResultMessageTypeDef](./type_defs.md#createstoragelocationresultmessagetypedef)
- [CustomAmiTypeDef](./type_defs.md#customamitypedef)
- [DeletePlatformVersionResultTypeDef](./type_defs.md#deleteplatformversionresulttypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DescribeAccountAttributesResultTypeDef](./type_defs.md#describeaccountattributesresulttypedef)
- [DescribeEnvironmentHealthResultTypeDef](./type_defs.md#describeenvironmenthealthresulttypedef)
- [DescribeEnvironmentManagedActionHistoryResultTypeDef](./type_defs.md#describeenvironmentmanagedactionhistoryresulttypedef)
- [DescribeEnvironmentManagedActionsResultTypeDef](./type_defs.md#describeenvironmentmanagedactionsresulttypedef)
- [DescribeInstancesHealthResultTypeDef](./type_defs.md#describeinstanceshealthresulttypedef)
- [DescribePlatformVersionResultTypeDef](./type_defs.md#describeplatformversionresulttypedef)
- [EnvironmentDescriptionTypeDef](./type_defs.md#environmentdescriptiontypedef)
- [EnvironmentDescriptionsMessageTypeDef](./type_defs.md#environmentdescriptionsmessagetypedef)
- [EnvironmentInfoDescriptionTypeDef](./type_defs.md#environmentinfodescriptiontypedef)
- [EnvironmentLinkTypeDef](./type_defs.md#environmentlinktypedef)
- [EnvironmentResourceDescriptionTypeDef](./type_defs.md#environmentresourcedescriptiontypedef)
- [EnvironmentResourceDescriptionsMessageTypeDef](./type_defs.md#environmentresourcedescriptionsmessagetypedef)
- [EnvironmentResourcesDescriptionTypeDef](./type_defs.md#environmentresourcesdescriptiontypedef)
- [EnvironmentTierTypeDef](./type_defs.md#environmenttiertypedef)
- [EventDescriptionTypeDef](./type_defs.md#eventdescriptiontypedef)
- [EventDescriptionsMessageTypeDef](./type_defs.md#eventdescriptionsmessagetypedef)
- [InstanceHealthSummaryTypeDef](./type_defs.md#instancehealthsummarytypedef)
- [InstanceTypeDef](./type_defs.md#instancetypedef)
- [LatencyTypeDef](./type_defs.md#latencytypedef)
- [LaunchConfigurationTypeDef](./type_defs.md#launchconfigurationtypedef)
- [LaunchTemplateTypeDef](./type_defs.md#launchtemplatetypedef)
- [ListAvailableSolutionStacksResultMessageTypeDef](./type_defs.md#listavailablesolutionstacksresultmessagetypedef)
- [ListPlatformBranchesResultTypeDef](./type_defs.md#listplatformbranchesresulttypedef)
- [ListPlatformVersionsResultTypeDef](./type_defs.md#listplatformversionsresulttypedef)
- [ListenerTypeDef](./type_defs.md#listenertypedef)
- [LoadBalancerDescriptionTypeDef](./type_defs.md#loadbalancerdescriptiontypedef)
- [LoadBalancerTypeDef](./type_defs.md#loadbalancertypedef)
- [ManagedActionHistoryItemTypeDef](./type_defs.md#managedactionhistoryitemtypedef)
- [ManagedActionTypeDef](./type_defs.md#managedactiontypedef)
- [MaxAgeRuleTypeDef](./type_defs.md#maxageruletypedef)
- [MaxCountRuleTypeDef](./type_defs.md#maxcountruletypedef)
- [OptionRestrictionRegexTypeDef](./type_defs.md#optionrestrictionregextypedef)
- [OptionSpecificationTypeDef](./type_defs.md#optionspecificationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PlatformBranchSummaryTypeDef](./type_defs.md#platformbranchsummarytypedef)
- [PlatformDescriptionTypeDef](./type_defs.md#platformdescriptiontypedef)
- [PlatformFilterTypeDef](./type_defs.md#platformfiltertypedef)
- [PlatformFrameworkTypeDef](./type_defs.md#platformframeworktypedef)
- [PlatformProgrammingLanguageTypeDef](./type_defs.md#platformprogramminglanguagetypedef)
- [PlatformSummaryTypeDef](./type_defs.md#platformsummarytypedef)
- [QueueTypeDef](./type_defs.md#queuetypedef)
- [ResourceQuotaTypeDef](./type_defs.md#resourcequotatypedef)
- [ResourceQuotasTypeDef](./type_defs.md#resourcequotastypedef)
- [ResourceTagsDescriptionMessageTypeDef](./type_defs.md#resourcetagsdescriptionmessagetypedef)
- [RetrieveEnvironmentInfoResultMessageTypeDef](./type_defs.md#retrieveenvironmentinforesultmessagetypedef)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [SearchFilterTypeDef](./type_defs.md#searchfiltertypedef)
- [SingleInstanceHealthTypeDef](./type_defs.md#singleinstancehealthtypedef)
- [SolutionStackDescriptionTypeDef](./type_defs.md#solutionstackdescriptiontypedef)
- [SourceBuildInformationTypeDef](./type_defs.md#sourcebuildinformationtypedef)
- [SourceConfigurationTypeDef](./type_defs.md#sourceconfigurationtypedef)
- [StatusCodesTypeDef](./type_defs.md#statuscodestypedef)
- [SystemStatusTypeDef](./type_defs.md#systemstatustypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TriggerTypeDef](./type_defs.md#triggertypedef)
- [ValidationMessageTypeDef](./type_defs.md#validationmessagetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
