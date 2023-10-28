# Client

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Client

> Auto-generated documentation for [mypy_boto3_builder.parsers.client](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/client.py) module.

## parse_client

[Show source in client.py:26](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/client.py#L26)

Parse boto3 client to a structure.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

Client structure.

#### Signature

```python
def parse_client(
    session: Session, service_name: ServiceName, shape_parser: ShapeParser
) -> Client: ...
```

#### See also

- [Client](../structures/client.md#client)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](./shape_parser.md#shapeparser)
