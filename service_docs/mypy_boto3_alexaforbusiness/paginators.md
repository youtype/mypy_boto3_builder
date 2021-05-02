# Paginators for boto3 AlexaForBusiness module

> [Index](../index.md) > [AlexaForBusiness](./index.md) > Paginators

Auto-generated documentation for [AlexaForBusiness](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness)
type annotations stubs module [mypy_boto3_alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/).

- [Paginators for boto3 AlexaForBusiness module](#paginators-for-boto3-alexaforbusiness-module)
  - [ListBusinessReportSchedulesPaginator](#listbusinessreportschedulespaginator)
  - [ListConferenceProvidersPaginator](#listconferenceproviderspaginator)
  - [ListDeviceEventsPaginator](#listdeviceeventspaginator)
  - [ListSkillsPaginator](#listskillspaginator)
  - [ListSkillsStoreCategoriesPaginator](#listskillsstorecategoriespaginator)
  - [ListSkillsStoreSkillsByCategoryPaginator](#listskillsstoreskillsbycategorypaginator)
  - [ListSmartHomeAppliancesPaginator](#listsmarthomeappliancespaginator)
  - [ListTagsPaginator](#listtagspaginator)
  - [SearchDevicesPaginator](#searchdevicespaginator)
  - [SearchProfilesPaginator](#searchprofilespaginator)
  - [SearchRoomsPaginator](#searchroomspaginator)
  - [SearchSkillGroupsPaginator](#searchskillgroupspaginator)
  - [SearchUsersPaginator](#searchuserspaginator)

## ListBusinessReportSchedulesPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_business_report_schedules")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListBusinessReportSchedulesPaginator

def get_list_business_report_schedules_paginator() -> ListBusinessReportSchedulesPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_business_report_schedules")
```

[Paginator.ListBusinessReportSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules)

```python
class ListBusinessReportSchedulesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBusinessReportSchedulesResponseTypeDef]:
        pass
```
## ListConferenceProvidersPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_conference_providers")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListConferenceProvidersPaginator

def get_list_conference_providers_paginator() -> ListConferenceProvidersPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_conference_providers")
```

[Paginator.ListConferenceProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders)

```python
class ListConferenceProvidersPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConferenceProvidersResponseTypeDef]:
        pass
```
## ListDeviceEventsPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_device_events")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListDeviceEventsPaginator

def get_list_device_events_paginator() -> ListDeviceEventsPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_device_events")
```

[Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents)

```python
class ListDeviceEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        DeviceArn: str,
        EventType: DeviceEventType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceEventsResponseTypeDef]:
        pass
```
## ListSkillsPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_skills")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListSkillsPaginator

def get_list_skills_paginator() -> ListSkillsPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_skills")
```

[Paginator.ListSkills documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills)

```python
class ListSkillsPaginator(Boto3Paginator):
    def paginate(
        self,
        SkillGroupArn: str = None,
        EnablementType: EnablementTypeFilter = None,
        SkillType: SkillTypeFilter = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSkillsResponseTypeDef]:
        pass
```
## ListSkillsStoreCategoriesPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_skills_store_categories")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListSkillsStoreCategoriesPaginator

def get_list_skills_store_categories_paginator() -> ListSkillsStoreCategoriesPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_skills_store_categories")
```

[Paginator.ListSkillsStoreCategories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories)

```python
class ListSkillsStoreCategoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSkillsStoreCategoriesResponseTypeDef]:
        pass
```
## ListSkillsStoreSkillsByCategoryPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_skills_store_skills_by_category")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListSkillsStoreSkillsByCategoryPaginator

def get_list_skills_store_skills_by_category_paginator() -> ListSkillsStoreSkillsByCategoryPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_skills_store_skills_by_category")
```

[Paginator.ListSkillsStoreSkillsByCategory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory)

```python
class ListSkillsStoreSkillsByCategoryPaginator(Boto3Paginator):
    def paginate(
        self,
        CategoryId: int,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSkillsStoreSkillsByCategoryResponseTypeDef]:
        pass
```
## ListSmartHomeAppliancesPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_smart_home_appliances")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListSmartHomeAppliancesPaginator

def get_list_smart_home_appliances_paginator() -> ListSmartHomeAppliancesPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_smart_home_appliances")
```

[Paginator.ListSmartHomeAppliances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances)

```python
class ListSmartHomeAppliancesPaginator(Boto3Paginator):
    def paginate(
        self,
        RoomArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSmartHomeAppliancesResponseTypeDef]:
        pass
```
## ListTagsPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("list_tags")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListTagsPaginator

def get_list_tags_paginator() -> ListTagsPaginator:
    return boto3.client("alexaforbusiness").get_paginator("list_tags")
```

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags)

```python
class ListTagsPaginator(Boto3Paginator):
    def paginate(
        self,
        Arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        pass
```
## SearchDevicesPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("search_devices")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import SearchDevicesPaginator

def get_search_devices_paginator() -> SearchDevicesPaginator:
    return boto3.client("alexaforbusiness").get_paginator("search_devices")
```

[Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices)

```python
class SearchDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDevicesResponseTypeDef]:
        pass
```
## SearchProfilesPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("search_profiles")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import SearchProfilesPaginator

def get_search_profiles_paginator() -> SearchProfilesPaginator:
    return boto3.client("alexaforbusiness").get_paginator("search_profiles")
```

[Paginator.SearchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles)

```python
class SearchProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchProfilesResponseTypeDef]:
        pass
```
## SearchRoomsPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("search_rooms")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import SearchRoomsPaginator

def get_search_rooms_paginator() -> SearchRoomsPaginator:
    return boto3.client("alexaforbusiness").get_paginator("search_rooms")
```

[Paginator.SearchRooms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms)

```python
class SearchRoomsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchRoomsResponseTypeDef]:
        pass
```
## SearchSkillGroupsPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("search_skill_groups")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import SearchSkillGroupsPaginator

def get_search_skill_groups_paginator() -> SearchSkillGroupsPaginator:
    return boto3.client("alexaforbusiness").get_paginator("search_skill_groups")
```

[Paginator.SearchSkillGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups)

```python
class SearchSkillGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSkillGroupsResponseTypeDef]:
        pass
```
## SearchUsersPaginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator("search_users")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import SearchUsersPaginator

def get_search_users_paginator() -> SearchUsersPaginator:
    return boto3.client("alexaforbusiness").get_paginator("search_users")
```

[Paginator.SearchUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers)

```python
class SearchUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortCriteria: List[SortTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchUsersResponseTypeDef]:
        pass
```