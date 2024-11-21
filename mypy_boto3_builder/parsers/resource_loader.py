"""
Loader for botocore resource shapes.

Copyright 2024 Vlad Emelianov
"""

import contextlib
from typing import Any, ClassVar, cast

from botocore.exceptions import UnknownServiceError
from botocore.loaders import Loader

from mypy_boto3_builder.parsers.shape_parser_types import (
    PaginatorsShape,
    ResourcesShape,
    WaitersShape,
)
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.boto3_utils import get_boto3_session, get_botocore_session


class ResourceLoader:
    """
    Loader for botocore resource shapes.
    """

    SERVICE_RESOURCE_KEY = "service"
    _loader: ClassVar[Loader | None] = None
    _cache: ClassVar[dict[str, dict[str, Any] | None]] = {}

    @classmethod
    def _get_loader(cls) -> Loader:
        if cls._loader:
            return cls._loader
        # FIXME: side-load boto3 resources
        get_boto3_session()
        botocore_session = get_botocore_session()
        loader: Loader = botocore_session.get_component("data_loader")
        cls._loader = loader
        return loader

    def _load_resource(self, service_name: ServiceName, type_name: str) -> dict[str, Any] | None:
        cache_key = f"{service_name.boto3_name}.{type_name}"
        # if cache_key in self._cache:
        #     return self._cache[cache_key]
        loader = self._get_loader()
        data: dict[str, Any] | None = None
        with contextlib.suppress(UnknownServiceError):
            data = loader.load_service_model(service_name.boto3_name, type_name)

        self._cache[cache_key] = data
        return data

    def load_waiters(self, service_name: ServiceName) -> WaitersShape | None:
        """
        Load waiters shape.
        """
        return cast(WaitersShape | None, self._load_resource(service_name, "waiters-2"))

    def load_paginators(self, service_name: ServiceName) -> PaginatorsShape | None:
        """
        Load paginators shape.
        """
        return cast(PaginatorsShape | None, self._load_resource(service_name, "paginators-2"))

    def load_resources(self, service_name: ServiceName) -> ResourcesShape | None:
        """
        Load resources shape.
        """
        return cast(ResourcesShape | None, self._load_resource(service_name, "resources-1"))

    def has_service_resource(self, service_name: ServiceName) -> bool:
        """
        Check if service has ServiceResource.
        """
        resources = self.load_resources(service_name)
        if not resources:
            return False
        return self.SERVICE_RESOURCE_KEY in resources
