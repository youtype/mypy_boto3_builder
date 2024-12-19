"""
Import replacement map for aio libraries.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator, Mapping
from typing import Final

from botocore.client import BaseClient
from botocore.config import Config
from botocore.eventstream import EventStream
from botocore.paginate import PageIterator, Paginator
from botocore.response import StreamingBody
from botocore.waiter import Waiter

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.utils.type_checks import is_external_import

AIO_IMPORT_MAP: Final[Mapping[ExternalImport, ExternalImport]] = {
    ExternalImport.from_class(StreamingBody): ExternalImport(
        Import.aiobotocore + "response", "StreamingBody"
    ),
    ExternalImport.from_class(EventStream): ExternalImport(
        Import.aiobotocore + "eventstream", "AioEventStream"
    ),
    ExternalImport.from_class(Config): ExternalImport(Import.aiobotocore + "config", "AioConfig"),
    ExternalImport.from_class(Waiter): ExternalImport(Import.aiobotocore + "waiter", "AIOWaiter"),
    ExternalImport.from_class(Paginator): ExternalImport(
        Import.aiobotocore + "paginate", "AioPaginator"
    ),
    ExternalImport.from_class(PageIterator): ExternalImport(
        Import.aiobotocore + "paginate", "AioPageIterator"
    ),
    ExternalImport.from_class(BaseClient): ExternalImport(
        Import.aiobotocore + "client", "AioBaseClient"
    ),
    ExternalImport(Import.boto3 + "resources" + "base", "ServiceResource"): ExternalImport(
        Import.aioboto3 + "resources" + "base", "AIOBoto3ServiceResource"
    ),
    ExternalImport(Import.boto3 + "resources" + "collection", "ResourceCollection"): ExternalImport(
        Import.aioboto3 + "resources" + "collection", "AIOResourceCollection"
    ),
    ExternalImport(Import.boto3 + "dynamodb" + "table", "BatchWriter"): ExternalImport(
        Import.aioboto3 + "dynamodb" + "table", "BatchWriter"
    ),
    ExternalImport(Import.boto3 + "dynamodb" + "table", "TableResource"): ExternalImport(
        Import.aioboto3 + "dynamodb" + "table", "CustomTableResource"
    ),
}


def replace_imports_with_aio(type_annotations: Iterator[FakeAnnotation]) -> None:
    """
    Replace botocore/boto3 imports in type annotations with aioboto3/aiobotocore.
    """
    for type_annotation in type_annotations:
        if not is_external_import(type_annotation):
            continue

        if type_annotation in AIO_IMPORT_MAP:
            new_type_annotation = AIO_IMPORT_MAP[type_annotation]
            type_annotation.copy_from(new_type_annotation)
            continue
