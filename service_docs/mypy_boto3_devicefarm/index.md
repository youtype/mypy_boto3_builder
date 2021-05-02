# Type annotations for boto3 DeviceFarm module

> [Index](../index.md) > DeviceFarm

Auto-generated documentation for [DeviceFarm](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm)
type annotations stubs module [mypy_boto3_devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/).

```bash
pip install mypy-boto3-devicefarm
```

- [Type annotations for boto3 DeviceFarm module](#type-annotations-for-boto3-devicefarm-module)
  - [DeviceFarmClient](#devicefarmclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DeviceFarmClient

Type annotations for  `boto3.client("devicefarm")` as [DeviceFarmClient](./client.md)

Can be used directly:

```python
from mypy_boto3_devicefarm.client import DeviceFarmClient
```


DeviceFarmClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_device_pool](./client.md#create-device-pool)
- [create_instance_profile](./client.md#create-instance-profile)
- [create_network_profile](./client.md#create-network-profile)
- [create_project](./client.md#create-project)
- [create_remote_access_session](./client.md#create-remote-access-session)
- [create_test_grid_project](./client.md#create-test-grid-project)
- [create_test_grid_url](./client.md#create-test-grid-url)
- [create_upload](./client.md#create-upload)
- [create_vpce_configuration](./client.md#create-vpce-configuration)
- [delete_device_pool](./client.md#delete-device-pool)
- [delete_instance_profile](./client.md#delete-instance-profile)
- [delete_network_profile](./client.md#delete-network-profile)
- [delete_project](./client.md#delete-project)
- [delete_remote_access_session](./client.md#delete-remote-access-session)
- [delete_run](./client.md#delete-run)
- [delete_test_grid_project](./client.md#delete-test-grid-project)
- [delete_upload](./client.md#delete-upload)
- [delete_vpce_configuration](./client.md#delete-vpce-configuration)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account_settings](./client.md#get-account-settings)
- [get_device](./client.md#get-device)
- [get_device_instance](./client.md#get-device-instance)
- [get_device_pool](./client.md#get-device-pool)
- [get_device_pool_compatibility](./client.md#get-device-pool-compatibility)
- [get_instance_profile](./client.md#get-instance-profile)
- [get_job](./client.md#get-job)
- [get_network_profile](./client.md#get-network-profile)
- [get_offering_status](./client.md#get-offering-status)
- [get_paginator](./client.md#get-paginator)
- [get_project](./client.md#get-project)
- [get_remote_access_session](./client.md#get-remote-access-session)
- [get_run](./client.md#get-run)
- [get_suite](./client.md#get-suite)
- [get_test](./client.md#get-test)
- [get_test_grid_project](./client.md#get-test-grid-project)
- [get_test_grid_session](./client.md#get-test-grid-session)
- [get_upload](./client.md#get-upload)
- [get_vpce_configuration](./client.md#get-vpce-configuration)
- [install_to_remote_access_session](./client.md#install-to-remote-access-session)
- [list_artifacts](./client.md#list-artifacts)
- [list_device_instances](./client.md#list-device-instances)
- [list_device_pools](./client.md#list-device-pools)
- [list_devices](./client.md#list-devices)
- [list_instance_profiles](./client.md#list-instance-profiles)
- [list_jobs](./client.md#list-jobs)
- [list_network_profiles](./client.md#list-network-profiles)
- [list_offering_promotions](./client.md#list-offering-promotions)
- [list_offering_transactions](./client.md#list-offering-transactions)
- [list_offerings](./client.md#list-offerings)
- [list_projects](./client.md#list-projects)
- [list_remote_access_sessions](./client.md#list-remote-access-sessions)
- [list_runs](./client.md#list-runs)
- [list_samples](./client.md#list-samples)
- [list_suites](./client.md#list-suites)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_test_grid_projects](./client.md#list-test-grid-projects)
- [list_test_grid_session_actions](./client.md#list-test-grid-session-actions)
- [list_test_grid_session_artifacts](./client.md#list-test-grid-session-artifacts)
- [list_test_grid_sessions](./client.md#list-test-grid-sessions)
- [list_tests](./client.md#list-tests)
- [list_unique_problems](./client.md#list-unique-problems)
- [list_uploads](./client.md#list-uploads)
- [list_vpce_configurations](./client.md#list-vpce-configurations)
- [purchase_offering](./client.md#purchase-offering)
- [renew_offering](./client.md#renew-offering)
- [schedule_run](./client.md#schedule-run)
- [stop_job](./client.md#stop-job)
- [stop_remote_access_session](./client.md#stop-remote-access-session)
- [stop_run](./client.md#stop-run)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_device_instance](./client.md#update-device-instance)
- [update_device_pool](./client.md#update-device-pool)
- [update_instance_profile](./client.md#update-instance-profile)
- [update_network_profile](./client.md#update-network-profile)
- [update_project](./client.md#update-project)
- [update_test_grid_project](./client.md#update-test-grid-project)
- [update_upload](./client.md#update-upload)
- [update_vpce_configuration](./client.md#update-vpce-configuration)




### Exceptions
- [ArgumentException](./client.md#argumentexception)
- [CannotDeleteException](./client.md#cannotdeleteexception)
- [ClientError](./client.md#clienterror)
- [IdempotencyException](./client.md#idempotencyexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotEligibleException](./client.md#noteligibleexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceAccountException](./client.md#serviceaccountexception)
- [TagOperationException](./client.md#tagoperationexception)
- [TagPolicyException](./client.md#tagpolicyexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("devicefarm").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import GetOfferingStatusPaginator, ...
```

- [GetOfferingStatusPaginator](./paginators.md#getofferingstatuspaginator)
- [ListArtifactsPaginator](./paginators.md#listartifactspaginator)
- [ListDeviceInstancesPaginator](./paginators.md#listdeviceinstancespaginator)
- [ListDevicePoolsPaginator](./paginators.md#listdevicepoolspaginator)
- [ListDevicesPaginator](./paginators.md#listdevicespaginator)
- [ListInstanceProfilesPaginator](./paginators.md#listinstanceprofilespaginator)
- [ListJobsPaginator](./paginators.md#listjobspaginator)
- [ListNetworkProfilesPaginator](./paginators.md#listnetworkprofilespaginator)
- [ListOfferingPromotionsPaginator](./paginators.md#listofferingpromotionspaginator)
- [ListOfferingTransactionsPaginator](./paginators.md#listofferingtransactionspaginator)
- [ListOfferingsPaginator](./paginators.md#listofferingspaginator)
- [ListProjectsPaginator](./paginators.md#listprojectspaginator)
- [ListRemoteAccessSessionsPaginator](./paginators.md#listremoteaccesssessionspaginator)
- [ListRunsPaginator](./paginators.md#listrunspaginator)
- [ListSamplesPaginator](./paginators.md#listsamplespaginator)
- [ListSuitesPaginator](./paginators.md#listsuitespaginator)
- [ListTestsPaginator](./paginators.md#listtestspaginator)
- [ListUniqueProblemsPaginator](./paginators.md#listuniqueproblemspaginator)
- [ListUploadsPaginator](./paginators.md#listuploadspaginator)
- [ListVPCEConfigurationsPaginator](./paginators.md#listvpceconfigurationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_devicefarm.literals import ArtifactCategory, ...
```

- [ArtifactCategory](./literals.md#artifactcategory)
- [ArtifactType](./literals.md#artifacttype)
- [BillingMethod](./literals.md#billingmethod)
- [CurrencyCode](./literals.md#currencycode)
- [DeviceAttribute](./literals.md#deviceattribute)
- [DeviceAvailability](./literals.md#deviceavailability)
- [DeviceFilterAttribute](./literals.md#devicefilterattribute)
- [DeviceFormFactor](./literals.md#deviceformfactor)
- [DevicePlatform](./literals.md#deviceplatform)
- [DevicePoolType](./literals.md#devicepooltype)
- [ExecutionResult](./literals.md#executionresult)
- [ExecutionResultCode](./literals.md#executionresultcode)
- [ExecutionStatus](./literals.md#executionstatus)
- [GetOfferingStatusPaginatorName](./literals.md#getofferingstatuspaginatorname)
- [InstanceStatus](./literals.md#instancestatus)
- [InteractionMode](./literals.md#interactionmode)
- [ListArtifactsPaginatorName](./literals.md#listartifactspaginatorname)
- [ListDeviceInstancesPaginatorName](./literals.md#listdeviceinstancespaginatorname)
- [ListDevicePoolsPaginatorName](./literals.md#listdevicepoolspaginatorname)
- [ListDevicesPaginatorName](./literals.md#listdevicespaginatorname)
- [ListInstanceProfilesPaginatorName](./literals.md#listinstanceprofilespaginatorname)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)
- [ListNetworkProfilesPaginatorName](./literals.md#listnetworkprofilespaginatorname)
- [ListOfferingPromotionsPaginatorName](./literals.md#listofferingpromotionspaginatorname)
- [ListOfferingTransactionsPaginatorName](./literals.md#listofferingtransactionspaginatorname)
- [ListOfferingsPaginatorName](./literals.md#listofferingspaginatorname)
- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)
- [ListRemoteAccessSessionsPaginatorName](./literals.md#listremoteaccesssessionspaginatorname)
- [ListRunsPaginatorName](./literals.md#listrunspaginatorname)
- [ListSamplesPaginatorName](./literals.md#listsamplespaginatorname)
- [ListSuitesPaginatorName](./literals.md#listsuitespaginatorname)
- [ListTestsPaginatorName](./literals.md#listtestspaginatorname)
- [ListUniqueProblemsPaginatorName](./literals.md#listuniqueproblemspaginatorname)
- [ListUploadsPaginatorName](./literals.md#listuploadspaginatorname)
- [ListVPCEConfigurationsPaginatorName](./literals.md#listvpceconfigurationspaginatorname)
- [NetworkProfileType](./literals.md#networkprofiletype)
- [OfferingTransactionType](./literals.md#offeringtransactiontype)
- [OfferingType](./literals.md#offeringtype)
- [RecurringChargeFrequency](./literals.md#recurringchargefrequency)
- [RuleOperator](./literals.md#ruleoperator)
- [SampleType](./literals.md#sampletype)
- [TestGridSessionArtifactCategory](./literals.md#testgridsessionartifactcategory)
- [TestGridSessionArtifactType](./literals.md#testgridsessionartifacttype)
- [TestGridSessionStatus](./literals.md#testgridsessionstatus)
- [TestType](./literals.md#testtype)
- [UploadCategory](./literals.md#uploadcategory)
- [UploadStatus](./literals.md#uploadstatus)
- [UploadType](./literals.md#uploadtype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_devicefarm.type_defs import AccountSettingsTypeDef, ...
```

- [AccountSettingsTypeDef](./type_defs.md#accountsettingstypedef)
- [ArtifactTypeDef](./type_defs.md#artifacttypedef)
- [CPUTypeDef](./type_defs.md#cputypedef)
- [CountersTypeDef](./type_defs.md#counterstypedef)
- [CustomerArtifactPathsTypeDef](./type_defs.md#customerartifactpathstypedef)
- [DeviceFilterTypeDef](./type_defs.md#devicefiltertypedef)
- [DeviceInstanceTypeDef](./type_defs.md#deviceinstancetypedef)
- [DeviceMinutesTypeDef](./type_defs.md#deviceminutestypedef)
- [DevicePoolCompatibilityResultTypeDef](./type_defs.md#devicepoolcompatibilityresulttypedef)
- [DevicePoolTypeDef](./type_defs.md#devicepooltypedef)
- [DeviceSelectionResultTypeDef](./type_defs.md#deviceselectionresulttypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [IncompatibilityMessageTypeDef](./type_defs.md#incompatibilitymessagetypedef)
- [InstanceProfileTypeDef](./type_defs.md#instanceprofiletypedef)
- [JobTypeDef](./type_defs.md#jobtypedef)
- [LocationTypeDef](./type_defs.md#locationtypedef)
- [MonetaryAmountTypeDef](./type_defs.md#monetaryamounttypedef)
- [NetworkProfileTypeDef](./type_defs.md#networkprofiletypedef)
- [OfferingPromotionTypeDef](./type_defs.md#offeringpromotiontypedef)
- [OfferingStatusTypeDef](./type_defs.md#offeringstatustypedef)
- [OfferingTransactionTypeDef](./type_defs.md#offeringtransactiontypedef)
- [OfferingTypeDef](./type_defs.md#offeringtypedef)
- [ProblemDetailTypeDef](./type_defs.md#problemdetailtypedef)
- [ProblemTypeDef](./type_defs.md#problemtypedef)
- [ProjectTypeDef](./type_defs.md#projecttypedef)
- [RadiosTypeDef](./type_defs.md#radiostypedef)
- [RecurringChargeTypeDef](./type_defs.md#recurringchargetypedef)
- [RemoteAccessSessionTypeDef](./type_defs.md#remoteaccesssessiontypedef)
- [ResolutionTypeDef](./type_defs.md#resolutiontypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [RunTypeDef](./type_defs.md#runtypedef)
- [SampleTypeDef](./type_defs.md#sampletypedef)
- [SuiteTypeDef](./type_defs.md#suitetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TestGridProjectTypeDef](./type_defs.md#testgridprojecttypedef)
- [TestGridSessionActionTypeDef](./type_defs.md#testgridsessionactiontypedef)
- [TestGridSessionArtifactTypeDef](./type_defs.md#testgridsessionartifacttypedef)
- [TestGridSessionTypeDef](./type_defs.md#testgridsessiontypedef)
- [TestTypeDef](./type_defs.md#testtypedef)
- [TrialMinutesTypeDef](./type_defs.md#trialminutestypedef)
- [UniqueProblemTypeDef](./type_defs.md#uniqueproblemtypedef)
- [UploadTypeDef](./type_defs.md#uploadtypedef)
- [VPCEConfigurationTypeDef](./type_defs.md#vpceconfigurationtypedef)
- [CreateDevicePoolResultTypeDef](./type_defs.md#createdevicepoolresulttypedef)
- [CreateInstanceProfileResultTypeDef](./type_defs.md#createinstanceprofileresulttypedef)
- [CreateNetworkProfileResultTypeDef](./type_defs.md#createnetworkprofileresulttypedef)
- [CreateProjectResultTypeDef](./type_defs.md#createprojectresulttypedef)
- [CreateRemoteAccessSessionConfigurationTypeDef](./type_defs.md#createremoteaccesssessionconfigurationtypedef)
- [CreateRemoteAccessSessionResultTypeDef](./type_defs.md#createremoteaccesssessionresulttypedef)
- [CreateTestGridProjectResultTypeDef](./type_defs.md#createtestgridprojectresulttypedef)
- [CreateTestGridUrlResultTypeDef](./type_defs.md#createtestgridurlresulttypedef)
- [CreateUploadResultTypeDef](./type_defs.md#createuploadresulttypedef)
- [CreateVPCEConfigurationResultTypeDef](./type_defs.md#createvpceconfigurationresulttypedef)
- [DeviceSelectionConfigurationTypeDef](./type_defs.md#deviceselectionconfigurationtypedef)
- [ExecutionConfigurationTypeDef](./type_defs.md#executionconfigurationtypedef)
- [GetAccountSettingsResultTypeDef](./type_defs.md#getaccountsettingsresulttypedef)
- [GetDeviceInstanceResultTypeDef](./type_defs.md#getdeviceinstanceresulttypedef)
- [GetDevicePoolCompatibilityResultTypeDef](./type_defs.md#getdevicepoolcompatibilityresulttypedef)
- [GetDevicePoolResultTypeDef](./type_defs.md#getdevicepoolresulttypedef)
- [GetDeviceResultTypeDef](./type_defs.md#getdeviceresulttypedef)
- [GetInstanceProfileResultTypeDef](./type_defs.md#getinstanceprofileresulttypedef)
- [GetJobResultTypeDef](./type_defs.md#getjobresulttypedef)
- [GetNetworkProfileResultTypeDef](./type_defs.md#getnetworkprofileresulttypedef)
- [GetOfferingStatusResultTypeDef](./type_defs.md#getofferingstatusresulttypedef)
- [GetProjectResultTypeDef](./type_defs.md#getprojectresulttypedef)
- [GetRemoteAccessSessionResultTypeDef](./type_defs.md#getremoteaccesssessionresulttypedef)
- [GetRunResultTypeDef](./type_defs.md#getrunresulttypedef)
- [GetSuiteResultTypeDef](./type_defs.md#getsuiteresulttypedef)
- [GetTestGridProjectResultTypeDef](./type_defs.md#gettestgridprojectresulttypedef)
- [GetTestGridSessionResultTypeDef](./type_defs.md#gettestgridsessionresulttypedef)
- [GetTestResultTypeDef](./type_defs.md#gettestresulttypedef)
- [GetUploadResultTypeDef](./type_defs.md#getuploadresulttypedef)
- [GetVPCEConfigurationResultTypeDef](./type_defs.md#getvpceconfigurationresulttypedef)
- [InstallToRemoteAccessSessionResultTypeDef](./type_defs.md#installtoremoteaccesssessionresulttypedef)
- [ListArtifactsResultTypeDef](./type_defs.md#listartifactsresulttypedef)
- [ListDeviceInstancesResultTypeDef](./type_defs.md#listdeviceinstancesresulttypedef)
- [ListDevicePoolsResultTypeDef](./type_defs.md#listdevicepoolsresulttypedef)
- [ListDevicesResultTypeDef](./type_defs.md#listdevicesresulttypedef)
- [ListInstanceProfilesResultTypeDef](./type_defs.md#listinstanceprofilesresulttypedef)
- [ListJobsResultTypeDef](./type_defs.md#listjobsresulttypedef)
- [ListNetworkProfilesResultTypeDef](./type_defs.md#listnetworkprofilesresulttypedef)
- [ListOfferingPromotionsResultTypeDef](./type_defs.md#listofferingpromotionsresulttypedef)
- [ListOfferingTransactionsResultTypeDef](./type_defs.md#listofferingtransactionsresulttypedef)
- [ListOfferingsResultTypeDef](./type_defs.md#listofferingsresulttypedef)
- [ListProjectsResultTypeDef](./type_defs.md#listprojectsresulttypedef)
- [ListRemoteAccessSessionsResultTypeDef](./type_defs.md#listremoteaccesssessionsresulttypedef)
- [ListRunsResultTypeDef](./type_defs.md#listrunsresulttypedef)
- [ListSamplesResultTypeDef](./type_defs.md#listsamplesresulttypedef)
- [ListSuitesResultTypeDef](./type_defs.md#listsuitesresulttypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTestGridProjectsResultTypeDef](./type_defs.md#listtestgridprojectsresulttypedef)
- [ListTestGridSessionActionsResultTypeDef](./type_defs.md#listtestgridsessionactionsresulttypedef)
- [ListTestGridSessionArtifactsResultTypeDef](./type_defs.md#listtestgridsessionartifactsresulttypedef)
- [ListTestGridSessionsResultTypeDef](./type_defs.md#listtestgridsessionsresulttypedef)
- [ListTestsResultTypeDef](./type_defs.md#listtestsresulttypedef)
- [ListUniqueProblemsResultTypeDef](./type_defs.md#listuniqueproblemsresulttypedef)
- [ListUploadsResultTypeDef](./type_defs.md#listuploadsresulttypedef)
- [ListVPCEConfigurationsResultTypeDef](./type_defs.md#listvpceconfigurationsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PurchaseOfferingResultTypeDef](./type_defs.md#purchaseofferingresulttypedef)
- [RenewOfferingResultTypeDef](./type_defs.md#renewofferingresulttypedef)
- [ScheduleRunConfigurationTypeDef](./type_defs.md#schedulerunconfigurationtypedef)
- [ScheduleRunResultTypeDef](./type_defs.md#schedulerunresulttypedef)
- [ScheduleRunTestTypeDef](./type_defs.md#scheduleruntesttypedef)
- [StopJobResultTypeDef](./type_defs.md#stopjobresulttypedef)
- [StopRemoteAccessSessionResultTypeDef](./type_defs.md#stopremoteaccesssessionresulttypedef)
- [StopRunResultTypeDef](./type_defs.md#stoprunresulttypedef)
- [UpdateDeviceInstanceResultTypeDef](./type_defs.md#updatedeviceinstanceresulttypedef)
- [UpdateDevicePoolResultTypeDef](./type_defs.md#updatedevicepoolresulttypedef)
- [UpdateInstanceProfileResultTypeDef](./type_defs.md#updateinstanceprofileresulttypedef)
- [UpdateNetworkProfileResultTypeDef](./type_defs.md#updatenetworkprofileresulttypedef)
- [UpdateProjectResultTypeDef](./type_defs.md#updateprojectresulttypedef)
- [UpdateTestGridProjectResultTypeDef](./type_defs.md#updatetestgridprojectresulttypedef)
- [UpdateUploadResultTypeDef](./type_defs.md#updateuploadresulttypedef)
- [UpdateVPCEConfigurationResultTypeDef](./type_defs.md#updatevpceconfigurationresulttypedef)
