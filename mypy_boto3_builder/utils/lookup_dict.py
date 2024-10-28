"""
Lookup dictionary to get values by multiple keys.
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

    Arguments:
        hash_map -- Initial hash map.
        required_keys -- Number of required keys in th end of key tuple.
    """

    _ALL: ClassVar = ALL

    def __init__(
        self,
        hash_map: Mapping[str, _T],
    ) -> None:
        self._hash_map = hash_map
        self._lookup_hash_map: dict[tuple[str, ...], _V] = {}
        self._keys_len = 0
        self._products: tuple[tuple[bool, ...], ...] = ()

    @property
    def _lookup(self) -> dict[tuple[str, ...], _V]:
        if not self._lookup_hash_map:
            self._lookup_hash_map = self._generate_lookup(
                {str(k): v for k, v in self._hash_map.items()}, ()
            )
            self._keys_len = len(next(iter(self._lookup_hash_map)))
            self._products = self._generate_products()

        return self._lookup_hash_map

    def _generate_products(self) -> tuple[tuple[bool, ...], ...]:
        static_keys = [True for _i in range(self._keys_len)]
        for keys in self._lookup_hash_map:
            for i, key in enumerate(keys):
                if key == self._ALL:
                    static_keys[i] = False

        frozen_static_keys = tuple(static_keys)
        if all(frozen_static_keys):
            return (frozen_static_keys,)

        shifting_keys_count = len([key for key in static_keys if not key])
        products = tuple(itertools.product((True, False), repeat=shifting_keys_count))
        return tuple(self._join_product(frozen_static_keys, product) for product in products)

    @staticmethod
    def _join_product(static_keys: tuple[bool, ...], product: tuple[bool, ...]) -> tuple[bool, ...]:
        product_iter = iter(product)
        return tuple(True if key else next(product_iter) for key in static_keys)

    def _generate_lookup(
        self, hash_map: Mapping[str, _T], keys: tuple[str, ...]
    ) -> dict[tuple[str, ...], _V]:
        result: dict[tuple[str, ...], _V] = {}
        for key, value in hash_map.items():
            new_keys = (*keys, key)
            if isinstance(value, Mapping):
                value = cast(Mapping[str, _T], value)  # type: ignore
                result.update(self._generate_lookup(value, new_keys))
            else:
                value_v = cast(_V, value)  # type: ignore
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
