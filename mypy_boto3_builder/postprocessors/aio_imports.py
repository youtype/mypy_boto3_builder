"""
Import replacement map for aio libraries.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final

from botocore.client import BaseClient
from botocore.config import Config
from botocore.eventstream import EventStream
from botocore.paginate import PageIterator, Paginator
from botocore.response import StreamingBody
from botocore.waiter import Waiter

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.type_annotations.external_import import ExternalImport

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


def replace_import_with_aio(external_import: ExternalImport) -> None:
    """
    Replace botocore/boto3 import with aioboto3/aiobotocore.
    """
    if external_import not in AIO_IMPORT_MAP:
        return
    new_external_import = AIO_IMPORT_MAP[external_import]
    external_import.copy_from(new_external_import)
