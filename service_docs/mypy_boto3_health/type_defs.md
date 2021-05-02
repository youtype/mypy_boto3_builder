# Structures for boto3 Health module

> [Index](../index.md) > [Health](./index.md) > Structures

Auto-generated documentation for [Health](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health)
type annotations stubs module [mypy_boto3_health](https://pypi.org/project/mypy-boto3-health/).

- [Structures for boto3 Health module](#structures-for-boto3-health-module)
  - [AffectedEntityTypeDef](#affectedentitytypedef)
  - [DateTimeRangeTypeDef](#datetimerangetypedef)
  - [DescribeAffectedAccountsForOrganizationResponseTypeDef](#describeaffectedaccountsfororganizationresponsetypedef)
  - [DescribeAffectedEntitiesForOrganizationResponseTypeDef](#describeaffectedentitiesfororganizationresponsetypedef)
  - [DescribeAffectedEntitiesResponseTypeDef](#describeaffectedentitiesresponsetypedef)
  - [DescribeEntityAggregatesResponseTypeDef](#describeentityaggregatesresponsetypedef)
  - [DescribeEventAggregatesResponseTypeDef](#describeeventaggregatesresponsetypedef)
  - [DescribeEventDetailsForOrganizationResponseTypeDef](#describeeventdetailsfororganizationresponsetypedef)
  - [DescribeEventDetailsResponseTypeDef](#describeeventdetailsresponsetypedef)
  - [DescribeEventTypesResponseTypeDef](#describeeventtypesresponsetypedef)
  - [DescribeEventsForOrganizationResponseTypeDef](#describeeventsfororganizationresponsetypedef)
  - [DescribeEventsResponseTypeDef](#describeeventsresponsetypedef)
  - [DescribeHealthServiceStatusForOrganizationResponseTypeDef](#describehealthservicestatusfororganizationresponsetypedef)
  - [EntityAggregateTypeDef](#entityaggregatetypedef)
  - [EntityFilterTypeDef](#entityfiltertypedef)
  - [EventAccountFilterTypeDef](#eventaccountfiltertypedef)
  - [EventAggregateTypeDef](#eventaggregatetypedef)
  - [EventDescriptionTypeDef](#eventdescriptiontypedef)
  - [EventDetailsErrorItemTypeDef](#eventdetailserroritemtypedef)
  - [EventDetailsTypeDef](#eventdetailstypedef)
  - [EventFilterTypeDef](#eventfiltertypedef)
  - [EventTypeDef](#eventtypedef)
  - [EventTypeFilterTypeDef](#eventtypefiltertypedef)
  - [EventTypeTypeDef](#eventtypetypedef)
  - [OrganizationAffectedEntitiesErrorItemTypeDef](#organizationaffectedentitieserroritemtypedef)
  - [OrganizationEventDetailsErrorItemTypeDef](#organizationeventdetailserroritemtypedef)
  - [OrganizationEventDetailsTypeDef](#organizationeventdetailstypedef)
  - [OrganizationEventFilterTypeDef](#organizationeventfiltertypedef)
  - [OrganizationEventTypeDef](#organizationeventtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## AffectedEntityTypeDef

```python
from mypy_boto3_health.type_defs import AffectedEntityTypeDef
```




Optional fields:
- `entityArn`: `str`
- `eventArn`: `str`
- `entityValue`: `str`
- `entityUrl`: `str`
- `awsAccountId`: `str`
- `lastUpdatedTime`: `datetime`
- `statusCode`: `entityStatusCode`
- `tags`: `Dict[str, str]`


## DateTimeRangeTypeDef

```python
from mypy_boto3_health.type_defs import DateTimeRangeTypeDef
```




Optional fields:
- `from`: `datetime`
- `to`: `datetime`


## DescribeAffectedAccountsForOrganizationResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeAffectedAccountsForOrganizationResponseTypeDef
```




Optional fields:
- `affectedAccounts`: `List[str]`
- `eventScopeCode`: `eventScopeCode`
- `nextToken`: `str`


## DescribeAffectedEntitiesForOrganizationResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeAffectedEntitiesForOrganizationResponseTypeDef
```




Optional fields:
- `entities`: `List["AffectedEntityTypeDef"]`
- `failedSet`: `List["OrganizationAffectedEntitiesErrorItemTypeDef"]`
- `nextToken`: `str`


## DescribeAffectedEntitiesResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeAffectedEntitiesResponseTypeDef
```




Optional fields:
- `entities`: `List["AffectedEntityTypeDef"]`
- `nextToken`: `str`


## DescribeEntityAggregatesResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEntityAggregatesResponseTypeDef
```




Optional fields:
- `entityAggregates`: `List["EntityAggregateTypeDef"]`


## DescribeEventAggregatesResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEventAggregatesResponseTypeDef
```




Optional fields:
- `eventAggregates`: `List["EventAggregateTypeDef"]`
- `nextToken`: `str`


## DescribeEventDetailsForOrganizationResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEventDetailsForOrganizationResponseTypeDef
```




Optional fields:
- `successfulSet`: `List["OrganizationEventDetailsTypeDef"]`
- `failedSet`: `List["OrganizationEventDetailsErrorItemTypeDef"]`


## DescribeEventDetailsResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEventDetailsResponseTypeDef
```




Optional fields:
- `successfulSet`: `List["EventDetailsTypeDef"]`
- `failedSet`: `List["EventDetailsErrorItemTypeDef"]`


## DescribeEventTypesResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEventTypesResponseTypeDef
```




Optional fields:
- `eventTypes`: `List["EventTypeTypeDef"]`
- `nextToken`: `str`


## DescribeEventsForOrganizationResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEventsForOrganizationResponseTypeDef
```




Optional fields:
- `events`: `List["OrganizationEventTypeDef"]`
- `nextToken`: `str`


## DescribeEventsResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeEventsResponseTypeDef
```




Optional fields:
- `events`: `List["EventTypeDef"]`
- `nextToken`: `str`


## DescribeHealthServiceStatusForOrganizationResponseTypeDef

```python
from mypy_boto3_health.type_defs import DescribeHealthServiceStatusForOrganizationResponseTypeDef
```




Optional fields:
- `healthServiceAccessStatusForOrganization`: `str`


## EntityAggregateTypeDef

```python
from mypy_boto3_health.type_defs import EntityAggregateTypeDef
```




Optional fields:
- `eventArn`: `str`
- `count`: `int`


## EntityFilterTypeDef

```python
from mypy_boto3_health.type_defs import EntityFilterTypeDef
```


Required fields:
- `eventArns`: `List[str]`



Optional fields:
- `entityArns`: `List[str]`
- `entityValues`: `List[str]`
- `lastUpdatedTimes`: `List["DateTimeRangeTypeDef"]`
- `tags`: `List[Dict[str, str]]`
- `statusCodes`: `List[entityStatusCode]`


## EventAccountFilterTypeDef

```python
from mypy_boto3_health.type_defs import EventAccountFilterTypeDef
```


Required fields:
- `eventArn`: `str`



Optional fields:
- `awsAccountId`: `str`


## EventAggregateTypeDef

```python
from mypy_boto3_health.type_defs import EventAggregateTypeDef
```




Optional fields:
- `aggregateValue`: `str`
- `count`: `int`


## EventDescriptionTypeDef

```python
from mypy_boto3_health.type_defs import EventDescriptionTypeDef
```




Optional fields:
- `latestDescription`: `str`


## EventDetailsErrorItemTypeDef

```python
from mypy_boto3_health.type_defs import EventDetailsErrorItemTypeDef
```




Optional fields:
- `eventArn`: `str`
- `errorName`: `str`
- `errorMessage`: `str`


## EventDetailsTypeDef

```python
from mypy_boto3_health.type_defs import EventDetailsTypeDef
```




Optional fields:
- `event`: `"EventTypeDef"`
- `eventDescription`: `"EventDescriptionTypeDef"`
- `eventMetadata`: `Dict[str, str]`


## EventFilterTypeDef

```python
from mypy_boto3_health.type_defs import EventFilterTypeDef
```




Optional fields:
- `eventArns`: `List[str]`
- `eventTypeCodes`: `List[str]`
- `services`: `List[str]`
- `regions`: `List[str]`
- `availabilityZones`: `List[str]`
- `startTimes`: `List["DateTimeRangeTypeDef"]`
- `endTimes`: `List["DateTimeRangeTypeDef"]`
- `lastUpdatedTimes`: `List["DateTimeRangeTypeDef"]`
- `entityArns`: `List[str]`
- `entityValues`: `List[str]`
- `eventTypeCategories`: `List[eventTypeCategory]`
- `tags`: `List[Dict[str, str]]`
- `eventStatusCodes`: `List[eventStatusCode]`


## EventTypeDef

```python
from mypy_boto3_health.type_defs import EventTypeDef
```




Optional fields:
- `arn`: `str`
- `service`: `str`
- `eventTypeCode`: `str`
- `eventTypeCategory`: `eventTypeCategory`
- `region`: `str`
- `availabilityZone`: `str`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `lastUpdatedTime`: `datetime`
- `statusCode`: `eventStatusCode`
- `eventScopeCode`: `eventScopeCode`


## EventTypeFilterTypeDef

```python
from mypy_boto3_health.type_defs import EventTypeFilterTypeDef
```




Optional fields:
- `eventTypeCodes`: `List[str]`
- `services`: `List[str]`
- `eventTypeCategories`: `List[eventTypeCategory]`


## EventTypeTypeDef

```python
from mypy_boto3_health.type_defs import EventTypeTypeDef
```




Optional fields:
- `service`: `str`
- `code`: `str`
- `category`: `eventTypeCategory`


## OrganizationAffectedEntitiesErrorItemTypeDef

```python
from mypy_boto3_health.type_defs import OrganizationAffectedEntitiesErrorItemTypeDef
```




Optional fields:
- `awsAccountId`: `str`
- `eventArn`: `str`
- `errorName`: `str`
- `errorMessage`: `str`


## OrganizationEventDetailsErrorItemTypeDef

```python
from mypy_boto3_health.type_defs import OrganizationEventDetailsErrorItemTypeDef
```




Optional fields:
- `awsAccountId`: `str`
- `eventArn`: `str`
- `errorName`: `str`
- `errorMessage`: `str`


## OrganizationEventDetailsTypeDef

```python
from mypy_boto3_health.type_defs import OrganizationEventDetailsTypeDef
```




Optional fields:
- `awsAccountId`: `str`
- `event`: `"EventTypeDef"`
- `eventDescription`: `"EventDescriptionTypeDef"`
- `eventMetadata`: `Dict[str, str]`


## OrganizationEventFilterTypeDef

```python
from mypy_boto3_health.type_defs import OrganizationEventFilterTypeDef
```




Optional fields:
- `eventTypeCodes`: `List[str]`
- `awsAccountIds`: `List[str]`
- `services`: `List[str]`
- `regions`: `List[str]`
- `startTime`: `"DateTimeRangeTypeDef"`
- `endTime`: `"DateTimeRangeTypeDef"`
- `lastUpdatedTime`: `"DateTimeRangeTypeDef"`
- `entityArns`: `List[str]`
- `entityValues`: `List[str]`
- `eventTypeCategories`: `List[eventTypeCategory]`
- `eventStatusCodes`: `List[eventStatusCode]`


## OrganizationEventTypeDef

```python
from mypy_boto3_health.type_defs import OrganizationEventTypeDef
```




Optional fields:
- `arn`: `str`
- `service`: `str`
- `eventTypeCode`: `str`
- `eventTypeCategory`: `eventTypeCategory`
- `eventScopeCode`: `eventScopeCode`
- `region`: `str`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `lastUpdatedTime`: `datetime`
- `statusCode`: `eventStatusCode`


## PaginatorConfigTypeDef

```python
from mypy_boto3_health.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

