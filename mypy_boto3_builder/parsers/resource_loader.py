"""
Loader for botocore resource shapes.

Copyright 2024 Vlad Emelianov
"""

import contextlib
import importlib
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any, ClassVar, TypeVar, cast

from botocore.exceptions import UnknownServiceError
from botocore.loaders import Loader

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.shape_parser_types import (
    PaginatorsShape,
    ResourcesShape,
    WaitersShape,
)
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.boto3_utils import get_botocore_session

_T = TypeVar("_T")


class ResourceLoader:
    """
    Loader for botocore resource shapes.
    """

    SERVICE_RESOURCE_KEY = "service"
    WAITERS_KEY = "waiters-2"
    PAGINATORS_KEY = "paginators-1"
    RESOURCES_KEY = "resources-1"
    _loader: ClassVar[Loader | None] = None
    _cache: ClassVar[dict[str, Mapping[str, Any] | None]] = {}

    @classmethod
    def _get_loader(cls) -> Loader:
        if cls._loader:
            return cls._loader
        botocore_session = get_botocore_session()
        loader: Loader = botocore_session.get_component("data_loader")
        cls._loader = loader
        cls._inject_boto3_path()
        return loader

    @classmethod
    def _inject_boto3_path(cls) -> None:
        """
        Backport of `boto3/session.py` `Session._setup_loader` method.
        """
        boto3_module = None
        with contextlib.suppress(ModuleNotFoundError):
            boto3_module = importlib.import_module("boto3")

        if not boto3_module:
            get_logger().debug("boto3 module not found, skipping resources injection")
            return

        if not boto3_module.__file__:
            get_logger().warning(
                "boto3 module __file__ is not defined, skipping resources injection"
            )
            return

        path = Path(boto3_module.__file__).parent / "data"
        if not cls._loader:
            raise ValueError("Loader is not initialized")
        cls._loader.search_paths.append(path.as_posix())

    def _load_resource(
        self, service_name: ServiceName, type_name: str, _response_type: type[_T]
    ) -> _T | None:
        cache_key = f"{service_name.boto3_name}.{type_name}"
        if cache_key in self._cache:
            return cast("_T | None", self._cache[cache_key])
        loader = self._get_loader()
        data: dict[str, Any] | None = None
        with contextlib.suppress(UnknownServiceError):
            data = loader.load_service_model(service_name.boto3_name, type_name)

        self._cache[cache_key] = data
        return cast("_T | None", data)

    def load_waiters(self, service_name: ServiceName) -> WaitersShape | None:
        """
        Load waiters shape.
        """
        return self._load_resource(service_name, self.WAITERS_KEY, WaitersShape)

    def load_paginators(self, service_name: ServiceName) -> PaginatorsShape | None:
        """
        Load paginators shape.
        """
        return self._load_resource(service_name, self.PAGINATORS_KEY, PaginatorsShape)

    def load_resources(self, service_name: ServiceName) -> ResourcesShape | None:
        """
        Load resources shape.
        """
        return self._load_resource(service_name, self.RESOURCES_KEY, ResourcesShape)

    def has_service_resource(self, service_name: ServiceName) -> bool:
        """
        Check if service has ServiceResource.
        """
        resources = self.load_resources(service_name)
        if not resources:
            return False
        return self.SERVICE_RESOURCE_KEY in resources

    def get_resource_service_names(self, service_names: Iterable[ServiceName]) -> list[ServiceName]:
        """
        Get service names that have a ServiceResource.
        """
        return [
            service_name
            for service_name in service_names
            if self.has_service_resource(service_name)
        ]
