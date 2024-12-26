"""
InstallRequires container.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

from mypy_boto3_builder.utils.version import sort_versions


@dataclass
class InstallRequiresItem:
    """
    Item for install_requires.
    """

    name: str
    drop_python_version: str | None = None
    min_version: str | None = None

    def __hash__(self) -> int:
        """
        Calculate hash value.
        """
        return hash(self.name)

    @classmethod
    def parse(cls, item: str) -> "InstallRequiresItem":
        """
        Parse item from string.
        """
        name = item
        min_version: str | None = None
        drop_python_version: str | None = None
        if ">=" in name:
            name, min_version = name.split(">=")

        if "; python_version<" in name:
            name, drop_python_version = name.split("; python_version<")
            drop_python_version = drop_python_version.replace('"', "")

        return cls(name=name, min_version=min_version, drop_python_version=drop_python_version)

    def render(self) -> str:
        """
        Render item to a valid install_requires string for setup.py.
        """
        version = f">={self.min_version}" if self.min_version else ""

        python_version = ""
        if self.drop_python_version:
            python_version = f'; python_version<"{self.drop_python_version}"'

        return f"{self.name}{version}{python_version}"


class InstallRequires:
    """
    InstallRequires container.
    """

    def __init__(self, items: Iterable[InstallRequiresItem | str] = ()) -> None:
        self.items: list[InstallRequiresItem] = []
        self.add(*items)

    def __bool__(self) -> bool:
        """
        Whether install_requires is not empty.
        """
        return bool(self.items)

    def get(self, name: str) -> InstallRequiresItem | None:
        """
        Get item by name.
        """
        for item in self.items:
            if item.name == name:
                return item
        return None

    def update(self, other: "InstallRequires") -> None:
        """
        Update install_requires with another one.
        """
        for item in other.items:
            self.add(item)

    def add(self, *raw_items: InstallRequiresItem | str) -> None:
        """
        Add item to install_requires.
        """
        for raw_item in raw_items:
            item = InstallRequiresItem.parse(raw_item) if isinstance(raw_item, str) else raw_item
            old_item = self.get(item.name)
            if not old_item:
                self.items.append(item)
                continue

            drop_python_versions = sort_versions(
                filter(None, (item.drop_python_version, old_item.drop_python_version))
            )
            min_versions = sort_versions(filter(None, (item.min_version, old_item.min_version)))

            old_item.drop_python_version = (
                drop_python_versions[-1] if drop_python_versions else None
            )
            old_item.min_version = min_versions[-1] if min_versions else None

    def iterate_items(self) -> Iterator[InstallRequiresItem]:
        """
        Iterate over all items for rendering.
        """
        yield from sorted(self.items, key=lambda x: x.name)

    def clear(self) -> None:
        """
        Clear install_requires.
        """
        self.items = []
