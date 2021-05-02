# Type annotations for boto3 SNS module

> [Index](../index.md) > SNS

Auto-generated documentation for [SNS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS)
type annotations stubs module [mypy_boto3_sns](https://pypi.org/project/mypy-boto3-sns/).

```bash
pip install mypy-boto3-sns
```

- [Type annotations for boto3 SNS module](#type-annotations-for-boto3-sns-module)
  - [SNSClient](#snsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [SNSServiceResource](#snsserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SNSClient

Type annotations for  `boto3.client("sns")` as [SNSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sns.client import SNSClient
```


SNSClient [exceptions](./client.md#exceptions)



### Methods
- [add_permission](./client.md#add-permission)
- [can_paginate](./client.md#can-paginate)
- [check_if_phone_number_is_opted_out](./client.md#check-if-phone-number-is-opted-out)
- [confirm_subscription](./client.md#confirm-subscription)
- [create_platform_application](./client.md#create-platform-application)
- [create_platform_endpoint](./client.md#create-platform-endpoint)
- [create_topic](./client.md#create-topic)
- [delete_endpoint](./client.md#delete-endpoint)
- [delete_platform_application](./client.md#delete-platform-application)
- [delete_topic](./client.md#delete-topic)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_endpoint_attributes](./client.md#get-endpoint-attributes)
- [get_paginator](./client.md#get-paginator)
- [get_platform_application_attributes](./client.md#get-platform-application-attributes)
- [get_sms_attributes](./client.md#get-sms-attributes)
- [get_subscription_attributes](./client.md#get-subscription-attributes)
- [get_topic_attributes](./client.md#get-topic-attributes)
- [list_endpoints_by_platform_application](./client.md#list-endpoints-by-platform-application)
- [list_phone_numbers_opted_out](./client.md#list-phone-numbers-opted-out)
- [list_platform_applications](./client.md#list-platform-applications)
- [list_subscriptions](./client.md#list-subscriptions)
- [list_subscriptions_by_topic](./client.md#list-subscriptions-by-topic)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_topics](./client.md#list-topics)
- [opt_in_phone_number](./client.md#opt-in-phone-number)
- [publish](./client.md#publish)
- [remove_permission](./client.md#remove-permission)
- [set_endpoint_attributes](./client.md#set-endpoint-attributes)
- [set_platform_application_attributes](./client.md#set-platform-application-attributes)
- [set_sms_attributes](./client.md#set-sms-attributes)
- [set_subscription_attributes](./client.md#set-subscription-attributes)
- [set_topic_attributes](./client.md#set-topic-attributes)
- [subscribe](./client.md#subscribe)
- [tag_resource](./client.md#tag-resource)
- [unsubscribe](./client.md#unsubscribe)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AuthorizationErrorException](./client.md#authorizationerrorexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentAccessException](./client.md#concurrentaccessexception)
- [EndpointDisabledException](./client.md#endpointdisabledexception)
- [FilterPolicyLimitExceededException](./client.md#filterpolicylimitexceededexception)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidSecurityException](./client.md#invalidsecurityexception)
- [KMSAccessDeniedException](./client.md#kmsaccessdeniedexception)
- [KMSDisabledException](./client.md#kmsdisabledexception)
- [KMSInvalidStateException](./client.md#kmsinvalidstateexception)
- [KMSNotFoundException](./client.md#kmsnotfoundexception)
- [KMSOptInRequired](./client.md#kmsoptinrequired)
- [KMSThrottlingException](./client.md#kmsthrottlingexception)
- [NotFoundException](./client.md#notfoundexception)
- [PlatformApplicationDisabledException](./client.md#platformapplicationdisabledexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [StaleTagException](./client.md#staletagexception)
- [SubscriptionLimitExceededException](./client.md#subscriptionlimitexceededexception)
- [TagLimitExceededException](./client.md#taglimitexceededexception)
- [TagPolicyException](./client.md#tagpolicyexception)
- [ThrottledException](./client.md#throttledexception)
- [TopicLimitExceededException](./client.md#topiclimitexceededexception)




## SNSServiceResource

Type annotations for  `boto3.resource("sns")` as [SNSServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_sns.service_resource import SNSServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("sns").*`.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import ServiceResourcePlatformApplicationsCollection, ...
```

- [ServiceResourcePlatformApplicationsCollection](./service_resource.md#snsserviceresource.platform-applications)
- [ServiceResourceSubscriptionsCollection](./service_resource.md#snsserviceresource.subscriptions)
- [ServiceResourceTopicsCollection](./service_resource.md#snsserviceresource.topics)




### Resources

Type annotations for additional resources from `boto3.resource("sns").*`.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import PlatformApplication, ...
```

- [PlatformApplication](./service_resource.md#platformapplication)
- [PlatformEndpoint](./service_resource.md#platformendpoint)
- [Subscription](./service_resource.md#subscription)
- [Topic](./service_resource.md#topic)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sns").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListEndpointsByPlatformApplicationPaginator, ...
```

- [ListEndpointsByPlatformApplicationPaginator](./paginators.md#listendpointsbyplatformapplicationpaginator)
- [ListPhoneNumbersOptedOutPaginator](./paginators.md#listphonenumbersoptedoutpaginator)
- [ListPlatformApplicationsPaginator](./paginators.md#listplatformapplicationspaginator)
- [ListSubscriptionsPaginator](./paginators.md#listsubscriptionspaginator)
- [ListSubscriptionsByTopicPaginator](./paginators.md#listsubscriptionsbytopicpaginator)
- [ListTopicsPaginator](./paginators.md#listtopicspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sns.literals import ListEndpointsByPlatformApplicationPaginatorName, ...
```

- [ListEndpointsByPlatformApplicationPaginatorName](./literals.md#listendpointsbyplatformapplicationpaginatorname)
- [ListPhoneNumbersOptedOutPaginatorName](./literals.md#listphonenumbersoptedoutpaginatorname)
- [ListPlatformApplicationsPaginatorName](./literals.md#listplatformapplicationspaginatorname)
- [ListSubscriptionsByTopicPaginatorName](./literals.md#listsubscriptionsbytopicpaginatorname)
- [ListSubscriptionsPaginatorName](./literals.md#listsubscriptionspaginatorname)
- [ListTopicsPaginatorName](./literals.md#listtopicspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sns.type_defs import CheckIfPhoneNumberIsOptedOutResponseTypeDef, ...
```

- [CheckIfPhoneNumberIsOptedOutResponseTypeDef](./type_defs.md#checkifphonenumberisoptedoutresponsetypedef)
- [ConfirmSubscriptionResponseTypeDef](./type_defs.md#confirmsubscriptionresponsetypedef)
- [CreateEndpointResponseTypeDef](./type_defs.md#createendpointresponsetypedef)
- [CreatePlatformApplicationResponseTypeDef](./type_defs.md#createplatformapplicationresponsetypedef)
- [CreateTopicResponseTypeDef](./type_defs.md#createtopicresponsetypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [GetEndpointAttributesResponseTypeDef](./type_defs.md#getendpointattributesresponsetypedef)
- [GetPlatformApplicationAttributesResponseTypeDef](./type_defs.md#getplatformapplicationattributesresponsetypedef)
- [GetSMSAttributesResponseTypeDef](./type_defs.md#getsmsattributesresponsetypedef)
- [GetSubscriptionAttributesResponseTypeDef](./type_defs.md#getsubscriptionattributesresponsetypedef)
- [GetTopicAttributesResponseTypeDef](./type_defs.md#gettopicattributesresponsetypedef)
- [ListEndpointsByPlatformApplicationResponseTypeDef](./type_defs.md#listendpointsbyplatformapplicationresponsetypedef)
- [ListPhoneNumbersOptedOutResponseTypeDef](./type_defs.md#listphonenumbersoptedoutresponsetypedef)
- [ListPlatformApplicationsResponseTypeDef](./type_defs.md#listplatformapplicationsresponsetypedef)
- [ListSubscriptionsByTopicResponseTypeDef](./type_defs.md#listsubscriptionsbytopicresponsetypedef)
- [ListSubscriptionsResponseTypeDef](./type_defs.md#listsubscriptionsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTopicsResponseTypeDef](./type_defs.md#listtopicsresponsetypedef)
- [MessageAttributeValueTypeDef](./type_defs.md#messageattributevaluetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PlatformApplicationTypeDef](./type_defs.md#platformapplicationtypedef)
- [PublishResponseTypeDef](./type_defs.md#publishresponsetypedef)
- [SubscribeResponseTypeDef](./type_defs.md#subscriberesponsetypedef)
- [SubscriptionTypeDef](./type_defs.md#subscriptiontypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TopicTypeDef](./type_defs.md#topictypedef)
