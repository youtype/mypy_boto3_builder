"""
Boto3 ServiceResource collections parser, produces `structures.Collection`.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.boto3_ports.model import Collection as Boto3Collection
from mypy_boto3_builder.boto3_ports.model import ResourceModel
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.utils.strings import get_class_prefix


def parse_collection(
    collection: Boto3Collection,
    service_name: ServiceName,
    resource_name: str,
    shape_parser: ShapeParser,
) -> Collection:
    """
    Parse Collection from boto3 resource.

    Arguments:
        collection -- Boto3 collection.
        service_name -- Service name.
        resource_name -- Resource name.
        shape_parser -- Shape parser.
    """
    if not collection.resource:
        raise ValueError(f"Collection {collection.name} does not have resource")
    object_class_name = collection.resource.type
    collection_record = Collection(
        name=f"{resource_name}{get_class_prefix(collection.name)}Collection",
        parent_name=resource_name,
        attribute_name=collection.name,
        service_name=service_name,
        type_annotation=InternalImport(collection.name),
        object_class_name=object_class_name,
    )
    self_type = InternalImport(collection_record.name)

    # FIXME: other collection methods use different anchor format. This will probably change.
    all_method = Method(
        name="all",
        arguments=(Argument.self(),),
        return_type=self_type,
        docstring=(
            "Get all items from the collection, optionally"
            " with a custom page size and item count limit."
        ),
        boto3_doc_link=f"{collection_record.boto3_doc_link_parent}#{service_name.class_name}.{collection_record.parent_name}.all",
    )

    collection_record.methods.append(all_method)
    filter_method = shape_parser.get_collection_filter_method(
        collection_record.name,
        collection,
        self_type,
    )
    filter_method.docstring = (
        "Get items from the collection, passing keyword arguments along"
        " as parameters to the underlying service operation, which are"
        " typically used to filter the results."
    )
    filter_method.type_ignore = "override"
    collection_record.methods.append(filter_method)
    batch_methods = shape_parser.get_collection_batch_methods(collection_record.name, collection)
    for batch_method in batch_methods:
        batch_method.docstring = "Batch method."
        collection_record.methods.append(batch_method)

    extra_methods = (
        Method(
            name="limit",
            arguments=[Argument.self(), Argument("count", Type.int)],
            return_type=self_type,
            docstring=f"Return at most this many {object_class_name}s.",
        ),
        Method(
            name="page_size",
            arguments=[Argument.self(), Argument("count", Type.int)],
            return_type=self_type,
            docstring=f"Fetch at most this many {object_class_name}s per service request.",
        ),
        Method(
            name="pages",
            arguments=[Argument.self()],
            return_type=TypeSubscript(
                Type.Iterator,
                [Type.wrap_list(InternalImport(name=object_class_name))],
            ),
            docstring=f"A generator which yields pages of {object_class_name}s.",
        ),
        Method(
            name="__iter__",
            arguments=[Argument.self()],
            return_type=TypeSubscript(Type.Iterator, [InternalImport(name=object_class_name)]),
            docstring=f"A generator which yields {object_class_name}s.",
        ),
    )
    collection_record.methods.extend(extra_methods)
    return collection_record


def parse_collections(
    service_name: ServiceName,
    resource_name: str,
    resource_model: ResourceModel,
    shape_parser: ShapeParser,
) -> list[Collection]:
    """
    Extract collections from boto3 resource.

    Arguments:
        service_name -- Service name.
        resource_name -- Resource name.
        resource -- boto3 service resource.
        shape_parser -- Shape parser.
    """
    result: list[Collection] = []
    for collection in resource_model.collections:
        if not collection.resource:
            continue
        collection_record = parse_collection(collection, service_name, resource_name, shape_parser)
        result.append(collection_record)
    return result
