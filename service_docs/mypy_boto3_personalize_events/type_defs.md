# Structures for boto3 PersonalizeEvents module

> [Index](../index.md) > [PersonalizeEvents](./index.md) > Structures

Auto-generated documentation for [PersonalizeEvents](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents)
type annotations stubs module [mypy_boto3_personalize_events](https://pypi.org/project/mypy-boto3-personalize-events/).

- [Structures for boto3 PersonalizeEvents module](#structures-for-boto3-personalizeevents-module)
  - [EventTypeDef](#eventtypedef)
  - [ItemTypeDef](#itemtypedef)
  - [UserTypeDef](#usertypedef)

## EventTypeDef

```python
from mypy_boto3_personalize_events.type_defs import EventTypeDef
```


Required fields:
- `eventType`: `str`
- `sentAt`: `datetime`



Optional fields:
- `eventId`: `str`
- `eventValue`: `float`
- `itemId`: `str`
- `properties`: `str`
- `recommendationId`: `str`
- `impression`: `List[str]`


## ItemTypeDef

```python
from mypy_boto3_personalize_events.type_defs import ItemTypeDef
```


Required fields:
- `itemId`: `str`



Optional fields:
- `properties`: `str`


## UserTypeDef

```python
from mypy_boto3_personalize_events.type_defs import UserTypeDef
```


Required fields:
- `userId`: `str`



Optional fields:
- `properties`: `str`

