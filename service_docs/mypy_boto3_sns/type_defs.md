# Structures for boto3 SNS module

> [Index](../index.md) > [SNS](./index.md) > Structures

Auto-generated documentation for [SNS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#SNS)
type annotations stubs module [mypy_boto3_sns](https://pypi.org/project/mypy-boto3-sns/).

- [Structures for boto3 SNS module](#structures-for-boto3-sns-module)
  - [CheckIfPhoneNumberIsOptedOutResponseTypeDef](#checkifphonenumberisoptedoutresponsetypedef)
  - [ConfirmSubscriptionResponseTypeDef](#confirmsubscriptionresponsetypedef)
  - [CreateEndpointResponseTypeDef](#createendpointresponsetypedef)
  - [CreatePlatformApplicationResponseTypeDef](#createplatformapplicationresponsetypedef)
  - [CreateTopicResponseTypeDef](#createtopicresponsetypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [GetEndpointAttributesResponseTypeDef](#getendpointattributesresponsetypedef)
  - [GetPlatformApplicationAttributesResponseTypeDef](#getplatformapplicationattributesresponsetypedef)
  - [GetSMSAttributesResponseTypeDef](#getsmsattributesresponsetypedef)
  - [GetSubscriptionAttributesResponseTypeDef](#getsubscriptionattributesresponsetypedef)
  - [GetTopicAttributesResponseTypeDef](#gettopicattributesresponsetypedef)
  - [ListEndpointsByPlatformApplicationResponseTypeDef](#listendpointsbyplatformapplicationresponsetypedef)
  - [ListPhoneNumbersOptedOutResponseTypeDef](#listphonenumbersoptedoutresponsetypedef)
  - [ListPlatformApplicationsResponseTypeDef](#listplatformapplicationsresponsetypedef)
  - [ListSubscriptionsByTopicResponseTypeDef](#listsubscriptionsbytopicresponsetypedef)
  - [ListSubscriptionsResponseTypeDef](#listsubscriptionsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTopicsResponseTypeDef](#listtopicsresponsetypedef)
  - [MessageAttributeValueTypeDef](#messageattributevaluetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PlatformApplicationTypeDef](#platformapplicationtypedef)
  - [PublishResponseTypeDef](#publishresponsetypedef)
  - [SubscribeResponseTypeDef](#subscriberesponsetypedef)
  - [SubscriptionTypeDef](#subscriptiontypedef)
  - [TagTypeDef](#tagtypedef)
  - [TopicTypeDef](#topictypedef)

## CheckIfPhoneNumberIsOptedOutResponseTypeDef

```python
from mypy_boto3_sns.type_defs import CheckIfPhoneNumberIsOptedOutResponseTypeDef
```




Optional fields:
- `isOptedOut`: `bool`


## ConfirmSubscriptionResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ConfirmSubscriptionResponseTypeDef
```




Optional fields:
- `SubscriptionArn`: `str`


## CreateEndpointResponseTypeDef

```python
from mypy_boto3_sns.type_defs import CreateEndpointResponseTypeDef
```




Optional fields:
- `EndpointArn`: `str`


## CreatePlatformApplicationResponseTypeDef

```python
from mypy_boto3_sns.type_defs import CreatePlatformApplicationResponseTypeDef
```




Optional fields:
- `PlatformApplicationArn`: `str`


## CreateTopicResponseTypeDef

```python
from mypy_boto3_sns.type_defs import CreateTopicResponseTypeDef
```




Optional fields:
- `TopicArn`: `str`


## EndpointTypeDef

```python
from mypy_boto3_sns.type_defs import EndpointTypeDef
```




Optional fields:
- `EndpointArn`: `str`
- `Attributes`: `Dict[str, str]`


## GetEndpointAttributesResponseTypeDef

```python
from mypy_boto3_sns.type_defs import GetEndpointAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`


## GetPlatformApplicationAttributesResponseTypeDef

```python
from mypy_boto3_sns.type_defs import GetPlatformApplicationAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`


## GetSMSAttributesResponseTypeDef

```python
from mypy_boto3_sns.type_defs import GetSMSAttributesResponseTypeDef
```




Optional fields:
- `attributes`: `Dict[str, str]`


## GetSubscriptionAttributesResponseTypeDef

```python
from mypy_boto3_sns.type_defs import GetSubscriptionAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`


## GetTopicAttributesResponseTypeDef

```python
from mypy_boto3_sns.type_defs import GetTopicAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, str]`


## ListEndpointsByPlatformApplicationResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListEndpointsByPlatformApplicationResponseTypeDef
```




Optional fields:
- `Endpoints`: `List["EndpointTypeDef"]`
- `NextToken`: `str`


## ListPhoneNumbersOptedOutResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListPhoneNumbersOptedOutResponseTypeDef
```




Optional fields:
- `phoneNumbers`: `List[str]`
- `nextToken`: `str`


## ListPlatformApplicationsResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListPlatformApplicationsResponseTypeDef
```




Optional fields:
- `PlatformApplications`: `List["PlatformApplicationTypeDef"]`
- `NextToken`: `str`


## ListSubscriptionsByTopicResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListSubscriptionsByTopicResponseTypeDef
```




Optional fields:
- `Subscriptions`: `List["SubscriptionTypeDef"]`
- `NextToken`: `str`


## ListSubscriptionsResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListSubscriptionsResponseTypeDef
```




Optional fields:
- `Subscriptions`: `List["SubscriptionTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListTopicsResponseTypeDef

```python
from mypy_boto3_sns.type_defs import ListTopicsResponseTypeDef
```




Optional fields:
- `Topics`: `List["TopicTypeDef"]`
- `NextToken`: `str`


## MessageAttributeValueTypeDef

```python
from mypy_boto3_sns.type_defs import MessageAttributeValueTypeDef
```


Required fields:
- `DataType`: `str`



Optional fields:
- `StringValue`: `str`
- `BinaryValue`: `Union[bytes, IO[bytes]]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sns.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PlatformApplicationTypeDef

```python
from mypy_boto3_sns.type_defs import PlatformApplicationTypeDef
```




Optional fields:
- `PlatformApplicationArn`: `str`
- `Attributes`: `Dict[str, str]`


## PublishResponseTypeDef

```python
from mypy_boto3_sns.type_defs import PublishResponseTypeDef
```




Optional fields:
- `MessageId`: `str`
- `SequenceNumber`: `str`


## SubscribeResponseTypeDef

```python
from mypy_boto3_sns.type_defs import SubscribeResponseTypeDef
```




Optional fields:
- `SubscriptionArn`: `str`


## SubscriptionTypeDef

```python
from mypy_boto3_sns.type_defs import SubscriptionTypeDef
```




Optional fields:
- `SubscriptionArn`: `str`
- `Owner`: `str`
- `Protocol`: `str`
- `Endpoint`: `str`
- `TopicArn`: `str`


## TagTypeDef

```python
from mypy_boto3_sns.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TopicTypeDef

```python
from mypy_boto3_sns.type_defs import TopicTypeDef
```




Optional fields:
- `TopicArn`: `str`

