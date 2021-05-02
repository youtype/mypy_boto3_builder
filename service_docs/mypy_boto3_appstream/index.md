# Type annotations for boto3 AppStream module

> [Index](../index.md) > AppStream

Auto-generated documentation for [AppStream](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream)
type annotations stubs module [mypy_boto3_appstream](https://pypi.org/project/mypy-boto3-appstream/).

```bash
pip install mypy-boto3-appstream
```

- [Type annotations for boto3 AppStream module](#type-annotations-for-boto3-appstream-module)
  - [AppStreamClient](#appstreamclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## AppStreamClient

Type annotations for  `boto3.client("appstream")` as [AppStreamClient](./client.md)

Can be used directly:

```python
from mypy_boto3_appstream.client import AppStreamClient
```


AppStreamClient [exceptions](./client.md#exceptions)



### Methods
- [associate_fleet](./client.md#associate-fleet)
- [batch_associate_user_stack](./client.md#batch-associate-user-stack)
- [batch_disassociate_user_stack](./client.md#batch-disassociate-user-stack)
- [can_paginate](./client.md#can-paginate)
- [copy_image](./client.md#copy-image)
- [create_directory_config](./client.md#create-directory-config)
- [create_fleet](./client.md#create-fleet)
- [create_image_builder](./client.md#create-image-builder)
- [create_image_builder_streaming_url](./client.md#create-image-builder-streaming-url)
- [create_stack](./client.md#create-stack)
- [create_streaming_url](./client.md#create-streaming-url)
- [create_updated_image](./client.md#create-updated-image)
- [create_usage_report_subscription](./client.md#create-usage-report-subscription)
- [create_user](./client.md#create-user)
- [delete_directory_config](./client.md#delete-directory-config)
- [delete_fleet](./client.md#delete-fleet)
- [delete_image](./client.md#delete-image)
- [delete_image_builder](./client.md#delete-image-builder)
- [delete_image_permissions](./client.md#delete-image-permissions)
- [delete_stack](./client.md#delete-stack)
- [delete_usage_report_subscription](./client.md#delete-usage-report-subscription)
- [delete_user](./client.md#delete-user)
- [describe_directory_configs](./client.md#describe-directory-configs)
- [describe_fleets](./client.md#describe-fleets)
- [describe_image_builders](./client.md#describe-image-builders)
- [describe_image_permissions](./client.md#describe-image-permissions)
- [describe_images](./client.md#describe-images)
- [describe_sessions](./client.md#describe-sessions)
- [describe_stacks](./client.md#describe-stacks)
- [describe_usage_report_subscriptions](./client.md#describe-usage-report-subscriptions)
- [describe_user_stack_associations](./client.md#describe-user-stack-associations)
- [describe_users](./client.md#describe-users)
- [disable_user](./client.md#disable-user)
- [disassociate_fleet](./client.md#disassociate-fleet)
- [enable_user](./client.md#enable-user)
- [expire_session](./client.md#expire-session)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_associated_fleets](./client.md#list-associated-fleets)
- [list_associated_stacks](./client.md#list-associated-stacks)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_fleet](./client.md#start-fleet)
- [start_image_builder](./client.md#start-image-builder)
- [stop_fleet](./client.md#stop-fleet)
- [stop_image_builder](./client.md#stop-image-builder)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_directory_config](./client.md#update-directory-config)
- [update_fleet](./client.md#update-fleet)
- [update_image_permissions](./client.md#update-image-permissions)
- [update_stack](./client.md#update-stack)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [IncompatibleImageException](./client.md#incompatibleimageexception)
- [InvalidAccountStatusException](./client.md#invalidaccountstatusexception)
- [InvalidParameterCombinationException](./client.md#invalidparametercombinationexception)
- [InvalidRoleException](./client.md#invalidroleexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [RequestLimitExceededException](./client.md#requestlimitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotAvailableException](./client.md#resourcenotavailableexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("appstream").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeDirectoryConfigsPaginator, ...
```

- [DescribeDirectoryConfigsPaginator](./paginators.md#describedirectoryconfigspaginator)
- [DescribeFleetsPaginator](./paginators.md#describefleetspaginator)
- [DescribeImageBuildersPaginator](./paginators.md#describeimagebuilderspaginator)
- [DescribeImagesPaginator](./paginators.md#describeimagespaginator)
- [DescribeSessionsPaginator](./paginators.md#describesessionspaginator)
- [DescribeStacksPaginator](./paginators.md#describestackspaginator)
- [DescribeUserStackAssociationsPaginator](./paginators.md#describeuserstackassociationspaginator)
- [DescribeUsersPaginator](./paginators.md#describeuserspaginator)
- [ListAssociatedFleetsPaginator](./paginators.md#listassociatedfleetspaginator)
- [ListAssociatedStacksPaginator](./paginators.md#listassociatedstackspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("appstream").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_appstream.waiters import FleetStartedWaiter, ...
```

- [FleetStartedWaiter](./waiters.md#fleetstartedwaiter)
- [FleetStoppedWaiter](./waiters.md#fleetstoppedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appstream.literals import AccessEndpointType, ...
```

- [AccessEndpointType](./literals.md#accessendpointtype)
- [Action](./literals.md#action)
- [AuthenticationType](./literals.md#authenticationtype)
- [DescribeDirectoryConfigsPaginatorName](./literals.md#describedirectoryconfigspaginatorname)
- [DescribeFleetsPaginatorName](./literals.md#describefleetspaginatorname)
- [DescribeImageBuildersPaginatorName](./literals.md#describeimagebuilderspaginatorname)
- [DescribeImagesPaginatorName](./literals.md#describeimagespaginatorname)
- [DescribeSessionsPaginatorName](./literals.md#describesessionspaginatorname)
- [DescribeStacksPaginatorName](./literals.md#describestackspaginatorname)
- [DescribeUserStackAssociationsPaginatorName](./literals.md#describeuserstackassociationspaginatorname)
- [DescribeUsersPaginatorName](./literals.md#describeuserspaginatorname)
- [FleetAttribute](./literals.md#fleetattribute)
- [FleetErrorCode](./literals.md#fleeterrorcode)
- [FleetStartedWaiterName](./literals.md#fleetstartedwaitername)
- [FleetState](./literals.md#fleetstate)
- [FleetStoppedWaiterName](./literals.md#fleetstoppedwaitername)
- [FleetType](./literals.md#fleettype)
- [ImageBuilderState](./literals.md#imagebuilderstate)
- [ImageBuilderStateChangeReasonCode](./literals.md#imagebuilderstatechangereasoncode)
- [ImageState](./literals.md#imagestate)
- [ImageStateChangeReasonCode](./literals.md#imagestatechangereasoncode)
- [ListAssociatedFleetsPaginatorName](./literals.md#listassociatedfleetspaginatorname)
- [ListAssociatedStacksPaginatorName](./literals.md#listassociatedstackspaginatorname)
- [MessageAction](./literals.md#messageaction)
- [Permission](./literals.md#permission)
- [PlatformType](./literals.md#platformtype)
- [SessionConnectionState](./literals.md#sessionconnectionstate)
- [SessionState](./literals.md#sessionstate)
- [StackAttribute](./literals.md#stackattribute)
- [StackErrorCode](./literals.md#stackerrorcode)
- [StorageConnectorType](./literals.md#storageconnectortype)
- [StreamView](./literals.md#streamview)
- [UsageReportExecutionErrorCode](./literals.md#usagereportexecutionerrorcode)
- [UsageReportSchedule](./literals.md#usagereportschedule)
- [UserStackAssociationErrorCode](./literals.md#userstackassociationerrorcode)
- [VisibilityType](./literals.md#visibilitytype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef, ...
```

- [AccessEndpointTypeDef](./type_defs.md#accessendpointtypedef)
- [ApplicationSettingsResponseTypeDef](./type_defs.md#applicationsettingsresponsetypedef)
- [ApplicationSettingsTypeDef](./type_defs.md#applicationsettingstypedef)
- [ApplicationTypeDef](./type_defs.md#applicationtypedef)
- [BatchAssociateUserStackResultTypeDef](./type_defs.md#batchassociateuserstackresulttypedef)
- [BatchDisassociateUserStackResultTypeDef](./type_defs.md#batchdisassociateuserstackresulttypedef)
- [ComputeCapacityStatusTypeDef](./type_defs.md#computecapacitystatustypedef)
- [ComputeCapacityTypeDef](./type_defs.md#computecapacitytypedef)
- [CopyImageResponseTypeDef](./type_defs.md#copyimageresponsetypedef)
- [CreateDirectoryConfigResultTypeDef](./type_defs.md#createdirectoryconfigresulttypedef)
- [CreateFleetResultTypeDef](./type_defs.md#createfleetresulttypedef)
- [CreateImageBuilderResultTypeDef](./type_defs.md#createimagebuilderresulttypedef)
- [CreateImageBuilderStreamingURLResultTypeDef](./type_defs.md#createimagebuilderstreamingurlresulttypedef)
- [CreateStackResultTypeDef](./type_defs.md#createstackresulttypedef)
- [CreateStreamingURLResultTypeDef](./type_defs.md#createstreamingurlresulttypedef)
- [CreateUpdatedImageResultTypeDef](./type_defs.md#createupdatedimageresulttypedef)
- [CreateUsageReportSubscriptionResultTypeDef](./type_defs.md#createusagereportsubscriptionresulttypedef)
- [DeleteImageBuilderResultTypeDef](./type_defs.md#deleteimagebuilderresulttypedef)
- [DeleteImageResultTypeDef](./type_defs.md#deleteimageresulttypedef)
- [DescribeDirectoryConfigsResultTypeDef](./type_defs.md#describedirectoryconfigsresulttypedef)
- [DescribeFleetsResultTypeDef](./type_defs.md#describefleetsresulttypedef)
- [DescribeImageBuildersResultTypeDef](./type_defs.md#describeimagebuildersresulttypedef)
- [DescribeImagePermissionsResultTypeDef](./type_defs.md#describeimagepermissionsresulttypedef)
- [DescribeImagesResultTypeDef](./type_defs.md#describeimagesresulttypedef)
- [DescribeSessionsResultTypeDef](./type_defs.md#describesessionsresulttypedef)
- [DescribeStacksResultTypeDef](./type_defs.md#describestacksresulttypedef)
- [DescribeUsageReportSubscriptionsResultTypeDef](./type_defs.md#describeusagereportsubscriptionsresulttypedef)
- [DescribeUserStackAssociationsResultTypeDef](./type_defs.md#describeuserstackassociationsresulttypedef)
- [DescribeUsersResultTypeDef](./type_defs.md#describeusersresulttypedef)
- [DirectoryConfigTypeDef](./type_defs.md#directoryconfigtypedef)
- [DomainJoinInfoTypeDef](./type_defs.md#domainjoininfotypedef)
- [FleetErrorTypeDef](./type_defs.md#fleeterrortypedef)
- [FleetTypeDef](./type_defs.md#fleettypedef)
- [ImageBuilderStateChangeReasonTypeDef](./type_defs.md#imagebuilderstatechangereasontypedef)
- [ImageBuilderTypeDef](./type_defs.md#imagebuildertypedef)
- [ImagePermissionsTypeDef](./type_defs.md#imagepermissionstypedef)
- [ImageStateChangeReasonTypeDef](./type_defs.md#imagestatechangereasontypedef)
- [ImageTypeDef](./type_defs.md#imagetypedef)
- [LastReportGenerationExecutionErrorTypeDef](./type_defs.md#lastreportgenerationexecutionerrortypedef)
- [ListAssociatedFleetsResultTypeDef](./type_defs.md#listassociatedfleetsresulttypedef)
- [ListAssociatedStacksResultTypeDef](./type_defs.md#listassociatedstacksresulttypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NetworkAccessConfigurationTypeDef](./type_defs.md#networkaccessconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResourceErrorTypeDef](./type_defs.md#resourceerrortypedef)
- [ServiceAccountCredentialsTypeDef](./type_defs.md#serviceaccountcredentialstypedef)
- [SessionTypeDef](./type_defs.md#sessiontypedef)
- [SharedImagePermissionsTypeDef](./type_defs.md#sharedimagepermissionstypedef)
- [StackErrorTypeDef](./type_defs.md#stackerrortypedef)
- [StackTypeDef](./type_defs.md#stacktypedef)
- [StartImageBuilderResultTypeDef](./type_defs.md#startimagebuilderresulttypedef)
- [StopImageBuilderResultTypeDef](./type_defs.md#stopimagebuilderresulttypedef)
- [StorageConnectorTypeDef](./type_defs.md#storageconnectortypedef)
- [UpdateDirectoryConfigResultTypeDef](./type_defs.md#updatedirectoryconfigresulttypedef)
- [UpdateFleetResultTypeDef](./type_defs.md#updatefleetresulttypedef)
- [UpdateStackResultTypeDef](./type_defs.md#updatestackresulttypedef)
- [UsageReportSubscriptionTypeDef](./type_defs.md#usagereportsubscriptiontypedef)
- [UserSettingTypeDef](./type_defs.md#usersettingtypedef)
- [UserStackAssociationErrorTypeDef](./type_defs.md#userstackassociationerrortypedef)
- [UserStackAssociationTypeDef](./type_defs.md#userstackassociationtypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
- [VpcConfigTypeDef](./type_defs.md#vpcconfigtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
