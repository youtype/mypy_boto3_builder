# SNSServiceResource for boto3 SNS module

> [Index](../index.md) > [SNS](./index.md) > SNSServiceResource

Auto-generated documentation for [SNS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS)
type annotations stubs module [mypy_boto3_sns](https://pypi.org/project/mypy-boto3-sns/).

- [SNSServiceResource for boto3 SNS module](#snsserviceresource-for-boto3-sns-module)
  - [SNSServiceResource](#snsserviceresource)
  - [Methods](#methods)
    - [SNSServiceResource.PlatformApplication](#snsserviceresourceplatformapplication)
    - [SNSServiceResource.PlatformEndpoint](#snsserviceresourceplatformendpoint)
    - [SNSServiceResource.Subscription](#snsserviceresourcesubscription)
    - [SNSServiceResource.Topic](#snsserviceresourcetopic)
    - [SNSServiceResource.create_platform_application](#snsserviceresourcecreate_platform_application)
    - [SNSServiceResource.create_topic](#snsserviceresourcecreate_topic)
    - [SNSServiceResource.get_available_subresources](#snsserviceresourceget_available_subresources)
  - [Collections](#collections)
    - [SNSServiceResource.platform_applications](#snsserviceresourceplatform_applications)
    - [SNSServiceResource.subscriptions](#snsserviceresourcesubscriptions)
    - [SNSServiceResource.topics](#snsserviceresourcetopics)
  - [PlatformApplication](#platformapplication)
    - [PlatformApplication attributes](#platformapplication-attributes)
    - [PlatformApplication methods](#platformapplication-methods)
    - [PlatformApplication collections](#platformapplication-collections)
  - [PlatformEndpoint](#platformendpoint)
    - [PlatformEndpoint attributes](#platformendpoint-attributes)
    - [PlatformEndpoint methods](#platformendpoint-methods)
  - [Subscription](#subscription)
    - [Subscription attributes](#subscription-attributes)
    - [Subscription methods](#subscription-methods)
  - [Topic](#topic)
    - [Topic attributes](#topic-attributes)
    - [Topic methods](#topic-methods)
    - [Topic collections](#topic-collections)

## SNSServiceResource

Type annotations for `boto3.resource("sns")`, included resources and collections.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import SNSServiceResource
```



## Methods

### SNSServiceResource.PlatformApplication

Type annotations for `boto3.resource("sns").PlatformApplication` method.

[ServiceResource.PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)

Definition:

```python
def PlatformApplication(
    self,
    arn: str
) -> _PlatformApplication:
    pass
```

### SNSServiceResource.PlatformEndpoint

Type annotations for `boto3.resource("sns").PlatformEndpoint` method.

[ServiceResource.PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)

Definition:

```python
def PlatformEndpoint(
    self,
    arn: str
) -> _PlatformEndpoint:
    pass
```

### SNSServiceResource.Subscription

Type annotations for `boto3.resource("sns").Subscription` method.

[ServiceResource.Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Subscription)

Definition:

```python
def Subscription(
    self,
    arn: str
) -> _Subscription:
    pass
```

### SNSServiceResource.Topic

Type annotations for `boto3.resource("sns").Topic` method.

[ServiceResource.Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Topic)

Definition:

```python
def Topic(
    self,
    arn: str
) -> _Topic:
    pass
```

### SNSServiceResource.create_platform_application

Type annotations for `boto3.resource("sns").create_platform_application` method.

[ServiceResource.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.create_platform_application)

Definition:

```python
def create_platform_application(
    self,
    Name: str,
    Platform: str,
    Attributes: Dict[str, str]
) -> _PlatformApplication:
    pass
```

### SNSServiceResource.create_topic

Type annotations for `boto3.resource("sns").create_topic` method.

[ServiceResource.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.create_topic)

Definition:

```python
def create_topic(
    self,
    Name: str,
    Attributes: Dict[str, str] = None,
    Tags: List["TagTypeDef"] = None
) -> _Topic:
    pass
```

### SNSServiceResource.get_available_subresources

Type annotations for `boto3.resource("sns").get_available_subresources` method.

[ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)

Definition:

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```




## Collections

### SNSServiceResource.platform_applications

Type annotations for `boto3.resource("sns").platform_applications` collection.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import ServiceResourcePlatformApplicationsCollection,

def get_collection() -> ServiceResourcePlatformApplicationsCollection:
    return boto3.resource("sns").platform_applications(
        ...
    )
```

[ServiceResource.platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.platform_applications)

Definition:

```python
class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def filter(  # type: ignore
        self,
        NextToken: str = None
    ) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourcePlatformApplicationsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["PlatformApplication"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["PlatformApplication"]:
        pass
```

### SNSServiceResource.subscriptions

Type annotations for `boto3.resource("sns").subscriptions` collection.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import ServiceResourceSubscriptionsCollection,

def get_collection() -> ServiceResourceSubscriptionsCollection:
    return boto3.resource("sns").subscriptions(
        ...
    )
```

[ServiceResource.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.subscriptions)

Definition:

```python
class ServiceResourceSubscriptionsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceSubscriptionsCollection":
        pass

    def filter(  # type: ignore
        self,
        NextToken: str = None
    ) -> "ServiceResourceSubscriptionsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceSubscriptionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceSubscriptionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Subscription"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Subscription"]:
        pass
```

### SNSServiceResource.topics

Type annotations for `boto3.resource("sns").topics` collection.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import ServiceResourceTopicsCollection,

def get_collection() -> ServiceResourceTopicsCollection:
    return boto3.resource("sns").topics(
        ...
    )
```

[ServiceResource.topics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.topics)

Definition:

```python
class ServiceResourceTopicsCollection(ResourceCollection):
    def all(
        self
    ) -> "ServiceResourceTopicsCollection":
        pass

    def filter(  # type: ignore
        self,
        NextToken: str = None
    ) -> "ServiceResourceTopicsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "ServiceResourceTopicsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "ServiceResourceTopicsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Topic"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Topic"]:
        pass
```




## PlatformApplication

Type annotations for `boto3.resource("sns").PlatformApplication` class.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import PlatformApplication

def get_resource() -> PlatformApplication:
    return boto3.resource("sns").PlatformApplication(...)
```

[PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)


### PlatformApplication attributes


- `attributes`: `Dict[str, Any]`

- `arn`: `str`

- `endpoints`: `PlatformApplicationEndpointsCollection`




### PlatformApplication methods


#### PlatformApplication.create_platform_endpoint

Type annotations for `boto3.resource("sns").create_platform_endpoint` method.

[PlatformApplication.create_platform_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.create_platform_endpoint)

```python
def create_platform_endpoint(
    self,
    Token: str,
    CustomUserData: str = None,
    Attributes: Dict[str, str] = None
) -> _PlatformEndpoint:
    pass
```

#### PlatformApplication.delete

Type annotations for `boto3.resource("sns").delete` method.

[PlatformApplication.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### PlatformApplication.get_available_subresources

Type annotations for `boto3.resource("sns").get_available_subresources` method.

[PlatformApplication.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### PlatformApplication.load

Type annotations for `boto3.resource("sns").load` method.

[PlatformApplication.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.load)

```python
def load(
    self
) -> None:
    pass
```

#### PlatformApplication.reload

Type annotations for `boto3.resource("sns").reload` method.

[PlatformApplication.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### PlatformApplication.set_attributes

Type annotations for `boto3.resource("sns").set_attributes` method.

[PlatformApplication.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.set_attributes)

```python
def set_attributes(
    self,
    Attributes: Dict[str, str]
) -> None:
    pass
```




### PlatformApplication collections


#### PlatformApplication.endpoints

Type annotations for `boto3.resource("sns").PlatformApplication(...).endpoints` collection.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import PlatformApplicationEndpointsCollection,

def get_collection() -> PlatformApplicationEndpointsCollection:
    resource = boto3.resource("sns").PlatformApplication(...)
    return resource.endpoints
```

[PlatformApplication.endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformApplication.endpoints)

```python
class PlatformApplicationEndpointsCollection(ResourceCollection):
    def all(
        self
    ) -> "PlatformApplicationEndpointsCollection":
        pass

    def filter(  # type: ignore
        self,
        NextToken: str = None
    ) -> "PlatformApplicationEndpointsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "PlatformApplicationEndpointsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "PlatformApplicationEndpointsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["PlatformEndpoint"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["PlatformEndpoint"]:
        pass
```




## PlatformEndpoint

Type annotations for `boto3.resource("sns").PlatformEndpoint` class.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import PlatformEndpoint

def get_resource() -> PlatformEndpoint:
    return boto3.resource("sns").PlatformEndpoint(...)
```

[PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)


### PlatformEndpoint attributes


- `attributes`: `Dict[str, Any]`

- `arn`: `str`




### PlatformEndpoint methods


#### PlatformEndpoint.delete

Type annotations for `boto3.resource("sns").delete` method.

[PlatformEndpoint.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### PlatformEndpoint.get_available_subresources

Type annotations for `boto3.resource("sns").get_available_subresources` method.

[PlatformEndpoint.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### PlatformEndpoint.load

Type annotations for `boto3.resource("sns").load` method.

[PlatformEndpoint.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.load)

```python
def load(
    self
) -> None:
    pass
```

#### PlatformEndpoint.publish

Type annotations for `boto3.resource("sns").publish` method.

[PlatformEndpoint.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.publish)

```python
def publish(
    self,
    Message: str,
    TopicArn: str = None,
    PhoneNumber: str = None,
    Subject: str = None,
    MessageStructure: str = None,
    MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
    MessageDeduplicationId: str = None,
    MessageGroupId: str = None
) -> PublishResponseTypeDef:
    pass
```

#### PlatformEndpoint.reload

Type annotations for `boto3.resource("sns").reload` method.

[PlatformEndpoint.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### PlatformEndpoint.set_attributes

Type annotations for `boto3.resource("sns").set_attributes` method.

[PlatformEndpoint.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.PlatformEndpoint.set_attributes)

```python
def set_attributes(
    self,
    Attributes: Dict[str, str]
) -> None:
    pass
```






## Subscription

Type annotations for `boto3.resource("sns").Subscription` class.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import Subscription

def get_resource() -> Subscription:
    return boto3.resource("sns").Subscription(...)
```

[Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Subscription)


### Subscription attributes


- `attributes`: `Dict[str, Any]`

- `arn`: `str`




### Subscription methods


#### Subscription.delete

Type annotations for `boto3.resource("sns").delete` method.

[Subscription.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Subscription.get_available_subresources

Type annotations for `boto3.resource("sns").get_available_subresources` method.

[Subscription.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Subscription.load

Type annotations for `boto3.resource("sns").load` method.

[Subscription.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.load)

```python
def load(
    self
) -> None:
    pass
```

#### Subscription.reload

Type annotations for `boto3.resource("sns").reload` method.

[Subscription.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Subscription.set_attributes

Type annotations for `boto3.resource("sns").set_attributes` method.

[Subscription.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Subscription.set_attributes)

```python
def set_attributes(
    self,
    AttributeName: str,
    AttributeValue: str = None
) -> None:
    pass
```






## Topic

Type annotations for `boto3.resource("sns").Topic` class.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import Topic

def get_resource() -> Topic:
    return boto3.resource("sns").Topic(...)
```

[Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.ServiceResource.Topic)


### Topic attributes


- `attributes`: `Dict[str, Any]`

- `arn`: `str`

- `subscriptions`: `TopicSubscriptionsCollection`




### Topic methods


#### Topic.add_permission

Type annotations for `boto3.resource("sns").add_permission` method.

[Topic.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.add_permission)

```python
def add_permission(
    self,
    Label: str,
    AWSAccountId: List[str],
    ActionName: List[str]
) -> None:
    pass
```

#### Topic.confirm_subscription

Type annotations for `boto3.resource("sns").confirm_subscription` method.

[Topic.confirm_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.confirm_subscription)

```python
def confirm_subscription(
    self,
    Token: str,
    AuthenticateOnUnsubscribe: str = None
) -> _Subscription:
    pass
```

#### Topic.delete

Type annotations for `boto3.resource("sns").delete` method.

[Topic.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.delete)

```python
def delete(
    self
) -> None:
    pass
```

#### Topic.get_available_subresources

Type annotations for `boto3.resource("sns").get_available_subresources` method.

[Topic.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.get_available_subresources)

```python
def get_available_subresources(
    self
) -> List[str]:
    pass
```

#### Topic.load

Type annotations for `boto3.resource("sns").load` method.

[Topic.load documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.load)

```python
def load(
    self
) -> None:
    pass
```

#### Topic.publish

Type annotations for `boto3.resource("sns").publish` method.

[Topic.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.publish)

```python
def publish(
    self,
    Message: str,
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

#### Topic.reload

Type annotations for `boto3.resource("sns").reload` method.

[Topic.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.reload)

```python
def reload(
    self
) -> None:
    pass
```

#### Topic.remove_permission

Type annotations for `boto3.resource("sns").remove_permission` method.

[Topic.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.remove_permission)

```python
def remove_permission(
    self,
    Label: str
) -> None:
    pass
```

#### Topic.set_attributes

Type annotations for `boto3.resource("sns").set_attributes` method.

[Topic.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.set_attributes)

```python
def set_attributes(
    self,
    AttributeName: str,
    AttributeValue: str = None
) -> None:
    pass
```

#### Topic.subscribe

Type annotations for `boto3.resource("sns").subscribe` method.

[Topic.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.subscribe)

```python
def subscribe(
    self,
    Protocol: str,
    Endpoint: str = None,
    Attributes: Dict[str, str] = None,
    ReturnSubscriptionArn: bool = None
) -> _Subscription:
    pass
```




### Topic collections


#### Topic.subscriptions

Type annotations for `boto3.resource("sns").Topic(...).subscriptions` collection.

Can be used directly:

```python
from mypy_boto3_sns.service_resource import TopicSubscriptionsCollection,

def get_collection() -> TopicSubscriptionsCollection:
    resource = boto3.resource("sns").Topic(...)
    return resource.subscriptions
```

[Topic.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS.Topic.subscriptions)

```python
class TopicSubscriptionsCollection(ResourceCollection):
    def all(
        self
    ) -> "TopicSubscriptionsCollection":
        pass

    def filter(  # type: ignore
        self,
        NextToken: str = None
    ) -> "TopicSubscriptionsCollection":
        pass

    def limit(
        self,
        count: int
    ) -> "TopicSubscriptionsCollection":
        pass

    def page_size(
        self,
        count: int
    ) -> "TopicSubscriptionsCollection":
        pass

    def pages(
        self
    ) -> Iterator[List["Subscription"]]:
        pass

    def __iter__(
        self
    ) -> Iterator["Subscription"]:
        pass
```


