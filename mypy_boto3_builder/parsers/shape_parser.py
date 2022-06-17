"""
Parser for botocore shape files.
"""
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from boto3.resources.model import Collection
from boto3.session import Session
from botocore import xform_name
from botocore.exceptions import UnknownServiceError
from botocore.model import (
    ListShape,
    MapShape,
    OperationModel,
    ServiceModel,
    Shape,
    StringShape,
    StructureShape,
)
from botocore.session import Session as BotocoreSession

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import AliasInternalImport, InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_maps.literal_type_map import get_literal_type_stub
from mypy_boto3_builder.type_maps.method_type_map import (
    get_default_value_stub,
    get_method_type_stub,
)
from mypy_boto3_builder.type_maps.shape_type_map import (
    OUTPUT_SHAPE_TYPE_MAP,
    SHAPE_TYPE_MAP,
    get_shape_type_stub,
)
from mypy_boto3_builder.type_maps.typed_dicts import (
    empty_response_metadata_type,
    paginator_config_type,
    response_metadata_type,
    waiter_config_type,
)


class ShapeParserError(Exception):
    """
    Main error for ShapeParser.
    """


class ShapeParser:
    """
    Parser for botocore shape files.

    Arguments:
        session -- Boto3 session.
        service_name -- ServiceName.
    """

    # Alias map fixes added by botocore for documentation build.
    # https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L773
    # https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L1055
    ARGUMENT_ALIASES: dict[ServiceName, dict[str, dict[str, str]]] = {
        ServiceNameCatalog.cloudsearchdomain: {"Search": {"return": "returnFields"}},
        ServiceNameCatalog.logs: {"CreateExportTask": {"from": "fromTime"}},
        ServiceNameCatalog.ec2: {"*": {"Filter": "Filters"}},
        ServiceNameCatalog.s3: {
            "PutBucketAcl": {"ContentMD5": "None"},
            "PutBucketCors": {"ContentMD5": "None"},
            "PutBucketLifecycle": {"ContentMD5": "None"},
            "PutBucketLogging": {"ContentMD5": "None"},
            "PutBucketNotification": {"ContentMD5": "None"},
            "PutBucketPolicy": {"ContentMD5": "None"},
            "PutBucketReplication": {"ContentMD5": "None"},
            "PutBucketRequestPayment": {"ContentMD5": "None"},
            "PutBucketTagging": {"ContentMD5": "None"},
            "PutBucketVersioning": {"ContentMD5": "None"},
            "PutBucketWebsite": {"ContentMD5": "None"},
            "PutObjectAcl": {"ContentMD5": "None"},
        },
    }

    def __init__(self, session: Session, service_name: ServiceName):
        loader = session._loader
        botocore_session: BotocoreSession = session._session
        service_data = botocore_session.get_service_data(service_name.boto3_name)
        self.service_name = service_name
        self.service_model = ServiceModel(service_data, service_name.boto3_name)
        self._resource_name: str = ""
        self._typed_dict_map: dict[str, TypeTypedDict] = {}
        self._waiters_shape: Mapping[str, Any] | None = None
        try:
            self._waiters_shape = loader.load_service_model(service_name.boto3_name, "waiters-2")
        except UnknownServiceError:
            pass
        self._paginators_shape: Mapping[str, Any] | None = None
        try:
            self._paginators_shape = loader.load_service_model(
                service_name.boto3_name, "paginators-1"
            )
        except UnknownServiceError:
            pass
        self._resources_shape: Mapping[str, Any] | None = None
        try:
            self._resources_shape = loader.load_service_model(
                service_name.boto3_name, "resources-1"
            )
        except UnknownServiceError:
            pass

        self.logger = get_logger()
        self.proxy_operation_model = OperationModel({}, self.service_model)

    @property
    def resource_name(self) -> str:
        """
        Parsed resource name.
        """
        return self._resource_name

    def _get_operation(self, name: str) -> OperationModel:
        return self.service_model.operation_model(name)

    def _get_operation_names(self) -> list[str]:
        return list(self.service_model.operation_names)

    def _get_paginator(self, name: str) -> dict[str, Any]:
        if not self._paginators_shape:
            raise ShapeParserError(f"Unknown paginator: {name}")
        try:
            return self._paginators_shape["pagination"][name]
        except KeyError as e:
            raise ShapeParserError(f"Unknown paginator: {name}") from e

    def _get_service_resource(self) -> dict[str, Any]:
        if not self._resources_shape:
            raise ShapeParserError("Resource shape not found")
        return self._resources_shape["service"]

    def _get_resource_shape(self, name: str) -> dict[str, Any]:
        if not self._resources_shape:
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
        result: list[str] = []
        if self._paginators_shape:
            for name in self._paginators_shape.get("pagination", []):
                result.append(name)
        result.sort()
        return result

    def _get_argument_alias(self, operation_name: str, argument_name: str) -> str:
        service_map = self.ARGUMENT_ALIASES.get(self.service_name)
        if not service_map:
            return argument_name

        operation_map: dict[str, str] = {}
        if "*" in service_map:
            operation_map = service_map["*"]
        if operation_name in service_map:
            operation_map = service_map[operation_name]

        if not operation_map:
            return argument_name

        if argument_name not in operation_map:
            return argument_name

        return operation_map[argument_name]

    def _parse_arguments(
        self,
        class_name: str,
        method_name: str,
        operation_name: str,
        shape: StructureShape,
        exclude_names: Iterable[str] = tuple(),
        optional_only: bool = False,
    ) -> list[Argument]:
        result: list[Argument] = []
        required = shape.required_members
        for argument_name, argument_shape in shape.members.items():
            if argument_name in exclude_names:
                continue
            argument_alias = self._get_argument_alias(operation_name, argument_name)
            if argument_alias == "None":
                continue

            argument_type_stub = get_method_type_stub(
                self.service_name, class_name, method_name, argument_name
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
                self.service_name, class_name, method_name, argument_name
            )
            if default_value_stub is not None:
                argument.default = default_value_stub
            if optional_only and argument.required:
                continue

            # FIXME: https://github.com/boto/boto3/issues/2813
            # if not argument.required and argument.type_annotation:
            #     argument.type_annotation = Type.get_optional(argument.type_annotation)

            result.append(argument)

        result.sort(key=lambda x: not x.required)
        return result

    def _parse_return_type(
        self, class_name: str, method_name: str, shape: Shape | None
    ) -> FakeAnnotation:
        argument_type_stub = get_method_type_stub(
            self.service_name, class_name, method_name, "return"
        )
        if argument_type_stub is not None:
            return argument_type_stub

        if shape:
            return self.parse_shape(shape, output=True)

        return Type.none

    @staticmethod
    def _get_kw_flags(method_name: str, arguments: Sequence[Argument]) -> list[Argument]:
        if len(arguments) and not method_name[0].isupper():
            return [Argument.kwflag()]

        return []

    def get_client_method_map(self) -> dict[str, Method]:
        """
        Get client methods from shape.

        Returns:
            A map of method name to Method.
        """
        self._resource_name = ""
        result: dict[str, Method] = {
            "can_paginate": Method(
                "can_paginate",
                [Argument("self", None), Argument("operation_name", Type.str)],
                Type.bool,
            ),
            "generate_presigned_url": Method(
                "generate_presigned_url",
                [
                    Argument("self", None),
                    Argument("ClientMethod", Type.str),
                    Argument("Params", Type.MappingStrAny, Type.Ellipsis),
                    Argument("ExpiresIn", Type.int, TypeConstant(3600)),
                    Argument("HttpMethod", Type.str, Type.Ellipsis),
                ],
                Type.str,
            ),
        }
        for operation_name in self._get_operation_names():
            operation_model = self._get_operation(operation_name)
            arguments: list[Argument] = [Argument("self", None)]
            method_name = xform_name(operation_name)

            if operation_model.input_shape is not None:
                shape_arguments = self._parse_arguments(
                    "Client",
                    method_name,
                    operation_name,
                    operation_model.input_shape,
                )
                arguments.extend(self._get_kw_flags(method_name, shape_arguments))
                arguments.extend(shape_arguments)

            return_type = self._parse_return_type(
                "Client", method_name, operation_model.output_shape
            )
            if return_type is Type.none:
                return_type = empty_response_metadata_type

            method = Method(name=method_name, arguments=arguments, return_type=return_type)
            if operation_model.input_shape:
                method.create_request_type_annotation(
                    self._get_typed_dict_name(operation_model.input_shape, postfix="Request")
                )
            result[method.name] = method
        return result

    @staticmethod
    def _get_typed_dict_name(shape: Shape, postfix: str = "") -> str:
        return f"{shape.name}{postfix}TypeDef"

    def _parse_shape_string(self, shape: StringShape) -> FakeAnnotation:
        if not shape.enum:
            return Type.str

        literal_name = f"{shape.name}Type"
        literal_type_stub = get_literal_type_stub(self.service_name, literal_name)
        if literal_type_stub:
            return TypeLiteral(literal_name, literal_type_stub)

        return TypeLiteral(literal_name, [option for option in shape.enum])

    def _parse_shape_map(
        self,
        shape: MapShape,
        output_child: bool = False,
        is_streaming: bool = False,
    ) -> FakeAnnotation:
        type_subscript = TypeSubscript(Type.Dict) if output_child else TypeSubscript(Type.Mapping)
        if shape.key:
            type_subscript.add_child(
                self.parse_shape(shape.key, output_child=output_child, is_streaming=is_streaming)
            )
        else:
            type_subscript.add_child(Type.str)
        if shape.value:
            type_subscript.add_child(
                self.parse_shape(shape.value, output_child=output_child, is_streaming=is_streaming)
            )
        else:
            type_subscript.add_child(Type.Any)
        return type_subscript

    def _parse_shape_structure(
        self,
        shape: StructureShape,
        output: bool = False,
        output_child: bool = False,
        is_streaming: bool = False,
    ) -> FakeAnnotation:
        if not shape.members.items():
            return Type.DictStrAny if output_child else Type.MappingStrAny

        required = shape.required_members
        typed_dict_name = self._get_shape_type_name(shape)
        typed_dict = TypeTypedDict(typed_dict_name)

        if typed_dict.name in self._typed_dict_map:
            old_typed_dict = self._typed_dict_map[typed_dict.name]
            child_names = {i.name for i in old_typed_dict.children}
            if output and "ResponseMetadata" in child_names:
                return self._typed_dict_map[typed_dict.name]
            if not output and "ResponseMetadata" not in child_names:
                return self._typed_dict_map[typed_dict.name]

            if output:
                typed_dict.name = self._get_typed_dict_name(shape, postfix="ResponseMetadata")
                self.logger.debug(f"Marking {typed_dict.name} as ResponseMetadataTypeDef")
            else:
                old_typed_dict.name = self._get_typed_dict_name(shape, postfix="ResponseMetadata")
                self._typed_dict_map[old_typed_dict.name] = old_typed_dict
                self.logger.debug(f"Marking {old_typed_dict.name} as ResponseMetadataTypeDef")

        self._typed_dict_map[typed_dict.name] = typed_dict
        for attr_name, attr_shape in shape.members.items():
            typed_dict.add_attribute(
                attr_name,
                self.parse_shape(
                    attr_shape,
                    output_child=output or output_child,
                    is_streaming=is_streaming,
                ),
                attr_name in required,
            )
        if output:
            self._make_output_typed_dict(typed_dict)
        return typed_dict

    def _make_output_typed_dict(self, typed_dict: TypeTypedDict) -> None:
        for attribute in typed_dict.children:
            attribute.required = True
        child_names = {i.name for i in typed_dict.children}
        if "ResponseMetadata" not in child_names:
            typed_dict.add_attribute(
                "ResponseMetadata",
                response_metadata_type,
                True,
            )

    def _parse_shape_list(self, shape: ListShape, output_child: bool = False) -> FakeAnnotation:
        type_subscript = TypeSubscript(Type.List) if output_child else TypeSubscript(Type.Sequence)
        if shape.member:
            type_subscript.add_child(self.parse_shape(shape.member, output_child=output_child))
        else:
            type_subscript.add_child(Type.Any)
        return type_subscript

    def _get_shape_type_name(self, shape: Shape) -> str:
        if not isinstance(shape, StructureShape):
            return shape.type_name

        if self.service_name.is_custom_resource(self.resource_name):
            return self._get_typed_dict_name(shape, postfix=self.resource_name)

        return self._get_typed_dict_name(shape)

    def parse_shape(
        self,
        shape: Shape,
        output: bool = False,
        output_child: bool = False,
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
        if not is_streaming:
            is_streaming = "streaming" in shape.serialization and shape.serialization["streaming"]
            if output or output_child:
                is_streaming = self.proxy_operation_model._get_streaming_body(shape) is not None  # type: ignore

        type_name = self._get_shape_type_name(shape)
        if is_streaming and type_name == "blob":
            type_name = "blob_streaming"

        shape_type_stub = get_shape_type_stub(
            (
                OUTPUT_SHAPE_TYPE_MAP if output or output_child else {},
                SHAPE_TYPE_MAP,
            ),
            self.service_name,
            type_name,
        )
        if shape_type_stub:
            return shape_type_stub

        if isinstance(shape, StringShape):
            return self._parse_shape_string(shape)

        if isinstance(shape, MapShape):
            return self._parse_shape_map(
                shape,
                output_child=output or output_child,
                is_streaming=is_streaming,
            )

        if isinstance(shape, StructureShape):
            return self._parse_shape_structure(
                shape,
                output=output,
                output_child=output or output_child,
                is_streaming=is_streaming,
            )

        if isinstance(shape, ListShape):
            return self._parse_shape_list(shape, output_child=output or output_child)

        if self._resources_shape and shape.type_name in self._resources_shape["resources"]:
            return AliasInternalImport(shape.type_name)

        self.logger.warning(f"Unknown shape: {shape} {type_name}")
        return Type.Any

    def get_paginate_method(self, paginator_name: str) -> Method:
        """
        Get Paginator `paginate` method.

        Arguments:
            paginator_name -- Paginator name.

        Returns:
            Method.
        """
        operation_name = paginator_name
        paginator_shape = self._get_paginator(paginator_name)
        operation_shape = self._get_operation(operation_name)
        skip_argument_names: list[str] = []
        input_token = paginator_shape["input_token"]
        if isinstance(input_token, list):
            skip_argument_names.extend(input_token)
        else:
            skip_argument_names.append(input_token)
        if "limit_key" in paginator_shape:
            skip_argument_names.append(paginator_shape["limit_key"])

        arguments: list[Argument] = [Argument("self", None)]

        if operation_shape.input_shape is not None:
            shape_arguments = self._parse_arguments(
                "Paginator",
                "paginate",
                operation_name,
                operation_shape.input_shape,
                exclude_names=skip_argument_names,
            )
            shape_arguments.append(
                Argument("PaginationConfig", paginator_config_type, Type.Ellipsis)
            )
            arguments.extend(self._get_kw_flags("paginate", shape_arguments))
            arguments.extend(shape_arguments)

        return_type: FakeAnnotation = Type.none
        if operation_shape.output_shape is not None:
            page_iterator_import = InternalImport("_PageIterator", stringify=False)
            return_item = self._parse_return_type(
                "Paginator", "paginate", operation_shape.output_shape
            )
            return_type = TypeSubscript(page_iterator_import, [return_item])

        method = Method("paginate", arguments, return_type)
        if operation_shape.input_shape is not None:
            method.create_request_type_annotation(
                self._get_typed_dict_name(
                    operation_shape.input_shape, postfix=f"{paginator_name}Paginate"
                )
            )
        return method

    def get_wait_method(self, waiter_name: str) -> Method:
        """
        Get Waiter `wait` method.

        Arguments:
            waiter_name -- Waiter name.

        Returns:
            Method.
        """
        if not self._waiters_shape:
            raise ShapeParserError("Waiter not found")
        operation_name = self._waiters_shape["waiters"][waiter_name]["operation"]
        operation_shape = self._get_operation(operation_name)

        arguments: list[Argument] = [Argument("self", None)]

        if operation_shape.input_shape is not None:
            shape_arguments = self._parse_arguments(
                "Waiter", "wait", operation_name, operation_shape.input_shape
            )
            shape_arguments.append(Argument("WaiterConfig", waiter_config_type, Type.Ellipsis))
            arguments.extend(self._get_kw_flags("wait", shape_arguments))
            arguments.extend(shape_arguments)

        method = Method(name="wait", arguments=arguments, return_type=Type.none)
        if operation_shape.input_shape is not None:
            method.create_request_type_annotation(
                self._get_typed_dict_name(operation_shape.input_shape, postfix=f"{waiter_name}Wait")
            )
        return method

    def get_service_resource_method_map(self) -> dict[str, Method]:
        """
        Get methods for ServiceResource.

        Returns:
            A map of method name to Method.
        """
        result: dict[str, Method] = {
            "get_available_subresources": Method(
                "get_available_subresources",
                [Argument("self", None)],
                TypeSubscript(Type.Sequence, [Type.str]),
            ),
        }
        self._resource_name = "ServiceResource"
        service_resource_shape = self._get_service_resource()
        for action_name, action_shape in service_resource_shape.get("actions", {}).items():
            method = self._get_resource_method(action_name, action_shape)
            result[method.name] = method

        return result

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
                "get_available_subresources",
                [Argument("self", None)],
                TypeSubscript(Type.Sequence, [Type.str]),
            ),
            "load": Method("load", [Argument("self", None)], Type.none),
            "reload": Method("reload", [Argument("self", None)], Type.none),
        }

        for action_name, action_shape in resource_shape.get("actions", {}).items():
            method = self._get_resource_method(action_name, action_shape)
            result[method.name] = method

        for waiter_name in resource_shape.get("waiters", {}):
            method = Method(
                f"wait_until_{xform_name(waiter_name)}",
                [Argument("self", None)],
                Type.none,
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

    def _get_skip_argument_names(self, action_shape: dict[str, Any]) -> set[str]:
        result = set()
        params = action_shape["request"].get("params", {})
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
        self, arguments: list[Argument], action_shape: dict[str, Any]
    ) -> None:
        params = action_shape["request"].get("params", {})
        arguments_map = {a.name: a for a in arguments}
        for param in params:
            target = param["target"]
            source = param["source"]
            if source == "string" and target in arguments_map:
                arguments_map[target].default = TypeConstant(param["value"])

    def _get_resource_method(self, action_name: str, action_shape: dict[str, Any]) -> Method:
        return_type: FakeAnnotation = Type.none
        method_name = xform_name(action_name)
        arguments: list[Argument] = [Argument("self", None)]
        if "resource" in action_shape:
            return_type = self._parse_return_type(
                self.resource_name, method_name, Shape("resource", action_shape["resource"])
            )
            path = action_shape["resource"].get("path", "")
            if path.endswith("[]"):
                return_type = TypeSubscript(Type.List, [return_type])

        operation_shape = None
        if "request" in action_shape:
            operation_name = action_shape["request"]["operation"]
            operation_shape = self._get_operation(operation_name)
            skip_argument_names = self._get_skip_argument_names(action_shape)
            if operation_shape.input_shape is not None:
                shape_arguments = self._parse_arguments(
                    self.resource_name,
                    method_name,
                    operation_name,
                    operation_shape.input_shape,
                    exclude_names=skip_argument_names,
                )
                arguments.extend(self._get_kw_flags(method_name, shape_arguments))
                arguments.extend(shape_arguments)

            self._enrich_arguments_defaults(arguments, action_shape)
            arguments.sort(key=lambda x: not x.required)

            if operation_shape.output_shape is not None and return_type is Type.none:
                operation_return_type = self.parse_shape(operation_shape.output_shape, output=True)
                return_type = operation_return_type

        method = Method(name=method_name, arguments=arguments, return_type=return_type)
        if operation_shape and operation_shape.input_shape is not None:
            method.create_request_type_annotation(
                self._get_typed_dict_name(
                    operation_shape.input_shape, postfix=f"{self.resource_name}{action_name}"
                )
            )
        return method

    def get_collection_filter_method(
        self, name: str, collection: Collection, self_type: FakeAnnotation
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
            arguments=[Argument("self", None)],
            return_type=self_type,
        )
        if not collection.request:
            return result

        operation_name = collection.request.operation
        operation_model = self._get_operation(operation_name)

        if operation_model.input_shape is not None:
            shape_arguments = self._parse_arguments(
                name,
                result.name,
                operation_name,
                operation_model.input_shape,
                optional_only=True,
            )
            result.arguments.extend(self._get_kw_flags(result.name, shape_arguments))
            result.arguments.extend(shape_arguments)

        return result

    def get_collection_batch_methods(self, name: str, collection: Collection) -> list[Method]:
        """
        Get batch operations for Resource collection.

        Arguments:
            name -- Collection record name.
            collection -- Boto3 Collection.
            class_type -- Collection self type annotation.

        Returns:
            List of Method records.
        """
        result = []
        for batch_action in collection.batch_actions:
            method = Method(
                name=batch_action.name,
                arguments=[Argument("self", None)],
                return_type=Type.none,
            )
            result.append(method)
            if batch_action.request:
                operation_name = batch_action.request.operation
                operation_model = self._get_operation(operation_name)
                if operation_model.input_shape is not None:
                    shape_arguments = self._parse_arguments(
                        name,
                        batch_action.name,
                        operation_name,
                        operation_model.input_shape,
                        optional_only=True,
                    )
                    method.arguments.extend(self._get_kw_flags(batch_action.name, shape_arguments))
                    method.arguments.extend(shape_arguments)
                if operation_model.output_shape is not None:
                    item_return_type = self.parse_shape(operation_model.output_shape, output=True)
                    return_type = TypeSubscript(Type.List, [item_return_type])
                    method.return_type = return_type

        return result
