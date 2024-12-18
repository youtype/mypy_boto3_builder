"""
Lookup dictionary to get values by multiple keys.

Copyright 2024 Vlad Emelianov
"""

import itertools
from collections.abc import Iterator, Mapping
from typing import ClassVar, Generic, TypeVar, cast

from mypy_boto3_builder.constants import ALL

_T = TypeVar("_T")
_V = TypeVar("_V")


class LookupDict(Generic[_V]):
    """
    Lookup dictionary to get values by multiple keys.

    Supports "*" as a wildcard key in a lookup dict.

    Arguments:
        hash_map -- Lookup hash map.
    """

    _ALL: ClassVar = ALL

    def __init__(
        self,
        items: Mapping[str, _T],
    ) -> None:
        self._items = items
        self._lookup_items: dict[tuple[str, ...], _V] = {}
        self._keys_len = 0
        self._products: tuple[tuple[bool, ...], ...] = ()

    @property
    def _lookup(self) -> dict[tuple[str, ...], _V]:
        if not self._lookup_items:
            self._lookup_items = self._generate_lookup({str(k): v for k, v in self._items.items()})
            self._keys_len = len(next(iter(self._lookup_items)))
            self._products = tuple(self._generate_products())

        return self._lookup_items

    def _generate_products(self) -> Iterator[tuple[bool, ...]]:
        static_keys = tuple(
            not any(keys[i] == self._ALL for keys in self._lookup_items)
            for i in range(self._keys_len)
        )
        if all(static_keys):
            yield static_keys
            return

        shifting_keys_count = static_keys.count(False)
        products = itertools.product((True, False), repeat=shifting_keys_count)
        for product in products:
            product_iter = iter(product)
            yield tuple(True if key else next(product_iter) for key in static_keys)

    def _generate_lookup(self, hash_map: Mapping[str, _T]) -> dict[tuple[str, ...], _V]:
        result: dict[tuple[str, ...], _V] = {}
        stack: list[tuple[Mapping[str, _T], tuple[str, ...]]] = [(hash_map, ())]

        while stack:
            current_map, current_keys = stack.pop()
            for key, value in current_map.items():
                new_keys = (*current_keys, key)
                if isinstance(value, Mapping):
                    value_t = cast("Mapping[str, _T]", value)
                    stack.append((value_t, new_keys))
                else:
                    value_v = cast("_V", value)
                    result[new_keys] = value_v

        return result

    def _iterate_lookup_keys(self, keys: tuple[str, ...]) -> Iterator[tuple[str, ...]]:
        if len(keys) != self._keys_len:
            raise ValueError(f"Got {len(keys)}, {self._keys_len} expected: {keys}")

        for product in self._products:
            yield tuple(
                key if is_static else self._ALL
                for is_static, key in zip(product, keys, strict=True)
            )

    def get(self, *keys: str) -> _V | None:
        """
        Get value by multiple keys.
        """
        lookup = self._lookup
        for lookup_keys in self._iterate_lookup_keys(keys):
            result = lookup.get(lookup_keys)
            if result is not None:
                return result
        return None
