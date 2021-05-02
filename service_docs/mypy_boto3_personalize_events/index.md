# Type annotations for boto3 PersonalizeEvents module

> [Index](../index.md) > PersonalizeEvents

Auto-generated documentation for [PersonalizeEvents](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents)
type annotations stubs module [mypy_boto3_personalize_events](https://pypi.org/project/mypy-boto3-personalize-events/).

```bash
pip install mypy-boto3-personalize-events
```

- [Type annotations for boto3 PersonalizeEvents module](#type-annotations-for-boto3-personalizeevents-module)
  - [PersonalizeEventsClient](#personalizeeventsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## PersonalizeEventsClient

Type annotations for  `boto3.client("personalize-events")` as [PersonalizeEventsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_personalize_events.client import PersonalizeEventsClient
```


PersonalizeEventsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [put_events](./client.md#put-events)
- [put_items](./client.md#put-items)
- [put_users](./client.md#put-users)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidInputException](./client.md#invalidinputexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_personalize_events.type_defs import EventTypeDef, ...
```

- [EventTypeDef](./type_defs.md#eventtypedef)
- [ItemTypeDef](./type_defs.md#itemtypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
