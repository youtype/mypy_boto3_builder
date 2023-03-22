# Boto3 Utils

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
Boto3 Utils

> Auto-generated documentation for [mypy_boto3_builder.utils.boto3_utils](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_utils.py) module.

## get_boto3_client

[Show source in boto3_utils.py:35](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_utils.py#L35)

Get boto3 client from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 client.

#### Signature

```python
@cache
def get_boto3_client(session: Session, service_name: ServiceName) -> BaseClient:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)



## get_boto3_resource

[Show source in boto3_utils.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_utils.py#L50)

Get boto3 resource from `session`.

#### Arguments

- `session` - boto3 session.
- `service_name` - ServiceName instance.

#### Returns

Boto3 resource or None.

#### Signature

```python
@cache
def get_boto3_resource(
    session: Session, service_name: ServiceName
) -> Boto3ServiceResource | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)



## get_boto3_session

[Show source in boto3_utils.py:18](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_utils.py#L18)

Create and cache boto3 session.

#### Signature

```python
@cache
def get_boto3_session() -> Session:
    ...
```



## get_botocore_session

[Show source in boto3_utils.py:28](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_utils.py#L28)

Get botocore session from boto3 session.

#### Signature

```python
def get_botocore_session(session: Session) -> BotocoreSession:
    ...
```



## get_region_name_literal

[Show source in boto3_utils.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_utils.py#L68)

Get Literal with all regions.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

TypeLiteral for region names.

#### Signature

```python
def get_region_name_literal(
    session: Session, service_names: Iterable[ServiceName]
) -> TypeLiteral | None:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
