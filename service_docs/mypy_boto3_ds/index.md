# Type annotations for boto3 DirectoryService module

> [Index](../index.md) > DirectoryService

Auto-generated documentation for [DirectoryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService)
type annotations stubs module [mypy_boto3_ds](https://pypi.org/project/mypy-boto3-ds/).

```bash
pip install mypy-boto3-ds
```

- [Type annotations for boto3 DirectoryService module](#type-annotations-for-boto3-directoryservice-module)
  - [DirectoryServiceClient](#directoryserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DirectoryServiceClient

Type annotations for  `boto3.client("ds")` as [DirectoryServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ds.client import DirectoryServiceClient
```


DirectoryServiceClient [exceptions](./client.md#exceptions)



### Methods
- [accept_shared_directory](./client.md#accept-shared-directory)
- [add_ip_routes](./client.md#add-ip-routes)
- [add_region](./client.md#add-region)
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [can_paginate](./client.md#can-paginate)
- [cancel_schema_extension](./client.md#cancel-schema-extension)
- [connect_directory](./client.md#connect-directory)
- [create_alias](./client.md#create-alias)
- [create_computer](./client.md#create-computer)
- [create_conditional_forwarder](./client.md#create-conditional-forwarder)
- [create_directory](./client.md#create-directory)
- [create_log_subscription](./client.md#create-log-subscription)
- [create_microsoft_ad](./client.md#create-microsoft-ad)
- [create_snapshot](./client.md#create-snapshot)
- [create_trust](./client.md#create-trust)
- [delete_conditional_forwarder](./client.md#delete-conditional-forwarder)
- [delete_directory](./client.md#delete-directory)
- [delete_log_subscription](./client.md#delete-log-subscription)
- [delete_snapshot](./client.md#delete-snapshot)
- [delete_trust](./client.md#delete-trust)
- [deregister_certificate](./client.md#deregister-certificate)
- [deregister_event_topic](./client.md#deregister-event-topic)
- [describe_certificate](./client.md#describe-certificate)
- [describe_conditional_forwarders](./client.md#describe-conditional-forwarders)
- [describe_directories](./client.md#describe-directories)
- [describe_domain_controllers](./client.md#describe-domain-controllers)
- [describe_event_topics](./client.md#describe-event-topics)
- [describe_ldaps_settings](./client.md#describe-ldaps-settings)
- [describe_regions](./client.md#describe-regions)
- [describe_shared_directories](./client.md#describe-shared-directories)
- [describe_snapshots](./client.md#describe-snapshots)
- [describe_trusts](./client.md#describe-trusts)
- [disable_client_authentication](./client.md#disable-client-authentication)
- [disable_ldaps](./client.md#disable-ldaps)
- [disable_radius](./client.md#disable-radius)
- [disable_sso](./client.md#disable-sso)
- [enable_client_authentication](./client.md#enable-client-authentication)
- [enable_ldaps](./client.md#enable-ldaps)
- [enable_radius](./client.md#enable-radius)
- [enable_sso](./client.md#enable-sso)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_directory_limits](./client.md#get-directory-limits)
- [get_paginator](./client.md#get-paginator)
- [get_snapshot_limits](./client.md#get-snapshot-limits)
- [list_certificates](./client.md#list-certificates)
- [list_ip_routes](./client.md#list-ip-routes)
- [list_log_subscriptions](./client.md#list-log-subscriptions)
- [list_schema_extensions](./client.md#list-schema-extensions)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [register_certificate](./client.md#register-certificate)
- [register_event_topic](./client.md#register-event-topic)
- [reject_shared_directory](./client.md#reject-shared-directory)
- [remove_ip_routes](./client.md#remove-ip-routes)
- [remove_region](./client.md#remove-region)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)
- [reset_user_password](./client.md#reset-user-password)
- [restore_from_snapshot](./client.md#restore-from-snapshot)
- [share_directory](./client.md#share-directory)
- [start_schema_extension](./client.md#start-schema-extension)
- [unshare_directory](./client.md#unshare-directory)
- [update_conditional_forwarder](./client.md#update-conditional-forwarder)
- [update_number_of_domain_controllers](./client.md#update-number-of-domain-controllers)
- [update_radius](./client.md#update-radius)
- [update_trust](./client.md#update-trust)
- [verify_trust](./client.md#verify-trust)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AuthenticationFailedException](./client.md#authenticationfailedexception)
- [CertificateAlreadyExistsException](./client.md#certificatealreadyexistsexception)
- [CertificateDoesNotExistException](./client.md#certificatedoesnotexistexception)
- [CertificateInUseException](./client.md#certificateinuseexception)
- [CertificateLimitExceededException](./client.md#certificatelimitexceededexception)
- [ClientError](./client.md#clienterror)
- [ClientException](./client.md#clientexception)
- [DirectoryAlreadyInRegionException](./client.md#directoryalreadyinregionexception)
- [DirectoryAlreadySharedException](./client.md#directoryalreadysharedexception)
- [DirectoryDoesNotExistException](./client.md#directorydoesnotexistexception)
- [DirectoryLimitExceededException](./client.md#directorylimitexceededexception)
- [DirectoryNotSharedException](./client.md#directorynotsharedexception)
- [DirectoryUnavailableException](./client.md#directoryunavailableexception)
- [DomainControllerLimitExceededException](./client.md#domaincontrollerlimitexceededexception)
- [EntityAlreadyExistsException](./client.md#entityalreadyexistsexception)
- [EntityDoesNotExistException](./client.md#entitydoesnotexistexception)
- [InsufficientPermissionsException](./client.md#insufficientpermissionsexception)
- [InvalidCertificateException](./client.md#invalidcertificateexception)
- [InvalidClientAuthStatusException](./client.md#invalidclientauthstatusexception)
- [InvalidLDAPSStatusException](./client.md#invalidldapsstatusexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidPasswordException](./client.md#invalidpasswordexception)
- [InvalidTargetException](./client.md#invalidtargetexception)
- [IpRouteLimitExceededException](./client.md#iproutelimitexceededexception)
- [NoAvailableCertificateException](./client.md#noavailablecertificateexception)
- [OrganizationsException](./client.md#organizationsexception)
- [RegionLimitExceededException](./client.md#regionlimitexceededexception)
- [ServiceException](./client.md#serviceexception)
- [ShareLimitExceededException](./client.md#sharelimitexceededexception)
- [SnapshotLimitExceededException](./client.md#snapshotlimitexceededexception)
- [TagLimitExceededException](./client.md#taglimitexceededexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)
- [UserDoesNotExistException](./client.md#userdoesnotexistexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ds").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ds.paginators import DescribeDirectoriesPaginator, ...
```

- [DescribeDirectoriesPaginator](./paginators.md#describedirectoriespaginator)
- [DescribeDomainControllersPaginator](./paginators.md#describedomaincontrollerspaginator)
- [DescribeSharedDirectoriesPaginator](./paginators.md#describeshareddirectoriespaginator)
- [DescribeSnapshotsPaginator](./paginators.md#describesnapshotspaginator)
- [DescribeTrustsPaginator](./paginators.md#describetrustspaginator)
- [ListIpRoutesPaginator](./paginators.md#listiproutespaginator)
- [ListLogSubscriptionsPaginator](./paginators.md#listlogsubscriptionspaginator)
- [ListSchemaExtensionsPaginator](./paginators.md#listschemaextensionspaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ds.literals import CertificateState, ...
```

- [CertificateState](./literals.md#certificatestate)
- [CertificateType](./literals.md#certificatetype)
- [ClientAuthenticationType](./literals.md#clientauthenticationtype)
- [DescribeDirectoriesPaginatorName](./literals.md#describedirectoriespaginatorname)
- [DescribeDomainControllersPaginatorName](./literals.md#describedomaincontrollerspaginatorname)
- [DescribeSharedDirectoriesPaginatorName](./literals.md#describeshareddirectoriespaginatorname)
- [DescribeSnapshotsPaginatorName](./literals.md#describesnapshotspaginatorname)
- [DescribeTrustsPaginatorName](./literals.md#describetrustspaginatorname)
- [DirectoryEdition](./literals.md#directoryedition)
- [DirectorySize](./literals.md#directorysize)
- [DirectoryStage](./literals.md#directorystage)
- [DirectoryType](./literals.md#directorytype)
- [DomainControllerStatus](./literals.md#domaincontrollerstatus)
- [IpRouteStatusMsg](./literals.md#iproutestatusmsg)
- [LDAPSStatus](./literals.md#ldapsstatus)
- [LDAPSType](./literals.md#ldapstype)
- [ListIpRoutesPaginatorName](./literals.md#listiproutespaginatorname)
- [ListLogSubscriptionsPaginatorName](./literals.md#listlogsubscriptionspaginatorname)
- [ListSchemaExtensionsPaginatorName](./literals.md#listschemaextensionspaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [RadiusAuthenticationProtocol](./literals.md#radiusauthenticationprotocol)
- [RadiusStatus](./literals.md#radiusstatus)
- [RegionType](./literals.md#regiontype)
- [ReplicationScope](./literals.md#replicationscope)
- [SchemaExtensionStatus](./literals.md#schemaextensionstatus)
- [SelectiveAuth](./literals.md#selectiveauth)
- [ShareMethod](./literals.md#sharemethod)
- [ShareStatus](./literals.md#sharestatus)
- [SnapshotStatus](./literals.md#snapshotstatus)
- [SnapshotType](./literals.md#snapshottype)
- [TargetType](./literals.md#targettype)
- [TopicStatus](./literals.md#topicstatus)
- [TrustDirection](./literals.md#trustdirection)
- [TrustState](./literals.md#truststate)
- [TrustType](./literals.md#trusttype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ds.type_defs import AcceptSharedDirectoryResultTypeDef, ...
```

- [AcceptSharedDirectoryResultTypeDef](./type_defs.md#acceptshareddirectoryresulttypedef)
- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [CertificateInfoTypeDef](./type_defs.md#certificateinfotypedef)
- [CertificateTypeDef](./type_defs.md#certificatetypedef)
- [ClientCertAuthSettingsTypeDef](./type_defs.md#clientcertauthsettingstypedef)
- [ComputerTypeDef](./type_defs.md#computertypedef)
- [ConditionalForwarderTypeDef](./type_defs.md#conditionalforwardertypedef)
- [ConnectDirectoryResultTypeDef](./type_defs.md#connectdirectoryresulttypedef)
- [CreateAliasResultTypeDef](./type_defs.md#createaliasresulttypedef)
- [CreateComputerResultTypeDef](./type_defs.md#createcomputerresulttypedef)
- [CreateDirectoryResultTypeDef](./type_defs.md#createdirectoryresulttypedef)
- [CreateMicrosoftADResultTypeDef](./type_defs.md#createmicrosoftadresulttypedef)
- [CreateSnapshotResultTypeDef](./type_defs.md#createsnapshotresulttypedef)
- [CreateTrustResultTypeDef](./type_defs.md#createtrustresulttypedef)
- [DeleteDirectoryResultTypeDef](./type_defs.md#deletedirectoryresulttypedef)
- [DeleteSnapshotResultTypeDef](./type_defs.md#deletesnapshotresulttypedef)
- [DeleteTrustResultTypeDef](./type_defs.md#deletetrustresulttypedef)
- [DescribeCertificateResultTypeDef](./type_defs.md#describecertificateresulttypedef)
- [DescribeConditionalForwardersResultTypeDef](./type_defs.md#describeconditionalforwardersresulttypedef)
- [DescribeDirectoriesResultTypeDef](./type_defs.md#describedirectoriesresulttypedef)
- [DescribeDomainControllersResultTypeDef](./type_defs.md#describedomaincontrollersresulttypedef)
- [DescribeEventTopicsResultTypeDef](./type_defs.md#describeeventtopicsresulttypedef)
- [DescribeLDAPSSettingsResultTypeDef](./type_defs.md#describeldapssettingsresulttypedef)
- [DescribeRegionsResultTypeDef](./type_defs.md#describeregionsresulttypedef)
- [DescribeSharedDirectoriesResultTypeDef](./type_defs.md#describeshareddirectoriesresulttypedef)
- [DescribeSnapshotsResultTypeDef](./type_defs.md#describesnapshotsresulttypedef)
- [DescribeTrustsResultTypeDef](./type_defs.md#describetrustsresulttypedef)
- [DirectoryConnectSettingsDescriptionTypeDef](./type_defs.md#directoryconnectsettingsdescriptiontypedef)
- [DirectoryConnectSettingsTypeDef](./type_defs.md#directoryconnectsettingstypedef)
- [DirectoryDescriptionTypeDef](./type_defs.md#directorydescriptiontypedef)
- [DirectoryLimitsTypeDef](./type_defs.md#directorylimitstypedef)
- [DirectoryVpcSettingsDescriptionTypeDef](./type_defs.md#directoryvpcsettingsdescriptiontypedef)
- [DirectoryVpcSettingsTypeDef](./type_defs.md#directoryvpcsettingstypedef)
- [DomainControllerTypeDef](./type_defs.md#domaincontrollertypedef)
- [EventTopicTypeDef](./type_defs.md#eventtopictypedef)
- [GetDirectoryLimitsResultTypeDef](./type_defs.md#getdirectorylimitsresulttypedef)
- [GetSnapshotLimitsResultTypeDef](./type_defs.md#getsnapshotlimitsresulttypedef)
- [IpRouteInfoTypeDef](./type_defs.md#iprouteinfotypedef)
- [IpRouteTypeDef](./type_defs.md#iproutetypedef)
- [LDAPSSettingInfoTypeDef](./type_defs.md#ldapssettinginfotypedef)
- [ListCertificatesResultTypeDef](./type_defs.md#listcertificatesresulttypedef)
- [ListIpRoutesResultTypeDef](./type_defs.md#listiproutesresulttypedef)
- [ListLogSubscriptionsResultTypeDef](./type_defs.md#listlogsubscriptionsresulttypedef)
- [ListSchemaExtensionsResultTypeDef](./type_defs.md#listschemaextensionsresulttypedef)
- [ListTagsForResourceResultTypeDef](./type_defs.md#listtagsforresourceresulttypedef)
- [LogSubscriptionTypeDef](./type_defs.md#logsubscriptiontypedef)
- [OwnerDirectoryDescriptionTypeDef](./type_defs.md#ownerdirectorydescriptiontypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RadiusSettingsTypeDef](./type_defs.md#radiussettingstypedef)
- [RegionDescriptionTypeDef](./type_defs.md#regiondescriptiontypedef)
- [RegionsInfoTypeDef](./type_defs.md#regionsinfotypedef)
- [RegisterCertificateResultTypeDef](./type_defs.md#registercertificateresulttypedef)
- [RejectSharedDirectoryResultTypeDef](./type_defs.md#rejectshareddirectoryresulttypedef)
- [SchemaExtensionInfoTypeDef](./type_defs.md#schemaextensioninfotypedef)
- [ShareDirectoryResultTypeDef](./type_defs.md#sharedirectoryresulttypedef)
- [ShareTargetTypeDef](./type_defs.md#sharetargettypedef)
- [SharedDirectoryTypeDef](./type_defs.md#shareddirectorytypedef)
- [SnapshotLimitsTypeDef](./type_defs.md#snapshotlimitstypedef)
- [SnapshotTypeDef](./type_defs.md#snapshottypedef)
- [StartSchemaExtensionResultTypeDef](./type_defs.md#startschemaextensionresulttypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TrustTypeDef](./type_defs.md#trusttypedef)
- [UnshareDirectoryResultTypeDef](./type_defs.md#unsharedirectoryresulttypedef)
- [UnshareTargetTypeDef](./type_defs.md#unsharetargettypedef)
- [UpdateTrustResultTypeDef](./type_defs.md#updatetrustresulttypedef)
- [VerifyTrustResultTypeDef](./type_defs.md#verifytrustresulttypedef)
