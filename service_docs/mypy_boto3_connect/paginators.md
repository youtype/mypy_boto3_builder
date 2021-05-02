# Paginators for boto3 Connect module

> [Index](../index.md) > [Connect](./index.md) > Paginators

Auto-generated documentation for [Connect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect)
type annotations stubs module [mypy_boto3_connect](https://pypi.org/project/mypy-boto3-connect/).

- [Paginators for boto3 Connect module](#paginators-for-boto3-connect-module)
  - [GetMetricDataPaginator](#getmetricdatapaginator)
  - [ListApprovedOriginsPaginator](#listapprovedoriginspaginator)
  - [ListContactFlowsPaginator](#listcontactflowspaginator)
  - [ListHoursOfOperationsPaginator](#listhoursofoperationspaginator)
  - [ListInstanceAttributesPaginator](#listinstanceattributespaginator)
  - [ListInstanceStorageConfigsPaginator](#listinstancestorageconfigspaginator)
  - [ListInstancesPaginator](#listinstancespaginator)
  - [ListIntegrationAssociationsPaginator](#listintegrationassociationspaginator)
  - [ListLambdaFunctionsPaginator](#listlambdafunctionspaginator)
  - [ListLexBotsPaginator](#listlexbotspaginator)
  - [ListPhoneNumbersPaginator](#listphonenumberspaginator)
  - [ListPromptsPaginator](#listpromptspaginator)
  - [ListQueueQuickConnectsPaginator](#listqueuequickconnectspaginator)
  - [ListQueuesPaginator](#listqueuespaginator)
  - [ListQuickConnectsPaginator](#listquickconnectspaginator)
  - [ListRoutingProfileQueuesPaginator](#listroutingprofilequeuespaginator)
  - [ListRoutingProfilesPaginator](#listroutingprofilespaginator)
  - [ListSecurityKeysPaginator](#listsecuritykeyspaginator)
  - [ListSecurityProfilesPaginator](#listsecurityprofilespaginator)
  - [ListUseCasesPaginator](#listusecasespaginator)
  - [ListUserHierarchyGroupsPaginator](#listuserhierarchygroupspaginator)
  - [ListUsersPaginator](#listuserspaginator)

## GetMetricDataPaginator

Type annotations for `boto3.client("connect").get_paginator("get_metric_data")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import GetMetricDataPaginator

def get_get_metric_data_paginator() -> GetMetricDataPaginator:
    return boto3.client("connect").get_paginator("get_metric_data")
```

[Paginator.GetMetricData documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.GetMetricData)

```python
class GetMetricDataPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: FiltersTypeDef,
        HistoricalMetrics: List["HistoricalMetricTypeDef"],
        Groupings: List[Grouping] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetMetricDataResponseTypeDef]:
        pass
```
## ListApprovedOriginsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_approved_origins")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListApprovedOriginsPaginator

def get_list_approved_origins_paginator() -> ListApprovedOriginsPaginator:
    return boto3.client("connect").get_paginator("list_approved_origins")
```

[Paginator.ListApprovedOrigins documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins)

```python
class ListApprovedOriginsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApprovedOriginsResponseTypeDef]:
        pass
```
## ListContactFlowsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_contact_flows")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListContactFlowsPaginator

def get_list_contact_flows_paginator() -> ListContactFlowsPaginator:
    return boto3.client("connect").get_paginator("list_contact_flows")
```

[Paginator.ListContactFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactFlows)

```python
class ListContactFlowsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        ContactFlowTypes: List[ContactFlowType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContactFlowsResponseTypeDef]:
        pass
```
## ListHoursOfOperationsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_hours_of_operations")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListHoursOfOperationsPaginator

def get_list_hours_of_operations_paginator() -> ListHoursOfOperationsPaginator:
    return boto3.client("connect").get_paginator("list_hours_of_operations")
```

[Paginator.ListHoursOfOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)

```python
class ListHoursOfOperationsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHoursOfOperationsResponseTypeDef]:
        pass
```
## ListInstanceAttributesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_instance_attributes")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListInstanceAttributesPaginator

def get_list_instance_attributes_paginator() -> ListInstanceAttributesPaginator:
    return boto3.client("connect").get_paginator("list_instance_attributes")
```

[Paginator.ListInstanceAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes)

```python
class ListInstanceAttributesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceAttributesResponseTypeDef]:
        pass
```
## ListInstanceStorageConfigsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_instance_storage_configs")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListInstanceStorageConfigsPaginator

def get_list_instance_storage_configs_paginator() -> ListInstanceStorageConfigsPaginator:
    return boto3.client("connect").get_paginator("list_instance_storage_configs")
```

[Paginator.ListInstanceStorageConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs)

```python
class ListInstanceStorageConfigsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        ResourceType: InstanceStorageResourceType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceStorageConfigsResponseTypeDef]:
        pass
```
## ListInstancesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_instances")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListInstancesPaginator

def get_list_instances_paginator() -> ListInstancesPaginator:
    return boto3.client("connect").get_paginator("list_instances")
```

[Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstances)

```python
class ListInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        pass
```
## ListIntegrationAssociationsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_integration_associations")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListIntegrationAssociationsPaginator

def get_list_integration_associations_paginator() -> ListIntegrationAssociationsPaginator:
    return boto3.client("connect").get_paginator("list_integration_associations")
```

[Paginator.ListIntegrationAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations)

```python
class ListIntegrationAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIntegrationAssociationsResponseTypeDef]:
        pass
```
## ListLambdaFunctionsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_lambda_functions")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListLambdaFunctionsPaginator

def get_list_lambda_functions_paginator() -> ListLambdaFunctionsPaginator:
    return boto3.client("connect").get_paginator("list_lambda_functions")
```

[Paginator.ListLambdaFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions)

```python
class ListLambdaFunctionsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLambdaFunctionsResponseTypeDef]:
        pass
```
## ListLexBotsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_lex_bots")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListLexBotsPaginator

def get_list_lex_bots_paginator() -> ListLexBotsPaginator:
    return boto3.client("connect").get_paginator("list_lex_bots")
```

[Paginator.ListLexBots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLexBots)

```python
class ListLexBotsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLexBotsResponseTypeDef]:
        pass
```
## ListPhoneNumbersPaginator

Type annotations for `boto3.client("connect").get_paginator("list_phone_numbers")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListPhoneNumbersPaginator

def get_list_phone_numbers_paginator() -> ListPhoneNumbersPaginator:
    return boto3.client("connect").get_paginator("list_phone_numbers")
```

[Paginator.ListPhoneNumbers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)

```python
class ListPhoneNumbersPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[PhoneNumberType] = None,
        PhoneNumberCountryCodes: List[PhoneNumberCountryCode] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPhoneNumbersResponseTypeDef]:
        pass
```
## ListPromptsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_prompts")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListPromptsPaginator

def get_list_prompts_paginator() -> ListPromptsPaginator:
    return boto3.client("connect").get_paginator("list_prompts")
```

[Paginator.ListPrompts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPrompts)

```python
class ListPromptsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPromptsResponseTypeDef]:
        pass
```
## ListQueueQuickConnectsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_queue_quick_connects")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListQueueQuickConnectsPaginator

def get_list_queue_quick_connects_paginator() -> ListQueueQuickConnectsPaginator:
    return boto3.client("connect").get_paginator("list_queue_quick_connects")
```

[Paginator.ListQueueQuickConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects)

```python
class ListQueueQuickConnectsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        QueueId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueueQuickConnectsResponseTypeDef]:
        pass
```
## ListQueuesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_queues")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListQueuesPaginator

def get_list_queues_paginator() -> ListQueuesPaginator:
    return boto3.client("connect").get_paginator("list_queues")
```

[Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueues)

```python
class ListQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        QueueTypes: List[QueueType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueuesResponseTypeDef]:
        pass
```
## ListQuickConnectsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_quick_connects")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListQuickConnectsPaginator

def get_list_quick_connects_paginator() -> ListQuickConnectsPaginator:
    return boto3.client("connect").get_paginator("list_quick_connects")
```

[Paginator.ListQuickConnects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQuickConnects)

```python
class ListQuickConnectsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        QuickConnectTypes: List[QuickConnectType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQuickConnectsResponseTypeDef]:
        pass
```
## ListRoutingProfileQueuesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_routing_profile_queues")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListRoutingProfileQueuesPaginator

def get_list_routing_profile_queues_paginator() -> ListRoutingProfileQueuesPaginator:
    return boto3.client("connect").get_paginator("list_routing_profile_queues")
```

[Paginator.ListRoutingProfileQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues)

```python
class ListRoutingProfileQueuesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        RoutingProfileId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutingProfileQueuesResponseTypeDef]:
        pass
```
## ListRoutingProfilesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_routing_profiles")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListRoutingProfilesPaginator

def get_list_routing_profiles_paginator() -> ListRoutingProfilesPaginator:
    return boto3.client("connect").get_paginator("list_routing_profiles")
```

[Paginator.ListRoutingProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)

```python
class ListRoutingProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoutingProfilesResponseTypeDef]:
        pass
```
## ListSecurityKeysPaginator

Type annotations for `boto3.client("connect").get_paginator("list_security_keys")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListSecurityKeysPaginator

def get_list_security_keys_paginator() -> ListSecurityKeysPaginator:
    return boto3.client("connect").get_paginator("list_security_keys")
```

[Paginator.ListSecurityKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityKeys)

```python
class ListSecurityKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityKeysResponseTypeDef]:
        pass
```
## ListSecurityProfilesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_security_profiles")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListSecurityProfilesPaginator

def get_list_security_profiles_paginator() -> ListSecurityProfilesPaginator:
    return boto3.client("connect").get_paginator("list_security_profiles")
```

[Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)

```python
class ListSecurityProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesResponseTypeDef]:
        pass
```
## ListUseCasesPaginator

Type annotations for `boto3.client("connect").get_paginator("list_use_cases")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListUseCasesPaginator

def get_list_use_cases_paginator() -> ListUseCasesPaginator:
    return boto3.client("connect").get_paginator("list_use_cases")
```

[Paginator.ListUseCases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUseCases)

```python
class ListUseCasesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        IntegrationAssociationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUseCasesResponseTypeDef]:
        pass
```
## ListUserHierarchyGroupsPaginator

Type annotations for `boto3.client("connect").get_paginator("list_user_hierarchy_groups")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListUserHierarchyGroupsPaginator

def get_list_user_hierarchy_groups_paginator() -> ListUserHierarchyGroupsPaginator:
    return boto3.client("connect").get_paginator("list_user_hierarchy_groups")
```

[Paginator.ListUserHierarchyGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)

```python
class ListUserHierarchyGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUserHierarchyGroupsResponseTypeDef]:
        pass
```
## ListUsersPaginator

Type annotations for `boto3.client("connect").get_paginator("list_users")`.

Can be used directly:

```python
from mypy_boto3_connect.paginators import ListUsersPaginator

def get_list_users_paginator() -> ListUsersPaginator:
    return boto3.client("connect").get_paginator("list_users")
```

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUsers)

```python
class ListUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsersResponseTypeDef]:
        pass
```