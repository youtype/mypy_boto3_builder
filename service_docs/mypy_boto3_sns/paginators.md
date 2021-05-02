# Paginators for boto3 SNS module

> [Index](../index.md) > [SNS](./index.md) > Paginators

Auto-generated documentation for [SNS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS)
type annotations stubs module [mypy_boto3_sns](https://pypi.org/project/mypy-boto3-sns/).

- [Paginators for boto3 SNS module](#paginators-for-boto3-sns-module)
  - [ListEndpointsByPlatformApplicationPaginator](#listendpointsbyplatformapplicationpaginator)
  - [ListPhoneNumbersOptedOutPaginator](#listphonenumbersoptedoutpaginator)
  - [ListPlatformApplicationsPaginator](#listplatformapplicationspaginator)
  - [ListSubscriptionsPaginator](#listsubscriptionspaginator)
  - [ListSubscriptionsByTopicPaginator](#listsubscriptionsbytopicpaginator)
  - [ListTopicsPaginator](#listtopicspaginator)

## ListEndpointsByPlatformApplicationPaginator

Type annotations for `boto3.client("sns").get_paginator("list_endpoints_by_platform_application")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListEndpointsByPlatformApplicationPaginator

def get_list_endpoints_by_platform_application_paginator() -> ListEndpointsByPlatformApplicationPaginator:
    return boto3.client("sns").get_paginator("list_endpoints_by_platform_application")
```

[Paginator.ListEndpointsByPlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)

```python
class ListEndpointsByPlatformApplicationPaginator(Boto3Paginator):
    def paginate(
        self,
        PlatformApplicationArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointsByPlatformApplicationResponseTypeDef]:
        pass
```
## ListPhoneNumbersOptedOutPaginator

Type annotations for `boto3.client("sns").get_paginator("list_phone_numbers_opted_out")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListPhoneNumbersOptedOutPaginator

def get_list_phone_numbers_opted_out_paginator() -> ListPhoneNumbersOptedOutPaginator:
    return boto3.client("sns").get_paginator("list_phone_numbers_opted_out")
```

[Paginator.ListPhoneNumbersOptedOut documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)

```python
class ListPhoneNumbersOptedOutPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPhoneNumbersOptedOutResponseTypeDef]:
        pass
```
## ListPlatformApplicationsPaginator

Type annotations for `boto3.client("sns").get_paginator("list_platform_applications")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListPlatformApplicationsPaginator

def get_list_platform_applications_paginator() -> ListPlatformApplicationsPaginator:
    return boto3.client("sns").get_paginator("list_platform_applications")
```

[Paginator.ListPlatformApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)

```python
class ListPlatformApplicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPlatformApplicationsResponseTypeDef]:
        pass
```
## ListSubscriptionsPaginator

Type annotations for `boto3.client("sns").get_paginator("list_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListSubscriptionsPaginator

def get_list_subscriptions_paginator() -> ListSubscriptionsPaginator:
    return boto3.client("sns").get_paginator("list_subscriptions")
```

[Paginator.ListSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListSubscriptions)

```python
class ListSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionsResponseTypeDef]:
        pass
```
## ListSubscriptionsByTopicPaginator

Type annotations for `boto3.client("sns").get_paginator("list_subscriptions_by_topic")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListSubscriptionsByTopicPaginator

def get_list_subscriptions_by_topic_paginator() -> ListSubscriptionsByTopicPaginator:
    return boto3.client("sns").get_paginator("list_subscriptions_by_topic")
```

[Paginator.ListSubscriptionsByTopic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)

```python
class ListSubscriptionsByTopicPaginator(Boto3Paginator):
    def paginate(
        self,
        TopicArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionsByTopicResponseTypeDef]:
        pass
```
## ListTopicsPaginator

Type annotations for `boto3.client("sns").get_paginator("list_topics")`.

Can be used directly:

```python
from mypy_boto3_sns.paginators import ListTopicsPaginator

def get_list_topics_paginator() -> ListTopicsPaginator:
    return boto3.client("sns").get_paginator("list_topics")
```

[Paginator.ListTopics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Paginator.ListTopics)

```python
class ListTopicsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicsResponseTypeDef]:
        pass
```