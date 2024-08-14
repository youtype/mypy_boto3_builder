# ShapeParser

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](./index.md#parsers) / ShapeParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.shape_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py) module.

## ShapeParser

[Show source in shape_parser.py:81](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L81)

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

### ShapeParser._get_streaming_body

[Show source in shape_parser.py:470](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L470)

Get the streaming member's shape if any; or None otherwise.

#### Signature

```python
@staticmethod
def _get_streaming_body(shape: Shape) -> Shape | None: ...
```

### ShapeParser().fix_method_arguments_for_mypy

[Show source in shape_parser.py:1085](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L1085)

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

[Show source in shape_parser.py:1024](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L1024)

Fix typed dict names to avoid duplicates.

#### Signature

```python
def fix_typed_dict_names(self) -> None: ...
```

### ShapeParser().get_client_method_map

[Show source in shape_parser.py:246](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L246)

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

[Show source in shape_parser.py:942](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L942)

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

[Show source in shape_parser.py:904](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L904)

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

[Show source in shape_parser.py:575](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L575)

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

[Show source in shape_parser.py:164](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L164)

Get available paginator names.

#### Returns

A list of paginator names.

#### Signature

```python
def get_paginator_names(self) -> list[str]: ...
```

### ShapeParser().get_resource_identifier_attributes

[Show source in shape_parser.py:745](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L745)

Get attributes for Resource identifiers.

#### Arguments

- [ShapeParser().resource_name](#shapeparserresource_name) - Resource name.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_resource_identifier_attributes(self, resource_name: str) -> list[Attribute]: ...
```

#### See also

- [Attribute](../structures/attribute.md#attribute)

### ShapeParser().get_resource_method_map

[Show source in shape_parser.py:763](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L763)

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

[Show source in shape_parser.py:707](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L707)

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

[Show source in shape_parser.py:631](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L631)

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

[Show source in shape_parser.py:518](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L518)

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
    is_output: bool = False,
    is_output_child: bool = False,
    is_streaming: bool = False,
) -> FakeAnnotation: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ShapeParser().resource_name

[Show source in shape_parser.py:121](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L121)

Parsed resource name.

#### Signature

```python
@property
def resource_name(self) -> str: ...
```



## ShapeParserError

[Show source in shape_parser.py:75](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L75)

Main error for ShapeParser.

#### Signature

```python
class ShapeParserError(Exception): ...
```
