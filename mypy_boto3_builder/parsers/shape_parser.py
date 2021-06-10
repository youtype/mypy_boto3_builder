"""
Parser for botocore shape files.
"""
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

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
from botocore.response import StreamingBody
from botocore.session import Session as BotocoreSession

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import AliasInternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.type_maps.literal_type_map import get_literal_type_stub
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub
from mypy_boto3_builder.type_maps.shape_type_map import get_shape_type_stub
from mypy_boto3_builder.type_maps.typed_dicts import paginator_config_type, waiter_config_type


class ShapeParserError(Exception):
    pass


class ShapeParser:
    """
    Parser for botocore shape files.

    Arguments:
        session -- Boto3 session.
        service_name -- ServiceName.
    """

    # Type map for shape types.
    SHAPE_TYPE_MAP = {
        "integer": Type.int,
        "long": Type.int,
        "boolean": Type.bool,
        "double": Type.float,
        "float": Type.float,
        "timestamp": ExternalImport(ImportString("datetime"), "datetime"),
        "blob": TypeSubscript(Type.Union, [Type.bytes, Type.IOBytes]),
    }

    # Alias map fixes added by botocore for documentation build.
    # https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L773
    # https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L1055
    ARGUMENT_ALIASES: Dict[str, Dict[str, Dict[str, str]]] = {
        ServiceNameCatalog.cloudsearchdomain.boto3_name: {"Search": {"return": "returnFields"}},
        ServiceNameCatalog.logs.boto3_name: {"CreateExportTask": {"from": "fromTime"}},
        ServiceNameCatalog.ec2.boto3_name: {"*": {"Filter": "Filters"}},
        ServiceNameCatalog.s3.boto3_name: {
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
        self._typed_dict_map: Dict[str, TypeTypedDict] = {}
        self._waiters_shape: Optional[Mapping[str, Any]] = None
        try:
            self._waiters_shape = loader.load_service_model(service_name.boto3_name, "waiters-2")
        except UnknownServiceError:
            pass
        self._paginators_shape: Optional[Mapping[str, Any]] = None
        try:
            self._paginators_shape = loader.load_service_model(
                service_name.boto3_name, "paginators-1"
            )
        except UnknownServiceError:
            pass
        self._resources_shape: Optional[Mapping[str, Any]] = None
        try:
            self._resources_shape = loader.load_service_model(
                service_name.boto3_name, "resources-1"
            )
        except UnknownServiceError:
            pass

        self.logger = get_logger()
        self.response_metadata_typed_dict = TypeTypedDict(
            "ResponseMetadataTypeDef",
            [
                TypedDictAttribute("RequestId", Type.str, True),
                TypedDictAttribute("HostId", Type.str, True),
                TypedDictAttribute("HTTPStatusCode", Type.int, True),
                TypedDictAttribute("HTTPHeaders", Type.DictStrAny, True),
                TypedDictAttribute("RetryAttempts", Type.int, True),
            ],
        )

    def _get_operation(self, name: str) -> OperationModel:
        return self.service_model.operation_model(name)

    def _get_operation_names(self) -> List[str]:
        return list(self.service_model.operation_names)

    def _get_paginator(self, name: str) -> Dict[str, Any]:
        if not self._paginators_shape:
            raise ShapeParserError(f"Unknown paginator: {name}")
        try:
            return self._paginators_shape["pagination"][name]
        except KeyError as e:
            raise ShapeParserError(f"Unknown paginator: {name}") from e

    def _get_service_resource(self) -> Dict[str, Any]:
        if not self._resources_shape:
            raise ShapeParserError("Resource shape not found")
        return self._resources_shape["service"]

    def _get_resource_shape(self, name: str) -> Dict[str, Any]:
        if not self._resources_shape:
            raise ShapeParserError("Resource shape not found")
        try:
            return self._resources_shape["resources"][name]
        except KeyError as e:
            raise ShapeParserError(f"Unknown resource: {name}") from e

    def get_paginator_names(self) -> List[str]:
        """
        Get available paginator names.

        Returns:
            A list of paginator names.
        """
        result: List[str] = []
        if self._paginators_shape:
            for name in self._paginators_shape.get("pagination", []):
                result.append(name)
        result.sort()
        return result

    def _get_argument_alias(self, operation_name: str, argument_name: str) -> str:
        service_map = self.ARGUMENT_ALIASES.get(self.service_name.boto3_name)
        if not service_map:
            return argument_name

        operation_map: Dict[str, str] = {}
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
    ) -> List[Argument]:
        result: List[Argument] = []
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
                argument_type = self._parse_shape(argument_shape, check_streaming=False)
            argument = Argument(argument_alias, argument_type)
            if argument_name not in required:
                argument.default = Type.none
            if optional_only and argument.required:
                continue
            result.append(argument)

        result.sort(key=lambda x: not x.required)
        return result

    def _parse_return_type(
        self, class_name: str, method_name: str, shape: Optional[Shape]
    ) -> FakeAnnotation:
        argument_type_stub = get_method_type_stub(
            self.service_name, class_name, method_name, "return"
        )
        if argument_type_stub is not None:
            return argument_type_stub

        if shape:
            return self._parse_shape(shape)

        return Type.none

    @staticmethod
    def _get_kw_flags(arguments: Sequence[Argument]) -> List[Argument]:
        if len(arguments) > 2:
            return [Argument.kwflag()]

        return []

    def get_client_method_map(self) -> Dict[str, Method]:
        """
        Get client methods from shape.

        Returns:
            A map of method name to Method.
        """
        result: Dict[str, Method] = {
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
                    Argument("Params", Type.DictStrAny, Type.none),
                    Argument("ExpiresIn", Type.int, TypeConstant(3600)),
                    Argument("HttpMethod", Type.str, Type.none),
                ],
                Type.str,
            ),
        }
        for operation_name in self._get_operation_names():
            operation_model = self._get_operation(operation_name)
            arguments: List[Argument] = [Argument("self", None)]
            method_name = xform_name(operation_name)

            if operation_model.input_shape is not None:
                shape_arguments = self._parse_arguments(
                    "Client",
                    method_name,
                    operation_name,
                    operation_model.input_shape,
                )
                arguments.extend(self._get_kw_flags(shape_arguments))
                arguments.extend(shape_arguments)

            return_type = self._parse_return_type(
                "Client", method_name, operation_model.output_shape
            )

            method = Method(name=method_name, arguments=arguments, return_type=return_type)
            result[method.name] = method
        return result

    def _parse_shape_string(self, shape: StringShape) -> FakeAnnotation:
        if not shape.enum:
            return Type.str

        literal_name = f"{shape.name}Type"
        literal_type_stub = get_literal_type_stub(self.service_name, literal_name)
        if literal_type_stub:
            return literal_type_stub

        return TypeLiteral(f"{shape.name}Type", [option for option in shape.enum])

    def _parse_shape_map(self, shape: MapShape) -> FakeAnnotation:
        type_subscript = TypeSubscript(Type.Dict)
        if shape.key:
            type_subscript.add_child(self._parse_shape(shape.key))
        else:
            type_subscript.add_child(Type.str)
        if shape.value:
            type_subscript.add_child(self._parse_shape(shape.value))
        else:
            type_subscript.add_child(Type.Any)
        return type_subscript

    def _parse_shape_structure(self, shape: StructureShape) -> FakeAnnotation:
        if not shape.members.items():
            return Type.DictStrAny

        required = shape.required_members
        typed_dict_name = f"{shape.name}TypeDef"
        shape_type_stub = get_shape_type_stub(self.service_name, typed_dict_name)
        if shape_type_stub:
            return shape_type_stub

        if typed_dict_name in self._typed_dict_map:
            return self._typed_dict_map[typed_dict_name]
        typed_dict = TypeTypedDict(typed_dict_name)
        self._typed_dict_map[typed_dict_name] = typed_dict
        for attr_name, attr_shape in shape.members.items():
            typed_dict.add_attribute(
                attr_name,
                self._parse_shape(attr_shape),
                attr_name in required,
            )
        if shape.name.endswith("Output"):
            for attribute in typed_dict.children:
                attribute.required = True
            typed_dict.add_attribute(
                "ResponseMetadata",
                self.response_metadata_typed_dict,
                True,
            )
        return typed_dict

    def _parse_shape_list(self, shape: ListShape) -> FakeAnnotation:
        type_subscript = TypeSubscript(Type.List)
        if shape.member:
            type_subscript.add_child(self._parse_shape(shape.member))
        else:
            type_subscript.add_child(Type.Any)
        return type_subscript

    def _parse_shape(self, shape: Shape, check_streaming: bool = True) -> FakeAnnotation:
        if check_streaming and "streaming" in shape.serialization:
            if shape.serialization["streaming"]:
                return TypeClass(StreamingBody)
            return Type.bytes

        if shape.type_name in self.SHAPE_TYPE_MAP:
            return self.SHAPE_TYPE_MAP[shape.type_name]

        if isinstance(shape, StringShape):
            return self._parse_shape_string(shape)

        if isinstance(shape, MapShape):
            return self._parse_shape_map(shape)

        if isinstance(shape, StructureShape):
            return self._parse_shape_structure(shape)

        if isinstance(shape, ListShape):
            return self._parse_shape_list(shape)

        if self._resources_shape and shape.type_name in self._resources_shape["resources"]:
            return AliasInternalImport(shape.type_name)

        self.logger.warning(f"Unknown shape: {shape}")
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
        skip_argument_names: List[str] = []
        input_token = paginator_shape["input_token"]
        if isinstance(input_token, list):
            skip_argument_names.extend(input_token)
        else:
            skip_argument_names.append(input_token)
        if "limit_key" in paginator_shape:
            skip_argument_names.append(paginator_shape["limit_key"])

        arguments: List[Argument] = [Argument("self", None)]

        if operation_shape.input_shape is not None:
            shape_arguments = self._parse_arguments(
                "Paginator",
                "paginate",
                operation_name,
                operation_shape.input_shape,
                exclude_names=skip_argument_names,
            )
            shape_arguments.append(Argument("PaginationConfig", paginator_config_type, Type.none))
            arguments.extend(self._get_kw_flags(shape_arguments))
            arguments.extend(shape_arguments)

        return_type: FakeAnnotation = Type.none
        if operation_shape.output_shape is not None:
            return_type = TypeSubscript(
                Type.Iterator,
                [
                    self._parse_return_type("Paginator", "paginate", operation_shape.output_shape),
                ],
            )

        return Method("paginate", arguments, return_type)

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

        arguments: List[Argument] = [Argument("self", None)]

        if operation_shape.input_shape is not None:
            shape_arguments = self._parse_arguments(
                "Waiter", "wait", operation_name, operation_shape.input_shape
            )
            shape_arguments.append(Argument("WaiterConfig", waiter_config_type, Type.none))
            arguments.extend(self._get_kw_flags(shape_arguments))
            arguments.extend(shape_arguments)

        return Method(name="wait", arguments=arguments, return_type=Type.none)

    def get_service_resource_method_map(self) -> Dict[str, Method]:
        """
        Get methods for ServiceResource.

        Returns:
            A map of method name to Method.
        """
        result: Dict[str, Method] = {
            "get_available_subresources": Method(
                "get_available_subresources",
                [Argument("self", None)],
                TypeSubscript(Type.List, [Type.str]),
            ),
        }
        service_resource_shape = self._get_service_resource()
        for action_name, action_shape in service_resource_shape.get("actions", {}).items():
            method = self._get_resource_method("ServiceResource", action_name, action_shape)
            result[method.name] = method

        return result

    def get_resource_method_map(self, resource_name: str) -> Dict[str, Method]:
        """
        Get methods for Resource.

        Arguments:
            resource_name -- Resource name.

        Returns:
            A map of method name to Method.
        """
        resource_shape = self._get_resource_shape(resource_name)
        result: Dict[str, Method] = {
            "get_available_subresources": Method(
                "get_available_subresources",
                [Argument("self", None)],
                TypeSubscript(Type.List, [Type.str]),
            ),
            "load": Method("load", [Argument("self", None)], Type.none),
            "reload": Method("reload", [Argument("self", None)], Type.none),
        }

        for action_name, action_shape in resource_shape.get("actions", {}).items():
            method = self._get_resource_method(resource_name, action_name, action_shape)
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
        if "[" not in target:
            return target
        return target.split("[")[0]

    def _get_resource_method(
        self, resource_name: str, action_name: str, action_shape: Dict[str, Any]
    ) -> Method:
        return_type: FakeAnnotation = Type.none
        method_name = xform_name(action_name)
        arguments: List[Argument] = [Argument("self", None)]
        if "resource" in action_shape:
            return_type = self._parse_return_type(
                resource_name, method_name, Shape("resource", action_shape["resource"])
            )
            path = action_shape["resource"].get("path", "")
            if path.endswith("[]"):
                return_type = TypeSubscript(Type.List, [return_type])

        if "request" in action_shape:
            operation_name = action_shape["request"]["operation"]
            operation_shape = self._get_operation(operation_name)
            skip_argument_names = set(
                self._get_arg_from_target(i["target"])
                for i in action_shape["request"].get("params", {})
                if i["source"] == "identifier"
            )
            if operation_shape.input_shape is not None:
                shape_arguments = self._parse_arguments(
                    resource_name,
                    method_name,
                    operation_name,
                    operation_shape.input_shape,
                    exclude_names=skip_argument_names,
                )
                arguments.extend(self._get_kw_flags(shape_arguments))
                arguments.extend(shape_arguments)
            if operation_shape.output_shape is not None and return_type is Type.none:
                operation_return_type = self._parse_shape(operation_shape.output_shape)
                return_type = operation_return_type

        return Method(name=method_name, arguments=arguments, return_type=return_type)

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
        result = Method("filter", [Argument("self", None)], self_type)
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
            result.arguments.extend(self._get_kw_flags(shape_arguments))
            result.arguments.extend(shape_arguments)

        return result

    def get_collection_batch_methods(self, name: str, collection: Collection) -> List[Method]:
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
            method = Method(batch_action.name, [Argument("self", None)], Type.none)
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
                    method.arguments.extend(self._get_kw_flags(shape_arguments))
                    method.arguments.extend(shape_arguments)
                if operation_model.output_shape is not None:
                    return_type = self._parse_shape(operation_model.output_shape)
                    method.return_type = return_type

        return result
