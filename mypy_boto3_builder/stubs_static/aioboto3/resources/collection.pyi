import logging
from typing import Any, Iterator, List

from boto3.resources.base import ServiceResource
from boto3.resources.collection import CollectionFactory, CollectionManager, ResourceCollection
from boto3.resources.factory import ResourceFactory
from boto3.resources.model import Collection
from boto3.utils import ServiceContext
from botocore.hooks import BaseEventHooks

logger: logging.Logger

class AIOResourceCollection(ResourceCollection):
    """
    Converted the ResourceCollection.pages() function to an async generator so that we can do
    async for on a paginator inside that function

    Converted the __iter__
    """

    async def __anext__(self) -> Iterator[Any]: ...
    def __aiter__(self) -> Iterator[Any]: ...
    def __iter__(self) -> Iterator[Any]: ...
    async def pages(self) -> Iterator[List[Any]]: ...  # type: ignore [override]

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
