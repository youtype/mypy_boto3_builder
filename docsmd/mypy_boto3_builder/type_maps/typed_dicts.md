# Typed Dicts

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Maps](./index.md#type-maps) / Typed Dicts

> Auto-generated documentation for [mypy_boto3_builder.type_maps.typed_dicts](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/typed_dicts.py) module.

#### Attributes

- `CopySourceTypeDef` - s3: TypeTypedDict('CopySourceTypeDef', [TypedDictAttribute('Bucket', Type.str, True), TypedDictAttribute('Key', Type.str, True), TypedDictAttribute('VersionId', Type.str, False)])

- `TagTypeDef` - ec2: TypeTypedDict('TagTypeDef', [TypedDictAttribute('Key', Type.str, False), TypedDictAttribute('Value', Type.str, False)])

- `EmptyResponseMetadataTypeDef` - dynamodb: TypeTypedDict('EmptyResponseMetadataTypeDef', [TypedDictAttribute('ResponseMetadata', ResponseMetadataTypeDef, True)])

- `AttributeValueTypeDef`: `TypeTypedDict` - dynamodb: TypeTypedDict('AttributeValueTypeDef', [TypedDictAttribute('S', Type.str, False), TypedDictAttribute('N', Type.str, False), TypedDictAttribute('B', Type.bytes, False), TypedDictAttribute('SS', TypeSubscript(Type.Sequence, [Type.str]), False), TypedDictAttribute('NS', TypeSubscript(Type.Sequence, [Type.str]), False), TypedDictAttribute('BS', TypeSubscript(Type.Sequence, [Type.bytes]), False), TypedDictAttribute('M', Type.MappingStrAny, False), TypedDictAttribute('L', Type.SequenceAny, False), TypedDictAttribute('NULL', Type.bool, False), TypedDictAttribute('BOOL', Type.bool, False)])

- `GetTemplateOutputTypeDef` - cloudformation: TypeTypedDict('GetTemplateOutputTypeDef', [TypedDictAttribute('TemplateBody', Type.DictStrAny, True), TypedDictAttribute('StagesAvailable', TypeSubscript(Type.List, [InternalImport(name='TemplateStageType', module_name=ServiceModuleName.literals)]), True), TypedDictAttribute('ResponseMetadata', ResponseMetadataTypeDef, True)])

- `PolicyDocumentStatementTypeDef` - iam: TypeTypedDict('PolicyDocumentStatementTypeDef', [TypedDictAttribute('Effect', Type.str, True), TypedDictAttribute('Resource', TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True), TypedDictAttribute('Sid', Type.str, True), TypedDictAttribute('Action', TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True)])

- `CloudwatchEventStateTypeDef` - cloudwatch events: TypeTypedDict('CloudwatchEventStateTypeDef', [TypedDictAttribute('reason', Type.str, False), TypedDictAttribute('reasonData', Type.str, False), TypedDictAttribute('timestamp', Type.str, True), TypedDictAttribute('value', Type.str, True), TypedDictAttribute('actionsSuppressedBy', Type.str, False), TypedDictAttribute('actionsSuppressedReason', Type.str, False)])
