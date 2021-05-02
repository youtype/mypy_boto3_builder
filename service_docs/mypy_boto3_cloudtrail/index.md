# Type annotations for boto3 CloudTrail module

> [Index](../index.md) > CloudTrail

Auto-generated documentation for [CloudTrail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail)
type annotations stubs module [mypy_boto3_cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/).

```bash
pip install mypy-boto3-cloudtrail
```

- [Type annotations for boto3 CloudTrail module](#type-annotations-for-boto3-cloudtrail-module)
  - [CloudTrailClient](#cloudtrailclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudTrailClient

Type annotations for  `boto3.client("cloudtrail")` as [CloudTrailClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudtrail.client import CloudTrailClient
```


CloudTrailClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags](./client.md#add-tags)
- [can_paginate](./client.md#can-paginate)
- [create_trail](./client.md#create-trail)
- [delete_trail](./client.md#delete-trail)
- [describe_trails](./client.md#describe-trails)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_event_selectors](./client.md#get-event-selectors)
- [get_insight_selectors](./client.md#get-insight-selectors)
- [get_paginator](./client.md#get-paginator)
- [get_trail](./client.md#get-trail)
- [get_trail_status](./client.md#get-trail-status)
- [list_public_keys](./client.md#list-public-keys)
- [list_tags](./client.md#list-tags)
- [list_trails](./client.md#list-trails)
- [lookup_events](./client.md#lookup-events)
- [put_event_selectors](./client.md#put-event-selectors)
- [put_insight_selectors](./client.md#put-insight-selectors)
- [remove_tags](./client.md#remove-tags)
- [start_logging](./client.md#start-logging)
- [stop_logging](./client.md#stop-logging)
- [update_trail](./client.md#update-trail)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CloudTrailARNInvalidException](./client.md#cloudtrailarninvalidexception)
- [CloudTrailAccessNotEnabledException](./client.md#cloudtrailaccessnotenabledexception)
- [CloudTrailInvalidClientTokenIdException](./client.md#cloudtrailinvalidclienttokenidexception)
- [CloudWatchLogsDeliveryUnavailableException](./client.md#cloudwatchlogsdeliveryunavailableexception)
- [ConflictException](./client.md#conflictexception)
- [InsightNotEnabledException](./client.md#insightnotenabledexception)
- [InsufficientDependencyServiceAccessPermissionException](./client.md#insufficientdependencyserviceaccesspermissionexception)
- [InsufficientEncryptionPolicyException](./client.md#insufficientencryptionpolicyexception)
- [InsufficientS3BucketPolicyException](./client.md#insufficients3bucketpolicyexception)
- [InsufficientSnsTopicPolicyException](./client.md#insufficientsnstopicpolicyexception)
- [InvalidCloudWatchLogsLogGroupArnException](./client.md#invalidcloudwatchlogsloggrouparnexception)
- [InvalidCloudWatchLogsRoleArnException](./client.md#invalidcloudwatchlogsrolearnexception)
- [InvalidEventCategoryException](./client.md#invalideventcategoryexception)
- [InvalidEventSelectorsException](./client.md#invalideventselectorsexception)
- [InvalidHomeRegionException](./client.md#invalidhomeregionexception)
- [InvalidInsightSelectorsException](./client.md#invalidinsightselectorsexception)
- [InvalidKmsKeyIdException](./client.md#invalidkmskeyidexception)
- [InvalidLookupAttributesException](./client.md#invalidlookupattributesexception)
- [InvalidMaxResultsException](./client.md#invalidmaxresultsexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterCombinationException](./client.md#invalidparametercombinationexception)
- [InvalidS3BucketNameException](./client.md#invalids3bucketnameexception)
- [InvalidS3PrefixException](./client.md#invalids3prefixexception)
- [InvalidSnsTopicNameException](./client.md#invalidsnstopicnameexception)
- [InvalidTagParameterException](./client.md#invalidtagparameterexception)
- [InvalidTimeRangeException](./client.md#invalidtimerangeexception)
- [InvalidTokenException](./client.md#invalidtokenexception)
- [InvalidTrailNameException](./client.md#invalidtrailnameexception)
- [KmsException](./client.md#kmsexception)
- [KmsKeyDisabledException](./client.md#kmskeydisabledexception)
- [KmsKeyNotFoundException](./client.md#kmskeynotfoundexception)
- [MaximumNumberOfTrailsExceededException](./client.md#maximumnumberoftrailsexceededexception)
- [NotOrganizationMasterAccountException](./client.md#notorganizationmasteraccountexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [OrganizationNotInAllFeaturesModeException](./client.md#organizationnotinallfeaturesmodeexception)
- [OrganizationsNotInUseException](./client.md#organizationsnotinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceTypeNotSupportedException](./client.md#resourcetypenotsupportedexception)
- [S3BucketDoesNotExistException](./client.md#s3bucketdoesnotexistexception)
- [TagsLimitExceededException](./client.md#tagslimitexceededexception)
- [TrailAlreadyExistsException](./client.md#trailalreadyexistsexception)
- [TrailNotFoundException](./client.md#trailnotfoundexception)
- [TrailNotProvidedException](./client.md#trailnotprovidedexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cloudtrail").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cloudtrail.paginators import ListPublicKeysPaginator, ...
```

- [ListPublicKeysPaginator](./paginators.md#listpublickeyspaginator)
- [ListTagsPaginator](./paginators.md#listtagspaginator)
- [ListTrailsPaginator](./paginators.md#listtrailspaginator)
- [LookupEventsPaginator](./paginators.md#lookupeventspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudtrail.literals import EventCategory, ...
```

- [EventCategory](./literals.md#eventcategory)
- [InsightType](./literals.md#insighttype)
- [ListPublicKeysPaginatorName](./literals.md#listpublickeyspaginatorname)
- [ListTagsPaginatorName](./literals.md#listtagspaginatorname)
- [ListTrailsPaginatorName](./literals.md#listtrailspaginatorname)
- [LookupAttributeKey](./literals.md#lookupattributekey)
- [LookupEventsPaginatorName](./literals.md#lookupeventspaginatorname)
- [ReadWriteType](./literals.md#readwritetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudtrail.type_defs import AdvancedEventSelectorTypeDef, ...
```

- [AdvancedEventSelectorTypeDef](./type_defs.md#advancedeventselectortypedef)
- [AdvancedFieldSelectorTypeDef](./type_defs.md#advancedfieldselectortypedef)
- [DataResourceTypeDef](./type_defs.md#dataresourcetypedef)
- [EventSelectorTypeDef](./type_defs.md#eventselectortypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [InsightSelectorTypeDef](./type_defs.md#insightselectortypedef)
- [PublicKeyTypeDef](./type_defs.md#publickeytypedef)
- [ResourceTagTypeDef](./type_defs.md#resourcetagtypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TrailInfoTypeDef](./type_defs.md#trailinfotypedef)
- [TrailTypeDef](./type_defs.md#trailtypedef)
- [CreateTrailResponseTypeDef](./type_defs.md#createtrailresponsetypedef)
- [DescribeTrailsResponseTypeDef](./type_defs.md#describetrailsresponsetypedef)
- [GetEventSelectorsResponseTypeDef](./type_defs.md#geteventselectorsresponsetypedef)
- [GetInsightSelectorsResponseTypeDef](./type_defs.md#getinsightselectorsresponsetypedef)
- [GetTrailResponseTypeDef](./type_defs.md#gettrailresponsetypedef)
- [GetTrailStatusResponseTypeDef](./type_defs.md#gettrailstatusresponsetypedef)
- [ListPublicKeysResponseTypeDef](./type_defs.md#listpublickeysresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [ListTrailsResponseTypeDef](./type_defs.md#listtrailsresponsetypedef)
- [LookupAttributeTypeDef](./type_defs.md#lookupattributetypedef)
- [LookupEventsResponseTypeDef](./type_defs.md#lookupeventsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutEventSelectorsResponseTypeDef](./type_defs.md#puteventselectorsresponsetypedef)
- [PutInsightSelectorsResponseTypeDef](./type_defs.md#putinsightselectorsresponsetypedef)
- [UpdateTrailResponseTypeDef](./type_defs.md#updatetrailresponsetypedef)
