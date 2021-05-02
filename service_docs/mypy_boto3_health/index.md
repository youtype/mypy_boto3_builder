# Type annotations for boto3 Health module

> [Index](../index.md) > Health

Auto-generated documentation for [Health](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health)
type annotations stubs module [mypy_boto3_health](https://pypi.org/project/mypy-boto3-health/).

```bash
pip install mypy-boto3-health
```

- [Type annotations for boto3 Health module](#type-annotations-for-boto3-health-module)
  - [HealthClient](#healthclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## HealthClient

Type annotations for  `boto3.client("health")` as [HealthClient](./client.md)

Can be used directly:

```python
from mypy_boto3_health.client import HealthClient
```


HealthClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_affected_accounts_for_organization](./client.md#describe-affected-accounts-for-organization)
- [describe_affected_entities](./client.md#describe-affected-entities)
- [describe_affected_entities_for_organization](./client.md#describe-affected-entities-for-organization)
- [describe_entity_aggregates](./client.md#describe-entity-aggregates)
- [describe_event_aggregates](./client.md#describe-event-aggregates)
- [describe_event_details](./client.md#describe-event-details)
- [describe_event_details_for_organization](./client.md#describe-event-details-for-organization)
- [describe_event_types](./client.md#describe-event-types)
- [describe_events](./client.md#describe-events)
- [describe_events_for_organization](./client.md#describe-events-for-organization)
- [describe_health_service_status_for_organization](./client.md#describe-health-service-status-for-organization)
- [disable_health_service_access_for_organization](./client.md#disable-health-service-access-for-organization)
- [enable_health_service_access_for_organization](./client.md#enable-health-service-access-for-organization)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InvalidPaginationToken](./client.md#invalidpaginationtoken)
- [UnsupportedLocale](./client.md#unsupportedlocale)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("health").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_health.paginators import DescribeAffectedAccountsForOrganizationPaginator, ...
```

- [DescribeAffectedAccountsForOrganizationPaginator](./paginators.md#describeaffectedaccountsfororganizationpaginator)
- [DescribeAffectedEntitiesPaginator](./paginators.md#describeaffectedentitiespaginator)
- [DescribeAffectedEntitiesForOrganizationPaginator](./paginators.md#describeaffectedentitiesfororganizationpaginator)
- [DescribeEventAggregatesPaginator](./paginators.md#describeeventaggregatespaginator)
- [DescribeEventTypesPaginator](./paginators.md#describeeventtypespaginator)
- [DescribeEventsPaginator](./paginators.md#describeeventspaginator)
- [DescribeEventsForOrganizationPaginator](./paginators.md#describeeventsfororganizationpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_health.literals import DescribeAffectedAccountsForOrganizationPaginatorName, ...
```

- [DescribeAffectedAccountsForOrganizationPaginatorName](./literals.md#describeaffectedaccountsfororganizationpaginatorname)
- [DescribeAffectedEntitiesForOrganizationPaginatorName](./literals.md#describeaffectedentitiesfororganizationpaginatorname)
- [DescribeAffectedEntitiesPaginatorName](./literals.md#describeaffectedentitiespaginatorname)
- [DescribeEventAggregatesPaginatorName](./literals.md#describeeventaggregatespaginatorname)
- [DescribeEventTypesPaginatorName](./literals.md#describeeventtypespaginatorname)
- [DescribeEventsForOrganizationPaginatorName](./literals.md#describeeventsfororganizationpaginatorname)
- [DescribeEventsPaginatorName](./literals.md#describeeventspaginatorname)
- [entityStatusCode](./literals.md#entitystatuscode)
- [eventAggregateField](./literals.md#eventaggregatefield)
- [eventScopeCode](./literals.md#eventscopecode)
- [eventStatusCode](./literals.md#eventstatuscode)
- [eventTypeCategory](./literals.md#eventtypecategory)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_health.type_defs import AffectedEntityTypeDef, ...
```

- [AffectedEntityTypeDef](./type_defs.md#affectedentitytypedef)
- [DateTimeRangeTypeDef](./type_defs.md#datetimerangetypedef)
- [EntityAggregateTypeDef](./type_defs.md#entityaggregatetypedef)
- [EventAggregateTypeDef](./type_defs.md#eventaggregatetypedef)
- [EventDescriptionTypeDef](./type_defs.md#eventdescriptiontypedef)
- [EventDetailsErrorItemTypeDef](./type_defs.md#eventdetailserroritemtypedef)
- [EventDetailsTypeDef](./type_defs.md#eventdetailstypedef)
- [EventTypeDef](./type_defs.md#eventtypedef)
- [EventTypeTypeDef](./type_defs.md#eventtypetypedef)
- [OrganizationAffectedEntitiesErrorItemTypeDef](./type_defs.md#organizationaffectedentitieserroritemtypedef)
- [OrganizationEventDetailsErrorItemTypeDef](./type_defs.md#organizationeventdetailserroritemtypedef)
- [OrganizationEventDetailsTypeDef](./type_defs.md#organizationeventdetailstypedef)
- [OrganizationEventTypeDef](./type_defs.md#organizationeventtypedef)
- [DescribeAffectedAccountsForOrganizationResponseTypeDef](./type_defs.md#describeaffectedaccountsfororganizationresponsetypedef)
- [DescribeAffectedEntitiesForOrganizationResponseTypeDef](./type_defs.md#describeaffectedentitiesfororganizationresponsetypedef)
- [DescribeAffectedEntitiesResponseTypeDef](./type_defs.md#describeaffectedentitiesresponsetypedef)
- [DescribeEntityAggregatesResponseTypeDef](./type_defs.md#describeentityaggregatesresponsetypedef)
- [DescribeEventAggregatesResponseTypeDef](./type_defs.md#describeeventaggregatesresponsetypedef)
- [DescribeEventDetailsForOrganizationResponseTypeDef](./type_defs.md#describeeventdetailsfororganizationresponsetypedef)
- [DescribeEventDetailsResponseTypeDef](./type_defs.md#describeeventdetailsresponsetypedef)
- [DescribeEventTypesResponseTypeDef](./type_defs.md#describeeventtypesresponsetypedef)
- [DescribeEventsForOrganizationResponseTypeDef](./type_defs.md#describeeventsfororganizationresponsetypedef)
- [DescribeEventsResponseTypeDef](./type_defs.md#describeeventsresponsetypedef)
- [DescribeHealthServiceStatusForOrganizationResponseTypeDef](./type_defs.md#describehealthservicestatusfororganizationresponsetypedef)
- [EntityFilterTypeDef](./type_defs.md#entityfiltertypedef)
- [EventAccountFilterTypeDef](./type_defs.md#eventaccountfiltertypedef)
- [EventFilterTypeDef](./type_defs.md#eventfiltertypedef)
- [EventTypeFilterTypeDef](./type_defs.md#eventtypefiltertypedef)
- [OrganizationEventFilterTypeDef](./type_defs.md#organizationeventfiltertypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
