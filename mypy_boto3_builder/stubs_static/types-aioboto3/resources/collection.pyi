"""
Type annotations for aioboto3.resources.collection module.

Copyright 2024 Vlad Emelianov
"""

import logging
from typing import Any, AsyncIterator, NoReturn

from boto3.resources.base import ServiceResource
from boto3.resources.collection import CollectionFactory, CollectionManager, ResourceCollection
from boto3.resources.factory import ResourceFactory
from boto3.resources.model import Collection
from boto3.utils import ServiceContext
from botocore.hooks import BaseEventHooks

logger: logging.Logger

class AIOResourceCollection(ResourceCollection):
    def __anext__(self) -> AsyncIterator[Any]: ...
    def __aiter__(self) -> AsyncIterator[Any]: ...
    def __iter__(self) -> NoReturn: ...
    def pages(self) -> AsyncIterator[list[Any]]: ...  # type: ignore[override]

class AIOCollectionManager(CollectionManager):
    def __init__(
        self,
        collection_model: Collection,
        parent: ServiceResource,
        factory: ResourceFactory,
        service_context: ServiceContext,
    ) -> None: ...

class AIOCollectionFactory(CollectionFactory):
    def load_from_definition(
        self,
        resource_name: str,
        collection_model: Collection,
        service_context: ServiceContext,
        event_emitter: BaseEventHooks,
    ) -> AIOCollectionManager: ...
