# SNSClient for boto3 SNS module

> [Index](../index.md) > [SNS](./index.md) > SNSClient

Auto-generated documentation for [SNS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS)
type annotations stubs module [mypy_boto3_sns](https://pypi.org/project/mypy-boto3-sns/).

- [SNSClient for boto3 SNS module](#snsclient-for-boto3-sns-module)
  - [SNSClient](#snsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_permission](#add_permission)
    - [can_paginate](#can_paginate)
    - [check_if_phone_number_is_opted_out](#check_if_phone_number_is_opted_out)
    - [confirm_subscription](#confirm_subscription)
    - [create_platform_application](#create_platform_application)
    - [create_platform_endpoint](#create_platform_endpoint)
    - [create_topic](#create_topic)
    - [delete_endpoint](#delete_endpoint)
    - [delete_platform_application](#delete_platform_application)
    - [delete_topic](#delete_topic)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_endpoint_attributes](#get_endpoint_attributes)
    - [get_platform_application_attributes](#get_platform_application_attributes)
    - [get_sms_attributes](#get_sms_attributes)
    - [get_subscription_attributes](#get_subscription_attributes)
    - [get_topic_attributes](#get_topic_attributes)
    - [list_endpoints_by_platform_application](#list_endpoints_by_platform_application)
    - [list_phone_numbers_opted_out](#list_phone_numbers_opted_out)
    - [list_platform_applications](#list_platform_applications)
    - [list_subscriptions](#list_subscriptions)
    - [list_subscriptions_by_topic](#list_subscriptions_by_topic)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_topics](#list_topics)
    - [opt_in_phone_number](#opt_in_phone_number)
    - [publish](#publish)
    - [remove_permission](#remove_permission)
    - [set_endpoint_attributes](#set_endpoint_attributes)
    - [set_platform_application_attributes](#set_platform_application_attributes)
    - [set_sms_attributes](#set_sms_attributes)
    - [set_subscription_attributes](#set_subscription_attributes)
    - [set_topic_attributes](#set_topic_attributes)
    - [subscribe](#subscribe)
    - [tag_resource](#tag_resource)
    - [unsubscribe](#unsubscribe)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)

## SNSClient

Type annotations for `boto3.client("sns")`

Can be used directly:

```python
from mypy_boto3_sns.client import SNSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sns.client import Exceptions

def handle_error(exc: Exceptions.AuthorizationErrorException) -> None:
    ...
```


Exceptions:

- `Exceptions.AuthorizationErrorException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentAccessException`
- `Exceptions.EndpointDisabledException`
- `Exceptions.FilterPolicyLimitExceededException`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidSecurityException`
- `Exceptions.KMSAccessDeniedException`
- `Exceptions.KMSDisabledException`
- `Exceptions.KMSInvalidStateException`
- `Exceptions.KMSNotFoundException`
- `Exceptions.KMSOptInRequired`
- `Exceptions.KMSThrottlingException`
- `Exceptions.NotFoundException`
- `Exceptions.PlatformApplicationDisabledException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.StaleTagException`
- `Exceptions.SubscriptionLimitExceededException`
- `Exceptions.TagLimitExceededException`
- `Exceptions.TagPolicyException`
- `Exceptions.ThrottledException`
- `Exceptions.TopicLimitExceededException`


## Methods


### add_permission

Type annotations for `boto3.client("sns").add_permission` method.

[Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.add_permission)

```python
def add_permission(
    self,
    TopicArn: str,
    Label: str,
    AWSAccountId: List[str],
    ActionName: List[str]
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("sns").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### check_if_phone_number_is_opted_out

Type annotations for `boto3.client("sns").check_if_phone_number_is_opted_out` method.

[Client.check_if_phone_number_is_opted_out documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.check_if_phone_number_is_opted_out)

```python
def check_if_phone_number_is_opted_out(
    self,
    phoneNumber: str
) -> CheckIfPhoneNumberIsOptedOutResponseTypeDef:
    pass
```

### confirm_subscription

Type annotations for `boto3.client("sns").confirm_subscription` method.

[Client.confirm_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.confirm_subscription)

```python
def confirm_subscription(
    self,
    TopicArn: str,
    Token: str,
    AuthenticateOnUnsubscribe: str = None
) -> ConfirmSubscriptionResponseTypeDef:
    pass
```

### create_platform_application

Type annotations for `boto3.client("sns").create_platform_application` method.

[Client.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.create_platform_application)

```python
def create_platform_application(
    self,
    Name: str,
    Platform: str,
    Attributes: Dict[str, str]
) -> CreatePlatformApplicationResponseTypeDef:
    pass
```

### create_platform_endpoint

Type annotations for `boto3.client("sns").create_platform_endpoint` method.

[Client.create_platform_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.create_platform_endpoint)

```python
def create_platform_endpoint(
    self,
    PlatformApplicationArn: str,
    Token: str,
    CustomUserData: str = None,
    Attributes: Dict[str, str] = None
) -> CreateEndpointResponseTypeDef:
    pass
```

### create_topic

Type annotations for `boto3.client("sns").create_topic` method.

[Client.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.create_topic)

```python
def create_topic(
    self,
    Name: str,
    Attributes: Dict[str, str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTopicResponseTypeDef:
    pass
```

### delete_endpoint

Type annotations for `boto3.client("sns").delete_endpoint` method.

[Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.delete_endpoint)

```python
def delete_endpoint(
    self,
    EndpointArn: str
) -> None:
    pass
```

### delete_platform_application

Type annotations for `boto3.client("sns").delete_platform_application` method.

[Client.delete_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.delete_platform_application)

```python
def delete_platform_application(
    self,
    PlatformApplicationArn: str
) -> None:
    pass
```

### delete_topic

Type annotations for `boto3.client("sns").delete_topic` method.

[Client.delete_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.delete_topic)

```python
def delete_topic(
    self,
    TopicArn: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sns").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_endpoint_attributes

Type annotations for `boto3.client("sns").get_endpoint_attributes` method.

[Client.get_endpoint_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.get_endpoint_attributes)

```python
def get_endpoint_attributes(
    self,
    EndpointArn: str
) -> GetEndpointAttributesResponseTypeDef:
    pass
```

### get_platform_application_attributes

Type annotations for `boto3.client("sns").get_platform_application_attributes` method.

[Client.get_platform_application_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.get_platform_application_attributes)

```python
def get_platform_application_attributes(
    self,
    PlatformApplicationArn: str
) -> GetPlatformApplicationAttributesResponseTypeDef:
    pass
```

### get_sms_attributes

Type annotations for `boto3.client("sns").get_sms_attributes` method.

[Client.get_sms_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.get_sms_attributes)

```python
def get_sms_attributes(
    self,
    attributes: List[str] = None
) -> GetSMSAttributesResponseTypeDef:
    pass
```

### get_subscription_attributes

Type annotations for `boto3.client("sns").get_subscription_attributes` method.

[Client.get_subscription_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.get_subscription_attributes)

```python
def get_subscription_attributes(
    self,
    SubscriptionArn: str
) -> GetSubscriptionAttributesResponseTypeDef:
    pass
```

### get_topic_attributes

Type annotations for `boto3.client("sns").get_topic_attributes` method.

[Client.get_topic_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.get_topic_attributes)

```python
def get_topic_attributes(
    self,
    TopicArn: str
) -> GetTopicAttributesResponseTypeDef:
    pass
```

### list_endpoints_by_platform_application

Type annotations for `boto3.client("sns").list_endpoints_by_platform_application` method.

[Client.list_endpoints_by_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_endpoints_by_platform_application)

```python
def list_endpoints_by_platform_application(
    self,
    PlatformApplicationArn: str,
    NextToken: str = None
) -> ListEndpointsByPlatformApplicationResponseTypeDef:
    pass
```

### list_phone_numbers_opted_out

Type annotations for `boto3.client("sns").list_phone_numbers_opted_out` method.

[Client.list_phone_numbers_opted_out documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_phone_numbers_opted_out)

```python
def list_phone_numbers_opted_out(
    self,
    nextToken: str = None
) -> ListPhoneNumbersOptedOutResponseTypeDef:
    pass
```

### list_platform_applications

Type annotations for `boto3.client("sns").list_platform_applications` method.

[Client.list_platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_platform_applications)

```python
def list_platform_applications(
    self,
    NextToken: str = None
) -> ListPlatformApplicationsResponseTypeDef:
    pass
```

### list_subscriptions

Type annotations for `boto3.client("sns").list_subscriptions` method.

[Client.list_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_subscriptions)

```python
def list_subscriptions(
    self,
    NextToken: str = None
) -> ListSubscriptionsResponseTypeDef:
    pass
```

### list_subscriptions_by_topic

Type annotations for `boto3.client("sns").list_subscriptions_by_topic` method.

[Client.list_subscriptions_by_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_subscriptions_by_topic)

```python
def list_subscriptions_by_topic(
    self,
    TopicArn: str,
    NextToken: str = None
) -> ListSubscriptionsByTopicResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("sns").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_topics

Type annotations for `boto3.client("sns").list_topics` method.

[Client.list_topics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.list_topics)

```python
def list_topics(
    self,
    NextToken: str = None
) -> ListTopicsResponseTypeDef:
    pass
```

### opt_in_phone_number

Type annotations for `boto3.client("sns").opt_in_phone_number` method.

[Client.opt_in_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.opt_in_phone_number)

```python
def opt_in_phone_number(
    self,
    phoneNumber: str
) -> Dict[str, Any]:
    pass
```

### publish

Type annotations for `boto3.client("sns").publish` method.

[Client.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.publish)

```python
def publish(
    self,
    Message: str,
    TopicArn: str = None,
    TargetArn: str = None,
    PhoneNumber: str = None,
    Subject: str = None,
    MessageStructure: str = None,
    MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
    MessageDeduplicationId: str = None,
    MessageGroupId: str = None
) -> PublishResponseTypeDef:
    pass
```

### remove_permission

Type annotations for `boto3.client("sns").remove_permission` method.

[Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.remove_permission)

```python
def remove_permission(
    self,
    TopicArn: str,
    Label: str
) -> None:
    pass
```

### set_endpoint_attributes

Type annotations for `boto3.client("sns").set_endpoint_attributes` method.

[Client.set_endpoint_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.set_endpoint_attributes)

```python
def set_endpoint_attributes(
    self,
    EndpointArn: str,
    Attributes: Dict[str, str]
) -> None:
    pass
```

### set_platform_application_attributes

Type annotations for `boto3.client("sns").set_platform_application_attributes` method.

[Client.set_platform_application_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.set_platform_application_attributes)

```python
def set_platform_application_attributes(
    self,
    PlatformApplicationArn: str,
    Attributes: Dict[str, str]
) -> None:
    pass
```

### set_sms_attributes

Type annotations for `boto3.client("sns").set_sms_attributes` method.

[Client.set_sms_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.set_sms_attributes)

```python
def set_sms_attributes(
    self,
    attributes: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### set_subscription_attributes

Type annotations for `boto3.client("sns").set_subscription_attributes` method.

[Client.set_subscription_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.set_subscription_attributes)

```python
def set_subscription_attributes(
    self,
    SubscriptionArn: str,
    AttributeName: str,
    AttributeValue: str = None
) -> None:
    pass
```

### set_topic_attributes

Type annotations for `boto3.client("sns").set_topic_attributes` method.

[Client.set_topic_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.set_topic_attributes)

```python
def set_topic_attributes(
    self,
    TopicArn: str,
    AttributeName: str,
    AttributeValue: str = None
) -> None:
    pass
```

### subscribe

Type annotations for `boto3.client("sns").subscribe` method.

[Client.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.subscribe)

```python
def subscribe(
    self,
    TopicArn: str,
    Protocol: str,
    Endpoint: str = None,
    Attributes: Dict[str, str] = None,
    ReturnSubscriptionArn: bool = None
) -> SubscribeResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("sns").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### unsubscribe

Type annotations for `boto3.client("sns").unsubscribe` method.

[Client.unsubscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.unsubscribe)

```python
def unsubscribe(
    self,
    SubscriptionArn: str
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("sns").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("sns").get_paginator` method.

[Paginator.ListEndpointsByPlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)

```python
@overload
def get_paginator(
    self,
    operation_name: ListEndpointsByPlatformApplicationPaginatorName
) -> ListEndpointsByPlatformApplicationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("sns").get_paginator` method.

[Paginator.ListPhoneNumbersOptedOut documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPhoneNumbersOptedOutPaginatorName
) -> ListPhoneNumbersOptedOutPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("sns").get_paginator` method.

[Paginator.ListPlatformApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)

```python
@overload
def get_paginator(
    self,
    operation_name: ListPlatformApplicationsPaginatorName
) -> ListPlatformApplicationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("sns").get_paginator` method.

[Paginator.ListSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListSubscriptions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSubscriptionsPaginatorName
) -> ListSubscriptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("sns").get_paginator` method.

[Paginator.ListSubscriptionsByTopic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSubscriptionsByTopicPaginatorName
) -> ListSubscriptionsByTopicPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("sns").get_paginator` method.

[Paginator.ListTopics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListTopics)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTopicsPaginatorName
) -> ListTopicsPaginator:
    pass
```