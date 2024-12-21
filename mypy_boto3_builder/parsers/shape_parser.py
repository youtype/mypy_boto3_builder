"""
Parser for botocore shape files.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable, Sequence

from botocore.eventstream import EventStream
from botocore.model import (
    ListShape,
    MapShape,
    OperationModel,
    ServiceModel,
    Shape,
    StringShape,
    StructureShape,
)
from botocore.paginate import PageIterator

from mypy_boto3_builder.boto3_ports.model import Collection as Boto3Collection
from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.constants import (
    ATTRIBUTES,
    CLIENT,
    SERVICE_RESOURCE,
)
from mypy_boto3_builder.exceptions import ShapeParserError
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.resource_loader import ResourceLoader
from mypy_boto3_builder.parsers.shape_parser_types import (
    ActionShape,
    IdentifierShape,
    PaginatorShape,
    PaginatorsShape,
    ResourceShape,
    ResourcesShape,
    SubResourceShape,
    WaitersShape,
)
from mypy_boto3_builder.parsers.typed_dict_map import TypedDictMap
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_parent import TypeParent
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion
from mypy_boto3_builder.type_maps.argument_alias_map import get_argument_alias
from mypy_boto3_builder.type_maps.literal_type_map import get_type_literal_stub
from mypy_boto3_builder.type_maps.method_type_map import (
    get_default_value_stub,
    get_method_type_stub,
)
from mypy_boto3_builder.type_maps.required_attribute_map import is_required
from mypy_boto3_builder.type_maps.shape_type_map import (
    get_output_shape_type_stub,
    get_shape_type_stub,
)
from mypy_boto3_builder.type_maps.typed_dicts import (
    EmptyResponseMetadataTypeDef,
    PaginatorConfigTypeDef,
    ResponseMetadataTypeDef,
    WaiterConfigTypeDef,
)
from mypy_boto3_builder.utils.boto3_utils import get_botocore_session
from mypy_boto3_builder.utils.strings import (
    capitalize,
    extract_docstring_from_html,
    get_short_docstring,
    get_type_def_name,
    xform_name,
)
from mypy_boto3_builder.utils.type_checks import is_union


class ShapeParser:
    """
    Parser for botocore shape files.

    Arguments:
        service_name -- ServiceName.
    """

    def __init__(self, service_name: ServiceName) -> None:
        botocore_session = get_botocore_session()
        self._resource_loader = ResourceLoader()
        service_data = botocore_session.get_service_data(service_name.boto3_name)
        self.service_name = service_name
        self.service_model = ServiceModel(service_data, service_name.boto3_name)
        self._resource_name: str = ""
        self._type_literal_map: dict[str, TypeLiteral] = {}
        self._typed_dict_map = TypedDictMap()
        self._output_typed_dict_map = TypedDictMap()
        self._response_typed_dict_map = TypedDictMap()
        self._fixed_typed_dict_map: dict[TypeTypedDict, TypeTypedDict] = {}

        self.logger = get_logger()

    @property
    def _waiters_shape(self) -> WaitersShape | None:
        return self._resource_loader.load_waiters(self.service_name)

    @property
    def _paginators_shape(self) -> PaginatorsShape | None:
        return self._resource_loader.load_paginators(self.service_name)

    @property
    def _resources_shape(self) -> ResourcesShape | None:
        return self._resource_loader.load_resources(self.service_name)

    @property
    def resource_name(self) -> str:
        """
        Parsed resource name.
        """
        return self._resource_name

    def _get_operation(self, name: str) -> OperationModel:
        return self.service_model.operation_model(name)

    def _get_paginator(self, name: str) -> PaginatorShape:
        if not self._paginators_shape:
            raise ShapeParserError(f"Unknown paginator: {name}")
        try:
            return self._paginators_shape["pagination"][name]
        except KeyError as e:
            raise ShapeParserError(f"Unknown paginator: {name}") from e

    def has_service_resource(self) -> bool:
        """
        Check if service has ServiceResource.
        """
        return self._resource_loader.has_service_resource(self.service_name)

    def _get_service_resource(self) -> ResourceShape:
        if not self._resources_shape:
            raise ShapeParserError("Resource shape not found")
        if "service" not in self._resources_shape:
            raise ShapeParserError("Service resource shape not found")
        return self._resources_shape["service"]

    def get_subresource_names(self) -> list[str]:
        """
        Get available subresource names.
        """
        return list(self._get_subresources().keys())

    def _get_subresources(self) -> dict[str, ResourceShape]:
        if not self._resources_shape:
            return {}
        if "resources" not in self._resources_shape:
            return {}

        return self._resources_shape["resources"]

    def get_service_resource_model(self) -> ResourceModel:
        """
        Get service resource model.
        """
        if not self.has_service_resource():
            raise ShapeParserError("Service resource does not exist")
        return ResourceModel(
            name=self.service_name.boto3_name,
            definition=dict(self._get_service_resource()),
            resource_defs=self._get_subresources(),
        )

    def get_resource_model(self, resource_name: str) -> ResourceModel:
        """
        Get service resource model.
        """
        resource_defs = self._get_subresources()
        if resource_name not in resource_defs:
            raise ShapeParserError(f"Resource {resource_name} not found in subresources")
        return ResourceModel(
            name=resource_name,
            definition=dict(resource_defs[resource_name]),
            resource_defs=resource_defs,
        )

    def _get_resource_shape(self, name: str) -> ResourceShape:
        if name == SERVICE_RESOURCE:
            return self._get_service_resource()

        if not self._resources_shape or "resources" not in self._resources_shape:
            raise ShapeParserError("Resource shape not found")

        try:
            return self._resources_shape["resources"][name]
        except KeyError as e:
            raise ShapeParserError(f"Unknown resource: {name}") from e

    def get_paginator_names(self) -> list[str]:
        """
        Get available paginator names.

        Returns:
            A list of paginator names.
        """
        if not self._paginators_shape or not self._paginators_shape.get("pagination"):
            return []
        result = list(self._paginators_shape["pagination"])
        result.sort()
        return result

    def _parse_arguments(
        self,
        *,
        class_name: str,
        method_name: str,
        operation_name: str,
        shape: StructureShape,
        exclude_names: Iterable[str] = (),
        optional_only: bool = False,
    ) -> list[Argument]:
        result: list[Argument] = []
        required = shape.required_members
        for argument_name, argument_shape in shape.members.items():
            if argument_name in exclude_names:
                continue
            argument_alias = get_argument_alias(self.service_name, operation_name, argument_name)

            argument_type_stub = get_method_type_stub(
                self.service_name,
                class_name,
                method_name,
                argument_name,
            )
            if argument_type_stub is Type.RemoveArgument:
                continue
            if argument_type_stub is not None:
                argument_type = argument_type_stub
            else:
                argument_type = self.parse_shape(argument_shape)
            argument = Argument(argument_alias, argument_type)
            if argument_name not in required:
                argument.default = Type.Ellipsis
            default_value_stub = get_default_value_stub(
                self.service_name,
                class_name,
                method_name,
                argument_name,
            )
            if default_value_stub is not None:
                argument.default = default_value_stub
            if optional_only and argument.required:
                continue

            # FIXME: https://github.com/boto/boto3/issues/2813
            # if not argument.required and argument.type_annotation:
            #     argument.type_annotation = get_optional(argument.type_annotation)

            result.append(argument)

        result.sort(key=lambda x: not x.required)
        return result

    def _parse_return_type(
        self,
        class_name: str,
        method_name: str,
        shape: Shape | None,
    ) -> FakeAnnotation:
        argument_type_stub = get_method_type_stub(
            self.service_name,
            class_name,
            method_name,
            "return",
        )
        if argument_type_stub is not None:
            return argument_type_stub

        if shape:
            return self.parse_shape(shape, is_output=True)

        return Type.none

    @staticmethod
    def _get_kw_flags(method_name: str, arguments: Sequence[Argument]) -> tuple[Argument, ...]:
        if not arguments:
            return ()
        if method_name[:1].isupper():
            return ()

        return (Argument.kwflag(),)

    def get_client_method_map(self) -> dict[str, Method]:
        """
        Get client methods from shape.

        Returns:
            A map of method name to Method.
        """
        self._resource_name = CLIENT
        result: dict[str, Method] = {
            "can_paginate": Method(
                name="can_paginate",
                arguments=(Argument.self(), Argument("operation_name", Type.str)),
                return_type=Type.bool,
            ),
            "generate_presigned_url": Method(
                name="generate_presigned_url",
                arguments=(
                    Argument.self(),
                    Argument("ClientMethod", Type.str),
                    Argument("Params", Type.MappingStrAny, Type.Ellipsis),
                    Argument("ExpiresIn", Type.int, TypeConstant(3600)),
                    Argument("HttpMethod", Type.str, Type.Ellipsis),
                ),
                return_type=Type.str,
            ),
        }
        for operation_name in self.service_model.operation_names:
            operation_model = self._get_operation(operation_name)
            arguments: list[Argument] = [Argument.self()]
            method_name = xform_name(operation_name)

            if operation_model.input_shape is not None:
                shape_arguments = self._parse_arguments(
                    class_name=self._resource_name,
                    method_name=method_name,
                    operation_name=operation_name,
                    shape=operation_model.input_shape,
                )
                arguments.extend(self._get_kw_flags(method_name, shape_arguments))
                arguments.extend(shape_arguments)

            return_type = self._parse_return_type(
                self._resource_name,
                method_name,
                operation_model.output_shape,
            )
            if return_type is Type.none:
                return_type = EmptyResponseMetadataTypeDef

            method = Method(
                name=method_name,
                arguments=arguments,
                return_type=return_type,
                docstring=get_short_docstring(
                    extract_docstring_from_html(operation_model.documentation)
                ),
            )
            if operation_model.input_shape:
                method.create_request_type_annotation(
                    self._get_typed_dict_name(operation_model.input_shape, postfix="Request"),
                )
            result[method.name] = method
        return result

    @staticmethod
    def _get_typed_dict_name(shape: Shape, postfix: str = "") -> str:
        return get_type_def_name(shape.name, postfix)

    @staticmethod
    def _get_literal_name(shape: StringShape) -> str:
        # FIXME: hack for apigatewayv2
        if shape.name == "__string":
            children_name = "".join(sorted(capitalize(i) for i in shape.enum))
            return f"{children_name}Type"

        name = capitalize(shape.name.lstrip("_"))
        return f"{name}Type"

    def _parse_shape_string(self, shape: StringShape) -> FakeAnnotation:
        if shape.enum:
            literal_name = self._get_literal_name(shape)
            type_literal_stub = get_type_literal_stub(self.service_name, literal_name)
            type_literal = type_literal_stub or TypeLiteral(literal_name, set(shape.enum))
            if literal_name in self._type_literal_map:
                old_type_literal = self._type_literal_map[literal_name]
                if not type_literal.is_same(old_type_literal):
                    raise ShapeParserError(
                        f"Literal {literal_name} has different values:"
                        f" {old_type_literal.children} vs {type_literal.children}",
                    )
                return old_type_literal

            self._type_literal_map[literal_name] = type_literal
            return type_literal

        # FIXME: botocore does not always try to parse response as JSON
        # pattern = shape.metadata.get("pattern", "")
        # if pattern in (
        #     "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
        #     "^[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+$",
        # ):
        #     if output_child:
        #         return Type.DictStrAny
        #     else:
        #         return DictOrStrTypeDef

        return Type.str

    def _parse_shape_map(
        self,
        shape: MapShape,
        *,
        is_output_child: bool = False,
        is_streaming: bool = False,
    ) -> FakeAnnotation:
        parent = Type.dict if is_output_child else Type.Mapping
        key_child = (
            self.parse_shape(
                shape.key,
                is_output_child=is_output_child,
                is_streaming=is_streaming,
            )
            if shape.key
            else Type.str
        )
        value_child = (
            self.parse_shape(
                shape.value,
                is_output_child=is_output_child,
                is_streaming=is_streaming,
            )
            if shape.value
            else Type.Any
        )
        return TypeSubscript(parent, [key_child, value_child])

    def _get_typed_dict_map(self, *, output: bool, output_child: bool) -> TypedDictMap:
        if output:
            return self._response_typed_dict_map
        if output_child:
            return self._output_typed_dict_map
        return self._typed_dict_map

    def _parse_shape_structure(
        self,
        shape: StructureShape,
        *,
        output: bool = False,
        output_child: bool = False,
        is_streaming: bool = False,
    ) -> FakeAnnotation:
        if not shape.members.items():
            return Type.DictStrAny if output_child else Type.MappingStrAny

        required = shape.required_members
        is_output_or_child = output or output_child
        typed_dict_name = self._get_shape_type_name(shape)
        typed_dict = TypeTypedDict(typed_dict_name)

        typed_dict_map = self._get_typed_dict_map(output=output, output_child=output_child)
        resource_typed_dict_name = self._get_typed_dict_name(shape, postfix=self.resource_name)
        found_typed_dict = typed_dict_map.get(typed_dict.name)
        found_resource_typed_dict = typed_dict_map.get(resource_typed_dict_name)

        if found_resource_typed_dict:
            return found_resource_typed_dict

        typed_dict_map[resource_typed_dict_name] = typed_dict

        for attr_name, attr_shape in shape.members.items():
            typed_dict.add_attribute(
                attr_name,
                self.parse_shape(
                    attr_shape,
                    is_output=False,
                    is_output_child=is_output_or_child,
                    is_streaming=is_streaming,
                ),
                required=attr_name in required,
            )
        if output:
            self._mark_typed_dict_as_total(typed_dict)
            self._add_response_metadata(typed_dict)

        if found_typed_dict and not typed_dict.is_same(found_typed_dict):
            self.logger.debug(
                f"Renaming conflicting {typed_dict.name} to {resource_typed_dict_name}",
            )
            typed_dict.name = resource_typed_dict_name
        typed_dict_map[typed_dict.name] = typed_dict
        return typed_dict

    def _mark_typed_dict_as_total(self, typed_dict: TypeTypedDict) -> None:
        for attribute in typed_dict.children:
            if is_required(self.service_name, typed_dict.name, attribute.name):
                attribute.mark_as_required()
            else:
                self.logger.debug(
                    f"Leaving output {typed_dict.name}.{attribute.name}"
                    f" as {attribute.get_type_annotation().render()}",
                )

    def _add_response_metadata(self, typed_dict: TypeTypedDict) -> None:
        child_names = {i.name for i in typed_dict.children}
        if "ResponseMetadata" not in child_names:
            typed_dict.add_attribute(
                "ResponseMetadata",
                ResponseMetadataTypeDef,
                required=True,
            )

    def _parse_shape_list(
        self,
        shape: ListShape,
        *,
        is_output_child: bool = False,
    ) -> FakeAnnotation:
        type_subscript = (
            TypeSubscript(Type.list) if is_output_child else TypeSubscript(Type.Sequence)
        )
        if shape.member:
            type_subscript.add_child(
                self.parse_shape(shape.member, is_output_child=is_output_child),
            )
        else:
            type_subscript.add_child(Type.Any)
        return type_subscript

    def _get_shape_type_name(self, shape: Shape) -> str:
        if isinstance(shape, StructureShape):
            return self._get_typed_dict_name(shape)

        if isinstance(shape, StringShape):
            return shape.name

        return shape.type_name

    @staticmethod
    def _get_streaming_body(shape: Shape) -> Shape | None:
        """
        Get the streaming member's shape if any; or None otherwise.
        """
        if not isinstance(shape, StructureShape):
            return None
        payload = shape.serialization.get("payload")
        if payload is not None:
            payload_shape = shape.members.get(payload)
            if isinstance(payload_shape, Shape) and payload_shape.type_name == "blob":
                return payload_shape
        return None

    def _parse_shape_by_type(
        self,
        shape: Shape,
        *,
        is_output_or_child: bool,
        output: bool,
        is_streaming: bool,
    ) -> FakeAnnotation:
        match shape:
            case StringShape():
                return self._parse_shape_string(shape)
            case MapShape():
                return self._parse_shape_map(
                    shape,
                    is_output_child=is_output_or_child,
                    is_streaming=is_streaming,
                )
            case StructureShape():
                return self._parse_shape_structure(
                    shape,
                    output=output,
                    output_child=is_output_or_child,
                    is_streaming=is_streaming,
                )
            case ListShape():
                return self._parse_shape_list(shape, is_output_child=is_output_or_child)
            case _:
                pass

        if shape.type_name in self.get_subresource_names():
            return InternalImport(shape.type_name, use_alias=True)

        self.logger.warning(f"Unknown shape: {shape} {shape.type_name}")
        return Type.Any

    def parse_shape(
        self,
        shape: Shape,
        *,
        is_output: bool = False,
        is_output_child: bool = False,
        is_streaming: bool = False,
    ) -> FakeAnnotation:
        """
        Parse any botocore shape to TypeAnnotation.

        Arguments:
            shape -- Botocore shape.
            output -- Whether shape should use strict output types.
            output_child -- Whether shape parent is marked as output.
            is_streaming -- Whether shape should be streaming.

        Returns:
            TypeAnnotation or similar class.
        """
        if shape.serialization.get("eventstream"):
            shape.serialization["eventstream"] = False
            return TypeSubscript(
                ExternalImport.from_class(EventStream),
                [
                    self.parse_shape(
                        shape,
                        is_output=is_output,
                        is_output_child=is_output_child,
                        is_streaming=is_streaming,
                    ),
                ],
            )
        is_output_or_child = is_output or is_output_child
        if not is_streaming:
            is_streaming = "streaming" in shape.serialization and shape.serialization["streaming"]
            if is_output_or_child:
                is_streaming = self._get_streaming_body(shape) is not None

        type_name = self._get_shape_type_name(shape)
        if is_streaming and shape.type_name == "blob":
            type_name = "blob_streaming"

        if is_output_or_child:
            shape_type_stub = get_output_shape_type_stub(
                self.service_name,
                self._resource_name,
                type_name,
            )
        else:
            shape_type_stub = get_shape_type_stub(self.service_name, self._resource_name, type_name)

        if shape_type_stub:
            return shape_type_stub

        result = self._parse_shape_by_type(
            shape,
            is_output_or_child=is_output_or_child,
            output=is_output,
            is_streaming=is_streaming,
        )
        if isinstance(result, TypeTypedDict):
            replacement = Type.DictStrAny if is_output_or_child else Type.MappingStrAny
            mutated_parents = result.replace_self_references(replacement)
            for mutated_parent in sorted(mutated_parents):
                self.logger.debug(
                    f"Replaced self reference for {result.render()} in {mutated_parent.render()}",
                )

        return result

    def get_paginator_subscript(self, paginator_name: str) -> FakeAnnotation:
        """
        Get Paginator return class.
        """
        operation_name = paginator_name
        operation_shape = self._get_operation(operation_name)
        if operation_shape.output_shape is None:
            return Type.Any

        return self._parse_return_type(
            "Paginator",
            "paginate",
            operation_shape.output_shape,
        )

    def get_paginate_method(self, paginator_name: str) -> Method:
        """
        Get Paginator `paginate` method.

        Arguments:
            paginator_name -- Paginator name.

        Returns:
            Method.
        """
        self._resource_name = "Paginator"
        operation_name = paginator_name
        paginator_shape = self._get_paginator(paginator_name)
        operation_shape = self._get_operation(operation_name)
        skip_argument_names: list[str] = []
        input_token: list[str] | str = paginator_shape["input_token"]
        if isinstance(input_token, list):
            skip_argument_names.extend(input_token)
        else:
            skip_argument_names.append(input_token)
        if "limit_key" in paginator_shape:
            skip_argument_names.append(paginator_shape["limit_key"])

        arguments: list[Argument] = [Argument.self()]

        if operation_shape.input_shape is not None:
            shape_arguments = self._parse_arguments(
                class_name="Paginator",
                method_name="paginate",
                operation_name=operation_name,
                shape=operation_shape.input_shape,
                exclude_names=skip_argument_names,
            )
            shape_arguments.append(
                Argument("PaginationConfig", PaginatorConfigTypeDef, Type.Ellipsis),
            )
            arguments.extend(self._get_kw_flags("paginate", shape_arguments))
            arguments.extend(shape_arguments)

        subscript = self.get_paginator_subscript(operation_name)
        return_type = TypeSubscript(ExternalImport.from_class(PageIterator), [subscript])
        method = Method(
            name="paginate",
            arguments=arguments,
            return_type=return_type,
            type_ignore="override",
        )
        if operation_shape.input_shape is not None:
            method.create_request_type_annotation(
                self._get_typed_dict_name(
                    operation_shape.input_shape,
                    postfix="Paginate",
                ),
            )
        return method

    def get_waiter_names(self) -> list[str]:
        """
        Get Waiter class names.
        """
        if not self._waiters_shape:
            return []

        return list(self._waiters_shape["waiters"].keys())

    def get_wait_method(self, waiter_name: str) -> Method:
        """
        Get Waiter `wait` method.

        Arguments:
            waiter_name -- Waiter name.

        Returns:
            Method.
        """
        self._resource_name = "Waiter"
        if not self._waiters_shape:
            raise ShapeParserError("Waiter shape is not defined")
        operation_name = self._waiters_shape["waiters"][waiter_name]["operation"]
        operation_shape = self._get_operation(operation_name)

        arguments: list[Argument] = [Argument.self()]

        if operation_shape.input_shape is not None:
            shape_arguments = self._parse_arguments(
                class_name="Waiter",
                method_name="wait",
                operation_name=operation_name,
                shape=operation_shape.input_shape,
            )
            shape_arguments.append(Argument("WaiterConfig", WaiterConfigTypeDef, Type.Ellipsis))
            arguments.extend(self._get_kw_flags("wait", shape_arguments))
            arguments.extend(shape_arguments)

        method = Method(
            name="wait",
            arguments=arguments,
            return_type=Type.none,
            type_ignore="override",
        )
        if operation_shape.input_shape is not None:
            method.create_request_type_annotation(
                self._get_typed_dict_name(
                    operation_shape.input_shape,
                    postfix="Wait",
                ),
            )
        return method

    def _get_identifier_type(
        self,
        resource_name: str,
        method_name: str,
        identifier_name: str,
        identifier: IdentifierShape,
    ) -> FakeAnnotation:
        argument_type_stub = get_method_type_stub(
            self.service_name,
            resource_name,
            method_name,
            identifier_name,
        )
        if argument_type_stub:
            return argument_type_stub
        identifier_type = identifier.get("type")
        if identifier_type:
            argument_type_stub = get_shape_type_stub(
                self.service_name,
                resource_name,
                identifier_type,
            )
            if argument_type_stub:
                return argument_type_stub

        return Type.str

    @staticmethod
    def _get_identifier_xform_name(identifier: IdentifierShape) -> str:
        return xform_name(identifier.get("name") or identifier.get("target") or "unknown")

    def _get_identifier_argument(
        self,
        resource_name: str,
        method_name: str,
        identifier: IdentifierShape,
    ) -> Argument:
        argument_name = self._get_identifier_xform_name(identifier)
        argument_type = self._get_identifier_type(
            resource_name,
            method_name,
            argument_name,
            identifier,
        )
        return Argument(argument_name, argument_type)

    def _get_identifier_attribute(
        self,
        resource_name: str,
        identifier: IdentifierShape,
    ) -> Attribute:
        attribute_name = self._get_identifier_xform_name(identifier)
        attribute_type = self._get_identifier_type(
            resource_name,
            ATTRIBUTES,
            attribute_name,
            identifier,
        )
        return Attribute(name=attribute_name, type_annotation=attribute_type, is_identifier=True)

    def _get_existing_sub_resource_names(
        self, service_resource_shape: ResourceShape, names: Iterable[str]
    ) -> set[str]:
        """
        Refer to `boto3.model._get_related_resources` definition.

        Probably it contains a bug that causes the issue with `ec2` package.
        """
        result: set[str] = set()
        has_map = service_resource_shape.get("has", {})
        has_rename_map: dict[str, str] = {}
        for has_name, has_def in has_map.items():
            old_name = has_def.get("resource", {}).get("type")
            if old_name:
                has_rename_map[old_name] = has_name
        for name in names:
            if name not in has_rename_map:
                result.add(name)
            else:
                result.add(has_rename_map[name])

        return result

    def get_service_resource_method_map(self) -> dict[str, Method]:
        """
        Get methods for ServiceResource.

        Returns:
            A map of method name to Method.
        """
        result: dict[str, Method] = {
            "get_available_subresources": Method(
                name="get_available_subresources",
                arguments=[Argument.self()],
                return_type=TypeSubscript(Type.Sequence, [Type.str]),
                docstring="Returns a list of all the available sub-resources for this resource.",
            ),
        }
        self._resource_name = SERVICE_RESOURCE
        service_resource_shape = self._get_resource_shape(self._resource_name)
        for action_name, action_shape in service_resource_shape.get("actions", {}).items():
            method = self._get_resource_method(action_name, action_shape)
            result[method.name] = method

        sub_resource_names = self.get_subresource_names()
        existing_sub_resource_names = self._get_existing_sub_resource_names(
            service_resource_shape, sub_resource_names
        )
        for sub_resource_name in sub_resource_names:
            # FIXME: hack for ec2: KeyPairInfo is not registered, but present in docs
            if sub_resource_name not in existing_sub_resource_names:
                self.logger.debug(
                    f"Skipping {sub_resource_name} sub resource"
                    " because it is not present in ServiceResource.has"
                )
                continue
            sub_resource_shape = self._get_resource_shape(sub_resource_name)
            if not self._is_subresource(sub_resource_shape):
                continue
            arguments = [Argument.self()]
            identifiers = sub_resource_shape.get("identifiers", [])
            for identifier in identifiers:
                argument = self._get_identifier_argument(
                    self._resource_name,
                    sub_resource_name,
                    identifier,
                )
                arguments.append(argument)
            method = Method(
                name=sub_resource_name,
                arguments=arguments,
                return_type=InternalImport(sub_resource_name, use_alias=True),
                docstring=f"Creates a {sub_resource_name} resource.",
            )
            result[method.name] = method

        return result

    def get_identifier_attributes(self, resource_name: str) -> list[Attribute]:
        """
        Get attributes for Resource identifiers.

        Arguments:
            resource_name -- Resource name.

        Returns:
            A map of method name to Method.
        """
        self._resource_name = resource_name
        resource_shape = self._get_resource_shape(resource_name)
        identifiers = resource_shape.get("identifiers", [])
        return [
            self._get_identifier_attribute(resource_name, identifier) for identifier in identifiers
        ]

    def get_resource_load_method(self, method_name: str = "load") -> Method:
        """
        Get Resource `load` or `reload` method.
        """
        return Method(name=method_name, arguments=[Argument.self()], return_type=Type.none)

    @staticmethod
    def _is_subresource(subresource_shape: ResourceShape | SubResourceShape) -> bool:
        for identifier in subresource_shape.get("identifiers", []):
            if identifier.get("source") == "data":
                return False

        return True

    def get_resource_method_map(self, resource_name: str) -> dict[str, Method]:
        """
        Get methods for Resource.

        Arguments:
            resource_name -- Resource name.

        Returns:
            A map of method name to Method.
        """
        self._resource_name = resource_name
        resource_shape = self._get_resource_shape(resource_name)
        result: dict[str, Method] = {
            "get_available_subresources": Method(
                name="get_available_subresources",
                arguments=[Argument.self()],
                return_type=TypeSubscript(Type.Sequence, [Type.str]),
                docstring=(
                    f"Returns a list of all the available sub-resources for this {resource_name}."
                ),
            ),
        }

        if "actions" in resource_shape:
            for action_name, action_shape in resource_shape["actions"].items():
                method = self._get_resource_method(action_name, action_shape)
                result[method.name] = method

        if "waiters" in resource_shape:
            for waiter_name in resource_shape["waiters"]:
                state_name = xform_name(waiter_name)
                method = Method(
                    name=f"wait_until_{state_name}",
                    arguments=[Argument.self()],
                    return_type=Type.none,
                    docstring=f"Waits until {resource_name} is {state_name}.",
                )
                result[method.name] = method

        for method_name, sub_resource in resource_shape.get("has", {}).items():
            if "resource" not in sub_resource:
                continue
            data = sub_resource["resource"]
            if not self._is_subresource(data):
                continue
            arguments = [Argument.self()]
            identifiers = data.get("identifiers", [])
            for identifier in identifiers:
                if identifier.get("source") != "input":
                    continue
                argument = self._get_identifier_argument(
                    resource_name,
                    method_name,
                    identifier,
                )
                arguments.append(argument)

            sub_resource_name = data["type"]
            method = Method(
                name=method_name,
                arguments=arguments,
                return_type=InternalImport(sub_resource_name, use_alias=True),
                docstring=f"Creates a {sub_resource_name} resource.",
            )
            result[method.name] = method

        return result

    @staticmethod
    def _get_arg_from_target(target: str) -> str:
        if "[" in target:
            target = target.split("[")[0]
        if "." in target:
            target = target.split(".")[0]
        return target

    def _get_skip_argument_names(self, action_shape: ActionShape) -> set[str]:
        result: set[str] = set()
        params = action_shape["request"].get("params", [])
        for param in params:
            target = param["target"]
            source = param["source"]
            if source == "identifier":
                result.add(self._get_arg_from_target(target))
                continue
            if source == "string" and "." in target:
                result.add(self._get_arg_from_target(target))
                continue

        return result

    def _enrich_arguments_defaults(
        self,
        arguments: list[Argument],
        action_shape: ActionShape,
    ) -> None:
        request = action_shape["request"]
        arguments_map = {a.name: a for a in arguments}
        if "params" in request:
            for param in request["params"]:
                target = param["target"]
                source = param["source"]
                if source == "string" and target in arguments_map:
                    arguments_map[target].default = TypeConstant(param["value"])

    def _get_resource_method(self, action_name: str, action_shape: ActionShape) -> Method:
        return_type: FakeAnnotation = Type.none
        method_name = xform_name(action_name)
        arguments: list[Argument] = [Argument.self()]
        if "resource" in action_shape:
            return_type = self._parse_return_type(
                self.resource_name,
                method_name,
                Shape("resource", action_shape["resource"]),
            )
            path = action_shape["resource"].get("path", "")
            if path.endswith("[]"):
                return_type = TypeSubscript(Type.list, [return_type])

        operation_model = None
        if "request" in action_shape:
            operation_name = action_shape["request"]["operation"]
            operation_model = self._get_operation(operation_name)
            skip_argument_names = self._get_skip_argument_names(action_shape)
            if operation_model.input_shape is not None:
                shape_arguments = self._parse_arguments(
                    class_name=self.resource_name,
                    method_name=method_name,
                    operation_name=operation_name,
                    shape=operation_model.input_shape,
                    exclude_names=skip_argument_names,
                )
                arguments.extend(self._get_kw_flags(method_name, shape_arguments))
                arguments.extend(shape_arguments)

            self._enrich_arguments_defaults(arguments, action_shape)
            arguments.sort(key=lambda x: not x.required)

            if operation_model.output_shape is not None and return_type is Type.none:
                operation_return_type = self.parse_shape(
                    operation_model.output_shape,
                    is_output=True,
                )
                return_type = operation_return_type

        method = Method(
            name=method_name,
            arguments=arguments,
            return_type=return_type,
            docstring=get_short_docstring(
                extract_docstring_from_html(operation_model.documentation),
            ),
        )
        if operation_model and operation_model.input_shape is not None:
            method.create_request_type_annotation(
                self._get_typed_dict_name(
                    operation_model.input_shape,
                    postfix=f"{self.resource_name}{action_name}",
                ),
            )
        return method

    def get_collection_filter_method(
        self,
        name: str,
        collection: Boto3Collection,
        self_type: FakeAnnotation,
    ) -> Method:
        """
        Get `filter` classmethod for Resource collection.

        Arguments:
            name -- Collection record name.
            collection -- Boto3 Collection.
            class_type -- Collection class type annotation.

        Returns:
            Filter Method record.
        """
        result = Method(
            name="filter",
            arguments=[Argument.self()],
            return_type=self_type,
        )
        if not collection.request:
            return result

        operation_name = collection.request.operation
        operation_model = self._get_operation(operation_name)

        if operation_model.input_shape is not None:
            shape_arguments = self._parse_arguments(
                class_name=name,
                method_name=result.name,
                operation_name=operation_name,
                shape=operation_model.input_shape,
                optional_only=True,
            )
            result.arguments.extend(self._get_kw_flags(result.name, shape_arguments))
            result.arguments.extend(shape_arguments)

        return result

    def get_collection_batch_methods(self, name: str, collection: Boto3Collection) -> list[Method]:
        """
        Get batch operations for Resource collection.

        Arguments:
            name -- Collection record name.
            collection -- Boto3 Collection.
            class_type -- Collection self type annotation.

        Returns:
            List of Method records.
        """
        result: list[Method] = []
        for batch_action in collection.batch_actions:
            method = Method(
                name=batch_action.name,
                arguments=[Argument.self()],
                return_type=Type.none,
            )
            result.append(method)
            if batch_action.request:
                operation_name = batch_action.request.operation
                operation_model = self._get_operation(operation_name)
                if operation_model.input_shape is not None:
                    shape_arguments = self._parse_arguments(
                        class_name=name,
                        method_name=batch_action.name,
                        operation_name=operation_name,
                        shape=operation_model.input_shape,
                        optional_only=True,
                    )
                    method.arguments.extend(self._get_kw_flags(batch_action.name, shape_arguments))
                    method.arguments.extend(shape_arguments)
                if operation_model.output_shape is not None:
                    item_return_type = self.parse_shape(
                        operation_model.output_shape,
                        is_output=True,
                    )
                    return_type = TypeSubscript(Type.list, [item_return_type])
                    method.return_type = return_type

        return result

    @staticmethod
    def _get_typed_dict_name_prefix(name: str) -> str:
        if name.endswith("OutputTypeDef"):
            return name[: -len("OutputTypeDef")]
        if name.endswith("TypeDef"):
            return name[: -len("TypeDef")]

        raise ShapeParserError(f"Unknown typed dict name format: {name}")

    def _get_typed_dict(
        self,
        name: str,
        maps: Sequence[dict[str, TypeTypedDict]],
    ) -> TypeTypedDict | None:
        for typed_dict_map in maps:
            if name in typed_dict_map:
                return typed_dict_map[name]
        return None

    def _get_non_clashing_typed_dict_name(self, typed_dict: TypeTypedDict, postfix: str) -> str:
        new_typed_dict_name = get_type_def_name(
            self._get_typed_dict_name_prefix(typed_dict.name),
            postfix,
        )
        clashing_typed_dict = self._get_typed_dict(
            new_typed_dict_name,
            (
                self._typed_dict_map,
                self._output_typed_dict_map,
                self._response_typed_dict_map,
            ),
        )
        if not clashing_typed_dict:
            return new_typed_dict_name

        temp_typed_dict = typed_dict.copy()
        temp_typed_dict.name = new_typed_dict_name
        if clashing_typed_dict.is_same(temp_typed_dict):
            return new_typed_dict_name

        self.logger.debug(f"Clashing typed dict name found: {new_typed_dict_name}")
        return self._get_non_clashing_typed_dict_name(typed_dict, "Extra" + postfix)

    def fix_typed_dict_names(self) -> None:
        """
        Fix typed dict names to avoid duplicates.
        """
        output_typed_dict_names = self._output_typed_dict_map.get_sorted_names()
        for name in output_typed_dict_names:
            typed_dict = self._get_typed_dict(
                name,
                (self._typed_dict_map,),
            )
            if typed_dict is None:
                continue

            for output_typed_dict in self._output_typed_dict_map.iterate_by_name(name):
                if typed_dict.is_same(output_typed_dict):
                    continue

                old_typed_dict_name = output_typed_dict.name
                new_typed_dict_name = self._get_non_clashing_typed_dict_name(
                    output_typed_dict,
                    "Output",
                )
                self._fixed_typed_dict_map[typed_dict] = output_typed_dict
                self.logger.debug(
                    "Fixing output TypedDict name clash"
                    f" {old_typed_dict_name} -> {new_typed_dict_name}",
                )

                self._output_typed_dict_map.rename(output_typed_dict, new_typed_dict_name)

                if old_typed_dict_name in self._response_typed_dict_map:
                    del self._response_typed_dict_map[old_typed_dict_name]
                    self._response_typed_dict_map.add(output_typed_dict)

        response_typed_dict_names = self._response_typed_dict_map.get_sorted_names()
        for name in response_typed_dict_names:
            typed_dict = self._get_typed_dict(
                name,
                (
                    self._typed_dict_map,
                    self._output_typed_dict_map,
                ),
            )
            if typed_dict is None:
                continue

            for response_typed_dict in self._response_typed_dict_map.iterate_by_name(name):
                if typed_dict.is_same(response_typed_dict):
                    continue

                old_typed_dict_name = response_typed_dict.name
                new_typed_dict_name = self._get_non_clashing_typed_dict_name(
                    response_typed_dict,
                    "Response",
                )
                self.logger.debug(
                    "Fixing response TypedDict name clash"
                    f" {old_typed_dict_name} -> {new_typed_dict_name}",
                )

                self._response_typed_dict_map.rename(response_typed_dict, new_typed_dict_name)

    @staticmethod
    def _get_parent_type_annotations(
        methods: Sequence[Method],
    ) -> set[TypeParent]:
        result: set[TypeParent] = set()
        for method in methods:
            for argument in method.arguments:
                if isinstance(argument.type_annotation, TypeParent):
                    result.add(argument.type_annotation)
        return result

    def convert_input_arguments_to_unions(self, methods: Sequence[Method]) -> None:
        """
        Accept both input and output shapes in method arguments.

        mypy does not compare TypedDicts, so we need to accept both input and output shapes.
        https://github.com/youtype/mypy_boto3_builder/issues/209
        """
        parent_type_annotations = list(self._get_parent_type_annotations(methods))
        for input_typed_dict, output_typed_dict in self._fixed_typed_dict_map.items():
            union_name = self._get_non_clashing_typed_dict_name(input_typed_dict, "Union")
            union_type_annotation = TypeUnion(
                name=union_name,
                children=[input_typed_dict, output_typed_dict],
            )
            for type_annotation in parent_type_annotations:
                parents = type_annotation.find_type_annotation_parents(input_typed_dict)
                if not parents:
                    continue

                for parent in sorted(parents):
                    if is_union(parent) and parent.name == union_name:
                        continue
                    self.logger.debug(
                        f"Adding output shape to {parent.render()} type:"
                        f" {input_typed_dict.name} | {output_typed_dict.name}",
                    )
                    parent.replace_child(input_typed_dict, union_type_annotation)
