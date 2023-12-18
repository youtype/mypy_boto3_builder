# ShapeParser

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
ShapeParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.shape_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py) module.

## ShapeParser

[Show source in shape_parser.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L73)

Parser for botocore shape files.

#### Arguments

- `session` - Boto3 session.
- `service_name` - ServiceName.

#### Signature

```python
class ShapeParser:
    def __init__(self, session: Session, service_name: ServiceName): ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### ShapeParser().fix_method_arguments_for_mypy

[Show source in shape_parser.py:992](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L992)

Accept both input and output shapes in method arguments.

mypy does not compare TypedDicts, so we need to accept both input and output shapes.
https://github.com/youtype/mypy_boto3_builder/issues/209

#### Signature

```python
def fix_method_arguments_for_mypy(self, methods: Sequence[Method]) -> None: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().fix_typed_dict_names

[Show source in shape_parser.py:919](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L919)

Fix typed dict names to avoid duplicates.

#### Signature

```python
def fix_typed_dict_names(self) -> None: ...
```

### ShapeParser().get_client_method_map

[Show source in shape_parser.py:237](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L237)

Get client methods from shape.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_client_method_map(self) -> dict[str, Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_collection_batch_methods

[Show source in shape_parser.py:844](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L844)

Get batch operations for Resource collection.

#### Arguments

- `name` - Collection record name.
- `collection` - Boto3 Collection.
- `class_type` - Collection self type annotation.

#### Returns

List of Method records.

#### Signature

```python
def get_collection_batch_methods(
    self, name: str, collection: Collection
) -> list[Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_collection_filter_method

[Show source in shape_parser.py:806](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L806)

Get `filter` classmethod for Resource collection.

#### Arguments

- `name` - Collection record name.
- `collection` - Boto3 Collection.
- `class_type` - Collection class type annotation.

#### Returns

Filter Method record.

#### Signature

```python
def get_collection_filter_method(
    self, name: str, collection: Collection, self_type: FakeAnnotation
) -> Method: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](../structures/method.md#method)

### ShapeParser().get_paginate_method

[Show source in shape_parser.py:546](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L546)

Get Paginator `paginate` method.

#### Arguments

- `paginator_name` - Paginator name.

#### Returns

Method.

#### Signature

```python
def get_paginate_method(self, paginator_name: str) -> Method: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_paginator_names

[Show source in shape_parser.py:155](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L155)

Get available paginator names.

#### Returns

A list of paginator names.

#### Signature

```python
def get_paginator_names(self) -> list[str]: ...
```

### ShapeParser().get_resource_method_map

[Show source in shape_parser.py:670](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L670)

Get methods for Resource.

#### Arguments

- [ShapeParser().resource_name](#shapeparserresource_name) - Resource name.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_resource_method_map(self, resource_name: str) -> dict[str, Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_service_resource_method_map

[Show source in shape_parser.py:635](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L635)

Get methods for ServiceResource.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_service_resource_method_map(self) -> dict[str, Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_wait_method

[Show source in shape_parser.py:602](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L602)

Get Waiter `wait` method.

#### Arguments

- `waiter_name` - Waiter name.

#### Returns

Method.

#### Signature

```python
def get_wait_method(self, waiter_name: str) -> Method: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().parse_shape

[Show source in shape_parser.py:464](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L464)

Parse any botocore shape to TypeAnnotation.

#### Arguments

- `shape` - Botocore shape.
- `output` - Whether shape should use strict output types.
- `output_child` - Whether shape parent is marked as output.
- `is_streaming` - Whether shape should be streaming.

#### Returns

TypeAnnotation or similar class.

#### Signature

```python
def parse_shape(
    self,
    shape: Shape,
    output: bool = False,
    output_child: bool = False,
    is_streaming: bool = False,
) -> FakeAnnotation: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ShapeParser().resource_name

[Show source in shape_parser.py:113](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L113)

Parsed resource name.

#### Signature

```python
@property
def resource_name(self) -> str: ...
```



## ShapeParserError

[Show source in shape_parser.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L67)

Main error for ShapeParser.

#### Signature

```python
class ShapeParserError(Exception): ...
```
