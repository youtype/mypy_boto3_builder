"""
Boto3 ServiceResource collections parser, produces `structures.Collection`.
"""
from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.utils.strings import get_class_prefix


def parse_collections(
    parent_name: str,
    resource: Boto3ServiceResource,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> list[Collection]:
    """
    Extract collections from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Collection structures.
    """
    result: list[Collection] = []
    for collection in resource.meta.resource_model.collections:
        if not collection.resource:
            continue
        object_class_name = collection.resource.type
        collection_record = Collection(
            name=f"{parent_name}{get_class_prefix(collection.name)}Collection",
            parent_name=parent_name,
            attribute_name=collection.name,
            service_name=service_name,
            type_annotation=InternalImport(collection.name),
            object_class_name=object_class_name,
        )
        self_type = InternalImport(collection_record.name, stringify=True)

        collection_record.methods.append(
            Method(
                name="all",
                arguments=[Argument("self", None)],
                return_type=self_type,
                docstring=(
                    "Get all items from the collection, optionally"
                    " with a custom page size and item count limit."
                ),
            )
        )
        filter_method = shape_parser.get_collection_filter_method(
            collection_record.name, collection, self_type
        )
        filter_method.docstring = (
            "Get items from the collection, passing keyword arguments along"
            " as parameters to the underlying service operation, which are"
            " typically used to filter the results."
        )
        filter_method.type_ignore = True
        collection_record.methods.append(filter_method)
        batch_methods = shape_parser.get_collection_batch_methods(
            collection_record.name, collection
        )
        for batch_method in batch_methods:
            batch_method.docstring = "Batch method."
            collection_record.methods.append(batch_method)
        collection_record.methods.append(
            Method(
                "limit",
                [Argument("self", None), Argument("count", Type.int)],
                self_type,
                docstring=f"Return at most this many {object_class_name}s.",
            )
        )
        collection_record.methods.append(
            Method(
                "page_size",
                [Argument("self", None), Argument("count", Type.int)],
                self_type,
                docstring=f"Fetch at most this many {object_class_name}s per service request.",
            )
        )
        collection_record.methods.append(
            Method(
                "pages",
                [Argument("self", None)],
                TypeSubscript(
                    Type.Iterator,
                    [TypeSubscript(Type.List, [InternalImport(name=object_class_name)])],
                ),
                docstring=f"A generator which yields pages of {object_class_name}s.",
            )
        )
        collection_record.methods.append(
            Method(
                "__iter__",
                [Argument("self", None)],
                TypeSubscript(Type.Iterator, [InternalImport(name=object_class_name)]),
                docstring=f"A generator which yields {object_class_name}s.",
            )
        )

        result.append(collection_record)
    return result
